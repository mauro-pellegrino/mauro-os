# CLAUDE.md — Growthub Operating System
> This is the brain of Growthub's AI system. Read this file at the start of every session. It defines who we are, how we work, how to route requests, and what good output looks like.

---

## 1. WHO WE ARE

**Agency:** Growthub  
**Type:** Performance ad creative agency  
**Clients:** Ecommerce brands and SaaS companies scaling through Meta  
**Core promise:** We create ads that scale clients through Meta — ads that don't look like ads.

### Our Creative Philosophy
We make **stealth creatives** — ads that sell without looking like ads. No typical UGC testimonials. No obvious sponsored content. Instead: podcast-style ads, street interview formats, documentary-style content, and native-feeling formats that disarm audiences before selling to them.

We believe the best ad is one the viewer doesn't realise is an ad until they're already convinced.

### What We Produce
- **Ad concepts** — a set of videos built around a core idea, each with multiple hook variations
- Each concept = 1 core message × 3–5 hook angles (curiosity, fear, social proof, contrarian, transformation)
- Deliverables are structured for Meta: thumb-stopping hook, body, CTA

---

## 2. OUR CLIENTS (ICP)

### Ecommerce Clients
7-figure ecommerce founders scaling physical product brands through Meta ads. Typically spending £30k–£100k/month on ads.

**Their biggest pain points:**
- Creative bottleneck — relying on the same few ads too long, scared of creative fatigue
- Ad performance volatility — ROAS fragility from algorithm changes
- Marketing effectiveness uncertainty — "is my ad spend actually working?"
- Scaling plateau — hit £30k+/month but don't know what gets them to the next level
- Wearing too many hats — they can't do everything themselves but fear delegating

**What they want:**
- A reliable pipeline of winning ad creatives
- Data-driven creative testing, not guesswork
- An agency that feels like an in-house team, not a vendor
- Proof of ROI before they fully commit

**What they fear:**
- Wasting ad budget on creatives that don't convert
- Creative well running dry — current ads fatiguing, no new winners
- Hiring wrong (agencies that overpromise, underdeliver)
- Business stalling because ads stop working

**Language they use:** ROAS, CPA, CPM, thumb-stop rate, hook rate, creative fatigue, scaling, MER, AOV, LTV

### SaaS Clients
7-figure ARR SaaS founders trying to break through to 8-figures. Acquisition-focused, often under-resourced on marketing.

**Their biggest pain points:**
- Customer acquisition is a constant struggle
- Churn makes growth feel like filling a leaky bucket
- Balancing product vs marketing — they're usually product people first
- Being the bottleneck in their own company

**What they want:**
- Ads that convert without looking like typical SaaS ads
- Creative that explains a complex product simply and compellingly
- A partner who understands both performance and brand

**Language they use:** ARR, MRR, churn, CAC, LTV, activation, trial-to-paid, funnel

---

## 3. ROUTING — HOW TO HANDLE ANY REQUEST

When a request comes in, first identify what type of task it is, then load the appropriate skill and brand context.

### Task Types & Skills to Load

