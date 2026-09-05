#!/usr/bin/env python3
"""Spark stage table for the BLAI build agent: which stages run on the DGX Spark and how.

Each Spark stage is one row in STAGES (build stages, run in order) or PUBLISH (run when the hub
note is approved): name, kind, workspace, function. Mechanical stages call the skill scripts
directly; creative stages run `claude -p` inside the workspace with the unattended prompt from
_design/builder-brief.md. build.py decides when a stage runs and what happens when it fails.

Library use (build/build.py):
    from stage_runner import STAGES, PUBLISH, Ctx, StageError, run_stage, poll_status
CLI use:
    python3 build/stage_runner.py --list [--local]
    python3 build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --stage 06-voice --dry-run
    python3 build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --stage 06-voice --local
    python3 build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --poll

Paths: repo root = BLAI_REPO_DIR (default: the parent of build/), per-slug binaries =
BLAI_BUILD_DIR/<slug>/ (default $HOME/blai/builds). Every skill script path is computed from the
repo root. Exit codes: 0 ok, 1 the stage failed, 2 usage.

--local is the credential-free test mode for a developer machine (build/README.md, "Local test run
on a Mac"). It needs no API key: voice stages pass --engine kokoro, publish only prints what
publish.py --dry-run would send and leaves the note at approved, the gate card prints through
send_card.py --dry-run while the note still reaches review, a failed WER gate warns instead of
blocking (the local Whisper model, not the voice, sets that floor), the repo is the one this file
lives in and the build dir is <repo>/.local-builds. build.py additionally skips git-sync.
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


def _local_requested() -> bool:
    """--local is read from argv (and BLAI_LOCAL) at import time, because REPO and BUILD_DIR are
    module constants that build.py imports by value before it parses its own arguments."""
    if "--local" in sys.argv[1:]:
        return True
    return (os.environ.get("BLAI_LOCAL") or "").strip().lower() not in ("", "0", "false", "no")


LOCAL = _local_requested()
if LOCAL:  # a developer machine: this checkout, its own build dir, no keys
    REPO = HERE.parent.resolve()
    BUILD_DIR = REPO / ".local-builds"
else:
    REPO = pathlib.Path(os.environ.get("BLAI_REPO_DIR") or HERE.parent).resolve()
    BUILD_DIR = pathlib.Path(os.environ.get("BLAI_BUILD_DIR") or (pathlib.Path.home() / "blai" / "builds"))
sys.path.insert(0, str(REPO / "tools"))
import hubnote  # noqa: E402

SKILLS = REPO / "skills"
SCRIPT = {
    "generate_audio": SKILLS / "elevenlabs-narration" / "scripts" / "generate_audio.py",
    "qa_transcribe": SKILLS / "elevenlabs-narration" / "scripts" / "qa_transcribe.py",
    "captions": SKILLS / "elevenlabs-narration" / "scripts" / "captions.py",
    "publish": SKILLS / "blotato-publish" / "scripts" / "publish.py",
    "send_card": SKILLS / "telegram-gate" / "scripts" / "send_card.py",
    "scene_timing": SKILLS / "render-shorts" / "scripts" / "scene_timing.py",
    "scene_packets": SKILLS / "render-shorts" / "scripts" / "scene_packets.py",
    "scene_worker": SKILLS / "render-shorts" / "scripts" / "scene_worker.py",
    "assemble": SKILLS / "render-shorts" / "scripts" / "assemble.py",
    "render_note": SKILLS / "render-shorts" / "scripts" / "render_note.py",
}
PY = sys.executable or "python3"
RENDER_SKILL = SKILLS / "render-shorts"
# The scripted render (2026-09-05) is the default; --agent-render (or BLAI_AGENT_RENDER=1) keeps
# the claude -p path for interactive creative work. Scene model seats come from the env so the
# seat map lives in build/.env, not here.
AGENT_RENDER = ("--agent-render" in sys.argv[1:]
                or (os.environ.get("BLAI_AGENT_RENDER") or "").strip().lower() not in ("", "0", "false", "no"))
SCENE_TIMEOUT = 30 * 60
ASSEMBLE_TIMEOUT = 40 * 60

# Timeouts (seconds)
CLAUDE_TIMEOUT = 2 * 3600
VOICE_TIMEOUT = 30 * 60
QA_TIMEOUT = 30 * 60
CAPTIONS_TIMEOUT = 10 * 60
PUBLISH_TIMEOUT = 30 * 60
CARD_TIMEOUT = 120

UNATTENDED = ("Run stage {stage} for {slug} in unattended mode. Read CLAUDE.md, then "
              "stages/{stage}/CONTEXT.md, and follow it exactly. Build dir: {build}.")
LOCAL_SUFFIX = (" Local test mode: no paid service is configured, so make no network call that needs "
                "a key, pass --engine kokoro to generate_audio.py, pass --dry-run to every "
                "send_card.py and publish.py call, and leave the hub note at review.")

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

    def __init__(self, note, dry_run: bool = False, fresh: bool = False, log=None, local=None):
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
        self.local = LOCAL if local is None else bool(local)
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
        if self.local:
            prompt += LOCAL_SUFFIX
        cmd = ["claude", "-p", "--dangerously-skip-permissions", "--output-format", "json",
               "--max-turns", str(max_turns), prompt]
        env = dict(os.environ)
        env.pop("CLAUDECODE", None)  # never look like a nested interactive session
        env["BLAI_BUILD_DIR"] = str(BUILD_DIR)
        env["BLAI_REPO_DIR"] = str(REPO)
        if self.local:
            env["BLAI_LOCAL"] = "1"
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


# -- voice (shorts 06) --------------------------------------------------------
def _voice(ctx: Ctx, stage: str) -> str:
    out = ctx.build / "voice"
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
    wav = out / "narration.wav"
    engine = ["--engine", "kokoro"] if ctx.local else []  # local test runs need no ElevenLabs key
    if ctx.fresh or ctx.dry_run or not (wav.exists() and (out / "voice.json").exists()):
        ctx.run([PY, SCRIPT["generate_audio"], *source, "--out", out, "--format", "short", *engine],
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
    ctx.write_text(ctx.stage_out(stage, "voice.md"), voice_note(ctx, stage, voice, qa))
    ctx.link_artifact("Voice", stage, ctx.slug + "-voice")
    wer = float(qa.get("wer") or 0)
    mism = qa.get("mismatches") or []
    if not qa.get("pass"):
        heard = "; ".join("expected %r heard %r" % (m.get("expected", ""), m.get("heard", "")) for m in mism[:3])
        if ctx.local:  # the local Whisper model sets the floor here, not the voice: warn, do not block
            ctx.say("warning: local run, WER %.3f above threshold, %d mismatch(es): %s" % (wer, len(mism), heard))
            ctx.journal("%s local: WER %.3f above threshold, not blocking (see build/README.md)" % (stage, wer))
        else:
            raise StageError("voice QA failed: WER %.3f, %d mismatch(es): %s" % (wer, len(mism), heard))
    return "voice %.1fs, wer %.3f%s" % (float(voice.get("duration_s") or 0), wer,
                                        " (%s)" % voice.get("engine") if ctx.local else "")


def voice_note(ctx: Ctx, stage: str, voice: dict, qa: dict) -> str:
    mism = qa.get("mismatches") or []
    lines = [
        "# Voice: %s" % ctx.slug, "",
        "Stage %s on %s at %s. Audio lives in `$BLAI_BUILD_DIR/%s/voice/` (binaries are never committed)."
        % (stage, socket.gethostname(), _now(), ctx.slug), "",
        "| Field | Value |", "|-------|-------|",
        "| Format | short |",
        "| Engine | %s |" % (voice.get("engine") or "elevenlabs"),
        "| Duration | %.1f s |" % float(voice.get("duration_s") or 0),
        "| Words per second | %s |" % voice.get("words_per_second", ""),
        "| Characters | %s |" % voice.get("chars", ""),
        "| Chunks | %s |" % voice.get("chunks", ""),
        "| Model | %s |" % voice.get("model", ""),
        "| Alignment | %s |" % (voice.get("alignment_source") or "elevenlabs"),
        "| Credits estimate | %s |" % voice.get("credits_estimate", ""),
        "| WER | %.3f (threshold 0.03) |" % float(qa.get("wer") or 0),
        "| QA | %s |" % ("pass" if qa.get("pass") else ("FAIL, not blocking (local run)" if ctx.local else "FAIL")),
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
    return _voice(ctx, "06-voice")


# -- render (shorts 07) -------------------------------------------------------
def _scene_key(path: pathlib.Path) -> tuple:
    """s1, s2, ... s10 in numeric order (ids are 's<N>' or 's0N')."""
    m = re.search(r"(\d+)", path.name)
    return (int(m.group(1)) if m else 0, path.name)


def _render_scripted(ctx: Ctx, stage: str) -> None:
    """scene_timing -> scene_packets -> scene_worker per scene (sequential) -> assemble -> render note
    -> hub review -> gate card. No agent session; the model is called only inside scene_worker."""
    storyboard = ctx.stage_out("04-script", "storyboard.json")
    voice = ctx.build / "voice"
    wav, captions = voice / "narration.wav", voice / "captions.json"
    for p, what in ((storyboard, "storyboard"), (wav, "narration.wav"), (captions, "captions.json")):
        ctx.require(p, what)
    timing = ctx.build / "timing.json"
    ctx.run([PY, SCRIPT["scene_timing"], "--storyboard", storyboard, "--captions", captions, "--out", timing],
            "scene_timing", timeout=120)
    packets = ctx.build / "scenes-work"
    ctx.run([PY, SCRIPT["scene_packets"], "--storyboard", storyboard, "--timing", timing, "--out", packets],
            "scene_packets", timeout=60)
    scenes, workers = ctx.build / "scenes", ctx.build / "workers"
    if not ctx.dry_run:
        scenes.mkdir(parents=True, exist_ok=True)
    packet_files = sorted(packets.glob("*-packet.json"), key=_scene_key) if packets.exists() else []
    if ctx.dry_run and not packet_files:
        ctx.plan("scene_worker.py per packet in %s (sequential, 3 rounds each)" % packets)
    for packet in packet_files:
        sid = packet.name[:-len("-packet.json")]
        clip = scenes / ("%s.mp4" % sid)
        if clip.exists() and not ctx.fresh:
            ctx.say("scene %s: reusing %s (pass --fresh to re-render)" % (sid, clip))
            continue
        res = ctx.run([PY, SCRIPT["scene_worker"], "--packet", packet, "--work-dir", workers / sid,
                       "--scenes-dir", scenes], "scene-" + sid, timeout=SCENE_TIMEOUT, check=False)
        if not ctx.dry_run and res.returncode != 0:
            raise StageError("%s: scene %s failed: %s" % (stage, sid, _tail(res.stdout or res.stderr, 4)))
    render = ctx.build / "render"
    res = ctx.run([PY, SCRIPT["assemble"], "--slug", ctx.slug, "--storyboard", storyboard, "--audio", wav,
                   "--captions", captions, "--scenes-dir", scenes, "--out", render],
                  "assemble", cwd=RENDER_SKILL, timeout=ASSEMBLE_TIMEOUT, check=False)
    info = _parse_json(res.stdout) if not ctx.dry_run else {}
    info = info if isinstance(info, dict) else {}
    if not ctx.dry_run:
        if res.returncode != 0 or not (render / "final.mp4").exists():
            raise StageError("%s: assemble.py exited %d: %s" % (stage, res.returncode, _tail(res.stderr or res.stdout, 5)))
        (render / "assemble.json").write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8")
        if not (info.get("lint_ok") and info.get("safe_zone_ok")):
            raise StageError("%s: release gates failed: lint_ok=%s safe_zone_ok=%s warnings=%s" % (
                stage, info.get("lint_ok"), info.get("safe_zone_ok"), (info.get("warnings") or [])[:3]))
    note = ctx.stage_out(stage, "render.md")
    message_id = ""
    if ctx.local:
        _local_gate_card(ctx, stage)
    else:
        ctx.hub_update(status="review")
        card = ctx.run([PY, SCRIPT["send_card"], "--kind", "gate", "--hub", ctx.note, "--video", render / "final.mp4"],
                       "gate-card", timeout=CARD_TIMEOUT, check=False)
        if not ctx.dry_run:
            if card.returncode != 0:
                raise StageError("%s: send_card.py exited %d: %s" % (stage, card.returncode, _tail(card.stderr or card.stdout, 3)))
            got = _parse_json(card.stdout) or {}
            message_id = str(got.get("message_id") or "")
    ctx.run([PY, SCRIPT["render_note"], "--slug", ctx.slug, "--assemble-json", render / "assemble.json",
             "--workers-dir", workers, "--timing", timing, "--voice-json", voice / "voice.json", "--out", note,
             "--card-message-id", message_id], "render_note", timeout=60)
    if not ctx.dry_run:
        ctx.journal("%s ok %.2fs: %d scenes via scene_worker.py, lint %s, safe-zone %s, loop %s, card message_id %s"
                    % (stage, float(info.get("duration_s") or 0), len(packet_files), info.get("lint_ok"),
                       info.get("safe_zone_ok"), info.get("loop_ok"), message_id or "none"))


def _render(ctx: Ctx, stage: str) -> str:
    if AGENT_RENDER:
        ctx.claude(UNATTENDED.format(stage=stage, slug=ctx.slug, build=ctx.build), stage, max_turns=200)
    else:
        _render_scripted(ctx, stage)
    checks = [(ctx.build / "render" / "final.mp4", "final.mp4"),
              (ctx.stage_out(stage, "render.md"), "render note")]
    if ctx.dry_run:
        for p, what in checks:
            ctx.plan("verify %s exists: %s" % (what, p))
        if ctx.local:
            _local_gate_card(ctx, stage)
        else:
            ctx.plan("verify hub status == review (the stage sends the gate card)")
        return "dry-run"
    missing = [what for p, what in checks if not (p.exists() and p.stat().st_size > 0)]
    if ctx.local and AGENT_RENDER:  # no Telegram token here: print the card the Spark would send, then open the gate
        _local_gate_card(ctx, stage)
    status = ctx.refresh().get("status")
    if status != "review":
        missing.append("hub status is %r, expected review" % status)
    if missing:
        raise StageError("%s: after %s: %s" % (stage, "claude -p" if AGENT_RENDER else "the scripted render",
                                               "; ".join(missing)))
    ctx.link_artifact("Render", stage, ctx.slug + "-render")
    return "render ok, status=review"


def _local_gate_card(ctx: Ctx, stage: str) -> None:
    """Local mode: print the gate card through send_card.py --dry-run and put the note in review."""
    cmd = [PY, SCRIPT["send_card"], "--kind", "gate", "--hub", ctx.note, "--dry-run"]
    video = ctx.build / "render" / "final.mp4"
    if ctx.dry_run or video.exists():
        cmd += ["--video", video]
    res = ctx.run(cmd, "gate-card-dry-run", timeout=CARD_TIMEOUT, check=False)
    if not ctx.dry_run:
        print(res.stdout, flush=True)
        if res.returncode != 0:
            ctx.say("warning: send_card.py --dry-run exited %d: %s" % (res.returncode, _tail(res.stderr, 3)))
        if ctx.refresh().get("status") != "review":
            ctx.hub_update(status="review")
    ctx.journal("%s local: gate card printed with --dry-run, nothing sent, status=review" % stage)


def stage_render_shorts(ctx: Ctx) -> str:
    """claude -p (stages/07-render/CONTEXT.md) -> render/final.mp4, <slug>-render.md, status=review"""
    return _render(ctx, "07-render")



# -- publish (shorts 08) ------------------------------------------------------
def _publish(ctx: Ctx, stage: str, package_stage: str) -> str:
    if not ctx.dry_run and ctx.meta.get("status") != "approved":
        raise StageError("%s: hub status is %r, expected approved" % (stage, ctx.meta.get("status")))
    package = ctx.stage_out(package_stage, "package.md")
    video = ctx.build / "render" / "final.mp4"
    ctx.require(package, "package note")
    ctx.require(video, "final.mp4")
    cmd = [PY, SCRIPT["publish"], "--package", package, "--video", video, "--slot", "auto"]
    privacy = os.environ.get("BLAI_PUBLISH_PRIVACY", "").strip()
    if privacy:
        cmd += ["--privacy", privacy]
    if ctx.local:  # nothing is uploaded and nothing is posted: print the body and stop at approved
        res = ctx.run(cmd + ["--dry-run"], "publish-dry-run", timeout=PUBLISH_TIMEOUT, check=False)
        if not ctx.dry_run:
            print(res.stdout, flush=True)
            if res.returncode != 0:
                ctx.say("warning: publish.py --dry-run exited %d: %s" % (res.returncode, _tail(res.stderr, 4)))
        ctx.journal("%s local: publishing skipped, printed publish.py --dry-run, status stays approved" % stage)
        return "local: publish skipped (dry-run body printed), status stays approved"
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
    return _publish(ctx, "08-publish", "05-package")


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
}
PUBLISH = {
    "shorts": Stage("08-publish", "mechanical", "shorts", stage_publish_shorts),
}


def all_stages():
    for ws in ("shorts",):
        for st in STAGES[ws]:
            yield st
        yield PUBLISH[ws]


def find_stage(name: str, workspace: str):
    for st in all_stages():
        if st.name == name and st.workspace == workspace:
            return st
    return None


def run_stage(note, stage: Stage, dry_run: bool = False, fresh: bool = False, log=None, local=None):
    """Run one stage for one hub note. Returns (ok, seconds, message); never raises."""
    t0 = time.time()
    try:
        ctx = Ctx(note, dry_run=dry_run, fresh=fresh, log=log, local=local)
        msg = stage.fn(ctx) or "ok"
        return True, time.time() - t0, msg
    except StageError as e:
        return False, time.time() - t0, str(e)
    except Exception as e:  # noqa: BLE001 - a stage must never take the loop down
        return False, time.time() - t0, "%s: %s" % (type(e).__name__, e)


LOCAL_NOTES = [
    "voice (06-voice): generate_audio.py --engine kokoro, no ElevenLabs key needed",
    "voice QA: a WER above the threshold warns and journals instead of blocking the note",
    "render (07-render): claude -p is told it is a local run; the gate card prints "
    "through send_card.py --dry-run and the note still reaches review",
    "publish (08-publish): nothing is uploaded or posted; publish.py --dry-run is "
    "printed and the note stays at approved",
    "build.py: no required .env values (paths only), and git-sync is skipped",
]


def print_table() -> None:
    print("%-10s %-11s %-10s %s" % ("workspace", "stage", "kind", "what runs"))
    for st in all_stages():
        print("%-10s %-11s %-10s %s" % (st.workspace, st.name, st.kind, (st.fn.__doc__ or "").strip()))
    print("\nrepo: %s\nbuild dir: %s" % (REPO, BUILD_DIR))
    if LOCAL:
        print("\nlocal mode (--local): credential-free test run on this machine")
        for line in LOCAL_NOTES:
            print("  - " + line)
    else:
        print("\n--list --local shows what the credential-free local test mode changes")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print the stage table and exit "
                    "(with --local: what local mode changes)")
    ap.add_argument("--note", help="hub note: workspaces/<ws>/videos/<slug>.md")
    ap.add_argument("--stage", metavar="NAME", help="run this one stage by hand, for example 06-voice "
                    "or 11-publish (see --list for the names of both workspaces)")
    ap.add_argument("--poll", action="store_true", help="poll publish.py --status for a scheduled note")
    ap.add_argument("--dry-run", action="store_true", help="print the commands instead of running them")
    ap.add_argument("--fresh", action="store_true", help="ignore build-dir outputs from earlier attempts")
    ap.add_argument("--local", action="store_true", help="credential-free local test mode: Kokoro voice, "
                    "no publish, no card sent, build dir <repo>/.local-builds (BLAI_LOCAL=1 does the same)")
    a = ap.parse_args(argv)
    a.local = a.local or LOCAL  # BLAI_LOCAL already moved REPO and BUILD_DIR; keep the stages in step
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
            state, url, _raw = poll_status(Ctx(a.note, dry_run=a.dry_run, local=a.local))
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
        print("plan %s %s (%s)%s:" % (stage.name, meta.get("slug"), stage.kind,
                                      ", local mode" if a.local else ""))
    ok, secs, msg = run_stage(a.note, stage, dry_run=a.dry_run, fresh=a.fresh, local=a.local)
    print("%s %s %ds: %s" % (stage.name, "ok" if ok else "fail", secs, msg))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
