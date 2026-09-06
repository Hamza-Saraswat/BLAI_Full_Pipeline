#!/usr/bin/env python3
"""Send a Telegram card (ideas FYI, approval gate, blocked, post-publish checklist, or free text).

Usage:
  send_card.py --kind fyi-ideas --ideas workspaces/shorts/stages/02-ideas/output/<date>-ideas.md [--dry-run]
  send_card.py --kind gate --hub workspaces/<ws>/videos/<slug>.md [--video final.mp4] [--preview-url URL]
               [--package FILE-package.md] [--duration-s N] [--dry-run]
  send_card.py --kind blocked --hub FILE.md [--text "<stage>: <reason>"] [--dry-run]
  send_card.py --kind checklist --hub FILE.md [--dry-run]
  send_card.py --kind text --text "..." [--hub FILE.md] [--dry-run]

Layouts and buttons: rules/cards.md. Callback data: approve|reject|rerender|rescript|retry:<slug>,
swap:<date>:<n>. The gate card attaches the video with sendVideo when --video is under 48 MB, otherwise
it links --preview-url (or the hub's preview_url). Sent message ids are stored in
build/state/telegram-messages.json keyed by slug (ideas cards: "ideas:<date>") so bot.py can clear
stale keyboards. Prints {"message_id": N}. Env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID.
--dry-run: no network; prints the rendered text and keyboard with message_id 0. Exit 0/1.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import tgapi  # noqa: E402

KINDS = ("fyi-ideas", "gate", "blocked", "checklist", "text")


def log(msg: str) -> None:
    tgapi.log(msg, "send_card")


def first_heading(body: str) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    return m.group(1).strip() if m else ""


def card_fyi_ideas(ideas_path: pathlib.Path, date: str) -> tuple:
    text = ideas_path.read_text(encoding="utf-8")
    ideas = tgapi.parse_ideas(text)
    if not ideas:
        raise SystemExit("no ranked ideas found in %s (expected '## 1. Title' headings, see rules/cards.md)" % ideas_path)
    ws_name, _ = tgapi.workspace_of(ideas_path)
    lines = ["\U0001f4a1 <b>Today's picks (%s)</b>" % tgapi.esc(date)]
    for idea in ideas[:2]:  # the two picks in full; the rest as one line each (2026-09-06: 12 full entries was a wall)
        head = "%d. <b>%s</b>" % (idea["rank"], tgapi.esc(idea["title"]))
        if idea.get("format"):
            head += " [%s]" % tgapi.esc(idea["format"])
        lines += ["", head]
        if idea.get("angle"):
            lines.append(tgapi.esc(idea["angle"]))
    others = ideas[2:]
    if others:
        lines += ["", "<i>Also ranked:</i> " + "; ".join("%d. %s" % (i["rank"], tgapi.esc(i["title"])) for i in others[:8])]
    lines += ["", "Nothing to do unless you want a swap: tap Swap n to put idea n in pick 2."]
    rows, row = [], []
    for i in ideas[:8]:
        row.append(("Swap %d" % i["rank"], "swap:%s:%d" % (date, i["rank"])))
        if len(row) == 4:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    keyboard = tgapi.inline_keyboard(rows)
    return "\n".join(lines), keyboard, "ideas:%s" % date


def card_gate(meta: dict, body: str, hub_path: pathlib.Path, slug: str, args) -> tuple:
    title = meta.get("title") or first_heading(body) or slug
    duration = args.duration_s
    if duration is None and args.video:
        duration = tgapi.ffprobe_duration(pathlib.Path(args.video))
    insight = ""
    package = pathlib.Path(args.package) if args.package else tgapi.resolve_package(hub_path, body, slug)
    if package:
        manifest = tgapi.read_manifest(package) or {}
        insight = manifest.get("original_insight", "")
        if not meta.get("title") and manifest.get("title"):
            title = manifest["title"]
    fmt = meta.get("format") or meta.get("workspace") or "n/a"
    line2 = "format: %s | duration: %s | structure: %s" % (
        tgapi.esc(fmt), ("%d s" % round(duration)) if duration else "n/a", tgapi.esc(meta.get("structure") or "n/a"))
    line3 = "style: %s | seo: %s" % (tgapi.esc(meta.get("style_pack") or "n/a"), tgapi.esc(meta.get("seo_score") or "n/a"))
    lines = ["\U0001f3ac <b>Ready to post: %s</b>" % tgapi.esc(title), line2, line3,
             "insight: %s" % (tgapi.esc(insight) if insight else "n/a"),
             "Approve posts it public at the next slot (11:00 or 18:00 CT). Reject asks you for a note.",
             "<i>%s</i>" % tgapi.esc(slug)]
    attach = bool(args.video) and pathlib.Path(args.video).exists() and pathlib.Path(args.video).stat().st_size <= tgapi.MAX_VIDEO_BYTES
    if args.video and not attach:
        log("video missing or over 48 MB; linking the preview instead")
    preview = args.preview_url or meta.get("preview_url") or ""
    if not attach:
        lines.append("preview: %s" % (tgapi.esc(preview) if preview else "none"))
    keyboard = tgapi.inline_keyboard([[("Approve", "approve:%s" % slug), ("Reject", "reject:%s" % slug)],
                                      [("Re-render", "rerender:%s" % slug), ("Re-script", "rescript:%s" % slug)]])
    return "\n".join(lines), keyboard, slug, attach


STAGE_WORDS = {"01-radar": "Radar", "02-ideas": "Ideas", "03-research": "Research", "04-script": "Script",
               "05-package": "Package", "06-voice": "Voice", "07-render": "Render", "08-publish": "Publish"}


def human_reason(reason: str) -> tuple:
    """'07-render: 07-render: scene s02 did not pass ...' -> ('Render', 'scene s02 did not pass ...')."""
    reason = (reason or "").strip()
    stage = ""
    changed = True
    while changed:
        changed = False
        for key, word in STAGE_WORDS.items():
            if reason.startswith(key + ":"):
                reason = reason[len(key) + 1:].strip()
                stage, changed = word, True
    return stage, reason or "no reason recorded"


def card_blocked(meta: dict, body: str, slug: str, text: str) -> tuple:
    title = meta.get("title") or first_heading(body) or slug
    stage, what = human_reason(text or meta.get("blocked_reason") or "")
    lines = ["❌ <b>Build failed: %s</b>" % tgapi.esc(title),
             ("%s stage: %s" % (stage, tgapi.esc(what))) if stage else tgapi.esc(what),
             "Next: the next build pass retries it on its own (08:35, 10:35, 12:35 CT). Tap Retry to queue it now.",
             "<i>%s</i>" % tgapi.esc(slug)]
    return "\n".join(lines), tgapi.inline_keyboard([[("Retry", "retry:%s" % slug)]]), slug


def card_checklist(meta: dict, body: str, slug: str, url_override: str) -> tuple:
    title = meta.get("title") or first_heading(body) or slug
    url = url_override or meta.get("youtube_url") or "(youtube_url not set yet)"
    third = "Add the related-video link"
    lines = ["<b>Published: %s</b>" % tgapi.esc(title), tgapi.esc(url), "Studio tasks (no API exists for these):",
             "1. Pin a comment", "2. End screen and cards", "3. %s" % third, "4. Community post"]
    return "\n".join(lines), None, slug


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", required=True, choices=KINDS)
    ap.add_argument("--hub", help="hub note workspaces/<ws>/videos/<slug>.md")
    ap.add_argument("--ideas", help="ideas note <date>-ideas.md (fyi-ideas)")
    ap.add_argument("--date", help="date for the ideas card (default: from the ideas filename)")
    ap.add_argument("--video", help="final.mp4 to attach to the gate card")
    ap.add_argument("--preview-url", help="preview link when the video is not attached (gate) or the URL (checklist)")
    ap.add_argument("--package", help="package note for the original insight (default: linked from the hub)")
    ap.add_argument("--duration-s", type=float, default=None)
    ap.add_argument("--text", help="blocked reason, or the message for --kind text")
    ap.add_argument("--html", action="store_true", help="--kind text: the message is already Telegram HTML (bold, italics); do not escape it")
    ap.add_argument("--repo", help="repo root for build/state (default: this repo)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tgapi.load_env()
    repo = pathlib.Path(args.repo).resolve() if args.repo else tgapi.REPO_ROOT
    # BLAI_GATE_BOT_TOKEN wins: on the Spark TELEGRAM_BOT_TOKEN may belong to Hermes's chat bot
    # (2026-09-03: a gate card went out from the chat bot, whose buttons nobody polls).
    token = os.environ.get("BLAI_GATE_BOT_TOKEN", "") or os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not args.dry_run and (not token or not chat_id):
        raise SystemExit("BLAI_GATE_BOT_TOKEN (or TELEGRAM_BOT_TOKEN) and TELEGRAM_CHAT_ID must be set")
    tg = tgapi.Telegram(token, chat_id or "0", dry_run=args.dry_run)

    meta, body, hub_path, slug = {}, "", None, ""
    if args.hub:
        hub_path = pathlib.Path(args.hub)
        if not hub_path.exists():
            raise SystemExit("hub note not found: %s" % hub_path)
        meta, body = tgapi.hubnote().read(hub_path)
        slug = meta.get("slug") or hub_path.stem
    elif args.kind in ("gate", "blocked", "checklist"):
        raise SystemExit("--hub is required for --kind %s" % args.kind)

    attach = False
    if args.kind == "fyi-ideas":
        if not args.ideas:
            raise SystemExit("--ideas is required for --kind fyi-ideas")
        ideas_path = pathlib.Path(args.ideas)
        if not ideas_path.exists():
            raise SystemExit("ideas note not found: %s" % ideas_path)
        date = args.date or ideas_path.name[:10]
        if not tgapi.DATE_RE.match(date):
            raise SystemExit("cannot infer the date from %s; pass --date YYYY-MM-DD" % ideas_path.name)
        text, keyboard, key = card_fyi_ideas(ideas_path, date)
    elif args.kind == "gate":
        text, keyboard, key, attach = card_gate(meta, body, hub_path, slug, args)
    elif args.kind == "blocked":
        text, keyboard, key = card_blocked(meta, body, slug, args.text or "")
    elif args.kind == "checklist":
        text, keyboard, key = card_checklist(meta, body, slug, args.preview_url or "")
    else:
        if not args.text:
            raise SystemExit("--text is required for --kind text")
        text, keyboard, key = (args.text if args.html else tgapi.esc(args.text)), None, (slug or "text")

    if args.kind in ("gate", "blocked") and not args.dry_run:
        for old in tgapi.pop_messages(repo, key, kinds=("gate", "blocked")):
            tg.clear_keyboard(old.get("chat_id") or chat_id, old.get("message_id"))

    if attach:
        vw = vh = 0
        try:
            import subprocess
            probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                                    "-show_entries", "stream=width,height", "-of", "csv=p=0",
                                    args.video], capture_output=True, text=True, timeout=30)
            vw, vh = (int(x) for x in probe.stdout.strip().split(",")[:2])
        except Exception:
            pass  # dimensions are a nicety; the send must not fail over them
        result = tg.send_video(pathlib.Path(args.video), text, keyboard, width=vw, height=vh)
    else:
        result = tg.send_message(text, keyboard, preview=(args.kind in ("gate", "checklist")))
    message_id = result.get("message_id") if isinstance(result, dict) else None
    if not args.dry_run and message_id is not None:
        tgapi.record_message(repo, key, message_id, args.kind, chat_id)
    out = {"message_id": message_id, "kind": args.kind, "key": key}
    if args.dry_run:
        out.update({"dry_run": True, "attached_video": attach, "text": text, "reply_markup": keyboard})
    print(json.dumps(out, ensure_ascii=False))
    log("%s card for %s: message_id %s" % (args.kind, key, message_id))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
    except tgapi.TelegramError as e:
        log(str(e))
        sys.exit(1)
