# Worked Example

**A complete magnet, built from these exact pages by someone who had never built one, working alone.**

No calls, no questions, no shortcuts. He read pages 00 to 05, filled in his brand context, and produced everything below. It took him a few hours. His second would take about fifteen minutes.

**Read this before you build.** Not for the topic, for the shape. Notice how long each page is, where the fill-in page sits, what the image prompts actually say, and how the post bullets name deliverables rather than topics. Copy the shape, not the content.

The magnet is a prompt swipe file, the subtype page 04 tells you to start with. Source material was a single video transcript.

---

# MAGNET (worked example): 10 Prompts That Turn One Video Into a Week of Content

> **What this file is.** The full magnet, built page by page, exactly as it should land in Notion. This is the QA run's finished asset (product page 4, the worked example) and the paste source for the live Notion build. Built by "Juan" from the docs alone. Every decision and every gap is logged in [lead-magnet-build-log.md](lead-magnet-build-log.md).
>
> **Subtype:** prompt-swipe-file · **DM noun:** file · **Keyword:** ENGINE
> **Structure followed:** `notion-delivery-build.md` (5 fixed subpages) as the canonical build, with the subtype's 10 grouped prompts living inside Subpage 2.
> **Source material:** `research/transcripts/maurojpelle/youtube-first-content-system-with-ai.md`

---

## Title options (3, per subtype rule — pick one before shipping)

