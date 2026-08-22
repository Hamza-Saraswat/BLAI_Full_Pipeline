#!/usr/bin/env python3
"""Generate narration with ElevenLabs and keep character-level timestamps.

Usage:
  generate_audio.py --text FILE.txt --out DIR [--voice-id ID] [--model eleven_multilingual_v2]
                    [--format long|short] [--max-chars 4500] [--fade-ms 0] [--dry-run]
  generate_audio.py --storyboard FILE.json --out DIR ...   (reads the storyboard's narration_full)

Outputs in DIR:
  narration.wav    44.1 kHz mono PCM, all chunks concatenated
  alignment.json   character timestamps for the whole narration (chunk times offset by the
                   accumulated duration) plus the chunk table
  chunks/NN.mp3    raw ElevenLabs output per chunk (mp3_44100_192) + chunks/NN.json (its alignment)
  voice.json       {duration_s, chars, chunks, credits_estimate, model, voice_id_hint, ...}

Steps: apply pronunciation_dictionary.json aliases -> chunk at paragraph boundaries (<= --max-chars,
one chunk for --format short) -> POST /v1/text-to-speech/{voice}/with-timestamps per chunk with
previous_text/next_text and a pinned seed -> decode, measure, concatenate with ffmpeg -> write files.

Env (build/.env or the environment): ELEVENLABS_API_KEY, ELEVEN_VOICE_ID, ELEVEN_MODEL_ID, ELEVEN_SEED.
--only-chunks 2,5 re-synthesizes just those chunks (pair with --seed for a fresh take) and reuses the
stored mp3 + alignment of every other chunk, then rebuilds narration.wav and alignment.json.
--dry-run makes no network call: it writes a 3 s silent narration.wav and a synthetic alignment so
qa_transcribe.py and captions.py can run. Exit 0 on success, 1 on failure. Logs go to stderr.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import wave

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent
DICT_PATH = SKILL_DIR / "pronunciation_dictionary.json"

API_BASE = "https://api.elevenlabs.io/v1"
OUTPUT_FORMAT = "mp3_44100_192"  # needs Creator+; pcm_44100 needs Pro+
SAMPLE_RATE = 44100
DEFAULT_MODEL = "eleven_multilingual_v2"
DEFAULT_SEED = 4242
DEFAULT_MAX_CHARS = 4500
DRY_RUN_SECONDS = 3.0

# Per-request character limits per model (research section 3.1); unknown models get the v3 limit.
MODEL_LIMITS = {
    "eleven_v3": 5000,
    "eleven_multilingual_v2": 10000,
    "eleven_flash_v2_5": 40000,
    "eleven_turbo_v2_5": 40000,
    "eleven_flash_v2": 30000,
    "eleven_turbo_v2": 30000,
}
CREDITS_PER_CHAR = {"eleven_flash_v2_5": 0.5, "eleven_turbo_v2_5": 0.5, "eleven_flash_v2": 0.5, "eleven_turbo_v2": 0.5}
USD_PER_1K_CHARS = {"eleven_flash_v2_5": 0.05, "eleven_turbo_v2_5": 0.05, "eleven_flash_v2": 0.05, "eleven_turbo_v2": 0.05}

VOICE_SETTINGS = {
    "stability": 0.5,
    "similarity_boost": 0.8,
    "style": 0.2,
    "use_speaker_boost": True,
    "speed": 1.0,
}


def log(msg: str) -> None:
    sys.stderr.write("[generate_audio] %s\n" % msg)
    sys.stderr.flush()


def load_env() -> None:
    env_file = REPO_ROOT / "build" / ".env"
    if not env_file.exists():
        return
    try:
        from dotenv import load_dotenv  # type: ignore
    except ImportError:
        log("build/.env found but python-dotenv is not installed; using os.environ only (pip install python-dotenv)")
        return
    load_dotenv(env_file, override=False)


# ----------------------------------------------------------------------------- text


def read_input_text(args) -> str:
    if args.text:
        return pathlib.Path(args.text).read_text(encoding="utf-8")
    data = json.loads(pathlib.Path(args.storyboard).read_text(encoding="utf-8"))
    text = data.get("narration_full")
    if not text or not str(text).strip():
        raise SystemExit("storyboard has no narration_full")
    return str(text)


def load_aliases() -> dict:
    if not DICT_PATH.exists():
        log("no pronunciation dictionary at %s" % DICT_PATH)
        return {}
    data = json.loads(DICT_PATH.read_text(encoding="utf-8"))
    aliases = data.get("aliases", {})
    return {k: v for k, v in aliases.items() if isinstance(k, str) and isinstance(v, str) and k}


def apply_aliases(text: str, aliases: dict) -> tuple[str, list]:
    """Case-sensitive whole-word replacement, longest term first, single pass (no cascading)."""
    if not aliases:
        return text, []
    terms = sorted(aliases, key=len, reverse=True)
    pattern = re.compile(r"(?<![A-Za-z0-9_])(?:%s)(?![A-Za-z0-9_])" % "|".join(re.escape(t) for t in terms))
    counts: dict = {}

    def sub(m):
        term = m.group(0)
        counts[term] = counts.get(term, 0) + 1
        return aliases[term]

    out = pattern.sub(sub, text)
    applied = [{"term": t, "alias": aliases[t], "count": c} for t, c in sorted(counts.items())]
    return out, applied


def split_paragraphs(text: str) -> list:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    paras = [re.sub(r"[ \t]+\n", "\n", p).strip() for p in re.split(r"\n\s*\n", text)]
    return [p for p in paras if p]


def split_sentences(paragraph: str) -> list:
    parts = re.split(r"(?<=[.!?])\s+", paragraph.strip())
    return [p for p in parts if p]


def hard_split(text: str, limit: int) -> list:
    out = []
    while len(text) > limit:
        cut = text.rfind(" ", 0, limit)
        if cut <= 0:
            cut = limit
        out.append(text[:cut].strip())
        text = text[cut:].strip()
    if text:
        out.append(text)
    return out


def chunk_text(paragraphs: list, max_chars: int) -> list:
    """Pack whole paragraphs into chunks of <= max_chars; split a paragraph only when it alone is too long."""
    units = []
    for p in paragraphs:
        if len(p) <= max_chars:
            units.append(p)
            continue
        buf = ""
        for s in split_sentences(p):
            pieces = hard_split(s, max_chars) if len(s) > max_chars else [s]
            for piece in pieces:
                if buf and len(buf) + 1 + len(piece) > max_chars:
                    units.append(buf)
                    buf = piece
                else:
                    buf = (buf + " " + piece).strip()
        if buf:
            units.append(buf)
    chunks = []
    cur = ""
    for u in units:
        if cur and len(cur) + 2 + len(u) > max_chars:
            chunks.append(cur)
            cur = u
        else:
            cur = (cur + "\n\n" + u) if cur else u
    if cur:
        chunks.append(cur)
    return chunks


# ------------------------------------------------------------------------------ api


def tts_with_timestamps(chunk: str, previous_text: str, next_text: str, voice_id: str, model: str,
                        seed: int, api_key: str, attempts: int = 5) -> dict:
    url = "%s/text-to-speech/%s/with-timestamps?output_format=%s" % (API_BASE, voice_id, OUTPUT_FORMAT)
    body = {
        "text": chunk,
        "model_id": model,
        "voice_settings": dict(VOICE_SETTINGS),
        "previous_text": previous_text,
        "next_text": next_text,
        "seed": seed,
    }
    data = json.dumps(body).encode("utf-8")
    delay = 2.0
    for attempt in range(1, attempts + 1):
        req = urllib.request.Request(url, data=data, method="POST", headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:300]
            except Exception:
                pass
            if e.code == 429 or e.code >= 500:
                log("HTTP %s on attempt %d/%d; retrying in %.0fs %s" % (e.code, attempt, attempts, delay, detail))
                time.sleep(delay)
                delay *= 2
                continue
            raise SystemExit("ElevenLabs HTTP %s: %s" % (e.code, detail))
        except urllib.error.URLError as e:
            log("network error on attempt %d/%d: %s" % (attempt, attempts, e.reason))
            time.sleep(delay)
            delay *= 2
    raise SystemExit("ElevenLabs request failed after %d attempts" % attempts)


# ------------------------------------------------------------------------- ffmpeg bits


def have(tool: str) -> bool:
    return shutil.which(tool) is not None


def run(cmd: list) -> None:
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        raise SystemExit("%s failed: %s" % (cmd[0], proc.stderr.strip()[-800:]))


def decode_to_wav(src: pathlib.Path, dst: pathlib.Path) -> None:
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-ar", str(SAMPLE_RATE), "-ac", "1",
         "-c:a", "pcm_s16le", str(dst)])


def wav_duration(path: pathlib.Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / float(w.getframerate())


def probe_duration(path: pathlib.Path) -> float:
    if have("ffprobe"):
        proc = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                               "-of", "default=nw=1:nk=1", str(path)], stdout=subprocess.PIPE, text=True)
        try:
            return float(proc.stdout.strip())
        except ValueError:
            pass
    return wav_duration(path)


def concat_wavs(wavs: list, out: pathlib.Path, fade_ms: int, durations: list) -> None:
    if fade_ms <= 0 or len(wavs) == 1:
        listing = out.parent / "concat.txt"
        listing.write_text("".join("file '%s'\n" % str(p).replace("'", "'\\''") for p in wavs), encoding="utf-8")
        run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(listing),
             "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s16le", str(out)])
        listing.unlink(missing_ok=True)
        return
    fade = fade_ms / 1000.0
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for p in wavs:
        cmd += ["-i", str(p)]
    parts = []
    for i, d in enumerate(durations):
        parts.append("[%d:a]afade=t=in:st=0:d=%.3f,afade=t=out:st=%.3f:d=%.3f[a%d]" % (i, fade, max(0.0, d - fade), fade, i))
    graph = ";".join(parts) + ";" + "".join("[a%d]" % i for i in range(len(wavs))) + "concat=n=%d:v=0:a=1[out]" % len(wavs)
    cmd += ["-filter_complex", graph, "-map", "[out]", "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s16le", str(out)]
    run(cmd)


def write_silence(path: pathlib.Path, seconds: float) -> None:
    if have("ffmpeg"):
        run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=%d:cl=mono" % SAMPLE_RATE,
             "-t", "%.3f" % seconds, "-c:a", "pcm_s16le", str(path)])
        return
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(b"\x00\x00" * int(seconds * SAMPLE_RATE))


# -------------------------------------------------------------------------- alignment


def build_alignment(chunk_records: list) -> dict:
    """Concatenate per-chunk character alignments; each chunk's times shift by its offset_s."""
    chars: list = []
    starts: list = []
    ends: list = []
    for i, rec in enumerate(chunk_records):
        off = rec["offset_s"]
        al = rec["alignment"]
        if i > 0:
            chars.append("\n")
            starts.append(round(off, 4))
            ends.append(round(off, 4))
        for c, s, e in zip(al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]):
            chars.append(c)
            starts.append(round(off + float(s), 4))
            ends.append(round(off + float(e), 4))
    return {"characters": chars, "character_start_times_seconds": starts, "character_end_times_seconds": ends}


