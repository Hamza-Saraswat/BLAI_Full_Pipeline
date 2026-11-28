For the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs.

 [Skip to content](https://unsloth.ai/docs/models/inkling-2-mini#gitbook-main-content)

[Introducing Unsloth Desktop: the first local app to run & train models\\
\\
✨Read more](https://unsloth.ai/docs/desktop)

**Inkling 2 Mini** is Thinking Machines Lab’s **26.4B MoE (5.4B active)** model for coding, agentic, and **vision** workloads. Released under Apache 2.0 and built on a Looped Transformers variant, it has **1M context** and scores **48.2% on DeepSWE v1.1** and **77.9% on SWEBench Pro v2 (Hard)**, making it the strongest for its size, ahead of Qwen3.8-27B. It ties Qwen3.8-27B on Terminal Bench 4.0 at **5.6%**.

This guide covers running Inkling 2 Mini on a Mac, NVIDIA or AMD device with Unsloth Desktop which has [~1.9x faster inference](https://unsloth.ai/docs/models/inkling-2-mini#id-23rd-november-update) for the model.

Run on 16GB RAM or **24GB RAM** for **full precision**. GGUF: [**Inkling 2 Mini GGUF**](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)

[Run Inkling 2 Guide](https://unsloth.ai/docs/models/inkling-2-mini#run-inkling-2-mini-guide) [Download Unsloth](https://unsloth.ai/download)

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fbnhx2GlFHFh3fjMdbN26%252Fgta%2520example.gif%3Falt%3Dmedia%26token%3D6f9605aa-3c77-4796-a014-96214063f1b0&width=768&dpr=3&quality=100&sign=71160c985302d7cb4dc6b79a06b09add&sv=3)

Example of 4-bit Inkling Mini running in Unsloth

Want to train the model? See [Fine-tune Inkling 2 Mini](https://unsloth.ai/docs/models/inkling-2-mini/fine-tuning) for the notebooks, benchmarks, and setup.

### ⚙️ Usage Guide[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#usage-guide)

#### Inkling 2 Mini Requirements[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#inkling-2-mini-requirements)

`UD-Q8_K_XL` is **full precision**. The recommended quant is `UD-Q4_K_XL` **(17.6 GB).**

**Table: Hardware Requirements** (RAM + VRAM, or unified memory)

1-bit

2-bit

3-bit

4-bit

8-bit (Lossless)

9 GB

10-11 GB

13-15 GB

17-18 GB

24 GB

See [Quantization Analysis](https://unsloth.ai/docs/models/inkling-2-mini#quantization-analysis) for all GGUF sizes and results.

Use these ranges as a starting point. Longer contexts, image inputs and other apps can use more memory. The `mmproj-F16.gguf` vision projector adds 639 MB to the download.

#### Recommended Settings[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#recommended-settings)

Temperature

Top-p

Top-k

Min-p

`1.0`

`1.0`

`0`

`0.0`

### 24th November Update[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#id-24th-november-update)

You can now finetune and train Inkling-2-Mini on any local GPU with Unsloth and we provide a free Kaggle 2xT4 notebook for it! We train 1.8 to 3.1x faster than TRL with all optimizations turned on, and use 50% less VRAM. See [Fine-tune Inkling 2 Mini](https://unsloth.ai/docs/models/inkling-2-mini/fine-tuning) for more details

We also fixed and improved Inkling-2-Mini inference speed further and fixed context lengths being priced incorrectly which slowed Inkling-2-Mini in Unsloth Desktop by 2-3x.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F5HICgfWx3ha64hQ4mpVo%252Finkling-2-mini-vs-trl-v2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=648a79fc93d527a7008eb4efde1ad172&sv=3)

### 23rd November Update[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#id-23rd-november-update)

Unsloth is **up to 1.9x faster than mainline llama.cpp** for Inkling-2-Mini inference decoding with some llama.cpp optimizations! We also fixed the Q8\_0 KV cache using more VRAM than F16 issue.

Also all quants are updated so **mainline llama.cpp can load them**! For more information, see: [Inference optimizations](https://unsloth.ai/docs/models/inkling-2-mini#inference-speed)

![Inkling-2-Mini UD-Q4_K_XL decode speed across GPUs: Unsloth llama.cpp prebuilts vs mainline](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fc9IoUVjzX5Khdzy2PKIG%252Finkling2_mini_decode_speed_gpus.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3185d7872d4fb5f480ea193b8bcbfbe6&sv=3)

Decode speed across GPUs: Unsloth prebuilts vs mainline llama.cpp

## Run Inkling 2 Mini Guide[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#run-inkling-2-mini-guide)

Use an Unsloth or llama.cpp build with **looped-layer support** and **per-expert NVFP4 scales**. [Inkling 2 Mini model card](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)

[Run in Unsloth Desktop](https://unsloth.ai/docs/models/inkling-2-mini#run-inkling-2-mini-in-unsloth-desktop) [Run in llama.cpp](https://unsloth.ai/docs/models/inkling-2-mini#run-inkling-2-mini-in-llama-cpp)

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fc9F8coH46gJj7gxZEhRU%252Fsnow-fall.webp%3Falt%3Dmedia%26token%3D2ede2108-5204-405d-9e6a-57d1a903c5f0&width=768&dpr=3&quality=100&sign=2398db40db4510b448dac50be73262e6&sv=3)

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FXRbHGqQn9DJR1prbs4w5%252Flighthouse.webp%3Falt%3Dmedia%26token%3De17bd9b1-d5d4-4659-b532-8373188e3811&width=768&dpr=3&quality=100&sign=edb11bc30a69ce501bcc4cd1ba03705f&sv=3)

### 🦥 Run Inkling 2 Mini in Unsloth Desktop[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#run-inkling-2-mini-in-unsloth-desktop)

1

#### Install Unsloth[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#install-unsloth)

Download and launch the [Unsloth Desktop app](https://unsloth.ai/docs/desktop) for macOS, Windows or Linux.

[Download Unsloth](https://unsloth.ai/download)

- [Download for macOS](https://unsloth.ai/download/mac)

- [Download for Windows](https://unsloth.ai/download/windows)

- [Download for Linux](https://unsloth.ai/download/linux)


Or, if you prefer to install manually:

Native install

Docker

Homebrew

WinGet

**MacOS, Linux, WSL:**

GitBook AssistantAskCopy

```
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows:**

GitBook AssistantAskCopy

```
irm https://unsloth.ai/install.ps1 | iex
```

The [Unsloth Docker image](https://hub.docker.com/r/unsloth/unsloth)`unsloth/unsloth` is available on Docker. [Read guide.](https://unsloth.ai/docs/get-started/install/docker)

Install Unsloth Desktop:

GitBook AssistantAskCopy

```
brew install --cask unsloth
```

Update Unsloth Desktop:

GitBook AssistantAskCopy

```
brew upgrade --cask unsloth
```

Install Unsloth Desktop:

GitBook AssistantAskCopy

```
winget install --id UnslothAI.Unsloth -e
```

Update Unsloth Desktop:

GitBook AssistantAskCopy

```
winget upgrade --id UnslothAI.Unsloth -e
```

2

#### Search and download Inkling 2 Mini[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#search-and-download-inkling-2-mini)

In **Chat**, open **Select model**, or go to **Model hub**. Search for **Inkling 2 Mini**, select [**unsloth/Inkling-2-Mini-GGUF**](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF) and download the quant that fits your device. Once it downloads, select the model in Chat and start a conversation. You can also load a compatible Mini GGUF from your local files.

3

#### Run and Serve Inkling 2 Mini with the Unsloth API[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#run-and-serve-inkling-2-mini-with-the-unsloth-api)

This example uses the 4-bit `UD-Q4_K_XL` quant (17.63 GB). Change the suffix after the colon to select another quant from the repository.

GitBook AssistantAskCopy

```
unsloth run --model unsloth/Inkling-2-Mini-GGUF:UD-Q4_K_XL \
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0
```

Use the endpoint URL and API key printed in the terminal to connect your client. [Unsloth API guide](https://unsloth.ai/docs/basics/api)

### 🦙 Run Inkling 2 Mini in llama.cpp[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#run-inkling-2-mini-in-llama-cpp)

1

#### Install llama.cpp[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#install-llama.cpp)

Unsloth GGUFs now can run in mainline llama.cpp! Our [b12649-mix-c7059d6](https://github.com/unslothai/llama.cpp/releases/tag/b12649-mix-c7059d6) build decodes faster in our benchmarks and supports both DSpark drafter layouts.

Apple

NVIDIA

AMD

Windows

DGX Spark

GitBook AssistantAskCopy

```
curl -L -o llama.tar.gz https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/llama-b12649-mix-c7059d6-bin-macos-arm64.tar.gz
mkdir -p llama.cpp
tar -xzf llama.tar.gz -C llama.cpp --strip-components=1
./llama.cpp/llama-server --version
```

**CUDA 12** build for most NVIDIA GPUs: RTX 20 to RTX 50 series, V100, T4, A100, H100 and B200. Install the [CUDA toolkit](https://developer.nvidia.com/cuda-downloads) first. With CUDA 13, swap `cuda12-portable` for `cuda13-portable`. For GTX 10 series and older, use `cuda12-legacy`.

GitBook AssistantAskCopy

```
curl -L -o llama.tar.gz https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/app-b12649-mix-c7059d6-linux-x64-cuda12-portable.tar.gz
mkdir -p llama.cpp
tar -xzf llama.tar.gz -C llama.cpp
./llama.cpp/llama-server --version
```

**ROCm** build for Radeon RX 9000 (`gfx120X`). It bundles the ROCm libraries, so a full ROCm install is not needed. For other GPUs, swap `gfx120X` for `gfx1151` (Ryzen AI Max), `gfx1150` (Ryzen AI 300), `gfx110X` (RX 7000), `gfx103X` (RX 6000), `gfx90a` (MI200) or `gfx908` (MI100). For any other AMD GPU, use the `vulkan` build.

GitBook AssistantAskCopy

```
curl -L -o llama.tar.gz https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/app-b12649-mix-c7059d6-linux-x64-rocm-gfx120X.tar.gz
mkdir -p llama.cpp
tar -xzf llama.tar.gz -C llama.cpp
./llama.cpp/llama-server --version
```

**CUDA 12** build for NVIDIA GPUs. Install the [CUDA toolkit](https://developer.nvidia.com/cuda-downloads) first, then run these in PowerShell. With CUDA 13, swap `cuda12-portable` for `cuda13-portable`. For AMD, swap it for `rocm-gfx120X` or your GPU's build from the AMD tab. Use `vulkan` for other GPUs or `cpu` for CPU only.

GitBook AssistantAskCopy

```
curl.exe -L -o llama.zip https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/app-b12649-mix-c7059d6-windows-x64-cuda12-portable.zip
Expand-Archive llama.zip -DestinationPath llama.cpp
.\llama.cpp\llama-server.exe --version
```

GitBook AssistantAskCopy

```
curl -L -o llama.tar.gz https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/app-b12649-mix-c7059d6-linux-arm64-cuda13-portable.tar.gz
mkdir -p llama.cpp
tar -xzf llama.tar.gz -C llama.cpp
./llama.cpp/llama-server --version
```

For Intel Macs, CPU-only, Vulkan or Linux ARM64, pick the matching file from the [release page](https://github.com/unslothai/llama.cpp/releases/tag/b12649-mix-c7059d6). Keep `llama-server` and its bundled libraries together in `llama.cpp`.

You can also build llama.cpp from source:

GitBook AssistantAskCopy

```
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev git -y
git clone https://github.com/ggml-org/llama.cpp
git -C llama.cpp fetch origin pull/30817/head:deepseek41
git -C llama.cpp checkout deepseek41
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2

#### Download the GGUF[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#download-the-gguf)

Download the 4-bit `UD-Q4_K_XL` GGUF, the F16 vision projector and the Q8\_0 DSpark drafter. For another quant, use its filename from the repository. [GGUF files](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF/tree/main)

GitBook AssistantAskCopy

```
pip install -U huggingface_hub
hf download unsloth/Inkling-2-Mini-GGUF \
    Inkling-2-Mini-UD-Q4_K_XL.gguf mmproj-F16.gguf \
    dspark-Inkling-2-Mini-Q8_0.gguf \
    --local-dir Inkling-2-Mini-GGUF
```

3

#### Run Inkling 2 Mini[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#run-inkling-2-mini)

Start the local chat server with the prebuilt binary.

macOS, Linux or WSL

Windows PowerShell

GitBook AssistantAskCopy

```
./llama.cpp/llama-server \
    --model Inkling-2-Mini-GGUF/Inkling-2-Mini-UD-Q4_K_XL.gguf \
    --mmproj Inkling-2-Mini-GGUF/mmproj-F16.gguf \
    --model-draft Inkling-2-Mini-GGUF/dspark-Inkling-2-Mini-Q8_0.gguf \
    --spec-type draft-dspark --spec-draft-n-max 2 --n-gpu-layers-draft 99 \
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \
    --host 127.0.0.1 --port 8080
```

GitBook AssistantAskCopy

```
.\llama.cpp\llama-server.exe `
    --model Inkling-2-Mini-GGUF/Inkling-2-Mini-UD-Q4_K_XL.gguf `
    --mmproj Inkling-2-Mini-GGUF/mmproj-F16.gguf `
    --model-draft Inkling-2-Mini-GGUF/dspark-Inkling-2-Mini-Q8_0.gguf `
    --spec-type draft-dspark --spec-draft-n-max 2 --n-gpu-layers-draft 99 `
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 `
    --host 127.0.0.1 --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080/) to chat or upload an image. The `--model-draft` and `--spec-type draft-dspark` flags turn on DSpark speculative decoding with the 0.4 GB drafter, and `--spec-draft-n-max 2` is the fastest depth for Inkling 2 on this build (the third draft token is rarely accepted).

To run without it, drop the drafter from the download and the `--model-draft` and `--spec-type` lines from the server command. For text-only chat, omit the projector from the download and drop `--mmproj` from the server command. If memory is limited, reduce `--ctx-size` or `--n-gpu-layers`. For CPU-only inference, set `--n-gpu-layers 0` and `--n-gpu-layers-draft 0`.

### ⏯️ Looped transformer architecture[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#looped-transformer-architecture)

Inkling-2-Mini uses a modified looped transformer architecture where layers 6-17 are looped 3 times and if we combine this with embeddings, only 5.4B gets activated. This is different from other LLM architectures where each decoder layer is only run once - Inkling-2-Mini essentially runs layers 6 to 17 three times, effectively compressing its disk space and footprint during the training process.

It is **rumored** that the GPT-6 Astra class of models might also employ a variant of the looped transformer architecture as well, and Inkling-2-Mini is the one of the first powerful open models to employ a variant of this mechanism.

### 📊 Quantization Analysis[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#quantization-analysis)

We compare each GGUF with `UD-Q8_K_XL` across seven domains using identical llama.cpp settings. The reference keeps the original NVFP4 expert weights and stores the remaining weights in BF16. UD-Q4\_K\_XL is also nearly lossless with MXFP8 weights dequantized to Q8\_0. UD-Q8\_K\_XL upcasts MXFP8 to BF16 so KLD = 0.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FqWPOI9paCJed36b9qV1x%252Fsize_vs_top1%287%29.png%3Falt%3Dmedia%26token%3D186fd174-4199-4d66-949e-fc851aa614ef&width=768&dpr=3&quality=100&sign=f9b521abfebbfda0c563a92986c0d1a8&sv=3)

The 4-bit `UD-Q4_K_XL` gets **0.0107 mean KLD** and **98.0% top-token agreement** at **17.63 GB**. The 2-bit `UD-IQ2_XXS` brings the download down to **8.49 GB** with **90.6% agreement**.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FObpB27Pzg7eddzGOefoK%252Fsize_vs_kld%284%29.png%3Falt%3Dmedia%26token%3Db388d982-caaa-402f-bc8f-f49938036713&width=768&dpr=3&quality=100&sign=09a9dd9e309266eb15888aa475a14c87&sv=3)

Click to view full quantization table [Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini#click-to-view-full-quantization-table)

Quant

Size (GB)

Mean KLD vs UD-Q8\_K\_XL

Same top token

UD-IQ1\_S

7.76

0.0911

89.4%

UD-IQ1\_M

8.02

0.0867

90.2%

UD-IQ2\_XXS

8.49

0.0726

90.6%

UD-Q2\_K\_XL

9.14

0.0595

91.6%

UD-IQ3\_XXS

11.66

0.0269

94.7%

UD-Q3\_K\_XL

13.63

0.0174

96.3%

UD-IQ4\_XS

15.73

0.0109

97.7%

UD-Q4\_K\_M

16.61

0.0108

97.9%

UD-Q4\_K\_XL

17.63

0.0107

98.0%

UD-Q8\_K\_XL

22.87

reference

### 🚀Inference optimizations[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#inference-speed)

Unsloth is **up to 1.9x faster than mainline llama.cpp** for Inkling-2-Mini inference decoding with some llama.cpp optimizations! We measured decode speed (`tg1024`, 1024 generated tokens) for `UD-Q4_K_XL` with an F16 KV cache across four llama.cpp builds: our previous prebuilt ([b12588-mix-c0c3de8](https://github.com/unslothai/llama.cpp/releases/tag/b12588-mix-c0c3de8)), our b12631 prebuilt ([b12631-mix-acc0843](https://github.com/unslothai/llama.cpp/releases/tag/b12631-mix-acc0843)), an Unsloth's latest llama.cpp build vs mainline llama.cpp b12649 and Strata. We also fixed Q4\_0 / Q8\_0 etc using more memory than F16 by supporting banded attention in flash attention for other precisions.

![Inkling-2-Mini UD-Q4_K_XL decode speed across GPUs: Unsloth llama.cpp prebuilts vs mainline](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fc9IoUVjzX5Khdzy2PKIG%252Finkling2_mini_decode_speed_gpus.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3185d7872d4fb5f480ea193b8bcbfbe6&sv=3)

Decode speed across GPUs: Unsloth prebuilts vs mainline llama.cpp

GPU (tokens/s)

Previous b12588

b12631

New Unsloth

Mainline b12649

New vs mainline

NVIDIA B200

68.88

85.08

**110.77**

68.00

**1.63x**

NVIDIA RTX PRO 6000 Blackwell

81.71

101.11

**125.24**

81.35

**1.54x**

NVIDIA A100 40GB

45.11

54.17

**67.02**

45.02

**1.49x**

NVIDIA L4

36.23

39.09

**42.88**

35.84

**1.20x**

NVIDIA T4 (5 MoE layers on CPU)

19.68

21.71

**23.90**

19.71

**1.21x**

AMD Ryzen AI Max (gfx1151), Linux

24.40

27.58

**32.78**

24.15

**1.36x**

AMD Ryzen AI Max (gfx1151), Windows

16.62

**25.65**

not measured

13.74

1.87x (b12631)

- A Q8\_0 KV cache (`--cache-type-k q8_0 --cache-type-v q8_0`) costs about 3% to 7% decode speed on the candidate (B200: 103.06 vs 110.77 tokens/s) and keeps the same ordering between builds - but you get 2x more context length!

- `UD-Q2_K_XL` follows the same pattern. On B200 with F16 KV: previous 69.67, current 86.65, new 113.90, mainline 69.31 tokens/s. On T4 it fits fully on the GPU: 25.64, 28.54, 31.45 and 25.73 tokens/s.


#### DSpark speculative decoding[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#dspark-speculative-decoding)

Dspark does help improve generation speed, and our new build also gets faster combined with Dspark:

![Inkling-2-Mini DSpark speculative decoding speed on B200](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F6zL3VlE7TyV0Wo0We1Xt%252Finkling2_mini_dspark_speed.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=478c9b2dc9ff7c6ea415de08310b8e59&sv=3)

DSpark speculative decoding on B200

Sampling

b12631, no drafter

b12631 + DSpark

New, no drafter

New + DSpark

Greedy

77.5

96.1 (1.24x)

99.9

**117.3** (1.17x)

Temperature 1.0

69.8

79.0 (1.13x)

86.9

**96.6** (1.11x)

We did see that a depth of 2 using our old drafter was faster on average than llama.cpp's current dspark implementation, so in unsloth, we default to the old dspark module. The new dspark should use a depth of 3.

Drafter

Depth 2

Depth 3

Depth 4

Depth 5

Padded-vocab drafter

**1.24x / 1.15x**

1.24x / 1.10x

-

-

`Mainline_Support` drafter

1.09x / 1.03x

1.16x / 1.03x

1.12x / 1.03x

1.04x / 0.97x

#### Comparison with Strata[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#comparison-with-strata)

We benchmarked Strata on B200 (`tg1024`, DSpark off), in tokens/s of running our quants:

![Inkling-2-Mini decode speed on B200: Unsloth llama.cpp vs Strata](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FD0cFDouVjxtmuuI0jFTz%252Finkling2_mini_strata_speed.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4b27e2a7a692cda11dbb70e9e6968019&sv=3)

Unsloth llama.cpp vs Strata on B200

GGUF

KV cache

Strata

b12631

New Unsloth

UD-Q4\_K\_XL

F16

105.2

84.2

**111.8**

UD-Q4\_K\_XL

Q8\_0

**107.1**

80.3

101.4

UD-Q2\_K\_XL

F16

105.4

85.6

**113.5**

UD-Q2\_K\_XL

Q8\_0

**105.2**

82.6

103.9

UD-Q4\_K\_XL, server

F16

**110.4**

81.5

102.4

Unsloth is generally faster or on par with Strata when running Inkling-2-Mini for decode speed. Also Strata does not run the our GGUF weights as stored - at load time it repacks `UD-Q4_K_XL` to NVFP4 and `UD-Q2_K_XL` to IQ1\_S, so it is not running the same quantization.

### 📊 Benchmarks[Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini\#benchmarks)

In Thinking Machines Lab’s evaluations, Mini leads the three similarly sized models below on the listed software engineering and search benchmarks. Mini scores **6.0 percentage points higher than Qwen3.8-27B on DeepSWE v1.1** and **4.1 points higher on SWEBench Pro v2 (Hard)**.

Click to view full benchmark table [Direct link to heading](https://unsloth.ai/docs/models/inkling-2-mini#click-to-view-full-benchmark-table)

Benchmark

Inkling 2 Mini

Gemma 4 31B

Muse Glimmer

Qwen3.8-27B

Nemotron 3.5 Super VL

Parameters (active / total B)

5 / 26

31 / 31

30 / 30

27 / 27

12 / 125

SWE-bench Verified

**79.2%**

46.1%

76.0%

77.8%

71.1%

DeepSWE v1.1

**48.2%**

0.3%

4.4%

42.2%

24.7%

Terminal Bench v4.0

**5.6%**

0.0%

0.5%

**5.6%**

0.0%

AA Index v5.0

**20.1**

4.4

6.3

**20.1**

13.6

Vals Index v2.2

**46.5%**

–

–

–

29.8%

SWE-bench Pro (Hard)

**77.9%**

14.2%

44.3%

73.8%

44.1%

Terminal Bench v2.1

71.6%

43.4%

51.7%

**73.0%**

60.7%

BrowseComp

**79.0%**

37.0%

63.9%

61.6%

78.9%

DeepSearchQA

**85.3%**

61.7%

74.6%

79.7%

77.7%

GDPVal-AA v2.1

1319

627

792

**1427**

1162

AutomationBench-AA

41.8%

4.9%

6.8%

**48.2%**

14.8%

JobBench

**49.6%**

8.2%

16.1%

33.4%

36.5%

MMMU Pro

74.9%

73.4%

74.3%

**76.3%**

72.3%

OmniDocBench v1.6

**92.8%**

82.5%

90.4%

91.5%

77.9%

ScreenSpot Pro (original / Python)

**76.5 / 87.7%**

5.9 / –

75.4 / –

57.6 / 78.9%

43.5 / –

Chartography (original / Python)

**22.1 / 72.5%**

12.0 / 11.8%

17.4 / 25.1%

12.2 / 52.1%

9.7 / 29.3%

HLE-Diamond

15.2%

7.2%

9.1%

**15.3%**

8.8%

ARC-AGI (v1 / v2)

**84.5 / 49.3%**

–

–

87.5 / 42.4%

22.7 / 1.5%

LongBench v2

**66.9%**

52.9%

33.1%

52.3%

62.1%

AA-Omniscience (score)

-8.6

-48.5

-32.2

-6.4

**-2.9**

AA-Omniscience (non-hallucination)

63.4%

14.5%

16.4%

**71.4%**

69.5%

FORTRESS (adversarial)

89.5%

67.8%

**90.3%**

78.8%

79.6%

FORTRESS (benign)

96.4%

97.6%

89.1%

**97.8%**

92.7%

StrongREJECT

97.8%

98.1%

99.0%

99.0%

**99.4%**

[PreviousSandboxing in Unsloth](https://unsloth.ai/docs/new/studio/sandboxing-in-unsloth) [NextFine-tune Inkling 2 Mini](https://unsloth.ai/docs/models/inkling-2-mini/fine-tuning)

Last updated 2 days ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject