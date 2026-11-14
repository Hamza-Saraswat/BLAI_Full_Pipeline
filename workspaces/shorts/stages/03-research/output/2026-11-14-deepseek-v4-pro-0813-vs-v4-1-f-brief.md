---
slug: 2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f
stage: 03-research
topic: "DeepSeek V4 Pro 0813 vs V4.1 Flash: which one you pull for local hardware"
depth: standard
generated_at: 2026-11-14T12:41:38Z
sources: 10
hub: "[[videos/2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f]]"
---

# Research brief: DeepSeek V4 Pro 0813 vs V4.1 Flash, which one you pull for local hardware

## Summary
Tonight's pull is DeepSeek-V4.1-Flash, specifically the 1017 update, not the headline V4 Pro 0813. The number that decides it is disk and memory, not parameters: the smallest Flash GGUF is 233 GB and Unsloth says it runs on a 128GB+ RAM device, while the smallest Pro quant published so far is 850 GB. The strongest concrete case: on DeepSeek's own table the 552B-backbone Flash beats the 1.6T Pro on Terminal-Bench 2.1 (90.6 vs 87.9) and DeepSWE v1.1 (74.2 vs 62.7), so the small model is the quality pick for coding and agents. Not verified: any local tokens-per-second figure (community numbers with no method shown), native Mac MLX builds, and whether Ollama can pull these weights locally. One conflict to flag: sources disagree on the Pro's size (1.6T in DeepSeek's own table and Artificial Analysis, 1.57T from Unsloth, 1.7T on the Hugging Face sidebar), and the 2026-11-14 Hacker News thread showed 24 points in the Algolia record but 22 on the page itself.

## Thesis
For running DeepSeek at home tonight, pull V4.1 Flash, not V4 Pro: the 552B Flash beats the 1.6T Pro on the coding-agent benchmarks local users actually run, and its 233 GB smallest download fits a 128 GB machine with SSD streaming, while the Pro's smallest published file is 850 GB.

## Explanation path
The viewer already knows how to download a model, so the video names both candidates immediately and puts the deciding gap on screen: DeepSeek-V4-Pro-0813 against DeepSeek-V4.1-Flash-1017, with their smallest real downloads, 850 GB and 233 GB. Parameters alone would predict a blowout, so the video unpacks mixture-of-experts: total parameters are everything the model knows, active parameters are what any single token touches, and the catch for hardware is that every expert still has to sit on your disk or in your memory. That makes the memory story concrete: SSD offloading is what lets a 128 GB machine hold the 233 GB Flash, and nothing published lets it hold the Pro. Quality arrives as the twist rather than the concession: DeepSeek's own tables put the Flash ahead of the Pro on Terminal-Bench 2.1 and DeepSWE v1.1, and Artificial Analysis ranks Flash 1017 near the top of its Intelligence Index while the Pro sits mid-pack, so the smaller pull is the better coding and agent model, not the budget one. The Pro's territory shows up in the world-knowledge rows of the same tables, where its larger backbone still leads, and that is where the video can be honest about what the Flash gives up. API prices close the loop for anyone comparing against the cloud: DeepSeek's own pricing page charges $0.3 in / $1.2 out per million tokens for the Flash at peak against $1.32 / $3.96 for the Pro. The payoff is the pick and the pull: check free memory, choose the quant that fits, download the Unsloth GGUF, run it in llama.cpp or Unsloth Desktop with the Engram offloaded to SSD, and set reasoning effort to trade speed against depth.

## Claims
1. **DeepSeek-V4-Pro-0813 is the official release of DeepSeek-V4-Pro, superseding the preview, with weights on Hugging Face under the MIT License.**
   - Source: deepseek-ai/DeepSeek-V4-Pro-0813, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813
   - Tier: primary | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "DeepSeek-V4-Pro-0813 is the official release of DeepSeek-V4-Pro, superseding the preview version" ... "This repository and the model weights are licensed under the MIT License."
