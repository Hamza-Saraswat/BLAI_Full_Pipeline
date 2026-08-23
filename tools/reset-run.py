#!/usr/bin/env python3
"""Remove every trace of one test run so the next run cannot inherit half of it.

    python3 tools/reset-run.py --slug 2026-08-23-some-topic [--workspace shorts] [--dry-run]
    python3 tools/reset-run.py --date 2026-08-23 --workspace shorts     # radar/ideas artifacts too

Removes: the hub note, every stage output whose filename carries the slug, the slug's entry in
script-ledger.json / episode-ledger.json / styles/history.json, the published note if one exists,
and the build folder under .local-builds/. Prints what it did; --dry-run prints without touching.
"""
import argparse
import json
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGERS = [
    ROOT / "workspaces/shorts/stages/04-script/output/script-ledger.json",
    ROOT / "workspaces/long-form/stages/02-ideas/output/episode-ledger.json",
    ROOT / "skills/render-shorts/styles/history.json",
]


def rm(path: pathlib.Path, dry: bool, log: list) -> None:
    if not path.exists():
        return
    log.append(("would remove" if dry else "removed") + " " + str(path.relative_to(ROOT)))
    if dry:
        return
    shutil.rmtree(path) if path.is_dir() else path.unlink()


def prune_ledger(path: pathlib.Path, slug: str, dry: bool, log: list) -> None:
    if not path.exists():
        return
    try:
        data = json.loads(path.read_text() or "[]")
    except json.JSONDecodeError:
        log.append("skipped unreadable ledger " + str(path.relative_to(ROOT)))
        return
    if not isinstance(data, list):
        return
    kept = [e for e in data if not (isinstance(e, dict) and e.get("slug") == slug)]
    if len(kept) == len(data):
        return
    log.append(("would drop" if dry else "dropped") + " %d entry(s) from %s"
               % (len(data) - len(kept), path.relative_to(ROOT)))
    if not dry:
        path.write_text(json.dumps(kept, indent=2) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--date", help="also remove date-keyed radar and ideas artifacts")
    ap.add_argument("--workspace", choices=["shorts", "long-form", "both"], default="both")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not a.slug and not a.date:
        return ap.error("give --slug, --date, or both")
    spaces = ["shorts", "long-form"] if a.workspace == "both" else [a.workspace]
    log: list = []

    for ws in spaces:
        wsdir = ROOT / "workspaces" / ws
        if a.slug:
            rm(wsdir / "videos" / (a.slug + ".md"), a.dry_run, log)
            rm(wsdir / "published" / (a.slug + ".md"), a.dry_run, log)
            for f in sorted(wsdir.glob("stages/*/output/*")):
                if f.name.startswith(a.slug) and f.name != ".gitkeep":
                    rm(f, a.dry_run, log)
        if a.date:
            for f in sorted(wsdir.glob("stages/*/output/*")):
                if f.name.startswith(a.date) and f.name != ".gitkeep":
                    rm(f, a.dry_run, log)
    if a.slug:
        for led in LEDGERS:
            prune_ledger(led, a.slug, a.dry_run, log)
        rm(ROOT / ".local-builds" / a.slug, a.dry_run, log)

    print("\n".join(log) if log else "nothing to remove")
    return 0


if __name__ == "__main__":
    sys.exit(main())
