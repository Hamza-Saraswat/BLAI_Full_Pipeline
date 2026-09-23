https://qwen.ai/blog?id=qwen3-coder-next
Accessed: 2026-09-23

# Qwen3-Coder-Next: Pushing Small Hybrid Models on Agentic Coding | Qwen (2026/02/02, QwenTeam)

"We introduce **Qwen3-Coder-Next**, an open-weight language model designed specifically for coding agents and local development. Built on top of **Qwen3-Next-80B-A3B-Base**, which adopts a novel architecture with hybrid attention and MoE, Qwen3-Coder-Next has been agentically trained at scale on large-scale executable task synthesis, environment interaction, and reinforcement learning, obtaining strong coding and agentic capabilities with significantly lower inference costs."

## Performance on Coding Agent Benchmarks

- "Qwen3-Coder-Next achieves **over 70% on SWE-Bench Verified** using the SWE-Agent scaffold."
- "Performance remains competitive across **multilingual settings** and the more challenging **SWE-Bench Pro** benchmark."
- "**Qwen3-Coder-Next (3B active)** achieves SWE-Bench-Pro performance comparable to models with **10x-20x more active parameters**."
- "Qwen3-Coder-Next sits on a strong Pareto frontier for **cost-effective agent deployment**."

## Scaling Agentic Training

Recipe: continued pretraining on code- and agent-centric data; supervised fine-tuning on high-quality agent trajectories; domain-specialized expert training; expert distillation into a single deployment-ready model. "This recipe emphasizes **long-horizon reasoning, tool usage, and recovery from execution failures**."

Demos with OpenClaw, Qwen Code, Claude Code, Web dev, browser use, Cline.
