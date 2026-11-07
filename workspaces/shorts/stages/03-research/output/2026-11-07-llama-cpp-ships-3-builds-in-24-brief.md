---
slug: 2026-11-07-llama-cpp-ships-3-builds-in-24
stage: 03-research
topic: "llama.cpp shipped b12186, b12187 and b12188 inside one day -- re-pin and re-measure"
depth: standard
generated_at: 2026-11-07T12:38:13Z
sources: 10
hub: "[[videos/2026-11-07-llama-cpp-ships-3-builds-in-24]]"
---

# Research brief: llama.cpp ships 3 builds in 24 hours -- re-pin yours

## Summary
llama.cpp has no stable release to wait for, so the only honest posture is a pinned build number plus a habit of re-pinning: on 07 Nov 2026 the project stamped builds b12186, b12187 and b12188 at 11:11, 11:42 and 11:58 -- three releases inside one hour, six by late morning. The strongest concrete case is that each of those builds is one merged, named change (a Vulkan fix, a WebGPU kernel, a llama-server scheduling fix), not filler: upstream ships small real changes continuously, and every build ships 40 prebuilt artifacts ("Assets40") for Windows, macOS and Linux backends. What could not be verified: any tokens-per-second delta from re-pinning -- no number exists upstream, so the viewer must measure their own box with llama-bench. One conflict: a 2024 discussion describes llama.cpp as rolling releases without semantic versioning, while the current release.md documents semver tags and says GitHub releases carry only nightly/development builds -- the b-numbers the viewer sees are the dev stream.

## Thesis
Because llama.cpp ships continuously and maintains no stable release -- b12186, b12187 and b12188 landed between 07 Nov 11:11 and 07 Nov 11:58 -- a build pinned yesterday is already three releases stale, and the move is to re-pin and re-measure with llama-bench.

## Explanation path
Start with what the viewer actually has: one downloaded or compiled llama.cpp with a build number in it, frozen at the day they got it. Establish that upstream does not share that freeze: the maintainer says there is no stable release and the project develops too fast to pick one, so builds stream out as numbered tags cut from master. Then land the event: on the morning of 07 Nov 2026 the releases page stamped b12186 at 11:11, b12187 at 11:42 and b12188 at 11:58 -- three releases inside one hour, and the sixth build of that day -- and each one is a single named change (Vulkan, WebGPU, llama-server), which is what continuous delivery looks like. Explain why stale costs something: fixes and kernels land in these small builds, official docs treat "clone and rebuild" as the normal update path, and the releases page hands you 40 prebuilt artifacts so re-pinning is a download, not an ordeal. Close with the discipline that makes it repeatable: llama-bench reports average tokens per second and records the build number in every result row, so re-pin then re-measure, and next time you can say how much the update was worth rather than guessing.

