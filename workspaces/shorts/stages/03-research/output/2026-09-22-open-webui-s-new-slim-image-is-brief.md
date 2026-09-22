---
slug: 2026-09-22-open-webui-s-new-slim-image-is
stage: 03-research
topic: "Open WebUI v0.11.4 ships a slim Docker image at about 175 MB"
depth: standard
generated_at: 2026-09-22T11:42:32Z
sources: 10
hub: "[[videos/2026-09-22-open-webui-s-new-slim-image-is]]"
---

# Research brief: Open WebUI v0.11.4 ships a slim Docker image at about 175 MB

## Summary
Open WebUI v0.11.4 (released 21 Sep 2026) rebuilt its slim Docker image around the realization that most self-hosters never needed the bundled machine-learning stack: the release notes themselves state the slim build "comes down at around 175 MB", and Docker Hub's own tag page confirms 168.31 MB compressed for linux/amd64. The strongest concrete case: the previous v0.11.3-slim tag on the same registry weighed 1.44 GB, so this is not marketing math but a registry-listed collapse, driven by dropping the embedded models, torch and the tools that installed them. What could not be verified: the release notes' "around 175 MB" and Docker Hub's "168.31 MB" are close but not identical figures for presumably the same artifact, and no primary page decompresses sizes by architecture beyond amd64/arm64. One conflict to handle in the script: "89% smaller" is measured against the last release's slim (1.44 GB), while the standard image is 1.54 GB, so the honest comparison is slim-vs-slim, not slim-vs-standard. The project is also explicit that slim is a trade, not a free win: it refuses to start on MySQL or S3 storage, and voice, PDF reading and local embeddings move out to external services.

## Thesis
Open WebUI's new slim image proves the standard local AI front end never needed to be a multi-gigabyte download: strip the bundled models and their libraries and the whole interface pulls in about 175 MB, with the work you actually use delegated to services you point it at.

## Explanation path
Start from what the viewer already does: they run Open WebUI in Docker next to Ollama or an API key, and the image they pull is the heavyweight one. Establish what was actually inside that image: not just the chat interface but an entire local machine-learning stack -- the PyTorch library, pre-downloaded speech and embedding models, converters like ffmpeg and pandoc -- installed "just in case" even though most users' model inference happens elsewhere. Then the v0.11.4 change: the maintainers asked which of that a front end really needs, cut it, and published the result as the slim variant. Bring in the registry numbers so the size claim is concrete and checkable, and be honest that the 89% headline compares slim to the previous slim, not to the standard image. From sizes, move to the trade: slim refuses to start under configurations that need the removed stack (MySQL database, S3 file storage), and features like voice, PDF upload and local embeddings now require pointing at an external service -- which is no change at all for a default install chatting through Ollama or a hosted API. Land on the switch itself: the viewer's docker pull or compose file changes by one tag suffix, their volume keeps their chats, and the payoff is a pull measured in seconds of download instead of a coffee break.

