# FireCrawl Usage

The FireCrawl MCP server is declared in `.mcp.json` (`npx -y firecrawl-mcp`, key from `FIRECRAWL_API_KEY`, see `shared/env-template.md`). In Claude Code its tools appear with the `mcp__firecrawl__` prefix: `firecrawl_search`, `firecrawl_scrape`, `firecrawl_map` and others. Cloud routines reach `api.firecrawl.dev` through the allowlist in `shared/cloud-environment.md`; on the Spark the same `.mcp.json` works when the key is in `build/.env`.

## Which tool for which job

| Job | Tool | How |
|-----|------|-----|
| Find candidate pages for a question | `firecrawl_search` | `query`, `limit` 5-8. Returns title, URL, snippet. Read the snippets, pick 1-3 pages. A snippet is not a fetch. Do not pass `scrapeOptions`: it scrapes every result and spends the fetch budget on pages you will not cite. |
| Read a page you intend to cite | `firecrawl_scrape` | `url`, `formats: ["markdown"]`, `onlyMainContent: true`. Use it for JS-heavy docs, blogs, model cards, GitHub releases, pricing pages, PDFs (papers). Read the passage, copy the quote verbatim. |
| Find the right page inside a docs site | `firecrawl_map` | `url` of the site root plus `search` term; returns URLs only. Then scrape one. Optional; skip when search already found the page. |
| Never in this skill | `firecrawl_crawl`, `firecrawl_extract`, batch scrape | Whole-site crawls and schema extraction spend credits on nothing a brief needs. |

## Fallbacks

- Tools absent (connector not attached, key empty, MCP failed to start): `WebSearch` for discovery, `WebFetch` for reading. Same rules apply: a fetch is a fetch, a snippet is not.
- A scrape fails (403, timeout, empty markdown): retry once with `WebFetch`. If still nothing, the page was not read: drop it from Claims and list it under NOT FOUND with the URL so the reviewer can open it by hand.
- Paywalled or login-walled: do not cite. Find the primary source the article is reporting on.
- A page that loads but does not contain the fact the snippet promised: say so under NOT FOUND; do not cite the snippet.
- Never let a missing or failing tool end the run. The brief records under Notes which tool family was used.

## Cost hygiene

- Scrape only pages you will cite. Search first, read snippets, pick, then scrape.
- Budgets per run, split across subagents by the orchestrator: `standard` at most 6 searches and 12 scrapes; `deep` at most 12 searches and 25 scrapes. A subagent that hits its budget stops and reports what it has.
- One URL, one fetch. The orchestrator assigns distinct questions so subagents do not fetch the same page; a subagent never re-fetches a page it already has.
- Prefer the canonical URL (no tracking parameters, no `?utm_`), and record the URL you actually fetched.
- Start from tier 1 pages (model card, release notes, paper) when the topic names a product; they answer most questions in one fetch.

## Record what you did

- Each claim's `accessed` date is the run date.
- The Sources table's "Fetched via" column says `firecrawl_scrape`, `WebFetch` or `firecrawl_search+scrape` per page.
- Under Notes, one line: which tool family ran, how many searches and scrapes were spent, and anything that failed.
