# Validation Report (ICM build stage 5), 2026-08-22

Checks from `research/ICM-BUILD-GUIDE.md` section 6.5, run on both workspaces after all skills were in place.

| # | Check | Shorts | Long-form | Notes |
|---|-------|--------|-----------|-------|
| 1 | Cross-reference integrity (Inputs paths resolve) | pass | pass | `tools/validate.py` rule "Inputs-table paths resolve"; build-dir paths use `[build-dir]` and are resolved at run time |
| 2 | No circular dependencies | pass | pass | rule "Stage cross-references are one-way"; later stages are never named in earlier stage files |
| 3 | Placeholder coverage | pass | pass | the workspaces ship configured; questionnaires edit values in place; no `{{` tokens |
| 4 | Conditional sections | pass | pass | none used |
| 5 | Stage handoff chain | pass | pass | every stage output is named in the next stage's Inputs (see `_design/stage-contracts.md`) |
| 6 | CONTEXT.md purity | pass | pass | contracts hold only title, sentence, Inputs, Process, Checkpoints, Audit, Verify, Outputs, closing sentence |
| 7 | Checkpoints in creative stages | pass | pass | ideas, research, script, package, outline, spec; unattended mode resolves them into Decisions blocks (documented deviation) |
| 8 | Audits in creative and build stages | pass | pass | every stage has an Audit table; render stages also carry a Verify table |
| 9 | Spec stage purity | n/a | pass | `stages/06-spec/references/spec-format.md` forbids component names, frames, pixels |
| 10 | Line counts | pass | pass | CONTEXT.md 40-59 lines; reference files under 120 lines |
| 11 | Naming | pass | pass | lowercase-with-hyphens, zero-padded stages, `.gitkeep` in empty folders |
| 12 | Tool prerequisites | pass | pass | `skills/*/setup.md` and `build/install.sh`; `shared/env-template.md` for paid APIs; `.gitignore` covers `.env` |
| 13 | Quality scan | pass | pass | no em dashes in authored files (ported and vendored files are exempt) |
| 14 | Mechanical check | 17/17 | 17/17 | `python3 tools/validate.py workspaces/<ws> --allow-outputs` |

Extra checks: `tools/check_outputs.py` 0 failures; `python3 -m compileall tools build skills` clean; `.github/workflows/validate.yml` runs the same three on every push.

## Integration runs (macOS, dry-run or fixtures)

- Shorts stages 01-02 commands as written in the contracts: radar dry-run (47 items after dedupe, 7 cross-source merges), autocomplete/competition/opportunity scoring, two hub notes via `new-run.py`, FYI and gate cards rendered by `send_card.py --dry-run`.
- Render-shorts: Remotion smoke render, full 1080x1920 assemble with loudness, safe-zone and loop gates passing.
- Render-longform: draft render of the 14-scene fixture, three thumbnails, `chapters.json`, lint on a 1080p synthetic clip.
- Narration, publish, Telegram bot: every script in dry-run against fixtures; `publish.py --chapters` replaces estimated chapter lines with measured ones.
- Build agent: `build.py --dry-run --once` prints the full stage plan for both workspaces; `install.sh --dry-run` clean.

## Not verified (needs the Spark or credentials)

`install.sh` on Ubuntu arm64, systemd user units, unattended `claude -p`, ElevenLabs, Blotato, R2, Telegram, YouTube Data API and FireCrawl live calls, the vidIQ connector, the first end-to-end run of each routine. Tracked in `_design/github-issues.md`.

## Deviations from the base conventions (recorded in each workspace CLAUDE.md)

Committed text outputs; unattended checkpoints; per-video hub note as the progress file; machine-checked audit rows; Verify sections; two execution hosts; an `input/` folder in the long-form workspace.
