#!/usr/bin/env python3
"""Reddit source for the trend radar: top posts from the local-AI subreddits.

    python3 reddit.py --hours 48 --limit 25 [--out FILE] [--dry-run]

OAuth client-credentials flow when REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET are set, else the
public https://www.reddit.com/r/<sub>/top.json endpoint. The user agent comes from
REDDIT_USER_AGENT (default blai-radar/1.0). Subreddit list: rules/sources.md, block
```reddit-subreddits (built-in default below when the rule file is missing).

Output: JSON list, one object per post with title, url (outbound link, or the thread for self
posts), permalink, subreddit, score, num_comments, created_utc, published_at, selftext (300 chars).
"""
from __future__ import annotations

import base64
import sys
import urllib.parse

import radarlib as rl

SOURCE = "reddit"
DEFAULT_LIMIT = 25
DEFAULT_SUBREDDITS = ["LocalLLaMA", "ollama", "LocalLLM"]
TOKEN_URL = "https://www.reddit.com/api/v1/access_token"


def _token(client_id: str, secret: str, user_agent: str) -> str:
    basic = base64.b64encode(("%s:%s" % (client_id, secret)).encode("utf-8")).decode("ascii")
    data = rl.get_json(TOKEN_URL, headers={"Authorization": "Basic " + basic, "User-Agent": user_agent,
                                           "Content-Type": "application/x-www-form-urlencoded"},
                       data="grant_type=client_credentials", source=SOURCE)
    token = data.get("access_token") if isinstance(data, dict) else None
    if not token:
        raise RuntimeError("OAuth response carried no access_token")
    return token


def _listing(sub: str, period: str, limit: int, user_agent: str, token: str | None) -> dict:
    query = urllib.parse.urlencode({"t": period, "limit": limit, "raw_json": 1})
    if token:
        url = "https://oauth.reddit.com/r/%s/top?%s" % (sub, query)
        headers = {"Authorization": "bearer " + token, "User-Agent": user_agent}
    else:
        url = "https://www.reddit.com/r/%s/top.json?%s" % (sub, query)
        headers = {"User-Agent": user_agent}
    return rl.get_json(url, headers=headers, source=SOURCE)


def parse_listing(sub: str, listing: dict, now, hours: int) -> list[dict]:
    """Turn one Reddit listing (public or OAuth shape, identical) into radar source items."""
    cutoff = now.timestamp() - hours * 3600
    items = []
    for child in ((listing or {}).get("data") or {}).get("children") or []:
        post = child.get("data") or {}
        if post.get("stickied") or post.get("over_18"):
            continue
        created = post.get("created_utc")
        if created is None or float(created) < cutoff:
            continue
        permalink = "https://www.reddit.com" + str(post.get("permalink") or "")
        url = str(post.get("url") or permalink)
        if post.get("is_self") or url.startswith("/"):
            url = permalink
        items.append({
            "source": SOURCE,
            "subreddit": post.get("subreddit") or sub,
            "title": rl.clip(post.get("title"), 300),
            "url": url,
            "permalink": permalink,
            "score": int(post.get("score") or 0),
            "num_comments": int(post.get("num_comments") or 0),
            "created_utc": int(float(created)),
            "published_at": rl.iso(rl.parse_time(created)),
            "selftext": rl.clip(post.get("selftext"), 300),
        })
    return items


def collect(hours: int = 48, limit: int = DEFAULT_LIMIT, dry_run: bool = False) -> list[dict]:
    now = rl.now_for(dry_run)
    subs = rl.rule_list("reddit-subreddits", DEFAULT_SUBREDDITS)
    if dry_run:
        fixture = rl.fixture("reddit.json")
        items = []
        for sub in subs:
            items += parse_listing(sub, fixture.get(sub) or {}, now, hours)[:limit]
        return items
    user_agent = rl.env("REDDIT_USER_AGENT") or rl.DEFAULT_UA
    client_id, secret = rl.env("REDDIT_CLIENT_ID"), rl.env("REDDIT_CLIENT_SECRET")
    token = _token(client_id, secret, user_agent) if client_id and secret else None
    rl.log(SOURCE, "mode: %s" % ("oauth" if token else "public json"))
    period = "day" if hours <= 24 else ("week" if hours <= 168 else "month")
    items, failures = [], 0
    for sub in subs:
        try:
            items += parse_listing(sub, _listing(sub, period, limit, user_agent, token), now, hours)
        except RuntimeError as err:
            failures += 1
            rl.log(SOURCE, "r/%s failed: %s" % (sub, err))
    if subs and failures == len(subs):
        raise RuntimeError("every subreddit failed")
    return items


if __name__ == "__main__":
    sys.exit(rl.run_source(SOURCE, collect, __doc__, DEFAULT_LIMIT))
