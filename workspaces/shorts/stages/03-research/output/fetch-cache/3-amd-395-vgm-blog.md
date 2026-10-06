[Skip to main content](https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html#)

[AMD Website Accessibility Statement](https://www.amd.com/en/site-notifications/accessibility-statement.html)

# AMD Ryzen™ AI MAX+ 395 Processor: Breakthrough AI Performance in Thin and Light

Mar 17, 2025

![feature image.jpg](https://www.amd.com/content/dam/amd/en/images/blogs/migrated-blogs/752960-0.jpg)

The AMD Ryzen™ AI MAX+ 395 (codename: “Strix Halo”) is the most powerful x86 APU in the market today and delivers a significant performance boost over the competition. Powered by 16 “Zen 5” CPU cores, 50+ peak AI TOPS XDNA™ 2 NPU and a truly massive integrated GPU driven by 40 AMD RDNA™ 3.5 CUs, the Ryzen™ AI MAX+ 395 is a transformative upgrade for premium thin and light devices. The Ryzen™ AI MAX+ 395 is available today with system memory options ranging from 32GB all the way up to 128GB of unified memory – out of which up to 96GB can be converted to VRAM through AMD Variable Graphics Memory.

The Ryzen™ AI Max+ 395 excels in consumer AI workloads like the llama.cpp-powered application: LM Studio. Shaping up to be _the_ must-have app for client LLM workloads, LM Studio allows users to locally run the latest language model without any technical knowledge required and unleash their creativity and productivity. Deploying new AI text and vision models on Day 1 has never been simpler.

The “Strix Halo” platform extends AMD performance leadership in LM Studio with the new AMD Ryzen™ AI MAX series of processors.

As a primer: the model size is dictated by the number of parameters and the precision used. Generally speaking, doubling the parameter count (on the same architecture) or doubling the precision will also double the size of the model. Most of our competition’s current-generation offerings in this space max out at 32GB on-package memory. This is enough shared graphics memory to run large language models (roughly) up to 16GB in size.

**Benchmarking text and vision language models in LM Studio**

For this comparison, we will be using the ASUS ROG Flow Z13 with 64GB of unified memory. We will restrict the LLM size to models that fit inside 16GB to ensure that it runs on the competition’s 32GB laptop. In terms of latency, we will be looking at time to first token (which is how long the LLM takes to respond) and tokens/s for performance.

From the results, we can see that the ASUS ROG Flow Z13 - powered by the integrated Radeon™ 8060S and taking full advantage of the 256 GB/s bandwidth - effortlessly achieves up to 2.2x the performance of the Intel Arc 140V in token throughput.

The performance uplift is very consistent across different model types (whether you are running chain-of-thought DeepSeek R1 Distills or standard models like Microsoft Phi 4) and different parameter sizes.

![AMD Ryzen(TM) AI MAX+ 395 LLM Benchmarks Tokens Per Second.jpg](https://www.amd.com/content/dam/amd/en/images/blogs/migrated-blogs/752960-1.jpg)

AMD Ryzen(TM) AI MAX+ 395 LLM Benchmarks Tokens Per Second.jpg

In time to first token benchmarks, the AMD Ryzen™ AI MAX+ 395 processor is up to 4x faster than the competition in smaller models like Llama 3.2 3b Instruct.

Going up to 7 billion and 8 billion models like the DeepSeek R1 Distill Qwen 7b and DeepSeek R1 Distill Llama 8b, the Ryzen™ AI Max+ 395 is up to 9.1x faster. When looking at 14 billion parameter models (which is approaching the largest size that can comfortably fit on a standard 32GB laptop), the ASUS ROG Flow Z13 is up to 12.2x faster than the Intel Core Ultra 258V powered laptop – _more than an order of magnitude faster than the competition!_

![2-alt.jpg](https://www.amd.com/content/dam/amd/en/images/blogs/migrated-blogs/752960-2.jpg)

2-alt.jpg

The larger the LLM, the faster AMD Ryzen™ AI Max+ 395 processor is in responding to the user query. So whether you are having a conversation with the model or giving it large summarization tasks involving thousands of tokens – the AMD machine will be much faster to respond. This advantage scales with the prompt length – so the heavier the task – the more pronounced the advantage will be.

Text-only LLMs are also slowly getting replaced with highly capable multi-modal models that have vision adapters and visual reasoning capabilities. The IBM Granite Vision is one example and the recently launched Google Gemma 3 family of models is another – with both providing highly capable vision capabilities to next generation AMD AI PCs. Both of these models run performantly on an AMD Ryzen™ AI MAX+ 395 processor.

An interesting point to note here: when running vision models, the time to first token metric also effectively becomes the time it takes for the model to analyze the image you give it.

![AMD Ryzen(TM) AI MAX+ 395 LLM Benchmarks Vision Models.jpg](https://www.amd.com/content/dam/amd/en/images/blogs/migrated-blogs/752960-3.jpg)

AMD Ryzen(TM) AI MAX+ 395 LLM Benchmarks Vision Models.jpg

The Ryzen™ AI Max+ 395 processor is up to 7x faster in IBM Granite Vision 3.2 3b, up to 4.6x faster in Google Gemma 3 4b and up to 6x faster in Google Gemma 3 12b. The ASUS ROG Flow Z13 came with a 64GB memory option so it can also effortlessly run the Google Gemma 3 27B Vision model – which is currently considered the current SOTA (state of the art) vision model.

[Watch on YouTube](https://www.youtube.com/watch?v=mAl3qTLsNcw)

To watch YouTube content on this site, please change your privacy settings to enable cookies. Alternatively, click 'Watch on YouTube' to view the video directly on YouTube. Your personal data will be processed by YouTube in compliance with its own privacy policy and cookies policy available on its website.

Edit Privacy Settings

Another example is running the DeepSeek R1 Distill Qwen 32b in 6-bit precision (while 4-bit is industry standard for everyday use cases, coding can require higher precision to maintain coding accuracy) – which you can use to code a gaming classic in roughly 5 minutes:

[Watch on YouTube](https://www.youtube.com/watch?v=8llG9hIq8I4)

To watch YouTube content on this site, please change your privacy settings to enable cookies. Alternatively, click 'Watch on YouTube' to view the video directly on YouTube. Your personal data will be processed by YouTube in compliance with its own privacy policy and cookies policy available on its website.

Edit Privacy Settings

**Related: The AMD Ryzen™ AI Max+ 395 is [also available in the HP ZBook Ultra G1a as a PRO series processor](https://community.amd.com/t5/ai/integration-ascendant-exploring-the-amd-ryzen-ai-max-pro-series/ba-p/753606).**

**Setting up for LLM runs**

Now let’s talk about how to tune your AMD Ryzen™ AI Max+ 395 processor for maximum performance and capability for large language models.

![AMD_AI_4-1741990285028.png](https://www.amd.com/content/dam/amd/en/images/blogs/migrated-blogs/752960-4.png)

AMD\_AI\_4-1741990285028.png

**_Image:_** _VGM options on a 32GB laptop. VGM High = 16GB dedicated graphics memory._

Please make sure you are on the latest AMD Software: Adrenalin Edition™ driver update. AMD laptops powered by AMD Ryzen™ AI 300 series processors feature Variable Graphics Memory. AMD recommends turning on VGM for any LLM workloads to help token throughput and allow larger model sizes to run. A VGM setting of High is recommended. You can access the VGM options through the Performance > Tuning tab in AMD Software: Adrenalin Edition™.

**You can download and install [LM Studio from their website](https://lmstudio.ai/).**

When running LLMs – please check “manually select parameters” and set the GPU Offload setting to MAX. AMD recommends Q4 K M quantization for everyday use and Q6 or Q8 for coding.

Experiencing AI locally on laptops powered by the AMD Ryzen™ AI MAX+ 395 processor is a great way for the power user to experience state-of-the-art AI models while having a portable, thin and light, gaming and productivity powerhouse. AMD is firmly committed to supporting the open-source ecosystem and enabling AI for everyone.

Share:

#### Article By

* * *

![Profile Image of AMD AI Group](https://www.amd.com/content/dam/code/images/coveo/default.jpg)

[AMD AI Group](https://www.amd.com/en/blogs/by-author/amd-ai-group.html)

![](https://www.amd.com/content/dam/amd/en/images/backgrounds/dividers/divider-white-pearl-gradient-medium.jpg)

## Related Blogs

[View All Blogs](https://www.amd.com/en/search/blogs.html)

- [MoRI UMBP Empowers AMD Instinct GPUs](https://www.amd.com/en/developer/resources/technical-articles/2026/mori-umbp-empowers-amd-instinct-gpus.html)

[![MoRI UMBP Empowers AMD Instinct GPUs](https://www.amd.com/content/dam/amd/en/images/abstract/3317200-ai-aspirations.jpg)](https://www.amd.com/en/developer/resources/technical-articles/2026/mori-umbp-empowers-amd-instinct-gpus.html)





##### [MoRI UMBP Empowers AMD Instinct GPUs](https://www.amd.com/en/developer/resources/technical-articles/2026/mori-umbp-empowers-amd-instinct-gpus.html)




See how UMBP, MoRI and SGLang optimize KV cache reuse to boost AMD Instinct™ MI355X GPU agentic AI performance and cost efficiency





October 01, 2026


- [Automating Performance Bottleneck Identification with the TraceLens Agent — ROCm Blogs](https://rocm.blogs.amd.com/software-tools-optimization/tracelens-analysis-agent/README.html)

[![Automating Performance Bottleneck Identification with the TraceLens Agent — ROCm Blogs](https://rocm.blogs.amd.com/_images/software-tools-optimization-tracelens-analysis-agent-images-TraceLens_Agent.webp)](https://rocm.blogs.amd.com/software-tools-optimization/tracelens-analysis-agent/README.html)





##### [Automating Performance Bottleneck Identification with the TraceLens Agent — ROCm Blogs](https://rocm.blogs.amd.com/software-tools-optimization/tracelens-analysis-agent/README.html)




TraceLens Agent is an agentic workflow that examines GPU traces to deliver a prioritized optimization report, detailing root causes and fixes.





September 29, 2026


- [MORI CCO](https://www.amd.com/en/developer/resources/technical-articles/2026/mori-cco.html)

[![MORI CCO](https://www.amd.com/content/dam/amd/en/images/abstract/2760484-accelerated-computing-7.jpg)](https://www.amd.com/en/developer/resources/technical-articles/2026/mori-cco.html)





##### [MORI CCO](https://www.amd.com/en/developer/resources/technical-articles/2026/mori-cco.html)




MORI CCO enables compute-communication overlap on AMD Instinct™ GPUs. Build faster distributed inference and training kernels with device-side communication.





September 29, 2026


- [Unlocking Sim2Real for a Robotic Arm with RL Accelerated by AMD Instinct GPUs — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/sim2real-rl-instinct/README.html)

[![Unlocking Sim2Real for a Robotic Arm with RL Accelerated by AMD Instinct GPUs — ROCm Blogs](https://rocm.blogs.amd.com/_images/artificial-intelligence-sim2real-rl-instinct-images-sim2real-rl.webp)](https://rocm.blogs.amd.com/artificial-intelligence/sim2real-rl-instinct/README.html)





##### [Unlocking Sim2Real for a Robotic Arm with RL Accelerated by AMD Instinct GPUs — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/sim2real-rl-instinct/README.html)




Train an XArm-6 pick-and-lift policy with PPO in MuJoCo Warp on AMD Instinct GPUs, then transfer it to the real robot.





September 28, 2026


- [How AMD Ryzen AI Max PRO 400 Series Processors Bring Local Agentic AI to Business Customers](https://www.amd.com/en/blogs/2026/how-amd-ryzen-ai-max-pro-400-series-processors-bring-local-agentic-ai-to-business-customers.html)

[![How AMD Ryzen AI Max PRO 400 Series Processors Bring Local Agentic AI to Business Customers](https://www.amd.com/content/dam/amd/en/images/blogs/designs/projects/other-commercial-blogs/gorgon-halo-launch/gorgon-halo-feature-image.jpg)](https://www.amd.com/en/blogs/2026/how-amd-ryzen-ai-max-pro-400-series-processors-bring-local-agentic-ai-to-business-customers.html)





##### [How AMD Ryzen AI Max PRO 400 Series Processors Bring Local Agentic AI to Business Customers](https://www.amd.com/en/blogs/2026/how-amd-ryzen-ai-max-pro-400-series-processors-bring-local-agentic-ai-to-business-customers.html)




See how AMD Ryzen AI Max PRO 400 Series processors bring local agentic AI to business with more memory, flexible deployment, and lower costs.





September 28, 2026


- [UltraQuant on AMD Instinct: More Efficient Agentic Serving for Qwen3.8-MXFP4 — ROCm Blogs](https://rocm.blogs.amd.com/software-tools-optimization/ultraquant-kv4/README.html)

[![UltraQuant on AMD Instinct: More Efficient Agentic Serving for Qwen3.8-MXFP4 — ROCm Blogs](https://rocm.blogs.amd.com/_images/software-tools-optimization-ultraquant-kv4-images-ultraquant-kv4.webp)](https://rocm.blogs.amd.com/software-tools-optimization/ultraquant-kv4/README.html)





##### [UltraQuant on AMD Instinct: More Efficient Agentic Serving for Qwen3.8-MXFP4 — ROCm Blogs](https://rocm.blogs.amd.com/software-tools-optimization/ultraquant-kv4/README.html)




A native 4-bit MXFP4 KV cache that speeds up Qwen3.8 decode over 8-bit KV on AMD Instinct MI355X, with no accuracy loss.





September 24, 2026


- [Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html)

[![Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo — ROCm Blogs](https://rocm.blogs.amd.com/_images/artificial-intelligence-quark-strix-halo-images-quark-strix-halo-thumbnail.webp)](https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html)





##### [Local Quantization and Multi-Backend Deployment with AMD Quark on Strix Halo — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/quark-strix-halo/README.html)




Quantize a 35B MoE model directly on AMD Strix Halo with AMD Quark, export to GGUF and safetensors, validate with llama.cpp and vLLM, and deploy through Lemonade.





September 24, 2026


- [Model Weight Profiles: Where Do the Parameters Go? — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/model-weight-profiles/README.html)

[![Model Weight Profiles: Where Do the Parameters Go? — ROCm Blogs](https://rocm.blogs.amd.com/_images/artificial-intelligence-model-weight-profiles-images-model-weight-profiles-thumbnail.webp)](https://rocm.blogs.amd.com/artificial-intelligence/model-weight-profiles/README.html)





##### [Model Weight Profiles: Where Do the Parameters Go? — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/model-weight-profiles/README.html)




Introduce Model Weight Profiles and compare embeddings, attention, and dense layers so checkpoint size and quantization savings make sense.





September 24, 2026



Footnotes

**Legal footnotes:**

**SHO26** \- Testing as of March 2025 by AMD. All tests conducted on LM Studio 0.3.11. Llama.cpp runtime 1.18. Tokens/s and time to first token: Sustained performance average of multiple runs with specimen prompt "How long would it take for a ball dropped from 10 meter height to hit the ground?". Models tested: DeepSeek R1 Distill Qwen 1.5b Q4 K M, DeepSeek R1 Distill Qwen 7b Q4 K M, DeepSeek R1 Distill Qwen 8b Q4 K M, DeepSeek R1 Distill Qwen 14b Q4 K M, Phi 4 Mini Instruct 3.8b, Phi 4 Q4 K M, Llama 3.2 3b Instruct. AMD Ryzen™ AI MAX+ 395 on an ASUS ROG Flow Z13 with 64GB 8000 MT/s memory, Windows 11 Pro 24H2 and Adrenalin 25.3.1 WHQL. VGM = 32GB Intel Core Ultra 7 258V on an HP Zenbook S14 with 32GB 8533 MT/s memory, Windows 11 Pro 24H2 and Intel Graphics Driver 32.0.101.6559. Performance may vary. **SHO27** \- Testing as of March 2025 by AMD. All tests conducted on LM Studio 0.3.13. Llama.cpp runtime 1.19.2. Time to first token using prompt “Describe this image” and picture taken from: [www.loc.gov/item/2013648266/](https://www.loc.gov/item/2013648266/) Models tested: IBM Granite Vision 3.2 2b, Google Gemma 3 4b, Google Gemma 3 12b and Google Gemma 3 27b AMD Ryzen™ AI MAX+ 395 on an ASUS ROG Flow Z13 with 64GB 8000 MT/s memory, Windows 11 Pro 24H2 and Adrenalin 25.3.1 WHQL. VGM = 32GB Intel Core Ultra 7 258V on an HP Zenbook S14 with 32GB 8533 MT/s memory, Windows 11 Pro 24H2 and Intel Graphics Driver 32.0.101.6559. Links to third party sites are provided for convenience and unless explicitly stated, AMD is not responsible for the contents of such linked sites and no endorsement is implied. Performance may vary. **GD-97**\- Links to third party sites are provided for convenience and unless explicitly stated, AMD is not responsible for the contents of such linked sites and no endorsement is implied.

**GD-220e**\- Ryzen™ AI is defined as the combination of a dedicated AI engine, AMD Radeon™ graphics engine, and Ryzen processor cores that enable AI capabilities. OEM and ISV enablement is required, and certain AI features may not yet be optimized for Ryzen AI processors. Ryzen AI is compatible with: (a) AMD Ryzen 7040 and 8040 Series processors and Ryzen PRO 7040/8040 Series processors except Ryzen 5 7540U, Ryzen 5 8540U, Ryzen 3 7440U, and Ryzen 3 8440U processors; (b) AMD Ryzen AI 300 Series processors and AMD Ryzen AI PRO 300 Series processors; (c) all AMD Ryzen 8000G Series desktop processors except the Ryzen 5 8500G/GE and Ryzen 3 8300G/GE; (d) AMD Ryzen 200 Series processors and Ryzen PRO 200 Series processors except Ryzen 5 220 and Ryzen 3 210; and (e) AMD Ryzen AI Max Series processors and Ryzen AI PRO Max Series processors. Please check with your system manufacturer for feature availability prior to purchase


Feedback


##### AMD.com Feedback

### Ask AMD

Hi! How can I help you today?

This AI chat may occasionally be inaccurate. By using it, you agree to AMD's [Privacy Policy](https://www.amd.com/en/legal/privacy.html). Conversations may be recorded to operate and improve the service. Do not share sensitive information.

Qualified