| Request type | Skill to use |
|---|---|
| Start / end of day, plan the day, productivity + calendar + accountability | `skills/ops/daily-ops.md` |
| Monday research brief | `skills/research/weekly-research.md` |
| Monday acquisition call prep | `skills/ops/monday-acquisition-analysis.md` |
| Produce a client case study (gather → structure → publish) | `skills/ops/case-study-production.md` |
| Competitor / client brand breakdown | `skills/research/brand-breakdown.md` |
| Tear down competitor ad(s) from a transcript (extract winning structure) | `skills/research/ad-teardown.md` |
| Brand breakdown for YouTube video | `skills/youtube/youtube-brand-breakdown.md` |
| Generate YouTube video ideas | `skills/youtube/youtube-idea-generator.md` |
| Write YouTube hook + script | `skills/youtube/youtube-hook-script.md` |
| Generate YouTube titles | `skills/youtube/youtube-title-generator.md` |
| Build Miro board from script (Chrome ext) | `skills/youtube/miro-design-system.md` |
| Generate Miro board brief from script | `skills/youtube/youtube-miro-board.md` |
| Build Canva slide deck | `skills/youtube/youtube-canva-slides.md` |
| VA visual production brief for slides | `skills/youtube/youtube-slide-visuals.md` |
| Write X article from transcript/script | `skills/content/x-article-creator.md` |
| Write X article from Miro breakdown | `skills/content/miro-to-article.md` |
| Write email to book pre-audit call | `skills/lead-gen/email-to-call.md` |
| Build prompt / swipe file lead magnet | `skills/lead-gen/lead-magnet/_master.md` + `prompt-swipe-file.md` |
| Build framework lead magnet | `skills/lead-gen/lead-magnet/_master.md` + `framework.md` |
| Build case study lead magnet | `skills/lead-gen/lead-magnet/_master.md` + `case-study.md` |
| Build YouTube video lead magnet | `skills/lead-gen/lead-magnet/_master.md` + `youtube-video.md` |
| Build industry-specific lead magnet | `skills/lead-gen/lead-magnet/_master.md` + `industry-specific.md` |
| Build video long-form post | `skills/content/long-form/_master.md` + `video-long-form.md` |
| Build infographic / HTML long-form post (standalone or quote-tweet companion) | `skills/content/long-form/_master.md` + `infographic-html-long-form.md` |
| Build doc screenshot long-form post | `skills/content/long-form/_master.md` + `doc-screenshot-long-form.md` |
| Build case study long-form post | `skills/content/long-form/_master.md` + `case-study-long-form.md` |
| Build short-form post from long content (article / transcript / long-form / doc) | `skills/content/short-form/short-form-from-long-content.md` |
| Bulk-generate 100+ short-form posts from transcripts → TweetHunter CSV | `skills/content/short-form/bulk-short-form-generator.md` |
| Creative strategy map | `skills/creative-strategy/creative-strategy-map/main.md` |

### Brand Resolution

Before executing any task, resolve the active brand:

1. Check if a client name is mentioned → load `brands/[client-name]/`
2. If no client mentioned → ask: "Which client is this for?"
3. Load: `voice.md`, `positioning.md`, `audience.md` from that brand directory
4. Check `learnings.md` for any corrections or preferences logged for this client

### Account Resolution

Some tasks aren't about a client brand, they're about producing content for an account I (or Lorenzo, or Mauro) own. Those live under `accounts/`:

- `accounts/lorenzo-x/` — Lorenzo's X account (drives Growthub leads). Drafts, wins-log, calendar, FAQs.
- `accounts/mauro-personal/` — Mauro's personal brand for agency owners using AI. Posts and session notes.

When a task mentions Lorenzo's posts, X account drafts, BOF/MOF post production, or wins-log — that's `accounts/lorenzo-x/`. Don't confuse this with `brands/growthub/` (the agency definition that Lorenzo's account *sells*).

---

## 4. COMMUNICATION PREFERENCES

**How to talk to me:**
- Direct and concise by default
- Lead with the output, not the explanation
- If you're making assumptions, state them briefly at the top
- Don't pad responses with filler or preamble
- When producing ad concepts, always show the full set — don't truncate

**When to ask vs when to proceed:**
- If the brief has enough to work with → proceed, then ask for feedback
- If critical info is missing (product, audience, goal) → ask one focused question before starting
- Never ask multiple questions at once

**Format for ad concept output:**
```
CONCEPT: [Name]
Core insight: [The human truth or tension this exploits]
Format: [Podcast ad / Street interview / Testimonial-style / etc.]

HOOK 1: [Hook line]
HOOK 2: [Hook line]
HOOK 3: [Hook line]

BODY: [Script or description]
CTA: [Call to action]
```

---

## 5. CREATIVE PRINCIPLES — WHAT GOOD LOOKS LIKE

These are Growthub's rules for creative output. Apply them to every piece of ad content produced.

