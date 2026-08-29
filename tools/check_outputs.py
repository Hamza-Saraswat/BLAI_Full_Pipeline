#!/usr/bin/env python3
"""Check committed hub notes and package manifests against shared/schemas (stdlib only; a small
subset of JSON Schema: required, enum, pattern, type, minItems/maxItems, maxLength, const).

    python3 tools/check_outputs.py            # whole repo
Exit 1 on the first workspace with failures.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import hubnote  # noqa: E402


def check(value, schema, path="$"):
    errs = []
    t = schema.get("type")
    types = t if isinstance(t, list) else ([t] if t else [])
    if types:
        ok = any(
            (ty == "object" and isinstance(value, dict)) or (ty == "array" and isinstance(value, list)) or
            (ty == "string" and isinstance(value, str)) or (ty == "boolean" and isinstance(value, bool)) or
            (ty == "integer" and isinstance(value, int) and not isinstance(value, bool)) or
            (ty == "number" and isinstance(value, (int, float)) and not isinstance(value, bool))
            for ty in types)
        if not ok:
            return ["%s: expected %s" % (path, types)]
    if "enum" in schema and value not in schema["enum"]:
        errs.append("%s: %r not in %s" % (path, value, schema["enum"]))
    if "const" in schema and value != schema["const"]:
        errs.append("%s: must be %r" % (path, schema["const"]))
    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errs.append("%s: %r does not match %s" % (path, value, schema["pattern"]))
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errs.append("%s: longer than %d" % (path, schema["maxLength"]))
        if "minLength" in schema and len(value) < schema["minLength"]:
            errs.append("%s: shorter than %d" % (path, schema["minLength"]))
    if isinstance(value, dict):
        for r in schema.get("required", []):
            if r not in value:
                errs.append("%s: missing %s" % (path, r))
        for k, sub in schema.get("properties", {}).items():
            if k in value:
                errs += check(value[k], sub, path + "." + k)
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errs.append("%s: fewer than %d items" % (path, schema["minItems"]))
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errs.append("%s: more than %d items" % (path, schema["maxItems"]))
        if "items" in schema:
            for i, it in enumerate(value):
                errs += check(it, schema["items"], "%s[%d]" % (path, i))
    return errs


def manifest_from_package(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"```json\s*\n(.*?)\n```", text, re.S)
    return json.loads(m.group(1)) if m else None



def main():
    schemas = {p.stem: json.loads(p.read_text()) for p in (ROOT / "shared" / "schemas").glob("*.json")}
    failures = 0
    for ws in ("shorts",):
        wsdir = ROOT / "workspaces" / ws
        for note in sorted((wsdir / "videos").glob("*.md")):
            meta, _ = hubnote.read(note)
            if "seo_score" in meta:
                try:
                    meta["seo_score"] = float(meta["seo_score"])
                except ValueError:
                    pass
            for e in check(meta, schemas["hub-note.schema"]):
                failures += 1; print("FAIL %s: %s" % (note.relative_to(ROOT), e))
        for pkg in sorted(wsdir.glob("stages/*-package/output/*-package.md")):
            man = manifest_from_package(pkg)
            if man is None:
                failures += 1; print("FAIL %s: no ```json manifest block" % pkg.relative_to(ROOT)); continue
            for e in check(man, schemas["publish-manifest.schema"]):
                failures += 1; print("FAIL %s: %s" % (pkg.relative_to(ROOT), e))
    print("check_outputs: %d failure(s)" % failures)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
