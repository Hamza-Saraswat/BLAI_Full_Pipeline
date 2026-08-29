# Hermes deployment log, 2026-08-29 (Spark: gn100-83c4)

Doc-vs-reality corrections found while executing the v2 plan. The plan file said to record these.

## Corrections to the user's Hermes plan doc

1. The local model actually running is `unsloth/Qwen3.6-27B` at ctx 8192 (not Qwen3.6-35B-A3B-NVFP4),
   Docker-in-tmux at :8000.
2. "Hermes auto-probes Z.ai endpoints -- do NOT hand-set GLM_BASE_URL" is WRONG for billing: the
   bundled zai provider registers `https://api.z.ai/api/paas/v4` (PAY-AS-YOU-GO) as its default.
   We hand-set `GLM_BASE_URL=https://api.z.ai/api/coding/paas/v4` per the user's flat-plan
   directive. Verified live: `hermes -z ... --provider zai -m glm-5.3` -> "GLM OK" on the coding
   endpoint. USER ACTION OUTSTANDING: glance at the Z.ai console once -- plan quota consumed,
   PAYG balance untouched.
3. The `kimi-coding` provider drops the Authorization header for legacy (`sk-...`, non-`sk-kimi-`)
   Moonshot keys in this build -- raw curl with the same key works, Hermes 401s ("Missing
   Authentication header" from the server). Worked around with a NAMED provider:
   `providers.moonshot-k3.base_url=https://api.moonshot.ai/v1`, `key_env=KIMI_API_KEY`,
   `model.default=kimi-k3`. Verified: "K3 OK". (Upstream bug candidate.)
4. Hermes requires models with >= 64K context; the running Qwen serves 8192, so the wired
   `qwen-local` provider is UNUSABLE until the container is relaunched with a larger
   `--max-model-len` (Qwen3.6-27B supports far more; the box has the RAM). Left parked per the
   "no duties yet" decision -- relaunching the user's container is their call.
5. `hermes model` is interactive-only; the headless path is `hermes config set` + named providers.
   The config key is `model.default` (NOT `model.model` -- setting the wrong key leaves the
   shipped `anthropic/claude-opus-4.6` default active).
6. `~/.hermes/.env` ships template lines like an empty `KIMI_API_KEY=`; the loader takes the
   FIRST occurrence, so appending a real key to the end silently loses to the empty template
   line. Dedupe keeping non-empty values.
7. Project-local skills load from `./.hermes/skills` or `./.agents/skills` -- NOT a repo's own
   `skills/` tree. The clean mechanism is `skills.external_dirs: [~/blai/repo/skills]`
   (read-only, no copying): all 15 repo skills (5 triggers + 10 pipeline + vendored subs) now
   list as local/enabled.
8. `hermes config set` mangles list values; nested structures (platform_toolsets) need a YAML
   edit (Hermes's own venv has pyyaml).
9. Telegram token transcription: BotFather tokens are case-sensitive and 0/O-ambiguous in
   screenshots -- verify with getMe before wiring (the gate token needed the letter-O variant).

## State after this session

- Providers live: `moonshot-k3` (K3 OK), `zai` on the coding endpoint (GLM OK), `qwen-local`
  (parked, ctx floor). SOUL.md installed; platform_toolsets: telegram = the factory set
  (web, terminal, file, skills, todo, cronjob, messaging, memory, session_search, clarify,
  delegation, code_execution); browser/vision/image_gen/tts NOT granted.
- Services: `hermes-gateway.service` (own installer unit) and `blai-telegram-bot.service`
  running; linger on. `blai-build.timer` intentionally NOT enabled.
- Keys placed (mode 600): build/.env -- FireCrawl (live-verified), Blotato, gate-bot token +
  chat id 5000565559; ~/.hermes/.env -- Kimi, GLM/ZAI + GLM_BASE_URL pin, gateway token,
  pinned dashboard session token.
- Deploy key added on GitHub (read/write, verified `ssh -T git@github-blai`).
- PENDING: manim apt packages (user's one sudo command: `ssh -t spark 'sudo bash ~/blai/manim-deps.sh'`);
  user DMs @blai_hermes_bot to pair; Tailscale; Chatterbox venv (installing); dashboard service;
  Phase 7 walk; Phase 8 cron; R2 keys.
