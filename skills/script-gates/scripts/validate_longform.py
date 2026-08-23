#!/usr/bin/env python3
"""validate_longform.py --script FILE.md [--narration FILE.txt] [--outline FILE.md] [--json] [--dry-run]

Machine gate for a long-form episode script, the sibling of validate_storyboard.py.
Stdlib only. Findings come in the same three tiers:

  BLOCKERS   the episode cannot be built as written: wrong length for its target,
             chapters that do not exist or do not match the outline, beats that
             are not beats, a measured number with nothing to measure it with.
             Exit 1.
  ADVISORIES craft nits with an owner: hype, spoken CTAs, template openers,
             runaway sentences, positional labels, no direct address, dead air,
             a missing opening number, analogy pile-up. Exit 3, never blocking.
  WARNINGS   hints that never move the exit code (missing outline, unknown
             structure, frontmatter that disagrees with the text).

Pacing is estimated at 150 spoken words per minute (2.5 words per second), the
figure the long-form outline format and shared/platform-specs.md both use.

The banned-word lists and the sentence splitter are imported from
validate_storyboard.py in this folder, so Shorts and long-form ban the same
words. If that import fails, a small built-in list is used and a warning says so.

Inputs, all optional except --script:
  --script     [slug]-script.md, per workspaces/long-form/stages/05-script/references/script-format.md
  --narration  [slug]-narration.txt; when absent the beat narrations are joined instead
  --outline    [slug]-outline.md; supplies target_minutes and the chapter list to match
  --json       print the JSON report instead of the text one
  --dry-run    run every check, print the report, then exit 0 whatever it found

Rules and thresholds: skills/script-gates/rules/longform-gates.md.
Exit 0 = clean, 1 = blockers, 3 = advisories only, 2 = usage error.
"""
import argparse
import json
import re
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent

# ---- shared vocabulary, imported from the Shorts validator ------------------
# One source of truth for the banned words. The fallback keeps this gate usable
# if the sibling script is mid-rewrite; it is deliberately shorter, and says so.
_IMPORT_WARNING = None
try:
    sys.path.insert(0, str(SCRIPTS_DIR))
    import validate_storyboard as _vs

    BANNED_HYPE = list(_vs.BANNED_HYPE)
    BANNED_CTA = list(_vs.BANNED_CTA)
    BANNED_OPENERS = list(_vs.BANNED_OPENERS)
    FILLERS = list(_vs.FILLERS)
    sentences = _vs.sentences
    words = _vs.words
except Exception as exc:  # noqa: BLE001 - any failure falls back, never crashes
    _IMPORT_WARNING = ("could not import validate_storyboard.py (%s); "
                       "using the built-in fallback word lists" % exc)
    BANNED_HYPE = ["revolutionary", "insane", "game-changer", "mind-blowing",
                   "secret sauce", "next-level", "seamless"]
    BANNED_CTA = ["follow for", "subscribe", "like and", "smash that",
                  "hit the bell", "link in bio", "don't forget to"]
    BANNED_OPENERS = ["hey guys", "welcome back", "in this video", "what's up",
                      "today we", "today i'm going", "let's talk about"]
    FILLERS = ["basically", "actually", "let's dive in", "without further ado"]

    def sentences(text):
        parts = re.split(r"(?<=[.!?])\s+", text.strip())
        return [p for p in parts if re.search(r"\w", p)]

    def words(text):
        return re.findall(r"[\w']+", text)

# The four openers named in the long-form spec, plus everything the Shorts list
# already bans. "let's dive in" lives in the Shorts FILLERS list.
LONGFORM_OPENERS = sorted(set(BANNED_OPENERS)
                          | {p for p in FILLERS if p in ("let's dive in", "let's get started")}
                          | {"in this video", "today we", "let's dive in", "welcome back"})

WPM = 150.0
WPS = WPM / 60.0                 # 2.5 words per second
BAND = 0.15                      # target words plus or minus 15 percent
MIN_CHAPTERS = 3
MIN_CHAPTER_S = 60
BEAT_WORDS = (20, 60)
SENTENCE_CAP = 20
SENTENCE_AVG_MAX = 18
MAX_LABELS = 3
LABEL_STRUCTURE = "build-along"
HOOK_NUMBER_S = 20               # the surprising number is spoken by 0:20
NEW_INFO_GAP_S = 30
MAX_ANALOGIES = 1
KNOWN_STRUCTURES = {"concept-deep-dive", "build-along", "buyers-guide",
                    "benchmark-showdown", "myth-bust-long"}

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)
CHAPTER_RE = re.compile(r"^##\s+Chapter\s+(\d+)\s*[:.\-]?\s*(.*)$", re.I)
BEAT_ID_RE = re.compile(r"^\d+\.\d+$")
# Positional labels: the plan's regex, applied per sentence.
LABEL_RE = re.compile(r"^\s*\(?(?:in\s+|that's\s+|and\s+)?"
                      r"(stage|step|part|phase)\s+"
                      r"(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b", re.I)
