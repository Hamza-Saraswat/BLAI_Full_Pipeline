> Fetched web_extract on 2026-09-18. URL: https://lazyskills.sh/troubleshooting/skills-not-triggering

# Claude Code Skill Not Triggering? 8 Causes and Their Fixes (LazySkills)

## How a skill gets triggered in the first place

"When a session starts, the agent scans its skill directories and collects one thing from each skill: the `description` field in the SKILL.md frontmatter. The instruction bodies stay on disk. When you send a request, the agent compares it against those descriptions, and only a skill whose description matches gets its full instructions loaded."

## The checklist

1. Wrong directory or nesting -- project skills at `.claude/skills/<skill-name>/SKILL.md`, personal at `~/.claude/skills/<skill-name>/SKILL.md`; the file must sit exactly one folder deep. `changelog/changelog/SKILL.md` two levels deep is never found.
2. Filename case -- the filename is `SKILL.md`, uppercase SKILL, lowercase md; a lowercase `skill.md` is missed with no warning; bites macOS users hardest (case-insensitive filesystem).
3. Broken frontmatter -- needs `name` and `description`, fenced by `---` on both sides; a missing closing fence means the YAML never terminates and parses as garbage. "run the file through any YAML linter before blaming anything else."
4. A description with nothing to match -- "the big one once the files are valid: the skill loads, shows up in listings, and still never fires. The description is the only signal the agent has at selection time." Working example: "description: Extract text and tables from PDF files. Use when the user asks to read, parse, or convert a PDF." Also: two installed skills with near-identical descriptions compete.
5. Invocation is disabled on purpose -- `disable-model-invocation: true` makes a skill name-invoked only.
6. Stale session -- descriptions collected at session start; a skill installed mid-conversation is invisible until a new session.
7. Too many skills -- descriptions share the context budget; "GitHub issue reports describe installs of 137 skills where only 116 load, with the rest silently absent."
8. Different agents, different rules -- verify per agent.

FAQ: "Listed means loaded, and firing is a separate step. The agent picks skills by matching your request against each description, so a vague description like helps with code gives it nothing to match."

FAQ: "If explicit invocation works but natural phrasing never does, the files are fine and the description is the problem."
