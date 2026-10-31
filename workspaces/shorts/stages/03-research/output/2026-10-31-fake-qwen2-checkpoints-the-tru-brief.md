---
slug: 2026-10-31-fake-qwen2-checkpoints-the-tru
stage: 03-research
topic: "Fake Qwen2-labeled checkpoints on Hugging Face carry crypto-mining malware that runs via trust_remote_code"
depth: standard
generated_at: 2026-10-31T11:40:22Z
sources: 9
hub: "[[videos/2026-10-31-fake-qwen2-checkpoints-the-tru]]"
---

# Research brief: Fake Qwen2 checkpoints on Hugging Face are mining malware in disguise

## Summary
Pluto Security published the Load/Mine report on October 29, 2026: 31 malicious repositories across seven Hugging Face accounts, disguised as small Qwen2 test models, that mine Pearl (PRL) cryptocurrency into the operator's wallet the moment someone loads them with trust_remote_code enabled. The most arresting number: the flagship fake MENXIANGYU/qwen2-tiny contained a model.safetensors file of just 42 bytes with no tensors inside, yet climbed to 28,412 downloads by October 28 while every Hugging Face scanner returned clean. The strongest concrete case: a shared research GPU cluster joined the operator's pool with nine workers within 90 seconds of each other, and dropped off about six minutes later when an admin killed the jobs. What could not be verified: how many machines were actually infected (downloads are not infections) and whether the still-live second-wave repos have since been removed. One near-conflict: wave-one downloads are "728" in Pluto's scope table and "more than 700" in BleepingComputer's writeup; compatible, and Pluto's exact table wins.

## Thesis
A fake model repo on Hugging Face needs no poisoned weights or pickle exploit to own your GPU: trust_remote_code=True imports the publisher's Python with your privileges before any weights load, so the defense is a tonight-doable checklist -- vet the org, prefer safetensors, keep the flag off, verify the hash.

## Explanation path
Start with what the viewer already does: they grab a small "test" checkpoint from Hugging Face by name, paste the loading snippet, and click through the trust_remote_code prompt without reading the code, which is the exact behavior the campaign was built around. Establish the event before the mechanism: Pluto Security tracked 31 malicious repositories across seven accounts in two waves since September 2026, and the second wave came back within days of the first takedown. Before any deep technical dive, land the horror detail: the flagship fake qwen2-tiny held a 42-byte model.safetensors with no tensors; everything malicious lived in modeling_evil2.py, a plain Python file the config's auto_map pointed at. Only then explain the mechanism, because the mechanism explains the defense: config.json names a Python file, Transformers imports it at load time, and Python runs a module's top-level statements to define its classes, so a _boot() call sitting next to the class definition executes before any weights load, no pickle needed. Then the platform gap: Hugging Face scans every file smaller than 2 GB with ClamAV and displays pickle imports, but a plain .py file is neither a known malware signature nor a serialized model, so the flagship scanned clean while it collected 28,412 downloads. Then the payoff for the local-AI viewer: the payload runs as their own interpreter, launches the miner from memory as a fake kernel worker named [kworker/u20:1], and leaves a watchdog that restarts it every 120 seconds plus shell hooks that survive reboots. Close with the checklist that maps one-to-one onto the attack: pull from the official org only, glance at the file list before downloading, prefer .safetensors weights (the format built to prevent arbitrary code execution), keep trust_remote_code off unless you have read the .py files it runs, pin the revision you reviewed, and check the machine if you already loaded a suspect model, because the model loading "successfully" is not evidence of safety; it is the attack completing.

## Claims
1. **Pluto Security disclosed the campaign on October 29, 2026: 31 malicious repositories across seven Hugging Face accounts, in two waves since September 2026, disguised as small Qwen2 test checkpoints, with the second wave still live eight days after being reported.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl
   - Quote: "We tracked 31 malicious repositories across seven Hugging Face accounts. The 19 second-wave repositories have been downloaded more than 29,000 times, and they were still live eight days after we reported them."
2. **The code runs before the model does: trust_remote_code=True imports the repository's Python with the caller's privileges before any weights load, and no malicious weights are needed.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl
   - Quote: "trust_remote_code=True imports the repository's Python with the caller's privileges before any weights load. No malicious weights are needed."
