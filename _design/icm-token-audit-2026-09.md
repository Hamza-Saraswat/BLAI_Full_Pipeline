# ICM and token audit, 2026-09-05

Question from the operator: is the ICM structure set up correctly, and is it actually saving
tokens? Evidence-based answer, stage by stage, after the Hermes deployment and the scripted
render landed the same day.

## 1. Structure: is ICM set up correctly?

`tools/validate.py workspaces/shorts --allow-outputs` = **17/17** after today's edits (stage-07
contract rewritten for the scripted render; two em dashes the Aug-30 writer left in outputs
removed). The five layers, stage contracts, handoffs, triggers and guardrails are unchanged
from `icm-compliance-2026-08.md`; the four documented deviations still stand. New today, all
inside the pattern language:

| Change | ICM pattern | Where |
|---|---|---|
| Scene workers are a script, not an agent | 10 specs are contracts, 12 audits are scripts, 7 tool prerequisites | `07-render/CONTEXT.md` step 2, `skills/render-shorts/scripts/scene_worker.py` |
| Rules read verbatim by the worker, never copied | 5 canonical sources | `scene-agent.md`, tool rules, `styles/<pack>.md` fed as-is |
| How a transcriber hears a term lives next to how it is spoken | 5 canonical sources, 15 shared constants | `pronunciation_dictionary.json` `_heard_as` |
| Render note generated from machine outputs | 14 docs over outputs | `render_note.py` |
| One trigger, one slug per Hermes session | 2 output handoffs | `skills/blai-run/SKILL.md` |

Verdict: correct. What ICM governs (what each stage may read, how stages hand off, what counts
as done) held through every failure this week; the failures were execution mechanics.

## 2. Tokens: what the structure could not save, and what did

Z.ai's credit formula for GLM-5.3: `(input x 6.9 + cached x 1.7 + output x 24) / 10,000`.
Sept 2-5 ledger (59.1M GLM tokens): 2.48M fresh input, ~56M cached re-reads, 0.72M output ->
**73% of credits were cached context re-reads** inside agent loops. ICM keeps each turn's
context small (~6-8K per stage); it cannot stop an agent from re-sending that context 300 times.
The lever is fewer turns, i.e. scripts.

Measured, per stage of one Short (credits at Z.ai's standard rate; off-peak is 50%):

| Stage | Before (agent) | Now | Mechanism |
|---|---|---|---|
| 01-02 ideas (both picks) | ~150 | ~150 | agent (GLM), unchanged |
| 03-05 produce, per slug | ~850 | ~850 | agent (GLM) + K3 writers via `llm_call.py` |
| 06 voice | 0 | 0 | scripts |
| 07 render | **~2,000** | **~50-120** | `scene_worker.py` on GLM-5.3-Flash, 1-3 rounds, sequential; measured 4.5-13 credits per scene |
| 08 publish | 0 | 0 | scripts |
| **Per Short** | **~3,000** | **~1,050** | |

Kimi (metered): writers + judge are three direct calls per Short (~30-45K tokens); the daily
digest ~100K. The Aug-30 walk (64.9M K3 tokens) is the number that must never repeat, and the
seat map + one-slug-per-session rules make it structurally impossible for a scheduled run.

## 3. What is still an agent, and why it is next

Stages 03-05 (~850 credits/slug) are now 80% of a Short's cost: the research fan-out pulls page
content into the orchestrator's context, and the script stage runs many validator turns. The
same treatment applies: research inside one delegate returning only the brief path (rule
exists, enforce it in the shim), `glm-5.3-flash` for the child session (3x cheaper credits),
and the mechanical validators run by a driver script instead of agent turns. Target: ~300
credits per slug, which puts two Shorts a day inside the Lite tier's 10K/week.

## 4. Guardrails that keep it honest

`tools/health_check.py` (daily report 08:05 CT, hourly alerts): GLM quota probe with Z.ai's
reset time, Kimi balance with a $10/day spend alert, blocked hubs with reasons, services,
preflight, today's scene credits, disk/GPU, cron states, R2 reachability. Every number above is
re-derivable from `workers/*/handback.json`, `hermes insights`, and the two consoles.
