[![logo](https://openwebui.com/logo.png)](https://openwebui.com/)

Product

Resources

[Community](https://openwebui.com/home) [Customers](https://openwebui.com/customers) [Sign In](https://openwebui.com/auth?type=login)

[All articles](https://openwebui.com/blog)

November 4, 2026 /10 MINUTES READ

![Open WebUI v0.13.0: your model gets a computer](https://community.s3.openwebui.com/uploads/users/6ddf0023-1d2a-4af3-bbbe-41612061a0d8/2026/11/dbfb01d0-0bcb-49ca-97b0-ab0cd6fa3e3e.png)

SUMMARY

v0.13.0 gives your team's models a computer. An administrator connects it once, and everyone with access gets a desktop, a browser, and a Git panel in tabs beside the chat, with nothing to install. Work passes between people through shared files, comment threads, and a notification inbox. Models can hand work to sub-agents on other models and write their own tools, and MCP servers can show interactive apps in the chat. The release includes security fixes and a database migration.

Open WebUI v0.13.0 gives your whole team's models a computer. An administrator connects it once, and everyone with access gets a real desktop, a real browser, and Git in tabs beside their chat, with nothing to install. One person's model finishes a job, and the next person carries on from the same files.

Anyone can watch their model work, take the mouse, or make every step wait for approval, and your team can review the result on the exact words. Each section below shows a feature, then walks you through trying it yourself. Most of the clips follow one demo team taking date-parser to v2.4.

## The short version [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#the-short-version)

- **A computer for your whole team.** Connect Open Terminal once, choose who gets it, and each person's model works on a real desktop and in a real browser, while they watch, step in, or approve each action.
- **Work that passes between people.** Models leave their work on shared files, teammates comment on the exact words, and mentions land in one inbox.
- **Git in the side panel.** Review what the model changed, then stage, commit, push, and work with pull requests without leaving the chat.
- **Tabs beside your chat.** Files, terminals, artifacts, previews, voice calls, and comments sit next to the conversation, and they can fill the whole window.
- **More capable models.** Sub-agents can run on other models, a model can write its own tools, and MCP servers can show interactive apps in the chat.

**Update as soon as you can.** v0.13.0 includes security fixes, and we'll publish the advisories once CVE numbers are assigned. It also includes a database migration, so back up first. A few changes need a decision, and [Before you upgrade](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer#before-you-upgrade) covers them.

## Give your team a computer [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#give-your-team-a-computer)

Hand a model work that lives in apps, not only in text, and let the next person carry on from it. It works on a desktop in a tab beside your chat, every click happens in front of you, and what it leaves behind is there for your team.

_Maya's model reads an import log in LibreOffice Calc and leaves a note, and Priya, on her own desktop, has her model pick it up_

Nobody installs anything. Each person picks the terminal in the message box and gets their own desktop, working on the same files as everyone else on that terminal. Take the mouse whenever you want, work the same apps yourself, check a document it made, or handle a step that needs manual input. Keyboard, clipboard, and audio come through too, where they're available.

**Try it.** The desktop runs through [Open Terminal](https://docs.openwebui.com/features/open-terminal/), a self-hosted environment where a model can run commands and manage files. You set it up once for the whole team, and the next sections use it too.

Start it with Docker, and swap in your own key. Use the default image, about 4 GB, because the `slim` and `alpine` images don't include the desktop.

```
$ docker run -d --name open-terminal --restart unless-stopped -p 8000:8000 -v open-terminal:/home/user -e OPEN_TERMINAL_API_KEY=your-secret-key ghcr.io/open-webui/open-terminal
```

Then, in Open WebUI:

_Open Terminal added in Settings, opened to the team, switched on, and picked in the message box, and the desktop appears_

1. Click your name at the bottom of the sidebar, and go to `Settings > Admin > Integrations`.
2. In the Open Terminal section, click +, enter `http://localhost:8000` and your key, and save. The [connection guide](https://docs.openwebui.com/features/open-terminal/setup/connecting) covers other setups.
3. Before you save, click Access and choose who gets it. Public opens it to everyone, or add groups and people. Until you do, only administrators can use it.
4. Turn on the switch next to your new connection. It starts off, and the Terminal menu won't appear until it's on.
5. Share the model too. In `Settings > Admin > Models`, open the model, click Access, and choose who gets it. If it's a custom model, do the same for the model it's built on, or teammates will see "Model not found".
6. Start a new chat with a model that has tool calling and image input, because desktop tools send screenshots.
7. In the message box, pick your terminal from the Terminal menu.
8. Click the Tabs button at the top of the chat, and open the Desktop tab from the + menu.
9. Send your request. We used this one:

> On the desktop, double-click failed-dates.csv to open it in LibreOffice Calc and read it the way I would. Then tell me which date format keeps failing, and save that to handoff.txt on the desktop for Priya.

You'll see the mouse move on the desktop, and the answer arrives in the chat. Then have a teammate sign in, repeat steps 7 and 8, and ask their model to read the file you left. We used this one:

> Maya left handoff.txt on the desktop. Read it and tell me which test we should add.

If it doesn't go that way:

- Ask the model to work the desktop itself, such as "double-click the file". A program it starts from the shell has no display, so it won't appear on the desktop.
- If a local model clicks in the wrong spot, tell it in the system prompt that clicks take pixel coordinates from the latest screenshot, and give the screenshot's size. Some local models answer on a 0 to 1000 grid until you say so.
- If nothing happens at all, check the model's tool-calling mode, which should be Native.

**Where it runs.** In the default Docker image, it's a Linux desktop inside the container, apart from everyone's own machines. Installed with `pip` on macOS or Windows, it's your own logged-in screen, so the model works as you. Use Docker for a team.

**Who shares what.** Everyone on one connection shares its files and running programs, which suits people working on the same thing. Set up more than one terminal and give each group its own. For a small, trusted team, [multi-user mode](https://github.com/open-webui/open-terminal#built-in-multi-user-mode) gives each person their own workspace. When people need to be protected from each other, [Terminals](https://github.com/open-webui/terminals) gives each person a separate container, and it needs an Enterprise License.

**Where screenshots go.** They go to the model you pick. A local model keeps them on your hardware, and a cloud model sends them to its provider.

We recorded these clips on the Docker image with Open Terminal v0.16.0, with `gpt-6.1-sol` as the main model and `gpt-6-luna` running the sub-agents.

### Tabs that hold everything [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#tabs-that-hold-everything)

We rebuilt the space beside your chat around tabs. Files, terminal sessions, artifacts, previews, voice calls, and comments now sit next to the conversation. Drag tabs into any order, and create new files that save straight into the selected terminal.

_Tabs take the whole window, then go back beside the conversation_

**Try it.** On a larger screen, click Use full-width tabs to give the tabs the whole chat area, with the conversation as a tab of its own. Click Use side tabs to go back. Open WebUI remembers your choice.

## Let it fix the code [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#let-it-fix-the-code)

You don't have to take a model's word for what it changed, and neither does your team. From here we follow date-parser, a small demo project with one failing test between it and v2.4. Hand the model that test, and the Git panel fills in as it works.

_The Changes list fills in as the model fixes a failing test, then a diff opens_

**Try it.**

1. With your terminal picked, open the Files tab and click into a folder that's a Git repository.
2. Open the Git panel at the bottom of the Files tab.
3. Give the model a job in that folder. We used this one:

> A test in the date-parser folder fails. Fix it and run python3 -m unittest. Don't commit.

Your changes appear in the panel as the model makes them, and clicking one opens its diff. Anyone on the same terminal can open that folder and see the same changes. From the same panel, you can stage, discard, and commit changes, manage branches and worktrees, push and pull, browse history, and work with GitHub pull requests. Open files can show their changes with Show diff. On terminals that support it, the panel, the list of open ports, and running processes update as soon as something changes.

## Review it together [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#review-it-together)

A fix isn't finished until someone else has looked at it. Your team can review a model's work right where it happened, on the exact words, without pasting anything into another app.

_A comment on one sentence mentions a teammate, whose window opens the highlighted passage_

**Try it.**

1. Turn on Comments in `Settings > Admin > General`, or set `ENABLE_COMMENTS`.
2. Select a passage in a chat message or a note page, and click Comment.
3. Type your comment, and use @ to mention a teammate.

The passage stays highlighted, and your teammate lands on it. The Comments tab in the side panel, which `/comments` opens, holds the thread, with replies and reactions. Comments work on chats, notes, models, knowledge bases, prompts, skills, and tools.

### Ask something on the side [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#ask-something-on-the-side)

Ask a quick question without derailing the conversation.

_`/btw` opens a side chat that answers outside the main conversation_

**Try it.** Type `/side` or `/btw` in a chat, or choose Side chat in the side panel, and a temporary conversation opens with the chat so far as context. Nothing from it is added to the main chat, and it disappears when you close its tab. Side chats are for administrators and people with the new Allow Side Chat permission, which is off by default.

### One inbox for what needs you [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#one-inbox-for-what-needs-you)

Mentions, replies, and failed automation runs all land in one place, the Inbox we added to the sidebar.

_A mention arrives, and the inbox lists it beside a failed automation run_

**Try it.** It's already on. Click the bell at the top of the sidebar to see comments on your items, replies, mentions in comments and channels, failed automation runs, and upcoming calendar events. Administrators can turn it off in `Settings > Admin > General`, or with `ENABLE_NOTIFICATIONS`.

## Let it test in a browser [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#let-it-test-in-a-browser)

A model can now check what it builds the way you would. With the fix reviewed, we asked for the v2.4 announcement page, and the model built it, served it, and opened it in a browser you share.

_The model builds a small page on the terminal, serves it, and checks it in the shared browser_

**Try it.**

1. Make sure you're on Open Terminal v0.16.0 or later, with your terminal picked in the message box.
2. Open the Browser tab from the + menu.
3. Ask the model to build something and check it. We used this:

> Make a one-page site in a release-notes folder in my home folder announcing date-parser v2.4: ISO dates like 2026-11-02 now parse. Serve it on port 5173, then open it in the browser and check it.

The page opens in the tab, and you can use it at the same time as the model. We added the Browser tab with navigation controls, multiple tabs, and a mobile viewport, and it opens websites and local development servers. Chrome mode gives you and the model one shared browser session, so it can navigate sites, fill in forms, and test web apps. Proxy mode is still there for previews. The browser tools need Chrome, and the [README](https://github.com/open-webui/open-terminal#configuration) lists the settings.

**On the open web,** a page can carry instructions aimed at the model, local or not. For sites you don't control, run Open Terminal in Docker, keep Ask for approval on, and stay signed out of accounts you care about. The model can use whatever you're signed in to in that shared session. Published Docker images turn off Chromium's own sandbox so it can start under Docker's default restrictions. If your runtime allows it, set `OPEN_TERMINAL_BROWSER_NO_SANDBOX=false` to turn it back on.

## Stay in control [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#stay-in-control)

You don't have to sit and watch while a model works. Turn on approvals, and every tool call waits for you, including the desktop and browser tools. We put a "Waiting for approval" marker in the sidebar, so you can work in another chat and come back when you're needed.

_A tool call waits in one chat while the sidebar shows its marker from another_

**Try it.**

1. An administrator turns on Tool Permissions in `Settings > Admin > Interface`, or sets `ENABLE_TOOL_PERMISSIONS`.
2. Open the + menu in the message box, and pick Ask for approval.
3. Ask the model to use a tool, then click Allow when it stops.

The default is Full access, where tool calls run straight away.

## Run apps in your chat [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#run-apps-in-your-chat)

A reply can now be a working app. We added MCP apps, so a tool from an MCP server can show an interactive app right in the conversation after it runs. MCP servers are outside tools that a model can call. For date-parser, that's the team's release board, where the fix moves to Done.

_A release board drawn by an MCP server, and the confirmation before it moves a card_

**Try it.**

1. Connect an MCP server that comes with an app in `Settings > Admin > Integrations`, and use Access to choose who gets it.
2. In the message box, open Integrations, then Tools, and switch it on.
3. Ask for it. We typed "Show me the v2.4 release board."

The app sits in a sandboxed frame that can only reach the sites the server declares, and every tool call it wants to make waits for you to confirm it.

## More for everyone [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#more-for-everyone)

### Sub-agents on other models [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#sub-agents-on-other-models)

Put a large model in charge, and let small ones take the simple questions. We made sub-agents work across models, so you can assign research, coding, and review to different models.

_A small model picked in the Sub-agents list, then sub-agents on it reading three vendor notes_

**Try it.**

1. Turn on Enable sub-agents in `Settings > Admin > Sub-agents`, or set `ENABLE_SUBAGENTS`. They're off by default, and they have no limits unless you set them.
2. Edit a model in the model editor, and pick the models it can hand work to in its Sub-agents list.
3. Ask it to split up a job. Everyone who uses that model gets the same setup, and the parent chooses among the models each person can access.

To give a sub-agent a terminal file, have the model put the file's path or its text in the task.

### Models that write their own tools [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#models-that-write-their-own-tools)

Ask a model for a tool it doesn't have, and it writes one. With native function calling, it can create a private Python tool in your workspace, ready to use again.

_The model writes a temperature converter, which then opens from Workspace > Tools_

**Try it.** Ask for the tool in plain words, then find it in `Workspace > Tools`. It's there for administrators and for people allowed to create workspace tools, and you can turn it off for a model under Tool Creation in its builtin tools.

### Controls beside the message box [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#controls-beside-the-message-box)

Everything you set for one chat now sits next to where you type.

_Setting a chat's system prompt from Controls beside the message box_

**Try it.** Open Controls from the model controls menu next to the message input. We moved a chat's files, valves, system prompt, and advanced parameters there. The button at the top of the chat opens the tabbed side panel instead.

### Models in 3D [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#models-in-3d)

Open a 3D file without leaving Open WebUI. We built a viewer you can rotate and zoom.

_An STL file from the terminal in the 3D viewer_

**Try it.** Click a GLB, glTF, STL, OBJ, or PLY file in a terminal's file browser, or in a file shown in a reply.

### Small things you'll notice [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#small-things-youll-notice)

- Every block in a note has a handle, so you can drag it or move it up or down.
- Code blocks in notes have a Copy button.
- The rename field at the top of a chat has the sparkle button that generates a title.
- From 768 pixels wide, channel threads and a note's pages and chat open beside the content, not over it.
- The PowerPoint preview draws pie, doughnut, and horizontal bar charts.
- Terminal files show their size in the toolbar, and the file browser can sort by date added.
- Hovering a reaction in a channel shows who reacted.

### More accessibility work [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#more-accessibility-work)

We kept going after the [last release's work](https://openwebui.com/blog/v0-12-4-and-v0-12-5-accessibility-and-shared-notes). Screen readers now hear a name for every window, form field, setting, and icon button, and keyboard users can answer tool approvals, dismiss notifications, resize the sidebar, and reach every event on the calendar. Closing a window opened from a menu returns focus to the menu button.

_A tool approval answered with the keyboard alone_

## More for administrators [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#more-for-administrators)

### A switch for every tool [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#a-switch-for-every-tool)

You can now take a tool out of use without deleting it. Every tool in `Workspace > Tools` has an on and off switch, for everyone who can edit it. A tool that's switched off can't be picked or run in any chat, including chats where it was already selected.

_Switching a tool off takes it out of the chat's Tools menu_

### Limits for knowledge bases [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#limits-for-knowledge-bases)

You can now cap how many files a knowledge base holds, how large each file may be, and how many go in with one upload. Set them for all knowledge bases in `Settings > Admin > Documents`, or with `KNOWLEDGE_MAX_FILE_COUNT`, `KNOWLEDGE_MAX_FILE_SIZE`, and `KNOWLEDGE_MAX_UPLOAD_COUNT`. A knowledge base's owner can set tighter file count and size limits under Advanced, and the global limits always apply.

_A file count limit set for every knowledge base, then an upload stopped at the limit_

### Open WebUI Desktop 0.1 [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#open-webui-desktop-01)

We refocused the separately installed app for macOS, Windows, and Linux on setting up and running Open WebUI on your own computer, with optional llama.cpp local models. It has a slimmer interface, searchable settings, startup logs, and optional automatic updates. [Download v0.1.4](https://github.com/open-webui/desktop/releases/tag/v0.1.4).

### Other smaller changes [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#other-smaller-changes)

- System prompts, saved prompts, and API chat requests can use `{{USER_ROLE}}`, which becomes the signed-in user's role.
- When the same model handles a conversation and its compaction summary, eligible requests reuse the conversation's prompt structure, so the provider can use its prompt cache.
- Chat Completions API clients get the expected streaming format when the upstream model uses the Responses API.

## Before you upgrade [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#before-you-upgrade)

Back up your database and data first. v0.13.0 changes the database schema, so going back to an earlier version means restoring that backup. Read the first three rows below before you start the new version.

| What changed | What to do |
| --- | --- |
| Database schema changes. Mixing versions across workers, servers, or load-balanced instances causes failures | Back up, then update all instances at the same time |
| Sub-agent limits now default to no limit. They were 20 at once, 20 in the background, 30 tool loops each, and 30,000 characters of output | If you use sub-agents and want limits, set them in `Settings > Admin > Sub-agents`, or with `SUBAGENTS_MAX_CONCURRENT`, `SUBAGENTS_MAX_ASYNC`, `SUBAGENTS_MAX_ITERATIONS`, and `SUBAGENTS_MAX_OUTPUT` |
| Models with native function calling can create private Python tools, for administrators and people allowed to create workspace tools | To stop this for a model, turn off Tool Creation in its builtin tools in the model editor |
| One response can run up to 1,024 rounds of tool calls, up from 256 | Set `CHAT_RESPONSE_MAX_TOOL_CALL_ITERATIONS` to 256 to keep the old limit |
| Controls moved from the top of the chat to the model controls menu next to the message input | Let your users know. The top button now opens the side panel |
| The chat Overview now opens as a full-screen window from the chat's menu | Nothing |
| The Inbox is on by default | Turn it off in `Settings > Admin > General`, or with `ENABLE_NOTIFICATIONS`, if you don't want it |
| Personal notifications no longer offer "Retrieval Content process failed", so webhooks don't get that alert | If you rely on it, watch file processing another way |
| Open WebUI Desktop no longer switches between remote servers, bundles Open Terminal, or has the old Spotlight and global voice overlays | See the [Desktop 0.1.0 release notes](https://github.com/open-webui/desktop/releases/tag/v0.1.0). The Desktop and Browser tabs use a separately configured Open Terminal |

When you're ready, the [updating guide](https://docs.openwebui.com/getting-started/updating) has the steps, and the [release notes](https://github.com/open-webui/open-webui/releases/tag/v0.13.0) list every change.

## Where to start [\#](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer\#where-to-start)

Give your team a computer: follow [the steps above](https://openwebui.com/blog/v0-13-0-your-model-gets-a-computer#give-your-team-a-computer), and hand it something real to do. Then bring in a teammate, and have them pick up what it left and comment on it. Tell us what you build, and what you'd like next, on the [issue tracker](https://github.com/open-webui/open-webui/issues).

_The Open WebUI Team_

## AI on your terms.

Your models. Your data. Your infrastructure.

[Get started →](https://docs.openwebui.com/getting-started/) [Enterprise sales →](https://openwebui.com/contact/sales)

* * *

### Related articles

[![Open WebUI v0.12.4 and v0.12.5: screen readers, shared notes, and session analytics](https://community.s3.openwebui.com/uploads/users/6ddf0023-1d2a-4af3-bbbe-41612061a0d8/2026/11/35be16ce-89a1-4e2e-90b3-b683570ebf42.png)\\
\\
news\\
\\
/\\
\\
November 4, 2026\\
\\
Open WebUI v0.12.4 and v0.12.5: screen readers, shared notes, and session analytics\\
\\
Open WebUI v0.12.4 and v0.12.5 let a screen reader follow a chat from start to finish, give notes pages and live presence, and show where your tokens go.\\
\\
![Open WebUI](https://openwebui.com/user.png)\\
\\
Open WebUI\\
\\
Admin](https://openwebui.com/blog/v0-12-4-and-v0-12-5-accessibility-and-shared-notes) [![Put your model to real work in Open WebUI](https://community.s3.openwebui.com/uploads/users/6ddf0023-1d2a-4af3-bbbe-41612061a0d8/2026/11/495fce26-10de-4456-bf2c-04dfc805b653.png)\\
\\
Guide\\
\\
/\\
\\
November 18, 2026\\
\\
Put your model to real work in Open WebUI\\
\\
Our team uses Codex and Claude Code in Open WebUI for software engineering, documents, and most other work, from a desk, a phone, or a tablet. Here's how that works.\\
\\
![Open WebUI](https://openwebui.com/user.png)\\
\\
Open WebUI\\
\\
Admin](https://openwebui.com/blog/put-your-model-to-real-work-in-open-webui) [![What is Open Terminal, the computer your model works on in Open WebUI](https://community.s3.openwebui.com/uploads/users/6ddf0023-1d2a-4af3-bbbe-41612061a0d8/2026/11/63383664-e2aa-4d07-948f-95f3f4234cbb.png)\\
\\
Guide\\
\\
/\\
\\
November 18, 2026\\
\\
What is Open Terminal, the computer your model works on in Open WebUI\\
\\
Open Terminal gives the model in Open WebUI a real computer to run commands, edit files, and use coding agents on. What it is, and how to set it up from scratch.\\
\\
![Open WebUI](https://openwebui.com/user.png)\\
\\
Open WebUI\\
\\
Admin](https://openwebui.com/blog/what-is-open-terminal-in-open-webui)

We use optional analytics to improve our websites, and advertising cookies on this site. [Privacy Policy](https://openwebui.com/privacy).

AcceptReject