2. **DeepSeek V4 Pro 0813 has 1.6T parameters (49B active) and a context window of 1M tokens.**
   - Source: DeepSeek V4 Pro 0813 Models - Artificial Analysis, https://artificialanalysis.ai/models/deepseek-v4-pro
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "DeepSeek V4 Pro 0813 has 1.6T parameters (49B active)." ... "DeepSeek V4 Pro 0813 has a context window of 1M tokens."
3. **DeepSeek-V4.1-Flash is a multimodal Mixture-of-Experts model with 552B backbone parameters plus a 196B-parameter Engram memory, activating 8B parameters per token during prefill and 16B during decode, with contexts of up to one million tokens, under the MIT License.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters and support for contexts of up to one million tokens" ... "activate only 8B parameters per token during prefill and 16B during decode" ... "Engram conditional memory (196B parameters, sparsely accessed via token-based lookup)"
4. **On DeepSeek's own comparison table, DeepSeek-V4.1-Flash outscores DeepSeek-V4-Pro on Terminal-Bench 2.1 (90.6 vs 87.9 Pass@1) and on DeepSWE v1.1 (74.2 vs 62.7 Resolved).**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "Terminal-Bench 2.1 (Pass@1) | 89.1 | 88.8 | 88.3 | 88.2 | 87.9 | 82.7 | 90.6" and "DeepSWE v1.1 (Resolved) | 74.0 | 73.0 | 67.5 | 66.9 | 62.7 | 54.4 | 74.2" (columns in order: Opus-5.0, GPT-5.6 Sol, K3, GLM-5.3, DS-V4-Pro, DS-V4-Flash, DS-V4.1-Flash)
5. **On the Artificial Analysis Intelligence Index, DeepSeek V4.1 Flash 1017 (Max) scores 33, well above the comparable-model median of 23.**
   - Source: DeepSeek V4.1 Flash 1017 Models - Artificial Analysis, https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "DeepSeek V4.1 Flash 1017 (Max) scores 33 on the Artificial Analysis Intelligence Index, placing it well above average among comparable models (median: 23)."
6. **On the same Artificial Analysis Intelligence Index, DeepSeek V4 Pro 0813 (Max) scores 23.**
   - Source: DeepSeek V4 Pro 0813 Models - Artificial Analysis, https://artificialanalysis.ai/models/deepseek-v4-pro
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "DeepSeek V4 Pro 0813 achieves a score of 23 (max), 21 (high), and 13 (non-reasoning) on the Artificial Analysis Intelligence Index."
7. **The smallest DeepSeek-V4-Pro-0813 GGUF quant Unsloth has published is UD-Q4_K_XL at 850 GB, and Unsloth states the model needs substantially more memory than the Flash family.**
   - Source: unsloth/DeepSeek-V4-Pro-0813-GGUF, https://huggingface.co/unsloth/DeepSeek-V4-Pro-0813-GGUF
   - Tier: docs | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "UD-Q4_K_XL 850 GB" ... "DeepSeek-V4-Pro-0813 is a 1.57T parameter model with 48B active parameters per token, so it needs substantially more memory than DeepSeek-V4-Flash-0731." ... "Quants are uploaded to this repository as they finish converting."
8. **The smallest DeepSeek-V4.1-Flash-1017 GGUF quant from Unsloth is UD-IQ1_S at 233 GB, which Unsloth says runs on a 128GB+ RAM device, with 3-bit on 256GB and full precision on 320GB.**
   - Source: unsloth/DeepSeek-V4.1-Flash-1017-GGUF, https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF
   - Tier: docs | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "UD-IQ1_S 233 GB" ... "Run on a 128GB+ RAM device for the smallest 1-bit, 3-bit on 256GB or full precision on 320GB."
