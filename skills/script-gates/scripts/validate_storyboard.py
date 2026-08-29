#!/usr/bin/env python3
"""validate_storyboard.py <storyboard.json> [--history FILE]  — v3 (soft gate), v2 port

Machine gate before Gate 1. Stdlib-only. Findings come in two tiers:

  BLOCKERS   machine-breaking — a downstream stage literally cannot proceed.
             Hard-fail (exit 1); these block Gate-1 approval.
  ADVISORIES stylistic / evidence-based craft nits. Surfaced to the human,
             who may approve anyway. Never block the pipeline (exit 3).

A third, even softer `warnings` tier is kept for hints that never affect the
exit code. `violations` = blockers + advisories is retained for back-compat.

This validator checks PHYSICS, not storytelling. How the concept is explained
— analogy or none, what structure, what ending — is the storyboard writer's
call and is deliberately unchecked here.

STRUCTURE   [blocker] hook first / payoff_close last / roles+enums / scene
            keys / est 2-25 / 3-7 scenes / concat rule / target 28-60
            [advisory] archetype adjacency · style-pack rotation
CONCAT      [blocker] scene narrations joined by single spaces == narration_full
LANGUAGE    [advisory] FK grade >8 · sentence cap 20 / avg <=15 · hook
            sentence 5-12 · banned openers/closers/fillers/hype/CTA
            · (passive-ish: warn)
PACING      [advisory] words/sec vs target · est-sum vs target (word budget: warn)
VOICE       [advisory] >3 "we/our/us" in a second-person band · no "you/your/
            you're" in the first three sentences
ENDING      [advisory] sentences after the payoff line: `ending` from
            formats.json (abrupt = 1, resolution-or-recap = 2). The payoff is
            anchored at the FIRST sentence of the final payoff_close scene
LENGTH      [advisory] narration_full over the band's narration_max_chars
HOOKS       [advisory] hook_text <=7 words · >=10 hook_candidates ·
            title==hook (title length: warn)
SFX         [advisory] <=6 total
SHAPE       `structure` (narrative shape) is free text: never rejected; an
            unlisted value is a warning only. Absent script_format = classic.

Paths (v2 port, all relative to this file): formats.json, tts_lexicon.json and
voice.config.json (wps_by_format, then wps) in skills/script-gates/; the schema in
shared/schemas/storyboard.schema.json; style history in
skills/render-shorts/styles/history.json (--history overrides; a missing file
is "no history" and raises an advisory, never a crash).

Exit 0 = clean · 1 = blockers · 3 = advisories-only (JSON printed either way).
"""
import argparse
import json
import re
import sys
from pathlib import Path

# v2 port (skills/script-gates/scripts/): every data file is found relative to
# this file. parents[1] is skills/script-gates, parents[3] is the repo root.
SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "shared" / "schemas" / "storyboard.schema.json"  # repointed from pipeline/schemas/
FORMATS_PATH = SKILL_DIR / "formats.json"  # repointed from pipeline/formats.json
LEXICON_PATH = SKILL_DIR / "tts_lexicon.json"  # repointed from pipeline/tts_lexicon.json
VOICE_CONFIG_PATH = SKILL_DIR / "voice.config.json"  # repointed from pipeline/voice.config.json
HISTORY_PATH = REPO_ROOT / "skills" / "render-shorts" / "styles" / "history.json"  # repointed from docs/styles/history.json

TOOLS = {"hyperframes", "manim"}
# hook must be first, payoff_close last; the middle labels are free.
# "foreshadow" is retained so boards shipped under v2 still validate.
ROLES = {"hook", "foreshadow", "explain", "payoff_close"}


def _packs_from_schema():
    """style_pack enum from the schema file — the single source of truth."""
    schema = SCHEMA_PATH  # repointed: shared/schemas/storyboard.schema.json
    try:
        enum = json.load(open(schema))["properties"]["style_pack"]["enum"]
        return set(enum)
    except Exception:
        return {"signal", "terminal", "sketch", "blueprint",
                "axon", "halftone", "silicon"}


def _lexicon():
    """say/keep tables from skills/script-gates/tts_lexicon.json (shared with the normalizer)."""
    path = LEXICON_PATH  # repointed: skills/script-gates/tts_lexicon.json
    try:
        lex = json.load(open(path))
        return set(lex.get("say", {})), set(lex.get("keep", []))
    except Exception:
        return set(), set()


