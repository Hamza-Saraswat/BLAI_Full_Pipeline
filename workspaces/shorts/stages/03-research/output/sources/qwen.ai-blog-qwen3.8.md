# URL: https://qwen.ai/blog?id=qwen3.8

# Qwen3.8-Max: A New Bar for Coding and Cowork | Qwen

2026/08/02 · 25 minute · 5068 words · QwenTeam丨Translations:简体中文

Today, we are officially releasing **Qwen 3.8-Max**, the most capable model in the Qwen family to date. This also marks the first time we will open-source the weights of a Qwen-Max-class model — the open weights will be released next week. Built upon the architectural foundation of Qwen 3.5, Qwen 3.8-Max scales to **2.4 trillion** parameters, delivering comprehensive improvements across coding, work, research, and long-horizon tasks. It can not only answer more challenging questions, but also complete complex tasks end-to-end with greater reliability, producing dependable deliverables.

- **Qwen3.8-Max** — now available via [QwenCloud](https://www.qwencloud.com/):
  - 2.4T parameters (95B active), with open weights releasing next week
  - comprehensive improvements across coding, work, research, and long-horizon tasks
  - end-to-end and dependable delivery of complex tasks
- Call via API on [QwenCloud](https://www.qwencloud.com/).

## Coding

For a top model, coding today means far more than writing a function on request — it means taking a real, multi-day project from an empty folder all the way to a finished result, on its own. We tested Qwen3.8-Max on three such challenges, where every result had to be earned by actually writing and running code, with **no human help at all**. One thread runs through all three: Qwen3.8-Max doesn't just follow a fixed plan — it **self-evolves through feedback loops**, whether that means building a harness that upgrades itself, refining a research method experiment after experiment, or climbing a competition leaderboard submission after submission.

### 10+ Days of Autonomous Coding: Building a Self-Evolving Harness

In this case, Qwen3.8-Max was asked to create the `oh-my-cli` project from scratch and, over a 10+ day long-horizon autonomous coding run, build a self-evolving harness. [...] The complete project trace is publicly available in the GitHub repository [qwen-code-dev-bot/oh-my-cli](https://github.com/qwen-code-dev-bot/oh-my-cli).

As of **July 30, 2026**, after approximately **16 days** of fully autonomous AI operation, the repository had accumulated **265 commits, 127 PRs, and 151 issues**, demonstrating a continuously evolving autonomous coding capability.

### Reproduce a research paper — then improve it

We handed Qwen3.8-Max a recent research paper — ["Unified Data Selection for LLM Reasoning"](https://arxiv.org/abs/2605.22389) — and asked it to: **reproduce the paper's experiment in code, then try to do better.**

[...] Qwen3.8-Max started from **nothing but the paper and a set of GPUs** — no starter code, no ready-made pipeline. [...]

Working **completely on its own for about five days** (~125 hours of continuous effort), Qwen3.8-Max wrote roughly **7,600 lines of code**, took over **1,100 actions**, and ran **33 rounds of GPU training**. [...] it finally evolved a new method that **beats the paper's own approach**, a **+2.7-point** gain on the competition-level math benchmark AIME24.

### Beat hundreds of human teams in 24 hours

[...] the [WWW2025 Multimodal Dialogue Intent Recognition Challenge](https://tianchi.aliyun.com/competition/entrance/532277), hosted on **Alibaba Cloud's Tianchi platform**, where **526 human teams** were competing. [...] Across **45 submissions** — each round's feedback steering the next round of fine-tuning and re-weighting — its accuracy climbed steadily from **0.60 to a final 0.853**, beating **458 of the 526 human teams (87% of the field)**.

## Build with Qwen3.8

### Coding Assistants

#### OpenClaw

```
json
{  "models": {    "mode": "merge",    "providers": {      "modelstudio": {        "baseUrl": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1",        "apiKey": "DASHSCOPE_API_KEY",        "api": "openai-completions",        "models": [          {            "id": "qwen3.8-max",            "name": "qwen3.8-max",            "reasoning": true,            "input": ["text", "image"],            "contextWindow": 1000000,            "maxTokens": 65536          }        ]      }    }  },  "agents": {    "defaults": {      "model": {        "primary": "modelstudio/qwen3.8-max"      }    }  }}
```

Qwen APIs support the OpenAI Responses protocol, enabling use with **Codex**:

[... model-catalog snippet with "context_window": 1000000, "effective_context_window_percent": 95 ...]

## Summary

Qwen3.8-Max is our most capable model to date, and the first open-weight model at Max scale. Scaling to 2.4 trillion parameters, it delivers comprehensive gains across coding, real-world work, long-horizon tasks, and multimodal agents — able to take complex, open-ended goals from start to finish with minimal human involvement and produce dependable deliverables. The open weights will be released next week. We welcome community feedback and look forward to seeing what you build.

## Citation

```
bibtex
@misc{qwen38,    title = {Qwen3.8-Max: A New Bar for Coding and Cowork},    url = {https://qwen.ai/blog?id=qwen3.8},    author = {{Qwen Team}},    month = {August},    year = {2026}}
```

[Go to Top (Alt+G)](https://qwen.ai/blog?id=qwen3.8#top "Go to Top")

Qwen © 2026 · Powered by Alibaba Cloud
