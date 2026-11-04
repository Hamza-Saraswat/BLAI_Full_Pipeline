# URL: https://github.com/ggml-org/llama.cpp/discussions/27164
My issues and what I had to do to get Qwen3.8-27B /Qwen3.8-27B-MTP-ONLY-Q6_K.gguf /Qwen3.8-27B-MTP-ONLY-Q4_K_M.gguf to work with Llama.cpp · ggml-org/llama.cpp · Discussion #27164

Started by infinitelayerworks on Aug 16, 2026, in General. 1 comment, 2 participants.

## llama.cpp / WSL CUDA: Qwen3.8-27B garbage output — DeltaNet CUDA bug, not MTP-specific

I ran into a pretty confusing issue with **Qwen3.8-27B in llama.cpp under WSL + CUDA on an RTX 3090**, and I wanted to document the fix because it can easily look like an MTP, quantization, driver, or corrupted-model problem.

### Short version
Qwen3.8-27B would:
- Load normally
- Use the expected amount of VRAM
- Run at full GPU inference speed
- Show no crash or obvious CUDA error

…but **every completion was corrupted garbage**.

Examples from the logs: `/Q i` and `ance iurnesNSE){''),('-ract`

The problem turned out **not to be MTP**. The base Qwen3.8-27B model was already broken on CUDA **before MTP speculative decoding was involved**. The actual issue was an older llama.cpp CUDA implementation affecting Qwen3.8's **DeltaNet/Gated DeltaNet layers**.

### Environment
- **OS:** WSL
- **GPU:** RTX 3090 24 GB
- **Backend:** llama.cpp CUDA
- **Old llama.cpp commit:** `221f0f6`
- **Working updated build:** around `b10450` / commit `ece963f41`
- Flash Attention enabled in the final working configuration
- Vision/mmproj enabled in the final service
- MTP speculative decoding enabled in the final service
- MTP draft models used: Qwen3.8-27B-MTP-ONLY-Q6_K.gguf, Qwen3.8-27B-MTP-ONLY-Q4_K_M.gguf
- Main model testing included `Q4_K_XL` and `Q6_K` quantizations

### Symptoms
The model loaded correctly and VRAM usage looked reasonable at roughly **19 GB**. Inference also ran at normal GPU speed. No OOM, no CUDA crash, no obvious model-load failure, no useful warning — but generated tokens were garbage.

### Important finding: MTP was NOT the cause
Stripped-down test (No MTP, No mmproj, minimal flags, plain model inference):
- Q4_K_XL without MTP: "unparsed Content-only output: /Q i" — garbage
- Q6_K without MTP: also failed, corrupted output

Main service Q4_K_XL + MTP: "unparsed Content-only output: ance iurnesNSE){''),('-ract"

Failure matrix:
| Configuration | Result |
| --- | --- |
| Q4_K_XL + MTP | ❌ Garbage |
| Q4_K_XL without MTP | ❌ Garbage |
| Q6_K without MTP | ❌ Garbage |
| Same GGUF through Vulkan/non-CUDA path | ✅ Correct |
| Updated llama.cpp CUDA + matching new `.so` libraries | ✅ Correct |
| Updated CUDA + MTP | ✅ Correct |

### What was actually broken
Qwen3.8-27B uses a hybrid architecture containing **DeltaNet / Gated DeltaNet-style layers** in addition to normal attention. The llama.cpp revision `221f0f6` had a problem in the **CUDA execution path used by those DeltaNet layers**. Once those layers produced incorrect results, the rest of the model generation was corrupted. "The model could load successfully and run quickly while still generating completely invalid output."

Confirmed the GGUFs were good: the **same GGUF via the Vulkan/non-CUDA backend** (b10448 release build) "immediately produced completely normal text."

### Another problem: shallow clone
The repo was cloned `--depth 1`, so `git pull` kept saying "Already up to date" while the checkout was actually **hundreds of commits behind current master**. Fixed with `git fetch --unshallow`, `git stash`, `git pull origin master` → moved from `221f0f6` to `ece963f` (~build 10450).

### Rebuild
cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=86 -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j4
(For an RTX 3090, compute capability 86.)

### CRITICAL gotcha: replacing llama-server alone did NOT fix it
After compiling the updated llama.cpp and replacing `llama-server`, the model still produced the same garbage: the new executable was still loading an **old `libggml-cuda.so`** through the existing library path (NEW llama-server + OLD libggml-cuda.so). Fix: update the matching shared libraries too (libggml.so, libggml-base.so, libggml-cpu.so, libggml-cuda.so, libllama.so). Check with `ldd /path/to/llama-server` and `echo $LD_LIBRARY_PATH`.

### Result after updating BOTH the binary and shared libraries
Final result on his RTX 3090:
- **Clean Qwen3.8-27B output**
- **~42.9 tok/s**
- CUDA working, Flash Attention working, Vision/mmproj working, MTP speculative decoding working

### TL;DR
If Qwen3.8-27B loads normally in llama.cpp CUDA but every response is garbage: 1. Try the model without MTP. 2. Try another backend if possible. 3. Check your actual llama.cpp commit/build. 4. If cloned with `--depth 1`, don't blindly trust `git pull` saying "Already up to date". 5. `git fetch --unshallow` + `git pull origin master`. 6. Rebuild llama.cpp with CUDA. 7. Update the shared libraries along with `llama-server`. 8. Check `ldd` and `LD_LIBRARY_PATH`. "In my case the problem was not the GGUF, not Q4 vs Q6, and not MTP. It was the older **Qwen3.8 DeltaNet CUDA path in llama.cpp**, followed by the extra trap of the rebuilt server still loading an old CUDA shared library."

## Reply — mohammedhachoud, Oct 15, 2026 (3 weeks ago)
"Thanks for sharing this! I ran into almost exactly the same issue with Qwen3.8-27B on a DGX Spark. The model loaded normally and inference speed looked fine, but every response was just repeated `/` characters. I initially suspected CUDA too, especially after reading your discussion. But after testing with a CPU-only build, I found that the GGUF file itself was corrupted, despite having the correct file size. I documented the debugging process and what eventually fixed it here: my discussion #30609. Just wanted to share since the symptoms were so similar, but the root cause was completely different."
