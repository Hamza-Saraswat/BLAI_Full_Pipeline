[Skip to content](https://github.com/ggml-org/llama.cpp/issues/32197#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/issues/32197) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/issues/32197) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/issues/32197) to refresh your session.Dismiss alert

{{ message }}

# DeepSeek-V4.1-Flash (deepseek41): CPU/AMX scheduler aborts on non-contiguous attn\_wo\_a input\#32197

[New issue](https://github.com/login?return_to=https://github.com/ggml-org/llama.cpp/issues/32197)

Copy link

[New issue](https://github.com/login?return_to=https://github.com/ggml-org/llama.cpp/issues/32197)

Copy link

Open

Open

[DeepSeek-V4.1-Flash (deepseek41): CPU/AMX scheduler aborts on non-contiguous attn\_wo\_a input](https://github.com/ggml-org/llama.cpp/issues/32197#top)#32197

Copy link

## Description

[![@lucdurb](https://avatars.githubusercontent.com/u/81250814?v=4&size=48)](https://github.com/lucdurb)

[lucdurb](https://github.com/lucdurb)

opened [2h agoon Nov 13, 2026](https://github.com/ggml-org/llama.cpp/issues/32197#issue-6369739363)

Issue body actions

### Description

`llama-server` aborts while building the compute graph for

`DeepSeek-V4.1-Flash-1017-UD-Q4_K_XL` on a CPU-only Intel system with AMX.

The scheduler cannot assign a backend to `MUL_MAT` nodes named

`attn_wo_a-*`.

### Root cause observed

Instrumenting `ggml::cpu::amx::supports_op` shows:

```
AMX_REJECT: attn_wo_a-0 reason=not_contiguous src0=1 src1=0
SCHED_FAIL: node=attn_wo_a-0 op=MUL_MAT type=f32
ne=[1024][1][4][8]
src0=q8_0 ne=[4096][1024] buf=AMX
src1=f32  ne=[4096]    buf=none[4]
GGML_ASSERT(*cur_backend_id != -1) failed
```

The AMX backend requires both `src0` and `src1` to be contiguous.

`src0` is a contiguous `Q8_0` weight in the AMX buffer, but `src1`

is a non-contiguous `F32` activation.

Because the CPU backend’s extra-buffer check returns immediately after

consulting the AMX extra-buffer type, the generic CPU backend is not

consulted as a fallback. The node remains unassigned and

`ggml_backend_sched_split_graph()` aborts.

### Reproduction

```
./build/bin/llama-server \
  --model <path-to>/DeepSeek-V4.1-Flash-1017-UD-Q4_K_XL-00001-of-00009.gguf \
  --host 127.0.0.1 \
  --port 8080 \
  --ctx-size 1024 \
  --threads 16 \
  --device none \
  --n-gpu-layers 0 \
  --fit off \
  --no-warmup \
  -lv 5
```

### Environment

- llama.cpp: `2d8a32502`, build `12360`
- CPU-only build: no CUDA, Vulkan, HIP, or Metal
- Intel CPUs with AMX INT8
- Model: `unsloth/DeepSeek-V4.1-Flash-1017-GGUF`, `UD-Q4_K_XL`, 9 shards
- GGUF architecture: `deepseek41`
- GGUF version: `1017`

### Expected behavior

The graph should either make the `attn_wo_a` activation contiguous before

the `MUL_MAT`, or the scheduler/backend should provide a CPU fallback for

the non-contiguous input.

### Relevant log excerpt

```
AMX_REJECT: attn_wo_a-0 reason=not_contiguous src0=1 src1=0
SCHED_FAIL: node=attn_wo_a-0 op=MUL_MAT type=f32 ne=[1024] src0=q8_0 ne=[4096][1024] buf=AMX src1=f32 ne=[4096] buf=none[1][4][8]
/opt/llama.cpp-source/ggml/src/ggml-backend.cpp:1735: GGML_ASSERT(*cur_backend_id != -1) failed
```

## Activity

[Sign up for free](https://github.com/signup?return_to=https://github.com/ggml-org/llama.cpp/issues/32197)**to join this conversation on GitHub.** Already have an account?[Sign in to comment](https://github.com/login?return_to=https://github.com/ggml-org/llama.cpp/issues/32197)

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

No labels

No labels

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

### Participants

[![@lucdurb](https://avatars.githubusercontent.com/u/81250814?s=64&v=4)](https://github.com/lucdurb)

## Issue actions

- ![](https://github.githubassets.com/assets/github-copilot-app-light-15ad5534265eeacd.svg)Open in GitHub Copilot app

You can’t perform that action at this time.