---
slug: 2026-10-21-same-mcp-server-different-answ
format: smooth-explainer
structure: contrarian-take
style_pack: signal
value_types: TEACHES,REFRAMES
promise: After this, you check what your own harness shows the model before you blame the server.
target_duration_s: 104
brief: 2026-10-21-same-mcp-server-different-answ-brief.md
drafts: 2026-10-21-same-mcp-server-different-answ-drafts.md
---

# The compatibility table is the working spec

## Decisions
- Two structures tried: worked-example (A) and contrarian-take (B); B won 20 to 16. A's first concrete beat landed near second ten and its Step one/Step two labels deleted with zero loss (finding 14); B's four-way enumeration (text, data, both, nothing) teaches better without labels.
- Hook: "One probe graded every major agent on MCP." (case pattern; situation was A's). Divergence forced by assignment: two patterns, two drafts, per finding 12.
- Graft from A: the marker-mechanism sentence into s02 (see drafts note).
- Checkpoints (unattended): structures contrarian-take + worked-example confirmed (rotation clear vs myth-bust and news-react-so-what); hooks kept 2 of 10 across different patterns (situation, case).

## Hook candidates
1. One probe graded every major agent on MCP. *
2. You run one MCP server in two agents. They disagree.
3. Same server, same tool call, two different answers.
4. Claude Code passed. Grok got the answer twice.
5. Your MCP server is fine. Your harness is the variable.
6. MCP says should. Your harness hears maybe.
7. One tool result travels in two shapes. Agents disagree on which one counts.
8. The browser wars are back, and this time they are agents.
9. Grok Bot showed the model nothing. Cursor Agent CLI too.
10. The spec says SHOULD. The table says what actually happens.

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | One probe graded every major agent on MCP. Claude Code CLI passed. Grok CLI failed what you assumed was standard. | EVERY AGENT. ONE MCP PROBE. | Frame 1 composition: split verdict layout, left cell "Claude Code CLI - PASS" in neutral white, right cell "Grok CLI - FAIL" with FAIL in amber, both fully legible at frame 1 above the caption band. Motion onset at 0.35s: the amber FAIL tag scales up once. | hyperframes | split-compare | 7.0 |
| s02 | explain | The probe is What the Harness, a compatibility field guide from Polytomic. It plants random markers in each field and asks the agent what it sees. It grades the promise of MCP, the standard that connects agents to your server: same server, same behavior everywhere. | WHAT THE HARNESS · by Polytomic | Centered stack on dark. On "What the Harness" the title "WHAT THE HARNESS" rises in; on "from Polytomic" a small "by Polytomic" fades beneath; on "same behavior everywhere" a thin amber rule scales in under the stack. One text block animates at a time. | hyperframes | centered-stack | 10.5 |
| s03 | explain | Claude Code CLI earned its pass at MCP client version two point one point two nine six. The verdict reads: uses structured output. | Claude Code CLI · 2.1.296 · PASS | Giant number treatment: "Claude Code CLI" settled at top. On "two point one point two nine six" the digits 2.1.296 scale into center stage; on "uses structured output" an amber "PASS" tag fades in below. | hyperframes | giant-number | 8.0 |
| s04 | explain | Grok CLI told the model the answer twice. Duplicate output, the same fail across three observed versions. | GROK CLI · DUPLICATE OUTPUT · 3 VERSIONS | Fresh dark frame. On "the answer twice" two identical answer cards fade in, stacked with a slight offset. On "Duplicate output" an amber "DUPLICATE" tag scales in over them; on "three observed versions" a small "3 VERSIONS" fades beside it. | hyperframes | split-compare | 6.0 |
| s05 | explain | Look at the harness, the app that connects your model to MCP servers. A tool result carries the answer as text and again as structured data, machine readable JSON. | tool result → text + structuredContent | Drawn diagram, motion starts at 0.3 s: on "carries the answer as text" a sharp-cornered box labeled "tool result" draws in, then an arrow grows to a "text" field; on "again as structured data" a second arrow grows to a "structuredContent" field tinted amber. Labels appear with their arrows. | manim | diagram-flow | 10.0 |
| s06 | explain | The MCP spec says a server should mirror that JSON into text. Should is permission. So the server did nothing wrong. Your harness picks what the model sees: text, data, both, or nothing. | SHOULD: text · data · both · nothing | On "should mirror that JSON into text" the word SHOULD rises large in amber. On "Should is permission" SHOULD settles smaller at top; then four chips fade in one at a time on their spoken words: "text", "data", "both", "nothing". | hyperframes | centered-stack | 11.5 |
| s07 | explain | Sometimes the model sees nothing. On a structured only reply, Grok Bot and Cursor Agent CLI recorded no output at all. The payload never surfaced. | Grok Bot · Cursor Agent CLI · NO OUTPUT | Two-column grid: on "Grok Bot and Cursor Agent CLI" two cells rise, labeled "Grok Bot" and "Cursor Agent CLI". On "no output at all" a single amber "NO OUTPUT" badge fades in spanning both cells. | hyperframes | grid | 8.5 |
| s08 | explain | Even the protocol is a moving target. Against that same server, Codex CLI and Amp CLI negotiated an older revision. Claude Code CLI and Grok CLI got the newest, which removed the opening handshake. | OLDER: CODEX·AMP → NEWEST: CLAUDE·GROK | A horizontal line draws left to right on "negotiated an older revision"; a left node rises labeled "OLDER · CODEX · AMP". On "got the newest" a right node rises in amber: "NEWEST · CLAUDE · GROK". On "removed the opening handshake" a small link icon on the line fades out. | manim | timeline | 11.5 |
| s09 | foreshadow | Web developers lived this: browsers rendered the same page differently, so they trusted compatibility tables over the spec. The limit: browser quirks were bugs, while the MCP spec's should makes this legal. | THEN: browser bugs · NOW: legal SHOULD | On "browsers rendered the same page differently" a left panel fades in: a retro browser window captioned "THEN". On "makes this legal" a right panel rises: a spec page captioned "NOW" with one amber-highlighted line reading "SHOULD". | hyperframes | split-compare | 11.0 |
| s10 | foreshadow | What the Harness runs one probe server with reviewed community submissions. That is a field guide, and it stops short of a conformance suite. Each verdict covers one client version, one session. | FIELD GUIDE ≠ CONFORMANCE SUITE | Centered stack: on "reviewed community submissions" a card labeled "FIELD GUIDE" rises in; on "stops short of a conformance suite" a second line fades below it, "≠ CONFORMANCE SUITE" in amber. Both settle. | hyperframes | centered-stack | 11.0 |
| s11 | payoff_close | The compatibility table, not the MCP spec, is what your agent implements. So point your harness at the probe and read which markers reach your model. | THE TABLE IS THE SPEC | Composition rhymes with frame 1: two cells in the same split family, settled. On "The compatibility table" the left cell rises: "THE TABLE" in amber; on "not the MCP spec" the right cell fades in dimmed: "THE SPEC". Through the final sentence both cells hold still as a thin amber rule scales in beneath. | hyperframes | split-compare | 9.5 |

## Notes for review
- Number budget: two of three spent (client version two point one point two nine six; three observed versions). Protocol dates 2025-06-18 and 2026-07-28 were demoted to "older"/"newest" with named clients to protect the cap.
- Claim softened: the Hacker News "inconsistent implementations" framing became "the server did nothing wrong"; the site itself says its pass/fail rubric is a preference, not a standard's mandate. No token-waste claim (the site states overhead was not measured).
- Analogy limit in s09: browser quirks were bugs against a fixed spec; the MCP spec's SHOULD makes some measured divergence legal.
