---
slug: 2026-09-18-69-of-public-claude-skills-nev
stage: 03-research
topic: "A lint of 216 public Claude Code skills found 69% cannot reliably trigger -- and the fixes are mechanical"
depth: standard
generated_at: 2026-09-18T11:51:36Z
sources: 9
hub: "[[videos/2026-09-18-69-of-public-claude-skills-nev]]"
---

# Research brief: 69% of public Claude Code skills cannot reliably trigger

## Summary

Thesis: skills fail to fire because their one-line description is written like a title instead of a trigger, and rewriting that line before publishing fixes it. Most arresting number: 69% of the 215 public skills the lint could score have a description that will not reliably trigger (87 outright unlikely, 61 borderline). Strongest concrete case: only 1 of 216 audited skills passed every check cleanly while the average score was 82.1/100, proving the failure hides in one line while everything else looks fine. Could not be verified: the community's roughly 50% real-world activation-rate figures (Medium 650-trial experiment, hook success rates), which are tier 4 only and sit under Unverified. Conflict: practitioners claim auto-activation "never works" while official docs describe it as designed behavior with mechanical failure causes; no direct numeric conflict found, and the docs side carries the actionable ground truth.

## Thesis

Most public Claude Code skills never fire because their one-line description is written like a title instead of a trigger, and rewriting that single frontmatter line before publishing fixes it.

## Explanation path

Start where the viewer stands: they installed skills from GitHub, the skills show up when listed, and Claude keeps doing the task without them. Establish how triggering actually works before any numbers: at startup Claude Code loads only the name and description of every installed skill into its context, and the body of the skill is read only after the model decides the request matches that description text. That makes the description the entire selection surface. Now the measurement: Skill Crossroads, a linter for Claude Code artifacts, graded 216 public skills across 18 pinned repositories and its LLM triggering check judged that 69% of the 215 skills it could score have a description that will not reliably trigger, split into 40% outright unlikely to fire and 28% borderline. Explain what failing means in practice, in the lint's own words: the description reads like a title, buries the use case, or omits the natural-language phrases a user would actually say. Then land the myth-bust: the failure is not mysterious model flakiness, it is mechanical, and so is the fix. Ground the fix in official docs: Anthropic's own guidance says the description must state what the skill does and when to use it, that Claude chooses from potentially 100+ skills using that line, that the combined description text is truncated at 1,536 characters in the skill listing, and that malformed YAML silently strips the description so there is nothing to match. The specific anti-pattern the lint counted most: only 52% of skills pass the invocation-cues check, meaning almost half never tell the model when to use them. Close with the mechanical checklist the viewer can run tonight: lead the description with the use case, add the phrases a user would actually say, keep it inside the listing cap, validate the frontmatter, and test with a natural request before shipping.

## Claims

1. **Among the 215 of 216 public Claude Code skills it could score, the Skill Crossroads lint found 69% have a description that will not reliably trigger: 87 (40%) outright unlikely to fire and 61 (28%) borderline.**
   - Source: The State of Claude Code Skills -- Skill Crossroads, https://skillcrossroads.com/report
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "Among skills Skill Crossroads could score, 69% have a description that won't reliably trigger -- 87 (40%) outright unlikely to fire, 61 (28%) borderline."
2. **The audit graded 216 public skills across 18 pinned git repositories on 2026-09-10 under rubric v1.2 with LLM-assisted checks, the average score across all 216 skills is 82.1/100, and 1 of 216 skills passed every check cleanly.**
   - Source: The State of Claude Code Skills -- Skill Crossroads, https://skillcrossroads.com/report
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "The average Skill Crossroads score across all 216 skills is **82.1/100**." and "1 of 216 skills (0%) pass every check Skill Crossroads ran, cleanly."
3. **The most common trigger defect the lint counted is missing invocation cues: only 52% of scored skills pass TRIGGER-03 (invocation cues in description), with 96 warn and 8 fail verdicts, 104 of 215 skills flagged in total.**
   - Source: The State of Claude Code Skills -- Skill Crossroads, https://skillcrossroads.com/report
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "TRIGGER-03 invocation cues in description ██████████░░░░░░░░░░ 52% n=215 (96 warn, 8 fail)"
4. **Official Claude Code docs state Claude uses the frontmatter description to decide when to apply a skill, and the combined description and when_to_use text is truncated at 1,536 characters in the skill listing.**
   - Source: Extend Claude with skills - Claude Code Docs, https://code.claude.com/docs/en/skills
   - Tier: primary | Confidence: high | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "Claude uses this to decide when to apply the skill. ... the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage."
5. **The official troubleshooting guide says that if Claude does not use your skill you should check the description includes keywords users would naturally say, and that malformed frontmatter YAML makes Claude Code load the skill body with empty metadata so Claude cannot match against the description at all.**
   - Source: Extend Claude with skills - Claude Code Docs, https://code.claude.com/docs/en/skills
   - Tier: primary | Confidence: high | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "If the frontmatter YAML is malformed, Claude Code loads the skill body with empty metadata, so `/skill-name` still works but Claude can't match against your `description`."
