# Drafts: 2026-11-24-nariq-a-27b-at-3-bits-in-10-gb

Two blind drafts on kimi-k3, judged blind on kimi-k3 per judge-rubric.md.

## Score table

row 1 Hook: A=3 B=1 -- A lands "twenty-seven billion" plus the felt "would not fit" pain in the opening breath; B's "Your card isn't too small" has tension but no product or number in the first five words. row 2 Payoff timing: A=3 B=2 -- A's promised concrete (27B didn't fit, numbers attached) lands by second 4; B's first hard number (fifty-three gigabytes) doesn't arrive until about second 7. row 3 Specificity without cramming: A=2 B=2 -- A mostly spends one number per sentence but crams four-days/three-bit/27B/10.12 into the news beat; B is disciplined except the triple-stack "One file, one benchmark family, four days old." Neither drifts an Unverified claim into assertion. row 4 Voice: A=3 B=3 -- Both clean second person with glosses folded into apposition and the dry "grading its own homework" beat landing unexplained. row 5 Navigation: A=2 B=3 -- B's pivots each name the turn ("Here is the evidence against it," "Who should stay put?") and the order is locked; A's mechanism and score scenes could swap without breaking, and "The fine print:" is a bare signpost. row 6 Difference: A=2 B=3 -- A reuses the news-react-so-what shape from three scripts back; B's contrarian-take, paradox opening rhythm, and question-swap landing are all absent from the recent run. row 7 The repeat test: A=2 B=3 -- B's last thing heard is a standalone quotable line; A's last words ("It was whether your memory could hold it") are a fragment that only works attached to its setup. row 8 Teaching: A=2 B=3 -- B shows why this quant holds (trellis errors cancel, calibrated on the model's own agent tokens), so a viewer can predict the next calibration-matched quant; A shows bits-as-size concretely but never explains why this 3-bit escaped the old failure mode.

Total: A=19 B=20. Winner: draft B.

## Grafts
Move A's opening sentence, "You downloaded a twenty-seven billion parameter model and it would not fit," to the top of B's first scene, before "Your card isn't too small." Allowed because the loser's hook scores 3 against the winner's 1 (at least 2 higher), it is a single sentence, it is the same second person, scene one's heard numbers go from two to three which sits at the cap, and the named-contradiction still lands inside scene one so B's contrarian spine and its "card was never the problem" callback stay intact. LOSER_NEEDS: A reported the scores without the mechanism that explains them -- the trellis coding and agent-trace calibration -- so it could teach bits-as-size but never why this quant broke the 3-bit curse. It also needed a payoff that stands alone as one quotable sentence, on a shape and a wall-callback landing the recent run hadn't already spent. REPEAT_LINE: The only question left is what memory you have.

## Loser needs
A reported the scores without the mechanism that explains them -- the trellis coding and agent-trace calibration -- so it could teach bits-as-size but never why this quant broke the 3-bit curse. It also needed a payoff that stands alone as one quotable sentence, on a shape and a wall-callback landing the recent run hadn't already spent. REPEAT_LINE: The only question left is what memory you have.

## Repeat line (winner)
The only question left is what memory you have.

### Draft A -- news-react-so-what (hook pattern situation)

Narration:
  s01 (hook, giant-number, 13.4s): You downloaded a twenty-seven billion parameter model and it would not fit. Your card isn't too small. The file is. The full-precision original of the model you gave up on needs about fifty-three gigabytes. Your card holds twelve gigabytes.
  s02 (explain, centered-stack, 12.8s): Everyone running local models learned the rule. Quantization, fewer bits per stored number, always costs quality. Below four bits a model is supposed to fall apart. A twenty-seven billion parameter model is supposed to need a workstation.
  s03 (explain, split-compare, 20.7s): Here is the evidence against it. NariQ is a three-bit compression of Qwen3.8-27B, built by Nari Labs. The GGUF, the single file your local tools load, is ten point one two gigabytes. On DeepSWE, a benchmark of real software tasks, it scored forty-one against the original's thirty-nine point eight. Every earlier attempt at or below three bits fell further behind.
  s04 (explain, diagram-flow, 25.0s): Why does it hold up? The original stores every parameter, each a stored number, in BF16, the model's full sixteen-bit memory. Quantization rounds each number down to three bits. Picture rounding pi from five decimal places to three point one. Close enough for most work; exact math notices first, casual chat never does. NariQ's twist is trellis coding, choosing which numbers to flatten together so the rounding errors cancel instead of stacking. It was tuned on tokens the full model wrote during real agent sessions.
  s05 (explain, timeline, 11.7s): Now the narrower claim this earns. One file, one benchmark family, four days old. Every quality number comes from the publisher's own tests, so the only referee so far is grading its own homework.
  s06 (explain, grid, 18.6s): Stock llama.cpp, the engine under the usual local tools, cannot load the file yet. Neither can Ollama or LM Studio; you would need the Nari Labs fork. That fork is slower than stock quants, the usual compressed files, on most hardware, with one exception, a workstation-class GPU. Support in stock tools has no date.
  s07 (foreshadow, split-compare, 13.1s): Who should stay put? If you need the last fraction of a point, or long exact math, stay on BF16. If your card is a GeForce, the publisher says it plainly: GeForce cards have not been tested yet.
  s08 (payoff_close, centered-stack, 11.4s): The card was never the problem, and three bits was never the real question. The old question was whether three bits is good enough. The only question left is what memory you have.

