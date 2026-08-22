#!/usr/bin/env python3
"""Shared helpers for the trend-radar scripts (stdlib only, Python 3.9+).

Every script in this folder imports this module from its own directory:

    import radarlib as rl

It provides environment loading, stderr logging with secret redaction, HTTP with retries,
fixture loading for --dry-run, time helpers, the fenced-list reader for rules/sources.md,
and the shared CLI (--hours, --limit, --out, --dry-run) used by the six source scripts.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REPO_DIR = SKILL_DIR.parents[1]          # skills/trend-radar -> skills -> repo root
FIXTURES_DIR = SKILL_DIR / "fixtures"
RULES_DIR = SKILL_DIR / "rules"
DEFAULT_UA = "blai-radar/1.0"
# --dry-run pins the clock here; every fixture is dated around this instant.
DRY_RUN_NOW = "2026-08-25T12:00:00Z"


class Skip(Exception):
    """A source cannot run (missing key). radar.py notes it on stderr and carries on."""


_PARAM_RE = re.compile(r"(key|token|secret|password|client_secret|access_token)=([^&\s\"']+)", re.I)
_AUTH_RE = re.compile(r"\b(bearer|basic)\s+[A-Za-z0-9._~+/=-]{8,}", re.I)


def redact(text: str) -> str:
    """Strip anything that looks like a credential before it reaches a log line."""
    text = _PARAM_RE.sub(lambda m: m.group(1) + "=REDACTED", str(text))
    return _AUTH_RE.sub(lambda m: m.group(1) + " REDACTED", text)


def log(source: str, msg) -> None:
    sys.stderr.write("[%s] %s\n" % (source, redact(msg)))
    sys.stderr.flush()


def load_env() -> None:
    """Fill os.environ from BLAI_ENV_FILE, build/.env or .env (first found; never overrides)."""
    candidates = [os.environ.get("BLAI_ENV_FILE"), REPO_DIR / "build" / ".env", REPO_DIR / ".env"]
    for cand in candidates:
        if not cand:
            continue
        path = pathlib.Path(cand)
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'\"")
            if key and value and key not in os.environ:
                os.environ[key] = value
        return


def env(name: str) -> str | None:
    value = os.environ.get(name, "").strip()
    return value or None


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def now_for(dry_run: bool) -> dt.datetime:
    return parse_time(DRY_RUN_NOW) if dry_run else utcnow()


_FRACTION_RE = re.compile(r"\.(\d+)(?=[+-]|$)")


def _pad_fraction(match) -> str:
    """Python 3.9's fromisoformat accepts only 3 or 6 fraction digits; 3.11+ accepts any."""
    digits = match.group(1)
    if len(digits) in (3, 6):
        return "." + digits
    return "." + (digits[:6] if len(digits) > 6 else digits.ljust(6, "0"))


def parse_time(value) -> dt.datetime | None:
    """Epoch seconds or ISO-8601 (Z or offset) to an aware UTC datetime; None when unreadable."""
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return dt.datetime.fromtimestamp(float(value), dt.timezone.utc)
    text = str(value).strip()
    if re.fullmatch(r"\d{9,11}(\.\d+)?", text):
        return dt.datetime.fromtimestamp(float(text), dt.timezone.utc)
    text = text.replace("Z", "+00:00")
    text = _FRACTION_RE.sub(_pad_fraction, text)
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def iso(value: dt.datetime | None) -> str | None:
    return value.strftime("%Y-%m-%dT%H:%M:%SZ") if value else None


def age_hours(published: dt.datetime | None, now: dt.datetime) -> float | None:
    if not published:
        return None
    return max(0.0, (now - published).total_seconds() / 3600.0)


