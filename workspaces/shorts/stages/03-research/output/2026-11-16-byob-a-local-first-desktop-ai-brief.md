---
slug: 2026-11-16-byob-a-local-first-desktop-ai
stage: 03-research
topic: "byob: a local-first desktop AI agent, no Electron"
depth: standard
generated_at: 2026-11-16T12:42:02Z
sources: 10
hub: "[[videos/2026-11-16-byob-a-local-first-desktop-ai]]"
---

# Research brief: byob: a local-first desktop AI agent, no Electron

## Summary
The video's idea: the missing half of local AI is not the model, it is the desktop body -- and a brand-new open-source project called byob ("Bring Your Own Brain") is that body, one native Rust program with no Electron that treats your already-running llama-server or Ollama as its entire backend. The most arresting number is the download size pair: about 60 MB with everything in it, 13 MB for the slim build, for a full agent desktop. The strongest concrete case is the README's hero demo: a two-sheet budget workbook filling in beside the chat while a local llama.cpp model writes it, recorded live with only the waits cut. What could not be verified: byob's RAM use while running (no fetched page publishes one; 60 MB is download size, not memory) and any real-world stability, since the tracker has zero issues filed. No material conflict between sources; only staleness: the project site still offers "Download byob 0.3.5" hours after v0.3.6 shipped, so the releases page is authoritative.

## Thesis
A one-week-old Rust rewrite proves a desktop AI agent needs neither a bundled model nor a bundled browser: point it at the OpenAI-compatible server you already run on localhost and it gives that model hands -- about a 60 MB download, no Electron, no account.

## Explanation path
Start from the split the name encodes: the brain and the body. The brain is the model server the viewer already runs -- llama-server, Ollama, LM Studio, vLLM -- each speaking the OpenAI-compatible HTTP dialect on a localhost port. The body is what has been missing: a desktop harness with hands (files, commands, spreadsheets, approval cards) whose only contract with the model is a URL. Establish that most agent harnesses ship as TypeScript plus Electron, a bundled Chromium, and that byob's author rebuilt the same shape as one native Rust program that draws its own interface on the GPU, going as far as prototyping six other Rust GUI toolkits before choosing egui. Then the connect beat: the predecessor hob bundled llama.cpp, and byob's defining move was dropping the bundled inference entirely, so first run just scans the usual ports, offers a Test connection button, and the model you connect becomes the default. The payoff is artifacts appearing beside the chat with per-turn undo. Land the honesty beat before the install line: a week-old, single-author project with an empty issue tracker and unsigned macOS builds is something you can try tonight, not yet something to hand your taxes.

## Claims
1. **byob is a native desktop AI coworker for the model you already run: point it at any OpenAI-compatible endpoint (llama-server, Ollama, LM Studio, vLLM or a hosted API) and it works in a folder with you, reading and writing files, running code, and building spreadsheets, charts, documents and small apps beside the chat.**
   - Source: Scronkfinkle/byob: Bring Your Own Brain - Local Agent Harness, https://github.com/Scronkfinkle/byob
   - Tier: primary | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "A native desktop AI coworker for the model you already run. Point byob at any OpenAI-compatible endpoint (llama-server, Ollama, LM Studio, vLLM or a hosted API) and it works in a folder with you: reads and writes files, runs code, and builds spreadsheets, charts, documents and small apps beside the chat."
2. **byob is one native program for Linux, macOS and Windows that draws its own interface on the GPU, with no Electron -- it is desktop software, not a web page in a window.**
   - Source: Scronkfinkle/byob: Bring Your Own Brain - Local Agent Harness, https://github.com/Scronkfinkle/byob
   - Tier: primary | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "byob is **desktop software, not a web page in a window**: one program for Linux, macOS and Windows that draws its own interface on the GPU, with no Electron."
3. **The full download is about a 60 MB folder with everything in it, and the slim build is 13 MB.**
   - Source: Scronkfinkle/byob: Bring Your Own Brain - Local Agent Harness, https://github.com/Scronkfinkle/byob
   - Tier: primary | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "A real desktop app. One folder, about a 60 MB download with everything in it (13 MB for the slim build), and native file dialogs, drag and drop and keyboard shortcuts."
4. **On first run byob shows a Connect a model screen listing servers it found on this computer's usual ports -- llama-server 8080, Ollama 11434, LM Studio 1234, vLLM 8000 -- plus presets and a Test connection button; tool calling falls back to prompt-based calls when the server has none.**
   - Source: Scronkfinkle/byob: Bring Your Own Brain - Local Agent Harness, https://github.com/Scronkfinkle/byob
   - Tier: primary | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "On first run byob shows **Connect a model**: servers it found on this computer's usual ports (llama-server 8080, Ollama 11434, LM Studio 1234, vLLM 8000), presets for those and for hosted APIs, and a Test connection button."
5. **byob began as a rewrite of hob, an earlier desktop coworker that bundled llama.cpp; byob drops the bundled inference, so the agent never runs the model itself.**
   - Source: Scronkfinkle/byob: Bring Your Own Brain - Local Agent Harness, https://github.com/Scronkfinkle/byob
   - Tier: primary | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "byob began as a rewrite of hob, an earlier desktop coworker that bundled llama.cpp; byob drops the bundled inference."
