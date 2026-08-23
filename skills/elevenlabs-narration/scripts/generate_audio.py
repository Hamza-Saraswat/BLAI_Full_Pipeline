#!/usr/bin/env python3
"""Generate narration with ElevenLabs or with a local Kokoro model, and keep word timestamps.

Usage:
  generate_audio.py --text FILE.txt --out DIR [--engine auto|elevenlabs|kokoro] [--voice-id ID]
                    [--model eleven_multilingual_v2] [--format long|short] [--max-chars 4500]
                    [--fade-ms 0] [--kokoro-voice am_eric] [--kokoro-speed 1.05]
                    [--kokoro-root DIR] [--align auto|whisper|proportional] [--dry-run]
  generate_audio.py --storyboard FILE.json --out DIR ...   (reads the storyboard's narration_full)

Outputs in DIR (one contract for both engines, so no later stage changes):
  narration.wav    44.1 kHz mono PCM, all chunks concatenated
  alignment.json   {words[{word,start,end}], source, characters, character_*_times_seconds, chunks}
                   character times are ElevenLabs' own when it ran, derived from the words otherwise
  chunks/NN.mp3    raw ElevenLabs output per chunk (mp3_44100_192) + chunks/NN.json (its alignment)
  chunks/NN.wav    raw Kokoro output per chunk (24 kHz) + chunks/NN.json + chunks/NN.txt
  voice.json       {duration_s, chars, chunks, credits_estimate, model, engine, alignment_source, ...}

Steps: apply pronunciation_dictionary.json aliases -> chunk at paragraph boundaries (<= --max-chars,
one chunk for --format short) -> synthesize each chunk -> decode, measure, concatenate with ffmpeg.
ElevenLabs POSTs /v1/text-to-speech/{voice}/with-timestamps per chunk with previous_text/next_text
and a pinned seed. Kokoro runs the v1 repo's pipeline/scripts/tts_local.py in its own venv, once per
chunk, then times the words with whisper.cpp when a built binary is there ("source": "whisper") and
otherwise by spreading each chunk's measured duration over its words by character length
("source": "proportional"). Kokoro needs no key and makes no network call.

--engine auto (the default) picks ElevenLabs when ELEVENLABS_API_KEY and ELEVEN_VOICE_ID are both
set, else Kokoro when the local model file is there, else it fails naming both options. The engine
that ran and the reason are printed to stderr as one line.

Env (build/.env or the environment): ELEVENLABS_API_KEY, ELEVEN_VOICE_ID, ELEVEN_MODEL_ID,
ELEVEN_SEED; BLAI_KOKORO_ROOT, WHISPER_CPP_BIN, WHISPER_CPP_MODEL for the local engine.
--only-chunks 2,5 re-synthesizes just those chunks (pair with --seed for a fresh take) and reuses the
stored audio + alignment of every other chunk, then rebuilds narration.wav and alignment.json.
--dry-run makes no network call and starts no engine: it writes a 3 s silent narration.wav and a
synthetic alignment so qa_transcribe.py and captions.py can run. Exit 0/1. Logs go to stderr.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import difflib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
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

# Local Kokoro engine (credential-free test runs). The v1 repo owns the model, the venv and the
# runner; nothing here writes into it. Override with --kokoro-root or BLAI_KOKORO_ROOT when it moves.
KOKORO_ROOT = pathlib.Path.home() / "Documents" / "Projects" / "BLAI_Animator"
KOKORO_VOICE = "am_eric"
KOKORO_SPEED = 1.05
KOKORO_MODEL_NAME = "kokoro-v1.0"
WHISPER_MODEL_NAME = "ggml-base.en.bin"

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
        # absolute paths: ffmpeg resolves a relative entry against the listing's own directory
        listing.write_text("".join("file '%s'\n" % str(pathlib.Path(p).resolve()).replace("'", "'\\''")
                                   for p in wavs), encoding="utf-8")
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


# ---------------------------------------------------------------------------- kokoro


def kokoro_paths(root) -> dict:
    """Where the v1 repo keeps the local voice: its venv python, the runner, the model files."""
    root = pathlib.Path(root).expanduser()
    return {
        "root": root,
        "python": root / "pipeline" / ".venv" / "bin" / "python",
        "script": root / "pipeline" / "scripts" / "tts_local.py",
        "config": root / "pipeline" / "voice.config.json",
        "model": root / "pipeline" / "models" / "kokoro-v1.0.onnx",
        "voices": root / "pipeline" / "models" / "voices-v1.0.bin",
        "whisper": root / "render" / "remotion" / "whisper.cpp",
    }


def choose_engine(requested: str, kk: dict, api_key: str, voice_id: str) -> tuple:
    """Return (engine, reason). Raises SystemExit naming both options when neither is usable."""
    eleven_ok = bool(api_key and voice_id)
    kokoro_ok = kk["model"].exists()
    eleven_missing = " and ".join(n for n, v in (("ELEVENLABS_API_KEY", api_key),
                                                 ("ELEVEN_VOICE_ID", voice_id)) if not v)
    if requested == "elevenlabs":
        if not eleven_ok:
            raise SystemExit("--engine elevenlabs needs %s (build/.env or the environment)" % eleven_missing)
        return "elevenlabs", "asked for with --engine elevenlabs"
    if requested == "kokoro":
        if not kokoro_ok:
            raise SystemExit("--engine kokoro needs the model at %s (pass --kokoro-root or set "
                             "BLAI_KOKORO_ROOT)" % kk["model"])
        return "kokoro", "asked for with --engine kokoro"
    if eleven_ok:
        return "elevenlabs", "ELEVENLABS_API_KEY and ELEVEN_VOICE_ID are both set"
    if kokoro_ok:
        return "kokoro", "%s not set, local model found at %s" % (eleven_missing, kk["model"])
    raise SystemExit("no voice engine: set ELEVENLABS_API_KEY and ELEVEN_VOICE_ID for ElevenLabs, "
                     "or point --kokoro-root at a checkout with pipeline/models/kokoro-v1.0.onnx "
                     "for the local Kokoro engine (looked at %s)" % kk["model"])


def check_kokoro(kk: dict) -> None:
    for key, what in (("python", "venv python"), ("script", "tts_local.py"), ("config", "voice.config.json"),
                      ("model", "kokoro model"), ("voices", "voices bin")):
        if not kk[key].exists():
            raise SystemExit("kokoro %s not found: %s (pass --kokoro-root)" % (what, kk[key]))
    if not have("ffmpeg"):
        raise SystemExit("ffmpeg is required to resample and concatenate Kokoro chunks")


def kokoro_synth(kk: dict, text_file: pathlib.Path, out_wav: pathlib.Path, voice: str, speed: float) -> dict:
    """One chunk through the v1 runner. --no-normalize: our alias pass already fixed the spoken text."""
    cmd = [str(kk["python"]), str(kk["script"]), "--script-file", str(text_file), "--out", str(out_wav),
           "--engine", "kokoro", "--voice", voice, "--speed", "%g" % speed,
           "--config", str(kk["config"]), "--no-normalize"]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0 or not out_wav.exists():
        raise SystemExit("kokoro tts_local.py exited %d: %s" % (proc.returncode, proc.stderr.strip()[-800:]))
    try:
        return json.loads(proc.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return {}


# ------------------------------------------------------------------- word timing


def find_whisper(kk: dict) -> tuple:
    """A built whisper.cpp binary and an English model, or (None, None). No build is attempted."""
    cands = []
    env_bin = (os.environ.get("WHISPER_CPP_BIN") or "").strip()
    if env_bin:
        cands.append(pathlib.Path(env_bin).expanduser())
    wroot = kk["whisper"]
    cands += [wroot / "build" / "bin" / "whisper-cli", wroot / "build" / "bin" / "main", wroot / "main"]
    for name in ("whisper-cli", "whisper-cpp", "main"):
        found = shutil.which(name)
        if found:
            cands.append(pathlib.Path(found))
    binary = next((c for c in cands if c.is_file() and os.access(str(c), os.X_OK)), None)
    if binary is None:
        return None, None
    models = []
    env_model = (os.environ.get("WHISPER_CPP_MODEL") or "").strip()
    if env_model:
        models.append(pathlib.Path(env_model).expanduser())
    models += [wroot / WHISPER_MODEL_NAME, binary.parent / WHISPER_MODEL_NAME,
               wroot / "models" / WHISPER_MODEL_NAME,
               pathlib.Path.home() / ".cache" / "whisper.cpp" / WHISPER_MODEL_NAME]
    model = next((m for m in models if m.is_file()), None)
    if model is None:
        return None, None
    return binary, model


def whisper_words(wav: pathlib.Path, binary: pathlib.Path, model: pathlib.Path) -> list:
    """Word-level times from whisper.cpp: -ml 1 with -sow emits one JSON segment per word."""
    with tempfile.TemporaryDirectory() as tmp:
        wav16 = pathlib.Path(tmp) / "audio16k.wav"
        run(["ffmpeg", "-y", "-v", "error", "-i", str(wav), "-ar", "16000", "-ac", "1",
             "-c:a", "pcm_s16le", str(wav16)])  # whisper.cpp only reads 16 kHz mono
        prefix = pathlib.Path(tmp) / "words"
        cmd = [str(binary), "-m", str(model), "-f", str(wav16), "-oj", "-of", str(prefix),
               "-ml", "1", "-sow", "-np", "-l", "en"]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            raise RuntimeError("whisper.cpp exited %d: %s" % (proc.returncode, proc.stderr.strip()[-400:]))
        data = json.loads(pathlib.Path(str(prefix) + ".json").read_text(encoding="utf-8"))
    words = []
    for item in data.get("transcription", []):
        text = (item.get("text") or "").strip()
        if not text:
            continue
        offs = item.get("offsets") or {}
        words.append({"word": text, "start": float(offs.get("from", 0)) / 1000.0,
                      "end": float(offs.get("to", 0)) / 1000.0})
    return words


def norm_word(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", word.lower())


def map_heard_onto_script(spoken: list, heard: list, duration: float) -> list:
    """Give every word we sent a time: 1:1 matches take the heard time, a run that whisper heard
    differently shares the run's span by word length, a run it missed shares the gap before the next
    word it did hear. The words stay the ones we sent, so captions.py still maps them to the script."""
    a = [norm_word(w) for w in spoken]
    b = [norm_word(w["word"]) for w in heard]
    out = []
    last_end = 0.0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                h = heard[j1 + k]
                out.append({"word": spoken[i1 + k], "start": h["start"], "end": h["end"]})
                last_end = h["end"]
            continue
        if tag == "insert":  # whisper heard words we never sent: keep the clock, drop the words
            if j2 > j1:
                last_end = heard[j2 - 1]["end"]
            continue
        block = spoken[i1:i2]
        if j2 > j1:
            span_start, span_end = heard[j1]["start"], heard[j2 - 1]["end"]
        else:  # nothing heard here: fill the gap up to the next word whisper did hear
            span_start = last_end
            span_end = heard[j1]["start"] if j1 < len(heard) else duration
        span_start = max(span_start, last_end)
        span_end = max(span_end, span_start)
        total = float(sum(max(1, len(norm_word(w))) for w in block)) or 1.0
        t = span_start
        for w in block:
            share = (span_end - span_start) * max(1, len(norm_word(w))) / total
            out.append({"word": w, "start": t, "end": t + share})
            t += share
        last_end = span_end
    return [{"word": w["word"], "start": round(max(0.0, w["start"]), 4),
             "end": round(max(w["start"], min(w["end"], duration)), 4)} for w in out]


def proportional_words(chunks: list, records: list) -> list:
    """Fallback timing: each chunk's measured duration split over its words by character length."""
    words = []
    for chunk, rec in zip(chunks, records):
        parts = chunk.split()
        if not parts:
            continue
        total = float(sum(max(1, len(p)) for p in parts))
        t = float(rec["offset_s"])
        for p in parts:
            share = float(rec["duration_s"]) * max(1, len(p)) / total
            words.append({"word": p, "start": round(t, 4), "end": round(t + share, 4)})
            t += share
    return words


