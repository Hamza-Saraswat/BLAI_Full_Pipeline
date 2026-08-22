# Opportunity Score

`scripts/opportunity_score.py` implements this file (research section 2.8: opportunity is demand
over competition, each a z-blend, with a named-product bonus). Change the two together.

## Inputs per candidate

| Field | From | Used as |
|-------|------|---------|
| `autocomplete.depth_score` | `autocomplete.py` | demand, linear |
| `vidiq.volume` | vidIQ MCP (`rules/vidiq-mcp.md`), or `vidiq: null` | demand, log10(1 + x) |
| `trend_slope` | a Trends source when attached, else `null` | demand, linear |
| `competition.median_views` | `competition.py` | competition, log10(1 + x) |
| `competition.median_subs` | `competition.py` | competition, log10(1 + x) |
| `competition.share_recent_180d` | `competition.py` | competition, linear |
| `competition.exact_title_rate` | `competition.py` | competition, linear |
| `competition.small_channel_velocity` | `competition.py` | +5 bonus test only |
| `named_product` | the agent: true when the keyword names a product or model | +10 bonus |

Counts (volume, views, subscribers) are log-scaled before z-scoring so one viral outlier does
not flatten the rest of the set. `vidiq.competition` and `vidiq.overall` are recorded for the
ideas note but are not in the formula.

## Formula

1. For every column above, compute population z-scores across the candidate set
   (`z = (x - mean) / sd`). Missing values stay missing; a column with fewer than two present
   values, or a flat column, scores 0 for everyone who has it.
2. `demand = mean of the present z among depth_score, vidiq_volume, trend_slope`
   (0 when none is present).
3. `competition = mean of the present z among median_views, median_subs, share_recent_180d,
   exact_title_rate` (higher means more competition; 0 when none is present).
4. `base = clip(50 + 15 * (demand - competition), 0, 100)`.
5. `+10` when `named_product` is true.
6. `+5` when `small_channel_velocity` is above the median of the set's present velocities
   (small channels already winning on the keyword means demand exceeds supply).
7. `opportunity = clip(base + bonuses, 0, 100)`, rounded to one decimal.
8. Rank by opportunity descending, ties by demand descending, then keyword.

A candidate at the set's average on everything scores 50; each full standard deviation of net
advantage moves it 15 points. Scores only mean something inside one candidate set: compare
candidates from the same run, never across runs.

## Output per candidate

`demand`, `competition_score`, `opportunity`, `rank`, `bonuses {named_product,
small_channel_velocity}` and `z {depth_score, vidiq_volume, trend_slope, median_views,
median_subs, share_recent_180d, exact_title_rate}` (null where the input was missing), added to
the original object. The list is written sorted by rank.

## Worked example (fixtures/candidates.json, six candidates)

Candidate: `deepseek v4 flash dgx spark`, depth_score 9, vidiq volume 12,000, trend_slope 0.8,
median_views 4,200, median_subs 18,000, share_recent_180d 0.9, exact_title_rate 0.15,
small_channel_velocity 820, named_product true.

| Column | z |
|--------|---|
| depth_score | -0.5335 (9 is below the set's mean of about 14) |
| vidiq_volume | -0.1571 (log scale; 12,000 sits just under the set's mean) |
| trend_slope | +1.3544 (0.8 is the strongest slope in the set) |
| median_views | -0.4863 |
| median_subs | -0.4524 |
| share_recent_180d | +0.6727 (many fresh videos: the topic is contested) |
| exact_title_rate | -0.8662 (few titles carry the whole phrase: a gap) |

- demand = mean(-0.5335, -0.1571, +1.3544) = +0.2213
- competition = mean(-0.4863, -0.4524, +0.6727, -0.8662) = -0.2831
- base = 50 + 15 * (0.2213 + 0.2831) = 57.57
- named product: +10; velocity 820 is above the set median 275: +5
- opportunity = 72.6, rank 1 of 6

The same set ranks `ollama vs llama.cpp` second at 63.9 (highest demand, +0.65, but strong
competition, +0.39, and slow small channels), `dgx spark firmware` third at 57.7 (thin demand,
-0.84, rescued by weak competition and both bonuses), and `llm quantization explained` last at
46.9 (average demand, above-average competition, no product, no bonus). `dgx spark firmware`
shows the missing-value rule: with `vidiq: null` and `trend_slope: null` its demand is the
depth_score z alone.

## Reading the result

- 65 and above with a named product: take it to research.
- 50 to 65: viable when the title can carry a product name, otherwise look for a long-tail
  suggestion from the autocomplete list.
- Below 50: generic or saturated; skip unless the radar's why-now is strong enough to win on
  browse rather than search.
- `exact_title_rate` above 0.7 together with `median_subs` above 100,000 means big channels own
  the exact phrase; prefer a narrower keyword even when the score is decent.
