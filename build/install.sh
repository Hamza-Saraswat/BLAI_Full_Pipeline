#!/usr/bin/env bash
# BLAI DGX Spark installer. User-level where possible, idempotent, safe to re-run.
#
#   bash build/install.sh            # install or update everything, then print the checklist
#   bash build/install.sh --dry-run  # print what would be done, change nothing
#   bash build/install.sh --help
#
# Run it from the clone the build agent should use: /srv/blai/repo when sudo works
# (sudo mkdir -p /srv/blai && sudo chown "$USER" /srv/blai, then git clone), else $HOME/blai/repo.
# BLAI_REPO_DIR (environment, then build/.env, then this clone) is the single source of truth for
# the repo path; BLAI_BUILD_DIR (default $HOME/blai/builds) holds the per-slug binaries.
# Exit 0 when every automated step succeeded (human steps may remain), 1 when a step failed.
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$REPO/build/.env"
BLAI_HOME="$HOME/blai"
VENV="$BLAI_HOME/venv"
LOCAL_BIN="$HOME/.local/bin"
UNIT_DIR="$HOME/.config/systemd/user"
GITHUB_REPO="Hamza-Saraswat/BLAI_Full_Pipeline"
DEPLOY_KEY="$HOME/.ssh/blai_deploy"
NVM_VERSION="v0.40.3"
# Keep in sync with REQUIRED_ENV in build/build.py and the header of build/.env.example.
REQUIRED="BLOTATO_API_KEY BLOTATO_YOUTUBE_ACCOUNT_ID TELEGRAM_BOT_TOKEN TELEGRAM_CHAT_ID R2_ACCOUNT_ID R2_ACCESS_KEY_ID R2_SECRET_ACCESS_KEY R2_BUCKET R2_PUBLIC_BASE_URL"
MANIM_APT="libcairo2-dev libpango1.0-dev pkg-config python3-dev build-essential"
CHROME_APT="libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2t64 libasound2 fonts-liberation"

usage() { sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'; }
DRY=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown flag: $arg" >&2; usage; exit 2 ;;
  esac
done

DONE=(); TODO=(); HARD=0
step() { printf '\n== %s\n' "$*"; }
note() { printf '   %s\n' "$*"; }
ok()   { if [ "$DRY" = 1 ]; then DONE+=("(dry-run) $*"); printf '   would: %s\n' "$*"; else DONE+=("$*"); printf '   done: %s\n' "$*"; fi; }
todo() { TODO+=("$*"); printf '   TODO: %s\n' "$*"; }
fail() { HARD=1; todo "$*"; }
run()  { if [ "$DRY" = 1 ]; then printf '   + %s\n' "$*"; return 0; fi; "$@"; }
have() { command -v "$1" >/dev/null 2>&1; }
envval() { grep -E "^$1=" "$ENV_FILE" 2>/dev/null | head -1 | cut -d= -f2- | sed -e 's/^"//' -e 's/"$//'; }
set_env() {  # set_env KEY VALUE: replace or append the line in build/.env
  if [ "$DRY" = 1 ]; then note "+ $1=$2 in build/.env"; return 0; fi
  [ -f "$ENV_FILE" ] || return 0
  if grep -qE "^$1=" "$ENV_FILE"; then
    sed -i.bak -e "s|^$1=.*|$1=$2|" "$ENV_FILE" && rm -f "$ENV_FILE.bak"
  else
    printf '%s=%s\n' "$1" "$2" >> "$ENV_FILE"
  fi
}

# -- 1. host ----------------------------------------------------------------------
step "1. Host"
ARCH="$(uname -m)"; OS="$(uname -s)"
PRETTY="$( (. /etc/os-release 2>/dev/null && printf '%s' "${PRETTY_NAME:-}") || true)"
note "arch $ARCH, os $OS${PRETTY:+ ($PRETTY)}, user $USER, home $HOME, clone $REPO"
[ "$OS" = "Linux" ] || note "warning: expected Linux (DGX Spark); only a dry run makes sense here"
case "$ARCH" in aarch64|arm64) ;; *) note "warning: expected aarch64" ;; esac
HAVE_SUDO=0
if sudo -n true 2>/dev/null; then HAVE_SUDO=1; fi
note "sudo without a password: $([ "$HAVE_SUDO" = 1 ] && echo yes || echo no)"
note "python3: $(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>/dev/null || echo missing)"
BLAI_REPO_DIR="${BLAI_REPO_DIR:-$(envval BLAI_REPO_DIR)}"
BLAI_REPO_DIR="${BLAI_REPO_DIR:-$REPO}"
if [ "$BLAI_REPO_DIR" != "$REPO" ]; then
  note "warning: BLAI_REPO_DIR=$BLAI_REPO_DIR but this clone is $REPO; using this clone"
  BLAI_REPO_DIR="$REPO"
