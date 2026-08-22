# Manifest mapping

`publish.py` reads the ```json block of `<slug>-package.md` (shape: `shared/schemas/publish-manifest.schema.json`), validates it, and maps it onto Blotato's `POST /v2/posts`. The same fields map onto a future direct uploader (`videos.insert`), so the package stage never changes when the transport does.

## Field by field

| Manifest field | Blotato `POST /v2/posts` | Direct YouTube Data API (future) |
|----------------|--------------------------|----------------------------------|
| `slug` | R2 keys `previews/<slug>/final.mp4` and `previews/<slug>/thumbnail.<ext>` | local file paths |
| `format` | slot rule in `slots.py` (Shorts 11:00/18:00, long-form 09:00); Shorts must be vertical and under 3 min or YouTube lists them as regular videos | no field; YouTube classifies Shorts by aspect ratio and length |
| `title` (<= 100 chars) | `post.target.title` | `snippet.title` |
| `title_variants` | not sent; used by the reviewer in Studio "Test & Compare" (no API) | not sent |
| `description` | `post.content.text`, with chapters, the related long-form URL and the hashtags appended when they are not already in it; total <= 5,000 bytes | `snippet.description` |
| `hashtags` (1-3) | appended as the last line of the text | part of the description |
| `tags` | not supported by Blotato (research 1.7) | `snippet.tags` |
| `category_id` (default 28) | not supported | `snippet.categoryId` |
| `default_language` | not supported | `snippet.defaultLanguage` |
| `privacy_status` | `post.target.privacyStatus`; precedence `--privacy`, then `BLAI_PUBLISH_PRIVACY`, then the manifest | `status.privacyStatus` |
| `notify_subscribers` | `post.target.shouldNotifySubscribers` (false for Shorts, true for long-form per `shared/playbook/compliance.md`) | `notifySubscribers` request parameter |
| `made_for_kids` (always false) | `post.target.isMadeForKids: false` | `status.selfDeclaredMadeForKids` |
| `contains_synthetic_media` | `post.target.containsSyntheticMedia` | `status.containsSyntheticMedia` |
| `playlist_ids` | `post.target.playlistIds` | `playlistItems.insert` per id |
| `thumbnail` (relative to the package note) or `--thumbnail` | uploaded to R2, then `post.target.thumbnailUrl` | `thumbnails.set` |
| `chapters` (`[{time, label}]`) | appended to the text as a "Chapters" block (first chapter must be `00:00`, at least three, for YouTube to render them) | description |
| `publish_slot_hint` | `scheduledTime` when it is still more than 30 minutes away; otherwise the next free slot | `status.publishAt` with `privacyStatus: private` |
| `related_long_form_url` | appended as `Full video: <url>` | description; the Shorts "related video" link is Studio-only |
| `original_insight`, `seo_score`, `reviewer_notes` | not sent; they are the compliance record in the package note | not sent |

## Fixed values

- `post.accountId` = `BLOTATO_YOUTUBE_ACCOUNT_ID` (find it with `publish.py --accounts`).
- `post.content.platform` = `youtube`, `post.target.targetType` = `youtube`.
- `post.content.mediaUrls` = `[<R2 public URL of final.mp4>]`. Blotato fetches the file from that URL when it posts, so the object must stay public until the status is `published`.
- `scheduledTime` is ISO-8601 with an offset (for example `2026-08-25T18:00:00-05:00`), never naive.

## Validation before any upload

1. Every `required` key of the schema is present; enums, `maxLength`, `minItems`, `maxItems`, `pattern`, `const` and `minimum`/`maximum` are checked field by field.
2. Title <= 100 characters, hashtags <= 3, `made_for_kids` false, slug lowercase-with-hyphens.
3. The composed description (after chapters, related URL and hashtags) <= 5,000 bytes UTF-8.
4. Thumbnail over 2 MB logs a warning (YouTube's limit); the video file must exist.

A failed validation exits 1 and uploads nothing; fix the package note, not the script.

## Slot selection

`--slot ISO` wins; else a future `publish_slot_hint`; else `slots.next_slot(format, now)` skipping every `publish_slot` already written in `workspaces/*/videos/*.md` (other slugs only), so two Shorts approved the same day take 11:00 and 18:00 in order and a third rolls to the next day. The lead of 30 minutes gives Blotato time to fetch and process the media.
