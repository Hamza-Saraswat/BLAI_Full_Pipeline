---
slug: 2026-11-26-claude-code-with-a-free-local
format: classic
structure: news-react-so-what
style_pack: terminal
value_types: TEACHES,EQUIPS
promise: after this Short you can point Claude Code at a free local Ollama model with three lines and run your first prompt tonight
target_duration_s: 38
brief: 2026-11-26-claude-code-with-a-free-local-brief.md
drafts: 2026-11-26-claude-code-with-a-free-local-drafts.md
---

# Claude Code on a free local LLM: the Ollama setup

## Decisions
- Two structures tried: draft A worked-example (three legal step labels, Price hook "Twenty dollars a month, or three lines tonight."), draft B news-react-so-what (named-contradiction hook "Claude Code runs without Anthropic's cloud."). B won 22 to 17 on the eight-row rubric: its concrete fact lands at the first sentence, its navigation carries content instead of a step scaffold, and its payoff line "zero dollars a prompt" stands alone without the metaphor.
- Hook: candidate 2 of 10, the named contradiction, the pattern the judge's row 1 scored 3; the Price hook (candidate 1) went to draft A and died with it.
- Graft taken from draft A: "It's Ollama's engineering, not Anthropic's blessing." replaced B's "Anthropic doesn't support this" in s05, same unsupported-status fact in the wry register, no numbers moved.

## Hook candidates
1. Twenty dollars a month, or three lines tonight. (draft A)
2. Claude Code runs without Anthropic's cloud. * (winner, draft B)
3. Your terminal agent doesn't need Anthropic's servers.
4. Three lines turn Claude Code local tonight.
5. Four thousand tokens will break your local Claude Code.
6. Claude Code on your GPU, zero dollars a prompt.
7. You pay Pro rates. Your GPU idles.
8. Ollama speaks Anthropic's language since January.
9. Sixteen gigabytes runs a Claude Code model tonight.
10. Same agent, same terminal, zero dollars a prompt.

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Claude Code runs without Anthropic's cloud. In January, Ollama began answering the Anthropic Messages API, Claude Code's request format. | CLAUDE CODE RUNS WITHOUT ANTHROPIC'S CLOUD | Frame 1 opens on a finished terminal composition: the hook line typed in amber top-center, cursor blinking, motion onset at 0.4 s; beneath it a version line stamps OLLAMA v0.14.0, JAN 16 2026 on 'In January', and the terminal prompt retypes itself on the final beat. Hard cuts only, no fades on text. | hyperframes | centered-stack | 7 |
| s02 | explain | Your twenty-dollar Pro agent now runs on your gaming PC. | PRO $20/MO TO YOUR GPU | Split screen hard-cuts in: left pane a cloud invoice receipt scrolling its line items, right pane the same claude prompt running against a localhost banner; the left pane's receipt tears away on 'gaming PC' leaving the local pane full-frame. | hyperframes | split-compare | 3 |
| s03 | explain | Claude Code is a courier packing Anthropic-format boxes. The base address, where requests go, is only the drop-off. | BASE_URL = THE DROP-OFF ONLY | A courier route diagram draws left to right: a terminal icon packs identical amber boxes on 'packing Anthropic-format boxes', and on 'only the drop-off' the route's destination label rewrites itself from a cloud icon to a garage icon while the boxes stay untouched. | hyperframes | diagram-flow | 6 |
| s04 | explain | Ollama, your garage, signed by copying Anthropic's protocol, so box quality rides on shelf space, your card's memory. | SHELF SPACE = YOUR CARD'S MEMORY | A centered garage-shelf outline fills with amber model-weight blocks on 'signed by copying Anthropic's protocol'; on 'shelf space' the blocks resize against a GPU silhouette drawn beside the shelf, and the shelf label rewrites VRAM on the final beat. | hyperframes | centered-stack | 6 |
| s05 | explain | The catch: it's Ollama's engineering, not Anthropic's blessing. The previous open model scored six point six percent on tool use. | tau2-bench tool use: 6.6% | Split screen: left pane a grayed Anthropic docs note stamped UNSUPPORTED on "doesn't support this"; right pane a terminal emitting malformed tool JSON that loops and retries on 'six point six percent', with the score stamped large in amber. | hyperframes | split-compare | 6 |
| s06 | explain | Ollama's default context, how much code it sees, starts at four thousand tokens. Agent work wants sixty-four thousand tokens minimum, so set that first. | DEFAULT 4K, SET 64000 | A giant amber 4K shatters into fragments on 'four thousand tokens', the fragments reassemble into 64000 on 'sixty-four thousand tokens', and OLLAMA_CONTEXT_LENGTH=64000 types itself beneath the number on 'set that first'. | hyperframes | giant-number | 8 |
| s07 | payoff_close | Tonight, run ollama launch claude with qwen three coder, then check slash status. Same terminal, same agent, zero dollars a prompt. | ollama launch claude --model qwen3-coder | A centered terminal echoes frame one's composition: the launch command types itself on 'Tonight', /status prints CONNECTED TO LOCALHOST on 'slash status', a $0 badge replaces the invoice on 'zero dollars a prompt', and the wordmark settle fills the final half second so the last frame rhymes with frame one. | hyperframes | centered-stack | 7 |

## Notes for review
Numbers are verbatim from the brief ($20 monthly Pro, 6.6% tau2-bench, 4k default, 64000 minimum); "it's Ollama's engineering, not Anthropic's blessing" carries the brief's Anthropic-does-not-endorse conflict as the honest catch (the s05 visual still shows the UNSUPPORTED docs note). The analogy limit rides on "box quality rides on shelf space, your card's memory". No positional labels anywhere: navigation is by content. Value delivery: TEACHES rides on s03-s04 (the courier redirect mechanism, spoken as "the base address, where requests go, is only the drop-off"), EQUIPS rides on s06-s07 (set 64000, then the launch one-liner the viewer runs tonight).
