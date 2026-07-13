# YouTube Title Generator
**Version 2.2 | Updated 30 March 2026**

Generates YouTube titles for Lorenzo's channel in 3 steps: extract the mechanism from outlier titles, map it to the video topic, rebuild it with Growthub's unique angle. Every title serves two permanent goals (see below) — reach and conversion.

---

## Required Reading

Before producing any written output, read `brands/growthub/voice.md` and `brands/growthub/audience.md` in full. All copy must pass the 60-second pre-publish checklist at the bottom of voice.md. Ground every audience-facing decision (tier, stated pain, language) in the v2.1 ICP in audience.md.

---

## Step 0 — Surface What's Already Known

Before generating any titles, surface all existing title references, competitor examples, and approved directions already on file for this topic. Output first, then ask for additional context.

### 1. Search existing research and skill files

```bash
grep -rli "[topic keyword]" /Users/mauro/growthub-os/research/
grep -ni "[topic keyword]" /Users/mauro/growthub-os/skills/youtube-title-generator.md
```

Extract from matches:
- Any competitor titles on this topic already saved in the Reference Table or research files
- Any approved directions already listed in this skill for this topic
- Any outlier titles from the weekly brief that overlap with the topic

### 2. Output a title knowledge summary

```
WHAT'S ALREADY ON FILE: [TOPIC] TITLES
----------------------------------------
Competitor titles found:
- "[title]" — Mechanism: [mechanism name]

Approved directions already listed:
- "[title]" — Why it works: [note]

Outlier titles from weekly brief:
- "[title]" — Channel: [channel name]

Mechanisms most applicable to this topic:
- [Mechanism name] — because [reason]
```

### 3. Request additional context

After the summary, ask:

> "That's what's already on file for this topic. Anything to add before I generate titles? For example: a specific client result to anchor on, a number to use, or a title direction Lorenzo already has in mind."

Wait for the response before generating titles.

---

## When to Run This Skill

- A video idea has been chosen and needs a title
- Someone asks "give me titles for this video"
- Running the weekly research brief and need to convert outlier titles into Lorenzo versions

---

## Two Permanent Goals

Every title must serve both of these simultaneously. They are not optional and do not change video to video.

**Goal 1 — Qualified views**
Attract founders spending £30k–£100k/month on Meta who are hitting a ceiling. These are people who already run ads, already have a brand, and are stuck at a level they cannot break past. A title that pulls in beginners but not this group is a failure. A title that pulls in this group at scale is a win.

**Goal 2 — Audience conversion**
Move the existing audience toward booking a call. Every video Lorenzo makes is also a sales asset. Titles that signal depth, proof, and in-house experience build the trust that eventually turns viewers into booked calls.

When evaluating any title, ask: does this make a £50k/month Meta spender stop scrolling? If yes, it passes. If it reads as beginner content or generic advice, it fails.

---

## Title Philosophy (from Lorenzo)

These four principles override any other instinct when writing titles.

**1. Reach over voice**
Titles should aim for maximum audience reach, not necessarily reflect Lorenzo's personal speaking style. If a format (lowercase, casual, list-style) reaches more of the right people, use it — even if it doesn't feel 100% like Lorenzo's voice in conversation. The video earns the voice. The title earns the click.

**2. Validate against a competitor outlier**
Before finalising a title, find the closest competitor title that outperformed its channel average on the same topic. Extract the mechanism. Adapt it. Do not write in a vacuum.

**3. Add the Growthub sauce**
The mechanism is borrowed. What makes it Growthub's is the angle that only Growthub can credibly claim:
- In-house data: "$106M in managed spend", "$1M+ on street interview ads"
- Formats nobody else teaches: podcast-style ads, street interviews, documentary creative
- Real client results (with placeholders where unconfirmed — see below)
- The stealth creative principle: ads that don't look like ads

A competitor can use "How to write hooks." Lorenzo's version is "How to write hooks with a 45% hook rate" — the specific number is the sauce.

**4. Use placeholders when client numbers aren't confirmed**
Never invent a specific number. If the case study result hasn't been confirmed, use a placeholder:
- `$XM/year` or `£Xk/month` (not `$1.2M/year`)
- `£Xk/day to £Xk/day` for before/after contrast
- `The 3 ads that generated $[X] for our client`

