# Voice: 2026-10-29-deepseek-v4-1-flash-kv-cache-c

Stage 06-voice on gn100-83c4 at 2026-10-29T12:23:09Z. Audio lives in `$BLAI_BUILD_DIR/2026-10-29-deepseek-v4-1-flash-kv-cache-c/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 37.4 s |
| Words per second | 2.998 |
| Characters | 684 |
| Chunks | 2 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.077 (threshold 0.03) |
| QA | pass |

## Mismatches
- at 3.1 s: expected "cache", heard "cash"
- at 9.4 s: expected "cache", heard "cash"
- at 18.9 s: expected "pertoken cache", heard "per token cash"
- at 25.0 s: expected "cpp's cache", heard "cpps cash"
- at 31.0 s: expected "cache", heard "cash"
- at 35.3 s: expected "cache", heard "cash"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
