# Ghosted Calls: X and LinkedIn best practices, from October 2026

**Status: draft for Mauro's review, written 2026-10-01.** Rules below come from four sources and
each rule names its source. Nothing here is a number we invented.

| Tag | Source |
|---|---|
| `[algo]` | X source code, `~/growthub-os/research/x-algorithm/README.md` (updated 2026-09-30) |
| `[ours]` | Mauro's own X data, `brand/analytics/2026-09-content-review.md` |
| `[paolo]` | Paolo consult, `research/paolo-trivellato/linkedin-playbook-2026-09-24.md` |
| `[wiz]` | Wiz consult, `research/wiz-of-ecom/synthesis.md` (not adopted row by row yet) |
| `[shann]` | @shannholmberg study, `research/profile-studies/vehicles-from-shannholmberg.md` |

**The lane does not change.** AI content systems that book calls, for established agency owners.
Never ecom ad creative. Every post comes from a system Mauro really runs.

**The time budget does not change.** 5 to 7 hours a week (`brand/operating-baseline.md`).

---

## The starting line

| | September 2026 |
|---|---|
| X impressions | 63,443 (Sep 1–28) |
| X new follows | 285 |
| X profile visits | 366 |
| X originals a week | fell from 29 to 17 |
| LinkedIn | `[NEEDS: does Mauro post on LinkedIn as Ghosted Calls yet, and the follower count]` |
| Email list | none |
| Capture funnel | none |

---

## The order of work

1. **Capture before more content.** `[paolo]` `[wiz]` Both advisors said the same thing without
   prompting: the leak is between the post and the booked call. Build once: an opt-in page, a
   thank-you page with a short VSL and a book-a-call link, and 3 emails in 3 days.
2. **Then volume on X.** `[ours]` Mean impressions per original held at about 270 all September
   while the count fell. Volume is the lever under direct control.
3. **Then LinkedIn lead magnets**, once the capture funnel exists. `[paolo]`

**The asset comes first.** A post with a keyword CTA ships only when the resource is built
(`CLAUDE.md` §7). The Sep 5 post (2,315 impressions, 16 bookmarks) still has nothing to send.

---

## X

**What the ranker rewards, as of 30 Sep** `[algo]`

- **Time spent after the tap.** New on 29 Sep: `cont_click_dwell_time` went from 0 to 0.4 and the
  tap itself dropped to 0.3. A hook that gets the tap and a body that loses the reader now scores
  lower. Write the body to be read to the end.
- **The first 2 hours.** On 30 Sep xAI switched on test slots for fresh posts: accounts under 50K
  followers, posts under 200 impressions, under 2 hours old. Mauro's account qualifies. Post when
  the audience is online, and answer every reply in that window.
- **Replies and quotes** (5.0), **mutual replies** (+15.0 boost), **copy-link shares** (20.0).
  These are what the ranker tries hardest to predict.
- **Links are not penalised by the scorer.** Open link is +0.2.
- **"Not interested" is now -47.52.** Ragebait and off-lane posts cost more than before.
- **Insult-labelled posts are now dropped for every viewer who does not follow you.**

**What our own data says** `[ours]`

- **Restore volume to about 29 originals a week.**
- **Bare-link article drops:** median 532 impressions against 156 for everything else. Post more
  of them. Judge them on bookmarks and reach, never on profile visits.
- **Pair every article drop with a standalone single-idea post.** Those earned the most profile
  visits per impression.
- **Capture and X-mechanics topics** had the two highest profile-visit rates on the account.
- **Replies go to large in-niche accounts.** @wizofecom returned 214 impressions per reply. The
  median reply returns 14. Stop the high-count replies to accounts that return under 10.

**Formats to run** `[paolo]` `[shann]` `[wiz]`

| Format | Cadence | Why |
|---|---|---|
| Mid-to-long listicle ("the 9 parts of the system that books our calls") | 1 a day | Dwell time and bookmarks `[paolo]`, matches the 29 Sep dwell change `[algo]` |
| How-to post that opens with "how" | the daily default | 6.6x median over other openers in Shann's set `[shann]` |
| Article: a breakdown of a company the ICP admires | 1 a week | Paolo's Clay breakdown did 300K and closed 8-figure agencies `[paolo]` |
| Quote-tweet a viral AI-content or agent flex with the real workflow | when one appears | X shows the quote to everyone who engaged with the original `[wiz]` |
| Split CTA: the link goes in its own post right after the main one | any post with a link | The main post stays clean `[shann]` |
| ASCII diagram of a system we run (cream background PNG) | 1–2 a week | Visual for listicles and how-tos. Renderer: `content/ascii/render.py` |

