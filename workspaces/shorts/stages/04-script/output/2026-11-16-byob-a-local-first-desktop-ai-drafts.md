---
slug: 2026-11-16-byob-a-local-first-desktop-ai
stage: 04-script
generated_at: 2026-11-16T13:20:00Z
hub: "[[videos/2026-11-16-byob-a-local-first-desktop-ai]]"
---

# Drafts and scores: byob, a local-first desktop AI agent

Two blind writers, two structures, three separate kimi-k3 calls (writer A, writer B, judge). Neither writer saw the other's draft; the judge saw only the two boards and the ledger tail.

## Draft A -- how-to-three-moves, hook "tonight"

| Scene | Narration |
|-------|-----------|
| s01 | Three moves tonight, and your Ollama model builds a spreadsheet. Right now it only chats; it can't touch a file. |
| s02 | Step one: install byob, bring your own brain, an agent that ships no model. The download is about sixty megabytes. |
| s03 | Step two: point it at your OpenAI-compatible endpoint, a server that speaks OpenAI's HTTP shape, then press Test connection. |
| s04 | Step three: open a workspace folder, then run one real job, a spreadsheet from a CSV, approving every action card. |
| s05 | The catch: it's a week old. Seven stars, empty issue tracker, unsigned Mac builds. |
| s06 | Point byob at llama-server, and the model you already run gets hands. |

## Draft B -- myth-bust, hook "named-contradiction" (WINNER)

| Scene | Narration |
|-------|-----------|
| s01 | byob: bring your own brain. The desktop agent ships without one. Your Ollama stays the brain. |
| s02 | You'd expect it to run the model. It never does. Thirteen megabytes of program: one client for any OpenAI-compatible endpoint, a server that speaks OpenAI's API shape. Yours is already listening. |
| s03 | Once connected, it reads files, runs code, builds spreadsheets beside your chat. Its predecessor hob bundled llama.cpp, the whole engine. byob drops even Electron, the bundled browser most agents ship. |
| s04 | Tonight: cargo install byob, or unpack the release: about sixty megabytes of download. Launch it with one flag at your server, then press Test connection. |
| s05 | A week old, solo-built, seven stars, an empty issue tracker. No bundled brain, no bundled browser: your model grows hands tonight. |

(The s04 "then press Test connection" clause is the graft from A, applied after judging.)

## Score table

| Row | A | B |
|-----|---|---|
| 1 Hook | 1 | 3 |
| 2 Payoff timing | 2 | 2 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 2 | 3 |
| 5 Navigation | 1 | 2 |
| 6 Difference | 1 | 2 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 2 | 2 |
| **Total** | **15** | **20** |

## Winner and grafts
- Winner: B (myth-bust), 20 to 15.
- Graft taken from A: the clause "then press Test connection", appended to B's s04. Reason: B's install beat never confirmed the connection actually answers; A's concrete UI action is the one operational detail B said worse. Appending does not touch structure, person, or number budget.
- No hook graft: A's hook did not outscore B's by two points on row 1 (1 vs 3 goes the other way).

## What the losing shape would have needed
A needed a hook carrying a product or number inside its tension, since "Your model. New hands. Tonight." only names a topic. It also needed to escape the how-to/tonight/37-second fingerprint already sitting in the shipped ledger, which capped both its navigation and difference rows.

## Gate history (both boards, all runs)
- A: final validator 0 blockers / eval 9/9 after two fix rounds (scene_specificity, then positional_labels action-verb on "Step three").
- B: final validator 0 blockers / eval 9/9 after two fix rounds (hook_concrete + scene_specificity, then sameness hook-pattern and scene_specificity again after the hook-scene restructure).
- Judge drift check: none on either board.
