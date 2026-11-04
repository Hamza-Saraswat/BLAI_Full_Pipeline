# URL: https://lmstudio.ai/models/qwen/qwen3.8-27b
qwen/qwen3.8-27b • LM Studio

- Star 166 · Fork 2
- "Use Model in LM Studio" deeplink
- Description: "State-of-the-art laptop size model capable of reasoning, tools calling, and image understanding"
- Model type: Language model
- Stats: 1.6M Downloads · 166 stars · 2 forks
- Capabilities: Vision Input, Trained for tool use, Reasoning (Supports reasoning)
- **Minimum system memory: 16GB**
- Tags: 27B, qwen35
- Last updated: "Updated on August 17" by lmmy

## README

### Qwen3.8 27B

Qwen3.8 27B is a compact, deployment-friendly dense vision-language model built on the Qwen3.5 architecture. It delivers stronger performance across coding, professional work, research, and long-horizon agentic tasks.

### Highlights
- **Agent Execution**: stronger autonomous planning and environment-feedback handling improve reliability on complex, multi-step tasks.
- **Flexible Thinking Control**: thinking is enabled by default, with `xhigh`, `medium`, and `low` reasoning-effort levels. Reasoning from previous messages is preserved by default for better continuity in agentic workflows.
- **Vision-Language Understanding**: native image understanding supports content ranging from STEM diagrams to documents.
- **Long Context**: natively supports up to 262,144 tokens.

### Custom Fields
- Reasoning Effort: select (default=xhigh) — Controls how much reasoning the model should perform.
- Enable Thinking: boolean (default=true) — Controls whether the model will think before replying
- Preserve Thinking: boolean (default=true) — Preserve reasoning content in all prior assistant turns instead of only the most recent one

### Parameters
- Min P Sampling: Disabled
- Presence Penalty: Disabled
- Repeat Penalty: Disabled
- Temperature: 1
- Top K Sampling: 20
- Top P Sampling: 0.95

### Sources — The underlying model files this model uses
- Based on lmstudio-community/Qwen3.8-27B-GGUF (GGUF)
- lmstudio-community/Qwen3.8-27B-MLX-4bit (MLX)
- lmstudio-community/Qwen3.8-27B-MLX-5bit (MLX)
- lmstudio-community/Qwen3.8-27B-MLX-6bit (MLX)
- lmstudio-community/Qwen3.8-27B-MLX-8bit (MLX)
