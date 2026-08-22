#!/usr/bin/env python3
"""Upload to or delete from the Cloudflare R2 bucket that hosts publish previews.

Usage:
  r2.py upload FILE --key KEY [--content-type TYPE] [--dry-run]   prints the public URL
  r2.py delete --key KEY [--dry-run]
  r2.py url --key KEY                                             prints the public URL without touching R2

Env (build/.env): R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET (default blai-previews),
R2_PUBLIC_BASE_URL (the bucket's public r2.dev URL or custom domain, no trailing slash).
Uses boto3 against https://<R2_ACCOUNT_ID>.r2.cloudflarestorage.com, region "auto". --dry-run makes no
network call and prints a fake URL. Exit 0/1, logs to stderr. Importable: upload(), delete(), public_url().
"""
from __future__ import annotations

import argparse
import mimetypes
import os
import pathlib
import sys

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
DEFAULT_BUCKET = "blai-previews"


def log(msg: str) -> None:
    sys.stderr.write("[r2] %s\n" % msg)
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


def bucket() -> str:
    return os.environ.get("R2_BUCKET") or DEFAULT_BUCKET


def public_url(key: str, dry_run: bool = False) -> str:
    base = os.environ.get("R2_PUBLIC_BASE_URL", "").rstrip("/")
    key = key.lstrip("/")
    if base:
        return "%s/%s" % (base, key)
    if dry_run:
        return "https://r2.example.invalid/%s/%s" % (bucket(), key)
    raise SystemExit("R2_PUBLIC_BASE_URL is not set (the bucket's public URL or custom domain)")


def client():
    try:
        import boto3  # type: ignore
    except ImportError:
        raise SystemExit("boto3 is not installed: pip install boto3")
    account = os.environ.get("R2_ACCOUNT_ID", "")
    key_id = os.environ.get("R2_ACCESS_KEY_ID", "")
    secret = os.environ.get("R2_SECRET_ACCESS_KEY", "")
    missing = [n for n, v in (("R2_ACCOUNT_ID", account), ("R2_ACCESS_KEY_ID", key_id), ("R2_SECRET_ACCESS_KEY", secret)) if not v]
    if missing:
        raise SystemExit("missing env: %s" % ", ".join(missing))
    return boto3.client(
        "s3",
        endpoint_url="https://%s.r2.cloudflarestorage.com" % account,
        aws_access_key_id=key_id,
        aws_secret_access_key=secret,
        region_name="auto",
    )


def upload(path, key: str, content_type: str | None = None, dry_run: bool = False) -> str:
    path = pathlib.Path(path)
    if not path.exists():
        raise SystemExit("file not found: %s" % path)
    ct = content_type or mimetypes.guess_type(str(path))[0] or "application/octet-stream"
    size_mb = path.stat().st_size / 1e6
    url = public_url(key, dry_run=dry_run)
    if dry_run:
        log("dry run: would upload %s (%.1f MB, %s) to %s/%s" % (path.name, size_mb, ct, bucket(), key))
        return url
    log("uploading %s (%.1f MB, %s) to %s/%s" % (path.name, size_mb, ct, bucket(), key))
    client().upload_file(str(path), bucket(), key.lstrip("/"), ExtraArgs={"ContentType": ct})
    return url


def delete(key: str, dry_run: bool = False) -> None:
    if dry_run:
        log("dry run: would delete %s/%s" % (bucket(), key))
        return
    client().delete_object(Bucket=bucket(), Key=key.lstrip("/"))
    log("deleted %s/%s" % (bucket(), key))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    up = sub.add_parser("upload", help="upload FILE and print its public URL")
    up.add_argument("file")
    up.add_argument("--key", required=True)
    up.add_argument("--content-type", default=None)
    up.add_argument("--dry-run", action="store_true")
    de = sub.add_parser("delete", help="delete an object")
    de.add_argument("--key", required=True)
    de.add_argument("--dry-run", action="store_true")
    ur = sub.add_parser("url", help="print the public URL for a key")
    ur.add_argument("--key", required=True)
    args = ap.parse_args()
    load_env()
    if args.cmd == "upload":
        print(upload(args.file, args.key, args.content_type, args.dry_run))
    elif args.cmd == "delete":
        delete(args.key, args.dry_run)
    else:
        print(public_url(args.key, dry_run=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        if e.code not in (0, None) and not isinstance(e.code, int):
            log(str(e.code))
            sys.exit(1)
        raise
