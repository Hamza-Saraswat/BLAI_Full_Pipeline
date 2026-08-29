#!/usr/bin/env python3
"""BLAI build agent: the loop that runs on the DGX Spark.

    python3 build/build.py --once [--dry-run] [--slug S] [--workspace shorts] [--fresh]
    python3 build/build.py --interval 300        # keep looping (the systemd timer normally does this)
    python3 build/build.py --once --local        # credential-free test run on a developer machine

One pass:
  1. take build/locks/build.lock (exit 0 quietly when another pass holds it)
  2. recover uncommitted changes left by an interrupted pass, then git pull --rebase
  3. publish every hub note with status=approved (shorts 08-publish)
  4. poll every note with status=scheduled; flip to published (+ youtube_url) when Blotato says so
  5. build the oldest note with status=ready-to-build, one per pass: status=building + build_host,
     push, run the workspace's Spark stages in order (stage_runner.STAGES), journal every stage,
     push after each; on failure retry the stage once, then status=blocked, blocked_reason,
     journal, push, Telegram blocked card
--dry-run prints the planned commands and touches neither git nor the notes.
--slug picks one note regardless of age: ready-to-build, blocked or stale building notes are
(re)built, approved notes are published, scheduled notes are polled.
--local is the credential-free test mode (build/README.md, "Local test run on a Mac"): no API key
is required, only the paths; the voice stages run the local Kokoro engine; publishing does not
happen (publish.py --dry-run is printed and the note stays at approved); the gate card prints
through send_card.py --dry-run while the note still reaches review; git-sync is skipped;
BLAI_BUILD_DIR is <repo>/.local-builds and BLAI_REPO_DIR is the repo this script lives in.
Exit codes: 0 ok, 1 the pass hit an error, 2 configuration problem (empty required .env values).
Logs: build/logs/<date>.log plus stderr. Per-slug binaries: $BLAI_BUILD_DIR/<slug>/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import os
import pathlib
import socket
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent


def load_env(path: pathlib.Path) -> int:
    """Load KEY=VALUE lines into os.environ (existing variables win). Never prints a value."""
    if not path.exists():
        return 0
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv(path, override=False)
        return 1
    except ImportError:
        pass
    n = 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        if k and k not in os.environ:
            os.environ[k] = v
            n += 1
    return n


load_env(HERE / ".env")  # before stage_runner reads BLAI_REPO_DIR / BLAI_BUILD_DIR
sys.path.insert(0, str(HERE))
import stage_runner as sr  # noqa: E402  (reads --local from sys.argv: it fixes REPO and BUILD_DIR)
from stage_runner import BUILD_DIR, LOCAL, PUBLISH, REPO, STAGES, Ctx, StageError, poll_status, run_stage  # noqa: E402
import hubnote  # noqa: E402  (stage_runner put <repo>/tools on sys.path)

HOST = socket.gethostname()
LOCK = REPO / "build" / "locks" / "build.lock"
LOG_DIR = REPO / "build" / "logs"
WORKSPACES = ("shorts",)
# Keep in sync with the REQUIRED list in build/install.sh and the header of build/.env.example.
REQUIRED_ENV = ("ELEVENLABS_API_KEY", "ELEVEN_VOICE_ID", "BLOTATO_API_KEY", "BLOTATO_YOUTUBE_ACCOUNT_ID",
                "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID", "R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID",
                "R2_SECRET_ACCESS_KEY", "R2_BUCKET", "R2_PUBLIC_BASE_URL")


class PassError(Exception):
    """Abort the whole pass (for example git pull failed)."""


def check_local_paths(log: "Log") -> int:
    """--local requires paths, never keys. Returns 0 when the run can go ahead, else 2."""
    problems = []
    if not (REPO / "workspaces").is_dir() or not (REPO / "skills").is_dir():
        problems.append("%s does not look like the repo (no workspaces/ and skills/)" % REPO)
    if log.dry_run:  # a dry run creates nothing: check the parent instead
        if not BUILD_DIR.exists() and not BUILD_DIR.parent.is_dir():
            problems.append("build dir %s cannot be created: %s is not a directory" % (BUILD_DIR, BUILD_DIR.parent))
    else:
        try:
            BUILD_DIR.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            problems.append("cannot create the build dir %s: %s" % (BUILD_DIR, e))
    if problems:
        log("error: local run cannot start: " + "; ".join(problems))
        return 2
    have = [k for k in REQUIRED_ENV if os.environ.get(k)]
    log("local run: repo %s, build dir %s, %d of %d .env values set (none required)"
        % (REPO, BUILD_DIR, len(have), len(REQUIRED_ENV)))
    return 0


class Log:
    def __init__(self, dry_run: bool):
        self.dry_run = dry_run

    def __call__(self, msg: str) -> None:
        line = "%s %s" % (dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), msg)
        sys.stdout.flush()  # keep dry-run plan lines (stdout) in order with the log (stderr)
        print(line, file=sys.stderr, flush=True)
        if not self.dry_run:
            LOG_DIR.mkdir(parents=True, exist_ok=True)
            day = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
            with open(LOG_DIR / (day + ".log"), "a", encoding="utf-8") as fh:
                fh.write(line + "\n")


# -- lock, git ----------------------------------------------------------------
def acquire_lock(path: pathlib.Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(path), os.O_RDWR | os.O_CREAT, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(fd)
        return None
    os.ftruncate(fd, 0)
    os.write(fd, ("%d %s %s\n" % (os.getpid(), HOST, dt.datetime.now(dt.timezone.utc).isoformat())).encode())
    return fd


def git(*args: str):
    return subprocess.run(["git", *args], cwd=str(REPO), capture_output=True, text=True)


def git_sync(log: Log, message: str) -> bool:
    """Commit everything and push via tools/git-sync.sh (rebase + retry). Returns True on success."""
    if LOCAL:  # a local test run leaves the working tree exactly as it found it
        if log.dry_run:
            print("  git-sync skipped (--local): %r" % message)
        else:
            log("git-sync skipped (--local): %s" % message)
        return True
    if log.dry_run:
        print("  git-sync %r" % message)
        return True
    res = subprocess.run([str(REPO / "tools" / "git-sync.sh"), message], cwd=str(REPO),
                         capture_output=True, text=True)
    for line in (res.stdout + res.stderr).strip().splitlines()[-3:]:
        log("git-sync: " + line)
    if res.returncode != 0:
        log("error: git-sync failed; the changes stay local until the next pass recovers them")
    return res.returncode == 0


def git_refresh(log: Log) -> None:
    if LOCAL:
        log("git skipped (--local): no recovery commit, no pull --rebase, no push")
        return
    if git("status", "--porcelain").stdout.strip():
        log("recovering uncommitted changes from an interrupted pass")
        git_sync(log, "build(%s): recover changes from an interrupted pass" % HOST)
    res = git("pull", "--rebase", "--quiet")
    if res.returncode != 0:
        raise PassError("git pull --rebase failed: %s" % sr._tail(res.stderr or res.stdout, 4))


# -- notes --------------------------------------------------------------------
def scan(workspaces) -> list:
    rows = []
    for ws in workspaces:
        for p in hubnote.find(REPO / "workspaces" / ws):
            meta, _ = hubnote.read(p)
            rows.append((p, meta))
    rows.sort(key=lambda r: (str(r[1].get("created", "")), r[1].get("slug", "")))  # oldest first
    return rows


def journal(p: pathlib.Path, line: str) -> None:
    hubnote.append_section(p, "Build journal", line)


def parse_iso(value: str):
    value = (value or "").strip()
    if not value:
        return None
    try:
        t = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)



def send_blocked_card(log: Log, p: pathlib.Path, reason: str) -> None:
    cmd = [sr.PY, str(sr.SCRIPT["send_card"]), "--kind", "blocked", "--hub", str(p), "--text", reason[:900]]
    if LOCAL:  # no Telegram token on a local run: print the card instead of sending it
        cmd.append("--dry-run")
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=sr.CARD_TIMEOUT)
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        log("warning: blocked card not sent: %s" % e)
        return
    if res.returncode != 0:
        log("warning: blocked card failed (exit %d): %s" % (res.returncode, sr._tail(res.stderr or res.stdout, 3)))


# -- the three kinds of work ----------------------------------------------------
def run_with_retry(log: Log, p: pathlib.Path, meta: dict, stage, fresh: bool) -> bool:
    """Run a stage, retry once, else block the note. Returns True when the stage passed."""
    ws, slug = meta["workspace"], meta["slug"]
    msg = ""
    for attempt in (1, 2):
        ok, secs, msg = run_stage(p, stage, dry_run=False, fresh=(fresh and attempt == 1), log=log)
        journal(p, "%s %s %ds%s" % (stage.name, "ok" if ok else "fail", int(secs), "" if ok else " (%s)" % msg[:160]))
        log("%s %s %s %ds: %s" % (slug, stage.name, "ok" if ok else "fail", int(secs), msg))
        if ok:
            git_sync(log, "build(%s): %s %s ok" % (ws, slug, stage.name))
            return True
        current, _ = hubnote.read(p)
        if current.get("status") == "blocked":
            break  # the stage itself decided (for example the reconcile rule); no retry
        if attempt == 1:
            log("%s: retrying %s once" % (slug, stage.name))
    current, _ = hubnote.read(p)
    if current.get("status") == "blocked" and current.get("blocked_reason"):
        reason = current["blocked_reason"]
    else:
        reason = "%s: %s" % (stage.name, msg)
    hubnote.update(p, status="blocked", blocked_reason=reason[:400])
    journal(p, "blocked at %s" % stage.name)
    git_sync(log, "build(%s): %s blocked at %s" % (ws, slug, stage.name))
    send_blocked_card(log, p, reason)
    return False


def build_note(log: Log, p: pathlib.Path, meta: dict, a) -> bool:
    ws, slug = meta["workspace"], meta["slug"]
    stages = STAGES[ws]
    if a.dry_run:
        sync = "git-sync skipped (--local)" if LOCAL else "git-sync"
        print("build %s (%s, status %s): %s" % (slug, ws, meta.get("status"), " -> ".join(s.name for s in stages)))
        print("  hub set status=building build_host=%s; journal 'build start'; %s" % (HOST, sync))
        for st in stages:
            print("  stage %s (%s):" % (st.name, st.kind))
            run_stage(p, st, dry_run=True, fresh=a.fresh, log=log)
            print("  journal '%s ok <seconds>s'; %s (on failure: retry once, then status=blocked, "
                  "blocked_reason, journal, %s, send_card.py --kind blocked%s)"
                  % (st.name, sync, sync, " --dry-run" if LOCAL else ""))
        return True
    log("build start: %s (%s) on %s" % (slug, ws, HOST))
    hubnote.update(p, status="building", build_host=HOST, blocked_reason="")
    journal(p, "build start on %s" % HOST)
    git_sync(log, "build(%s): %s building on %s" % (ws, slug, HOST))
    for st in stages:
        if not run_with_retry(log, p, meta, st, a.fresh):
            return False
    final, _ = hubnote.read(p)
    journal(p, "build done, status %s" % final.get("status"))
    git_sync(log, "build(%s): %s done, status %s" % (ws, slug, final.get("status")))
    log("build done: %s status=%s" % (slug, final.get("status")))
    return True


def publish_note(log: Log, p: pathlib.Path, meta: dict, a) -> bool:
    ws, slug = meta["workspace"], meta["slug"]
    stage = PUBLISH[ws]
    if a.dry_run:
        print("publish %s (%s, status %s): %s%s" % (slug, ws, meta.get("status"), stage.name,
                                                    " (local: printed, not sent)" if LOCAL else ""))
        run_stage(p, stage, dry_run=True, fresh=a.fresh, log=log)
        print("  journal '%s ok <seconds>s'; %s" % (stage.name, "git-sync skipped (--local)" if LOCAL else "git-sync"))
        return True
    if meta.get("status") == "blocked":  # a blocked publish is retried from approved
        hubnote.update(p, status="approved", blocked_reason="")
    log("publish start: %s (%s)" % (slug, ws))
    return run_with_retry(log, p, meta, stage, a.fresh)


def poll_note(log: Log, p: pathlib.Path, meta: dict, a) -> None:
    ws, slug = meta["workspace"], meta["slug"]
    post_id = meta.get("blotato_post_id", "")
    if not post_id:
        log("%s: scheduled but no blotato_post_id; not polling" % slug)
        return
    slot = parse_iso(meta.get("publish_slot", ""))
    if slot and dt.datetime.now(dt.timezone.utc) < slot:
        if a.dry_run:
            print("poll %s: slot %s not reached, skip" % (slug, meta.get("publish_slot")))
        return
    if a.dry_run:
        print("poll %s (%s): publish.py --status %s; on published: hub set status=published youtube_url=<url>, "
              "update published/%s.md, journal, git-sync" % (slug, ws, post_id, slug))
        return
    try:
        state, url, raw = poll_status(Ctx(p, log=log))
    except StageError as e:
        log("warning: %s: poll failed: %s" % (slug, e))
        return
    if state == "published":
        hubnote.update(p, status="published", youtube_url=url)
        journal(p, "published %s" % (url or "(url not reported yet)"))
        pub = REPO / "workspaces" / ws / "published" / (slug + ".md")
        if pub.exists():
            hubnote.update(pub, youtube_url=url)
        git_sync(log, "publish(%s): %s published" % (ws, slug))
        log("%s: published %s" % (slug, url))
    elif state == "failed":
        reason = "Blotato reported %s for post %s" % (raw.get("status") or "failure", post_id)
        hubnote.update(p, status="blocked", blocked_reason=reason)
        journal(p, "blocked: " + reason)
        git_sync(log, "publish(%s): %s failed at Blotato" % (ws, slug))
        send_blocked_card(log, p, reason)
    else:
        log("%s: still %s at Blotato" % (slug, state))


# -- one pass -----------------------------------------------------------------
def run_pass(a, log: Log) -> int:
    log("pass start host=%s repo=%s build_dir=%s%s%s" % (HOST, REPO, BUILD_DIR,
        " (local)" if LOCAL else "", " (dry-run)" if a.dry_run else ""))
    if LOCAL:
        log("local mode: no key is required, only the paths above")
        for line in sr.LOCAL_NOTES:
            log("  - " + line)
    if not a.dry_run:
        try:
            git_refresh(log)
        except PassError as e:
            log("error: %s" % e)
            return 1
    workspaces = [a.workspace] if a.workspace else list(WORKSPACES)
    rows = scan(workspaces)
    if a.slug:
        rows = [r for r in rows if r[1].get("slug") == a.slug]
        if not rows:
            log("error: no hub note with slug %s in %s" % (a.slug, ", ".join(workspaces)))
            return 1
    rc = 0
    touched = set()
    for p, meta in rows:  # 1. publish approved notes (and re-publish blocked publishes when --slug)
        status = meta.get("status")
        retry_publish = (a.slug and status == "blocked"
                         and str(meta.get("blocked_reason", "")).startswith(PUBLISH[meta["workspace"]].name))
        if status == "approved" or retry_publish:
            touched.add(p)
            if not publish_note(log, p, meta, a):
                rc = 1
    for p, meta in rows:  # 2. poll scheduled notes
        if meta.get("status") == "scheduled":
            touched.add(p)
            poll_note(log, p, meta, a)
    buildable = {"ready-to-build"} | ({"blocked", "building"} if a.slug else set())
    built = None
    for p, meta in rows:  # 3. build one note
        if p in touched or meta.get("status") not in buildable:
            continue
        if not build_note(log, p, meta, a):
            rc = 1
        built = p
        break
    if not touched and built is None:
        log("nothing to do" + (": %s has status %s" % (a.slug, rows[0][1].get("status")) if a.slug else ""))
    log("pass end rc=%d" % rc)
    return rc


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--once", action="store_true", help="run one pass and exit (what the systemd timer does)")
    ap.add_argument("--interval", type=int, default=300, help="seconds between passes without --once (default 300)")
    ap.add_argument("--dry-run", action="store_true", help="print the plan; run nothing, write nothing, no git")
    ap.add_argument("--slug", help="work on this slug only (rebuilds blocked or stale building notes)")
    ap.add_argument("--workspace", choices=list(WORKSPACES), help="scan one workspace only")
    ap.add_argument("--fresh", action="store_true", help="ignore build-dir outputs of earlier attempts "
                    "(regenerate audio, capture again, post again)")
    ap.add_argument("--local", action="store_true", help="credential-free test run on this machine: Kokoro "
                    "voice, no publish, no card sent, no git-sync, build dir <repo>/.local-builds "
                    "(BLAI_LOCAL=1 does the same for a whole shell)")
    a = ap.parse_args(argv)
    a.local = a.local or LOCAL  # BLAI_LOCAL already moved REPO and BUILD_DIR; keep the checks in step
    log = Log(a.dry_run)
    if a.local:
        rc = check_local_paths(log)
        if rc:
            return rc
    else:
        missing = [k for k in REQUIRED_ENV if not os.environ.get(k)]
        if missing and not a.dry_run:
            log("error: build/.env has empty required values: %s; not picking up work" % ", ".join(missing))
            return 2
        if missing:
            log("note: empty required values ignored in dry-run: %s" % ", ".join(missing))
    if a.dry_run:
        return run_pass(a, log)
    fd = acquire_lock(LOCK)
    if fd is None:
        print("build: another pass holds %s; exiting" % LOCK, file=sys.stderr)
        return 0
    try:
        if a.once:
            return run_pass(a, log)
        while True:
            run_pass(a, log)
            time.sleep(max(30, a.interval))
    except KeyboardInterrupt:
        return 0
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
