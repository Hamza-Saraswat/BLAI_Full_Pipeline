# Drafts: 2026-11-21-verify-your-deepseek-v4-1-flas

Two blind drafts on kimi-k3, judged blind on kimi-k3 per judge-rubric.md.

## Score table

| row | name | A | B |
|---|---|---|---|
| 1 | hook | 3 | 2 |
| 2 | payoff timing | 3 | 2 |
| 3 | specificity without cramming | 3 | 3 |
| 4 | voice | 3 | 3 |
| 5 | navigation | 2 | 3 |
| 6 | difference | 3 | 1 |
| 7 | repeat test | 2 | 3 |
| 8 | teaching | 3 | 3 |

Total: A=22 B=20. Winner: draft A.

## Grafts
none  --  B's hook (row 1: 2 vs 3) does not clear the 2+ bar, and its strongest sentences fail the graft rules: "It was abliterated, edited to stop refusing; capability scores never moved" collides with A's existing "Capability scores never moved," the tamper-seal line would add a second analogy vehicle to a one-analogy script, and the "skips hashing by default" clause is fused to B's own 233 GB sentence, so moving any of them would require rewriting A's surrounding beats.

## Loser needs
The myth-bust spent its best number on a hook whose tension does not resolve until "became one" (word six, past the five-word bar), and the obligatory belief-statement beat pushes the break past second eight even with the fairness adjustment, so it needed a hook that detonates inside five words and a leaner myth beat. It also re-ran the 11-16 myth-bust shape and the 11-17 number-shock hook within the same week, so against a fresh structure it needed a visibly different opening rhythm or landing, not just a strong middle.

## Repeat line (winner)
No hash, no load.

### Draft A -- news-react-so-what (hook pattern wrong-diagnosis)

Narration:
  s01 (hook, centered-stack, 5.9s): Prime Intellect served the wrong weights for over two days. Same endpoint, different DeepSeek weights answering you.
  s02 (explain, split-compare, 7.2s): Capability scores never moved. On JailbreakBench, a refusal test, ninety-eight of one hundred refusals became one. Scores grade answers, not origins.
  s03 (explain, giant-number, 10.7s): Unsloth's smallest one-bit pack is a GGUF your runner loads: two hundred thirty-three gigabytes of weights, never hashed. Same restaurant sign, different kitchen; diners can peek, clients cannot, so check files.
  s04 (explain, timeline, 6.9s): Tonight, pin the revision, the full commit hash. Fetch the manifest, the list of expected fingerprints. No hash, no load.
  s05 (payoff_close, centered-stack, 6.6s): A match proves Hugging Face's bits arrived, never that they deserved trust. Verify every pull before you load it.

On-screen:
  s01: deepseek/deepseek-v4.1-flash | same endpoint | different weights
  s02: GPQA Diamond: unchanged | tau-bench: unchanged | JailbreakBench refusals: 98/100 -> 1
  s03: smallest 1-bit GGUF: 233 GB | sha256: skipped by default
  s04: hf download --revision <full hash> | fetch SHA256SUMS manifest | sha256sum -c SHA256SUMS | hf cache verify
  s05: match = the repo's bits | not proof of trust | verify every pull

### Draft B -- myth-bust (hook pattern number-shock)

Narration:
  s01 (hook, centered-stack, 4.8s): Ninety-eight refusals out of a hundred became one. The name you called never changed.
  s02 (explain, split-compare, 3.8s): The belief sounds reasonable: ace the benchmarks, the weights are genuine.
  s03 (explain, timeline, 10.0s): Prime Intellect's hosted DeepSeek kept its name. Behind it, different weights answered for over two days in November. It was abliterated, edited to stop refusing; capability scores never moved.
  s04 (explain, diagram-flow, 8.3s): On disk, the only evidence is a fingerprint of the exact bits. Think tamper seals on medicine bottles: they prove pills untouched, never good.
  s05 (explain, centered-stack, 9.7s): Pin the full revision hash, pull the manifest of expected fingerprints, verify before loading. Two hundred thirty-three gigabytes of shards, and your download tool skips hashing by default.
  s06 (payoff_close, split-compare, 6.9s): A match proves you got the repo's bits, not that it deserved trust. Hash every pull before you load it.

On-screen:
  s01: DeepSeek v4.1-flash | JailbreakBench refusals | 98 of 100 -> 1
  s02: the belief | GPQA Diamond: aced it | so weights are genuine?
  s03: same name, different weights | over 2 days | GPQA Diamond: unchanged | t-bench: unchanged
  s04: SHA-256 | fingerprint of the exact bits | seal proves untouched, never good
  s05: hf download --revision <full hash> | SHA256SUMS manifest | hf cache verify | Hugging Face downloads skip hashing
  s06: match = transport integrity | match != repo trust | hash every pull

