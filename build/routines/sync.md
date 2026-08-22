# Syncing the routines

The five cloud routines are created and updated with the `RemoteTrigger` tool from a Claude Code session (the `/schedule` skill loads it; `ToolSearch select:RemoteTrigger` when it is deferred). The prompt text of each routine is the "Prompt" section of the matching file in this folder; paste it verbatim into `events[0].data.message.content`. Routines cannot be deleted from the tool; use https://claude.ai/code/routines for that.

## Fixed values

| Field | Value |
|-------|-------|
| Environment | `env_01XYTtSrThHrPHciRYUeHibm` (claude.ai/code environment "Default", see `shared/cloud-environment.md`) |
| Repo | `https://github.com/Hamza-Saraswat/BLAI_Full_Pipeline` (branch `main`, cloned at the working directory) |
| `allowed_tools` | `["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebFetch", "WebSearch", "mcp__firecrawl__firecrawl_scrape", "mcp__firecrawl__firecrawl_search", "mcp__firecrawl__firecrawl_map"]`; the ideas routines add the vidIQ tools as `mcp__vidiq__*` (read the tool names from the connector after attaching it) |
| `enabled` | `false` at creation; flip to `true` with an update once the environment variables exist |

| Routine | `name` | `cron_expression` (UTC) | `model` | `mcp_connections` |
|---------|--------|--------------------------|---------|-------------------|
| Shorts ideas | `blai-shorts-ideas` | `0 11 * * *` | `claude-sonnet-5` | vidIQ |
| Shorts produce | `blai-shorts-produce` | `0 12 * * *` | `claude-opus-5` | none |
| Long-form ideas | `blai-longform-ideas` | `0 11 * * 1,3,5` | `claude-sonnet-5` | vidIQ |
| Long-form produce | `blai-longform-produce` | `0 12 * * 1,3,5` | `claude-opus-5` | none |
| Weekly retro | `blai-weekly-retro` | `0 13 * * 0` | `claude-sonnet-5` | none |

Cron is UTC; the local times in the routine files assume CT summer time. Move the ideas and produce crons one hour later in winter if 06:00/07:00 CT must hold.

## Create body

```json
{
  "name": "blai-shorts-ideas",
  "cron_expression": "0 11 * * *",
  "enabled": false,
  "mcp_connections": [
    {"connector_uuid": "<uuid of the vidIQ connector from claude.ai/customize/connectors>", "name": "vidiq", "url": "https://mcp.vidiq.com/mcp"}
  ],
  "job_config": {
    "ccr": {
      "environment_id": "env_01XYTtSrThHrPHciRYUeHibm",
      "session_context": {
        "model": "claude-sonnet-5",
        "sources": [{"git_repository": {"url": "https://github.com/Hamza-Saraswat/BLAI_Full_Pipeline"}}],
        "allowed_tools": ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebFetch", "WebSearch", "mcp__firecrawl__firecrawl_scrape", "mcp__firecrawl__firecrawl_search", "mcp__firecrawl__firecrawl_map"]
      },
      "events": [
        {"data": {"uuid": "<fresh lowercase v4 uuid>", "session_id": "", "type": "user", "parent_tool_use_id": null,
                  "message": {"role": "user", "content": "<the Prompt section of shorts-ideas.md>"}}}
      ]
    }
  }
}
```

Call `RemoteTrigger {action: "create", body: <that>}` once per routine; the response carries the routine id (`https://claude.ai/code/routines/<id>`). Record the ids in this file's table when they exist.

## Update, enable, run

- Change a prompt: edit the routine file here, commit, then `RemoteTrigger {action: "update", trigger_id, body: {job_config: {...same shape with the new content...}}}`. Partial updates are allowed; the `job_config` object is replaced whole, so send the full `ccr` block.
- Enable: `{action: "update", trigger_id, body: {enabled: true}}`. Enable the ideas routines first, watch two runs (`{action: "list_runs", trigger_id}` then `{action: "get_run_log", session_id}`), then the produce routines, then the retro.
- Replace connectors: `body: {mcp_connections: [...]}`; remove all: `body: {clear_mcp_connections: true}`.
- Run now: `{action: "run", trigger_id}`. Use this for the first test of each routine instead of waiting for the cron.

## Connectors

Add the vidIQ MCP once at https://claude.ai/customize/connectors (custom connector, URL `https://mcp.vidiq.com/mcp`, OAuth). Its `connector_uuid` shows up in the `/schedule` skill's connector list; attach it only to the two ideas routines. FireCrawl is not a connector: it runs from the repo's `.mcp.json` inside the session with `FIRECRAWL_API_KEY` from the environment.

## The re-script API trigger

The Telegram bot (`skills/telegram-gate/scripts/bot.py`) re-scripts a rejected video by POSTing `{"text": "rescript <slug>: <feedback>"}` to `ROUTINE_RESCRIPT_URL` with `ROUTINE_RESCRIPT_TOKEN`. Create that trigger on the produce routine's page at https://claude.ai/code/routines (API trigger; the `RemoteTrigger` tool exposes only cron and one-time schedules) and copy the URL and token into the Spark's `build/.env`. The payload text arrives as part of the run's input, which is why both produce prompts start by looking for a `rescript <slug>:` line. One trigger per produce routine; the bot picks the URL by workspace when two are configured, otherwise it uses the single `ROUTINE_RESCRIPT_URL` for both.

## Checklist before enabling

1. Cloud environment variables set (`shared/env-template.md`, cloud block).
2. Network allowlist contains the domains in `shared/cloud-environment.md`.
3. vidIQ connector attached to both ideas routines.
4. One manual `run` of each routine reviewed with `get_run_log`.
5. Daily cap checked at claude.ai/code/routines (4 runs on Mon/Wed/Fri, 2 otherwise, plus Sunday's retro).
