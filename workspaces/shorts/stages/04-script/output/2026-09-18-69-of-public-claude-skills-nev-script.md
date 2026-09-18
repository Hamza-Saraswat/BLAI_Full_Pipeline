---
slug: 2026-09-18-69-of-public-claude-skills-nev
format: classic
structure: number-first
style_pack: signal
value_types: TEACHES,REFRAMES
promise: after forty-four seconds you can open any SKILL.md and rewrite the one description line so the skill actually fires
target_duration_s: 44
brief: 2026-09-18-69-of-public-claude-skills-nev-brief.md
drafts: 2026-09-18-69-of-public-claude-skills-nev-drafts.md
---

# 69% of public Claude skills never trigger

## Decisions

- Structures tried: number-first (draft A) and how-to-three-moves (draft B). Myth-bust and
  contrarian-take, the natural fits for a myth-bust lane, are hard-banned: the ledger's last
  two entries (2026-09-16, 2026-09-17) used them. A won 21-10 on the judge rubric.
- Hook: "Sixty-nine percent of skills never fire." (number-shock, candidate 1). Product-grade
  specific, legible as frame-1 text in five words, true per the brief, names the tension in the
  first five words.
- Graft from B: "If it just says 'Helps with documents,' that's the failure." into A's fourth
  scene. A diagnosed the failure abstractly; B's line shows Anthropic's own anti-example. No
  other grafts.
- Value lines: TEACHES lands in scene 3 ("That one line ... is the entire selection surface");
  REFRAMES lands in scene 4 ("It's mechanical, not model flakiness").
- Soft gates: entity_spend 0.14 and top2 miss kept on purpose. The script says "a lint" and
  "Claude Code" instead of naming Skill Crossroads in narration; on screen the entities are
  skills, descriptions, SKILL.md. Reason: narration names crowd the 44-second runtime and the
  lint's method (a static checker) matters more than its brand.
- Normalizer: no narration changes expected; digits only on screen.

## Hook candidates

1. Sixty-nine percent of skills never fire. *
2. Sixty-nine percent of public Claude skills never trigger.
3. Two hundred sixteen skills checked. One passed clean.
4. Your Claude skills are installed, listed, and asleep.
5. A lint just graded two hundred sixteen Claude skills.
6. Three moves and your Claude skills fire tonight.
7. Claude reads one line of your skill. Most blow it.
8. Only fifty-two percent of skills say when to fire.
9. Your skills folder is a crew nobody calls in.
10. One line of text decides if your skill ever runs.

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Sixty-nine percent of skills never fire. | 69%. Skills that never fire. | Giant "69%" and subline fully legible at frame 1 on dark background; the number begins a subtle scale settle within half a second, single amber accent, nothing else moves. | hyperframes | giant-number | 2.4 |
| s02 | explain | Your skills show up when listed, yet Claude works without them. A lint, a static checker, judged two hundred sixteen of them. | 216 public skills judged | On "show up when listed" a left column of skill names fades in; on "works without them" a right column rises showing the task done alone; on "two hundred sixteen" the count fades in below, amber accent on the count only. | hyperframes | split-compare | 8.3 |
| s03 | explain | At startup, Claude Code loads only names and descriptions. That one line, what the skill does and when to use it, is the entire selection surface. The body loads after your request matches. | description = entire selection surface | On "loads only names and descriptions" rows of one-line descriptions fade in as a list; on "entire selection surface" one description line scales up with amber highlight; on "after your request matches" a thick instruction block rises beneath it, connected by a thin line. | manim | diagram-flow | 12.4 |
| s04 | explain | Most score fine elsewhere; the failure hides in that line. If it just says 'Helps with documents,' that's the failure. It's mechanical, not model flakiness. | vague description = silent failure | On "score fine elsewhere" a short checklist of green checkmarks fades in; on "Helps with documents" a vague description line appears and dims everything else, amber highlight on it through "that's the failure"; on "not model flakiness" the screen text fades in beneath. | hyperframes | centered-stack | 8.6 |
| s05 | explain | Only fifty-two percent of skills include invocation cues, the phrases that say when to fire. Lead yours with the use case and the words you'd say. | 52% include invocation cues | On "fifty-two percent" a horizontal bar fills to the 52% mark with counter; on "invocation cues" a vague line reading "Helps with documents" fades in at left; on "lead yours with the use case" a rewritten line rises at right with the trigger phrase in amber. | hyperframes | split-compare | 9.3 |
| s06 | payoff_close | One line in SKILL.md decides if your skill runs. Rewrite it, and it fires. | rewrite the line | On "one line in SKILL.md" a single description line centers and scales up alone; on "rewrite it, and it fires" the line retypes into its fixed form and the skill name rises beneath it in amber; wordmark settle. | hyperframes | centered-stack | 4.5 |

## Notes for review

- The sixty-nine percent is one linter's LLM judgement on 215 of 216 skills, not a production
  failure measurement; the narration says "judged" and never "proved".
- The graft line "Helps with documents" is Anthropic's own anti-example from its authoring
  best-practices page, quoted verbatim.
- No analogy used: the mechanism is shown concretely. The crew-board analogy from the brief was
  available and deliberately left out to keep the runtime tight; if review wants it, scene 3 is
  where it would go, with its 1,536-character limit stated in the same clause.
- Estimated total 43.5 s at 2.9 wps; target set to 44 s inside the classic hard band (28-60),
  above the 32-38 sweet spot. The extra seconds carry the mechanism scene.
