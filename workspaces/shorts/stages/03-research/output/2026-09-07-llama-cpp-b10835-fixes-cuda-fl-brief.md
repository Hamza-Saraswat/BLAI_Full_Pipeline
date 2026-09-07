---
slug: 2026-09-07-llama-cpp-b10835-fixes-cuda-fl
stage: 03-research
topic: "llama.cpp release b10835 fixes a divergent barrier in CUDA f16 flash attention; NVIDIA GPU owners should update tonight"
depth: standard
generated_at: 2026-09-07T11:37:48Z
sources: 12
hub: "[[videos/2026-09-07-llama-cpp-b10835-fixes-cuda-fl]]"
---

# Research brief: llama.cpp release b10835 fixes a divergent barrier in CUDA f16 flash attention; NVIDIA GPU owners should update tonight

## Summary
llama.cpp shipped release b10835 the morning of Sep 7, 2026 carrying exactly one fix: a divergent block-wide barrier in the CUDA f16 flash attention kernel, patched by PR #27870 after issue #27678 flagged it. The most arresting number is the verification: compute-sanitizer went from "3232 errors before and 0 after this fix" on an RTX 5090, with the original reporter's attached run showing "4000 errors". The strongest concrete case is the rhythm of the morning: b10834 at 07 Sep 07:18, b10835 at 07 Sep 08:08, b10837 at 07 Sep 08:35 -- three releases inside 77 minutes, one of them this fix. What could not be verified: no fetched page documents a user seeing garbled text from this specific barrier; the evidence is sanitizer errors (undefined behavior) plus separate flash-attn crash reports, so "wrong output" must stay hedged. Source conflict: the ideas framing says "three releases in four hours", but the fetched release pages timestamp the span at 07:18 to 08:35; trust the release pages.

## Thesis
On the morning of Sep 7, 2026, llama.cpp release b10835 fixed a divergent barrier that has lurked in the CUDA f16 flash attention kernel since the original native-MMA implementation, dropping compute-sanitizer errors from 3232 to 0, and NVIDIA GPU owners should update tonight.

## Explanation path
Start with what the viewer already runs: llama.cpp is the engine underneath the local-AI world, and apps like LM Studio and Ollama bundle it, so "I don't use llama.cpp" is almost never true. Then name flash attention: the trick that computes the model's attention step as one fused kernel, skipping a huge intermediate write to video memory -- same math, less memory, which is why the -fa flag is famous as a speed-and-VRAM tweak. The catch the video lands: inside the CUDA version of that kernel sits a barrier, a checkpoint every thread in a block must reach, and NVIDIA requires every thread execute the exact same barrier instruction. Since the first native-MMA kernel (PR #11583, Feb 1, 2025), one barrier sat inside a branch only some threads enter, which CUDA calls undefined behavior. Establish how it was caught and fixed: a synccheck run on an RTX 4070 reported thousands of divergent-barrier errors, PR #27870 moved the synchronization out of the branch, and errors went to zero with no measurable performance cost. Close on the update-tonight action: check your build number, grab the b10835 prebuilt binary for your GPU or rebuild with GGML_CUDA=ON, and know that LM Studio and Ollama users inherit the fix only when those apps bump their bundled engine.

