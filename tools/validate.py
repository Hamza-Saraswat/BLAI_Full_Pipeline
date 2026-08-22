#!/usr/bin/env python3
"""Check an ICM workspace (or a repo of workspaces) against the ICM conventions.

Adapted from bin/validate.py proposed in RinDig/Interpretable-Context-Methodology
PR #14 (Avicennasis, MIT). Changes from upstream: runs on a single workspace
folder as well as a repo with workspaces/; three added rules (placeholder
coverage between the questionnaire and the files, with numbered families such as
PILLAR_2_ANGLE and PILLAR_N_ANGLE compared as one; no bracket-style placeholders;
balanced conditional sections, counting only markers that stand alone on a line);
a few more protocol-mandated names exempted from
the lowercase rule; folders whose name starts with "_" (such as _core and
_design) are treated as documentation and skipped by the placeholder rules.

Sources of truth: ICM-BUILD-GUIDE.md section 4 (patterns, naming, guardrails)
and section 5.2 (placeholder syntax).

Usage:
  python3 validate.py [workspace_or_repo_root] [--strict]

By default, style rules (line counts, em dashes, file naming) skip bundled
skills/ content, which is copied verbatim from upstream per Pattern 9.
--strict checks everything.

Exits 0 if all rules pass, 1 otherwise.
"""

import collections
import os
import re
import sys

EM_DASH = chr(0x2014)  # by codepoint: the rule forbids the literal
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", ".claude"}
# Filenames the spec itself mandates in non-lowercase form, plus dotfiles.
NAME_EXEMPT = {"CLAUDE.md", "CONTEXT.md", "CONVENTIONS.md", "README.md", "SKILL.md",
               "ICM-BUILD-GUIDE.md", "LICENSE", "LICENSE.txt", "LICENSE.md",
               "_core", "_design", ".gitkeep", ".gitignore", ".gitattributes",
               ".github", ".env", ".env.local", ".env.example"}
LOWER_RE = re.compile(r"^[a-z0-9]+([-._][a-z0-9]+)*$")
STAGE_RE = re.compile(r"^\d{2}-[a-z0-9]+(-[a-z0-9]+)*$")
# A path ref containing any of these is resolved at run time, not check time.
RUNTIME_MARKERS = ("{{", "[", "*")
PLACEHOLDER_LINKS = re.compile(
    r"\]\(\s*(link-to-\S*|TODO|TBD|url|example\.com\S*|#?)\s*\)", re.I)
VALUE_PH = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")
# Real conditional markers stand alone on a line; prose mentions are ignored.
COND_OPEN = re.compile(r"^\s*\{\{\?([A-Z][A-Z0-9_]*)\}\}\s*$", re.M)
COND_CLOSE = re.compile(r"^\s*\{\{/([A-Z][A-Z0-9_]*)\}\}\s*$", re.M)
BRACKET_PH = re.compile(r"\[[A-Z]+(?:_[A-Z]+)+\]")
# Generic tokens used when writing ABOUT placeholders, not as placeholders.
META_TOKENS = {"PLACEHOLDER", "PLACEHOLDERS", "PLACEHOLDER_NAME", "SCREAMING_SNAKE_CASE",
               "NAME", "SECTION", "SECTION_NAME", "VARIABLES", "VARIABLE"}

results = []
# BLAI deviation (documented in each workspace CLAUDE.md): text outputs are committed as the
# audit trail, so --allow-outputs skips the "only .gitkeep" rule. Binaries stay gitignored.
ALLOW_OUTPUTS = "--allow-outputs" in sys.argv


def rule(name, violations, note=""):
    results.append((name, list(violations), note))


def posix(rel):
    return "/" + rel.replace(os.sep, "/") + "/"


def is_vendored(rel):
    return "/skills/" in posix(rel)


def is_doc(rel):
    """Top-level folders starting with "_" hold conventions and planning docs."""
    return rel.replace(os.sep, "/").split("/")[0].startswith("_")


def in_output(rel):
    return "/output/" in posix(rel)


def family(name):
    """{{PILLAR_2_ANGLE}} and {{PILLAR_N_ANGLE}} are one family: digits become N."""
    return re.sub(r"_\d+(?=_|$)", "_N", name)


def walk_files(root, ext=None, skip_vendored=False):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            p = os.path.join(dp, f)
            r = os.path.relpath(p, root)
            if skip_vendored and is_vendored(r):
                continue
            if ext and not f.endswith(ext):
                continue
            yield r, p


def walk_dirs(root, skip_vendored=False):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for d in dn:
            p = os.path.join(dp, d)
            r = os.path.relpath(p, root)
            if skip_vendored and is_vendored(r):
                continue
            yield r, p


