# Offer decision: the whole system, free files, paid install

Built 2026-10-09 from Mauro's round 4 decisions (`review-queue/decisions/2026-10-09-v4.txt`, items 12, 13,
16, 17). Reads with `ownership-inventory.md`, `whop-community-research.md`, `whop-product-v1.md`,
`intake-viability-v2.md`, `jk-molina-review.md`, `brand/engine/README.md`, `brand/engine/NEXT-BUILD-PLAN.md`
and the X scripts in `tools/`. Visual version: `product-ladder.html` / `product-ladder.png`.

Replaces the v1 pick in `whop-product-v1.md` (Outlier Intake as the paid kit). Round 4, #13: "i see no
demand for this yet, i would rather give away my whole system of going from yt vid to content and voice
and company brain".

---

## 0. The ownership fact, first

The core offer sits on files that live in growthub-os. Every one of them was written by Mauro
(`git log` in growthub-os: all commits by "Mauro Pellegrino"), while he worked for the agency:

| System | growthub-os files | First commit there |
|---|---|---|
| YouTube system | `skills/youtube/` (9 files) | 2026-04-20 |
| Video to article | `skills/content/miro-to-article.md`, `x-articles/` (9 files) | 2026-04-20, 2026-09-01 |
| Long form, short form | `skills/content/long-form/`, `short-form/` | 2026-05-26, 2026-05-27 |
| Lead magnets | `skills/lead-gen/lead-magnet/` (7 files) | 2026-05-26 |
| Company brain | `skills/ops/company-brain-install.md`, `ops/SOURCE-ORDER.md`, `ops/tools/staleness-check.py`, `brain-health.py`, `decisions-check.py` | 2026-09-15 |
| Voice, measured | `ops/tools/voice-extract.py` | 2026-09-14 |

`growthub-os/ops/MAP.md` says "`growthub-os` is canonical for skills". Round 4, #12 settled two things:
`jlago-del` is Juan, a Ghosted Calls employee, so inventory row 10 (X reply assistant, content analytics
review) and the 2 Juan files in row 13 are Ghosted Calls work. And "Lead magnet system should work, let's
use it". That is Mauro's call to use it. It does not answer the agency.

**So this plan uses the files because Mauro said so, and action point 1 is a written yes from the agency,
dated.** Draft of the ask (Mauro sends it, in his own words):

> I want to give away a generic version of the content skills I wrote (YouTube to article and posts, lead
> magnets, the brain setup) under Ghosted Calls. No Growthub name, no client, no number, no example from
> our accounts. OK with you?

Until that yes exists, every packaged file is a clean rewrite: a search for `growthub`, `lorenzo`, `bogdan`,
`/Users/mauro`, client names and `leadshark` returns 0. `research/bogdan-brain/` never ships (client names,
4 redacted credentials, `research/bogdan-brain/README.md`).

---

## 1. The decision

