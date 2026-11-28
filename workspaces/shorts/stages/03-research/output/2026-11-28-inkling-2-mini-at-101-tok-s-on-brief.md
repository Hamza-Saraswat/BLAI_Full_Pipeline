---
slug: 2026-11-28-inkling-2-mini-at-101-tok-s-on
stage: 03-research
topic: "Can one GB10 hit 101 tok/s on Inkling 2 Mini in vLLM, and which settings get it there?"
depth: standard
generated_at: 2026-11-28T12:53:23Z
sources: 9
hub: "[[videos/2026-11-28-inkling-2-mini-at-101-tok-s-on]]"
---

# Research brief: Can one GB10 hit 101 tok/s on Inkling 2 Mini in vLLM, and which settings get it there?

## Summary
The teach is a budget, not a purchase: on the same benchmark, one GB10 box went from a published 61.4 to 101 tok/s by trading settings against the machine's single 128 GB memory pool, not by adding hardware. The most arresting number is 101 tok/s for a single request (195.7 tok/s in aggregate across four), measured by a homelab author on an MSI EdgeXpert GB10 with an FP8 KV cache at 131,072-token context, who published the launch command and every A/B run. The strongest concrete case for the writer: the five-change progression from baseline to 101 and the abridged launch command sit on one page. What could not be verified: every number from the Hacker News commenters (about 220 tok/s on a 5090, 150 decode on a Mac engine) and any first-party reproduction on our own Spark. One conflict: tonyd2wild's README rounds the same draft-model comparison to 61 to 88 tok/s where the writeup's table says 61.4 to 88.2 -- the same measurement, rounded differently.

## Thesis
A desk-side GB10 with 128 GB of shared memory hits 101 tok/s on Inkling 2 Mini not by adding hardware but by trading prefill chunk size, KV-cache precision and a draft model against one memory budget.

## Explanation path
Speed on this box is a budgeting story before it is a compute story. Establish what a tokens-per-second number measures -- a request splits into prefill, reading your prompt, and decode, writing the reply, and the 101 number is decode only -- before any hardware or flag appears. Then establish the machine: one GB10 chip whose 128 GB of memory is shared between CPU and GPU, which is why every setting is a trade against the same pool, and the model: a mixture-of-experts design that stores 26.4B weights but activates 5.4B effective per token, arriving as one about-20GB checkpoint already in 4-bit-class precision. With those three fixed, the settings land as consequences: a small draft model guesses tokens ahead so each decode step commits one to eight tokens; an FP8 KV cache roughly doubles how much conversation fits; the prefill chunk stays small so the KV cache keeps full-length requests; and the prefill win comes from kernel launch configuration because memory bandwidth was not the limit. Close on the transferable habit: profile one real step, change one knob, measure again.

## Claims
1. **Inkling 2 Mini is Thinking Machines Lab's looped mixture-of-experts model with 26.4B total parameters, 3.4B active and 5.4B effective active parameters per token across three loop passes, released November 20, 2026 under Apache 2.0 with a context window up to 1M tokens.**
   - Source: thinkingmachines/Inkling-2-Mini model card, https://huggingface.co/thinkingmachines/Inkling-2-Mini
   - Tier: primary | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "Parameters 26.4B, 3.4B active ... Since the model runs with three passes, there are 5.4B effective active parameters per token. ... Inkling 2 Mini supports a context window of up to 1M tokens."
2. **The weights ship as one checkpoint of about 20GB in mixed NVFP4 and MXFP8 precisions, with 1x NVIDIA DGX Spark supported, Apple silicon devices with 32GB or more memory, and 32GB or more of VRAM recommended on other GPUs.**
   - Source: thinkingmachines/Inkling-2-Mini model card, https://huggingface.co/thinkingmachines/Inkling-2-Mini
   - Tier: primary | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "The model is distributed as a single checkpoint of about 20GB, in mixed NVFP4 and MXFP8 precisions. ... Other GPUs and platforms are possible, with 32GB or more of VRAM recommended"
3. **A homelab author measured 101 tok/s of single-request decode and 195.7 tok/s in aggregate for four concurrent requests, running the official checkpoint in vLLM on one GB10 machine (an MSI EdgeXpert with 128 GB of unified memory) with an FP8 KV cache, a 131,072-token context and 36% of memory.**
   - Source: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10, https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "A few days of tuning later, Inkling runs at: 101 tok/s for a single request. 195.7 tok/s in aggregate for four concurrent requests. ... Inkling still uses 36% of the GB10's memory."
