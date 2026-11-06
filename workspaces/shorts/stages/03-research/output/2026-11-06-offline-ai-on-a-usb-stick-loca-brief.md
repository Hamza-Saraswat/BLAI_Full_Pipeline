---
slug: 2026-11-06-offline-ai-on-a-usb-stick-loca
stage: 03-research
topic: "Offline AI on a USB stick: local LLM plus Kiwix, no network"
depth: standard
generated_at: 2026-11-06T12:39:21Z
sources: 8
hub: "[[videos/2026-11-06-offline-ai-on-a-usb-stick-loca]]"
---

# Research brief: Offline AI on a USB stick: local LLM plus Kiwix, no network

## Summary
The video lands one idea: a cheap USB stick can carry both halves of an offline answer machine, a model file that runs with no install and a compressed library sitting next to it. The arresting number is 91 GB, all of English Wikipedia with images per Kiwix's own sizing post, made pocket-scale next to a 2.02 GB model file. The strongest concrete case is Survival LLM, whose launch pulled 546 points on Hacker News and which ships about 930,000 Wikipedia articles plus FEMA and CDC guides, showing the exact passage behind every answer. Not verified: speed on viewer hardware, current ZIM sizes (the 91 GB figure is from October 2022), and the "95% accurate" retrieval claim from the thread. The conflict to name on camera: Windows blocks single executables above 4 GB, and HN commenters argued the model layer adds hallucination risk that plain Kiwix search does not have.

## Thesis
A USB stick can hold a whole offline AI kit tonight: one 2.02 GB model file that runs on any computer with no install, next to all of English Wikipedia compressed by Kiwix, answering with zero network.

## Explanation path
Start where the network is gone: a blackout, a plane, a cabin with no signal, and every chatbot the viewer has ever used dies at once. Establish that an offline answer machine has two halves, a brain and a library, and neither actually needs the internet. The brain is a model file: a small model such as Llama 3.2 3B compressed with Q4_K_M quantization is a single 2.02 GB file, and llamafile bolts the engine and the weights into one executable that runs on Windows, Mac or Linux with no installation, which is exactly what makes a USB stick viable as the delivery vehicle. The library is the half most viewers have never heard of: Kiwix has spent two decades turning whole websites into ZIM archives, and that compression is what fits roughly 6.5 million articles into 91 GB with images, 46 GB without, 12 GB as introductions only. Assemble the kit on screen: model file, ZIM archive, and the portable Kiwix reader, all copied to one stick and opened on any machine. Land the honest catches while the payoff is still showing: Windows refuses single executables above 4 GB, so bigger models must travel as separate weights plus a small launcher; a small model paraphrases rather than quotes and can invent a citation, which is why Survival LLM highlights the passage it read; and the whole category was just stress-tested by a free offline assistant whose launch thread argued loudly about exactly this hallucination risk.

## Claims
1. **Survival LLM is a free, open-source AI assistant and emergency library that runs entirely on the user's own computer, carrying about 930,000 Wikipedia articles plus FEMA, CDC and military references.**
   - Source: Survival LLM, https://www.brangus.io/survival-llm
   - Tier: primary | Confidence: high | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "Medical references, FEMA and CDC guidance, survival manuals, how-to guides, repair guides and about 930,000 Wikipedia articles."
2. **The Survival LLM library is a 9 GB download for everything (19 GB once installed), or 1.3 GB (3 GB installed) without Wikipedia and iFixit.**
   - Source: Survival LLM, https://www.brangus.io/survival-llm
   - Tier: primary | Confidence: high | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "Plus the library: a 9 GB download for everything (19 GB once installed), or 1.3 GB (3 GB installed) without Wikipedia and iFixit."
3. **Mozilla's llamafile combines llama.cpp with Cosmopolitan Libc into a single-file executable that runs locally on most operating systems and CPU architectures, with no installation.**
   - Source: mozilla-ai/llamafile README, https://github.com/mozilla-ai/llamafile
   - Tier: primary | Confidence: high | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "combining llama.cpp with Cosmopolitan Libc into one framework that collapses all the complexity of LLMs down to a single-file executable (called a \"llamafile\") that runs locally on most operating systems and CPU architectures, with no installation."
4. **A Llama-3.2-3B-Instruct model at the Q4_K_M quantization is a 2.02GB file.**
   - Source: bartowski/Llama-3.2-3B-Instruct-GGUF model card, https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "Q4_K_M | 2.02GB | false | Good quality, default size for must use cases, _recommended_."
5. **As of October 2022, the Full English Wikipedia ZIM with images used 91GB of storage (ca. 6.5 million articles), 46 GB without images, and 12 GB for the mini version.**
   - Source: What is the size of Wikipedia? (Kiwix Hub), https://hub.kiwix.org/weblog/2022/10/what-is-the-size-of-wikipedia/
   - Tier: docs | Confidence: medium | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "As of October 2022, the Full English Wikipedia (ca. 6.5 million articles), with images will use up 91GB of storage space"
