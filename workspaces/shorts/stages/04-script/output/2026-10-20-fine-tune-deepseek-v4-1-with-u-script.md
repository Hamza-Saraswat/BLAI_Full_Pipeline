---
slug: 2026-10-20-fine-tune-deepseek-v4-1-with-u
format: smooth-explainer
structure: news-react-so-what
style_pack: terminal
value_types: EQUIPS,TEACHES
promise: After forty-five seconds you know V4.1 runs locally but has no fine-tuning recipe yet, and you can run the stock Unsloth QLoRA flow tonight on a model that fits your card.
target_duration_s: 102
brief: 2026-10-20-fine-tune-deepseek-v4-1-with-u-brief.md
drafts: 2026-10-20-fine-tune-deepseek-v4-1-with-u-drafts.md
---

# DeepSeek V4.1 Runs Locally, but the Fine-Tune Did Not Ship

## Decisions
- Structures tried: how-to-three-moves (A) vs news-react-so-what (B); B won 22-16 (kimi-k3 judge). A's catch-first shape delayed its first hard number to ~13 s and dropped the 1-bit/Engram-on-SSD conditions off the 125 GB figure.
- Hook: candidate 2 family (number-shock) rewritten under gate pressure: "V four point one runs locally, about one hundred twenty-five gigabytes of memory." (13 words, pays by second 4). A took candidate 1 (tonight).
- Graft from A: the 3 GB VRAM floor sentence into B's s09 (judge-allowed, names the hardware floor B lacked).
- B's hook originally the 233 GB download; the spoken form "two-hundred-thirty-three-gigabyte" collides with the matcher's "three-gigabyte" token for the 3 GB row (a false 4th number); moved to 125 GB rather than pass on an artifact. 233 GB lives in the description.
- Editors after writers: A hook trimmed to 8 frame-1 words; B s03 number given its referent ("of memory"); "One bit per weight." cut (number cap); "It runs free on Colab" softened to "the free tier of Colab" (the docs page says free on Colab, Kaggle, or locally).
- style_pack terminal (topic fit 6 hits; previous signal). Structure rotation legal: last two were worked-example, myth-bust.
- Soft gates: entity_spend 0.32 and top2 present (advisories; extractor reads "DeepSeek"/"V4.1" as top-2 and both are present in B). Kept per soft-gate policy.

