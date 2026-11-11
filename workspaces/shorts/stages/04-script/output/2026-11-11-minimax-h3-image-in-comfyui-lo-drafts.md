# Drafts: 2026-11-11-minimax-h3-image-in-comfyui-lo

Both blind drafts in full, the judge's table, the winner, the graft, and what the loser needed.
Written by two separate kimi-k3 calls from the same brief and voice law, different structures,
different assigned hook patterns; judged by a third.

## Draft A (how-to-three-moves, hook pattern "tonight")

structure how-to-three-moves | hook_text "MiniMax H3 runs tonight" | target 112s | 11 scenes
- [s01 hook centered-stack 9.7s] MiniMax's new image model runs on your own GPU tonight, in three moves. Three days ago MiniMax published the weights. No server between your prompt and the picture.  ||  ON SCREEN: MiniMax H3 runs tonight | weights published | no server in the middle
- [s02 explain split-compare 9.7s] Here's what you're installing. The weights are just model files. One checkpoint, one of those files, does both jobs: writes pictures from text, edits photos you already have.  ||  ON SCREEN: 1 checkpoint: generate + edit
- [s03 explain giant-number 7.9s] It renders natively at sixteen megapixels, poster sharp. And it's distilled to six sampling steps, six denoising passes, no negative prompt to babysit.  ||  ON SCREEN: 16 MP native | 6 steps, no negative prompt
- [s04 explain timeline 11.7s] Step one: install the ComfyUI update, the latest one. ComfyUI is the free app where you wire boxes into workflows. Its core merged H three Image support yesterday. No custom nodes, no third-party packs.  ||  ON SCREEN: Step 1: update ComfyUI | core support: merged | no custom nodes
- [s05 explain giant-number 11.0s] Step two: pull the four files into three folders. They live on the Comfy-Org page at Hugging Face, the app store for model files. Together they cost about fifty-five gigabytes of disk.  ||  ON SCREEN: Step 2: 4 files, 3 folders | Comfy-Org on Hugging Face | 54.79 GB total
- [s06 explain timeline 11.0s] That's the real price of tonight, so start the download and go make dinner. A cup of coffee pours while the bar crawls. When it finishes, each file has a named home.  ||  ON SCREEN: 54.79 GB | start download, go make dinner
- [s07 explain grid 13.8s] The diffusion model, the core that refines noise into a picture, goes in diffusion models. The text encoder, which reads your prompt into numbers, goes in text encoders. The VAE, the decoder that finally makes your PNG, goes in vae.  ||  ON SCREEN: diffusion_models: DiT | text_encoders: encoder | vae: VAE
- [s08 explain centered-stack 10.0s] Step three: open the template and press run. Templates are ready-made workflows that ship inside ComfyUI. Open MiniMax H three Image Text to Image; the graph is already wired.  ||  ON SCREEN: Step 3: open template, run | MiniMax-H3-Image: Text to Image
- [s09 foreshadow split-compare 14.1s] It starts small on purpose. Nobody has published a VRAM floor yet; VRAM is your graphics card's memory. The R T X thirty sixty stories are about MiniMax's video model from August, not this one. Watch it on the first pass.  ||  ON SCREEN: starts small on purpose | VRAM floor: unpublished
- [s10 foreshadow grid 4.1s] Headroom? Raise the resolution selector. Choking? Shrink the canvas, keep the model.  ||  ON SCREEN: headroom: raise resolution | choking: shrink canvas
- [s11 payoff_close centered-stack 8.6s] There's your picture, rendered by your own GPU. No server, no queue, no per-image bill. Big companies need written permission; you just needed disk space.  ||  ON SCREEN: rendered locally | no server, no queue, no bill | license: written permission

## Draft B (contrarian-take, hook pattern "wrong-diagnosis")

