#!/usr/bin/env python3
"""Read and update BLAI hub notes (workspaces/<ws>/videos/<slug>.md) without a YAML library.

Frontmatter is a flat list of `key: value` lines (see shared/hub-note-template.md). Values are
plain scalars; quotes are optional and stripped. Lists are not supported on purpose.

Library use:
    from hubnote import read, update, append_section, find
CLI use:
    python3 tools/hubnote.py get   workspaces/shorts/videos/<slug>.md status
    python3 tools/hubnote.py set   workspaces/shorts/videos/<slug>.md status=review preview_url=https://...
    python3 tools/hubnote.py journal workspaces/shorts/videos/<slug>.md "07-render ok 412s"
    python3 tools/hubnote.py find  workspaces/shorts ready-to-build
"""
from __future__ import annotations
import datetime as dt
import pathlib
import re
import sys

FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _unquote(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def _quote(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if s == "" or re.search(r"[:#\[\]{}&*!|>'\"%@`,]|^\s|\s$", s):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def read(path) -> tuple[dict, str]:
    text = pathlib.Path(path).read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = _unquote(v)
    return meta, text[m.end():]


def write(path, meta: dict, body: str) -> None:
    lines = ["---"] + ["%s: %s" % (k, _quote(v)) for k, v in meta.items()] + ["---"]
    pathlib.Path(path).write_text("\n".join(lines) + "\n" + body.lstrip("\n"), encoding="utf-8")


def update(path, **fields) -> dict:
    meta, body = read(path)
    for k, v in fields.items():
        meta[k] = v
    meta["updated"] = _now()
    write(path, meta, body)
    return meta


def append_section(path, heading: str, line: str) -> None:
    """Append a bullet under `## <heading>` (created at the end if missing)."""
    meta, body = read(path)
    marker = "## " + heading
    stamp = "- %s %s" % (_now(), line)
    if marker in body:
        head, rest = body.split(marker, 1)
        # insert before the next top-level heading inside `rest`
        m = re.search(r"\n## ", rest)
        if m:
            rest = rest[:m.start()].rstrip("\n") + "\n" + stamp + "\n" + rest[m.start():]
        else:
            rest = rest.rstrip("\n") + "\n" + stamp + "\n"
        body = head + marker + rest
    else:
        body = body.rstrip("\n") + "\n\n" + marker + "\n" + stamp + "\n"
    write(path, meta, body)


def find(workspace_dir, status: str | None = None) -> list[pathlib.Path]:
    out = []
    for p in sorted(pathlib.Path(workspace_dir, "videos").glob("*.md")):
        meta, _ = read(p)
        if meta.get("slug") and (status is None or meta.get("status") == status):
            out.append(p)
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    cmd = argv[0]
    if cmd == "get":
        meta, _ = read(argv[1]); print(meta.get(argv[2], "") if len(argv) > 2 else meta); return 0
    if cmd == "set":
        fields = dict(a.split("=", 1) for a in argv[2:]); update(argv[1], **fields); return 0
    if cmd == "journal":
        append_section(argv[1], "Build journal", " ".join(argv[2:])); return 0
    if cmd == "find":
        for p in find(argv[1], argv[2] if len(argv) > 2 else None): print(p)
        return 0
    print("unknown command", cmd); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
