> Fetched web_extract on 2026-09-18. URL: https://skillcrossroads.com/report

# The State of Claude Code Skills

_An evidence-based audit of 216 public Claude Code skills across 18 repositories, graded by **Skill Crossroads** (rubric v1.2) -- the signpost for Claude Code artifacts. Includes the LLM-assisted checks (full edition). Every figure is traceable to the pinned git trees in the methodology. Generated 2026-09-10._

> **Edition & pinning.** Generated **2026-09-10** under **rubric v1.2, LLM (full) edition**. This report is a pinned snapshot: its figures are exact for the git trees and rubric named in the methodology, and are regenerated -- never hand-edited -- when the rubric moves.

> **Scope.** A deliberately mixed sample: Anthropic's well-maintained `anthropics/skills` catalog alongside a spread of community-authored repos (up to 12 skills each). This is a read on skills people actually publish -- not a curated best-of.

## The headline

**Among skills Skill Crossroads could score, 69% have a description that won't reliably trigger** -- 87 (40%) outright unlikely to fire, 61 (28%) borderline. "My skill never fires" is the #1 real-world skill failure, and it hides in the frontmatter `description`.

Skill Crossroads scored **215 of 216** skills for triggering -- 1 could not be reached (model/network errors) and are excluded from the triggering figures.

The average Skill Crossroads score across all 216 skills is **82.1/100**.

## Will your skill even fire? (Triggering & Discoverability)

How the LLM triggering check graded each description:

fires reliably (pass) 31% (67)
borderline (warn) 28% (61)
won't fire (fail) 40% (87)

A description fails when it reads like a title, buries the use case, omits the natural-language phrases a user would actually say, or is so broad it never anchors. All of it is fixable **before** you publish -- that's the point of the check.

## Grade distribution

A 7 (3%) | B 156 (72%) | C 45 (21%) | D 2 (1%) | F 6 (3%)

## How skills do on each check (share that pass cleanly)

STRUCT-01 valid YAML frontmatter 96% n=215 (0 warn, 8 fail)
STRUCT-02 recommended fields present 96% n=215 (1 warn, 8 fail)
STRUCT-05 supporting-file references resolve 94% n=208 (0 warn, 13 fail)
TOKEN-01 under the line/token budget 91% n=215 (16 warn, 4 fail)
TOKEN-02 progressive disclosure 84% n=208 (33 warn, 0 fail)
TOKEN-03 description budget footprint 99% n=215 (2 warn, 0 fail)
TOKEN-04 recurring per-invocation cost 91% n=215 (19 warn, 0 fail)
CLARITY-03 no ASCII-art / persona filler 97% n=215 (1 warn, 6 fail)
SAFETY-01 no hardcoded secrets 97% n=216 (0 warn, 6 fail)
SAFETY-02 allowed-tools least-privilege 95% n=215 (10 warn, 0 fail)
SAFETY-03 no destructive auto-invocation 87% n=215 (28 warn, 0 fail)
SAFETY-04 no shell-injection in ! blocks 100% n=215 (0 warn, 0 fail)
TRIGGER-02 description long enough to anchor 90% n=215 (13 warn, 9 fail)
TRIGGER-03 invocation cues in description 52% n=215 (96 warn, 8 fail)
TRIGGER-05 invocation flags consistent 100% n=215 (0 warn, 0 fail)
VERIFY-01 evals present 0% n=208 (10 warn, 197 fail)
VERIFY-03 version/changelog/readme hygiene 100% n=208 (0 warn, 0 fail)
TRIGGER-01 description triggers reliably 31% n=215 (61 warn, 87 fail)
CLARITY-02 no internal contradictions 80% n=208 (35 warn, 6 fail)
CLARITY-05 constraints & failure modes stated 0% n=215 (21 warn, 193 fail)
VERIFY-04 verification step present 3% n=214 (6 warn, 202 fail)

## What this means

**1 of 216 skills (0%)** pass every check Skill Crossroads ran, cleanly.

The most common defects across the sample:

- constraints & failure modes stated (CLARITY-05): 214 of 215
- verification step present (VERIFY-04): 208 of 214
- evals present (VERIFY-01): 207 of 208
- description triggers reliably (TRIGGER-01): 148 of 215
- invocation cues in description (TRIGGER-03): 104 of 215
- no internal contradictions (CLARITY-02): 41 of 208
- progressive disclosure (TOKEN-02): 33 of 208
- no destructive auto-invocation (SAFETY-03): 28 of 215
- description long enough to anchor (TRIGGER-02): 22 of 215
- under the line/token budget (TOKEN-01): 20 of 215

Each is catchable **before** publishing, with `npx skillcrossroads ./your-skill`.

## Methodology & reproducibility

Deterministic checks (rubric v1.2, no LLM) plus LLM-assisted checks (TRIGGER-01 triggering judge, CLARITY-02 contradictions, CLARITY-05 constraints, VERIFY-04 verification) were run 2026-09-10 against each repo's git tree at the sha below. Deterministic figures are bit-reproducible from those trees; LLM verdicts are content-hash cached and pinned to the same trees, but model output is not guaranteed bit-identical across runs.

Repos (18, 12 skills each, tree SHAs pinned): anthropics/skills, diegosouzapw/awesome-omni-skill, lionelsimai/claude-skills-collection, membranedev/application-skills, Trompetilla/Skills, LeoYeAI/openclaw-master-skills, ComeOnOliver/skillshub, agentskillexchange/skills, ranbot-ai/awesome-skills, inbharatai/claude-skills, onfire7777/universal-ai-skills-library, FridrichMethod/awesome-skills, rootcastleco/rei-skills, itsmostafa/aws-agent-skills, kid-sid/claude-spellbook, Cortexa-LLC/ai-pack, Sandeeprdy1729/skill_galaxy, excatt/superclaude-plusplus.

Reproduce: `npm run build && BEACON_LLM=1 ANTHROPIC_API_KEY=... node scripts/state-of-skills.mjs` (default repo set) -- or pass `owner/repo ...` to scan your own.
