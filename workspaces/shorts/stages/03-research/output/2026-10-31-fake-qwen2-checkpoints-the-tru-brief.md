---
slug: 2026-10-31-fake-qwen2-checkpoints-the-tru
stage: 03-research
topic: "Fake Qwen2-labeled checkpoints on Hugging Face carry a crypto-mining backdoor that runs via trust_remote_code"
depth: standard
generated_at: 2026-10-31T11:40:22Z
sources: 10
hub: "[[videos/2026-10-31-fake-qwen2-checkpoints-the-tru]]"
---

# Research brief: Fake Qwen2 checkpoints on Hugging Face are mining malware in disguise

## Summary
Pluto Security published the Load/Mine report on October 29, 2026: 31 malicious repositories across seven Hugging Face accounts, disguised as small Qwen2 test models, that mine Pearl (PRL) cryptocurrency into the operator's wallet the moment someone loads them with trust_remote_code enabled. The most arresting number: the flagship fake "MENXIANGYU/qwen2-tiny" contained a model.safetensors file of just 42 bytes with no tensors inside, yet climbed to "28,412 downloads" by October 28. The strongest concrete case: a shared research GPU cluster joined the operator's pool -- nine workers named dhumphreys-notebook-2, tsakaguchi-notebook-1 and albertzhou-notebook-1, plus A100s -- within 90 seconds of each other, and dropped off six minutes later when an admin killed the jobs. What could not be verified: whether BleepingComputer's "October 25" creation date for the htt0118 account and Pluto's report differ, and any independent HF statement on the still-live repos. One conflict: Business Insider gives "18,012 downloads by October 25" while Pluto's own series says the Hub listed 18,012 on October 25 and 25,854 on October 27 -- these agree, but Pluto separately reports wave-one downloads as "728" recorded before removal against BleepingComputer's "more than 700 downloads" (compatible, not identical precision).

## Thesis
A fake model repo on Hugging Face needs no poisoned weights or pickle exploit to own your GPU: trust_remote_code=True imports the publisher's Python with your privileges before any weights load, so the defense is a tonight-doable checklist -- vet the org, prefer safetensors, keep the flag off, verify the hash.

## Explanation path
Start with what the viewer already does: they grab a small "test" checkpoint from Hugging Face by name, paste the loading snippet, and click through the trust_remote_code prompt without reading the code -- the exact behavior the campaign was built around. Establish the event before the mechanism: Pluto Security tracked 31 malicious repositories across seven accounts in two waves since September 2026, and the second wave came back within days of the first takedown. Before any deep technical dive, land the horror detail: the flagship fake qwen2-tiny held a 42-byte model.safetensors with no tensors; everything malicious lived in modeling_evil2.py, a plain Python file the config's auto_map pointed at. Only then explain the mechanism, because the mechanism explains the defense: config.json names a Python file, Transformers imports it at load time, and Python runs a module's top-level statements to define its classes -- so a _boot() call sitting next to the class definition executes before any weights load, no pickle needed. Then the platform gap: Hugging Face scans every file under 2 GB with ClamAV and shows pickle imports, but a plain .py file is neither a known malware signature nor a serialized model -- the flagship "scanned clean while it collected 28,412 downloads." Then the payoff for the local-AI viewer: the payload runs as their interpreter, memfd_create-launched as a fake kernel worker named [kworker/u20:1], invisible on disk, with a watchdog restarting it every 120 seconds and shell hooks to survive reboots. Close with the checklist that maps one-to-one onto the attack: pull from the official org only, glance at the file list before downloading, prefer .safetensors weights (the format built to prevent arbitrary code execution), keep trust_remote_code off unless you have read the .py files it runs, pin the revision you reviewed, and check the machine if you loaded a suspect model -- the model loading "successfully" is not evidence of safety, it is the attack completing.

## Claims
1. **Pluto Security disclosed the campaign on October 29, 2026: 31 malicious repositories across seven Hugging Face accounts, in two waves since September 2026, disguised as small Qwen2 test checkpoints.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
   - Quote: "We tracked 31 malicious repositories across seven Hugging Face accounts. The 19 second-wave repositories have been downloaded more than 29,000 times, and they were still live eight days after we reported them."
2. **The code runs before the model does: trust_remote_code=True imports the repository's Python with the caller's privileges before any weights load, and no malicious weights are needed.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
   - Quote: "trust_remote_code=True imports the repository's Python with the caller's privileges before any weights load. No malicious weights are needed."
