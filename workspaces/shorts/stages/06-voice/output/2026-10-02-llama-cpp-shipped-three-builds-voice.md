# Voice: 2026-10-02-llama-cpp-shipped-three-builds

Stage 06-voice on gn100-83c4 at 2026-10-02T12:30:49Z. Audio lives in `$BLAI_BUILD_DIR/2026-10-02-llama-cpp-shipped-three-builds/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 44.3 s |
| Words per second | 2.82 |
| Characters | 781 |
| Chunks | 2 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.047 (threshold 0.03) |
| QA | pass |

## Mismatches
- at 0.0 s: expected "rebuild", heard "rebuilt"
- at 1.3 s: expected "tagged", heard "tag"
- at 15.4 s: expected "", heard "hundred"
- at 16.1 s: expected "bus", heard "bust"
- at 28.3 s: expected "a pinned", heard "append"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