SECOND_PERSON_RE = re.compile(r"\b(you|your|yours|you're|you've|you'll|you'd)\b", re.I)
DIGIT_RE = re.compile(r"\d")
NUMBER_WORDS = (r"one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
                r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|"
                r"twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
                r"hundred|thousand|million|billion|trillion|percent|half|twice|double")
NUMBER_WORD_RE = re.compile(r"\b(%s)\b" % NUMBER_WORDS, re.I)
ACTION_VERB_RE = re.compile(r"\b\w+(?:e|y)?(?:s|ing|ed)?\b")
ANALOGY_RE = re.compile(r"(think of (?:it|this) as|imagine (?:a|an|you)|"
                        r"\blike a\b|\blike an\b|\bas if\b|the way a\b|"
                        r"picture a\b|it's basically a\b|is basically a\b)", re.I)


# ---- parsing ---------------------------------------------------------------
def frontmatter(text):
    """The leading --- block as a flat dict of strings; {} when there is none."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def table_rows(lines):
    """Cell lists for every pipe row in `lines`, header and separator dropped."""
    rows = []
    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            continue
        if re.fullmatch(r"\|[\s\-:|]+\|", s):
            continue
        rows.append([c.strip() for c in s.strip("|").split("|")])
    return rows


def parse_script(text):
    """(frontmatter, [chapter]) where a chapter is {num, label, beats[]}."""
    meta = frontmatter(text)
    lines = text.splitlines()
    starts = [(i, CHAPTER_RE.match(ln)) for i, ln in enumerate(lines)]
    starts = [(i, m) for i, m in starts if m]
    chapters = []
    for pos, (i, m) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        body = lines[i + 1:end]
        beats = []
        for cells in table_rows(body):
            if not cells or not BEAT_ID_RE.match(cells[0]):
                continue
            beats.append({
                "id": cells[0],
                "narration": cells[1] if len(cells) > 1 else "",
                "on_screen": cells[2] if len(cells) > 2 else "",
                "visual": cells[3] if len(cells) > 3 else "",
                "scene_hint": cells[4] if len(cells) > 4 else "",
                "cue": cells[5] if len(cells) > 5 else "",
            })
        chapters.append({"num": m.group(1), "label": m.group(2).strip(), "beats": beats})
    return meta, chapters


def parse_outline(text):
    """(frontmatter, [chapter label]) read from the '## Chapters' table."""
    meta = frontmatter(text)
    lines = text.splitlines()
    labels = []
    inside = False
    for line in lines:
        if line.startswith("## "):
            inside = line.strip().lower().startswith("## chapters")
            continue
        if not inside:
            continue
        for cells in table_rows([line]):
            if len(cells) < 2:
                continue
            if cells[0].lower() in ("#", "no", "num"):
                continue
            if not re.fullmatch(r"\d+", cells[0].strip()):
                continue
            labels.append(cells[1])
    return meta, labels


def norm_label(label):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", label or "")).strip().lower()


def snip(text, limit=60):
    """Trim a sentence for a finding line, with an ellipsis only when it was cut."""
    text = " ".join(text.split())
    return text if len(text) <= limit else text[:limit].rstrip() + "..."


def est_s(word_count):
    return word_count / WPS


def as_int(value, default=None):
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return default


# ---- checks ----------------------------------------------------------------
def carries_new_info(beat):
    """A beat is new information when it carries a number, a cue or a named thing."""
    text = "%s %s" % (beat["narration"], beat["on_screen"])
    if beat["cue"].strip():
        return True
    if DIGIT_RE.search(text) or NUMBER_WORD_RE.search(text):
        return True
    for sent in sentences(beat["narration"]):
        toks = re.findall(r"[A-Za-z][\w'.-]*", sent)
        for tok in toks[1:]:
            if tok[0].isupper() and tok.lower() != "i":
                return True
    return False


def check(script_path, narration_path, outline_path):
    bl, adv, warn = [], [], []
    if _IMPORT_WARNING:
        warn.append(_IMPORT_WARNING)

    script_text = Path(script_path).read_text(encoding="utf-8")
    meta, chapters = parse_script(script_text)
    beats = [b for c in chapters for b in c["beats"]]

    outline_meta, outline_labels = {}, []
    if outline_path:
        o_text = Path(outline_path).read_text(encoding="utf-8")
        outline_meta, outline_labels = parse_outline(o_text)
    else:
        warn.append("no --outline: the chapter-order check did not run")

    structure = (meta.get("structure") or outline_meta.get("structure") or "").strip()
    if not structure:
        warn.append("no `structure` in the script or outline frontmatter; "
                    "positional labels are judged as if the shape were not build-along")
    elif structure not in KNOWN_STRUCTURES:
        warn.append("structure '%s' is not in the episode-structures library (allowed; informational)"
                    % structure)

    if narration_path:
        narration = Path(narration_path).read_text(encoding="utf-8")
    else:
        narration = " ".join(b["narration"] for b in beats)
        warn.append("no --narration: the beat narrations were joined instead")
    narration = re.sub(r"\[measured\]", " ", narration)
    ws = words(narration)
    sents = sentences(narration)

    # ---- blockers ----------------------------------------------------------
    target_minutes = as_int(outline_meta.get("target_minutes"),
                            as_int(meta.get("target_minutes")))
    if target_minutes is None:
        adv.append("no target_minutes in the outline or the script: the word band was not checked")
    else:
        want = target_minutes * WPM
        lo, hi = int(want * (1 - BAND)), int(want * (1 + BAND))
        if not lo <= len(ws) <= hi:
            bl.append("narration %d words outside %d-%d for %d target minutes "
                      "(%d words per minute, plus or minus %d percent)"
                      % (len(ws), lo, hi, target_minutes, int(WPM), int(BAND * 100)))

    if not chapters:
        bl.append("no '## Chapter N: label' headings found in the script")
    elif len(chapters) < MIN_CHAPTERS:
        bl.append("%d chapters, fewer than the %d minimum" % (len(chapters), MIN_CHAPTERS))
    for c in chapters:
        c_words = sum(len(words(b["narration"])) for b in c["beats"])
        if est_s(c_words) < MIN_CHAPTER_S:
            bl.append("chapter %s '%s': ~%.0fs (%d words) under the %ds minimum"
                      % (c["num"], c["label"], est_s(c_words), c_words, MIN_CHAPTER_S))

    if not beats:
        bl.append("no beat rows found: every chapter needs a beat table")
    for b in beats:
        n = len(words(b["narration"]))
        if not BEAT_WORDS[0] <= n <= BEAT_WORDS[1]:
            bl.append("beat %s: %d words outside %d-%d"
                      % (b["id"], n, BEAT_WORDS[0], BEAT_WORDS[1]))
        if "[measured]" in b["narration"].lower() and not b["cue"].strip():
            bl.append("beat %s: a [measured] number with no capture cue id" % b["id"])

    if outline_labels:
        script_labels = [c["label"] for c in chapters]
        if len(script_labels) != len(outline_labels):
            bl.append("%d script chapters vs %d outline chapters"
                      % (len(script_labels), len(outline_labels)))
        for i, (a, b_) in enumerate(zip(script_labels, outline_labels), start=1):
            if norm_label(a) != norm_label(b_):
                bl.append("chapter %d label '%s' does not match the outline's '%s'" % (i, a, b_))

    # ---- advisories --------------------------------------------------------
    low = " " + narration.lower() + " "
    for p in BANNED_HYPE:
        if p in low:
            adv.append("banned hype: '%s'" % p)
    for p in BANNED_CTA:
        if p in low:
            adv.append("spoken CTA phrase: '%s' -- the ask lives in the description" % p)
    head = " ".join(sents[:3]).lower()
    for p in LONGFORM_OPENERS:
        if p in head:
            adv.append("banned opener: '%s'" % p)

    lens = [len(words(s)) for s in sents]
    for s, n in zip(sents, lens):
        if n > SENTENCE_CAP:
            adv.append("sentence >%d words (%d): '%s'" % (SENTENCE_CAP, n, snip(s)))
    if lens and sum(lens) / len(lens) > SENTENCE_AVG_MAX:
        adv.append("avg sentence %.1f words > %d" % (sum(lens) / len(lens), SENTENCE_AVG_MAX))

    labels = [s for s in sents if LABEL_RE.match(s)]
    if labels and structure != LABEL_STRUCTURE:
        for s in labels:
            adv.append("positional label outside %s ('%s'): '%s'"
                       % (LABEL_STRUCTURE, structure or "unset", snip(s, 50)))
    elif len(labels) > MAX_LABELS:
        adv.append("%d positional labels, at most %d in a %s episode"
                   % (len(labels), MAX_LABELS, LABEL_STRUCTURE))
    for s in labels:
        if len(words(s)) < 6:
            warn.append("positional label carries no action: '%s'" % snip(s))

    if sents and not SECOND_PERSON_RE.search(" ".join(sents[:3])):
        adv.append("no second-person marker in the first three sentences: "
                   "name the viewer's situation")

    run_s, run_ids = 0.0, []
    for b in beats:
        dur = est_s(len(words(b["narration"])))
        if carries_new_info(b):
            if run_s > NEW_INFO_GAP_S:
                adv.append("~%.0fs with no new information (beats %s to %s): a number, "
                           "a named thing or a step at least every %ds"
                           % (run_s, run_ids[0], run_ids[-1], NEW_INFO_GAP_S))
            run_s, run_ids = 0.0, []
        else:
            run_s += dur
            run_ids.append(b["id"])
    if run_s > NEW_INFO_GAP_S and run_ids:
        adv.append("~%.0fs with no new information (beats %s to %s): a number, "
                   "a named thing or a step at least every %ds"
                   % (run_s, run_ids[0], run_ids[-1], NEW_INFO_GAP_S))

    opening = " ".join(ws[:int(HOOK_NUMBER_S * WPS)])
    if ws and not (DIGIT_RE.search(opening) or NUMBER_WORD_RE.search(opening)):
        adv.append("no number in the first %d words (~0:%d): the surprising number is "
                   "spoken by 0:%d and shown at the same moment"
                   % (int(HOOK_NUMBER_S * WPS), HOOK_NUMBER_S, HOOK_NUMBER_S))

    found = [m.group(0).strip().lower() for m in ANALOGY_RE.finditer(narration)]
    if len(found) > MAX_ANALOGIES:
        adv.append("%d analogy markers (%s) -- one analogy per episode, carried the whole way"
                   % (len(found), ", ".join(sorted(set(found))[:4])))

    declared = as_int(meta.get("words"))
    if declared is not None and abs(declared - len(ws)) > max(25, 0.05 * len(ws)):
        warn.append("frontmatter words: %d, narration has %d" % (declared, len(ws)))
    declared_ch = as_int(meta.get("chapters"))
    if declared_ch is not None and declared_ch != len(chapters):
        warn.append("frontmatter chapters: %d, script has %d" % (declared_ch, len(chapters)))

    report = {
        "file": str(script_path),
        "structure": structure or None,
        "target_minutes": target_minutes,
        "chapters": len(chapters),
        "beats": len(beats),
        "words": len(ws),
        "est_speech_s": round(est_s(len(ws)), 1),
        "blockers": bl,
        "advisories": adv,
        "violations": bl + adv,
        "warnings": warn,
    }
    return report


def render_text(r, dry_run):
    out = ["validate_longform: %s" % r["file"],
           "  structure %s | chapters %d | beats %d | words %d (~%.1f min at %d wpm)"
           % (r["structure"] or "unset", r["chapters"], r["beats"], r["words"],
              r["est_speech_s"] / 60.0, int(WPM))]
    for tier in ("blockers", "advisories", "warnings"):
        out.append("  %s (%d)" % (tier.upper(), len(r[tier])))
        for item in r[tier]:
            out.append("    - %s" % item)
    verdict = ("blockers" if r["blockers"]
               else "advisories only" if r["advisories"] else "clean")
    out.append("  result: %s%s" % (verdict, " (dry run, exit 0)" if dry_run else ""))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(
        description="Machine gate for a long-form script: blockers exit 1, advisories exit 3, clean exit 0.",
        epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--script", help="path to [slug]-script.md")
    ap.add_argument("--narration", default=None,
                    help="path to [slug]-narration.txt (default: join the beat narrations)")
    ap.add_argument("--outline", default=None,
                    help="path to [slug]-outline.md (supplies target_minutes and the chapter list)")
    ap.add_argument("--json", action="store_true", help="print the JSON report instead of the text one")
    ap.add_argument("--dry-run", action="store_true",
                    help="run every check, print the report, then exit 0 whatever it found")
    args = ap.parse_args()
    if not args.script:
        print(__doc__)
        sys.exit(2)
    for label, path in (("script", args.script), ("narration", args.narration),
                        ("outline", args.outline)):
        if path and not Path(path).is_file():
            print("validate_longform: no such %s file: %s" % (label, path), file=sys.stderr)
            sys.exit(2)

    report = check(args.script, args.narration, args.outline)
    if args.dry_run:
        report["dry_run"] = True
    print(json.dumps(report, indent=2) if args.json else render_text(report, args.dry_run))
    if args.dry_run:
        sys.exit(0)
    if report["blockers"]:
        sys.exit(1)
    if report["advisories"]:
        sys.exit(3)
    sys.exit(0)


if __name__ == "__main__":
    main()
