#!/usr/bin/env python3
"""safe_zone_check.py <video-or-image> [--stills N] [--debug-dir DIR] [--scene]

--scene: additionally forbids the caption band (y 1260-1470) -- use for SCENE
renders (captions are composited there at assembly). Omit for final videos.

Verifies no bright (text-like) content sits in the UI-reserved margins of the
1080x1920 canvas. Brand background is dark navy (luma ~20); text is warm
white/amber (luma >170), so luminance in forbidden strips is a reliable proxy.

Forbidden strips (from AGENTS.md safe area 900x1160 centered, biased to the
real dangers): bottom 450px, right 120px, top 240px, left 90px.

Stdlib-only: samples N frames with ffmpeg, measures per-strip max luma via
signalstats through ffprobe. --debug-dir writes stills with the safe-area box
drawn. Exit 0 = pass, 1 = violations.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

STRIPS = {  # name: (w, h, x, y) crops on 1080x1920
    "bottom_450": (900, 450, 90, 1470),   # exclude right strip (counted once)
    "right_120": (120, 1920, 960, 0),
    "top_240": (900, 240, 90, 0),
    "left_90": (90, 1920, 0, 0),
}
# --scene mode only: captions own y 1260-1470 at assembly, so SCENE content
# must keep clear of it (prevents caption-over-diagram collisions like the
# CHEF overlap in video #1). Final videos legitimately have captions here.
SCENE_EXTRA_STRIPS = {
    "caption_band_1260_1470": (900, 210, 90, 1260),
}
YMAX_THRESHOLD = 140  # navy bg ~20-35; antialiased text edges push >150


def frame_times(path, n):
    dur = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
         "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True, check=True).stdout.strip())
    return [dur * (i + 0.5) / n for i in range(n)]


def extract_still(video, t, out_png):
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{t:.3f}",
         "-i", video, "-frames:v", "1", out_png], check=True)


def strip_ymax(png, crop):
    w, h, x, y = crop
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-f", "lavfi",
         f"movie={png},crop={w}:{h}:{x}:{y},signalstats",
         "-show_entries", "frame_tags=lavfi.signalstats.YMAX",
         "-of", "default=noprint_wrappers=1:nokey=1"],
        capture_output=True, text=True, check=True).stdout.strip()
    return int(float(out.splitlines()[0])) if out else 0


def draw_debug(png, out_png):
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", png,
         "-vf", "drawbox=x=90:y=240:w=900:h=1160:color=lime@0.9:t=4",
         out_png], check=True)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    src = args[0]
    n = int(sys.argv[sys.argv.index("--stills") + 1]) if "--stills" in sys.argv else 5
    strips = dict(STRIPS)
    if "--scene" in sys.argv:
        strips.update(SCENE_EXTRA_STRIPS)
    debug_dir = (Path(sys.argv[sys.argv.index("--debug-dir") + 1])
                 if "--debug-dir" in sys.argv else None)
    if debug_dir:
        debug_dir.mkdir(parents=True, exist_ok=True)

    is_image = src.lower().endswith((".png", ".jpg", ".jpeg"))
    violations, checked = [], []

    with tempfile.TemporaryDirectory() as td:
        stills = []
        if is_image:
            stills = [(0.0, src)]
        else:
            for i, t in enumerate(frame_times(src, n)):
                p = str(Path(td) / f"f{i}.png")
                extract_still(src, t, p)
                stills.append((t, p))

        for t, png in stills:
            frame_report = {"t": round(t, 2)}
            for name, crop in strips.items():
                ymax = strip_ymax(png, crop)
                frame_report[name] = ymax
                if ymax > YMAX_THRESHOLD:
                    violations.append(
                        f"t={t:.2f}s: bright content (YMAX={ymax}) in {name} strip")
            checked.append(frame_report)
            if debug_dir:
                draw_debug(png, str(debug_dir / f"safezone_t{t:.1f}.png"))

    print(json.dumps({"file": src, "threshold": YMAX_THRESHOLD,
                      "frames": checked, "violations": violations}, indent=2))
    sys.exit(1 if violations else 0)


if __name__ == "__main__":
    main()
