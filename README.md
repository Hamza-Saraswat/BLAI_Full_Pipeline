# BLAI Full Pipeline

Automated content factory for the **Build Local AI** YouTube channel, built with the Interpretable Context Methodology (ICM): folder structure as agent architecture, markdown as the interface, one agent reading the right files at each stage.

- `workspaces/shorts/` produces two Shorts a day.
- Cloud routines (claude.ai/code) run the thinking stages every morning and push markdown to this repo.
- A build agent on a DGX Spark pulls the repo, renders and voices the videos, and sends a Telegram card.
- One tap approves; Blotato schedules the upload to YouTube.
- The repo is cloned inside an Obsidian vault, so every idea, brief, script, package and build journal is a note.

Start here: `CLAUDE.md` (root router), then `workspaces/<name>/CLAUDE.md`.

Repo layout and conventions follow `research/ICM-BUILD-GUIDE.md`. Posting rules, voice and publishing choices follow `research/youtube-automation-research.md`.

Directories: `brand-vault/`, `shared/`, `skills/`, `workspaces/`, `build/`, `tools/`, `analytics/`, `research/`, `_design/`.

License: MIT for original code and docs. Vendored skills keep their own licenses (see each `skills/<name>/LICENSE` where present).
