#!/usr/bin/env python3
"""Factory health: one daily report, plus alerts the moment something needs the operator.

    python3 tools/health_check.py --mode daily  [--send]   # 08:05 CT: the full picture
    python3 tools/health_check.py --mode alerts [--send]   # hourly: only what is wrong, deduped 6 h

Checks: user services (hermes-gateway, hermes-serve, blai-telegram-bot), tools/preflight.py,
hub notes (blocked with reasons, counts by status, today's staleness), the GLM coding-plan
quota (a 5-token probe: HTTP 429 = bucket empty, with Z.ai's reset time), the Kimi balance
(Moonshot /v1/users/me/balance; alert when the 24 h drop exceeds --kimi-daily-limit dollars),
today's scene-worker credits (from workers/*/handback.json, Z.ai's multipliers), disk and GPU
headroom, cron job states, the R2 public host. State lives in build/state/health.json.

Delivery: --send posts through skills/telegram-gate/scripts/send_card.py --kind text (the gate
bot). Without --send the text is printed. Exit 0 always (a cron job must not flap); --strict
exits 1 when any alert fired. Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
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
STATUSES = ("idea", "researched", "scripted", "ready-to-build", "review", "approved", "scheduled",
            "published", "rejected", "blocked")
FLASH = (2.3, 0.56, 8.0)  # input, cached, output multipliers per 10K tokens (Z.ai docs)
GLM53 = (6.9, 1.7, 24.0)
DEDUPE_S = 6 * 3600


def sh(cmd, timeout=60, env=None) -> tuple:
    try:
        p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, timeout=timeout, env=env)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return 127, "", str(e)


def now_local() -> dt.datetime:
    return dt.datetime.now().astimezone()


class Health:
    def __init__(self, a):
        self.a = a
        self.alerts: list = []   # (fingerprint, text)
        self.lines: list = []    # daily report lines
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

    # -- checks ---------------------------------------------------------------
    def services(self) -> None:
        if not shutil.which("systemctl"):
            self.lines.append("services: systemctl not available here")
            return
        down = []
        for s in SERVICES:
            rc, out, _ = sh(["systemctl", "--user", "is-active", s], timeout=15)
            if out != "active":
                down.append("%s=%s" % (s.replace(".service", ""), out or "unknown"))
        if down:
            self.alert("services", "SERVICE DOWN: " + ", ".join(down))
        self.lines.append("services: " + ("all 3 active" if not down else ", ".join(down)))

    def preflight(self) -> None:
        rc, out, err = sh([sys.executable, REPO / "tools" / "preflight.py", "--quick", "--json"], timeout=120)
        failed = []
        for line in out.splitlines():
            try:
                c = json.loads(line)
            except ValueError:
                continue
            if c.get("required") and not c.get("ok"):
                failed.append("%s (%s)" % (c.get("check"), (c.get("detail") or "")[:60]))
        if failed:
            self.alert("preflight", "PREFLIGHT FAIL: " + "; ".join(failed))
        self.lines.append("preflight: " + ("all required checks pass" if not failed else "; ".join(failed)))

    def hubs(self) -> None:
        counts = {}
        blocked = []
        for s in STATUSES:
            paths = hubnote.find(WS, s)
            if paths:
                counts[s] = len(paths)
            if s == "blocked":
                for p in paths:
                    meta, _ = hubnote.read(p)
                    blocked.append("%s: %s" % (meta.get("slug"), str(meta.get("blocked_reason") or "")[:90]))
        self.lines.append("hubs: " + (", ".join("%s %d" % (k, v) for k, v in counts.items()) or "none"))
        for b in blocked:
            self.alert("blocked:" + b.split(":")[0], "BLOCKED " + b)
        today = now_local().strftime("%Y-%m-%d")
        ideas_note = WS / "stages" / "02-ideas" / "output" / ("%s-ideas.md" % today)
        hour = now_local().hour
        if hour >= 8 and not ideas_note.exists():
            self.alert("stale-ideas", "NO IDEAS NOTE for %s by %02d:00 (the 06:00 job did not deliver)" % (today, hour))
        self.lines.append("today: ideas note %s; hubs in review %d, scheduled %d" % (
            "present" if ideas_note.exists() else "absent", counts.get("review", 0), counts.get("scheduled", 0)))

    def glm_quota(self) -> None:
        sysf, userf = REPO / "build" / "state" / "probe-sys.txt", REPO / "build" / "state" / "probe-user.txt"
        sysf.parent.mkdir(parents=True, exist_ok=True)
        sysf.write_text("Reply with one word.", encoding="utf-8")
        userf.write_text("OK", encoding="utf-8")
        rc, out, err = sh([sys.executable, REPO / "tools" / "llm_call.py", "--provider", "zai", "--model", "glm-5.3-flash",
                           "--system-file", sysf, "--user-file", userf, "--max-tokens", "3"], timeout=60)
        msg = (err or out)[-300:]
        if rc == 0:
            self.lines.append("glm: coding plan answering (probe ok)")
        elif "429" in msg and "limit" in msg.lower():
            reset = ""
            for tok in msg.split():
                if tok.startswith("20") and ":" in tok:
                    reset = tok.strip("'\"}]).,")
            self.alert("glm-quota", "GLM QUOTA REACHED (Z.ai coding plan)%s. Builds and produce will fail until then; free fallback covers scene code only."
                       % ((" - resets " + reset + " Beijing") if reset else ""))
            self.lines.append("glm: QUOTA REACHED %s" % reset)
        else:
            self.alert("glm-error", "GLM PROBE FAILED: %s" % msg[-160:])
            self.lines.append("glm: probe failed (%s)" % msg[-80:])

    def kimi(self) -> None:
        key = os.environ.get("KIMI_API_KEY", "").strip()
        if not key:
            self.lines.append("kimi: KIMI_API_KEY not in env; balance unknown")
            return
        req = urllib.request.Request("https://api.moonshot.ai/v1/users/me/balance",
                                     headers={"Authorization": "Bearer " + key})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                bal = float((json.loads(r.read().decode("utf-8")).get("data") or {}).get("available_balance"))
        except Exception as e:  # noqa: BLE001
            self.lines.append("kimi: balance query failed (%s)" % str(e)[:80])
            return
        readings = [x for x in self.state.get("kimi", []) if time.time() - x["t"] < 8 * 86400]
        readings.append({"t": time.time(), "balance": bal})
        self.state["kimi"] = readings[-400:]
        older = [x for x in readings if time.time() - x["t"] >= 86400 - 1800]
        base = older[-1]["balance"] if older else readings[0]["balance"]
        spent = round(base - bal, 2)
        self.lines.append("kimi: balance $%.2f; spent last 24h $%.2f (limit $%.0f/day)" % (bal, max(0.0, spent), self.a.kimi_daily_limit))
        if spent > self.a.kimi_daily_limit:
            self.alert("kimi-spend", "KIMI SPEND $%.2f IN 24H exceeds the $%.0f/day limit (balance $%.2f)" % (spent, self.a.kimi_daily_limit, bal))
        if bal < self.a.kimi_min_balance:
            self.alert("kimi-balance", "KIMI BALANCE LOW: $%.2f (top up before the writers stall)" % bal)

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
        self.lines.append("scene credits today: ~%.0f over %d scene(s), %d failed (standard rate; off-peak halves it)" % (tot, scenes, fails))

    def resources(self) -> None:
        try:
            du = shutil.disk_usage(str(BUILD_DIR if BUILD_DIR.exists() else pathlib.Path.home()))
            free_pct = 100.0 * du.free / du.total
            self.lines.append("disk: %.0f%% free (%.0f GB)" % (free_pct, du.free / 1e9))
            if free_pct < 10:
                self.alert("disk", "DISK LOW: %.0f%% free on the build volume" % free_pct)
        except OSError:
            pass
        rc, out, _ = sh(["nvidia-smi", "--query-gpu=memory.used,memory.total,utilization.gpu", "--format=csv,noheader"], timeout=20)
        if rc == 0 and out:
            self.lines.append("gpu: " + out.splitlines()[0])

    def cron(self) -> None:
        hermes = shutil.which("hermes") or str(pathlib.Path.home() / ".local" / "bin" / "hermes")
        rc, out, _ = sh([hermes, "cron", "list", "--all"], timeout=60)
        if rc != 0:
            self.lines.append("cron: hermes cron list failed")
            return
        active, paused = [], []
        cur = None
        for line in out.splitlines():
            s = line.strip()
            if s.endswith("[active]"):
                cur = "active"
            elif s.endswith("[paused]"):
                cur = "paused"
            elif s.startswith("Name:") and cur:
                (active if cur == "active" else paused).append(s.split(":", 1)[1].strip())
                cur = None
        self.lines.append("cron: %d active (%s)%s" % (len(active), ", ".join(active), ("; paused: " + ", ".join(paused)) if paused else ""))

    def r2(self) -> None:
        base = os.environ.get("R2_PUBLIC_BASE_URL", "").strip()
        if not base:
            return
        try:
            req = urllib.request.Request(base + "/", method="HEAD")
            urllib.request.urlopen(req, timeout=15)
            self.lines.append("r2: public host reachable")
        except Exception as e:  # noqa: BLE001
            code = getattr(e, "code", None)
            if code in (400, 403, 404):
                self.lines.append("r2: public host reachable (HTTP %s on /)" % code)
            else:
                self.alert("r2", "R2 PUBLIC HOST UNREACHABLE: %s" % str(e)[:80])

    # -- run ------------------------------------------------------------------
    def run(self) -> tuple:
        self.services()
        self.preflight()
        self.hubs()
        self.glm_quota()
        self.kimi()
        self.scene_credits()
        self.resources()
        self.cron()
        self.r2()
        stamp = now_local().strftime("%Y-%m-%d %H:%M %Z")
        sent = self.state.setdefault("sent", {})
        fresh = []
        for key, text in self.alerts:
            last = sent.get(key, 0)
            if time.time() - last > DEDUPE_S:
                fresh.append(text)
                sent[key] = time.time()
        for key in list(sent):
            if not any(k == key for k, _ in self.alerts) and time.time() - sent[key] > DEDUPE_S:
                del sent[key]
        self.save_state()
        if self.a.mode == "daily":
            head = "BLAI health %s" % stamp
            body = "\n".join(self.lines)
            if self.alerts:
                body += "\n\nATTENTION:\n" + "\n".join(t for _, t in self.alerts)
            return head + "\n" + body, bool(self.alerts)
        if fresh:
            return "BLAI ALERT %s\n" % stamp + "\n".join(fresh), True
        return "", False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["daily", "alerts"], default="daily")
    ap.add_argument("--send", action="store_true", help="deliver through the gate bot (send_card.py --kind text)")
    ap.add_argument("--kimi-daily-limit", type=float, default=float(os.environ.get("BLAI_KIMI_DAILY_LIMIT_USD", 10)))
    ap.add_argument("--kimi-min-balance", type=float, default=float(os.environ.get("BLAI_KIMI_MIN_BALANCE_USD", 5)))
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    text, alerted = Health(a).run()
    if text:
        print(text)
        if a.send:
            rc, out, err = sh([sys.executable, REPO / "skills" / "telegram-gate" / "scripts" / "send_card.py",
                               "--kind", "text", "--text", text], timeout=60)
            if rc != 0:
                print("send failed: %s" % (err or out)[-200:], file=sys.stderr)
    return 1 if (a.strict and alerted) else 0


if __name__ == "__main__":
    sys.exit(main())