## Claims
1. **Release b10835, published 07 Sep 08:08 as a Pre-release at commit b74f590, exists to ship one change titled "ggml-cuda: fix divergent barrier in f16 flash attention (#27870)" (plus a follow-up "ggml-cuda: avoid duplicate metadata pointer setup").**
   - Source: Release b10835, https://github.com/ggml-org/llama.cpp/releases/tag/b10835
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "ggml-cuda: fix divergent barrier in f16 flash attention ( [#27870](https://github.com/ggml-org/llama.cpp/pull/27870)) - ggml-cuda: avoid duplicate metadata pointer setup"
2. **The root cause was a block-wide `__syncthreads()` sitting inside the `threadIdx.y % np == 0` branch of the `flash_attn_ext_f16_process_tile` kernel, so not all threads reached the same barrier; PR #27870 moved the synchronization out of the branch while keeping the metadata work on the intended warps.**
   - Source: PR #27870 "ggml-cuda: fix divergent barrier in f16 flash attention", https://github.com/ggml-org/llama.cpp/pull/27870
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "I moved the block-wide synchronization out of the `threadIdx.y % np == 0` branch so all threads in the `np > 1` case reach the same `__syncthreads()`, while keeping the metadata calculation and SHMEM writeback limited to the intended warps."
3. **The fix is tool-verified: compute-sanitizer synccheck showed thousands of divergent-barrier errors on the flash attention op, and the PR author measured "3232 errors before and 0 after this fix" reproducing on an RTX 5090, CUDA 13.3, driver 610.43.02.**
   - Source: PR #27870, https://github.com/ggml-org/llama.cpp/pull/27870
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "compute-sanitizer reports 3232 errors before and 0 after this fix."
4. **This was not a fresh regression: issue #27678 (opened Aug 24, 2026 by a reporter on build 10615, RTX 4070, CUDA toolkit 13.3.73, driver 610.57.04, attached run reporting "4000 errors") traces the warp-dependent barrier to the original native MMA FlashAttention implementation, introduced in commit 864a0b6 / PR #11583, and a maintainer confirmed against the CUDA docs that treating two different `__syncthreads` instances as interchangeable "is therefore **not** correct".**
   - Source: Issue #27678, https://github.com/ggml-org/llama.cpp/issues/27678
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "The affected native MMA FlashAttention implementation was introduced in commit 864a0b6, PR #11583"
5. **The scope is the NVIDIA CUDA backend with f16 flash attention: first reported on RTX 4070 (CUDA toolkit 13.3.73, driver 610.57.04), then reproduced, fixed, and tested on RTX 5090 (CUDA 13.3, driver 610.43.02), with the fix confirmed on the report thread as "0 errors in 10/10 runs".**
   - Source: PR #27870, https://github.com/ggml-org/llama.cpp/pull/27870
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "The issue was initially reported on RTX 4070, CUDA toolkit 13.3.73, driver 610.57.04. I was able to reproduce, fix, and test the fix on RTX 5090, CUDA 13.3, driver 610.43.02."
6. **The fix costs nothing in speed: on Qwen3.8-27B-UD-Q4_K_XL.gguf with FlashAttention enabled at context depth 100k, pp512 moved from 1390.27 ± 21.66 to 1388.10 ± 21.43 t/s (-0.15%) and tg128 from 59.75 ± 0.06 to 59.73 ± 0.05 t/s (-0.03%), so the PR concludes "No measurable performance regression."**
   - Source: PR #27870, https://github.com/ggml-org/llama.cpp/pull/27870
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "Therefore, **No measurable performance regression.**"
7. **b10834, published 07 Sep 07:18 at commit 992cb50, shipped "ggml: allow backend inputs to not create another split (#28387)" -- the release immediately before the fix.**
   - Source: Release b10834, https://github.com/ggml-org/llama.cpp/releases/tag/b10834
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "ggml: allow backend inputs to not create another split ( [#28387](https://github.com/ggml-org/llama.cpp/pull/28387))"
8. **b10837, published 07 Sep 08:35 at commit 5202104, shipped "caps : recheck typed content if template checks for string (#28511)" -- 77 minutes after b10834, making it three releases in one morning with the fix in the middle.**
   - Source: Release b10837, https://github.com/ggml-org/llama.cpp/releases/tag/b10837
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "caps : recheck typed content if template checks for string ( [#28511](https://github.com/ggml-org/llama.cpp/pull/28511))"
9. **Turning flash attention off has been the classic escape hatch for CUDA flash-attn-path faults: issue #26609 documents a deterministic "CUDA error: an illegal memory access" on Qwen3.6-35B MoE across release builds b10107, b10243, and b10488 that "disappears with -fa off".**
   - Source: Issue #26609, https://github.com/ggml-org/llama.cpp/issues/26609
   - Tier: primary | Confidence: high | Accessed: 2026-09-07 | Via: web_extract
   - Quote: "The crash is **deterministic** (reproduced 5+ times across two builds) and **disappears with `--flash-attn off`**."
