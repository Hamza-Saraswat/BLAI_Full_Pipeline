InstallvLLM 0.25.0+ · CUDApip / Docker

Verified on NVIDIA H200

CopycURLBenchEnv

```
export VLLM_USE_RUST_FRONTEND=1
```

```
vllm serve deepseek-ai/DeepSeek-V4-Pro-0813 \
  --trust-remote-code \
  --kv-cache-dtype fp8 \
  --block-size 256 \
  --enable-expert-parallel \
  --tensor-parallel-size 8 \
  --max-model-len 800000 \
  --max-num-seqs 512 \
  --disable-flashinfer-autotune \
  --compilation-config '{"mode": 0, "cudagraph_mode": "FULL_DECODE_ONLY"}' \
  --tokenizer-mode deepseek_v4 \
  --tool-call-parser deepseek_v4 \
  --enable-auto-tool-choice \
  --reasoning-parser deepseek_v4 \
  --speculative-config '{"method":"dspark","num_speculative_tokens":7,"draft_sample_method":"probabilistic"}'
```

Hardware

NVIDIA

H10080G/GPUH200141G/GPUB200180G/GPU2 presetsGB200 NVL4192G/GPUB300268G/GPUGB300 NVL4288G/GPU

AMD

MI300X192G/GPUMI325X256G/GPUMI355X288G/GPU2 presetsMI350X288G/GPU

Variant

FP8 (0813)960 GBFP8 (PREVIEW)960 GBNVFP4960 GBDSPARK960 GBNVFP4+FP8 (REDHAT)1000 GB

Official DeepSeek-V4-Pro release (2026-08-13) superseding the preview — substantially stronger agentic performance, with the DSpark draft module attached.

