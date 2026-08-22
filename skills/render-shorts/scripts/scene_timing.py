#!/usr/bin/env python3
"""scene_timing.py: per-scene time slots from the storyboard and word-timed captions.

Port of the timing half of v1 render/remotion/scripts/align-captions.mjs.
The narration plays straight through while scene clips play back to back, so
scenes must tile the voice timeline contiguously: scene i runs from its first
word to scene i+1's first word (speech gaps are absorbed by the earlier
scene), scene 1 starts at 0, and only the last scene gets a 1.0 s hold.

Usage:
  scene_timing.py --storyboard FILE.json --captions captions.json [--out timing.json]
                  [--narration-norm FILE.json] [--dry-run]

captions.json accepts either shape:
  [{"word": "Hello", "start": 0.12, "end": 0.40}]          (elevenlabs-narration; seconds)
  [{"text": " Hello", "startMs": 120, "endMs": 400, ...}]  (@remotion/captions)
Seconds vs milliseconds is auto-detected (a Short never exceeds 400 s).

Output (stdout, and --out when given):
  [{"scene_id": "s1", "start_ms": 0, "end_ms": 5120, "duration_s": 5.12, "words": 14}, ...]
Exit 0 on success, 1 on failure, 3 when the caption word count drifts more
than 10 % from the script (the slots are still written; review them).
Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional

LAST_SCENE_EXTRA_MS = 1000
WORD_RE = re.compile(r"[\w']+")


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text or ""))


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def normalize_captions(raw: Any) -> List[Dict[str, Any]]:
    """Return [{text, startMs, endMs, timestampMs, confidence}] with non-empty words.

    `text` carries a leading space for every word after the first, which is
    what @remotion/captions expects (whitespace-sensitive rendering).
    """
    if isinstance(raw, dict):
        for key in ("captions", "words"):
            if isinstance(raw.get(key), list):
                raw = raw[key]
                break
    if not isinstance(raw, list):
        raise ValueError("captions must be a JSON list")
    items = []
    for c in raw:
        if not isinstance(c, dict):
            continue
        if "startMs" in c:
            text = str(c.get("text", ""))
            start, end = float(c["startMs"]), float(c.get("endMs", c["startMs"]))
            scale = 1.0
        else:
            text = str(c.get("word", c.get("text", "")))
            start, end = float(c.get("start", 0.0)), float(c.get("end", c.get("start", 0.0)))
            scale = None  # decided below
        if not text.strip():
            continue
        items.append([text, start, end, c.get("confidence"), scale])
    if not items:
        return []
    # unit detection for {word,start,end}: values above 400 can only be ms
    needs_unit = [i for i in items if i[4] is None]
    if needs_unit:
        max_end = max(i[2] for i in needs_unit)
        unit = 1.0 if max_end > 400 else 1000.0
        for i in needs_unit:
            i[4] = unit
    out = []
    for idx, (text, start, end, conf, scale) in enumerate(items):
        start_ms = int(round(start * scale))
        end_ms = max(start_ms, int(round(end * scale)))
        word = text.strip()
        out.append({
            "text": word if idx == 0 else " " + word,
            "startMs": start_ms,
            "endMs": end_ms,
            "timestampMs": int(round((start_ms + end_ms) / 2)),
            "confidence": float(conf) if isinstance(conf, (int, float)) else None,
        })
    return out


def scene_word_counts(storyboard: Dict[str, Any], norm: Optional[Dict[str, Any]]) -> List[int]:
    scenes = storyboard.get("scenes") or []
    if norm and isinstance(norm.get("scenes"), list) and len(norm["scenes"]) == len(scenes):
        return [count_words(s.get("text", "")) for s in norm["scenes"]]
    return [count_words(s.get("narration", "")) for s in scenes]


def compute_timing(storyboard: Dict[str, Any], words: List[Dict[str, Any]],
                   norm: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    scenes = storyboard.get("scenes") or []
    if not scenes:
        raise ValueError("storyboard has no scenes")
    if not words:
        raise ValueError("captions contain no words")
    counts = scene_word_counts(storyboard, norm)
    total = sum(counts) or 1
    n = len(words)
    bounds = []
    cum = 0
    prev = 0
    for i in range(len(scenes)):
        cum += counts[i]
        if i == len(scenes) - 1:
            end_idx = n
        else:
            end_idx = max(prev + 1, int(round(n * cum / total)))
            end_idx = min(end_idx, n - (len(scenes) - 1 - i))  # leave a word for each later scene
            end_idx = max(end_idx, prev + 1)
        bounds.append((prev, end_idx))
        prev = end_idx
    timing = []
    for i, scene in enumerate(scenes):
        start_idx, end_idx = bounds[i]
        start_idx = min(start_idx, n - 1)
        end_idx = max(start_idx + 1, min(end_idx, n))
        chunk = words[start_idx:end_idx]
        is_last = i == len(scenes) - 1
        start_ms = 0 if i == 0 else words[start_idx]["startMs"]
        if is_last:
            end_ms = chunk[-1]["endMs"] + LAST_SCENE_EXTRA_MS
        else:
            end_ms = words[end_idx]["startMs"] if end_idx < n else chunk[-1]["endMs"]
        end_ms = max(end_ms, start_ms + 1)
        timing.append({
            "scene_id": scene.get("id", "s%d" % (i + 1)),
            "start_ms": int(start_ms),
            "end_ms": int(end_ms),
            "duration_s": round((end_ms - start_ms) / 1000.0, 2),
            "words": len(chunk),
        })
    return timing


def scene_words(words: List[Dict[str, Any]], slot: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Caption words whose start falls inside a timing slot, re-based to the scene."""
    out = []
    for w in words:
        if slot["start_ms"] <= w["startMs"] < slot["end_ms"]:
            out.append({
                "text": w["text"].strip(),
                "startMs": w["startMs"] - slot["start_ms"],
                "endMs": w["endMs"] - slot["start_ms"],
            })
    return out


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--storyboard", required=True)
    ap.add_argument("--captions", required=True)
    ap.add_argument("--out", help="write timing.json here (stdout always gets the JSON)")
    ap.add_argument("--narration-norm", help="optional v1-style normalized narration JSON {full, scenes[{text}]}")
    ap.add_argument("--dry-run", action="store_true", help="compute but never write --out")
    args = ap.parse_args(argv)
    try:
        storyboard = load_json(args.storyboard)
        words = normalize_captions(load_json(args.captions))
        norm = load_json(args.narration_norm) if args.narration_norm and os.path.exists(args.narration_norm) else None
        timing = compute_timing(storyboard, words, norm)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        log("scene_timing: %s" % exc)
        return 1
    script_words = count_words(norm["full"]) if norm and norm.get("full") else count_words(storyboard.get("narration_full", ""))
    drift = abs(len(words) - script_words) / float(script_words or 1)
    if args.out and not args.dry_run:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(timing, fh, indent=2)
        log("scene_timing: wrote %s" % args.out)
    print(json.dumps(timing, indent=2))
    log("scene_timing: %d caption words vs %d script words, drift %.1f%%"
        % (len(words), script_words, drift * 100))
    if drift > 0.10:
        log("scene_timing: WARN word-count drift above 10%%, review the slots")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
