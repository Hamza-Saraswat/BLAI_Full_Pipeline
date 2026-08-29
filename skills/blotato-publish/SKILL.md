---
name: blotato-publish
description: Schedule an approved video on YouTube through Blotato, mapping the package note's manifest onto the API, hosting the media on Cloudflare R2, and picking the publish slot from the posting playbook.
metadata:
  tags: "publish, youtube, blotato, r2, scheduling"
---

# Blotato publish

## When to Use

- The publish stage (Shorts stage 08) on the DGX Spark, after the hub note reached `approved` through the Telegram gate.
- Polling a scheduled post until YouTube has it (`--status`), or listing the connected accounts once during setup (`--accounts`).
- Computing a slot for planning (`slots.py`) without posting anything.

Not for: uploading drafts for review (the gate card links the R2 preview directly), or anything on a hub note that is not `approved`.

## What You Need Before Calling

- `build/.env` with `BLOTATO_API_KEY`, `BLOTATO_YOUTUBE_ACCOUNT_ID`, `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`, `R2_PUBLIC_BASE_URL`, and `BLAI_PUBLISH_PRIVACY` (`private` until the first post is verified).
- The package note `<slug>-package.md` with a manifest that follows `shared/schemas/publish-manifest.schema.json` and the rendered `final.mp4` that passed the lint scripts.
- `boto3` installed (`pip install boto3`); `python-dotenv` optional.
- The approval time (now) and, for a Short, awareness that two Shorts a day fill 11:00 and 18:00 CT in order.

## How It Works

1. `scripts/publish.py --package FILE-package.md --video final.mp4 [--slot auto|ISO] [--privacy ...]` parses the manifest and validates it (schema checks, title <= 100 chars, <= 3 hashtags, description <= 5,000 bytes after hashtags); any error exits 1 before an upload.
2. The video goes to R2 with `scripts/r2.py` under `previews/<slug>/`; the public URL becomes `mediaUrls[0]`.
3. The slot is `--slot ISO`, else a still-future `publish_slot_hint`, else `scripts/slots.py` (11:00/18:00 CT, 30 minutes minimum lead, slots already in hub notes skipped).
4. The body is built exactly as `rules/manifest-mapping.md` describes and sent to `POST https://backend.blotato.com/v2/posts` with the `blotato-api-key` header; 429 and 5xx retry with exponential backoff (5 attempts).
5. stdout gets `{post_submission_id, scheduled_time, media_url, thumbnail_url}`; `--dry-run` prints the same plus the exact `body` without touching the network.
6. `publish.py --status ID` prints `{post_submission_id, status, youtube_url, error, raw}`; `publish.py --accounts` prints `[{id, platform, name}]`.

Examples: `python3 skills/blotato-publish/scripts/publish.py --package workspaces/shorts/stages/05-package/output/<slug>-package.md --video builds/<slug>/render/final.mp4` and `python3 skills/blotato-publish/scripts/slots.py --format long --after 2026-08-29T20:00:00-05:00`.

## Rules

- `rules/manifest-mapping.md`: every manifest field, where it lands in the Blotato body, and where it will land in a direct `videos.insert` call later.
- `rules/status-and-errors.md`: response codes, the retry policy, the 30 per minute limit, status polling, and what the pipeline does on failure.

## After the Call

- Set the hub note: `status=scheduled`, `blotato_post_id=<post_submission_id>`, `publish_slot=<scheduled_time>`, and append a build-journal line (`tools/hubnote.py`).
- Write `<slug>-publish.md` in the stage output with the slot, the media URL, the privacy used and the manifest as sent (without any key).
- Poll `--status` every 10 minutes; on `published` set `status=published` and `youtube_url`, move the hub note's summary into `published/`, and send the Telegram checklist card for the Studio-only tasks.
- Keep the R2 object until the status is `published`; clean up a week later with `r2.py delete`.
