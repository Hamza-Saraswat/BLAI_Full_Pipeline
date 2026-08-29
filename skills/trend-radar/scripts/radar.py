#!/usr/bin/env python3
"""Trend radar: run every source, merge, score, dedupe, and write the daily radar files.

    python3 radar.py --workspace shorts --date YYYY-MM-DD [--hours 48] [--out DIR]
                     [--dedupe-dir workspaces/<ws>] [--dry-run]

Writes DIR/<date>-radar.json (a list of items with id, title, url, source, published_at,
signals, products, summary, why_now, score) and DIR/<date>-radar.md (a digest grouped by Shorts
lane, at least the top 30). Default DIR is
workspaces/<workspace>/stages/01-radar/output under the repo root.

Sources that lack their key are skipped with a stderr note; a source that errors is skipped
too. --dry-run parses the fixtures under fixtures/ with the clock pinned to 2026-08-25T12:00Z
and dedupes against fixtures/dedupe-workspace unless --dedupe-dir is given. stdout gets a
one-line JSON summary. Exit 1 only when no source produced an item or a file could not be written.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import radarlib as rl            # noqa: E402
import scoring                   # noqa: E402
import reddit                    # noqa: E402
import hn                        # noqa: E402
import hf_trending               # noqa: E402
import github_releases           # noqa: E402
import youtube_recent            # noqa: E402
import firecrawl_search          # noqa: E402

SOURCES = [("reddit", reddit), ("hn", hn), ("hf", hf_trending), ("github", github_releases),
           ("youtube", youtube_recent), ("firecrawl", firecrawl_search)]
PREVIOUS_RADARS = 7
DIGEST_CAP = 60
FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
TRACKING = ("utm_", "ref=", "fbclid=", "si=", "feature=")


def load_hubnote():
    sys.path.insert(0, str(rl.REPO_DIR / "tools"))
    try:
        import hubnote
        return hubnote
    except ImportError:
        rl.log("radar", "tools/hubnote.py not importable, using a minimal frontmatter reader")
        return None


def read_note(path: pathlib.Path, hubnote) -> tuple[dict, str]:
    if hubnote:
        return hubnote.read(path)
    text = path.read_text(encoding="utf-8")
    match = FM_RE.match(text)
    meta = {}
    if match:
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip("\"'")
        return meta, text[match.end():]
    return meta, text


def first_heading(body: str) -> str:
    match = re.search(r"^# (.+)$", body or "", re.M)
    return match.group(1).strip() if match else ""


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (title or "").lower())


def norm_url(url: str) -> str:
    if not url:
        return ""
    text = url.strip().lower()
    text = re.sub(r"^https?://", "", text)
    text = re.sub(r"^(www|m|old|mobile)\.", "", text)
    text = text.split("#", 1)[0]
    match = re.match(r"^youtu\.be/([a-z0-9_-]{6,})", text)
    if match:
        text = "youtube.com/watch?v=" + match.group(1)
    if "?" in text:
        base, query = text.split("?", 1)
        keep = [p for p in query.split("&") if p and not p.startswith(TRACKING)]
        text = base + ("?" + "&".join(keep) if keep else "")
    return text.rstrip("/")


def domain(url: str) -> str:
    host = urllib.parse.urlsplit(url or "").netloc.lower()
    return re.sub(r"^(www|m|old)\.", "", host) or "link"


def summary_for(raw: dict) -> str:
    source = raw.get("source")
    if source == "reddit":
        text = raw.get("selftext") or ""
    elif source == "hn":
        text = raw.get("summary") or ""
    elif source == "hf":
        text = "%s model on Hugging Face, %s likes, %s downloads, trending score %s, created %s" % (
            raw.get("pipeline_tag"), scoring.compact(raw.get("likes")), scoring.compact(raw.get("downloads")),
            scoring.compact(raw.get("trendingScore")), (raw.get("createdAt") or "")[:10])
    elif source == "github":
        text = raw.get("body") or ""
    elif source == "youtube":
        text = raw.get("description") or ""
    else:
        text = raw.get("description") or raw.get("markdown") or ""
    return rl.clip(text, 300)


def raw_signals(raw: dict) -> dict:
    keys = {"reddit": ("subreddit", "score", "num_comments"), "hn": ("points", "num_comments"),
            "hf": ("pipeline_tag", "likes", "downloads", "trendingScore", "lists"),
            "github": ("repo", "tag", "prerelease"),
            "youtube": ("channel", "views", "views_per_hour", "duration_s"), "firecrawl": ("query",)}
    return {k: raw.get(k) for k in keys.get(raw.get("source"), ()) if k in raw}


def normalize(raw: dict, now, hours: int) -> tuple[dict, set]:
    source = raw.get("source") or "unknown"
    published = rl.parse_time(raw.get("published_at"))
    age = rl.age_hours(published, now)
    title = rl.clip(raw.get("title"), 300)
    url = (raw.get("permalink") if source == "reddit" else raw.get("url")) or raw.get("url") or ""
    summary = summary_for(raw)
    text = title + " " + summary
    names, kinds = scoring.products(text)
    bonus = scoring.product_bonus(kinds)
    strength, parts = scoring.signal(raw)
    fade = scoring.decay(age, hours)
    weight = scoring.SOURCE_WEIGHT.get(source, 0.8)
    kind = scoring.why_now_kind(raw, text)
    score = min(1.0, scoring.BASE_SCALE * weight * strength * fade + bonus)
    signals = raw_signals(raw)
    signals.update({"signal": strength, "signal_parts": parts, "decay": fade,
                    "age_h": round(age, 1) if age is not None else None, "source_weight": weight,
                    "product_bonus": bonus, "why_now_kind": kind})
    item = {
        "id": "%s-%s" % (source, hashlib.sha1((url or title).encode("utf-8")).hexdigest()[:10]),
        "title": title, "url": url, "source": source, "published_at": rl.iso(published),
        "signals": signals, "products": names, "summary": summary,
        "why_now": scoring.why_now_text(kind, raw, age), "score": int(round(100 * score)),
    }
    item["_kinds"] = kinds
    item["_tag"] = raw.get("pipeline_tag")
    keys = {norm_url(u) for u in (raw.get("url"), raw.get("permalink"), raw.get("hn_url"), raw.get("html_url")) if u}
    return item, keys


def merge_duplicates(entries: list) -> tuple[list, int]:
    """Same URL or same normalized title across sources: keep the strongest, remember the rest."""
    entries.sort(key=lambda e: (-e[0]["score"], e[0]["published_at"] or ""))
    kept, by_url, by_title, merged = [], {}, {}, 0
    for item, keys in entries:
        title_key = norm_title(item["title"])
        target = next((by_url[k] for k in keys if k in by_url), None)
        if target is None and title_key:
            target = by_title.get(title_key)
        if target is not None:
            merged += 1
            if target["signals"]["why_now_kind"] == "Discussed" and item["signals"]["why_now_kind"] != "Discussed":
                target["why_now"] = item["why_now"]          # the merged source knows what happened
                target["signals"]["why_now_kind"] = item["signals"]["why_now_kind"]
            also = target["signals"].setdefault("also_seen_in", [])
            if item["source"] != target["source"] and item["source"] not in also:
                also.append(item["source"])
                target["score"] = min(100, target["score"] + scoring.CROSS_SOURCE_BOOST)
            for name in item["products"]:
                if name not in target["products"]:
                    target["products"].append(name)
            target["_kinds"] |= item["_kinds"]
            target["_keys"] |= keys
        else:
            item["_keys"] = set(keys)
            kept.append(item)
            if title_key:
                by_title[title_key] = item
        for key in keys:
            by_url.setdefault(key, target if target is not None else item)
    return kept, merged


def seen_keys(workspace_dirs: list, out_dir: pathlib.Path, date: str, hubnote) -> tuple[set, set, list]:
    titles, urls, notes = set(), set(), []
    for ws_dir in workspace_dirs:
        for sub in ("videos", "published"):
            folder = pathlib.Path(ws_dir) / sub
            if not folder.is_dir():
                continue
            count = 0
            for path in sorted(folder.glob("*.md")):
                try:
                    meta, body = read_note(path, hubnote)
                except Exception as err:
                    rl.log("radar", "could not read %s: %s" % (path, err))
                    continue
                title = meta.get("title") or first_heading(body)
                if title:
                    titles.add(norm_title(title))
                    count += 1
            notes.append("%s: %d title(s)" % (folder, count))
    previous = sorted(p for p in out_dir.glob("*-radar.json") if p.name < "%s-radar.json" % date)
    previous = previous[-PREVIOUS_RADARS:]
    for path in previous:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as err:
            rl.log("radar", "could not read %s: %s" % (path, err))
            continue
        for item in data if isinstance(data, list) else []:
            if item.get("title"):
                titles.add(norm_title(item["title"]))
            if item.get("url"):
                urls.add(norm_url(item["url"]))
    notes.append("previous radars: %d" % len(previous))
    return titles, urls, notes


def dedupe(items: list, titles: set, urls: set) -> tuple[list, dict]:
    kept, dropped = [], {"title": 0, "url": 0}
    for item in items:
        if norm_title(item["title"]) in titles:
            dropped["title"] += 1
        elif any(k in urls for k in item["_keys"]):
            dropped["url"] += 1
        else:
            kept.append(item)
    return kept, dropped


def bullet(item: dict) -> str:
    label = item["title"].replace("[", "(").replace("]", ")")
    names = ", ".join(item["products"]) or "none"
    return "- **%d** [%s](%s) (%s, %s) -- products: %s -- why now: %s" % (
        item["score"], label, item["url"], item["source"], domain(item["url"]), names, item["why_now"])


def describe(status: dict) -> str:
    if status["state"] == "ok":
        return "%d" % status["count"]
    return "%s (%s)" % (status["state"], status.get("note", ""))


def digest(items: list, args, now, status: dict, stats: dict, groups: list, label: str) -> str:
    listed = items[:DIGEST_CAP]
    lines = ["# Trend radar: %s, %s" % (args.workspace, args.date), ""]
    lines.append("- Window: %d h ending %s%s" % (args.hours, rl.iso(now), " (dry-run clock, fixtures)" if args.dry_run else ""))
    lines.append("- Sources: " + ", ".join("%s %s" % (name, describe(status[name])) for name, _ in SOURCES))
    lines.append("- Candidates %d, merged %d cross-source duplicate(s), dropped %d by dedupe (%d by title, %d by url), dropped %d off-topic, kept %d, listed %d" % (
        stats["candidates"], stats["merged"], stats["dropped_title"] + stats["dropped_url"],
        stats["dropped_title"], stats["dropped_url"], stats.get("dropped_off_topic", 0),
        len(items), len(listed)))
    lines.append("- Grouped by %s from brand-vault/content-pillars.md; score 0-100 per rules/scoring.md" % label)
    lines += ["", "## Top 10", ""]
    for rank, item in enumerate(items[:10], 1):
        lines.append("%d. %d %s (%s)" % (rank, item["score"], item["title"], item["source"]))
    buckets = {name: [] for name in groups}
    for item in listed:
        buckets.setdefault(item["signals"]["group"], []).append(item)
    for name in groups:
        rows = buckets.get(name, [])
        lines += ["", "## %s (%d)" % (name, len(rows)), ""]
        if not rows:
            lines.append("- nothing in this window")
        lines += [bullet(item) for item in rows]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workspace", required=True, choices=["shorts"])
    ap.add_argument("--date", required=True, help="run date YYYY-MM-DD, used in the output file names")
    ap.add_argument("--hours", type=int, default=48, help="look-back window for the sources (default 48)")
    ap.add_argument("--out", help="output folder (default workspaces/<ws>/stages/01-radar/output)")
    ap.add_argument("--dedupe-dir", help="workspace folder whose videos/ and published/ titles are excluded")
    ap.add_argument("--dry-run", action="store_true", help="fixtures only, no network, pinned clock")
    args = ap.parse_args(argv)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date) or args.hours <= 0:
        rl.log("radar", "error: --date must be YYYY-MM-DD and --hours positive")
        return 1
    rl.load_env()
    now = rl.now_for(args.dry_run)
    out_dir = pathlib.Path(args.out) if args.out else rl.REPO_DIR / "workspaces" / args.workspace / "stages" / "01-radar" / "output"
    out_dir = out_dir.resolve()
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as err:
        rl.log("radar", "error: cannot create %s: %s" % (out_dir, err))
        return 1

    raw, status = [], {}
    for name, module in SOURCES:
        try:
            items = module.collect(args.hours, module.DEFAULT_LIMIT, args.dry_run)
            status[name] = {"state": "ok", "count": len(items)}
            raw += items
            rl.log("radar", "%s: %d item(s)" % (name, len(items)))
        except rl.Skip as why:
            status[name] = {"state": "skipped", "count": 0, "note": str(why)}
            rl.log("radar", "%s skipped: %s" % (name, why))
        except Exception as err:
            status[name] = {"state": "error", "count": 0, "note": str(err)[:160]}
            rl.log("radar", "%s error: %s" % (name, err))
    if not raw:
        rl.log("radar", "error: no source produced an item")
        return 1

    entries = [normalize(item, now, args.hours) for item in raw]
    items, merged = merge_duplicates(entries)

    hubnote = load_hubnote()
    workspace_dirs = []
    implicit = out_dir.parents[2] if len(out_dir.parents) > 2 else None
    if implicit and (implicit / "videos").is_dir():
        workspace_dirs.append(implicit)
    if args.dedupe_dir:
        workspace_dirs.append(pathlib.Path(args.dedupe_dir))
    elif args.dry_run:
        workspace_dirs.append(rl.FIXTURES_DIR / "dedupe-workspace")
    titles, urls, notes = seen_keys(workspace_dirs, out_dir, args.date, hubnote)
    rl.log("radar", "dedupe keys: " + "; ".join(notes))
    items, dropped = dedupe(items, titles, urls)

    # relevance gate: this channel is about running AI on your own hardware, and the
    # discussion sources rank by popularity, not by topic.
    relevant, off_topic = [], []
    for item in items:
        ok, why = scoring.relevance(item["title"] + " " + item["summary"] + " " + (item.get("url") or ""),
                                    item.get("products") or [])
        if ok:
            item["signals"]["relevance"] = why
            relevant.append(item)
        else:
            off_topic.append(item["title"])
    dropped["off_topic"] = len(off_topic)
    if off_topic:
        rl.log("radar", "dropped %d off-topic item(s): %s"
               % (len(off_topic), "; ".join(t[:48] for t in off_topic[:4])
                  + (" ..." if len(off_topic) > 4 else "")))
    items = relevant

    for item in items:
        item["signals"]["group"] = scoring.lane(item["title"], item["summary"], item["_kinds"], item["products"])
    items.sort(key=lambda it: it["published_at"] or "", reverse=True)   # newest first among equal scores
    items.sort(key=lambda it: it["score"], reverse=True)
    for item in items:
        for private in ("_kinds", "_tag", "_keys"):
            item.pop(private, None)

    stats = {"candidates": len(raw), "merged": merged, "dropped_title": dropped["title"],
             "dropped_url": dropped["url"], "dropped_off_topic": dropped.get("off_topic", 0)}
    json_path = out_dir / ("%s-radar.json" % args.date)
    md_path = out_dir / ("%s-radar.md" % args.date)
    groups, label = scoring.LANE_ORDER, "Shorts lane"
    try:
        json_path.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        md_path.write_text(digest(items, args, now, status, stats, groups, label), encoding="utf-8")
    except OSError as err:
        rl.log("radar", "error: cannot write outputs: %s" % err)
        return 1
    rl.log("radar", "kept %d item(s); wrote %s and %s" % (len(items), json_path.name, md_path.name))
    summary = {"date": args.date, "workspace": args.workspace, "json": str(json_path), "md": str(md_path),
               "kept": len(items), "merged": merged, "dropped": dropped, "sources": status}
    sys.stdout.write(json.dumps(summary) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