10. **Viewers can be exposed without running llama.cpp directly: LM Studio "supports running LLMs on Mac, Windows, and Linux using llama.cpp" through managed runtimes, and Ollama's repository vendors llama.cpp (an `llama` directory with a `LLAMA_CPP_VERSION` file) whose latest visible version bump is b10760 (#18199) -- older than the b10835 fix.**
    - Source: Welcome to LM Studio Docs!, https://lmstudio.ai/docs/app (and https://github.com/ollama/ollama)
    - Tier: docs | Confidence: medium | Accessed: 2026-09-07 | Via: web_extract

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | compute-sanitizer divergent-barrier errors, before vs after fix (RTX 5090, CUDA 13.3) | 3232 errors before and 0 after this fix | https://github.com/ggml-org/llama.cpp/pull/27870 | "compute-sanitizer reports 3232 errors before and 0 after this fix." |
| 2 | compute-sanitizer ERROR SUMMARY in the original attached run (RTX 4070, build 10615) | 4000 errors | https://github.com/ggml-org/llama.cpp/issues/27678 | "The sanitizer reports thousands of divergent-barrier errors; the attached run reports 4000 errors." |
| 3 | b10834 publish timestamp | 07 Sep 07:18 | https://github.com/ggml-org/llama.cpp/releases/tag/b10834 | "released this 4 hours ago 07 Sep 07:18" |
| 4 | b10835 publish timestamp | 07 Sep 08:08 | https://github.com/ggml-org/llama.cpp/releases/tag/b10835 | "released this 3 hours ago 07 Sep 08:08" |
| 5 | b10837 publish timestamp | 07 Sep 08:35 | https://github.com/ggml-org/llama.cpp/releases/tag/b10837 | "released this 31 minutes ago 07 Sep 08:35" |
| 6 | pp512 @ d100000 before vs after fix, Qwen3.8-27B-UD-Q4_K_XL.gguf, FlashAttention enabled | 1390.27 ± 21.66 -> 1388.10 ± 21.43 t/s (-0.15%) | https://github.com/ggml-org/llama.cpp/pull/27870 | "pp512 @ d100000 (t/s) | 1390.27 ± 21.66 | 1388.10 ± 21.43 | -0.15%" |
| 7 | Ollama's bundled llama.cpp, latest visible version bump on its repo page | b10760 | https://github.com/ollama/ollama | "llama.cpp: version bump b10760 (#18199)" |

## Analogy candidates
- **Vehicle: every worker must clock into the same checkpoint.** Mapping: a CUDA barrier (`__syncthreads()`) is a checkpoint every thread in a block has to hit before anyone continues; the code only told the threads matching `threadIdx.y % np == 0` about it, so the checkpoint jams -- NVIDIA's rule is that all threads must execute the exact same barrier instruction. Breaks when: a jammed checkpoint is loud and visible, while a divergent barrier is undefined behavior -- it can mean wrong numbers, a hang, or nothing observable at all.
- **Vehicle: doing the arithmetic in your head instead of photocopying the whole spreadsheet.** Mapping: standard attention writes a huge intermediate matrix to slow video memory between steps; flash attention fuses the steps and keeps tiles in fast on-chip memory -- same result, shorter path. Breaks when: unlike a mental shortcut this is not an approximation, the math is identical; that is exactly why a bug here threatens correctness rather than speed.

## Misconceptions
- Myth: garbled output means my model file or my quant is corrupt. Reality: this fault lived in llama.cpp's CUDA kernel, not in the .gguf file; the engine mis-executes attention, so replacing the binary, not re-downloading the model, is the fix (claims 1, 2, 9).
- Myth: flash attention is only a speed tweak, so a bug in it just makes things slower. Reality: flash attention reroutes attention through memory with identical math, and the fix measured "No measurable performance regression" (pp512 -0.15%); the danger was correctness -- undefined behavior from a broken barrier (claims 2, 6).
- Myth: I use LM Studio or Ollama, so llama.cpp news is not about me. Reality: LM Studio runs models "using llama.cpp" and Ollama's repo carries a vendored llama.cpp whose latest visible bump is b10760; those apps inherit the fix only when they bump their bundled engine (claim 10).

