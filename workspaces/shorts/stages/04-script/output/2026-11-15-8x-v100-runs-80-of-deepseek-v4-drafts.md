# 2026-11-15-8x-v100-runs-80-of-deepseek-v4 -- drafts and verdict

Two blind writers on kimi-k3, separate processes, private scratch dirs. Neither saw the other.
### Draft A -- myth-bust (hook pattern: case)

Hook text (frame 1): 8x V100 · 2018 · DeepSeek v4.1

| Scene | Role | Narration | On-screen |
|---|---|---|---|
| s1 | hook | A lawyer's basement server runs eighty percent of DeepSeek on twenty eighteen cards. | 8x V100 · 2018 · DeepSeek v4.1  /  80% AT HIGH PRECISION |
| s2 | explain | You've been told cards like that are dead. Everyone knows the story: data center cards that old can't run a modern model. This one handles his daily legal work, drafting and research, and the case files never leave his office. That was the whole point of the build. | THE STORY: too old  /  THIS SERVER: daily legal work  /  files stay in-office |
| s3 | explain | Add up the memory across every card and you get two hundred fifty-six gigabytes of memory. The boards came used, at gaming-card prices. No new hardware anywhere in the rack. | 256 GB VRAM TOTAL  /  USED, GAMING-CARD PRICES |
| s4 | explain | DeepSeek is a mixture-of-experts model, where a router wakes only a few specialists per word. So every expert stays resident on the cards at two bits. The busiest ones get promoted to N V F P four, a higher-quality four-bit format. Most of the work now lands on the promoted experts. | ROUTER PICKS A FEW EXPERTS  /  15,360 EXPERTS AT 2-BIT  /  5,949 AT NVFP4 |
| s5 | explain | Picture a workshop. Every tool hangs on the wall at two bits. The handful you reach for all day get the full-quality version on the bench. Which tools count as most-used was tallied from his own mix of documents. | WALL: EVERY TOOL AT 2-BIT  /  BENCH: NVFP4  /  COUNTED FROM HIS OWN DOCUMENTS |
| s6 | explain | Open a second request at the same time and the bench shrinks. A little more of the work falls back to two bits, because the cards are already full. For a one-lawyer office running one thing at a time, that trade is fine. | 1 REQUEST: FULL NVFP4 BENCH  /  2: SMALLER BENCH |
| s7 | explain | Here's where the myth still holds. The R-five-eighty driver, the software that keeps the cards alive, is the last release they get. A new card with F-P-four in the hardware wins on watts, and it won't heat the office. | R580: LAST DRIVER FOR VOLTA  /  NEW FP4 CARD WINS ON WATTS |
| s8 | payoff_close | So before you recycle the past, check the used listings. Your old data center cards are not scrap. The math that makes a huge model fit them is the story. | NOT SCRAP  /  THE MATH IS THE STORY |

### Draft B -- worked-example (hook pattern: situation)

Hook text (frame 1): 8x V100 meets DeepSeek v4.1 Flash

| Scene | Role | Narration | On-screen |
|---|---|---|---|
| s1 | hook | You buy eight used data center cards. Then DeepSeek V four point one Flash arrives, bigger than all eight. | 8 used cards, 2018  /  then the model arrives |
| s2 | foreshadow | Everyone told you cards this old are scrap. One lawyer's server disagrees. Picture a lawyer who can't send case files to the cloud. His answer: eight used Tesla V one hundred cards, two hundred fifty-six gigabytes of memory in one home server. | a lawyer's offline server  /  8 cards, 256 GB total |
| s3 | explain | The model he wants is huge. At official precision, by his estimate, it needs two hundred sixty-nine gigabytes of model. The cards hold less than that before anything else loads. | DeepSeek v4.1 Flash: 269 GB  /  the cards hold 256 GB |
| s4 | explain | The rescue is the model's own design. It's a mixture-of-experts model, where a router wakes only a few specialists per word instead of using every parameter. So most of those gigabytes sleep most of the time. | router picks a few experts  /  rest stay asleep |
| s5 | explain | He stores every expert at two bit, the cheapest storage that works. Then the busiest get promoted to N V F P four, a sharper four-bit format, until the cards are full. Think of a workshop: every tool hangs on the wall. The few you grab all day get the good steel. His own files picked the favorites. | every expert stays 2-bit  /  5,949 of 15,360 go NVFP4 |
| s6 | explain | The result: about eighty percent of its decoding, the word-by-word writing, lands on the sharpened experts. He checked it against Nvidia's own four-bit build of the same model. His box picks the same next word more often, and its answers change less. So much for scrap. | 80% of decode on NVFP4  /  same next token, more often |
| s7 | explain | The catches are honest ones. A second request at the same time shrinks the promoted set, so the solo numbers are the best case. And by his account, Nvidia's R five eighty driver branch is the last that ever supports these cards. | 2nd request: smaller promoted set  /  R580 = last Volta driver |
| s8 | payoff_close | Eight bargain-bin cards, a careful headcount, and the biggest model he owns runs at high precision all day. The model never had to fit. Only the parts in daily use had to fit well. | the model never had to fit  /  only the busy parts fit well |

## Score table

| # | Row | A | B |
|---|-----|---|---|
| 1 | Hook | 3 | 2 |
| 2 | Payoff timing | 3 | 1 |
| 3 | Specificity | 1 | 1 |
| 4 | Voice | 0 | 0 |
| 5 | Navigation | 3 | 3 |
| 6 | Difference | 1 | 3 |
| 7 | Repeat test | 2 | 3 |
| 8 | Teaching | 3 | 3 |
| | **Total** | **16** | **16** |

**Winner: B** -- Tied at 16, B wins the row-6 tie-break: its worked-example shape, second-person opening rhythm, and 'the model never had to fit' landing are all absent from the last five shipped, while A re-runs the Nov 12 myth-bust shape with a verdict-plus-check-imperative close that echoes two recent endings.

## Grafts

None.

## What the losing shape needed

A needed a shape the recent run had not already used, since its myth-bust repeats the Nov 12 structure and its 'check the used listings / not scrap' close echoes both the Nov 13 check-imperative and the Nov 12 myth-verdict, capping it at 1 on difference. It also needed to keep the power-and-heat comparison inside the brief and to frame R580 as the builder's unverified claim instead of asserting it as fact.

## Judge notes (row-4 / drift findings, fixed after the verdict)

- A row-4 break: 'a new card with FP4 in the hardware wins on watts, and it won't heat the office' asserts efficiency and thermal claims that appear nowhere in the brief.
- B row-4 break: the s2 sentence 'His answer: eight used Tesla V one hundred cards, two hundred fifty-six gigabytes of memory of memory in one home server' runs 21 words as written (the duplicated 'of memory' pushes it over the 20-word cap).
- Shared factual drift capping row 3 at 1 for both drafts: each asserts R580 is the last driver/release these cards get, while the brief states that any specific Volta end-of-support date appears on no fetched page (builder's unverified 'borrowed time' claim).
- B's spoken 269 GB is hedged with 'by his estimate' and sits under the brief's parameter-framing conflict note, so it was not scored as drift; A's hook speaks two new numbers in one breath (80% and 2018), noted but not double-penalized since row 4 was already 0.

Post-verdict fixes applied to the winner: de-duplicated "of memory of memory" in s2 (introduced by the orchestrator referent patch); hedged the R580 end-of-support line as the builder's account ("by his account") to match the brief's unverified list. Gates re-run after: validator 0 blockers, eval all gates pass, variety ok.
