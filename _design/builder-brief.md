# Builder Brief (read before writing any skill, script or contract)

This file is the contract between the people and agents building the repo. Every path, CLI flag and output name below is fixed; stage contracts and the build agent depend on them.

## Repo facts

- Root: the repo is cloned inside an Obsidian vault. Every `.md` is a note; write Obsidian-friendly markdown (wikilinks allowed in outputs, never in Layer 3 reference files).
- Conventions: ICM (`research/ICM-BUILD-GUIDE.md` section 4). Lowercase-with-hyphens names, no spaces, no em dashes in any file we author (write `--` or a comma), `CONTEXT.md` under 80 lines, reference files under 200 lines, `.gitkeep` in empty folders. Vendored third-party content is exempt from style rules.
- Hosts: cloud routines run the thinking stages (Ubuntu 24.04, Python 3.12, Node 22, ffmpeg, Playwright Chromium, network allowlisted). The DGX Spark (Ubuntu, aarch64, Python 3.12, CUDA GB10, Node 22 installed by `build/install.sh`) runs voice, capture, render and publish.
- Secrets only via environment variables (cloud) or `build/.env` (Spark). Scripts load `.env` if `python-dotenv` is present, else they read `os.environ`. Never print a secret.
- Python: stdlib first; third-party imports guarded with a clear `pip install ...` message; every script has `--help`, `--dry-run` (no network, no paid call, deterministic fixture output), returns exit code 0 on success and 1 on failure, logs to stderr, data to stdout or to `--out`.
- Hub notes: `workspaces/<ws>/videos/<slug>.md`, flat frontmatter, helpers in `tools/hubnote.py` (`read`, `update`, `append_section`, `find`). Status values and who sets them: `shared/pipeline-overview.md`.
- Slug: `YYYY-MM-DD-topic-slug`. Artifacts: `workspaces/<ws>/stages/NN-name/output/<slug>-<type>.md` (date-based artifacts use `<date>-<type>.md`).
- Skill shape: `skills/<name>/SKILL.md` with frontmatter `name`, `description`, `metadata: {tags: "a, b"}` then When to Use, What You Need Before Calling, How It Works (numbered), Rules (one line per rule file), After the Call. Rule files in `rules/`, scripts in `scripts/`.

## Skill layouts and CLI contracts

### skills/trend-radar
- `scripts/radar.py --workspace shorts|long-form --date YYYY-MM-DD [--hours 48] [--out DIR] [--dedupe-dir workspaces/<ws>] [--dry-run]` writes `DIR/<date>-radar.json` and `DIR/<date>-radar.md`. Item: `{id, title, url, source, published_at, signals{...}, products[], summary, why_now}`. Dedupe drops items whose URL or normalized title appears in `videos/*.md` titles, `published/*.md`, or the previous 7 radar JSON files in `DIR`.
- Source scripts, each `--hours N --limit N [--dry-run]`, JSON list on stdout: `reddit.py` (r/LocalLLaMA, r/ollama; OAuth if `REDDIT_*` set, else public `.json` endpoints with a UA), `hn.py` (Algolia, query set in rules/sources.md), `hf_trending.py`, `github_releases.py` (repo list in rules/sources.md), `youtube_recent.py` (Data API `search.list`, needs `YT_API_KEY`, skipped if absent), `firecrawl_search.py` (FireCrawl search API, needs `FIRECRAWL_API_KEY`, skipped if absent).
- Rules: `sources.md` (what each source is for, query lists, repo list), `scoring.md` (signal normalization, product-name extraction list, why-now rubric), `dedupe.md`.

### skills/youtube-keyword-research
- `scripts/autocomplete.py "seed" [--hl en --gl US] [--dry-run]` JSON: `{seed, suggestions[], expansions{prefix: [...]}, depth_score}` using `suggestqueries.google.com` with `ds=yt`, `client=firefox`.
- `scripts/competition.py "query" [--max 20] [--dry-run]` JSON: `{query, top[{id,title,channel,subs,views,published_at,duration_s,is_short}], median_views, median_subs, share_recent_180d, exact_title_rate, small_channel_velocity}`; needs `YT_API_KEY` (`search.list` + `videos.list` + `channels.list`).
- `scripts/opportunity_score.py --candidates FILE.json --out FILE.json` where a candidate is `{title, keyword, autocomplete{}, competition{}, vidiq{volume, competition}|null, trend_slope|null, named_product: bool}`; writes the same list with `demand`, `competition_score`, `opportunity` (0-100) and `rank`. Formula in `rules/opportunity-score.md` (research section 2.8; z-blend; named-product bonus +10).
- Rules: `vidiq-mcp.md` (which vidIQ MCP tools to call, what to record, credit budget ~10 calls per run, what to do when the connector is absent), `opportunity-score.md`.