## Glossary
- **llama.cpp**: the open-source C/C++ engine that runs model files locally, and the engine bundled underneath apps like LM Studio and Ollama.
- **CUDA**: NVIDIA's layer for running computation on its GPUs; a CUDA bug affects NVIDIA graphics cards, not Macs or AMD cards.
- **flash attention**: a way of computing the model's attention step as one fused kernel that skips writing a huge intermediate matrix to video memory; same math, less memory.
- **f16**: half-precision 16-bit floating point, the number format this attention kernel computes in.
- **barrier (`__syncthreads()`)**: a checkpoint inside a CUDA program that every thread in a block must reach before any of them continue.
- **divergent barrier**: the failure where only some threads reach a given barrier, which CUDA's rules define as undefined behavior.
- **compute-sanitizer**: NVIDIA's checking tool for GPU code; its synccheck mode is what reported the thousands of barrier errors.
- **build number (like b10835)**: llama.cpp's numbered rolling builds; the b-number in your startup line tells you whether you have the fix.
- **quantization**: shrinking a model file to fewer bits so it fits in video memory; often blamed for corruption, but this bug was in the engine, not the file.

## Unverified
- No fetched page shows a user seeing garbled or wrong text specifically from this divergent barrier; the grounded evidence is sanitizer errors (undefined behavior) plus separate flash-attn crash reports, so narration must hedge wrong output as a risk, not a documented symptom.
- Whether this barrier is the root cause of the watchdog stalls in issue #27102 is only a collaborator's open question, not a conclusion.
- The timezone behind the displayed "07 Sep 07:18 / 08:08 / 08:35" timestamps is unknown (GitHub renders viewer-local times); the Sep 7, 2026 date is corroborated by the pages.
- Which llama.cpp version first turned flash attention on by default for CUDA; the benchmark states current builds default it on but names no version.
- LM Studio's exact bundled llama.cpp build number tonight; its engines docs page returned 404 and the fetched docs page names no build number.
- The ideas-note framing of "three releases in four hours"; the fetched release pages show a 77-minute span (07:18 to 08:35), which is what the narration should use.

