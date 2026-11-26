---
slug: 2026-11-26-claude-code-with-a-free-local
stage: 04-script
generated_at: 2026-11-26T13:50:00Z
brief: 2026-11-26-claude-code-with-a-free-local-brief.md
winner: B (news-react-so-what)
---

# Drafts and judgment: Claude Code on a free local LLM

Both drafts passed every machine gate before the judge ran (validator blockers 0, eval failures empty, sameness clean against the ledger's last five).

## Draft A (worked-example, Price hook)

Narration (130 words, 5 scenes + payoff):

"Twenty dollars a month, or three lines tonight. You use Claude Code Pro, and a gaming PC sits right there. Claude Code is a courier packing the same Anthropic boxes. Nothing else changes. The base address, where its requests go, is the drop-off. Ollama, a model server on your machine, signs for them. Step one: pull qwen three coder, the thirty-b tag, nineteen gigabytes on disk. Step two: set the context, the code the model sees at once. The default, four thousand tokens, can fail the first request. Agent work wants sixty-four thousand tokens. Step three: three lines point Claude Code at your garage. It's Ollama's engineering, not Anthropic's blessing. Box quality rides on shelf space, your VRAM. Same courier, same terminal, free delivery."

Scenes: s01 hook (giant-number, $20/mo meter) / s02 mechanism (diagram-flow, courier route) / s03 model pick (centered-stack, ollama pull) / s04 context trap (split-compare, 4k vs 64000) / s05 three lines (centered-stack) / s06 payoff_close (giant-number, $0).

## Draft B (news-react-so-what, named-contradiction hook) -- WINNER

Narration (130 words, 7 scenes), after one graft:

"Claude Code runs without Anthropic's cloud. In January, Ollama began answering the Anthropic Messages API, Claude Code's request format. Your twenty-dollar Pro agent now runs on your gaming PC. Claude Code is a courier packing Anthropic-format boxes. The base address, where requests go, is only the drop-off. Ollama, your garage, signed by copying Anthropic's protocol, so box quality rides on shelf space, your card's memory. The catch: it's Ollama's engineering, not Anthropic's blessing. The previous open model scored six point six percent on tool use. Ollama's default context, how much code it sees, starts at four thousand tokens. Agent work wants sixty-four thousand tokens minimum, so set that first. Tonight, run ollama launch claude with qwen three coder, then check slash status. Same terminal, same agent, zero dollars a prompt."

Scenes: s01 hook (centered-stack, version stamp) / s02 consequence (split-compare, invoice to GPU) / s03 mechanism (diagram-flow, courier) / s04 garage (centered-stack, shelf blocks) / s05 catch (split-compare, 6.6%) / s06 context trap (giant-number, 4K to 64000) / s07 payoff_close (centered-stack, launch command).

## Score table (judge: kimi-k3, rubric verbatim, ledger last 5 supplied)

| # | Row | A | B |
|---|-----|---|---|
| 1 | Hook | 3 | 2 |
| 2 | Payoff timing | 1 | 3 |
| 3 | Specificity without cramming | 3 | 3 |
| 4 | Voice | 3 | 3 |
| 5 | Navigation | 1 | 3 |
| 6 | Difference | 1 | 2 |
| 7 | The repeat test | 2 | 3 |
| 8 | Teaching | 3 | 3 |
| | **Total** | **17** | **22** |

## Winner and grafts

B wins 22 to 17. One graft, from A into B's s05: "It's Ollama's engineering, not Anthropic's blessing." replaces "Anthropic doesn't support this", keeping B's "The catch:" lead -- same unsupported-status fact delivered in the wry register B's voice row already earns, no numbers added, person and the catch beat intact. The graft was applied to the storyboard and all gates re-run: validator blockers 0, eval failures empty.

## What the losing shape would have needed

The worked-example needed its first concrete thing (Ollama, the base address) inside eight seconds instead of an eleven-second courier prologue, and transitions that carry content rather than a "Step one, two, three" scaffold that costs nothing when deleted and echoes yesterday's three-move shape. With a price hook on a worked-example three days after that exact pairing shipped, it also needed a payoff line a viewer can repeat without the metaphor attached: "free delivery" only makes sense inside its own analogy, while "zero dollars a prompt" stands alone.
