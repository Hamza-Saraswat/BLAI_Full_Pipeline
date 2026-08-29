---
slug: 2026-08-29-glm-5-3-just-went-open-weight
workspace: shorts
stage: 03-research
depth: standard
---

# GLM-5.3 went open-weight, and nothing you own can run it: research brief

## Summary

The thesis: the license opened, the memory did not -- GLM-5.3-Flash's smallest build is 93.09 GB
against a 32 GB flagship card. The arresting number: even the ONE-BIT quant is 93.09 GB.
The strongest concrete case: Unsloth's own guide names exactly one machine class that fits,
"128GB devices", and picks UD-IQ3_XXS (120.37 GB) for them. Could not verify: any
tokens-per-second figure, on any hardware -- nothing here was measured by us and the guide
publishes no speeds. Source conflict: none found; the API-summed folder sizes and Unsloth's
published table agree to the second decimal.

## Thesis

GLM-5.3-Flash is MIT-licensed and open-weight, but its smallest GGUF is 93.09 GB, so no consumer GPU can hold it: this release is for 128 GB unified-memory machines, not your graphics card.

## Explanation path

Open the headline everyone saw, then put the smallest file size next to the biggest consumer card. Explain why the 18B-active number does not rescue it: every expert must be resident, so memory follows total parameters, not active ones. Land on the one machine class the drop actually serves and the one-line check a viewer performs before downloading anything.

## The viewer

- **Situation**: Owns a gaming GPU between 8 and 24 GB, saw 'GLM-5.3 is now open-weight' at the top of Hacker News, and is deciding whether to download it tonight.
- **Objection**: "It says 18B active parameters, and 18B models run fine on my card, so surely a quant of this fits."

## Claims

