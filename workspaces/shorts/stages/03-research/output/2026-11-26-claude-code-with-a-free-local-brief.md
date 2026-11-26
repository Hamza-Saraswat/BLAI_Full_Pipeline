---
slug: 2026-11-26-claude-code-with-a-free-local
stage: 03-research
topic: "Claude Code with a free local LLM: the Ollama setup"
depth: standard
generated_at: 2026-11-26T12:47:25Z
sources: 16
hub: "[[videos/2026-11-26-claude-code-with-a-free-local]]"
---

# Research brief: Claude Code with a free local LLM: the Ollama setup

## Summary
The concrete case is a three-line redirect: a dummy token, a blanked API key and ANTHROPIC_BASE_URL=http://localhost:11434 -- or the single command ollama launch claude --model qwen3-coder. The arresting contrast is Ollama's default 4k context on machines under 24 GiB VRAM against its own docs floor of at least 64000 tokens for coding agents: the silent trap that breaks the setup on the first request. The money framing is Anthropic's own pricing: Pro is $20 if billed monthly, Claude Code is absent from the Free plan, and Max is $100 per month. What could not be verified: any official sentence saying Claude Code is free to use with your own models, and any tokens-per-second figure (no first-party measurement yet). The one conflict: Anthropic's docs say they do not support routing Claude Code to non-Claude models, while Ollama ships and documents that exact integration as its own feature.

## Thesis
Claude Code was never married to Anthropic's cloud: because Ollama's local server speaks the Anthropic Messages API, three environment variables put a free model you already own behind the same terminal agent, if your context length and tool-calling hold up.

## Explanation path
Start with what Claude Code actually is: a terminal client that sends Anthropic-format requests to whatever endpoint ANTHROPIC_BASE_URL names, which is why Claude Code's own docs describe the variable as changing where requests are sent, not which model answers them. Establish that Ollama implemented the Anthropic Messages API in v0.14.0, so a viewer's own machine can be that endpoint at http://localhost:11434. The connection itself is deliberately tiny: a dummy auth token, a blanked API key, the base URL -- or a single ollama launch claude line that sets all of it. Then come the two knobs that decide whether the redirect is worth anything. The model must be a real tool-caller: qwen3-coder:30b, a 19GB download that activates only 3.3B of its 30.5B parameters, or gpt-oss:20b, which its own page says runs on as little as 16GB of memory. And the server context must be raised, because Ollama's default on machines under 24 GiB VRAM is 4k tokens while its docs floor for agent and coding work is 64000. Once the setup works, the money lands: the same agent, zero per-prompt cost, no usage window. Close the loop with the honest catch: this is Ollama's engineering, not an Anthropic-supported path, and tool use is exactly where local models are weakest, so the honest promise is daily engineering work on your own box, not SWE-bench-scale refactors.

## Claims
1. **Ollama v0.14.0 and later answer the Anthropic Messages API, an ability announced January 16, 2026 that makes Claude Code drivable by open-source models.**
   - Source: Claude Code with Anthropic API compatibility · Ollama Blog, https://ollama.com/blog/claude
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "Ollama v0.14.0 and later are now compatible with the Anthropic Messages API, making it possible to use tools like Claude Code with open-source models."
2. **ANTHROPIC_BASE_URL changes where Claude Code's requests are sent, not which model answers them.**
   - Source: Model configuration - Claude Code Docs, https://code.claude.com/docs/en/model-config
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "ANTHROPIC_BASE_URL changes where requests are sent, not which model answers them."
3. **The official local setup is a dummy token, a blanked API key and the local base URL, then a model flag -- or the one-liner ollama launch claude.**
   - Source: Claude Code - Ollama, https://docs.ollama.com/integrations/claude-code
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "export ANTHROPIC_AUTH_TOKEN=ollama
     export ANTHROPIC_API_KEY=""
     export ANTHROPIC_BASE_URL=http://localhost:11434" and "ollama launch claude"
