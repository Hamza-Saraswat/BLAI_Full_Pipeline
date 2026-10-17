---
slug: 2026-10-17-hy-memory-30b-a3b-a-30b-that-r
format: classic
structure: news-react-so-what
style_pack: terminal
value_types: TEACHES,REFRAMES
promise: after half a minute the viewer can say what Hy-Memory-30B-A3B is, why it is not a chat model, and that it runs tonight from an eighteen-gigabyte file
target_duration_s: 36
brief: 2026-10-17-hy-memory-30b-a3b-a-30b-that-r-brief.md
drafts: 2026-10-17-hy-memory-30b-a3b-a-30b-that-r-drafts.md
---

# Hy-Memory-30B-A3B: a 30B that remembers

## Decisions
- Structures tried: news-react-so-what (draft A) vs worked-example (draft B); A won 21-18 on the judge rubric (hook, payoff timing and specificity rows; B's "Nobody else has run them yet" was a finding-17 drift). No grafts.
- Hook: number-shock "Eighteen gigabytes just beat Claude at remembering." (candidate 1); B's wrong-diagnosis hook kept as candidate 2 for the record.
- Gates: validator 0 blockers 0 advisories (FK 6.0 warning kept: "statistical" and "parameters" are load-bearing, rephrasing them dumbs down the mechanism); eval all gates pass (entity_spend and top2 advisory by design); normalizer scenes_changed 0.
- Value lines: TEACHES = s03 "It never chats; it decides what to keep and what to overwrite." REFRAMES = s06 payoff "Remembering stopped being a bigger brain. It's a small service beside the model you already run."

## Hook candidates
1. Eighteen gigabytes just beat Claude at remembering. *
2. Your model isn't forgetful. Its memory was never written.
3. Tencent shipped a model that only remembers.
4. Fifty-five point four nine beats fifty-four point six two.
5. You chat. It forgets. That was the whole problem.
6. Hy-Memory-30B-A3B: the 30B that never talks to you.
7. A three-billion-active model just matched Claude's memory.
8. Stop paying Claude to take notes.
9. Your local model needs a secretary, not a bigger brain.
10. Thirty billion parameters for one job: remembering.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Eighteen gigabytes just beat Claude at remembering. Tencent's Hy-Memory has one job. It writes what your assistant remembers. | 18 GB beats Claude at remembering | Frame 1 finished and legible; motion onset at 0.4 s: the number scales up. Frame 1 is finished and legible: giant amber "18 GB" centered in the 900x1160 safe area, white subline beneath, dark background. At 0.4 s the number scales up slightly while a thin amber underline rises under the subline, timed to "just beat Claude". Only these two elements move. | hyperframes | giant-number | 5.6 |
| s02 | explain | Your local model forgets you between chats. Frameworks like mem zero keep a memory bank, notes stored outside the model. | Mem0 keeps a bank / outside the model | A chat-bubble icon labeled "your model" sits left of a notebook labeled "memory bank". On "forgets you between chats" the bubble fades to grey; on "notes stored outside the model" a dotted path rises from bubble to notebook. Entrances are fade and rise only, onset after 0.3 s. | hyperframes | diagram-flow | 6.2 |
| s03 | explain | A frontier model wrote those notes. Hy-Memory takes that job. It never chats; it decides what to keep and what to overwrite. | frontier wrote notes / Hy-Memory takes over / never chats | Short text chips rise one at a time in a centered stack: "frontier model wrote the notes", then "Hy-Memory takes the job", then "never chats". Stagger so at most two chips animate at once. The amber highlight lands on "Hy-Memory" exactly on "takes that job". | hyperframes | centered-stack | 6.9 |
| s04 | explain | On the memory tests it scores fifty-five point five percent. Claude Opus five scores fifty-four point six. | Hy-Memory 55.49% / Claude Opus 5 54.62% | Two horizontal bars scale from zero on "scores fifty-five point five percent": an amber bar to 55.49 labeled Hy-Memory, a grey bar to 54.62 labeled Claude Opus 5. The amber bar edges past grey precisely on "fifty-four point six". Both shown numbers are spoken in this scene. | manim | split-compare | 5.3 |
| s05 | explain | Catch: the scores are Tencent's own. Half are statistical ties. The weights are free; that eighteen-gigabyte file runs tonight. | Tencent's own scores / half are ties / 18 GB GGUF | A two-cell grid fades in on "the scores are Tencent's own": left cell reads "Tencent's own scores", right cell "half are statistical ties" over two equal mini-bars. On "the weights are free" the grid fades and a single file chip labeled "18 GB GGUF" rises, timed to "eighteen-gigabyte file runs tonight". | hyperframes | grid | 5.9 |
| s06 | payoff_close | Remembering stopped being a bigger brain. It's a small service beside the model you already run. | chat model + memory writer | On "stopped being a bigger brain" one large grey box fades out; on "small service beside the model you already run" two small boxes rise side by side, grey "chat model" and amber "memory writer". In the final 0.5 s the amber box settles into a centered wordmark, echoing the hook's amber-on-dark frame. | hyperframes | diagram-flow | 5.0 |

## Notes for review
- The hook's "eighteen gigabytes" is the Q4_K_M GGUF size (brief key number 6, 18.237 GB decimal); "beat Claude" is the 55.49% vs 54.62% macro average on Tencent's own 20% subsample matrix, hedged in s05.
- s05 says "half are statistical ties": two of four harnesses (60.55 vs 60.53; 50.51 vs 50.50), per claim 10.
- "Mem zero" is the spoken form of Mem0; it is a memory framework, not a Tencent product.
- FK grade 6.0 kept above the 5 target; the words that lift it are the mechanism's own names.
