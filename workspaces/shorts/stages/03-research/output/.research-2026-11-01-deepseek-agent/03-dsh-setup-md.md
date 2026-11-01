fetched: 2026-11-01
via: web_extract
url: https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/SETUP.md
title: dsh-superagent SETUP.md

KEY FACTS (verbatim):
- "Instructions for an agent that sets up dsh-superagent with its operator. If you are a person, ask your coding agent to read this file and follow it."
- Prerequisites: "Node.js 22.19+ or 24+, pnpm, git 2.32+, tmux, Python 3.8+, GitHub CLI 2.48+, and DSH within the `engines.dsh` range of `package.json`."
- "DSH also needs a model provider; if the operator has never run DSH with a model, configuring one is an operator step."
- Defaults: "profile `superagent` ... port `3082`; state directory `<home>/.dsh/state/superagent` as an absolute path; an hourly check from the operator's own profile, which repairs dsh-superagent when it is not running; branch prefix `agent/`; accept mode `observe`, which records proactive work without doing it"
- Question 3 recommendation: "A dedicated account, never the operator's own: everything the agent writes appears under this name."
- Question 9 recommendation (auto-merge): "No: people merge until the agent's pull requests have been right for a while."
- How to try it: "from an account on the allowed list, comment `@<agent login> <request>` on an issue in the repository. A Ticket appears on the overview within about a minute."
- Panel URL handed over at the end; "Superagent" entry in the sidebar.
- Setup is run BY a coding agent: probe checks node, pnpm, git, tmux, python3, gh, dsh versions.
