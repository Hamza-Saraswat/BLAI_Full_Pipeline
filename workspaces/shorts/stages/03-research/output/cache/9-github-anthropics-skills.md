[Skip to content](https://github.com/anthropics/skills#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/anthropics/skills) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/anthropics/skills) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/anthropics/skills) to refresh your session.Dismiss alert

{{ message }}

[anthropics](https://github.com/anthropics)/ **[skills](https://github.com/anthropics/skills)** Public

- [Notifications](https://github.com/login?return_to=%2Fanthropics%2Fskills) You must be signed in to change notification settings
- [Fork\\
21k](https://github.com/login?return_to=%2Fanthropics%2Fskills)
- [Star\\
177k](https://github.com/login?return_to=%2Fanthropics%2Fskills)


main

[**15** Branches](https://github.com/anthropics/skills/branches) [**0** Tags](https://github.com/anthropics/skills/tags)

[Go to Branches page](https://github.com/anthropics/skills/branches)[Go to Tags page](https://github.com/anthropics/skills/tags)

Go to file

Code

Open more actions menu

## Latest commit

![cj-ant](https://avatars.githubusercontent.com/u/286490957?v=4&size=40)![claude](https://avatars.githubusercontent.com/u/81847?v=4&size=40)

[cj-ant](https://github.com/anthropics/skills/commits?author=cj-ant)

and

[claude](https://github.com/anthropics/skills/commits?author=claude)

[Update claude-api skill: Managed Agents `auto` permission policy and …](https://github.com/anthropics/skills/commit/34040c9c568585f6929bedeaad110ad08f079624)

Open commit details

last weekSep 10, 2026

[34040c9](https://github.com/anthropics/skills/commit/34040c9c568585f6929bedeaad110ad08f079624) · last weekSep 10, 2026

## History

[55 Commits](https://github.com/anthropics/skills/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/anthropics/skills/commits/main/) 55 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [.claude-plugin](https://github.com/anthropics/skills/tree/main/.claude-plugin ".claude-plugin") | [.claude-plugin](https://github.com/anthropics/skills/tree/main/.claude-plugin ".claude-plugin") | [Rename claude-academy-guide skill to academy-guide and shorten its de…](https://github.com/anthropics/skills/commit/0a64e398ec6bb34a494f0c347e8ccae53a862f8e "Rename claude-academy-guide skill to academy-guide and shorten its description (#1605)  Two changes to make the skill packageable as an uploaded custom skill, with no other content changes:  - Rename: the skill folder, the SKILL.md frontmatter name, and the   marketplace.json entry name and path. Skill names cannot contain the   reserved words \"claude\" or \"anthropic\" (per the agent skills   best-practices documentation). - Description: shortened from 1,176 to 992 characters to fit the   1,024-character limit that skill upload validation applies to the   SKILL.md frontmatter description. The shortened text is the version   tested internally.") | last monthAug 18, 2026 |
| [skills](https://github.com/anthropics/skills/tree/main/skills "skills") | [skills](https://github.com/anthropics/skills/tree/main/skills "skills") | [Update claude-api skill: Managed Agents `auto` permission policy and …](https://github.com/anthropics/skills/commit/34040c9c568585f6929bedeaad110ad08f079624 "Update claude-api skill: Managed Agents `auto` permission policy and `ant beta:sessions connect` (#1750)  Adds the third Managed Agents permission policy, `auto`, alongside `always_allow` / `always_ask`: the three outcomes (runs, denied as high-risk with an error tool result while the session keeps running, pauses for approval when indeterminate), a config example, what the evaluation trusts, and the \"not a human checkpoint\" warning. Documents the `evaluated_permission` and `evaluation` fields on `agent.tool_use` / `agent.mcp_tool_use`, and updates the client-pattern and multiagent guides to gate on `evaluated_permission === 'ask'` rather than the configured policy.  Adds `ant beta:sessions connect` to the CLI guide: terminal viewer keybindings, the allow/deny prompt, and the `--web` local session viewer.  Fixes the deny example to use `deny_message` (the real field) instead of `message`.   Claude-Session: https://claude.ai/code/session_01UkZpc4FqLFPLBJF2Zcuq3a  Co-authored-by: Claude <noreply@anthropic.com>") | last weekSep 10, 2026 |
| [spec](https://github.com/anthropics/skills/tree/main/spec "spec") | [spec](https://github.com/anthropics/skills/tree/main/spec "spec") | [Add link to Agent Skills specification website (](https://github.com/anthropics/skills/commit/69c0b1a0674149f27b61b2635f935524b6add202 "Add link to Agent Skills specification website (#160)  Added a note at the top of the README directing users to agentskills.io for information about the Agent Skills standard.  🤖 Generated with [Claude Code](https://claude.com/claude-code)  Co-authored-by: Claude <noreply@anthropic.com>") [#160](https://github.com/anthropics/skills/pull/160) [)](https://github.com/anthropics/skills/commit/69c0b1a0674149f27b61b2635f935524b6add202 "Add link to Agent Skills specification website (#160)  Added a note at the top of the README directing users to agentskills.io for information about the Agent Skills standard.  🤖 Generated with [Claude Code](https://claude.com/claude-code)  Co-authored-by: Claude <noreply@anthropic.com>") | 9 months agoDec 20, 2025 |
| [template](https://github.com/anthropics/skills/tree/main/template "template") | [template](https://github.com/anthropics/skills/tree/main/template "template") | [Move example skills into dedicated folder and create minimal top-leve…](https://github.com/anthropics/skills/commit/ef740771ac901e03fbca3ce4e1c453a96010f30a "Move example skills into dedicated folder and create minimal top-level folder structure (#129)") | 10 months agoDec 1, 2025 |
| [.gitignore](https://github.com/anthropics/skills/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/anthropics/skills/blob/main/.gitignore ".gitignore") | [Add link to Agent Skills specification website (](https://github.com/anthropics/skills/commit/69c0b1a0674149f27b61b2635f935524b6add202 "Add link to Agent Skills specification website (#160)  Added a note at the top of the README directing users to agentskills.io for information about the Agent Skills standard.  🤖 Generated with [Claude Code](https://claude.com/claude-code)  Co-authored-by: Claude <noreply@anthropic.com>") [#160](https://github.com/anthropics/skills/pull/160) [)](https://github.com/anthropics/skills/commit/69c0b1a0674149f27b61b2635f935524b6add202 "Add link to Agent Skills specification website (#160)  Added a note at the top of the README directing users to agentskills.io for information about the Agent Skills standard.  🤖 Generated with [Claude Code](https://claude.com/claude-code)  Co-authored-by: Claude <noreply@anthropic.com>") | 9 months agoDec 20, 2025 |
| [README.md](https://github.com/anthropics/skills/blob/main/README.md "README.md") | [README.md](https://github.com/anthropics/skills/blob/main/README.md "README.md") | [Update README.md (](https://github.com/anthropics/skills/commit/f458cee31a7577a47ba0c9a101976fa599385174 "Update README.md (#1094)") [#1094](https://github.com/anthropics/skills/pull/1094) [)](https://github.com/anthropics/skills/commit/f458cee31a7577a47ba0c9a101976fa599385174 "Update README.md (#1094)") | 4 months agoMay 9, 2026 |
| [THIRD\_PARTY\_NOTICES.md](https://github.com/anthropics/skills/blob/main/THIRD_PARTY_NOTICES.md "THIRD_PARTY_NOTICES.md") | [THIRD\_PARTY\_NOTICES.md](https://github.com/anthropics/skills/blob/main/THIRD_PARTY_NOTICES.md "THIRD_PARTY_NOTICES.md") | [Add 3rd Party notices (](https://github.com/anthropics/skills/commit/ec841043a5cdd938a42d711367a89999be0a2862 "Add 3rd Party notices (#4)") [#4](https://github.com/anthropics/skills/pull/4) [)](https://github.com/anthropics/skills/commit/ec841043a5cdd938a42d711367a89999be0a2862 "Add 3rd Party notices (#4)") | 11 months agoOct 16, 2025 |
| View all files |

## Repository files navigation

> **Note:** This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io/).

[![skills.sh](https://camo.githubusercontent.com/a496f383b21ae2e5ee09d2739c96f23cfad055fc117de8e444957f8c4a2314c7/68747470733a2f2f736b696c6c732e73682f622f616e7468726f706963732f736b696c6c73)](https://skills.sh/anthropics/skills)

# Skills

[Permalink: Skills](https://github.com/anthropics/skills#skills)

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

For more information, check out:

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# About This Repository

[Permalink: About This Repository](https://github.com/anthropics/skills#about-this-repository)

This repository contains skills that demonstrate what's possible with Claude's skills system. These skills range from creative applications (art, music, design) to technical tasks (testing web apps, MCP server generation) to enterprise workflows (communications, branding, etc.).

Each skill is self-contained in its own folder with a `SKILL.md` file containing the instructions and metadata that Claude uses. Browse through these skills to get inspiration for your own skills or to understand different patterns and approaches.

Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power [Claude's document capabilities](https://www.anthropic.com/news/create-files) under the hood in the [`skills/docx`](https://github.com/anthropics/skills/blob/main/skills/docx), [`skills/pdf`](https://github.com/anthropics/skills/blob/main/skills/pdf), [`skills/pptx`](https://github.com/anthropics/skills/blob/main/skills/pptx), and [`skills/xlsx`](https://github.com/anthropics/skills/blob/main/skills/xlsx) subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application.

## Disclaimer

[Permalink: Disclaimer](https://github.com/anthropics/skills#disclaimer)

**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

# Skill Sets

[Permalink: Skill Sets](https://github.com/anthropics/skills#skill-sets)

- [./skills](https://github.com/anthropics/skills/blob/main/skills): Skill examples for Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills
- [./spec](https://github.com/anthropics/skills/blob/main/spec): The Agent Skills specification
- [./template](https://github.com/anthropics/skills/blob/main/template): Skill template

# Try in Claude Code, Claude.ai, and the API

[Permalink: Try in Claude Code, Claude.ai, and the API](https://github.com/anthropics/skills#try-in-claude-code-claudeai-and-the-api)

## Claude Code

[Permalink: Claude Code](https://github.com/anthropics/skills#claude-code)

You can register this repository as a Claude Code Plugin marketplace by running the following command in Claude Code:

```
/plugin marketplace add anthropics/skills
```

Then, to install a specific set of skills:

1. Select `Browse and install plugins`
2. Select `anthropic-agent-skills`
3. Select `document-skills` or `example-skills`
4. Select `Install now`

Alternatively, directly install either Plugin via:

```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

After installing the plugin, you can use the skill by just mentioning it. For instance, if you install the `document-skills` plugin from the marketplace, you can ask Claude Code to do something like: "Use the PDF skill to extract the form fields from `path/to/some-file.pdf`"

## Claude.ai

[Permalink: Claude.ai](https://github.com/anthropics/skills#claudeai)

These example skills are all already available to paid plans in Claude.ai.

To use any skill from this repository or upload custom skills, follow the instructions in [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b).

## Claude API

[Permalink: Claude API](https://github.com/anthropics/skills#claude-api)

You can use Anthropic's pre-built skills, and upload custom skills, via the Claude API. See the [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) for more.

# Creating a Basic Skill

[Permalink: Creating a Basic Skill](https://github.com/anthropics/skills#creating-a-basic-skill)

Skills are simple to create - just a folder with a `SKILL.md` file containing YAML frontmatter and instructions. You can use the **template-skill** in this repository as a starting point:

```
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires only two fields:

- `name` \- A unique identifier for your skill (lowercase, hyphens for spaces)
- `description` \- A complete description of what the skill does and when to use it

The markdown content below contains the instructions, examples, and guidelines that Claude will follow. For more details, see [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills).

# Partner Skills

[Permalink: Partner Skills](https://github.com/anthropics/skills#partner-skills)

Skills are a great way to teach Claude how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:

- **Notion** \- [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)

## About

Public repository for Agent Skills

### Topics

[agent-skills](https://github.com/topics/agent-skills)

### Resources

[Readme](https://github.com/anthropics/skills#readme-ov-file)

[Activity](https://github.com/anthropics/skills/activity)

[Custom properties](https://github.com/anthropics/skills/custom-properties)

### Stars

**177.0k** stars

### Watchers

**1.1k** watching

### Forks

[**21.0k** forks](https://github.com/anthropics/skills/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fanthropics%2Fskills&report=anthropics+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.