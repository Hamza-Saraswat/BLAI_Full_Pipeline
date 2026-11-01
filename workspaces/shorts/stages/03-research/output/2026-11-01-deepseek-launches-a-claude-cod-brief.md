---
slug: 2026-11-01-deepseek-launches-a-claude-cod
stage: 03-research
topic: "DeepSeek launches a Claude Code rival: the local angle"
depth: standard
generated_at: 2026-11-01T12:40:00Z
sources: 11
hub: "[[videos/2026-11-01-deepseek-launches-a-claude-cod]]"
---

# Research brief: DeepSeek launches a Claude Code rival: the local angle

## Summary
The reframe writes itself: what Bloomberg reported hours ago as a Claude Code rival is not a cloud service at all, it is an MIT-licensed research repo, and that repo is the part you can run tonight. The most arresting number is DeepSeek's own simulation showing p95 task completion of 15.7 minutes versus 29.5 minutes for a single-session agent, roughly 1.9x, but the same report admits the tests measure scheduling on synthetic messages, not coding quality. The strongest concrete case: a public repo, 5.3k stars at fetch, that listens to one GitHub repository, runs each request in an isolated worker session, and answers with a pull request, on your machine, with your choice of model endpoint including a self-hosted one. What could not be verified: whether a fully local stack (harness plus a local OpenAI-compatible model server) actually completes a Ticket end to end, and the repo's one-day star growth ("4,000+ stars in a day" circulates only in community posts). Conflict to carry honestly: Bloomberg frames the launch as a challenge to Anthropic's product, while the repo's own README says "not an official DeepSeek product" -- both are true, and that tension is the video.

## Thesis
DeepSeek's Claude Code rival is not a cloud service you sign up for: the thing that launched is an MIT-licensed repo that runs on your own machine, and its brain is whatever model endpoint you point it at, including one on your own hardware.

## Explanation path
Open on the headline as the viewer met it: Bloomberg, hours old, DeepSeek drops a more autonomous coding agent to challenge Claude Code, from a lab sitting on about 100 billion yuan ($15 billion) of fresh funding. Then land the twist: the "new open-source offering" in Bloomberg's own sentence is the product -- there is no separate hosted service in the reporting, there is a GitHub repo. Establish what the repo is before why it matters: dsh-superagent is a bundle for DeepSeek Harness, a proactive coding agent for exactly one GitHub repository that listens for allowed people to ask for work, opens a Ticket for each request, works it in its own session and directory, and answers in the original conversation, often with a pull request. Now the idea underneath: DeepSeek's design essay argues the bottleneck has moved from model capability to human attention, because a person can actively follow only 3 to 5 sessions at once, so instead of one chat window the architecture splits into a Router that talks to people and isolated Workers that execute. Show what they claim it buys: in their simulation, p95 task completion of 15.7 minutes against 29.5 minutes for a single session -- and immediately what the claim is worth, since DeepSeek itself says the runs use synthetic load and do not measure single-task execution. Then the local consequence, which is the reason this channel cares: the agent scaffolding runs on your machine as a DeepSeek Harness profile, the harness itself is open source and starts with one npx command on localhost, and the model behind it is a pluggable provider -- DeepSeek's API, a third-party lab, or a self-hosted OpenAI-compatible server you run yourself. Close on the honest catch and the tonight-step: it is research code that its own authors call not production-ready, proactive work is parked in observe mode by default, both presets run with danger-full-access as your OS user, and setup is a guided conversation where your own coding agent reads SETUP.md and configures it with you.

## Claims
1. **Bloomberg reported on 2026-11-01 that DeepSeek released a prototype of a more autonomous coding agent to challenge Claude Code, and described the launch itself as open source.**
   - Source: DeepSeek Drops Enhanced Coding Agent With Aim to Rival Anthropic (Bloomberg via LiveMint), https://www.livemint.com/companies/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-11793506699829.html
   - Tier: docs | Confidence: high | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "The new open-source offering, dubbed "Super-Agent," can proactively monitor group chats among developers for feedback on coding issues and suggest solutions without being summoned, the DeepSeek Harness team said in a post on WeChat on Saturday."
2. **dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness: it opens a work item when an allowed person asks, works it in its own agent session and directory, and answers with a pull request.**
   - Source: GitHub - deepseek-ai/dsh-superagent-prototype: Towards a More Autonomous Agent System, https://github.com/deepseek-ai/dsh-superagent-prototype
   - Tier: primary | Confidence: high | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness."
