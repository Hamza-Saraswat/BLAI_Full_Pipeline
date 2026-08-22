# Platform Specs

Both formats stay complete here; each workspace's stage contracts point at one row.

## Shorts (workspaces/shorts)

| Spec | Value |
|------|-------|
| Canvas | 1080 x 1920, 30 fps, H.264 / yuv420p, AAC 48 kHz, loudness about -14 LUFS |
| Classification | vertical or square and 180 s or shorter is a Short; no `#Shorts` tag needed |
| Length bands | `classic` 32-38 s (hard max 60); `smooth-explainer` 75-150 s (hard max 180); see `skills/script-gates/formats.json` |
| Safe area | 900 x 1160 centered; nothing that matters in the bottom 450 px or the right 120 px |
| Caption band | y 1260-1470; scene content never enters it |
| Hook | text fully legible at frame 1, a motion onset within 0.5 s, payoff starts by second 4 |
| Visual change | at least every 3 s; no static stretch over 5 s; new information every 5-8 s |
| On-screen text | at most 8 words visible at once; minimum text height about 64 px |
| Ending | final 0.5 s wordmark settle; last frame rhymes with frame 1 (loop anchor) |
| Thumbnail | none (99.9 % of Shorts views come from the feed) |
| Notify subscribers | false |

## Long-form (workspaces/long-form)

| Spec | Value |
|------|-------|
| Canvas | 1920 x 1080, 30 fps, H.264 / yuv420p, AAC 48 kHz, loudness about -14 LUFS |
| Length | 8-20 min target; 1,200-3,000 narration words; chapters at least 3, each at least 60 s |
| Safe area | lower thirds and captions inside 1728 x 972 centered (5 % margins) |
| Captions | SRT sidecar uploaded with the video; burned-in captions only for on-screen terms |
| Chapters | `00:00` first, ascending, each 10 s or longer; list goes in the description |
| Thumbnail | 1280 x 720 or larger, 16:9, JPG or PNG, 2 MB or less; at most 4 words, at most 3 focus areas; 3 variants rendered |
| Hook | first 30 s carry the promise and the first concrete thing; the one surprising number by 0:20 |
| Pacing | new information at least every 30 s; visual change at least every 8 s |
| Notify subscribers | true |
