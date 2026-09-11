---
slug: 2026-09-11-ollama-coding-agent-qwen-3-8-2
format: smooth-explainer
structure: how-to-three-moves
style_pack: terminal
value_types: EQUIPS,TEACHES
promise: after about two minutes the viewer can set up a local coding agent tonight -- OpenCode as the harness, Ollama serving the Qwen twenty-seven-billion model, context capped, agent sandboxed -- and can say why the cap exists.
target_duration_s: 128
brief: 2026-09-11-ollama-coding-agent-qwen-3-8-2-brief.md
drafts: 2026-09-11-ollama-coding-agent-qwen-3-8-2-drafts.md
---

# Ollama coding agent: Qwen 3.8 27B mxfp8 on one laptop

## Decisions
- Structures tried: how-to-three-moves (draft A) and number-first (draft B); both clear the rotation rule (last two shipped: news-react-so-what 09-10, worked-example 09-09). A won 20-18; the judge credited its legal Move labels, closed count and stronger closer; B lost two points to a drifted absence-of-evidence claim (finding 17) and row 6 (number-first aired 09-06).
- Hook: #4 of 10, Tonight pattern, 7/7 -- "Three installs and your Mac runs a coding agent tonight." B drew #1 Number shock, 6/7; writers held two different patterns (finding 12 guard).
- One graft from B: "The cap is the difference between a slow agent and a locked laptop." replaces A's plain assertion in s09 (stakes contrast over assertion; no rewrite needed; no number cost). B's hook led by one point only, under the two-point graft threshold.
- Gates on the winner: validator 0 blockers / 0 advisories; eval_short all nine gates pass (number_spend 3/8 spent, cap 3 respected; hook waived-concrete for smooth band; sameness clean vs last 5); variety recorded (entry 10); style pack terminal (topic fit 3 keyword hits; previous signal).
- Value delivery: EQUIPS -- "Move one/two/three" scenes carry the real commands (ollama pull qwen3.8:27b-mxfp8, context 65536, sbx run opencode --kit). TEACHES -- s06/s07 show context as the second memory tenant and why the uncapped default locks the laptop.

