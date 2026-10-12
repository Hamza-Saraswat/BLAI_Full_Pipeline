---
slug: 2026-10-12-ai-agent-swarms-on-ollama-how
stage: 04-script
generated_at: 2026-10-12
judge: kimi-k3 (blind, three separate llm_call processes)
---

# Drafts and scores: 2026-10-12-ai-agent-swarms-on-ollama-how

Both drafts passed all machine gates before judging (validator 0 blockers 0 advisories, eval gate1_ready true, variety ok). Draft B is shown as judged; the two grafts applied to the winner are listed after the score table.

## Draft A (structure: worked-example, hook pattern: situation)

TITLE: How an Ollama Agent Swarm Actually Works

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | You've got Ollama running. A swarm is one line away. One model on your G P U, one prompt at a time. | You've got Ollama running. | Terminal on dark background; frame 1 shows "You've got Ollama running." fully legible. At 0.4 s it fades out as the next line fades in under a blinking amber cursor. | hyperframes | centered-stack | 6.9 |
| s02 | turn | An agent is your Ollama chat model with extras: a name, a role, and a tool it can call. Meet Researcher. It still reads messages and writes replies. | one model, plus name, role, tool | Chat loop icon; three tags fade in one at a time on "a name, a role, and a tool", then the card stamps "Researcher". | manim | diagram-flow | 9.7 |
| s03 | turn | Add a second agent, Writer, and you have a swarm. Somebody must pick who speaks. AutoGen lets the model itself pick, from each agent's name and description. Picture a group chat with a moderator. Except every chatter is one model wearing name tags. | selector picks the next speaker | Two cards, Researcher and Writer, in a grid; an amber selector chip scales in on "the model itself pick" and points between them. | manim | grid | 14.8 |
| s04 | mechanism | Here's what travels: messages and answers from tools. AutoGen broadcasts every reply to the whole team, so both agents share one conversation. A stop word or message cap, the termination condition, ends the run. | every reply goes to everyone | A reply bubble rises from Researcher and duplicates to both cards on "broadcasts every reply"; a shared transcript grows, then a small TERMINATE chip fades in. | manim | diagram-flow | 11.7 |
| s05 | turn | This team still points at a cloud A P I. Point it home. One line, base U R L, points every agent at your Ollama server. Port eleven four three four, slash v one. The A P I key is required, and ignored. | localhost:11434/v1 | Config file view; the line highlights on "One line" while a cloud icon fades into a small local tower. Code centered, amber highlight. | hyperframes | centered-stack | 14.8 |
| s06 | contrast | On the cloud, every one of those broadcasts is billed. G P T six point one Sol charges two dollars per million input tokens, the chunks of text a model reads. A swarm re-sends its conversation with every turn. | GPT-6.1 Sol $2.00 / 1M input tokens | Giant price scales in on "two dollars"; behind it a tiny transcript loops while a meter spins on each resend. | hyperframes | giant-number | 13.8 |
| s07 | turn | At home, the meter disappears. NVIDIA's D G X Spark, a box sold for exactly this job, runs on a two hundred forty watt power supply. Your next token costs electricity, not dollars. | DGX Spark 240 W power supply | Split screen: left, an invoice stamping per message; right, a wall plug whose amber watt readout rises to 240 on "two hundred forty watt". | hyperframes | split-compare | 10.7 |
| s08 | mechanism | The bill comes in memory instead. Ollama's default is one parallel request per model. The team takes turns. More slots cost more memory: slots times the context window, the text the model holds at once. | RAM = slots × context | One conveyor slot feeds a model block on "one parallel request"; a second slot fades in and the RAM bar doubles on "More slots cost more memory". | manim | diagram-flow | 12.1 |
| s09 | honest_catch | Cheap tokens are not free results. MAST, the largest failure audit, read over sixteen hundred annotated traces of real runs. It found fourteen unique failure modes. They cluster in coordination, not model quality. | 14 failure modes | Giant amber 14 rises on "fourteen unique failure modes"; faint rows of trace thumbnails sit behind it. | hyperframes | giant-number | 11.4 |
| s10 | payoff_close | A local swarm buys you unlimited cheap tokens, not unlimited good ones. It was one line. The rest is your model taking turns. | A swarm is one line away. | The terminal from frame 1 returns; the line settles on "taking turns", cursor blinks, wordmark fades in for the final half second. | hyperframes | centered-stack | 7.9 |

