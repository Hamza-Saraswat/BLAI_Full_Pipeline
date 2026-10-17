---
slug: 2026-10-17-hy-memory-30b-a3b-a-30b-that-r
stage: 04-script
---

# Drafts: Hy-Memory-30B-A3B

## Draft A (news-react-so-what, hook number-shock) -- WINNER 21-18

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| s01 | hook | Eighteen gigabytes just beat Claude at remembering. Tencent's Hy-Memory has one job: writing what your assistant remembers. | 18 GB beats Claude at remembering | Frame 1 is finished and legible: giant amber "18 GB" centered in the 900x1160 safe area, white subline beneath, dark background. At 0.4 s the number scales up slightly while a thin amber underline rises under the subline, timed to "just beat Claude". Only these two elements move. | hyperframes | giant-number | 5 |
| s02 | explain | Your local model forgets you between chats. Frameworks like mem zero keep a memory bank, notes stored outside the model. | Mem0 keeps a memory bank outside the model | A chat-bubble icon labeled "your model" sits left of a notebook labeled "memory bank". On "forgets you between chats" the bubble fades to grey; on "notes stored outside the model" a dotted path rises from bubble to notebook. Entrances are fade and rise only, onset after 0.3 s. | hyperframes | diagram-flow | 7 |
| s03 | explain | A frontier model wrote those notes. Hy-Memory takes that job. It never chats; it decides what to keep and what to overwrite. | Hy-Memory-30B-A3B · never chats · keeps · overwrites | Short text chips rise one at a time in a centered stack: "frontier model wrote the notes", then "Hy-Memory takes the job", then "never chats". Stagger so at most two chips animate at once. The amber highlight lands on "Hy-Memory" exactly on "takes that job". | hyperframes | centered-stack | 7 |
| s04 | explain | On the memory tests it scores fifty-five point five percent. Claude Opus five scores fifty-four point six. | Hy-Memory 55.49% · Claude Opus 5 54.62% | Two horizontal bars scale from zero on "scores fifty-five point five percent": an amber bar to 55.49 labeled Hy-Memory, a grey bar to 54.62 labeled Claude Opus 5. The amber bar edges past grey precisely on "fifty-four point six". Both shown numbers are spoken in this scene. | manim | split-compare | 5 |
| s05 | explain | Catch: the scores are Tencent's own; half are statistical ties. The weights are free; that eighteen-gigabyte file runs tonight. | Tencent's own scores · half are statistical ties → 18 GB GGUF | A two-cell grid fades in on "the scores are Tencent's own": left cell reads "Tencent's own scores", right cell "half are statistical ties" over two equal mini-bars. On "the weights are free" the grid fades and a single file chip labeled "18 GB GGUF" rises, timed to "eighteen-gigabyte file runs tonight". | hyperframes | grid | 6 |
| s06 | payoff_close | Remembering stopped being a bigger brain. It's a small service beside the model you already run. | chat model + memory writer | On "stopped being a bigger brain" one large grey box fades out; on "small service beside the model you already run" two small boxes rise side by side, grey "chat model" and amber "memory writer". In the final 0.5 s the amber box settles into a centered wordmark, echoing the hook's amber-on-dark frame. | hyperframes | diagram-flow | 5 |

Word count: 113