SAY_TOKENS, KEEP_TOKENS = _lexicon()


# Fallback mirrors skills/script-gates/formats.json's classic entry so the validator keeps
# working (classically) if the file is missing. smooth-explainer REQUIRES the
# file — absent, a smooth board simply blocks on the classic target band, which
# is the safe direction.
_CLASSIC_FALLBACK = {
    "target_s": {"min": 28, "max": 60, "sweet_min": 32, "sweet_max": 38},
    "words": {"min": 70, "max": 130, "hint": "~85-110"},
    "narration_max_chars": 1200,
    "scene_count": {"min": 3, "max": 7},
    "scene_long_advisory_s": 12,
    "scene_narration_advisory_s": 13,
    "hook": {"concrete_required": True, "first_sentence_words": {"min": 5, "max": 12}, "scene_max_s": 7},
    "sentence": {"cap": 20, "pct_over_cap": 0.0, "avg_max": 15, "runaway": None},
    "numbers": {"policy": "band", "min_count": 2, "max_count": 5},
    "person": "you",
    "ending": "abrupt",
    "est_sum_tolerance": {"lo": 0.8, "hi": 1.25},
    "wps_fallback": 2.6,
}


def _formats():
    """Per-format bands from skills/script-gates/formats.json (single source of truth)."""
    path = FORMATS_PATH  # repointed: skills/script-gates/formats.json
    try:
        return json.load(open(path))["formats"]
    except Exception:
        return {"classic": _CLASSIC_FALLBACK}


def _structures():
    """Known narrative shapes: the informational `structures` list in formats.json; [] when absent."""
    try:
        return list(json.load(open(FORMATS_PATH)).get("structures", []))
    except Exception:
        return []


def _wps(fmt, fmt_cfg):
    """Words/sec, in preference order: the pinned voice's measured per-format rate
    (voice.config.json `wps_by_format[fmt]`) beats its flat `wps`, which beats the
    band's `wps_fallback` in formats.json, which beats 2.6."""
    cfg = {}
    try:
        cfg = json.load(open(VOICE_CONFIG_PATH))  # repointed: skills/script-gates/voice.config.json
    except Exception:
        pass
    by_fmt = cfg.get("wps_by_format") or {}
    w = by_fmt.get(fmt) if isinstance(by_fmt, dict) else None
    if not w:
        w = cfg.get("wps")
    if w:
        return float(w)
    return float(fmt_cfg.get("wps_fallback", 2.6))


PACKS = _packs_from_schema()
ARCHETYPES = {"centered-stack", "split-compare", "timeline", "grid",
              "giant-number", "diagram-flow"}
MOODS = {"curious-tech", "steady-build", "warm-optimist", "none"}
WPS = 2.6

BANNED_HYPE = ["revolutionary", "insane", "game-changer", "game changing",
               "mind-blowing", "mindblowing", "secret sauce",
               "they don't want you"]
BANNED_CTA = ["follow for", "subscribe", "like and", "smash that",
              "hit the bell", "link in bio", "don't forget to"]
BANNED_OPENERS = ["hey guys", "welcome back", "in this video", "what's up",
                  "today i'm going", "today i am going", "today we",
                  "let's talk about", "so today"]
BANNED_CLOSERS = ["so yeah", "anyway", "that's it for", "thanks for watching"]
FILLERS = ["basically", "actually", "you know", "kind of", "sort of",
           "at the end of the day", "without further ado", "let's dive in",
           "let's get started"]
# Number without a referent: a scale word or capacity unit that ENDS its
# clause names a quantity of nothing ("holds twenty four gigabytes." — of
# WHAT?). Requiring clause-final position makes rate phrases ("gigabytes a
# second") and money ("thousand dollars") pass for free: the referent word
# sits between the unit and the punctuation.
NUM_UNIT_RE = re.compile(
    r"\b((?:[A-Za-z][\w'-]*\s+){0,3}"
    r"(?:billions?|millions?|trillions?|gigabytes?|gigs?|terabytes?|megabytes?|petabytes?))"
    r"\s*(?=[.,;:!?—–]|$)", re.I)

def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if re.search(r"\w", p)]


def words(text):
    return re.findall(r"[\w']+", text)


def syllables(word):
    w = word.lower().strip("'")
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and n > 1 and not w.endswith(("le", "ee", "ye")):
        n -= 1
    return max(1, n)


