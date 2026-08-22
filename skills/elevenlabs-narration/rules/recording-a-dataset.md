# Recording a PVC dataset

The dataset is the product. A Professional Voice Clone (PVC) trained on 30-60 minutes of clean, consistent narration sounds like the creator; one trained on noisy, mixed-style audio sounds like a worse stock voice. Plan: Creator plan (one PVC slot), trained on this dataset, used with Multilingual v2 for long-form. Source: research section 3.5.

## The seven steps

1. Length and scope. 30 minutes minimum, 60-120 minutes ideal, up to 3 hours useful. One speaker, one style per session. Do not mix a calm explainer read with a punchy Shorts read in the same dataset; if both are wanted, record two datasets and train two clones (one PVC slot on Creator, so the Shorts clone is an Instant Voice Clone from the second dataset).
2. Room and signal chain. Quiet treated room (closet with clothes beats an empty office). XLR condenser into an audio interface, pop filter, about two fists from the mic, consistent gain for the whole session. Target RMS between -23 and -18 dB and a true peak of -3 dB. Check a take with `ffmpeg -i take.wav -af astats -f null -` (read "RMS level" and "Peak level") or `ffmpeg -i take.wav -af ebur128 -f null -` for integrated loudness.
3. Read in the publishing register. The clone replicates the speaking style in the samples. Read real scripts from `workspaces/long-form` at the pace and energy the channel publishes with; the clone will not add energy later.
4. No processing. No music, no reverb, no de-noiser, no compressor or limiter artifacts. Export WAV (or MP3 at 192 kbps or higher). Trim silence only; do not loudness-normalize the dataset.
5. Content coverage. Avoid long pauses, fillers and throat clears (re-take instead of leaving them in). Include numbers (prices, percentages, years, model sizes), acronyms and the channel's recurring product names: read the keys of `pronunciation_dictionary.json` once inside real sentences (DGX Spark, GB10, Qwen, vLLM, llama.cpp, GGUF, KV cache, CUDA, NVIDIA, Unsloth, Ollama, FP8, FP4, RTX 5090, tokens per second).
6. Verification and training. Upload, then complete the voice captcha in the same delivery and the same room; if verification fails, retry after 24 hours. Training takes 3-6 hours, up to 24. PVC trains on Flash v2.5, Turbo v2.5 and Multilingual v2; v3 is not listed for PVC, so treat PVC + v3 as a test, not a plan.
7. Archive the raw WAVs. Keep the unprocessed session files outside the vendor (local disk plus one backup). They are the portable asset: the same recordings train the Cartesia or Inworld hedge clone if ElevenLabs changes terms or pricing.

## Session checklist

- Same mic, same distance, same gain for every take; note the settings in the session folder.
- Water nearby; stop when the voice tires, quality beats minutes.
- Slate nothing. The dataset should contain only narration.
- Before uploading, listen to 2 minutes at random points for mouth noise, clipping and room tone changes.
- Name files `pvc-<date>-<take>.wav` and keep a `README.txt` with the register, mic and date.

## What the pipeline needs after training

- Put the trained voice id in `build/.env` as `ELEVEN_VOICE_ID` (never in a committed file).
- Run `scripts/generate_audio.py --text fixtures/sample-script.txt --out /tmp/pvc-check` and listen to the product names; fix misreads in `pronunciation_dictionary.json` (see `pronunciation.md`), not by re-recording.
- Keep a stock or Voice Design voice id on file as the A/B control for the first 3-5 videos (see `chunking-and-settings.md`).
