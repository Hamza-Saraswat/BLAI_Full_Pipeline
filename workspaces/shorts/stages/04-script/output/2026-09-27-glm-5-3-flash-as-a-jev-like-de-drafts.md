---
slug: 2026-09-27-glm-5-3-flash-as-a-jev-like-de
stage: 04-script
generated_at: 2026-09-27
---

# Drafts and judge: 2026-09-27-glm-5-3-flash-as-a-jev-like-de

Both drafts passed validator (0 blockers) and eval gates after one fix round each; A's fix round dropped a fourth
heard number and lifted scene specificity, B's dropped the memory-number match and split a 17 s scene.

## Draft A (myth-bust, 106 s)
| Scene | Role | Narration | On-screen text | Est s |
|-------|------|-----------|----------------|-------|
| s01 | hook | GLM Flash just matched a model built only for decisions. | A generalist just tied the specialist | 3.5 |
| s02 | explain | Across twenty-eight public text datasets, the median gap was zero point seven percentage points in Jev's favor. Your routing calls are decisions just like this one. | 0.7 points, median gap | 9.5 |
| s03 | explain | The myth says those calls need a purpose-built model, a specialist you rent by the decision. Jev is that pro, a decision model, one that takes your state plus named options and returns a typed choice. | Myth: routing needs a purpose-built pro | 12.5 |
| s04 | explain | The myth had evidence. Ask an ordinary model to route, and it writes a whole JSON object. A reasoning model thinks for hundreds of tokens first. Neither says how sure it is. | JSON out, confidence nowhere | 10.5 |
| s05 | explain | Your software knows the answer's shape, so it numbers the options and ends the prompt at the first answer token. Think of a multiple-choice sheet with 'answer' pre-printed, except yours reads full state and can hold over a hundred options. | number the options / end the prompt early | 14.0 |
| s06 | explain | Then it masks the vocabulary, the model's whole word list, down to those option numbers. One forward pass, a single run of the model, returns each option's log probabilities, raw scores you normalize into shares. No fine-tuning, the model exactly as it ships. | one token, every option scored | 15.0 |
| s07 | explain | The library behind this is open source. It speaks to any vLLM endpoint, the engine that serves models behind an OpenAI-style API. | MIT-licensed, any vLLM endpoint | 7.5 |
| s08 | explain | Hosted, the myth still wins on price. A million decisions cost about sixty-two euros with hosted GLM Flash, about sixteen with Jev, at list prices. | EUR 62 vs EUR 16 / per million decisions | 8.5 |
| s09 | explain | That parity was measured on the hosted model, not your local quant, a lower-precision copy that shrinks the file. | measured hosted, not your quant | 6.5 |
| s10 | explain | At home, the math flips. GLM Flash is open weights, and its smallest quant fits a big-memory machine. The Mac or big-RAM box already under your desk. | fits the machine you own | 9.5 |
| s11 | payoff_close | Your routing calls stop being a metered bill and become electricity. And the decider on your desk reads the scanned documents Jev cannot touch at all. | calls become electricity / reads scans Jev can't | 9.0 |

## Draft B (comparison-ladder, 105 s) -- WINNER
| Scene | Role | Narration | On-screen text | Est s |
|-------|------|-----------|----------------|-------|
| s01 | hook | Jev or a free model? Let the ladder decide. Your agent pipeline is full of calls that just pick: route this ticket, choose that tool. | Jev or a free model? / Let the ladder decide | 8.5 |
| s02 | explain | The axis of this ladder: who makes your routing decisions, and where. Meet Jev, a hosted decision API that takes your state plus named options and returns a typed choice with probabilities. | who decides, and where | 11.0 |
| s03 | explain | Meet GLM Flash, an open model built to write prose. The trick is refusing to let it answer in words. Think multiple-choice answer sheet, not essay, except this sheet still reads your full state first. | essay / answer sheet | 12.0 |
| s04 | explain | Your software numbers the options and ends the prompt where the answer begins. It masks the vocabulary, narrowing the next token to those numbers. | options numbered / prompt ends early | 9.5 |
| s05 | explain | Then it reads one token's log probabilities, the raw scores, in a single forward pass, one model run. Every option gets a probability, no fine-tuning. | one pass, every option scored | 8.5 |
| s06 | explain | Start with accuracy. Across twenty-eight text datasets, the median gap is zero point seven percentage points in Jev's favor. They split the wins, ten datasets each, and it is not statistically significant. | 0.7 / median gap, Jev's favor | 11.5 |
| s07 | explain | Climb to cost. Per million decisions, hosted GLM Flash costs about sixty-two euros, Jev about sixteen. The hosted ladder favors Jev. | 62 vs 16 / € per million decisions | 7.5 |
| s08 | explain | Serve GLM Flash on your own machine and the bill drops to zero. Its smallest quant, a shrunken lower-precision copy, fits a big-memory box. One caveat: parity was measured on the hosted model, not on your quant. | zero euros, at home / parity: hosted only | 13.0 |
| s09 | explain | Now what each one cannot do. Jev reads text only: no images, no audio, no video. GLM Flash reads the scanned document, at seventy point two percent on sixteen hundred business documents. Jev cannot answer there at all. | Jev: text only / GLM-5.3-Flash: reads scans | 13.0 |
| s10 | payoff_close | Your routing calls stop being a metered bill and become electricity. The rule: rent Jev for plain text at scale, decide at home for images, privacy, or a zero bill. | text at scale → Jev / images, privacy, zero → home | 10.5 |

## Judge output (kimi-k3, verbatim)

SCORES:
row 1: A=3 B=3
row 2: A=2 B=2
row 3: A=3 B=3
row 4: A=3 B=3
row 5: A=3 B=2
row 6: A=3 B=3
row 7: A=2 B=3
row 8: A=3 B=3
total A=22 B=22

WINNER: draft B — totals and row 6 both tie, so the slot goes to the draft whose last sound is its repeatable payoff: B's decision rule lands final, quantified (seventy point two percent on sixteen hundred scanned documents) and reusable, in five fewer seconds, while A buries its best line under a kicker and leaves the scan claim qualitative.

GRAFTS: A's closing line "Your routing calls stop being a metered bill and become electricity." moves into B's payoff scene as the setup sentence before the rule; legal because B states the same at-home economics flatter ("the bill drops to zero"), the sentence adds no numbers, keeps second person, requires no rewriting of the surrounding beat, and leaves B's rule as the last line heard.

LOSER-NOTES: The myth-bust spent roughly twenty seconds (s03-s04) restating a belief its own 3.5-second hook had already busted, time the winner spent on evidence and the capability boundary instead. To win, it needed its one great line, "become electricity," as the final sound rather than penultimate under the scan kicker, and a hard number behind that scan claim.

## Post-judge
The graft was applied to scene 10 of draft B exactly as the judge allowed; gates re-run clean
(validator 0/0, eval failures none). Ledger entry recorded; style pack axon recorded.
