# vidIQ MCP

The vidIQ MCP server at `https://mcp.vidiq.com/mcp` (OAuth) is attached to the two ideas
routines as a custom connector (`shared/cloud-environment.md`). It is the only YouTube-native
demand source in the stack and it spends no Data API quota. The scripts in this skill cannot
reach it: the agent calls it, writes what it learned into the candidate JSON, then runs
`scripts/opportunity_score.py`.

## Finding the tools

Tool names are discovered at run time, not written here: list the server's tools first, then
pick two kinds.

| Kind | Looks like | Used for |
|------|------------|----------|
| keyword research | takes a keyword, returns search volume, a competition figure and an overall score | one call per shortlisted candidate |
| trending | returns rising keywords or videos for a niche or seed | one call per run, seeds new candidates |

Leave title and thumbnail scoring, transcript and comment tools alone during the ideas stage;
they belong to the package stage and to research.

## What to record

Per candidate, straight from the tool's answer, untouched:

```json
"vidiq": {"volume": 12000, "competition": 31, "overall": 71,
          "source_tool": "<tool name as listed>", "fetched_at": "2026-08-25T11:04:00Z"}
```

`volume` is monthly searches, `competition` and `overall` are vidIQ's 0-100 figures. The
opportunity score z-scores `volume` across the candidate set; `competition` and `overall` are
shown in the ideas note as context and are not part of the formula (rules/opportunity-score.md).
When the tool answers with a range or a label ("high"), record the midpoint or the number the
tool gives alongside the label, and say so in the ideas note.

## Budget

About 10 calls per run. Each call costs 5 credits: the Free plan's 150 credits a month allow
about 30 calls, Boost's 2,000 about 400. Order of spending:

1. one trending call for the niche (local AI, DGX Spark), to seed candidates the radar missed
2. keyword research for the candidates with the highest autocomplete `depth_score`, up to 8 or 9
3. stop. Never loop over every autocomplete suggestion; the autocomplete script is free and
   already ranks breadth.

Record the count of calls made in the ideas note so the weekly retro can see the spend.

## When the connector is absent

The connector is missing when the tool list shows no vidIQ tools, or when the first call fails
with an authorization error. Then:

- set `vidiq: null` on every candidate; the score drops the vidIQ column and blends demand from
  autocomplete depth and trend slope only
- write in the ideas note: "vidIQ connector not available this run; demand scored from
  autocomplete (and trend slope where present)"
- never estimate or invent a volume, and never copy last week's figures forward

## trend_slope without vidIQ

`trend_slope` is optional. When a Trends source is attached (SerpApi `google_trends` with
`gprop=youtube`, DataForSEO, or trendsmcp; research section 2.8), record the 90-day slope of
relative interest as a number around -1 to +1. Without one, leave `trend_slope: null`.
