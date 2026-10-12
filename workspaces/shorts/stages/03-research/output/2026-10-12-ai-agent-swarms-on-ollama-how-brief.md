---
slug: 2026-10-12-ai-agent-swarms-on-ollama-how
stage: 03-research
topic: "How AI agent swarms actually work when the models run locally on Ollama"
depth: standard
generated_at: 2026-10-12T11:39:03Z
sources: 11
hub: "[[videos/2026-10-12-ai-agent-swarms-on-ollama-how]]"
---

# Research brief: AI agent swarms on Ollama: how they actually work

## Summary
The hook is live and current: an Ask HN poster quotes Karpathy on labs running swarms of thousands of agents while admitting he cannot get 3 to cooperate. The most arresting number is the cost gap: GPT-6.1 Sol charges $2.00 / 1M input tokens while a DGX Spark, a box NVIDIA markets for exactly this workload, draws from a 240 Watts power supply. The strongest concrete case is AutoGen's SelectorGroupChat, where a model literally picks the next speaker and every reply is broadcast to the whole team. Not verified anywhere: a cents-per-million-token figure for local inference, which no fetched page computes and our own hardware would have to measure. One wrinkle the writer must not trip on: CrewAI's docs show base_url http://localhost:11434 while Ollama's own examples standardize on the /v1 suffix, and both hit the same server.

## Thesis
A swarm is not many minds on your machine but one local model taking turns through roles, and once Ollama serves those turns your marginal token is paid in electricity and RAM, not a per-token bill.

## Explanation path
Start from what the viewer already owns: one model in a chat window, where every answer is one model reading a prompt and writing a reply. An agent is that same loop dressed with a name, a role description, and tools, so nothing exotic has to be bought for swarming to make sense. The swarm is the coordination layer sitting over those agents: something must decide who goes next, and that something is usually itself a model call, whether it is AutoGen's selector reading the shared conversation, an OpenAI Agents SDK handoff disguised as a tool call, or LangGraph edges routing between nodes that read and write one shared state object. Establish what actually travels between agents, messages, tool results, and task objects riding a shared conversation or state, before any hardware enters, because the coordination pattern rather than the model count is what defines the system. Then move the whole thing onto the viewer's machine: every agent points at the same Ollama server through its OpenAI-compatible endpoint at http://localhost:11434/v1, which is why framework code written for a cloud API turns local by changing one base_url line. With the wiring understood, the economics land as a reversal: a cloud swarm meters every coordination token at a posted per-million price, while the local swarm's marginal token comes from a box with a fixed watt ceiling, so cost moves from the invoice to the wall socket and the memory. Close on the honest catch, the MAST finding that multi-agent failures cluster into coordination problems with 14 named modes, so the payoff is the viewer knowing a local swarm buys unlimited cheap tokens, not unlimited good ones, and that parallelism is paid for in RAM.

## Claims
1. **The question is real and current: an Ask HN thread quotes Karpathy that frontier labs look like "swarms of thousands of agents collaborating over weeks on software mega projects" while the poster admits "I'm already struggling to get 2-3 agents to work together reliably."**
   - Source: Ask HN: How do swarms of AI agents work?, https://news.ycombinator.com/item?id=50047180
   - Tier: community | Confidence: medium | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "I'm already struggling to get 2-3 agents to work together reliably. I can't really wrap my head around how you'd coordinate thousands of them"
2. **In the OpenAI Agents SDK, a handoff between agents is represented to the model as an ordinary tool call with a name like transfer_to_refund_agent, so delegation is just routing.**
   - Source: Handoffs - OpenAI Agents SDK, https://openai.github.io/openai-agents-python/handoffs/
   - Tier: primary | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "Handoffs are represented as tools to the LLM. So if there's a handoff to an agent named `Refund Agent`, the tool would be named `transfer_to_refund_agent`."
