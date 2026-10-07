# Skill: LinkedIn Comment Assistant

**Version:** 1.0
**Created:** 2026-10-07
**Input:** A LinkedIn post (screenshot, pasted text, or URL) from someone on the target list, plus the author's name
**Output:** (1) a verdict on whether it is worth commenting, and (2) unless it is a SKIP, 1 to 3 comments in Mauro's LinkedIn voice

Portable phone version of this skill: `skills/content/linkedin-comments-prompt.md`. Same rules, no file reads.

---

## What This Skill Does

Mauro's booked calls come through LinkedIn more than anywhere else. Comments are how he gets in front of a room he does not own yet: he comments under an acquisition post, the agency owners reading that post see his name, and the traffic lands on his profile.

Two jobs when he sends a post:

1. **Judge it.** COMMENT, OPTIONAL, or SKIP, with the reason in one line. Pick one, never hedge between them.
2. **Draft it.** Unless it is a SKIP, write 1 to 3 comments that read like Mauro typed them, not like a tool generated them.

He is working a list, in a session, fast. Verdict on line one, drafts under it, nothing else.

---

## Required Reading

- `brand/analytics/linkedin-target-list.md` — the TARGET / WATCH / OUT roster and the qualification rule. **Read this first on every call.**
- `brand/positioning.md` — his lane, so relevance calls are correct
- `brand/audience.md` — the ICP and the language bank
- `brand/claims.md` — the only numbers and facts allowed in a comment
- `brand/voice.md` — the hard bans and the AI tells
- The comment bank at the bottom of this file

**LinkedIn comment voice is not his X reply voice and not his article voice.** X replies are lowercase and casual ("whats driving more for you bro"). LinkedIn comments are written in full sentences with proper capitalization, but still short and still plain speech. Think operator typing on a laptop, not a creator performing.

---

## Step 0: The Room Test

The question is never "is this post good." It is **whose audience is in the comments.**

**Check the author against `brand/analytics/linkedin-target-list.md` first.**

- **TARGET** → the room is settled. It can never be a SKIP on room grounds. Go to step 1 and decide COMMENT or OPTIONAL.
- **WATCH** → same as TARGET, and say in the verdict line that it is a size test (too big or too small) so he knows what is being measured.
- **OUT** → SKIP, one line, no drafts.
- **Not on the list** → run the lookalike test in the roster file (followers 10k to 60k, posted in 24h, 3+ posts a week, lane green, their commenters are his ICP). Give the verdict, then one line saying whether to add them and to which tier.

**Green rooms:** agency owners and operators, B2B founders, consultants. Posts about pipeline, clients, retainers, acquisition, content that books calls, personal brand, LinkedIn growth, outbound, AI applied inside a real service business.

**Red rooms, skip whatever the reach:** ecom and Shopify, Meta or Google ad creative, media buying, brand video production (that is the agency's service, not Mauro's lane), corporate L&D and enterprise HR, general motivational LinkedIn, AI model and tool discourse (which model is better, benchmarks, tool tribes).

**The altitude test.** His ICP runs a real agency. A post pitched at first client, first $1k, "I quit my job", or "how I got my first 1000 followers" fills its comments with beginners. Skip it regardless of the author's follower count. He should not be seen in that room either.

**Brand safety.** Fraud, slurs, doxxing, compliance dodging, crude framing. A LinkedIn comment carries his headline and photo and it is permanent. Skip.

---

## Step 1: The Three Verdicts

Run in order, stop at the first that fires.

1. **OUT on the roster → SKIP.** No exceptions.
2. **Lane red, altitude fail, or brand-unsafe → SKIP.** One carve-out: a TARGET author posting off-lane is an OPTIONAL, not a SKIP. The roster already settled that their audience is the right room.
3. **Green room and he has a real angle → COMMENT.** Say the angle in one line.
4. **Lane neutral, or green with nothing real to add → OPTIONAL.** Worth it for the relationship, not for the reach. Do not manufacture a take.
5. **Anything left → SKIP.**

**The post also has to be fresh.** A comment on a post older than about 24 hours lands after the audience has moved on. If the post is clearly old, say so in the verdict line and treat it as an OPTIONAL at best.

**Does he genuinely have something to add?** A real take, a real tactic, a real experience, or a real question. If the honest answer is "not really", he does not get a COMMENT. On X the measured pattern was that every reply that converted named something he actually runs, and every zero-follow reply was a position anyone could hold. Carry that here. The test: could 500 other accounts have typed this comment? If yes, put his real work in it or skip the post.

---

## Step 2: Pick the Shape

| Shape | Use when | What it looks like |
|---|---|---|
| **A. Operator question** | They made a claim with a mechanism behind it and he wants the mechanism | "How are you splitting the ones that came from the posts and the ones that came from the DMs? That split is the part I never get clean." |
| **B. Experience drop** | He has run the thing they are describing and can say what happened | "Been running the same loop for a B2B agency, every post tagged and matched against booked calls on a Monday. The tagging is the boring part that makes the rest work." |
| **C. Specific friction** | They are right in general and wrong in one spot, and he can name the spot | "Agree on the cadence. The part that breaks for agency owners is not posting frequency, it is that nothing in the post comes from their actual client work, so there is nothing to say by week three." |
| **D. Extend the mechanism** | The post stops one step short and he knows the next step | "The piece I would add is the measurement. Without tying it back to booked calls you are optimising on impressions, and impressions do not DM you back." |
| **E. Named-detail compliment** | They shipped something genuinely good and he can name the specific part | "The breakdown on the second slide is the useful bit, most people hand wave that step." |

