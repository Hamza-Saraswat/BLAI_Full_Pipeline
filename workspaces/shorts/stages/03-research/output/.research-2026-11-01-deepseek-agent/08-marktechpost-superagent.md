fetched: 2026-11-01
via: web_extract
url: https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/
title: DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent - MarkTechPost
author: Asif Razzaq, dated 2026-11-01

KEY FACTS (verbatim):
- "The DeepSeek Harness team just released dsh-superagent, an MIT-licensed research prototype. DeepSeek dsh-superagent is a proactive coding agent for one GitHub repository. It is packaged as a bundle for DeepSeek Harness."
- "The release shipped alongside a design post, _Exploring Super-agent Design: Towards a More Autonomous Agent System_." (links yicai.com/news/103419784.html)
- TL;DaR: "What is it?: A TypeScript bundle, v0.1.0, released as 1 commit under MIT. It uses whatever model the Harness profile is set to."
- "Runs on: Your own machine, as a dedicated DeepSeek Harness profile. Needs Node.js 22.19+ or 24+, git 2.32+, Python 3.8+, tmux and GitHub CLI 2.48+."
- "Best: p95 task completion of 15.7 minutes vs 29.5 minutes for the single-session baseline (about 1.9x faster)."
- "Worst: Tested only on synthetic messages and simulated tools. Real coding quality was not measured."
- "DeepSeek team argues that mainstream agents treat 1 session as the basic unit. ... a person can actively follow only 3 to 5 sessions at once. Human attention, not model capability, becomes the bottleneck for multitasking." (attributes to ifeng report)
- Architecture: "A long-running Router handles interaction and dispatch. Isolated Worker sessions do the actual work." Domain flow: "Source -> Trigger ... Eval ... Ticket ... Subscription".
- "Shell commands move to the background after 5 seconds, so Workers keep receiving messages"
- "Background work gets up to 30 minutes per turn."
- Accept modes: "3 accept modes: `off`, `observe` (default) and `auto`. In `observe`, the agent only records what it would have accepted."
- Benchmarks: "Super-agent: p50 of 12.4 minutes, p95 of 15.7 minutes." / "Single session plus subagents, neutral prompt: p95 of 29.5 minutes. No p50 was given." / "the baseline called a subagent 0 times in 5 runs"
- Test setup: "Each run had about 300 messages, of which about 20 were real work requests. Each scheme ran 5 times"
- "Router load: as arrivals rose from about 1 to 40 per minute, batch size grew from 1.0 to 2.8. Per-request latency rose from 2.5 to 3.9 seconds."
- Ablation: "Router decisions rose about 30%, and cache-read tokens rose about 37%, from 23.23M to 31.77M"
- "All figures are self-reported and come from secondary reports of the report."
- Safety: "Both presets run with danger-full-access as the operator's OS user. DeepSeek suggests a dedicated OS account for isolation."
- Limits: "github.com only. GitHub Enterprise Server is not supported. Feishu is the only chat Source shipped." / "Watchdog, storage/compute separation and async ReAct are described in the essay. Some designs are future directions." / "Long-term memory, prompt injection, credential leaks and oversight across many tasks remain unsolved."
- Comparison table rows: vs GitHub Copilot cloud agent, Claude Code Action, OpenAI Codex. "Where it runs: Your machine (Harness profile)" vs "GitHub, in the background" / "Your GitHub Actions runner" / "Codex cloud". License MIT vs Not disclosed / MIT / CLI agent open source.
- Conclusion takeaway: "Proactive work stays in `observe` mode until a team switches it on." "It runs with full OS-user access, so isolate it before use."
