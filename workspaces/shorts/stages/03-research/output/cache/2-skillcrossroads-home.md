For people who build on Claude Code

# Every skill hits a crossroads before you ship it.

Skill Crossroads grades your Claude Code skills, agents, slash commands, MCP configs, and plugins against an evidence-based rubric -- then points you one of three ways: ship, fix, or rethink.

Scan

[See a sample scorecard](https://skillcrossroads.com/scorecard)

Not on GitHub? [Paste a SKILL.md](https://skillcrossroads.com/paste) -- or scan locally:`npx skillcrossroads ./my-skill`

ShipFixRethink

[Skill Crossroads grade A− -- direction: shipskill crossroadsA−](https://skillcrossroads.com/scorecard)

## A grade is a direction, not a gold star.

ShipA / B

Your artifact is solid. Embed the badge and release with confidence.

FixC / D

Close, but Skill Crossroads found specific problems -- each with the file and line to change.

RethinkF

Deeper issues: it will not trigger, is not safe, or has no way to prove it works.

## How it works

1. 1


   ### Point Skill Crossroads at your artifact.



   `npx skillcrossroads ./my-skill`, a repo URL, or your CI.

2. 2


   ### It runs the rubric.



   Fast deterministic checks plus AI-assisted review across six categories -- every finding cited to a file and line.

3. 3


   ### You get a scorecard, a badge, and a fix list.



   Ranked by how much each fix raises your grade.


## What Skill Crossroads checks

### Correctness & Structure

Valid frontmatter and manifest, resolvable references, nothing pointing at files that do not exist.

### Triggering & Discoverability

Will the model actually invoke it? The number-one reason good skills look broken.

### Clarity & Instructions

Unambiguous, contradiction-free, and phrased as standing instructions.

### Token & Context Cost

What it costs every turn, and whether it uses progressive disclosure.

### Safety & Security

Over-broad tool grants, injection surface, and secrets that should not be there.

### Verifiability & Maintainability

Are there real evals, or tests that only grep the source?

## Receipts, not vibes.

Every finding cites the file and line, and shows what your artifact claims versus what Skill Crossroads could verify. No hype, no false confidence -- Skill Crossroads will tell you when your own skill scores a C, and exactly why.

SKILL.md:1claimed “fires on notes” → verified: under-triggers

Description too generic to fire reliably.

Fix: lead with the use case, add trigger phrases. +14 → A−

## Put the signpost in your README.

One line embeds your Skill Crossroads badge. Anyone who sees it can click through to the full, evidence-cited scorecard -- and run their own. Good work gets shown; the badge does the rest.

[Skill Crossroads grade A− -- direction: shipskill crossroadsA−](https://skillcrossroads.com/scorecard)

```
[![Skill Crossroads: A−](https://skillcrossroads.com/api/badge/OWNER/REPO.svg)](https://skillcrossroads.com/s/OWNER/REPO)
```

## Pricing

### Free

Scan public artifacts and local files, full rubric, local badge, CI GitHub Action + PR gating. This is the whole tool, in the open.

### Pro

Private repos, hosted always-fresh badges, score history, managed AI checks.

### Team

Org-wide custom rules, seats for your team, shared dashboards.

Free covers everything you need to grade and share a public skill.

## The State of Claude Code Skills.

Skill Crossroads publishes evidence-based reports on what actually makes real skills pass or fail across the ecosystem.

[Read the report](https://skillcrossroads.com/report)