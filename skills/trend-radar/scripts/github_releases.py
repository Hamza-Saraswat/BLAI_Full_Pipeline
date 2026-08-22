#!/usr/bin/env python3
"""GitHub releases source for the trend radar: latest releases of the core local-AI runtimes.

    python3 github_releases.py --hours 48 --limit 3 [--out FILE] [--dry-run]

GET https://api.github.com/repos/<owner>/<repo>/releases?per_page=N for every repo in
rules/sources.md (block ```github-repos). GITHUB_TOKEN is sent as a bearer header when set
(raises the limit from 60 to 5,000 requests per hour); without it the call is anonymous, never
skipped. Releases published inside the last max(--hours, 168) hours are kept: a release stays
news for a week and the radar's recency decay handles the rest.

Output: JSON list with repo, tag, name, title, published_at, body (500 chars), html_url, url,
prerelease.
"""
from __future__ import annotations

import datetime as dt
import sys
import time

import radarlib as rl

SOURCE = "github"
DEFAULT_LIMIT = 3
DEFAULT_REPOS = ["ggml-org/llama.cpp", "vllm-project/vllm", "ollama/ollama", "unslothai/unsloth",
                 "sgl-project/sglang", "NVIDIA/TensorRT-LLM", "huggingface/transformers",
                 "exo-explore/exo", "mlc-ai/mlc-llm", "ggml-org/whisper.cpp",
                 "open-webui/open-webui", "NVIDIA/dgx-spark-playbooks"]


def parse_releases(repo: str, releases: list, now, window_hours: int) -> list[dict]:
    cutoff = now - dt.timedelta(hours=window_hours)
    items = []
    for rel in releases or []:
        if rel.get("draft"):
            continue
        published = rl.parse_time(rel.get("published_at") or rel.get("created_at"))
        if published and published < cutoff:
            continue
        tag = str(rel.get("tag_name") or "")
        name = rl.clip(rel.get("name") or tag, 200)
        short = repo.split("/")[-1]
        title = "%s %s" % (short, tag)
        if name and name != tag and name.lower() != title.lower():
            title += ": " + name
        items.append({
            "source": SOURCE,
            "repo": repo,
            "tag": tag,
            "name": name,
            "title": rl.clip(title, 300),
            "published_at": rl.iso(published),
            "body": rl.clip(rel.get("body"), 500),
            "html_url": rel.get("html_url"),
            "url": rel.get("html_url"),
            "prerelease": bool(rel.get("prerelease")),
        })
    return items


def collect(hours: int = 48, limit: int = DEFAULT_LIMIT, dry_run: bool = False) -> list[dict]:
    now = rl.now_for(dry_run)
    window = max(hours, 168)
    repos = rl.rule_list("github-repos", DEFAULT_REPOS)
    if dry_run:
        fixture = rl.fixture("github_releases.json")
        items = []
        for repo in repos:
            items += parse_releases(repo, (fixture.get(repo) or [])[:limit], now, window)
        return items
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    token = rl.env("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    rl.log(SOURCE, "auth: %s" % ("token" if token else "anonymous (60 req/h)"))
    items, failures = [], 0
    for index, repo in enumerate(repos):
        url = "https://api.github.com/repos/%s/releases?per_page=%d" % (repo, limit)
        try:
            data = rl.get_json(url, headers=headers, source=SOURCE)
            if not isinstance(data, list):
                raise RuntimeError("unexpected response shape")
            items += parse_releases(repo, data, now, window)
        except RuntimeError as err:
            failures += 1
            rl.log(SOURCE, "%s failed: %s" % (repo, err))
        if index < len(repos) - 1:
            time.sleep(0.2)
    if repos and failures == len(repos):
        raise RuntimeError("every repo failed")
    return items


if __name__ == "__main__":
    sys.exit(rl.run_source(SOURCE, collect, __doc__, DEFAULT_LIMIT))
