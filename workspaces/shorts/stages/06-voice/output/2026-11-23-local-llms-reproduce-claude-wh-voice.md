# Voice: 2026-11-23-local-llms-reproduce-claude-wh

Stage 06-voice on gn100-83c4 at 2026-11-23T13:21:37Z. Audio lives in `$BLAI_BUILD_DIR/2026-11-23-local-llms-reproduce-claude-wh/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 90.2 s |
| Words per second | 3.348 |
| Characters | 1653 |
| Chunks | 3 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.023 (threshold 0.03) |
| QA | pass |

## Mismatches
- at 13.6 s: expected "as", heard "his"
- at 56.2 s: expected "past", heard "passed"
- at 57.9 s: expected "tie", heard "tied"
- at 60.9 s: expected "", heard "tied today's sonnet"
- at 70.6 s: expected "plainer", heard "planer"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
