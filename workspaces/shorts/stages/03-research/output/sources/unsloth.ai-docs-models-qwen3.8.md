# URL: https://unsloth.ai/docs/models/qwen3.8
[Introducing Unsloth Desktop: the first local app to run & train models\\
\\
✨Read more](https://unsloth.ai/docs/desktop)

For the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). This page is also available as [Markdown](https://unsloth.ai/docs/models/qwen3.8.md).

Qwen3.8 is Qwen’s new model family, featuring Qwen3.8- **27B**, Qwen3.8- **2.4T-A95B** and Qwen3.8- **Max**. Qwen3.8-27B has **vision** and reasoning capabilities, a **256K context** window, and runs locally on **17GB RAM/VRAM** setups. Qwen3.8 excels at agentic coding, vision and chat tasks, and can now run via Unsloth GGUFs, NVFP4 and [Unsloth Desktop](https://unsloth.ai/docs/models/qwen3.8#run-qwen3.8-in-unsloth-desktop). Qwen3.8-2.4T-A95B is a 2.4T parameter (95B active) model with rivaling GPT-5.6 Sol.

**Aug 19 Update:** Qwen3.8-27B GGUFs now use [Unsloth Dynamic V3.0](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) for 10% more accuracy at the same size, largely outperforming others.

[Run Qwen3.8 Guide](https://unsloth.ai/docs/models/qwen3.8#run-qwen3.8-guide) [Download Unsloth](https://unsloth.ai/download)

Thank you Qwen for day zero access. Unsloth quants also include:

- **Developer Role Support** for agentic tools like Codex

- [MTP enabled](https://unsloth.ai/docs/models/mtp) for fast inference

- **Tool calling:** Improved parsing nested objects to make tools succeed more


Full-precision Qwen3.8-2.4T-A95B requires 4.9TB of storage and 1-bit [Unsloth](https://github.com/unslothai/unsloth) Dynamic GGUFs takes **397GB (91% smaller)**, and larger IQ1\_S takes 508GB.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F6aw6IjO7lnYJhSyzXYwq%252Fvolcano%2520qwen.gif%3Falt%3Dmedia%26token%3D94e56117-d10d-45e8-82dc-3e134b2b9359&width=768&dpr=3&quality=100&sign=a26de084e3490bbe639a061a042cfbb1&sv=3)

Dynamic 4-bit Qwen3.8-27B in Unsloth Desktop

Unsloth quants:

- [Qwen3.8- **27B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)

- [Qwen3.8-27B- **NVFP4**](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4)


### ⚙️ Usage Guide[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#usage-guide)

#### Qwen3.8-27B Requirements:[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#qwen3.8-27b-requirements)

Qwen3.8- **27B** 4-bit quants work on 16-19GB VRAM like RTX 5080, 4090 or a Mac with 24GB RAM.
**Table: Hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

1-bit

2-bit

3-bit

4-bit

6-bit

8-bit

BF16

7-8 GB

9-11 GB

12-14 GB

16-19 GB

23-26 GB

31 GB

56 GB

If you want to use [MTP](https://unsloth.ai/docs/models/mtp) for faster inference, prepare to have 1-2GB extra headroom.

#### Qwen3.8- **2.4T** Requirements:[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#qwen3.8-2.4t-requirements)

- [Qwen3.8- **2.4T-A95B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF)


Dynamic 1-bit XXXS

Dynamic 1-bit Standard

Dynamic 2-bit

Q8\_0

BF16 (Lossless)

397GB

508GB

657 GB

2.6 TB

4.9 TB

### Recommended Settings[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#recommended-settings)

#### Qwen3.8- **27B Settings:**[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#qwen3.8-27b-settings)

Qwen3.8-27B is a **hybrid thinking** model with different default settings for thinking and non-thinking modes. Extra high is enabled by default so if you want shorter thinking traces, you can [adjust the thinking effort](https://unsloth.ai/docs/models/qwen3.8#thinking--preserve-thinking):

Parameter

Thinking Mode

Instruct (non-thinking) Mode

`temperature`

1.0

0.7

`top_p`

0.95

0.80

`top_k`

20

20

`min_p`

0.0

0.0

`presence_penalty`

0.0

1.5

`repetition_penalty`

1.0

1.0

- **Maximum context window:**`262,144` (can be extended to 1M via YaRN)

- Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`

- Instruct (or non-thinking) mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`


#### Qwen3.8- **2.4T Settings:**[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#qwen3.8-2.4t-settings)

Qwen3.8-2.4T is **thinking-only**, while Qwen3.8-Max is hybrid.

Default

temperature = 1.0

top\_p = 0.95

top\_k = 20

min\_p = 0.0

presence\_penalty = 0.0

- Context length = up to `1,010,000`

- `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`


If the model fits, you will get ~20 tokens/s generation when using B200s and >120 tokens / s throughput. Best rule of thumb: RAM+VRAM ≈ the quant size; otherwise it’ll still work, just much slower due to disk offloading.

### 💡 Thinking + Preserve Thinking[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#thinking--preserve-thinking)

Qwen3.8 has **Preserve Thinking** which leaves the thinking trace from the previous conversation. This increases the number of tokens you use, but could increase accuracy in continued conversations. [Unsloth](https://unsloth.ai/docs/models/qwen3.8#run-qwen3.8-in-unsloth-desktop) has 'Think' and Preserved Thinking toggles for Qwen3.8 (see right):

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FLdgmjRrb5qhpbY9PwYe8%252FScreenshot%25202026-08-14%2520at%252011.26.15%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3D6333f5ca-196d-46ae-9efd-2e522014e6db&width=768&dpr=3&quality=100&sign=cbe50d179bbbfdbe8b85df8cf0bd326b&sv=3)

Qwen3.8-27B comes with support for `reasoning_effort`, which can be used to adjust reasoning depth and control cost. These toggles are automatically enabled in Unsloth:

- `xhigh` (default): for complex tasks demanding thorough analysis

- `medium`: balancing accuracy and speed

- `low`: efficient reasoning optimizing for speed and cost

- none


To change[thinking / reasoning](https://unsloth.ai/docs/models/qwen3.8#how-to-enable-or-disable-reasoning-and-thinking) effort in `unsloth run` or `llama-server`, use `--chat-template-kwargs '{"reasoning_effort":"medium"}'`

If you're on **Windows** Powershell, use: `--chat-template-kwargs "{\"reasoning_effort\":\"medium\"}"`

Change `medium` to your desired reasoning level.

## Run Qwen3.8 Guide[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#run-qwen3.8-guide)

You can now run Qwen3.8 in llama.cpp and Unsloth Desktop. For the large Qwen3.8-2.T model, we will be utilizing the 397GB `IQ1_XXXS` quant (named Q1\_0) for best results in terms of accessibility and accuracy and it will require at least 450GB RAM. Feel free to change quantization type.

- Hugging Face: [Qwen3.8-27B- **GGUF**](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)• [Qwen3.8-27B- **NVFP4**](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4)

- ModelScope: [Qwen3.8-27B- **GGUF**](https://www.modelscope.cn/models/unsloth/Qwen3.8-27B-GGUF)• [Qwen3.8-27B- **NVFP4**](https://www.modelscope.cn/models/unsloth/Qwen3.8-27B-NVFP4)

- **2.4T-A95B:** [Qwen3.8- **2.4T-A95B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF)


[Run in Unsloth Desktop](https://unsloth.ai/docs/models/qwen3.8#run-qwen3.8-in-unsloth-desktop) [Run in llama.cpp](https://unsloth.ai/docs/models/qwen3.8#run-qwen3.8-in-llama.cpp) [NVFP4 Guide](https://unsloth.ai/docs/models/qwen3.8#run-qwen3.8-in-llama.cpp)

### 🦥 Run Qwen3.8 in Unsloth Desktop[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#run-qwen3.8-in-unsloth-desktop)

Qwen3.8 can run in [Unsloth Desktop](https://unsloth.ai/docs/models/qwen3.8#run-qwen3.8-in-unsloth-desktop), an open-source UI app for local AI. **Unsloth automatically offloads to RAM and detects multiGPU setups**. With Unsloth Desktop, you can run models locally on **MacOS, Windows**, Linux and:

- Search, download, [run GGUFs](https://unsloth.ai/docs/new/studio#run-models-locally), MLX and safetensor models

- [**Self-healing** tool calling](https://unsloth.ai/docs/new/studio/chat#auto-healing-tool-calling) \+ **web search**

- [**Code execution**](https://unsloth.ai/docs/desktop#code-execution) (Python, Bash)

- [Automatic inference](https://unsloth.ai/docs/desktop#feature-deep-dive) parameter tuning (temp, top-p, etc.)

- Fast CPU + GPU inference via MLX and llama.cpp

- [Train LLMs](https://unsloth.ai/docs/new/studio#no-code-training) 2x faster with 70% less VRAM


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F6IXaXdTVyvbrnjehlxys%252Fkimik3.gif%3Falt%3Dmedia%26token%3D31e1213b-d7da-46e9-bc7f-3a8c402513fc&width=768&dpr=3&quality=100&sign=a1fbe160e02666b6ff3661645bb16add&sv=3)

1

#### Install Unsloth[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#install-unsloth)

The easiest way to get started is by downloading the [Unsloth Desktop app](https://unsloth.ai/docs/desktop). Works on [macOS](https://unsloth.ai/docs/get-started/install/mac), [Windows](https://unsloth.ai/docs/get-started/install/windows-installation), and [Linux](https://unsloth.ai/docs/get-started/install/linux).

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

#### Search and download Qwen3.8[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#search-and-download-qwen3.8)

Go to [Unsloth Chat](https://unsloth.ai/docs/new/studio/chat) or Model hub and search for Qwen3.8 in the search bar and download your desired model and quant.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fo53hIyoFypinWWLa1c0x%252FScreenshot%25202026-08-14%2520at%252012.42.38%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Da69de985-56ee-4ef3-8e10-f669cc168346&width=768&dpr=3&quality=100&sign=3eb059ca75af7c8bb57f0ea0b72bd26c&sv=3)

3

#### Run Qwen3.8[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#run-qwen3.8)

Inference parameters should be auto-set when using Unsloth, however you can still change it manually. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth inference guide](https://unsloth.ai/docs/new/studio/chat).

For example using Unsloth Desktop with the 397GB Qwen3.8 (-91% smaller) allows you to toggle thinking modes, allow inline canvas, web search and code execution and much more.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fb3IiYJzHzsp2698xTim4%252Fgiffyy%2520gf.gif%3Falt%3Dmedia%26token%3Df1bda1a1-b81f-43e2-ba10-dbdc9a29c0c0&width=768&dpr=3&quality=100&sign=ff495189fe708312b38633ae46419c12&sv=3)

Dynamic 1-bit 397GB 91% smaller GGUF of Qwen3.8 2.4T in Unsloth Desktop

4

#### Serve Qwen3.8 with Unsloth API[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#serve-qwen3.8-with-unsloth-api)

You can use `unsloth run` command and serve Qwen3.8 via an API using `llama-server` runtime flags, including context sizing, GPU layers, threading, sampling, networking, and tool configuration. For more info see our [API docs](https://unsloth.ai/docs/basics/api) or [unsloth start](https://unsloth.ai/docs/integrations/unsloth-start).

GitBook AssistantAskCopy

```
unsloth run --model unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0 \
    --reasoning-effort medium
```

5

#### Unsloth is now ready[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#unsloth-is-now-ready)

You can also do many other things with Qwen3.8 via Unsloth Desktop like:

- **Connect tools:** [Claude Code](https://unsloth.ai/docs/basics/claude-code), [Codex](https://unsloth.ai/docs/basics/codex), [web search](https://unsloth.ai/docs/new/studio/chat#advanced-web-search), [MCP](https://unsloth.ai/docs/basics/mcp) and more

- **Train models:** Fine-tune text, diffusion, [embedding](https://unsloth.ai/docs/basics/embedding-finetuning), and more

- **Generate media:** Create and train [images](https://unsloth.ai/docs/basics/diffusion-image), video, [TTS](https://unsloth.ai/docs/basics/text-to-speech-tts-fine-tuning) locally


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FYShiiub5gs5pCQLX6d4U%252FScreenshot%25202026-08-15%2520at%252012.18.24%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Dd6996797-a144-4113-b4c3-155cca6c39a0&width=768&dpr=3&quality=100&sign=3f9d1a85dc56321d5075ed1983939d5f&sv=3)

### Qwen3.8-2.4T-A95B New 1-bit data-types[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#qwen3.8-2.4t-a95b-new-1-bit-data-types)

We extended IQ1\_S in llama.cpp which is 1.5625 bits per weight to 1.1875 bpw by reducing the number of entries in the codebook - we found this works well for large models, and can still retain a lot of accuracy - we also found these new data-types to be fine for post training quantization (PTQ) without the need for QAT or QAD (quantization aware training / distillation). [Qwen3.8- **2.4T-A95B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF)

Due to naming issues, we used TQ2\_0, TQ1\_0 and Q1\_0 otherwise it won't pop up in the HF repo.

Dtype

Naming

BPW

\# entries

Index bits

Block

IQ1\_S

IQ1\_S

**1.5625**

2048

11

50 B

UD-IQ1\_XS

TQ2\_0

1.4375

1024

10

46 B

UD-IQ1\_XXS

TQ1\_0

1.3125

512

9

42 B

UD-IQ1\_XXXS

Q1\_0

**1.1875**

256

8

38 B

We are still running benchmarks for the new data-types, but for other large models, we get **good results without any QAT / QAD**:

Dtype

GiB

PPL

KLD

top-p

IQ1\_S

553.204

2.578876

0.564553

78.882

UD-IQ1\_XS

513.583

2.931261

0.690161

75.726

UD-IQ1\_XXS

473.961

3.540383

0.876007

71.284

UD-IQ1\_XXXS

434.340

4.488796

1.109944

66.257

### 🦙 Run Qwen3.8 in llama.cpp[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#run-qwen3.8-in-llama.cpp)

1

We need to use the specific IQ1\_XXXS branch [here](https://github.com/unslothai/llama.cpp/pull/61). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

GitBook AssistantAskCopy

```
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone --branch iq1-narrow https://github.com/unslothai/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2

If you just want to run the standard `IQ1_S` and other quants, then compile llama.cpp normally:

GitBook AssistantAskCopy

```
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

3

Download the model via (after installing `pip install huggingface_hub`). You can choose `Q1_0` for `IQ1_XXXS` or other quantized versions like `Q8_0` . If downloads get stuck, see: [Hugging Face Hub, XET debugging](https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging)

**Qwen3.8-27B:**

GitBook AssistantAskCopy

```
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-27B-GGUF \
    --local-dir unsloth/Qwen3.8-27B-GGUF \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q3_K_XL*" for 3-bit
```

**Qwen3.8-2.4T:**

GitBook AssistantAskCopy

```
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --local-dir unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --include "*Q1_0*" # Use "*IQ2_XXS*" for 2-bit
```

4

To run the model in llama-cli, follow the code snippets below:
Remember to [change settings](https://unsloth.ai/docs/models/qwen3.8#recommended-settings) according to your use-case.

**Qwen3.8-27B:**

GitBook AssistantAskCopy

```
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-27B-GGUF/Qwen3.8-27B-UD-Q4_K_XL.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

**Qwen3.8-2.4T:**

GitBook AssistantAskCopy

```
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-2.4T-A95B-GGUF/UD-Q1_0/Qwen3.8-2.4T-A95B-UD-Q1_0-00001-of-00010.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

5

To run the general UD-IQ1\_S you can do:

**Qwen3.8-2.4T:**

GitBook AssistantAskCopy

```
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --local-dir unsloth/Qwen3.8-2.4T-A95B-GGFF \
    --include "*IQ1_S*" # Use "*IQ2_XXS*" for 2-bit
```

6

Then to run it:

GitBook AssistantAskCopy

```
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-2.4T-A95B-GGUF/UD-IQ1_S/Qwen3.8-2.4T-A95B-UD-IQ1_S-00001-of-00012.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

### ⚡️NVFP4[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#nvfp4)

Like Qwen3.6, we’re also releasing new [dynamic NVFP4 Qwen3.8](https://unsloth.ai/docs/basics/nvfp4)-27B quants that run **~1.5× faster** than BF16 checkpoints, with **better performance** and comparable file sizes. Run Qwen3.8-27B NVFP4 **1.5x faster** on **24GB VRAM.** We also added **FP8 KV cache calibration** for 2x longer context lengths! NVFP4 requires NVIDIA's Blackwell GPUs like RTX 50X, DGX Spark (see [Qwen3.8-27B](https://unsloth.ai/docs/models/qwen3.8#dgx-spark-with-nvfp4-quants)), B200, B300 GPUs. For older GPUs, our GGUFs work well! You can run NVFP4 quants in [vLLM](https://unsloth.ai/docs/models/qwen3.8#vllm) only for now (SGLang is not supported).

- [Qwen3.8-27B- **NVFP4**](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4)quant


batch

BF16 total tok/s

NVFP4 total tok/s

speedup

BF16 per-user

NVFP4 per-user

1

89.8

**133.7**

1.49x

89.8

**133.7**

8

649.4

**938.8**

1.45x

81.2

**117.3**

32

1983.0

**2787.0**

1.41x

62.0

**87.1**

64

3048.5

**4407.2**

1.45x

47.6

**68.9**

See below for previous benchmarks conducted for Qwen3.6 as well comparing to other NVFP4 implementations which use 16bit activations vs our NVFP4 activations:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F8zM7cg0Xgo2pAlop1iPW%252F01_qwen36_combined_throughput.png%3Falt%3Dmedia%26token%3D23131a96-4c41-42d7-aa16-5bfb21bb44a3&width=768&dpr=3&quality=100&sign=9583bd271a17702a070557a0de23b576&sv=3)

All benchmarks use 1x B200 128 concurrency. Higher concurrency can boost 35B to 17,561 tokens / s.

For accuracy benchmarks we ran KLD and Top-1 agreement over Code, Chat and many domains. NVFP4 is consistency 92% to 97% accuracy recovery vs BF16

corpus

KLD mean

top-1 agreement

zh

0.01628

93.55%

code

0.02600

96.68%

refgen

0.03993

94.46%

chat

0.05818

92.15%

ja / ko / ru / es

0.0124-0.0155

94-95%

For accuracy benchmarks For Qwen 3.6, we conducted MMLU-Pro, AIME 2025, GPQA for FP8, BF16, NVIDIA's NVFP4 and our NVFP4s - we show our faster quants do similarly on all:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FFhOUUUlRBj3dafGnmvhK%252F03_qwen36_combined_accuracy%287%29.png%3Falt%3Dmedia%26token%3D9178447f-d5ae-4489-9bdc-73b2b7b1631b&width=768&dpr=3&quality=100&sign=e79034ef21499e1332ea0e9e33ef62bc&sv=3)

For more information, you can read our [Dynamic NVFP4 quants blog](https://unsloth.ai/docs/basics/nvfp4).

To run NVFP4 quants, see below for commands to run Qwen3.8-27B in [vLLM](https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide) or [SGLang](https://unsloth.ai/docs/basics/inference-and-deployment/sglang-guide):

#### **vLLM:**[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#vllm)

To install vLLM in a separate venv:

GitBook AssistantAskCopy

```
uv venv unsloth-nvfp4-env --python 3.13
source unsloth-nvfp4-env/bin/activate
uv pip install "vllm>=0.25.0" "flashinfer-python>=0.6.13" "nvidia-cutlass-dsl>=4.5.2" \
    --torch-backend=auto
```

Then to serve the 27B variant:

GitBook AssistantAskCopy

```
vllm serve unsloth/Qwen3.8-27B-NVFP4
```

To enable MTP / speculative decoding (faster decode but somewhat less throughput), use:

GitBook AssistantAskCopy

```
vllm serve unsloth/Qwen3.8-27B-NVFP4
    --speculative-config '{"method": "mtp", "num_speculative_tokens": 2}'
```

If you get Torchcodec issues, be sure to do the below then relaunch vllm.

GitBook AssistantAskCopy

```
sudo apt-get update
sudo apt-get install -y ffmpeg
```

#### **SGLang:**[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#sglang)

If using SGLang, you must use **SGLang version v0.5.19** otherwise it will not work since we quantize the lm\_head to FP8.

vLLM has a `CompressedTensorsW8A8Fp8` kernel which supports this, whilst SGLang v0.5.19 cannot load the FP8 lm\_head. v0.5.19 works now!

For sglang after installing the latest:

GitBook AssistantAskCopy

```
uv pip install sglang sglang-kernel \
  --extra-index-url https://sgl-project.github.io/whl/cu130/ \
  --extra-index-url https://download.pytorch.org/whl/cu130 \
  --index-strategy unsafe-best-match
```

You can then serve it:

GitBook AssistantAskCopy

```
sglang serve unsloth/Qwen3.8-27B-NVFP4
```

To enable MTP, use:

GitBook AssistantAskCopy

```
sglang serve unsloth/Qwen3.8-27B-NVFP4 --speculative-algorithm EAGLE \
    --speculative-num-steps 3 --speculative-eagle-topk 1  --speculative-num-draft-tokens 4
```

### 🤯Quantization Analysis[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#quantization-analysis)

NVFP4 quants are 1.5x faster than BF16 and retains 92 to 97% top-1 accuracy.

We used [Dynamic 3.0 GGUFs](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) to make Qwen3.8-27B much better!

Top-1 accuracy plot as shown in UD-3 fro Qwen3.8-27B:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FVg5FHPxOpmaJ1r3ciw4u%252Fimage.png%3Falt%3Dmedia%26token%3D107ef044-0181-489b-b6ae-da218e16c98b&width=768&dpr=3&quality=100&sign=1d650d6108527f584a14d07606632a24&sv=3)

And mean KLD for Qwen3.8:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Ft8BnEqBLUQGUgu2cAKKI%252Fimage.png%3Falt%3Dmedia%26token%3D912d5b6a-540f-4ee0-9208-f5ad45776341&width=768&dpr=3&quality=100&sign=547e27686304f37d8063794818ab1950&sv=3)

### 📊 Benchmarks[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#benchmarks)

For GGUF quantization benchmarks you can see above for our [quantization analysis](https://unsloth.ai/docs/models/qwen3.8#quantization-analysis) or [Dynamic V3.0 article](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs).

#### Qwen3.8- **27B**[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#qwen3.8-27b)

See further below for table benchmarks:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FWijY5wYmLx70Ao2ol7Tj%252Fqwen%2520benchmark%25201.jpeg%3Falt%3Dmedia%26token%3Df69ebf50-cf35-426f-a610-8eeb32151d90&width=768&dpr=3&quality=100&sign=0593da64866fe85ceaf089fff13d0ecd&sv=3)

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FELa2vq8Wh3oelQi6Bf07%252Fqwen%2520benchmark%25202.jpeg%3Falt%3Dmedia%26token%3D2cc6d085-630d-4fa1-9b50-784b22a1fb04&width=768&dpr=3&quality=100&sign=c632695912aa7ed989fb334b670135b0&sv=3)

#### Text Performance[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#text-performance)

Benchmark

Qwen3.8-27B

Qwen3.6-27B

Qwen3.7-Plus

Muse Glimmer-30B

Opus4.6 Max

**Coding**

Agentic terminal codingTerminal Bench 2.1 (Terminus)

73.0

63.4

64.0

51.7

**78.2**

Agentic codingSWE-bench Pro

**61.7**

53.5

57.6

51.2

53.4

Repo-level code generationNL2Repo-Bench

42.3

36.2

41.1

--

**47.6**

Agentic codingDeepSWE 1.1

**42.2**

13.3

14.2

--

--

Software engineeringQwenSWEBench

**79.0**

49.3

59.2

--

63.8

**Agent**

Long-horizon office workCoWorkBench

**70.7**

61.0

65.1

--

68.2

Professional job tasksJobBench

**33.4**

21.8

27.6

--

--

Frontier agentic tasksAgents' Last Exam

Pass@1 **20.4** Score **42.9**

Pass@110.6Score27.3

Pass@113.2Score33.6

--

--

General

Instruction followingIFBench

**79.5**

69.1

79.1

77.0

62.5

Scientific reasoningGPQA Diamond

89.2

87.8

90.3

83.5

**91.3**

Multidisciplinary reasoningHLE

30.8

24.0

34.7

22.0

**40.0**

Competitive codingLiveCodeBench v6

**90.3**

83.9

89.6

--

88.8

#### Qwen3.8- **2.4T-A95B**[Direct link to heading](https://unsloth.ai/docs/models/qwen3.8\#qwen3.8-2.4t-a95b)

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FWP0nBgaQcnnAGjqG1jyQ%252Fqwen3.8%2520bench.jpg%3Falt%3Dmedia%26token%3D92a0d19c-51cb-4df2-a4f5-334fe08e6a21&width=768&dpr=3&quality=100&sign=e4492aecb4b1770cbf743f97bfbcf52a&sv=3)

[PreviousDeepSeek-V4.1-Flash](https://unsloth.ai/docs/models/deepseek-v4.1-flash) [NextFine-tune Qwen3.8](https://unsloth.ai/docs/models/qwen3.8/train)

Last updated 19 days ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject