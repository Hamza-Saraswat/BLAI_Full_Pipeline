# Publish Timing and Slots

Priors from the July 2026 Buffer study (1.8 M videos) and YouTube guidance. Other 2026 studies disagree, so treat these as starting points and let the weekly retro move them.

## Defaults (audience timezone America/Chicago)

| Format | Slots | Rule |
|--------|-------|------|
| Shorts | 11:00 and 18:00 CT daily | never 12:00-17:00 except Friday; Thu/Fri/Sat evenings are the strongest |
| Long-form | next 09:00 CT after approval; Sunday 10:00 CT when the approval lands on Saturday | weekday 08:00-11:00 window; avoid weekday 13:00-17:00 |

`publish.py` computes `scheduledTime` as the next free slot at or after approval plus 30 minutes (Blotato needs the media fetched and processed first). Two Shorts approved the same day take the two slots in order; a third rolls to the next day.

## Frequency

- Shorts: 2 per day, separate schedule from long-form.
- Long-form: target 3 per week (Mon/Wed/Fri production); ramping 1 -> 2 -> 3 while the format settles is recommended.
- A weak Short does not hurt the next long-form video; Shorts and long-form are ranked per video.

## Captures on the Spark

Experiment captures (long-form stage 08) run in the night window 01:00-06:00 CT by default so they do not compete with the creator's own GPU work. Override per run by setting `capture_window: any` in the hub note.

## What to watch (weekly retro)

Impressions CTR 2-10 % is typical; high CTR with low average view duration means the title or thumbnail over-promised. For Shorts, "viewed vs swiped away" and engaged views are the metrics that matter.
