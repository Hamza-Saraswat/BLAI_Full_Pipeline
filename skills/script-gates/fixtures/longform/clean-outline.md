---
slug: seventy-b-on-the-spark
series: my-dgx-spark-projects
structure: build-along
value_types: EQUIPS, PROVES
target_minutes: 5
---

# Outline: Serving a 70B model on the Spark

Fixture: the outline `clean-script.md` was written from. Trimmed to five target minutes.

## Angle
A seventy-billion-parameter model fits on the Spark, and the thing that stops it is the cache, not the weights.

## Value brief
- EQUIPS: the context flag to set before the first request, and what to watch while it runs
- PROVES: twenty-eight tokens a second at a context of eight thousand, measured on our box
- Hook: I loaded it, it answered at four tokens a second, and nothing in the log said why
- Payoff: twenty-eight tokens a second after one flag
- The number by 0:20: a hundred and twenty-eight gigabytes of unified memory

## Chapters
| # | Chapter | Target s | The one idea | Measurement shown | Muted viewer understands |
|---|---------|----------|--------------|-------------------|--------------------------|
| 1 | The goal | 66 | The arithmetic says it fits | none | two numbers, one inside the other |
| 2 | The setup | 62 | It ran, and it ran wrong | first token rate | a counter crawling |
| 3 | Where it fell over | 63 | The cache is a running cost | cache size | one block shoving another off the bar |
| 4 | The fix and the number | 62 | One flag moves the whole result | tokens per second | the counter climbing to twenty-eight |
| 5 | What to copy | 63 | Set the context to the workload | none | one copyable command |

## Visual philosophy
Terminal replays carry chapters 2 and 4, because the failure and the fix are both things the box says out loud. Diagrams carry chapter 3, where the memory split is the whole idea. Everything else stays typographic, one number at a time.

## Decisions
- Shape: `build-along` over `concept-deep-dive`, because the failure is real and measured. Judge totals 19 to 15.