Placeholders should be swapped for real numbers before the video goes live. If no real number is available, switch to a mechanism that doesn't require one.

---

## Inputs Required

1. **The video topic / angle** — one sentence describing what the video covers
2. **The weekly research brief** — the outlier titles to analyse (from `skills/weekly-research.md` output)
3. **Growthub credentials** — specific numbers available to use (see below)

---

## Growthub Credential Numbers

Use these in titles whenever a number claim is made. Never invent numbers.

| Credential | Number |
|---|---|
| Total managed Meta spend (last 12 months) | $106M |
| Mid-range anchor (last 6 months) | $63M |
| Brands worked with | 100+ |
| Studio | Own studio (in-house production) |
| Street interview ads spend | +$1M |
| Specific client results | pull from `brands/growthub/learnings.md` or brief what the video covers |

Use `$106M` as the primary credential. Use `$63M` as the recency anchor when framing current results. Never use the old $106M or $46M figures — those are outdated.

If the video is a client case study, the client's actual result is the number. Use it exactly — odd specificity ($1.81M) outperforms round numbers ($2M).

---

## Step 1 — Extract the Mechanism from Outlier Titles

Before writing any title, analyse the outlier titles from the weekly brief. For each one, identify which tension mechanism makes it work. There are 8 mechanisms.

### The 8 Mechanisms

**1. Number Contrast**
Two numbers set against each other. The gap between them is the entire hook. No explanation needed.
- *$3k/day VS $87k/day | The Creative Gap Exposed*
- *From $2k/Day to $160k/Day in 30 Days*
- Works for: before/after case studies, creative testing results, scaling breakdowns

**2. Oddly Specific Proof**
A non-round number signals real data, not a made-up claim. Specificity does the credibility work.
- *$264,590 per day on Shopify | Full Creative Strategy*
- *$827,869 in 4 days on Shopify*
- Works for: case studies, spend breakdowns, results videos. Fails for: conceptual/educational videos with no hard number.

**3. Credential Anchor**
Total scale or spend leads the title. The number establishes who Lorenzo is before the viewer reads the rest.
- *My $106M Meta Ads Strategy (step by step)*
- *My $100M Meta Ads Creative Strategy*
- Works for: strategy overviews, methodology videos, anything where Lorenzo's experience is the draw. Fails for: client-specific case studies (use their number, not the credential).

**4. Belief-Breaker**
The title contradicts something the viewer currently believes. Creates mild friction — they either agree and click, or disagree and click.
- *Why Your "Bad" Ads Get Spend on Facebook*
- *No One Will Buy Your Brand*
- *Why you aren't scaling*
- Works for: ICP belief-breaking videos, contrarian takes, mechanism explainers. Fails for: tutorials or case studies where the mechanism is the draw.

**5. Named Format or Mechanism**
The specific technique or format is the subject. Viewer clicks to learn the named thing before competitors do.
- *Unaware Ads: How to Legally Print Money in eCom*
- *8 Figure B Roll Creative Strategy*
- *Street Interview Ads*
- Works for: format tutorials, creative strategy explainers, named frameworks. Fails for: general "how to run ads" content where there's no named concept.

**6. Platform / Technical Problem**
Names the specific technical problem the viewer is experiencing. Viewer recognises their situation.
- *Why Your Ads Are Invisible For Meta (Andromeda Update)*
- *How to fix Meta Ads roller coaster performance*
- Works for: timely algorithm/platform content, troubleshooting videos. Fails for: evergreen strategy content.

**7. Speed Compression**
A time frame that makes the result feel achievable. Compresses the timeline to create urgency.
- *$827,869 in 4 days*
- *From $2k/Day to $160k/Day in 30 Days*
- *How to Find a Facebook Ads Post ID In 90 Seconds*
- Works for: case studies with a clear timeline, quick tactical videos. Fails for: slow-burn strategy content where speed isn't the point.