## Claims
1. **Open WebUI's own release notes for v0.11.4 state the slim build "comes down at around 175 MB, near enough 89% smaller than the last release".**
   - Source: Release v0.11.4 · open-webui/open-webui · GitHub, https://github.com/open-webui/open-webui/releases/tag/v0.11.4
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "A slim build now comes down at around 175 MB, near enough 89% smaller than the last release"
2. **Docker Hub's tag page lists the current slim image (tag 0.11.4-slim) at a compressed size of 168.31 MB for linux/amd64.**
   - Source: openwebui/open-webui - Docker Image, https://hub.docker.com/r/openwebui/open-webui/tags
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "[4dc1a385ddd7](...) | linux/amd64 | 168.31 MB"
3. **The same Docker Hub page lists the previous v0.11.3-slim tag at 1.44 GB (linux/amd64) and the current standard 0.11.4 tag at 1.54 GB (linux/amd64).**
   - Source: openwebui/open-webui - Docker Image, https://hub.docker.com/r/openwebui/open-webui/tags
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "[4086320c12bd](...) | linux/amd64 | 1.44 GB" and "[332438e079ad](...) | linux/amd64 | 1.54 GB"
4. **The shrink came from removing the local machine-learning stack: the official docs list "no `torch`, no `sentence-transformers`, no `transformers`, no `faster-whisper`, no `unstructured`, and no `ffmpeg`, `pandoc` or build toolchain".**
   - Source: Quick Start / Open WebUI, https://docs.openwebui.com/getting-started/quick-start/
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "no `torch`, no `sentence-transformers`, no `transformers`, no `faster-whisper`, no `unstructured`, and no `ffmpeg`, `pandoc` or build toolchain"
5. **Slim is published under the tag `:main-slim` on ghcr.io with the bare `:slim` alias on Docker Hub, and slim is a variant of its own with no cuda or ollama combination.**
   - Source: Quick Start / Open WebUI, https://docs.openwebui.com/getting-started/quick-start/
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "`:main-slim` | Smaller image with the local machine-learning stack removed" and "Slim is a variant of its own, so there is no `cuda-slim` or `ollama-slim`."
6. **Slim refuses to start rather than failing later when the application database is not SQLite or PostgreSQL, or file storage is not local.**
   - Source: Quick Start / Open WebUI, https://docs.openwebui.com/getting-started/quick-start/
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "Two settings are checked at boot, and slim refuses to start rather than failing later"
7. **The official docs state nothing extra is required to run slim and chatting works exactly as on the standard image.**
   - Source: Quick Start / Open WebUI, https://docs.openwebui.com/getting-started/quick-start/
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "**Nothing extra is required to run it.** It starts on its own and chatting works exactly as it does on `:main`, with the model provider you were going to configure anyway."
8. **The code interpreter on slim fetches its Python packages from cdn.jsdelivr.net in the browser instead of from the instance.**
   - Source: Quick Start / Open WebUI, https://docs.openwebui.com/getting-started/quick-start/
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "the browser fetches the Python packages from `cdn.jsdelivr.net` rather than from your instance"
9. **The v0.11.4 release notes also state the standard image lost about 170 MB by dropping a second copy of Python, duplicate fonts and unused packages.**
   - Source: Release v0.11.4 · open-webui/open-webui · GitHub, https://github.com/open-webui/open-webui/releases/tag/v0.11.4
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "The image no longer carries a second copy of Python, two sets of fonts nothing ever loaded, packages nothing imports, or the tool that installed them, taking about 170 MB off a standard build."
10. **User data lives in a Docker volume that survives the image swap, so switching to slim keeps chats, users and settings.**
   - Source: Updating Open WebUI / Open WebUI, https://docs.openwebui.com/getting-started/updating/
   - Tier: primary | Confidence: high | Accessed: 2026-09-22 | Via: web_extract
   - Quote: "Your data (chats, users, settings, uploads) lives in a Docker volume or local database, not inside the container."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | slim image size (release notes) | around 175 MB | https://github.com/open-webui/open-webui/releases/tag/v0.11.4 | "comes down at around 175 MB" |
| 2 | slim image size (Docker Hub, linux/amd64, compressed) | 168.31 MB | https://hub.docker.com/r/openwebui/open-webui/tags | "linux/amd64 \| 168.31 MB" |
| 3 | reduction vs last release (release notes) | 89% smaller | https://github.com/open-webui/open-webui/releases/tag/v0.11.4 | "near enough 89% smaller than the last release" |
| 4 | previous slim (v0.11.3-slim, linux/amd64, compressed) | 1.44 GB | https://hub.docker.com/r/openwebui/open-webui/tags | "linux/amd64 \| 1.44 GB" |
| 5 | standard image (v0.11.4, linux/amd64, compressed) | 1.54 GB | https://hub.docker.com/r/openwebui/open-webui/tags | "linux/amd64 \| 1.54 GB" |
| 6 | standard-image reduction (release notes) | about 170 MB | https://github.com/open-webui/open-webui/releases/tag/v0.11.4 | "taking about 170 MB off a standard build" |

