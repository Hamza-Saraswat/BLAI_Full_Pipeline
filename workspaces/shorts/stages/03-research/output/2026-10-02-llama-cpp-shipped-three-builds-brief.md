---
slug: 2026-10-02-llama-cpp-shipped-three-builds
stage: 03-research
topic: "llama.cpp shipped three builds in seven hours"
depth: standard
generated_at: 2026-10-02T11:38:44Z
sources: 9
hub: "[[videos/2026-10-02-llama-cpp-shipped-three-builds]]"
---

# Research brief: llama.cpp shipped three builds in seven hours

## Summary
The fetched releases index corrects the premise: the three-build window (b11339 to b11344) spans 4 h 25 min, and the fuller story is 10 tagged builds between 00:48 and 08:54 on 02 Oct, each a single targeted fix pushed by the release bot. The most arresting number is 10 nightlies in one morning against a project whose own docs say the GitHub releases page carries only nightly/development builds. The strongest concrete case is issue #13157: a maintainer dates a "recently pulled" setup to January from the startup build line, the same line that reveals a stale binary shadowing a fresh build. Reddit was unfetchable this run (403), so every Reddit-sourced belief sits under Unverified. One conflict: the idea's title says seven hours; the pages say 4 h 25 min, and this brief carries the corrected figures.

## Thesis
The b-numbered llama.cpp builds are the project's documented nightlies, cut by a bot, and on 02 Oct 2026 ten of them landed in one morning, so the tag you pin is the only thing keeping your local setup reproducible.

## Explanation path
Start with what actually happened this morning: ten tagged builds, b11331 through b11344, published between 00:48 and 08:54, three of them inside a four-and-a-half-hour window, each one a single targeted fix, each pushed by the release bot. Before the viewer can feel why that matters they need the project's two-track versioning: official releases are semantic-version tags where the tag is the release artifact, while the GitHub releases page carries only nightly development builds, which is what the b numbers are. Once nightlies are understood as the default channel, the pain arrives on its own: an old binary rejects new-model GGUFs outright, maintainers' first diagnostic is the build line the binary prints at startup, and the usual culprit is a stale binary shadowing the fresh one from PATH or a venv. That reframes the morning burst as the re-pin moment: check out a newer tag, rebuild for the connected hardware, and know what to fall back to. Close on the honest catch: pinning the code pins the code, not the compiler or the GPU flags.

## Claims
1. **On 02 Oct 2026 llama.cpp published releases b11339, b11342 and b11344, and the b11339-to-b11344 span was 4 h 25 min (04:29 to 08:54), not the seven hours the idea's title claimed.**
   - Source: Releases · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "02 Oct 04:29" (b11339) and "02 Oct 08:54" (b11344); 265 minutes computed
2. **Ten tagged releases (b11331 through b11344) shipped on 02 Oct between 00:48 and 08:54, a span of 8 h 06 min.**
   - Source: Releases · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: release list shows b11344, b11342, b11339, b11338, b11337, b11335, b11334, b11333, b11332, b11331; oldest on page "02 Oct 00:48"