## Suggested outline
1. b10835 landed this morning at 07 Sep 08:08, sandwiched between b10834 (07:18) and b10837 (08:35) -- three releases in 77 minutes, and the middle one exists to fix a single bug: a divergent barrier in CUDA f16 flash attention, with sanitizer errors falling from 3232 to 0.
2. What flash attention is and why this is a correctness bug, not a speed bug: the fused kernel that skips the giant intermediate write, the rule that every thread must hit the exact same barrier, and the branch that has broken that rule since the original kernel shipped in PR #11583 on Feb 1, 2025.
3. What you do tonight: check the build number your tool prints, grab the b10835 prebuilt for your GPU or rebuild with -DGGML_CUDA=ON, and if you sit behind LM Studio or Ollama, watch for their engine bump (Ollama's page shows b10760).

## Viewer situation
You run a local model on your NVIDIA gaming GPU through llama.cpp, LM Studio, or Ollama, your copy is older than b10835, and you have not updated it tonight.

## Has process
`true`
- Check the build number your tool prints at startup (llama.cpp reports build N; the bug report shows "build 10615") or your app's runtime panel.
- Download the b10835 prebuilt for your GPU from the releases page (for example the Windows x64 CUDA 12 or CUDA 13 zip) or run git pull and rebuild with `cmake -B build -DGGML_CUDA=ON`.
- Replace the old binary or restart the server so the new build loads.
- Confirm the startup line now reports the new build number, 10835.

## Objection
A divergent barrier is undefined behavior, not a proven wrong-answer generator, and no fetched case shows garbled text from this exact bug -- update for the hygiene and the crash-adjacent reports, but do not tell viewers their old outputs were garbage.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/ggml-org/llama.cpp/releases/tag/b10835 | Release b10835 - ggml-org/llama.cpp | primary | web_extract | 2026-09-07 |
| 2 | https://github.com/ggml-org/llama.cpp/pull/27870 | ggml-cuda: fix divergent barrier in f16 flash attention (PR #27870) | primary | web_extract | 2026-09-07 |
| 3 | https://github.com/ggml-org/llama.cpp/issues/27678 | Misc. bug: CUDA FlashAttention synccheck reports divergent __syncthreads (Issue #27678) | primary | web_extract | 2026-09-07 |
| 4 | https://github.com/ggml-org/llama.cpp/releases/tag/b10834 | Release b10834 - ggml-org/llama.cpp | primary | web_extract | 2026-09-07 |
| 5 | https://github.com/ggml-org/llama.cpp/releases/tag/b10837 | Release b10837 - ggml-org/llama.cpp | primary | web_extract | 2026-09-07 |
| 6 | https://github.com/ggml-org/llama.cpp/issues/26609 | CUDA illegal memory access in cudaStreamSynchronize (flash-attn path) with Qwen3.6-35B MoE + partial expert offload, deterministic, cross-build (b10107, b10243); disappears with -fa off (Issue #26609) | primary | web_extract | 2026-09-07 |
| 7 | https://github.com/ggml-org/llama.cpp/issues/27102 | Eval bug: CUDA kernel stall during model execution, killed by watchdog (Issue #27102) | primary | web_extract | 2026-09-07 |
| 8 | https://github.com/ggml-org/llama.cpp | ggml-org/llama.cpp: LLM inference in C/C++ (README) | primary | web_extract | 2026-09-07 |
| 9 | https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md | llama.cpp docs/build.md (Build llama.cpp locally, CUDA section) | docs | web_extract | 2026-09-07 |
| 10 | https://inventivehq.com/blog/flash-attention-llama-cpp-benchmark | Flash Attention in llama.cpp: -fa Is Free Because It's Already On | benchmark | web_extract | 2026-09-07 |
| 11 | https://github.com/ollama/ollama | ollama/ollama (repository, llama.cpp vendored as llama/ with LLAMA_CPP_VERSION) | primary | web_extract | 2026-09-07 |
| 12 | https://lmstudio.ai/docs/app | Welcome to LM Studio Docs! | docs | web_extract | 2026-09-07 |

## Notes
- Timestamp conflict: the ideas framing says three releases in about four hours; the fetched release pages show b10834 at 07 Sep 07:18 and b10837 at 07 Sep 08:35, a 77-minute span. Trust the release pages and say 77 minutes, not four hours.
- Numbering nuance: #27870 is the fixing pull request; the underlying bug report is issue #27678 (both fetched). Do not call #27870 an issue on screen.
- Claim 10 spans two sources (LM Studio docs for the bundle statement, Ollama repo for b10760); the JSON cites the LM Studio docs URL, and both URLs appear in the Sources table.
- Ollama's b10760 is read from the latest visible commit touching its LLAMA_CPP_VERSION file on the fetched repo page; treat as "at least b10760, dated before the fix", medium confidence.
- The llama.cpp engines page for LM Studio (lmstudio.ai/docs/app/engines) returned 404 this session; the general docs page grounds the bundling statement instead.
- Update path is grounded: the b10835 release page lists prebuilt Windows x64 CUDA 12 (12.4) and CUDA 13 (13.3) zips, and docs/build.md gives `cmake -B build -DGGML_CUDA=ON` plus `cmake --build build --config Release`.

## Decisions
Research checkpoint (unattended): angle confirmed -- b10835 fixes the divergent barrier in CUDA f16 flash attention (#27870), update-tonight classic; slug unchanged.
Why: ideas note pick 1 (opportunity 87.4) names the one-fact story; no swap requested.