## Analogy candidates
- **Vehicle**: Buying a phone that shipped with a professional kitchen installed, just in case you wanted to cook. Mapping: The old image carried PyTorch, speech models and converters for work most users delegate to Ollama or an API anyway; slim ships just the phone. Breaks when: The viewer actually uses those features locally, because a phone cannot grow a kitchen back, while slim can be swapped for the standard tag.
- **Vehicle**: A moving truck vs a hatchback for the commute. Mapping: Standard image is the truck: capable of hauling everything (local voice, embeddings, any database); slim is the hatchback that carries the actual daily load, chatting, and parks easier. Breaks when: The viewer's deployment needs the truck bed (MySQL, S3 storage), which slim refuses at boot.
- **Vehicle**: A hotel room mini-bar. Mapping: Every item in the mini-bar looks convenient and costs the room space and weight; slim is the same room with the mini-bar removed because you were ordering delivery (external services) all along. Breaks when: The hotel guest is offline, since slim's code interpreter needs the CDN and air-gapped users should stay standard.

## Misconceptions
- Myth: Slim is a smaller compressed download but the same multi-GB thing once unpacked on disk. Reality: Docker Hub's compressed size is the download, and it lists 168.31 MB for linux/amd64 (claim 2).
- Myth: The 89% claim is slim versus the standard image. Reality: The release notes say "89% smaller than the last release", and the last release's slim tag was 1.44 GB, matching the ratio; the standard image is a separate 1.54 GB (claims 1 and 3).
- Myth: Slim means features are missing or removed from the interface. Reality: The docs state nothing extra is required to run it and chatting works exactly as on :main; what changes is where the work happens (claim 7).
- Myth: Slim is only for Kubernetes or enterprise deployments. Reality: The docs frame it as the smaller image for anyone using Open WebUI as a chat front end for hosted models (claims 7 and 5).

## Glossary
- **slim image**: A Docker image variant of Open WebUI with the local machine-learning stack removed so it downloads at a fraction of the size.
- **Docker image**: The pre-packaged template Docker downloads and runs a program from; bigger images mean longer pulls.
- **tag**: The label suffix on a Docker image name (like :main-slim or :0.11.4) that picks a specific build or variant.
- **compressed size**: The size of a Docker image as stored in the registry, which is the amount you actually download.
- **bundled model**: A speech or embedding model pre-downloaded into the standard image whether or not you use it.
- **embedding model**: The model that turns documents into numeric vectors so knowledge search can find relevant passages.
- **torch (PyTorch)**: The Python library for running neural networks, and one of the largest single packages in the standard image.
- **ffmpeg**: A universal audio and video converter that was carried in the standard image for media handling.
- **RAG (retrieval augmented generation)**: Feeding a model relevant chunks from your own documents at answer time.
- **vector store**: The database that holds document embeddings for knowledge search; slim supports only pgvector.
- **pgvector**: A PostgreSQL extension that stores and searches vectors, the only vector store client slim carries.
- **code interpreter**: The feature that runs the model's Python code in your browser; on slim it loads its packages from a public CDN.
- **volume**: The Docker-managed storage folder that holds your chats and settings separately from the container, so it survives image swaps.

## Unverified
- How long the slim image takes to download or start on the viewer's own hardware, since no first-party measurement exists yet.
- Whether the "around 175 MB" in the release notes and the 168.31 MB on Docker Hub refer to exactly the same measurement basis beyond both being described as the slim build's size.
- Community reaction beyond one Reddit thread title and the GitHub discussion history, since Reddit blocked fetching and no HN thread on v0.11.4 exists yet.
- That the old image at one point reached 11 GB as one GitHub commenter claimed in 2025, since that is a community figure from a discussion, not a registry page.

