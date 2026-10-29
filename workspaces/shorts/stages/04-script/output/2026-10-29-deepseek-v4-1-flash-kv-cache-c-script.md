---
slug: 2026-10-29-deepseek-v4-1-flash-kv-cache-c
format: classic
structure: myth-bust
style_pack: signal
value_types: TEACHES,EQUIPS
promise: After this Short you can tell trained-in KV cache compression apart from a runtime flag, and you know where llama.cpp's cache flags still help.
target_duration_s: 38
brief: 2026-10-29-deepseek-v4-1-flash-kv-cache-c-brief.md
drafts: 2026-10-29-deepseek-v4-1-flash-kv-cache-c-drafts.md
---

# KV cache compression isn't a flag

## Decisions
- Structures tried: number-first (A) and myth-bust (B); B won 22-20 on the judge rubric (rows 1, 6, 8 decided it: hook tension in the first five words, shape further from the 10-26 number-shock open, and teaching that transfers to the next model). No grafts: the loser's hook scored lower on row 1, and its wry beat could not move without breaking the voice cap.
- Hook: "Your flag isn't the trick." (wrong-diagnosis pattern, scored 5/7; number-shock "Eight hundred ninety bytes per token." went to draft A). Both picks clear the last two ledger hook patterns (tonight, other).
- Checkpoints passed unattended: structures/promise confirmed before drafting; 10 hooks written, two picks from different patterns.
- Gates: validator 0 blockers (advisory: 0 keyword tags, filled by stage 05); eval all nine gates pass (number_spend 3 rows / 3 heard; entity gates pass); sameness clean vs last five; variety check ok. Sentence-stretch warning on draft A only; winner clean.

## Hook candidates
1. Eight hundred ninety bytes per token. (number-shock, went to draft A)
2. DeepSeek just made context nearly free.
3. Your chat memory isn't the model. It's the notes.
4. One million tokens. One tiny note each.
5. Four hundred thirty-seven times smaller notes.
6. Your memory fills. The notes did it.
7. DeepSeek's cache shrank four hundred thirty-seven times.
8. Stop blaming the model. Blame its notes.
9. Eight hundred ninety bytes. A whole context.
10. The flag isn't the compression. The model is.
11. * Your flag isn't the trick. The training is. (wrong-diagnosis, pick, draft B)

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s1 | hook | Your flag isn't the trick. The training is. DeepSeek's new cache bill: eight hundred ninety bytes per token. | 890 BYTES PER TOKEN | YOUR FLAG ISN'T THE TRICK | Frame 1: dark signal grid, amber flag outline upper center, text 'YOUR FLAG ISN'T THE TRICK' fully legible at frame 1. Motion onset 0.35s: the flag outline fades out. On 'The train | hyperframes | giant-number | 6.6 |
| s2 | explain | The belief: compression is a switch. Set a flag, shrink the KV cache, the running notes kept per token, to four-bit. | THE MYTH | SET A FLAG, GET 4-BIT | NOTES PER TOKEN | Frame 1: centered card labeled 'THE MYTH'. Motion onset 0.3s on 'The belief': the card brightens. On 'Set a flag' an amber toggle flips on below the card and 'SET A FLAG, GET 4-BIT | hyperframes | centered-stack | 7.2 |
| s3 | explain | The truth: DeepSeek trained it into the weights. No switch involved. Layers share one set of notes, each stored four-bit from training. Per-token cache drops about four hundred thirty-seven-fold versus DeepSeek V one. | TRAINED IN, NOT TOGGLED | LAYERS SHARE ONE PAD | 437x vs V1 | Frame 1: three horizontal layer bars stacked. Motion onset 0.35s on 'The truth': header 'TRAINED IN, NOT TOGGLED' fades in. On 'Layers share one set of notes' the three bars conver | hyperframes | diagram-flow | 11.0 |
| s4 | explain | The myth still half works. llama.cpp's cache flags still shrink notes on models you run. On DeepSeek, quantizing the key half of that cache once gave confident gibberish on every backend. | Q8_0 still shrinks notes | DEEPSEEK K: GIBBERISH | Frame 1: empty split panels. Motion onset 0.35s on 'The myth still half works': left panel fills with flags '-CTK -CTV Q8_0' fading in over a shrinking note pad, captioned 'Q8_0 st | hyperframes | split-compare | 10.7 |
| s5 | payoff_close | Your flag nudges the cache. The training rebuilt it. | FLAG NUDGES | TRAINING REBUILDS | Frame 1: two short amber rules centered. Motion onset 0.3s on 'Your flag nudges': 'FLAG NUDGES' rises in place by the first rule. On 'The training rebuilt it' 'TRAINING REBUILDS' s | hyperframes | centered-stack | 3.1 |

## Notes for review
- The 437-fold line is spoken as a drop "versus DeepSeek V one" so the referent is unambiguous; on screen it is "437x vs V1".
- The gibberish beat is historical: the bug was fixed July 2026; "once gave" carries that.
- "q8_0" is never spoken; narration says "cache flags" and the flag names live on screen only.
- Draft A's one-million-token beat was not grafted; if the human wants the 1M context number, it belongs in the description or a follow-up.
