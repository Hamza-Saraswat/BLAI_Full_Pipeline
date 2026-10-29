---
slug: 2026-10-29-deepseek-v4-1-flash-kv-cache-c
stage: 04-script
generated_at: 2026-10-29T13:20:00Z
winner: B (myth-bust) 22-20 over A (number-first)
---

# Drafts: 2026-10-29-deepseek-v4-1-flash-kv-cache-c

Both drafts passed the machine gates before judging (validator 0 blockers; all nine eval gates; sameness clean against the last five ledger entries).

## Draft A (number-first)

# Draft: 890 Bytes a Token

## Promise
You can tell whether a big cache number is trained into the model or available as a flag, and what eight hundred ninety bytes per token means for long chats on your own machine.

## Scenes
| id | role | narration | on_screen_text | visual_brief | layout_archetype | est_duration_s |
|-----|------|-----------|----------------|--------------|------------------|----------------|
| s1 | hook | Eight hundred ninety bytes per token. That's what DeepSeek V4.1 Flash pays, in memory, to remember each token of your longest chat. | 890 bytes per token \| + V4.1-Flash KV cache | Frame 1: near-black field, faint amber oscilloscope grid, giant amber "890" centered with "bytes per token" beneath. At ~0.4s on "Eight hundred ninety bytes", a thin amber baseline rises under the digits. On "That's what DeepSeek V4.1 Flash pays", the label "V4.1-Flash KV cache" fades in below. On "your longest chat", a row of tiny token ticks fades in along the baseline. | giant-number | 6.9 |
| s2 | explain | That bill is the KV cache, the running notes a model keeps on every token it reads. DeepSeek V1 spent about four hundred thirty-seven times more bytes on every token. | notes per token \| V1 vs V4.1-Flash: 437x | Frame 1: screen split, left header "V1", right "V4.1-Flash", faint amber center line. On "That bill is the KV cache", the strip "notes per token" fades in top center. On "DeepSeek V1 spent", a tall stack of amber note-cards rises in place on the left. On "four hundred thirty-seven times more", a "437x" badge scales in at center, then one small note-card fades in on the right. | split-compare | 10.3 |
| s3 | explain | No flag gets you this number. The model did the homework in training. Layers share one set of notes, written in FP4, a four-bit number format. | no flag does this \| one shared pad FP4 4-bit | Frame 1: three dim horizontal layer bars at left, one empty pad outline at right. On "No flag gets you this number", the caption "no flag does this" fades in top. On "did the homework in training", the three bars brighten. On "share one set of notes", thin connectors fade in from each bar to the single pad. On "FP4, a four-bit number format", the pad label "FP4 4-bit" scales in. | diagram-flow | 9.3 |
| s4 | foreshadow | So the notes for a chat one million tokens long stop eating your memory. | 1M-token chat notes stay small | Frame 1: horizontal amber chat timeline with growing token ticks, small memory bar beneath. On "a chat one million tokens long", the end tick "1M tokens" scales in at the right. On "stop eating your memory", the memory bar pulses once and stays small while "notes stay small" fades in. | timeline | 4.8 |
| s5 | payoff_close | The notes were always the bill, and DeepSeek just made them cheap. | BUILD LOCAL AI | Frame 1: the single amber note-pad, centered on black. On "The notes were always the bill", the pad scales down to one thin amber line. On "DeepSeek just made them cheap", the line settles and the "BUILD LOCAL AI" wordmark rises gently into place. | centered-stack | 4.1 |

## Value lines
- TEACHES: The KV cache is the running notes a model keeps on every token it reads, and DeepSeek V4.1 Flash trained that cost down to eight hundred ninety bytes per token, about four hundred thirty-seven times less than V1.
- EQUIPS: No flag gets you this number, so you can now separate the compression trained into the weights from the smaller runtime cache-type lever when you judge any model's long-chat memory bill.

## Wry beat
"The model did the homework in training." (s3)

## Draft B (myth-bust, winner)

# Draft: Your Flag Isn't the Trick

## Promise
You can tell trained-in KV cache compression apart from a runtime flag, and you know exactly where your q8_0 cache flags still help and where they once broke a DeepSeek model.