3. **The flagship fake MENXIANGYU/qwen2-tiny contained no actual model: its model.safetensors was just 42 bytes with no tensors, and the payload lived in modeling_evil2.py, which auto_map pointed to.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl
   - Quote: "Its configuration looks like any Qwen2 model, but model.safetensors contains no tensors and is just 42 bytes. The payload is in modeling_evil2.py, and auto_map points to modeling_evil2.EvilModel."
4. **The fake qwen2-tiny climbed from 7,354 downloads at disclosure to 28,412 downloads by October 28, 2026, while scanning clean on every scanner that ran, including a JFrog report that the payload file was "not a machine-learning model."**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl
   - Quote: "The second-wave flagship scanned clean while it collected 28,412 downloads"
5. **The malware is a GPU crypto-miner paying real money: the operator's wallet had received about 2,276 PRL across 716 transactions (roughly $5,000) and was still active on mining pools after the repositories behind it were removed.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl
   - Quote: "The wallet had received about 2,276 PRL across 716 transactions and sent about 2,241 PRL onward. That is realized profit, not a pending balance."
6. **Hugging Face's malware scanning runs every file smaller than 2 GB through the ClamAV antivirus at each commit, and ClamAV matches known signatures; a plain Python file referenced by auto_map is neither a known signature nor a serialized model, so it scans clean.**
   - Source: Malware Scanning - Hugging Face, https://huggingface.co/docs/hub/security-malware
   - Tier: docs | Confidence: high | Accessed: 2026-10-31 | Via: web_extract
   - Quote: "We run every file of your repositories that is smaller than 2 GB through a malware scanner."
7. **The Transformers security policy puts the responsibility on the user: it recommends safetensors as "developed specifically to prevent arbitrary code execution on your system" and says to "always" verify the content of the modeling files when using trust_remote_code.**
   - Source: Security Policy - huggingface/transformers, https://raw.githubusercontent.com/huggingface/transformers/main/SECURITY.md
   - Tier: docs | Confidence: high | Accessed: 2026-10-31 | Via: curl
   - Quote: "We heavily recommend uploading and downloading models in the safetensors format (which is the default prioritized by the transformers library), as developed specifically to prevent arbitrary code execution on your system."
8. **The miner hides as a fake Linux kernel worker: the payload copies the binary into a memory-backed file descriptor and executes it as [kworker/u20:1], leaving no executable path on disk, while a watchdog restarts a missing miner every 120 seconds.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl
   - Quote: "Using the model loader's own interpreter, the watchdog restarts a missing miner every 120 seconds."
9. **A near-identical copy of the fake payload was still live on Hugging Face under the account htt0118 when checked, listing a model size of 0 params and no model card.**
   - Source: htt0118/qwen2-tiny - Hugging Face, https://huggingface.co/htt0118/qwen2-tiny
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: web_extract
   - Quote: "No model card ... Model size 0 params"
10. **Vetting the publisher is a real filter: the campaign's fake READMEs were copied word for word from the official Qwen2.5-0.5B model card, so the org name is the tell, not the card text.**
    - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
    - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl
    - Quote: "The README was copied word for word from the official Qwen2.5-0.5B model card."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | flagship fake downloads by October 28 | 28,412 downloads | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "the Hub listed it at 18,012 on October 25, 25,854 on October 27 and 28,412 on October 28" |
| 2 | fake weights file size | 42 bytes | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "model.safetensors contains no tensors and is just 42 bytes" |
| 3 | malicious repositories across seven accounts | 31 malicious repositories | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "We tracked 31 malicious repositories across seven Hugging Face accounts" |
| 4 | operator wallet received on-chain | about 2,276 PRL (~$5,000) | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "The wallet had received about 2,276 PRL across 716 transactions" |
| 5 | watchdog relaunch interval | every 120 seconds | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "the watchdog restarts a missing miner every 120 seconds" |
| 6 | Hugging Face malware scan file-size cap | smaller than 2 GB | https://huggingface.co/docs/hub/security-malware | "every file of your repositories that is smaller than 2 GB through a malware scanner" |
| 7 | real Qwen2.5-0.5B parameter count | 0.49B | https://huggingface.co/Qwen/Qwen2.5-0.5B | "Number of Parameters: 0.49B" |
| 8 | live htt0118 copy, downloads last month | 98 | https://huggingface.co/htt0118/qwen2-tiny | "Downloads last month98" |

