---
slug: 2026-10-25-ollama-v0-40-11-is-it-worth-re
format: classic
structure: news-react-so-what
style_pack: terminal
value_types: TEACHES,EQUIPS
promise: After half a minute you can decide the v0.40.11 ping deserves no re-pull, and the only pull worth tonight is phonon or d3.
target_duration_s: 35
brief: 2026-10-25-ollama-v0-40-11-is-it-worth-re-brief.md
drafts: 2026-10-25-ollama-v0-40-11-is-it-worth-re-drafts.md
---

# Ollama v0.40.11: is it worth re-pulling your models?

## Decisions
- Structures tried: news-react-so-what (draft A, won 20-18) and how-to-three-moves (draft B). A lands the promised answer by second 2 and closes on the reusable rule; the judge kept A's voice row at 0 for the hook question and A still won.
- Hook: decision pattern, "Should you update Ollama? Nothing re-downloads." (candidate 1 of 10); different pattern from the last two ledger hooks (number-shock, named-contradiction).
- Graft from B: "One click." into s02, because it states brief claim 6 (the update is one click on macOS and Windows) which A never voiced.
- Gates: validate_storyboard 0 blockers, 0 warnings; eval_short exit 0, all hard gates pass (number_spend 3 of 2-5, hook_concrete via entity Ollama, scene_specificity 6/6, skeleton clean, positional_labels 0, sameness clean vs 5). Soft advisories kept with reasons: entity_spend 0.23 and top2 missing "v0.40.11" because the version string is unspoken on purpose (Hard Constraint 4: no digit strings in narration; the brief's number set is carried by 113 MB, 2B, 3 GB); validator advisory "digits in narration: '3,'" is the product name d3, which the TTS normalizer passes through verbatim, not a number.
- Voice edit round 1 (mine, not the writers): both blind drafts opened narration with the viewer's situation instead of their assigned hook, the convergence finding 12 warns about; s01 of each draft now leads with the assigned hook, situation named by sentence 2-3.
- Value delivery: TEACHES is s02 ("Updates swap the app, nothing else. One click. Your pulls sit in a folder it never touches."); EQUIPS is s06 ("Update always, re-pull never, and pull new only when a feature names a model.") plus the two named pulls in s03 and s04.

## Hook candidates
1. * Should you update Ollama? Nothing re-downloads. (decision; pick, draft A)
2. Three moves and Ollama's updated tonight. (tonight; pick, draft B)
3. Update pings Ollama. Your models stay put. (situation)
4. One hundred thirteen megabytes buys Ollama speech. (number shock; banned, last-two pattern)
5. Ollama's update never touches your pulled models. (named contradiction; banned, last-two pattern)
6. You run Ollama. The update ping landed. Relax. (situation)
7. New Ollama, same models, zero re-downloads. (named contradiction; banned)
8. v0.40.11 ships speech. Your disk stays calm. (named contradiction; banned)
9. Re-pull after updating Ollama? Don't. (decision)
10. Ollama updated overnight. Nothing vanished. (situation)

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Should you update Ollama tonight? Nothing re-downloads. Your models stay safe on disk. | Should you update Ollama? \| Nothing re-downloads. | Frame 1 (t=0): dark terminal backdrop, amber caret, centered two-line hook 'Should you update Ollama?' in bone white over 'Nothing re-downloads.' in amber, all text 64px or taller inside the 900x1160 safe area, tiny menubar icon top-center with an amber update dot. Motion onset at 0.35 s: the update dot pulses once. On 'Nothing re-downloads', the pulse ring snaps off and the phrase gains an amber underline. On 'Your models stay safe on disk', a row of dim file chips labeled '~/.ollama/models' fades in below the text and holds frozen through the cut. Never more than two elements animating at once. | hyperframes | centered-stack | 4.1 |
| s02 | explain | Updates swap the app, nothing else. One click. Your pulls sit in a folder it never touches. New player, same songs. | APP: swapped \| MODELS: stay put | Split-compare on the same dark terminal: left card labeled 'APP', right card labeled 'MODELS', thin amber vertical divider, no text over 7 characters on the minor side. On 'Updates swap the app', the app glyph inside the left card fades out and a refreshed glyph fades in at the same footprint. On 'Your pulls sit in a folder it never touches', the right card's border lights amber and a write-arrow aimed at it gets a slash drawn through it. On 'New player, same songs', a small music-note glyph pops beside the MODELS card. All motion is fade or scale in place; nothing slides. | hyperframes | split-compare | 6.6 |
| s03 | explain | What's new: speech on macOS, replies read aloud. That's phonon, a speech model. It turns text into audio, and the whole feature is a hundred and thirteen megabytes on disk. | speech: macOS \| phonon: speech model \| 113 MB | Giant-number scene entered by staged swap, never a dissolve. A caption 'speech: macOS' types in on 'What's new'. On 'replies read aloud', amber audio bars rise from a center baseline and keep looping gently. The caption hard-swaps to 'phonon: speech model' on 'That's phonon'. On 'a hundred and thirteen megabytes', '113 MB' scales in as the giant amber number with an emphasis punch, the text pre-sized to SAFE_W/1.12 so the 1.12 scale stays inside safe width, bars still moving beneath it. Only the bars plus one text element animate at any moment. | hyperframes | giant-number | 9.4 |
| s04 | explain | Meet d3, a decision model that scores options instead of chatting. The smallest is two billion parameters. It pulls about three gigabytes on disk. | d3: decision model \| 2B params \| ≈3 GB | Grid scene: one d3 card scales in on 'Meet d3', tagged 'decision model' beneath the name. On 'scores options instead of chatting', three empty option bars appear under the card and fill to uneven widths, no digits anywhere on the bars. On 'The smallest is two billion parameters', a '2B params' chip fades in at the card's corner. On 'It pulls about three gigabytes', a '≈3 GB' badge pops in beside the chip. Bars and badge are the only moving elements; the whole grid sits inside the safe area and nothing enters the caption band. | hyperframes | grid | 7.5 |
| s05 | foreshadow | The catch: zero point forty point two rewrote old models once, backups kept. Updates never re-pull. A downgrade can. | v0.40.2 \| backups kept \| downgrades re-pull | Timeline: a thin horizontal amber line with two nodes, 'v0.40.2' on the left and 'today' on the right. On 'zero point forty point two', the left node lights amber and the file glyph above it duplicates into a faded twin labeled 'backups kept'. On 'Updates never re-pull', a download arrow above the line gets a slash drawn through it. On 'A downgrade can', a small arrow below the line flips to point backward and the download glyph flashes once, then everything holds still for the cut to the close. | hyperframes | timeline | 5.9 |
| s06 | payoff_close | Update always, re-pull never, and pull new only when a feature names a model. | Update always. \| Re-pull never. \| Pull new. | Centered-stack that rhymes with frame 1: same typeface, same two-line geometry and amber accent as the hook composition. 'Update always.' rises in place on its spoken phrase; 'Re-pull never.' follows in amber on its phrase; 'Pull new when a feature names one.' fades in last, smaller and dimmed. Only one text block animates at a time. After the final word the frame holds, and in the final 0.5 s a small 'BUILD LOCAL AI' wordmark settles at the top of the safe area. First and last 8 frames fully static. | hyperframes | centered-stack | 4.4 |

## Notes for review
- The judge zeroed draft A's voice row: the hook asks a question the viewer cannot answer from what they own. Kept anyway (the question names the decision the video answers in the next sentence); if you disagree, swap to candidate 10's situation framing.
- Spoken numbers: three spent (113 MB, 2B params, about 3 GB) plus the version "zero point forty point two"; "v0.40.11" itself is never spoken, only shown in the title and description, per Hard Constraint 4.
- The music-player analogy lands in s02 ("New player, same songs") and its limit becomes the catch in s05; the analogy object carries the full limit text.
- est_sum is 37.9 s against target 35; normalizer changed 1 scene. Tighten inter-scene pauses in assembly if the VO lands long.
