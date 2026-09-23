https://huggingface.co/Qwen/Qwen3.8-27B
Accessed: 2026-09-23

# Qwen/Qwen3.8-27B - Hugging Face (rendered model card)

This repository contains model weights and configuration files for the post-trained model in the Hugging Face Transformers format. Compatible with Transformers, vLLM, SGLang, TokenSpeed.

"Following the widespread community adoption of the Qwen3.5 and Qwen3.6 series, we are pleased to introduce Qwen3.8, the most capable generation in the Qwen open-model family to date."

"Qwen3.8-27B brings these advances to a compact, deployment-friendly dense model: a native vision-language model that understands images and videos, with flexible thinking control."

## Model Overview

- Type: Causal Language Model with Vision Encoder
- Training Stage: Pre-training & Post-training
- Language Model
  - Number of Parameters: 27B
  - Hidden Dimension: 5120
  - Token Embedding: 248,320 (Padded)
  - Number of Layers: 64
  - Hidden Layout: 16 x (3 x (Gated DeltaNet -> FFN) -> 1 x (Gated Attention -> FFN))
  - MTP (Multi-Token Prediction): trained with multiple steps
- Context Length: 262,144 natively and extensible up to 1,000,000 tokens.

"Thinking mode is on by default and can be disabled per request; reasoning depth can be tuned with `reasoning_effort`".

Serving: SGLang (Qwen3.8 Cookbook), vLLM (Qwen3.8 Recipe), TokenSpeed. Hosted Qwen Cloud version "1M context length by default" coming soon.

## Benchmark Results (Text Performance)

| Benchmark | Qwen3.8-27B | Qwen3.6-27B |
| Agentic terminal coding Terminal Bench 2.1 (Terminus) | 73.0 | 63.4 |
| Agentic coding SWE-bench Pro | 61.7 | 53.5 |
| Software engineering QwenSWEBench | 79.0 | 49.3 |
| Instruction following IFBench | 79.5 | 69.1 |
| LiveCodeBench v6 | 90.3 | 83.9 |

(SWE-bench Pro note: "all models are evaluated with the Claude Code harness at temp=1.0, top_p=0.95, and a 256K context window")

"Qwen3.8-27B natively supports context lengths of up to 262,144 tokens. For long-horizon tasks where the total length (including both input and output) exceeds this limit, we recommend using RoPE scaling techniques to handle long texts effectively, e.g., YaRN."

## Evaluation results (HF metadata)

- SWE-bench_Pro: 61.7 *
- deep_swe: 42.2
- gpqa Diamond: 89.2

License: not stated in the fetched card text.