4. **Ollama defaults to a 4k context below 24 GiB VRAM (32k on 24-48 GiB, 256k at 48 GiB or more), its docs floor for agents and coding tools is at least 64000 tokens, and the server context is set with OLLAMA_CONTEXT_LENGTH=64000 ollama serve.**
   - Source: Context length - Ollama, https://docs.ollama.com/context-length
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "Tasks which require large context like web search, agents, and coding tools should be set to at least 64000 tokens." and "OLLAMA_CONTEXT_LENGTH=64000 ollama serve"
5. **qwen3-coder:30b, Ollama's current-generation coding pick, is a 19GB download with a 256K context window: 30.5B parameters at Q4_K_M with only 3.3B activated, 11.4M downloads, Apache 2.0.**
   - Source: qwen3-coder, https://ollama.com/library/qwen3-coder
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "qwen3-coder:30b offers 30B total parameters with only 3.3B activated, delivering strong performance while maintaining efficiency." and "19GB · 256K context window · Text"
6. **gpt-oss:20b is a 14GB download with 128K context whose own model page says it runs on systems with as little as 16GB memory, and its flagship sibling fits a single 80GB GPU.**
   - Source: gpt-oss, https://ollama.com/library/gpt-oss
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "enables the smaller model to run on systems with as little as 16GB memory, and the larger model to fit on a single 80GB GPU"
7. **Claude Code is unavailable on Anthropic's Free plan; the cheapest plan that includes it is Pro at $20 if billed monthly ($17 per month with annual subscription discount, $200 billed up front), and Max is $100 per month with 5x Pro usage every 5 hours and every week.**
   - Source: Plans & pricing | Claude by Anthropic, https://www.anthropic.com/pricing
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." and "Claude Code | No | Yes | Yes | Yes"
8. **Anthropic's own quickstart lists a Claude subscription, a Console account, or a supported cloud provider as the prerequisite before you begin.**
   - Source: Quickstart - Claude Code Docs, https://code.claude.com/docs/en/quickstart
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "A Claude subscription (Pro, Max, Ultra, Team, or Enterprise), Claude Console account, or access through a supported cloud provider"
9. **Anthropic does not support routing Claude Code to non-Claude models through any gateway, and while a gateway credential is active the subscription's usage limits do not apply to those requests.**
   - Source: Other LLM gateways - Claude Code Docs, https://code.claude.com/docs/en/llm-gateway
   - Tier: primary | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
   - Quote: "Anthropic doesn't endorse, maintain, or audit third-party gateway products, and doesn't support routing Claude Code to non-Claude models through any gateway." and "requests carry that credential in place of a developer's claude.ai subscription login, and the subscription's usage limits don't apply to them"
10. **The gap that decides whether local works is agentic tool use, not chat quality: the previous-generation Gemma 3 27B scored 6.6% on the τ2-bench tool-use benchmark, a 4K context is exhausted in seconds and silently truncates files mid-edit, and malformed tool-call JSON loops on Invalid tool parameters.**
    - Source: Local Agentic Programming on the Cheap: Claude Code + Ollama + Gemma4 - KDnuggets, https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4
    - Tier: benchmark | Confidence: high | Accessed: 2026-11-26 | Via: web_extract
    - Quote: "The previous generation, Gemma 3 27B, scored 6.6% on that same benchmark." and "Claude Code reports Invalid tool parameters repeatedly. The agent apologizes and retries with identical or nearly identical parameters, then loops."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Pro plan price (monthly billing) | $20 if billed monthly | https://www.anthropic.com/pricing | "$20 if billed monthly." |
| 2 | Ollama default context below 24 GiB VRAM | 4k context | https://docs.ollama.com/context-length | "< 24 GiB VRAM: 4k context" |
| 3 | Ollama docs floor for agents and coding tools | at least 64000 tokens | https://docs.ollama.com/context-length | "should be set to at least 64000 tokens" |
| 4 | Ollama blog minimum context for Claude Code | at least 32K tokens context length | https://ollama.com/blog/claude | "It is recommended to run a model with at least 32K tokens context length." |
| 5 | qwen3-coder:30b download size | 19GB | https://ollama.com/library/qwen3-coder | "19GB · 256K context window · Text" |
| 6 | qwen3-coder:30b activated parameters | only 3.3B activated | https://ollama.com/library/qwen3-coder | "30B total parameters with only 3.3B activated" |
| 7 | gpt-oss:20b minimum memory | as little as 16GB memory | https://ollama.com/library/gpt-oss | "run on systems with as little as 16GB memory" |
| 8 | Gemma 3 27B agentic tool use (τ2-bench) | 6.6% | https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4 | "Gemma 3 27B, scored 6.6% on that same benchmark." |