fi
BLAI_BUILD_DIR="${BLAI_BUILD_DIR:-$(envval BLAI_BUILD_DIR)}"
BLAI_BUILD_DIR="${BLAI_BUILD_DIR:-$BLAI_HOME/builds}"
if [ "$HAVE_SUDO" = 1 ] && [ "$BLAI_REPO_DIR" != "/srv/blai/repo" ]; then
  note "hint: with sudo the recommended clone location is /srv/blai/repo (this clone works too)"
fi
note "BLAI_REPO_DIR=$BLAI_REPO_DIR  BLAI_BUILD_DIR=$BLAI_BUILD_DIR"
run mkdir -p "$BLAI_HOME" "$BLAI_BUILD_DIR" "$REPO/build/logs" "$REPO/build/state" "$REPO/build/locks" "$LOCAL_BIN" "$UNIT_DIR" "$HOME/.ssh"
[ "$DRY" = 1 ] || chmod 700 "$HOME/.ssh"
export PATH="$LOCAL_BIN:$PATH"
ok "directories"

# -- 2. node 22 via nvm --------------------------------------------------------------
step "2. Node 22 (nvm, user-level)"
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
load_nvm() { if [ -s "$NVM_DIR/nvm.sh" ]; then set +u; . "$NVM_DIR/nvm.sh" >/dev/null 2>&1; set -u; fi; }
nvm_run() { set +u; nvm "$@"; local rc=$?; set -u; return $rc; }
node_major() { node -p 'process.versions.node.split(".")[0]' 2>/dev/null || echo 0; }
load_nvm
if have node && [ "$(node_major)" -ge 22 ] 2>/dev/null; then
  ok "node $(node -v) present"
else
  if [ ! -s "$NVM_DIR/nvm.sh" ]; then
    note "installing nvm $NVM_VERSION into $NVM_DIR"
    run bash -c "curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/$NVM_VERSION/install.sh | bash" || fail "nvm install failed; install Node 22 by hand"
    load_nvm
  fi
  if type nvm >/dev/null 2>&1; then
    if run nvm_run install 22 && run nvm_run alias default 22; then ok "node $(node -v 2>/dev/null) via nvm"; else fail "nvm install 22 failed"; fi
  elif [ "$DRY" = 1 ]; then
    note "+ nvm install 22 && nvm alias default 22"
  else
    fail "nvm not loadable; install Node 22 by hand"
  fi
fi
for b in node npm npx; do  # stable paths for the systemd units (their PATH has ~/.local/bin, not nvm)
  if have "$b" && [ "$(command -v "$b")" != "$LOCAL_BIN/$b" ]; then run ln -sfn "$(command -v "$b")" "$LOCAL_BIN/$b"; fi
done

# -- 3. ffmpeg -------------------------------------------------------------------
step "3. ffmpeg"
if have ffmpeg; then
  ok "ffmpeg present ($(ffmpeg -version 2>/dev/null | head -1 | cut -d' ' -f1-3))"
elif [ "$HAVE_SUDO" = 1 ]; then
  run sudo apt-get update -qq
  if run sudo apt-get install -y -qq ffmpeg; then ok "ffmpeg via apt"; else fail "apt-get install ffmpeg failed"; fi