6. **Instead of Electron the interface is egui/eframe 0.37 on wgpu, chosen after gpui, iced, Slint, Freya, Xilem and Floem were prototyped on 2026-11-09, and hob's Electron IPC layer was replaced by byob-protocol plus byob-server.**
   - Source: byob architecture, https://raw.githubusercontent.com/Scronkfinkle/byob/main/docs/architecture.md
   - Tier: primary | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "egui/eframe 0.37 (wgpu; WebGPU with WebGL2 fallback on the web). gpui, iced, Slint, Freya, Xilem and Floem were prototyped on 2026-11-09"
7. **Ollama's local server is itself an OpenAI-compatible endpoint at http://localhost:11434/v1/, one of the ports byob scans, and its API key is required by clients but ignored by the server.**
   - Source: OpenAI compatibility - Ollama, https://docs.ollama.com/api/openai-compatibility
   - Tier: docs | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "base_url='http://localhost:11434/v1/', api_key='ollama',  # required but ignored"
8. **llama.cpp's llama-server exposes OpenAI API compatible chat completions, responses and embeddings routes, with function calling for ~any model -- the thing byob's --inference-url http://localhost:8080/v1 points at.**
   - Source: LLaMA.cpp HTTP Server, https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/server/README.md
   - Tier: docs | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "OpenAI API compatible chat completions, responses, and embeddings routes"
9. **The Show HN thread for byob sat at 4 points about 18 hours after posting; the author says most agent harness apps are TypeScript-based with Electron or IPC, and he rebuilt the idea without any web code in about a week.**
   - Source: Show HN: A local-first AI agent for the desktop, no Electron, any LLM endpoint | Hacker News, https://news.ycombinator.com/item?id=50507341
   - Tier: community | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
   - Quote: "After about a week, I ended up with a harness that feels pretty good!"
10. **The project's GitHub issue tracker shows 0 open and 0 closed issues at fetch, meaning no member of the public has filed a bug report yet.**
    - Source: Issues · Scronkfinkle/byob, https://github.com/Scronkfinkle/byob/issues
    - Tier: primary | Confidence: high | Accessed: 2026-11-16 | Via: web_extract
    - Quote: "Open 0 (0) ... Closed 0 (0)"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | full download size, everything included | about a 60 MB | https://github.com/Scronkfinkle/byob | "One folder, about a 60 MB download with everything in it (13 MB for the slim build)" |
| 2 | slim build download size | 13 MB | https://github.com/Scronkfinkle/byob | "(13 MB for the slim build)" |
| 3 | v0.3.6 Apple silicon macOS .dmg asset size | 64.3 MB | https://github.com/Scronkfinkle/byob/releases | "byob-0.3.6-aarch64-apple-darwin.dmg ... 64.3 MB" |
| 4 | repository stars at fetch | 7 | https://github.com/Scronkfinkle/byob | "Stars ... 7 stars" |
| 5 | releases published between 10 Nov 2026 (v0.1.0) and 16 Nov 2026 (v0.3.6) | 10 | https://github.com/Scronkfinkle/byob | "Releases 10 (10)" |

## Analogy candidates
- **BYOB restaurant**: byob supplies the table, the glasses and the service -- the window, the file tools, the approval cards -- and you supply the bottle: the model, already open on your counter at localhost:8080. Breaks when: at a restaurant the bottle just sits there, while here the entire meal is poured from your bottle, so a weak local model makes the service look bad -- tool calling quality belongs to the model, not the app.
- **Handset and exchange**: any telephone handset works on any network because both sides speak one standard; the OpenAI-compatible API is the dial tone of local AI, and byob is just a very capable handset. Breaks when: a handset only carries voice, but this handset has hands that act on your filesystem -- a slow exchange (low tokens per second) does not delay a call, it stalls a task halfway through a file edit.

## Misconceptions
- Myth: A "local-first AI agent" runs the model itself. Reality: byob ships no inference at all; it is an HTTP client to any OpenAI-compatible URL, and it exists precisely because its predecessor hob bundled llama.cpp and byob dropped that (claim 5).
- Myth: "No Electron" means no web technology anywhere in the app. Reality: the desktop shell is native Rust drawing on the GPU, but the browser UI is the same app compiled to WebAssembly and HTML artifacts render through a separate Servo renderer process that ships with byob -- what is gone is Chromium as the desktop shell (claims 2 and 6).
- Myth: Connecting it to your model means hand-editing config files. Reality: first run scans the usual ports and offers a Test connection button; the entire configuration can be one flag, byob --inference-url http://localhost:8080/v1 (claim 4).

