#!/usr/bin/env python3
"""variety_check.py -- the script ledger and the `sameness` gate.

Nothing in the pipeline checked whether today's Short feels like yesterday's.
This does. It keeps a rolling ledger of what shipped and refuses a board that
repeats the last few in shape, hook, ending, length or sentence rhythm.

  variety_check.py record --storyboard FILE.json --ledger PATH [--date YYYY-MM-DD]
  variety_check.py check  --storyboard FILE.json --ledger PATH [--window 5]
  variety_check.py entry  --storyboard FILE.json          (print the entry, write nothing)

`check` prints one JSON object {ok, violations, advisories, comparisons, entry}
and exits 0 when ok, 1 when any hard rule is violated. An empty or missing
ledger always passes. `--dry-run` works on every subcommand: it computes
everything and prints it but never touches the ledger file.

This file is also a library. `skills/script-gates/scripts/eval_short.py` imports
`ledger_entry`, `load_ledger` and `check_entry` to run the `sameness` gate; the
gate only runs when eval_short.py is given `--ledger`.

RULES (hard, over the last 5 entries; see rules/variety.md)
  structure          differs from the last two entries
  hook_pattern       differs from the last two entries
  closing_move       differs from the last two entries
  target_duration_s  not identical to all of the last three
  opener_bigrams     Jaccard vs each of the last five is at most 0.35

ADVISORY (never blocks, over the last 10 entries)
  repeated_phrase    an 8-word-or-longer word sequence this narration shares
                     with an earlier script. Re-teaching a concept is expected;
                     re-using the sentence is not.

Stdlib only, Python 3.9+.
"""
import argparse
import hashlib
import json
import re
import sys
from datetime import date as _date
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Prefer the validator's sentence/word splitting so every gate agrees on what a
# sentence is; fall back to identical copies when it is not importable.
try:
    sys.path.insert(0, str(HERE))
    from validate_storyboard import sentences, words  # type: ignore
except Exception:  # pragma: no cover - fallback path
    def sentences(text):
        parts = re.split(r"(?<=[.!?])\s+", (text or "").strip())
        return [p for p in parts if re.search(r"\w", p)]

    def words(text):
        return re.findall(r"[\w']+", text or "")

SHINGLE_N = 8          # words per shingle
SHINGLE_CAP = 400      # hashes kept per script (min-hash style: lowest 400)
HARD_WINDOW = 5        # entries the hard rules look back over
PHRASE_WINDOW = 10     # entries the repeated-phrase advisory looks back over
JACCARD_MAX = 0.35

LEDGER_DOC = ("Rolling record of shipped Shorts scripts. Appended by "
              "skills/script-gates/scripts/variety_check.py record; read by the "
              "`sameness` gate in eval_short.py. Newest entry last.")

# --- hook patterns -----------------------------------------------------------
# First match wins, in this order. The set is deliberately small and keyword
# driven: the point is a stable label to rotate against, not a taxonomy.
# Documented in rules/variety.md; keep the two in step.
_HOOK_RULES = [
    ("price", r"[$£€]|\bdollars?\b|\bprice[ds]?\b|\bpricing\b|\bcosts?\b|\bcheaper\b|\bfree\b"),
    ("tonight", r"\btonight\b|\btoday\b|\bthis week\b|\bright now\b|\bby tomorrow\b|\bjust (?:shipped|landed|dropped)\b"),
    ("number-shock", r"\d|\b(?:one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|"
                     r"million|billion|trillion|percent|half|twice|double|triple)\b"),
    ("wrong-diagnosis", r"\bwrong\b|\bmistake\b|\bmisread\b|\bblame\b|\byou think\b|\bthink it'?s\b|\blooks? (?:dumb|slow|broken)\b"),
    ("named-contradiction", r"\beveryone says\b|\bmyth\b|\bactually\b|\bbut\b|\bisn'?t\b|\bdidn'?t\b|\bdoesn'?t\b|\bwon'?t\b|\bcan'?t\b|\bnot\b"),
    ("decision", r"\bshould you\b|\bwhich\b|\bvs\.?\b|\bversus\b|\bworth it\b|\bbuy\b|\bpick\b|\bor\b"),
    ("case", r"\blaw firm\b|\bclinic\b|\bshop\b|\bcompan(?:y|ies)\b|\bbusiness(?:es)?\b|\benterprises?\b|\bteam\b|\bemployees?\b"),
    ("situation", r"^\s*you\b|\byou'?(?:ve|re|r)\b|\byour\b|\byou run\b|\byou got\b"),
]
_HOOK_RULES = [(name, re.compile(rx, re.I)) for name, rx in _HOOK_RULES]


def classify_hook(text):
    """Label a hook line with one of the documented patterns; 'other' on no match."""
    t = (text or "").strip()
    if not t:
        return "other"
    for name, rx in _HOOK_RULES:
        if rx.search(t):
            return name
    return "other"


# --- entry construction ------------------------------------------------------
def _norm_words(text):
    return [w.lower() for w in words(text)]


