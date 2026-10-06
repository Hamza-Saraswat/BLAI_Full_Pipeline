[Skip to content](https://docs.vllm.ai/en/stable/features/quantization/quark/#amd-quark)

[Provide feedback](https://github.com/vllm-project/vllm/issues/new?template=100-documentation.yml&title=%5BDocs%5D%20Feedback%20for%20%60%2Fen%2Fstable%2Ffeatures%2Fquantization%2Fquark%2F%60&body=%F0%9F%93%84%20**Reference%3A**%0Ahttps%3A%2F%2Fdocs.vllm.ai%2Fen%2Fstable%2Ffeatures%2Fquantization%2Fquark%2F%0A%0A%F0%9F%93%9D%20**Feedback%3A**%0A_Your%20response_ "Provide feedback") [Edit this page](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/quark.md "Edit this page")

# AMD Quark [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#amd-quark "Permanent link")

Quantization can effectively reduce memory and bandwidth usage, accelerate computation and improve throughput while with minimal accuracy loss. vLLM can leverage [Quark](https://quark.docs.amd.com/latest/), the flexible and powerful quantization toolkit, to produce performant quantized models to run on AMD GPUs. Quark has specialized support for quantizing large language models with weight, activation and kv-cache quantization and cutting-edge quantization algorithms like AWQ, GPTQ, Rotation and SmoothQuant.

## Quark Installation [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#quark-installation "Permanent link")

Before quantizing models, you need to install Quark. The latest release of Quark can be installed with pip:

```
pip install amd-quark
```

You can refer to [Quark installation guide](https://quark.docs.amd.com/latest/install.html) for more installation details.

Additionally, install `vllm` and `lm-evaluation-harness` for evaluation:

```
pip install vllm "lm-eval[api]>=0.4.12"
```

## Quantization Process [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#quantization-process "Permanent link")

After installing Quark, we will use an example to illustrate how to use Quark. The Quark quantization process can be listed for 5 steps as below:

1. Load the model
2. Prepare the calibration dataloader
3. Set the quantization configuration
4. Quantize the model and export
5. Evaluation in vLLM

### 1\. Load the Model [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#1-load-the-model "Permanent link")

Quark uses [Transformers](https://huggingface.co/docs/transformers/en/index) to fetch model and tokenizer.

Code

```
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "meta-llama/Llama-2-70b-chat-hf"
MAX_SEQ_LEN = 512

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    dtype="auto",
)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, model_max_length=MAX_SEQ_LEN)
tokenizer.pad_token = tokenizer.eos_token
```

### 2\. Prepare the Calibration Dataloader [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#2-prepare-the-calibration-dataloader "Permanent link")

Quark uses the [PyTorch Dataloader](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html) to load calibration data. For more details about how to use calibration datasets efficiently, please refer to [Adding Calibration Datasets](https://quark.docs.amd.com/latest/pytorch/calibration_datasets.html).

Code

```
from datasets import load_dataset
from torch.utils.data import DataLoader

BATCH_SIZE = 1
NUM_CALIBRATION_DATA = 512

# Load the dataset and get calibration data.
dataset = load_dataset("mit-han-lab/pile-val-backup", split="validation")
text_data = dataset["text"][:NUM_CALIBRATION_DATA]

tokenized_outputs = tokenizer(
    text_data,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=MAX_SEQ_LEN,
)
calib_dataloader = DataLoader(
    tokenized_outputs['input_ids'],
    batch_size=BATCH_SIZE,
    drop_last=True,
)
```

### 3\. Set the Quantization Configuration [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#3-set-the-quantization-configuration "Permanent link")

We need to set the quantization configuration, you can check [quark config guide](https://quark.docs.amd.com/latest/pytorch/user_guide_config_description.html) for further details. Here we use FP8 per-tensor quantization on weight, activation, kv-cache and the quantization algorithm is AutoSmoothQuant.

Note

Note the quantization algorithm needs a JSON config file and the config file is located in [Quark PyTorch examples](https://quark.docs.amd.com/latest/pytorch/pytorch_examples.html), under the directory `examples/torch/language_modeling/llm_ptq/models`. For example, AutoSmoothQuant config file for Llama is `examples/torch/language_modeling/llm_ptq/models/llama/autosmoothquant_config.json`.

Code

```
from quark.torch.quantization import (Config, QuantizationConfig,
                                    FP8E4M3PerTensorSpec,
                                    load_quant_algo_config_from_file)

# Define fp8/per-tensor/static spec.
FP8_PER_TENSOR_SPEC = FP8E4M3PerTensorSpec(
    observer_method="min_max",
    is_dynamic=False,
).to_quantization_spec()

# Define global quantization config, input tensors and weight apply FP8_PER_TENSOR_SPEC.
global_quant_config = QuantizationConfig(
    input_tensors=FP8_PER_TENSOR_SPEC,
    weight=FP8_PER_TENSOR_SPEC,
)

# Define quantization config for kv-cache layers, output tensors apply FP8_PER_TENSOR_SPEC.
KV_CACHE_SPEC = FP8_PER_TENSOR_SPEC
kv_cache_layer_names_for_llama = ["*k_proj", "*v_proj"]
kv_cache_quant_config = {
    name: QuantizationConfig(
        input_tensors=global_quant_config.input_tensors,
        weight=global_quant_config.weight,
        output_tensors=KV_CACHE_SPEC,
    )
    for name in kv_cache_layer_names_for_llama
}
layer_quant_config = kv_cache_quant_config.copy()

# Define algorithm config by config file.
LLAMA_AUTOSMOOTHQUANT_CONFIG_FILE = "examples/torch/language_modeling/llm_ptq/models/llama/autosmoothquant_config.json"
algo_config = load_quant_algo_config_from_file(LLAMA_AUTOSMOOTHQUANT_CONFIG_FILE)

EXCLUDE_LAYERS = ["lm_head"]
quant_config = Config(
    global_quant_config=global_quant_config,
    layer_quant_config=layer_quant_config,
    kv_cache_quant_config=kv_cache_quant_config,
    exclude=EXCLUDE_LAYERS,
    algo_config=algo_config,
)
```

### 4\. Quantize the Model and Export [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#4-quantize-the-model-and-export "Permanent link")

Then we can apply the quantization. After quantizing, we need to freeze the quantized model first before exporting. Note that we need to export model with format of HuggingFace `safetensors`, you can refer to [HuggingFace format exporting](https://quark.docs.amd.com/latest/pytorch/export/quark_export_hf.html) for more exporting format details.

Code

```
import torch
from quark.torch import ModelQuantizer, ModelExporter
from quark.torch.export import ExporterConfig, JsonExporterConfig

# Apply quantization.
quantizer = ModelQuantizer(quant_config)
quant_model = quantizer.quantize_model(model, calib_dataloader)

# Freeze quantized model to export.
freezed_model = quantizer.freeze(model)

# Define export config.
LLAMA_KV_CACHE_GROUP = ["*k_proj", "*v_proj"]
export_config = ExporterConfig(json_export_config=JsonExporterConfig())
export_config.json_export_config.kv_cache_group = LLAMA_KV_CACHE_GROUP

# Model: Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant
EXPORT_DIR = MODEL_ID.split("/")[1] + "-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant"
exporter = ModelExporter(config=export_config, export_dir=EXPORT_DIR)
with torch.no_grad():
    exporter.export_safetensors_model(
        freezed_model,
        quant_config=quant_config,
        tokenizer=tokenizer,
    )
```

### 5\. Evaluation in vLLM [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#5-evaluation-in-vllm "Permanent link")

Now, you can load and run the Quark quantized model directly through the LLM entrypoint:

Code

```
from vllm import LLM, SamplingParams

# Sample prompts.
prompts = [\
    "Hello, my name is",\
    "The president of the United States is",\
    "The capital of France is",\
    "The future of AI is",\
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

# Create an LLM.
llm = LLM(
    model="Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant",
    kv_cache_dtype="fp8",
    quantization="quark",
)
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
print("\nGenerated Outputs:\n" + "-" * 60)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt:    {prompt!r}")
    print(f"Output:    {generated_text!r}")
    print("-" * 60)
```

Or, you can use `lm_eval` to evaluate accuracy:

```
lm_eval --model vllm \
  --model_args pretrained=Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant,kv_cache_dtype='fp8',quantization='quark' \
  --tasks gsm8k
```

## Quark Quantization Script [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#quark-quantization-script "Permanent link")

In addition to the example of Python API above, Quark also offers a [quantization script](https://quark.docs.amd.com/latest/pytorch/example_quark_torch_llm_ptq.html) to quantize large language models more conveniently. It supports quantizing models with variety of different quantization schemes and optimization algorithms. It can export the quantized model and run evaluation tasks on the fly. With the script, the example above can be:

```
python3 quantize_quark.py --model_dir meta-llama/Llama-2-70b-chat-hf \
                          --output_dir /path/to/output \
                          --quant_scheme w_fp8_a_fp8 \
                          --kv_cache_dtype fp8 \
                          --quant_algo autosmoothquant \
                          --num_calib_data 512 \
                          --model_export hf_format \
                          --tasks gsm8k
```

## Using OCP MX (MXFP4, MXFP6) models [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#using-ocp-mx-mxfp4-mxfp6-models "Permanent link")

vLLM supports loading MXFP4 and MXFP6 models quantized offline through AMD Quark, compliant with [Open Compute Project (OCP) specification](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf).

The scheme currently only supports dynamic quantization for activations.

Example usage, after installing the latest AMD Quark release:

```
vllm serve fxmarty/qwen_1.5-moe-a2.7b-mxfp4 --tensor-parallel-size 1
# or, for a model using fp6 activations and fp4 weights:
vllm serve fxmarty/qwen1.5_moe_a2.7b_chat_w_fp4_a_fp6_e2m3 --tensor-parallel-size 1
```

A simulation of the matrix multiplication execution in MXFP4/MXFP6 can be run on devices that do not support OCP MX operations natively (e.g. AMD Instinct MI325, MI300 and MI250), dequantizing weights from FP4/FP6 to half precision on the fly, using a fused kernel. This is useful e.g. to evaluate FP4/FP6 models using vLLM, or alternatively to benefit from the ~2.5-4x memory savings (compared to float16 and bfloat16).

To generate offline models quantized using MXFP4 data type, the easiest approach is to use AMD Quark's [quantization script](https://quark.docs.amd.com/latest/pytorch/example_quark_torch_llm_ptq.html), as an example:

```
python quantize_quark.py --model_dir Qwen/Qwen1.5-MoE-A2.7B-Chat \
    --quant_scheme w_mxfp4_a_mxfp4 \
    --output_dir qwen_1.5-moe-a2.7b-mxfp4 \
    --skip_evaluation \
    --model_export hf_format \
    --group_size 32
```

The current integration supports [all combination of FP4, FP6\_E3M2, FP6\_E2M3](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/utils/ocp_mx_utils.py) used for either weights or activations.

## Using Quark Quantized layerwise Auto Mixed Precision (AMP) Models [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#using-quark-quantized-layerwise-auto-mixed-precision-amp-models "Permanent link")

vLLM also supports loading layerwise mixed precision model quantized using AMD Quark. Currently, mixed scheme of {MXFP4, FP8} is supported, where FP8 here denotes for FP8 per-tensor scheme. More mixed precision schemes are planned to be supported in a near future, including

- Unquantized Linear and/or MoE layer(s) as an option for each layer, i.e., mixed of {MXFP4, FP8, BF16/FP16}
- MXFP6 quantization extension, i.e., {MXFP4, MXFP6, FP8, BF16/FP16}

Although one can maximize serving throughput using the lowest precision supported on a given device (e.g. MXFP4 for AMD Instinct MI355, FP8 for AMD Instinct MI300), these aggressive schemes can be detrimental to accuracy recovering from quantization on target tasks. Mixed precision allows to strike a balance between maximizing accuracy and throughput.

There are two steps to generate and deploy a mixed precision model quantized with AMD Quark, as shown below.

### 1\. Quantize a model using mixed precision in AMD Quark [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#1-quantize-a-model-using-mixed-precision-in-amd-quark "Permanent link")

Firstly, the layerwise mixed-precision configuration for a given LLM model is searched and then quantized using AMD Quark. We will provide a detailed tutorial with Quark APIs later.

As examples, we provide some ready-to-use quantized mixed precision model to show the usage in vLLM and the accuracy benefits. They are:

- amd/Llama-2-70b-chat-hf-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8
- amd/Mixtral-8x7B-Instruct-v0.1-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8
- amd/Qwen3-8B-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8

### 2\. inference the quantized mixed precision model in vLLM [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#2-inference-the-quantized-mixed-precision-model-in-vllm "Permanent link")

Models quantized with AMD Quark using mixed precision can natively be reload in vLLM, and e.g. evaluated using lm-evaluation-harness as follows:

```
lm_eval --model vllm \
    --model_args pretrained=amd/Llama-2-70b-chat-hf-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8,tensor_parallel_size=4,dtype=auto,gpu_memory_utilization=0.8,trust_remote_code=False \
    --tasks mmlu \
    --batch_size auto
```

## Online Quantization [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#online-quantization "Permanent link")

All the workflows above are _offline_ quantization: you run a script, write a new quantized checkpoint to disk, and later load it for serving. This produces the most accurate and smallest checkpoints because it can run accuracy-recovery algorithms (rotation, SmoothQuant, GPTQ, AWQ) during export, but it requires a separate quantization step and a second copy of the model on disk.

_Online_ quantization instead quantizes the weights at load time, directly from a high-precision checkpoint, and offers several advantages over the offline flow:

- **No export step** — serve directly from the original `bf16`/`fp16` checkpoint; no separate quantization run before deployment.
- **No extra disk footprint** — nothing new is written to disk, so there is no second copy of the model to store or manage.
- **No calibration data** — activations are scaled dynamically at runtime, so no calibration dataset is needed.
- **Fast iteration** — switch schemes or per-layer selections instantly by changing a config, without re-exporting.

### vLLM online quantization [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#vllm-online-quantization "Permanent link")

vLLM has [built-in online quantization](https://docs.vllm.ai/en/stable/features/quantization/online/) that skips the export step: it loads an ordinary high-precision (`bf16`) checkpoint and quantizes each layer's weights to schemes such as FP8 or MXFP4 at load time, without a pre-quantized checkpoint or calibration data. No new checkpoint is written to disk. See [Online Quantization](https://docs.vllm.ai/en/stable/features/quantization/online/) for the supported schemes and configuration.

### Quark online quantization [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#quark-online-quantization "Permanent link")

AMD Quark provides its own online path, exposed as the `quark_online` quantization backend, for users who want parity with Quark's offline export and Quark's per-layer mixed-precision configs. Like vLLM's built-in online quantization, it quantizes weights inside the weight-loading hook just before serving and writes no new checkpoint.

Its quant math is aligned byte-for-byte with Quark's offline export, so what you validate online is what you get offline. Use it to _find_ the scheme and per-layer selection you want.

Compared to vLLM's built-in online quantization, the `quark_online` plugin adds:

- **Flexible config parsing** — a terse config expands into Quark's verbose per-layer config, delegating all per-layer matching to a real `QuarkConfig`.
- **Per-layer / mixed schemes** — dispatch a different method per layer (e.g. MXFP4 experts with FP8 attention on an MoE model). Each online method subclasses the matching offline scheme, so a load-time quantized layer runs the identical inference kernel as an offline one.
- **Re-quantizing an already-quantized checkpoint** — an FP8 block-scale checkpoint (e.g. DeepSeek-R1) is dequantized and re-quantized to a target scheme layer-locally at load time, with no new checkpoint.

The plugin ships in AMD Quark — no fork of vLLM, no patched checkpoint format; see the [Quark documentation](https://quark.docs.amd.com/latest/) for details. Three presets ship ready to use:

| Preset key | Scheme |
| --- | --- |
| `ptpc_fp8` | FP8 E4M3, per-channel weight + dynamic per-token activation |
| `mxfp4` | MXFP4, per-group (group size 32) with E8M0 block scale |
| `linear_ptpc_fp8_moe_mxfp4` | Mixed: attention in FP8, MoE experts in MXFP4 |

### Python API [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#python-api "Permanent link")

```
from vllm import LLM, SamplingParams
from quark.online_quantization.vllm import HF_QUANTIZATION_CONFIGS

llm = LLM(
    model="Qwen/Qwen3-30B-A3B-Thinking-2507",
    quantization="quark_online",
    hf_overrides=HF_QUANTIZATION_CONFIGS["ptpc_fp8"],
    enforce_eager=True,
    tensor_parallel_size=1,
)
out = llm.generate(["The capital of France is"], SamplingParams(temperature=0.0, max_tokens=100))
print(out)
```

### Native vLLM CLI [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#native-vllm-cli "Permanent link")

```
export VLLM_PLUGINS="${VLLM_PLUGINS:-quark_online_quant}"
ONLINE_QUANT_CONFIG='{"online_quant_config": {"global_quant_config": "ptpc_fp8", "exclude_layer": ["lm_head"]}}'

vllm serve Qwen/Qwen3-8B \
  --trust-remote-code \
  --tensor-parallel-size 1 \
  --additional-config "$ONLINE_QUANT_CONFIG"
```

### Re-quantizing an offline checkpoint [¶](https://docs.vllm.ai/en/stable/features/quantization/quark/\#re-quantizing-an-offline-checkpoint "Permanent link")

No extra arguments — the same `hf_overrides` detects the checkpoint's existing config and merges it automatically:

```
llm = LLM(
    model="deepseek-ai/DeepSeek-R1",           # ships quant_method: "fp8"
    quantization="quark_online",
    hf_overrides=HF_QUANTIZATION_CONFIGS["ptpc_fp8"],
    tensor_parallel_size=8,
)
```

The plugin can be disabled with `QUARK_DISABLE_VLLM_PLUGIN=1`, and it steps aside automatically if another platform plugin (e.g. ATOM) has already taken over the backend.

Back to top

Versions[latest](https://docs.vllm.ai/en/latest/features/quantization/quark/)**[stable](https://docs.vllm.ai/en/stable/features/quantization/quark/)**[v0.31.0](https://docs.vllm.ai/en/v0.31.0/features/quantization/quark/)[v0.30.0](https://docs.vllm.ai/en/v0.30.0/features/quantization/quark/)[v0.29.0](https://docs.vllm.ai/en/v0.29.0/features/quantization/quark/)[v0.28.0](https://docs.vllm.ai/en/v0.28.0/features/quantization/quark/)[v0.27.1](https://docs.vllm.ai/en/v0.27.1/features/quantization/quark/)[v0.27.0](https://docs.vllm.ai/en/v0.27.0/features/quantization/quark/)[v0.26.0](https://docs.vllm.ai/en/v0.26.0/features/quantization/quark/)[v0.25.1](https://docs.vllm.ai/en/v0.25.1/features/quantization/quark/)[v0.25.0](https://docs.vllm.ai/en/v0.25.0/features/quantization/quark/)[v0.24.0](https://docs.vllm.ai/en/v0.24.0/features/quantization/quark/)[v0.23.0](https://docs.vllm.ai/en/v0.23.0/features/quantization/quark/)[v0.22.1](https://docs.vllm.ai/en/v0.22.1/features/quantization/quark/)[v0.22.0](https://docs.vllm.ai/en/v0.22.0/features/quantization/quark/)[v0.21.0](https://docs.vllm.ai/en/v0.21.0/features/quantization/quark/)[v0.20.2](https://docs.vllm.ai/en/v0.20.2/features/quantization/quark/)[v0.20.1](https://docs.vllm.ai/en/v0.20.1/features/quantization/quark/)[v0.20.0](https://docs.vllm.ai/en/v0.20.0/features/quantization/quark/)[v0.19.1](https://docs.vllm.ai/en/v0.19.1/features/quantization/quark/)[v0.19.0](https://docs.vllm.ai/en/v0.19.0/features/quantization/quark/)[v0.18.2](https://docs.vllm.ai/en/v0.18.2/features/quantization/quark/)[v0.18.1](https://docs.vllm.ai/en/v0.18.1/features/quantization/quark/)[v0.18.0](https://docs.vllm.ai/en/v0.18.0/features/quantization/quark/)[v0.17.1](https://docs.vllm.ai/en/v0.17.1/features/quantization/quark/)[v0.17.0](https://docs.vllm.ai/en/v0.17.0/features/quantization/quark/)[v0.16.0](https://docs.vllm.ai/en/v0.16.0/features/quantization/quark/)[v0.15.1](https://docs.vllm.ai/en/v0.15.1/features/quantization/quark/)[v0.15.0](https://docs.vllm.ai/en/v0.15.0/features/quantization/quark/)[v0.14.1](https://docs.vllm.ai/en/v0.14.1/features/quantization/quark/)[v0.14.0](https://docs.vllm.ai/en/v0.14.0/features/quantization/quark/)[v0.13.0](https://docs.vllm.ai/en/v0.13.0/features/quantization/quark/)[v0.12.0](https://docs.vllm.ai/en/v0.12.0/features/quantization/quark/)[v0.11.2](https://docs.vllm.ai/en/v0.11.2/features/quantization/quark/)[v0.11.1](https://docs.vllm.ai/en/v0.11.1/features/quantization/quark/)[v0.11.0](https://docs.vllm.ai/en/v0.11.0/features/quantization/quark/)[v0.10.2](https://docs.vllm.ai/en/v0.10.2/features/quantization/quark/)[v0.10.1.1](https://docs.vllm.ai/en/v0.10.1.1/features/quantization/quark/)[v0.10.1](https://docs.vllm.ai/en/v0.10.1/features/quantization/quark/)[v0.10.0](https://docs.vllm.ai/en/v0.10.0/features/quantization/quark/)[v0.9.2](https://docs.vllm.ai/en/v0.9.2/features/quantization/quark/)[v0.9.1](https://docs.vllm.ai/en/v0.9.1/features/quantization/quark/)[v0.9.0.1](https://docs.vllm.ai/en/v0.9.0.1/features/quantization/quark/)[v0.9.0](https://docs.vllm.ai/en/v0.9.0/features/quantization/quark/)[v0.8.5.post1](https://docs.vllm.ai/en/v0.8.5.post1/features/quantization/quark/)[v0.8.5](https://docs.vllm.ai/en/v0.8.5/features/quantization/quark/)[v0.8.4](https://docs.vllm.ai/en/v0.8.4/features/quantization/quark/)[v0.8.3](https://docs.vllm.ai/en/v0.8.3/features/quantization/quark/)[v0.8.2](https://docs.vllm.ai/en/v0.8.2/features/quantization/quark/)[v0.8.1](https://docs.vllm.ai/en/v0.8.1/features/quantization/quark/)[v0.8.0](https://docs.vllm.ai/en/v0.8.0/features/quantization/quark/)[v0.7.3](https://docs.vllm.ai/en/v0.7.3/features/quantization/quark/)[v0.7.2](https://docs.vllm.ai/en/v0.7.2/features/quantization/quark/)[v0.7.1](https://docs.vllm.ai/en/v0.7.1/features/quantization/quark/)[v0.7.0](https://docs.vllm.ai/en/v0.7.0/features/quantization/quark/)[v0.6.6.post1](https://docs.vllm.ai/en/v0.6.6.post1/features/quantization/quark/)[v0.6.6](https://docs.vllm.ai/en/v0.6.6/features/quantization/quark/)[v0.6.5](https://docs.vllm.ai/en/v0.6.5/features/quantization/quark/)[v0.6.4.post1](https://docs.vllm.ai/en/v0.6.4.post1/features/quantization/quark/)[v0.6.4](https://docs.vllm.ai/en/v0.6.4/features/quantization/quark/)[v0.6.3.post1](https://docs.vllm.ai/en/v0.6.3.post1/features/quantization/quark/)[v0.6.3](https://docs.vllm.ai/en/v0.6.3/features/quantization/quark/)[v0.6.2](https://docs.vllm.ai/en/v0.6.2/features/quantization/quark/)[v0.6.1.post2](https://docs.vllm.ai/en/v0.6.1.post2/features/quantization/quark/)[v0.6.1.post1](https://docs.vllm.ai/en/v0.6.1.post1/features/quantization/quark/)[v0.6.1](https://docs.vllm.ai/en/v0.6.1/features/quantization/quark/)[v0.6.0](https://docs.vllm.ai/en/v0.6.0/features/quantization/quark/)[v0.5.5](https://docs.vllm.ai/en/v0.5.5/features/quantization/quark/)[v0.5.4](https://docs.vllm.ai/en/v0.5.4/features/quantization/quark/)[v0.5.3.post1](https://docs.vllm.ai/en/v0.5.3.post1/features/quantization/quark/)[v0.5.3](https://docs.vllm.ai/en/v0.5.3/features/quantization/quark/)[v0.5.2](https://docs.vllm.ai/en/v0.5.2/features/quantization/quark/)[v0.5.1](https://docs.vllm.ai/en/v0.5.1/features/quantization/quark/)[v0.5.0.post1](https://docs.vllm.ai/en/v0.5.0.post1/features/quantization/quark/)[v0.5.0](https://docs.vllm.ai/en/v0.5.0/features/quantization/quark/)[v0.4.3](https://docs.vllm.ai/en/v0.4.3/features/quantization/quark/)[v0.4.2](https://docs.vllm.ai/en/v0.4.2/features/quantization/quark/)[v0.4.1](https://docs.vllm.ai/en/v0.4.1/features/quantization/quark/)[v0.4.0.post1](https://docs.vllm.ai/en/v0.4.0.post1/features/quantization/quark/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/vllm/?utm_source=vllm&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/vllm/builds/?utm_source=vllm&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=vllm&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=vllm&utm_content=flyout)

Ask AI