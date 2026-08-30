---
slug: 2026-08-30-dgx-spark-has-128-gb-and-a-70b
duration_s: 109.16
chars: 2147
chunks: 4
wer: 0.0787
model: chatterbox
---

# Voice: 2026-08-30-dgx-spark-has-128-gb-and-a-70b

## Timing

| Scene | Starts at | Ends at | Seconds |
|-------|-----------|---------|---------|
| s1 | 0.00 | 8.02 | 8.02 |
| s2 | 8.02 | 18.48 | 10.46 |
| s3 | 18.48 | 26.07 | 7.59 |
| s4 | 26.07 | 40.20 | 14.13 |
| s5 | 40.20 | 52.03 | 11.83 |
| s6 | 52.03 | 66.61 | 14.58 |
| s7 | 66.61 | 84.45 | 17.84 |
| s8 | 84.45 | 100.08 | 15.63 |
| s9 | 100.08 | 110.16 | 10.08 |

## QA

- WER: 0.0787 (threshold 0.03) -- WARNING, not blocked: this is a local run (chatterbox stock voice, ggml-base.en local Whisper), and the stage contract journals the small local Whisper model's own error floor instead of blocking on it.
- Mismatches: 13 runs, all small-model noise on a synthetic voice: "re reads" heard as "rereads" (x4, hyphenation), single function-word swaps ("a"->"one", "at"->"to", "wakes"->"weights", "doorway's width"->"doorways with"), "gptoss"->"gpt oss" (spacing), two whisper insertions ("hundred", "one"), one merged segment at "Why the gap." No truncation, no dropped sentence, every spoken number present in the transcript.
- Alignment: whisper.cpp (ggml-base.en), 360 words heard, 373 script words timed. First pass was proportional; alignment was rebuilt from the same chunk wavs via the reuse path (`--only-chunks 99`), audio unchanged.

## Normalizer expansions

- none: scenes_changed 0 on the winning storyboard.

## Rounds

1. generated 1 chunk, 40.0 s -- REJECTED: chatterbox truncated the 2147-char single pass at exactly 40.0 s (words_per_second 9.325, physically impossible). Root cause: generate_audio.py's chunk limit was keyed on the ElevenLabs model id, so chatterbox never tripped the "chunking anyway" path. Fixed in skills/elevenlabs-narration/scripts/generate_audio.py (MODEL_LIMITS["chatterbox"]=600, engine-aware limit resolved before chunking).
2. generated 4 chunks (563/581/600/400 chars), 109.16 s, 3.417 wps, QA warned as above; captions 97 cues.
