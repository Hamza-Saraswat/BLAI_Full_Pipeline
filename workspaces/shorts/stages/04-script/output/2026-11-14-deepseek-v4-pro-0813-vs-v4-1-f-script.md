---
slug: 2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f
format: smooth-explainer
structure: comparison-ladder
style_pack: halftone
value_types: EQUIPS,REFRAMES
promise: After this Short you can pick which DeepSeek to pull tonight, using the one number that decides it: the smallest file that fits your free memory.
target_duration_s: 107
brief: 2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f-brief.md
drafts: 2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f-drafts.md
---

# DeepSeek Pro 0813 or V4.1 Flash: the pull decision

## Decisions

- Structures tried: comparison-ladder (draft A, won 23/24) vs contrarian-take (draft B, 19/24); both cleared rotation (last two shipped: news-react-so-what, myth-bust). Unattended checkpoint: confirmed as picked.
- Hooks: 10 written, two kept from different patterns; A opens Decision ("Pro or Flash? One number decides"), B opens Number shock ("552B beat 1.6T"). Number shock was fine for B alone: it repeats 2026-11-10's ledger pattern and the judge docked B for it, not A.
- Grafts: none (hook tie at 3; both B candidate sentences would break A's number budget or import the drifted claim).
- Value delivery: EQUIPS is the s09 pull walk plus the closing rule ("your free memory picks the model"); REFRAMES is the s07 twist (the smaller pull is the quality pick on DeepSeek's own table).
- Payoff timing note: the hook names both products in sentence one (concrete at second 0); the first number lands at about second 6 in s02, inside the 5-8 s universal band.
- Style pack halftone via style_rotation.py --pick (topic fit; previous terminal).

## Hook candidates

1. Pro or Flash? One number decides. *
2. Eight hundred fifty gigabytes. Two hundred thirty-three. Pick.
3. The bigger DeepSeek is the wrong pull tonight.
4. The small DeepSeek beat the big one.
5. One is eight hundred fifty gigabytes. Guess which fits.
6. Same family, same week, one runs tonight.
7. You've got one hundred twenty-eight gigabytes. One of these fits.
8. DeepSeek shipped a giant. You can't hold it.
9. The flagships are on the shelf. Your drive decides.
10. Big model, small drive. The drive wins.

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Tonight it's DeepSeek Pro or Flash, and one number decides. | Pro or Flash? One number decides | Frame 1, fully legible: 1080x1920 halftone canvas split vertically into 'Pro' (left) and 'Flash' (right) columns flanking a thin divider, hook text 'Pro or Flash? One number decide... | hyperframes | split-compare | 3.4 |
| s02 | explain | You're picking between two DeepSeek downloads tonight. The Pro's smallest published file is eight hundred fifty gigabytes on disk. The Flash's smallest is two hundred thirty-three gigabytes on your drive. | Pro: smallest file 850 GB | Flash: smallest file 233 GB | Dark halftone field with a small drive icon top center. As narration says 'eight hundred fifty gigabytes', '850 GB' fades in giant under a 'Pro' label at center, well above 64 px. ... | hyperframes | giant-number | 10.3 |
| s03 | explain | Both are quantized, stored at lower precision to shrink the file. One file each. Both ship as a single-file build you can run tonight. Unsloth publishes them on Hugging Face, fully open weights. | Quantized: lower precision, smaller file | One file, runs tonight | GGUF from Unsloth on Hugging Face | Centered stack inside the safe area: a single document icon labeled 'GGUF' in amber mid-frame. On 'quantized, stored at lower precision', a small precision-dial glyph fades in abov... | hyperframes | centered-stack | 11.4 |
| s04 | explain | Each is a mixture of experts, a model that wakes only a slice of itself per word. Those active parameters, the slice that does the work, stay small. Every expert still has to sit on your drive or in your memory. | Mixture of experts | Active slice per word | Every expert still sits somewhere | Diagram: a 4x3 grid of rounded expert tiles right of center, one amber router node left, connected by thin static lines. On 'wakes only a slice of itself per word', two tiles brigh... | hyperframes | diagram-flow | 14.1 |
| s05 | explain | So what fits tonight? Drive streaming, pulling parts of the model from your fast drive into memory when they are needed, is the trick. On Unsloth's numbers, a big Spark-class machine holds the Flash. Nothing published yet holds the Pro. | SSD STREAMING | Flash: fits tonight | Pro: no published fit | Two columns return: 'Flash' left, 'Pro' right, beat text 'SSD STREAMING' top center. On 'pulling parts of the model from your fast drive into memory', small blocks rise in place fr... | hyperframes | split-compare | 13.8 |
| s06 | explain | Picture a master carpenter with a rolling tool chest. The daily tools ride inside; the rare ones fetch from the store across the street, your drive. Except a router inside the model picks per word, and the fetch costs seconds instead of a trip across town. | Rolling chest: daily tools | Rare tools fetch from the drive | Router picks per word | Halftone illustration center frame: a carpenter's rolling tool chest, top drawer open. On 'The daily tools ride inside', three small tools rise in place from the drawer. On 'the ra... | hyperframes | centered-stack | 15.9 |
| s07 | explain | Here's the twist. On DeepSeek's own table, the Flash scores ninety point six on the terminal bench, ahead of the Pro. The smaller pull is the quality pick for coding and agents, not the compromise. | DeepSeek's own table | Terminal-Bench: Flash 90.6 | Quality pick, not compromise | A table header fades in top center: 'DeepSeek's own table' with 'Terminal-Bench' beneath it. On 'ninety point six', '90.6' scales up giant in amber beside a tall Flash bar; a short... | hyperframes | giant-number | 12.1 |
| s08 | explain | The Pro still leads the world-knowledge rows, where its bigger backbone earns its keep. And if you ever rent these in DeepSeek's cloud, the Flash is the cheaper seat there too. | Knowledge rows: Pro leads | Coding rows: Flash leads | Cloud: Flash costs less | Split table in the safe area: rows labeled 'Knowledge' and 'Coding', columns 'Pro' and 'Flash'. On 'The Pro still leads the world-knowledge rows', an amber dot fades into the Pro c... | hyperframes | split-compare | 10.7 |
| s09 | explain | So tonight: count your free memory. Grab the Unsloth single-file build that fits. Run it in llama dot cpp or Unsloth Desktop. Let your drive hold the overflow. Set reasoning effort to trade speed against depth. | Count free memory | Pull the Unsloth GGUF that fits | llama.cpp + Unsloth Desktop | Drive holds overflow | Set reasoning effort | Horizontal timeline across the midline of the safe area with five ticks revealed left to right as narration lands each phrase. Each tick rises in place on its phrase: 'Count free m... | hyperframes | timeline | 12.4 |
| s10 | payoff_close | The rule to keep: your free memory picks the model. Tonight, it picks the Flash. | Your memory picks the model | Tonight: Flash | The two-column composition from frame 1 returns, rhyming with the hook: 'Pro' column dim, 'Flash' column lit amber. On 'your free memory picks the model', the beat text 'Your memor... | hyperframes | centered-stack | 5.2 |

## Notes for review

Number budget: exactly three spoken numbers (850 GB, 233 GB, 90.6); every on-screen digit is spoken in the same scene and beat. Because of this, (1) the Pro's Terminal-Bench 2.1 score of 87.9 appears only as an unlabeled shorter bar, and (2) the bench version digit '2.1' is omitted from screen text since it cannot be spoken; verify that showing 'Terminal-Bench' without the version is acceptable rather than misleading. 'Big Spark-class machine' stands in for Unsloth's 128GB+ RAM figure, which was outside the spoken-number budget. 'Nothing published yet holds the Pro' hedges against Unsloth's still-filling Pro GGUF repo. No tokens-per-second, MLX, or Ollama-local claims are made, per the unverified list. TTS check: 'llama dot cpp' should read as llama.cpp; adjust spelling if the voice mangles 'cpp'. All scenes avoid ALL-CAPS narration tokens (GGUF/SSD appear on screen only), no em dashes, no hype words, and only one 'not X' antithesis (s07).

- The judge's repeat-test line: "Your free memory picks the model."
- Rounded nothing: 850 GB / 233 GB / 90.6 are verbatim brief numbers, spoken in full words.