else
  case "$ARCH" in aarch64|arm64) FF_ARCH=linuxarm64 ;; *) FF_ARCH=linux64 ;; esac
  FF_URL="https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-${FF_ARCH}-gpl.tar.xz"
  note "no sudo: installing a static ffmpeg build from BtbN into $LOCAL_BIN"
  note "source: $FF_URL"
  if [ "$DRY" = 1 ]; then
    note "+ curl -fL $FF_URL | tar -xJ; copy bin/ffmpeg and bin/ffprobe into $LOCAL_BIN"
  else
    TMP="$(mktemp -d)"
    if curl -fL --progress-bar "$FF_URL" -o "$TMP/ffmpeg.tar.xz" && tar -xJf "$TMP/ffmpeg.tar.xz" -C "$TMP" \
       && cp "$TMP"/ffmpeg-*/bin/ffmpeg "$TMP"/ffmpeg-*/bin/ffprobe "$LOCAL_BIN/" && chmod +x "$LOCAL_BIN/ffmpeg" "$LOCAL_BIN/ffprobe"; then
      ok "ffmpeg static build in $LOCAL_BIN (no sudo needed)"
    else
      fail "ffmpeg download failed; fetch $FF_URL by hand and copy bin/ffmpeg, bin/ffprobe into $LOCAL_BIN"
    fi
    rm -rf "$TMP"
  fi
fi

# -- 4. python venv ----------------------------------------------------------------
step "4. Python venv $VENV"
if [ ! -x "$VENV/bin/python" ]; then
  if ! run python3 -m venv "$VENV"; then
    if [ "$HAVE_SUDO" = 1 ]; then run sudo apt-get install -y -qq python3-venv && run python3 -m venv "$VENV"; fi
  fi
fi
if [ -x "$VENV/bin/pip" ] || [ "$DRY" = 1 ]; then
  run "$VENV/bin/pip" install -q --upgrade pip
  if run "$VENV/bin/pip" install -q -r "$REPO/build/requirements.txt"; then ok "venv packages from build/requirements.txt"; else fail "pip install -r build/requirements.txt failed"; fi
else
  fail "could not create the venv (apt package python3-venv missing?)"
fi

# -- 5. asciinema ------------------------------------------------------------------
step "5. asciinema"
if have asciinema; then
  ok "asciinema present"
elif have pipx; then
  if run pipx install asciinema; then ok "asciinema via pipx"; else fail "pipx install asciinema failed"; fi
elif [ "$DRY" = 1 ]; then
  note "+ python3 -m pip install --user asciinema (fallback: the venv + a symlink in $LOCAL_BIN)"
elif python3 -m pip install --user -q asciinema 2>/dev/null; then
  ok "asciinema via pip --user"
elif [ -x "$VENV/bin/pip" ] && "$VENV/bin/pip" install -q asciinema && ln -sfn "$VENV/bin/asciinema" "$LOCAL_BIN/asciinema"; then
  ok "asciinema in the venv, linked into $LOCAL_BIN"
else
  fail "asciinema install failed (try: pipx install asciinema)"
fi

# -- 6. claude code cli ------------------------------------------------------------------
step "6. Claude Code CLI"
if have claude; then
  ok "claude present ($(claude --version 2>/dev/null | head -1))"
elif run bash -c "curl -fsSL https://claude.ai/install.sh | bash"; then
  ok "claude installed into $LOCAL_BIN"
else
  fail "claude install failed: curl -fsSL https://claude.ai/install.sh | bash"
fi
if [ -f "$HOME/.claude/.credentials.json" ]; then
  ok "claude login found"
else
  todo "log in once on this box: run 'claude', then '/login' (the render stages run 'claude -p' unattended)"
fi

# -- 7. render projects -----------------------------------------------------------------
step "7. Render projects (npm install, Remotion browser)"
for d in skills/render-shorts/remotion skills/render-shorts/hyperframes; do
  if [ -f "$REPO/$d/package.json" ]; then
    if (cd "$REPO/$d" && run npm install --no-audit --no-fund --loglevel=error); then ok "npm install $d"; else fail "npm install failed in $d"; fi
  else
    note "skip $d (no package.json in this checkout)"
  fi
done
for d in skills/render-shorts/remotion; do
  if [ -f "$REPO/$d/package.json" ]; then
    if (cd "$REPO/$d" && run npx remotion browser ensure); then ok "remotion browser ensure $d"; else fail "npx remotion browser ensure failed in $d"; fi
  fi
done
if [ "$HAVE_SUDO" = 1 ]; then
  if [ "$DRY" = 1 ]; then
    note "+ sudo apt-get install -y <each of> $CHROME_APT (best effort, for the headless browser)"
  else
    for p in $CHROME_APT; do sudo apt-get install -y -qq "$p" >/dev/null 2>&1 || true; done
    ok "headless browser libraries (best effort)"
  fi
else
  note "no sudo: if the Remotion browser fails to start, ask an admin for: $CHROME_APT"