3. **The repo's own README fences it hard: research prototype, not an official DeepSeek product, much of the engineering done by coding agents, not production-ready.**
   - Source: GitHub - deepseek-ai/dsh-superagent-prototype: Towards a More Autonomous Agent System, https://github.com/deepseek-ai/dsh-superagent-prototype
   - Tier: primary | Confidence: high | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "Research prototype for reference only, not an official DeepSeek product." and "This code grew out of our team's day-to-day development work, with much of the engineering done by coding agents."
4. **In DeepSeek's self-reported simulation the Super-agent reached p95 task completion of 15.7 minutes versus 29.5 minutes for a single-session baseline (about 1.9x faster), but the tests used only synthetic messages and simulated tools and did not measure real coding quality.**
   - Source: DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent - MarkTechPost, https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/
   - Tier: docs | Confidence: medium | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "p95 task completion of 15.7 minutes vs 29.5 minutes for the single-session baseline (about 1.9x faster)" and "Tested only on synthetic messages and simulated tools. Real coding quality was not measured."
5. **DeepSeek's design essay claims a person can actively follow only 3 to 5 sessions at once, making human attention, not model capability, the bottleneck for multitasking agents.**
   - Source: DeepSeek提出Super-agent架构设计：Router与Worker双层架构 (IT之家 via ifeng), https://tech.ifeng.com/c/8xg9tbvWnnf
   - Tier: docs | Confidence: medium | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "一个人通常只能同时跟进 3 至 5 个活跃 Session" (a person can usually actively follow only 3 to 5 active sessions)
6. **It runs on your own machine as a dedicated Harness profile, and the prerequisites are ordinary dev tools, not a datacenter: Node.js 22.19+ or 24+, pnpm, git 2.32+, tmux, Python 3.8+, GitHub CLI 2.48+, plus DSH and a model provider.**
   - Source: dsh-superagent SETUP.md, https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/SETUP.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "Prerequisites: Node.js 22.19+ or 24+, pnpm, git 2.32+, tmux, Python 3.8+, GitHub CLI 2.48+, and DSH within the `engines.dsh` range of `package.json`." and "DSH also needs a model provider."
7. **The model is a pluggable endpoint: DSH's provider settings support a self-hosted server or any custom gateway speaking OpenAI Chat Completions, OpenAI Responses, or Anthropic Messages.**
   - Source: Configure models | DeepSeek Harness, https://deepseek-harness.github.io/deepseek-harness/en/guide/providers
   - Tier: primary | Confidence: high | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "Switch the card to Custom model API for a relay, a company gateway, a self-hosted server, or any provider absent from the installed catalog."
8. **The platform it depends on, DeepSeek Harness, is itself open source under MIT with 267.9k stars at fetch, and starts locally with one command that serves a Web UI on your own machine.**
   - Source: GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness: Everything is a Plugin., https://github.com/deepseek-ai/deepseek-harness
   - Tier: primary | Confidence: high | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "The command starts the Web UI at http://127.0.0.1:3080 by default and opens it in the default browser for a local launch."
9. **The stakes context: DeepSeek has raised about 100 billion yuan ($15 billion) in its latest round, one of China's largest ever, ahead of its IPO, explicitly to compete with Anthropic and OpenAI.**
   - Source: DeepSeek Drops Enhanced Coding Agent With Aim to Rival Anthropic (Bloomberg via LiveMint), https://www.livemint.com/companies/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-11793506699829.html
   - Tier: docs | Confidence: medium | Accessed: 2026-11-01 | Via: web_extract
   - Quote: "DeepSeek has raised about 100 billion yuan ($15 billion) in its latest fundraising round, one of China's largest-ever, ahead of its initial public offering."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Super-agent p95 task completion (synthetic simulation) | 15.7 minutes | https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/ | "p95 task completion of 15.7 minutes vs 29.5 minutes for the single-session baseline" |
