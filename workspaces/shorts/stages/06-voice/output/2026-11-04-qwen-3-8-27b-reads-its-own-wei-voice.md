# Voice: 2026-11-04-qwen-3-8-27b-reads-its-own-wei

Stage 06-voice on gn100-83c4 at 2026-11-04T13:20:38Z. Audio lives in `$BLAI_BUILD_DIR/2026-11-04-qwen-3-8-27b-reads-its-own-wei/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 34.0 s |
| Words per second | 3.143 |
| Characters | 657 |
| Chunks | 2 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.045 (threshold 0.03) |
| QA | FAIL |

## Mismatches
- at 3.8 s: expected "thousand", heard "zero"
- at 5.7 s: expected "thousand", heard ""
- at 30.7 s: expected "rikiyat's", heard "ricky ateez's"
- at 32.5 s: expected "can", heard "should"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
