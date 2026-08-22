#!/usr/bin/env python3
"""Schedule a YouTube upload through Blotato from a package note's manifest.

Usage:
  publish.py --package FILE-package.md --video final.mp4 [--thumbnail FILE.png]
             [--slot auto|ISO] [--privacy private|public|unlisted] [--dry-run]
  publish.py --status POST_SUBMISSION_ID [--dry-run]
  publish.py --accounts [--dry-run]

Flow: parse the ```json manifest in the package note -> validate it against
shared/schemas/publish-manifest.schema.json (plus YouTube limits) -> upload the video (and thumbnail) to R2
with r2.py under previews/<slug>/ -> pick the slot (--slot ISO, else manifest publish_slot_hint, else the
next free slot from slots.py, skipping slots already taken in hub notes) -> POST /v2/posts -> print
{post_submission_id, scheduled_time, media_url, thumbnail_url}.

Env (build/.env): BLOTATO_API_KEY, BLOTATO_YOUTUBE_ACCOUNT_ID, BLAI_PUBLISH_PRIVACY (default privacy), R2_*.
Privacy precedence: --privacy, then BLAI_PUBLISH_PRIVACY, then the manifest's privacy_status.
Retries 429 and 5xx with exponential backoff (5 attempts). Rate limit is 30 requests per minute.
--dry-run: no upload, no API call; prints the exact body that would be sent. Exit 0/1, logs to stderr.
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
REPO_ROOT = SKILL_DIR.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))
import r2  # noqa: E402
import slots  # noqa: E402

API_BASE = "https://backend.blotato.com"
POSTS_PATH = "/v2/posts"
# Blotato docs call this "Get Post Status" and key it by postSubmissionId. If the real path differs,
# correct it here only.
STATUS_PATH = "/v2/posts/{id}"
ACCOUNTS_PATH = "/v2/users/me/accounts"
SCHEMA_PATH = REPO_ROOT / "shared" / "schemas" / "publish-manifest.schema.json"
MAX_DESCRIPTION_BYTES = 5000
MAX_TITLE_CHARS = 100
MAX_HASHTAGS = 3
MAX_THUMBNAIL_BYTES = 2 * 1024 * 1024
RETRY_ATTEMPTS = 5
PRIVACY_VALUES = ("private", "public", "unlisted")


def log(msg: str) -> None:
    sys.stderr.write("[publish] %s\n" % msg)
    sys.stderr.flush()


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


# -------------------------------------------------------------------------- manifest


def read_manifest(package_path: pathlib.Path) -> dict:
    text = package_path.read_text(encoding="utf-8")
    m = re.search(r"```json\s*\n(.*?)\n```", text, re.S)
    if not m:
        raise SystemExit("no ```json manifest block in %s" % package_path)
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        raise SystemExit("manifest JSON is invalid: %s" % e)
    if not isinstance(data, dict):
        raise SystemExit("manifest must be a JSON object")
    return data


def _check(path: str, value, spec: dict) -> list:
    errs = []
    if "enum" in spec and value not in spec["enum"]:
        errs.append("%s must be one of %s" % (path, ", ".join(map(str, spec["enum"]))))
    if "const" in spec and value != spec["const"]:
        errs.append("%s must be %s" % (path, json.dumps(spec["const"])))
    t = spec.get("type")
    if t == "string":
        if not isinstance(value, str):
            return errs + ["%s must be a string" % path]
        if "maxLength" in spec and len(value) > spec["maxLength"]:
            errs.append("%s is %d chars, max %d" % (path, len(value), spec["maxLength"]))
        if "minLength" in spec and len(value) < spec["minLength"]:
            errs.append("%s is shorter than %d chars" % (path, spec["minLength"]))
        if "pattern" in spec and not re.search(spec["pattern"], value):
            errs.append("%s does not match %s" % (path, spec["pattern"]))
    elif t == "number":
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return errs + ["%s must be a number" % path]
        if "minimum" in spec and value < spec["minimum"]:
            errs.append("%s below %s" % (path, spec["minimum"]))
        if "maximum" in spec and value > spec["maximum"]:
            errs.append("%s above %s" % (path, spec["maximum"]))
    elif t == "boolean":
        if not isinstance(value, bool):
            errs.append("%s must be true or false" % path)
    elif t == "array":
        if not isinstance(value, list):
            return errs + ["%s must be a list" % path]
        if "minItems" in spec and len(value) < spec["minItems"]:
            errs.append("%s needs at least %d item(s)" % (path, spec["minItems"]))
        if "maxItems" in spec and len(value) > spec["maxItems"]:
            errs.append("%s has %d items, max %d" % (path, len(value), spec["maxItems"]))
        if "items" in spec:
            for i, item in enumerate(value):
                errs += _check("%s[%d]" % (path, i), item, spec["items"])
    elif t == "object":
        if not isinstance(value, dict):
            return errs + ["%s must be an object" % path]
        for key in spec.get("required", []):
            if key not in value:
                errs.append("%s.%s is required" % (path, key))
        for key, sub in spec.get("properties", {}).items():
            if key in value:
                errs += _check("%s.%s" % (path, key), value[key], sub)
    return errs


def validate_manifest(m: dict, schema_path: pathlib.Path = SCHEMA_PATH) -> list:
    errs = []
    if schema_path.exists():
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        errs += _check("manifest", m, schema)
    else:
        log("schema not found at %s; applying built-in checks only" % schema_path)
        for key in ("slug", "format", "title", "description", "hashtags", "privacy_status",
                    "notify_subscribers", "made_for_kids", "contains_synthetic_media", "original_insight"):
            if key not in m:
                errs.append("manifest.%s is required" % key)
        title = m.get("title", "")
        if isinstance(title, str) and len(title) > MAX_TITLE_CHARS:
            errs.append("title is %d chars, max %d" % (len(title), MAX_TITLE_CHARS))
        tags = m.get("hashtags", [])
        if isinstance(tags, list) and len(tags) > MAX_HASHTAGS:
            errs.append("hashtags has %d entries, max %d" % (len(tags), MAX_HASHTAGS))
        if m.get("made_for_kids") is True:
            errs.append("made_for_kids must be false")
    if isinstance(m.get("slug"), str) and not re.match(r"^[a-z0-9][a-z0-9-]*$", m["slug"]):
        errs.append("slug must be lowercase letters, digits and hyphens")
    return sorted(set(errs))


def compose_description(m: dict) -> str:
    desc = str(m.get("description", "")).rstrip()
    chapters = m.get("chapters") or []
    if chapters and isinstance(chapters, list) and str(chapters[0].get("time", "")) not in desc:
        desc += "\n\nChapters\n" + "\n".join("%s %s" % (c.get("time", ""), c.get("label", "")) for c in chapters)
    related = m.get("related_long_form_url")
    if related and related not in desc:
        desc += "\n\nFull video: %s" % related
    missing = [h for h in m.get("hashtags", []) if h not in desc]
    if missing:
        desc += "\n\n" + " ".join(missing)
    return desc


# ------------------------------------------------------------------------------ api


def api(method: str, path: str, body: dict | None = None, api_key: str = "") -> dict:
    url = API_BASE + path
    data = json.dumps(body).encode("utf-8") if body is not None else None
    delay = 2.0
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        req = urllib.request.Request(url, data=data, method=method, headers={
            "blotato-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw.strip() else {}
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:400]
            except Exception:
                pass
            if e.code == 429 or e.code >= 500:
                retry_after = e.headers.get("Retry-After") if e.headers else None
                wait = float(retry_after) if retry_after and retry_after.isdigit() else delay
                log("HTTP %d on %s %s (attempt %d/%d); retrying in %.0fs %s" % (e.code, method, path, attempt, RETRY_ATTEMPTS, wait, detail))
                time.sleep(wait)
                delay *= 2
                continue
            raise SystemExit("Blotato HTTP %d on %s %s: %s" % (e.code, method, path, detail))
        except urllib.error.URLError as e:
            log("network error on %s %s (attempt %d/%d): %s" % (method, path, attempt, RETRY_ATTEMPTS, e.reason))
            time.sleep(delay)
            delay *= 2
    raise SystemExit("Blotato %s %s failed after %d attempts" % (method, path, RETRY_ATTEMPTS))


def normalize_status(raw: dict, post_id: str) -> dict:
    node = raw.get("post") if isinstance(raw.get("post"), dict) else raw
    status = ""
    for key in ("status", "state", "postStatus", "publishStatus"):
        if isinstance(node.get(key), str):
            status = node[key].lower()
            break
    url = ""
    for key in ("youtubeUrl", "publishedUrl", "postUrl", "permalink", "url", "externalUrl"):
        if isinstance(node.get(key), str) and node[key].startswith("http"):
            url = node[key]
            break
    error = node.get("error") or node.get("errorMessage") or ""
    return {"post_submission_id": post_id, "status": status, "youtube_url": url, "error": error, "raw": raw}


def list_accounts(raw) -> list:
    items = raw
    if isinstance(raw, dict):
        for key in ("items", "accounts", "data"):
            if isinstance(raw.get(key), list):
                items = raw[key]
                break
    out = []
    for a in items if isinstance(items, list) else []:
        if not isinstance(a, dict):
            continue
        out.append({"id": a.get("id"), "platform": a.get("platform"),
                    "name": a.get("name") or a.get("username") or a.get("displayName") or ""})
    return out


# ---------------------------------------------------------------------------- slots


def taken_slots(own_slug: str) -> list:
    """publish_slot values already written in hub notes across both workspaces."""
    taken = []
    for hub in sorted(REPO_ROOT.glob("workspaces/*/videos/*.md")):
        try:
            text = hub.read_text(encoding="utf-8")
        except OSError:
            continue
        fm = re.match(r"\A---\n(.*?)\n---", text, re.S)
        if not fm:
            continue
        slug = ""
        slot = ""
        for line in fm.group(1).splitlines():
            if line.startswith("slug:"):
                slug = line.split(":", 1)[1].strip().strip("\"'")
            elif line.startswith("publish_slot:"):
                slot = line.split(":", 1)[1].strip().strip("\"'")
        if slot and slug != own_slug:
            try:
                taken.append(slots.parse_iso(slot))
            except SystemExit:
                continue
    return taken


def pick_slot(args, manifest: dict, now: dt.datetime) -> str:
    if args.slot and args.slot != "auto":
        return slots.parse_iso(args.slot).isoformat()
    hint = manifest.get("publish_slot_hint")
    if hint:
        t = slots.parse_iso(hint)
        if t > now + dt.timedelta(minutes=slots.DEFAULT_LEAD_MIN):
            return t.isoformat()
        log("publish_slot_hint %s is in the past; picking the next free slot" % hint)
    fmt = manifest.get("format", "short")
    return slots.next_slot(fmt, now, taken=taken_slots(manifest.get("slug", ""))).isoformat()


# ------------------------------------------------------------------------------- body


def build_body(manifest: dict, account_id: str, media_url: str, thumbnail_url: str | None,
               privacy: str, scheduled_time: str) -> dict:
    target = {
        "targetType": "youtube",
        "title": manifest["title"],
        "privacyStatus": privacy,
        "shouldNotifySubscribers": bool(manifest.get("notify_subscribers", False)),
        "isMadeForKids": False,
        "containsSyntheticMedia": bool(manifest.get("contains_synthetic_media", False)),
    }
    if thumbnail_url:
        target["thumbnailUrl"] = thumbnail_url
    if manifest.get("playlist_ids"):
        target["playlistIds"] = list(manifest["playlist_ids"])
    return {
        "post": {
            "accountId": account_id,
            "content": {"text": compose_description(manifest), "platform": "youtube", "mediaUrls": [media_url]},
            "target": target,
        },
        "scheduledTime": scheduled_time,
    }


# ------------------------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--package", help="<slug>-package.md with the ```json manifest")
    ap.add_argument("--video", help="final.mp4 to upload")
    ap.add_argument("--thumbnail", help="thumbnail image (png/jpg); default: manifest.thumbnail relative to the package note")
    ap.add_argument("--slot", default="auto", help="auto (default) or an ISO-8601 time with offset")
    ap.add_argument("--chapters", metavar="FILE", help="JSON list of {time, label} with MEASURED chapter times (long-form); replaces the manifest's chapters and any MM:SS lines already in the description")
    ap.add_argument("--privacy", choices=PRIVACY_VALUES, default=None)
    ap.add_argument("--status", metavar="ID", help="print the normalized status of a post submission")
    ap.add_argument("--accounts", action="store_true", help="list connected Blotato accounts")
    ap.add_argument("--now", default=None, help="override the current time (ISO-8601) for slot selection")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    load_env()
    api_key = os.environ.get("BLOTATO_API_KEY", "")

    if args.accounts:
        if args.dry_run:
            raw = {"items": [{"id": "acc_dryrun", "platform": "youtube", "username": "Build Local AI"}]}
        else:
            if not api_key:
                raise SystemExit("BLOTATO_API_KEY is not set")
            raw = api("GET", ACCOUNTS_PATH, api_key=api_key)
        print(json.dumps(list_accounts(raw), indent=2))
        return 0

    if args.status:
        if args.dry_run:
            raw = {"id": args.status, "status": "scheduled", "url": ""}
        else:
            if not api_key:
                raise SystemExit("BLOTATO_API_KEY is not set")
            raw = api("GET", STATUS_PATH.format(id=args.status), api_key=api_key)
        print(json.dumps(normalize_status(raw, args.status)))
        return 0

    if not args.package or not args.video:
        raise SystemExit("--package and --video are required (or use --status / --accounts)")
    package = pathlib.Path(args.package)
    video = pathlib.Path(args.video)
    if not package.exists():
        raise SystemExit("package note not found: %s" % package)
    if not video.exists():
        raise SystemExit("video not found: %s" % video)

    manifest = read_manifest(package)
    if args.chapters:
        measured = json.loads(pathlib.Path(args.chapters).read_text(encoding="utf-8"))
        if not isinstance(measured, list) or not measured or str(measured[0].get("time", "")) not in ("00:00", "0:00", "00:00:00"):
            log("--chapters must be a non-empty list whose first entry is 00:00"); return 1
        manifest["chapters"] = measured
        # drop any estimated chapter lines (and a bare "Chapters" header) so compose_description re-adds the measured ones
        kept = [ln for ln in str(manifest.get("description", "")).splitlines()
                if not re.match(r"^\s*\d{1,2}:\d{2}(:\d{2})?\s+\S", ln) and ln.strip().lower() != "chapters"]
        manifest["description"] = re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()
    errors = validate_manifest(manifest)
    desc = compose_description(manifest)
    desc_bytes = len(desc.encode("utf-8"))
    if desc_bytes > MAX_DESCRIPTION_BYTES:
        errors.append("description is %d bytes after chapters and hashtags, max %d" % (desc_bytes, MAX_DESCRIPTION_BYTES))
    if errors:
        for e in errors:
            log("manifest error: %s" % e)
        raise SystemExit("manifest failed validation (%d error(s)); nothing uploaded" % len(errors))
    slug = manifest["slug"]

    thumb = pathlib.Path(args.thumbnail) if args.thumbnail else None
    if thumb is None and manifest.get("thumbnail"):
        cand = (package.parent / manifest["thumbnail"]).resolve()
        if cand.exists():
            thumb = cand
        else:
            log("manifest thumbnail %s not found next to the package note; continuing without it" % manifest["thumbnail"])
    if thumb is not None:
        if not thumb.exists():
            raise SystemExit("thumbnail not found: %s" % thumb)
        if thumb.stat().st_size > MAX_THUMBNAIL_BYTES:
            log("thumbnail is %.1f MB; YouTube accepts up to 2 MB" % (thumb.stat().st_size / 1e6))

    privacy = args.privacy or os.environ.get("BLAI_PUBLISH_PRIVACY", "").strip().lower() or manifest["privacy_status"]
    if privacy not in PRIVACY_VALUES:
        raise SystemExit("privacy must be one of %s (got %s)" % (", ".join(PRIVACY_VALUES), privacy))
    account_id = os.environ.get("BLOTATO_YOUTUBE_ACCOUNT_ID", "")
    if not args.dry_run and (not api_key or not account_id):
        raise SystemExit("BLOTATO_API_KEY and BLOTATO_YOUTUBE_ACCOUNT_ID must be set (publish.py --accounts lists ids)")

    now = slots.parse_iso(args.now) if args.now else dt.datetime.now(dt.timezone.utc)
    scheduled = pick_slot(args, manifest, now)

    media_url = r2.upload(video, "previews/%s/final.mp4" % slug, "video/mp4", dry_run=args.dry_run)
    thumbnail_url = None
    if thumb is not None:
        thumbnail_url = r2.upload(thumb, "previews/%s/thumbnail%s" % (slug, thumb.suffix.lower() or ".png"), dry_run=args.dry_run)

    body = build_body(manifest, account_id or "ACCOUNT_ID", media_url, thumbnail_url, privacy, scheduled)
    log("%s %s: title %r, %s, %d-byte description, slot %s" % (
        "dry run" if args.dry_run else "posting", slug, manifest["title"], privacy, desc_bytes, scheduled))

    if args.dry_run:
        print(json.dumps({"post_submission_id": "dry-run", "scheduled_time": scheduled, "media_url": media_url,
                          "thumbnail_url": thumbnail_url, "dry_run": True, "body": body}, indent=2))
        return 0

    resp = api("POST", POSTS_PATH, body, api_key=api_key)
    post_id = resp.get("postSubmissionId") or resp.get("post_submission_id") or resp.get("id") or ""
    if not post_id:
        log("response without a submission id: %s" % json.dumps(resp)[:400])
    print(json.dumps({"post_submission_id": post_id, "scheduled_time": scheduled, "media_url": media_url,
                      "thumbnail_url": thumbnail_url}))
    return 0 if post_id else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