NOTES: Analogy: AutoGen's selector as a group chat with a moderator (s03); its limit lands in the same scene: "except every chatter is one model wearing name tags". Screen numbers spent: $2.00/1M (s06), 240 W (s07), 14 (s09); port 11434 appears inside the endpoint text and is spoken in-scene. Hedged by omission: no local per-token price is claimed (brief lists it Unverified), and the Karpathy "thousands of agents" line stays out entirely since it is community tier.

## Draft B (structure: myth-bust, hook pattern: named-contradiction) -- WINNER

TITLE: How an Agent Swarm Runs on One Local Model

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| s01 | hook | Three agents. One model. No per-token bill. You run one model in Ollama, prompt by prompt. A swarm sounds like three models on three graphics cards. | Three agents. One model. No per-token bill. | Frame 1: hook text fully legible, amber accent, centered above the caption band. At 0.35 s three agent chips scale in and merge into one model card on "One model"; two spare card outlines fade out on "three graphics cards". | hyperframes | centered-stack | 9.0 |
| s02 | mechanism | An agent is your Ollama chat with a name, a role, and tools. The same model answers as each agent. Three agents is one model taking turns. | name + role + tools | On "a name, a role, and tools" a loop diagram, prompt arrow to model box to reply, fades in while three tags rise onto the single model box. On "taking turns" a dot cycles through the tags, one at a time. | manim | diagram-flow | 9.3 |
| s03 | mechanism | So who speaks next? AutoGen's SelectorGroupChat hands that choice to a model. It reads the shared conversation and picks the next speaker. Each reply is broadcast to the whole team. | who speaks next? | On "who speaks next" a chat thread rises message by message. On "picks the next speaker" an amber marker hops to one avatar, and on "broadcast" the new reply fades in under every name. | hyperframes | timeline | 10.3 |
| s04 | evidence | OpenAI's Agents SDK does it with a tool call. A handoff, one agent passing the task, is a tool called transfer to refund agent. LangGraph instead shares one state, a common board every agent reads and writes. | handoff = tool call / one shared board (sequential) | On "transfer to refund agent" a tool-call chip scales in on the left panel. On "common board" the right panel fades in, one board filling as two agent icons write to it; the second label rises only after the first settles. | hyperframes | split-compare | 12.8 |
| s05 | turn | Every framework points at a base U R L, the address for model requests. Set it to localhost, port eleven thousand four hundred thirty-four. One line re-points the swarm to your Ollama server. The client demands an A P I key; Ollama ignores it. | base_url = localhost:11434 | On "base U R L" a config card fades in showing the base_url line, then the localhost address scales in as the port is spoken. On "ignores it" the API key field fades to grey. | hyperframes | centered-stack | 15.2 |
| s06 | contrast | The deeper change is the bill. G P T six point one Sol charges two dollars per million input tokens, chunks of text. Every message between agents pays that meter. | GPT-6.1 Sol: $2.00 / 1M input tokens | On "two dollars" a giant price scales in with the model caption beneath. On "pays that meter" a small meter ticks up beside each message in the thread. | hyperframes | giant-number | 10.3 |
| s07 | contrast | Your box never meters a token. NVIDIA's D G X Spark, built for this workload, ships with a two hundred forty watt power supply. Cloud charges per plate. Your box is a buffet, stove already on. | 240 W power supply | On "power supply" the frame splits: an invoice card fades out left while a wall plug and the wattage rise in right. On "stove already on" a stove icon glows amber. | hyperframes | split-compare | 12.4 |
| s08 | honest_catch | The buffet has one stove, though. Ollama serves one request at a time by default, and extra parallel slots cost memory. Your three agents take turns. Want them at once? Then the myth has a point: parallelism costs memory. | more parallel = more RAM | On "one request at a time" three agent chips queue at a single stove slot. On "parallelism costs memory" a memory bar rises and the equation fades in above it. | manim | diagram-flow | 13.4 |
| s09 | evidence | The honest catch: MAST, the largest published audit of multi-agent failures. It annotated more than sixteen hundred traces, records of real swarm runs. | MAST: why swarms fail | On "sixteen hundred traces" rows of trace cards rise in fast, staggered, filling a grid under the heading. | hyperframes | grid | 7.9 |
| s10 | payoff_close | It sorted them into fourteen failure modes, mostly coordination, not weak models. So a local swarm buys you unlimited cheap tokens, not unlimited good ones. | 14 failure modes / Three agents. One model. Cheap tokens. (sequential) | On "fourteen failure modes" the digits scale in over the dimmed grid. On "cheap tokens" the text cross-fades to the closing line, rhyming frame 1, then the wordmark settles for the final half second. | hyperframes | centered-stack | 8.6 |

