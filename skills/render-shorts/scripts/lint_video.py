#!/usr/bin/env python3
"""lint_video.py <video> [--final] [--max-s N] [--warn-band LO:HI]

Deterministic spec check for pipeline video artifacts. Stdlib-only (ffprobe/ffmpeg).

Scene mode (default): 1080x1920, 30fps, yuv420p, h264. Duration 2-25s. No audio required.
Final mode (--final):  same specs + duration <= max-s (default 60; warn outside
                       the warn band, default 28:47), audio stream present,
                       integrated loudness -14 LUFS +/- 1.5.

This script stays deliberately dumb: it does NOT read skills/script-gates/formats.json.
The caller (dashboard verify.ts) resolves the board's script_format and passes
--max-s/--warn-band for non-classic formats; the bare CLI is byte-identical to
the historical classic behavior.

Exit 0 = pass, exit 1 = fail (violations printed as JSON).
"""
import json
import re
import subprocess
import sys


def ffprobe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path],
        capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(out)


def measure_lufs(path):
    """Integrated loudness via ffmpeg loudnorm analysis pass."""
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", path,
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", proc.stderr, re.DOTALL)
    if not m:
        return None
    return float(json.loads(m.group(0))["input_i"])


def _flag_value(name, default):
    """--name VALUE from argv (manual style, matching the rest of this script)."""
    argv = sys.argv[1:]
    if name in argv:
        i = argv.index(name)
        if i + 1 < len(argv):
            return argv[i + 1]
    return default


def main():
    skip = set()
    argv = sys.argv[1:]
    for flag in ("--max-s", "--warn-band"):
        if flag in argv:
            i = argv.index(flag)
            skip.update({i, i + 1})
    args = [a for j, a in enumerate(argv) if not a.startswith("--") and j not in skip]
    final = "--final" in argv
    max_s = float(_flag_value("--max-s", 60.0))
    try:
        lo, hi = (float(x) for x in str(_flag_value("--warn-band", "28:47")).split(":"))
    except ValueError:
        lo, hi = 28.0, 47.0
    if not args:
        print(__doc__)
        sys.exit(2)
    path = args[0]

    info = ffprobe(path)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    duration = float(info["format"]["duration"])

    violations, warnings = [], []

    if v is None:
        violations.append("no video stream")
    else:
        if (v["width"], v["height"]) != (1080, 1920):
            violations.append(f"resolution {v['width']}x{v['height']} != 1080x1920")
        num, den = (int(x) for x in v["r_frame_rate"].split("/"))
        fps = num / den if den else 0
        if abs(fps - 30) > 0.05:
            violations.append(f"fps {fps:.3f} != 30")
        if v.get("pix_fmt") != "yuv420p":
            violations.append(f"pix_fmt {v.get('pix_fmt')} != yuv420p")
        if v.get("codec_name") != "h264":
            violations.append(f"codec {v.get('codec_name')} != h264")

    if final:
        if duration > max_s:
            violations.append(f"duration {duration:.2f}s > {max_s:.0f}s hard max")
        elif not (lo <= duration <= hi):
            warnings.append(f"duration {duration:.2f}s outside {lo:.0f}-{hi:.0f}s target")
        if a is None:
            violations.append("final video has no audio stream")
        else:
            lufs = measure_lufs(path)
            if lufs is None:
                warnings.append("could not measure loudness")
            elif abs(lufs - (-14.0)) > 1.5:
                violations.append(f"loudness {lufs:.1f} LUFS outside -14 +/- 1.5")
    else:
        if not (2.0 <= duration <= 25.0):
            violations.append(f"scene duration {duration:.2f}s outside 2-25s")

    result = {"file": path, "mode": "final" if final else "scene",
              "duration_s": round(duration, 2),
              "violations": violations, "warnings": warnings}
    print(json.dumps(result, indent=2))
    sys.exit(1 if violations else 0)


if __name__ == "__main__":
    main()