9. **On DeepSeek's official pricing page, deepseek-flash (model version DeepSeek-V4.1-Flash-1017) peak pricing is $0.3 per 1M input tokens (cache miss) and $1.2 per 1M output tokens, while deepseek-v4-pro peak pricing is $1.32 and $3.96, and off-peak rates are half of peak.**
   - Source: Models & Pricing | DeepSeek API Docs, https://api-docs.deepseek.com/quick_start/pricing/
   - Tier: primary | Confidence: high | Accessed: 2026-11-14 | Via: web_extract
   - Quote: "1M INPUT TOKENS (CACHE MISS) | OFF-PEAK | $0.15 | $0.66 | PEAK | $0.3 | $1.32" and "1M OUTPUT TOKENS | OFF-PEAK | $0.6 | $1.98 | PEAK | $1.2 | $3.96" (columns in order: deepseek-flash, deepseek-v4-pro) ... "Off-peak rates are half of the peak rates."
10. **DeepSeek-V4-Pro-0813 hit Hacker News on the morning of 2026-11-14: a thread posted at 2026-11-14T00:50:33Z linking the Hugging Face model card had 24 points by 11:58 UTC in the Algolia record.**
    - Source: HN Algolia search API (DeepSeek stories, 2026-11-14), https://hn.algolia.com/api/v1/search_by_date?query=deepseek&tags=story&numericFilters=created_at_i%3E1794489600&hitsPerPage=30
    - Tier: community | Confidence: medium | Accessed: 2026-11-14 | Via: web_extract
    - Quote: "created_at":"2026-11-14T00:50:33Z","created_at_i":1794617433,"num_comments":1,"objectID":"50492302","points":24,"title":"DeepSeek V4 Pro 0813","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | V4 Pro 0813 total / active parameters | 1.6T parameters (49B active) | https://artificialanalysis.ai/models/deepseek-v4-pro | "DeepSeek V4 Pro 0813 has 1.6T parameters (49B active)." |
| 2 | V4.1-Flash backbone parameters | 552B backbone parameters | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "552B backbone parameters and support for contexts of up to one million tokens" |
| 3 | V4.1-Flash activated parameters per token (prefill / decode) | 8B / 16B | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "activate only 8B parameters per token during prefill and 16B during decode" |
| 4 | V4.1-Flash global KV cache footprint per token | 890 bytes per token | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "reduce the global KV cache footprint to 890 bytes per token" |
| 5 | Smallest V4.1-Flash-1017 GGUF (UD-IQ1_S, Unsloth) | 233 GB | https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF | "UD-IQ1_S 233 GB" |
| 6 | Smallest V4-Pro-0813 GGUF published (UD-Q4_K_XL, Unsloth) | 850 GB | https://huggingface.co/unsloth/DeepSeek-V4-Pro-0813-GGUF | "UD-Q4_K_XL 850 GB" |
| 7 | deepseek-flash (V4.1-Flash-1017) peak API price, input (cache miss) / output per 1M tokens | $0.3 / $1.2 | https://api-docs.deepseek.com/quick_start/pricing/ | "PEAK | $0.3 | $1.32" and "PEAK | $1.2 | $3.96" |
| 8 | deepseek-v4-pro peak API price, input (cache miss) / output per 1M tokens | $1.32 / $3.96 | https://api-docs.deepseek.com/quick_start/pricing/ | "PEAK | $0.3 | $1.32" and "PEAK | $1.2 | $3.96" |

## Analogy candidates
- **Workshop vs rolling tool chest**: The Pro is a full cabinet-making workshop, every specialist machine installed on site (850 GB before you start); the Flash is a master carpenter whose rolling chest (233 GB) holds the tools used constantly while the rare ones get fetched from the hardware store across the street (your SSD). Breaks when: experts are not chosen consciously the way a carpenter picks a tool; a router inside the model decides per token, and the fetch from SSD costs seconds of speed, not a drive across town.
- **Iceberg**: The 8B / 16B active parameters are the tip you see working on each token; the whole 552B backbone plus the 196B Engram is the mass that still has to be in RAM or streamed from disk. Breaks when: it suggests the submerged mass is dead weight; every expert takes its turn depending on the question, so the whole iceberg matters to quality.