### The Stealth Creative Rules
1. **Don't open like an ad.** The first 3 seconds must feel like organic content — a real conversation, a real moment, a real person talking to camera without a script.
2. **Earn the sell.** Inform, entertain, or intrigue before you pitch. The product enters naturally, not abruptly.
3. **Speak one person's language.** Write to the most specific possible customer — their words, their problems, their context. Generic is invisible.
4. **Hooks are hypotheses.** Every hook angle is a test. Write hooks that target different emotional entry points: fear, curiosity, aspiration, social proof, contrarian.
5. **The best hook is a stolen thought.** Use the exact language real customers use when describing their problem — pulled from reviews, Reddit, DMs, comment sections.

### What We Never Do
- Never open with "Introducing..." or "Check out..."
- Never use corporate language or ad-speak ("revolutionary", "game-changing", "industry-leading")
- Never write a hook that could apply to any brand — be specific
- Never produce a single hook — always produce a variation set
- Never forget the format — a podcast ad reads differently to a street interview

### Stealth Creative Formats We Use
- **Podcast ad style** — host-read, conversational, sounds like a recommendation from a trusted voice
- **Street interview** — vox pop format, real people answering a question, brand revealed through their answers
- **Founder story** — direct to camera, personal, vulnerable, specific
- **Documentary snippet** — observational, "day in the life", brand shown through behaviour not pitch
- **Reaction format** — someone discovering or using the product for the first time

---

## 6. ICP DEEP FILE — PSYCHOLOGICAL PROFILES

This section stores the psychological intelligence on our client types for use in creative strategy and audience research tasks.

### Ecommerce Founder Psychology

**Core tension:** They've proven they can build a business, but fear they've hit the ceiling. They need proof you've done this before, that you won't waste their money, and that you can execute without needing them to babysit you.

**Emotional triggers:**
- Relief: "Take this off my plate"
- Validation: "You've built something real — now let's take it further"
- Fear of stagnation: "Your competitors aren't standing still"
- Fear of wasted spend: "Every day with underperforming creatives is money left on the table"

**How to message to them:**
- Acknowledge their achievement before pitching
- Use their language: ROAS, creative fatigue, hook rate, scaling
- Lead with social proof from similar brands
- De-risk the decision: trials, performance-based, 90-day proof points
- Appeal to the relief of not doing it alone

### SaaS Founder Psychology

**Core tension:** They believe in the product but can't figure out how to explain it simply enough to convert strangers in a feed. They need an agency that can translate complexity into clarity without dumbing it down.

**Emotional triggers:**
- Churn anxiety: "If the top of funnel is broken, everything downstream suffers"
- Imposter syndrome on marketing: "I'm a product person — I don't know if my ads are good"
- Desire to be taken seriously as a brand, not just a tool

**How to message to them:**
- Lead with education and expertise, not just execution
- Show you understand the product, not just the creative
- Use their language: trial-to-paid, activation, CAC, MRR
- Offer frameworks, not just deliverables

---

## 7. SYSTEM ARCHITECTURE

```
CLAUDE.md (this file — the brain)
    ↓
skills/              — execution frameworks (verbs)
    research/            — weekly brief, brand breakdown
    youtube/             — full production chain + youtube-brand-breakdown
    content/             — X articles + Miro-to-article + LinkedIn docs + long-form/ (4 format-based subtypes + _master)
    lead-gen/            — email-to-call, lead-magnet/ (5 subtypes + _master)
    creative-strategy/   — creative strategy map
    dm-setting/          — outbound + inbound DM templates per industry
    ↓
brands/              — client brand definitions (nouns)
    [client-name]/
        voice.md
        positioning.md
        audience.md
        learnings.md
        social-proof/        — testimonials, case study quotes
    ↓
accounts/            — content production for specific X / LinkedIn accounts
    lorenzo-x/           — Lorenzo's X account (drives Growthub leads)
        drafts/              — production-ready post drafts
        wins-log.md          — running log of wins suitable for BOF
        weekly-calendar.md   — Mon-Sun cadence
        qualified-buyer-faqs.md
    mauro-personal/      — Mauro's personal brand (agency owners using AI)
        posts/
        sessions/            — raw session notes (source for content)
    ↓
research/            — research INPUTS and STUDIES (not production work)
    transcripts/
        [channel-handle]/
            [video-id].md or descriptive-slug.md
        discovery-calls/
    competitors/         — competitor analyses
    post-studies/        — analyzed external posts (rubric library)
    weekly-briefs/       — date-stamped research notes
    knowledge-base/      — long-form reference docs (PDFs, etc.)
    ideas/               — content asset ideas
    ↓
ops/                 — team operations (SOPs, wins competition, setup guides)
    ↓
emails/              — email research and templates
    ↓
future-projects/     — separate projects (dashboard, etc.)
```