3. **b11344 is one targeted fix: "CUDA: fix 2 broken Volta FA cases".**
   - Source: Release b11344 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b11344
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "CUDA: fix 2 broken Volta FA cases ( [#29803](https://github.com/ggml-org/llama.cpp/pull/29803))"
4. **b11342 fixes cache-directory creation through symlinks on a buggy libstdc++, authored by a Hugging Face engineer, with the root cause an upstream GCC bug.**
   - Source: Release b11342 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b11342
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "common,rpc : fix cache dir creation through symlinks on buggy libstdc++" ... "Signed-off-by: Adrien Gallouët angt@huggingface.co"; "See https://gcc.gnu.org/bugzilla/show_bug.cgi?id=101510"
5. **b11339 clamps a KV-cache pool bound that overshot when a batch fills the whole context, and its commit was AI-assisted, credited in the release note.**
   - Source: Release b11339 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b11339
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "llama : clamp kpool re-pool bound to existing pools"; "Assisted-by: pi:llama.cpp/MiMo-V2.6-Flash-MOPD"; failure mode: "the first full-context decode builds bigger tensors than reserved"
6. **The official release process uses semantic versioning and the git tag is the release artifact.**
   - Source: Release process (docs/release.md, llama.cpp master), https://raw.githubusercontent.com/ggml-org/llama.cpp/master/docs/release.md
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "No GitHub Release object is created, the tag is the release artifact."
7. **The b-numbered builds on the GitHub releases page are the project's own documented nightlies.**
   - Source: Release process (docs/release.md, llama.cpp master), https://raw.githubusercontent.com/ggml-org/llama.cpp/master/docs/release.md
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "Currently releases are not published to github releases, only nightly/development builds are available there."
8. **All three builds are marked Pre-release, published by the github-actions bot rather than a human, and each release page carries 37 binary assets covering Apple Silicon, CUDA 12/13, Vulkan and ROCm 10.0.**
   - Source: Release b11339 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b11339
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "Pre-release" + publisher github-actions; "macOS Apple Silicon (arm64)", "Windows x64 (CUDA 13)", "Ubuntu x64 (Vulkan)", "Ubuntu x64 (ROCm 10.0)", "Assets37"
9. **Default source builds identify as development builds by appending a -dev suffix to the version string; a clean string requires passing -DLLAMA_BUILD_IS_DEV=OFF.**
   - Source: Release process (docs/release.md, llama.cpp master), https://raw.githubusercontent.com/ggml-org/llama.cpp/master/docs/release.md
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "By default, `LLAMA_BUILD_IS_DEV=ON` which appends a `-dev` suffix to `LLAMA_VERSION`"
10. **Builds compile for the hardware present at build time by default.**
   - Source: Build llama.cpp locally (docs/build.md, llama.cpp master), https://raw.githubusercontent.com/ggml-org/llama.cpp/master/docs/build.md
   - Tier: primary | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "By default llama.cpp will be built for the hardware that is connected to the system at that time."
11. **Maintainers' first diagnostic for a broken setup is the build line printed at startup.**
   - Source: Issue #13157: Architecture qwen3 not supported, https://github.com/ggml-org/llama.cpp/issues/13157
   - Tier: community | Confidence: high | Accessed: 2026-10-02 | Via: web_extract
   - Quote: "Your versions are very old: - build: 4591 (7919256) - this is from January ... Update to latest version."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | tagged releases on 02 Oct 2026 (b11331-b11344) | 10 | https://github.com/ggml-org/llama.cpp/releases | release list shows b11344 through b11331; oldest on page "02 Oct 00:48" |
| 2 | span of the whole 02 Oct burst (00:48 to 08:54) | 8 h 06 min | https://github.com/ggml-org/llama.cpp/releases | computed from "02 Oct 00:48" and "02 Oct 08:54" |
| 3 | span b11339 to b11344 (the three-build window) | 4 h 25 min | https://github.com/ggml-org/llama.cpp/releases | "02 Oct 04:29" to "02 Oct 08:54"; 265 minutes computed |
| 4 | gap between b11339 and b11342 | 0 h 37 min | https://github.com/ggml-org/llama.cpp/releases | "02 Oct 04:29" to "02 Oct 05:06"; computed |
| 5 | binary assets per release page | Assets37 (37) | https://github.com/ggml-org/llama.cpp/releases/tag/b11344 | "Assets37" |
| 6 | stale build a maintainer dated from January | build: 4591 (7919256) | https://github.com/ggml-org/llama.cpp/issues/13157 | "build: 4591 (7919256) - this is from January" |
| 7 | CUDA cases fixed by b11344 | 2 broken Volta FA cases | https://github.com/ggml-org/llama.cpp/releases/tag/b11344 | "CUDA: fix 2 broken Volta FA cases" |