3. **Microsoft AutoGen's SelectorGroupChat implements the orchestrator pattern: a generative model reads the shared conversation plus each agent's name and description to pick the next speaker, whose response is then broadcast to all other participants before a termination condition is checked.**
   - Source: Selector Group Chat - AutoGen, https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html
   - Tier: docs | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "A generative model (e.g., an LLM) selects the next speaker based on the shared context, enabling dynamic, context-aware collaboration."
4. **LangGraph implements the shared-blackboard pattern: agents are nodes, functions that encode agent logic, that read and write a single shared state object while edges decide which node runs next, in the docs' own words "nodes do the work, edges tell what to do next."**
   - Source: Graph API overview - Docs by LangChain, https://langchain-ai.github.io/langgraph/concepts/multi_agent/
   - Tier: docs | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "In short: nodes do the work, edges tell what to do next."
5. **A swarm reaches local models through Ollama's OpenAI-compatible endpoint: any OpenAI client points at base_url http://localhost:11434/v1/ and the API key is required but ignored.**
   - Source: OpenAI compatibility - Ollama, https://docs.ollama.com/api/openai-compatibility
   - Tier: primary | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "The client requires an API key value, but Ollama ignores it."
6. **CrewAI's docs give the local recipe in three moves, install Ollama, run a model, then configure LLM(model="ollama/llama3:70b", base_url="http://localhost:11434"), so a crew of agents shares one local server.**
   - Source: LLMs - CrewAI, https://docs.crewai.com/concepts/llms
   - Tier: docs | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "llm = LLM(model=\"ollama/llama3:70b\", base_url=\"http://localhost:11434\")"
7. **AutoGen ships a dedicated OllamaChatCompletionClient that assumes your Ollama server runs locally on port 11434, while warning that small local models are typically not as capable as larger cloud models.**
   - Source: Models - AutoGen, https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html
   - Tier: docs | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "Small local models are typically not as capable as larger models on the cloud. For some tasks they may not perform as well and the output may be suprising."
8. **A local swarm's real ceiling is memory, governed by two Ollama defaults: OLLAMA_NUM_PARALLEL, parallel requests each model processes at the same time, default 1, and OLLAMA_MAX_LOADED_MODELS, default 3 * the number of GPUs or 3 for CPU inference, with required RAM scaling by OLLAMA_NUM_PARALLEL * OLLAMA_CONTEXT_LENGTH.**
   - Source: FAQ - Ollama, https://docs.ollama.com/faq
   - Tier: primary | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "Required RAM will scale by `OLLAMA_NUM_PARALLEL` * `OLLAMA_CONTEXT_LENGTH`."
9. **NVIDIA sells DGX Spark explicitly for this workload, saying its stack lets "agents and large models run locally, reducing the need for cloud-based token generation resources," inside a 240 Watts power supply with a 140 W GB10 chip TDP, and its ConnectX networking links up to four Sparks to run multi-agent workloads.**
   - Source: NVIDIA DGX Spark, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
   - Tier: primary | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
   - Quote: "Large local memory, powerful AI compute and the NVIDIA AI software stack enable agents and large models to run locally, reducing the need for cloud-based token generation resources."
10. **The largest published audit of multi-agent failures, MAST, annotated 1600+ traces across 7 popular MAS frameworks and identified 14 unique failure modes clustered into 3 categories: system design issues, inter-agent misalignment, and task verification.**
    - Source: Why Do Multi-Agent LLM Systems Fail?, https://arxiv.org/abs/2503.13657
    - Tier: primary | Confidence: high | Accessed: 2026-10-12 | Via: web_extract
    - Quote: "This process identifies 14 unique modes, clustered into 3 categories: (i) system design issues, (ii) inter-agent misalignment, and (iii) task verification."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | OLLAMA_NUM_PARALLEL default (parallel requests each model processes at once) | 1 | https://docs.ollama.com/faq | "The maximum number of parallel requests each model will process at the same time, default 1." |
