---
slug: 2026-09-02-claude-code-went-rogue-and-del
stage: 03-research
topic: "Claude Code deleted 15% of a heritage archive: blast radius and the case for controlling where your agent runs"
depth: standard
generated_at: 2026-09-03T02:40:00Z
sources: 7
hub: "[[videos/2026-09-02-claude-code-went-rogue-and-del]]"
---

# Research brief: Claude Code went rogue and deleted years of work

## Summary
On July 19, 2026, a Claude Code agent (v2.1.204) being used by heritage conservationist Udaya Kumar P L deleted four or five software programmes and original photographs from his computer, about 15% of the records of the Bengaluru Inscriptions 3D Digital Conservation Project, after "a quoting error in an AI-generated command turned the instruction into 'delete everything'"; the agent's own attempt to kill the process was blocked by its safety layer, twice, and the destruction proceeded until he shut the computer down. The project spent a decade scanning inscription stones with commercial 3D scanners that cost more than $25,000 each, and is now spending Rs 15 lakh on backup hardening; the data on the NAS survived, the data on his computer's drive did not. Anthropic's own permissions docs confirm the architecture that makes this possible: shell execution is a first-class tool of the agent, and a "yes, don't ask again" approval saves permanently to the repo. HN commenters split between "backups were the missing control" and "the provider of the instrument bears responsibility", with no response from any human at Anthropic after more than a month. What could not be verified: whether a permission prompt or sandbox setting could have prevented this specific deletion (the report says the agent breached even the sandboxed environment), and the samachardaily's claim of an official forensic investigation, which reads as AI-generated amplification and is quarantined under Unverified. The thesis for a local-AI channel: the failure mode is not model quality, it is blast radius, where the agent runs decides what a quoting error can reach.

## Thesis
The Bengaluru deletion shows the real risk of autonomous coding agents is not intelligence but blast radius: a quoting error became irreversible because the agent with shell access ran where ten years of irreplaceable scans also lived.

## Explanation path
Open on the incident as a story: a conservationist watches for four minutes while an agent deletes a decade of photographs, and the agent's own safety system blocks its attempt to stop itself, twice. Establish what was lost: not code, 3D scans and photographs of stone inscriptions that urbanisation is erasing, collected since 2021 by a project whose scanners cost more than twenty-five thousand dollars each. Then name the mechanism in one breath: the agent runs shell commands as a first-class tool, one quoting error turned a cache-clearing command into delete-everything, and permission rules that say "don't ask again" persist. With the mechanism visible, reframe: the same agent pointed at a fresh container can only damage the container, and the backup that survived here was the one on separate hardware the agent could not reach. Close on the honest catch: local does not mean safe by default, an agent with root on your desk deletes just as thoroughly, and even the report's sandbox did not hold; the control that works is isolation plus backups, which is why the project is buying a second NAS and offsite tape.

## Claims
1. **A Claude Code agent deleted about 15% of the Bengaluru inscriptions project's records on July 19, 2026.**
   - Source: When Claude Code went rogue, years of Bengaluru heritage work disappeared, https://www.deccanherald.com/india/karnataka/bengaluru/when-claude-code-went-rogue-years-of-bengaluru-heritage-work-disappeared-4131958
   - Tier: docs | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "On July 19, Claude Code (v2.1.204) wiped out four or five software programmes and some original photographs of Bengaluru's inscriptions, hero stones, temples and coins, collected over the past decade. The loss amounted to 15% of the records"
2. **A quoting error in an AI-generated command turned the instruction into "delete everything", and the safety layer blocked the agent's own kill attempts twice.**
   - Source: same Deccan Herald report, quoting Udaya Kumar P L's posts on X
   - Tier: docs | Confidence: high | Accessed: 2026-03-09 | Via: web_fetch
   - Quote: "a quoting error in an AI-generated command turned the instruction into 'delete everything'" and "When it understood and tried to kill the process, its safety system blocked the kill. Twice… The safety layer permitted the destruction"
3. **The project is spending Rs 15 lakh on backups; NAS data survived, the computer's drive did not.**
   - Source: same Deccan Herald report
   - Tier: docs | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "The Mythic Society, which launched the project in 2021, is now spending Rs 15 lakh to strengthen its backup systems" and "The data backed up on our NAS (Network-Attached Storage) system is safe. The data on my computer's drive was lost."