## Analogy candidates
- **A courier route with a changeable drop-off address**: Claude Code is the courier that always packs the same Anthropic-format boxes; ANTHROPIC_BASE_URL is only the delivery address, and Ollama is your garage that learned to sign for them. Breaks when: the receiving end had to implement the sender's exact protocol to sign at all, and once delivery is free the box quality depends on your garage's shelf space (VRAM), not the courier.
- **A home gym versus the gym membership**: Pro and Max are the all-inclusive gym whose front desk caps you every 5 hours and every week; the local model is the home gym with weights you already paid for (your GPU's memory) and no per-session fee. Breaks when: the workout spans many stations at once -- a large multi-file refactor -- where the gym's Opus-grade equipment still wins and your 30B home rack does not.
- **An engine that fires only some cylinders**: qwen3-coder:30b parks 30.5B parameters in the engine but burns only 3.3B per token, which is why a "30B" model runs at all on a 24 GB card. Breaks when: the whole engine still has to sit in the garage -- the full 19GB of weights is in memory even when only a few cylinders fire.

## Misconceptions
- Myth: You need an Anthropic API key or paid account to point Claude Code at Ollama. Reality: the official local setup exports a dummy token, blanks ANTHROPIC_API_KEY and talks to localhost; what you give up is Anthropic's endorsement and support, not a key (claim 3, claim 9).
- Myth: Any Ollama chat model can drive Claude Code. Reality: the model must call tools and hold context -- the docs floor for agent work is at least 64000 tokens and the old open model scored 6.6% on the tool-use benchmark (claim 4, claim 10).
- Myth: A 30B-parameter model needs roughly 30GB of memory. Reality: qwen3-coder:30b is 30.5B parameters but downloads as a 19GB file at Q4_K_M and activates only 3.3B per token (claim 5).
- Myth: Set ANTHROPIC_BASE_URL and it just works. Reality: out of the box Ollama serves a 4k context below 24 GiB VRAM, which an agentic session exhausts in seconds while silently truncating files mid-edit; raise OLLAMA_CONTEXT_LENGTH before judging the model (claim 4, claim 10).

## Glossary
- **token**: the unit a language model reads and writes in, roughly a short word or word fragment, and the unit context length is counted in.
- **context window (context length)**: the maximum number of tokens the model can hold in memory at once, per Ollama's docs "the maximum number of tokens that the model has access to in memory".
- **environment variable**: a named setting stored in your shell that programs read when they start, used here to redirect Claude Code's traffic.
- **base URL (endpoint)**: the network address a client sends its API requests to; swapping Anthropic's server for localhost:11434 is the whole redirect.
- **tool calling**: the model's ability to request real actions (read a file, edit a file, run a command) instead of only producing text.
- **model tag**: the suffix after the colon that picks a model variant and size, as in qwen3-coder:30b.
- **quantization (Q4_K_M)**: storing weights at roughly 4 bits instead of 16, shrinking a 30.5B-parameter model to a 19GB file at a small quality cost.
- **mixture of experts (MoE)**: an architecture where only a fraction of the total parameters fire for each token, so total size and per-token compute differ.
- **activated parameters**: the subset of an MoE's weights used per token, e.g. only 3.3B of qwen3-coder:30b's 30.5B.
- **VRAM**: the memory on your graphics card, which decides how big a model and how large a context Ollama will run; a Mac's shared pool counts too ("memory or unified memory").
- **KV cache**: the extra memory the model needs on top of its weights to hold the conversation so far; it grows with context length and pages to disk when it outgrows memory.
- **τ2-bench**: a benchmark scoring how reliably a model calls tools, executes steps and handles errors across a multi-step agentic workflow -- exactly what Claude Code demands.

## Unverified
- No fetched code.claude.com or anthropic.com page states that Claude Code itself is free to use with your own models or gateways; the quickstart prerequisite points the other way, so the video must not claim Anthropic's blessing for this path.
- Which Ollama version introduced the ollama launch claude launcher, and any minimum Claude Code version for the integration, are not stated on any fetched page.
- The claim that a 24 GB card fits qwen3-coder:30b with room for context is derived arithmetic from the 19GB file size, not a vendor statement; no Ollama-published table maps models to specific consumer GPUs.
- No AMD- or Mac-specific performance guidance was fetched; memory-fit statements rest on Ollama's generic "memory or unified memory" wording.
- Tokens per second on any specific machine has no number here; that is a first-party measurement for the build stage, not a web fact.
- A Medium "reality check" article was unreachable (server 500 on two attempts) and contributed nothing to this brief.

## Suggested outline
1. Open on the meter: Pro is $20 a month, Max is $100 with caps every 5 hours, and the Free plan has no Claude Code at all.
2. Land the mechanism: ANTHROPIC_BASE_URL changes where requests are sent, not which model answers them, and Ollama has spoken Anthropic's Messages API since v0.14.0.
3. Show the three lines: a dummy token, a blanked key, the local base URL -- or the single command ollama launch claude --model qwen3-coder.
4. Pick the model by hardware: qwen3-coder:30b is a 19GB download with only 3.3B parameters active per token; gpt-oss:20b runs on as little as 16GB.
5. Defuse the trap: Ollama's default context is 4k below 24 GiB VRAM while agent work wants at least 64000 tokens, so set OLLAMA_CONTEXT_LENGTH before judging the model.
6. Close on the honest catch: Anthropic does not support routing Claude Code to non-Claude models and tool use is where local models fall over (6.6% for the old open model on the tool-use benchmark), then the payoff: same terminal, same agent, zero dollars per prompt.

## Viewer situation
You already use Claude Code on a Pro plan, or you have wanted a terminal coding agent, and a gaming PC or Mac with 16 to 24 GB of memory is sitting right there.

## Has process
`true`
- Install Ollama and pull a tool-calling coding model sized to your memory (ollama pull qwen3-coder:30b for a 24 GB card, gpt-oss:20b for 16 GB).
- Set the server context before serving: OLLAMA_CONTEXT_LENGTH=64000 ollama serve.
- Point Claude Code at the local server: export ANTHROPIC_AUTH_TOKEN=ollama, export ANTHROPIC_API_KEY="", export ANTHROPIC_BASE_URL=http://localhost:11434 -- or run ollama launch claude --model qwen3-coder.
- Start Claude Code and run /status to confirm the connection.

## Objection
Anthropic does not support this path, and a local model that scores 6.6% on tool use will spend your evening emitting broken tool JSON -- the free prompts cost you the thing you were actually buying, an agent that finishes the job.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://docs.ollama.com/integrations/claude-code | Claude Code - Ollama | primary | web_extract | 2026-11-26 |
| 2 | https://ollama.com/blog/claude | Claude Code with Anthropic API compatibility · Ollama Blog | primary | web_extract | 2026-11-26 |
| 3 | https://code.claude.com/docs/en/model-config | Model configuration - Claude Code Docs | primary | web_extract | 2026-11-26 |
| 4 | https://docs.ollama.com/context-length | Context length - Ollama | primary | web_extract | 2026-11-26 |
| 5 | https://ollama.com/library/qwen3-coder | qwen3-coder | primary | web_extract | 2026-11-26 |
| 6 | https://ollama.com/library/qwen3-coder:30b | qwen3-coder:30b | primary | web_extract | 2026-11-26 |
| 7 | https://ollama.com/library/gpt-oss | gpt-oss | primary | web_extract | 2026-11-26 |
| 8 | https://ollama.com/library/qwen2.5-coder | qwen2.5-coder | primary | web_extract | 2026-11-26 |
| 9 | https://ollama.com/library/kimi-k2.7-code | kimi-k2.7-code | primary | web_extract | 2026-11-26 |
| 10 | https://www.anthropic.com/pricing | Plans & pricing | Claude by Anthropic | primary | web_extract | 2026-11-26 |
| 11 | https://code.claude.com/docs/en/quickstart | Quickstart - Claude Code Docs | primary | web_extract | 2026-11-26 |
| 12 | https://code.claude.com/docs/en/llm-gateway | Other LLM gateways - Claude Code Docs | primary | web_extract | 2026-11-26 |
| 13 | https://code.claude.com/docs/en/costs | Manage costs effectively - Claude Code Docs | primary | web_extract | 2026-11-26 |
| 14 | https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4 | Local Agentic Programming on the Cheap: Claude Code + Ollama + Gemma4 - KDnuggets | benchmark | web_extract | 2026-11-26 |
| 15 | https://github.com/ollama/ollama/issues/15390 | Claude Code & Ollama Integration - Invalid tool parameters & CPU Fallback · Issue #15390 · ollama/ollama | community | web_extract | 2026-11-26 |
| 16 | https://michaelwolfinger.com/blog/2026/claude-code-ollama-local-llm/ | Run Claude Code with Ollama: ollama launch claude, manual setup, context length, models | community | web_extract | 2026-11-26 |

## Notes
Ran on web_search + web_extract with FireCrawl out of credits (402); 16 pages fetched across three research subagents plus one orchestrator fetch; the Micro Center walkthrough from the ideas note was intentionally not fetched so this brief stands on primary pages. Conflict to carry into the script: Anthropic's docs list a paid path as the prerequisite and disown routing Claude Code to non-Claude models (llm-gateway page), while Ollama publishes and maintains the integration as a feature of its own server; present the setup as Ollama's engineering, not Anthropic's blessing. Thin spots: no vendor statement that a 24 GB card fits qwen3-coder:30b (the 19GB file size is the verbatim fact); no tokens-per-second number exists until the build stage measures one; kimi-k2.7-code is cloud-only on Ollama ($0.95 input / $4.00 output per 1M tokens, 1.04T parameters), so it must not be presented as a free local option.
