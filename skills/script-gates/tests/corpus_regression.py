#!/usr/bin/env python3
"""corpus_regression.py -- run every gate over the v1 corpus and assert the
recalibration did what it claimed.

The 38 shipped v1 boards are a free labelled regression set: the forensic pass
already knows which of them use the "stage one, stage two" template, which are
pinned to 113 seconds, and which four actually shipped. This runs the current
gates over all of them, prints a per-board table, and asserts five things:

  1  positional_labels fails EXACTLY the ten label boards and passes the two
     clean smooth boards of the same format.
  2  feeding the twelve smooth boards through variety_check in slug order fires
     `sameness` on the target_duration_s pin, and the byte-identical
     moe-local-rematch / moe-wake-up-trick pair trips it too.
  3  the four shipped boards pass `skeleton` (with "so" removed from the list)
     and pass the recalibrated `number_spend`.
  4  no board that passed the physics validator before now fails it: blocker
     counts are diffed against tests/baseline_validator.json, captured from the
     pre-change validate_storyboard.py over the same corpus.
  5  formats.json `person: you` activates the we/our/us advisory on a CLASSIC
     board (checked with a synthesised we-heavy copy, never a corpus edit).

The corpus repo is READ-ONLY: nothing here writes inside --corpus. Every
artifact goes to a temp directory that is removed on exit.

  corpus_regression.py [--corpus GLOB_DIR] [--baseline FILE] [--dry-run] [-v]

Exit 0 when every assertion holds, 1 when one fails, 2 on a usage error.
Stdlib only, Python 3.9+.
"""
import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
SCRIPTS = SKILL_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS))

import eval_short as E     # noqa: E402
import variety_check as V  # noqa: E402

DEFAULT_CORPUS = "/Users/hamzasaraswat/Documents/Projects/BLAI_Animator/out"
DEFAULT_BASELINE = HERE / "baseline_validator.json"
HISTORY = SKILL_DIR / "fixtures" / "history.json"

# --- the expectations (from the forensic pass; see the plan, section 11) ------
EXPECT_POSITIONAL_FAIL = {
    "63-of-companies-just-admitted-their",
    "deepseeks-new-model-just-beat-frontier",
    "format-how-to-title-will-qwen3-8-maxs-2-4",
    "simple-explanation-on-how-to-install",
    "title-dgx-spark-vs-mac-studio",
    "title-everyone-says-dgx-spark-is",
    "title-meta-just-shipped-a-free",
    "title-nvidias-nemotron-3-5-lightning-turn",
    "what-nvidias-new-dgx-spark-firmware",
    "z-ai-didnt-make-glm-5-3-bigger",
}
EXPECT_POSITIONAL_PASS = {"what-is-moe-mixture-of-experts", "what-is-the-dgx-spark-and"}
SHIPPED = ["gpu-doorway-bandwidth", "moe-wake-up-trick", "shrink-the-numbers",
           "three-laptops-one-brain-hook-our"]
DUP_PAIR = ("moe-local-rematch", "moe-wake-up-trick")


def boards(corpus):
    """(slug, storyboard path) for every board, keyed by DIRECTORY name.

    The directory name is the board identity here, not the storyboard's `slug`
    field: two corpus boards are byte-identical and share one internal slug.

    Pinned to the 38 slugs frozen in baseline_validator.json: the corpus dir is
    v1's LIVE output and its autopilot keeps adding boards (six landed between
    2026-08-24 and 2026-08-28), so an unpinned glob makes the assertions rot
    while the gates are innocent (finding 67)."""
    root = Path(corpus)
    frozen = set(json.loads((Path(__file__).parent / "baseline_validator.json")
                            .read_text())["boards"])
    found = [(p.parent.name, p) for p in sorted(root.glob("*/storyboard.json"))
             if p.parent.name in frozen]
    skipped = len(list(root.glob("*/storyboard.json"))) - len(found)
    if skipped:
        print("corpus: %d newer board(s) outside the frozen 38 ignored" % skipped)
    return found


def score(slug, sb_path, tmp, ledger=None):
    """Full eval for one board; research.json is used when the board has one."""
    res = sb_path.parent / "research.json"
    ev = E.build_eval(slug, str(sb_path), str(res) if res.exists() else None,
                      None, label=slug, history=str(HISTORY), ledger=ledger)
    (tmp / (slug + ".eval.json")).write_text(json.dumps(ev, indent=2))
    return ev


# --- assertions --------------------------------------------------------------
def assert_positional(rows, fails):
    got = {r["slug"] for r in rows if "positional_labels" in r["failures"]}
    ok = True
    missing, extra = EXPECT_POSITIONAL_FAIL - got, got - EXPECT_POSITIONAL_FAIL
    if missing:
        fails.append("positional_labels did NOT fail: %s" % sorted(missing))
        ok = False
    if extra:
        fails.append("positional_labels unexpectedly failed: %s" % sorted(extra))
        ok = False
    for slug in sorted(EXPECT_POSITIONAL_PASS):
        row = next((r for r in rows if r["slug"] == slug), None)
        if row is None:
            fails.append("expected-clean board missing from the corpus: %s" % slug)
            ok = False
        elif "positional_labels" in row["failures"]:
            fails.append("clean board failed positional_labels: %s" % slug)
            ok = False
    return ok, sorted(got)


def assert_sameness(corpus, fails):
    """Feed the smooth boards through the ledger in slug order, then the dup pair."""
    smooth = [(s, p) for s, p in boards(corpus)
              if (json.loads(p.read_text()).get("script_format") == "smooth-explainer")]
    tmp = Path(tempfile.mkdtemp(prefix="variety-"))
    ok = True
    try:
        ledger = tmp / "smooth-ledger.json"
        pin_hits, first_pin = [], None
        for slug, path in smooth:
            sb = json.loads(path.read_text())
            entry = V.ledger_entry(sb, date="2026-01-01", slug=slug)
            res = V.check_entry(entry, V.load_ledger(ledger))
            if any(v["rule"] == "target_duration_s" for v in res["violations"]):
                pin_hits.append(slug)
                first_pin = first_pin or slug
            V.append_entry(ledger, entry)
        if not pin_hits:
            fails.append("sameness never fired on the target_duration_s pin")
            ok = False

        # the byte-identical pair
        dup_ledger = tmp / "dup-ledger.json"
        a, b = DUP_PAIR
        sa = json.loads((Path(corpus) / a / "storyboard.json").read_text())
        sbb = json.loads((Path(corpus) / b / "storyboard.json").read_text())
        V.append_entry(dup_ledger, V.ledger_entry(sa, date="2026-01-01", slug=a))
        dup = V.check_entry(V.ledger_entry(sbb, date="2026-01-02", slug=b),
                            V.load_ledger(dup_ledger))
        rules = {v["rule"] for v in dup["violations"]}
        if dup["ok"] or "opener_bigrams" not in rules:
            fails.append("sameness did not fire on the identical %s / %s pair "
                         "(violations: %s)" % (a, b, sorted(rules)))
            ok = False
        shared = sum(x.get("shared", 0) for x in dup["advisories"])
        if not shared:
            fails.append("repeated_phrase advisory silent on the identical pair")
            ok = False
        return ok, {"smooth_boards": len(smooth), "pin_hits": pin_hits,
                    "dup_rules": sorted(rules), "dup_shared_phrases": shared}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def assert_shipped(rows, fails):
    ok, detail = True, {}
    for slug in SHIPPED:
        row = next((r for r in rows if r["slug"] == slug), None)
        if row is None:
            fails.append("shipped board missing from the corpus: %s" % slug)
            ok = False
            continue
        detail[slug] = {"skeleton": row["skeleton_density"],
                        "number_spend": row["detail"]["number_spend"]}
        for gate in ("skeleton", "number_spend"):
            if gate in row["failures"]:
                fails.append("shipped board %s still fails %s" % (slug, gate))
                ok = False
    return ok, detail


def assert_no_physics_regression(rows, baseline_path, fails):
    try:
        base = json.loads(Path(baseline_path).read_text())["boards"]
    except Exception as e:
        fails.append("baseline unreadable (%s): %s" % (baseline_path, e))
        return False, {}
    ok, changed = True, {}
    for r in rows:
        was = (base.get(r["slug"]) or {}).get("blockers")
        now = r["blockers"]
        if was is None:
            changed[r["slug"]] = {"before": None, "after": now, "note": "not in baseline"}
            continue
        if now != was:
            changed[r["slug"]] = {"before": was, "after": now}
            if now > was:
                fails.append("physics regression: %s blockers %d -> %d"
                             % (r["slug"], was, now))
                ok = False
    return ok, changed


def assert_person_activates(corpus, fails):
    """formats.json person=you must switch the we/our advisory on for CLASSIC."""
    import subprocess
    src = Path(corpus) / "shrink-the-numbers" / "storyboard.json"
    if not src.exists():
        fails.append("cannot check the person advisory: %s missing" % src)
        return False, {}
    sb = json.loads(src.read_text())
    if sb.get("script_format"):
        fails.append("person check needs a classic board; %s is %s"
                     % (src.parent.name, sb["script_format"]))
        return False, {}
    extra = " We ran it, we measured it, our box, and we saw us win."
    sb["scenes"][-1]["narration"] += extra
    sb["narration_full"] += extra
    tmp = Path(tempfile.mkdtemp(prefix="person-"))
    try:
        f = tmp / "we-heavy.json"
        f.write_text(json.dumps(sb))
        p = subprocess.run([sys.executable, str(SCRIPTS / "validate_storyboard.py"),
                            str(f), "--history", str(HISTORY)],
                           capture_output=True, text=True)
        adv = (json.loads(p.stdout) or {}).get("advisories") or []
        hit = [a for a in adv if "first-person-plural" in a]
        if not hit:
            fails.append("person=you did not activate the we/our advisory for classic")
            return False, {"advisories": len(adv)}
        return True, {"advisory": hit[0]}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --- table -------------------------------------------------------------------
def print_table(rows):
    head = ("board", "fmt", "lbl", "skel", "spend", "blk", "failures")
    print("%-42s %-6s %3s %6s %7s %4s  %s" % head)
    print("-" * 118)
    for r in rows:
        ns = r["detail"]["number_spend"]
        spend = "%s/%s" % (ns.get("spent"), ns.get("total"))
        print("%-42s %-6s %3d %6.3f %7s %4s  %s" % (
            r["slug"][:42], "smooth" if r["fmt"] != "classic" else "class",
            r["labels"], r["skeleton_density"], spend,
            r["blockers"] if r["blockers"] is not None else "-",
            ",".join(r["failures"]) or "-"))


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="corpus_regression.py",
        description="Run every script gate over the v1 storyboard corpus and assert "
                    "the recalibration's expected results.",
        epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", default=DEFAULT_CORPUS,
                    help="directory holding <slug>/storyboard.json (default: %s). "
                         "READ-ONLY: nothing is written inside it." % DEFAULT_CORPUS)
    ap.add_argument("--baseline", default=str(DEFAULT_BASELINE),
                    help="pre-change validator blocker counts (default: %s)" % DEFAULT_BASELINE)
    ap.add_argument("--dry-run", action="store_true",
                    help="list the boards that would be scored and exit 0; run nothing")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="print the assertion detail blocks as JSON")
    a = ap.parse_args(argv)

    found = boards(a.corpus)
    if not found:
        print("error: no <slug>/storyboard.json under %s" % a.corpus, file=sys.stderr)
        return 2
    if a.dry_run:
        print(json.dumps({"dry_run": True, "corpus": a.corpus,
                          "boards": [s for s, _ in found],
                          "baseline": a.baseline}, indent=2))
        return 0

    tmp = Path(tempfile.mkdtemp(prefix="corpus-regression-"))
    fails = []
    try:
        rows = []
        for slug, path in found:
            ev = score(slug, path, tmp)
            bm, ov = ev["board_metrics"], ev["overall"]
            vout = ((ev.get("validators") or {}).get("storyboard") or {}).get("output") or {}
            bl = vout.get("blockers")
            rows.append({
                "slug": slug,
                "fmt": ev["script_format"],
                "labels": bm["positional_labels"]["count"],
                "skeleton_density": bm["skeleton"]["density"],
                "blockers": len(bl) if isinstance(bl, list) else None,
                "failures": ov["failures"],
                "detail": ov["detail"],
            })
        print_table(rows)
        print()

        results = []
        ok1, got = assert_positional(rows, fails)
        results.append(("1 positional_labels fails exactly the 10 label boards, "
                        "passes the 2 clean smooth boards", ok1,
                        {"failed": got, "expected": sorted(EXPECT_POSITIONAL_FAIL),
                         "expected_pass": sorted(EXPECT_POSITIONAL_PASS)}))
        ok2, d2 = assert_sameness(a.corpus, fails)
        results.append(("2 sameness fires on the 113s pin and the identical "
                        "moe pair", ok2, d2))
        ok3, d3 = assert_shipped(rows, fails)
        results.append(("3 the 4 shipped boards pass skeleton and number_spend", ok3, d3))
        ok4, d4 = assert_no_physics_regression(rows, a.baseline, fails)
        results.append(("4 no new validator blockers vs the pre-change baseline",
                        ok4, {"changed": d4}))
        ok5, d5 = assert_person_activates(a.corpus, fails)
        results.append(("5 person=you activates the we/our advisory for classic",
                        ok5, d5))

        print("ASSERTIONS")
        for name, ok, detail in results:
            print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
            if a.verbose:
                print("        " + json.dumps(detail)[:1000])
        print()
        if fails:
            print("FAILED (%d):" % len(fails))
            for f in fails:
                print("  - " + f)
            return 1
        print("all assertions hold over %d boards" % len(rows))
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
