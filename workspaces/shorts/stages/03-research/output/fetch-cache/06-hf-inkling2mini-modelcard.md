# 06 -- Hugging Face model card, thinkingmachines/Inkling-2-Mini (tier 1)

URL: https://huggingface.co/thinkingmachines/Inkling-2-Mini
Accessed: 2026-11-23 | Via: web_extract | Tier: primary (first-party model card)

## Verbatim
- "Model provider: Thinking Machines Lab, Inc."
- "Date of release: November 20, 2026"
- "License: Apache 2.0"
- "The model is distributed as a single checkpoint of about 20GB, in mixed NVFP4 and MXFP8 precisions."
- Required hardware: "1x NVIDIA DGX Spark; Apple silicon devices with 32GB or more memory (MacBooks, Mac minis and Studios); Other GPUs and platforms are possible, with 32GB or more of VRAM recommended"
- "A 24-layer decoder-only transformer with sparse Mixture-of-Experts (MoE) feed-forward layers. The middle 12 layers run three times with shared weights, giving 48 layer applications per token from 24 layers of weights. In each layer, each token is routed to 8 of 128 experts."
- "26.4B, 3.4B active" / "each extra pass through the looped layers adds about 1.0B effective active parameters. Since the model runs with three passes, there are 5.4B effective active parameters per token."
- "Inkling 2 Mini supports a context window of up to 1M tokens."
- Downloads last month: 41,888.

## Evals table (Thinking Machines Lab's own, harnesses named)
- "DeepSWE v1.1 mini-swe-agent v2.4.6 | 48.2% | 0.3% (Gemma 4 31B) | 4.4% (Muse Glimmer) | 42.2% (Qwen3.8-27B) | 24.7% (Nemotron 3.5 Super VL)"
- "SWEBench Verified bash only | 79.2% | 46.1% | 76.0% | 77.8% | 71.1%"
- "SWEBench Pro v2 (Hard) mini-swe-agent v2.4.6 | 77.9% | ... | 73.8% (Qwen3.8-27B)"
- "Terminal Bench v4.0 mini-swe-agent v2.4.6 | 5.6% | ... | 5.6% (Qwen3.8-27B, tie)"
- "BrowseComp Inkling 2 Mini with compaction | 79.0% | ... | 61.6% (Qwen3.8-27B) | 78.9% (Nemotron)"
- Params row: "activated / total: 5.4/26.4 (Inkling) vs 27.0/27.0 (Qwen3.8-27B), 12.0/124.5 (Nemotron)"
- Safety guidance: "Run agentic workloads in a sandbox, and require confirmation before destructive or irreversible actions."

## Use in brief
- First-party facts for the "what is actually running at home" beat: params, MoE routing (8 of 128 experts), looped layers, 1M context, ~20GB checkpoint, Nov 20 2026 release.
- Eval parity within size class: 79.2% vs 77.8% SWE-bench Verified. NOTE: comparisons are against same-size open peers, NOT against Claude; the card does not benchmark vs Claude.