def shingles8(text, n=SHINGLE_N, cap=SHINGLE_CAP):
    """Hashes of every contiguous n-word lowercased sequence, as hex strings.

    Capped at `cap` by keeping the LOWEST hash values (a min-hash sample), so a
    long script and a short one still intersect at the right rate and the cap is
    deterministic rather than "whatever came first"."""
    ws = _norm_words(text)
    if len(ws) < n:
        return []
    seen = set()
    for i in range(len(ws) - n + 1):
        gram = " ".join(ws[i:i + n])
        seen.add(hashlib.blake2b(gram.encode("utf-8"), digest_size=8).hexdigest())
    return sorted(seen)[:cap]


def opener_bigrams(text):
    """Sorted unique lowercased first-two-words of every sentence."""
    out = set()
    for s in sentences(text or ""):
        ws = _norm_words(s)
        if len(ws) >= 2:
            out.add(" ".join(ws[:2]))
        elif ws:
            out.add(ws[0])
    return sorted(out)


def _narration(sb):
    return sb.get("narration_full") or " ".join(
        s.get("narration", "") for s in (sb.get("scenes") or []))


def ledger_entry(sb, date=None, slug=None):
    """Build the ledger row for a storyboard dict. Pure; writes nothing.

    `slug` overrides the storyboard's own slug field. The regression corpus needs
    this: two v1 boards ship byte-identical storyboards under different
    directories but carry the SAME internal slug, and the ledger keys off slug."""
    scenes = sb.get("scenes") or []
    narr = _narration(sb)
    hook_text = sb.get("hook_text") or ""
    sents = sentences(narr)
    # hook_pattern: an explicit storyboard field wins, then the storyboard's
    # `structure`-carried hook if one is recorded, then the classifier.
    pattern = sb.get("hook_pattern")
    if not pattern:
        pattern = classify_hook(hook_text or (sents[0] if sents else ""))
    last_narr = scenes[-1].get("narration", "") if scenes else ""
    analogy = sb.get("analogy") or {}
    vehicle = analogy.get("vehicle") if isinstance(analogy, dict) else None
    return {
        "slug": slug or sb.get("slug"),
        "date": date or _date.today().isoformat(),
        "format": sb.get("script_format") or "classic",
        "structure": sb.get("structure"),
        "hook_pattern": pattern,
        "hook_head": " ".join(_norm_words(hook_text)[:4]),
        "closing_move": " ".join(_norm_words(last_narr)[:6]),
        "target_duration_s": sb.get("target_duration_s"),
        "opener_bigrams": opener_bigrams(narr),
        "analogies": [vehicle] if vehicle else [],
        "shingles8": shingles8(narr),
    }


# --- ledger io ---------------------------------------------------------------
def load_ledger(path):
    """Entries oldest-first. A missing, empty or unreadable ledger is []."""
    if not path:
        return []
    p = Path(path)
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text() or "{}")
    except Exception:
        return []
    if isinstance(data, list):
        return data
    return list(data.get("entries") or [])


def append_entry(path, entry):
    """Append one entry, preserving the file's shape. Returns the new length."""
    p = Path(path)
    entries = load_ledger(p)
    entries.append(entry)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps({"_doc": LEDGER_DOC, "entries": entries}, indent=2) + "\n")
    tmp.replace(p)
    return len(entries)


# --- the sameness rules ------------------------------------------------------
def _jaccard(a, b):
    sa, sb_ = set(a or []), set(b or [])
    if not sa and not sb_:
        return 0.0
    union = sa | sb_
    return len(sa & sb_) / len(union) if union else 0.0


def check_entry(entry, ledger, window=HARD_WINDOW, phrase_window=PHRASE_WINDOW):
    """Run the sameness rules for `entry` against `ledger` (oldest-first).

    Ledger rows carrying this entry's own slug are skipped, so re-checking a
    board that is already recorded never fails against itself. An empty ledger
    always passes. Returns {ok, violations, advisories, comparisons, ...}."""
    prior = [e for e in (ledger or []) if e.get("slug") != entry.get("slug")]
    recent = prior[-window:]
    violations, advisories = [], []

    last2 = recent[-2:]
    for field, human in (("structure", "structure"),
                         ("hook_pattern", "hook pattern"),
                         ("closing_move", "closing move")):
        mine = entry.get(field)
        clash = [e for e in last2 if e.get(field) == mine]
        if clash and mine is not None:
            violations.append({
                "rule": field,
                "detail": "%s %r repeats %s" % (
                    human, mine, ", ".join(str(e.get("slug")) for e in clash)),
                "against": [e.get("slug") for e in clash]})
        elif clash and mine is None:
            # a board with no `structure` still counts as "the same shape as
            # the last one" when the last one had none either.
            violations.append({
                "rule": field,
                "detail": "%s is unset, same as %s" % (
                    human, ", ".join(str(e.get("slug")) for e in clash)),
                "against": [e.get("slug") for e in clash]})

    last3 = recent[-3:]
    tgt = entry.get("target_duration_s")
    if len(last3) >= 3 and tgt is not None and all(
            e.get("target_duration_s") == tgt for e in last3):
        violations.append({
            "rule": "target_duration_s",
            "detail": "target_duration_s %s is identical to the last three (%s)" % (
                tgt, ", ".join(str(e.get("slug")) for e in last3)),
            "against": [e.get("slug") for e in last3]})

    for e in recent:
        j = _jaccard(entry.get("opener_bigrams"), e.get("opener_bigrams"))
        if j > JACCARD_MAX:
            violations.append({
                "rule": "opener_bigrams",
                "detail": "sentence-opener Jaccard %.2f vs %s (max %.2f)" % (
                    j, e.get("slug"), JACCARD_MAX),
                "against": [e.get("slug")], "jaccard": round(j, 3)})

    mine_sh = set(entry.get("shingles8") or [])
    for e in prior[-phrase_window:]:
        shared = mine_sh & set(e.get("shingles8") or [])
        if shared:
            advisories.append({
                "rule": "repeated_phrase",
                "detail": "%d shared %d-word phrase(s) with %s" % (
                    len(shared), SHINGLE_N, e.get("slug")),
                "against": [e.get("slug")], "shared": len(shared)})

    return {"ok": not violations, "violations": violations,
            "advisories": advisories, "comparisons": len(recent),
            "phrase_comparisons": len(prior[-phrase_window:])}


