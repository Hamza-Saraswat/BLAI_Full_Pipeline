# Voice: 2026-09-09-vllm-0-29-sizes-its-own-kv-cac

Stage 06-voice on gn100-83c4 at 2026-09-09T13:36:23Z. Audio lives in `$BLAI_BUILD_DIR/2026-09-09-vllm-0-29-sizes-its-own-kv-cac/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 39.4 s |
| Words per second | 2.89 |
| Characters | 687 |
| Chunks | 2 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.035 (threshold 0.03) |
| QA | pass |

## Mismatches
- at 1.2 s: expected "stopped", heard "stop"
- at 9.9 s: expected "weights eat", heard "waitseat"
- at 19.9 s: expected "returned", heard "returns"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