def words_to_chars(words: list) -> dict:
    """Character arrays derived from word times (a space between words), so every reader of the
    old character contract keeps working when ElevenLabs did not produce one."""
    chars: list = []
    starts: list = []
    ends: list = []
    for i, w in enumerate(words):
        if i:
            chars.append(" ")
            starts.append(round(words[i - 1]["end"], 4))
            ends.append(round(w["start"], 4))
        text = w["word"]
        span = max(0.0, float(w["end"]) - float(w["start"]))
        n = max(1, len(text))
        for k, c in enumerate(text):
            chars.append(c)
            starts.append(round(float(w["start"]) + span * k / n, 4))
            ends.append(round(float(w["start"]) + span * (k + 1) / n, 4))
    return {"characters": chars, "character_start_times_seconds": starts, "character_end_times_seconds": ends}


def chars_to_words(al: dict) -> list:
    """The word split captions.py has always used, so an ElevenLabs alignment keeps its timing."""
    words = []
    cur: list = []
    for c, s, e in zip(al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]):
        if c.isspace():
            if cur:
                words.append({"word": "".join(x[0] for x in cur), "start": cur[0][1], "end": cur[-1][2]})
                cur = []
            continue
        cur.append((c, float(s), float(e)))
    if cur:
        words.append({"word": "".join(x[0] for x in cur), "start": cur[0][1], "end": cur[-1][2]})
    return words


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
    ap.add_argument("--engine", choices=["auto", "elevenlabs", "kokoro"], default="auto",
                    help="auto (default): ElevenLabs when its key and voice id are set, else local Kokoro")
    ap.add_argument("--voice-id", default=None, help="ElevenLabs voice id (default ELEVEN_VOICE_ID)")
    ap.add_argument("--model", default=None, help="model id (default ELEVEN_MODEL_ID or %s)" % DEFAULT_MODEL)
    ap.add_argument("--format", choices=["long", "short"], default="long", help="short = one chunk")
    ap.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS, help="chunk size cap (default %d)" % DEFAULT_MAX_CHARS)
    ap.add_argument("--fade-ms", type=int, default=0, help="optional fade in/out per chunk at the stitch (0 = plain concat)")
    ap.add_argument("--seed", type=int, default=None, help="override ELEVEN_SEED (use a new seed when regenerating a bad chunk)")
    ap.add_argument("--only-chunks", default="", help="comma-separated chunk indexes to regenerate; others reuse DIR/chunks/NN.*")
    ap.add_argument("--kokoro-voice", default=KOKORO_VOICE, help="Kokoro voice id (default %s)" % KOKORO_VOICE)
    ap.add_argument("--kokoro-speed", type=float, default=KOKORO_SPEED, help="Kokoro speed (default %s)" % KOKORO_SPEED)
    ap.add_argument("--kokoro-root", default=None, help="checkout that owns the Kokoro model, venv and "
                    "tts_local.py (default BLAI_KOKORO_ROOT or %s)" % KOKORO_ROOT)
    ap.add_argument("--align", choices=["auto", "whisper", "proportional"], default="auto",
                    help="Kokoro word timing: auto (whisper.cpp when built, else proportional)")
    ap.add_argument("--dry-run", action="store_true", help="no network, no engine: silent wav + synthetic alignment")
    args = ap.parse_args()

    load_env()
    model = args.model or os.environ.get("ELEVEN_MODEL_ID") or DEFAULT_MODEL
    voice_id = args.voice_id or os.environ.get("ELEVEN_VOICE_ID", "")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "")
    kk = kokoro_paths(args.kokoro_root or os.environ.get("BLAI_KOKORO_ROOT") or KOKORO_ROOT)
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
    if args.dry_run:
        engine, why = (args.engine if args.engine != "auto" else "none"), "dry run: nothing is synthesized"
    else:
        engine, why = choose_engine(args.engine, kk, api_key, voice_id)
    log("engine: %s (%s)" % (engine, why))
    local = engine == "kokoro"
    credits = 0.0 if local else chars_sent * CREDITS_PER_CHAR.get(model, 1.0)
    usd = 0.0 if local else chars_sent / 1000.0 * USD_PER_1K_CHARS.get(model, 0.10)
    engine_model = KOKORO_MODEL_NAME if local else model
    log("%d chars (%d after aliases, %d alias hits), %d chunk(s), model %s, ~%d credits" % (
        len(original), chars_sent, sum(a["count"] for a in applied), len(chunks), engine_model, credits))

    records = []
    words = None
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
    elif local:
        check_kokoro(kk)
        log("kokoro: %s, voice %s, speed %s" % (kk["model"], args.kokoro_voice, args.kokoro_speed))
        offset = 0.0
        wavs = []
        durations = []
        for i, chunk in enumerate(chunks):
            raw = chunks_dir / ("%02d.wav" % i)          # 24 kHz, straight from Kokoro
            meta = chunks_dir / ("%02d.json" % i)
            chunk_txt = chunks_dir / ("%02d.txt" % i)    # exactly what the engine was asked to say
            if only and i not in only and raw.exists() and meta.exists():
                log("chunk %02d/%02d: reusing %s" % (i + 1, len(chunks), raw.name))
            else:
                log("chunk %02d/%02d: %d chars" % (i + 1, len(chunks), len(chunk)))
                chunk_txt.write_text(chunk + "\n", encoding="utf-8")
                info = kokoro_synth(kk, chunk_txt, raw, args.kokoro_voice, args.kokoro_speed)
                meta.write_text(json.dumps({"chars": len(chunk), "voice": args.kokoro_voice,
                                            "speed": args.kokoro_speed, "engine": "kokoro",
                                            "kokoro": info}), encoding="utf-8")
            wav_chunk = chunks_dir / ("%02d-44k.wav" % i)
            decode_to_wav(raw, wav_chunk)               # 44.1 kHz mono, the pipeline's contract
            d = probe_duration(wav_chunk)
            records.append({"index": i, "file": "chunks/%02d.wav" % i, "chars": len(chunk),
                            "duration_s": round(d, 4), "offset_s": round(offset, 4)})
            wavs.append(wav_chunk)
            durations.append(d)
            offset += d
        concat_wavs(wavs, out / "narration.wav", args.fade_ms, durations)
        for w in wavs:
            w.unlink(missing_ok=True)
        duration = wav_duration(out / "narration.wav")
        spoken = " ".join(chunks).split()
        binary, wmodel = (None, None) if args.align == "proportional" else find_whisper(kk)
        if args.align == "whisper" and binary is None:
            raise SystemExit("--align whisper needs a built whisper.cpp binary and an English model "
                             "(looked under %s; set WHISPER_CPP_BIN and WHISPER_CPP_MODEL)" % kk["whisper"])
        if binary is not None:
            log("alignment: whisper.cpp %s with %s" % (binary.name, wmodel.name))
            try:
                heard = whisper_words(out / "narration.wav", binary, wmodel)
                if not heard:
                    raise RuntimeError("whisper.cpp returned no words")
                words = map_heard_onto_script(spoken, heard, duration)
                source = "whisper"
                log("alignment: %d words heard, %d script words timed" % (len(heard), len(words)))
            except (RuntimeError, OSError, ValueError, KeyError) as e:
                log("alignment: whisper.cpp failed (%s); falling back to proportional timing" % e)
                words = None
        elif args.align != "proportional":
            log("alignment: no built whisper.cpp under %s; using proportional timing" % kk["whisper"])
        if words is None:
            words = proportional_words(chunks, records)
            source = "proportional"
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

    if words is None:  # ElevenLabs and dry run: the character alignment is the source of truth
        alignment = build_alignment(records)
        words = chars_to_words(alignment)
    else:              # Kokoro: word times are measured, character times are derived from them
        alignment = words_to_chars(words)
    alignment.update({
        "words": [{"word": w["word"], "start": round(float(w["start"]), 4), "end": round(float(w["end"]), 4)}
                  for w in words],
        "text": "\n".join(c for c in chunks),
        "source": source,
        "engine": engine,
        "model": engine_model,
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
        "model": engine_model,
        "engine": engine,
        "alignment_source": source,
        "voice_id_hint": (args.kokoro_voice if local else
                          (("..." + voice_id[-4:]) if voice_id else "none")),
        "format": args.format,
        "seed": seed,
        "output_format": "wav_24000" if local else OUTPUT_FORMAT,
        "voice_settings": {"voice": args.kokoro_voice, "speed": args.kokoro_speed} if local else VOICE_SETTINGS,
        "aliases_applied": applied,
        "script_words": len(original.split()),
        "aligned_words": len(words),
        # pacing: script words per second of finished audio (skills/script-gates/voice.config.json wps)
        "words_per_second": round(len(original.split()) / duration, 3) if duration else 0.0,
        "dry_run": bool(args.dry_run),
        "created": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    (out / "voice.json").write_text(json.dumps(voice, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "duration_s": voice["duration_s"], "chunks": len(chunks),
                      "engine": engine, "alignment_source": source,
                      "words_per_second": voice["words_per_second"],
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