1. **The offer is the whole system, and the files are free.** YouTube video to content (X article, 10 X posts, LinkedIn post, a lead magnet that IS the post) plus a voice file plus a company brain (source order, claims ledger, the Gate). A free Whop product delivers the ZIP, the setup guide and the Looms. Mauro asked for this (#13), JK's table says files alone "rarely serve as an upsell" (`servant.pdf` p3), and the free room is how every big community fills its paid tier (AAS: 452,600 free, 3,700 paid).
2. **What is paid is access: a one-time Install Sprint.** One live group install call, then 14 days where Mauro reviews each buyer's first video-to-content run (1 article, 10 posts) and their filled brain. **$197 founding for cohort 1, 10 seats, 5-day cart, then $297.** The band comes from the stranger test: the agency-owner persona pays "$150 to $300" for the system with "a review of his first batch" (`intake-viability-v2.md`). Fallback: $100 founding (JK's customer step) if the first 10 direct conversations name price as the blocker.
3. **Whop model: free product + one-time paid cohort + Agency Booked Calls as the higher option at checkout.** No monthly room yet. The 22 Aug rule (`ACTIONS.md` line 13, `brand/engine/README.md`) says recurring needs modules arriving, weekly corrections and a live element, and none runs today. The room opens at $49/mo only after the weekly drop (Mon read, Wed template, Fri Gate catch) has run 4 weeks in the free tier. Monthly at that point matches the market band ($19 to $129/mo, `whop-community-research.md`).
4. **Launch size: the free list is the audience, and it is small.** @maurojpelle earned 19 follows from June to 5 Oct (`tools/x-three-accounts.py`: 0, 1, 10, 5, 3 by month), median 84 impressions per original post since 1 Jun, best post 2,316. A launch post reaches hundreds of people. Buyers for cohort 1 come from direct messages to the lists that exist (section 5). I plan for single-digit buyers in cohort 1. That is a judgement from these numbers, not a forecast.
5. **The free system is also the reach play.** Resource posts brought nearly all Lorenzo and Bogdan follows (May: 14 posts, 878 follows; 11 posts, 699 follows, `tools/x-follow-drivers.py`) and stopped after the X automation bans. A post or article can BE the resource: "I'm giving away the system" as an X article, Whop link in bio, no comment-to-DM. Mauro's own lifts favour the words it needs: skills 2.44x, prompts 2.04x, article 1.83x, code 1.80x, agents 1.64x (`tools/x-keywords.py`).

What this drops: the $500 one-time module 01 (22 Aug), the Outlier Intake as paid v1 (8 Oct), and the separate $27 to $99 kits. The intake sheet becomes one free tool inside the system.

`[NEEDS: Mauro confirms $197 / $297 and the 10 seats]` `[NEEDS: the product name; "The Engine" is the working name from brand/engine/]`

---

## 2. What exactly gets sent

### The package

```
the-engine/                         one ZIP on the free Whop product
  README.md                         setup guide: what you need, 3 install paths, first run in 20 minutes
  START-HERE.md                     the 5 stages (source, extraction, formats, distribution, measurement)
  claude-code/
    CLAUDE.md                       template: who you are, who you serve, routing table, operating rules
    brain/
      SOURCE-ORDER.md               which source wins, one list per question type
      claims-ledger.md              approved / banned / gaps, every number with a source and a date
      decisions-ledger.md           agreed to done
      voice.md                      generated by skills/voice/, starts empty
      bans.md                       hard bans, starts with 10 generic AI tells
      rejected/  approved/          one file per correction, 4 blocks each
    skills/
      00-source/                    transcript library: folder rule, fetch-once rule, paste or yt-dlp
      01-voice/voice-extraction.md
      02-video-to-content/          the orchestrator + article, 10 posts, LinkedIn, long form, cover prompt
      03-lead-magnet/               magnet subtypes, the post or article is the resource
      04-measure/                   the Monday read on your own X export
    .claude/agents/gate.md          5-pass review before you see a draft
    .claude/hooks/voice-gate.py     fires the checks on writing prompts
    tools/                          staleness-check.py, monday-read.py, outlier sheet (index.html)
    inputs/transcripts/  outputs/
  claude-ai-project/
    instructions.md                 paste into Project instructions
    knowledge/                      the brain files + skill files as .md, a list of what to upload
    prompts.md                      the Gate run, the Monday read on a pasted CSV
  example/                          one finished run on one of Mauro's own recorded videos
```

### The three versions

| Version | Who it is for | What runs | What does not run |
|---|---|---|---|
| **Claude Code** | Owner or team member with a terminal | Everything: hook, Gate agent, scripts | |
| **claude.ai Project** | Owner with a VA, no terminal. Both stranger personas in `intake-viability-v2.md` use a browser chat, never a terminal | Brain, voice, every content skill as knowledge files; Gate as a final prompt; Monday read as a pasted-CSV prompt | The hook (no auto-fire), the scripts, the staleness check |
| **Notion** | | | `[NEEDS: Mauro reverses 22 Aug]`. `brand/engine/README.md`: "Notion is out, permanently". Not designed |

