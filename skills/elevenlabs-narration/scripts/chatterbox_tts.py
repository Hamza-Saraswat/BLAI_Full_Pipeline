#!/usr/bin/env python3
"""One Chatterbox chunk, run INSIDE the Chatterbox venv (not the system python).

    <cbx-venv>/bin/python chatterbox_tts.py --script-file chunk.txt --out chunk.wav
                                            [--ref voice.wav] [--device auto|cuda|mps|cpu]

Zero-shot voice clone when --ref is given (the creator's recording); the model's stock
voice otherwise (the documented stand-in until a recording exists). Output is a mono wav
at the model's native 24 kHz; generate_audio.py resamples to the 44.1 kHz contract.
Prints one JSON line: {"duration_s", "device", "cloned", "sample_rate"}.

Portability guards, both hit in real runs (finding 68 and the 2026-08-29 bake-off):
- MPS: torchaudio's sinc resampler and parts of the vocoder trip conv1d channel limits on
  the CLONED path; reference resampling is routed through CPU, and if generation still
  fails on MPS the whole run retries on CPU rather than dying.
- The model loads once per process; generate_audio.py calls this per chunk, which is fine
  for Shorts (one chunk) and acceptable for multi-chunk runs.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--script-file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ref", default="", help="reference wav to clone; empty = stock voice")
    ap.add_argument("--device", default="auto", choices=["auto", "cuda", "mps", "cpu"])
    a = ap.parse_args()

    import os

    # A Docker vLLM often leaves ~/.cache/huggingface root-owned; fall back to a
    # user-owned cache instead of dying on PermissionError (Spark, 2026-08-29).
    if "HF_HOME" not in os.environ:
        default_hub = pathlib.Path.home() / ".cache" / "huggingface"
        if default_hub.exists() and not os.access(default_hub, os.W_OK):
            os.environ["HF_HOME"] = str(pathlib.Path.home() / "blai" / "voice" / "hf-cache")

    import torch

    if a.device != "auto":
        dev = a.device
    elif torch.cuda.is_available():
        dev = "cuda"
    elif torch.backends.mps.is_available():
        dev = "mps"
    else:
        dev = "cpu"

    # MPS: route reference resampling through CPU (conv1d channel limit).
    if dev == "mps":
        import chatterbox.models.s3gen.s3gen as _s3g
        _orig = _s3g.get_resampler

        def _cpu_resampler(sr_in, sr_out, device):
            r = _orig(sr_in, sr_out, "cpu")
            return lambda w: r(w.detach().to("cpu")).to(device)

        _s3g.get_resampler = _cpu_resampler

    from chatterbox.tts import ChatterboxTTS

    text = pathlib.Path(a.script_file).read_text(encoding="utf-8").strip()
    ref = a.ref.strip()

    def synth(device: str):
        model = ChatterboxTTS.from_pretrained(device=device)
        kwargs = {"audio_prompt_path": ref} if ref else {}
        return model, model.generate(text, **kwargs)

    try:
        model, wav = synth(dev)
    except (NotImplementedError, RuntimeError) as e:
        if dev == "mps":
            print("chatterbox: mps failed (%s); retrying on cpu" % e, file=sys.stderr)
            dev = "cpu"
            model, wav = synth(dev)
        else:
            raise

    # soundfile, not torchaudio.save: torchaudio 2.11+ delegates save to the separate
    # torchcodec package and ImportErrors without it (hit live on the Spark, 2026-08-29).
    import soundfile as sf

    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out), wav.squeeze(0).cpu().numpy(), model.sr)
    print(json.dumps({"duration_s": round(wav.shape[-1] / model.sr, 3), "device": dev,
                      "cloned": bool(ref), "sample_rate": model.sr}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
