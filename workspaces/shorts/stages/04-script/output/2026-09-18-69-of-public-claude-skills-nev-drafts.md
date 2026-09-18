---
slug: 2026-09-18-69-of-public-claude-skills-nev
winner: draft A (number-first)
score: 21-10
---

# Drafts and judge: 69% of public Claude skills never trigger

## Draft A (number-first) -- WINNER 21

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| 1 | hook | Sixty-nine percent of public Claude Code skills cannot reliably trigger. | 69% won't reliably trigger | Giant "69%" and subline fully legible at frame 1 on dark background; at 0.30s the number does a subtle scale settle, single amber accent, nothing else moves. | hyperframes | giant-number | 3.4 |
| 2 | explain | Your skills show up when listed, yet Claude works without them. A lint, a static checker for skill files, judged two hundred sixteen of them. | 216 public skills judged | On "show up when listed", a left column of skill names fades in; on "works without them", a right column rises showing the task done alone; on "two hundred sixteen", the count text fades in below, amber accent on the count only. | hyperframes | split-compare | 8.3 |
| 3 | explain | At startup, Claude Code loads only names and descriptions. That description, one line saying what the skill does and when to use it, is the entire selection surface. The full instructions load after your request matches it. | description = entire selection surface | On "loads only names and descriptions", rows of one-line descriptions fade in as a list; on "entire selection surface", one description line scales up with amber highlight; on "after your request matches it", a thick instruction block rises beneath it, connected by a thin line. | manim | diagram-flow | 11.4 |
| 4 | explain | Most score fine elsewhere; the failure hides in that line. It's mechanical, not model flakiness. | mechanical, not model flakiness | On "score fine elsewhere", a short checklist of green checkmarks fades in; on "hides in that line", everything dims except the single description line, which scales slightly; on "mechanical, not model flakiness", the screen text fades in beneath. | hyperframes | centered-stack | 4.8 |
| 5 | explain | Only fifty-two percent of skills include invocation cues, the phrases that say when to fire. Lead yours with the use case and the words you'd actually say. | 52% include invocation cues | On "fifty-two percent", a horizontal bar fills to the 52% mark with counter; on "invocation cues", a vague line reading "Helps with documents" fades in at left; on "lead yours with the use case", a rewritten line rises at right with the trigger phrase in amber. | hyperframes | split-compare | 9.3 |
| 6 | payoff_close | One line of text decides whether your skill ever runs. Rewrite it, and it fires. | rewrite the line | On "one line of text", a single description line centers and scales up alone; on "rewrite it, and it fires", the line retypes into its fixed form and the skill name rises beneath it in amber; wordmark settle. | hyperframes | centered-stack | 5.2 |

## Draft B (how-to-three-moves) -- 10

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-----|------|------------------------|----------------------------------------|--------------|------|--------|-------|
| 1 | hook | Three moves and your skills fire tonight. They list fine, but Claude ignores them. | Three moves and your skills fire tonight. | Frame-1 hook text fully legible at frame 1, centered. On "They list fine," a short skill-name list fades in below, amber accent on names. On "Claude ignores them," the list dims. Motion onset after 0.30s, one element at a time. | hyperframes | centered-stack | 5.2 |
| 2 | explain | At startup, Claude Code loads only each skill's name and description, one summary line. Your request matches that line alone. | Only name and description load | Diagram: on "loads only each skill's name and description," two small cards labeled "name" and "description" rise. On "Your request matches that line alone," a request bar fades in left and a connector fades to the description card, amber accent on the match. At most two elements animating. | manim | diagram-flow | 6.9 |
| 3 | explain | A lint, a static checker, judged sixty-nine percent of two hundred fifteen public skills that won't reliably trigger. | 69% of 215 skills won't reliably trigger | Giant "69%" scales in on "sixty-nine percent," amber accent. Subtext "of 215 skills" fades in on "two hundred fifteen public skills." One soft thud sfx on the number. Two elements max, onsets after 0.30s. | hyperframes | giant-number | 6.2 |
| 4 | explain | Move one: open SKILL.md, the instruction file, and read the description line. If it just says "Helps with documents," that's the failure. | Description: "Helps with documents" | A SKILL.md file card fades in on "open SKILL.md"; its frontmatter block rises slightly on "the instruction file." On "'Helps with documents,'" that single description line highlights in amber through "that's the failure." One text block at a time. | hyperframes | centered-stack | 7.6 |
| 5 | explain | Move two: rewrite it: use case first, then the words users say. Stay under one thousand five hundred thirty-six characters, the listing cap. | Cap: 1,536 characters | Split compare, one block at a time: on "rewrite it," the old line "Helps with documents" shows left; on "use case first, then the words users say," it fades as the rewrite "Use when the user asks to parse PDFs" rises right, amber on the use case. On "thirty-six characters," "Cap: 1,536 characters" fades in below. One swap tick sfx. | hyperframes | split-compare | 7.9 |
| 6 | payoff_close | Move three: validate the frontmatter, the metadata block, then test with a plain request. The skill fires without being called by name. | Fires without being called by name | Timeline: a "validate" node fades in on "validate the frontmatter"; a "test" node rises on "test with a plain request." On "The skill fires without being called by name," the final node accents amber with one chime sfx, then all text clears and the channel wordmark settle | manim | timeline | 7.6 |

## Judge scores (kimi-k3, rubric judge-rubric.md)

| row | draft A | draft B |
|-----|---------|---------|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 2 | 1 |
| 3 Specificity | 3 | 1 |
| 4 Voice | 2 | 0 |
| 5 Navigation | 3 | 1 |
| 6 Difference | 2 | 1 |
| 7 Repeat test | 3 | 2 |
| 8 Teaching | 3 | 2 |
| Total | 21 | 10 |

Winner: A. Graft: "If it just says 'Helps with documents,' that's the failure." moved from B s04 into A s04; A diagnosed the failure abstractly and B's line shows Anthropic's own anti-example. No other grafts.

What the losing shape would have needed: the two numbers split with correct referents, move one landing by second eight, and a close stating the fix rather than the test outcome. It also repeated the 2026-09-11 tonight hook and Move-label shape.
