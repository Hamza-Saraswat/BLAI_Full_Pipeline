#!/usr/bin/env python3
"""Write the stage-07 render note from machine outputs (no agent prose).

    render_note.py --slug S --assemble-json OUT/assemble.json --workers-dir BUILD/workers \
                   --timing BUILD/timing.json --voice-json BUILD/voice/voice.json \
                   --out stages/07-render/output/S-render.md [--card-message-id N] [--decision TEXT ...]

Same shape the render stage always produced (frontmatter with the gate verdicts, Gates, Scene
timings and attempts, Assembly, Decisions, Card) so `check_outputs.py` and the hub note's
Artifacts link keep working. Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import pathlib
import sys


def _cue(c) -> str:
    """assemble.py emits sfx cues as dicts ({sfx|name, at_ms|ms|start_ms}); older notes wrote 'pop@0ms'."""
    if isinstance(c, dict):
        name = c.get("sfx") or c.get("name") or c.get("id") or "sfx"
        at = c.get("at_ms", c.get("ms", c.get("start_ms", "")))
        return "%s@%sms" % (name, at) if at != "" else str(name)
    return str(c)


def load(path: str, default):
    p = pathlib.Path(path) if path else None
    if not p or not p.exists():
        return default
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except ValueError:
        return default


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--assemble-json", required=True)
    ap.add_argument("--workers-dir", required=True)
    ap.add_argument("--timing", required=True)
    ap.add_argument("--voice-json", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--card-message-id", default="")
    ap.add_argument("--decision", action="append", default=[])
    a = ap.parse_args()

    asm = load(a.assemble_json, {})
    timing = load(a.timing, [])
    voice = load(a.voice_json, {})
    handbacks = [load(f, {}) for f in sorted(glob.glob(str(pathlib.Path(a.workers_dir) / "*" / "handback.json")))]
    hb_by = {h.get("scene_id"): h for h in handbacks if h.get("scene_id")}
    order = [str(t.get("scene_id")) for t in timing] or sorted(hb_by)
    rendered = [s for s in order if hb_by.get(s, {}).get("status") == "ok"]
    lint, sz, loop = asm.get("lint_ok"), asm.get("safe_zone_ok"), asm.get("loop_ok")
    dur = float(asm.get("duration_s") or 0)
    narr = float(voice.get("duration_s") or 0)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = ["---", "slug: %s" % a.slug, "duration_s: %.2f" % dur,
             "gate_lint: %s" % ("pass" if lint else "fail"), "gate_safe_zone: %s" % ("pass" if sz else "fail"),
             "gate_loop: %s" % ("pass" if loop else ("fail" if loop is False else "n/a")),
             "loop_ssim: %s" % asm.get("loop_ssim", ""), "---", "",
             "# Render: %s" % a.slug, "",
             "Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at %s." % stamp, "",
             "## Gates",
             "- lint_video --final: %s (duration %.2f s)" % ("pass" if lint else "FAIL", dur),
             "- safe_zone_check: %s" % ("pass" if sz else "FAIL"),
             "- loop_check: %s (ssim %s)" % ("similar" if loop else ("not similar" if loop is False else "n/a"), asm.get("loop_ssim", "")),
             "- Length: %.2f s; narration %.2f s" % (dur, narr),
             "- Scenes: %d/%d storyboard scenes rendered (%s)" % (len(rendered), len(order), ", ".join(rendered) or "none"),
             "- Captions: %s words; sfx cues %s; music %s" % (asm.get("caption_words", ""),
                                                            ", ".join(_cue(c) for c in (asm.get("sfx_cues") or [])) or "none",
                                                            asm.get("music") or "none"), "",
             "## Scene timings and attempts", "",
             "| Scene | Target s | Delivered s | Attempts | Model | Flags |", "|-------|----------|-------------|----------|-------|-------|"]
    tmap = {str(t.get("scene_id")): t for t in timing}
    for s in order:
        h, t = hb_by.get(s, {}), tmap.get(s, {})
        model = ((h.get("usage") or [{}])[-1] or {}).get("model", "")
        lines.append("| %s | %.2f | %.2f | %s | %s | %s |" % (
            s, float(t.get("duration_s") or h.get("target_s") or 0), float(h.get("duration_s") or 0),
            h.get("attempts", ""), model, "; ".join(h.get("flagged") or []) or ("FAILED: " + h.get("status", "")
                                                                                if h.get("status", "").startswith("failed") else "")))
    lines += ["", "## Assembly"]
    lines += ["- %s" % w for w in (asm.get("warnings") or [])] or ["- no assembler warnings"]
    lines += ["- props: %s" % asm.get("props", ""), "", "## Decisions (unattended)"]
    lines += ["- %s" % d for d in a.decision] or ["- scripted render: no checkpoint reached a human; every gate above is machine-decided"]
    lines += ["", "## Card", "- gate card sent: message_id %s" % (a.card_message_id or "(not sent)"), ""]
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"out": str(out), "scenes_ok": len(rendered), "scenes": len(order),
                      "gates_ok": bool(lint and sz)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
