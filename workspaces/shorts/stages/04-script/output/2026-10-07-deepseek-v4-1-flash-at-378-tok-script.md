---
slug: 2026-10-07-deepseek-v4-1-flash-at-378-tok
format: smooth-explainer
structure: contrarian-take
style_pack: blueprint
value_types: REFRAMES,PROVES
promise: after this you can read any cache-hit tok/s headline and know exactly what your own first prompt will pay
target_duration_s: 88
brief: 2026-10-07-deepseek-v4-1-flash-at-378-tok-brief.md
drafts: 2026-10-07-deepseek-v4-1-flash-at-378-tok-drafts.md
---

# DeepSeek v4.1 Flash at 378 tok/s: the cache-hit catch

## Decisions
- Two structures tried: contrarian-take (draft A) and worked-example (draft B). myth-bust and number-first were barred by the rotation rule (last two shipped: myth-bust 2026-10-06, comparison-ladder 2026-10-05; number-first forces a number hook, which classifies number-shock, also 2026-10-06). Judge: A wins 21 to 18 on payoff timing and difference; no grafts.
- Hook: "That speed isn't your speed." (named-contradiction, candidate 1). Scores on number plus felt tension in the first five words; last two shipped hooks were number-shock and decision.
- Unattended checkpoint 1: structures contrarian-take + worked-example locked, value types REFRAMES,PROVES confirmed, promise as above; rotation rule cleared on both.
- Unattended checkpoint 2: 10 hooks written and scored per hook-library; picks marked with * below, one per draft, different patterns (A named-contradiction, B situation).
- Gates on the winner: validator 0 blockers (advisory: 0 YouTube keyword tags, package stage owns tags); eval_short exit 0 (number_spend 3 of cap 3, hook_concrete via 378, scene_specificity 6/8, sameness clean); variety_check ok vs 31 ledger entries.
- The 99.7% hit rate is deliberately not spoken: the smooth-explainer cap is three numbers and 378/13s/500ms spend them; on screen it reads "nearly every request, a repeat".

