# Status, errors and retries

## Response codes from `POST /v2/posts`

| Code | Meaning | What `publish.py` does | What you do |
|------|---------|------------------------|-------------|
| 200 / 201 | accepted; body carries `postSubmissionId` | prints `{post_submission_id, scheduled_time, media_url, thumbnail_url}` | set the hub note `status=scheduled`, `blotato_post_id`, `publish_slot` |
| 400 | validation error (title too long, missing `privacyStatus`, bad `scheduledTime`, media URL not fetchable) | exits 1, prints the first 400 bytes of the error | fix the package note or the R2 public URL, rerun |
| 401 | bad or missing `blotato-api-key` | exits 1 | check `BLOTATO_API_KEY` in `build/.env` |
| 403 | account not connected, plan limit, or YouTube token expired on Blotato's side | exits 1 | reconnect the channel in Blotato, check `--accounts` |
| 404 | unknown id (status) or wrong path | exits 1 | for `--status`, confirm `STATUS_PATH` in `publish.py` against the Blotato docs ("Get Post Status") |
| 413 | media too large for the plan | exits 1 | re-encode; a Short should be well under 100 MB |
| 429 | rate limit, 30 requests per minute per key | waits `Retry-After` or 2, 4, 8, 16, 32 s and retries, 5 attempts | nothing; if it persists, another process is polling too fast |
| 5xx | Blotato outage | same backoff, 5 attempts | wait; the slot still holds if it is more than 30 minutes away, otherwise rerun with `--slot auto` |

After five failed attempts the script exits 1. The R2 objects stay in place so a rerun does not re-upload by accident; rerun with the same flags (the upload overwrites the same key).

## `--status ID`

`GET /v2/posts/{id}` (constant `STATUS_PATH`). Output is normalized to `{post_submission_id, status, youtube_url, error, raw}`:

- `status` is Blotato's value lowercased (`scheduled`, `pending`, `published`, `failed` or whatever the API returns; `raw` keeps the original).
- `youtube_url` is filled from the first URL-looking field once the video exists; empty before that.
- Exit 0 means the poll worked, not that the post succeeded; read `status`.

Polling rule: once every 10 minutes until `status` is `published` or a failure value, never more than once every 2 seconds (the 30 per minute limit is shared by every script using the key). The build agent sets `status=published` and `youtube_url` in the hub note when it sees the URL, then sends the Telegram checklist card.

## `--accounts`

`GET /v2/users/me/accounts` printed as `[{id, platform, name}]`. Run it once after connecting the channel and put the YouTube id in `BLOTATO_YOUTUBE_ACCOUNT_ID`.

## On failure, in the pipeline

1. The publish stage sets the hub note `status=blocked` with `blocked_reason` = the first error line, and sends the blocked card (`skills/telegram-gate`).
2. Retry from Telegram puts the note back to `ready-to-build`; the build agent reruns only the publish stage (video and package note are unchanged).
3. If the post was accepted but the status later reports failure, the hub goes back to `approved` with the Blotato error in `feedback`, and the next run schedules a new slot.

## Privacy and first-post check

Keep `BLAI_PUBLISH_PRIVACY=private` until one post is verified end to end in YouTube Studio (title, description, synthetic-media flag, Shorts shelf). Then set it to `public`; the manifest's `privacy_status` only applies when the env value is empty.

## Cleanup

Delete preview objects a week after `published` with `r2.py delete --key previews/<slug>/final.mp4` (the weekly retro can batch this). Never delete before Blotato reports `published`.
