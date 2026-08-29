---
name: script-gates
description: Machine gates for Shorts scripts. Validates a storyboard against the format bands (blockers and advisories), scores whether the storyboard spent the research brief's specifics and avoided the stage-label template (nine gates), keeps a variety ledger so two videos cannot feel like the same video, and normalizes narration into spoken form for the voice engine. Run after every storyboard write and before voice.
metadata:
  tags: "shorts, storyboard, validation, eval, variety, tts, narration"
---

# script-gates

Port of the v1 pipeline's proven gates, plus the two gates v1 lacked. Four stdlib-only Python scripts, a regression test and the data files they read. Nothing here writes a script; the gates say what is wrong and the script stage fixes it. Every script takes `--help` and `--dry-run`.

## When to Use

- Stage 04 (script) of `workspaces/shorts`, right after the storyboard JSON is regenerated from the script file, and again after every fix.
- Stage 06 (voice), to produce the spoken-form narration the voice engine reads.
- Any re-script run triggered from Telegram (`rescript:<slug>`).

## What You Need Before Calling

- `<slug>-storyboard.json` conforming to `shared/schemas/storyboard.schema.json`. The script file wins over the JSON: regenerate the JSON from the script, never the reverse (`shared/pipeline-overview.md`).
- `<slug>-brief.json` from stage 03 (for `eval_short.py`; without it the spend gates read as not applicable, not failed).
- `output/script-ledger.json` for the variety gate. Without it `sameness` does not run at all and the eval JSON says so; it is not a pass.
- This folder's data files: `formats.json` (bands **and** every gate threshold), `tts_lexicon.json` (say / keep / units), `voice.config.json` (`wps_by_format`, then `wps`, words per second of the pinned voice). `skills/render-shorts/styles/history.json` is optional: when it is missing the validator reports "no history" as an advisory and continues.
- Python 3.9 or newer, no packages.

## How It Works

All paths below are relative to the repo root. Every script has `--help`.

1. **Validate the storyboard.** Physics only: hook first, payoff_close last, bands from `formats.json`, concat rule (scene narrations joined by single spaces must equal `narration_full`), spoken-number checks, lexicon coverage, style-pack rotation, plus the voice advisories (over-use of "we / our", no "you" in the first three sentences), the `ending` tail budget and `narration_max_chars`. Prints one JSON object with `blockers`, `advisories`, `warnings`. Exit 0 clean, 1 blockers, 3 advisories only.

   ```
   python3 skills/script-gates/scripts/validate_storyboard.py \
     workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-storyboard.json
   ```

   `--history FILE` points the rotation check elsewhere (tests use `skills/script-gates/fixtures/history.json`). `script_format` absent means classic; an unknown value degrades to classic with an advisory; `structure` is free text and never rejected.

2. **Score the spend, the labels and the sameness.** Did the storyboard use what the research found, does it navigate by content rather than "stage one, stage two", and does it differ from the last five? Reads the brief JSON, the storyboard and (optionally) the ledger, runs the validator itself, writes an eval JSON and prints `overall` (`gate1_ready`, `failures`, `detail`). Exit 0 when the gates pass, 4 when any fails, 2 on usage errors. The nine gates and which are soft: `rules/eval-gates.md`.

   ```
   python3 skills/script-gates/scripts/eval_short.py \
     --storyboard workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-storyboard.json \
     --research   workspaces/shorts/stages/03-research/output/2026-08-25-deepseek-v4-flash-128gb-brief.json \
     --ledger     workspaces/shorts/output/script-ledger.json \
     --out        workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-eval.json
   ```

   `--label NAME` names the run; `--history FILE` is passed through to the validator; `--ledger FILE` turns the `sameness` gate on (omit it and the gate does not run, which the eval JSON records); `--dry-run` scores and prints but writes nothing; `--report [--out FILE]` renders every eval JSON it finds (`out/*/eval.json` and `workspaces/*/stages/*/output/*eval.json`) into one HTML page. The bare `<slug>` form expects a v1-style `out/<slug>/` tree under `--root` and is kept for v1 checkouts only.

3. **Check and record variety.** The ledger of what shipped and the rules that stop today's Short repeating the last five: shape, hook pattern, closing move, duration, sentence-opener rhythm, plus an advisory on any repeated 8-word phrase. `check` prints `{ok, violations, advisories, comparisons}` and exits 0 or 1; `record` appends the entry once the script is final; `entry` prints the row and writes nothing. Full rules: `rules/variety.md`.

   ```
   python3 skills/script-gates/scripts/variety_check.py check \
     --storyboard workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-storyboard.json \
     --ledger     workspaces/shorts/output/script-ledger.json

   python3 skills/script-gates/scripts/variety_check.py record \
     --storyboard <same> --ledger workspaces/shorts/output/script-ledger.json --date 2026-08-25
   ```

   `--window N` widens the hard-rule lookback (default 5); `--slug NAME` overrides the storyboard's own slug; `--dry-run` computes everything and writes nothing. `eval_short.py` imports this file to run the same rules as its `sameness` gate.

