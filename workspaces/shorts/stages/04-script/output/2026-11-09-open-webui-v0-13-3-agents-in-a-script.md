---
slug: 2026-11-09-open-webui-v0-13-3-agents-in-a
format: smooth-explainer
structure: news-react-so-what
style_pack: terminal
value_types: TEACHES,EQUIPS
promise: name what shipped in Open WebUI v0.13.3 and wire one safe first automation tonight, knowing the one risk to check first
target_duration_s: 133.0
brief: 2026-11-09-open-webui-v0-13-3-agents-in-a-brief.md
drafts: 2026-11-09-open-webui-v0-13-3-agents-in-a-drafts.md
---

# Open WebUI v0.13.3: Your Coding Agent Now Runs on a Schedule

## Decisions
- Structures tried: news-react-so-what (draft B, winner, judge 19/24) and how-to-three-moves (draft A, 17/24). Both cleared rotation against the last two (myth-bust, worked-example).
- Hook: pick 2 "Open WebUI just handed your coding agent a calendar." (situation pattern, 7/7 on the hook-library score; runner "automations now run agents in the folder you pick" lost the tie on repeat-out-loud).
- Graft from A: the appositive "the self-hosted interface in front of your models" into s01; B's hook named Open WebUI without a plain definition. No other text moved.
- Gates: validator 0 blockers; eval all-pass (number_spend, hook_concrete, scene_specificity, skeleton, positional_labels, sameness, validator); variety check ok (5 comparisons, 0 violations); normalizer scenes_changed 0.
- Judge note: A's shape spent its first fifteen seconds restating the pain; its repeatable line sat mid-script. Kept for the record, not grafted.

## Hook candidates
1. Three moves and your coding agent runs on a schedule tonight.
2. Open WebUI just handed your coding agent a calendar. *
3. Your coding agent now runs while you sleep. Here is the setup.
4. One hundred fifty-eight thousand stars, and today it got a clock.
5. v0.13.3: automations now pick the terminal, folder, and agent.
6. You typed every agent run you ever made. Not anymore.
7. A scheduled automation can now drive a coding agent in your project folder.
8. Your agent waits for you to type. Give it a calendar instead.
9. Open WebUI v0.13.3 turns agents into night-shift workers.
10. Unattended agent errands, three settings, zero new servers.

## Script

