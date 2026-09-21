---
slug: 2026-09-21-stop-paying-for-an-llm-judge
format: smooth-explainer
structure: worked-example
style_pack: signal
value_types: TEACHES,REFRAMES
promise: After this you can swap the per-token API judge in your eval loop for a small local decision model you run tonight, and know which verdicts must stay on the big model.
target_duration_s: 132
brief: 2026-09-21-stop-paying-for-an-llm-judge-brief.md
drafts: 2026-09-21-stop-paying-for-an-llm-judge-drafts.md
---

# Stop paying for an LLM judge

## Decisions
- Structures tried: worked-example (A, won twenty-one to twenty) and number-first (B). Rotation ruled out myth-bust (the pillar lane) and contrarian-take, the last two shipped shapes; the belief-busting job rides inside A's honest-catch beats instead.
- Hook: pick seven of ten, the price contrast "Same 500 verdicts: 34 cents or 28 dollars" (pattern price), the brief's most arresting number; B's writers' packet carried the named-contradiction pick so the drafts could not converge.
- Grafts from B: the calibration definition into the forward-pass scene; "The nightly sample retires." into the accuracy scene. Judge's reasons are in the drafts note.
- Gates: validator zero blockers zero advisories; eval nine gates pass (number spend two heard, entity and top-two soft gates pass, positional labels three legal action labels); variety check ok against the last five.
- Value lines: TEACHES on "Probabilities come out in a single forward pass... Calibrated means the score matches how often it is actually right."; REFRAMES on "The judge stopped being a bill and became a download."

