#!/usr/bin/env python3
"""Competition snapshot for a keyword from the YouTube Data API v3.

    python3 competition.py "dgx spark" [--max 20] [--out FILE] [--dry-run]

search.list (part=snippet, type=video, maxResults=--max, order=relevance, relevanceLanguage=en),
then videos.list (statistics, contentDetails, snippet) for those ids, then channels.list
(statistics) for their channels. Quota: 100 + 1 + 1 units per run, about 80 runs fit the daily
budget shared with the trend radar. Needs YT_API_KEY (exit 1 without it); --dry-run parses
fixtures/competition.json with the clock pinned to 2026-08-25T12:00Z.

Output: {query, n, top[{id, title, channel, channel_id, subs, views, published_at, duration_s,
is_short, views_per_day, exact_title}], median_views, median_subs, share_recent_180d,
exact_title_rate, small_channel_velocity, small_channels, quota_units, fetched_at}.
"""
from __future__ import annotations

import argparse
import re
import statistics
import sys
import urllib.parse

import kwlib as kw

SOURCE = "competition"
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"
CHANNELS_URL = "https://www.googleapis.com/youtube/v3/channels"
SMALL_CHANNEL_SUBS = 10000
RECENT_DAYS = 180
SHORT_MAX_S = 180
DURATION_RE = re.compile(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")


def duration_seconds(text) -> int | None:
    match = DURATION_RE.fullmatch(str(text or ""))
    if not match:
        return None
    days, hours, minutes, seconds = (int(x or 0) for x in match.groups())
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def tokens(text: str) -> list[str]:
    return [t for t in re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).split() if t]


def build_rows(query: str, videos: list, channels: list, now) -> list[dict]:
    subs_by_channel = {}
    for channel in channels or []:
        stats = channel.get("statistics") or {}
        hidden = stats.get("hiddenSubscriberCount")
        subs_by_channel[channel.get("id")] = None if hidden else int(stats.get("subscriberCount") or 0)
    query_tokens = tokens(query)
    rows = []
    for video in videos or []:
        video_id = video.get("id") if isinstance(video.get("id"), str) else (video.get("id") or {}).get("videoId")
        if not video_id:
            continue
        snippet = video.get("snippet") or {}
        stats = video.get("statistics") or {}
        published = kw.parse_time(snippet.get("publishedAt"))
        age_days = max(1.0, (now - published).total_seconds() / 86400.0) if published else None
        views = int(stats.get("viewCount") or 0)
        duration = duration_seconds((video.get("contentDetails") or {}).get("duration"))
        title_tokens = set(tokens(snippet.get("title")))
        rows.append({
            "id": video_id,
            "title": snippet.get("title") or "",
            "channel": snippet.get("channelTitle") or "",
            "channel_id": snippet.get("channelId"),
            "subs": subs_by_channel.get(snippet.get("channelId")),
            "views": views,
            "published_at": kw.iso(published),
            "duration_s": duration,
            "is_short": duration is not None and duration <= SHORT_MAX_S,
            "views_per_day": round(views / age_days, 1) if age_days else None,
            "age_days": round(age_days, 1) if age_days else None,
            "exact_title": bool(query_tokens) and all(t in title_tokens for t in query_tokens),
        })
    return rows


def summarize(query: str, rows: list, now, quota_units: int) -> dict:
    subs = [r["subs"] for r in rows if r["subs"] is not None]
    small = [r for r in rows if r["subs"] is not None and r["subs"] < SMALL_CHANNEL_SUBS
             and r["views_per_day"] is not None]
    recent = [r for r in rows if r["age_days"] is not None and r["age_days"] <= RECENT_DAYS]
    return {
        "query": query,
        "n": len(rows),
        "top": rows,
        "median_views": statistics.median([r["views"] for r in rows]) if rows else 0,
        "median_subs": statistics.median(subs) if subs else 0,
        "share_recent_180d": round(len(recent) / len(rows), 3) if rows else 0.0,
        "exact_title_rate": round(sum(1 for r in rows if r["exact_title"]) / len(rows), 3) if rows else 0.0,
        "small_channel_velocity": round(statistics.fmean(r["views_per_day"] for r in small), 1) if small else None,
        "small_channels": len(small),
        "quota_units": quota_units,
        "fetched_at": kw.iso(now),
    }


def _search_ids(query: str, key: str, limit: int) -> list[str]:
    params = urllib.parse.urlencode({"part": "snippet", "type": "video", "maxResults": limit,
                                     "order": "relevance", "relevanceLanguage": "en", "q": query, "key": key})
    data = kw.get_json(SEARCH_URL + "?" + params, source=SOURCE)
    return [(it.get("id") or {}).get("videoId") for it in data.get("items") or []
            if (it.get("id") or {}).get("videoId")]


def _batched(url: str, part: str, ids: list[str], key: str) -> list[dict]:
    items = []
    for start in range(0, len(ids), 50):
        params = urllib.parse.urlencode({"part": part, "id": ",".join(ids[start:start + 50]), "key": key})
        items += kw.get_json(url + "?" + params, source=SOURCE).get("items") or []
    return items


def collect(query: str, limit: int, dry_run: bool) -> dict:
    now = kw.now_for(dry_run)
    if dry_run:
        fixture = kw.fixture("competition.json")
        ids = [(it.get("id") or {}).get("videoId") for it in (fixture.get("search") or {}).get("items") or []][:limit]
        videos = [v for v in (fixture.get("videos") or {}).get("items") or [] if v.get("id") in ids]
        channels = (fixture.get("channels") or {}).get("items") or []
        return summarize(query, build_rows(query, videos, channels, now), now, 0)
    key = kw.env("YT_API_KEY")
    if not key:
        raise RuntimeError("YT_API_KEY not set (use --dry-run for fixture output)")
    ids = _search_ids(query, key, limit)
    if not ids:
        return summarize(query, [], now, 100)
    videos = _batched(VIDEOS_URL, "statistics,contentDetails,snippet", ids, key)
    channel_ids = []
    for video in videos:
        cid = (video.get("snippet") or {}).get("channelId")
        if cid and cid not in channel_ids:
            channel_ids.append(cid)
    channels = _batched(CHANNELS_URL, "statistics", channel_ids, key) if channel_ids else []
    units = 100 + (len(ids) + 49) // 50 + (len(channel_ids) + 49) // 50
    return summarize(query, build_rows(query, videos, channels, now), now, units)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", help="keyword to inspect, for example \"dgx spark\"")
    ap.add_argument("--max", type=int, default=20, help="videos to inspect, 1-50 (default 20)")
    ap.add_argument("--out", help="write the JSON here instead of stdout")
    ap.add_argument("--dry-run", action="store_true", help="fixture only, no network, no quota")
    args = ap.parse_args(argv)
    if not args.query.strip() or not 1 <= args.max <= 50:
        kw.log(SOURCE, "error: query must be non-empty and --max between 1 and 50")
        return 1
    kw.load_env()
    try:
        data = collect(args.query.strip(), args.max, args.dry_run)
    except Exception as err:
        kw.log(SOURCE, "error: %s" % err)
        return 1
    kw.emit(data, args.out)
    kw.log(SOURCE, "%r: %d videos, median views %s, median subs %s, exact-title rate %s%s" % (
        data["query"], data["n"], data["median_views"], data["median_subs"], data["exact_title_rate"],
        " (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