## Suggested outline
1. Hook: the front end you pull every update just shrank from gigabytes to about 175 MB, and the registry itself says 168.31 MB.
2. What was actually inside the old image: an entire local ML stack shipped just in case you never configured Ollama or an API.
3. The honest catch: slim trades local voice, PDF reading and any-database support for the size, and the 89% is slim versus last slim, not versus standard.

## Viewer situation
You run Open WebUI in Docker today with the standard image tag, chatting through Ollama or a hosted API key, and you wince at the multi-gigabyte pull on every update.

## Has process
`true`

- Check your setup uses SQLite and local file storage (the defaults) rather than MySQL or an S3 bucket.
- Change the image in your docker run command or compose file from the standard tag to the slim tag (ghcr.io/open-webui/open-webui:main-slim, or openwebui/open-webui:slim on Docker Hub).
- Pull and recreate the container as with any update; keep the same volume so chats and settings carry over.
- Point any feature you use that needs a model -- voice, PDF extraction, embeddings -- at an external service in the admin settings.

## Objection
A skeptical engineer says the size cut is honest but overstated as a win: the standard image is 1.54 GB, not 10 GB, most of it is downloaded once and cached, and if you ever want local voice or document embeddings you are back on the fat image or wiring up external services anyway.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/open-webui/open-webui/releases/tag/v0.11.4 | Release v0.11.4 · open-webui/open-webui · GitHub | primary | web_extract | 2026-09-22 |
| 2 | https://docs.openwebui.com/getting-started/quick-start/ | Quick Start / Open WebUI | primary | web_extract | 2026-09-22 |
| 3 | https://hub.docker.com/r/openwebui/open-webui/tags | openwebui/open-webui - Docker Image | primary | web_extract | 2026-09-22 |
| 4 | https://docs.openwebui.com/getting-started/updating/ | Updating Open WebUI / Open WebUI | primary | web_extract | 2026-09-22 |
| 5 | https://github.com/open-webui/open-webui/releases/tag/v0.11.3 | Release v0.11.3 · open-webui/open-webui · GitHub | primary | web_extract | 2026-09-22 |
| 6 | https://github.com/open-webui/open-webui/discussions/12801 | enh: open-webui:slim docker image · Discussion #12801 | community | web_extract | 2026-09-22 |
| 7 | https://openwebui.com/blog/ | Blog • Open WebUI | primary | web_extract | 2026-09-22 |
| 8 | https://hn.algolia.com/api/v1/search?query=%22open%20webui%22%200.11.4 | HN Algolia search: open webui 0.11.4 (no results) | community | web_extract | 2026-09-22 |
| 9 | https://hn.algolia.com/api/v1/search?query=open-webui%20slim&tags=comment | HN Algolia comment search: open-webui slim | community | web_extract | 2026-09-22 |
| 10 | https://freedom.tech/posts/2026-09-21-open-webui-0-11-4/ | Open WebUI 0.11.4 | Freedom.Tech | docs | web_extract | 2026-09-22 |

## Notes
Two size figures coexist: the release notes' "around 175 MB" (unqualified basis) and Docker Hub's "168.31 MB" (compressed, linux/amd64; arm64 is 167.72 MB). The script should name the basis when quoting. The 89% figure is the project's own and checks out arithmetically against the previous slim tag (1.44 GB to 168.31 MB is about 88.3% on amd64, "near enough 89%"), but it compares slim to slim, not slim to the 1.54 GB standard image; both framings are honest if labeled. Thin spot: community reaction could not be fetched this run (Reddit 403 to all clients, no HN thread yet at 16 h post-release), so misconceptions are drawn from what the primary docs explicitly preempt (nothing extra required, features not removed) rather than from observed community posts. The GitHub discussion #12801 (2024-2025) supplies the history: users complained the image hit 11 GB and that the then-existing :latest-slim was somehow larger than :latest (5.2 GB vs 2.4 GB, community figures), which explains why a real rebuild was needed.