fi

# -- 8. manim ----------------------------------------------------------------------
step "8. manim"
if [ "$HAVE_SUDO" = 1 ]; then
  if run sudo apt-get install -y -qq $MANIM_APT; then ok "manim apt packages"; else fail "apt packages for manim failed: $MANIM_APT"; fi
else
  todo "ask an admin for the manim apt packages: sudo apt-get install -y $MANIM_APT"
fi
if [ -x "$VENV/bin/pip" ] || [ "$DRY" = 1 ]; then
  if run "$VENV/bin/pip" install -q manim; then ok "manim in the venv"; else fail "pip install manim failed (usually the apt packages above)"; fi
fi

# -- 9. github deploy key --------------------------------------------------------------
step "9. GitHub deploy key"
if [ -f "$DEPLOY_KEY" ]; then
  ok "deploy key $DEPLOY_KEY present"
elif run ssh-keygen -q -t ed25519 -N "" -f "$DEPLOY_KEY" -C "blai-deploy@$(hostname)"; then
  ok "generated $DEPLOY_KEY"
else
  fail "ssh-keygen failed"
fi
if grep -qs "^Host github-blai" "$HOME/.ssh/config"; then
  ok "ssh config alias github-blai present"
elif [ "$DRY" = 1 ]; then
  note "+ append 'Host github-blai' (HostName github.com, IdentityFile $DEPLOY_KEY) to ~/.ssh/config"
else
  printf '\nHost github-blai\n  HostName github.com\n  User git\n  IdentityFile %s\n  IdentitiesOnly yes\n' "$DEPLOY_KEY" >> "$HOME/.ssh/config"
  chmod 600 "$HOME/.ssh/config"
  ok "ssh config alias github-blai"
fi
if run git -C "$REPO" remote set-url origin "git@github-blai:$GITHUB_REPO.git"; then ok "origin -> git@github-blai:$GITHUB_REPO.git"; fi
git -C "$REPO" config user.name >/dev/null 2>&1 || run git -C "$REPO" config user.name "BLAI Spark"
git -C "$REPO" config user.email >/dev/null 2>&1 || run git -C "$REPO" config user.email "blai-spark@users.noreply.github.com"
if [ -f "$DEPLOY_KEY.pub" ]; then
  printf '   public key (add it as a deploy key WITH write access at https://github.com/%s/settings/keys):\n   %s\n' "$GITHUB_REPO" "$(cat "$DEPLOY_KEY.pub")"
  if [ "$DRY" = 0 ] && ssh -T -o BatchMode=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=10 git@github-blai 2>&1 | grep -q "successfully authenticated"; then
    ok "GitHub accepts the deploy key"
  else
    todo "add the deploy key above on GitHub (write access), then check with: ssh -T git@github-blai"
  fi
fi

# -- 10. .env ----------------------------------------------------------------------
step "10. build/.env"
if [ -f "$ENV_FILE" ]; then
  ok "build/.env present"
elif run cp "$REPO/build/.env.example" "$ENV_FILE"; then
  ok "created build/.env from build/.env.example"
fi
[ "$DRY" = 1 ] || [ ! -f "$ENV_FILE" ] || chmod 600 "$ENV_FILE"
[ "$(envval BLAI_REPO_DIR)" = "$BLAI_REPO_DIR" ] || set_env BLAI_REPO_DIR "$BLAI_REPO_DIR"
[ "$(envval BLAI_BUILD_DIR)" = "$BLAI_BUILD_DIR" ] || set_env BLAI_BUILD_DIR "$BLAI_BUILD_DIR"
EMPTY=""
for k in $REQUIRED; do [ -n "$(envval "$k")" ] || EMPTY="$EMPTY $k"; done
if [ -n "$EMPTY" ]; then todo "fill these in build/.env:$EMPTY"; else ok "all required .env values are set"; fi

