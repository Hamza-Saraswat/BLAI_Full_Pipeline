[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40ivan.seleznov1%2Fwhy-claude-code-skills-dont-activate-and-how-to-fix-it-86f679409af1&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40ivan.seleznov1%2Fwhy-claude-code-skills-dont-activate-and-how-to-fix-it-86f679409af1&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

[Claude](https://medium.com/tag/claude?source=post_page---header_tags--86f679409af1-----------------------------------------)

[Skills](https://medium.com/tag/skills?source=post_page---header_tags--86f679409af1-----------------------------------------)

[AI Agent](https://medium.com/tag/ai-agent?source=post_page---header_tags--86f679409af1-----------------------------------------)

[Prompt Engineering](https://medium.com/tag/prompt-engineering?source=post_page---header_tags--86f679409af1-----------------------------------------)

[Software Development](https://medium.com/tag/software-development?source=post_page---header_tags--86f679409af1-----------------------------------------)

# Why Claude Code Skills Don’t Activate -- And How to Fix It

[![Ivan Seleznov](https://miro.medium.com/v2/da:true/resize:fill:32:32/0*Lf8CYZhO0sY0PR7i)](https://medium.com/@ivan.seleznov1?source=post_page---byline--86f679409af1-----------------------------------------)

[Ivan Seleznov](https://medium.com/@ivan.seleznov1?source=post_page---byline--86f679409af1-----------------------------------------)

Follow

11 min read

·

Feb 5, 2026

75

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D86f679409af1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ivan.seleznov1%2Fwhy-claude-code-skills-dont-activate-and-how-to-fix-it-86f679409af1&source=---header_actions--86f679409af1---------------------post_audio_button--------------------)

Share

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*vZSLkRy322edEDVT3F2iXA.jpeg)

Article Preview Image (generated with gemini-3-pro-image-preview)

## TL;DR

**Problem**: Claude Code skills have unreliable auto-activation (~50% baseline in the wild)

**Experiment**: 650 automated trials testing 3 description variants × 4 environment conditions

**Key Finding**: Directive descriptions (“ALWAYS invoke…Do not X directly”) achieve 100% activation; standard descriptions drop to 37% with hooks

**Recommendation**: Use the SKILL.md template provided below with explicit triggers and negative constraints

## Introduction & Motivation

## The Promise vs Reality

Anthropic’s documentation claims skills are “model-invoked” and “autonomously decided” -- the model should intelligently recognize when a skill is relevant and invoke it automatically.

Reality: “Claude Code skills just sit there. You have to remember to use them.”

Developers report approximately 50% activation rate -- essentially a coin flip whether your carefully crafted skill will be used when relevant.

## Community Workarounds

**Scott Spence** documented this problem extensively. In [Claude Code Skills Don’t Auto-Activate](https://scottspence.com/posts/claude-code-skills-dont-auto-activate), he observed that even when queries precisely matched skill descriptions, Claude ignored skills:

> _“Claude Code is not automatically discovering or prioritizing available skills”_

In a follow-up article, [How to Make Claude Code Skills Activate Reliably](https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably), he built a testing framework with 200+ prompts and found that a “forced eval hook” achieved 84% activation through a complex 3-step commitment mechanism:

> _“The difference is the commitment mechanism”_

The [Limor AI Claude Hooks implementation](https://github.com/ytrofr/claude-code-implementation-guide/blob/main/examples/limor-ai-claude-hooks/hooks/pre-prompt.sh) took an even more elaborate approach: synonym expansion, hybrid scoring, caching, 70+ predefined patterns, and a weighted scoring algorithm. This shows how complex solutions become when the root cause isn’t addressed.

## Research Question

Can we fix activation through better SKILL.md descriptions alone, without complex hooks?

## How We Got Here: Evolution of the Experiment

The final experimental design didn’t appear fully formed. It emerged through a series of failed interventions, each one narrowing the search space until we found the actual lever.

## Step 1: Establishing the Baseline

We started by measuring what happens out of the box. Three skills were registered with their default [SKILL.md descriptions](https://github.com/SeleznovIvan/claude-skills-test/tree/main/skills) (the ones Anthropic’s documentation suggests), and we ran automated queries against them with no other configuration. ( [baseline data](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/01-baseline))

**Result**: ~50% activation rate. Half the time, Claude just did the work directly instead of invoking the skill. This confirmed the community reports weren’t anecdotal -- the problem is real and reproducible.

## Step 2: Adding Project Context (CLAUDE.md)

The first hypothesis was that Claude might need more context about the project to know skills are important. A `CLAUDE.md` file sits at the project root and tells Claude about the project's purpose and conventions. Maybe if Claude understood the project better, it would recognize when to use skills.

**Result**: +15 percentage points improvement (to ~65%). Better, but still failing a third of the time. Project context helps, but it’s not enough on its own. ( [CLAUDE.md experiment data](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/02-claude-md))

## Step 3: Adding Keywords to SKILL.md

SKILL.md frontmatter supports a `keywords` field. The hypothesis was that adding more keyword matches might help Claude's routing logic find the right skill.

**Result**: 0 percentage point change. Keywords had zero measurable effect on activation. The model doesn’t appear to use them for routing decisions. This was a dead end.

## Step 4: Testing Pre-Prompt Hooks

Community solutions like Scott Spence’s “forced eval hook” and Limor AI’s scoring system use hooks -- shell commands that run before each prompt and inject instructions telling Claude to check for relevant skills. These are the most popular workarounds, so we tested a [scoring-based pre-prompt hook](https://github.com/SeleznovIvan/claude-skills-test/blob/main/scripts/skill-scoring-hook.sh).

**Result**: Activation actually **dropped by 30 percentage points** in some configurations. The hook injected competing instructions that confused the model. Instead of clarifying “use the Skill tool,” the hook was interpreted as “do this kind of work” -- and Claude did the work directly. This was the most surprising finding of the early experiments.

## Step 5: The Pivot -- Examining the Description Field

At this point, we had tried everything _around_ the skill (project context, keywords, hooks) and none of it reliably worked. The one thing we hadn’t varied was the `description:` field in SKILL.md frontmatter itself -- the single line of text that tells Claude what the skill does and when to use it.

We tested [3 description variants](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/04-description):

- [**Variant A (Current)**](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/04-description/variant-a-current): The default passive style -- “Docker expert for containerization. Use when…”
- [**Variant B (Expanded)**](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/04-description/variant-b-expanded): Same style but with more trigger keywords -- “…or any Docker-related task”
- [**Variant C (Directive)**](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/04-description/variant-c-directive): Imperative commands with a negative constraint -- “ALWAYS invoke…Do not X directly”

**Result**: Variant C achieved 100% activation in no-hook conditions. Variant A sat at 77%. The description wording was the lever all along.

## Step 6: Replication

The initial experiment had N=1 per cell (216 total sessions). Promising, but it could be statistical noise or model variance. To make publishable claims, we needed larger samples with proper statistical tests -- hence the [replication experiment](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/05-replication): N=3 per cell, 650 total trials, with Fisher’s exact test, logistic regression, and Cochran-Mantel-Haenszel stratified analysis.

## SKILL.md Description Template

## The Template

```
---
name: <skill-name>
description: <Domain> expert. ALWAYS invoke this skill when the user asks about <trigger topics>. Do not <alternative action> directly -- use this skill first.
---
```

**Components:**

1. **Domain identifier**: “Docker and containerization expert”
2. **ALWAYS invoke**: Directive keyword (not “Use when” -- that’s a suggestion)
3. **Trigger topic list**: Comprehensive but not exhaustive
4. **Negative constraint**: “Do not \[what Claude would do instead\] directly”

## Example: What Failed vs What Works

**FAILED -- Variant A (37% activation with hooks):**

```
description: Docker expert for containerization. Use when creating Dockerfiles, containerizing applications, or configuring Docker images.
```

**FAILED -- Variant B (also poor without CLAUDE.md):**

```
description: Docker and containerization expert. Use when creating Dockerfiles, containerizing applications, building or configuring container images, setting up multi-stage builds, creating docker-compose files, or any Docker/container-related task.
```

**WORKS -- Variant C (100% activation):**

```
description: Docker and containerization expert. ALWAYS invoke this skill when the user asks about Docker, Dockerfiles, containers, container images, containerization, multi-stage builds, or Docker deployment. Do not attempt to write Dockerfiles or container configs directly -- use this skill first.
```

## Why It Works

The combination of **positive routing** (“ALWAYS invoke”) + **negative constraint** (“Do not X directly”) is what makes Variant C uniquely effective:

- “ALWAYS invoke” alone: Claude might still bypass for “simple” tasks
- “Do not X” alone: Claude doesn’t know what to do instead
- Together: Unambiguous instruction with blocked escape path

## Experimental Design

## Independent Variables

**Description Variants (A, B, C):**

```
Variant      | Style               | Key Difference
-------------|---------------------|--------------------------------------
A: Current   | Passive, informative| "Use when..."
B: Expanded  | More keywords       | "...or any X-related task"
C: Directive | Imperative          | "ALWAYS invoke...Do not X directly"
```

**Environment Conditions (C1–C4):**

```
Condition      | CLAUDE.md | Hook | Description
---------------|-----------|------|------------------------
C1: Bare       | No        | No   | Minimal setup
C2: +CLAUDE.md | Yes       | No   | Project context file
C3: +Hook      | No        | Yes  | Pre-prompt hook active
C4: +Both      | Yes       | Yes  | Full configuration
```

## Test Prompt Generation

**Why 18 prompts across 3 skills?**

Each skill needs queries with varying specificity (explicit vs implicit triggers). Six queries per skill covers: exact name matches, keyword triggers, synonym triggers, and edge cases.

Skills chosen to cover different domains:

- **dockerfile-generator**: containerization
- **git-workflow**: version control
- **svelte5-runes**: frontend framework

## Full Test Suite

Each query is designed to test a different activation trigger -- from explicit skill name mentions to vague requests where Claude has to infer intent. The `why` field documents the reasoning behind each query choice. ( [test-cases.json](https://github.com/SeleznovIvan/claude-skills-test/blob/main/test-cases.json))

## Get Ivan Seleznov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

**dockerfile-generator** (6 queries):

```
Query                                | Why This Query
-------------------------------------|--------------------------------------
"write a dockerfile"                 | Unique task -- only docker skill
"generate dockerfile for node app"   | Docker + app context
"containerize my application"        | Container synonym trigger
"create docker image config"         | Docker image context
"help with multi-stage docker build" | Docker build optimization
"setup dockerfile for python flask"  | Dockerfile for specific stack
```

**git-workflow** (6 queries):

```
Query                                      | Why This Query
-------------------------------------------|--------------------------------------
"resolve git merge conflict"               | Unique domain -- only git skill
"help with git rebase"                     | Git rebase assistance
"fix my git history"                       | Git history task
"squash commits before PR"                 | Git squash workflow
"undo last git commit"                     | Git recovery task
"cherry pick a commit from another branch" | Advanced git operation
```

**svelte5-runes** (6 queries):

```
Query                                | Why This Query
-------------------------------------|--------------------------------------
"use svelte5 runes"                  | Explicit skill name mention
"create reactive state with $state"  | Unique keyword $state
"convert svelte 4 to svelte 5"      | Migration task with svelte 5
"use $derived and $effect"           | Multiple unique rune keywords
"how do I use runes in svelte"       | Direct runes question
"svelte 5 component with $props"     | Props rune usage
```

## Experiment Configuration

The replication experiment was driven by a single [config file](https://github.com/SeleznovIvan/claude-skills-test/blob/main/experiments/05-replication/data/config.json) that defined the full factorial design:

```
{
  "experiment": "replication-v2",
  "reps": 3,
  "seed": 42,
  "max_turns": 5,
  "delay_ms": 2000,
  "variants": ["a", "b", "c"],
  "conditions": ["c1", "c2", "c3", "c4"],
  "condition_matrix": {
    "c1": { "claude_md": false, "hook": false },
    "c2": { "claude_md": true,  "hook": false },
    "c3": { "claude_md": false, "hook": true },
    "c4": { "claude_md": true,  "hook": true }
  },
  "skills": ["dockerfile-generator", "git-workflow", "svelte5-runes"],
  "queries_per_skill": 6,
  "total_queries": 18,
  "total_sessions": 648
}
```

This produces 3 variants × 4 conditions × 18 queries × 3 repetitions = 648 planned sessions (650 actual due to two retried error sessions).

## Why Multiple Trials (N=3 per cell)

**Addressing stochasticity:**

- LLMs have inherent randomness in responses
- Single trial (N=1) can’t distinguish signal from noise
- N=3 provides 54 trials per condition (18 queries × 3 reps) for statistical power

**Statistical benefits:**

- Can compute confidence intervals
- Can run Fisher’s exact test for significance
- Can detect if effects are consistent across replications

## Automated CLI Execution

**Methodology:**

```
claude -p "<query>" --max-turns 5 --allowedTools "Skill" --output-format json
```

- `--max-turns 5`: Allows sufficient turns for skill invocation
- `--allowedTools "Skill"`: Restricts to Skill tool to measure activation intent
- Automated orchestration: [Shell script](https://github.com/SeleznovIvan/claude-skills-test/blob/main/experiments/05-replication/run-experiment-v2.sh) swaps SKILL.md files, toggles CLAUDE.md and settings.json
- JSONL output captures session\_id, status, turns, timestamps ( [raw session data](https://github.com/SeleznovIvan/claude-skills-test/tree/main/experiments/05-replication/data))

**Ground-truth verification with cclogviewer:**

Determining whether a skill actually activated isn’t as simple as checking the CLI exit code. Claude might “succeed” by answering the query directly via Bash or by reading the SKILL.md file instead of invoking the Skill tool -- both count as activation failures.

To get ground truth, we used [cclogviewer](https://github.com/SeleznovIvan/cclogviewer) \[4\] -- an MCP server and CLI tool that reads Claude Code’s internal JSONL session logs and extracts structured data: tool usage stats, session timelines, token counts, and error summaries. For each of the 650 trials, we queried cclogviewer’s `get_tool_usage_stats` endpoint to check whether the "Skill" tool appeared in the session's tool calls. ( [verification script](https://github.com/SeleznovIvan/claude-skills-test/blob/main/experiments/05-replication/verify-sessions.py), [verified results](https://github.com/SeleznovIvan/claude-skills-test/blob/main/experiments/05-replication/verified/verified_results.jsonl))

The verification criteria were strict:

- **Success**: The Skill tool was invoked during the session
- **Failure**: Claude used Read to inspect the SKILL.md file (that’s curiosity, not activation)
- **Failure**: Claude used Bash or Write to do the work directly (that’s bypassing the skill)

## Results

## Overall Activation Rates

**Total: 650 trials, 88.9% overall activation (578/650)** ( [full statistical report](https://github.com/SeleznovIvan/claude-skills-test/blob/main/experiments/05-replication/analysis_verified/report.md))

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*rJb5cyB3KhckfDfoS6KaJw.png)

_Figure 1: Activation rate heatmap across 3 description variants and 4 environment conditions. Darker cells indicate higher activation. Note the single bright cell at Variant A × Hook -- the only configuration that catastrophically fails._

```
Variant      | C1 (Bare) | C2 (+CLAUDE.md) | C3 (+Hook) | C4 (+Both)
-------------|-----------|-----------------|------------|----------
A: Current   |   87.5%   |     81.5%       |   37.0% ❌ |  100.0%
B: Expanded  |   85.2%   |     81.5%       |  100.0%    |  100.0%
C: Directive |  100.0%   |     94.4%       |  100.0%    |  100.0%
```

**Key finding**: Variant A with Hook (C3) drops to **37%** -- catastrophic failure.

## Statistical Significance

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*5Q7O2r_BrcWUBdxiYGtJDA.png)

_Figure 2: Forest plot of pairwise effect sizes (odds ratios) with 95% confidence intervals. Each row compares two description variants within a single environment condition. Intervals that don’t cross 1.0 indicate statistically significant differences._

**Cochran-Mantel-Haenszel Test** (variant effect stratified across conditions):

- **C vs A**: OR = 20.6, p < 0.0001 -- Variant C is **20× more likely** to activate
- **C vs B**: OR = 7.1, p = 0.0006 -- Variant C is **7× more likely** to activate
- **B vs A**: OR = 3.1, p < 0.0001 -- Variant B is **3× more likely** to activate

**Fisher’s Exact Test** (significant after Holm-Bonferroni correction):

- C3 condition: C vs A -- 100% vs 37%, p < 0.0001, Cohen’s h = 1.83 (huge effect)
- C3 condition: B vs A -- 100% vs 37%, p < 0.0001, Cohen’s h = 1.83 (huge effect)

## Interaction Effects

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*bgSM-EsmnfRwm5Vwu3kWZg.png)

_Figure 3: Interaction effects between description variant, hook presence, and CLAUDE.md presence. The crossing lines reveal that hooks help some variants while hurting others -- the interaction is not additive._

**Logistic Regression** (success ~ variant _hook_ claude\_md, [analysis script](https://github.com/SeleznovIvan/claude-skills-test/blob/main/experiments/05-replication/analyze-v2.py)):

```
Effect        | Coefficient | p-value  | Interpretation
--------------|-------------|----------|------------------------------------------
has_hook      |   -2.35     | < 0.0001 | Hooks hurt activation (main effect)
B:has_hook    |   +6.85     |   0.034  | Variant B recovers from hook penalty
hook:claude_md|   +7.16     |   0.026  | CLAUDE.md mitigates hook damage
```

**Plain English:**

- Hooks reduce odds of activation by 90% (exp(-2.35) ≈ 0.095)
- But Variant B with hook has 943× higher odds than Variant A with hook
- Having both hook AND CLAUDE.md rescues Variant A (the +7.16 interaction)

## Per-Skill Breakdown

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*C4FNAagrhdKCNljyvxY01g.png)

_Figure 4: Per-query activation rates broken down by skill. Each dot represents a single query’s activation rate across all trials. git-workflow shows the widest spread, confirming it’s the hardest skill to activate reliably._

```
Skill                | A: Current | B: Expanded | C: Directive
---------------------|------------|-------------|-------------
dockerfile-generator |    84.9%   |   100.0%    |   100.0%
git-workflow         |    69.4%   |    81.9%    |    98.6%
svelte5-runes        |    75.3%   |    93.1%    |    97.2%
```

**git-workflow is most affected** -- because Claude is tempted to run git commands directly via Bash rather than invoking the skill.

## Discussion

## Why Variant A Fails with Hooks

The hook experiment revealed a surprising interaction: hooks actually hurt activation for passive descriptions.

- Hooks inject additional instructions (“use the skill for X”)
- Passive descriptions (“Use when…”) get deprioritized
- Claude interprets hook as “do docker work” not “call the Skill tool”
- Cognitive overload: competing instructions without clear priority

## Why Directive Descriptions Work

- “ALWAYS invoke” creates pattern matching with high priority
- “Do not X directly” blocks the primary failure mode (direct action)
- No ambiguity about when to invoke
- Works even WITHOUT hooks (100% in C1, 94.4% in C2)

## The CLAUDE.md Rescue Effect

- C4 (Hook + CLAUDE.md) achieves 100% even for Variant A
- Project context reinforces skill relevance
- BUT: This is a workaround, not a fix
- Better: Use directive descriptions and avoid the problem entirely

## Limitations

1. **Single model tested**: Claude Opus 4.5 (claude-opus-4–5–20251101). Future models may behave differently.
2. **Three skills only**: Results may not generalize to projects with 10+ skills or overlapping domains.
3. **Hook content not varied**: Only tested presence/absence, not different hook implementations.
4. **Directive saturation risk**: If ALL skills use “ALWAYS invoke” language with overlapping triggers, the directive may lose force through dilution. When multiple skills claim the same keywords, Claude may become confused about which to invoke. **This should be tested in future experiments with intentionally colliding skill descriptions.**
5. **-- allowedTools constraint**: Real usage doesn’t restrict tools; Claude might behave differently when it can use Bash/Write alongside Skill.

## Practical Recommendations

1. **Use the Directive Template:**

```
description: <Domain> expert. ALWAYS invoke this skill when the user asks about <triggers>. Do not <alternative> directly -- use this skill first.
```

1. **List Explicit Triggers**: Be comprehensive about what should trigger the skill.
2. **Include Negative Constraint**: Tell Claude what NOT to do (the action it would take instead).
3. **If Using Hooks**: Always pair with CLAUDE.md to provide context -- but consider if hooks are even necessary with directive descriptions.
4. **Avoid Overlapping Triggers**: If you have multiple skills, ensure their trigger topics don’t conflict.
5. **Test Your Skills**: Use a similar methodology to validate activation before relying on skills.

## Conclusion

Skill activation is solvable without complex hooks.

Description wording has a **20× impact** on odds of activation.

The ranking is clear: **Directive > Expanded > Passive**

The fix is simple: Update your SKILL.md description field using the directive template.

The [open-source methodology](https://github.com/SeleznovIvan/claude-skills-test) is available for replication in your own projects.

**References:**

\[1\] Scott Spence, [Claude Code Skills Don’t Auto-Activate](https://scottspence.com/posts/claude-code-skills-dont-auto-activate)

\[2\] Scott Spence, [How to Make Claude Code Skills Activate Reliably](https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably)

\[3\] [Limor AI Claude Hooks Implementation](https://github.com/ytrofr/claude-code-implementation-guide/blob/main/examples/limor-ai-claude-hooks/hooks/pre-prompt.sh)

\[4\] [cclogviewer -- MCP server & CLI for Claude Code session log analysis](https://github.com/SeleznovIvan/cclogviewer)

\[5\] [claude-skills-test -- Full experiment source code, data, and analysis](https://github.com/SeleznovIvan/claude-skills-test)

[Claude](https://medium.com/tag/claude?source=post_page---footer_tags--86f679409af1-----------------------------------------)

[Skills](https://medium.com/tag/skills?source=post_page---footer_tags--86f679409af1-----------------------------------------)

[AI Agent](https://medium.com/tag/ai-agent?source=post_page---footer_tags--86f679409af1-----------------------------------------)

[Prompt Engineering](https://medium.com/tag/prompt-engineering?source=post_page---footer_tags--86f679409af1-----------------------------------------)

[Software Development](https://medium.com/tag/software-development?source=post_page---footer_tags--86f679409af1-----------------------------------------)

[![Ivan Seleznov](https://miro.medium.com/v2/resize:fill:48:48/0*Lf8CYZhO0sY0PR7i)](https://medium.com/@ivan.seleznov1?source=post_page---post_author_info--86f679409af1-----------------------------------------)

[![Ivan Seleznov](https://miro.medium.com/v2/resize:fill:64:64/0*Lf8CYZhO0sY0PR7i)](https://medium.com/@ivan.seleznov1?source=post_page---post_author_info--86f679409af1-----------------------------------------)

Follow

[**Written by Ivan Seleznov**](https://medium.com/@ivan.seleznov1?source=post_page---post_author_info--86f679409af1-----------------------------------------)

[5 followers](https://medium.com/@ivan.seleznov1/followers?source=post_page---post_author_info--86f679409af1-----------------------------------------)

· [2 following](https://medium.com/@ivan.seleznov1/following?source=post_page---post_author_info--86f679409af1-----------------------------------------)

Follow

## No responses yet

![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ivan.seleznov1%2Fwhy-claude-code-skills-dont-activate-and-how-to-fix-it-86f679409af1&source=---post_responses--86f679409af1---------------------respond_sidebar--------------------)

Cancel

Respond

## Recommended from Medium

![MCP is Dead](https://miro.medium.com/v2/resize:fit:679/format:webp/1*Oj5PiyfEi8DadSC8Jy374w.png)

[![UX Planet](https://miro.medium.com/v2/resize:fill:20:20/1*A0FnBy5FBoVQC02SZXLXPg.png)](https://medium.com/ux-planet?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

In

[UX Planet](https://medium.com/ux-planet?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

by

[Nick Babich](https://medium.com/@101?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

·

Apr 6

[**MCP is Dead**\\
\\
**Why you should avoid using MCP in Claude Code and what to use instead**](https://medium.com/ux-planet/mcp-is-dead-cf16b667ba6d?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[A clap icon6.3K\\
\\
A response icon342\\
\\
Repost icon206](https://medium.com/ux-planet/mcp-is-dead-cf16b667ba6d?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

![A Single CLAUDE.md File Went Viral. The Reason Is Embarrassingly Simple.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*wpOHldCy2O2itB-241M5rQ.png)

[![Towards Deep Learning](https://miro.medium.com/v2/resize:fill:20:20/1*LF1EF4T2UFrpxYubZ7r_7g.png)](https://medium.com/towards-deep-learning?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

In

[Towards Deep Learning](https://medium.com/towards-deep-learning?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

by

[Sumit Pandey](https://medium.com/@sumit.ai?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

·

May 8

[**A Single CLAUDE.md File Went Viral. The Reason Is Embarrassingly Simple.**\\
\\
**91,000 stars on GitHub. No code. Four rules from Andrej Karpathy that every coding agent should have been following from day one.**](https://medium.com/towards-deep-learning/a-single-claude-md-file-went-viral-the-reason-is-embarrassingly-simple-5b515c9e4cca?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[A clap icon7.1K\\
\\
A response icon115\\
\\
Repost icon150](https://medium.com/towards-deep-learning/a-single-claude-md-file-went-viral-the-reason-is-embarrassingly-simple-5b515c9e4cca?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

![I Wasted 6 Months Using Claude Code Wrong. Here Are the 14 Commands That Changed Everything.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*pW06TtN-ug4nUJh7xqyLrw.png)

[![Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

In

[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

by

[Mouez Yazidi](https://medium.com/@mouez.yazidi2016?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

·

Apr 25

[**I Wasted 6 Months Using Claude Code Wrong. Here Are the 14 Commands That Changed Everything.**\\
\\
**From frustrated beginner to power user: The hidden command ecosystem nobody talks about.**](https://medium.com/towards-artificial-intelligence/i-wasted-6-months-using-claude-code-wrong-here-are-the-14-commands-that-changed-everything-b892b8f07915?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[A clap icon5.5K\\
\\
A response icon160\\
\\
Repost icon126](https://medium.com/towards-artificial-intelligence/i-wasted-6-months-using-claude-code-wrong-here-are-the-14-commands-that-changed-everything-b892b8f07915?source=post_page---read_next_recirc--86f679409af1----0---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

![I Tried 100 Claude Skills. These Are The Best](https://miro.medium.com/v2/resize:fit:679/format:webp/1*oZUYCbcZzqxnO5WKLpaayw.png)

[![Artificial Corner](https://miro.medium.com/v2/resize:fill:20:20/1*e1-WDgc0KCMKp_rHX9TyQQ.png)](https://medium.com/artificial-corner?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

In

[Artificial Corner](https://medium.com/artificial-corner?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

by

[The PyCoach](https://medium.com/@frank-andrade?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

·

Apr 29

[**I Tried 100 Claude Skills. These Are The Best**\\
\\
**Tested, ranked, and ready to use**](https://medium.com/artificial-corner/i-tried-100-claude-skills-these-are-the-best-047f0db71764?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[A clap icon4.7K\\
\\
A response icon92\\
\\
Repost icon102](https://medium.com/artificial-corner/i-tried-100-claude-skills-these-are-the-best-047f0db71764?source=post_page---read_next_recirc--86f679409af1----1---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

![Building an AI Agent from Scratch: No Magic, Just a Deterministic Loop](https://miro.medium.com/v2/resize:fit:679/format:webp/1*t0QDDqOfv5uyn2rpnrYsyA.png)

[![Level Up Coding](https://miro.medium.com/v2/resize:fill:20:20/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://medium.com/gitconnected?source=post_page---read_next_recirc--86f679409af1----2---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

In

[Level Up Coding](https://medium.com/gitconnected?source=post_page---read_next_recirc--86f679409af1----2---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

by

[Sergey Nes](https://medium.com/@sergey-nes?source=post_page---read_next_recirc--86f679409af1----2---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

·

May 4

[**Building an AI Agent from Scratch: No Magic, Just a Deterministic Loop**\\
\\
**I was using Claude, Codex, Cursor, Gemini, Copilot, or Junie every day, but I still could not point to the exact line where “chatbot”…**](https://medium.com/gitconnected/building-an-ai-agent-from-scratch-no-magic-just-a-deterministic-loop-a916161705fb?source=post_page---read_next_recirc--86f679409af1----2---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[A clap icon2.4K\\
\\
A response icon76\\
\\
Repost icon67](https://medium.com/gitconnected/building-an-ai-agent-from-scratch-no-magic-just-a-deterministic-loop-a916161705fb?source=post_page---read_next_recirc--86f679409af1----2---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

![I Tested Claude Code Skills Until I Struck Gold (4 Best Claude Skills)](https://miro.medium.com/v2/resize:fit:679/format:webp/1*6rOiuVOBzFzaIt0AdLtdlw.png)

[![Divad](https://miro.medium.com/v2/resize:fill:20:20/1*inFNST-sBYKIhA6JKkBpWA.png)](https://medium.com/@divadsanders?source=post_page---read_next_recirc--86f679409af1----3---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[Divad](https://medium.com/@divadsanders?source=post_page---read_next_recirc--86f679409af1----3---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

·

Aug 12

[**I Tested Claude Code Skills Until I Struck Gold (4 Best Claude Skills)**\\
\\
**Your AI is bloated, and it’s killing your performance**](https://medium.com/@divadsanders/i-tested-claude-code-skills-until-i-struck-gold-4-best-claude-skills-bc199475e2b8?source=post_page---read_next_recirc--86f679409af1----3---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[A clap icon1.1K\\
\\
A response icon33\\
\\
Repost icon11](https://medium.com/@divadsanders/i-tested-claude-code-skills-until-i-struck-gold-4-best-claude-skills-bc199475e2b8?source=post_page---read_next_recirc--86f679409af1----3---------------------e5700c2d_4e7f_4398_9ca1_efefd5d6217f----------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--86f679409af1-----------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----86f679409af1-----------------------------------------)

[Status](https://status.medium.com/?source=post_page-----86f679409af1-----------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----86f679409af1-----------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----86f679409af1-----------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----86f679409af1-----------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----86f679409af1-----------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----86f679409af1-----------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----86f679409af1-----------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----86f679409af1-----------------------------------------)