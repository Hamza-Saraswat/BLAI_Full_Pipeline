#!/usr/bin/env python3
"""Public YouTube stats for the channel's videos (Data API v3 with an API key, no OAuth).

    python3 skills/youtube-analytics/scripts/yt_stats.py                        # @BuildLocalAI, all uploads
    python3 skills/youtube-analytics/scripts/yt_stats.py --handle @Other --max 200
    python3 skills/youtube-analytics/scripts/yt_stats.py --channel-id UCxxxxxxxx
    python3 skills/youtube-analytics/scripts/yt_stats.py --ids a,b,c            # explicit video ids
    python3 skills/youtube-analytics/scripts/yt_stats.py --dry-run              # fixture, no network

channels.list (forHandle or id) -> uploads playlist -> playlistItems.list (paged, 50 per call) ->
videos.list (statistics, contentDetails, snippet; 50 ids per call). Video ids map to slugs through
the youtube_url of workspaces/*/published/*.md and videos/*.md. Writes analytics/stats/<date>.json
(committed on purpose: the retro needs last week's snapshot too). Needs YT_API_KEY in the
environment (or build/.env when python-dotenv is installed). Quota: about 1 + 2 * ceil(n / 50)
units of the 10,000 daily units. Exit codes: 0 ok, 1 failure (no key, API error, no channel).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "tools"))
try:
    import hubnote  # noqa: E402
except ImportError:  # running outside the repo: slug mapping is skipped
    hubnote = None

API = "https://www.googleapis.com/youtube/v3/"
DEFAULT_HANDLE = "@BuildLocalAI"
WORKSPACES = ("shorts", "long-form")
YT_ID_RE = re.compile(r"(?:youtu\.be/|[?&]v=|/shorts/|/live/|/embed/)([A-Za-z0-9_-]{11})")
FIXTURE = {
    "channel": {"id": "UCfixture000000000000000", "handle": "@buildlocalai", "title": "Build Local AI",
                "subscribers": 1200, "views": 98000, "videos": 3},
    "rows": [
        {"videoId": "dQw4w9WgXcQ", "slug": "2026-08-17-deepseek-v4-flash-128gb", "workspace": "shorts", "format": "short",
         "title": "Can DeepSeek V4 Flash run on 128 GB?", "publishedAt": "2026-08-17T16:00:00Z", "durationS": 48.0,
         "views": 4200, "likes": 210, "comments": 18},
        {"videoId": "9bZkp7q19f0", "slug": "2026-08-19-kv-cache-explained", "workspace": "shorts", "format": "short",
         "title": "KV cache, explained with a bookshelf", "publishedAt": "2026-08-19T23:00:00Z", "durationS": 55.0,
         "views": 1500, "likes": 90, "comments": 7},
        {"videoId": "kJQP7kiw5Fk", "slug": "2026-08-18-spark-vs-5090-benchmarks", "workspace": "long-form", "format": "long",
         "title": "DGX Spark vs RTX 5090: 12 models measured", "publishedAt": "2026-08-18T14:00:00Z", "durationS": 720.0,
         "views": 6100, "likes": 380, "comments": 64},
    ],
}


class ApiError(Exception):
    pass


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def load_env() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore
    except ImportError:
        return
    p = REPO / "build" / ".env"
    if p.exists():
        load_dotenv(p, override=False)


def api(endpoint: str, params: dict, key: str) -> dict:
    """One Data API call. Error messages name the endpoint, never the URL (it carries the key)."""
    qs = urllib.parse.urlencode(dict(params, key=key))
    req = urllib.request.Request(API + endpoint + "?" + qs, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        raise ApiError("YouTube API HTTP %d on %s: %s" % (e.code, endpoint, detail))
    except urllib.error.URLError as e:
        raise ApiError("YouTube API unreachable (%s): %s" % (endpoint, e.reason))


def iso_duration_s(d: str):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    if not m or not any(m.groups()):
        return None
    days, h, mi, s = (int(g or 0) for g in m.groups())
    return float(days * 86400 + h * 3600 + mi * 60 + s)


def video_id(url: str) -> str:
    m = YT_ID_RE.search(url or "")
    return m.group(1) if m else ""


def resolve_channel(key: str, channel_id: str, handle: str) -> dict:
    params = {"part": "snippet,contentDetails,statistics"}
    if channel_id:
        params["id"] = channel_id
    else:
        params["forHandle"] = handle if handle.startswith("@") else "@" + handle
    items = api("channels", params, key).get("items") or []
    if not items:
        raise ApiError("channel not found: %s" % (channel_id or handle))
    c = items[0]
    st = c.get("statistics") or {}
    return {
        "id": c["id"],
        "handle": (c.get("snippet") or {}).get("customUrl", ""),
        "title": (c.get("snippet") or {}).get("title", ""),
        "uploads": ((c.get("contentDetails") or {}).get("relatedPlaylists") or {}).get("uploads", ""),
        "subscribers": int(st.get("subscriberCount", 0)) if not st.get("hiddenSubscriberCount") else None,
        "views": int(st.get("viewCount", 0)),
        "videos": int(st.get("videoCount", 0)),
    }


def upload_ids(key: str, playlist_id: str, limit: int) -> list:
    ids, token = [], None
    while len(ids) < limit:
        params = {"part": "contentDetails", "playlistId": playlist_id, "maxResults": 50}
        if token:
            params["pageToken"] = token
        data = api("playlistItems", params, key)
        ids += [it["contentDetails"]["videoId"] for it in data.get("items", []) if it.get("contentDetails")]
        token = data.get("nextPageToken")
        if not token:
            break
    return ids[:limit]


def fetch_videos(key: str, ids: list) -> dict:
    out = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        data = api("videos", {"part": "statistics,contentDetails,snippet", "id": ",".join(chunk), "maxResults": 50}, key)
        for it in data.get("items", []):
            st, cd, sn = it.get("statistics") or {}, it.get("contentDetails") or {}, it.get("snippet") or {}
            out[it["id"]] = {
                "videoId": it["id"],
                "title": sn.get("title", ""),
                "publishedAt": sn.get("publishedAt", ""),
                "durationS": iso_duration_s(cd.get("duration", "")),
                "views": int(st.get("viewCount", 0)),
                "likes": int(st["likeCount"]) if "likeCount" in st else None,
                "comments": int(st["commentCount"]) if "commentCount" in st else None,
            }
    return out


def slug_map() -> dict:
    """videoId -> (slug, workspace) from the youtube_url of published/ and videos/ notes."""
    m = {}
    if hubnote is None:
        return m
    for ws in WORKSPACES:
        for sub in ("published", "videos"):
            for p in sorted((REPO / "workspaces" / ws / sub).glob("*.md")):
                meta, _ = hubnote.read(p)
                vid = video_id(meta.get("youtube_url", ""))
                if vid and meta.get("slug"):
                    m.setdefault(vid, (meta["slug"], ws))
    return m


def build_rows(ids: list, stats: dict, slugs: dict) -> list:
    rows = []
    for vid in ids:
        s = stats.get(vid)
        slug, ws = slugs.get(vid, ("", ""))
        row = {"videoId": vid, "slug": slug, "workspace": ws}
        if s is None:
            row.update({"missing": True, "views": None, "likes": None, "comments": None, "durationS": None,
                        "title": "", "publishedAt": "", "format": ""})
        else:
            row.update(s)
            d = s.get("durationS")
            row["format"] = "short" if ws == "shorts" else "long" if ws == "long-form" else (
                "short" if d is not None and d <= 180 else "long")
        rows.append(row)
    return rows


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--handle", default=os.environ.get("YT_CHANNEL_HANDLE") or DEFAULT_HANDLE,
                    help="channel handle (default %s, or YT_CHANNEL_HANDLE)" % DEFAULT_HANDLE)
    ap.add_argument("--channel-id", default=os.environ.get("YT_CHANNEL_ID", ""), help="channel id UC... (or YT_CHANNEL_ID)")
    ap.add_argument("--ids", help="comma-separated video ids (skips the channel lookup)")
    ap.add_argument("--max", type=int, default=500, help="newest uploads to fetch (default 500)")
    ap.add_argument("--out", default=str(REPO / "analytics" / "stats"), help="snapshot directory (default analytics/stats)")
    ap.add_argument("--dry-run", action="store_true", help="print a fixture snapshot; no network, nothing written")
    a = ap.parse_args(argv)
    now = dt.datetime.now(dt.timezone.utc)
    if a.dry_run:
        snap = {"fetched_at": "2026-08-23T13:05:00Z", "dry_run": True, "channel": FIXTURE["channel"], "rows": FIXTURE["rows"]}
        print(json.dumps(snap, indent=2))
        log("dry-run: %d fixture rows, nothing written" % len(snap["rows"]))
        return 0
    load_env()
    key = os.environ.get("YT_API_KEY", "")
    if not key:
        log("error: YT_API_KEY is not set (Google Cloud console: enable YouTube Data API v3, create an API key)")
        return 1
    try:
        channel = None
        if a.ids:
            ids = [v.strip() for v in a.ids.split(",") if v.strip()]
        else:
            channel = resolve_channel(key, a.channel_id, a.handle)
            if not channel["uploads"]:
                raise ApiError("channel %s has no uploads playlist" % channel["id"])
            ids = upload_ids(key, channel["uploads"], a.max)
        if not ids:
            log("error: no video ids to fetch")
            return 1
        stats = fetch_videos(key, ids)
    except ApiError as e:
        log("error: %s" % e)
        return 1
    rows = build_rows(ids, stats, slug_map())
    snap = {"fetched_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "channel": channel, "rows": rows}
    out_dir = pathlib.Path(a.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / (now.strftime("%Y-%m-%d") + ".json")
    path.write_text(json.dumps(snap, indent=2) + "\n", encoding="utf-8")
    w = max([len(r["slug"] or r["videoId"]) for r in rows] + [4])
    log("%-*s  %-11s  %8s  %6s  %8s" % (w, "slug", "videoId", "views", "likes", "comments"))
    for r in rows[:25]:
        log("%-*s  %-11s  %8s  %6s  %8s" % (w, r["slug"] or "-", r["videoId"], r.get("views"), r.get("likes"), r.get("comments")))
    if len(rows) > 25:
        log("... %d more" % (len(rows) - 25))
    print(json.dumps({"videos": len(rows), "mapped_to_slugs": sum(1 for r in rows if r["slug"]), "snapshot": str(path)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
