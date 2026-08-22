#!/usr/bin/env python3
"""Create milestones, labels and issues on GitHub from _design/github-issues.md using the gh CLI.

    gh auth login   # with the account that owns the repo
    python3 tools/create-issues.py [--repo Hamza-Saraswat/BLAI_Full_Pipeline] [--dry-run]

Items marked [x] are created and then closed with a comment. Re-running skips titles that already exist.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LABELS = {"foundations": "0e8a16", "shorts": "1d76db", "long-form": "5319e7", "spark": "d93f0b",
          "skill": "fbca04", "needs-human": "b60205"}


def gh(*args, dry=False, input_json=None):
    cmd = ["gh"] + list(args)
    if dry:
        print("DRY:", " ".join(cmd)); return ""
    res = subprocess.run(cmd, capture_output=True, text=True, input=input_json)
    if res.returncode != 0:
        print(res.stderr.strip(), file=sys.stderr)
        raise SystemExit("gh failed: %s" % " ".join(cmd[:4]))
    return res.stdout


def parse(md):
    milestones, current = [], None
    for line in md.splitlines():
        m = re.match(r"^## Milestone: (.+)$", line)
        if m:
            current = {"title": m.group(1).strip(), "issues": []}; milestones.append(current); continue
        m = re.match(r"^- \[( |x)\] (.+?)\s*\|\s*labels:\s*(.*)$", line)
        if m and current is not None:
            current["issues"].append({"done": m.group(1) == "x", "title": m.group(2).strip(),
                                      "labels": [l.strip() for l in m.group(3).split(",") if l.strip()], "body": ""})
            continue
        if line.startswith("  ") and current and current["issues"]:
            current["issues"][-1]["body"] += line.strip() + "\n"
    return milestones


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="Hamza-Saraswat/BLAI_Full_Pipeline")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    repo, dry = a.repo, a.dry_run
    plan = parse((ROOT / "_design" / "github-issues.md").read_text(encoding="utf-8"))

    for name, color in LABELS.items():
        gh("label", "create", name, "--color", color, "-R", repo, "--force", dry=dry)
    existing_ms = {} if dry else {m["title"]: m["number"] for m in json.loads(gh("api", "repos/%s/milestones?state=all&per_page=100" % repo))}
    existing_issues = set() if dry else {i["title"] for i in json.loads(gh("issue", "list", "-R", repo, "--state", "all", "--limit", "200", "--json", "title"))}

    for ms in plan:
        if ms["title"] not in existing_ms:
            out = gh("api", "-X", "POST", "repos/%s/milestones" % repo, "-f", "title=%s" % ms["title"], dry=dry)
            existing_ms[ms["title"]] = json.loads(out)["number"] if out else 0
        for it in ms["issues"]:
            if it["title"] in existing_issues:
                print("skip (exists):", it["title"]); continue
            args = ["issue", "create", "-R", repo, "--title", it["title"], "--body", it["body"] or it["title"],
                    "--milestone", ms["title"]]
            for l in it["labels"]:
                args += ["--label", l]
            url = gh(*args, dry=dry).strip()
            print("created:", it["title"], url)
            if it["done"] and url:
                gh("issue", "close", url, "-R", repo, "--comment", "Done in the initial build (2026-08-22).", dry=dry)


if __name__ == "__main__":
    main()
