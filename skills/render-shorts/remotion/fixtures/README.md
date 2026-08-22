# Remotion fixtures

- `example-props.json`: a real v1 props file (the "shrink-the-numbers" Short: six segments, whisper-aligned captions, no music, no sfx). It shows the exact shape `scripts/assemble.py` generates. Its media (`shrink-the-numbers/*.mp4`, `vo.wav`) is not ported, so it does not render as-is.
- `../smoke-props.json` plus `../public/smoke/` (three 1080x1920 clips and a 13 s voice track, 1.2 MB): the renderable smoke test. `npx remotion render Assembly out/smoke.mp4 --props=smoke-props.json --color-space=bt709` from `remotion/`.
- `../public/sfx/`: the five bundled cues (`whoosh`, `pop`, `tick`, `ding`, `type`) referenced by the `sfx` prop; recipe in `../../assets/sfx/README.md`.
