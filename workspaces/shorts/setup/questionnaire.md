# Onboarding Questionnaire: BLAI Shorts

Read this file when the user types `setup`. This workspace ships configured for the Build Local AI channel (the values below are already in the files), so ask ALL questions in one pass only to confirm or change them. These configure the production system, not a specific Short; topics come from the radar every morning. Never write an API key or voice id into any committed file; those go in the cloud environment or `build/.env` (see `../../shared/env-template.md`).

### Q1: How many Shorts per day?
- Current value: 2
- Files: `stages/02-ideas/references/selection-rules.md` ("Picks per day")
- Type: number
- Default: 2

### Q2: How should the two daily picks split across the length bands?
- Current value: alternate `classic` and `smooth-explainer` across the two picks; a news-react pick is always `classic`
- Files: `stages/02-ideas/references/selection-rules.md` ("Format mix")
- Type: free text
- Default: as above

### Q3: How should the gate card deliver the preview?
- Current value: `telegram-video` (attach the mp4 when under 48 MB, else an R2 link)
- Files: `stages/07-render/references/scene-workflow.md` ("Preview delivery")
- Type: selection
- Options: telegram-video, link-only

### Q4: Which brand voice facts should change?
- Current value: the files in `../../brand-vault/` as shipped (ported from the v1 soul doc)
- Files: `../../brand-vault/identity.md`, `../../brand-vault/voice-rules.md`
- Type: free text
- Note: present the Hard Constraints, the Wrong/Right table and Pacing and ask the user to edit anything that does not sound like them (the two-pass voice review)

### Q5: Publish slots for Shorts (audience time, America/Chicago)?
- Current value: 11:00 and 18:00
- Files: `../../shared/playbook/publish-timing.md` ("Defaults")
- Type: two times
- Default: 11:00, 18:00

---

## After Onboarding

Pass 1: apply every changed value in the listed files (edit the sentence that carries the current value; there are no `{{PLACEHOLDER}}` tokens in this workspace).

Pass 2 (voice review): show the populated Hard Constraints, Sentence Rules table and Pacing from `../../brand-vault/voice-rules.md` and ask for edits. Apply them.

Then scan every `.md` file in the workspace for `{{[A-Z][A-Z0-9_]*}}` tokens; none should exist. Tell the user: "Shorts is configured. Type `ideas` to run today's sweep, or wait for the 06:00 routine."
