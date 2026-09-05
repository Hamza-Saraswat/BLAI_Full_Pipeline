#!/usr/bin/env python3
"""Cut one packet per storyboard scene: the only thing a scene worker sees.

    scene_packets.py --storyboard sb.json --timing timing.json --out DIR [--tolerance 0.15]

Reads the storyboard's `scenes[]` (id, role, tool, layout_archetype, narration,
on_screen_text, visual_brief, sfx) and scene_timing.py's output
([{scene_id, start_ms, end_ms, duration_s, words}]), joins them on scene id and
writes DIR/<scene_id>-packet.json with exactly the keys the 2026-08-30 walk's
workers used, plus `pack` (the storyboard's style_pack). Prints one JSON line:
{"packets": N, "dir": DIR, "missing_timing": [...]}. Exit 1 when a scene has no
timing row. Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

KEYS = ("scene_id", "target_duration_s", "tolerance_s", "start_ms", "end_ms", "narration",
        "on_screen_text", "visual_brief", "tool", "layout_archetype", "role", "words", "sfx", "pack")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--storyboard", required=True)
    ap.add_argument("--timing", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tolerance", type=float, default=0.15)
    a = ap.parse_args()

    sb = json.loads(pathlib.Path(a.storyboard).read_text(encoding="utf-8"))
    timing = json.loads(pathlib.Path(a.timing).read_text(encoding="utf-8"))
    by_id = {str(t.get("scene_id")): t for t in timing}
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    pack = sb.get("style_pack", "")
    missing, n = [], 0
    for s in sb.get("scenes", []):
        sid = str(s.get("id") or s.get("scene_id"))
        t = by_id.get(sid)
        if not t:
            missing.append(sid)
            continue
        packet = {
            "scene_id": sid,
            "target_duration_s": round(float(t["duration_s"]), 2),
            "tolerance_s": a.tolerance,
            "start_ms": int(t["start_ms"]),
            "end_ms": int(t["end_ms"]),
            "narration": s.get("narration", ""),
            "on_screen_text": s.get("on_screen_text", ""),
            "visual_brief": s.get("visual_brief", ""),
            "tool": s.get("tool", "hyperframes"),
            "layout_archetype": s.get("layout_archetype", ""),
            "role": s.get("role", ""),
            "words": t.get("words"),
            "sfx": s.get("sfx"),
            "pack": pack,
        }
        (out / ("%s-packet.json" % sid)).write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n",
                                                    encoding="utf-8")
        n += 1
    print(json.dumps({"packets": n, "dir": str(out), "missing_timing": missing}))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
