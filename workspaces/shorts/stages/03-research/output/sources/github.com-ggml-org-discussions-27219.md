# Source: https://github.com/ggml-org/llama.cpp/discussions/27219
# Fetched: 2026-11-27 via web_extract

[Skip to content](https://github.com/ggml-org/llama.cpp/discussions/27219#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/discussions/27219) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/discussions/27219) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/discussions/27219) to refresh your session.Dismiss alert

{{ message }}

# RFC: Adding a native AMD ggml-hrx backend  \#27219

[stellaraccident](https://github.com/stellaraccident)

started this conversation in
[General](https://github.com/ggml-org/llama.cpp/discussions/categories/general)

[RFC: Adding a native AMD ggml-hrx backend](https://github.com/ggml-org/llama.cpp/discussions/27219#top)#27219

[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=40&v=4)\\
stellaraccident](https://github.com/stellaraccident)

on Aug 16Aug 17, 2026·
22 comments
·
29 replies


[Return to top](https://github.com/ggml-org/llama.cpp/discussions/27219#top)

Discussion options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

## [![](https://avatars.githubusercontent.com/u/494208?s=64&v=4)\ stellaraccident](https://github.com/stellaraccident) [on Aug 16Aug 17, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussion-10629329)

|     |
| --- |
| (see draft PR: [#27218](https://github.com/ggml-org/llama.cpp/pull/27218))<br>At AMD, we are actively optimizing AMD GPU performance in llama.cpp under the existing Vulkan and HIP (CUDA-derived) backends. However, as ROCm matures on client systems, we have repeatedly run into the costs of not having AMD native backends and optimized client libraries that can be independently optimized for the best possible performance of the GPUs and NPUs on our silicon. In addition, as ROCm was originally developed primarily to service the datacenter market, it often faces headwinds when trying to integrate and deploy to client operating systems in a way that best meets the needs there. As a result, we have been working on a lighter, more focused subset of ROCm that is optimized for these use cases. We call this [HRX](https://github.com/ROCm/hrx-system), and we have been co-developing it with the needs of a dedicated llama.cpp backend for a couple of months, for eventual inclusion into ROCm proper as a focused, redistributable set of libraries.<br>While the work is still early, we wanted to discuss with the community the possibility of finishing this work and landing it as a new ggml-hrx backend in llama.cpp. While we have done a lot of experimental work to optimize this backend for a wide swath of models and use cases, we decided that for an initial debut and discussion, we would focus the contribution on a minimal kernel library sufficient to run the unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF Q4\_K\_M model performantly on RDNA3 (W7900) and RDNA3.5 (Strix Halo). This RFC PR carries that minimum set, and we will continue to develop the branch for wide model, operating system, and system coverage.<br>## HRX Technology<br>The HRX technology that underpins the ggml-hrx backend is optimized for client deployment use cases:<br>- Small [libhrx runtime library](https://github.com/ROCm/hrx-system/blob/main/libhrx/include/hrx_runtime.h) (~2MiB) that depends on a minimal set of ROCm system components for interfacing with the device drivers and profiler. Leverages features in our Radeon GPUs to lower per-dispatch overhead to similar levels as is seen in the graphics pipelines.<br>- Native low-level, explicit, command-buffer based API as the primary API for libhrx for new integrations.<br>- Optional HIP API compatibility on top of libhrx (not used in ggml-hrx but available for systems looking to migrate incrementally and presently at 88% HIP API compliance).<br>- [Real-time Embedded Loom JIT compiler](https://rocm.github.io/hrx-system/loom/) capable of specializing and optimizing kernels for the exact hardware on a machine to HSACO in ~1-15 milliseconds, putting it in the range of being able to JIT all kernels for all architectures instead of needing to ship pre-compiled kernel libraries.<br>- No dependency on pre-compiled ROCm kernel libraries, large downloads, etc.<br>- Builds on our Linux/Windows driver unification work to have the same execution path on both Linux and Windows.<br>## Performance<br>We are not going to cite absolute performance comparisons on this early work. Our existing published metrics and deployment paths remain our recommended way to get the best performance from llama.cpp on our hardware as this backend continues to evolve.<br>With that said, the performance benefits of this new technology are real. Compared to the faster between the existing Vulkan and HIP ggml backends, we are routinely achieving on the order of:<br>- 30-50% tok/s uplift on prefill<br>- Parity to 15% tok/s uplift on non-MTP decode (heavily dependent on the exact card and memory system behavior with non-MTP being the most overhead sensitive path which we benchmark)<br>Further, the simplicity and vertical integration of the HRX stack makes exploiting performance advantages of specific cards much easier, compared with attempting to isolate performance improvements in the existing ROCm stack, which often has different historic optimization goals and many more software layers.<br>As we land more of the work for coverage and features, we will publish absolute benchmark claims. For now, this boilerplate PR was formulated to have the bare minimum to meet functionality and demonstrate single model/use-case performance on Strix Halo and W7900 to show viability without trying to land a full-coverage backend in one patch.<br>## Build and Size<br>All in, the ggml-hrx backend presently adds ~32MiB on-disk/stripped above a CPU-only llama.cpp backend. It is standalone, requiring no additional software installation beyond AMD GPU drivers. We expect this number to decrease as some of the ROCm driver interface components are optimized for this use case.<br>On a 16-core/32-thread Ryzen AI MAX+ 395, a clean, uncached Release build with the HRX backend enabled completes in approximately one minute. This includes libhrx, the Loom compiler, ggml-hrx, llama.cpp itself, and kernel bundling for the JIT compiler. We expect that these numbers will grow upward somewhat with full coverage of models and systems, but the delta should be incremental.<br>At this footprint and build time, ordinary contributors can work across all of our software, directly as part of the final project, without high end build systems or the overheads and distribution complexity traditionally assumed to come with depending on software like ROCm.<br>## Next Steps<br>We have biased this initial submission to be structurally minimal. As such, once landed, much of the work involves landing pre-work that has already been done for other models and GPUs:<br>- Integrate with upstream CI and release process<br>- Land Qwen 3.8 coverage from the side branch (already showing performance uplift)<br>- Incrementally extend model and GPU coverage to include everything that the current backends support<br>- Productionize our static Windows build recipe (currently can generate a completely static/self-contained 26.1MiB llama.exe)<br>## Disclosure on AI Use<br>Per project policies, we are disclosing that significant portions of this project have been built with the assistance of AI. Specific models vary by contributor, but Codex with Sol was most commonly used for the ggml-hrx backend itself. The code was meticulously reviewed, revised and tested by hand in order to produce an implementation that should fit in with the rest of the project and that the contributors can explain and defend in detail. The kernels were heavily tuned and optimized through many rounds of our automated kernel tuning technology, which we will share more about at a later date.<br>Co-authored-by: Rob Suderman [Robert.Suderman@amd.com](mailto:Robert.Suderman@amd.com)<br>Co-authored-by: Ben Vanik [Ben.Vanik@amd.com](mailto:Ben.Vanik@amd.com)<br>Co-authored-by: Aryaman Vasishta [Aaryaman.Vasishta@amd.com](mailto:Aaryaman.Vasishta@amd.com)<br>Co-authored-by: Stella Laurenzo [slaurenz@amd.com](mailto:slaurenz@amd.com) |

20You must be logged in to vote

👍1❤️28🚀4👀7

All reactions

- 👍1
- ❤️28
- 🚀4
- 👀7

## Replies:   22 comments  ·  29 replies

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/2290863?s=64&v=4)\ inforithmics](https://github.com/inforithmics) [on Aug 17Aug 17, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18047326)

|     |
| --- |
| Is there a document that describes the architecture of the backend? because looking at the code files it seems that the backend optimizes by model architecture. Would be interested to know how it is done without looking through the code. |

1You must be logged in to vote

All reactions

3 replies


[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=60&v=4)](https://github.com/stellaraccident)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

#### [stellaraccident](https://github.com/stellaraccident) [on Aug 17Aug 17, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18053678)   Author

|     |
| --- |
| > Is there a document that describes the architecture of the backend? because looking at the code files it seems that the backend optimizes by model architecture. Would be interested to know how it is done without looking through the code.<br>We have a design doc that we used amongst ourselves for this. Let me get it cleaned up/current and post it today. Most of what is in this initial branch are fusions that should generalize pretty well to adjacent model families (although some of them still carry the "qwen" prefix, which is what they were optimized against). What we left out of this branch was the long-tail, single kernel coverage for all claimed ops. We included a couple of those in this submission to illustrate the point, but these are fairly mechanical/bulky to implement and we opted to save all of them for a followup. |

All reactions

[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=60&v=4)](https://github.com/stellaraccident)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [stellaraccident](https://github.com/stellaraccident) [on Aug 18Aug 18, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18060123)   Author

|     |
| --- |
| I'm attaching an AI generated document that summarizes our original design doc and provides some of the design thinking and history/rejected alternatives.<br>[hrx-backend-architecture.md](https://github.com/user-attachments/files/31165074/hrx-backend-architecture.md)<br>(the summary is basically what I said above) |

All reactions

[![@inforithmics](https://avatars.githubusercontent.com/u/2290863?s=60&v=4)](https://github.com/inforithmics)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

#### [inforithmics](https://github.com/inforithmics) [on Aug 18Aug 18, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18060361)

|     |
| --- |
| Thanks a Lot, this is very sophisticated/advanced/clever technology. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/264964?s=64&v=4)\ Geramy](https://github.com/Geramy) [on Aug 17Aug 17, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18055463)

|     |
| --- |
| > On a 16-core/32-thread Ryzen AI MAX+ 395, a clean, uncached Release build with the HRX backend enabled completes in approximately one minute.<br>That's crazy amazing! |

2You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/631764?s=64&v=4)\ neuhaus](https://github.com/neuhaus) [on Aug 18Aug 18, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18068472)

|     |
| --- |
| Sounds great! Will it also support clustering more than one Strix Halo system?<br>With Nvidia Spark and Apple being competitors offering RDMA tensor parallelism, this is an important aspect. |

1You must be logged in to vote

👀2

All reactions

- 👀2

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/5508949?s=64&v=4)\ rsuderman](https://github.com/rsuderman) [on Aug 20Aug 20, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18099270)

|     |
| --- |
| For those interested in building and running:<br>```<br>git clone --depth 1 --branch users/stella/hrx-rfc-v1 https://github.com/AMD-Ecosystem/llama.cpp<br>git clone -b main https://github.com/ROCm/hrx-system<br>cd hrx-system<br>git checkout 8ef82dbfa0385f7953ceadd884317be7e512ea38<br>cd ..<br>mkdir build<br>cmake -G Ninja -B build -S llama.cpp -DGGML_HRX=ON -DHRX_SOURCE_DIR=hrx-system<br>cmake --build build<br>```<br>To execute you will need access to a W7900 or AI Max+ 395. You can observe the available device via the llama-cli when built with the HRX backend enabled.<br>```<br>build/bin/llama-cli --list-devices<br>``` |

2You must be logged in to vote

👍1

All reactions

- 👍1

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/2290863?s=64&v=4)\ inforithmics](https://github.com/inforithmics) [on Aug 24Aug 24, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18140128)

|     |
| --- |
| I had to adapt the build so that it took the clang from rocm<br>```<br>git clone --depth 1 --branch users/stella/hrx-rfc-v1 https://github.com/AMD-Ecosystem/llama.cpp<br>git clone -b main https://github.com/ROCm/hrx-system<br>cd hrx-system<br>git checkout 8ef82dbfa0385f7953ceadd884317be7e512ea38<br>cd ..<br>mkdir build<br>export ROCM_PATH=/opt/rocm<br>export CC="$ROCM_PATH/llvm/bin/clang"<br>export CXX="$ROCM_PATH/llvm/bin/clang++"<br>cmake -G Ninja -B build -S llama.cpp \<br>  -DGGML_HRX=ON \<br>  -DHRX_SOURCE_DIR=hrx-system \<br>  -DCMAKE_BUILD_TYPE=Release \<br>  -DCMAKE_C_COMPILER="$CC" \<br>  -DCMAKE_CXX_COMPILER="$CXX" \<br>  -DIREE_ROCM_PATH="$ROCM_PATH"<br>cmake --build build<br>```<br>The build took me 1m and 6s. Because I have only a GFX1150 iGPU I cannot test if it would work. |

1You must be logged in to vote

All reactions

2 replies


[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=60&v=4)](https://github.com/stellaraccident)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

#### [stellaraccident](https://github.com/stellaraccident) [on Aug 24Aug 24, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18140215)   Author

|     |
| --- |
| Thanks. We're working on eliminating that requirement: It is currently required to use ROCm's clang to compile device code for certain parts of libhrx (i.e. blit/transfer kernels and such). |

👍3

All reactions

- 👍3

[![@benvanik](https://avatars.githubusercontent.com/u/75337?s=60&v=4)](https://github.com/benvanik)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

#### [benvanik](https://github.com/benvanik) [on Aug 31Aug 31, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18221800)

|     |
| --- |
| (latest hrx-system main now uses prebuilt binaries so no rocm required) |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/1131751?s=64&v=4)\ ckuethe](https://github.com/ckuethe) [on Aug 26Aug 26, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18165800)

|     |
| --- |
| So close, yet so far on 7900XT.<br>```<br>ckuethe@ryzen:~/githubs/llama-hrx$ ./build/bin/llama-cli --list-devices<br>Available devices:<br>  HRX0: AMD Radeon RX 7900 XT (Node 1) (gfx1100) (20464 MiB, 20464 MiB free)<br>ckuethe@ryzen:~/githubs/llama-hrx$ ./build/bin/llama-completion --list-devices<br>Available devices:<br>  HRX0: AMD Radeon RX 7900 XT (Node 1) (gfx1100) (20464 MiB, 20464 MiB free)<br>ckuethe@ryzen:~/githubs/llama-hrx$ ./build/bin/llama-completion -p "Who are you?" -m ~/.cache/huggingface/hub/models--ggml-org--gemma-3-4b-it-GGUF/snapshots/d0976223747697cb51e056d85c532013931fe52e/<br>gemma-3-4b-it-Q4_K_M.gguf  mmproj-model-f16.gguf      <br>ckuethe@ryzen:~/githubs/llama-hrx$ ./build/bin/llama-completion -p "Who are you?" -m ~/.cache/huggingface/hub/models--ggml-org--gemma-3-4b-it-GGUF/snapshots/d0976223747697cb51e056d85c532013931fe52e/gemma-3-4b-it-Q4_K_M.gguf <br>0.00.790.454 I llama_completion: llama backend init<br>0.00.790.460 I llama_completion: load the model and apply lora adapter, if any<br>0.01.109.984 W load: control-looking token:    212 '</s>' was not control-type; this is probably a bug in the model. its type will be overridden<br>0.03.541.078 E graph_compute: unsupported HRX node 0: GET_ROWS output=2:f32[2560,2,1,1]<-GET_ROWS inputs=[0:q6_K[2560,262144,1,1], 1:i32[2,1,1,1]] consumers=[]<br>0.03.541.083 E graph_compute: ggml_backend_sched_graph_compute_async failed with error -1<br>0.03.541.083 E process_ubatch: failed to compute graph, compute status: -1<br>0.03.541.084 W decode: removing memory module entries for seq_id = 0, pos = [0, +inf)<br>0.03.541.162 E llama_decode: failed to decode, ret = -3<br>0.03.547.433 I llama_completion: llama threadpool init, n_threads = 16<br>0.03.547.446 I llama_completion: chat template is available, enabling conversation mode (disable it with -no-cnv)<br>0.03.547.447 W *** User-specified prompt will pre-start conversation, did you mean to set --system-prompt (-sys) instead?<br>0.03.547.647 I llama_completion: chat template example:<br><start_of_turn>user<br>You are a helpful assistant<br>Hello<end_of_turn><br><start_of_turn>model<br>Hi there<end_of_turn><br><start_of_turn>user<br>How are you?<end_of_turn><br><start_of_turn>model<br>0.03.547.649 I <br>0.03.547.690 I system_info: n_threads = 16 (n_threads_batch = 16) / 32 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | LLAMAFILE = 1 | OPENMP = 1 | REPACK = 1 | <br>0.03.547.691 I <br>0.03.547.854 I llama_completion: interactive mode on.<br>0.03.547.857 I sampler seed: 1669429659<br>0.03.547.863 I sampler params: <br>	repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000<br>	dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = -1<br>	top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, top_n_sigma = -1.000, temp = 0.800<br>	mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000, adaptive_target = -1.000, adaptive_decay = 0.900<br>0.03.547.868 I sampler chain: logits -> ?penalties -> ?dry -> ?top-n-sigma -> top-k -> ?typical -> top-p -> min-p -> ?xtc -> temp-ext -> dist <br>0.03.547.868 I generate: n_ctx = 131072, n_batch = 2048, n_predict = -1, n_keep = 1<br>0.03.547.868 I <br>0.03.547.869 I == Running in interactive mode. ==<br>0.03.547.869 I  - Press Ctrl+C to interject at any time.<br>0.03.547.869 I  - Press Return to return control to the AI.<br> - To return control without starting a new line, end your input with '/'.<br> - If you want to submit another line, end your input with '\'.<br>0.03.547.869 I  - Not using system message. To change it, set a different value via -sys PROMPT<br>0.03.547.869 I <br>user<br>Who are you?<br>model<br>0.03.548.442 E graph_compute: unsupported HRX node 0: GET_ROWS output=2:f32[2560,13,1,1]<-GET_ROWS inputs=[0:q6_K[2560,262144,1,1], 1:i32[13,1,1,1]] consumers=[]<br>0.03.548.444 E graph_compute: ggml_backend_sched_graph_compute_async failed with error -1<br>0.03.548.445 E process_ubatch: failed to compute graph, compute status: -1<br>0.03.548.445 W decode: removing memory module entries for seq_id = 0, pos = [0, +inf)<br>0.03.548.515 E llama_decode: failed to decode, ret = -3<br>0.03.548.517 E cmn  common_promp: failed to eval<br>``` |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@rsuderman](https://avatars.githubusercontent.com/u/5508949?s=60&v=4)](https://github.com/rsuderman)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [rsuderman](https://github.com/rsuderman) [on Aug 31Aug 31, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18221804)\
\
|     |\
| --- |\
| We are still working on expanding model coverage. The initial version was mostly a proof of concept running on qwen 30b whereas it looks like you are using gemma 3. We should have more support landing as we widen op coverage. Will update once I see it landing. |\
\
👍1\
\
All reactions\
\
- 👍1\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/5508949?s=64&v=4)\ rsuderman](https://github.com/rsuderman) [on Aug 31Aug 31, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18221822)\
\
|     |\
| --- |\
| We have a newer version with support for llama 3 across multiple quantization formats and `f16` here.<br>[https://github.com/AMD-Ecosystem/llama.cpp/tree/hrx-graph-develop-v2](https://github.com/AMD-Ecosystem/llama.cpp/tree/hrx-graph-develop-v2)<br>This is more generalized so we should have a good cadence for increasing model coverage while moving away from the qwen focused implementation. |\
\
2You must be logged in to vote\
\
All reactions\
\
2 replies\
\
\
[![@ckuethe](https://avatars.githubusercontent.com/u/1131751?s=60&v=4)](https://github.com/ckuethe)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [ckuethe](https://github.com/ckuethe) [on Aug 31Aug 31, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18222303)\
\
|     |\
| --- |\
| I tried the binary build on my RX7900 and it's working well with gemma3 (>130t/s) and gpt-oss-20b (>140t/s) |\
\
All reactions\
\
[![@pwilkin](https://avatars.githubusercontent.com/u/5802960?s=60&v=4)](https://github.com/pwilkin)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [pwilkin](https://github.com/pwilkin) [on Sep 3Sep 3, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18275551)   Collaborator\
\
|     |\
| --- |\
| [@rsuderman](https://github.com/rsuderman) thanks, this looks much better and makes me more confident in the direction this is going. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/21368004?s=64&v=4)\ kheiman61](https://github.com/kheiman61) [on Sep 2Sep 3, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18260172)\
\
| Tried it out on my Strix Halo 395+ / 128GB. Based on some quick testing with my local coding harness, can confirm that this is definitely on the right track. The results also matched what I observed as a test just summarizing paragraphs with each directly in llama.cpp.\
\
Great stuff!\
\
## HRX vs HIP — Qwen3-30B-A3B-Instruct-2507 Q4\_K\_M, gfx1151 (Radeon 8060S / Strix Halo)\
\
Both backends built from llama.cpp `33a1f2b23` (b10224), running ROCm 10.1 + HSA 1.21.\
\
Mean of 5 interleaved runs on an otherwise idle machine.\
\
| Test | HRX (t/s) | HIP (t/s) | HRX vs HIP |\
| --- | --: | --: | --: |\
| pp16 | 218.6 ±0.6 | 304.2 ±7.6 | −28.1% |\
| pp32 | 351.7 ±2.5 | 416.7 ±13.0 | −15.6% |\
| pp64 | 568.2 ±1.9 | 412.7 ±33.6 | +37.7% |\
| pp128 | 912.8 ±6.4 | 408.7 ±11.2 | **+123.3%** |\
| pp256 | 1172.5 ±66.4 | 636.6 ±6.5 | +84.2% |\
| pp512 | 1261.8 ±160.1 | 937.5 ±9.8 | +34.6% |\
| pp1024 | 1592.1 ±19.8 | 1319.3 ±21.8 | +20.7% |\
| tg128 | 85.1 ±0.7 | 68.0 ±0.3 | **+25.1%** |\
| tg512 | 80.6 ±0.2 | 66.3 ±0.2 | +21.5% |\
| tg128 @ depth 1024 | 78.2 ±0.3 | 64.6 ±0.5 | +21.0% |\
\
**Notes**\
\
- HIP is ahead below ~32 tokens (per-dispatch overhead dominates); crossover sits between 32 and 64.\
- HRX's pp512 spread (±160) is unusually wide — treat +34.6% as approximate.\
- Short-prompt rows are warm-up sensitive: measured standalone with per-size warm-up, HIP reached 273 t/s at pp16 vs HRX's stable 218. hipBLASt autotuning needs repetition; HRX is steady from the first run.\
- pp1024 uses matched `-b/-ub` — HRX cannot chunk prefill against a non-empty KV cache. Throughput regresses above 1024, so measurements stop there. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/1646210?s=64&v=4)\ John-Gee](https://github.com/John-Gee) [on Sep 3Sep 3, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18262785)\
\
|     |\
| --- |\
| I really appreciate the smaller size, I always disliked the waste from the huge ROCm install, and I look forward to seeing how it compares on performance to [https://github.com/warpfront/hipfire](https://github.com/warpfront/hipfire) in the future. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/36085700?s=64&v=4)\ Ruslan-Riazantsev](https://github.com/Ruslan-Riazantsev) [on Sep 3Sep 3, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18271037)\
\
|     |\
| --- |\
| Is support for gfx1030 even considered for this backend, or people with older hardware would be better of using Vulkan instead? |\
\
1You must be logged in to vote\
\
All reactions\
\
2 replies\
\
\
[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=60&v=4)](https://github.com/stellaraccident)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [stellaraccident](https://github.com/stellaraccident) [on Sep 3Sep 3, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18271333)   Author\
\
|     |\
| --- |\
| We will support all of older hardware that rocm supports. Just takes time but not very hard. I was just doing a proof of concept of Radeon VII last night to see how bad it is, and should be straight forward. But until that happens, vulkan is a viable option. |\
\
❤️5\
\
All reactions\
\
- ❤️5\
\
[![@Ruslan-Riazantsev](https://avatars.githubusercontent.com/u/36085700?s=60&v=4)](https://github.com/Ruslan-Riazantsev)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [Ruslan-Riazantsev](https://github.com/Ruslan-Riazantsev) [on Sep 3Sep 3, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18272155)\
\
|     |\
| --- |\
| [@stellaraccident](https://github.com/stellaraccident) Thank you, that's a great news! |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
### [![](https://avatars.githubusercontent.com/u/5233329?s=64&v=4)\ digitalscream](https://github.com/digitalscream) [on Sep 3Sep 3, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18273382)\
\
|     |\
| --- |\
| Well, I sincerely hope that the maintainers find an acceptable way to move forward with this, rather than rejecting it - it would be of _huge_ benefit to us AMD GPU owners, by the looks of it. _Especially_ if it gives us good multi-GPU handling on both MoE and dense models, which can't be said of the current ROCm or Vulkan approaches.<br>I really want to come back to llama.cpp, but vLLM performance on R9700s is just better at the moment. Those performance numbers should take llama.cpp well past what I'm seeing in vLLM in some cases, which gives me hope that I'll be able to leave that painful mess behind.<br>It really would suck if this just ended up as another vendor-specific fork. |\
\
2You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@LaurentChardin](https://avatars.githubusercontent.com/u/504748?s=60&v=4)](https://github.com/LaurentChardin)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [LaurentChardin](https://github.com/LaurentChardin) [on Sep 4Sep 4, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18288619)\
\
|     |\
| --- |\
| As [@stellaraccident](https://github.com/stellaraccident) stated, this is currently a preliminary sharing with the community to request feedbacks and share the design principles in order to become a full fledge backend option. I believe this is great that this come early in the process to give time to have feedback from the maintainers expectations. I understand at this stage this is not really yet ready to be fully incorporated but i believe the expectations at the moment is to share the underlying design decisions and philosophy to ensure this is on a path that would permit proper inclusion. As an AMD GPU users, i hope the maintainers will see this opportunity with open eyes and also share concrete feedback to the initial team to move together in this path. |\
\
👍2\
\
All reactions\
\
- 👍2\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/9589343?s=64&v=4)\ pgarba](https://github.com/pgarba) [on Sep 4Sep 4, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18292839)\
\
|     |\
| --- |\
| I tried to compile and run it but getting an error:<br>\`./llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF<br>Loading model... \|/home/adam/llm/hxl/llama.cpp/ggml/src/ggml-backend.cpp:898: pre-allocated tensor (cache\_r\_l0 (reshaped) (view) (view)) in a buffer (HRX0) that cannot run the operation (SCALE)<br>This GDB supports auto-downloading debuginfo from the following URLs:<br>[https://debuginfod.cachyos.org](https://debuginfod.cachyos.org/)<br>[https://debuginfod.archlinux.org](https://debuginfod.archlinux.org/)<br>Enable debuginfod for this session? (y or \[n\]) \[answered N; input not from terminal\]<br>Debuginfod has been disabled.<br>To make this setting permanent, add 'set debuginfod enabled off' to .gdbinit.<br>\[Thread debugging using libthread\_db enabled\]<br>Using host libthread\_db library "/usr/lib/libthread\_db.so.1".<br>0x00007f7591cb61f2 in ?? () from /usr/lib/libc.so.6<br>#0 0x00007f7591cb61f2 in ?? () from /usr/lib/libc.so.6<br>[#1](https://github.com/ggml-org/llama.cpp/issues/1) 0x00007f7591d00eaa in clock\_nanosleep () from /usr/lib/libc.so.6<br>[#2](https://github.com/ggml-org/llama.cpp/issues/2) 0x00007f7591d11237 in nanosleep () from /usr/lib/libc.so.6<br>[#3](https://github.com/ggml-org/llama.cpp/pull/3) 0x00007f7594804fdb in cli\_server::wait\_ready(std::function<bool ()>) () from /home/adam/llm/hxl/build/bin/libllama-cli-impl.so<br>[#4](https://github.com/ggml-org/llama.cpp/issues/4) 0x00007f75947ee518 in cli\_context::init() () from /home/adam/llm/hxl/build/bin/libllama-cli-impl.so<br>[#5](https://github.com/ggml-org/llama.cpp/issues/5) 0x00007f75947e3e4c in llama\_cli(int, char\*\*) () from /home/adam/llm/hxl/build/bin/libllama-cli-impl.so<br>[#6](https://github.com/ggml-org/llama.cpp/pull/6) 0x00005630e1d4a346 in main ()<br>\`<br>Trying the hrx-graph-develop-v2 branch. |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@rsuderman](https://avatars.githubusercontent.com/u/5508949?s=60&v=4)](https://github.com/rsuderman)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [rsuderman](https://github.com/rsuderman) [on Sep 11Sep 11, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18404330)\
\
|     |\
| --- |\
| I should have an RFC up soon which will include scale support and wider model coverage. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
### [![](https://avatars.githubusercontent.com/u/205989374?s=64&v=4)\ vletu-ghub](https://github.com/vletu-ghub) [on Sep 6Sep 6, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18316761)\
\
|     |\
| --- |\
| Super excited about this work. My setup is only a single 7900 XTX, Windows, llama.cpp and Qwen 3.8 27B, UD Q4 K XL and 8bit cache [@142k](https://github.com/142k), no vision, MTP on (3 tokens). Would this be supported now on Linux at least? |\
\
2You must be logged in to vote\
\
All reactions\
\
7 replies\
\
\
Show 2 previous replies\
\
[![@vletu-ghub](https://avatars.githubusercontent.com/u/205989374?s=60&v=4)](https://github.com/vletu-ghub)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [vletu-ghub](https://github.com/vletu-ghub) [on Sep 9Sep 9, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18369018)\
\
|     |\
| --- |\
| Ah, I see. Well, very grateful to the llama.cpp contributors, I literally check, download and start using pre-releases a few times a day. I've also started an AI assisted project (Sol and Astra) that takes a llama.cpp release and applies a set of patches designed to optimize my setup/workflow as much as possible. The patches are based on various other github projects, various PRs for llama.cpp, the HRX architecture document, CUDA optimizations (translated for AMD), etc. I doubt any performance increase would be useful to the llama.cpp project, as it would be heavily tuned for my setup exactly, Hoping HRX can make this project moot, but until then, I'm exploring all the options.<br>[@stellaraccident](https://github.com/stellaraccident) \- very excited about your project. Can't wait to have a preview of HRX on Windows, that also supports qwen 3.8 27B. |\
\
All reactions\
\
[![@rsuderman](https://avatars.githubusercontent.com/u/5508949?s=60&v=4)](https://github.com/rsuderman)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [rsuderman](https://github.com/rsuderman) [on Sep 11Sep 11, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18404369)\
\
|     |\
| --- |\
| We should have support for your exact setup soon (specifically MTP on the 7900). For now we are focusing on getting full coverage of the models used by the lemonade benchmarks. This should include both windows and linux coverage. The work to get this running on windows has been landing in the `hrx` repo but have not yet been able to validate it works with our llama cpp implementaiton. |\
\
👍4🎉1\
\
All reactions\
\
- 👍4\
- 🎉1\
\
[![@vletu-ghub](https://avatars.githubusercontent.com/u/205989374?s=60&v=4)](https://github.com/vletu-ghub)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
edited\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{editor}}'s edit\
\
{{actor}} deleted this content\
.\
\
# {{editor}}'s edit\
\
#### [vletu-ghub](https://github.com/vletu-ghub) [on Sep 11Sep 11, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18405890)\
\
|     |\
| --- |\
| Awesome. [@rsuderman](https://github.com/rsuderman), can't wait to test it. I'm still trying to squeeze every last drop of performance out of my hardware, before I can focus on what I actually want to build.<br>I've built (Codex assisted) some monitoring tool that captures memory pressure and system ram spilling. Ran some synthetic benchmarks to probe various context sizes, using different setting combinations (mtp on, vision on/off, etc).<br>If anyone is interested, using build 10908, qwen 3.8 27b, ud q4 k xl, 8bit kv cache, 142k context, mtp on (3token):<br>```<br>Metric	                                                  ROCm	      Vulkan	        Winner<br>Cold PP, 113,600 tokens	                             564.7 t/s	      358.3 t/s	        ROCm +57.6%<br>Long-context TG	                                     39.75 t/s	      47.04 t/s	        Vulkan +18.4%<br>Normalized target evals	                             10.34/s	      12.03/s	        Vulkan +16.3%<br>Post-compaction PP	                                 718.2 t/s	      527.8 t/s	        ROCm +36.1%<br>Post-compaction TG	                                 60.61 t/s	      68.57 t/s	        Vulkan +13.1%<br>```<br>This simulates a long coding session in DSH. Note that Vulkan is stable (no dram spill) at 150k, but this compares performance at the same context size. I can run vulkan at 142k + vision on.<br>I'll run this benchmark against HRX as well, once it's out. Right now, it's a difficult trade-off, but for this type of workflow (hours long coding sessions, compaction at 80%), vulkan wins with an estimated total time lower by 5% than ROCm.<br>P.S.: achieving those context sizes at that quantization requires running the monitor off the integrated GPU, instead of off the 7900XTX. But that's a Windows problem, rather than a llama.cpp or AMD problem. Windows would use ~1.1GB - ~1.7GB otherwise. Monitor on iGPU leaves the entire 24GB vram free for llama.cpp. |\
\
All reactions\
\
[![@vletu-ghub](https://avatars.githubusercontent.com/u/205989374?s=60&v=4)](https://github.com/vletu-ghub)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [vletu-ghub](https://github.com/vletu-ghub) [on Sep 11Sep 11, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18406221)\
\
|     |\
| --- |\
| [@rsuderman](https://github.com/rsuderman) , I'm also curious about this repo which I watch: [https://github.com/lemonade-sdk/llamacpp-rocm/releases](https://github.com/lemonade-sdk/llamacpp-rocm/releases). I've tested rocm 10,1 alpha, didn't find any obvious performance improvement (vs rocm 10.0.0), gave up. I see it's been bumped up to 10.2a. The issue is there seem to be no release notes. Once HRX is fully rolled out, is the plan to phase out rocm, at least in llama.cpp? Considering my use case, is there any point in chasing the lemonade releases? |\
\
All reactions\
\
[![@AaronStGeorge](https://avatars.githubusercontent.com/u/2278731?s=60&v=4)](https://github.com/AaronStGeorge)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [AaronStGeorge](https://github.com/AaronStGeorge) [on Oct 6Oct 6, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18785506)\
\
|     |\
| --- |\
| We've updated lemonade to use a fairly recent hrx build recently: [lemonade-sdk/lemonade#3723](https://github.com/lemonade-sdk/lemonade/pull/3723). Hrx builds are produced here until it's available as part of main line builds: [https://github.com/ROCm/ggml-staging-automation](https://github.com/ROCm/ggml-staging-automation) (note ggml-staging-automation is intended to be temporary, so don't build automation that relies on it). |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/99437150?s=64&v=4)\ rwfsmith](https://github.com/rwfsmith) [on Sep 15Sep 15, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18455428)\
\
|     |\
| --- |\
| I got llama.cpp with the HRX backend running on Windows and with the Qwen3.8-Flash-Next UD-Q3\_K\_XL model on my Strix Halo, but I haven't been able to optimize the performance to match Vulkan yet. Any suggestions on how best to find the bottlenecks? I should probably just wait for somebody more experienced to handle it, I was just excited about the prospect of running this model at a higher speed :). |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/274903179?s=64&v=4)\ a-n-t-0](https://github.com/a-n-t-0) [on Sep 16Sep 16, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18466880)\
\
|     |\
| --- |\
| [@stellaraccident](https://github.com/stellaraccident) [@rsuderman](https://github.com/rsuderman)<br>A potentially interesting data point for future HRX multi-GPU / tensor-parallel work:<br>I benchmarked the new llama.cpp internal ROCm 2-GPU AllReduce from [#27825](https://github.com/ggml-org/llama.cpp/pull/27825) against RCCL on:<br>- 2x RX 7900 XTX / gfx1100<br>- PCIe 4.0 x8/x8<br>- Qwen3.8-27B Q8\_0<br>- tensor split<br>RCCL is clearly faster for prompt processing, but the specialized internal AllReduce is consistently faster for decode:<br>```<br>TG short context:<br>internal AllReduce: 36.60 t/s<br>RCCL:               35.62 t/s<br>TG at 100k KV depth:<br>internal AllReduce: 31.59 t/s<br>RCCL:               30.81 t/s<br>```<br>So the internal path keeps roughly a 2.5-2.8% decode advantage even at 100k KV depth.<br>RCCL remains around 9% faster on the large prefill test.<br>Full benchmark and configuration:<br>[#27825 (comment)](https://github.com/ggml-org/llama.cpp/pull/27825#issuecomment-5699240655)<br>I thought this could be useful for HRX design: for decode on a simple 2-GPU RDNA3 topology, a very lightweight specialized collective may be worth keeping alongside a more general RCCL-style path. |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=60&v=4)](https://github.com/stellaraccident)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [stellaraccident](https://github.com/stellaraccident) [on Sep 16Sep 17, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18474802)   Author\
\
|     |\
| --- |\
| Thanks, and I believe it. Once you get into bandwidth limited regimes, it is hard for general purpose implementations to compete. We'll definitely have light weight primitives in this implementation for doing the kind of collective comms that show up all the time for this scale of problem. If you vertically integrate the solution, it becomes fairly easy to optimize in a way that is hard when working across big library boundaries. Just trying to not get out over our skis and focused for the moment on getting general support for all of the models. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/144213886?s=64&v=4)\ huppiflupp](https://github.com/huppiflupp) [on Sep 19Sep 19, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18511605)\
\
|     |\
| --- |\
| Since the RFC mentions NPUs as a target: a few measured numbers from Linux on Strix Halo (GMKtec EVO-X2, 395, 128 GB, kernel 7.2, in-tree `amdxdna`, XRT 2.26, Mesa 26.2.1) that may matter for placement decisions. Details in [colibri #1590](https://github.com/JustVugg/colibri/discussions/1590#discussioncomment-18497077).<br>- **Energy per token, NPU vs iGPU, same model** (Gemma 4 E4B, NPU via FastFlowLM, iGPU via llama.cpp Vulkan): NPU 12.1 tok/s at 22 W socket, iGPU 57.3 tok/s at 72 W. **Above idle both cost ~1.1 J/token**; including idle, the iGPU is a third cheaper. The NPU's value here is low power and a free iGPU, not energy per token.<br>- **Shared memory controller:** iGPU alone 226 GB/s read, CPU alone 108 GB/s. While the iGPU streams, the CPU drops to **~17 GB/s**. CPU+iGPU hybrid placement (e.g. `--n-cpu-moe`) is bandwidth-starved on this part, and an NPU lane will compete for the same controller.<br>- **Telemetry gap:** on Linux the NPU has no power sensor of its own (`xrt-smi examine -r platform` → `GET_INFO``-EOPNOTSUPP` on the in-tree driver), and RAPL package equals amdgpu PPT, so NPU power can only be inferred from the socket delta. Per-engine power (NPU/GPU/CPU) via HRX would make these comparisons much easier.<br>Happy to run HRX against Vulkan and HIP on this box, with perplexity, once there's a build you'd like tested. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/144213886?s=64&v=4)\ huppiflupp](https://github.com/huppiflupp) [on Sep 19Sep 19, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18512703)\
\
| HRX on a second Strix Halo (GMKtec EVO-X2, 395, 128 GB), Fedora 44 / kernel 7.2. Build notes for non-Ubuntu distros: [HRX.md](https://github.com/huppiflupp/strix-halo-npu-linux/blob/main/HRX.md). Distro ROCm 7.1's HSA 1.18 asserts in `hsa_amd_signal_wait_any`, so I needed TheRock ROCm 10.1 via `LD_LIBRARY_PATH`. Qwen3-30B-A3B-Instruct-2507 Q4\_K\_M, `-fa 1`, master `ec92815` for Vulkan/HIP:\
\
|  | HRX | Vulkan | HIP |\
| --- | --- | --- | --- |\
| pp512 | **1724** | 1466 | 1650 |\
| pp1024 / pp2048 (single ubatch, `-ub` = prompt) | 1836 / 1653 | – | – |\
| tg128 | 85.3 | **89.5** | 72.9 |\
\
Greedy output over 96 tokens is identical to Vulkan and HIP on 2 of 3 prompts; the third diverges at the same point HIP does (normal FP ordering).\
\
Two failures that may help:\
\
1. **Only the first ubatch works.** pp1024/2048/4096 with the default `-ub 512` fail with `failed to decode prompt batch, res = -3`, and so does `-d 8192`. With `-ub` equal to the prompt length it runs. Every ubatch with a non-empty KV cache seems to fail.\
2. **`llama-perplexity` fails** with `unsupported HRX node: GET_ROWS output=f32[2048,0,1,1] … inputs=[f32[2048,512], i32[0,1,1,1]]`, i.e. GET\_ROWS with an empty index tensor.\
\
Happy to re-run on a newer branch. |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@pwilkin](https://avatars.githubusercontent.com/u/5802960?s=60&v=4)](https://github.com/pwilkin)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [pwilkin](https://github.com/pwilkin) [on Sep 19Sep 19, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18513447)   Collaborator\
\
|     |\
| --- |\
| The two are most likely related, as KV cache access uses GET\_ROWS. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/144213886?s=64&v=4)\ huppiflupp](https://github.com/huppiflupp) [on Sep 19Sep 19, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18515196)\
\
| Follow-up to my [earlier results](https://github.com/ggml-org/llama.cpp/discussions/27219#discussioncomment-18512703) on Strix Halo (gfx1151, Radeon 8060S). Each of the three failures I reported there turned out to be a small fix. With those fixes, long-context decode then showed a memory-ordering problem, so there's a fourth. Branch: [https://github.com/huppiflupp/llama.cpp/tree/hrx-fixes](https://github.com/huppiflupp/llama.cpp/tree/hrx-fixes) (four commits on `users/stella/hrx-rfc-v1`, only under `ggml/src/ggml-hrx`).\
\
1. **Empty output nodes** (`dispatch-scheduler.cpp`). `llama-perplexity` builds a `GET_ROWS` over an empty output-row index (`f32[n,0] <- i32[0]`), and that rejected the whole graph. A node with a zero-element output is now elided, the same way a layout alias is.\
2. **Prompts longer than one ubatch** (`dispatch-qwen-flash-attention.cpp`, `command-program-bindings.cpp`, `graph-executor.cpp`).\
\
   - A later ubatch has a mask `n_kv` wide (cached prefix + ubatch). That is neither the compact nor the capacity width, so the match was rejected. The prefill kernel already reads causality from the mask, so it now attends over `mask->ne[0]` rows.\
   - A ubatch with no outputs has zero-byte `inp_out_ids` and logits. These failed with `external value N has an empty binding`; they are now skipped at binding time.\
3. **Decode past 2048 tokens of context.** The fused decode-split kernel stops at 2048 KV tokens, because its cooperative reducer folds at most 32 blocks. The corpus already has `decode_split_produce_partials_f32_f16_wmma` and `decode_split_reduce_f32` (up to 32768), but they are not registered. I registered them as a priority-150 dispatch for `2048 < n_kv <= 32768`. It is followed by `decode_split_quantize_reference_4096`, so `attn_output` still gets its Q8\_1 input. Your own test shows that quantizer is bit-identical to `pack_completed_q8`. The decode matcher already requires 32 query heads, so 4096 always holds, but a proper export would be cleaner than borrowing the test kernel.\
4. **Decode-split grid order** (`flash_attention_decode_split_f32_f16_wmma.loom`).\
\
   - The grid was `(kv_block, kv_head)`, so all blocks of head 0 were issued before any block of head 1. Each K/V row holds all four heads (4 × 256 B), so every row was fetched in four passes, a full KV sweep apart.\
   - Beyond ~8k tokens that working set no longer fits the 32 MB MALL. The producer then fell to ~67 GB/s: 250 µs per layer, 2.7× the time for 2× the data compared with 4k.\
   - Swapping to `(kv_head, kv_block)` gives 97.5 µs per layer (~170 GB/s). Math and partial layout are unchanged. This also applies to the fused ≤2048 kernels, where it makes no measurable difference.\
\
Qwen3-30B-A3B-Instruct-2507 Q4\_K\_M, `-fa 1`, TheRock 10.1 HSA runtime:\
\
|  | HRX before | HRX with fixes | Vulkan | HIP |\
| --- | --- | --- | --- | --- |\
| pp4096 (`-ub 512`) | `-3` | 1308 | 1187 | 1429 |\
| tg64 @ d4096 | `-3` | 66.9 | 74.6 | – |\
| tg128 @ d8192 | `-3` | 57.1 | 65.4 | 55.9 |\
| PPL wikitext-2, `-c 2048`, 20 chunks | fails | 6.4170 | 6.4075 | 6.4061 |\
\
Correctness:\
\
- PPL at the default `-ub 512` (four ubatches per chunk) is identical to a single 2048-token ubatch.\
- Greedy decoding on a 7163-token prompt, where every generated token goes through the long-context path: 128/128 tokens identical to Vulkan, both before and after fix 4.\
- On a 2722-token prompt HRX diverges at a near-tie. At that position Vulkan's top two are _culture_ −0.859 and _thought_ −0.876 logprob. HIP diverges from Vulkan elsewhere in the same run.\
\
At 8k, the remaining gap to Vulkan is ~2 ms per token. About 1.5 ms of that is attention: the long path runs producer (97.5 µs), reducer (15.8 µs) and Q8 pack (2.8 µs) as separate dispatches, while Vulkan uses one.\
\
A side note for anyone profiling this: with `HRX_PROFILE_MODE=dispatch`, graph launches record no dispatch events. `libhrx/graph_exec.c` creates the partition command buffers without `IREE_HAL_COMMAND_BUFFER_MODE_RETAIN_PROFILE_METADATA`, so the AMDGPU HAL gives them profile id 0 and skips them. Setting that flag while `device->profiling_active` is true makes `iree-profile executable` report per-kernel times. That is how the numbers above were measured. I can open that as an issue or PR on ROCm/hrx-system.\
\
Happy to turn any of this into a PR against your branch if that's useful. |\
\
1You must be logged in to vote\
\
All reactions\
\
5 replies\
\
\
[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=60&v=4)](https://github.com/stellaraccident)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [stellaraccident](https://github.com/stellaraccident) [on Sep 19Sep 19, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18516117)   Author\
\
|     |\
| --- |\
| This is great. Thank you so much for taking the time. [@rsuderman](https://github.com/rsuderman) / [@jammm](https://github.com/jammm) let's make sure to track this and get fixes/PRs incorporated.<br>(We're off this weekend so just setting expectations that this might not get looked at until Monday) |\
\
All reactions\
\
[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=60&v=4)](https://github.com/stellaraccident)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [stellaraccident](https://github.com/stellaraccident) [on Sep 19Sep 19, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18516146)   Author\
\
|     |\
| --- |\
| For trivial fixes to hrx-system, PRs welcome. For more involved things or if not wanting to take the time to meet all of the requirements (testing, coding conventions, etc), a good issue is perfectly fine and we can take it from there. |\
\
👍1\
\
All reactions\
\
- 👍1\
\
[![@huppiflupp](https://avatars.githubusercontent.com/u/144213886?s=60&v=4)](https://github.com/huppiflupp)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [huppiflupp](https://github.com/huppiflupp) [on Sep 19Sep 19, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18519020)\
\
| [@rsuderman](https://github.com/rsuderman) [@jammm](https://github.com/jammm): while porting the fixes from my earlier comment to `hrx-graph-develop-v2` (v3, `4767e2f`), I found that **decode produces garbage on gfx1151** even on the untouched branch. Prefill looks fine.\
\
Setup: Strix Halo (Radeon 8060S, gfx1151), Fedora 44 / kernel 7.2, TheRock ROCm 10.1 HSA runtime via `LD_LIBRARY_PATH`, Qwen3-30B-A3B-Instruct-2507 Q4\_K\_M, `llama-server -fa on -ngl 999 -dev HRX0`, greedy.\
\
|  | output of "Name three rivers in Germany." |\
| --- | --- |\
| RFC branch (`users/stella/hrx-rfc-v1`) | "Sure! Three rivers in Germany are: 1. Rhine River 2. Danube River 3. Elbe River" |\
| v3 `4767e2f` \+ hrx-system `main``47c75c23` | "Three rivers in Germany.:\\n\\n::\\n\\n::::: to:fühl:::: to.:................." |\
| v3 `4767e2f` \+ hrx-system `a65bac68` (15 Sep, matching the v3 merge) | identical garbage |\
\
- The first generated token (from prefill) is right. Everything after it is wrong, and deterministically so.\
- `llama-perplexity` (prefill only) gives 6.4018 vs Vulkan 6.4075, so prefill is fine.\
- `llama-bench` tg looks healthy (89.8 t/s), because it doesn't check outputs.\
\
Not the cause (each makes no difference):\
\
- `GGML_HRX_DISABLE_GRAPH_REPLAY=1`\
- `GGML_HRX_DEBUG_SERIAL_EXECUTION=1`\
- `GGML_HRX_DIAGNOSTIC_FRESH_TRANSIENT_ARENA=1`\
- disabling the decode-split flash attention (routing decode to `ggml_flash_attention_f32_f16_wmma` changes the garbage but doesn't fix it)\
\
`GGML_HRX_DISABLE_QWEN_DISPATCH=1` fails the request (HTTP 500).\
\
Compared with the RFC branch, the decode kernels that differ are the generalized `ggml_flash_attention_decode_split_f32_f16_wmma_next_q8` (loom-libs) and `ggml_get_rows_f32`. The Qwen3-MoE FFN/projection decode kernels have the same names as on the RFC branch.\
\
I couldn't bisect further with the usual tools: `llama-eval-callback` splits the graph into single ops HRX doesn't support, and `llama-perplexity -ub 1` needs more output rows than the decode routes allow. Happy to run whatever diagnostic you suggest.\
\
Two v3 changes that are independent of this bug, for when it's fixed: [https://github.com/huppiflupp/llama.cpp/tree/hrx-v3-fixes](https://github.com/huppiflupp/llama.cpp/tree/hrx-v3-fixes)\
\
1. The graph-program cache rejects zero-byte views (`metadata does not match current tensor`), so prompts longer than one ubatch fail. This is the v3 counterpart of the empty-binding issue.\
2. The long-context decode path and the KV-head-major grid order from my earlier comment, ported to loom-libs.\
\
Both are untested for correctness because of the decode bug above.\
\
The profiler fix I mentioned is now [ROCm/hrx-system#677](https://github.com/ROCm/hrx-system/pull/677). |\
\
All reactions\
\
[![@AaronStGeorge](https://avatars.githubusercontent.com/u/2278731?s=60&v=4)](https://github.com/AaronStGeorge)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [AaronStGeorge](https://github.com/AaronStGeorge) [on Oct 6Oct 6, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18785840)\
\
|     |\
| --- |\
| [@huppiflupp](https://github.com/huppiflupp) we've merged several numerical fixes recently,<br>[AMD-Ecosystem#119](https://github.com/AMD-Ecosystem/llama.cpp/pull/119)<br>[AMD-Ecosystem#117](https://github.com/AMD-Ecosystem/llama.cpp/pull/117)<br>[AMD-Ecosystem#120](https://github.com/AMD-Ecosystem/llama.cpp/pull/120) / [ROCm/hrx-system#1301](https://github.com/ROCm/hrx-system/pull/1301)<br>Though, looking at the latest [CI run](https://github.com/ROCm/ggml-staging-automation/actions/runs/37358385120) with some larger models we don't always run (they're large) it looks like there may be some additional regressions, we'll get those fixed! |\
\
👍2\
\
All reactions\
\
- 👍2\
\
[![@John-Gee](https://avatars.githubusercontent.com/u/1646210?s=60&v=4)](https://github.com/John-Gee)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [John-Gee](https://github.com/John-Gee) [on Oct 11Oct 12, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18872512)\
\
|     |\
| --- |\
| [@AaronStGeorge](https://github.com/AaronStGeorge) That CI run link is awesome to see how things are today, thanks a lot! |\
\
🚀1\
\
All reactions\
\
- 🚀1\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/981494?s=64&v=4)\ emansom](https://github.com/emansom) [on Oct 15Oct 15, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18959364)\
\
|     |\
| --- |\
| Any plans for gfx1201 / R9700 / 9070 XT support?<br>```<br>0.04.391.172 E graph_compute: no HRX dispatch registry for target gfx1201<br>0.04.391.174 E graph_compute: ggml_backend_sched_graph_compute_async failed with error -1<br>0.04.391.174 E process_ubatch: failed to compute graph, compute status: -1<br>``` |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@AaronStGeorge](https://avatars.githubusercontent.com/u/2278731?s=60&v=4)](https://github.com/AaronStGeorge)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [AaronStGeorge](https://github.com/AaronStGeorge) [on Oct 15Oct 15, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-18960893)\
\
|     |\
| --- |\
| Yes! Not sure on timeline yet but that's in the plans. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/17640822?s=64&v=4)\ icocoon](https://github.com/icocoon) [on Oct 25Oct 25, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-19178067)\
\
|     |\
| --- |\
| Hi — thanks for opening this up and for the detailed RFC. I've been reading the backend sources and the HRX docs with interest.<br>Some context on where I'm coming from: I run a 7900 XTX (`gfx1100`) on Windows 11, and my main use case is long-context local inference — roughly 128K–150K tokens on a 27B model. On a 24 GB card that only fits with a quantized KV cache (`q8_0`). The Windows path matters to me for the same reason: it's the machine I actually work on every day.<br>Reading the branch, I understand the initial submission targets a single model on W7900 / Strix Halo with f16 K/V — and from `dispatch-flash-attention.cpp` and `dispatch-rope-set-rows.cpp` the type gates look f16-only, so that reads as deliberate scoping rather than an oversight.<br>My question: **is quantized K/V (`q8_0`, `q4_0`) on the roadmap, and roughly what stage would it land at?** I'm not asking for a date — mostly trying to understand whether this is part of the coverage work, or a separate piece that might not happen.<br>A secondary question, if I may: the RFC mentions productionizing a static Windows build recipe. Is there an intended timeline for that becoming the supported path, or should Windows users plan on building from source for a while?<br>Thanks again — the JIT approach and the footprint numbers are genuinely interesting. |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@AaronStGeorge](https://avatars.githubusercontent.com/u/2278731?s=60&v=4)](https://github.com/AaronStGeorge)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [AaronStGeorge](https://github.com/AaronStGeorge) [last monthOct 29, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-19272085)\
\
|     |\
| --- |\
| Quantized K/V with the `-ctk``-ctv` flags will be supported at some point. HRX intends to be a fully featured backend so if vulkan and other similar backends support a feature, in general, hrx intends to as well.<br>I'm not sure on the exact timeline for windows support/packaging. It's definitely on the roadmap. |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/3746601?s=64&v=4)\ briansp2020](https://github.com/briansp2020) [last monthOct 31, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-19305047)\
\
|     |\
| --- |\
| [@stellaraccident](https://github.com/stellaraccident) Thank you for starting an effort to improve llama.cpp performance on AMD hardware. I'm very interested in improving the performance of llama.cpp on AMD hardware and have been contributing to [https://github.com/stew675/llama-cpp-rdna-boosts](https://github.com/stew675/llama-cpp-rdna-boosts). As we all know, to improve the over all performance, it is important to have low overhead runtime system. So, I was very excited to find out that AMD is actually working on HRX. But when I ran some benchmark on my 7900 XTX comparing HRX vs HIP with our optimized kernels, the result was not what I expected. I have created a discussion thread at [AMD-Ecosystem#167](https://github.com/AMD-Ecosystem/llama.cpp/discussions/167) and would love to have experts from AMD shed some light on this topic.<br>Thank you for your attention. |\
\
1You must be logged in to vote\
\
All reactions\
\
1 reply\
\
\
[![@rsuderman](https://avatars.githubusercontent.com/u/5508949?s=60&v=4)](https://github.com/rsuderman)\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
#### [rsuderman](https://github.com/rsuderman) [3 weeks agoNov 5, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-19424040)\
\
|     |\
| --- |\
| There is definitely a bit of column A and column B. We did ship new kernels that better support specialization due to `loom`. HRX was a bit of two-fold, there are meaningful improvements in dispatch speed that add up on smaller total workload (e.g. decode steps) but part of the motivation as well is to simplify shipping. HRX has a substantially smaller binary size and speaks directly with the device making it easier to ship the library dependency with llama-cpp? |\
\
All reactions\
\
Comment options\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/27219).\
\
# {{title}}\
\
Quote reply\
\
### [![](https://avatars.githubusercontent.com/u/3746601?s=64&v=4)\ briansp2020](https://github.com/briansp2020) [3 weeks agoNov 6, 2026](https://github.com/ggml-org/llama.cpp/discussions/27219\#discussioncomment-19429902)\
\
|     |\
| --- |\
| [@rsuderman](https://github.com/rsuderman) I'd love to learn more about HRX. Would you be kind enough to share how you benchmarked the improvements in dispatch speed? Being a hobbyist, I'm trying to maximize the performance of the hardware I have, rather then sink more money in to get faster hardware. I have posted what I have been able to compare at [AMD-Ecosystem#167 (comment)](https://github.com/AMD-Ecosystem/llama.cpp/discussions/167#discussioncomment-19429870) since this repo does not allow AI generated post. I'd love for people with more knowledge to comment and shed some light on it. |\
\
1You must be logged in to vote\
\
All reactions\
\
0 replies\
\
\
[Sign up for free](https://github.com/join?source=comment-repo) **to join this conversation on GitHub**.\
Already have an account?\
[Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fggml-org%2Fllama.cpp%2Fdiscussions%2F27219)\
\
Category\
\
\
[💬\\
\\
General](https://github.com/ggml-org/llama.cpp/discussions/categories/general)\
\
Labels\
\
\
None yet\
\
\
23 participants\
\
\
[![@stellaraccident](https://avatars.githubusercontent.com/u/494208?s=48&v=4)](https://github.com/stellaraccident) [![@benvanik](https://avatars.githubusercontent.com/u/75337?s=48&v=4)](https://github.com/benvanik) [![@Geramy](https://avatars.githubusercontent.com/u/264964?s=48&v=4)](https://github.com/Geramy) [![@LaurentChardin](https://avatars.githubusercontent.com/u/504748?s=48&v=4)](https://github.com/LaurentChardin) [![@neuhaus](https://avatars.githubusercontent.com/u/631764?s=48&v=4)](https://github.com/neuhaus) [![@emansom](https://avatars.githubusercontent.com/u/981494?s=48&v=4)](https://github.com/emansom) [![@ckuethe](https://avatars.githubusercontent.com/u/1131751?s=48&v=4)](https://github.com/ckuethe) [![@John-Gee](https://avatars.githubusercontent.com/u/1646210?s=48&v=4)](https://github.com/John-Gee) [![@AaronStGeorge](https://avatars.githubusercontent.com/u/2278731?s=48&v=4)](https://github.com/AaronStGeorge) [![@inforithmics](https://avatars.githubusercontent.com/u/2290863?s=48&v=4)](https://github.com/inforithmics) [![@briansp2020](https://avatars.githubusercontent.com/u/3746601?s=48&v=4)](https://github.com/briansp2020) [![@digitalscream](https://avatars.githubusercontent.com/u/5233329?s=48&v=4)](https://github.com/digitalscream) [![@rsuderman](https://avatars.githubusercontent.com/u/5508949?s=48&v=4)](https://github.com/rsuderman) [![@pwilkin](https://avatars.githubusercontent.com/u/5802960?s=48&v=4)](https://github.com/pwilkin) [![@pgarba](https://avatars.githubusercontent.com/u/9589343?s=48&v=4)](https://github.com/pgarba) [![@0cc4m](https://avatars.githubusercontent.com/u/11707594?s=48&v=4)](https://github.com/0cc4m) [![@icocoon](https://avatars.githubusercontent.com/u/17640822?s=48&v=4)](https://github.com/icocoon) [![@kheiman61](https://avatars.githubusercontent.com/u/21368004?s=48&v=4)](https://github.com/kheiman61) [![@Ruslan-Riazantsev](https://avatars.githubusercontent.com/u/36085700?s=48&v=4)](https://github.com/Ruslan-Riazantsev) [![@rwfsmith](https://avatars.githubusercontent.com/u/99437150?s=48&v=4)](https://github.com/rwfsmith) [![@huppiflupp](https://avatars.githubusercontent.com/u/144213886?s=48&v=4)](https://github.com/huppiflupp) and others\
\
Heading\
\
Bold\
\
Italic\
\
Quote\
\
Code\
\
Link\
\
* * *\
\
Numbered list\
\
Unordered list\
\
Task list\
\
* * *\
\
Attach files\
\
Mention\
\
Reference\
\
# Select a reply\
\
Loading\
\
[Create a new saved reply](https://github.com/ggml-org/llama.cpp/discussions/27219)\
\
👍1 reacted with thumbs up emoji👎1 reacted with thumbs down emoji😄1 reacted with laugh emoji🎉1 reacted with hooray emoji😕1 reacted with confused emoji❤️1 reacted with heart emoji🚀1 reacted with rocket emoji👀1 reacted with eyes emoji\
\
You can’t perform that action at this time.