# Publish Timing and Slots

Priors from the July 2026 Buffer study (1.8 M videos) and YouTube guidance. Other 2026 studies disagree, so treat these as starting points and let the weekly retro move them.

## Defaults (audience timezone America/Chicago)

| Format | Slots | Rule |
|--------|-------|------|
| Shorts | 11:00 and 18:00 CT daily | never 12:00-17:00 except Friday; Thu/Fri/Sat evenings are the strongest |

`publish.py` computes `scheduledTime` as the next free slot at or after approval plus 30 minutes (Blotato needs the media fetched and processed first). Two Shorts approved the same day take the two slots in order; a third rolls to the next day.

## Frequency

- Shorts: 2 per day.
- Every video is ranked on its own; a weak Short does not drag the next one down.


## What to watch (weekly retro)

Impressions CTR 2-10 % is typical; high CTR with low average view duration means the title or thumbnail over-promised. For Shorts, "viewed vs swiped away" and engaged views are the metrics that matter.
