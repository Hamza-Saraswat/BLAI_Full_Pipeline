# YouTube Automation Pipeline — Research Report

**Date:** 2026-08-22
**Scope:** A fully automated, human-review-gated content pipeline for one YouTube channel producing **long-form** (16:9, ~8–20 min) and **Shorts** (9:16, ≤3 min), triggered by a cloud routine/cron against a folder structure.
**Questions answered:** (1) how to post both formats headlessly — API, CLI, MCP, or third-party; (2) programmatic keyword research and codified posting best practices; (3) clone-your-own-voice vs. stock voice, ElevenLabs vs. alternatives, with real costs.

**Legend:** **[verified]** = fetched from the primary/official source on 2026-08-22 · *(secondary)* = from a dated third-party article where the official page was unreachable · *(unverified)* = could not be confirmed; treat as a hint and test it.

---

## 0. Executive summary

| Question | Answer |
|---|---|
| **How do I post long-form + Shorts automatically?** | Use the official **YouTube Data API v3** from a small Python upload service. There is no separate Shorts API — any square/vertical video ≤3 min is auto-classified as a Short. Default quota is now **100 uploads/day** (the "6 uploads/day" figure everywhere online is obsolete). The single real obstacle is that **videos uploaded from an un-audited Google Cloud project are locked private** until you pass YouTube's compliance audit (4–14 days reported; plan for 2–4 weeks). Bridge the gap — and keep as permanent fallback — with **Upload-Post** ($24/mo, free tier 10 uploads/mo) or **Zernio** (free ≤2 accounts), which use their own audited Google app. No first-party Google or claude.ai YouTube MCP/connector exists; local MCP servers and CLIs all reuse your own GCP project and therefore don't avoid the lock. |
| **Is there a good API/MCP for SEO & keyword research?** | Yes — **vidIQ ships an official remote MCP server** (`https://mcp.vidiq.com/mcp`) with YouTube-native keyword volume/competition, trending, competitor analysis, and title/thumbnail scoring; free during launch, $19/mo Boost after. Combine with the free YouTube autocomplete endpoint, the Data API (`search.list` own 100/day bucket, new cheap `videos.batchGetStats`), and the Analytics API's search-terms report for your own channel. TubeBuddy has no API; Ahrefs/Semrush have no YouTube endpoints; `pytrends` is dead; Google's official Trends API is still an allow-listed alpha. Posting best practices are codified in §2.9 as rules an LLM can follow, with a 0–100 scoring rubric in §2.7. |
| **Clone my voice or use a stock voice? Is ElevenLabs the most expensive?** | **Clone your own voice** (ElevenLabs Professional Voice Clone from 60–120 min of clean recording). YouTube's disclosure policy explicitly exempts own-voice clones; you own the recordings (PlayAI deleted all customer clones when it shut down Dec 31 2025); a real voice is "authentic creator" evidence under the YPP policy. ElevenLabs is top-band per character but **no longer an outlier** after a May 2026 price cut ($0.10/1k chars v2/v3, $0.05/1k Flash). At your volume it's **≈ $22–30/mo** (Creator plan) — the cost is the plan tier PVC requires, not characters. **Cartesia** Sonic-3.6 (current arena #1, $49 flat with PVC) is the strongest alternative; **Inworld TTS-2** (~$4–13/mo, instant clone) is the cheap fallback; self-hosting isn't worth it below ~50 h/month. |
| **Total monthly cost** | **≈ $25–60/mo** base (voice $22–30, publishing $0–24, keyword $0–19, STT QA ~$1); **≈ $80–150/mo** at 3× volume. |
| **Biggest risk** | YouTube's **"inauthentic content"** YPP policy (July 15 2025, tightened July 2026) demonetizes templated, mass-produced AI content and AI personas posing as human experts. The human review gate and genuinely distinct per-video insight are the defense (§4). |

**Things that contradict common knowledge (all verified):**
1. Upload quota: `videos.insert` cost fell from ~1,600 to ~100 units (Dec 4 2025) and moved into its own bucket of 100 calls/day (June 1 2026).
2. Shorts can be up to 3 minutes (since Oct 15 2024); `#Shorts` is not required.
3. The AI-disclosure flag is settable via API (`status.containsSyntheticMedia`), and cloning your own voice does **not** require disclosure.
4. Hashtag spam threshold is now >60 (not >15).
5. ElevenLabs API pricing dropped up to 55% on May 7 2026; Creator now includes 121k credits, Pro 600k.
6. Custom thumbnails for Shorts exist as of July 25 2026 (YPP + desktop Studio only; API support unverified).

---

## 1. Posting to YouTube automatically

### 1.1 Verified facts about the YouTube Data API v3 **[verified]**

| Fact | Detail | Source |
|---|---|---|
| **Quota model (changed)** | Dec 4 2025: upload cost ~1,600 → ~100 units. June 1 2026: `videos.insert` and `search.list` charged to **their own buckets — 100 calls/day each**; 10,000 units/day for everything else. Resets midnight PT. | [Revision history](https://developers.google.com/youtube/v3/revision_history) · [Quota costs](https://developers.google.com/youtube/v3/determine_quota_cost) · [Getting started](https://developers.google.com/youtube/v3/getting-started) |
| Other costs | `videos.update` 50 · `thumbnails.set` 50 · `playlistItems.insert` 50 · `captions.insert` 400 · `commentThreads.insert` 50 · `videos.list` 1 · `channels.list` 1 · `videos.batchGetStats` 1 (own 10k bucket, 50 IDs/call, added June 3 2026) | same |
| **Un-audited project lock** | "All videos uploaded via the `videos.insert` endpoint from unverified API projects created after 28 July 2020 will be restricted to private viewing mode. To lift this restriction, each project must undergo an audit." No later revision repeals it. Locked videos **cannot be appealed** — re-upload via an audited client. | [Revision history 2020-07-28](https://developers.google.com/youtube/v3/revision_history) · [Help 7300965](https://support.google.com/youtube/answer/7300965) |
| Scheduling | `status.publishAt` (ISO 8601) "can be set only if the privacy status of the video is private" and "the video has never been published"; on `videos.update` you must re-send `privacyStatus=private`; a past date publishes immediately. No rounding documented *(unverified)*. | [videos resource](https://developers.google.com/youtube/v3/docs/videos) |
| AI disclosure | `status.containsSyntheticMedia` (bool) settable on insert/update (added Oct 30 2024). | same |
| Other settable status | `selfDeclaredMadeForKids`, `license` (`youtube`/`creativeCommon`), `embeddable`, `publicStatsViewable`; `recordingDetails.recordingDate`; `snippet.categoryId`, `defaultLanguage`, `localizations`; query param `notifySubscribers` (default **true**). `paidProductPlacementDetails.hasPaidProductPlacement` is on the resource/insert parts but absent from update's settable list *(partially verified)*. | same · [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) |
| Limits | Title ≤100 chars (no `<` `>`); description ≤5,000 **bytes** (multibyte counts); tags ≤500 chars total incl. commas/quotes. File ≤256 GB / 12 h. | same · [Help 71673](https://support.google.com/youtube/answer/71673) |
| **Shorts** | No separate API, no `isShort` field ([open request](https://issuetracker.google.com/issues/464519393)). Uploaded on/after Oct 15 2024, **square or vertical, ≤3 min → Short**; use 16:9 to avoid. `#Shorts` optional. Licensed music in Shorts capped at 90 s (some tracks 60/30 s). 3:01 vertical = long-form; 16:9 ≤3 min = long-form. | [Help 15424877](https://support.google.com/youtube/answer/15424877) · [Help 12779649](https://support.google.com/youtube/answer/12779649) |
| Thumbnails | `thumbnails.set`: 2 MB max, JPEG/PNG; requires a **phone-verified** channel; errors `forbidden (403)`, `uploadRateLimitExceeded (429)`. | [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set) · [Help 72431](https://support.google.com/youtube/answer/72431) |
| Captions | `captions.insert`: 400 units, requires scope `youtube.force-ssl`, 100 MB, needs `snippet.videoId/language/name`. | [captions.insert](https://developers.google.com/youtube/v3/docs/captions/insert) |
| Chapters | Description text only: first timestamp `00:00`, ≥3 timestamps ascending, each ≥10 s; unavailable during active strikes. | [Help 9884579](https://support.google.com/youtube/answer/9884579) |
| Resumable upload | POST with `X-Upload-Content-Length` → `Location` session URI → PUT chunks (multiples of 256 KB except last); `308 Resume Incomplete` + `Range` to resume; backoff on 5xx. | [Resumable guide](https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol) |
| Un-verified channel caps | No phone verification → 15-minute max length, no custom thumbnails. | [Help 71673](https://support.google.com/youtube/answer/71673) |

**Weekly quota budget for ~2 long-form + 7 Shorts:** 9 upload-bucket calls (of 700) + ~450 thumbnails + ~450 playlist adds + up to 3,600 captions ≈ 4,500 of 70,000 general units. Quota is a non-issue; only `captions.insert` (25/day max) could ever bite.

### 1.2 The compliance audit — two processes people confuse

| | OAuth app verification (Cloud Console) | **YouTube API Services compliance audit** |
|---|---|---|
| Who reviews | Google Trust & Safety | YouTube API team |
| Required? | **No** for a personal-use app with <100 users ([when not needed](https://support.google.com/cloud/answer/13464323)); users just see an "unverified app" interstitial | **Yes — this is what unlocks public uploads** |
| How | Cloud Console | [Audit & Quota Extension form](https://support.google.com/youtube/contact/yt_api_form) — applicant type **individual** or organization; use case "video uploading"; needs HTTPS website + HTTPS privacy-policy URL, GCP project number, endpoints used, screenshots/recording of consent + upload |
| Timeline | 3–5 business days if you do it | No commitment stated. Reported: 4 days and 7–14 days for "personal use, own channel" applicants; older reports 2–4 weeks or longer ([porjo/youtubeuploader #86](https://github.com/porjo/youtubeuploader/issues/86), [Postproxy](https://postproxy.dev/blog/youtube-upload-api-guide/)). Periodic re-audits. |

- Your use case is explicitly approved by the [developer policies](https://developers.google.com/youtube/terms/developer-policies): "Promoting your own business or artistic enterprise by uploading original audiovisual content to YouTube or maintaining channel(s) on YouTube."
- **No single-owner workaround:** "Internal" consent type requires a Google Workspace org; the lock is per API project regardless of audience. Community anecdotes about flipping locked videos public are contradicted by Google's no-appeal statement — don't build on them.
- YouTube scopes appear to be "sensitive" rather than "restricted" (no security assessment needed) — inferred from Google's [verification requirements](https://support.google.com/cloud/answer/13464321), not stated verbatim.

### 1.3 OAuth 2.0 for a headless server **[verified]**

- **The 7-day trap:** an External consent screen in **"Testing"** status issues refresh tokens that expire after 7 days ([OAuth2 docs](https://developers.google.com/identity/protocols/oauth2#expiration), [App audience](https://support.google.com/cloud/answer/15549945)).
- **Fix:** Cloud Console → OAuth consent → **Publish app → "In production"** without submitting for verification. Tokens then persist. Other expiry causes: 6 months unused; user revocation; **100 refresh tokens per account per client ID** (oldest silently invalidated).
- **Scopes:** `videos.insert` accepts `youtube.upload`/`youtube`/`youtube.force-ssl`/`youtubepartner`; `thumbnails.set` accepts the first three; `captions.insert` **requires** `youtube.force-ssl`. Practical minimum: **`youtube.force-ssl` alone**.
- Do the consent once on a laptop, store the refresh token in your secrets manager, copy to the server. If the channel is a **Brand Account**, choose it on the account chooser or uploads land on your personal channel.

### 1.4 Client libraries

- **Python `google-api-python-client`:** `MediaFileUpload(path, chunksize=…, resumable=True)` + `next_chunk()` loop ([media docs](https://googleapis.github.io/google-api-python-client/docs/media.html)); official sample `upload_video.py` retries 500/502/503/504 with exponential backoff ([sample](https://github.com/youtube/api-samples/blob/master/python/upload_video.py); repo archived Aug 2025 but the code is valid). **Recommended.**
- **Node `googleapis`:** streams `media.body` with progress, but **no resumable pause/resume API** (open since 2014, [#276](https://github.com/googleapis/google-api-nodejs-client/issues/276)) and a "first upload never processes" report ([#3566](https://github.com/googleapis/google-api-nodejs-client/issues/3566)).

### 1.5 CLIs

| Tool | Lang · stars · last push | Schedule | Thumb | Playlist | Captions | AI flag | Headless OAuth | Verdict |
|---|---|---|---|---|---|---|---|---|
| [porjo/youtubeuploader](https://github.com/porjo/youtubeuploader) | Go · 885★ · 2026-08-07 | ✔ `-metaJSON` (`publishAt`) | ✔ | ✔ | ✔ | ✔ `containsSyntheticMedia` | ✔ generate token locally, copy to server | **Best maintained CLI.** Resumable, `-chunksize`, `-ratelimit`. README's "~6 videos/24h" note is stale. |
| [tokland/youtube-upload](https://github.com/tokland/youtube-upload) | Python · 2,191★ · 2024-04-25 | ✔ | ✔ | ✔ | — | — | token file | Effectively dead (Py2 era). |
| [faborsky/youtube-cli-app](https://github.com/faborsky/youtube-cli-app) | Python · 5★ · 2026-08-18 | ✔ | ✔ | ✔ | — | — | token file | Young, solo-maintained. |
| [fix2015/youtube-publish](https://github.com/fix2015/youtube-publish) | npm · 2★ · 2026-04 | ✔ bulk | — | ✔ | — | — | browser once | Hobby project. |
| [davidmosiah/youtube-shorts-agent](https://github.com/davidmosiah/youtube-shorts-agent) | JS CLI+MCP · 1★ · 2026-08-15 | — | — | — | — | ✔ | PKCE | Shorts-only, dry-run focus. |

All CLIs use **your** GCP project → the private lock applies until audited.

### 1.6 MCP servers that can upload

Directory sweep (official MCP registry, Smithery, Glama, PulseMCP, mcp.so): 51 "youtube" entries in the official registry, 3 upload-capable. **claude.ai has no YouTube connector; Google ships official MCPs for Ads/Analytics but not YouTube** ([Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)).

| Server | Stars · last push | Upload | Schedule | Thumb | Playlist | Captions | Notes |
|---|---|---|---|---|---|---|---|
| [anwerj/youtube-uploader-mcp](https://github.com/anwerj/youtube-uploader-mcp) (Go) | 51★ · 2026-07-12 | ✔ | ✔ | ✔ <2 MB | ✔ | ✔ | Most complete local one; auto-refreshes tokens; your GCP project. |
| [mrchevyceleb/youtube-mcp](https://github.com/mrchevyceleb/youtube-mcp) (TS) | 2★ · 2026-08-14 | ✔ resumable | ✗ | ✔ | ✔ | ✔ | 22 tools. |
| [brentwpeterson/mcp-youtube](https://github.com/brentwpeterson/mcp-youtube) (Py) | 1★ · 2026-08-14 | ✔ | ? | ? | ✔ | ✔ | Brand-account guard. |
| [i1s-abhishek/youtube-studio-mcp](https://github.com/i1s-abhishek/youtube-studio-mcp) | 13★ · 2026-04-20 | **✗** | ✗ | ✔ | ✗ | ✗ | Metadata/analytics only. |
| [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) | 566★ · 2026-08-08 | **✗ read-only** | — | — | — | — | Research only (§2.2). |
| Harper Labs "YouTube Studio MCP" (hosted, OAuth, free) | released 2026-05-25; repo 404 | ✔ | ? | ✔ | ✔ | ✔ | In official registry; **whether it uses an audited Google app is unverified.** |
| [Blotato hosted MCP](https://help.blotato.com/api/mcp) | commercial | ✔ | ✔ | ✔ URL | ✔ | — | Uses Blotato's audited app; Starter $29 incl. API. |
| [Post Bridge agent-mode](https://github.com/post-bridge-hq/agent-mode) | 15★ · 2026-08-20 | ✔ Shorts only | ✔ | ✔ | — | — | $5/mo API add-on; **5-min video cap**. |
| Metricool MCP | — | ✔ | ✔ | ? | ✔ | — | Advanced plan $67+/mo. |

For a cron pipeline an MCP adds nothing over a direct client; only the *hosted* ones help, because they bring an audited Google app.

### 1.7 Third-party posting APIs / schedulers

"Own app" = the vendor's audited Google app → no GCP project, no audit, no private lock for you.

| Service | 2026 price | Own app | Long-form | Shorts | Schedule | Thumbnail | AI flag / kids | Media input | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **[Upload-Post](https://www.upload-post.com)** | Free 10 uploads/mo (2 profiles); **Basic $24/mo ($16 annual)** unlimited, 5 profiles; Pro $50; Advanced $147 | ✔ | ✔ 256 GB | ✔ | ✔ `scheduled_date` + `timezone` | ✔ file or URL | ✔ `containsSyntheticMedia`, `selfDeclaredMadeForKids`, `license`, `embeddable`, `defaultLanguage`, playlist, subtitles | **multipart file** or URL | Fullest YouTube param map ([docs](https://docs.upload-post.com/api/upload-video.md)). **`privacyStatus` defaults to public — always send it.** Shorts how-to still says 60 s (stale). |
| **[Zernio](https://zernio.com)** (ex-Late / getlate.dev) | **1–2 accounts free**; 3–10 $6/acct; 11–100 $3/acct ([pricing](https://zernio.com/pricing)) | ✔ | ✔ 256 GB | ✔ auto ≤3 min | ✔ `scheduledFor` | ✔ URL (not Shorts) | ✔ AI flag, kids, `categoryId`, `playlistId` | public URL | No `tags`/`notifySubscribers` ([YouTube guide](https://docs.zernio.com/platforms/youtube)). |
| [Ayrshare](https://www.ayrshare.com/pricing/) | Premium **$149** (1 profile), Launch $299, Business $599; 28-day trial, no free plan | ✔ | ✔ 4 GB | ✔ `shorts:true` (adds #shorts) | ✔ | ✔ URL <2 MB | ✔ incl. `notifySubscribers`, subtitles | public URL | Most mature; overpriced for one channel. |
| [Blotato](https://www.blotato.com/pricing) | Starter **$29** (20 accounts, API + hosted MCP), Creator $97 | ✔ | ✔ | ✔ | ✔ | ✔ `thumbnailUrl` | ✔; **no tags** | public URL | Cross-posts Shorts to TikTok/Reels in the same call. |
| [Post Bridge](https://www.post-bridge.com/pricing) | $29/$49/$99 + **$5 API add-on** | ✔ | **✗ 300 s / 500 MB cap** | ✔ | ✔ | ✔ | ? | local/URL | Shorts-only for you. |
| [Metricool](https://metricool.com/pricing/) | Free; Starter $25; **Advanced $67+** for API/MCP | ✔ | ✔ | ✔ | ✔ | ? | ? | — | UI-first; API docs are a PDF. |
| [Buffer](https://buffer.com/resources/buffer-api-is-here/) (new GraphQL API) | API on every plan incl. Free | ✔ | ✔ | ? | ✔ `dueAt` | **✗ no thumbnail** | ✔ `isAiGenerated`, kids, `notifySubscribers`, license, category | **public URL only** | Not enough without thumbnails. |
| [Publer](https://publer.com/help/en/article/how-to-access-the-publer-api-1w08edo/) | API on Business (~$10–21 base + $7/extra account *(secondary)*) | ✔ | ✔ <2 GB | ✔ ≤3 min | ✔ | ✔ | ? | — | |
| Hootsuite | Enterprise only | ✔ | ✔ | ? | ✔ | ? | ? | — | Not self-serve. |
| SocialBee | $29–449 | — | UI only | — | — | — | — | — | **No public API**. |
| Zapier YouTube app | per plan; trial 5 uploads/24 h | ✔ | **~100 MB / 180 s limit** | — | ✗ | ✗ | ✗ | URL | Docs still cite 1,600 units. |
| Make "Upload a Video" | per plan | ✔ (optional own client) | >1 GB problematic | — | ✔ | ✗ | ? | data/URL | Thin docs. |
| **n8n YouTube node** | self-host free | **✗ n8n Cloud's shared Google OAuth is blocked for YouTube** ([#18693](https://github.com/n8n-io/n8n/issues/18693), closed "not planned") → bring your own GCP client → private lock | multi-GB uploads hang ([community](https://community.n8n.io/t/large-file-youtube-upload/65854)) | ✔ | ✔ `publishAt` | **✗ no thumbnail, no playlist** | ✔ kids, license, embeddable, `notifySubscribers`, recording date | binary | Use an HTTP Request node → Upload-Post or your Python service instead. |
| Postiz (AGPL) / Mixpost Pro | ~$29 cloud / $299 one-time *(secondary)* | **✗ self-host needs your own Google project** | ✔ | ✔ | ✔ | ✔ | ? | — | Same private-lock problem as DIY. |

### 1.8 Practical gotchas (2025–2026)

1. **Stale quota folklore** — blogs, Zapier docs and porjo's README still say 1,600 units / 6 uploads a day. Current: 100 uploads/day in a dedicated bucket.
2. **Private lock** — no appeal; re-upload required (§1.2).
3. **`uploadLimitExceeded` (400)** — a **per-channel** daily cap, separate from API quota: "we limit how many videos a channel can upload in a 24-hour period across desktop, mobile, and YouTube API… limits may vary by country/region or channel history" — number unpublished ([Help 10383400](https://support.google.com/youtube/answer/10383400)). Community estimates 10–20/day for new channels *(unverified)*. Your ~9/week is far below any of these.
4. **Phone-verify first** — else 15-min max length and no custom thumbnails.
5. **Shorts classification has no API confirmation** — verify via `videos.list` `contentDetails.duration` + your known aspect ratio. Shorts thumbnails via API: *unverified, assume no*.
6. **`publishAt` rules** — private only, never-published only, past = immediate, re-send `privacyStatus=private` on update, blocked during strike penalties; no documented rounding. One Jan 2026 forum report of a scheduled time silently shifting went unexplained ([discuss.google.dev](https://discuss.google.dev/t/when-using-the-youtube-api-to-publish-a-video-scheduled-for-a-specific-release-time-the-videos-scheduled-release-time-will-be-moved-forward-after-publication/320829)).
7. **Limits** — title 100 chars, description 5,000 bytes (UTF-8), tags 500 chars incl. commas.
8. **Refresh tokens** — 7 days in Testing; 6-month inactivity; 100-token cap per client.
9. **`notifySubscribers` defaults to true** — several Shorts a week will spam the bell; set `false` on Shorts.
10. **Made-for-kids is effectively irreversible in side effects** (comments, notifications, personalized ads, end screens disabled) — default `false`.
11. **Brand Account mis-targeting** at consent time.
12. **Processing lag** — Shorts typically 1–3 min before playable; poll `videos.list` `status.uploadStatus` / `processingDetails` before `thumbnails.set`.
13. **Node client lacks resumable pause/resume** — use Python or the raw protocol.
14. **Audit maintenance** — periodic re-audits; anecdotal need to keep uploading to retain status.

### 1.9 Recommendation for posting

**Primary: direct Data API from a small Python upload service, own GCP project, audit submitted on day one. Bridge & permanent fallback: Upload-Post.**

1. **Channel prep:** phone-verify at youtube.com/verify. Note whether it's a Brand Account.
2. **GCP:** new project → enable YouTube Data API v3 → OAuth consent *External* → scope `youtube.force-ssl` → **Publish app ("In production"), do not submit for verification** → Desktop OAuth client → one-time consent on a laptop (click through "unverified app") → store refresh token in secrets manager.
3. **Submit the audit form** as an individual, use case "video uploading", own channel. Needs a one-page HTTPS site + privacy policy + short screen recording of consent + upload. Ask for default quota (you don't need more). Until approval, route uploads through Upload-Post.
4. **Upload job per manifest item:** `videos.insert` resumable (`chunksize` 8–16 MB), `part=snippet,status,recordingDetails`; body: `snippet.title/description (with 00:00 chapters)/tags/categoryId/defaultLanguage`, `status.privacyStatus="private"`, **no `publishAt` yet**, `status.selfDeclaredMadeForKids=false`, `status.containsSyntheticMedia` from manifest, `status.license`; query `notifySubscribers=false` for Shorts. Persist session URI + video ID immediately (idempotency); retry 5xx/429 with backoff; on `uploadLimitExceeded` sleep to next day. Poll `videos.list` until `uploadStatus=processed`, then `thumbnails.set` (long-form), `playlistItems.insert`, `captions.insert` (SRT).
5. **Review gate:** reviewer approves → `videos.update` with `status.privacyStatus="private"` **and** `status.publishAt`. Validate client-side: title ≤100, description ≤5,000 bytes, tags ≤500 chars, chapters (00:00 first, ≥3, ≥10 s), Shorts = square/vertical and ≤180 s.
6. If you'd rather not write the client, wrap [porjo/youtubeuploader](https://github.com/porjo/youtubeuploader) (`-metaJSON` carries `publishAt` and `containsSyntheticMedia`) — same GCP/audit requirements.

**Fallbacks:** Upload-Post (Basic $24/mo; multipart file upload; full param map; send `privacyStatus` explicitly) · Zernio (free ≤2 accounts; needs a stable public MP4 URL on R2/S3; no tags) · Blotato ($29) only if you also want Shorts cross-posted to TikTok/Reels.
**Avoid:** Post Bridge (5-min cap), Zapier (100 MB/180 s), n8n Cloud's built-in YouTube credential (blocked), self-hosted n8n/Postiz/local MCPs as a way to *avoid* the audit (they can't), Ayrshare for one channel ($149), tokland/youtube-upload (dead).

---

## 2. Keyword research & posting best practices

### 2.1 Keyword-research tools — programmatic access

| Tool | YouTube-relevant output | API? | MCP? | Price (2026) | Verdict |
|---|---|---|---|---|---|
| **vidIQ** | Keyword volume + competition, trending videos (views/hr), channel & competitor analytics, outlier scores, title/thumbnail scoring, transcripts, comment themes | No public REST API *(unverified)* | **Official remote MCP** `https://mcp.vidiq.com/mcp` (OAuth) — [vidiq.com/mcp](https://vidiq.com/mcp/), [help](https://support.vidiq.com/en/articles/15082430-vidiq-mcp) | Free 150 credits/mo; Boost $19/mo (2,000 credits); Max $49/mo (6,000) ([plans](https://vidiq.com/plans/)). 5 credits/call; MCP free on all plans during launch | **Primary demand source.** YouTube-native data; doesn't consume your Data API quota. |
| **TubeBuddy** | Keyword Explorer, SEO Studio (browser extension) | **No public API** | No | Pro ~$12/mo, Legend ~$26/mo *(secondary)* | Not usable headless. |
| **Ahrefs** | YouTube mode in Keywords Explorer UI | API v3 on Lite+, **no YouTube endpoint** | Ahrefs MCP (shares units) | $129–$1,499/mo ([API v3](https://help.ahrefs.com/en/articles/6559232-about-api-v3)) | Overkill; skip. |
| **Semrush** | "Keyword Analytics for YouTube" app | Main API needs Business ($549/mo) + units; YouTube app has PDF export only | No | App $10/mo ([KB](https://www.semrush.com/kb/1362-keyword-analytics-for-youtube)) | Not viable programmatically. |
| **Keywords Everywhere** | Google volume; extension shows YouTube volume | API exists but **no YouTube endpoint** | No | 200k credits $80, 500k $150 ([credits](https://keywordseverywhere.com/credits.html)) | Cheap Google-volume fallback only. |
| **keywordtool.io** | YouTube autocomplete ideas + estimated YouTube volume | Yes (`/v2/search/volume/youtube`) | No | Starter $88/mo (50 req/day) … Agency $788 ([API](https://keywordtool.io/api)) | One of few with a YouTube-volume API; expensive. |
| **DataForSEO** | YouTube SERP (organic, video info, subtitles, comments); Google Trends incl. **YouTube property**; Ads volume | Yes, pay-as-you-go | 3rd-party MCPs | YouTube SERP $0.0006 std / $0.0012 priority / $0.002 live per request ([pricing](https://dataforseo.com/pricing/serp/youtube-serp-api)); Trends $0.0027 std / $0.011 live per task ([pricing](https://dataforseo.com/pricing/keywords-data/google-trends)) | Best cost for bulk SERP + Trends. |
| **SerpApi** | YouTube Search API; Google Trends with `gprop=youtube` | Yes | No | Free 250/mo; Starter $25 (1k); Developer $75; Production $150 ([pricing](https://serpapi.com/pricing)) | Simplest; ~10× DataForSEO's price. |
| **Apify** | Scraper actors: search, channel videos incl. Shorts, trending, comments, transcripts | Yes | Apify MCP exists | Platform free $5 credit; `apidojo/youtube-scraper` $0.50/1k videos ([page](https://apify.com/apidojo/youtube-scraper)) | Bypasses search quota; scraping is ToS-grey. |
| **Google Trends official API** | Relative interest, 1,800 days, removes 5-term compare limit | Alpha, **application-gated** (announced July 24 2025; still allow-listed July 2026) | — | Free | Apply; YouTube-property filter not mentioned *(unverified)*. [Announcement](https://developers.google.com/search/blog/2025/07/trends-api) |
| `pytrends` | — | **Archived Apr 17 2025**; 429s | — | — | Dead. |
| **trendsmcp** | Trends-style series incl. `youtube` source | REST + Python | Yes | Free 100 req/mo | New (0★); [repo](https://github.com/trendsmcp/google-search-trends-api). |
| **YouTube autocomplete** | 10 suggestions/seed, locale-aware | Undocumented GET `https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=…` (JSON); `client=youtube` → JSONP | — | Free | Working July 20 2026 (40/40 HTTP 200, [ChocoData](https://github.com/ChocoData-com/youtube-suggest-scraper)). Pass `hl`/`gl`. ToS-grey but universal. |
| **YouTube Data API v3** | `search.list`, `videos.list`, `videos.batchGetStats`, `channels.list` | Official | many wrappers | Free (quota in §1.1) | Core. |
| **YouTube Analytics & Reporting API** | Own channel: traffic sources, **search terms** (`insightTrafficSourceDetail` filtered by `insightTrafficSourceType==YT_SEARCH`), retention curve (`elapsedVideoTimeRatio`), day/country/device | Official ([dimensions](https://developers.google.com/youtube/analytics/dimensions)) | — | Free | **No hour-of-day dimension** → "When your viewers are on YouTube" is Studio-only. |
| YouTube Studio Research / Inspiration tab | "Your viewers' searches", content gaps; Aug 2026 test adds outlier multipliers | **No API/export** | — | Free | Human reviewer uses it manually ([Tubefilter Aug 2026](https://www.tubefilter.com/2026/08/05/youtube-research-tab-outlier-multipliers-viewer-comparison-data/)). |
| Social Blade | Channel stats history | Paid API, prepaid credits; price behind login | No | — | Marginal vs `channels.list`. |
| Morningfame / 1of10 / ViewStats | Keyword tool / outlier discovery | No API | No | $348–480/yr | Skip. |
| TubeLab | Outlier finder, title formulas | REST (vendor claim) | No | $178.80/yr | Vendor marketing; unproven. |
| NoxInfluencer | Influencer DB | Enterprise API | No | ~$1,499/quarter | Not for a solo channel. |
| Rapidtags / Tagstat | Tag generators | unofficial wrappers only | No | free-ish | An LLM generates tags better. |

### 2.2 MCP servers for YouTube research (none of these upload)

| Server | Stars | Tools | Needs key? | Notes |
|---|---|---|---|---|
| [vidIQ MCP](https://vidiq.com/mcp/) (official, remote) | n/a | keyword research, trending, competitor/outlier analysis, title/thumbnail scoring, transcripts, comment themes | vidIQ account | Best YouTube-native demand data. |
| [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) | 566 | video details, search, transcripts, channel stats, playlists, advanced search | Data API key | MIT; npm/Smithery/Docker. |
| [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 583 | transcripts (Shorts OK) | No | MIT. |
| [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | 543 | subtitles via yt-dlp | No (yt-dlp) | |
| [icraft2170/youtube-data-mcp-server](https://github.com/icraft2170/youtube-data-mcp-server) | 65 | search, trending by region, channel stats, engagement, transcripts | Yes | MIT. |
| [wynandw87/claude-code-youtube-mcp](https://github.com/wynandw87/claude-code-youtube-mcp) | 7 | 15 tools incl. keyless transcripts, most-replayed heatmap, chapters | partly | Young. |
| [labeveryday/youtube-mcp-server-enhanced](https://github.com/labeveryday/youtube-mcp-server-enhanced) | 6 | metrics/transcripts via yt-dlp | No | ToS-grey scraping. |
| Google Trends MCPs: [trendsmcp](https://github.com/trendsmcp/google-search-trends-api), [andrewlwn77/google-trends-mcp](https://github.com/andrewlwn77/google-trends-mcp), [cryptoken/GoogleTrendsMCP](https://github.com/cryptoken/GoogleTrendsMCP) | low | compare keywords, trending, related queries | varies | Anything built on pytrends is broken. |

Directories to watch: [Smithery](https://smithery.ai/servers/youtube), [PulseMCP](https://www.pulsemcp.com/servers), [Glama](https://glama.ai/mcp/servers).

### 2.3 Open-source libraries

| Library | Status (Aug 2026) | Use | Risk |
|---|---|---|---|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Active | `yt-dlp "ytsearch50:query" --flat-playlist --dump-json --skip-download` = search without quota; `ytsearchdate:` | Datacenter IPs hit "Sign in to confirm you're not a bot"; needs cookies/residential proxy + JS runtime; **ToS-grey**. |
| [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) | 8.1k★, active | competitor transcripts | Cloud IPs blocked; docs recommend rotating residential proxies (~$5–10/mo). |
| [scrapetube](https://github.com/dermasmid/scrapetube) | 523★, 27 open issues | channel videos/search without key | Maintenance uncertain. |
| youtube-search-python | **Archived June 2022** | — | Don't use. |
| pytrends | **Archived Apr 2025** | — | Don't use. |

### 2.4 What you can derive from the official APIs (no scraping)

- **Competition for a keyword:** `search.list(q, type=video, order=relevance|viewCount, publishedAfter, videoDuration=short|medium|long, regionCode, relevanceLanguage)` → top 20–50 IDs (1 call from the 100/day bucket) → `videos.batchGetStats` (1 unit) for views/likes/comments/duration/publish date → `channels.list` (1 unit) for subscribers. Compute: median views, median channel size, share <6 months old, share that are Shorts, exact-phrase-in-title rate.
- **View velocity:** views ÷ days since `publishedAt`, re-sampled daily via `batchGetStats` (50 IDs/call).
- **Demand proxies:** autocomplete expansion depth (`q`, `q a…z`, `how to q`, `q 2026`), vidIQ volume/competition, Trends-YouTube interest (SerpApi `gprop=youtube` / DataForSEO / trendsmcp).
- **Own channel:** weekly Analytics pull of `YT_SEARCH` terms (low-volume terms suppressed), traffic-source mix (`SUBSCRIBER`, `RELATED_VIDEO`, `SHORTS`, `YT_SEARCH`, `EXT_URL`…), retention curve, views by day/country → feeds next week's keyword candidates and the timing experiment.
- **Not available by API:** Research/Inspiration tab, hourly audience heatmap, outlier multiplier.

### 2.5 Posting best practices (2025–2026), with sources

**Titles** — hard limit 100 chars; ~50–60 visible in search/feeds, ~40 in the mobile Shorts feed *(secondary)*. YouTube's own guidance ([title & thumbnail tips](https://support.google.com/youtube/answer/12340300)): be accurate (mismatch hurts discoverability); be succinct — important words first, episode numbers/branding last; limit ALL CAPS and emoji; two title types — **searchable** (states the topic) vs **intriguing** (curiosity for browse); check CTR by surface in the first 24 h. Pick 1–2 main keywords and use them in both title and description ([description tips](https://support.google.com/youtube/answer/12948449)). The recommendation system's signals are post-click: clicks, watch time, survey responses, shares/likes/dislikes; "recommendations drive a significant amount of the overall viewership… even more than channel subscriptions or search" ([YouTube blog](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)). YouTube's clickbait tell: high CTR + low AVD + fewer impressions ([CTR FAQ](https://support.google.com/youtube/answer/7628154)). Paddy Galloway (third-party): titles <50–60 chars, simple universal words, title + thumbnail complement rather than repeat.

**Descriptions** — ≤5,000 bytes; first ~150 chars show above "Show more". Unique per video; 1–2 keywords prominently; chapters; playlist/channel links; verify the search terms from "How viewers find your videos" appear in the text ([12948449](https://support.google.com/youtube/answer/12948449)).

**Tags** — "minimal role in your video's discovery"; useful for misspellings; misleading tags violate spam policy ([tags](https://support.google.com/youtube/answer/146402)). ≤500 chars total.

**Hashtags** — up to 3 shown above the title; **>60 hashtags → all ignored** (many blogs still say 15); no spaces; must relate to content ([hashtags](https://support.google.com/youtube/answer/6390658)).

**Chapters** — `00:00` first, ≥3, ≥10 s each, ascending; manual list overrides auto-chapters ([chapters](https://support.google.com/youtube/answer/9884579)).

**Thumbnails** — 16:9 up to 3840×2160 (min width 640), 9:16 for Shorts; JPG/PNG; 2 MB on mobile / 50 MB desktop; phone-verified account; Shorts custom thumbnails desktop-Studio only ([thumbnails](https://support.google.com/youtube/answer/72431)). Keep ≥1280×720 and ≤2 MB for `thumbnails.set`. 90% of best-performing videos use custom thumbnails; rule of thirds; readable text; design for small screens ([12340300](https://support.google.com/youtube/answer/12340300)). Galloway: ≤3 focus areas, <5 words, glance test, 3 genuinely different variants. **Test & Compare:** up to 3 variants; winner by **watch-time share**, not CTR; desktop-only; excludes Shorts, made-for-kids, private; ~2 weeks; editing title/thumbnail cancels the test; **no API** ([A/B help](https://support.google.com/youtube/answer/13861714)).

**Shorts** — square/vertical ≤3 min → Short ([15424877](https://support.google.com/youtube/answer/15424877)); title ≤100 ([Shorts basics](https://support.google.com/youtube/answer/10059070)); no `#Shorts` needed. **Custom Shorts thumbnails** launched July 24–25 2026: YPP only, desktop only, no A/B; shown ~3:2-cropped on channel/home surfaces; YouTube says 99.9% of Shorts views come from the feed where no thumbnail shows ([Tubefilter](https://www.tubefilter.com/2026/07/24/youtube-shorts-custom-thumbnails-neal-mohan-feature-update/), [ppc.land](https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/)); API support *unverified*. **Related-video link** (Short → long-form) exists since 2023 but is **not settable via the Data API** — reviewer adds it in Studio. Shorts and long-form are ranked per video: "If one Short doesn't perform well, it doesn't affect the distribution of your next long-form video" (Rene Ritchie, via [Panda Video](https://www.pandavideo.com/blog/shorts-and-long-form-videos-same-channel)). Views count on any play/replay since Mar 31 2025; revenue uses engaged views. Key Studio metric: "Viewed vs. swiped away" (third-party: swipe-away <30–40% healthy, *unverified*). July 2026 UI: thumbs replaced by a heart; ~200B daily Shorts views ([2026 CEO letter](https://blog.youtube/inside-youtube/the-future-of-youtube-2026/)).

**Publish timing** — [Buffer, Jul 24 2026, 1.8M videos](https://buffer.com/resources/best-time-to-post-on-youtube/): long-form best **Sunday 10 a.m.** (then Sun 9 a.m., Fri 12 p.m.; window 8–11 a.m.); Shorts best **Friday 4/6/7 p.m.** (Fri/Sat/Thu, 6–9 p.m.); worst long-form: weekday early-mid afternoon; worst Shorts: 12–5 p.m. except Friday. Other 2026 studies disagree (Sprout: Mon–Thu 1 p.m.; SocialPilot: Wednesday) — treat all as priors. Channel-specific "When your viewers are on YouTube" is Studio-only (no hour dimension in the Analytics API) → start from priors in the audience's top `country` timezone, then run your own day/hour experiments. Frequency (third-party consensus): ≥1 long-form/week, 3–5 Shorts/week, **separate schedules**.

**Search vs Browse** — no official percentages; recommendations outweigh search. Keyword placement (title first 40–60 chars, description first 150) serves Search + Google; title/thumbnail promise + first 30 s + retention serve Browse/Suggested.

**Benchmarks** — "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%"; new videos vary more; Home impressions depress CTR ([CTR FAQ](https://support.google.com/youtube/answer/7628154)). No official retention benchmark (third-party rule of thumb 50–60% solid, 70% strong).

### 2.6 API-settable vs human-only

| Item | Data API | Source |
|---|---|---|
| Title, description, tags, category, language, localizations | ✔ | [videos](https://developers.google.com/youtube/v3/docs/videos) |
| Scheduled publish | ✔ `publishAt` (+ `privacyStatus=private`) | same |
| Made for kids | ✔ `selfDeclaredMadeForKids` | same |
| AI disclosure | ✔ `containsSyntheticMedia` | [revision history](https://developers.google.com/youtube/v3/revision_history) |
| Custom thumbnail (long-form) | ✔ `thumbnails.set` | [quota](https://developers.google.com/youtube/v3/determine_quota_cost) |
| Custom thumbnail (Shorts) | *unverified* (4-week-old feature) | [ppc.land](https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/) |
| Captions | ✔ `captions.insert` | quota page |
| Playlists | ✔ | quota page |
| Top-level comment | ✔ `commentThreads.insert` | API docs |
| **Pin comment** | **✗** | [comments](https://developers.google.com/youtube/v3/docs/comments), [api-samples #360](https://github.com/youtube/api-samples/issues/360) |
| **End screens & cards** | **✗** (feature request open since Jan 2025) | [Issue 387277988](https://issuetracker.google.com/issues/387277988) |
| **Community posts** | **✗** | [postiz #537](https://github.com/gitroomhq/postiz-app/issues/537) |
| **Shorts related-video link** | **✗** | [Vizard help](https://help.vizard.ai/en/articles/13643189-can-i-add-a-link-to-my-long-form-youtube-video-when-publishing-shorts-via-vizard), [post-bridge help](https://support.post-bridge.com/social-media-scheduling/can-i-link-youtube-shorts-to-long-form-videos) |
| **Test & Compare** | **✗** | [A/B help](https://support.google.com/youtube/answer/13861714) |

### 2.7 Rubrics you can reimplement

**TubeBuddy SEO Studio** ([support](https://support.tubebuddy.com/hc/en-us/articles/39107477828251-How-to-use-SEO-Studio)): keyword in title · ≥80% of keyword words in title · keyword in first 60 chars of title · reads naturally · keyword in first 200 chars of description · partial matches elsewhere · tags include keyword + variants.
**vidIQ SEO score** ([scorecard](https://support.vidiq.com/en/articles/9696241-the-vidiq-scorecard)): 50% actionable (tag count, tag volume, "triple keyword" in title + description + tags) + 50% performance (views, engagement).

**Proposed LLM gate rubric (0–100; require ≥80 before the human-review queue):**

| Check | Pts |
|---|---|
| Primary keyword in title within first 40 chars; title 35–65 chars; accurate; ≤1 ALL-CAPS word; ≤1 emoji | 20 |
| Title type tagged (searchable vs intriguing) and matches target surface; title + thumbnail text complement | 10 |
| Description: keyword + plain-English summary in first 150 chars; unique; 800–2,000 chars; valid chapters; links; credits | 20 |
| Hashtags: 2–3 relevant, no spaces, ≤60 total | 5 |
| Tags: ≤500 chars; primary keyword, 2–3 variants, misspellings, 8–15 total, nothing irrelevant | 5 |
| Thumbnail: ≤4 words, ≤3 focus areas, readable at 160 px, ≥1280×720, ≤2 MB, correct ratio | 15 |
| Shorts: square/vertical, ≤180 s, hook in first 2 s, ≤40-char visible title | 10 |
| Compliance: `containsSyntheticMedia` correct; made-for-kids set; originality statement in review notes; no AI persona as human expert in YMYL topics | 15 |

### 2.8 Recommended keyword stack

**Tier 0 — $0/mo:** YouTube autocomplete fan-out (free; pass `hl`/`gl`; backoff) · Data API (`search.list` budget ~80/day; `batchGetStats` for velocity; `channels.list`) · Analytics API weekly `YT_SEARCH` pull · vidIQ MCP on Free (~30 calls/mo) · SerpApi free (250/mo, `engine=google_trends&gprop=youtube`) or trendsmcp free · `youtube-transcript-api` with a residential proxy if you want competitor transcripts.
**Tier 1 — ~$25–50/mo:** vidIQ Boost ($19 → ~400 MCP calls/mo) · DataForSEO pay-as-you-go for bulk SERP/Trends (1,000 scans ≈ $0.60–2.70) · optional Apify `apidojo/youtube-scraper` for large channel listings.
**Skip:** Ahrefs/Semrush APIs, keywordtool.io unless bulk volume is needed, TubeBuddy, pytrends, youtube-search-python, Social Blade.

**Opportunity score:** `opportunity = demand / competition` where demand = z-blend(autocomplete expansion count, vidIQ volume, Trends-YouTube 90-day slope) and competition = z-blend(median views of top-20, median channel subscribers, share of top-20 <180 days old, exact-phrase title matches). Prefer keywords whose top-20 includes small channels with high view velocity (demand exceeds supply).

### 2.9 Codified posting rules (one page for the metadata-generation LLM)

**Long-form (16:9, 8–20 min)**
- Title ≤65 chars (hard 100); primary keyword in first 40; accurate; ≤1 emoji; ≤1 ALL-CAPS word; branding/episode # last; generate 1 searchable + 2 intriguing variants; pick by target surface.
- Description: line 1 = keyword + one-sentence promise (≤150 chars); 2–4 natural sentences with 1–2 keywords; chapters block (`00:00 Intro` first, ≥3, ≥10 s, ascending); links; credits; 2–3 hashtags at the end; 800–2,000 chars; unique.
- Tags: 8–15, ≤500 chars; exact keyword, variants, misspellings, topic, format.
- Thumbnail: 16:9, ≥1280×720, ≤2 MB JPG/PNG; ≤4 words; ≤3 focus areas; high contrast; readable at 160 px; don't repeat the title; produce 2–3 variants for Test & Compare.
- Publish: `privacyStatus=private` + `publishAt` in the audience's top-country timezone; prior Sunday 10 a.m. / weekday 8–11 a.m.; avoid weekday 1–5 p.m.; ≥1/week, same weekday.
- Set `categoryId`, `defaultLanguage`, `selfDeclaredMadeForKids=false`, `containsSyntheticMedia` per §4, playlist, captions.
- Queue for the human reviewer: end screen + cards, pinned comment, Shorts related-video link, Test & Compare, community post.

**Shorts (9:16 or 1:1, ≤180 s)**
- Hook in the first 2 s; aim ≤60 s unless the idea needs more; 1080×1920.
- Title ≤40 visible chars (hard 100); no `#Shorts` needed; 2–3 hashtags in description; first line names the related long-form.
- Thumbnail: if in YPP, supply a 9:16 image with key elements centered; otherwise skip.
- Publish prior: Thu/Fri/Sat 4–9 p.m. audience time; never 12–5 p.m. except Friday; 3–5/week on a separate schedule; `notifySubscribers=false`.
- Judge by "viewed vs swiped away" and engaged views; a weak Short does not hurt long-form.

**Compliance (every upload)** — `containsSyntheticMedia=true` only for realistic synthetic people/events/scenes or altered real footage; original commentary per video; vary structure; visible/audible human element; no slideshow + TTS; no AI persona as a human expert on health/finance/legal/politics; reviewer sign-off logged.

**Watch (Analytics API):** CTR 2–10% typical; high CTR + low AVD → fix title/thumbnail mismatch; fold weekly `YT_SEARCH` terms into titles/descriptions.

---

## 3. Voice: clone vs stock, ElevenLabs vs alternatives

Workload used for all cost math: ~1,000 chars ≈ 1 minute of narration. **Base** = 8 long-form × ~12k chars + 20 Shorts × ~1.2k ≈ 120k chars → **170k with a 40% retry buffer** (~2.8 h audio). **Heavy** = 3× → **500k** (~8.3 h).

### 3.1 ElevenLabs **[verified — fetched 2026-08-22]**

**Plans** ([pricing](https://elevenlabs.io/pricing)):

| Plan | $/mo | Annual | Credits/mo | ≈ minutes (v2/v3) | Instant clone | Pro clone | Commercial |
|---|---|---|---|---|---|---|---|
| Free | $0 | — | 10k | ~10 | No | No | **No** |
| Starter | $6 | $5 | 30k | ~30 | Yes | No | Yes |
| Creator | $22 ($11 first month) | $18.33 | **121k** | ~121 | Yes | **Yes (1 slot)** | Yes |
| Pro | $99 | $82.50 | 600k | ~600 | Yes | Yes | Yes |
| Scale | $299 | $249.17 | 1.8M | ~1,800 | Yes | Yes (3) | Yes |
| Business | $990 | $825 | 6M | ~6,000 | Yes | Yes (10) | Yes |

Older 2026 articles still show 100k/500k/2M credits and $330/$1,320 — the official page today shows the post-May-2026 structure above.

**Credits per character:** Multilingual v2 = 1; Eleven v3 = 1 (the 80%-off alpha promo ended June 2025); Flash v2.5 / Turbo v2.5 = 0.5 via API (Turbo is deprecated in favor of Flash).
**API pay-as-you-go** ([pricing/api](https://elevenlabs.io/pricing/api)): **$0.10/1k chars for v3 & Multilingual v2; $0.05/1k for Flash/Turbo/"v3 Conversational"** — after a May 7 2026 cut of up to 55% ([announcement](https://elevenlabs.io/blog/weve-lowered-api-agents-pricing-and-introduced-pay-as-you-go)). Same rate on every paid tier; only Enterprise negotiates lower. Discrepancy to check in-app: the API pricing page describes Creator as "220k characters of TTS (v3) included" vs. 121k credits on the main page.

**Cloning** ([docs](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning)):

| | Instant (IVC) | Professional (PVC) |
|---|---|---|
| Plan | Starter+ | **Creator+** |
| Audio | <2 min usable (10 s min) | **30 min minimum; 2–3 h recommended; 180 min max** |
| Format guidance | clean audio | MP3 192 kbps+; RMS −23 to −18 dB; true peak −3 dB; single speaker; no music/noise; treated room; XLR mic; two fists from mic; pop filter |
| Style | reference only | "The speaking style in the samples you provide will be replicated in the output" |
| Verification | voice captcha | voice captcha read in the same delivery; retry after 24 h |
| Training | none | **3–6 h typical, up to 24 h** |
| Quality | "relies on prior knowledge… an educated guess" | "substantially higher quality," better consistency and emotional range |
| Models trained | — | **Flash v2.5, Turbo v2.5, Multilingual v2** (+ v2 English). **v3 not listed.** |

**v3 + PVC:** the v3 launch note says "Professional Voice Clones (PVCs) are currently not fully optimized for Eleven v3… use an Instant Voice Clone (IVC) or designed voice" ([blog](https://elevenlabs.io/blog/eleven-v3)); 2026 docs still list only v2-family models. v3 went GA Feb 2 2026 *(secondary)*. **Treat PVC+v3 as unverified; test it.**

**API specifics for batch:** per-request limits **v3 5,000 / Multilingual v2 10,000 / Flash v2.5 40,000 chars** ([models](https://elevenlabs.io/docs/overview/models)). Output: `mp3_44100_192` requires Creator+; `pcm_44100`/`wav_44100` require Pro+ ([with-timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps)). **Timestamps:** `/v1/text-to-speech/{voice_id}/with-timestamps` returns character-level alignment (+ `normalized_alignment`) — aggregate to words for captions. Continuity: `previous_text`/`next_text` or `previous_request_ids`/`next_request_ids` (max 3); `seed`; up to 3 `pronunciation_dictionary_locators`; `voice_settings` (stability, similarity_boost, style, speed, speaker_boost). v3 audio tags: `[whispers] [sighs] [laughs] [sad] [excited] [slowly]…`. Voice Design (`eleven_ttv_v3`) creates a unique voice from a text prompt. Concurrency: Free 2, Starter 3, Creator 5, Pro 10. Arena (Artificial Analysis, 2026-08-22): v3 Conversational 1,220 (#5), Eleven v3 1,179 (#13), Multilingual v2 1,104, Flash v2.5 1,084.

### 3.2 Major cloud alternatives

| Vendor | Models & price | Cloning | Timestamps | Limits / notes |
|---|---|---|---|---|
| **OpenAI** ([pricing](https://developers.openai.com/api/docs/pricing)) | tts-1 $15/1M; tts-1-hd $30/1M; **gpt-4o-mini-tts** $0.60/1M text-in + $12/1M audio-out tokens ≈ **$0.015/min** (≈$15/1M chars); 13 voices; `instructions` steerability | **none** (policy) | **no** → pair with `gpt-4o-mini-transcribe` $0.003/min | 2,000 tokens/request; **24 kHz only**; Elo 1,108 (tts-1-hd). Tier B. |
| **Google Gemini API TTS** ([pricing](https://ai.google.dev/gemini-api/docs/pricing)) | 2.5 Flash TTS $10/1M audio tokens (≈**$0.015/min**; batch $5); 2.5 Pro / **3.1 Flash TTS** $20/1M (≈$0.03/min); ~30 voices; style via prompt; multi-speaker | **none** | no | 32k-token context but "quality and consistency may drift with outputs longer than a few minutes" → chunk per paragraph. **3.1 Flash TTS Elo 1,212 (#6) — best quality-per-dollar stock voice.** |
| **Google Cloud TTS** (*secondary*, [texttolab Jun 2026](https://texttolab.com/blog/google-cloud-tts-pricing)) | Standard $4; WaveNet $4; Neural2 $16; **Chirp 3 HD $30 (1M free/mo)**; Studio $160; **Instant Custom Voice $60** | ICV **allow-list via sales**; ≤10 s reference + fixed consent script ([docs](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice)) | SSML `<mark>` only *(memory)* | 5,000 bytes/request; long-audio API reportedly doesn't work with Chirp 3 HD. Tier B. |
| **Microsoft Azure** (*secondary*, [texttolab Jun 2026](https://texttolab.com/blog/azure-text-to-speech-pricing)) | Neural $15–16/1M (0.5M free/mo); **Neural HD $22**; **Personal Voice $24 + ~$0.60/profile/mo**; Custom Neural Voice Pro enterprise (~$2.9k/mo hosting) | **Personal Voice: limited-access approval**, 1 min audio + recorded consent ([overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/personal-voice-overview)) | WordBoundary events | 10 min audio/request; batch API. Elo 1,031 (Neural). Tier B/C. |
| **Amazon Polly** ([pricing](https://aws.amazon.com/polly/pricing/)) | Standard $4; Neural $16; **Generative $30**; Long-Form $100 | none (Brand Voice = bespoke) | Speech Marks | Elo 887 (Neural). Tier C. |

### 3.3 Specialist TTS vendors

| Vendor | Model · price | Cloning | Timestamps | Elo | Notes |
|---|---|---|---|---|---|
| **Cartesia** ([pricing](https://cartesia.ai/pricing)) | **Sonic-3.6** (Aug 18 2026). Free 20k credits (no commercial); **Pro $5/100k**; **Startup $49/1.25M**; Scale $299/8M. 1 credit = 1 char; ≈$49/1M AA-normalized | IVC on Pro; **PVC (2 clones) on Startup**. PVC credit rules contradictory (launch blog: free training, 1 credit/char; 2026 articles: 1M-credit training + 1.5 credits/char) — confirm | yes (`add_timestamps`) | **1,285 (#1)** | 42 languages; IPA dictionaries; emotion tags; 44.1/48 kHz; concurrency Pro 3 / Startup 5. |
| **Inworld** ([pricing](https://inworld.ai/pricing)) | **TTS-2 $25/1M** → $5 enterprise; **TTS-2 Flash $15/1M**; first 70 min free; commercial on all tiers | IVC on all paid tiers; PVC add-on from $300/mo | yes (+phonemes, visemes) | 1,196–1,208 | 200+ languages; custom pronunciations; pause controls. **Best cheap cloned-voice option.** |
| **Hume** ([pricing](https://www.hume.ai/pricing)) | Octave 2 (preview): Free $0/10k; Starter $3/30k; Creator $14/140k ($0.10/1k over); Pro $70/1M ($0.05/1k) | IVC from 15 s; voice design | word + phoneme | 1,057 (#58) | 5,000 chars/utterance; underperforms marketing. |
| **Fish Audio** (*secondary*, [texttolab Aug 2026](https://texttolab.com/blog/fish-audio-pricing)) | S2.1 Pro **$15/1M bytes**; Plus ~$11–20/mo; **S2.1 Pro API free until Aug 31 2026** under fair use ([blog](https://fish.audio/blog/s2-1-pro-free-api/)) | IVC 10–30 s; "proof of rights" for commercial clone use | yes | 1,125 | Open weights are **research-license** (commercial needs a license). |
| **MiniMax** ([fal HD](https://fal.ai/models/fal-ai/minimax/speech-2.8-hd), [API](https://platform.minimax.io/docs/api-reference/speech-t2a-http)) | Speech 2.8 HD **$100/1M**; Turbo **$60/1M**; rapid clone ~$1.50/voice | rapid clone | word-level (`subtitle_file`) | 1,173 (#14) | <10k chars/request; 44.1 kHz; IPA dictionary; Chinese vendor (data residency). |
| **Deepgram** ([pricing](https://deepgram.com/pricing)) | Aura-2 $30/1M; Flux $45/1M | **none** | no | ~1,054 | 2,000 chars/request; agent-oriented. |
| **Resemble AI** | Pricing page now lists detection products; TTS via Flex PAYG *(secondary, inconsistent ~$0.0005–0.006/s)* | rapid $2 / pro $5 per voice/mo | — | — | Company pivoted to deepfake detection; its open model Chatterbox is the asset. |
| **PlayAI / Play.ht** | — | — | — | — | **Dead.** Meta acqui-hire July 2025; API offline; **platform, voices, clones and data deleted Dec 31 2025, no export.** Own your raw recordings. |
| Speechify (Simba 3.2) | ~$10/1M AA-normalized *(not fetched)* | ? | ? | 1,240 (#3) | Cheapest top-5 model — worth a trial. |
| Smallest.ai Lightning V3.1 Pro · VUI Labs Luna · Alibaba Qwen-Audio-3.0-TTS-Plus | $19.5 · $80 · $27.6 per 1M | ? | ? | 1,195 · 1,221 · 1,240 | Arena leaders; less-known ecosystems. |
| Murf, WellSaid, LOVO/Genny, Typecast | $20–100/mo plan-based; cloning gated *(memory)* | — | — | not top-50 | Creator-UI products. |

**Artificial Analysis Speech Arena (provider-voice board, fetched 2026-08-22)** — top 10: Cartesia Sonic 3.6 (1,285), Alibaba Qwen-Audio-3.0-TTS-Plus (1,240), Speechify Simba 3.2 (1,240), VUI Luna (1,221), ElevenLabs v3 Conversational (1,220), Google Gemini 3.1 Flash TTS (1,212), StepFun StepAudio 2.5 (1,208), Cartesia Sonic 3.5 (1,203), Inworld TTS 1.5 Max (1,196), Smallest Lightning V3.1 Pro (1,195). Also: Eleven v3 1,179 (#13), MiniMax 2.8 HD 1,173, Fish S2 Pro 1,125 (#27, best open-weight), OpenAI tts-1-hd 1,108, Multilingual v2 1,104, Kokoro 1,060, Hume Octave 2 1,057, Azure Neural 1,031, Chatterbox 1,020 (#75), Polly Neural 887. **Caveat:** arenas score short clips for naturalness, not 15-minute stability or pronunciation of your vocabulary.

### 3.4 Open-source / self-hosted

| Model | License (commercial?) | Cloning | Size/GPU | Quality | Long-form | Hosted $ |
|---|---|---|---|---|---|---|
| **Chatterbox** (Resemble) — Turbo 350M EN, Multilingual V3 500M, Nano CPU | **MIT — yes** | zero-shot 5–20 s | ~4 GB VRAM; RTF ≈0.5 on 4090 | Elo 1,020; vendor blind test claims 65% preference vs ElevenLabs Turbo | needs chunking; community audiobook servers exist | fal $0.020–0.025/1k; Replicate L40S $0.000975/s |
| **Kokoro-82M** | Apache 2.0 — yes | **no** (54 presets) | CPU-capable | Elo 1,060 | chunk by sentence | ~$0.7/1M on Replicate |
| **Qwen3-TTS** (Jan 2026) | Apache 2.0 — yes | zero-shot 3 s; voice design | 0.6B/1.7B | strong EN/ZH | chunking | self-host |
| Fish Speech S2-Pro | **research license — commercial needs license** | 10–30 s | 4–5B | Elo 1,125 | chunking | use their API |
| VibeVoice (Microsoft) | MIT with re-release use restrictions, audible AI disclaimer + watermark | no | 1.5B/7B | good; 90-min multi-speaker | best OSS long-form, EN/ZH | self-host |
| IndexTTS-2/2.5 | Apache 2.0 with extra clauses | zero-shot; emotion control | ~0.5B | good | chunking | self-host |
| Higgs Audio v2 | Community license (commercial <100k AAU); v3 non-commercial | zero-shot | 3B | good | chunking | self-host |
| Dia · Orpheus · Zonos · CosyVoice 3 · Sesame CSM · Step-Audio-EditX | Apache 2.0 (Orpheus weights Llama license) | yes | 1–3B | decent; Step-Audio ~1,105 | chunking | Replicate/fal |
| Voxtral TTS (Mistral) | **CC-BY-NC — no** | 3 s | 4B | 1,056 | — | API ~$16/1M |
| F5-TTS | weights **CC-BY-NC — no** | yes | 0.3B | good | — | — |
| XTTS-v2 (Coqui) | **CPML non-commercial; Coqui defunct — no** | yes | 0.5B | dated | — | — |
| Spark-TTS | **CC-BY-NC-SA — no** | yes | 0.5B | decent | — | — |

**Economics at your volume:** Modal L40S $0.000542/s with $30/mo free credits; Replicate L40S $0.000975/s. 2.8 h of Chatterbox audio ≈ 1–1.5 GPU-hours ≈ **$2–6/month** — but you own chunking, stitching, drift QA, forced alignment for captions (no native timestamps), and a model ranked ~75th for naturalness. **Verdict: not worth it below ~50 h/month unless privacy/offline is the goal.** If you ever do: Chatterbox (MIT) and Qwen3-TTS (Apache) are the clean-license picks.

### 3.5 Clone your own voice vs. stock voice → **clone it (PVC), keep a stock voice as the A/B control**

**Quality evidence**
- Official: PVC is "substantially higher quality" with "stronger emotional range" and handles long narration pacing far better than IVC ([help](https://help.elevenlabs.io/hc/en-us/articles/13313681788305)).
- 4-month first-hand test (Creator + Pro, 1.4M chars, Jan–May 2026): IVC from 90 s was "85% me" with limited emotion; PVC from 30+ min noticeably superior — a partner could not tell the clone from the real voice on the first clip; persistent flaws = **proper nouns ("Anthropic", "Llama") and inconsistent dramatic pauses**; v3 audio tags fixed most emotion issues ([tabswire, May 9 2026](https://tabswire.com/elevenlabs-review/)).
- Educator with 40 min uploaded: IVC "sounded robotic"; PVC "pretty much just like me" with "some odd pronunciations" ([Substack](https://andrewvh.substack.com/p/how-i-used-elevenlabs-to-clone-my)).
- **The dataset is the product:** a PVC from 30–60 min of clean, consistent narration sounds like you; one from noisy, mixed-style audio sounds like a worse stock voice. Proper nouns and numbers are the #1 failure mode for *every* vendor → pronunciation dictionary regardless.

**Brand / trust / policy**
- YPP "inauthentic content" does not single out synthetic narration; "channels that use AI in their content remain eligible for monetization" (YouTube's Rene Ritchie via [Social Media Today](https://www.socialmediatoday.com/news/youtube-clarifies-monetization-update-inauthentic-repeated-content/752892/)). The risk is the *content pipeline* — templated LLM-script + stock-voice + stock-B-roll channels are what get removed.
- Disclosure is **not required** for "cloning one's own voice to create voice overs or dubs" ([Help 14328491](https://support.google.com/youtube/answer/14328491)). A stock voice on an original script needs no label either.
- Audience reaction (2026 creator reporting): viewers react negatively to low-quality, monotonous AI voices, not to AI voices per se; voice tone drives watch time and retention.

**Legal / consent** — every reputable vendor gates cloning (ElevenLabs voice-captcha; Google fixed consent script; Azure recorded statement + approval; Fish proof of rights). **Your own voice = zero friction everywhere.** Cloning anyone else's voice is a ToS breach and legal exposure.

**Practical controls** — a PVC or saved Voice-Design voice is frozen; vendor library voices can change or disappear. Pin `seed` + identical `voice_settings`. Pronunciation: ElevenLabs dictionaries (IPA/CMU + alias), Cartesia IPA, MiniMax, Google/Azure SSML; OpenAI/Gemini prompt-only. Emotion: v3 audio tags, Cartesia tags, Gemini/OpenAI style prompts. Languages: ElevenLabs PVC 38, Sonic 42, Inworld 200+.

**Recording a PVC dataset that works** (ElevenLabs guidance; applies everywhere)
1. 30 min minimum, **60–120 min ideal** (≤3 h useful), single speaker, one style per session.
2. Quiet treated room; XLR condenser + interface; pop filter; ~two fists from mic; consistent gain; RMS −23 to −18 dB; true peak −3 dB.
3. **Read in exactly the register you'll publish in** (consider a second, punchier dataset/clone for Shorts).
4. No music, reverb, or de-noiser artifacts; export 192 kbps+ MP3 or WAV.
5. Avoid long pauses, fillers, throat clears; include numbers, acronyms, and your channel's recurring proper nouns.
6. Complete the voice captcha in the same delivery; training 3–6 h (up to 24 h).
7. **Archive the raw WAVs** — your portable asset (the PlayAI lesson).

### 3.6 Pipeline considerations

| Need | ElevenLabs | Cartesia | Inworld | Gemini | OpenAI | Google Cloud | Azure | Fish / MiniMax | Chatterbox/Kokoro |
|---|---|---|---|---|---|---|---|---|---|
| Word timestamps | char-level (`/with-timestamps`) | yes | yes (+visemes) | **no** | **no** → STT | `<mark>` only | WordBoundary | yes | no → forced alignment |
| Max chars/request | v3 5k / v2 10k / Flash 40k | undocumented | undocumented | 32k tokens (drifts) | 2k tokens | 5 kB | 10 min audio | <10k (MiniMax) | chunk ~120–500 |
| Pronunciation control | dictionaries (3/req) | IPA dictionaries | custom | prompt only | prompt only | SSML/IPA | SSML/lexicon | dictionaries | none |
| 44.1 kHz output | mp3 192 (Creator+), PCM (Pro+) | up to 48 kHz | undocumented | 24 kHz | **24 kHz only** | 24 kHz | up to 48 kHz | 44.1 kHz | 24 kHz |
| Long-form stability | v2 = "stable" model; v3 more expressive/less stable; use prev/next text | good | TTS-2 claims 40% fewer word errors | drifts after minutes | chunk | chunk | 10-min cap, batch API | chunk | chunk per sentence |

**Rules of thumb**
- Normalize numbers, units, acronyms, URLs *before* TTS; don't rely on vendor normalization.
- Chunk at paragraph boundaries ≤4,500 chars (v3) / ≤9,000 (v2); pass `previous_text`/`next_text`; same seed + voice settings; crossfade 20–50 ms on stitch.
- **QA loop:** transcribe every chunk (ElevenLabs Scribe v2 $0.22/h or `gpt-4o-mini-transcribe` $0.003/min), diff against the script, auto-regenerate chunks above a WER threshold — this is what the 40% retry buffer pays for.
- Request 44.1 kHz (or PCM); ffmpeg → 48 kHz AAC for the mux; keep the alignment JSON for karaoke captions and `captions.insert`.

### 3.7 Master comparison

| Vendor | Best model | $/1M chars (or per min) | Cloning | Min plan for commercial | Timestamps | Quality | Notes |
|---|---|---|---|---|---|---|---|
| **ElevenLabs** | v3 / Multilingual v2 / Flash v2.5 | $100 / $100 / $50 PAYG | IVC Starter+ · **PVC Creator+** | Starter $6 (PVC: Creator $22) | char-level | **A** | Best cloning + tooling; PVC+v3 not officially optimized |
| **Cartesia** | Sonic-3.6 | ≈$49; $5/100k · $49/1.25M | IVC Pro · **PVC Startup** | Pro $5 | word | **A** (#1) | 48 kHz; IPA dictionaries |
| **Inworld** | TTS-2 / Flash | $25 / $15 on-demand | IVC all paid · PVC $300+/mo | on-demand | word+phoneme | A− | Best cheap cloned voice |
| **Google Gemini** | 3.1 Flash / 2.5 Flash TTS | ≈$0.03 / $0.015 per min | none | PAYG | no | **A** (#6) | Drifts >few min |
| Google Cloud TTS | Chirp 3 HD / ICV | $30 / $60; 1M free | ICV allow-list | PAYG | mark only | B | 5 kB/request |
| Azure | Neural HD / Personal Voice | $22 / $24 | Personal Voice limited-access | PAYG | WordBoundary | B | 10-min/request |
| Polly | Generative | $30 | none | PAYG | Speech Marks | C | Dated |
| OpenAI | gpt-4o-mini-tts / tts-1-hd | ≈$15 / $30 | none | PAYG | no | B | 2k tokens; 24 kHz |
| Hume | Octave 2 | $50–150 by plan | IVC 15 s | Creator $14 | word+phoneme | B− | #58 |
| Fish Audio | S2.1 Pro | $15 (free to Aug 31 2026) | IVC; rights proof | Plus ~$11–20 | yes | B+ | research-license weights |
| MiniMax | 2.8 HD / Turbo | $100 / $60 | rapid clone | PAYG | word | A− | CN vendor |
| Deepgram | Aura-2 | $30 | none | PAYG | no | C | agents |
| Speechify | Simba 3.2 | ~$10 | ? | ? | ? | A (#3) | test it |
| PlayAI | — | — | — | **dead** | — | — | — |
| Self-hosted Chatterbox | Turbo/Multilingual (MIT) | fal $20–25; own GPU $1–3/h audio | zero-shot | n/a | no | B− | ops burden |
| Self-hosted Kokoro | v1.0 (Apache) | ~$0.7; CPU | none | n/a | no | B− | cheapest OK stock |

### 3.8 Cost at your workload

| Path | Base (170k chars) | Heavy (500k chars) | Basis |
|---|---|---|---|
| **ElevenLabs Creator — PVC on Multilingual v2** | **≈ $27** ($22 + 49k × $0.10/1k) | **≈ $60**, or **Pro $99 flat** (600k credits) | official plan + API rates |
| ElevenLabs Creator — Flash v2.5 via API (0.5 credit/char) | $22 (fits plan) | ≈ $35 | official |
| ElevenLabs pure PAYG (no PVC) | $17 (v3) / $8.50 (Flash) | $50 / $25 | official |
| **Cartesia Startup (PVC)** | $49 flat | $49 flat (1.25M credits) | official |
| **Inworld TTS-2 / Flash** | ≈ $4.25 / $2.55 | ≈ $12.50 / $7.50 | official |
| Gemini 2.5 Flash TTS (stock) | ≈ $2.55 | ≈ $7.50 | official; batch halves it |
| Gemini 3.1 Flash TTS (stock) | ≈ $5.10 | ≈ $15 | official |
| OpenAI gpt-4o-mini-tts (stock) | ≈ $2.55 | ≈ $7.50 | official |
| Google Chirp 3 HD (stock) | $0 within 1M free | $0 | secondary |
| Google Instant Custom Voice | $10.20 | $30 | secondary |
| Azure Neural HD / Personal Voice | $3.74 / ≈ $4.70 | $11 / ≈ $12.60 | secondary |
| Hume Octave 2 | ≈ $17 | ≈ $50 (or Pro $70) | official |
| Fish S2.1 Pro | ≈ $2.55 ($0 until Aug 31 2026) | ≈ $7.50 | secondary + official promo |
| MiniMax 2.8 HD / Turbo | $17 / $10.20 | $50 / $30 | fal |
| Chatterbox on fal (Turbo) | ≈ $3.40 | ≈ $10 | fal |
| Chatterbox on Modal | ≈ $0 within free credits | ≈ $7–10 | official |
| Kokoro on Replicate | ≈ $0.12 | ≈ $0.35 | secondary |
| + STT QA / caption timing where needed | +$0.50–1 | +$1.50–3 | official |

### 3.9 Voice recommendation

1. **Clone your own voice (PVC)** with a stock/designed voice as the control. Render the first 3–5 videos both ways, compare retention, keep a Voice-Design v3 voice on file as a no-rights-issue fallback. Plan: **PVC + Multilingual v2 for long-form**; **IVC of your voice + v3 (or v3-Conversational) for Shorts**.
2. **Primary vendor — ElevenLabs Creator ($22/mo; $11 first month).** The only vendor combining PVC at a hobbyist price, 44.1 kHz/192 kbps output, character-level timestamps, pronunciation dictionaries, prev/next-text stitching and a stable v2 model. **≈ $22–30/mo base; ≈ $60–99/mo heavy.**
3. **Alt-primary — Cartesia Startup ($49 flat):** arena #1, PVC included, covers heavy usage with no overage math; younger tooling; confirm PVC credit rules before training.
4. **Fallback / outage hedge — Inworld TTS-2** (instant clone of the same recordings, ~$4–13/mo) and **Gemini Flash TTS** as the stock-voice control arm. Fish Audio is technically fine but licensing wording makes it a secondary.
5. **Avoid as narration primaries:** OpenAI (no cloning, 24 kHz, no timestamps), Deepgram, Polly/Azure Neural (dated), Hume (#58), Resemble (pivoted), PlayAI (dead). **Skip self-hosting** below ~50 h/month.

---

## 4. Policy constraints that shape the whole pipeline **[verified]**

1. **YPP "Inauthentic content"** (renamed from "repetitious content"; effective July 15 2025) — [Channel monetization policies](https://support.google.com/youtube/answer/1311392). **Not monetizable:** "similar or repetitive content with low educational value, commentary, narratives, or minimal variation"; "videos where characters are put in the same situation over and over again with the same outcome"; "image slideshows, templated storylines, or scrolling text with minimal or no narrative"; **"AI-generated content made with generic or unoriginal templates"** suggesting mass production without the creator's authentic insights. **Allowed:** same intro/outro with different bulk content; a series with consistent characters/format where each video has "a distinct storyline, focus, or concept"; automated tools where "the final product must still demonstrate your creative vision." Reused-content rules unchanged: commentary, critical review, reaction with commentary, substantive transformation are fine; clip compilations with no narrative are not.
2. **July 2026 clarification** ([TechCrunch Jul 20 2026](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/), [Tubefilter Jul 13 2026](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/)): three non-monetizable buckets — (a) generic or repetitive template content, AI "without the creator's authentic perspective"; (b) unsatisfying/off-putting emotionally manipulative formulas; (c) **AI personas presenting as human experts on health, legal, finance, or politics**. "Channels with too much of any of these three types of content will not be able to monetize." AI as a tool remains allowed. Enforcement: YouTube removed or hid ≥18 large AI-slop channels in Jan 2026 ([Tubefilter](https://www.tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/)); the widely repeated "16 channels / 35M subs / 4.7B views" figure is from secondary blogs *(unverified)*; some non-AI faceless channels were reportedly caught as collateral.
3. **AI disclosure — "altered or synthetic content"** ([Help 14328491](https://support.google.com/youtube/answer/14328491)). **Required** when realistic content makes a real person appear to say/do something they didn't, alters footage of a real event/place, or generates a realistic scene that didn't occur. **Not required** for "cloning one's own voice to create voice overs or dubs," "production assistance, like using generative AI tools to create or improve a video outline, script, thumbnail, title, or infographic," captions, clearly unrealistic/animated content, beauty filters, color/lighting. Label appears in the player (photorealistic) or expanded description (animated). Consistently not disclosing → forced labels, removal, or YPP suspension. **Disclosing does not restrict reach or monetization.** Set `status.containsSyntheticMedia` per video.

**Design consequences:** every video needs an original argument/research angle, not a template with swapped nouns; vary structure, hooks, visuals and narration across episodes; keep a real human voice and editorial stance; never present an AI persona as a human expert on money/health/law/politics; log the human reviewer's sign-off per video (audit trail); no slideshow-plus-TTS formats; `containsSyntheticMedia=true` only for realistic synthetic visuals of real people/places/events.

---

## 5. Recommended architecture

### 5.1 Stack

| Layer | Choice | Monthly cost |
|---|---|---|
| Keyword/topic research | vidIQ MCP (Free → Boost $19) + YouTube autocomplete fan-out + Data API `search.list`/`batchGetStats`/`channels.list` + Analytics API weekly `YT_SEARCH` pull + SerpApi free tier for Trends-YouTube | $0 → $19–45 |
| Metadata generation | LLM step following §2.9, scored by §2.7 rubric (gate ≥80) | LLM tokens |
| Voice | ElevenLabs Creator: PVC on Multilingual v2 (long-form), IVC + v3 (Shorts); pronunciation dictionary; STT QA loop; Inworld TTS-2 fallback | $22–30 base / $60–99 heavy |
| Publishing | Python upload service on the Data API (own GCP project, audit submitted day one); Upload-Post as bridge until the audit passes and as permanent fallback | $0 after audit; $24 during bridge |
| Human review gate | Queue (folder manifest or DB table) showing video, title variants, thumbnail variants, description, SEO score, compliance flags → approval sets `publishAt` | — |
| **Total** | | **≈ $25–60/mo base; ≈ $80–150/mo heavy** |

### 5.2 Per-item manifest (what the folder structure carries into the upload job)

`video.mp4` · `thumbnail.jpg` (≤2 MB) · `captions.srt` · `meta.json` = `{ format: "long"|"short", title, title_variants[], description (with chapters), tags[], categoryId, defaultLanguage, playlistId, containsSyntheticMedia, selfDeclaredMadeForKids: false, notifySubscribers (false for Shorts), publishAt (null until approved), seo_score, compliance_notes, reviewer_signoff }`

### 5.3 Human-only checklist (reviewer completes in Studio after publish — no API exists)

Pin comment · end screen + cards · Shorts → long-form "related video" link · Test & Compare thumbnail A/B (long-form, desktop) · community post.

### 5.4 Implementation sequence

1. **Channel & Google setup (day 1):** phone-verify channel; GCP project; OAuth consent External + `youtube.force-ssl`; **Publish "In production"**; Desktop client; one-time consent; store refresh token. One-page HTTPS site + privacy policy; **submit the audit form** (individual, "video uploading", own channel).
2. **Bridge publisher (day 1–2):** Upload-Post free tier; test one private long-form + one private Short end-to-end with thumbnail, playlist, `scheduled_date`, `containsSyntheticMedia`, explicit `privacyStatus`.
3. **Voice (week 1):** record 60–120 min PVC dataset; ElevenLabs Creator; train PVC; pronunciation dictionary; render one 2,000-word script with timestamps; STT QA diff; A/B vs a stock voice and a Cartesia/Inworld render.
4. **Keyword research step (week 1–2):** vidIQ MCP + autocomplete + Data API + Analytics API; opportunity score; ranked topic backlog.
5. **Metadata generator + rubric gate (week 2).**
6. **Direct-API uploader + review gate (week 2–3):** Python service, idempotent, resumable; switch from Upload-Post to direct API once the audit passes (keep Upload-Post configured).
7. **Verify the unverified items (§6).**
8. If orchestrating in **n8n**: n8n Cloud's built-in YouTube credential is blocked — call the Python upload service / Upload-Post via HTTP Request nodes, not the native YouTube node.

### 5.5 Verification checklist (all doable on private videos)

1. **Upload path:** upload a 16:9 test and a 9:16 ≤180 s test as `private` via the Data API; confirm `uploadStatus=processed`; confirm the vertical one appears in the channel's Shorts tab and the horizontal one doesn't.
2. **Private lock:** check for the "locked private / unverified API service" notice in Studio before the audit passes; repeat after approval.
3. **Scheduling:** `videos.update` with `privacyStatus=private` + `publishAt` 20 min ahead; confirm the flip time (checks for undocumented rounding).
4. **Thumbnails/captions/playlists:** `thumbnails.set` on the long-form test **and on the Short** (record the result); `captions.insert` with generated SRT; `playlistItems.insert`.
5. **Bridge parity:** repeat step 1 via Upload-Post with explicit `privacyStatus=private`.
6. **Voice:** render the same 2,000-word script on PVC+v2, IVC+v3, Cartesia Sonic-3.6, Inworld TTS-2; transcribe; WER vs script; listen for drift at minutes 8–12; confirm timestamp alignment.
7. **Keyword stack:** one vidIQ MCP call, one autocomplete fan-out, one `search.list` + `batchGetStats` scan, one Analytics `YT_SEARCH` pull; confirm quota debits from the expected buckets.
8. **Rubric:** run the generator on 5 topics; confirm rejects for title >100, description >5,000 bytes, tags >500, invalid chapters.
9. **Policy gate:** `containsSyntheticMedia` true only when the manifest marks realistic AI visuals; `notifySubscribers=false` on Shorts.

---

## 6. Unverified items to test before relying on them

- `thumbnails.set` on a Short (custom Shorts thumbnails launched July 25 2026, YPP + desktop Studio only).
- Any rounding of `publishAt` (none documented; one unexplained forum report of a shifted time).
- Whether Harper Labs' hosted "YouTube Studio MCP" runs an audited Google app.
- Exact per-channel daily upload cap (`uploadLimitExceeded`).
- ElevenLabs PVC quality on Eleven v3; the Creator "121k credits vs 220k v3 characters" discrepancy; Cartesia PVC credit rules.
- Whether Google's official Trends API alpha exposes the YouTube-search property.
- The verbatim "(Optional) Include #Shorts…" help-page sentence (not reproducible on the fetched page).

---

## 7. Sources

**YouTube Data / Analytics API (official):** [Revision history](https://developers.google.com/youtube/v3/revision_history) · [Quota costs](https://developers.google.com/youtube/v3/determine_quota_cost) · [Getting started](https://developers.google.com/youtube/v3/getting-started) · [Quota & compliance audits](https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits) · [Audit & Quota Extension form](https://support.google.com/youtube/contact/yt_api_form) · [Developer policies](https://developers.google.com/youtube/terms/developer-policies) · [videos resource](https://developers.google.com/youtube/v3/docs/videos) · [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) · [videos.update](https://developers.google.com/youtube/v3/docs/videos/update) · [thumbnails.set](https://developers.google.com/youtube/v3/docs/thumbnails/set) · [captions.insert](https://developers.google.com/youtube/v3/docs/captions/insert) · [comments](https://developers.google.com/youtube/v3/docs/comments) · [Resumable uploads](https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol) · [Analytics dimensions](https://developers.google.com/youtube/analytics/dimensions) · [Analytics sample requests](https://developers.google.com/youtube/analytics/sample-requests) · [Python media docs](https://googleapis.github.io/google-api-python-client/docs/media.html) · [upload_video.py sample](https://github.com/youtube/api-samples/blob/master/python/upload_video.py)

**Google OAuth:** [OAuth2 token expiration](https://developers.google.com/identity/protocols/oauth2#expiration) · [App audience / testing](https://support.google.com/cloud/answer/15549945) · [When verification is not needed](https://support.google.com/cloud/answer/13464323) · [Unverified apps](https://support.google.com/cloud/answer/7454865) · [Verification requirements](https://support.google.com/cloud/answer/13464321) · [Sensitive scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification)

**YouTube Help (policy & features):** [Videos locked as private 7300965](https://support.google.com/youtube/answer/7300965) · [Three-minute Shorts 15424877](https://support.google.com/youtube/answer/15424877) · [Upload Shorts 12779649](https://support.google.com/youtube/answer/12779649) · [Shorts basics 10059070](https://support.google.com/youtube/answer/10059070) · [Upload limits 71673](https://support.google.com/youtube/answer/71673) · [Daily upload limit 10383400](https://support.google.com/youtube/answer/10383400) · [Thumbnails 72431](https://support.google.com/youtube/answer/72431) · [Title & thumbnail tips 12340300](https://support.google.com/youtube/answer/12340300) · [Description tips 12948449](https://support.google.com/youtube/answer/12948449) · [Tags 146402](https://support.google.com/youtube/answer/146402) · [Hashtags 6390658](https://support.google.com/youtube/answer/6390658) · [Chapters 9884579](https://support.google.com/youtube/answer/9884579) · [Test & Compare 13861714](https://support.google.com/youtube/answer/13861714) · [CTR FAQ 7628154](https://support.google.com/youtube/answer/7628154) · [Scheduling 1270709](https://support.google.com/youtube/answer/1270709) · [AI disclosure 14328491](https://support.google.com/youtube/answer/14328491) · [AI label 15447836](https://support.google.com/youtube/answer/15447836) · [YPP monetization policies 1311392](https://support.google.com/youtube/answer/1311392)

**YouTube blog / news:** [Recommendation system](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/) · [2026 CEO letter](https://blog.youtube/inside-youtube/the-future-of-youtube-2026/) · [Shorts thumbnails (Studio)](https://blog.youtube/news-and-events/youtube-studio-custom-thumbnail-updates/) · [Tubefilter Shorts thumbnails](https://www.tubefilter.com/2026/07/24/youtube-shorts-custom-thumbnails-neal-mohan-feature-update/) · [ppc.land Shorts thumbnails](https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/) · [Tubefilter Research tab Aug 2026](https://www.tubefilter.com/2026/08/05/youtube-research-tab-outlier-multipliers-viewer-comparison-data/) · [TechCrunch Jul 2025 policy](https://techcrunch.com/2025/07/09/youtube-prepares-crackdown-on-mass-produced-and-repetitive-videos-as-concern-over-ai-slop-grows/) · [Social Media Today clarification](https://www.socialmediatoday.com/news/youtube-clarifies-monetization-update-inauthentic-repeated-content/752892/) · [TechCrunch Jul 2026 clarification](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/) · [Tubefilter Jul 2026](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/) · [Tubefilter Jan 2026 crackdown](https://www.tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/) · [TNW collateral damage](https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage) · [Buffer best time to post (Jul 2026)](https://buffer.com/resources/best-time-to-post-on-youtube/) · [Panda Video on Shorts vs long-form](https://www.pandavideo.com/blog/shorts-and-long-form-videos-same-channel)

**Upload tooling:** [porjo/youtubeuploader](https://github.com/porjo/youtubeuploader) · [issue #86 (audit anecdotes)](https://github.com/porjo/youtubeuploader/issues/86) · [tokland/youtube-upload](https://github.com/tokland/youtube-upload) · [googleapis Node #276](https://github.com/googleapis/google-api-nodejs-client/issues/276) · [anwerj/youtube-uploader-mcp](https://github.com/anwerj/youtube-uploader-mcp) · [mrchevyceleb/youtube-mcp](https://github.com/mrchevyceleb/youtube-mcp) · [Harper Labs MCP on PulseMCP](https://www.pulsemcp.com/servers/harper-labs-youtube-studio) · [Upload-Post docs](https://docs.upload-post.com/api/upload-video.md) · [Zernio pricing](https://zernio.com/pricing) · [Zernio YouTube guide](https://docs.zernio.com/platforms/youtube) · [Ayrshare pricing](https://www.ayrshare.com/pricing/) · [Ayrshare YouTube docs](https://www.ayrshare.com/docs/apis/post/social-networks/youtube) · [Blotato pricing](https://www.blotato.com/pricing) · [Blotato MCP](https://help.blotato.com/api/mcp) · [Post Bridge limits](https://support.post-bridge.com/media-limits-and-processing/post-bridge-platform-limits-and-restrictions) · [Metricool pricing](https://metricool.com/pricing/) · [Buffer API](https://buffer.com/resources/buffer-api-is-here/) · [Buffer YouTube metadata](https://developers.buffer.com/types/YoutubePostMetadataInput.html) · [Publer API](https://publer.com/help/en/article/how-to-access-the-publer-api-1w08edo/) · [SocialBee no API](https://help.socialbee.com/hc/en-us/articles/29979123668375-Do-you-have-a-public-API-or-white-labeling-options) · [Zapier YouTube problems](https://help.zapier.com/hc/en-us/articles/8495991159693-Common-Problems-with-YouTube) · [n8n #18693](https://github.com/n8n-io/n8n/issues/18693) · [n8n large file thread](https://community.n8n.io/t/large-file-youtube-upload/65854) · [Postiz YouTube](https://docs.postiz.com/providers/youtube) · [Google official MCPs](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) · [Postproxy upload guide](https://postproxy.dev/blog/youtube-upload-api-guide/) · [bundle.social Shorts API](https://bundle.social/blog/youtube-shorts-api-secrets)

**Keyword tools:** [vidIQ MCP](https://vidiq.com/mcp/) · [vidIQ MCP help](https://support.vidiq.com/en/articles/15082430-vidiq-mcp) · [vidIQ plans](https://vidiq.com/plans/) · [vidIQ scorecard](https://support.vidiq.com/en/articles/9696241-the-vidiq-scorecard) · [TubeBuddy SEO Studio](https://support.tubebuddy.com/hc/en-us/articles/39107477828251-How-to-use-SEO-Studio) · [Ahrefs API v3](https://help.ahrefs.com/en/articles/6559232-about-api-v3) · [Semrush YouTube app](https://www.semrush.com/kb/1362-keyword-analytics-for-youtube) · [Keywords Everywhere credits](https://keywordseverywhere.com/credits.html) · [keywordtool.io API](https://keywordtool.io/api) · [DataForSEO YouTube SERP](https://dataforseo.com/pricing/serp/youtube-serp-api) · [DataForSEO Trends](https://dataforseo.com/pricing/keywords-data/google-trends) · [SerpApi pricing](https://serpapi.com/pricing) · [SerpApi YouTube](https://serpapi.com/youtube-search-api) · [SerpApi Trends](https://serpapi.com/google-trends-api) · [Apify pricing](https://apify.com/pricing) · [apidojo/youtube-scraper](https://apify.com/apidojo/youtube-scraper) · [Google Trends API alpha](https://developers.google.com/search/blog/2025/07/trends-api) · [trendsmcp](https://github.com/trendsmcp/google-search-trends-api) · [YouTube suggest scraper README](https://github.com/ChocoData-com/youtube-suggest-scraper/blob/main/README.md) · [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) · [kimtaeyoon83 transcript MCP](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) · [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) · [icraft2170/youtube-data-mcp-server](https://github.com/icraft2170/youtube-data-mcp-server) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) · [pytrends (archived)](https://github.com/GeneralMills/pytrends)

**Voice — ElevenLabs (official):** [pricing](https://elevenlabs.io/pricing) · [API pricing](https://elevenlabs.io/pricing/api) · [May 2026 price cut](https://elevenlabs.io/blog/weve-lowered-api-agents-pricing-and-introduced-pay-as-you-go) · [models](https://elevenlabs.io/docs/overview/models) · [voice cloning concepts](https://elevenlabs.io/docs/eleven-api/concepts/voice-cloning) · [PVC guide](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning) · [with-timestamps API](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps) · [v3](https://elevenlabs.io/v3) · [v3 launch post](https://elevenlabs.io/blog/eleven-v3) · [Voice Design](https://elevenlabs.io/docs/eleven-creative/voices/voice-design) · [IVC vs PVC help](https://help.elevenlabs.io/hc/en-us/articles/13313681788305) · [concurrency](https://help.elevenlabs.io/hc/en-us/articles/14312733311761). **Secondary:** [flexprice](https://flexprice.io/blog/elevenlabs-pricing-breakdown) · [texttolab](https://texttolab.com/blog/elevenlabs-pricing) · [bigvu](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/) · [coval review](https://www.coval.ai/blog/elevenlabs-review-2026-voice-cloning-and-synthesis-capabilities-explained/) · [tabswire 4-month review](https://tabswire.com/elevenlabs-review/) · [Substack PVC account](https://andrewvh.substack.com/p/how-i-used-elevenlabs-to-clone-my)

**Voice — other vendors:** [OpenAI pricing](https://developers.openai.com/api/docs/pricing) · [OpenAI TTS guide](https://developers.openai.com/api/docs/guides/text-to-speech) · [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) · [Chirp 3 ICV](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice) · [Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) · [Google Cloud TTS pricing (secondary)](https://texttolab.com/blog/google-cloud-tts-pricing) · [Azure Personal Voice](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/personal-voice-overview) · [Azure quotas](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-services-quotas-and-limits) · [Azure pricing (secondary)](https://texttolab.com/blog/azure-text-to-speech-pricing) · [Polly pricing](https://aws.amazon.com/polly/pricing/) · [Cartesia pricing](https://cartesia.ai/pricing) · [Cartesia models](https://docs.cartesia.ai/build-with-cartesia/models/tts) · [Cartesia PVC blog](https://www.cartesia.ai/blog/pro-voice-cloning) · [Sonic-3.6 news](https://www.marktechpost.com/2026/08/18/cartesia-ships-sonic-3-6-a-streaming-tts-model-that-now-leads-both-artificial-analysis-speech-arenas/) · [Hume pricing](https://www.hume.ai/pricing) · [Hume TTS docs](https://dev.hume.ai/docs/text-to-speech-tts/overview) · [Fish free API](https://fish.audio/blog/s2-1-pro-free-api/) · [Fish S2-Pro license](https://huggingface.co/fishaudio/s2-pro) · [Fish pricing (secondary)](https://texttolab.com/blog/fish-audio-pricing) · [MiniMax API](https://platform.minimax.io/docs/api-reference/speech-t2a-http) · [MiniMax on fal](https://fal.ai/models/fal-ai/minimax/speech-2.8-hd) · [Inworld pricing](https://inworld.ai/pricing) · [Inworld TTS docs](https://docs.inworld.ai/docs/tts/tts) · [Deepgram pricing](https://deepgram.com/pricing) · [Resemble pricing](https://www.resemble.ai/pricing/) · [PlayAI shutdown](https://texttolab.com/blog/play-ht-shutdown-alternatives) · [Artificial Analysis arena](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice) · [TTS Arena snapshot May 2026](https://offlinetts.com/blog/tts-arena-leaderboard-2026/)

**Voice — open source & hosting:** [Chatterbox](https://github.com/resemble-ai/chatterbox) · [Chatterbox on fal](https://fal.ai/models/fal-ai/chatterbox/text-to-speech) · [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) · [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) · [VibeVoice](https://github.com/microsoft/VibeVoice) · [Higgs Audio license](https://huggingface.co/bosonai/higgs-audio-v2-generation-3B-base/blob/main/LICENSE) · [Voxtral TTS](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) · [F5-TTS license discussion](https://github.com/SWivid/F5-TTS/discussions/997) · [XTTS-v2 license discussion](https://huggingface.co/coqui/XTTS-v2/discussions/106) · [Modal pricing](https://modal.com/pricing) · [Replicate pricing](https://replicate.com/pricing)

*Not reachable during research:* reddit.com (crawler-blocked), Hugging Face TTS Arena V2 (would not render), several JS-rendered official pricing pages (Google Cloud TTS, Azure Speech) — secondary sources used and marked.
