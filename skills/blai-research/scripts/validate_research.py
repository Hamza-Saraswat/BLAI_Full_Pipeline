#!/usr/bin/env python3
"""validate_research.py <brief.json> [--schema PATH]  -- blockers-only gate for the research brief.

v2 port of pipeline/scripts/validate_research.py. Stdlib-only. The brief is
producer-reviewed, not machine-consumed by a renderer, so there are no
stylistic advisories, only blockers that would make the brief useless to the
script writer:

  BLOCKERS  every violation of shared/schemas/research.schema.json (required
            keys, types, enums, patterns, lengths, unknown keys), which covers
            the v1 checks: >=3 claims, an http(s) source_url on every claim,
            non-empty thesis / explanation_path / suggested_outline.

--schema defaults to ../../../shared/schemas/research.schema.json relative to
this file. When the schema cannot be read, the v1 built-in checks run alone and
a warning names the missing file.

Output shape matches validate_storyboard.py:
  {file, blockers, advisories: [], violations, warnings}

Exit 0 = clean, 1 = blockers, 2 = usage.
"""
import argparse
import json
import re
import sys
from pathlib import Path

# v2 port (skills/blai-research/scripts/): parents[3] is the repo root.
REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SCHEMA = REPO_ROOT / "shared" / "schemas" / "research.schema.json"
DEFAULT_SCHEMA_HINT = "../../../shared/schemas/research.schema.json"

# v1 fallbacks, used only when the schema file cannot be read.
QUALITIES = {"primary", "docs", "benchmark", "community"}
CONFIDENCES = {"high", "medium"}
DEPTHS = {"standard", "deep"}
REQUIRED = {
    "slug": str, "topic": str, "generated_at": str, "depth": str,
    "thesis": str, "explanation_path": str, "claims": list,
    "key_numbers": list, "analogy_candidates": list, "misconceptions": list,
    "glossary": list, "unverified": list, "suggested_outline": str,
}


def _type_ok(value, typ):
    if typ == "object":
        return isinstance(value, dict)
    if typ == "array":
        return isinstance(value, list)
    if typ == "string":
        return isinstance(value, str)
    if typ == "boolean":
        return isinstance(value, bool)
    if typ == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if typ == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if typ == "null":
        return value is None
    return True


def check_schema(value, schema, path="$"):
    """The JSON Schema draft-07 subset used by shared/schemas: type, enum,
    pattern, minLength, maxLength, minItems, maxItems, items, required,
    properties, additionalProperties. Returns a list of messages."""
    errs = []
    types = schema.get("type")
    if types:
        types = types if isinstance(types, list) else [types]
        if not any(_type_ok(value, t) for t in types):
            return [f"{path}: expected {'/'.join(types)}, got {type(value).__name__}"]
    if "enum" in schema and value not in schema["enum"]:
        errs.append(f"{path}: {value!r} is not one of {schema['enum']}")
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errs.append(f"{path}: {len(value)} chars, need at least {schema['minLength']}")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errs.append(f"{path}: {len(value)} chars, at most {schema['maxLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errs.append(f"{path}: {value!r} does not match {schema['pattern']}")
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errs.append(f"{path}: {len(value)} items, need at least {schema['minItems']}")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errs.append(f"{path}: {len(value)} items, at most {schema['maxItems']}")
        if "items" in schema:
            for i, item in enumerate(value):
                errs += check_schema(item, schema["items"], f"{path}[{i}]")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errs.append(f"{path}: missing key: {key}")
        for key, sub in props.items():
            if key in value:
                errs += check_schema(value[key], sub, f"{path}.{key}")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errs.append(f"{path}: unknown key: {key}")
    return errs


def builtin_checks(rb):
    """The v1 gate, unchanged: required keys and types, shape, >=3 sourced claims."""
    bl = []
    for key, typ in REQUIRED.items():
        if key not in rb:
            bl.append(f"missing key: {key}")
        elif not isinstance(rb[key], typ):
            bl.append(f"{key}: expected {typ.__name__}")
    if bl:
        return bl
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,40}", rb["slug"]):
        bl.append(f"bad slug: {rb['slug']}")
    if rb["depth"] not in DEPTHS:
        bl.append(f"bad depth: {rb['depth']!r} (use standard|deep)")
    if not rb["thesis"].strip():
        bl.append("thesis is empty")
    if not rb["explanation_path"].strip():
        bl.append("explanation_path is empty")
    if not rb["suggested_outline"].strip():
        bl.append("suggested_outline is empty (it seeds the video outline)")
    claims = rb["claims"]
    if len(claims) < 3:
        bl.append(f"only {len(claims)} claims; need >=3 sourced claims")
    for i, c in enumerate(claims):
        cid = f"claim[{i}]"
        if not isinstance(c, dict):
            bl.append(f"{cid}: not an object")
            continue
        url = c.get("source_url", "")
        if not (isinstance(url, str) and re.match(r"^https?://", url)):
            bl.append(f"{cid}: missing/invalid http(s) source_url")
        if not str(c.get("claim", "")).strip():
            bl.append(f"{cid}: empty claim text")
        q = c.get("source_quality")
        if q is not None and q not in QUALITIES:
            bl.append(f"{cid}: bad source_quality {q!r}")
        conf = c.get("confidence")
        if conf is not None and conf not in CONFIDENCES:
            bl.append(f"{cid}: bad confidence {conf!r}")
    return bl


def _emit(path, bl, warnings=None):
    print(json.dumps({"file": path, "blockers": bl, "advisories": [],
                      "violations": bl, "warnings": warnings or []}, indent=2))
    sys.exit(1 if bl else 0)


def main():
    ap = argparse.ArgumentParser(
        description="Blockers-only gate for a research brief JSON (exit 0 clean, 1 blockers, 2 usage).",
        epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("brief", nargs="?", help="path to <slug>-brief.json")
    ap.add_argument("--schema", default=None,
                    help=f"JSON schema to enforce (default: {DEFAULT_SCHEMA_HINT} relative to this script)")
    args = ap.parse_args()
    if not args.brief:
        print(__doc__)
        sys.exit(2)
    path = args.brief
    try:
        rb = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        _emit(path, [f"not valid JSON: {e}"])
    if not isinstance(rb, dict):
        _emit(path, ["top level is not an object"])

    schema_path = Path(args.schema) if args.schema else DEFAULT_SCHEMA
    warnings = []
    try:
        schema = json.load(open(schema_path, encoding="utf-8"))
    except Exception as e:
        schema = None
        warnings.append(f"schema not readable at {schema_path} ({e}); ran the built-in v1 checks only")
        print(warnings[-1], file=sys.stderr)

    if schema is None:
        _emit(path, builtin_checks(rb), warnings)

    bl = check_schema(rb, schema)
    # Whitespace-only text passes minLength but is still useless to the writer.
    for key in ("thesis", "explanation_path", "suggested_outline"):
        if isinstance(rb.get(key), str) and not rb[key].strip():
            bl.append(f"$.{key}: blank")
    _emit(path, bl, warnings)


if __name__ == "__main__":
    main()
