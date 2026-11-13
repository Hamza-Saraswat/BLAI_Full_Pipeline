[Skip to content](https://github.com/ggml-org/llama.cpp/issues/32198#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/issues/32198) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/issues/32198) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/ggml-org/llama.cpp/issues/32198) to refresh your session.Dismiss alert

{{ message }}

# Eval bug: Hexagon MUL\_MAT\_ID returns inf or wrong values when activations or results exceed the fp16 range\#32198

[New issue](https://github.com/login?return_to=https://github.com/ggml-org/llama.cpp/issues/32198)

Copy link

[New issue](https://github.com/login?return_to=https://github.com/ggml-org/llama.cpp/issues/32198)

Copy link

Open

Open

[Eval bug: Hexagon MUL\_MAT\_ID returns inf or wrong values when activations or results exceed the fp16 range](https://github.com/ggml-org/llama.cpp/issues/32198#top)#32198

Copy link

## Description

[![@Helldez](https://avatars.githubusercontent.com/u/74499579?u=ecc75fbfdfbc94a80145e58e9a5372815f2ce7f6&v=4&size=48)](https://github.com/Helldez)

[Helldez](https://github.com/Helldez)

opened [1h agoon Nov 13, 2026](https://github.com/ggml-org/llama.cpp/issues/32198#issue-6370037760)

Issue body actions

### Name and Version

ggml at `cd959bae9` (llama.cpp 0.9.0, 2026-11-04), built with the NDK r27c, `GGML_BACKEND_DL=ON`. The Hexagon backend is loaded as a module. Called through the ggml backend API.

### Operating systems

Other? (Please let us know in description): Android

### GGML backends

Hexagon

### Hardware

Snapdragon phone, Hexagon v81 (`HTP0`, DMA64 on), 12 GB RAM

### Models

gemma-4-26B-A4B-it Q4\_K\_M. Qwen3.6-35B-A3B Q4\_K\_M as a control.

### Problem description & steps to reproduce

`MUL_MAT_ID` on HTP0 gives inf, or values far from the CPU's, once the inputs or the results go past the fp16 range. Below that range it matches the CPU.

I ran one MUL\_MAT\_ID with the real expert weights of layer 0 of gemma-4-26B-A4B (`ffn_gate_up_exps` q4\_K `[2816,1408,128]` and `ffn_down_exps` q8\_0 `[704,2816,128]`): 64 tokens, top-8 random ids, f32 activations from N(0,1). In some runs I also set 4 channels to ±V. I compared HTP0 with the CPU backend (weights in the HTP0 buffer type, inputs on the CPU, `ggml_backend_sched` with both backends):

| activations | gate\_up (q4\_K) NMSE | down (q8\_0) NMSE |
| --- | --- | --- |
| N(0,1), also ×100 and ×1000 | 5.0e-5 | 2.9e-5 |
| 4 channels at ±1e3 | 2.0e-4 | 3.1e-5 |
| 4 channels at ±3e4 | 9.7e-7 | 1.4e-7 |
| 4 channels at ±1e5 | **1.2e-1** | **nan, 4 non-finite outputs** (CPU max \|y\| 1.06e5, HTP0 6.45e4) |

The breaking point is the fp16 limit (65504). `GGML_HEXAGON_MM_SELECT=1` (HVX only) gives the same results as HMX.

Full model: prefilling 64 tokens of gemma-4-26B-A4B on HTP0 (expert matmuls on the NPU, the rest on the CPU) diverges from the CPU prefill. The next token agrees in 25 of 31 positions, mean KL 0.60, one position at KL 13.5 where the CPU's top token had p = 0.999. Qwen3.6-35B-A3B Q4\_K\_M on the same path: 94% agreement, mean KL 0.004. I did not dump Gemma's real activations, so it is a guess that they cross 65504 there; Gemma is known for very large activations in a few channels.

Expected: either a result as close to the CPU as in the other rows, or the op not claimed by the backend for inputs it cannot represent.

### First Bad Commit

Not bisected.

### Relevant log output

```
ffn_gate_up_exps q4_K K=2816 scale 1 outlier 30000: device NMSE 9.710e-07, non-finite 0, |y|max device 1.16e+04 host 1.16e+04
ffn_down_exps q8_0 K=704 scale 1 outlier 30000: device NMSE 1.359e-07, non-finite 0, |y|max device 3.17e+04 host 3.17e+04
ffn_gate_up_exps q4_K K=2816 scale 1 outlier 100000: device NMSE 1.188e-01, non-finite 0, |y|max device 2.54e+04 host 3.88e+04
ffn_down_exps q8_0 K=704 scale 1 outlier 100000: device NMSE -nan, non-finite 4, |y|max device 6.45e+04 host 1.06e+05
```

The test program (about 150 lines, ggml API only) is available on request.

## Activity

1. [![](https://avatars.githubusercontent.com/u/74499579?s=64&u=ecc75fbfdfbc94a80145e58e9a5372815f2ce7f6&v=4)Helldez](https://github.com/Helldez)

added a commit that references this issue [1h agoon Nov 13, 2026](https://github.com/ggml-org/llama.cpp/issues/32198#event-36021258456)









[fix(engine): the prefill device's check also logs the KL divergence f…](https://github.com/Helldez/BigMoeOnEdge/commit/d1be4c979c396bfa04c15f5779ece5a0895c3678)

...



[d1be4c9](https://github.com/Helldez/BigMoeOnEdge/commit/d1be4c979c396bfa04c15f5779ece5a0895c3678)


[Sign up for free](https://github.com/signup?return_to=https://github.com/ggml-org/llama.cpp/issues/32198)**to join this conversation on GitHub.** Already have an account?[Sign in to comment](https://github.com/login?return_to=https://github.com/ggml-org/llama.cpp/issues/32198)

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

[![@Helldez](https://avatars.githubusercontent.com/u/74499579?s=64&u=ecc75fbfdfbc94a80145e58e9a5372815f2ce7f6&v=4)](https://github.com/Helldez)

## Issue actions

- ![](https://github.githubassets.com/assets/github-copilot-app-light-15ad5534265eeacd.svg)Open in GitHub Copilot app

You can’t perform that action at this time.