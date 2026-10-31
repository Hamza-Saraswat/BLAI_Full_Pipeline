---
slug: 2026-10-31-fake-qwen2-checkpoints-the-tru
format: classic
structure: worked-example
style_pack: terminal
value_types: EQUIPS,TEACHES
promise: after 35 seconds you can look at any Hugging Face model page and know whether to load it
target_duration_s: 44
brief: 2026-10-31-fake-qwen2-checkpoints-the-tru-brief.md
drafts: 2026-10-31-fake-qwen2-checkpoints-the-tru-drafts.md
---

# Fake Qwen2 checkpoints: the page you trust is the page you verified

## Decisions

- Structures tried: how-to-three-moves (draft A) and worked-example (draft B). B won 20-18 on
  the judge rubric (payoff timing, voice, navigation, teaching rows). Judge note recorded: its
  row-3 "invented specifics" flags (svc.py, Pearl, Pluto) are false positives -- all three are
  in the research brief; the judge saw only an excerpt. Scores were equal on that row, so the
  verdict stands.
- Hook: "You download open models from Hugging Face and click trust." (situation pattern,
  candidate 3 of 10). Why: names the viewer's exact click-through; number-shock and
  named-contradiction were rotation-banned; tonight was spent by draft A.
- No grafts taken: A's hook scored equal on row 1 (2-2), below the two-point graft threshold.
- Labels: B carries none (worked-example navigates by content); A used Move one/two/three
  legally but the judge called them mechanical under the deletion test.

## Hook candidates

1. Three moves and your next Hugging Face model stays clean tonight. (draft A's hook)
2. Three checks and no fake model loads tonight.
3. *You paste the snippet. The repo runs its own code first. (basis of the pick; final wording
   above)
4. You click trust. That click runs a stranger's Python. (used as frame-1 text)
5. The clean scan isn't the proof. The org name is.
6. Your scanner isn't the safety. The org name is.
7. A fake Qwen2 scanned clean to twenty-eight thousand downloads. (banned: number-shock)
8. Hugging Face or Qwen? The org name decides.
9. Three moves and no fake model loads tonight.
10. You download by name. The repo runs first.

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | You download open models from Hugging Face and click trust. The repo's code runs before the model does. | You click trust. The repo runs first. | Frame 1 opens on the finished composition, caret blinking from 0.30s: black terminal; frame-one text typewriters in amber over a blinking block cursor; on "The repo's code runs before the model does." a second prompt line prints beneath. | hyperframes | centered-stack | 6.2 |
| s02 | explain | Take qwen-two-tiny. Perfect page. The card was copied from the real Qwen card. The org was a random string. Scanned clean past twenty-eight thousand downloads. | MENXIANGYU is not Qwen. 28,412 downloads. ClamAV: clean | Split-compare rises in place: left a repo card for "Take qwen2-tiny" with README lines mirroring the real Qwen card, right the org field stamped amber "MENXIANGYU"; a download counter settles at 28,412 beside a green ClamAV PASS tag on "Scanned clean past twenty-eight thousand downloads." | hyperframes | split-compare | 6.6 |
| s03 | explain | The weights file is forty-two bytes, holding no tensors. The config points straight at that Python file. | model.safetensors: 42 bytes -> auto_map: modeling_evil2.py | Diagram-flow, terminal file listing: "model.safetensors" scales in tagged "42 B" on "forty-two bytes, holding no tensors"; an amber arrow draws from config auto_map to "modeling_evil2.py" on "The config points straight at that Python file." | hyperframes | diagram-flow | 4.8 |
| s04 | explain | You click trust_remote_code, the flag that runs the repo's Python before weights load. The weights never mattered. | trust_remote_code=True: repo Python runs first | Timeline with two ticks: "repo Python runs" lights amber first on "the flag that runs the repo's Python before weights load"; the "weights load" tick greys out on "The weights never mattered." | hyperframes | timeline | 5.9 |
| s05 | explain | A miner hides as a kernel worker, a background process. A watchdog restarts it every two minutes. Your GPU mines Pearl. This ride is Transformers-only; Ollama and llama.cpp never type the flag. | [kworker/u20:1] GPU -> PRL | Centered-stack process list: one amber line "[kworker/u20:1]" fades in among grey system processes on "A miner hides as a kernel worker"; a watchdog loop stamp "120 s" appears on "restarts it every two minutes"; on "never type the flag," the process list dims. | hyperframes | centered-stack | 10.0 |
| s06 | payoff_close | Delete the repo, grep startup files for svc.py. The page you trust is the page you verified. | grep svc.py, ps [kworker] | Grid of two checklist cells typewrites in on "grep startup files for svc.py," each cell ticking amber; the grid holds through the payoff line, then wordmark settle. | hyperframes | grid | 5.2 |

## Notes for review

- "twenty-eight thousand downloads" is the rounded spoken form; the verbatim figure 28,412
  (Pluto's count, October 28) is on screen in s02.
- "every two minutes" is the spoken form of "every 120 seconds" (watchdog interval, Pluto).
- The s05 catch line says "Transformers-only" which is Pluto's scope, not a safety claim about
  Ollama/llama.cpp; the brief marks their exposure unverified.
- Judge flagged svc.py and Pearl as invented; both are Pluto's own IoCs (grep for svc.py; the
  coin PRL is Pearl). No change needed.