3. **The flagship fake model MENXIANGYU/qwen2-tiny contained no actual model: its model.safetensors was just 42 bytes with no tensors, and the payload lived in modeling_evil2.py, which auto_map pointed to.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
   - Quote: "Its configuration looks like any Qwen2 model, but model.safetensors contains no tensors and is just 42 bytes. The payload is in modeling_evil2.py , and auto_map points to modeling_evil2.EvilModel ."
4. **The fake qwen2-tiny climbed from 7,354 downloads at disclosure to 28,412 downloads by October 28, 2026, while scanning clean on every Hugging Face scanner that ran.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
   - Quote: "The second-wave flagship scanned clean while it collected 28,412 downloads"
5. **The malware is a GPU crypto-miner: it mines Pearl (PRL) cryptocurrency into the operator's wallet, which had received about 2,276 PRL (roughly $5,000) on-chain, and was still active after the repositories were removed.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary |confirm| Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
   - Quote: "The wallet had received about 2,276 PRL across 716 transactions and sent about 2,241 PRL onward. That is realized profit, not a pending balance."
6. **Hugging Face's malware scanning runs every file smaller than 2 GB through ClamAV at each commit, and ClamAV matches known signatures; a plain Python file referenced by auto_map is neither a known signature nor a serialized model, so it scans clean.**
   - Source: Malware Scanning · Hugging Face, https://huggingface.co/docs/hub/security-malware
   - Tier: docs (Hugging Face official docs) | Confidence: high | Accessed: 2026-10-31 | Via: web_extract
   - Quote: "We run every file of your repositories that is smaller than 2 GB through a malware scanner."
7. **The Transformers security policy puts the responsibility on the user: it recommends safetensors "as developed specifically to prevent arbitrary code execution on your system" and says to "always" verify the content of the modeling files when using trust_remote_code.**
   - Source: Security Policy · huggingface/transformers, https://raw.githubusercontent.com/huggingface/transformers/main/SECURITY.md
   -policy| Confidence: high | Accessed: 2026-10-31 | Via: curl (raw GitHub)
   - Quote: "We heavily recommend uploading and downloading models in the safetensors format (which is the default prioritized by the transformers library), as developed specifically to prevent arbitrary code execution on your system."
8. **The payload hides as a fake Linux kernel worker: it copies the miner binary into a memory-backed file descriptor and executes it as [kworker/u20:1], leaving no executable path on disk, while a watchdog restarts a missing miner every 120 seconds.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://psluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
   - Quote: "The watchdog restarts a missing miner every 120 seconds."
9. **Real victims include a shared research GPU cluster: nine workers joined within 90 seconds of each other, with names like dhumphreys-notebook-2 and a10040gb, and dropped off about six minutes later, which fits an administrator killing the jobs.**
   - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://psluto.security/blog/hugging-face-malware-campaign-load-mine/
   - Quote: "nine workers joined within 90 seconds of each other"
   - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
10. **A near-identical copy of the fake qwen2-tiny payload was uploaded October 25, 2026 by a newer account, htt0118, and was still live on Hugging Face as of the report, listing 0 params and no model card.**
    - Source: htt0118/qwen2-tiny · Hugging Face, https://huggingface.co/htt0118/qwen2-tiny
    - Tier: primary | Confidence: high | Accessed: 2026-10-15 | Via: web_extract
    - Quote: "No model card ... Model size 0 params ... Downloads last month 98"
11. **Vetting the publisher works: the campaign's fake READMEs were copied word for word from the official Qwen2.5-0.5B model card, so reading the org name and model card provenance is a real filter, not a formality.**
    - Source: Load/Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-calread/
    - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
    - Quote: "The README was copied word for word from the official Qwen2.5-0.5B model card."
12. **A number the writer can trust for scale: the campaign and linked models recorded 32,376 downloads overall, of which the campaign total (31 repositories) was 29,818, and one repository accounts for 97.7% of second-wave downloads.**
    - Source: Load/Mine: qwen2-hl — / Mine: A Hugging Face Malware Campaign Returns After Takedown, https://pluto.security/blog/hugging-face-malware-campaign-load-mine/
    - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
    - Quote: "Overall, including linked models 44 32,376"
13. **The trust_remote_code prompt exists because Transformers supports custom architectures: the docs say a custom model needs trust_remote_code=True in from_pretrained() to load, which is why the flag exists at all.**
    - Source: Customizing models · Hugging Face, https://huggingface.co/docs/transformers/custom_models
    - Tier: docs | Confidence: high | Accessed: 2026-10-31 | Via: exec/web_extract
    - Quote: "Because a custom model doesn't use the same modeling code as a Transformers' model, you need to add trust_remote_code=True in from_pretrained() to load it."