On-screen:
  s01: Not the card. The file. | 53.8 GB full file | 12 GB your card
  s02: quantization costs quality | under 4 bits falls apart | 27B params need a workstation
  s03: NariQ 3-bit GGUF | 10.12 GB | DeepSWE 41.0 vs 39.8
  s04: BF16: full memory | quant: 3 bits | pi: 5 decimals to 3.1 | trellis: errors cancel
  s05: 1 file | 1 benchmark family | 4 days old | scores self-graded
  s06: stock llama.cpp cannot load | Ollama, LM Studio: no | Nari Labs fork required | slower except 1 workstation GPU
  s07: need the last fraction? stay on BF16 | GeForce cards: not tested yet
  s08: old question: is 3 bits enough? | new question: what memory do you have?

### Draft B -- contrarian-take (hook pattern named-contradiction)

Narration:
  s01 (hook, giant-number, 11.7s): You downloaded a twenty-seven billion parameter model and it would not fit. The file at full precision is about fifty-three gigabytes. Your card holds twelve gigabytes of memory. That gap is the whole story.
  s02 (explain, centered-stack, 12.8s): Four days ago, Nari Labs posted NariQ, a three-bit compression of Qwen3.8-27B, the Qwen model with twenty-seven billion parameters. The download is a single GGUF, the file format llama.cpp reads. It is ten point one two gigabytes.
  s03 (explain, diagram-flow, 22.4s): At three bits, the whole model fits the card you already own. The trick is quantization, keeping fewer bits for each stored number. BF16, the model's full sixteen-bit memory, drops to three bits per number. That is about one-fifth the storage. Think of rounding pi for homework: fewer digits, same answer. But the loss is not uniform: exact math notices first, casual chat never does.
  s04 (explain, split-compare, 15.2s): Does the smaller file still think? DeepSWE, a benchmark where an agent solves real software tasks, has the answer. The three-bit file scored forty-one points on it. The full-precision original scored thirty-nine point eight. The small file did not just survive; it edged ahead.
  s05 (explain, centered-stack, 13.4s): Now the catch, spoken plainly: those scores are the publisher grading its own homework. Nari Labs ran those tests in a fork, its own modified copy of llama.cpp. The release has one author and it is four days old.
  s06 (explain, grid, 18.3s): The fine print: the fork is tuned for workstation cards, the professional kind. On everything except one workstation card, it runs slower than ordinary compressed files. GeForce cards have not been tested yet. Stock llama.cpp will not even load the file. Any tokens-per-second number, the speed of the replies, is folklore this week.
  s07 (explain, diagram-flow, 13.1s): Tonight, check your free memory before you download anything, not your benchmark sheet. The file needs room, and so does the KV cache, the model's thinking memory. If both fit, tonight you run a twenty-seven billion parameter model.
  s08 (payoff_close, centered-stack, 8.6s): Remember the wall at that download screen. The wall was never whether the model was smart enough. It was whether your memory could hold it.

On-screen:
  s01: 53.8 GB file | 12 GB card | it would not fit
  s02: NariQ, 4 days ago | Qwen3.8-27B at 3 bits | 10.12 GB GGUF
  s03: 16 bits to 3 bits | ~1/5 the storage | rounding pi
  s04: DeepSWE coding benchmark | 41.0 vs 39.8 | 3-bit edges ahead
  s05: publisher's own harness | its own llama.cpp fork | 1 author, 4 days old
  s06: tuned: workstation GPUs | slower except 1 workstation GPU | GeForce: not tested | stock llama.cpp can't load it
  s07: check free VRAM | file + KV cache | you run the 27B tonight
  s08: not intelligence | it was memory

