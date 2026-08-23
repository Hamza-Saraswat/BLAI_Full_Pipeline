# Environment Template

Secrets never appear in any committed file. Two hosts hold them.

A local test run needs none of them. `python3 build/build.py --once --local` builds voice and render on a developer machine with an offline Kokoro voice, prints the Telegram card and the Blotato body instead of sending them, and skips git-sync, so nothing below has to exist before the first video is rendered. It checks paths, not keys. See `build/README.md`, "Local test run on a Mac".

## Cloud environment (claude.ai/code environment "Default")

Set these as environment variables on the cloud environment. Anyone with access to the environment can read them, so only low-risk keys go here.

```
FIRECRAWL_API_KEY=
YT_API_KEY=
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=blai-radar/1.0
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
GITHUB_TOKEN=
```

| Variable | Read by | How to get it |
|----------|---------|---------------|
| `GITHUB_TOKEN` (optional) | `skills/trend-radar/scripts/github_releases.py` | any fine-grained token with public read; raises the unauthenticated rate limit. The cloud session's git proxy handles pushes without it |
| `FIRECRAWL_API_KEY` | `.mcp.json` (FireCrawl MCP), `skills/trend-radar/scripts/firecrawl_search.py` | firecrawl.dev dashboard; reuse the v1 key |
| `YT_API_KEY` | `skills/trend-radar/scripts/youtube_recent.py`, `skills/youtube-keyword-research/scripts/competition.py`, `skills/youtube-analytics` | Google Cloud console: project, enable YouTube Data API v3, create an API key (no OAuth needed) |
| `REDDIT_*` | `skills/trend-radar/scripts/reddit.py` | reddit.com/prefs/apps: create a "script" app. Required in practice: Reddit's public `.json` endpoint answers 403 to cloud clients |
| `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` | `skills/telegram-gate/scripts/send_card.py` (morning FYI) | @BotFather for the token; send the bot a message, then `getUpdates` shows your chat id (`build/install.sh` prints it) |

## DGX Spark (`build/.env`, mode 600, owned by the `blai` user)

```
ELEVENLABS_API_KEY=
ELEVEN_VOICE_ID=
ELEVEN_MODEL_ID=eleven_multilingual_v2
ELEVEN_SEED=4242
BLOTATO_API_KEY=
BLOTATO_YOUTUBE_ACCOUNT_ID=
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
R2_ACCOUNT_ID=
R2_ACCESS_KEY_ID=
R2_SECRET_ACCESS_KEY=
R2_BUCKET=blai-previews
R2_PUBLIC_BASE_URL=
YT_API_KEY=
ROUTINE_RESCRIPT_URL=
ROUTINE_RESCRIPT_TOKEN=
BLAI_REPO_DIR=/srv/blai/repo
BLAI_BUILD_DIR=/srv/blai/builds
BLAI_PUBLISH_PRIVACY=private
```

| Variable | Read by | How to get it |
|----------|---------|---------------|
| `ELEVENLABS_API_KEY`, `ELEVEN_VOICE_ID` | `skills/elevenlabs-narration/scripts/generate_audio.py` | ElevenLabs Creator plan; the voice id of the trained Professional Voice Clone |
| `BLOTATO_API_KEY`, `BLOTATO_YOUTUBE_ACCOUNT_ID` | `skills/blotato-publish/scripts/publish.py` | Blotato settings > API; `GET /v2/users/me/accounts` lists the account id (`publish.py --accounts`) |
| `R2_*` | `skills/blotato-publish/scripts/r2.py` | Cloudflare dashboard: R2 bucket + API token with object read/write; enable the public bucket URL or a custom domain |
| `ROUTINE_RESCRIPT_*` | `skills/telegram-gate/scripts/bot.py` | the API trigger URL + token shown once when the produce routine's API trigger is created |
| `BLAI_PUBLISH_PRIVACY` | `publish.py` | keep `private` until the first test post is verified, then set `public` |

## What never goes into `.env`

Per-run creative content, slugs, titles, feedback. Those live in hub notes.

## Ignore rules to confirm

`.gitignore` contains `.env` and `.env.*`. `build/install.sh` creates `build/.env` from this file with empty values and refuses to start the build loop while required values are empty.
