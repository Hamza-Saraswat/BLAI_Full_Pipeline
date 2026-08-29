# Cloud Environment and Routines

Routines run in the claude.ai/code environment **Default** (`env_01XYTtSrThHrPHciRYUeHibm`) with this repo cloned at `main`.

## Network allowlist

Set network access to **Custom** with "include default domains" checked, and add:

| Domain | Used by |
|--------|---------|
| `api.telegram.org` | morning FYI cards from the ideas routines |
| `api.firecrawl.dev` | FireCrawl MCP and `firecrawl_search.py` |
| `www.googleapis.com` | YouTube Data API (`search.list`, `videos.list`, `videos.batchGetStats`, `channels.list`) |
| `suggestqueries.google.com` | YouTube autocomplete fan-out |
| `oauth.reddit.com`, `www.reddit.com` | Reddit API |
| `hn.algolia.com` | Hacker News search |
| `huggingface.co` | trending models |
| `api.github.com` | releases of the core runtimes (already in the default list) |

MCP connector traffic is routed through Anthropic and needs no allowlist entry.

## Connectors

| Connector | URL | Attach to |
|-----------|-----|-----------|
| vidIQ MCP (custom connector, OAuth) | `https://mcp.vidiq.com/mcp` | `blai-shorts-ideas` |

Add it once at claude.ai/customize/connectors, then attach it to the two ideas routines.

## Environment variables

The cloud block of `shared/env-template.md`.

## Routines

| Routine | Cron (UTC) | Local (CT, summer) | Model | Prompt |
|---------|-----------|--------------------|-------|--------|
| `blai-shorts-ideas` | `0 11 * * *` | 06:00 daily | claude-sonnet-5 | `cd workspaces/shorts` then `ideas --unattended` |
| `blai-shorts-produce` | `0 12 * * *` | 07:00 daily | claude-opus-5 | `cd workspaces/shorts` then `produce --unattended` |
| `blai-weekly-retro` | `0 13 * * 0` | 08:00 Sunday | claude-sonnet-5 | `cd analytics` then `retro --unattended` |

The exact prompt text lives in `build/routines/*.md` and is pushed with `build/routines/sync.md` instructions. Routines are created disabled and enabled once the environment variables exist.

## Daily cap

Check the per-account routine cap at claude.ai/code/routines. This repo needs at most 4 runs on a Mon/Wed/Fri and 2 on other days.
