# Voice bake-off, 2026-08 (Phase 4 of the shorts-only rebuild)

Goal: a cheaper way to run the creator's cloned voice than an ElevenLabs subscription, or a
better local model than Kokoro (which cannot clone at all). Decision gate: the creator's
listening test against their own 1-3 minute recording.

## License gate (checked 2026-08-29, primary sources)

| Candidate | Code | Weights | Commercial | Verdict |
|---|---|---|---|---|
| Chatterbox (Resemble AI) | MIT | MIT | yes | **QUALIFIED -- front-runner.** Zero-shot from a reference clip; MPS supported; ships a watermarker |
| OpenVoice V2 (MyShell) | MIT | MIT | "free for both commercial and research use" | QUALIFIED |
| Fish Speech / OpenAudio | FISH AUDIO RESEARCH LICENSE | same | unclear at best | **DISQUALIFIED** for a monetized channel |
| XTTS-v2 (Coqui) | -- | CPML | no (non-commercial) | DISQUALIFIED (expected; company defunct) |
| F5-TTS | MIT code | CC-BY-NC weights | no | DISQUALIFIED (expected) |

## Runs on this Mac (M2, 16 GB, macOS)

- **Chatterbox**: installed in a scratch venv (`chatterbox-tts` + torch, Python 3.11).
  Two install traps for the integration note: uv venvs ship no setuptools, and
  `resemble-perth` needs `pkg_resources`, which setuptools >= 81 removed -- pin
  `setuptools<81`. Model: ~3.0 GB from HF on first run; loads in 23 s on MPS.
  Smoke: COMPLETE. Both samples transcribe at **WER 0.0** (whisper base.en, zero mismatches),
  cleaner than Kokoro's 0.015-0.031 on the same checker.
  - `cbx_default` (stock voice): 9.32 s from the 40-word test line.
  - `cbx_cloned` (cloned from the stand-in reference): 11.80 s -> ~3.4 wps.
  - MPS caveats, both worked around: torchaudio's sinc resampler and the HiFiGAN vocoder each
    hit "Output channels > 65536 not supported at the MPS device" on the CLONED path only.
    The default path renders on MPS; the cloned path runs on CPU (RTF ~6.6x -- a 38 s Short
    would take ~4 min, fine for an unattended overnight build, and a non-issue on the Spark's
    CUDA). Listening set delivered to the creator 2026-08-29.
- **OpenVoice V2**: install ABORTED -- its own torch copy hit `No space left on device`
  on this 8.7-GB-free disk. Qualified on license; revisit on the Spark (3.1 TB free)
  only if Chatterbox fails the listening test.

## The money frame

Shorts-only volume is ~65k chars/month (measured). ElevenLabs Creator ($22/mo, 121k
credits, PVC) fits the budget and stays the documented fallback; it is a subscription
forever and the clone stops working if it lapses. A local clone is $0/month and on-brand
for the channel; the cost is quality risk, which the listening test decides.

## Pending

1. The creator's 1-3 minute clean recording (the one input only they can provide).
2. Chatterbox smoke numbers (RTF on MPS, WER via qa_transcribe) -- run in progress.
3. Listening test: creator's clone (Chatterbox) vs Kokoro vs [ElevenLabs fallback decision].
4. If Chatterbox wins: wire as third `--engine` in generate_audio.py (contract unchanged),
   measure its wps into voice.config.json `voices_wps`.