| 2 | OLLAMA_MAX_LOADED_MODELS default (models loaded concurrently) | 3 * the number of GPUs or 3 for CPU inference | https://docs.ollama.com/faq | "The default is 3 * the number of GPUs or 3 for CPU inference." |
| 3 | Ollama default context window | 4096 tokens | https://docs.ollama.com/faq | "By default, Ollama uses a context window size of 4096 tokens." |
| 4 | GPT-6.1 Sol input price (standard processing, OpenAI pricing page, 2026-10-12) | $2.00 / 1M tokens | https://openai.com/api/pricing/ | "Input:$2.00 / 1M tokens" |
| 5 | GPT-6.1 Sol output price (standard processing, OpenAI pricing page, 2026-10-12) | $10.00 / 1M tokens | https://openai.com/api/pricing/ | "Output:$10.00 / 1M tokens" |
| 6 | DGX Spark whole-system power supply | 240 Watts | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "Power Supply | 240 Watts |" |
| 7 | GB10 chip thermal design power (CPU and GPU) | 140 W | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "GB10 TDP1 | 140 W |" |
| 8 | MAST-Data annotated multi-agent traces (across 7 frameworks) | 1600+ | https://arxiv.org/abs/2503.13657 | "a comprehensive dataset of 1600+ annotated traces collected across 7 popular MAS frameworks" |

## Analogy candidates
- **A kitchen brigade**: The orchestrator is the head chef who plans and delegates but never cooks, agents are stations, and orders ride the rail as messages; the pass where every finished plate lands is the shared conversation. Breaks when: a brigade's stations are genuinely different skills, while swarm agents are one model wearing different prompt hats, so any agent could in principle work any station.
- **A group chat with a moderator**: AutoGen's SelectorGroupChat is literally a chat where a model moderates, picking the next speaker from each member's name and description, every reply broadcast to all, until a termination condition fires. Breaks when: human chatters bring separate memories and minds, while these agents share one context window and often one model, one mind with name tags.
- **An all-you-can-eat buffet versus a la carte**: Cloud APIs charge per plate, $2.00 / 1M tokens input on GPT-6.1 Sol, while the local box is a flat-rate buffet where the stove is already on. Breaks when: the buffet has one stove, so extra diners queue instead of eating in parallel, and the real limit is pantry size, meaning RAM, not appetite.

## Misconceptions
- Myth: Every agent in a swarm needs its own model or its own GPU. Reality: agents are role prompts hitting the same endpoint; AutoGen's docs build a whole team on one model client, and Ollama's OLLAMA_MAX_LOADED_MODELS default of 3 models is a ceiling you could hit, not a floor you need (claims 3, 8).
- Myth: More agents means better output. Reality: the MAST audit of 1600+ traces found 14 failure modes and shows coordination design, not model capability, is where multi-agent systems break (claim 10).
- Myth: A local swarm is free to scale up. Reality: tokens stop costing dollars but parallelism costs memory, since Ollama's required RAM scales by OLLAMA_NUM_PARALLEL * OLLAMA_CONTEXT_LENGTH and its default is 1 parallel request per model (claim 8).

## Glossary
- **agent**: A model in a loop, given a name, a role description, and tools, that reads messages and produces messages or tool calls.
- **swarm**: Several agents coordinated so tasks decompose and results combine, what researchers call a multi-agent system.
- **orchestrator**: The agent or mechanism that decides which agent works next, either by selecting a speaker or by routing handoffs.
- **handoff**: A delegation from one agent to another that the OpenAI Agents SDK represents to the model as a tool call.
- **shared state**: The single data object that every agent node reads from and writes to, the blackboard in LangGraph's graph model.
- **token**: The chunk of text, roughly a word fragment, that models consume and emit and that cloud APIs bill by the million.
- **endpoint**: The URL a framework sends model requests to, such as Ollama's http://localhost:11434/v1.
- **base URL**: The base_url config field where swapping the cloud address for the local one re-points an entire swarm.
- **OLLAMA_NUM_PARALLEL**: The Ollama setting for how many requests one model processes simultaneously, default 1, with RAM scaling by it times the context length.
- **context window**: How much text a model can hold at once, 4096 tokens under Ollama's default.
- **termination condition**: The rule, such as a stop word like TERMINATE or a message cap, that tells a swarm to halt.

