https://huggingface.co/Qwen/Qwen3-Coder-Next
Accessed: 2026-09-23

# Qwen/Qwen3-Coder-Next - Hugging Face (rendered model card)

## Highlights

Today, we're announcing **Qwen3-Coder-Next**, an open-weight language model designed specifically for coding agents and local development. It features the following key enhancements:

- **Super Efficient with Significant Performance**: With only 3B activated parameters (80B total parameters), it achieves performance comparable to models with 10-20x more active parameters, making it highly cost-effective for agent deployment.
- **Advanced Agentic Capabilities**: Through an elaborate training recipe, it excels at long-horizon reasoning, complex tool usage, and recovery from execution failures, ensuring robust performance in dynamic coding tasks.
- **Versatile Integration with Real-World IDE**: Its 256k context length, combined with adaptability to various scaffold templates, enables seamless integration with different CLI/IDE platforms (e.g., Claude Code, Qwen Code, Qoder, Kilo, Trae, Cline, etc.), supporting diverse development environments.

## Model Overview

**Qwen3-Coder-Next** has the following features:

- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Number of Parameters: 80B in total and 3B activated
- Number of Parameters (Non-Embedding): 79B
- Hidden Dimension: 2048
- Number of Layers: 48
  - Hybrid Layout: 12 * (3 * (Gated DeltaNet -> MoE) -> 1 * (Gated Attention -> MoE))
- Mixture of Experts:
  - Number of Experts: 512
  - Number of Activated Experts: 10
  - Number of Shared Experts: 1
  - Expert Intermediate Dimension: 512
- Context Length: 262,144 natively

**NOTE: This model supports only non-thinking mode and does not generate `<think></think>` blocks in its output. Meanwhile, specifying `enable_thinking=False` is no longer required.**

Recommended sampling: temperature=1.0, top_p=0.95, top_k=40.

Deployment: SGLang (`sglang>=v0.5.8`) or vLLM (`vllm>=0.15.0`), e.g. `vllm serve Qwen/Qwen3-Coder-Next --port 8000 --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser qwen3_coder`. "The default context length is 256K. Consider reducing the context length to a smaller value, e.g. `32768`, if the server fails to start."

Downloads last month: 520,734. Model size: 80B params, Tensor type BF16.

## Evaluation results

- SWE-bench/SWE-bench_Verified - Swe Bench Resolved: 70.6 *
- ScaleAI/SWE-bench_Pro - SWE Bench Pro: 44.3 *
- harborframework/terminal-bench-2.0 - Terminalbench 2: 36.2 *

(* source https://huggingface.co/papers/2603.00729)
