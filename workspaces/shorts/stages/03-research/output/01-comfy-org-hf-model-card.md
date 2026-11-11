# Source: https://huggingface.co/Comfy-Org/MiniMax-H3-Image
# Fetched: 2026-11-11 via hermes web_extract

# MiniMax H3 Image

Repackaged model files for ComfyUI.

Original model repository: [https://huggingface.co/MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)

## Prompt Enhancer

For prompt enhancement, we recommend to use the model `qwen3.5_9b_w4a8_gptq` with the Generate Text node.

* * *

Place the files in the following folders:

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── minimax_h3_image_pruned_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3.5_9b_w4a8_gptq.safetensors
│   │   ├── qwen3vl_32b_minimax_h3_int8_convrot.safetensors
│   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
│   ├── 📂 vae/
│   │   └── minimax_h3_image_vae_fp16.safetensors
```

## License

Note [MiniMax H3 Image license agreement](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE) is different from the original MiniMax H3 license:

> You shall obtain a separate, prior written authorization from MiniMax by sending a request through [https://platform.minimax.io/license](https://platform.minimax.io/license), if the Annualized Revenue of you and/or your affiliates exceeds 1 Million USD, or, you provide Hosted Service(s) to any Third Parties.

## Workflows

| Workflow | Thumb |
| :-: | :-: |
| [MiniMax-H3-Image: Image Edit](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_edit.json) | [![MiniMax-H3-Image: Image Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_edit-1.webp)](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_edit.json) |
| [MiniMax-H3-Image: Text to Image](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_t2i.json) | [![MiniMax-H3-Image: Text to Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_t2i-1.webp)](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_t2i.json) |

Downloads last month351,803

Inference Providers [NEW](https://huggingface.co/docs/inference-providers)

[Text-to-Image](https://huggingface.co/tasks/text-to-image "Learn more about text-to-image")

This model isn't deployed by any Inference Provider. [🙋Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=Comfy-Org/MiniMax-H3-Image&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5BComfy-Org%2FMiniMax-H3-Image%5D(%2FComfy-Org%2FMiniMax-H3-Image)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A(optional)%20Which%20providers%20are%20you%20interested%20in%3F%20(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6)%0A)

## Model tree for Comfy-Org/MiniMax-H3-Image

Base model

[MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)

Finetuned

[MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)

Finetuned

( [11](https://huggingface.co/models?other=base_model:finetune:MiniMaxAI/MiniMax-H3-Image))

this model

Quantizations

[2 models](https://huggingface.co/models?other=base_model:quantized:Comfy-Org/MiniMax-H3-Image)

## Space using Comfy-Org/MiniMax-H3-Image1

Inference providers allow you to run inference using different serverless providers.

StripeM-Inner
