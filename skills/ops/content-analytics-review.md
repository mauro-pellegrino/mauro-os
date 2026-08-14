# Skill: Content Analytics Review (Monthly)

**Version:** 1.0
**Created:** 2026-08-14
**Cadence:** Monthly
**Input:** X (Twitter) account analytics content export (CSV) for the period, optionally the prior month's export for comparison
**Output:** A reach-and-distribution read of what to post more of, who to reply to, and how to grow impressions next month, plus a short secondary note on topics/angles

---

## What This Skill Does

Mauro exports his X content analytics once a month and this skill turns it into a decision, not a dashboard. The goal is reach: **impressions and new follows.** It answers three questions with his real numbers:

1. **Format** — which post types earn reach per post, so he posts more of what works.
2. **Distribution** — which accounts he replies to actually put him in front of people (and which are dead weight), plus where new follows really come from.
3. **Impression growth** — the specific levers to pull next month, ranked, grounded in the export.

A short secondary section covers topics/angles (what to double down on by bookmarks and follows), but reach is the headline. The reason: for a still-small account, the bottleneck is distribution, not topic quality. Good posts that nobody sees are a distribution problem, and this skill treats them that way.

---

## Required Reading

- `brand/positioning.md` — his lane, so topic/angle calls point at the right audience
- `brand/audience.md` — the ICP and the rooms (accounts) worth being seen in
- Prior month's saved review (if any) in `brand/analytics/` so month-over-month is real

---

## The Data

X's content export has these columns (the script keys off them, don't rename):

`Post id, Date, Post text, Post Link, Impressions, Likes, Engagements, Bookmarks, Shares, New follows, Replies, Reposts, Profile visits, Detail Expands, URL Clicks, Hashtag Clicks, Permalink Clicks`

What each signal means for this review:
- **Impressions** — raw reach. The headline metric.
- **New follows** — the conversion that compounds. Weight this heavily; reach without follows is noise.
- **Bookmarks** — save-worthy value. A high-bookmark, low-impression post is good content with a distribution problem: redistribute it.
- **Profile visits** — intent. A post that sends people to the profile is doing account-growth work even at low reach.
- **Engagements / Likes / Replies** — supporting, not primary. Don't optimize for likes.

---

## Step 1: Run the Script

From the repo root:

```bash
python skills/ops/content-analytics-review.py "<path-to-this-month-export.csv>" --prev "<path-to-last-month-export.csv>"
```

`--prev` is optional; drop it for the first run. The script prints: totals (+ deltas vs prior month), format table, reply-reach by account, top posts, follow drivers, save-worthy posts, and impressions-by-length. It flags any bucket or account with n<3 as directional only.

If Python isn't handy, the same analysis can be done by reading the CSV directly, but the script keeps the month-over-month math honest and repeatable.

---

## Step 2: Read It Reach-First

Interpret the output in this order. Do not skip to topics.

### Format
Rank formats by **mean impressions per post** and by **follows**, not by total impression share (share just rewards whatever he posted most of). Call out the format that earns the most reach per post and whether he's under-using it. On the Aug 2025-2026 baseline: link/media posts earned ~4x the reach per post of everything else but were only 10 of 319 posts. That's an under-use flag.

### Distribution (the core of this review)
The reply-reach-by-account table is the most actionable thing here. For each account he replies to:
- **High imp + high follows** → keep replying, this room converts (baseline example: @perkmaybe, 3 replies to 3 follows).
- **High imp + zero follows** → reach without conversion. Fine for visibility, but he's spending a lot of replies for nothing (baseline: @lorenzo_pravata, 27 replies, 1,470 imp, 0 follows, mostly banter). Flag it.
- **One-off big hits** → replying under a large account once spiked reach (baseline: @thedankoe 1,349 imp off one reply). These say "reply more under big accounts in the niche," which is a distribution lever, not luck to chase randomly.

Then look at the follow-driver list: what actually produced follows this month, and what format/room those came from.

