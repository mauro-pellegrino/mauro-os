# X (Twitter) Algorithm Dig — read from the source code

**Source:** [github.com/xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) (official, xAI org)
**Method:** GitHub REST API + raw file reads of the actual Rust source. Web search used only to identify claims, then every claim checked against code.
**Fetched:** 2026-08-04
**Repo facts at fetch time:** created 2026-01-19 · last code push **2026-05-15** · 26,909 stars · 216 files · Rust 62.9% / Python 37.1%

---

## 0. The single most important finding

**The formula is public. The numbers are not.**

`home-mixer/scorers/weighted_scorer.rs` computes the final score as a weighted sum of predicted action probabilities. Every weight is a named constant imported from `crate::params as p` (e.g. `p::REPLY_WEIGHT`, `p::RETWEET_WEIGHT`).

**There is no `params` module in the repository.** Verified: no file matching `param`/`config`/`const` anywhere in the 216-file tree, and 404 on `home-mixer/params.rs`, `home-mixer/params/mod.rs`, `home-mixer/src/params.rs`.

So the published code tells you **exactly which signals are scored and how they combine**, and tells you **nothing about their relative size**.

Every "a reply is worth 13.5 likes" / "a repost is 20x a like" / "one reply outweighs 150 likes" figure circulating in 2026 comes from the **2023** `twitter/the-algorithm` release, which did ship explicit weights. Those numbers are three years old, from a system since replaced. Treat them as folklore, not fact. Do not put them in content.

---

## 1. Architecture (verified)

Two candidate sources, ranked together:

| Source | Component | What it is |
|---|---|---|
| In-network | **Thunder** | In-memory post store, accounts you follow |
| Out-of-network | **Phoenix retrieval** | Two-tower model over a global corpus |

Both are scored by **Phoenix**, a Grok-based transformer (ported from the Grok-1 open-source release). Pipeline: query hydration → candidate sourcing → candidate hydration → pre-scoring filters → scoring → top-K selection → post-selection filters.

**Direct quote from the README:**

> "We have eliminated every single hand-engineered feature and most heuristics from the system. The Grok-based transformer does all the heavy lifting by understanding your engagement history (what you liked, replied to, shared, etc.) and using that to determine what content is relevant to you."

This is the most consequential sentence in the repo. Ranking is driven by a model reading **the viewer's own engagement history**, not by rules you can reverse-engineer and exploit.

---

## 2. The 19 scored actions (verified, exact list)

From `weighted_scorer.rs`. This is the complete set of heads that feed the score.

**Positive (15):**
`favorite` · `reply` · `retweet` · `photo_expand` · `click` · `profile_click` · `vqv` (video quality view) · `share` · `share_via_dm` · `share_via_copy_link` · `dwell` · `quote` · `quoted_click` · `dwell_time` (continuous) · `follow_author`

**Negative (4):**
`not_interested` · `block_author` · `mute_author` · `report`

Negative-scoring posts run through `offset_score()`, which renormalizes them against `NEGATIVE_WEIGHTS_SUM` / `WEIGHTS_SUM` rather than simply flooring at zero.

**What this list actually tells us:** likes are one of fifteen positive heads. `profile_click`, `follow_author`, `share_via_dm`, `share_via_copy_link`, `dwell_time` and `quoted_click` are all separately scored. A post that makes someone open your profile, follow you, and DM it to a colleague is scoring on four heads at once.

---

## 3. Author diversity: posting more does not stack (verified)

`author_diversity_scorer.rs`:

```
multiplier(position) = (1 - floor) * decay^position + floor
```

`position` = how many of that author's higher-scoring posts already appear in the same feed response. Your first post gets multiplier ~1.0. Your second gets decayed. Your third more so. It asymptotes to `floor`, so it never reaches zero.

`AUTHOR_DIVERSITY_DECAY` and `AUTHOR_DIVERSITY_FLOOR` are both in the unpublished params.

**Implication:** volume for its own sake is throttled at the response level. Five posts do not buy five slots in one person's feed.

---

## 4. Out-of-network is discounted (verified)

`oon_scorer.rs`, with its own comment:

> `// Prioritize in-network candidates over out-of-network candidates`

```rust
Some(false) => base_score * p::OON_WEIGHT_FACTOR,
```

Out-of-network candidates are multiplied by a factor explicitly framed as a de-prioritization. `OON_WEIGHT_FACTOR` is unpublished.

**Implication:** reaching people who don't follow you is structurally harder than reaching people who do. Growth comes from converting the reach you get into follows (`follow_author` is a scored head), not from banking on out-of-network virality.

---

## 5. Age is a hard cutoff, not a decay (verified)

`age_filter.rs` removes any post older than `max_age`. Note the failure mode:

```rust
duration_since_creation_opt(tweet_id).map(|age| age <= self.max_age).unwrap_or(false)
```

If age can't be determined, the post is **removed**. Fails closed.

**Implication:** there is no evergreen resurfacing in For You. An old post does not come back. Re-angle and repost instead.

---

## 6. Video gating (verified)

`weighted_scorer.rs` only applies the video-quality-view weight if the video clears a minimum:

