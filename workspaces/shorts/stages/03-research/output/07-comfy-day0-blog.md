# Source: https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui
# Fetched: 2026-11-11 via hermes web_extract

[![ComfyUI Newsletter](https://substackcdn.com/image/fetch/$s_!uyu8!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9545d140-0202-4a03-b9a2-58724fc1be59_500x500.png)](https://blog.comfy.org/)

# [ComfyUI Newsletter](https://blog.comfy.org/)

SubscribeSign in

# MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video

### An open-weights omni-modal video model with real stereo sound and 2K output -- this powerful model is greatly optimized in ComfyUI and can run locally on a 3060.

[![Rob's avatar](https://substackcdn.com/image/fetch/$s_!LqNK!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb173e2f-3d4c-479b-b41b-2b24c2216010_768x768.png)](https://substack.com/@hellorob)[![Alexis Rolland's avatar](https://substackcdn.com/image/fetch/$s_!7pf0!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77690c4b-7475-4a45-863a-3b37d64dd1dd_600x602.png)](https://substack.com/@rollandalexis)

[Rob](https://substack.com/@hellorob) and [Alexis Rolland](https://substack.com/@rollandalexis)

Aug 02, 2026

10

2

Share

MiniMax H3 dropped today with open weights, and it’s natively supported in ComfyUI as of this morning. Day zero.

This is a next-generation open-weights video model. Feed it text, images, video, or audio and it generates video with real stereo sound, up to 2K, up to 15 seconds a clip. It is MiniMax’s third-generation video model, following Hailuo 01 and Hailuo 02, and the first the company has released with open weights.

[Try on Comfy Cloud](https://links.comfy.org/4pTj4QV)

## Model Highlights

- **Text-to-video** -- prompt only.

- **Image-to-video** -- bring an image to life.

- **First-and-last-frame** -- control the opening frame, the closing frame, or both, and let the model fill in the rest.

- **Reference-to-video** -- supply reference images, video, or audio and carry a subject, a motion, or a voice through the clip.


Output runs to 2K and up to 15 seconds. Audio is generated with the video in the same pass, in stereo, not bolted on afterward.

#### Multimodal context understanding

This is the capability MiniMax leads with, and it’s what collapses five separate tasks into one model. Real work rarely draws on one modality. H3 takes images, audio, and video together and resolves them against a prompt that explains how they relate. Describe the relationship between your inputs and the shot you want, and the model handles the cross-modal work itself.

#### Native stereo audio

Audio is a property of the model, not a post-process. Every audio output is native stereo.

#### Editing and motion transfer

Motion transfer is the one that matters most for graph work. A reference video can supply movement -- a camera move, a performance, a cutting rhythm -- while the subject and style come from elsewhere. Combined with in-place editing, that means iterating on a shot.

## Example Outputs

```
Bold comic-book ink style, heavy linework, red and blue-black palette, night city. Use <Picture 2> and <Picture 1> as reference frames and <Audio 1> exactly as it is.
CUT 1: top-down view of the little boy superhero on the rooftop -- red cape fluttering in the wind, hands planted on his hips, freckles and a cocky grin as he looks straight up into the camera. The camera slowly descends toward him as he delivers his line -- as he speaks, comic-book graphic overlay text word by word in sync with his voice: "GET READY TO" - "MEET" -- "YOUR" -- "MAKER" -- huge jagged comic lettering, white with heavy black outlines and red drop shadows, tilted at scrappy angles, until the three words hang stacked in the air above him between his face and the lens.
TRANSITION: a violent WHIP PAN off the rooftop that SMEARS the floating words away with it, motion-streaked --
CUT 2: low hero angle on the colossal black mech-kaiju towering over the skyline as it rears back and unleashes a GIANT terrifying ROAR -- jaws wide with fangs, red eyes and chest-core flaring blinding bright, blue lightning arcing off its head, the roar's shockwave rippling dust and rattling windows down the buildings, comic-style speed-lines and ink splatter bursting from the impact of the sound. It leans INTO the camera as the roar peaks. Hold on the roar.
```

```
Editorial tech product film. The transparent gaming mouse from <Picture 1> in its original scene: a pitch-black studio void with a dark, subtle reflective surface, lit by dramatic duotone vibrant blue and warm neon orange rim lighting, deep soft shadow falloff into pure black. Monochromatic dark palette with electric blue and amber accents. Material motif: glowing internal metallic micro-components and glossy acrylic refractions. The environment is constant throughout.
SHOT 1: The scene opens exactly on image 1, the mouse resting confidently on the dark surface; the blue and orange lights slowly pulse brighter, refracting deeply through the transparent acrylic shell as the camera executes a slow, deliberate push-in to reveal the intricate circuitry.
SHOT 2: Cut to an extreme macro profile of the ridged scroll wheel and layered internal micro-components; the camera glides slowly along the side as a sharp beam of warm orange light sweeps across the metallic textures, contrasting perfectly against the deep blue ambient glow.
SHOT 3: Cut to a low-angle beauty shot: the mouse levitates weightlessly a few centimeters above the dark reflective surface, rotating in a slow, precise orbit; the duotone lighting flares gently along the glassy transparent edges before fading slowly into a sleek silhouette.
Audio: deep pulsing sub-bass room tone, sharp tactile mechanical clicks, a sweeping glassy whoosh on cuts, and a rising electronic swell that resolves to near-silence on the final fade.
```

```
High-fashion editorial film, luxurious slow motion throughout, soft gradient studio sky.
MUSIC & SFX: a cinematic score fusing deep taiko drums, shimmering koto plucks and modern sub-bass drives the film

SHOT 1: beside her, the mask hangs BROKEN -- shattered into the floating shard formation of <Picture 2>, every kintsugi piece suspended and slowly rotating in place, the gold seams between them dim and waiting. She turns her eyes to it.
SHOT 2: THE ASSEMBLY, with enormous energy -- the gold seams IGNITE, arcs of molten light leaping shard to shard like welding fire, and the pieces snap together one by one, accelerating from slow to rapid-fire, each snap flaring gold, molten droplets spinning off, the surrounding liquid ribbons shuddering with shockwave ripples -- until the final shard slams home and the whole mask fuses, its kintsugi veins blazing.
SHOT 3: the golden dragon of <Picture 3> SWOOPS through the frame in one huge serpentine fly-through -- red glass antlers first, its coils wrapping the space around her and the mask, scales throwing golden light, its wake dragging the crimson liquid into a spiral behind it.
SHOT 4: in the dragon's wake the mask magnetically RIPS across the air onto her face -- a fast, hard, perfectly straight pull -- seating with a deep flare as every gold crack lights, and glowing kintsugi veins spread from the mask's edge down her neck and across the sunset jacket, embroidery igniting thread by thread.
SHOT 5: she descends and lands softly ON the dark liquid wave, snapping into a poised warrior stance and holding it like a lookbook frame -- the dragon coiled behind her shoulder, both liquids spiraling upward around her into a double helix. Held editorial poster frame as the camera settles.
Use <Picture 1>, <Picture 2>, <Picture 3> as reference images.
```

```
Vibrant fisheye product commercial, hyper-saturated summer light, the woman from <Picture 1> in a yellow raincoat crouched by a jungle waterfall holding a rainbow-gradient soda can toward the lens, condensation dripping.
MUSIC: an upbeat tropical house track drives the entire film -- punchy kick drum, bright steel-drum plucks, warm bass groove.

CUT 1 : the fisheye hero frame -- as she looks into the lens, GIANT BOLD TYPOGRAPHY stamps across the background behind her, one word per beat: "STAY" then "HYDRATED" -- massive clean white block letters spanning the whole scene, curving with the fisheye distortion, sitting behind her but in front of the waterfall. She reaches her opposite hand towards the can and hooks a finger under the tab.
TRANSITION: extreme close-up of the tab -- it OPENS with a crisp CLICK-hiss, and exactly on the click the fisheye lens iris shutters closed to black, like a camera blinking.
CUT 2: the iris reopens on a new POV -- the can EXTREMELY distorted in the foreground, huge and warped by the fisheye, she smiles and dumps the liquid out of the can onto the floor, droplets scattering weightlessly, sunlight refracting rainbow through the stream, the waterfall soft behind her.
TRANSITION: she lowers the can and one fat droplet falls toward the lens, filling the frame --
CUT 3: through the droplet into the final wide: the rainbow can floating upright and serene in the turquoise waterfall pool, label facing camera, bobbing gently in the mist, the waterfall thundering softly behind -- and "STAY COMFY" shimmering as a reflection on the water's surface beside it. Hold the product hero frame.
Crisp, joyful, premium product-ad energy. Fisheye distortion in every shot.
```

## Optimized for local inference in ComfyUI

Getting H3 to run well on consumer hardware took significant machine learning engineering. We found that the model's modulation weights (~40% of the total parameters) could be pruned and replaced with a functionally equivalent lookup table, dramatically shrinking the memory footprint with no loss in output quality.

On top of that, the weights ship with an accurate and efficient int8 convrot quantization, and custom kernels reduce the peak VRAM use during inference.

[![](https://substackcdn.com/image/fetch/$s_!59Bc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d2552b-d84c-4385-9602-bf344dca2ebe_1000x727.png)](https://substackcdn.com/image/fetch/$s_!59Bc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d2552b-d84c-4385-9602-bf344dca2ebe_1000x727.png)

The result gives a total memory footprint **reduced by 66%, from 123.6 GB in full precision to 42.5 GB** with the smallest models variants. Combining this with our dynamic VRAM offloading enables a next-generation 2K video model to run locally on a GPU like the RTX 3060.

## Getting started

1. Update ComfyUI to the latest version **0.30.0 or go to [Comfy Cloud](https://links.comfy.org/4pTj4QV)**

2. Download the workflows below, or find them in the template library.

[Download MiniMax H3 I2V Workflow](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_i2v.json)

[Download MiniMax H3 R2V Workflow](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_r2v.json)

[Download MiniMax H3 T2V Workflow](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_t2v.json)

3. Follow the note in the workflow to download the models and save them in the correct model directory.

4. Write your prompt, connect any frame or reference inputs, and run.


Model weights: 🤗 [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

As always, enjoy creating!

[![rogue's avatar](https://substackcdn.com/image/fetch/$s_!Tfxb!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Forange.png)](https://substack.com/profile/9885092-rogue)[![Çağlar Doğan's avatar](https://substackcdn.com/image/fetch/$s_!ByG1!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0988d9b-f37c-4314-9ad0-dad4618c6150_3084x3084.jpeg)](https://substack.com/profile/446285018-caglar-dogan)[![Amir's avatar](https://substackcdn.com/image/fetch/$s_!CW5O!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c83cb9-57f4-4b43-a992-7fe5583e5693_144x144.png)](https://substack.com/profile/352132075-amir)[![元始祭龙's avatar](https://substackcdn.com/image/fetch/$s_!rOj6!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58c636e3-51fb-4ed2-a038-9af2f51fc006_2048x2048.jpeg)](https://substack.com/profile/454830152-514359cb796d)[![Daxiong (Lin)'s avatar](https://substackcdn.com/image/fetch/$s_!7zTL!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08d1a924-8801-4c3b-8e0a-e42ce365f1c0_1077x1077.jpeg)](https://substack.com/profile/327492471-daxiong-lin)

10 Likes

10

2

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![duo.duo's avatar](https://substackcdn.com/image/fetch/$s_!Tfxb!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Forange.png)](https://substack.com/profile/534851992-duoduo?utm_source=comment)

[duo.duo](https://substack.com/profile/534851992-duoduo?utm_source=substack-feed-item)

[Aug 3](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui/comment/307088847 "Aug 3, 2026, 2:38 AM")

Why does the R2V workflow only allow two image references? Isn't the maximum number 9?

Like

Reply

Share

[1 reply](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui/comment/307088847)

[1 more comment...](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui/comments)

TopLatestDiscussions

[Wan2.1 Video Model Native Support in ComfyUI!](https://blog.comfy.org/p/wan21-video-model-native-support)

[14B and 1.3B video generation workflows available now! Accessible for consumer GPUs!](https://blog.comfy.org/p/wan21-video-model-native-support)

Feb 26, 2025•[Jo Zhang](https://substack.com/@jozhang)

57

39

9

![](https://substackcdn.com/image/fetch/$s_!VXzX!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F990be2ac-d52c-408e-b48c-a3acb96d9b65_768x768.webp)

[WAN2.2 Animate & Qwen-Image-Edit 2509 Native Support in ComfyUI](https://blog.comfy.org/p/wan22-animate-and-qwen-image-edit-2509)

[New level of pose reference and image editing](https://blog.comfy.org/p/wan22-animate-and-qwen-image-edit-2509)

Sep 23, 2025•[Daxiong (Lin)](https://substack.com/@comfyuiwiki)

45

28

2

![](https://substackcdn.com/image/fetch/$s_!BYLs!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9ce071b-ba7f-43b8-a8ae-e5baede2b882_3123x2216.png)

[Introducting ComfyUI Native Partner Nodes (and New Brand!)](https://blog.comfy.org/p/comfyui-native-api-nodes)

[One platform, 11 models, 65 nodes, all at once!](https://blog.comfy.org/p/comfyui-native-api-nodes)

May 6, 2025•[Robin](https://substack.com/@robinjhuang)

56

26

5

![](https://substackcdn.com/image/fetch/$s_!Usn5!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e29daa9-2ee7-483f-873a-8cbd5a33489f_2059x1159.png)

See all

### Ready for more?

Subscribe