4. **The inscription scanning uses commercial 3D scanners that cost more than $25,000 each; the project began in 2021 under the Mythic Society.**
   - Source: Stones that tell stories, https://bengaluru.com/stones-that-tell-stories/
   - Tier: community | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "The only way to do this was to use good commercial scanners but these were very expensive costing more than $25,000 each."
5. **Claude Code treats shell execution as an agent tool requiring approval, and a "yes, don't ask again" approval saves permanently to the repository settings.**
   - Source: Configure permissions, Claude Code docs, https://code.claude.com/docs/en/permissions
   - Tier: primary | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Bash commands | Shell execution | Yes, except a built-in set of read-only commands | Permanently per repository and command"
6. **Claude Code is a cloud-agent product: it authenticates to claude.ai accounts and runs across terminal, IDE, web and Slack.**
   - Source: Claude Code by Anthropic, https://www.anthropic.com/claude-code
   - Tier: primary | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Work with Claude directly in your codebase. Build, debug, and ship from your terminal, IDE, Slack, web, and more."
7. **More than a month later, Udaya reports no response from "one human being" at Anthropic or its India head.**
   - Source: same Deccan Herald report
   - - Tier: docs | Confidence: high | Accessed: 2026-09-03 | Via: web_fetch
   - Quote: "Udaya says he has not received a response from even 'one human being' at Anthropic"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Share of project records lost | 15% | https://www.deccanherald.com/india/karnataka/bengaluru/when-claude-code-went-rogue-years-of-bengaluru-heritage-work-disappeared-4131958 | "The loss amounted to 15% of the records" |
| 2 | Duration of the destructive run | four minutes | same | "For four minutes, heritage conservationist Udaya Kumar P L watched an AI agent wreak havoc on his computer." |
| 3 | Agent's kill attempts blocked by its own safety layer | Twice | same | "its safety system blocked the kill. Twice" |
| 4 | Backup hardening spend | Rs 15 lakh | same | "now spending Rs 15 lakh to strengthen its backup systems" |
| 5 | Cost of each 3D scanner | more than $25,000 | https://bengaluru.com/stones-that-tell-stories/ | "costing more than $25,000 each" |
| 6 | Project start year | 2021 | same | "The Mythic Society Bengaluru Inscriptions 3D Digital Conservation Project was started in 2021" |
| 7 | Agent version | v2.1.204 | Deccan Herald | "Claude Code (v2.1.204)" |
| 8 | Collection period of lost photographs | over the past decade | Deccan Herald | "collected over the past decade" |

## Analogy candidates
- **Vehicle**: a forklift in a warehouse. **Mapping**: the agent is the forklift, shell access is the keys, and the working directory is the aisle it shares with ten years of shelved inventory; the Bengaluru failure is a forklift operating in the archive room, and the fix is not a smarter driver but a separate building. **Breaks when**: a forklift cannot write a better instruction for itself mid-crash, while the agent's kill attempt shows it partially could; the picture also undersells that the "don't ask again" switch was already flipped.
- **Vehicle**: the intern with root. **Mapping**: an enthusiastic intern given the server password, one mis-typed command from `rm -rf` at the wrong depth, except the intern works at machine speed and its undo request needs a human. **Breaks when**: an intern can be trained by one incident; a model's behaviour is changed only by its vendor, and the report notes no human at the vendor responded after a month.

## Misconceptions
- Myth: the danger of coding agents is that they get too smart. Reality: this agent was doing routine maintenance, a quoting error in a cache-clearing command did the damage, and its safety layer blocked its own stop attempt; the risk is an ordinary bug with shell access to irreplaceable data. (claims 2, 5)
- Myth: local means safe. Reality: an agent with shell access on your desk deletes just as thoroughly as a cloud one, the surviving copies in Bengaluru lived on separate NAS hardware the agent could not reach, and even the report's sandboxed environment was breached; isolation and backups are the controls, not geography. (claims 3, 5)