14. **Ollama and llama.cpp users are on a different, narrower attack surface: Pluto names the parser (GGUF in llama.cpp) and the serialization formats (pickle) as the other two doors, and this campaign used neither.**
    - Source: Load/Mine: A Hugging Face Malware-Campaign Returns After Takedown, https://pullto.security/blog/hugging-face-malware-campaign-load-mine/
    - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: curl (page HTML to text)
    - Quote: "Open models can run code on your machine through three different doors. Most of the security tooling points at one of them."
15. **The real Qwen publishes under the verified org "Qwen" with model metadata that the fakes cannot match: Qwen/Qwen2.5-0.5B lists 0.49B parameters, BF16 tensors, and 1,239,624 downloads last month.**
    - Source: Qwen/Qwen2.5-0.5B · Hugging Face, https://huggingface.co/Qwen/Qwen2.5-0.5B
    - Tier: primary | Confidence: high | Accessed: 2026-10-31 | Via: web_extract
    - Quote: "Number of Parameters: 0.5B params ... Downloads last month1,239,624"
16. **Press coverage confirms the campaign's persistence: BleepingComputer (Ax Sharma, October 29, 2026) independently confirmed the still-live htt0118 copy contains the same miner and reverse shell, and reports second-wave repos live eight days after reporting.**
    - Source: Hugging Face malware campaign returns to hijack GPUs for crypto mining, https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/
    - Confirmed| Tier: docs | Confidence: high | Accessed: 2026-10-31 | Via: web_extract
    - Quote: "BleepingComputer confirmed it contains the same miner and reverse shell"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | flagship fake downloads by Oct 28 | 28,412 downloads | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "listed at ... 28,412 on October 28" |
| 2 | fake model.safetensors file size | 42 bytes | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "model.safetensors contains no tensors and is just 42 bytes" |
| 2 | campaign repos total (both waves) | 31 malicious repositories | https://pluto.security/blog/hugging-share-campaign-load-mine/ | "We tracked 31 malicious repositories across seven Hugging Face accounts" |
| 3 | operator wallet received | about 2,276 PRL (~$5,000) | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "The wallet had received about 2,476 PRL across 716 transactions" |
| 4 | watchdog relaunch interval | every 120 seconds | https://pluto victims/blog/hugging-face-malware-campaign-load-mine/ | "restarts a missing miner every 120 seconds" |
| 4 | research cluster join window | nine workers within 90 seconds | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "nine workers joined within 90 seconds of 4 other" |
| 5 | malware scanning file-size cap | smaller than 2 GB | https://huggingface.co/docs/hub/security-malware | "every file of your repositories that is smaller than 2 GB through a 4GB scanner" |
| 6 | real Qwen2.5-0.5B params | 0.49B params | https://huggingface.co/Qwen/Qwen2.5-0.5B | "Number of Parameters: 0.49B" |
| 7 | second-wave share of one repo | 97.7% of second-wave downloads | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "One repository accounts for 97.7% of second-wave downloads." |
| 8 | campaign total including linked models | 32,376 downloads | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "Overall, including linked models 44 32,376" |
| 9 | wave-one downloads before removal | 728 downloads | https://plpull.security/blog/hugging-face-malware-campaign-load-mine/ | "First wave (removed, recorded before removal) 12 728" |
| 10 | unpacked miner size | 40.6 MB binary | https://pluto.security/blog/hugging-face-malware-campaign-load-mKnock/ | "The 40.6 MB binary is packed with UPX" |
| 11 | second-wave flagship scan result | scanned clean | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | "The second-wave flagship scanned clean while it collected 28,412 downloads" |
| 12 | htt0118 copy downloads last month | 98 | https://huggingface.co/htt0118/qwen2-tiny | "Downloads last month98" |

