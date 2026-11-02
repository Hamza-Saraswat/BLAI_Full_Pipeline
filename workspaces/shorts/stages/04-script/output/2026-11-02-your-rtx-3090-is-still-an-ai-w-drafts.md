---
slug: 2026-11-02-your-rtx-3090-is-still-an-ai-w
stage: 04-script
generated_at: 2026-11-02
---

# Drafts and judge record: RTX 3090 Still Runs Local AI: The One Spec That Decides What Fits

Both drafts passed every machine gate before judging (validator zero blockers, eval exit 0, three key numbers heard, sameness clean). Draft A wrote number-first, draft B story-first, from separate blind packets on Kimi K3.

### Draft A (number-first, hook pattern number-shock, target 105s)

- **s01 (hook)** Thirteen and a half million opinions, read by a GPU six years old. Every AI video since twenty twenty-three has called your RTX thirty ninety obsolete.  
  - On screen: 13,576,547 opinions. One old GPU. / 6 YEARS OLD / OBSOLETE?
- **s02 (explain)** Those opinions came from Reddit and Hacker News threads, millions of owners arguing about gear. A builder fed them through a Gemma model into a site called Trust Me Bro Reviews. It ranks products, places and tools by what real owners said, shills filtered out.  
  - On screen: Reddit + Hacker News / Trust Me Bro Reviews / shills filtered out / products · places · tools
- **s03 (explain)** That job ran in a basement on pairs of RTX thirty nineties, a card released in twenty twenty. Each pair is joined by NVLink, a direct cable between two GPUs. The internet's verdict says you need a forty ninety or fifty ninety for local AI.  
  - On screen: pairs of RTX 3090s / NVLink: direct cable, 2 GPUs / 2020 / you need a 4090 or 5090
- **s04 (explain)** One spec decides what fits: VRAM, the memory on the card itself. A model fits only if its weights fit inside that memory. Your thirty ninety carries twenty-four gigabytes of memory, the same capacity a forty ninety carries.  
  - On screen: VRAM = memory on the card / RTX 3090 · 24 GB / RTX 4090 · 24 GB / same capacity
- **s05 (explain)** A benchmark called llama-bench ran a twenty-seven-billion-parameter Qwen model on one thirty ninety. Quantization shrank the weights to fewer bits so it fits, at small cost. It generates nearly forty tokens a second, about reading speed.  
  - On screen: llama-bench · Qwen3.6 27B / quantized: fewer bits per weight / 39.878 tokens/s / single RTX 3090
- **s06 (explain)** Here's the honest catch. A forty ninety is faster on sixteen-bit math. It also carries dedicated hardware for an eight-bit number format your card will never get. The biggest open models barely fit on one card and crawl.  
  - On screen: THE HONEST CATCH / 16-bit math: 4090 faster / FP8 hardware: none on 3090 / giant models barely fit, then crawl
- **s07 (explain)** Your thirty ninety also drinks more power, and its memory bandwidth, how fast it reads its own memory, lags newer boards. That's the honest tax on older silicon. The tax never touches capacity, the spec that decides what you're allowed to run.  
  - On screen: 3090 vs newer boards: power / the honest tax / CAPACITY / decides what you can run
- **s08 (payoff_close)** Capacity was the spec everyone skipped. Your thirty ninety matches a forty ninety there, so your card still runs what the new card runs. Obsolete meant not enough memory, and memory was never the problem.  
  - On screen: capacity decides what runs / 3090 = 4090 on capacity / Obsolete meant not enough memory / Memory was never the problem.

### Draft B (story-first, hook pattern case, target 95s)

- **s01 (hook)** A guy in a basement ranked half the internet's product advice. The cards are pairs of thirty nineties from twenty twenty. The same card sits in your tower.  
  - On screen: A basement. Pairs of 3090s.
- **s02 (explain)** His site is called Trust Me Bro Reviews. It reads Reddit and Hacker News opinions, filters out the shills and fake praise, and ranks what people actually love. Thirteen and a half million opinions became a ranked list of products, places and tools.  
  - On screen: Trust Me Bro Reviews / Reddit + Hacker News / 13,576,547 opinions ranked
- **s03 (foreshadow)** His cards are RTX thirty nineties, a generation the internet loves to bury. Every AI video lately has called that card obsolete, too old and too slow for local models. The comments said buy a newer card or go home.  
  - On screen: RTX 3090 / obsolete? / too old / too slow
- **s04 (explain)** Here is what actually ran in that basement. Pairs of thirty nineties, joined by NVLink, a direct cable that links one card straight to another. vLLM, an open-source serving engine, fed a Gemma mixture-of-experts model, many specialists with a few awake per word.  
  - On screen: 3090 + 3090 / NVLink / vLLM / Gemma MoE
- **s05 (explain)** What decides what runs on your card is VRAM, the memory on the card itself. If a model fits inside it, the model runs. Your thirty ninety carries twenty-four gigabytes of memory. The newer card carries the same.  
  - On screen: 3090: 24 GB / 4090: 24 GB / same capacity
- **s06 (explain)** The honest wall is real. A seventy-billion-parameter LLaMA squeezes into that memory, then crawls slower than reading speed. Tokens are word-pieces, the chunks a model speaks in. His giant job also ran on pairs, never one card.  
  - On screen: giant models: slower than reading
- **s07 (explain)** The newer card is faster, with built-in hardware for a compact number format yours will never get. Picture an old pickup: same bed as the new truck, same loads, more fuel, no turbo. It breaks when the load outgrows the bed.  
  - On screen: FP8: newer hardware / same bed / more fuel / no turbo
- **s08 (payoff_close)** One spec decides what fits, and on that spec your card still matches. Obsolete meant not enough memory, and yours never had that problem. It's old, not obsolete.  
  - On screen: old, not obsolete / Build Local AI

## Scores (judge on Kimi K3, rubric 0-3 per row)

| Row | A | B |
|-----|---|---|
| hook | 3 | 2 |
| payoff_timing | 1 | 1 |
| specificity | 1 | 3 |
| voice | 3 | 3 |
| navigation | 3 | 3 |
| difference | 3 | 3 |
| repeat_test | 3 | 3 |
| teaching | 3 | 3 |
| **Total** | **20** | **21** |

**Winner: draft B** (21 to 20).

Reason: A's hook ('13,576,547 opinions. One old GPU' / 'read by a GPU six years old') implies one card ran the marquee job, which is exactly the drift the brief forbids; that caps A's specificity at 1 and costs it the win. B holds the pairs qualifier in every scene that touches the basement job (s01, s04, s06), stays inside the number budget with only two key figures, and matches A on voice, navigation, difference, repeat and teaching.

## Grafts

None.

## What the losing shape would have needed

A needed its hook to keep the number-shock while saying 'pairs of old GPUs' instead of 'one old GPU' — the singular card was the entire two-point margin via the specificity cap. Its mid-script reveal gave it no timing advantage over B to compensate, and 'nearly forty tokens a second, about reading speed' also undersold its own best benchmark.
