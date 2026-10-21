---
slug: 2026-10-21-same-mcp-server-different-answ
stage: 03-research
topic: "Same MCP server, different answers: what the Harness measured"
depth: standard
generated_at: 2026-10-21T11:38:36Z
sources: 8
hub: "[[videos/2026-10-21-same-mcp-server-different-answ]]"
---

# Research brief: Same MCP server, different answers: what the Harness measured

## Summary
The thesis: one MCP server, two harnesses, two different answers, so the measured compatibility table is the working spec. The most arresting number is the head-to-head: Claude Code CLI at MCP client version 2.1.296 passed the double-payload probe while Grok CLI at MCP client version 1.0.60 failed it with duplicated output, the same fail across 3 observed versions. The strongest concrete case is Grok Bot (MCP client version 0.1.0) and Cursor Agent CLI getting no output at all from the structured-only probe. What could not be verified: token overhead and any accuracy impact of duplication, because the site states exact token overhead was not measured. One tension to carry: the Hacker News framing calls the implementations inconsistent, while the site itself cautions that its pass/fail rubric is a preference, not a claim about what the MCP standard mandates.

## Thesis
The same MCP server hands different harnesses different answers, so the measured compatibility table, not the protocol document, is the spec your agent actually implements.

## Explanation path
MCP promised one protocol so any client could call any server, but a tool result arrives in two shapes, a text field and a structuredContent field, and the specification only says servers SHOULD mirror one into the other. That SHOULD is the crack the harnesses fall through: each agent app decides for itself whether the model sees the text, the structured object, both, or nothing. Grasp the double payload before the verdicts, because every result in the field guide comes from planting distinct random markers in the two fields and asking the agent what it can see. With the mechanism clear, the measured table lands as evidence rather than trivia: identical probes, named clients, pinned versions, different outcomes. The protocol-version split deepens the point, since the same server negotiated 2025-06-18 with Codex CLI and 2026-07-28 with Claude Code CLI, and the 2026 revision changed the connection handshake itself. The payoff for someone wiring tools locally: treat the compatibility table the way web developers once treated browser tables, as the working spec, and probe your own harness before you trust it.

## Claims
1. **What the Harness? went up as a Show HN post by Polytomic on 2026-10-20, framed around LLM agents (Claude, Codex, Grok, Amp, etc) being inconsistent in their MCP implementations, with tables inspired by the browser-compatibility tables of yore.**
   - Source: Show HN: What the Harness? LLM agent inconsistencies in MCP implementation | Hacker News, https://news.ycombinator.com/item?id=50170765
   - Tier: community | Confidence: medium | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "We made tables inspired by the browser-compatibility tables of yore that list the differences."
2. **The guide publishes the latest approved run per harness with the MCP client and version named, and its authors state that preferring one structured payload is a preference, not a claim about what the MCP standard mandates.**
   - Source: What the Harness? · MCP compatibility field guide by Polytomic, https://what-the-harness.polytomic.com
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "This preference is not a claim about what the MCP standard mandates."
3. **On the double-payload probe, where one tool result carries both a text field and a structuredContent field, Claude Code CLI (MCP client version 2.1.296, run Oct 13, 2026) earned Pass: uses structured output, while Grok CLI (MCP client version 1.0.60, run Oct 19, 2026) earned Fail: Duplicate output, the same fail across 3 observed versions.**
   - Source: What the Harness? · MCP compatibility field guide by Polytomic, https://what-the-harness.polytomic.com
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "Grok CLILatest observed · MCP client version 1.0.60Run: Oct 19, 20263 versionsSame results across 3 observations | **Fail** Duplicate output"
4. **When the probe returned structuredContent only, Grok Bot (MCP client version 0.1.0) and Cursor Agent CLI recorded Fail: No output, so the structured payload never surfaced to the agent.**
   - Source: What the Harness? · MCP compatibility field guide by Polytomic, https://what-the-harness.polytomic.com
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "Grok BotLatest observed · MCP client version 0.1.0Run: Oct 19, 2026MCP client: connectors-manager | **Warn** Falls back to text | **Pass** | **Fail** No output"
5. **Connected to the same server, Claude Code CLI and Grok CLI negotiated protocol 2026-07-28 while Codex CLI (MCP client version 0.162.1) and Amp CLI negotiated 2025-06-18, and Cursor Desktop and Grok Bot negotiated 2025-11-25.**
   - Source: What the Harness? · MCP compatibility field guide by Polytomic, https://what-the-harness.polytomic.com
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "Codex CLILatest observed · MCP client version 0.162.1Run: Oct 19, 20262 versionsSame results across 2 observations | **Older protocol** 2025-06-18"
6. **The MCP specification for 2025-06-18 says that for backwards compatibility a tool that returns structured content SHOULD also return the serialized JSON in a TextContent block, a SHOULD that leaves each harness free to pass one or both shapes to the model.**
   - Source: Tools - Model Context Protocol (2025-06-18), https://modelcontextprotocol.io/specification/2025-06-18/server/tools
   - Tier: primary | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "For backwards compatibility, a tool that returns structured content SHOULD also return the serialized JSON in a TextContent block."
