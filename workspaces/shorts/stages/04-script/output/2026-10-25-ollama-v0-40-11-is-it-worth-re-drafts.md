# Drafts: 2026-10-25-ollama-v0-40-11-is-it-worth-re

Two blind drafts on kimi-k3, one packet each, private scratch dirs. Both passed the machine
gates before judging (validate_storyboard 0 blockers; eval_short exit 0).

## Draft A (news-react-so-what, hook: decision)

| Scene | Narration |
|-------|-----------|
| s01 | Should you update Ollama tonight? Nothing re-downloads. Your models stay safe on disk. |
| s02 | Updates swap the app, nothing else. One click. Your pulls sit in a folder it never touches. New player, same songs. |
| s03 | What's new: speech on macOS, replies read aloud. That's phonon, a speech model. It turns text into audio, and the whole feature is a hundred and thirteen megabytes on disk. |
| s04 | Meet d3, a decision model that scores options instead of chatting. The smallest is two billion parameters. It pulls about three gigabytes on disk. |
| s05 | The catch: zero point forty point two rewrote old models once, backups kept. Updates never re-pull. A downgrade can. |
| s06 | Update always, re-pull never, and pull new only when a feature names a model. |

("One click." grafted from B after judging; A's original s02 read "Updates swap the app,
nothing else. Your pulls sit in a folder it never touches. New player, same songs.")

## Draft B (how-to-three-moves, hook: tonight)

| Scene | Narration |
|-------|-----------|
| s01 | Three moves and Ollama's updated tonight. That update ping in your menubar? It never touches your models. |
| s02 | Move one: click Restart to update in that menubar. One click. Ollama swaps the app, never your model folder. |
| s03 | Move two: pull phonon, the speech model. It reads text aloud. The download is a hundred and thirteen megabytes on disk. |
| s04 | Or pull d3, a decision model. It scores options instead of chatting, about a three gigabyte download. |
| s05 | One catch: Ollama once rewrote old model formats quietly. Backups kept. Safe until the next swap. |
| s06 | Move three: on a Mac, run phonon and hear the reply out loud. App swapped, models untouched, box talking. |

## Judge scores (0-3 per row, max 24)

| Row | A | B |
|-----|---|---|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 3 | 2 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 0 | 2 |
| 5 Navigation | 2 | 2 |
| 6 Difference | 3 | 2 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 3 | 2 |
| **Total** | **20** | **18** |

Winner: A, 20-18. Even with row 4 zeroed (the hook asks a question the viewer cannot answer
from what they own), A wins on hook tension, payoff timing, difference and teaching: it lands
the promised answer by second 2 and closes on the reusable rule "Update always, re-pull never,"
while B's close summarizes instead of handing the viewer a rule they can extend.

Grafts: "One click." from B into A's s02, because it states brief claim 6 (the update is one
click on macOS and Windows) which A never voiced, and it inserts without touching structure,
person or number budget.

What B would have needed to win: first five words carrying the viewer's actual tension (the
feared re-download) instead of a plain ease promise, the first concrete move landing inside
four seconds, and a close that converts the catch into a forward-looking rule rather than a
summary; its number-led opening cadence also echoed the recent number-first run.
