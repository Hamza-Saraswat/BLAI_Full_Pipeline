# Stage 03: Research

Turn each of today's picks into a sourced brief. Facts in the brief bind every later stage.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../02-ideas/output/[date]-ideas.md` | Rows for today's picks; `[date]-picks.md` if present | Angle, keyword, why-now, swap instructions |
| Hub notes | `../../videos/` | Notes dated [date] with status `idea` | The slugs to research |
| Skill | `../../../../skills/blai-research/SKILL.md` | Full file | Fan-out method, FireCrawl usage, brief layout |
| Skill rule | `../../../../skills/blai-research/rules/citation-rules.md` | Full file | What counts as a source |
| Brand vault | `../../../../brand-vault/identity.md` | "Audience" | Do not research what the viewer already knows |
| Reference | `references/shorts-research-scope.md` | Full file | Depth and what a Short needs from a brief |

## Process

1. List today's picks. If `[date]-picks.md` asks for a swap, create the replacement hub note with `new-run.py` (status `idea`) and set the swapped note to `rejected` with `feedback: swapped`.
2. For each pick restate the angle in one sentence and confirm the slug. **[Checkpoint]** -- confirm or redirect.
3. Run the research method at standard depth (8-12 sources, FireCrawl when available). Numbers verbatim with units; every claim with a URL fetched this run; unsupported beliefs under Unverified.
4. Write `output/[slug]-brief.md` and `output/[slug]-brief.json`.
5. Run `python3 ../../../../skills/blai-research/scripts/validate_research.py output/[slug]-brief.json`. Run the audit checks below. If any fail, revise before saving.
6. Update the hub note: `status: researched`, Artifacts link.
7. Unattended: `../../../../tools/git-sync.sh "shorts: [slug] research"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Restated angle and slug | Confirm or redirect before sources are gathered |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Validator | `validate_research.py` exits 0 |
| Claims | at least 5 claims, each with a fetched URL; every number quoted verbatim with its unit |
| Thesis | one sentence a viewer could repeat, consistent with the pick's angle |
| Specifics | at least 3 key numbers and 2 named products or tools |
| Audience | no claim explains something the Audience section says viewers already know |
| Writer fields | `viewer_situation`, `objection` and `has_process` are all present; when `has_process` is true, `process_steps` lists actions the viewer performs |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Brief | `output/[slug]-brief.md` | markdown per the research skill's brief-format.md |
| Brief data | `output/[slug]-brief.json` | `shared/schemas/research.schema.json` |

The brief in `output/` is the human edit surface. Cut a claim, add a source, sharpen the thesis. The script stage reads whatever is there.