def synthetic_alignment(text: str, seconds: float) -> dict:
    n = max(1, len(text))
    step = seconds / n
    return {
        "characters": list(text),
        "character_start_times_seconds": [round(i * step, 4) for i in range(len(text))],
        "character_end_times_seconds": [round((i + 1) * step, 4) for i in range(len(text))],
    }


# ------------------------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--text", help="plain-text narration file")
    src.add_argument("--storyboard", help="storyboard JSON; uses its narration_full field")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--voice-id", default=None, help="ElevenLabs voice id (default ELEVEN_VOICE_ID)")
    ap.add_argument("--model", default=None, help="model id (default ELEVEN_MODEL_ID or %s)" % DEFAULT_MODEL)
    ap.add_argument("--format", choices=["long", "short"], default="long", help="short = one chunk")
    ap.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS, help="chunk size cap (default %d)" % DEFAULT_MAX_CHARS)
    ap.add_argument("--fade-ms", type=int, default=0, help="optional fade in/out per chunk at the stitch (0 = plain concat)")
    ap.add_argument("--seed", type=int, default=None, help="override ELEVEN_SEED (use a new seed when regenerating a bad chunk)")
    ap.add_argument("--only-chunks", default="", help="comma-separated chunk indexes to regenerate; others reuse DIR/chunks/NN.mp3")
    ap.add_argument("--dry-run", action="store_true", help="no network: silent wav + synthetic alignment")
    args = ap.parse_args()

    load_env()
    model = args.model or os.environ.get("ELEVEN_MODEL_ID") or DEFAULT_MODEL
    voice_id = args.voice_id or os.environ.get("ELEVEN_VOICE_ID", "")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "")
    try:
        seed = args.seed if args.seed is not None else int(os.environ.get("ELEVEN_SEED", DEFAULT_SEED))
    except ValueError:
        seed = DEFAULT_SEED
    only = set()
    if args.only_chunks.strip():
        try:
            only = {int(x) for x in args.only_chunks.split(",") if x.strip()}
        except ValueError:
            raise SystemExit("--only-chunks expects comma-separated integers")

    out = pathlib.Path(args.out)
    chunks_dir = out / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)

    original = read_input_text(args)
    aliases = load_aliases()
    text, applied = apply_aliases(original, aliases)
    limit = MODEL_LIMITS.get(model, MODEL_LIMITS["eleven_v3"])
    max_chars = min(args.max_chars, limit)
    paragraphs = split_paragraphs(text)
    if not paragraphs:
        raise SystemExit("narration text is empty")
    if args.format == "short":
        whole = "\n\n".join(paragraphs)
        if len(whole) <= limit:
            chunks = [whole]
        else:
            log("short narration is %d chars, above the %s limit of %d; chunking anyway" % (len(whole), model, limit))
            chunks = chunk_text(paragraphs, max_chars)
    else:
        chunks = chunk_text(paragraphs, max_chars)
    chars_sent = sum(len(c) for c in chunks)
    credits = chars_sent * CREDITS_PER_CHAR.get(model, 1.0)
    usd = chars_sent / 1000.0 * USD_PER_1K_CHARS.get(model, 0.10)
    log("%d chars (%d after aliases, %d alias hits), %d chunk(s), model %s, ~%d credits" % (
        len(original), chars_sent, sum(a["count"] for a in applied), len(chunks), model, credits))

    records = []
    if args.dry_run:
        log("dry run: writing %.0f s of silence and a synthetic alignment (no API call)" % DRY_RUN_SECONDS)
        write_silence(out / "narration.wav", DRY_RUN_SECONDS)
        duration = wav_duration(out / "narration.wav")
        offset = 0.0
        for i, chunk in enumerate(chunks):
            share = duration * len(chunk) / float(chars_sent)
            records.append({"index": i, "file": None, "chars": len(chunk), "duration_s": round(share, 4),
                            "offset_s": round(offset, 4), "alignment": synthetic_alignment(chunk, share)})
            offset += share
        source = "dry-run"
    else:
        if not api_key:
            raise SystemExit("ELEVENLABS_API_KEY is not set (build/.env or environment)")
        if not voice_id:
            raise SystemExit("no voice id: pass --voice-id or set ELEVEN_VOICE_ID")
        if not have("ffmpeg"):
            raise SystemExit("ffmpeg is required to decode and concatenate chunks")
        offset = 0.0
        wavs = []
        durations = []
        for i, chunk in enumerate(chunks):
            prev_text = chunks[i - 1][-600:] if i > 0 else ""
            next_text = chunks[i + 1][:600] if i + 1 < len(chunks) else ""
            mp3 = chunks_dir / ("%02d.mp3" % i)
            meta = chunks_dir / ("%02d.json" % i)
            if only and i not in only and mp3.exists() and meta.exists():
                log("chunk %02d/%02d: reusing %s" % (i + 1, len(chunks), mp3.name))
                resp = json.loads(meta.read_text(encoding="utf-8"))
            else:
                log("chunk %02d/%02d: %d chars" % (i + 1, len(chunks), len(chunk)))
                resp = tts_with_timestamps(chunk, prev_text, next_text, voice_id, model, seed, api_key)
                if "audio_base64" not in resp or "alignment" not in resp:
                    raise SystemExit("unexpected response for chunk %d (keys: %s)" % (i, ", ".join(sorted(resp.keys()))))
                mp3.write_bytes(base64.b64decode(resp["audio_base64"]))
                meta.write_text(json.dumps({"alignment": resp["alignment"], "request_id": resp.get("request_id"),
                                            "chars": len(chunk), "seed": seed}), encoding="utf-8")
            wav_chunk = chunks_dir / ("%02d.wav" % i)
            decode_to_wav(mp3, wav_chunk)
            d = probe_duration(wav_chunk)
            records.append({"index": i, "file": "chunks/%02d.mp3" % i, "chars": len(chunk), "duration_s": round(d, 4),
                            "offset_s": round(offset, 4), "alignment": resp["alignment"],
                            "request_id": resp.get("request_id")})
            wavs.append(wav_chunk)
            durations.append(d)
            offset += d
        concat_wavs(wavs, out / "narration.wav", args.fade_ms, durations)
        for w in wavs:
            w.unlink(missing_ok=True)
        duration = wav_duration(out / "narration.wav")
        source = "elevenlabs"

    alignment = build_alignment(records)
    alignment.update({
        "text": "\n".join(c for c in chunks),
        "source": source,
        "model": model,
        "sample_rate": SAMPLE_RATE,
        "duration_s": round(duration, 4),
        "chunks": [{k: v for k, v in r.items() if k != "alignment"} for r in records],
    })
    (out / "alignment.json").write_text(json.dumps(alignment, ensure_ascii=False), encoding="utf-8")

    voice = {
        "duration_s": round(duration, 3),
        "chars": len(original),
        "chars_sent": chars_sent,
        "chunks": len(chunks),
        "credits_estimate": round(credits),
        "usd_estimate": round(usd, 4),
        "model": model,
        "voice_id_hint": ("..." + voice_id[-4:]) if voice_id else "none",
        "format": args.format,
        "seed": seed,
        "output_format": OUTPUT_FORMAT,
        "voice_settings": VOICE_SETTINGS,
        "aliases_applied": applied,
        "dry_run": bool(args.dry_run),
        "created": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    (out / "voice.json").write_text(json.dumps(voice, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "duration_s": voice["duration_s"], "chunks": len(chunks),
                      "credits_estimate": voice["credits_estimate"], "dry_run": bool(args.dry_run)}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
    except KeyboardInterrupt:
        sys.exit(1)
