---
slug: 2026-10-13-airlock-see-what-your-ai-agent
stage: 03-research
topic: "Sandbox your AI agent and see what it touches (Airlock)"
depth: standard
generated_at: 2026-10-13T11:40:00Z
sources: 9
hub: "[[videos/2026-10-13-airlock-see-what-your-ai-agent]]"
---

# Research brief: Sandbox your AI agent and see what it touches (Airlock)

## Summary
Airlock is a free macOS app, one `brew install --cask simonmaddox/tap/airlock` away, that runs Claude Code or Codex in a virtual machine on a copy of your project and shows every process, file and network touch in one timeline before you accept changes per file. The most arresting constraint is Apple's own: two macOS virtual machines at a time. The strongest concrete case is the approval-prompt failure the site names plainly: prompts see only the command the agent typed, never what the build script went on to do. What could not be verified: the creator's design write-up (Access Denied), any reception beyond two HN comments, and App Store acceptance. No hard conflict between sources; the only tension is framing -- Docker's comparison table calls E2B, Daytona, Modal and Cloudflare cloud-only, which is vendor marketing, though E2B's own pricing page agrees it sells cloud tiers.

## Thesis
Stop clicking allow on your AI agent's fortieth prompt: run it in a disposable virtual machine that copies your project, logs every process it spawns, and hands you a per-file diff to accept or reject.

## Explanation path

The viewer starts where they already are: an agent in the terminal and an allow-click every time it asks. Establish why that gate fails before proposing anything -- the prompt only shows the command the agent typed, never what a build script does next, and attention is gone by the fortieth yes. With the problem felt, introduce the fence as an old idea applied to agents: a virtual machine the agent gets instead of your Mac, holding a copy of the project, so the worst case shrinks from your laptop to a disposable duplicate. Then deliver the half approval prompts never had: because Airlock observes from inside the virtual machine's operating system, it lists every process the agent spawned, every file it touched and every server it contacted, live, in one timeline -- the curl hidden inside a script appears next to the command that launched it. Show the return path: changes come back as a per-file diff you tick, with the dangerous categories (build scripts, git hooks, CI config) flagged because they execute on your Mac later. Close honestly before the landscape: containment is not trust -- public hosts stay reachable unless locked, and the model still calls Anthropic or OpenAI. Then place the move in the field: Docker Sandboxes does the virtual-machine trick across platforms and can burst to cloud, Claude Code and Codex ship built-in OS sandboxes that are off by default, and E2B rents cloud sandboxes by the hour -- so the Mac viewer can act tonight with one brew command, and the PC viewer knows which door is theirs.

## Claims
1. **Airlock runs Claude Code or Codex in a virtual machine on your Mac, works on a copy of your project, and you choose which of its changes to keep; it requires a Mac with Apple silicon running macOS 26 or later and installs from a DMG or with `brew install --cask simonmaddox/tap/airlock`.**
   - Source: Airlock: coding agents, kept contained, https://airlock.sorrel.systems/
   - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "Airlock runs Claude Code or Codex in a virtual machine on your Mac. It works on a copy of your project, and you choose which of its changes to keep." ... "For Macs with Apple silicon, running macOS 26 or later."
2. **Typing `airlock run claude` in a project folder opens Claude Code in your terminal as normal, with your CLAUDE.md, skills and memory, and the virtual machine cannot see your local network, so your router and NAS are out of reach.**
   - Source: Airlock: coding agents, kept contained, https://airlock.sorrel.systems/
   - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "Type `airlock run claude` in a project folder and Claude Code opens in your terminal as normal, with your CLAUDE.md, skills and memory." ... "It can't see your local network, so your router and NAS are out of reach."
3. **Approval prompts only ever see the command the agent typed, not what the build script went on to do, and by the fortieth you are clicking yes without reading, so Airlock turns the prompts off and moves the agent somewhere the only thing of yours it can touch is a copy of your project.**
   - Source: Airlock: coding agents, kept contained, https://airlock.sorrel.systems/
   - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "Approval prompts are meant to catch that, but by the fortieth you're clicking yes without reading. And they only ever see the command the agent typed, not what the build script went on to do."
