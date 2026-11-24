# Voice: 2026-11-24-nariq-a-27b-at-3-bits-in-10-gb

Stage 06-voice on gn100-83c4 at 2026-11-24T13:43:42Z. Audio lives in `$BLAI_BUILD_DIR/2026-11-24-nariq-a-27b-at-3-bits-in-10-gb/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 128.2 s |
| Words per second | 2.965 |
| Characters | 2253 |
| Chunks | 4 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.035 (threshold 0.03) |
| QA | pass |

## Mismatches
- at 25.1 s: expected "here is", heard "here's"
- at 30.2 s: expected "point eight", heard "hundred"
- at 30.8 s: expected "b", heard "beat"
- at 36.9 s: expected "point one two", heard "twelve"
- at 45.3 s: expected "point", heard ""
- at 61.7 s: expected "point", heard ""
- at 89.5 s: expected "stock llama", heard "stocklama"
- at 92.7 s: expected "ollama", heard "olahma"
- at 97.9 s: expected "quants", heard "wants"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
