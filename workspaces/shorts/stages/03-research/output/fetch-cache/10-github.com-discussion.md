<!-- url: https://github.com/ggml-org/llama.cpp/discussions/16578 -->
<!-- fetched via web_extract 2026-10-24, tier 3 (benchmark, ggerganov show-and-tell with commands and hardware listed). -->

[Skip to content](https://github.com/ggml-org/llama.cpp/discussions/16578#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/discussions/16578) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/discussions/16578) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/discussions/16578) to refresh your session.Dismiss alert

{{ message }}

# Performance of llama.cpp on NVIDIA DGX Spark  \#16578

[ggerganov](https://github.com/ggerganov)

started this conversation in
[Show and tell](https://github.com/ggml-org/llama.cpp/discussions/categories/show-and-tell)

[Performance of llama.cpp on NVIDIA DGX Spark](https://github.com/ggml-org/llama.cpp/discussions/16578#top)#16578

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=40&v=4)\\
ggerganov](https://github.com/ggerganov)

on Oct 14, 2025Oct 14, 2025·
32 comments
·
119 replies


[Return to top](https://github.com/ggml-org/llama.cpp/discussions/16578#top)

Discussion options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

## [![](https://avatars.githubusercontent.com/u/1991296?s=64&v=4)\ ggerganov](https://github.com/ggerganov) [on Oct 14, 2025Oct 14, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussion-9026280)   Maintainer

|     |
| --- |
| # Overview<br>This document summarizes the performance of `llama.cpp` for various models on the new [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/).<br>Benchmarks include:<br>- Prefill (`pp`) and generation (`tg`) at various context depths (`d`)<br>- Batch sizes of 1, 2, 4, 8, 16, 32 typical for local environments<br>Models:<br>- `gpt-oss-20b`<br>- `gpt-oss-120b`<br>- `Qwen3 Coder 30B A3B`<br>- `Qwen2.5 Coder 7B`<br>- `Gemma 3 4B QAT`<br>- `GLM 4.5 Air`<br>Feel free to request additional benchmarks for models and use cases.<br># Benchmarks<br>Build with:<br>```<br>cmake -B build-cuda -DGGML_CUDA=ON<br>cmake --build build-cuda -j<br>```<br>Using the following commands:<br>```<br># sequential requests<br>llama-bench -m [model.gguf] -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0<br># parallel requests<br>llama-batched-bench -m [model.gguf] -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap<br>```<br>#### Results<br>[https://github.com/ggml-org/llama.cpp/blob/master/benches/dgx-spark/dgx-spark.md](https://github.com/ggml-org/llama.cpp/blob/master/benches/dgx-spark/dgx-spark.md)<br># Evals<br>```<br># server for gpt-oss-120b evals<br>llama-server -hf ggml-org/gpt-oss-120b-GGUF --ctx-size 1048576 -np 8 --jinja -ub 2048 -b 2048 -ngl 99 --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.01 --chat-template-kwargs '{"reasoning_effort": "high"}' --port 8066 --no-mmap<br># eval script from https://github.com/openai/gpt-oss<br>OPENAI_API_KEY=x python -m gpt_oss.evals --base-url http://localhost:8066/v1 --eval aime25 --sampler chat_completions --model openai/gpt-oss-120b --reasoning-effort high --n-threads 8<br>```<br>- 8x AIME25, `gpt-oss-120b`, `high`: [`93.75%`](https://github.com/ggml-org/llama.cpp/blob/master/benches/dgx-spark/run-aime-120b-t8-x8-high.log)<br>#### History<br>- `2025 Oct 14 (b6761)` [`7ea15bb`](https://github.com/ggml-org/llama.cpp/commit/7ea15bb64c81e3813eb0babf9a57e1bc5697f569) Initial numbers<br>- `2025 Oct 15 (b6767)` [`5acd455`](https://github.com/ggml-org/llama.cpp/commit/5acd455460f457942d8dd02e3dd9b1eebfce99fe) Improved decode via [CUDA: Changing the CUDA scheduling strategy to spin #16585](https://github.com/ggml-org/llama.cpp/pull/16585)<br>- `2025 Oct 26 (b6845)` [`73a48c9`](https://github.com/ggml-org/llama.cpp/commit/73a48c9790d320476b3e5ef75bda09f2f8269e6e) Various improvements + disabled mmap<br>- `2025 Nov 09 (b6989)` [`eeee367`](https://github.com/ggml-org/llama.cpp/commit/eeee367de51fb34d46c8103fc0ae827e84d94470) Various improvements<br>- `2026 Feb 05 (b7946)` [`3795cc1`](https://github.com/ggml-org/llama.cpp/commit/3795cc1e89e16fbc145f8a5457ea30abd86e0d1d) Various improvements<br>## Model loading performance<br>- [Performance of llama.cpp on NVIDIA DGX Spark #16578 (reply in thread)](https://github.com/ggml-org/llama.cpp/discussions/16578#discussioncomment-14849584)<br>## More info<br>- [NVIDIA DGX Spark Arrives for World’s AI Developers](https://nvidianews.nvidia.com/news/nvidia-dgx-spark-arrives-for-worlds-ai-developers)<br>- [guide : setting up NVIDIA DGX Spark with ggml](https://github.com/ggml-org/llama.cpp/discussions/16514) |

11You must be logged in to vote

👍40🎉4❤️9🚀5

All reactions

- 👍40
- 🎉4
- ❤️9
- 🚀5

## Replies:   32 comments  ·  119 replies

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/4948919?s=64&v=4)\ Saren-Arterius](https://github.com/Saren-Arterius) [on Oct 14, 2025Oct 14, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14678523)

|     |
| --- |
| Thanks for the benchmark! I would like to request additional benchmark for a very popular model GLM-4.5-Air-FP8:<br>[https://huggingface.co/zai-org/GLM-4.5-Air-FP8](https://huggingface.co/zai-org/GLM-4.5-Air-FP8)<br>and quants for it:<br>- Q4\_K\_M<br>- Q6\_K<br>- Q8 (if possible)<br>  <br>  [https://huggingface.co/unsloth/GLM-4.5-Air-GGUF/tree/main](https://huggingface.co/unsloth/GLM-4.5-Air-GGUF/tree/main) |

4You must be logged in to vote

All reactions

1 reply


[![@Saren-Arterius](https://avatars.githubusercontent.com/u/4948919?s=60&v=4)](https://github.com/Saren-Arterius)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [Saren-Arterius](https://github.com/Saren-Arterius) [on Oct 14, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14682213)

|     |
| --- |
| Saw the benchmark results. Thank you so much for the work! Appreciate very much. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/57131752?s=64&v=4)\ SinaYa](https://github.com/SinaYa) [on Oct 14, 2025Oct 14, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14680252)

|     |
| --- |
| Hi. It would be great to see a Qwen Next 80B benchmark for these two models:<br>[https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8](https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound)<br>(Has acceptable t/s even on CPU... I'm not sure if this one runs on llama.cpp)<br>[https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8)<br>(Official quants)<br>Thanks. |

4You must be logged in to vote

All reactions

3 replies


[![@sorasoras](https://avatars.githubusercontent.com/u/6722084?s=60&v=4)](https://github.com/sorasoras)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [sorasoras](https://github.com/sorasoras) [on Oct 14, 2025Oct 14, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14680874)

|     |
| --- |
| Not support yet with open pr currently |

All reactions

[![@icsy7867](https://avatars.githubusercontent.com/u/3788162?s=60&v=4)](https://github.com/icsy7867)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [icsy7867](https://github.com/icsy7867) [on Oct 14, 2025Oct 14, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14681231)

|     |
| --- |
| > Hi. It would be great to see a Qwen Next 80B benchmark for these two models:<br>> <br>> [https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8](https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound) (Has acceptable t/s even on CPU... I'm not sure if this one runs on llama.cpp)<br>> <br>> [https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8) (Official quants)<br>> <br>> Thanks.<br>Yeah I really want to see the performance of a specific model comparing full 16 bit precision, Q8, Q4, FP4 and FP8.<br>None the less, thank you for the wonderful data! |

All reactions

[![@slewsys](https://avatars.githubusercontent.com/u/418762?s=60&v=4)](https://github.com/slewsys)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [slewsys](https://github.com/slewsys) [on Feb 8Feb 8, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15731159)

|     |
| --- |
| [Qwen3-Next-80B-A3B-Instruct-GGUF](https://huggingface.co/ggml-org/Qwen3-Next-80B-A3B-Instruct-GGUF) |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/126896609?s=64&v=4)\ mfarme](https://github.com/mfarme) [on Oct 14, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14681451)

|     |
| --- |
| Getting similar performance with my Farmework Desktop. Thanks for helping my FOMO. |

8You must be logged in to vote

All reactions

12 replies


Show 7 previous replies

[![@LucidityCrash](https://avatars.githubusercontent.com/u/49124523?s=60&v=4)](https://github.com/LucidityCrash)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [LucidityCrash](https://github.com/LucidityCrash) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14688515)

|     |
| --- |
| > Someone please help explain this to me? I am not trying to bash on this machine, I am just trying to understand the justification for paying almost twice as much for the same performance with similar specs.<br>I'm sure the connectx-7 200GB networking has something to do with the pricing difference :) |

👍4

All reactions

- 👍4

[![@cocoderss](https://avatars.githubusercontent.com/u/159393146?s=60&v=4)](https://github.com/cocoderss)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [cocoderss](https://github.com/cocoderss) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14689166)

|     |
| --- |
| > btw it's most likely a much better choice if you want GB10 to buy the Asus GB10 systems for $1k less (at least that's what I did) - DGX Spark is more expensive but it's not the only choice<br>Interesting, the Asus GB10 seems to run with 240W power adapter, much higher than the DGX Spark. I wonder if you will get more performance given the higher power intake. |

All reactions

[![@icsy7867](https://avatars.githubusercontent.com/u/3788162?s=60&v=4)](https://github.com/icsy7867)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [icsy7867](https://github.com/icsy7867) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14689417)

|     |
| --- |
| > > btw it's most likely a much better choice if you want GB10 to buy the Asus GB10 systems for $1k less (at least that's what I did) - DGX Spark is more expensive but it's not the only choice<br>> <br>> Interesting, the Asus GB10 seems to run with 240W power adapter, much higher than the DGX Spark. I wonder if you will get more performance given the higher power intake.<br>I havent seen the specs. But its possible ASUS just used a power adapter with a high enough rating for the device? For example, I can plug a 90watt compatible power adapter into my 45watt laptop. It will pull what it needs to. |

All reactions

[![@geerlingguy](https://avatars.githubusercontent.com/u/481677?s=60&v=4)](https://github.com/geerlingguy)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [geerlingguy](https://github.com/geerlingguy) [on Oct 16, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14693953)

|     |
| --- |
| [@bartlettroscoe](https://github.com/bartlettroscoe) i benched gpt-oss 120b on Framework Desktop a couple months ago: [geerlingguy/ai-benchmarks#21 (comment)](https://github.com/geerlingguy/ai-benchmarks/issues/21#issuecomment-3164570956) |

👍2

All reactions

- 👍2

[![@Djip007](https://avatars.githubusercontent.com/u/3705339?s=60&v=4)](https://github.com/Djip007)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [Djip007](https://github.com/Djip007) [on Oct 21, 2025Oct 21, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14744756)

| with "correct" rocm and build I get:

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp1 | 45.40 ± 0.01 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp2 | 57.58 ± 0.95 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp3 | 74.03 ± 2.34 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp4 | 90.93 ± 2.95 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp8 | 142.31 ± 5.57 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp12 | 173.14 ± 12.88 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp16 | 205.43 ± 6.72 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp24 | 235.43 ± 11.38 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp32 | 234.24 ± 10.83 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp48 | 216.49 ± 10.21 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp64 | 311.52 ± 7.33 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp96 | 386.08 ± 10.33 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp128 | 446.85 ± 6.77 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp192 | 509.42 ± 8.09 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp256 | 594.22 ± 9.46 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp384 | 698.31 ± 3.26 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp512 | 763.53 ± 4.88 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp768 | 845.23 ± 6.57 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp1024 | 927.17 ± 1.20 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp1536 | 987.73 ± 1.96 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp2048 | 1017.17 ± 4.10 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp3072 | 939.48 ± 2.72 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp4096 | 953.72 ± 1.16 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | tg16 | 45.43 ± 0.01 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 999 | 2048 | 1 | 0 | pp512+tg64 | 264.68 ± 0.82 | |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/139727413?s=64&v=4)\ netrunnereve](https://github.com/netrunnereve) [on Oct 14, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14682382)   Collaborator

|     |
| --- |
| Can you run the classic llama 2 7B Q4\_0 so it can be compared [on the chart](https://github.com/ggml-org/llama.cpp/discussions/15013)? |

5You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/1659141?s=64&v=4)\ atsyplikhin](https://github.com/atsyplikhin) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14682932)

|     |
| --- |
| Super interesting, thanks for sharing, Georgi!<br>> `llama-bench -m [model.gguf] -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048`<br>Could you please help me understand: Does "-d" mean KV cache length before the "-p" prefill happens? What does "-ub" define, eg batch size? |

1You must be logged in to vote

All reactions

1 reply


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14687018)   Maintainer  Author

|     |
| --- |
| > Does "-d" mean KV cache length before the "-p" prefill happens?<br>Yes.<br>> What does "-ub" define, eg batch size?<br>Yes. |

❤️1

All reactions

- ❤️1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/8567128?s=64&v=4)\ beebopkim](https://github.com/beebopkim) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14682983)

|     |
| --- |
| Could you add llama2-7b result to [#15013](https://github.com/ggml-org/llama.cpp/discussions/15013)? |

2You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/6314556?s=64&v=4)\ Ramalama2](https://github.com/Ramalama2) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14684223)

|     |
| --- |
| Awesome, thank you!<br>So for gpt-oss-120B around 35 tokens/s on dgx spark.<br>On vllm im getting with 131k context and at almost any length around 180 tokens/s on a 300W RTX6000 96gb Max-Q edition.<br>So whats the sense of a dgx spark? I mean sure it has 128gb memory, but i can offload bigger models between 96gb vram and the rest to normal Ram (CPU)...<br>So in the end i can run even bigger models and even faster as the dgx could.<br>Its too expensive for what it offers. If the DGX Spark would be around 2k, like the Ryzen Max 395+ Mini-PC's it would be fine and okay.<br>But for 4k usd/eur its absolutely senseless...<br>PS: And a Mac Mini/Studio is a much better option at 4k usd/eur, compared to a DGX Sparc. |

6You must be logged in to vote

👍8

All reactions

- 👍8

9 replies


Show 4 previous replies

[![@Ramalama2](https://avatars.githubusercontent.com/u/6314556?s=60&v=4)](https://github.com/Ramalama2)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [Ramalama2](https://github.com/Ramalama2) [on Oct 15, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14692528)

|     |
| --- |
| Guys, please dont take fp4 or fp8 as a win.<br>Let me explain:<br>I do compare embedding models in different quantisations (for my project [@work](https://github.com/work)).<br>Comparing embedding Models is actually great, because you can simply query the resulting vector database and see the quantisation impacts.<br>From my tests, no matter which Model, be it Qwen3-Embedding or BGE-M3 or anything else, the impact of Quantisation is Huge!<br>FP32 is Amazing<br>BF16 is still Amazing<br>int8/Q8 = you see already a degradation because the results start to differ, but only 5-10% of the results are different.<br>Q4 = 50% of the results are different, almost unusable Model<br>So you Guys want to tell me that FP4 is a win?<br>In my Opinion FP8 is fine and usable, but FP4 will be unusable crap.<br>No Matter what the Marketing says, 1% quality loss is a huge lie!!!<br>I didnt tested fp4 tho, not even fp8, so i cant say for sure.<br>But from my experience with all other quantisations fp4 should be crap.<br>Cheers! |

❤️3

All reactions

- ❤️3

[![@icsy7867](https://avatars.githubusercontent.com/u/3788162?s=60&v=4)](https://github.com/icsy7867)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [icsy7867](https://github.com/icsy7867) [on Oct 15, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14692579)

|     |
| --- |
| It depends on the model. In many cases, in my experience FP4 does a fantastic job. Also NVFP4 has the potential to be amazing.<br>So is it situational? Sure, it can be. But I don't think it's something that can be ignored.<br>Also, FP8 is also great, I have found little reason to not use it. |

👍4

All reactions

- 👍4

[![@lhl](https://avatars.githubusercontent.com/u/2581?s=60&v=4)](https://github.com/lhl)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [lhl](https://github.com/lhl) [on Oct 17, 2025Oct 18, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14714912)

|     |
| --- |
| I'd agree that everyone should eval for their particular downstream tasks rather than just trusting perplexity or KLD. When running quants on my 405B model I ran JA MT-Bench evals and was surprised to find a bigger difference with FP8-Dynamic than IQ3\_M.<br>[@icsy7867](https://github.com/icsy7867) I know you're just theory-crafting instead of running tests, but see my PRO 6000 TensorRT/NVFP4 benchmark below, but there is zero throughput benefit from NVFP4. Maybe related to [NVIDIA/TransformerEngine#2255](https://github.com/NVIDIA/TransformerEngine/issues/2255) \- I never use TensorRT and it's impossible to build so I just used the latest docker for my tests (tensorrt-llm/release:1.2.0rc0) but I've put my full scripts/details online so it's easy for anyone to rent any GPU they want to check any configuration/variation for themselves.<br>[#16578 (reply in thread)](https://github.com/ggml-org/llama.cpp/discussions/16578#discussioncomment-14713170) |

❤️1

All reactions

- ❤️1

[![@Djip007](https://avatars.githubusercontent.com/u/3705339?s=60&v=4)](https://github.com/Djip007)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [Djip007](https://github.com/Djip007) [on Oct 21, 2025Oct 21, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14744794)

| yes it rely depend on model. for exemple I get for Mistral-SMAL:

|  | BF16 | Q8\_0\_L | Q8\_0 | Q8\_0 Q8\_0 | Q6\_K | Q6\_K Q8\_0 | Q5\_K\_M | Q4\_K\_M | Q3\_K\_M |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| Mean PPL | 5.377047 | 5.417646 | 5.428002 | 5.429658 | 5.433468 | 5.432926 | 5.448926 | 5.521099 | 5.798507 |
| Mean KLD |  | 0.008340 | 0.010369 | 0.010459 | 0.012241 | 0.012291 | 0.014935 | 0.027426 | 0.079385 |
| Maximum KLD |  | 2.048998 | 3.975800 | 1.263743 | 5.553815 | 5.662407 | 3.943127 | 4.050639 | 7.999546 |
| 99.9% KLD |  | 0.204782 | 0.223453 | 0.219347 | 0.247532 | 0.250371 | 0.367634 | 0.993010 | 2.745419 |
| 99.0% KLD |  | 0.078322 | 0.087357 | 0.087095 | 0.099235 | 0.099381 | 0.123670 | 0.250287 | 0.844125 |
| 95.0% KLD |  | 0.032427 | 0.037600 | 0.038312 | 0.043401 | 0.043684 | 0.050811 | 0.088569 | 0.267027 |
| 90.0% KLD |  | 0.019813 | 0.023899 | 0.024312 | 0.027942 | 0.028040 | 0.032904 | 0.055239 | 0.157323 |
| Median KLD |  | 0.003369 | 0.005111 | 0.005167 | 0.006354 | 0.006390 | 0.007717 | 0.013581 | 0.036258 |
| 10.0% KLD |  | 0.000082 | 0.000128 | 0.000131 | 0.000159 | 0.000163 | 0.000188 | 0.000353 | 0.001116 |
| 5.0% KLD |  | 0.000016 | 0.000027 | 0.000028 | 0.000036 | 0.000037 | 0.000043 | 0.000087 | 0.000311 |
| 1.0% KLD |  | -0.000000 | 0.000001 | 0.000001 | 0.000003 | 0.000003 | 0.000003 | 0.000010 | 0.000045 |
| 0.1% KLD |  | -0.000016 | -0.000011 | -0.000010 | -0.000007 | -0.000007 | -0.000007 | -0.000001 | 0.000008 |
| Minimum KLD |  | -0.000157 | -0.000188 | -0.000198 | -0.000248 | -0.000164 | -0.000149 | -0.000273 | -0.000017 |
| Same top p |  | 95.971 | 94.905 | 94.947 | 94.457 | 94.394 | 94.030 | 92.372 | 88.237 | |

All reactions

[![@icsy7867](https://avatars.githubusercontent.com/u/3788162?s=60&v=4)](https://github.com/icsy7867)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [icsy7867](https://github.com/icsy7867) [on Oct 21, 2025Oct 22, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14746317)

|     |
| --- |
| > I'd agree that everyone should eval for their particular downstream tasks rather than just trusting perplexity or KLD. When running quants on my 405B model I ran JA MT-Bench evals and was surprised to find a bigger difference with FP8-Dynamic than IQ3\_M.<br>> <br>> [@icsy7867](https://github.com/icsy7867) I know you're just theory-crafting instead of running tests, but see my PRO 6000 TensorRT/NVFP4 benchmark below, but there is zero throughput benefit from NVFP4. Maybe related to [NVIDIA/TransformerEngine#2255](https://github.com/NVIDIA/TransformerEngine/issues/2255) \- I never use TensorRT and it's impossible to build so I just used the latest docker for my tests (tensorrt-llm/release:1.2.0rc0) but I've put my full scripts/details online so it's easy for anyone to rent any GPU they want to check any configuration/variation for themselves.<br>> <br>> [#16578 (reply in thread)](https://github.com/ggml-org/llama.cpp/discussions/16578#discussioncomment-14713170)<br>I appreciate the edit you did there. But you arent wrong, I wish I had a Blackwell gpu to test. But I am surprised the 6000 Pro doesnt have a speedup there from the FP4 tensor cores. Your data is much appreciated though, thanks. |

👍1

All reactions

- 👍1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/159393146?s=64&v=4)\ cocoderss](https://github.com/cocoderss) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14687993)

|     |
| --- |
| [@ggerganov](https://github.com/ggerganov) Are there llama.cpp benchmarks for the AGX Thor? It seems it's similar offering but Nvidia markets it as twice as fast.<br>There are no official detailed spec sheet for the DGX Spark to make a comparison to the Thor (2560 cuda cores and 92 tensor cores), but Nvidia claims 2PLOPS (sparse FP4) for the Thor and 1PFLOPS (sparse FP4) for the Spark.<br>I guess this might only affect batching, but it would be interesting to know given that Thor is **cheaper** than Spark. |

1You must be logged in to vote

👀1

All reactions

- 👀1

6 replies


Show 1 previous reply

[![@woachk](https://avatars.githubusercontent.com/u/24752637?s=60&v=4)](https://github.com/woachk)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [woachk](https://github.com/woachk) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14688238)

|     |
| --- |
| Quick tldr:<br>Thor is sm\_110 (formerly sm\_101) with the datacenter-style tensor cores - including tensor memory. And no raytracing cores. While Spark is sm\_121 with the full consumer Blackwell feature set.<br>Thor and Spark have relatively similar memory bandwidth. The Thor CPU is _much_ slower.<br>Vector throughput on Thor is 1/3rd of the one on DGX Spark but you get twice the matrix throughput.<br>Thor has 4 cursed Synopsys 25GbE NICs (set to 10GbE by default, see [https://docs.nvidia.com/jetson/archives/r38.2/DeveloperGuide/SD/Kernel/Enable25GbEthernetOnQSFP.html](https://docs.nvidia.com/jetson/archives/r38.2/DeveloperGuide/SD/Kernel/Enable25GbEthernetOnQSFP.html) as it doesn't have auto-negociation of the link rate) exposed via a QSFP connector providing 4x25GbE while Spark systems have regular ConnectX-7.<br>Thor uses a downstream L4T stack instead of regular NVIDIA drivers unlike Spark. But at least the CUDA SDK is the same unlike prior Tegras. Oh and you get less other IO too.<br>Side note: might be better to also consider GB10 systems from OEMs. Those are available for cheaper than AGX Thor devkits too. |

👍7👎2

All reactions

- 👍7
- 👎2

[![@cocoderss](https://avatars.githubusercontent.com/u/159393146?s=60&v=4)](https://github.com/cocoderss)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [cocoderss](https://github.com/cocoderss) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14688371)

|     |
| --- |
| > I'm not familiar with AGX Thor. But if you have one, you can easily run the same benchmarks on it.<br>I don't have one unfortunately, hoping whoever does will run those benchmarks.<br>> Vector throughput on Thor is 1/3rd of the one on DGX Spark but you get twice the matrix throughput.<br>This is a very weird and interesting tradeoff. |

All reactions

[![@yf225](https://avatars.githubusercontent.com/u/4063635?s=60&v=4)](https://github.com/yf225)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [yf225](https://github.com/yf225) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14691878)

|     |
| --- |
| > Thor is sm\_110 (formerly sm\_101) with the datacenter-style tensor cores - including tensor memory<br>[@woachk](https://github.com/woachk) does "tensor memory" here refer to TMEM? |

All reactions

[![@woachk](https://avatars.githubusercontent.com/u/24752637?s=60&v=4)](https://github.com/woachk)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [woachk](https://github.com/woachk) [on Oct 15, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14693006)

|     |
| --- |
| Yes. |

👍1

All reactions

- 👍1

[![@letsrock85](https://avatars.githubusercontent.com/u/4653524?s=60&v=4)](https://github.com/letsrock85)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [letsrock85](https://github.com/letsrock85) [on Nov 8, 2025Nov 8, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14912328)

|     |
| --- |
| Here're my two cents - AGX Thor bench results:<br> ![image_2025-11-08_14-17-01](https://private-user-images.githubusercontent.com/4653524/511714071-cafea719-19e4-4522-ae5e-4937d1b77b62.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii80NjUzNTI0LzUxMTcxNDA3MS1jYWZlYTcxOS0xOWU0LTQ1MjItYWU1ZS00OTM3ZDFiNzdiNjIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAyMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMjNUMDYwNzIzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzEyZDNjYzNmZWNlMzRkY2YzNDNiYWJkMWFjNGE5YzdjZGU2MTE2Yzg0M2Q1NzU0YjBlNjc2NmY4MDhlOTAyNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.R29QGhS8apsOdvJMTH0aEsjlVJ2WLpyNpZda8CQ799A) <br>And Asus Ascent GX10 ( dgx spark):<br> ![image_2025-11-08_14-33-29](https://private-user-images.githubusercontent.com/4653524/511714149-49ed9361-d8e8-4530-b432-639163ee54f4.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii80NjUzNTI0LzUxMTcxNDE0OS00OWVkOTM2MS1kOGU4LTQ1MzAtYjQzMi02MzkxNjNlZTU0ZjQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAyMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMjNUMDYwNzIzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzRkMTJjNzZlOGIzODhiZmU2YjEzYTkyMWI5YmI3YjY3MTAxYzllMzc5YWVjYzYzZTU4ZWNjYmY1M2YxN2IwNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.DAfLVUvDA2zKeLk44n8QuHdfoPR4vQulhsQrXRL9mYI) <br>I want to point out one thing - I discovered that THOR gives a 22-28% speed boost on Generative AI (video/image generation)!<br>[https://x.com/letsrock\_85/status/1985927672581476427?s=20](https://x.com/letsrock_85/status/1985927672581476427?s=20) |

👍2

All reactions

- 👍2

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/13773563?s=64&v=4)\ eous](https://github.com/eous) [on Oct 15, 2025Oct 15, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14690612)

|     |
| --- |
| For those curious about Thor performance<br>(All models are the same as linked in the original benchmark with the same command)<br>llama.cpp git commit: [`f9fb33f`](https://github.com/ggml-org/llama.cpp/commit/f9fb33f2630b4b4ba9081ce9c0c921f8cd8ba4eb)<br>Jetpack 7.0 \[L4T 38.2.2\]<br>Docker container: nvcr.io/nvidia/pytorch:25.09-py3<br>MAXN and jetson\_clocks enabled<br>## gpt-oss-20b-gguf<br>```<br># ./bin/llama-bench -m /workspace/models/gpt-oss-20b-GGUF/gpt-oss-20b-mxfp4.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048<br>ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no<br>ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no<br>ggml_cuda_init: found 1 CUDA devices:<br>  Device 0: NVIDIA Thor, compute capability 11.0, VMM: yes<br>| model                          |       size |     params | backend    | ngl | n_ubatch | fa |            test |                  t/s |<br>| ------------------------------ | ---------: | ---------: | ---------- | --: | -------: | -: | --------------: | -------------------: |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |          pp2048 |       2008.85 ± 4.18 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |            tg32 |         60.85 ± 0.17 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d4096 |       1862.13 ± 4.80 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d4096 |         55.03 ± 0.06 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d8192 |       1740.90 ± 3.24 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d8192 |         53.58 ± 0.18 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d16384 |       1446.75 ± 3.01 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d16384 |         52.49 ± 1.94 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d32768 |       1193.93 ± 0.72 |<br>| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d32768 |         48.33 ± 0.04 |<br>build: f9fb33f2 (6771)<br>```<br>## Qwen3-Coder-30B-A3B-Instruct-Q8\_0-GGUF<br>```<br># ./bin/llama-bench -m /workspace/models/Qwen3-Coder-30B-A3B-Instruct-Q8_0-GGUF/qwen3-coder-30b-a3b-instruct-q8_0.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048<br>ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no<br>ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no<br>ggml_cuda_init: found 1 CUDA devices:<br>  Device 0: NVIDIA Thor, compute capability 11.0, VMM: yes<br>| model                          |       size |     params | backend    | ngl | n_ubatch | fa |            test |                  t/s |<br>| ------------------------------ | ---------: | ---------: | ---------- | --: | -------: | -: | --------------: | -------------------: |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |          pp2048 |       1654.25 ± 1.80 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |            tg32 |         44.26 ± 0.11 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d4096 |       1410.87 ± 2.22 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d4096 |         39.46 ± 0.04 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d8192 |       1228.69 ± 1.78 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d8192 |         36.88 ± 0.13 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d16384 |        985.39 ± 7.04 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d16384 |         33.55 ± 0.01 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d32768 |        686.45 ± 0.93 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d32768 |         26.92 ± 0.05 |<br>build: f9fb33f2 (6771)<br>```<br>## gpt-oss-120b<br>```<br># ./bin/llama-bench -m /workspace/models/gpt-oss-120b-GGUF/gpt-oss-120b-mxfp4-00001-of-00003.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048<br>ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no<br>ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no<br>ggml_cuda_init: found 1 CUDA devices:<br>  Device 0: NVIDIA Thor, compute capability 11.0, VMM: yes<br>| model                          |       size |     params | backend    | ngl | n_ubatch | fa |            test |                  t/s |<br>| ------------------------------ | ---------: | ---------: | ---------- | --: | -------: | -: | --------------: | -------------------: |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |          pp2048 |        967.20 ± 6.04 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |            tg32 |         42.00 ± 0.09 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d4096 |        932.85 ± 2.33 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d4096 |         38.81 ± 0.04 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d8192 |        892.28 ± 2.88 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d8192 |         39.22 ± 1.05 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d16384 |        827.57 ± 1.28 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d16384 |         37.77 ± 0.01 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d32768 |        677.70 ± 1.06 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d32768 |         34.02 ± 0.02 |<br>build: f9fb33f2 (6771)<br>``` |

2You must be logged in to vote

❤️7

All reactions

- ❤️7

9 replies


Show 4 previous replies

[![@woachk](https://avatars.githubusercontent.com/u/24752637?s=60&v=4)](https://github.com/woachk)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [woachk](https://github.com/woachk) [on Oct 16, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14694222)

|     |
| --- |
| That commit only applies the change to `if (prop.major == 12 && prop.minor == 1) {`, wonder if also adding it to 11.0 changes things |

👍1

All reactions

- 👍1

[![@eous](https://avatars.githubusercontent.com/u/13773563?s=60&v=4)](https://github.com/eous)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eous](https://github.com/eous) [on Oct 16, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14703396)

|     |
| --- |
| I did a quick one off build where I removed the conditional around the scheduling block to force spin and I do see a consistent improvement. Just looking at power draw there is a probably at least another 10-20% performance untapped on thor beyond moving it to the spin scheduler. Currently looks like we are mostly cpu bound.<br> ![llama_bench_comparison_dark](https://private-user-images.githubusercontent.com/13773563/502289507-0d8bb5ab-8d1b-4299-ad24-d923450d6268.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii8xMzc3MzU2My81MDIyODk1MDctMGQ4YmI1YWItOGQxYi00Mjk5LWFkMjQtZDkyMzQ1MGQ2MjY4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDIzVDA2MDcyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI1MDY0MGU5OGZmYTU0MGE2NGM4Yzk2ZGQ0ZjU2OWU0ZDg0NDgyYzFiYjlmYWMzMjJhOTE4YmRkM2RlZDg1Y2UmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.8kmFa4aDF45wLtpdBC3fe34ZJpDE9j0LKlpim8TsPnI)  ![llama_batched_comparison_dark](https://private-user-images.githubusercontent.com/13773563/502289510-818e7061-45f2-4195-b9e7-5d7784b473d6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii8xMzc3MzU2My81MDIyODk1MTAtODE4ZTcwNjEtNDVmMi00MTk1LWI5ZTctNWQ3Nzg0YjQ3M2Q2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDIzVDA2MDcyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZhMGIzNDBmZTcyZGM2MGE5ZDNmZGVlMTBmZTI5YzdmN2U1ZjgyMTUwYjJlZGVkYjRiMjkwMmM2M2U2MTdjMWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.aP9gPvOzQRauMpvpgFjZd2oKA35CyngruBvQ-VmsUpQ) <br>## Llama-bench Test Results (Qwen3moe 30B)<br>schedule Default Spin Improvement (%)<br>test<br>pp2048 1654.25 1700.05 2.77<br>pp2048 @ d16384 985.39 992.37 0.71<br>pp2048 @ d32768 686.45 687.30 0.12<br>pp2048 @ d4096 1410.87 1446.22 2.51<br>pp2048 @ d8192 1228.69 1257.35 2.33<br>tg32 44.26 45.67 3.19<br>tg32 @ d16384 33.55 33.62 0.21<br>tg32 @ d32768 26.92 27.05 0.48<br>tg32 @ d4096 39.46 40.64 2.99<br>tg32 @ d8192 36.88 38.09 3.28<br>Average improvement: 1.86%<br>Best improvement: 3.28% (tg32 @ d8192)<br>Worst improvement: 0.12% (pp2048 @ d32768)<br>## Llama-batched-bench Test Results<br>PP=4096:<br>Average throughput improvement: 2.03%<br>Best batch size improvement: B2 (4.48%)<br>Worst batch size improvement: B16 (0.06%)<br>PP=8192:<br>Average throughput improvement: 0.05%<br>Best batch size improvement: B32 (0.07%)<br>Worst batch size improvement: B16 (0.03%)<br>```<br>Spin schedule<br>  Device 0: NVIDIA Thor, compute capability 11.0, VMM: yes<br>Test: llama-bench<br>| model                          |       size |     params | backend    | ngl | n_ubatch | fa |            test |                  t/s |<br>| ------------------------------ | ---------: | ---------: | ---------- | --: | -------: | -: | --------------: | -------------------: |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |          pp2048 |       1700.05 ± 2.02 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |            tg32 |         45.67 ± 0.11 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d4096 |       1446.22 ± 3.54 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d4096 |         40.64 ± 0.05 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |  pp2048 @ d8192 |       1257.35 ± 0.75 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |    tg32 @ d8192 |         38.09 ± 0.09 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d16384 |        992.37 ± 1.89 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d16384 |         33.62 ± 0.01 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 | pp2048 @ d32768 |        687.30 ± 0.48 |<br>| qwen3moe 30B.A3B Q8_0          |  30.25 GiB |    30.53 B | CUDA       |  99 |     2048 |  1 |   tg32 @ d32768 |         27.05 ± 0.03 |<br>Test: llama-batched-bench<br>|    PP |     TG |    B |   N_KV |   T_PP s | S_PP t/s |   T_TG s | S_TG t/s |      T s |    S t/s |<br>|-------|--------|------|--------|----------|----------|----------|----------|----------|----------|<br>|  4096 |     32 |    1 |   4128 |    2.537 |  1614.38 |    0.789 |    40.54 |    3.327 |  1240.92 |<br>|  4096 |     32 |    2 |   8256 |    4.949 |  1655.30 |    1.301 |    49.18 |    6.250 |  1320.87 |<br>|  4096 |     32 |    4 |  16512 |    9.887 |  1657.09 |    1.663 |    76.98 |   11.550 |  1429.62 |<br>|  4096 |     32 |    8 |  33024 |   19.739 |  1660.11 |    2.289 |   111.86 |   22.027 |  1499.25 |<br>|  4096 |     32 |   16 |  66048 |   39.464 |  1660.65 |    3.279 |   156.14 |   42.743 |  1545.23 |<br>|  4096 |     32 |   32 | 132096 |   78.936 |  1660.49 |    5.033 |   203.46 |   83.968 |  1573.16 |<br>|  8192 |     32 |    1 |   8224 |    5.314 |  1541.47 |    0.839 |    38.14 |    6.153 |  1336.50 |<br>|  8192 |     32 |    2 |  16448 |   10.614 |  1543.68 |    1.396 |    45.86 |   12.009 |  1369.61 |<br>|  8192 |     32 |    4 |  32896 |   21.220 |  1544.24 |    1.888 |    67.79 |   23.108 |  1423.59 |<br>|  8192 |     32 |    8 |  65792 |   42.394 |  1545.87 |    2.792 |    91.68 |   45.187 |  1456.01 |<br>|  8192 |     32 |   16 | 131584 |   84.800 |  1545.66 |    4.206 |   121.73 |   89.006 |  1478.37 |<br>|  8192 |     32 |   32 | 263168 |  169.577 |  1545.87 |    6.867 |   149.11 |  176.444 |  1491.51 |<br>``` |

👍1

All reactions

- 👍1

[![@woachk](https://avatars.githubusercontent.com/u/24752637?s=60&v=4)](https://github.com/woachk)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [woachk](https://github.com/woachk) [on Oct 16, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14703736)

|     |
| --- |
| For prompt processing there's a lot more on the table but that means switching to tcgen05 MMA instructions. (Which is a separate instruction set than the regular tensor core one)<br>And there's also the matter of using lower precision MMAs in general |

❤️1

All reactions

- ❤️1

[![@aazzolini](https://avatars.githubusercontent.com/u/37222419?s=60&v=4)](https://github.com/aazzolini)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [aazzolini](https://github.com/aazzolini) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14712711)

|     |
| --- |
| I believe that Thor doesn't support tcgen05 because it doesn't have tensor-memory |

All reactions

[![@woachk](https://avatars.githubusercontent.com/u/24752637?s=60&v=4)](https://github.com/woachk)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [woachk](https://github.com/woachk) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14714309)

|     |
| --- |
| Thor does have tensor memory - it uses the data centre tensor cores (it's sm\_110\[a\]), Spark does not.<br>See [https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-mma-instructions-mma](https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-mma-instructions-mma) |

👍2

All reactions

- 👍2

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/564658?s=64&v=4)\ qdrddr](https://github.com/qdrddr) [on Oct 16, 2025Oct 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14703473)

|     |
| --- |
| Would love to see **accuracy** of the same models on main banchmarks running in DGX as they **will vary** on different HW & FW in addition to the speed.<br>As its clearly sing here [https://artificialanalysis.ai/models/gpt-oss-120b/providers](https://artificialanalysis.ai/models/gpt-oss-120b/providers)<br>![CleanShot 2025-10-16 at 16 41 40](https://private-user-images.githubusercontent.com/564658/502293207-ab3f12cc-d055-4cf8-a35f-7dab117bf62c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii81NjQ2NTgvNTAyMjkzMjA3LWFiM2YxMmNjLWQwNTUtNGNmOC1hMzVmLTdkYWIxMTdiZjYyYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDIzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAyM1QwNjA3MjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02ODI5YTI1YTAyYjllOTZjNTFlN2U3MzI4MDMyZTU2ZDlmN2M2ZjQyMGFkOTQ4ZmU2NTUyYWUxYWZlNDdhMjA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.ZrLBeyAQINr2aGEwS_vQyvb81kZzHHOFMIVbrSoztO0) |

1You must be logged in to vote

👍3

All reactions

- 👍3

1 reply


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Nov 10, 2025Nov 10, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14922378)   Maintainer  Author

|     |
| --- |
| Added AIME25 evals in the post. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/1251237?s=64&v=4)\ jasonburton5](https://github.com/jasonburton5) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14711006)

|     |
| --- |
| Please bench the full Qwen3 coder model |

1You must be logged in to vote

All reactions

2 replies


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14712745)   Maintainer  Author

|     |
| --- |
| There isn't any measurable benefits in terms of quality compared to `Q8_0`, so don't think there is any point in benching that as it is most likely going to perform worse in terms of speed. |

All reactions

[![@jasonburton5](https://avatars.githubusercontent.com/u/1251237?s=60&v=4)](https://github.com/jasonburton5)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [jasonburton5](https://github.com/jasonburton5) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14713039)

|     |
| --- |
| I am just impressed that it might run at all. It's there any bench on fine-tuning? |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/564658?s=64&v=4)\ qdrddr](https://github.com/qdrddr) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14711975)

|     |
| --- |
| Would love to see this this cluster setup in the comparison table too<br>EXO Lab cluster with 2xDGX + MacStudio<br>[https://blog.exolabs.net/nvidia-dgx-spark/](https://blog.exolabs.net/nvidia-dgx-spark/) |

2You must be logged in to vote

All reactions

1 reply


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14712756)   Maintainer  Author

|     |
| --- |
| AFAICT this is vaporware. |

👍2😕1❤️2

All reactions

- 👍2
- 😕1
- ❤️2

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/37222419?s=64&v=4)\ aazzolini](https://github.com/aazzolini) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14712726)

|     |
| --- |
| On the subject of Spark and Thor, I have been looking for alternatives to TensorRT for python-free and community driven inference engine. I'm looking to leverage nvfp4 tensor cores , and wonder if there's any project or folks working to support those in llama.cpp? |

1You must be logged in to vote

All reactions

6 replies


Show 1 previous reply

[![@woachk](https://avatars.githubusercontent.com/u/24752637?s=60&v=4)](https://github.com/woachk)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [woachk](https://github.com/woachk) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14713103)

|     |
| --- |
| The whole Blackwell product range, from the RTX 5050 onwards to the B200/300 through iGPUs |

All reactions

[![@woachk](https://avatars.githubusercontent.com/u/24752637?s=60&v=4)](https://github.com/woachk)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [woachk](https://github.com/woachk) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14713159)

|     |
| --- |
| That said: [NVIDIA/TransformerEngine#2255](https://github.com/NVIDIA/TransformerEngine/issues/2255) |

All reactions

[![@lhl](https://avatars.githubusercontent.com/u/2581?s=60&v=4)](https://github.com/lhl)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [lhl](https://github.com/lhl) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14713170)

| Just as an FYI, I don't have a Spark but I tested NVP4 on an RTX PRO 6000 (Llama 3.1 8B Instruct). NVP4 w/ TensorRT does not perform better than llama.cpp at bs=1, and at higher concurency, doesn't take a lead until c=32.

I didn't test quality loss, but from a pure throughput perspective, I don't think the current NVFP4 implementation is particularly good. Certainly not worth all the custom quanting and other hassles...

| Config | Req/s | Prefill Tok/s | Decode Tok/s | Total Tok/s | Max Out Tok/s | TTFT mean | TTFT med | TTFT p99 | TPOT mean | TPOT med | TPOT p99 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| llama.cpp.q4\_k\_m | **1.65** | **1683.45** | **207.16** | **1890.61** | **223.00** | 74.17 | 75.75 | 85.71 | **4.36** | **4.22** | 8.40 |
| sglang.fp8-auto | 1.15 | 1173.85 | 142.83 | 1316.68 | 146.00 | 54.88 | 55.31 | 55.79 | 6.61 | 6.62 | 6.62 |
| sglang.fp8-dynamic | 1.04 | 1065.99 | 130.29 | 1196.28 | 132.00 | 55.91 | 56.30 | 57.13 | 7.28 | 7.29 | 7.29 |
| sglang.w4a16 | 1.56 | 1590.93 | 194.85 | 1785.78 | 204.00 | 53.69 | 54.10 | 54.79 | 4.74 | 4.75 | **4.76** |
| trt.fp8 | 0.59 | 605.67 | 74.33 | 680.01 | 76.00 | 39.94 | 40.24 | 40.76 | 13.24 | 13.24 | 13.27 |
| trt.nvfp4 | 0.60 | 608.22 | 74.38 | 682.61 | 76.00 | **30.91** | **31.05** | **31.31** | 13.30 | 13.30 | 13.34 |
| vllm.fp8-dynamic | 0.77 | 789.55 | 94.90 | 884.45 | 98.00 | 34.94 | 35.12 | 36.43 | 10.34 | 10.34 | 10.36 |
| vllm.w4a16 | 1.52 | 1549.83 | 189.81 | 1739.64 | 196.00 | 49.09 | 49.39 | 50.30 | 4.92 | 4.92 | 4.96 | |

All reactions

[![@aazzolini](https://avatars.githubusercontent.com/u/37222419?s=60&v=4)](https://github.com/aazzolini)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [aazzolini](https://github.com/aazzolini) [on Oct 17, 2025Oct 17, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14713909)

|     |
| --- |
| [@lhl](https://github.com/lhl) what's the prefill sequence length in the profiles above?<br>my usecase is pre-fill only at seqlen > 300 |

All reactions

[![@lhl](https://avatars.githubusercontent.com/u/2581?s=60&v=4)](https://github.com/lhl)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [lhl](https://github.com/lhl) [on Oct 17, 2025Oct 18, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14714735)

|     |
| --- |
| This is using a standard vLLM bench - ShareGPT w/ prefill 1024 and decode 128 I believe. If you have a specific use case it's probably best to just trying the device directly - I think they're available for a buck or two on Vast or Runpod.<br>I think the compute is particularly strong for a client card. For example, the PRO 6000 actually beats an H100 on our Whisper inference sweeps. (Still trains much slower though)<br>Here's my LLM sweep scripts (and raw results) btw: [https://github.com/AUGMXNT/speed-benchmarking/tree/main/nvfp4](https://github.com/AUGMXNT/speed-benchmarking/tree/main/nvfp4) |

👍1

All reactions

- 👍1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/2192184?s=64&v=4)\ eugr](https://github.com/eugr) [on Oct 21, 2025Oct 22, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14746095)

| [@ggerganov](https://github.com/ggerganov) \- what flags did you use to compile for DGX Spark? Also, did you set GGML\_CUDA\_ENABLE\_UNIFIED\_MEMORY=1?

I've just got the spark, and I'm not getting the same performance numbers as you. Also, the model loading is super slow. Not sure what's going on, I'm probably missing something.

It does seem to offload layers to GPU properly, but nvtop/nvidia-smi shows host memory utilization growing to quite large numbers (more than 100GB and then it all goes to GPU memory). In comparison, my Strix Halo PC loads the same model 5x faster.

My numbers:

Without GGML\_CUDA\_ENABLE\_UNIFIED\_MEMORY=1:

Model loading time - 1 minute 44 seconds using this command:

```
build/bin/llama-server -m ~/.cache/llama.cpp/ggml-org_gpt-oss-120b-GGUF_gpt-oss-120b-mxfp4-00001-of-00003.gguf -fa 1 -ngl 999 -ub 2048
```

Benchmarks:

```
build/bin/llama-bench -m ~/.cache/llama.cpp/ggml-org_gpt-oss-120b-GGUF_gpt-oss-120b-mxfp4-00001-of-00003.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048
```

| model | size | params | backend | ngl | n\_ubatch | fa | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 | 1737.17 ± 81.66 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 | 45.87 ± 0.74 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d4096 | 1777.81 ± 5.92 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d4096 | 43.41 ± 0.31 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d8192 | 1720.17 ± 8.49 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d8192 | 41.52 ± 0.29 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d16384 | 1512.23 ± 11.81 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d16384 | 38.39 ± 0.15 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d32768 | 1231.86 ± 6.14 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d32768 | 34.29 ± 0.07 |

build: [`03792ad`](https://github.com/ggml-org/llama.cpp/commit/03792ad93609fc67e41041c6347d9aa14e5e0d74) (6816)

With GGML\_CUDA\_ENABLE\_UNIFIED\_MEMORY=1:

Model loading time: 49 seconds

Benchmarks:

| model | size | params | backend | ngl | n\_ubatch | fa | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 | 1672.33 ± 65.23 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 | 40.61 ± 0.38 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d4096 | 1661.97 ± 8.73 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d4096 | 38.29 ± 0.35 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d8192 | 1587.22 ± 12.23 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d8192 | 36.85 ± 0.42 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d16384 | 1384.96 ± 6.77 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d16384 | 34.62 ± 0.22 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | pp2048 @ d32768 | 1124.23 ± 4.65 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | tg32 @ d32768 | 30.47 ± 0.08 |

For comparison, from my GMKTek Evo X2 (AMD AI MAX+ 395), same llama.cpp build, compiled with HIP:

Model loading time: 25 seconds (8 seconds if still in caches!!!)

| model | size | params | backend | ngl | n\_ubatch | fa | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | pp2048 | 999.59 ± 4.31 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | tg32 | 47.49 ± 0.01 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | pp2048 @ d4096 | 824.37 ± 1.16 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | tg32 @ d4096 | 44.23 ± 0.01 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | pp2048 @ d8192 | 703.42 ± 1.54 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | tg32 @ d8192 | 42.52 ± 0.04 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | pp2048 @ d16384 | 514.89 ± 3.86 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | tg32 @ d16384 | 39.71 ± 0.01 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | pp2048 @ d32768 | 348.59 ± 2.11 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | ROCm | 99 | 2048 | 1 | tg32 @ d32768 | 35.39 ± 0.01 |

Any ideas? You benchmarks look closer to what I'd expect from this device. And long loading time makes me think that it is doing some extra mallocs/copying. |

1You must be logged in to vote

All reactions

13 replies


Show 8 previous replies

[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [eugr](https://github.com/eugr) [on Nov 2, 2025Nov 2, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14849584)

| [@ggerganov](https://github.com/ggerganov) \- yep, confirmed that it's the kernel. Most likely this option which appeared in 6.17: NO\_PAGE\_MAPCOUNT.

Compiled NVIDIA 6.17.1 kernel from their repository, and I'm getting fast model loading speed (22 seconds from cold for gpt-oss-120b) AND the same generation benchmarks I get on DGX OS:

| model | size | params | backend | test | t/s |
| --- | --: | --: | --- | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 | 1956.03 ± 9.28 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 | 60.57 ± 0.25 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d4096 | 1637.34 ± 4.86 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d4096 | 54.14 ± 0.08 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d8192 | 1512.01 ± 5.66 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d8192 | 51.54 ± 0.14 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d16384 | 1307.42 ± 3.79 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d16384 | 47.45 ± 0.08 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d32768 | 1027.31 ± 4.79 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d32768 | 40.55 ± 0.13 |

build: [`7db35a7`](https://github.com/ggml-org/llama.cpp/commit/7db35a7958a943be1693879f42d166f152613979) (6922)

This is on Fedora 43 Server with the new compiled kernel. On DGX Spark, of course :) |

👍1

All reactions

- 👍1

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Nov 2, 2025Nov 2, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14849802)   Maintainer  Author

|     |
| --- |
| [@eugr](https://github.com/eugr) Thanks for the follow-up. I have added a section to the post referencing your findings about model load performance. |

👍1

All reactions

- 👍1

[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eugr](https://github.com/eugr) [on Nov 2, 2025Nov 3, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14853641)

|     |
| --- |
| One more thing to note: mmap performance is still mediocre even with 6.17.1, so you **have to** use --no-mmap flag!<br>Loading gpt-oss-120b on 6.17.1 kernel:<br>- with mmap: 1 minute 30 seconds<br>- without mmap (--no-mmap): 22 seconds<br>Same for vLLM, btw. Loading Qwen3-Next-80B-A3B-FP8 takes 8 minutes 44 seconds with default parameters and 1 minute 30 seconds with --safetensors-load-strategy eager (equivalent of --no-mmap), but the downside is much higher RAM consumption by vllm. Good thing that doesn't happen with llama.cpp! |

👍1

All reactions

- 👍1

[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eugr](https://github.com/eugr) [on Nov 19, 2025Nov 19, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15016441)

|     |
| --- |
| Another update: DGX Spark just received an update to 6.14 kernel (6.17 is expected in January). Good news is that model loading is now significantly improved - takes 27 seconds on my machine for gpt-oss-120b compared to 68 seconds on previous 6.11. Still not as fast as 6.17, but close.<br>Mmap performance remains bad, so don't use it. |

All reactions

[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eugr](https://github.com/eugr) [on Nov 21, 2025Nov 21, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15042534)

|     |
| --- |
| Another improvement, suggested by Nvidia folks - increase NVME read-ahead buffer:<br>```<br>sudo bash -c "echo 8192 > /sys/block/nvme0n1/queue/read_ahead_kb"<br>```<br>On kernel 6.17 improves both mmap performance (from almost 2 minutes to 30 seconds) and no-mmap performance (from 20 to 15 seconds). Weirdly enough, works well only with llama.cpp, vllm model loading remains bad.<br>On kernel 6.14 (now standard after a recent update), doesn't affect mmap performance, but improves no-mmap performance similar to 6.17. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/564658?s=64&v=4)\ qdrddr](https://github.com/qdrddr) [on Oct 25, 2025Oct 25, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14781991)

|     |
| --- |
| Throughput is not the only metric.<br>We need to take into account that different HW/FW produce **different accuracy for the same model**.<br>And can vary from a little to drastic difference.<br>Can someone test popular LLMs like gpt-oss? |

1You must be logged in to vote

All reactions

1 reply


[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eugr](https://github.com/eugr) [on Oct 27, 2025Oct 27, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14797395)

|     |
| --- |
| I was reading [this](https://docs.nvidia.com/dgx/dgx-spark-porting-guide/optimization.html) and wonder if the loading speed differences are because under DGX OS it uses older gcc/llvm that doesn't target gb10, and under Fedora it targets gb10:<br>Since LLVM version 21 and gcc version 15, it is also possible to specifically target DGX Spark with -mcpu=gb10. This enables optimizations for the Cortex-X925 and Cortex-A725 cores as well as the optional crypto extension and is thus preferred over a more generic -march switch. When compiling on the Spark itself, this architecture is automatically selected with -march=native. |

All reactions

2 hidden items

Load more…


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/4864089?s=64&v=4)\ spamshaker](https://github.com/spamshaker) [on Nov 16, 2025Nov 16, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-14980101)

| All right, a little dry facts I spotted.

## Chat on M4 Max with 64GB RAM

![image](https://private-user-images.githubusercontent.com/4864089/514835297-afee32c8-e762-4a14-950b-45514751432b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii80ODY0MDg5LzUxNDgzNTI5Ny1hZmVlMzJjOC1lNzYyLTRhMTQtOTUwYi00NTUxNDc1MTQzMmIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAyMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMjNUMDYwNzIzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTZmZjNiY2MxZjMyZjNiMGI3ZGQ5ZmI4ZGNjZTJmZWJjMDYzNWE5M2QzYzM5NDFhY2VlYzVlYzVlZGIzOGE5MCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.IRGuejHzDJknBKqsS5D1KYtnt3Z2Mj4Jdtuw5UQfwSI)

## Chat on Spark with CUDA

![image](https://private-user-images.githubusercontent.com/4864089/514835275-367683fd-e04b-4078-9c1d-f9fcff832c6f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii80ODY0MDg5LzUxNDgzNTI3NS0zNjc2ODNmZC1lMDRiLTQwNzgtOWMxZC1mOWZjZmY4MzJjNmYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAyMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMjNUMDYwNzIzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9M2Y2N2VmOTIwNmM1NmI5MjRiMmY4NTYxYmQwOTk0Y2I0YTQzMjlhOGY2ZTkwYzZiMzA2ZmUxZDc3MDZiOTJiMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.mj_uIgEFS4EG2ZWhxOmzC3Sx2h4wXtoUa0txx27DUTA)

```
 llama-bench -m  /Users/dev/Library/Caches/llama.cpp/ggml-org_gpt-oss-20b-GGUF_gpt-oss-20b-mxfp4.gguf -t 1 -fa 1 -b 2048 -ub 2048 -p 2048,8192,16384,32768
```

```
ggml_metal_device_init: tensor API disabled for pre-M5 and pre-A19 devices
ggml_metal_library_init: using embedded metal library
ggml_metal_library_init: loaded in 0.005 sec
ggml_metal_device_init: GPU name:   Apple M4 Max
ggml_metal_device_init: GPU family: MTLGPUFamilyApple9  (1009)
ggml_metal_device_init: GPU family: MTLGPUFamilyCommon3 (3003)
ggml_metal_device_init: GPU family: MTLGPUFamilyMetal4  (5002)
ggml_metal_device_init: simdgroup reduction   = true
ggml_metal_device_init: simdgroup matrix mul. = true
ggml_metal_device_init: has unified memory    = true
ggml_metal_device_init: has bfloat            = true
ggml_metal_device_init: has tensor            = false
ggml_metal_device_init: use residency sets    = true
ggml_metal_device_init: use shared buffers    = true
ggml_metal_device_init: recommendedMaxWorkingSetSize  = 55662.79 MB
| model                          |       size |     params | backend    | threads | n_ubatch | fa |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | -------: | -: | --------------: | -------------------: |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | Metal,BLAS |       1 |     2048 |  1 |          pp2048 |       1849.79 ± 2.29 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | Metal,BLAS |       1 |     2048 |  1 |          pp8192 |      1613.83 ± 31.03 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | Metal,BLAS |       1 |     2048 |  1 |         pp16384 |      1388.79 ± 19.19 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | Metal,BLAS |       1 |     2048 |  1 |         pp32768 |       1093.58 ± 5.65 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | Metal,BLAS |       1 |     2048 |  1 |           tg128 |        117.83 ± 1.59 |

build: 5da766496 (7030)
```

```
 llama-bench -m /home/dev/.cache/llama.cpp/ggml-org_gpt-oss-20b-GGUF_gpt-oss-20b-mxfp4.gguf -t 1 -fa 1 -b 2048 -ub 2048 -p 2048,8192,16384,32768
```

```
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
 Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes
| model                          |       size |     params | backend    | ngl | threads | n_ubatch | fa |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | ------: | -------: | -: | --------------: | -------------------: |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |       1 |     2048 |  1 |          pp2048 |      3797.76 ± 16.28 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |       1 |     2048 |  1 |          pp8192 |       3718.87 ± 6.86 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |       1 |     2048 |  1 |         pp16384 |       3507.38 ± 7.53 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |       1 |     2048 |  1 |         pp32768 |       3094.77 ± 5.55 |
| gpt-oss 20B MXFP4 MoE          |  11.27 GiB |    20.91 B | CUDA       |  99 |       1 |     2048 |  1 |           tg128 |         86.23 ± 0.25 |

build: c7b7db044 (7067)
```

I guess thats because Metal runs better than CUDA on smaller context if I understand results correctly

| Device | model | size | params | backend | ngl | threads | n\_ubatch | fa | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: | --: |
| MBP | gpt-oss 20B MXFP4 MoE | 11.27 GiB | 20.91 B | Metal,BLAS | x | 1 | 2048 | 1 | tg128 | 117.83 ± 1.59 |
| Spark | gpt-oss 20B MXFP4 MoE | 11.27 GiB | 20.91 B | CUDA | 99 | 1 | 2048 | 1 | tg128 | 86.23 ± 0.25 |

This sounds like a memory‑bandwidth issue, which on the [DGX Spark is limited to only 273 GB/s](https://docs.nvidia.com/dgx/dgx-spark/hardware.html).

[https://news.ycombinator.com/item?id=38703611](https://news.ycombinator.com/item?id=38703611)

* * *

Details

| Spec | MacBook Pro 16″ | NVIDIA DGX Spark |
| --- | --- | --- |
| **Device Type** | High-end laptop / mobile workstation | Desktop “AI supercomputer” mini-PC |
| **Processor / Architecture** | Apple M4 Max (16-core CPU) | 20-core ARM (10 × Cortex-X925 + 10 × Cortex-A725) ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/hardware.html "Hardware Overview — DGX Spark User Guide")) |
| **GPU / Graphics** | Integrated in M4 Max (Apple GPU) | Blackwell GPU (Nvidia), 5th-gen Tensor Cores, 4th-gen RT cores ( [NVIDIA](https://www.nvidia.com/en-us/products/workstations/dgx-spark/ "A Grace Blackwell AI supercomputer on your desk | NVIDIA DGX Spark")) |
| **Memory (RAM / Unified)** | 64 GB unified memory | **128 GB LPDDR5x** unified system memory ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/hardware.html "Hardware Overview — DGX Spark User Guide")) |
| **Memory Bandwidth** | (Apple doesn’t usually disclose same metrics, but very high for unified Apple Silicon) | ~273 GB/s ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/hardware.html "Hardware Overview — DGX Spark User Guide")) |
| **Storage / SSD** | 1 TB SSD | 1 TB or **4 TB NVMe M.2** (self-encrypting) ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/hardware.html "Hardware Overview — DGX Spark User Guide")) |
| **Performance (AI / Compute)** | Strong for general compute, creative workloads, some ML, but not “server-level” AI FLOPS | Up to **1 PFLOP (FP4, sparse)** performance claimed by Nvidia ( [NVIDIA](https://www.nvidia.com/en-us/products/workstations/dgx-spark/ "A Grace Blackwell AI supercomputer on your desk | NVIDIA DGX Spark")) |
| **Connectivity / Ports** | — (depends on exact Mac model, but you mentioned: 3x Thunderbolt, HDMI, SDXC, MagSafe 3) | 4 × USB Type-C, 1 × HDMI 2.1a, 10 GbE (RJ-45), ConnectX-7 NIC, Wi-Fi 7, Bluetooth 5.4 ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/hardware.html "Hardware Overview — DGX Spark User Guide")) |
| **Power / Power Adapter** | 140 W USB-C power adapter | External **240 W** power supply ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/hardware.html "Hardware Overview — DGX Spark User Guide")) |
| **Size / Form Factor** | Laptop — portable, integrated screen | Very compact desktop: 150 mm × 150 mm × 50.5 mm; ~1.2 kg ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/hardware.html "Hardware Overview — DGX Spark User Guide")) |
| **Operating System / Software** | macOS | **NVIDIA DGX OS**, with CUDA, AI frameworks, container support ( [NVIDIA Docs](https://docs.nvidia.com/dgx/dgx-spark/system-overview.html "System Overview — DGX Spark User Guide")) |
| **Use Case Strengths** | Mobility, general productivity, creative work, development | AI training / inference, local LLM fine-tuning, prototyping large models (up to ~200B parameters) ( [CHIP - Technologie mamy we krwi!](https://www.chip.pl/2025/11/czym-jest-nvidia-dgx-spark "Ten komputer jest mniejszy od mojego routera, a bije na głowę wydajność potężnego peceta")) |
| **Thermal / Power Considerations** | Optimized for mobile thermal envelope | High-performance thermal system, but some report thermal throttling / lower-than-claimed power draw ( [Reddit](https://www.reddit.com//r/LocalLLaMA/comments/1ohtp6d "Bad news: DGX Spark may have only half the performance claimed.")) |
| **Price / Positioning** | ~6'000 USD | ~4'000 USD for DGX Spark per Nvidia’s spec sheet ( [NVIDIA](https://www.nvidia.com/en-us/products/workstations/dgx-spark/ "A Grace Blackwell AI supercomputer on your desk | NVIDIA DGX Spark")) |

# Tokens Per Sec

at 16 Nov 2025

## On MacBook Pro M4 Max:

1. Installation



```
brew install llama.cpp
```

2. Running



```
llama-server -hf ggml-org/gpt-oss-20b-GGUF --ctx-size 0 --jinja -ub 2048 -b 2048
```

3. Using

I used Brave Browser to go to [http://localhost:8080/](http://localhost:8080/)


## The result 117.32 tokens/sec

## Steps On DGX Spark

1. Access to device



```
# from remote terminal
ssh -L 8081:localhost:8080 user@spark-local
```

2. Installation 💩



```
# There is a https://github.com/ggml-org/llama.cpp/discussions/16514 but it is a script that compiles sources
# so fallback to compilation
```

3. Compilation



```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp/
cmake -B build -DGGML_NATIVE=OFF -DGGML_CUDA=ON -DGGML_BACKEND_DL=ON -DGGML_CPU_ALL_VARIANTS=ON -DLLAMA_BUILD_TESTS=OFF -DCMAKE_EXE_LINKER_FLAGS=-Wl,--allow-shlib-undefined .
cmake --build build-cuda -j
sudo cp build-cuda/bin/* /usr/local/bin/
```

4. Running



```
     # finally :)
     llama-server -hf ggml-org/gpt-oss-20b-GGUF --ctx-size 0 --jinja -ub 2048 -b 2048
```

5. Using (SSH tunneling)


I used Brave Browser to go to [http://localhost:8081/](http://localhost:8081/)


## The result 84.67 tokens/sec

```
Using the chat directly on Spark Machine via Brave Browser I got wierd result ~72 tokens/sec
```

# Conclusion

Price Rate: 6000/4000 => 1.5

Tokens Rate: 117.32/84.67 => 1.38

Dev Rate: Hard to say

I Would bet the Mac Studio M4 Max with 128GB RAM (at price ~5000 USD) would be better for price rate comparison for headless machines, but I

guess that the performance would be the same as for MacBook Pro M4 Max |

0You must be logged in to vote

👍1

All reactions

- 👍1

1 reply


[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [eugr](https://github.com/eugr) [on Nov 19, 2025Nov 19, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15016425)

|     |
| --- |
| Well, yes, M4 Max has double memory bandwidth compared to Spark, so inference will be faster. Prompt processing, however, is faster on Spark because of better GPU. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/2192184?s=64&v=4)\ eugr](https://github.com/eugr) [on Nov 20, 2025Nov 21, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15033766)

| Well, someone had to do it :)

Running Unsloth/Qwen3-VL-235B-A22B-Instruct:Q4\_K\_XL on dual Sparks with full context (but tested up to 32K):

```
eugr@spark:~/llm/llama.cpp$ build/bin/llama-bench -m ~/.cache/llama.cpp/unsloth_Qwen3-VL-235B-A22B-Instruct-GGUF_UD-Q4_K_XL_Qwen3-VL-235B-A22B-Instruct-UD-Q4_K_XL-00001-of-00003.gguf --rpc 192.168.177.12:15001 -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes

| model | size | params | backend | test | t/s |
| --- | --: | --: | --- | --: | --: |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | pp2048 | 528.52 ± 2.88 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | tg32 | 12.98 ± 0.05 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | pp2048 @ d4096 | 469.70 ± 5.47 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | tg32 @ d4096 | 11.62 ± 0.08 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | pp2048 @ d8192 | 420.87 ± 8.01 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | tg32 @ d8192 | 11.15 ± 0.08 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | pp2048 @ d16384 | 340.40 ± 8.40 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | tg32 @ d16384 | 9.90 ± 0.02 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | pp2048 @ d32768 | 226.70 ± 35.69 |
| qwen3vlmoe 235B.A22B Q4\_K - Medium | 124.91 GiB | 235.09 B | CUDA,RPC | tg32 @ d32768 | 8.03 ± 0.04 |

build: [`dd0f321`](https://github.com/ggml-org/llama.cpp/commit/dd0f3219419b24740864b5343958a97e1b3e4b26) (7121)

I also tried gpt-oss-120b on dual Sparks briefly - haven't tried llama-bench yet, but on test generation I've got 47 t/s on dual Sparks vs. 57 t/s on a single one.

I feel like the performance can be improved if RPC backend gets NCCL support, as TCP/IP stack adds a lot more latency - we are talking 1-2 microsecond latency as measured by `ib_send_lat`. |

1You must be logged in to vote

All reactions

19 replies


Show 14 previous replies

[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eugr](https://github.com/eugr) [on Nov 25, 2025Nov 25, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15080125)

|     |
| --- |
| [@rgerganov](https://github.com/rgerganov) \- suddenly realized that I was running VLLM over Ethernet all this time. Still over the 200G connection, but NCCL was not using Infiniband due to missing libraries in my container. After I fixed that, got improvement and also a good comparison between NCCL using ethernet and IB/RoCE over the same physical interface => reinforces the fact that there is a dramatic difference in latency.<br>The example below is a "fast" model - the one where network latency becomes a bottleneck.<br>TL;DR:<br>Using tensor parallel for the cluster:<br>- Cluster (200G Ethernet): 56 t/s<br>- Cluster (200G Infiniband/ROCE): 76 t/s<br>- Single node: 65 t/s<br>```<br>vllm serve RedHatAI/Qwen3-30B-A3B-NVFP4 --gpu-memory-utilization 0.5 --host 0.0.0.0 --port 8888 -tp 2 --distributed-executor-backend ray<br>```<br>**Using NCCL over Ethernet:**<br>```<br>                             Output tokens per second<br>  900 +---------------------------------------------------------------------+<br>      |                                                                     |<br>  800 |*                                                                    |<br>      |******                                                               |<br>  700 |*     ***                                                            |<br>      |      *  * **                                                        |<br>  600 |          *  ** **                                                   |<br>      |               *  * *                                                |<br>  500 |                  ** *                                               |<br>      |                     ****                                            |<br>      |                         ****                                        |<br>  400 |                             *****                                   |<br>      |                                  * ***                              |<br>  300 |                                   *   **                            |<br>      |                                         ******                      |<br>  200 |                                               **                    |<br>      |                                                 ******* ****        |<br>  100 |                                                        *    *       |<br>      |                                                              *      |<br>    0 +---------------------------------------------------------------------+<br>      0           10         20          30          40         50          60<br>                          Concurrent requests per second<br>  100 +---------------------------------------------------------------------+<br>      |*                                                                    |<br>      | *                                                                   |<br>      | *                                                                   |<br>   80 |  **                                                                 |<br>      |    *                                                                |<br>      |     **                                                              |<br>      |       ******                                                        |<br>   60 |             *                                                       |<br>      |              *****                                                  |<br>      |                   ***                                               |<br>   40 |                      ***                                            |<br>      |                         **                                          |<br>      |                           ******                                    |<br>      |                                 *******                             |<br>   20 |                                        **                           |<br>      |                                          ******                     |<br>      |                                                ******               |<br>      |                                                      ********       |<br>    0 +---------------------------------------------------------------------+<br>      0           10         20          30          40         50          60<br>============ Serving Benchmark Result ============<br>Successful requests:                     100<br>Failed requests:                         0<br>Benchmark duration (s):                  53.81<br>Total input tokens:                      23260<br>Total generated tokens:                  22061<br>Request throughput (req/s):              1.86<br>Output token throughput (tok/s):         409.97<br>Peak output token throughput (tok/s):    827.00<br>Peak concurrent requests:                100.00<br>Total Token throughput (tok/s):          842.23<br>---------------Time to First Token----------------<br>Mean TTFT (ms):                          408.75<br>Median TTFT (ms):                        411.69<br>P99 TTFT (ms):                           419.31<br>-----Time per Output Token (excl. 1st token)------<br>Mean TPOT (ms):                          95.97<br>Median TPOT (ms):                        95.01<br>P99 TPOT (ms):                           113.26<br>---------------Inter-token Latency----------------<br>Mean ITL (ms):                           85.29<br>Median ITL (ms):                         88.24<br>P99 ITL (ms):                            115.49<br>==================================================<br>```<br>```<br>============ Serving Benchmark Result ============<br>Successful requests:                     1<br>Failed requests:                         0<br>Benchmark duration (s):                  2.21<br>Total input tokens:                      12<br>Total generated tokens:                  119<br>Request throughput (req/s):              0.45<br>Output token throughput (tok/s):         53.88<br>Peak output token throughput (tok/s):    56.00<br>Peak concurrent requests:                1.00<br>Total Token throughput (tok/s):          59.32<br>---------------Time to First Token----------------<br>Mean TTFT (ms):                          71.60<br>Median TTFT (ms):                        71.60<br>P99 TTFT (ms):                           71.60<br>-----Time per Output Token (excl. 1st token)------<br>Mean TPOT (ms):                          18.11<br>Median TPOT (ms):                        18.11<br>P99 TPOT (ms):                           18.11<br>---------------Inter-token Latency----------------<br>Mean ITL (ms):                           18.11<br>Median ITL (ms):                         17.79<br>P99 ITL (ms):                            23.61<br>==================================================<br>```<br>**Using NCCL over Infiniband**<br>```<br>                             Output tokens per second<br>  1600 +--------------------------------------------------------------------+<br>       |                                                                    |<br>  1400 | *                                                                  |<br>       |* *                                                                 |<br>       |   *                                                                |<br>  1200 |    ******                                                          |<br>       |          **                                                        |<br>  1000 |            ****                                                    |<br>       |                ****                                                |<br>   800 |                    **                                              |<br>       |                      ****                                          |<br>       |                          ****                                      |<br>   600 |                              *******                               |<br>       |                                     **                             |<br>   400 |                                       ******                       |<br>       |                                             **                     |<br>       |                                               ******               |<br>   200 |                                                     ******         |<br>       |                                                           *        |<br>     0 +--------------------------------------------------------------------+<br>       0         5         10        15       20        25        30        35<br>                          Concurrent requests per second<br>  100 +---------------------------------------------------------------------+<br>      |*                                                                    |<br>      | *                                                                   |<br>      |  *                                                                  |<br>   80 |  *                                                                  |<br>      |   *                                                                 |<br>      |    **                                                               |<br>      |      ******                                                         |<br>   60 |            **                                                       |<br>      |              ****                                                   |<br>      |                  ****                                               |<br>   40 |                      **                                             |<br>      |                        **                                           |<br>      |                          ******                                     |<br>      |                                ********                             |<br>   20 |                                        **                           |<br>      |                                          ****                       |<br>      |                                              ******                 |<br>      |                                                    **********       |<br>    0 +---------------------------------------------------------------------+<br>      0         5         10        15        20        25        30        35<br>============ Serving Benchmark Result ============<br>Successful requests:                     100<br>Failed requests:                         0<br>Benchmark duration (s):                  31.21<br>Total input tokens:                      23260<br>Total generated tokens:                  22061<br>Request throughput (req/s):              3.20<br>Output token throughput (tok/s):         706.85<br>Peak output token throughput (tok/s):    1444.00<br>Peak concurrent requests:                100.00<br>Total Token throughput (tok/s):          1452.11<br>---------------Time to First Token----------------<br>Mean TTFT (ms):                          233.55<br>Median TTFT (ms):                        235.12<br>P99 TTFT (ms):                           240.96<br>-----Time per Output Token (excl. 1st token)------<br>Mean TPOT (ms):                          54.45<br>Median TPOT (ms):                        55.48<br>P99 TPOT (ms):                           61.20<br>---------------Inter-token Latency----------------<br>Mean ITL (ms):                           49.53<br>Median ITL (ms):                         52.57<br>P99 ITL (ms):                            61.96<br>==================================================<br>```<br>```<br>============ Serving Benchmark Result ============<br>Successful requests:                     1<br>Failed requests:                         0<br>Benchmark duration (s):                  1.55<br>Total input tokens:                      12<br>Total generated tokens:                  119<br>Request throughput (req/s):              0.64<br>Output token throughput (tok/s):         76.60<br>Peak output token throughput (tok/s):    75.00<br>Peak concurrent requests:                1.00<br>Total Token throughput (tok/s):          84.33<br>---------------Time to First Token----------------<br>Mean TTFT (ms):                          41.52<br>Median TTFT (ms):                        41.52<br>P99 TTFT (ms):                           41.52<br>-----Time per Output Token (excl. 1st token)------<br>Mean TPOT (ms):                          12.81<br>Median TPOT (ms):                        12.81<br>P99 TPOT (ms):                           12.81<br>---------------Inter-token Latency----------------<br>Mean ITL (ms):                           12.81<br>Median ITL (ms):                         12.72<br>P99 ITL (ms):                            14.26<br>==================================================<br>```<br>**Single**<br>```<br>vllm serve RedHatAI/Qwen3-30B-A3B-NVFP4 --load-format fastsafetensors --gpu-memory-utilization 0.5 --host 0.0.0.0 --port 8888<br>```<br>```<br>vllm bench serve   --backend vllm   --model RedHatAI/Qwen3-30B-A3B-NVFP4   --endpoint /v1/completions   --dataset-name sharegpt   --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json   --num-prompts 100   --port 8888<br>```<br>```<br>                             Output tokens per second<br>  1200 +--------------------------------------------------------------------+<br>       |                                                                    |<br>       |*                                                                   |<br>  1000 |**                                                                  |<br>       |* *                                                                 |<br>       |   ***                                                              |<br>   800 |      * **                                                          |<br>       |      **  ****                                                      |<br>       |              *                                                     |<br>   600 |              *****                                                 |<br>       |                   ****                                             |<br>       |                       ** **                                        |<br>       |                         *  **** **                                 |<br>   400 |                                *  ******                           |<br>       |                                         **                         |<br>       |                                           *******                  |<br>   200 |                                                  *****             |<br>       |                                                       ********     |<br>       |                                                               *    |<br>     0 +--------------------------------------------------------------------+<br>       0      5      10     15     20     25    30     35     40     45     50<br>                          Concurrent requests per second<br>  100 +---------------------------------------------------------------------+<br>      |*                                                                    |<br>      | *                                                                   |<br>      |  *                                                                  |<br>   80 |   *                                                                 |<br>      |   *                                                                 |<br>      |    ***                                                              |<br>      |       ******                                                        |<br>   60 |             *                                                       |<br>      |              ******                                                 |<br>      |                    **                                               |<br>   40 |                      ***                                            |<br>      |                         ***                                         |<br>      |                            ******                                   |<br>      |                                  ********                           |<br>   20 |                                          *                          |<br>      |                                           *******                   |<br>      |                                                  ******             |<br>      |                                                        **********   |<br>    0 +---------------------------------------------------------------------+<br>      0      5      10     15     20     25     30     35     40     45     50<br>============ Serving Benchmark Result ============<br>Successful requests:                     100<br>Failed requests:                         0<br>Benchmark duration (s):                  47.14<br>Total input tokens:                      23260<br>Total generated tokens:                  22061<br>Request throughput (req/s):              2.12<br>Output token throughput (tok/s):         468.03<br>Peak output token throughput (tok/s):    1051.00<br>Peak concurrent requests:                100.00<br>Total Token throughput (tok/s):          961.51<br>---------------Time to First Token----------------<br>Mean TTFT (ms):                          290.74<br>Median TTFT (ms):                        350.14<br>P99 TTFT (ms):                           353.63<br>-----Time per Output Token (excl. 1st token)------<br>Mean TPOT (ms):                          80.69<br>Median TPOT (ms):                        81.65<br>P99 TPOT (ms):                           99.00<br>---------------Inter-token Latency----------------<br>Mean ITL (ms):                           74.37<br>Median ITL (ms):                         79.14<br>P99 ITL (ms):                            88.78<br>==================================================<br>```<br>```<br>============ Serving Benchmark Result ============<br>Successful requests:                     1<br>Failed requests:                         0<br>Benchmark duration (s):                  1.81<br>Total input tokens:                      12<br>Total generated tokens:                  119<br>Request throughput (req/s):              0.55<br>Output token throughput (tok/s):         65.60<br>Peak output token throughput (tok/s):    64.00<br>Peak concurrent requests:                1.00<br>Total Token throughput (tok/s):          72.21<br>---------------Time to First Token----------------<br>Mean TTFT (ms):                          52.73<br>Median TTFT (ms):                        52.73<br>P99 TTFT (ms):                           52.73<br>-----Time per Output Token (excl. 1st token)------<br>Mean TPOT (ms):                          14.92<br>Median TPOT (ms):                        14.92<br>P99 TPOT (ms):                           14.92<br>---------------Inter-token Latency----------------<br>Mean ITL (ms):                           14.92<br>Median ITL (ms):                         14.92<br>P99 ITL (ms):                            15.96<br>==================================================<br>``` |

👍2

All reactions

- 👍2

[![@rgerganov](https://avatars.githubusercontent.com/u/271616?s=60&v=4)](https://github.com/rgerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [rgerganov](https://github.com/rgerganov) [on Nov 26, 2025Nov 26, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15083515)   Collaborator

|     |
| --- |
| [@eugr](https://github.com/eugr) thanks a lot for these benchmarks, using the infiniband transport is clearly a huge boost compared to ethernet. I will start thinking how to abstract the transport layer in the RPC backend, so we can support other transports like infiniband/RDMA in addition to plain tcp/ip |

👍2

All reactions

- 👍2

[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eugr](https://github.com/eugr) [on Dec 1, 2025Dec 1, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15127724)

|     |
| --- |
| [@rgerganov](https://github.com/rgerganov) \- one other observation: disabling CPU idle states (or at least deep idle states) improves llama.cpp RPC performance on Spark due to keeping CPU cores in awake state => avoiding wake up latency penalty.<br>That made me thinking - vllm/ray use busy loop to keep processes that are responsible for network communications awake vs. sleeping. I wonder if that will help here too? |

All reactions

[![@rgerganov](https://avatars.githubusercontent.com/u/271616?s=60&v=4)](https://github.com/rgerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [rgerganov](https://github.com/rgerganov) [on Dec 2, 2025Dec 2, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15132582)   Collaborator

|     |
| --- |
| Interesting. How do you disable CPU idle states and how much improvement do you observe?<br>The RPC backend is currently using blocking I/O and there is no way we can use busy loops unless we switch to async I/O. |

All reactions

[![@eugr](https://avatars.githubusercontent.com/u/2192184?s=60&v=4)](https://github.com/eugr)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eugr](https://github.com/eugr) [on Dec 2, 2025Dec 2, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15139580)

| ```
sudo cpupower idle-set -D 0
```

Although, it may be too aggressive, I may try -D 1.

As for the difference, here is ping.

With all idle states enabled:

```
eugr@spark:~/llm/llama.cpp$ ping 192.168.177.12
PING 192.168.177.12 (192.168.177.12) 56(84) bytes of data.
64 bytes from 192.168.177.12: icmp_seq=1 ttl=64 time=0.860 ms
64 bytes from 192.168.177.12: icmp_seq=2 ttl=64 time=1.12 ms
64 bytes from 192.168.177.12: icmp_seq=3 ttl=64 time=1.26 ms
64 bytes from 192.168.177.12: icmp_seq=4 ttl=64 time=1.16 ms
64 bytes from 192.168.177.12: icmp_seq=5 ttl=64 time=1.18 ms
64 bytes from 192.168.177.12: icmp_seq=6 ttl=64 time=1.16 ms
64 bytes from 192.168.177.12: icmp_seq=7 ttl=64 time=1.14 ms
64 bytes from 192.168.177.12: icmp_seq=8 ttl=64 time=0.828 ms
64 bytes from 192.168.177.12: icmp_seq=9 ttl=64 time=0.327 ms
64 bytes from 192.168.177.12: icmp_seq=10 ttl=64 time=1.02 ms
64 bytes from 192.168.177.12: icmp_seq=11 ttl=64 time=1.05 ms
^C
--- 192.168.177.12 ping statistics ---
11 packets transmitted, 11 received, 0% packet loss, time 10099ms
rtt min/avg/max/mdev = 0.327/1.010/1.264/0.250 ms
```

After disabling idle states:

```
eugr@spark:~/llm/llama.cpp$ ping 192.168.177.12
PING 192.168.177.12 (192.168.177.12) 56(84) bytes of data.
64 bytes from 192.168.177.12: icmp_seq=1 ttl=64 time=0.101 ms
64 bytes from 192.168.177.12: icmp_seq=2 ttl=64 time=0.032 ms
64 bytes from 192.168.177.12: icmp_seq=3 ttl=64 time=0.018 ms
64 bytes from 192.168.177.12: icmp_seq=4 ttl=64 time=0.022 ms
64 bytes from 192.168.177.12: icmp_seq=5 ttl=64 time=0.017 ms
64 bytes from 192.168.177.12: icmp_seq=6 ttl=64 time=0.029 ms
64 bytes from 192.168.177.12: icmp_seq=7 ttl=64 time=0.017 ms
64 bytes from 192.168.177.12: icmp_seq=8 ttl=64 time=0.015 ms
64 bytes from 192.168.177.12: icmp_seq=9 ttl=64 time=0.029 ms
64 bytes from 192.168.177.12: icmp_seq=10 ttl=64 time=0.025 ms
^C
--- 192.168.177.12 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9223ms
rtt min/avg/max/mdev = 0.015/0.030/0.101/0.024 ms
```

Performance difference with gpt-oss-120b:

```
build/bin/llama-bench -m ~/.cache/llama.cpp/ggml-org_gpt-oss-120b-GGUF_gpt-oss-120b-mxfp4-00001-of-00003.gguf --rpc 192.168.177.12:15001 -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

| model | size | params | backend | test | t/s |
| --- | --: | --: | --- | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 | 1740.62 ± 16.32 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 | 49.59 ± 2.13 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d4096 | 1595.65 ± 16.81 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d4096 | 46.61 ± 0.79 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d8192 | 1466.08 ± 6.10 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d8192 | 42.15 ± 0.64 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d16384 | 1234.22 ± 20.70 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d16384 | 38.82 ± 0.48 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d32768 | 946.42 ± 8.47 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d32768 | 31.72 ± 0.44 |

build: [`583cb83`](https://github.com/ggml-org/llama.cpp/commit/583cb83416467e8abf9b37349dcf1f6a0083745a) (7157)

**WITH DISABLED IDLE STATES**

| model | size | params | backend | test | t/s |
| --- | --: | --: | --- | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 | 1764.65 ± 5.72 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 | 55.49 ± 0.36 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d4096 | 1612.70 ± 14.41 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d4096 | 50.51 ± 0.41 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d8192 | 1480.67 ± 15.35 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d8192 | 45.99 ± 0.52 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d16384 | 1244.27 ± 14.47 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d16384 | 41.53 ± 0.25 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | pp2048 @ d32768 | 941.72 ± 13.00 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA,RPC | tg32 @ d32768 | 33.15 ± 0.20 |

build: [`583cb83`](https://github.com/ggml-org/llama.cpp/commit/583cb83416467e8abf9b37349dcf1f6a0083745a) (7157) |

👍3

All reactions

- 👍3

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/3705339?s=64&v=4)\ Djip007](https://github.com/Djip007) [on Dec 3, 2025Dec 3, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15147353)

|     |
| --- |
| network topology:<br>[https://www.servethehome.com/the-nvidia-gb10-connectx-7-200gbe-networking-is-really-different/](https://www.servethehome.com/the-nvidia-gb10-connectx-7-200gbe-networking-is-really-different/) |

1You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/39029310?s=64&v=4)\ d-shehu](https://github.com/d-shehu) [on Dec 5, 2025Dec 6, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15177752)

|     |
| --- |
| Any chance this can be extended to an environment with mixed GPUs (Nvidia, AMD and possibly Metal, CPU)?<br>NCCL and RCCL are not interoperable so would sending RPC messages across RoCE help? Thanks. |

1You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/166155368?s=64&v=4)\ fairydreaming](https://github.com/fairydreaming) [on Dec 9, 2025Dec 9, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15211907)   Collaborator

|     |
| --- |
| There is a reasonably priced [MikroTik CRS812 DDQ](https://mikrotik.com/product/crs812_ddq) switch that (in theory) may allow connecting up to 8 DGX Sparks. It has 2 x 400 GbE ports, 2 x 200 GbE and 8 x 50 GbE ports. I think two Sparks can be connected directly to 2 x 200 GbE ports, there are [QSFP-DD to 2xQSFP56 splitter cables](https://network.nvidia.com/pdf/prod_cables/PB_MCP7H60-W0xxRyy_400GbE_QSFP-DD_to_2x200GbE_QSFP56_DAC.pdf) (400GbE to 2 x 200GbE) to connect four more to 2 x 400 GbE ports and perhaps with cables like [this](https://www.fs.com/eu-en/products/88130.html) it would even be possible to connect two more Sparks via remaining 8 x 50 GbE ports. Not sure if this all would work out of the box, but it certainly looks promising. Has anyone tried it? |

1You must be logged in to vote

All reactions

1 reply


[![@openmarmot](https://avatars.githubusercontent.com/u/16908152?s=60&v=4)](https://github.com/openmarmot)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [openmarmot](https://github.com/openmarmot) [on Dec 17, 2025Dec 18, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15284645)

|     |
| --- |
| I had a guy message me on X who had got one for review and needed help setting it up. I think he got it working with a pair of DGX's eventually. the trick was there were some very specific settings to get the cable working.<br>Here was the specific detail that he had missed : "2x200G, 4x100G, 8x50G,  8x25G, 2x40G, 8x10G and 8x1G: Must be set with a forced speed mode and auto-negotiation disabled."<br>Probably not worth it as the performance of two of them doesn't seem that amazing but it would be a fun project if you don't mind spending the $$. I suspect that switch gets loud - although perhaps you could replace the fans with nocturnas |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/166155368?s=64&v=4)\ fairydreaming](https://github.com/fairydreaming) [on Dec 13, 2025Dec 13, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15247902)   Collaborator

|     |
| --- |
| [@ggerganov](https://github.com/ggerganov) link to dgx-spark.md benchmark results in the top post is broken (it's missing dgx-spark directory). |

1You must be logged in to vote

👍1

All reactions

- 👍1

1 reply


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Dec 14, 2025Dec 14, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15250246)   Maintainer  Author

|     |
| --- |
| Thanks |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/2192184?s=64&v=4)\ eugr](https://github.com/eugr) [on Dec 25, 2025Dec 25, 2025](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15339484)

| Wow, the latest Blackwell optimizations in llama.cpp made noticeable bump in prompt processing on DGX Spark:

| model | size | params | backend | test | t/s |
| --- | --: | --: | --- | --: | --: |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 | 2438.11 ± 13.72 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 | 57.81 ± 0.53 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d4096 | 2294.32 ± 12.61 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d4096 | 54.68 ± 0.52 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d8192 | 2149.21 ± 8.88 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d8192 | 51.75 ± 0.56 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d16384 | 1824.37 ± 8.93 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d16384 | 48.29 ± 0.21 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | pp2048 @ d32768 | 1415.53 ± 9.85 |
| gpt-oss 120B MXFP4 MoE | 59.02 GiB | 116.83 B | CUDA | tg32 @ d32768 | 41.42 ± 0.17 |

build: [`f5acfb2`](https://github.com/ggml-org/llama.cpp/commit/f5acfb2ffa1a0bc9d01a0a40f4d7c17421d7d570) (7535) |

6You must be logged in to vote

🚀3

All reactions

- 🚀3

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/16908152?s=64&v=4)\ openmarmot](https://github.com/openmarmot) [on Feb 7Feb 7, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15726693)

|     |
| --- |
| is anyone seeing slowdowns over time with llama-server and glm 4.7 flash on the spark?<br>I have a small sample prompt that I use to get a feel for token generation speed of a model.<br>I have consistently noticed that t/s with the prompt gets cut in half or more after several days of keeping the llama-server up serving glm 4.7 flash q8. restarting the llama-server process fixes this. It will go from about 40 t/s to 20 or lower over several days of uptime<br>I've only seen this with glm 4.7 flash so far. Happy to open an issue but I feel like I don't have enough info to be useful. It is repeatable however.<br>I'd use another model but glm 4.7 flash is really really good with opencode. It is the best agent programming model that I have used so far. |

1You must be logged in to vote

All reactions

2 replies


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [ggerganov](https://github.com/ggerganov) [on Feb 7Feb 7, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15726979)   Maintainer  Author

|     |
| --- |
| The issue is most likely that you are using the unified KV cache with multiple server slots (the default). This is not yet optimized for the CUDA backend and leads to a slowdown with time.<br>The simplest workaround is to disable the unified kv cache with:<br>```<br>llama-server ... -np 1<br>``` |

❤️1

All reactions

- ❤️1

[![@openmarmot](https://avatars.githubusercontent.com/u/16908152?s=60&v=4)](https://github.com/openmarmot)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [openmarmot](https://github.com/openmarmot) [on Feb 7Feb 7, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15727064)

|     |
| --- |
| perfect I will add that. Thank you very much! |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/85888?s=64&v=4)\ raphaelamorim](https://github.com/raphaelamorim) [on Feb 28Feb 28, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15957084)

|     |
| --- |
| [@ggerganov](https://github.com/ggerganov) would love to get your feedback. We're adding benchmarks to llama.cpp including the experimental NCCL support.<br>When NVIDIA started shipping DGX Spark in mid-October 2025, the pitch was basically: “desktop box, huge unified memory, run big models locally (even ~200B params for inference).”<br>The fun part is how quickly the software + community benchmarking story evolved from “here are some early numbers” to a real, reproducible leaderboard.<br>On Oct 14, 2025, ggerganov posted a DGX Spark performance thread in llama.cpp with a clear methodology: measure prefill (pp) and generation/decode (tg) across multiple context depths and batch sizes, using llama.cpp CUDA builds + llama-bench / llama-batched-bench.<br>Fast forward: the NVIDIA DGX Spark community basically acknowledged the recurring problem (“everyone posts partial flags, then nobody can reproduce it two weeks later”), we've agreed on our community tools for runtime image building, orchestration, recipe format and launched Spark Arena on Feb 11, 2026.<br>Top of the board right now (decode tokens/sec):<br>```<br>gpt-oss-120b (vLLM, MXFP4, 2 nodes): 75.96 tok/s<br>Qwen3-Coder-Next (SGLang, FP8, 2 nodes): 60.51 tok/s<br>gpt-oss-120b (vLLM, MXFP4, single node): 58.82 tok/s<br>NVIDIA-Nemotron-3-Nano-30B-A3B (vLLM, NVFP4, single node): 56.11 tok/s<br>```<br>[https://spark-arena.com/](https://spark-arena.com/) |

1You must be logged in to vote

👍2

All reactions

- 👍2

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/179122?s=64&v=4)\ gelim](https://github.com/gelim) [on Mar 1Mar 1, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-15961263)

|     |
| --- |
| Hello,<br>With the release of the latest Qwen 3.5 serie. I would be eager to know what are the perfs with **current** llama.cpp. And additionally if there are ongoing/coming PRs identified that will have a big impact in performance improvement (my hope is on work related to [#19504](https://github.com/ggml-org/llama.cpp/pull/19504) and future MTP support)<br>Qwen3.5 35B A3B Q8<br>Qwen3.5 122B A3B Q4<br>An "older" one Qwen3-Coder-Next Q8<br>Possible to leverage NVFP4 optimization available on the GB10?<br>For reference I see people benching with mostly vllm here: [https://spark-arena.com/leaderboard](https://spark-arena.com/leaderboard)<br>NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 seen at tg128@65535 70 tok/sec<br>gpt-oss-120b MXFP4 at tg128@65535 40 tok/sec (I see from [@eugr](https://github.com/eugr) message 2m ago that tg seems on par with vllm but llama.cpp is well behind in pp)<br>Qwen3.5-35B-A3B-FP8 at tg128@65535 38 tok/sec<br>Recent news shows the Qwen3.5 serie support very well aggressive quantization ( [https://x.com/i/status/2025951400119751040](https://x.com/i/status/2025951400119751040))<br>Meaning that this TQ1\_0 could even been considered to run on the GB10.<br>PS: qwen3-next recent perfs on Spark here<br>[#19375](https://github.com/ggml-org/llama.cpp/pull/19375) |

1You must be logged in to vote

All reactions

16 replies


Show 11 previous replies

[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=60&v=4)](https://github.com/ggerganov)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [ggerganov](https://github.com/ggerganov) [on Mar 12Mar 12, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16103751)   Maintainer  Author

|     |
| --- |
| [@gelim](https://github.com/gelim) Where do you get your vllm data from? On the site that you posted, I see this:<br> ![image](https://private-user-images.githubusercontent.com/1991296/562528631-d86acb40-bcbe-4747-9992-55508ba0fca5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii8xOTkxMjk2LzU2MjUyODYzMS1kODZhY2I0MC1iY2JlLTQ3NDctOTk5Mi01NTUwOGJhMGZjYTUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAyMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMjNUMDYwNzIzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MmE0ZTAxMTBjMTExOTk1MDJlNWFiYTM0OGE1NjQzNmFjNzYyNDI1ODg3MjhiNzQ4ZGFhZmVjOWVhYzc3NTQxYSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.6GDoqONJcmwE9-QMW-04tx1rc1LBsu52ORrUpNg3fk4) <br>Which is 2192.54 t/s at 32k context. |

👍1

All reactions

- 👍1

[![@mdengler](https://avatars.githubusercontent.com/u/777015?s=60&v=4)](https://github.com/mdengler)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [mdengler](https://github.com/mdengler) [on Mar 12Mar 12, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16104457)

|     |
| --- |
| > Can you try again? I think there should some improvements again after [#20340](https://github.com/ggml-org/llama.cpp/pull/20340)<br>This is with:<br>```<br>*  557fe2d91  vendor : update cpp-httplib to 0.37.1 (#20390) by Alessandro de Oliveira Faria (A.K.A.CABELO) (8 hours ago)   (HEAD -> master, origin/master)  Thu Mar 12 09:57:06 2026 -0300<br>```<br>...built on a DGX Spark:<br>```<br># build flags:<br>#               cmake -B build \<br>#               -DGGML_CUDA=ON \<br>#               -DLLAMA_OPENSSL=ON \<br>#               -DCMAKE_CUDA_ARCHITECTURES=121 \<br>```<br>Benchmark results are:<br>```<br>$ build/bin/llama-bench -fa 1 --mmap 0 -ngl 99 -ub 4096 -b 4096 -d 0,20000,48000 -p 4096 -m ~/.cache/llama.cpp/ggml-org_gpt-oss-120b-GGUF_gpt-oss-120b-mxfp4-00001-of-00003.gguf<br>Running as unit: run-r1d61f1b4f9fb4cb08841d128e96ee123.scope; invocation ID: e0c1e8679db24e9f96a1735303a58517<br>ggml_cuda_init: found 1 CUDA devices (Total VRAM: 122570 MiB):<br>  Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 122570 MiB (89490 MiB free)<br>| model                          |       size |     params | backend    | ngl | n_batch | n_ubatch | fa | mmap |            test |                  t/s |<br>| ------------------------------ | ---------: | ---------: | ---------- | --: | ------: | -------: | -: | ---: | --------------: | -------------------: |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |    4096 |     4096 |  1 |    0 |          pp4096 |       2046.65 ± 3.43 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |    4096 |     4096 |  1 |    0 |           tg128 |         45.34 ± 0.11 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |    4096 |     4096 |  1 |    0 | pp4096 @ d20000 |       1676.22 ± 2.55 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |    4096 |     4096 |  1 |    0 |  tg128 @ d20000 |         36.70 ± 0.13 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |    4096 |     4096 |  1 |    0 | pp4096 @ d48000 |       1225.06 ± 3.34 |<br>| gpt-oss 120B MXFP4 MoE         |  59.02 GiB |   116.83 B | CUDA       |  99 |    4096 |     4096 |  1 |    0 |  tg128 @ d48000 |         30.43 ± 0.02 |<br>build: 557fe2d91 (8322)<br>``` |

All reactions

[![@icsy7867](https://avatars.githubusercontent.com/u/3788162?s=60&v=4)](https://github.com/icsy7867)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [icsy7867](https://github.com/icsy7867) [on Mar 12Mar 12, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16105430)

|     |
| --- |
| > yay it's pretty good. Now getting closer to vllm pp speed, as for the decrease on tg speed I would say it's rather marginal.<br>> <br>> Framework pp2048@d32768 tg32@d32768<br>> <br>> vllm( [recipe](https://spark-arena.com/api/recipes/80fced6b-fec1-4657-aa5b-adaaab7d09bb/raw)) **2739.37** tok/s **43.38** tok/s<br>> <br>> llama.cpp(b8322) 2100 tok/s 42.83 tok/s<br>This is awesome to see!<br>Any chance you could try and nvfp4 on the GB10? :D |

All reactions

[![@openmarmot](https://avatars.githubusercontent.com/u/16908152?s=60&v=4)](https://github.com/openmarmot)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [openmarmot](https://github.com/openmarmot) [on Mar 12Mar 12, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16105600)

|     |
| --- |
| no nvfp4 on the gb10 yet. |

All reactions

[![@gelim](https://avatars.githubusercontent.com/u/179122?s=60&v=4)](https://github.com/gelim)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [gelim](https://github.com/gelim) [on Mar 13Mar 13, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16112864)

|     |
| --- |
| > [@gelim](https://github.com/gelim) Where do you get your vllm data from? On the site that you posted, I see this:<br>I took this one.<br> ![Screenshot 2026-03-13 at 09 33 14](https://private-user-images.githubusercontent.com/179122/562880099-4dd29636-758f-4785-b6cc-ae35808924af.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii8xNzkxMjIvNTYyODgwMDk5LTRkZDI5NjM2LTc1OGYtNDc4NS1iNmNjLWFlMzU4MDg5MjRhZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDIzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAyM1QwNjA3MjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02YjQ4OTUwM2JlOWU0MzA4MmYyNjM2ZTQ5MTE4YmYzMDNhOTljMmQyMzA5MzY2Y2RiMzdlYTFkOGVkNjY5YjNkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ._Ut6aNNeVIErZ5h8wC8BCEJU-NxLErj7gVICHYMyCQA) <br>There are others available with better tg speed (46-47 tok/sec) and worst pp speed (~2k ish). Their difference is:<br>- KV cache dtype set to fp8<br>- Use flashinfer as attention backend<br>E.g: diff between [https://spark-arena.com/api/recipes/c091e5aa-6f0d-453e-aaa7-8c63b30f9df5/raw](https://spark-arena.com/api/recipes/c091e5aa-6f0d-453e-aaa7-8c63b30f9df5/raw) and [https://spark-arena.com/api/recipes/80fced6b-fec1-4657-aa5b-adaaab7d09bb/raw](https://spark-arena.com/api/recipes/80fced6b-fec1-4657-aa5b-adaaab7d09bb/raw) |

👍1

All reactions

- 👍1

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/60984362?s=64&v=4)\ ruicatxiao](https://github.com/ruicatxiao) [on Mar 11Mar 11, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16084289)

|     |
| --- |
| For latest llama.cpp build on DGX Spark, can people share their build flags? Curious whether we need to specify 120 or 121 for -DCMAKE\_CUDA\_ARCHITECTURES |

1You must be logged in to vote

All reactions

1 reply


[![@openmarmot](https://avatars.githubusercontent.com/u/16908152?s=60&v=4)](https://github.com/openmarmot)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [openmarmot](https://github.com/openmarmot) [on Mar 11Mar 11, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16086546)

|     |
| --- |
| I am not doing anything fancy. here is my rebuild script : [https://github.com/openmarmot/tech-notes/blob/main/nvidia/DGX\_Spark/llamacpp/rebuild\_llama\_cpp.sh](https://github.com/openmarmot/tech-notes/blob/main/nvidia/DGX_Spark/llamacpp/rebuild_llama_cpp.sh) |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/60984362?s=64&v=4)\ ruicatxiao](https://github.com/ruicatxiao) [on Mar 13Mar 13, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16122162)

|     |
| --- |
| I am seeing faster pp and tg speed with latest builds, even versus just 3 days ago!<br>Prior:<br>\| bartowski-qwen35moe 122B.A10B Q5\_K - Small \| 78.97 GiB \| 122.11 B \| CUDA \| 999 \| 16 \| q8\_0 \| q8\_0 \| 1 \| pp512 \| 467.42 ± 19.62 \|<br>\| bartowski-qwen35moe 122B.A10B Q5\_K - Small \| 78.97 GiB \| 122.11 B \| CUDA \| 999 \| 16 \| q8\_0 \| q8\_0 \| 1 \| tg128 \| 18.50 ± 0.12 \|<br>Current:<br>\| bartowski-qwen35moe 122B.A10B Q5\_K - Small \| 78.97 GiB \| 122.11 B \| CUDA \| 999 \| 16 \| q8\_0 \| q8\_0 \| 1 \| pp512 \| 707.20 ± 2.30 \|<br>\| bartowski-qwen35moe 122B.A10B Q5\_K - Small \| 78.97 GiB \| 122.11 B \| CUDA \| 999 \| 16 \| q8\_0 \| q8\_0 \| 1 \| tg128 \| 23.03 ± 0.10 \| |

1You must be logged in to vote

All reactions

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/179122?s=64&v=4)\ gelim](https://github.com/gelim) [on Mar 14Mar 14, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16133852)

|     |
| --- |
| Speaking about Spark performance, I stumbled on that: [https://www.reddit.com/r/LocalLLaMA/s/Z0RzA1NAPJ](https://www.reddit.com/r/LocalLLaMA/s/Z0RzA1NAPJ)<br>This is claiming big perf boost by allowing K=64 tiles size hence fitting inside the 99KB SMEM for consumer grade Blackwell (like the Spark's GB10).<br>This seems huge whenever full NVFP4 support will land. |

3You must be logged in to vote

All reactions

5 replies


[![@eous](https://avatars.githubusercontent.com/u/13773563?s=60&v=4)](https://github.com/eous)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [eous](https://github.com/eous) [on Mar 15Mar 15, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16144882)

|     |
| --- |
| ![gpu_arch_lineage](https://private-user-images.githubusercontent.com/13773563/563771616-bc92f4b4-1b55-4c1a-9584-1ecd04f39155.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii8xMzc3MzU2My81NjM3NzE2MTYtYmM5MmY0YjQtMWI1NS00YzFhLTk1ODQtMWVjZDA0ZjM5MTU1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDIzVDA2MDcyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThmMDYyNGI4MjQ4M2NmMGNhMTJhNzNlYmZiNzk3ZDcxNzk2NmU4NGY5NzhhM2QwMzVlYjcyZWVjNDQ1YjgzMjAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.oDd11exA5SEIXoatcKyT8DP-8NQrU0vOzMvRBrKBIzg) |

All reactions

[![@gelim](https://avatars.githubusercontent.com/u/179122?s=60&v=4)](https://github.com/gelim)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

#### [gelim](https://github.com/gelim) [on Mar 16Mar 16, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16160222)

|     |
| --- |
| by looking a bit more at the PTX instruction in `ggml/src/ggml-cuda/mma.cuh:mma_block_scaled()`:<br>```<br>        asm volatile(<br>            "mma.sync.aligned.kind::mxf4.block_scale.scale_vec::2X.m16n8k64.row.col.f32.e2m1.e2m1.f32.ue8m0 "<br>            "{%0, %1, %2, %3}, {%4, %5, %6, %7}, {%8, %9}, {%0, %1, %2, %3}, "<br>            "%10, {0, 0}, %11, {0, 0};"<br>            : "+f"(Dxi[0]), "+f"(Dxi[1]), "+f"(Dxi[2]), "+f"(Dxi[3])<br>            : "r"(Axi[0]), "r"(Axi[1]), "r"(Axi[2]), "r"(Axi[3]), "r"(Bxi[0]), "r"(Bxi[1]), "r"(a_scale), "r"(b_scale));<br>[...]<br>```<br>would confirm that K=64 is properly used in code path related to MMA for Blackwell architecture. |

All reactions

[![@am17an](https://avatars.githubusercontent.com/u/2929750?s=60&v=4)](https://github.com/am17an)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [am17an](https://github.com/am17an) [on Mar 16Mar 16, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16160513)   Collaborator

|     |
| --- |
| I'm skeptical of the post you mentioned. In general, relying on reddit posts is not recommended |

All reactions

[![@gelim](https://avatars.githubusercontent.com/u/179122?s=60&v=4)](https://github.com/gelim)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [gelim](https://github.com/gelim) [on Mar 16Mar 16, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16160693)

|     |
| --- |
| in second sight it seems out of topic for llama.cpp. As I'm not really knowledgeable on the codebase at first I had the impression it could be beneficial. Glad to hear if my second comment by digging in the code is as well out of topic. |

All reactions

[![@am17an](https://avatars.githubusercontent.com/u/2929750?s=60&v=4)](https://github.com/am17an)

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

#### [am17an](https://github.com/am17an) [on Mar 16Mar 16, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16160755)   Collaborator

|     |
| --- |
| That is correct spot for mxfp4 multiplication, nvfp4 would also similar. I would be extremely surprised if cutlass/flash-infer didn't use this. |

All reactions

Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

edited

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{editor}}'s edit

{{actor}} deleted this content
.

# {{editor}}'s edit

### [![](https://avatars.githubusercontent.com/u/3746963?s=64&v=4)\ cody-vibe](https://github.com/cody-vibe) [on Mar 30Mar 30, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16377832)

| Compile log

```
CFLAGS="-O3 -mcpu=native -mtune=native -fomit-frame-pointer -pipe"   \
CXXFLAGS="-O3 -mcpu=native -mtune=native -fomit-frame-pointer -pipe" \
cmake -S . -B build               \
  -DGGML_CUDA=ON                  \
  -DGGML_CUDA_F16=ON              \
  -DGGML_CUDA_FORCE_MMQ=ON        \
  -DGGML_NATIVE=ON                \
  -DGGML_LTO=ON                   \
  -DGGML_OPENMP=ON                \
  -DCMAKE_BUILD_TYPE=Release      \
  -DCMAKE_CUDA_ARCHITECTURES=121a
```

```
-- The C compiler identification is GNU 13.3.0
-- The CXX compiler identification is GNU 13.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMAKE_BUILD_TYPE=Release
-- Found Git: /usr/bin/git (found version "2.43.0")
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Warning: ccache not found - consider installing it for faster compilation or disable this warning with GGML_CCACHE=OFF
-- CMAKE_SYSTEM_PROCESSOR: aarch64
-- GGML_SYSTEM_ARCH: ARM
-- Including CPU backend
-- Found OpenMP_C: -fopenmp (found version "4.5")
-- Found OpenMP_CXX: -fopenmp (found version "4.5")
-- Found OpenMP: TRUE (found version "4.5")
-- ARM detected
-- Performing Test GGML_COMPILER_SUPPORTS_FP16_FORMAT_I3E
-- Performing Test GGML_COMPILER_SUPPORTS_FP16_FORMAT_I3E - Failed
CMake Warning at ggml/src/ggml-cpu/CMakeLists.txt:146 (message):
ARM -march/-mcpu not found, -mcpu=native will be used
Call Stack (most recent call first):
ggml/src/CMakeLists.txt:445 (ggml_add_cpu_backend_variant_impl)

-- Performing Test GGML_MACHINE_SUPPORTS_dotprod
-- Performing Test GGML_MACHINE_SUPPORTS_dotprod - Failed
-- Performing Test GGML_MACHINE_SUPPORTS_nodotprod
-- Performing Test GGML_MACHINE_SUPPORTS_nodotprod - Failed
-- Performing Test GGML_MACHINE_SUPPORTS_i8mm
-- Performing Test GGML_MACHINE_SUPPORTS_i8mm - Failed
-- Performing Test GGML_MACHINE_SUPPORTS_noi8mm
-- Performing Test GGML_MACHINE_SUPPORTS_noi8mm - Failed
-- Performing Test GGML_MACHINE_SUPPORTS_sve
-- Performing Test GGML_MACHINE_SUPPORTS_sve - Failed
-- Performing Test GGML_MACHINE_SUPPORTS_nosve
-- Performing Test GGML_MACHINE_SUPPORTS_nosve - Failed
-- Performing Test GGML_MACHINE_SUPPORTS_sme
-- Performing Test GGML_MACHINE_SUPPORTS_sme - Failed
-- Performing Test GGML_MACHINE_SUPPORTS_nosme
-- Performing Test GGML_MACHINE_SUPPORTS_nosme - Failed
-- Checking for ARM features using flags:
--   -mcpu=native
-- Performing Test HAVE_DOTPROD
-- Performing Test HAVE_DOTPROD - Failed
-- Performing Test HAVE_SVE
-- Performing Test HAVE_SVE - Failed
-- Performing Test HAVE_MATMUL_INT8
-- Performing Test HAVE_MATMUL_INT8 - Failed
-- Performing Test HAVE_FMA
-- Performing Test HAVE_FMA - Success
-- Performing Test HAVE_FP16_VECTOR_ARITHMETIC
-- Performing Test HAVE_FP16_VECTOR_ARITHMETIC - Failed
-- Performing Test HAVE_SME
-- Performing Test HAVE_SME - Failed
-- Adding CPU backend variant ggml-cpu: -mcpu=native
-- Found CUDAToolkit: /usr/local/cuda/targets/sbsa-linux/include (found version "13.0.88")
-- CUDA Toolkit found
-- The CUDA compiler identification is NVIDIA 13.0.88
-- Detecting CUDA compiler ABI info
-- Detecting CUDA compiler ABI info - done
-- Check for working CUDA compiler: /usr/local/cuda/bin/nvcc - skipped
-- Detecting CUDA compile features
-- Detecting CUDA compile features - done
-- Replacing 121-real in CMAKE_CUDA_ARCHITECTURES_NATIVE with 121a-real
-- Using CMAKE_CUDA_ARCHITECTURES=121a CMAKE_CUDA_ARCHITECTURES_NATIVE=121a-real
-- CUDA host compiler is GNU 13.3.0
-- Including CUDA backend
-- ggml version: 0.9.8
-- ggml commit:  7c203670f
-- Found OpenSSL: /usr/lib/aarch64-linux-gnu/libcrypto.so (found version "3.0.13")
-- Performing Test OPENSSL_VERSION_SUPPORTED
-- Performing Test OPENSSL_VERSION_SUPPORTED - Success
-- OpenSSL found: 3.0.13
-- Generating embedded license file for target: common
-- Configuring done (3.7s)
-- Generating done (0.1s)
-- Build files have been written to: /home/sparky/Workspace/ai-spark/src/llama-cpp/build
[  1%] Building C object ggml/src/CMakeFiles/ggml-base.dir/ggml.c.o
[  1%] Building CXX object vendor/cpp-httplib/CMakeFiles/cpp-httplib.dir/httplib.cpp.o
[  1%] Building CXX object ggml/src/CMakeFiles/ggml-base.dir/ggml.cpp.o
[  1%] Building C object examples/gguf-hash/CMakeFiles/sha256.dir/deps/sha256/sha256.c.o
[  1%] Building C object ggml/src/CMakeFiles/ggml-base.dir/ggml-alloc.c.o
[  1%] Building CXX object ggml/src/CMakeFiles/ggml-base.dir/ggml-opt.cpp.o
[  2%] Building C object ggml/src/CMakeFiles/ggml-base.dir/ggml-quants.c.o
[  3%] Building C object examples/gguf-hash/CMakeFiles/xxhash.dir/deps/xxhash/xxhash.c.o
[  3%] Building CXX object ggml/src/CMakeFiles/ggml-base.dir/ggml-backend.cpp.o
[  3%] Building CXX object ggml/src/CMakeFiles/ggml-base.dir/ggml-threading.cpp.o
[  3%] Building CXX object ggml/src/CMakeFiles/ggml-base.dir/gguf.cpp.o
[  3%] Building CXX object tools/mtmd/CMakeFiles/llama-gemma3-cli.dir/deprecation-warning.cpp.o
[  4%] Building CXX object tools/mtmd/CMakeFiles/llama-minicpmv-cli.dir/deprecation-warning.cpp.o
[  4%] Building CXX object common/CMakeFiles/build_info.dir/build-info.cpp.o
[  4%] Building C object examples/gguf-hash/CMakeFiles/sha1.dir/deps/sha1/sha1.c.o
[  4%] Building CXX object tools/mtmd/CMakeFiles/llama-qwen2vl-cli.dir/deprecation-warning.cpp.o
[  5%] Building CXX object tools/mtmd/CMakeFiles/llama-llava-cli.dir/deprecation-warning.cpp.o
[  5%] Built target build_info
[  5%] Built target sha1
[  5%] Linking CXX executable ../../bin/llama-gemma3-cli
[  6%] Linking CXX executable ../../bin/llama-qwen2vl-cli
[  6%] Linking CXX executable ../../bin/llama-llava-cli
[  6%] Built target sha256
[  6%] Linking CXX executable ../../bin/llama-minicpmv-cli
[  6%] Built target llama-gemma3-cli
[  6%] Built target llama-qwen2vl-cli
[  6%] Built target llama-llava-cli
[  6%] Built target llama-minicpmv-cli
[  6%] Linking CXX shared library ../../bin/libggml-base.so
[  6%] Built target xxhash
[  6%] Built target ggml-base
[  6%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/acc.cu.o
[  6%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/arange.cu.o
[  6%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/argmax.cu.o
[  6%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/ggml-cpu.cpp.o
[  6%] Building C object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/quants.c.o
[  6%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/binbcast.cu.o
[  6%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/traits.cpp.o
[  6%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/amx/amx.cpp.o
[  6%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/add-id.cu.o
[  6%] Building C object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/ggml-cpu.c.o
[  6%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/repack.cpp.o
[  7%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/argsort.cu.o
[  7%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/clamp.cu.o
[  7%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/concat.cu.o
[  7%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/conv-transpose-1d.cu.o
[  8%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/hbm.cpp.o
[  9%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/conv2d-dw.cu.o
[  9%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/conv2d-transpose.cu.o
[  9%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/amx/mmq.cpp.o
[ 10%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/binary-ops.cpp.o
[ 10%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/unary-ops.cpp.o
[ 10%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/vec.cpp.o
[ 10%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/ops.cpp.o
[ 10%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/llamafile/sgemm.cpp.o
[ 10%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/conv2d.cu.o
[ 10%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/convert.cu.o
[ 10%] Building C object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/arch/arm/quants.c.o
[ 11%] Building CXX object ggml/src/CMakeFiles/ggml-cpu.dir/ggml-cpu/arch/arm/repack.cpp.o
[ 11%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/count-equal.cu.o
[ 11%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/cpy.cu.o
[ 11%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/cross-entropy-loss.cu.o
[ 12%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/cumsum.cu.o
[ 12%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/diag.cu.o
[ 12%] Linking CXX shared library ../../bin/libggml-cpu.so
[ 12%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/diagmask.cu.o
[ 12%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/fattn-wmma-f16.cu.o
[ 12%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/fattn-tile.cu.o
[ 12%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/fattn.cu.o
[ 13%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/fill.cu.o
[ 13%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/gated_delta_net.cu.o
[ 13%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/getrows.cu.o
[ 13%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/ggml-cuda.cu.o
[ 13%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/gla.cu.o
[ 13%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/im2col.cu.o
[ 14%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/mean.cu.o
[ 14%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/mmf.cu.o
[ 14%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/mmid.cu.o
[ 14%] Built target ggml-cpu
[ 14%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/mmq.cu.o
[ 14%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/mmvf.cu.o
[ 14%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/mmvq.cu.o
[ 15%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/norm.cu.o
[ 15%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/opt-step-adamw.cu.o
[ 15%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/opt-step-sgd.cu.o
[ 15%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/out-prod.cu.o
[ 15%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/pad.cu.o
[ 15%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/pad_reflect_1d.cu.o
[ 16%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/pool2d.cu.o
[ 16%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/quantize.cu.o
[ 16%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/roll.cu.o
[ 16%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/rope.cu.o
[ 16%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/scale.cu.o
[ 16%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/set-rows.cu.o
[ 17%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/set.cu.o
[ 17%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/softcap.cu.o
[ 17%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/softmax.cu.o
[ 17%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/solve_tri.cu.o
[ 17%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/ssm-conv.cu.o
[ 18%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/ssm-scan.cu.o
[ 18%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/sum.cu.o
[ 18%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/sumrows.cu.o
[ 18%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/top-k.cu.o
[ 18%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/topk-moe.cu.o
[ 19%] Linking CXX static library libcpp-httplib.a
[ 19%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/tri.cu.o
[ 19%] Built target cpp-httplib
[ 20%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/tsembd.cu.o
[ 20%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/unary.cu.o
[ 20%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/upscale.cu.o
[ 20%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/wkv.cu.o
[ 20%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq112-dv112.cu.o
[ 20%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq128-dv128.cu.o
[ 21%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq256-dv256.cu.o
[ 21%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq40-dv40.cu.o
[ 21%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq576-dv512.cu.o
[ 21%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq64-dv64.cu.o
[ 21%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq72-dv72.cu.o
[ 21%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq80-dv80.cu.o
[ 22%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-tile-instance-dkq96-dv96.cu.o
[ 22%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_1-ncols2_16.cu.o
[ 22%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_1-ncols2_32.cu.o
[ 22%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_1-ncols2_8.cu.o
[ 22%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_16-ncols2_1.cu.o
[ 22%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_16-ncols2_2.cu.o
[ 23%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_16-ncols2_4.cu.o
[ 23%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_2-ncols2_16.cu.o
[ 23%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_2-ncols2_32.cu.o
[ 23%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_2-ncols2_4.cu.o
[ 23%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_2-ncols2_8.cu.o
[ 23%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_32-ncols2_1.cu.o
[ 24%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_32-ncols2_2.cu.o
[ 24%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_4-ncols2_16.cu.o
[ 24%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_4-ncols2_2.cu.o
[ 24%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_4-ncols2_4.cu.o
[ 24%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_4-ncols2_8.cu.o
[ 24%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_64-ncols2_1.cu.o
[ 25%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_8-ncols2_1.cu.o
[ 25%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_8-ncols2_2.cu.o
[ 25%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_8-ncols2_4.cu.o
[ 25%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-mma-f16-instance-ncols1_8-ncols2_8.cu.o
[ 25%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq1_s.cu.o
[ 25%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq2_s.cu.o
[ 26%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq2_xs.cu.o
[ 26%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq2_xxs.cu.o
[ 26%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq3_s.cu.o
[ 26%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq3_xxs.cu.o
[ 26%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq4_nl.cu.o
[ 26%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-iq4_xs.cu.o
[ 27%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-mxfp4.cu.o
[ 27%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q2_k.cu.o
[ 27%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q3_k.cu.o
[ 27%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q4_0.cu.o
[ 27%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q4_1.cu.o
[ 27%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q4_k.cu.o
[ 28%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q5_0.cu.o
[ 28%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q5_1.cu.o
[ 28%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q5_k.cu.o
[ 28%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q6_k.cu.o
[ 28%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmq-instance-q8_0.cu.o
[ 29%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_1.cu.o
[ 29%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_10.cu.o
[ 29%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_11.cu.o
[ 29%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_12.cu.o
[ 29%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_13.cu.o
[ 29%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_14.cu.o
[ 30%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_15.cu.o
[ 30%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_16.cu.o
[ 30%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_2.cu.o
[ 30%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_3.cu.o
[ 30%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_4.cu.o
[ 30%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_5.cu.o
[ 31%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_6.cu.o
[ 31%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_7.cu.o
[ 31%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_8.cu.o
[ 31%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/mmf-instance-ncols_9.cu.o
[ 31%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-vec-instance-f16-f16.cu.o
[ 31%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-vec-instance-q4_0-q4_0.cu.o
[ 32%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-vec-instance-bf16-bf16.cu.o
[ 32%] Building CUDA object ggml/src/ggml-cuda/CMakeFiles/ggml-cuda.dir/template-instances/fattn-vec-instance-q8_0-q8_0.cu.o
[ 32%] Linking CUDA shared library ../../../bin/libggml-cuda.so
[ 32%] Built target ggml-cuda
[ 32%] Building CXX object ggml/src/CMakeFiles/ggml.dir/ggml-backend-dl.cpp.o
[ 32%] Building CXX object ggml/src/CMakeFiles/ggml.dir/ggml-backend-reg.cpp.o
[ 32%] Linking CXX shared library ../../bin/libggml.so
[ 32%] Built target ggml
[ 32%] Building CXX object examples/gguf-hash/CMakeFiles/llama-gguf-hash.dir/gguf-hash.cpp.o
[ 32%] Building CXX object examples/gguf/CMakeFiles/llama-gguf.dir/gguf.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-adapter.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-cparams.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-graph.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-hparams.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-kv-cache.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-io.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-batch.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-memory.cpp.o
[ 33%] Building CXX object src/CMakeFiles/llama.dir/llama-arch.cpp.o
[ 34%] Building CXX object src/CMakeFiles/llama.dir/llama-kv-cache-iswa.cpp.o
[ 34%] Building CXX object src/CMakeFiles/llama.dir/llama-context.cpp.o
[ 34%] Building CXX object src/CMakeFiles/llama.dir/llama-chat.cpp.o
[ 35%] Building CXX object src/CMakeFiles/llama.dir/llama-grammar.cpp.o
[ 35%] Building CXX object src/CMakeFiles/llama.dir/llama-impl.cpp.o
[ 35%] Building CXX object src/CMakeFiles/llama.dir/llama-memory-hybrid.cpp.o
[ 35%] Building CXX object src/CMakeFiles/llama.dir/llama-memory-recurrent.cpp.o
[ 35%] Building CXX object src/CMakeFiles/llama.dir/llama-memory-hybrid-iswa.cpp.o
[ 35%] Building CXX object src/CMakeFiles/llama.dir/llama-mmap.cpp.o
[ 36%] Building CXX object src/CMakeFiles/llama.dir/llama-model-loader.cpp.o
[ 36%] Building CXX object src/CMakeFiles/llama.dir/llama-model-saver.cpp.o
[ 36%] Building CXX object src/CMakeFiles/llama.dir/llama-model.cpp.o
[ 36%] Linking CXX executable ../../bin/llama-gguf
[ 36%] Building CXX object src/CMakeFiles/llama.dir/llama-quant.cpp.o
[ 36%] Linking CXX executable ../../bin/llama-gguf-hash
[ 36%] Built target llama-gguf
[ 36%] Building CXX object src/CMakeFiles/llama.dir/llama-sampler.cpp.o
[ 36%] Built target llama-gguf-hash
[ 36%] Building CXX object src/CMakeFiles/llama.dir/llama-vocab.cpp.o
[ 37%] Building CXX object src/CMakeFiles/llama.dir/unicode-data.cpp.o
[ 37%] Building CXX object src/CMakeFiles/llama.dir/unicode.cpp.o
[ 37%] Building CXX object src/CMakeFiles/llama.dir/models/afmoe.cpp.o
[ 37%] Building CXX object src/CMakeFiles/llama.dir/models/apertus.cpp.o
[ 37%] Building CXX object src/CMakeFiles/llama.dir/models/arcee.cpp.o
[ 37%] Building CXX object src/CMakeFiles/llama.dir/models/arctic.cpp.o
[ 38%] Building CXX object src/CMakeFiles/llama.dir/models/arwkv7.cpp.o
[ 38%] Building CXX object src/CMakeFiles/llama.dir/models/baichuan.cpp.o
[ 38%] Building CXX object src/CMakeFiles/llama.dir/models/bailingmoe.cpp.o
[ 38%] Building CXX object src/CMakeFiles/llama.dir/models/bailingmoe2.cpp.o
[ 38%] Building CXX object src/CMakeFiles/llama.dir/models/bert.cpp.o
[ 39%] Building CXX object src/CMakeFiles/llama.dir/models/bitnet.cpp.o
[ 39%] Building CXX object src/CMakeFiles/llama.dir/models/bloom.cpp.o
[ 39%] Building CXX object src/CMakeFiles/llama.dir/models/chameleon.cpp.o
[ 39%] Building CXX object src/CMakeFiles/llama.dir/models/chatglm.cpp.o
[ 39%] Building CXX object src/CMakeFiles/llama.dir/models/codeshell.cpp.o
[ 39%] Building CXX object src/CMakeFiles/llama.dir/models/cogvlm.cpp.o
[ 40%] Building CXX object src/CMakeFiles/llama.dir/models/cohere2-iswa.cpp.o
[ 40%] Building CXX object src/CMakeFiles/llama.dir/models/command-r.cpp.o
[ 40%] Building CXX object src/CMakeFiles/llama.dir/models/dbrx.cpp.o
[ 40%] Building CXX object src/CMakeFiles/llama.dir/models/deci.cpp.o
[ 40%] Building CXX object src/CMakeFiles/llama.dir/models/deepseek.cpp.o
[ 40%] Building CXX object src/CMakeFiles/llama.dir/models/deepseek2.cpp.o
[ 41%] Building CXX object src/CMakeFiles/llama.dir/models/delta-net-base.cpp.o
[ 41%] Building CXX object src/CMakeFiles/llama.dir/models/dots1.cpp.o
[ 41%] Building CXX object src/CMakeFiles/llama.dir/models/dream.cpp.o
[ 41%] Building CXX object src/CMakeFiles/llama.dir/models/ernie4-5-moe.cpp.o
[ 41%] Building CXX object src/CMakeFiles/llama.dir/models/ernie4-5.cpp.o
[ 41%] Building CXX object src/CMakeFiles/llama.dir/models/eurobert.cpp.o
[ 42%] Building CXX object src/CMakeFiles/llama.dir/models/exaone-moe.cpp.o
[ 42%] Building CXX object src/CMakeFiles/llama.dir/models/exaone.cpp.o
[ 42%] Building CXX object src/CMakeFiles/llama.dir/models/exaone4.cpp.o
[ 42%] Building CXX object src/CMakeFiles/llama.dir/models/falcon-h1.cpp.o
[ 42%] Building CXX object src/CMakeFiles/llama.dir/models/falcon.cpp.o
[ 42%] Building CXX object src/CMakeFiles/llama.dir/models/gemma-embedding.cpp.o
[ 43%] Building CXX object src/CMakeFiles/llama.dir/models/gemma.cpp.o
[ 43%] Building CXX object src/CMakeFiles/llama.dir/models/gemma2-iswa.cpp.o
[ 43%] Building CXX object src/CMakeFiles/llama.dir/models/gemma3.cpp.o
[ 43%] Building CXX object src/CMakeFiles/llama.dir/models/gemma3n-iswa.cpp.o
[ 43%] Building CXX object src/CMakeFiles/llama.dir/models/glm4-moe.cpp.o
[ 43%] Building CXX object src/CMakeFiles/llama.dir/models/glm4.cpp.o
[ 44%] Building CXX object src/CMakeFiles/llama.dir/models/gpt2.cpp.o
[ 44%] Building CXX object src/CMakeFiles/llama.dir/models/gptneox.cpp.o
[ 44%] Building CXX object src/CMakeFiles/llama.dir/models/granite-hybrid.cpp.o
[ 44%] Building CXX object src/CMakeFiles/llama.dir/models/granite.cpp.o
[ 44%] Building CXX object src/CMakeFiles/llama.dir/models/grok.cpp.o
[ 44%] Building CXX object src/CMakeFiles/llama.dir/models/grovemoe.cpp.o
[ 45%] Building CXX object src/CMakeFiles/llama.dir/models/hunyuan-dense.cpp.o
[ 45%] Building CXX object src/CMakeFiles/llama.dir/models/hunyuan-moe.cpp.o
[ 45%] Building CXX object src/CMakeFiles/llama.dir/models/internlm2.cpp.o
[ 45%] Building CXX object src/CMakeFiles/llama.dir/models/jais.cpp.o
[ 45%] Building CXX object src/CMakeFiles/llama.dir/models/jais2.cpp.o
[ 45%] Building CXX object src/CMakeFiles/llama.dir/models/jamba.cpp.o
[ 46%] Building CXX object src/CMakeFiles/llama.dir/models/kimi-linear.cpp.o
[ 46%] Building CXX object src/CMakeFiles/llama.dir/models/lfm2.cpp.o
[ 46%] Building CXX object src/CMakeFiles/llama.dir/models/llada-moe.cpp.o
[ 46%] Building CXX object src/CMakeFiles/llama.dir/models/llada.cpp.o
[ 46%] Building CXX object src/CMakeFiles/llama.dir/models/llama-iswa.cpp.o
[ 46%] Building CXX object src/CMakeFiles/llama.dir/models/llama.cpp.o
[ 47%] Building CXX object src/CMakeFiles/llama.dir/models/maincoder.cpp.o
[ 47%] Building CXX object src/CMakeFiles/llama.dir/models/mamba-base.cpp.o
[ 47%] Building CXX object src/CMakeFiles/llama.dir/models/mamba.cpp.o
[ 47%] Building CXX object src/CMakeFiles/llama.dir/models/mimo2-iswa.cpp.o
[ 47%] Building CXX object src/CMakeFiles/llama.dir/models/minicpm3.cpp.o
[ 47%] Building CXX object src/CMakeFiles/llama.dir/models/minimax-m2.cpp.o
[ 48%] Building CXX object src/CMakeFiles/llama.dir/models/mistral3.cpp.o
[ 48%] Building CXX object src/CMakeFiles/llama.dir/models/modern-bert.cpp.o
[ 48%] Building CXX object src/CMakeFiles/llama.dir/models/nemotron-h.cpp.o
[ 48%] Building CXX object src/CMakeFiles/llama.dir/models/mpt.cpp.o
[ 48%] Building CXX object src/CMakeFiles/llama.dir/models/nemotron.cpp.o
[ 49%] Building CXX object src/CMakeFiles/llama.dir/models/neo-bert.cpp.o
[ 49%] Building CXX object src/CMakeFiles/llama.dir/models/olmo.cpp.o
[ 49%] Building CXX object src/CMakeFiles/llama.dir/models/olmo2.cpp.o
[ 49%] Building CXX object src/CMakeFiles/llama.dir/models/olmoe.cpp.o
[ 49%] Building CXX object src/CMakeFiles/llama.dir/models/openai-moe-iswa.cpp.o
[ 49%] Building CXX object src/CMakeFiles/llama.dir/models/openelm.cpp.o
[ 50%] Building CXX object src/CMakeFiles/llama.dir/models/orion.cpp.o
[ 50%] Building CXX object src/CMakeFiles/llama.dir/models/paddleocr.cpp.o
[ 50%] Building CXX object src/CMakeFiles/llama.dir/models/pangu-embedded.cpp.o
[ 50%] Building CXX object src/CMakeFiles/llama.dir/models/phi2.cpp.o
[ 50%] Building CXX object src/CMakeFiles/llama.dir/models/phi3.cpp.o
[ 50%] Building CXX object src/CMakeFiles/llama.dir/models/plamo.cpp.o
[ 51%] Building CXX object src/CMakeFiles/llama.dir/models/plamo2.cpp.o
[ 51%] Building CXX object src/CMakeFiles/llama.dir/models/plamo3.cpp.o
[ 51%] Building CXX object src/CMakeFiles/llama.dir/models/plm.cpp.o
[ 51%] Building CXX object src/CMakeFiles/llama.dir/models/qwen.cpp.o
[ 51%] Building CXX object src/CMakeFiles/llama.dir/models/qwen2.cpp.o
[ 51%] Building CXX object src/CMakeFiles/llama.dir/models/qwen2moe.cpp.o
[ 52%] Building CXX object src/CMakeFiles/llama.dir/models/qwen2vl.cpp.o
[ 52%] Building CXX object src/CMakeFiles/llama.dir/models/qwen3.cpp.o
[ 52%] Building CXX object src/CMakeFiles/llama.dir/models/qwen35.cpp.o
[ 52%] Building CXX object src/CMakeFiles/llama.dir/models/qwen3moe.cpp.o
[ 52%] Building CXX object src/CMakeFiles/llama.dir/models/qwen35moe.cpp.o
[ 52%] Building CXX object src/CMakeFiles/llama.dir/models/qwen3next.cpp.o
[ 53%] Building CXX object src/CMakeFiles/llama.dir/models/qwen3vl-moe.cpp.o
[ 53%] Building CXX object src/CMakeFiles/llama.dir/models/qwen3vl.cpp.o
[ 53%] Building CXX object src/CMakeFiles/llama.dir/models/refact.cpp.o
[ 53%] Building CXX object src/CMakeFiles/llama.dir/models/rnd1.cpp.o
[ 53%] Building CXX object src/CMakeFiles/llama.dir/models/rwkv6-base.cpp.o
[ 53%] Building CXX object src/CMakeFiles/llama.dir/models/rwkv6.cpp.o
[ 54%] Building CXX object src/CMakeFiles/llama.dir/models/rwkv6qwen2.cpp.o
[ 54%] Building CXX object src/CMakeFiles/llama.dir/models/rwkv7-base.cpp.o
[ 54%] Building CXX object src/CMakeFiles/llama.dir/models/rwkv7.cpp.o
[ 54%] Building CXX object src/CMakeFiles/llama.dir/models/seed-oss.cpp.o
[ 54%] Building CXX object src/CMakeFiles/llama.dir/models/smallthinker.cpp.o
[ 54%] Building CXX object src/CMakeFiles/llama.dir/models/smollm3.cpp.o
[ 55%] Building CXX object src/CMakeFiles/llama.dir/models/stablelm.cpp.o
[ 55%] Building CXX object src/CMakeFiles/llama.dir/models/starcoder.cpp.o
[ 55%] Building CXX object src/CMakeFiles/llama.dir/models/step35-iswa.cpp.o
[ 55%] Building CXX object src/CMakeFiles/llama.dir/models/starcoder2.cpp.o
[ 55%] Building CXX object src/CMakeFiles/llama.dir/models/t5-dec.cpp.o
[ 55%] Building CXX object src/CMakeFiles/llama.dir/models/t5-enc.cpp.o
[ 56%] Building CXX object src/CMakeFiles/llama.dir/models/wavtokenizer-dec.cpp.o
[ 56%] Building CXX object src/CMakeFiles/llama.dir/models/xverse.cpp.o
[ 56%] Linking CXX shared library ../bin/libllama.so
[ 56%] Built target llama
[ 56%] Building C object tests/CMakeFiles/test-c.dir/test-c.c.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/chat-diff-analyzer.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/console.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/debug.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/download.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/json-partial.cpp.o
[ 56%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/mtmd.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/json-schema-to-grammar.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/arg.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/llguidance.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/chat-auto-parser-generator.cpp.o
[ 56%] Building CXX object common/CMakeFiles/common.dir/chat-auto-parser-helpers.cpp.o
[ 56%] Building CXX object examples/simple/CMakeFiles/llama-simple.dir/simple.cpp.o
[ 57%] Building CXX object common/CMakeFiles/common.dir/chat-peg-parser.cpp.o
[ 57%] Building CXX object common/CMakeFiles/common.dir/chat.cpp.o
[ 57%] Building CXX object common/CMakeFiles/common.dir/common.cpp.o
[ 57%] Building CXX object examples/simple-chat/CMakeFiles/llama-simple-chat.dir/simple-chat.cpp.o
[ 58%] Building CXX object common/CMakeFiles/common.dir/hf-cache.cpp.o
[ 58%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/mtmd-image.cpp.o
[ 59%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/mtmd-audio.cpp.o
[ 59%] Linking C executable ../bin/test-c
[ 59%] Built target test-c
[ 59%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/mtmd-helper.cpp.o
[ 59%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/clip.cpp.o
[ 59%] Linking CXX executable ../../bin/llama-simple
[ 59%] Built target llama-simple
[ 59%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/cogvlm.cpp.o
[ 59%] Linking CXX executable ../../bin/llama-simple-chat
[ 59%] Built target llama-simple-chat
[ 59%] Building CXX object common/CMakeFiles/common.dir/log.cpp.o
[ 59%] Building CXX object common/CMakeFiles/common.dir/ngram-cache.cpp.o
[ 60%] Building CXX object common/CMakeFiles/common.dir/ngram-map.cpp.o
[ 60%] Building CXX object common/CMakeFiles/common.dir/ngram-mod.cpp.o
[ 60%] Building CXX object common/CMakeFiles/common.dir/peg-parser.cpp.o
[ 60%] Building CXX object common/CMakeFiles/common.dir/preset.cpp.o
[ 60%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/conformer.cpp.o
[ 61%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/glm4v.cpp.o
[ 61%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/internvl.cpp.o
[ 61%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/kimivl.cpp.o
[ 61%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/kimik25.cpp.o
[ 61%] Building CXX object common/CMakeFiles/common.dir/regex-partial.cpp.o
[ 61%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/nemotron-v2-vl.cpp.o
[ 61%] Building CXX object common/CMakeFiles/common.dir/reasoning-budget.cpp.o
[ 61%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/llama4.cpp.o
[ 62%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/llava.cpp.o
[ 62%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/minicpmv.cpp.o
[ 62%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/paddleocr.cpp.o
[ 62%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/pixtral.cpp.o
[ 62%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/qwen2vl.cpp.o
[ 62%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/qwen3vl.cpp.o
[ 63%] Building CXX object common/CMakeFiles/common.dir/sampling.cpp.o
[ 64%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/siglip.cpp.o
[ 64%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/whisper-enc.cpp.o
[ 64%] Building CXX object common/CMakeFiles/common.dir/speculative.cpp.o
[ 64%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/deepseekocr.cpp.o
[ 64%] Building CXX object common/CMakeFiles/common.dir/unicode.cpp.o
[ 64%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/mobilenetv5.cpp.o
[ 64%] Building CXX object common/CMakeFiles/common.dir/jinja/lexer.cpp.o
[ 64%] Building CXX object common/CMakeFiles/common.dir/jinja/parser.cpp.o
[ 64%] Building CXX object common/CMakeFiles/common.dir/jinja/runtime.cpp.o
[ 64%] Building CXX object tools/mtmd/CMakeFiles/mtmd.dir/models/youtuvl.cpp.o
[ 65%] Building CXX object common/CMakeFiles/common.dir/jinja/value.cpp.o
[ 65%] Building CXX object common/CMakeFiles/common.dir/jinja/string.cpp.o
[ 65%] Building CXX object common/CMakeFiles/common.dir/jinja/caps.cpp.o
[ 65%] Building CXX object common/CMakeFiles/common.dir/__/license.cpp.o
[ 65%] Linking CXX shared library ../../bin/libmtmd.so
[ 65%] Built target mtmd
[ 65%] Linking CXX static library libcommon.a
[ 65%] Built target common
[ 65%] Building CXX object tests/CMakeFiles/test-sampling.dir/test-sampling.cpp.o
[ 65%] Building CXX object tests/CMakeFiles/test-json-schema-to-grammar.dir/test-json-schema-to-grammar.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-gbnf-validator.dir/test-gbnf-validator.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-llama-archs.dir/test-llama-archs.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-jinja.dir/test-jinja.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-quantize-stats.dir/test-quantize-stats.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-tokenizer-0.dir/test-tokenizer-0.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-llama-grammar.dir/test-llama-grammar.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-grammar-integration.dir/test-grammar-integration.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-tokenizer-1-bpe.dir/test-tokenizer-1-bpe.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-chat.dir/test-chat.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-chat-template.dir/test-chat-template.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-reasoning-budget.dir/test-reasoning-budget.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-tokenizer-1-spm.dir/test-tokenizer-1-spm.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-grammar-parser.dir/test-grammar-parser.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-chat-auto-parser.dir/test-chat-auto-parser.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-chat-peg-parser.dir/test-chat-peg-parser.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-log.dir/test-log.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/test-peg-parser.cpp.o
[ 66%] Building CXX object tests/CMakeFiles/test-json-partial.dir/test-json-partial.cpp.o
[ 67%] Building CXX object tests/CMakeFiles/test-log.dir/get-model.cpp.o
[ 67%] Linking CXX executable ../bin/test-log
[ 67%] Built target test-log
[ 68%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/peg-parser/simple-tokenize.cpp.o
[ 68%] Linking CXX executable ../bin/test-gbnf-validator
[ 68%] Linking CXX executable ../bin/test-tokenizer-1-bpe
[ 68%] Built target test-gbnf-validator
[ 68%] Building CXX object tests/CMakeFiles/test-jinja.dir/get-model.cpp.o
[ 68%] Building CXX object tests/CMakeFiles/test-grammar-parser.dir/get-model.cpp.o
[ 69%] Building CXX object tests/CMakeFiles/test-reasoning-budget.dir/get-model.cpp.o
[ 69%] Linking CXX executable ../bin/test-reasoning-budget
[ 69%] Building CXX object tests/CMakeFiles/test-json-partial.dir/get-model.cpp.o
[ 69%] Built target test-tokenizer-1-bpe
[ 69%] Building CXX object tests/CMakeFiles/test-chat-template.dir/get-model.cpp.o
[ 70%] Building CXX object tests/CMakeFiles/test-llama-archs.dir/get-model.cpp.o
[ 70%] Building CXX object tests/CMakeFiles/test-sampling.dir/get-model.cpp.o
[ 70%] Building CXX object tests/CMakeFiles/test-llama-grammar.dir/get-model.cpp.o
[ 70%] Building CXX object tests/CMakeFiles/test-json-schema-to-grammar.dir/get-model.cpp.o
[ 71%] Building CXX object tests/CMakeFiles/test-chat-peg-parser.dir/peg-parser/simple-tokenize.cpp.o
[ 71%] Linking CXX executable ../bin/test-sampling
[ 72%] Building CXX object tests/CMakeFiles/test-chat.dir/get-model.cpp.o
[ 72%] Built target test-reasoning-budget
[ 72%] Building CXX object tests/CMakeFiles/test-chat-auto-parser.dir/get-model.cpp.o
[ 72%] Building CXX object tests/CMakeFiles/test-grammar-integration.dir/get-model.cpp.o
[ 72%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/peg-parser/test-basic.cpp.o
[ 72%] Linking CXX executable ../bin/test-llama-archs
[ 72%] Linking CXX executable ../bin/test-llama-grammar
[ 72%] Building CXX object tests/CMakeFiles/test-regex-partial.dir/test-regex-partial.cpp.o
[ 72%] Building CXX object tests/CMakeFiles/test-chat-peg-parser.dir/get-model.cpp.o
[ 72%] Built target test-sampling
[ 73%] Linking CXX executable ../bin/test-tokenizer-0
[ 73%] Building CXX object tests/CMakeFiles/test-thread-safety.dir/test-thread-safety.cpp.o
[ 73%] Building CXX object tests/CMakeFiles/test-regex-partial.dir/get-model.cpp.o
[ 73%] Built target test-llama-archs
[ 73%] Linking CXX executable ../bin/test-tokenizer-1-spm
[ 73%] Built target test-llama-grammar
[ 73%] Building CXX object tests/CMakeFiles/test-thread-safety.dir/get-model.cpp.o
[ 73%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/peg-parser/test-gbnf-generation.cpp.o
[ 73%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/peg-parser/test-json-parser.cpp.o
[ 74%] Building CXX object tests/CMakeFiles/test-arg-parser.dir/test-arg-parser.cpp.o
[ 74%] Built target test-tokenizer-0
[ 74%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/peg-parser/test-json-serialization.cpp.o
[ 74%] Built target test-tokenizer-1-spm
[ 74%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/peg-parser/test-python-dict-parser.cpp.o
[ 75%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/peg-parser/test-unicode.cpp.o
[ 76%] Linking CXX executable ../bin/test-grammar-parser
[ 76%] Built target test-grammar-parser
[ 76%] Building CXX object tests/CMakeFiles/test-arg-parser.dir/get-model.cpp.o
[ 76%] Building CXX object tests/CMakeFiles/test-peg-parser.dir/get-model.cpp.o
[ 76%] Building CXX object tests/CMakeFiles/test-opt.dir/test-opt.cpp.o
[ 76%] Linking CXX executable ../bin/test-regex-partial
[ 76%] Built target test-regex-partial
[ 76%] Building CXX object tests/CMakeFiles/test-opt.dir/get-model.cpp.o
[ 77%] Linking CXX executable ../bin/test-json-partial
[ 77%] Building CXX object tests/CMakeFiles/test-gguf.dir/test-gguf.cpp.o
[ 77%] Built target test-json-partial
[ 78%] Building CXX object tests/CMakeFiles/test-backend-ops.dir/test-backend-ops.cpp.o
[ 78%] Linking CXX executable ../bin/test-thread-safety
[ 78%] Built target test-thread-safety
[ 78%] Building CXX object tests/CMakeFiles/test-gguf.dir/get-model.cpp.o
[ 78%] Building CXX object tests/CMakeFiles/test-backend-ops.dir/get-model.cpp.o
[ 78%] Linking CXX executable ../bin/test-opt
[ 78%] Building CXX object tests/CMakeFiles/test-model-load-cancel.dir/test-model-load-cancel.cpp.o
[ 78%] Building CXX object tests/CMakeFiles/test-model-load-cancel.dir/get-model.cpp.o
[ 78%] Built target test-opt
[ 78%] Building CXX object tests/CMakeFiles/test-autorelease.dir/test-autorelease.cpp.o
[ 78%] Linking CXX executable ../bin/test-model-load-cancel
[ 78%] Linking CXX executable ../bin/test-arg-parser
[ 78%] Built target test-model-load-cancel
[ 78%] Building CXX object tests/CMakeFiles/test-autorelease.dir/get-model.cpp.o
[ 78%] Building CXX object tests/CMakeFiles/test-backend-sampler.dir/test-backend-sampler.cpp.o
[ 78%] Linking CXX executable ../bin/test-quantize-stats
[ 78%] Built target test-arg-parser
[ 78%] Building CXX object tests/CMakeFiles/test-backend-sampler.dir/get-model.cpp.o
[ 78%] Linking CXX executable ../bin/test-autorelease
[ 78%] Built target test-quantize-stats
[ 78%] Building CXX object tests/CMakeFiles/test-state-restore-fragmented.dir/test-state-restore-fragmented.cpp.o
[ 79%] Building CXX object tests/CMakeFiles/test-barrier.dir/test-barrier.cpp.o
[ 79%] Built target test-autorelease
[ 79%] Building CXX object tests/CMakeFiles/test-barrier.dir/get-model.cpp.o
[ 80%] Building CXX object tests/CMakeFiles/test-state-restore-fragmented.dir/get-model.cpp.o
[ 80%] Linking CXX executable ../bin/test-grammar-integration
[ 80%] Building CXX object tests/CMakeFiles/test-quantize-fns.dir/test-quantize-fns.cpp.o
[ 80%] Built target test-grammar-integration
[ 80%] Building CXX object tests/CMakeFiles/test-quantize-fns.dir/get-model.cpp.o
[ 80%] Linking CXX executable ../bin/test-barrier
[ 81%] Building CXX object tests/CMakeFiles/test-quantize-perf.dir/test-quantize-perf.cpp.o
[ 81%] Built target test-barrier
[ 81%] Building CXX object tests/CMakeFiles/test-quantize-perf.dir/get-model.cpp.o
[ 81%] Building CXX object tests/CMakeFiles/test-rope.dir/test-rope.cpp.o
[ 81%] Building C object tests/CMakeFiles/test-mtmd-c-api.dir/test-mtmd-c-api.c.o
[ 81%] Linking CXX executable ../bin/test-quantize-fns
[ 81%] Linking CXX executable ../bin/test-gguf
[ 82%] Building CXX object tests/CMakeFiles/test-mtmd-c-api.dir/get-model.cpp.o
[ 82%] Built target test-quantize-fns
[ 82%] Linking CXX executable ../bin/test-mtmd-c-api
[ 82%] Building CXX object tests/CMakeFiles/gguf-model-data.dir/gguf-model-data.cpp.o
[ 83%] Building CXX object tests/CMakeFiles/test-rope.dir/get-model.cpp.o
[ 83%] Built target test-gguf
[ 83%] Built target test-mtmd-c-api
[ 83%] Building CXX object tests/CMakeFiles/test-alloc.dir/test-alloc.cpp.o
[ 83%] Linking CXX executable ../bin/test-rope
[ 83%] Building CXX object tests/CMakeFiles/export-graph-ops.dir/export-graph-ops.cpp.o
[ 83%] Built target test-rope
[ 83%] Building CXX object examples/batched/CMakeFiles/llama-batched.dir/batched.cpp.o
[ 83%] Linking CXX executable ../bin/test-json-schema-to-grammar
[ 83%] Linking CXX executable ../bin/test-quantize-perf
[ 83%] Built target test-json-schema-to-grammar
[ 83%] Building CXX object tests/CMakeFiles/test-alloc.dir/get-model.cpp.o
[ 84%] Building CXX object examples/debug/CMakeFiles/llama-debug.dir/debug.cpp.o
[ 84%] Built target test-quantize-perf
[ 85%] Building CXX object examples/embedding/CMakeFiles/llama-embedding.dir/embedding.cpp.o
[ 85%] Linking CXX executable ../bin/test-state-restore-fragmented
[ 85%] Building CXX object examples/idle/CMakeFiles/llama-idle.dir/idle.cpp.o
[ 85%] Building CXX object examples/eval-callback/CMakeFiles/llama-eval-callback.dir/eval-callback.cpp.o
[ 85%] Built target test-state-restore-fragmented
[ 85%] Building CXX object examples/lookahead/CMakeFiles/llama-lookahead.dir/lookahead.cpp.o
[ 85%] Linking CXX executable ../bin/test-alloc
[ 85%] Built target test-alloc
[ 85%] Building CXX object examples/lookup/CMakeFiles/llama-lookup.dir/lookup.cpp.o
[ 85%] Linking CXX executable ../bin/export-graph-ops
[ 85%] Linking CXX executable ../../bin/llama-batched
[ 85%] Built target export-graph-ops
[ 86%] Building CXX object examples/lookup/CMakeFiles/llama-lookup-create.dir/lookup-create.cpp.o
[ 86%] Built target llama-batched
[ 86%] Building CXX object examples/lookup/CMakeFiles/llama-lookup-merge.dir/lookup-merge.cpp.o
[ 86%] Linking CXX executable ../bin/test-backend-sampler
[ 86%] Building CXX object examples/lookup/CMakeFiles/llama-lookup-stats.dir/lookup-stats.cpp.o
[ 87%] Building CXX object examples/parallel/CMakeFiles/llama-parallel.dir/parallel.cpp.o
[ 87%] Linking CXX executable ../../bin/llama-embedding
[ 87%] Built target test-backend-sampler
[ 87%] Building CXX object examples/passkey/CMakeFiles/llama-passkey.dir/passkey.cpp.o
[ 87%] Linking CXX executable ../../bin/llama-idle
[ 87%] Linking CXX executable ../../bin/llama-lookup-merge
[ 87%] Built target llama-embedding
[ 87%] Building CXX object examples/retrieval/CMakeFiles/llama-retrieval.dir/retrieval.cpp.o
[ 87%] Linking CXX executable ../bin/test-chat-template
[ 87%] Built target llama-lookup-merge
[ 87%] Linking CXX executable ../../bin/llama-lookahead
[ 87%] Building CXX object examples/save-load-state/CMakeFiles/llama-save-load-state.dir/save-load-state.cpp.o
[ 87%] Built target test-chat-template
[ 87%] Built target llama-idle
[ 87%] Building CXX object examples/speculative/CMakeFiles/llama-speculative.dir/speculative.cpp.o
[ 87%] Building CXX object examples/speculative-simple/CMakeFiles/llama-speculative-simple.dir/speculative-simple.cpp.o
[ 87%] Linking CXX executable ../../bin/llama-lookup
[ 87%] Built target llama-lookahead
[ 88%] Building CXX object examples/gen-docs/CMakeFiles/llama-gen-docs.dir/gen-docs.cpp.o
[ 88%] Built target llama-lookup
[ 89%] Building CXX object examples/training/CMakeFiles/llama-finetune.dir/finetune.cpp.o
[ 89%] Linking CXX executable ../../bin/llama-eval-callback
[ 89%] Linking CXX executable ../../bin/llama-lookup-stats
[ 89%] Linking CXX executable ../../bin/llama-parallel
[ 90%] Linking CXX executable ../../bin/llama-save-load-state
[ 90%] Linking CXX executable ../../bin/llama-lookup-create
[ 90%] Built target llama-eval-callback
[ 90%] Building CXX object examples/diffusion/CMakeFiles/llama-diffusion-cli.dir/diffusion-cli.cpp.o
[ 90%] Built target llama-lookup-stats
[ 90%] Building CXX object examples/convert-llama2c-to-ggml/CMakeFiles/llama-convert-llama2c-to-ggml.dir/convert-llama2c-to-ggml.cpp.o
[ 90%] Built target llama-parallel
[ 90%] Building CXX object pocs/vdot/CMakeFiles/llama-vdot.dir/vdot.cpp.o
[ 90%] Built target llama-lookup-create
[ 91%] Building CXX object pocs/vdot/CMakeFiles/llama-q8dot.dir/q8dot.cpp.o
[ 91%] Built target llama-save-load-state
[ 91%] Building CXX object tools/batched-bench/CMakeFiles/llama-batched-bench.dir/batched-bench.cpp.o
[ 91%] Linking CXX executable ../../bin/llama-passkey
[ 91%] Linking CXX executable ../../bin/llama-retrieval
[ 91%] Built target llama-passkey
[ 92%] Building CXX object tools/gguf-split/CMakeFiles/llama-gguf-split.dir/gguf-split.cpp.o
[ 92%] Linking CXX executable ../../bin/llama-vdot
[ 92%] Built target llama-retrieval
[ 92%] Building CXX object tools/imatrix/CMakeFiles/llama-imatrix.dir/imatrix.cpp.o
[ 92%] Building CXX object tools/llama-bench/CMakeFiles/llama-bench.dir/llama-bench.cpp.o
[ 92%] Linking CXX executable ../../bin/llama-q8dot
[ 92%] Built target llama-vdot
[ 92%] Building CXX object tools/completion/CMakeFiles/llama-completion.dir/completion.cpp.o
[ 92%] Built target llama-q8dot
[ 92%] Linking CXX executable ../../bin/llama-debug
[ 92%] Linking CXX executable ../../bin/llama-gen-docs
[ 92%] Linking CXX executable ../../bin/llama-finetune
[ 92%] Building CXX object tools/perplexity/CMakeFiles/llama-perplexity.dir/perplexity.cpp.o
[ 92%] Built target llama-gen-docs
[ 93%] Linking CXX executable ../../bin/llama-batched-bench
[ 93%] Linking CXX static library libgguf-model-data.a
[ 93%] Building CXX object tools/quantize/CMakeFiles/llama-quantize.dir/quantize.cpp.o
[ 93%] Built target llama-debug
[ 94%] Building CXX object tools/server/CMakeFiles/server-context.dir/server-task.cpp.o
[ 94%] Built target llama-finetune
[ 94%] Built target gguf-model-data
[ 94%] Linking CXX executable ../../bin/llama-gguf-split
[ 94%] Building CXX object tools/server/CMakeFiles/server-context.dir/server-queue.cpp.o
[ 94%] Building CXX object tools/tokenize/CMakeFiles/llama-tokenize.dir/tokenize.cpp.o
[ 94%] Linking CXX executable ../bin/test-peg-parser
[ 94%] Built target llama-gguf-split
[ 95%] Linking CXX executable ../../bin/llama-speculative
/home/sparky/Workspace/ai-spark/src/llama-cpp/tools/perplexity/perplexity.cpp: In lambda function:
/home/sparky/Workspace/ai-spark/src/llama-cpp/tools/perplexity/perplexity.cpp:1771:41: note: parameter passing for argument of type ‘std::pair<double, double>’ when C++17 is enabled changed to match C++14 in GCC 10.1
1771 |             return std::make_pair(0., 0.);
      |                                         ^
[ 95%] Building CXX object tools/parser/CMakeFiles/llama-debug-template-parser.dir/debug-template-parser.cpp.o
[ 95%] Built target test-peg-parser
[ 95%] Building CXX object tools/parser/CMakeFiles/llama-template-analysis.dir/template-analysis.cpp.o
[ 95%] Built target llama-batched-bench
[ 95%] Building CXX object tools/tts/CMakeFiles/llama-tts.dir/tts.cpp.o
[ 95%] Linking CXX executable ../../bin/llama-speculative-simple
[ 95%] Linking CXX executable ../../bin/llama-convert-llama2c-to-ggml
[ 95%] Built target llama-speculative
[ 96%] Linking CXX executable ../../bin/llama-tokenize
[ 96%] Building CXX object tools/mtmd/CMakeFiles/llama-mtmd-cli.dir/mtmd-cli.cpp.o
[ 96%] Built target llama-convert-llama2c-to-ggml
[ 96%] Building CXX object tools/server/CMakeFiles/server-context.dir/server-common.cpp.o
[ 96%] Built target llama-speculative-simple
[ 96%] Building CXX object tools/server/CMakeFiles/server-context.dir/server-context.cpp.o
[ 96%] Built target llama-tokenize
[ 96%] Building CXX object tools/mtmd/CMakeFiles/llama-mtmd-debug.dir/debug/mtmd-debug.cpp.o
[ 96%] Linking CXX executable ../../bin/llama-diffusion-cli
[ 96%] Linking CXX executable ../../bin/llama-quantize
[ 96%] Built target llama-quantize
[ 96%] Building CXX object tools/cvector-generator/CMakeFiles/llama-cvector-generator.dir/cvector-generator.cpp.o
[ 96%] Built target llama-diffusion-cli
[ 96%] Building CXX object tools/export-lora/CMakeFiles/llama-export-lora.dir/export-lora.cpp.o
[ 96%] Linking CXX executable ../bin/test-chat
[ 96%] Linking CXX executable ../bin/test-chat-auto-parser
[ 96%] Linking CXX executable ../../bin/llama-perplexity
[ 96%] Built target test-chat
[ 96%] Building CXX object tools/server/CMakeFiles/server-context.dir/server-tools.cpp.o
[ 96%] Built target test-chat-auto-parser
[ 96%] Building CXX object tools/fit-params/CMakeFiles/llama-fit-params.dir/fit-params.cpp.o
[ 96%] Linking CXX executable ../bin/test-chat-peg-parser
[ 96%] Built target llama-perplexity
[ 96%] Building CXX object tools/results/CMakeFiles/llama-results.dir/results.cpp.o
[ 96%] Built target test-chat-peg-parser
[ 96%] Building CXX object tests/CMakeFiles/test-gguf-model-data.dir/test-gguf-model-data.cpp.o
[ 96%] Linking CXX executable ../../bin/llama-mtmd-debug
[ 97%] Linking CXX executable ../bin/test-gguf-model-data
[ 97%] Built target test-gguf-model-data
[ 97%] Built target llama-mtmd-debug
[ 97%] Linking CXX executable ../../bin/llama-results
[ 97%] Linking CXX executable ../../bin/llama-mtmd-cli
[ 97%] Built target llama-results
[ 97%] Linking CXX executable ../../bin/llama-fit-params
[ 97%] Built target llama-mtmd-cli
[ 98%] Linking CXX executable ../../bin/llama-completion
[ 98%] Built target llama-fit-params
[ 98%] Linking CXX executable ../../bin/llama-imatrix
[ 98%] Linking CXX executable ../../bin/llama-cvector-generator
[ 98%] Built target llama-completion
[ 98%] Linking CXX executable ../../bin/llama-export-lora
[ 98%] Built target llama-cvector-generator
[ 98%] Built target llama-imatrix
[ 98%] Built target llama-export-lora
[ 98%] Linking CXX executable ../bin/test-jinja
[ 98%] Built target test-jinja
[ 98%] Linking CXX executable ../../bin/llama-template-analysis
[ 98%] Linking CXX executable ../../bin/llama-debug-template-parser
[ 98%] Built target llama-template-analysis
[ 98%] Built target llama-debug-template-parser
[ 98%] Linking CXX executable ../../bin/llama-bench
[ 98%] Built target llama-bench
[ 98%] Linking CXX executable ../bin/test-backend-ops
[ 98%] Linking CXX executable ../../bin/llama-tts
[ 98%] Built target test-backend-ops
[ 98%] Built target llama-tts
[ 99%] Linking CXX static library libserver-context.a
[ 99%] Built target server-context
[ 99%] Generating loading.html.hpp
[ 99%] Generating index.html.gz.hpp
[ 99%] Building CXX object tools/cli/CMakeFiles/llama-cli.dir/cli.cpp.o
[ 99%] Building CXX object tools/server/CMakeFiles/llama-server.dir/server-models.cpp.o
[ 99%] Building CXX object tools/server/CMakeFiles/llama-server.dir/server-http.cpp.o
[ 99%] Building CXX object tools/server/CMakeFiles/llama-server.dir/server.cpp.o
[ 99%] Linking CXX executable ../../bin/llama-cli
[ 99%] Built target llama-cli
[100%] Linking CXX executable ../../bin/llama-server
[100%] Built target llama-server
```

## Qwen3-Coder-Next-MXFP4\_MOE

```
src/llama-cpp/build/bin/llama-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--Qwen3-Coder-Next-GGUF/snapshots/ce09c67b53bc8739eef83fe67b2f5d293c270632/Qwen3-Coder-Next-MXFP4_MOE.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 | 1743.03 ± 5.06 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 | 49.33 ± 0.36 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d4096 | 1708.29 ± 3.86 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d4096 | 49.15 ± 0.47 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d8192 | 1677.69 ± 2.23 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d8192 | 47.43 ± 0.59 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d16384 | 1606.85 ± 3.13 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d16384 | 44.98 ± 0.36 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d32768 | 1492.84 ± 2.35 |
| qwen3next 80B.A3B MXFP4 MoE | 44.73 GiB | 79.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d32768 | 40.86 ± 0.27 |

build: [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0) (8580)

```
src/llama-cpp/build/bin/llama-batched-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--Qwen3-Coder-Next-GGUF/snapshots/ce09c67b53bc8739eef83fe67b2f5d293c270632/Qwen3-Coder-Next-MXFP4_MOE.gguf -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

build: 8580 ( [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0)) with GNU 13.3.0 for Linux aarch64

main: n\_kv\_max = 303104, n\_batch = 2048, n\_ubatch = 2048, flash\_attn = 1, is\_pp\_shared = 0, is\_tg\_separate = 0, n\_gpu\_layers = -1, n\_threads = 20, n\_threads\_batch = 20

| PP | TG | B | N\_KV | T\_PP s | S\_PP t/s | T\_TG s | S\_TG t/s | T s | S t/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4096 | 32 | 1 | 4128 | 2.562 | 1598.53 | 0.690 | 46.35 | 3.253 | 1269.06 |
| 4096 | 32 | 2 | 8256 | 4.714 | 1737.62 | 0.925 | 69.19 | 5.640 | 1463.95 |
| 4096 | 32 | 4 | 16512 | 9.417 | 1739.81 | 1.262 | 101.39 | 10.680 | 1546.13 |
| 4096 | 32 | 8 | 33024 | 18.885 | 1735.14 | 1.954 | 131.03 | 20.839 | 1584.75 |
| 4096 | 32 | 16 | 66048 | 37.889 | 1729.70 | 3.622 | 141.35 | 41.511 | 1591.10 |
| 4096 | 32 | 32 | 132096 | 75.499 | 1736.08 | 5.992 | 170.90 | 81.491 | 1621.00 |
| 8192 | 32 | 1 | 8224 | 4.759 | 1721.23 | 0.738 | 43.34 | 5.498 | 1495.87 |
| 8192 | 32 | 2 | 16448 | 9.523 | 1720.52 | 0.947 | 67.58 | 10.470 | 1571.01 |
| 8192 | 32 | 4 | 32896 | 19.049 | 1720.23 | 1.304 | 98.13 | 20.353 | 1616.27 |
| 8192 | 32 | 8 | 65792 | 38.046 | 1722.55 | 2.073 | 123.49 | 40.119 | 1639.92 |
| 8192 | 32 | 16 | 131584 | 76.068 | 1723.09 | 3.895 | 131.47 | 79.962 | 1645.57 |
| 8192 | 32 | 32 | 263168 | 152.137 | 1723.07 | 6.537 | 156.66 | 158.674 | 1658.54 |

## Qwen3.5-35B-A3B-MXFP4\_MOE

```
src/llama-cpp/build/bin/llama-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--Qwen3.5-35B-A3B-GGUF/snapshots/bc014a17be43adabd7066b7a86075ff935c6a4e2/Qwen3.5-35B-A3B-MXFP4_MOE.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 | 2788.57 ± 6.85 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | tg32 | 59.98 ± 0.56 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d4096 | 2740.31 ± 8.91 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d4096 | 59.45 ± 0.49 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d8192 | 2669.27 ± 9.32 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d8192 | 56.89 ± 0.82 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d16384 | 2520.22 ± 3.67 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d16384 | 54.42 ± 0.52 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d32768 | 2259.41 ± 4.74 |
| qwen35moe 35B.A3B Q4\_K - Medium | 20.09 GiB | 34.66 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d32768 | 49.70 ± 0.39 |

build: [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0) (8580)

```
src/llama-cpp/build/bin/llama-batched-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--Qwen3.5-35B-A3B-GGUF/snapshots/bc014a17be43adabd7066b7a86075ff935c6a4e2/Qwen3.5-35B-A3B-MXFP4_MOE.gguf -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

build: 8580 ( [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0)) with GNU 13.3.0 for Linux aarch64

main: n\_kv\_max = 303104, n\_batch = 2048, n\_ubatch = 2048, flash\_attn = 1, is\_pp\_shared = 0, is\_tg\_separate = 0, n\_gpu\_layers = -1, n\_threads = 20, n\_threads\_batch = 20

| PP | TG | B | N\_KV | T\_PP s | S\_PP t/s | T\_TG s | S\_TG t/s | T s | S t/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4096 | 32 | 1 | 4128 | 1.468 | 2790.51 | 0.557 | 57.46 | 2.025 | 2038.74 |
| 4096 | 32 | 2 | 8256 | 2.908 | 2817.29 | 0.717 | 89.24 | 3.625 | 2277.54 |
| 4096 | 32 | 4 | 16512 | 5.827 | 2811.77 | 0.997 | 128.45 | 6.823 | 2419.90 |
| 4096 | 32 | 8 | 33024 | 11.647 | 2813.42 | 1.574 | 162.62 | 13.221 | 2497.79 |
| 4096 | 32 | 16 | 66048 | 23.282 | 2814.90 | 2.883 | 177.58 | 26.165 | 2524.29 |
| 4096 | 32 | 32 | 132096 | 46.572 | 2814.37 | 4.729 | 216.53 | 51.301 | 2574.90 |
| 8192 | 32 | 1 | 8224 | 2.961 | 2766.20 | 0.575 | 55.60 | 3.537 | 2325.17 |
| 8192 | 32 | 2 | 16448 | 5.907 | 2773.49 | 0.741 | 86.34 | 6.649 | 2473.91 |
| 8192 | 32 | 4 | 32896 | 11.795 | 2778.21 | 1.042 | 122.88 | 12.836 | 2562.73 |
| 8192 | 32 | 8 | 65792 | 23.591 | 2778.04 | 1.685 | 151.90 | 25.276 | 2602.95 |
| 8192 | 32 | 16 | 131584 | 47.024 | 2787.36 | 3.119 | 164.17 | 50.142 | 2624.21 |
| 8192 | 32 | 32 | 263168 | 93.922 | 2791.08 | 5.189 | 197.35 | 99.111 | 2655.29 |

## Qwen3.5-122B-A10B-MXFP4\_MOE

```
src/llama-cpp/build/bin/llama-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--Qwen3.5-122B-A10B-GGUF/snapshots/51eab4d59d53f573fb9206cb3ce613f1d0aa392b/MXFP4_MOE/Qwen3.5-122B-A10B-MXFP4_MOE-00001-of-00003.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 | 1074.77 ± 4.18 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | tg32 | 21.33 ± 0.05 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d4096 | 1049.88 ± 4.73 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d4096 | 20.98 ± 0.08 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d8192 | 1026.43 ± 1.82 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d8192 | 20.87 ± 0.10 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d16384 | 976.22 ± 1.54 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d16384 | 20.37 ± 0.11 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d32768 | 897.12 ± 1.18 |
| qwen35moe 122B.A10B Q4\_K - Medium | 69.53 GiB | 122.11 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d32768 | 19.54 ± 0.07 |

build: [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0) (8580)

```
src/llama-cpp/build/bin/llama-batched-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--Qwen3.5-122B-A10B-GGUF/snapshots/51eab4d59d53f573fb9206cb3ce613f1d0aa392b/MXFP4_MOE/Qwen3.5-122B-A10B-MXFP4_MOE-00001-of-00003.gguf -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

build: 8580 ( [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0)) with GNU 13.3.0 for Linux aarch64

main: n\_kv\_max = 303104, n\_batch = 2048, n\_ubatch = 2048, flash\_attn = 1, is\_pp\_shared = 0, is\_tg\_separate = 0, n\_gpu\_layers = -1, n\_threads = 20, n\_threads\_batch = 20

| PP | TG | B | N\_KV | T\_PP s | S\_PP t/s | T\_TG s | S\_TG t/s | T s | S t/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4096 | 32 | 1 | 4128 | 3.771 | 1086.19 | 1.454 | 22.02 | 5.225 | 790.12 |
| 4096 | 32 | 2 | 8256 | 7.549 | 1085.24 | 1.941 | 32.97 | 9.490 | 869.98 |
| 4096 | 32 | 4 | 16512 | 15.106 | 1084.61 | 2.803 | 45.66 | 17.909 | 921.99 |
| 4096 | 32 | 8 | 33024 | 30.337 | 1080.12 | 4.811 | 53.21 | 35.149 | 939.55 |
| 4096 | 32 | 16 | 66048 | 60.573 | 1081.93 | 7.867 | 65.08 | 68.440 | 965.05 |
| 4096 | 32 | 32 | 132096 | 121.032 | 1082.95 | 13.356 | 76.67 | 134.388 | 982.94 |
| 8192 | 32 | 1 | 8224 | 7.660 | 1069.48 | 1.473 | 21.73 | 9.133 | 900.51 |
| 8192 | 32 | 2 | 16448 | 15.283 | 1072.01 | 1.964 | 32.58 | 17.248 | 953.63 |
| 8192 | 32 | 4 | 32896 | 30.583 | 1071.46 | 2.848 | 44.94 | 33.431 | 984.00 |
| 8192 | 32 | 8 | 65792 | 61.198 | 1070.89 | 5.074 | 50.45 | 66.272 | 992.76 |
| 8192 | 32 | 16 | 131584 | 122.281 | 1071.89 | 8.405 | 60.92 | 130.686 | 1006.87 |
| 8192 | 32 | 32 | 263168 | 244.653 | 1071.49 | 14.523 | 70.51 | 259.176 | 1015.40 |

## gpt-oss-20b-UD-Q4\_K\_XL

```
src/llama-cpp/build/bin/llama-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--gpt-oss-20b-GGUF/snapshots/d449b42d93e1c2c7bda5312f5c25c8fb91dfa9b4/gpt-oss-20b-UD-Q4_K_XL.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 | 4452.88 ± 13.79 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | tg32 | 86.05 ± 0.40 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d4096 | 4230.47 ± 23.92 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d4096 | 81.59 ± 0.41 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d8192 | 3981.86 ± 38.44 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d8192 | 76.82 ± 1.92 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d16384 | 3366.15 ± 7.10 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d16384 | 72.28 ± 0.53 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d32768 | 2615.79 ± 7.89 |
| gpt-oss 20B Q4\_K - Medium | 11.04 GiB | 20.91 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d32768 | 62.34 ± 0.28 |

build: [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0) (8580)

```
src/llama-cpp/build/bin/llama-batched-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--gpt-oss-20b-GGUF/snapshots/d449b42d93e1c2c7bda5312f5c25c8fb91dfa9b4/gpt-oss-20b-UD-Q4_K_XL.gguf -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

build: 8580 ( [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0)) with GNU 13.3.0 for Linux aarch64

main: n\_kv\_max = 303104, n\_batch = 2048, n\_ubatch = 2048, flash\_attn = 1, is\_pp\_shared = 0, is\_tg\_separate = 0, n\_gpu\_layers = -1, n\_threads = 20, n\_threads\_batch = 20

| PP | TG | B | N\_KV | T\_PP s | S\_PP t/s | T\_TG s | S\_TG t/s | T s | S t/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4096 | 32 | 1 | 4128 | 1.054 | 3886.22 | 0.403 | 79.47 | 1.457 | 2833.89 |
| 4096 | 32 | 2 | 8256 | 1.821 | 4497.83 | 0.554 | 115.53 | 2.375 | 3475.79 |
| 4096 | 32 | 4 | 16512 | 3.629 | 4514.55 | 0.753 | 170.09 | 4.382 | 3768.40 |
| 4096 | 32 | 8 | 33024 | 7.267 | 4509.02 | 1.163 | 220.13 | 8.430 | 3917.37 |
| 4096 | 32 | 16 | 66048 | 14.474 | 4527.69 | 1.502 | 340.77 | 15.977 | 4133.95 |
| 4096 | 32 | 32 | 132096 | 28.984 | 4522.16 | 2.198 | 465.81 | 31.183 | 4236.19 |
| 8192 | 32 | 1 | 8224 | 1.877 | 4363.94 | 0.422 | 75.79 | 2.299 | 3576.52 |
| 8192 | 32 | 2 | 16448 | 3.749 | 4370.53 | 0.594 | 107.74 | 4.343 | 3787.46 |
| 8192 | 32 | 4 | 32896 | 7.461 | 4391.85 | 0.806 | 158.80 | 8.267 | 3979.13 |
| 8192 | 32 | 8 | 65792 | 14.895 | 4399.91 | 1.283 | 199.49 | 16.178 | 4066.73 |
| 8192 | 32 | 16 | 131584 | 29.761 | 4404.12 | 1.762 | 290.56 | 31.523 | 4174.18 |
| 8192 | 32 | 32 | 263168 | 59.602 | 4398.22 | 2.681 | 381.90 | 62.284 | 4225.32 |

## gpt-oss-120b-UD-Q4\_K\_XL

```
src/llama-cpp/build/bin/llama-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--gpt-oss-120b-GGUF/snapshots/ff1a82da6ad466e32284fa3d2b86694db3204789/UD-Q4_K_XL/gpt-oss-120b-UD-Q4_K_XL-00001-of-00002.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 | 2443.59 ± 11.32 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | tg32 | 62.36 ± 0.38 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d4096 | 2315.10 ± 7.06 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d4096 | 58.85 ± 0.32 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d8192 | 2222.26 ± 6.07 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d8192 | 55.51 ± 0.57 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d16384 | 1947.73 ± 4.30 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d16384 | 51.46 ± 0.23 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d32768 | 1561.09 ± 4.37 |
| gpt-oss 120B Q4\_K - Medium | 58.68 GiB | 116.83 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d32768 | 44.03 ± 0.14 |

build: [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0) (8580)

```
src/llama-cpp/build/bin/llama-batched-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--gpt-oss-120b-GGUF/snapshots/ff1a82da6ad466e32284fa3d2b86694db3204789/UD-Q4_K_XL/gpt-oss-120b-UD-Q4_K_XL-00001-of-00002.gguf -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

build: 8580 ( [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0)) with GNU 13.3.0 for Linux aarch64

main: n\_kv\_max = 303104, n\_batch = 2048, n\_ubatch = 2048, flash\_attn = 1, is\_pp\_shared = 0, is\_tg\_separate = 0, n\_gpu\_layers = -1, n\_threads = 20, n\_threads\_batch = 20

| PP | TG | B | N\_KV | T\_PP s | S\_PP t/s | T\_TG s | S\_TG t/s | T s | S t/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4096 | 32 | 1 | 4128 | 1.845 | 2219.77 | 0.562 | 56.98 | 2.407 | 1715.08 |
| 4096 | 32 | 2 | 8256 | 3.347 | 2447.20 | 0.810 | 79.00 | 4.158 | 1985.78 |
| 4096 | 32 | 4 | 16512 | 6.700 | 2445.22 | 1.182 | 108.28 | 7.883 | 2094.76 |
| 4096 | 32 | 8 | 33024 | 13.411 | 2443.28 | 1.929 | 132.70 | 15.341 | 2152.70 |
| 4096 | 32 | 16 | 66048 | 26.873 | 2438.75 | 2.650 | 193.24 | 29.522 | 2237.23 |
| 4096 | 32 | 32 | 132096 | 53.769 | 2437.68 | 3.923 | 261.01 | 57.692 | 2289.66 |
| 8192 | 32 | 1 | 8224 | 3.438 | 2383.12 | 0.593 | 53.99 | 4.030 | 2040.59 |
| 8192 | 32 | 2 | 16448 | 6.909 | 2371.47 | 0.896 | 71.43 | 7.805 | 2107.42 |
| 8192 | 32 | 4 | 32896 | 13.746 | 2383.87 | 1.266 | 101.12 | 15.012 | 2191.38 |
| 8192 | 32 | 8 | 65792 | 27.502 | 2382.92 | 2.187 | 117.05 | 29.690 | 2216.00 |
| 8192 | 32 | 16 | 131584 | 54.924 | 2386.41 | 2.980 | 171.81 | 57.904 | 2272.44 |
| 8192 | 32 | 32 | 263168 | 109.988 | 2383.39 | 4.688 | 218.42 | 114.676 | 2294.88 |

## NVIDIA-Nemotron-3-Nano-4B-UD-Q4\_K\_XL

```
src/llama-cpp/build/bin/llama-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--NVIDIA-Nemotron-3-Nano-4B-GGUF/snapshots/8e81be55c5aa3d63bb82b6ceec62d50805d9e1bb/NVIDIA-Nemotron-3-Nano-4B-UD-Q4_K_XL.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 | 3206.33 ± 8.89 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | tg32 | 63.04 ± 0.13 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d4096 | 3106.36 ± 9.75 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d4096 | 62.20 ± 0.32 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d8192 | 3003.92 ± 9.88 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d8192 | 60.13 ± 1.00 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d16384 | 2766.67 ± 10.90 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d16384 | 57.99 ± 0.22 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d32768 | 2439.79 ± 5.43 |
| nemotron\_h ?B Q4\_K - Medium | 2.91 GiB | 3.97 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d32768 | 53.66 ± 0.18 |

build: [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0) (8580)

```
src/llama-cpp/build/bin/llama-batched-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--NVIDIA-Nemotron-3-Nano-4B-GGUF/snapshots/8e81be55c5aa3d63bb82b6ceec62d50805d9e1bb/NVIDIA-Nemotron-3-Nano-4B-UD-Q4_K_XL.gguf -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap
```

main: n\_kv\_max = 303104, n\_batch = 2048, n\_ubatch = 2048, flash\_attn = 1, is\_pp\_shared = 0, is\_tg\_separate = 0, n\_gpu\_layers = -1, n\_threads = 20, n\_threads\_batch = 20

| PP | TG | B | N\_KV | T\_PP s | S\_PP t/s | T\_TG s | S\_TG t/s | T s | S t/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4096 | 32 | 1 | 4128 | 1.274 | 3214.88 | 0.524 | 61.03 | 1.798 | 2295.36 |
| 4096 | 32 | 2 | 8256 | 2.537 | 3229.14 | 0.767 | 83.47 | 3.304 | 2499.09 |
| 4096 | 32 | 4 | 16512 | 5.072 | 3230.44 | 1.190 | 107.56 | 6.262 | 2636.95 |
| 4096 | 32 | 8 | 33024 | 10.127 | 3235.79 | 2.107 | 121.51 | 12.233 | 2699.47 |
| 4096 | 32 | 16 | 66048 | 20.247 | 3236.84 | 3.877 | 132.05 | 24.124 | 2737.84 |
| 4096 | 32 | 32 | 132096 | 40.461 | 3239.43 | 7.417 | 138.07 | 47.878 | 2759.01 |
| 8192 | 32 | 1 | 8224 | 2.569 | 3188.43 | 0.536 | 59.65 | 3.106 | 2648.01 |
| 8192 | 32 | 2 | 16448 | 5.146 | 3183.92 | 0.778 | 82.26 | 5.924 | 2776.58 |
| 8192 | 32 | 4 | 32896 | 10.252 | 3196.27 | 1.234 | 103.69 | 11.486 | 2863.92 |
| 8192 | 32 | 8 | 65792 | 20.512 | 3195.07 | 2.198 | 116.48 | 22.709 | 2897.13 |
| 8192 | 32 | 16 | 131584 | 40.969 | 3199.30 | 4.079 | 125.53 | 45.048 | 2921.00 |
| 8192 | 32 | 32 | 263168 | 81.908 | 3200.46 | 7.824 | 130.88 | 89.732 | 2932.82 |

## NVIDIA-Nemotron-3-Super-120B-A12B-MXFP4\_MOE

```
src/llama-cpp/build/bin/llama-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--NVIDIA-Nemotron-3-Super-120B-A12B-GGUF/snapshots/036038fb30334a2d56a146c6f0d4871ab5edccbb/MXFP4_MOE/NVIDIA-Nemotron-3-Super-120B-A12B-MXFP4_MOE-00001-of-00003.gguf -fa 1 -d 0,4096,8192,16384,32768 -p 2048 -n 32 -ub 2048 -mmp 0
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

| model | size | params | backend | ngl | n\_ubatch | fa | mmap | test | t/s |
| --- | --: | --: | --- | --: | --: | --: | --: | --: | --: |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 | 729.57 ± 1.52 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 | 16.58 ± 0.04 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d4096 | 724.96 ± 0.83 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d4096 | 16.57 ± 0.05 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d8192 | 720.57 ± 0.76 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d8192 | 16.52 ± 0.06 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d16384 | 714.13 ± 1.26 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d16384 | 16.42 ± 0.04 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | pp2048 @ d32768 | 696.00 ± 0.80 |
| nemotron\_h\_moe 120B.A12B MXFP4 MoE | 76.42 GiB | 120.67 B | CUDA | 99 | 2048 | 1 | 0 | tg32 @ d32768 | 16.21 ± 0.04 |

build: [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0) (8580)

```
src/llama-cpp/build/bin/llama-batched-bench -m /home/sparky/.cache/huggingface/hub/models--unsloth--NVIDIA-Nemotron-3-Super-120B-A12B-GGUF/snapshots/036038fb30334a2d56a146c6f0d4871ab5edccbb/MXFP4_MOE/NVIDIA-Nemotron-3-Super-120B-A12B-MXFP4_MOE-00001-of-00003.gguf -fa 1 -c 300000 -ub 2048 -npp 4096,8192 -ntg 32 -npl 1,2,4,8,16,32 --no-mmap
```

ggml\_cuda\_init: found 1 CUDA devices (Total VRAM: 124610 MiB):

Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124610 MiB

build: 8580 ( [`7c20367`](https://github.com/ggml-org/llama.cpp/commit/7c203670f8d746382247ed369fea7fbf10df8ae0)) with GNU 13.3.0 for Linux aarch64

main: n\_kv\_max = 303104, n\_batch = 2048, n\_ubatch = 2048, flash\_attn = 1, is\_pp\_shared = 0, is\_tg\_separate = 0, n\_gpu\_layers = -1, n\_threads = 20, n\_threads\_batch = 20

| PP | TG | B | N\_KV | T\_PP s | S\_PP t/s | T\_TG s | S\_TG t/s | T s | S t/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4096 | 32 | 1 | 4128 | 6.085 | 673.17 | 1.946 | 16.44 | 8.031 | 514.02 |
| 4096 | 32 | 2 | 8256 | 11.325 | 723.34 | 3.034 | 21.10 | 14.359 | 574.97 |
| 4096 | 32 | 4 | 16512 | 22.660 | 723.04 | 5.297 | 24.17 | 27.956 | 590.63 |
| 4096 | 32 | 8 | 33024 | 45.323 | 722.98 | 10.007 | 25.58 | 55.330 | 596.85 |
| 4096 | 32 | 16 | 66048 | 90.703 | 722.53 | 16.937 | 30.23 | 107.641 | 613.60 |
| 4096 | 32 | 32 | 132096 | 181.392 | 722.59 | 31.129 | 32.90 | 212.521 | 621.57 |
| 8192 | 32 | 1 | 8224 | 11.376 | 720.11 | 1.945 | 16.45 | 13.321 | 617.35 |
| 8192 | 32 | 2 | 16448 | 22.715 | 721.27 | 3.043 | 21.03 | 25.758 | 638.55 |
| 8192 | 32 | 4 | 32896 | 45.390 | 721.92 | 5.324 | 24.04 | 50.714 | 648.66 |
| 8192 | 32 | 8 | 65792 | 90.687 | 722.66 | 10.115 | 25.31 | 100.802 | 652.69 |
| 8192 | 32 | 16 | 131584 | 181.414 | 722.50 | 17.170 | 29.82 | 198.584 | 662.61 |
| 8192 | 32 | 32 | 263168 | 362.690 | 722.78 | 31.488 | 32.52 | 394.178 | 667.64 | |

1You must be logged in to vote

👍3

All reactions

- 👍3

0 replies


Comment options

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/ggml-org/llama.cpp/discussions/16578).

# {{title}}

Quote reply

### [![](https://avatars.githubusercontent.com/u/184003273?s=64&v=4)\ dentity007](https://github.com/dentity007) [on Mar 30Mar 31, 2026](https://github.com/ggml-org/llama.cpp/discussions/16578\#discussioncomment-16388381)

|     |
| --- |
| ![Gemini_Generated_Image_6dyvfm6dyvfm6dyv](https://private-user-images.githubusercontent.com/184003273/571641152-f7cac130-8ab4-4c69-a133-31a61d3188b5.jpeg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI3MzU5NDMsIm5iZiI6MTc5MjczNTY0MywicGF0aCI6Ii8xODQwMDMyNzMvNTcxNjQxMTUyLWY3Y2FjMTMwLThhYjQtNGM2OS1hMTMzLTMxYTYxZDMxODhiNS5qcGVnP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MTAyMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjEwMjNUMDYwNzIzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjkxNzhlNWUyNzVkOTQ2YWViMTc1NTYzY2U2NDA5NDZkZTA1Y2RlZDA4NDhjZDYxMGViOTMxMWVmMDVjNzMwMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGanBlZyJ9.uba5oFyF9hKmgBlX4D8pT9pGAvjiI-1f3_2KEKu8g18)<br>Adding KV cache quantization data to this thread. Tested --cache-type-k / --cache-type-v with f16, q8\_0, and q4\_0 on Nemotron 3 Nano 30B A3B (Q4\_K\_XL) at 128K context.<br>Key finding: q4\_0 KV cache has a devastating performance cliff at 64K+ context on Spark. Prompt processing drops 92.5% (282.7 to 21.3 tok/s) due to dequantization overhead. q8\_0 is the sweet spot: 2x compression with under 5% speed hit at all context lengths.<br>Interestingly, q4\_0 uses ~6% MORE RSS than f16 on Spark's unified memory. The per group scale/zero point metadata overhead exceeds the compression savings.<br>Config Context Prompt tps Gen tps RSS<br>f16 ~8K 371.3 14.7 1.25 GB<br>f16 ~32K 328.3 13.5 1.59 GB<br>f16 ~64K 282.7 13.3 1.94 GB<br>q4\_0 ~8K 363.4 14.2 1.34 GB<br>q4\_0 ~32K 316.9 11.0 1.69 GB<br>q4\_0 ~64K 21.3 8.6 2.06 GB<br>Build: b8399, aarch64 + CUDA, GB10 compute 12.1, CUDA 13.0<br>For most Spark workloads, f16 is the right default. 128GB unified memory means there's no KV cache memory pressure to solve. The exception is extreme concurrency or 500K+ context, where q8\_0 makes sense.<br>Full writeup: [https://www.linkedin.com/pulse/i-benchmarked-kv-cache-quantization-my-dgx-spark-heres-nathan-maine-szxtc](https://www.linkedin.com/pulse/i-benchmarked-kv-cache-quantization-my-dgx-spark-heres-nathan-maine-szxtc) |

1You must be logged in to vote

❤️3👀1

All reactions

- ❤️3
- 👀1

0 replies


[Sign up for free](https://github.com/join?source=comment-repo) **to join this conversation on GitHub**.
Already have an account?
[Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fggml-org%2Fllama.cpp%2Fdiscussions%2F16578)

Category


[🙌\\
\\
Show and tell](https://github.com/ggml-org/llama.cpp/discussions/categories/show-and-tell)

Labels


None yet


41 participants


[![@ggerganov](https://avatars.githubusercontent.com/u/1991296?s=48&v=4)](https://github.com/ggerganov) [![@lhl](https://avatars.githubusercontent.com/u/2581?s=48&v=4)](https://github.com/lhl) [![@raphaelamorim](https://avatars.githubusercontent.com/u/85888?s=48&v=4)](https://github.com/raphaelamorim) [![@Slach](https://avatars.githubusercontent.com/u/105560?s=48&v=4)](https://github.com/Slach) [![@gelim](https://avatars.githubusercontent.com/u/179122?s=48&v=4)](https://github.com/gelim) [![@rgerganov](https://avatars.githubusercontent.com/u/271616?s=48&v=4)](https://github.com/rgerganov) [![@slewsys](https://avatars.githubusercontent.com/u/418762?s=48&v=4)](https://github.com/slewsys) [![@geerlingguy](https://avatars.githubusercontent.com/u/481677?s=48&v=4)](https://github.com/geerlingguy) [![@qdrddr](https://avatars.githubusercontent.com/u/564658?s=48&v=4)](https://github.com/qdrddr) [![@mdengler](https://avatars.githubusercontent.com/u/777015?s=48&v=4)](https://github.com/mdengler) [![@jasonburton5](https://avatars.githubusercontent.com/u/1251237?s=48&v=4)](https://github.com/jasonburton5) [![@atsyplikhin](https://avatars.githubusercontent.com/u/1659141?s=48&v=4)](https://github.com/atsyplikhin) [![@bartlettroscoe](https://avatars.githubusercontent.com/u/1959736?s=48&v=4)](https://github.com/bartlettroscoe) [![@eugr](https://avatars.githubusercontent.com/u/2192184?s=48&v=4)](https://github.com/eugr) [![@am17an](https://avatars.githubusercontent.com/u/2929750?s=48&v=4)](https://github.com/am17an) [![@Djip007](https://avatars.githubusercontent.com/u/3705339?s=48&v=4)](https://github.com/Djip007) [![@cody-vibe](https://avatars.githubusercontent.com/u/3746963?s=48&v=4)](https://github.com/cody-vibe) [![@icsy7867](https://avatars.githubusercontent.com/u/3788162?s=48&v=4)](https://github.com/icsy7867) [![@yf225](https://avatars.githubusercontent.com/u/4063635?s=48&v=4)](https://github.com/yf225) [![@letsrock85](https://avatars.githubusercontent.com/u/4653524?s=48&v=4)](https://github.com/letsrock85) [![@spamshaker](https://avatars.githubusercontent.com/u/4864089?s=48&v=4)](https://github.com/spamshaker) and others

Heading

Bold

Italic

Quote

Code

Link

* * *

Numbered list

Unordered list

Task list

* * *

Attach files

Mention

Reference

# Select a reply

Loading

[Create a new saved reply](https://github.com/ggml-org/llama.cpp/discussions/16578)

👍1 reacted with thumbs up emoji👎1 reacted with thumbs down emoji😄1 reacted with laugh emoji🎉1 reacted with hooray emoji😕1 reacted with confused emoji❤️1 reacted with heart emoji🚀1 reacted with rocket emoji👀1 reacted with eyes emoji

You can’t perform that action at this time.