## Analogy candidates
- **The named bus departure**: a b-number is the 7:42 bus, a specific departure you can board again tomorrow; master or latest is whichever bus pulls up next; pinning is deciding you always take the 7:42. Breaks when: every bus on a route drives identically, but two b-builds can differ in speed, output or model support, so the schedule metaphor hides that the vehicle itself changes.
- **The dyno-signed engine map**: a pinned build is the exact engine map your best dyno sheet was recorded on; ten builds in a morning is the factory shipping ten new maps before lunch; re-pinning is flashing back to the map your numbers came from. Breaks when: an ECU map is one file, while a build pins code plus compiler and hardware flags at once, so the flash is never the whole story.

## Misconceptions
- Myth: The b-numbers are llama.cpp's real version numbers. Reality: official releases are semantic-version tags; the b-family is the project's own documented nightly/development channel (claim 7).
- Myth: I cloned llama.cpp recently, so I am running a recent build. Reality: the executing binary can be months old; maintainers dated one recent setup to January from the startup build line (claim 11).
- Myth: This GGUF is broken. Reality: the model file is fine; the binary predates the architecture (unknown model architecture: qwen3) and updating fixes it (claim 11's issue).
- Myth: New release builds are instantly available everywhere. Reality: even latest-prebuilt-binary users hit the unknown-architecture error because prebuilts lag master.
- Myth: llama.cpp shipped three builds in seven hours. Reality: the b11339-to-b11344 span is 4 h 25 min; the fuller story is ten builds in 8 h 06 min on 02 Oct (claims 1-2).

## Glossary
- **b-tag**: llama.cpp's numbered build tags (b11339, b11342, b11344), the nightly channel cut automatically from master.
- **pre-release**: GitHub's flag on every b-tagged build; the llama.cpp docs call these nightly/development builds.
- **pinned commit**: an exact git tag or SHA you git checkout after cloning, so every machine and every rerun compiles the same code.
- **build from source**: cloning the repo and compiling it yourself with CMake instead of downloading pre-built binaries.
- **nightly**: the b-numbered development builds the README badges separately from the semantic-version releases.
- **GGUF**: the single-file model container llama.cpp loads; new architectures require a binary new enough to know them.
- **stale binary**: an old compiled llama-cli or main left in PATH or a venv that keeps getting invoked after a rebuild.
- **CUDA**: NVIDIA's GPU-computing platform; llama.cpp's CUDA backend provides GPU acceleration using an NVIDIA GPU.
- **Metal**: Apple's GPU API, the default backend on macOS, where computation runs on the GPU.
- **KV cache pool**: pooled memory slots for the attention KV cache; b11339 clamps the pool bound so a full-context batch cannot overshoot reserved memory.
- **Flash Attention (FA)**: a fast attention kernel; b11344 fixes 2 broken cases on Volta (pre-Turing NVIDIA GPUs).
- **re-pin**: deliberately moving your frozen checkout forward to a newer tag and rebuilding.

## Unverified
- GitHub's release timestamps print as 02 Oct 08:54 with no timezone or year; they are consistent with UTC cross-checked against relative ages, but the page never states it.
- Whether tags b11336, b11340, b11341 and b11343 exist without published releases cannot be confirmed from the fetched index.
- A Reddit PSA recommends re-pinning via git reset --hard, git clean, git fetch --all --tags --prune and git checkout of a tag; snippet only, Reddit blocked all fetches.
- r/LocalLLaMA jokes that five minutes after a git pull there were probably three new PRs; snippet only, community tier.
- How often power users pin versus ride master has no fetched evidence either way.
- Tokens-per-second or memory impact of these builds on the Spark should be measured first-party before quoting any performance expectation.

## Suggested outline
1. Open on the burst: ten tagged builds before 09:00 on 02 Oct, three of them inside four and a half hours, each a single fix, each pushed by the bot.
2. Name the channel: the b-numbers are the documented nightlies; official releases are the semantic-version tags, and the tag is the release artifact.
3. Show the pain: an old binary rejects new GGUFs outright; maintainers read the startup build line first and keep finding January-old binaries that were just pulled.
4. Land the thesis: with ten nightlies a morning, the pinned tag is the only thing making your numbers reproducible; re-pin deliberately, then verify the binary you run is the one you built.

## Viewer situation
You built llama.cpp from source once, it runs, and you have not touched the checkout since; new-model GGUFs are starting to fail with unknown-architecture errors.

## Has process
`true`
- Read the build and commit line your binary prints at startup to learn what you are actually running.
- git fetch --tags in your llama.cpp checkout to see the new b-tags.
- git checkout the build tag you want to pin (for example b11344).
- Rebuild with cmake --build and install the fresh binary.
- Check PATH and any venv for an older llama-cli or main still shadowing the new build.
- Run a known model and compare against your last recorded numbers; if the new tag regresses, fall back to the previous known-good tag.

## Objection
Pinning the tag pins the code, not the run: builds compile for the connected hardware by default and the version string stays a -dev build unless you pass -DLLAMA_BUILD_IS_DEV=OFF, so reproducibility still depends on the machine and the flags.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/ggml-org/llama.cpp/releases | Releases · ggml-org/llama.cpp · GitHub | primary | web_extract | 2026-10-02 |
| 2 | https://github.com/ggml-org/llama.cpp/releases/tag/b11344 | Release b11344 · ggml-org/llama.cpp · GitHub | primary | web_extract | 2026-10-02 |
| 3 | https://github.com/ggml-org/llama.cpp/releases/tag/b11342 | Release b11342 · ggml-org/llama.cpp · GitHub | primary | web_extract | 2026-10-02 |
| 4 | https://github.com/ggml-org/llama.cpp/releases/tag/b11339 | Release b11339 · ggml-org/llama.cpp · GitHub | primary | web_extract | 2026-10-02 |
| 5 | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/docs/release.md | Release process (docs/release.md, llama.cpp master) | primary | web_extract | 2026-10-02 |
| 6 | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/docs/build.md | Build llama.cpp locally (docs/build.md, llama.cpp master) | primary | web_extract | 2026-10-02 |
| 7 | https://github.com/ggml-org/llama.cpp/issues/13157 | Issue #13157: Architecture qwen3 not supported | community | web_extract | 2026-10-02 |
| 8 | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/README.md | llama.cpp README (master) | primary | web_extract | 2026-10-02 |
| 9 | https://github.com/ggml-org/llama.cpp/issues/7974 | Issue #7974: MTLComputePipelineDescriptorInternal failed assertion | community | web_extract | 2026-10-02 |

## Notes
Conflict: the idea's title says seven hours; the fetched releases index shows the b11339-to-b11344 span is 4 h 25 min and the fuller story is 10 builds in 8 h 06 min. The brief carries the corrected numbers; the script stage should not say seven hours. The docs site (ggml-org.github.io) 404s; raw.githubusercontent.com doc files are the fetched equivalents. Reddit was unfetchable this run (403), so every Reddit-sourced belief sits under Unverified. Issue #7974 and the README are fetched supporting pages no claim cites.

## Decisions
- Stage-03 checkpoint: angle confirmed as "the b-numbered builds are documented nightlies, and one morning of them (10 builds on 02 Oct) is the re-pin moment for anyone holding a pinned checkout"; slug unchanged. The idea's "seven hours" was corrected by the fetched pages to 4 h 25 min for the three-build window, 8 h 06 min for the ten-build morning; the script stage must not say seven hours.
- Source depth: 9 sources fetched via web_search discovery + web_extract (FIRECRAWL 402, no connector), inside the standard band; 11 claims (9 primary, 2 community), 7 key numbers, 2 analogy candidates with limits, 5 misconceptions, 12 glossary terms.
