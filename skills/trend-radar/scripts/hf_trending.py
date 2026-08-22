#!/usr/bin/env python3
"""Hugging Face source for the trend radar: trending and most-downloaded models (no key needed).

    python3 hf_trending.py --hours 48 --limit 40 [--out FILE] [--dry-run]

Two calls: /api/models?sort=trendingScore&direction=-1&limit=N and ?sort=downloads&direction=-1.
Kept: pipeline tags text-generation, image-text-to-text (today's tag for vision-language models),
image-to-text, text-to-speech, automatic-speech-recognition, text-to-image, text-to-video, created
(or, failing that, modified) inside the last max(--hours, 336) hours. Trending builds over days,
so the window never drops below two weeks; the radar's decay ranks the older ones down.
The list endpoint returns createdAt but usually no lastModified.

Output: JSON list with id, url, title (the id), pipeline_tag, likes, downloads, lastModified,
createdAt, trendingScore, lists (which of the two lists carried it), published_at.
"""
from __future__ import annotations

import datetime as dt
import sys

import radarlib as rl

SOURCE = "hf"
DEFAULT_LIMIT = 40
PIPELINES = {"text-generation", "image-text-to-text", "image-to-text", "text-to-speech",
             "automatic-speech-recognition", "text-to-image", "text-to-video"}
ENDPOINT = "https://huggingface.co/api/models"


def parse_models(models: list, list_name: str, now, window_hours: int) -> list[dict]:
    cutoff = now - dt.timedelta(hours=window_hours)
    items = []
    for model in models or []:
        tag = model.get("pipeline_tag")
        model_id = model.get("id") or model.get("modelId")
        if tag not in PIPELINES or not model_id or model.get("private"):
            continue
        created = rl.parse_time(model.get("createdAt"))
        modified = rl.parse_time(model.get("lastModified"))
        stamp = created or modified
        if stamp and stamp < cutoff:
            continue
        items.append({
            "source": SOURCE,
            "id": model_id,
            "url": "https://huggingface.co/" + model_id,
            "title": model_id,
            "pipeline_tag": tag,
            "likes": int(model.get("likes") or 0),
            "downloads": int(model.get("downloads") or 0),
            "lastModified": model.get("lastModified"),
            "createdAt": model.get("createdAt"),
            "trendingScore": float(model.get("trendingScore") or 0),
            "lists": [list_name],
            "published_at": rl.iso(stamp),
        })
    return items


def merge(batches: list[list[dict]]) -> list[dict]:
    """A model present in both lists is one item that remembers both lists."""
    by_id: dict[str, dict] = {}
    for batch in batches:
        for item in batch:
            kept = by_id.get(item["id"])
            if kept:
                kept["lists"] = sorted(set(kept["lists"]) | set(item["lists"]))
                kept["trendingScore"] = max(kept["trendingScore"], item["trendingScore"])
            else:
                by_id[item["id"]] = item
    return list(by_id.values())


def collect(hours: int = 48, limit: int = DEFAULT_LIMIT, dry_run: bool = False) -> list[dict]:
    now = rl.now_for(dry_run)
    window = max(hours, 336)
    if dry_run:
        fixture = rl.fixture("hf_trending.json")
        return merge([parse_models(fixture.get("trending") or [], "trending", now, window)[:limit],
                      parse_models(fixture.get("downloads") or [], "downloads", now, window)[:limit]])
    batches, failures = [], 0
    for list_name, sort_key in (("trending", "trendingScore"), ("downloads", "downloads")):
        url = "%s?sort=%s&direction=-1&limit=%d" % (ENDPOINT, sort_key, limit)
        try:
            data = rl.get_json(url, source=SOURCE)
            if not isinstance(data, list):
                raise RuntimeError("unexpected response shape")
            batches.append(parse_models(data, list_name, now, window))
        except RuntimeError as err:
            failures += 1
            rl.log(SOURCE, "%s list failed: %s" % (list_name, err))
    if failures == 2:
        raise RuntimeError("both model lists failed")
    return merge(batches)


if __name__ == "__main__":
    sys.exit(rl.run_source(SOURCE, collect, __doc__, DEFAULT_LIMIT))