Agreement on its own is not a shape. If the only honest comment is "great post", the verdict was OPTIONAL and the right move is a like.

---

## Step 3: Write It

**Length**
- 15 to 50 words. Two to four sentences. One idea.
- Under about 10 words it reads like pod filler and nobody sees it.
- Over about 60 words he is writing a post in someone else's comment section. If the thought is that big, it is his own post. Say so in one line and hand it to `skills/content/linkedin-long-form.md`.

**Register**
- Full sentences, proper capitalization, contractions are fine. No lowercase-casual X texture here, no "bro", no "broski", no "haha".
- Peer to peer with the author, never lecturing, never teaching the room.
- Plain speech. If a line sounds like a caption written to impress, rewrite it as the thing he would actually say.
- Mild profanity, which is a real part of his voice on X, stays out of LinkedIn comments. [CALIBRATE: confirm with Mauro, he may want one per week on a post that earns it.]

**Hard bans (from `brand/voice.md`, they apply double in a comment)**
- No em dashes.
- No "it's not X, it's Y" or any theatrical reframe.
- No "most people" or "most agencies" openers.
- No colon-then-payoff, no three-part parallel stacks, no "here's the thing".
- No wise-narrator tone, no "let that sink in".
- No problem-to-purpose reversal ("that's the filter doing its job").
- No emojis, no hashtags, no tagging people in to farm a reply, no link drop, no CTA, no sign-off.

**Proof rules**
- Only what is in `brand/claims.md`. He runs the AI content and inbound engine for a B2B agency, he ties content to booked calls, he runs a weekly acquisition analysis. The $300k/mo, the $28k deal and the 150 booked calls all need his sign-off before they appear in public copy.
- Never name the client or the agency.
- Never invent a number to sound credible. Bracket it or leave it out.
- Never claim a tool he does not run. Claude Code, Miro, Notion, LeadShark and Calendly are in the repo. Python is not, and that correction is already logged.

**Saturation check.** Before drafting, check whether this point was already made in another comment this session. His most repeated angles: distribution beats the build, content books calls not vanity reach, small and specific beats big audience, taste is the edge, it is an input problem not the model, evals are the piece people skip. Firing the same angle into five comment sections in one morning reads as a script. If the post only allows a repeat, SKIP it unless there is a fresh angle.

---

## Output Format

Verdict on line one. No preamble, no restating the post.

**SKIP is one line, that is the whole answer:**

```
SKIP — [reason in under 12 words]
```

**OPTIONAL:**

```
OPTIONAL — [reason in under 12 words]

1. "[comment]"
2. "[comment]"

→ [which one, under 10 words]
```

**COMMENT:**

```
COMMENT — [reason in under 12 words]

1. "[comment]"
2. "[comment]"

→ [which one, under 10 words]
```

Two options is usually right, three is the ceiling. Shape labels stay internal unless he asks.

Anything else (roster changes, notes on their writing, a content idea the post sparked) goes in one short line **after** the pick, never before the verdict.

---

## The Comment Bank

[CALIBRATE: this starts empty of real anchors. Mauro has a measured reply bank on X and nothing yet on LinkedIn. Log every comment he actually posts here, with the author and what came back, and the drafts start matching him instead of approximating him.]

| Date | Author | His comment | What came back |
|---|---|---|---|
| | | | |

Until there are real anchors, draft against the X converted-reply pattern translated up a register: answer with his own operating reality, in one or two sentences, with the specific thing he runs named.

---

## Anti-Patterns

- **Commenting on everything.** The SKIP is half the value.
- **"Great post, Vasilije!"** Pod filler. It costs him more credibility than it buys reach.
- **Writing a mini-post in their comments.** Over 60 words belongs on his own feed.
- **Correcting the author in public to look smart.** Friction is good, point scoring is not.
- **Selling.** No DM pitch, no lead magnet, no link. The comment earns the profile click, the profile does the selling.
- **Lowercase X texture on LinkedIn.** Reads as careless in this room.
- **Spraying one comment across every account on the list in one morning.** Pick 4 to 6, go deep, come back tomorrow.
- **Commenting on a three-day-old post.** The room has left.
- **Burying the verdict under analysis.** He is working a list.

---

## Cross-Reference

- **The roster and the lookalike test**: `brand/analytics/linkedin-target-list.md`
- **Phone version of this skill**: `skills/content/linkedin-comments-prompt.md`
- **Voice rules and AI tells**: `brand/voice.md`
- **Allowed numbers and facts**: `brand/claims.md`
- **When the comment is too big and wants to be a post**: `skills/content/linkedin-long-form.md`
- **When a thread turns into a real conversation worth taking to DMs**: `skills/dm-setting/`
- **The same job on X**: `skills/content/x-reply-assistant.md`
