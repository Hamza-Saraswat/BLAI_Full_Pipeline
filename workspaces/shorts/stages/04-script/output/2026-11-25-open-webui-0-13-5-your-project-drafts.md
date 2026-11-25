# Drafts: 2026-11-25-open-webui-0-13-5-your-project

Two blind writers on kimi-k3, separate processes, separate scratch directories; neither saw the other. Judge: kimi-k3, rubric as system, both storyboards as user.

## Draft A (how-to-three-moves, Situation hook) -- WINNER
Working title: Open WebUI 0.13.5: Your Project Beside Your Chat
Hook text: Your model and your project, apart
| s01 | hook | Your model lives in Open WebUI, and your project lives on disk. The chat cannot see your project. Every code question is a copy-paste round trip between browser and editor. | 10.3 |
| s02 | explain | Open WebUI zero point thirteen point five changes what a folder is. It becomes a folder workspace, a sidebar folder tied to a computer and a project directory you pick once. | 10.7 |
| s03 | explain | Move one: connect the machine. A machine is an Open Terminal connection, a self-hosted computer where the model runs commands. You start it with a single Docker command and leave it running. The default image takes about four gigabytes of disk. The slim and alpine images skip the desktop, and the desktop is the point. | 19.0 |
| s04 | explain | Move two: set the folder's machine and directory. Create a folder in the sidebar and open its settings. Pick the Machine and the Working directory, your project folder on disk. New chats inside inherit its model, machine, directory, system prompt and knowledge. | 14.5 |
| s05 | explain | Move three: give the model a job. Tell it that a test fails in the date parser folder: fix it and run the tests. The fix lands in the Files tab while the tests run in the terminal. Your app opens in the Browser tab, and the chat stays open beside it. | 17.9 |
| s06 | explain | Nothing here is free rein. The machine is a container you started, and the directory was picked once. Ask for approval, a per-chat mode, makes every tool call wait for your click. | 11.0 |
| s07 | explain | The honest catch: these are browser tabs over a container, not an I D E. But the model picker lists thirteen coding agents, including Cursor and GitHub Copilot. The agent moves inside your self-hosted setup instead of living in the editor. | 14.1 |
| s08 | foreshadow | An A G E N T S dot M D, a project instructions file, sits in the project folder. Every new chat there reads it before answering. Reopen the folder tomorrow and your chats, files and terminals are where you left them. | 14.5 |
| s09 | payoff_close | In Open WebUI, your project's tests and your app run live beside the chat. The copy-paste round trip is done. | 6.9 |

## Draft B (news-react-so-what, Named contradiction hook)
Working title: Open WebUI 0.13.5: Your Chat Just Grew a Terminal
Hook text: Your chat grew a terminal
| s01 | hook | Your Open WebUI chat just grew a terminal and a browser. You run local models through oh-lah-mah, your model server, and your project sits on disk. Every code question means copy-pasting snippets between the browser chat and your editor. | 13.4 |
| s02 | explain | This morning's release is version zero point thirteen point five. It adds folder workspaces, sidebar folders with a machine and a project directory chosen once. The consequence: your tests, terminal, and browser now sit beside the chat, working in that folder. So much for tidy chat drawers. | 16.2 |
| s03 | explain | Give the folder workspace a job: fix the failing test in the date parser. The model edits the code, runs the tests in the terminal tab, and shows the app in the Browser tab. You watch each diff, a before-and-after view, land in the Git panel while the chat stays open. | 17.6 |
| s04 | explain | Every new chat there starts with the folder's model, machine, and instructions already loaded. Thirteen coding agents sit in the model picker, including Cursor and GitHub Copilot. The agent moves inside your self-hosted interface, running on your hardware, instead of the chat living inside an editor. | 15.9 |
| s05 | explain | The catch: the machine is a container, an isolated computer you start yourself, about four gigabytes of disk. It is a browser pane over that container, not an I D E. Upgrading converts your existing chat database, so back up first. | 14.1 |
| s06 | explain | Nothing gets free rein: you picked that machine and directory once. Ask for approval, a mode where every tool call waits for your click. A G E N T S dot M D, a project instructions file, is read by every new chat. | 14.8 |
| s07 | foreshadow | Tonight: connect a machine, create the folder, set its Machine and working directory, then hand the model a job. | 6.6 |
| s08 | payoff_close | Tonight, your project sits beside your chat. The copy-paste round trip is done. | 4.5 |

## Judge score table

| Row | A | B |
|-----|---|---|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 1 | 3 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 2 | 2 |
| 6 Difference | 3 | 0 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 2 | 2 |
| Total | 20 | 18 |

## Winner and grafts
Winner: A, 20 to 18. Grafts: none.

## Judge verdict (verbatim)
ROW_SCORES:
A: 3 1 3 3 2 3 3 2 total 20
B: 2 3 3 3 2 0 3 2 total 18
WINNER: A
GRAFTS: none
LOSER_NEEDS: B's named-contradiction hook repeated the exact hook pattern from 2026-11-24 and its "grew a terminal" phrasing echoed the 2026-11-20 closing, so the shape needed a hook pattern and wording with no fingerprint in the recent ledger. It also needed its lead line to be a pain the viewer feels rather than a curiosity, since the copy-paste ache is present only as a subordinate screen line while the headline spends itself on surprise.
NOTES: Payoff timing evidence: A's 30-word problem tableau runs about 10.3 s at 2.9 wps, so the folder-workspace answer lands around second 12-14, while B names the terminal and browser by word 11, roughly second 4. The table hides duration: A estimates 118.9 s against a 95 s target (B is 103.1 s), so A wins on structure but needs a real trim before recording. Both drafts end on the identical line "The copy-paste round trip is done," which is why row 7 cannot separate them, and B's "upgrading converts your existing chat database" is a hard assertion worth re-checking against the brief.

## What the loser would have needed
See the judge's LOSER_NEEDS above: B's named-contradiction hook repeated 2026-11-24's pattern and its phrasing echoed 2026-11-20's closing; its lead line needed to be the viewer's pain rather than curiosity.

## Post-judge fixes to the winner
- Hook text changed from "Your chat can't see your project" to "Your model and your project, apart" after the sameness gate flagged the named-contradiction repeat; the hook scene's narration now opens on the situation and the wall lands in sentence two.
- Trimmed from 345 words (118.9 s est) to 285 words (98.3 s est) per the judge's duration note; s08 folded into s07 and the close.
- s07 split into two scenes (18.3 s was over the 16 s smooth advisory), payoff scene rebuilt as a grid to avoid repeating the adjacent archetype.
- scene_specificity fix: s05 named "date parser folder" (glossary term), s09 named "Open WebUI".