4. **Airlock watches from inside the virtual machine's operating system, so it sees every process rather than just the commands the agent typed: if the agent writes a script that calls `curl`, you see the `curl`, with files touched and servers talked to in the same timeline.**
   - Source: Airlock: coding agents, kept contained, https://airlock.sorrel.systems/
   - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "Airlock watches from inside the virtual machine's operating system, so it sees every process, not just the commands the agent typed. If the agent writes a script that calls `curl`, you see the `curl`."
5. **When the agent is done you get every file it changed as a diff; you tick the ones you want applied and can undo them later, and build scripts, git hooks, CI config and the agent's own settings are flagged because they run on your Mac later.**
   - Source: Airlock: coding agents, kept contained, https://airlock.sorrel.systems/
   - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "When the agent's done, you get every file it changed as a diff. Tick the ones you want and they're applied to your project. Change your mind later and undo them. Build scripts, git hooks, CI config and the agent's own settings are flagged, because they run on your Mac later, and that's how an agent's code would get out."
6. **Apple allows two macOS virtual machines at a time, so that is the limit on concurrent Airlock sessions.**
   - Source: Airlock: coding agents, kept contained, https://airlock.sorrel.systems/
   - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "Apple allows two macOS virtual machines at a time, so that's the limit."
7. **Airlock's creator is Simon Maddox of England, UK, who wrote on Hacker News that Claude and Codex effectively have the ability to do anything they want on his laptop; the app is free, requires no account, and has no tracking or analytics.**
   - Source: Show HN: I built Airlock, to sandbox your AI agent and know what it's doing, https://news.ycombinator.com/item?id=50054620
   - Tier: community | Confidence: medium | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "I didn't like that Claude and codex effectively have the ability to do anything they want on my laptop and my local network" ... "It's free, requires no account, and has no tracking or analytics." (Creator identity corroborated by https://github.com/simonmaddox : "Simon Maddox", "England, UK".)
8. **The project is candid about limits: Airlock contains the agent, it does not make it trustworthy; sessions can reach public hosts unless you lock them down, so anything in the copy of your project could be sent somewhere, and model requests go to Anthropic or OpenAI as usual.**
   - Source: Airlock: coding agents, kept contained, https://airlock.sorrel.systems/
   - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "Airlock contains the agent. It doesn't make it trustworthy. Sessions can reach public hosts unless you lock them down, so anything in the copy of your project could be sent somewhere."
9. **Claude Code ships its own sandbox around shell commands, enforced by the operating system (Seatbelt on macOS, bubblewrap on Linux and WSL2) and built on the open source @anthropic-ai/sandbox-runtime package, but the sandbox is off by default.**
   - Source: Configure the sandboxed Bash tool - Claude Code Docs, https://code.claude.com/docs/en/sandboxing
   - Tier: docs | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
   - Quote: "The sandbox is off by default." ... "macOS: sandboxing uses the built-in Seatbelt framework" ... "Claude Code builds the sandbox on the open source `@anthropic-ai/sandbox-runtime` package."
10. **Docker Sandboxes is the established cross-platform alternative: it runs Claude Code, Codex and other agents in MicroVM environments that each get their own kernel and no path back to the host, locally or in Docker-managed cloud, with cloud compute metered from $0.07 per hour for a Micro sandbox.**
    - Source: Docker Sandboxes | Sandboxes for Coding Agents | Docker, https://www.docker.com/products/docker-sandboxes/
    - Tier: primary | Confidence: high | Accessed: 2026-10-13 | Via: web_extract
    - Quote: "Run Claude Code, Codex, and your other agents at full speed in MicroVM environments. Local or cloud. One CLI." ... "Each one gets its own kernel, its own private Docker Engine, and no path back to the host." ... "| Micro | 1 | 2 GB | $0.07 |"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Airlock minimum macOS version | macOS 26 or later | https://airlock.sorrel.systems/ | "For Macs with Apple silicon, running macOS 26 or later." |
| 2 | concurrent macOS virtual machines Apple allows (Airlock session ceiling) | two macOS virtual machines at a time | https://airlock.sorrel.systems/ | "Apple allows two macOS virtual machines at a time, so that's the limit." |
| 3 | Airlock current version (Homebrew cask, seen 2026-10-13) | 1.0.1 (202610130921) | https://github.com/simonmaddox/homebrew-tap | "Airlock 1.0.1 (202610130921)" |
| 4 | E2B Pro plan price | $150 /month | https://e2b.dev/pricing | "pro $150 /month + Usage Costs" |
| 5 | E2B Hobby tier concurrent sandboxes | 20 concurrent sandboxes | https://e2b.dev/pricing | "20 concurrent sandboxes" |
| 6 | Docker Sandboxes cloud Micro sandbox price (1 vCPU, 2 GB) | $0.07 per hour | https://www.docker.com/products/docker-sandboxes/ | "Size Micro, vCPUs 1, GB 2 GB, Per hour $0.07" |

## Analogy candidates
- **Hazmat quarantine airlock**: The agent suits up in a sealed room with a copy of your materials; you watch through the window (the live timeline) and carry only the approved items back through the airlock (the per-file diff). Breaks when: a quarantine room goes silent once sealed, but Airlock's room reports every move as it happens; and unless you cut the phone line, the occupant can still call out to public hosts.
- **Rental car with a dashcam**: The agent drives a rental (a copy of the project) while your own car stays parked at home; the dashcam (watching from inside the VM) shows every place it actually went, and you decide what comes back inside it. Breaks when: a rental protects the car, not the places it drives to; network destinations stay reachable unless you lock the session to a host list.

## Misconceptions
- Myth: The allow prompts keep an agent contained. Reality: Prompts only ever see the command the agent typed, not what a build script it launches goes on to do, and by the fortieth one you are clicking yes without reading (claim 3).
- Myth: If the agent is sandboxed, whatever it does inside is harmless. Reality: Sessions can still reach public hosts unless you lock them down, so anything in the copied project could be sent somewhere, and model requests still go to Anthropic or OpenAI (claim 8).
- Myth: Sandboxing an agent means putting it in a Docker container. Reality: A container shares your machine's kernel; Docker's own sandbox product is a microVM with its own kernel and no path back to the host (claim 10).

## Glossary
- **sandbox**: A fenced-off corner of your computer where a program can work without being able to touch anything outside the fence.
- **virtual machine (VM)**: A complete pretend computer running inside your real one, with its own operating system.
- **kernel**: The core program of an operating system that decides what every other program is allowed to touch.
- **microVM**: A stripped-down virtual machine that starts in seconds and exists to be thrown away.
- **Seatbelt**: The sandboxing machinery built into macOS; App Store apps run under it.
- **bubblewrap**: A Linux tool that walls one process off from the rest of the system.
- **diff**: A before-and-after view of a file showing exactly which lines were added or removed.
- **git hook**: A script that runs automatically at git moments such as commit, on your machine.
- **approval prompt**: The allow-or-deny question an agent shows before running a command it considers risky.
- **prompt fatigue**: The numbness that sets in after dozens of approval prompts, where you click allow without reading.

## Unverified
- The creator's design write-up on simonmaddox.com returned Access Denied when fetched, so its contents could not be read this session.
- Community reception beyond the two Hacker News comments could not be sampled: Reddit JSON returned 403 on this box and a surfaced Reddit showcase thread was not fetchable.
- Whether Apple will accept Airlock into the Mac App Store is unknown; the site says Coming soon to the Mac App Store and the creator says he hopes Apple approves it.
- How much overhead an Airlock virtual machine adds to agent run time on a given Mac is unmeasured; the site only says it starts in seconds.

## Suggested outline
1. Hook: your agent ran a command you approved -- and a script you never saw did the real work; by the fortieth allow-click, nobody reads.
2. The move: one brew command puts Claude Code or Codex in a virtual machine on a copy of your project, watched from inside the VM's OS so every process, file and host lands in one live timeline, and you accept changes per file.
3. Honest catch and the field: public hosts stay open unless you lock them, model traffic still leaves for Anthropic or OpenAI, Apple allows two macOS VMs at a time -- and Docker Sandboxes, built-in Seatbelt or bubblewrap sandboxes, or E2B's cloud tier cover the viewer without a Mac.

## Viewer situation
You've got a Mac (or you're watching from a gaming PC) and you let Claude Code or Codex loose in your terminal, clicking allow every time it asks and hoping nothing wanders outside the project folder.

