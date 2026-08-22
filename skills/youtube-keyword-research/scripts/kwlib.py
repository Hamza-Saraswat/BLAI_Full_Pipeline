#!/usr/bin/env python3
"""Shared helpers for the youtube-keyword-research scripts (stdlib only, Python 3.9+).

    import kwlib as kw

Environment loading, stderr logging with secret redaction, HTTP with retries, fixture loading
for --dry-run, time helpers and JSON output to stdout or --out.
"""
from __future__ import annotations

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
REPO_DIR = SKILL_DIR.parents[1]
FIXTURES_DIR = SKILL_DIR / "fixtures"
DEFAULT_UA = "blai-keyword-research/1.0"
DRY_RUN_NOW = "2026-08-25T12:00:00Z"   # fixtures are dated around this instant

_PARAM_RE = re.compile(r"(key|token|secret|password|access_token)=([^&\s\"']+)", re.I)
_AUTH_RE = re.compile(r"\b(bearer|basic)\s+[A-Za-z0-9._~+/=-]{8,}", re.I)


def redact(text) -> str:
    text = _PARAM_RE.sub(lambda m: m.group(1) + "=REDACTED", str(text))
    return _AUTH_RE.sub(lambda m: m.group(1) + " REDACTED", text)


def log(source: str, msg) -> None:
    sys.stderr.write("[%s] %s\n" % (source, redact(msg)))
    sys.stderr.flush()


def load_env() -> None:
    """Fill os.environ from BLAI_ENV_FILE, build/.env or .env (first found; never overrides)."""
    for cand in (os.environ.get("BLAI_ENV_FILE"), REPO_DIR / "build" / ".env", REPO_DIR / ".env"):
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
            key, value = key.strip(), value.strip().strip("'\"")
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
    if value is None or value == "":
        return None
    text = str(value).strip().replace("Z", "+00:00")
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


def http(url: str, headers: dict | None = None, timeout: int = 20, retries: int = 2,
         source: str = "http") -> tuple[int, bytes, dict]:
    """GET returning (status, body, headers); retries 429 and 5xx with backoff."""
    hdrs = {"User-Agent": DEFAULT_UA, "Accept": "application/json, text/javascript, */*"}
    hdrs.update(headers or {})
    safe_url = redact(url)
    last = "request failed"
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=hdrs)
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


def get_json(url: str, headers: dict | None = None, timeout: int = 20, source: str = "http"):
    status, raw, hdrs = http(url, headers=headers, timeout=timeout, source=source)
    charset = "utf-8"
    match = re.search(r"charset=([\w-]+)", hdrs.get("Content-Type", "") or "", re.I)
    if match:
        charset = match.group(1)
    try:
        return json.loads(raw.decode(charset, "replace"))
    except (json.JSONDecodeError, LookupError) as err:
        raise RuntimeError("bad JSON (HTTP %s) from %s: %s" % (status, redact(url), err)) from None


def fixture(name: str):
    with open(FIXTURES_DIR / name, encoding="utf-8") as fh:
        return json.load(fh)


def emit(data, out: str | None) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if out:
        path = pathlib.Path(out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")
        sys.stdout.flush()
