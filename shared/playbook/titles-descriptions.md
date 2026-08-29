# Titles and Descriptions

Source: YouTube's own title and description guidance plus the 2026 research in `research/youtube-automation-research.md` section 2.5. The packaging stages follow these rules and score the result with `seo-rubric.md`.

## Titles

- Hard limit 100 characters; about 50-60 show in search and feeds, about 40 in the mobile Shorts feed. Target: 40 visible characters.
- Primary keyword inside the first 40 characters. Important words first, branding last.
- **Name the specific product or model** ("DGX Spark", "DeepSeek V4 Flash", "Unsloth"). Channel search traffic is almost entirely product-name queries, and search viewers watch about twice as long.
- Accurate over clever: a title that over-promises produces high click-through and low watch time, which YouTube treats as clickbait and stops recommending.
- At most one ALL-CAPS word, at most one emoji, no `<` or `>`.
- Two title types. **Searchable** states the topic ("How to run DeepSeek V4 Flash on a DGX Spark"). **Intriguing** opens a gap ("Can DeepSeek V4 Flash run on 128 GB?"). Write one searchable and two intriguing variants; pick by target surface (search-heavy topics get the searchable one).
- Never restate the hook text verbatim; title and thumbnail complement, they do not repeat.
- Question phrasing is fine when natural (long-tail search).

## Descriptions

- Limit 5,000 bytes (UTF-8; multibyte characters count more than once).
- The first ~150 characters show above "Show more": keyword plus a one-sentence promise.
- Then 2-4 natural sentences with 1-2 keywords, unique to this video (never a pasted channel blurb first).
- First line names the channel's closest related video (or the channel itself), then 2-3 hashtags at the end. No chapter block.
- Put the search terms viewers actually use (weekly `YT_SEARCH` pull, once available) into the text.
- State the CTA here, never in the narration.

## Metadata the API cannot set (reviewer does it in Studio after publish)

Pinned comment, end screens and cards, the Shorts "related video" link, community posts. The publish stage sends these as a Telegram checklist.
