---
slug: 2026-09-24-qwen-image-2-1-edits-pictures
stage: 04-script
winner: A (how-to-three-moves)
score: 21 - 19
judge: kimi-k3 blind call, 2026-09-24
---

# Drafts: 2026-09-24-qwen-image-2-1-edits-pictures

Both drafts passed validate_storyboard (0 blockers) and all nine eval_short gates before judging.

## Score table (rubric rows 1-8, max 3 each)

| Row | Draft A | Draft B |
|-----|---------|---------|
| 1 | 2 | 3 |
| 2 | 2 | 3 |
| 3 | 3 | 1 |
| 4 | 3 | 0 |
| 5 | 3 | 3 |
| 6 | 3 | 3 |
| 7 | 2 | 3 |
| 8 | 3 | 3 |

Total A 21, Total B 19. Winner: A. No tiebreak needed.

## Grafts

None. The loser's hook did not outscore the winner's by two on row 1 (B 3, A 2), so no hook swap; no sentence moved.

## What the losing shape would have needed

The news-react needed to keep the unverified 'under twice as slow' figure out of narration, since its own review notes flag 2x as forbidden; that one drifted claim capped row 3 at 1 and broke hard constraint 6, zeroing row 4. It also needed its spoken consequence to arrive as early as its visuals, because the narration makes the viewer wait roughly twenty seconds for the payoff the first frame already demonstrates.

## Draft A in full (winner, how-to-three-moves, hook pattern tonight)

- title: Qwen-Image-2.1 photo edits on your GPU
- hook_text: Three moves: local photo edits
- words: 323; music_mood: steady-build

### s01 hook (centered-stack, hyperframes, est 6.9s)
- narration: Three moves and Qwen Image two point one edits your photos tonight. The folder you keep meaning to fix stays on your own drive.
- on-screen: Three moves: local photo edits
- visual: Frame 1: centered amber hook text 'Three moves: local photo edits', fully legible, above a dim photo thumbnail. A soft scale pulse on the text begins almost immediately after the open. On 'edits your photos tonight', a second thumbnail rises in place beside the first, same photo with a swapped backg

### s02 explain (split-compare, hyperframes, est 15.2s)
- narration: Qwen Image two point one is a single model. It makes pictures, and it edits the ones you already have. You hand it a photo and an instruction, like change the background to a sunset beach. Everything outside the edit stays put. People still look like themselves.
- on-screen: same model: makes and edits | everything else stays put
- visual: Split-compare: left panel shows a portrait on a plain background, right panel mirrors it. On 'a single model', one chip icon fades in centered above the panels. On 'change the background to a sunset beach', the right panel's background fades to a sunset beach while the person stays identical. On 'st

### s03 explain (centered-stack, manim, est 13.4s)
- narration: Here's the wall. The part that paints the image, the transformer, is fourteen point two three gigabytes at full precision. The text encoder, the part that reads your instruction, is even bigger. That does not fit a gaming card.
- on-screen: 14.23 GB for the transformer | text encoder: even bigger
- visual: Centered stack. On 'fourteen point two three gigabytes', large digits '14.23 GB' scale in center frame above a transformer block icon. On 'even bigger', the lower caption hard-cuts to 'text encoder: even bigger', never a cross-dissolve. On 'does not fit', a GPU card outline below fills past its capa

### s04 explain (diagram-flow, manim, est 20.0s)
- narration: Quantization is the shrink: each stored weight keeps fewer bits. Think of pi with its long tail rounded off. The number still works, and the file gets much smaller. You trade a little fidelity, and the loss is not even; exact math notices first. Unsloth ships the shrink as an int eight file, seven point two six gigabytes on disk.
- on-screen: fewer bits per weight | smaller file, a little fidelity
- visual: Diagram-flow, three nodes left to right: a stack of tall bars (a weight), a trim icon, a shorter stack. On 'keeps fewer bits', the bars shorten in place. On 'tail rounded off', they trim again. On 'file gets much smaller', a file icon at the last node scales down. On 'trade a little fidelity', one c

