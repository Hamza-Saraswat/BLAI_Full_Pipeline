#!/usr/bin/env python3
"""Create a hub note for a new video run from shared/hub-note-template.md.

    python3 tools/new-run.py --workspace shorts --slug 2026-08-25-deepseek-v4-flash-128gb \
        --title "Can DeepSeek V4 Flash run on 128 GB?" --pillar news-react --structure number-first \
        --format smooth-explainer --value-types "TEACHES,PROVES" [--date 2026-08-25]

Prints the path of the created note. Refuses to overwrite an existing note.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import hubnote  # noqa: E402

STAGES = {
    "shorts": ["01-radar", "02-ideas", "03-research", "04-script", "05-package", "06-voice", "07-render", "08-publish"],
    "long-form": ["01-radar", "02-ideas", "03-research", "04-outline", "05-script", "06-spec", "07-package", "08-capture", "09-voice", "10-render", "11-publish"],
}


def slugify(text: str, limit: int = 30) -> str:
    """Topic part of the slug. 30 chars keeps the full slug (date + topic) inside the 41-char
    limit that shared/schemas/storyboard.schema.json and the validator enforce."""
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:limit].rstrip("-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True, choices=list(STAGES))
    ap.add_argument("--slug", help="full slug YYYY-MM-DD-topic; derived from --title and --date when omitted")
    ap.add_argument("--title", default="")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    for f in ("pillar", "series", "structure", "format", "style_pack", "value_types"):
        ap.add_argument("--" + f.replace("_", "-"), dest=f, default="")
    a = ap.parse_args()

    slug = a.slug or "%s-%s" % (a.date, slugify(a.title))
    if not re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(-[a-z0-9]+)*$", slug):
        sys.exit("bad slug: %s" % slug)
    if len(slug) > 41:
        sys.exit("slug too long (%d > 41): %s" % (len(slug), slug))
    ws = ROOT / "workspaces" / a.workspace
    path = ws / "videos" / (slug + ".md")
    if path.exists():
        sys.exit("exists: %s" % path)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "slug": slug, "workspace": a.workspace, "title": a.title, "status": "idea",
        "pillar": a.pillar, "series": a.series, "structure": a.structure, "format": a.format,
        "style_pack": a.style_pack, "value_types": a.value_types, "created": a.date, "updated": now,
        "publish_slot": "", "seo_score": 0, "feedback": "", "blocked_reason": "", "build_host": "",
        "preview_url": "", "youtube_url": "", "blotato_post_id": "",
    }
    date = slug[:10]
    lines = ["# %s" % (a.title or slug), "", "## Artifacts"]
    for st in STAGES[a.workspace]:
        name = st[3:]
        if name in ("radar", "ideas"):
            lines.append("- %s: [[stages/%s/output/%s-%s]]" % (name.capitalize(), st, date, name))
        else:
            lines.append("- %s: (filled by stage %s)" % (name.capitalize(), st[:2]))
    lines += ["", "## Decisions", "", "## Build journal", ""]
    hubnote.write(path, meta, "\n".join(lines) + "\n")
    print(path)


if __name__ == "__main__":
    main()