6. **A 128GB microSD card able to hold the full English Wikipedia ZIM cost less than USD 20 at Kiwix's October 2022 sizing.**
   - Source: What is the size of Wikipedia? (Kiwix Hub), https://hub.kiwix.org/weblog/2022/10/what-is-the-size-of-wikipedia/
   - Tier: docs | Confidence: medium | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "A 128GB microSD card to store it on will cost you less than USD 20."
7. **Only executables under 4GB can run on Windows, so any llamafile above 4GB will not work and larger models must load external weights.**
   - Source: mozilla-ai/llamafile README, https://github.com/mozilla-ai/llamafile
   - Tier: primary | Confidence: high | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "Note - Only executables under 4GB can run on Windows, so any llamafile above 4GB won't work."
8. **PrivacyTools confirms the USB-stick workflow end to end: copy one llamafile to a USB drive, run it on any machine, and the model never touches the internet.**
   - Source: llamafile Review: Private AI in 2026 - PrivacyTools.io, https://privacytools.io/app/llamafile
   - Tier: docs | Confidence: high | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "copy one file to a USB drive, run it on any machine, and the model never touches the internet."
9. **Kiwix Reader is a browser-like application that opens ZIM files, and the mini Wikipedia ZIM saves about 95% of the space of the full version.**
   - Source: Kiwix Reader (get.kiwix.org), https://get.kiwix.org/applications/kiwix-reader/
   - Tier: primary | Confidence: high | Accessed: 2026-11-06 | Via: web_extract
   - Quote: "mini: only the introduction of each article, plus the infobox. Saves about 95% of space vs. the full version."
10. **The Survival LLM launch drew 546 points and 204 comments on Hacker News, with top criticisms being hallucinated sources and comparisons to plain Kiwix.**
    - Source: Survival LLM: AI assistant and emergency library that runs on your own computer | Hacker News, https://news.ycombinator.com/item?id=50264853
    - Tier: community | Confidence: medium | Accessed: 2026-11-06 | Via: web_extract
    - Quote: "546 points by Luc 9 days ago ... 204 comments"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Llama-3.2-3B-Instruct Q4_K_M model file | 2.02GB | https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF | "Q4_K_M \| 2.02GB \| false \| Good quality, default size for must use cases, _recommended_." |
| 2 | Full English Wikipedia ZIM with images (October 2022) | 91GB | https://hub.kiwix.org/weblog/2022/10/what-is-the-size-of-wikipedia/ | "will use up 91GB of storage space" |
| 3 | English Wikipedia ZIM without images (nopic) | 46 GB | https://hub.kiwix.org/weblog/2022/10/what-is-the-size-of-wikipedia/ | "you are down to 46 GB" |
| 4 | English Wikipedia mini ZIM (introductions only) | 12 GB | https://hub.kiwix.org/weblog/2022/10/what-is-the-size-of-wikipedia/ | "then 12 GB is all you need" |
| 5 | Storage card that holds the full encyclopedia | less than USD 20 | https://hub.kiwix.org/weblog/2022/10/what-is-the-size-of-wikipedia/ | "A 128GB microSD card to store it on will cost you less than USD 20." |
| 6 | Survival LLM full library download | 9 GB (19 GB once installed) | https://www.brangus.io/survival-llm | "a 9 GB download for everything (19 GB once installed)" |
| 7 | Windows single-executable cap for llamafile | 4GB | https://github.com/mozilla-ai/llamafile | "Only executables under 4GB can run on Windows" |
| 8 | Wikipedia articles inside Survival LLM | about 930,000 | https://www.brangus.io/survival-llm | "about 930,000 Wikipedia articles" |

## Analogy candidates
- **A glovebox survival kit**: the USB stick is the glovebox, the llamafile is the friend who explains what to do, the ZIM library is the stack of official manuals. Breaks when: a glovebox kit holds fixed supplies, while the model writes new sentences and can misstate what the manual says.
- **A librarian plus the whole library in your pocket**: the model is the librarian who answers in plain words, the ZIM is the actual stacks, Kiwix is the reading room. Breaks when: a librarian quotes the book exactly, an LLM paraphrases and can invent a citation.

## Misconceptions
- Myth: Running your own AI needs a beefy GPU or a hardware upgrade. Reality: a 3-billion-parameter model at Q4_K_M is a 2.02GB file that llamafile runs on ordinary CPUs with no install and no GPU (claims 3, 4).
- Myth: Without internet there is no Wikipedia. Reality: Kiwix has shipped the whole English encyclopedia as an offline ZIM for years, 91GB with images at the last official sizing (claim 5).
- Myth: An offline assistant that cites sources is as trustworthy as the library it carries. Reality: Survival LLM's own page says the small models make mistakes more often, and its launch thread's loudest criticism was hallucinated sources, so the app shows the exact passage to check (claims 1, 10).

