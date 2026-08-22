# Spec Format

## Enabled scene types

title-card, chapter-card, kinetic-text, code-typing, terminal-replay, diagram, comparison-table, chart, stat-callout, quote, end-card. Disabled until their assets exist: `mascot-talk` (needs the mascot design), `b-roll` (needs a stock source). Enable them here when ready.

## `[slug]-spec.md`

```
---
slug: [slug]
target_duration_s: 720
scenes: 34
---

# Spec: [working title]

## Scene sequence
| # | Id | Type | Chapter | Est s | On-screen text | Visual intent | Capture |
|---|----|------|---------|-------|----------------|---------------|---------|

## Thumbnail concepts
1. words: "22 tok/s on 128 GB" | focus: the number
2. ...
3. ...

## Decisions
- Why this visual mix; which beats were merged or split and why.
```

## Rules

- The spec never contains component names, frame numbers, pixel positions, fonts or colors. Those belong to the render skill.
- Every scene carries the exact narration text of its beat; the render stage times scenes from the captions using that text.
- `data` carries only what the scene library asks for (code text, rows, series, nodes, quote). Numbers in `data` match the narration.
- `sync_points` name a phrase in the narration and the event that should land on it ("count-up reaches 22", "arrow lands on GPU").
- One `title-card` first, one `chapter-card` at every chapter start, one `end-card` last.
