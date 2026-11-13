---
slug: 2026-11-13-llama-cpp-1-0-pin-it-before-b1
stage: 03-research
topic: "llama.cpp v1.0.0 is the first stable tag, and a pre-release nightly with a known break shipped the same morning: pin the tag, don't ride master"
depth: standard
generated_at: 2026-11-13T13:03:00Z
sources: 11
hub: "[[videos/2026-11-13-llama-cpp-1-0-pin-it-before-b1]]"
---

# Research brief: llama.cpp 1.0 shipped today -- pin the tag before b1 bites

## Summary

- Thesis in brief: v1.0.0 is the first tag cut under the release conditions, and the nightly one commit past it already has a filed crash, so a home install should pin the tag rather than ride master.
- Most arresting number: the crash report against build 12360 landed 31 minutes after the v1.0.0 tag timestamp (2026-11-13T10:20:13Z tag, 2026-11-13T10:51:13Z issue).
- Strongest concrete case: Homebrew users poured 347 --HEAD build errors in 30 days against 68 on the stable formula, while stable still sits at 0.9.0 -- the pin/no-pin gap is measurable, not theoretical.
- Could not be verified: whether the b12360 abort reaches beyond CPU-only Intel AMX systems, and whether any performance difference exists on our own hardware.
- Conflict: GitHub's banner clocks for the three releases disagree with the exact source-archive tag timestamps; the brief uses the archive timestamps (see Notes).

## Thesis

llama.cpp shipped v1.0.0, its first stable tag, this morning, but master kept moving and the nightly cut one commit past the tag already has a filed crash, so pin the v1.0.0 tag in your install instead of riding master.

## Explanation path

Start by establishing that llama.cpp now runs two version lines at once: official vX.Y.Z release tags and b-number nightly builds cut from master, and that the v1.0.0 release page itself points at a nightly, b12359, under Assets. Then walk the morning's timeline from the fetched timestamps: the b12359 and b12360 tags were created five and a half minutes apart, v1.0.0 followed about an hour after b12359, and half an hour after the v1.0.0 tag a user filed an abort against build 12360 -- the commit exactly one step past the stable tag. Before the payoff lands, the viewer has to understand why the two lines differ: the maintainer's versioning doc says nightlies are built from master with the dev flag on, while release tags are built with it off and only cut when the internal ggml copy matches the released ggml, which is what makes a tag worth pinning. Then make the consequence concrete for a home install: Homebrew's stable formula is still 0.9.0 and its --HEAD track logged hundreds of build errors this month, v1.0.0 also removed 35 deprecated API functions so blind upgrades bite both ways, and even the official llama.app ships a pinned b-number engine rather than master. Land on the single action: check which build you run, pin the tag deliberately, and move to the next tag on purpose.

## Claims

1. **llama.cpp v1.0.0 was tagged at 2026-11-13T10:20:13Z on commit b1b770d, and the release page itself lists a nightly build, b12359, under Assets.**
   - Source: Release v1.0.0: ggml-org/llama.cpp, https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "Source code (zip) ... 11 minutes ago 2026-11-13T10:20:13Z" and "**Nightly build:** [b12359]"
2. **The b12359 release is labelled Pre-release, its source tag was created at 2026-11-13T09:09:55Z, and it is cut from b1b770d, the same commit as the v1.0.0 tag.**
   - Source: Release b12359: ggml-org/llama.cpp, https://github.com/ggml-org/llama.cpp/releases/tag/b12359
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "Pre-release" and "Source code (zip) ... 2 hours ago 2026-11-13T09:09:55Z"
3. **The b12360 release is labelled Pre-release, its source tag was created at 2026-11-13T09:15:25Z, and it is cut from commit 2d8a325.**
   - Source: Release b12360: ggml-org/llama.cpp, https://github.com/ggml-org/llama.cpp/releases/tag/b12360
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "Pre-release" and "Source code (zip) ... 2 hours ago 2026-11-13T09:15:25Z"
4. **The v1.0.0 release page shows exactly 1 commit to 2d8a325 since the release, and 2d8a325 is the commit b12360 is cut from, so the broken nightly sits one commit past the stable tag.**
   - Source: Release v1.0.0: ggml-org/llama.cpp, https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "1 commit to 2d8a32502909ca065c41c4cf5f2fb1c427c047fc since this release"
