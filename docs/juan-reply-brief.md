# Juan: the reply brief for @maurojpelle

**Date:** 2026-10-08. **Data:** `research/x-analytics/maurojpelle-2026-07-08-to-2026-10-05.csv`, read with `tools/x-reply-targets.py`. **The list:** `brand/analytics/reply-target-list.md`.

## Why this changes

Since 1 Sep: 151 replies, 1 follow. In September the account sent 50 replies at a median of 24 impressions. In the first 5 days of October it sent 101 replies at a median of 9. Only 9 of the 137 replies outside the team went to a handle on the August list. More replies to random accounts gave less reach per reply.

## The rule

1. **15 replies a day, as a maximum.** The week with 20 a day had the lowest reach per reply.
2. **Within 15 minutes of the post.** An early reply sits near the top of the thread. A late reply sits under 200 others.
3. **On the list only.** KEEP, TEST, BIG ROOMS and BUYER ACCOUNTS in `reply-target-list.md`. A handle that is not on the list gets no reply. If an account looks right, add it to a note for Mauro. Do not reply first.
4. **One specific point from Mauro's real work in every reply.** A question about their system, or one fact from his. Take the facts from `brand/claims.md` (rows marked "yes") and from his own posts in the export. Never invent a number.
5. **No replies to the team.** @lorenzo_pravata and @Bogzabs96 got 14 replies, 694 impressions and 0 follows. A like or a repost is fine.
6. **No one-word replies.** "Fireee", "so true", "nice list", "appreciate it bro!" are banned.

## What a good reply looks like (real rows from the export)

| Reply | Impressions | Profile visits |
|---|---|---|
| @danielfazio "every one of our best clients could do this themselves, they just do the math on their hourly rate" | 139 | **6** |
| @retentiongoat "whats your source list for the clay enrichment on this" | 100 | **4** |
| @ethanejk "25 posts a day is wild, hows the quality holding up past post 10" | 100 | **4** |
| @lukethorburg "whats level 6 actually look like from the inside, just more pods or something structurally different" | 154 | **3** |
| @tirimisyjr "we log every objection right after the call into one doc, half our posts come straight out of it" | 18 | 2 |

What they share: each one asks about the poster's own system, or gives one concrete detail from a real operation.

## What a generic reply looks like

| Reply | Impressions | Profile visits |
|---|---|---|
| @lorenzo_pravata "Fireee" | 117 | 1 (team, 0 follows) |
| @madebyharman "so true" | 10 | 0 |
| @chriscoolstuff "nice list" | 17 | 0 |
| @revenumaxxing "the scoreboard lies weekly, the process doesnt" | 18 | 0 |
| @matt_teeixeira "focus is just saying no to good ideas on purpose" | 3 | 0 |

@revenumaxxing got 13 replies of this kind: 254 impressions, 1 profile visit, 0 follows. A wise-sounding sentence gets no profile visit.

**Where to find Mauro's facts (his own posts):** the four lowest-reach articles booked 78% of the calls. The same gated offer ran three times: 263 comments, then 81, then 34. Boards for his YouTube videos took 4 hours each and now take close to 2. Objections from calls go into one doc and feed the posts.

## The daily routine (20 minutes in total)

1. **Once:** turn on post notifications (the bell) for every account in KEEP, TEST, BIG ROOMS and BUYER ACCOUNTS.
2. **When a notification lands:** open it. If the post is on-lane and under 15 minutes old, reply. If the post is about AI models or tools, or about a first client or $1k MRR, skip it.
3. **Write the reply in under 1 minute.** One sentence or one question. Lowercase is fine. No em dashes. Use `/reply` in Claude Code when you are not sure.
4. **Keep a tally.** Stop at 15 for the day. Spread them over at least 8 different accounts.
5. **End of day (2 minutes):** write down any new account that looked right. Mauro decides on Monday.

## What gets measured every week

Every Monday:

1. Mauro exports X Analytics > Content for the last 7 days into `research/x-analytics/`.
2. Run `python3 tools/x-reply-targets.py --since <last Monday> --csv <that file> --rows`.
3. Read three numbers:
   - **Profile visits per reply** (outside the team). Baseline since 1 Sep: **0.43**.
   - **Follows from replies.** Baseline since 1 Sep: **1** in 5 weeks.
   - **Replies to roster handles.** The target is every reply.
4. Move accounts between tiers with the rules at the end of `reply-target-list.md`.
