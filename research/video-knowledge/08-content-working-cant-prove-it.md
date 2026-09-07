# 08 · your content is working, you just can't prove it

**Alt title:** impressions don't predict calls. i measured it.
**What this file is:** the information behind the video. Not a script.
**Written:** 2026-09-07

**Sources**
- `~/growthub-os/skills/content/x-articles/_corpus.md` (the impressions-versus-calls section)
- `~/growthub-os/ops/tools/impressions-vs-calls.py` (the script behind the correlations)
- `~/growthub-os/skills/ops/monday-acquisition-analysis.md` (the weekly run, ten sections)
- `~/growthub-os/ops/CONVENTIONS.md` (rule 3 and rule 4)
- `research/x-analytics/maurojpelle-2026-05-25-to-2026-08-22.csv`

**ICP cut:** the owner who posts, sees impressions move, and cannot tell his partner whether any of
it produced revenue.
**Reach cut:** this contradicts the single most repeated assumption in content marketing, with a
correlation coefficient and a named script behind it. It is the strongest authority piece in the set.

---

## The one claim

Impressions and booked calls are independent on our own data. Both are worth optimising, and a rule
that lifts one says nothing about the other.

---

## The information

### 1. The measurement

Twelve articles from one account, the only set carrying both numbers. Same account, so audience size
is constant and the impression spread is post-level rather than follower-level. That makes it the
cleanest test available on our own data. `[measured: impressions-vs-calls.py]`

| pair | Spearman rho |
|---|---|
| impressions vs calls booked | **+0.16** |
| impressions vs lift over baseline | **+0.05** |
| calls vs lift over baseline | +0.89 |

Effectively zero on the first two.

### 2. The two numbers that make it concrete

**The bottom four articles by reach pulled 9.0% of the audience and booked 78% of the calls.**

The account's **47,000-impression article booked 2 calls against a 4.2 baseline.** Its
**5,500-impression article booked 8 against a 3.8 baseline.** The small one outbooked the big one
four to one while reaching a twelfth of the people.

### 3. What separates a converter from a reach piece

Twelve articles with three-day booking lift, `[observed, n=12]`, the sharpest hypothesis available
rather than a measurement:

| shape | how it did |
|---|---|
| a process we run | 2.27x, 2.20x, 2.12x, 1.30x, 1.03x, 0.88x |
| a mechanism we exploit | 1.74x |
| an opinion | 1.30x |
| a competitor teardown | 1.06x |
| a stunt | 1.03x |
| a tool tutorial | **0.48x** |
| someone else's case study | **0.30x** |

**Every converter documents something we operate. Both failures teach a tool or narrate someone
else's win.** That is the sentence the whole video is built to earn.

Length behaves differently in the convert lane too: all twelve run 738 to 1,012 words, which is the
corpus's second-weakest band on reach.

### 4. Why nobody can prove any of this by default

**The UTM Source field is filled on 4 of 541 bookings.** A unique DM word per piece is the only
attributable path from content to a booked call. `[measured: _corpus.md]`

And attribution by account is not available at all: 649 of 678 Calendly rows sit under a single
owner and the UTM field is empty on 673 of them, which is why the tool that looks like it measures
one account's bookings says in capitals in its own docstring that it does not.
`[measured: named in CONVENTIONS.md rule 3]`

Two different exports, two different windows. Both say the same thing: the default instrumentation
does not answer the question.

### 5. The weekly run that replaces guessing

The Monday analysis takes four inputs (call structure tracker, Calendly export, X analytics, weekly
targets), rebuilds a fixed ten-section structure, adds a diff against last week on every metric, and
carries the action items and open questions forward so nothing falls off silently.

Two standing interpretation rules worth stealing on camera:

- **Conducted, not booked.** The tracker is by conducted date and is the source of truth for call
  volume. Calendly dates lead or lag, because someone sees a post one week and books a slot that
  lands in another. A call conducted this week can trace to content from one or two weeks earlier.
- **Impressions per post is the signal, not impressions.** Overposting collapses the ratio while the
  headline number keeps climbing.

### 6. What to do with it

Declare the intent of a piece before writing it. A reach article that books nothing is not a
failure, and a convert article at 5,000 impressions is not a failure. Judge each on its own metric.
`[observed: set by Mauro 2026-09-01, recorded in _corpus.md]`

---

## Evidence

| Claim | Status |
|---|---|
| Spearman +0.16, +0.05, +0.89 | `[measured: impressions-vs-calls.py, n=12, one account]` |
| Bottom four by reach: 9.0% of audience, 78% of calls | `[measured: same run]` |
| 47,000 impressions booked 2 vs 4.2 baseline | `[measured: same run]` |
| Converters document something we operate | `[observed, n=12, hypothesis not measurement]` |
| UTM filled on 4 of 541 bookings | `[measured: _corpus.md]` |
| 649 of 678 rows under one owner, UTM empty on 673 | `[measured: CONVENTIONS.md rule 3]` |

---

## Beats on camera

1. The question nobody can answer: which post produced revenue.
2. The setup. Twelve articles, one account, both numbers present.
3. The three correlations on screen.
4. The two articles side by side. 47,000 against 5,500.
5. What the converters have in common, and what both failures were.
6. The length finding that contradicts the reach rule.
7. 4 of 541. Why the keyword is the only instrument.
8. Conducted versus booked, and the one-to-two week lag.
9. Impressions per post as the real signal.
10. Declare the intent before you write.
11. CTA.

---

## Do not say

- That reach does not matter. The finding is independence, and both get optimised.
- These numbers as a general law. n=12, one account, and the file says so.
- The account name.

## Gaps

- `[NEEDS: re-run impressions-vs-calls.py if captures have been added since 2026-09-01]`
- `[NEEDS: the same test on @maurojpelle's own data once the keyword instrumentation has run long enough]`
