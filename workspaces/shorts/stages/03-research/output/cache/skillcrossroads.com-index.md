> Fetched web_extract on 2026-09-18. URL: https://skillcrossroads.com

# Skill Crossroads -- Know before you ship.

For people who build on Claude Code

# Every skill hits a crossroads before you ship it.

Skill Crossroads grades your Claude Code skills, agents, slash commands, MCP configs, and plugins against an evidence-based rubric -- then points you one of three ways: ship, fix, or rethink.

Scan: `npx skillcrossroads ./my-skill`

Not on GitHub? Paste a SKILL.md -- or scan locally.

## A grade is a direction, not a gold star.

Ship A / B: Your artifact is solid. Embed the badge and release with confidence.
Fix C / D: Close, but Skill Crossroads found specific problems -- each with the file and line to change.
Rethink F: Deeper issues: it will not trigger, is not safe, or has no way to prove it works.

## How it works

1. Point Skill Crossroads at your artifact. `npx skillcrossroads ./my-skill`, a repo URL, or your CI.
2. It runs the rubric. Fast deterministic checks plus AI-assisted review across six categories -- every finding cited to a file and line.
3. You get a scorecard, a badge, and a fix list. Ranked by how much each fix raises your grade.

## What Skill Crossroads checks

Correctness & Structure: Valid frontmatter and manifest, resolvable references, nothing pointing at files that do not exist.
Triggering & Discoverability: Will the model actually invoke it? The number-one reason good skills look broken.
Clarity & Instructions: Unambiguous, contradiction-free, and phrased as standing instructions.
Token & Context Cost: What it costs every turn, and whether it uses progressive disclosure.
Safety & Security: Over-broad tool grants, injection surface, and secrets that should not be there.
Verifiability & Maintainability: Are there real evals, or tests that only grep the source?

## Receipts, not vibes.

Every finding cites the file and line, and shows what your artifact claims versus what Skill Crossroads could verify.

SKILL.md:1 claimed "fires on notes" -> verified: under-triggers
Description too generic to fire reliably.
Fix: lead with the use case, add trigger phrases. +14 -> A-

## The State of Claude Code Skills.

Skill Crossroads publishes evidence-based reports on what actually makes real skills pass or fail across the ecosystem.