## Misconceptions
- Myth: The model with more parameters is automatically the better pull, so 1.6T beats 552B. Reality: DeepSeek's own table scores the 552B-backbone Flash above the 1.6T Pro on Terminal-Bench 2.1 (90.6 vs 87.9) and DeepSWE v1.1 (74.2 vs 62.7) (claim 4).
- Myth: If only 8B / 16B parameters are active per token, you only need enough memory for that. Reality: all 552B backbone parameters plus the 196B Engram must be on your disk and in RAM or streamed from SSD, so even the smallest Flash file is 233 GB (claims 3, 8).
- Myth: The Pro 0813 weights dropped this morning. Reality: Artificial Analysis dates the V4 Pro 0813 release to August 2026; what happened on 2026-11-14 is a Hacker News thread about the model, not a new weight drop (claims 2, 10).

## Glossary
- **Mixture-of-Experts (MoE)**: a model architecture that keeps many specialist sub-networks (experts) and routes each token through only a few of them.
- **Active parameters**: the subset of a model's weights that actually processes any single token, as opposed to the total stored on disk.
- **Quantization**: storing model weights at lower numeric precision to shrink the file, trading some accuracy for size.
- **GGUF**: the single-file model format that runtimes like llama.cpp, LM Studio and Ollama load.
- **KV cache**: the memory a model keeps of everything it has already read in a conversation so it does not recompute it.
- **Tokens per second**: how fast a model generates text on your hardware.
- **SSD offloading / SSD streaming**: keeping parts of the model on your fast drive and reading them into memory only when needed.
- **Engram**: DeepSeek's name for the V4.1-Flash's conditional memory module, 196B parameters accessed sparsely by lookup.
- **DSpark speculative decoding**: a small draft model guesses several tokens ahead and the big model verifies them in one pass, speeding up generation.
- **Context window**: how much text the model can consider at once; both of these models accept up to one million tokens.

## Unverified
- Community threads report tokens-per-second figures for these models on unnamed hardware (for example 83.2 tokens/s for V4 Pro 0813), but no fetched page shows a measurement method, so treat any local speed claim as untested.
- No fetched page gives a first-party tokens-per-second number for either model on a 128 GB DGX Spark; a measurement from our own hardware should replace this line before the script cites one.
- Whether a native Apple-Silicon MLX build of V4.1-Flash-1017 exists was not confirmed by any fetched page, so Mac viewers should verify before assuming a non-GGUF path.
- Ollama's listing for deepseek-v4.1-flash appeared in search with cloud tags only and was not fetched as a page, so whether Ollama can pull these weights locally is unconfirmed.
- Whether DeepSeek shipped anything new on 2026-11-14 is unconfirmed; the day's event in fetched sources is the Hacker News thread, and Artificial Analysis dates the V4 Pro 0813 release to August 2026.

## Suggested outline
1. Open on the size gap that decides the night: the smallest DeepSeek-V4-Pro-0813 download is 850 GB, the smallest DeepSeek-V4.1-Flash-1017 download is 233 GB, and only one of them runs on a 128 GB machine.
2. Land the twist with DeepSeek's own table: the 552B Flash outscores the 1.6T Pro on Terminal-Bench 2.1 (90.6 vs 87.9) and DeepSWE v1.1 (74.2 vs 62.7), so the small model is the quality pick for coding and agents, not the compromise.
3. Walk the pull: count free memory, grab the Unsloth GGUF that fits, run it in llama.cpp or Unsloth Desktop with SSD offload, then close on who still needs the Pro and what the API costs ($0.3 / $1.2 vs $1.32 / $3.96 per 1M tokens at peak).

## Viewer situation
You've got a gaming PC, a Mac, or a 128 GB DGX Spark, you've downloaded a model before, and tonight you're deciding which of DeepSeek's two open-weight flagships to pull.