## Glossary
- **local LLM**: a model file you run on your own machine, where no request ever leaves the computer.
- **llamafile**: Mozilla's single executable that bundles a model and the llama.cpp engine into one file.
- **llama.cpp**: the open-source engine that runs model files on ordinary processors and GPUs.
- **Cosmopolitan Libc**: a library that compiles one program to run unchanged on Windows, macOS and Linux.
- **GGUF**: the file format model weights are distributed in, the thing you actually download.
- **quantization**: shrinking model weights to fewer bits so the file takes a fraction of the memory, at some cost in quality.
- **Q4_K_M**: a popular 4-bit quantization setting that keeps quality high while cutting file size sharply.
- **Kiwix**: free open-source software that reads whole websites offline.
- **ZIM file**: the compressed archive format Kiwix reads, one file per website.
- **RAG (retrieval-augmented generation)**: the model first searches a document collection, then answers from what it found and shows the sources.

## Unverified
- Tokens per second and load time when running a 3B model from a USB stick on the viewer's own hardware; no first-party measurement exists yet.
- Current 2026 Wikipedia ZIM sizes; the 91GB, 46 GB and 12 GB figures are Kiwix's October 2022 sizing.
- The claim that Survival LLM's retrieval answers are "95% accurate", which appeared only in a commenter's paraphrase on Hacker News.
- Whether USB 2.0 versus 3.0 stick speed is the real bottleneck for model load time; no fetched page measured it.

## Suggested outline
1. Hook with the two sizes: all of English Wikipedia with images is 91 GB and the AI brain is a 2.02 GB file, so both halves fit on one cheap stick.
2. Build it on screen: copy a llamafile, a mini or nopic Wikipedia ZIM, and the portable Kiwix Reader onto the stick, then open them on any machine with no install.
3. Pull the plug and give the honest catch: it still answers offline, but Windows blocks single files above 4 GB, and a small model can invent a citation, so make it show the passage it read.

## Viewer situation
You've got a spare USB stick and a gaming PC or Mac, and you've downloaded a model before, but every AI you use today stops working the moment the network does.

## Has process
`true`. The real steps the viewer performs:
- Download a small model as a llamafile (or the llamafile launcher plus a GGUF file).
- Download a Wikipedia ZIM from the Kiwix catalog (mini at 12 GB, nopic at 46 GB, or the full version).
- Download the portable Kiwix Reader build.
- Copy the model file, the ZIM and Kiwix onto one USB stick.
- Plug the stick into any computer and open the llamafile and Kiwix without installing anything.
- Disconnect the network and test questions against both halves.

## Objection
A 3-billion-parameter model on CPU is slow and weak, the stick's read speed throttles load time, and the LLM cannot actually search the ZIM, so this is two disconnected tools sharing one stick rather than a real offline assistant.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.brangus.io/survival-llm | Survival LLM | primary | web_extract | 2026-11-06 |
| 2 | https://news.ycombinator.com/item?id=50264853 | Survival LLM: AI assistant and emergency library that runs on your own computer (Hacker News) | community | web_extract | 2026-11-06 |
| 3 | https://hub.kiwix.org/weblog/2022/10/what-is-the-size-of-wikipedia/ | What is the size of Wikipedia? (Kiwix Hub) | docs | web_extract | 2026-11-06 |
| 4 | https://github.com/mozilla-ai/llamafile | mozilla-ai/llamafile: Distribute and run LLMs with a single file. | primary | web_extract | 2026-11-06 |
| 5 | https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF | bartowski/Llama-3.2-3B-Instruct-GGUF | primary | web_extract | 2026-11-06 |
| 6 | https://kiwix.org/en/ | Kiwix - Home | primary | web_extract | 2026-11-06 |
| 7 | https://privacytools.io/app/llamafile | llamafile Review: Private AI in 2026 - PrivacyTools.io | docs | web_extract | 2026-11-06 |
| 8 | https://get.kiwix.org/applications/kiwix-reader/ | Kiwix Reader (get.kiwix.org) | primary | web_extract | 2026-11-06 |

## Notes
The Wikipedia ZIM sizes are Kiwix's October 2022 figures, four years old at access; the script should present them as scale, not a live catalog number. The Hacker News thread is the only community-tier source and backs sentiment and criticism, not numbers used in Key numbers. Survival LLM itself installs to a computer rather than running stick-native, but its 0.4.0 update (October 29, 2026) added moving the library to an external drive, which is the bridge from that story to this USB build. The llamafile Windows 4 GB cap is the practical reason this build pairs a sub-4 GB model with separate ZIM files. FireCrawl had no credits this run; every source was fetched with web_extract.
