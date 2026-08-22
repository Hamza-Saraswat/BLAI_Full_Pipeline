#!/usr/bin/env python3
"""Lint a rendered long-form episode against shared/platform-specs.md (long-form row).

Usage:
  lint_longform.py final.mp4 --target-s N [--chapters FILE.json] [--loudness-tolerance 1.5]

Checks (error unless noted): file exists; video h264, 1920x1080, 30 fps, yuv420p; an audio
stream (warn if not AAC 48 kHz); integrated loudness -14 LUFS +/- tolerance via ffmpeg
ebur128 (warn when ffmpeg lacks the filter; silent audio is an error); duration within
+/-10 % of --target-s; chapters (when given): first at 00:00, ascending, each 10 s or
longer, at least 3, all inside the video.

Prints a JSON report on stdout; exit 0 when every error-level check passes, else 1.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

TARGET_LUFS = -14.0
DURATION_TOLERANCE = 0.10
MIN_CHAPTER_S = 10
MIN_CHAPTERS = 3


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def ffprobe(path: Path) -> dict | None:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(path)],
            capture_output=True, text=True, check=True,
        ).stdout
        return json.loads(out)
    except (OSError, subprocess.CalledProcessError, ValueError):
        return None


def has_filter(name: str) -> bool:
    try:
        out = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True).stdout
    except OSError:
        return False
    return re.search(r"\s%s\s" % re.escape(name), out) is not None


def integrated_loudness(path: Path) -> float | None:
    """Integrated loudness in LUFS from ffmpeg's ebur128 scanner, None when unreadable."""
    try:
        proc = subprocess.run(
            ["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-filter_complex", "ebur128=peak=true", "-f", "null", "-"],
            capture_output=True, text=True,
        )
    except OSError:
        return None
    m = re.search(r"Integrated loudness:\s*\n\s*I:\s*(-?[0-9.]+|-inf)\s*LUFS", proc.stderr)
    if not m:
        return None
    return float("-inf") if m.group(1) == "-inf" else float(m.group(1))


def frame_rate(stream: dict) -> float | None:
    for key in ("r_frame_rate", "avg_frame_rate"):
        val = stream.get(key, "")
        if "/" in val:
            num, den = val.split("/", 1)
            try:
                if float(den) != 0:
                    return float(num) / float(den)
            except ValueError:
                pass
    return None