## Has process
`true`
- Count your free memory (unified RAM on a Mac or the Spark, system RAM plus VRAM on a gaming PC) before choosing anything.
- Pick the model that fits that number: DeepSeek-V4.1-Flash-1017 if you have 128 GB or more, V4 Pro 0813 only if you can hold an 850 GB model.
- Download the matching GGUF from Unsloth's Hugging Face repository, choosing the quant size that fits (UD-IQ1_S at 233 GB is the smallest Flash file).
- Run it in llama.cpp or Unsloth Desktop, letting SSD offloading hold the parts that do not fit in RAM.
- Set reasoning effort to trade speed against depth (a 1-100 setting on Flash, low / high / max on Pro).

## Objection
"Benchmarks on DeepSeek's own card favor their new Flash because the comparison runs were tuned for it; the Pro still wins the knowledge rows, so run both quants on your own box for a night before you crown the small one."

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813 | deepseek-ai/DeepSeek-V4-Pro-0813 | primary | web_extract | 2026-11-14 |
| 2 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash | primary | web_extract | 2026-11-14 |
| 3 | https://api-docs.deepseek.com/quick_start/pricing/ | Models & Pricing | DeepSeek API Docs | primary | web_extract | 2026-11-14 |
| 4 | https://artificialanalysis.ai/models/deepseek-v4-pro | DeepSeek V4 Pro 0813 Models - Artificial Analysis | benchmark | web_extract | 2026-11-14 |
| 5 | https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017 | DeepSeek V4.1 Flash 1017 Models - Artificial Analysis | benchmark | web_extract | 2026-11-14 |
| 6 | https://huggingface.co/unsloth/DeepSeek-V4-Pro-0813-GGUF | unsloth/DeepSeek-V4-Pro-0813-GGUF | docs | web_extract | 2026-11-14 |
| 7 | https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF | unsloth/DeepSeek-V4.1-Flash-1017-GGUF | docs | web_extract | 2026-11-14 |
| 8 | https://unsloth.ai/docs/models/deepseek-v4.1-flash | DeepSeek-V4.1-Flash: Run Locally Guide | Unsloth Documentation | docs | web_extract | 2026-11-14 |
| 9 | https://news.ycombinator.com/item?id=50492302 | DeepSeek V4 Pro 0813 | Hacker News | community | web_extract | 2026-11-14 |
| 10 | https://hn.algolia.com/api/v1/search_by_date?query=deepseek&tags=story&numericFilters=created_at_i%3E1794489600&hitsPerPage=30 | HN Algolia search API (DeepSeek stories, 2026-11-14) | community | web_extract | 2026-11-14 |

## Notes
Naming trap: the Flash to pull today is DeepSeek-V4.1-Flash-1017, the October update; DeepSeek's pricing page lists MODEL VERSION DeepSeek-V4.1-Flash-1017 for deepseek-flash, and the base V4.1-Flash card's frontier-table column DS-V4.1-Flash is the earlier September model. The 1017 card's own gains (DeepSWE v1.1 77.0, Terminal-Bench 4.0 42.3) were read on the Unsloth 1017 page and only strengthen the pick. Conflicts: parameter counts differ by source (1.6T / 49B in DeepSeek's base-model table and Artificial Analysis, 1.57T / 48B from Unsloth, 1.7T on the Hugging Face sidebar, likely counting the DSpark draft module); the brief trusts DeepSeek's own table via the verbatim Artificial Analysis sentence. The 2026-11-14 HN thread showed 24 points in the Algolia record but 22 points on the page when fetched; points move, cite the thread, not the count. The task framing said the Pro 0813 open-weight drop happened about 11 hours before 2026-11-14; fetched pages date the weights to August 2026, so the video should frame 2026-11-14 as the day the HN discussion put the model back in front of local-AI people, not as release day. Unsloth could not reproduce a rival quantizer's recovery claims (GSQ-RCO IQ1_M claims 98.7% recovery, Unsloth measured 97.24 with p-value 0.0013), so avoid any quant-quality percentages beyond Unsloth's own tables. The Pro GGUF repository is still filling ("Quants are uploaded to this repository as they finish converting"), so a smaller Pro quant than 850 GB may appear and soften the memory argument; Terminal-Bench 2.1 and 4.0 are different harnesses and their scores must never be mixed in one comparison.
