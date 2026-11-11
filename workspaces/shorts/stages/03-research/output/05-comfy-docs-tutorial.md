# Source: https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image
# Fetched: 2026-11-11 via hermes web_extract

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.comfy.org/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image#content-area)

**MiniMax-H3-Image** is MiniMax’s open-weights image model, and one checkpoint covers both text to image and image editing. The diffusion transformer is 33.1B parameters in BF16, distilled to a 6-step sampler with no CFG. Output is native at about 16 MP, so a 4096 x 4096 image is a single pass rather than an upscale chain.**Related links**

- [MiniMaxAI/MiniMax-H3-Image (Hugging Face)](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image): official model card and weights
- [MiniMax-H3-Image (ModelScope)](https://modelscope.cn/models/minimax/MiniMax-H3-Image): official mirror for mainland China
- [MiniMax-AI/MiniMax-H3-Image (GitHub)](https://github.com/MiniMax-AI/MiniMax-H3-Image): official examples and skills
- [Comfy-Org/MiniMax-H3-Image (Hugging Face)](https://huggingface.co/Comfy-Org/MiniMax-H3-Image): diffusion model and image VAE
- [Comfy-Org/MiniMax-H3 (Hugging Face)](https://huggingface.co/Comfy-Org/MiniMax-H3): Qwen3-VL-32B text encoder used by this model
- [MiniMaxAI/MiniMax-H3-Image-PE (Hugging Face)](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE): official prompt expander

## [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#key-features)  Key features

- **Text to image and editing in one checkpoint**: no separate edit model or adapter to load
- **6-step sampling**: guidance is fixed at 1, so there is no CFG pass and no negative prompt
- **About 16 MP natively**: 4096 x 4096 up to 6272 x 2688 without an upscale pass
- **Multiple references**: up to 16 input images, addressed as `<Picture 1>` upwards in the prompt
- **Optional prompt expander**: turns a short request into the detailed caption the model reads best
- **Open weights**: full local control in ComfyUI

- Local users

- Cloud users


Make sure your ComfyUI is updated.

- [Download ComfyUI](https://www.comfy.org/download)
- [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template).
If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

1. You are not using the latest ComfyUI version (Nightly version)
2. Some nodes failed to import at startup

- [Cloud](https://cloud.comfy.org/) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#templates)  Templates

Two template Workflows ship with the model. Both need ComfyUI **0.45.0+** and template pack **0.11.104+**.

### [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#image_minimax_h3_image_t2i)  MiniMax-H3-Image Text to Image

Generate an image from a text prompt. The template opens at 4 MP on a square canvas, deliberately below the model’s native resolution so low-VRAM machines do not run out of memory. Raise the size with the resolution selector when the GPU has room.![MiniMax-H3-Image text to image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_t2i-1.webp)

[**Download Workflow** \\
\\
Download JSON or search “MiniMax-H3-Image: Text to Image” in Template Library](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_t2i.json)

### [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#image_minimax_h3_image_edit)  MiniMax-H3-Image Image Edit

Edit a picture by describing the change. The template loads the source as `<Picture 1>`, builds a reference-aware caption from your instruction, and finishes with a before/after comparison node.![MiniMax-H3-Image image edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_edit-1.webp)

[**Download Workflow** \\
\\
Download JSON or search “MiniMax-H3-Image: Image Edit” in Template Library](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_edit.json)

**Input materials**The template ships with one source picture, loaded as `<Picture 1>` in its `LoadImage` node.

[**vintage\_yellow\_taxi.png** \\
\\
Source image the template edits](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/vintage_yellow_taxi.png)

## [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#model-downloads)  Model downloads

Four files go under `ComfyUI/models`. All of them come from Comfy-Org mirror repositories.

[**Diffusion model: minimax\_h3\_image\_pruned\_int8\_convrot.safetensors** \\
\\
Pruned INT8 DiT, 21 GB. Place in `ComfyUI/models/diffusion_models/`](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/blob/main/diffusion_models/minimax_h3_image_pruned_int8_convrot.safetensors)

[**Text encoder: qwen3vl\_32b\_minimax\_h3\_int8\_convrot.safetensors** \\
\\
Qwen3-VL-32B, INT8, 25.28 GB. Place in `ComfyUI/models/text_encoders/`](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors)

[**Prompt expander: qwen3.5\_9b\_w4a8\_gptq.safetensors** \\
\\
Qwen3.5 9B W4A8, 7.34 GB. Place in `ComfyUI/models/text_encoders/`](https://huggingface.co/Comfy-Org/Qwen3.5/blob/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors)

[**VAE: minimax\_h3\_image\_vae\_fp16.safetensors** \\
\\
Image VAE, FP16, 1.17 GB. Place in `ComfyUI/models/vae/`](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/blob/main/vae/minimax_h3_image_vae_fp16.safetensors)

**Model Storage Location**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── minimax_h3_image_pruned_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3vl_32b_minimax_h3_int8_convrot.safetensors
│   │   └── qwen3.5_9b_w4a8_gptq.safetensors
│   └── 📂 vae/
│       └── minimax_h3_image_vae_fp16.safetensors
```

## [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#sampling-and-canvas-size)  Sampling and canvas size

Both templates ship the distilled schedule:

| Setting | Value |
| --- | --- |
| Sampler | euler |
| Scheduler | simple |
| Steps | 6 |
| Guidance (CFG) | 1 |
| Denoise | 1 |

With guidance at 1 there is no classifier-free guidance pass, so the templates carry no negative prompt. Write everything you want, including things to avoid, into the positive prompt.Native output is about 16 MP. Every edge is generated on a multiple of 32 px, and any width and height are accepted. These sizes cover the common ratios:

| Aspect ratio | Size (width x height) |
| --- | --- |
| 1:1 | 4096 x 4096 |
| 4:3 | 4736 x 3552 |
| 3:4 | 3552 x 4736 |
| 3:2 | 5024 x 3360 |
| 2:3 | 3360 x 5024 |
| 16:9 | 5472 x 3072 |
| 9:16 | 3072 x 5472 |
| 21:9 | 6272 x 2688 |

Smaller canvases work too and cost less time. In the text-to-image template the resolution selector sets the aspect ratio and the target megapixels separately, so 4 MP is a starting point rather than a limit.

## [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#reference-images-in-image-editing)  Reference images in image editing

The image editing template sends the source image to the model as `<Picture 1>`. Additional images are labelled in order, `<Picture 2>`, `<Picture 3>`, up to 16 references, and the prompt addresses each one by its label. The first picture is the one being edited; the rest supply identity, props, materials, or composition. A short instruction is enough, for example replacing the vehicle in `<Picture 1>` with the one in `<Picture 2>`.To add a reference, place another `Load Image` node in the workflow and connect it to both the prompt generation step and the conditioning node. Reference images need no preparation: the template rounds the source to a multiple of 32 px, and ComfyUI scales the internal copies itself, a 1024 px short edge for the vision side and a short edge clamped between 1024 and 2048 px for the VAE side, both on the 32 px grid.If an edit runs out of memory, enable the `Resize Image/Mask` node in the template and lower its megapixels before sampling.

## [​](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image\#prompt-expander)  Prompt expander

Both templates hold a text generation step in front of the sampler. In the text-to-image template it rewrites the prompt into a detailed English caption and picks an aspect ratio for the canvas. In the image editing template it turns a short instruction into a reference-aware description of the finished image.The official expander for MiniMax-H3-Image is a Qwen3.8-27B FP4 model, published as [MiniMaxAI/MiniMax-H3-Image-PE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE). The templates use a lighter Qwen3.5 9B W4A8 build instead, so the expander fits beside the 21 GB diffusion model on one GPU.The text-to-image template ships with the expander switched off, so your prompt reaches the model exactly as typed; switch it on when you want the caption rewritten and the aspect ratio chosen for you. The image editing template ships with it on.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/minimax/minimax-h3-image.mdx) [Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/minimax/minimax-h3-image)

 {"docsConfig":{"theme":"mint","$schema":"https://mintlify.com/docs.json","name":"ComfyUI","colors":{"primary":"#49378B","light":"#F2FF59","dark":"#F2FF59"},"logo":{"light":"https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max\\u0026auto=format\\u0026n=WCFdTagRdhtvk9-o\\u0026q=85\\u0026s=ec112de87239058f5a931a7e4b594965","dark":"https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max\\u0026auto=format\\u0026n=QzWbjSCBG7w61rR3\\u0026q=85\\u0026s=62b4d879fb3aadbd7a468d1539032d6f","href":"/"},"favicon":"https://mintcdn.com/dripart/maKDA164-rrTfyxY/favicon.ico?fit=max\\u0026auto=format\\u0026n=maKDA164-rrTfyxY\\u0026q=85\\u0026s=94f3a697cf4c9a1ee3961b69219d0942","appearance":{"default":"dark"},"navbar":{"links":\[{"href":"https://blog.comfy.org/?utm\_source=docs","label":"Blog"},{"href":"/tutorials/partner-nodes/pricing","label":"Pricing"},{"href":"https://platform.comfy.org/?utm\_source=docs","label":"Platform"},{"href":"https://comfy.org/download?utm\_source=docs","label":"Download"}\],"primary":{"type":"button","label":"Comfy Cloud","href":"https://comfy.org/cloud?utm\_source=docs"}},"footer":{"socials":{"github":"https://github.com/Comfy-Org/ComfyUI","x":"https://x.com/ComfyUI","discord":"https://discord.com/invite/comfyorg","youtube":"https://www.youtube.com/@comfyorg"},"links":\[{"header":"Resources","items":\[{"label":"installation","href":"/installation/system\_requirements"},{"label":"Tutorials","href":"/tutorials/basic/text-to-image"},{"label":"Development","href":"/development/overview"}\]},{"header":"Products","items":\[{"label":"Features","href":"https://www.comfy.org/?utm\_source=docs"},{"label":"Gallery","href":"https://www.comfy.org/gallery?utm\_source=docs"},{"label":"Download","href":"https://www.comfy.org/download?utm\_source=docs"}\]},{"header":"Company","items":\[{"label":"About","href":"https://www.comfy.org/about?utm\_source=docs"},{"label":"Careers","href":"https://www.comfy.org/careers?utm\_source=docs"},{"label":"Terms of Service","href":"https://www.comfy.org/terms-of-service?utm\_source=docs"},{"label":"Privacy Policy","href":"https://www.comfy.org/privacy-policy?utm\_source=docs"}\]}\]},"search":{"prompt":"Search Comfy documentation..."},"seo":{"metatags":{"googlebot":"max-video-preview:0"}},"icons":{"library":"fontawesome"},"integrations":{"ga4":{"measurementId":"G-MXC01ZDDHQ"},"posthog":{"apiKey":"phc\_iKfK86id4xVYws9LybMje0h44eGtfwFgRPIBehmy8rO"}},"contextual":{"options":\["copy","view","chatgpt","claude"\],"display":"header"},"styling":{"latex":true},"navigation":{"languages":\[{"language":"en","href":""},{"language":"zh","footer":{"socials":{"github":"https://github.com/Comfy-Org/ComfyUI","x":"https://x.com/ComfyUI","discord":"https://discord.com/invite/comfyorg","youtube":"https://www.youtube.com/@comfyorg"},"links":\[{"header":"资源","items":\[{"label":"安装","href":"/zh/installation/system\_requirements"},{"label":"教程","href":"/zh/tutorials/basic/text-to-image"},{"label":"开发","href":"/zh/development/overview"}\]},{"header":"产品","items":\[{"label":"功能","href":"https://www.comfy.org/?utm\_source=docs"},{"label":"画廊","href":"https://www.comfy.org/gallery?utm\_source=docs"},{"label":"下载","href":"https://www.comfy.org/download?utm\_source=docs"}\]},{"header":"公司","items":\[{"label":"关于","href":"https://www.comfy.org/about?utm\_source=docs"},{"label":"招聘","href":"https://www.comfy.org/careers?utm\_source=docs"},{"label":"服务条款","href":"https://www.comfy.org/terms-of-service?utm\_source=docs"},{"label":"隐私政策","href":"https://www.comfy.org/privacy-policy?utm\_source=docs"}\]}\]},"href":"zh"},{"language":"ja","footer":{"socials":{"github":"https://github.com/Comfy-Org/ComfyUI","x":"https://x.com/ComfyUI","discord":"https://discord.com/invite/comfyorg","youtube":"https://www.youtube.com/@comfyorg"},"links":\[{"header":"リソース","items":\[{"label":"インストール","href":"/ja/installation/system\_requirements"},{"label":"チュートリアル","href":"/ja/tutorials/basic/text-to-image"},{"label":"開発","href":"/ja/development/overview"}\]},{"header":"プロダクト","items":\[{"label":"機能","href":"https://www.comfy.org/?utm\_source=docs"},{"label":"ギャラリー","href":"https://www.comfy.org/gallery?utm\_source=docs"},{"label":"ダウンロード","href":"https://www.comfy.org/download?utm\_source=docs"}\]},{"header":"会社情報","items":\[{"label":"概要","href":"https://www.comfy.org/about?utm\_source=docs"},{"label":"採用情報","href":"https://www.comfy.org/careers?utm\_source=docs"},{"label":"利用規約","href":"https://www.comfy.org/terms-of-service?utm\_source=docs"},{"label":"プライバシーポリシー","href":"https://www.comfy.org/privacy-policy?utm\_source=docs"}\]}\]},"navbar":{"links":\[{"href":"/ja/tutorials/partner-nodes/pricing","label":"料金"},{"href":"https://comfy.org/download?utm\_source=docs","label":"ダウンロード"}\],"primary":{"type":"button","label":"Comfy Cloud","href":"https://comfy.org/cloud?utm\_source=docs"}},"href":"ja"},{"language":"ko","footer":{"socials":{"github":"https://github.com/Comfy-Org/ComfyUI","x":"https://x.com/ComfyUI","discord":"https://discord.com/invite/comfyorg","youtube":"https://www.youtube.com/@comfyorg"},"links":\[{"header":"리소스","items":\[{"label":"설치","href":"/ko/installation/system\_requirements"},{"label":"튜토리얼","href":"/ko/tutorials/basic/text-to-image"},{"label":"개발","href":"/ko/development/overview"}\]},{"header":"제품","items":\[{"label":"기능","href":"https://www.comfy.org/?utm\_source=docs"},{"label":"갤러리","href":"https://www.comfy.org/gallery?utm\_source=docs"},{"label":"다운로드","href":"https://www.comfy.org/download?utm\_source=docs"}\]},{"header":"회사 정보","items":\[{"label":"소개","href":"https://www.comfy.org/about?utm\_source=docs"},{"label":"채용","href":"https://www.comfy.org/careers?utm\_source=docs"},{"label":"이용약관","href":"https://www.comfy.org/terms-of-service?utm\_source=docs"},{"label":"개인정보 처리방침","href":"https://www.comfy.org/privacy-policy?utm\_source=docs"}\]}\]},"navbar":{"links":\[{"href":"/ko/tutorials/partner-nodes/pricing","label":"가격 정책"},{"href":"https://comfy.org/download?utm\_source=docs","label":"다운로드"}\],"primary":{"type":"button","label":"Comfy Cloud","href":"https://comfy.org/cloud?utm\_source=docs"}},"href":"ko"},{"language":"es","href":"es"}\]}},"deployment":{"deploymentMetadataValue":{"subdomain":"dripart","hasAudioNarration":false,"actualSubdomain":"dripart","customDomains":\["docs.comfy.org"\],"gitSource":{"type":"github","owner":"comfy-org","repo":"docs","deployBranch":"main","contentDirectory":"","isPrivate":false,"mountPath":"","label":""},"feedback":{"thumbs":true,"edits":true,"issues":true,"agentFeedback":true},"entitlements":{"AI\_CHAT":{"status":"DISABLED"},"WEB\_MCP":{"status":"ENABLED"},"NARRATION":{"status":"DISABLED"}},"buildId":"6af3eba319de42d27705913b","clientVersion":"0.0.4102","searchFilterCounts":\[{"language":"en","tag":"Built-in Nodes","count":1166},{"language":"ja","tag":"組み込みノード","count":1166},{"language":"zh","tag":"内置节点","count":1166},{"language":"en","tag":"Nodes","count":1165},{"language":"ja","tag":"ノード","count":1165},{"language":"zh","tag":"节点","count":1165},{"language":"ko","tag":"내장 노드 (Built-in Nodes)","count":1124},{"language":"ko","tag":"노드","count":1123},{"language":"es","tag":"Nodos integrados","count":1058},{"language":"es","tag":"Nodos","count":1057},{"language":"en","tag":"Tutorials","count":421},{"language":"es","tag":"Tutoriales","count":421},{"language":"en","tag":"Model","count":381},{"language":"ja","tag":"Model","count":381},{"language":"ko","tag":"Model","count":381},{"language":"zh","tag":"Model","count":381},{"language":"es","tag":"Modelo","count":378},{"language":"en","tag":"Image","count":356},{"language":"en","tag":"Partner","count":348},{"language":"ja","tag":"Partner","count":348},{"language":"ko","tag":"Partner","count":348},{"language":"zh","tag":"Partner","count":348},{"language":"es","tag":"Partner","count":346},{"language":"es","tag":"Imagen","count":326},{"language":"ja","tag":"API 開発","count":326},{"language":"ko","tag":"API 개발","count":326},{"language":"zh","tag":"API 开发","count":326},{"language":"ja","tag":"はじめに","count":313},{"language":"ko","tag":"시작하기","count":313},{"language":"zh","tag":"开始使用","count":313},{"language":"en","tag":"Video","count":291},{"language":"en","tag":"Comfy Router","count":290},{"language":"ja","tag":"Comfy Router","count":289},{"language":"ko","tag":"Comfy Router","count":289},{"language":"zh","tag":"Comfy Router","count":289},{"language":"es","tag":"Video","count":266},{"language":"es","tag":"Comfy Router","count":266},{"language":"en","tag":"Models","count":260},{"language":"ja","tag":"Models","count":259},{"language":"ko","tag":"Models","count":259},{"language":"zh","tag":"Models","count":259},{"language":"en","tag":"All Models","count":257},{"language":"es","tag":"Models","count":227},{"language":"es","tag":"All Models","count":224},{"language":"ja","tag":"画像","count":208},{"language":"ko","tag":"이미지","count":208},{"language":"zh","tag":"图像","count":208},{"language":"ja","tag":"Video","count":193},{"language":"zh","tag":"Video","count":193},{"language":"ko","tag":"Video","count":176}\],"searchSettings":{"maxResults":10}},"assistantConfig":{"enableStarterQuestions":false},"basePath":"","hasChatPermissions":false,"hasWebMcpPermissions":true,"toggles":\[{"name":"kill-isr","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"custom-rbac-roles","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"agent-mintlify-slack","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"agent-integrations-settings","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"rbac-expansion","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automations-pr-grouping","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"custom-prefix","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"analytics-v7","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"user-flows-analytics","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"no-publish-flow","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-onboarding","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"llms-txt-v2","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"snapshot-serving-live","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"stripTemperatureMiddleware","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"support-platform-pylon-zendesk","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"snapshot-serving","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"instant-rollback","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"granular-notifications-server","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"granular-notifications","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automations-fable","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"fixed-ai-action-pricing","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automation-resolve-merge-conflict","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"scoped-publishing","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"mintql","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"page-level-analytics","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"edi

[... middle omitted -- see footer ...]

utorials/partner-nodes/elevenlabs/text-to-sound-effects"},{"title":"ElevenLabs Text to Dialogue","sidebarTitle":"Text to Dialogue","href":"/tutorials/partner-nodes/elevenlabs/text-to-dialogue"},{"title":"ElevenLabs Voice Isolation","sidebarTitle":"Voice Isolation","href":"/tutorials/partner-nodes/elevenlabs/voice-isolation"}\]},{"group":"Fish Audio","pages":\[{"title":"Fish Audio: Text to Speech, Voice Cloning, and Speech to Text in ComfyUI","sidebarTitle":"Overview","href":"/tutorials/partner-nodes/fishaudio/fish-audio"},{"title":"Fish Audio Drama 3: directions, word tags, and templates","sidebarTitle":"Drama 3","href":"/tutorials/partner-nodes/fishaudio/drama-3"},{"title":"Fish Audio Prompt Guide: writing prompts for Fish Audio TTS in ComfyUI","sidebarTitle":"Prompt Guide","href":"/tutorials/partner-nodes/fishaudio/prompt-guide"}\]},{"group":"ByteDance","pages":\[{"title":"ByteDance Seed Audio 1.0 - Universal Audio Generation","sidebarTitle":"Seed Audio 1 0","href":"/tutorials/partner-nodes/bytedance/seed-audio-1-0"}\]},{"group":"Sonilo","pages":\[{"title":"Sonilo in ComfyUI: Video to Music and Text to Audio Generation","sidebarTitle":"Video To Music","href":"/tutorials/partner-nodes/sonilo/video-to-music"},{"title":"Sonilo Music 1.5 in ComfyUI: Lyrics to Song","sidebarTitle":"Music 1.5","href":"/tutorials/partner-nodes/sonilo/music-1-5"}\]},{"group":"HeyGen","pages":\[{"title":"HeyGen Voice 1.0 in ComfyUI: Voice Cloning and Text to Speech","sidebarTitle":"HeyGen Voice 1.0","href":"/tutorials/partner-nodes/heygen/heygen-voice-1"}\]},{"group":"Mirelo","pages":\[{"title":"Mirelo SFX 2.0 in ComfyUI: Video to SFX and Text to SFX","sidebarTitle":"SFX 2.0","href":"/tutorials/partner-nodes/mirelo/mirelo-sfx"}\]},{"group":"VEED","pages":\[{"title":"VEED Clean Audio: Speech Cleanup for Audio and Video","sidebarTitle":"Clean Audio","href":"/tutorials/partner-nodes/veed/veed-clean-audio"}\]}\]},{"group":"LLMs","pages":\[{"title":"LLMs in ComfyUI Workflows","sidebarTitle":"Overview","href":"/tutorials/partner-nodes/language/overview"},{"group":"Anthropic","pages":\[{"title":"Anthropic Claude in ComfyUI: Chat and Image Analysis Workflows","sidebarTitle":"Claude","href":"/tutorials/partner-nodes/anthropic/claude"}\]},{"group":"Google","pages":\[{"title":"Google Gemini in ComfyUI: Chat and Image Understanding","sidebarTitle":"Gemini","href":"/tutorials/partner-nodes/google/gemini"}\]},{"group":"OpenAI","pages":\[{"title":"OpenAI Chat in ComfyUI: Conversations and Image Understanding","sidebarTitle":"Chat","href":"/tutorials/partner-nodes/openai/chat"},{"title":"GPT-6 Astra in ComfyUI","sidebarTitle":"GPT-6 Astra","href":"/tutorials/partner-nodes/openai/gpt-6-astra"}\]},{"group":"OpenRouter","pages":\[{"title":"OpenRouter LLM in ComfyUI: Many Models in One Node","sidebarTitle":"Llm","href":"/tutorials/partner-nodes/openrouter/llm"}\]}\]}\]}\]}\]},{"tab":"Comfy Router","pages":\[{"title":"Comfy Router","href":"/development/comfy-router/quickstart"}\]},{"tab":"Agent tools","pages":\[{"title":"Agent tools","href":"/agent-tools"}\]},{"tab":"Built-in Nodes","pages":\[{"title":"Built-in Nodes","href":"/built-in-nodes/overview"}\]},{"tab":"Developer","pages":\[{"title":"Developer","href":"/development/overview"}\]},{"tab":"Support","pages":\[{"title":"Support","href":"/support/contact-support"}\]}\]},{"language":"zh","footer":{"socials":{"github":"https://github.com/Comfy-Org/ComfyUI","x":"https://x.com/ComfyUI","discord":"https://discord.com/invite/comfyorg","youtube":"https://www.youtube.com/@comfyorg"},"links":\[{"header":"资源","items":\[{"label":"安装","href":"/zh/installation/system\_requirements"},{"label":"教程","href":"/zh/tutorials/basic/text-to-image"},{"label":"开发","href":"/zh/development/overview"}\]},{"header":"产品","items":\[{"label":"功能","href":"https://www.comfy.org/?utm\_source=docs"},{"label":"画廊","href":"https://www.comfy.org/gallery?utm\_source=docs"},{"label":"下载","href":"https://www.comfy.org/download?utm\_source=docs"}\]},{"header":"公司","items":\[{"label":"关于","href":"https://www.comfy.org/about?utm\_source=docs"},{"label":"招聘","href":"https://www.comfy.org/careers?utm\_source=docs"},{"label":"服务条款","href":"https://www.comfy.org/terms-of-service?utm\_source=docs"},{"label":"隐私政策","href":"https://www.comfy.org/privacy-policy?utm\_source=docs"}\]}\]},"pages":\[{"title":"zh","href":"/zh/tutorials/image/minimax/minimax-h3-image"}\]},{"language":"ja","footer":{"socials":{"github":"https://github.com/Comfy-Org/ComfyUI","x":"https://x.com/ComfyUI","discord":"https://discord.com/invite/comfyorg","youtube":"https://www.youtube.com/@comfyorg"},"links":\[{"header":"リソース","items":\[{"label":"インストール","href":"/ja/installation/system\_requirements"},{"label":"チュートリアル","href":"/ja/tutorials/basic/text-to-image"},{"label":"開発","href":"/ja/development/overview"}\]},{"header":"プロダクト","items":\[{"label":"機能","href":"https://www.comfy.org/?utm\_source=docs"},{"label":"ギャラリー","href":"https://www.comfy.org/gallery?utm\_source=docs"},{"label":"ダウンロード","href":"https://www.comfy.org/download?utm\_source=docs"}\]},{"header":"会社情報","items":\[{"label":"概要","href":"https://www.comfy.org/about?utm\_source=docs"},{"label":"採用情報","href":"https://www.comfy.org/careers?utm\_source=docs"},{"label":"利用規約","href":"https://www.comfy.org/terms-of-service?utm\_source=docs"},{"label":"プライバシーポリシー","href":"https://www.comfy.org/privacy-policy?utm\_source=docs"}\]}\]},"navbar":{"links":\[{"href":"/ja/tutorials/partner-nodes/pricing","label":"料金"},{"href":"https://comfy.org/download?utm\_source=docs","label":"ダウンロード"}\],"primary":{"type":"button","label":"Comfy Cloud","href":"https://comfy.org/cloud?utm\_source=docs"}},"pages":\[{"title":"ja","href":"/ja/tutorials/image/minimax/minimax-h3-image"}\]},{"language":"ko","footer":{"socials":{"github":"https://github.com/Comfy-Org/ComfyUI","x":"https://x.com/ComfyUI","discord":"https://discord.com/invite/comfyorg","youtube":"https://www.youtube.com/@comfyorg"},"links":\[{"header":"리소스","items":\[{"label":"설치","href":"/ko/installation/system\_requirements"},{"label":"튜토리얼","href":"/ko/tutorials/basic/text-to-image"},{"label":"개발","href":"/ko/development/overview"}\]},{"header":"제품","items":\[{"label":"기능","href":"https://www.comfy.org/?utm\_source=docs"},{"label":"갤러리","href":"https://www.comfy.org/gallery?utm\_source=docs"},{"label":"다운로드","href":"https://www.comfy.org/download?utm\_source=docs"}\]},{"header":"회사 정보","items":\[{"label":"소개","href":"https://www.comfy.org/about?utm\_source=docs"},{"label":"채용","href":"https://www.comfy.org/careers?utm\_source=docs"},{"label":"이용약관","href":"https://www.comfy.org/terms-of-service?utm\_source=docs"},{"label":"개인정보 처리방침","href":"https://www.comfy.org/privacy-policy?utm\_source=docs"}\]}\]},"navbar":{"links":\[{"href":"/ko/tutorials/partner-nodes/pricing","label":"가격 정책"},{"href":"https://comfy.org/download?utm\_source=docs","label":"다운로드"}\],"primary":{"type":"button","label":"Comfy Cloud","href":"https://comfy.org/cloud?utm\_source=docs"}},"pages":\[{"title":"ko","href":"/ko/tutorials/image/minimax/minimax-h3-image"}\]},{"language":"es","pages":\[{"title":"es","href":"/es/tutorials/image/minimax/minimax-h3-image"}\]}\]},"basePath":"","title":"MiniMax-H3-Image: 16 MP text to image and image editing in ComfyUI - ComfyUI","buildId":"dpl\_596ePT575z4qnAFksq1biRW97aLY","deploymentId":"dpl\_596ePT575z4qnAFksq1biRW97aLY","dynamics":\["a74be98ba7"\],"chunks":\["zoom-image-lightbox-C5F0mVLH.js","lightbox-handle-r17bVUz3.js"\]}

──────── [TRUNCATED] ────────
Showing 22,500 chars (head) + 7,500 chars (tail) of 121,773 total clean characters.
Full text saved to: /home/buildlocalai/.hermes/cache/web/docs.comfy.org-f25efc4431.md
To read the omitted middle: read_file path="/home/buildlocalai/.hermes/cache/web/docs.comfy.org-f25efc4431.md" offset=149 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
