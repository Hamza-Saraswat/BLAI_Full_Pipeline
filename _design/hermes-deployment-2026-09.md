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

02:00 CT one-shot build (2026-09-03): the fresh window was emptied again on ONE slug without a
finished render (9 GLM sessions, +6.8M tokens; the free fallback carried 214K), and a second
429 appeared: "Rate limit reached for requests" (per-minute cap) from nine scene workers in
parallel. Credits are not linear in tokens: a build's many short agent calls burn the bucket
faster than produce's long ones. Children launched from the parent's `terminal(background=true)`
did NOT inherit `build/.env` (voice landed in the repo's `.local-builds/`, not `~/blai/builds`):
the child launch now sources `build/.env` explicitly. Rules added to blai-run: scene workers one
at a time; voice/assembly are scripts. Today's recovery: per-slug one-shots at 07:05 (window
resets 07:00) and 12:05 CT; regular build paused; ideas/produce paused pending the tier decision.
Structural fix proposed: a deterministic `scene_worker.py` (llm_call for code -> render -> lint
-> at most 3 fix rounds) so scenes stop being full agent sessions.

## 2026-09-05: where the credits went, and the scripted render

Z.ai's formula (`(input x 6.9 + cached x 1.7 + output x 24) / 10,000` for GLM-5.3) on four days
of ledger (2.48M fresh input, ~56M cached re-reads, 0.72M output): **73% of credits were
context re-reads**; a build was ~2,000 credits, a bucket. Four bucket exhaustions Sept 2-3.
The Sept-3 07:05 build succeeded (6/6 scenes, card message 5) but in the STOCK voice and from
the CHAT bot: cron-launched sessions never saw `build/.env` (no `BLAI_VOICE_REF`, and
`TELEGRAM_BOT_TOKEN` resolved to Hermes's own bot). GLM's vision tool was unavailable to the
workers; they verified stills programmatically.

Fixes, all live:
- `build/.env` mirrored into `~/.hermes/.env` (21 keys; secrets included, mode 600; gateway
  restarted). New `BLAI_GATE_BOT_TOKEN`, read first by `send_card.py`/`bot.py`, so the two bots
  can never collide again. Every cron job delivers to `telegram:<chat id>` (the digests had no
  target and were lost).
- **Scripted render.** `skills/render-shorts/scripts/scene_worker.py` (rules read verbatim ->
  one completion -> HyperFrames lint/validate/inspect -> render -> ffprobe/safe-zone/lint_video
  -> at most 3 rounds), `scene_packets.py`, `render_note.py`; `build/stage_runner.py::_render`
  runs them in order (agent path only behind `--agent-render`). Stage-07 contract step 2,
  the render skill and `scene-agent.md` updated; validator 17/17.
- First live scene (s06, GLM-5.3-Flash): round 1 pass, 4.33 s vs 4.32 target, 12,379 in /
  1,767 out tokens = **~4.3 credits**, 66 s wall. Attempt 1 had failed 3 rounds because the
  reply hit a 6K output cap (thinking mode ate the budget): fixed with `thinking: disabled` on
  Z.ai, a 16K cap, saved raw replies, truncation reported as a named failure.
- `blai-build` is now `--no-agent --script blai-build.sh` (`build.py --once` under a 16 GiB
  systemd scope, up to three passes), paused until the schedule is re-enabled.
- Z.ai tiers (docs): Lite 2K/5h + 10K/week; Pro 12K/60K; Max 28K/140K. Off-peak 50%.

First scripted builds of the Sept-3 Short in the creator's clone (five passes the same evening,
each one a lesson now encoded in code):
1. Voice QA blocked at WER 0.068 on the clone. Six of eight "errors" were the transcriber's
   spelling: "GB" for a spoken "gigabytes", "multitoken" for "multi-token", "3 .8" for "3.8",
   and the phrase "tokens a second" never canonicalized because the transcript side was
   normalized word by word. `qa_transcribe.py` now: a `_heard_as` table in
   `pronunciation_dictionary.json` (canonical spoken form -> transcriber variants, incl. Qwen),
   number-word hyphens split / other hyphens joined, spaced decimals collapsed, the joined pass
   always adopted, and a spacing-only mismatch forgiven. Result 0.017 (two real one-word
   slips). Threshold unchanged at 0.03.
2. Six stale scene clips were reused under a 6 s longer narration ("segments win" cut the
   audio). `stage_runner` now reuses a clip only if `ffprobe` duration fits the packet's target
   within tolerance.
3. `render_note.py` crashed on dict-shaped sfx cues AFTER the gate card was sent, so two cards
   for a broken cut went out (their keyboards were cleared by the blocked card). The note is
   written before the card now, then rewritten with the message id.
4. `scene_worker.py` tripped on a dangling symlink left by the Sept-3 agent worker in the same
   `workers/sNN/hf` directory (`.exists()` follows links). The project dir is rebuilt fresh
   per run.
5. s01 at 7.5 s needed two worker runs (3 rounds failed on `inspect --strict`, then 2 rounds
   passed): ~27.6K in / 6.6K out tokens = ~12 credits for the hardest scene so far.
6. s03 failed six rounds across two runs on one `inspect --strict` WARNING (a label nested in
   an accent span reads as a text overlap for 0.5 s). Worker now saves every round's report,
   seeds a retried run with the previous run's last report, and escalates the final round to
   GLM-5.3 (`--escalate`, `BLAI_SCENE_ESCALATE`). With the seeded report s03 passed on round 2
   on Flash; escalation was never needed.

**Build #6 (22:17-22:45 CT): status review, gate card 13 from the gate bot, 41.23 s in the
clone, all gates green.** Per-scene (Flash, in/out tokens -> credits at standard rate):
s01 27.6K/6.6K ~12 · s02 28.1K/7.3K ~12 · s03 27.2K/8.7K ~13 · s04 27.0K/4.8K ~10 ·
s05 12.4K/2.1K ~4.5 (first round) · s06 reused (fit the window). Final renders ~52 credits,
~115 counting every failed round of the evening; the agent build was ~2,000. Zero Hermes
sessions, zero K3.

Schedule re-enabled for one Short a day (fits Lite's 10K/week until stage 03-05 gets the same
scripted treatment): 05:45 preflight · 06:00 ideas (GLM) · 06:30 produce, FIRST PICK ONLY
(GLM child session, K3 writers) · 08:00 digest (K3) · 08:30 + 10:30 build (script) · publish
poller 10:00-20:00. The second Sept-2 Short (ready-to-build) builds in the 08:30 pass.

## Still parked

Tailscale SSH `check` mode (`tailscale set --ssh=false` from the LAN), `tailscale serve --bg
9119` for the dashboard, the Mac `spark-ts` alias -> tailnet IP. Self-learning loop:
`_design/self-learning-loop.md` (design only).
