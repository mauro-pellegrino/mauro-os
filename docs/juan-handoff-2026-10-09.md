# Juan: handoff for @maurojpelle, 9 Oct 2026

Everything below is approved by Mauro (reviews of 8 and 9 Oct). Paste the text exactly as it is. Do not edit
a word. If something is marked `[NEEDS: x]`, that part is not ready: ask Mauro, do not fill it yourself.

## Your to-do list

1. **Schedule the posts** in the table below, X and LinkedIn, on the dates shown.
   - [NEEDS: posting times. The repo has no time slots for @maurojpelle. Ask Mauro once, then use the same times every day.]
   - Article days (Thu 15 and Thu 22 Oct): publish the article on X first, then post the bare article link as its own post.
   - Hold any item with a `[NEEDS]` on its media until Mauro sends what is missing. The text can be scheduled.
2. **Build the private X List "Reply rooms"** (once, about 20 minutes).
   - x.com > Lists > New List. Name: "Reply rooms". Turn on "Make private". Save. Pin it, sort by Latest.
   - Add every handle in `docs/juan-x-list-handles.txt` above the line `# UNVERIFIED`.
   - The 28 handles under `# UNVERIFIED`: open each profile on x.com first. Add it only if the handle exists,
     it is a real person, and the follower count is 100K to 1M. If one fails, leave it off the List and delete it
     from the file.
   - For each checked handle, write the follower count and the date in `brand/analytics/reply-target-list.md`.
3. **Replies, every day**, per `docs/juan-reply-brief.md`:
   - 15 replies a day, as a maximum. Spread them over 8 or more accounts.
   - Reply within 15 minutes of the post.
   - Reply only to posts in the "Reply rooms" List. Never from "For you".
   - One real point in every reply: a question about their system, or one fact from Mauro's work
     (`brand/claims.md`, rows marked "yes", or his own posts). Never invent a number.
   - No replies to the team (@lorenzo_pravata, @Bogzabs96). A like or a repost is fine.
   - No one-word replies ("fireee", "so true", "nice list").
   - Skip posts about AI models or tools, or about a first client or $1k MRR.
   - End of day: note any new account that looks right. Do not add it to the List. Mauro decides on Monday.
4. **Weekly report, every Friday**, to Mauro:
   - Replies sent per day (target: 15 or fewer) and how many different accounts they went to.
   - New accounts you noted for Mauro to decide on.
   - The UNVERIFIED check: which handles you added (with count), which you removed and why.
   - Posts: what went out on X and LinkedIn, with links, and anything that did not go out and why.
   - Every `[NEEDS]` still open.

   Mauro reads the numbers (profile visits and follows per reply) himself on Monday from the X export. You do not need to pull them.

## Schedule

| Date | Platform | Post | Media |
|---|---|---|---|
| Mon 12 Oct | X | X1 ascii diagrams that draw themselves | [NEEDS: a demo animation that is not the process map] |
| Tue 13 Oct | X | X2 what a backlog file does | [NEEDS: screenshot of the AT A GLANCE table in `BACKLOG.md`] |
| Wed 14 Oct | X | X3 /sod | none |
| Wed 14 Oct | LinkedIn | PM-LI process map, LinkedIn version | `tools/ascii-anim/examples/process-map-one-process-cream-1600x900.mp4` |
| Thu 15 Oct | X | Article 1 + bare link post | cover: [NEEDS: Article 1 cover] |
| Fri 16 Oct | X | PM-X process map long form | `tools/ascii-anim/examples/process-map-one-process-cream-1080x1080.mp4` |
| Fri 16 Oct | LinkedIn | LI2 option A, the whole content system | none |
| Sat 17 Oct | X | CA operator confession A, the review loop | none (self-reply: [NEEDS]) |
| Mon 19 Oct | X | X6 the monday diary | [NEEDS: Mauro confirms, see X6] |
| Tue 20 Oct | X | X7 the outlier rule | none |
| Tue 20 Oct | LinkedIn | LI3 mapping one content process | none |
| Wed 21 Oct | X | X8 templates live in a doc | `content/ascii/outlier-01-intake.png` |
| Thu 22 Oct | X | Article 2 + bare link post | cover: [NEEDS: Article 2 cover] |
| Thu 22 Oct | X | X9 the batch rule | none |
| Fri 23 Oct | X | X10 the claims file | none |
| spare, no date | LinkedIn | LI2 option B, the personal version | none |

