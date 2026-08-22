#!/usr/bin/env python3
"""assemble.py: stitch rendered scene clips, narration and captions into the final Short.

Port of the v1 editor stage (skills/blai-editor + render/remotion) as one
standalone script. The Remotion project in skills/render-shorts/remotion/
does the compositing; this script generates its props, stages the media,
renders, normalizes loudness and runs the release gates.

Usage:
  assemble.py --slug S --storyboard FILE.json --audio narration.wav --captions captions.json
              --scenes-dir DIR --out DIR [--draft] [--music FILE | --no-music]
              [--music-db -22] [--timeout-s 1800] [--keep-staging] [--skip-gates] [--dry-run]

Inputs:
  --scenes-dir DIR   one clip per storyboard scene at DIR/<scene_id>.mp4 (1080x1920, 30 fps;
                     anything else is conformed with ffmpeg while staging)
  --audio            narration wav (played from frame 0 at full volume)
  --captions         [{word, start, end}] from elevenlabs-narration (seconds; ms auto-detected)
                     or @remotion/captions objects [{text, startMs, endMs}]
  music              --music FILE, else the first file in assets/music/ whose name starts with the
                     storyboard's music_mood, else no music (silence beats a wrong vibe)
  sfx                storyboard scenes[].sfx [{at: start|number-reveal|end, name}] become cues on
                     the composition timeline (max 6, never two within one second)

Outputs:
  DIR/final.mp4 (DIR/final-draft.mp4 with --draft), DIR/<slug>-props.json (the generated Remotion
  props), DIR/qa/safe-zone.png (final only), and one JSON line on stdout:
  {"final": ..., "duration_s": ..., "lint_ok": ..., "safe_zone_ok": ..., "loop_ok": ..., ...}

--draft renders at --scale 0.25 with crf 32: quick to check timing and audio, never publishable,
and lint_video.py always flags its resolution (exit code stays 0 on a draft).
--dry-run writes the props JSON and prints the plan without rendering (no Chrome, no ffmpeg encode).
Exit 0 on success, 1 on failure (missing inputs, render error, or a failed hard gate on a final).
Stdlib only; needs ffmpeg/ffprobe, Node 22 and `npm install` done in remotion/.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from typing import Any, Dict, List, Optional, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, ".."))
REMOTION_DIR = os.path.join(SKILL_ROOT, "remotion")
MUSIC_DIR = os.path.join(SKILL_ROOT, "assets", "music")
FORMATS_JSON = os.path.join(SKILL_ROOT, "..", "script-gates", "formats.json")
sys.path.insert(0, HERE)
from scene_timing import compute_timing, normalize_captions  # noqa: E402

FALLBACK_BANDS = {"classic": (60.0, (28.0, 47.0)), "smooth-explainer": (180.0, (70.0, 155.0))}
SFX_NAMES = {"whoosh", "pop", "tick", "ding", "type"}
SFX_MAX_CUES = 6
SFX_MIN_GAP_MS = 1000
SFX_END_LEAD_MS = 350  # a whoosh is 350 ms; an "end" cue finishes on the cut
DEFAULT_MUSIC_DB = -22.0
MUSIC_EXTS = (".mp3", ".wav", ".m4a", ".aac", ".ogg")
NUMBER_WORD_RE = re.compile(
    r"\d|\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|"
    r"fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|"
    r"seventy|eighty|ninety|hundred|thousand|million|billion|trillion|percent|half|quarter|"
    r"double|triple|twice)\b", re.I)


def log(msg: str) -> None:
    print("assemble: " + msg, file=sys.stderr)
    sys.stderr.flush()


def fail(msg: str) -> int:
    log("ERROR " + msg)
    return 1


def run(cmd: List[str], cwd: Optional[str] = None, timeout: Optional[float] = None,
        capture: bool = True) -> subprocess.CompletedProcess:
    log("$ " + " ".join(cmd))
    if capture:
        return subprocess.run(cmd, cwd=cwd, timeout=timeout, capture_output=True, text=True)
    return subprocess.run(cmd, cwd=cwd, timeout=timeout, stdout=sys.stderr, stderr=subprocess.STDOUT, text=True)


def ffprobe(path: str) -> Dict[str, Any]:
    res = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path],
                         capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError("ffprobe failed for %s: %s" % (path, res.stderr.strip()[:200]))
    info = json.loads(res.stdout)
    v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), None)
    a = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), None)
    fps = 0.0
    if v and v.get("r_frame_rate"):
        num, den = (int(x) for x in v["r_frame_rate"].split("/"))
        fps = num / den if den else 0.0
    return {
        "duration_s": float(info.get("format", {}).get("duration", 0.0)),
        "width": int(v["width"]) if v else 0,
        "height": int(v["height"]) if v else 0,
        "fps": fps,
        "pix_fmt": v.get("pix_fmt") if v else None,
        "codec": v.get("codec_name") if v else None,
        "has_audio": a is not None,
    }


def scene_is_conformant(info: Dict[str, Any]) -> bool:
    return (info["width"], info["height"]) == (1080, 1920) and abs(info["fps"] - 30) <= 0.05 \
        and info["pix_fmt"] == "yuv420p" and info["codec"] == "h264"


def conform_scene(src: str, dst: str) -> None:
    """v1 normalize.sh: 1080x1920@30 H.264 yuv420p, letterboxed in brand navy, silent."""
    res = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", src,
               "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,"
                      "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0B1020,fps=30,format=yuv420p",
               "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-movflags", "+faststart", "-an", dst])
    if res.returncode != 0:
        raise RuntimeError("ffmpeg conform failed for %s: %s" % (src, res.stderr.strip()[:300]))


def load_bands(script_format: str) -> Tuple[float, Tuple[float, float]]:
    try:
        with open(FORMATS_JSON, encoding="utf-8") as fh:
            fmt = json.load(fh)["formats"][script_format]
        return float(fmt["final_max_s"]), (float(fmt["final_warn_s"]["min"]), float(fmt["final_warn_s"]["max"]))
    except (OSError, KeyError, ValueError, TypeError):
        return FALLBACK_BANDS.get(script_format, FALLBACK_BANDS["classic"])


def pick_music(explicit: Optional[str], no_music: bool, mood: Optional[str]) -> Optional[str]:
    if no_music:
        return None
    if explicit:
        if not os.path.isfile(explicit):
            raise FileNotFoundError("music file not found: %s" % explicit)
        return os.path.abspath(explicit)
    if not mood or mood == "none" or not os.path.isdir(MUSIC_DIR):
        return None
    for name in sorted(os.listdir(MUSIC_DIR)):
        if name.lower().startswith(mood.lower()) and name.lower().endswith(MUSIC_EXTS):
            return os.path.join(MUSIC_DIR, name)
    return None


def build_sfx(storyboard: Dict[str, Any], scene_bounds: List[Tuple[int, int]], words: List[Dict[str, Any]],
              warnings: List[str]) -> List[Dict[str, Any]]:
    scenes = storyboard.get("scenes") or []
    try:
        slots = compute_timing(storyboard, words) if words else []
    except ValueError:
        slots = []
    cues: List[Dict[str, Any]] = []
    for i, scene in enumerate(scenes):
        start_ms, end_ms = scene_bounds[i]
        for marker in scene.get("sfx") or []:
            name = str(marker.get("name", ""))
            at = str(marker.get("at", "start"))
            if name not in SFX_NAMES:
                warnings.append("scene %s: unknown sfx %r skipped" % (scene.get("id"), name))
                continue
            if at == "start":
                at_ms = start_ms
            elif at == "end":
                at_ms = max(start_ms, end_ms - SFX_END_LEAD_MS)
            else:  # number-reveal: the first spoken number in this scene's narration window
                at_ms = None
                if i < len(slots):
                    lo, hi = slots[i]["start_ms"], slots[i]["end_ms"]
                    for w in words:
                        if lo <= w["startMs"] < hi and NUMBER_WORD_RE.search(w["text"]):
                            at_ms = w["startMs"]
                            break
                if at_ms is None:
                    at_ms = (start_ms + end_ms) // 2
                    warnings.append("scene %s: no spoken number found, number-reveal cue at scene midpoint"
                                    % scene.get("id"))
            cues.append({"atMs": int(at_ms), "name": name, "_scene": scene.get("id"), "_at": at})
    cues.sort(key=lambda c: c["atMs"])
    kept: List[Dict[str, Any]] = []
    for cue in cues:
        if kept and cue["atMs"] - kept[-1]["atMs"] < SFX_MIN_GAP_MS:
            warnings.append("sfx %s at %d ms dropped: within %d ms of the previous cue"
                            % (cue["name"], cue["atMs"], SFX_MIN_GAP_MS))
            continue
        if len(kept) >= SFX_MAX_CUES:
            warnings.append("sfx %s at %d ms dropped: more than %d cues" % (cue["name"], cue["atMs"], SFX_MAX_CUES))
            continue
        kept.append(cue)
    return [{"atMs": c["atMs"], "name": c["name"]} for c in kept]


def measure_loudness(path: str) -> Optional[Dict[str, str]]:
    res = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af",
                          "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                         capture_output=True, text=True)
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", res.stderr, re.DOTALL)
    return json.loads(m.group(0)) if m else None


def loudnorm(raw: str, final: str, measured: Optional[Dict[str, str]] = None) -> None:
    af = "loudnorm=I=-14:TP=-1.5:LRA=11"
    if measured:
        af += ":measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true" % (
            measured["input_i"], measured["input_tp"], measured["input_lra"], measured["input_thresh"],
            measured.get("target_offset", "0"))
    res = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", raw, "-af", af,
               "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", final])
    if res.returncode != 0:
        raise RuntimeError("loudnorm pass failed: %s" % res.stderr.strip()[:300])


def run_lint(final: str, max_s: float, band: Tuple[float, float]) -> Tuple[bool, Dict[str, Any]]:
    res = run([sys.executable, os.path.join(HERE, "lint_video.py"), final, "--final",
               "--max-s", str(max_s), "--warn-band", "%s:%s" % (band[0], band[1])])
    try:
        detail = json.loads(res.stdout)
    except ValueError:
        detail = {"raw": (res.stdout or res.stderr)[:500]}
    return res.returncode == 0, detail


def run_safe_zone(final: str, qa_dir: str) -> Tuple[bool, Dict[str, Any]]:
    res = run([sys.executable, os.path.join(HERE, "safe_zone_check.py"), final, "--stills", "8", "--debug-dir", qa_dir])
    try:
        detail = json.loads(res.stdout)
        detail.pop("frames", None)
    except ValueError:
        detail = {"raw": (res.stdout or res.stderr)[:500]}
    return res.returncode == 0, detail


def run_loop_check(final: str) -> Tuple[Optional[bool], Optional[float]]:
    script = os.path.join(REMOTION_DIR, "scripts", "loop_check.mjs")
    res = run(["node", script, final], cwd=REMOTION_DIR)
    try:
        data = json.loads(res.stdout.strip().splitlines()[-1])
        return bool(data.get("similar")), float(data.get("ssim"))
    except (ValueError, IndexError, TypeError):
        return None, None


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--storyboard", required=True)
    ap.add_argument("--audio", required=True, help="narration wav")
    ap.add_argument("--captions", required=True, help="captions.json")
    ap.add_argument("--scenes-dir", required=True, help="DIR/<scene_id>.mp4 per storyboard scene")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--draft", action="store_true", help="scale 0.25, crf 32, writes final-draft.mp4")
    ap.add_argument("--music", help="music file (overrides the assets/music mood lookup)")
    ap.add_argument("--no-music", action="store_true")
    ap.add_argument("--music-db", type=float, default=DEFAULT_MUSIC_DB, help="music bed level in dBFS (default -22)")
    ap.add_argument("--timeout-s", type=float, default=1800.0, help="render timeout (default 30 min)")
    ap.add_argument("--keep-staging", action="store_true", help="keep remotion/public/<slug>/ after the render")
    ap.add_argument("--skip-gates", action="store_true", help="render only; no lint, safe-zone, loop or QA still")
    ap.add_argument("--dry-run", action="store_true", help="write props and print the plan; no render")
    args = ap.parse_args(argv)

    warnings: List[str] = []
    out_dir = os.path.abspath(args.out)
    os.makedirs(out_dir, exist_ok=True)
    try:
        with open(args.storyboard, encoding="utf-8") as fh:
            storyboard = json.load(fh)
        with open(args.captions, encoding="utf-8") as fh:
            words = normalize_captions(json.load(fh))
    except (OSError, ValueError) as exc:
        return fail("cannot read inputs: %s" % exc)
    scenes = storyboard.get("scenes") or []
    if not scenes:
        return fail("storyboard has no scenes")
    if not words:
        warnings.append("captions are empty: the Short will render without captions")
    if not os.path.isfile(args.audio):
        return fail("audio not found: %s" % args.audio)

    # Scene clips, in storyboard order.
    scene_files = []
    missing = []
    for scene in scenes:
        sid = scene.get("id")
        path = os.path.join(os.path.abspath(args.scenes_dir), "%s.mp4" % sid)
        if not os.path.isfile(path):
            missing.append(path)
        scene_files.append((sid, path))
    if missing and not args.dry_run:
        return fail("missing scene clips: %s" % ", ".join(missing))
    if missing:
        warnings.append("dry run with missing scene clips: %s" % ", ".join(os.path.basename(m) for m in missing))

    infos: Dict[str, Dict[str, Any]] = {}
    try:
        for sid, path in scene_files:
            if os.path.isfile(path):
                infos[sid] = ffprobe(path)
        audio_info = ffprobe(args.audio)
    except RuntimeError as exc:
        return fail(str(exc))
    scene_bounds: List[Tuple[int, int]] = []
    cursor = 0
    for i, (sid, _) in enumerate(scene_files):
        dur_ms = int(round(infos[sid]["duration_s"] * 1000)) if sid in infos else int(
            round(float(scenes[i].get("est_duration_s", 5)) * 1000))
        scene_bounds.append((cursor, cursor + dur_ms))
        cursor += dur_ms
    video_total_s = cursor / 1000.0
    if abs(video_total_s - audio_info["duration_s"]) > 0.5:
        warnings.append("video total %.2fs vs narration %.2fs (segments win; check scene durations)"
                        % (video_total_s, audio_info["duration_s"]))

    try:
        music = pick_music(args.music, args.no_music, storyboard.get("music_mood"))
    except FileNotFoundError as exc:
        return fail(str(exc))
    sfx = build_sfx(storyboard, scene_bounds, words, warnings)

    staging_rel = args.slug
    props: Dict[str, Any] = {
        "segments": [{"src": "%s/%s.mp4" % (staging_rel, sid)} for sid, _ in scene_files],
        "voiceoverSrc": "%s/narration.wav" % staging_rel,
        "captions": words,
        "musicVolumeDb": args.music_db,
        "showSafeZones": False,
    }
    if music:
        props["musicSrc"] = "%s/music%s" % (staging_rel, os.path.splitext(music)[1].lower())
    if sfx:
        props["sfx"] = sfx
    props_path = os.path.join(out_dir, "%s-props.json" % args.slug)
    with open(props_path, "w", encoding="utf-8") as fh:
        json.dump(props, fh, indent=2)
    log("wrote %s (%d segments, %d caption words, %d sfx cues, music %s)"
        % (props_path, len(scene_files), len(words), len(sfx), os.path.basename(music) if music else "none"))

    script_format = storyboard.get("script_format") or "classic"
    max_s, band = load_bands(script_format)
    final_name = "final-draft.mp4" if args.draft else "final.mp4"
    final_path = os.path.join(out_dir, final_name)
    raw_path = os.path.join(out_dir, "%s-raw.mp4" % args.slug)
    render_cmd = ["npx", "remotion", "render", "Assembly", raw_path, "--props=" + props_path, "--color-space=bt709"]
    if args.draft:
        render_cmd += ["--scale=0.25", "--crf=32"]

    summary: Dict[str, Any] = {
        "final": None, "duration_s": None, "lint_ok": None, "safe_zone_ok": None, "loop_ok": None,
        "loop_ssim": None, "props": props_path, "draft": bool(args.draft), "script_format": script_format,
        "video_total_s": round(video_total_s, 2), "narration_s": round(audio_info["duration_s"], 2),
        "music": os.path.basename(music) if music else None, "sfx_cues": sfx, "caption_words": len(words),
        "warnings": warnings,
    }
    if args.dry_run:
        summary["plan"] = " ".join(render_cmd)
        print(json.dumps(summary))
        return 0

    # Stage media under remotion/public/<slug>/ (headless Chrome only reads served files).
    staging = os.path.join(REMOTION_DIR, "public", staging_rel)
    shutil.rmtree(staging, ignore_errors=True)
    os.makedirs(staging)
    try:
        for sid, path in scene_files:
            dst = os.path.join(staging, "%s.mp4" % sid)
            if scene_is_conformant(infos[sid]):
                shutil.copy2(path, dst)
            else:
                log("scene %s is %dx%d @ %.2f fps %s; conforming to 1080x1920@30 yuv420p"
                    % (sid, infos[sid]["width"], infos[sid]["height"], infos[sid]["fps"], infos[sid]["pix_fmt"]))
                conform_scene(path, dst)
                warnings.append("scene %s was re-encoded to the canvas spec" % sid)
        shutil.copy2(args.audio, os.path.join(staging, "narration.wav"))
        if music:
            shutil.copy2(music, os.path.join(staging, "music" + os.path.splitext(music)[1].lower()))
    except (OSError, RuntimeError) as exc:
        return fail("staging failed: %s" % exc)

    # Render (bt709 is required: the default output is full-range yuvj420p and fails lint).
    try:
        res = run(render_cmd, cwd=REMOTION_DIR, timeout=args.timeout_s, capture=False)
    except subprocess.TimeoutExpired:
        return fail("remotion render timed out after %.0fs" % args.timeout_s)
    if res.returncode != 0 or not os.path.isfile(raw_path):
        return fail("remotion render failed (exit %s)" % res.returncode)

    try:
        loudnorm(raw_path, final_path)
    except RuntimeError as exc:
        return fail(str(exc))
    try:
        final_info = ffprobe(final_path)
    except RuntimeError as exc:
        return fail(str(exc))
    summary["final"] = final_path
    summary["duration_s"] = round(final_info["duration_s"], 2)

    gates_ok = True
    if not args.skip_gates:
        lint_ok, lint_detail = run_lint(final_path, max_s, band)
        if not lint_ok and not args.draft and any("loudness" in v for v in lint_detail.get("violations", [])):
            log("loudness out of band after the single pass; one two-pass correction round")
            measured = measure_loudness(raw_path)
            if measured:
                try:
                    loudnorm(raw_path, final_path, measured)
                    lint_ok, lint_detail = run_lint(final_path, max_s, band)
                except RuntimeError as exc:
                    warnings.append("two-pass loudnorm failed: %s" % exc)
        summary["lint_ok"] = lint_ok
        summary["lint"] = lint_detail
        if not args.draft:
            qa_dir = os.path.join(out_dir, "qa")
            os.makedirs(qa_dir, exist_ok=True)
            sz_ok, sz_detail = run_safe_zone(final_path, qa_dir)
            summary["safe_zone_ok"] = sz_ok
            summary["safe_zone"] = sz_detail
            loop_ok, ssim = run_loop_check(final_path)
            summary["loop_ok"] = loop_ok
            summary["loop_ssim"] = ssim
            if loop_ok is False:
                warnings.append("loop check failed (ssim %s): first and last frame do not rhyme; flag it, do not fake a fix" % ssim)
            sz_props = dict(props)
            sz_props["showSafeZones"] = True
            sz_props_path = os.path.join(out_dir, "%s-props-safezones.json" % args.slug)
            with open(sz_props_path, "w", encoding="utf-8") as fh:
                json.dump(sz_props, fh, indent=2)
            mid_frame = max(1, int(final_info["duration_s"] * 30 / 2))
            still = run(["npx", "remotion", "still", "Assembly", os.path.join(qa_dir, "safe-zone.png"),
                         "--props=" + sz_props_path, "--frame=%d" % mid_frame], cwd=REMOTION_DIR,
                        timeout=min(args.timeout_s, 600))
            if still.returncode != 0:
                warnings.append("safe-zone still failed: %s" % (still.stderr or still.stdout)[-300:])
            else:
                summary["safe_zone_still"] = os.path.join(qa_dir, "safe-zone.png")
            gates_ok = bool(lint_ok and sz_ok)
    if os.path.isfile(raw_path):
        os.remove(raw_path)
    if not args.keep_staging:
        shutil.rmtree(staging, ignore_errors=True)

    print(json.dumps(summary))
    if not args.draft and not gates_ok:
        return fail("release gates failed (see lint/safe_zone in the summary)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
