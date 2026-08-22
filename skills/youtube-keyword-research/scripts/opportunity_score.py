#!/usr/bin/env python3
"""Rank keyword candidates by opportunity. The formula lives in rules/opportunity-score.md.

    python3 opportunity_score.py --candidates FILE.json --out FILE.json
    python3 opportunity_score.py --dry-run [--out FILE.json]      # scores fixtures/candidates.json

Input: a JSON list of candidates
  {title, keyword, autocomplete{depth_score}, competition{median_views, median_subs,
   share_recent_180d, exact_title_rate, small_channel_velocity}, vidiq{volume, competition,
   overall}|null, trend_slope|null, named_product: bool}
Output: the same list sorted by rank, each candidate enriched with demand, competition_score,
opportunity (0-100), rank, bonuses{named_product, small_channel_velocity} and z{...} (the
component z-scores, null where the input was missing). No network is involved; --dry-run only
picks the fixture when --candidates is absent. Exit 1 on unreadable input.
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import statistics
import sys

import kwlib as kw

SOURCE = "opportunity"
BASE = 50.0
SPREAD = 15.0
NAMED_PRODUCT_BONUS = 10.0
VELOCITY_BONUS = 5.0


def number(value) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def field(candidate: dict, group: str, key: str) -> float | None:
    holder = candidate.get(group)
    return number(holder.get(key)) if isinstance(holder, dict) else None


DEMAND = [("depth_score", lambda c: field(c, "autocomplete", "depth_score"), False),
          ("vidiq_volume", lambda c: field(c, "vidiq", "volume"), True),
          ("trend_slope", lambda c: number(c.get("trend_slope")), False)]
COMPETITION = [("median_views", lambda c: field(c, "competition", "median_views"), True),
               ("median_subs", lambda c: field(c, "competition", "median_subs"), True),
               ("share_recent_180d", lambda c: field(c, "competition", "share_recent_180d"), False),
               ("exact_title_rate", lambda c: field(c, "competition", "exact_title_rate"), False)]


def zscores(values: list) -> list:
    """Population z-scores over the present values; None stays None; a flat column is all zeros."""
    present = [v for v in values if v is not None]
    if len(present) < 2:
        return [0.0 if v is not None else None for v in values]
    mean, sd = statistics.fmean(present), statistics.pstdev(present)
    if sd < 1e-12:
        return [0.0 if v is not None else None for v in values]
    return [round((v - mean) / sd, 4) if v is not None else None for v in values]


def column(candidates: list, getter, log_scale: bool) -> list:
    values = [getter(c) for c in candidates]
    if log_scale:
        values = [math.log10(1 + max(0.0, v)) if v is not None else None for v in values]
    return zscores(values)


def mean_present(values: list) -> float:
    present = [v for v in values if v is not None]
    return round(statistics.fmean(present), 4) if present else 0.0


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def score(candidates: list) -> list:
    demand_cols = {name: column(candidates, getter, log_scale) for name, getter, log_scale in DEMAND}
    comp_cols = {name: column(candidates, getter, log_scale) for name, getter, log_scale in COMPETITION}
    velocities = [field(c, "competition", "small_channel_velocity") for c in candidates]
    present = [v for v in velocities if v is not None]
    velocity_median = statistics.median(present) if present else None
    for index, candidate in enumerate(candidates):
        demand = mean_present([demand_cols[name][index] for name in demand_cols])
        competition = mean_present([comp_cols[name][index] for name in comp_cols])
        base = clamp(BASE + SPREAD * (demand - competition))
        named = NAMED_PRODUCT_BONUS if candidate.get("named_product") else 0.0
        fast_small = (velocity_median is not None and velocities[index] is not None
                      and velocities[index] > velocity_median)
        velocity = VELOCITY_BONUS if fast_small else 0.0
        candidate["demand"] = demand
        candidate["competition_score"] = competition
        candidate["opportunity"] = round(clamp(base + named + velocity), 1)
        candidate["bonuses"] = {"named_product": named, "small_channel_velocity": velocity}
        candidate["z"] = {name: demand_cols[name][index] for name in demand_cols}
        candidate["z"].update({name: comp_cols[name][index] for name in comp_cols})
    candidates.sort(key=lambda c: (-c["opportunity"], -c["demand"], str(c.get("keyword") or "")))
    for rank, candidate in enumerate(candidates, 1):
        candidate["rank"] = rank
    return candidates


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--candidates", help="JSON list of candidates (default with --dry-run: fixtures/candidates.json)")
    ap.add_argument("--out", help="write the ranked list here instead of stdout")
    ap.add_argument("--dry-run", action="store_true", help="score the fixture when --candidates is absent")
    args = ap.parse_args(argv)
    if not args.candidates and not args.dry_run:
        kw.log(SOURCE, "error: --candidates FILE.json is required (or --dry-run)")
        return 1
    path = pathlib.Path(args.candidates) if args.candidates else kw.FIXTURES_DIR / "candidates.json"
    try:
        candidates = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as err:
        kw.log(SOURCE, "error: cannot read %s: %s" % (path, err))
        return 1
    if not isinstance(candidates, list) or not all(isinstance(c, dict) and c.get("keyword") for c in candidates):
        kw.log(SOURCE, "error: input must be a list of objects that each carry a keyword")
        return 1
    ranked = score(candidates)
    kw.emit(ranked, args.out)
    for c in ranked:
        kw.log(SOURCE, "#%d %5.1f demand %+.2f competition %+.2f  %s" % (
            c["rank"], c["opportunity"], c["demand"], c["competition_score"], c["keyword"]))
    kw.log(SOURCE, "%d candidate(s) ranked from %s" % (len(ranked), path.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