**8. Process Transparency**
Shows the work rather than claiming expertise. "Full strategy", "step by step", "our exact process" — positions Lorenzo as a practitioner, not a teacher.
- *$34,592 per day on Shopify | Full Creative Strategy*
- *My $106M Meta Ads Strategy (step by step)*
- *How I Make BANGER Street Interview Ads (+$1M Spent)*
- Works for: deep-dive tutorials, full walkthroughs, anything where the behind-the-scenes access is the value. Fails for: short punchy belief-breaker content.

---

## Step 2 — Map the Mechanism to the Video Topic

Not every mechanism is equally strong for every topic. Use this table as a starting point — not a constraint. Any mechanism can work for any topic if executed correctly.

| Video type | Strongest mechanisms |
|---|---|
| Client case study | Number Contrast, Oddly Specific Proof, Speed Compression |
| Strategy overview / methodology | Credential Anchor, Process Transparency, Named Mechanism |
| Format tutorial (street interview, podcast ad, VSL) | Named Mechanism, Process Transparency, Credential Anchor |
| Belief-breaking / contrarian | Belief-Breaker, Number Contrast |
| Algorithm / platform update | Platform/Technical Problem, Belief-Breaker |
| Creative volume / ad fatigue | Belief-Breaker, Number Contrast, Oddly Specific Proof |
| Tactical how-to | Process Transparency, Named Mechanism, Speed Compression |

Pick the top 2 mechanisms that fit the topic. Write at least 3 title variations per mechanism. Then validate each against the reference table — if no competitor has outperformed on this mechanism for this topic, reconsider.

---

## Step 3 — Rebuild in Lorenzo's Voice

### Voice Rules

**Do:**
- Lead with the result or number. If the video has a number, it goes in position 1 or 2.
- Use "My" or "We" — personal ownership of the strategy or result.
- Keep it under 10 words before any parenthetical. Count them.
- Use the parenthetical for specificity: a number, a format name, a time frame, a platform name.
- Use lowercase when the tone is conversational. Not every title needs title case.
- Name the platform. "Meta", not "social media" or "paid ads".
- Let the gap do the work in contrast titles. "$2k/day to $38k/day" needs no explanation.

**Don't:**
- No "dark truth", "hidden", "exposed", "secret", "glitch", "illegal" — theatrical language.
- No "Here's why / Here's what / Here's how" — YouTube filler.
- No round numbers when you have a real one. $1.81M beats $2M every time.
- No invented numbers. Use a placeholder (`$XM`, `£Xk/day`) until the real figure is confirmed.
- No adjectives that don't add information: "ultimate", "complete", "powerful", "game-changing".
- No explaining the insight in the title. The title creates curiosity. The video delivers the answer.
- No questions. Statements outperform questions for this audience.

### Parenthetical Rules

The parenthetical is for specificity, not punchlines.

Good parentheticals:
- `(step by step)` — process signal
- `(Andromeda update)` — timeliness signal
- `(+$1M spent)` — credential signal
- `($106M in Meta spend)` — credential signal
- `(full breakdown)` — depth signal
- `(2026)` — timeliness signal

Bad parentheticals:
- `(you need to see this)` — theatrical
- `(everyone's missing this)` — theatrical
- `(this changes everything)` — theatrical
- `(it's not what you think)` — theatrical

---

## Reference Table — Competitor Title → Mechanism → Lorenzo Version

