# URL: https://huggingface.co/Qwen/Qwen3.8-27B

# Qwen3.8-27B

> This repository contains model weights and configuration files for the post-trained model in the Hugging Face Transformers format.
>
> These artifacts are compatible with Hugging Face Transformers, vLLM, SGLang, TokenSpeed, etc.

> For users seeking managed, scalable inference without infrastructure maintenance, the official Qwen API service is provided by [Qwen Cloud](https://www.qwencloud.com/).
> In particular, **Qwen3.8-27B** will be available as a hosted version with more production features, e.g., 1M context length by default, official built-in tools. For more information, please refer to the [Qwen3.8-27B Overview](https://www.qwencloud.com/models/qwen3.8-27b). The service is coming soon. Stay tuned for updates.

Following the widespread community adoption of the Qwen3.5 and Qwen3.6 series, we are pleased to introduce Qwen3.8, the most capable generation in the Qwen open-model family to date.

Built on the architectural foundation of Qwen3.5, Qwen3.8 delivers substantial gains across coding, professional work, research, and long-horizon agentic tasks. Qwen3.8-27B brings these advances to a compact, deployment-friendly dense model: a native vision-language model that understands images and videos, with flexible thinking control, designed to carry complex, multi-step tasks through to completion with greater reliability.

## Qwen3.8 Highlights

Qwen3.8-27B features the following enhancements:

- **Core Capabilities**: Comprehensive improvements across coding, professional work, research, and long-horizon agentic tasks.
- **Agent Execution**: Stronger autonomous planning and better handling of environment feedback, leading to more reliable end-to-end task completion.
- **Downstream Compatibility**: Broader support for popular harnesses and development tools, making it easier to integrate into your existing stack.
- **Flexible Thinking Control**: Thinking mode is on by default and can be disabled per request; reasoning depth can be tuned with `reasoning_effort`, and reasoning context from historical messages is retained via `preserve_thinking`.
- **Vision-Language Understanding**: Native support for image and video understanding, from STEM diagrams and documents to hour-scale videos.

## Model Overview

- Type: Causal Language Model with Vision Encoder
- Training Stage: Pre-training & Post-training
- Language Model
  - Number of Parameters: 27B
  - Hidden Dimension: 5120
  - Token Embedding: 248,320 (Padded)
  - Number of Layers: 64
  - Hidden Layout: 16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))
  - Gated DeltaNet:
    - Number of Linear Attention Heads: 48 for V and 16 for QK
    - Head Dimension: 128
  - Gated Attention:
    - Number of Attention Heads: 24 for Q and 4 for KV
    - Head Dimension: 256
    - Rotary Position Embedding Dimension: 64
  - Feed Forward Network:
    - Intermediate Dimension: 17,408
  - LM Output: 248,320 (Padded)
  - MTP (Multi-Token Prediction): trained with multiple steps
- Context Length: 262,144 natively and extensible up to 1,000,000 tokens.

## Benchmark Results

### Text Performance

|  | Qwen3.8-27B | Qwen3.6-27B | Qwen3.7-Plus | Muse Glimmer-30B | Opus4.6 Max |
| --- | --- | --- | --- | --- | --- |
| Coding |
| Agentic terminal coding<br>Terminal Bench 2.1 (Terminus) | 73.0 | 63.4 | 64.0 | 51.7 | **78.2** |
| Agentic coding<br>SWE-bench Pro | **61.7** | 53.5 | 57.6 | 51.2 | 53.4 |
| Repo-level code generation<br>NL2Repo-Bench | 42.3 | 36.2 | 41.1 | -- | **47.6** |
| Agentic coding<br>DeepSWE 1.1 | **42.2** | 13.3 | 14.2 | -- | -- |
| Software engineering<br>QwenSWEBench | **79.0** | 49.3 | 59.2 | -- | 63.8 |
| Agent |
| Long-horizon office work<br>CoWorkBench | **70.7** | 61.0 | 65.1 | -- | 68.2 |
| Professional job tasks<br>JobBench | **33.4** | 21.8 | 27.6 | -- | -- |
| Frontier agentic tasks<br>Agents' Last Exam | Pass@1 **20.4** Score **42.9** | Pass@1 10.6 Score 27.3 | Pass@1 13.2 Score 33.6 | -- | -- |
| General |
| Instruction following<br>IFBench | **79.5** | 69.1 | 79.1 | 77.0 | 62.5 |
| Scientific reasoning<br>GPQA Diamond | 89.2 | 87.8 | 90.3 | 83.5 | **91.3** |
| Multidisciplinary reasoning<br>HLE | 30.8 | 24.0 | 34.7 | 22.0 | **40.0** |
| Competitive coding<br>LiveCodeBench v6 | **90.3** | 83.9 | 89.6 | -- | 88.8 |

### VL Performance

