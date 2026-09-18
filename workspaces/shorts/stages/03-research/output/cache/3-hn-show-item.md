|     |     |     |
| --- | --- | --- |
| |     |     |     |
| --- | --- | --- |
| [![](https://news.ycombinator.com/y18.svg)](https://news.ycombinator.com/) | **[Hacker News](https://news.ycombinator.com/news)** [new](https://news.ycombinator.com/newest) \| [past](https://news.ycombinator.com/front) \| [comments](https://news.ycombinator.com/newcomments) \| [ask](https://news.ycombinator.com/ask) \| [show](https://news.ycombinator.com/show) \| [jobs](https://news.ycombinator.com/jobs) \| [submit](https://news.ycombinator.com/submit) | [login](https://news.ycombinator.com/login?goto=item%3Fid%3D49744398) | |

| |     |     |     |
| --- | --- | --- |
|  |  | \[flagged\] [Show HN: Linting 216 public Claude Code skills – 69% won't reliably trigger](https://skillcrossroads.com/) ( [skillcrossroads.com](https://news.ycombinator.com/from?site=skillcrossroads.com)) |
|  | 2 points by [sgharlow](https://news.ycombinator.com/user?id=sgharlow) [8 hours ago](https://news.ycombinator.com/item?id=49744398) \| [hide](https://news.ycombinator.com/hide?id=49744398&goto=item%3Fid%3D49744398) \| [past](https://hn.algolia.com/?query=Show%20HN%3A%20Linting%20216%20public%20Claude%20Code%20skills%20%E2%80%93%2069%25%20won%27t%20reliably%20trigger&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0) \| [favorite](https://news.ycombinator.com/fave?id=49744398&auth=2222632360bd399c3b5d407c26928eaaca26fd1b) \| [discuss](https://news.ycombinator.com/item?id=49744398) |
|  | I built a linter for Claude Code artifacts (skills, subagents, slash commands, .mcp.json configs, and plugins) and then pointed it at a pile of public repos to see what people actually ship. A few of the numbers surprised me enough that I wrote them up.<br>The one that stuck: across 87 public subagents, 57% (50 of 87) declare no \`tools\` list at all. That reads like a safe default, but it's the opposite. A subagent with no \`tools\` inherits the caller's entire toolbox, Bash included. Permission prompts still gate execution, but a worker you meant to "just read code" now carries the grant surface to run shell — the opposite of least-privilege. Add 16 more that grant bare \`Bash\` and 8 that grant a wildcard, and 85% of the sample isn't least-privilege.<br>Other findings from the two scans:<br>\- Of 215 public skills scored for triggering, 69% have a \`description\` that won't reliably trigger (40% outright unlikely to fire, 28% borderline). "My skill never fires" is the #1 real-world failure, and it hides in one frontmatter line.<br>\- 83% of subagents (72 of 87) lack invocation cues ("use when…") in their description.<br>\- 1 of 216 skills, and 0 of 87 subagents, pass every check cleanly. Almost everyone got secrets right: only 6 of 216 skills tripped the scanner.<br>How it works: mostly pure, deterministic checks that emit file:line evidence ("SKILL.md:14 links ./references/converter.md, not found"). An optional LLM check (bring your own key) judges whether a description will actually trigger. The CLI is free (\`npx skillcrossroads ./my-skill\`), there's a GitHub Action that gates PRs, and it's open-core: the public audits are free, money is a hosted Pro tier.<br>Limits: the two reports ran different editions (skills on rubric v1.2 with the LLM checks, agents on v1.2 deterministic-only), both labeled, tree SHAs pinned, reproduction commands published. The rubric is strict on purpose, and every finding carries file:line evidence you can check against the artifact itself. The sample is 216 skills across 18 repos and 123 agents/commands (87 subagents + 36 commands) across 10 repos, caps disclosed, and you can re-run it on your own repos.<br>Reports: [https://skillcrossroads.com/report?ref=hn-show](https://skillcrossroads.com/report?ref=hn-show) and [https://skillcrossroads.com/report-agents?ref=hn-show](https://skillcrossroads.com/report-agents?ref=hn-show)<br>Code: [https://github.com/sgharlow/skillcrossroads](https://github.com/sgharlow/skillcrossroads) |

|  | [help](https://news.ycombinator.com/formatdoc) |

|
| |
| ![](https://news.ycombinator.com/s.gif)

|     |
| --- |
|  |

[Guidelines](https://news.ycombinator.com/newsguidelines.html) \| [FAQ](https://news.ycombinator.com/newsfaq.html) \| [Lists](https://news.ycombinator.com/lists) \| [API](https://github.com/HackerNews/API) \| [Security](https://news.ycombinator.com/security.html) \| [Legal](https://www.ycombinator.com/legal/) \| [Apply to YC](https://www.ycombinator.com/apply/) \| [Contact](mailto:hn@ycombinator.com)

Search: |