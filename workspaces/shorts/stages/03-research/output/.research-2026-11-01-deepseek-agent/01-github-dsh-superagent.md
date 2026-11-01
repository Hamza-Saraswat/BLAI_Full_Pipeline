fetched: 2026-11-01
via: web_extract
url: https://github.com/deepseek-ai/dsh-superagent-prototype
title: GitHub - deepseek-ai/dsh-superagent-prototype: Towards a More Autonomous Agent System

KEY FACTS:
- "Research prototype for reference only, not an official DeepSeek product." "This code grew out of our team's day-to-day development work, with much of the engineering done by coding agents. Treat it as research code, not production-ready software."
- "We have adapted it for publication, so it is not identical to our internal version or the implementation described in _Exploring Super-agent Design: Towards a More Autonomous Agent System_. Some designs discussed in the article are directions for future development and are not implemented in this prototype."
- "dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. It listens to GitHub and, optionally, Feishu. When someone allowed asks the agent for work, it opens a work item, works on it in its own agent session and directory, and answers in the original conversation, for example with a pull request. A web panel shows what needs a person."
- "take as little human attention as possible, and give as much value as possible."
- Setup: "Setup has many steps, so an agent does it with you. Ask your coding agent: Read SETUP.md in this repository and set up dsh-superagent with me." "It asks one short question at a time, shows the full plan once, and then installs and configures everything."
- License: MIT
- Stars: 5.3k stars; Watchers: 29 watching; Forks: 501 forks
- Latest commit: "feat: add the dsh-superagent research prototype" by DeepSeek Harness Team, Oct 31, 2026, 1 commit, 1 branch, 0 tags
- Docs: 000 Philosophy, 001 Domain model, 002 Authorization, 003 Execution, 004 Prompts, 005 Panel, 006 Deployment, 007 Architecture, 008 Cookbook
- Development: `pnpm check` runs the typecheck, the tests and the build.
- Tech: TypeScript (tsconfig, tsdown.config.ts, vitest), pnpm, package.json