| s01 | hook | Open WebUI, the self-hosted interface in front of your models, just handed your coding agent a calendar. That is an AI that edits code in a folder by itself. While you sleep, it can run your test suite, change nothing, and report what failed. | your coding agent gets a calendar | Frame 1: a sharp-cornered terminal window centered on black, holding one monospace line "your coding agent gets a calendar" with a block cursor. Motion onset 0.35 s: on "a calendar" the cursor types a second line "schedule: daily". On "edits code in a folder by itself" a folder glyph with file icons appears inside the window. On "change nothing" a line hard-prints "files changed: 0". On "report what failed" a red FAIL row prints, hard cut, no fade. | hyperframes | centered-stack | 15.2 |
| s02 | explain | Yesterday's release notes say it plainly: scheduled prompts can now run coding agents. GitHub shows about one hundred fifty eight thousand stars on the project. All week, the changelog has been turning chat prompts into clock-driven errands. | v0.13.3 · 2026-11-08 · 158.2k stars | A monospace timeline across a black field with square tick marks. First motion at 0.40 s. On "Yesterday's release notes" the right tick types "v0.13.3 2026-11-08". On "one hundred fifty eight thousand stars" a counter under the tick hard-sets to "158.2k stars". On "clock-driven errands" three small square clock glyphs type in along the line, left to right, then hold. | hyperframes | timeline | 12.8 |
| s03 | explain | Open WebUI calls that an automation: a saved prompt with a clock on it. The server fires it whether your browser is open or closed. Until now, every agent run started because you sat there typing. Now the run starts itself. | same prompt, now with a clock | Split screen with a hard vertical divider, no rounded corners. First motion at 0.40 s. On "a saved prompt with a clock on it" the same typed prompt appears in both panes, and the right pane gains a square clock glyph. On "whether your browser is open or closed" the left browser frame cuts to black while the right prints "run started". On "you sat there typing" the left cursor blinks idle. On "starts itself" the right pane types new chat lines with no cursor present. | hyperframes | split-compare | 14.1 |
| s04 | explain | You know the old loop: the fix appears in a chat window and dies there. A terminal, one connected workspace with a real folder, lets the agent read and write files. But every tool call waited for your Allow click, with you as full-time bouncer. | chat talks; a terminal touches files | Manim diagram, monospace labels, square-cornered boxes on black. First motion at 0.40 s. On "the fix appears in a chat window" a box labeled CHAT fills with text lines, then greys out on "dies there". On "one connected workspace with a real folder" a TERMINAL box appears with a folder node, and straight arrows draw from CHAT to TERMINAL to the folder on "read and write files". On "Allow click" a small ALLOW button flashes between the boxes; on "full-time bouncer" it turns into a barrier glyph. | manim | diagram-flow | 15.5 |
| s05 | explain | So what did yesterday actually add? The automation editor now saves the terminal, the working folder and the agent alongside the schedule. On a terminal that offers them, the picker lists Claude Code, Codex and Pi. Before firing, it checks that the terminal and agent are still available. Results land as a real chat, plus a run history marked success or error. | terminal + folder + agent, saved with schedule | A grid of four sharp-cornered tiles: TERMINAL, FOLDER, AGENT, SCHEDULE. First motion at 0.40 s. On "saves the terminal, the working folder and the agent" the first three tiles highlight in sequence and straight lines pull them into SCHEDULE. On "Claude Code, Codex and Pi" the AGENT tile types the three names as rows. On "checks that the terminal and agent are still available" a preflight line types "terminal: ok" then "agent: ok". On "success or error" a run-history list prints two rows tagged SUCCESS and ERROR. | hyperframes | grid | 21.4 |
| s06 | explain | Now the honest catch. Unattended runs execute with full tool approval; nobody is there to click Allow. A scheduled prompt is also a thin spec. Treat it like a night-shift junior developer: it only knows what the ticket and the folder say. The docs' own answer: a throwaway folder, and a prompt that says what not to touch. Keep the first errand read-only, just like that test run. | full tool approval, nobody clicks Allow | One centered sharp-cornered terminal window. First motion at 0.40 s. On "full tool approval" the window types "approval: FULL" and the ALLOW button from the earlier scene appears greyed with a straight strike. On "thin spec" a one-line prompt sits beside a tall file tree. On "night-shift junior developer" a card types "ticket in, code out, nothing carried overnight". On "a throwaway folder" a line types "workspace: /tmp/scratch". On "what not to touch" the prompt appends "DO NOT TOUCH src/". On "read-only" it appends "run tests, change nothing". | hyperframes | centered-stack | 23.4 |
| s07 | explain | Tonight, the setup is short. Connect a terminal under Settings, Admin, Integrations. Or install Tether, the desktop app that ties in your own machine, no ports to open. Create an automation, pick the terminal, the folder and the agent. Set it to daily, hit Run now once, and read the chat it creates. Leave it enabled only when the output is something you can judge in seconds. | connect, create, run now, read the chat | A vertical flow of four square nodes joined by straight lines, typewriter labels. First motion at 0.40 s. On "Connect a terminal" the node types "Settings > Admin > Integrations" and the URL "http://localhost:\" breaks to "8000" with a backslash. On "install Tether" a side tag prints "or: Tether app -- no ports". On "Create an automation" the node types "User Menu > Automations > New". On "daily, hit Run now" the next node types "Daily 09:00" beside a RUN NOW keycap. On "read the chat it creates" the last node shows a transcript line "FAIL: test_login". | hyperframes | diagram-flow | 23.1 |
| s08 | payoff_close | Do that tonight and tomorrow starts differently. The calendar fires, the agent works, and the failing test is already waiting in a chat. | tomorrow, the failure is already named | A centered sharp-cornered terminal window on black, opening on a square clock glyph reading 09:00. First motion at 0.45 s: on "The calendar fires" the clock hand snaps and a fresh chat types line by line, "ran test suite", "changed no files", "1 failing test -- error output attached". On "already waiting in a chat" the typing stops and the block cursor blinks twice, then the frame holds static for the outro. No fade. | hyperframes | centered-stack | 7.9 |

## Notes for review
- The 158.2k stars number: spoken as "about a hundred and fifty-eight thousand stars", unit and referent kept, rounded once for the ear.
- The honest catch (unattended agent, full tool approval, nobody clicks Allow) lands in s06 with the docs' own answer: run it once manually, keep the first task read-only.
- Analogy limit stated in one clause in s05 (cron runs a fixed command; an agent decides, so it can surprise you).
- s06 is the longest scene at about twenty-three seconds with three visual beats; flagged by the long-scene advisory, kept because the beat is the honest catch and splitting it would orphan the docs' answer.