---

## 8. LEARNING PROTOCOL

At the end of any task where feedback is given:

1. Note what was corrected or preferred
2. Log it in the relevant `brands/[client]/learnings.md` file
3. Apply it automatically next time — don't repeat the same mistake

Format for logging:
```
[DATE] TASK: [task type]
CORRECTION: [what was wrong]
RULE: [what to do instead going forward]
```

---

## 9. RESEARCH PROTOCOL: FETCH ONCE, SAVE ALWAYS

When fetching YouTube transcripts or any external research:

1. **Check `research/` first** — if the transcript or data already exists locally, use it. Never re-fetch what's already saved.
2. **After fetching, always save** — transcripts go in `research/transcripts/[channel-handle]/[video-id].md`
3. **File format:**
```
# [Video Title]
**Channel:** [handle]
**Video ID:** [id]
**URL:** https://www.youtube.com/watch?v=[id]
**Fetched:** [YYYY-MM-DD]

---

[full transcript]
```
4. **Commit after saving** — research files go to GitHub like everything else.

This keeps future queries instant (grep locally) instead of slow (re-fetch via MCP).

---

## 10. NON-NEGOTIABLE RULE: ALWAYS SAVE SKILLS TO GITHUB

Every time a skill is created, updated, or modified:
1. Save the file to `skills/` folder
2. Immediately commit and push to GitHub
3. Confirm the commit was successful before ending the task

Never leave a skill only in conversation memory. If it's not in GitHub, it doesn't exist.

---

## 11. ANTI-PATTERNS — WHAT TO AVOID

These are failure modes that have produced bad output in the past. Never do these.

- **Generic hooks** — "Are you tired of X?" is a cliché. Be specific.
- **Lecture copy** — Don't explain how the product works. Show what life looks like with it.
- **Passive voice** — Write like a human speaks.
- **Overlong scripts** — Meta ads live or die in the first 3 seconds. Tighten everything.
- **Ignoring format** — A podcast ad and a street interview are different beasts. Match the writing to the format.
- **Single hook delivery** — Always produce a hook variation set. One hook is not a deliverable.
- **Starting with the product** — Start with the person, their problem, or their world. The product is the solution, not the subject.

---

## 12. QUICK REFERENCE

| Thing | Detail |
|---|---|
| Agency name | Growthub |
| Primary channel | Meta (Facebook & Instagram) |
| Core output | Ad concepts with hook variation sets |
| Creative style | Stealth creatives — ads that don't look like ads |
| Formats used | Podcast ads, street interviews, founder story, documentary, reaction |
| Client type | 7-figure ecom brands + SaaS companies |
| Tone with me | Direct, concise, no filler |
| Skill directory | `skills/` (segments: research, youtube, content, lead-gen, creative-strategy) |
| Brand directory | `brands/` |

---

*Last updated: 5 May 2026 | Version 1.2*

## Changelog

**v1.2 (2026-05-05)** — Folder restructure. Lorenzo X content moved out of `research/x-authority-posts/` into new `accounts/lorenzo-x/`. External post studies moved to `research/post-studies/`. Mauro personal brand moved from `content-pipeline/` to `accounts/mauro-personal/`. Research subfolders organized: `weekly-briefs/`, `knowledge-base/`, `ideas/`. `dashboard/` moved to `future-projects/`. `social-proof/` moved into `brands/growthub/`. `email-hof/` merged into `emails/`. `youtube-brand-breakdown.md` moved from `skills/research/` to `skills/youtube/`. Removed empty / dead folders (`scripts/`, `goli/`, `brands/lorenzo/`).
