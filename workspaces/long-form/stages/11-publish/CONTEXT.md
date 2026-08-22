# Stage 11: Publish

Schedule the approved episode on YouTube through Blotato with its thumbnail and measured chapters; record where it went. Mechanical: the build agent runs it when the hub status is `approved`.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../07-package/output/[slug]-package.md` | The fenced `json` manifest block | Everything the upload needs |
| Build dir | `[build-dir]/[slug]/render/` | final.mp4, thumbnails, chapters.json | What is uploaded |
| Hub note | `../../videos/[slug].md` | `status`, `thumbnail_pick` | Must be `approved`; which still |
| Skill | `../../../../skills/blotato-publish/SKILL.md` | Full file | Commands, slots, status polling |
| Skill rule | `../../../../skills/blotato-publish/rules/status-and-errors.md` | Full file | Retries and failures |
| Playbook | `../../../../shared/playbook/publish-timing.md` | "Defaults" | Long-form slot rule |
| Skill | `../../../../skills/telegram-gate/SKILL.md` | "checklist" card | Studio tasks the API cannot do |
| Reference | `references/publish-note-format.md` | Full file | Layout of the publish and published notes |

## Process

1. Confirm `status: approved` and that the manifest validates (`check_outputs.py`).
2. Run `publish.py --package [package] --video [final.mp4] --thumbnail [thumbnails/N.png] --chapters [chapters.json] --slot auto`.
3. Write `output/[slug]-publish.md`; update the hub (`status: scheduled`, `blotato_post_id`, `publish_slot`); create `../../published/[slug].md`.
4. Send `send_card.py --kind checklist --hub [hub]` (end screens, cards, pinned comment, Test & Compare thumbnails, the Shorts related-video links).
5. Run the audit checks below. If any fail, set the hub note to `blocked`.
6. `../../../../tools/git-sync.sh "long-form: [slug] publish"`.
7. Later runs poll `publish.py --status [id]` and set `status: published` and `youtube_url`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Accepted | Blotato returned 201 with a post submission id |
| Chapters | the uploaded description carries the measured chapter block, `00:00` first |
| Thumbnail | the chosen still was sent as `thumbnailUrl` |
| Records | hub note, publish note and published note agree |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Publish note | `output/[slug]-publish.md` | post id, slot, media and thumbnail urls |
| Published note | `../../published/[slug].md` | frontmatter for dedupe and analytics |

The published note is the last edit surface. Loop-back routing lives in `../../../../shared/pipeline-overview.md`.