structure contrarian-take | hook_text "Think it's too big? It isn't." | target 121s | 11 scenes
- [s01 hook centered-stack 9.3s] You think this model needs a datacenter. It needs one folder. You've made pictures on somebody else's server, and assumed your PC can't hold one this size.  ||  ON SCREEN: Think it's too big? It isn't. | somebody else's server
- [s02 explain timeline 11.0s] Three days ago, MiniMax published H three Image's weights, the files that make the model work, free to download. ComfyUI, the free node app for running models yourself, merged native support yesterday.  ||  ON SCREEN: weights open on Hugging Face | merged into ComfyUI core
- [s03 explain giant-number 7.9s] The Comfy-Org repack page already shows three hundred fifty-one thousand downloads in its first month. That's not a datacenter crowd; that's home machines.  ||  ON SCREEN: 351,803 downloads, first month
- [s04 explain diagram-flow 13.1s] So what is it? One checkpoint, the trained model file, that writes pictures from text and edits photos you feed it. Its core is a diffusion transformer, thirty-three billion parameters of machinery that turns noise into a picture.  ||  ON SCREEN: 1 checkpoint: generate + edit | 33.1B parameters
- [s05 explain split-compare 12.8s] Raw, it's too big for a home card. Comfy-Org's repack uses int eight, storing numbers more roughly so the files shrink, like rounding pi to three point one. The loss isn't perfectly even, but most accuracy survives.  ||  ON SCREEN: raw files: overflow | INT8: rougher numbers | pi, rounded
- [s06 explain grid 15.9s] The install is four files into three folders. The diffusion model goes in diffusion models. The text encoder, the part that reads your prompt into numbers, goes in text encoders, twice. The VAE, the decoder that gives you a PNG you can open, goes in vae.  ||  ON SCREEN: 4 files, 3 folders | diffusion_models, text_encoders, vae
- [s07 explain giant-number 5.9s] Total cost, about fifty-five gigabytes of disk. That's the whole bill unless your card is too small.  ||  ON SCREEN: 54.79 GB total
- [s08 explain centered-stack 10.3s] Update ComfyUI itself first, because support merged into the core app yesterday; no custom node packs to hunt. ComfyUI's built-in MiniMax template, a ready-made wiring, does the graph for you.  ||  ON SCREEN: update ComfyUI | MiniMax-H3-Image: Text to Image
- [s09 foreshadow split-compare 6.9s] The MiniMax template starts small on purpose, so smaller cards don't choke. Raise the resolution once your card shows headroom.  ||  ON SCREEN: starts small on purpose | headroom: raise resolution
- [s10 foreshadow grid 15.5s] Now the catches. Nobody has published a VRAM floor, the graphics-card memory this model must fit in, for H three Image. The R T X thirty sixty stories are about MiniMax's video model from August, not this one. Speed on your card is unmeasured, too.  ||  ON SCREEN: VRAM floor: none published | RTX 3060 stories: the video model | local speed: unmeasured
- [s11 payoff_close centered-stack 12.1s] Four files, three folders, one update, and MiniMax's image model lives in a folder on your drive. If your card has the memory, you're generating tonight. If not, the disk space is all you've spent.  ||  ON SCREEN: Not a datacenter. One folder. | your GPU, tonight

## Judge

SCORES
| row | A | B |
|-----|---|---|
| 1 hook | 2 | 1 |
| 2 payoff timing | 2 | 2 |
| 3 specificity | 3 | 2 |
| 4 voice | 3 | 2 |
| 5 navigation | 3 | 2 |
| 6 difference | 2 | 3 |
| 7 repeat test | 2 | 2 |
| 8 teaching | 2 | 3 |
| TOTAL | 19 | 17 |

WINNER: A

REASON: A names the product in the hook, pays "runs tonight" with "weights published, no server" inside eight seconds, and opens a count ("three moves") that its three legal, action-naming steps close; its numbers are spent one at a time with no wobble. B has the fresher shape and the best single teaching beat in either draft (int eight via rounded pi), but its hook withholds the product, the proof that "it isn't too big" lands two full scenes after the break, and "three hundred fifty-one thousand downloads in its first month" collides with its own "three days ago".

GRAFTS
- The sentence "The R T X thirty sixty stories are about MiniMax's video model from August, not this one." moves from B s10 into A s09, placed after the VRAM-floor sentence and before "Watch it on the first pass." Reason: this is the one beat B says that A says worse by omission; a viewer who searches will meet the 3060 stories before any benchmark, and A's caution scene does not arm them. The graft adds a single spoken number to a scene that currently has none, keeps the impersonal-declarative register A already uses, leaves A's step structure and its opened-and-closed count untouched, and grows s09 by roughly four seconds without rewriting any surrounding beat.
- No second graft. B's int eight explanation is the loser's strongest material, but A never raises file size or quantization, so inserting it would require building a new beat and rewriting the beats around it; the rules say do not graft in that case.

LOSER-WOULD-HAVE-WON-IF: B would have won if the hook carried the product name ("You think MiniMax's new image model needs a datacenter") and the size-proof, the repack plus the download count, landed within eight seconds of the break instead of behind two scenes of timeline. It also needed to kill the "first month" claim that fights "three days ago", and to spend its one permitted not-X-but-Y on the close rather than three times across the script.

## Graft applied

"The R T X thirty sixty stories are about MiniMax's video model from August, not this one." moved
from B s10 into A s09, between the VRAM-floor sentence and "Watch it on the first pass." One
sentence, no structural rewrite; s09 grew to 14.1 s; validator and all nine eval gates re-run
clean after the graft. No other line moved.

## What the losing shape would have needed (judge's words)

See the verdict's LOSER-WOULD-HAVE-WON-IF above: the product in the hook, the size-proof within
eight seconds of the break, the "first month" claim reconciled with "three days ago", and one
not-X-but-Y spent on the close instead of three.
