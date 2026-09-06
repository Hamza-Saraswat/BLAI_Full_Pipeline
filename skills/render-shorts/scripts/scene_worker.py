#!/usr/bin/env python3
"""Deterministic scene worker: one scene, one model call per round, the rules read verbatim.

    scene_worker.py --packet BUILD/scenes-work/s4-packet.json --work-dir BUILD/workers/s4 \
                    --scenes-dir BUILD/scenes [--provider zai] [--model glm-5.3-flash] \
                    [--fallback opencode-free:nemotron-3-ultra-free[,provider:model...]] \
                    [--max-rounds 3] [--skill-dir skills/render-shorts] [--dry-run]

Why a script and not an agent (2026-09-05): an agent worker spends ~40 tool calls per scene and
re-sends its whole context on each, which is where 73% of the GLM credits went. This script
does what `rules/scene-agent.md` orders, in order, with the model called only to write the
scene file: round 1 = the rules (`scene-agent.md`, the tool rules, `styles/<pack>.md`, the
pack snippet for HyperFrames) + the packet -> the complete file; every later round = the same
plus the previous file and the exact failure report. The canonical rule files are read at run
time, never copied (ICM Pattern 5).

Per round: write the file -> static audits (HyperFrames: lint, validate, inspect --strict) ->
render -> ffprobe (1080x1920, 30 fps, duration within tolerance) -> safe_zone_check.py --scene
--stills 9 -> lint_video.py (scene mode) -> head/tail stillness (advisory, rule 10). Pass ->
copy to <scenes-dir>/<scene_id>.mp4 and write work-dir/handback.json (the Handback fields).
Exit 0 on success, 1 when --max-rounds is exhausted or the model is unreachable. Stdout: one
JSON line (the handback). Stdlib only; `tools/llm_call.py` is imported for the model call.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
SKILL_DEFAULT = HERE.parent
REPO = SKILL_DEFAULT.parent.parent
sys.path.insert(0, str(REPO / "tools"))
import llm_call  # noqa: E402

FPS = 30
RENDER_TIMEOUT = 900
STATIC_TIMEOUT = 300


def sh(cmd, cwd=None, timeout=STATIC_TIMEOUT, env=None) -> tuple:
    try:
        p = subprocess.run([str(c) for c in cmd], cwd=str(cwd) if cwd else None, env=env,
                           capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or ""), (p.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, "", "timed out after %ss" % timeout
    except FileNotFoundError as e:
        return 127, "", "not found: %s" % e


def tail(text: str, n: int = 25, limit: int = 3000) -> str:
    lines = [ln for ln in (text or "").strip().splitlines() if ln.strip()]
    out = "\n".join(lines[-n:])
    return out[-limit:]


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def browser_path() -> str:
    env = os.environ.get("HYPERFRAMES_BROWSER_PATH", "").strip()
    if env:
        return env
    hits = sorted(glob.glob(str(pathlib.Path.home() / ".cache" / "ms-playwright" / "chromium-*" / "chrome-linux" / "chrome")))
    return hits[-1] if hits else ""


def ffprobe(mp4: pathlib.Path) -> dict:
    rc, out, err = sh(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                       "stream=width,height,r_frame_rate:format=duration", "-of", "json", mp4], timeout=60)
    if rc != 0:
        return {"error": tail(err, 3)}
    d = json.loads(out or "{}")
    st = (d.get("streams") or [{}])[0]
    num, _, den = (st.get("r_frame_rate") or "0/1").partition("/")
    fps = float(num) / float(den or 1) if den else 0.0
    return {"width": st.get("width"), "height": st.get("height"), "fps": round(fps, 3),
            "duration": float((d.get("format") or {}).get("duration") or 0)}


def stillness(mp4: pathlib.Path, seconds: float = 0.5) -> list:
    """Advisory head/tail motion check (scene-agent.md rule 10): YMAX > 100 AND a YAVG spike."""
    rc, out, _ = sh(["ffprobe", "-v", "error", "-f", "lavfi",
                     "movie=%s,tblend=all_mode=difference,signalstats" % str(mp4).replace(":", "\\:"),
                     "-show_entries", "frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.YMAX",
                     "-of", "csv=p=0"], timeout=120)
    if rc != 0 or not out.strip():
        return []
    rows = []
    for line in out.strip().splitlines():
        parts = line.split(",")
        try:
            rows.append((float(parts[0]), float(parts[1])))
        except (ValueError, IndexError):
            continue
    n = int(seconds * FPS)
    flags = []
    if len(rows) > 2 * n:
        if any(ya > 2.0 and ym > 100 for ya, ym in rows[:n]):
            flags.append("motion inside the first %.1fs (rule 10 stillness)" % seconds)
        if any(ya > 2.0 and ym > 100 for ya, ym in rows[-n:]):
            flags.append("motion inside the last %.1fs (rule 10 stillness)" % seconds)
    return flags


def extract_code(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)  # reasoning leaked into content
    blocks = re.findall(r"```[a-zA-Z0-9_-]*\n(.*?)```", text, re.S)
    if blocks:
        return max(blocks, key=len).strip("\n") + "\n"
    # an unterminated fence (truncated reply) still yields the file body
    m = re.search(r"```[a-zA-Z0-9_-]*\n(.*)$", text, re.S)
    if m:
        return m.group(1).strip("\n") + "\n"
    return text.strip() + "\n"


class Worker:
    def __init__(self, a):
        self.a = a
        self.packet = json.loads(pathlib.Path(a.packet).read_text(encoding="utf-8"))
        self.sid = str(self.packet["scene_id"])
        self.tool = self.packet.get("tool", "hyperframes")
        self.pack = self.packet.get("pack", "")
        self.target = float(self.packet["target_duration_s"])
        self.tol = float(self.packet.get("tolerance_s", 0.15))
        self.skill = pathlib.Path(a.skill_dir).resolve()
        self.work = pathlib.Path(a.work_dir).resolve()
        self.scenes = pathlib.Path(a.scenes_dir).resolve()
        self.work.mkdir(parents=True, exist_ok=True)
        self.scenes.mkdir(parents=True, exist_ok=True)
        self.usage = []
        self.chain = [(a.provider, a.model)] + [tuple(x.split(":", 1)) for x in a.fallback.split(",") if ":" in x]

    # -- prompt --------------------------------------------------------------
    def rules_text(self) -> str:
        files = [self.skill / "rules" / "scene-agent.md",
                 self.skill / "rules" / ("%s-1.md" % self.tool), self.skill / "rules" / ("%s-2.md" % self.tool),
                 self.skill / "styles" / ("%s.md" % self.pack)]
        if self.tool == "hyperframes":
            files.append(self.skill / "hyperframes" / "packs" / ("%s-snippet.html" % self.pack))
        parts = []
        for f in files:
            t = read(f)
            if t:
                parts.append("===== FILE: %s =====\n%s" % (f.relative_to(self.skill), t))
        return "\n\n".join(parts)

    def deliverable(self) -> str:
        frames = int(round(self.target * FPS))
        if self.tool == "hyperframes":
            return ("Deliver ONE fenced code block containing the COMPLETE index.html for this scene, under 260 lines. "
                    "It sits at the HyperFrames project root, links packs/vendor/gsap.min.js and packs/%s.css exactly "
                    "like the pack snippet, keeps the snippet's root composition contract (data-composition-id, "
                    "data-width/data-height, data-duration=\"%.2f\" = %d frames at 30 fps, the window.__timelines "
                    "registration). Start the reply with the fence; no prose before or after it, no second block."
                    % (self.pack, self.target, frames))
        return ("Deliver ONE fenced code block containing the COMPLETE Python file %s.py, under 200 lines, defining "
                "class %s(Scene). It is rendered from skills/render-shorts/manim/ (manim.cfg applies): import from "
                "blai_layout and blai_packs, Text()/Pango only, total animation time exactly %.2f s (%d frames at 30 "
                "fps). Start the reply with the fence; no prose before or after it, no second block."
                % (self.sid, self.scene_class(), self.target, frames))

    def scene_class(self) -> str:
        return "Scene" + self.sid.upper()

    def system_prompt(self) -> str:
        return ("You are a BLAI scene worker. Obey every rule below; the linters that follow enforce them. "
                "Output only the requested file.\n\n" + self.rules_text())

    def user_prompt(self, round_no: int, prev_code: str, report: str) -> str:
        u = "Scene packet (the spec):\n```json\n%s\n```\n\n%s" % (json.dumps(self.packet, indent=2, ensure_ascii=False),
                                                                self.deliverable())
        if round_no > 1 or (report and prev_code):
            u += ("\n\nRound %d. The previous file FAILED verification. Fix exactly what the report names and keep "
                  "everything else.\n\nFailure report:\n%s\n\nPrevious file:\n```\n%s```" % (round_no, report, prev_code))
        return u

    # -- model ---------------------------------------------------------------
    def ask(self, round_no: int, prev_code: str, report: str) -> str:
        system, user = self.system_prompt(), self.user_prompt(round_no, prev_code, report)
        last = ""
        chain = list(self.chain)
        if round_no >= self.a.escalate_from and self.a.escalate and ":" in self.a.escalate:
            # from round 3 on: the stronger seat first (Flash failed twice), the usual chain behind it
            chain = [tuple(self.a.escalate.split(":", 1))] + chain
        for provider, model in chain:
            try:
                extra = {"thinking": {"type": "disabled"}} if provider == "zai" else None
                text, usage = llm_call.complete(provider, model, system, user, max_tokens=self.a.max_tokens,
                                                timeout=self.a.model_timeout, extra_body=extra)
                usage.update({"round": round_no, "provider": provider})
                self.usage.append(usage)
                (self.work / ("round-%d.response.md" % round_no)).write_text(text, encoding="utf-8")
                if usage.get("finish_reason") == "length":
                    # a truncated file never lints; make the next round shorten it instead of guessing
                    text = "```\n" + extract_code(text) + "```\n"
                    self.truncated = True
                else:
                    self.truncated = False
                return text
            except RuntimeError as e:
                last = str(e)
                m = re.search(r"HTTP (\d{3})", last)
                code = int(m.group(1)) if m else 0
                if code in (429, 500, 502, 503, 504, 0):
                    continue  # quota, overload or unreachable: next seat in the chain
                raise SystemExit("scene_worker %s: %s %s: %s" % (self.sid, provider, model, last))
        raise SystemExit("scene_worker %s: every provider failed; last: %s" % (self.sid, last))

    # -- files + renders ------------------------------------------------------
    def hf_dir(self) -> pathlib.Path:
        """A fresh per-scene HyperFrames project on the first call of a run: an agent worker may
        have left files (or a dangling symlink, which .exists() reports as absent) in the same
        directory on an earlier day (2026-09-05, s02)."""
        hf = self.work / "hf"
        if not getattr(self, "_hf_ready", False):
            if hf.exists() or hf.is_symlink():
                shutil.rmtree(hf, ignore_errors=True)
            hf.mkdir(parents=True, exist_ok=True)
            src = self.skill / "hyperframes"
            for name in ("hyperframes.json", "meta.json", "package.json", "package-lock.json"):
                if (src / name).exists():
                    shutil.copy2(src / name, hf / name)
            for link in ("node_modules", "packs"):
                target = hf / link
                if target.is_symlink() or target.exists():
                    target.unlink() if target.is_symlink() else shutil.rmtree(target)
                os.symlink(src / link, target)
            self._hf_ready = True
        return hf

    def write_file(self, code: str) -> pathlib.Path:
        if self.tool == "hyperframes":
            p = self.hf_dir() / "index.html"
        else:
            p = self.work / ("%s.py" % self.sid)
        p.write_text(code, encoding="utf-8")
        return p

    def static_checks(self) -> list:
        if self.tool != "hyperframes":
            return []
        hf, cli = self.hf_dir(), self.skill / "hyperframes" / "node_modules" / ".bin" / "hyperframes"
        env = dict(os.environ)
        bp = browser_path()
        if bp:
            env["HYPERFRAMES_BROWSER_PATH"] = bp
        fails = []
        for name, args in (("lint", ["lint"]), ("validate", ["validate"]),
                           ("inspect", ["inspect", "--samples", "40", "--at-transitions", "--strict"])):
            rc, out, err = sh([cli, *args], cwd=hf, env=env)
            if rc != 0:
                fails.append("hyperframes %s exit %d:\n%s" % (name, rc, tail(out + "\n" + err)))
        return fails

    def render(self) -> tuple:
        out = self.work / ("%s.mp4" % self.sid)
        if out.exists():
            out.unlink()
        if self.tool == "hyperframes":
            hf, cli = self.hf_dir(), self.skill / "hyperframes" / "node_modules" / ".bin" / "hyperframes"
            env = dict(os.environ)
            bp = browser_path()
            if bp:
                env["HYPERFRAMES_BROWSER_PATH"] = bp
            rc, o, e = sh([cli, "render", "--output", out, "--fps", str(FPS), "--quality", "high"],
                          cwd=hf, timeout=RENDER_TIMEOUT, env=env)
            if rc != 0 or not out.exists():
                return None, "hyperframes render exit %d:\n%s" % (rc, tail(o + "\n" + e))
            return out, ""
        manim_dir = self.skill / "manim"
        py = manim_dir / ".venv" / "bin" / "manim"
        src = self.work / ("%s.py" % self.sid)
        rc, o, e = sh([py, "render", src, self.scene_class()], cwd=manim_dir, timeout=RENDER_TIMEOUT)
        if rc != 0:
            return None, "manim render exit %d:\n%s" % (rc, tail(o + "\n" + e))
        hits = sorted(glob.glob(str(manim_dir / "media" / "videos" / self.sid / "*" / (self.scene_class() + ".mp4"))),
                      key=os.path.getmtime)
        if not hits:
            return None, "manim produced no %s.mp4 under media/videos/%s" % (self.scene_class(), self.sid)
        shutil.copy2(hits[-1], out)
        return out, ""

    def verify(self, mp4: pathlib.Path) -> tuple:
        """(hard failures, advisory flags, probe)"""
        fails, flags = [], []
        pr = ffprobe(mp4)
        if pr.get("error"):
            return ["ffprobe: %s" % pr["error"]], flags, pr
        if (pr.get("width"), pr.get("height")) != (1080, 1920):
            fails.append("resolution %sx%s != 1080x1920" % (pr.get("width"), pr.get("height")))
        if abs(pr.get("fps", 0) - FPS) > 0.01:
            fails.append("fps %s != 30" % pr.get("fps"))
        if abs(pr["duration"] - self.target) > self.tol:
            fails.append("duration %.2fs vs target %.2fs (tolerance %.2fs)" % (pr["duration"], self.target, self.tol))
        rc, o, e = sh([sys.executable, self.skill / "scripts" / "safe_zone_check.py", mp4, "--scene", "--stills", "9"],
                      timeout=300)
        if rc != 0:
            fails.append("safe_zone_check exit %d:\n%s" % (rc, tail(o + "\n" + e, 12)))
        rc, o, e = sh([sys.executable, self.skill / "scripts" / "lint_video.py", mp4], timeout=120)
        if rc != 0:
            fails.append("lint_video exit %d:\n%s" % (rc, tail(o + "\n" + e, 12)))
        flags += stillness(mp4)
        return fails, flags, pr

    # -- loop ----------------------------------------------------------------
    def run(self) -> int:
        t0 = time.time()
        code, report, attempts, pr, flags = "", "", 0, {}, []
        history = []
        # A previous run of this scene (a stage retry) leaves its last report and file behind:
        # start informed instead of repeating the same first draft.
        prev_report = self.work / "last-report.txt"
        if prev_report.exists() and not self.a.dry_run:
            report = "A previous run of this scene failed with:\n" + prev_report.read_text(encoding="utf-8")[-3000:]
            prev_file = self.hf_dir() / "index.html" if self.tool == "hyperframes" else self.work / ("%s.py" % self.sid)
            code = read(prev_file) if prev_file.exists() else ""
        for round_no in range(1, self.a.max_rounds + 1):
            attempts = round_no
            if self.a.dry_run:
                print(json.dumps({"dry_run": True, "scene_id": self.sid, "tool": self.tool, "pack": self.pack,
                                  "system_chars": len(self.system_prompt()), "user_chars": len(self.user_prompt(1, "", "")),
                                  "chain": self.chain}))
                return 0
            code = extract_code(self.ask(round_no, code, report))
            self.write_file(code)
            fails = ["reply truncated at max_tokens (%d): the file must be shorter; drop decoration, keep the "
                     "contract" % self.a.max_tokens] if getattr(self, "truncated", False) else []
            fails += self.static_checks() if not fails else []
            mp4 = None
            if not fails:
                mp4, err = self.render()
                if err:
                    fails.append(err)
            if not fails and mp4 is not None:
                fails, flags, pr = self.verify(mp4)
            history.append({"round": round_no, "failures": [f.splitlines()[0][:160] for f in fails]})
            (self.work / ("round-%d.report.txt" % round_no)).write_text("\n\n".join(fails) or "PASS\n", encoding="utf-8")
            if fails:
                (self.work / "last-report.txt").write_text("\n\n".join(fails), encoding="utf-8")
            if not fails and mp4 is not None:
                final = self.scenes / ("%s.mp4" % self.sid)
                shutil.copy2(mp4, final)
                hb = self.handback(attempts, pr, flags, history, str(final), "ok", t0)
                print(json.dumps(hb))
                return 0
            report = "\n\n".join(fails)
        hb = self.handback(attempts, pr, flags, history, "", "failed: " + tail(report, 6, 500), t0)
        print(json.dumps(hb))
        return 1

    def handback(self, attempts, pr, flags, history, path, status, t0) -> dict:
        hb = {"scene_id": self.sid, "tool": self.tool, "pack": self.pack, "status": status, "attempts": attempts,
              "target_s": self.target, "duration_s": round(float(pr.get("duration") or 0), 2), "final_path": path,
              "flagged": flags, "history": history, "usage": self.usage, "seconds": round(time.time() - t0, 1)}
        (self.work / "handback.json").write_text(json.dumps(hb, indent=2) + "\n", encoding="utf-8")
        return hb


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packet", required=True)
    ap.add_argument("--work-dir", required=True)
    ap.add_argument("--scenes-dir", required=True)
    ap.add_argument("--skill-dir", default=str(SKILL_DEFAULT))
    ap.add_argument("--provider", default=os.environ.get("BLAI_SCENE_PROVIDER", "zai"))
    ap.add_argument("--model", default=os.environ.get("BLAI_SCENE_MODEL", "glm-5.3-flash"))
    ap.add_argument("--fallback", default=os.environ.get("BLAI_SCENE_FALLBACK", "opencode-free:nemotron-3-ultra-free"))
    ap.add_argument("--max-rounds", type=int, default=int(os.environ.get("BLAI_SCENE_ROUNDS", 5)),
                    help="scene-agent.md allows five attempts; a round costs ~4-13 credits")
    ap.add_argument("--escalate", default=os.environ.get("BLAI_SCENE_ESCALATE", "zai:glm-5.3"),
                    help="provider:model tried first from --escalate-from on (empty to disable)")
    ap.add_argument("--escalate-from", type=int, default=3)
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--model-timeout", type=int, default=300)
    ap.add_argument("--dry-run", action="store_true", help="print prompt sizes and the provider chain; no calls")
    a = ap.parse_args()
    return Worker(a).run()


if __name__ == "__main__":
    sys.exit(main())
