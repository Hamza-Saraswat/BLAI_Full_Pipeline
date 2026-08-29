#!/usr/bin/env python3
"""Run every skill's documented verification before anything renders.

    python3 tools/preflight.py [--json] [--quick]

One line per check; exit 1 when any REQUIRED check fails. Exists because of
finding 33 (2026-08-23 dry run): the ICM validator proves a tool has a setup
guide, not that the guide was ever run -- Manim was documented, ported, and
never installed, and the first render would have died ten minutes in, after
voice had already succeeded. This is the cheap version of "run the guide":
each check is the skill's own documented smoke command or a file the render
path dereferences on its first frame.

Required checks gate a build. Optional checks degrade a feature and only warn
(whisper alignment falls back to proportional timing; ElevenLabs falls back to
Kokoro and vice versa -- one voice engine must be reachable, not both).
--quick skips the two slow checks (hyperframes --version, manim import).
Stdlib only. Safe to run anywhere; changes nothing.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
RS = ROOT / "skills" / "render-shorts"


def run(cmd, cwd=None, timeout=120):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr).strip()
    except FileNotFoundError:
        return 127, "not found"
    except subprocess.TimeoutExpired:
        return 124, "timed out"


def checks(quick: bool):
    # -- system binaries the assembly and linters shell out to ------------------
    for name in ("ffmpeg", "ffprobe"):
        path = shutil.which(name)
        yield {"check": name, "required": True, "ok": bool(path), "detail": path or "not on PATH"}
    node = shutil.which("node")
    ok, detail = (False, "not on PATH"), None
    if node:
        rc, out = run([node, "--version"], timeout=15)
        ok = (rc == 0 and out.startswith("v") and int(out[1:].split(".")[0]) >= 20, out)
    yield {"check": "node", "required": True, "ok": ok[0] if node else False,
           "detail": ok[1] if node else "not on PATH"}

    # -- HyperFrames: pinned local bin (rules/hyperframes-1.md) -----------------
    hf = RS / "hyperframes" / "node_modules" / ".bin" / "hyperframes"
    if not hf.exists():
        yield {"check": "hyperframes", "required": True, "ok": False,
               "detail": "%s missing: run `npm install` in skills/render-shorts/hyperframes" % hf}
    elif quick:
        yield {"check": "hyperframes", "required": True, "ok": True, "detail": "local bin present (--quick)"}
    else:
        rc, out = run([str(hf), "--version"], cwd=RS / "hyperframes", timeout=60)
        yield {"check": "hyperframes", "required": True, "ok": rc == 0,
               "detail": out.splitlines()[-1] if out else "exit %d" % rc}
    gsap = RS / "hyperframes" / "packs" / "vendor" / "gsap.min.js"
    yield {"check": "gsap-vendored", "required": True, "ok": gsap.exists() and gsap.stat().st_size > 50000,
           "detail": str(gsap) if gsap.exists() else "missing: renders would need the CDN (finding 54)"}

    # -- Manim venv (manim/SETUP-NOTES.md; finding 33) --------------------------
    venv_py = RS / "manim" / ".venv" / "bin" / "python"
    if not venv_py.exists():
        yield {"check": "manim", "required": True, "ok": False,
               "detail": "venv missing: run the setup.md command in skills/render-shorts (finding 33)"}
    elif quick:
        yield {"check": "manim", "required": True, "ok": True, "detail": "venv present (--quick)"}
    else:
        rc, out = run([str(venv_py), "-c",
                       "import manim, blai_layout, blai_packs; print(manim.__version__)"],
                      cwd=RS / "manim", timeout=90)
        yield {"check": "manim", "required": True, "ok": rc == 0,
               "detail": ("manim " + out.splitlines()[-1]) if rc == 0 else out[-200:]}

    # -- Remotion assembly project ---------------------------------------------
    rem = RS / "remotion" / "node_modules"
    yield {"check": "remotion-deps", "required": True, "ok": rem.is_dir(),
           "detail": "node_modules present" if rem.is_dir()
           else "run `npm install` in skills/render-shorts/remotion"}

    # -- voice: at least one engine must be reachable ---------------------------
    eleven = bool(os.environ.get("ELEVENLABS_API_KEY")) and bool(os.environ.get("ELEVEN_VOICE_ID"))
    kroot = pathlib.Path(os.environ.get("BLAI_KOKORO_ROOT", "").strip() or
                         (pathlib.Path.home() / "Documents" / "Projects" / "BLAI_Animator"))
    kokoro = (kroot / "pipeline" / "models" / "kokoro-v1.0.onnx").exists()
    yield {"check": "voice-engine", "required": True, "ok": eleven or kokoro,
           "detail": ("elevenlabs keys set" if eleven else "") +
                     (" + " if eleven and kokoro else "") +
                     ("kokoro model at %s" % kroot if kokoro else "") or
                     "no ELEVENLABS_API_KEY/ELEVEN_VOICE_ID and no kokoro model (BLAI_KOKORO_ROOT)"}

    # -- optional: whisper alignment (captions fall back to proportional) -------
    wbin = (os.environ.get("WHISPER_CPP_BIN") or "").strip()
    wroot = kroot / "render" / "remotion" / "whisper.cpp"
    wcands = ([pathlib.Path(wbin)] if wbin else []) + \
             [wroot / "build" / "bin" / "whisper-cli", wroot / "build" / "bin" / "main", wroot / "main"]
    whisper = next((c for c in wcands if c.exists()), None)
    yield {"check": "whisper-align", "required": False, "ok": whisper is not None,
           "detail": str(whisper) if whisper else "not found: word timing falls back to proportional"}

    # -- optional: publish path scoping guard -----------------------------------
    gs = ROOT / "tools" / "git-sync.sh"
    yield {"check": "git-sync", "required": False, "ok": gs.exists() and os.access(gs, os.X_OK),
           "detail": "executable" if os.access(gs, os.X_OK) else "not executable"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="one JSON object per line, no summary prose")
    ap.add_argument("--quick", action="store_true", help="skip the slow version probes")
    a = ap.parse_args()
    failed_required = 0
    warned = 0
    for c in checks(a.quick):
        if a.json:
            print(json.dumps(c))
        else:
            mark = "OK  " if c["ok"] else ("FAIL" if c["required"] else "warn")
            print("%s %-16s %s" % (mark, c["check"], c["detail"]))
        if not c["ok"]:
            if c["required"]:
                failed_required += 1
            else:
                warned += 1
    if not a.json:
        print("preflight: %s (%d warning(s))" %
              ("all required checks pass" if not failed_required
               else "%d REQUIRED check(s) failed" % failed_required, warned))
    return 1 if failed_required else 0


if __name__ == "__main__":
    sys.exit(main())
