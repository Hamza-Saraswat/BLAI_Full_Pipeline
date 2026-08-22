# Content Pillars

Agents load only the pillar or series section the current run falls under.

## Shorts Lanes

| Lane | Angle | Topic fit | Default structures (see `workspaces/shorts/stages/04-script/references/script-structures.md`) |
|------|-------|-----------|------------------------------------------------------------------------|
| `news-react` | A thing shipped this week; here is the one consequence for people running AI at home | model releases, runtime releases, price changes, policy | number-first, news-react-so-what |
| `myth-bust` | Everyone says X; the measurement says Y | "you need a 4090", "local is slow", "cloud is cheaper" | myth-bust, contrarian-take |
| `comparison` | Two named things, one decision | DGX Spark vs RTX 5090, vLLM vs llama.cpp, Q4 vs Q8 | comparison-ladder, number-first |
| `how-to` | Three moves that get the viewer from nothing to running | install, load, tune, serve | how-to-three-moves, worked-example |
| `explainer` | One concept made physical | quantization, MoE, KV cache, bandwidth, context length | worked-example, story-first |
| `enterprise-privacy` | Why a clinic, law firm or shop cannot paste data into a cloud model, and what to run instead | compliance, leaks, EU AI Act, on-prem | story-first, news-react-so-what |

Rotation: pillar and structure must differ from the previous day's picks; at most one `news-react` per day.

## Long-form Series

| Series | Angle | Episode shapes | Default scene types |
|--------|-------|----------------|---------------------|
| `local-ai-for-dummies` | One concept per episode, explained from zero with one worked example carried the whole way | "What is a token, really", "Why your GPU's doorway matters" | kinetic-text, diagram, comparison-table, mascot-talk |
| `my-dgx-spark-projects` | What I built on the Spark this week, with the real numbers and the real failures | fine-tune runs, serving setups, agent experiments | terminal-replay, code-typing, stat-callout, chapter-card |
| `benchmarks` | Named models on named hardware, measured by us | tokens per second, load time, memory, quality spot checks | chart, comparison-table, terminal-replay |
| `inference-engineering-at-home` | The flags and formats that change what fits and how fast it runs | quantization formats, KV cache, FP8/FP4, batch size, context | code-typing, diagram, stat-callout |
| `dgx-spark-specific` | Everything NVIDIA-specific about the box | firmware, drivers, containers, networking two Sparks | terminal-replay, diagram |
| `beyond-llms` | Video, voice and image models you can run locally | TTS, image generation, video models, speech-to-text | comparison-table, b-roll, stat-callout |

Rotation: no series twice in a row. The `my-dgx-spark-projects` series draws from notes in `workspaces/long-form/input/` (the priority lane).
