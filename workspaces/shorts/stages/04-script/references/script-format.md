# Script Note Format and Storyboard Mapping

## `[slug]-script.md`

```
---
slug: [slug]
format: classic | smooth-explainer
structure: [from script-structures.md]
style_pack: [from style_rotation.py]
value_types: A, B
promise: [one sentence: what the viewer can do or decide after 40 seconds]
target_duration_s: [inside the band]
brief: [slug]-brief.md
drafts: [slug]-drafts.md
---

# [working title]

## Decisions
- The two structures tried and why; which won and by how many points
- Hook: which of the 10 and why
- Any graft taken from the losing draft

## Hook candidates
1. ... (10 lines, the pick marked with *)

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | ... | ... | ... | hyperframes | ... | 4 |
| ... | ... | ... | ... | ... | manim | ... | ... |
| sNN | payoff_close | ... | ... | wordmark settle | hyperframes | ... | 3 |

## Notes for review
What the reviewer should check (a number you rounded, a claim you softened, the analogy's limit).
```

## Mapping to `[slug]-storyboard.json`

| Storyboard field | Comes from |
|------------------|------------|
| `slug`, `topic` | hub note slug and the brief's thesis subject |
| `title`, `description`, `hashtags` | working values; the package stage overwrites the final ones in its own note |
| `hook_text`, `hook_candidates` | the picked hook and the 10 candidates |
| `style_pack`, `script_format`, `structure`, `value_types` | the script header |
| `target_duration_s` | the script header |
| `narration_full` | every scene's narration joined with single spaces, in order |
| `analogy`, `music_mood` | the brief's analogy candidate used (or empty) and a mood word |
| `scenes[]` | one entry per script row: `id`, `role`, `tool`, `layout_archetype`, `narration`, `on_screen_text`, `visual_brief`, `est_duration_s`, optional `render_notes` |
| `notes_for_review` | the Notes for review section |

Rules: scene narration strings must concatenate exactly to `narration_full`; numbers are words in narration and digits on screen; a number on screen is spoken in the same scene; the last scene's role is `payoff_close`; the schema is `shared/schemas/storyboard.schema.json` and the validator in `skills/script-gates` is the judge.

## The drafts note

`[slug]-drafts.md` holds both drafts, the judge's score table for every row, the winner, each graft with its reason, and two sentences on what the losing shape would have needed. Layout and scoring live in `judge-rubric.md`. This note is committed: the weekly retro reads it when one structure keeps losing.

## The ledger

`output/script-ledger.json` is appended by `variety_check.py record` after the winner is saved. It carries the structure, hook pattern, closing move, duration and sentence-opener fingerprint of every script, and it is what the `sameness` gate compares against. Never edit it by hand; if a run is abandoned, delete its entry rather than rewriting it.
