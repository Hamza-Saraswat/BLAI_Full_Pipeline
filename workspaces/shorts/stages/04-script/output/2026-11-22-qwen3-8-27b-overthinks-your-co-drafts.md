# Drafts: 2026-11-22-qwen3-8-27b-overthinks-your-co

Judge: kimi-k3, blind to the writing; rubric per judge-rubric.md. Both drafts passed all machine gates before judging (validator zero blockers, eval zero failures).

## Draft A (how-to-three-moves, hook pattern: tonight)

Hook text: "3 moves. 21 minutes gone."

| Scene | Role | Narration | Est s |
|-------|------|-----------|-------|
| s01 | hook | Three moves and your coder stops stalling tonight. Twenty-one minutes thinking on one prompt: that's your local Qwen's factory default. | 7 |
| s02 | explain | Step one: set reasoning effort, the dial for how long it thinks, to medium. Qwen three point eight ships on x high, the maximum. Nobody asked it to. | 10 |
| s03 | explain | Step two: cap the thinking; the flag is only a suggestion. A budget is a hard stop: two thousand forty-eight reasoning tokens. | 8 |
| s04 | explain | Step three: paste the closing line. When the cap hits, it tells the model: act on the code already read. | 7 |
| s05 | payoff_close | Same model, same issues: sixty-four percent fixed instead of fifty-two, on a quarter of the thinking. It just writes the code. | 7 |

## Draft B (myth-bust, hook pattern: number-shock) -- WINNER

Hook text: "21 minutes. One SVG."

| Scene | Role | Narration | Est s |
|-------|------|-----------|-------|
| s01 | hook | Twenty-one minutes for one vector image. You run it locally for coding. So: slow model. | 5 |
| s02 | foreshadow | Same weights, medium effort: seventy-seven seconds a question, same typical score. | 4 |
| s03 | explain | Qwen three point eight gives thinking three stops: low, medium, x high. The chat template, the formatter behind every request, hands you the maximum when you set nothing. Generous. | 10 |
| s04 | explain | Set reasoning effort, the thinking-depth dial, to medium. The flag is only a suggestion; a budget is a hard stop: two thousand forty-eight thinking tokens. | 9 |
| s05 | explain | x high keeps the higher ceiling, and agent retries can eat the savings. Qwen says so itself. | 7 |
| s06 | payoff_close | Dwim resolved sixty-four percent against fifty-two, same model, same issues. You never bought a slow model; the dial shipped glued. | 7 |

## Score table

| Row | A | B | Note |
|-----|---|---|-------|
| 1 Hook | 2 | 3 | B names the number and the tension in five words; A's "three moves" is any how-to. |
| 2 Payoff timing | 2 | 3 | B lands the break (77 s, same score) by second 9 of 42 with the myth named at second 1; A pays at the close only. |
| 3 Specificity | 3 | 3 | Both spend numbers where they land; neither crams. |
| 4 Voice | 3 | 3 | Both clean, second person; B carries the "Generous." wry beat. |
| 5 Navigation | 2 | 3 | A's labels are legal but mechanical in places; B navigates purely by content. |
| 6 Difference | 1 | 2 | A repeats the 2026-11-19 how-to-three-moves/tonight combination; B differs in shape, opening and landing. |
| 7 Repeat test | 2 | 3 | B's "the dial shipped glued" is the repeatable line and the last thing heard. |
| 8 Teaching | 2 | 3 | B shows the mechanism (template default, soft flag, hard cap) so the viewer can predict new cases. |
| **Total** | **17** | **23** | |

## Grafts

1. "The flag is only a suggestion; a budget is a hard stop" from A into B's s04, replacing "Engines can ignore that, so add a hard cap". Reason: A states the soft-linkage vs hard-cap distinction in one repeatable line; the swap adds no numbers, keeps B's person and beat intact, and sets up s05's caveat.

## What the loser needed

A needed a shape that was not the identical how-to-three-moves/tonight combination aired three scripts ago, since repeating a recent structure capped its difference score before content was weighed. It also needed its best line at the end: "the flag is only a suggestion; a budget is a hard stop" was the repeatable payoff but it sat at step two, while the actual close ("It just writes the code") could have ended any video on this topic.