## Glossary
- **OpenAI-compatible endpoint**: a server that speaks the same HTTP API shape as OpenAI's chat completions, so any client built for OpenAI can talk to it -- including a local one on localhost.
- **Electron**: a desktop-app framework that ships a whole Chromium browser plus Node.js inside every app; the standard way TypeScript agent harnesses become desktop programs.
- **llama-server**: the llama.cpp HTTP server that loads a GGUF model file on your own machine and serves it on a local port.
- **egui**: an immediate-mode GUI toolkit in Rust that draws its interface directly through the GPU (via wgpu) instead of rendering HTML.
- **tool calling**: the model asking the client to run a function (read a file, run a command) and using the result; when a server lacks it, byob falls back to prompt-based calls.
- **WebAssembly (wasm)**: a binary format that compiles programs like Rust code to run in a browser tab -- how byob's same native UI also runs on a phone.
- **Landlock**: a Linux kernel feature that lets a program voluntarily give up access to files and folders, how byob sandboxes run_command and run_python on Linux.

## Unverified
- byob's RAM use while running has no published number in any fetched page; the 60 MB figure is download size, not memory, and our own hardware would have to measure it.
- An Electron-based agent harness with the same features would use several times more memory than byob; no fetched page states such a number.
- That Ollama, LM Studio and vLLM connect as smoothly as llama-server does in practice; the README lists presets for all of them, but nobody here has tried it.
- Whether the project survives its first weeks of public exposure cannot be known from a single Show HN post.

## Suggested outline
1. Cold open: your llama-server is already running -- here is the 13 MB slim desktop harness that gives it hands, no Electron, no account.
2. The two-piece stack: a model server speaking OpenAI-compatible HTTP on localhost, and byob pointing at its URL; first run scans the usual ports (8080, 11434, 1234, 8000) and tests the connection for you.
3. Honest catch, then the payoff: about a week old, one main author, zero issues filed, unsigned on macOS, and about a 60 MB is download size not RAM -- and still, tonight: cargo install byob, connect, approve the first diff.

## Viewer situation
You already run a local model on llama-server, Ollama or LM Studio and talk to it in a web UI or a terminal, but it has no hands: it cannot touch your files, run code, or build anything beside the conversation.

## Has process
`true`
- Start your local model server (for example llama-server with a GGUF file, or `ollama serve`) and note the port it listens on.
- Install byob: `cargo install byob`, or download the release archive for Linux, macOS or Windows from the releases page and unpack it.
- Launch byob and wait for the Connect a model screen; pick the server it found on its usual port, or start it by hand with `byob --inference-url http://localhost:8080/v1 --model local`.
- Press Test connection to confirm the endpoint answers, then keep that model as the default.
- Open or create a workspace folder so the agent's file tools and commands have a place to run.
- Ask for something concrete -- build a spreadsheet from a CSV, run a script -- and approve each action card, with its diff, before anything runs.
- Optionally run `byob --serve` and `tailscale serve 7470` to reach the same live session from your phone.

## Objection
It is about a week old with one main author, 7 stars, an empty issue tracker and unsigned macOS builds, so "no Electron" is an aesthetic claim until strangers have hammered on it -- and about a 60 MB is the download size, not the memory it uses, which nobody has published.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/Scronkfinkle/byob | Scronkfinkle/byob: Bring Your Own Brain - Local Agent Harness | primary | web_extract | 2026-11-16 |
| 2 | https://github.com/Scronkfinkle/byob/releases | Releases · Scronkfinkle/byob | primary | web_extract | 2026-11-16 |
| 3 | https://raw.githubusercontent.com/Scronkfinkle/byob/main/docs/architecture.md | byob architecture | primary | web_extract | 2026-11-16 |
| 4 | https://raw.githubusercontent.com/Scronkfinkle/byob/main/ROADMAP.md | Roadmap | primary | web_extract | 2026-11-16 |
| 5 | https://byob.chat | byob: bring your own brain | primary | web_extract | 2026-11-16 |
| 6 | https://github.com/Scronkfinkle/byob/issues | Issues · Scronkfinkle/byob | primary | web_extract | 2026-11-16 |
| 7 | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/server/README.md | LLaMA.cpp HTTP Server | docs | web_extract | 2026-11-16 |
| 8 | https://docs.ollama.com/api/openai-compatibility | OpenAI compatibility - Ollama | docs | web_extract | 2026-11-16 |
| 9 | https://news.ycombinator.com/item?id=50507341 | Show HN: A local-first AI agent for the desktop, no Electron, any LLM endpoint | community | web_extract | 2026-11-16 |
| 10 | https://trendshift.io/repositories/359647 | Scronkfinkle/byob -- GitHub trending stats & insights | community | web_extract | 2026-11-16 |

## Notes
Trendshift (fetched 2026-11-16) corroborates the timeline: repository created 7 days ago, +4 stars over three days, one social mention total (the Show HN post). Two minor discrepancies, both resolved toward the repo: byob.chat still offers "Download byob 0.3.5" hours after v0.3.6 shipped (trust the releases page), and Trendshift lists the license as "Apache License 2.0" while the repo states "MIT OR Apache-2.0". Community reception is a single Show HN post at 4 points with no comments at fetch -- the video must not claim broader traction. The Show HN number is community-tier, so it stays in claims and out of key numbers.
