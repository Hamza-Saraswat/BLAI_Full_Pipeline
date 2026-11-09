---
slug: 2026-11-09-open-webui-v0-13-3-agents-in-a
stage: 03-research
topic: "Open WebUI v0.13.3 ships agents in automations"
depth: standard
generated_at: 2026-11-09T12:40:35Z
sources: 10
hub: "[[videos/2026-11-09-open-webui-v0-13-3-agents-in-a]]"
---

# Research brief: Open WebUI v0.13.3 ships agents in automations

## Summary
Open WebUI has spent this release cycle turning chat prompts into clock-driven errands, and v0.13.3 (dated 2026-11-08 in the changelog) closes the chain by letting an automation save its own terminal, working folder and coding agent. The scale behind the change: the open-webui repository shows 158.2k stars and 23.0k forks on GitHub. The strongest concrete case is Open WebUI's own suggested first task: a daily 9:00 run that executes the test suite in one workspace, changes no files, and reports the failing test with its error output. Not verified: download counts, community reaction to v0.13.3 specifically (the release is under a day old and the subreddit thread returned 403), and whether Aider specifically is offered as an agent (no fetched page names it). One conflict: the automations docs page still says the automation editor has no terminal setting because a run uses the terminal configured on the model, while the v0.13.3 release notes say the editor now picks the terminal, folder and agent directly -- the release notes are newer and first-party, so this brief follows them.

## Thesis
Open WebUI v0.13.3 lets a scheduled automation run a coding agent in the terminal and folder you chose, so your first unattended agent errand is three moves away.

## Explanation path
Begin with the thing the viewer already does: asking a model in a chat to fix something, and the wall they hit -- the fix lives in a chat window and dies there. Introduce the terminal as the hands: one connected computer workspace with a real folder turns the same chat into an agent that reads and writes files. Name the gate that has kept this attended: tool calls wait for a person to click Allow, so agent runs needed someone present. Reveal what the schedule adds: an automation is the same prompt with a clock on it, run by the server whether or not a browser is open. Land the release's actual move -- the automation editor now saves the terminal, the folder and the coding agent together with the schedule, and checks that they are still available before a run starts. Show where the evidence lands: a real chat holding the whole run, and a run-history line marked success or error. Finish on the guardrail the docs state themselves: unattended runs execute with full tool approval because nobody is there to click Allow, so the first folder should be a throwaway and the prompt should say what not to touch.

## Claims
1. **Open WebUI v0.13.3, dated 2026-11-08 in the changelog, adds "Agents in automations": the automation editor now lets you choose a terminal and a working folder, then select a coding agent available there.**
   - Source: Release v0.13.3 - open-webui/open-webui - GitHub, https://github.com/open-webui/open-webui/releases/tag/v0.13.3
   - Tier: primary | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "The automation editor now lets you choose a terminal and working folder, then select a coding agent available there."
2. **Scheduled runs reuse the saved terminal and folder and check that both the terminal and the agent are still available before starting, and agent automations send their results to a chat.**
   - Source: open-webui/CHANGELOG.md at main - GitHub, https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "Scheduled runs use that saved terminal and folder, and check that the terminal and agent are still available before starting. Agent automations send their results to a chat; channel destinations remain available for ordinary models."
3. **The coding agents in question are named tools -- Claude Code, Codex and Pi -- which have appeared in the model picker on agent-capable Open Terminals since v0.13.1, dated 2026-11-03.**
   - Source: open-webui/CHANGELOG.md at main - GitHub, https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "On an Open Terminal that offers agents, coding agents such as Claude Code, Codex and Pi now appear in the model picker."
4. **Scheduled runs execute with full tool approval because nobody is there to click Allow, so Open WebUI's own guidance is to give the task a workspace you are comfortable with and a prompt that says exactly what to do, and what not to.**
   - Source: Scheduled tasks / Open WebUI, https://docs.openwebui.com/ecosystem/computer/automate/scheduled-tasks
   - Tier: docs | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "Scheduled runs execute with full tool approval: nobody is there to click Allow. Give the task a workspace you're comfortable with and a prompt that says exactly what to do (and what not to)."
5. **Every scheduled run produces a real chat in the selected workspace, visible in the sidebar with the full task activity, plus a run-history entry on the task showing success or error with the error text.**
   - Source: Scheduled tasks / Open WebUI, https://docs.openwebui.com/ecosystem/computer/automate/scheduled-tasks
   - Tier: docs | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "Every run creates: a real chat in the selected workspace, visible in the sidebar with the full task activity, and a run-history entry on the task showing success or error (with the error text)."
6. **Tether, introduced in this release cycle, is the desktop companion app for macOS, Windows and Linux that ties your own computer to Open WebUI, connecting outward so there are no ports to open, with a renewable session that expires after 90 days without use by default.**
   - Source: open-webui/CHANGELOG.md at main - GitHub, https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "Tether connects out to Open WebUI, so there are no ports to open [...] It signs in with a renewable session that expires after 90 days without use by default"
