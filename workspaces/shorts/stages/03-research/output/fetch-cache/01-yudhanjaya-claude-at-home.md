# 01 -- yudhanjaya.com, Honey, We Have Claude at Home (primary experiment)

URL: https://yudhanjaya.com/docs/experiments/local-llms-experiments/
Accessed: 2026-11-23 | Via: web_extract | Tier: primary (self-published experiment write-up with methodology, full-page cached at ~/.hermes/cache/web/yudhanjaya.com-d3b0b8aa33.md)

Author: Yudhanjaya Wijeratne (developer). Subtitle: "or running local llms on your own hardware".
This is the primary experiment the emergent.sh news item summarizes.

## Setup (verbatim)
- "Leviathan is my PC for work, gaming, etc. It started out as a Ryzen 5800 X3D with a Radeon 5700 XT."
- "my RAM is DDR4, at 3200 Mhz. My 3080 (bought secondhand) is on the x4 slot."
- "My GPUs are power-limited to 220w, because that 3080 can really spike and cause headaches for my 1000-watt Corsair power supply."
- "here are the local AI models I have on disk and their speeds, at a context window of 128,000."
- "I've got 64 gigs of RAM and am barely past that 24 GB VRAM limit - albeit with a bottleneck; two cards, one much slower than the other."
- Engines named: llama.cpp, vLLM, SGLang; derivatives Strata, PolyStrata, Maya, Koboldcpp; wrappers LMStudio, Ollama, Unsloth Desktop.
- "because I'm on offgrid solar, my energy is practically free."

## What 'reproduce' means (verbatim)
- "My test for their competence is a harness / engine that takes a NetLogo economic simulation, converts it to Typescript, checks for 1:1 parity between outputs, ... and produces an interactive HTML economic sim complete with places, people, dashboards, and adjustable policy levers. This is a fairly challenging task, and Sonnet, Deepseek and GLM all manage very similar outputs."
- "All of these model are, I would say, slightly better than Claude Opus 4.5 (November 24, 2025). They are not as good as Claude Opus 5.5, Gemini Neon, or the GPT Astra-Luna-Sol combo."
- "the two most popular models on this list Deepseek 4.1 and GLM 5.3 Flash - almost tie with Claude Sonnet 5.5, but the keyword is almost."
- "The biggest on the list are somewhere around Claude Opus 4.5 (November 24, 2025) for smarts, possibly tying with today's Claude Haiku models."
- "I'm not going to claim that I've got a drop-in replacement for Claude Opus 5.5 here."
- "All of these models are smarter than ChatGPT when it released. ... all of these are 'smarter' than GPT-4 (2023)."
- Not a blind test, not benchmark parity vs Claude: one author, one personal workload, qualitative comparison.

## Speed numbers (verbatim)
- "Claude, via the desktop app, usually doles out its tokens at somewhere between 60-80 tokens per second."
- "On my hardware, I'm happy to get 30 tps. This is just under half the speed of a subscription; this to me is acceptable."
- "Deepseek 4.1 gave me a whopping 10.3 tps, 12 if I prayed."
- "MiniMax M3.1-Flash Maya-XS IQ1_S (93 GB) gave me 2.9 tok/s at 128K and sent my system thrashing between swap and RAM. I couldn't even finish benchmarking it."
- Table (context 128,000, Decode tok/s): GLM-5.3-Flash 321B/18B "20.7 code / 23.6 prose"; Hy4-Flash 220B/12B "33.3 code / 26.2 prose"; Qwen3.8 Flash-Next IQ3_S 125B/6B "70.4"; Swift 1.5 IQ2_XS 125B/6B "141.9"; Ling-3.0-flash Q4_K_M 124B/5.1B "47.3 code / 53.5 prose"; Flint 40B-A2.5B "111.6 (cold 72.8)"; MiniCPM-V 4.7 Q4_K_M 35B/3B "172.1 (cold 103.1)"; Muse Glimmer UD-Q4_K_XL "135.3"; Inkling 2 Mini UD-Q4_K_XL 26.2B/3.4B "42 code / 69 prose"; DeepSeek-V4-Pro-Qwen3.5-9B Q5_K_M "163.8"; LFM3-Omni-2B Q8_0 2.17B dense "215.5", prefill "11,980 / 183.0 (29K)".
- RAM table: GLM-5.3-Flash "53.0 pinned + 5.1"; Ling-3.0-flash "2.3 + 57.8"; Swift IQ2_XS "35.3 + 0.2"; Inkling 2 Mini "7.6 + 10.4".

## Cost and hardware access (verbatim)
- "Qwen 3.8 Flash-Next can be run on as a 12 GB 3060 with as little as 16 gigs of VRAM if you have an NVME drive."
- "thus, given the system I'm running, it often makes more sense to have a $10 subscription that gives me access to these models and to let them shepherd smaller models to do complex tasks."
- Goldilocks pick: Qwen 3.8 Flash-Next via Strata; "In Strata, download the Qwen IQ3_S variant if you have a good computer and like 16 GB of VRAM. If not, go for the IQ2_XS Swift variant."

## Break points the author himself states (verbatim)
- "They are not going to be very fast unless you've got some serious hardware, like RTX 6000s (plural) and great servings of DDR5 RAM."
- "At these speeds, these are not the kind of models I would personally use for chat or data extraction tasks. These are the kind of models that are best used for code, where I write a detailed markdown file explaining what I want done and how, point them at it, and let them grind overnight."
- "they do require pretty much my entire system's resources, so there's no space for a smaller, faster model"
- "LFM was able to find the needle at 11,000 tokens. It was able to find the needle at 32k, but at 88k, it simply couldn't."
- "LFM, in my testing, has not been good past the 32k context window."
- "[Hy4] runs, but at abysmal prefill speeds - so it takes a long time to read anything."
- "Intelligence among these models tend to be spiky."
- On quantization myths: "the choice of agent and harness - ie: the software you slap on top of a model - matters more for these large models than the gap between quants."
- Benchmarks skepticism on others: MiMo "benchmaxxed ... the equivalent of a student who can ace an exam but is totally mid outside it."