## Hook candidates
1. Thirty-four cents or twenty-eight dollars, for the same 500 judgments
2. Kev-4B judges your agent, from 9 GB of your GPU
3. Stop renting a lawyer to sort your eval mail
4. Your eval bill is 92x too noisy, and too high
5. You pay per word for a verdict that is one bit
6. The judge does not need to write an essay
7. Same 500 verdicts: 34 cents or 28 dollars *
8. Cut your judge bill by 98.8 percent tonight
9. The judge flips when you swap two answers
10. Five hundred verdicts, thirty-four cents, local

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s1 | hook | You score your agent's traces with a frontier API judge. Every verdict bills per token. Five hundred verdicts: thirty-four cents, or twenty-eight dollars for Claude. | Same 500 verdicts: 34 cents or 28 dollars | Frame 1 composition: dark slate backdrop, the full hook line 'Same 500 verdicts: 34 cents or 28 dollars' centered in the safe area, '34 cents' in amber, everything else off-white. Motion onset at t=0.30s: the amber '34 cents' scales up a touch. On 'writes each verdict token by token' a thin invoice underline fades in. On 'twenty-eight dollars for Claude' the right-hand figure rises in place. Fade and scale only, two elements animating at most. | hyperframes | giant-number | 8.6 |
| s2 | explain | Look at what that bill buys. The judge, a GPT or Claude model, returns a paragraph of reasoning. Plus a JSON blob, a block of structured fields. Your software keeps a single label. The rest is generated and billed anyway. | GPT judge: paragraph + JSON | your code keeps: a label | On 'paragraph of reasoning' a gray text card fades in center, stacked with dummy prose lines. On 'JSON blob' a second card rises beneath it with amber braces and field rows. On 'keeps a single label' both cards dim except one amber label chip, which scales up. On 'generated and billed anyway' the dimmed blocks fade out, leaving only the chip centered. One text block at a time; entrances are fade and rise-in-place. | hyperframes | centered-stack | 13.8 |
| s3 | foreshadow | Generation brings friends. Re-score the identical trace and the verdict can drift. Swap the order of the answers and the winner can flip. That flaw is position bias. | same trace, new score | swap order, flip winner | position bias | Two verdict cards fade in side by side on 'Re-score the identical trace'. On 'the verdict can drift' the right card's badge ticks from PASS to a wobbling near-miss shade. On 'Swap the order of the answers' the two answer rows trade places by rising and settling, never sliding from an edge. On 'the winner can flip' the amber check mark hops rows. On 'position bias' a small caption fades in below. | manim | split-compare | 9.3 |
| s4 | foreshadow | A decision model is a different shape of thing. State and typed questions go in. Probabilities come out in a single forward pass, a straight trip through the network. Calibrated means the score matches how often it is actually right. Nothing gets written. | state + questions in | probabilities out, single pass | calibrated: score matches reality | Diagram draws on 'state and typed questions go in': an input node on the left with two labeled arrows entering. On 'probabilities come out', three probability bars scale upward on the right. On 'nothing gets written', the output side shows one node and no text stream. Amber accent on the output bars only; motion starts at frame nine. | manim | diagram-flow | 14.8 |
| s5 | explain | Your API judge is a courtroom lawyer, billing by the word for an opinion on every envelope. The decision model is the mail sorter, circling the routing slip at a glance. | lawyer bills by the word | sorter circles the slip | Split screen on 'courtroom lawyer, billing by the word': left panel a formal opinion document with a ticking word counter, right panel a plain routing slip. On 'circling the routing slip', an amber circle draws around one label on the slip. Hard cut between panels; counter ticks on 'every envelope'. | hyperframes | split-compare | 10.7 |
| s6 | explain | Kev four B is that sorter with open weights and an Apache license. A LoRA adapter, a small set of trainable weights on a frozen Qwen base. It serves from about nine gigabytes of GPU memory. On your own card, no API key, no meter running. | Kev-4B = LoRA adapter on Qwen base | open weights, Apache license | ~9 GB GPU memory | On 'Kev four B' the product wordmark fades in center. On 'LoRA adapter' a thin amber adapter ring scales in around a frozen gray base block labeled Qwen. On 'about nine gigabytes of GPU memory' a vertical memory meter fills to a notch labeled '~9 GB'. On 'no API key, no meter running' a key icon and a coin meter fade out together. Stacked, centered, fade and scale entrances only. | hyperframes | centered-stack | 15.9 |
| s7 | explain | Step one: clone the repository and install the server. Step two: start the judge locally with the serve command. Step three: send each trace as state plus typed questions, then read back a probability per question. | uv sync --extra serve | python -m kev.serve | state + questions -> probability | A vertical timeline of three nodes fades in, each node lighting amber as its step is spoken. On 'clone the repository' a terminal card shows 'uv sync --extra serve'; on 'start the judge locally' the card text swaps to 'python -m kev.serve'; on 'state plus typed questions' a chip reading 'state + questions' fades in beside an arrow ending at 'probability'. Only one card's text changes at a time; all entrances are fades. | hyperframes | timeline | 12.8 |
| s8 | explain | Out of domain means question families it never trained on. On that locked suite, Kev four B scores zero point eight three two. Tooling is catching up, so judging every trace inside the agent loop stops being a luxury. The nightly sample retires. | locked out-of-domain suite | Kev-4B: 0.832 | the nightly sample retires | On 'locked suite' a padlocked test-suite card fades in behind the frame. On 'zero point eight three two' the giant amber figure '0.832' scales in center under a small 'Kev-4B' label. On 'Tooling is catching up' a small request chip rises at the bottom; on 'inside the agent loop' a thin loop arrow draws itself around the chip. Two animations maximum at once, no slides. | hyperframes | giant-number | 14.8 |
| s9 | explain | Here is the honest catch. You could call Kev a classifier dressed up as a judge. Date arithmetic and broad knowledge still go to the big model. | the fair objection | dates + knowledge go big | On 'honest catch' the screen splits: left panel 'stays local', right panel 'big model keeps'. On 'classifier dressed up as a judge', a small card rises on the left. On 'date arithmetic and broad knowledge', two chips rise into the right panel with amber outlines. | hyperframes | split-compare | 8.6 |
| s10 | explain | It trails by a wide margin there. Date arithmetic still trips it, where its hosted sibling Jev scores higher. The sorter cannot write an opinion at all, so reasoned critique goes back to the lawyer. | not calibrated off home turf | critique goes to the lawyer | A two by two grid fades in on 'wide margin': cells for dates, knowledge, confidence, critique. On 'not calibrated', the confidence cell's meter needle wavers. On 'goes back to the lawyer', the critique cell dims and a gavel icon rises in place. Amber on the wavering meter only. | manim | grid | 12.1 |
| s11 | payoff_close | So tonight the same suite runs again. Every verdict comes back from Kev, on your own GPU, identical on every rerun. The judge stopped being a bill and became a download. | same suite tonight | no per-token bill | On 'the same suite runs again' the frame-1 invoice card fades back in, same layout as the hook, but the total line stays blank. On 'from your own GPU' a small GPU chip icon pulses amber. On 'identical on every rerun' two matching check marks rise in place. On 'became a download' the card folds into a download-arrow badge. Final half second: channel wordmark settles center, visual only. Last frame rhymes with frame 1. | hyperframes | centered-stack | 10.7 |

## Notes for review
- The five hundred verdicts number is LangChain's measurement of hosted Jev against Claude Sonnet; the video says "for Claude" and never claims we measured it. Nothing here has run on our own hardware yet.
- Accuracy is spoken as zero point eight three two, Kev four B on the author's frozen out-of-domain suite; self-reported, hedged by "on that locked suite".
- The lawyer-and-mail-sorter analogy states its limit in the honest-catch scene: the sorter cannot write an opinion, so reasoned critique goes back to the lawyer.
- The three on-screen numbers ($0.34 vs $28.17, 0.832, 9 GB) are each spoken in their own scene, one at a time.
