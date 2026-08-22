# Dedupe

The radar must not resurface what the channel already made, is making, or saw yesterday.
`radar.py` runs three passes, in this order.

## 1. Cross-source merge (inside one run)

Two raw items are the same story when any of their URLs match after normalization, or when
their normalized titles are equal. The stronger-scored item survives; the other source's name
lands in `signals.also_seen_in`, the product lists are unioned, a survivor whose why-now was only
"Discussed" adopts the merged source's more specific why-now (a GitHub release merging into an HN
thread makes it "Shipped"), and the survivor gains 5 points
per extra source (a story on Reddit, HN and Hugging Face at once is a stronger signal than any
of the three alone). URLs compared per item: the outbound link, the Reddit permalink, the HN
thread, the GitHub release page.

## 2. Already made or in progress

Titles are collected from the `title` frontmatter of every hub note (first `# heading` when the
frontmatter has no title), read with `tools/hubnote.py`:

- `DIR/../../../videos/*.md` and `DIR/../../../published/*.md`, the workspace that owns the
  output folder when `DIR` is the default `workspaces/<ws>/stages/01-radar/output`
- `<dedupe-dir>/videos/*.md` and `<dedupe-dir>/published/*.md` when `--dedupe-dir` is given
  (pass the other workspace to keep Shorts and long-form from chasing the same story)
- in `--dry-run` without `--dedupe-dir`: `fixtures/dedupe-workspace/`

An item whose normalized title equals one of those titles is dropped. Hub-note titles are
video titles, so this pass mostly catches the ideas stage copying a headline verbatim; the
ideas stage still reads `published/` for topical overlap (root `CLAUDE.md`, rule 5).

## 3. Seen in the previous seven radars

The seven most recent `*-radar.json` files in `DIR` whose date is before `--date` contribute
every item's normalized title and URL. A same-day file is ignored so a re-run of today does not
dedupe against itself. Anything still hot after a week returns once the old radar scrolls out;
that is intended: a week-old story is the ideas stage's call, not the radar's.

## Normalization

- Title: lowercase, then strip everything except `a-z` and `0-9`
  ("Ollama 0.13 -- NVFP4!" and "ollama 0.13 nvfp4" are equal).
- URL: lowercase, drop the scheme and a leading `www.`, `m.`, `old.` or `mobile.`, drop the
  fragment, drop `utm_*`, `ref`, `fbclid`, `si` and `feature` query parameters, map `youtu.be/ID`
  to `youtube.com/watch?v=ID`, strip the trailing slash.

## What the run reports

stderr: `dedupe keys: <folder>: N title(s); ...; previous radars: N`. The digest's third line
counts candidates, merged duplicates, drops by title, drops by URL, kept and listed. The JSON
summary on stdout carries the same counts under `merged` and `dropped`.

## Known limits

- A rephrased headline passes (this is exact-title matching on purpose; fuzzy matching would
  drop distinct stories about the same product). The ideas stage handles topical overlap.
- Dedupe reads titles only; it never opens a hub note's body or a published video's script.
- Nothing is ever deleted: dropped items simply do not appear in the radar files.
