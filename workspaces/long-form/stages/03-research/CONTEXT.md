# Stage 03: Research

Produce the deep brief for the episode and, when it touches the Spark, the experiment plan the capture stage will run.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../02-ideas/output/[date]-ideas.md` | "Pick", "Keyword notes", `[date]-picks.md` if present | Road, keyword, swap instructions |
| Hub note | `../../videos/[slug].md` | Frontmatter | Slug, series, value types |
| User notes | `../../input/` | The note the pick came from, if any | Primary source for the creator's own work |
| Skill | `../../../../skills/blai-research/SKILL.md` | Full file | Fan-out method, FireCrawl usage, brief layout |
| Skill rule | `../../../../skills/blai-research/rules/citation-rules.md` | Full file | Source tiers |
| Skill rule | `../../../../skills/dgx-capture/rules/experiment-plan-format.md` | Full file | Shape of the experiment plan |
| Skill rule | `../../../../skills/dgx-capture/rules/allowlist.md` | "Families" | Only allowlisted command families may be planned |
| Brand vault | `../../../../brand-vault/identity.md` | "Audience", "Channel Facts" | What viewers know; what hardware we have |
| Reference | `references/episode-research-scope.md` | Full file | Depth and what an episode needs |

## Process

1. Apply any swap in `[date]-picks.md` (new hub note, old one `rejected`). Restate the road in one sentence. **[Checkpoint]** -- confirm or redirect.
2. Run the research method at deep depth (15-25 sources). Numbers verbatim with units; every claim with a fetched URL; unsupported beliefs under Unverified; the input note's numbers marked `source_quality: own-measurement`.
3. If the episode touches the Spark, write `output/[slug]-experiment.md` per experiment-plan-format.md: 3-8 commands, each with id, timeout, what it proves and how to parse it; every command from an allowlisted family. Otherwise write nothing and say so in the brief.
4. Write `output/[slug]-brief.md` and `output/[slug]-brief.json`; run `validate_research.py`.
5. Run the audit checks below. If any fail, revise before saving.
6. Update the hub note (`status: researched`, Artifacts links).
7. Unattended: `../../../../tools/git-sync.sh "long-form: [slug] research"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | The road in one sentence and the slug | Confirm or redirect |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Validator | `validate_research.py` exits 0 |
| Depth | 15 or more sources; 10 or more claims; 6 or more key numbers |
| Plan | every planned command's first token is in the allowlist families; every command has a timeout and a parse rule |
| Road | the brief's suggested outline has at least three chapters that match the road |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Brief | `output/[slug]-brief.md`, `output/[slug]-brief.json` | per the research skill |
| Experiment plan | `output/[slug]-experiment.md` | per dgx-capture rules (optional) |

The brief and the experiment plan are the human edit surface. Add a command, cut a claim. The outline stage and the capture stage read whatever is there.
