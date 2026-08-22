# Callbacks

Grammar: `<action>:<slug>` for video cards and `swap:<date>:<n>` for the ideas card. Slugs are `YYYY-MM-DD-topic-slug` (lowercase, digits, hyphens); anything else is answered with "unknown button" and ignored. Only the chat in `TELEGRAM_CHAT_ID` is served.

## What the bot does on every tap

1. `answerCallbackQuery` (stops the spinner).
2. `editMessageReplyMarkup` with an empty keyboard on the tapped message, plus any other gate, blocked or ideas card stored for the same key in `build/state/telegram-messages.json`.
3. Finds the hub note by slug across both workspaces (`workspaces/*/videos/<slug>.md`) and applies the action below with `tools/hubnote.py` (`update`, `append_section`).
4. Runs `tools/git-sync.sh "telegram: <slug> <action>"` (skipped in `--dry-run`).
5. Sends a one-line confirmation message.

## Actions

| Callback | Hub note change | Journal line | Commit message |
|----------|-----------------|--------------|----------------|
| `approve:<slug>` | `status=approved`, `feedback` cleared | `telegram approve (approved_at <ts>)` (the compliance sign-off record) | `telegram: <slug> approve` |
| `reject:<slug>` | `status=rejected`; bot remembers "awaiting feedback for slug" | `telegram reject; awaiting feedback` | `telegram: <slug> reject` |
| next text message after reject | `feedback=<text>` | `telegram feedback: <text>` | `telegram: <slug> feedback` |
| `rerender:<slug>` | `status=ready-to-build`, `feedback=re-render` | `telegram re-render requested` | `telegram: <slug> rerender` |
| `rescript:<slug>` | `status=rejected`; awaiting feedback | `telegram re-script requested; awaiting feedback` | `telegram: <slug> rescript` |
| next text message after rescript | `feedback=<text>`, then `POST ROUTINE_RESCRIPT_URL` with `{"text": "rescript <slug>: <feedback>"}` and `Authorization: Bearer ROUTINE_RESCRIPT_TOKEN` | `telegram feedback: ...` then `re-script trigger posted (HTTP 200)` or `ROUTINE_RESCRIPT_URL unset; journaled only` | `telegram: <slug> feedback` |
| `retry:<slug>` | `status=ready-to-build`, `blocked_reason` cleared | `telegram retry` | `telegram: <slug> retry` |
| `swap:<date>:<n>` (n = 3..5) | appends `- <ts> swap pick 2 for idea <n>` to `workspaces/<ws>/stages/02-ideas/output/<date>-picks.md`, where `<ws>` is the workspace holding `<date>-ideas.md` (falls back to `shorts`) | none (no hub yet) | `telegram: ideas <date> swap <n>` |
| `swap:<date>:1` or `:2` | nothing; answered "already a pick" | none | none |

Reply `skip` (or `-`, `none`) to a feedback request to continue without feedback; for a re-script that posts the trigger with `(no feedback)`. A pending feedback request survives restarts (it is in the state file) and is replaced by the next reject or rescript tap.

## State

`build/state/telegram-state.json`: `{"offset": <next update_id>, "pending_feedback": {"slug", "action", "since"} | null, "last_update_at"}`. The offset is advanced before each update is handled, so a crashing update is not replayed forever. Delete the file to re-read the last 24 hours of updates (Telegram keeps them); the hub changes are idempotent enough for that (a second approve re-journals, nothing else).

`build/state/telegram-messages.json`: `{"<slug>": [{"message_id", "kind", "chat_id", "sent_at"}]}`, written by `send_card.py` and drained by the bot when it clears keyboards.

Both files are gitignored (`build/state/`).

## Running it

- Service: `build/systemd/blai-telegram-bot.service` runs `bot.py` (no flags) as a user unit; it long-polls with `timeout=30` and backs off 5 s to 120 s on errors.
- Cron style: `bot.py --once` handles one poll and exits.
- Local check: `bot.py --dry-run --repo skills/telegram-gate/fixtures/repo` (copy the fixture tree first if you want to keep it pristine) prints one JSON line per fixture update and edits the fixture hub note; nothing is sent or committed.

## Safety

- The bot token never appears in logs; API errors are sanitised before printing.
- Only `message` and `callback_query` updates are requested (`allowed_updates`).
- A tap from another chat is answered with "not your chat" and ignored.
- Hub notes are the only files the bot edits, plus the picks note; it never touches stage outputs.
