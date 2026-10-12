---
slug: 2026-10-12-ai-agent-swarms-on-ollama-how
format: smooth-explainer
structure: myth-bust
style_pack: terminal
value_types: TEACHES,REFRAMES
promise: After two minutes you can explain how a swarm coordinates, point any framework at the Ollama box you already run, and say what scaling it really costs.
target_duration_s: 117
brief: 2026-10-12-ai-agent-swarms-on-ollama-how-brief.md
drafts: 2026-10-12-ai-agent-swarms-on-ollama-how-drafts.md
---

# An Agent Swarm Runs on One Local Model

## Decisions
- Structures tried: worked-example (draft A, 20/24) and myth-bust (draft B, 24/24); B won by 4 on the judge rubric, taking rows 1, 2, 6 and 7 (hook tension, payoff timing, difference vs the ledger, repeat test).
- Hook: candidate 4, "A swarm isn't many models", a named-contradiction; candidate 2 was withdrawn after the variety gate flagged number-shock repeating 2026-10-10, and the swap is the reason B opens on the contradiction instead of the number.
- Grafts from A: the resend-mechanism sentence into the pricing scene and the termination-condition sentence into the selector scene, both named in the drafts note.
- Value lines: TEACHES lands on "It's a single model taking turns" (selector, handoff, shared state all shown); REFRAMES lands on "Your agents take turns. Want them at once? Then the myth has a point: parallelism costs memory."
- Gates on the final board: validator 0 blockers 0 advisories; eval gate1_ready true (entity_spend soft advisory only); variety check ok.

## Hook candidates
1. You've got Ollama running. A swarm is one line away. (situation; kept for draft A)
2. Three agents. One model. No per-token bill. (number-shock; withdrawn: pattern repeats 2026-10-10)
3. Thousands of agents, says Karpathy. You can't wire three. (named-contradiction; community-tier claim kept out)
4. * A swarm isn't many models. It's one model taking turns. (named-contradiction; PICKED for draft B, now the winner)
5. One model, many roles, zero token bills. (price; weaker tension)
6. Your Ollama box could run a swarm tonight. (tonight; overpromises a build)
7. Two dollars per million tokens, or your wall socket. (price; number needs setup)
8. Every agent in the swarm is the same model. (named-contradiction; flat, no tension)
9. Swarms aren't magic. They're group chat. (named-contradiction; no product)
10. Stop renting agents. Your GPU already is one. (contrarian; hype-adjacent)

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | A swarm isn't many models. It's a single model taking turns. You already run that model in Ollama, and a swarm sounds like a pile of extra machines. | A swarm isn't many models. | Frame 1: hook text "A swarm isn't many models." fully legible, amber accent, centered above the caption band. Motion onset within 0.5 s: at 0.35 s three agent chips scale in and merge into one model card on 'one model taking turns'; two spare card outlines fade out on 'three cards'. | hyperframes | centered-stack | 9.7 |
| s02 | explain | An agent is your Ollama chat with a name, a role, and tools. The same model answers as each agent. Every agent is that same model taking turns. | name + role + tools | On "a name, a role, and tools" a loop diagram, prompt arrow to model box to reply, fades in while three tags rise onto the single model box. On "taking turns" a dot cycles through the tags, one at a time. | manim | diagram-flow | 9.7 |
| s03 | explain | So who speaks next? AutoGen's SelectorGroupChat hands that choice to a model. It reads the shared conversation and picks the next speaker. Each reply is broadcast to the whole team. A stop word or message cap, the termination condition, ends the run. | who speaks next? | On "who speaks next" a chat thread rises message by message. On "picks the next speaker" an amber marker hops to one avatar, and on "broadcast" the new reply fades in under every name. On 'stop word' a small TERMINATE chip fades in at the thread's end. | hyperframes | timeline | 14.5 |
| s04 | explain | OpenAI's Agents SDK does it with a tool call. A handoff, one agent passing the task, is a tool called transfer to refund agent. LangGraph instead shares one state, a common board every agent reads and writes. | handoff = a tool call | On "transfer to refund agent" a tool-call chip scales in on the left panel. On "common board" the right panel fades in, one board filling as two agent icons write to it; the second label rises only after the first settles. | hyperframes | split-compare | 12.8 |
| s05 | explain | Every framework points at a base U R L, the address for model requests. Set it to localhost, port eleven thousand four hundred thirty-four. One line re-points the swarm to your Ollama server. The client demands an A P I key; Ollama ignores it. | base_url = localhost:11434 | On "base U R L" a config card fades in showing the base_url line, then the localhost address scales in as the port is spoken. On "ignores it" the API key field fades to grey. | hyperframes | centered-stack | 15.2 |
| s06 | explain | The deeper change is the bill. G P T six point one Sol charges two dollars per million input tokens, chunks of text. A swarm re-sends its conversation with every turn. Every message between agents pays that meter. | GPT-6.1 Sol | $2.00 / 1M input tokens | On "two dollars" a giant price scales in with the model caption beneath. On "pays that meter" a small meter ticks up beside each message in the thread. On 're-sends its conversation' the transcript loop visibly grows one pass longer. | hyperframes | giant-number | 13.1 |
| s07 | explain | Your box never meters a token. NVIDIA's D G X Spark, built for this workload, ships with a two hundred forty watt power supply. Cloud charges per plate. Your box is a buffet, stove already on. | 240 W power supply | On "power supply" the frame splits: an invoice card fades out left while a wall plug and the wattage rise in right. On "stove already on" a stove icon glows amber. | hyperframes | split-compare | 12.4 |
| s08 | explain | The buffet has a single stove, though. Ollama serves a single request at a time by default, and extra parallel slots cost memory. Your agents take turns. Want them at once? Then the myth has a point: parallelism costs memory. | more parallel = more RAM | On "one request at a time" three agent chips queue at a single stove slot. On "parallelism costs memory" a memory bar rises and the equation fades in above it. | manim | diagram-flow | 13.8 |
| s09 | explain | The honest catch: MAST, the largest published audit of multi-agent failures. It annotated traces of real swarm runs across the popular frameworks. | MAST: why swarms fail | On "sixteen hundred traces" rows of trace cards rise in fast, staggered, filling a grid under the heading. | hyperframes | grid | 7.6 |
| s10 | payoff_close | It sorted them into fourteen failure modes, mostly coordination, not weak models. So a local swarm buys you unlimited cheap tokens, not unlimited good ones. | 14 failure modes | On "fourteen failure modes" the digits scale in over the dimmed grid. On "cheap tokens" the text cross-fades to the closing line, rhyming frame 1, then the wordmark settles for the final half second. | hyperframes | centered-stack | 8.6 |

## Notes for review
- The three on-screen numbers are $2.00 / 1M input tokens, 240 W and 14 failure modes; the 1600+ trace count was cut to respect the smooth-explainer cap after the first eval failed number_spend.
- The analogy is the buffet with one stove; its limit lands at the top of the memory scene ("The buffet has a single stove, though").
- No local cents-per-token figure is claimed anywhere; the brief lists it Unverified. The Karpathy "thousands of agents" line stays out entirely (community tier).
- Hook candidate 4's spoken form differs from its candidate line because the variety swap happened after drafting; the frame-1 text is "A swarm isn't many models."
- Numbers in narration follow the brief verbatim: "two dollars per million input tokens", "two hundred forty watt power supply", "fourteen failure modes".