### s05 explain (split-compare, manim, est 18.6s)
- narration: Unsloth says its F P eight build, another eight-bit format, runs in six gigabytes of video memory, using offloading. Offloading parks pieces of the model in system memory and swaps them in as needed. Treat those figures as Unsloth's estimates, not tested minimums. Slower, yes, but gentler than you would guess. Your patience does the heavy lifting.
- on-screen: 6GB VRAM plus offloading | estimates, not tested minimums
- visual: Split-compare: left panel a GPU block labeled '6GB VRAM', right panel a larger block labeled 'system RAM'. On 'parks pieces of the model in system memory', three small cubes rise in place inside the RAM block. On 'swaps them in', one cube on each side alternates glow, two elements at most. On 'estim

### s06 explain (timeline, hyperframes, est 8.6s)
- narration: Step one: install Unsloth Desktop on your gaming PC. It is the app that runs these models locally. Let it update to the latest version.
- on-screen: Step one: install Unsloth Desktop
- visual: Timeline: three hollow dots across the top of the safe area; the first fills amber on 'Step one'. Center: an installer window fades in with an empty progress bar. On 'install Unsloth Desktop', the bar fills left to right. On 'update to the latest version', a small tag reading 'latest' rises in place

### s07 explain (grid, hyperframes, est 9.3s)
- narration: Step two: pick Qwen Image two point one in the Model hub and choose int eight. It is the safer pick for fidelity. The app downloads the quant and uses it automatically.
- on-screen: Step two: model hub, choose INT8
- visual: Grid of six model cards, a hub view. On 'pick Qwen-Image-2.1', one card scales up slightly and gains an amber border. On 'choose INT8', two chips fade in on that card, INT8 and FP8, and the INT8 chip fills amber. On 'safer pick for fidelity', a small check rises in place on the INT8 chip, and the se

### s08 payoff_close (split-compare, hyperframes, est 13.4s)
- narration: Step three: open the Edit tab, load your photo, and type your edit: remove the watch. Hit generate, and lower the resolution if memory runs out. The watch is gone, and everything else is exactly where you left it.
- on-screen: Step three: Edit tab, type edit | remove the watch
- visual: Split-compare Edit tab. Left: a vacation photo with a watch on a wrist, circled. On 'type your edit', the prompt 'remove the watch' types into the prompt box, the only animating text. On 'Hit generate', the generate button pulses once. On 'The watch is gone', the right panel fades from empty to the 

## Draft B in full (news-react-so-what, hook pattern named-contradiction)

- title: Qwen-Image-2.1 photo edits on 6GB VRAM
- hook_text: It fixes yours, locally
- words: 333; music_mood: curious-tech

### s01 hook (centered-stack, hyperframes, est 5.9s)
- narration: Qwen Image two point one doesn't just make pictures. It fixes your photos, locally. No credits, no uploads.
- on-screen: It fixes yours, locally
- visual: Frame 1: a beach-photo card centered with the hook text fully legible beneath it. On the opening word, a red circle scales in around a metal watch on a wrist in the photo. On 'fixes', the watch fades out, leaving clean skin. On 'locally', a small GPU icon rises in place at the left of the safe area.

### s02 explain (split-compare, hyperframes, est 15.5s)
- narration: This week Qwen released Qwen Image two point one, one open-weights model that both creates and edits images. The same weights that draw a picture can take your photo plus an instruction and return the edit. Days later Unsloth shipped it with slimmed files.
- on-screen: Shipped this week | One model: creates and edits
- visual: Header 'Shipped this week' fades in on the first sentence. Split screen below: left panel shows a typed prompt with a generated image fading in on 'creates'; right panel shows the same beach photo plus a typed instruction, and the edited result hard-swaps in on 'edits'. On 'Unsloth shipped it', a sm