4. **Normalize narration for the voice engine.** Deterministic safety net: expands digits, money, units, model tokens and ALL-CAPS runs into spoken words using `tts_lexicon.json`, idempotently. Never edits the storyboard. Writes the text the voice stage reads plus a per-scene sidecar for caption alignment.

   ```
   python3 skills/script-gates/scripts/normalize_narration.py \
     --storyboard workspaces/shorts/stages/04-script/output/2026-08-25-deepseek-v4-flash-128gb-storyboard.json \
     --out-txt    workspaces/shorts/stages/06-voice/output/2026-08-25-deepseek-v4-flash-128gb-narration.txt \
     --out-json   workspaces/shorts/stages/06-voice/output/2026-08-25-deepseek-v4-flash-128gb-narration.norm.json
   ```

   Ad hoc: `--text "A 27B model on an RTX 4090."` prints the spoken form; `--stdin` reads a stream; `--lexicon FILE` swaps the table; `--dry-run` normalizes and reports but writes no files; `--self-test` runs the leak corpus and must pass after every lexicon edit.

5. **Loop until clean.** Blockers: fix the script, regenerate the JSON, validate again. Advisories: fix them, or record the reason for keeping the line in the hub note `## Decisions`. Gate failures: the eval JSON lists the material left on the table (`board_metrics.number_spend.detail[].spent == false`, `entity_spend.missing`), the offending label sentences (`positional_labels.offenders`) and the ledger entries this script clashes with (`sameness.violations[]`); feed that list to the rewrite.

6. **Regression-test a threshold change.** `tests/corpus_regression.py` runs every gate over the 38-board v1 corpus, prints a per-board table and asserts the calibration: `positional_labels` fails exactly the ten label boards and passes the two clean smooth ones, `sameness` fires on the 113-second pin and the duplicate board pair, the four shipped boards pass `skeleton` and `number_spend`, no board gains a validator blocker against `tests/baseline_validator.json`, and `person: you` activates the "we / our" advisory for classic. Run it after every edit to `formats.json` or a gate.

   ```
   python3 skills/script-gates/tests/corpus_regression.py [--corpus DIR] [--baseline FILE] [-v]
   ```

   `--corpus` points at any directory of `<slug>/storyboard.json` (default: the v1 `BLAI_Animator/out` tree, which is READ-ONLY: the test writes only to a temp directory). `--dry-run` lists the boards it would score. Exit 0 when every assertion holds.

## Data Files

- `formats.json`: the `classic` and `smooth-explainer` bands plus every `eval_short.py` gate threshold (`numbers.min_count` / `max_count`, `scene_specificity.allow_generic`, `skeleton.max_density`, `positional_labels.allowed_structures`, `entity_spend`, `top2`, `validator`) and the informational `structures` list. Single source of truth for both scripts; edit numbers here only, in lockstep with the baseline diffs, then re-run `tests/corpus_regression.py`.
- `tts_lexicon.json`: `say` (token to spoken form), `keep` (tokens the engine already says right), `units` (numeric suffix to unit name). Producer-editable; values may contain no digits and no un-kept ALL-CAPS runs.
- `voice.config.json`: the pinned voice and its rate. Both scripts read `wps_by_format[script_format]` first, then the flat `wps`, then the band's `wps_fallback`. Every shipped value is 2.9 and provisional for the ElevenLabs professional clone; re-measure after the first three renders (audio seconds divided by narration words, per format), write the result into `wps_by_format`, or the pacing advisories drift.
- `fixtures/history.json`: empty style-pack history for tests. The live file is `skills/render-shorts/styles/history.json`, appended by `style_rotation.py --record`.
- `tests/baseline_validator.json`: pre-change validator blocker, advisory and warning counts per corpus board. `corpus_regression.py` diffs against it so a threshold edit cannot quietly break a board that used to pass the physics.
- `output/script-ledger.json` (in the workspace, not here): the variety ledger. See `rules/variety.md`.

## Rules

- `rules/format-bands.md`: what every knob in the classic and smooth-explainer bands means, how the validator applies it, and why `structure` is independent of the band.
- `rules/number-and-term-rules.md`: spoken numbers, acronyms and product names, on-screen versus narration, the lexicon, and exactly what the validator and normalizer check.
- `rules/eval-gates.md`: the nine `eval_short.py` gates one line each, per-format differences, the `positional_labels` rule and its action-verb heuristic, and which gates are soft (entity_spend, top2).
- `rules/variety.md`: the ledger's fields, the hook-pattern classifier, the five `sameness` rules and the repeated-phrase advisory, and how a run proceeds past a failure by writing a Decisions block.

## After the Call

- Record one line per tool in the hub note `## Decisions`: validator blockers and advisories count, eval gates passed or failed with the failure names, `sameness` violations if any, normalizer `scenes_changed`.
- Append the ledger entry (`variety_check.py record`) once the winning script is final, and only then: a recorded entry that never shipped poisons the next five rotations.
- A board that still has blockers never moves to `scripted`. Soft-gate failures move on only with a written reason.
- Keep the normalized text next to the storyboard; the voice stage reads the `.txt`, the caption step reads the `.norm.json`.
- After a lexicon edit, run `--self-test` and re-run the validator on the current board: an acronym advisory disappears only when the lexicon knows the token.
- After the first three voice renders, update `wps_by_format` in `voice.config.json` with the measured per-format rate.
