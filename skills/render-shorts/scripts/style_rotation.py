#!/usr/bin/env python3
"""style_rotation.py: pick or record the style pack for a video.

Rule (from styles/README.md): never the same pack twice in a row, one pack per
video, pick by topic fit, record the pick when the storyboard is approved.

Usage:
  style_rotation.py --pick --slug S [--history styles/history.json] [--storyboard FILE.json]
                    [--topic "text"] [--exclude PACK[,PACK]] [--json]
  style_rotation.py --record PACK --slug S [--history styles/history.json] [--date YYYY-MM-DD]
                    [--force] [--dry-run]

--pick prints the chosen pack name on stdout (or a JSON object with --json:
{pack, last, reason, scores}). Topic-fit hints come from the storyboard's
topic, title, hook_text and narration when --storyboard is given, or from
--topic. Ties go to the least recently used pack. With no hints the default
pack (signal) wins unless it was the last one used.

--exclude removes packs from the candidate set on top of the never-twice rule. Two Shorts
produced the same morning run --pick concurrently, and the ledger only records on approval,
so without it both draws return the same pack (finding 8, 2026-08-23 dry run): the second
pick passes the first pick's pack via --exclude.

--record appends {slug, pack, date} to the history file and refuses a pack
that equals the previous entry (unless --force) or is not a known pack.
Exit 0 on success, 1 on failure. Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_HISTORY = os.path.join(HERE, "..", "styles", "history.json")
PACKS = ["signal", "terminal", "sketch", "blueprint", "axon", "halftone", "silicon"]
DEFAULT_PACK = "signal"

# Topic-fit keywords per pack (summary of the selection table in styles/README.md).
HINTS: Dict[str, List[str]] = {
    "terminal": ["cli", "command", "terminal", "install", "setup", "docker", "ollama", "vllm",
                 "llama.cpp", "llama-server", "serve", "flag", "config", "api key", "script",
                 "how to", "step by step", "run it", "curl", "pip ", "npm "],
    "sketch": ["intuition", "analogy", "think of", "imagine", "like a", "picture a", "why does",
               "what is", "explained", "concept", "metaphor", "napkin", "in plain"],
    "blueprint": ["architecture", "how it works", "internals", "under the hood", "kv cache",
                  "attention", "layer", "pipeline", "request flow", "scheduler", "unified memory",
                  "cache", "container", "diagram"],
    "axon": ["topology", "data flow", "inside the box", "routes", "routing", "cluster", "network",
             "system", "moe", "mixture of experts", "experts", "tokens flow", "what happens inside",
             "between machines", "multi-node"],
    "halftone": ["hot take", "myth", " vs ", "versus", "face-off", "showdown", "wrong", "actually",
                 "everyone says", "overrated", "underrated", "beats", "beat ", "benchmark war",
                 "unpopular", "truth"],
    "silicon": ["gpu", "vram", "bandwidth", "quantization", "quantized", "hardware", "chip",
                "memory bus", "tokens per second", "tok/s", "dgx", "spark", "nvidia", "apple silicon",
                "m4", "rtx", "cuda", "watt", "thermal", "die", "hbm", "gddr"],
    "signal": ["benchmark", "comparison", "compare", "news", "released", "launch", "announce",
               "numbers", "price", "cost", "ranking", "top 5", "update"],
}


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def load_history(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {"_rule": "Append on storyboard approval. Never the same pack as the last entry.", "used": []}
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict) or not isinstance(data.get("used"), list):
        raise ValueError("history file must be an object with a 'used' list")
    return data


def last_pack(history: Dict[str, Any]) -> Optional[str]:
    used = [u for u in history.get("used", []) if isinstance(u, dict) and u.get("pack")]
    return used[-1]["pack"] if used else None


def hint_text(storyboard_path: Optional[str], topic: Optional[str]) -> str:
    parts: List[str] = []
    if topic:
        parts.append(topic)
    if storyboard_path:
        with open(storyboard_path, encoding="utf-8") as fh:
            sb = json.load(fh)
        for key in ("topic", "title", "hook_text", "narration_full"):
            val = sb.get(key)
            if isinstance(val, str):
                parts.append(val)
        for scene in sb.get("scenes") or []:
            if isinstance(scene, dict):
                parts.append(str(scene.get("visual_brief", "")))
    return " ".join(parts).lower()


def score_packs(text: str) -> Dict[str, int]:
    scores = {p: 0 for p in PACKS}
    for pack, words in HINTS.items():
        for w in words:
            w_l = w.lower()
            if w_l.strip() and w_l in text:
                scores[pack] += len(re.findall(re.escape(w_l), text))
    return scores


def recency_rank(history: Dict[str, Any]) -> Dict[str, int]:
    """Higher value = used longer ago (never used = highest)."""
    used = [u.get("pack") for u in history.get("used", []) if isinstance(u, dict)]
    rank = {}
    for p in PACKS:
        if p in used:
            rank[p] = len(used) - 1 - max(i for i, x in enumerate(used) if x == p)
        else:
            rank[p] = len(used) + 1
    return rank


def pick(history: Dict[str, Any], text: str, exclude: Optional[List[str]] = None) -> Dict[str, Any]:
    last = last_pack(history)
    scores = score_packs(text)
    rec = recency_rank(history)
    banned = {last} | set(exclude or [])
    candidates = [p for p in PACKS if p not in banned] or [p for p in PACKS if p != last]
    best_score = max(scores[p] for p in candidates)
    if best_score > 0:
        top = [p for p in candidates if scores[p] == best_score]
        chosen = sorted(top, key=lambda p: (-rec[p], PACKS.index(p)))[0]
        reason = "topic fit (%d keyword hits)" % best_score
        if len(top) > 1:
            reason += ", tie broken by least recent use"
    elif DEFAULT_PACK in candidates:
        chosen = DEFAULT_PACK
        reason = "no topic hints, default pack"
    else:
        chosen = sorted(candidates, key=lambda p: (-rec[p], PACKS.index(p)))[0]
        reason = "no topic hints, default pack was used last, least recently used instead"
    if last:
        reason += "; previous pack was %s" % last
    return {"pack": chosen, "last": last, "reason": reason, "scores": scores}


def record(history_path: str, pack: str, slug: str, date: str, force: bool, dry_run: bool) -> int:
    if pack not in PACKS:
        log("style_rotation: unknown pack %r (known: %s)" % (pack, ", ".join(PACKS)))
        return 1
    history = load_history(history_path)
    last = last_pack(history)
    if last == pack and not force:
        log("style_rotation: refusing to record %s twice in a row (last entry is %s); use --force to override" % (pack, last))
        return 1
    entry = {"slug": slug, "pack": pack, "date": date}
    history["used"].append(entry)
    if dry_run:
        log("style_rotation: dry run, would append %s to %s" % (json.dumps(entry), history_path))
        print(json.dumps(entry))
        return 0
    os.makedirs(os.path.dirname(os.path.abspath(history_path)), exist_ok=True)
    with open(history_path, "w", encoding="utf-8") as fh:
        json.dump(history, fh, indent=2)
        fh.write("\n")
    log("style_rotation: recorded %s for %s in %s" % (pack, slug, history_path))
    print(json.dumps(entry))
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--pick", action="store_true", help="print the next pack")
    mode.add_argument("--record", metavar="PACK", help="append PACK for --slug to the history")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--history", default=DEFAULT_HISTORY)
    ap.add_argument("--storyboard", help="storyboard JSON for topic-fit hints (--pick)")
    ap.add_argument("--topic", help="free text for topic-fit hints (--pick)")
    ap.add_argument("--exclude", default="", help="comma-separated packs to skip on top of the never-twice rule (--pick); pass the sibling Short's pack when two are produced the same day")
    ap.add_argument("--json", action="store_true", help="--pick prints a JSON object instead of the bare pack name")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="date for --record (default today)")
    ap.add_argument("--force", action="store_true", help="--record even if it repeats the last pack")
    ap.add_argument("--dry-run", action="store_true", help="--record prints the entry without writing")
    args = ap.parse_args(argv)
    try:
        if args.pick:
            history = load_history(args.history)
            result = pick(history, hint_text(args.storyboard, args.topic),
                          [x.strip() for x in args.exclude.split(",") if x.strip()])
            result["slug"] = args.slug
            log("style_rotation: %s (%s)" % (result["pack"], result["reason"]))
            print(json.dumps(result, indent=2) if args.json else result["pack"])
            return 0
        return record(args.history, args.record, args.slug, args.date, args.force, args.dry_run)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        log("style_rotation: %s" % exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
