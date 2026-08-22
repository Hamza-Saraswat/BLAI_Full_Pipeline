# Ideas Note Format

```
# Ideas: [date]

## Picks
| # | Slug | Title | Lane | Format | Value types | Opportunity |
|---|------|-------|------|--------|-------------|-------------|
| 1 | ... | ... | ... | classic | TEACHES, PROVES | 78 |
| 2 | ... | ... | ... | smooth-explainer | EQUIPS, REFRAMES | 71 |

## Ranked candidates
| Rank | Title | Lane | Keyword | Autocomplete depth | Competition (median views / subs) | vidIQ (volume / competition) | Opportunity | Why now |
|------|-------|------|---------|--------------------|------------------------------------|-------------------------------|-------------|---------|
(8-12 rows; the two picks marked with *)

## Keyword notes
One short paragraph per pick: the search phrase a viewer types, the top competing titles, the gap we fill.

## Decisions
- Picks: why these two (lane rotation, scores, corrections).
- Skipped: the best candidate not picked and why.

## Sources
The radar item ids each pick draws on.
```

Rules: titles in this note are working titles; the package stage writes the final ones. Every number in the table comes from a script's output, never typed from memory.

## Top five for the card

The Telegram FYI parser reads this section (`skills/telegram-gate/rules/cards.md`). One block per rank, exactly this shape:

```
## 1. Can DeepSeek V4 Flash run on 128 GB?
- angle: The FP8 build leaves 40 GB free for context on a DGX Spark.
- why now: DeepSeek shipped V4 Flash 0731 this week.
- format: smooth-explainer
```

Ranks 1 and 2 are the picks; ranks 3-5 are what a `swap` tap can promote.