| 2 | Single-session baseline p95 | 29.5 minutes | https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/ | "Single session plus subagents, neutral prompt: p95 of 29.5 minutes." |
| 3 | Super-agent p50 task completion | 12.4 minutes | https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/ | "Super-agent: p50 of 12.4 minutes, p95 of 15.7 minutes." |
| 4 | Sessions one person can actively follow | 3 to 5 sessions | https://tech.ifeng.com/c/8xg9tbvWnnf | "一个人通常只能同时跟进 3 至 5 个活跃 Session" |
| 5 | DeepSeek latest fundraise | about 100 billion yuan ($15 billion) | https://www.livemint.com/companies/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-11793506699829.html | "raised about 100 billion yuan ($15 billion) in its latest fundraising round" |
| 6 | dsh-superagent repo stars (at fetch 2026-11-01) | 5.3k stars | https://github.com/deepseek-ai/dsh-superagent-prototype | "5.3k stars" |
| 7 | DeepSeek Harness repo stars (at fetch 2026-11-01) | 267.9k stars | https://github.com/deepseek-ai/deepseek-harness | "267.9k stars" |

## Analogy candidates
- **Shop foreman with isolated bays**: the Router is the foreman who takes every incoming request, hands each job to a worker in its own bay with its own tools, and comes back to you only with a finished job, a question, or a failure, because your attention is scarcer than mechanic-hours. Breaks when: a foreman delegates to skilled humans he trusts, while here the foreman and every worker are the same model wearing different tool belts, and the shop keys are your full OS user account (danger-full-access).
- **Answering service for your repository**: it monitors the issue tracker and group chat around the clock so you do not have to, and rings you only when a rule you wrote allows it or a person must act. Breaks when: an answering service only relays messages, while this thing writes code and opens pull requests, so the failure mode is unrequested action, not a missed message.

## Misconceptions
- Myth: DeepSeek launched a hosted Claude Code competitor you sign up for and wait in line to use. Reality: the launch Bloomberg reported is the open-source repo itself, an MIT-licensed prototype you clone and run as a profile on your own machine (claims 1, 2, 6).
- Myth: This is a local Claude Code killer you download, with the intelligence included. Reality: the repo is scaffolding without a brain -- it needs a model provider you configure, and that endpoint can be DeepSeek's API, another lab's, or a self-hosted OpenAI-compatible server of your own (claims 6, 7).
- Myth: The numbers prove it is about 1.9x better than a regular agent at coding. Reality: the 15.7 vs 29.5 minutes figures come from DeepSeek's own simulation on synthetic messages with simulated tools, and DeepSeek says they do not measure single-task execution ability (claim 4).

## Glossary
- **harness**: the software scaffolding wrapped around a language model that lets it call tools, run commands, and manage multi-step work.
- **Router**: the long-running front session that talks to people, keeps the global picture, and hands each unit of work to a worker.
- **Worker**: an isolated agent session that does one Ticket's work in its own directory and reports back to the Router instead of talking to you.
- **Ticket**: one unit of authorized work the agent opened from a request, run in its own session and directory.
- **observe mode**: the default setting in which the agent records the proactive work it would have done without actually doing it.
- **model provider**: the endpoint that actually generates the model's responses; the repo ships without one, so you must configure it.
- **OpenAI-compatible endpoint**: a server that speaks the same API format as OpenAI's chat endpoint, which is one of the three protocols DSH's custom-provider option accepts.
- **pull request**: a GitHub proposal to merge a set of code changes into a repository, which a person reviews and merges.
- **p95**: the time by which 95 percent of tasks were finished in a test run.

## Unverified
- Community posts circulate "4,000+ stars in a day" for the repo; GitHub showed 5.3k stars at fetch, but the one-day growth rate is not stated by any fetched page.
- Whether a fully local stack, the harness plus a self-hosted OpenAI-compatible model server, completes a Ticket end to end has not been measured; the docs support the configuration, and this session did not run it.
- No first-party number exists in the fetched pages for RAM, CPU, or tokens-per-second cost of running DeepSeek Harness itself on consumer hardware.
- DeepSeek says an internal Super-agent instance has been running continuously, but the fetched reports give no duration or scale numbers.
- A Reddit thread titled as a claim that the super-agent direction is not safe could not be read beyond its title, so community skepticism is unsummarized.
- The Bloomberg original is paywalled; its text was verified only through two syndicated copies carrying the full article.
- A claim that calls through DeepSeek Harness were free "until billing starts November 1, Beijing time" appeared only in a search snippet and was never fetched.