Delivery: Whop free product holds the ZIP and the Looms. The free member list is the cohort 1 list, which a
public GitHub repo would not give. `[NEEDS: verify Whop free products, course pages and file delivery are on the free tier; flagged unverified in brand/engine/README.md since 22 Aug]`

### Per system: source, what is missing, Growthub dependency

| System | Source today | Missing to work without Mauro | Growthub? |
|---|---|---|---|
| **Company brain** | growthub-os `company-brain-install.md` (247 lines, 17 agency mentions), `SOURCE-ORDER.md` (126), `staleness-check.py`, `decisions-check.py`. mauro-os Gate (`.claude/agents/gate.md`, `hooks/voice-gate.py`, `gate-playbook.md`, clean) | Blank templates for 5 files. A new "find your 3 failures" interview prompt. The worked example rebuilt on Ghosted Calls failures (review-queue decisions), since all three in the method doc are Growthub's. Hook made path-free | **Yes** (method + tools). Gate is clean |
| **Voice** | mauro-os `skills/research/voice-extraction.md` (clean, 7 steps). growthub-os `voice-extract.py` (103 lines) | A worked example on a public account. A browser version of step 3 (mining with counts). `brand/voice.md` stays out (agency fork) | Script **yes**, method no |
| **YouTube video to content** | growthub-os `x-articles/` 01 to 07 (0 to 2 agency mentions per file), `short-form-from-long-content.md` (16), `long-form/video-long-form.md` (27), `linkedin-docs/`. mauro-os rewrites of long form and short form. mauro-os `CLAUDE.md` section 7 (the markdown-to-article-plus-10-posts handoff) | **The orchestrator skill does not exist.** Today the flow is a rule in `CLAUDE.md` plus 4 skill files. Write `02-video-to-content/run.md`: transcript in, article + 10 posts + LinkedIn post + cover prompt out, Gate last. One worked example on Mauro's own recording (`research/transcripts/maurojpelle/how-to-create-lead-magnets-with-claude.md`, 2026-08-20). The article corpus (`_corpus.md`) cites agency captures: keep the rules, drop the account names | **Yes** |
| **Lead magnets** | mauro-os `brand/engine/module-01-lead-magnets/` (9 pages, 1,901 lines, build-tested by Juan, `content/qa/lead-magnet-build-log.md`), `skills/lead-gen/lead-magnet/` (7 files) | Cut LeadShark and comment-to-DM (26 lines across 5 pages) and `youtube-lead-magnet.md`'s autodm package. Replace with "the post or article is the resource, link in bio". Page 03 evidence is a 40-row July pull from an agency account: label it or rebuild on Mauro's export. Zero screenshots in a module that says screenshots win | **Yes** (twins from 2026-05-26, proof from an agency account) |
| **Measurement (Monday read)** | mauro-os `maurojpelle-baseline.py`, `x-keywords.py`, `x-follow-drivers.py`, `/gc-monday` | One `monday-read.py` that reads any X export by column name. The `x-*` scripts read founders' exports today | **Yes** for the `x-*` inputs; method is Mauro's |
| **Outlier sheet** | `content/lead-magnets/outlier-to-template-intake/index.html` | Gaps 1, 2, 4 from `intake-viability-v2.md`: floor line, gated-post flag, 390px layout | Mixed (row 5) |

### Looms to record

| # | Loom | Version |
|---|---|---|
| 1 | What you get and the 5 stages | both |
| 2 | Install, Claude Code | Claude Code |
| 3 | Install, claude.ai Project | Project |
| 4 | Fill the brain: your 3 failures into a source order and a claims ledger | both |
| 5 | Your voice file from your own best posts | both |
| 6 | One video into one X article, live | both |
| 7 | The same video into 10 posts and a LinkedIn post | both |
| 8 | The same video into a lead magnet that is the post | both |
| 9 | The Gate catches a draft, and the rejection gets logged | both |
| 10 | The Monday read on your own export | Claude Code |

Target under 10 minutes each. `[NEEDS: Mauro records; lengths come from the recordings]`

---

