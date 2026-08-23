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
| Reference | `../04-outline/references/episode-structures.md` | The section for the outline's `structure` | Chapter pattern, payoff placement, the trap to avoid |
| Reference | `references/hook-library.md` | Full file | The first thirty seconds; write 8 hooks, keep 1 |
| Reference | `references/script-format.md` | Full file | Layout, beat table, narration file rules |
| Reference | `references/retention-beats.md` | Full file | Pacing rules for long-form |
| Skill | `../../../../skills/script-gates/SKILL.md` | "normalize_narration.py" | Spoken-form check |
| Skill rule | `../../../../skills/script-gates/rules/longform-gates.md` | Full file | What the long-form script gate checks and what blocks |
| Shared | `../../../../shared/platform-specs.md` | "Long-form" table | Length, chapters, pacing |

## Process

1. Read the outline and the brief. Take the outline's `structure` and load that section of episode-structures.md. Confirm the chapter list and the two value types. **[Checkpoint]** -- present the chapter list with one line of narration intent each.
2. Write 8 hook candidates per hook-library.md, score them, keep one. Record all 8 and the winner under `## Decisions`. The first thirty seconds carries the hook, the "why you" line, the promise, and the surprising number by 0:20.
3. Write the full script in one pass per script-format.md: for each chapter a beat table (narration in spoken form, on-screen text with digits, visual intent, scene-type hint, capture cue id when a measurement is shown). Numbers that will be measured are written with the expected value and marked `[measured]` so the capture stage can rewrite them.
4. Write `output/[slug]-narration.txt`: narration only, one paragraph per beat, a blank line between chapters, no stage directions.
5. Run `normalize_narration.py --text` on the narration file; rewrite any token it had to expand.
6. Run the gate: `python3 ../../../../skills/script-gates/scripts/validate_longform.py --script output/[slug]-script.md --narration output/[slug]-narration.txt --outline ../04-outline/output/[slug]-outline.md`. Rewrite until it reports zero blockers; fix each advisory or record why it stands.
7. Run the audit checks below. If any fail, revise before saving.
8. Save `output/[slug]-script.md`; update the hub (`status: scripted`, Artifacts link, Decisions).
9. Unattended: `../../../../tools/git-sync.sh "long-form: [slug] script"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | Chapter list with narration intent | Approve or reorder before writing |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Script gate | `validate_longform.py` reports zero blockers; every advisory is fixed or carries a written reason |
| Voice | zero Hard Constraint violations; sentences 20 words or fewer, average 18 or fewer |
| Shape | the script follows the outline's `structure`: chapter pattern, payoff placement, no positional labels outside `build-along` |
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