```rust
if candidate.video_duration_ms.is_some_and(|ms| ms > p::MIN_VIDEO_DURATION_MS)
    { p::VQV_WEIGHT } else { 0.0 }
```

There is a **minimum** duration gate and no maximum in this code. `MIN_VIDEO_DURATION_MS` is unpublished.

`video_filter.rs` is a user-preference filter (fires only when `query.exclude_videos` is set), not a penalty.

---

## 7. The full filter list (verified, 20 filters)

`age` · `ancillary_vf` · `author_socialgraph` · `core_data_hydration` · `dedup_conversation` · `drop_duplicates` · `ineligible_subscription` · `muted_keyword` · `new_user_topic_ids` · `previously_seen_posts` · `previously_seen_posts_backup` · `previously_served_posts` · `retweet_deduplication` · `self_tweet` · `topic_ids` · `vf` (visibility filtering) · `video`

**There is no link filter.** Nothing in the published filter set or the scorer touches external links.

`ineligible_subscription_filter.rs` exists, which means subscription status gates something, but no multiplier or magnitude is published.

---

## 8. Also shipped in the May 15 update

- **Grox** (`grox/`): content-understanding service with classifiers and embedders for **spam detection, post-category classification, and PTOS policy enforcement**. So there is a classifier layer, separate from ranking.
- **Ads blending** (`home-mixer/ads/`): ad injection and positioning, with brand-safety tracking.
- Pre-trained mini Phoenix model (~3 GB via Git LFS), 256-dim embeddings, 4 heads, 2 layers. Runnable inference.
- Query hydrators now include impression bloom filters, mutual follow graphs, followed topics, starter packs, served history.

---

## 9. Claims that do NOT survive contact with the code

| Circulating claim | Verdict |
|---|---|
| "Reply = 13.5x a like, repost = 20x, bookmark = 10x" | **2023 numbers.** Not in the 2026 code. Weights unpublished. |
| "One reply the author responds to = 150 likes" | Same. 2023 release. |
| "External links suppressed up to 80%" | **No link filter or link weight exists** in the published code. Unsupported. |
| "First 30 minutes is the mathematical point of no return" | No time-window mechanic in the code. There is a hard age cutoff, not a 30-minute decay curve. |
| "Native video under 2m20s gets the most distribution" | Code has a **minimum** duration gate for VQV credit and no maximum. Value unpublished. |
| "Premium = 2x out-of-network boost; non-Premium need 4-8x engagement" | A subscription filter exists; no multiplier is published. Unsupported as stated. |
| "Updated every four weeks" | **Last code push was 2026-05-15.** ~2.5 months stale as of 2026-08-04. |
| "Bookmarks are a top-3 signal" | `bookmark` is **not among the 19 action heads.** Not in this scorer at all. |

The date claims in secondary coverage also conflict (Jan 11 vs Jan 20 vs May 15). Repo `created_at` is **2026-01-19**; the May 15 release is a documented update in the README.

---

## 10. What this means for @maurojpelle

1. **Hacks are dead by design.** "Eliminated every single hand-engineered feature" means there is no rule left to game. The lever is being the post the right viewer's history already predicts they'll engage with.
2. **Optimize for the heads that compound, not for likes.** `profile_click` → `follow_author` is the growth path and both are scored. A post that earns a profile visit and a follow is worth more than one that earns a like, mechanically.
3. **`share_via_dm` and `share_via_copy_link` are scored actions.** The auto-DM lead-magnet flow (comment keyword → DM) and "send this to your ops person" content are working with the scorer, not around it.
4. **Volume is throttled per response.** Author diversity decay means the fix for low reach is not more posts.
5. **Ragebait carries real downside.** `not_interested`, `block_author`, `mute_author`, `report` are subtracted and renormalized. Engagement bait that provokes mutes lowers the score.
6. **Nothing resurfaces.** Hard age cutoff. Repurposing means reposting a new angle, not hoping an old post revives.
7. **Reply depth matters directionally, magnitude unknown.** `reply` and `quote` are separate heads from `favorite`, so conversation is scored separately from approval. How much more is unpublished. **Say "replies are scored separately from likes," never "a reply is worth 13.5 likes."**

---

## 11. Content angle this unlocks

The strongest available angle is not "here are the ranking factors." Every SEO blog has that, wrong. It is:

**"Everyone is quoting X algorithm weights from 2023. I read the actual 2026 code and the weights aren't in it."**

That is checkable, contrarian, and true, and it lands squarely in the anti-hype lane. Supporting proof: the `crate::params` import with no params module, and the 19-head list nobody is publishing correctly.

---

## 12. Open items / what would sharpen this

- The params module will not be published; treat all magnitudes as permanently unknown unless xAI changes course.
- `phoenix/README.md` states the released code is *"representative of the model used internally with the exception of specific scaling optimizations."*
- Worth re-checking the repo monthly for a push newer than 2026-05-15.
- Not yet read: `grox/tasks/task_filters.py` (spam classification specifics), `home-mixer/ads/`, the retrieval two-tower detail in `phoenix/`.
