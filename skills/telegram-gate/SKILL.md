---
name: telegram-gate
description: The one-tap human gate. Sends Telegram cards (ideas FYI, approval gate with preview, blocked, post-publish checklist) and runs the bot that turns button taps into hub-note status changes, feedback and commits.
metadata:
  tags: "telegram, approval, gate, bot, notifications"
---

# Telegram gate

## When to Use

- A render stage finished and the hub note is `review`: send the gate card with the preview.
- A Spark stage blocked after retries: send the blocked card so Retry is one tap away.
- Blotato reported `published`: send the checklist of Studio-only tasks with the YouTube URL.
- The morning ideas routine wants a heads-up with swap buttons, or any stage wants a free-text notice.
- Running the bot itself (`bot.py`) as the `blai-telegram-bot` user service on the Spark.

Not for: chatting with the bot, or approving anything outside the status machine in `shared/pipeline-overview.md`.

## What You Need Before Calling

- `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in `build/.env` (Spark) or the cloud environment; `ROUTINE_RESCRIPT_URL` and `ROUTINE_RESCRIPT_TOKEN` for the re-script trigger (optional: without them the bot journals the request instead).
- The hub note path `workspaces/<ws>/videos/<slug>.md` (its `title`, `format`, `structure`, `style_pack`, `seo_score`, `preview_url`, `youtube_url`, `blocked_reason` fill the cards) and, for the gate, `final.mp4` or a preview URL; the package note linked from the hub supplies the original insight.
- For the ideas card, `<date>-ideas.md` with ranked `## N. Title` headings (format in `rules/cards.md`).
- `ffprobe` on PATH if the gate card should show the duration from the video.

## How It Works

1. `scripts/send_card.py --kind gate --hub FILE.md --video final.mp4` renders the card from `rules/cards.md`, attaches the video with `sendVideo` when it is under 48 MB (else links `--preview-url` or the hub's `preview_url`), adds the Approve / Reject / Re-render / Re-script keyboard, stores the message id in `build/state/telegram-messages.json` and prints `{"message_id": N}`. Other kinds: `fyi-ideas --ideas FILE.md` (Swap 1-5), `blocked --text "<stage>: <reason>"` (Retry), `checklist` (no buttons), `text --text "..."`.
2. `scripts/bot.py` long-polls `getUpdates` (`timeout=30`, `allowed_updates` message and callback_query), answers each tap, removes the keyboard, and applies the action from `rules/callbacks.md`: approve sets `status=approved` with an `approved_at` journal line; reject sets `rejected` and stores the next text message as `feedback`; rerender sets `ready-to-build` with `feedback=re-render`; rescript sets `rejected`, waits for feedback, then POSTs `{"text": "rescript <slug>: <feedback>"}` to the routine trigger; retry sets `ready-to-build`; swap writes `<date>-picks.md`.
3. After every hub change the bot runs `tools/git-sync.sh "telegram: <slug> <action>"`, so the Spark build loop and the cloud routines see the decision on their next pull.
4. State lives in `build/state/telegram-state.json` (offset, pending feedback); `--once` handles one poll for cron use; the default loops with backoff.
5. `--dry-run` on both scripts makes no network call: `send_card.py` prints the rendered text and keyboard; `bot.py` replays `fixtures/updates.json` against `--repo` and prints one JSON line per update.

Examples: `python3 skills/telegram-gate/scripts/send_card.py --kind gate --hub workspaces/shorts/videos/<slug>.md --video builds/<slug>/render/final.mp4` and `python3 skills/telegram-gate/scripts/bot.py --once`.

## Rules

- `rules/cards.md`: the exact text layout, inputs and button rows of every card kind, plus Telegram limits.
- `rules/callbacks.md`: the callback grammar, what each tap changes in the hub note, journal lines, commit messages, state files and safety checks.

## After the Call

- The render stage sets the hub note `status=review` only after `send_card.py` returned a message id; if it fails, the stage stays `building` and retries on the next loop.
- The build loop watches for `approved` (publish), `ready-to-build` (re-render or retry) and `rejected` with `feedback` (a re-script run reads it).
- The approve journal line is the human sign-off required by `shared/playbook/compliance.md`; never set `approved` by hand without a journal line.
- Keep `build/state/` out of git (already ignored) and back it up with the Spark's other runtime state.
