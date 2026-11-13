By the [llama.cpp](https://github.com/ggml-org/llama.cpp) team and Hugging Face

# Your AI.  On your computer.

Llama is a tiny menu bar app that runs the latest open models on your Mac.Llama is a system tray app that runs the latest open models on your PC.Llama is an app for Mac and Windows that runs the latest open models on your computer. Chat with them, or use them in your other apps.

[Download for Mac](https://llama.app/download/mac) [Download for Windows 11](https://llama.app/download/windows) Watch the intro 0:36

[View on GitHub](https://github.com/ggml-org/Llama-Windows)

1 MB download · Free · Open source · Works offline

On Linux? Install the command-line version:

`curl -LsSf https://llama.app/install.sh | sh`

Prefer Brew or Winget? [Package managers](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md)·Rather build from source? [Follow instructions](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)

Wed Sep 23 10:24

Llama

2 localhost:9931Open chat 1

Installed models

Qwen3.8 27B19.0 GB

gpt-oss 20B12.1 GB

gemma-4 E4B4.59 GB

3 Recommended for this Mac

gemma-4 12B7.22 GB

Browse modelsFull catalog on the web

llama.cpp b9726SettingsQuit

Llama

2 localhost:9931Open chat 1

Installed models

Qwen3.8 27B19.0 GB

gpt-oss 20B12.1 GB

gemma-4 E4B4.59 GB

3 Recommended for this PC

gemma-4 12B7.22 GB

Browse modelsFull catalog on the web

llama.cpp b9726SettingsQuit

10:24 AM9/23/2026

1. 1Open chatChat with any model in your browser. Like ChatGPT, but on your Maccomputer.
2. 2A local APIYour apps connect here. It speaks the OpenAI API, so coding agents, editors, and
    scripts just work.
3. 3Recommended for this MacPCModels that fit your Maccomputer, one click to install. Llama picks
    the settings.

## Like OpenAI, but on your Maccomputer

OpenAI has ChatGPT to chat with and an API to build on. Llama gives you both, running on
your own computer, with models you choose.

For you

### Chat · like ChatGPT

lease-agreement.pdf

Summarize this and flag anything unusual.

It's a standard 12-month lease. Two things stand out: it renews automatically unless you
give 90 days' notice, and…

Click “Open chat” in the menu. Nothing to set up.

For your apps

### API · like the OpenAI API

Coding agentsPi

EditorsOpenAI-compatible

Chat appsOpenAI-compatible

Your own codeAny OpenAI SDK

Point any app that works with OpenAI at `localhost:9931/v1`

### Your models · download once, use everywhere

Qwen3.8 27B gpt-oss 20B gemma-4 E4B

## Nothing to set up

Running AI locally used to mean reading forum threads about settings. Llama checks your Maccomputer and sets up each model to run well on it, based on how llama.cpp actually works. You only pick
which model to talk to.

Know what you're doing? Every llama.cpp setting is still there, in one plain-text file.

Qwen3.8 27BChosen by Llama, for your Maccomputer

- QuantizationHighest precision that fits in memoryAuto
- Context sizeOnly sizes that fit in memoryAuto
- Image inputOn for models that understand imagesAuto
- Speculative decodingOn for models that support itAuto
- Batch sizeLarger on Macs with 32 GB or moreAuto

## Light enough to forget it's there

Local AI has a reputation for eating disk space and memory. Llama keeps both to a minimum.

### 4 MB app

A native Mac app, and just a 1 MB download -- smaller than a photo.

Llama.dmg1 MBDownload

Llama.app4 MBInstalled

### Each model stored once

Kept in the Hugging Face cache, shared with llama.cpp and other tools.

Llamallama.cppOther tools

Qwen3.8 27B19 GBIn the Hugging Face cache

### Nothing loaded when idle

Models load when something asks for one and unload after 5 minutes idle.

In use5 min idleUnloaded

## A great model for every Maccomputer

Llama suggests one that fits when you open it. Here's where to start.

[16 GB Macof memory or more Gemma 4Everyday questions, writing, and images](https://llama.app/models/gemma-4) [24 GB Macof memory or more GPT-OSSStep-by-step reasoning from OpenAI](https://llama.app/models/gpt-oss) [32 GB Macof memory or more Qwen 3.8Strong at code, reasoning, and long documents](https://llama.app/models/qwen-3-8)

[Browse models](https://llama.app/models)

## Build on Llama

Your apps get a local AI API they can all share, and Llama takes care of the engine and the
models.

### OpenAI-compatible API

If your code works with OpenAI, it works with Llama. Change the base URL and keep
everything else -- no API keys, no usage bills.

- OpenAI- and Anthropic-compatible
endpoints
- Streaming, tool calling, structured
output, vision
- Already use llama.cpp? Your
models show up automatically
- The `llama` command too: `llama cli`, `llama serve`,
and more
- Reach it from your other devices
over Tailscale

[API reference](https://llama.app/docs/api) [Command line](https://llama.app/docs/cli)

$curl http://localhost:9931/v1/chat/completions \-H"Content-Type: application/json"\-d'{
"model": "ggml-org/gpt-oss-20b-GGUF:MXFP4",
"messages": \[{"role": "user", "content": "Hi!"}\]
}'

### Nothing to bundle

Your app talks to Llama over the API, and a one-click link installs the model it needs. No
engine to ship, no gigabytes in your download -- and your users keep one copy of each model
for all their apps.

Without Llama 57 GB on disk

Chat app

EngineModel 19 GB

Coding agent

EngineModel 19 GB

Your app

EngineModel 19 GB

With Llama 19 GB on disk

Chat appCoding agentYour app

Llama

EngineModel 19 GB

## Local AI starts here

Free, open source, and yours to keep.

[Download for Mac](https://llama.app/download/mac) [Download for Windows 11](https://llama.app/download/windows)

or

`brew install --cask llama-app`

Just want the command line?Install the command line:

`curl -LsSf https://llama.app/install.sh | sh`

`irm https://llama.app/install.ps1 | iex`