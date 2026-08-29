#!/usr/bin/env python3
"""eval_short.py — did the storyboard SPEND the research's specifics?

The v3 storyboard writer is free to tell the story any way it likes; the one
thing it may not do is throw away the concrete material the research found.
This scores exactly that, plus the stage telemetry around it.

  eval_short.py --storyboard P --research P [--label NAME] [--out P] [--history P]
  eval_short.py <slug> [--root DIR]        -> DIR/out/<slug>/eval.json (v1 tree only)
  eval_short.py --report [--diff old:new] [--out P]

v2 port: lives in skills/script-gates/scripts/. formats.json and voice.config.json
(wps) are read from skills/script-gates/; validate_storyboard.py is the sibling
script; validate_research.py is skills/blai-research/scripts/validate_research.py.
Stages pass explicit --storyboard/--research/--out paths; the <slug> form needs a
v1-style out/<slug>/ tree under --root. --report scans out/*/eval.json and
workspaces/*/stages/*/output/*eval.json.

GATES (Gate-1 delegation contract; thresholds come from formats.json, see
gates_for(); the GATE_FALLBACKS dict below is only a per-key safety net)
  number_spend       classic: at least 2 and at most 5 key numbers spent;
                     smooth-explainer: a cap of 3. The floor is clamped to the
                     brief's own total so a thin brief cannot make it unreachable
  entity_spend       >= 0.5 of the filtered named-entity set (ADVISORY since finding 9)
  top2               both top-ranked entities present (ADVISORY since finding 9)
  hook_concrete      hook + first sentence carries a digit/number/entity
  scene_specificity  every scene but one (classic) / but two (smooth) carries a key
                     number, a named entity or a glossary term from the brief
  skeleton           sentence-initial First/Then/Next/Finally <= 0.15 ("so" is
                     natural speech and was removed from the list)
  positional_labels  no "stage one / step two" template; see POSITIONAL_RE
  sameness           not the same shape/hook/ending/length/rhythm as the last
                     five ledger entries. ONLY runs when --ledger is passed
  validator          validate_storyboard.py reports zero blockers

Exit 0 = gates pass (or report written) - 4 = gates fail - 2 = usage/IO error.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
# v2 port: scripts/ -> skills/script-gates/ -> skills/ -> repo root.
SKILL_DIR = Path(__file__).resolve().parents[1]  # skills/script-gates (formats.json, voice.config.json)
REPO_ROOT = Path(__file__).resolve().parents[3]  # repo root (repointed from the v1 "has out/" guess)
RESEARCH_VALIDATOR = REPO_ROOT / "skills" / "blai-research" / "scripts" / "validate_research.py"  # repointed from pipeline/scripts/
WPS = 2.6  # historical default; _wps() below prefers the pinned voice's measured rate


def _format_cfg(fmt):
    """Band knobs for a script format from skills/script-gates/formats.json; {} on any miss.
    (Reading a data file keeps this script single-file/stdlib — it already
    reads storyboard.json, research.json and dashboard project records.)"""
    try:
        return json.loads((SKILL_DIR / "formats.json").read_text())["formats"][fmt]  # repointed
    except Exception:
        return {}


def _wps(fmt="classic"):
    """Words/sec, in preference order: the pinned voice's measured per-format
    rate (voice.config.json `wps_by_format[fmt]`) > its flat `wps` > the band's
    `wps_fallback` in formats.json > 2.6."""
    try:
        cfg = json.loads((SKILL_DIR / "voice.config.json").read_text())  # repointed
    except Exception:
        cfg = {}
    by_fmt = cfg.get("wps_by_format") or {}
    w = by_fmt.get(fmt) if isinstance(by_fmt, dict) else None
    if not w:
        w = cfg.get("wps")
    if w:
        return float(w)
    return float(_format_cfg(fmt).get("wps_fallback", WPS))

# --- validator helpers -------------------------------------------------------
# Prefer the canonical implementations so sentence splitting / FK match the
# machine gate exactly; fall back to identical copies when the validator is not
# importable (e.g. running the harness standalone against exported artifacts).
try:
    sys.path.insert(0, str(HERE))
    from validate_storyboard import fk_grade, sentences, words  # type: ignore
except Exception:  # pragma: no cover - fallback path
    def sentences(text):
        parts = re.split(r"(?<=[.!?])\s+", (text or "").strip())
        return [p for p in parts if re.search(r"\w", p)]

    def words(text):
        return re.findall(r"[\w']+", text or "")

    def _syllables(word):
        w = word.lower().strip("'")
        if not w:
            return 0
        n = len(re.findall(r"[aeiouy]+", w))
        if w.endswith("e") and n > 1 and not w.endswith(("le", "ee", "ye")):
            n -= 1
        return max(1, n)

    def fk_grade(text):
        sents, ws = sentences(text), words(text)
        if not sents or not ws:
            return 0.0
        syl = sum(_syllables(w) for w in ws)
        return 0.39 * (len(ws) / len(sents)) + 11.8 * (syl / len(ws)) - 15.59

# formats.json is the single source of truth for every gate threshold.
# GATE_FALLBACKS is a per-key safety net used only when the file is missing or a
# key is absent from it; it must mirror the shipped formats.json values.
# variety_check.py is the sibling library behind the `sameness` gate. It is
# optional: without it (or without --ledger) the gate simply does not run.
try:
    from variety_check import check_entry as _vc_check  # type: ignore
    from variety_check import ledger_entry as _vc_entry  # type: ignore
    from variety_check import load_ledger as _vc_load  # type: ignore
except Exception:  # pragma: no cover
    _vc_check = _vc_entry = _vc_load = None

GATE_FALLBACKS = {
    "classic": {
        "number_spend": {"min_count": 2, "max_count": 5},
        "entity_spend": {"min_ratio": 0.5},
        "top2": {"required": True},
        "hook_concrete": {"required": True},
        "scene_specificity": {"allow_generic": 1},
        "skeleton": {"max_density": 0.15},
        "positional_labels": {"allowed_structures": ["how-to-three-moves", "worked-example"],
                              "max_labels": 3, "min_label_words": 6},
        "sameness": {"window": 5},
        "validator": {"max_blockers": 0},
    },
    # smooth-explainer inverts two gates: numbers are a CAP (the format spends
    # 1-3, each on its own beat; see rules/format-bands.md), and the hook opens
    # on a situation, so no digit/entity is required in it. It also buys one
    # extra non-specific scene, which is where a wry beat or direct address goes.
    "smooth-explainer": {
        "number_spend": {"max_count": 3},
        "entity_spend": {"min_ratio": 0.5},
        "top2": {"required": True},
        "hook_concrete": {"required": False},
        "scene_specificity": {"allow_generic": 2},
        "skeleton": {"max_density": 0.15},
        "positional_labels": {"allowed_structures": ["how-to-three-moves", "worked-example"],
                              "max_labels": 3, "min_label_words": 6},
        "sameness": {"window": 5},
        "validator": {"max_blockers": 0},
    },
}
GATES = GATE_FALLBACKS["classic"]  # back-compat alias


def _merge(fallback, override, keys):
    out = dict(fallback)
    if isinstance(override, dict):
        for k in keys:
            if k in override:
                out[k] = override[k]
    return out


def gates_for(fmt):
    """Gate thresholds for a script format, READ FROM formats.json.

    Every threshold below lives in skills/script-gates/formats.json; a key the
    file does not carry falls back to GATE_FALLBACKS. The one non-merge case is
    `numbers`: when the file states a numbers block at all, it is taken whole,
    so a format that declares only `max_count` genuinely has no floor."""
    fb = GATE_FALLBACKS.get(fmt) or GATE_FALLBACKS["classic"]
    cfg = _format_cfg(fmt)
    nums = cfg.get("numbers") if isinstance(cfg.get("numbers"), dict) else {}
    if "min_count" in nums or "max_count" in nums:
        number_spend = {k: nums[k] for k in ("min_count", "max_count") if k in nums}
    else:
        number_spend = dict(fb["number_spend"])
    hook_cfg = cfg.get("hook") if isinstance(cfg.get("hook"), dict) else {}
    return {
        "number_spend": number_spend,
        "entity_spend": _merge(fb["entity_spend"], cfg.get("entity_spend"), ("min_ratio",)),
        "top2": _merge(fb["top2"], cfg.get("top2"), ("required",)),
        "hook_concrete": {"required": bool(hook_cfg.get("concrete_required",
                                                        fb["hook_concrete"]["required"]))},
        "scene_specificity": _merge(fb["scene_specificity"], cfg.get("scene_specificity"),
                                    ("allow_generic",)),
        "skeleton": _merge(fb["skeleton"], cfg.get("skeleton"), ("max_density",)),
        "positional_labels": _merge(fb["positional_labels"], cfg.get("positional_labels"),
                                    ("allowed_structures", "max_labels", "min_label_words")),
        "sameness": _merge(fb["sameness"], cfg.get("sameness"), ("window",)),
        "validator": _merge(fb["validator"], cfg.get("validator"), ("max_blockers",)),
    }

# --- number vocabulary -------------------------------------------------------
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
SCALES = [(1_000_000_000, "billion"), (1_000_000, "million"), (1_000, "thousand")]
MONTHS = ["january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december"]
ORDINALS = {1: "first", 2: "second", 3: "third", 5: "fifth", 8: "eighth",
            9: "ninth", 12: "twelfth", 13: "thirteenth", 20: "twentieth",
            21: "twenty-first", 22: "twenty-second", 23: "twenty-third",
            30: "thirtieth", 31: "thirty-first"}

UNIT_WORDS = {
    "gb/s": ["gb/s", "gigabytes per second", "gigabytes a second"],
    "tb/s": ["tb/s", "terabytes per second"],
    "tok/s": ["tok/s", "tokens per second", "tokens a second"],
    "gb": ["gb", "gigabytes", "gigabyte", "gigs", "gig"],
    "mb": ["mb", "megabytes", "megabyte"],
    "tb": ["tb", "terabytes", "terabyte"],
    "ms": ["ms", "milliseconds", "millisecond"],
    "s": ["seconds", "second"],
    "w": ["watts", "watt"],
    "%": ["%", "percent", "per cent"],
    "x": ["x", "times"],
    "b": ["b", "billion", "billion-parameter"],
    "days": ["days", "day"],
    "weeks": ["weeks", "week"],
    "hours": ["hours", "hour"],
    "$": ["dollars", "dollar"],
}
STOPWORDS = set("""the a an of for and or in on at to is are was were be been being with
that this these those it its your you our their they them he she as by from into over under
per about which who whom what when where how not no than then so but if while can could may
might will would should must have has had do does did just only also more most much many very
each every some any other another same such own""".split())

ENTITY_STOP = set("""The A An And But For With When Where While Before After Since Because If
This That These Those Your Our Their Its It They You We He She There Here Data Information
Content Consumer Free Plus Team Business Enterprise Inputting Running Pasting Deleting Using
Once Every Each Both Most Many Some Any No Not Only Also Even Still Yet Just How What Why Who
On In At To Of By From Into Over Under Per About Which AI IT US OK Open Local Third New""".split())
# generic tech acronyms are vocabulary, not named examples
ENTITY_STOP |= set("""API RAM GPU CPU VRAM LLM LLMs PDF URL FAQ CEO CTO SaaS
HTTP HTTPS JSON CSV UI UX OS PC GB MB TB SSD HDD PROCESSOR MEMORY STORAGE
DISK MODEL TOKEN TOKENS SWAP""".split())
LEADING_STOP_EXTRA = {"More", "Less", "Most", "Fewer", "Enough"}
ENTITY_STOP |= {m.capitalize() for m in MONTHS}
ENTITY_STOP |= {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                "Saturday", "Sunday"}

# "so" was REMOVED from this list: it opens ~5.8% of sentences in both formats,
# it is natural speech rather than scaffolding, and banning it is what pushed the
# writer into "Stage two:" (see rules/eval-gates.md and the positional_labels
# gate below). The 0.15 density cap is unchanged.
SKELETON_RE = re.compile(
    r"^\s*(first|second|third|then|next|finally|lastly|and then)\b[,]?", re.I)

# --- positional labels ("stage one, stage two") ------------------------------
# The template the corpus collapsed into: `stage` opens 8.6% of every sentence in
# the smooth-explainer scripts. Matched at the start of a sentence, optionally
# behind a leading "And "/"But ", an "in " and a "that's".
POSITIONAL_RE = re.compile(
    r"^\s*(?:(?:and|but)\s+)?(?:in\s+)?(?:that['\u2019]s\s+)?"
    r"(stage|step|part|phase)\s+"
    r"(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b", re.I)

_ORDINAL_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                  "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

# Action-verb heuristic. It exists to let a LEGITIMATE imperative label through
# ("Stage two, you cap the context window at four thousand tokens.") and to catch
# the three empty labels the corpus shipped ("Stage three.", "Stage four, then.",
# "Stage four is the strange one."). It is deliberately GENEROUS, because a false
# failure here blocks a good script:
#   a label sentence carries an action verb when it contains either
#     (a) a word in ACTION_VERBS, or
#     (b) ANY word ending in -s, -ed or -ing that is not in NON_VERB_STOP.
# NON_VERB_STOP holds only copulas, auxiliaries, pronouns and function words,
# never ordinary nouns, so almost anything that describes an action passes.
ACTION_VERBS = set("""
measure shrink load run cap send swap quantize install pull set open close check
build write read add batch boot bring cache click clone compare compile copy count
cut download drop export feed find fix flash get give go hit hold import index keep
know leave let make merge mount move name pass paste patch pick plug point prune push
put route save scale see ship show size split stack start stop store stream switch
take tell test train trim try tune turn type unzip upload use wait wake want watch
wire work choose
""".split())
NON_VERB_STOP = set("""
is was has does this its his hers theirs yours ours us as thus plus less unless yes
across towards besides versus whereas news series gas bias
nothing something anything everything during being having always sometimes perhaps
thing things string strings ceiling morning evening
indeed instead ahead hundred red
""".split())


def has_action_verb(sentence):
    """Generous action-verb test; see the comment above ACTION_VERBS.

    A contraction is judged on its head ("that's" -> "that", "you're" -> "you"),
    so the -s branch cannot mistake "That's" for a verb."""
    for w in re.findall(r"[A-Za-z]+(?:['\u2019][A-Za-z]+)*", sentence or ""):
        t = re.split(r"['\u2019]", w.lower())[0]
        if not t or t in NON_VERB_STOP:
            continue
        if t in ACTION_VERBS:
            return True
        if t.endswith(("ing", "ed", "s")):
            return True
    return False


def find_positional_labels(narration):
    """Every sentence of `narration` that opens with a positional label."""
    out = []
    for i, sent in enumerate(sentences(narration or "")):
        m = POSITIONAL_RE.match(sent)
        if not m:
            continue
        raw = m.group(2).lower()
        ordinal = _ORDINAL_WORDS.get(raw)
        if ordinal is None:
            try:
                ordinal = int(raw)
            except ValueError:
                ordinal = None
        out.append({"sentence_index": i, "sentence": sent, "label": m.group(1).lower(),
                    "ordinal": ordinal, "words": len(words(sent)),
                    "has_action_verb": has_action_verb(sent)})
    return out

# capitalized words that start a sentence/phrase but never start a real name
LEADING_STOP = {"In", "On", "At", "To", "Of", "By", "From", "With", "Before",
                "After", "Since", "Because", "If", "When", "Where", "While",
                "And", "But", "For", "The", "A", "An", "This", "That", "These",
                "Those", "Once", "Every", "Each", "Both", "Most", "Many",
                "Some", "Any", "No", "Not", "Only", "Also", "Even", "Still",
                "Yet", "Just", "How", "What", "Why", "Who", "Running",
                "Inputting", "Pasting", "Deleting", "Using", "Data", "Its",
                "Information", "Content", "Your", "Our", "Their", "It", "They"}
# product-tier qualifiers that wrap a real product name
TIER_WORDS = {"Consumer", "Standard", "Public", "Personal", "Individual",
              "Free", "Plus", "Team", "Business", "Enterprise", "API", "Inc",
              "LLC", "Tier", "Tiers", "Plan", "Plans"}


def int_to_words(n):
    """0..999,999,999,999 -> english words (spaced tens; hyphen variant added later)."""
    n = int(n)
    if n < 0:
        return ""
    if n < 20:
        return ONES[n]
    if n < 100:
        t, r = divmod(n, 10)
        return TENS[t] + ("" if r == 0 else " " + ONES[r])
    if n < 1000:
        h, r = divmod(n, 100)
        return ONES[h] + " hundred" + ("" if r == 0 else " " + int_to_words(r))
    for scale, name in SCALES:
        if n >= scale:
            major, rest = divmod(n, scale)
            out = int_to_words(major) + " " + name
            if rest:
                out += " " + int_to_words(rest)
            return out
    return str(n)


def _sig_round(n, digits):
    """2190294 -> (2, 'million') for digits=1 ; (2.2, 'million') for digits=2."""
    for scale, name in SCALES:
        if n >= scale:
            v = n / scale
            v = round(v, max(0, digits - 1))
            if abs(v - round(v)) < 1e-9:
                v = int(round(v))
            return v, name
    return None, None


def _num_word(v):
    """2 -> 'two' ; 2.2 -> 'two point two'."""
    if isinstance(v, int) or float(v).is_integer():
        return int_to_words(int(v))
    whole, frac = str(v).split(".")
    return int_to_words(int(whole)) + " point " + " ".join(
        ONES[int(d)] for d in frac)


def parse_value(value):
    """Value string -> list of facts. Each: {kind, num, unit, currency}."""
    v = (value or "").strip()
    approx = bool(re.match(r"^\s*(~|≈|about|around|at least|up to|under|over|<|>)",
                           v, re.I))
    facts = []
    low = v.lower()
    for mi, mon in enumerate(MONTHS, start=1):
        if re.search(r"\b" + mon + r"\b", low):
            day = re.search(r"\b" + mon + r"\s+(\d{1,2})\b", low)
            year = re.search(r"\b(19|20)\d{2}\b", low)
            facts.append({"kind": "date", "month": mi, "month_name": mon,
                          "day": int(day.group(1)) if day else None,
                          "year": int(year.group(0)) if year else None})
            break
    if facts:
        return facts, approx
    for m in re.finditer(r"([$£€])?\s?(\d[\d,]*(?:\.\d+)?)\s*([A-Za-z%][\w/]*)?", v):
        cur, raw, unit = m.group(1), m.group(2), (m.group(3) or "").lower()
        try:
            num = float(raw.replace(",", ""))
        except ValueError:
            continue
        if unit in ("in", "of", "to", "and", "a", "the"):
            unit = ""
        # "20 million" — the magnitude belongs to the number, not the unit,
        # else no "twenty million" candidate is ever generated
        scale_map = {"thousand": 1_000, "million": 1_000_000,
                     "billion": 1_000_000_000, "trillion": 1_000_000_000_000}
        if unit in scale_map:
            num *= scale_map[unit]
            unit = ""
            tail2 = v[m.end():].lstrip().lower()
            um = re.match(r"([a-z%/]+)", tail2)
            if um and um.group(1) in ("tokens", "chats", "logs", "users", "rows"):
                unit = ""
        tail = v[m.end():m.end() + 8].lower()
        if unit in ("", None) and tail.startswith("/"):
            unit = tail[1:].split()[0] if len(tail) > 1 else ""
        facts.append({"kind": "num", "num": num, "unit": unit,
                      "currency": cur or ("$" if "$" in v else None)})
    return facts, approx


def candidates_for(fact):
    """-> list of (token, strength) where strength in {'strong','weak'}."""
    out = []
    if fact["kind"] == "date":
        mon = fact["month_name"]
        if fact.get("day"):
            d = fact["day"]
            out.append((f"{mon} {d}", "strong"))
            if d in ORDINALS:
                out.append((f"{mon} {ORDINALS[d]}", "strong"))
        if fact.get("year"):
            out.append((f"{mon} {fact['year']}", "strong"))
        if not fact.get("day") and not fact.get("year"):
            out.append((mon, "weak"))
        return out

    n, unit, cur = fact["num"], (fact.get("unit") or ""), fact.get("currency")
    is_int = float(n).is_integer()
    ival = int(n) if is_int else None
    digits_plain = (f"{ival:,}" if is_int else f"{n:g}")
    digits_bare = (str(ival) if is_int else f"{n:g}")

    # bare numerals / number-words: weak unless a unit or currency rides along
    out.append((digits_plain, "weak"))
    if digits_bare != digits_plain:
        out.append((digits_bare, "weak"))
    if is_int and ival <= 1000:
        w = int_to_words(ival)
        out.append((w, "weak"))
        if " " in w:
            out.append((w.replace(" ", "-"), "weak"))
    if not is_int:
        out.append((_num_word(n), "weak"))

    if cur:
        out.append((f"{cur}{digits_plain}", "strong"))
        out.append((f"{cur}{digits_bare}", "strong"))
        if is_int and ival <= 1000:
            out.append((f"{int_to_words(ival)} dollars", "strong"))

    # magnitude roundings — how a script actually says a big number
    if n >= 10_000:
        for digits in (1, 2):
            val, name = _sig_round(n, digits)
            if val is None:
                continue
            vs = f"{val:g}"
            out.append((f"{vs} {name}", "strong"))
            out.append((f"{_num_word(val)} {name}", "strong"))
            letter = {"billion": "B", "million": "M", "thousand": "K"}[name]
            out.append((f"{vs}{letter}", "strong"))
            if cur:
                out.append((f"{cur}{vs}{letter}", "strong"))
                out.append((f"{cur}{vs} {name}", "strong"))
                out.append((f"{_num_word(val)} {name} dollars", "strong"))

    # Rounded forms. House style (AGENTS.md) is "numbers rounded to what a viewer
    # can hold", so a script SHOULD say "forty-one gigabytes" for 41.42 GB. Without
    # these candidates the writer is penalised for following the style guide.
    rounded = []
    if not is_int:
        r = int(round(n))
        if r > 0 and abs(r - n) / n < 0.25:
            rounded.append(r)
        if n >= 10 and int(n) != r:
            rounded.append(int(n))          # also accept truncation ("forty-one")
    for r in rounded:
        out.append((str(r), "weak"))
        if r <= 1000:
            w = int_to_words(r)
            out.append((w, "weak"))
            if " " in w:
                out.append((w.replace(" ", "-"), "weak"))
        for key, syns in UNIT_WORDS.items():
            if unit == key or (unit and unit.rstrip("s") == key.rstrip("s")):
                for s in syns:
                    out.append((f"{r}{s}" if s in ("%", "x") else f"{r} {s}", "strong"))
                    if r <= 1000:
                        rw = int_to_words(r)
                        out.append((f"{rw} {s}", "strong"))
                        if " " in rw:
                            out.append((f"{rw.replace(' ', '-')} {s}", "strong"))
                break

    # units make any form strong
    for key, syns in UNIT_WORDS.items():
        if unit == key or (unit and unit.rstrip("s") == key.rstrip("s")):
            for s in syns:
                out.append((f"{digits_bare}{s}" if s in ("%", "x") else f"{digits_bare} {s}", "strong"))
                out.append((f"{digits_plain} {s}", "strong"))
                if is_int and ival <= 1000:
                    out.append((f"{int_to_words(ival)} {s}", "strong"))
                elif not is_int:
                    out.append((f"{_num_word(n)} {s}", "strong"))
            if unit == "x" and is_int and ival in (2, 3):
                out.append(({2: "twice", 3: "triple"}[ival], "strong"))
            break

    seen, uniq = set(), []
    for tok, strength in out:
        tok = tok.strip()
        if not tok or tok in seen:
            continue
        seen.add(tok)
        uniq.append((tok, strength))
    return uniq


def _tok_regex(token):
    """Build the match pattern by joining escaped parts, never by chained
    replaces on an escaped string (that corrupts the character classes)."""
    parts = [p for p in re.split(r"[\s\-]+", token.strip()) if p]
    esc = [re.escape(p).replace(r"\$", r"\$\s?") for p in parts]
    body = r"[\s\-]+".join(esc)
    return re.compile(r"(?<![\w$])" + body + r"(?![\w%])", re.I)


def label_context(label):
    return {w for w in re.findall(r"[a-z0-9]+", (label or "").lower())
            if len(w) >= 4 and w not in STOPWORDS}


def find_token(token, strength, corpus, ctx_words):
    """Return match text or None. Weak tokens need label context within +/-3 words."""
    rx = _tok_regex(token)
    for m in rx.finditer(corpus):
        if strength == "strong":
            return m.group(0)
        if not ctx_words:
            continue
        before = re.findall(r"[a-z0-9']+", corpus[:m.start()].lower())[-3:]
        after = re.findall(r"[a-z0-9']+", corpus[m.end():].lower())[:3]
        if ctx_words & set(before + after):
            return m.group(0)
    return None


# --- entities ---------------------------------------------------------------
def _is_product_token(tok):
    return (re.fullmatch(r"[A-Z]{3,}", tok)
            or re.search(r"[a-z][A-Z]", tok)
            or (re.search(r"[A-Za-z]", tok) and re.search(r"\d", tok)))


def _trim_name(name):
    """Strip leading connectives/qualifiers, tier wrappers, and anything past a
    sentence boundary ("ChatGPT. The" is two sentences, not a name)."""
    name = re.sub(r"'s\b", "", name)
    name = re.split(r"(?<=[.!?])\s+", name)[0]
    toks = [t for t in name.split() if t]
    while toks and (toks[0].capitalize() in LEADING_STOP
                    or toks[0] in LEADING_STOP_EXTRA
                    or toks[0] in TIER_WORDS or toks[0].islower()):
        toks.pop(0)
    while toks and (toks[-1] in TIER_WORDS or toks[-1].islower()):
        toks.pop()
    return " ".join(toks).rstrip(".")


def extract_entities(research):
    src = [c.get("claim", "") for c in research.get("claims", [])]
    src.append(research.get("thesis", ""))
    for m in research.get("misconceptions", []):
        src.append(m.get("myth", ""))
        src.append(m.get("reality", ""))
    text = "\n".join(t for t in src if t)

    found = {}

    def add(name, kind):
        name = name.strip()
        if not name:
            return
        key = name.lower()
        found.setdefault(key, {"name": name, "kind": kind})

    for m in re.finditer(r"\b([A-Z][\w.\-]+)\s+v\.?\s+([A-Z][\w.\-]+)", text):
        add(f"{m.group(1)} v. {m.group(2)}", "case")
    joiner = r"(?:of|the|for|and|&)"
    multi = re.compile(
        r"\b([A-Z][A-Za-z0-9.&'\-]*(?:\s+(?:" + joiner + r"\s+)?[A-Z][A-Za-z0-9.&'\-]*)+"
        r"(?:\s+\d+(?:\.\d+)?)?)")
    for m in multi.finditer(text):
        name = _trim_name(m.group(1))
        # "GPU VRAM" / "RAM the OS" are generic vocabulary wearing capital letters,
        # not named examples — drop when every surviving token is a stopword.
        if name and all(t in ENTITY_STOP or t.islower() for t in name.split()):
            continue
        if len(name.split()) >= 2:
            add(name, "multi")
        elif name and (_is_product_token(name) or len(name) > 2):
            add(name, "product" if _is_product_token(name) else "single")
    # product tokens, merged with a trailing model/version number when present
    # so "RTX 4090" and "Llama 3.1" are one named thing, not a bare prefix
    for m in re.finditer(r"\b([A-Za-z][\w.:\-]*)\b(\s+(\d[\w.]*))?", text):
        tok = m.group(1)
        if len(tok) < 3 or tok in ENTITY_STOP or not _is_product_token(tok):
            continue
        num = m.group(3)
        if num and not re.fullmatch(r"\d{4}", num) and re.search(r"[A-Za-z]", tok):
            add(f"{tok} {num}".rstrip("."), "product")
        else:
            add(tok, "product")
    # plain capitalized words, mid-sentence only — a sentence-initial capital is
    # ambiguous ("Generating each token…" is a verb, not a name)
    for m in re.finditer(r"(?<=[^.!?\n]\s)\b([A-Z][a-z]{2,})\b", text):
        tok = m.group(1)
        if tok not in ENTITY_STOP and tok not in LEADING_STOP:
            add(tok, "single")

    # glossary filter: definitional jargon is not a "named example".
    gloss_l = []
    for g in research.get("glossary", []):
        t = (g.get("term") or "").lower().strip()
        if not t:
            continue
        gloss_l.append(t)
        inner = re.search(r"\(([^)]+)\)", t)
        if inner:                                   # "BAA (Business Associate Agreement)"
            gloss_l.append(inner.group(1).strip())
            gloss_l.append(t.split("(")[0].strip())

    def is_jargon(name):
        nl = name.lower()
        for g in gloss_l:
            if not g:
                continue
            if nl == g:
                # the brief defines this exact thing: a single capitalized
                # product name (Ollama) is still a real named example;
                # acronyms and phrases are vocabulary.
                return " " in name or name.isupper()
            if g in nl or nl in g:
                # a fragment of, or wrapper around, a defined phrase
                # ("Protected" from "PHI (Protected Health Information)")
                return True
        return False

    ents = [r for r in found.values()
            if r["name"] not in ENTITY_STOP and not is_jargon(r["name"])]

    # A single token that only ever appears wedged between other capitalized
    # words is a fragment of a longer name ("Bar" from "California State Bar").
    # One that also stands alone is a real entity ("OpenAI", which also occurs
    # inside "Trinidad v. OpenAI"). Case-sensitive: proper nouns only.
    def standalone_count(tok):
        n = 0
        for m in re.finditer(r"(?<![\w'])" + re.escape(tok) + r"(?![\w'])", text):
            prev = text[:m.start()].rstrip()
            prev_word = re.search(r"([A-Za-z][\w.'\-]*)$", prev)
            nxt = re.match(r"\s+([A-Za-z][\w.'\-]*)", text[m.end():])
            prev_cap = bool(prev_word and prev_word.group(1)[0].isupper()
                            and not prev.endswith((".", "!", "?", "\n")))
            nxt_cap = bool(nxt and nxt.group(1)[0].isupper())
            # "Trinidad v. OpenAI" — the case marker means this token is the
            # head of a case name, not a standalone entity
            nxt_case = bool(nxt and re.fullmatch(r"v\.?", nxt.group(1)))
            if not prev_cap and not nxt_cap and not nxt_case:
                n += 1
        return n

    kept = [e for e in ents
            if " " in e["name"] or standalone_count(e["name"]) >= 1]

    # fold "ChatGPT Business" / "Consumer ChatGPT" into the head product
    heads = {e["name"].lower() for e in kept if " " not in e["name"]}
    folded = []
    for e in kept:
        if " " in e["name"]:
            core = [t for t in e["name"].split() if t not in TIER_WORDS]
            if len(core) == 1 and core[0].lower() in heads:
                continue
        folded.append(e)

    for e in folded:
        e["count"] = len(_entity_rx(e["name"]).findall(text))
        tier, ccount = 4, 0
        for c in research.get("claims", []):
            if re.search(r"\b" + re.escape(e["name"].split()[0]), c.get("claim", ""), re.I) \
                    and _entity_rx(e["name"]).search(c.get("claim", "")):
                ccount += 1
                q = {"primary": 0, "docs": 1, "benchmark": 2,
                     "community": 3}.get(c.get("source_quality"), 4)
                tier = min(tier, q)
        e["tier"] = tier
        e["claim_count"] = ccount
    folded.sort(key=lambda e: (e["tier"], -e["claim_count"], -e["count"]))
    return folded


def _entity_rx(name):
    parts = [re.escape(p) for p in name.split()]
    pat = r"\s+".join(parts).replace(r"v\.", r"v\.?")
    return re.compile(r"(?<!\w)" + pat + r"(?:'s)?(?!\w)", re.I)


def _entity_found(name, corpus):
    """A script may shorten a long name and be RIGHT to: the brief's
    'PCIe Gen4 NVMe SSD' is spoken as 'NVMe SSD'. Accept the full name, or a
    trailing sub-phrase of it that still carries a distinctive (non-stopword)
    token — never a bare generic tail like 'SSD'."""
    if _entity_rx(name).search(corpus):
        return True
    toks = name.split()
    if any(re.fullmatch(r"v\.?", t) for t in toks):
        return False  # a case name must not match on one party alone
    for start in range(1, len(toks)):
        tail = toks[start:]
        if len(tail) < 2:
            continue  # a single trailing token is too weak a claim of the whole name
        if all(t in ENTITY_STOP for t in tail):
            continue
        if _entity_rx(" ".join(tail)).search(corpus):
            return True
    return False


# --- core scoring -----------------------------------------------------------
def score_board(sb, research):
    narration = sb.get("narration_full") or " ".join(
        s.get("narration", "") for s in sb.get("scenes", []))
    scenes = sb.get("scenes", [])
    hook_text = sb.get("hook_text", "")
    on_screen = " | ".join([hook_text] + [s.get("on_screen_text", "") for s in scenes])
    sents = sentences(narration)

    # --- numbers
    detail, spent = [], 0
    number_hits_by_scene = {s.get("id"): [] for s in scenes}
    for kn in (research or {}).get("key_numbers", []):
        label, value = kn.get("label", ""), kn.get("value", "")
        facts, _approx = parse_value(value)
        ctx = label_context(label)
        matched_in, matched_token = None, None
        for f in facts:
            for tok, strength in candidates_for(f):
                nar = find_token(tok, strength, narration, ctx)
                osc = find_token(tok, strength, on_screen, ctx)
                if nar or osc:
                    matched_token = nar or osc
                    matched_in = "both" if (nar and osc) else ("narration" if nar else "on_screen")
                    break
            if matched_in:
                break
        sids = []
        if matched_in:
            spent += 1
            for s in scenes:
                blob = (s.get("narration", "") + " " + s.get("on_screen_text", ""))
                for f in facts:
                    if any(find_token(t, st, blob, ctx) for t, st in candidates_for(f)):
                        sids.append(s.get("id"))
                        number_hits_by_scene[s.get("id")].append(f"num:{value}")
                        break
        detail.append({"label": label, "value": value, "spent": bool(matched_in),
                       "matched_in": matched_in, "matched_token": matched_token,
                       "scene_ids": sids})
    n_total = len(detail)
    # distinct = how many number PHRASES a listener actually hears. One spoken "about three
    # times" can satisfy several brief rows (a ratio, two bandwidths, a second ratio), which
    # inflates `spent` and made the cap fire on scripts that spend one number well. The gates
    # count distinct phrases; `spent` stays for reporting coverage of the brief.
    distinct = len({(d.get("matched_token") or "").strip().lower()
                    for d in detail if d.get("spent") and d.get("matched_token")})
    number_spend = {"total": n_total, "spent": spent, "distinct": distinct,
                    "score": round(spent / n_total, 3) if n_total else None,
                    "detail": detail}

    # --- entities
    ents = extract_entities(research or {})
    ent_out, found_names, missing = [], [], []
    ent_hits_by_scene = {s.get("id"): [] for s in scenes}
    for e in ents:
        rx = _entity_rx(e["name"])
        in_nar = _entity_found(e["name"], narration)
        in_osc = _entity_found(e["name"], on_screen)
        where = [w for w, ok in (("narration", in_nar), ("on_screen", in_osc)) if ok]
        if where:
            found_names.append(e["name"])
            for s in scenes:
                blob = s.get("narration", "") + " " + s.get("on_screen_text", "")
                if rx.search(blob):
                    ent_hits_by_scene[s.get("id")].append(f"entity:{e['name']}")
        else:
            missing.append(e["name"])
        ent_out.append({"name": e["name"], "tier": e["tier"],
                        "claim_count": e["claim_count"],
                        "found": bool(where), "matched_in": where})
    e_total = len(ent_out)
    top2 = [e["name"] for e in ents[:2]]
    top2_present = all(any(o["name"] == t and o["found"] for o in ent_out) for t in top2) if top2 else False
    entity_spend = {"total": e_total, "found_count": len(found_names),
                    "score": round(len(found_names) / e_total, 3) if e_total else None,
                    "found": found_names, "missing": missing,
                    "top2": top2, "top2_present": top2_present,
                    "entities": ent_out}

    # --- positional labels ("stage one, stage two")
    labels = find_positional_labels(narration)
    positional_labels = {"count": len(labels), "structure": sb.get("structure"),
                         "labels": labels}

    # --- skeleton
    offenders = [s for s in sents if SKELETON_RE.match(s)]
    skeleton = {"sentences": len(sents), "hits": len(offenders),
                "density": round(len(offenders) / len(sents), 3) if sents else 0.0,
                "offenders": offenders}

    # --- hook
    hook_corpus = hook_text + " " + (sents[0] if sents else "")
    via = []
    if re.search(r"\d", hook_corpus):
        via.append("digit")
    for kn in (research or {}).get("key_numbers", []):
        facts, _ = parse_value(kn.get("value", ""))
        ctx = label_context(kn.get("label", ""))
        for f in facts:
            if any(find_token(t, st, hook_corpus, ctx) for t, st in candidates_for(f)):
                via.append(f"number:{kn.get('value')}")
                break
    for e in ents:
        if _entity_rx(e["name"]).search(hook_corpus):
            via.append(f"entity:{e['name']}")
    hook = {"concrete": bool(via), "via": via, "hook_text": hook_text,
            "first_sentence": sents[0] if sents else ""}

    # --- per-scene specificity
    # A scene is specific when it carries something FROM THE BRIEF: a key number, a named
    # entity, or a glossary term. Glossary terms were added 2026-08-22 after a demo script
    # failed the gate on beats like "the machine pulls the model's weights out of memory",
    # which is the most specific sentence in the script and contains no proper noun or digit.
    # Note this deliberately differs from extract_entities above, which filters glossary terms
    # OUT: a defined term is not a "named example" for the entity gates, but it is a specific.
    gloss_terms = []
    for g in ((research or {}).get("glossary") or []):
        t = (g.get("term") if isinstance(g, dict) else g) or ""
        t = str(t).strip()
        if len(t) >= 3:
            gloss_terms.append(t)
    gloss_rx = [(t, re.compile(r"\b" + re.escape(t) + r"s?\b", re.I)) for t in gloss_terms]

    scene_rows = []
    for s in scenes:
        hits = number_hits_by_scene.get(s.get("id"), []) + ent_hits_by_scene.get(s.get("id"), [])
        if not hits:
            corpus = (s.get("narration", "") or "") + " " + (s.get("on_screen_text", "") or "")
            hits = ["glossary:" + t for t, rx in gloss_rx if rx.search(corpus)]
        scene_rows.append({"id": s.get("id"), "role": s.get("role"),
                           "est_duration_s": s.get("est_duration_s"),
                           "specific": bool(hits), "hits": hits,
                           "narration": s.get("narration", "")})
    spec_count = sum(1 for r in scene_rows if r["specific"])
    scene_specificity = {"total": len(scene_rows), "specific_count": spec_count,
                         "ratio": round(spec_count / len(scene_rows), 3) if scene_rows else 0.0,
                         "scenes": scene_rows}

    ws = words(narration)
    fmt = (sb.get("script_format") or "classic")
    wps = _wps(fmt)
    band = _format_cfg(fmt).get("vo_band_s") or {"min": 20.0, "max": 58.0}
    est_speech = len(ws) / wps if ws else 0.0
    language = {"fk_grade": round(fk_grade(narration), 1), "words": len(ws),
                "sentences": len(sents), "est_speech_s": round(est_speech, 1),
                "vo_band_ok": band["min"] <= est_speech <= band["max"]}

    return {"number_spend": number_spend, "entity_spend": entity_spend,
            "skeleton": skeleton, "hook": hook,
            "positional_labels": positional_labels,
            "scene_specificity": scene_specificity, "language": language,
            "narration_full": narration, "on_screen": on_screen}


def apply_gates(board, validator_blockers, fmt="classic", sameness=None):
    """Run the nine gates. `sameness` is the variety_check result dict, or None
    when no ledger was supplied, in which case that gate does not run at all
    and says so in the detail block."""
    if board is None:
        return {"gate1_ready": False, "failures": ["no_storyboard"], "advisories": [], "detail": {}}
    G = gates_for(fmt)
    f, adv, d = [], [], {}
    # With no research brief there is nothing to "spend" — the spend gates are
    # not applicable rather than failed (keeps briefless boards from reading as
    # broken in the report).
    has_brief = bool(board["number_spend"]["total"] or board["entity_spend"]["total"])
    ns = board["number_spend"]
    gn = G["number_spend"]
    minc, maxc = gn.get("min_count"), gn.get("max_count")
    # classic is now a BAND (at least 2, at most 5); smooth-explainer is a cap
    # only. The floor is clamped to the brief's own total so a thin brief cannot
    # make the bar unreachable.
    need = min(minc, ns["total"]) if (minc is not None and ns["total"]) else 0
    if not ns["total"]:
        shown_need = "n/a"
    elif minc is None:
        shown_need = "<=%s" % maxc          # cap-only format: no floor to meet
    else:
        shown_need = need
    heard = ns.get("distinct", ns["spent"])   # distinct spoken phrases, not brief rows matched
    d["number_spend"] = {"spent": ns["spent"], "heard": heard, "total": ns["total"],
                         "need": shown_need, "min": minc, "max": maxc,
                         "mode": "cap" if minc is None else "band"}
    if ns["total"]:
        under = minc is not None and heard < need
        over = maxc is not None and heard > maxc
        if under or over:
            d["number_spend"]["reason"] = (
                "the viewer hears %d distinct number%s (%d of %d brief rows matched); the band is %s-%s"
                % (heard, "" if heard == 1 else "s", ns["spent"], ns["total"],
                   "0" if minc is None else str(need),
                   "any" if maxc is None else str(maxc)))
            f.append("number_spend")

    # entity_spend and top2 are ADVISORY, not hard gates (finding 9, 2026-08-23 dry run):
    # the extractor's "entities" include sentence fragments, licenses and quant format names,
    # so as hard gates they failed 35 of the 38 published boards and every fresh draft.
    # They still appear in the report; the writer and the judge read them, nothing blocks on them.
    es = board["entity_spend"]
    d["entity_spend"] = {"score": es["score"], "need": G["entity_spend"]["min_ratio"], "advisory": True}
    if es["total"] and (es["score"] or 0) < G["entity_spend"]["min_ratio"]:
        adv.append("entity_spend")
    d["top2"] = {"top2": es["top2"], "present": es["top2_present"], "advisory": True}
    if es["total"] and not es["top2_present"]:
        adv.append("top2")

    d["hook_concrete"] = {"concrete": board["hook"]["concrete"], "via": board["hook"]["via"],
                          **({} if G["hook_concrete"]["required"] else {"waived": True})}
    if G["hook_concrete"]["required"] and not board["hook"]["concrete"]:
        f.append("hook_concrete")

    ss = board["scene_specificity"]
    need_spec = max(0, ss["total"] - G["scene_specificity"]["allow_generic"])
    d["scene_specificity"] = {"specific": ss["specific_count"],
                              "need": need_spec if has_brief else "n/a",
                              "total": ss["total"]}
    if has_brief and ss["specific_count"] < need_spec:
        f.append("scene_specificity")

    # Finding 18: "Not antithetical" (voice-rules) is checkable -- "not X, but Y" at most
    # once per script. Advisory: judges disagreed on hand counts, so the mechanical count
    # informs rather than blocks.
    narration_all = board.get("narration_full") or ""
    nxby = len(re.findall(r"\bnot\s+(?:a\s+|an\s+|the\s+)?\w+(?:\s\w+){0,3}?[,;]?\s+but\s+", narration_all, re.I))
    d["not_x_but_y"] = {"count": nxby, "max": 1, "advisory": True}
    if nxby > 1:
        adv.append("not_x_but_y")

    sk = board["skeleton"]
    d["skeleton"] = {"density": sk["density"], "max": G["skeleton"]["max_density"]}
    if sk["density"] > G["skeleton"]["max_density"]:
        f.append("skeleton")

    # --- positional labels: the "stage one, stage two" template -------------
    pl = board.get("positional_labels") or {"count": 0, "structure": None, "labels": []}
    gp = G["positional_labels"]
    allowed = list(gp.get("allowed_structures") or [])
    max_labels = gp.get("max_labels", 3)
    min_label_words = gp.get("min_label_words", 6)
    struct = pl.get("structure")
    reasons = []
    if pl["count"]:
        if not struct or struct not in allowed:
            reasons.append(
                "%s, so the video does not walk the viewer through a process and "
                "no positional label is permitted (allowed structures: %s); first "
                "hit: \u201c%s\u201d"
                % ("structure is absent" if not struct else "structure is '%s'" % struct,
                   ", ".join(allowed) or "none", pl["labels"][0]["sentence"].strip()))
        else:
            if pl["count"] > max_labels:
                reasons.append("%d positional labels, at most %d"
                               % (pl["count"], max_labels))
            ords = [l.get("ordinal") for l in pl["labels"]]
            if ords != list(range(1, len(ords) + 1)):
                reasons.append("label ordinals %s are not strictly ascending from one"
                               % (ords,))
            short = [l["sentence"].strip() for l in pl["labels"]
                     if l["words"] < min_label_words]
            if short:
                reasons.append("label sentence(s) under %d words: %s"
                               % (min_label_words,
                                  "; ".join("\u201c%s\u201d" % x for x in short)))
            dead = [l["sentence"].strip() for l in pl["labels"]
                    if not l["has_action_verb"]]
            if dead:
                reasons.append("label sentence(s) naming no action: %s"
                               % "; ".join("\u201c%s\u201d" % x for x in dead))
    d["positional_labels"] = {"count": pl["count"], "structure": struct,
                              "allowed_structures": allowed,
                              "max_labels": max_labels,
                              "min_label_words": min_label_words,
                              "offenders": [l["sentence"].strip() for l in pl["labels"]],
                              "reasons": reasons,
                              "reason": " · ".join(reasons) if reasons else None}
    if reasons:
        f.append("positional_labels")

    # --- sameness: only when a ledger was supplied --------------------------
    if sameness is None:
        d["sameness"] = {"checked": False, "ok": None,
                         "reason": "not run: no --ledger was passed, so nothing "
                                   "checks this script against the last five"}
    else:
        viol = sameness.get("violations") or []
        d["sameness"] = {"checked": True, "ok": bool(sameness.get("ok")),
                         "ledger": sameness.get("ledger"),
                         "comparisons": sameness.get("comparisons"),
                         "violations": viol,
                         "advisories": sameness.get("advisories") or [],
                         "reason": ("; ".join(v.get("detail", "") for v in viol)
                                    or sameness.get("error"))}
        if sameness.get("error"):
            d["sameness"]["error"] = sameness["error"]
        if not sameness.get("ok"):
            f.append("sameness")

    d["validator"] = {"blockers": validator_blockers}
    if validator_blockers is not None and validator_blockers > G["validator"]["max_blockers"]:
        f.append("validator")

    return {"gate1_ready": not f, "failures": f, "advisories": adv, "detail": d}


def research_metrics(r):
    if not r:
        return None
    claims = r.get("claims", [])
    by_q = {}
    domains = set()
    for c in claims:
        by_q[c.get("source_quality", "?")] = by_q.get(c.get("source_quality", "?"), 0) + 1
        m = re.match(r"https?://([^/]+)", c.get("source_url", "") or "")
        if m:
            domains.add(".".join(m.group(1).lower().replace("www.", "").split(".")[-2:]))
    unv = r.get("unverified", [])
    good = by_q.get("primary", 0) + by_q.get("docs", 0)
    return {
        "claims_total": len(claims), "claims_by_quality": by_q,
        "pct_primary_docs": round(good / len(claims), 3) if claims else 0.0,
        "key_numbers_total": len(r.get("key_numbers", [])),
        "entities_total": len(extract_entities(r)),
        "misconceptions_total": len(r.get("misconceptions", [])),
        "unverified_ratio": round(len(unv) / (len(claims) + len(unv)), 3) if (claims or unv) else 0.0,
        "source_domains": sorted(domains), "domain_diversity": len(domains),
        "depth": r.get("depth"), "has_notes": bool(r.get("notes")),
    }


def run_validator(script, path, extra_args=()):
    if not script or not Path(script).exists() or not path or not Path(path).exists():
        return None
    try:
        p = subprocess.run([sys.executable, str(script), str(path), *extra_args],
                           capture_output=True, text=True, timeout=120)
        try:
            out = json.loads(p.stdout)
        except Exception:
            out = {"parse_error": (p.stdout or p.stderr or "")[:400]}
        return {"exit_code": p.returncode, "output": out}
    except Exception as e:
        return {"exit_code": None, "output": {"error": str(e)}}


def telemetry_for(slug, data_dir):
    jobs_dir = Path(data_dir) / "jobs" if data_dir else None
    if not jobs_dir or not jobs_dir.exists():
        return {"note": "dashboard/data not readable"}
    stages = {}
    for jf in sorted(jobs_dir.glob("*.json")):
        try:
            rec = json.loads(jf.read_text())
        except Exception:
            continue
        if rec.get("slug") != slug or rec.get("dryRun"):
            continue
        t = rec.get("type", "?")
        row = {"job_id": rec.get("id"), "status": rec.get("status"),
               "model": (rec.get("meta") or {}).get("model"),
               "scene_id": rec.get("sceneId"),
               "cost_usd": rec.get("costUsd"), "error": rec.get("error"),
               "wall_ms": None, "api_ms": None, "num_turns": None,
               "tokens_in": None, "tokens_out": None, "cache_read": None,
               "source": "job-record"}
        try:
            st, en = rec.get("startedAt"), rec.get("endedAt")
            if st and en:
                row["wall_ms"] = int((datetime.fromisoformat(en.replace("Z", "+00:00"))
                                      - datetime.fromisoformat(st.replace("Z", "+00:00"))
                                      ).total_seconds() * 1000)
        except Exception:
            pass
        sf = jobs_dir / f"{rec.get('id')}.stream.ndjson"
        if sf.exists():
            try:
                size = sf.stat().st_size
                with sf.open("rb") as fh:
                    fh.seek(max(0, size - 262144))
                    chunk = fh.read().decode("utf-8", "replace").splitlines()
                for line in reversed(chunk):
                    line = line.strip()
                    if not line.startswith("{"):
                        continue
                    try:
                        ev = json.loads(line)
                    except Exception:
                        continue
                    if ev.get("type") == "result":
                        u = ev.get("usage") or {}
                        row.update({"api_ms": ev.get("duration_api_ms"),
                                    "num_turns": ev.get("num_turns"),
                                    "cost_usd": ev.get("total_cost_usd", row["cost_usd"]),
                                    "tokens_in": u.get("input_tokens"),
                                    "tokens_out": u.get("output_tokens"),
                                    "cache_read": u.get("cache_read_input_tokens"),
                                    "source": "stream"})
                        if ev.get("duration_ms"):
                            row["wall_ms"] = ev["duration_ms"]
                        break
            except Exception:
                pass
        stages.setdefault(t, []).append(row)
    totals = {"cost_usd": 0.0, "wall_ms": 0, "api_ms": 0}
    for rows in stages.values():
        for r in rows:
            totals["cost_usd"] += (r.get("cost_usd") or 0) or 0
            totals["wall_ms"] += (r.get("wall_ms") or 0) or 0
            totals["api_ms"] += (r.get("api_ms") or 0) or 0
    totals["cost_usd"] = round(totals["cost_usd"], 4)
    return {"stages": stages, "totals": totals}


def _api(base, path, timeout=30):
    import urllib.request
    try:
        with urllib.request.urlopen(base.rstrip("/") + path, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"__error": str(e)}


def telemetry_from_api(base, slug):
    """Job-record telemetry over HTTP. Token/turn counts live only in the
    per-job stream files on disk, so this degrades to wall-clock + cost."""
    jobs = _api(base, f"/api/jobs?slug={slug}")
    rows = jobs if isinstance(jobs, list) else (jobs.get("jobs") or [])
    if isinstance(jobs, dict) and jobs.get("__error"):
        return {"note": f"api error: {jobs['__error']}"}
    stages, totals = {}, {"cost_usd": 0.0, "wall_ms": 0, "api_ms": 0}
    for j in rows:
        if j.get("slug") != slug or j.get("dryRun"):
            continue
        wall = None
        try:
            st, en = j.get("startedAt"), j.get("endedAt")
            if st and en:
                wall = int((datetime.fromisoformat(en.replace("Z", "+00:00"))
                            - datetime.fromisoformat(st.replace("Z", "+00:00"))
                            ).total_seconds() * 1000)
        except Exception:
            pass
        row = {"job_id": j.get("id"), "status": j.get("status"),
               "model": (j.get("meta") or {}).get("model"),
               "scene_id": j.get("sceneId"), "cost_usd": j.get("costUsd"),
               "error": j.get("error"), "wall_ms": wall, "api_ms": None,
               "num_turns": None, "tokens_in": None, "tokens_out": None,
               "cache_read": None, "source": "api"}
        stages.setdefault(j.get("type", "?"), []).append(row)
        totals["cost_usd"] += (j.get("costUsd") or 0) or 0
        totals["wall_ms"] += wall or 0
    totals["cost_usd"] = round(totals["cost_usd"], 4)
    return {"stages": stages, "totals": totals}


def sameness_for(sb, ledger, fmt="classic"):
    """Run variety_check's sameness rules for a storyboard against a ledger.
    Returns None when no ledger was asked for (the gate then does not run)."""
    if not ledger or not sb:
        return None
    if _vc_entry is None:
        return {"ok": True, "violations": [], "advisories": [], "comparisons": 0,
                "ledger": str(ledger),
                "error": "variety_check.py not importable, sameness not enforced"}
    try:
        entry = _vc_entry(sb)
        res = _vc_check(entry, _vc_load(ledger),
                        window=gates_for(fmt)["sameness"].get("window", 5))
        res["ledger"] = str(ledger)
        return res
    except Exception as e:  # never let the variety library block a run
        return {"ok": True, "violations": [], "advisories": [], "comparisons": 0,
                "ledger": str(ledger), "error": "variety_check failed: %s" % e}


def build_eval_api(slug, base, label=None, ledger=None):
    """Score a run using only the dashboard HTTP API (no repo filesystem)."""
    sb_resp = _api(base, f"/api/projects/{slug}/storyboard")
    res_resp = _api(base, f"/api/projects/{slug}/research")
    rec = _api(base, f"/api/projects/{slug}")

    sb = sb_resp.get("storyboard") if isinstance(sb_resp, dict) else None
    res = res_resp.get("brief") if isinstance(res_resp, dict) else None
    board = score_board(sb, res or {}) if sb else None

    # the server ran the real validator; reuse its verdict verbatim
    validators = {"storyboard": None, "research": None}
    vb = None
    if isinstance(sb_resp, dict) and "blockers" in sb_resp:
        validators["storyboard"] = {"exit_code": None, "source": "dashboard",
                                    "output": {k: sb_resp.get(k) for k in
                                               ("blockers", "advisories",
                                                "violations", "warnings")}}
        vb = len(sb_resp.get("blockers") or [])
    proj = None
    if isinstance(rec, dict) and rec.get("slug"):
        proj = {"status": rec.get("status"), "imported": rec.get("imported"),
                "research": rec.get("research"),
                "storyboard": {k: (rec.get("storyboard") or {}).get(k)
                               for k in ("exists", "valid", "approvedAt")},
                "regen_attempts": len(((rec.get("storyboard") or {}).get("regenNotes")) or []),
                "vo": rec.get("vo"), "final": rec.get("final"),
                "scenes_done": sum(1 for s in (rec.get("scenes") or [])
                                   if s.get("status") == "done"),
                "scenes_total": len(rec.get("scenes") or [])}
    fmt = ((sb or {}).get("script_format") or "classic")
    same = sameness_for(sb, ledger, fmt)
    return {
        "eval_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "slug": label or slug,
        "inputs": {"storyboard_path": f"{base}/api/projects/{slug}/storyboard",
                   "research_path": f"{base}/api/projects/{slug}/research",
                   "mode": "api", "project_record": proj,
                   "ledger_path": str(ledger) if ledger else None},
        "research_metrics": research_metrics(res),
        "board_metrics": board,
        "validators": validators,
        "telemetry": telemetry_from_api(base, slug),
        "script_format": fmt,
        "thresholds": gates_for(fmt),
        "overall": apply_gates(board, vb, fmt, sameness=same),
    }


def build_eval(slug, sb_path, res_path, root, label=None, history=None, ledger=None):
    sb = json.loads(Path(sb_path).read_text()) if sb_path and Path(sb_path).exists() else None
    res = json.loads(Path(res_path).read_text()) if res_path and Path(res_path).exists() else None
    board = score_board(sb, res or {}) if sb else None
    # repointed: the storyboard validator is this script's sibling; the research
    # validator lives in skills/blai-research/scripts/ (v1: pipeline/scripts/ for both).
    validators = {
        "storyboard": run_validator(HERE / "validate_storyboard.py", sb_path,
                                    ("--history", str(history)) if history else ()),
        "research": run_validator(RESEARCH_VALIDATOR, res_path),
    }
    vb = None
    if validators["storyboard"] and isinstance(validators["storyboard"].get("output"), dict):
        bl = validators["storyboard"]["output"].get("blockers")
        vb = len(bl) if isinstance(bl, list) else None
    proj = None
    if root:  # v1 dashboard project record; absent in v2, so proj stays None
        pf = Path(root) / "dashboard" / "data" / "projects" / f"{slug}.json"
        if pf.exists():
            try:
                p = json.loads(pf.read_text())
                proj = {"status": p.get("status"), "imported": p.get("imported"),
                        "research": p.get("research"),
                        "storyboard": {k: (p.get("storyboard") or {}).get(k)
                                       for k in ("exists", "valid", "approvedAt")},
                        "regen_attempts": len(((p.get("storyboard") or {}).get("regenNotes")) or []),
                        "vo": p.get("vo"), "final": p.get("final"),
                        "scenes_done": sum(1 for s in (p.get("scenes") or [])
                                           if s.get("status") == "done"),
                        "scenes_total": len(p.get("scenes") or [])}
            except Exception:
                pass
    fmt = ((sb or {}).get("script_format") or "classic")
    same = sameness_for(sb, ledger, fmt)
    return {
        "eval_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "slug": label or slug,
        "inputs": {"storyboard_path": str(sb_path) if sb_path else None,
                   "research_path": str(res_path) if res_path else None,
                   "project_record": proj,
                   "ledger_path": str(ledger) if ledger else None},
        "research_metrics": research_metrics(res),
        "board_metrics": board,
        "validators": validators,
        "telemetry": telemetry_for(slug, (Path(root) / "dashboard" / "data") if root else None),
        "script_format": fmt,
        "thresholds": gates_for(fmt),
        "overall": apply_gates(board, vb, fmt, sameness=same),
    }


# --- report -----------------------------------------------------------------
CSS = """
:root{--bg:#0B1020;--panel:#111731;--line:#232A45;--ink:#F5F0E8;--amber:#FFB347;
--ok:#8FD49B;--bad:#FF6B6B;--mut:#8B93A7}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:14px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:22px;margin:0 0 4px} h2{font-size:16px;margin:26px 0 10px}
h3{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);
margin:18px 0 8px;font-weight:600}
a{color:var(--amber)} code,.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.sub{color:var(--mut);font-size:12.5px}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;
padding:18px;margin:18px 0}
.chip{display:inline-block;padding:2px 9px;border-radius:999px;font-size:11.5px;
border:1px solid var(--line);margin:0 4px 4px 0;white-space:nowrap}
.pass{color:var(--ok);border-color:#2C5138;background:#14251A}
.fail{color:var(--bad);border-color:#5B2A2E;background:#251316}
.warn{color:var(--amber);border-color:#5A4423;background:#241B0E}
.dim{color:var(--mut)}
table{border-collapse:collapse;width:100%;font-size:12.5px}
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{color:var(--mut);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.06em}
.tnum{font-family:ui-monospace,Menlo,monospace;text-align:right}
.bar{height:8px;background:#1A2138;border-radius:99px;overflow:hidden;position:relative}
.bar>i{display:block;height:100%;background:var(--amber)}
.bar>u{position:absolute;top:-3px;width:2px;height:14px;background:var(--ink);opacity:.7}
.gauge{margin:10px 0}
.gauge .lab{display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px}
.scenes{display:flex;gap:4px;margin:6px 0}
.scenes div{height:26px;border-radius:4px;font-size:10.5px;display:flex;
align-items:center;justify-content:center;color:#0B1020;font-weight:700}
.narr{background:#0D1striped;padding:12px;border-radius:8px;background:#0D1226;
border:1px solid var(--line);line-height:1.85}
mark{background:#3A2E12;color:var(--amber);padding:1px 3px;border-radius:3px}
.skel{text-decoration:underline wavy var(--bad);text-underline-offset:3px}
.callout{border:1px solid #5A4423;background:#1C1509;border-radius:10px;padding:12px;margin:10px 0}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:820px){.grid2{grid-template-columns:1fr}}
.timeline{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}
.stage{flex:1;min-width:120px;border:1px solid var(--line);border-radius:8px;padding:8px 10px}
.stage b{display:block;font-size:11px;text-transform:uppercase;color:var(--mut);letter-spacing:.06em}
details{margin-top:8px} summary{cursor:pointer;color:var(--mut);font-size:12.5px}
.diffcol{background:#0D1226;border:1px solid var(--line);border-radius:8px;padding:12px;line-height:1.8}
.dchg{background:#1C2440;border-left:2px solid var(--amber);padding-left:6px;display:block;margin:3px 0}
"""


def _esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def _chip(text, state="dim"):
    return f'<span class="chip {state}">{_esc(text)}</span>'


def _gauge(label, value, threshold, extra=""):
    v = 0 if value is None else max(0.0, min(1.0, float(value)))
    return (f'<div class="gauge"><div class="lab"><span>{_esc(label)}</span>'
            f'<span class="mono">{"—" if value is None else f"{value:.0%}"} {_esc(extra)}</span></div>'
            f'<div class="bar"><i style="width:{v*100:.1f}%"></i>'
            f'<u style="left:{threshold*100:.1f}%"></u></div></div>')


def _highlight(narration, board):
    txt = _esc(narration)
    toks = []
    for d in board["number_spend"]["detail"]:
        if d.get("matched_token"):
            toks.append(d["matched_token"])
    for e in board["entity_spend"]["entities"]:
        if e.get("found"):
            toks.append(e["name"])
    for t in sorted(set(toks), key=len, reverse=True):
        try:
            txt = re.sub(r"(?<!<mark>)(?<![\w>])(" + re.escape(_esc(t)) + r")(?![\w<])",
                         r"<mark>\1</mark>", txt, flags=re.I)
        except re.error:
            pass
    txt = re.sub(r"(?:(?<=^)|(?<=[.!?]\s))(First|Then|Next|So|Finally|Lastly|Second|Third)\b",
                 r'<span class="skel">\1</span>', txt)
    return txt


def _fmt_ms(ms):
    if not ms:
        return "—"
    s = ms / 1000.0
    return f"{s:.0f}s" if s < 90 else f"{s/60:.1f}m"


def _run_card(ev, judge):
    b = ev.get("board_metrics")
    o = ev.get("overall", {})
    slug = ev.get("slug")
    h = [f'<section class="card" id="run-{_esc(slug)}">']
    proj = (ev.get("inputs") or {}).get("project_record") or {}
    head = [_chip(slug, "warn")]
    if proj.get("status"):
        head.append(_chip(proj["status"]))
    if proj.get("imported"):
        head.append(_chip("imported"))
    head.append(_chip("GATE1 READY" if o.get("gate1_ready") else "GATES FAILING",
                      "pass" if o.get("gate1_ready") else "fail"))
    h.append(f'<h2>{_esc(slug)}</h2><div>{"".join(head)}</div>')

    # stage timeline
    tel = ev.get("telemetry") or {}
    stages = tel.get("stages") or {}
    if stages:
        h.append('<h3>stages</h3><div class="timeline">')
        for st in ("research", "storyboard", "vo", "scene", "assemble"):
            rows = stages.get(st) or []
            if not rows:
                h.append(f'<div class="stage"><b>{st}</b><span class="dim">—</span></div>')
                continue
            wall = sum(r.get("wall_ms") or 0 for r in rows)
            cost = sum(r.get("cost_usd") or 0 for r in rows)
            bad = sum(1 for r in rows if r.get("status") in ("failed", "cancelled"))
            h.append(f'<div class="stage"><b>{st}</b>{_fmt_ms(wall)}'
                     f'<span class="dim"> · {len(rows)} job(s)'
                     + (f' · <span style="color:var(--bad)">{bad} failed</span>' if bad else "")
                     + (f' · ${cost:.2f}' if cost else "") + '</span></div>')
        h.append('</div>')

    if not b:
        h.append('<p class="dim">No storyboard yet — research-stage metrics only.</p>')
    else:
        # gates
        h.append('<h3>gates</h3><div>')
        for name, det in (o.get("detail") or {}).items():
            failed = name in (o.get("failures") or [])
            val = ""
            if name == "number_spend":
                val = f'{det.get("spent")}/{det.get("total")} (need {det.get("need")})'
            elif name == "entity_spend":
                val = f'{(det.get("score") or 0):.0%} (need {det.get("need"):.0%})'
            elif name == "top2":
                val = ", ".join(det.get("top2") or []) or "—"
            elif name == "hook_concrete":
                val = ",".join(det.get("via") or []) or "none"
            elif name == "scene_specificity":
                val = f'{det.get("specific")}/{det.get("total")} (need {det.get("need")})'
            elif name == "skeleton":
                val = f'{det.get("density")} (max {det.get("max")})'
            elif name == "positional_labels":
                val = (f'{det.get("count")} label(s)' if det.get("count")
                       else "none") + (f': {det.get("reason")}' if det.get("reason") else "")
            elif name == "sameness":
                if not det.get("checked"):
                    val = "not checked (no ledger)"
                else:
                    val = (f'{det.get("comparisons")} compared'
                           + (f': {det.get("reason")}' if det.get("reason") else ""))
            elif name == "validator":
                bl = det.get("blockers")
                val = "n/a" if bl is None else f"{bl} blockers"
            state = "fail" if failed else "pass"
            if name == "sameness" and not det.get("checked"):
                state = "dim"  # not run is not the same as passed
            h.append(_chip(f"{name}: {val}", state))
        h.append('</div>')

        ns, es = b["number_spend"], b["entity_spend"]
        h.append('<div class="grid2"><div>')
        h.append(_gauge("number spend", ns["score"], 0.5,
                        f'{ns["spent"]}/{ns["total"]}'))
        h.append(_gauge("entity spend", es["score"], 0.5,
                        f'{es["found_count"]}/{es["total"]}'))
        h.append('</div><div>')
        lang = b["language"]
        h.append(f'<table><tr><th>words</th><td class="tnum">{lang["words"]}</td>'
                 f'<th>FK</th><td class="tnum">{lang["fk_grade"]}</td></tr>'
                 f'<tr><th>est speech</th><td class="tnum">{lang["est_speech_s"]}s</td>'
                 f'<th>VO band</th><td>{"ok" if lang["vo_band_ok"] else "OUT OF BAND"}</td></tr>'
                 f'<tr><th>skeleton</th><td class="tnum">{b["skeleton"]["density"]}</td>'
                 f'<th>hits</th><td class="tnum">{b["skeleton"]["hits"]}/{b["skeleton"]["sentences"]}</td></tr>'
                 f'</table>')
        h.append('</div></div>')

        # missing material
        unspent = [d for d in ns["detail"] if not d["spent"]]
        if unspent or es["missing"]:
            h.append('<div class="callout"><b>Material left on the table</b>'
                     '<div class="sub">paste into a regenerate note</div><ul>')
            for d in unspent:
                h.append(f'<li class="mono">{_esc(d["value"])} <span class="dim">— {_esc(d["label"])}</span></li>')
            if es["missing"]:
                h.append('<li>' + ", ".join(_esc(m) for m in es["missing"]) + '</li>')
            h.append('</ul></div>')

        # narration
        h.append('<h3>narration — matched specifics highlighted, skeleton connectives underlined</h3>')
        h.append(f'<div class="narr">{_highlight(b["narration_full"], b)}</div>')

        # scene strip
        ss = b["scene_specificity"]
        total_est = sum((s.get("est_duration_s") or 1) for s in ss["scenes"]) or 1
        h.append('<h3>per-scene specificity</h3><div class="scenes">')
        for s in ss["scenes"]:
            w = (s.get("est_duration_s") or 1) / total_est * 100
            col = "var(--ok)" if s["specific"] else "var(--bad)"
            tip = f'{s["id"]} {s.get("role","")} — ' + (", ".join(s["hits"]) if s["hits"] else "no specific")
            h.append(f'<div style="width:{w:.1f}%;background:{col}" title="{_esc(tip)}">{_esc(s["id"])}</div>')
        h.append('</div>')

        # entities
        h.append('<h3>entities</h3><div>')
        for e in es["entities"]:
            state = "pass" if e["found"] else "dim"
            star = "★ " if e["name"] in (es["top2"] or []) else ""
            h.append(_chip(f'{star}{e["name"]}', state))
        h.append('</div>')

    # research
    rm = ev.get("research_metrics")
    if rm:
        h.append('<h3>research brief</h3>')
        h.append(f'<table><tr><th>claims</th><td class="tnum">{rm["claims_total"]}</td>'
                 f'<th>primary+docs</th><td class="tnum">{rm["pct_primary_docs"]:.0%}</td>'
                 f'<th>key numbers</th><td class="tnum">{rm["key_numbers_total"]}</td></tr>'
                 f'<tr><th>entities</th><td class="tnum">{rm["entities_total"]}</td>'
                 f'<th>domains</th><td class="tnum">{rm["domain_diversity"]}</td>'
                 f'<th>unverified</th><td class="tnum">{rm["unverified_ratio"]:.0%}</td></tr></table>')

    # validators
    v = (ev.get("validators") or {}).get("storyboard")
    if v and isinstance(v.get("output"), dict):
        out = v["output"]
        bl, ad = out.get("blockers") or [], out.get("advisories") or []
        h.append('<h3>validator</h3>')
        if bl:
            h.append('<div>' + "".join(_chip(x, "fail") for x in bl) + '</div>')
        if ad:
            h.append('<details><summary>' + f'{len(ad)} advisories' + '</summary><ul>'
                     + "".join(f'<li>{_esc(x)}</li>' for x in ad) + '</ul></details>')
        if not bl and not ad:
            h.append(_chip("clean", "pass"))

    # telemetry table
    if stages:
        h.append('<details><summary>telemetry — per job</summary><table>'
                 '<tr><th>type</th><th>scene</th><th>status</th><th>model</th>'
                 '<th>wall</th><th>api</th><th>turns</th><th>in</th><th>out</th>'
                 '<th>cache</th><th>$</th></tr>')
        for st, rows in stages.items():
            for r in rows:
                cost = r.get("cost_usd")
                cost_s = f"{cost:.3f}" if cost else "—"
                h.append('<tr>'
                         f'<td>{_esc(st)}</td><td>{_esc(r.get("scene_id") or "")}</td>'
                         f'<td>{_esc(r.get("status"))}</td><td>{_esc(r.get("model") or "")}</td>'
                         f'<td class="tnum">{_fmt_ms(r.get("wall_ms"))}</td>'
                         f'<td class="tnum">{_fmt_ms(r.get("api_ms"))}</td>'
                         f'<td class="tnum">{r.get("num_turns") or "—"}</td>'
                         f'<td class="tnum">{r.get("tokens_in") or "—"}</td>'
                         f'<td class="tnum">{r.get("tokens_out") or "—"}</td>'
                         f'<td class="tnum">{r.get("cache_read") or "—"}</td>'
                         f'<td class="tnum">{cost_s}</td>'
                         '</tr>')
        h.append('</table></details>')

    # judge
    if judge:
        h.append('<h3>judge</h3>')
        verdict = judge.get("verdict", "?")
        state = {"pass": "pass", "revise": "warn", "fail": "fail"}.get(verdict, "dim")
        h.append(f'<div>{_chip("verdict: " + verdict, state)}')
        for k, val in (judge.get("scores") or {}).items():
            h.append(_chip(f"{k} {val}/10"))
        h.append('</div>')
        if judge.get("best_line"):
            h.append(f'<p class="sub">best: <em>{_esc(judge["best_line"])}</em></p>')
        if judge.get("worst_line"):
            h.append(f'<p class="sub">worst: <em>{_esc(judge["worst_line"])}</em></p>')
        if judge.get("missing_material"):
            h.append('<ul>' + "".join(f'<li>{_esc(m)}</li>' for m in judge["missing_material"]) + '</ul>')
        if judge.get("notes"):
            h.append(f'<p class="sub">{_esc(judge["notes"])}</p>')

    h.append('</section>')
    return "".join(h)


def _diff_panel(old_ev, new_ev):
    import difflib
    ob = old_ev.get("board_metrics")
    nb = new_ev.get("board_metrics")
    if not ob or not nb:
        return ""
    a, b = sentences(ob["narration_full"]), sentences(nb["narration_full"])
    sm = difflib.SequenceMatcher(None, a, b)
    left, right = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        for s in a[i1:i2]:
            left.append(_esc(s) if tag == "equal" else f'<span class="dchg">{_esc(s)}</span>')
        for s in b[j1:j2]:
            right.append(_esc(s) if tag == "equal" else f'<span class="dchg">{_esc(s)}</span>')
    rows = [
        ("words", ob["language"]["words"], nb["language"]["words"]),
        ("sentences", ob["language"]["sentences"], nb["language"]["sentences"]),
        ("FK grade", ob["language"]["fk_grade"], nb["language"]["fk_grade"]),
        ("skeleton density", ob["skeleton"]["density"], nb["skeleton"]["density"]),
        ("numbers spent", f'{ob["number_spend"]["spent"]}/{ob["number_spend"]["total"]}',
         f'{nb["number_spend"]["spent"]}/{nb["number_spend"]["total"]}'),
        ("entities found", f'{ob["entity_spend"]["found_count"]}/{ob["entity_spend"]["total"]}',
         f'{nb["entity_spend"]["found_count"]}/{nb["entity_spend"]["total"]}'),
        ("scenes specific", f'{ob["scene_specificity"]["specific_count"]}/{ob["scene_specificity"]["total"]}',
         f'{nb["scene_specificity"]["specific_count"]}/{nb["scene_specificity"]["total"]}'),
    ]
    tbl = "".join(f'<tr><th>{_esc(k)}</th><td class="tnum">{_esc(x)}</td>'
                  f'<td class="tnum">{_esc(y)}</td></tr>' for k, x, y in rows)
    return (f'<section class="card"><h2>A/B — same research, two writers</h2>'
            f'<div class="grid2"><div><h3>v2 · {_esc(old_ev["slug"])}</h3>'
            f'<div class="diffcol">{" ".join(left)}</div></div>'
            f'<div><h3>v3 · {_esc(new_ev["slug"])}</h3>'
            f'<div class="diffcol">{" ".join(right)}</div></div></div>'
            f'<table><tr><th></th><th>v2</th><th>v3</th></tr>{tbl}</table></section>')


def write_report(root, diff=None, out_path=None):
    root = Path(root) if root else REPO_ROOT
    evals, judges = {}, {}
    # v1 tree (out/<slug>/eval.json) and the v2 stage layout; both optional.
    eval_files = sorted((root / "out").glob("*/eval.json")) if (root / "out").exists() else []
    eval_files += sorted(root.glob("workspaces/*/stages/*/output/*eval.json"))
    for ef in eval_files:
        if ef.parent.name == "ready-to-publish":
            continue
        try:
            ev = json.loads(ef.read_text())
        except Exception:
            continue
        evals[ev.get("slug") or ef.parent.name] = ev
        jf = ef.parent / "judge.json"
        if jf.exists():
            try:
                judges[ev.get("slug") or ef.parent.name] = json.loads(jf.read_text())
            except Exception:
                pass

    h = ['<!doctype html><html><head><meta charset="utf-8">',
         '<meta http-equiv="refresh" content="20">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>BLAI eval — storyteller-v3</title>', f'<style>{CSS}</style></head><body>',
         '<div class="wrap">',
         '<h1>BLAI eval — storyteller-v3</h1>',
         f'<div class="sub">generated {datetime.now(timezone.utc).isoformat(timespec="seconds")} '
         f'· auto-refresh 20s · gates: numbers≥min(3,50%) · entities≥50% · top2 · concrete hook '
         f'· scenes≥n-1 · skeleton≤0.15 · 0 blockers '
         f'· smooth-explainer: numbers≤3 (cap) · hook gate waived</div>']

    if evals:
        h.append('<h2>summary</h2><div class="panel"><table><tr><th>run</th>'
                 '<th>numbers</th><th>entities</th><th>top2</th><th>hook</th>'
                 '<th>scenes</th><th>skeleton</th><th>validator</th><th>judge</th>'
                 '<th>ready</th></tr>')
        for slug, ev in evals.items():
            o = ev.get("overall", {})
            d = o.get("detail") or {}
            fails = set(o.get("failures") or [])

            def cell(key, text):
                cls = "fail" if key in fails else "pass"
                return f'<td><span class="chip {cls}">{_esc(text)}</span></td>'
            if not ev.get("board_metrics"):
                h.append(f'<tr><td><a href="#run-{_esc(slug)}">{_esc(slug)}</a></td>'
                         f'<td colspan="9" class="dim">research only</td></tr>')
                continue
            j = judges.get(slug, {})
            h.append(
                f'<tr><td><a href="#run-{_esc(slug)}">{_esc(slug)}</a></td>'
                + cell("number_spend", f'{d.get("number_spend",{}).get("spent")}/{d.get("number_spend",{}).get("total")}')
                + cell("entity_spend", f'{(d.get("entity_spend",{}).get("score") or 0):.0%}')
                + cell("top2", "yes" if d.get("top2", {}).get("present") else "no")
                + cell("hook_concrete", "yes" if d.get("hook_concrete", {}).get("concrete") else "no")
                + cell("scene_specificity", f'{d.get("scene_specificity",{}).get("specific")}/{d.get("scene_specificity",{}).get("total")}')
                + cell("skeleton", str(d.get("skeleton", {}).get("density")))
                + cell("validator", str(d.get("validator", {}).get("blockers")))
                + f'<td>{_esc(j.get("verdict","—"))}</td>'
                + f'<td><span class="chip {"pass" if o.get("gate1_ready") else "fail"}">'
                  f'{"READY" if o.get("gate1_ready") else "NOT READY"}</span></td></tr>')
        h.append('</table></div>')
    else:
        h.append('<div class="panel dim">No eval.json files yet.</div>')

    if diff and ":" in diff:
        old, new = diff.split(":", 1)
        if old in evals and new in evals:
            h.append(_diff_panel(evals[old], evals[new]))

    for slug, ev in evals.items():
        h.append(_run_card(ev, judges.get(slug)))

    h.append('</div></body></html>')
    dest = Path(out_path) if out_path else (
        (root / "out" / "eval-report.html") if (root / "out").exists() else Path("eval-report.html"))
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".html.tmp")
    tmp.write_text("".join(h))
    os.replace(tmp, dest)
    return dest


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--research")
    ap.add_argument("--storyboard")
    ap.add_argument("--label")
    ap.add_argument("--out")
    ap.add_argument("--root")
    ap.add_argument("--api", help="dashboard base URL; score over HTTP with no repo access")
    ap.add_argument("--evaldir", help="where to write <slug>/eval.json in --api mode")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--diff")
    ap.add_argument("--history", help="style-pack history file handed to validate_storyboard.py "
                                      "(default: skills/render-shorts/styles/history.json)")
    ap.add_argument("--ledger", help="script ledger JSON (output/script-ledger.json). "
                                     "WITHOUT it the `sameness` gate does not run at all, "
                                     "and the eval JSON says so.")
    ap.add_argument("--dry-run", action="store_true",
                    help="score everything and print the result, but write no files")
    a = ap.parse_args()

    root = Path(a.root) if a.root else REPO_ROOT
    if a.report:
        if a.dry_run:
            print(json.dumps({"dry_run": True, "would_write":
                              str(Path(a.out) if a.out else root / "evals" / "report.html")},
                             indent=2))
            return 0
        out = write_report(root, a.diff, a.out)
        print(f"wrote {out}")
        return 0

    if a.api:
        if not a.slug:
            ap.error("--api needs a slug")
        ev = build_eval_api(a.slug, a.api, label=a.label, ledger=a.ledger)
        base_dir = Path(a.evaldir) if a.evaldir else Path("evals")
        dest = Path(a.out) if a.out else base_dir / "out" / (a.label or a.slug) / "eval.json"
        if not a.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_suffix(".json.tmp")
            tmp.write_text(json.dumps(ev, indent=2))
            os.replace(tmp, dest)
        print(json.dumps(ev["overall"], indent=2))
        print(f"-> {dest}" + (" (dry run: not written)" if a.dry_run else ""))
        return 0 if ev["overall"]["gate1_ready"] else 4

    if a.storyboard or (a.research and not a.slug):
        slug = a.label or (a.slug or "adhoc")
        ev = build_eval(slug, a.storyboard, a.research, root, label=slug,
                        history=a.history, ledger=a.ledger)
        dest = Path(a.out) if a.out else Path(f"{slug}.eval.json")
    else:
        if not a.slug:
            ap.error("need a slug, or --storyboard/--research paths")
        if not (Path(root) / "out").exists():
            ap.error(f"no out/<slug>/ tree under {root}: pass --storyboard/--research/--out "
                     "(v2 layout) or --root of a v1 checkout")
        slug = a.slug
        d = Path(root) / "out" / slug
        ev = build_eval(slug, d / "storyboard.json",
                        Path(a.research) if a.research else d / "research.json", root,
                        history=a.history, ledger=a.ledger)
        dest = Path(a.out) if a.out else d / "eval.json"

    if not a.dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_suffix(dest.suffix + ".tmp")
        tmp.write_text(json.dumps(ev, indent=2))
        os.replace(tmp, dest)
    print(json.dumps(ev["overall"], indent=2))
    print(f"-> {dest}" + (" (dry run: not written)" if a.dry_run else ""))
    return 0 if ev["overall"]["gate1_ready"] else 4


if __name__ == "__main__":
    sys.exit(main())
