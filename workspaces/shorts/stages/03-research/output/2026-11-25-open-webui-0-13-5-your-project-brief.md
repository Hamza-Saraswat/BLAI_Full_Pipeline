---
slug: 2026-11-25-open-webui-0-13-5-your-project
stage: 03-research
topic: "Open WebUI 0.13.5 folder workspaces: your project beside your chat"
depth: standard
generated_at: 2026-11-25T13:04:35Z
sources: 9
hub: "[[videos/2026-11-25-open-webui-0-13-5-your-project]]"
---

# Research brief: Open WebUI 0.13.5 folder workspaces: your project beside your chat

## Summary
Open WebUI shipped v0.13.5 this morning (25 Nov 2026, 09:37 UTC) with Folder workspaces as its headline Added item. The viewer's move tonight is concrete: one Docker container, one sidebar folder with a Machine and Working directory, and a browser tab running beside the chat. The most arresting number is the 34x message-send speedup in the 130 MB PostgreSQL test chat (server accept time 0.32 seconds, down from 10.9; database writes from 533 MB to 2 KB per message) -- but that is a performance bullet, not the feature, so the script should spend it late, if at all. The strongest concrete case is the 0.13.0 blog's worked example: a failing test in the date-parser folder, the model fixing it and running python3 -m unittest, the viewer watching the diff in the Git panel and the app in the Browser tab, chat open the whole time. What could not be verified: community reaction to 0.13.5 (released hours before research; nothing fetched), a beta/preview label on the feature (absent from every fetched page), and Open WebUI's total install base (only GitHub "Used by 280", which counts dependent repos, not installs). One conflict: Hacker News commenters call the license source-available because the branding cannot be removed, while the README calls the platform open-source in spirit; the LICENSE file itself was never fetched, so the license stays out of Claims.

## Thesis
In Open WebUI 0.13.5, a sidebar folder becomes a project workspace: you pick one machine and one project directory once, and the chat, the terminal running your tests, and the browser showing your app all stay open beside each other.

## Explanation path
Open with the situation the viewer is already in: a local model in Open WebUI, and a real project on disk that the chat cannot see or touch; every code question means a copy-paste round trip. Establish what 0.13.5's Folder workspaces changes: the folder is no longer a tidy drawer for chats but a project workspace -- choose the computer and the project directory once for the folder, and its new chats inherit the default model, machine, working directory, system prompt and knowledge. Before the folder means anything, the viewer must connect one machine, Open Terminal, as a one-time admin step: one docker run, one entry under Settings > Admin > Integrations, switch on, model access set. With the folder bound, show the payoff as one live loop rather than a tour of buttons: give the model a job in the folder (the 0.13.0 blog's example is a failing test in the date-parser folder), watch the fix land in the Files tab's Git panel (click a change, see the diff), run the tests in the terminal tab, and try the app in the Browser tab while the chat stays open the whole time. Land the trust beat before the ending: the machine is a container you chose, not free rein -- the folder's machine and directory were picked once, and every tool call can be made to wait for a click (Ask for approval). Close on what the folder remembers: AGENTS.md or CLAUDE.md in the project folder is read by every new chat there, and the folder keeps its own tabs, so tomorrow it reopens where you left it.

