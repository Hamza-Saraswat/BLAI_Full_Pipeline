# Voice: 2026-11-15-8x-v100-runs-80-of-deepseek-v4

Stage 06-voice on gn100-83c4 at 2026-11-15T13:23:10Z. Audio lives in `$BLAI_BUILD_DIR/2026-11-15-8x-v100-runs-80-of-deepseek-v4/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 97.2 s |
| Words per second | 3.157 |
| Characters | 1717 |
| Chunks | 3 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.019 (threshold 0.03) |
| QA | pass |

## Mismatches
- at 4.4 s: expected "point", heard ""
- at 10.1 s: expected "lawyer's", heard "lawyer"
- at 49.5 s: expected "four", heard "for"
- at 58.3 s: expected "picked", heard "pick"
- at 82.9 s: expected "", heard "hundred"
- at 95.6 s: expected "in", heard "and"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
