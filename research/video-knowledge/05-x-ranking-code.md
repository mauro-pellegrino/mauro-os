# 05 · i read x's ranking code so you don't have to

**Alt title:** every x algorithm number you've seen is from 2023
**What this file is:** the information behind the video. Not a script.
**Written:** 2026-09-07
**Overlap warning:** the existing Miro board "YT 03 · The X Algorithm Weights Nobody Has" covers the
same dig. This is either the replacement for that board or the sequel that goes wider. Decide before
recording.

**Sources**
- `research/x-algorithm/x-algorithm-dig-2026-08-04.md` (read from the source, method documented)
- `research/transcripts/maurojpelle/2026-09-04-x-source-code-myth-buster-thread.md`
- `github.com/xai-org/x-algorithm`

**ICP cut:** the operator being sold "algorithm secrets" by people who have never opened the repo.
**Reach cut:** this is the highest-reach idea in the set. It is a public, checkable claim against
the most repeated numbers in the entire content niche.

---

## The one claim

The formula is public and the numbers are not. Every weight circulating in 2026 comes from a
different system that was replaced.

---

## The information

### 1. The repo, with its facts at fetch time

`xai-org/x-algorithm`, the official one. Created 2026-01-19. Last code push **2026-05-15**. 26,909
stars. 216 files. Rust 62.9%, Python 37.1%. Fetched and read 2026-08-04 through the GitHub API and
raw file reads, with web search used only to identify the claims that then got checked against code.
`[measured: recorded in the dig, with method]`

### 2. The finding

`home-mixer/scorers/weighted_scorer.rs` computes the final score as a weighted sum of predicted
action probabilities. Every weight is a named constant imported from `crate::params as p`, for
example `p::REPLY_WEIGHT` and `p::RETWEET_WEIGHT`.

**There is no `params` module in the repository.** Verified: no file matching `param`, `config` or
`const` anywhere in the 216-file tree, and 404 on `home-mixer/params.rs`, `home-mixer/params/mod.rs`
and `home-mixer/src/params.rs`.

So the published code tells you exactly which signals are scored and how they combine, and tells
you nothing about their relative size.

### 3. Where the folklore comes from

Every "a reply is worth 13.5 likes", "a repost is 20x a like", "one reply outweighs 150 likes"
figure comes from the **2023** `twitter/the-algorithm` release, which did ship explicit weights.
Those numbers are three years old and describe a system that has since been replaced. They are
folklore. They do not go in content.

### 4. The architecture, verified

Two candidate sources, ranked together. **Thunder** is the in-memory post store for accounts you
follow. **Phoenix retrieval** is a two-tower model over a global corpus for everything else. Both
are scored by **Phoenix**, a Grok-based transformer ported from the Grok-1 open-source release.
The pipeline runs query hydration, candidate sourcing, candidate hydration, pre-scoring filters,
scoring, top-K selection, post-selection filters.

### 5. The sentence that matters most

Straight from the repo README:

> "We have eliminated every single hand-engineered feature and most heuristics from the system. The
> Grok-based transformer does all the heavy lifting by understanding your engagement history (what
> you liked, replied to, shared, etc.) and using that to determine what content is relevant to you."

Ranking is driven by a model reading the viewer's own engagement history. That is the death of
reverse-engineerable rules, and it is the actual takeaway for anyone posting.

### 6. What the operator does with this

Since there are no exploitable weights, the only lever left is who your post gets shown to, which
is decided by the engagement history of the people it reaches first. That is a content-quality and
audience-composition argument, and it is the argument the video should land on.

---

## Evidence

| Claim | Status |
|---|---|
| No params module, verified by 404 and tree search | `[measured: the dig, 2026-08-04]` |
| Repo facts: 26,909 stars, 216 files, last push 2026-05-15 | `[measured: at fetch time, may have moved]` |
| Circulating weights originate in the 2023 release | `[measured: the 2023 repo did ship weights]` |
| Thunder, Phoenix retrieval, Phoenix scorer | `[measured: read from source]` |
| The rules era is over for practical purposes | `[assumed: reading of the README quote]` |

---

## Beats on camera

1. The numbers everyone quotes, shown as screenshots.
2. Open the repo live. Stars, files, last push date.
3. The scorer file. The weighted sum. The named constants.
4. Search for the params module. Watch it not exist.
5. Where the old numbers actually came from.
6. The architecture in one diagram.
7. Read the README quote out loud.
8. What is left to optimise once the rules are gone.
9. How to run the same check yourself on any claim.
10. CTA.

---

## Do not say

- Any weight, even to debunk it, without saying 2023 in the same sentence.
- That the repo is fake or that X is hiding something. It ships the formula and withholds the
  constants, and that is the accurate statement.
- Anything about the state of the repo after 2026-08-04 without re-checking first.

## Gaps

- `[NEEDS: re-fetch the repo facts on the day of recording, the stars and last-push date will have moved]`
