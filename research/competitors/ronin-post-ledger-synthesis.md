# Synthesis: Ronin post ledger, 12 Aug to 15 Sep 2026

> **NOT ADOPTED.** Research input only. Nothing here enters `skills/` until Mauro signs off row by row on the table at the bottom.

**Source:** [`ronin-post-ledger-2026-09-15.md`](ronin-post-ledger-2026-09-15.md) (+ the source PDF alongside it)
**Written:** 2026-09-15
**Cross-read against:** [`../x-algorithm/x-algorithm-dig-2026-08-04.md`](../x-algorithm/x-algorithm-dig-2026-08-04.md), [`ronin-deronin.md`](ronin-deronin.md)

---

## 1. Where his impressions actually come from

63 items in 35 days produced 4,468,112 impressions. Three of those items are X Articles and they carry 64.3% of the total.

| Format | n | Median impr | Share of window |
|---|---|---|---|
| post | 45 | 15,430 | 22.8% |
| quote tweet pointing at an article | 14 | 32,126 | 10.3% |
| own X Article | 3 | 115,817 | 64.3% |

Drop the freak 2.7M item and the two remaining articles still median 87,660, which is 5.7x a plain post. The format difference survives the outlier.

The 45 plain posts are the floor of the account. They keep it alive and they do not move the number. That matches `author_diversity_scorer.rs` in the algorithm dig: a second and third post in the same feed response get multiplied down, so volume for its own sake is throttled at the response level.

## 2. The re-fire loop is the actual mechanic

He published 3 articles and posted 14 quote tweets pointing at articles. Roughly four to five re-fires per article, spread over the following weeks, each with a fresh angle in the QT body.

This is mechanically correct rather than lucky. `age_filter.rs` removes any post past `max_age` and fails closed, so nothing resurfaces in For You. An old article cannot come back on its own. A quote tweet creates a brand new post, with a brand new age clock, pointing at the same asset. It is the only way to re-serve a long-form piece to the feed.

A QT medians 32,126 against a plain post's 15,430. He is getting 2.1x a normal post for re-pointing at work he already did.

## 3. The number he is topping is not the number Mauro wants

Two of his three articles in this window can be identified from the 09-11 quote tweet, where he names them by age (inferred from the dates, not stated in the ledger):

- "9 days ago, 11,000 words article, full guide on how to become Robotics Engineer" → the 09-02 article, **2,699,633 impressions**
- "3 days ago, 8,000 words article, with sharing my full workflow on running solo-agency" → the 09-07 article, **59,504 impressions**

The mass-market career guide did 45x the on-topic operator piece. It has nothing to do with @CloseAI_hq, nothing to do with his solo-agency offer, and nothing to do with anyone who could buy from him. It is career-advice content for people entering a field.

So the honest read of "get to the top of the impressions": the top of the impressions is reachable, and the route Ronin took runs away from his own buyer. For Mauro, whose ICP is established agency owners at mid six figures a month and up, the equivalent move would be writing "how to start a marketing agency in 2026" and collecting a million views from people who will never book a call. That is belief #11 with a bigger budget.

The lever worth taking from this is the **format and the re-fire loop**, at ICP-native subject matter, measured on bookmark rate and profile clicks rather than raw impressions.

## 4. Bookmarks separate his winners from his floor

Median bookmark rate across the 63 items is 0.51% of impressions. His eight best run 1.83% to 3.54%.

The clearest case is the 09-10 anti-slop post: a complete, copy-pasteable protocol pasted into the post body, no link, no gate, no keyword. 26,653 impressions and a 2.62% bookmark rate on a plain post. The whole asset was in the post.

`share_via_dm` and `share_via_copy_link` are scored heads per the algorithm dig, and a bookmark is the save that precedes both. Bookmark rate is the leading indicator worth tracking here, not likes.

## 5. Volume has a documented cost

On 09-11 he posted that X flagged him for "high volume, repetitive or manipulative posting" and filed an appeal. He was running 1.8 items a day plus 8,000 and 11,000 word articles. The appeal outcome is not in this window.

