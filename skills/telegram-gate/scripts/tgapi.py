#!/usr/bin/env python3
"""Shared helpers for the Telegram gate scripts (stdlib only).

Bot API client over urllib (JSON calls and multipart uploads), HTML escaping, inline keyboards,
state files under build/state/, and hub-note / ideas-note lookup across both workspaces.
Not a CLI; imported by send_card.py and bot.py.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent
API_BASE = "https://api.telegram.org"
MAX_VIDEO_BYTES = 48 * 1024 * 1024
MESSAGE_LIMIT = 4096
CAPTION_LIMIT = 1024
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,80}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STATE_FILE = "telegram-state.json"
MESSAGES_FILE = "telegram-messages.json"


def log(msg: str, tag: str = "telegram") -> None:
    sys.stderr.write("[%s] %s\n" % (tag, msg))
    sys.stderr.flush()


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_env() -> None:
    env_file = REPO_ROOT / "build" / ".env"
    if not env_file.exists():
        return
    try:
        from dotenv import load_dotenv  # type: ignore
    except ImportError:
        log("build/.env found but python-dotenv is missing; using os.environ (pip install python-dotenv)")
        return
    load_dotenv(env_file, override=False)


def hubnote():
    """Import tools/hubnote.py from the repo this skill lives in."""
    tools = REPO_ROOT / "tools"
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    import hubnote as hn  # type: ignore
    return hn


def esc(s) -> str:
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline_keyboard(rows: list) -> dict:
    return {"inline_keyboard": [[{"text": t, "callback_data": d} for t, d in row] for row in rows]}


def multipart_encode(fields: dict, files: dict) -> tuple:
    """fields: name -> str; files: name -> (filename, bytes, content_type). Returns (body, content_type)."""
    boundary = "----blai" + uuid.uuid4().hex
    b = boundary.encode("ascii")
    parts = []
    for name, value in fields.items():
        parts += [b"--" + b, b'Content-Disposition: form-data; name="%s"' % name.encode("ascii"), b"", str(value).encode("utf-8")]
    for name, (filename, data, ctype) in files.items():
        parts += [b"--" + b,
                  b'Content-Disposition: form-data; name="%s"; filename="%s"' % (name.encode("ascii"), filename.encode("utf-8")),
                  b"Content-Type: " + ctype.encode("ascii"), b"", data]
    parts += [b"--" + b + b"--", b""]
    return b"\r\n".join(parts), "multipart/form-data; boundary=" + boundary


class TelegramError(Exception):
    pass


class Telegram:
    def __init__(self, token: str, chat_id: str, dry_run: bool = False):
        self.token = token
        self.chat_id = str(chat_id)
        self.dry_run = dry_run
        self._fake_id = 0

    def _sanitize(self, text: str) -> str:
        return text.replace(self.token, "***") if self.token else text

    def call(self, method: str, payload: dict | None = None, files: dict | None = None, timeout: int = 35):
        payload = dict(payload or {})
        if self.dry_run:
            self._fake_id += 1
            shown = {k: (v if k != "reply_markup" else "<keyboard>") for k, v in payload.items() if k not in ("text", "caption")}
            log("dry run: %s %s%s" % (method, json.dumps(shown, ensure_ascii=False)[:300], " +file" if files else ""))
            if method == "getUpdates":
                return []
            if method in ("sendMessage", "sendVideo", "sendPhoto"):
                return {"message_id": 0, "chat": {"id": self.chat_id}, "date": 0}
            return True
        if not self.token:
            raise TelegramError("TELEGRAM_BOT_TOKEN is not set")
        url = "%s/bot%s/%s" % (API_BASE, self.token, method)
        if files:
            fields = {k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in payload.items()}
            body, ctype = multipart_encode(fields, files)
        else:
            body, ctype = json.dumps(payload).encode("utf-8"), "application/json"
        for attempt in range(1, 4):
            req = urllib.request.Request(url, data=body, method="POST", headers={"Content-Type": ctype})
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                try:
                    data = json.loads(e.read().decode("utf-8"))
                except Exception:
                    data = {"ok": False, "description": "HTTP %d" % e.code, "error_code": e.code}
            except urllib.error.URLError as e:
                if attempt == 3:
                    raise TelegramError("network error on %s: %s" % (method, self._sanitize(str(e.reason))))
                time.sleep(3 * attempt)
                continue
            if data.get("ok"):
                return data.get("result")
            if data.get("error_code") == 429:
                wait = int(data.get("parameters", {}).get("retry_after", 3))
                log("rate limited on %s; waiting %ds" % (method, wait))
                time.sleep(wait)
                continue
            raise TelegramError("%s failed: %s" % (method, self._sanitize(str(data.get("description", data)))))
        raise TelegramError("%s failed after retries" % method)

    def send_message(self, text: str, keyboard: dict | None = None, preview: bool = False) -> dict:
        payload = {"chat_id": self.chat_id, "text": text[:MESSAGE_LIMIT], "parse_mode": "HTML",
                   "disable_web_page_preview": not preview}
        if keyboard:
            payload["reply_markup"] = keyboard
        return self.call("sendMessage", payload)

    def send_video(self, path: pathlib.Path, caption: str, keyboard: dict | None = None,
                   width: int = 0, height: int = 0) -> dict:
        payload = {"chat_id": self.chat_id, "caption": caption[:CAPTION_LIMIT], "parse_mode": "HTML", "supports_streaming": True}
        # Without explicit dimensions Telegram guesses and can render a 9:16
        # Short as a square-ish preview in the chat (seen on the first gate card).
        if width and height:
            payload.update({"width": int(width), "height": int(height)})
        if keyboard:
            payload["reply_markup"] = keyboard
        data = b"" if self.dry_run else path.read_bytes()
        return self.call("sendVideo", payload, files={"video": (path.name, data, "video/mp4")}, timeout=300)

    def answer_callback(self, callback_id: str, text: str = "") -> None:
        try:
            self.call("answerCallbackQuery", {"callback_query_id": callback_id, "text": text[:200]})
        except TelegramError as e:
            log("answerCallbackQuery: %s" % e)

    def clear_keyboard(self, chat_id, message_id) -> None:
        try:
            self.call("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id,
                                                 "reply_markup": {"inline_keyboard": []}})
        except TelegramError as e:
            log("editMessageReplyMarkup %s: %s" % (message_id, e))


# ------------------------------------------------------------------------------ state


def state_dir(repo: pathlib.Path, create: bool = False) -> pathlib.Path:
    d = repo / "build" / "state"
    if create:
        d.mkdir(parents=True, exist_ok=True)
    return d


def read_json(path: pathlib.Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def write_json_atomic(path: pathlib.Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp-%d" % os.getpid())
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def record_message(repo: pathlib.Path, key: str, message_id, kind: str, chat_id: str) -> None:
    path = state_dir(repo) / MESSAGES_FILE
    data = read_json(path, {})
    data.setdefault(key, []).append({"message_id": message_id, "kind": kind, "chat_id": str(chat_id), "sent_at": now_iso()})
    write_json_atomic(path, data)


def pop_messages(repo: pathlib.Path, key: str, kinds=None) -> list:
    path = state_dir(repo) / MESSAGES_FILE
    data = read_json(path, {})
    entries = data.get(key, [])
    keep = [e for e in entries if kinds and e.get("kind") not in kinds]
    popped = [e for e in entries if e not in keep]
    if keep:
        data[key] = keep
    else:
        data.pop(key, None)
    write_json_atomic(path, data)
    return popped


# ------------------------------------------------------------------------- lookups


def find_hub(repo: pathlib.Path, slug: str):
    for p in sorted(repo.glob("workspaces/*/videos/%s.md" % slug)):
        return p
    return None


def workspace_of(path: pathlib.Path):
    parts = path.resolve().parts
    if "workspaces" in parts:
        i = parts.index("workspaces")
        if i + 1 < len(parts):
            return parts[i + 1], pathlib.Path(*parts[: i + 2])
    return None, None


def find_ideas_note(repo: pathlib.Path, date: str):
    for p in sorted(repo.glob("workspaces/*/stages/02-ideas/output/%s-ideas.md" % date)):
        return p
    return None


IDEA_HEAD = re.compile(r"^\s*(?:#{1,4}\s+)?(\d{1,2})[.)]\s+(.+?)\s*$")
IDEA_LABEL = re.compile(r"^\**\s*(angle|why now|why_now|why-now|format|pillar|structure)\s*\**\s*:\s*\**(.+?)\**\s*$", re.I)


def parse_ideas(text: str, limit: int = 5) -> list:
    """Ranked ideas: '## 1. Title' headings or '1. **Title**' items, then label lines (angle:, why now:)."""
    ideas = []
    cur = None
    for raw in text.splitlines():
        m = IDEA_HEAD.match(raw)
        if m and (raw.lstrip().startswith("#") or raw.lstrip()[:1].isdigit()):
            title = re.sub(r"\*\*|__|`|\[\[|\]\]", "", m.group(2)).strip()
            cur = {"rank": int(m.group(1)), "title": title, "angle": "", "why_now": "", "format": "", "lines": []}
            ideas.append(cur)
            continue
        if raw.lstrip().startswith("#"):
            cur = None
            continue
        if cur is None:
            continue
        s = raw.strip().lstrip("-*").strip()
        if not s:
            continue
        lm = IDEA_LABEL.match(s)
        if lm:
            key = lm.group(1).lower().replace(" ", "_").replace("-", "_")
            cur[key if key in ("angle", "why_now", "format") else "extra_" + key] = lm.group(2).strip()
        else:
            cur["lines"].append(s)
    for idea in ideas:
        if not idea["angle"] and idea["lines"]:
            idea["angle"] = idea["lines"][0]
        if not idea["why_now"] and len(idea["lines"]) > 1:
            idea["why_now"] = idea["lines"][1]
        del idea["lines"]
    ideas.sort(key=lambda i: i["rank"])
    return ideas[:limit]


def resolve_package(hub_path: pathlib.Path, body: str, slug: str):
    """The package note linked from the hub's Artifacts list, else stages/*/output/<slug>-package.md."""
    ws_name, ws_dir = workspace_of(hub_path)
    m = re.search(r"Package:\s*\[\[([^\]|#]+)", body)
    if m and ws_dir:
        rel = m.group(1).strip()
        cand = ws_dir / (rel if rel.endswith(".md") else rel + ".md")
        if cand.exists():
            return cand
    if ws_dir:
        for p in sorted(ws_dir.glob("stages/*/output/%s-package.md" % slug)):
            return p
    return None


def read_manifest(path: pathlib.Path):
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.search(r"```json\s*\n(.*?)\n```", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def ffprobe_duration(path: pathlib.Path):
    try:
        proc = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        return float(proc.stdout.strip())
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return None
