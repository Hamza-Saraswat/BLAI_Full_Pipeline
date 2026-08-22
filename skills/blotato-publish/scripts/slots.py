#!/usr/bin/env python3
"""Print the next publish slot per shared/playbook/publish-timing.md.

Usage:
  slots.py --format short|long --after ISO [--tz America/Chicago] [--lead-min 30] [--taken ISO,ISO] [--json]

Rules (audience timezone, default America/Chicago):
  short : 11:00 and 18:00 local every day; the next one at or after --after plus the lead.
  long  : 09:00 local Monday to Friday, 10:00 on Sunday, nothing on Saturday; so an approval on
          Saturday (or late Friday) lands on Sunday 10:00.
The lead (default 30 min) is the time Blotato needs to fetch and process the media. --taken lists
slots already scheduled (ISO-8601); those are skipped so two Shorts approved the same day take the two
slots in order and a third rolls to the next day. Output: one ISO-8601 timestamp with offset.
Importable: next_slot(fmt, after_dt, tz_name, lead_min, taken). No network. Exit 0/1.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from zoneinfo import ZoneInfo

DEFAULT_TZ = "America/Chicago"
DEFAULT_LEAD_MIN = 30
SHORT_TIMES = [(11, 0), (18, 0)]
LONG_WEEKDAY_TIME = (9, 0)
LONG_SUNDAY_TIME = (10, 0)
SEARCH_DAYS = 60


def log(msg: str) -> None:
    sys.stderr.write("[slots] %s\n" % msg)
    sys.stderr.flush()


def parse_iso(value: str, tz_name: str = DEFAULT_TZ) -> dt.datetime:
    s = value.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        t = dt.datetime.fromisoformat(s)
    except ValueError:
        raise SystemExit("not an ISO-8601 timestamp: %s" % value)
    if t.tzinfo is None:
        t = t.replace(tzinfo=ZoneInfo(tz_name))
    return t


def candidates(fmt: str, day: dt.date, tz) -> list:
    if fmt == "short":
        times = SHORT_TIMES
    else:
        wd = day.weekday()  # Monday = 0, Sunday = 6
        if wd == 5:
            times = []
        elif wd == 6:
            times = [LONG_SUNDAY_TIME]
        else:
            times = [LONG_WEEKDAY_TIME]
    return [dt.datetime.combine(day, dt.time(h, m), tzinfo=tz) for h, m in times]


def next_slot(fmt: str, after: dt.datetime, tz_name: str = DEFAULT_TZ, lead_min: int = DEFAULT_LEAD_MIN,
              taken=()) -> dt.datetime:
    if fmt not in ("short", "long"):
        raise SystemExit("format must be short or long")
    tz = ZoneInfo(tz_name)
    earliest = after.astimezone(tz) + dt.timedelta(minutes=lead_min)
    busy = {t.astimezone(dt.timezone.utc).replace(microsecond=0) for t in taken}
    day = earliest.date()
    for d in range(SEARCH_DAYS):
        for cand in candidates(fmt, day + dt.timedelta(days=d), tz):
            if cand >= earliest and cand.astimezone(dt.timezone.utc) not in busy:
                return cand
    raise SystemExit("no free slot within %d days" % SEARCH_DAYS)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--format", required=True, choices=["short", "long"])
    ap.add_argument("--after", required=True, help="ISO-8601 approval time (offset or Z; naive = --tz)")
    ap.add_argument("--tz", default=DEFAULT_TZ)
    ap.add_argument("--lead-min", type=int, default=DEFAULT_LEAD_MIN)
    ap.add_argument("--taken", default="", help="comma-separated ISO-8601 slots already scheduled")
    ap.add_argument("--json", action="store_true", help="print {slot, local, format, after, lead_min}")
    args = ap.parse_args()
    after = parse_iso(args.after, args.tz)
    taken = [parse_iso(t, args.tz) for t in args.taken.split(",") if t.strip()]
    slot = next_slot(args.format, after, args.tz, args.lead_min, taken)
    if args.json:
        print(json.dumps({"slot": slot.isoformat(), "local": slot.strftime("%A %Y-%m-%d %H:%M %Z"),
                          "format": args.format, "after": after.isoformat(), "lead_min": args.lead_min}))
    else:
        print(slot.isoformat())
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
