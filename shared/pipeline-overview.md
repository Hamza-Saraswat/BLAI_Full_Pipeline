# Pipeline Overview

## Hosts

| Host | Runs | Writes |
|------|------|--------|
| Cloud routine (claude.ai/code) | Shorts stages 01-05; long-form stages 01-07 | markdown and JSON outputs, hub notes; pushes `main` |
| DGX Spark build agent (`build/`) | Shorts stages 06-08; long-form stages 08-11 | `-voice.md`, `-render.md`, `-capture.md`, `-publish.md`; hub note status; pushes `main` |
| Telegram bot (on the Spark) | the human gate | hub note `status`, `feedback`; fires the re-script API trigger |
| You, in Obsidian or the GitHub app | edits to any note; Layer 3 changes | whatever you edit; pulled by the next run |

## Status machine

| Status | Set by | Next |
|--------|--------|------|
| `idea` | stage 02 (cloud) | 03 |
| `researched` | stage 03 (cloud) | 04 |
| `scripted` | stage 04 (Shorts) or 06 (long-form) (cloud) | package |
| `ready-to-build` | package stage (cloud) | Spark picks it up within 5 min |
| `building` | `build/build.py` | render stages |
| `review` | render stage after the Telegram card is sent | your tap |
| `approved` | Telegram bot | publish stage |
| `rejected` | Telegram bot (with `feedback`) | nothing, or a re-script run |
| `scheduled` | publish stage after Blotato returns 201 | status poll |
| `published` | publish stage when Blotato reports published | retro |
| `blocked` | any Spark stage after retries (`blocked_reason`) | you, or a re-run |

## Source of truth

| Artifact | Wins over | Regeneration rule |
|----------|-----------|-------------------|
| Measured numbers in `-capture.md` | numbers in the brief and the script | the reconcile step rewrites narration lines that cite them; beyond tolerance it blocks for re-script |
| The script file in `output/` | the storyboard JSON | regenerate the JSON from the script, never the reverse |
| Generated audio + timestamps | every caption, scene duration and sync point | regenerating audio recomputes all of them |
| The package note | what gets uploaded | the manifest is generated from the note at publish time |

## When to loop back

| Symptom | Go to |
|---------|-------|
| A claim is wrong or unsupported | research stage (03), then every stage after it |
| The script reads wrong, sounds off, or repeats last week's shape | script stage (04 Shorts / 05 long-form) |
| A scene lands off-cue or a number on screen is not spoken | render stage, checking the storyboard or spec first |
| Audio mispronounces a term | `skills/elevenlabs-narration/pronunciation_dictionary.json`, then the voice stage |
| The title or description failed the rubric | package stage |
| The same edit three runs in a row | the reference file or contract that produced it (ICM 8.6) |
