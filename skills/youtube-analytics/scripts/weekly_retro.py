#!/usr/bin/env python3
"""Weekly retro: rank the week's videos and propose playbook edits.

    python3 skills/youtube-analytics/scripts/weekly_retro.py --week 2026-W34 --out analytics/
    python3 skills/youtube-analytics/scripts/weekly_retro.py --week 2026-W34 --dry-run     # fixture, stdout only
    python3 skills/youtube-analytics/scripts/weekly_retro.py --week 2026-W34 --stdout      # real data, no file

Reads the two latest stats snapshots in analytics/stats/ (the latest, and the latest one at least
six days older), the published/*.md notes of both workspaces plus their hub notes, computes the
view delta between the snapshots and views per day for every video, ranks the videos published in
the ISO week (Monday to Sunday, America/Chicago) and writes analytics/<year>-w<ww>.md in the layout
of rules/retro-format.md. Exit codes: 0 ok, 1 failure (bad week, no snapshot, no published notes).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "tools"))
import hubnote  # noqa: E402

WORKSPACES = ("shorts", "long-form")
YT_ID_RE = re.compile(r"(?:youtu\.be/|[?&]v=|/shorts/|/live/|/embed/)([A-Za-z0-9_-]{11})")
PILLAR_FILE = "brand-vault/content-pillars.md"
TIMING_FILE = "shared/playbook/publish-timing.md"
SEO_FILE = "shared/playbook/seo-rubric.md"


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def tz_ct():
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo("America/Chicago")
    except Exception:  # noqa: BLE001
        return dt.timezone(dt.timedelta(hours=-5))


TZ = tz_ct()


def parse_week(text: str):
    m = re.fullmatch(r"(\d{4})-?[Ww]?(\d{1,2})", (text or "").strip())
    if not m:
        raise ValueError("week must look like 2026-W34")
    year, week = int(m.group(1)), int(m.group(2))
    monday = dt.date.fromisocalendar(year, week, 1)
    return year, week, monday, monday + dt.timedelta(days=6)


def parse_time(value):
    value = (value or "").strip()
    if not value:
        return None
    try:
        t = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)


def video_id(url: str) -> str:
    m = YT_ID_RE.search(url or "")
    return m.group(1) if m else ""


def fmt(n) -> str:
    if n is None:
        return "n/a"
    return "{:,.0f}".format(n) if abs(n) >= 10 else "{:.1f}".format(n)


# -- inputs ---------------------------------------------------------------------
def load_snapshots(stats_dir: pathlib.Path) -> list:
    out = []
    for p in sorted(stats_dir.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            log("warning: skipping bad JSON %s" % p)
            continue
        fetched = parse_time(data.get("fetched_at")) or parse_time(p.stem + "T12:00:00Z")
        if fetched:
            out.append((fetched, data, p.name))
    out.sort(key=lambda r: r[0])
    return out


def pick_snapshots(snaps: list):
    if not snaps:
        return None, None
    current = snaps[-1]
    for s in reversed(snaps[:-1]):
        if (current[0] - s[0]).days >= 6:
            return current, s
    return current, (snaps[0] if len(snaps) > 1 else None)


def rows_by_id(snap) -> dict:
    return {r["videoId"]: r for r in (snap[1].get("rows") or []) if r.get("videoId")} if snap else {}


def load_published() -> list:
    vids = []
    for ws in WORKSPACES:
        wsdir = REPO / "workspaces" / ws
        for p in sorted((wsdir / "published").glob("*.md")):
            meta, _ = hubnote.read(p)
            if not meta.get("slug"):
                continue
            hub = {}
            hp = wsdir / "videos" / (meta["slug"] + ".md")
            if hp.exists():
                hub, _ = hubnote.read(hp)
            url = meta.get("youtube_url") or hub.get("youtube_url", "")
            vids.append({
                "slug": meta["slug"], "workspace": ws, "title": meta.get("title") or hub.get("title", ""),
                "pillar": hub.get("pillar") or hub.get("series") or "", "structure": hub.get("structure", ""),
                "style_pack": hub.get("style_pack", ""), "seo_score": hub.get("seo_score", ""),
                "published_slot": meta.get("published_slot", ""), "video_id": video_id(url),
            })
    return vids


def load_not_shipped(monday: dt.date, sunday: dt.date) -> list:
    out = []
    for ws in WORKSPACES:
        for p in sorted((REPO / "workspaces" / ws / "videos").glob("*.md")):
            meta, _ = hubnote.read(p)
            if meta.get("status") not in ("blocked", "rejected"):
                continue
            created = meta.get("created", "")[:10]
            if monday.isoformat() <= created <= sunday.isoformat():
                out.append({"slug": meta.get("slug", p.stem), "workspace": ws, "status": meta["status"],
                            "reason": meta.get("blocked_reason") or meta.get("feedback") or ""})
    return out


# -- numbers ----------------------------------------------------------------
def enrich(videos: list, current, previous) -> None:
    cur, prev = rows_by_id(current), rows_by_id(previous)
    cur_by_slug = {r.get("slug"): r for r in cur.values() if r.get("slug")}
    now = current[0] if current else dt.datetime.now(dt.timezone.utc)
    for v in videos:
        row = cur.get(v["video_id"]) or cur_by_slug.get(v["slug"]) or {}
        if row and not v["video_id"]:
            v["video_id"] = row.get("videoId", "")
        v["views"] = row.get("views")
        v["likes"] = row.get("likes")
        v["comments"] = row.get("comments")
        published = parse_time(row.get("publishedAt")) or parse_time(v.get("published_slot"))
        v["published_at"] = published
        local = published.astimezone(TZ) if published else None
        v["local_date"] = local.date() if local else None
        v["slot"] = local.strftime("%a %H:%M") if local else ""
        v["slot_hour"] = local.hour if local else None
        age = (now - published).total_seconds() / 86400 if published else None
        v["age_days"] = age
        v["vpd"] = v["views"] / max(age, 1.0) if v["views"] is not None and age is not None else None
        prow = prev.get(v["video_id"]) if v["video_id"] else None
        v["views_prev"] = prow.get("views") if prow else None
        v["delta"] = (v["views"] - v["views_prev"]) if v["views"] is not None and v["views_prev"] is not None else None
        try:
            v["seo"] = float(v.get("seo_score") or 0)
        except (TypeError, ValueError):
            v["seo"] = 0.0


def group_means(vs: list, key: str) -> dict:
    groups = {}
    for v in vs:
        k = str(v.get(key) or "")
        if k and v.get("vpd") is not None:
            groups.setdefault(k, []).append(v["vpd"])
    return {k: (len(x), statistics.mean(x)) for k, x in groups.items()}


def label(v: dict) -> str:
    parts = [v.get("workspace", ""), v.get("pillar") or "no pillar", v.get("structure") or "no structure"]
    if v.get("style_pack"):
        parts.append(v["style_pack"])
    return ", ".join(p for p in parts if p)


def hypotheses(ranked: list, week: str):
    """Returns (hypothesis lines, checklist lines). Every claim carries its numbers."""
    hyp, edits = [], []
    if len(ranked) < 2:
        hyp.append("Fewer than two videos with a day of data: no pattern is worth a claim yet. Next week: keep the "
                   "cadence and let the numbers accumulate.")
        edits.append("- [ ] no playbook edit this week: fewer than two videos with data")
        return hyp, edits
    overall = statistics.mean(v["vpd"] for v in ranked)
    for key, what, target in (("pillar", "pillar or series", PILLAR_FILE), ("structure", "structure", PILLAR_FILE),
                              ("style_pack", "style pack", PILLAR_FILE)):
        for name, (n, mean) in sorted(group_means(ranked, key).items(), key=lambda kv: -kv[1][1]):
            ratio = mean / overall if overall else 0
            if n >= 2 and ratio >= 1.5:
                hyp.append("%s `%s` averaged %s views/day over %d videos, %.1fx the week's average of %s. Next week: "
                           "schedule one more `%s` and keep what it did." % (what.capitalize(), name, fmt(mean), n, ratio,
                                                                            fmt(overall), name))
                if key == "pillar":
                    edits.append("- [ ] `%s`: add a rotation note that `%s` may run twice in one day for one week "
                                 "(evidence: %s views/day over %d videos in %s, %.1fx average)"
                                 % (target, name, fmt(mean), n, week, ratio))
                else:
                    edits.append("- [ ] `%s`: move %s `%s` to the front of the defaults for the pillars it ran under "
                                 "(evidence: %s views/day over %d videos in %s, %.1fx average)"
                                 % (target, what, name, fmt(mean), n, week, ratio))
            elif n >= 2 and ratio <= 0.5:
                hyp.append("%s `%s` averaged %s views/day over %d videos, %.1fx the week's average. Next week: change "
                           "the hook or the structure before scheduling `%s` again." % (what.capitalize(), name, fmt(mean),
                                                                                     n, ratio, name))
    shorts = [v for v in ranked if v["workspace"] == "shorts" and v.get("slot_hour") is not None]
    slots = group_means(shorts, "slot_hour")
    if len(slots) >= 2:
        (h1, (n1, m1)), (h2, (n2, m2)) = sorted(slots.items(), key=lambda kv: -kv[1][1])[:2]
        if n1 >= 2 and n2 >= 2 and m2 and m1 / m2 >= 1.3:
            hyp.append("Shorts in the %s:00 CT slot averaged %s views/day (%d videos) against %s in the %s:00 slot "
                       "(%d videos). Next week: put the stronger idea of the day in the %s:00 slot."
                       % (h1, fmt(m1), n1, fmt(m2), h2, n2, h1))
            edits.append("- [ ] `%s`: note that %s:00 CT beat %s:00 CT by %.1fx in %s (%d vs %d Shorts) and put the "
                         "stronger daily idea there" % (TIMING_FILE, h1, h2, m1 / m2, week, n1, n2))
    days = group_means([v for v in ranked if v["workspace"] == "long-form"], "slot")
    if len(days) >= 2:
        best = max(days.items(), key=lambda kv: kv[1][1])
        hyp.append("Long-form: the %s slot led with %s views/day; with %d episodes a week this is a weak signal. Next "
                   "week: keep the slots, revisit after four weeks." % (best[0], fmt(best[1][1]), len(days)))
    by_ws = group_means(ranked, "workspace")
    if len(by_ws) == 2:
        ns, nl = by_ws["shorts"][0], by_ws["long-form"][0]
        hyp.append("Shorts averaged %s views/day (%d video%s), long-form %s (%d episode%s). They are ranked separately "
                   "by YouTube; compare each against its own previous week, not against each other."
                   % (fmt(by_ws["shorts"][1]), ns, "" if ns == 1 else "s", fmt(by_ws["long-form"][1]), nl,
                      "" if nl == 1 else "s"))
    scored = [v for v in ranked if v.get("seo")]
    if len(scored) >= 4:
        cut = statistics.median(v["seo"] for v in scored)
        hi = [v["vpd"] for v in scored if v["seo"] >= cut]
        lo = [v["vpd"] for v in scored if v["seo"] < cut]
        if hi and lo and statistics.mean(lo) and statistics.mean(hi) / statistics.mean(lo) >= 1.3:
            hyp.append("Videos with seo_score >= %.0f averaged %s views/day against %s below it. Next week: treat %.0f "
                       "as the floor at the package stage." % (cut, fmt(statistics.mean(hi)), fmt(statistics.mean(lo)), cut))
            edits.append("- [ ] `%s`: raise the minimum score to %.0f (evidence: %.1fx views/day above the median score "
                         "in %s)" % (SEO_FILE, cut, statistics.mean(hi) / statistics.mean(lo), week))
    if not hyp:
        hyp.append("No group of two or more videos differed from the average by more than 1.5x. Next week: keep the "
                   "rotation and test one deliberate change (a new hook style on one Short).")
    if not edits:
        edits.append("- [ ] no playbook edit this week: no group differed by more than 1.5x (or 1.3x for slots)")
    return hyp, edits


# -- the note -------------------------------------------------------------------
def render(week: str, monday: dt.date, sunday: dt.date, current, previous, videos: list, not_shipped: list) -> str:
    shipped = [v for v in videos if v.get("local_date") and monday <= v["local_date"] <= sunday]
    ranked = sorted([v for v in shipped if v.get("vpd") is not None], key=lambda v: -v["vpd"])
    nodata = [v for v in shipped if v.get("vpd") is None]
    older = sorted([v for v in videos if v not in shipped and v.get("delta")], key=lambda v: -v["delta"])[:3]
    median = statistics.median(v["vpd"] for v in ranked) if ranked else 0
    cur_date = current[0].strftime("%Y-%m-%d") if current else "none"
    prev_date = previous[0].strftime("%Y-%m-%d") if previous else "none"
    L = ["# Retro %s" % week, "",
         "Week %s to %s (America/Chicago). Snapshots: %s (current) and %s (previous); delta = views gained between "
         "them. Views/day = views at the current snapshot divided by the video's age in days (at least 1)."
         % (monday.isoformat(), sunday.isoformat(), cur_date, prev_date), "",
         "## What shipped", ""]
    if shipped:
        L += ["| Slug | Workspace | Pillar | Structure | Style pack | Slot (CT) | Views | Views/day | Delta |",
              "|------|-----------|--------|-----------|------------|-----------|-------|-----------|-------|"]
        for v in sorted(shipped, key=lambda v: v.get("published_at") or dt.datetime.min.replace(tzinfo=dt.timezone.utc)):
            L.append("| `%s` | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                v["slug"], v["workspace"], v.get("pillar", ""), v.get("structure", ""), v.get("style_pack", ""),
                v.get("slot", ""), fmt(v.get("views")), fmt(v.get("vpd")), fmt(v.get("delta"))))
        L.append("")
    L.append("- %d shipped, %d with stats, %d without stats yet (published after the current snapshot)."
             % (len(shipped), len(ranked), len(nodata)))
    if older:
        L.append("- Catalog movers (older videos by delta): " + "; ".join(
            "`%s` +%s" % (v["slug"], fmt(v["delta"])) for v in older) + ".")
    L += ["", "## What worked", ""]
    if ranked:
        for i, v in enumerate(ranked[:3], 1):
            L.append("%d. `%s` (%s): %s views/day, %.1fx the week median%s" % (
                i, v["slug"], label(v), fmt(v["vpd"]), (v["vpd"] / median) if median else 0,
                (', "%s"' % v["title"]) if v.get("title") else ""))
    else:
        L.append("- nothing with stats yet")
    L += ["", "## What did not", ""]
    weak = [v for v in ranked if median and v["vpd"] < 0.5 * median] if len(ranked) >= 4 else []
    for v in weak:
        L.append("- `%s` (%s): %s views/day, %.1fx the median" % (v["slug"], label(v), fmt(v["vpd"]), v["vpd"] / median))
    for v in not_shipped:
        L.append("- did not ship: `%s` (%s) %s%s" % (v["slug"], v["workspace"], v["status"],
                                                     (": " + v["reason"]) if v["reason"] else ""))
    if not weak and not not_shipped:
        L.append("- nothing below half the median" + (" (fewer than four videos with stats)" if len(ranked) < 4 else ""))
    hyp, edits = hypotheses(ranked, week)
    L += ["", "## Hypotheses for next week", ""] + ["- " + h for h in hyp]
    L += ["", "## Proposed playbook edits", "",
          "One item per edit; the retro routine applies the convincing ones on a branch and opens a pull request."] + edits
    L += ["", "## Data", "",
          "- Public Data API numbers only (views, likes, comments). Retention, impressions CTR and search terms are "
          "not in these snapshots; see `skills/youtube-analytics/rules/analytics-api.md`.",
          "- Regenerate: `python3 skills/youtube-analytics/scripts/weekly_retro.py --week %s --out analytics/`" % week, ""]
    return "\n".join(L)


# -- fixture ------------------------------------------------------------------
def fixture():
    prev = (parse_time("2026-08-16T13:00:00Z"), {"rows": [
        {"videoId": "aaaaaaaaaa1", "views": 900}, {"videoId": "aaaaaaaaaa2", "views": 400}]}, "2026-08-16.json")
    rows = [
        ("aaaaaaaaaa1", "2026-08-10T16:00:00Z", 2600), ("aaaaaaaaaa2", "2026-08-12T23:00:00Z", 700),
        ("bbbbbbbbbb1", "2026-08-17T16:00:00Z", 4200), ("bbbbbbbbbb2", "2026-08-17T23:00:00Z", 900),
        ("bbbbbbbbbb3", "2026-08-18T16:00:00Z", 3100), ("bbbbbbbbbb4", "2026-08-18T23:00:00Z", 1300),
        ("bbbbbbbbbb5", "2026-08-19T16:00:00Z", 600), ("bbbbbbbbbb6", "2026-08-20T23:00:00Z", 2200),
        ("cccccccccc1", "2026-08-18T14:00:00Z", 6100),
    ]
    cur = (parse_time("2026-08-23T13:00:00Z"), {"rows": [
        {"videoId": i, "publishedAt": p, "views": v, "likes": v // 20, "comments": v // 100} for i, p, v in rows]},
        "2026-08-23.json")
    meta = {
        "aaaaaaaaaa1": ("2026-08-10-ollama-vs-llama-cpp", "shorts", "comparison", "comparison-ladder", "terminal", 82),
        "aaaaaaaaaa2": ("2026-08-12-kv-cache-bookshelf", "shorts", "explainer", "worked-example", "sketch", 70),
        "bbbbbbbbbb1": ("2026-08-17-deepseek-v4-flash-128gb", "shorts", "news-react", "number-first", "signal", 88),
        "bbbbbbbbbb2": ("2026-08-17-why-local-is-not-slow", "shorts", "myth-bust", "myth-bust", "halftone", 74),
        "bbbbbbbbbb3": ("2026-08-18-q4-vs-q8-one-decision", "shorts", "comparison", "number-first", "blueprint", 86),
        "bbbbbbbbbb4": ("2026-08-18-install-load-serve", "shorts", "how-to", "how-to-three-moves", "axon", 79),
        "bbbbbbbbbb5": ("2026-08-19-clinic-cannot-paste-data", "shorts", "enterprise-privacy", "story-first", "silicon", 68),
        "bbbbbbbbbb6": ("2026-08-20-moe-made-physical", "shorts", "explainer", "worked-example", "sketch", 84),
        "cccccccccc1": ("2026-08-18-spark-vs-5090-benchmarks", "long-form", "benchmarks", "", "", 90),
    }
    videos = [{"slug": s, "workspace": ws, "title": s[11:].replace("-", " "), "pillar": pil, "structure": st,
               "style_pack": sp, "seo_score": seo, "published_slot": "", "video_id": vid}
              for vid, (s, ws, pil, st, sp, seo) in meta.items()]
    not_shipped = [{"slug": "2026-08-21-fp8-on-gb10", "workspace": "shorts", "status": "blocked",
                    "reason": "06-voice: voice QA failed: WER 0.041"}]
    return cur, prev, videos, not_shipped


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--week", required=True, help="ISO week, for example 2026-W34")
    ap.add_argument("--out", default=str(REPO / "analytics"), help="directory for <year>-w<ww>.md (default analytics/)")
    ap.add_argument("--stats", default=str(REPO / "analytics" / "stats"), help="snapshot directory (default analytics/stats)")
    ap.add_argument("--stdout", action="store_true", help="print the note instead of writing it")
    ap.add_argument("--dry-run", action="store_true", help="fixture data, print to stdout, write nothing")
    a = ap.parse_args(argv)
    try:
        year, week, monday, sunday = parse_week(a.week)
    except ValueError as e:
        log("error: %s" % e)
        return 1
    week_id = "%d-W%02d" % (year, week)
    if a.dry_run:
        current, previous, videos, not_shipped = fixture()
    else:
        current, previous = pick_snapshots(load_snapshots(pathlib.Path(a.stats)))
        if current is None:
            log("error: no snapshot in %s (run yt_stats.py first)" % a.stats)
            return 1
        if previous is None:
            log("warning: only one snapshot; deltas will be n/a")
        videos = load_published()
        if not videos:
            log("error: no published/*.md notes in either workspace")
            return 1
        not_shipped = load_not_shipped(monday, sunday)
    enrich(videos, current, previous)
    note = render(week_id, monday, sunday, current, previous, videos, not_shipped)
    if a.dry_run or a.stdout:
        print(note)
        return 0
    path = pathlib.Path(a.out) / ("%d-w%02d.md" % (year, week))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(note + "\n", encoding="utf-8")
    log("wrote %s" % path)
    print(json.dumps({"week": week_id, "note": str(path), "videos": len(videos)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