7. **The open-webui repository shows 158.2k stars, 683 watching and 23.0k forks on GitHub as accessed 2026-11-09.**
   - Source: open-webui/open-webui: User-friendly AI Interface (Supports Ollama, OpenAI API, ...) - GitHub, https://github.com/open-webui/open-webui
   - Tier: primary | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "Stars **158.2k** stars [...] **683** watching [...] **23.0k** forks"
8. **Automations are created under User Menu > Automations with a New Automation button, and support Once, Hourly, Daily, Weekly, Monthly and Custom (RRULE) schedule modes, with Daily, Weekly and Monthly running at the exact minute you pick in your own timezone.**
   - Source: Automations / Open WebUI, https://docs.openwebui.com/features/chat-conversations/chat-features/automations/
   - Tier: docs | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "Supported schedule modes: Once, Hourly, Daily, Weekly, Monthly, Custom (RRULE). Daily, Weekly and Monthly run at the exact minute you pick, in your own timezone."
9. **A terminal is connected under Settings > Admin > Integrations in the Open Terminal section, by clicking + and entering the terminal URL such as http://localhost:8000 plus the API key chosen during installation.**
   - Source: Connecting to Open WebUI / Open WebUI, https://docs.openwebui.com/features/open-terminal/setup/connecting
   - Tier: docs | Confidence: high | Accessed: 2026-11-09 | Via: web_extract
   - Quote: "In the Open Terminal section, click +, enter `http://localhost:8000` and your key, and save."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | v0.13.3 release date | 2026-11-08 | https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md | "[0.13.3] - 2026-11-08" |
| 2 | coding agents in model picker since | 2026-11-03 (v0.13.1) | https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md | "[0.13.1] - 2026-11-03" |
| 3 | open-webui GitHub stars (accessed 2026-11-09) | 158.2k | https://github.com/open-webui/open-webui | "**158.2k** stars" |
| 4 | open-webui GitHub forks (accessed 2026-11-09) | 23.0k | https://github.com/open-webui/open-webui | "**23.0k** forks" |
| 5 | Tether session expiry (default) | 90 days without use by default | https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md | "a renewable session that expires after 90 days without use by default" |
| 6 | Open Terminal default Docker image size | about 4 GB | https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer | "Use the default image, about 4 GB, because the `slim` and `alpine` images don't include the desktop." |
| 7 | terminal start wait (default) | 60 seconds by default | https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md | "Open WebUI now waits up to 60 seconds by default when it asks a terminal for its skills, AGENTS.md file or uploads" |

## Analogy candidates
- **A cron job with hands**: mapping -- cron fires a prompt on a clock exactly as it fires a script; the difference is the script now reads a folder and writes code. Breaks when: a cron job either runs or fails and emails you, while an agent run leaves a whole chat you can read and argue with, and the agent can deviate from its instructions in ways cron never can.
- **A night-shift junior developer**: mapping -- you leave a ticket, they work inside one repo folder overnight, and the morning chat log is the standup. Breaks when: a human junior carries memory between nights without a transcript and knows which rules were actually rules; the agent only has the prompt, the folder and what the run's chat preserved.
- **A Roomba for a code folder**: mapping -- you shut the door on a small bounded space and let it run on a schedule, and it is safe because the space is disposable. Breaks when: a Roomba physically cannot leave its room, but an agent with full tool approval can act on anything its folder and tools reach, including network calls.

## Misconceptions
- Myth: The agent keeps working only while I keep the browser tab open. Reality: Automations run server-side on their schedule, and every run leaves a real chat and a run-history entry whether or not anyone was watching (claims 2 and 5).
- Myth: Unattended is safe because the agent will stop and ask before doing anything risky. Reality: Scheduled runs execute with full tool approval -- nobody is there to click Allow -- which is exactly why the docs say to pick a workspace you are comfortable with and write instructions that state what not to do (claim 4).

## Glossary
- **Open WebUI**: a self-hosted web interface, run on your own machine or home server, that fronts local and cloud AI models.
- **Automation**: a saved prompt that Open WebUI runs on a schedule; each run creates a real chat.
- **Open Terminal**: the connected computer workspace (a real shell and filesystem) that lets a model run commands and edit files instead of just chatting.
- **Coding agent**: an AI coding tool such as Claude Code, Codex or Pi that edits code in a folder on its own.
- **Tether**: the desktop companion app for macOS, Windows and Linux that links your own computer to Open WebUI.
- **Working folder**: the directory the agent works in for a run; the boundary you chose for it.
- **Tool approval (permission prompt)**: the Allow click a normal chat requires before the model runs a tool such as a shell command.
- **RRULE**: the iCalendar recurrence syntax behind custom schedules, e.g. RRULE:FREQ=DAILY;BYHOUR=9;BYMINUTE=0 for every day at 09:00.
- **Run history**: the per-task list of past runs, each marked success or error with the error text.

