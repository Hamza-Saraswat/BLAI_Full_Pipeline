# Vendored HyperFrames skills

Origin: https://github.com/heygen-com/hyperframes (the `skills/` directory), installed in v1 on 2026-07-04 with `npx -y skills@1.5.14 add heygen-com/hyperframes --agent claude-code --skill '*' -y` (HyperFrames CLI 0.7.31 era) and copied here verbatim. License: Apache-2.0, copyright HeyGen. These files are third-party content: exempt from this repo's style rules (em dashes, 200-line cap, naming) and not covered by the repo license.

Kept (the skills `rules/hyperframes-1.md` tells a scene worker to load):

- `hyperframes-core/`: the composition contract (`data-*` timing, clips, tracks, sub-compositions, determinism rules)
- `hyperframes-cli/`: lint, validate, inspect, preview, render, doctor, browser
- `hyperframes-keyframes/`: seek-safe keyframes and GSAP timelines

Not vendored: `hyperframes` (the intent router), `hyperframes-animation`, `hyperframes-creative`, `hyperframes-media`, `hyperframes-registry`, and the video-workflow skills (product-launch-video, faceless-explainer, and so on). Cross-references to them inside the kept files point at files that are not here. Reinstall the full set with the command above if a worker needs them. Per-skill content hashes of the installed versions are in the v1 repo's `skills-lock.json`.
