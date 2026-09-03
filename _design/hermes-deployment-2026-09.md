# Hermes deployment log, September 2026

Continues `hermes-deployment-2026-08.md`. Doc-vs-reality corrections and decisions from the
first scheduled-run setup (2026-09-02).

## What the 2026-08-30 walk cost, and why

`hermes insights --days 2`: 64.9M tokens, 27 sessions on kimi-k3, 16.7K on glm-5.3. Two causes:
`delegation.model` was empty (subagents inherit the parent -> all 23 ran on metered K3), and the
whole pipeline ran as ONE 488-message session (44.5M of the tokens were the orchestrator
re-reading its own context). Moonshot bill ~$27.

## Fixes (all live on the box)

- `delegation: {provider: zai, model: glm-5.3}` -- every subagent bills the coding plan.
- `fallback_providers: [{provider: opencode-free, model: x-preview-f-free}]` -- keyless relay,
  fires only on rate-limit/overload.
- `web.backend: firecrawl` -- explicit; it was unset (auto).
- Stage 04 writers + judge are three `tools/llm_call.py` calls on K3 (packet in, draft out),
  never subagents. Measured: a 112-token prompt round-trips in 7.4s. **Moonshot rejects any
  `temperature` other than 1 for kimi-k3** (HTTP 400); the script omits the field unless asked.
- `skills/blai-run/SKILL.md`: one trigger per session, no exploration, no artifact reads,
  scene fix cap 3, no em dashes (the walk's brief and drafts notes carried two; validator
  fails the workspace on them -- fixed by hand).
- `build/build.py --publish-only`: steps 1-2 only, for the cron poller; agent sessions own 06-07.
- Chatterbox delivery params: `chatterbox_tts.py --exaggeration/--cfg-weight`, fed from
  `BLAI_VOICE_EXAGGERATION` / `BLAI_VOICE_CFG_WEIGHT` in `build/.env` by `generate_audio.py`.

## Schedule (box TZ is America/Chicago; cron strings are local)

| CT | job | model | mode |
|---|---|---|---|
| 05:45 | blai-preflight | none | `--no-agent --script` preflight.py |
| 06:00 | blai-ideas | glm-5.3 | agent, skills blai-run+blai-ideas |
| 08:00 | blai-digest | kimi-k3 | agent, ten lines, telegram |
| 08:30 | blai-produce | glm-5.3 | rejected-with-feedback rescan first (the rescript hook), then 03-05 per pick |
| 09:15 | blai-build | glm-5.3 | 06-07 + gate card per ready-to-build hub |
| */15 10-20 | blai-publish | none | `build.py --once --publish-only`; **PAUSED until R2 keys** |

`hermes cron create` quirk: the prompt positional must come right after the schedule, before any
`--option`; trailing prompts are rejected as unrecognized arguments.

## Voice

Reference = the user's own channel ((AI)gentic Bros, `K9cl9QiSjvQ`, 188-207s, chosen by a
whisper density scan: 3.84 words/s, single speaker), loudnorm I=-18, 24 kHz mono ->
`~/blai/voice/refs/hamza-yt-01.wav`. Three clones of the test line rendered on the GB10 in ~9s
each (neutral 0.5/0.5, calm 0.3/0.7, energetic 0.7/0.3). Wiring waits on the user's pick:
`BLAI_VOICE_REF` + the two params in `build/.env`, then a full-narration regen for the measured
`voices_wps["chatterbox:hamza-yt-01"]`.

## Publishing preconditions found tonight

`publish.py --accounts` returned `[]`: no YouTube channel is connected inside Blotato yet. R2
keys also absent. Both are user actions; the poller stays paused until then.

## Still parked

Tailscale SSH `check` mode (`tailscale set --ssh=false` from the LAN), `tailscale serve --bg
9119` for the dashboard, the Mac `spark-ts` alias -> tailnet IP. Self-learning loop:
`_design/self-learning-loop.md` (design only).