NOTES: One analogy: cloud per-plate billing versus a buffet with the stove already on (s07), with its limit stated at the top of s08, one stove so requests queue and memory is the real cap. Key numbers spent on screen: $2.00 / 1M input tokens (s06), 240 W (s07), 14 failure modes (s10); the sixteen hundred traces are spoken only, and port 11434 is shown so it is spoken. Hedged by omission: no local cents-per-token figure and no Karpathy line, both Unverified in the brief; used the bare localhost:11434 form per the brief's endpoint note, and dropped the termination-condition step for time.

## Judge verdict (verbatim)

WINNER: B
TOTAL_A: 20/24
TOTAL_B: 24/24
SCORES_A: 2,2,3,3,3,2,2,3
SCORES_B: 3,3,3,3,3,3,3,3
GRAFTS:
- A s06 sentence "A swarm re-sends its conversation with every turn." moves into B s06 after "chunks of text." — B states the meter but never the mechanism that makes it spin; this adds the compounding-cost cause with no new number and no rewrite of surrounding beats.
- A s04 sentence "A stop word or message cap, the termination condition, ends the run." appends to B s03 after the broadcast sentence — B's own notes admit dropping the termination step the brief's process requires, and the line is native to SelectorGroupChat's loop, so it slots in untouched.
LOSER_NEEDS: A's situation hook names a product but carries no tension in its first five words, and its promised "one line" is not shown until roughly second 50, so it needed a contradiction or number up front and a much earlier payoff. It also appends two sentences after its most repeatable line, and its worked-example-plus-situation fingerprint exactly repeats the 2026-10-08 ledger entry, costing it the variety row as well.
REASON: Both drafts are equally specific, drift-free, clean in voice, and tightly chained, so the match is decided at the opening and the close. B's named-contradiction hook lands numbers and felt tension inside five words and, per the myth-bust fairness rule, its break pays the hook's promise immediately, while A's hook is product-name-only and its first concrete beat arrives around second 7. B ends on the repeatable payoff line as the last thing heard and presents a fresher fingerprint against the ledger, taking rows 1, 2, 6, and 7.

## Score table

| Row | A | B |
|-----|---|---|
| 1 Hook | 2 | 3 |
| 2 Payoff timing | 2 | 3 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 3 | 3 |
| 6 Difference | 2 | 3 |
| 7 Repeat test | 2 | 3 |
| 8 Teaching | 3 | 3 |
| Total | 20/24 | 24/24 |

## Grafts applied to the winner
1. "A swarm re-sends its conversation with every turn." (A, pricing scene) into B's pricing scene: B states the meter but never the mechanism that makes it spin; no new number, no rewrite of surrounding beats.
2. "A stop word or message cap, the termination condition, ends the run." (A, broadcast scene) appended to B's selector scene: B's own notes admitted dropping the termination step the brief's process requires.

Post-graft board: 117 s target, 340 words, validator 0/0, eval gate1_ready true, variety ok.
