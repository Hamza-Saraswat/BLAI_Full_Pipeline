#!/usr/bin/env python3
"""normalize_narration.py — spoken-form normalizer for the BLAI voiceover stage.

The storyboard writer is supposed to spell numbers out ("twenty-seven billion",
not "27B"). That is a convention, and conventions leak: a sweep of the 25-board
corpus found 44 raw tokens that reached the TTS engine unexpanded — "27B",
"RTX 4090", "HIPAA", "EPYC", "NVMe", "7200-RPM" and friends. Kokoro then says
"twenty-seven bee".

This is the deterministic safety net. It never edits storyboard.json — it
produces the SPOKEN text that gets handed to the engine, plus a per-scene
sidecar so caption alignment measures drift against what was actually said.

    # pipeline use (writes both artifacts)
    python3 skills/script-gates/scripts/normalize_narration.py \
        --storyboard <dir>/<slug>-storyboard.json \
        --out-txt   <dir>/<slug>-narration.txt \
        --out-json  <dir>/<slug>-narration.norm.json

    # ad-hoc
    python3 skills/script-gates/scripts/normalize_narration.py --text "A 27B model on an RTX 4090."
    python3 skills/script-gates/scripts/normalize_narration.py --self-test

Rules live in skills/script-gates/tts_lexicon.json (producer-editable; v2 port
of pipeline/tts_lexicon.json). normalize_text() is idempotent: every replacement
produces digit-free, non-ALL-CAPS output, so re-running it is a no-op. That is
what lets the voice stage normalize defensively without double-expanding text
the pipeline already normalized.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# v2 port: scripts/ -> skills/script-gates/ -> skills/ -> repo root
SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_LEXICON = SKILL_DIR / "tts_lexicon.json"  # repointed from pipeline/tts_lexicon.json

# --- number spelling (copied from the sibling eval_short.py, which is a
# --- deliberately self-contained single file; keep the two in sync by hand) ---
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
SCALES = [(1_000_000_000, "billion"), (1_000_000, "million"), (1_000, "thousand")]


def int_to_words(n) -> str:
    n = int(n)
    if n < 0:
        return "minus " + int_to_words(-n)
    if n < 20:
        return ONES[n]
    if n < 100:
        t, r = divmod(n, 10)
        return TENS[t] + ("" if r == 0 else " " + ONES[r])
    if n < 1000:
        h, r = divmod(n, 100)
        return ONES[h] + " hundred" + ("" if r == 0 else " " + int_to_words(r))
    for scale, name in SCALES:
        if n >= scale:
            major, rest = divmod(n, scale)
            out = int_to_words(major) + " " + name
            if rest:
                out += " " + int_to_words(rest)
            return out
    return str(n)


def decimal_to_words(s: str) -> str:
    """'2.7' -> 'two point seven'; '0.5' -> 'zero point five'."""
    whole, _, frac = s.partition(".")
    out = int_to_words(whole or 0)
    if frac:
        out += " point " + " ".join(int_to_words(d) for d in frac)
    return out


def year_to_words(n: int) -> str:
    """1900-2099 read as pairs: 2026 -> 'twenty twenty six'; 2005 -> 'two thousand five'."""
    hi, lo = divmod(n, 100)
    if lo == 0:
        return int_to_words(hi) + " hundred"
    if lo < 10:
        return int_to_words(n)  # 2005 -> "two thousand five"
    return int_to_words(hi) + " " + int_to_words(lo)


def spell_out(token: str) -> str:
    """'GLM' -> 'G L M' (letters spaced so the engine reads them individually)."""
    return " ".join(ch for ch in token if ch.isalnum())


# A number is either grouped ("100,000") or plain ("512"), optionally with a
# decimal tail. Written this way so a trailing comma in prose ("512, EPYC")
# is NOT swallowed into the number.
NUM = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?"


def load_lexicon(path: Path | str | None = None) -> dict:
    p = Path(path) if path else DEFAULT_LEXICON
    try:
        with open(p, "r", encoding="utf-8") as f:
            lex = json.load(f)
    except Exception:
        return {"keep": [], "say": {}, "units": {}}
    lex.setdefault("keep", [])
    lex.setdefault("say", {})
    lex.setdefault("units", {})
    return lex


def normalize_text(text: str, lex: dict | None = None) -> str:
    """Rewrite narration into the form we want the TTS engine to read aloud."""
    if not text:
        return text
    lex = lex if lex is not None else load_lexicon()
    say: dict = lex.get("say", {})
    units: dict = lex.get("units", {})
    keep = set(lex.get("keep", []))
    out = text

    # 1. say map — longest key first so "RTX 4090" wins over "RTX"/"4090".
    for key in sorted(say, key=len, reverse=True):
        pat = r"(?<![A-Za-z0-9])" + re.escape(key) + r"(?![A-Za-z0-9])"
        out = re.sub(pat, say[key].replace("\\", "\\\\"), out)

    # 2. money: $4,000 / $4.5 billion -> spoken dollars
    def _money(m: re.Match) -> str:
        num = m.group(1).replace(",", "")
        scale = (m.group(2) or "").strip()
        words = decimal_to_words(num) if "." in num else int_to_words(num)
        scale_word = {"B": "billion", "M": "million", "K": "thousand"}.get(scale, scale)
        tail = f" {scale_word}" if scale_word else ""
        return f"{words}{tail} dollars"

    # The whitespace belongs inside the optional scale group; v1 let `\s*` swallow
    # the space after a bare amount ("$4,000 in" became "dollarsin").
    out = re.sub(rf"\$({NUM})(?:\s*(billion|million|thousand|B|M|K))?\b", _money, out)

    # 3. number + unit: 24GB, 273 GB/s, 7200-RPM, 2.5x, 90%
    if units:
        unit_alt = "|".join(sorted((re.escape(u) for u in units), key=len, reverse=True))

        def _unit(m: re.Match) -> str:
            num, unit = m.group(1), m.group(2)
            words = decimal_to_words(num) if "." in num else int_to_words(num.replace(",", ""))
            return f"{words} {units[unit]}"

        out = re.sub(rf"(?<![A-Za-z0-9])({NUM})[\s-]?({unit_alt})(?![A-Za-z0-9])",
                     _unit, out)

    # 4. letter + digits model tokens not caught by the lexicon: A100, H200, K3
    def _model(m: re.Match) -> str:
        return f"{m.group(1)} {int_to_words(m.group(2))}"

    out = re.sub(r"(?<![A-Za-z0-9])([A-Z])(\d{1,4})(?![A-Za-z0-9])", _model, out)

    # 5. plain numbers: decimals, years, comma ints, bare ints
    out = re.sub(r"(?<![A-Za-z0-9.])(\d+\.\d+)(?![A-Za-z0-9])",
                 lambda m: decimal_to_words(m.group(1)), out)

    def _int(m: re.Match) -> str:
        raw = m.group(1).replace(",", "")
        n = int(raw)
        if 1900 <= n <= 2099 and len(raw) == 4:
            return year_to_words(n)
        return int_to_words(n)

    out = re.sub(rf"(?<![A-Za-z0-9.])({NUM})(?![A-Za-z0-9])", _int, out)

    # 6. safety net: any remaining ALL-CAPS token gets spelled out. The trailing
    # `s?` keeps plurals whole ("GPUs"), otherwise the engine backtracks to "GP"
    # and the keep-list never matches.
    def _caps(m: re.Match) -> str:
        tok = m.group(1)
        if tok in keep:
            return tok
        if tok.endswith("s") and tok[:-1].isupper():
            return spell_out(tok[:-1]) + "'s"
        return spell_out(tok)

    out = re.sub(r"(?<![A-Za-z0-9])([A-Z]{2,}s?)(?![A-Za-z0-9])", _caps, out)

    return re.sub(r"[ \t]{2,}", " ", out).strip()


def normalize_storyboard(sb: dict, lex: dict | None = None) -> dict:
    """Per-scene normalization; `full` re-joins with the same rule as the concat blocker."""
    lex = lex if lex is not None else load_lexicon()
    scenes = []
    for s in sb.get("scenes") or []:
        raw = str(s.get("narration") or "")
        norm = normalize_text(raw, lex)
        scenes.append({
            "id": s.get("id"),
            "text": norm,
            "words": len(norm.split()),
            "changed": norm != raw,
        })
    full = " ".join(s["text"] for s in scenes)
    if not scenes:  # boards without scenes (or ad-hoc use) fall back to narration_full
        full = normalize_text(str(sb.get("narration_full") or ""), lex)
    return {
        "full": full,
        "words": len(full.split()),
        "scenes": scenes,
        "source": "normalize_narration.py",
    }


# --------------------------------------------------------------------------
# self-test: the real leak corpus swept out of out/*/storyboard.json
# --------------------------------------------------------------------------
SELF_TEST = [
    ("A 27B model just fell from 24 gigs to 17.", "twenty seven billion"),
    ("A gaming card like the RTX 4090 holds twenty four gigabytes.", "R T X forty ninety"),
    ("The 4090 hits nearly a thousand.", "forty ninety"),
    ("An M1 MacBook Air writes ten words a second.", "M one"),
    ("An A100, two hundred seventy-seven.", "A one hundred"),
    ("Same EPYC chip, same model.", "epic"),
    ("Eight H200 GPUs.", "H two hundred"),
    ("HIPAA says get consent first.", "hippa"),
    ("ABA Opinion 512 says get consent first.", "A B A"),
    ("ABA Opinion 512, EPYC, and more.", "five hundred twelve, epic"),   # comma survives
    ("It reviewed 141,000 evaluation runs.", "one hundred forty one thousand"),
    ("off an NVMe SSD.", "N V M E"),
    ("Off a 7200-RPM hard drive: five minutes.", "seven thousand two hundred R P M"),
    ("You didn't train your custom GPT.", "G P T"),
    ("Claude's API, five and twenty-five per million.", "A P I"),
    ("a separate tool like aider or opencode.", "ay-der"),
    ("GLM five-point-two, seven hundred forty-three billion.", "G L M"),
    ("It costs $4,000. On purpose.", "four thousand dollars"),
    ("It costs $4,000 in 2026.", "four thousand dollars in twenty twenty six"),  # space after a bare amount survives
    ("It moves 273 GB/s.", "two hundred seventy three gigabytes a second"),
    ("about 2.7 tokens a second", "two point seven"),
    ("a 24GB card", "twenty four gigabytes"),
    ("NVFP4 shrinks it.", "N V F P four"),
    ("the KV cache", "K V"),
    ("The EU can now fine your whole AI stack.", "EU"),          # keep-listed
    ("Your RAM and GPU and CPU are fine.", "RAM"),               # keep-listed
]


def run_self_test(lex: dict) -> int:
    failures = 0

    for src, expect in SELF_TEST:
        got = normalize_text(src, lex)
        if expect not in got:
            print(f"FAIL  {src!r}\n      expected to contain {expect!r}\n      got {got!r}")
            failures += 1

    # idempotency: normalizing twice must equal normalizing once
    for src, _ in SELF_TEST:
        once = normalize_text(src, lex)
        twice = normalize_text(once, lex)
        if once != twice:
            print(f"FAIL (not idempotent)  {src!r}\n      once:  {once!r}\n      twice: {twice!r}")
            failures += 1

    # no digits may survive in normalized output
    for src, _ in SELF_TEST:
        got = normalize_text(src, lex)
        if re.search(r"\d", got):
            print(f"FAIL (digit survived)  {src!r} -> {got!r}")
            failures += 1

    # lexicon hygiene: replacement values must not re-trigger later passes
    for key, val in (lex.get("say") or {}).items():
        if re.search(r"\d", val):
            print(f"FAIL (lexicon) say[{key!r}] value contains a digit: {val!r}")
            failures += 1
        stray = [t for t in re.findall(r"(?<![A-Za-z])[A-Z]{2,}(?![a-z])", val)
                 if t not in (lex.get("keep") or [])]
        if stray:
            print(f"FAIL (lexicon) say[{key!r}] value has un-kept ALL-CAPS runs {stray}: {val!r}")
            failures += 1

    total = len(SELF_TEST) * 3 + len(lex.get("say") or {})
    print(f"self-test: {total - failures}/{total} checks passed")
    return 1 if failures else 0


def main() -> None:
    ap = argparse.ArgumentParser(description="Normalize narration into spoken form for TTS")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--storyboard", help="path to storyboard.json")
    src.add_argument("--text", help="normalize a literal string and print it")
    src.add_argument("--stdin", action="store_true", help="normalize stdin")
    src.add_argument("--self-test", action="store_true", help="run the leak-corpus checks")
    ap.add_argument("--out-txt", help="write normalized narration text here")
    ap.add_argument("--out-json", help="write the per-scene sidecar here")
    ap.add_argument("--lexicon", help=f"lexicon path (default: {DEFAULT_LEXICON})")
    args = ap.parse_args()

    lex = load_lexicon(args.lexicon)

    if args.self_test:
        sys.exit(run_self_test(lex))

    if args.text is not None:
        print(normalize_text(args.text, lex))
        return

    if args.stdin:
        print(normalize_text(sys.stdin.read(), lex))
        return

    sb_path = Path(args.storyboard)
    if not sb_path.exists():
        print(f"error: storyboard not found: {sb_path}", file=sys.stderr)
        sys.exit(1)
    with open(sb_path, "r", encoding="utf-8") as f:
        sb = json.load(f)

    norm = normalize_storyboard(sb, lex)

    if args.out_txt:
        p = Path(args.out_txt)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(norm["full"] + "\n", encoding="utf-8")
    if args.out_json:
        p = Path(args.out_json)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(norm, indent=2), encoding="utf-8")

    changed = sum(1 for s in norm["scenes"] if s["changed"])
    print(json.dumps({
        "words": norm["words"],
        "scenes": len(norm["scenes"]),
        "scenes_changed": changed,
        "out_txt": args.out_txt,
        "out_json": args.out_json,
    }))


if __name__ == "__main__":
    main()