## Glossary
- **Claude Code**: Anthropic's agentic coding tool that runs in the terminal, IDE and cloud, and can execute shell commands as part of its work.
- **blast radius**: the set of things a failing system can damage; for an agent, everything its permissions and network can reach.
- **sandbox**: an isolated environment meant to contain a program's effects; here, a boundary the agent reportedly breached.
- **NAS (Network-Attached Storage)**: a separate storage box on the local network; the backup copy the deletion could not touch.
- **quoting error**: a misplaced quote character that changes what a shell treats as the command versus data, turning one command into another.
- **3D scan**: a detailed digital model of a physical object, here stone inscriptions made with commercial scanners.
- **permission rules**: the allow, ask and deny settings that decide what an agent may run without a human's approval.

## Unverified
- Whether a specific permission mode (ask for all shell commands) or a stricter sandbox would have prevented this deletion; the report says the agent breached the sandboxed environment but names no setting.
- Udaya's X posts are quoted by the report but were not fetched directly this session.
- The samachardaily's claims of an official forensic investigation and "urgent investigation by local authorities" could not be traced to any primary source and read as AI-generated amplification of the Deccan Herald piece; do not cite.
- Anthropic's side: no company statement was found; the report says it "could not reach Anthropic for comment".
- What "four or five software programmes" were, and whether any lost photographs exist in lower-resolution copies elsewhere.

## Suggested outline
1. Hook: for four minutes a man watched an AI agent delete a decade of work, and the agent's own safety system blocked its attempt to stop, twice.
2. What was lost and why it is irreplaceable: 15% of the records of a project scanning disappearing inscription stones with scanners that cost more than twenty-five thousand dollars each.
3. The mechanism and the reframe: a quoting error in a shell command, permanent "don't ask again" approvals, and the real control is blast radius, isolation plus backups, the second NAS and offsite tape, not model quality or geography.

## Viewer situation
You let a coding agent run shell commands in the folder where your real work lives, and you have never tested what it can delete.

## Has process
true

## Process steps
- List what your agent can reach: working directory, home folder, mounted NAS, cloud sync.
- Move irreplaceable files to storage the agent cannot write: a separate NAS or an offsite copy.
- Set permission rules to ask before every shell command, and delete any saved "don't ask again" rules.
- Run the agent in a sandbox or container with only the project folder mounted.
- Test the restore path once; a backup untested is a rumor.

## Objection
A skeptical engineer says: this is a backups story wearing an AI costume, the user approved permanent shell access and kept a decade of irreplaceable scans on a workstation drive, and no permission system saves someone from that.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.deccanherald.com/india/karnataka/bengaluru/when-claude-code-went-rogue-years-of-bengaluru-heritage-work-disappeared-4131958 | When Claude Code went rogue, years of Bengaluru heritage work disappeared | docs | web_fetch | 2026-09-03 |
| 2 | https://news.ycombinator.com/item?id=49533216 | When Claude Code went rogue... (Hacker News discussion) | community | web_fetch | 2026-09-03 |
| 3 | https://www.anthropic.com/claude-code | Claude Code by Anthropic | primary | web_fetch | 2026-09-03 |
| 4 | https://code.claude.com/docs/en/permissions | Configure permissions - Claude Code Docs | primary | web_fetch | 2026-09-03 |
| 5 | https://bengaluru.com/stones-that-tell-stories/ | Stones that tell stories - The Mythic Society project | community | web_fetch | 2026-09-03 |
| 6 | https://code.claude.com/docs/en/settings | Claude Code settings - Claude Code Docs | primary | web_fetch | 2026-09-03 |
| 7 | https://thesamachardaily.in/articles/tech/ai-tool-claude-code-erases-15-of-bengaluru-inscription-archive/ | AI tool Claude Code erases 15% of Bengaluru inscription archive | community | web_fetch | 2026-09-03 (quarantined under Unverified) |

## Notes
- Tier note: the Deccan Herald piece is the incident's primary reporting (byline, date, direct quotes); it is graded docs rather than primary because the X posts it quotes were not fetched directly.
- The samachardaily article contradicts the Deccan Herald on material facts (an "urgent investigation by local authorities" and a "forensic audit" appear nowhere in the original) and is not citable; the discrepancy is the reason it is listed in Sources but quarantined in Unverified.
- The local-AI angle must stay honest: this incident is not evidence that cloud agents are unsafe and local ones are safe; it is evidence that blast radius decides outcomes. The script should make that explicit or the comment section will.
