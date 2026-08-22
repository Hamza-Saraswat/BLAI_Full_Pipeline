---
name: script-gates
description: Machine gates for Shorts scripts. Validates a storyboard against the format bands (blockers and advisories), scores whether the storyboard spent the research brief's specifics (seven gates), and normalizes narration into spoken form for the voice engine. Run after every storyboard write and before voice.
metadata:
  tags: "shorts, storyboard, validation, eval, tts, narration"
---

# script-gates

Port of the v1 pipeline's proven gates. Three stdlib-only Python scripts plus the data files they read. Nothing here writes a script; the gates say what is wrong and the script stage fixes it.

## When to Use

- Stage 04 (script) of `workspaces/shorts`, right after the storyboard JSON is regenerated from the script file, and again after every fix.
- Stage 06 (voice), to produce the spoken-form narration the voice engine reads.
- Any re-script run triggered from Telegram (`rescript:<slug>`).
- Not for long-form: the bands are Shorts physics. Long-form uses `skills/render-longform/scripts/lint_longform.py`; the number and term rules still apply to long-form narration and `normalize_narration.py --text` works on any string.

## What You Need Before Calling

- `<slug>-storyboard.json` conforming to `shared/schemas/storyboard.schema.json`. The script file wins over the JSON: regenerate the JSON from the script, never the reverse (`shared/pipeline-overview.md`).
- `<slug>-brief.json` from stage 03 (for `eval_short.py`; without it the spend gates read as not applicable, not failed).
- This folder's data files: `formats.json` (bands), `tts_lexicon.json` (say / keep / units), `voice.config.json` (`wps`, words per second of the pinned voice). `skills/render-shorts/styles/history.json` is optional: when it is missing the validator reports "no history" as an advisory and continues.
- Python 3.9 or newer, no packages.

## How It Works

All paths below are relative to the repo root. Every script has `--help`.

1. **Validate the storyboard.** Physics only: hook first, payoff_close last, bands from `formats.json`, concat rule (scene narrations joined by single spaces must equal `narration_full`), spoken-number checks, lexicon coverage, style-pack rotation. Prints one JSON object with `blockers`, `advisories`, `warnings`. Exit 0 clean, 1 blockers, 3 advisories only.

   ```
   python3 skills/script-gates/scripts/validate_storyboard.py \
     workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-storyboard.json
   ```

   `--history FILE` points the rotation check elsewhere (tests use `skills/script-gates/fixtures/history.json`). `script_format` absent means classic; an unknown value degrades to classic with an advisory; `structure` is free text and never rejected.

2. **Score the spend.** Did the storyboard use what the research found? Reads the brief JSON and the storyboard, runs the validator itself, writes an eval JSON and prints `overall` (`gate1_ready`, `failures`, `detail`). Exit 0 when the gates pass, 4 when any fails, 2 on usage errors. The seven gates and which are soft: `rules/eval-gates.md`.

   ```
   python3 skills/script-gates/scripts/eval_short.py \
     --storyboard workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-storyboard.json \
     --research   workspaces/shorts/stages/03-research/output/2026-08-25-deepseek-v4-flash-128gb-brief.json \
     --out        workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-eval.json
   ```

   `--label NAME` names the run; `--history FILE` is passed through to the validator; `--report [--out FILE]` renders every eval JSON it finds (`out/*/eval.json` and `workspaces/*/stages/*/output/*eval.json`) into one HTML page. The bare `<slug>` form expects a v1-style `out/<slug>/` tree under `--root` and is kept for v1 checkouts only.

3. **Normalize narration for the voice engine.** Deterministic safety net: expands digits, money, units, model tokens and ALL-CAPS runs into spoken words using `tts_lexicon.json`, idempotently. Never edits the storyboard. Writes the text the voice stage reads plus a per-scene sidecar for caption alignment.

   ```
   python3 skills/script-gates/scripts/normalize_narration.py \
     --storyboard workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-storyboard.json \
     --out-txt    workspaces/shorts/stages/06-voice/output/2026-08-25-deepseek-v4-flash-128gb-narration.txt \
     --out-json   workspaces/shorts/stages/06-voice/output/2026-08-25-deepseek-v4-flash-128gb-narration.norm.json
   ```

   Ad hoc: `--text "A 27B model on an RTX 4090."` prints the spoken form; `--stdin` reads a stream; `--lexicon FILE` swaps the table; `--self-test` runs the leak corpus and must pass after every lexicon edit.

4. **Loop until clean.** Blockers: fix the script, regenerate the JSON, validate again. Advisories: fix them, or record the reason for keeping the line in the hub note `## Decisions`. Gate failures: the eval JSON lists the material left on the table (`board_metrics.number_spend.detail[].spent == false`, `entity_spend.missing`); feed that list to the rewrite.

## Data Files

- `formats.json`: the `classic` and `smooth-explainer` bands (unchanged from v1) plus the informational `structures` list. Single source of truth for both scripts; edit numbers here only, in lockstep with the baseline diffs.
- `tts_lexicon.json`: `say` (token to spoken form), `keep` (tokens the engine already says right), `units` (numeric suffix to unit name). Producer-editable; values may contain no digits and no un-kept ALL-CAPS runs.
- `voice.config.json`: the pinned voice and its `wps`. 2.9 is a provisional estimate for the ElevenLabs professional clone; re-measure after the first three renders (audio seconds divided by narration words) and update the value, or the pacing advisories drift.
- `fixtures/history.json`: empty style-pack history for tests. The live file is `skills/render-shorts/styles/history.json`, appended by `style_rotation.py --record`.

## Rules

- `rules/format-bands.md`: what every knob in the classic and smooth-explainer bands means, how the validator applies it, and why `structure` is independent of the band.
- `rules/number-and-term-rules.md`: spoken numbers, acronyms and product names, on-screen versus narration, the lexicon, and exactly what the validator and normalizer check.
- `rules/eval-gates.md`: the seven `eval_short.py` gates one line each, per-format differences, and which gates are soft (entity_spend, top2).

## After the Call

- Record one line per tool in the hub note `## Decisions`: validator blockers and advisories count, eval gates passed or failed with the failure names, normalizer `scenes_changed`.
- A board that still has blockers never moves to `scripted`. Soft-gate failures move on only with a written reason.
- Keep the normalized text next to the storyboard; the voice stage reads the `.txt`, the caption step reads the `.norm.json`.
- After a lexicon edit, run `--self-test` and re-run the validator on the current board: an acronym advisory disappears only when the lexicon knows the token.
- After the first three voice renders, update `wps` in `voice.config.json`.