Totals: X 12 slots (10 posts and 2 article drops). LinkedIn 3 posts, plus 1 spare.

**Do not post these**, even if you find them in the repo: LI1 (on hold), LI4 (killed), X4 (not cleared for this
handoff), X5 (replaced by PM-X on Fri 16 Oct, same diagram), operator confession B (killed), the loop animation (killed).

---

## X posts

### X1 · Mon 12 Oct · X

Media: [NEEDS: a demo animation that is not the process map. The process-map video runs once, on Fri 16 Oct with PM-X. Mauro picks or renders another diagram with `tools/ascii-anim/`.]

```text
I had claude build me a tool that makes my ascii diagrams draw themselves:

- the text types in with a cursor
- the box borders sweep in row by row
- small packets flow along every arrow
- the one box that matters pulses at the end

The tool turns the diagram into a web page, records it frame by frame in headless chrome and stitches the frames into an mp4, so it costs nothing and a 14 second video renders in about 30 seconds.
```

### X2 · Tue 13 Oct · X

Media: [NEEDS: screenshot of the AT A GLANCE table at the top of `BACKLOG.md` (the 5-column count table). It does not exist as an image yet. Juan: open `BACKLOG.md` in a Markdown preview and screenshot only that table.]

```text
Every repo I run in claude code has a BACKLOG.md, one file with everything that's still open on it:

- claude reads it at the start of every session, so I never re-explain where things stand
- every item is open, in progress, done or blocked
- a blocked item names who or what unblocks it
- nothing closes itself, every tick is a judgement call

Without that file every new session starts from zero, and claude only knows what I remember to tell it.
```

### X3 · Wed 14 Oct · X

Media: none.

```text
/sod is the first thing I run in the morning:

- reads the backlog and the fixed work for that weekday
- picks one rock, something I can finish alone in one sitting
- writes the calendar blocks, each named after what it ships
- caps admin and buffer at one 45 minute block

If finishing it depends on someone replying, it goes back in the backlog as a blocked row with their name on it.
```

### Article 1 · Thu 15 Oct · X

See the Articles section below. Publish the article, then post its link alone as a separate post.

### PM-X · Fri 16 Oct · X · process map long form

Media: `tools/ascii-anim/examples/process-map-one-process-cream-1080x1080.mp4`

```text
This is every step of one content process I run with claude, the linkedin lead magnet:

- find a proven post, mostly 300+ comments

- capture it, copy the text, screenshot the comment or the reply, paste the image into claude

- claude checks what we already built

- claude matches it to one of our resources, or builds a new one

- claude writes the post

- claude writes the auto dm

- claude makes the image

- claude builds the staging page

- I read the draft and it goes live

6 of the 9 steps are claude in one block, and the 3 that need a person sit outside it.

One run measured on the clock took 24 minutes from pasted post to live page.

The 24 minutes only holds because the resource behind the post already existed, and a run that has to build a new one hasn't been timed yet.
```

### CA · Sat 17 Oct · X · operator confession A

Media: none. Keep the lowercase and the "..." exactly as written.

Self-reply plug: [NEEDS: the free thing the self-reply points to. Post the main text without a self-reply until Mauro sends it.]

```text
i don't write a single first draft anymore...

i never even open notion to review
i'm not editing drafts line by line
i'm not even watching the agents while they write

all i care about is whether the draft gets approved the first time

so my whole day starts with one review page in the morning

every post, article and cover on one screen. approve, change or kill, and one line of why on every kill

then my only job is making sure each agent has:

- the reason behind every kill, saved as a rule
- a swipe file of posts that actually performed
- a source for every number it writes

after that i just wait for the next batch and kill less of it than last time

i've accepted that i'm the slowest part of the system... next to a stack of terminals running Opus 5.5

you should do the same
```

