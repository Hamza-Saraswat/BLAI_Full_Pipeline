# Stage 08: Publish

Schedule the approved Short on YouTube through Blotato and record where it went. Mechanical: the build agent runs this stage when the hub status is `approved`.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../05-package/output/[slug]-package.md` | The fenced `json` manifest block | Everything the upload needs |
| Build dir | `[build-dir]/[slug]/render/final.mp4` | The approved file | What is uploaded |
| Hub note | `../../videos/[slug].md` | `status`, `feedback` | Must be `approved` |
| Skill | `../../../../skills/blotato-publish/SKILL.md` | Full file | Commands, slots, status polling |
| Skill rule | `../../../../skills/blotato-publish/rules/status-and-errors.md` | Full file | Retries and failure handling |
| Playbook | `../../../../shared/playbook/publish-timing.md` | "Defaults" | Slot rules |
| Skill | `../../../../skills/telegram-gate/SKILL.md` | "checklist" card | Post-publish reminders |
| Reference | `references/publish-note-format.md` | Full file | Layout of the publish note |

## Process

1. Confirm the hub status is `approved` and the manifest validates (`python3 ../../../../tools/check_outputs.py`).
2. Run `publish.py --package [package] --video [final.mp4] --slot auto` (privacy from `BLAI_PUBLISH_PRIVACY`).
3. Write `output/[slug]-publish.md`; update the hub (`status: scheduled`, `blotato_post_id`, `publish_slot`); create `../../published/[slug].md` per publish-note-format.md.
4. Send `send_card.py --kind checklist --hub [hub]`.
5. Run the audit checks below. If any fail, set the hub note to `blocked` with the reason.
6. `../../../../tools/git-sync.sh "shorts: [slug] publish" workspaces/shorts skills/render-shorts/styles/history.json`.
7. On later runs: `publish.py --status [id]`; when published, set `status: published` and `youtube_url` in the hub note and the published note.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Accepted | Blotato returned 201 with a post submission id |
| Slot | the scheduled time is a valid slot at least 30 minutes ahead |
| Records | hub note, publish note and published note agree on ids and slot |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Publish note | `output/[slug]-publish.md` | post id, slot, media url, privacy |
| Published note | `../../published/[slug].md` | frontmatter for dedupe and analytics |

The published note is the last edit surface: add the YouTube URL by hand if the status poll misses it. Loop-back routing for anything wrong lives in `../../../../shared/pipeline-overview.md`.
