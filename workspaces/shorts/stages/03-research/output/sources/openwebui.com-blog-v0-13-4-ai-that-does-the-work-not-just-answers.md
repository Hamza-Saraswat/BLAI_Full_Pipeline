# SOURCE CACHE
# fetched via: web_extract
# accessed: 2026-11-25
# note: page text as fetched this session; em dashes (U+2014) replaced with -- per repo convention.

# url: https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers
# title: Open WebUI v0.13.4: Interactive Charts, Videos, and AI Agents - Open WebUI Blog
# tier: tier 2 (official vendor blog, published November 19, 2026)

[![logo](https://openwebui.com/logo.png)](https://openwebui.com/)

Product

Resources

[Community](https://openwebui.com/home) [Customers](https://openwebui.com/customers) [Sign In](https://openwebui.com/auth?type=login)

[All articles](https://openwebui.com/blog)

November 19, 2026 /42 MINUTES READ

![Open WebUI v0.13.4: AI that does the work, not just answers](https://community.s3.openwebui.com/uploads/users/6ddf0023-1d2a-4af3-bbbe-41612061a0d8/2026/11/68220f0b-3de4-480e-a8bd-77b0f7931226.png)

SUMMARY

v0.13.1 to v0.13.4 make Open WebUI a place where work gets done, not only answered. Models draw interactive charts, make videos from a prompt or a picture, use several image models, and search OpenAI-compatible vector stores. Agents such as Claude Code and Codex sit in the model picker and work on documents, spreadsheets, and code on a machine your team shares or one each with Terminals. Share a chat so a teammate carries on from the same point, follow every task on a folder board, and hand an agent a GitHub issue. Tether connects your own laptop, its local models, and its MCP servers, and answers questions about anything on your screen. Chats with tools cost less, large chats and files open much faster, and administrators can set an approval policy in plain words. v0.13.1 includes security fixes and database migrations, and v0.13.4 needs Terminals 0.4.0 and moves personal connections into Tether.

Ask most AI assistants for help and you get text back, and the work is still yours: pasting it into the spreadsheet, fixing the file, doing the next step. Over the last four releases we made Open WebUI the place the work itself gets done.

Ask for a chart of a spreadsheet and you get the chart, with a filter you can click. Attach a picture and ask for a video, and it plays in the chat. Hand a bigger job, such as a report, a folder of invoices, or a bug, to an agent like Claude Code or Codex, and it works on the real files while you watch from your desk or your phone. When it's done, fix a spreadsheet cell or a line of a document right beside the chat and save it. That's how our team does most of its engineering and writing now.

It works for a whole team, too. Sign an agent in once on a machine your team shares, and it's in everyone's model picker with nothing to install. Share a chat, and a teammate carries on where you stopped, with the same files and everything the agent already knows. Your own laptop joins in through Tether, our desktop app, with its files and the models you run on it.

v0.13.1 to v0.13.4 came out in November, so this post covers all four. It's long, because a lot shipped. The short version below is enough to decide whether to upgrade, the sections after it walk through each feature step by step, and the many smaller changes are listed by area in [Small improvements across the app](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers#small-improvements-across-the-app).

## The short version [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#the-short-version)

- **Charts and videos in the chat.** Models draw interactive charts and calculators, make videos from a prompt or a picture, use several image models, and search your OpenAI-compatible vector stores.
- **Agents that do whole jobs.** Claude Code, Codex, Gemini CLI, GitHub Copilot, and nine more sit in the model picker and work on documents, spreadsheets, and code on a computer you connect.
- **Pick up where a teammate stopped.** Share a chat with replies allowed, and your teammate carries on with the same agent and the same files.
- **Your own computer joins in.** Tether answers questions about anything on your screen and brings your laptop's files, local models, and tools to Open WebUI on any device.
- **Every task on one board.** A folder shows its chats as a board with statuses, and the Git panel hands a GitHub issue straight to an agent.
- **One machine for the team, or one each.** Share a machine with the agents signed in, or let people create their own, with your project ready when they start.
- **Faster and cheaper.** Long pastes, big PDFs, and large chats open in a fraction of the time, and chats with tools cost less.

**Update as soon as you can, and go straight to v0.13.4.** v0.13.1 includes security fixes, and we'll publish the advisories once CVE numbers are assigned. It also changes the database schema, so back up first and update every instance at the same time. If you run Terminals, v0.13.4 needs Terminals 0.4.0 or later, and models and tool servers people added in their own settings now come from Tether. Read [Before you upgrade](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers#before-you-upgrade) before you start.

## Charts, videos, and images in the chat [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#charts-videos-and-images-in-the-chat)

### Interactive charts and explainers [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#interactive-charts-and-explainers)

We added a Visualizations tool, so models can draw interactive charts, diagrams, calculators, and explainers right in the chat. Ask for a loan calculator, or a chart of a CSV you attached with a filter, and you get something you can click and change, not a picture of it. A button inside a visualization can suggest a follow-up message, which you confirm before it's sent. Common mistakes in what the model writes are repaired before it runs, so more visualizations draw on the first try.

_With Visualizations on, the model charts a CSV in the chat, the filter narrows it to the partner feed, and a night in the chart becomes the next question_

**Try it.** The Visualizations built-in tool is off by default. In the model editor, turn on **Visualizations** in the **Builtin Tools** section. **Builtin Tools** under **Features** is already on. It works with native function calling. If you've turned off scripts in embedded content in your settings, the visualization says that interactive scripts are disabled. Administrators can change the tool's instructions under **Visualization Prompt** in `Settings > Admin > Interface`, or with `VISUALIZATION_PROMPT_TEMPLATE`.

### Make videos from a prompt or an image [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#make-videos-from-a-prompt-or-an-image)

We added video generation, so models can make videos from a prompt or from an image in the chat, through OpenRouter, which offers models like Veo and Kling, or an OpenAI-compatible video server such as LiteLLM. The video plays in the chat.

**Try it.** Once an administrator has set up video generation, turn on **Video** in the + menu of the message input. If there's more than one video model, choose one from the arrow next to it. Then describe the video, or ask for one from an image already in the chat. Video uses the **Video Generation** built-in tool, so the model needs native function calling and that tool turned on in its **Builtin Tools**, which it is by default.

_Maya attaches an illustration for the billing wiki, picks Veo 3.1 from the arrow next to Video, and plays the 8-second clip it made from the picture_

### More than one image model [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#more-than-one-image-model)

We turned image settings into connections, so image generation can use several models from several servers. When more than one is available to you, choose it from the arrow next to **Image** in the + menu. With OpenAI, the default model is now GPT-IMAGE 2, it works with the stock settings, and when a request fails, you see the provider's own error, such as "Invalid size".

_gpt-image-1.5, picked from the arrow next to Image, draws an illustration, and a follow-up changes its background_

### Mention people [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#mention-people)

With the Chat History built-in tool, a model can look up people by name or email and mention them in its reply. Each mentioned person who can see the chat gets an inbox notification that opens the chat at that reply. Ask the model to let a teammate know about its answer in a chat they can see, and the notification brings them straight to it.

_Maya asks the model to tell Sam the summary is ready, it mentions him, and Sam's notification opens the chat at that reply_

## Agents that do whole jobs [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#agents-that-do-whole-jobs)

Agents like Claude Code and Codex were made for programmers, but they'll work on almost anything that lives in files. Give one a folder of invoices, and it reads them, builds a spreadsheet with a total per customer, and tells you which are overdue. Ask it to turn meeting notes into a report, or to find out why the tests fail and fix them. It keeps going, step by step, until the job is done, and you watch every step.

Until now they ran on one person's laptop, in a terminal window. In v0.13.0 we gave models a computer: a machine running Open Terminal, our self-hosted environment where a model can run commands, edit files, and use a browser and a desktop. Agents now live there too. Sign one in on the machine, and everyone with access picks it from the model picker like any other model. Nobody installs anything or manages their own API key, and nobody has to be at the machine.

We made an agent in the chat behave the way it does in its own terminal. Its messages and tool calls stream in as it works. You can attach files and images, stop a reply, and talk to it in a voice call. Where the agent offers them, choose its reasoning effort and service tier under **Model controls** in the message input. Each conversation uses one agent, so you can't put an agent side by side with other models in the same chat.

How an agent asks before it acts depends on your tool permissions. Out of the box, Tool Permissions is off and everyone has Full access, so an agent's requests are approved as it goes. Questions the agent asks you still wait for your answer. When an administrator turns on Tool Permissions, people can choose **Ask** or **Auto**, and a request that needs approval waits in the conversation with the agent's own options. Your answer is saved with the chat. We cover the policy behind Auto in [Set an approval policy](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers#set-an-approval-policy).

We support 13 agents: Claude Code, Codex, Cursor, Grok, OpenCode, Cline, Gemini CLI, Pi, Hermes, Antigravity, GitHub Copilot, Goose, and Qwen Code. Any other agent that speaks the Agent Client Protocol, such as Factory Droid or Kiro, can be added to Open Terminal with `OPEN_TERMINAL_ACP_AGENTS`, with no change to our code. Our `agents` image of Open Terminal comes with Claude Code and Codex installed. The others go in your own image, installed and signed in as the user Open Terminal runs as. If you want the work to stay on models you host, [OpenCode](https://opencode.ai/docs/providers) can point at any OpenAI-compatible endpoint.

_Maya gives the Engineering group the Workbench machine, then Sam picks Codex from the model picker, with nothing installed, and it fixes the failing tests_

We've made agent chats work much like other chats. You can regenerate a reply, edit an earlier message, or fork the chat, and Codex carries on from that point in its own session. Other agents start a new session from the conversation so far. Either way, changes the agent already made to files stay. Claude Code gets the same with the next Open Terminal release after 0.17.20, and until then it asks you to update. To continue a reply that stopped, send a new message.

An agent chat is titled with the start of your first message. If an administrator has set a task model that isn't an agent, that model writes a title once the agent has replied.

**Try it.** Whoever runs your Open WebUI sets up the machine once. Start the `agents` image with a key of your own:

```
$ docker run -d --name open-terminal --restart unless-stopped -p 8000:8000 -v open-terminal:/home/user -e OPEN_TERMINAL_API_KEY=your-secret-key ghcr.io/open-webui/open-terminal:agents
```

1. Sign the agent in. Run `docker exec -it open-terminal bash`, then `claude` and follow the prompts, or `codex login --device-auth`. Codex device login has to be allowed in your ChatGPT account or workspace. To use API keys instead, set `ANTHROPIC_API_KEY` for Claude Code, or run `printenv OPENAI_API_KEY | codex login --with-api-key`.
2. In `Settings > Admin > Integrations`, click **+** in the Open Terminal section and enter the machine's address and your key. That's `http://localhost:8000` on the same host, or `http://host.docker.internal:8000` when Open WebUI itself runs in Docker. **Verify Connection** confirms it.
3. Under **Access**, choose the groups that can use it. Until you do, only administrators can.
4. Save, and turn on the switch next to the connection.
5. To have agents ask before they act, turn on **Tool Permissions** in the **Tools** section of `Settings > Admin > Interface`, or set `ENABLE_TOOL_PERMISSIONS`.

Then anyone in those groups can use it:

1. Select the machine in the terminal menu of the message input, and choose the repository in the working directory menu beside it. The menu keeps a **Recently Used** list of folders for each person.
2. Choose the agent in the model picker. Agent chats have to be saved, so leave Temporary Chat off.
3. Give it a job you can check, such as:

> Read the invoices in this folder, put them in one spreadsheet with a total per customer, and tell me which ones are overdue.

> Find out why the failing test fails, fix it, and run the tests again. Explain what you changed.

If no agents appear, the agent isn't installed or signed in on that machine, or Open Terminal is too old. Agents need Open Terminal 0.17 or later, and Hermes, Antigravity, GitHub Copilot, Goose, and Qwen Code need 0.17.19. Without Docker, `uvx open-terminal@latest` starts the latest Open Terminal on any machine with `uv`.

Each chat remembers its machine and folder, so reopening it, on any device, puts you back where you were. You can switch the terminal or folder in the middle of a chat, too. In an agent chat, a new machine or a new agent starts a fresh session from the conversation, while switching to another model of the same agent keeps the session. If a machine goes away, its agent chats fall back to your default model, and earlier replies keep the agent's name.

To give a project a starting point, open a folder's menu in the sidebar, choose **Edit**, and open **Advanced**. Set its **Default terminal**, which opens the same menu as the message input, its **Working directory**, which you can pick with **Browse directories**, and its **Default Model**, which can be an agent. **System Prompt** and **Knowledge** live there too. Every new chat in that folder starts on that machine, in that folder, with that agent.

_Maya sets a default machine, working directory and Codex on the date-parser folder, and a new chat in the folder starts with all three_

### For bigger jobs [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#for-bigger-jobs)

We added a `cuda` image of Open Terminal with the CUDA development tools and GPU-enabled PyTorch, so an agent can compile GPU code or train a model on an NVIDIA GPU. It needs the NVIDIA Container Toolkit and `--gpus all` in the `docker run` command. The standard, `agents`, and `cuda` images now include GitHub's `gh` and Python's `uv`.

**System info** in the terminal menu shows a machine's CPU, memory, disk, network, uptime, and the programs using the most resources, using the container's limits when it has them.

_System info for the Workbench machine during a training job, with CPU, memory, disk, the network list, and the busiest processes_

## Pick up where a teammate stopped [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#pick-up-where-a-teammate-stopped)

Say you've had Claude Code working on a bug and you need to leave. Share the chat and allow replies. Your teammate opens it and sees the whole session: every message, every command the agent ran and what came back, and every approval. When they send a message, the agent continues its own session on your machine and in your files, with everything it already knows.

Work stops being stuck with whoever started it. Someone reviewing the change can also ask the agent why it did something, in the same conversation, and get an answer from the session that did the work. While they're in the chat, their picture shows in the tab bar.

We save each person's own view: open tabs and layout are kept per person, even in the same chat.

_Maya shares her Codex chat with replies allowed, and Sam reads every step the agent took and has it finish the job on the same files_

**Try it.**

1. In the agent chat, open the chat menu and choose **Share**.
2. Click **Add Access** and choose the people or group who can open it. Then set **Sharing mode**, which appears once someone has access, to **Allow replies**. The dialog tells you that people who can reply can also use the chat's own terminal.
3. Copy the link and send it to your teammate.
4. Your teammate opens the link, reads what the agent did, and replies to it.

Your teammate can change the chat's model, terminal, or folder, and the change is saved for both of you. Moving to another machine or another agent starts a new session from the conversation so far, using your teammate's own access. To keep the agent's place, stay on the same machine and agent. If your teammate forks your chat instead, the fork stays in your shared folder when they can edit it.

The same works for a whole project. Share a folder from its menu in the sidebar, and everyone with edit access can set the status and tags of every chat in it on the folder board, which we cover below.

## Give everyone a machine of their own [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#give-everyone-a-machine-of-their-own)

A shared machine is the simplest start, but everyone works in the same files. Terminals is our server that creates Open Terminal machines on demand, in Docker or Kubernetes. With Terminals 0.4.0, people create their own machines from the chat, without asking an administrator each time. One machine can serve everyone, or each person, chat, or model gets its own. A setup script runs when each one starts, so every new chat can open on a fresh machine with your repository cloned and its dependencies installed.

We'd start with one shared machine for one team. Move to Terminals when people begin to step on each other's files, or when you want each piece of work in its own clean copy.

_Sam and Priya both use the Checkout service terminal: Sam's agent fixes the rounding on his machine, and Priya's own copy still has the two failures_

**Try it.**

1. Open the terminal menu in the message input and click **+** next to **Terminals**. The menu shows even before you have any terminals, as long as you can create one. If there's no **+**, ask whoever runs your Open WebUI for Write access to the Terminals connection.
2. Give it a **Name**. To give each person, chat, or model its own machine, turn on **Separate instances** and choose **User**, **Chat**, or **Model**. It starts on **User**.
3. Open **Advanced**. For agents, choose the `agents` image under **Image**, which suggests the images your server allows. Set **Start directory** to `~/app` and add a **Setup script**:

Bash

Collapse
Copy

```
test -d .git || git clone https://github.com/your-org/your-app .
npm install
```

4. Under **Environment variables**, add what the machine needs, such as `ANTHROPIC_API_KEY` for Claude Code or `GITHUB_TOKEN` for a private repository. For Codex, set `OPENAI_API_KEY` here and add `printenv OPENAI_API_KEY | codex login --with-api-key` to the setup script.
5. Click **Create**.

The terminal is selected for your chat and starts the first time you use it. The first start takes longer while the image downloads. **CPU**, **Memory**, **Storage**, and **Network** in **Advanced** start at the server's defaults and show the most you can ask for. If you can write to more than one Terminals server, a **Server** picker chooses where it runs.

The setup script runs each time the machine starts, as the machine's user, in the start directory, before the machine takes requests. Only the home folder is kept between starts, so put the repository and anything you install there. If the script fails, the machine still starts, and **System info** shows the end of its output. Sub-agents in a per-chat terminal work in their parent chat's machine and files.

### Manage your terminals [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#manage-your-terminals)

Hover a terminal in the terminal menu and click **…** for **Restart**, **Stop** or **Start**, **System info**, **View files**, and **Terminal settings**. Stopping asks first and keeps the files, and the machine starts again the next time someone uses it. **View files** opens the machine's files in a window, without selecting it for your chat.

A terminal is private until you click **Private** in its settings and share it with people or groups. It can't be shared with everyone. Anyone you share it with can run commands and see every file on it, including its environment variables, so use keys meant for that group. The settings list every instance, with who it belongs to, and each one has **Start**, **Stop**, **Restart**, **View files**, **System info**, and **Delete instance**, with a spinner while the action runs. **Delete terminal** removes it with all its instances and their files. Once a terminal has instances, **Separate instances** is locked until you delete them.

If a terminal is deleted or your access is removed while a chat is open, the terminal menu says **Unavailable terminal** instead of quietly switching.

_A terminal's settings list every machine and whose it is, System info shows what one is using, and Restart keeps its files_

### Set up Terminals [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#set-up-terminals)

Running Terminals takes a few minutes for whoever runs your Open WebUI. On a Docker host:

Bash

Collapse
Copy

```
mkdir -p data
export API_KEY="$(openssl rand -hex 32)"
docker network create terminals
docker run -d --name terminals --network terminals -p 127.0.0.1:3000:3000 -e TERMINALS_API_KEY="$API_KEY" -e TERMINALS_DOCKER_NETWORK=terminals -e TERMINALS_DOCKER_HOST_DATA_DIR="$(pwd)/data/terminals" -v /var/run/docker.sock:/var/run/docker.sock -v "$(pwd)/data:/app/data" ghcr.io/open-webui/terminals:latest
```

If Open WebUI runs in Docker, connect it to the same network with `docker network connect terminals open-webui`. Then add a connection in the Open Terminal section of `Settings > Admin > Integrations` with `http://terminals:3000` and the key, and click **Verify Connection**. Administrators also reach these settings from the gear next to **Terminals** in the terminal menu.

Under **Access**, give **Write** to the groups that may create terminals. Write lets them manage every terminal on that connection, not only their own, and open the files and system info of anyone's running instance as that person. Give it to people you'd trust with that.

_An administrator adds the Terminals connection in Integrations, verifies it, and gives the team access_

- To control what machines can reach, define network profiles with `TERMINALS_NETWORK_PROFILES` on the Terminals server, and people pick one under **Network**. Profiles select networks you've already created. They don't create firewall rules.
- Terminals now pulls a newer `:latest` image before it starts a machine, so hosts don't stay on an old Open Terminal.
- Automations use the same choices. A per-user terminal runs as the automation's owner, and a per-chat terminal gets a new machine for each run's chat, so automations on agents or per-chat terminals have to post to a chat, not a channel.
- Terminals has its own admin page, with templates and environments to restart, reset, or delete, and you can delete a person's saved files across all their terminals.
- Kubernetes deployments are supported, in two modes, as the [README](https://github.com/open-webui/terminals) describes.

Terminals is free for personal, non-commercial use. Using it in an organization requires an Open WebUI Enterprise License with Terminals access. If you used Terminals 0.3, there's a manual move to 0.4.0, covered in [Before you upgrade](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers#before-you-upgrade).

## Start from a GitHub issue [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#start-from-a-github-issue)

With the GitHub CLI signed in on the machine, the Git panel covers the whole loop. Next to **Changes** and **History**, it has **Issues** and **Pull requests** for your repository, each with its count of open items. Open an issue and click **Work on this**, and the issue, its comments, and a request to create a branch, make the change, and summarize it are added to the message input, below anything you'd already typed.

On a pull request, **Fix** hands a failing check to the agent, **Address feedback** hands over the review comments and failing checks, and **Resolve conflicts in chat** asks it to merge the base branch in and resolve the conflicts. A single review comment has **Add to chat**. You can change any of these requests before you send it.

We built these so the request is written for you, with the context the agent needs, and you still read it before it goes. Pick whichever agent suits the job before you send it.

_Codex takes issue #23 from the Git panel and makes a branch and the fix, with every command and diff in its steps, then takes the review feedback on pull request #24_

**Try it.** The standard, `agents`, and `cuda` images of Open Terminal include the GitHub CLI. Run `gh auth login` once in the machine's terminal, select the machine with your repository as the working folder, and open **Files**. The Git panel is part of the Files tab. Issues need Open Terminal 0.17.8 or later, and the **Issues** tab only shows when the repository has issues turned on.

### Issues and pull requests, without leaving the chat [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#issues-and-pull-requests-without-leaving-the-chat)

The panel is a full GitHub workbench.

- **Pull requests.** Click **New pull request** to open one with a **Title**, **Description**, base and head branches, and **Draft**. Each pull request shows its checks, with each check's name linking to its run on GitHub, its review state, labels, activity, and conflicts. **Approve** and **Request changes** sit next to **Leave a comment**. The **Pull request actions** menu has **Checkout**, **Edit**, **Update branch**, **Mark ready**, **Close pull request**, **Reopen**, **Copy link**, **Copy branch name**, and **Open in GitHub**. Choose a merge method when you merge.
- **Issues.** Create, edit, and comment on issues. Close them with **Close as completed** or **Close as not planned**, or with **Close with comment**, and reopen them the same way.
- **Lists.** Rows show a colored dot for check status, with "Checks: 2 failing, 1 pending, 5 passing" on hover, plus conflicts, approvals, and when they were last updated. Filter pull requests by status, including **Merged**. With Open Terminal 0.17.8 or later, search reaches every issue and pull request in the repository, not only the ones loaded. Descriptions and comments render as Markdown, and the lists resize like the file list.
- **Changes.** Ctrl or Shift click files to discard several at once, or use **Discard all changes** from the **…** menu. Discard also removes staged and new files, and it asks first, because files that aren't in the last commit can't be recovered. The panel tells you what it's doing while it stages, pushes, or fetches.

_Maya publishes her branch and opens a draft pull request, Codex fixes the failing check from its log, the checks pass, and she approves Priya's pull request from the panel_

### See what the agent did [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#see-what-the-agent-did)

While the agent works, we show its steps as what it did: the command and its output, with the exit code when it failed; a diff of each file it edited, with the lines added and removed; or the files it read, the code it searched, and the pages it fetched. A run of steps is summed up as, for example, "Ran 2 commands, Edited 1 file". Other models that use the terminal tools get the same view, with numbered diffs from Open Terminal 0.17.20.

To look properly at what the agent changed, click **Split screen** and put the chat beside a file. The editor marks the lines changed since the last commit, and the file browser marks each file with its Git status, such as M for modified or A for added. Folders show when something inside them changed.

It isn't only code. If a model builds you a spreadsheet and one number is wrong, click the cell, fix it, and save, and the `.xlsx` file is updated in place, with no download and re-upload. The spreadsheet editor has a formula bar, takes pastes from other spreadsheets, and has resizable columns. Formula cells, protected sheets, and signed workbooks stay read-only. Markdown opens in a rich text editor and saves back as Markdown, with pasted images uploaded next to it.

_The changed lines in a file beside the chat, then a spreadsheet cell fixed and saved back to the file_

## Follow every task on a board [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#follow-every-task-on-a-board)

Once several agents are working, you need to know which ones are done and which are waiting on you. Click a folder's name in the sidebar to open its page, with its description under the name. Under **Display options**, set **Layout** to **Board**, and choose **Columns** by **Status**, **Tags**, or **Activity**. You can add **Rows** by another of them, and **Ordering** sorts by **Updated** or **Title**. Activity sorts chats into generating, unread, read, and waiting for approval. Cards waiting for approval carry a yellow dot. For a folder of your own, the badge next to its name in the sidebar counts chats that are unread or waiting for approval.

Statuses are yours to set up. Click the status icon on a card, choose **Edit statuses…**, and start from our suggestions: Backlog, To do, In progress, Waiting, and Done. Give each status an icon or an emoji, and drag them into the order you want. Drag cards between columns to change their status. Each card shows how long it has spent in its status in total, and hovering it lists the statuses before.

In a folder you share with write access, everyone who can edit it can set statuses and tags on every chat in it, so the board belongs to the team. Each card has the same menu as the sidebar, to rename, move, archive, or delete the chat, and its title shows the same hover preview. As a folder's owner, you can rename the chats teammates made in it.

_The invoice-import folder becomes a board with statuses, Codex chats are dragged into columns, and Columns by Activity shows the chat waiting for approval_

In List layout, the same chats can be grouped by status, tag, or activity, with **Show empty groups** if you want every group listed. The **Filter** menu, or **F** on the keyboard, narrows them by status, tag, person, activity, or date, and the search box looks through titles and messages. **Mark all as read** in the folder's menu clears the unread chats. Tags can have a color, which shows wherever the tag is used. Set it from the dot next to a tag in the tag picker, which the chat menu also has under **Tags**. A folder's own icon can be an emoji, set with **Change folder icon** in its **Edit** dialog.

The dropdown next to the folder's name switches the page between **Chats**, **Automations**, and **Knowledge**. **Knowledge** lists the knowledge bases, notes, chats, and files that new chats in the folder can use. Add, upload, drop, open, or remove them there. Folder pages open from memory when you come back to them and refresh in the background.

**Try it.**

1. Create a folder, set its default terminal and agent under **Edit**, and share it with your team with write access.
2. Start a few agent chats in it, then click the folder's name.
3. Choose **Display options**, set **Layout** to **Board** and **Columns** to **Status**, and add the suggested statuses.

### Schedule agents in a folder [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#schedule-agents-in-a-folder)

**Automations** on the folder page lists the folder's automations with their state and last run, and creates new ones there. An automation can run an agent on a schedule, such as a morning summary of new invoices or a nightly dependency check, and post each run as a new chat in the folder, marked with a clock. In a shared folder, everyone who can edit it can pause and run its automations and see their runs.

To schedule an agent, create an automation, pick a **Terminal** and **Working Directory**, and the agents on that machine appear in the model list. Keep the destination on a chat in this folder, because agent automations can't post to a channel, choose the agent, and set the schedule. Open WebUI checks that the terminal and agent are still there before each run.

We made an automation's own page editable in place: its name, instructions, schedule, model, terminal, and destination, with a **Save** button that appears once something changed. A **Status** switch pauses it, and **Next run** then says Paused. **Run now** runs it straight away, and **Copy link** sits beside it. The **More** menu has **Duplicate** and **Delete**. Below, each run reads "Ran" or "Failed" with its error, and clicking one opens its chat as a tab beside the page.

Administrators always have automations. Other people need the automations permission, which is off by default, and the folder page hides **Automations** without it. Turn it on in the default or group permissions under **Groups** on the admin **Users** page, or with `USER_PERMISSIONS_FEATURES_AUTOMATIONS`.

_An automation runs Codex on Workbench every night from the folder page, Run now starts it at once, and the run is a chat in the folder_

## Bring your own computer with Tether [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#bring-your-own-computer-with-tether)

Some work lives on your laptop. Tether is our desktop app for macOS, Windows, and Linux that connects your computer to Open WebUI. Once it's signed in, your computer appears under **Your devices** in the terminal menu, wherever you use Open WebUI, including your phone. A model, or an agent such as Claude Code installed on your laptop, can then work with its files, terminal, and browser, and on supported systems its desktop. Tether connects out to Open WebUI, so there are no ports to open and no VPN to set up, and your agents' logins stay on your machine.

_Maya connects Tether, installs Open Terminal and signs in, then the Codex on her laptop fixes the failing tests in a local folder_

**Try it.**

1. [Download Tether](https://github.com/open-webui/tether/releases/latest), enter your Open WebUI address under **Connect to Open WebUI**, and sign in.
2. When it asks **Set up Open Terminal?**, choose **Install and connect**. Access to local files and commands is optional and starts off. If you skip it, **Set up** on the connect screen brings it back.
3. In Open WebUI, select your computer under **Your devices** in the terminal menu, pick a folder, and give the model or agent a job.

The model is working with your real files, so point it at the right folder before you give it a job. Keep Tether running and the computer awake while you're away. Your device is only visible to your account, so for work your team should pick up, use a shared machine instead.

### Your local models and tools, everywhere you sign in [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#your-local-models-and-tools-everywhere-you-sign-in)

We've made Tether bring more than the computer. Models from Ollama, LM Studio, or any OpenAI-compatible server, OpenAPI and MCP tool servers, and other Open Terminal servers that you add in Tether appear just for you in the model picker, the Tools list of the + menu, and the terminal menu. That includes Open WebUI on your phone, or at a server you don't run. Open WebUI reaches them through Tether, so their addresses and keys never leave your computer.

MCP servers that run as a local command, which is how many are distributed, work too, with no proxy such as mcpo and no port to open. Tether starts the command on your computer and passes its messages through.

_Maya adds her laptop's Ollama and a local MCP server in Tether, then a small local model uses that tool to explain why a batch failed_

1. Open Tether's **Settings > Integrations**.
2. To add a local model server, click **+** next to **Models** and enter `http://127.0.0.1:11434/v1` for Ollama or `http://127.0.0.1:1234/v1` for LM Studio. In Open WebUI's model picker, the **Local** filter shows them, tagged with your device and connection name.
3. To add a tool server, click **+** next to **Tools**. Tool servers start switched off, so turn on **Enabled**. For an MCP server you run as a command, set **Transport** to **Local command (stdio)** and enter its executable and arguments. Tether runs it directly, without a shell, so use full paths rather than `~`. OpenAPI servers show under **Your devices** in the Tools list.
4. Click **+** next to **Terminals** to add another Open Terminal server you can reach from your computer.

Models need Tether 0.1.14 or later, and MCP servers 0.1.16. If you added integrations in 0.1.14 or 0.1.15, add them again in 0.1.16. A local MCP command runs with your own account's access and outside the sandbox below, so only add servers you trust. If a Tether model has the same ID as a model already in Open WebUI, the existing one is shown.

This replaces Direct Connections, which we removed. If you added models or tool servers in your own Open WebUI settings before, add them in Tether now, where they work in every Open WebUI you connect.

### Keep agents in one folder [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#keep-agents-in-one-folder)

When an agent works on your laptop, you might want it to work on one project and leave the rest alone. We added a sandbox in Tether 0.1.13 that holds Open Terminal, and everything it starts, agents included. The agent can only read and change files in the folder you pick, works offline unless you turn on network access, and accepts no incoming connections. It can still see that other files exist, with their names and sizes, but not what's in them. It needs no Docker, virtual machine, or administrator setup.

In Tether, open `Settings > Open Terminal > Sandbox`, turn on **Restrict file access**, choose the **Workspace folder**, and click **Apply and restart**. Turn on **Network access** if the agent needs to install packages or reach the internet. The folder can't be your home folder or the root of a drive.

The sandbox works on macOS and on Windows devices that support it, and not on Linux. While it's on, browser and desktop control stay off. If the sandbox can't be enforced, Open Terminal stays stopped rather than running without it. We'd turn it on before you let an agent work unattended on your own computer.

_Maya limits Tether to her invoice-import folder. The model can see the payroll file next to it but can't open it, and it reads the invoice report inside the folder without trouble_

### Use the sites you're already signed in to [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#use-the-sites-youre-already-signed-in-to)

In Tether's `Settings > Open Terminal`, you choose how the model gets a browser. **Launch Chrome** gives it a separate profile. **Connect to running Chrome** lets it work in your own Chrome, with your existing logins. Turn on remote debugging in Chrome and approve the connection when Chrome asks. Then open a **Browser** tab from the + menu in the chat, since the model's browser tools work through that tab. Open Terminal opens its own tabs and closes them when the session ends, leaving your other tabs alone. Any page can contain text aimed at the model, and the model can use every site you're signed in to, so turn on Tool Permissions and keep the chat on **Ask** when you use this, and stick to sites you trust.

_With Tether connected to her running Chrome and a Browser tab open in the chat, the model reads the overdue total from a dashboard Maya is signed in to_

### Ask about anything on your screen [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#ask-about-anything-on-your-screen)

Some questions start outside Open WebUI, like an error dialog, a chart in a report, or a form you've never seen. Press `Cmd+Shift+I` (`Ctrl+Shift+I` on Windows and Linux) in any app with Tether running, drag over the part of the screen you're asking about, type your question, and press Enter. The answer opens in Tether. You can paste an image instead, and attach up to four images, each under 10 MB. In voice calls inside Tether, screen sharing can attach a screenshot each time you speak.

_An invoice import fails in another app; Spotlight takes a screenshot of the error log, and the answer explains the date format and how to fix it_

### More in Tether [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#more-in-tether)

- Tether sends a desktop notification when a chat finishes or fails, a channel message arrives, or a calendar alert fires, even with no Open WebUI window open. Turn on **Browser Notifications** in Open WebUI's `Settings > Notifications` to get them.
- Open WebUI follows Tether's theme, so switching Tether to Dark turns Open WebUI dark too.
- Its terminal output picks up where it left off after a dropped connection, and it reconnects faster after the computer sleeps.
- **UI Scale** in Tether's General settings sets the app's size from 75% to 200%.
- Tether works behind Cloudflare Access, corporate proxies, and your own HTTPS certificates. For a certificate your computer doesn't recognize, **Trust Certificate** adds it.
- Model and tool connections in Tether take custom headers, under **Advanced**, for gateways that need them.
- Open Terminal in Tether has no open HTTP address by default. **Allow HTTP access** opens one, for your computer or your network, and **Copy URL and API key** gives you what other apps need.
- If Tether's Open Terminal breaks, Tether repairs it.

_Maya sets Tether's UI Scale, closes the window while a reply runs, and a desktop notification brings her back to the finished chat_

## Your machine's desktop [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#your-machines-desktop)

Open Terminal machines have a desktop that models and agents can see and control. We made it more capable in the Open Terminal releases that came out alongside these, so update Open Terminal to get the following.

- **Share your real Linux desktop.** Run `open-terminal run --desktop-mode host` to let the model see and use your logged-in desktop, with its open windows, instead of a separate one. Someone at the desktop approves the sharing. It works on X11 and on Wayland desktops such as Ubuntu GNOME.
- **Desktop sound.** Unmute the viewer to hear the desktop's audio, on Linux, macOS 13 and later, and Windows. It needs FFmpeg on the machine.
- **GNOME on Wayland.** A separate GNOME desktop now starts on Ubuntu 26.04 and other Wayland-only installations, with `--desktop-environment gnome`. Linux desktops use XFCE by default.
- **Apps open where you can see them.** Apps that the model starts with Open Terminal's commands, such as a browser, show their windows on the machine's desktop. Open the Desktop tab first.
- **Pasting works everywhere.** Pasting into a desktop that doesn't support the clipboard types the text in for you.
- **Smoother viewing.** The viewer follows your latest pointer position on slow connections, and the Browser tab and desktop sharing pause less between frames.

_A model on the Workbench machine opens a report in Chromium, and its window appears in the Desktop tab beside the chat_

## A workspace beside the chat [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#a-workspace-beside-the-chat)

Since v0.13.0, a chat can open files, terminals, a browser, and a desktop in tabs beside it. We've made that workspace something you can arrange and come back to.

- **Split panes.** On a large screen, click **Split screen**, or drag a tab or a chat to the edge, to see several tabs side by side in panes you can resize. Click **Split screen** again to go back to one pane. On a touch screen, long-press a tab to drag it.
- **Tabs remembered per chat.** Each chat's open tabs, split layout, and selected machine are saved on the server for each person, and come back on any device. Terminal and Browser tabs reconnect to the same running session after a reload, and closing a terminal tab asks **Stop terminal?** before it ends the shell.
- **Pages open as tabs.** Notes, channels, the workspace, automations, the calendar, the playground, the home page, and new chats from pinned models open as tabs beside the current chat, each with its icon. Click or drag them from the sidebar, pick them in the user menu, or follow a link to one in a message. A link to a page that's already open switches to its tab, and the browser's window title follows the active tab.
- **More than one chat.** **New Chat** in the tab bar's + menu opens a separate chat as a tab, with its own model and machine. A chat dragged in from the sidebar opens as its own tab too. Each chat tab has a **…** menu with **Share**, **Rename**, **Move**, **Archive**, and **Delete**. Double-click any chat tab to rename it, or click the sparkles to have the model write a title.
- **Side chats.** Type `/side` to branch a side chat from the current conversation, with everything said so far. Side chats now run the full chat, with sources, token usage, follow-up suggestions, slash commands, queued messages, web search, tool approvals and questions, previews, notifications, and several models at once. Their HTML and SVG previews open in their own **Artifacts** tab, and they keep their place in the parent chat after a reload.
- **Overview, Artifacts, and Comments** open from the + menu of the tab bar. Overview opens as a tab.
- **Keyboard shortcuts** open the Files, Desktop, Comments, new chat, new file, new terminal, and new browser tabs, switch and close tabs, and toggle split screen. Menus and tooltips show each shortcut, such as `Cmd+\` for split screen and `Cmd+W` to close a tab, and you can change them in the **Tabs** group of `Settings > Keyboard`. Shortcuts act on the chat you're focused on, including a side chat.
- **Drop files anywhere.** Drop a file anywhere in a chat to attach it, not only on the message input. A small "Drop to upload" label shows where it goes.
- **A message input that fits.** When the input gets narrow, the terminal and folder pickers move into the + menu, and labels shrink to icons. The Tools and Skills rows of the + menu show how many you've selected, such as "2 selected". **Compare text** moved to the `/compare` command.

_Notes opens as a tab beside the chat, a second chat runs with another model and gets a title from the model, and /side branches a side chat that knows the conversation_

### Files and terminals [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#files-and-terminals)

- `Cmd+P` (`Ctrl+P` on Windows and Linux) finds any file on the selected machine by name or path.
- Open several Files tabs on the same machine, each at a different folder. Drag a box over files to select several, and hold a dragged file over another Files tab to move it there.
- The grid view shows image thumbnails and file type icons, and folders with something in them look filled.
- Drag files from the file browser into the message input to attach them, one or several at once.
- The Files tab updates by itself when files change, including from commands run outside the chat. Click the path above it to type a folder to go to, with Tab to complete names, or to copy the open file's full path.
- If a file you're editing changes on disk, **Save** asks before it replaces the new version with your edits.
- Markdown files switch between **Editor** and **Source**. The editor shows math, Mermaid diagrams, and callouts such as `[!NOTE]` as rendered blocks, and clicking one opens its source. **Outline** lists the headings and jumps to the one you pick.
- SVG files can be zoomed and panned.
- The code editor suggests words that already appear in the file, and Tab accepts the suggestion. Other text files open straight in the editor.
- Clone a Git repository from the file browser or the folder pickers, from an HTTPS or SSH address.
- Folders in the working directory menu have an **Open folder** button that opens them in a new Files tab.
- Terminal tabs are named after the program running in them, with icons for programs such as Claude Code, Codex, Python, and Node.js. Naming by program needs Open Terminal 0.17.8 on macOS and Linux.
- The terminal renders with WebGL where your browser supports it, so heavy output keeps up. When the connection drops, it says "Connection interrupted. Reconnecting to the same terminal…" and picks up where it was.
- With no machine selected, the new tab menu still offers Files, terminals, the browser, the desktop, and voice notes, and asks you to pick a machine from a searchable list.
- `Cmd+Alt+M` (`Ctrl+Alt+M`) records a voice note into the current folder, with a transcript if you want one, and opens it as Markdown. Escape cancels it.
- The same note open in two panes stays in sync as you type in either.
- The image edit tool can take images from the selected machine by file path.

_A Mermaid diagram in a Markdown file is edited from its source and redraws, Ctrl+P finds a chart in another folder, and Grid view shows thumbnails_

## Carry on from your phone [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#carry-on-from-your-phone)

Start an agent at your desk, then open the same chat on your phone. We save each chat's open files, layout, machine, and folder on the server, so they come back with it. With Tool Permissions on, a request that needs approval waits in the conversation, so approve it from wherever you are and read the changes when it's done. If your connection drops, the agent keeps working for up to an hour and catches you up when you're back.

_A request started at the desk waits on the phone, and approving it there lets Codex commit and push_

**Try it.** With Tool Permissions on and the chat set to **Ask**, start an agent on a task, open the same chat on your phone, and approve the request when it asks.

While an approval is waiting, the reply counts as still in progress and **Regenerate** stays hidden, and in a voice call the answer after the approval is read aloud.

A message you send while a reply is still running joins a queue above the message input, with **Send now**, edit, and delete. In your own saved chats, with the message queue on, that queue lives on the server, so it's kept when you close the page or switch devices. In chats with regular models, the reply wraps up at its next step so your message is answered straight away. In agent chats, it's answered once the agent finishes. **Send now** stops the running reply and answers the queue. The first message of a new chat appears right away, while the chat is still being created.

_A follow-up waits above the input while a long check runs, it's still queued after the page is closed and the chat reopened in another window, and the reply answers it_

## Cheaper, steadier tool chats [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#cheaper-steadier-tool-chats)

Chats with tools cost less now. The start of a tool conversation stays the same between rounds, so providers can serve it from their prompt cache. Since v0.13.1, citation instructions, recalled memories, the skills list, and attached knowledge come after your message instead of being rewritten into the start. In v0.13.4, with native function calling, the skills list and attached knowledge are only added again when they change or after compaction, and memories already in the chat aren't sent again.

Tool call arguments go back to the model exactly as it wrote them, so local servers such as llama.cpp and vLLM keep reusing their cache too. How much you save depends on your model, provider, and conversation. Anthropic models behind OpenRouter or LiteLLM also keep their cache markers on tool results.

We made tool calling more forgiving, too, because not every model formats tool calls cleanly, especially smaller local ones.

- Tool calls run when a model wraps the arguments in code fences, encodes them twice, or sends numbers and true or false as text. A tool call written out as plain text is recognized and run.
- A tool call that fails twice with the same arguments ends the loop, so the model writes an answer. Reaching the tool call limit also ends with a final answer, and a reply cut off by the token limit doesn't run its unfinished calls.
- With Tool Search on, the model can run several tools it found in one `call_tool` request, a malformed call no longer turns tools off for the rest of the reply, and a call waiting for approval shows which tool it is.
- Replies where a model called a tool without writing text are sent back without an empty message, so proxies such as LiteLLM don't turn them into a placeholder line the model then copies.
- A command or tool server call that runs past `AIOHTTP_CLIENT_TIMEOUT_TOOL_SERVER` reaches the model as a timeout, so it can tell you.
- Tool calls keep the short label the model gave them, also when one call in a group fails, and the model sees its earlier labels when it continues.
- Context compaction shows "Compacting context" in the reply while it runs, keeps the earlier summary through repeated compactions, after a failed reply, and after a tool result too long to answer, and summaries aren't cut off at 1,000 tokens.
- Chats with Ollama models no longer get stuck after a tool call with cut-off or empty arguments, and the final answer after tool use works on vLLM.

_A 4B model running locally in Ollama compacts a long chat, then lists a folder with a terminal tool_

**Try it.** If tools didn't work with a local model before, turn them back on for that model and ask it to do something that needs one, such as reading a file from the selected machine.

## Faster chats, files, and pages [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#faster-chats-files-and-pages)

Some numbers from these releases:

| What | Before | After |
| --- | --- | --- |
| Typing after pasting 16,000 lines | 8.6 seconds per keystroke | 74 milliseconds |
| Prompt cache writes per turn in a tool chat, from a [community report](https://github.com/open-webui/open-webui/issues/33852) | 33,000 to 158,000 tokens | 472 tokens |
| Showing a reply with 300 code blocks that arrives at once | More than 2 minutes | 9 seconds |
| Opening a 1,500-page PDF in the file preview | More than 30 seconds | About 1 second |
| Loading a 2 MB profile picture | A few hundred milliseconds | About 15 milliseconds |
| Opening a 750 KB Markdown file from a terminal | About 19 seconds | About 2 seconds |

Large chats open about twice as fast, and marking a chat read or unread or removing a tag is 4 to 6 times faster. Sending a message no longer loads the whole conversation to check who may access it, or rewrites it when nothing about it changed. Long coding agent chats write several times less to the database while a reply streams.

Channels, long reasoning streams, the sidebar chat list, folders, and the model list with Redis load faster. Large PDFs use far less memory, because only the pages near the screen are drawn, so the browser's find only matches text on those pages. Exporting a knowledge base holds up other people's requests far less.

_A 1,500-page PDF opens at once and jumps to page 1,000, and a reply with 300 code blocks shows up in seconds_

## Documents and knowledge [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#documents-and-knowledge)

### Search your OpenAI vector stores [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#search-your-openai-vector-stores)

If your documents already live in vector stores on OpenAI, Azure OpenAI, or LiteLLM, Open WebUI can now search them as knowledge. The provider runs the search, so you don't need a matching embedding model, and nothing is copied. One knowledge base can search several stores at once, with the results merged, and a store that fails doesn't hide the others.

There are two ways to use them. Attach stores to a knowledge base you make, or turn on **List stores as knowledge bases** to show the connection's stores as read-only knowledge bases that stay in sync with the provider and share the connection's access settings. People then pick them like any other knowledge base in the chat.

_Two OpenAI vector stores in one knowledge connection, searched from the chat with # and cited in the answer_

**Try it.** In `Settings > Admin > Integrations`, under **External Knowledge Sources**, click **Add Connection**. **OpenAI-compatible** is the default provider. Enter the endpoint and key and click **Verify Connection**, which lists the stores, then add their IDs under **Vector Stores**, such as `vs_abc123`. Enter or a comma adds another. To list stores as knowledge bases instead, turn that on when you add the connection, and use **Store IDs** to limit which ones, or leave it empty for all. **Test** runs a sample query.

### Files read in full [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#files-read-in-full)

Short documents make more sense read whole, so we now include files with up to 50,000 characters of text in full, both when **Preload files** adds them and when the model reads them with its file search tool. The file viewer tells you when that happens.

_A short contract attached in full, and one answer built from a clause near the top and one near the end_

**Try it.** Attach a short document to a chat with a model that supports tools and has its Files tool on, and ask about it. With native function calling, models read attachments with their file tools, so Preload files is now off by default. For a model without tool support, turn on **Preload files** in its **Features**. Administrators can change the limit in `Settings > Admin > Documents` or with `RAG_FULL_TEXT_CHAR_THRESHOLD`.

### More for documents [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#more-for-documents)

- **Reindex Knowledge and Memory Vectors** in `Settings > Admin > Documents` now extracts each knowledge file again from its original, with your current settings, so PDFs get their page numbers back in citations.
- External knowledge bases search with every query the model generates, at the same time, instead of only the first.
- Knowledge searches find text with punctuation, such as "Art. 40".
- PowerPoint files with sections preview and show their comments. Excel workbooks with a sheet too large to preview still open, with that sheet available to download.
- Scanned PDFs that store pages as JPEG2000 images preview instead of showing blank pages, and zooming in PDF, Word, and PowerPoint previews stays put when you switch tabs.
- With the Playwright web loader, attached pages and web search results keep definition lists, figures with captions, and collapsible sections, so documentation sites keep their parameter descriptions.
- Web pages behind an internal certificate authority load, and unreachable sites are skipped after 10 seconds instead of about two minutes.
- Notes with footnotes open, and note recordings upload to S3-compatible storage.

_Reindexing from the Documents settings, and a PowerPoint deck in Files that previews its sections and Priya's review comment_

## Small improvements across the app [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#small-improvements-across-the-app)

We shipped a lot of small changes in these four releases, and together they make Open WebUI nicer to use every day. Here they are by area.

### Chats and messages [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#chats-and-messages)

- Replies show the time they finished, not the time you sent the prompt.
- Token counts in the usage tooltip are grouped by thousands for your language, such as 26,678,623.
- Unsent text stays with the chat or folder you typed it in, so each folder keeps its own draft, and drafts in chats that already have messages come back after a reload.
- Temporary Chat stays on through a reload, and choosing **Temporary** in the `/` menu of a new chat works.
- With Temporary Chat on by default, a new chat you switch to a normal chat stays normal after a reload.
- Temporary chats are skipped by the background memory review, so nothing from them becomes a memory.
- If a window missed a turn, such as a laptop that just woke up, saving an edited message keeps the newest reply in the conversation.
- Chats whose saved history loops back on itself open and show their messages.
- The file ask box, follow-up suggestions, and queued messages tell you "Model not selected" when there's no model, instead of trying to send.
- Continuing a reply on a Responses API connection adds to the reply you already have.
- With location access on, sending a message doesn't wait for a slow location lookup.
- A thumbs-down reason and comment are saved even when you save them before the feedback tags finish.
- Whole-number parameters such as Context Length, Max Tokens, and Seed reject a value with a decimal point, so "32.767" can't sneak in for 32767.
- Switching an optional valve from Default to Custom in the chat controls works, and emptying an on/off or number valve returns it to its default.
- Conversation summaries written with the plain summary prompt include earlier tool calls.
- DeepSeek thinking mode works with skills, knowledge, and memories when the connection's Provider is set to llama.cpp.
- A link to a folder in a message opens the folder in Open WebUI, and Ctrl or Cmd click opens a chat, note, or channel in a new browser tab.
- Workspace search finds message text and shows matching excerpts, and searches in notes, archived and shared chats, the user list, and the knowledge and file pickers always show results for what you typed last.
- A prompt sent from an embedded app or HTML preview goes only to the chat that shows it.
- Reference Chats leaves out the chat you're in.
- A chat that finishes while it's covered by another tab still sends its notification.

_A reply's finish time, token counts with separators, and an unsent draft that comes back after a reload_

### Side chats and sub-agents [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#side-chats-and-sub-agents)

- A new side chat says whether it will be saved or is temporary, and it's named after its first message.
- New side chats start with the same default tools, skills, filters, and web search as a normal chat with that model.
- Side chats work with the Temporary Chat permission turned off, and **Fork chat** in a side chat opens the copy.
- A side chat that finishes in the background sends a notification, like the main chat.
- After you pick a model in a side chat, the cursor goes back to its message input.
- A sub-agent that needs the browser to answer a question, such as a confirmation or a form, shows it in the tab that has the chat open.
- Two background sub-agent reports that finish close together stay in the same branch of the chat.

_A side chat says its messages are saved, and it shows in the chat list named after its question_

### Coding agents and terminals [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#coding-agents-and-terminals)

- Agents only show up where they can work. They stay out of Admin Models, base-model pickers, Arena, task model settings, group defaults, sub-agent settings, channel mentions, and the Playground.
- Changing terminals swaps the agent list straight away, and a slow list from a chat you've left can't replace the current one.
- When a terminal refuses to start an agent, the reply shows a short error you can read.
- The terminal and folder pickers lock while a reply is being written, so a chat's machine can't change halfway through.
- In a folder with a default terminal, a terminal you pick or turn off stays that way when you change the model. Switching to a model without its own terminal keeps the one you selected.
- Per-chat terminals aren't offered in temporary chats, where they can't work, and a remembered terminal that no longer exists is unselected when the page loads.
- If a folder's working directory is missing, your first message stays in the box with a warning, instead of creating an empty chat.
- A message that mentions one of the terminal's skills keeps its skill chip after a reload, and the + menu lists the terminal's skills straight away.
- When you switch a chat to another terminal, its Files tabs switch with it. A Files tab at the machine's home folder is titled Home.
- A file shown in a reply gets its preview, **Download**, and **Open** back as soon as its terminal is selected again.
- Browsing to another folder in Files leaves the chat's working folder alone, and opening Files again takes you back to where you were.
- An unsaved edit to a terminal file comes back, with its unsaved mark, when you return to the chat. Signing out warns you about unsaved file edits.
- The file viewer keeps the file's real size through Refresh and the back and forward arrows.
- The right-click menu in a Files list stays inside the window, near the edges too.
- Selecting files doesn't shift the rows, clicking an empty area clears the selection, and the delete confirmation names the file.
- In the Browser tab, **Open in new tab** beside a port opens the server running on it. With the chat open in two windows, the window that lost the browser says it opened in another viewer, and dragging the side panel divider resizes the page smoothly.
- In Open Terminal, a command that prints a lot of text slows down rather than losing output, a failed upload leaves the original file alone, opening a large folder such as `/` stays responsive, and the Browser tab keeps updating after you follow a link and shows emoji and flags.

_The terminal menu lists every machine, each with System info and View files in its … menu_

### Folders, the sidebar, and menus [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#folders-the-sidebar-and-menus)

- Pinning, unpinning, archiving, or restoring a chat keeps its place in the list, and pinning a chat or moving it to a folder doesn't mark it as read.
- Opening a chat in another browser tab keeps a folder's chat list on the page you were on, and dropping a chat on the folder it's already in does nothing.
- Folder chat lists update straight away when a chat is renamed, moved, archived, or deleted, and folders keep their loaded chats when you collapse and expand them. Renaming a chat renames its open tabs.
- Deleting a chat, channel, note, or automation closes its open tabs, and opening a chat that's already in a tab doesn't show it twice.
- A chat's hover preview in the sidebar stays out of the way of another chat's open menu, and shows your messages as bubbles even with Chat Bubble UI off.
- Menus that open above their button, such as **Model controls** and the + menu, grow upward, and right-aligned menus in Firefox open in place. Text boxes inside menus, such as tag search, keep their arrow keys.
- Clicking the sidebar closes an open model picker, and the model picker's tag filter picks up tags models gain while a chat is open.
- The calendar hides its sidebar when it's open in a narrow pane, and the calendar and automations lists refresh when you come back to them.
- The Temporary Chat button is on new chats with the tabbed layout, and admin banners show on the new chat page with tabs open.
- Tab content stays below the tab bar at a UI scale above 1, the chat background shows behind the tab bar, and top bars don't blur a page background image.
- When every control in a group is hidden with **Visible controls**, the empty group goes too.
- The Unpin button on a pinned note has a tooltip, and the Tools count in the workspace holds steady while the page opens.

_The badge on Maya's folder counts a chat waiting for approval, which has a yellow dot and a hover preview_

### Notes, channels, calls, and automations [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#notes-channels-calls-and-automations)

- Comments on a note open from a button in its top bar, and in a note you can edit, **Comment** is in the formatting toolbar. Heading 1, 2, and 3 share one heading menu, in notes and the message input.
- Dropping a file onto a note adds it to the note, and a code block without a language shows as plain text, which keeps long notes quick.
- Calendars can be renamed and recolored from the pencil next to each one.
- Channel headers have a **Search** button for that channel's messages. A channel only marks itself read while you can see it, and switching channels closes the open thread.
- Threads load older replies, and Esc and Ctrl or Cmd+Enter cancel or save the message you're editing.
- Clicking the browser notification for a reply in a thread opens that thread. Clicking a desktop notification opens the chat, channel, or calendar it's about.
- The channel Webhooks window keeps your edits when a new message arrives.
- **Return to call** reopens the voice call you're in after you switch to the chat tab, and reply audio plays only when Auto-Playback is on.
- Pick a **Notification sound style** in `Settings > Notifications`, Chime, Soft, Bell, or Tap, with a play button to hear each one. The sound plays in one tab only.
- The **Schedule** button when creating an automation shows the schedule in your language, and models that create automations use a schedule format that works.

_A note with comments in its top bar and one menu for headings_

### Tools, skills, and models [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#tools-skills-and-models)

- The Tools and Skills lists in the + menu are grouped by where each entry comes from, such as the workspace, tool servers, or the terminal.
- The tool, skill, filter, action, and sub-agent pickers in the model editor show each item's description, and switches with a description show it on hover.
- Drag files and folders onto a skill's files in the workspace to upload them into the open folder.
- MCP apps can suggest a message for the chat, which you confirm before it's sent, and they keep their state while the message around them updates.

_Tools in the + menu, grouped by where they come from, with 2 selected_

### Math and previews [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#math-and-previews)

- Formulas in table headers keep their letters as written, and inline formulas next to a hyphen render.
- Resetting the zoom of an image preview from below 10% returns it to 100%, centered.
- A file preview opened from the Controls menu stays open when you click inside it, and restoring a reply doesn't reopen its previews.

_A table whose header formula keeps its lowercase letters_

### Phones, touch screens, and the desktop app [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#phones-touch-screens-and-the-desktop-app)

- On a phone, opening, switching, or starting a chat doesn't bring up the keyboard over the conversation, and closing the + menu doesn't either.
- On iOS with Auto-Playback off, Open WebUI leaves audio from other apps playing.
- On touch screens, long-press to drag tabs, move them between panes, and drag files into the message input.
- Writing a comment on selected text on Android keeps the comment box open with the keyboard up.
- In the desktop app, banners and menus near the top of the window take clicks instead of dragging the window.
- Open WebUI works over plain HTTP at a LAN or Docker address, including chats, comments, Markdown editing, the New File, New Terminal, and Browser tabs, and clipboard prompts. Copy buttons work there too, **Copy Formatted Text** keeps its formatting, and **Auto-Copy Response** tells you when the browser blocks the clipboard.

_At phone size, the machine and folder pickers sit inside the + menu_

## Accessibility and languages [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#accessibility-and-languages)

We kept working on keyboard focus, so it stays where it belongs through more editing and navigation. It stays on buttons while they save, in place when you cancel an edit or switch message versions, and on the page buttons of lists. Closing a channel thread, a note panel, or a chat menu returns focus to where it was.

The sign-in skip link moves focus to the form, and a tab moved with `Alt+Shift+Arrow` keeps focus so you can move it several places in a row. The show password button is wider, holding Shift no longer swaps row buttons for Delete while you're using the keyboard, and Firefox keeps your place when you scroll up through a long chat.

Translations were updated for 50 languages, with a full pass on Brazilian Portuguese for the terminal, Git, spreadsheet, and tool settings.

_Alt+Shift+Right moves a tab while focus stays on it, and Escape closes the chat menu with focus back on its button_

## More for administrators [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#more-for-administrators)

### Set an approval policy [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#set-an-approval-policy)

Asking for approval on every tool call gets old fast, and Full access asks for none. We added **Auto** as a middle ground, controlled by an approval policy written in plain words. By default, the policy goes to the same model that's making the tool calls. Each call it makes carries a yes-or-no answer to "does this need approval under the policy?", and Open WebUI stops for the person when the answer is yes, or when the model doesn't give one. There's no extra service to run and no extra request per call.

The default policy asks before anything destructive or hard to undo, anything that communicates externally or publishes, financial actions, changes to security or access, anything that discloses credentials or sensitive data, and anything whose scope is unclear. Ordinary reads and clearly scoped, reversible work go ahead. Write your own to match how your organization works, such as "always ask before pushing to a shared branch".

_Auto is turned on with a one-line rule, the tests and the commit run on their own, and the push waits for approval_

1. In the **Tools** section of `Settings > Admin > Interface`, turn on **Tool Permissions** and **Auto permissions**, or set `ENABLE_TOOL_PERMISSIONS` and `ENABLE_TOOL_PERMISSIONS_AUTO`.
2. Leave **Engine** on **Default** to let the chat model apply the policy.
3. Write your rules in **Approval policy prompt**, or leave it empty to use the default. You can also set it with `TOOL_PERMISSIONS_AUTO_PROMPT`.

Coding agents work a little differently. Under Auto, Codex, Claude Code, and Grok use their own reviewers to approve routine actions and pass on only what they escalate. Claude Code and Grok need Open Terminal 0.17.19 for this. Your approval policy isn't sent to those reviewers. What they escalate, and every request from other agents, always asks with the Default engine.

To review agent requests against your policy, set **Engine** to **Decisions API**. It sends the tool, its arguments, the current request, and up to four recent user messages to a scoring service that implements `/decisions`, and asks when the score reaches your **Approval threshold**. Its settings are `TOOL_PERMISSIONS_AUTO_ENGINE=decisions`, `TOOL_PERMISSIONS_AUTO_DECISIONS_API_BASE_URL`, `TOOL_PERMISSIONS_AUTO_DECISIONS_API_KEY`, `TOOL_PERMISSIONS_AUTO_DECISIONS_MODEL`, and `TOOL_PERMISSIONS_AUTO_DECISIONS_THRESHOLD`, which defaults to 0.5.

Once it's on, Auto becomes the mode for anyone who hasn't picked one, and existing choices stay. People switch modes from the + menu in the message input. If a review fails or times out, the call asks. Auto doesn't work in channels.

### Decide who shares what [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#decide-who-shares-what)

An agent's login stays on the machine, and anyone who can use the machine can use its agents. On a standard Open Terminal, everyone with access shares its files and the signed-in agent account, which is what lets teammates pick up each other's work. We'd give each team its own machine and grant it to that team's group. [Multi-user mode](https://github.com/open-webui/open-terminal#built-in-multi-user-mode) gives each person their own workspace and agent login on one machine. For real isolation, Terminals gives each person, chat, or model its own container.

Each chat saves its terminal and folder. To give every chat a computer, pick a **Default terminal** under **Model Defaults** in `Settings > Admin > Models`, where **Terminal** is on by default. It applies to models without a terminal of their own. **Model Defaults** also has a **Tools** picker for the tools new chats start with, and the new model form starts with them selected. A group can now have several default models, set under **General** in the group's settings.

The **Sub-agents** permission, or `USER_PERMISSIONS_FEATURES_SUBAGENTS`, is on by default. Turn it off for users and groups who shouldn't have sub-agents, and they lose the timer tool with it. When you change permissions, open pages follow without a reload. A new chat becomes temporary once you enforce temporary chats, and turning off Folders, Channels, Notes, or multiple models takes effect on screen right away. Turning off Notes also stops live editing in notes that are already open.

_Model Defaults with a Default terminal and two tools, and a new chat that starts with both_

### Roll out Tether [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#roll-out-tether)

Tether connects out to the address people already use, so you don't open anything to reach their machines. People sign in the way they already do: with a password in Tether's own window, or with single sign-on, which opens their usual browser.

- A device is only visible to the account that connected it, and local file and command access starts off.
- Your instance needs WebSocket support, and Redis if it runs more than one worker.
- The sign-in renews while in use and expires after 90 days without use. Change that with `SESSION_EXPIRES_IN`.
- Tool servers and terminals from Tether need `ENABLE_TOOL_SERVERS` and `ENABLE_PLUGINS`, both on by default.
- Requests to a Tether computer keep going as long as data flows, read-only requests are repeated after a brief disconnect, and a busy computer refuses new work right away instead of timing out. A computer that connects after the page loads shows up under **Your devices** without a reload.
- Tether is free for personal, non-commercial use. Using it in an organization requires an Open WebUI Enterprise License, as its [README](https://github.com/open-webui/tether) explains.

We replaced Direct Connections with Tether. The personal connection and tool settings are gone from Open WebUI, and what people saved there isn't moved into Tether. Ask them to add those models and tool servers again in Tether's **Settings > Integrations**.

_Tether asks for the Open WebUI address, then shows the sign-in page you already use_

### Image, video, and knowledge connections [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#image-video-and-knowledge-connections)

We moved images and videos to connections, the way models work. In `Settings > Admin > Images`, click **Add Connection** for each image server, such as LiteLLM or another OpenAI-compatible server, Gemini, ComfyUI, or AUTOMATIC1111. Choose which models it offers for generating or editing images, and set who can use it. OpenAI-compatible ones take the same sign-in options and custom headers as model connections, and a LiteLLM server lists its image models by itself. Then pick the **Default Generation Model** and **Default Edit Model**, and give a model its own default image model in its settings if you like.

Videos work the same way in `Settings > Admin > Videos`, once you turn on **Video Generation** or set `ENABLE_VIDEO_GENERATION`. Add a connection, with **Provider** set to **OpenRouter** for OpenRouter. If you leave it on **Default**, an OpenRouter address is still treated as OpenRouter. Choose a **Default Video Model**, and set per-model defaults and access. People also need the **Video Generation** permission, which is off by default, or `USER_PERMISSIONS_FEATURES_VIDEO_GENERATION`. `VIDEO_GENERATION_TIMEOUT` and `VIDEO_GENERATION_POLL_INTERVAL` default to 900 and 5 seconds.

Vector stores connect under **External Knowledge Sources** in `Settings > Admin > Integrations`, as covered in [Search your OpenAI vector stores](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers#search-your-openai-vector-stores). The connection shows as its own row, with how many stores it lists, a switch, and a cog to configure it.

_Video Generation turned on, an OpenRouter connection with Veo as the Default Video Model, and the Video Generation permission given to Engineering_

### Keep a record [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#keep-a-record)

Agent sessions are stored as chats on your server, with each tool call, result, and approval. Administrators can open people's chats while `ENABLE_ADMIN_CHAT_ACCESS` is on, which it is by default. Admin analytics name coding agent replies by agent and model, and the session timeline shows model names.

- Audit logs mask API keys, tokens, and secrets saved in admin settings, not only passwords.
- The default server log leaves out search queries, found file names, search results, and the address of a failing reranker. Set `GLOBAL_LOG_LEVEL` to `DEBUG` to see them.
- Removing a stored OAuth session, because of `OAUTH_MAX_SESSIONS_PER_USER`, a sign-out from the identity provider, or a reconnected MCP server, logs a warning with the user, the session, and the reason.
- Connection headers can use `{{USER_IP}}` and `{{X_FORWARDED_FOR}}`, which both carry the client's address, so a model gateway can tell where each request came from. Both are empty for automations.
- Deleting an account removes it from the access lists of everything it was given.

_Analytics names coding agent replies by agent and model, lists each agent chat with who ran it, and shows the steps the agent took_

### Other settings [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#other-settings)

- Save on admin settings pages such as General, Interface, Documents, and Images shows how many settings changed. Click it to see each old and new value before you confirm, with passwords and keys hidden.
- **Tool Search** in the **Tools** section of `Settings > Admin > Interface` has a **Search engine**: keywords, embeddings from your Documents embedding model, or a relevance-scoring API with its own **API Base URL**, **Model**, **Relevance threshold**, and **Prompt**. Set it with `TOOL_SEARCH_ENGINE` as `bm25`, `embeddings`, or `decisions`, and `TOOL_SEARCH_DECISIONS_*` for the API.
- **Tool Call Labels**, or `ENABLE_TOOL_CALL_LABELS`, asks the model for short descriptions of its tool calls in the user's language.
- **Chat Read Limit** in `Settings > Admin > General`, or `VIEW_CHAT_MAX_CHARS`, caps how much of an earlier chat the Chat History tools return, keeping the newest messages.
- **Full Text Threshold** stays visible, and grayed out, while **Always Use Full Text** is on, and the file viewer says when the administrator has made full text always on.
- The admin Models list has an **Arena Models** view, and each arena model in Evaluations has a **Clone** button. The Evaluations feedback filter clears when you delete a model's last feedback.
- Long prompt templates and JSON fields in admin settings scroll instead of stretching the page.
- Groups need a name before they can be saved.
- The sign-up page and the user dialogs accept email addresses with non-ASCII characters.
- The toggles under **Visible controls** in `Settings > Admin > Interface` show their names.
- Open Terminal connections with **Auth** set to **Session** take an API key too, so **Verify Connection** and the terminal tools work with it.
- A `TERMINAL_PROXY_HEADERS` entry in any letter case replaces the terminal's own header, and repeated headers from the terminal, such as several cookies, are all passed on.

_Three Interface settings changed, and Save shows the old and new values before anything is saved_

### Fixes worth knowing [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#fixes-worth-knowing)

- A sign-in provider that's briefly unreachable during a token refresh no longer removes the user's stored sign-in, for tools, connections, and MCP servers. Two refreshes of the same MCP sign-in at once wait for each other, across workers with Redis.
- Signing in past `OAUTH_MAX_SESSIONS_PER_USER` removes the least recently used session, so a device still in use stays signed in, and signing out removes that browser's stored session unless it's the person's only one.
- When a single sign-on session that a tool server forwards has ended, picking its tools in the + menu asks you to sign in again.
- Automatic single sign-on no longer fails with a state mismatch after a session expires.
- MCP servers reconnect after they restart mid-reply, connect with tool lists larger than 1 MB, and sign in over OAuth with HS256 tokens or very large response headers.
- Busy servers with `DATABASE_ENABLE_SESSION_SHARING` on no longer run out of database connections on bursts of page loads.
- During a large knowledge base sync, chat attachments and other uploads outside knowledge bases keep moving. Knowledge base uploads take turns, using at most half of `THREAD_POOL_SIZE`.
- Workspace search on PostgreSQL works when stored text contains null characters.
- Sending a message on a Redis Cluster deployment no longer fails while Tether's relay starts.
- Local speech-to-text works again in pip installs. The MinerU loader works with MinerU 4.1 servers, Milvus stores each file's chunks once, and large sparse spreadsheets upload quickly.
- A local embedding model folder saves in `Settings > Admin > Documents`, along with its batch size.
- Qdrant 1.20 servers connect without a version warning.
- The admin endpoint that lists all users includes each user's groups.
- Server logs stay quieter: leaving a chat while its layout saves, closing a terminal view right after opening it, MCP servers a user hasn't connected yet, and OAuth token refreshes with a client secret no longer add errors or warnings.
- Building the Docker image that includes Ollama fails if Ollama didn't install, so you can't end up with an image that can't start it.

_Maya's single sign-on session has ended, picking the tool asks her to sign in again, and the tool then gets her token_

### For developers [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#for-developers)

- Open WebUI publishes `model.available` and `model.unavailable` events when a model appears in or disappears from the model list.
- Coding agent models report `owned_by: "terminal"` in the models API.
- Real-time updates for notes, comments, the inbox, access changes, and channels arrive as typed messages on the `events` socket channel.
- Chat responses report `write_access` for whether you can reply, next to the saved `share_mode`.
- Image generation and edit requests through the API run on the model they name, which has to be one of the caller's image models.
- Functions and Tools receive the model without its profile image.
- The Ollama OpenAI-compatible endpoint accepts assistant turns with only tool calls.
- Docker images install Python packages from hash-pinned lock files, so the same version always installs the same packages.
- Adding the same new tag to several chats at once through the API tags all of them.
- Comparing versions of a skill, tool, function, or prompt is limited to 5,000 lines per version.
- A person can have up to 20 collaborative documents, such as notes, open across all their tabs.
- `DATA_DIR=~/.open-webui uvx --python 3.12 open-webui@latest serve` runs Open WebUI with `uv` in one line.
- Open Terminal can start with `--isolated` to skip saved settings, notebook support is an optional install with `pip install 'open-terminal[notebooks]'`, and the startup banner and `open-terminal --version` show the installed version.

## Before you upgrade [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#before-you-upgrade)

Back up your database and associated data first. v0.13.1 changes the database schema, so update every instance together in multi-worker, multi-server, or load-balanced deployments. Rolling updates aren't supported. v0.13.4 converts your image settings into connections on its first start. Read the rows at the top before you start the new version.

| What changed | Version | What to do |
| --- | --- | --- |
| Security fixes are included | v0.13.1 | Update now, and follow the [security advisories](https://github.com/open-webui/open-webui/security/advisories) as they're published |
| Database schema changes | v0.13.1 | Back up first and update all instances together |
| With OAuth group management on, token exchange needs a groups claim for users in a group | v0.13.1 | Check that your identity provider sends a groups claim in the userinfo or the token |
| Terminals connections need Terminals 0.4.0 or later, and the policy settings on the connection are gone | v0.13.4 | Follow the manual [move to 0.4.0](https://github.com/open-webui/terminals/blob/main/CHANGELOG.md#moving-to-040-manually) in the Terminals changelog, remove `TERMINALS_OPEN_WEBUI_URL` and `TERMINALS_TOKEN_CACHE_TTL`, and pick one of the new terminals again for models, folders, automations, and chats that used the old connection. Open Terminal and Tether connections aren't affected |
| Direct Connections are removed, with `ENABLE_DIRECT_CONNECTIONS`, `ENABLE_DIRECT_INTEGRATIONS`, and `USER_PERMISSIONS_FEATURES_DIRECT_TOOL_SERVERS` | v0.13.4 | Ask people to add their own models and tool servers in Tether 0.1.14 or later, or 0.1.16 for MCP |
| Image settings become image connections on first start, and image environment variables such as `IMAGE_GENERATION_ENGINE` and `COMFYUI_BASE_URL` are no longer read afterwards | v0.13.4 | Manage images in `Settings > Admin > Images`, and check who can use each converted connection, since everyone who could generate images before keeps access. The variables are still read if `ENABLE_PERSISTENT_CONFIG` is off |
| OpenAI image generation defaults to GPT-IMAGE 2, and the shut-down DALL·E models are gone | v0.13.1 | Pick another model if you relied on DALL·E |
| Image API requests run on the model they name, which has to be one of the caller's image models | v0.13.4 | Check API clients that send a model name for image generation |
| With Tool Permissions off, the default, coding agents' requests are approved as they go | v0.13.1 | Turn on Tool Permissions if people should approve agent actions |
| Git discard also removes staged and new files | v0.13.1 | Read the confirmation: files not in the last commit are deleted and can't be recovered through Git |
| Coding agent model IDs use only letters, digits, dashes, and underscores | v0.13.4 | Pick agent models again in pins, default models, and automations, including most Codex models |
| Coding agent models report `owned_by: "terminal"` in the models API | v0.13.3 | Update API clients that filtered on `"agent"` |
| The first new message in an agent chat from an earlier version starts a new agent session from the chat so far | v0.13.4 | Nothing |
| Preload files is off by default with native function calling | v0.13.1 | Turn on **Preload files** in **Features** for models without tool support or with Files off. Legacy calling and API requests keep the old behavior |
| Retrieval defaults become 10 for `RAG_TOP_K` and `RAG_TOP_K_RERANKER`, and 1024 for `CHUNK_SIZE` | v0.13.1 | Saved settings stay. Expect more retrieved text with the defaults. Existing chunks change only when files are reindexed |
| Files under 50,000 characters are used in full | v0.13.1 | Change `RAG_FULL_TEXT_CHAR_THRESHOLD` if that's too much for your models |
| Recalled memories, the skills list, and attached knowledge arrive as hidden tool results with native calling | v0.13.1 | Check custom pipes that expect the last message to be from the user |
| Side chats are saved as regular chats | v0.13.1 | Turn on Temporary Chat, or enforce it, when those conversations should stay temporary |
| Auto becomes the default mode for anyone without one once enabled, and the Decisions API engine sends tool arguments and recent messages to its scoring service | v0.13.1 | Review the policy and engine before turning it on |
| New terminal connections save chat uploads into the terminal's working folder, and Tether computers always do | v0.13.4 | Existing connections keep their setting. Open Terminal 0.17.20 is recommended for multi-user setups |
| Docker images install Python packages from hash-pinned lock files | v0.13.4 | Custom images that edit `backend/requirements.txt` must run `backend/update-locks.sh` |
| Real-time events for notes, comments, the inbox, and channels arrive on the `events` socket channel, and chats report `write_access` | v0.13.4 | Update custom clients that listened for names such as `events:note` or read `share_mode` to decide who can reply |
| Reaching the tool call limit ends with a final answer, and Tool Search no longer lists hidden tools in the prompt | v0.13.1 | Check custom instructions that assume the model sees that list |
| Full Context Mode is now Always Use Full Text | v0.13.1 | Nothing |
| Overview, Artifacts, and Comments moved from the chat menu to the + menu of the tab bar, and Integrations moved into the + menu of the message input | v0.13.1, v0.13.4 | Turn on **Show Input Selections** to show selected tools and capabilities beside the input |
| Compare text left the + menu | v0.13.1 | Use the `/compare` command |
| Note comments open from a button in the note's top bar, and Heading 1, 2, and 3 share one heading menu in the formatting toolbar | v0.13.4 | Nothing |
| Add Context is now Attachments, Capabilities is now Features, and knowledge pickers say Knowledge instead of Collection | v0.13.4 | Nothing |
| Large-screen tabs always fill the chat area, and Show Files on Terminal Select is removed | v0.13.1 | Use split panes, and open Files from the + menu of the tab bar |
| Allow Side Chat no longer depends on the Temporary Chat permission, and now covers branching with `/side` | v0.13.1, v0.13.4 | Review group permissions if you relied on that |
| Browser tabs start in Chrome mode when the terminal offers it | v0.13.1 | Nothing. A failed start switches to Proxy mode with a message |

The [updating guide](https://docs.openwebui.com/getting-started/updating) covers the deployment steps, and the [release notes](https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md) are the full record of changes.

## Where to start [\#](https://openwebui.com/blog/v0-13-4-ai-that-does-the-work-not-just-answers\#where-to-start)

Here's where we'd start. Set up one shared machine with Claude Code or Codex signed in, and give it to one team. Have someone hand an agent a GitHub issue, share the chat when they have to stop, and let a teammate finish it. Then put a few of those chats in a shared folder and look at the board. When people start stepping on each other's files, give them machines of their own with Terminals. Tell us how it goes on the [issue tracker](https://github.com/open-webui/open-webui/issues).

_The Open WebUI Team_

## AI on your terms.

Your models. Your data. Your infrastructure.

[Get started →](https://docs.openwebui.com/getting-started/) [Enterprise sales →](https://openwebui.com/contact/sales)

* * *

### Related articles

[![Put your model to real work in Open WebUI](https://community.s3.openwebui.com/uploads/users/6ddf0023-1d2a-4af3-bbbe-41612061a0d8/2026/11/495fce26-10de-4456-bf2c-04dfc805b653.png)\\
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
Admin](https://openwebui.com/blog/what-is-open-terminal-in-open-webui) [![Introducing Terminals: a computer for everyone on your team in Open WebUI](https://community.s3.openwebui.com/uploads/users/6ddf0023-1d2a-4af3-bbbe-41612061a0d8/2026/11/01033e7a-d081-4343-a288-bba0dbc14a1d.png)\\
\\
news\\
\\
/\\
\\
November 18, 2026\\
\\
Introducing Terminals: a computer for everyone on your team in Open WebUI\\
\\
Terminals runs a sandboxed computer for each person, chat, or model in Open WebUI, on your own servers, inside limits IT sets once.\\
\\
![Open WebUI](https://openwebui.com/user.png)\\
\\
Open WebUI\\
\\
Admin](https://openwebui.com/blog/introducing-terminals)

We use optional analytics to improve our websites, and advertising cookies on this site. [Privacy Policy](https://openwebui.com/privacy).

AcceptReject