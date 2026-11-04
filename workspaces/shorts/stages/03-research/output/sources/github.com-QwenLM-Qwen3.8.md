# URL: https://github.com/QwenLM/Qwen3.8

# GitHub - QwenLM/Qwen3.8: Qwen3.8 is the large language model series developed by Qwen team, Alibaba Group.

Welcome to the GitHub repository of the Qwen3.5 open model series, including Qwen3.5, Qwen3.6, and the latest Qwen3.8. Here, you can find official information about Qwen3.8, post your questions (Issues), and share your ideas with the community (Discussions).

## Introduction

### Qwen3.8

For the first time, Qwen3.8 brings a Qwen-Max-class model to open release. Built on the architectural foundation of Qwen3.5, Qwen3.8 delivers substantial gains across coding, professional work, research, and long-horizon agentic tasks. Beyond answering harder questions, Qwen3.8 is designed to carry complex, multi-step tasks through to completion with greater reliability.

Qwen3.8 features the following enhancements:

- **Core Capabilities**: Comprehensive improvements across coding, professional work, research, and long-horizon agentic tasks.
- **Agent Execution**: Stronger autonomous planning and better handling of environment feedback, leading to more reliable end-to-end task completion.
- **Downstream Compatibility**: Broader support for popular harnesses and development tools, making it easier to integrate into your existing stack.
- **Flexible Thinking Control**: Reasoning depth can be tuned with `reasoning_effort`, and reasoning context from historical messages is retained via `preserve_thinking`.

## News

- 2026-08-14: Qwen3.8-27B is now available on [Hugging Face Hub](https://huggingface.co/collections/Qwen/qwen38) and [ModelScope](https://www.modelscope.cn/collections/Qwen/Qwen38). Read more on the model card.
- 2026-08-12: Qwen3.8-2.4T-A95B is now available on [Hugging Face Hub](https://huggingface.co/collections/Qwen/qwen38) and [ModelScope](https://www.modelscope.cn/collections/Qwen/Qwen38). Read more on the model card.
- 2026-04-22: Qwen3.6-27B is now available on [Hugging Face Hub](https://huggingface.co/collections/Qwen/qwen36) and [ModelScope](https://www.modelscope.cn/collections/Qwen/Qwen36). Read more on our [release blog](https://qwen.ai/blog?id=qwen3.6-27b)!
- 2026-04-16: Qwen3.6-35B-A3B is now available [...]
- 2026-03-02: Qwen3.5-9B, Qwen3.5-4B, Qwen3.5-2B, and Qwen3.5-0.8B are now available [...]
- 2026-02-24: Qwen3.5-122B-A10B, Qwen3.5-35B-A3B, and Qwen3.5-27B are released. [...]
- 2026-02-16: We release Qwen3.5. The first release includes a 397B-A17B MoE model. [...]
- 2025-09-11: We release Qwen3-Next-80B-A3B [...]

## Models

The official model weights are released on:

- Hugging Face Hub: Most LLM frameworks and applications support downloading model files from Hugging Face Hub automatically by specifying the model ID, e.g., `Qwen/Qwen3.8-27B`, `Qwen/Qwen3.6-35B-A3B`, and `Qwen/Qwen3.5-397B-A17B`.
- ModelScope: For users unable to access Hugging Face Hub, we strongly recommend using ModelScope. [...]

## Benchmarks

**Qwen3.8 Open Models**

For detailed results, please check out the [Qwen3.8-2.4T-A95B Model Card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) and the [Qwen3.8-27B Model Card](https://huggingface.co/Qwen/Qwen3.8-27B).

## Quickstart

[... Qwen Studio, Qoder, QwenWork, Qwen API ...]

#### vLLM

```
vllm serve Qwen/Qwen3.8-27B --port 8000 --tensor-parallel-size 4 --max-model-len 262144 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder
```

#### TokenSpeed

```
tokenspeed serve Qwen/Qwen3.8-27B --port 8000 --tensor-parallel-size 4 --max-model-len 262144 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder
```

### Finetuning

We advise you to use training frameworks, including Unsloth, Swift, Llama-Factory, to finetune your models with SFT, DPO, GRPO, etc.

## License Agreement

Please find the license file released with the model weights on Hugging Face Hub or ModelScope.

## Citation

```
@misc{qwen3.8,
    title  = {{Qwen3.8-Max}: A New Bar for Coding and Cowork},
    author = {{Qwen Team}},
    year   = {2026},
    month  = {August},
    url    = {https://qwen.ai/blog?id=qwen3.8}
}
```

## About

Qwen3.8 is the large language model series developed by Qwen team, Alibaba Group.

### Resources

Apache-2.0 license

Stars: 4.4k · Watchers: 31 · Forks: 342 · No releases published