## Hook candidates
1. That speed isn't your speed. *
2. 378 tok/s has a catch: it isn't yours.
3. The benchmark that isn't about you.
4. 378 tok/s wasn't your first prompt.
5. Everyone read the number. Nobody read the method.
6. DeepSeek v4.1 Flash isn't that fast for you.
7. Cache hits made that number. You have none.
8. That benchmark is somebody else's warmup.
9. You'd pay the prefill. They didn't.
10. The speed is real. It just isn't yours.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Three hundred seventy-eight tokens a second, and that speed isn't your speed. You saw the headline for DeepSeek four point one Flash. | 378 output tokens per second | That speed isn't your speed. | Frame 1: dark blueprint sheet, faint grid, giant amber digits '378' upper-center with a ruled label 'output tokens per second'; motion onset within 0.5 s as the digits tick upward and lock on 'Three hundred seventy-eight'. On 'isn't your speed', the hook line scales in beneath and an amber strike rule draws under it. On 'Hacker News', a small stamped tag 'seen on Hacker News' fades in top-left. All elements above y1400, clear of right 120 px. | hyperframes | giant-number | 7.6 |
| s02 | explain | That number is RunInfra's, measuring the model alone, just the writing. Nearly every request it served was a repeat the model had already read. A cache hit is a prompt whose start matches notes already stored. | RunInfra, model only | nearly every request, a repeat | On 'That number is RunInfra's', a blueprint nameplate 'RunInfra, model-only' fades in top-center with guide lines. On 'ninety-nine point seven percent', a giant amber '99.7%' rises into mid-frame with sub-label 'last 24 hours' and a small stamp 'cache hits'. On 'matches notes already stored', a checklist card slides no, rises in place and ticks one box. Centered stack, nothing below y1470. | hyperframes | centered-stack | 12.4 |
| s03 | explain | One room, one brain, a desk for each conversation. That desk is the KV cache, the running notes of everything already read. Keeping notes for repeats is prefix caching. A hit finds your desk untouched. | room = the model | desk = the KV cache | hit: desk untouched | On 'One room, one brain', a blueprint room outline draws itself with a single brain glyph at center. On 'a desk for each conversation', three small desk rectangles rise in a row. On 'the KV cache', one desk is tagged 'KV cache: running notes' in amber. On 'prefix caching', a dotted return arrow loops from a repeated prompt card back to the desk. On 'finds your desk untouched', the desk outline flashes amber, unchanged. Drawn line style, measured rules, safe area respected. | manim | diagram-flow | 12.1 |
| s04 | explain | But the desk takes memory, and it doesn't last. Memory pressure clears it. DeepSeek clears its disk cache nightly. Your first prompt is a cache miss. It owes full prefill, a complete read before the first word is written. | desk: not free, not forever | cleared nightly | miss = full prefill | Two annotated panels side by side. On 'isn't free, and it doesn't last', the left panel shows the desk with a small gauge draining. On 'clears its disk cache nightly', a moon glyph wipes the desk lines blank. On 'cache miss', the right panel desk redraws from an empty outline. On 'full prefill', a horizontal bar labeled 'read everything' fills completely before a pen glyph writes a word. Amber accents mark the cost, no elements in bottom 450 px. | manim | split-compare | 13.4 |
| s05 | explain | So what does your first prompt sit through? On DeepSeek's own API, a very long prompt took thirteen seconds to its first token. Warm, five hundred milliseconds. That gap is the cache. | first token, cold vs warm | from 13s to just 500ms | A ruled timeline across mid-frame titled 'DeepSeek's API: first token, very long prompt'. On 'thirteen seconds', a long amber bar draws rightward to a mark labeled '13s cold'. On 'five hundred milliseconds', a short bar draws beside it labeled '500ms warm'. On 'That gap is the cache', the space between the bars is hatched and tagged 'the cache'. Caption 'cold vs warm, same prompt' fades in above. Bars end well left of the right 120 px margin. | manim | timeline | 11.0 |
| s06 | explain | Whose speed is it? The traffic's, not the model's. Same model, same hardware, different requests. RunInfra's best account was an agent that had already read a very long prompt. The model doesn't make the hits. Your prompts do. | hit rate = traffic, not model | your prompts make the hits | On 'Whose speed is it?', a grid of identical request cards fades in. On 'The traffic's, not the model's', each card stamps itself 'HIT' in amber while a model box at the side stays blank. On 'already read a very long prompt', one tall scroll card unrolls behind the grid, tagged 'RunInfra's best account'. On 'Your prompts do', the final stamp pauses mid-press, then lands with a small bounce. Grid sits centered, clear of the caption band. | hyperframes | grid | 13.1 |
| s07 | explain | Independent tests on DeepSeek's own API measured it slower. The number is real, and cache hits are how production agents run. Every new conversation repeats that first read. | independent check: slower | new chat = first read again | Two ruled frames side by side, no digits. On 'measured it slower', the left frame labeled 'the headline' keeps a tall bar while the right frame labeled 'independent check' draws a visibly shorter bar. On 'pays that first read again', a fresh chat card fades into the right frame and its read bar restarts from blank. Amber highlights the difference; composition stays above y1400. | hyperframes | split-compare | 9.7 |
| s08 | payoff_close | So measure the first prompt. That one is yours. | measure the first prompt | the speed is yours | Build Local AI | On 'measure the first prompt', the strike-ruled hook line from scene 1 returns and re-inks as 'measure the first prompt', centered. On 'The number is real', the amber strike rule lifts off the old hook. On 'the speed is yours', a calm amber underline settles beneath the new line. Final 0.5 s: 'Build Local AI' wordmark fades in top-center and the blueprint grid stills, rhyming with frame 1's composition. | hyperframes | centered-stack | 3.1 |

## Notes for review
Check timing math: narration is about 279 words, landing near 96 s at 2.9 words per second. The independent 226.6 tok/s figure is deliberately softened to 'measured it slower' and is never spoken or shown; likewise the 128K prompt becomes 'a very long prompt' on screen and in narration. The desk analogy's limit (not free, cleared under pressure, nightly wipe) is stated in scene s04.
