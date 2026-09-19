# Voice: 2026-09-19-fine-tune-on-amd-unsloth-docke

Stage 06-voice on gn100-83c4 at 2026-09-19T12:46:23Z. Audio lives in `$BLAI_BUILD_DIR/2026-09-19-fine-tune-on-amd-unsloth-docke/voice/` (binaries are never committed).

| Field | Value |
|-------|-------|
| Format | short |
| Engine | chatterbox |
| Duration | 112.2 s |
| Words per second | 2.648 |
| Characters | 1769 |
| Chunks | 4 |
| Model | chatterbox |
| Alignment | whisper |
| Credits estimate | 0 |
| WER | 0.097 (threshold 0.03) |
| QA | FAIL |

## Mismatches
- at 9.3 s: expected "point five finetunes", heard "five fine tunes"
- at 20.0 s: expected "unslothrocm image", heard "unsloth rock mimage"
- at 26.0 s: expected "an", heard "and"
- at 29.2 s: expected "matched", heard "match"
- at 29.8 s: expected "in", heard "and"
- at 48.5 s: expected "docker", heard "dockers"
- at 56.6 s: expected "qlora", heard "q low raw"
- at 58.8 s: expected "compressed", heard "compress"
- at 59.4 s: expected "that is what cuts vram to the floor", heard ""
- at 90.3 s: expected "steam deck's", heard "steamedex"
- at 102.3 s: expected "cudaonly", heard "cu to only"
- at 110.1 s: expected "unslothrocm", heard "unsloth rockum"

## Files

`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, `qa.json`, `voice.json`
