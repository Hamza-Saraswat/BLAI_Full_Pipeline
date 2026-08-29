# Stage 06: Voice

Synthesize the narration with the creator's cloned voice, check it against the script, and produce word timings. Mechanical: the build agent runs this stage from `build/stage_runner.py`.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../04-script/output/[slug]-storyboard.json` | `narration_full` and scene narration | The text to speak |
| Skill | `../../../../skills/elevenlabs-narration/SKILL.md` | Full file | Commands and settings |
| Skill rule | `../../../../skills/elevenlabs-narration/rules/qa-loop.md` | Full file | What to do when the transcript disagrees with the script |
| Skill data | `../../../../skills/elevenlabs-narration/pronunciation_dictionary.json` | Full file | Aliases applied before synthesis |
| Engine | `../../../../build/.env.example` | Whether `ELEVENLABS_API_KEY` and `ELEVEN_VOICE_ID` are set in the runtime env it templates, never the values | `--engine auto` takes ElevenLabs when both are set, else the local engine; a local test run passes `--engine kokoro` and needs no key |
| Skill | `../../../../skills/script-gates/SKILL.md` | "normalize_narration.py" | Safety net for digits and acronyms |
| Reference | `references/voice-note-format.md` | Full file | Layout of the voice note |

## Process

1. Confirm `build/.env` holds `ELEVENLABS_API_KEY` and `ELEVEN_VOICE_ID`; the build dir for this slug is `[build-dir]/[slug]/voice/`. On a local test run neither is set: pass `--engine kokoro`, expect the free local voice, and expect `[build-dir]` to be `<repo>/.local-builds` (`build/README.md`, "Local test run on a Mac").
2. Run `normalize_narration.py` on the storyboard narration; every token it had to expand is a script bug to list in the note.
3. Run `generate_audio.py --storyboard [storyboard] --out [build-dir]/[slug]/voice --format short`, adding `--engine kokoro` on a local run. Record `voice.json`'s `engine` and `alignment_source` in the note: the two engines speak at different rates, so the duration check below is only meaningful against the engine that produced the audio.
4. Run `qa_transcribe.py --audio [build-dir]/[slug]/voice/narration.wav --script [narration.txt] --out [build-dir]/[slug]/voice`. If WER is above 3 %, add dictionary entries for the mispronounced terms and regenerate the failing chunks (at most two rounds).
5. Run `captions.py --alignment [build-dir]/[slug]/voice/alignment.json --script [narration.txt] --out [build-dir]/[slug]/voice`.
6. Run the audit checks below. If any fail, set the hub note to `blocked` with the reason instead of saving.
7. Write `output/[slug]-voice.md` per voice-note-format.md; journal the hub note (`06-voice ok [seconds]s`).

## Audit

| Check | Pass Condition |
|-------|---------------|
| WER | `qa.json` reports wer 0.03 or lower (a local run warns and journals instead of blocking: the small local Whisper model sets that floor by itself) |
| Duration | narration duration within the format's `vo_band_s` in `skills/script-gates/formats.json` |
| Files | `narration.wav`, `alignment.json`, `captions.json`, `captions.srt` exist |
| Expansions | every normalizer expansion is listed in the note |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Voice note | `output/[slug]-voice.md` | duration, chars, chunks, WER, mismatches, expansions |
| Audio and timings | `[build-dir]/[slug]/voice/` | narration.wav, alignment.json, captions.json, captions.srt (never committed) |

The pronunciation dictionary and the storyboard narration are the edit surfaces. Fix a term there and re-run the stage; the render stage reads the files in the build dir.