## Unverified
- Open WebUI download counts (Docker pulls, pip installs) appear on none of the fetched pages.
- Community reaction to v0.13.3 specifically is unverified: the release is under a day old and the subreddit thread for the cycle (r/OpenWebUI 0.13.1 post) returned 403 on fetch.
- Whether Aider specifically is offered as a selectable coding agent is unverified; every fetched page that names agents names Claude Code, Codex and Pi.
- The exact on-screen labels inside the v0.13.3 automation editor beyond the release note wording are unverified (the docs page describing the editor predates the release).
- How an agent automation behaves when its terminal is mid-restart at fire time, beyond the release note saying availability is checked before starting.

## Suggested outline
1. Hook: while you slept, a coding agent ran inside a folder you picked -- Open WebUI v0.13.3 put agents inside automations.
2. Recall the familiar starting point: asking a model in a chat to fix something, and the fix dying in the chat window.
3. Add the hands: one connected terminal with a real folder turns chat into an agent that reads and writes files.
4. Name the old wall: tool calls wait for Allow, so agent runs needed a person in the chair.
5. Deliver the release's move: the automation editor saves the terminal, the folder and the agent with the schedule, and checks they still exist before each run.
6. Show the three viewer moves on screen: connect the terminal, create the automation and pick terminal, folder, agent, then hit Run now.
7. Show where the evidence lands: a real chat with the whole run, and a run-history line marked success or error.
8. Honest catch: unattended means full tool approval, nobody clicks Allow, so start with a throwaway folder and a prompt that says what not to touch.

## Viewer situation
You have Open WebUI running with your models at home and you have watched a coding agent work in a chat, but every one of those runs started because you sat there and typed.

## Has process
true
Connect an Open Terminal under Settings > Admin > Integrations (or sign into Tether so your own computer appears under Your devices in the terminal menu).
Create the automation under User Menu > Automations with the New Automation button.
Choose the terminal, pick the working folder, and select the coding agent available there.
Set the schedule (Once, Hourly, Daily, Weekly, Monthly, or a custom RRULE) and write instructions that say exactly what to do and what not to.
Click Run now once and read the chat it creates before trusting the schedule.
Check the run-history entry for success or error, and leave the automation enabled only once the output is something you can judge in seconds.

## Objection
You are handing an unattended agent full tool approval on a real folder -- nobody is there to click Allow -- and a scheduled prompt is a thin spec for code changes.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/open-webui/open-webui/releases/tag/v0.13.3 | Release v0.13.3 - open-webui/open-webui - GitHub | primary | web_extract | 2026-11-09 |
| 2 | https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md | open-webui/CHANGELOG.md at main - GitHub | primary | web_extract | 2026-11-09 |
| 3 | https://docs.openwebui.com/features/chat-conversations/chat-features/automations/ | Automations / Open WebUI | docs | web_extract | 2026-11-09 |
| 4 | https://docs.openwebui.com/ecosystem/computer/automate/scheduled-tasks | Scheduled tasks / Open WebUI | docs | web_extract | 2026-11-09 |
| 5 | https://docs.openwebui.com/features/open-terminal | Open Terminal / Open WebUI | docs | web_extract | 2026-11-09 |
| 6 | https://github.com/open-webui/open-webui | open-webui/open-webui: User-friendly AI Interface - GitHub | primary | web_extract | 2026-11-09 |
| 7 | https://docs.openwebui.com/features/open-terminal/coding-agents | Coding Agents / Open WebUI | docs | web_extract | 2026-11-09 |
| 8 | https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer | Open WebUI v0.13.0: Your Model Gets a Computer (official blog) | docs | web_extract | 2026-11-09 |
| 9 | https://github.com/open-webui/tether | open-webui/tether: The desktop companion for Open WebUI | primary | web_extract | 2026-11-09 |
| 10 | https://docs.openwebui.com/features/open-terminal/setup/connecting | Connecting to Open WebUI / Open WebUI | docs | web_extract | 2026-11-09 |

## Notes
Conflict, not averaged: the automations docs page (source 3) states "The automation editor has no terminal setting. A run uses the terminal configured on the model it runs", while the v0.13.3 release notes (source 1) state the editor now lets you choose a terminal and working folder directly. This brief follows the release notes: they are first-party, dated 2026-11-08, and describe the newer behavior; the docs page appears not yet updated for v0.13.3 (it also omits agent selection). Consequence for the script: present terminal, folder and agent selection as living in the automation editor per the release note, and do not teach the older configure-terminal-on-the-model path as the current flow. Same-day releases: the changelog dates both 0.13.2 and 0.13.3 as 2026-11-08; v0.13.2 contained only fixes, so "what is new vs 0.13.2" is exactly the agents-in-automations editor, terminal and folder switching during a chat, and the Brazilian Portuguese translations. Sentiment leads: r/OpenWebUI threads exist for the 0.13.x cycle but the fetch of the 0.13.1 thread returned 403, so no community tier source is cited anywhere. The Instagram post announcing "Your coding agent can now run on a schedule in Open WebUI" was seen only as a search snippet and is not treated as fetched.
