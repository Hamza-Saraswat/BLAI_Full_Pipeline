---
slug: 2026-11-08-aivim-a-vim-ai-editor-running
format: classic
structure: worked-example
style_pack: sketch
value_types: TEACHES,EQUIPS
promise: After this Short you can point AIVim at the Ollama server already on your machine and turn a plain-English instruction into reviewed Bash tonight.
target_duration_s: 39
brief: 2026-11-08-aivim-a-vim-ai-editor-running-brief.md
drafts: 2026-11-08-aivim-a-vim-ai-editor-running-drafts.md
---

# AIVim: Plug Your Editor Into Ollama

## Decisions
- Structures tried: worked-example (A) vs news-react-so-what (B). A won 21-18: dependency-ordered turns each naming what changed, numbers spent where they land, payoff line quotable and last. B's news shape restated its own hook at beat two and put its repeatable line at second ten.
- Hook: candidate 1 (Situation pattern, assigned to A) over candidate 2 (Named contradiction, assigned to B). Names the viewer's idle asset (Ollama already running) and the tension inside five words.
- No grafts: B's hook was not two points better, and its two candidate lines would break A's word budget and force a close rewrite.
- Gates: validator 0 blockers 0 advisories; eval all gates pass (advisory only: entity_spend 0.188); sameness ok, 5 comparisons, 0 violations; style pack sketch (LRU; previous was signal).
- est_duration_s = words/2.9 throughout; scene narrations concatenate exactly to narration_full.

## Hook candidates
1. * Your Ollama models are already running. This editor finally uses them. (Situation; A)
2. AIVim just shipped: a Vim-style editor running your Ollama model. (Named contradiction; B)
3. One URL, and your Ollama model edits code with you. (Number-ish; payoff word early, but no product tension)
4. Three moves tonight: a Vim editor that thinks with your model. (Tonight; overlaps 11-06's hook pattern)
5. Zero stars. One maintainer. Your editor still runs local AI tonight. (Number shock; spends Unverified numbers, unsafe)
6. Vim keys, local model, no cloud account. AIVim just shipped. (Named contradiction; flat rhythm, no tension)
7. Your editor's AI brain is already installed. It's called Ollama. (Wrong diagnosis shape; cute but buries the product)
8. Fifty kilobytes of context, and the model never leaves your machine. (Number shock; number needs setup before it means anything)
9. localhost 11434 is the only account this AI editor needs. (Named contradiction; reads as a claim, not a hook)
10. Stop pasting code into a chat tab. Edit with the model instead. (Situation; imperative, viewer-action before the product lands)

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Your Ollama models are already running. This editor finally uses them. | Your Ollama is running \| This editor uses it | Frame 1 fully legible: chalk hook line centered on dark slate, small wobbly server-rack sketch below with one amber LED dot blinking within 0.5 s. On the narration phrase "This editor finally uses them" the second text line rises in place beneath and a hand-drawn arrow draws from it toward the rack. Motion onset at 0.30 s, one element at a time. | hyperframes | centered-stack | 3.8 |
| s02 | explain | Tonight you install AIVim, a terminal editor with Vim motions. It wants Python three point nine or newer. | pipx install aivim \| Python 3.9+ | Split-compare. Left pane: the command "pipx install aivim" types itself keystroke by keystroke, anchored to "Tonight you install AIVim". Right pane: a chalk terminal window rises in place titled aivim with the letters h j k l circled, anchored to "your Vim motions"; the 3.9+ badge draws on "Python three point nine or newer". Fade and rise-in-place only, sequenced. | hyperframes | split-compare | 6.2 |
| s03 | explain | aivim --connect points it at localhost, port eleven four three four, the plug every AI tool speaks. The editor now knows where the model lives. | aivim --connect -> localhost:11434/v1 | Diagram-flow. Two hand-drawn boxes labeled aivim and Ollama, present from 0.30 s. On "points it at localhost" a wobbly chalk arrow draws from editor to server. On "port eleven four three four" the label localhost:11434/v1 fades in on the wire. On "The editor now knows where the model lives" a chalk circle closes around the whole link. One animation at a time. | manim | diagram-flow | 8.6 |
| s04 | explain | Open a file in AIVim, type list the biggest logs here, then a blank line. Bash streams in while you keep typing. | list the biggest logs here \| ls -S *.log | Split-compare. Top half: the instruction "list the biggest logs here" types in with a blank chalk line drawn under it, anchored to "then a blank line". Bottom half: the Bash "ls -S *.log" streams token by token into the buffer, anchored to "Bash streams in", while the top cursor keeps blinking for "while you keep typing". Exactly two elements animate. | hyperframes | split-compare | 7.6 |
| s05 | explain | Requests carry up to fifty kilobytes of your file. The reply gets checked, not run; you review before it stays. | 50 KiB context \| checked not run | Centered-stack checklist on slate. On "fifty kilobytes of your file" a chalk tag reading 50 KiB fades in beside a file sketch. On "gets checked, not run" a check mark draws beside checked and a cross beside not run, in amber. On "you review before it stays" a wobbly circle closes around you review. Sequenced draw-on reveals, never more than two moving. | hyperframes | centered-stack | 6.9 |
| s06 | payoff_close | AIVim is a Vim subset, days old. But editor, model, the whole conversation stays on your machine. | editor + model + conversation \| on your machine | Diagram-flow payoff. On "a Vim subset" a small plain chalk caption fades in at the corner, unadorned. On "editor, model" two chalk circles rise in place inside one big hand-drawn machine outline, joined by a wobbly double arrow. On "stays on your machine" a crossed-out cloud sketch draws outside the box and the frame holds still for the wordmark settle. | manim | diagram-flow | 5.9 |

## Notes for review
- The port is spoken as "eleven four three four" and shown as digits 11434 in the same scene (s03); verified against Ollama docs claim 5.
- 50 KiB is the verbatim per-request context budget (claim-sourced); spoken "fifty kilobytes" per Hard Constraint 4.
- The honest catch is in the payoff scene itself: subset, days old. Adoption numbers stay out of narration (Unverified in the brief).
- est sums 39 s, at the top of the classic sweet band; if voice runs long, s03 is the trim candidate.