def fk_grade(text):
    sents = sentences(text)
    ws = words(text)
    if not sents or not ws:
        return 0.0
    syl = sum(syllables(w) for w in ws)
    return 0.39 * (len(ws) / len(sents)) + 11.8 * (syl / len(ws)) - 15.59


def _emit(path, scenes, grade, ws, est_speech, bl, adv, warn):
    """Print the diagnostic JSON and exit with the tiered code."""
    print(json.dumps({"file": path, "scenes": scenes,
                      "fk_grade": round(grade, 1),
                      "words": ws,
                      "est_speech_s": round(est_speech, 1),
                      "blockers": bl,
                      "advisories": adv,
                      "violations": bl + adv,
                      "warnings": warn}, indent=2))
    if bl:
        sys.exit(1)
    if adv:
        sys.exit(3)
    sys.exit(0)


def main():
    ap = argparse.ArgumentParser(
        description="Machine gate for a Short storyboard: blockers exit 1, advisories exit 3, clean exit 0.",
        epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("storyboard", nargs="?", help="path to the storyboard JSON")
    ap.add_argument("--history", default=None,
                    help=f"style-pack history file (default: {HISTORY_PATH}); "
                         "a missing file means no history and is reported as an advisory")
    ap.add_argument("--dry-run", action="store_true",
                    help="no-op: this script only reads and prints. Accepted so every "
                         "script in skills/script-gates takes the same flags.")
    args = ap.parse_args()
    if not args.storyboard:
        print(__doc__)
        sys.exit(2)
    path = args.storyboard
    sb = json.load(open(path))
    bl, adv, warn = [], [], []

    # ---- required keys (missing => can't proceed) ------------------------
    for key in ["slug", "topic", "title", "description", "hashtags",
                "hook_text", "hook_candidates", "style_pack",
                "target_duration_s", "narration_full",
                "music_mood", "scenes"]:
        if key not in sb:
            bl.append(f"missing key: {key}")
    if bl:
        print(json.dumps({"file": path, "blockers": bl, "advisories": [],
                          "violations": bl, "warnings": warn}, indent=2))
        sys.exit(1)

    # ---- enums / shape ---------------------------------------------------
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,40}", sb["slug"]):
        bl.append(f"bad slug: {sb['slug']}")
    if sb["music_mood"] not in MOODS:
        adv.append(f"bad music_mood: {sb['music_mood']}")
    if sb["style_pack"] not in PACKS:
        adv.append(f"bad style_pack: {sb['style_pack']}")

    # Script format: absent = classic. Unknown value degrades to classic with
    # an advisory (never a blocker) so a typo can't strand a board.
    formats = _formats()
    fmt = sb.get("script_format", "classic")
    if fmt not in formats:
        adv.append(f"unknown script_format '{fmt}' — treating as classic (see skills/script-gates/formats.json)")
        fmt = "classic"
    F = formats.get(fmt, _CLASSIC_FALLBACK)
    WPS = _wps(fmt, F)

    # v2: `structure` is the narrative shape (script-structures.md). It is
    # independent of the band and never rejected; an unlisted value is only
    # noted at the warning tier so a typo stays visible.
    structure = sb.get("structure")
    if structure is not None:
        if not isinstance(structure, str):
            adv.append("structure must be a string when present")
        else:
            known = _structures()
            if known and structure not in known:
                warn.append(f"structure '{structure}' not in the formats.json structures list (allowed; informational)")

    tgt = sb["target_duration_s"]
    _t = F["target_s"]
    if not (_t["min"] <= tgt <= _t["max"]):
        bl.append(f"target_duration_s {tgt} outside {_t['min']}-{_t['max']}")
    elif not (_t["sweet_min"] <= tgt <= _t["sweet_max"]):
        warn.append(f"target {tgt}s outside the {_t['sweet_min']}-{_t['sweet_max']}s evidence band")
    if not all(re.fullmatch(r"#[A-Za-z0-9]+", h) for h in sb["hashtags"]):
        adv.append("hashtags must all match #Alnum")
    # repointed: shared/playbook/hashtags-tags.md is the source of truth. YouTube shows at
    # most 3 above the title, so 2-3 is the target; the schema floor is 3. The package stage
    # writes the final list, so these are working values.
    if not 2 <= len(sb["hashtags"]) <= 4:
        adv.append(f"{len(sb['hashtags'])} hashtags -- 2-3 is the target "
                   "(only 3 show above the title; see shared/playbook/hashtags-tags.md)")
    tags = sb.get("tags") or []
    if len(tags) < 15:
        adv.append(f"{len(tags)} YouTube keyword tags — 15–25 recommended "
                   "(the Studio Tags box, separate from hashtags)")
    if len(sb["title"]) > 40:
        warn.append(f"title {len(sb['title'])} chars — mobile truncates ~40")
    if sb["title"].strip().lower() == sb["hook_text"].strip().lower():
        adv.append("title is verbatim hook_text — re-confirm the promise, don't repeat it")

    # ---- hooks -----------------------------------------------------------
    if len(words(sb["hook_text"])) > 7:
        adv.append(f"hook_text >7 words: '{sb['hook_text']}'")
    if len(sb.get("hook_candidates", [])) < 10:
        adv.append(f"only {len(sb.get('hook_candidates', []))} hook_candidates — write >=10")

    narr = sb["narration_full"]
    sents = sentences(narr)
    ws = words(narr)

    first = sents[0] if sents else ""
    fw = len(words(first))
    _h = F["hook"]["first_sentence_words"]
    if not (_h["min"] <= fw <= _h["max"]):
        adv.append(f"hook sentence {fw} words — must be {_h['min']}-{_h['max']}: '{first}'")

    # ---- language --------------------------------------------------------
    grade = fk_grade(narr)
    if grade > 8:
        adv.append(f"FK grade {grade:.1f} > 8 — simplify hard")
    elif grade > 5:
        warn.append(f"FK grade {grade:.1f} — target <=5")

    lens = [len(words(s)) for s in sents]
    _s = F["sentence"]
    if not _s.get("pct_over_cap"):
        # classic: every over-cap sentence is named
        for s, n in zip(sents, lens):
            if n > _s["cap"]:
                adv.append(f"sentence >{_s['cap']} words ({n}): '{s[:60]}…'")
    else:
        # smooth: a SHARE of long sentences is allowed (reference explainers run
        # ~20% over 20 words); only a runaway sentence is named individually.
        over = sum(1 for n in lens if n > _s["cap"])
        if lens and over / len(lens) > _s["pct_over_cap"]:
            adv.append(f"{over}/{len(lens)} sentences over {_s['cap']} words — "
                       f"this format allows ~{int(_s['pct_over_cap']*100)}%")
        if _s.get("runaway"):
            for s, n in zip(sents, lens):
                if n > _s["runaway"]:
                    adv.append(f"runaway sentence ({n} words): '{s[:60]}…'")
    if lens and sum(lens) / len(lens) > _s["avg_max"]:
        adv.append(f"avg sentence {sum(lens)/len(lens):.1f} words > {_s['avg_max']}")
    if len(lens) >= 4:
        for i in range(0, len(lens) - 3):
            if min(lens[i:i + 4]) > 6:
                warn.append("4 consecutive sentences all >6 words — add a punch sentence")
                break

    low = " " + narr.lower() + " "
    for p in BANNED_HYPE:
        if p in low:
            adv.append(f"banned hype: '{p}'")
    for p in BANNED_CTA:
        if p in low:
            adv.append(f"spoken CTA phrase: '{p}' — CTAs live in description/pinned comment")
    head = " ".join(sents[:2]).lower()
    for p in BANNED_OPENERS:
        if p in head:
            adv.append(f"banned opener: '{p}'")
    tail = " ".join(sents[-2:]).lower()
    for p in BANNED_CLOSERS:
        if p in tail:
            adv.append(f"banned closer: '{p}'")
    fills = [p for p in FILLERS if p in low]
    if len(fills) > 2:
        adv.append(f"filler density: {fills}")
    elif fills:
        warn.append(f"fillers present: {fills}")
    passive = len(re.findall(r"\b(is|are|was|were|been|being|be)\s+\w+ed\b", low))
    if sents and passive / len(sents) > 0.2:
        warn.append(f"passive-ish constructions in ~{passive}/{len(sents)} sentences")

    # ---- scenes ----------------------------------------------------------
    scenes = sb["scenes"]
    _c = F["scene_count"]
    if not (_c["min"] <= len(scenes) <= _c["max"]):
        bl.append(f"{len(scenes)} scenes outside {_c['min']}-{_c['max']}")
    sfx_total = 0
    prev_arch = None
    for i, s in enumerate(scenes):
        sid = s.get("id", f"idx{i}")
        for key in ["id", "role", "tool", "layout_archetype", "narration",
                    "on_screen_text", "visual_brief", "est_duration_s"]:
            if key not in s:
                bl.append(f"{sid}: missing {key}")
        if s.get("tool") not in TOOLS:
            bl.append(f"{sid}: bad tool")
        if s.get("role") not in ROLES:
            bl.append(f"{sid}: bad role (cta is retired; use payoff_close)")
        arch = s.get("layout_archetype")
        if arch not in ARCHETYPES:
            bl.append(f"{sid}: bad layout_archetype")
        if arch and arch == prev_arch:
            adv.append(f"{sid}: repeats adjacent archetype '{arch}'")
        prev_arch = arch
        if not (2 <= float(s.get("est_duration_s", 0)) <= 25):
            bl.append(f"{sid}: est_duration_s outside 2-25")
        # long single-render scenes cost the most render time and lose retention;
        # flag by est AND by narration length (actual slot ≈ narration/WPS).
        est_s = float(s.get("est_duration_s", 0))
        if est_s > F["scene_long_advisory_s"]:
            adv.append(f"{sid}: est {est_s:.0f}s — long single-render scene; consider splitting the beat")
        nwords = len(words(s.get("narration", "")))
        if nwords / WPS > F["scene_narration_advisory_s"]:
            adv.append(f"{sid}: narration ~{nwords} words (~{nwords/WPS:.0f}s on screen) — long single-render scene; split the beat")
        if len(s.get("visual_brief", "")) < 40:
            adv.append(f"{sid}: visual_brief too thin")
        # TTS-hostile narration. The normalizer expands these anyway, but the
        # WRITER owns the phrasing — "twenty-seven billion" reads better than
        # whatever a lexicon guesses. on_screen_text is deliberately exempt:
        # digits belong on screen.
        scene_narr = s.get("narration", "")
        digits = re.search(r"[\$€£]?\d[\d,.]*\w*", scene_narr)
        if digits:
            adv.append(f"{sid}: digits in narration: '{digits.group(0)}' — write numbers as words")
        for m in NUM_UNIT_RE.finditer(scene_narr):
            adv.append(f"{sid}: number without referent: '…{m.group(1)}' — "
                       f"name what it measures ('gigabytes of memory', 'billion parameters')")
        for tok in re.findall(r"(?<![A-Za-z0-9])([A-Z]{2,}s?)(?![A-Za-z0-9])", scene_narr):
            if tok in KEEP_TOKENS:
                continue
            if tok in SAY_TOKENS:
                warn.append(f"{sid}: '{tok}' will be spoken via skills/script-gates/tts_lexicon.json")
            else:
                adv.append(f"{sid}: acronym '{tok}' has no spoken form — "
                           f"rewrite it or add an entry to skills/script-gates/tts_lexicon.json")
        for beat in s.get("on_screen_text", "").split("|"):
            if len(words(beat)) > 8:
                adv.append(f"{sid}: on-screen beat >8 words: '{beat.strip()}'")
        sfx_total += len(s.get("sfx", []))
        # beat density: brief must promise change often enough
        dur = float(s.get("est_duration_s", 0))
        brief = s.get("visual_brief", "")
        cues = len(re.findall(r"\b(then|swap|appear|fade|draw|count|reveal|pulse|slide|switch|land|pop|type|erase|on ['\"])", brief.lower()))
        if dur > 6 and cues < max(2, int(dur / 3)):
            warn.append(f"{sid}: {dur:.0f}s scene with ~{cues} visual beats in brief — need a change every ~3s")
    if sfx_total > 6:
        adv.append(f"{sfx_total} sfx cues > 6 max")

    roles = [s.get("role") for s in scenes]
    if roles[:1] != ["hook"]:
        bl.append("first scene must be role=hook")
    if roles[-1:] != ["payoff_close"]:
        bl.append("last scene must be role=payoff_close")
    if roles[0] == "hook" and float(scenes[0].get("est_duration_s", 99)) > F["hook"]["scene_max_s"]:
        adv.append(f"hook scene >{F['hook']['scene_max_s']}s")

    # hook scene brief must name frame-1 + motion onset
    b0 = scenes[0].get("visual_brief", "").lower()
    if "frame 1" not in b0 and "frame one" not in b0 and "first frame" not in b0:
        adv.append("hook visual_brief must specify the frame-1 composition")
    if not re.search(r"(onset|snaps?|pops?|slams?|begins|starts|draws?|mid-)", b0):
        warn.append("hook brief: name the <=0.5s motion onset explicitly")

    # ---- concat rule -----------------------------------------------------
    joined = " ".join(s.get("narration", "") for s in scenes)
    if joined != narr:
        for i, (a, b) in enumerate(zip(joined, narr)):
            if a != b:
                bl.append(f"concat rule broken at char {i}: '…{joined[max(0,i-25):i+25]}…' vs '…{narr[max(0,i-25):i+25]}…'")
                break
        else:
            bl.append(f"concat rule broken: lengths {len(joined)} vs {len(narr)}")

    # ---- pacing ----------------------------------------------------------
    est_speech = len(ws) / WPS
    if not (0.75 * tgt <= est_speech <= 1.25 * tgt):
        adv.append(f"narration ~{est_speech:.0f}s at {WPS}wps vs target {tgt}s")
    _w = F["words"]
    if not (_w["min"] <= len(ws) <= _w["max"]):
        warn.append(f"{len(ws)} words — {_t['sweet_min']}-{_t['sweet_max']}s band wants {_w['hint']}")
    est_sum = sum(float(s.get("est_duration_s", 0)) for s in scenes)
    _tol = F["est_sum_tolerance"]
    if not (_tol["lo"] * tgt <= est_sum <= _tol["hi"] * tgt):
        adv.append(f"sum(est)={est_sum:.0f}s vs target {tgt}s")

    # ---- person, ending, narration length ---------------------------------
    # Both bands are second person now (formats.json `person`); "we" is reserved
    # for our own measurements.
    if F.get("person") == "you":
        plural = len(re.findall(r"\b(?:we|our|ours|us)\b", narr, re.I))
        if plural > 3:
            adv.append(f"{plural} first-person-plural uses ('we/our') — this format is second-person ('you')")
        # Direct address: the viewer's situation is named early or the script is
        # talking about the subject instead of to the viewer.
        head3 = " ".join(sents[:3])
        if not re.search(r"\b(?:you|your|you['\u2019]re)\b", head3, re.I):
            adv.append("no second-person marker ('you', 'your', \"you're\") in the first "
                       "three sentences: name the viewer's situation up front")

    # `ending` (formats.json): the last spoken sentence is the payoff and almost
    # nothing follows it. The payoff is anchored, deterministically, at the FIRST
    # sentence of the final payoff_close scene; every sentence after it in that
    # scene is tail. `abrupt` allows one tail sentence, `resolution-or-recap` two.
    _ending = F.get("ending")
    _tail_budget = {"abrupt": 1, "resolution-or-recap": 2}.get(_ending)
    if _tail_budget is not None and scenes:
        _last_sents = sentences(scenes[-1].get("narration", "") or "")
        _tail = _last_sents[1:]
        if len(_tail) > _tail_budget:
            adv.append(f"ending '{_ending}': {len(_tail)} sentences follow the payoff line "
                       f"(at most {_tail_budget}): cut to the payoff and stop: "
                       f"'{' '.join(_tail)[:80]}…'")

    # `narration_max_chars` (formats.json): the schema's per-band bound.
    _max_chars = F.get("narration_max_chars")
    if _max_chars and len(narr) > _max_chars:
        adv.append(f"narration_full {len(narr)} chars > {_max_chars} for {fmt} "
                   f"(skills/script-gates/formats.json narration_max_chars)")

    # ---- style-pack rotation ---------------------------------------------
    # repointed: skills/render-shorts/styles/history.json (v1: docs/styles/history.json).
    # A missing or unreadable file means "no history": the rotation rule cannot be
    # checked, so say so as an advisory and carry on. Never a crash, never a blocker.
    hist = Path(args.history) if args.history else HISTORY_PATH
    try:
        used = json.load(open(hist)).get("used", [])
    except FileNotFoundError:
        used = []
        adv.append(f"style-pack rotation not checked: no history file at {hist} (treated as no history)")
    except Exception as e:
        used = []
        adv.append(f"style-pack rotation not checked: could not read {hist} ({e})")
    if used and used[-1].get("pack") == sb["style_pack"] and used[-1].get("slug") != sb["slug"]:
        adv.append(f"style_pack '{sb['style_pack']}' same as previous video — rotate")

    _emit(path, len(scenes), grade, len(ws), est_speech, bl, adv, warn)


if __name__ == "__main__":
    main()
