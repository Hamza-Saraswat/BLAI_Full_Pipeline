---
name: blai-research
description: Turn one video idea into a sourced research brief, written twice (markdown for people, JSON for machines), by fanning out parallel web-research subagents that cite only pages fetched this session, quote numbers verbatim with units, and park unsupported beliefs under Unverified. Use at the research stage of either workspace, before any script is written.
metadata:
  tags: "research, sources, citations, firecrawl, brief"
---

# blai-research

You produce the one artifact the script writer trusts as ground truth: a sourced route through the concept with real names and real numbers. Research the topic on its own merits, from scratch; a viewer arrives knowing nothing and so do you. Come back with material so specific the writer cannot help but make a concrete video.

## When to Use

- Stage 03 (research) of `workspaces/shorts` and `workspaces/long-form`, once an idea has a slug and a hub note.
- A re-research after a rejected or unsupported claim (`shared/pipeline-overview.md`, "When to loop back"): every stage after 03 then re-runs.
- Not for writing the script, choosing the structure, or measuring anything on our own hardware. Expected measurements go under Unverified; `skills/dgx-capture` replaces them with real numbers.

## What You Need Before Calling

- The hub note `workspaces/<ws>/videos/<slug>.md` (title, pillar or series, format, value_types) and the ideas line that picked it.
- Depth, named by the stage contract: `standard` (8-12 sources, Shorts) or `deep` (15-25 sources, long-form).
- The slug, today's date (ISO), and the output folder (the stage's `output/`).
- FireCrawl MCP tools (`firecrawl_search`, `firecrawl_scrape`) when the connector is attached and `FIRECRAWL_API_KEY` is set; otherwise `WebSearch` and `WebFetch`. A missing tool never fails the run (`rules/firecrawl-usage.md`).
- `shared/schemas/research.schema.json` and the three rule files below. `brand-vault/identity.md` "Audience" section for who the brief serves.

## How It Works

1. **Plan.** Restate the idea in one line. Decompose it into 3-5 research questions the video must answer: what the thing is, why it matters to someone running AI on their own hardware, the load-bearing number or numbers, the concrete case or story, the common misconception. Note what the hub note and ideas line already steer toward (a smooth explainer wants one scenario that carries the whole script; a news-react wants the dated event and its one consequence).
2. **Fan out.** Spawn one subagent per question with the Task tool (called Agent in current Claude Code), all in the same turn so they run in parallel. Give each the brief in step 3 with its own question and its share of the tool budget: standard 2-3 subagents, deep 4-5. Assign distinct questions so no two subagents fetch the same pages.
3. **Subagent brief.** Paste verbatim, fill the brackets:

   ```
   You research ONE question for a Build Local AI video brief. Question: [question].
   Topic: [topic]. Today: [date]. Budget: [n] searches, [m] page fetches.
   Tools: firecrawl_search to find pages; firecrawl_scrape (formats ["markdown"],
   onlyMainContent true) for pages you will cite. If those tools are absent use
   WebSearch then WebFetch. A search snippet is not a fetch.
   Rules: cite only pages you fetched and read in this session; quote every number
   verbatim with its unit and qualifier; prefer primary > docs > benchmark >
   community; a belief you could not ground in a fetched page goes under
   UNVERIFIED, never under FINDINGS; never invent or guess a URL.
   Return exactly these sections, one item per line, fields separated by " | ":
   FINDINGS: claim (one sentence) | verbatim quote | url | page title | tier | confidence high/medium | fetched via | accessed date
   NUMBERS: label | verbatim value with unit | url
   ANALOGY CANDIDATES: vehicle | mapping | where it breaks
   MISCONCEPTIONS: myth | reality | url
   GLOSSARY: term | one-sentence definition
   UNVERIFIED: plain sentences
   NOT FOUND: what you searched for and did not find
   ```

4. **Merge.** Dedupe by URL. Rank claims by tier, then confidence, then specificity (a named company, a dated event, a court case beats a category). When sources conflict keep both, say which you trust and why under Notes. Everything under UNVERIFIED or NOT FOUND stays out of Claims. Check every URL in Claims and Key numbers against the subagents' fetched lists; drop any that was only seen in a snippet.
5. **Synthesize.** Thesis (one sentence, the idea the video lands). Explanation path (prose: the route from zero to the payoff, what must be understood before what; a proposal, the script may restructure it). Claims (at least 3, load-bearing, specific, each with source, tier, confidence, accessed date, and the verbatim quote when the claim carries a number). Key numbers (verbatim with units; flag the most arresting one, it is probably the hook). 0-3 analogy candidates with their breaking point. Misconceptions as myth and reality pairs. Glossary of terms the video must define in one sentence. Unverified. Suggested outline: one beat per line, strongest concrete fact early.
6. **Write both files.** `<slug>-brief.md` per `rules/brief-format.md` and `<slug>-brief.json` conforming to `shared/schemas/research.schema.json`, same facts in both, `depth` set to the depth you ran. The JSON never carries a URL the markdown lacks; the markdown never carries a claim the JSON lacks.
7. **Validate.** `python3 skills/blai-research/scripts/validate_research.py <output>/<slug>-brief.json` until it exits 0. It enforces the schema (required keys, types, enums, `^https?://` on every `source_url`, at least 3 claims, no unknown keys). `--schema PATH` overrides the default `../../../shared/schemas/research.schema.json`.

   ```
   python3 skills/blai-research/scripts/validate_research.py \
     workspaces/shorts/stages/03-research/output/2026-08-25-deepseek-v4-flash-128gb-brief.json
   ```

## Rules

- `rules/citation-rules.md`: the four source tiers, what counts as fetched, the verbatim-number rule, what goes under Unverified.
- `rules/brief-format.md`: the markdown layout (Summary through Sources) and how each heading mirrors a JSON key.
- `rules/firecrawl-usage.md`: which FireCrawl tool for which job, the WebFetch fallback, and cost hygiene (scrape only pages you will cite).

## After the Call

- The brief is the deliverable. Keep the chat summary short: thesis, source count by tier, the most arresting number, the strongest analogy, any conflict or thin spot the writer should know about.
- The stage contract, not this skill, links the brief in the hub note (`## Artifacts`, "Brief"), appends the decision line, and sets `status: researched` with `tools/hubnote.py`.
- Write only the two brief files. Never touch the script, the storyboard, or any other stage's output.
- If the concept is thin or the sources are weak, say so under Notes instead of padding Unverified with filler; a thin brief is a reason to send the idea back, not to fake depth.

## Three fields the writer cannot invent

Every brief carries `viewer_situation` (what the viewer has or does today, one sentence, second person), `has_process` plus `process_steps` (true only for steps the viewer performs; a mechanism or an argument is not a process), and `objection` (what a skeptical engineer says back). The script stage uses them to open in direct address, to choose a structure, and to decide whether positional labels are permitted at all. Getting `has_process` wrong is how a script ends up numbering things that are not steps. See `rules/brief-format.md`.
