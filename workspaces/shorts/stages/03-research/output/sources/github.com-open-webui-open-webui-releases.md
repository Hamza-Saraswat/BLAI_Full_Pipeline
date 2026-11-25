[Skip to content](https://github.com/open-webui/open-webui/releases#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/open-webui/open-webui/releases) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/open-webui/open-webui/releases) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/open-webui/open-webui/releases) to refresh your session.Dismiss alert

{{ message }}

Releases · open-webui/open-webui

## v0.13.5

[v0.13.5](https://github.com/open-webui/open-webui/releases/tag/v0.13.5)[Latest](https://github.com/open-webui/open-webui/releases/latest)

[Latest](https://github.com/open-webui/open-webui/releases/latest)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

2 hours ago
25 Nov 09:37


[v0.13.5](https://github.com/open-webui/open-webui/tree/v0.13.5)

[`926f826`](https://github.com/open-webui/open-webui/commit/926f826eaef6179c092a936eede6c7363e425975)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Nov 25, 2026, 04:37 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- **Folder workspaces.** Run your project’s tests in a terminal and try the app in a browser while your chat stays open beside them. Choose the computer and project directory once for the folder. Even in a shared folder, everyone can return to their own tabs and layout. If you used the standalone Open WebUI Computer (cptr) app, that workflow is now built into Open WebUI. [#34804](https://github.com/open-webui/open-webui/pull/34804), [#34805](https://github.com/open-webui/open-webui/pull/34805), [#34800](https://github.com/open-webui/open-webui/issues/34800), [#34803](https://github.com/open-webui/open-webui/issues/34803)
- **Project instructions and skills.** Tell the assistant how your project works once in an `AGENTS.md` or `CLAUDE.md` file. Every new chat in that project folder reads those instructions. Connect the project machine with Open Terminal 0.18.0 or later and the assistant can also follow reusable project instructions called skills, run checks in your terminal and inspect the result in your browser tab.
- **Long chat performance.** Sending a message was 34× faster in our 130 MB PostgreSQL test chat. The server accepted it in 0.32 seconds, down from 10.9, because it now saves just the messages that changed. Database writes fell from 533 MB to 2 KB per message. [#34689](https://github.com/open-webui/open-webui/pull/34689), [#34671](https://github.com/open-webui/open-webui/pull/34671), [#34688](https://github.com/open-webui/open-webui/issues/34688), [#34672](https://github.com/open-webui/open-webui/issues/34672), [#34674](https://github.com/open-webui/open-webui/issues/34674), [#34670](https://github.com/open-webui/open-webui/issues/34670), [#34646](https://github.com/open-webui/open-webui/issues/34646)
- **Automatic model selection.** Put one router in the chat’s model picker and it can send coding questions to one model and writing requests to another. Admins choose text patterns or describe the kind of question each model should handle. If nothing matches, the router uses the first model on its list or picks one at random. [#34900](https://github.com/open-webui/open-webui/pull/34900), [#34895](https://github.com/open-webui/open-webui/pull/34895), [#34791](https://github.com/open-webui/open-webui/pull/34791), [#34796](https://github.com/open-webui/open-webui/pull/34796), [#34908](https://github.com/open-webui/open-webui/pull/34908), [#34662](https://github.com/open-webui/open-webui/pull/34662), [#34956](https://github.com/open-webui/open-webui/pull/34956), [#34957](https://github.com/open-webui/open-webui/pull/34957), [#34887](https://github.com/open-webui/open-webui/issues/34887), [#34786](https://github.com/open-webui/open-webui/issues/34786), [#34793](https://github.com/open-webui/open-webui/issues/34793), [#34897](https://github.com/open-webui/open-webui/issues/34897), [#34898](https://github.com/open-webui/open-webui/issues/34898), [#34466](https://github.com/open-webui/open-webui/discussions/34466), [#15996](https://github.com/open-webui/open-webui/discussions/15996)
- **Citations beside the chat.** Hover over a source number for a quick excerpt, or click it to read the evidence beside the answer. You can compare passages from the same document, see how closely they match your question and jump to the cited PDF page when page information is available. [#34923](https://github.com/open-webui/open-webui/pull/34923), [#34836](https://github.com/open-webui/open-webui/pull/34836), [#34921](https://github.com/open-webui/open-webui/issues/34921), [#34828](https://github.com/open-webui/open-webui/issues/34828), [#34831](https://github.com/open-webui/open-webui/issues/34831), [#34832](https://github.com/open-webui/open-webui/issues/34832), [#34833](https://github.com/open-webui/open-webui/issues/34833), [#34913](https://github.com/open-webui/open-webui/issues/34913), [#34834](https://github.com/open-webui/open-webui/issues/34834), [#34829](https://github.com/open-webui/open-webui/issues/34829), [#20829](https://github.com/open-webui/open-webui/discussions/20829)
- **Steer a coding agent while it works.** If Codex or Claude Code starts editing the wrong file, send a correction in the same chat. The coding agent can act on a text follow-up while the job is running. A follow-up with attachments waits for the next turn so the agent receives the instruction and files together.
- **Recurring tasks can continue a conversation.** Schedule a morning status report in the same chat or channel thread each day. The automation reads the replies people added since its last run, so today’s report can account for a decision someone posted yesterday afternoon. [#33731](https://github.com/open-webui/open-webui/discussions/33731)
- **Use a remote computer from chat.** Connect a workstation over SSH, the same secure connection you use to log in remotely, and work with its files and command-line tools from chat. This setup requires Open Terminal 0.17.21 or later and supports Linux on x86-64 or ARM64 and Apple silicon Macs.
- **Follow work delegated by a chat.** When the assistant gives a task to another agent, open Status in the original chat and choose the agent under Threads. You can read its progress, approve a tool call or stop the job. Status also shows how much of the model’s available space for messages is in use and how many messages and tasks are waiting. [#34917](https://github.com/open-webui/open-webui/issues/34917), [#33262](https://github.com/open-webui/open-webui/issues/33262), [#34408](https://github.com/open-webui/open-webui/discussions/34408)
- **Generate videos with ComfyUI.** Describe a scene or attach a starting image to make a video in chat. Admins import a video-generation workflow from ComfyUI into Admin Settings > Images & Videos in API format and choose which inputs control the prompt, dimensions, frame count and frame rate. People using chat can then run it without opening ComfyUI. [#6343](https://github.com/open-webui/open-webui/issues/6343)
- **Ask another saved chat for help.** With sub-agents enabled, a planning chat can ask one of your coding chats why it chose a particular approach. An idle chat wakes up to handle the question, while a busy chat receives it between tool calls. A link shows the receiving chat which conversation asked.
- **Start an automation from another service.** A form submission can now trigger a task in Open WebUI and pass the submitted answers into its prompt. Give the form service the automation’s secret webhook URL so it knows where to send the data. The same task can also run on a schedule. [#26090](https://github.com/open-webui/open-webui/issues/26090)
- **Share an automated task.** Let teammates see a task’s past runs or give them permission to run it and change its schedule. When someone starts a shared automation, it runs with the owner’s permissions. The owner controls its instructions, model, variables and the secret URL external services use to trigger it. [#29527](https://github.com/open-webui/open-webui/discussions/29527)
- **Faster chat opening.** Start typing in a new chat while models and tools load. Reopening a saved chat also fetches the conversation and model list in parallel. In a 500-message test on a 5 Mbit/s connection, the messages appeared and the input was ready about a second sooner. [#34869](https://github.com/open-webui/open-webui/pull/34869), [#34842](https://github.com/open-webui/open-webui/pull/34842), [#34868](https://github.com/open-webui/open-webui/issues/34868), [#34841](https://github.com/open-webui/open-webui/issues/34841), [#34863](https://github.com/open-webui/open-webui/issues/34863), [#34874](https://github.com/open-webui/open-webui/issues/34874), [#34919](https://github.com/open-webui/open-webui/issues/34919)
- **Faster startup with connected tools.** After a restart, people can use chat while the server finishes connecting to external tools and machines. Even deployments without a shared Redis cache can reuse connection details on later requests, so opening another chat doesn’t repeat the same setup. [#34856](https://github.com/open-webui/open-webui/pull/34856), [#34866](https://github.com/open-webui/open-webui/pull/34866), [#34855](https://github.com/open-webui/open-webui/issues/34855), [#34865](https://github.com/open-webui/open-webui/issues/34865)
- **Notes in folders.** Keep a project brief in the same sidebar folder as the chats where you discuss it. Drag the note into the folder and it inherits the folder’s read or edit access, so the people already working there can use it too. [#34894](https://github.com/open-webui/open-webui/issues/34894), [#24242](https://github.com/open-webui/open-webui/discussions/24242)
- **Conversation-wide citations.** A source keeps its number throughout a saved conversation. If a model cites a report as “source 3,” you can come back several replies later, ask how source 3 supports a claim and still be talking about the same report.
- **Preview the files behind an answer.** Search a knowledge base you’ve attached to a chat and open its files beside the conversation to check what they contain. When attaching a large document, you can choose whether the assistant reads it in full or retrieves passages relevant to your question.
- **Limit how much tool output reaches the model.** A command can return a log so long that the model has little room left for earlier messages. Set `TOOL_OUTPUT_MAX_CHARS` to limit how many characters from each result go into the conversation. If a machine is connected, the model can still open the full output as a file. [#30110](https://github.com/open-webui/open-webui/issues/30110)
- **Faster shared chat search.** Find an old conversation faster, even on a site where thousands of chats have been shared. Search checks which chats you can open before looking through messages. In one PostgreSQL test with 61,000 chats, a two-word search under All fell from 18.2 seconds to 1.4. [#34911](https://github.com/open-webui/open-webui/pull/34911), \[ [#34903](https://github.com/open-webui/open-webui/issues/34903)\]( [https://gith](https://gith/)...

[Read more](https://github.com/open-webui/open-webui/releases/tag/v0.13.5)

Assets2

- [Source code (zip)](https://github.com/open-webui/open-webui/archive/refs/tags/v0.13.5.zip)

2 hours ago2026-11-25T09:37:38Z

- [Source code (tar.gz)](https://github.com/open-webui/open-webui/archive/refs/tags/v0.13.5.tar.gz)

2 hours ago2026-11-25T09:37:38Z


👍5Classic298, nahoj, kulbhushanchand, digin1, and Harvester62 reacted with thumbs up emoji🎉3Classic298, D-Kuzin, and kulbhushanchand reacted with hooray emoji❤️1Classic298 reacted with heart emoji🚀2Classic298 and maiconzucco reacted with rocket emoji👀1Classic298 reacted with eyes emoji

All reactions

- 👍5 reactions
- 🎉3 reactions
- ❤️1 reaction
- 🚀2 reactions
- 👀1 reaction

7 people reacted

## v0.13.4

[v0.13.4](https://github.com/open-webui/open-webui/releases/tag/v0.13.4)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

last week
17 Nov 14:46


[v0.13.4](https://github.com/open-webui/open-webui/tree/v0.13.4)

[`0666e59`](https://github.com/open-webui/open-webui/commit/0666e59d26a4d056e0bacee41742486badd71cf8)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Nov 17, 2026, 09:40 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- **Bring your own computer with Tether.** Tether turns your own computer into part of Open WebUI: models from Ollama, LM Studio or any OpenAI-compatible server, OpenAPI and MCP tool servers and Open Terminal servers that you add in the Tether app now show up just for you in the model selector, the Tools list of the + menu and the terminal menu of any Open WebUI you connect, from whatever device you open it on, and Open WebUI reaches them through Tether, so their addresses, commands and keys never leave your computer. This needs Tether 0.1.14 or later, or 0.1.16 for MCP servers, tool servers and terminals need "ENABLE\_TOOL\_SERVERS" turned on, and a Tether model whose ID matches a model already in Open WebUI stays hidden. Tether replaces Direct Connections. [#34397](https://github.com/open-webui/open-webui/issues/34397)
- **Sandboxed agents on your own computer.** Tether 0.1.13 or later can lock the terminal on your computer into a sandbox, so models and coding agents work in your real files without reaching the rest of your machine: on macOS and supported Windows devices, Open Terminal and everything it launches, coding agents included, can only touch the one folder you pick, run offline unless you turn on Network access and accept no incoming connections, with no Docker, virtual machine or administrator setup needed. If the sandbox cannot be enforced, the terminal stays stopped instead of quietly running without it, and browser and desktop control stay off while it is on. Turn it on in Tether under Settings > Open Terminal > Sandbox.
- **Local MCP servers through Tether.** Open WebUI can now use MCP servers that run as a local command over stdio, the way many MCP servers are distributed, by launching them on your computer through Tether 0.1.16 or later, with no proxy such as mcpo and no port to open. Add one in Tether under Settings > Integrations > Tools with its command, or connect an MCP server by its web address, and pick it from the Tools list of the + menu. Local commands run with your own account's access, outside Tether's workspace sandbox.
- **A computer for every user.** With Terminals 0.4.0 or later connected, Open WebUI now hands out sandboxed computers on demand: anyone with Write access to the connection can create a terminal right from the terminal menu of the message input, pick whether everyone shares one machine or each user, chat or model gets its own, and set its image, CPU, memory, storage, network profile, environment variables, start directory and a setup script that, for example, clones a repository and installs its dependencies, without an administrator setting up each one. Terminals can be shared with users and groups and their instances started, stopped, restarted or deleted, a View files option opens any terminal's files without selecting it for the chat, System info shows how the setup script went, and those who manage a terminal can open the files and system info of other people's running instances. Start and Stop need Terminals 0.4.1 or later, the start directory and setup script need Open Terminal 0.17.7 or later in the terminal's image, and network profiles are the ones an administrator defined with "TERMINALS\_NETWORK\_PROFILES".
- **Coding agents as chat models.** Coding agents now work much like any other model in the chat. Hermes, Antigravity, GitHub Copilot, Goose and Qwen Code join Codex, Claude Code, Cursor, Grok, OpenCode, Cline, Gemini CLI and Pi, and any other ACP agent added to Open Terminal with "OPEN\_TERMINAL\_ACP\_AGENTS" works as well, once it is installed and signed in on the terminal. Auto for tool permissions now lets Codex, Claude Code and Grok approve routine actions themselves and pass on only what they escalate, and the reasoning effort in the advanced parameters now also applies to Claude Code, Pi and ACP agents that offer effort levels, such as OpenCode, which stop with an error when the chosen level is not offered for the model. Replies can now be regenerated and earlier messages edited, and a forked or cloned agent chat picks up where the original left off: Codex continues its own conversation from that point, other agents start over from the chat so far, and file changes the agent already made stay. Claude Code continues its own conversation too with the next Open Terminal release after 0.17.20 and until then asks you to update Open Terminal instead. The new agents and Auto for Claude Code and Grok need Open Terminal 0.17.19 or later, and effort for Claude Code, Pi and ACP agents needs 0.17.9 or later. [#34167](https://github.com/open-webui/open-webui/issues/34167)
- **Pages open as tabs.** Notes, channels, the workspace, automations, the calendar, the playground, the home page and new chats from pinned models now open as tabs beside the current chat when you click or drag them from the sidebar, pick them in the user menu or follow a link to one of them in a chat message, and starting a new chat, also from a sidebar folder, keeps the open tabs.
- **Queued messages steer replies.** A message you send to your own chat while a reply is still running now waits on the server, so it is kept when you leave the page, and the reply wraps up at its next step so your message is answered right away with what it has done so far.
- **Instant first message.** The first message of a new chat now shows up right away while the chat is still being created, instead of only once it exists, unless files are still being uploaded with it.
- **Full chat in side chats.** Side chats now run the same chat as the main view, so message buttons, sources, token usage, follow-up suggestions, slash commands, queued messages, chat variables, web search settings, tool events such as code execution and input requests, HTML and SVG previews, notifications while the window is in the background, unsent text after a page reload and answers from several models at once now work there too, and a side chat's tab now has the chat menu. [#34064](https://github.com/open-webui/open-webui/pull/34064), [#34165](https://github.com/open-webui/open-webui/pull/34165), [#34147](https://github.com/open-webui/open-webui/pull/34147), [#34031](https://github.com/open-webui/open-webui/issues/34031)
- **Interactive visualizations.** Models can now draw interactive charts, diagrams, calculators and explainers right in the chat with the new Visualizations built-in tool, which is off by default and turned on per model under Builtin Tools, and administrators can rewrite its instructions under Admin Settings > Interface > Visualization Prompt or with "VISUALIZATION\_PROMPT\_TEMPLATE".
- **Video generation.** Models can now generate videos with a built-in tool, also starting from an image in the chat, once an administrator turns on Video Generation under Admin Settings > Videos, adds connections to OpenAI, LiteLLM or OpenRouter, which offers models such as Veo and Kling, with a default video model, per-model defaults and access settings, and grants the Video Generation permission, which is off by default, after which users turn on Video in the + menu, can pick the model there and watch the result in the chat. [#13780](https://github.com/open-webui/open-webui/discussions/13780), [#13927](https://github.com/open-webui/open-webui/discussions/13927)
- **Several image models.** Administrators can now add several image connections under Admin Settings > Images, each an OpenAI-compatible server such as LiteLLM, Gemini, ComfyUI or AUTOMATIC1111 with its own models, sizes, workflows and access, used for generating images, editing them or both, where OpenAI-compatible ones offer the same sign-in options and custom headers as model connections and list the image models of a LiteLLM server by themselves when no model IDs are entered, choose the default generation and edit models and give a model its own default image model in its settings, and users with more than one image model pick one from the Image entry in the + menu of the message input. [#10344](https://github.com/open-webui/open-webui/discussions/10344)
- **Git panel becomes a GitHub workbench.** With Open Terminal 0.17.8 or later and the GitHub CLI signed in on the terminal, as included in the full, agents and cuda images, the Git panel now covers the whole GitHub loop: browse, search, create, edit, comment on, close and reopen the repository's issues, see each pull request's checks, review state, labels, activity and conflicts with a status filter and a choice of merge method, and search issues and pull requests across the whole repository instead of only the loaded list. Buttons such as Work on this, Fix, Address feedback and Resolve conflicts in chat hand the issue, review or conflict to the model as a ready-made request in the message input, and changed files can be picked with Ctrl or Shift click to discard several at once or all of them.
- **Terminals follow your chats.** Each chat now saves its terminal and working folder and switches back to them when you reopen it, including a terminal you turned off, and administrators can pick a default terminal under Admin Settings > Models > Model Defaults that new chats start with for every model without a terminal of its own, so every chat can start with a computer attached. Chats from earlier versions open without a terminal unless they are coding agent chats.
- **Folder chat board.** Folder pages now list their chats with a search through titles and messages and filters for status, tags, people, activity and last update, and can show them as a board with columns and rows by status, tag or activity such as unread, generating or waiting for approval, gives each chat there the sidebar's chat menu to rename, move, archive or delete it, and a folder's badge in the sidebar now also counts chats waiting for approval. [#33771](https://github.com/open-webui/open-webui/issues/33771)
- **Chat statuses in folders.** Folders can now set up statuses for their chats under Edit statuses, with Backlog, To do, In progress, Wai...

[Read more](https://github.com/open-webui/open-webui/releases/tag/v0.13.4)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍32silentoplayz, onihilist, donatas-xyz, gromflomite, sma33in, oteissonniere, Neobyte82, rlax777, Classic298, Kylapaallikko, and 22 more reacted with thumbs up emoji😄4silentoplayz, Classic298, clutteredSchemaVPN, and Bobyyy70 reacted with laugh emoji🎉16blueinkgz, silentoplayz, antebudimir, onihilist, defmmg-cell, Classic298, DesertGun, ctg49, Cabeda, JonPC4, and 6 more reacted with hooray emoji❤️7silentoplayz, jdstu30, donatas-xyz, rlax777, Classic298, i-iooi-i, and akiraaisha reacted with heart emoji🚀7silentoplayz, defmmg-cell, Classic298, asoderlind, i-iooi-i, akiraaisha, and ChrisCaponeLima reacted with rocket emoji👀4silentoplayz, defmmg-cell, Classic298, and akiraaisha reacted with eyes emoji

All reactions

- 👍32 reactions
- 😄4 reactions
- 🎉16 reactions
- ❤️7 reactions
- 🚀7 reactions
- 👀4 reactions

48 people reacted

## v0.13.3

[v0.13.3](https://github.com/open-webui/open-webui/releases/tag/v0.13.3)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

2 weeks ago
08 Nov 23:48


[v0.13.3](https://github.com/open-webui/open-webui/tree/v0.13.3)

[`b0e6098`](https://github.com/open-webui/open-webui/commit/b0e6098e940942281d9c83f3529ea117287a3a22)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Nov 8, 2026, 06:48 PM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- 🦾 **Agents in automations.** The automation editor now lets you choose a terminal and working folder, then select a coding agent available there. Scheduled runs use that saved terminal and folder, and check that the terminal and agent are still available before starting. Agent automations send their results to a chat; channel destinations remain available for ordinary models. [Commit](https://github.com/open-webui/open-webui/commit/21fc016141c73a0e11b428c61bde20527bbc228a)
- 📂 **Change terminal and folder during a chat.** You can now choose a different terminal or working folder after sending messages, including in temporary chats. Both controls remain disabled while a reply is being generated. [Commit](https://github.com/open-webui/open-webui/commit/a518ff1630b74ed6edd62538c5da4bb26cc6dd20)
- 🇧🇷 **Brazilian Portuguese translations.** Added missing translations for terminal and folder controls, Git actions, spreadsheet editing, voice notes, tab shortcuts, notification sounds and tool settings. Updated the explanations for document retrieval, tool permissions and voice settings. [#33945](https://github.com/open-webui/open-webui/pull/33945)

### Fixed

- 📂 **Files tabs follow terminal changes.** Switching a chat to another terminal now updates its open Files tabs to show that terminal's files, instead of leaving the previous terminal's folders on screen. With a terminal set to "Per chat", the Files tab also switches to the chat's own files after the first message. [#33954](https://github.com/open-webui/open-webui/pull/33954)
- 🧭 **Agents in unsupported model pickers.** Connecting a terminal no longer adds its coding agents to Admin Models, base-model selectors, Arena candidates, task-model settings, group defaults, sub-agent settings, channel mentions or the Playground. Notes also stop choosing a terminal agent for title generation. Agents cannot be saved or imported as custom models or their base models, and their chat menu no longer offers Edit. [Commit](https://github.com/open-webui/open-webui/commit/21fc016141c73a0e11b428c61bde20527bbc228a), [Commit](https://github.com/open-webui/open-webui/commit/6d3123b5b4a90962bff44c69c7e0bae0c65557d5)
- 🔌 **Agent list after switching terminals.** Changing terminals immediately removes the previous terminal's agents from the chat's model list while the new list loads. A model-list request from a chat you have left can no longer replace the current list. [Commit](https://github.com/open-webui/open-webui/commit/21fc016141c73a0e11b428c61bde20527bbc228a)
- 📋 **Copy buttons over plain HTTP.** At a plain HTTP address on your local network, copying comment links, search links, shared-chat links, webhook URLs, chat IDs, Git branch names, commit hashes and spreadsheet cells now works. Copy Formatted Text preserves formatting, and copied text keeps its final line break. [#33939](https://github.com/open-webui/open-webui/pull/33939)
- 📝 **Clipboard prompts and Auto-Copy Response over plain HTTP.** Prompts using the clipboard placeholder now insert into chats and channels even when the browser blocks clipboard access, with a message explaining that the clipboard could not be read. Auto-Copy Response stays off and shows a permission message instead of silently failing to turn on; turning it off no longer requires clipboard access. [#33939](https://github.com/open-webui/open-webui/pull/33939)
- 🧠 **DeepSeek thinking mode with skills, knowledge and memories.** These chats no longer fail with a missing reasoning error when the connection's Provider is set to "llama.cpp". DeepSeek thinking mode still requires that setting; connections using "Default" are unchanged. [#33950](https://github.com/open-webui/open-webui/pull/33950)
- 🏷️ **Labels on grouped tool calls.** With Tool Call Labels enabled, a group of tool calls keeps the labels that are present even if one call has none. The unlabeled call shows its tool name instead of making the whole group lose its labels. [#33932](https://github.com/open-webui/open-webui/pull/33932)
- 💬 **Tool labels in later replies.** The model now sees the labels it wrote for earlier tool calls when continuing a reply or answering another message, removing a reason it could stop writing labels as the conversation continued. [#33953](https://github.com/open-webui/open-webui/pull/33953)
- 🔎 **Knowledge searches containing punctuation.** Searches in knowledge files now find text such as "Art. 40" when the model marks the period as literal punctuation, instead of returning no matches. [#33936](https://github.com/open-webui/open-webui/pull/33936)
- 🪟 **Side Chat with Temporary Chat disabled.** Leaving Enforce Temporary Chat switched on while disabling Temporary Chat no longer prevents users from sending and saving side chats or dragging an existing chat into the side panel. [#33930](https://github.com/open-webui/open-webui/pull/33930)
- 🏠 **Home folder tab title.** A Files tab at the connected machine's home directory now says "Home" instead of showing the directory name, including when reopening saved tabs. Other folders keep their names. [Commit](https://github.com/open-webui/open-webui/commit/241c8c0e47e19b0adeb13d577ca538d2252b0ad4)
- 🦙 **Missing Ollama in Docker images.** Building the image that includes Ollama now fails if Ollama was not installed, instead of producing an image that cannot start Ollama after its download failed. [#33944](https://github.com/open-webui/open-webui/pull/33944)
- 📄 **Errors after leaving a chat.** Closing or leaving a chat while its tab layout is being saved no longer fills the server log with an error report for the dropped connection. [#33929](https://github.com/open-webui/open-webui/pull/33929)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍37silentoplayz, Classic298, killfrenzy96, oteissonniere, sultan-young, i-iooi-i, Koutzin, denisshutov23021985-netizen, AndreXSchmidt, marc1077, and 27 more reacted with thumbs up emoji😄3silentoplayz, Classic298, and kaeferpsd reacted with laugh emoji🎉7silentoplayz, Classic298, blueinkgz, i-iooi-i, Koutzin, kaeferpsd, and ivanbaldo reacted with hooray emoji❤️10silentoplayz, Classic298, i-iooi-i, GioF71, tariktalay, FriedVariable, kaeferpsd, Flagy, damienosborne78, and ivanbaldo reacted with heart emoji🚀5silentoplayz, Classic298, i-iooi-i, kaeferpsd, and ivanbaldo reacted with rocket emoji👀6silentoplayz, Classic298, kaeferpsd, kkliuiev, ivanbaldo, and Doors5Misha44444e reacted with eyes emoji

All reactions

- 👍37 reactions
- 😄3 reactions
- 🎉7 reactions
- ❤️10 reactions
- 🚀5 reactions
- 👀6 reactions

43 people reacted

## v0.13.2

[v0.13.2](https://github.com/open-webui/open-webui/releases/tag/v0.13.2)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

2 weeks ago
08 Nov 11:53


[v0.13.2](https://github.com/open-webui/open-webui/tree/v0.13.2)

[`b7a005e`](https://github.com/open-webui/open-webui/commit/b7a005e5a5c0c0d869f2aebf4b8f051c5fb37245)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Nov 8, 2026, 06:53 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Fixed

- 🔓 **Chat over plain HTTP.** Opening Open WebUI over plain HTTP at a LAN or Docker address now loads new and existing chats instead of staying on a spinner with "crypto.randomUUID is not a function". [#33919](https://github.com/open-webui/open-webui/issues/33919)
- 📝 **Comments and Markdown editing over plain HTTP.** Creating, replying to and editing comments, and editing Markdown files containing rendered blocks such as Mermaid diagrams or callouts, no longer fail with the same UUID error. [Commit](https://github.com/open-webui/open-webui/commit/3c400952cbb30e8eb72652d83b2af2f75a3b9341)
- 🎛️ **Side Chat permission switch.** The Allow Side Chat switch is now visible even when Temporary Chat is off, so administrators can configure the two permissions independently. [#33920](https://github.com/open-webui/open-webui/pull/33920)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍22m5moshbk, madnight, kulbhushanchand, Classic298, k-shopnil, donatas-xyz, verygoodgirl, rlax777, Jxstin1337, showmidelo, and 12 more reacted with thumbs up emoji😄2silentoplayz and chrisbagsrocks reacted with laugh emoji🎉9blueinkgz, sponger544, D-Kuzin, Classic298, DesertGun, devmidnightst, silentoplayz, i-iooi-i, and chrisbagsrocks reacted with hooray emoji❤️12mixmafritz, Classic298, rlax777, nacifyas, T100D, hbusul, misternapps, devmidnightst, silentoplayz, i-iooi-i, and 2 more reacted with heart emoji🚀4silentoplayz, Classic298, i-iooi-i, and chrisbagsrocks reacted with rocket emoji👀2silentoplayz and chrisbagsrocks reacted with eyes emoji

All reactions

- 👍22 reactions
- 😄2 reactions
- 🎉9 reactions
- ❤️12 reactions
- 🚀4 reactions
- 👀2 reactions

31 people reacted

## v0.13.1

[v0.13.1](https://github.com/open-webui/open-webui/releases/tag/v0.13.1)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

2 weeks ago
08 Nov 11:07


[v0.13.1](https://github.com/open-webui/open-webui/tree/v0.13.1)

[`bbd199a`](https://github.com/open-webui/open-webui/commit/bbd199ae506e58a3e951452099fa04329b9589ea)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Nov 8, 2026, 06:07 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- 🦾 **Coding agents as models.** On an Open Terminal that offers agents, coding agents such as Claude Code, Codex and Pi now appear in the model picker. You can chat with them or call them by voice, choose their reasoning effort and service tier, and approve their tool requests in the chat. Each conversation uses one agent, and agent chats cannot be regenerated, continued or edited and resent. If an agent's terminal goes away, its chats and new chats fall back to the default model and earlier replies keep the agent's name. Autocompletion in agent chats uses the task model, or is skipped when there is none. [#33843](https://github.com/open-webui/open-webui/pull/33843), [#33860](https://github.com/open-webui/open-webui/pull/33860), [#33880](https://github.com/open-webui/open-webui/pull/33880), [#33857](https://github.com/open-webui/open-webui/pull/33857)
- 🪢 **Introducing Tether.** [Tether](https://github.com/open-webui/tether) is the new desktop companion app for macOS, Windows and Linux that ties your own computer to Open WebUI. Sign in once and your computer shows up under Your devices in the terminal menu, so models, coding agents and automations can work in your real files, repositories and tools, and you can reach them from any browser, including your phone. Tether connects out to Open WebUI, so there are no ports to open, its terminal output resumes after a dropped connection, and it delivers notifications to your desktop even when no Open WebUI page is open. It signs in with a renewable session that expires after 90 days without use by default, set with "SESSION\_EXPIRES\_IN".
- 💸 **Much cheaper tool chats.** Chats that use tools now cost much less. Citation instructions, memory recall, the skills list and attached knowledge are no longer rewritten into the system prompt or your message on every tool round, so the start of the conversation stays the same between requests and providers can serve it from their prompt cache. Custom pipes see a different message layout as a result; see Context as hidden tool results under Changed. [#33852](https://github.com/open-webui/open-webui/issues/33852)
- 🚦 **Auto tool permissions.** Administrators can now turn on Auto, a third tool permission mode next to Full access and Ask for approval (off by default). A review model checks each tool call and runs it right away only when it judges that no confirmation is needed. The review sends the tool, its arguments and your last few messages to the configured scoring API, and any call it cannot review, because of an error, a timeout or too much context, asks for approval.
- 📚 **Full text for small files.** Files whose extracted text is shorter than a new threshold (50,000 characters by default, set with "RAG\_FULL\_TEXT\_CHAR\_THRESHOLD" or in the admin Documents settings) are now included in full instead of through retrieval. This applies both when Preload files adds the content to the conversation and when the model reads an attached file with its file search tool, and the file viewer shows when it happens.
- ⏱️ **Faster large chats.** Large chats now open about twice as fast, and marking a chat as read or unread or removing a tag from it is 4 to 6 times faster. [#33665](https://github.com/open-webui/open-webui/pull/33665), [#33666](https://github.com/open-webui/open-webui/pull/33666)
- 🏎️ **Faster chat access checks.** Sending messages, typing indicators, shared links, comments and file access no longer load the whole conversation just to check who may access it, which helps most on large chats. [#33667](https://github.com/open-webui/open-webui/pull/33667), [#33669](https://github.com/open-webui/open-webui/pull/33669)
- 🔧 **More forgiving tool calls.** Tool calls with arguments wrapped in code fences, encoded twice or sent as text instead of numbers and booleans now run, and tool calls a model writes out as plain text markup are recognised and executed. [#33868](https://github.com/open-webui/open-webui/issues/33868)
- 🛑 **Tool loop stops.** A tool call that fails twice in a row with the same arguments now ends the tool loop so the model writes a final answer, and a reply cut off by the token limit no longer runs its unfinished tool calls.
- 🛠️ **Default tools for models.** The Model Defaults section in the admin Models settings now has a Tools picker, models without their own tool list start new chats with those tools enabled, and the new model form preselects them. [#33749](https://github.com/open-webui/open-webui/pull/33749), [#33787](https://github.com/open-webui/open-webui/pull/33787)
- 🚀 **Faster channels.** The channel list, the channel messages and the replied-to messages in a channel now load much faster, especially with many channels or many replies, and new database indexes speed up channel threads and reactions. [#33690](https://github.com/open-webui/open-webui/pull/33690), [#33691](https://github.com/open-webui/open-webui/pull/33691), [#33688](https://github.com/open-webui/open-webui/pull/33688)
- 🪶 **Lighter reasoning streams.** Long reasoning replies from providers such as OpenRouter now send far less data to the browser and to Redis while they stream. [#33698](https://github.com/open-webui/open-webui/pull/33698)
- 🗂️ **Faster sidebar chat list.** The chat list in the sidebar now appears as soon as its own data is ready instead of waiting for the channel list. [#33686](https://github.com/open-webui/open-webui/pull/33686)
- ⌨️ **Faster typing after large pastes.** Typing in the chat input after pasting 16,000 lines of text is now about 117 times faster, down from 8.6 seconds to 74 milliseconds per keystroke. [#33729](https://github.com/open-webui/open-webui/pull/33729), [#12087](https://github.com/open-webui/open-webui/issues/12087)
- 🧮 **Faster Redis filter lookups.** With Redis enabled, chat requests now look up the filters of a model faster. [#33668](https://github.com/open-webui/open-webui/pull/33668)
- 🪟 **Split tab panes.** On large screens, dragging a tab or a chat to the edge of the workspace, or pressing the new Split screen button, splits it into resizable panes, so several tabs, including the chat, stay visible side by side. Tabs can also be reordered and moved between panes with a long press and drag on touch screens. [Commit](https://github.com/open-webui/open-webui/commit/b5eaa59d0a5f85a85940bd2ec1afb4aa4ff21a80)
- 🧳 **Tabs remembered per chat.** The open tabs, split layout and selected terminal of each chat are now saved privately for each user on the server and restored when you reopen the chat, even on another device. Signing out warns you about unsaved file edits. [#33899](https://github.com/open-webui/open-webui/pull/33899), [#33885](https://github.com/open-webui/open-webui/pull/33885)
- 🪣 **Batched Tool Search calls.** With Tool Search on, the model can run several independent tools it found in a single call\_tool request, which saves model turns and so lowers the cost of tool-heavy chats.
- 🧭 **Tool Search engines.** Tool Search in the admin Interface settings can now match tools with embeddings from the Documents embedding model (kept in memory, not stored) or by sending the query and tool definitions to a relevance-scoring API, besides the default keyword search.
- 🏷️ **Readable tool call labels.** Administrators can now turn on Tool Call Labels in Admin Settings > Interface or with "ENABLE\_TOOL\_CALL\_LABELS", off by default, to ask the model for short descriptions in the user's language of what each tool call is doing and what it did. [Commit](https://github.com/open-webui/open-webui/commit/2416b1fc0b83571652e0efff83f9591c89b62a64)
- ✂️ **Chat read limit.** Admins can limit how much of an earlier chat the Chat History tools return, with "VIEW\_CHAT\_MAX\_CHARS" or the new Chat Read Limit field in Admin Settings > General, and the newest messages are kept while older ones are cut. [#33695](https://github.com/open-webui/open-webui/pull/33695), [#33608](https://github.com/open-webui/open-webui/issues/33608)
- 🌍 **Client IP header placeholders.** Custom headers of connections can now use "{{USER\_IP}}" and "{{X\_FORWARDED\_FOR}}" to pass the client address on to the upstream provider, and both are empty for automations and background jobs. [#33833](https://github.com/open-webui/open-webui/pull/33833), [#33819](https://github.com/open-webui/open-webui/issues/33819)
- ✉️ **Non-ASCII email addresses.** The sign-up page and the add and edit user dialogs now accept email addresses with non-ASCII characters. [#33693](https://github.com/open-webui/open-webui/pull/33693), [#33681](https://github.com/open-webui/open-webui/issues/33681)
- 🕒 **Reply finish time.** Assistant replies now show the time they finished instead of the time the prompt was sent. [#33895](https://github.com/open-webui/open-webui/pull/33895)
- 🧐 **Channel message search.** Each channel header has a Search button that searches the messages of that channel.
- 🔔 **Notifications open their chat.** Clicking a desktop notification now brings Open WebUI to the front and opens the related chat, channel or calendar.
- 📮 **MCP Apps message the chat.** An MCP App can now send a text message to the chat, which you confirm first in a Confirm Prompt from Embed dialog. [#33907](https://github.com/open-webui/open-webui/pull/33907)
- 🖱️ **Drag chats into side panel.** Dragging a chat from the sidebar onto the chat area opens it as a side chat tab, and a side chat can now also be started from an empty new chat.
- 🪄 **Quick open files.** A new shortcut, Cmd+P (Ctrl+P elsewhere), opens a search box that finds files in the selected terminal by name or path and opens the one you pick in a tab.
- 🎹 **Tab keyboard shortcuts.** New shortcuts, which can be changed in Settings > Keyboard, open the Files, Desktop, Comments, new chat, new file, new terminal and new browser tabs, close and switch between tabs and toggle the split screen.
- 🗺️ **Working directory picker.** The message input has a working directory menu with folder search, a Recently Used lis...

[Read more](https://github.com/open-webui/open-webui/releases/tag/v0.13.1)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍14oteissonniere, Classic298, XboxFlow, FreeWeeFee, rosimelade, donatas-xyz, Jxstin1337, engideer-tech, silentoplayz, enelbit, and 4 more reacted with thumbs up emoji😄3Classic298, nacifyas, and silentoplayz reacted with laugh emoji🎉4Classic298, silentoplayz, i-iooi-i, and ivanbaldo reacted with hooray emoji❤️4Classic298, silentoplayz, i-iooi-i, and ivanbaldo reacted with heart emoji🚀5Classic298, fakezeta, silentoplayz, i-iooi-i, and ivanbaldo reacted with rocket emoji👀5Classic298, rosimelade, verygoodgirl, silentoplayz, and ivanbaldo reacted with eyes emoji

All reactions

- 👍14 reactions
- 😄3 reactions
- 🎉4 reactions
- ❤️4 reactions
- 🚀5 reactions
- 👀5 reactions

17 people reacted

## v0.13.0

[v0.13.0](https://github.com/open-webui/open-webui/releases/tag/v0.13.0)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

3 weeks ago
03 Nov 12:23


[v0.13.0](https://github.com/open-webui/open-webui/tree/v0.13.0)

[`c38885a`](https://github.com/open-webui/open-webui/commit/c38885a1a737da4968f157092f304f3b5481d0bf)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Nov 3, 2026, 07:21 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- 📑 **Tabbed workspace.** The Tabs button at the top of a chat now opens a workspace for files, multiple terminal sessions, artifacts, previews, voice calls and comments. Add tabs from the + menu, drag to reorder them, and create and save new files directly into the selected terminal. Keep the conversation and its working files together while coding, analyzing data or reviewing generated documents. [Commit](https://github.com/open-webui/open-webui/commit/2d7cf5ec99c3fa5c7ee48b91823fb8021b846cf3), [Commit](https://github.com/open-webui/open-webui/commit/5b58b1ebc03024fca1efd498aeabe4d9880dc3aa), [Commit](https://github.com/open-webui/open-webui/commit/a06aa230f75cc2d3512d1bca197a98f3c35da96f), [Commit](https://github.com/open-webui/open-webui/commit/cdc6feecd3769aac41844d81bd775dfb69b44912)
- 🖥️ **Open Terminal Desktop tab for computer use.** Open the Desktop tab from the + menu to view and control the desktop provided by your connected Open Terminal, with mouse, keyboard, clipboard and audio support where available. With a model that can call its desktop tools, you can follow computer-use workflows in the same desktop and step in yourself: operate graphical apps, inspect generated documents or handle a step that needs manual input. Requires an Open Terminal connection with desktop support enabled. [Commit](https://github.com/open-webui/open-webui/commit/b51e68fbb3e641e7f9027f5164fcf6b0e111cf27), [Commit](https://github.com/open-webui/open-webui/commit/3bd0cdd0f3cc075420540462f2bf246c73236495), [Commit](https://github.com/open-webui/open-webui/commit/03401a6e331d25425533933da85d3e5496deca3f), [Commit](https://github.com/open-webui/open-webui/commit/6dd3cc216f63085d2a1105117c65064c3e0ca3b6)
- 🌐 **Browser tab for browser use and web app testing.** Open websites and local development servers beside your chat, with navigation controls, multiple tabs and a mobile viewport. On a compatible Open Terminal connection, Chrome mode gives you and the model a shared browser session for browser automation: navigate sites, interact with forms and test the web apps the model builds. You can watch the work and interact with the page yourself; Proxy mode remains available for previews. Requires browser support on the selected terminal, and Chrome availability for browser-use tools. [Commit](https://github.com/open-webui/open-webui/commit/fbe69b01fd58a374211d348a28eb5988b11d41de), [Commit](https://github.com/open-webui/open-webui/commit/3bd0cdd0f3cc075420540462f2bf246c73236495), [Commit](https://github.com/open-webui/open-webui/commit/9260e312fb4238b504652eff0d8ca45445ca0821)
- ↔️ **Full-width tabs.** On larger screens, expand the tabbed workspace to fill the chat area, with the main conversation kept as its own tab. Switch between the chat, code, browser and desktop with more room to work, or return to the side-by-side layout; your layout choice is remembered. [Commit](https://github.com/open-webui/open-webui/commit/09030d5dd2def4324d98c25f92cf54b1ec1844f1), [Commit](https://github.com/open-webui/open-webui/commit/1ce8616ab9587ca717015d5af9cb26ee4296311f)
- 💻 **Open WebUI Desktop 0.1.x.** The separately installed app for macOS, Windows and Linux now focuses on setting up and running Open WebUI on your own computer, with optional llama.cpp local models. The 0.1.0–0.1.4 updates bring a slimmer interface, searchable settings, startup logs, optional automatic Desktop updates, start-to-tray controls and image copying and saving. They also improve screen sharing, knowledge folder uploads, Linux graphics and shortcuts, and NVIDIA/AMD local-model setup and updates. Use it for a managed local installation and local AI workflows. [Desktop changelog](https://github.com/open-webui/desktop/blob/v0.1.4/CHANGELOG.md), [Download v0.1.4](https://github.com/open-webui/desktop/releases/tag/v0.1.4)
- 🌿 **Git in the side panel.** When the selected terminal's folder is a Git repository, a Git panel in the tabbed side panel now lets you review diffs, stage, discard and commit changes, manage branches and worktrees, push and pull, browse history and work with GitHub pull requests, and open files can show their changes with Show diff. [Commit](https://github.com/open-webui/open-webui/commit/58926cfe7b98aab83c2544714d26cdbcc90722a3), [Commit](https://github.com/open-webui/open-webui/commit/3e24a08f8ec8472dcbbc46e7e39ab35aaa4a6f4f), [Commit](https://github.com/open-webui/open-webui/commit/30f0779d12072f98b2c3ce1b08819c72ab9c66d8), [Commit](https://github.com/open-webui/open-webui/commit/295b0778938cb9a133712b1bda4a18df92406375), [Commit](https://github.com/open-webui/open-webui/commit/250108302e6d73406c643a51eb5d9f80d39ddc03)
- ⚡ **Live terminal updates.** On terminals that support it, the Git panel, the list of open ports and the running processes and their output now update as soon as something changes instead of every few seconds. [Commit](https://github.com/open-webui/open-webui/commit/c4c10aa2559e10883797e3dd6702e16dc36eff19), [Commit](https://github.com/open-webui/open-webui/commit/70c5e38fc7ce3864426b484c07ee201cba2b9d07)
- 💭 **Side chats.** Typing "/side" or "/btw" in a chat, or choosing Side chat in the side panel, now opens a temporary side conversation using the chat so far as context. Ask a quick question or explore an alternative without adding the detour to the main conversation; the side chat disappears when you close its tab. Available to administrators and users given the new Allow Side Chat permission, which is off by default. [Commit](https://github.com/open-webui/open-webui/commit/321701c1af09d58f9ed6b67a22416ab8ddcfa165), [Commit](https://github.com/open-webui/open-webui/commit/151f7a84d1ca6949234671cd86d697abbce76444), [Commit](https://github.com/open-webui/open-webui/commit/27963030eccda5b8b27905ec0a35d5d9f09788e6)
- 💬 **Comment threads.** Administrators can now turn on Comments in Admin Settings > General or with "ENABLE\_COMMENTS", which lets users leave comments with replies, reactions and mentions on the chats, notes, models, knowledge bases, prompts, skills and tools they can open, including on a selected passage of a chat message, which then stays highlighted in the reply, or of a note page, shown in a Comments tab in the chat's side panel, which "/comments" opens, and with comment counts in the workspace lists. [Commit](https://github.com/open-webui/open-webui/commit/9d1b4ef362f103f2dda05760a44c96df82c064fd), [Commit](https://github.com/open-webui/open-webui/commit/91e8deee74c627fee29c4c81833766040334170f), [Commit](https://github.com/open-webui/open-webui/commit/63312766f8de94bc8a054d7923f2f83410b841a2), [Commit](https://github.com/open-webui/open-webui/commit/04d78a483de671dbe789082b79638f9e44078819)
- 🔔 **Notification inbox.** A new Inbox in the sidebar collects comments on your items, replies to your comments, mentions in comments and channels, replies in channels, failed automation runs and upcoming calendar events with an unread count, and administrators can turn it off in Admin Settings > General or with "ENABLE\_NOTIFICATIONS". [Commit](https://github.com/open-webui/open-webui/commit/3814b7b2f152c671fd3789e5a0099313d5316467), [Commit](https://github.com/open-webui/open-webui/commit/1a870d9481630861fe6d63de835d983df50b72c3), [#19539](https://github.com/open-webui/open-webui/issues/19539)
- 🧩 **MCP Apps in chat.** Tools from MCP servers that come with an interactive app now show that app right in the chat after they run, in a sandboxed frame that can only reach the sites the server declares, and every tool call the app wants to make waits for you to confirm it. [Commit](https://github.com/open-webui/open-webui/commit/0e0ba872a4d3e70c4e19e5c62b05fd7187b917f3), [Commit](https://github.com/open-webui/open-webui/commit/4ab90a6c1ff9526640e73ad37e67e88e693e2172), [#21040](https://github.com/open-webui/open-webui/discussions/21040), [#20915](https://github.com/open-webui/open-webui/discussions/20915)
- ✨ **Generate title from top bar.** The rename field at the top of an open chat now has the same sparkle button as the sidebar, which generates a title from the conversation and saves it right away. [#33382](https://github.com/open-webui/open-webui/pull/33382)
- 📐 **Side panels on tablets.** On screens from 768 pixels wide, such as tablets and narrow windows, channel threads and the pages list and chat in notes now open beside the content instead of over it, picking a terminal opens its files beside the chat as well, and the search dialog shows its preview there by default and remembers whether you turned it on or off at any window size. [Commit](https://github.com/open-webui/open-webui/commit/cbeb8e3630cafd7ef6fd28b552bf7114729f21b9), [Commit](https://github.com/open-webui/open-webui/commit/c5981aaea6b25bb9b9601e62b9ff75da33aaaf4e)
- 📊 **More PowerPoint charts.** The PowerPoint preview now draws pie, doughnut and horizontal bar charts as well as values below zero, and shows "Chart preview unavailable" for charts it cannot draw. [Commit](https://github.com/open-webui/open-webui/commit/09fbbd6d69293084d9e09cbb7d3b93e5d305ec5c), [#32884](https://github.com/open-webui/open-webui/issues/32884)
- 🧊 **3D model previews.** GLB, glTF, STL, OBJ and PLY files in a terminal's file browser and in files shown in chat replies now open in a 3D viewer that you can rotate and zoom. [Commit](https://github.com/open-webui/open-webui/commit/fe0d22cc24ddc2421b4e36a66a174188cc61d265)
- 🔘 **Switch tools on and off.** Tools in Workspace > Tools now have an on and off switch for everyone who can edit them, and a tool that is switched off can no longer be picked or run in any chat, including chats where it was already selected. [Commit](https://github.com/open-webui/open-webui/commit/9d1b4ef362f103f2dda05760a44c96df82c064fd)
- 🛠️ **Tool creation from chat.** Models with native function calling can now create a private Python tool in your workspace when you ask them to, for administrators and users allowed to create workspace tools, and it ca...

[Read more](https://github.com/open-webui/open-webui/releases/tag/v0.13.0)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍55gromflomite, q8itz, oteissonniere, andrecrafts, Kasraaam, Classic298, czj44223-cloud, zragon, D-Kuzin, sauer-adrian, and 45 more reacted with thumbs up emoji😄3silentoplayz, ivanbaldo, and developer-tvn reacted with laugh emoji🎉14blueinkgz, marc1077, xjulian3x, steffenboe, vb2007, silentoplayz, GersonnVelasquez, Secrumanthy, hknet, endash9, and 4 more reacted with hooray emoji❤️15xjulian3x, frankhuurman, ralf-mens, dancormier, chris282, Harvester62, silentoplayz, hbusul, shaqagain, digitalwannabe, and 5 more reacted with heart emoji🚀12sokai, JonPC4, DesertGun, donatas-xyz, parsalotfy, maiconzucco, chris282, sverstegen, silentoplayz, i-iooi-i, and 2 more reacted with rocket emoji👀3EgrorBs, silentoplayz, and ivanbaldo reacted with eyes emoji

All reactions

- 👍55 reactions
- 😄3 reactions
- 🎉14 reactions
- ❤️15 reactions
- 🚀12 reactions
- 👀3 reactions

73 people reacted

## v0.12.5

[v0.12.5](https://github.com/open-webui/open-webui/releases/tag/v0.12.5)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

last month
29 Oct 09:08


[v0.12.5](https://github.com/open-webui/open-webui/tree/v0.12.5)

[`f7ac7ee`](https://github.com/open-webui/open-webui/commit/f7ac7ee10962ddec0017f5c29b6740d9b9c5faca)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Oct 29, 2026, 05:05 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- 🧭 **Analytics session explorer.** Administrators can now open a Sessions tab in Admin Analytics that lists each chat with its tokens, responses, errors and time span, filters them by search, model, token range or sub-agents, and shows a chat's saved replies and tool calls with their timing and outcome, as long as "ENABLE\_ADMIN\_CHAT\_ACCESS" is on. [Commit](https://github.com/open-webui/open-webui/commit/7b303cf496f22d665ff1f1013a2308de0d74a7a4)
- 📑 **Pages in notes.** Notes can now hold several pages and subpages, which you can add, rename, reorder, move under another page, download, link to and delete from the page tabs, and search results and the model now work with notes page by page. [Commit](https://github.com/open-webui/open-webui/commit/b34885efc639c10cbf06c35cd2d4ff6055e36b45)
- 👀 **Live presence in notes.** A note now shows who else has it open, and clicking a person jumps to the page and spot they are working on. [Commit](https://github.com/open-webui/open-webui/commit/e3ad014fb250c663a124ada0046c4017b85aabd6)
- ✏️ **Rename from chat menu.** The menu next to an open chat's title now has Rename, which turns the title at the top of the page into a text box, so a chat can be renamed without finding it in the sidebar first. [#33177](https://github.com/open-webui/open-webui/pull/33177), [#33176](https://github.com/open-webui/open-webui/discussions/33176), [#33246](https://github.com/open-webui/open-webui/issues/33246), [#33339](https://github.com/open-webui/open-webui/pull/33339), [#33338](https://github.com/open-webui/open-webui/issues/33338), [Commit](https://github.com/open-webui/open-webui/commit/551b03ff90bddaa2bbdac49d76d2bab61367e895), [Commit](https://github.com/open-webui/open-webui/commit/f517e528d2f2865c6e730966343eef6c02c064b8)
- 🖼️ **Generated images in terminals.** When a terminal is selected in a chat, generated and edited images are now also saved to its working folder, so the model can keep working on them with the terminal's tools. [Commit](https://github.com/open-webui/open-webui/commit/b420726ff1f04dff07a2877511b30ebe7b9887bb)
- 🗃️ **Models show chat files.** Models can now show a file attached in the chat or stored in an attached knowledge base right in the reply with the built-in display\_file tool, which until now only worked for terminal files. [#32471](https://github.com/open-webui/open-webui/issues/32471), [Commit](https://github.com/open-webui/open-webui/commit/f2cdbbebe3cb40aab77516515198c7fa6c4818b7), [Commit](https://github.com/open-webui/open-webui/commit/ef29fb12f1f641bf1d83b434a37298846d211deb)
- 💾 **Chat model choice saved.** Changing the model in a chat is now saved with the chat right away, so the chat reopens with that model even when no message was sent after the change. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013)
- ⌨️ **Unassign single shortcuts.** Settings > Keyboard now shows a small x beside every assigned shortcut that unassigns only that one, so a shortcut such as Regenerate Response on Ctrl+R or Cmd+R can be switched off while all others keep working. [#33185](https://github.com/open-webui/open-webui/pull/33185), [#31463](https://github.com/open-webui/open-webui/discussions/31463), [Commit](https://github.com/open-webui/open-webui/commit/9fef07de3ae8c16b8f53e46b456c144bd739a8a2)
- 🎚️ **Slider for number Valves.** Plugin authors can now show a number Valve or UserValve as a slider with a number box beside it, whose ends come from the field's minimum and maximum, so users see the allowed range while picking a value. [#33179](https://github.com/open-webui/open-webui/pull/33179), [#32045](https://github.com/open-webui/open-webui/discussions/32045), [Commit](https://github.com/open-webui/open-webui/commit/9ed317dc90c7a7fda96a6de68491648341d27ca2)
- 📇 **Provider details for models.** Administrators editing a model now see a Provider details section with the input and output types, context window, maximum output and supported parameters that the provider reports for it. [Commit](https://github.com/open-webui/open-webui/commit/18996b03bafa46e80bf91a1798ed1b8e0c86081c)
- 🧲 **Embedding prefixes in settings.** Administrators can now set the query and content prefixes that some embedding models need under Admin Settings > Documents, where they could only be set with the "RAG\_EMBEDDING\_QUERY\_PREFIX" and "RAG\_EMBEDDING\_CONTENT\_PREFIX" environment variables. [Commit](https://github.com/open-webui/open-webui/commit/4a10c093ab1dc9d195c4bcd662c22aec97bba22c)
- ⏱️ **Terminal start timeout.** Open WebUI now waits up to 60 seconds by default when it asks a terminal for its skills, AGENTS.md file or uploads, so a terminal that is still starting can answer, with "AIOHTTP\_CLIENT\_TIMEOUT\_TERMINAL" to change the limit and a message naming the terminal when it still times out. [Commit](https://github.com/open-webui/open-webui/commit/ab133dba2183491d7c22229ae2b3b30cacf020d4)
- 🚨 **Automation failure notifications.** Automation run failed is now an event users can pick for their notification targets under Settings > Notifications, so the owner hears about every failed run with the automation's name and error. [#33331](https://github.com/open-webui/open-webui/pull/33331), [#33228](https://github.com/open-webui/open-webui/issues/33228), [Commit](https://github.com/open-webui/open-webui/commit/e49ff5df64a1523b80fce8ef03637953265c4355)
- ⚡ **Faster knowledge base commands.** Knowledge base commands such as ls, cat and grep and the knowledge base sync check now list files without loading every file's full text, so on large knowledge bases each call is up to ten times faster and uses far less memory. [#33332](https://github.com/open-webui/open-webui/pull/33332), [#33322](https://github.com/open-webui/open-webui/issues/33322), [Commit](https://github.com/open-webui/open-webui/commit/517f824eb42615b203eb5c1f8779c268aa829960)
- 🔭 **Faster chat search.** Searching your chats, including from the Reference Chats menu and the model's chat search tool, no longer loads every matching chat in full, so results come back faster on large chat histories, and a result's message preview in the Reference Chats menu now loads when you hover it. [Commit](https://github.com/open-webui/open-webui/commit/44a9d499db851f7c6243ada8bfddb9d5b419f473)
- 📦 **Batched document embedding.** Large documents are now embedded and saved in batches of 1000 chunks by default, set with "RAG\_EMBEDDING\_BUFFER\_SIZE", so processing a very large file holds far less in memory at once. [Commit](https://github.com/open-webui/open-webui/commit/58536b65038dc7ff17d02dd78c60cc71ce110f92)
- 🧾 **Mistral OCR model choice.** Administrators can now pick the Mistral OCR model and send extra request options through a Parameters field in Admin Settings > Documents or "MISTRAL\_OCR\_PARAMS", for example to stay on an older OCR model or to match what an Azure AI Foundry endpoint expects. [#33333](https://github.com/open-webui/open-webui/pull/33333), [#19707](https://github.com/open-webui/open-webui/issues/19707), [Commit](https://github.com/open-webui/open-webui/commit/f1f0a194aef3d029f8243f7e7ac553d492283c07)
- 📉 **Negative relevance threshold.** The Relevance Threshold in Admin Settings > Documents now takes negative values for rerankers that return raw scores below zero, where the field refused them and a negative "RAG\_RELEVANCE\_THRESHOLD" kept the page from saving while hybrid search was on. [#33330](https://github.com/open-webui/open-webui/pull/33330), [#29888](https://github.com/open-webui/open-webui/issues/29888), [Commit](https://github.com/open-webui/open-webui/commit/34ef99dbfb0815fbca10d3faea2da7c50f29e19f)
- 🎞️ **Animated ComfyUI images.** Images from ComfyUI's Save Animated WEBP and Save Animated PNG nodes now show up in the chat as the animated file, for both image generation and image editing. [#33325](https://github.com/open-webui/open-webui/pull/33325), [#33013](https://github.com/open-webui/open-webui/issues/33013), [Commit](https://github.com/open-webui/open-webui/commit/cfe745b00c272679db7a6082749f6f7a6c5f7e36)
- 📡 **Metrics skip health checks.** OpenTelemetry metrics now leave out requests whose URL matches "OTEL\_PYTHON\_FASTAPI\_EXCLUDED\_URLS" or "OTEL\_PYTHON\_EXCLUDED\_URLS", so health checks and probes no longer fill the request metrics, the same way traces already skip them. [#33329](https://github.com/open-webui/open-webui/pull/33329), [#31609](https://github.com/open-webui/open-webui/issues/31609), [Commit](https://github.com/open-webui/open-webui/commit/76b7be67fce6375244e4b00f0fdda5fb896e056e)
- 🗝️ **Admins manage user API keys.** Administrators can now rotate or delete a user's API key in the Edit User dialog, and a rotated key is shown once so it can be copied. [#32774](https://github.com/open-webui/open-webui/issues/32774), [Commit](https://github.com/open-webui/open-webui/commit/360d81dfe8f68f8fe7e26702cfcdc8921941da1a), [Commit](https://github.com/open-webui/open-webui/commit/fdaa240d441de02a687f3ea069409f5ff7851a74)
- 👓 **More hideable chat controls.** Administrators can now also hide the selected tools, skills, filters, web search, image generation and code interpreter shown in the chat input, through Visible controls in Admin Settings > Interface or "UI\_VISIBILITY". [#32408](https://github.com/open-webui/open-webui/issues/32408), [Commit](https://github.com/open-webui/open-webui/commit/839759cb179e9924149648a896cd9bab15037d6e)
- ♿ **Improved UI accessibility.** Screen reader and keyboard users can now move through a chat message by message with each message's name as a heading, move through menus and submenus with the arrow keys, Home and End, reach a note's Generate title button and the options of a filter list opened with the mouse, leave the Compare revision editors with Escape and Tab, and hear names for every field of the calendar event window, the last column of the Users and Feedback tables and each day in the Settings > Usage heatmap, while the mo...

[Read more](https://github.com/open-webui/open-webui/releases/tag/v0.12.5)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍35donatas-xyz, SollWar, oteissonniere, gromflomite, D-Kuzin, Jxstin1337, vanich79, jdickman1, nahoj, YosypC, and 25 more reacted with thumbs up emoji🎉8Classic298, blueinkgz, AshleyMedway, silentoplayz, evanjs, martijnn, i-iooi-i, and ivanbaldo reacted with hooray emoji❤️8Classic298, kulbhushanchand, silentoplayz, dupoint, DillonKyleDev, lucakottmann, i-iooi-i, and ivanbaldo reacted with heart emoji🚀6Classic298, DesertGun, silentoplayz, Ashutoshdev-hub, i-iooi-i, and ivanbaldo reacted with rocket emoji👀3Classic298, silentoplayz, and ivanbaldo reacted with eyes emoji

All reactions

- 👍35 reactions
- 🎉8 reactions
- ❤️8 reactions
- 🚀6 reactions
- 👀3 reactions

43 people reacted

## v0.12.4

[v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

Oct 25
25 Oct 08:07


[v0.12.4](https://github.com/open-webui/open-webui/tree/v0.12.4)

[`33c1978`](https://github.com/open-webui/open-webui/commit/33c1978d5bad52a31df75ea55143025dfad18d16)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Oct 25, 2026, 04:00 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- 🎯 **Load selected skills on demand.** Administrators can turn on "Load selected skills on demand" under Admin Settings > General or set "ENABLE\_SKILL\_LAZY\_LOADING", so skills selected in the chat or attached to a model are only listed for the model to load when it needs them instead of sending their full instructions with every message, while skills mentioned in the message still load right away, and it is off by default and needs the built-in Skills tool. [Commit](https://github.com/open-webui/open-webui/commit/079fb19e75f8be4b44fada0c755cf383b21a625b)
- 📍 **Compaction shown in chats.** A "Context compacted" line now marks the message where older messages were summarized, opens to show the summary and also appears inside a reply when compaction ran between its tool calls, Chat Controls > Overview tags that message, and compaction progress and errors now show in the chat instead of as pop-up notices. [Commit](https://github.com/open-webui/open-webui/commit/f465a4be11c0c64969da70f1f5b770bd21088b8a), [Commit](https://github.com/open-webui/open-webui/commit/c8786f426ad263ea4113652ed576d3c15ee341d6), [Commit](https://github.com/open-webui/open-webui/commit/3311f999928964ca1f7870fefb407553197dc2d5), [Commit](https://github.com/open-webui/open-webui/commit/3855acf02d44b78e7969599155896865fd362123), [#31324](https://github.com/open-webui/open-webui/issues/31324)
- 🗜️ **Compaction in more chats.** Context compaction now also runs in temporary chats and in short chats that are already over the threshold, such as one question with a reply full of tool output, so the follow-up and any regenerate or edit of it no longer fail with a context length error. [#32794](https://github.com/open-webui/open-webui/pull/32794), [Commit](https://github.com/open-webui/open-webui/commit/56eca192ab7d98dd9d1a9811e4452dc32145848d), [#32781](https://github.com/open-webui/open-webui/issues/32781), [Commit](https://github.com/open-webui/open-webui/commit/d5cd7f4907f9a6832dc5b52520a1381ef50a663c), [#32600](https://github.com/open-webui/open-webui/issues/32600)
- 🕶️ **Hide controls for users.** Administrators can now hide single controls from users under Visible controls in Admin Settings > Interface or with "UI\_VISIBILITY", such as model capabilities, default features and built-in tools in the model editor, Capture, Compare text, Attach Webpage, Attach Files, Attach Notes, Attach Knowledge and Reference Chats in the + menu, the /status, /model and /settings commands, the usage info, Fork, Merge Responses, Preview, Artifacts, Archive and Tags in chats, Set as default and Keep in Sidebar for models and settings such as the Usage tab and the speech engines, while hidden controls keep their values and the features behind them stay usable, hiding Archive also hides Unarchive, and administrators still see every control. [Commit](https://github.com/open-webui/open-webui/commit/08bfaa4be67f6f87878b2209d568a648818506a7), [#32830](https://github.com/open-webui/open-webui/issues/32830)
- 🫙 **Unavailable options hidden.** Options that cannot take effect are now hidden, such as Capture in the + menu without a Vision model, Attach Notes for users without the Notes permission, the Valves pickers in Chat Controls for disabled tools and functions, the Context Compaction Threshold while context compaction is off, the title, follow-up and tag generation switches in Settings > Interface while the admin has turned them off, Compress Images in Channels for users who cannot use channels, the Web Search in Chat setting while web search is not available to the user, the Voice section of Settings > Interface for users who cannot make calls, group and default permission toggles for features the admin has turned off, the Terminal capability and default terminal in the model editor while no terminal server or direct integration is available, the New Temporary Chat and Delete Chat shortcuts for users who may not use them, the Web Search, Image Generation, Code Interpreter and Memory capabilities and Default Features in the model editor while that feature is off for the instance, built-in tools in the model editor that the model's capabilities rule out or whose feature is off, the engine settings in Admin Settings > Web Search and Admin Settings > Images while web search or image generation is off, the Web Search Query Generation switch in Admin Settings > Interface while web search is off, the Regenerate Menu and terminal settings in Settings > Interface while they cannot apply, "/skills:create" for models that cannot create skills, the Call button while speech-to-text is unavailable, the Audio settings tab for users allowed no speech or calls, the multi-factor authentication section while MFA does not apply to the user and the openwebui.com author link on a new chat while community sharing is off, while saved values are kept for when they apply again. [#32969](https://github.com/open-webui/open-webui/pull/32969), [#32967](https://github.com/open-webui/open-webui/pull/32967), [#32959](https://github.com/open-webui/open-webui/pull/32959), [Commit](https://github.com/open-webui/open-webui/commit/9e5a355fd2b318cf68726c69dbf37dae5e8413b0), [Commit](https://github.com/open-webui/open-webui/commit/9faca2ac5bd69c536e4a87563af39a195d6ea32e), [Commit](https://github.com/open-webui/open-webui/commit/4324573f16b5ce888c9baf235188d7bcfe4b5f51), [#32962](https://github.com/open-webui/open-webui/pull/32962), [#32973](https://github.com/open-webui/open-webui/pull/32973), [#32976](https://github.com/open-webui/open-webui/pull/32976), [#32977](https://github.com/open-webui/open-webui/pull/32977), [#32980](https://github.com/open-webui/open-webui/pull/32980), [#32961](https://github.com/open-webui/open-webui/pull/32961), [Commit](https://github.com/open-webui/open-webui/commit/1f737b894827d19b1b1b4e9dfd5eea23992a3a96), [Commit](https://github.com/open-webui/open-webui/commit/be8f2c0a21d7eb3c873c085f90273dc5e6e39b3d), [Commit](https://github.com/open-webui/open-webui/commit/fbad6fb252f6eb7ccce86944b3bb83623f2d5598), [Commit](https://github.com/open-webui/open-webui/commit/11406c1654794d153f120899f12728cf84490488), [Commit](https://github.com/open-webui/open-webui/commit/35ee76cebb523c21703b31a2cf4347e984490a95), [Commit](https://github.com/open-webui/open-webui/commit/502af86b254b3d071e6b906223493f486cc73c51), [#32972](https://github.com/open-webui/open-webui/pull/32972), [Commit](https://github.com/open-webui/open-webui/commit/521da58ff3bcbb3205e695286ff8f71a64d23606), [#32975](https://github.com/open-webui/open-webui/pull/32975), [Commit](https://github.com/open-webui/open-webui/commit/d48b5e1c878140ce04b5cf5c30d15a472cbd9346), [#32983](https://github.com/open-webui/open-webui/pull/32983), [Commit](https://github.com/open-webui/open-webui/commit/8852d460b7009f776a131e88cbf0cbad595a16d8), [#32966](https://github.com/open-webui/open-webui/pull/32966), [Commit](https://github.com/open-webui/open-webui/commit/5e62c8997f9d14ebc321022a552380f4dc932526), [#32978](https://github.com/open-webui/open-webui/pull/32978), [Commit](https://github.com/open-webui/open-webui/commit/159a29ed06c4e689c465c105c74cf0d9ff4904b9), [#32963](https://github.com/open-webui/open-webui/pull/32963), [Commit](https://github.com/open-webui/open-webui/commit/98f23b17a5755216e31c09ee938e36e46d139fee), [#32965](https://github.com/open-webui/open-webui/pull/32965), [Commit](https://github.com/open-webui/open-webui/commit/758e4f6cc3bc504c8e100e535694dbc93214ad31), [#32984](https://github.com/open-webui/open-webui/pull/32984), [Commit](https://github.com/open-webui/open-webui/commit/e11c1bb38c3695917038b0d79933b35886b0e70e), [#32985](https://github.com/open-webui/open-webui/pull/32985), [Commit](https://github.com/open-webui/open-webui/commit/1d6d805587c06847d9518ccab79fe780aba8d1a6), [#32986](https://github.com/open-webui/open-webui/pull/32986), [Commit](https://github.com/open-webui/open-webui/commit/d2e88ba37abf6d83d9fcffec8574e155b352f4ca), [#32974](https://github.com/open-webui/open-webui/pull/32974), [Commit](https://github.com/open-webui/open-webui/commit/c4aac6152b59e17610bbb5aa9bab1e230460c3ed), [#32981](https://github.com/open-webui/open-webui/pull/32981), [Commit](https://github.com/open-webui/open-webui/commit/11081b1567dd4b5b41907b8733c21239079a94ca), [#32971](https://github.com/open-webui/open-webui/pull/32971), [Commit](https://github.com/open-webui/open-webui/commit/f36ed913719814419d5a621b528ec1b56595809c), [#32970](https://github.com/open-webui/open-webui/pull/32970), [Commit](https://github.com/open-webui/open-webui/commit/b02ff544597755624953ecc15290bee19348ca54), [#32964](https://github.com/open-webui/open-webui/pull/32964), [Commit](https://github.com/open-webui/open-webui/commit/2cf014c7e9be601116d8e93da0d7367f77d6f14e), [#32830](https://github.com/open-webui/open-webui/issues/32830)
- 🔏 **Access button respects sharing.** The Access button and menu entry of models, prompts, tools, knowledge, skills and notes and the Access button in folder settings are now hidden from users without the matching sharing permission, who had nothing they could change in its dialog. [#32979](https://github.com/open-webui/open-webui/pull/32979), [Commit](https://github.com/open-webui/open-webui/commit/ac12b04aada033117f9f7e8ee4fb9562c7d5a417), [#32830](https://github.com/open-webui/open-webui/issues/32830)
- 🖇️ **Attach entries without uploads.** When files cannot be attached, because of a missing permission or a selected model without File Upload, the greyed Attach Knowledge, Reference Chats and Attach Notes entries in the + menu no longer open and the # and @ lists leave out what cannot be attached, including pasted links for users without the web upload permission, so a picked item no longer vanishes from the input without a message. [#32968](https://github.com/open-webui/open-webui/pull/32968), [Commit](https://github.com/open-webui/open-webui/commit/75c4421b3ab94b1a39d74674475294571bd20bcd), \[ [#32830](https://github.com/open-webui/open-webui/issues/32830)\](http...

[Read more](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍35Classic298, silentoplayz, gromflomite, tjbck, MTS2Code, iChristGit, plevart, oteissonniere, Kylapaallikko, Gessler377, and 25 more reacted with thumbs up emoji🎉16Classic298, silentoplayz, tjbck, blueinkgz, iChristGit, plevart, DesertGun, xjulian3x, JonPC4, meshaabi, and 6 more reacted with hooray emoji❤️13Classic298, silentoplayz, tjbck, iChristGit, plevart, gaby, xjulian3x, JonPC4, meshaabi, i-iooi-i, and 3 more reacted with heart emoji🚀13Classic298, silentoplayz, tjbck, iChristGit, plevart, ArminShoeibi, tariktalay, JonPC4, meshaabi, i-iooi-i, and 3 more reacted with rocket emoji👀8Classic298, silentoplayz, tjbck, iChristGit, meshaabi, theedgeofc-a11y, DillonKyleDev, and ivanbaldo reacted with eyes emoji

All reactions

- 👍35 reactions
- 🎉16 reactions
- ❤️13 reactions
- 🚀13 reactions
- 👀8 reactions

41 people reacted

## v0.12.3

[v0.12.3](https://github.com/open-webui/open-webui/releases/tag/v0.12.3)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

Oct 16
16 Oct 11:46


[v0.12.3](https://github.com/open-webui/open-webui/tree/v0.12.3)

[`91ea4e3`](https://github.com/open-webui/open-webui/commit/91ea4e3421d1d8069f13d4a463fcb5986d94ea60)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Oct 16, 2026, 07:46 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- 🔐 **End-to-end encrypted chats.** Direct messages and private group channels can now hold a temporary end-to-end encrypted chat: a member picks Encrypted Chat in the channel menu, the other members see "Encrypted chat in progress" with a Join link, messages of up to 16 KiB are encrypted in the browser with MLS and only passed through the server without being saved, participants can verify each other by comparing codes and see when others are typing, and the chat is cleared when you leave or reload and ends when channel membership or access changes. Administrators turn it on under Admin Settings > General > Encrypted channels or with "ENABLE\_ENCRYPTED\_CHANNELS" and grant it with the new Encrypted Channels permission, off by default or set with "USER\_PERMISSIONS\_FEATURES\_ENCRYPTED\_CHANNELS", and it needs websocket connections with websocket server logging off and HTTPS in production. [Commit](https://github.com/open-webui/open-webui/commit/7dc91de86c41866f4170602f074c39dbf1609377), [Commit](https://github.com/open-webui/open-webui/commit/0b3812f2857b4c65fd1ab931f40de4f1264edc46), [Commit](https://github.com/open-webui/open-webui/commit/b1e876896caee5bf30a010fb414a9249ec7f59a2), [Commit](https://github.com/open-webui/open-webui/commit/4dedaaf6e2292c2c4fb48668eee1292cfd7de2d0)
- 📡 **Much lighter streaming with Redis.** With Redis, a streaming reply is now stored under its own key and new text is appended to it instead of rewriting the whole reply into a shared hash on every update, and replies started on older instances are still read during an upgrade; with room channels on, each instance now only subscribes to the rooms of people connected to it, so Redis no longer sends it live updates for chats it does not serve. [Commit](https://github.com/open-webui/open-webui/commit/f5a26f53a089eeb9683ead687a1fd3e9125132a6) [Commit](https://github.com/open-webui/open-webui/commit/362b01d0b2ba677858a5af85caf3dd8544c5e6df) [#32478](https://github.com/open-webui/open-webui/issues/32478)
- 🔍 **Compare view options and undo.** The Compare revision view has a Comparison options menu to ignore whitespace, ignore emphasis markers or only show changes with the unchanged lines folded away, an Undo button that steps back through your edits in both panes in order, and changed lines that are now lined up by their matching text. [Commit](https://github.com/open-webui/open-webui/commit/d0750f6617acd3b57ce58ba1d543c37e6c793c8d), [Commit](https://github.com/open-webui/open-webui/commit/a087aa1deb4d999b122f882335fd08af8f06e72c), [Commit](https://github.com/open-webui/open-webui/commit/10ce0d23651fc2c96fd0d276147cd48105e21b84), [Commit](https://github.com/open-webui/open-webui/commit/3288fe010a5e8f8a59e1e5d2262957d175e56bde)
- 📝 **Richer Markdown file previews.** Markdown files opened in the terminal file browser now render with the same renderer as chat replies, including math, footnotes, highlighted code blocks, alerts and Mermaid diagrams, as well as HTML blocks mixed with Markdown, laid out as a compact document, and task list checkboxes in an editable file can be ticked to save the change to the file. [Commit](https://github.com/open-webui/open-webui/commit/c9a52208da9e8deeac6f2df7fcacbe519c2acb29) [Commit](https://github.com/open-webui/open-webui/commit/7c3980338b72c5faa7e7f3a088deb477644fef40) [Commit](https://github.com/open-webui/open-webui/commit/15ac5163ea00a934ec0c68d2bb7f6bc5c655223e) [#32514](https://github.com/open-webui/open-webui/issues/32514)
- 👀 **Live collaborators in shared chats.** The top bar of a chat now shows the pictures of the other people who have the same chat open at that moment, up to three and a count for the rest, with a Collaborators list that opens their profile cards. [Commit](https://github.com/open-webui/open-webui/commit/4dedaaf6e2292c2c4fb48668eee1292cfd7de2d0), [Commit](https://github.com/open-webui/open-webui/commit/8191ac30dd79b4a39130fe83ffc16035776be484), [Commit](https://github.com/open-webui/open-webui/commit/8e9519240fcdcd568a9b951ba06e523c58e68350)
- ✏️ **Edit and regenerate in shared chats with replies.** In a chat from a shared folder that allows replies, people who may edit messages can now edit a prompt to start a new branch and regenerate any reply, not only replies to their own messages, and others viewing the chat stay on the branch they had selected. [Commit](https://github.com/open-webui/open-webui/commit/2a6e0da057d3b6eb6ba506346c4db788cab735f0), [Commit](https://github.com/open-webui/open-webui/commit/788a61180be76aef27761b051300d6eefa715947)
- 🗄️ **Folder access in the folder editor.** Sharing a folder now happens through an Access button in the Edit Folder dialog instead of a Share item in the folder menu, the sharing mode can be set before anyone is added, and subfolders note that access granted to parent folders also applies to them. [Commit](https://github.com/open-webui/open-webui/commit/f4557ca06b8331c8914bac9e8f54ce63b0445c21), [Commit](https://github.com/open-webui/open-webui/commit/4a70253bc8586ad1d2a97241665b2060324bab37)
- 🔎 **Workspace search.** The search window now searches your chats, chats in folders shared with you, chats shared with you, channel and direct messages and notes in one place, with filters for content type, a folder or channel, and whether something was created by you or shared with you, highlighted matches, a preview of each result with Ctrl/Cmd + Enter, Copy link, and channel results that open the thread scrolled to the matching message. [Commit](https://github.com/open-webui/open-webui/commit/b4db56ae96651d926adb4aefc6ec1275f35c6b6f), [Commit](https://github.com/open-webui/open-webui/commit/ef28e99e587a2845a2852bb6ab8c182dc1588980), [Commit](https://github.com/open-webui/open-webui/commit/1a1a81d8e09330900ac74e4bc97a48e1e0d52a8a)
- 💭 **Comments in document previews.** Word, Excel, PowerPoint and PDF files opened in the terminal file browser now show their comments and replies, marked where they belong in the document and opened by hovering or tapping a marker, and older .xls spreadsheets can now be previewed too. [Commit](https://github.com/open-webui/open-webui/commit/ba0b2169e1799e1915c6dbb071c56d54896467fb)
- 🧹 **Clear Input Selections shortcut.** Clearing the model override, selected tools and filters and the web search, image generation and code interpreter toggles from the chat input is now a shortcut you can change in Settings > Shortcuts, still Escape by default. [Commit](https://github.com/open-webui/open-webui/commit/9cf48f4fb0a8aef30010294912a3a5674850beaf)
- 🙋 **Ask about a file from the file browser.** Selecting text in a file open in the terminal file browser now shows an "Ask or edit…" box that sends your request to the model with the file attached and the selection quoted, so it can answer or edit that file in the same terminal; unsaved edits can be saved before sending, and requests sent while a reply is running wait in the queue. [Commit](https://github.com/open-webui/open-webui/commit/af34515131d9efd41cfeae5c1ea50a7f7ed84443)
- ☁️ **Google Drive access limited to picked files.** The Google Drive picker now asks only for access to the files a user picks instead of read access to their whole Drive, so self-hosted installs no longer need Google's restricted-scope verification and users no longer see the "Google hasn't verified this app" warning. [#32531](https://github.com/open-webui/open-webui/pull/32531) [Commit](https://github.com/open-webui/open-webui/commit/ed5c2d7522c126b6163aad56762790025b31ec0b) [#29537](https://github.com/open-webui/open-webui/issues/29537)
- 📜 **Full text of long status lines.** Status lines above a reply, such as a token usage summary sent by a function, can now be clicked to show their full text, and with several status lines the history shows every entry in full. [#32532](https://github.com/open-webui/open-webui/pull/32532) [Commit](https://github.com/open-webui/open-webui/commit/291b57bec24ec670050b996ede45ea6dd56c7f9f) [#30056](https://github.com/open-webui/open-webui/issues/30056)
- 📏 **Skill read limits.** Administrators can set how many characters of a skill the model reads at once and how long the preview of longer instructions is, under Admin Settings > General with "Skill Read Limit" and "Skill Preview Length" or the "SKILL\_CONTENT\_MAX\_CHARS" and "SKILL\_PREVIEW\_MAX\_CHARS" environment variables, which default to 20000 and 5000. [Commit](https://github.com/open-webui/open-webui/commit/92e64c1d59cdd99b5f33a108186a1d368daab964)
- 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.
- 🌐 **Translation updates.** Translations for Portuguese (Brazil), Chinese (Traditional), Arabic, Bengali, Hebrew, Georgian, Punjabi, Slovak, Serbian, Urdu, Uzbek and Vietnamese were enhanced and expanded. [#32440](https://github.com/open-webui/open-webui/pull/32440), [#32482](https://github.com/open-webui/open-webui/pull/32482), [#32501](https://github.com/open-webui/open-webui/pull/32501)

### Fixed

- 🧾 **API key header requests in the audit log.** Requests authenticated with an API key in the x-api-key header, as Anthropic SDKs send it, or in a header set with "CUSTOM\_API\_KEY\_HEADER" now appear in the audit log under the key's owner, and failed attempts with a wrong key are logged without a user, where these requests were missing from the audit log. [#32443](https://github.com/open-webui/open-webui/pull/32443), [Commit](https://github.com/open-webui/open-webui/commit/f7c8ad012ddcf458c39cdf8a96b41c410655196c)
- 📚 **Knowledge sharing kept on rename.** A collaborator with write access who edits a shared knowledge base's name or description no longer turns off sharing they could not set themselves, such as Public. [#32450](https://github.com/open-webui/open-webui/pull/32450), [Commit](https://github.com/open-webui/open-webui/commit/08f6023427cdad6179b8fc5f656c99f3f0ad44f8), \[ [#32449](https://github.com/open-webui/open-webui/issues/32449)\]( [https://github.com/open-webui/open-webu](https://github.com/open-webui/open-webu)...

[Read more](https://github.com/open-webui/open-webui/releases/tag/v0.12.3)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍19oteissonniere, Classic298, KOCM0C, RomualdYT, hundehausen, zragon, xjulian3x, MissedShot, showmidelo, sunjiale-hue, and 9 more reacted with thumbs up emoji🎉11Classic298, RomualdYT, blueinkgz, xjulian3x, ctg49, andrewSC, nvxcii, rafabiton, smokeev-dev, silentoplayz, and ivanbaldo reacted with hooray emoji❤️16rosimelade, SRusinek, donatas-xyz, tariktalay, T100D, romayojr, GuilhermeDellatin, Classic298, Vrantschesko, xjulian3x, and 6 more reacted with heart emoji🚀7Classic298, andrewSC, rafabiton, smokeev-dev, silentoplayz, erickstryck, and ivanbaldo reacted with rocket emoji👀5rosimelade, Classic298, silentoplayz, adavila3, and ivanbaldo reacted with eyes emoji

All reactions

- 👍19 reactions
- 🎉11 reactions
- ❤️16 reactions
- 🚀7 reactions
- 👀5 reactions

35 people reacted

## v0.12.2

[v0.12.2](https://github.com/open-webui/open-webui/releases/tag/v0.12.2)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

## No results found

[View all tags](https://github.com/open-webui/open-webui/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)[github-actions](https://github.com/apps/github-actions)

released this

Oct 14
14 Oct 21:07


[v0.12.2](https://github.com/open-webui/open-webui/tree/v0.12.2)

[`6a18585`](https://github.com/open-webui/open-webui/commit/6a18585ff4c2e5f6805f682222cfbc46dc669ef8)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.


GPG key ID: B5690EEEBB952194

Verified
on Oct 14, 2026, 05:07 PM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).


### Added

- 📑 **MinerU 4.x servers.** The MinerU document engine now works with self-hosted MinerU 4.x servers, where every document failed with a 404 because 4.x removed the old parsing interface; 3.x servers work as before, 4.x servers take a tier (flash, basic, standard or advanced) and enable\_ocr in the MinerU parameters while language and model\_version stay 3.x only, and images that 4.x returns inside the document text are left out of the indexed content. [#32422](https://github.com/open-webui/open-webui/pull/32422), [Commit](https://github.com/open-webui/open-webui/commit/81f5b8adf80e49bd2213390b59dc867074c3738e), [#31516](https://github.com/open-webui/open-webui/issues/31516)
- 🤝 **Keep both changes when comparing.** The Compare revision view now has a Keep both button that puts the original and the proposed text of the selected change into the proposed revision, original first, so you no longer have to pick one side. [Commit](https://github.com/open-webui/open-webui/commit/97b7ed73c84767611d3a26d594c36f63619d92ea)
- 📚 **Open attached knowledge from its preview.** Clicking the name in the preview of an attached knowledge collection now opens that collection in the workspace, and file and link names are real links that open in a new tab. [Commit](https://github.com/open-webui/open-webui/commit/40bf4a1b99aa0aae316095eff100c07570c542da)
- 🏷️ **Model ID in custom headers.** Custom headers on connections and tool servers can now use {{MODEL\_ID}}, which holds the ID of the model handling the chat request, the workspace model's own ID for a workspace model and each model's own ID in a multi-model chat, so downstream services can route or log usage per model. [#32426](https://github.com/open-webui/open-webui/pull/32426), [Commit](https://github.com/open-webui/open-webui/commit/bae22752d3995f573a373ee1ae4735b746d952a9), [#30006](https://github.com/open-webui/open-webui/issues/30006)
- 🧾 **Requested model in the audit log.** Audit log entries for chat and completion requests, including the OpenAI, Ollama and Anthropic compatible endpoints, now carry a model\_id field with the model the client asked for at every AUDIT\_LOG\_LEVEL, where the model only appeared in the request body and went missing when MAX\_BODY\_LOG\_SIZE cut a long prompt; other requests log it as null. [#32429](https://github.com/open-webui/open-webui/pull/32429), [Commit](https://github.com/open-webui/open-webui/commit/fb3d92a6ef56b5a8a6820f615f6e6294c44eaad7), [#30097](https://github.com/open-webui/open-webui/issues/30097)
- 🔐 **Custom TLS certificate for Milvus.** Open WebUI can now connect to a Milvus server with a self-signed or company-issued TLS certificate by pointing the new "MILVUS\_SERVER\_PEM\_PATH" environment variable at the certificate file, in normal and multi-tenancy mode. [#32427](https://github.com/open-webui/open-webui/pull/32427), [Commit](https://github.com/open-webui/open-webui/commit/3bc82bb2c110fc3ed7064e6107a4731b8d9ab5ae), [#31632](https://github.com/open-webui/open-webui/issues/31632)
- 🧭 **call\_tool for Tool Search.** With Tool Search on, the model now gets a new call\_tool tool and runs a tool it found with search\_tools through it, passing the tool's name and its arguments, instead of calling the deferred tool directly by a name that is not in the request's tool list, which strict providers rejected; approvals and other tool behavior stay the same. [Commit](https://github.com/open-webui/open-webui/commit/7b47c3b22ce983d57f4a13073748a935c4614889), [#32243](https://github.com/open-webui/open-webui/issues/32243)
- 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

### Fixed

- 🔏 **Channel message metadata kept server side.** Channel messages posted or edited through the API no longer take their metadata from the request, so a user can no longer make a message appear to come from a channel webhook or a model. [#32421](https://github.com/open-webui/open-webui/pull/32421), [Commit](https://github.com/open-webui/open-webui/commit/44953df70ed758a6321f7a2e139c93aca29129f1)
- 👮 **SCIM cannot delete admins.** An identity provider can no longer delete administrator accounts, including the first admin, through a SCIM delete request, which now answers with 403 and leaves the account in place, so a sync that prunes unassigned users can no longer leave the instance without an administrator; admins are removed in the admin panel. [#32415](https://github.com/open-webui/open-webui/pull/32415), [Commit](https://github.com/open-webui/open-webui/commit/6276e81cec38f5c5cce067e4be905c5710c2d7d6), [#27662](https://github.com/open-webui/open-webui/issues/27662)
- 🗝️ **Collection names checked as stored.** Retrieval access checks now compare collection names the way vector stores resolve them, ignoring letter case and treating hyphens and underscores alike, so a name written differently can no longer pass the check as something other than the collection that is then read. [#32435](https://github.com/open-webui/open-webui/pull/32435), [Commit](https://github.com/open-webui/open-webui/commit/30f3c49fb02c22269b42fe3b310209926ee7e8f9)
- 📱 **Voice on Android Chrome.** Voice calls and dictation on Android Chrome no longer go silent or hang on Listening after about ten uses until the page is reloaded, since the microphone level display now releases its audio output after each turn. [#32417](https://github.com/open-webui/open-webui/pull/32417), [Commit](https://github.com/open-webui/open-webui/commit/f35b1993271e6f0cf1ffc55375d634a65c9e0ab1), [#29969](https://github.com/open-webui/open-webui/issues/29969)
- 🖥️ **Per chat terminal file actions.** With the Open Terminal chat context set to Per chat, opening HTML files, running notebooks, saving edited files, creating new files, deleting several selected files and downloading a folder or selection as a zip now use the chat's own workspace, where HTML files showed "File not found" and saved files never appeared in the chat. [#32418](https://github.com/open-webui/open-webui/pull/32418), [Commit](https://github.com/open-webui/open-webui/commit/77fd8aea613c42e0d590804c7f9fdcf6f5f4af02), [#29965](https://github.com/open-webui/open-webui/issues/29965)
- 🧮 **Memory reindex rate limits.** Reindexing memories, from the admin Reindex Knowledge and Memory Vectors button, a user resetting their memory vectors or the automatic reindex after an embedding model change, now follows the Embedding Concurrent Requests limit and batch size, where it sent one request per memory at once and rate-limited providers failed most of them with 429 errors. [#32420](https://github.com/open-webui/open-webui/pull/32420), [Commit](https://github.com/open-webui/open-webui/commit/8bddf9bc62c3ffcaa3e6433bc5ac0f1d04a94421), [#32212](https://github.com/open-webui/open-webui/issues/32212)
- ⏰ **Automation run results.** An automation run is now recorded as successful only after its reply finishes, and a reply that fails or is cancelled is recorded as an error that links to the chat, where runs counted as successful as soon as the reply started. [Commit](https://github.com/open-webui/open-webui/commit/de446952c2db1168dca5c6e3da6d961e6f55a8eb)
- 📜 **Long polling kept out of the audit log.** With websocket support turned off, every socket.io long polling request is no longer written to the audit log as its own entry, which flooded it and could not be filtered with AUDIT\_EXCLUDED\_PATHS, so the audit log looks the same with either transport. [#32425](https://github.com/open-webui/open-webui/pull/32425), [Commit](https://github.com/open-webui/open-webui/commit/209b15b9633c63ce1b7cf3c1fdc6e032d67978c6), [#31871](https://github.com/open-webui/open-webui/issues/31871)
- 📎 **Sources of approved tools.** With tool approval set to ask, a knowledge or file tool the user approved now saves and shows its sources below the reply, where they were lost after approval. [#32439](https://github.com/open-webui/open-webui/pull/32439), [Commit](https://github.com/open-webui/open-webui/commit/5fde0485a5adda046d283416a5c4c7a543d7a5fe), [#32436](https://github.com/open-webui/open-webui/issues/32436)
- 🗂️ **Sidebar hover previews.** Moving the pointer from one sidebar folder to the next no longer leaves the first folder's preview open or keeps the next one from opening, and folder and chat previews now also open when the pointer rests on the padding around a name. [#32438](https://github.com/open-webui/open-webui/pull/32438), [Commit](https://github.com/open-webui/open-webui/commit/5e2748a03edd2459d07fcfea168daf740092bf94), [#32437](https://github.com/open-webui/open-webui/issues/32437)

### Changed

- 🔖 **Valkey connections tagged as Open WebUI.** Open WebUI's Valkey vector store connections now report their library name as GlidePySync(open-webui), so operators of a shared Valkey or ElastiCache can tell its traffic apart; this needs valkey-glide-sync 2.5.2 or newer, so installs that use VECTOR\_DB=valkey with an older manually installed version must upgrade it, or startup fails. [#32428](https://github.com/open-webui/open-webui/pull/32428), [Commit](https://github.com/open-webui/open-webui/commit/980225e5823808de7ace86a8ee73a0b880b37023), [#31654](https://github.com/open-webui/open-webui/issues/31654)

Assets2

Loading

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/open-webui/open-webui/releases).

👍26Classic298, oteissonniere, zragon, vinas1, 2428424081cn, donatas-xyz, rosimelade, Harvester62, iki007, arasouli, and 16 more reacted with thumbs up emoji🎉6Classic298, vinas1, 2428424081cn, i-iooi-i, silentoplayz, and ivanbaldo reacted with hooray emoji❤️9Classic298, tariktalay, vinas1, 2428424081cn, iki007, i-iooi-i, vanontom, silentoplayz, and ivanbaldo reacted with heart emoji🚀8Classic298, vinas1, 2428424081cn, rosimelade, iki007, i-iooi-i, silentoplayz, and ivanbaldo reacted with rocket emoji👀6Classic298, vinas1, 2428424081cn, rosimelade, silentoplayz, and ivanbaldo reacted with eyes emoji

All reactions

- 👍26 reactions
- 🎉6 reactions
- ❤️9 reactions
- 🚀8 reactions
- 👀6 reactions

28 people reacted

Previous [1](https://github.com/open-webui/open-webui/releases?page=1) [2](https://github.com/open-webui/open-webui/releases?page=2) [3](https://github.com/open-webui/open-webui/releases?page=3) [4](https://github.com/open-webui/open-webui/releases?page=4) [5](https://github.com/open-webui/open-webui/releases?page=5)… [18](https://github.com/open-webui/open-webui/releases?page=18) [19](https://github.com/open-webui/open-webui/releases?page=19) [Next](https://github.com/open-webui/open-webui/releases?page=2)

Previous [Next](https://github.com/open-webui/open-webui/releases?page=2)

You can’t perform that action at this time.