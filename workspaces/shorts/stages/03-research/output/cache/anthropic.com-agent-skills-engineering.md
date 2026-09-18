> Fetched web_extract on 2026-09-18. URL: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

# Equipping agents for the real world with Agent Skills

Published Oct 16, 2025. Anthropic engineering blog. (Update: Agent Skills published as an open standard, December 18, 2025.)

Key passages:

"At its simplest, a skill is a directory that contains a `SKILL.md file`. This file must start with YAML frontmatter that contains some required metadata: `name` and `description`. At startup, the agent pre-loads the `name` and `description` of every installed skill into its system prompt."

"This metadata is the **first level** of _progressive disclosure_: it provides just enough information for Claude to know when each skill should be used without loading all of it into context. The actual body of this file is the **second level** of detail. If Claude thinks the skill is relevant to the current task, it will load the skill by reading its full `SKILL.md` into context."

"Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable."

Trigger sequence: 1) context window has core system prompt + metadata of installed skills + user message; 2) Claude triggers the PDF skill by invoking a Bash tool to read `pdf/SKILL.md`; 3) Claude chooses to read bundled `forms.md`; 4) proceeds with the task.

Authoring guidance: "**Think from Claude's perspective:** Monitor how Claude uses your skill in real scenarios and iterate based on observations... Pay special attention to the `name` and `description` of your skill. Claude will use these when deciding whether to trigger the skill in response to its current task."

"Building a skill for an agent is like putting together an onboarding guide for a new hire."

Agent Skills supported across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform. Example skill: the PDF skill in github.com/anthropics/skills.