## Hook candidates
1. Three moves and your fine-tuned Llama runs tonight. *
2. The DeepSeek fine-tune you want sits on a two-hundred-thirty-three-gigabyte download. *
3. You watched DeepSeek V4.1 land. The fine-tune did not.
4. Unsloth shipped V4.1 support. Support means running.
5. Just 3GB of VRAM trains a model tonight.
6. Fifty-five-two billion parameters. About sixteen wake per word.
7. You want your own DeepSeek. Tonight you train Llama.
8. Your card can't fine-tune V4.1. Nothing can.
9. Yesterday's beta runs DeepSeek V4.1 in 125 GB.
10. Stop waiting for a V4.1 fine-tune that isn't coming.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | V four point one runs locally, about one hundred twenty-five gigabytes of memory. | V4.1 runs locally: about 125 GB | Dark frame, hook line centered in the safe area, legible from frame 1, type at least 64 px, amber on "125 GB". At 0.30 s the number does one subtle scale pulse. One text block animating, first and last 8 frames stable. | hyperframes | centered-stack | 3.1 |
| s02 | foreshadow | Yesterday, Unsloth shipped a beta whose headline is DeepSeek V four point one running locally. You watched it land wanting your own copy, fine-tuned, meaning retrained on your examples. | Unsloth beta: V4.1 runs locally | Hard cut to a sharp-corner terminal card centered above the caption band. Static header "unsloth / release". On "Yesterday" the line typewrites in, "V4.1" in amber. One text block animating, all else static. | hyperframes | timeline | 10.0 |
| s03 | explain | Here is what changes for you. Park the Engram table, a giant lookup memory, on your S S D. Then V four point one runs in about one hundred twenty-five gigabytes of memory. | Engram on SSD: about 125 GB | Hard cut to split-compare: left block labeled "SSD" (minor side, 3 chars), right memory bar. On "Park the Engram table" an amber slab fades onto the SSD; on "one hundred twenty-five gigabytes" the bar fades in with its label. One element animating per phrase. | manim | split-compare | 11.4 |
| s04 | explain | Picture a library. The Engram table is the basement archive; each word pages up only the rows it needs. The limit: the reading room alone still overflows any gaming card. | Library: archive in the basement | Manim line building with two floors, reading room above, basement archive below, sharp corners. On "pages up" a small row rises in place to the reading room; on "The limit" the reading room outline scales amber beside a tiny dim GPU box. At most two elements animating, phrase-anchored. | manim | diagram-flow | 10.3 |
| s05 | explain | The model holds five hundred fifty-two billion parameters. It is a mixture of experts: a router wakes only a few specialist blocks per word. And memory bills you for the whole model, not the slice that fires. | 552B parameters, few fire per word | Center stat "552B parameters" fades in, amber digits. On "router wakes" a few of many dim expert blocks fade amber; on "memory bills you" every block, lit and dim, takes an amber outline. One text block plus one block group animating. | manim | giant-number | 12.8 |
| s06 | foreshadow | Here is the honest part: in this release, support means running. No fine-tuning recipe, no notebook, no training checkpoint shipped for V four point one. | No V4.1 training recipe shipped | Hard cut to a sharp-corner release-notes panel. On each named absence, "recipe", "notebook", "checkpoint", a line typewrites in, then takes an amber strike-through. One text block animating, beats anchored to the list. | hyperframes | centered-stack | 8.6 |
| s07 | explain | Unsloth's own guide points its training advice at other models. V four point one even ships without a chat template, the rules that shape your prompts. Support, it turns out, is a spectator sport. | Guide: train other models. No chat template. | Doc-style card, sharp corners. On "training advice" the first line rises in place; on "chat template" a second line rises below it; on "spectator sport" both lines dim slightly. One block animating at a time, amber on key phrases. | hyperframes | timeline | 11.7 |
| s08 | explain | So tonight, run Unsloth's stock Q LoRA recipe. That is thin LoRA adapters trained on a four-bit compressed copy of a model that fits your card. | Stock QLoRA: load_in_4bit = True | Hard cut to a sharp-corner notebook cell. The flag typewrites in on "four-bit compressed copy"; on "fits your card" the cell border pulses amber once. One text block animating, code never shrunk below minimum type size. | hyperframes | centered-stack | 9.0 |
| s09 | explain | It runs on the free tier of Colab. The stock recipe fine-tunes with just three gigabytes of V RAM, your graphics card's memory. Load a four-bit Llama checkpoint and attach the adapters. Train on your question-and-answer dataset, save the adapter, and export to guff, the file Ollama runs. | Load, attach, train, export GGUF | Four sharp-corner step cards in a row. Each card rises in place as its verb is spoken, only one card animating at a time, amber border on the active card. On "guff" the last card gains its "GGUF" label. | hyperframes | grid | 16.6 |
| s10 | payoff_close | If a V four point one training path ever ships, this same recipe inherits it. Tonight, you train the model that fits your card. | Train what fits your card | Hard cut to a centered dark hero that mirrors frame 1. The line fades in on "Tonight", amber on "train", held above the caption band. Final 0.5 s: small wordmark settles below the line inside the safe area; last frame rhymes with frame 1. | hyperframes | centered-stack | 8.3 |

## Notes for review
- The 125 GB figure: verbatim is "about 125 GB of memory at 1-bit" with the Engram table on SSD; narration carries "about" and the SSD condition is in s03's preceding sentence. Check the ear keeps "about".
- "export to guff" is the spoken form of GGUF; captions should read GGUF.
- The graft sentence says "just three gigabytes of V RAM" -- the docs page says "just 3GB VRAM" for fine-tuning or RL on Colab, Kaggle, or locally; kept because the appositive defines VRAM for the beginner.
- s09 now runs ~17 s on paper (advisory): voice/render should split the beat at the graft sentence if it feels long.
