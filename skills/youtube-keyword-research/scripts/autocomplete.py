#!/usr/bin/env python3
"""YouTube autocomplete fan-out: how deep the suggestion tree is for a seed keyword.

    python3 autocomplete.py "dgx spark" [--hl en] [--gl US] [--out FILE] [--dry-run]

32 GET calls to suggestqueries.google.com (client=firefox, ds=yt, JSON answer
[query, [suggestions]]): the seed, the seed plus " a" to " z", "how to " + seed,
seed + " <this year>", seed + " vs", seed + " review", "best " + seed, 0.25 s apart. No key, no
quota; the endpoint is undocumented, so a failed call is logged and counts as an empty expansion,
and the run exits 1 only when every call failed.

Output: {seed, hl, gl, suggestions (unique, in order of discovery), expansions {query: [...]},
depth_score (number of unique suggestions across all expansions), calls, failed, fetched_at}.
--dry-run fills the expansions from fixtures/autocomplete.json, a template keyed by "{seed}".
"""
from __future__ import annotations

import argparse
import datetime as dt
import string
import sys
import time
import urllib.parse

import kwlib as kw

SOURCE = "autocomplete"
ENDPOINT = "https://suggestqueries.google.com/complete/search"
PAUSE_S = 0.25


def expansions(seed: str, year: int) -> list[str]:
    seed = seed.strip()
    return ([seed] + ["%s %s" % (seed, letter) for letter in string.ascii_lowercase]
            + ["how to " + seed, "%s %d" % (seed, year), seed + " vs", seed + " review", "best " + seed])


def parse_suggestions(payload) -> list[str]:
    """[query, [suggestions]] where a suggestion may be a string or a [string, ...] pair."""
    if not isinstance(payload, list) or len(payload) < 2 or not isinstance(payload[1], list):
        raise RuntimeError("unexpected autocomplete payload shape")
    out = []
    for entry in payload[1]:
        if isinstance(entry, list) and entry:
            entry = entry[0]
        if isinstance(entry, str) and entry.strip():
            out.append(entry.strip())
    return out


def fetch(query: str, hl: str, gl: str) -> list[str]:
    params = urllib.parse.urlencode({"client": "firefox", "ds": "yt", "hl": hl, "gl": gl, "q": query})
    return parse_suggestions(kw.get_json(ENDPOINT + "?" + params, source=SOURCE))


def collect(seed: str, hl: str, gl: str, dry_run: bool) -> dict:
    now = kw.now_for(dry_run)
    queries = expansions(seed, now.year)
    template = kw.fixture("autocomplete.json") if dry_run else None
    result, unique, failed = {}, [], 0
    for index, query in enumerate(queries):
        if dry_run:
            key = query.replace(seed.strip(), "{seed}", 1).replace(str(now.year), "{year}")
            suggestions = [s.replace("{seed}", seed.strip()).replace("{year}", str(now.year))
                           for s in template.get(key, [])]
        else:
            try:
                suggestions = fetch(query, hl, gl)
            except RuntimeError as err:
                failed += 1
                kw.log(SOURCE, "%r failed: %s" % (query, err))
                suggestions = []
            if index < len(queries) - 1:
                time.sleep(PAUSE_S)
        result[query] = suggestions
        for item in suggestions:
            if item not in unique:
                unique.append(item)
    if not dry_run and failed == len(queries):
        raise RuntimeError("every autocomplete call failed")
    return {"seed": seed.strip(), "hl": hl, "gl": gl, "suggestions": unique, "expansions": result,
            "depth_score": len(unique), "calls": len(queries), "failed": failed, "fetched_at": kw.iso(now)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seed", help="keyword to expand, for example \"dgx spark\"")
    ap.add_argument("--hl", default="en", help="interface language (default en)")
    ap.add_argument("--gl", default="US", help="country code (default US)")
    ap.add_argument("--out", help="write the JSON here instead of stdout")
    ap.add_argument("--dry-run", action="store_true", help="fixture template, no network")
    args = ap.parse_args(argv)
    if not args.seed.strip():
        kw.log(SOURCE, "error: empty seed")
        return 1
    kw.load_env()
    try:
        data = collect(args.seed, args.hl, args.gl, args.dry_run)
    except Exception as err:
        kw.log(SOURCE, "error: %s" % err)
        return 1
    kw.emit(data, args.out)
    kw.log(SOURCE, "%r: depth_score %d from %d calls%s" % (
        data["seed"], data["depth_score"], data["calls"], " (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
