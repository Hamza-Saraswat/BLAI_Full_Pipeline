# Stage 07: Package

Turn the script and spec into titles, a description with chapters, flags and the publish manifest.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../05-script/output/[slug]-script.md` | Header, chapter labels, "Notes for review" | What the episode says |
| Previous stage | `../06-spec/output/[slug]-spec.json` | `chapters`, `scenes[].est_duration_s`, `thumbnail_concepts` | Estimated chapter times and thumbnail text |
| Hub note | `../../videos/[slug].md` | Frontmatter | Slug, series, value types |
| Playbook | `../../../../shared/playbook/titles-descriptions.md` | Full file | Title and description rules |
| Playbook | `../../../../shared/playbook/hashtags-tags.md` | Full file | Hashtag and tag rules |
| Playbook | `../../../../shared/playbook/thumbnails.md` | "Long-form" | Thumbnail text rules |
| Playbook | `../../../../shared/playbook/compliance.md` | Full file | Flags and the original-insight statement |
| Playbook | `../../../../shared/playbook/seo-rubric.md` | Full file | The score gate |
| Playbook | `../../../../shared/playbook/publish-timing.md` | "Defaults" | Slot hint |
| Reference | `references/package-format.md` | Full file | Layout and the manifest block with chapters |
| Archive | `../../published/` | Frontmatter titles | No duplicate titles; related episodes |

## Process

1. Write three titles (one searchable, two intriguing) naming the product or project; pick one.
2. Write the description: first 150 characters carry the keyword and the promise; 2-4 sentences; the chapters block with estimated times from the spec (`00:00` first, ascending, 10 s or more apart); links and credits; 2-3 hashtags. Tags list, category `28`, `notify_subscribers: true`, `made_for_kids: false`, `contains_synthetic_media` per compliance.md, `original_insight`.
3. Score with seo-rubric.md; revise until 80 or higher. **[Checkpoint]** -- present titles, description and score.
4. Write `output/[slug]-package.md` with the manifest block; run `python3 ../../../../tools/check_outputs.py`.
5. Run the audit checks below. If any fail, revise before saving.
6. Update the hub (`title`, `seo_score`, `status: ready-to-build`, Artifacts link).
7. Unattended: `../../../../tools/git-sync.sh "long-form: [slug] package"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | Three titles with the pick, the description, the rubric score | Choose a title or redirect |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Rubric | score 80 or higher with every row scored |
| Chapters | `00:00` first, at least 3, ascending, 10 s or more apart, labels match the script's chapter labels |
| Limits | title 100 characters or fewer, keyword in the first 40; description 800-2,000 characters and 5,000 bytes or fewer; 2-3 hashtags |
| Schema | `check_outputs.py` exits 0 |
| Compliance | flags justified; `original_insight` specific to this episode |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Package | `output/[slug]-package.md` | per package-format.md with a fenced `json` manifest block |

The package note is the human edit surface and the last cloud stop. The render stage replaces the chapter times with measured ones; the build agent reads whatever is there when it publishes.
