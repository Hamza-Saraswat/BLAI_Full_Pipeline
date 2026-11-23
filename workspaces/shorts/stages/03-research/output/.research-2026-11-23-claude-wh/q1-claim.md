FINDINGS | The primary experiment is "Honey, We Have Claude at Home" by developer Yudhanjaya Wijeratne, self-published at yudhanjaya.com/docs/experiments/local-llms-experiments/ (HN submission Nov 22, 2026); the phrase "local LLMs reproduce Claude" is Emergent's headline framing of it, not the author's own (caches 01, 02)
FINDINGS | "Reproduce" in the experiment means qualitative parity on one author-built workload: a harness that converts a NetLogo economic simulation to TypeScript, checks 1:1 output parity, pulls OSM data and builds an interactive HTML sim -- "Sonnet, Deepseek and GLM all manage very similar outputs" (cache 01)
FINDINGS | It is NOT a blind test, NOT benchmark parity vs Claude, and NOT persona mimicry; one author, one machine, his own tasks; he writes "I'm not going to claim that I've got a drop-in replacement for Claude Opus 5.5 here" (cache 01)
FINDINGS | Hardware: "Leviathan", a Ryzen 5800 X3D PC with a secondhand RTX 3080 plus a 4080, 64 GB DDR4-3200 RAM, GPUs power-limited to 220 W; "a generation or two of hardware behind" the top end (cache 01)
FINDINGS | Method: heavily quantized open-weight models (IQ2 to Q5) run through llama.cpp-family engines (Strata, PolyStrata, Maya, llama-server), some streaming expert weights from NVMe; he benchmarked decode speeds at a context window of 128,000 (cache 01)
FINDINGS | His capability ceiling claim, verbatim: the big local models are "slightly better than Claude Opus 4.5 (November 24, 2025)", not as good as Claude Opus 5.5, and DeepSeek 4.1 and GLM 5.3 Flash "almost tie with Claude Sonnet 5.5, but the keyword is almost" (cache 01)
FINDINGS | What he published: a long-form guide with speed tables (14 models, decode tok/s and prefill at 88K), RAM usage tables, model recommendations by hardware tier, and engine setup instructions; benchmarks addendum promised but "a whole slew of benchmarks I haven't posted here" (cache 01)
FINDINGS | Emergent's Nov 22 write-up (byline Sakthy, SEO Manager, "2 min read") summarizes the guide and upgrades the claim: local models "can match or exceed cloud alternatives in specific domains" and calls local deployment "a production-ready alternative" -- stronger than the primary's hedged wording (cache 02)
FINDINGS | The second Nov 22 publication is a beginner guide by Jerry James on gpupartner.com ("A beginner's guide to Local AI with Inkling, Qwen, and Unsloth"), which hit the HN front page (544 points live / 566 via API, 227-238 comments within 14 hours) -- it is a setup walkthrough, not a Claude-parity experiment (caches 03, 04)
FINDINGS | The model at the center of the beginner wave is Thinking Machines Lab's Inkling 2 Mini: 26.4B total / 5.4B effective active parameters, MoE with 8 of 128 experts per layer, looped layers (24 layers, 48 layer applications per token), 1M-token context, Apache 2.0, released November 20, 2026 (caches 03, 06)
NUMBERS | 60-80 tokens per second | Claude via the desktop app, per the experimenter's own baseline | cache 01
NUMBERS | 30 tps | his big-model tier on his hardware, "just under half the speed of a subscription" | cache 01
NUMBERS | 128,000 | context window all his speed benchmarks were run at | cache 01
ANALOGY CANDIDATES | Home cooking vs a restaurant: a skilled cook with a good kitchen can match a restaurant on the dishes they cook every week, for the cost of groceries; breaks when you order something off-menu (new domains, frontier difficulty) or need service speed (tokens per second)
ANALOGY CANDIDATES | Folding laundry to fit a smaller suitcase (the experimenter's own quantization image): you pack the same clothes into less space; breaks when the fold lines show -- some fabrics (workloads) wrinkle badly at 2-3 bits, others never do
ANALOGY CANDIDATES | A cover band that nails the hits: sounds like the record on the songs it rehearsed (your repeated workloads); breaks on requests from the audience it never learned (long context, novel agent tasks)
MISCONCEPTIONS | Myth: the experiments proved local models equal today's Claude | Reality: the author's own words cap it at "almost" tying Claude Sonnet 5.5 and beating only 2025's Claude Opus 4.5 (claim 2, cache 01)
GLOSSARY | local LLM: an AI model whose file you download and run on your own GPU instead of renting it from a company's servers
GLOSSARY | quantization: storing the model's numbers in fewer bits so it fits in less memory, trading a little accuracy for size and speed
GLOSSARY | VRAM: the memory on your graphics card; the model, plus its working memory for the conversation, has to fit there to run fast
GLOSSARY | tokens per second: how fast the model writes its answer, the at-home equivalent of how snappy a chat app feels
GLOSSARY | open weights: the model's learned numbers are published as a file anyone can download and run, like an open-source program
GLOSSARY | mixture of experts: a model that keeps many specialist sub-networks on disk but activates only a few per word, so a huge model can run at small-model speed
GLOSSARY | context window: how much of the conversation and documents the model can keep in mind at once, measured in tokens
GLOSSARY | MoE | see mixture of experts
GLOSSARY | engine (inference engine): the program that loads the model file and runs it on your hardware, e.g. llama.cpp or Unsloth Desktop
GLOSSARY | GGUF: the single-file format quantized models ship in, what you actually download
GLOSSARY | KV cache: the model's working memory for the current conversation; it grows with context and competes with the model for VRAM
GLOSSARY | blind test: judging two models' outputs without knowing which is which; the reproduce-Claude experiments did not use one
GLOSSARY | prefill: the work a model does reading your long input before it starts writing; slow prefill means long waits on big pastes
UNVERIFIED | Emergent's summary claims local deployment is "feasible on systems with 16GB to 32GB of RAM" and response times "within 2-3x of cloud APIs for most queries"; neither figure appears in the primary write-up, so the video should not state them as the experimenter's numbers
UNVERIFIED | A widely shared HN comment claims Inkling 2 on an M5 Max found codebase issues "Claude didn't find in previous audits" and was "faster than GLM or Claude"; single anonymous anecdote, no methodology
UNVERIFIED | The claim that operational costs after hardware investment are "essentially zero" ignores electricity; the primary author's near-zero energy cost comes from offgrid solar, which most viewers do not have
NOT FOUND | No blind A/B test, win-rate scoreboard, or named benchmark comparing these local models directly against a Claude model was published in any fetched source; "reproduce" rests on one developer's workload parity and vibe
