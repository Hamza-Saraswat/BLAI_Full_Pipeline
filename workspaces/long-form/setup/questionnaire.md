# Onboarding Questionnaire: BLAI Long-form

Read this file when the user types `setup`. The workspace ships configured (values below are already in the files); ask ALL questions in one pass to confirm or change them. System-level only; episode topics come from the radar. Never write secrets into committed files (`../../shared/env-template.md`).

### Q1: How many episodes per week, and on which production days?
- Current value: 3, produced Mon/Wed/Fri mornings (ramping 1 -> 2 -> 3 is recommended for the first month)
- Files: `stages/02-ideas/references/selection-rules.md` ("Cadence"), `../../shared/cloud-environment.md` (routine cron)
- Type: number + days
- Default: 3, Mon/Wed/Fri

### Q2: Target episode length?
- Current value: 10-14 minutes (hard band 8-20)
- Files: `stages/04-outline/references/outline-format.md` ("Length")
- Type: range in minutes
- Default: 10-14

### Q3: When may experiment captures run on the Spark?
- Current value: `night` (01:00-06:00 America/Chicago), overridable per episode with `capture_window: any` in the hub note
- Files: `stages/08-capture/references/capture-note-format.md` ("Window")
- Type: selection
- Options: night, any

### Q4: Which scene types are enabled?
- Current value: all library scenes except `mascot-talk` and `b-roll`, which stay off until a mascot design and a stock source exist
- Files: `stages/06-spec/references/spec-format.md` ("Enabled scene types")
- Type: multi-select
- Options: mascot-talk, b-roll

### Q5: Which series should be favored this month?
- Current value: none favored; rotation only
- Files: `stages/02-ideas/references/selection-rules.md` ("Favored series")
- Type: free text
- Default: none

---

## After Onboarding

Pass 1: apply every changed value in the listed files (there are no `{{PLACEHOLDER}}` tokens in this workspace; edit the sentence that carries the current value).

Pass 2 (voice review): the brand vault is shared with the Shorts workspace; run the voice review there if it has not been done.

Scan every `.md` file for `{{[A-Z][A-Z0-9_]*}}` tokens; none should exist. Tell the user: "Long-form is configured. Drop a project note into `input/` and type `ideas`, or wait for the next Mon/Wed/Fri routine."