## Has process
true
Install Airlock on your Apple-silicon Mac with brew install --cask simonmaddox/tap/airlock, or download the DMG.
Open your project folder in the terminal and run airlock run claude or airlock run codex.
Let the agent work in the virtual machine on its copy of the project, without approving individual prompts.
Watch the timeline for every process it ran, every file it touched, and every server it talked to.
Review the per-file diff when it finishes and tick only the changes you want applied to your real project.

## Objection
A virtual machine is a wall around the agent, not a filter on it: unless you lock down hosts, the copy of your project can still be sent to public servers, model traffic still goes to Anthropic or OpenAI, applied code still needs reading, and Apple caps you at two macOS VMs at a time.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://airlock.sorrel.systems/ | Airlock: coding agents, kept contained | primary | web_extract | 2026-10-13 |
| 2 | https://news.ycombinator.com/item?id=50054620 | Show HN: I built Airlock, to sandbox your AI agent and know what it's doing | community | web_extract | 2026-10-13 |
| 3 | https://github.com/simonmaddox | simonmaddox (Simon Maddox) - GitHub | primary | web_extract | 2026-10-13 |
| 4 | https://github.com/simonmaddox/homebrew-tap | GitHub - simonmaddox/homebrew-tap | primary | web_extract | 2026-10-13 |
| 5 | https://code.claude.com/docs/en/sandboxing | Configure the sandboxed Bash tool - Claude Code Docs | docs | web_extract | 2026-10-13 |
| 6 | https://learn.chatgpt.com/docs/sandboxing | Sandbox - ChatGPT Learn (Codex) | docs | web_extract | 2026-10-13 |
| 7 | https://www.docker.com/products/docker-sandboxes/ | Docker Sandboxes - Sandboxes for Coding Agents - Docker | primary | web_extract | 2026-10-13 |
| 8 | https://e2b.dev/pricing | Pricing - E2B, The AI Agent Cloud | primary | web_extract | 2026-10-13 |
| 9 | https://binds.ch/blog/scode-sandbox-for-ai-coding-tools | scode: A Seatbelt for AI Coding - Laurent Bindschaedler | community | web_extract | 2026-10-13 |

## Notes
Freshness: the Show HN thread was 15 hours old at fetch with 3 points and 2 comments, and the Homebrew tap carries Airlock 1.0.1 (202610130921) committed the same day -- this is a day-one project, so expect rough edges and fast change; the tap repo shows 0 stars, 0 watching, 0 forks. Vendor framing: Docker's product page carries a comparison table calling E2B, Daytona, Modal and Cloudflare cloud-only; treat competitor rows as marketing -- E2B's own pricing page was fetched and agrees it sells cloud sandbox tiers (Hobby free with $100 of usage credits, Pro $150 /month). scode (binds.ch, tier 4) is an independent single-script Seatbelt and bubblewrap wrapper by an EPFL researcher, evidence the problem is widely felt; its numbers were not used. The OpenAI Codex sandbox docs page corroborates that Codex also ships a Seatbelt-based sandbox on macOS and frames sandboxes as the cure for approval fatigue. Fetch blockers this session: FireCrawl 402 and Reddit JSON 403.
