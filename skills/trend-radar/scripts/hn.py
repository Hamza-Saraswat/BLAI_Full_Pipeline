#!/usr/bin/env python3
"""Hacker News source for the trend radar (Algolia search, no key needed).

    python3 hn.py --hours 48 --limit 20 [--out FILE] [--dry-run]

One search_by_date call per query in rules/sources.md (block ```hn-queries), stories only,
created inside the window. Stories that match several queries appear once.

Output: JSON list with title, url (story link, or the HN thread for text posts), hn_url,
objectID, query, points, num_comments, created_at, published_at, summary (story text, 300 chars).
"""
from __future__ import annotations

import sys
import time
import urllib.parse

import radarlib as rl

SOURCE = "hn"
DEFAULT_LIMIT = 20
DEFAULT_QUERIES = ["local llm", "llama.cpp", "ollama", "vllm", "DGX Spark", "quantization",
                   "open weights", "Qwen", "DeepSeek", "Mistral", "Unsloth"]
ENDPOINT = "https://hn.algolia.com/api/v1/search_by_date"


def parse_hits(data: dict, query: str) -> list[dict]:
    items = []
    for hit in (data or {}).get("hits") or []:
        object_id = str(hit.get("objectID") or "")
        if not object_id or not hit.get("title"):
            continue
        hn_url = "https://news.ycombinator.com/item?id=" + object_id
        published = rl.parse_time(hit.get("created_at") or hit.get("created_at_i"))
        items.append({
            "source": SOURCE,
            "query": query,
            "objectID": object_id,
            "title": rl.clip(hit.get("title"), 300),
            "url": hit.get("url") or hn_url,
            "hn_url": hn_url,
            "points": int(hit.get("points") or 0),
            "num_comments": int(hit.get("num_comments") or 0),
            "created_at": hit.get("created_at"),
            "published_at": rl.iso(published),
            "summary": rl.clip(hit.get("story_text") or "", 300),
        })
    return items


def collect(hours: int = 48, limit: int = DEFAULT_LIMIT, dry_run: bool = False) -> list[dict]:
    now = rl.now_for(dry_run)
    queries = rl.rule_list("hn-queries", DEFAULT_QUERIES)
    since = int(now.timestamp()) - hours * 3600
    seen, items = set(), []

    def take(batch):
        for item in batch:
            if item["objectID"] in seen:
                continue
            seen.add(item["objectID"])
            items.append(item)

    if dry_run:
        take(parse_hits(rl.fixture("hn.json"), "(fixture)"))
        return items
    failures = 0
    for index, query in enumerate(queries):
        params = urllib.parse.urlencode({"query": query, "tags": "story", "hitsPerPage": limit,
                                         "numericFilters": "created_at_i>%d" % since})
        try:
            take(parse_hits(rl.get_json(ENDPOINT + "?" + params, source=SOURCE), query))
        except RuntimeError as err:
            failures += 1
            rl.log(SOURCE, "query %r failed: %s" % (query, err))
        if index < len(queries) - 1:
            time.sleep(0.2)             # stay far below the 10,000 req/hour public limit
    if queries and failures == len(queries):
        raise RuntimeError("every query failed")
    return items


if __name__ == "__main__":
    sys.exit(rl.run_source(SOURCE, collect, __doc__, DEFAULT_LIMIT))
