---
slug: 2026-09-10-deepseek-v4-1-flash-open-weigh
format: classic
structure: news-react-so-what
style_pack: signal
value_types: TEACHES, EQUIPS
promise: after ~38 seconds the viewer can say what the 890-bytes-per-token KV cache number changes for their machine and what to watch for next
target_duration_s: 38
brief: 2026-09-10-deepseek-v4-1-flash-open-weigh-brief.md
drafts: 2026-09-10-deepseek-v4-1-flash-open-weigh-drafts.md
---

# DeepSeek V4.1 Flash: open weights just landed

## Decisions
- Structures tried: news-react-so-what (draft A) vs number-first (draft B); A won 19-17 on the judge rubric (hook 3v2, teaching 3v2; no grafts). Both cleared rotation (last two: comparison-ladder, worked-example).
- Hook: candidate 8, named-contradiction ("DeepSeek's new Flash beat its own Pro. Your card is the catch."), compressed to "Flash beat Pro. Your card can't." for frame 1. Draft B took candidate 9, number-shock.
- Unattended checkpoint calls: structures+promise confirmed per contract step 1; hooks 10 scored, picks marked per step 2.
- Judge retro flags logged: close pattern calcifying (viewer imperative 3 of last 5), durations clustering 37-38 s, "quant"/"token" gloss borderline under constraint 3.

## Hook candidates
1. Eight hundred ninety bytes. That is what one token costs now.
2. DeepSeek V4.1 Flash just dropped its weights, free.
3. This model's notes shrank four hundred thirty-seven times.
4. You've got twenty-four gigabytes. A million-token context just got cheap.
5. Your GPU isn't the problem. Your notes are.
6. DeepSeek just shrank the cost of context memory 437 times.
7. Your chat history is about to stop filling your RAM.
8. DeepSeek's new Flash beat its own Pro. Your card is the catch. *
9. One token used to cost 389,120 bytes. Now 890. *
10. Twenty-four gigabytes won't hold the weights. The notes will fit.

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | DeepSeek's new Flash beat its own Pro. Your card is the catch. Free weights dropped this morning. | Flash beat Pro. Your card can't. | Frame 1 composition: finished amber-on-dark kinetic headline "Flash beat Pro. Your card can't." fully legible, GPU-card silhouette below. Motion onset within 0.5 s of frame 1: a slow pulse on "can't" starting at 0.4 s. On 'Free weights dropped this morning' a small HF-style download tag rises in place under the headline. | hyperframes | centered-stack | 6 |
| s02 | explain | One token of context now costs eight hundred ninety bytes of KV cache, a model's running notes. | 890 bytes per token | On 'One token of context' a single token chip fades in at center. On 'eight hundred ninety bytes' the giant amber 890 scales in with 'bytes per token' beneath. On 'a model's running notes' two thin note-lines fade in stacked beside the number. | hyperframes | giant-number | 6 |
| s03 | explain | DeepSeek's layers share one set of notes, written in half-size shorthand. Sous chefs, one clipboard; the model trained to share. | One shared clipboard, half-size notes | On 'share one set of notes' three layer boxes fade in left, each holding a note-card; the three cards fade out as one shared card scales in at center. On 'half-size shorthand' the shared card scales to half size. On 'the model trained to share' a tiny dumbbell glyph fades in beside it. | manim | diagram-flow | 7 |
| s04 | explain | By our arithmetic, a million-token context needs under one gigabyte of cache. The weights: five hundred fifty-two billion parameters. They won't fit your card. | 0.9 GB cache vs 552B parameters | Split screen, cache left, weights right. On 'under one gigabyte of cache' a small amber bar labeled 0.9 GB scales in left, tagged 'our math'. On 'five hundred fifty-two billion parameters' a massive dark block labeled 552B rises right, dwarfing the bar. On "won't fit your card" the GPU silhouette from frame 1 fades in under the block with an amber X scaling onto it. | hyperframes | split-compare | 8 |
| s05 | explain | That beat-its-Pro score is DeepSeek's own harness. And a finished local build? We couldn't find one yet. | Vendor harness. No finished quant yet. | On 'That beat-its-Pro score' a small vendor-harness tag fades in top corner over a faint benchmark row. On "We couldn't find one yet" three empty quant-listing slots appear along a thin timeline, each flashing empty; no fill animation. | hyperframes | timeline | 6 |
| s06 | payoff_close | Your twenty-four gigabyte card is the gate. Watch for the first quant that fits. | Your card is the gate | Frame rhymes with frame 1: same amber-on-dark centered geometry. On 'Your card is the gate' the line fades in alone, mirroring the frame-1 headline. On 'the first quant that fits' one slot from the timeline fills amber once, then the wordmark settle. | hyperframes | centered-stack | 5 |

## Notes for review
- 0.9 GB for a million-token context is OUR arithmetic from the tech report's per-token figure, not a DeepSeek claim; it is hedged on screen as "our math".
- Spoken numbers: 890 bytes, one gigabyte (cache), 552 billion parameters, twenty-four gigabyte card. 389,120 stays off the narration in draft A (it is draft B's hook).
- The beat-its-Pro claim is scoped to "that score" and named as DeepSeek's own harness; Opus-5.0 leads on other benches per the brief.
- Analogy limit stated: sharing works because the model was trained to share.
- "Quant" is spoken unglossed twice (s05, s06); judge logged it as a voice-rules candidate, not a gate failure.
