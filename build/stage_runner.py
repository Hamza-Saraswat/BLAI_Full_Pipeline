#!/usr/bin/env python3
"""Spark stage table for the BLAI build agent: which stages run on the DGX Spark and how.

Each Spark stage is one row in STAGES (build stages, run in order) or PUBLISH (run when the hub
note is approved): name, kind, workspace, function. Mechanical stages call the skill scripts
directly; creative stages run `claude -p` inside the workspace with the unattended prompt from
_design/builder-brief.md. build.py decides when a stage runs and what happens when it fails.

Library use (build/build.py):
    from stage_runner import STAGES, PUBLISH, Ctx, StageError, run_stage, poll_status
CLI use:
    python3 build/stage_runner.py --list
    python3 build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --stage 06-voice --dry-run
    python3 build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --poll

Paths: repo root = BLAI_REPO_DIR (default: the parent of build/), per-slug binaries =
BLAI_BUILD_DIR/<slug>/ (default $HOME/blai/builds). Every skill script path is computed from the
repo root. Exit codes: 0 ok, 1 the stage failed, 2 usage.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import shlex
import socket
import subprocess
import sys
import time
from typing import Callable, NamedTuple

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(os.environ.get("BLAI_REPO_DIR") or HERE.parent).resolve()
BUILD_DIR = pathlib.Path(os.environ.get("BLAI_BUILD_DIR") or (pathlib.Path.home() / "blai" / "builds"))
sys.path.insert(0, str(REPO / "tools"))
import hubnote  # noqa: E402

SKILLS = REPO / "skills"
SCRIPT = {
    "generate_audio": SKILLS / "elevenlabs-narration" / "scripts" / "generate_audio.py",
    "qa_transcribe": SKILLS / "elevenlabs-narration" / "scripts" / "qa_transcribe.py",
    "captions": SKILLS / "elevenlabs-narration" / "scripts" / "captions.py",
    "capture": SKILLS / "dgx-capture" / "scripts" / "capture.py",
    "publish": SKILLS / "blotato-publish" / "scripts" / "publish.py",
    "send_card": SKILLS / "telegram-gate" / "scripts" / "send_card.py",
}
PY = sys.executable or "python3"

# Timeouts (seconds)
CLAUDE_TIMEOUT = 2 * 3600
VOICE_TIMEOUT = 30 * 60
QA_TIMEOUT = 30 * 60
CAPTIONS_TIMEOUT = 10 * 60
CAPTURE_TIMEOUT = 6 * 3600
PUBLISH_TIMEOUT = 30 * 60
CARD_TIMEOUT = 120

UNATTENDED = ("Run stage {stage} for {slug} in unattended mode. Read CLAUDE.md, then "
              "stages/{stage}/CONTEXT.md, and follow it exactly. Build dir: {build}.")
RECONCILE = ("Run stage 08-capture reconcile for {slug} in unattended mode. Read CLAUDE.md, then "
             "stages/08-capture/CONTEXT.md, and follow it exactly. Build dir: {build}. "
             "The capture results are in {build}/capture/capture.json.")

VOICE_FIXTURE = {"duration_s": 0.0, "chars": 0, "chunks": 0, "credits_estimate": 0, "model": ""}
QA_FIXTURE = {"wer": 0.0, "mismatches": [], "pass": True}
PUBLISH_FIXTURE = {"post_submission_id": "dry-run", "scheduled_time": "", "media_url": "", "thumbnail_url": ""}
PUBLISHED_STATES = {"published", "posted", "success", "succeeded", "done", "completed"}
FAILED_STATES = {"failed", "error", "errored", "rejected", "cancelled", "canceled"}
URL_KEYS = ("youtube_url", "youtubeUrl", "published_url", "publishedUrl", "post_url", "postUrl",
            "public_url", "publicUrl", "url")


class StageError(Exception):
    """A stage failed; str(error) is what goes into blocked_reason."""


class Stage(NamedTuple):
    name: str
    kind: str
    workspace: str
    fn: Callable[["Ctx"], str]


class DryResult(NamedTuple):
    returncode: int = 0
    stdout: str = "{}"
    stderr: str = ""


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _tail(text: str, n: int = 8, limit: int = 600) -> str:
    lines = [ln for ln in (text or "").strip().splitlines() if ln.strip()]
    out = "\n".join(lines[-n:]).strip()
    return out if len(out) <= limit else out[-limit:]


def _parse_json(text: str):
    """The last JSON object printed on stdout (scripts may log lines before it)."""
    text = (text or "").strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except ValueError:
        pass
    for line in reversed(text.splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                return json.loads(line)
            except ValueError:
                continue
    start, end = text.find("{"), text.rfind("}")
    if 0 <= start < end:
        try:
            return json.loads(text[start:end + 1])
        except ValueError:
            return None
    return None


def _find_url(obj) -> str:
    if isinstance(obj, dict):
        for k in URL_KEYS:
            v = obj.get(k)
            if isinstance(v, str) and v.startswith("http"):
                return v
        for v in obj.values():
            found = _find_url(v)
            if found:
                return found
    if isinstance(obj, list):
        for v in obj:
            found = _find_url(v)
            if found:
                return found
    return ""


class Ctx:
    """What a stage function needs: the hub note, the paths, and helpers (run, claude, write,
    hub_update, journal) that print a plan instead of acting when dry_run is set."""

    def __init__(self, note, dry_run: bool = False, fresh: bool = False, log=None):
        self.note = pathlib.Path(note).resolve()
        self.meta, _ = hubnote.read(self.note)
        if not self.meta.get("slug") or self.meta.get("workspace") not in STAGES:
            raise StageError("not a hub note (needs slug and workspace): %s" % self.note)
        self.slug = self.meta["slug"]
        self.workspace = self.meta["workspace"]
        self.ws_dir = REPO / "workspaces" / self.workspace
        self.build = BUILD_DIR / self.slug
        self.dry_run = dry_run
        self.fresh = fresh
        self._log = log or (lambda m: print(m, file=sys.stderr, flush=True))

    # -- small helpers ------------------------------------------------------
    def say(self, msg: str) -> None:
        self._log("[%s] %s" % (self.slug, msg))

    def plan(self, msg: str) -> None:
        print("  " + msg, flush=True)

    def refresh(self) -> dict:
        self.meta, _ = hubnote.read(self.note)
        return self.meta

    def stage_out(self, stage: str, suffix: str) -> pathlib.Path:
        return self.ws_dir / "stages" / stage / "output" / ("%s-%s" % (self.slug, suffix))

    def require(self, path: pathlib.Path, what: str) -> None:
        if self.dry_run:
            self.plan("needs %s: %s%s" % (what, path, "" if path.exists() else " (absent here)"))
            return
        if not path.exists():
            raise StageError("missing %s: %s" % (what, path))

    # -- actions --------------------------------------------------------------
    def run(self, cmd, name: str, cwd=None, timeout=None, env=None, check: bool = True):
        cmd = [str(c) for c in cmd]
        shown = " ".join(shlex.quote(c) for c in cmd)
        where = " (cwd %s)" % cwd if cwd else ""
        if self.dry_run:
            self.plan("$ %s%s" % (shown, where))
            return DryResult()
        self.say("%s: %s%s" % (name, shown, where))
        t0 = time.time()
        try:
            res = subprocess.run(cmd, cwd=str(cwd) if cwd else None, env=env,
                                 capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            raise StageError("%s timed out after %ss" % (name, timeout))
        except FileNotFoundError as e:
            raise StageError("%s: command not found: %s" % (name, e.filename or cmd[0]))
        self._save_output(name, res)
        self.say("%s: exit %d after %ds" % (name, res.returncode, time.time() - t0))
        if check and res.returncode != 0:
            raise StageError("%s exited %d: %s" % (name, res.returncode, _tail(res.stderr or res.stdout)))
        return res

    def _save_output(self, name: str, res) -> None:
        d = self.build / "logs"
        d.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        (d / ("%s-%s.log" % (name, stamp))).write_text(
            "exit %d\n--- stdout ---\n%s\n--- stderr ---\n%s\n" % (res.returncode, res.stdout, res.stderr),
            encoding="utf-8")
        for line in _tail(res.stderr, 15, 2000).splitlines():
            self.say("  | " + line)

    def claude(self, prompt: str, name: str, max_turns: int = 200, timeout: int = CLAUDE_TIMEOUT) -> dict:
        cmd = ["claude", "-p", "--dangerously-skip-permissions", "--output-format", "json",
               "--max-turns", str(max_turns), prompt]
        env = dict(os.environ)
        env.pop("CLAUDECODE", None)  # never look like a nested interactive session
        env["BLAI_BUILD_DIR"] = str(BUILD_DIR)
        env["BLAI_REPO_DIR"] = str(REPO)
        res = self.run(cmd, name + "-claude", cwd=self.ws_dir, timeout=timeout, env=env, check=False)
        if self.dry_run:
            return {}
        info = _parse_json(res.stdout)
        info = info if isinstance(info, dict) else {}
        self.say("%s: claude turns=%s cost_usd=%s is_error=%s" % (
            name, info.get("num_turns"), info.get("total_cost_usd"), info.get("is_error")))
        if res.returncode != 0 or info.get("is_error"):
            detail = _tail(str(info.get("result") or res.stderr or res.stdout), 5)
            raise StageError("%s: claude -p failed (exit %d): %s" % (name, res.returncode, detail))
        return info

    def write_text(self, path: pathlib.Path, text: str) -> None:
        if self.dry_run:
            self.plan("write %s" % path)
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.say("wrote %s" % path)

    def read_json(self, path: pathlib.Path, fixture: dict) -> dict:
        if self.dry_run:
            self.plan("read %s" % path)
            return dict(fixture)
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            raise StageError("expected output missing: %s" % path)
        except ValueError as e:
            raise StageError("bad JSON in %s: %s" % (path, e))

    def hub_update(self, **fields) -> None:
        if self.dry_run:
            self.plan("hub set " + " ".join("%s=%s" % (k, v) for k, v in fields.items()))
            return
        hubnote.update(self.note, **fields)
        self.refresh()

    def journal(self, line: str) -> None:
        if self.dry_run:
            self.plan("hub journal: " + line)
            return
        hubnote.append_section(self.note, "Build journal", line)

    def link_artifact(self, label: str, stage: str, stem: str) -> None:
        """Replace `- <Label>: (filled by stage NN)` in the hub note with the wikilink."""
        link = "- %s: [[stages/%s/output/%s]]" % (label, stage, stem)
        if self.dry_run:
            self.plan("hub artifacts: " + link)
            return
        meta, body = hubnote.read(self.note)
        pat = re.compile(r"^- %s: \(filled by stage \d\d\)[ \t]*$" % re.escape(label), re.M)
        if pat.search(body):
            hubnote.write(self.note, meta, pat.sub(link, body, count=1))


# -- voice (shorts 06, long-form 09) ------------------------------------------
def _voice(ctx: Ctx, stage: str, fmt: str) -> str:
    out = ctx.build / "voice"
    if fmt == "short":
        storyboard = ctx.stage_out("04-script", "storyboard.json")
        ctx.require(storyboard, "storyboard")
        script = out / "narration.txt"
        if ctx.dry_run:
            ctx.plan("extract narration_full from %s -> %s" % (storyboard, script))
        else:
            text = json.loads(storyboard.read_text(encoding="utf-8")).get("narration_full", "").strip()
            if not text:
                raise StageError("storyboard has no narration_full: %s" % storyboard)
            out.mkdir(parents=True, exist_ok=True)
            script.write_text(text + "\n", encoding="utf-8")
        source = ["--storyboard", storyboard]
    else:
        script = ctx.stage_out("05-script", "narration.txt")
        ctx.require(script, "narration text")
        source = ["--text", script]
    wav = out / "narration.wav"
    if ctx.fresh or ctx.dry_run or not (wav.exists() and (out / "voice.json").exists()):
        ctx.run([PY, SCRIPT["generate_audio"], *source, "--out", out, "--format", fmt],
                "generate_audio", timeout=VOICE_TIMEOUT)
    else:
        ctx.say("reusing %s (pass --fresh to regenerate)" % wav)
    # qa_transcribe.py exits 1 when WER > threshold but still writes qa.json: read it, write the
    # voice note, then fail with the mismatches (a missing qa.json means the engine itself failed).
    qa_res = ctx.run([PY, SCRIPT["qa_transcribe"], "--audio", wav, "--script", script, "--out", out],
                     "qa_transcribe", timeout=QA_TIMEOUT, check=False)
    if not ctx.dry_run and qa_res.returncode != 0 and not (out / "qa.json").exists():
        raise StageError("qa_transcribe exited %d: %s" % (qa_res.returncode, _tail(qa_res.stderr or qa_res.stdout)))
    ctx.run([PY, SCRIPT["captions"], "--alignment", out / "alignment.json", "--script", script, "--out", out],
            "captions", timeout=CAPTIONS_TIMEOUT)
    voice = ctx.read_json(out / "voice.json", VOICE_FIXTURE)
    qa = ctx.read_json(out / "qa.json", QA_FIXTURE)
    ctx.write_text(ctx.stage_out(stage, "voice.md"), voice_note(ctx, stage, fmt, voice, qa))
    ctx.link_artifact("Voice", stage, ctx.slug + "-voice")
    wer = float(qa.get("wer") or 0)
    mism = qa.get("mismatches") or []
    if not qa.get("pass"):
        heard = "; ".join("expected %r heard %r" % (m.get("expected", ""), m.get("heard", "")) for m in mism[:3])
        raise StageError("voice QA failed: WER %.3f, %d mismatch(es): %s" % (wer, len(mism), heard))
    return "voice %.1fs, wer %.3f" % (float(voice.get("duration_s") or 0), wer)


def voice_note(ctx: Ctx, stage: str, fmt: str, voice: dict, qa: dict) -> str:
    mism = qa.get("mismatches") or []
    lines = [
        "# Voice: %s" % ctx.slug, "",
        "Stage %s on %s at %s. Audio lives in `$BLAI_BUILD_DIR/%s/voice/` (binaries are never committed)."
        % (stage, socket.gethostname(), _now(), ctx.slug), "",
        "| Field | Value |", "|-------|-------|",
        "| Format | %s |" % fmt,
        "| Duration | %.1f s |" % float(voice.get("duration_s") or 0),
        "| Characters | %s |" % voice.get("chars", ""),
        "| Chunks | %s |" % voice.get("chunks", ""),
        "| Model | %s |" % voice.get("model", ""),
        "| Credits estimate | %s |" % voice.get("credits_estimate", ""),
        "| WER | %.3f (threshold 0.03) |" % float(qa.get("wer") or 0),
        "| QA | %s |" % ("pass" if qa.get("pass") else "FAIL"),
        "", "## Mismatches",
    ]
    lines += ['- at %.1f s: expected "%s", heard "%s"' % (float(m.get("at_s") or 0), m.get("expected", ""),
                                                         m.get("heard", "")) for m in mism] or ["- none"]
    lines += ["", "## Files", "",
              "`narration.wav`, `alignment.json`, `captions.json`, `captions.srt`, `transcript.json`, "
              "`qa.json`, `voice.json`", ""]
    return "\n".join(lines)


def stage_voice_shorts(ctx: Ctx) -> str:
    """generate_audio.py (storyboard) + qa_transcribe.py + captions.py -> <slug>-voice.md"""
    return _voice(ctx, "06-voice", "short")


def stage_voice_long(ctx: Ctx) -> str:
    """generate_audio.py (narration.txt) + qa_transcribe.py + captions.py -> <slug>-voice.md"""
    return _voice(ctx, "09-voice", "long")


# -- render (shorts 07, long-form 10) -----------------------------------------
def _render(ctx: Ctx, stage: str, want_thumbnails: bool) -> str:
    ctx.claude(UNATTENDED.format(stage=stage, slug=ctx.slug, build=ctx.build), stage, max_turns=200)
    checks = [(ctx.build / "render" / "final.mp4", "final.mp4"),
              (ctx.stage_out(stage, "render.md"), "render note")]
    if want_thumbnails:
        checks.append((ctx.build / "render" / "thumbnails" / "1.png", "thumbnails/1.png"))
    if ctx.dry_run:
        for p, what in checks:
            ctx.plan("verify %s exists: %s" % (what, p))
        ctx.plan("verify hub status == review (the stage sends the gate card)")
        return "dry-run"
    missing = [what for p, what in checks if not (p.exists() and p.stat().st_size > 0)]
    status = ctx.refresh().get("status")
    if status != "review":
        missing.append("hub status is %r, expected review" % status)
    if missing:
        raise StageError("%s: after claude -p: %s" % (stage, "; ".join(missing)))
    ctx.link_artifact("Render", stage, ctx.slug + "-render")
    return "render ok, status=review"


def stage_render_shorts(ctx: Ctx) -> str:
    """claude -p (stages/07-render/CONTEXT.md) -> render/final.mp4, <slug>-render.md, status=review"""
    return _render(ctx, "07-render", want_thumbnails=False)


def stage_render_long(ctx: Ctx) -> str:
    """claude -p (stages/10-render/CONTEXT.md) -> final.mp4 + thumbnails, <slug>-render.md, status=review"""
    return _render(ctx, "10-render", want_thumbnails=True)


# -- capture (long-form 08) ---------------------------------------------------
NO_EXPERIMENT = ("# Capture: {slug}\n\nNo experiment: `stages/03-research/output/{slug}-experiment.md` "
                 "does not exist, so there was nothing to capture and nothing to reconcile "
                 "(stage 08-capture on {host} at {now}).\n")


def stage_capture(ctx: Ctx) -> str:
    """capture.py (experiment plan, night window) then claude -p reconcile -> <slug>-capture.md"""
    stage = "08-capture"
    plan = ctx.stage_out("03-research", "experiment.md")
    note = ctx.stage_out(stage, "capture.md")
    if not plan.exists():
        if ctx.dry_run:
            ctx.plan("experiment file absent (%s): would write a 'no experiment' note and skip; "
                     "with a plan the commands would be:" % plan)
        else:
            ctx.say("no experiment file (%s): nothing to capture" % plan)
            ctx.write_text(note, NO_EXPERIMENT.format(slug=ctx.slug, host=socket.gethostname(), now=_now()))
            ctx.link_artifact("Capture", stage, ctx.slug + "-capture")
            return "no experiment, skipped"
    window = (ctx.meta.get("capture_window") or "night").strip().lower() or "night"
    cap = ctx.build / "capture"
    if ctx.fresh or ctx.dry_run or not (cap / "capture.json").exists():
        ctx.run([PY, SCRIPT["capture"], "--plan", plan, "--out", cap, "--window", window],
                "capture", timeout=CAPTURE_TIMEOUT)
    else:
        ctx.say("reusing %s (pass --fresh to capture again)" % (cap / "capture.json"))
    ctx.claude(RECONCILE.format(slug=ctx.slug, build=ctx.build), stage, max_turns=100)
    if ctx.dry_run:
        ctx.plan("verify capture note exists: %s; verify hub status != blocked" % note)
        return "dry-run"
    meta = ctx.refresh()
    if meta.get("status") == "blocked":
        raise StageError("reconcile blocked the run: %s" % meta.get("blocked_reason", ""))
    if not note.exists():
        raise StageError("reconcile did not write %s" % note)
    ctx.link_artifact("Capture", stage, ctx.slug + "-capture")
    return "capture and reconcile ok"


# -- publish (shorts 08, long-form 11) ----------------------------------------
def _publish(ctx: Ctx, stage: str, package_stage: str, with_thumbnail: bool) -> str:
    if not ctx.dry_run and ctx.meta.get("status") != "approved":
        raise StageError("%s: hub status is %r, expected approved" % (stage, ctx.meta.get("status")))
    package = ctx.stage_out(package_stage, "package.md")
    video = ctx.build / "render" / "final.mp4"
    ctx.require(package, "package note")
    ctx.require(video, "final.mp4")
    cmd = [PY, SCRIPT["publish"], "--package", package, "--video", video, "--slot", "auto"]
    if with_thumbnail:
        pick = re.sub(r"\.png$", "", (ctx.meta.get("thumbnail_pick") or "1").strip()) or "1"
        thumb = ctx.build / "render" / "thumbnails" / (pick + ".png")
        ctx.require(thumb, "thumbnail")
        cmd += ["--thumbnail", thumb]
    privacy = os.environ.get("BLAI_PUBLISH_PRIVACY", "").strip()
    if privacy:
        cmd += ["--privacy", privacy]
    marker = ctx.build / "publish.json"  # one post per slug, even when a later step fails
    if marker.exists() and not ctx.fresh and not ctx.dry_run:
        ctx.say("reusing %s from an earlier attempt (not posting again)" % marker)
        info = json.loads(marker.read_text(encoding="utf-8"))
    else:
        res = ctx.run(cmd, "publish", timeout=PUBLISH_TIMEOUT)
        info = PUBLISH_FIXTURE if ctx.dry_run else _parse_json(res.stdout)
        if not isinstance(info, dict) or not info.get("post_submission_id"):
            raise StageError("publish.py printed no post_submission_id: %s" % _tail(res.stdout, 5))
        if not ctx.dry_run:
            marker.parent.mkdir(parents=True, exist_ok=True)
            marker.write_text(json.dumps(info, indent=2), encoding="utf-8")
    post_id = str(info.get("post_submission_id"))
    slot = str(info.get("scheduled_time") or "")
    ctx.write_text(ctx.stage_out(stage, "publish.md"), publish_note(ctx, stage, info, privacy))
    ctx.hub_update(status="scheduled", blotato_post_id=post_id, publish_slot=slot)
    ctx.link_artifact("Publish", stage, ctx.slug + "-publish")
    write_published(ctx, stage, post_id, slot)
    try:
        ctx.run([PY, SCRIPT["send_card"], "--kind", "checklist", "--hub", ctx.note], "checklist-card",
                timeout=CARD_TIMEOUT)
    except StageError as e:  # the post is scheduled; a missing card must not re-run publish
        ctx.say("warning: checklist card failed: %s" % e)
    return "scheduled %s (post %s)" % (slot or "next slot", post_id)


def publish_note(ctx: Ctx, stage: str, info: dict, privacy: str) -> str:
    return "\n".join([
        "# Publish: %s" % ctx.slug, "",
        "Stage %s on %s at %s via Blotato." % (stage, socket.gethostname(), _now()), "",
        "| Field | Value |", "|-------|-------|",
        "| Post submission id | %s |" % info.get("post_submission_id", ""),
        "| Scheduled time | %s |" % info.get("scheduled_time", ""),
        "| Media url | %s |" % info.get("media_url", ""),
        "| Thumbnail url | %s |" % info.get("thumbnail_url", ""),
        "| Privacy | %s |" % (privacy or "(publish.py default)"),
        "", "The build loop polls `publish.py --status` after the slot and fills `youtube_url` in the hub "
        "note and in `published/%s.md`." % ctx.slug, ""])


def write_published(ctx: Ctx, stage: str, post_id: str, slot: str) -> None:
    path = ctx.ws_dir / "published" / (ctx.slug + ".md")
    meta = {"slug": ctx.slug, "title": ctx.meta.get("title", ""), "published_slot": slot,
            "youtube_url": "", "blotato_post_id": post_id}
    body = "# %s\n\nHub note: [[videos/%s]]\nPublish note: [[stages/%s/output/%s-publish]]\n" % (
        ctx.meta.get("title") or ctx.slug, ctx.slug, stage, ctx.slug)
    if ctx.dry_run:
        ctx.plan("write %s (frontmatter: slug, title, published_slot, youtube_url, blotato_post_id)" % path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    hubnote.write(path, meta, body)
    ctx.say("wrote %s" % path)


def stage_publish_shorts(ctx: Ctx) -> str:
    """publish.py (05-package, final.mp4, slot auto) -> <slug>-publish.md, published/<slug>.md, status=scheduled"""
    return _publish(ctx, "08-publish", "05-package", with_thumbnail=False)


def stage_publish_long(ctx: Ctx) -> str:
    """publish.py (07-package, final.mp4, thumbnail <thumbnail_pick or 1>.png) -> <slug>-publish.md, status=scheduled"""
    return _publish(ctx, "11-publish", "07-package", with_thumbnail=True)


def poll_status(ctx: Ctx):
    """publish.py --status <blotato_post_id>. Returns (state, youtube_url, raw) with state in
    scheduled | published | failed."""
    post_id = ctx.meta.get("blotato_post_id", "")
    if not post_id:
        raise StageError("hub note has no blotato_post_id")
    res = ctx.run([PY, SCRIPT["publish"], "--status", post_id], "publish-status", timeout=300, check=False)
    if ctx.dry_run:
        return "scheduled", "", {}
    info = _parse_json(res.stdout)
    if res.returncode != 0 or not isinstance(info, dict):
        raise StageError("publish.py --status exited %d: %s" % (res.returncode, _tail(res.stderr or res.stdout, 4)))
    state = str(info.get("status") or info.get("state") or "").strip().lower()
    url = _find_url(info)
    if state in PUBLISHED_STATES or (url and "youtu" in url):
        return "published", url, info
    if state in FAILED_STATES or info.get("error"):
        return "failed", "", info
    return "scheduled", url, info


# -- the table ----------------------------------------------------------------
STAGES = {
    "shorts": [
        Stage("06-voice", "mechanical", "shorts", stage_voice_shorts),
        Stage("07-render", "creative", "shorts", stage_render_shorts),
    ],
    "long-form": [
        Stage("08-capture", "mixed", "long-form", stage_capture),
        Stage("09-voice", "mechanical", "long-form", stage_voice_long),
        Stage("10-render", "creative", "long-form", stage_render_long),
    ],
}
PUBLISH = {
    "shorts": Stage("08-publish", "mechanical", "shorts", stage_publish_shorts),
    "long-form": Stage("11-publish", "mechanical", "long-form", stage_publish_long),
}


def all_stages():
    for ws in ("shorts", "long-form"):
        for st in STAGES[ws]:
            yield st
        yield PUBLISH[ws]


def find_stage(name: str, workspace: str):
    for st in all_stages():
        if st.name == name and st.workspace == workspace:
            return st
    return None


def run_stage(note, stage: Stage, dry_run: bool = False, fresh: bool = False, log=None):
    """Run one stage for one hub note. Returns (ok, seconds, message); never raises."""
    t0 = time.time()
    try:
        ctx = Ctx(note, dry_run=dry_run, fresh=fresh, log=log)
        msg = stage.fn(ctx) or "ok"
        return True, time.time() - t0, msg
    except StageError as e:
        return False, time.time() - t0, str(e)
    except Exception as e:  # noqa: BLE001 - a stage must never take the loop down
        return False, time.time() - t0, "%s: %s" % (type(e).__name__, e)


def print_table() -> None:
    print("%-10s %-11s %-10s %s" % ("workspace", "stage", "kind", "what runs"))
    for st in all_stages():
        print("%-10s %-11s %-10s %s" % (st.workspace, st.name, st.kind, (st.fn.__doc__ or "").strip()))
    print("\nrepo: %s\nbuild dir: %s" % (REPO, BUILD_DIR))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print the stage table and exit")
    ap.add_argument("--note", help="hub note: workspaces/<ws>/videos/<slug>.md")
    ap.add_argument("--stage", help="stage to run, for example 06-voice or 11-publish")
    ap.add_argument("--poll", action="store_true", help="poll publish.py --status for a scheduled note")
    ap.add_argument("--dry-run", action="store_true", help="print the commands instead of running them")
    ap.add_argument("--fresh", action="store_true", help="ignore build-dir outputs from earlier attempts")
    a = ap.parse_args(argv)
    if a.list:
        print_table()
        return 0
    if not a.note or not (a.stage or a.poll):
        ap.print_usage()
        print("stage_runner: --note with --stage or --poll, or --list", file=sys.stderr)
        return 2
    meta, _ = hubnote.read(a.note)
    if a.poll:
        try:
            state, url, _raw = poll_status(Ctx(a.note, dry_run=a.dry_run))
        except StageError as e:
            print("poll failed: %s" % e, file=sys.stderr)
            return 1
        print(json.dumps({"state": state, "youtube_url": url}))
        return 0
    stage = find_stage(a.stage, meta.get("workspace", ""))
    if stage is None:
        print("no stage %s for workspace %s (see --list)" % (a.stage, meta.get("workspace")), file=sys.stderr)
        return 2
    if a.dry_run:
        print("plan %s %s (%s):" % (stage.name, meta.get("slug"), stage.kind))
    ok, secs, msg = run_stage(a.note, stage, dry_run=a.dry_run, fresh=a.fresh)
    print("%s %s %ds: %s" % (stage.name, "ok" if ok else "fail", secs, msg))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