1. **10 Prompts That Turn One Video Into a Week of Content** ← recommended (number-led, names the object; matches the shareable doc's own "10 Prompts for X" winning pattern)
2. Claude YouTube-to-Content System for Agency Inbound
3. The Claude Content Engine: One Video, a Week of Posts

**Recommended shipped title:** Option 1.

**Subtitle:** 10 prompts I use to turn one YouTube video into a week of LinkedIn and X posts, from the engine I run daily for a real B2B agency.

**Keyword:** ENGINE (6 chars, ALL CAPS, topic-related)

---

# PARENT PAGE

**Cover:** solid brand-color block. Brand color picked for this run: **`#5B4BE1`** (electric indigo). [GUESS — no brand color exists yet; flagged in build log. Reuse this hex on every magnet if kept.]

**Authority line (very top, before intro):**
> Built by Mauro, who runs this exact content engine daily for a real B2B agency.

**Title:** 10 Prompts That Turn One Video Into a Week of Content

**Subtitle:** 10 prompts I use to turn one YouTube video into a week of LinkedIn and X posts, from the engine I run daily for a real B2B agency.

**Intro paragraph:**
You already make good video. The problem is it stops there, and the rest of the week is a blank page. These 10 prompts take one video transcript and pull a full week of LinkedIn and X posts out of it, in your voice, ready to schedule. Start on the page called "Start Here," do the two-minute setup once, then run the prompts in order.

**Then: 5 nested child subpages (below).**

**Bottom of parent page:**
> Want this installed in your agency? Book a call: `{{calendly_url}}`
> [BLOCKER — no booking link exists yet. Do not invent one. Ship with the DM reply-offer instead until the link exists.]
>
> Created by @maurojpelle

> **PAGE IMAGE PROMPT (16:9, real example screenshot):** A tight, retina screenshot of THIS finished Notion parent page: brand-indigo cover, the title "10 Prompts That Turn One Video Into a Week of Content," the one-line intro, and the visible list of the 5 nested subpages beneath it. No browser chrome, no sidebar, no cursor, no comment bubbles, no Share button. Title legible at feed-thumbnail size. This doubles as the post's cover image.
> **HTML STYLE PROMPT (Claude):** Render this parent page as a single dark-background (#0B0B12) hero block, 1600x900. Indigo (#5B4BE1) top band 120px tall. Title in large white sans-serif (Inter, 64px, bold). Subtitle below in 28px at 80% white. Under it, a vertical list of the 5 subpage names each as a white rounded pill with a small page glyph on the left. Credit line "Created by @maurojpelle" bottom-left in 20px 60% white. No other decoration.

---

# SUBPAGE 1 — "Start Here: How to Use"

**Run this once, then never again.**

**Setup (2 minutes):**

1. Open Claude and create a new Project called "Content Engine."
2. Add two files to the project's knowledge:
   - Your **voice document** (how you actually write; if you don't have one, paste 5-10 of your own posts you're happy with).
   - Your **positioning** (who you help, the outcome you sell, the belief you argue with). Three lines is enough.
3. That's the setup. The project now writes as you, for your audience, every time, so you never re-explain yourself in a prompt again.

**How to run it each week:**

1. Grab the transcript of your latest video (YouTube auto-captions, a Fireflies/Otter export, or paste the raw upload).
2. Open the "Content Engine" project and run the 10 prompts on the next page in order, top to bottom.
3. Prompts 1-4 turn the video into raw material and a shortlist of angles. Prompts 5-8 write the posts. Prompts 9-10 clean them and lay them across the week.
4. Total time once the transcript is in hand: about 15 minutes of running prompts, plus your own read-through.

**The one rule:** run them in order. Each prompt feeds the next. Skipping to "write the posts" without the extract and angle steps is how you get generic output.

> **PAGE IMAGE PROMPT (16:9, doodle scene):** A simple two-color line doodle (indigo on off-white) of a single film reel on the left with five arrows fanning out to five small document icons on the right, each doc labeled with a tiny platform mark (in, X). One source, many outputs. No text sentences, just the labels. Adds the "trickle-down" mental model the page describes without restating the steps.
> **HTML STYLE PROMPT (Claude):** Render the setup as a 3-step vertical checklist card, 1200px wide, white card on transparent bg, each step a numbered indigo circle + bold label + one grey sub-line. Below it a thin divider and the weekly-run steps as a lighter 4-item list. Inter font. Nothing else.

---

# SUBPAGE 2 — "The Asset (copy this)"

> All 10 prompts. Copy the whole block into your "Content Engine" project and run them top to bottom. Tokens in `[BRACKETS]` are the only things you fill in; everything else is paste-ready.
> **Structure note (for the builder, delete before shipping):** the subtype spec groups these into 5 named pairs with a worked example per pair. `notion-delivery-build.md` puts them all in one code block on this single page instead. This build follows the delivery prompt and keeps the group labels as headers inside the block. See build-log gap #1.

```
=== SETUP ONCE (do this before Prompt 1) ===
In your "Content Engine" Claude Project, confirm your voice document and
positioning are attached as project knowledge. Then paste your video
transcript into the chat and say: "This is the transcript for this week's
video. Hold it as the source for everything that follows."


=== GROUP 1: EXTRACT (Prompts 1-2) — get the raw material out ===

PROMPT 1 — Pull the beats
From the transcript, list every distinct idea, claim, or lesson as its own
one-line beat. For each beat include the timestamp and one sentence on why an
agency owner would care. Rank them by how useful they'd be to someone trying
to get clients from content. Give me 8-15 beats. Don't write any posts yet.

PROMPT 2 — Pull the verbatim lines
Now go back through the transcript and pull the 10 most quotable lines in my
own words, exactly as I said them. These are the lines that sound like me, not
like content. Keep the phrasing raw. I'll reuse these so the posts still sound
like a person.


=== GROUP 2: ANGLE (Prompts 3-4) — decide what's worth posting ===

PROMPT 3 — Turn beats into angles
Take the ranked beats and turn the top 8 into post angles aimed at
[YOUR ICP, e.g. established agency owners whose referral pipeline is drying up].
For each angle give me: the beat it comes from, the one-line hook, the platform
it fits best (LinkedIn or X), and the single pain or desire it hits. One line
each. Don't write the posts.

PROMPT 4 — Kill the weak ones (this one tells you no)
Be a hard editor. Of those 8 angles, tell me which 3 you would NOT post and
why: too generic, no proof behind it, already said a hundred times, or the
hook promises nothing the reader receives. Then give me the 5 that survive,
in the order I should publish them across the week. Do not soften this. If an
angle is weak, say so plainly.


=== GROUP 3: LINKEDIN (Prompts 5-6) ===

PROMPT 5 — Write the LinkedIn post
Write a LinkedIn post from angle #[N] using my voice document. Structure:
one-line hook, 2-3 lines of setup with a real proof point from the transcript,
then 3-4 concrete takeaways as short lines, then a soft close. No hashtags. No
em dashes. Use only claims the transcript actually supports; if you need a
number I didn't give, write [NUMBER] and I'll fill it.

PROMPT 6 — Turn it into a carousel/doc outline
Take that same LinkedIn post and give me a 6-slide document outline: slide 1 is
the hook, slides 2-5 are one takeaway each with a 4-6 word headline and one
support line, slide 6 is the close plus a soft CTA. Keep every headline under 7
words. This ships as a LinkedIn PDF/carousel.


=== GROUP 4: X (Prompts 7-8) ===

PROMPT 7 — Write the X thread
Write an X thread from angle #[N]. Tweet 1 is the hook and must earn the click
on its own. Each following tweet is one idea, one line or two, building on the
last. 5-7 tweets. Last tweet is a one-line takeaway, not a CTA. Match my voice
document. No em dashes, no "it's not X it's Y" lines.

PROMPT 8 — Write 5 standalone X posts
Give me 5 standalone X posts (not a thread), each from a different beat in the
list. Each is 1-3 lines, a single sharp idea an agency owner could screenshot.
Vary the openers. At least one should be a direct contrarian take. My voice.


=== GROUP 5: FINISH (Prompts 9-10) ===

PROMPT 9 — De-AI pass (voice check)
Take everything you just wrote and edit it against these tells: em dashes,
"it's not X it's Y" reframes, "most people/most brands" openers, stacked
three-word staccato, and any line I couldn't have said out loud. Rewrite every
line that trips one. Return the cleaned versions only, labeled by platform.

PROMPT 10 — Lay it across the week
Take the final posts and map them to a 5-day schedule (Mon-Fri). For each day
give me: platform, the post, and the best format (text, thread, carousel).
Spread LinkedIn and X so I'm not posting the same shape two days running. Output
as a simple table I can paste into my scheduler.
```

> **PAGE IMAGE PROMPT (16:9, real example screenshot):** A tight screenshot of Prompt 4 ("Kill the weak ones") open in a real Claude chat, showing the prompt on top and Claude's actual reply below it cutting three angles with reasons. Real output only, no fabricated chat. This proves the "prompt that tells you no" does what the page claims. Crop out all browser chrome.
> **HTML STYLE PROMPT (Claude):** Render the 5 group labels as a horizontal 5-step progress bar (Extract, Angle, LinkedIn, X, Finish), indigo filled, white text, 1400px wide, above a note that reads "10 prompts, run top to bottom." Monospace for the group names. Transparent background.

---

# SUBPAGE 3 — "What's Inside"

What you're getting, in one screen:

- **10 paste-ready prompts**, chained in order, that take one video transcript to a full week of posts.
- **A two-minute setup** that makes every prompt write in your voice without re-explaining yourself.
- **Prompt 4 is the editor that tells you no**, so you don't publish the three weak angles you'd have posted anyway.
- **Both platforms covered**: LinkedIn posts and carousels, X threads and standalone posts, from the same source.
- **A de-AI pass** that strips the tells before anything goes out.
- **A finished week**, mapped Monday to Friday, ready to schedule.

The prompts are the asset. Everything else on this page is just the map of them.

> **PAGE IMAGE PROMPT (16:9, worked example):** A filled-in one-week content calendar, Mon-Fri, each day a small card showing platform + post type (LinkedIn post, X thread, carousel, 5 standalone X posts, recap), populated from THIS run's actual output. Shows what "a week of content" looks like when it's done. Real posts from the worked example, not placeholder lorem.
> **HTML STYLE PROMPT (Claude):** Render this as a 6-item checklist, dark card (#0B0B12), each item a white check in an indigo circle + bold white label + one grey line. 1200px. Inter. No header image.

---

# SUBPAGE 4 — "Worked Example"

**Real run of the chain on the source video** (`youtube-first-content-system-with-ai.md`, "Why We're Building the Whole Content System on YouTube First"). Anonymized where needed. This is what the output looks like when you run it.

**Prompt 1 output (beats), top 3 of 12:**
- `0:33` YouTube builds trust faster than a post for high-ticket, because a 12-minute video of you on a topic you know closes $10k deals a single post can't. (why care: trust is the bottleneck on big agency deals)
- `1:07` Focus all effort on one high-quality video and every other platform gets easier, because everything trickles down from it. (why care: solves the "no time for 4 platforms" problem)
- `2:47` Build a skill, test it on real work, keep iterating; the first version is always bad and even a good one has room. (why care: the anti-perfectionism operating rule)

**Prompt 2 output (verbatim lines), 3 of 10:**
- "Trust is much more built through a 12-minute video of you speaking about a topic that you know compared to one article."
- "If you focus on the quality of a YouTube video, you can then easily make quality content in every other place."
- "Stick with the skill and don't be complacent. Sometimes the skill as it starts is pretty shit."

**Prompt 4 output (the editor that says no), abridged:**
> Cut these 3:
> - "AI makes content fast": too generic, every account says it, no proof attached.
> - "We're going to a million a month": a goal, not a received value, reads as a flex.
> - "I've used Claude Code for 3 days": undercuts authority on a trust-led post.
>
> Keep these 5, in this order: (1) trickle-down system, (2) YouTube-builds-trust for high-ticket, (3) the skill-iteration loop, (4) why one source beats four blank pages, (5) the anti-perfectionism rule.

**Prompt 5 output (LinkedIn post from angle #1, trickle-down):**
> I make one video a week. Everything else I post comes out of that one video.
>
> Agency owners tell me they can't keep up with LinkedIn and X and a newsletter and video. The fix isn't more time. It's one source.
>
> I run the content engine for a B2B agency, and the whole thing points at one high-quality video a week. Then it trickles down:
>
> - The video's best 8 ideas become the week's post angles
> - Three get cut by an editor pass before I ever write them
> - The five that survive become LinkedIn posts, X threads, and a carousel
> - A voice pass strips anything that sounds like AI
>
> One recording. A week of content. Fifteen minutes of prompts between them.
>
> If you're posting on four platforms from four blank pages, that's the thing to change this week.

**Prompt 10 output (the mapped week):**

| Day | Platform | Post | Format |
|---|---|---|---|
| Mon | LinkedIn | Trickle-down: one video, a week of content | Text post |
| Tue | X | Trust beats reach for $10k deals (thread) | Thread |
| Wed | LinkedIn | The skill-iteration loop | Carousel (6 slides) |
| Thu | X | 5 standalone takes on the content engine | 5 posts |
| Fri | LinkedIn | Why one source beats four blank pages | Text post |

> **PAGE IMAGE PROMPT (16:9, real example screenshot):** Side-by-side: the raw transcript on the left, the finished Monday LinkedIn post on the right, an arrow between them. Both real, from this run. Proves the transform end to end. No fabricated engagement numbers anywhere in frame.
> **HTML STYLE PROMPT (Claude):** Render the mapped-week table as a clean 5-row schedule, Mon-Fri down the left in indigo, platform as a small pill, post title bold white, format in grey. Dark card, 1400px, Inter. This table is the page's centerpiece.

---

# SUBPAGE 5 — "Want a Free Breakdown?"

You've got the prompts. If you want a second pair of eyes on how you're using them:

Reply **"yes"** to the DM and I'll do a free teardown of your agency's content and inbound setup, where the engine is leaking, and the one change that would move it.

No pitch on the call unless you ask for one. I run this exact engine daily, so it's the part I actually enjoy pulling apart.

> Want this installed for you instead of DIY? Book a call: `{{calendly_url}}` [BLOCKER — pending]

Created by @maurojpelle

> **PAGE IMAGE PROMPT (16:9, doodle scene):** A simple indigo-on-white doodle of two speech bubbles, one small ("yes") and one larger reply bubble with a magnifying glass over a tiny funnel, signaling "free teardown of your setup." Warm and low-key, not salesy. No sentences.
> **HTML STYLE PROMPT (Claude):** Render as a single centered CTA card, dark bg, indigo border, white headline "Want a free breakdown?", one grey support line, and a pill that reads Reply "yes". 1000px. Inter. Minimal.

---

# DELIVERY KIT (goes with the magnet, not inside it)

## X post copy (autodm)

You already make good video. Then the rest of the week is a blank page.

So I built a file of 10 prompts that turns one video into a full week of LinkedIn and X posts, in your voice. It's the exact chain I run on the engine for a B2B agency.

Inside the file:

- The 10 prompts, chained in order, transcript in and a week of posts out
- The prompt that tells you which angles NOT to post
- Both platforms covered: LinkedIn posts, carousels, X threads
- A de-AI pass that strips the tells before anything ships
- A worked example, the whole thing run on one real video

Want a copy? Like + Comment "ENGINE" and I'll send it over ASAP

(Must be following)

## LinkedIn post copy (autodm)

I make one video a week. Every other post I publish comes out of that one video.

Agency owners keep telling me they can't keep up with LinkedIn, X, and video all at once. It isn't an effort problem, it's that they start from four blank pages instead of one source. I run the content engine for a B2B agency, and the whole thing points at one video that trickles down to everything else.

(This is the exact system I run daily, not theory.)

I break down:

✓ The 10 prompts that take one transcript to a week of posts
✓ The editor prompt that kills the 3 weak angles before you write them
✓ How the same source becomes LinkedIn posts, carousels, and X threads
✓ The de-AI pass that strips the tells before anything goes out
✓ A worked example, the whole chain run on one real video

Here's how to get it:

1. Connect with me Mauro Pelle
2. Comment "ENGINE" below

I'll send it over ASAP.

## DM (fires on "ENGINE")

Hey (name), here's the file:

LINK

P.S. Want a free teardown of your agency's content and inbound setup? Reply "yes" and we can chat about how it works.

## LeadShark config

| Setting | Value |
|---|---|
| Trigger keyword | ENGINE |
| DM template | file DM above |
| Auto-connect | OFF |
| Partially Engage | ON |
| Follow-up DM | OFF |

## Cover image

**Default (per spec):** clean retina screenshot of the finished Notion parent page (indigo cover, title, intro, the 5 visible subpage names). Crop tight, no browser chrome. Cannot be produced until the live Notion page exists (see build-log gap on Notion access).

**Fallback designed card (build as HTML, screenshot it):**
- Indigo (#5B4BE1) band header
- Near-black body, white text
- Title: 10 Prompts That Turn One Video Into a Week of Content
- Subtitle: 10 prompts I use to turn one video into a week of LinkedIn and X posts
- Credit: Created by @maurojpelle
- 5-6 star (✷) bullets naming the prompt groups: ✷ Extract ✷ Angle ✷ LinkedIn ✷ X ✷ Finish ✷ Worked example
- Bottom: file icon + "10-prompt-content-engine" + file size (companion file signal)