| Competitor title | Mechanism | Lorenzo version |
|---|---|---|
| *$3k/day VS $87k/day \| The Creative Gap Exposed* | Number Contrast | *£Xk/day to £Xk/day \| What changed (one creative format)* |
| *$827,869 in 4 days on Shopify \| Offer + Landing Page Strategy* | Oddly Specific Proof + Speed Compression | *$[X]M in 5 days for a supplement brand (full breakdown)* |
| *Why Your "Bad" Ads Get Spend on Facebook* | Belief-Breaker | *Why your worst ads get the most spend* |
| *My $106M Meta Ads Strategy (step by step)* | Credential Anchor + Process Transparency | *(already Lorenzo's — use as written)* |
| *No One Will Buy Your Brand* | Belief-Breaker | *Nobody is clicking your ad. Here's why.* |
| *Unaware Ads: How to Legally Print Money in eCom* | Named Mechanism | *Unaware ads: my $106M Meta strategy starts here* |
| *Scale to $2.3M/Month on Shopify with Unaware Ads* | Oddly Specific Proof + Named Mechanism | *$2.3M/month with one creative type (unaware ads)* |
| *From $2k/Day to $160k/Day in 30 Days* | Number Contrast + Speed Compression | *£Xk/day to £Xk/day in 90 days (what we changed)* |
| *How I Make BANGER Street Interview Ads (+$1M Spent)* | Named Mechanism + Credential Anchor | *(already Lorenzo's — use as written)* |
| *The Real Reason Your Business Stopped Growing* | Belief-Breaker | *Why brands plateau at $30k/month (it's not your ads)* |
| *$100M e-commerce playbook for 2026* | Credential Anchor | *My $106M Meta ads strategy for 2026* |
| *He scaled an eCom brand to $800k/day…* | Oddly Specific Proof + Curiosity gap | *He was at £Xk/day. Now £Xk/day. One thing changed.* |
| *8 Figure B Roll Creative Strategy* | Named Mechanism | *The b-roll ad format scaling 8-figure brands on Meta* |

---

## Approved Direction Examples (from Mauro and Lorenzo)

These are titles from Mauro and Lorenzo's shortlist that represent the right direction. Use them as calibration for tone, mechanism, and Growthub's angle. They are not a fixed list to repeat — they show what good looks like.

| Title | Why it works |
|---|---|
| *Ranking every ad format in 2026* | Opinionated, list-based, searchable. Growthub is one of few with enough real data to credibly rank formats. |
| *How to write hooks with a 45% hook rate* | Specific benchmark makes it credible and searchable. Add format impact angle — the same hook lands differently in a street interview vs a VSL. Validate against recent hook videos before publishing. |
| *How to pick winning angles every single time (2026)* | "Every single time" removes the guesswork frustration the ICP feels. Year marker keeps it current. |
| *How to run humor ads on Meta in 2026* | Niche format that almost nobody teaches. High-intent, low-competition. Growthub has in-house data on this. |
| *The 3 ads that generated $[X] for our client* | Case study format. Placeholder until client number confirmed — swap `$[X]` for real figure before publishing. |
| *What unaware ads are (and why they scale brands past $1M/month)* | Named mechanism + outcome proof. Definitional title — owns the term "unaware ads" in search. |
| *How $100k/day brands source creators* | Targets exactly the ICP ceiling (£30k–£100k/month). Operational detail most channels skip. |
| *How to script organic ads on Meta ($100M+ generated)* | Credential in parenthetical. Organic ads framing is differentiated from standard paid creative advice. |
| *I tested over 5000 ads. Here are the scripts ACTUALLY making money* | Volume proof + implied insider access. "ACTUALLY" signals contrast from noise — resonates with an audience sick of generic advice. |
| *How I use viral TikToks to create winning Facebook Ads (to scale to $1M/month on Meta)* | Cross-platform angle nobody else connects. Outcome anchor in parenthetical. |

---

## Output Format

### Generate titles

For each mechanism selected in Step 2, write 3–5 title variations. Label each clearly.

```
MECHANISM: [Mechanism name]

1. [Title]
2. [Title]
3. [Title]
```

### Shortlist

After generating all titles, pick the top 5. For each one, note in one line why it works and one line where it could fail.

```
TOP 5

1. [Title]
   Works because: [one line]
   Fails if: [one line]

2. [Title]
   ...
```

### Recommendation

State the single recommended title with a one-sentence reason.

```
RECOMMENDED: [Title]
Why: [one sentence — specific to the video topic and Lorenzo's channel]
```

---

## Anti-Patterns

- Never write a title with a round number when an oddly specific one is available.
- Never use theatrical language ("dark truth", "hidden", "exposed", "secret").
- Never write more than 10 words before the parenthetical. Count them.
- Never use the parenthetical for a punchline. Use it for a fact.
- Never recommend a title that any generic Meta ads channel could have written. The Growthub sauce must be visible — a specific number, a specific format, or a perspective only Lorenzo can credibly claim.
- Never write a question title.
- Never explain the insight in the title. If the title gives away the answer, rewrite it.
- Never produce fewer than 6 title variations across at least 2 mechanisms.
- Never use an invented specific number. Use a placeholder (`$[X]`, `£Xk/day`) and note that it needs confirming before the video goes live.
