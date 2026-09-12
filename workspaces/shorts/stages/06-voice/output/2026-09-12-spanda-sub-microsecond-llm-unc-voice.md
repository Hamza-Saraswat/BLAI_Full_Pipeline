# Voice: 2026-09-12-spanda-sub-microsecond-llm-unc

Stage 06-voice on gn100-83c4 at 2026-09-12T13:36:19Z. Audio lives in `$BLAI_BUILD_DIR/2026-09-12-spanda-sub-microsecond-llm-unc/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 48.3 s |
| Words per second | 2.69 |
| Characters | 845 |
| Chunks | 2 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.075 (threshold 0.03) |
| QA | pass |

## Mismatches
- at 4.5 s: expected "ohlah ma", heard "ola hma"
- at 8.4 s: expected "calm", heard "comm"
- at 21.3 s: expected "meanings", heard "meetings"
- at 21.8 s: expected "a", heard "the"
- at 24.4 s: expected "thousand", heard ""
- at 31.9 s: expected "ohlah ma", heard "ola hma"
- at 33.2 s: expected "point nine", heard "ninety"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
