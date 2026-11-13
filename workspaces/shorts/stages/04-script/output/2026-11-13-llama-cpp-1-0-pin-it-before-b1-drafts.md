# Drafts: 2026-11-13-llama-cpp-1-0-pin-it-before-b1

Both drafts written blind (separate writer processes, separate scratch dirs, different assigned structures and hook patterns). Both cleared the machine gates before judging: validator 0 blockers, eval hard gates pass, sameness clean vs last 5. Judge: third blind process, rubric + voice rules only.

## Draft A (news-react-so-what, hook: wrong-diagnosis)

| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | You're not on llama.cpp one point oh. You're on a nightly build, a daily cut of the development trunk. | You're not on llama.cpp 1.0 | 7.0 |
| s02 | explain | This morning llama.cpp shipped its first stable tag, a snapshot frozen at one commit. One commit past it, the next nightly had a crash report. | stable tag, +1 commit, crash report | 9.0 |
| s03 | explain | Homebrew tracked thirty days of build errors. The newest-code track logged three hundred forty-seven build errors. The stable formula logged sixty-eight build errors. | --HEAD: 347 errors | 8.3 |
| s04 | foreshadow | The tag has teeth. It removed thirty-five deprecated functions, old calls marked for deletion. Code built on them stops compiling. | 35 deprecated functions removed | 7.3 |
| s05 | payoff_close | Tonight, check your build. A b number means you didn't choose it, so pin the tag and choose every move after that. | $ pin v1.0.0 | 7.3 |

## Draft B (number-first, hook: number-shock)

| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | Three hundred forty-seven build errors this month. The stable formula had sixty-eight. | 347 errors. Stable: 68. | 4.5 |
| s02 | explain | You run llama dot cpp, the engine that runs models on your machine. Both counts are Homebrew's, the Mac package manager. Its newest-code track pours nightly builds, a daily cut of the trunk. | HEAD: newest code | 11.8 |
| s03 | explain | This morning brought the first stable tag, a named snapshot: version one point oh. Thirty-one minutes later, a crash report hit the next nightly, an automatic build one commit past it. | v1.0.0 tag, 31 min, crash | 11.1 |
| s04 | foreshadow | The tag also removes thirty-five deprecated functions, old calls your code may still use. | 35 deprecated calls removed | 5.2 |
| s05 | payoff_close | Check which build you're running. If it's a b-number nightly, pin the tag and move when you choose. | > pin the tag | 6.6 |

## Score table (judge, 0-3 per row)

| Row | A | B |
|-----|---|---|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 2 | 2 |
| 3 Specificity | 3 | 2 |
| 4 Voice | 3 | 2 |
| 5 Navigation | 3 | 2 |
| 6 Difference | 1 | 2 |
| 7 Repeat test | 2 | 3 |
| 8 Teaching | 3 | 2 |
| **Total** | **20** | **17** |

## Winner

A, 20-17, no grafts. Judge: "A opens with a product plus a tension the viewer feels in five words, spends exactly one number per sentence, and every transition carries content ('The tag has teeth' pivots from evidence to cost with nothing explained). B's contrast lands too late to name what the numbers count, crams two numbers into the timeline sentence, resets for definitions in scene two, and its opening rhythm repeats the number-shock script from three entries back; its repeatable closing line wins row 7 but cannot close a three-point gap."

## Grafts

None.

## What the losing shape would have needed

Number-first needed the product named within the first two beats so the 347-vs-68 contrast attached to something the viewer runs, and one number per sentence through the timeline instead of "thirty-one minutes later... one commit past it." It also needed the removed-functions consequence shown rather than implied ("stops compiling", not "your code may still use") plus one wry beat to reach A's voice score.