|  | Qwen3.8-27B | Qwen3.6-27B | Qwen3.7-Plus | Muse Glimmer-30B | Opus4.6 Max |
| --- | --- | --- | --- | --- | --- |
| Computer use<br>OSWorld-Verified | **84.3** | 63.9 | 73.3 | 65.9 | 72.7 |
| Browser use<br>WebArena-Verified | **64.8** | 48.8 | 55.3 | -- | -- |
| Mobile use<br>AndroidWorld | **81.9** | 70.3 | 81.0 | -- | 62.0 |
| Application recreation<br>RecreationBench | **47.1** | 29.8 | 30.2 | -- | -- |
| Multimodal tool use<br>ClawEval-MM | Pass@3 **57.4** Average 56.9 | Pass@3 42.6 Average 50.4 | Pass@3 **57.4** Average **60.1** | -- | Pass@3 52.5 Average 54.7 |
| Multimodal software engineering<br>SWE-MM | **38.6** | 25.7 | 30.0 | -- | 27.1 |
| Visual web development<br>Vision2Web | **62.9** | 45.0 | 42.1 | -- | -- |
| Visual math problem solving<br>MathVision | Without CI 90.0 With CI **94.6** | Without CI 85.1 | Without CI **90.3** | -- | Without CI 65.5 |
| General visual reasoning<br>BabyVision | Without CI **65.7** With CI **85.6** | Without CI 28.9 | Without CI 64.7 With CI 70.4 | -- | Without CI 12.6 |
| Scientific chart analysis<br>CharXiv (RQ) | Without CI 83.7 With CI **90.2** | Without CI 78.4 | Without CI **85.8** With CI 85.9 | 78.8 | Without CI 66.0 |
| Document intelligence<br>OmniDocBench 1.5 | 91.1 | 89.4 | **91.4** | 75.8 | 86.6 |
| Real-world perception<br>RealWorldQA | 85.9 | 84.1 | **86.9** | -- | 73.9 |
| Embodied intelligence<br>ERQA | 65.5 | 62.5 | **69.8** | -- | 40.8 |

## Quickstart

For streamlined integration, we recommend using Qwen3.8 via APIs.

### Serving Qwen3.8

- [SGLang](https://www.sglang.io/): [Qwen3.8 Cookbook](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-27B)
- [vLLM](https://vllm.ai/): [Qwen3.8 Recipe](https://recipes.vllm.ai/Qwen/Qwen3.8-27B)
- [TokenSpeed](https://lightseek.org/tokenspeed/): [Qwen3.8 Recipe](https://lightseek.org/tokenspeed/recipes/models#qwen3-8)

### API Usage

> Qwen3.8 models operate in thinking mode by default, generating thinking content signified by `<think>\n...</think>\n\n` before producing the final response.

> We recommend using the following sets of sampling parameters for generation:
>
> - Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`
> - Instruct (or non-thinking) mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`

Qwen3.8 comes with official support for `reasoning_effort`, which can be used to adjust reasoning depth and control cost:

- `xhigh` (default): for complex tasks demanding thorough analysis
- `medium`: balancing accuracy and speed
- `low`: efficient reasoning optimizing for speed and cost

In addition, `preserve_thinking` is enabled by default for all workloads for the best out-of-the-box experience.

## Best Practices

1. **Sampling Parameters**: as above.

2. **Adequate Output Length**: To optimize performance on agentic tasks, we recommend allocating sufficient output length... within the 1M context length:
   - Reasoning Content: Set the maximum output length to 262,144 tokens.
   - Final Response: Set the maximum output length to 131,072 tokens.

3. **Processing Ultra-Long Texts**: Qwen3.8-27B natively supports context lengths of up to 262,144 tokens. For long-horizon tasks where the total length (including both input and output) exceeds this limit, we recommend using RoPE scaling techniques to handle long texts effectively, e.g., YaRN.

   YaRN is currently supported by several inference frameworks, e.g., vLLM, SGLang, and TokenSpeed.

   vLLM example:

   ```shell
   VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve ... --hf-overrides '{"text_config": {"rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --max-model-len 1000000
   ```

   > All the notable open-source frameworks implement static YaRN, which means the scaling factor remains constant regardless of input length, **potentially impacting performance on shorter texts.**

4. **Long Video Understanding**: ... set the `longest_edge` parameter in the video_preprocessor_config file to 469,762,048 (corresponding to 224k video tokens) to enable higher frame-rate sampling for hour-scale videos...

## Citation

```bibtex
@misc{qwen38,
    title = {{Qwen3.8-Max}: A New Bar for Coding and Cowork},
    url = {https://qwen.ai/blog?id=qwen3.8},
    author = {{Qwen Team}},
    month = {August},
    year = {2026}
}
```

Downloads last month 8,032,442

Safetensors
Model size: 28B params
Tensor type: BF16

[Image-Text-to-Text](https://huggingface.co/tasks/image-text-to-text)

## Model tree for Qwen/Qwen3.8-27B

Adapters: 287 models
Finetunes: 817 models
Merges: 28 models
Quantizations: 1660 models (Use with llama.cpp / Llama / LM Studio / Jan)

## Collection including Qwen/Qwen3.8-27B

[4 items • Updated Aug 13 • 605](https://huggingface.co/collections/Qwen/qwen38)

## Evaluation results

- datacurve/deep-swe · Deep Swe: 42.2
- Idavidrein/gpqa · Diamond: 89.2
- harborframework/terminal-bench · Terminalbench 4: 5.6 *
- harborframework/terminal-bench-science: 0.5 *
- harborframework/terminal-bench-2.1 · Terminalbench 2 1: 73 *
- agents-last-exam · Overall Pass Rate: 20.39 * (harness=claude_code; harness_variant=reasoning-max; attempted=148/152; official leaderboard snapshot=2026-10-01T20:39:17.826877+00:00; values are percentages (0-100); equal-task aggregation; unattempted tasks contribute zero; pass threshold score>=0.999. This is an official leaderboard export, not an HF-verified evaluation.)

Ranked #1 in the < 128B size range (multiple community evaluations, Artificial Analysis Terminal-Bench 4.0 leaderboard, ALE official leaderboard)
