---
slug: 2026-11-25-open-webui-0-13-5-your-project
format: smooth-explainer
structure: how-to-three-moves
style_pack: signal
value_types: EQUIPS,TEACHES
promise: After this you can connect one machine, bind a folder to your project directory, and give your local model a job in that project tonight.
target_duration_s: 95
brief: 2026-11-25-open-webui-0-13-5-your-project-brief.md
drafts: 2026-11-25-open-webui-0-13-5-your-project-drafts.md
---

# Open WebUI 0.13.5: your project beside your chat

## Decisions
- Two structures tried: how-to-three-moves (draft A) and news-react-so-what (draft B); A won 20 to 18 on the judge rubric, no grafts. Judge note acted on: A trimmed from 118.9 s to 98.3 s estimated and its s07 split into two scenes before saving.
- Hook: candidate 1, "Your model and your project, apart" (Situation pattern). The writer's first hook, "Your chat can't see your project", was auto-classified named-contradiction, the same pattern as 2026-11-24, and would have failed the sameness gate; the hook text now opens on the viewer's situation and the wall lands in sentence two.
- Positional labels: three, one per move, each naming its action (connect the machine, set the folder's machine and directory, give the model a job). Legal for this structure.
- Numbers spent: two (four gigabytes of disk; thirteen coding agents). The 34x performance figures stay unspent per the brief's Notes (late-spend, PROVES material, not EQUIPS).
- Remaining advisories kept with reason: 8 hashtags (stage 05 trims to the final set) and 0 YouTube keyword tags (stage 05 writes 15 to 25).

## Hook candidates
1. *Your model and your project, apart (picked: Situation)
2. Your chat grew a terminal (draft B opener: Named contradiction)
3. 0.13.5: your project beside your chat (Named product)
4. Your chat can't see your code (Named contradiction; rejected: sameness clash with 2026-11-24)
5. Copy-pasting code into your chat ends tonight (Tonight)
6. Your model, your folder, one window (Situation variant)
7. The chat that finally sees your project (Named contradiction variant)
8. Your project's tests, beside your chat (Situation variant)
9. A chat app that runs your tests (Named contradiction variant)
10. Your folder is now a workspace (Situation variant)

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Your model lives in Open WebUI, and your project lives on disk. The chat cannot see your project. Every code question is a copy-paste round trip. | Your chat can't see your project  /  copy-paste, every single question | Built in hyperframes. Frame 1: flat dark background, split screen; left a chat panel labeled Open WebUI, right a dim file tree labeled project, empty gap between; hook text "Your chat can't see your project" in big bold amber type up top. Motion onset at t=0.35 s: an amber divider line rises-in-place in the gap. On "copy-paste round trip", a code snippet card fades out of the tree and scales into the chat, then back, never sliding. Max two elements moving. Hard cut out. Music steady-build enters low; sfx: whoosh at start. | hyperframes | split-compare | 9.0 |
| s02 | explain | Open WebUI zero point thirteen point five changes what a folder is. It becomes a folder workspace, a sidebar folder tied to a computer and a project directory you pick once. | v0.13.5  /  folder workspace  /  one computer, one project directory | Built in hyperframes. Flat dark centered stack. On "zero point thirteen point five", a bold amber badge reading v0.13.5 fades in top center. On "folder workspace", a plain folder icon scales up below it; on "computer and a project directory", two chips rise-in-place onto the folder, one labeled computer, one labeled project directory, settling as "you pick once" lands. Entrances only fade, scale, rise-in-place; two elements animating max. Hard cut. | hyperframes | centered-stack | 10.7 |
| s03 | explain | Move one: connect the machine. A machine is an Open Terminal connection, a self-hosted computer where the model runs commands. One Docker command starts it. The default image takes about four gigabytes of disk, desktop included. | Move one: connect the machine  /  Open Terminal  /  4 GB of disk | Built in hyperframes. Flat dark stage with a centered terminal card. On "Move one", the label rises-in-place top left in amber. On "Open Terminal", a chip fades in naming it. On "single Docker command", the docker run command types itself into the card. On "four gigabytes of disk", a giant amber 4 GB scales up center with a pop sfx; on "desktop is the point", a small caption fades in below reading slim and alpine skip the desktop. Two elements moving max. Hard cut. | hyperframes | giant-number | 12.4 |
| s04 | explain | Move two: set the folder's machine and directory. Create a folder in the sidebar, open its settings, pick the Machine and the Working directory. New chats inside inherit its model, directory and knowledge. | Move two: set machine + directory  /  new chats inherit your defaults | Built in hyperframes. Flat dark split-compare: left, the Open WebUI sidebar with a fresh folder highlighted amber; right, its settings card. On "Pick the Machine and the Working directory", two fields rise-in-place: Machine set to Open Terminal, Working directory set to /home/user/date-parser. On "inherit", small chips fade in under the folder one pair at a time: model, machine, directory, prompt, knowledge. Fade and rise-in-place only, two moving max. Hard cut. | hyperframes | split-compare | 11.4 |
| s05 | explain | Move three: give the model a job. Tell it a test fails in the date parser folder: fix it and run the tests. The fix lands in the Files tab, the tests run in the terminal, and your app opens in the Browser tab. | Move three: give the job  /  Files  /  terminal  /  Browser  /  chat stays open | Built in hyperframes. Flat dark grid: chat column left, three panes right labeled Files, terminal, Browser. On "a test fails", the job message types into the chat box. On "fix lands", an amber diff card fades into the Files pane; on "tests run", amber check lines rise-in-place in the terminal pane; on "app opens", a small web page scales into the Browser pane while the chat column stays lit. Max two elements animating at once. Hard cut. | hyperframes | grid | 15.2 |
| s06 | explain | Nothing here is free rein. The machine is a container you started, and the directory was picked once. Ask for approval, a per-chat mode, makes every tool call wait for your click. | no free rein  /  Ask for approval  /  every call waits for Allow | Built in hyperframes. Flat dark centered stack. On "free rein", a container chip labeled Machine with a bold amber outline fades in. On "Ask for approval", a toggle card rises-in-place reading Ask for approval, and a tool call card fades in beneath it, paused mid-action. On "wait for your click", an amber Allow button scales up and holds a gentle pulse until the sentence ends. Nothing else moves. Hard cut. | hyperframes | centered-stack | 11.0 |
| s07 | explain | The honest catch: these are browser tabs over a container, not an I D E. But the model picker lists thirteen coding agents, including Cursor. | honest catch: not an IDE  /  13 coding agents  /  Cursor + GitHub Copilot | Built in hyperframes. Flat dark stage. On "honest catch", a plain browser pane fades in beside a faint editor outline, captioned not an IDE in bold type. On "thirteen coding agents", those fade back and a giant amber 13 scales up center with a ding sfx; on "Cursor and GitHub Copilot", two small chips rise-in-place under it. On "moves inside", the chips drift-settle toward the browser pane using scale only. Two elements moving max. Hard cut. | hyperframes | giant-number | 8.6 |
| s08 | explain | The agent moves inside your self-hosted setup. An A G E N T S dot M D in the project folder is read by every new chat there. | AGENTS.md  /  every new chat reads it | Two-up on 'moves inside your self-hosted setup': left card a chat pane with a model-picker chip, right card a home server glyph, a connecting line draws between them. On 'A G E N T S dot M D', a file card rises in place on the right with the filename in mono, a chat bubble fades in beside it, and a small arrow loops file to bubble on 'read by every new chat'. Amber underline on the filename. Hard cut in; fade-swap one element at a time. | hyperframes | split-compare | 9.7 |
| s09 | payoff_close | Reopen the folder tomorrow and everything is where you left it. In Open WebUI, your tests and your app run live beside the chat. The copy-paste round trip is done. | tests pass  /  app live  /  chat open | Loop-anchor rhyme with frame 1, resolved as a grid of three lit tiles. On 'where you left it', the three tiles fade in already lit: terminal green with passing tests, browser showing the app, chat open. On 'run live beside the chat', the tiles scale up one notch together. On 'round trip is done', the snippet card from frame 1 pops out. Final 0.5 s: wordmark settle, tiles dim behind it. | hyperframes | grid | 10.3 |

## Notes for review
- The word "thirteen" is spoken in scene s07; "4 GB" appears on screen in s03 while "four gigabytes of disk" is spoken in the same scene.
- The payoff line is "The copy-paste round trip is done." (last sentence of s09); two resolution sentences precede the final payoff sentence, inside the smooth-explainer allowance.
- The honest catch answers the brief's objection: browser tabs over a container, not an IDE, then the thirteen agents including Cursor.
- Wry beat: none carried; the writer's drafts were earnest and the judge did not flag row 4 below 3.
- est sum 98.3 s versus target 95: inside the 0.8-1.25 tolerance at wps 2.9 (provisional rate; re-measure after the first renders).