5. **At 2026-11-13T10:51:13Z a user filed issue #32197 reporting that llama-server aborts while building the compute graph for DeepSeek-V4.1-Flash-1017-UD-Q4_K_XL on a CPU-only Intel system with AMX, running llama.cpp 2d8a32502, build 12360.**
   - Source: DeepSeek-V4.1-Flash (deepseek41): CPU/AMX scheduler aborts on non-contiguous attn_wo_a input (issue #32197), https://github.com/ggml-org/llama.cpp/issues/32197
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "llama.cpp: `2d8a32502`, build `12360`" and "on a CPU-only Intel system with AMX"
6. **The maintainer's versioning doc states that nightlies are cut from master as b[NUM] tags built with -DLLAMA_BUILD_IS_DEV=ON, while official releases are vX.Y.Z tags built with -DLLAMA_BUILD_IS_DEV=OFF and are created only when the internal ggml copy is identical to the released ggml copy.**
   - Source: dist : releases and versioning of ggml-org projects (discussion #1579), https://github.com/ggml-org/ggml/discussions/1579
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "The release tags are created on the condition that the internal `ggml` copy is identical to the released `ggml` copy."
7. **v1.0.0 removes the deprecated public API: the release PR lists llama.h: remove llama_set_warmup, 35 deprecated functions, defrag_thold and --defrag-thold.**
   - Source: llama.cpp : bump version to 1.0.0 (pull request #32190), https://github.com/ggml-org/llama.cpp/pull/32190
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "llama.h: remove `llama_set_warmup`, 35 deprecated functions, `defrag_thold` and `--defrag-thold`"
8. **Homebrew's llama.cpp formula still pours stable 0.9.0, and over the last 30 days --HEAD installs logged 347 build errors against 68 for the stable formula.**
   - Source: Homebrew Formulae: llama.cpp, https://formulae.brew.sh/formula/llama.cpp
   - Tier: docs | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "Installs (`--HEAD`) | 257 | 716 | 3,274 ... Build Errors (`--HEAD`) | 347 ... Build Errors | 68" and "**stable** ... 0.9.0"
9. **The official llama.app desktop app, by the llama.cpp team and Hugging Face, ships a pinned engine build rather than master: its own site shows llama.cpp b9726 in the app's status menu.**
   - Source: Llama: Your AI, on your computer (llama.app), https://llama.app/
   - Tier: primary | Confidence: high | Accessed: 2026-11-13 | Via: web_extract
   - Quote: "By the llama.cpp team and Hugging Face" and "llama.cpp b9726"

## Key numbers

| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | v1.0.0 source tag created (release page asset timestamp) | 2026-11-13T10:20:13Z | https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0 | "2026-11-13T10:20:13Z" |
| 2 | b12360 pre-release source tag created | 2026-11-13T09:15:25Z | https://github.com/ggml-org/llama.cpp/releases/tag/b12360 | "2026-11-13T09:15:25Z" |
| 3 | issue #32197 (build 12360 abort) opened | 2026-11-13T10:51:13Z | https://github.com/ggml-org/llama.cpp/issues/32197 | "opened 2h ago on Nov 13, 2026" (GitHub API created_at 2026-11-13T10:51:13Z) |
| 4 | deprecated public API functions removed in v1.0.0 | 35 deprecated functions | https://github.com/ggml-org/llama.cpp/pull/32190 | "remove `llama_set_warmup`, 35 deprecated functions" |
| 5 | Homebrew --HEAD build errors in 30 days (vs 68 on stable) | 347 | https://formulae.brew.sh/formula/llama.cpp | "Build Errors (`--HEAD`) | 347" |

## Analogy candidates

- **Moving into a certified house vs living on the construction site**: the v1.0.0 tag is the inspected house (dev flag off, ggml copy matched to the release); master and its b-number nightlies are the site where rooms are still being moved, and b12360 is the scaffold that collapsed the same morning the house was certified. Breaks when: a finished house implies the work is done, but v1.0.0 is only the first certified snapshot and fixes will follow as new tags; also, all the new model architectures arrive on the construction site first.
- **Cooking from a pinned recipe vs eating whatever the chef is trying today**: a b-number nightly is the chef's experiment (sometimes DeepSeek-V4.1-Flash crashes the kitchen); a vX.Y.Z tag is the recipe that went through the release conditions and will cook the same tomorrow. Breaks when: recipes rarely remove ingredients you depend on, while v1.0.0 did remove 35 deprecated functions, so even the pinned track demands one deliberate migration.

## Misconceptions

- Myth: llama.cpp hitting 1.0 means the project is finished and master is now safe to ride. Reality: 1.0.0 is just the first tag cut under the release conditions; the b-number nightlies are separately marked Pre-release and kept moving the same morning the tag shipped (claims 1-4).
- Myth: A newer b-number is simply a newer version of 1.0. Reality: Nightlies build from master with -DLLAMA_BUILD_IS_DEV=ON; release tags build with -DLLAMA_BUILD_IS_DEV=OFF and are only cut when the internal ggml copy is identical to the released ggml (claim 6).
- Myth: Upgrading to 1.0 cannot break anything. Reality: v1.0.0 removes 35 deprecated functions from llama.h, so code built against the old public API stops compiling until it is updated (claim 7).

## Glossary

- **llama.cpp**: An open-source C/C++ engine, by ggml-org, that runs large language models on your own CPU or GPU.
- **tag (release tag)**: A named snapshot of the code at one commit, like v1.0.0, that a release is built from.
- **nightly build**: An automatic build cut from the master branch each day, named by its commit number, like b12360.
- **pre-release**: A build GitHub explicitly labels as not stable, which is what every b-number nightly is marked as.
- **master branch**: The development trunk of the project where every change lands first, before any release tag is cut.
- **pinning**: Fixing your install to one exact version so updates happen only when you choose them.
- **--HEAD (Homebrew)**: A Homebrew install option that builds the package from the newest development code instead of the stable formula.

## Unverified

- Whether the b12360 abort affects anything beyond CPU-only Intel systems with AMX; the issue was open and unreproduced by maintainers at fetch time.
- Whether and when Homebrew bumps its stable llama.cpp formula from 0.9.0 to 1.0.0.
- Any performance difference between v1.0.0 and b12360 on our own hardware; no first-party measurement exists yet.
- Whether more b-number pre-releases follow today; only b12359 and b12360 were tagged at fetch time.
- What the v1.0.0 release note's promised "More info at 3PM CET" announcement contains; it had not happened at fetch time.

## Suggested outline

1. This morning llama.cpp shipped v1.0.0, its first stable tag, and within the hour a user filed a crash report against b12360, the nightly cut one commit past the tag.
2. Two tracks now exist: the vX.Y.Z tag, built with the dev flag off and cut only when the internal ggml matches the released ggml, versus the b-number nightlies built from master and marked Pre-release.
3. Pin it tonight: check whether your install names a b-number, pour the stable tag deliberately, write the version down, and move to the next tag on purpose.

## Viewer situation

You've got llama.cpp running on your gaming PC or Mac and you update it by grabbing the newest build from the repo or Homebrew, so what you run day to day is a b-number nightly rather than a tagged release.

## Has process

true

- Check the build you are running and note whether it names a b-number or a vX.Y.Z tag (the llama.app menu shows it; a source build is whatever commit you cloned).
- Pin the tag deliberately: brew install llama.cpp for the stable formula, or download the v1.0.0 source archive from the release page instead of cloning master.
- If you build from source, clone the repo and check out the v1.0.0 tag before running cmake -B build.
- Write the exact version into your setup notes and move to the next vX.Y.Z tag on purpose, not to whatever b-number was newest today.

## Objection

One filed issue on one commit is not a broken release -- the abort is on CPU-only AMX systems, and pinning tags means waiting while new model support lands on master first.

## Sources

| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/ggml-org/llama.cpp/releases | Releases: ggml-org/llama.cpp | primary | web_extract | 2026-11-13 |
| 2 | https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0 | Release v1.0.0: ggml-org/llama.cpp | primary | web_extract | 2026-11-13 |
| 3 | https://github.com/ggml-org/llama.cpp/releases/tag/b12359 | Release b12359: ggml-org/llama.cpp | primary | web_extract | 2026-11-13 |
| 4 | https://github.com/ggml-org/llama.cpp/releases/tag/b12360 | Release b12360: ggml-org/llama.cpp | primary | web_extract | 2026-11-13 |
| 5 | https://github.com/ggml-org/ggml/discussions/1579 | dist : releases and versioning of ggml-org projects | primary | web_extract | 2026-11-13 |
| 6 | https://github.com/ggml-org/llama.cpp/pull/32190 | llama.cpp : bump version to 1.0.0 (PR #32190) | primary | web_extract | 2026-11-13 |
| 7 | https://github.com/ggml-org/llama.cpp/issues/32197 | DeepSeek-V4.1-Flash CPU/AMX scheduler abort (issue #32197) | primary | web_extract | 2026-11-13 |
| 8 | https://github.com/ggml-org/llama.cpp/issues/32198 | Hexagon MUL_MAT_ID inf/wrong values (issue #32198) | primary | web_extract | 2026-11-13 |
| 9 | https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md | Build llama.cpp locally (docs/build.md) | docs | web_extract | 2026-11-13 |
| 10 | https://llama.app/ | Llama: Your AI, on your computer | primary | web_extract | 2026-11-13 |
| 11 | https://formulae.brew.sh/formula/llama.cpp | Homebrew Formulae: llama.cpp | docs | web_extract | 2026-11-13 |

## Notes

Tool family: FireCrawl returned 402 (no credit), so discovery ran on web_search and every cited page was fetched with web_extract; 11 unique URLs fetched and cached under output/ as 01-11 *.md; one URL (the Homebrew formula page) was fetched twice because the cache layer did not persist the first result. Issue #32197's created_at timestamp was read from the GitHub issues API (api.github.com, same resource) via curl this session. Computed spans, derived from the verbatim timestamps in Key numbers: b12359 to b12360 tag span 5 minutes 30 seconds; v1.0.0 tag to issue #32197 opened 31 minutes. Conflict: GitHub's release banner clocks (10:02, 10:20, 10:21) disagree with the source-archive tag timestamps (09:09:55Z, 09:15:25Z, 10:20:13Z); the brief uses the archive timestamps because they are exact and attached to the tagged artifacts. Thin spot: no first-party measurement on our hardware, and the b12360 abort is one open issue on one CPU configuration, not a widely confirmed regression.
