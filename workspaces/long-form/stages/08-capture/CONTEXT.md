# Stage 08: Capture

Run the episode's experiment plan on the DGX Spark under guardrails, then reconcile the script with what was measured. The build agent runs the capture mechanically and the reconcile step through Claude Code.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../03-research/output/[slug]-experiment.md` | Full file when present | The commands to run and the expected values |
| Previous stage | `../05-script/output/[slug]-narration.txt` | Lines carrying `[measured]` | The lines to rewrite |
| Previous stage | `../05-script/output/[slug]-script.md` | Beats with a capture cue | Where each measurement is shown |
| Hub note | `../../videos/[slug].md` | `capture_window` | Night or any |
| Skill | `../../../../skills/dgx-capture/SKILL.md` | Full file | Runner, allowlist, parsing |
| Skill rule | `../../../../skills/dgx-capture/rules/reconcile.md` | Full file | Tolerances and how lines are rewritten |
| Brand vault | `../../../../brand-vault/voice-rules.md` | "Hard Constraints" | Spoken-number rules for rewritten lines |
| Reference | `references/capture-note-format.md` | Full file | Layout of the capture note |

## Process

1. If no experiment plan exists, write `output/[slug]-capture.md` stating "no experiment" and stop (the stage passes).
2. Run `capture.py --plan [experiment.md] --out [build-dir]/[slug]/capture --window [hub capture_window or night]`; a refused command fails the stage.
3. Compare every measured metric with the expected value and with the `[measured]` lines in the narration.
4. Reconcile per reconcile.md: within tolerance, rewrite the narration line (and the script beat) with the measured value in spoken form and drop the marker; beyond tolerance, keep the lines, set the hub note to `blocked` with `blocked_reason: re-script: [metric] measured X vs scripted Y` and stop.
5. Run the audit checks below. If any fail, set the hub note to `blocked`.
6. Write `output/[slug]-capture.md`; journal the hub note.
7. `../../../../tools/git-sync.sh "long-form: [slug] capture"`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Plan ran | every planned command ran, or is listed as skipped with a reason |
| No markers | no `[measured]` marker remains in the narration file |
| Consistency | no number in the script contradicts `capture.json` |
| Recordings | every command has a `.cast` or a stdout transcript in the build dir |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Capture note | `output/[slug]-capture.md` | per capture-note-format.md |
| Recordings and metrics | `[build-dir]/[slug]/capture/` | capture.json and casts (never committed) |

The experiment plan is the edit surface: change a command there and re-run the stage. The narration file it rewrote is what the voice stage reads.
