# Hermes on the Spark: install and configuration

The reproducible record of this box's Hermes setup (ICM Pattern 7: a setup guide someone who has
never seen the tool can follow). The agent-side identity lives in `SOUL.md` next to this file;
copy it to `~/.hermes/SOUL.md` -- Hermes only reads it from its home, never from a repo.

## 1. Install

    curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o /tmp/hermes-install.sh
    less /tmp/hermes-install.sh        # inspect once; aarch64 is supported (bundled node arm64)
    bash /tmp/hermes-install.sh
    hermes doctor

## 2. Config (`~/.hermes/config.yaml`)

    terminal:
      backend: local
      cwd: /home/<user>/blai/repo
      timeout: 600
    skills:
      write_approval: true

Project context: Hermes loads the repo's `CLAUDE.md` chain (first-match precedence:
`.hermes.md`/`HERMES.md` > `AGENTS.override.md` > `AGENTS.md` > `CLAUDE.md`, ONE type only).
**Never add a HERMES.md or AGENTS.md to the repo** -- either would silently suppress `CLAUDE.md`.

## 3. Identity, bots, toolsets

- `cp build/hermes/SOUL.md ~/.hermes/SOUL.md`
- Bots: `blai` (orchestrator; Kimi K3; toolsets: skills, terminal, process, cronjob, delegation,
  todo, clarify, memory, session_search, messaging) and `smith` (doer; GLM-5.3; toolsets:
  terminal, process, file, code_execution, skills, todo). Writers/judge/scene workers are
  ephemeral `delegate_task` subagents -- never durable bots (writer blindness, findings 12/26).
- Everything else OFF: browser, vision, image_gen, tts, x_search, homeassistant, spotify,
  discord*. The `web` toolset is ON for research work only (stage 03's instrument).
- `hermes skills trust` on the repo once: the bundled `skills/*/SKILL.md` are agentskills.io
  format and become directly callable; the five `/blai-*` trigger skills route to the stage
  contracts.

## 4. Models

- `kimi-coding` (K3) default; `zai` (GLM) doer; `custom` -> http://127.0.0.1:8000/v1 (qwen-base,
  provider only, no duties yet).
- **GLM must bill the coding plan**: resolved base URL must contain `/api/coding/paas/v4`
  (hand-set it if the auto-probe picked the general endpoint); verify one test call consumes
  plan quota, not PAYG balance, in the Z.ai console. If Z.ai rejects Hermes on the coding
  endpoint, STOP and surface the choice -- never silently fall back to metered billing.

## 5. Services (systemd --user, after `loginctl enable-linger`)

Units in this directory: `hermes-serve.service` (dashboard, chat WS channels on, session token
pinned in `~/.hermes/.env`), `hermes-telegram.service` (gateway), `vllm-qwen.service`
(reproduces the Docker vLLM so the wired endpoint survives reboots), plus the repo's
`blai-telegram-bot.service`. `blai-build.timer` stays OFF -- Hermes cron replaces the poll loop.

## 6. Env keys expected

`~/.hermes/.env`: KIMI_API_KEY, GLM/ZAI key, HERMES_DASHBOARD_SESSION_TOKEN, TELEGRAM token
(gateway flow). `build/.env`: FIRECRAWL_API_KEY, BLOTATO_API_KEY (+R2 later), gate-bot
TELEGRAM_BOT_TOKEN + chat id, BLAI_REPO_DIR, BLAI_BUILD_DIR. All mode 600, never committed.
