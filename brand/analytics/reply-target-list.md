# Reply Target List

**Built:** 2026-08-24 from `exports/2026-08-18-to-08-24-content.csv` (246 replies, 166 accounts)
**Used by:** `skills/content/x-reply-assistant.md` Step 0 (the room test)
**Refresh:** every weekly analytics review. Move accounts between tiers on the numbers, not on feel.

Read this before judging any reply. If the handle is on the RED list, the answer is skip regardless of how good the post is.

---

## KEEP: rooms that converted

| Account | Replies | Imp | Follows | Profile visits | What the room talks about |
|---|---|---|---|---|---|
| @paolo_scales | 4 | 257 | 1 | 2 | Sales ops, audit call vs sales call. Best combination of volume, reach and conversion in the data. |
| @simonnyyberg | 4 | 46 | **2** | 3 | Automation, efficiency, where deals come from. Highest conversion of any account. |
| @chanduuu_cs | 6 | 164 | 1 | 5 | Mixed. Converted once, but his replies there ran to banter. Keep and raise the quality. |
| @kearneyy | 1 | 58 | 1 | 5 | Asked what he does, he answered with the engine. 5 profile visits off one reply. |
| @DanielSmidstrup | 1 | 13 | 1 | 0 | X growth, posts vs replies. |
| @GrammarHippy | 1 | 37 | 1 | 0 | Client relationships, staying close to the client. |
| @thejustinwelsh | 1 | 5 | 1 | 0 | Large solopreneur audience. One follow off 5 impressions. Worth real volume. |
| @Gavel_on_X | 2 | 18 | 1 | 1 | Mindset/goals. Thin, but it converted. |

## TEST: on-lane rooms that have not converted yet

These got on-lane replies and produced profile visits or real reach without a follow. Give each 5+ replies before judging.

| Account | Replies | Imp | Profile visits | Why it belongs here |
|---|---|---|---|---|
| @AlexHartsuff | 4 | 158 | **7** | Agency pricing ("jumped 3k to 10k/mo for the same work once i repriced"). Highest profile visits of any account in the week. |
| @scaling_shields | 1 | 189 | 3 | Cold email burning out for agencies. Exact ICP pain, only tried once. |
| @Dwriteway | 2 | 211 | 1 | Inbound, not needing clients. Real reach. |
| @MCovBrown | 2 | 112 | 0 | Cheap clients needing the most saving. Agency room. |
| @gabriel1 | 2 | 65 | 0 | Analysing your best clients. Agency room. |
| @itsmarcosruiz | 2 | 39 | 2 | Content vetting you before outreach. |
| @LoganTGott | 2 | 39 | 0 | Profile and posts, growth room. |
| @heyblake | 3 | 35 | 0 | Call transcripts into buyer language. On-lane, room may be too small. |
| @georgeclem | 2 | 17 | 0 | "Owners hide in fulfilment because acquisition feels spammy." Perfect ICP language, tiny reach. |
| @siddharthwv | 3 | 23 | 1 | Cringe content booking calls. On-lane, tiny reach. |
| @MichLieben | 2 | 8 | 0 | Proof posts booking calls. On-lane, tiny reach. |

## RED: do not reply

The room does not contain agency owners. Two ways a room goes red.

**1. Wrong subject.** AI models, tools, benchmarks, prompt tricks. The accounts below. These paid in impressions and returned nothing.

**2. Wrong altitude.** The post is pitched at $1k MRR, first client, first $10k, quitting the job, "proof someone will pay." No handle needed to call it, the numbers in the post are the signal. Mauro's ICP is at $100k to $500k a month, so the replies are 100x below him and there is nobody there to convert. Skip on sight.

| Account | Replies | Imp | Follows | Room |
|---|---|---|---|---|
| @heyshrutimishra | 2 | **1,621** | 0 | AI models, Chinese model comparisons. Biggest reach of the week, zero return. |
| @trikcode | 1 | 718 | 0 | Model preference debate. |
| @mishaglouberman | 1 | 495 | 0 | Off-lane entirely (data/sleep). |
| @TTrimoreau | 5 | 281 | 0 | Tool switching, "Claude code for now". 2nd highest reply volume, nothing back. |
| @rubenhassid | 3 | 179 | 0 | AI prompting and infographics. AI-creator audience. |
| @levie | 1 | 158 | 0 | Models and evals, enterprise tech audience. |
| @aymanalabdul, @polydao, @dan__rosenthal, @wilczyn, @NickpxJ, @omkarships, @MediaKing, @YashHustle_22 | 17 total | 268 | 0 | The Claude/tool-talk cluster. Same room, different handles. |

## DROP: dead weight

3+ replies, 0 follows, 0-1 profile visits. Off the list until the weekly review says otherwise.

@KevinSzabo14 (5), @Aidanb2b (4), @AdityaKhanduri (4), @HeyAliux (4), @sattyyouneed (4), @pmitu (3), @GohilHardy (3), @launch_llama (3)

Combined across the 11 accounts flagged in the review: 39 replies, 663 impressions, 0 follows, 4 profile visits.

---

## The gap in this list

KEEP has 8 accounts and only one of them (@paolo_scales, 257 imp over 4 replies) delivers meaningful reach. The green rooms found so far are either tiny (@georgeclem 17 imp, @MichLieben 8 imp) or barely tested.

Meanwhile every large room he is currently in is red. That is the actual bottleneck: **he has no big green room.** 

So the sourcing job is specific: find 8 to 10 accounts whose posts are about agency pipeline, client acquisition, retainers and offers, and whose replies pull hundreds of impressions rather than dozens. Until that list exists, reply volume can be reallocated off the red rooms but total reach will stay capped.

Candidates to check first, since their audiences overlap the ICP: @thejustinwelsh (already converted once), @scaling_shields, @AlexHartsuff, @paolo_scales, and whoever those four reply to.

## How to maintain this

1. Run `skills/ops/content-analytics-review.md` weekly.
2. Any account with 3+ replies, 0 follows and 0-1 profile visits moves to DROP.
3. Any account that produces a follow moves to KEEP.
4. Any account whose replies are about models, tools or benchmarks moves to RED, no matter the reach.
4b. Any account posting at beginner altitude ($1k MRR, first client, first $10k) moves to RED, no matter the reach.
5. Any TEST account still at zero after 5 replies moves to DROP.
