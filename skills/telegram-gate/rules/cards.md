# Cards

Every card is one Telegram message (`parse_mode=HTML`, values escaped) with an inline keyboard. `scripts/send_card.py` renders them exactly as below; `scripts/bot.py` reads the buttons. Message ids are stored in `build/state/telegram-messages.json` keyed by slug (ideas cards: `ideas:<date>`) so the bot can clear stale keyboards. No emoji.

## fyi-ideas (morning, from the cloud routine)

Input: `--ideas workspaces/<ws>/stages/02-ideas/output/<date>-ideas.md`. The parser expects ranked ideas as `## N. Title` headings (or `N. **Title**` list items) followed by label lines `- angle: ...`, `- why now: ...`, optional `- format: ...`; without labels the first body line is the angle and the second the why-now. The first five ranks are shown.

```
<b>Ideas for 2026-08-25</b> (shorts)
Default picks: 1 and 2. Tap Swap n to put idea n in pick 2.

1. <b>Title</b> [format]
angle
<i>why now:</i> reason

2. ...
```

Buttons, one row: `Swap 1` ... `Swap 5` with callback `swap:<date>:<n>`. Swap 1 and Swap 2 answer "already a pick" and change nothing.

## gate (after render, status `review`)

Input: `--hub` plus `--video final.mp4` (attached with `sendVideo` when under 48 MB) or `--preview-url`. Duration comes from `--duration-s` or ffprobe on the video; the insight comes from the package note linked in the hub's Artifacts list (or `--package`).

```
<b>Gate: Title</b>
2026-08-25-topic-slug
format: short | duration: 48 s | structure: myth-bust
style: neon-grid | seo: 82
insight: the original_insight sentence from the manifest
preview: https://...        (only when the video is not attached)
```

Buttons, two rows: `Approve` `Reject` / `Re-render` `Re-script` with callbacks `approve:<slug>`, `reject:<slug>`, `rerender:<slug>`, `rescript:<slug>`. Sending a new gate card clears the keyboard of the previous gate or blocked card for the same slug. Captions are capped at 1,024 characters by Telegram; the card stays well under it.

## blocked (a Spark stage failed after retries)

Input: `--hub` and `--text "<stage>: <reason>"` (falls back to the hub's `blocked_reason`).

```
❌ <b>Build failed: Title</b>
Render stage: scene s03 did not pass safe_zone_check after 5 rounds: text inside the right rail
Next: the next build pass retries it on its own (08:35, 10:35, 12:35 CT). Tap Retry to queue it now.
<i>2026-08-25-topic-slug</i>
```

The stage prefix (`07-render:`) becomes a word; the reason is one human sentence (the
scripted render writes it from the worker's handback, never a JSON dump: 2026-09-06).
Button: `Retry` with callback `retry:<slug>`.

## checklist (after Blotato reports published)

Input: `--hub` (uses `youtube_url`, `title`, `format`); `--preview-url` overrides the URL.

```
<b>Published: Title</b>
https://www.youtube.com/...
Studio tasks (no API exists for these):
1. Pin a comment
2. End screen and cards
3. Add the related-video link
4. Community post
```

No buttons. Source of the task list: research section 5.3.

## text

`--text "..."` sent as escaped plain text (no buttons). Use it for morning summaries and one-off notices. With `--hub` the message id is stored under that slug.

## Limits and behaviour

- `sendMessage` text is cut at 4,096 characters, captions at 1,024; the ideas card with five long ideas is the only one that can get close.
- `disable_web_page_preview` is on except for gate links and checklist URLs.
- Rate limits (429) are honoured with the `retry_after` the API returns.
- `--dry-run` prints the rendered text and keyboard with `message_id: 0` and sends nothing.
