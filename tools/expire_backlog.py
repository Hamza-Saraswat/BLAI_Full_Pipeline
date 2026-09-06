#!/usr/bin/env python3
"""Retire every hub note that is not from today's picks: the factory carries no backlog.

    python3 tools/expire_backlog.py [--date YYYY-MM-DD] [--workspace shorts] [--dry-run]

Operator policy (2026-09-06): each morning starts from that day's radar -> ideas -> picks and
goes through the whole pipeline fresh. A note dated before --date (default: today, local time)
that is still in flight (idea, researched, scripted, ready-to-build, building, review, blocked,
rejected) becomes `status: expired` with a journal line. Notes already handed to YouTube
(approved, scheduled, published) and notes already expired are left alone. --slug work by a
human still rebuilds anything (build.py --slug). Prints one JSON line {expired: [...], kept: N}.
Stdlib only; the workspace's own hubnote.py does the writes.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(REPO / "tools"))
import hubnote  # noqa: E402

IN_FLIGHT = {"idea", "researched", "scripted", "ready-to-build", "building", "review", "blocked", "rejected"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=dt.datetime.now().astimezone().strftime("%Y-%m-%d"))
    ap.add_argument("--workspace", default="shorts")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    ws = REPO / "workspaces" / a.workspace
    expired, kept = [], 0
    for p in hubnote.find(ws):
        meta, _ = hubnote.read(p)
        slug = str(meta.get("slug", ""))
        if slug[:10] >= a.date or meta.get("status") not in IN_FLIGHT:
            kept += 1
            continue
        expired.append("%s (%s)" % (slug, meta.get("status")))
        if not a.dry_run:
            hubnote.update(p, status="expired", blocked_reason="")
            hubnote.append_section(p, "Build journal", "%s expired: not from today's picks (%s); the factory carries no backlog"
                                   % (dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), a.date))
    print(json.dumps({"date": a.date, "expired": expired, "kept": kept, "dry_run": a.dry_run}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