### skills/blai-research
- Port of v1 `skills/blai-research/SKILL.md` (fan-out subagents, cite only fetched URLs) rewritten for v2: FireCrawl MCP on every run when available, `WebFetch` fallback. Brief is written twice: `<slug>-brief.md` (human) and `<slug>-brief.json` (machine, schema `shared/schemas/research.schema.json`).
- `scripts/validate_research.py <brief.json> [--schema ../../shared/schemas/research.schema.json]` exit 0/1 (port of v1; default schema path relative to the script's own location).
- Rules: `citation-rules.md`, `brief-format.md` (the markdown layout that mirrors the JSON).

### skills/script-gates
- Port of v1 `pipeline/scripts/validate_storyboard.py`, `eval_short.py`, `normalize_narration.py`, `pipeline/formats.json`, `pipeline/tts_lexicon.json`, plus a new `voice.config.json` (`engine: elevenlabs`, `wps: 2.9`, measured later). Paths inside the scripts point at: `skills/script-gates/formats.json`, `skills/script-gates/tts_lexicon.json`, `skills/script-gates/voice.config.json`, `shared/schemas/storyboard.schema.json` (via `../../shared/...` from the script's own location), `skills/render-shorts/styles/history.json`. Keep v1 CLIs; document each in SKILL.md with one example.
- `formats.json` keeps `classic` and `smooth-explainer` bands unchanged and adds `structure` as a free field (the validator must not reject unknown `structure` values).
- Rules: `format-bands.md` (what each band means), `number-and-term-rules.md` (spoken numbers, lexicon usage), `eval-gates.md` (the 7 gates, one line each, and which are soft).

### skills/elevenlabs-narration
- `scripts/generate_audio.py --text FILE.txt|--storyboard FILE.json --out DIR [--voice-id ID] [--model eleven_multilingual_v2] [--format long|short] [--dry-run]` -> `DIR/narration.wav` (44.1 kHz mono), `DIR/alignment.json` (character timestamps from `/v1/text-to-speech/{voice}/with-timestamps`, concatenated with offsets), `DIR/chunks/NN.mp3`, `DIR/voice.json` summary `{duration_s, chars, chunks, credits_estimate, model, voice_id_hint}`. Chunk at paragraph boundaries, <= 4,500 chars, pass `previous_text`/`next_text`, pin `seed`, apply `pronunciation_dictionary.json` (alias rules) before the call.
- `scripts/qa_transcribe.py --audio DIR/narration.wav --script FILE.txt --out DIR [--dry-run]` -> `DIR/transcript.json`, `DIR/qa.json` `{wer, mismatches[{expected, heard, at_s}], pass: bool}`; uses `faster-whisper` when importable, else `whisper.cpp` binary on PATH, else fails with install hints. Threshold 0.03.
- `scripts/captions.py --alignment DIR/alignment.json --script FILE.txt --out DIR` -> `DIR/captions.json` (`[{word, start, end}]`) and `DIR/captions.srt`.
- Rules: `recording-a-dataset.md`, `chunking-and-settings.md`, `qa-loop.md`, `pronunciation.md`.

### skills/render-shorts (port of v1)
- `remotion/` (v1 `render/remotion` source without node_modules/out/props json), `hyperframes/` (v1 `render/hyperframes` without node_modules/media), `manim/` (v1 `render/manim` without media/__pycache__), `styles/` (v1 `docs/styles/*.md` + `history.json`), `rules/hyperframes.md`, `rules/manim.md`, `rules/remotion-editor.md` (v1 `docs/appendices`), `rules/scene-agent.md` (scene worker rules from v1 `AGENTS.md` plus `skills/blai-hyperframes|blai-manim|blai-editor`), `vendor/` only the `hyperframes-*` skills the rules actually reference.
- `scripts/assemble.py --slug S --storyboard FILE.json --audio narration.wav --captions captions.json --scenes-dir DIR --out DIR [--draft]` -> `DIR/final.mp4` via the Remotion project (props JSON generated, not hand-copied).
- `scripts/lint_video.py final.mp4` and `scripts/safe_zone_check.py final.mp4` (ports), exit 0/1.
- `scripts/style_rotation.py --pick --slug S [--history styles/history.json]` prints the next pack honoring "never the same pack twice in a row" and records it with `--record PACK`.

### skills/render-longform (new)
- `remotion/` Remotion 4 + React 19 TypeScript project, 1920x1080@30. `src/Root.tsx` registers `Episode` (props: spec, captions, audioSrc, captures) and `Thumbnail` (props: concept, title). Scene components under `src/scenes/`: `TitleCard`, `ChapterCard`, `KineticText`, `CodeTyping`, `TerminalReplay` (plays an asciinema v2 cast or a `capture.json` stdout transcript), `Diagram` (boxes + arrows from `data.nodes/edges`), `ComparisonTable`, `Chart` (bar/line from `data.series`), `StatCallout`, `Quote`, `MascotTalk` (placeholder SVG mascot, mouth opens by audio amplitude envelope from `captions.json` word timing; real design dropped in later), `BRoll` (plays a local clip with an overlay; clip path from `data.src`), `EndCard`. Brand constants in `src/constants.ts` (`#0B1020`, `#F5F0E8`, `#FFB347`, `#7BD88F`, `#FF6B6B`, Inter). Scene durations come from the spec (`est_duration_s`) stretched to the real narration timing when `captions.json` is present.
- `scripts/render_longform.py --spec FILE.json --audio narration.wav --captions captions.json [--captures DIR] --out DIR [--draft]` -> `DIR/final.mp4`, `DIR/thumbnails/1.png,2.png,3.png`, `DIR/captions.srt` copy, `DIR/render.json` timings. `--draft` renders at 640x360 with `--frames` sampling for a quick check.
- `scripts/lint_longform.py final.mp4 --target-s N [--chapters FILE]` exit 0/1 (resolution, fps, codec, loudness -14 +/- 1 LUFS via ffmpeg ebur128, duration within +/-10 %).
- Rules: `scene-library.md` (each scene type: when, what the spec must carry in `data`, what the muted viewer gets), `spec-to-composition.md`, `thumbnails.md`.

### skills/dgx-capture (new)
- `scripts/capture.py --plan FILE.md|FILE.json --out DIR [--window any|night] [--dry-run]` runs each command in the plan (format in `rules/experiment-plan-format.md`: id, command, timeout_s, expect, parse) under `timeout`, records with `asciinema rec` when available (else captures stdout/stderr), refuses any command whose first token is not in `allowlist.json` or that contains a denied pattern (`rm -rf`, `sudo`, `>`/`>>` outside `DIR`, `curl | sh`), checks `nvidia-smi` free memory before GPU commands, writes `DIR/capture.json` `[{id, command, exit, duration_s, stdout_tail, metrics{tok_s, vram_gb, load_s, ...}}]` and `DIR/<id>.cast`.
- Rules: `allowlist.md` (families: ollama, llama-server/llama-cli, vllm, python benchmark scripts under `skills/dgx-capture/benchmarks/`, nvidia-smi, docker run of listed images, huggingface-cli download), `experiment-plan-format.md`, `reconcile.md` (tolerance 10 % for tok/s, 5 % for memory; how a narration line is rewritten).

### skills/blotato-publish (new)
- `scripts/publish.py --package FILE-package.md --video final.mp4 [--thumbnail FILE.png] [--slot auto|ISO] [--privacy private|public|unlisted] [--dry-run]` uploads the video (and thumbnail) to R2 via `r2.py`, builds the Blotato body from the manifest (`rules/manifest-mapping.md`), `POST https://backend.blotato.com/v2/posts` with header `blotato-api-key`, prints JSON `{post_submission_id, scheduled_time, media_url, thumbnail_url}`. `--status ID` polls. `--accounts` lists accounts. Rate limit 30/min; retry 429/5xx with backoff.
- `scripts/r2.py upload FILE --key KEY` prints the public URL; `r2.py delete --key KEY`; uses `boto3` (S3-compatible) with `R2_*` env.
- `scripts/slots.py --format short|long --after ISO` prints the next slot per `shared/playbook/publish-timing.md` (America/Chicago).
- Rules: `manifest-mapping.md`, `status-and-errors.md`.

### skills/telegram-gate (new)
- `scripts/send_card.py --kind fyi-ideas|gate|blocked|checklist|text --hub FILE.md [--ideas FILE.md] [--video FILE.mp4] [--preview-url URL] [--text "..."] [--dry-run]` sends via Bot API (`sendMessage`/`sendVideo`, inline keyboards from `rules/cards.md`), prints `{message_id}`. Callback data: `approve:<slug>`, `reject:<slug>`, `rerender:<slug>`, `rescript:<slug>`, `swap:<date>:<n>`.
- `scripts/bot.py [--once] [--dry-run]` long-polls `getUpdates`, answers callbacks, updates the hub note (`status`, `feedback`, `approved_at` in the build journal), commits with `tools/git-sync.sh`, handles a text reply after Reject as `feedback`, handles `swap:` by writing `workspaces/<ws>/stages/02-ideas/output/<date>-picks.md`, handles `rescript:` by POSTing to `ROUTINE_RESCRIPT_URL` with `{"text": "rescript <slug>: <feedback>"}`. Single-process; state in `build/state/telegram-offset.json`.
- Rules: `cards.md` (exact card layouts), `callbacks.md`.

### skills/youtube-analytics (Phase 4)
- `scripts/yt_stats.py` (port of v1) and `scripts/weekly_retro.py --week YYYY-WW --out analytics/` producing `analytics/<week>.md`; rules `retro-format.md`.

### build/
- `install.sh` (idempotent, user-level where possible, prints what needs sudo), `systemd/blai-build.service` + `.timer` (every 5 min) + `blai-telegram-bot.service` as **user units**, `build.py` (`--once`, `--dry-run`, `--slug S`), `stage_runner.py` (how each Spark stage is invoked: mechanical stages call the skill scripts; creative stages run `claude -p --dangerously-skip-permissions --output-format json` inside the workspace with the prompt "Run stage NN for <slug> in unattended mode. Read CLAUDE.md, then stages/NN-name/CONTEXT.md, and follow it exactly."), `routines/*.md` (the four routine prompts plus the retro), `README.md`, `.env.example` generated from `shared/env-template.md`.