## Claims
1. **Open WebUI v0.13.5 was released on 2026-11-25 at 09:37 UTC with Folder workspaces as the first item under Added.**
   - Source: Release v0.13.5, https://github.com/open-webui/open-webui/releases/tag/v0.13.5
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
2. **Folder workspaces let the viewer run the project's tests in a terminal and try the app in a browser while the chat stays open beside them, with the computer and project directory chosen once for the folder, and per-user tabs and layout even in a shared folder.**
   - Source: Release v0.13.5, https://github.com/open-webui/open-webui/releases/tag/v0.13.5
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
3. **The Folder workspaces feature replaces the standalone Open WebUI Computer (cptr) app by building that workflow into Open WebUI itself.**
   - Source: Release v0.13.5, https://github.com/open-webui/open-webui/releases/tag/v0.13.5
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
4. **Every new chat in a project folder reads the project's instructions from an AGENTS.md or CLAUDE.md file, and with Open Terminal 0.18.0 or later the assistant can follow reusable project skills, run checks in the terminal and inspect the result in a browser tab.**
   - Source: Release v0.13.5, https://github.com/open-webui/open-webui/releases/tag/v0.13.5
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
5. **Open WebUI's GitHub repository showed 159.5k stars, 23.1k forks and 888 contributors when fetched on 2026-11-25.**
   - Source: GitHub - open-webui/open-webui: User-friendly AI Interface (Supports Ollama, OpenAI API, ...), https://github.com/open-webui/open-webui
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
6. **Open WebUI is a self-hosted, offline-capable platform that connects local models through Ollama and OpenAI-compatible APIs, with a Docker image bundling Open WebUI with Ollama and Nvidia GPU support via --gpus all for the :cuda and :ollama images.**
   - Source: GitHub - open-webui/open-webui, https://github.com/open-webui/open-webui
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
7. **In the UI, clicking a folder in the sidebar makes it the active workspace, and new chats inherit the folder's default model, machine, working directory, system prompt and knowledge; the folder keeps its own tabs, so reopening it brings back the chats, files and terminals left open there.**
   - Source: Folders & Projects / Open WebUI, https://docs.openwebui.com/features/chat-conversations/chat-features/conversation-organization/
   - Tier: docs | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
8. **The machine behind a folder workspace is started with one Docker command using the default Open Terminal image, which is about 4 GB because the slim and alpine images do not include the desktop.**
   - Source: Open WebUI v0.13.0: Your Model Gets a Computer, https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
9. **Cursor and GitHub Copilot are among 13 coding agents selectable in Open WebUI's model picker, so the agent tool moves inside the self-hosted UI rather than the chat living inside the editor.**
   - Source: Open WebUI v0.13.4: Interactive Charts, Videos, and AI Agents, https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers
   - Tier: docs | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
10. **The pieces of folder workspaces arrived progressively across the 0.13.x line: v0.13.0 (03 Nov 2026) added the tabbed workspace, v0.13.1 added the working-directory picker, v0.13.4 (17 Nov 2026) made chats remember their terminal and folder and gave folder pages a chat board, and v0.13.5 binds one computer and project directory to the folder as the named feature.**
   - Source: Releases - open-webui/open-webui, https://github.com/open-webui/open-webui/releases
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract
11. **Upgrading to 0.13.5 converts existing database history because chats are now stored message-by-message; the release notes say to back up first and upgrade all workers and servers together because the old and new formats are incompatible.**
   - Source: Release v0.13.5, https://github.com/open-webui/open-webui/releases/tag/v0.13.5
   - Tier: primary | Confidence: high | Accessed: 2026-11-25 | Via: web_extract

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | message-send speedup, 130 MB PostgreSQL test chat | 34x faster | https://github.com/open-webui/open-webui/releases/tag/v0.13.5 | "Sending a message was 34x faster in our 130 MB PostgreSQL test chat." |
| 2 | server accept time, before to after | 0.32 seconds, down from 10.9 | https://github.com/open-webui/open-webui/releases/tag/v0.13.5 | "The server accepted it in 0.32 seconds, down from 10.9" |
| 3 | database writes per message, before to after | 533 MB to 2 KB per message | https://github.com/open-webui/open-webui/releases/tag/v0.13.5 | "Database writes fell from 533 MB to 2 KB per message." |
| 4 | GitHub stars (seen 2026-11-25) | 159.5k stars | https://github.com/open-webui/open-webui | "159.5k stars" |
| 5 | GitHub contributors (seen 2026-11-25) | 888 contributors | https://github.com/open-webui/open-webui | "888 contributors" |
| 6 | Open Terminal default Docker image size | about 4 GB | https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer | "Use the default image, about 4 GB, because the `slim` and `alpine` images don't include the desktop." |
| 7 | coding agents selectable in the model picker | 13 agents | https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers | "We support 13 agents: Claude Code, Codex, Cursor, Grok, OpenCode, Cline, Gemini CLI, Pi, Hermes, Antigravity, GitHub Copilot, Goose, and Qwen Code." |
| 8 | v0.13.5 release timestamp | 2026-11-25T09:37:38Z | https://github.com/open-webui/open-webui/releases/tag/v0.13.5 | "2 hours ago 2026-11-25T09:37:38Z" |

