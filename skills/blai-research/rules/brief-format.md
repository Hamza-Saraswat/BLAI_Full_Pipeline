# Brief Format

The brief is written twice. `<slug>-brief.md` is for the human reviewer and the Obsidian archive; `<slug>-brief.json` is for machines and must conform to `shared/schemas/research.schema.json`. Same facts, same URLs, same order. No em dashes in either; wikilinks only in the markdown.

## Markdown layout

Use these headings, in this order, all of them (write "none" under a heading with nothing to say). The frontmatter is the ICM metadata header.

```markdown
---
slug: 2026-08-25-deepseek-v4-flash-128gb
stage: 03-research
topic: "Can DeepSeek V4 Flash run on 128 GB?"
depth: standard
generated_at: 2026-08-25T12:40:00Z
sources: 9
hub: "[[videos/2026-08-25-deepseek-v4-flash-128gb]]"
---

# Research brief: Can DeepSeek V4 Flash run on 128 GB?

## Summary
Three to five lines for the reviewer, carrying five DISTINCT elements: the thesis, the most
arresting number, the strongest concrete case, what could not be verified, any conflict between
sources. The Summary is not a restatement of `## Thesis` -- in the 2026-08-23 dry run every
brief's Summary was byte-identical to its Thesis, which collapsed the five things two blind
writers had to diverge on into one sentence, and both writers then wrote the same hook
(findings 12 and 29). If your Summary and Thesis read the same, the Summary is not done.

## Thesis
One sentence: the single idea the video lands.

## Explanation path

Write it as content, never as positions. "Establish that one job has two halves, reading and writing, before either machine appears" is right. "Stage one, reading. Stage two, writing." is wrong: positional vocabulary in the brief becomes positional vocabulary in the narration, which is banned by Hard Constraint 10 in `brand-vault/voice-rules.md`. Name the thing, not its number.
Prose. The route from zero to the payoff: what must be understood before what, and why that order. A proposal the script may restructure.

## Claims
1. **The claim in one sentence, number verbatim with unit.**
   - Source: Page title, https://example.com/page
   - Tier: primary | Confidence: high | Accessed: 2026-08-25 | Via: firecrawl_scrape
   - Quote: "the sentence on the page that carries the number" (required when the claim carries a number)
2. ...

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total parameters (all experts in memory) | 30.5B | https://... | "..." |

## Analogy candidates
- **Vehicle**: mapping back to the real thing. Breaks when: ...

## Misconceptions
- Myth: ... Reality: ... (claim 3)

## Glossary
- **term**: one-sentence definition.

## Unverified
- One plain sentence per item.

## Suggested outline
1. One beat per line, strongest concrete fact early.
2. ...

## Viewer situation
One sentence: what the viewer already has or does today, in their words. Second person.

## Has process
`true` or `false`. When true, list the real steps the viewer performs, one per line, each starting with a verb. When false, write "false" and nothing else. Never list rhetorical moves, components or layers as steps.

## Objection
One sentence: what a skeptical engineer says back to the thesis.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|

## Notes
Open questions, conflicting sources, thin spots. Omit the heading when empty.
```

## How the markdown mirrors the JSON

| Markdown heading | JSON key | Shape |
|------------------|----------|-------|
| frontmatter `slug`, `topic`, `depth`, `generated_at` | `slug`, `topic`, `depth`, `generated_at` | strings; `depth` is `standard` or `deep` |
| Summary | (none) | human only; no facts that are not below |
| Thesis | `thesis` | one string, 20-400 chars |
| Explanation path | `explanation_path` | one string, 40 chars or more |
| Claims | `claims[]` | `{claim, source_url, source_title, source_quality, confidence, accessed}`; the quote stays in the markdown, the number stays verbatim in `claim` |
| Key numbers | `key_numbers[]` | `{label, value, source_url}`; `value` verbatim with unit |
| Analogy candidates | `analogy_candidates[]` | `{vehicle, mapping, limit}` |
| Misconceptions | `misconceptions[]` | `{myth, reality}` |
| Glossary | `glossary[]` | `{term, definition}` |
| Unverified | `unverified[]` | strings |
| Suggested outline | `suggested_outline` | the numbered lines joined with newlines, numbers stripped |
| Sources | (none) | every `source_url` in the JSON appears here; the table may hold fetched pages no claim cites |
| Notes | `notes` | optional string |

- Claim numbering in the markdown is the order of `claims[]` in the JSON, so "claim 3" under Misconceptions points at `claims[2]`.
- The JSON has `additionalProperties: false` at every level: no extra keys (no `quote`, no `via`, no `sources`). Those live in the markdown only.
- Slugs match `^[a-z0-9][a-z0-9-]{2,40}$` (41 characters at most), so the topic part of `YYYY-MM-DD-topic` stays at 30 characters or fewer.
- Write the JSON with two-space indentation and UTF-8; keep quotes as plain `"` inside strings (escape them), and never wrap a URL in a wikilink or angle brackets.

## Size by depth

| Depth | Sources fetched | Claims | Key numbers | Subagents |
|-------|-----------------|--------|-------------|-----------|
| `standard` (Shorts) | 8-12 | 5-10 | 3-8 | 2-3 |

A brief above the band is not better; it is a writer reading more than the video can spend.