7. **Version negotiation is built into MCP: if the server supports the requested protocol version it MUST respond with the same version, otherwise it MUST respond with another protocol version it supports, which is how one server ends up speaking three different versions to different clients.**
   - Source: Lifecycle - Model Context Protocol (2025-06-18), https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle
   - Tier: primary | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "If the server supports the requested protocol version, it **MUST** respond with the same version. Otherwise, the server **MUST** respond with another protocol version it supports."
8. **The 2026-07-28 revision made MCP stateless by removing the initialize/notifications/initialized handshake, removed ping, and added a server/discover RPC, so the protocol a harness implements is a moving target.**
   - Source: Key Changes - Model Context Protocol (2026-07-28), https://modelcontextprotocol.io/specification/2026-07-28/changelog
   - Tier: primary | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake."
9. **MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers and introduced as a new standard for connecting AI assistants to the systems where data lives.**
   - Source: Introducing the Model Context Protocol \ Anthropic, https://www.anthropic.com/news/model-context-protocol
   - Tier: primary | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
   - Quote: "MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers."
10. **The probes plant independent random markers in content[0].text and structuredContent so an agent cannot infer an unseen marker from the other field, and the site states that exact token overhead was not measured.**
    - Source: Run the probe · What the harness?, https://what-the-harness.polytomic.com/submission-guide.html
    - Tier: benchmark | Confidence: high | Accessed: 2026-10-21 | Via: web_extract
    - Quote: "An agent cannot infer an unseen marker from the other field. ... Exact token overhead was not measured."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Claude Code CLI MCP client version, latest observed, Pass on double payload | 2.1.296 | https://what-the-harness.polytomic.com | "Claude Code CLILatest observed · MCP client version 2.1.296Run: Oct 13, 2026" |
| 2 | Grok CLI MCP client version, latest observed, Fail: Duplicate output, same across 3 observed versions | 1.0.60 | https://what-the-harness.polytomic.com | "MCP client version 1.0.60Run: Oct 19, 20263 versionsSame results across 3 observations" |
| 3 | Grok Bot MCP client version, Fail: No output on the structured-only probe | 0.1.0 | https://what-the-harness.polytomic.com | "Grok BotLatest observed · MCP client version 0.1.0Run: Oct 19, 2026" |
| 4 | Newest MCP protocol revision the probe server tests | 2026-07-28 | https://modelcontextprotocol.io/specification/2026-07-28/changelog | "changes made to the Model Context Protocol (MCP) specification since the previous revision, 2025-11-25" |
| 5 | Protocol version negotiated by Codex CLI 0.162.1 and Amp CLI | 2025-06-18 | https://what-the-harness.polytomic.com | "**Older protocol** 2025-06-18" |
| 6 | Tests in the What the Harness suite | all four tests | https://what-the-harness.polytomic.com/submission-guide.html | "The prompt runs all four tests" |

## Analogy candidates
- **Browser compatibility tables of the old web**: the same web page rendered differently in each browser, so developers learned to test against measured compatibility grids instead of the W3C spec; the same MCP server now answers differently per harness, so you test against this grid. Breaks when: browser quirks were mostly bugs against a fixed spec, while here the MCP spec itself only says SHOULD for mirroring structured output into text, so some of the measured divergence is legal behavior rather than a defect.

## Misconceptions
- Myth: MCP is a standard, so plugging the same server into any agent gives the model the same tool output. Reality: the spec only says servers SHOULD mirror structured JSON into text, and measured runs show Claude Code CLI passing where Grok CLI duplicates and Grok Bot and Cursor Agent CLI drop the structured payload entirely (claims 3 and 4).
- Myth: everyone speaks current MCP, so protocol version is a detail. Reality: against one server on runs dated Oct 5 to Oct 19, 2026, Claude Code CLI and Grok CLI negotiated 2026-07-28 while Codex CLI and Amp CLI sat on 2025-06-18 and Cursor and Grok Bot on 2025-11-25 (claims 5 and 8).

