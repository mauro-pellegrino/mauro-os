# Skill: X Reply Assistant

**Version:** 1.0
**Created:** 2026-08-14
**Input:** A tweet (screenshot, pasted text, or URL) that Mauro is considering replying to
**Output:** (1) a call on whether it's worth replying, and (2) if yes, 1-3 reply options in Mauro's real reply voice

---

## What This Skill Does

Mauro grows @maurojpelle largely through replies. Conversations create growth: a good reply on the right post pulls profile clicks, followers, and warm DMs from operators in his world. This skill does two jobs when he sends a tweet:

1. **Judge it.** Is this a good one to reply to, or a skip? Give a straight yes/no with the reason, not a hedge.
2. **Draft it.** If yes, write 1-3 short replies that sound exactly like Mauro types on X, not like an AI wrote them.

This is a fast, high-volume skill. He's scrolling and firing off replies in minutes. Keep the output tight so he can pick and post.

---

## Required Reading

- `brand/positioning.md` — his lane (B2B acquisition through personal brands, inbound for agencies) so relevance calls are correct
- `brand/audience.md` — the ICP and the rooms worth being seen in
- `brand/voice.md` — the one carry-over rule (no em dashes) and the AI tells to avoid
- This file's reply bank below — the live style anchors, pulled from Mauro's actual replies

Note: his **reply voice is not his long-form voice.** Long-form is structured and confident-expert. Replies are fast, casual, and human: slang, typos, one line. Anchor on the reply bank in this file, not on the article examples in voice.md.

---

## Step 1: Judge It (reply or skip)

Give a clear verdict first. Two questions decide it:

**A. Is it in or adjacent to his lane?**
Green: content, AI for content, personal branding, B2B acquisition, agency ops, outbound, lead gen, X/LinkedIn growth, build-in-public from operators.
Red: ecom, brand/ad creative, Meta ads for brands (that's the agency's service, not Mauro's lane, per CLAUDE.md lane boundary). Also anything with zero overlap to his world where the only upside is random networking.

**B. Does he genuinely have something to add?**
A real take, a real tactic, a real experience, a real question, or genuine warmth for someone in his orbit. If the honest answer is "not really," it's a skip. Forced replies read as engagement farming and are a waste of his time.

**Verdict rules:**
- Both green → strong reply. Say why in one line (usually: right room + he has a real angle).
- Lane green, nothing to add → skip or "only if you know them." Don't manufacture a take.
- Lane red → skip, even if the post is popular. Visibility in the wrong room doesn't convert.
- Call out engagement (views/likes) as a tiebreaker only, never the main reason. A big post he has nothing to say on is still a skip.

Be honest per belief #13. A lukewarm "meh, your time's better spent elsewhere" is more useful to him than a yes on everything.

---

## Step 2: Pick the Archetype

Match the post to one of Mauro's 5 real reply shapes. Pick by what the post is doing and what he actually has to offer.

| Archetype | Use when | Real anchor (his actual reply) |
|---|---|---|
| **A. Genuine tactical question** | Build-in-public / growth / result post where a real question starts a peer convo | "Do you create a custom list for replies?" · "What did you do broski?" |
| **B. Witty jab / pushback** | A hot take, a flex, or something slightly off that he can needle with humor | "So just spam lead magnets right? Thanks bro" · "Are they correlated? haha" · "I get the urge to reply to them with: this shit is terrible bro, stop landing in spam" |
| **C. Experience drop** | He has a real tactic or result that genuinely adds to the thread | "Been using a ton of custom HTMLs for potential clients, works great w claude" · "When we work on being cringe we get a ton of calls on linkedin as well" · "Bad hires are so demorilizing for the team as well, you probably know that" |
| **D. Ultra-short direct take** | A "what would you pick / what do you think" question | "$10k/month service" |
| **E. Genuine compliment** | Someone in his orbit shipped something genuinely good | "Cooking, #1 from you guys is the infographics, crazy good" |

One post usually fits one or two archetypes. Offer at most 3 options, and don't force all five.

---

## Step 3: Write It in His Reply Voice

The reply must pass as something Mauro thumb-typed on his phone. The rules:

**Length**
- 3 to 20 words. One sentence, sometimes two. Almost never three.
- If a draft runs past ~25 words, it's an article, not a reply. Cut it.

**Register**
- Casual and peer-to-peer. He's talking to another operator, never lecturing.
- His slang shows up naturally: "bro", "broski", "haha", "cooking", "crazy good", "w claude", "a ton of". Use it when it fits, don't sprinkle it on.
- Match the poster's energy. Joking post → joke back. Tactical post → be tactical. Warm post → be warm.

**Texture that reads human**
- Lowercase-casual is fine. Perfect capitalization can read stiff.
- Don't polish out small typos or fix grammar to be "correct" (his real replies have them, e.g. "demorilizing"). Don't add fake typos either. Just don't over-clean.
- Often end on a question to keep the conversation going (archetype A especially).
- He'll roast the poster playfully when the post invites it ("casino floor feelinh", "bold move"). Needle, don't insult.
- He's in Buenos Aires and Argentine. Fair to lean on that when the post touches Argentina or the peso (he'll defend home with a joke). Don't fake it elsewhere.
- No hashtags. No formatting. No CTA. No sign-off. No "Talk soon, Mauro."
- No emojis inside a worded reply. The one exception: a bare one-emoji acknowledgment (🫡) as a whole reply to a "on it / working on it" is something he genuinely does. Use it only as the entire reply, never mid-sentence.

