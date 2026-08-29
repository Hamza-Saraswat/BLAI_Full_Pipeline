# Scene constraints the storyboard must respect

The renderer enforces these; a brief that ignores them gets silently rewritten by a scene
worker, fifteen separate times. Write briefs that are legal on arrival (finding 61). Full
render-side law: `skills/render-shorts/rules/scene-agent.md` and the pack files.

## Motion

- Entrances are fade, scale, or rise-in-place only. NEVER "slides in from the edge": elements
  may not travel through the UI margins, and the safe-zone linter samples mid-animation frames.
- Motion onset no earlier than t=0.30s (frame 9); first and last 8 frames are stable. A brief
  that says "onset at 0.25s" is illegal by 0.017s.
- At most 2 elements animating at once; at most one text block animating at a time. A
  whole-screen change is a staged swap or a hard cut, never a cross-dissolve of two text blocks.

## Text budgets

- Hard cap 8 words visible at once. `on_screen_text` with two full clauses (12 words) cannot be
  drawn together: write one clause, or expect the worker to hard-cut between them.
- Minimum text height 64 px at 1080 wide. Monospace (terminal pack) advance is 0.6 em, so at
  64 px one line holds about 19 characters inside the safe box; long commands need a `\`
  continuation, not a smaller font.
- `split-compare` in the terminal pack: the minor side's longest word fits only at <= 7
  characters. A three-node `timeline` with word labels is at the width limit; labels wrap to
  two lines.

## Pack law (summary; the pack file wins)

- One accent color. Amber stays the single accent in every pack; do not ask for three amber
  elements in one frame.
- `terminal`: sharp corners only outside the window frame -- no pills, no rounded chips; hard
  cuts and typewriters, no soft fades on text.
- A number on screen is spoken in the same scene; deliberate recalls (the loop anchor) are the
  documented exception, and the last frame must rhyme with frame 1.

## Time

- Anchor every beat to a narration phrase, never a wall-clock second (script-format.md).
- A scene that receives an emphasis punch (`Indicate`, scale 1.12) must size that text to
  SAFE_W / 1.12 or the punch peak leaves the safe area.
