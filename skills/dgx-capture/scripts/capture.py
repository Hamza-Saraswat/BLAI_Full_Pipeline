#!/usr/bin/env python3
"""Run an experiment plan on the DGX Spark under an allowlist, record every command and
parse the numbers the episode cites.

Usage:
  capture.py --plan FILE.md|FILE.json --out DIR [--window any|night] [--dry-run]
             [--allowlist FILE] [--gpu-min-free-gb N] [--cwd DIR] [--now ISO8601]

Plan format: rules/experiment-plan-format.md (a ```json block with
[{id, command, timeout_s, expect, parse}]). For each command: allowlist check
(allowlist.json, all-or-nothing before anything runs), GPU free-memory check before
GPU commands, run under `timeout`, recorded with `asciinema rec` when available
(DIR/<id>.cast) else captured with subprocess, metrics parsed by regex.

Writes DIR/capture.json: [{id, command, status, exit, duration_s, stdout_tail, metrics, cast, ...}].
Exit 1 if any command was refused, failed, timed out or returned no metric, unless the
entry says "expect": "may_fail" (refusals always exit 1). --dry-run runs nothing: it
checks the plan against the allowlist and writes capture.json from fixtures/fake-outputs.
Default window is night: 01:00-06:00 America/Chicago; outside it the run exits 1 at once.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
DEFAULT_ALLOWLIST = SKILL / "allowlist.json"
FAKE_DIR = SKILL / "fixtures" / "fake-outputs"
DEFAULT_PLAN = SKILL / "fixtures" / "plan-example.md"
PARSE_TYPES = ("tok_s", "vram_gb", "load_s", "ollama_ps", "none")
EXPECT_VALUES = ("ok", "may_fail")
NIGHT_START, NIGHT_END = 1, 6
TZ_NAME = "America/Chicago"
TAIL_LINES = 60
TAIL_CHARS = 6000
EXIT_MARK = "__BLAI_EXIT__:"
ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]|\x1b\][^\x07]*(?:\x07|\x1b\\)|\x1b[()][A-Za-z0-9]|\x1b[=>]")
OPERATORS = {"|", "||", "&&", ";", "&"}
REDIRECT_RE = re.compile(r"^(\d?>>?|&>>?|\d?>\||<)(.*)$")
DOCKER_VALUE_OPTS = {
    "-v", "--volume", "-p", "--publish", "-e", "--env", "--name", "--gpus", "--shm-size", "--ipc", "--network", "--net",
    "-w", "--workdir", "-u", "--user", "--entrypoint", "--memory", "-m", "--cpus", "--mount", "--label", "-l",
    "--ulimit", "--device", "--runtime", "--env-file", "--platform", "--restart", "--hostname", "-h", "--pid",
    "--cap-add", "--cap-drop", "--security-opt", "--log-driver", "--add-host", "--dns", "--tmpfs",
}
CURL_OUTPUT_OPTS = {"-o", "--output", "-O", "--remote-name", "--output-dir"}


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------------------------- plan

def load_plan(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        m = re.search(r"```json\s*\n(.*?)\n```", text, re.S)
        if not m:
            raise ValueError("no ```json block found in %s" % path)
        data = json.loads(m.group(1))
    if isinstance(data, dict):
        data = data.get("commands") or data.get("plan") or []
    if not isinstance(data, list) or not data:
        raise ValueError("plan has no commands")
    entries = []
    seen = set()
    for i, raw in enumerate(data):
        if not isinstance(raw, dict):
            raise ValueError("plan entry %d is not an object" % i)
        cid = str(raw.get("id", "")).strip()
        if not re.match(r"^[a-z0-9][a-z0-9_-]*$", cid):
            raise ValueError("plan entry %d: id %r must be lowercase letters, digits, - or _" % (i, cid))
        if cid in seen:
            raise ValueError("plan entry %d: duplicate id %s" % (i, cid))
        seen.add(cid)
        cmd = raw.get("command")
        if not isinstance(cmd, str) or not cmd.strip():
            raise ValueError("plan entry %s: command must be a non-empty string" % cid)
        expect = str(raw.get("expect", "ok"))
        if expect not in EXPECT_VALUES:
            raise ValueError("plan entry %s: expect must be one of %s" % (cid, ", ".join(EXPECT_VALUES)))
        parse = str(raw.get("parse", "none"))
        if parse not in PARSE_TYPES:
            raise ValueError("plan entry %s: parse must be one of %s" % (cid, ", ".join(PARSE_TYPES)))
        try:
            timeout_s = int(raw.get("timeout_s", 600))
        except (TypeError, ValueError):
            raise ValueError("plan entry %s: timeout_s must be an integer" % cid)
        if timeout_s < 1:
            raise ValueError("plan entry %s: timeout_s must be >= 1" % cid)
        entries.append({
            "id": cid, "command": cmd.strip(), "timeout_s": timeout_s, "expect": expect, "parse": parse,
            "gpu": raw.get("gpu"), "note": raw.get("note"),
        })
    return entries


# --------------------------------------------------------------- allowlist

class Refusal(Exception):
    def __init__(self, rule: str, detail: str):
        super().__init__("%s: %s" % (rule, detail))
        self.rule = rule
        self.detail = detail


def _split_segments(tokens: list[str]) -> list[list[str]]:
    segments: list[list[str]] = [[]]
    for tok in tokens:
        if tok in OPERATORS:
            segments.append([])
        else:
            segments[-1].append(tok)
    return [s for s in segments if s]


def _check_redirect_target(target: str, out_dir: Path, cwd: Path) -> None:
    if target in ("/dev/null", "&1", "&2", "1", "2"):
        return
    path = Path(target)
    resolved = (path if path.is_absolute() else cwd / path).resolve()
    try:
        resolved.relative_to(out_dir.resolve())
    except ValueError:
        raise Refusal("redirect-outside-capture-dir", "redirection to %s is outside %s" % (target, out_dir))


def _strip_redirects(segment: list[str], out_dir: Path, cwd: Path) -> list[str]:
    out = []
    i = 0
    while i < len(segment):
        tok = segment[i]
        m = REDIRECT_RE.match(tok)
        if m:
            op, rest = m.group(1), m.group(2)
            if op == "<":
                i += 1 if rest else 2
                continue
            target = rest if rest else (segment[i + 1] if i + 1 < len(segment) else "")
            if not target:
                raise Refusal("redirect-outside-capture-dir", "redirection without a target")
            _check_redirect_target(target, out_dir, cwd)
            i += 1 if rest else 2
            continue
        out.append(tok)
        i += 1
    return out


def _docker_image(tokens: list[str]) -> str | None:
    i = 2  # after "docker run"
    while i < len(tokens):
        tok = tokens[i]
        if tok.startswith("-"):
            if "=" not in tok and tok in DOCKER_VALUE_OPTS:
                i += 2
            else:
                i += 1
            continue
        return tok
    return None


def check_segment(tokens: list[str], allow: dict, out_dir: Path, cwd: Path, first_segment: bool) -> str | None:
    """Return the family name (or 'filter:<name>') or raise Refusal."""
    tokens = _strip_redirects(tokens, out_dir, cwd)
    if not tokens:
        raise Refusal("empty-segment", "a pipeline segment has no command")
    first = tokens[0]
    if first == "env" or "=" in first:
        raise Refusal("environment-prefix", "set variables in build/.env, not inline (%s)" % first)
    if not first_segment and first in allow.get("filters", []):
        if first == "tee":
            for tok in tokens[1:]:
                if not tok.startswith("-"):
                    _check_redirect_target(tok, out_dir, cwd)
        return "filter:" + first
    fam = next((f for f in allow["families"] if f["first_token"] == first), None)
    if fam is None:
        raise Refusal("not-in-allowlist", "first token %r is not an allowed command family" % first)
    subs = fam.get("subcommands")
    if subs:
        sub = tokens[1] if len(tokens) > 1 else ""
        if sub not in subs:
            raise Refusal("subcommand", "%s %s is not allowed (allowed: %s)" % (first, sub or "(none)", ", ".join(subs)))
    if fam.get("arg_pattern"):
        arg = tokens[1] if len(tokens) > 1 else ""
        if not re.search(fam["arg_pattern"], arg):
            raise Refusal("argument-pattern", "%s %s does not match %s" % (first, arg or "(none)", fam["arg_pattern"]))
    if fam.get("url_pattern"):
        urls = [t for t in tokens[1:] if re.match(r"^[a-z]+://", t)]
        if not urls:
            raise Refusal("url-pattern", "%s needs an explicit http://localhost URL" % first)
        for u in urls:
            if not re.search(fam["url_pattern"], u):
                raise Refusal("url-pattern", "%s may only hit local endpoints, not %s" % (first, u))
        for i, t in enumerate(tokens):
            if t in CURL_OUTPUT_OPTS:
                target = tokens[i + 1] if i + 1 < len(tokens) and t != "-O" else ""
                if t in ("-O", "--remote-name"):
                    raise Refusal("curl-output", "curl -O writes into the working directory; use -o DIR/file inside --out")
                _check_redirect_target(target, out_dir, cwd)
    if fam.get("image_patterns"):
        for flag in fam.get("deny_flags", []):
            if flag in tokens:
                raise Refusal("docker-flag", "%s is not allowed" % flag)
        for i, t in enumerate(tokens):
            if t in ("-v", "--volume", "--mount") and i + 1 < len(tokens):
                host = tokens[i + 1].split(":")[0]
                if host in ("/", "/etc", "/root", "/home", "/usr", "/var", "/boot"):
                    raise Refusal("docker-mount", "mounting %s into a container is not allowed" % host)
        image = _docker_image(tokens)
        if image is None or not any(re.search(pat, image) for pat in fam["image_patterns"]):
            raise Refusal("docker-image", "image %r is not in the allowed list (%s)" % (image, ", ".join(fam["image_patterns"])))
    return fam["name"]


def check_command(command: str, allow: dict, out_dir: Path, cwd: Path) -> dict:
    """Raise Refusal or return {families: [...], gpu: bool}."""
    for rule in allow.get("deny", []):
        if re.search(rule["pattern"], command):
            raise Refusal(rule["name"], rule.get("why", "denied pattern"))
    if "\n" in command:
        raise Refusal("multiline", "one command per plan entry")
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError as exc:
        raise Refusal("unparseable", "could not parse the command: %s" % exc)
    segments = _split_segments(tokens)
    if not segments:
        raise Refusal("empty-command", "nothing to run")
    families = []
    for i, seg in enumerate(segments):
        families.append(check_segment(seg, allow, out_dir, cwd, first_segment=(i == 0)))
    fam_defs = {f["name"]: f for f in allow["families"]}
    gpu = any(fam_defs.get(f, {}).get("gpu") for f in families)
    return {"families": families, "gpu": gpu}


# ------------------------------------------------------------------- metrics

def _to_seconds(value: str, unit: str) -> float:
    v = float(value)
    return {"ms": v / 1000.0, "s": v, "m": v * 60.0, "h": v * 3600.0, "µs": v / 1e6, "us": v / 1e6}.get(unit, v)


def extract_metrics(text: str) -> dict:
    """Every number the known tools print, keyed the way the reconcile step expects."""
    t = ANSI_RE.sub("", text)
    m: dict = {}
    # ollama --verbose
    r = re.search(r"^\s*eval rate:\s*([\d.]+)\s*tokens/s", t, re.M)
    if r:
        m["tok_s"] = float(r.group(1))
    r = re.search(r"^\s*prompt eval rate:\s*([\d.]+)\s*tokens/s", t, re.M)
    if r:
        m["prompt_tok_s"] = float(r.group(1))
    r = re.search(r"^\s*load duration:\s*([\d.]+)\s*(ms|s|m|µs|us)\b", t, re.M)
    if r:
        m["load_s"] = round(_to_seconds(r.group(1), r.group(2)), 3)
    r = re.search(r"^\s*total duration:\s*([\d.]+)\s*(ms|s|m|h)\b", t, re.M)
    if r:
        m["total_s"] = round(_to_seconds(r.group(1), r.group(2)), 3)
    r = re.search(r"^\s*eval count:\s*(\d+)\s*token", t, re.M)
    if r:
        m["eval_count"] = int(r.group(1))
    # llama.cpp timings ("prompt eval time" must not shadow "eval time")
    r = re.search(r"(?<!prompt )\beval time\s*=.*?\(\s*[\d.]+\s*ms per token,\s*([\d.]+)\s*tokens per second", t)
    if r:
        m["tok_s"] = float(r.group(1))
    r = re.search(r"prompt eval time\s*=.*?\(\s*[\d.]+\s*ms per token,\s*([\d.]+)\s*tokens per second", t)
    if r:
        m["prompt_tok_s"] = float(r.group(1))
    r = re.search(r"\bload time\s*=\s*([\d.]+)\s*ms", t)
    if r:
        m["load_s"] = round(float(r.group(1)) / 1000.0, 3)
    # llama-bench table rows
    tg = [float(x) for x in re.findall(r"\|\s*tg\d+\s*\|\s*([\d.]+)\s*(?:±|\+/-)", t)]
    if tg:
        m["tok_s"] = tg[0]
    pp = [float(x) for x in re.findall(r"\|\s*pp\d+\s*\|\s*([\d.]+)\s*(?:±|\+/-)", t)]
    if pp:
        m["prompt_tok_s"] = pp[0]
    # vllm bench serve
    r = re.search(r"Output token throughput \(tok/s\):\s*([\d.]+)", t)
    if r:
        m["tok_s"] = float(r.group(1))
    r = re.search(r"Total [Tt]oken throughput \(tok/s\):\s*([\d.]+)", t)
    if r:
        m["total_tok_s"] = float(r.group(1))
    r = re.search(r"Median TTFT \(ms\):\s*([\d.]+)", t) or re.search(r"Mean TTFT \(ms\):\s*([\d.]+)", t)
    if r:
        m["ttft_ms"] = float(r.group(1))
    r = re.search(r"Mean TPOT \(ms\):\s*([\d.]+)", t)
    if r:
        m["tpot_ms"] = float(r.group(1))
    # nvidia-smi csv: "used MiB, total MiB"
    r = re.search(r"^\s*([\d.]+)\s*MiB\s*,\s*([\d.]+)\s*MiB", t, re.M)
    if r:
        m["vram_gb"] = round(float(r.group(1)) / 1024.0, 2)
        m["vram_total_gb"] = round(float(r.group(2)) / 1024.0, 2)
    # ollama ps table
    rows = re.findall(r"^(\S+)\s+([0-9a-f]{6,})\s+([\d.]+)\s*(GB|MB)\s+(\d+%\s*(?:GPU|CPU)(?:/\d+%\s*(?:GPU|CPU))?)", t, re.M)
    if rows:
        models = []
        for name, _, size, unit, proc in rows:
            gb = float(size) / (1024.0 if unit == "MB" else 1.0)
            models.append({"name": name, "size_gb": round(gb, 2), "processor": re.sub(r"\s+", " ", proc)})
        m["models"] = models
        m["ollama_vram_gb"] = round(sum(x["size_gb"] for x in models if "GPU" in x["processor"]), 2)
    # JSON printed by the benchmark scripts (last {...} line wins)
    for line in reversed(t.splitlines()):
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                obj = json.loads(line)
            except ValueError:
                continue
            for key in ("tok_s", "ttft_ms", "prompt_tok_s", "load_s", "vram_gb"):
                if isinstance(obj.get(key), (int, float)):
                    m[key] = obj[key]
            break
    return m


PARSE_KEY = {"tok_s": "tok_s", "vram_gb": "vram_gb", "load_s": "load_s", "ollama_ps": "models", "none": None}


# ----------------------------------------------------------------------- run

def gpu_free_gb(allow: dict, dry_run: bool) -> tuple[float | None, float | None, str]:
    if dry_run:
        text = (FAKE_DIR / "nvidia-smi.txt").read_text()
    else:
        if shutil.which("nvidia-smi") is None:
            return None, None, "nvidia-smi not on PATH"
        try:
            text = subprocess.run(shlex.split(allow["gpu_query"]), capture_output=True, text=True, timeout=30).stdout
        except (OSError, subprocess.TimeoutExpired) as exc:
            return None, None, "nvidia-smi failed: %s" % exc
    m = re.search(r"([\d.]+)\s*MiB\s*,\s*([\d.]+)\s*MiB", text)
    if not m:
        return None, None, "could not parse nvidia-smi output: %s" % text.strip()[:120]
    used, total = float(m.group(1)) / 1024.0, float(m.group(2)) / 1024.0
    return round(total - used, 2), round(total, 2), ""


def cast_to_text(cast_path: Path) -> str:
    out = []
    for line in cast_path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if isinstance(ev, list) and len(ev) >= 3 and ev[1] == "o":
            out.append(str(ev[2]))
    return "".join(out)


def tail(text: str) -> str:
    text = ANSI_RE.sub("", text).replace("\r\n", "\n")
    lines = text.split("\n")
    if len(lines) > TAIL_LINES:
        lines = lines[-TAIL_LINES:]
    joined = "\n".join(lines)
    return joined[-TAIL_CHARS:]


def fake_output(entry: dict, families: list[str]) -> str:
    fam = families[0] if families else ""
    cmd = entry["command"]
    name = "generic.txt"
    if fam == "ollama":
        sub = shlex.split(cmd)[1] if len(shlex.split(cmd)) > 1 else ""
        name = {"run": "ollama-run-verbose.txt", "ps": "ollama-ps.txt", "pull": "ollama-pull.txt", "list": "ollama-list.txt"}.get(sub, "generic.txt")
    elif fam in ("llama-cli", "llama-server"):
        name = "llama-cli-timings.txt"
    elif fam == "llama-bench":
        name = "llama-bench.txt"
    elif fam == "vllm":
        name = "vllm-bench.txt"
    elif fam == "nvidia-smi":
        name = "nvidia-smi.txt"
    elif fam == "python-benchmarks":
        name = "bench-ollama.json" if "bench_ollama" in cmd else "bench-openai-compat.json"
    path = FAKE_DIR / name
    return path.read_text() if path.exists() else "ok\n"


def run_entry(entry: dict, out_dir: Path, cwd: Path, use_asciinema: bool, timeout_bin: str | None) -> dict:
    cid = entry["id"]
    cast_path = out_dir / ("%s.cast" % cid)
    prefix = "%s -k 5 %d " % (timeout_bin, entry["timeout_s"]) if timeout_bin else ""
    inner = "%sbash -c %s; echo %s$?" % (prefix, shlex.quote(entry["command"]), EXIT_MARK)
    if use_asciinema:
        argv = ["asciinema", "rec", "--quiet", "--overwrite", "-c", inner, str(cast_path)]
    else:
        argv = ["bash", "-c", inner]
    started = time.time()
    status, exit_code, transcript, reason = "ok", None, "", ""
    try:
        proc = subprocess.run(argv, cwd=str(cwd), capture_output=True, text=True, stdin=subprocess.DEVNULL,
                              timeout=entry["timeout_s"] + 20, start_new_session=True)
        transcript = (proc.stdout or "") + (proc.stderr or "")
    except subprocess.TimeoutExpired as exc:
        status, reason = "timeout", "no exit after %d s" % entry["timeout_s"]
        transcript = ((exc.stdout or b"").decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")) + \
                     ((exc.stderr or b"").decode("utf-8", "replace") if isinstance(exc.stderr, bytes) else (exc.stderr or ""))
    except OSError as exc:
        status, reason = "failed", "could not start: %s" % exc
    duration = round(time.time() - started, 3)
    if use_asciinema and cast_path.exists():
        transcript = cast_to_text(cast_path)
    m = re.search(re.escape(EXIT_MARK) + r"(\d+)", transcript)
    if m:
        exit_code = int(m.group(1))
        transcript = transcript[: m.start()].rstrip() + "\n"
        if exit_code == 124 and timeout_bin:
            status, reason = "timeout", "killed by timeout after %d s" % entry["timeout_s"]
        elif exit_code != 0 and status == "ok":
            status, reason = "failed", "exit %d" % exit_code
    elif status == "ok":
        status, reason = "failed", "no exit marker in the transcript"
    metrics = extract_metrics(transcript)
    return {
        "status": status, "exit": exit_code, "duration_s": duration, "stdout_tail": tail(transcript), "metrics": metrics,
        "cast": cast_path.name if (use_asciinema and cast_path.exists()) else None, "reason": reason or None,
    }


def in_night_window(now: dt.datetime) -> bool:
    return NIGHT_START <= now.hour < NIGHT_END


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", help="experiment plan (.md with a ```json block, or .json); default in --dry-run: fixtures/plan-example.md")
    ap.add_argument("--out", required=True, help="capture directory: capture.json and <id>.cast go here")
    ap.add_argument("--window", choices=["any", "night"], default="night", help="night = 01:00-06:00 %s (default)" % TZ_NAME)
    ap.add_argument("--allowlist", default=str(DEFAULT_ALLOWLIST))
    ap.add_argument("--gpu-min-free-gb", type=float, help="refuse GPU commands when less is free (default from allowlist.json)")
    ap.add_argument("--cwd", default=os.getcwd(), help="working directory for the commands (default: current; use the repo root)")
    ap.add_argument("--no-asciinema", action="store_true", help="capture with subprocess even if asciinema is installed")
    ap.add_argument("--now", help="ISO 8601 time used for the window check (tests)")
    ap.add_argument("--dry-run", action="store_true", help="check the plan, run nothing, write capture.json from fake outputs")
    args = ap.parse_args()

    out_dir = Path(args.out).resolve()
    cwd = Path(args.cwd).resolve()
    plan_path = Path(args.plan).resolve() if args.plan else (DEFAULT_PLAN if args.dry_run else None)
    if plan_path is None:
        log("error: --plan is required (only --dry-run has a default)")
        return 1
    if not plan_path.exists():
        log("error: plan not found: %s" % plan_path)
        return 1
    try:
        allow = json.loads(Path(args.allowlist).read_text(encoding="utf-8"))
        entries = load_plan(plan_path)
    except (ValueError, OSError) as exc:
        log("error: %s" % exc)
        return 1
    min_free = args.gpu_min_free_gb if args.gpu_min_free_gb is not None else float(allow.get("gpu_min_free_gb", 8))

    # 1. Allowlist, all or nothing: a plan with one bad command runs nothing.
    checked = {}
    refused = []
    for e in entries:
        try:
            checked[e["id"]] = check_command(e["command"], allow, out_dir, cwd)
        except Refusal as exc:
            refused.append((e, exc))
            log("REFUSED %s: rule '%s': %s\n    command: %s" % (e["id"], exc.rule, exc.detail, e["command"]))
    if refused:
        out_dir.mkdir(parents=True, exist_ok=True)
        results = [{"id": e["id"], "command": e["command"], "status": "refused", "exit": None, "duration_s": 0.0,
                    "started_at": None, "timeout_s": e["timeout_s"], "expect": e["expect"], "parse": e["parse"], "cast": None,
                    "stdout_tail": "", "metrics": {}, "reason": "rule '%s': %s" % (exc.rule, exc.detail)}
                   for e, exc in refused]
        (out_dir / "capture.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        log("error: %d of %d commands refused by allowlist.json; nothing was run (see rules/allowlist.md)" % (len(refused), len(entries)))
        print(json.dumps({"out": str(out_dir), "refused": [e["id"] for e, _ in refused], "ran": 0}, indent=2))
        return 1

    # 2. Window.
    try:
        from zoneinfo import ZoneInfo  # Python 3.9+
        tz = ZoneInfo(TZ_NAME)
    except Exception:  # pragma: no cover
        tz = None
        log("warning: zoneinfo unavailable; window check uses local time")
    now = dt.datetime.fromisoformat(args.now) if args.now else dt.datetime.now(tz)
    if tz is not None and now.tzinfo is not None:
        now = now.astimezone(tz)
    if args.window == "night" and not in_night_window(now):
        msg = "outside the night window (01:00-06:00 %s): it is %s; pass --window any to run now" % (TZ_NAME, now.strftime("%H:%M %Z"))
        if args.dry_run:
            log("warning (dry run, not enforced): " + msg)
        else:
            log("error: " + msg)
            return 1

    # 3. Run.
    use_asciinema = shutil.which("asciinema") is not None and not args.no_asciinema and not args.dry_run
    timeout_bin = shutil.which("timeout") or shutil.which("gtimeout")
    if not timeout_bin and not args.dry_run:
        log("warning: no `timeout` binary on PATH; relying on the Python-side timeout only")
    log("capture: %d commands, out=%s, asciinema=%s, window=%s, dry_run=%s" % (len(entries), out_dir, use_asciinema, args.window, args.dry_run))
    out_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    failures = 0
    for e in entries:
        info = checked[e["id"]]
        is_gpu = bool(e["gpu"]) if e["gpu"] is not None else info["gpu"]
        rec = {"id": e["id"], "command": e["command"], "status": "ok", "exit": None, "duration_s": 0.0,
               "started_at": (dt.datetime.now(tz) if not args.dry_run else now).isoformat(timespec="seconds"),
               "timeout_s": e["timeout_s"], "expect": e["expect"], "parse": e["parse"], "families": info["families"],
               "gpu": is_gpu, "cast": None, "stdout_tail": "", "metrics": {}, "reason": None}
        if e.get("note"):
            rec["note"] = e["note"]
        if is_gpu:
            free, total, err = gpu_free_gb(allow, args.dry_run)
            if err:
                log("warning: %s: GPU check skipped (%s)" % (e["id"], err))
                rec["gpu_free_gb"] = None
            else:
                rec["gpu_free_gb"] = free
                rec["gpu_total_gb"] = total
                if free is not None and free < min_free:
                    rec["status"], rec["reason"] = "skipped", "gpu_busy: only %.1f GB free, need %.1f" % (free, min_free)
        if rec["status"] == "ok":
            if args.dry_run:
                text = fake_output(e, info["families"])
                rec.update({"exit": 0, "duration_s": 1.0, "stdout_tail": tail(text), "metrics": extract_metrics(text), "cast": None})
            else:
                log("run %s: %s" % (e["id"], e["command"]))
                rec.update(run_entry(e, out_dir, cwd, use_asciinema, timeout_bin))
        key = PARSE_KEY[e["parse"]]
        if rec["status"] == "ok" and key and key not in rec["metrics"]:
            rec["status"], rec["reason"] = "no_metric", "parse=%s but no %s in the output" % (e["parse"], key)
        ok = rec["status"] == "ok" or e["expect"] == "may_fail"
        if not ok:
            failures += 1
        log("%s %s (%s, %.1f s) %s" % ("ok  " if rec["status"] == "ok" else "FAIL", e["id"], rec["status"], rec["duration_s"],
                                        json.dumps(rec["metrics"]) if rec["metrics"] else (rec["reason"] or "")))
        results.append(rec)
        (out_dir / "capture.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    summary = {"out": str(out_dir), "dry_run": args.dry_run, "ran": len(results), "failed": failures,
               "metrics": {r["id"]: r["metrics"] for r in results if r["metrics"]},
               "statuses": {r["id"]: r["status"] for r in results}}
    print(json.dumps(summary, indent=2))
    if failures:
        log("error: %d command(s) failed without expect: may_fail" % failures)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