## Hook candidates
1. Thirty-two gigabytes. That's the whole model, on your laptop.
2. You've tried local models. Tonight one writes your code.
3. You've got one laptop. It can be your coding agent.
4. Three installs and your Mac runs a coding agent tonight. *
5. A coding agent with no cloud, no key, no subscription.
6. Sixty-four thousand tokens. That's the cap that saves your laptop.
7. Your laptop isn't too small. The context window was uncapped.
8. Qwen 3.8 runs your agent. Ollama serves it. sbx cages it.
9. No API key. Your forty-eight-gigabyte Mac is the datacenter.
10. One developer front-paged the whole setup. Here's the stack.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Three installs and your Mac runs a coding agent tonight. A coding agent reads your files, runs commands and edits code. You've watched cloud agents, never your own project. | Three installs. Coding agent tonight. | Frame 1: title 'Three installs. Coding agent tonight.' fully legible on a dark terminal; motion onset at 0.4s as the title's caret blinks and the first prompt line rises in place. At 'reads your files' three empty prompt lines rise in place behind it, one at a time. Last frame's wordmark matches this style. | hyperframes | centered-stack | 10 |
| s02 | explain | Move one: install the three tools. Ollama, a free server that runs models behind one command. OpenCode, the open source agent that lives in your terminal. S B X, Docker's sandbox, a small virtual machine the agent is locked inside. | sbx · OpenCode · Ollama | Three cards in a left-to-right flow. At "Ollama" card one fades in with "ollama.com"; at "OpenCode" card two with "brew install anomalyco/tap/opencode"; at "S B X" card three with "brew install docker/tap/sbx". One card animates at a time. | hyperframes | diagram-flow | 14 |
| s03 | explain | This recipe comes from a walkthrough written on a MacBook Pro with forty-eight gigabytes of memory. That laptop is the whole datacenter. | 48GB MacBook Pro | Caption "MacBook Pro" fades in at "MacBook Pro"; the giant "48GB" scales up at "forty-eight gigabytes of memory". | hyperframes | giant-number | 8 |
| s04 | explain | Move two: pull the model. One command pulls the twenty-seven-billion-parameter Qwen, a coding model built for agent work, thirty-two gigabytes on disk. The download takes a while. It only happens once. | ollama pull qwen3.8:27b-mxfp8 \| 32GB | Terminal panel. The command fades in at "pull the model"; the "32GB" badge scales in at "thirty-two gigabytes on disk"; a progress bar creeps from "The download takes a while". | hyperframes | centered-stack | 11 |
| s05 | explain | The model fits because of M X F P eight, a quantization storing each weight as an eight-bit number. Each small block of weights gets its own scaling factor. You lose a little accuracy. For coding help, you will not feel it. | mxfp8 = 8-bit weights | Split view. Left: a row of long precise numbers, fades in early. Right: the same row as short 8-bit blocks, fading in at "eight-bit number". One small scale tag per block; a single tag pulses at "scaling factor". | manim | split-compare | 14 |
| s06 | explain | Memory has a second tenant: the context window, the model's working memory, measured in tokens, chunks of text. Every file the agent reads sits inside it, and it grows with every word. | context: the model's working memory \| grows with every file | Horizontal memory bar on a chat timeline. The model block sits pre-filled at 'second tenant'. At 'grows with every word' a context segment extends with each chat tick toward a ceiling line marked memory. | manim | timeline | 11 |
| s07 | explain | On a machine this size, Ollama's default context is generous. Unchecked, it eats the headroom and locks the laptop. | default: generous \| headroom: gone | Continuation of the memory bar. At 'eats the headroom' the context segment fills the remaining bar; at 'locks the laptop' it touches the ceiling line and the line pulses red once. | manim | diagram-flow | 7 |
| s08 | explain | Move three: cap the context, then cage the agent. In OpenCode's config, set the model to sixty-five thousand tokens of context. | context: 65536 | A config file card centered. The line 'context: 65536' scales gently at 'sixty-five thousand tokens of context'. One text line animating at a time. | hyperframes | centered-stack | 7 |
| s09 | explain | Also drop reasoning effort, the hidden thinking, to low. The cap is the difference between a slow agent and a locked laptop. Ollama's own docs back the number. | effort: low \| docs: at least 64000 tokens | Split card. Left: a dial glyph with its pointer resting at 'low' fades in at 'the hidden thinking'. Right: at 'Ollama's own docs' a docs chip fades in reading 'at least 64000 tokens'. | hyperframes | split-compare | 8 |
| s10 | explain | Now the cage: one folder, an S B X kit pointing the agent at your local Ollama. Run it, and OpenCode works inside its own filesystem and network. A hallucinated command dies in the sandbox, not on your machine. | sbx run opencode --kit ./sbx-kit/ | An agent box inside a walled sandbox, host machine outside. The launch command fades in at "Run it". At "hallucinated command" an arrow rises from the agent and stops at the wall on "dies in the sandbox". | hyperframes | diagram-flow | 13 |
| s11 | explain | The honest catch. It runs slower than a paid cloud model, and the community argues about Ollama itself. We have not timed this exact stack. The trade: no A P I key, and your code never leaves the laptop. | Slower than cloud. No API key. | Split view. Left: a cloud card with quick tick marks. Right: a laptop card with slower ticks. At "no A P I key" a small lock fades in over the laptop card. | hyperframes | split-compare | 13 |
| s12 | payoff_close | Then it is running. OpenCode edits your project while the Qwen thinks on your own hardware, caged and capped. Three installs, and tonight your Mac is the agent's whole datacenter. | Three installs. Coding agent tonight. | Terminal shows diff lines fading in one by one at "OpenCode edits your project". On the payoff sentence the wordmark fades in centered, same style as frame 1, and the video ends. | hyperframes | centered-stack | 10 |

## Notes for review
- The 65536 cap is rounded to "sixty-five thousand tokens" in speech; the exact 65536 sits on screen in s08. Ollama's docs number (at least 64000 tokens) is on screen in s09, not spoken as a fourth number.
- s04 speaks two numbers in adjacent sentences (twenty-seven billion parameters, then thirty-two gigabytes); judge flagged and accepted; each has its own sentence, referent and on-screen pairing.
- Speed stays attributed: "We have not timed this exact stack" per the brief's Unverified; the llama.cpp debate is omitted from the winner (it lived in B).
- Move labels are legal here: has_process true, three labels, ascending, each names an action, and the count closes on "Three installs" in the payoff.