## Analogy candidates
- **Vehicle: a memo slipped into a bundle of blueprints.** Mapping: the repo looks like a normal model package (config.json, a README copied word for word from the real card, a weights file), but the malicious logic is a memo (modeling_evil2.py) inserted into the bundle, and trust_remote_code=True is the instruction "execute any memo in the bundle on arrival." Breaks when: a memo is passive text a human reads, while the .py file executes automatically with your privileges the moment you load, and it leaves a watchdog and shell hooks behind after you delete the repo.
- **Vehicle: a frozen dinner with a sticky note inside.** Mapping: safetensors is the sealed, see-through meal (the format cannot execute code), while custom code is the sticky note that says "run me." Breaks when: the viewer never opens the package to inspect it; they paste a snippet and click through the prompt, and the note runs during loading, not at mealtime.
- **Vehicle: a fake utility worker with a clipboard.** Mapping: the miner disguises itself as a kernel worker ([kworker/u20:1]) the way a scammer dresses as a technician; the process list looks official while the GPU does the attacker's work. Breaks when: a real technician works a shift and leaves, while this one is memory-resident, invisible to disk scans, restarted every 120 seconds, and can hand over a reverse shell long after the "visit."

## Misconceptions
- Myth: "Hugging Face scans everything, so a clean scan means safe." Reality: scanning matches known malware signatures and pickle imports, but a plain Python file referenced by auto_map is neither, so the flagship scanned clean while it collected 28,412 downloads (claim 4, claim 6).
- Myth: "Safetensors files can carry this malware too." Reality: safetensors was built to prevent arbitrary code execution; the fake's model.safetensors was an empty 42-byte decoy, and the malware lived in the .py file the flag runs (claim 3, claim 7).
- Myth: "I would notice a miner on my machine." Reality: the payload launches from memory as a fake kernel worker with no executable path on disk, and the first sign is usually a GPU busier than it should be or a cloud bill (claim 8).
- Myth: "This kind of attack needs poisoned weights or a pickle exploit." Reality: no malicious weights are needed; the permission to run a custom implementation is the whole attack (claim 2).
- Myth: "A convincing model card means a legit model." Reality: the fake READMEs were copied word for word from the official Qwen2.5-0.5B model card, so the org name is the tell, not the card (claim 10).

## Glossary
- **trust_remote_code**: A loading flag that tells Transformers to download and import the model repository's own Python files, which run with your privileges before any weights load.
- **safetensors**: Hugging Face's weight-serialization format, built specifically to prevent arbitrary code execution, unlike pickle.
- **auto_map**: The section of a repo's config.json that names which Python module and class Transformers should import to build the model.
- **pickle**: Python's serialization format and the default for PyTorch .bin weights, which can execute arbitrary code when deserialized.
- **reverse shell**: A backdoor where the victim machine connects out to the attacker's server and hands over an interactive command shell.
- **memfd_create**: A Linux syscall that creates an anonymous memory-backed file, letting malware run a binary without writing an executable path to disk.
- **PRL (Pearl)**: The cryptocurrency this campaign's wallets mined into, visible on public pool dashboards.
- **ClamAV**: The open-source antivirus whose signature matching Hugging Face runs on every uploaded file under 2 GB.
- **watchdog**: A separate process that restarts the miner if it is killed; here, every 120 seconds.
- **IoC (Indicator of Compromise)**: A concrete artifact such as a file path, hash, process name or network address that defenders use to check whether a machine was hit.

## Unverified
- The number of confirmed infected machines is unknown; Pluto's counts measure downloads, not confirmed infections or unique victims.
- Whether Hugging Face has removed the still-live second-wave and linked repositories since Pluto's October 28 status table.
- That Ollama or llama.cpp users are unaffected in general; Pluto names the GGUF parser and pickle formats as two other doors for code execution, and this campaign simply did not use them.
- That the operator's wallet keeps growing after Pluto's October 21 on-chain capture.
- Whether any given home machine is clean; that needs a first-party run of Pluto's quick checks (grep for svc.py in shell startup files, look for /tmp/.cch/, look for a process named [kworker/u20:1] carrying mining arguments).