[![](https://recipes.vllm.ai/platform-logos/huggingface.svg)deepseek-ai/DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)

Strategy

Tensor ParallelTensor + Expert ParallelData + Expert ParallelDP Attention + Tensor ParallelPrefill/Decode Disaggregation

Single-node TEP. TP splits dense layers and EP splits expert layers across local GPUs. TP must be set to GPU count to avoid OOM from replicated dense layers. For MoE models only.

Balanced

KV Offload

OffSimpleOffloadingMooncake StoreLMCacheIAXLUMBP

Nodes

Single-nodeMulti-node (example: 2)16×GPU

Frontend

RustPython

The experimental Rust frontend can improve throughput and latency, especially under high concurrency. Switch to Python if you encounter unsupported features or compatibility issues.

Features

Tool CallingReasoningSpec Decoding(for low latency & small batch size)

Draft sampling: greedy at temperature 0. For chat at temperature 0.6–1.0, probabilistic usually accepts more tokens, at the cost of a little more VRAM.

Advanced— performance tuning

max-num-batched-tokens = 8192

Tunable batch budget; 8192 is a common sweet spot

max-num-seqs = 256

Max concurrent sequences per batch; lower for latency, higher for throughput

gpu-memory-utilization = 0.95

Push KV cache further; use with caution on shared GPUs

max-model-len = auto

Auto-size context window to what KV cache can hold on your hardware

no-enable-flashinfer-autotune

Skip FlashInfer autotuning at startup (faster startup, may lose autotuned perf)

enable-ep-weight-filter

Skip loading expert weights that don't belong to this EP rank — speeds up weight loading for large MoE models

GuidePresets4

## Overview [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#overview "Copy link to this section")

DeepSeek-V4-Pro is the flagship of the V4 preview family: a 1.6T-total / 49B-active
Mixture-of-Experts model. It pairs a **hybrid attention stack** — Compressed Sparse
Attention (CSA) + Heavily Compressed Attention (HCA) — with **Manifold-Constrained**
**Hyper-Connections (mHC)** to reach 27% of V3.2's per-token inference FLOPs and 10% of
V3.2's KV cache at 1M context. Pre-trained on 32T+ tokens with the **Muon optimizer**
for faster convergence; post-training is a two-stage pipeline (domain-specific expert
cultivation + unified consolidation via on-policy distillation).

Checkpoint is **FP4+FP8 mixed**: MoE expert weights are stored in FP4 while the
remaining (attention / norm / router) params stay in FP8.

An **NVFP4 variant** (`nvidia/DeepSeek-V4-Pro-NVFP4`) is also available — NVIDIA
modelopt re-quantizes the MoE experts to standard NVFP4 while attention, shared
experts, router head, and MTP stay FP8. Pick it from the **Variant** row; it runs on
Blackwell GPUs with the FP4 indexer cache.

## Checkpoints [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#checkpoints "Copy link to this section")

Four checkpoints are on the **Variant** row. They differ in _which weights you serve_
and _which draft module ships with them_ — the speculative method itself is picked on
the **Spec Decoding** row.

| Variant | Repo | Draft | Notes |
| --- | --- | --- | --- |
| **FP8 (0813)** (default) | `deepseek-ai/DeepSeek-V4-Pro-0813` | DSpark | Official release, preview structure + DSpark |
| **FP8 (Preview)** | `deepseek-ai/DeepSeek-V4-Pro` | MTP | Preview FP4+FP8 mixed weights |
| **NVFP4** | `nvidia/DeepSeek-V4-Pro-NVFP4` | MTP | modelopt re-quant, Blackwell |
| **DSpark** | `deepseek-ai/DeepSeek-V4-Pro-DSpark` | DSpark | Preview weights + fused DSpark module |

**0813 is the official DeepSeek-V4-Pro release** and the default here, superseding
the preview with substantially stronger agentic capability — 87.9 on Terminal Bench
2.1, 62.7 on DeepSWE and 42.7 on HLE (60.0 with tools), versus 72.1, 12.8 and 37.7
for the preview. It is built on the preview model structure with a DSpark speculative
decoding module attached. The preview weights remain available as the
**FP8 (Preview)** variant for reproducing earlier results.

**DSpark** is _not_ new weights — it is the preview checkpoint with a speculative
decoding module attached (see [DeepSpec](https://github.com/deepseek-ai/DeepSpec)).
Both fused checkpoints add a `dspark_*` block to `config.json`; the preview and NVFP4
checkpoints have no such block, which is why the DSpark method is offered only on the
two variants that carry the draft. Selecting either one auto-enables **Spec Decoding**
with `method: dspark`, emitting:

```
--speculative-config '{"method":"dspark","num_speculative_tokens":7,"draft_sample_method":"probabilistic"}'
```

The fused checkpoints are ~893 GB on disk versus ~865 GB for the preview — the draft
module is the difference. Both require **vLLM 0.25.0**, above this recipe's 0.20.0
baseline; the Install block bumps automatically when either is selected.

## Reasoning modes [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#reasoning-modes "Copy link to this section")

The chat template exposes three reasoning-effort modes:

- **Non-think** — fast, intuitive responses.
- **Think High** — explicit chain-of-thought for complex problem-solving and planning.
- **Think Max** — maximum reasoning effort; requires `--max-model-len >= 393216`
(384K tokens) to avoid truncation.

Recommended sampling: `temperature = 1.0`, `top_p = 1.0`.

On the **0813** variant the effort levels are named `low` / `high` / `max`, and
DeepSeek recommends `top_p = 0.95` for agentic scenarios (`1.0` otherwise) with
`temperature = 1.0`. Allow up to **384K output tokens** at the `high` and `max`
levels.

Note that the 0813 release ships no Jinja chat template — the repo provides an
`encoding/` folder with `encode_messages` / `parse_message_from_completion_text`
helpers instead. Serving through vLLM with `--tokenizer-mode deepseek_v4` (the
**Tool Calling** pill) applies the built-in DeepSeek-V4 encoding, so the OpenAI-
compatible endpoint works without the helper scripts.

### OpenAI Client Example [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#openai-client-example "Copy link to this section")

For DeepSeek-V4, keep reasoning controls in `chat_template_kwargs`, as it exposes a
custom **Think Max** mode via `"reasoning_effort": "max"`.

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
model = "deepseek-ai/DeepSeek-V4-Pro-0813"
messages = [{"role": "user", "content": "What is 17*19? Return only the final integer."}]

# Non-think
resp = client.chat.completions.create(
    model=model,
    messages=messages,
)

# Think High
resp = client.chat.completions.create(
    model=model,
    messages=messages,
    extra_body={
        "chat_template_kwargs": {
            "thinking": True,
            "reasoning_effort": "high",
        },
    },
)

# Think Max
resp = client.chat.completions.create(
    model=model,
    messages=messages,
    extra_body={
        "chat_template_kwargs": {
            "thinking": True,
            "reasoning_effort": "max",
        },
    },
)
```

## Recommended deployments [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#recommended-deployments "Copy link to this section")

- **B300 (8× GPU)**: single-node DP + EP with `--data-parallel-size 8`.
- **H200 (8× GPU)**: DP + EP with `--data-parallel-size 8`. Context is capped at
800K tokens (`--max-model-len 800000`) to leave KV headroom with dense params
replicated across ranks — applies to both single-node and multi-node H200.
- **MI355X (8× GPU)**: validated with ROCm + AITER (`VLLM_ROCM_USE_AITER=1`),
`--max-num-seqs 128`,
`--max-num-batched-tokens 8192`, and `--distributed-executor-backend mp`.
- **GB200 NVL4 (4× GPU per tray)**: the ~960 GB mixed-precision checkpoint does not
fit on one tray; run multi-node DP + EP across **2 trays** (8 GPUs total) with
`--data-parallel-size 8`. Pick the "Multi-Node" tab and set nodes to 2.

### MI355X (8×288GB) [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#mi355x-8288gb "Copy link to this section")

```bash
export VLLM_ROCM_USE_AITER=1

vllm serve deepseek-ai/DeepSeek-V4-Pro \
  --host localhost \
  --port 8001 \
  --dtype auto \
  --kv-cache-dtype fp8 \
  --tensor-parallel-size 8 \
  --max-num-seqs 512 \
  --max-num-batched-tokens 8192 \
  --distributed-executor-backend mp \
  --trust-remote-code \
  --tokenizer-mode deepseek_v4 \
  --reasoning-parser deepseek_v4 \
  --tool-call-parser deepseek_v4 \
  --enable-auto-tool-choice \
  --compilation-config '{"mode": 3, "cudagraph_mode": "FULL_DECODE_ONLY"}'
```

#### MI355X is validated on GSM8K dataset: [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#mi355x-is-validated-on-gsm8k-dataset "Copy link to this section")

##### Launch command [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#launch-command "Copy link to this section")

```bash
MODEL=deepseek-ai/DeepSeek-V4-Pro
lm_eval --model local-completions \
  --model_args model=$MODEL,base_url=http://0.0.0.0:8001/v1/completions,num_concurrent=128,max_retries=10,max_gen_toks=2048,timeout=60000 \
  --batch_size auto \
  --tasks gsm8k \
  --num_fewshot 8 \
  --output_path . 2>&1 | tee -a eval.log
```

##### Reported result [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#reported-result "Copy link to this section")

```text
local-completions ({'model': 'deepseek-ai/DeepSeek-V4-Pro', 'base_url': 'http://0.0.0.0:8001/v1/completions', 'num_concurrent': 128, 'max_retries': 10, 'max_gen_toks': 2048, 'timeout': 60000}), gen_kwargs: ({}), limit: None, num_fewshot: 8, batch_size: auto
|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k|      3|flexible-extract|     8|exact_match|↑  |0.9538|±  |0.0058|
|     |       |strict-match    |     8|exact_match|↑  |0.9545|±  |0.0057|
```

## KV Cache Offloading [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#kv-cache-offloading "Copy link to this section")

Agentic and multi-turn workloads reuse long prefixes whose KV state can exceed on-GPU
capacity. The **KV Offload** row attaches a host-DRAM KV tier to any serving strategy —
pick one of three connectors:

- **Simple** — `SimpleCPUOffloadConnector`: spills KV blocks to a per-rank region of CPU
DRAM on each node. The simplest way to extend effective KV capacity for a single instance.
- **Mooncake** — `MooncakeStoreConnector`: pools CPU DRAM into a distributed shared KV
store — either embedded (each rank's vLLM worker runs a Mooncake client that donates a DRAM segment)
or standalone (a per-node `mooncake_store_service` owns the node's DRAM and contributes
it to the pool, decoupling cache lifetime from the engine). A cluster-wide
`mooncake_master` coordinates the pool; across 2+ instances, GPU workers share it for
cross-instance prefix reuse. Install from the extra-install block above; see the [Mooncake docs](https://kvcache-ai.github.io/Mooncake/).
- **LMCache** — `LMCacheMPConnector`: a node-local KV pool served by a
companion `lmcache server` process, launched before `vllm serve`.
Single-node strategies only. Install from the extra-install block above; see the [LMCache docs](https://docs.lmcache.ai/).

## Agentic serving on GB200/GB300 (DSpark) [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#agentic-serving-on-gb200gb300-dspark "Copy link to this section")

For agentic serving, use the following common settings with
[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813/tree/72e1d3230f6c080a530b0a1d46f8eb4602340597)
and its native DSpark draft. These are separate from the command-builder defaults.

### Common settings [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#common-settings "Copy link to this section")

Set `VLLM_USE_V2_MODEL_RUNNER=1` and use these engine arguments:

```text
--tokenizer-mode deepseek_v4 --trust-remote-code
--kv-cache-dtype fp8 --block-size 256
--no-disable-hybrid-kv-cache-manager --disable-flashinfer-autotune
--attention-config '{"backend":"FLASHINFER_MLA_SPARSE_DSV4","use_prefill_query_quantization":true,"indexer_kv_dtype":"mxfp4"}'
--speculative-config '{"method":"dspark","num_speculative_tokens":6,"draft_sample_method":"probabilistic","rejection_sample_method":"block"}'
```

The example uses `K=6`, where `K` is `num_speculative_tokens`. Tune K and the
prefill/decode (PD) ratio for each target concurrency to balance throughput,
per-user latency and time to first token. Use the same K on both PD roles.

For aggregate TP serving, use
`--disable-custom-all-reduce`, `VLLM_ALLREDUCE_USE_FLASHINFER=1`,
`VLLM_FLASHINFER_ALLREDUCE_BACKEND=auto`; do not select an EP MoE backend.
For DEP (TP1 with data and expert parallelism), both pools instead use
`--enable-expert-parallel --enable-ep-weight-filter --enable-cumem-allocator`,
`--moe-backend deep_gemm_amxf4_mega_moe` and `VLLM_DSV4_MEGA_FP8_COMBINE=1`.
This MoE configuration supports the native mixed FP4/FP8 checkpoint, unlike
the FP8-only `deep_gemm_mega_moe` setting above.

For aggregate and decode, set `cudagraph_mode=FULL_DECODE_ONLY` and `mode=0`
in `--compilation-config`, with explicit capture sizes `n*(K+1)` for `n=1..S`.
`S` is `max-num-seqs` per DP rank, or per engine for pure TP. Set the maximum
capture size to `S*(K+1)`; aggregate serving can also include `n*K` sizes.
Recompute the capture sizes when K or S changes. Size `max-num-batched-tokens`
to cover verification tokens plus any prefill work scheduled on that engine.

### Scheduling, NUMA binding, and streaming [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#scheduling-numa-binding-and-streaming "Copy link to this section")

**DEP decode scheduling:** the decode example below uses:

```text
--prefill-schedule-interval 16 --long-prefill-token-threshold 512
```

The interval controls how often DP ranks admit new prefill requests. Increasing
it can balance work across ranks but delays admission. The threshold limits
long-prefill chunk size when requests share the token budget.
Compare these overrides with leaving both flags unset, measuring throughput,
time to first token, and inter-token latency at your target load. Retune when
changing the workload, pool sizes, hardware, or engine version.

The prefill example uses `--long-prefill-token-threshold 1024` and leaves
`--prefill-schedule-interval` unset.

**DEP NUMA binding:** on every prefill and decode node, enable binding and
provide one NUMA node ID per visible GPU. For the four-GPU layout where GPUs
0/1 are local to NUMA node 0 and GPUs 2/3 to NUMA node 1, use:

```text
--numa-bind --numa-bind-nodes 0 0 1 1
```

Match the list to the local GPU order and topology on each node, including
GB300 deployments. See the [vLLM NUMA binding guide](https://docs.vllm.ai/en/latest/configuration/optimization/#numa-binding-for-multi-socket-gpu-nodes)
for automatic detection and explicit mappings.

**Aggregate streaming:** add `--stream-interval 10` to the aggregate TP8
worker at concurrency 1, 4, or 8. This batches streamed output into larger
updates to reduce host overhead; use a smaller interval when smoother token
delivery matters more. The DEP configurations leave this override unset.

### Running with Dynamo [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#running-with-dynamo "Copy link to this section")

The example below runs a DEP8 prefill pool and a DEP8 decode pool, each across
two four-GPU GB200 nodes, plus a host for shared services and the frontend.
Run the Python commands in `vllm/vllm-openai:nightly-dev-arm64-cu13.0.1-20ebb28`
with the model, recipe files, GPUs, and RDMA devices accessible;
use host networking so the advertised addresses are reachable across nodes.
Install the matching Dynamo packages in each frontend/worker container:

```bash
python3 -m pip install --extra-index-url https://pypi.nvidia.com \
  ai-dynamo==1.3.0.dev20260720 ai-dynamo-runtime==1.3.0.dev20260720
```

Save the following as `dynamo-env.sh` and source it in each shell. Replace the
example addresses with routable addresses on your cluster. `MODEL_PATH` must
contain the pinned 0813 checkpoint on every worker.

```bash
export INFRA_IP=10.0.0.10
export ETCD_ENDPOINTS="http://${INFRA_IP}:2379"
export NATS_SERVER="nats://${INFRA_IP}:4222"
export DYN_NAMESPACE=dspark
export MODEL_PATH=/models/DeepSeek-V4-Pro-0813
export SERVED_MODEL=deepseek-ai/DeepSeek-V4-Pro-0813
export PREFILL_HEAD_IP=10.0.0.11
export DECODE_HEAD_IP=10.0.0.21
```

**Shared services.** Provide `etcd`, `nats-server`, and `mooncake_master` on the
service host's `PATH`. See the official [Dynamo service setup](https://github.com/ai-dynamo/dynamo/blob/59dd504105db498b11e5715854a2512d57b7a1e0/dev/docker-compose.yml)
and [Mooncake installation](https://kvcache-ai.github.io/Mooncake/) for installation
options. Start these services once on the private cluster network, before workers:

```bash
source ./dynamo-env.sh
etcd --data-dir ./etcd-data --listen-client-urls http://0.0.0.0:2379 \
  --advertise-client-urls "$ETCD_ENDPOINTS" >etcd.log 2>&1 &
cat >nats.conf <<'EOF'
port: 4222
max_payload: 33554432
jetstream { store_dir: "./nats-data" }
EOF
nats-server -c ./nats.conf >nats.log 2>&1 &
mooncake_master --port=8700 --enable_http_metadata_server=true \
  --http_metadata_server_port=8701 --eviction_high_watermark_ratio=0.9 \
  --default_kv_lease_ttl=10000 --rpc_thread_num=16 \
  --enable_metric_reporting=true --metrics_port=8702 >mooncake.log 2>&1 &
```

Wait for the services to listen before continuing. All hosts must reach the
shared endpoints; workers must also reach each other's DP rendezvous and NIXL
addresses. Existing managed services can supply the same endpoints.

**Frontend.** In a separate shell, start the HTTP endpoint for the disaggregated
deployment:

```bash
source ./dynamo-env.sh
export DYN_ROUTER_ACTIVE_REQUEST_EXPIRY_SECS=3600
export DYN_TCP_CHANNEL_BUFFER=128
export DYN_TCP_REQUEST_TIMEOUT=60
python3 -m dynamo.frontend --http-port 8000 --router-mode random \
  --router-session-affinity-ttl-secs 900
```

- Aggregate: `--router-mode kv`, `DYN_ROUTER_TEMPERATURE=0` and
`DYN_TOKENIZER=fastokens`.
- Disaggregated: `--router-mode random` with session affinity, or `kv` with
the same tokenizer settings. Send a stable conversation
ID as `x-dynamo-session-id` and set `--router-session-affinity-ttl-secs` to
cover the conversation lifetime.
- Both DEP roles use `MultiConnector` with `NixlConnector` for PD transfer and
`MooncakeStoreConnector` for shared prefix storage. Enable store lookup only
on prefill, and set `VLLM_CONNECTOR_PREFETCH_DEPTH=0` there. Role-specific
`--kv-transfer-config` values:

Prefill — save as `prefill-kv.json` in the worker's working directory:

```json
{"kv_connector":"MultiConnector","kv_role":"kv_both","kv_connector_extra_config":{"connectors":[{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_load_failure_policy":"fail","kv_buffer_device":"cuda","kv_connector_extra_config":{"enforce_handshake_compat":false,"enable_cross_layers_blocks":false}},{"kv_connector":"MooncakeStoreConnector","kv_role":"kv_both","kv_connector_extra_config":{"load_async":true,"lookup_async":true,"enable_cross_layers_blocks":false,"enable_offload":false}}]}}
```

Decode — save as `decode-kv.json` in the worker's working directory:

```json
{"kv_connector":"MultiConnector","kv_role":"kv_consumer","kv_connector_extra_config":{"connectors":[{"kv_connector":"NixlConnector","kv_role":"kv_consumer","kv_load_failure_policy":"fail","kv_buffer_device":"cuda","kv_connector_extra_config":{"enforce_handshake_compat":false,"enable_cross_layers_blocks":false}},{"kv_connector":"MooncakeStoreConnector","kv_role":"kv_consumer","kv_connector_extra_config":{"load_async":true,"lookup_async":false,"enable_lookup":false,"enable_cross_layers_blocks":false,"enable_offload":false}}]}}
```

**Worker environment.** Run the following in Bash on each worker node. Set
`NODE_IP` to that node's routable address and `NODE_RANK` to 0 or 1 within its
own pool. For example, prefill nodes `10.0.0.11` / `10.0.0.12` use ranks 0 / 1;
decode nodes `10.0.0.21` / `10.0.0.22` also use ranks 0 / 1. All four GPUs are
visible to one launch process per node. Adjust the NUMA and NIC mappings to
match the hardware. The embedded Mooncake store uses 140 GB per local rank
in this example; ensure enough host memory or resize it for your deployment.

```bash
source ./dynamo-env.sh
export NODE_IP=10.0.0.11  # Change on each worker node.
NODE_RANK=0              # Use 1 on the second node of either pool.
export CUDA_VISIBLE_DEVICES=0,1,2,3
export VLLM_HOST_IP="$NODE_IP"
export VLLM_NIXL_SIDE_CHANNEL_HOST="$NODE_IP"
export VLLM_NIXL_SIDE_CHANNEL_PORT=20096
export DYN_SYSTEM_PORT=8081
export VLLM_USE_V2_MODEL_RUNNER=1 VLLM_DSV4_MEGA_FP8_COMBINE=1
export PYTHONHASHSEED=0
export MOONCAKE_MASTER="${INFRA_IP}:8700"
export MOONCAKE_TE_META_DATA_SERVER="http://${INFRA_IP}:8701/metadata"
export MOONCAKE_LOCAL_HOSTNAME="$NODE_IP"
export MOONCAKE_CONFIG_PATH="$PWD/mooncake.json"
cat >"$MOONCAKE_CONFIG_PATH" <<EOF
{"metadata_server":"P2PHANDSHAKE",
 "master_server_address":"${MOONCAKE_MASTER}","global_segment_size":"140GB",
 "local_buffer_size":"4GB","protocol":"rdma",
 "device_name":"mlx5_0,mlx5_1,mlx5_2,mlx5_3","mode":"embedded","enable_offload":false}
EOF

COMMON_ARGS=(
  --model "$MODEL_PATH" --served-model-name "$SERVED_MODEL"
  --tensor-parallel-size 1 --pipeline-parallel-size 1
  --data-parallel-size 8 --data-parallel-size-local 4
  --data-parallel-start-rank "$((4 * NODE_RANK))"
  --data-parallel-rpc-port 13345 --data-parallel-hybrid-lb
  --enable-expert-parallel --enable-ep-weight-filter --enable-cumem-allocator
  --moe-backend deep_gemm_amxf4_mega_moe
  --numa-bind --numa-bind-nodes 0 0 1 1
  --tokenizer-mode deepseek_v4 --trust-remote-code
  --max-model-len 1048576 --kv-cache-dtype fp8 --block-size 256
  --no-disable-hybrid-kv-cache-manager --disable-flashinfer-autotune
  --attention-config '{"backend":"FLASHINFER_MLA_SPARSE_DSV4","use_prefill_query_quantization":true,"indexer_kv_dtype":"mxfp4"}'
  --speculative-config '{"method":"dspark","num_speculative_tokens":5,"draft_sample_method":"probabilistic","rejection_sample_method":"block"}'
)
```

**Prefill workers.** Run once on each prefill node after the worker environment
block, keeping `PREFILL_HEAD_IP` identical across the pool:

```bash
export VLLM_CONNECTOR_PREFETCH_DEPTH=0
python3 -m dynamo.vllm "${COMMON_ARGS[@]}" --disaggregation-mode prefill \
  --data-parallel-address "$PREFILL_HEAD_IP" \
  --kv-transfer-config "$(cat prefill-kv.json)" \
  --max-num-seqs 64 --max-num-batched-tokens 8192 \
  --long-prefill-token-threshold 1024 --gpu-memory-utilization 0.85 \
  --max-cudagraph-capture-size 384
```

**Decode workers.** Run once on each decode node after the worker environment
block. This example uses K=5 and S=8, so graph capture sizes are 6 through 48:

```bash
python3 -m dynamo.vllm "${COMMON_ARGS[@]}" --disaggregation-mode decode \
  --data-parallel-address "$DECODE_HEAD_IP" \
  --kv-transfer-config "$(cat decode-kv.json)" \
  --max-num-seqs 8 --max-num-batched-tokens 8240 \
  --prefill-schedule-interval 16 --long-prefill-token-threshold 512 \
  --gpu-memory-utilization 0.9 --kv-cache-memory-bytes 37580963840 \
  --max-cudagraph-capture-size 48 \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY","mode":0,"cudagraph_capture_sizes":[6,12,18,24,30,36,42,48]}'
```

For DEP12/DEP16, set `--data-parallel-size` to 12/16 in the corresponding
pool and run on three/four four-GPU nodes. Each pool keeps its own head address;
start ranks are `4 * NODE_RANK` (0, 4, 8, 12). Tune scheduling for the target
workload and recompute graph sizes when changing K or S. The same port numbers can be
reused on separate hosts; co-located workers need distinct port allocations.
The [official Dynamo vLLM examples](https://github.com/ai-dynamo/dynamo/tree/59dd504105db498b11e5715854a2512d57b7a1e0/examples/backends/vllm/launch)
provide the aggregate and KV-routing launch patterns; apply this section's
model and aggregate settings when using those patterns.

Once all workers register, send requests to the frontend, retaining the same
session ID for turns in one conversation:

```bash
curl "http://${INFRA_IP}:8000/v1/chat/completions" \
  -H 'Content-Type: application/json' -H 'x-dynamo-session-id: example-session' \
  -d '{"model":"deepseek-ai/DeepSeek-V4-Pro-0813","messages":[{"role":"user","content":"Hello"}],"max_tokens":32}'
```

## MI355X AgentX profiles (InferenceX \#4526) [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#mi355x-agentx-profiles-inferencex-4526 "Copy link to this section")

The opt-in **AgentX TP8 + monokernel** and **AgentX DPA8 + TP experts** presets
cover the [InferenceX #4526](https://github.com/SemiAnalysisAI/InferenceX/pull/4526)
agentic-coding lane for
[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
on one eight-GPU MI355X node. Both use native DSpark K6, mixed FP8/MXFP4
weights and FP8 KV cache; only the TP8 arm enables the monokernel. They pin the
source nightly and target/tokenizer revisions, leaving the generic recipe and
the separate fixed-sequence lane unchanged.

These source profiles await resolution of the shared INT4 draft-communication
precision issue described in their runbooks before production qualification.

Their generated commands retain real target verification for serving and eval.
The preset runbooks record runtime package prerequisites, the session-affine
DP router, all twelve concurrency points, and the separate throughput-only
synthetic acceptance overlay (`3.77`). The source sweep and real GSM8K evals
supply external validation; no GPU run was performed for this recipe update.

## Fixed-sequence benchmark reproduction (InferenceX MI355X 8K/1K) [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#fixed-sequence-benchmark-reproduction-inferencex-mi355x-8k1k "Copy link to this section")

This is a **second, separate InferenceX lane** — not a variation of the Agentic
sweep above. It is a fixed-sequence measurement at input length 8192 and output
length 1024 on one 8× MI355X node, run as two arms: **STP** (no speculative
decoding) and **real MTP with two draft tokens**. Neither arm is the general
recipe default, and neither is a recommendation for other AMD workloads.

The checkpoint is `deepseek-ai/DeepSeek-V4-Pro` — the **FP8 (Preview)** pill in
the Variant row, whose mixed FP4+FP8 weights InferenceX labels `fp4`. It is not
the `0813` default variant and not the DSpark checkpoint.

### Source configuration [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#source-configuration "Copy link to this section")

| Item | Value |
| --- | --- |
| InferenceX PR | [#2792](https://github.com/SemiAnalysisAI/InferenceX/pull/2792) |
| Config keys | `dsv4-fp4-mi355x-vllm` (STP), `dsv4-fp4-mi355x-vllm-mtp` (MTP) |
| Hardware | one node, 8× MI355X |
| Image | `vllm/vllm-openai-rocm:nightly-7c5dc571cbd1064ecc8a9b1045637ff647aa22cb` |
| Image digest | `sha256:f0bdaf5217a09949842b45c1ea1f12260d3205ec81f143b320dfc2eb3ec95e55` |
| Parallelism | TP 8, DP 1, EP 1 — no `--enable-expert-parallel` |
| Workload | ISL 8192, OSL 1024; concurrency 4, 8, 16, 32, 64, 128, 256, 512 |
| Requests per point | 10 × concurrency |

The image is pinned to an immutable nightly tag rather than a floating
`:nightly`, because the measurements depend on the ROCm DeepSeek-V4 kernel state
in that specific build. The Install block's AMD default stays on `:nightly`
deliberately — pin the tag above only when reproducing these numbers.

### STP launch (no speculative decoding) [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#stp-launch-no-speculative-decoding "Copy link to this section")

```bash
export VLLM_ROCM_USE_AITER=1
export VLLM_ROCM_USE_AITER_MOE=1
# Fuses the FP8 shared expert into the MXFP4 routed-expert AITER kernel.
# See the shared-expert note below for the build and eligibility requirements.
export VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=1
export VLLM_ROCM_QUICK_REDUCE_QUANTIZATION=INT4

vllm serve deepseek-ai/DeepSeek-V4-Pro \
  --port "${PORT:-8000}" \
  --tensor-parallel-size 8 \
  --data-parallel-size 1 \
  --async-scheduling \
  --no-enable-prefix-caching \
  --distributed-executor-backend mp \
  --gpu-memory-utilization 0.8 \
  --kv-cache-dtype fp8 \
  --trust-remote-code \
  --moe-backend aiter \
  --tokenizer-mode deepseek_v4 \
  --reasoning-parser deepseek_v4 \
  --compilation-config '{"mode":3,"cudagraph_mode":"FULL_AND_PIECEWISE"}'
```

### MTP arm (real speculation, 2 draft tokens) [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#mtp-arm-real-speculation-2-draft-tokens "Copy link to this section")

The MTP arm is the same launch plus one flag. Everything else — environment,
parallelism, memory, cache, executor, MoE backend, parsers, compilation — is
identical:

```bash
  --speculative-config '{"method":"mtp","num_speculative_tokens":2}'
```

This is **real** MTP: draft tokens are verified against the target model. ROCm
support for the DeepSeek-V4 MTP head landed in
[vllm-project/vllm#43385](https://github.com/vllm-project/vllm/pull/43385). The
same two-token config is available from the command builder — enable _Spec_
_decoding_ and pick the **MTP** mode with the FP8 (Preview) variant selected.

### Left at engine defaults [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#left-at-engine-defaults "Copy link to this section")

This lane deliberately passes no `--max-model-len`, `--max-num-seqs`,
`--max-num-batched-tokens`, or `--block-size`, and no tool-calling flags. That
differs from this recipe's general AMD configuration, which does set several of
them — one reason this reproduction is documented separately rather than folded
into the default command.

### Benchmarking the MTP arm needs chat formatting [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#benchmarking-the-mtp-arm-needs-chat-formatting "Copy link to this section")

MTP-style speculation is trained against chat-formatted input. Benchmarking it
with raw completion prompts silently depresses the acceptance rate, so measure
it against the chat endpoint, which applies the DeepSeek-V4 chat template that
`--tokenizer-mode deepseek_v4` installs:

```bash
CONC=32

vllm bench serve \
  --model deepseek-ai/DeepSeek-V4-Pro \
  --host localhost \
  --port "${PORT:-8000}" \
  --backend openai-chat \
  --endpoint /v1/chat/completions \
  --dataset-name random \
  --random-input-len 8192 \
  --random-output-len 1024 \
  --num-prompts "$((CONC * 10))" \
  --max-concurrency "$CONC" \
  --ignore-eos \
  --trust-remote-code
```

InferenceX drives its own benchmark client with a private DeepSeek-V4 encoder
rather than the tokenizer's built-in template, so the numbers on its dashboard
are not byte-identical to what the command above produces. Use the chat endpoint
for any MTP acceptance measurement regardless.

### Shared-expert fusion requires a recent build [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#shared-expert-fusion-requires-a-recent-build "Copy link to this section")

`VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=1` is a request, not a guarantee:
vLLM gates the fused shared-expert path on its own eligibility check.
[vllm-project/vllm#53161](https://github.com/vllm-project/vllm/pull/53161),
merged as `de69e821`, added the heterogeneous path that fuses the native-FP8
shared expert into the MXFP4 routed-expert kernel. Current `:nightly` images
include it, so the flag takes effect. On any build older than `de69e821` the
check rejects this mixed FP4+FP8 checkpoint outright and the fusion
self-disables at startup — including the immutable tag pinned in the
reproduction table above, which predates the fix.

On a build that includes it, the fusion additionally requires gfx950 (MI355X),
tensor parallelism 8, data parallelism 1, no expert parallelism and no EPLB,
`--moe-backend aiter`, BF16 model dtype, and the DeepSeek-V4 block-128 FP8
shared-expert quantization config. Both arms here satisfy this. Data-parallel
attention does not, and keeps the unfused path.

Eligibility is also re-checked per invocation against AITER's tuned-config
coverage for the number of MoE input rows. Decode-sized batches are covered and
take the fused kernel; large prefill chunks fall back to the unfused path, so an
8K-input workload runs fused during decode and unfused during prefill.

Failures are silent and logged at debug level, so check the server log before
assuming the fused path executed rather than inferring it from the flag. The
line to look for is `Using AITER DeepSeek V4 heterogeneous MoE for CSV-covered MoE input rows`.

### How this differs from the Agentic sweep above [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#how-this-differs-from-the-agentic-sweep-above "Copy link to this section")

| Setting | Fixed-sequence 8K/1K | Agentic sweep |
| --- | --- | --- |
| Workload | ISL 8192 / OSL 1024, conc 4–512 | agentic-coding traces |
| `--gpu-memory-utilization` | `0.8` | `0.86` |
| Prefix caching | `--no-enable-prefix-caching` | `--enable-prefix-caching` |
| Speculation | none (STP) or real MTP, 2 tokens | real DSpark K6 for serving/eval; synthetic AL 3.77 for throughput |
| `--max-num-seqs` | not passed | per point: twice concurrency for TP8, concurrency for DPA8 |
| `--max-num-batched-tokens` | not passed | `8192` |

The Agentic lane's synthetic acceptance length is a benchmark-comparability
device. This lane never uses it: the STP arm has no draft at all, and the MTP
arm verifies against the real target.

### Provenance [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro\#provenance "Copy link to this section")

Validation for this configuration comes from InferenceX, not from this
repository — no MI355X benchmark was rerun here.

- InferenceX PR: [#2792](https://github.com/SemiAnalysisAI/InferenceX/pull/2792)
- STP script: [`dsv4_fp4_mi355x_vllm.sh`](https://github.com/SemiAnalysisAI/InferenceX/blob/7393456f925f4962fc9bb6438567e73f7ca12bf8/benchmarks/single_node/fixed_seq_len/dsv4_fp4_mi355x_vllm.sh)
- MTP script: [`dsv4_fp4_mi355x_vllm_mtp.sh`](https://github.com/SemiAnalysisAI/InferenceX/blob/7393456f925f4962fc9bb6438567e73f7ca12bf8/benchmarks/single_node/fixed_seq_len/dsv4_fp4_mi355x_vllm_mtp.sh)
- Config matrix: [`configs/amd-master.yaml`](https://github.com/SemiAnalysisAI/InferenceX/blob/7393456f925f4962fc9bb6438567e73f7ca12bf8/configs/amd-master.yaml)
- Successful sweep: [run 33538769698](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/33538769698),
which ran at commit `7a209b121932696b7efd437ac50d19c53efc7a94`. All eight
concurrency points passed on both arms, plus `lm-eval` GSM8K eval-only jobs at
concurrency 128 and 512. Commits after that point on the PR branch do not touch
either fixed-sequence script or these two config entries.
- ROCm DeepSeek-V4 MTP support: [vllm-project/vllm#43385](https://github.com/vllm-project/vllm/pull/43385)

Configurations qualified on specific hardware, layered on the baseline command. Unless marked Opt-in, a preset applies automatically on its hardware and strategy; pick Baseline in the builder to drop it.

B2002 presetsAgentX TP8 · AgentX DEP

AgentX TP8Opt-in [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro#preset-b200_agentx_tp "Copy link to this section")

Tensor Parallel · FP8 (0813) · Agentic (InferenceX AgentX)

TP8 on one 8-GPU B200 node with DSpark (six draft tokens), FlashInfer sparse MLA and a fixed 50 GiB KV cache per GPU; no host KV offload.

5 points · concurrency 1–14 · image vllm/vllm-openai:nightly-8e2beaa3…@sha256:3207cb99c0f5…

[Use this preset](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?hardware=b200&variant=default&strategy=single_node_tp&preset=b200_agentx_tp#recipe-builder) [InferenceX #4554](https://github.com/SemiAnalysisAI/InferenceX/pull/4554)

Runbook

The TP8 points of the B200 AgentX lane (`dsv4-fp4-b200-vllm-agentic-mtp` and its low-concurrency
companion, [SemiAnalysisAI/InferenceX#4554](https://github.com/SemiAnalysisAI/InferenceX/pull/4554)) serve the
0813 checkpoint with DSpark (six draft tokens) as one aggregated vLLM worker on one 8-GPU B200 node: TP8, no
expert parallelism, no host KV offload. Each GPU holds a fixed 50 GiB KV cache and `--max-num-seqs` equals the
concurrency.

Concurrency 4 is the low-latency variant: a 40 GiB KV cache, the `deep_select` sparse indexer top-k backend and
graph capture up to 16384 tokens. Concurrency 10 sets `--prefix-cache-retention-interval 32768` and
`--prefill-schedule-interval 64`, shards the indexer at 4096 rows (`indexer_tp_shard_min_rows`) and leaves
`VLLM_DSV4_MEGA_FP8_COMBINE` unset. Concurrency 4 and 10 were measured on a second pinned image, shown on
those points.

Left out of the command: the lane also exported `VLLM_PREFIX_CACHE_RETENTION_INTERVAL`, which vLLM removed in
v0.30.0 ( [vllm#55353](https://github.com/vllm-project/vllm/pull/55353)) in favour of the flag above, so it had
no effect on the image it ran on; and `--served-model-name`, which the builder replaces with the checkpoint ID.
The throughput points in InferenceX swap block verification for synthetic rejection at a committed
acceptance length so every point is measured at the same acceptance rate; the command does not set it.

AgentX DEPOpt-in [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro#preset-b200_agentx_dep "Copy link to this section")

Data + Expert Parallel · FP8 (0813) · Agentic (InferenceX AgentX)

Data-parallel ranks with expert parallelism and a Simple CPU KV tier behind a consistent-hash vLLM Router: DEP8 for concurrency 64 to 192, TP4 x DP2 at 32 and TP2 x DP4 at 48 and 64.

8 points · concurrency 32–192 · image vllm/vllm-openai:nightly-8e2beaa3…@sha256:3207cb99c0f5…

[Use this preset](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?hardware=b200&variant=default&strategy=single_node_dep&preset=b200_agentx_dep#recipe-builder) [InferenceX #4554](https://github.com/SemiAnalysisAI/InferenceX/pull/4554)

Runbook

The data-parallel points of the B200 AgentX lane (`dsv4-fp4-b200-vllm-agentic-mtp` and its low-concurrency
companion, [SemiAnalysisAI/InferenceX#4554](https://github.com/SemiAnalysisAI/InferenceX/pull/4554)) serve the
0813 checkpoint with DSpark (six draft tokens) as one engine on one 8-GPU B200 node: DEP8 (TP1 x DP8) for
concurrency 64 to 192, TP4 x DP2 at 32 and TP2 x DP4 at 48 and 64, all with expert parallelism and the Simple
CPU KV tier. Each rank gets 241.5 GB of host memory (1932 GB across the node), so size it to the machine.
`--max-num-seqs` is per DP rank, and `--max-num-batched-tokens` is an 8192-token prefill budget plus seven
verification slots per sequence. The TP4 x DP2 and TP2 x DP4 points leave `VLLM_DSV4_MEGA_FP8_COMBINE` unset.
TP2 x DP4 was measured on a second pinned image, shown on those points.

The lane fronts the server with vLLM Router 0.1.14 (`--policy consistent_hash`, `--intra-node-data-parallel-size`
equal to the server's DP size, as on the router tab), plus `--request-timeout-secs 14400` so long agentic
requests outlive the default and `--disable-retries` so a failed request is not replayed. Clients send a stable
per-conversation `X-Session-ID` so the router keeps a conversation on the rank that holds its prefix.

Left out of the command: `VLLM_PREFIX_CACHE_RETENTION_INTERVAL` (removed in vLLM v0.30.0,
[vllm#55353](https://github.com/vllm-project/vllm/pull/55353), so it had no effect), `--served-model-name`
(the builder replaces it with the checkpoint ID) and the router's Prometheus port. The throughput points in
InferenceX swap block verification for synthetic rejection at a committed acceptance length so every point is
measured at the same acceptance rate; the command does not set it.

MI355X2 presetsAgentX TP8 + monokernel · AgentX DPA8 + TP experts

AgentX TP8 + monokernelOpt-in [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro#preset-mi355x_agentx_tp "Copy link to this section")

Tensor Parallel · FP8 (0813) · Agentic coding (InferenceX AgentX)

Source reproduction: DSpark K6 and monokernel on eight MI355X GPUs; draft communication precision requires resolution.

9 points · concurrency 1–64 · image vllm/vllm-openai-rocm:nightly-e4a5b553… · pip Pillow · pip fastapi · pip uvicorn · model rev 72e1d3230f6c080a530b0a1d46f8eb4602340597

[Use this preset](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?hardware=mi355x&variant=default&strategy=single_node_tp&preset=mi355x_agentx_tp#recipe-builder) [InferenceX #4526](https://github.com/SemiAnalysisAI/InferenceX/pull/4526)

Runbook

This opt-in profile serves [DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
on one 8× MI355X node. The monokernel is enabled only for the TP8 arm;
[vLLM #61482](https://github.com/vllm-project/vllm/pull/61482) added this
DSpark-compatible path. These presets do not change the generic defaults.

**Qualification blocked:** the source enables nondefault INT4 QuickReduce
for draft collectives too. For example, 32 active K6 requests produce at
least 192 draft rows, making the BF16 attention-output reduction eligible
for INT4 communication in the pinned image. This conflicts with
[InferenceX's draft-precision rule](https://github.com/SemiAnalysisAI/InferenceX/blob/67de4b34ee1419b2a31c0e7200964a6e78015be4/CONTRIBUTING.md#draft-model-precision).
These are faithful source profiles, pending a source correction and
qualifying validation; they are not a production recommendation. Real
target verification and passing GSM8K do not resolve that precision issue.

InferenceX installs `Pillow fastapi uvicorn` before engine startup. When
using the pinned image interactively, install these prerequisites inside
the container, then run the generated Python command in that container:

```bash
uv pip install Pillow fastapi uvicorn
```

The generated Docker launch does not perform this setup step; provide the
dependencies in its container before using that launch form.

The source pins the target and tokenizer revisions, but supplies no separate
DSpark draft revision. DSpark loads the native draft from the same model ID
through the image's default mixed FP8/MXFP4 handling; no draft dtype or
quantization override is added. INT4 QuickReduce is shared by eligible
standard-path target and draft collectives, rather than being target-only.
The KV cache is FP8. The image is recorded as a tag, without a source-pinned
digest. Keep inherited environment settings consistent with the preset.

The generated serving commands use real target verification. For the
**InferenceX throughput sweep only**, merge the following keys into their
speculative config, retaining DSpark K6 and probabilistic drafting:

```json
{"rejection_sample_method":"synthetic","synthetic_acceptance_length":3.77}
```

`3.77` comes from the committed
[DeepSeek-V4-Pro thinking-on K6 golden curve](https://github.com/SemiAnalysisAI/InferenceX/blob/5ec3c995988e5d3632c1ff53e8ae39da3e799892/inferencex-e2e/infx/golden_al_distribution/dsv4-pro-0813-dspark.yaml).
Synthetic acceptance is a measurement control; do not use it for production
or accuracy evaluation. The generic Bench command is a smoke benchmark,
not an AgentX replay; reproduce AgentX with the linked InferenceX harness.

The TP8 scheduler caps are twice the listed client concurrency for AgentX
fan-out. No host-memory offload is enabled. The source's obsolete
`VLLM_PREFIX_CACHE_RETENTION_INTERVAL=32768` has no effect in this image;
the presets retain the effective CLI default of `0` (semantic checkpoints).

Evidence: [sweep 40260921924, attempt 3](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/40260921924/attempts/3)
for source head `882db2060239f4d849f8b1c93f3b8b192ad3637e` covers all twelve TP8/DPA
throughput points and two real-verification GSM8K evals. The current-head
[run 40626241537](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/40626241537)
only reuses that sweep; its performance/eval matrices are skipped.
Its actual CI merge `f301906060dcfd3b63ac6f77a735698f731f65b1` and the cited
head produce identical native recipe expansion for this lane.
This documentation change does not rerun GPU inference or establish private
agentic accuracy evaluation.

AgentX DPA8 + TP expertsOpt-in [Copy link to this section](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro#preset-mi355x_agentx_dpa "Copy link to this section")

DP Attention + Tensor Parallel · FP8 (0813) · Agentic coding (InferenceX AgentX)

TP1 attention / DP8 with tensor-sharded experts, DSpark K6 and session-affine routing; monokernel disabled.

3 points · concurrency 64–192 · image vllm/vllm-openai-rocm:nightly-e4a5b553… · pip Pillow · pip fastapi · pip uvicorn · pip vllm-router==0.1.14 · model rev 72e1d3230f6c080a530b0a1d46f8eb4602340597

[Use this preset](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?hardware=mi355x&variant=default&strategy=single_node_dpa_tp&preset=mi355x_agentx_dpa#recipe-builder) [InferenceX #4526](https://github.com/SemiAnalysisAI/InferenceX/pull/4526)

Runbook

This is the DP-attention arm of the
[TP8 profile](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro#preset-mi355x_agentx_tp), using the same checkpoint, image,
runtime prerequisites and real-versus-synthetic verification distinction.
The source qualification blocker described there remains unresolved.
Runtime flags are TP1/DP8 with no expert-parallel flag: experts remain
tensor-sharded across the eight ranks. The source's matrix label TP8/EP1
describes the aggregate topology, not the attention TP argument.
Monokernel remains disabled (the image default); TP8-only monokernel
eligibility does not extend to this arm.

Each DP scheduler caps sequences at the listed client concurrency.
The measured prefill interval is `8`; the `16384` long-prefill threshold
exceeds the `8192` token budget and does not bind.

For exact source routing, replace the generic router companion with this
pinned setup in another shell on the engine's host/container network:

```bash
uv pip install vllm-router==0.1.14
vllm-router \
  --host 0.0.0.0 --port 8000 \
  --worker-urls http://localhost:8100 \
  --intra-node-data-parallel-size 8 \
  --policy consistent_hash \
  --request-timeout-secs 14400 \
  --disable-retries
```

Clients connect to the router on port `8000`, retaining an `X-Session-ID`
across turns of each conversation. InferenceX maps correlation IDs to
this header; `AIPERF_HTTP_X_SESSION_ID_FROM_CORRELATION_ID=1` is a benchmark
client setting, not an engine environment variable.