def load_chapters(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("chapters") or []
    out = []
    for c in data:
        if not isinstance(c, dict):
            continue
        start = c.get("start_s", c.get("start", c.get("t")))
        if start is None and isinstance(c.get("timestamp"), str):
            parts = [int(p) for p in c["timestamp"].split(":")]
            start = sum(p * 60 ** i for i, p in enumerate(reversed(parts)))
        if start is None:
            continue
        out.append({"label": str(c.get("label", "")), "start_s": float(start)})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--target-s", type=float, required=True, help="target duration in seconds (spec.target_duration_s)")
    ap.add_argument("--chapters", help="chapters.json: [{label, start_s}] (render_longform.py writes it)")
    ap.add_argument("--loudness-tolerance", type=float, default=1.5, help="LU around -14 LUFS (default 1.5)")
    args = ap.parse_args()

    path = Path(args.video)
    checks: list[dict] = []

    def check(name: str, ok: bool, value, expected, level: str = "error", detail: str = "") -> None:
        checks.append({"name": name, "pass": bool(ok), "value": value, "expected": expected, "level": level, "detail": detail})

    if not path.exists():
        check("exists", False, str(path), "file present")
        report = {"file": str(path), "pass": False, "checks": checks}
        print(json.dumps(report, indent=2))
        return 1
    check("exists", True, str(path), "file present")

    info = ffprobe(path)
    if info is None:
        check("ffprobe", False, None, "ffprobe readable", detail="ffprobe missing or the file is not a media file")
        print(json.dumps({"file": str(path), "pass": False, "checks": checks}, indent=2))
        return 1
    streams = info.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio = next((s for s in streams if s.get("codec_type") == "audio"), None)

    if video is None:
        check("video_stream", False, None, "one video stream")
    else:
        check("codec", video.get("codec_name") == "h264", video.get("codec_name"), "h264")
        check("resolution", (video.get("width"), video.get("height")) == (1920, 1080),
              "%sx%s" % (video.get("width"), video.get("height")), "1920x1080")
        fps = frame_rate(video)
        check("fps", fps is not None and abs(fps - 30) < 0.01, round(fps, 3) if fps else None, "30")
        check("pix_fmt", video.get("pix_fmt") == "yuv420p", video.get("pix_fmt"), "yuv420p")
        rng = video.get("color_range")
        check("color_range", rng in (None, "tv", "unknown"), rng, "tv (limited range)", level="warn",
              detail="full-range output usually means the render ran without color space bt709")

    if audio is None:
        check("audio_stream", False, None, "one audio stream")
    else:
        check("audio_stream", True, audio.get("codec_name"), "present")
        check("audio_codec", audio.get("codec_name") == "aac", audio.get("codec_name"), "aac", level="warn")
        check("audio_rate", str(audio.get("sample_rate")) == "48000", audio.get("sample_rate"), "48000", level="warn")

    duration = float(info.get("format", {}).get("duration", 0) or 0)
    lo, hi = args.target_s * (1 - DURATION_TOLERANCE), args.target_s * (1 + DURATION_TOLERANCE)
    check("duration", lo <= duration <= hi, round(duration, 2), "%.0f to %.0f s (target %.0f +/- 10 %%)" % (lo, hi, args.target_s))

    if audio is not None:
        if not has_filter("ebur128"):
            check("loudness", True, None, "%.0f LUFS +/- %.1f" % (TARGET_LUFS, args.loudness_tolerance), level="warn",
                  detail="ffmpeg has no ebur128 filter; loudness not measured")
        else:
            lufs = integrated_loudness(path)
            if lufs is None:
                check("loudness", True, None, "%.0f LUFS +/- %.1f" % (TARGET_LUFS, args.loudness_tolerance), level="warn",
                      detail="ebur128 output could not be parsed")
            elif lufs == float("-inf") or lufs < -60:
                check("loudness", False, "silent", "%.0f LUFS +/- %.1f" % (TARGET_LUFS, args.loudness_tolerance),
                      detail="the audio track is silent")
            else:
                ok = abs(lufs - TARGET_LUFS) <= args.loudness_tolerance
                check("loudness", ok, lufs, "%.0f LUFS +/- %.1f" % (TARGET_LUFS, args.loudness_tolerance),
                      detail="" if ok else "run the loudnorm pass (render_longform.py does this for non-draft renders)")

    if args.chapters:
        cpath = Path(args.chapters)
        if not cpath.exists():
            check("chapters_file", False, str(cpath), "file present")
        else:
            chapters = load_chapters(cpath)
            starts = [c["start_s"] for c in chapters]
            check("chapters_count", len(chapters) >= MIN_CHAPTERS, len(chapters), ">= %d" % MIN_CHAPTERS)
            check("chapters_first_at_zero", bool(starts) and abs(starts[0]) < 0.5, starts[0] if starts else None, "00:00")
            check("chapters_ascending", all(b > a for a, b in zip(starts, starts[1:])), starts, "strictly ascending")
            gaps = [b - a for a, b in zip(starts, starts[1:])]
            if duration and starts:
                gaps.append(duration - starts[-1])
            check("chapters_min_length", all(g >= MIN_CHAPTER_S for g in gaps), [round(g, 1) for g in gaps], ">= %d s each" % MIN_CHAPTER_S)
            check("chapters_inside_video", all(s < duration for s in starts) if duration else True, None, "every start before the end")

    failed = [c for c in checks if not c["pass"] and c["level"] == "error"]
    warned = [c for c in checks if not c["pass"] and c["level"] == "warn"]
    report = {
        "file": str(path), "pass": not failed, "duration_s": round(duration, 3), "target_s": args.target_s,
        "failed": [c["name"] for c in failed], "warnings": [c["name"] for c in warned], "checks": checks,
    }
    print(json.dumps(report, indent=2))
    for c in failed:
        log("FAIL %s: %s (expected %s) %s" % (c["name"], c["value"], c["expected"], c["detail"]))
    for c in warned:
        log("warn %s: %s (expected %s) %s" % (c["name"], c["value"], c["expected"], c["detail"]))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