## Suggested outline
1. Hook: someone downloaded a "qwen2-tiny" test model this month, the weights file was 42 bytes, and their GPU started mining Pearl for a stranger.
2. The event: Pluto Security, October 29, 31 fake repos across seven accounts, two waves, back within days of takedown.
3. The tell anyone can check tonight: real org "Qwen" versus random-string accounts; the real card lists 0.49B parameters while the fake lists 0 params and no model card.
4. The mechanism in one breath: config.json's auto_map names a .py file, Transformers imports it at load, and a _boot() call runs before any weights, so trust_remote_code=True means "run this stranger's script as me."
5. Why the scanner did not save anyone: ClamAV matches signatures under 2 GB per file, and a plain .py file is neither a signature nor a serialized model, so the flagship scanned clean through 28,412 downloads.
6. What actually runs: a miner launched from memory as [kworker/u20:1], restarted every 120 seconds by a watchdog, with shell hooks that survive reboots.
7. The tonight checklist: check the org, read the file list, prefer safetensors, keep trust_remote_code off unless you read the code, pin the revision, verify the hash, and run the quick checks if you already loaded one.
8. Honest catch: cryptomining is the mildest thing this entry point can deliver; the same mechanism can run anything your loading process is allowed to do.

## Viewer situation
You download open models from Hugging Face by name, paste the loading snippet, and click through the trust_remote_code prompt without reading the code.

## Has process
true
Check the org name against the official publisher (Qwen, not MENXIANGYU or htt0118) before downloading.
Open the Files page and look for a real weights file and any .py files an auto_map points to.
Prefer .safetensors weights and keep trust_remote_code off unless you have read the Python it would run.
Pin the exact revision you reviewed when a model legitimately needs custom code.
Verify the sha256 of downloaded weight files against a trusted source before loading.
Run Pluto's quick checks on a suspect machine: grep for svc.py in shell startup files, look for /tmp/.cch/, and look for a process named [kworker/u20:1] carrying mining arguments.

## Objection
A skeptical engineer says: the checklist only covers the Transformers loading path, because safetensors did not stop this fake (its 42-byte decoy scanned clean, the attack lived in config.json and a .py file), and Ollama and llama.cpp users never type trust_remote_code at all.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | Load/Mine: A Hugging Face Malware Campaign Returns After Takedown | primary | curl | 2026-10-31 |
| 2 | https://huggingface.co/docs/hub/security-malware | Malware Scanning - Hugging Face | docs | web_extract | 2026-10-31 |
| 3 | https://huggingface.co/docs/hub/security-pickle | Pickle Scanning - Hugging Face | docs | web_extract | 2026-10-31 |
| 4 | https://huggingface.co/docs/safetensors/index | Safetensors - Hugging Face | docs | web_extract | 2026-10-31 |
| 5 | https://raw.githubusercontent.com/huggingface/transformers/main/SECURITY.md | Security Policy - huggingface/transformers | docs | curl | 2026-10-31 |
| 6 | https://huggingface.co/docs/transformers/custom_models | Customizing models - Hugging Face | docs | web_extract | 2026-10-31 |
| 7 | https://huggingface.co/htt0118/qwen2-tiny | htt0118/qwen2-tiny - Hugging Face | primary | web_extract | 2026-10-31 |
| 8 | https://huggingface.co/Qwen/Qwen2.5-0.5B | Qwen/Qwen2.5-0.5B - Hugging Face | primary | web_extract | 2026-10-31 |
| 9 | https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/ | Hugging Face malware campaign returns to hijack GPUs for crypto mining | docs | web_extract | 2026-10-31 |

## Notes
Two near-conflicts, both resolved in Pluto's favor. Wave-one downloads: Pluto's scope table records "728" before removal; BleepingComputer says "more than 700 downloads" (compatible; Pluto's exact table wins). Download milestones: Business Insider's "18,012 downloads by October 25" matches Pluto's Hub-listing series (7,354 at disclosure, 18,012 on October 25, 25,854 on October 27, 28,412 on October 28), so cite Pluto's series. Thin spots: the flagship MENXIANGYU/qwen2-tiny repo page itself is no longer fetchable (Hugging Face has disabled access, per BleepingComputer), so the 42-byte detail rests on Pluto's report alone; the live htt0118 copy is the only fake-repo page first-party fetchable today, showing 0 params and 98 downloads last month. The strongest hook number is the 42-byte weights file inside a repo downloaded 28,412 times.
