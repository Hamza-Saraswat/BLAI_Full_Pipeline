#!/usr/bin/env python3
"""FireCrawl web-news source for the trend radar (past-week web search with page markdown).

    python3 firecrawl_search.py --hours 48 --limit 10 [--out FILE] [--dry-run]

Needs FIRECRAWL_API_KEY (skipped with a note when absent). POST https://api.firecrawl.dev/v1/search
with {"query", "limit", "tbs": "qdr:w", "scrapeOptions": {"formats": ["markdown"]}} per query
in rules/sources.md (block ```firecrawl-queries). Results carry no reliable date, so
published_at is null and the radar scores them at the window's midpoint.

Output: JSON list with title, url, query, description (300 chars), markdown (600 chars),
published_at (null).
"""
from __future__ import annotations

import sys
import time

import radarlib as rl

SOURCE = "firecrawl"
DEFAULT_LIMIT = 10
DEFAULT_QUERIES = ["DGX Spark", "local LLM news", "NVIDIA DGX Spark firmware update",
                   "open weights model release", "run LLM locally"]
ENDPOINT = "https://api.firecrawl.dev/v1/search"


def parse_results(query: str, data: dict) -> list[dict]:
    rows = (data or {}).get("data")
    if isinstance(rows, dict):                 # newer responses nest web results
        rows = rows.get("web") or []
    items = []
    for row in rows or []:
        url = row.get("url")
        if not url:
            continue
        items.append({
            "source": SOURCE,
            "query": query,
            "title": rl.clip(row.get("title") or url, 300),
            "url": url,
            "description": rl.clip(row.get("description"), 300),
            "markdown": rl.clip(row.get("markdown"), 600),
            "published_at": None,
        })
    return items


def collect(hours: int = 48, limit: int = DEFAULT_LIMIT, dry_run: bool = False) -> list[dict]:
    queries = rl.rule_list("firecrawl-queries", DEFAULT_QUERIES)
    seen, items = set(), []

    def take(batch):
        for item in batch:
            if item["url"] in seen:
                continue
            seen.add(item["url"])
            items.append(item)

    if dry_run:
        fixture = rl.fixture("firecrawl_search.json")
        for query in queries:
            take(parse_results(query, fixture.get(query) or {})[:limit])
        return items
    key = rl.env("FIRECRAWL_API_KEY")
    if not key:
        raise rl.Skip("FIRECRAWL_API_KEY not set")
    headers = {"Authorization": "Bearer " + key}
    failures = 0
    for index, query in enumerate(queries):
        body = {"query": query, "limit": limit, "tbs": "qdr:w", "scrapeOptions": {"formats": ["markdown"]}}
        try:
            take(parse_results(query, rl.get_json(ENDPOINT, headers=headers, data=body, timeout=60,
                                                  source=SOURCE)))
        except RuntimeError as err:
            failures += 1
            rl.log(SOURCE, "query %r failed: %s" % (query, err))
        if index < len(queries) - 1:
            time.sleep(0.5)
    if queries and failures == len(queries):
        raise RuntimeError("every query failed")
    return items


if __name__ == "__main__":
    sys.exit(rl.run_source(SOURCE, collect, __doc__, DEFAULT_LIMIT))
