#!/usr/bin/env python3
"""Turn the character alignment into word captions (JSON) and an SRT file.

Usage:
  captions.py --alignment DIR/alignment.json --script FILE.txt --out DIR
              [--max-words 4] [--max-cue-s 1.8]

Words come from the alignment (split on whitespace; a word's start is its first character's
start, its end the last character's end). The alignment text is the aliased text that was sent
to ElevenLabs ("D G X" for "DGX"), so the words are then matched back onto the original script
words with difflib: 1:1 matches take the aligned time, replaced runs share the run's time span
proportionally to word length. The viewer sees the script's spelling with the voice's timing.

Outputs: DIR/captions.json [{word, start, end}] and DIR/captions.srt (cues of 3-4 words, at most
--max-cue-s seconds each, closed early at sentence punctuation). Exit 0/1. No network.
"""
from __future__ import annotations

import argparse
import difflib
import json
import pathlib
import re
import sys


def log(msg: str) -> None:
    sys.stderr.write("[captions] %s\n" % msg)
    sys.stderr.flush()


def words_from_alignment(al: dict) -> list:
    chars = al["characters"]
    starts = al["character_start_times_seconds"]
    ends = al["character_end_times_seconds"]
    words = []
    cur = []
    for c, s, e in zip(chars, starts, ends):
        if c.isspace():
            if cur:
                words.append({"word": "".join(x[0] for x in cur), "start": cur[0][1], "end": cur[-1][2]})
                cur = []
            continue
        cur.append((c, float(s), float(e)))
    if cur:
        words.append({"word": "".join(x[0] for x in cur), "start": cur[0][1], "end": cur[-1][2]})
    return words


def norm(w: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", w.lower())


def map_to_script(aligned: list, script_words: list) -> list:
    a_norm = [norm(w["word"]) for w in aligned]
    s_norm = [norm(w) for w in script_words]
    sm = difflib.SequenceMatcher(a=s_norm, b=a_norm, autojunk=False)
    out = []
    last_end = 0.0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                a = aligned[j1 + k]
                out.append({"word": script_words[i1 + k], "start": a["start"], "end": a["end"]})
                last_end = a["end"]
            continue
        if tag == "delete" or (tag == "replace" and j2 == j1):
            for k in range(i1, i2):
                out.append({"word": script_words[k], "start": last_end, "end": last_end})
            continue
        if tag == "insert":
            last_end = aligned[j2 - 1]["end"]
            continue
        span_start = aligned[j1]["start"]
        span_end = aligned[j2 - 1]["end"]
        block = script_words[i1:i2]
        total = float(sum(max(1, len(norm(w))) for w in block))
        t = span_start
        for w in block:
            share = (span_end - span_start) * max(1, len(norm(w))) / total
            out.append({"word": w, "start": round(t, 4), "end": round(t + share, 4)})
            t += share
        last_end = span_end
    return out


def srt_time(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return "%02d:%02d:%02d,%03d" % (h, m, s, ms)


def build_cues(words: list, max_words: int, max_cue_s: float) -> list:
    cues = []
    cur: list = []
    for w in words:
        if cur:
            too_long = (w["end"] - cur[0]["start"]) > max_cue_s
            if len(cur) >= max_words or too_long:
                cues.append(cur)
                cur = []
        cur.append(w)
        if re.search(r"[.!?]$", w["word"]) and len(cur) >= 3:
            cues.append(cur)
            cur = []
    if cur:
        cues.append(cur)
    return cues


def write_srt(cues: list, path: pathlib.Path) -> None:
    lines = []
    prev_end = 0.0
    for n, cue in enumerate(cues, 1):
        start = max(cue[0]["start"], prev_end)
        end = max(cue[-1]["end"], start + 0.2)
        prev_end = end
        lines += [str(n), "%s --> %s" % (srt_time(start), srt_time(end)), " ".join(w["word"] for w in cue), ""]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--alignment", required=True)
    ap.add_argument("--script", required=True, help="original narration text (viewer-facing spelling)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-words", type=int, default=4)
    ap.add_argument("--max-cue-s", type=float, default=1.8)
    args = ap.parse_args()

    al = json.loads(pathlib.Path(args.alignment).read_text(encoding="utf-8"))
    for key in ("characters", "character_start_times_seconds", "character_end_times_seconds"):
        if key not in al:
            raise SystemExit("alignment.json lacks %s" % key)
    script_words = pathlib.Path(args.script).read_text(encoding="utf-8").split()
    aligned = words_from_alignment(al)
    if not aligned:
        raise SystemExit("alignment has no words")
    words = map_to_script(aligned, script_words) if script_words else aligned
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "captions.json").write_text(json.dumps(words, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    cues = build_cues(words, args.max_words, args.max_cue_s)
    write_srt(cues, out / "captions.srt")
    log("%d aligned words -> %d script words, %d cues" % (len(aligned), len(words), len(cues)))
    print(json.dumps({"words": len(words), "cues": len(cues), "duration_s": round(words[-1]["end"], 3) if words else 0.0}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