### X6 · Mon 19 Oct · X

[NEEDS: Mauro confirms before Mon 19 Oct that the first Monday diary ran on 12 Oct. If it did not, this post moves to a later week. Do not schedule it until he says yes.]

Media: [NEEDS: screenshot of the week calendar. It is on Mauro's machine, and it shows hours per project, which do not go public. Mauro sends a version without the hours, or the post goes out text only.]

```text
Every monday my week opens with a diary, and claude writes first:

- dumps the week from my session logs, hours per repo
- adds the git log and both backlogs
- then I answer the diary questions
- then I pick 4 wins for the week

Claude goes first because every log I had to start myself died within 2 days.
```

### X7 · Tue 20 Oct · X

Media: none.

```text
When I save someone's post as a template I score it against their own account, never mine:

- their number divided by the median of their last 10 to 20 posts
- 3x is an outlier, 10x is strong
- under 50k impressions on x or 300 comments on linkedin it doesn't become a template

A 20k post is an outlier on a 4k account and a normal day on a 30k one.
```

### X8 · Wed 21 Oct · X

Media: `content/ascii/outlier-01-intake.png`

```text
Every template I run lives in one doc, never inside a claude skill:

- the skill says how a process runs
- the doc holds the shapes it can run
- each template has the shape, the rules and the original with its numbers
- every rule has to point at a line in the original
- each one routes to the process that already runs that post type

That way I add or retire a template without touching a skill.
```

### Article 2 · Thu 22 Oct · X

See the Articles section below. Publish the article, then post its link alone as a separate post.

### X9 · Thu 22 Oct · X

Media: none.

```text
When claude drafts 4 articles for the week, no two can share:

- a structure
- a title shape
- a cover

4 articles in one style is all your eggs in one basket, same as testing 4 ads with one hook, if that look doesn't land all 4 flop and you learn nothing about what to change.
```

### X10 · Fri 23 Oct · X

Media: none.

```text
Before any number goes in one of my posts, a view count, how long a process takes, a result, it needs a row in one claims file:

- the number, worded the way it can be said
- the file it came from
- whether it can go public

A second model checks every draft against that file before I read it, so a number with no row never reaches me.
```

---

## LinkedIn posts

### PM-LI · Wed 14 Oct · LinkedIn · process map

Media: `tools/ascii-anim/examples/process-map-one-process-cream-1600x900.mp4`. No CTA in the copy.

```text
I mapped one content process I run with claude, the linkedin lead magnet, and 6 of its 9 steps need no person at all.

The 3 steps a person does:

- find a proven post, mostly 300+ comments
- capture it, the text, a screenshot of the comment or the reply, and the image pasted into claude
- read the draft before it goes live

The 6 steps claude runs in a row:

- checks what we already built
- matches the post to one of our resources, or builds a new one
- writes the post
- writes the auto dm
- makes the image
- builds the staging page

One run took 24 minutes from pasted post to live page, measured on the clock. That time only holds because the resource behind the post already existed, and a run that has to build a new one hasn't been timed yet.

If you run lead magnets for your agency, map yours the same way and mark who does each step, because the steps marked with a person are the only ones that still need your time.
```

### LI2 option A · Fri 16 Oct · LinkedIn

Media: none.

```text
Every post, article and lead magnet on the accounts I run content for goes through one system in claude code, and none of it starts from a blank page.

Here's what the system does:

- every monday it pulls the x and linkedin exports, tags each post by pillar, angle and format, and matches the posts against the calls booked that week
- it tells me which angles to run more of, so next week's topics come from the posts that lined up with booked calls
- it scores the best posts from other accounts against each account's own average and saves the outliers as templates
- claude drafts from those templates and from our real work
- a second model checks every number in a draft against one claims file before I read anything
- every draft I reject gets a written reason, and that reason becomes a rule claude reads before the next batch

The monday part took me a few weekends to build.

If you run an agency, build the monday part first, because matching every post to the calls booked that week is what tells you which content to make more of.
```

### LI3 · Tue 20 Oct · LinkedIn

Media: none.

```text
How I map a content process so I can see where my time actually goes:

1. Pick one process that ships one thing on its own. Mine was the linkedin lead magnet.

2. Write every step in order, from opening the profile to the post going live.

3. Mark each step claude or me. When claude does several steps in a row, group them into one block on the side, so the human steps stand out.

4. Add a short note next to each box with what the step really involves. "Capture it" means copy the text, screenshot the comment and paste the image into claude.

5. Time one full run on the clock. Mine came out at 24 minutes, from pasted post to live page.

6. Write down what the time depends on. The 24 minutes only held because the resource behind the post already existed.

7. Leave every step you haven't timed as a question mark until it runs on the clock.
```

### LI2 option B · spare, no date · LinkedIn

Approved as a spare. Use it only when Mauro gives it a day.

```text
Every new claude session used to start from zero, and claude only knew what I remembered to tell it.

So I built the content system around files claude reads before it does anything:

- a backlog with everything still open, so I never re-explain where things stand
- a file per person, built from them talking for 10 minutes, so each account sounds like the person behind it
- a templates doc with the posts that outperformed on other accounts, scored against their own average
- one claims file, so every number in a draft has a source before I read it
- a rules file that grows every time I reject a draft and write down why

On top of that, every monday it matches the week's posts against the calls booked that week and tells me which angles to run more of.

If you run an agency, move everything you keep re-explaining to claude into files it reads first, so every session starts where the last one stopped.
```

---

## Articles (X)

Body source for both: `content/drafts/2026-10-w42-w43-posts.md`, sections "Article 1" and "Article 2". The full
text is also below. The `###` lines are section headings: set them as headings in the X article editor.

### Article 1 · Thu 15 Oct

- **Title:** How to build a claude content system that gets better with every batch
  (option 5, approved 9 Oct. The drafts file also lists title 1: do not use it.)
- **Cover:** [NEEDS: Article 1 cover. Not built. Spec: 5:2 terminal cover with one review card in the middle (post text, APPROVE / CHANGE / KILL, a why box) and a two-row first-pass line under it (26%, 46%).]
- **Body:**

```text
Every claude skill and agent I run for content kept making mistakes I had already corrected, because every correction I gave lived in a chat that no later session could read.

On 8 October I put every draft claude wrote for the accounts I run content for on one page, and approved 10 of the 39 cards as they were.

So I built a loop into the whole system, where every rejection gets written down once and becomes a rule the skills and agents read before the next batch. It covers everything claude makes for me, posts, articles, covers and lead magnets, and this is how it runs, step by step.

### 1. Put every draft on one page

Every draft claude makes now lands on one local page, whatever it is, posts, articles, covers or lead magnets. Each card has:

- the text, image or video, exactly as it would go out
- the source it was written from
- one line on top that says what I need to decide

The page lives outside my content repo, because it mixes drafts for more than one account.

### 2. Three buttons and a box

Every card has approve, change or kill, and a box for why.

A change with no reason teaches claude nothing. So when I press change and leave the box empty, the next round shows me options for that card (title, cover or body) instead of a guess.

### 3. Paste every decision back at once

When I'm done, one button copies every decision as plain text and I paste it into claude code. It gets saved word for word with the date before anything else happens.

New drafts never go on the page while a round is open. The clicks are saved against the cards that are on the page, so a rebuild with new cards would hide them on reload. New drafts wait in a separate folder until my decisions are in.

### 4. Turn every reason into a rule

This is the step that makes the next batch better. Each change or kill reason gets written into the file that produced the draft, either the skill that wrote it or the checks a second model runs before I see anything, with the review date and the card number as its source.

Three that came out of the second round:

- a post got killed for having nothing in it for the reader, so every post now has to give the reader something they can copy
- a post with a number and no context got "number about what?", so every number now has to say what it measures, on the same line or the one before
- I flagged weak last lines on two posts, so the last line now has to state the concrete reason in plain words

### 5. Track one number per content type

The number is first-pass approval, the share of drafts I approve on the first read without changing a word. It gets logged after every round, per content type (posts, articles, covers, titles), so I can see which skill is still guessing.

### What two rounds showed

First round 26% (10 of 39 cards), second round 46% (32 of 69).

Two rounds isn't a trend, the second round reviewed one post per card where the first bundled them, and the rules in step 4 came out of the second round, so the third round is the first one they get tested on.

If you review AI content for your agency and only copy one part of this, copy the why box, and put what you write in it somewhere the AI reads before its next draft.
```

### Article 2 · Thu 22 Oct

- **Title:** The principles of running content out of claude code
- **Cover:** [NEEDS: Article 2 cover. Not built. Spec: 5:2 terminal cover with a score table in the middle (outlier verdict column), a different layout from Article 1.]
- **Body:**

```text
Every post format I run started as someone else's outlier. These are the five rules that decide which ones I copy, where they live, and how they get used without everything starting to sound the same.

Each one is written down in a file Claude reads, so it applies the same way on a Tuesday as it does on the day I wrote it.

### 1. Score a post against its own account

A big number on a big account can be a normal day for that account. So a post only counts as an outlier against its own account's median.

- take the newest 10 to 20 posts from the account
- divide the post's number by their median
- 3x is an outlier, 10x is strong
- the number is impressions on x and comments on linkedin
- fewer than 5 posts means there's no median, so no verdict

Then a floor on top: under 50k impressions on x or 300 comments on linkedin, it doesn't become a template, whatever the ratio.

I ran my own account through it. My best post of September did 20x my median and still came out under the floor. A ratio on a small account tells you about that account.

### 2. Capture everything in one batch

For each outlier, four things go to Claude:

- the post text, copied, never retyped
- a screenshot with its image, and for an x article, shot from the feed so the title, cover and first lines are in one frame
- the link
- the numbers, checked exact on the post

They go over together, never one at a time. The link and the number are the two I never skip, because without them the post can't be scored again later.

### 3. Templates live in a doc, never inside a skill

A skill says how a process runs. The templates doc holds the shapes it can run. Keeping them apart means I can add or retire a template without editing a skill.

Each template has the same record: the shape line by line, the rules, the process it routes to, a status, and the original with its numbers. Every rule has to point at a line in the original. If Claude can't quote the line, the rule goes.

Before a new template gets saved, Claude checks whether the shape already exists. If it does, the post becomes another example under the old one.

### 4. No two articles in a batch look alike

When Claude drafts 4 articles for the week, no two can share a structure, a title shape or a cover. Two "5 steps" titles landed in one batch once, and that was enough.

So before a word gets written, Claude lists the 4 structures, the 4 title shapes and the 4 covers side by side, and redraws any repeat. The subjects and openers that already worked stay the same. Only the shape changes.

This article and last week's are the rule in action: one was a step-by-step build, this one is a set of principles, and the covers use different diagrams.

### 5. Every number needs a row before it can be posted

There's one claims file. Each row is a claim worded the way it can be said, where it came from, and whether it can go public.

When a draft is done, a second model checks every number and named fact in it against that file. Anything without a row fails, even if the number is real, and a real number from the wrong account fails too.

That check runs before I read the draft, so my reading time goes on the writing.

### How the five fit together

Rule 1 decides what's worth copying. Rule 2 makes the capture reusable. Rule 3 keeps the shapes in one place. Rule 4 stops the shapes from piling up into one look. Rule 5 keeps the numbers inside them honest.

If you build one of these first, build the score. Everything after it depends on copying the right posts.
```