6. **Anthropic's authoring best practices say the description is critical for skill selection because Claude uses it to choose the right Skill from potentially 100+ available Skills, and explicitly tells authors to avoid vague descriptions such as "Helps with documents".**
   - Source: Skill authoring best practices - Claude Platform Docs, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
   - Tier: primary | Confidence: high | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "The description is critical for skill selection: Claude uses it to choose the right Skill from potentially 100+ available Skills."
7. **Anthropic's engineering blog explains the selection mechanism: at startup the agent pre-loads only the name and description of every installed skill into its system prompt, and if Claude thinks the skill is relevant it then loads the full SKILL.md into context.**
   - Source: Equipping agents for the real world with Agent Skills - Anthropic, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
   - Tier: primary | Confidence: high | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "At startup, the agent pre-loads the `name` and `description` of every installed skill into its system prompt."
8. **Practitioners independently corroborate the failure mode: developer Scott Spence documented skills that list fine but never activate even when queries exactly match their descriptions, citing GitHub issue 9716 where multiple people report Claude Code is not automatically discovering or prioritizing available skills.**
   - Source: Claude Code Skills Don't Auto-Activate (a workaround) - Scott Spence, https://scottspence.com/posts/claude-code-skills-dont-auto-activate
   - Tier: community | Confidence: medium | Accessed: 2026-09-18 | Via: web_extract
   - Quote: "Even when users' queries _exactly matched_ skill descriptions, Claude would just... ignore the skill and do the work manually."

## Key numbers

| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | scored skills whose description will not reliably trigger (share of 215 scored) | 69% | https://skillcrossroads.com/report | "69% have a description that won't reliably trigger" |
| 2 | skills outright unlikely to fire | 87 (40%) | https://skillcrossroads.com/report | "87 (40%) outright unlikely to fire" |
| 3 | skills borderline for triggering | 61 (28%) | https://skillcrossroads.com/report | "61 (28%) borderline" |
| 4 | share of skills passing the invocation-cues check (TRIGGER-03) | 52% | https://skillcrossroads.com/report | "TRIGGER-03 invocation cues in description ... 52% n=215 (96 warn, 8 fail)" |
| 5 | skills passing every check cleanly | 1 of 216 | https://skillcrossroads.com/report | "1 of 216 skills (0%) pass every check Skill Crossroads ran, cleanly." |
| 6 | average Skill Crossroads score across all 216 skills | 82.1/100 | https://skillcrossroads.com/report | "The average Skill Crossroads score across all 216 skills is 82.1/100." |
| 7 | character cap on combined description and when_to_use text in the Claude Code skill listing | 1,536 characters | https://code.claude.com/docs/en/skills | "truncated at 1,536 characters in the skill listing" |

## Analogy candidates

- **Help-wanted posting on a crew board**: the description is a one-line job posting the foreman (Claude) scans to decide who to call in; the SKILL.md body is the worker who only shows up once picked, and a posting that reads "helpful person" never gets called. Breaks when: a human reads a job posting once and deliberates, while the model re-reads every description each turn against a character budget that can silently cut the posting off after 1,536 characters, so a good line buried at the end can vanish before it is ever compared.
- **Unlabeled spice jars**: installing skills is stocking a rack of jars; triggering is the cook picking the right jar by its label alone, and the lint found most jars have vague labels, so the contents are fine but the jar never gets picked. Breaks when: a human cook can open a jar, smell it, or remember what is inside, while at selection time the model has nothing but the label text and there is no opening the jar before choosing.

## Misconceptions

- Myth: If the skill is installed and shows up when I list my skills, Claude will use it when it is relevant. Reality: Listed and firing are separate steps; the model matches your request against the description text only, and the lint judged 69% of scored public descriptions unable to reliably trigger (claim 1).
- Myth: Skills failing to fire means the model is flaky or the feature is broken. Reality: The official docs give mechanical causes and mechanical fixes; the description must contain the keywords users would naturally say, malformed YAML silently strips the description, and overlong description text is truncated in the listing (claims 4 and 5).

## Glossary

- **Claude Code**: Anthropic's terminal coding agent, which loads skills from folders on your machine.
- **Agent Skill**: A folder whose SKILL.md file gives the agent instructions it loads only when the task is relevant.
- **SKILL.md**: The one required file in a skill: YAML frontmatter (name, description) plus markdown instructions.
- **frontmatter**: The YAML block between --- markers at the top of SKILL.md that holds the metadata Claude matches against.
- **description field**: The one frontmatter line stating what the skill does and when to use it, which Claude reads to decide whether to invoke the skill.
- **when_to_use**: An optional frontmatter field for trigger phrases and example requests, appended to the description in the skill listing.
- **triggering**: The model choosing to load a skill because your request matches its description text.
- **progressive disclosure**: The design where only skill names and descriptions load at startup, and the body and bundled files load only when needed.
- **invocation cues**: Phrases in a description that tell the model when to use the skill, like "use when the user asks to parse a PDF".
- **linter**: A static checker that flags mechanical defects in files before you ship them; here, Skill Crossroads grades SKILL.md artifacts.

