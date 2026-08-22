# Sources

Six scripts, one JSON list each, merged by `scripts/radar.py`. Every script takes
`--hours N --limit N [--out FILE] [--dry-run]`, logs to stderr, prints data to stdout, and exits 1
only when every request of a run failed. A missing key is a skip with a stderr note, never an error.

## What each source is for

| Source | Script | Key | Window | What it answers |
|--------|--------|-----|--------|-----------------|
| Reddit | `reddit.py` | optional `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` (OAuth); `REDDIT_USER_AGENT` (default `blai-radar/1.0`) | `--hours` exactly, from the `top` listing of the matching period | What home users are running, measuring and complaining about right now |
| Hacker News | `hn.py` | none (Algolia) | `--hours` exactly (`created_at_i` filter) | Which releases and write-ups the wider developer crowd rates |
| Hugging Face | `hf_trending.py` | none | models created in the last `max(--hours, 336)` h (two weeks) | Which new models people are pulling; non-text pipelines feed the `beyond-llms` series |
| GitHub releases | `github_releases.py` | optional `GITHUB_TOKEN` (raises the limit from 60 to 5,000 req/h) | releases published in the last `max(--hours, 168)` h | What the runtimes shipped, with the release notes that name the break or the speedup |
| YouTube | `youtube_recent.py` | `YT_API_KEY`, skipped without it | 7 days, fixed, ordered by views | What the audience already watches on the topic and how fast it is moving (views per hour) |
| FireCrawl | `firecrawl_search.py` | `FIRECRAWL_API_KEY`, skipped without it | past week (`tbs=qdr:w`) | Vendor news, firmware, pricing and regulation that never reach Reddit or HN in time |

## Lists the scripts read at run time

Each script reads the fenced block named below when it starts and falls back to the same
default list compiled into the script when this file is missing. One entry per line, lines
starting with `#` are ignored. Keep each list short: every entry is a request.

```reddit-subreddits
LocalLLaMA
ollama
LocalLLM
```

```hn-queries
local llm
llama.cpp
ollama
vllm
DGX Spark
quantization
open weights
Qwen
DeepSeek
Mistral
Unsloth
```

```github-repos
ggml-org/llama.cpp
vllm-project/vllm
ollama/ollama
unslothai/unsloth
sgl-project/sglang
NVIDIA/TensorRT-LLM
huggingface/transformers
exo-explore/exo
mlc-ai/mlc-llm
ggml-org/whisper.cpp
open-webui/open-webui
NVIDIA/dgx-spark-playbooks
```

```youtube-queries
local ai
dgx spark
ollama
llama.cpp
run llm locally
local llm
```

```firecrawl-queries
DGX Spark
local LLM news
NVIDIA DGX Spark firmware update
open weights model release
run LLM locally
```

Notes on the lists: the Hugging Face script has no query list; it filters the trending and
most-downloaded lists to the pipeline tags `text-generation`, `image-text-to-text` (the current
tag for vision-language models such as the Qwen VL line), `image-to-text`, `text-to-speech`,
`automatic-speech-recognition`, `text-to-image` and `text-to-video`. `NVIDIA/dgx-spark-playbooks`
publishes few formal releases; an empty answer is normal. `site:x.com` style queries are not
reliable on FireCrawl search, so the list stays with plain news phrasing.

## Rate limits and budgets per run

| Source | Calls per run | Limit that matters |
|--------|---------------|--------------------|
| Reddit public JSON | 3 | about 10 req/min per user agent; blocked user agents get 403 or 429, so keep `REDDIT_USER_AGENT` descriptive |
| Reddit OAuth | 1 token + 3 | 100 req/min per app; the token lasts an hour and is fetched fresh each run |
| HN Algolia | 11, 0.2 s apart | 10,000 req/h unauthenticated |
| Hugging Face | 2 | generous; no key |
| GitHub | 12, 0.2 s apart | 60 req/h anonymous (one run uses 12), 5,000 with `GITHUB_TOKEN` |
| YouTube Data API | 6 searches (100 units each) + 1 to 3 `videos.list` (1 unit each) | 10,000 units/day shared with `youtube-keyword-research`; this source takes about 600 |
| FireCrawl | 5 searches, 10 scraped results each | credits per scraped result; about 50 per run, so keep the list at 5 queries |

All HTTP calls retry 429 and 5xx twice with backoff (1.5 s, 3 s) and time out at 20 s
(60 s for FireCrawl, which scrapes pages).

## When a source fails

- Missing key: the script raises a skip; `radar.py` notes `<source> skipped: <reason>` on stderr
  and in the digest's Sources line. Never add a fake item for a skipped source.
- One query, subreddit or repo fails: logged, the rest continue. Only when every request of a
  run fails does the script exit 1 (standalone) or count as `error` (inside `radar.py`).
- Every source fails or is skipped: `radar.py` exits 1 and writes nothing. The ideas stage then
  says so in the ideas note instead of inventing a radar.
- Reddit 403 on the public endpoint: set `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET`
  (a "script" app at reddit.com/prefs/apps) to switch to OAuth. During the build (2026-08-22)
  the public endpoint answered 403 to every user agent tried, including a browser one, so treat
  the OAuth pair as required in practice; the public path is a fallback, not a plan.
- YouTube `quotaExceeded`: the daily 10,000 units are gone; the source is treated as an error
  and the radar runs without it. Do not retry until the next Pacific-time midnight.
- GitHub 403 with `rate limit`: anonymous budget spent; set `GITHUB_TOKEN` or wait an hour.

## Fixtures

`fixtures/<script>.json` holds a raw API-shaped response per source (listing, hits, model list,
releases per repo, search plus videos, results per query). `--dry-run` runs the real parser over
the fixture with the clock pinned to 2026-08-25T12:00Z, so window filters, duplicate handling
(the same URL in several sources) and the dedupe fixture workspace are all exercised offline.
Fixtures are synthetic: plausible titles and numbers, not real posts.