### s03 explain (centered-stack, hyperframes, est 12.1s)
- narration: The consequence for you: photo editing now fits the card you already own. Not a datacenter card. The one in your gaming rig. Cloud editors want credits and your uploads. This stays on your desk.
- on-screen: Fits the card you own | No credits, no uploads
- visual: Centered stack: the text 'Fits the card you own' above a gaming GPU silhouette. On 'Not a datacenter card', a faint server-rack outline behind the GPU scales down and fades out while the GPU rises slightly forward. On 'Cloud editors', a small cloud icon with an upload arrow fades in at left, then fa

### s04 explain (grid, hyperframes, est 11.7s)
- narration: Editing here means plain instructions on real photos. Remove the watch. Change the background to a sunset beach. Mark spots with circles or a painted mask; everything outside stays untouched. Faces keep looking like themselves.
- on-screen: Remove the watch | Background: sunset beach | Everything else stays put
- visual: Two-by-two grid of small photo cards. Top-left: portrait with a red circle on a wrist watch; on 'Remove the watch' the watch fades out. Top-right: same portrait; on 'sunset beach' the background hard-swaps to a sunset beach. Bottom-left: a painted mask over a jacket fades in on 'painted mask'. Botto

### s05 explain (diagram-flow, manim, est 14.1s)
- narration: Why did this need a shipping week? Memory. The full model's image core, the part that paints, is fourteen point two three gigabytes alone. The text encoder, the reader that turns your prompt into numbers, is bigger still. That is not a gaming rig.
- on-screen: Image core alone: 14.23 GB | The prompt reader is bigger
- visual: Left side: a block labeled 'image core' rises in place; on 'fourteen point two three gigabytes' its label '14.23 GB' fades in beside it. On 'bigger still', a taller unlabeled block for the prompt reader rises above it. Right side: a gaming GPU outline with a short memory bar. On 'not a gaming rig', 

### s06 explain (centered-stack, manim, est 18.6s)
- narration: Unsloth's fix is a quant, a copy storing each number in fewer bits. It's like rounding pi to three point one. Most accuracy survives and the file shrinks a lot, though the loss is not uniform and exact math notices first. The int eight build cuts that core to a seven point two six gigabyte file.
- on-screen: Fewer bits per number | π ≈ 3.1 | About half the size
- visual: Centered: 'π ≈ 3.1' in large type fades in on 'rounding pi', with a ghosted tail of extra digits behind it that fades away. Below, a wide block labeled 'full core' hard-swaps on 'shrinks a lot' to a block about half as wide labeled 'int eight'. On 'exact math notices first', one tiny digit flickers 

### s07 explain (split-compare, manim, est 19.0s)
- narration: Unsloth says the F P eight build can run on six gigabytes of video memory, using offloading. That parks pieces in system memory and pays a speed toll, under twice as slow. Those memory figures are Unsloth's estimates, not tested minimums. Both files are lossy: you trade a little fidelity, and int eight keeps more.
- on-screen: Runs on 6 GB VRAM | Estimates, not minimums | Lossy: a little fidelity
- visual: Left: a horizontal bar labeled '6 GB' fades in on 'six gigabytes of video memory'. On 'offloading', an arrow rises from the bar to a system-memory chip icon and two small blocks travel up it. On 'speed toll', the bar's fill creeps slowly once. On 'estimates', the line 'Estimates, not minimums' fades

### s08 payoff_close (centered-stack, hyperframes, est 15.9s)
- narration: Tonight, install Unsloth Desktop and pick Qwen Image two point one with an int eight or F P eight file. Load your photo in the Edit tab, type the instruction. Remove the stranger from the vacation shot, and the only machine that sees it is yours.
- on-screen: Pick the model, open Edit tab | It fixes yours, locally
- visual: Mock of Unsloth Desktop: a model row reading 'Qwen-Image-2.1' highlights on 'pick', with an int eight chip beside it. On 'Edit tab' the view hard-cuts to the Edit tab with the beach photo loaded, and the instruction 'remove the watch' types out letter by letter. On 'Remove the stranger', the photo h