## Scenes
| id | role | narration | on_screen_text | visual_brief | layout_archetype | est_duration_s |
|-----|------|-----------|----------------|--------------|------------------|----------------|
| s1 | hook | Your flag isn't the trick. The training is. Eight hundred ninety bytes of cache per token on DeepSeek's V4.1 Flash. | YOUR FLAG ISN'T THE TRICK \| THE TRAINING IS \| 890 BYTES PER TOKEN | Frame-1: dark signal grid, amber flag outline, text "YOUR FLAG ISN'T THE TRICK". Flag fades at 0.35s. On "The training is." the line "THE TRAINING IS." rises in place beneath. On "Eight hundred ninety bytes" a giant amber "890" scales up with "BYTES PER TOKEN" under it. On "DeepSeek's V4.1 Flash" a small tag "DEEPSEEK V4.1 FLASH" fades in under the number. | giant-number | 7.2 |
| s2 | explain | The belief: compression is a switch. Set a flag, shrink the KV cache, the running notes kept per token, to four-bit. | THE MYTH \| SET A FLAG → 4-BIT \| RUNNING NOTES PER TOKEN | Frame-1: centered card labeled "THE MYTH", fading in at 0.3s on "The belief". On "Set a flag" an amber toggle flips on below the card. Card and toggle fade as "SET A FLAG → 4-BIT" appears on "Set a flag". On "the KV cache" a pad of sticky notes rises in center, labeled "RUNNING NOTES PER TOKEN". On "to four-bit" the pad scales down to quarter size. | centered-stack | 7.2 |
| s3 | explain | The truth: DeepSeek trained it into the weights. Layers share one set of notes, each stored four-bit from training. Versus V1, per-token cache drops about four hundred thirty-seven-fold. | TRAINED IN, NOT TOGGLED \| LAYERS SHARE ONE PAD \| ≈437-FOLD VS V1 | Frame-1: three horizontal layer bars stacked. Header "TRAINED IN, NOT TOGGLED" fades in at 0.35s on "The truth". On "Layers share one set of notes" the three bars converge in place into one shared note pad. On "four-bit from training" the pad is stamped "STORED 4-BIT FROM TRAINING". Header and stamp fade as "≈437-FOLD VS V1" scales up on "four hundred thirty-seven-fold". | diagram-flow | 9.7 |
| s4 | explain | The myth still half works. llama.cpp's q8_0 flags shrink notes on models you run. On DeepSeek, quantizing one half of that cache once gave confident gibberish on every backend. | Q8_0: STILL SHRINKS NOTES \| DEEPSEEK K: CONFIDENT GIBBERISH | Frame-1: empty split panels. Left panel fills at 0.35s on "The myth still half works": flags "-CTK -CTV Q8_0" fade in over a shrinking note pad, captioned "Q8_0: STILL SHRINKS NOTES". On "On DeepSeek" the right panel rises: a note pad whose glyphs scramble, captioned "DEEPSEEK K: CONFIDENT GIBBERISH". Left caption fades as right caption lands. | split-compare | 10.0 |
| s5 | payoff_close | Your flag nudges the cache. The training rebuilt it. | FLAG NUDGES. \| TRAINING REBUILDS IT. | Frame-1: two short amber rules centered. "FLAG NUDGES." rises in place at 0.3s on "Your flag nudges the cache". "TRAINING REBUILDS IT." scales in on "The training rebuilt it". Both hold as the "BUILD LOCAL AI" wordmark fades in below and settles. | centered-stack | 3.1 |

## Value lines
- TEACHES: DeepSeek V4.1 Flash hits eight hundred ninety bytes of cache per token because layers share one set of notes and store them four-bit from training, a roughly four hundred thirty-seven-fold drop versus V1 that no flag can copy.
- EQUIPS: Keep using llama.cpp's -ctk/-ctv q8_0 flags to shrink the cache on models you already run, knowing they are a separate smaller lever and that quantizing the K half once produced gibberish on DeepSeek.

## Wry beat
s4: "On DeepSeek, quantizing one half of that cache once gave confident gibberish on every backend." The dryness lands on the bug, not the viewer.

## Judge score table

| # | Row | A | B |
|---|-----|---|---|
| 1 | Hook | 2 | 3 |
| 2 | Payoff timing | 3 | 2 |
| 3 | Specificity | 3 | 3 |
| 4 | Voice | 3 | 3 |
| 5 | Navigation | 3 | 3 |
| 6 | Difference | 1 | 2 |
| 7 | Repeat test | 3 | 3 |
| 8 | Teaching | 2 | 3 |
| | **Total** | **20** | **22** |

Row notes: B's first five words carry a tension the flag-running viewer feels and the number completes the hook (row 1). A pays its promise by second two (row 2; B timed from the break lands around second five, inside eight, not four). Row 6: A repeats the 10-26 giant-number cold open and mid-thirties duration; B differs from both of the last two shipped scripts in structure, opening rhythm and landing. Row 8: B teaches what flags still do and where they once broke, so the viewer can predict the next model's cache behavior.

## Grafts

None. The loser's hook scored lower on row 1, not two points higher. A's wry beat could not move (B already carries its one permitted wry beat). A's one-million-token sentence would have needed a new scene and a rewritten payoff turn.

## What the losing shape needed

Number-first needed the figure to arrive with tension attached inside the first five words, not a bare number the second sentence has to rescue, and an opening rhythm that does not rhyme with the 10-26 number-shock hook. It also needed to say what the flag still does, the usable lever, so its teaching transfers to the next model the viewer benchmarks.
