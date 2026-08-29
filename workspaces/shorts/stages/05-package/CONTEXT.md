# Stage 05: Package

Turn the finished script into everything the upload needs: titles, description, hashtags, flags and the publish manifest.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../04-script/output/[slug]-script.md` | Header, "Script", "Notes for review" | What the video says and promises |
| Previous stage | `../04-script/output/[slug]-storyboard.json` | `hook_text`, `target_duration_s`, `script_format` | Physics for the rubric |
| Hub note | `../../videos/[slug].md` | Frontmatter | Slug, pillar, value types |
| Playbook | `../../../../shared/playbook/titles-descriptions.md` | Full file | Title and description rules |
| Playbook | `../../../../shared/playbook/hashtags-tags.md` | Full file | Hashtag and tag rules |
| Playbook | `../../../../shared/playbook/compliance.md` | Full file | Flags and the original-insight statement |
| Playbook | `../../../../shared/playbook/seo-rubric.md` | Full file | The score gate |
| Playbook | `../../../../shared/playbook/publish-timing.md` | "Defaults" | Slot hint |
| Brand vault | `../../../../brand-vault/voice-rules.md` | "Hard Constraints" | No hype in titles either |
| Reference | `references/package-format.md` | Full file | Layout and the manifest block |
| Archive | `../../published/` | Frontmatter titles and URLs | Closest related video for the description; no duplicate titles |

## Process

1. Write three titles (one searchable, two intriguing), each naming the product; pick one and tag its type.
2. Write the description (first 150 characters: keyword and promise; a related-video or channel line; 2-3 hashtags), the tags list, category `28`, the flags (`notify_subscribers: false`, `made_for_kids: false`, `contains_synthetic_media` per compliance.md) and the `original_insight` sentence.
3. Score with seo-rubric.md and revise until the score is 80 or higher. **[Checkpoint]** -- present titles, description and score.
4. Write `output/[slug]-package.md` with the manifest block; run `python3 ../../../../tools/check_outputs.py`.
5. Run the audit checks below. If any fail, revise before saving.
6. Update the hub note: `title`, `seo_score`, `status: ready-to-build`, Artifacts link.
7. Unattended: `../../../../tools/git-sync.sh "shorts: [slug] package" workspaces/shorts skills/render-shorts/styles/history.json`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | Three titles with the pick, the description, the rubric score | Choose a title or redirect |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Rubric | score 80 or higher with every row scored |
| Limits | title 100 characters or fewer with the keyword in the first 40; description 5,000 bytes or fewer; 2-3 hashtags; tags 500 characters or fewer |
| Schema | `check_outputs.py` exits 0 |
| Compliance | `contains_synthetic_media` justified in one line; `original_insight` is specific to this video |
| No duplicate | the title differs from every title in `published/` |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Package | `output/[slug]-package.md` | per package-format.md, with a fenced `json` manifest block |

The package note is the human edit surface and the last cloud stop. Edit the title or description; the build agent reads whatever is there when it publishes.
