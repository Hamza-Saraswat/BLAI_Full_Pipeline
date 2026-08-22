# Thumbnails

Source of truth for the channel rules: `shared/playbook/thumbnails.md`. This file says how the `Thumbnail` composition turns one concept into one still.

## Input

`spec.thumbnail_concepts` holds exactly three `{words, focus}`: `words` is the line a viewer reads (at most 4 words; extra words are dropped), `focus` is the one object or number that gets the accent treatment (`41.7`, `128 GB`, `$0`). The three concepts should differ in idea, not only in wording: a number, an object, a contrast.

## Variants

`render_longform.py` renders concept N as variant N (`--props {concept, title, variant: N, series}`), 1280 x 720:

| Variant | Layout | Best for |
|---------|--------|----------|
| 1 | words on the left in two lines, the last line in amber; the focus in an amber disc on the right | a number or a short token as the focus |
| 2 | the focus huge and centered in amber, the words under it in warm white; the series tag on top | the number is the thumbnail |
| 3 | amber block on the left carrying the focus in the dark ink, the words stacked on the right | a contrast or a versus |

Every variant: background `#0B1020`, text `#F5F0E8`, accent `#FFB347`, Inter 800, one focal object, the wordmark small in a corner. Text is sized to fit its box (`fitSize` in `Thumbnail.tsx`), never below 40 px, so four long words shrink rather than overflow.

## Rules

- At most 4 words, at most 3 focus areas (words, focus, wordmark). Do not repeat the title; the title carries the words, the thumbnail carries the image or the number.
- Readable at 160 px wide: the smallest text on a variant is the wordmark, which is decoration; the words and the focus stay above 100 px at 1280 wide.
- No gradients, no photos in v1; the real mascot or a product photo can replace the disc in variant 1 later (`Thumbnail.tsx`, variant 1 block).
- Export: PNG from `npx remotion still`; when a PNG is over 2 MB the script writes a JPG next to it with `ffmpeg -q:v 3` (quality about 90) and reports both in `render.json`. Flat designs stay well under 200 KB.
- The publish stage uploads one file. Pick the variant by running Test & Compare in Studio (watch-time share, about two weeks, desktop only); until a winner exists, variant 1 is the default.

## Checking a thumbnail fast

```
cd skills/render-longform/remotion
npx remotion still src/index.ts Thumbnail /tmp/t1.png --props='{"concept":{"words":"41 tokens a second","focus":"41.7"},"title":"x","variant":1,"series":"benchmarks"}'
```

Look at it at 160 px wide (`ffmpeg -i /tmp/t1.png -vf scale=160:-1 /tmp/t1-small.png`). If the words are not legible there, shorten them.