## Analogy candidates
- **Cursor's side chat**: 0.13.5 docks the chat beside your project's terminal, browser and files instead of beside your code editor; chat and artifacts share one folder. Breaks when: Cursor binds the chat to its editor and its vendor's models, while Open WebUI's folder drives any model or agent on hardware you host, and it is a web UI, not an IDE.
- **A workshop bench beside your phone call**: the chat is the call; the tabbed side panel (Files, terminal, Browser, Git) is the bench where the project work happens, and you can look over or grab the tools any time without hanging up. Breaks when: the model works at the bench too, not just you, and on a shared folder teammates share the bench while each keeps their own tab layout.

## Misconceptions
- Myth: Folder workspaces are just chat folders for tidying the sidebar, like ChatGPT's folders. Reality: new chats inherit the folder's default model, machine, working directory, system prompt and knowledge, and the folder keeps its own tabs for files and terminals (claim 7).
- Myth: You still need the separate Open WebUI Computer (cptr) app to work beside your chat. Reality: that workflow is now built into Open WebUI itself as of v0.13.5 (claim 3).
- Myth: The model gets free rein over your machine. Reality: the machine and directory are chosen once per folder, the machine is a container you start yourself, and every tool call can be made to wait for a click under Ask for approval (claims 7 and 8).
- Myth: A folder workspace is only for teams. Reality: the single-user loop works end to end: one Open Terminal container, one folder with Machine and Working directory set, tabs beside your own chat (claim 8).

## Glossary
- **Folder workspace**: a sidebar folder that has a computer and project directory chosen once, so its chats, files, terminals and browser tabs work in that project while the chat stays open beside them.
- **Open Terminal**: the self-hosted computer environment, connected once in Settings > Admin > Integrations, where the model runs commands and manages files; version 0.18.0 or later enables project skills.
- **Machine**: what v0.13.5 calls terminal connections: the computer a chat or folder uses for files and commands, managed under Machines.
- **cptr**: the standalone Open WebUI Computer app whose beside-your-chat workflow v0.13.5 folds into the main product.
- **AGENTS.md / CLAUDE.md**: a project instructions file whose contents every new chat in that project folder automatically reads.
- **Ask for approval**: the per-chat mode, enabled by an administrator's Tool Permissions setting, that makes every tool call wait for you to click Allow.

## Unverified
- Community reaction to v0.13.5: the release shipped hours before this research and no post, thread or article about it was found.
- Whether Folder workspaces carries a beta, preview or experimental label anywhere: neither the release notes nor the fetched docs page carries such a qualifier.
- Open WebUI's total install base: no downloads or Docker-pull figure was fetched; GitHub's "Used by 280" counts only GitHub-registered dependent repositories, not installs.
- Whether the license formally forbids removing branding: only Hacker News commenters said so; the LICENSE file was not fetched this session.
- The exact click-path a v0.13.5 user sees when first binding a machine to a folder: the docs describe the Edit Folder dialog's Advanced section, but a v0.13.5-specific walkthrough page was not fetched.
- How folder workspaces behave for Ollama-only users with no Open Terminal connected: no fetched page states a fallback for the Files and Browser tabs without a machine.
- Open WebUI deployments on DGX-class hardware: no fetched page mentions DGX; the README documents Nvidia GPU access only generally.

## Suggested outline
1. Open on the copy-paste pain: your model is in Open WebUI, your project is on disk, and every code question is a copy-paste round trip.
2. Tonight's move: connect one machine (one docker run, about 4 GB), create the folder, set Machine and Working directory once.
3. The payoff loop: failing test in the date-parser folder, model fixes it and runs the tests, you watch the diff in the Git panel and the app in the Browser tab while the chat stays open.
4. The trust beat: the machine is a container you chose and every tool call can wait for your click.
5. The ending: the folder remembers -- AGENTS.md is read by every new chat, and tomorrow the folder reopens with your tabs where you left them.

## Viewer situation
You've got Open WebUI serving a local model (through Ollama or an OpenAI-compatible API), and a real project folder on disk; to ask the model about your code you copy-paste snippets between the browser chat and your editor or terminal.

