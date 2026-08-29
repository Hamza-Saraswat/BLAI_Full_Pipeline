# YouTube Analytics: what the API key gives and what needs OAuth

Two Google APIs, two access models. The pipeline starts with the cheap one and adds the second when the retro needs retention or search terms. Facts below follow `research/youtube-automation-research.md` (sections 1.3, 2.4, 2.5); verify anything marked "verify" against the current Google docs before relying on it.

## Data API v3 with an API key (what `yt_stats.py` uses)

| Gives | Endpoint | Cost (units) |
|-------|----------|--------------|
| Views, likes, comments, duration, publish time of any public video | `videos.list` (50 ids per call) | 1 per call |
| Subscriber count, total views, the uploads playlist | `channels.list` (`forHandle=@BuildLocalAI` or `id`) | 1 |
| The channel's upload list | `playlistItems.list` on the uploads playlist (50 per page) | 1 per page |
| Competitor videos for a query | `search.list` (keyword research skill) | 100 |

- Quota: 10,000 units per project per day. A full stats pull of 500 videos costs about 21 units.
- No OAuth, no consent screen, no compliance audit for read-only public data. Restrict the key to the YouTube Data API in the Cloud console.
- Like counts can be hidden per video (`likeCount` absent), comments can be disabled (`commentCount` absent); the snapshot stores `null` then.
- Not available with a key: anything about who watched, how long, or where they came from.

## YouTube Analytics API with OAuth (own channel only)

Scope `https://www.googleapis.com/auth/yt-analytics.readonly` (add `youtube.readonly` for video metadata in the same token). Endpoint `GET https://youtubeanalytics.googleapis.com/v2/reports` with `ids=channel==MINE`, `startDate`, `endDate`, `metrics`, `dimensions`, `filters`, `sort`.

| Need | Metrics and dimensions |
|------|------------------------|
| Retention curve per video | `metrics=audienceWatchRatio,relativeRetentionPerformance` with `dimensions=elapsedVideoTimeRatio`, `filters=video==<id>` |
| Average view duration and percentage | `metrics=views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage` with `dimensions=video` |
| Search terms that brought viewers | `dimensions=insightTrafficSourceDetail`, `filters=insightTrafficSourceType==YT_SEARCH` (low-volume terms are suppressed) |
| Traffic source mix (Shorts feed, suggested, search, external) | `dimensions=insightTrafficSourceType` |
| Subscribers gained per video | `metrics=subscribersGained,subscribersLost` with `dimensions=video` |
| Views by day, country, device | `dimensions=day`, `country`, `deviceType` |
| Engaged views (Shorts) | `metrics=engagedViews` (added in 2025; verify the metric name) |

Not in either API, Studio only: impressions and impressions click-through rate, "viewed vs swiped away" for Shorts, the hour-of-day "when your viewers are on YouTube" chart, Test & Compare results. When the retro wants CTR, a human reads it in Studio and adds it to the note by hand.

## Adding OAuth later (one afternoon)

1. Same Google Cloud project as the API key. Enable "YouTube Analytics API" (and "YouTube Data API v3").
2. OAuth consent screen: External, publish it to "In production" without submitting for verification. A consent screen left in "Testing" issues refresh tokens that expire after 7 days; production tokens persist (6 months unused, user revocation and the 100-tokens-per-client cap still apply).
3. Create a Desktop OAuth client. Do the one-time consent on a laptop (click through the "unverified app" screen), requesting `yt-analytics.readonly` and `youtube.readonly`, and keep the refresh token.
4. Store `YT_OAUTH_CLIENT_ID`, `YT_OAUTH_CLIENT_SECRET`, `YT_OAUTH_REFRESH_TOKEN` where the retro runs: the cloud environment (`shared/cloud-environment.md`) and, if the Spark ever pulls analytics, `build/.env`. Never in a note.
5. Add `oauth2.googleapis.com` and `youtubeanalytics.googleapis.com` to the cloud network allowlist.
6. Write `scripts/yt_analytics.py` next to `yt_stats.py`: exchange the refresh token at `https://oauth2.googleapis.com/token` (`grant_type=refresh_token`), call the reports endpoint per video for the week, and write `analytics/stats/<date>-analytics.json` with `{videoId: {avd_s, avp, retention[], search_terms[], traffic{}}}`. Then extend `weekly_retro.py` to read it: retention and search terms go into "What worked" and "Hypotheses", search terms also feed next week's keyword candidates.
7. The Reporting API (bulk daily CSV jobs) is the alternative when per-video report calls get slow; same OAuth, same project.

## Reading the numbers

- Impressions CTR of 2 to 10 % is typical (YouTube's own FAQ). High CTR with low average view duration means the title or thumbnail over-promised; fix the package, not the script.
- Shorts are judged by engaged views and "viewed vs swiped away" (Studio); each video is ranked on its own.
- Views/day across videos of different ages is a rough ranking key; retention is the signal that tells why. Until OAuth exists the retro states patterns only with two or more videos per group.