## 3. Everything he can offer, ranked by evidence

Evidence labels: **M** = @maurojpelle's own numbers. **L/B** = Lorenzo's or Bogdan's accounts (Growthub),
read as a signal of what the ICP clicks, never as Mauro's proof. **none** = no reach data yet.

| # | System | Repo | Evidence | Where it goes |
|---|---|---|---|---|
| 1 | Measurement loop (Monday read, keyword lift, follow drivers) | mauro-os `tools/`, `/gc-monday` | **M**: his top post (5 Sep, 2,316 impressions, 16 bookmarks, "needs to run this analysis") and #3 (26 Sep, 1,160, "Every monday the same thing runs") | Free module 04, the Monday drop |
| 2 | Claude prompts and skill files as the resource | both | **L/B**: "claude insane" 10.08x, prompts 9.02x (Lorenzo), prompts 9.92x, mini-guide 7.66x (Bogdan). **M**: skills 2.44x, prompts 2.04x | The giveaway article's words; prompt swipe file subtype |
| 3 | X article system | growthub-os `x-articles/`, `article-studies/` (41 captures) | **L**: articles above 10K precede most X-sourced above-floor bookings; the 14-day pipeline article did 25,000 (`_corpus.md`, art-032). **M**: article 1.83x | Free module 02 |
| 4 | Lead magnet system | mauro-os `brand/engine/module-01`, both `lead-magnet/` | **L/B**: May resource posts 878 and 699 follows; 0 after the bans | Free module 03, rewired |
| 5 | YouTube system (ideas, titles, hooks, boards) | both `skills/youtube/` | ICP fit: "already makes good YouTube videos" (`brand/vision-2026.md`, 17 Aug). Reach: `[NEEDS: YouTube numbers]` | Source stage; boards stay out (Miro, Growthub lanes) |
| 6 | Outlier intake + post templates | mauro-os | **M**: 15 Sep post on saving X articles, 1,067 impressions, 4 visits. Approved X7, X8 | Free tool |
| 7 | Company brain + Gate + approval-rate loop | both | none on reach. LI2 "whole content system" drafts exist (round 4) | Free module 00; the Fri drop |
| 8 | ASCII visuals kit | mauro-os `content/ascii/`, `tools/ascii-anim/` | none yet | Cohort bonus |
| 9 | Process maps | both | **M**: 5 Oct process post, 49 impressions | Later |
| 10 | X reply assistant (Juan's) | mauro-os | **M**: 151 replies since 1 Sep, 1 follow | Internal |
| 11 | Voice extraction | mauro-os | **M**: "voice" 0.30x on 20 posts | Inside the brain, never its own product |
| 12 | Profile study set | mauro-os | none | Later |
| 13 | Review queue, week calendar, morning page | `~/.claude/skills/` | Own-productivity posts fail the reader-value rule (`positioning.md`, review 8 Oct) | Internal |
| 14 | Agency Booked Calls | mauro-os `content/offer/` | 0 sends so far (BACKLOG) | Higher option |
| out | Creative strategy, ad skills, DM setting, outbound, content research reports | growthub-os | Agency lane (`positioning.md`), client data | Never |

One caution on the whole table: follows and calls barely move together on the Growthub accounts
(Spearman +0.09 same week, +0.27 next week, W02 to W26, `tools/x-follows-vs-calls.py`). Reach is the
input. Calls get counted on their own.

---

## 4. Action points

Owners: **M** = Mauro, **C** = Claude, **J** = Juan. Nothing here posts or sends without Mauro.

### First 7 days

| # | Day | Owner | Step | Time | First command or file |
|---|---|---|---|---|---|
| 1 | Fri 9 Oct | M | Send the agency ask (section 0). Log the answer and the date | 10 min | `content/plan/ownership-inventory.md` rows 5, 11 to 13 |
| 2 | Fri 9 Oct | M | Confirm price ($197 founding, 10 seats, $297 after) and pick the name | 5 min | this file, section 1 |
| 3 | Fri 9 Oct | C | Build the package skeleton and the scrub test | 45 min | `mkdir -p ~/mauro-os/products/engine/claude-code/{brain,skills,tools}` |
| 4 | Sat 10 Oct | M | Create the Whop store: one free product, one paid product (draft, hidden). Check free-tier gating and file delivery | 30 min | whop.com dashboard |
| 5 | Sat 10 Oct | C | Write the orchestrator `02-video-to-content/run.md` and run it on Mauro's lead magnet recording | 2 h | `research/transcripts/maurojpelle/how-to-create-lead-magnets-with-claude.md` |
| 6 | Sun 11 Oct | C | Port the brain: 5 blank templates, the 3-failures prompt, Gate path-free | 2 h | `growthub-os/skills/ops/company-brain-install.md` |
| 7 | Mon 12 Oct | C | Rewire module 01 lead magnets: cut LeadShark and comment-to-DM | 1.5 h | `grep -rn -i "leadshark\|autodm\|comment" brand/engine/module-01-lead-magnets/` |
| 8 | Mon 12 Oct | M | First `/gc-monday` run (already planned); its output becomes the first Monday drop | 30 min | `/gc-monday` |
| 9 | Tue 13 Oct | J | Stranger test 1: install the Claude Code version from the README only, on a public YouTube video. Log every stop | 2 h | `content/qa/engine-stranger-test-1.md` |
| 10 | Tue 13 Oct | C | Build the claude.ai Project version from the same files | 1 h | `products/engine/claude-ai-project/instructions.md` |
| 11 | Wed 14 Oct | M | Record Looms 1, 2 and 6 | 45 min | section 2, Loom list |
| 12 | Wed 14 Oct | C | Fix every stop from Juan's test. Run the scrub grep to 0 | 1.5 h | `grep -rniE "growthub\|lorenzo\|bogdan\|/Users/mauro\|leadshark" products/engine/` |
| 13 | Thu 15 Oct | M + C | Draft the giveaway article ("the whole system, free") and the Whop free page. Gate both. Stage only | 1 h | `content/drafts/` |
| 14 | Thu 15 Oct | M | Name the warm list: the 5 to 6 agency owners he ghostwrote for, the 2 to 3 churned contacts (blocked in BACKLOG since August) | 15 min | `BACKLOG.md`, NOW section |

About 7 hours of Mauro's time, inside the 5 to 7 hour week (`brand/vision-2026.md`). Claude carries about 11 hours.

### Weeks 2 to 4

| # | Owner | Step | Time | First file |
|---|---|---|---|---|
| 15 | J | Stranger test 2: claude.ai Project version, no terminal | 2 h | `content/qa/engine-stranger-test-2.md` |
| 16 | M | Record Looms 3, 4, 5, 7 to 10 | 1.5 h | section 2 |
| 17 | C | `tools/monday-read.py` for any X export, by column name | 1.5 h | `tools/maurojpelle-baseline.py` |
| 18 | M | Publish the free product and the giveaway article (after the agency yes) | 30 min | Whop |
| 19 | M + J | Direct messages, one a day per person: the free system to the warm list, the 15 YouTube prospects, the 5 warm fallback handles, Juan's reply list | 15 min/day | `tools/yt-prospects.py`, `brand/analytics/reply-target-list.md` |
| 20 | C | Weekly drop starts in the free tier: Mon read, Wed template, Fri Gate catch | 1 h/week | section 3, rows 1, 6, 7 |
| 21 | M | Open cohort 1: 5-day cart, 10 seats, close date | 5 days | Whop paid product |
| 22 | M | Day 14 of each buyer: offer Agency Booked Calls with a cap and a date | 10 min each | `content/offer/agency-booked-calls.html` |
| 23 | M + C | After 4 drops: decide the $49/mo room from the free-tier numbers (members, weekly active, replies) | 30 min | this file, section 1 point 3 |

Cohort 1 open date: `[NEEDS: Mauro picks]`. One option: open Mon 26 Oct, after the approved X6, X7, X8
and LI3 run 19 to 21 Oct.