## Glossary
- **MCP (Model Context Protocol)**: an open protocol that lets an AI application call tools and read data exposed by a server over one standard connection.
- **harness**: the agent application that hosts the model and connects to MCP servers on its behalf, such as Claude Code, Codex CLI, or Grok CLI.
- **structuredContent**: the JSON object field of a tool result, meant to carry machine-readable data.
- **TextContent**: the text portion of a tool result; the spec says servers SHOULD also mirror structured JSON here for backwards compatibility.
- **double payload**: a tool result that ships the same data in both the text and structured fields, risking the model seeing it twice.
- **protocol version**: the dated revision of MCP a connection agrees to use, such as 2025-06-18 or 2026-07-28.
- **version negotiation**: the rule that the server must answer with the client's requested protocol version if it supports it, otherwise another version it supports.
- **compatibility table**: a grid of clients versus features showing what actually works where, in the tradition of the old browser-support tables.

## Unverified
- How many tokens the duplicate payloads actually waste is unknown; the site's authors state exact token overhead was not measured.
- Whether duplicated or dropped tool output measurably degrades agent accuracy on real tasks was not tested by anyone fetched this run.
- Why Grok CLI still duplicates output across 3 observed versions while on the newest protocol has no stated cause; the site says a missing marker alone does not establish the cause.
- How the Grok, OpenAI, and Cursor clients behave on versions newer than the latest observed runs (Oct 19, 2026) is unknown from these pages.

## Suggested outline
1. Cold open on the head-to-head: one server, one probe, Claude Code CLI at MCP client version 2.1.296 passes with structured output while Grok CLI at MCP client version 1.0.60 fails by duplicating the payload, the same fail across 3 observed versions.
2. The why: a tool result has two shapes and the spec only says SHOULD for mirroring one into the other, and the same server negotiates three different protocol versions to different clients, so the harness, not the server, decides what the model sees.
3. The payoff: the compatibility table is the working spec; carry the site's own hedge that its rubric is a preference rather than a mandate, then point your own harness at the public probe endpoint and see what your stack actually passes through.

## Viewer situation
You run the same MCP server inside two different agents on your own machine and assume both harnesses show the model the same tool output.

## Has process
`true`. The steps the viewer performs, from the site's connection and submission guide:
- Add https://what-the-harness.polytomic.com/mcp as a Streamable HTTP MCP server in your agent's MCP settings.
- Give your agent the site's test prompt so it begins a run and calls the three output probes.
- Read the two test resources through MCP, not a browser, and record the exact markers you can see.
- Submit the report with the markers, keep your run token private, and wait for review; the table then shows your harness's latest approved run.

## Objection
One probe server with reviewed community submissions is not a standards conformance suite, and each verdict describes a single recorded client version and session rather than the whole harness.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://what-the-harness.polytomic.com | What the Harness? · MCP compatibility field guide by Polytomic | benchmark | web_extract | 2026-10-21 |
| 2 | https://what-the-harness.polytomic.com/submission-guide.html | Run the probe · What the harness? | benchmark | web_extract | 2026-10-21 |
| 3 | https://news.ycombinator.com/item?id=50170765 | Show HN: What the Harness? LLM agent inconsistencies in MCP implementation | Hacker News | community | web_extract | 2026-10-21 |
| 4 | https://modelcontextprotocol.io/specification/2025-06-18/server/tools | Tools - Model Context Protocol (2025-06-18) | primary | web_extract | 2026-10-21 |
| 5 | https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle | Lifecycle - Model Context Protocol (2025-06-18) | primary | web_extract | 2026-10-21 |
| 6 | https://modelcontextprotocol.io/specification/latest/server/tools | Tools - Model Context Protocol (2026-07-28) | primary | web_extract | 2026-10-21 |
| 7 | https://modelcontextprotocol.io/specification/2026-07-28/changelog | Key Changes - Model Context Protocol (2026-07-28) | primary | web_extract | 2026-10-21 |
| 8 | https://www.anthropic.com/news/model-context-protocol | Introducing the Model Context Protocol \ Anthropic | primary | web_extract | 2026-10-21 |

## Notes
The run-history page (history.html) renders its data with client-side JavaScript and returned an empty shell when fetched, so per-run evidence pages were not individually readable; every verdict above comes from the main results tables. Do not blur the Grok entries: Grok CLI duplicates output while on the newest protocol (2026-07-28), whereas Grok Bot drops structured-only output while on 2025-11-25; they are different MCP clients (grok-shell-what-the-harness versus connectors-manager). The Hacker News post had 1 point and 0 comments at fetch time, so community reaction is not a load-bearing element.
