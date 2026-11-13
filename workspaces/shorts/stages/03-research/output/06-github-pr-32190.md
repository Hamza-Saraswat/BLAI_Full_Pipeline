[Skip to content](https://github.com/ggml-org/llama.cpp/pull/32190#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/pull/32190) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/pull/32190) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/pull/32190) to refresh your session.Dismiss alert

{{ message }}

## Conversation

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=80&v=4)](https://github.com/ggerganov)

### ![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=48&v=4)**[ggerganov](https://github.com/ggerganov)**     commented   [1 hour agoNov 13, 2026](https://github.com/ggml-org/llama.cpp/pull/32190\#issue-6368054030)


Copy link


Copy Markdown

Member

## Overview

llama.cpp v1.0.0 removes the deprecated public API and promotes the NextN/speculative API to `llama.h`, adds OCP FP8 KV caches, a host-memory MoE expert cache with a configurable CPU share, and loading of external PLE shards. It adds three text architectures (Kimi-K3.1-Pro, Ripple and xing4\_0), drama-3 TTS, and MageVL-Cowork and Kimi-K3.1 vision, hardens `llama-server` (SSRF, CORS, DNS rebinding, MCP tool cancellation) and adds a `/v1/audio/speech` endpoint, ships a redesigned web UI with chat groups and a markdown editor, and updates `ggml` to v1.0.0.

### API changes

- llama.h: remove `llama_set_warmup`, 35 deprecated functions, `defrag_thold` and `--defrag-thold` ( [#30565](https://github.com/ggml-org/llama.cpp/pull/30565))
- llama.h: promote the NextN API from `llama-ext.h` and rename `llama_set_embd_state_src` to `llama_set_ctx_state_src` ( [#30565](https://github.com/ggml-org/llama.cpp/pull/30565))
- llama.h: add `moe_cache_size` and `moe_cache_cpu_share` to `llama_context_params` ( [#30966](https://github.com/ggml-org/llama.cpp/pull/30966))
- mtmd.h: add `MTMD_GEN_AUDIO_TYPE_DRAMA3` and `temp` in `mtmd_helper_gen_audio_inp` ( [#31613](https://github.com/ggml-org/llama.cpp/pull/31613), [#31655](https://github.com/ggml-org/llama.cpp/pull/31655))
- mtmd-helper.h: add `mtmd_helper_resampler` for streaming raw PCM at the model sample rate ( [#31964](https://github.com/ggml-org/llama.cpp/pull/31964))
- server: add the OpenAI-compatible `/v1/audio/speech` endpoint and a `temperature` option for `/tts` ( [#31763](https://github.com/ggml-org/llama.cpp/pull/31763), [#31655](https://github.com/ggml-org/llama.cpp/pull/31655))

### New models

- Kimi-K3.1-Pro: K3 with the full-attention MLA layers replaced by DSA ( [#31779](https://github.com/ggml-org/llama.cpp/pull/31779))
- Ripple-65B-Preview (`ricursive`): new dense 65B architecture, no new ops ( [#31692](https://github.com/ggml-org/llama.cpp/pull/31692))
- xing4\_0: mHC, MLA, MoE and MTP ( [#31589](https://github.com/ggml-org/llama.cpp/pull/31589))
- drama-3 TTS (fishaudio) ( [#31613](https://github.com/ggml-org/llama.cpp/pull/31613))

### Core changes

- FP8 KV caches (`-ctk/-ctv f8_e4m3`) with optional static per-tensor scales ( [#28392](https://github.com/ggml-org/llama.cpp/pull/28392))
- MoE cache: CPU share for misses, LRFU/ClassLRU replacement, no CPU wait on cached experts ( [#30966](https://github.com/ggml-org/llama.cpp/pull/30966), [#31233](https://github.com/ggml-org/llama.cpp/pull/31233), [#31888](https://github.com/ggml-org/llama.cpp/pull/31888))
- external PLE/engram loading from separate GGUF shards via `--shard`/`--ple` ( [#31185](https://github.com/ggml-org/llama.cpp/pull/31185))
- Windows unbuffered model load, mirroring the Linux DirectIO path ( [#26014](https://github.com/ggml-org/llama.cpp/pull/26014))
- reuse the backend scheduler and graph results across reserves, and skip unused graph metadata pages ( [#32009](https://github.com/ggml-org/llama.cpp/pull/32009), [#32089](https://github.com/ggml-org/llama.cpp/pull/32089), [#32043](https://github.com/ggml-org/llama.cpp/pull/32043))
- mark every sampling chain as a graph output to prevent output aliasing ( [#32015](https://github.com/ggml-org/llama.cpp/pull/32015))
- remove the non-fused GDN paths and the ubatch-dependent graph node budget ( [#32078](https://github.com/ggml-org/llama.cpp/pull/32078))
- store the MTP conv snapshots of every recurrent model in one `set_rows` ( [#31660](https://github.com/ggml-org/llama.cpp/pull/31660))
- per-model `build_rope` with a KV-shifting fix and tests ( [#31683](https://github.com/ggml-org/llama.cpp/pull/31683)); the model is a member of `llm_graph_context` ( [#31733](https://github.com/ggml-org/llama.cpp/pull/31733))
- fix on-device state copy sizes for quantized KV caches ( [#30541](https://github.com/ggml-org/llama.cpp/pull/30541))
- follow the reference precision of `ggml_prec_set_acc` call sites ( [#31851](https://github.com/ggml-org/llama.cpp/pull/31851))
- attach NVFP4 FFN scales in Granite and qwen2 ( [#31449](https://github.com/ggml-org/llama.cpp/pull/31449), [#31657](https://github.com/ggml-org/llama.cpp/pull/31657)); merge tensors on convert for qwen3.5 ( [#32102](https://github.com/ggml-org/llama.cpp/pull/32102))
- apply the iGPU lazy-mode fallback only when mmap is off ( [#31957](https://github.com/ggml-org/llama.cpp/pull/31957))
- fit: account for skipped NextN layers when setting `n_gpu_layers` ( [#31569](https://github.com/ggml-org/llama.cpp/pull/31569))
- jinja: chained comparisons and argument unpacking ( [#32072](https://github.com/ggml-org/llama.cpp/pull/32072)); TTS text normalization via the chat template ( [#32053](https://github.com/ggml-org/llama.cpp/pull/32053))
- chat: honor `response_format` in the qwen3-coder/deepseek/ministral3, Muse Spark and gemma4 parsers ( [#31956](https://github.com/ggml-org/llama.cpp/pull/31956), [#32017](https://github.com/ggml-org/llama.cpp/pull/32017), [#31915](https://github.com/ggml-org/llama.cpp/pull/31915))
- json-schema: fix `allOf` of plain types ( [#31834](https://github.com/ggml-org/llama.cpp/pull/31834)); escape control characters and sanitize invalid UTF-8 in tool arguments ( [#31937](https://github.com/ggml-org/llama.cpp/pull/31937), [#31861](https://github.com/ggml-org/llama.cpp/pull/31861))

### Multi-modality changes

- remove `clip.h` and consolidate the model/subcontext infrastructure into `mtmd` ( [#31865](https://github.com/ggml-org/llama.cpp/pull/31865))
- share the compute buffer among subcontexts to save memory for vision+audio+gen models ( [#31945](https://github.com/ggml-org/llama.cpp/pull/31945))
- compute log-mel in the graph instead of spawning threads per request ( [#31808](https://github.com/ggml-org/llama.cpp/pull/31808))
- support Gemma 4 streaming audio input ( [#31965](https://github.com/ggml-org/llama.cpp/pull/31965))
- support MageVL-Cowork ( [#31819](https://github.com/ggml-org/llama.cpp/pull/31819)) and Kimi-K3.1 vision ( [#31980](https://github.com/ggml-org/llama.cpp/pull/31980))
- require the projector and patch embedding tensors and a 2x2 spatial merge at load ( [#32129](https://github.com/ggml-org/llama.cpp/pull/32129), [#32130](https://github.com/ggml-org/llama.cpp/pull/32130))
- require an F32 position embedding for HunyuanVL and read the MiniCPM-V width from ne\[1\] ( [#32131](https://github.com/ggml-org/llama.cpp/pull/32131), [#32132](https://github.com/ggml-org/llama.cpp/pull/32132))

### Server changes

- security: add `--allow-unauthenticated-tools` and `--media-allow-private-urls` opt-ins ( [#32113](https://github.com/ggml-org/llama.cpp/pull/32113), [#32115](https://github.com/ggml-org/llama.cpp/pull/32115))
- security: fix `--cors-origins`, DNS rebinding, CORS proxy SSRF and child instance access ( [#32098](https://github.com/ggml-org/llama.cpp/pull/32098), [#32115](https://github.com/ggml-org/llama.cpp/pull/32115), [#32120](https://github.com/ggml-org/llama.cpp/pull/32120))
- restrict the `HF_TOKEN` to huggingface.co hosts ( [#31730](https://github.com/ggml-org/llama.cpp/pull/31730))
- cancel MCP tool calls on client disconnect or timeout and notify the MCP server ( [#32025](https://github.com/ggml-org/llama.cpp/pull/32025))
- keep the server awake while a request uses its state with `--sleep-idle-seconds` ( [#32133](https://github.com/ggml-org/llama.cpp/pull/32133))
- use reference-counted context checkpoints instead of deep copies ( [#30137](https://github.com/ggml-org/llama.cpp/pull/30137))
- visit parent slots before child slots for shared-prefix requests ( [#30779](https://github.com/ggml-org/llama.cpp/pull/30779))
- realtime API: send error events instead of crashing, reject non-object session updates, fix the output lang ( [#31632](https://github.com/ggml-org/llama.cpp/pull/31632), [#31714](https://github.com/ggml-org/llama.cpp/pull/31714), [#31982](https://github.com/ggml-org/llama.cpp/pull/31982))
- accept the top-level `response_format.schema` form and convert Responses `text.format` JSON schemas ( [#28697](https://github.com/ggml-org/llama.cpp/pull/28697), [#26145](https://github.com/ggml-org/llama.cpp/pull/26145))

### UI changes

- sidebar: fold, preview and rearrange sections ( [#31936](https://github.com/ggml-org/llama.cpp/pull/31936)) and gather chats into named groups ( [#32012](https://github.com/ggml-org/llama.cpp/pull/32012))
- move Models, MCP and Settings to a sidebar footer, with full-screen pages on phones ( [#32022](https://github.com/ggml-org/llama.cpp/pull/32022))
- mobile: native layout, safe areas and full-screen dialogs ( [#31949](https://github.com/ggml-org/llama.cpp/pull/31949))
- open the virtual keyboard in the chat editor on Android ( [#32060](https://github.com/ggml-org/llama.cpp/pull/32060))
- chat input: live-preview markdown editor that expands for long messages ( [#31955](https://github.com/ggml-org/llama.cpp/pull/31955), [#31973](https://github.com/ggml-org/llama.cpp/pull/31973))
- open the actions menu on right-click for chats, tabs, messages and models ( [#31545](https://github.com/ggml-org/llama.cpp/pull/31545))
- PDF attachments: show text and page thumbnails, stop endless conversion retries ( [#31468](https://github.com/ggml-org/llama.cpp/pull/31468))
- Discover: show audio capability from the mmproj ( [#31837](https://github.com/ggml-org/llama.cpp/pull/31837)) and keep downloads during search ( [#31467](https://github.com/ggml-org/llama.cpp/pull/31467))
- add a `search_chats` tool ( [#32051](https://github.com/ggml-org/llama.cpp/pull/32051)) and move the JS sandbox setting out of developer ( [#32054](https://github.com/ggml-org/llama.cpp/pull/32054))
- take the logo and favicons from the llama-brand package ( [#32039](https://github.com/ggml-org/llama.cpp/pull/32039), [#32112](https://github.com/ggml-org/llama.cpp/pull/32112))
- fix a hidden sidebar intercepting clicks ( [#31712](https://github.com/ggml-org/llama.cpp/pull/31712), [#32035](https://github.com/ggml-org/llama.cpp/pull/32035))

### ggml changes

- [v1.0.0](https://github.com/ggml-org/ggml/releases/tag/v1.0.0): ggml 1.0.0 prunes the deprecated public API and the legacy `DIAG_MASK` ops, adds configurable YaRN truncation and FP8 support, and brings broad performance work across backends: few-row quantized matmuls and MoE fusion on CUDA/Metal, a Vulkan prefill FlashAttention path, a device-side MoE scheduler on SYCL, decomposed Adreno FlashAttention in OpenCL, new WebGPU kernels, expanded Hexagon op coverage, and scheduler improvements that avoid uploading unused inputs.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/pull/32190).

🎉1tokinasin reacted with hooray emoji

All reactions

- 🎉1 reaction

[ggerganov](https://github.com/ggerganov)


added 2 commits
[2 hours agoNovember 13, 2026 10:38](https://github.com/ggml-org/llama.cpp/pull/32190#commits-pushed-9d83ef6)

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&v=4)](https://github.com/ggerganov)

`
          llama.cpp : bump version to 1.0.0
`

Verified

# Verified

This commit was signed with the committer’s **verified signature**.


[![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)](https://github.com/ggerganov)[ggerganov](https://github.com/ggerganov)
Georgi Gerganov


GPG key ID: 449E073F9DC10735

Verified
on Nov 13, 2026, 03:39 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits)

`
          9d83ef6
`

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&v=4)](https://github.com/ggerganov)

`
          readme : bump major version in link
` …

Verified

# Verified

This commit was signed with the committer’s **verified signature**.


[![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)](https://github.com/ggerganov)[ggerganov](https://github.com/ggerganov)
Georgi Gerganov


GPG key ID: 449E073F9DC10735

Verified
on Nov 13, 2026, 03:39 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits)

Loading

Loading status checks…

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/pull/32190).

`
          f45330a
`

```
[no ci]
```

[![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)](https://github.com/apps/github-actions)[github-actions](https://github.com/apps/github-actions) Bot

added
[documentation](https://github.com/ggml-org/llama.cpp/issues?q=state%3Aopen%20label%3Adocumentation) Improvements or additions to documentation [build](https://github.com/ggml-org/llama.cpp/issues?q=state%3Aopen%20label%3Abuild) Compilation issues

labels

[1 hour agoNov 13, 2026](https://github.com/ggml-org/llama.cpp/pull/32190#event-36009915133)

[![@danbev](https://avatars.githubusercontent.com/u/432351?s=80&u=01dbd5b0e6781f3cd3b69b8a5629aac12ef34add&v=4)](https://github.com/danbev)

### **[danbev](https://github.com/danbev)**     commented   [1 hour agoNov 13, 2026](https://github.com/ggml-org/llama.cpp/pull/32190\#issuecomment-6848501644)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/pull/32190).


Copy link


Copy Markdown

Member

|     |
| --- |
| Sorry about this, but we have the same issue in ggml for [examples/test-cmake](https://github.com/ggml-org/llama.cpp/blob/6859813352d80dd668d97c4ba68fd52149cf6bce/examples/test-cmake/CMakeLists.txt#L11).<br>I've tried the following locally which seems to work:<br>```<br>diff --git a/examples/test-cmake/CMakeLists.txt b/examples/test-cmake/CMakeLists.txt<br>index 6ceb3359e..340707ee7 100644<br>--- a/examples/test-cmake/CMakeLists.txt<br>+++ b/examples/test-cmake/CMakeLists.txt<br>@@ -8,7 +8,7 @@ option(LLAMA_TEST_USE_SUBDIR "Use add_subdirectory instead of find_package" OFF)<br> if(LLAMA_TEST_USE_SUBDIR)<br>     add_subdirectory(../../ llama.cpp)<br> else()<br>-    find_package(llama 0.1.0 REQUIRED)<br>+    find_package(llama CONFIG REQUIRED PATHS ${CMAKE_PREFIX_PATH} NO_DEFAULT_PATH)<br> endif()<br> <br> add_executable(test-cmake test-cmake.cpp)<br>```<br>I've opened [#32191](https://github.com/ggml-org/llama.cpp/pull/32191) to track this. |

👍1ggerganov reacted with thumbs up emoji

All reactions

- 👍1 reaction

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/pull/32190).

[![danbev](https://avatars.githubusercontent.com/u/432351?s=60&v=4)](https://github.com/danbev)

**[danbev](https://github.com/danbev)**

approved these changes

[1 hour agoNov 13, 2026](https://github.com/ggml-org/llama.cpp/pull/32190#pullrequestreview-5888485405)

[View reviewed changes](https://github.com/ggml-org/llama.cpp/pull/32190/files/f45330a067c70c37747d03a1c178defe0da4d9e5)

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&v=4)](https://github.com/ggerganov)

`
          examples : bump test-cmake version
` …

Verified

# Verified

This commit was signed with the committer’s **verified signature**.


[![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)](https://github.com/ggerganov)[ggerganov](https://github.com/ggerganov)
Georgi Gerganov


GPG key ID: 449E073F9DC10735

Verified
on Nov 13, 2026, 04:05 AM

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits)

Loading

Loading status checks…

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/pull/32190).

`
          f23103a
`

```
[no ci]
```

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&u=28314d364d7c28f8ec232fadb767970d3ad74e7b&v=4)](https://github.com/ggerganov)

[ggerganov](https://github.com/ggerganov)

requested a review
from a team
as a [code owner](https://github.com/ggml-org/llama.cpp/blob/6859813352d80dd668d97c4ba68fd52149cf6bce/CODEOWNERS#L41) [1 hour agoNovember 13, 2026 09:05](https://github.com/ggml-org/llama.cpp/pull/32190#event-36011170941)

[![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)](https://github.com/apps/github-actions)[github-actions](https://github.com/apps/github-actions) Bot

added
the [examples](https://github.com/ggml-org/llama.cpp/issues?q=state%3Aopen%20label%3Aexamples)
label

[1 hour agoNov 13, 2026](https://github.com/ggml-org/llama.cpp/pull/32190#event-36011209504)

Hide detailsView details

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&u=28314d364d7c28f8ec232fadb767970d3ad74e7b&v=4)](https://github.com/ggerganov)

[ggerganov](https://github.com/ggerganov)

merged commit [`4cda622`](https://github.com/ggml-org/llama.cpp/commit/4cda6227a01f395bbf96506258900dff39f42a67)
into

master[1 hour agoNov 13, 2026](https://github.com/ggml-org/llama.cpp/pull/32190#event-36011223347)

2 checks passed


2 checks passed

[![@github-actions[bot]](https://avatars.githubusercontent.com/in/15368?v=4)](https://github.com/apps/github-actions)

**video-demo-label**

[Details](https://github.com/ggml-org/llama.cpp/actions/runs/43398441503/job/131794993655)

[![@github-actions[bot]](https://avatars.githubusercontent.com/in/15368?v=4)](https://github.com/apps/github-actions)

**labeler**

[Details](https://github.com/ggml-org/llama.cpp/actions/runs/43398441572/job/131794993458)

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&u=28314d364d7c28f8ec232fadb767970d3ad74e7b&v=4)](https://github.com/ggerganov)

[ggerganov](https://github.com/ggerganov)


deleted the

llama-rc-v1.0.0

branch

[1 hour agoNovember 13, 2026 09:06](https://github.com/ggml-org/llama.cpp/pull/32190#event-36011237622)

[![@leehack](https://avatars.githubusercontent.com/u/1233094?s=40&v=4)](https://github.com/leehack)[leehack](https://github.com/leehack)

mentioned this pull request
[30 minutes agoNov 13, 2026](https://github.com/ggml-org/llama.cpp/pull/32190#ref-issue-5863430955)

[Qualify post-v0.6.0 upstream correctness fixes and consumer compatibility\\
leehack/llamadart-native#112](https://github.com/leehack/llamadart-native/issues/112)

Open

3 of 6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://github.com/ggml-org/llama.cpp/pull/32190)

[Sign up for free](https://github.com/join?source=comment-repo) **to join this conversation on GitHub**.
Already have an account?
[Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fggml-org%2Fllama.cpp%2Fpull%2F32190)

### Reviewers

[![@danbev](https://avatars.githubusercontent.com/u/432351?s=40&v=4)](https://github.com/danbev)[danbev](https://github.com/danbev)danbev approved these changes

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/pull/32190).

### Assignees

No one assigned

### Labels

[build](https://github.com/ggml-org/llama.cpp/issues?q=state%3Aopen%20label%3Abuild) Compilation issues [documentation](https://github.com/ggml-org/llama.cpp/issues?q=state%3Aopen%20label%3Adocumentation) Improvements or additions to documentation [examples](https://github.com/ggml-org/llama.cpp/issues?q=state%3Aopen%20label%3Aexamples)

### Projects

None yet

### Milestone

No milestone

### Development

Successfully merging this pull request may close these issues.

None yet

### 2 participants

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=52&v=4)](https://github.com/ggerganov)[![@danbev](https://avatars.githubusercontent.com/u/432351?s=52&v=4)](https://github.com/danbev)

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

You can’t perform that action at this time.