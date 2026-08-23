# Script Format (long-form)

## `[slug]-script.md`

```
---
slug: [slug]
series: [series]
structure: [structure]
value_types: A, B
target_minutes: 12
words: 1820
chapters: 4
---

# [working title]

## Decisions
- Chapter order and any outline change, with reasons.

## Chapter 1: [2-6 word label]
| Beat | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual intent (what a muted viewer understands) | Scene hint | Capture cue |
|------|-------------------------|------------------------------------------|--------------------------------------------------|------------|-------------|
| 1.1 | ... | ... | ... | kinetic-text | |
| 1.2 | ... "about twenty-two tokens per second [measured]" ... | 22 tok/s | ... | terminal-replay | cmd2 |

## Chapter 2: ...

## Notes for review
- Numbers rounded and how; analogies and their limits; anything the reviewer should double-check.
```

## `[slug]-narration.txt`

- Narration only, in reading order, one paragraph per beat, a blank line between chapters.
- Spoken form throughout: numbers as words with unit and referent, acronyms as said. The `[measured]` marker stays in the text until the capture stage rewrites the line; the voice stage strips any marker that remains.
- No headings, no stage directions, no on-screen text.

## Beat rules

- One idea per beat; 20-60 words per beat; a beat is the unit the spec stage maps to one scene.
- The first beat of chapter 1 is the hook; the promise lands inside the first 30 seconds.
- Every chapter ends on something usable (a command, a number, a decision rule).
- Scene hints come from the scene library in `skills/render-longform/rules/scene-library.md`; they are hints, the spec stage decides.
- Person: first person singular for what I did on the Spark, second person for what the viewer should do.
- `structure` is carried unchanged from the outline's frontmatter. It fixes the chapter pattern, where the payoff sits, and whether positional labels are allowed at all; the gate reads it from here.
