#!/usr/bin/env python3
"""Factory health for a human: one daily message, plus alerts the moment something needs you.

    python3 tools/health_check.py --mode daily  [--send]   # 08:05 CT: digest + health, ~15 short lines
    python3 tools/health_check.py --mode alerts [--send]   # hourly: only what is wrong, deduped 6 h

Daily message = a DIGEST (what posted, what waits for your tap, what failed and why, what is in
production today) followed by HEALTH marks: services, preflight, the GLM coding-plan quota (a
5-token probe; HTTP 429 = bucket empty, with Z.ai's reset time), the Kimi balance and its 24 h
spend (alert over --kimi-daily-limit dollars), today's scene-worker credits, disk, GPU, cron
jobs, the R2 public host. Every line starts with a mark: ok, warning, or failed. No jargon
dumps: the reason a Short blocked is one sentence. State lives in build/state/health.json.

Delivery: --send posts Telegram HTML through skills/telegram-gate/scripts/send_card.py
--kind text --html (the gate bot). Without --send the text is printed. Exit 0 always;
--strict exits 1 when an alert fired. Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import html
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(os.environ.get("BLAI_REPO_DIR") or HERE.parent).resolve()
BUILD_DIR = pathlib.Path(os.environ.get("BLAI_BUILD_DIR") or (pathlib.Path.home() / "blai" / "builds"))
sys.path.insert(0, str(REPO / "tools"))
import hubnote  # noqa: E402

WS = REPO / "workspaces" / "shorts"
STATE = REPO / "build" / "state" / "health.json"
SERVICES = ("hermes-gateway.service", "hermes-serve.service", "blai-telegram-bot.service")
FLASH = (2.3, 0.56, 8.0)  # input, cached, output credit multipliers per 10K tokens (Z.ai docs)
GLM53 = (6.9, 1.7, 24.0)
DEDUPE_S = 6 * 3600
OK, WARN, FAIL = "✅", "⚠️", "❌"
STAGE_WORDS = {"01-radar": "radar", "02-ideas": "ideas", "03-research": "research", "04-script": "script",
               "05-package": "package", "06-voice": "voice", "07-render": "render", "08-publish": "publish"}


def esc(s) -> str:
    return html.escape(str(s), quote=False)


def sh(cmd, timeout=60, env=None) -> tuple:
    try:
        p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, timeout=timeout, env=env)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return 127, "", str(e)


def now_local() -> dt.datetime:
    return dt.datetime.now().astimezone()


def human_reason(reason: str) -> str:
    reason = (reason or "").strip()
    stage = ""
    changed = True
    while changed:
        changed = False
        for key, word in STAGE_WORDS.items():
            if reason.startswith(key + ":"):
                reason, stage, changed = reason[len(key) + 1:].strip(), word, True
    reason = reason.split("\n")[0][:140] or "no reason recorded"
    return ("%s stage: %s" % (stage, reason)) if stage else reason


def fmt_slot(iso: str) -> str:
    try:
        t = dt.datetime.fromisoformat(str(iso).strip('"'))
        return t.strftime("%a %H:%M")
    except ValueError:
        return str(iso)


class Health:
    def __init__(self, a):
        self.a = a
        self.alerts: list = []   # (fingerprint, text)
        self.health: list = []   # (mark, text)
        self.digest: list = []
        self.state = self.load_state()

    # -- state ----------------------------------------------------------------
    def load_state(self) -> dict:
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {"kimi": [], "sent": {}}

    def save_state(self) -> None:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(json.dumps(self.state, indent=2) + "\n", encoding="utf-8")

    def alert(self, key: str, text: str) -> None:
        self.alerts.append((key, text))

    def mark(self, ok, text: str) -> None:
        self.health.append((OK if ok else WARN, text))

    # -- digest ---------------------------------------------------------------
    def build_digest(self) -> None:
        since = (now_local() - dt.timedelta(hours=36)).strftime("%Y-%m-%d")
        rows = []
        for p in hubnote.find(WS):
            meta, _ = hubnote.read(p)
            rows.append(meta)
        posted = [m for m in rows if m.get("status") == "published" and str(m.get("updated", ""))[:10] >= since]
        waiting = [m for m in rows if m.get("status") == "review"]
        scheduled = [m for m in rows if m.get("status") == "scheduled"]
        blocked = [m for m in rows if m.get("status") == "blocked"]
        today = now_local().strftime("%Y-%m-%d")
        producing = [m for m in rows if str(m.get("slug", "")).startswith(today)
                     and m.get("status") in ("idea", "researched", "scripted", "ready-to-build")]
        for m in posted:
            self.digest.append("▶️ <b>Posted:</b> %s\n%s" % (esc(m.get("title") or m.get("slug")), esc(m.get("youtube_url") or "")))
        for m in scheduled:
            self.digest.append("⏰ <b>Posting %s:</b> %s" % (fmt_slot(m.get("publish_slot", "")), esc(m.get("title") or m.get("slug"))))
        for m in waiting:
            # only a Short whose video is on THIS box is tappable here; August proof runs were built on the Mac
            if (BUILD_DIR / str(m.get("slug")) / "render" / "final.mp4").exists():
                self.digest.append("\U0001f3ac <b>Waiting for your tap:</b> %s (its card is in this chat)" % esc(m.get("title") or m.get("slug")))
        for m in blocked:
            self.digest.append("%s <b>Failed:</b> %s\n%s. It retries on the next build pass; tap Retry on its card to go now."
                               % (FAIL, esc(m.get("title") or m.get("slug")), esc(human_reason(str(m.get("blocked_reason") or "")))))
            self.alert("blocked:" + str(m.get("slug")), "%s Build failed: %s. %s" % (FAIL, esc(m.get("title") or m.get("slug")),
                                                                                   esc(human_reason(str(m.get("blocked_reason") or "")))))
        for m in producing:
            self.digest.append("\U0001f6e0 <b>In production:</b> %s (%s)" % (esc(m.get("title") or m.get("slug")), esc(m.get("status"))))
        if not self.digest:
            self.digest.append("Nothing moved in the last 36 hours.")

    # -- health checks --------------------------------------------------------
    def services(self) -> None:
        if not shutil.which("systemctl"):
            self.mark(True, "services: not checked on this host")
            return
        down = []
        for s in SERVICES:
            rc, out, _ = sh(["systemctl", "--user", "is-active", s], timeout=15)
            if out != "active":
                down.append(s.replace(".service", ""))
        if down:
            self.alert("services", "%s Service down: %s. Runs will not start until it is back." % (FAIL, ", ".join(down)))
        self.mark(not down, "services: " + ("all running" if not down else "DOWN: " + ", ".join(down)))

    def preflight(self) -> None:
        rc, out, err = sh([sys.executable, REPO / "tools" / "preflight.py", "--quick", "--json"], timeout=120)
        failed = []
        for line in out.splitlines():
            try:
                c = json.loads(line)
            except ValueError:
                continue
            if c.get("required") and not c.get("ok"):
                failed.append(str(c.get("check")))
        if failed:
            self.alert("preflight", "%s Preflight failed: %s. Nothing will build until fixed." % (FAIL, ", ".join(failed)))
        self.mark(not failed, "tools: " + ("all present" if not failed else "missing " + ", ".join(failed)))

    def morning(self) -> None:
        today = now_local().strftime("%Y-%m-%d")
        ideas_note = WS / "stages" / "02-ideas" / "output" / ("%s-ideas.md" % today)
        hour = now_local().hour
        if hour >= 8 and not ideas_note.exists():
            self.alert("stale-ideas", "%s No ideas run today by %02d:00. Tomorrow's 06:00 job will try again; ask me if you want it now." % (WARN, hour))
            self.mark(False, "morning run: no ideas note today")
        else:
            self.mark(True, "morning run: ideas note %s" % ("present" if ideas_note.exists() else "not due yet"))

    def glm_quota(self) -> None:
        sysf, userf = REPO / "build" / "state" / "probe-sys.txt", REPO / "build" / "state" / "probe-user.txt"
        sysf.parent.mkdir(parents=True, exist_ok=True)
        sysf.write_text("Reply with one word.", encoding="utf-8")
        userf.write_text("OK", encoding="utf-8")
        rc, out, err = sh([sys.executable, REPO / "tools" / "llm_call.py", "--provider", "zai", "--model", "glm-5.3-flash",
                           "--system-file", sysf, "--user-file", userf, "--max-tokens", "3"], timeout=60)
        msg = (err or out)[-300:]
        if rc == 0:
            self.mark(True, "GLM plan: answering")
        elif "429" in msg and "limit" in msg.lower():
            reset = ""
            for tok in msg.split():
                if tok.startswith("20") and ":" in tok:
                    reset = tok.strip("'\"}]).,")
            self.alert("glm-quota", "%s GLM plan limit reached. Builds and scripts pause until the reset%s; free fallback covers scene code only."
                       % (WARN, (" (" + reset + " Beijing time)") if reset else ""))
            self.mark(False, "GLM plan: LIMIT REACHED%s" % ((", resets " + reset) if reset else ""))
        else:
            self.alert("glm-error", "%s GLM did not answer the probe: %s" % (WARN, esc(msg[-120:])))
            self.mark(False, "GLM plan: probe failed")

    def kimi(self) -> None:
        key = os.environ.get("KIMI_API_KEY", "").strip()
        if not key:
            self.mark(False, "Kimi: key not in env, balance unknown")
            return
        req = urllib.request.Request("https://api.moonshot.ai/v1/users/me/balance", headers={"Authorization": "Bearer " + key})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                bal = float((json.loads(r.read().decode("utf-8")).get("data") or {}).get("available_balance"))
        except Exception as e:  # noqa: BLE001
            self.mark(False, "Kimi: balance query failed (%s)" % esc(str(e)[:60]))
            return
        readings = [x for x in self.state.get("kimi", []) if time.time() - x["t"] < 8 * 86400]
        readings.append({"t": time.time(), "balance": bal})
        self.state["kimi"] = readings[-400:]
        older = [x for x in readings if time.time() - x["t"] >= 86400 - 1800]
        base = older[-1]["balance"] if older else readings[0]["balance"]
        spent = max(0.0, round(base - bal, 2))
        ok = spent <= self.a.kimi_daily_limit and bal >= self.a.kimi_min_balance
        self.mark(ok, "Kimi: $%.2f left, $%.2f spent in 24h (limit $%.0f/day)" % (bal, spent, self.a.kimi_daily_limit))
        if spent > self.a.kimi_daily_limit:
            self.alert("kimi-spend", "%s Kimi spent $%.2f in 24h, over the $%.0f/day limit. Check the Moonshot console for what used it." % (WARN, spent, self.a.kimi_daily_limit))
        if bal < self.a.kimi_min_balance:
            self.alert("kimi-balance", "%s Kimi balance is $%.2f. Top up or the script writers stall." % (WARN, bal))

    def scene_credits(self) -> None:
        today = now_local().date()
        tot, scenes, fails = 0.0, 0, 0
        for h in glob.glob(str(BUILD_DIR / "*" / "workers" / "*" / "handback.json")):
            try:
                if dt.datetime.fromtimestamp(os.path.getmtime(h)).date() != today:
                    continue
                d = json.loads(pathlib.Path(h).read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            scenes += 1
            fails += 0 if d.get("status") == "ok" else 1
            for u in d.get("usage") or []:
                m = FLASH if "flash" in str(u.get("model", "")) else GLM53
                tot += ((u.get("prompt_tokens") or 0) * m[0] + (u.get("completion_tokens") or 0) * m[2]) / 10000.0
        self.mark(True, "GLM spent today: ~%.0f credits on %d scene%s%s" % (tot, scenes, "" if scenes == 1 else "s",
                                                                          (", %d failed" % fails) if fails else ""))

    def resources(self) -> None:
        try:
            du = shutil.disk_usage(str(BUILD_DIR if BUILD_DIR.exists() else pathlib.Path.home()))
            free_pct = 100.0 * du.free / du.total
            self.mark(free_pct >= 10, "disk: %.0f%% free" % free_pct)
            if free_pct < 10:
                self.alert("disk", "%s Disk is %.0f%% free. Renders will start failing." % (WARN, free_pct))
        except OSError:
            pass
        rc, out, _ = sh(["nvidia-smi", "--query-gpu=utilization.gpu,temperature.gpu", "--format=csv,noheader"], timeout=20)
        if rc == 0 and out:
            parts = [x.strip().replace(" %", "%") for x in out.splitlines()[0].split(",")[:2]]
            self.mark(True, "GPU: %s busy, %s C" % tuple(parts) if len(parts) == 2 else "GPU: " + out.splitlines()[0])

    def cron(self) -> None:
        hermes = shutil.which("hermes") or str(pathlib.Path.home() / ".local" / "bin" / "hermes")
        rc, out, _ = sh([hermes, "cron", "list", "--all"], timeout=60)
        if rc != 0:
            self.mark(False, "schedule: could not list jobs")
            return
        active, paused, cur = [], [], None
        for line in out.splitlines():
            s = line.strip()
            if s.endswith("[active]"):
                cur = "active"
            elif s.endswith("[paused]"):
                cur = "paused"
            elif s.startswith("Name:") and cur:
                (active if cur == "active" else paused).append(s.split(":", 1)[1].strip().replace("blai-", ""))
                cur = None
        self.mark(not paused, "schedule: %d jobs active%s" % (len(active), ("; paused: " + ", ".join(paused)) if paused else ""))

    def r2(self) -> None:
        base = os.environ.get("R2_PUBLIC_BASE_URL", "").strip()
        if not base:
            return
        try:
            urllib.request.urlopen(urllib.request.Request(base + "/", method="HEAD"), timeout=15)
            self.mark(True, "video host: reachable")
        except Exception as e:  # noqa: BLE001
            code = getattr(e, "code", None)
            if code in (400, 403, 404):
                self.mark(True, "video host: reachable")
            else:
                self.alert("r2", "%s The public video host is unreachable (%s). Posting will fail." % (FAIL, esc(str(e)[:60])))
                self.mark(False, "video host: unreachable")

    # -- run ------------------------------------------------------------------
    def run(self) -> tuple:
        self.build_digest()
        self.services()
        self.preflight()
        self.morning()
        self.glm_quota()
        self.kimi()
        self.scene_credits()
        self.resources()
        self.cron()
        self.r2()
        stamp = now_local().strftime("%a %b %-d, %H:%M")
        sent = self.state.setdefault("sent", {})
        fresh = []
        for key, text in self.alerts:
            if time.time() - sent.get(key, 0) > DEDUPE_S:
                fresh.append(text)
                sent[key] = time.time()
        for key in list(sent):
            if not any(k == key for k, _ in self.alerts) and time.time() - sent[key] > DEDUPE_S:
                del sent[key]
        self.save_state()
        if self.a.mode == "daily":
            out = ["<b>BLAI morning report, %s</b>" % esc(stamp), ""]
            out += self.digest
            out += ["", "<b>Health</b>"]
            out += ["%s %s" % (m, esc(t)) for m, t in self.health]
            return "\n".join(out), bool(self.alerts)
        if fresh:
            return "<b>BLAI alert, %s</b>\n" % esc(stamp) + "\n".join(fresh), True
        return "", False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["daily", "alerts"], default="daily")
    ap.add_argument("--send", action="store_true", help="deliver through the gate bot (send_card.py --kind text --html)")
    ap.add_argument("--kimi-daily-limit", type=float, default=float(os.environ.get("BLAI_KIMI_DAILY_LIMIT_USD", 10)))
    ap.add_argument("--kimi-min-balance", type=float, default=float(os.environ.get("BLAI_KIMI_MIN_BALANCE_USD", 5)))
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    text, alerted = Health(a).run()
    if text:
        print(text)
        if a.send:
            rc, out, err = sh([sys.executable, REPO / "skills" / "telegram-gate" / "scripts" / "send_card.py",
                               "--kind", "text", "--html", "--text", text], timeout=60)
            if rc != 0:
                print("send failed: %s" % (err or out)[-200:], file=sys.stderr)
    return 1 if (a.strict and alerted) else 0


if __name__ == "__main__":
    sys.exit(main())
