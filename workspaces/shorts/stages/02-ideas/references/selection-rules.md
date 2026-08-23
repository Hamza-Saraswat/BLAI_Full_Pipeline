# Selection Rules

## Picks per day

2. Both picks get a hub note and go through research, script and package the same morning.

## Format mix

Pick the band by fit, not by turn-taking. Bands are defined in `skills/script-gates/formats.json`.

| Take `classic` (32-38 s) when | Take `smooth-explainer` (75-150 s) when |
|---|---|
| the idea is one fact and one consequence | the idea needs a worked example carried the whole way |
| the number does the work on its own | the viewer has to follow a state changing three or more times |
| it is a release, a price change or a correction | it is a mechanism, a process, or a belief that needs dismantling |
| a viewer could act on it in one sentence | the honest catch needs its own beat |

Two soft constraints, in this order: the two picks of one day should not share a band, and no band runs three days straight. Fit wins over both; when it does, say so in the Decisions block.

## Ranking

1. Sort candidates by `opportunity` (0-100) from `opportunity_score.py`.
2. Discard candidates whose title names no product, model or tool.
3. Discard candidates already covered by a published Short or a hub note in the last 30 days (same product and same angle).
4. Prefer candidates whose radar items come from two or more sources.

## Rotation

- The two picks must come from different lanes.
- Neither lane may repeat yesterday's picks' lanes unless no other candidate scores above 60.
- At most one `news-react` per day; a second news item becomes a `comparison` or `myth-bust` angle if it still qualifies.
- Carry a "corrections" candidate (an item that contradicts a published claim) to the top 5 whenever one exists.

## Value tags

Exactly two of TEACHES, EQUIPS, REFRAMES, PROVES. PROVES only when the brief will carry a measurement from our own hardware or a cited benchmark.

## Ties and empties

On a tie, pick the candidate with the higher autocomplete depth. If fewer than two candidates score above 50, take the best two anyway and say so in the Decisions block; a quiet news day is a day for an evergreen explainer from the pillar list.