4. **On the same published benchmark, the vLLM baseline with the shipped DSpark drafter was 61.4 tok/s, swapping in the DFlash2 draft model lifted it to 88.2 tok/s, and the author's five further changes took the live service from 90.3 to 101.0 tok/s.**
   - Source: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10, https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "On their benchmark it lifted one request from 61.4 to 88.2 tok/s. With the same patches I measured 90.3. ... The finished service measured 101.0 and 100.7 tok/s in two runs."
5. **Raising the prefill chunk size sped prefill but shrank the KV cache: at 6,144-token chunks the cache held only 1.33 full 131,072-token requests, and at 8,192 the service would not start, so the configuration kept 4,096-token chunks.**
   - Source: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10, https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "At 6,144 tokens it held only 1.33 full requests. At 8,192 the service wouldn't start."
6. **The prefill bottleneck was kernel launch configuration, not memory bandwidth: the expert GEMMs reached about 38 TFLOP/s (roughly 8% of the GB10's FP4 peak), and retiling them cut a 32K prompt's time to first token from 12.2 to 9.7 seconds.**
   - Source: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10, https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "The expert GEMMs reached about 38 TFLOP/s, roughly 8% of the GB10's FP4 peak. Memory bandwidth wasn't the limit, so the kernel's launch configuration was worth a look. ... End to end, the 32K time to first token fell from 12.2 to 9.8 seconds in the A/B runs and to 9.7 on the live service."
7. **On one DGX Spark, an FP8 (E4M3) KV cache grows the KV pool to 3,308,911 tokens from 2,075,828 tokens at BF16, holding three full 1,048,576-token requests at once and passing a 949,953-token needle test.**
   - Source: Inkling-2-Mini-NVFP4-DGX-Spark repository, https://github.com/tonyd2wild/Inkling-2-Mini-NVFP4-DGX-Spark
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "KV pool | 1,346,671 tokens | 2,075,828 tokens | 3,308,911 tokens ... A 3.3M-token pool holds three full 1M requests at once."
8. **In vLLM V1 chunked prefill is always enabled by default, and the tuning docs state that smaller max_num_batched_tokens values achieve better inter-token latency while higher values achieve better time to first token.**
   - Source: Optimization and Tuning (vLLM docs), https://docs.vllm.ai/en/v0.10.2/configuration/optimization.html
   - Tier: docs | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "In vLLM V1, chunked prefill is always enabled by default. ... Smaller values (e.g., 2048) achieve better inter-token latency (ITL) because there are fewer prefills slowing down decodes."
9. **vLLM's official recipe for Inkling 2 Mini lists the DGX Spark (GB10) as supported hardware, serves it with the checkpoint's bundled DSpark speculative drafter, and caps the context at 262,144 tokens on the Spark to fit in memory.**
   - Source: thinkingmachines/Inkling-2-Mini | vLLM Recipes, https://recipes.vllm.ai/thinkingmachines/Inkling-2-Mini
   - Tier: docs | Confidence: high | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "On H100 and DGX Spark, the recipe caps the context at 262,144 tokens to fit in memory."
10. **The measurement was posted as a Show HN thread on Hacker News about a day before this brief, where the sharpest reply dismissed tok/s ratings in favor of output quality rather than challenging the method.**
   - Source: Show HN: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10 | Hacker News, https://news.ycombinator.com/item?id=50670443
   - Tier: community | Confidence: medium | Accessed: 2026-11-28 | Via: web_extract
   - Quote: "I don't care much for tok/s ratings if the output is crap and I haven't had really good results from Inkling 2 Mini vs most of the other models in the same weight class."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | single-request decode, final vLLM configuration, one GB10 | 101 tok/s | https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/ | "101 tok/s for a single request." |
| 2 | published single-request decode, vLLM + DSpark baseline, same benchmark | 61.4 tok/s | https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/ | "On their benchmark it lifted one request from 61.4 to 88.2 tok/s." |
| 3 | aggregate decode, four concurrent requests | 195.7 tok/s | https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/ | "195.7 tok/s in aggregate for four concurrent requests." |
| 4 | official checkpoint size on disk | about 20GB | https://huggingface.co/thinkingmachines/Inkling-2-Mini | "The model is distributed as a single checkpoint of about 20GB, in mixed NVFP4 and MXFP8 precisions." |
| 5 | recommended GGUF quant for a 24 GB card | 17.6 GB | https://unsloth.ai/docs/models/inkling-2-mini | "UD-Q8_K_XL is full precision. The recommended quant is UD-Q4_K_XL (17.6 GB)." |
| 6 | DGX Spark memory bandwidth | 273 GB/s | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "Memory | 128 GB LPDDR5x unified system memory, 256-bit interface, 4266 MHz, 273 GB/s bandwidth" |
| 7 | KV pool, FP8 KV tier, one DGX Spark | 3,308,911 tokens | https://github.com/tonyd2wild/Inkling-2-Mini-NVFP4-DGX-Spark | "A 3.3M-token pool holds three full 1M requests at once." |

## Analogy candidates
- **A prep cook and a head chef**: the draft model preps seven token guesses and Inkling verifies all of them in a single pass, keeping one to eight tokens per step -- that is where the decode speed comes from. Breaks when: it explains the draft-model win but none of the memory tradeoffs that decided every other setting.
- **One shared garage**: the CPU and the GPU park in the same 128 GB garage, and every crate reserved for the KV cache is a crate the OS and a second model cannot use, which is why the fast configuration uses a small chunk size and an FP8 KV cache. Breaks when: a garage does no computing, so it cannot explain why kernel retileing, not parking, moved prefill.

## Misconceptions
- Myth: vLLM is a batch-serving engine for companies; single-stream chat at home belongs to llama.cpp or Ollama. Reality: the biggest gains in this writeup were single-user gains, 61.4 to 101 tok/s for one request, and vLLM's own docs tune chunked prefill for inter-token latency (claims 4 and 8).
- Myth: a 273 GB/s unified-memory box is too bandwidth-starved for fast decode. Reality: the author profiled the expert GEMMs at roughly 8% of the GB10's FP4 peak and found memory bandwidth was not the limit; kernel launch configuration was (claim 6).
- Myth: a 26B model needs tens of gigabytes of VRAM before you can start, so you must re-quantize it yourself. Reality: the official checkpoint already ships in mixed NVFP4 and MXFP8 at about 20GB, so no re-quantization is needed on a Spark, and a recommended 4-bit GGUF at 17.6 GB fits a 24 GB card (claim 2).

## Glossary
- **tokens per second (tok/s)**: how many tokens the model writes per second once it has read your prompt; the headline speed number.
- **prefill**: reading your whole prompt into memory before the first word of the reply appears.
- **decode**: writing the reply after the first token, one step at a time.
- **KV cache**: the memory where the model keeps what it has already read so it does not re-read it on every token.
- **chunked prefill**: reading a long prompt in fixed-size chunks so ongoing decodes are not stalled behind it.
- **draft model (speculative decoding)**: a small model that guesses several tokens ahead while the big model checks all guesses in one pass.
- **mixture of experts (MoE)**: a model that stores many specialist sub-networks and routes each token through only a few of them.
- **quantization**: storing model weights in lower precision to shrink memory, such as NVFP4 or a 4-bit GGUF.
- **unified memory**: one pool of RAM shared by CPU and GPU, as on the DGX Spark's GB10.
- **CUDA graph**: a recorded sequence of GPU kernel launches that the engine replays every decode step instead of launching each kernel anew.

## Unverified
- Tokens per second on our own DGX Spark remains unmeasured; the expectation is the published 61 to 101 range on the DSpark and DFlash2 configurations.
- A Hacker News commenter reports more than 3k prefill and more than 100 decode on a 32 GB GPU with the base model; community-only, not verified.
- A Hacker News commenter reports about 220 tok/s on a 5090 with two 131k contexts via Basalt; community-only, not verified.
- A Hacker News commenter reports 5K prefill and 150 decode for oMlx on Mac; community-only, not verified.
- Whether the DFlash2 patches and the compile-stall fix have merged into a released vLLM version; the writeup ran them as eight overlay files, and vLLM pull request #69288 was still open.

## Suggested outline
1. Open on the number and the gap: 101 tokens per second on one desk-side GB10 box, against a published 61.4 on the same benchmark -- the difference is settings, not silicon.
2. Define what the number measures and what the box is: prefill versus decode, and one 128 GB memory pool shared by CPU and GPU that every setting draws from.
3. Walk the knobs that did the work -- a draft model that guesses ahead, an FP8 KV cache that roughly doubles what fits, a 4,096-token chunk size chosen to protect the KV cache -- then hand the viewer tonight's commands and the honest catch that untuned setups land near 61.

## Viewer situation
You have a gaming PC or a DGX Spark on your desk, you have already run a model in Ollama or LM Studio, and you keep hearing vLLM is for batch servers at work rather than one fast chat at home.

## Has process
`true`
- Check the memory you have against the model: the official checkpoint is about 20GB and the recommended GGUF quant UD-Q4_K_XL is 17.6 GB.
- On a gaming PC, install Unsloth Desktop (or a llama.cpp build with looped-layer support) and download the quant that fits your card.
- On a Spark, clone tonyd2wild's Inkling-2-Mini-NVFP4-DGX-Spark repository and run ./launch_standard.sh, then ./prepare_dflash2.sh and ./launch_dflash2.sh for the faster draft model.
- Keep the launch flags that protect the KV cache: 4,096-token chunks and an FP8 KV cache where your memory budget allows.
- Watch unified memory while the server warms up; the repository's watch_start.sh kills the container if MemAvailable drops under 3 GiB.

## Objection
The 101 tok/s needed eight patched overlay files beyond stock vLLM on a benchmark at temperature 0, and speed means nothing if the output is worse than the same-size competition -- as one skeptic on the thread said.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/thinkingmachines/Inkling-2-Mini | thinkingmachines/Inkling-2-Mini model card | primary | web_extract | 2026-11-28 |
| 2 | https://thinkingmachines.ai/news/inkling-2-mini/ | Introducing Inkling 2 Mini - Thinking Machines Lab | primary | web_extract | 2026-11-28 |
| 3 | https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/ | Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10 | benchmark | web_extract | 2026-11-28 |
| 4 | https://news.ycombinator.com/item?id=50670443 | Show HN: Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10 | Hacker News | community | web_extract | 2026-11-28 |
| 5 | https://github.com/tonyd2wild/Inkling-2-Mini-NVFP4-DGX-Spark | Inkling-2-Mini-NVFP4-DGX-Spark | benchmark | web_extract | 2026-11-28 |
| 6 | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Hardware Overview - DGX Spark User Guide | primary | web_extract | 2026-11-28 |
| 7 | https://recipes.vllm.ai/thinkingmachines/Inkling-2-Mini | thinkingmachines/Inkling-2-Mini | vLLM Recipes | docs | web_extract | 2026-11-28 |
| 8 | https://docs.vllm.ai/en/v0.10.2/configuration/optimization.html | Optimization and Tuning - vLLM | docs | web_extract | 2026-11-28 |
| 9 | https://unsloth.ai/docs/models/inkling-2-mini | Inkling 2 Mini - Run Locally Guide | Unsloth Documentation | docs | web_extract | 2026-11-28 |

## Notes
The 101 tok/s is decode speed on tonyd2wild's benchmark: five prompts in each of eight categories at temperature 0 with thinking off and 1,024 output tokens, excluding time to first token; on sampled everyday prompts at temperature 1.0 the tuned setup scored 69.8 to 70.7 tok/s. The serving image is vllm/vllm-openai:inkling-2-mini (vLLM 0.1.dev25855+g7cb5dae22, a pre-release of 0.35, per tonyd2wild's as-tested table); runtimenotes pins it by digest. Conflict: tonyd2wild's README rounds the DFlash2 swap to 61 tok/s to 88 tok/s (1.44x) where runtimenotes' table gives 61.4 and 88.2 for the same setup -- the same measurement, rounded differently; the brief reports the decimals. A viewer starting from tonyd2wild's repository tonight should expect its published 88, not 101, because the 101 configuration additionally mounts eight overlay files (DFlash2 patches, INT8 draft copies, the compile-stall fix, adaptive verify width, the prefill GEMM configuration). The Unsloth GGUF path is the gaming-PC route; the official NVFP4 checkpoint route is the Spark route. The Thinking Machines release notes corroborate the model facts and add that the ~20GB footprint was demonstrated offline on a MacBook Pro.