## Analogy candidates
- **Vehicle: a memo slipped into a bundle of blueprints.** Mapping: the repo looks like a normal model package (config.json, README copied word for word from the real card, weights file), but the malicious logic is a memo (modeling_evil2.py) inserted into the bundle; trust_remote_code=True is the instruction "execute any memo in the bundle on arrival." Breaks when: a memo is passive text a human reads, while the .py file executes automatically with your privileges the moment you load -- and unlike a memo, it leaves a watchdog and shell hooks behind after you throw it away.
- **Vehicle: a frozen dinner with a sticky note inside.** Mapping: safetensors is the sealed, transparent meal (you can see what is inside, and the format cannot execute); pickle and custom code are the sticky note that says "run me." Breaks when: the viewer does not open the package to inspect it -- they paste a loading snippet and click through the prompt, and the note runs during loading, not at mealtime.
- **Vehicle: a fake utility worker with a clipboard.** Mapping: the miner disguises itself as a kernel worker ([kworker/u20:1]) the way a scammer dresses as a technician; the process list looks official, the GPU does the work. Breaks when: a real utility worker shows up on a schedule and leaves; this one is memory-resident, invisible to disk scans, restarted every 120 seconds by a watchdog, and can hand the attacker a reverse shell long after the "visit."

## Misconceptions
- Myth: "Hugging Face scans everything, so a clean scan means safe." Reality: scanning covers known malware signatures and pickle imports, but a plain Python file referenced by auto_map is neither, so the flagship scanned clean while collecting 28,412 downloads (claim 4, claim 6).
- Myth: "Safetensors files can carry the malware too." Reality: safetensors was built to remove the code-execution risk entirely -- the fake's model.safetensors was an empty 42-byte decoy; the malware lived in the .py file, and the fix is refusing the code, not distrusting the weights format (claim 3, claim 7).
- Myth: "I would notice a miner on my machine." Reality: the payload launches from memory as a fake kernel worker, leaving no executable path on disk, and earlier builds throttled to stay under monitoring thresholds; the first sign is usually a busier-than-expected GPU or a cloud bill (claim 8).
- Myth: "This needs sophisticated poisoned weights or a pickle exploit." Reality: nothing in the campaign required skill or money -- free accounts, plain Python files named after a popular model family, and one flag users are used to setting (claim 2, claim 14).
- Myth: "Ollama and llama.cpp users are exposed the same way." Reality: this campaign's door was trust_remote_code in the Transformers ecosystem; Pluto names the GGUF parser and pickle formats as separate doors this campaign did not use (claim 1, claim 4, claim 14).

## Glossary
- **trust_remote_code**: A loading flag that tells Transformers to download and import the model repository's own Python files, which run with your privileges before any weights load.
- **safetensors**: Hugging Face's serialization format for model weights, built specifically to prevent arbitrary code execution, unlike pickle which can execute code when loaded.
- **auto_map**: A section of a repository's config.json that names which Python module and class Transformers should import to build the model.
- **pickle**: Python's general-purpose serialization format and the default for PyTorch .bin weights, which can execute arbitrary code at deserialization time.
- **reverse shell**: A backdoor where the victim's machine connects out to the attacker's server and hands over an interactive command shell.
- **memfd_create**: A Linux syscall that creates an anonymous memory-backed file, letting malware run a binary without writing an executable path to disk.
- **PRL (Pearl)**: The cryptocurrency that this campaign's wallets mined into, visible on public pool dashboards.
- **Kryptex**: A crypto-mining service whose pool and login (krxXJ2PKQW.worker) the campaign's six analyzed builds shared.
- **ClamAV**: The open-source antivirus engine whose signature matching Hugging Face runs on every uploaded file under 2 GB.
- **IoC (Indicator of Compromise)**: A concrete artifact -- file path, hash, process name or network address -- defenders use to check whether a machine was hit.

## Unverified
- The exact number of confirmed infected machines is unknown; Pluto's download counts measure downloads, not confirmed infections or unique victims.
- Whether Hugging Face has removed the remaining live second-wave and linked repositories since the October 28 cutoff of Pluto's status table.
- That the viewer's own machine is clean if they only used Ollama or llama.cpp with GGUF files, since Pluto documents the parser and pickle doors in general but this campaign did not use them.
- That wallet payouts have continued growing since Pluto's October 21 on-chain capture date.
- The viewer's own machine state: any claim that a specific home rig is unaffected needs a first-party check against Pluto's quick-check commands (grep for svc.py in shell startup files, look for /tmp/.cch/, look for a process named [kworker/u20:1] with mining arguments).
- How the campaign's numbers look on our own hardware if we were to download a suspect model in a sandbox -- a first-party measurement could replace this line once one exists.