## Suggested outline
1. Bloomberg, hours old: DeepSeek drops a coding agent to rival Claude Code, backed by about 100 billion yuan ($15 billion) -- and the open secret is in Bloomberg's own sentence, the offering is open source.
2. What actually shipped: an MIT research prototype that lives on your machine, listens to one GitHub repo, and farms each allowed request to an isolated worker session, because a person can follow only 3 to 5 sessions at once; DeepSeek's simulation says p95 15.7 minutes versus 29.5 minutes, on synthetic load it admits measures scheduling, not coding.
3. The local consequence: scaffolding without a brain -- the harness starts with one npx command, and you point it at any model provider, including a self-hosted OpenAI-compatible server; the honest catch is research code, observe-by-default, and danger-full-access, and the tonight-step is letting your own coding agent read SETUP.md and set it up with you.

## Viewer situation
You run open models at home on a gaming PC or a Mac, you work with an agent one chat window at a time, and you are wondering whether this week's launch changes anything for the hardware you already own.

## Has process
`true`
Install Node.js and start the harness on your own machine with `npx @deepseek-ai/dsh web`.
Open Settings, Models, and add a Custom model API provider with the base URL of the model endpoint you want, including a self-hosted OpenAI-compatible server.
Clone the dsh-superagent-prototype repository from GitHub.
Ask your own coding agent: "Read SETUP.md in this repository and set up dsh-superagent with me."
From an account on the allowed list, comment `@<agent login> <request>` on an issue in the repository and watch a Ticket appear on the panel.

## Objection
This is a one-commit research prototype whose own README says it is not an official product, whose speed numbers come from a synthetic message simulation that never measured coding quality, and which runs with danger-full-access as your OS user -- it demos an architecture, it does not dethrone Claude Code.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/deepseek-ai/dsh-superagent-prototype | GitHub - deepseek-ai/dsh-superagent-prototype: Towards a More Autonomous Agent System | primary | web_extract | 2026-11-01 |
| 2 | https://www.livemint.com/companies/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-11793506699829.html | DeepSeek Drops Enhanced Coding Agent With Aim to Rival Anthropic (Bloomberg via LiveMint) | docs | web_extract | 2026-11-01 |
| 3 | https://www.deccanchronicle.com/technology/deepseek-drops-enhanced-coding-agent-with-aim-to-rival-anthropic-2000806 | DeepSeek Drops Enhanced Coding Agent With Aim To Rival Anthropic (Bloomberg via Deccan Chronicle) | docs | web_extract | 2026-11-01 |
| 4 | https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/SETUP.md | dsh-superagent SETUP.md | primary | web_extract | 2026-11-01 |
| 5 | https://www.deepseek.com/en/harness/ | DeepSeek Harness (official product page) | primary | web_extract | 2026-11-01 |
| 6 | https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart | Use the Web UI - DeepSeek Harness docs | primary | web_extract | 2026-11-01 |
| 7 | https://deepseek-harness.github.io/deepseek-harness/en/guide/providers | Configure models - DeepSeek Harness docs | primary | web_extract | 2026-11-01 |
| 8 | https://news.ycombinator.com/item?id=50316116 | DeepSeek open-sources dsh-superagent, a coding agent largely built by agents - Hacker News | community | web_extract | 2026-11-01 |
| 9 | https://github.com/deepseek-ai/deepseek-harness | GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness: Everything is a Plugin. | primary | web_extract | 2026-11-01 |
| 10 | https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/ | DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent - MarkTechPost | docs | web_extract | 2026-11-01 |
| 11 | https://tech.ifeng.com/c/8xg9tbvWnnf | DeepSeek提出Super-agent架构设计：Router与Worker双层架构 (IT之家 via ifeng) | docs | web_extract | 2026-11-01 |

## Notes
The 12.4/15.7/29.5-minute figures originate in DeepSeek's own design essay, posted on WeChat and not directly fetchable this session; they were read through ifeng's report of the essay and independently matched by MarkTechPost, which flags them as self-reported from secondary reports -- treat them as a vendor simulation, not a benchmark. Bloomberg frames the launch as a challenge to Claude Code while the repo README says "not an official DeepSeek product"; the script should carry both framings rather than pick one. Star counts are point-in-time at fetch. The fully-local configuration (harness plus a local OpenAI-compatible server) is documented in DSH's provider guide but untested here, so any "runs fully local tonight" line must be hedged as the documented configuration, not a measured result.