def clip(text, limit: int) -> str:
    """Collapse whitespace, swap em dashes for `--` (repo rule), cut to `limit` characters."""
    text = str(text or "").replace("\u2014", "--").replace("\u2013", "-")   # em and en dash, by codepoint
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def http(url: str, headers: dict | None = None, data=None, timeout: int = 20,
         retries: int = 2, source: str = "http") -> tuple[int, bytes, dict]:
    """GET, or POST when `data` is given. Returns (status, body, headers). Retries 429/5xx."""
    hdrs = {"User-Agent": DEFAULT_UA, "Accept": "application/json"}
    hdrs.update(headers or {})
    body = None
    if data is not None:
        if isinstance(data, (dict, list)):
            body = json.dumps(data).encode("utf-8")
            hdrs.setdefault("Content-Type", "application/json")
        elif isinstance(data, str):
            body = data.encode("utf-8")
        else:
            body = data
    safe_url = redact(url)
    last = "request failed"
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=body, headers=hdrs,
                                     method="POST" if body is not None else "GET")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read(), dict(resp.headers)
        except urllib.error.HTTPError as err:
            last = "HTTP %s for %s" % (err.code, safe_url)
            if err.code in (429, 500, 502, 503, 504) and attempt < retries:
                wait = 1.5 * (2 ** attempt)
                log(source, "%s, retry in %.1fs" % (last, wait))
                time.sleep(wait)
                continue
            try:
                detail = err.read(300).decode("utf-8", "replace").strip()
            except Exception:
                detail = ""
            if detail.startswith("<"):
                detail = "(html body)"
            raise RuntimeError("%s %s" % (last, redact(detail))) from None
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            last = "%s for %s" % (getattr(err, "reason", err), safe_url)
            if attempt < retries:
                wait = 1.5 * (2 ** attempt)
                log(source, "%s, retry in %.1fs" % (last, wait))
                time.sleep(wait)
                continue
            raise RuntimeError(last) from None
    raise RuntimeError(last)


def get_json(url: str, headers: dict | None = None, data=None, timeout: int = 20,
             source: str = "http"):
    status, raw, _ = http(url, headers=headers, data=data, timeout=timeout, source=source)
    try:
        return json.loads(raw.decode("utf-8", "replace"))
    except json.JSONDecodeError as err:
        raise RuntimeError("bad JSON (HTTP %s) from %s: %s" % (status, redact(url), err)) from None


def fixture(name: str):
    path = FIXTURES_DIR / name
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def rule_list(block: str, default: list[str]) -> list[str]:
    """Lines of the fenced ```<block> list in rules/sources.md; the built-in default otherwise."""
    try:
        text = (RULES_DIR / "sources.md").read_text(encoding="utf-8")
    except OSError:
        return list(default)
    match = re.search(r"```%s\n(.*?)```" % re.escape(block), text, re.S)
    if not match:
        return list(default)
    lines = [ln.strip() for ln in match.group(1).splitlines()]
    lines = [ln for ln in lines if ln and not ln.startswith("#")]
    return lines or list(default)


def emit(data, out: str | None) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if out:
        path = pathlib.Path(out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")
        sys.stdout.flush()


def source_parser(description: str, limit: int) -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hours", type=int, default=48, help="look-back window in hours (default 48)")
    ap.add_argument("--limit", type=int, default=limit,
                    help="items per query, subreddit, repo or list (default %d)" % limit)
    ap.add_argument("--out", help="write the JSON list here instead of stdout")
    ap.add_argument("--dry-run", action="store_true",
                    help="parse the fixture under fixtures/ instead of calling the network")
    return ap


def run_source(name: str, collect, description: str, limit: int) -> int:
    """Standard main() for a source script. Exit 0 (data emitted) or 1 (network or parse failure)."""
    args = source_parser(description, limit).parse_args()
    if args.hours <= 0 or args.limit <= 0:
        log(name, "error: --hours and --limit must be positive")
        return 1
    load_env()
    try:
        items = collect(args.hours, args.limit, args.dry_run)
    except Skip as why:
        log(name, "skipped: %s" % why)
        items = []
    except Exception as err:          # network, parse, fixture
        log(name, "error: %s" % err)
        return 1
    emit(items, args.out)
    log(name, "%d item(s)%s" % (len(items), " from fixtures (dry-run)" if args.dry_run else ""))
    return 0