### Impression growth levers
Turn the above into a ranked, specific list for next month. Every lever must trace to a number in the export. Typical shape (re-derive from the actual data each month, don't copy):
1. Post more of the highest reach-per-post format that's under-used.
2. Reallocate reply volume from dead-weight accounts (high imp, no follows, no relationship value) toward accounts/rooms that convert or that are large and in-niche.
3. Redistribute the top save-worthy (bookmarked) posts: they're proven-good content that under-reached. Re-cut them as the winning format, or re-post at a better time.

### Topics / angles (secondary)
Rank by **bookmarks and follows**, never by impressions alone (a viral banter reply tells you nothing about topic). Name the 2-3 angles that earned saves or follows and are on-lane (personal brand, AI-for-content, B2B acquisition, agency ops). Flag anything off-lane (ecom, ad creative) that happened to reach, so he doesn't chase it.

---

## Step 3: Output the Review

Keep it to one screen. Format:

```
CONTENT ANALYTICS REVIEW — [month]

Headline: [impressions, follows, + deltas vs last month in one line]

FORMAT — post more of:
  - [format]: [reach/post + follow note]  ← [under-used? / working?]

DISTRIBUTION:
  - Keep replying to: [accounts/rooms that convert]
  - Cut / reallocate: [dead-weight accounts, with the number]
  - Reply more under: [large in-niche accounts that spiked reach]

IMPRESSION LEVERS FOR NEXT MONTH (ranked):
  1. [lever] — [expected effect, tied to the data]
  2. ...
  3. ...

TOPICS/ANGLES to double down on (by saves + follows):
  - [angle] — [why, with the number]

SAMPLE-SIZE FLAGS:
  - [anything resting on n<3 posts, marked directional]
```

Lead with the number, end on the point. No trailing summary sentence (voice.md rule #4).

---

## Step 4: Save the Review

Save the finished review to `brand/analytics/[YYYY-MM]-content-review.md` so next month's `--prev` comparison and the trend line are real. Save the CSV export alongside it (`brand/analytics/exports/`) per the repo's fetch-once-save-always rule. Commit both.

The review is an internal working doc, not public. It never publishes.

---

## Honesty Rules (specific to this skill)

- **Never invent a number.** Every claim traces to a cell in the export (belief #10, voice.md rule #6). If the data can't support a conclusion, say the data is thin and stop.
- **Flag small samples.** With a low-volume account, one viral post distorts means. Any conclusion resting on fewer than 3 posts is directional, label it.
- **Reach without follows is not a win.** Don't celebrate a banter reply that spiked impressions and converted nobody. Weight follows and bookmarks over raw reach.
- **Truth over flattery (belief #13).** If the month was flat or down, say so plainly and diagnose why. A pretty report that hides a stall is useless.
- **Distribution before topics.** Resist turning this into a topic-idea generator. The lever for a small account is who sees the content, not another angle.

---

## Anti-Patterns

- Ranking formats by total impression share instead of per-post reach (rewards volume, not quality).
- Optimizing for likes/engagements instead of follows and bookmarks.
- Treating a one-off viral reply as a repeatable topic insight.
- Recommending "post about X topic" when the data shows the topic already earns saves and just needs distribution.
- Skipping the month-over-month comparison when a prior export exists.
- Publishing or sharing the review. It's internal.

---

## Cross-Reference

- **Companion script**: `skills/ops/content-analytics-review.py`
- **Call attribution (different input, different goal)**: `skills/ops/monday-acquisition-analysis.md` ties content to *booked calls* via the Calendly export; this skill ties content to *reach and follows* via the X export. Run both; they answer different questions.
- **Turning save-worthy posts into more reach**: `skills/content/short-form/short-form-from-long-content.md`, `skills/content/visual-docs/mauro-visual-doc-system.md` (infographics, the highest-reach format on the baseline)
- **Better replies for the distribution lever**: `skills/content/x-reply-assistant.md`
- **Voice rules**: `brand/voice.md`