def phrases_for_hashes(text, hashes, limit=5):
    """Human-readable examples: the n-word phrases in `text` whose hash is in
    `hashes`. Used to name what got repeated, since the ledger stores only hashes."""
    ws = _norm_words(text)
    want, out = set(hashes or []), []
    for i in range(max(0, len(ws) - SHINGLE_N + 1)):
        gram = " ".join(ws[i:i + SHINGLE_N])
        h = hashlib.blake2b(gram.encode("utf-8"), digest_size=8).hexdigest()
        if h in want:
            out.append(gram)
            want.discard(h)
            if len(out) >= limit:
                break
    return out


# --- cli ---------------------------------------------------------------------
def _load_sb(path):
    p = Path(path)
    if not p.exists():
        print("error: storyboard not found: %s" % p, file=sys.stderr)
        sys.exit(2)
    return json.loads(p.read_text())


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="variety_check.py",
        description="Script ledger and the `sameness` gate: refuse a Short that "
                    "repeats the last few in shape, hook, ending, length or rhythm.",
        epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")

    p_rec = sub.add_parser("record", help="append this storyboard's entry to the ledger")
    p_rec.add_argument("--storyboard", required=True)
    p_rec.add_argument("--slug", help="override the storyboard's own slug for this entry")
    p_rec.add_argument("--ledger", required=True)
    p_rec.add_argument("--date", help="YYYY-MM-DD (default: today)")
    p_rec.add_argument("--dry-run", action="store_true",
                       help="print the entry that would be appended; write nothing")

    p_chk = sub.add_parser("check", help="run the sameness rules against the ledger")
    p_chk.add_argument("--storyboard", required=True)
    p_chk.add_argument("--slug", help="override the storyboard's own slug for this entry")
    p_chk.add_argument("--ledger", required=True)
    p_chk.add_argument("--window", type=int, default=HARD_WINDOW,
                       help="how many previous entries the hard rules see (default 5)")
    p_chk.add_argument("--dry-run", action="store_true",
                       help="no-op: check never writes. Accepted for symmetry.")

    p_ent = sub.add_parser("entry", help="print the ledger entry for a storyboard")
    p_ent.add_argument("--storyboard", required=True)
    p_ent.add_argument("--slug", help="override the storyboard's own slug for this entry")
    p_ent.add_argument("--date")
    p_ent.add_argument("--dry-run", action="store_true", help="no-op: entry never writes")

    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 2

    sb = _load_sb(a.storyboard)
    entry = ledger_entry(sb, date=getattr(a, "date", None), slug=getattr(a, "slug", None))

    if a.cmd == "entry":
        print(json.dumps(entry, indent=2))
        return 0

    if a.cmd == "record":
        if a.dry_run:
            print(json.dumps({"dry_run": True, "ledger": a.ledger,
                              "would_append": entry}, indent=2))
            return 0
        n = append_entry(a.ledger, entry)
        print(json.dumps({"recorded": entry["slug"], "ledger": a.ledger,
                          "entries": n}, indent=2))
        return 0

    # check
    ledger = load_ledger(a.ledger)
    res = check_entry(entry, ledger, window=a.window)
    narr = _narration(sb)
    for adv in res["advisories"]:
        prev = next((e for e in ledger if e.get("slug") in (adv.get("against") or [])), None)
        if prev:
            shared = set(entry.get("shingles8") or []) & set(prev.get("shingles8") or [])
            adv["examples"] = phrases_for_hashes(narr, shared)
    out = {"ok": res["ok"], "violations": res["violations"],
           "advisories": res["advisories"], "comparisons": res["comparisons"],
           "slug": entry["slug"], "ledger": a.ledger,
           "ledger_entries": len(ledger)}
    if a.dry_run:
        out["dry_run"] = True
    print(json.dumps(out, indent=2))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
