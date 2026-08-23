# Stage 09: Voice

Synthesize the episode narration with the creator's cloned voice, check it against the narration file, and produce word timings. Mechanical: the build agent runs it from `build/stage_runner.py`.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../05-script/output/[slug]-narration.txt` | Full file (as reconciled by the capture stage) | The text to speak |
| Skill | `../../../../skills/elevenlabs-narration/SKILL.md` | Full file | Commands and settings |
| Skill rule | `../../../../skills/elevenlabs-narration/rules/chunking-and-settings.md` | "Long-form" | Paragraph chunks, previous and next text, seed |
| Skill rule | `../../../../skills/elevenlabs-narration/rules/qa-loop.md` | Full file | WER gate and regeneration |
| Skill data | `../../../../skills/elevenlabs-narration/pronunciation_dictionary.json` | Full file | Aliases |
| Engine | `build/.env` (`ELEVENLABS_API_KEY`, `ELEVEN_VOICE_ID`) or the local Kokoro model | Whether they are set, never the values | `--engine auto` takes ElevenLabs when both are set and the local Kokoro engine otherwise; a local test run passes `--engine kokoro` and needs no key |
| Reference | `references/voice-note-format.md` | Full file | Layout of the voice note |

## Process

1. Confirm `build/.env` holds the ElevenLabs key and voice id; strip any `[measured]` marker that survived. On a local test run neither is set: pass `--engine kokoro`, expect the free local voice, and expect `[build-dir]` to be `<repo>/.local-builds` (`build/README.md`, "Local test run on a Mac").
2. Run `generate_audio.py --text [narration.txt] --out [build-dir]/[slug]/voice --format long`, adding `--engine kokoro` on a local run. Record `voice.json`'s `engine` and `alignment_source` in the note: the two engines speak at different rates, so a duration inside the target for one is outside it for the other, and a local episode length proves nothing about the real one.
3. Run `qa_transcribe.py`; above 3 % WER, add dictionary entries and regenerate failing chunks (at most two rounds); listen-check is replaced by a drift check: WER computed per chunk must not rise in the last third.
4. Run `captions.py`.
5. Run the audit checks below. If any fail, set the hub note to `blocked`.
6. Write `output/[slug]-voice.md`; journal the hub note.

## Audit

| Check | Pass Condition |
|-------|---------------|
| WER | overall 0.03 or lower; no chunk above 0.05 (a local run warns and journals instead of blocking: the small local Whisper model sets that floor by itself) |
| Duration | within 10 % of the spec's `target_duration_s` |
| Files | `narration.wav`, `alignment.json`, `captions.json`, `captions.srt` exist |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Voice note | `output/[slug]-voice.md` | duration, chars, chunks, per-chunk WER, mismatches |
| Audio and timings | `[build-dir]/[slug]/voice/` | never committed |

The narration file and the pronunciation dictionary are the edit surfaces; re-run the stage after editing either. The render stage reads the build dir.
