# Stage 05: Script

Write the full episode script in the channel's voice, with the visual intent of every beat, and the plain narration file the voice stage reads.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../04-outline/output/[slug]-outline.md` | Full file | Angle, value brief, chapters, visual philosophy |
| Previous stage | `../03-research/output/[slug]-brief.md` | "Claims", "Key numbers", "Analogy candidates", "Glossary" | Every fact comes from here |
| Previous stage | `../03-research/output/[slug]-experiment.md` | Command ids and expected values, when present | Capture cues and the numbers to be measured |
| Hub note | `../../videos/[slug].md` | `feedback` | Re-script notes |
| Brand vault | `../../../../brand-vault/voice-rules.md` | "Hard Constraints" through "What the Voice Is NOT" | Voice discipline |
| Brand vault | `../../../../brand-vault/identity.md` | "Audience" | Who is listening |
| Reference | `references/script-format.md` | Full file | Layout, beat table, narration file rules |
| Reference | `references/retention-beats.md` | Full file | Pacing rules for long-form |
| Skill | `../../../../skills/script-gates/SKILL.md` | "normalize_narration.py" | Spoken-form check |
| Shared | `../../../../shared/platform-specs.md` | "Long-form" table | Length, chapters, pacing |

## Process

1. Read the outline and the brief. Confirm the chapter list and the two value types. **[Checkpoint]** -- present the chapter list with one line of narration intent each.
2. Write the full script in one pass per script-format.md: for each chapter a beat table (narration in spoken form, on-screen text with digits, visual intent, scene-type hint, capture cue id when a measurement is shown). Numbers that will be measured are written with the expected value and marked `[measured]` so the capture stage can rewrite them.
3. Write `output/[slug]-narration.txt`: narration only, one paragraph per beat, a blank line between chapters, no stage directions.
4. Run `normalize_narration.py --text` on the narration file; rewrite any token it had to expand.
5. Run the audit checks below. If any fail, revise before saving.
6. Save `output/[slug]-script.md`; update the hub (`status: scripted`, Artifacts link, Decisions).
7. Unattended: `../../../../tools/git-sync.sh "long-form: [slug] script"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | Chapter list with narration intent | Approve or reorder before writing |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Voice | zero Hard Constraint violations; sentences 20 words or fewer, average 18 or fewer |
| Numbers | every number names its unit and referent; digits only in on-screen text; at most one new number per sentence |
| Pacing | a new-information beat at least every 30 s by estimate; the surprising number by 0:20 |
| Chapters | chapters match the outline in order and count; each 60 s or longer by estimate |
| Length | narration words within the band for the target minutes (about 150 words per minute) |
| No skeleton | no First/Then/Finally scaffolding, no "in this video", no recap of a recap |
| Cues | every capture cue id exists in the experiment plan; every `[measured]` number has a cue |
| Value delivery | both locked value types are delivered (the note names the beat for each) |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Script | `output/[slug]-script.md` | per script-format.md |
| Narration | `output/[slug]-narration.txt` | plain text, spoken form, paragraph per beat |

The script and the narration file are the human edit surface. Rewrite a beat, cut a chapter. The spec stage, the capture stage and the voice stage read whatever is there.
