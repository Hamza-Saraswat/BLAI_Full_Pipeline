#!/usr/bin/env python3
"""Render a BLAI long-form episode (1920x1080, 30 fps) from a spec with the Remotion
project in ../remotion, then render the three thumbnails and lint the result.

Usage:
  render_longform.py --spec FILE.json --audio narration.wav --captions captions.json
                     [--captures DIR] --out DIR [--draft] [--dry-run]

Writes into DIR:
  final.mp4            the episode (draft: 640x360, first 900 frames, crf 35)
  thumbnails/1.png     three thumbnail variants (plus N.jpg when a png is over 2 MB)
  captions.srt         copied from next to captions.json, else generated from the words
  chapters.json/.txt   chapter start times from the scene layout (for the description)
  layout.json          per-scene timings (src/timing.mjs), props-episode.json, props-thumb-N.json
  render.json          timings, output probe, warnings, lint result

Exit 0 on success, 1 on a validation error, a failed render or a failed lint.
Logs go to stderr. --dry-run validates, writes props and layout, prints the commands
and renders nothing.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
REMOTION_DIR = SKILL / "remotion"
SCHEMA_PATH = SKILL.parent.parent / "shared" / "schemas" / "longform-spec.schema.json"
ENTRY = "src/index.ts"

SCENE_TYPES = [
    "title-card", "chapter-card", "kinetic-text", "code-typing", "terminal-replay", "diagram",
    "comparison-table", "chart", "stat-callout", "quote", "mascot-talk", "b-roll", "end-card",
]
DATA_REQUIRED = {
    "code-typing": ["code"], "diagram": ["nodes"], "comparison-table": ["columns", "rows"],
    "chart": ["series"], "stat-callout": ["value"], "quote": ["text"],
}
FPS = 30
DRAFT_FRAMES = 900
DRAFT_SCALE = "0.33333333"
DRAFT_CRF = "35"
THUMB_MAX_BYTES = 2 * 1024 * 1024
LOUDNORM = "I=-14:TP=-1.5:LRA=11"


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def load_json(path: Path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def dump_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


# ---------------------------------------------------------------- validation

def validate_spec(spec, captures: dict) -> tuple[list[str], list[str]]:
    """Return (errors, warnings). Uses jsonschema when importable, always runs the
    minimal checks (required keys, scene types, ids, chapters, per-type data)."""
    errors: list[str] = []
    warnings: list[str] = []
    try:
        import jsonschema  # type: ignore
        if SCHEMA_PATH.exists():
            schema = load_json(SCHEMA_PATH)
            cls = jsonschema.validators.validator_for(schema)
            for e in sorted(cls(schema).iter_errors(spec), key=lambda e: list(e.path)):
                errors.append("schema " + "/".join(str(x) for x in e.path) + ": " + e.message)
        else:
            warnings.append("schema file not found at %s; minimal checks only" % SCHEMA_PATH)
    except ImportError:
        warnings.append("jsonschema not installed (pip install jsonschema); minimal checks only")
    if not isinstance(spec, dict):
        return ["spec is not a JSON object"], warnings
    for key in ("slug", "title", "target_duration_s", "chapters", "scenes", "thumbnail_concepts"):
        if key not in spec:
            errors.append("missing required key: %s" % key)
    scenes = spec.get("scenes") or []
    ids = [s.get("id") for s in scenes if isinstance(s, dict)]
    if len(scenes) < 8:
        errors.append("scenes: need at least 8, found %d" % len(scenes))
    if len(ids) != len(set(ids)):
        errors.append("scenes: duplicate ids")
    target = spec.get("target_duration_s")
    if not isinstance(target, int) or not 480 <= target <= 1200:
        errors.append("target_duration_s must be an integer between 480 and 1200")
    for i, s in enumerate(scenes):
        where = "scenes[%d]" % i
        if not isinstance(s, dict):
            errors.append(where + ": not an object")
            continue
        for key in ("id", "type", "narration", "est_duration_s", "visual_intent"):
            if key not in s:
                errors.append("%s: missing %s" % (where, key))
        sid = str(s.get("id", ""))
        if not re.match(r"^s\d{2,3}$", sid):
            errors.append("%s: id %r must look like s01" % (where, sid))
        stype = s.get("type")
        if stype not in SCENE_TYPES:
            errors.append("%s (%s): unknown type %r" % (where, sid, stype))
            continue
        if not isinstance(s.get("est_duration_s"), (int, float)) or s.get("est_duration_s", 0) < 2:
            errors.append("%s (%s): est_duration_s must be a number >= 2" % (where, sid))
        if not str(s.get("narration", "")).strip():
            errors.append("%s (%s): narration is empty" % (where, sid))
        data = s.get("data") or {}
        for key in DATA_REQUIRED.get(stype, []):
            if key not in data:
                errors.append("%s (%s): %s needs data.%s" % (where, sid, stype, key))
        if stype == "terminal-replay":
            ref = s.get("capture_ref") or data.get("capture_ref")
            if not ref:
                errors.append("%s (%s): terminal-replay needs capture_ref" % (where, sid))
            elif captures is not None and ref not in captures:
                warnings.append("%s (%s): capture %r not found in --captures; the scene will say so on screen" % (where, sid, ref))
        if stype == "b-roll" and not data.get("src"):
            warnings.append("%s (%s): b-roll has no data.src; a placeholder card renders" % (where, sid))
        for key in ("props", "frame", "frames", "x", "y", "px"):
            if key in data:
                warnings.append("%s (%s): data.%s looks like a render detail; the spec says what, not how" % (where, sid, key))
    chapters = spec.get("chapters") or []
    if len(chapters) < 3:
        errors.append("chapters: need at least 3, found %d" % len(chapters))
    for i, c in enumerate(chapters):
        if not isinstance(c, dict) or "label" not in c or "starts_at_scene" not in c:
            errors.append("chapters[%d]: needs label and starts_at_scene" % i)
        elif c["starts_at_scene"] not in ids:
            errors.append("chapters[%d]: starts_at_scene %r is not a scene id" % (i, c["starts_at_scene"]))
    if chapters and ids and isinstance(chapters[0], dict) and chapters[0].get("starts_at_scene") != ids[0]:
        warnings.append("the first chapter does not start at the first scene; YouTube wants a chapter at 00:00")
    concepts = spec.get("thumbnail_concepts") or []
    if len(concepts) != 3:
        errors.append("thumbnail_concepts: need exactly 3, found %d" % len(concepts))
    for i, c in enumerate(concepts):
        if not isinstance(c, dict) or "words" not in c or "focus" not in c:
            errors.append("thumbnail_concepts[%d]: needs words and focus" % i)
        elif len(str(c["words"]).split()) > 4:
            warnings.append("thumbnail_concepts[%d]: more than 4 words; only the first 4 render" % i)
    seen = set()
    deduped = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            deduped.append(e)
    return deduped, warnings


# ------------------------------------------------------------------- inputs

def load_captions(path: Path) -> tuple[list[dict], list[str]]:
    raw = load_json(path)
    warnings: list[str] = []
    if isinstance(raw, dict):
        raw = raw.get("words") or raw.get("captions") or []
    words = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        word = item.get("word", item.get("text"))
        start = item.get("start", item.get("start_s", item.get("startMs")))
        end = item.get("end", item.get("end_s", item.get("endMs")))
        if word is None or start is None or end is None:
            continue
        try:
            words.append({"word": str(word).strip(), "start": float(start), "end": float(end)})
        except (TypeError, ValueError):
            continue
    words = [w for w in words if w["word"]]
    if words and max(w["end"] for w in words) > 36000:
        warnings.append("caption times look like milliseconds; converted to seconds")
        for w in words:
            w["start"] /= 1000.0
            w["end"] /= 1000.0
    words.sort(key=lambda w: w["start"])
    return words, warnings


def audio_duration_s(path: Path) -> float | None:
    if path.suffix.lower() == ".wav":
        try:
            with wave.open(str(path), "rb") as wf:
                return wf.getnframes() / float(wf.getframerate())
        except wave.Error:
            pass
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        return float(out)
    except (OSError, subprocess.CalledProcessError, ValueError):
        return None


def load_captures(captures_dir: Path | None) -> tuple[dict, list[str]]:
    """capture.json ([{id, command, exit, duration_s, stdout_tail, metrics, cast}]) plus the
    text of each <id>.cast, keyed by id for the TerminalReplay scene."""
    warnings: list[str] = []
    if captures_dir is None:
        return {}, warnings
    manifest = captures_dir / "capture.json"
    if not manifest.exists():
        warnings.append("no capture.json in %s" % captures_dir)
        return {}, warnings
    entries = load_json(manifest)
    if isinstance(entries, dict):
        entries = entries.get("captures") or entries.get("commands") or []
    out = {}
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("id"):
            continue
        cid = str(entry["id"])
        rec = {
            "command": entry.get("command"),
            "exit": entry.get("exit"),
            "duration_s": entry.get("duration_s"),
            "stdout": entry.get("stdout_tail") or entry.get("stdout") or "",
            "metrics": entry.get("metrics") or {},
        }
        cast_name = entry.get("cast") or (cid + ".cast")
        cast_path = captures_dir / str(cast_name)
        if cast_path.exists():
            try:
                rec["cast"] = cast_path.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                warnings.append("could not read %s: %s" % (cast_path, exc))
        out[cid] = rec
    return out, warnings


def resolve_broll(src: str, spec_dir: Path, assets_dir: Path | None) -> Path | None:
    rel = src.replace("\\", "/").lstrip("/")
    candidates = [spec_dir / rel, Path.cwd() / rel]
    if assets_dir is not None:
        candidates.insert(0, assets_dir / rel)
    for c in candidates:
        if c.is_file():
            return c
    return None


def stage_media(spec: dict, audio: Path, spec_dir: Path, assets_dir: Path | None, dry_run: bool) -> tuple[str, list[str]]:
    """Copy the narration and every b-roll clip into remotion/public/<slug>/ and return
    (audio public path, warnings)."""
    warnings: list[str] = []
    slug = spec["slug"]
    pub = REMOTION_DIR / "public" / slug
    audio_name = "narration" + (audio.suffix.lower() or ".wav")
    if not dry_run:
        if pub.exists():
            shutil.rmtree(pub)
        pub.mkdir(parents=True)
        shutil.copy2(audio, pub / audio_name)
    for scene in spec.get("scenes", []):
        if scene.get("type") != "b-roll":
            continue
        src = (scene.get("data") or {}).get("src")
        if not src:
            continue
        found = resolve_broll(str(src), spec_dir, assets_dir)
        if found is None:
            warnings.append("b-roll %s: %s not found (looked next to the spec%s); placeholder card will render"
                            % (scene.get("id"), src, " and in --assets" if assets_dir else ""))
            continue
        if not dry_run:
            dest = pub / str(src).replace("\\", "/").lstrip("/")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(found, dest)
    return "%s/%s" % (slug, audio_name), warnings


# ------------------------------------------------------------------ helpers

def run(cmd: list[str], cwd: Path | None = None, capture: bool = False, env: dict | None = None) -> subprocess.CompletedProcess:
    log("$ " + " ".join(str(c) for c in cmd))
    return subprocess.run([str(c) for c in cmd], cwd=str(cwd) if cwd else None, text=True,
                          capture_output=capture, env=env)


def compute_layout(props_path: Path, audio_s: float | None) -> dict | None:
    cmd = ["node", str(REMOTION_DIR / "scripts" / "layout.mjs"), str(props_path)]
    if audio_s is not None:
        cmd += ["--audio-duration", "%.3f" % audio_s]
    proc = run(cmd, cwd=REMOTION_DIR, capture=True)
    if proc.returncode != 0:
        log(proc.stderr)
        return None
    return json.loads(proc.stdout)


def mmss(seconds: float) -> str:
    s = int(round(seconds))
    if s >= 3600:
        return "%d:%02d:%02d" % (s // 3600, (s % 3600) // 60, s % 60)
    return "%02d:%02d" % (s // 60, s % 60)


def srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    return "%02d:%02d:%02d,%03d" % (ms // 3600000, (ms % 3600000) // 60000, (ms % 60000) // 1000, ms % 1000)


def write_srt(words: list[dict], path: Path) -> None:
    cues = []
    current = None
    for w in words:
        if current and (len(current["words"]) >= 7 or w["end"] - current["start"] > 2.5 or w["start"] - current["end"] > 0.7):
            cues.append(current)
            current = None
        if current is None:
            current = {"words": [w["word"]], "start": w["start"], "end": w["end"]}
        else:
            current["words"].append(w["word"])
            current["end"] = max(current["end"], w["end"])
    if current:
        cues.append(current)
    with open(path, "w", encoding="utf-8") as fh:
        for i, c in enumerate(cues, 1):
            fh.write("%d\n%s --> %s\n%s\n\n" % (i, srt_time(c["start"]), srt_time(c["end"]), " ".join(c["words"])))


def ffprobe_video(path: Path) -> dict:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(path)],
            capture_output=True, text=True, check=True,
        ).stdout
        info = json.loads(out)
    except (OSError, subprocess.CalledProcessError, ValueError):
        return {}
    video = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
    return {
        "duration_s": float(info.get("format", {}).get("duration", 0) or 0),
        "width": video.get("width"),
        "height": video.get("height"),
        "codec": video.get("codec_name"),
        "pix_fmt": video.get("pix_fmt"),
        "fps": video.get("r_frame_rate"),
        "size_bytes": path.stat().st_size if path.exists() else None,
    }


def loudnorm_measure(path: Path) -> dict | None:
    proc = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "loudnorm=%s:print_format=json" % LOUDNORM,
                "-f", "null", "-"], capture=True)
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", proc.stderr, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except ValueError:
        return None


def normalize_loudness(raw: Path, final: Path) -> tuple[bool, str]:
    measured = loudnorm_measure(raw)
    if measured is None:
        return False, "loudnorm measurement failed; ffmpeg may lack the loudnorm filter"
    try:
        input_i = float(measured.get("input_i", "-inf"))
    except ValueError:
        input_i = float("-inf")
    if input_i < -60:
        shutil.copy2(raw, final)
        return True, "audio is silent (%.1f LUFS); copied without normalization" % input_i
    af = "loudnorm=%s:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true" % (
        LOUDNORM, measured["input_i"], measured["input_tp"], measured["input_lra"], measured["input_thresh"],
        measured.get("target_offset", "0"))
    proc = run(["ffmpeg", "-y", "-hide_banner", "-nostats", "-loglevel", "error", "-i", str(raw), "-af", af,
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(final)], capture=True)
    if proc.returncode != 0:
        return False, "loudnorm pass failed: " + proc.stderr.strip()[-400:]
    return True, "normalized from %.1f LUFS to -14 LUFS (two-pass loudnorm)" % input_i


# --------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spec", required=True, help="long-form spec JSON (shared/schemas/longform-spec.schema.json)")
    ap.add_argument("--audio", required=True, help="narration audio (wav preferred)")
    ap.add_argument("--captions", required=True, help="captions.json: [{word, start, end}] in seconds")
    ap.add_argument("--captures", help="directory with capture.json and <id>.cast files from skills/dgx-capture")
    ap.add_argument("--assets", help="extra directory to look up b-roll clips (default: next to the spec)")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--draft", action="store_true", help="640x360, crf 35, first %d frames only; lint skipped" % DRAFT_FRAMES)
    ap.add_argument("--concurrency", help="passed to remotion render (default: remotion.config.ts)")
    ap.add_argument("--safe-area", action="store_true", help="draw the 5 %% safe-area rectangle (debug)")
    ap.add_argument("--offline-fonts", action="store_true", help="do not fetch Inter; use the fallback fonts")
    ap.add_argument("--no-lint", action="store_true", help="skip lint_longform.py")
    ap.add_argument("--clean-public", action="store_true", help="delete remotion/public/<slug>/ after a successful render")
    ap.add_argument("--dry-run", action="store_true", help="validate, write props and layout, print commands, render nothing")
    args = ap.parse_args()

    t0 = time.time()
    timings: dict = {}
    warnings: list[str] = []
    out_dir = Path(args.out).resolve()
    spec_path = Path(args.spec).resolve()
    audio_path = Path(args.audio).resolve()
    captions_path = Path(args.captions).resolve()
    captures_dir = Path(args.captures).resolve() if args.captures else None
    assets_dir = Path(args.assets).resolve() if args.assets else None

    for p, what in ((spec_path, "spec"), (audio_path, "audio"), (captions_path, "captions")):
        if not p.exists():
            log("error: %s not found: %s" % (what, p))
            return 1
    if not (REMOTION_DIR / "node_modules").exists() and not args.dry_run:
        log("error: %s has no node_modules; run `npm install` there first (see setup.md)" % REMOTION_DIR)
        return 1

    spec = load_json(spec_path)
    captures, w = load_captures(captures_dir)
    warnings += w
    errors, w = validate_spec(spec, captures if captures_dir else None)
    warnings += w
    for msg in warnings:
        log("warning: " + msg)
    if errors:
        for e in errors:
            log("error: " + e)
        log("spec failed validation (%d errors)" % len(errors))
        return 1
    timings["validate_s"] = round(time.time() - t0, 3)

    captions, w = load_captions(captions_path)
    warnings += w
    if not captions:
        warnings.append("captions.json has no words; scenes keep their est_duration_s")
    audio_s = audio_duration_s(audio_path)
    if audio_s is None:
        warnings.append("could not read the audio duration; the last scene will not be extended to the audio end")

    t1 = time.time()
    audio_public, w = stage_media(spec, audio_path, spec_path.parent, assets_dir, args.dry_run)
    warnings += w
    timings["stage_media_s"] = round(time.time() - t1, 3)

    out_dir.mkdir(parents=True, exist_ok=True)
    slug = spec["slug"]
    props = {
        "spec": spec,
        "captions": captions,
        "audioSrc": audio_public,
        "captures": captures,
        "assetsBase": slug + "/",
        "showSafeArea": bool(args.safe_area),
    }
    props_path = out_dir / "props-episode.json"
    dump_json(props_path, props)

    layout = compute_layout(props_path, audio_s)
    if layout is None:
        log("error: scene layout failed (node scripts/layout.mjs)")
        return 1
    dump_json(out_dir / "layout.json", layout)
    chapters = [{"number": c["number"], "label": c["label"], "scene": c["sceneId"], "start_s": round(c["startS"], 3),
                 "timestamp": mmss(c["startS"])} for c in layout.get("chapters", [])]
    dump_json(out_dir / "chapters.json", chapters)
    with open(out_dir / "chapters.txt", "w", encoding="utf-8") as fh:
        for c in chapters:
            fh.write("%s %s\n" % (c["timestamp"], c["label"]))
    total_frames = int(layout["totalFrames"])
    matched = sum(1 for s in layout["scenes"] if s.get("matched"))
    log("layout: %d scenes, %.1f s, %d matched to captions, %d chapters" % (len(layout["scenes"]), layout["totalS"], matched, len(chapters)))
    if captions and matched < len(layout["scenes"]) // 2:
        warnings.append("only %d of %d scenes matched the captions; check that narration text and captions.json come from the same script" % (matched, len(layout["scenes"])))

    env = dict(os.environ)
    if args.offline_fonts:
        env["REMOTION_OFFLINE_FONTS"] = "1"

    final = out_dir / "final.mp4"
    raw = out_dir / "final-raw.mp4"
    render_cmd = ["npx", "remotion", "render", ENTRY, "Episode", str(raw if not args.draft else final), "--props=%s" % props_path]
    if args.concurrency:
        render_cmd.append("--concurrency=%s" % args.concurrency)
    if args.draft:
        last = max(0, min(total_frames - 1, DRAFT_FRAMES - 1))
        render_cmd += ["--scale=%s" % DRAFT_SCALE, "--crf=%s" % DRAFT_CRF, "--frames=0-%d" % last]
    thumb_cmds = []
    thumbs_dir = out_dir / "thumbnails"
    for n, concept in enumerate(spec["thumbnail_concepts"][:3], 1):
        tp = out_dir / ("props-thumb-%d.json" % n)
        dump_json(tp, {"concept": concept, "title": spec["title"], "variant": n, "series": spec.get("series", "")})
        thumb_cmds.append(["npx", "remotion", "still", ENTRY, "Thumbnail", str(thumbs_dir / ("%d.png" % n)), "--props=%s" % tp])

    report = {
        "slug": slug, "draft": bool(args.draft), "dry_run": bool(args.dry_run), "out": str(out_dir),
        "inputs": {"spec": str(spec_path), "audio": str(audio_path), "captions": str(captions_path),
                   "captures": str(captures_dir) if captures_dir else None, "audio_duration_s": audio_s,
                   "caption_words": len(captions), "captures_found": sorted(captures.keys())},
        "layout": {"total_s": layout["totalS"], "total_frames": total_frames, "scenes": len(layout["scenes"]),
                   "matched_scenes": matched, "chapters": chapters,
                   "scenes_detail": [{"id": s["id"], "type": s["type"], "start_s": round(s["startS"], 3), "end_s": round(s["endS"], 3),
                                      "matched": s["matched"]} for s in layout["scenes"]]},
        "commands": [" ".join(render_cmd)] + [" ".join(c) for c in thumb_cmds],
        "timings": timings, "warnings": warnings, "output": None, "thumbnails": [], "lint": None,
    }

    if args.dry_run:
        report["lint"] = {"skipped": True, "reason": "dry run"}
        timings["total_s"] = round(time.time() - t0, 3)
        dump_json(out_dir / "render.json", report)
        print(json.dumps({"dry_run": True, "out": str(out_dir), "total_s": layout["totalS"], "commands": report["commands"]}, indent=2))
        return 0

    t2 = time.time()
    proc = run(render_cmd, cwd=REMOTION_DIR, env=env)
    timings["render_s"] = round(time.time() - t2, 1)
    if proc.returncode != 0:
        log("error: remotion render failed (exit %d)" % proc.returncode)
        report["timings"] = timings
        dump_json(out_dir / "render.json", report)
        return 1

    if not args.draft:
        t3 = time.time()
        ok, msg = normalize_loudness(raw, final)
        timings["loudnorm_s"] = round(time.time() - t3, 1)
        log("loudness: " + msg)
        if not ok:
            warnings.append(msg)
            shutil.copy2(raw, final)
        else:
            report["loudness"] = msg
        raw.unlink(missing_ok=True)
    report["output"] = ffprobe_video(final)

    t4 = time.time()
    thumbs_dir.mkdir(parents=True, exist_ok=True)
    for cmd in thumb_cmds:
        proc = run(cmd, cwd=REMOTION_DIR, env=env)
        if proc.returncode != 0:
            log("error: thumbnail render failed (exit %d)" % proc.returncode)
            dump_json(out_dir / "render.json", report)
            return 1
        png = Path(cmd[5])
        entry = {"png": str(png), "bytes": png.stat().st_size}
        if entry["bytes"] > THUMB_MAX_BYTES:
            jpg = png.with_suffix(".jpg")
            conv = run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(png), "-q:v", "3", str(jpg)], capture=True)
            if conv.returncode == 0 and jpg.exists():
                entry["jpg"] = str(jpg)
                entry["jpg_bytes"] = jpg.stat().st_size
                if entry["jpg_bytes"] > THUMB_MAX_BYTES:
                    warnings.append("%s is still over 2 MB" % jpg.name)
            else:
                warnings.append("%s is over 2 MB and the jpg conversion failed" % png.name)
        report["thumbnails"].append(entry)
    timings["thumbnails_s"] = round(time.time() - t4, 1)

    sibling = captions_path.with_name("captions.srt")
    if sibling.exists():
        shutil.copy2(sibling, out_dir / "captions.srt")
        report["captions_srt"] = "copied from %s" % sibling
    else:
        write_srt(captions, out_dir / "captions.srt")
        report["captions_srt"] = "generated from captions.json"

    lint_ok = True
    if args.draft:
        report["lint"] = {"skipped": True, "reason": "draft render (640x360, first %d frames)" % DRAFT_FRAMES}
    elif args.no_lint:
        report["lint"] = {"skipped": True, "reason": "--no-lint"}
    else:
        t5 = time.time()
        proc = run([sys.executable, str(HERE / "lint_longform.py"), str(final), "--target-s", str(spec["target_duration_s"]),
                    "--chapters", str(out_dir / "chapters.json")], capture=True)
        timings["lint_s"] = round(time.time() - t5, 1)
        try:
            report["lint"] = json.loads(proc.stdout)
        except ValueError:
            report["lint"] = {"pass": False, "error": (proc.stdout + proc.stderr).strip()[-800:]}
        lint_ok = proc.returncode == 0
        if proc.stderr.strip():
            log(proc.stderr.strip())

    if args.clean_public:
        shutil.rmtree(REMOTION_DIR / "public" / slug, ignore_errors=True)

    timings["total_s"] = round(time.time() - t0, 1)
    report["timings"] = timings
    report["warnings"] = warnings
    dump_json(out_dir / "render.json", report)
    print(json.dumps({"out": str(out_dir), "final": str(final), "thumbnails": [t["png"] for t in report["thumbnails"]],
                      "output": report["output"], "lint_pass": lint_ok if not args.draft else None,
                      "warnings": len(warnings), "total_s": timings["total_s"]}, indent=2))
    if not lint_ok:
        log("lint failed; see %s" % (out_dir / "render.json"))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
