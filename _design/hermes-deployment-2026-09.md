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
each (neutral 0.5/0.5, calm 0.3/0.7, energetic 0.7/0.3). **User picked neutral.** Wired:
`BLAI_VOICE_REF`, `BLAI_VOICE_EXAGGERATION=0.5`, `BLAI_VOICE_CFG_WEIGHT=0.5` in `build/.env`.
Full regen of the 2026-08-30 narration in the clone: 373 words / 116.56 s = **3.20 wps** ->
`voices_wps["chatterbox:hamza-yt-01"]`. That regen fell back to proportional timing:
`find_whisper` found `WHISPER_CPP_BIN` but searched for the model only under the Kokoro tree.
Fixed twice over: `WHISPER_CPP_MODEL` added to `build/.env`, and the resolver now also checks
the binary's own checkout (`.../models/`). Forced `--align whisper` in the clone: 29 heard / 33
timed, source whisper.

## Publishing, closed the same night

`publish.py --accounts` first returned `[]`: the YouTube channel was not connected inside
Blotato. The user connected it (account id 48833, "Hamza (BuildLocalAI)"), created the R2
bucket `blai-media` with an Account API token scoped to it (ListBuckets is 403 by design), and
enabled the r2.dev public URL. Verified end to end: `r2.py upload` -> public fetch HTTP 200 ->
`r2.py delete`. `BLAI_PUBLISH_PRIVACY=private` until the first post is checked in Studio.

Two more corrections on the way:
- `build.py` listed `ELEVENLABS_API_KEY`/`ELEVEN_VOICE_ID` as REQUIRED env, so the publish-only
  pass refused to start on a Chatterbox box. Voice keys removed from `REQUIRED_ENV`,
  `install.sh` and `.env.example`; the engine choice is preflight's voice-engine check.
- Hermes cron `--script` takes ONLY a bare filename under `~/.hermes/scripts/` (`.sh` via
  bash); inline commands and absolute paths are rejected. Scripts: `blai-preflight.sh`,
  `blai-publish.sh` (both run under `~/blai/venv`, which has boto3 + python-dotenv; the
  system python has neither). Both test-fired: succeeded.

First scheduled dry cycle (2026-09-02 evening): `blai-ideas` on GLM = 1,330,226 tokens, zero
K3; picks `2026-09-02-claude-code-went-rogue-and-del`, `2026-09-02-dgx-spark-runs-qwen3-8-flash-n`.
`blai-produce` (both slugs, ONE session) = 15.8M GLM tokens; both hubs reached ready-to-build;
writers + judge went through `llm_call.py` on K3 (drafts notes: "judge: kimi-k3 via
tools/llm_call.py"), invisible to `hermes insights` because they are not Hermes sessions.
`blai-build` died after stage 06 (voice ok 122 s in the clone): **HTTP 429 "Usage limit reached
for 5 hour"** from the Z.ai coding plan (2K credits/5h; reset 01:38 CT). Measured: ~19M tokens
consumed the whole 5-hour bucket, i.e. ~1 credit per 10K tokens on this tier. The weekly cap is
10K credits (~100M tokens): at tonight's rate (~37M/day for two Shorts) the tier supports about
one Short every 2-3 days. The fallback then failed too: `x-preview-f-free` is no longer served
by the keyless relay (HTTP 401 "not supported"); the relay lists `deepseek-v4-flash-free`,
`nemotron-3-ultra-free` and others.

Response the same night: ideas + produce PAUSED; a one-shot `blai-build-once` at 02:00 CT
(after the reset) builds the two finished Shorts; fallback chain repointed at the served free
models; produce/build jobs rewritten as thin parents that launch one `hermes -z` child session
per slug (context reset per slug); blai-run gains the one-slug-per-session and
research-inside-delegate rules. Decision for the user: raise the Z.ai tier, or run one Short
a day on this one.

## Still parked

Tailscale SSH `check` mode (`tailscale set --ssh=false` from the LAN), `tailscale serve --bg
9119` for the dashboard, the Mac `spark-ts` alias -> tailnet IP. Self-learning loop:
`_design/self-learning-loop.md` (design only).
