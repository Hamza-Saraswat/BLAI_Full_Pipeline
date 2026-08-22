# Ideas Note Format (long-form)

```
# Episode ideas: [date]

## Pick
| Slug | Title | Series | Value types | Measures | Opportunity |

## Ranked candidates
| Rank | Title | Series | Keyword | Autocomplete depth | Competition (median views / subs) | vidIQ (volume / competition) | Opportunity | Carries 10 min? |
(5-8 rows; the pick marked with *)

## Keyword notes
One paragraph for the pick: the phrases viewers search, the top competing episodes and their lengths, the gap we fill.

## Decisions
- Pick: why (input lane, rotation, score).
- Runner-up: why not.

## Sources
Radar item ids the pick draws on; the input note it comes from, if any.
```

## Top five for the card

The Telegram FYI parser reads this section (`skills/telegram-gate/rules/cards.md`). One block per rank, exactly this shape:

```
## 1. Can DeepSeek V4 Flash run on 128 GB?
- angle: The FP8 build leaves 40 GB free for context on a DGX Spark.
- why now: DeepSeek shipped V4 Flash 0731 this week.
- format: long
```

Rank 1 is the pick; ranks 2-5 are what a `swap` tap can promote.
