# GitHub issues (source for tools/create-issues.py)

Format: `## Milestone: <title>` headers, then `- [ ] <title> | labels: a, b` items with an indented body. `[x]` marks an item already done at creation time; the script creates it and closes it with a comment. Run `python3 tools/create-issues.py` after `gh auth login` with the personal account that owns the repo.

## Milestone: Phase 0: Foundations

- [x] Clone repo into the vault, symlink from Projects, move research in, root routing files | labels: foundations
  Repo cloned at `Second Brain/BLAI`, symlink `~/Documents/Projects/BLAI_Full_Pipeline`, `research/` moved, root `CLAUDE.md`, `CONTEXT.md`, `README.md`, `.gitignore`, `.mcp.json`, `.claude/settings.json`.
- [x] ICM discovery and mapping documents | labels: foundations
  `_design/workflow-map.md`, `_design/stage-contracts.md`, `_design/builder-brief.md`.
- [x] Brand vault ported from the v1 soul doc | labels: foundations
  `brand-vault/identity.md`, `voice-rules.md`, `content-pillars.md`, `value-framework.md`, `CONTEXT.md`. Voice review pass with the creator still pending (run `setup` in a workspace).
- [x] Shared playbook, platform specs, schemas, env template, cloud environment doc | labels: foundations
  `shared/platform-specs.md`, `shared/playbook/*.md` (6 files), `shared/schemas/*.json` (5), `shared/hub-note-template.md`, `shared/env-template.md`, `shared/cloud-environment.md`, `shared/pipeline-overview.md`.
- [x] ICM validator, output checker, hub-note tools, CI workflow | labels: foundations
  `tools/validate.py` (Appendix A + `--allow-outputs`), `tools/check_outputs.py`, `tools/hubnote.py`, `tools/new-run.py`, `tools/git-sync.sh`, `.github/workflows/validate.yml`.
- [x] Obsidian: Git plugin, excluded folders, Bases dashboard | labels: foundations, needs-human
  Obsidian Git 2.39.0 installed manually with `basePath: BLAI`, `userIgnoreFilters` set, `dashboard.base` written. Human: restart Obsidian, turn off Restricted mode if prompted, confirm the plugin pulls.

## Milestone: Phase 1: Shorts cloud stages

- [x] skills/trend-radar and skills/youtube-keyword-research | labels: shorts, skill
  Scripts with `--dry-run`, rules, fixtures. Live calls verified for HN, Hugging Face and YouTube autocomplete only.
- [x] skills/blai-research port and FireCrawl MCP config | labels: shorts, skill
  v2 SKILL.md, `validate_research.py` with `--schema`, `.mcp.json` (needs `FIRECRAWL_API_KEY` in the cloud environment).
- [x] Shorts stages 01-05 contracts and references; skills/script-gates port | labels: shorts
  `workspaces/shorts/stages/01-05`, `script-structures.md`, `hook-library.md`, `script-format.md`; gates verified against 38 v1 boards.
- [x] Hub note template, new-run, git-sync, questionnaire, triggers | labels: shorts
  `setup`, `status`, `ideas`, `produce`, `rescript` documented in `workspaces/shorts/CLAUDE.md`.
- [ ] Routines blai-shorts-ideas and blai-shorts-produce, Telegram FYI, dry runs | labels: shorts, needs-human
  Create both routines disabled (prompts in `build/routines/`), add the vidIQ connector, set env vars and the network allowlist (`shared/cloud-environment.md`), enable, run once by hand, compare two days of scripts with v1 output.

## Milestone: Phase 2: Spark build + first automated Short

- [ ] Spark install: build/install.sh, systemd user units, deploy key, .env | labels: spark, needs-human
  Run `build/install.sh` on the Spark (ssh spark). Human: `claude` login, add the deploy key to GitHub (write), fill `build/.env`.
- [ ] skills/elevenlabs-narration: record the dataset, train the PVC, first render | labels: spark, needs-human
  Human: record 60-120 min per `rules/recording-a-dataset.md`, ElevenLabs Creator, train the PVC, set `ELEVEN_VOICE_ID`. Then render one v1 script and re-measure `wps` in `skills/script-gates/voice.config.json`.
- [ ] skills/render-shorts verified on arm64 | labels: spark, skill
  `npm install`, `npx remotion browser ensure`, HyperFrames and Manim smoke renders on the Spark; fix arm64 surprises.
- [ ] skills/telegram-gate bot live; build/build.py state machine end to end | labels: spark, needs-human
  Human: create the bot with @BotFather, set `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`. Then a test slug goes idea -> review -> approved -> scheduled with a private post.
- [ ] skills/blotato-publish live: accounts, private test post, then first public Short | labels: spark, needs-human
  Human: Blotato Starter, connect the channel, `BLOTATO_API_KEY`; Cloudflare R2 bucket + token. Flip `BLAI_PUBLISH_PRIVACY` to `public` after the private test.
- [ ] Disable the v1 idea routine and unload the v1 launchd jobs | labels: shorts, needs-human
  `trig_01AhocqKqiyUjEqic2zmk1TE` -> enabled false; `launchctl unload` the BLAI_Animator autopilot plists. Only after two clean days of the new routines.

## Milestone: Phase 3: Long-form

- [x] Long-form stages 01-07 contracts and references | labels: long-form
  `workspaces/long-form/stages/01-07`, `outline-format.md`, `script-format.md`, `retention-beats.md`, `spec-format.md`, `package-format.md`.
- [x] skills/render-longform scene library and thumbnails | labels: long-form, skill
  Remotion 16:9 project with 13 scene types, `render_longform.py`, `lint_longform.py`, fixtures; draft render verified on the Mac.
- [x] skills/dgx-capture guarded runner and reconcile rule; stages 08-11 | labels: long-form, spark, skill
  `capture.py` with allowlist, night window, metrics parsing; `workspaces/long-form/stages/08-11`.
- [ ] Routines blai-longform-ideas and blai-longform-produce; first episode end to end | labels: long-form, needs-human
  Create disabled, enable after env vars; drop the first curated note into `workspaces/long-form/input/`; approve the first card.

## Milestone: Phase 4: Polish loop

- [ ] Mascot scene: design candidates, rig, amplitude mouth | labels: long-form, needs-human
  Generate candidates with the image skill (needs a Gemini key), the creator picks one, vectorize, replace `src/mascot/Mascot.tsx`, enable `mascot-talk` in `stages/06-spec/references/spec-format.md`.
- [ ] B-roll scene with a free stock source | labels: long-form, needs-human
  Pexels or Pixabay API key; `BRoll` scene plays transformed clips; enable `b-roll` in the spec reference; compliance rules in `shared/playbook/compliance.md`.
- [x] skills/youtube-analytics and the weekly retro routine | labels: skill
  `yt_stats.py` port, `weekly_retro.py`, `analytics/CLAUDE.md` retro trigger. Routine `blai-weekly-retro` created disabled.
- [ ] Timing experiments, Test & Compare thumbnail notes, long-form style rotation | labels: long-form
  After four weeks of data: move the slot defaults in `shared/playbook/publish-timing.md`, document the thumbnail A/B workflow, add a second visual rotation for long-form.
