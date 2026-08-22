#!/usr/bin/env python3
"""YouTube source for the trend radar: the most-viewed videos of the last 7 days per query.

    python3 youtube_recent.py --hours 48 --limit 25 [--out FILE] [--dry-run]

Needs YT_API_KEY (skipped with a note when absent). search.list (part=snippet, type=video,
order=viewCount, publishedAfter=now-7d, maxResults=--limit, relevanceLanguage=en) per query in
rules/sources.md (block ```youtube-queries), then one videos.list (statistics, contentDetails,
snippet) per 50 ids. Quota: 100 units per search call plus 1 per videos.list, about 600 of the
daily 10,000 for the default six queries. --hours only feeds views_per_hour; the 7-day search
window is fixed so the velocity comparison stays stable.

Output: JSON list with id, url, title, channel, channel_id, views, likes, comments,
published_at, duration_s, views_per_hour, description (300 chars).
"""
from __future__ import annotations

import datetime as dt
import re
import sys
import urllib.parse

import radarlib as rl

SOURCE = "youtube"
DEFAULT_LIMIT = 25
DEFAULT_QUERIES = ["local ai", "dgx spark", "ollama", "llama.cpp", "run llm locally", "local llm"]
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"
DURATION_RE = re.compile(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")


def duration_seconds(text) -> int | None:
    match = DURATION_RE.fullmatch(str(text or ""))
    if not match:
        return None
    days, hours, minutes, seconds = (int(x or 0) for x in match.groups())
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def parse_videos(items: list, now) -> list[dict]:
    out = []
    for video in items or []:
        video_id = video.get("id") if isinstance(video.get("id"), str) else (video.get("id") or {}).get("videoId")
        if not video_id:
            continue
        snippet = video.get("snippet") or {}
        stats = video.get("statistics") or {}
        details = video.get("contentDetails") or {}
        published = rl.parse_time(snippet.get("publishedAt"))
        views = int(stats.get("viewCount") or 0)
        age = rl.age_hours(published, now)
        per_hour = round(views / max(1.0, age), 1) if age is not None else None
        out.append({
            "source": SOURCE,
            "id": video_id,
            "url": "https://www.youtube.com/watch?v=" + video_id,
            "title": rl.clip(snippet.get("title"), 300),
            "channel": rl.clip(snippet.get("channelTitle"), 120),
            "channel_id": snippet.get("channelId"),
            "views": views,
            "likes": int(stats.get("likeCount") or 0),
            "comments": int(stats.get("commentCount") or 0),
            "published_at": rl.iso(published),
            "duration_s": duration_seconds(details.get("duration")),
            "views_per_hour": per_hour,
            "description": rl.clip(snippet.get("description"), 300),
        })
    return out


def _search_ids(query: str, key: str, limit: int, published_after: str) -> list[str]:
    params = urllib.parse.urlencode({"part": "snippet", "type": "video", "order": "viewCount",
                                     "publishedAfter": published_after, "maxResults": min(limit, 50),
                                     "relevanceLanguage": "en", "q": query, "key": key})
    data = rl.get_json(SEARCH_URL + "?" + params, source=SOURCE)
    return [(it.get("id") or {}).get("videoId") for it in data.get("items") or []
            if (it.get("id") or {}).get("videoId")]


def _videos(ids: list[str], key: str) -> list[dict]:
    items = []
    for start in range(0, len(ids), 50):
        params = urllib.parse.urlencode({"part": "statistics,contentDetails,snippet",
                                         "id": ",".join(ids[start:start + 50]), "key": key})
        items += rl.get_json(VIDEOS_URL + "?" + params, source=SOURCE).get("items") or []
    return items


def collect(hours: int = 48, limit: int = DEFAULT_LIMIT, dry_run: bool = False) -> list[dict]:
    now = rl.now_for(dry_run)
    if dry_run:
        fixture = rl.fixture("youtube_recent.json")
        wanted = []
        for query_items in (fixture.get("search") or {}).values():
            for it in (query_items.get("items") or [])[:limit]:
                vid = (it.get("id") or {}).get("videoId")
                if vid and vid not in wanted:
                    wanted.append(vid)
        videos = [v for v in (fixture.get("videos") or {}).get("items") or [] if v.get("id") in wanted]
        return parse_videos(videos, now)
    key = rl.env("YT_API_KEY")
    if not key:
        raise rl.Skip("YT_API_KEY not set")
    queries = rl.rule_list("youtube-queries", DEFAULT_QUERIES)
    published_after = rl.iso(now - dt.timedelta(days=7))
    ids, failures = [], 0
    for query in queries:
        try:
            for vid in _search_ids(query, key, limit, published_after):
                if vid not in ids:
                    ids.append(vid)
        except RuntimeError as err:
            failures += 1
            rl.log(SOURCE, "search %r failed: %s" % (query, err))
    if queries and failures == len(queries):
        raise RuntimeError("every search failed (quota exhausted or key rejected)")
    return parse_videos(_videos(ids, key), now) if ids else []


if __name__ == "__main__":
    sys.exit(rl.run_source(SOURCE, collect, __doc__, DEFAULT_LIMIT))
