#!/usr/bin/env python3
"""Telegram gate bot: long-poll getUpdates, answer button taps, update hub notes, commit.

Usage:
  bot.py [--once] [--timeout 30] [--repo DIR] [--dry-run [--updates FILE.json]]

Callbacks (rules/callbacks.md):
  approve:<slug>   hub status=approved, journal line with approved_at
  reject:<slug>    hub status=rejected; the next text message becomes the hub's feedback
  rerender:<slug>  hub status=ready-to-build, feedback=re-render
  rescript:<slug>  hub status=rejected; after the feedback message, POST {"text": "rescript <slug>: <feedback>"}
                   to ROUTINE_RESCRIPT_URL (Bearer ROUTINE_RESCRIPT_TOKEN); journal only when unset.
                   Hermes deployment (2026-09): the URL stays unset; the 08:30 CT produce cron job
                   rescans hubs at status rejected with feedback and re-runs stages 04-05 for them.
  retry:<slug>     hub status=ready-to-build, blocked_reason cleared
  swap:<date>:<n>  append "swap pick 2 for idea n" to workspaces/<ws>/stages/02-ideas/output/<date>-picks.md
Every hub change runs tools/git-sync.sh "telegram: <slug> <action>" (skipped in --dry-run).
State (update offset, pending feedback) lives in build/state/telegram-state.json; message ids written by
send_card.py in build/state/telegram-messages.json are used to clear stale keyboards.
--once processes one poll and exits (cron style); the default loops forever with backoff on errors.
--dry-run: no network, no git; updates come from --updates (default fixtures/updates.json) and hub notes
under --repo are edited so the effect can be inspected; state is not saved. One JSON line per update on
stdout. Env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, ROUTINE_RESCRIPT_URL, ROUTINE_RESCRIPT_TOKEN. Exit 0/1.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import tgapi  # noqa: E402

ACTIONS = ("approve", "reject", "rerender", "rescript", "retry", "swap")
FEEDBACK_SKIP_WORDS = ("skip", "-", "none", "no feedback")


def log(msg: str) -> None:
    tgapi.log(msg, "bot")


class Bot:
    def __init__(self, repo: pathlib.Path, tg: tgapi.Telegram, dry_run: bool):
        self.repo = repo
        self.tg = tg
        self.dry_run = dry_run
        self.hn = tgapi.hubnote()
        self.state_path = tgapi.state_dir(repo) / tgapi.STATE_FILE
        self.state = tgapi.read_json(self.state_path, {"offset": 0, "pending_feedback": None, "last_update_at": ""})

    # ----------------------------------------------------------------- plumbing

    def save_state(self) -> None:
        if self.dry_run:
            return
        self.state["last_update_at"] = tgapi.now_iso()
        tgapi.write_json_atomic(self.state_path, self.state)

    def git_sync(self, message: str) -> None:
        if self.dry_run:
            log("dry run: skip git-sync %r" % message)
            return
        script = self.repo / "tools" / "git-sync.sh"
        if not script.exists():
            log("no tools/git-sync.sh under %s; skipping commit" % self.repo)
            return
        try:
            proc = subprocess.run(["bash", str(script), message], cwd=str(self.repo), stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, text=True, timeout=600)
            log("git-sync (%d): %s" % (proc.returncode, proc.stdout.strip()[-300:]))
        except (OSError, subprocess.TimeoutExpired) as e:
            log("git-sync failed: %s" % e)

    def journal(self, hub: pathlib.Path, line: str) -> None:
        self.hn.append_section(hub, "Build journal", line)

    def reply(self, text: str) -> None:
        try:
            self.tg.send_message(tgapi.esc(text))
        except tgapi.TelegramError as e:
            log("reply failed: %s" % e)

    def clear_cards(self, key: str) -> None:
        for old in tgapi.pop_messages(self.repo, key, kinds=("gate", "blocked", "fyi-ideas")) if not self.dry_run else []:
            self.tg.clear_keyboard(old.get("chat_id") or self.tg.chat_id, old.get("message_id"))

    def post_rescript(self, slug: str, feedback: str) -> str:
        url = os.environ.get("ROUTINE_RESCRIPT_URL", "")
        token = os.environ.get("ROUTINE_RESCRIPT_TOKEN", "")
        payload = {"text": "rescript %s: %s" % (slug, feedback or "(no feedback)")}
        if not url:
            return "ROUTINE_RESCRIPT_URL unset; journaled only"
        if self.dry_run:
            log("dry run: would POST %s to the re-script trigger" % json.dumps(payload))
            return "dry run: trigger not posted"
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), method="POST", headers={
            "Content-Type": "application/json", "Authorization": "Bearer %s" % token})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return "re-script trigger posted (HTTP %d)" % resp.status
        except urllib.error.HTTPError as e:
            return "re-script trigger failed: HTTP %d" % e.code
        except urllib.error.URLError as e:
            return "re-script trigger failed: %s" % e.reason

    # ------------------------------------------------------------------ actions

    def act(self, action: str, arg: str, extra: str = "") -> dict:
        if action == "swap":
            return self.act_swap(arg, extra)
        slug = arg
        if not tgapi.SLUG_RE.match(slug):
            return {"ok": False, "note": "bad slug"}
        hub = tgapi.find_hub(self.repo, slug)
        if hub is None:
            return {"ok": False, "note": "hub note not found for %s" % slug}
        stamp = tgapi.now_iso()
        if action == "approve":
            self.hn.update(hub, status="approved", feedback="")
            self.journal(hub, "telegram approve (approved_at %s)" % stamp)
            note = "approved; the publish stage picks the next slot"
        elif action == "reject":
            self.hn.update(hub, status="rejected")
            self.journal(hub, "telegram reject; awaiting feedback")
            self.state["pending_feedback"] = {"slug": slug, "action": "reject", "since": stamp}
            note = "rejected; send feedback as your next message"
        elif action == "rerender":
            self.hn.update(hub, status="ready-to-build", feedback="re-render")
            self.journal(hub, "telegram re-render requested")
            note = "re-render queued"
        elif action == "rescript":
            self.hn.update(hub, status="rejected")
            self.journal(hub, "telegram re-script requested; awaiting feedback")
            self.state["pending_feedback"] = {"slug": slug, "action": "rescript", "since": stamp}
            note = "re-script: send feedback as your next message (or 'skip')"
        elif action == "retry":
            self.hn.update(hub, status="ready-to-build", blocked_reason="")
            self.journal(hub, "telegram retry")
            note = "retry queued"
        else:
            return {"ok": False, "note": "unknown action %s" % action}
        self.clear_cards(slug)
        self.git_sync("telegram: %s %s" % (slug, action))
        return {"ok": True, "hub": str(hub), "note": note}

    def act_swap(self, date: str, n: str) -> dict:
        if not tgapi.DATE_RE.match(date) or not n.isdigit() or not 1 <= int(n) <= 5:
            return {"ok": False, "note": "bad swap data"}
        if int(n) <= 2:
            return {"ok": True, "note": "idea %s is already a pick" % n}
        ideas = tgapi.find_ideas_note(self.repo, date)
        if ideas is None:
            ws_dir = self.repo / "workspaces" / "shorts"
            log("ideas note for %s not found; writing picks under workspaces/shorts" % date)
        else:
            _, ws_dir = tgapi.workspace_of(ideas)
        picks = ws_dir / "stages" / "02-ideas" / "output" / ("%s-picks.md" % date)
        picks.parent.mkdir(parents=True, exist_ok=True)
        if not picks.exists():
            picks.write_text("# Picks for %s\n\nSwaps requested from the Telegram ideas card; the script stage reads the last line.\n\n" % date, encoding="utf-8")
        with picks.open("a", encoding="utf-8") as fh:
            fh.write("- %s swap pick 2 for idea %s\n" % (tgapi.now_iso(), n))
        self.clear_cards("ideas:%s" % date)
        self.git_sync("telegram: ideas %s swap %s" % (date, n))
        return {"ok": True, "picks": str(picks), "note": "pick 2 is now idea %s" % n}

    def apply_feedback(self, text: str) -> dict:
        pending = self.state.get("pending_feedback") or {}
        slug = pending.get("slug", "")
        hub = tgapi.find_hub(self.repo, slug) if slug else None
        if hub is None:
            self.state["pending_feedback"] = None
            return {"ok": False, "note": "pending hub %s not found" % slug}
        skip = text.strip().lower() in FEEDBACK_SKIP_WORDS
        feedback = "" if skip else text.strip()
        if feedback:
            self.hn.update(hub, feedback=feedback)
            self.journal(hub, "telegram feedback: %s" % feedback[:200])
        note = "feedback saved" if feedback else "no feedback"
        if pending.get("action") == "rescript":
            outcome = self.post_rescript(slug, feedback)
            self.journal(hub, outcome)
            note += "; " + outcome
        self.state["pending_feedback"] = None
        self.git_sync("telegram: %s feedback" % slug)
        return {"ok": True, "hub": str(hub), "note": note}

    # ------------------------------------------------------------------ updates

    def handle(self, update: dict) -> dict:
        uid = update.get("update_id")
        record = {"update_id": uid}
        cb = update.get("callback_query")
        msg = update.get("message")
        if cb:
            chat = str((cb.get("message") or {}).get("chat", {}).get("id", ""))
            if self.tg.chat_id not in ("0", "") and chat != self.tg.chat_id:
                self.tg.answer_callback(cb.get("id", ""), "not your chat")
                return dict(record, type="callback", ignored="foreign chat")
            data = str(cb.get("data", ""))
            parts = data.split(":")
            action = parts[0] if parts else ""
            if action not in ACTIONS or len(parts) < 2:
                self.tg.answer_callback(cb.get("id", ""), "unknown button")
                return dict(record, type="callback", data=data, ignored="unknown callback")
            self.tg.answer_callback(cb.get("id", ""), "working")
            mid = (cb.get("message") or {}).get("message_id")
            if mid is not None:
                self.tg.clear_keyboard(chat or self.tg.chat_id, mid)
            result = self.act(action, parts[1], parts[2] if len(parts) > 2 else "")
            self.reply("%s %s: %s" % (action, parts[1], result.get("note", "")))
            return dict(record, type="callback", action=action, target=":".join(parts[1:]), **result)
        if msg:
            chat = str(msg.get("chat", {}).get("id", ""))
            if self.tg.chat_id not in ("0", "") and chat != self.tg.chat_id:
                return dict(record, type="message", ignored="foreign chat")
            text = str(msg.get("text", "")).strip()
            if not text:
                return dict(record, type="message", ignored="no text")
            if text.startswith("/"):
                if text.split()[0] in ("/start", "/ping"):
                    self.reply("BLAI gate bot is listening. Cards arrive when a video is ready for review.")
                return dict(record, type="message", command=text.split()[0])
            if self.state.get("pending_feedback"):
                result = self.apply_feedback(text)
                self.reply("feedback for %s: %s" % (result.get("hub", "?").split("/")[-1], result.get("note", "")))
                return dict(record, type="message", action="feedback", **result)
            return dict(record, type="message", ignored="no pending feedback")
        return dict(record, ignored="unsupported update")

    def poll(self, timeout: int, fixture_updates=None) -> int:
        if fixture_updates is not None:
            updates = fixture_updates
        else:
            updates = self.tg.call("getUpdates", {"timeout": timeout, "offset": self.state.get("offset") or 0,
                                                  "allowed_updates": ["message", "callback_query"]}, timeout=timeout + 15) or []
        for u in updates:
            if isinstance(u.get("update_id"), int):
                self.state["offset"] = u["update_id"] + 1
            try:
                record = self.handle(u)
            except Exception as e:  # one bad update must not stop the loop
                record = {"update_id": u.get("update_id"), "error": str(e)}
                log("update %s failed: %s" % (u.get("update_id"), e))
            print(json.dumps(record, ensure_ascii=False))
            sys.stdout.flush()
            self.save_state()
        return len(updates)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--once", action="store_true", help="one getUpdates call, then exit")
    ap.add_argument("--timeout", type=int, default=30, help="long-poll timeout in seconds")
    ap.add_argument("--repo", help="repo root holding workspaces/ and build/state (default: this repo)")
    ap.add_argument("--updates", help="fixture updates JSON for --dry-run (default fixtures/updates.json)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tgapi.load_env()
    repo = pathlib.Path(args.repo).resolve() if args.repo else tgapi.REPO_ROOT
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not args.dry_run and (not token or not chat_id):
        raise SystemExit("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set")
    tg = tgapi.Telegram(token, chat_id or "0", dry_run=args.dry_run)
    bot = Bot(repo, tg, args.dry_run)

    if args.dry_run:
        fixture = pathlib.Path(args.updates) if args.updates else tgapi.SKILL_DIR / "fixtures" / "updates.json"
        updates = json.loads(fixture.read_text(encoding="utf-8"))
        log("dry run: %d fixture update(s) from %s against %s" % (len(updates), fixture.name, repo))
        bot.poll(args.timeout, fixture_updates=updates)
        return 0

    log("polling as chat %s (offset %s)%s" % (chat_id, bot.state.get("offset"), " once" if args.once else ""))
    backoff = 5
    while True:
        try:
            bot.poll(args.timeout)
            backoff = 5
        except tgapi.TelegramError as e:
            log("poll error: %s; retrying in %ds" % (e, backoff))
            if args.once:
                return 1
            time.sleep(backoff)
            backoff = min(backoff * 2, 120)
            continue
        except KeyboardInterrupt:
            return 0
        if args.once:
            return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