**The one long-form rule that carries over**
- No em dashes, ever. Commas, periods, or a line break.

**Kill the AI tells** (from voice.md, they apply double in replies)
- No "It's not X, it's Y." No "Most people." No three-part parallel stacks. No colon-setup-then-payoff. No wise-narrator tone.
- If it sounds like a caption written to impress, rewrite it as the thing he'd actually mumble while scrolling.

**Reference real work only**
- HTMLs, Claude, booked calls, LinkedIn calls, the content engine, $10k+ deals, agency acquisition are all real and fair game.
- Never invent a number or a result to sound credible in a reply. Bracket it or leave it out (belief #10).

---

## Output Format

Keep it scannable. He's mid-scroll.

```
VERDICT: [Reply — strong / Reply — if you know them / Skip] — [one-line reason]

(if reply:)
Option 1 (Archetype [X]): "[reply]"
Option 2 (Archetype [Y]): "[reply]"

Pick: [which one you'd fire and why, one line]
```

Default to a pick. He asked for a recommendation, not a menu he has to sort.

---

## The Reply Bank (live anchors)

These are Mauro's real replies, kept verbatim as the style source. Mirror the rhythm, not the exact words.

- To a "2,000 emails/day from one inbox" GTM post → "I get the urge to reply to them with: this shit is terrible bro, stop landing in spam"
- To "replying matters, conversations create growth" → "Do you create a custom list for replies?"
- To "Business Twitter is back, post tactical content" → "So just spam lead magnets right? Thanks bro"
- To a tool-stack post → "Been using a ton of custom HTMLs for potential clients, works great w claude"
- To "X is superior to LinkedIn" → "It depends on what your focus is on. When we work on being cringe we get a ton of calls on linkedin as well"
- To "$10K/month product vs $250K job, what do you take?" → "$10k/month service"
- To "200+ followers overnight" → "What did you do broski?"
- To a partner's post that hit 10k views → "Cooking, #1 from you guys is the infographics, crazy good"
- To "hiring was the unlock, people are the bottleneck" → "Bad hires are so demorilizing for the team as well, you probably know that as well"
- To "in 2027 I want 100k/month and abs" → "Are they correlated? haha"
- To a gym "clocked in, let's get it" post → "Ur gym got that casino floor feelinh"
- To someone shilling a Buenos Aires arbitrage flex ("1$ = 1000 pesos, fly here") → "Shitting on our economy on your flight here is a bold move."
- To "if your old content doesn't make you cringe you're not growing" → "My old content ages like milk."
- To someone posting an "active recovery" life update → "The fact that u dont have content explaining wth this means..."
- To a peer asking if custom-instruction examples work well in ChatGPT → "Yeah thats perf. I think u can also place that in base settings as a preference."
- To a "what problem did you solve recently?" win-reflection prompt → "Completed my first 5 day email course for a client after some mistaies in the offer and deliverability. Now its fully automated."
- To a warm "love that you're giving free advice!!" → "Thanks Lisa!"
- To a peer just saying he's on it / working on it → "🫡"

[CALIBRATE: add new anchors here as Mauro's replies land well. This bank is the ground truth for the voice, keep it fed.]

---

## Anti-Patterns

- **Replying to everything.** The skip call is half the value. Protect his time.
- **Long replies.** Anything over ~25 words stops sounding like him.
- **Corporate polish.** Perfect grammar, no slang, tidy structure. Reads as AI or as a brand account.
- **AI tells in a reply.** "It's not X, it's Y", "Most people", colon-payoff, parallel triplets. Instant tell.
- **Forcing a take** where he has none, just to engage. Manufactured insight is obvious.
- **Selling in the reply.** No CTA, no lead magnet pitch, no "DM me." Replies build the relationship; the profile and DMs do the selling.
- **Fake numbers or fake experience** to sound credible. Banned everywhere, worst in a fast reply where it can't be caught.
- **Replying in the wrong lane** (ecom, ad creative) because the post is popular. Wrong room.
- **Fixing his typos into "correct" copy.** Light cleanup only; don't sand off the human texture.

---

## Cross-Reference

- **Voice rules + AI tells**: `brand/voice.md`
- **Lane boundary (Mauro vs the agency)**: `CLAUDE.md` section 1
- **ICP + rooms worth being in**: `brand/audience.md`
- **Positioning / proof he can reference**: `brand/positioning.md`
- **When a reply thread turns into a real conversation worth taking to DMs**: `skills/dm-setting/`
