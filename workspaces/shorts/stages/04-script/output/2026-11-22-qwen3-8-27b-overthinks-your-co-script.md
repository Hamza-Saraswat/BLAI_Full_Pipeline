---
slug: 2026-11-22-qwen3-8-27b-overthinks-your-co
format: classic
structure: myth-bust
style_pack: signal
value_types: TEACHES,EQUIPS
promise: After this Short you can stop Qwen3.8-27B burning twenty-one minutes of thinking on one prompt, with one flag and one hard cap.
target_duration_s: 42
brief: 2026-11-22-qwen3-8-27b-overthinks-your-co-brief.md
drafts: 2026-11-22-qwen3-8-27b-overthinks-your-co-drafts.md
---

# Qwen3.8-27B overthinks your code: the fix

## Decisions
- Two structures tried: how-to-three-moves (draft A) vs myth-bust (draft B); B won 23 to 17 on the judge rubric, A capped on row 6 (difference) for repeating the 2026-11-19 how-to/tonight shape.
- Hook: "21 minutes. One SVG." (number-shock, candidate 1 of 10); digits on frame 1, spoken as words in narration; survives the hook_concrete matcher via digit and key number.
- Graft from A: "The flag is only a suggestion; a budget is a hard stop" replaces B's flatter "Engines can ignore that, so add a hard cap" in s04; no numbers added, person and beat intact.
- Gates on the winner: validator 0 blockers 0 advisories; eval failures none (entity_spend/top2 soft advisories only; no named-entity density in a classic this number-led); sameness ok against the last 5; normalizer scenes_changed 2.

## Hook candidates
1. Twenty-one minutes for one SVG. (*)
2. Three moves and your coder stops stalling tonight.
3. 22,276 reasoning tokens. 3,223 of code out.
4. Your coder isn't slow. Its dial is glued.
5. You ask for one edit. It thinks for twenty-one minutes.
6. Qwen3.8-27B thinks itself out of answers.
7. 19.4% of xhigh calls came back empty.
8. One prompt. Fourteen minutes of thinking.
9. Set two flags tonight, cut the thinking eight times.
10. xhigh or medium? Eight times the tokens decides.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Twenty-one minutes for one vector image. You run it locally for coding. So: slow model. | Qwen3.8-27B: 21 min, 1 SVG | Frame 1: giant "21:00" with "One SVG." beneath, fully legible, rise-in-place motion onset inside 0.5 s on "21"; on "slow model" the timer flickers amber. | hyperframes | giant-number | 5 |
| s02 | foreshadow | Same weights, medium effort: seventy-seven seconds a question, same typical score. | 77 s/question, same typical score | On "seventy-seven seconds" the giant timer collapses into a small "77 s" chip; a score dial holds steady on "same typical score". | hyperframes | centered-stack | 4 |
| s03 | explain | Qwen three point eight gives thinking three stops: low, medium, x high. The chat template, the formatter behind every request, hands you the maximum when you set nothing. Generous. | Qwen3.8-27B: low · medium · xhigh | Three-stop dial builds on "three stops"; the template card stamps "xhigh" on "hands you the maximum"; wry beat lands on "Generous." | hyperframes | diagram-flow | 10 |
| s04 | explain | Set reasoning effort, the thinking-depth dial, to medium. The flag is only a suggestion; a budget is a hard stop: two thousand forty-eight thinking tokens. | cap: 2,048 tokens | Terminal-style config line types "reasoning_effort medium" on "set"; on "hard stop" a token meter slams against a 2,048 wall. | hyperframes | split-compare | 9 |
| s05 | explain | x high keeps the higher ceiling, and agent retries can eat the savings. Qwen says so itself. | ceiling: xhigh · savings: medium | Split on "higher ceiling": left xhigh with an up arrow, right medium with a draining token bar on "retries can eat the savings". | hyperframes | split-compare | 7 |
| s06 | payoff_close | Dwim resolved sixty-four percent against fifty-two, same model, same issues. You never bought a slow model; the dial shipped glued. | dwim 64% vs OpenCode 52% | Giant "64" on "sixty-four percent" settles against a smaller "52"; wordmark settle on "the dial shipped glued". | hyperframes | giant-number | 7 |

## Notes for review
- The "21 minutes / 22,276 reasoning tokens" pair is Willison's single SVG prompt (community tier, primary-adjacent); the script speaks only the minutes, the tokens live on screen in the hook frame as "21 min" and nowhere else. Check the referent if the hook frame is edited.
- "Same typical score" compresses llm-bench.io's 78.2 vs 78.8 median scores; the honest full form is in the brief (claim 4).
- s03 "Generous." is the one wry beat; if it reads as snark in review, cut it, the beat survives.
- The 2,048 cap is dwim's harness cap (penberg.org), not a Qwen model setting; oMLX users set thinking_budget_tokens instead. The script says "a budget is a hard stop" without claiming a model flag name.
