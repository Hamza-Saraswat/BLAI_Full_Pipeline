# ICM compliance pass, 2026-08-29

The shorts-only workspace checked against `research/ICM-BUILD-GUIDE.md` (paper v2 + repo 02ba5d8),
after the long-form removal and the 66-finding fix pass. Format: principle -> evidence -> gap ->
what was done. Mechanical baseline: `tools/validate.py workspaces/shorts --allow-outputs` = 17/17;
`tools/check_outputs.py` = 0 failures; `tools/preflight.py` = 10/10 checks green on this Mac.

## 3.1 Five layers

| Layer | File | Verdict |
|---|---|---|
| 0 | root `CLAUDE.md` (48 lines) + `workspaces/shorts/CLAUDE.md` (89) | PASS -- folder map, triggers, routing, per-agent rules; rewritten shorts-only this pass |
| 1 | root `CONTEXT.md` (22) + workspace `CONTEXT.md` (26) | PASS -- routing only, no content |
| 2 | 8 stage `CONTEXT.md`, 43-66 lines | PASS -- all under the 80-line cap |
| 3 | `brand-vault/` (own CONTEXT.md), `shared/`, `skills/`, stage `references/` | PASS -- no reference file over 200 lines in the workspace scope |
| 4 | `stages/*/output/`, `input/`, `videos/` hub notes | PASS -- outputs committed BY DESIGN (deviation, below) |

## 3.2-3.3 Canonical tree, factory vs product

The repo adapts the guide's single-workspace tree to a repo-level container: `skills/`,
`brand-vault/` and `shared/` sit at the root and serve the one workspace, with root `CLAUDE.md`
as the router the guide's own 3.8 describes. Gap found during this pass: the root folder map
still drew a two-child `workspaces/` tree and a stale tools list -- fixed.

## 3.4 Stage contract

All 8 stages carry Inputs/Process/(Checkpoints)/(Audit)/(Verify)/Outputs in order (validator
checks 8-9), Inputs rows carry Section/Scope and Why, every path resolves (check 12). This pass
added: an Engine row that resolves to a committed file (`build/.env.example`) instead of the
runtime `.env`; `scene-constraints.md` in stage 04's Inputs so briefs are legal on arrival
(finding 61); audit rows in stage 03 for Summary-vs-Thesis and brief self-consistency
(findings 25, 29).

## 3.5 Handoffs and naming

`[slug]-[artifact]` naming enforced by the schemas; handoff via `output/` only; `check_outputs.py`
now also fails a hub note whose Artifacts wikilink still reads "(filled by stage NN)" when that
stage's output exists (finding 38) -- the body contract is machine-checked, not aspirational.

## 3.6-3.7 Triggers, movement

`setup`, `status`, `ideas`, `produce`, per-stage keywords declared in the workspace CLAUDE.md
table; status derives from disk. No orchestrator. PASS.

## 3.8 Mechanics

Delegation (stage 04's two blind writers, stage 07's scene workers) is prompted from the stage's
own CONTEXT.md + Layer 3 files, per the guide. This pass hardened it: each parallel worker gets a
PRIVATE scratch directory named in the contract (finding 11), and each writer a distinct hook
pattern (finding 12).

## 3.9 Token budget

Heaviest stage is 04-script: ~1,500 (L0-2) + brief (~2k) + voice-rule sections + structures +
hook library + scene-constraints (40 lines) + band/platform rows -- roughly 6-7k, inside the 8k
line. No reference file over 200 lines, so any single input can be loaded alone.

## 4.x Conventions

| Pattern | Verdict | Notes from this pass |
|---|---|---|
| 1 Stage contracts | PASS | validator 8-9 |
| 2 Output handoffs | PASS | |
| 3 One-way refs | PASS | validator 10 |
| 4 Selective sections | PASS | validator 9 |
| 5 Canonical sources | PASS with one mitigation | safe-area numbers now have ONE computing source (`blai_layout.py`, comments corrected -- finding 51); `SETUP-NOTES.md` still restates the table for humans but both docs now order "import the constants, never retype". wps: `voice.config.json` is canonical, `script-format.md` points |
| 6 CONTEXT = routing | PASS | all 43-66 lines |
| 7 Tool prerequisites | PASS, now enforced | setup guides existed but were never RUN (finding 33). New `tools/preflight.py` executes each skill's documented smoke check before any build; wired as build.py's first act |
| 8 Questionnaire | PASS | placeholders resolve (validator 16-18) |
| 9 Bundled skills | PASS | 10 skills, self-contained; GSAP now vendored so renders need no network (finding 54) |
| 10 Specs are contracts | PASS | storyboard carries visual_brief/beats, not pixel positions; beats now anchored to narration phrases, not wall-clock (finding 56) |
| 11 Checkpoints | PASS | creative stages 02/04/05 have them; unattended mode journals the decision instead |
| 12 Stage audits | PASS, sharpened | script-decidable checks name their script; entity gates demoted to advisory where they contradicted the shipped corpus (finding 9); judge rubric gained teaching row + myth-bust fairness + label deletion test + drift check (findings 14-17) |
| 13 Value validation | PASS | value_types locked in the hub note, checked at script audit |
| 14 Docs over outputs | PASS | root rule 5; dedupe read of `published/` is the named exception |
| 15 Shared constants | PASS | brand tokens in pack CSS/`blai_packs.py`; text classes split content (>=64px) vs chrome (finding 58) |

## 4.7 Guardrails

CONTEXT <=80 lines: PASS (max 66). References <=200: PASS. No em dashes: validator 3 PASS.
`.gitkeep`: validator 4 PASS. Naming: validator 5-7 PASS. Relative paths: validator 12 PASS.

## 4.8 Definition of done

- setup runs cleanly, placeholders resolve: PASS (validator)
- End-to-end run: the 2026-08-23 dry run produced two full Shorts on this Mac; a fresh post-refactor
  run is the last verification step of this rebuild
- Outputs committed: DELIBERATE DEVIATION -- text outputs are the audit trail and the Obsidian
  archive (root CLAUDE.md rule 3); binaries never committed; `validate.py --allow-outputs` encodes it
- Checkpoints + audits on creative stages: PASS
- No circular deps: PASS (validator 10)
- Validator passes: 17/17

## Documented deviations (all deliberate, all recorded here)

1. **Committed text outputs** (above).
2. **Repo-level container**: one workspace, with `skills/`/`brand-vault/`/`shared/` at the root
   serving it; root CLAUDE.md routes exactly as guide 3.8 prescribes for multi-folder repos.
3. **Triggers take arguments** (`ideas --date ...`); the guide's bare-keyword rule is kept for
   `setup`/`status`, and the argument forms are declared in the same table.
4. **`input/` priority lane** (guide section 9 convention) is adopted.

## What this pass changed to reach compliance

Root CLAUDE.md folder map + tools list corrected; Engine input row resolves to a committed file;
finding-38 body check added to `check_outputs.py`; `preflight.py` created and wired (Pattern 7's
missing half); scene-constraints reference created and wired (finding 61); all render-rule
documents reconciled with their own code (findings 51-55, 58-60).
