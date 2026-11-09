# Drafts: 2026-11-09-open-webui-v0-13-3-agents-in-a

## Draft A (how-to-three-moves, hook "Three moves and your coding agent runs on a schedule tonight.")

s: s01 Three moves and your coding agent runs on a schedule tonight. Right now, every agent run you have seen started because you sat down and typed.
s: s02 In chat, the model suggests a fix, and the fix dies in the window. Open WebUI, the self-hosted interface in front of your models, just gave the chat hands. A terminal is a real shell and folder on a machine it can reach, so the model edits files itself. But every tool call still waits for you to click Allow.
s: s03 Step one: connect a terminal under Admin settings. Open Settings, Admin, Integrations, hit the plus in the Open Terminal section, paste the local address and your key. On your own laptop, the Tether desktop app does the same with one sign in.
s: s04 Step two: build the automation around one folder. An automation is a saved prompt with a clock, run by the server whether or not your browser is open. Yesterday's release put agent selection in this editor. You pick the terminal and the working folder, the one directory it may touch.
s: s05 Then you pick a coding agent, a tool like Claude Code, Codex or Pi that edits code itself. Each scheduled run first checks that the terminal and the agent are still available.
s: s06 Step three: set the schedule and press Run now. Choose Daily at nine in the morning, in your own timezone. Write instructions with edges: run the test suite, change no files, report the failing test with its error. Then click Run now once, and read the chat it creates before trusting the clock.
s: s07 That run leaves a real chat in your sidebar, with the full task activity inside. The task also keeps a run history, each line marked success or error, with the error text.
s: s08 Here is the catch. Unattended runs execute with full tool approval, because nobody is there to click Allow. Treat it as a cron job with hands, except cron cannot wander off the script. So the first folder is a throwaway, and the prompt says exactly what not to touch.
s: s09 Once that manual run reads clean, leave the schedule enabled. Tomorrow at nine it runs without you, and the failing test is already waiting in its chat.

## Draft B (news-react-so-what, hook "Open WebUI just handed your coding agent a calendar.")

s: s01 Open WebUI, the self-hosted interface in front of your models, just handed your coding agent a calendar. That is an AI that edits code in a folder by itself. While you sleep, it can run your test suite, change nothing, and report what failed.
s: s02 Yesterday's release notes say it plainly: scheduled prompts can now run coding agents. GitHub shows about one hundred fifty eight thousand stars on the project. All week, the changelog has been turning chat prompts into clock-driven errands.
s: s03 Open WebUI calls that an automation: a saved prompt with a clock on it. The server fires it whether your browser is open or closed. Until now, every agent run started because you sat there typing. Now the run starts itself.
s: s04 You know the old loop: the fix appears in a chat window and dies there. A terminal, one connected workspace with a real folder, lets the agent read and write files. But every tool call waited for your Allow click, with you as full-time bouncer.
s: s05 So what did yesterday actually add? The automation editor now saves the terminal, the working folder and the agent alongside the schedule. On a terminal that offers them, the picker lists Claude Code, Codex and Pi. Before firing, it checks that the terminal and agent are still available. Results land as a real chat, plus a run history marked success or error.
s: s06 Now the honest catch. Unattended runs execute with full tool approval; nobody is there to click Allow. A scheduled prompt is also a thin spec. Treat it like a night-shift junior developer: it only knows what the ticket and the folder say. The docs' own answer: a throwaway folder, and a prompt that says what not to touch. Keep the first errand read-only, just like that test run.
s: s07 Tonight, the setup is short. Connect a terminal under Settings, Admin, Integrations. Or install Tether, the desktop app that ties in your own machine, no ports to open. Create an automation, pick the terminal, the folder and the agent. Set it to daily, hit Run now once, and read the chat it creates. Leave it enabled only when the output is something you can judge in seconds.
s: s08 Do that tonight and tomorrow starts differently. The calendar fires, the agent works, and the failing test is already waiting in a chat.

## Judge scores (rubric rows 1-8, max 3 each)

| Row | A (how-to-three-moves) | B (news-react-so-what) |
|-----|----|----|
| 1 Hook | 2 | 2 |
| 2 Payoff timing | 1 | 2 |
| 3 Specificity | 3 | 2 |
| 4 Voice | 3 | 2 |
| 5 Navigation | 2 | 2 |
| 6 Difference | 2 | 3 |
| 7 Repeat test | 2 | 3 |
| 8 Teaching | 2 | 3 |
| **Total** | **17** | **19** |

Winner: B, 19 to 17. B's payoff line lands as the last thing heard and it is the repeatable one; A parked its best line mid-script and opened on restated pain.

Grafts: "the self-hosted interface in front of your models" from A s01 into B s01 (B named Open WebUI with no plain definition; the appositive repairs it in six words without touching person, structure, or number budget).

What the losing shape needed: step one's substance inside the opening breath instead of fifteen seconds of restated pain, and the "cron job with hands" line moved into the payoff instead of mid-script. It also matched 2026-11-06's structure and hook pattern (how-to-three-moves + tonight), which capped row 6 at 2.