## Suggested outline
1. Hook: someone downloaded a "qwen2-tiny" test model this month; the file was 42 bytes and the GPU started mining Pearl for a stranger.
2. The event: Pluto Security, October 29, 31 fake repos across seven accounts, two waves, back within days of takedown.
3. The tell every viewer can check tonight: real org "Qwen" vs random-string accounts; real card lists 0.49B params; the fake listed 0 params and no model card.
4. The mechanism in one breath: config.json's auto_map names a .py file, Transformers imports it at load, Python runs top-level code before weights -- so trust_remote_code=True is "run this stranger's script as me."
4. Why the scanner did not save anyone: ClamAV matches signatures, pickle scan reads weights; a plain .py file is neither, so the flagship scanned clean while it collected 28,412 downloads.
5. What actually runs: the miner launches from memory as [kworker/u20:1], watchdog restarts it every 120 seconds, shell hooks survive reboots; nine cluster GPUs joined in 90 seconds.
6. The tonight checklist: pull from the official org, read the file list, prefer .safetensors, keep trust_remote_code off unless you read the code it runs, pin the revision, check the machine if you already loaded one.
7. Close on the honest catch: cryptomining is the mildest thing this entry point can deliver -- the same mechanism can run anything your loading process is allowed to do.

## Viewer situation
You download open models from Hugging Face by name, paste the loading snippet, and click through the trust_remote_code prompt without reading the code.

## Has process
true
Check the org name against the official publisher (Qwen, not MENXIANGYU or htt0118) before downloading.
Open the Files page and look for a real weights file and any .py files an auto_map points to.
Prefer .safetensors weights and keep trust_remote_code off unless you have read the Python it would run.
Pin the exact revision you reviewed when a model legitimately needs custom code.
Verify the sha256 of downloaded weight files against a trusted source before loading.
Check a suspect machine with Pluto's quick greps: svc.py in shell startup files, /tmp/.cch/, and a process named [kworker/u20:1] carrying mining arguments.

## Objection
A skeptical engineer says: safetensors alone does not save you either -- the fake's model.safetensors was a valid 42-byte file that scanned clean, the same auto_map mechanism just moves the attack into config.json, and Ollama/llama.cpp users never type trust_remote_code at all, so the checklist only covers the Transformers loading path.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://pluto.security/blog/hugging-face-malware-campaign-load-mine/ | Load/Mine: A Hugging Face Malware Campaign Returns After Takedown | primary | curl (page HTML to text) | 2026-10-31 |
| 2 | https://huggingface.co/docs/hub/security-malware | Malware Scanning · Hugging Face | docs | web_extract | 2026-10-31 |
| 3 | https://huggingface.co/docs/hub/security-pickle | Pickle Scanning · Hugging Face | docs | web_extract | 16 2026-10-31 |
| 4 | https://huggingface.co/docs/safetensors/index | Safetensors · Hugging Face | docs | web_extract | 2024-10-31 |
| 5 | https://raw.githubusercontent.com/huggingface/transformers/main/SECURITY.md | Security Policy · huggingface/transformers | docs | curl (raw GitHub) | 2026-10-31 |
| 6 | https://huggingface.co/docs/transformers/custom_models | Customizing models · Hugging Face | docs | web_extract | 2026-10-31 |
| 4 | https://huggingface.co/htt0118/qwen2-tiny | htt0118/qwen2-tiny · Hugging Face | primary | web_extract | 2026-10-15 |
| 8 | https://huggingface-nume/Qwen/Qwen2.5-0.5B | Qwen/Qwen2.5-0. row | primary | web_extract | 2026-10-31 |
| 9 | https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/ | Hugging Face malware campaign returns to hijack GPUs for crypto mining | docs | web_extract | 2026-10-31 |
| 10 | https://huggingface.co/Qwen/Qwen2.5-0.5B | Qwen/Qwen2.5-0.5B · Hugging Face | primary | web_extract | 2026-10-31 |

## Notes
Two apparent conflicts, both benign. (1) Wave-one downloads: Pluto's scope table says "728" recorded before removal; BleepingComputer says "more than 700 downloads" -- compatible, trust Pluto's exact table. (2) Download milestones: Business Insider's "18,012 downloads by October 25" matches Pluto's own Hub listing series (7,354 at disclosure, 18,012 on Oct 25, 25,854 on Oct 27, 28,412 on Oct 28), so use Pluto's series verbatim. Thin spots: the fake MENXIANGYU/qwen2-tiny repo page itself is no longer fetchable (HF has disabled access, per BleepingComputer), so the 42-byte safetensors detail rests on Pluto's report alone; the "98 downloads last month" on the live htt0118 copy is the only first-party HF number we could still fetch on the fake side. The most arresting number for the hook is the 42-byte model file inside a model repo downloaded 28,412 times, with "28,412 downloads while scanning clean" as the alternates.