## Draft B (worked-example, hook wrong-diagnosis)

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| s01 | hook | Your local model isn't forgetful. Its memory was never written. Yesterday you taught it your naming rules. | Your model isn't forgetful. Stamp: NEVER WRITTEN | Frame 1 is finished and legible: charcoal field, amber headline "Your model isn't forgetful." centered, beneath it a dim chat card showing the message "naming rules: snake_case". At 0.4 s the hollow amber stamp "NEVER WRITTEN" scales in over the card as "Its memory was never written" lands. On "Yesterday you taught it", the chat card fades to half brightness. | hyperframes | centered-stack | 5 |
| s02 | explain | Close the window, they are gone. What survives is a memory bank, a store outside your model. Mem Zero runs one, but a big model writes every entry. | memory bank: a store outside your model (later swaps to: big model writes every entry) | On "Close the window", the chat card fades out, its text lines dissolving upward. On "What survives is a memory bank", a database cylinder labeled "memory bank" rises in place right of the dead window, caption "a store outside your model" fading in beneath it. On "Mem Zero runs one", a "Mem0" chip fades onto the cylinder; on "a big model writes every entry", the caption swaps and a tall ghost card stamped "big model" fades in behind the cylinder. Only two elements move at once. | hyperframes | diagram-flow | 9 |
| s03 | explain | Tencent's Hy-Memory takes over that writing: what to keep, what to overwrite. It never chats. Thirty billion parameters sit loaded. Three billion wake per word. | Hy-Memory-30B-A3B · 30B loaded · 3B awake per word | On "Tencent's Hy-Memory", a model card titled "Hy-Memory-30B-A3B" rises in place at center, replacing the ghost card. On "It never chats", a crossed-out speech bubble fades in beside the card. On "Thirty billion parameters sit loaded" the chip "30B loaded" scales in, and on "Three billion wake per word" the chip "3B awake per word" scales in after it, amber on charcoal. | hyperframes | centered-stack | 8 |
| s04 | explain | On Tencent's own tests it scores fifty-five point four nine percent. Claude Opus Five scores fifty-four point six two percent. Nobody else has run them yet. | 55.49% · Opus 5: 54.62% · vendor matrix, unverified | On "fifty-five point four nine percent", "55.49%" counts up and settles giant in amber at center. On "Claude Opus Five scores", "Opus 5: 54.62%" fades in smaller beneath it. On "Nobody else has run them yet", the small tag "vendor matrix, unverified" fades in at top; nothing else moves. | manim | giant-number | 8 |
| s05 | payoff_close | It runs tonight from one eighteen-gigabyte file beside your chat model. Tomorrow, the naming rules are still there. | chat model + 18 GB GGUF; note: naming rules | Split frame: left card labeled "chat model", right a file card "18 GB · GGUF" that rises in place to sit level with it on "one eighteen-gigabyte file". On "Tomorrow, the naming rules are still there", the "naming rules" note from s01 fades into the file card. Final 0.5 s: the wordmark fades in centered, echoing s01's composition. | hyperframes | split-compare | 6 |

Word count: 114

## Judge report

WINNER: A

SCORES:
1 | A:3 B:1 | A: number + tension inside five words ("Eighteen gigabytes just beat Claude"); B names the topic but no product or number
2 | A:3 B:2 | A: the promised product and its job land by ~second 4; B's first concrete mechanism (memory bank) lands ~second 8
3 | A:3 B:1 | A: every beat earns its specific, one new number per sentence; B's "Nobody else has run them yet" speaks absence-of-evidence as assertion — finding 17 caps row 3 at 1
4 | A:3 B:3 | both clean second person with one dry beat that lands unexplained (A: "Catch:"; B: "Three billion wake per word")
5 | A:3 B:3 | no filler labels; transitions carry content and order is load-bearing (B's naming-rules plant in s01 pays off only in s05)
6 | A:1 B:3 | A repeats the number-shock opening (10-14) and the aphorism-reframe closing move of the recent run ("the api was never the model", "the unit of local ai is"); B brings a new opening rhythm (wrong-diagnosis), a callback landing, and a shape unlike the last two
7 | A:2 B:2 | each has exactly one line a viewer could repeat to a friend, but in both drafts that line is the hook, not the last thing heard
8 | A:3 B:3 | mechanism shown once, concretely, and predictive: A's viewer can infer any chat model pairs with a memory writer; B's viewer can infer why a 30B file runs at 3B cost

TOTALS: A=21 B=18

GRAFTS: none. B's hook scores lower on row 1, so no hook graft is permitted. B's strongest line ("Thirty billion parameters sit loaded. Three billion wake per word.") has no counterpart in A that A "says worse" — A never attempts the MoE point — and inserting it would add two numbers to A's budget and force rewrites around s03, which the grafting rules forbid.

LOSER-WHY: The worked-example needed a hook that stakes a product or number with tension in the first five words, and a first concrete payoff earlier than the memory-bank reveal at ~second 8. It also needed to hold the benchmark as attribution ("Tencent's own tests") without asserting the universal negative "Nobody else has run them yet," the exact drift finding 17 caps at 1 — that single sentence cost it the specificity row and the win.

Both drafts passed validator (0 blockers) and all eval gates before judging; B's sameness and hook_concrete gate failures were fixed pre-judging by pinning hook_pattern and adding the model name to frame-1 text.