## Unverified

- A Medium experiment (650 trials, 3 skills, replication with N=3 per cell) reports roughly 50% baseline auto-activation and 100% activation with directive descriptions; these activation rates are community-only and not corroborated by a tier 1-3 source in this run.
- Scott Spence reports hook-driven skill activation succeeding 4 of 10 times globally and 5 of 10 times locally on his setup; community-only.
- LazySkills relays GitHub issue reports of installs of 137 skills where only 116 load because descriptions overflow the context budget; community-only and secondhand.
- The claim that skills never auto-activate is one practitioner's experience with a specific setup; official docs describe model-invoked skills and give mechanical reasons they fail to fire.
- How reliably skills trigger on our own machines (the DGX Spark or a viewer's gaming PC) has not been measured by us and should not be asserted.

## Suggested outline

1. Hook with the number: a lint of 216 public Claude Code skills found 69% cannot reliably trigger, and the hiding place is one line of text.
2. Reveal the mechanism: at startup Claude loads only each skill's name and description, your request is matched against that one line, and the skill body loads after -- so the description is the whole selection surface.
3. Land the mechanical fix: lead the description with what the skill does plus "use when" trigger phrases a user would actually say, keep it inside the 1,536-character listing cap, validate the frontmatter before shipping, and test with a natural request.

## Viewer situation

You've got Claude Code installed, you've dropped a few skills from GitHub into your skills folder, they show up when you list them, and Claude keeps just doing the task without ever touching them.

## Has process

true

- Open the skill's SKILL.md and read the description line, checking whether it names what the skill does and when to use it.
- Rewrite the description to lead with the use case and the exact phrases a user would naturally say when they want the skill.
- Validate the frontmatter and description before publishing, for example with npx skillcrossroads ./my-skill or any YAML linter.
- Start a fresh session and test with a natural request, confirming the skill fires without invoking it by name.

## Objection

The 69% number is one linter's LLM judging description text on a 216-skill sample, not Claude actually failing in production, and its own report says LLM verdicts are not bit-reproducible across runs.

## Sources

| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://skillcrossroads.com/report | The State of Claude Code Skills -- Skill Crossroads | benchmark | web_extract | 2026-09-18 |
| 2 | https://skillcrossroads.com | Skill Crossroads -- Know before you ship. | benchmark | web_extract | 2026-09-18 |
| 3 | https://code.claude.com/docs/en/skills | Extend Claude with skills - Claude Code Docs | primary | web_extract | 2026-09-18 |
| 4 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | Skill authoring best practices - Claude Platform Docs | primary | web_extract | 2026-09-18 |
| 5 | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | Equipping agents for the real world with Agent Skills - Anthropic | primary | web_extract | 2026-09-18 |
| 6 | https://scottspence.com/posts/claude-code-skills-dont-auto-activate | Claude Code Skills Don't Auto-Activate (a workaround) - Scott Spence | community | web_extract | 2026-09-18 |
| 7 | https://medium.com/@ivan.seleznov1/why-claude-code-skills-dont-activate-and-how-to-fix-it-86f679409af1 | Why Claude Code Skills Don't Activate -- And How to Fix It - Medium | community | web_extract | 2026-09-18 |
| 8 | https://lazyskills.sh/troubleshooting/skills-not-triggering | Claude Code Skill Not Triggering? 8 Causes and Their Fixes - LazySkills | community | web_extract | 2026-09-18 |
| 9 | https://hn.algolia.com/api/v1/items/49744398 | Show HN: Linting 216 public Claude Code skills -- 69% won't reliably trigger (HN item 49744398) | community | terminal curl | 2026-09-18 |

## Notes

The 69% figure is LLM-judged (TRIGGER-01) on 215 of 216 skills; the report states deterministic figures are bit-reproducible from pinned git trees but LLM verdicts are not guaranteed identical across runs -- say "a lint judged" rather than "a test proved" in narration. Letter grades cluster high (72% of skills scored a B, average 82.1/100) because structure and safety are largely table stakes; triggering and verifiability are where the sample falls down (evals present: 0% pass cleanly), which supports the "fixes are mechanical" angle. The audit was posted to Hacker News on 2026-09-17 ("Show HN: Linting 216 public Claude Code skills -- 69% won't reliably trigger", 3 points, 0 comments as of 2026-09-18), so community pickup is thin and the report itself is the load-bearing source. Sample includes Anthropic's own anthropics/skills catalog, which blunts the "community skills are just sloppy" counterargument. No direct conflicts found between docs and the lint; the only tension is practitioners claiming auto-activation never works versus docs describing it as designed behavior with mechanical failure causes.
