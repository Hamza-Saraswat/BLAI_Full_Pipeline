#!/usr/bin/env python3
"""Transcribe the generated narration and diff it against the script (WER gate).

Usage:
  qa_transcribe.py --audio DIR/narration.wav --script FILE.txt --out DIR [--threshold 0.03]
                   [--engine auto|faster-whisper|whisper-cpp] [--dry-run]

Engines, in order: faster_whisper (model small.en, CUDA float16 when available, else CPU int8),
then a whisper.cpp binary on PATH (whisper-cli, whisper-cpp or main; model from WHISPER_CPP_MODEL),
else exit 1 with install hints. Both texts are normalized (lowercase, punctuation stripped, digits
spelled out, spelled letters collapsed) before the word-level Levenshtein WER.

The reference is compared twice, as written and with pronunciation_dictionary.json aliases applied
(the voice was asked to read "Kwen"), and the better score is kept (--no-aliases disables this).

Outputs: DIR/transcript.json {engine, model, text, words[{word,start,end}], segments[]}
         DIR/qa.json {wer, threshold, pass, reference, mismatches[{expected, heard, at_s}], counts{}}
Exit 1 when wer > threshold (or on any failure). --dry-run fabricates a transcript from the script
(WER 0) so the rest of the stage can run without a model.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import wave

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
WHISPER_MODEL = "small.en"
DEFAULT_THRESHOLD = 0.03


def log(msg: str) -> None:
    sys.stderr.write("[qa_transcribe] %s\n" % msg)
    sys.stderr.flush()


def load_env() -> None:
    env_file = REPO_ROOT / "build" / ".env"
    if not env_file.exists():
        return
    try:
        from dotenv import load_dotenv  # type: ignore
    except ImportError:
        return
    load_dotenv(env_file, override=False)


DICT_PATH = SCRIPT_DIR.parent / "pronunciation_dictionary.json"


def apply_dictionary(text: str) -> str:
    """Same alias pass as generate_audio.py, so the reference can be judged as the voice was asked to read it."""
    if not DICT_PATH.exists():
        return text
    aliases = json.loads(DICT_PATH.read_text(encoding="utf-8")).get("aliases", {})
    terms = sorted((t for t in aliases if t), key=len, reverse=True)
    if not terms:
        return text
    pattern = re.compile(r"(?<![A-Za-z0-9_])(?:%s)(?![A-Za-z0-9_])" % "|".join(re.escape(t) for t in terms))
    return pattern.sub(lambda m: aliases[m.group(0)], text)


# ---------------------------------------------------------------------- normalization

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
SCALES = [(1000000000, "billion"), (1000000, "million"), (1000, "thousand")]


def _below_thousand(n: int) -> str:
    words = []
    if n >= 100:
        words += [ONES[n // 100], "hundred"]
        n %= 100
    if n >= 20:
        words.append(TENS[n // 10])
        if n % 10:
            words.append(ONES[n % 10])
    elif n > 0 or not words:
        words.append(ONES[n])
    return " ".join(words)


def number_to_words(n: int) -> str:
    if n < 0:
        return "minus " + number_to_words(-n)
    if 1100 <= n <= 2099 and n % 100 != 0 and not (2000 <= n <= 2009):
        return _below_thousand(n // 100) + " " + _below_thousand(n % 100)  # years and model numbers: "twenty twenty six"
    if n < 1000:
        return _below_thousand(n)
    words = []
    for value, name in SCALES:
        if n >= value:
            words.append(_below_thousand(n // value) + " " + name)
            n %= value
    if n:
        words.append(_below_thousand(n))
    return " ".join(words)


def spell_numbers(text: str) -> str:
    text = re.sub(r"(\d),(?=\d{3}\b)", r"\1", text)
    text = re.sub(r"\$(\d+(?:\.\d+)?)", r"\1 dollars ", text)
    text = text.replace("%", " percent ")
    text = re.sub(r"([a-zA-Z])(?=\d)", r"\1 ", text)

    def dec(m):
        whole, frac = m.group(1), m.group(2)
        return number_to_words(int(whole)) + " point " + " ".join(ONES[int(d)] for d in frac)

    text = re.sub(r"\b(\d+)\.(\d+)\b", dec, text)
    text = re.sub(r"(\d+)(?=[a-zA-Z])", r"\1 ", text)
    return re.sub(r"\d+", lambda m: number_to_words(int(m.group(0))), text)


def normalize_words(text: str) -> list:
    text = text.lower().replace("-", " ").replace("/", " ")
    text = spell_numbers(text)
    text = re.sub(r"[^a-z0-9' ]+", " ", text)
    words = [w.strip("'") for w in text.split()]
    words = [w for w in words if w]
    out: list = []
    run_: list = []
    for w in words + [None]:
        if w is not None and len(w) == 1 and w.isalpha():
            run_.append(w)
            continue
        if run_:
            if len(run_) >= 2:
                out.append("".join(run_))  # "d g x" -> "dgx", "k v" -> "kv"
            else:
                out.extend(run_)
            run_ = []
        if w is not None:
            out.append(w)
    return out


# ------------------------------------------------------------------------ transcription


def transcribe_faster_whisper(audio: pathlib.Path) -> dict:
    from faster_whisper import WhisperModel  # type: ignore
    device, compute = "cpu", "int8"
    try:
        import ctranslate2  # type: ignore
        if ctranslate2.get_cuda_device_count() > 0:
            device, compute = "cuda", "float16"
    except Exception:
        pass
    log("faster-whisper %s on %s/%s" % (WHISPER_MODEL, device, compute))
    model = WhisperModel(WHISPER_MODEL, device=device, compute_type=compute)
    segments, info = model.transcribe(str(audio), beam_size=5, word_timestamps=True, language="en")
    words, segs = [], []
    for seg in segments:
        segs.append({"start": round(seg.start, 3), "end": round(seg.end, 3), "text": seg.text.strip()})
        for w in (seg.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)})
    text = " ".join(s["text"] for s in segs)
    return {"engine": "faster-whisper", "model": WHISPER_MODEL, "text": text, "words": words, "segments": segs}


def find_whisper_cpp() -> tuple:
    for name in ("whisper-cli", "whisper-cpp", "main"):
        path = shutil.which(name)
        if path:
            return name, path
    return None, None


def transcribe_whisper_cpp(audio: pathlib.Path, binary: str) -> dict:
    model = os.environ.get("WHISPER_CPP_MODEL") or str(pathlib.Path.home() / ".cache" / "whisper.cpp" / "ggml-small.en.bin")
    if not pathlib.Path(model).exists():
        raise SystemExit("whisper.cpp model not found at %s (set WHISPER_CPP_MODEL)" % model)
    with tempfile.TemporaryDirectory() as tmp:
        prefix = pathlib.Path(tmp) / "out"
        cmd = [binary, "-m", model, "-f", str(audio), "-oj", "-of", str(prefix), "-ml", "1", "-np"]
        log("whisper.cpp: %s" % " ".join(cmd[:3]))
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            raise SystemExit("whisper.cpp failed: %s" % proc.stderr.strip()[-500:])
        data = json.loads((pathlib.Path(str(prefix) + ".json")).read_text(encoding="utf-8"))
    words, segs = [], []
    for item in data.get("transcription", []):
        offs = item.get("offsets", {})
        start, end = offs.get("from", 0) / 1000.0, offs.get("to", 0) / 1000.0
        t = item.get("text", "").strip()
        if not t:
            continue
        segs.append({"start": start, "end": end, "text": t})
        for w in t.split():
            words.append({"word": w, "start": start, "end": end})
    return {"engine": "whisper.cpp", "model": pathlib.Path(model).name, "text": " ".join(s["text"] for s in segs),
            "words": words, "segments": segs}


def transcribe(audio: pathlib.Path, engine: str) -> dict:
    if engine in ("auto", "faster-whisper"):
        try:
            import faster_whisper  # noqa: F401
            return transcribe_faster_whisper(audio)
        except ImportError:
            if engine == "faster-whisper":
                raise SystemExit("faster_whisper is not installed: pip install faster-whisper")
    name, path = find_whisper_cpp()
    if path:
        return transcribe_whisper_cpp(audio, path)
    raise SystemExit("no transcription engine: pip install faster-whisper (recommended), or install whisper.cpp "
                     "(whisper-cli on PATH) and set WHISPER_CPP_MODEL to a ggml-small.en.bin file")


def dry_run_transcript(script_text: str, audio: pathlib.Path) -> dict:
    try:
        with wave.open(str(audio), "rb") as w:
            duration = w.getnframes() / float(w.getframerate())
    except Exception:
        duration = 3.0
    raw = script_text.split()
    step = duration / max(1, len(raw))
    words = [{"word": w, "start": round(i * step, 3), "end": round((i + 1) * step, 3)} for i, w in enumerate(raw)]
    return {"engine": "dry-run", "model": "none", "text": " ".join(raw), "words": words,
            "segments": [{"start": 0.0, "end": round(duration, 3), "text": " ".join(raw)}]}


# --------------------------------------------------------------------------- WER diff


def align(ref: list, hyp: list) -> tuple:
    """Levenshtein on word lists; returns (distance, ops) with ops in (kind, i, j)."""
    n, m = len(ref), len(hyp)
    prev = list(range(m + 1))
    back = [[0] * (m + 1) for _ in range(n + 1)]  # 0 diag, 1 up (del), 2 left (ins)
    for j in range(1, m + 1):
        back[0][j] = 2
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        back[i][0] = 1
        ri = ref[i - 1]
        for j in range(1, m + 1):
            sub = prev[j - 1] + (0 if ri == hyp[j - 1] else 1)
            dele = prev[j] + 1
            ins = cur[j - 1] + 1
            best = sub
            k = 0
            if dele < best:
                best, k = dele, 1
            if ins < best:
                best, k = ins, 2
            cur[j] = best
            back[i][j] = k
        prev = cur
    dist = prev[m]
    ops = []
    i, j = n, m
    while i > 0 or j > 0:
        k = back[i][j]
        if i > 0 and j > 0 and k == 0:
            ops.append(("equal" if ref[i - 1] == hyp[j - 1] else "sub", i - 1, j - 1))
            i, j = i - 1, j - 1
        elif i > 0 and (j == 0 or k == 1):
            ops.append(("del", i - 1, None))
            i -= 1
        else:
            ops.append(("ins", None, j - 1))
            j -= 1
    ops.reverse()
    return dist, ops


def mismatches_from_ops(ops: list, ref: list, hyp: list, hyp_times: list) -> list:
    out = []
    cur = None
    for kind, i, j in ops:
        if kind == "equal":
            if cur:
                out.append(cur)
                cur = None
            continue
        if cur is None:
            at = hyp_times[j] if j is not None and j < len(hyp_times) else (hyp_times[min(len(hyp_times) - 1, i or 0)] if hyp_times else 0.0)
            cur = {"expected": [], "heard": [], "at_s": round(at, 2)}
        if i is not None:
            cur["expected"].append(ref[i])
        if j is not None:
            cur["heard"].append(hyp[j])
    if cur:
        out.append(cur)
    return [{"expected": " ".join(m["expected"]), "heard": " ".join(m["heard"]), "at_s": m["at_s"]} for m in out]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--script", required=True, help="the narration text that was sent (original spelling)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    ap.add_argument("--engine", choices=["auto", "faster-whisper", "whisper-cpp"], default="auto")
    ap.add_argument("--no-aliases", action="store_true", help="compare against the raw script only")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    load_env()

    audio = pathlib.Path(args.audio)
    if not audio.exists():
        raise SystemExit("audio not found: %s" % audio)
    script_text = pathlib.Path(args.script).read_text(encoding="utf-8")
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    transcript = dry_run_transcript(script_text, audio) if args.dry_run else transcribe(audio, args.engine)
    (out / "transcript.json").write_text(json.dumps(transcript, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    ref = normalize_words(script_text)
    hyp_words = transcript["words"] or [{"word": w, "start": 0.0, "end": 0.0} for w in transcript["text"].split()]
    hyp = []
    hyp_times = []
    for w in hyp_words:
        toks = normalize_words(w["word"])
        for t in toks:
            hyp.append(t)
            hyp_times.append(float(w.get("start", 0.0)))
    # collapse spelled letters across word boundaries ("d", "g", "x" arriving as separate words)
    hyp_joined = normalize_words(" ".join(hyp))
    if len(hyp_joined) != len(hyp):
        times = []
        k = 0
        for t in hyp_joined:
            times.append(hyp_times[min(k, len(hyp_times) - 1)] if hyp_times else 0.0)
            k += max(1, len(t)) if len(t) > 1 and all(len(h) == 1 for h in hyp[k:k + len(t)]) else 1
        hyp, hyp_times = hyp_joined, times

    if not ref:
        raise SystemExit("script is empty after normalization")
    dist, ops = align(ref, hyp)
    ref_used = "script"
    if not args.no_aliases:
        aliased = apply_dictionary(script_text)
        if aliased != script_text:
            ref2 = normalize_words(aliased)
            dist2, ops2 = align(ref2, hyp)
            if dist2 / float(len(ref2)) < dist / float(len(ref)):
                ref, dist, ops, ref_used = ref2, dist2, ops2, "script+aliases"
    wer = dist / float(len(ref))
    counts = {"ref_words": len(ref), "hyp_words": len(hyp),
              "sub": sum(1 for o in ops if o[0] == "sub"), "ins": sum(1 for o in ops if o[0] == "ins"),
              "del": sum(1 for o in ops if o[0] == "del")}
    mism = mismatches_from_ops(ops, ref, hyp, hyp_times)
    passed = wer <= args.threshold
    qa = {"wer": round(wer, 4), "threshold": args.threshold, "pass": passed, "engine": transcript["engine"],
          "reference": ref_used, "mismatches": mism, "counts": counts}
    (out / "qa.json").write_text(json.dumps(qa, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    log("WER %.4f over %d words (%s); %d mismatch run(s); %s" % (wer, len(ref), transcript["engine"], len(mism), "PASS" if passed else "FAIL"))
    print(json.dumps({"wer": qa["wer"], "pass": passed, "mismatches": len(mism), "out": str(out)}))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
