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

### 2. ⚠️ A correction to make before this is said on camera

The corpus file says *"the bottom four articles by reach pulled 9.0% of the audience and booked 78%
of the calls."* Re-running the script on 2026-09-07 shows both figures are ratios **against the top
four**, not against the whole set:

- top four by impressions: **36 calls, 210,000 impressions**
- bottom four by impressions: **28 calls, 18,800 impressions**

28 of 36 is the 78%. 18,800 of 210,000 is the 9.0%. So the accurate sentence is: **the bottom four
booked 78% as many calls as the top four, on 9% of the reach.** Said the other way it is a false
claim, because the bottom four booked 30% of the 93 calls in the set, not 78%.
`[measured: impressions-vs-calls.py re-run 2026-09-07]`

### 3. The full table, and the nuance that keeps it honest

| impressions | rank | calls | rank | lift | article |
|---|---|---|---|---|---|
| 90,000 | 1 | 17 | 1 | 2.21 | a process we run |
| 48,000 | 2 | 6 | 9 | 0.88 | a process we run |
| 47,000 | 3 | 2 | 11 | 0.48 | a tool tutorial |
| 25,000 | 4 | 11 | 3 | 2.29 | a process we run |
| 15,000 | 5 | 7 | 7.5 | 1.03 | a process we run |
| 12,000 | 6 | 9 | 4.5 | 1.30 | a process we run |
| 7,700 | 7 | 12 | 2 | 1.74 | a mechanism we exploit |
| 6,000 | 8 | 1 | 12 | 0.29 | someone else's case study |
| 5,500 | 9 | 8 | 6 | 2.11 | a process we run |
| 5,000 | 10.5 | 7 | 7.5 | 1.03 | a stunt |
| 5,000 | 10.5 | 4 | 10 | 1.05 | a competitor teardown |
| 3,300 | 12 | 9 | 4.5 | 1.30 | an opinion |

**The nuance:** the biggest article by reach is also the biggest by calls. It ranks first on both.
The independence is real across the whole set and the top row is not a counterexample to it, but
anyone in the comments will find that row, so say it before they do.

The pair that carries the video is rows three and nine. **A 47,000-impression article booked 2 calls
against a 4.2 baseline. A 5,500-impression article booked 8 against 3.8.** The small one outbooked
the big one four to one on a twelfth of the reach.

### 4. What separates a converter from a reach piece

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

### 5. Why nobody can prove any of this by default

**The UTM Source field is filled on 4 of 541 bookings.** A unique DM word per piece is the only
attributable path from content to a booked call. `[measured: _corpus.md]`

And attribution by account is not available at all: 649 of 678 Calendly rows sit under a single
owner and the UTM field is empty on 673 of them, which is why the tool that looks like it measures
one account's bookings says in capitals in its own docstring that it does not.
`[measured: named in CONVENTIONS.md rule 3]`

Two different exports, two different windows. Both say the same thing: the default instrumentation
does not answer the question.

**And the keyword is not what is actually running.** `post-to-call.py` records the accepted standard
of proof as **same-day correlation**: a booking created on day D is credited to the posts that ran
on D and D-1, *"because there is no per-post tracking link and the UTM route was rejected as too
ugly for the bio."* The script says in its own docstring that this is correlation and not
attribution, and that one post plus one booking on one day is noise.

Run across a quarter, what it produces is a topic mix under above-floor booking days against the
baseline mix across all days:

| topic | under booking days | baseline | difference |
|---|---|---|---|
| AI / Claude | 17% | 16% | +1 |
| Formats and mechanics | 12% | 9% | +3 |
| Brand teardown | 11% | 10% | +1 |
| Spend and proof | 9% | 9% | 0 |

`[measured: post-to-call.py, run 2026-09-07]`

**That is close to no signal, and it is the honest headline of the whole video.** The one topic that
moves is formats and mechanics, by three points. Anyone selling you a content-to-revenue dashboard
is selling you a version of this table with the differences exaggerated.

### 6. The weekly run that replaces guessing

The Monday analysis takes four inputs (call structure tracker, Calendly export, X analytics, weekly
targets), rebuilds a fixed ten-section structure, adds a diff against last week on every metric, and
carries the action items and open questions forward so nothing falls off silently.

Two standing interpretation rules worth stealing on camera:

- **Conducted, not booked.** The tracker is by conducted date and is the source of truth for call
  volume. Calendly dates lead or lag, because someone sees a post one week and books a slot that
  lands in another. A call conducted this week can trace to content from one or two weeks earlier.
- **Impressions per post is the signal, not impressions.** Overposting collapses the ratio while the
  headline number keeps climbing.

### 7. What to do with it

Declare the intent of a piece before writing it. A reach article that books nothing is not a
failure, and a convert article at 5,000 impressions is not a failure. Judge each on its own metric.
`[observed: set by Mauro 2026-09-01, recorded in _corpus.md]`

---

## Evidence

| Claim | Status |
|---|---|
| Spearman +0.16, +0.05, +0.89 | `[measured: impressions-vs-calls.py, re-run 2026-09-07, unchanged]` |
| Bottom four booked 78% as many calls as the top four, on 9% of the reach | `[measured: same run. The corpus file's phrasing of this is ambiguous, see section 2]` |
| Topic mix under booking days is within 3 points of baseline | `[measured: post-to-call.py, 2026-09-07]` |
| The accepted standard of proof is D and D-1 correlation | `[observed: post-to-call.py docstring]` |
| 47,000 impressions booked 2 vs 4.2 baseline | `[measured: same run]` |
| Converters document something we operate | `[observed, n=12, hypothesis not measurement]` |
| UTM filled on 4 of 541 bookings | `[measured: _corpus.md]` |
| 649 of 678 rows under one owner, UTM empty on 673 | `[measured: CONVENTIONS.md rule 3]` |

---

## Beats on camera

1. The question nobody can answer: which post produced revenue.
2. The setup. Twelve articles, one account, both numbers present.
3. The three correlations on screen.
4. The full twelve-row table, including the row that ranks first on both.
5. The two articles side by side. 47,000 against 5,500.
6. The topic mix under booking days against baseline. Three points is the whole signal.
7. What the converters have in common, and what both failures were.
8. The length finding that contradicts the reach rule.
9. 4 of 541, and why the UTM route was rejected anyway.
10. Conducted versus booked, and the one-to-two week lag.
11. Impressions per post as the real signal.
12. Declare the intent before you write.
13. CTA.

---

## Do not say

- That reach does not matter. The finding is independence, and both get optimised.
- These numbers as a general law. n=12, one account, and the file says so.
- The account name.

## Gaps

- ~~re-run impressions-vs-calls.py~~ **Closed 2026-09-07.** Re-run, all three correlations
  unchanged, and it surfaced the phrasing error in section 2.
- `[NEEDS: the same test on @maurojpelle's own data once there is enough of it]`
- `[NEEDS: Mauro's call on whether to correct the 78% line in growthub-os _corpus.md and in the
  script's own print statement, since both carry the ambiguous wording]`
