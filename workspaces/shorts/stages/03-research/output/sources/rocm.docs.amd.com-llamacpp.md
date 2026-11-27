# Source: https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/advanced/advancedrad/windows/llm/llamacpp.html
# Fetched: 2026-11-27 via web_extract

# Llama.cpp pre-built binaries

[llama.cpp](https://github.com/ggml-org/llama.cpp) is an open-source framework for Large Language Model (LLM) inference that runs on both central processing units (CPUs) and graphics processing units (GPUs).

This document provides installation instructions for the **AMD-validated**`llama.cpp` **prebuilt binaries**. These are pre-compiled, stable executables (like `server` and `llama-bench`) that are ready to run on a Windows system without requiring any compilation.

1. Download the AMD-validated Windows binary package and extract it.

Windows

Download the prebuilt binary package.

```
curl.exe -o llama-bin-windows.zip "https://repo.radeon.com/rocm/llama.cpp/windows/rocm-rel-7.2.1/llama-b8407-windows-rocm-7.2.1-gfx110X-gfx115X-gfx120X-x64.zip"
```

2. Unzip the package into a new directory. (Powershell)

```
Expand-Archive -Path "llama-bin-windows.zip" -DestinationPath ".\llama_cpp_binaries"
```

3. Navigate into the inner directory

```
cd ./llama_cpp_binaries/<specific_folder_name>
```

4. Download a Test Model. These binaries are the “engine”; you still need a model file (in GGUF format) to run. For this tutorial, we will download the GPT-OSS-20B for testing.

Ubuntu 24.04

```
curl.exe -L -o test_model.gguf "https://huggingface.co/ggml-org/gpt-oss-20b-GGUF/resolve/main/gpt-oss-20b-mxfp4.gguf"
```

5. Run Llama-Server. `llama-server` is a lightweight, OpenAI-compatible web server included with `llama.cpp` that hosts your model locally. Once running, it provides a simple web interface that allows you to chat with the model directly in your browser.

Ubuntu 24.04

```
# Start the server
# -ngl 99: Offload all layers to your AMD GPU (Crucial for performance)
# -c: Context Length
# -fa: Enable Flash Attention to reduce memory usage and increase speed
.\llama-server.exe -m test_model.gguf -c 2048 -ngl 99 -fa on --port 8080
```

6. (Optional) Run a benchmark. Now, run the llama-bench tool against the test model. This command will load the model and run a standardized performance test, measuring your system’s prompt processing (PP) and token generation (TG) speed.

Ubuntu 24.04

```
# Run the benchmark with the downloaded model.
# -m: specifies the model file
.\llama-bench.exe -m .\test_model.gguf -fa 1
```

Versions: [latest](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/advanced/advancedrad/windows/llm/llamacpp.html), docs-7.2.1, docs-7.2, docs-7.1.1, docs-7.1, docs-7.0.2, docs-6.4.4, docs-6.4.2, docs-6.3.4, docs-6.3.2, docs-6.2.3, docs-6.1.3, docs-6.0.2, docs-5.7.0. Hosted on Read the Docs.
