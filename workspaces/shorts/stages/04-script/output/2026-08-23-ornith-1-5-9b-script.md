---
slug: 2026-08-23-ornith-1-5-9b
format: classic
structure: number-first
style_pack: signal
value_types: TEACHES, REFRAMES
target_duration_s: 36
brief: 2026-08-23-ornith-1-5-9b-brief.md
drafts: 2026-08-23-ornith-1-5-9b-drafts.md
winner: draft A
---

# Ornith 1.5 9B fits an 8 GB card

## Decisions

- Two structures written; the judge picked draft A. Scores and reasoning in `2026-08-23-ornith-1-5-9b-drafts.md`.
- Hook chosen from 10 candidates by the hook-library scoring.

## Hook candidates

1. 5.63 GB fixes real bugs  *
2. Nothing serious fits 8 GB. This does.
3. The whole coding model is 5.63 GB
4. Your 8 GB card is enough
5. 70.6 on SWE-bench, in 5.63 GB
6. One file, 5.63 GB, real bugs fixed
7. A 9B model scored 70.6
8. Six gigabytes of model, fixing real bugs
9. This 5.63 GB file fixes bugs
10. 8 GB card, 9B model, real bugs

## Script

| Scene | Role | Narration | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-----------|----------------|--------------|------|--------|-------|
| s1 | hook | Just under six gigabytes on disk, and that's a whole coding model. | 5.63 GB / the whole model | Frame 1: 5.63 GB set huge in amber on the flat near-black field, fully legible before anything else, a single ... | hyperframes | giant-number | 4.5 |
| s2 | explain | You've got eight gigabytes on your card, and a standing rule that nothing serious fits. | your card: 8 GB / nothing serious fits | The frame splits: a graphics card outline on the left stamped 8 GB, its empty slot drawn on the right. At 2s a... | hyperframes | split-compare | 5.5 |
| s3 | explain | This one does. It's Ornith's nine-billion-parameter model, squeezed into that single file. | Ornith 9B / one file, fits | The red rule erases and one file card survives at centre, labelled Ornith 9B. At 1s it drops into the card slo... | hyperframes | centered-stack | 5.0 |
| s4 | explain | On S W E bench Verified, it scores seventy point six. That test hands a model real bugs from real open-source projects. | SWE-bench Verified: 70.6 / real bugs, real repos | A single bar grows from zero and locks, the figure counting up to 70.6 in amber beside it. At 3s the bar's lab... | manim | giant-number | 8.0 |
| s5 | explain | Ornith ran those numbers itself. Averaged over five runs, with the git history stripped and the network switched off. | Ornith's own numbers / 5 runs, averaged / git history stripped, network off | Five identical run tiles draw into a row, each filling with its own result. At 2s they collapse into one avera... | manim | grid | 6.5 |
| s6 | payoff_close | Nobody outside Ornith has reproduced that yet. So pull the file tonight and hand it a bug that already beat you. | no outside reproduction / your card is enough | The averaged score panel dims and a label fades in over it reading NOT YET REPRODUCED. At 2s the panel slides ... | hyperframes | centered-stack | 7.0 |

## Notes for review

Four spoken numbers: five point six three rounded to 'just under six gigabytes' (the surprise, spoken in s1 against 5.63 GB on screen), nine billion parameters (what it is), seventy point six on SWE-bench Verified (the reason to care), five runs (the rigour inside the catch). Context window and GPQA left unspent per the brief's note; the download count was not needed. No analogy: the signature file has no picture for 'small model, big score' and the brief's hatchback is not in it, so the plain mechanism carries the beat. 'S W E bench' is written the way it is said, per the lexicon convention that renders GGUF as 'G G U F'. The close says nobody outside has reproduced the figure rather than naming the harness, because OpenHands and Harbor are not Ornith's. top2 wants 'Ornith-1.5' as well as 'Ornith'; the on-screen card reads 'Ornith 9B' on purpose, because the version digits 1.5 are never spoken and an unspoken number on screen is a render loop-back.