# -- 11. systemd user units --------------------------------------------------------------
step "11. systemd user units"
if have systemctl && systemctl --user show-environment >/dev/null 2>&1; then
  for unit in blai-build.service blai-build.timer blai-telegram-bot.service; do
    if [ "$DRY" = 1 ]; then
      note "+ install $unit into $UNIT_DIR (repo $BLAI_REPO_DIR, venv $VENV)"
    else
      sed -e "s|%h/blai/repo|$BLAI_REPO_DIR|g" -e "s|%h/blai/venv|$VENV|g" "$REPO/build/systemd/$unit" > "$UNIT_DIR/$unit"
    fi
  done
  ok "units in $UNIT_DIR"
  run systemctl --user daemon-reload
  if run systemctl --user enable blai-build.timer blai-telegram-bot.service >/dev/null 2>&1; then ok "enabled blai-build.timer and blai-telegram-bot.service"; fi
  if [ -z "$EMPTY" ]; then
    if run systemctl --user start blai-build.timer && run systemctl --user restart blai-telegram-bot.service; then
      ok "started blai-build.timer and blai-telegram-bot.service"
    else
      fail "start failed; see: journalctl --user -u blai-telegram-bot.service -u blai-build.service"
    fi
  else
    note "not started: build/.env still has empty required values"
    todo "rerun bash build/install.sh after filling build/.env to start the timer and the bot"
  fi
  if [ "$DRY" = 1 ]; then
    note "+ loginctl enable-linger $USER"
  elif loginctl enable-linger "$USER" 2>/dev/null; then
    ok "linger enabled (units keep running without a login session)"
  elif [ "$HAVE_SUDO" = 1 ] && sudo loginctl enable-linger "$USER" 2>/dev/null; then
    ok "linger enabled via sudo"
  else
    todo "ask an admin to run: sudo loginctl enable-linger $USER (otherwise the units stop at logout)"
  fi
else
  note "systemctl --user is not usable in this shell (no user session bus)"
  todo "install the units by hand: cp build/systemd/* ~/.config/systemd/user/ && systemctl --user daemon-reload && systemctl --user enable --now blai-build.timer blai-telegram-bot.service"
fi

# -- 12. telegram chat id ----------------------------------------------------------------
step "12. Telegram chat id"
TOKEN="$(envval TELEGRAM_BOT_TOKEN)"; CHAT="$(envval TELEGRAM_CHAT_ID)"
if [ -n "$TOKEN" ] && [ -z "$CHAT" ]; then
  if [ "$DRY" = 1 ]; then
    note "+ GET https://api.telegram.org/bot<token>/getUpdates and list the chat ids seen"
  else
    IDS="$(curl -fsS --max-time 20 "https://api.telegram.org/bot$TOKEN/getUpdates" 2>/dev/null | python3 -c '
import json, sys
try:
    data = json.load(sys.stdin)
except Exception:
    data = {}
seen = []
for u in data.get("result", []):
    m = u.get("message") or u.get("edited_message") or u.get("channel_post") or (u.get("callback_query") or {}).get("message") or {}
    c = m.get("chat") or {}
    if c.get("id") is not None and c["id"] not in [s[0] for s in seen]:
        seen.append((c["id"], c.get("username") or c.get("title") or c.get("first_name") or ""))
for i, n in seen:
    print("%s %s" % (i, n))' 2>/dev/null)"
    if [ -n "$IDS" ]; then
      note "chat ids the bot has seen (id name):"
      printf '%s\n' "$IDS" | sed 's/^/      /'
      todo "set TELEGRAM_CHAT_ID in build/.env to your chat id from the list above, then rerun install.sh"
    else
      todo "send your bot any message in Telegram, then rerun install.sh to see the chat id (getUpdates was empty)"
    fi
  fi
elif [ -z "$TOKEN" ]; then
  note "TELEGRAM_BOT_TOKEN is empty; skipping (get one from @BotFather)"
else
  ok "TELEGRAM_CHAT_ID set"
fi

# -- checklist --------------------------------------------------------------------
step "Checklist"
printf '   Done:\n'
if [ "${#DONE[@]}" -gt 0 ]; then for d in "${DONE[@]}"; do printf '     [x] %s\n' "$d"; done; fi
printf '   Needs a human:\n'
if [ "${#TODO[@]}" -gt 0 ]; then for t in "${TODO[@]}"; do printf '     [ ] %s\n' "$t"; done; else printf '     nothing: the build agent is live\n'; fi
printf '\n   status:   systemctl --user status blai-build.timer blai-telegram-bot.service\n'
printf '   logs:     journalctl --user -u blai-build.service -f   (or build/logs/<date>.log)\n'
printf '   dry pass: %s/bin/python %s/build/build.py --once --dry-run\n' "$VENV" "$REPO"
exit "$HARD"