**No autodms on X.** `[wiz]` X banned about 40,000 accounts for automation and Mauro's own autodms
stopped converting. Paolo also stopped them after a ban wave. Use the CTA "link in the next post"
or the article itself.

---

## LinkedIn

**LinkedIn is its own playbook.** Never cross-post X copy as it is.

| Rule | Source |
|---|---|
| **The CTA goes in the image or on a video banner, never in the copy.** A "comment WORD" line in the copy gets the post killed | `[paolo]` |
| **Lead-magnet image: a dense infographic**, templated from a winner (same structure, new topic and colours). The Notion-doc screenshot style is dead | `[paolo]` |
| **Lead-magnet copy: mid-length**, easy to read, looks like it covers a lot | `[paolo]` |
| **Lead Shark replies to the comment with the opt-in link.** Leave the DM message empty | `[paolo]` |
| **Every resource is delivered in Notion** | `[paolo]` |
| **Regular posts: about 5 a week, no infographics.** The one image that works is a screenshot of an X conversation Mauro was in, plus commentary | `[wiz]` |
| **70/30.** 70% broad for reach, 30% specific to agency owners with a direct book-a-call CTA | `[paolo]` |
| **Case-study lead magnets convert best**, positioned as a breakdown of how the result happened | `[paolo]` |

**Where Wiz and Paolo disagree on images:** Paolo for lead-magnet posts, Wiz for regular posts.

**The ideas are 90% of the work.** `[paolo]` Copy what wins on X first: X runs days to weeks ahead
of LinkedIn on anything AI.

**Warm outbound, weekly.** `[paolo]` Export from the Lead Shark **post** section, never the leads
section. Claude scores ICP fit. Filter for 3+ posts engaged. DM the top 5, reference the latest
post they engaged on, add one case study, end with "open to seeing how I'd approach it?".

---

## Both platforms

- **The swipe file scores each post against its own account's average**, never raw numbers.
  Worth copying: X 50K+ impressions, LinkedIn 300–400+ comments. `[paolo]`
- **Cycle 5 to 10 keywords on X each week** to find new accounts. `[paolo]`
- **Templates live in Notion or Miro, never inside the Claude skills.** `[paolo]`
- **One source, many posts.** Every system Mauro builds becomes an X listicle, an ASCII diagram,
  a LinkedIn lead magnet and, monthly, a YouTube video.

---

## What we measure, every Monday

| Metric | Why |
|---|---|
| **Profile visits** (X and LinkedIn) | Paolo's only leading indicator tied to booked calls. LinkedIn target: 2,000 a month before adding bottom-of-funnel posts |
| Follows per 1K impressions | Better than impressions on our own data |
| Bookmarks | The save signal for article drops |
| Opt-ins per lead-magnet post | Once the capture funnel exists |
| **Booked calls by source** | A separate Calendly link per source: X bio, LinkedIn bio, VSL page, each email |

Any Ghosted Calls plan names the @maurojpelle export it used (file path and date range) on its first screen. Direction set by Mauro: a paid group with a one-time Whop payment for his skills and systems, after they improve, then traffic (review 2026-10-08 GC #57) [metric: first-pass approval rate]

---

## A week, in the 5–7 hour budget

| Day | Work | Time |
|---|---|---|
| Monday | Analysis (the table above), pick the week's ideas from the swipe file | 1h |
| Tuesday | Write 5 X listicles and how-tos from the week's real work, 1 ASCII diagram | 1.5h |
| Wednesday | 1 LinkedIn lead magnet: resource in Notion, image, copy, Lead Shark | 1.5h |
| Thursday | 1 article (company breakdown) | 1.5h |
| Friday | Warm outbound to the top 5 from the Lead Shark export | 0.5h |
| Daily | Replies to large in-niche accounts, answer every reply in a post's first 2 hours | 15 min |

---

## Open before this goes live

- `[NEEDS]` LinkedIn account status and follower count.
- `[NEEDS]` The capture funnel tool: opt-in page, VSL page and email tool. None exists.
- `[NEEDS]` The resource behind the Sep 5 post.
- The public-number sign-offs in `brand/claims.md` (~$300k/mo agency, a third from organic, the
  $28k deal) block every case-study post until Mauro approves them.