## Has process
true
- Update Open WebUI to v0.13.5, backing up first because the upgrade converts existing database history.
- Start the machine once with Docker: docker run -d --name open-terminal --restart unless-stopped -p 8000:8000 -v open-terminal:/home/user -e OPEN_TERMINAL_API_KEY=your-secret-key ghcr.io/open-webui/open-terminal
- Connect it in Open WebUI: Settings > Admin > Integrations, click + in the Open Terminal section, enter http://localhost:8000 and your key, set Access, and turn on the switch.
- Create the folder: click the + button on the Folders section header in the sidebar, select New Folder, enter a name, click Save.
- Edit the folder, and under Advanced pick the Machine and set the Working directory, choosing the computer and project directory once for the folder.
- Click the folder in the sidebar to make it the active workspace, so new chats are created inside it and inherit its default model, machine, working directory, system prompt and knowledge.
- Open the tabs beside the chat from the Tabs button: Files, terminal, Browser; drag them into order and switch with Use full-width tabs / Use side tabs.
- Give the model a job in that folder, such as "A test in the date-parser folder fails. Fix it and run python3 -m unittest. Don't commit."
- Review the work beside the chat: open the Git panel at the bottom of the Files tab, click a change to see its diff, then try the app in the Browser tab while the chat stays open.
- Optionally gate every action: pick Ask for approval from the + menu in the message box, then click Allow when the model stops.
- Write an AGENTS.md or CLAUDE.md in the project folder so every new chat there reads the project instructions.

## Objection
A skeptical engineer says: I already have Cursor or Claude Code docked in my editor with a real file tree and language server; Open WebUI's folder tabs are a browser pane over a Docker container, not an IDE, and the model is whatever local model I run, not Claude.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/open-webui/open-webui/releases/tag/v0.13.5 | Release v0.13.5 - open-webui/open-webui - GitHub | primary | web_extract | 2026-11-25 |
| 2 | https://github.com/open-webui/open-webui/releases | Releases - open-webui/open-webui - GitHub | primary | web_extract | 2026-11-25 |
| 3 | https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md | open-webui/CHANGELOG.md at main - open-webui/open-webui - GitHub | primary | web_extract | 2026-11-25 |
| 4 | https://github.com/open-webui/open-webui | GitHub - open-webui/open-webui: User-friendly AI Interface (Supports Ollama, OpenAI API, ...) | primary | web_extract | 2026-11-25 |
| 5 | https://docs.openwebui.com/features/chat-conversations/chat-features/conversation-organization/ | Folders & Projects / Open WebUI | docs | web_extract | 2026-11-25 |
| 6 | https://docs.openwebui.com/features/workspace/ | Workspace / Open WebUI | docs | web_extract | 2026-11-25 |
| 7 | https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer | Open WebUI v0.13.0: Your Model Gets a Computer | primary | web_extract | 2026-11-25 |
| 8 | https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers | Open WebUI v0.13.4: Interactive Charts, Videos, and AI Agents - Open WebUI Blog | docs | web_extract | 2026-11-25 |
| 9 | https://news.ycombinator.com/item?id=48346990 | Why not just use open webui? | Hacker News | community | web_extract | 2026-11-25 |

## Notes
The 34x/533 MB-to-2 KB numbers are real and verbatim but are release-note performance claims about long chats, not the folder feature; the script should not hang the hook on them (the pick's value types are EQUIPS and TEACHES, not PROVES). The worked example (failing date-parser test, python3 -m unittest, Git diff, Browser tab) comes from the official 0.13.0 blog and is the strongest act-tonight material. The 0.13.x timeline in claim 10 is the brief's differentiation against "this is a minor patch" -- the feature is three weeks of assembly, not one bullet. The audience already knows Open WebUI exists; the brief deliberately does not explain what it is, only what the folder now does.

## Decisions
- Checkpoint (step 2): confirmed angle "Folder workspaces put your project's files and tests beside the chat that serves the model" with slug 2026-11-25-open-webui-0-13-5-your-project; no redirect.
- Depth standard, 9 sources fetched across 3 research questions via one 3-worker fan-out (page contents cached under output/sources/, never entering the orchestrator context); FireCrawl unavailable (402), workers fell back to web search + fetch per rules/firecrawl-usage.md.
- The 34x performance number stays in Key numbers but is flagged in Notes as a late-spend number; the hook and payoff belong to the folder-workspace loop and the 4 GB container, which the viewer can act on tonight.
