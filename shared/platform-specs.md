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