| # | Claim | Source | Quality | Confidence |
|---|-------|--------|---------|------------|
| 1 | GLM-5.3-Flash has 320B total parameters and 18B active parameters | [zai-org/GLM-5.3-Flash model card](https://huggingface.co/zai-org/GLM-5.3-Flash) | primary | high |
| 2 | GLM-5.3-Flash is released under the MIT license | [zai-org/GLM-5.3-Flash model card](https://huggingface.co/zai-org/GLM-5.3-Flash) | primary | high |
| 3 | The smallest published GGUF build, UD-IQ1_S, totals 93.09 GB | [unsloth/GLM-5.3-Flash-GGUF file listing (per-folder sizes summed via the HF API)](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF) | primary | high |
| 4 | The 2-bit UD-Q2_K_XL build totals 108.72 GB and the 4-bit UD-Q4_K_XL 199.71 GB | [unsloth/GLM-5.3-Flash-GGUF file listing (HF API)](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF) | primary | high |
| 5 | Unsloth's own guide puts the 1-bit build at 100 GB of memory and recommends UD-IQ3_XXS as the quant that fits on 128GB devices | [Unsloth: GLM-5.3-Flash, how to run locally](https://unsloth.ai/docs/models/glm-5.3-flash.md) | docs | high |
| 6 | The open-weight announcement carried 767 points and 260 comments on Hacker News within 28 hours | [BLAI radar 2026-08-29 (HN metadata for the GLM-5.3 item)](https://huggingface.co/zai-org/GLM-5.3) | community | high |
| 7 | The full GLM-5.3 (non-Flash) is 753B parameters, so the Flash variant IS the small one | [zai-org/GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3) | primary | high |
| 8 | The Flash base repo shows 189.8k downloads and the GGUF repo 27.3k within days of release | [Hugging Face trending metadata (radar sweep + HF API)](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF) | community | medium |

Quotes, verbatim, one per claim:

- claim 1: "With 320B total parameters and just 18B active parameters"
- claim 2: "MIT license"
- claim 3: "UD-IQ1_S: 93.09 GB (sum of the folder's .gguf files)"
- claim 4: "UD-Q2_K_XL: 108.72 GB; UD-Q4_K_XL: 199.71 GB"
- claim 5: "1-bit quantization: 100 GB; 3-bit UD-IQ3_XXS fits on 128GB devices"
- claim 6: "Shipped: 767 points, 260 comments on HN, 28 h ago"
- claim 7: "753B params"
- claim 8: "189.8k downloads (base), 27,288 downloads / 266 likes (GGUF repo)"

## Key numbers

| Label | Value | Source |
|-------|-------|--------|
| smallest GGUF (UD-IQ1_S) | **93.09 GB** | https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF |
| 2-bit UD-Q2_K_XL | **108.72 GB** | https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF |
| 3-bit UD-IQ3_XXS (the 128 GB pick) | **120.37 GB** | https://unsloth.ai/docs/models/glm-5.3-flash.md |
| 4-bit UD-Q4_K_XL | **199.71 GB** | https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF |
| total / active parameters | **320B / 18B** | https://huggingface.co/zai-org/GLM-5.3-Flash |
| 1-bit memory need (Unsloth) | **100 GB** | https://unsloth.ai/docs/models/glm-5.3-flash.md |
| biggest consumer GPU VRAM | **32 GB (RTX 5090)** | https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ |

## The quant ladder (summed .gguf bytes per folder, HF API, 2026-08-29)

| Build | Size |
|-------|------|
| UD-IQ1_S | 93.09 GB |
| UD-IQ1_M | 97.58 GB |
| UD-IQ2_XXS | 101.84 GB |
| UD-Q2_K_XL | 108.72 GB |
| UD-IQ3_XXS | 120.37 GB |
| UD-Q3_K_XL | 147.54 GB |
| UD-IQ4_XS | 156.82 GB |
| UD-Q4_K_XL | 199.71 GB |
| UD-Q5_K_XL | 240.31 GB |
| UD-Q6_K_XL | 291.83 GB |
| Q8_0 | 340.98 GB |
| BF16 | 641.64 GB |

## Process steps (has_process: true)

1. Read your machine's total GPU or unified memory (About This Mac, or nvidia-smi).
2. Open the Files tab of unsloth/GLM-5.3-Flash-GGUF and read the size of the smallest folder, UD-IQ1_S: 93.09 GB.
3. If your number is under 100 GB, close the tab: no quant of this model fits. At 128 GB, Unsloth's own guide points you at UD-IQ3_XXS.

## Analogy candidates

- **the receptionist**: 18B active parameters is the one receptionist who answers; 320B total is the whole staff directory that still has to be in the building. Limit: the building never gets smaller at night: every expert stays resident even when idle.

## Misconceptions

- **Myth**: Open-weight means you can run it on your GPU **Reality**: The license opens; the memory does not. The smallest build is 93.09 GB against a 32 GB flagship card.
- **Myth**: 18B active parameters means it needs what an 18B model needs **Reality**: Active parameters set compute per token, not memory: all 320B of experts must sit in memory for routing to reach them.

## Glossary

- **MoE (mixture of experts)**: A model built of many expert sub-networks; each token uses a few, but all of them stay loaded
- **UD quant**: Unsloth Dynamic quantization: different layers stored at different bit widths to keep quality at low size
- **unified memory**: One memory pool shared by CPU and GPU, as on a Mac Studio or a DGX Spark, so the whole pool can hold weights

## Unverified

- Tokens-per-second on any 128 GB device: Unsloth's guide gives no speed figures, and nothing here was measured on our hardware.
- The HN thread's comment texts (the endpoint rate-limited at fetch time); only the point and comment counts from the radar metadata are used.
- Whether llama.cpp needs special flags for the glm_moe_dsa architecture; the guide shows none.

## Suggested outline

Hook: the headline number against the file size. Then the receptionist beat for 320/18. Then the ladder: 93 to 200 GB, and the one machine class it serves at 128 GB. Payoff: the one-line memory check before you download 93 GB for nothing.

## Notes

Angle sharpened from the ideas note: the pick promised 'what fits your GPU' and the honest answer is 'nothing does'; the EQUIPS is the check that saves a wasted download, the TEACHES is active-vs-total memory.