## Claims
1. **llama.cpp published builds b12186, b12187 and b12188 on 07 Nov 2026 at 11:11, 11:42 and 11:58 -- 3 releases inside one hour.**
   - Source: Releases · ggml-org/llama.cpp, https://github.com/ggml-org/llama.cpp/releases
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "## b12188 ... 07 Nov 11:58 ... ## b12187 ... 07 Nov 11:42 ... ## b12186 ... 07 Nov 11:11"
2. **Build b12186 is a Vulkan fix -- "vulkan: Add 'readonly' to decodeBuf declarations" (PR #31833) -- with a possible future performance payoff.**
   - Source: Release b12186 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b12186
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "vulkan: Add 'readonly' to decodeBuf declarations. ( #31833) ... In a future driver version I hope to be able to get some perf gain out of this."
3. **Build b12187 adds a WebGPU compute kernel -- "webgpu : Implement group norm kernel" (PR #31490).**
   - Source: Release b12187 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b12187
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "webgpu : Implement group norm kernel ( #31490)"
4. **Build b12188 changes llama-server scheduling -- "server: visit parent slots before child slots" (PR #30779) -- so cached prompt prefixes wake their children into the same batch.**
   - Source: Release b12188 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b12188
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "server: visit parent slots before child slots ( #30779) ... Non-child slots are now visited before active child slots, so every child woken by its parent joins the same batch."
5. **Six builds were published on 07 Nov 2026 alone: b12183 (09:17), b12184 (09:47), b12185 (10:52), b12186 (11:11), b12187 (11:42), b12188 (11:58).**
   - Source: Releases · ggml-org/llama.cpp, https://github.com/ggml-org/llama.cpp/releases
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "## b12183 ... 07 Nov 09:17 ... ## b12184 ... 07 Nov 09:47 ... ## b12185 ... 07 Nov 10:52 ... ## b12186 ... 07 Nov 11:11 ... ## b12187 ... 07 Nov 11:42 ... ## b12188 ... 07 Nov 11:58"
6. **Every build ships 40 prebuilt download artifacts (the page renders "Assets40"), covering Windows, macOS, Linux and Android across CPU, CUDA, Vulkan, ROCm, SYCL and OpenVINO backends.**
   - Source: Release b12186 · ggml-org/llama.cpp · GitHub, https://github.com/ggml-org/llama.cpp/releases/tag/b12186
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "Assets40"
7. **The official update path is clone, configure and rebuild: "cmake -B build" then "cmake --build build --config Release", with "-j 8" running 8 compile jobs in parallel.**
   - Source: llama.cpp/docs/build.md at master, https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "cmake --build build --config Release -j 8 will run 8 jobs in parallel."
8. **There is no stable llama.cpp release: asked directly, maintainer ggerganov answered "Not atm.", because the project develops too fast to choose one.**
   - Source: Release Cycle of llama.cpp · Discussion #16111, https://github.com/ggml-org/llama.cpp/discussions/16111
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "Is there a notion of a \"stable\" release? Not atm. ... The project is developing very fast, so it is difficult to decide when we have a stable release."
9. **llama-bench measures prompt processing and text generation and reports "average tokens per second (t/s)", repeating each test 5 times by default and stamping every result row with the build number it ran on.**
   - Source: llama.cpp/tools/llama-bench/README.md at master, https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
   - Quote: "number of times to repeat each test (default: 5) ... The results are given in average tokens per second (t/s) and standard deviation. ... build_commit TEXT, build_number INTEGER"
10. **The b-numbered GitHub releases are the nightly/development stream: official release.md says stable releases reach users through llama-install.sh, package managers, or building from the tag -- not through GitHub releases.**
    - Source: llama.cpp/docs/release.md at master, https://github.com/ggml-org/llama.cpp/blob/master/docs/release.md
    - Tier: primary | Confidence: high | Accessed: 2026-11-07 | Via: web_extract
    - Quote: "Currently releases are not published to github releases, only nightly/development builds are available there."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | b12186 published | 07 Nov 11:11 | https://github.com/ggml-org/llama.cpp/releases | "07 Nov 11:11" |
| 2 | b12187 published | 07 Nov 11:42 | https://github.com/ggml-org/llama.cpp/releases/tag/b12187 | "07 Nov 11:42" |
| 3 | b12188 published | 07 Nov 11:58 | https://github.com/ggml-org/llama.cpp/releases/tag/b12188 | "07 Nov 11:58" |
| 4 | releases on 07 Nov 2026, countable on the index (b12183-b12188) | 6 builds | https://github.com/ggml-org/llama.cpp/releases | "## b12188 ... 07 Nov 11:58 ... ## b12183 ... 07 Nov 09:17" |
| 5 | prebuilt artifacts per release | Assets40 | https://github.com/ggml-org/llama.cpp/releases/tag/b12186 | "Assets40" |
| 6 | llama-bench repetitions per test (default) | 5 | https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md | "number of times to repeat each test (default: 5)" |
| 7 | commits on llama.cpp master | 12,187 Commits | https://github.com/ggml-org/llama.cpp | "12,187 Commits" |

## Analogy candidates
- **Phone OS updates**: mapping -- your build number is an OS version, and llama.cpp pushes updates the way phones push security patches: small, frequent, easy to install. Breaks when: phones have a stable channel and you can skip versions; llama.cpp has no stable release at all, so skipping means drifting.
- **Milk freshness date**: mapping -- a build number is a freshness stamp, and yesterday's pin is already past it. Breaks when: old milk is unsafe while an old llama.cpp build still runs fine -- it is just missing fixes and speed, not spoiled.

## Misconceptions
- Myth: There is a stable llama.cpp version I should wait for. Reality: The maintainer's own answer is "Not atm." -- the project develops too fast to pick one, so the b-number stream is the product (claim 8).
- Myth: Three builds in one hour means rushed, trivial junk. Reality: Each build is one merged, named change aimed at a specific backend or tool -- a Vulkan fix, a WebGPU kernel, a llama-server scheduling improvement (claims 2, 3, 4).

## Glossary
- **build number**: llama.cpp's version stamp (the b in b12188); every binary reports it and llama-bench records it with each result.
- **prebuilt binary**: a ready-to-run download of a build for your operating system and GPU backend, so you re-pin without compiling.
- **backend**: the part of llama.cpp that talks to specific hardware -- CUDA for NVIDIA, Vulkan for many GPUs, Metal on Mac -- which is why each release ships many separate downloads.
- **Vulkan**: a cross-platform GPU API llama.cpp uses as a backend that works on many graphics cards, not just one vendor.
- **llama-bench**: llama.cpp's built-in benchmark tool; it reports average tokens per second for prompt processing and generation.
- **tokens per second (t/s)**: how fast the model reads a prompt or writes text; the number to compare before and after a re-pin.

## Unverified
- No performance delta from re-pinning to b12188 is published anywhere upstream; any "x% faster" claim must come from the viewer's own llama-bench run.
- The b12186 Vulkan change's performance payoff is a hope, not a number -- the release note itself says "In a future driver version I hope to be able to get some perf gain out of this."
- Which build a typical viewer pinned "yesterday" is unknowable; the three-releases-stale framing assumes a pin older than b12185.
- Community claims that frequent llama.cpp rebuilds recover meaningful speed were not fetched this session and stay out of the claims.

## Suggested outline
1. While you were having breakfast llama.cpp shipped three builds -- b12186 at 11:11, b12187 at 11:42, b12188 at 11:58 -- and if you pinned yesterday, you are already behind; show the timestamps on the releases page.
2. What actually landed, one line each: a Vulkan fix, a WebGPU kernel, a llama-server scheduling change -- and the maintainer's own words that there is no stable release to wait for, plus the detail that these b-builds are the dev stream by design.
3. The move: check your build number, re-pin by grabbing one of the 40 prebuilt artifacts (or git pull and rebuild with cmake), then re-run llama-bench so the build number and your new tokens-per-second land in the same table -- that comparison, not the download, is the point.

## Viewer situation
You run a llama.cpp build you downloaded or compiled weeks ago on your gaming PC or Mac, and you could not say which build number it is.

## Has process
true
Check the build number your install reports, for example in a llama-bench run (its results record a build_number).
Compare that number with the newest tag on the llama.cpp releases page.
Download the prebuilt package for your operating system and backend from the latest release, or git pull and rebuild with cmake -B build and cmake --build build --config Release.
Swap in the new binaries and keep the old folder so you can roll back.
Re-run llama-bench with the same model and settings you used before.
Compare the old and new average tokens per second, noting both build numbers.

## Objection
Three builds in an hour is just CI churn -- nothing that lands that fast changes my tokens per second, so rebuilding is ceremony without payoff.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/ggml-org/llama.cpp/releases | Releases · ggml-org/llama.cpp | primary | web_extract | 2026-11-07 |
| 2 | https://github.com/ggml-org/llama.cpp/releases/tag/b12186 | Release b12186 · ggml-org/llama.cpp | primary | web_extract | 2026-11-07 |
| 3 | https://github.com/ggml-org/llama.cpp/releases/tag/b12187 | Release b12187 · ggml-org/llama.cpp | primary | web_extract | 2026-11-07 |
| 4 | https://github.com/ggml-org/llama.cpp/releases/tag/b12188 | Release b12188 · ggml-org/llama.cpp | primary | web_extract | 2026-11-07 |
| 5 | https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md | llama.cpp/docs/build.md at master | primary | web_extract | 2026-11-07 |
| 6 | https://github.com/ggml-org/llama.cpp/blob/master/docs/release.md | llama.cpp/docs/release.md at master | primary | web_extract | 2026-11-07 |
| 7 | https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md | llama.cpp/tools/llama-bench/README.md at master | primary | web_extract | 2026-11-07 |
| 8 | https://github.com/ggml-org/llama.cpp/discussions/16111 | Release Cycle of llama.cpp · Discussion #16111 | primary | web_extract | 2026-11-07 |
| 9 | https://github.com/ggml-org/llama.cpp | ggml-org/llama.cpp: LLM inference in C/C++ | primary | web_extract | 2026-11-07 |
| 10 | https://github.com/ggml-org/llama.cpp/discussions/9276 | Breaking Changes · Discussion #9276 | community | web_extract | 2026-11-07 |

## Notes
Conflict: discussion #9276 (Sep 2024) describes llama.cpp as "rolling releases instead of semantic versioning", while the current docs/release.md says the project uses semantic versioning (MAJOR.MINOR.PATCH) and that GitHub releases carry only nightly/development builds -- we follow release.md, and the distinction actually serves the video: the b-numbered builds the viewer downloads are the dev stream by design. Thin spot: no upstream performance number accompanies any of the three builds, so the payoff beat must be the viewer's own llama-bench comparison, never a quoted percentage. Dedupe: the 2026-09-19 Short covered three builds in two hours; this brief's core is the 07 Nov 2026 event (b12186-b12188, six builds in one morning) plus the re-pin/re-measure discipline.