## Unverified
- No fetched page computes a cents-per-million-token cost for local inference; any such figure must wait for a first-party measurement on our own hardware.
- How many tokens per second a three-agent swarm actually sustains on consumer GPUs is unmeasured here.
- That frontier labs really run thousands of concurrent agents rests on Karpathy's post quoted in a community thread, not on a primary source.
- Whether a single Ollama instance bottlenecks beyond three concurrent agents on 8 to 24 GB cards is community folklore until we measure it.

## Suggested outline
1. Open on the gap: Karpathy's thousands of agents versus an Ask HN poster who cannot get 3 to cooperate.
2. Name the trick: a swarm is one model, many roles, taking turns.
3. Show what travels: messages, tool results, and task objects riding a shared conversation or state.
4. Contrast the coordination shapes: a selector or handoff picks the next agent versus a shared blackboard every agent reads.
5. Wire it locally: one line, base_url http://localhost:11434/v1, turns cloud swarm code into local swarm code.
6. Flip the meter: $2.00 / 1M input tokens in the cloud versus a 240 Watts box that never meters.
7. Admit the real bill: RAM scales by OLLAMA_NUM_PARALLEL times OLLAMA_CONTEXT_LENGTH, default 1 parallel slot.
8. Land the honest catch: MAST's 1600+ traces and 14 failure modes, coordination fails, not the model.
9. Close: electricity, not dollars, so swarm cheap but verify everything.

## Viewer situation
You run a model like llama3.2 in Ollama on your own GPU and talk to it one prompt at a time, and you have heard about agent swarms but never wired one up.

## Has process
`true`
- Install Ollama and pull a model with ollama run llama3
- Point your framework's LLM config at the local server with model "ollama/llama3:70b" and base_url "http://localhost:11434"
- Define each agent's name, description, and role so a selector or handoff can route between them
- Give the team a termination condition, a stop word or message cap, so the run ends

## Objection
Cheap tokens are not free results: every handoff re-sends context through a small local model, so a swarm that loops burns your night and your RAM even when it never bills a card.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://news.ycombinator.com/item?id=50047180 | Ask HN: How do swarms of AI agents work? | community | web_extract | 2026-10-12 |
| 2 | https://openai.github.io/openai-agents-python/handoffs/ | Handoffs - OpenAI Agents SDK | primary | web_extract | 2026-10-12 |
| 3 | https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html | Selector Group Chat - AutoGen | docs | web_extract | 2026-10-12 |
| 4 | https://langchain-ai.github.io/langgraph/concepts/multi_agent/ | Graph API overview - Docs by LangChain | docs | web_extract | 2026-10-12 |
| 5 | https://docs.ollama.com/api/openai-compatibility | OpenAI compatibility - Ollama | primary | web_extract | 2026-10-12 |
| 6 | https://docs.crewai.com/concepts/llms | LLMs - CrewAI | docs | web_extract | 2026-10-12 |
| 7 | https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html | Models - AutoGen | docs | web_extract | 2026-10-12 |
| 8 | https://docs.ollama.com/faq | FAQ - Ollama | primary | web_extract | 2026-10-12 |
| 9 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | NVIDIA DGX Spark | primary | web_extract | 2026-10-12 |
| 10 | https://arxiv.org/abs/2503.13657 | Why Do Multi-Agent LLM Systems Fail? | primary | web_extract | 2026-10-12 |
| 11 | https://openai.com/api/pricing/ | Business Pricing \| OpenAI | primary | web_extract | 2026-10-12 |

## Notes
CrewAI's docs point at http://localhost:11434 through the LiteLLM provider while Ollama's own compatibility examples standardize on http://localhost:11434/v1; both reach the same server, and the narration should pick one form and stay consistent. The Karpathy "thousands of agents" line is community tier and should stay framed as a quote from a post, not an established fact. The electricity-per-token math is deliberately not claimed anywhere in this brief; the writer can contrast $2.00 / 1M tokens against a 240 Watts box without asserting a computed local per-token price.
