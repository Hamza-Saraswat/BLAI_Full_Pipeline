---
slug: 2026-11-16-byob-a-local-first-desktop-ai
format: classic
structure: myth-bust
style_pack: terminal
value_types: TEACHES,EQUIPS
promise: After the Short you can install byob, point it at the local server you already run, and know why it ships no model.
target_duration_s: 43
brief: 2026-11-16-byob-a-local-first-desktop-ai-brief.md
drafts: 2026-11-16-byob-a-local-first-desktop-ai-drafts.md
---

# byob: the desktop agent with no brain

## Decisions
- Structures tried: how-to-three-moves (draft A, fits has_process and the hub's how-to pillar) vs myth-bust (draft B, the brief's strongest misconception). B won 20 to 15: its hook carried product plus tension, its navigation was cleaner, and A's how-to/tonight shape echoed the 2026-11-11 ledger entry (judge capped A's navigation and difference rows for that fingerprint).
- Hook: candidate 2 of 10 ("byob: bring your own brain. The desktop agent ships without one."), named-contradiction pattern, rotating off the last two shipped patterns (number-shock 11-14, situation 11-15).
- Graft from A: "then press Test connection" appended to scene s4; B's install beat never confirmed the connection works. No other grafts.
- Machine gates on the final board: validator 0 blockers (5 advisories: hashtag count, missing YouTube tags, s2 API lexicon note, hook-scene length, FK 6.4), eval 9/9 gates passed (entity gates passed too), sameness clean, normalizer scenes_changed 2.

## Hook candidates
1. Three moves tonight, and your Ollama model builds a spreadsheet. (used by draft A)
2. *byob: bring your own brain. The desktop agent ships without one. (used by the winner)
3. Your Ollama server finally gets hands. Thirteen megabytes of hands.
4. The desktop AI agent that refuses to ship a model.
5. A local AI agent that starts by finding your server.
6. Sixty megabytes, no Electron, no account. Bring your own brain.
7. Point a desktop agent at localhost. It already speaks your server's language.
8. Your local model can't touch your files. byob changes that tonight.
9. No Electron, no bundled model, no account. Just hands for your local model.
10. One week old, ten releases, zero bundled models.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | byob: bring your own brain. The desktop agent ships without one. Your Ollama stays the brain. | byob. No brain. 13 MB. | Terminal window, frame 1: typed prompt "byob --help" frozen mid-cursor; the wordmark "byob" and the tag "no brain on board" already composed. On "ships without one" the 13 MB size chip pops (scale-in). Motion onset at 0.30 s: cursor blink resumes. | hyperframes | centered-stack | 5.5 |
| s02 | explain | You'd expect it to run the model. It never does. Thirteen megabytes of program: one client for any OpenAI-compatible endpoint, a server that speaks OpenAI's API shape. Yours is already listening. | one client, any compatible server | Split: left the 13 MB byob binary as a small terminal slab; right a port list "11434 Ollama / 8080 llama-server / 1234 LM Studio" typing in. On "Yours is already listening" the 11434 line highlights amber. | hyperframes | split-compare | 11.0 |
| s03 | explain | Once connected, it reads files, runs code, builds spreadsheets beside your chat. Its predecessor hob bundled llama.cpp, the whole engine. byob drops even Electron, the bundled browser most agents ship. | files, code, spreadsheets. hob bundled the model. | Timeline: three tick marks (files, code, spreadsheet) draw left to right on "reads files, runs code, builds spreadsheets"; on "hob bundled llama.cpp" a GGUF weight block attaches under an older "hob" node; on "drops even Electron" the block detaches and fades. | hyperframes | timeline | 10.7 |
| s04 | explain | Tonight: cargo install byob, or unpack the release: about sixty megabytes of download. Launch it with one flag at your server, then press Test connection. | cargo install byob · 60 MB download | Diagram flow: command line "cargo install byob" types; a download bar fills to "60 MB"; then the flag "--inference-url http://localhost:11434/v1" types and a "Test connection ✓" button press lands with a hard cut to a green tick. | hyperframes | diagram-flow | 8.6 |
| s05 | payoff_close | A week old, solo-built, seven stars, an empty issue tracker. No bundled brain, no bundled browser: your model grows hands tonight. | 7 stars · 0 issues · unsigned macOS builds | Centered: the honesty stat line (7 stars, 0 issues, unsigned) stacks as terminal chrome; on "grows hands tonight" the wordmark settles and a small hand glyph closes over the byob terminal window. Wordmark settle on the final beat. | hyperframes | centered-stack | 7.6 |

## Notes for review
- The "13 MB" and "about sixty megabytes" are download sizes, never RAM; no memory number exists in any fetched source (brief, Unverified).
- "Seven stars, an empty issue tracker" are fetch-time facts (2026-11-16); the Show HN thread sat at 4 points with no comments at fetch, so no broader traction is implied.
- "hob bundled llama.cpp" and "byob drops Electron" are the brief's claims 5 and 2; the Servo-renderer nuance (HTML artifacts still render via a bundled Servo process) is deliberately simplified to "drops even Electron" per the brief's own framing, not contradicted.
- est_duration_s uses wps 2.9, the provisional ElevenLabs-clone rate; re-time after the first render.