def read(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def sections(text):
    return [ln[3:].strip() for ln in text.splitlines() if ln.startswith("## ")]


def inputs_rows(text):
    """Yield cell-lists for each data row of the '## Inputs' table."""
    inside = False
    for ln in text.splitlines():
        if ln.startswith("## "):
            inside = ln.strip() == "## Inputs"
            continue
        if not inside or not ln.startswith("|"):
            continue
        if re.fullmatch(r"\|[-: |]+\|", ln.strip()):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells and cells[0] in ("Source", "File"):
            continue
        yield cells


def is_stage_context(rel):
    return os.path.basename(rel) == "CONTEXT.md" and "/stages/" in posix(rel)


def main(root, strict):
    root = os.path.abspath(root)
    V = not strict  # skip vendored skills/ for style rules unless --strict

    # -- Quality Guardrails -------------------------------------------------
    rule("CONTEXT.md under 80 lines",
         ["%s (%d)" % (r, len(read(p).splitlines()))
          for r, p in walk_files(root, ".md") if os.path.basename(r) == "CONTEXT.md"
          and len(read(p).splitlines()) > 80])

    L3 = ("references", "shared", "brand-vault", "design-system", "skills")
    rule("Reference files under 200 lines",
         ["%s (%d)" % (r, len(read(p).splitlines()))
          for r, p in walk_files(root, ".md", skip_vendored=V)
          if any("/%s/" % d in posix(r) for d in L3)
          and len(read(p).splitlines()) > 200])

    rule("No em dashes (U+2014)",
         ["%s (%d)" % (r, read(p).count(EM_DASH))
          for r, p in walk_files(root, (".md", ".txt", ".py", ".js", ".tsx"), skip_vendored=V)
          if EM_DASH in read(p)])

    rule("Empty persistent folders carry .gitkeep",
         [r for r, p in walk_dirs(root) if not os.listdir(p)])

    # -- Naming Conventions -------------------------------------------------
    rule("No spaces in file or folder names",
         sorted({r for r, _ in walk_files(root) if " " in r}
                | {r for r, _ in walk_dirs(root) if " " in r}))

    rule("Names are lowercase-with-hyphens",
         sorted({r for r, _ in list(walk_files(root, skip_vendored=V))
                 + list(walk_dirs(root, skip_vendored=V))
                 if os.path.basename(r) not in NAME_EXEMPT
                 and not LOWER_RE.match(os.path.basename(r))}))

    rule("Stage folders use a zero-padded numeric prefix",
         [r for r, _ in walk_dirs(root)
          if re.search(r"(^|/)stages/[^/]+$", r.replace(os.sep, "/"))
          and not STAGE_RE.match(os.path.basename(r))])

    # -- Pattern 1: stage contracts ----------------------------------------
    bad = []
    for r, p in walk_files(root, ".md"):
        if not is_stage_context(r):
            continue
        s = sections(read(p))
        try:
            if not s.index("Inputs") < s.index("Process") < s.index("Outputs"):
                bad.append("%s: out of order %s" % (r, s))
        except ValueError:
            bad.append("%s: missing Inputs/Process/Outputs, has %s" % (r, s))
    rule("Stage CONTEXT.md has Inputs, Process, Outputs in order", bad)

    # -- Pattern 4: every Inputs row names a section scope ------------------
    rule("Inputs rows carry a Section/Scope value",
         ["%s: %s" % (r, cells[:2])
          for r, p in walk_files(root, ".md") if is_stage_context(r)
          for cells in inputs_rows(read(p)) if len(cells) < 4 or not cells[2]])

    # -- Pattern 3: one-way cross-references --------------------------------
    # Works for both layouts: <root>/stages/NN-x and <root>/workspaces/<ws>/stages/NN-x
    edges = collections.defaultdict(set)
    for r, p in walk_files(root, ".md"):
        m = re.search(r"(?:(workspaces/[^/]+)/)?stages/(\d{2}-[a-z0-9-]+)/", posix(r))
        if not m:
            continue
        ws, src = (m.group(1) or "."), m.group(2)
        for tgt in set(re.findall(r"\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*", read(p))):
            if tgt != src and os.path.isdir(os.path.join(root, ws, "stages", tgt)):
                edges[(ws, src)].add(tgt)
    rule("Stage cross-references are one-way",
         sorted({"%s: %s <-> %s" % (ws, *sorted([s, t]))
                 for (ws, s), ts in edges.items() for t in ts
                 if s in edges.get((ws, t), ())}))

    # -- Pattern 2 / definition of done: no committed stage outputs ---------
    if not ALLOW_OUTPUTS:
        rule("Output folders contain only .gitkeep",
             ["%s: %s" % (r, sorted(set(os.listdir(p)) - {".gitkeep"}))
              for r, p in walk_dirs(root) if os.path.basename(r) == "output"
              and set(os.listdir(p)) - {".gitkeep"}])

    # -- Inputs-table paths actually resolve --------------------------------
    # The filesystem is the orchestration layer, so a wrong path here is an
    # uncaught bug. Per-run outputs are gitignored by design and are skipped.
    bad = []
    for r, p in walk_files(root, ".md"):
        if not is_stage_context(r):
            continue
        base = os.path.dirname(p)
        for cells in inputs_rows(read(p)):
            for ref in re.findall(r"`([^`]+)`", cells[1] if len(cells) > 1 else ""):
                ref = ref.strip()
                if not ref or ref.startswith("http"):
                    continue
                if not ("/" in ref or ref.endswith(".md")):
                    continue
                if any(m in ref for m in RUNTIME_MARKERS):
                    continue
                if re.search(r"/(output|input)/", ref):   # gitignored per-run artifact
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(base, ref))):
                    bad.append("%s -> %s" % (r, ref))
    rule("Inputs-table paths resolve", bad)

    # -- Every workspace is registered in both routing tables (repo layout) --
    ws_dir = os.path.join(root, "workspaces")
    bad = []
    if os.path.isdir(ws_dir):
        readme = read(os.path.join(root, "README.md")) if os.path.exists(
            os.path.join(root, "README.md")) else ""
        claude = read(os.path.join(root, "CLAUDE.md")) if os.path.exists(
            os.path.join(root, "CLAUDE.md")) else ""
        for w in sorted(os.listdir(ws_dir)):
            if not os.path.isdir(os.path.join(ws_dir, w)):
                continue
            missing = [n for n, t in (("README.md", readme), ("CLAUDE.md", claude))
                       if w not in t]
            if missing:
                bad.append("%s: absent from %s" % (w, ", ".join(missing)))
    rule("Every workspace is registered in README and root CLAUDE.md", bad)

    # -- No placeholder link targets ----------------------------------------
    rule("Markdown links have real targets",
         ["%s: %s" % (r, m.group(0))
          for r, p in walk_files(root, ".md", skip_vendored=V)
          for m in PLACEHOLDER_LINKS.finditer(read(p))])

    # -- Folders named in the README exist ----------------------------------
    bad = []
    readme_path = os.path.join(root, "README.md")
    if os.path.exists(readme_path):
        real = {os.path.basename(r) for r, _ in walk_dirs(root)}
        for name in sorted(set(re.findall(r"^\s{2,}([a-z_][a-z0-9_-]*)/\s+#",
                                          read(readme_path), re.M))):
            if name not in real:
                bad.append("README describes %s/ but no such directory exists" % name)
    rule("Directories described in the README exist", bad)

    # -- Placeholders: questionnaire <-> files, per workspace (added) -------
    bad = []
    for r, q in walk_files(root, ".md"):
        if is_doc(r) or r.replace(os.sep, "/").split("/")[-2:] != ["setup", "questionnaire.md"]:
            continue
        ws_root = os.path.dirname(os.path.dirname(q))
        label = os.path.relpath(ws_root, root)
        declared = {family(n) for n in VALUE_PH.findall(read(q))} - META_TOKENS
        used = collections.defaultdict(set)
        for r2, p2 in walk_files(ws_root, ".md"):
            if p2 == q or in_output(r2):
                continue
            for name in VALUE_PH.findall(read(p2)):
                if name not in META_TOKENS:
                    used[family(name)].add(r2)
        for name in sorted(set(used) - declared):
            bad.append("%s: {{%s}} in %s has no question"
                       % (label, name, ", ".join(sorted(used[name])[:3])))
        for name in sorted(declared - set(used)):
            bad.append("%s: question declares {{%s}} but no file contains it" % (label, name))
    rule("Placeholders match the questionnaire both ways", bad)

    # -- No bracket-style placeholders (added) ------------------------------
    rule("No bracket-style placeholders (use {{NAME}})",
         ["%s: %s" % (r, ", ".join(sorted(set(BRACKET_PH.findall(read(p))))[:4]))
          for r, p in walk_files(root, ".md", skip_vendored=V)
          if not is_doc(r) and not in_output(r) and BRACKET_PH.search(read(p))])

    # -- Conditional sections balanced (added) ------------------------------
    bad = []
    for r, p in walk_files(root, ".md"):
        if is_doc(r) or in_output(r):
            continue
        t = read(p)
        opens = collections.Counter(COND_OPEN.findall(t))
        closes = collections.Counter(COND_CLOSE.findall(t))
        for name in sorted(set(opens) | set(closes)):
            if opens[name] != closes[name]:
                bad.append("%s: {{?%s}} x%d vs {{/%s}} x%d"
                           % (r, name, opens[name], name, closes[name]))
    rule("Conditional sections are balanced", bad)

    # -- report -------------------------------------------------------------
    failed = 0
    for name, bad, note in results:
        if bad:
            failed += 1
            print("FAIL  %-52s %d" % (name, len(bad)))
            for b in bad[:6]:
                print("        - %s" % b)
            if len(bad) > 6:
                print("        ... and %d more" % (len(bad) - 6))
        else:
            print("PASS  %s" % name)
    print("\n%d/%d rules passed%s" % (len(results) - failed, len(results),
                                      "" if strict else "  (skills/ skipped; --strict to include)"))
    return 1 if failed else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    sys.exit(main(args[0] if args else ".", "--strict" in sys.argv))