His cadence is not a target to copy. It is the rate at which the spam classifier noticed him.

## 6. What this ledger cannot tell anyone

- Verbatim text exists for 8 of 63 items. The 2.7M article, the single result driving the whole window, has no text captured. Nothing here explains what the copy did.
- One account, ~110.8K followers, a dev and AI-engineering audience with a far wider addressable pool than Mauro's ICP, 35 days, n=3 on articles, one item at 60.4% of the total. This is not a sample anything can be regressed on. Every figure above is Ronin's, labelled as his, and stays that way in any content.
- Impressions are the only outcome measured. No calls, no revenue, no follower delta.

## 7. Flag, not a recommendation

`skills/content/anti-slop-protocol.md` was committed on 2026-09-10 (`03def52`), the same day Ronin published the same protocol in a post that took 26,653 impressions and 699 bookmarks. The protocol is public and widely copied. It is not proprietary to Mauro, it should never be presented as his own invention in content, and its own Inherited Sentence rule applies to the protocol text itself.

---

## Adopt / adapt / reject

Mauro signs off row by row. Nothing moves into `skills/` before that.

| # | Row | Call | Reason | Where it would land |
|---|---|---|---|---|
| 1 | X Articles as the primary reach vehicle, one per week, on ICP-native subject matter | **Adapt** | The format advantage is real and survives the outlier (5.7x a plain post). The topic selection does not transfer. Article subject stays inside the inbound lane per CLAUDE.md section 1. | `skills/content/vehicle-library.md`, `skills/ops/content-loop.md` |
| 2 | Re-fire every article with 4 to 5 quote tweets over the following 2 to 3 weeks, a different angle each time | **Adopt** | 2.1x a plain post, and `age_filter.rs` means a QT is the only way to re-serve a long-form asset. Costs no new writing. | `skills/ops/content-loop.md`, `skills/content/x-articles-POINTER.md` |
| 3 | Quote-tweet other operators' work with a real endorsement | **Adapt** | His 09-11 QT of @ForwardEditor took 55,211. Only run it when the piece is genuinely useful to an agency owner, otherwise it is borrowed reach from the wrong room. | `skills/content/x-reply-assistant.md` |
| 4 | Put the complete asset in the post body, no link, no gate | **Adopt** | 2.62% bookmark rate against a 0.51% median on the clearest example. Partly collides with the DM-trigger lead magnet play, so it needs a rule for which posts gate and which give it away outright. | `skills/content/vehicle-library.md`, `skills/lead-gen/lead-magnet/_master.md` |
| 5 | Track bookmark rate (bookmarks divided by impressions) as the per-post leading indicator, against Mauro's own baseline | **Adapt** | It separates his winners from his floor cleanly. His 0.51% median is his, not a benchmark. Mauro's baseline comes from `research/x-analytics/`. | `skills/ops/content-analytics-review.md`, `skills/ops/monday-acquisition-analysis.md` |
| 6 | Ugly specific numbers in the post body (88%, 40 to 60%, $56,880, 500 to 25,000 faces) | **Adopt** | His densest-specifics post took 95,192, third highest non-article in the window. Already beliefs #3 and #10 and the Round Number rule, so this confirms existing rules rather than adding one. | no change needed |
| 7 | 1.8 items per day | **Reject** | Author diversity decay throttles it, and X flagged him for "high volume, repetitive or manipulative posting" at exactly this rate. | — |
| 8 | Mass-appeal career-guide articles for the impression spike | **Reject** | 2,699,633 impressions from people who cannot buy. 45x the on-topic article and zero pipeline connection. | — |
| 9 | Platform-drama and account-status posts (rewards approval, spam-flag appeal) | **Reject** | 26,733 and 19,373, both above his median, and both creator-to-creator content. Mauro's ICP are agency owners, not X creators. Off-lane. | — |
| 10 | Any Ronin figure used in Mauro's content | **Adapt** | Only as "an account I track did X", always attributed, never as Mauro's own proof. His anchors are his. | `brand/claims.md` if any of these get cited |
