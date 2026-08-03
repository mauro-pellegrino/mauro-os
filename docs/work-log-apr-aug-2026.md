# Mauro's Work Log: April 1 to August 3, 2026

**For:** Juan (content production for @maurojpelle)
**Written:** 2026-08-03
**Source:** growthub-os git history (166 commits in this window, 219 total), mauro-os git history, the H1 2026 content-to-calls report, 22 daily worklogs, 11 acquisition call docs, and the weekly learning files.

---

## 0. How to use this doc

This is source material, not content. Every section below is something Mauro actually built, decided, or measured, with the real numbers attached. Your job is to turn these into posts, articles, threads and video ideas for **@maurojpelle**, which is Mauro's own brand aimed at **agency owners who want to run AI systems like he does**.

Three rules before you write anything:

1. **Every number in this doc is marked PUBLIC-OK or INTERNAL.** Only PUBLIC-OK numbers go into content. Nothing else, ever, and never invent one.
2. **Client names are INTERNAL.** Say "a subscription education platform" or "a haircare brand", never the brand name.
3. **Read `brand/positioning.md`, `brand/audience.md` and `brand/voice.md` first.** The audience file has a language bank pulled from 26 real Reddit threads. Use those exact words.

The topics ranked most-usable are marked ⭐ in each section.

---

## 1. The receipts (what Mauro can actually claim)

### PUBLIC-OK

| Claim | Detail |
|---|---|
| Content is 62% of the agency's qualified pipeline | H1 2026, 73 of 117 sales-qualified calls came from organic content. Cold email 21, referral 14, ads 7. |
| 375 calls booked in six months | Jan to Jun 2026 across both booking calendars. |
| He closed a $28k deal off X | Needs Mauro's sign-off on how it's framed. |
| Booking quality fell as volume rose | High-tier bookers (\$100k+/mo revenue or \$50k+/mo ad spend) went from 45% of bookings in February to 25% in June. |
| Lead magnets pull 10-25x reach but not qualified buyers | Lead-magnet posts average 27,500 impressions. Proof posts average 2,300. The proof posts are what book qualified calls. |
| One post is not a booking machine | Baseline is 6 bookings per 3 days. Across 16 posts above 25k impressions, the 3 days after averaged 7.1. A lift of 1.1. |
| Qualified buyers ask for one thing | Of 95 qualified bookers with a stated pain, creative quality/production/volume/diversity beat every other reason combined. One verbatim: "Need solid video creative. That's literally all." |
| A single day-level attribution case | Mon 2026-07-27: one X video post hit 15,000 views, 4 calls booked the same day. |
| Best qualified week measured | Jul 20-26: 10 calls conducted, 7 qualified (70%), zero no-shows. Content went 4 for 4. |
| The system is 51 skill files in git | Version-controlled, 219 commits. |
| 288 verbatim buyer pain answers collected | From the booking form, Jan to Jul 2026, grouped by ad spend tier. |
| His own brand starting line | 200 X followers, 1 YouTube video, no offer, no email list, as of Jul 1. Honest starting point, and it is usable content. |

### INTERNAL ONLY (never publish)

- Agency revenue figures and the share attributable to organic.
- Every client name: the education platform, the haircare brand, the SaaS client, the supplement brands, all of them.
- Specific client spend and dashboard screenshots.
- Team member names and who worked on what.
- Aggregate managed-spend figures from Lorenzo's videos. Those are Lorenzo's proof, not Mauro's. Never borrow them.

---

## 2. Timeline: what got built, month by month

### April 2026 — the skills library gets serious

| Date | What happened |
|---|---|
| Apr 1-10 | Built the brand-breakdown skill for competitor ad analysis. Added a "creative diversity / entity ID" layer to it. |
| Apr 6 | Built the YouTube-to-auto-DM skill (turn a video into a lead magnet with automated DM delivery). |
| Apr 6 | Built the creative-strategy-map skill with a live worked example. |
| Apr 8 | Rewrote the cold-email skill around one idea: lead with an insight, not with value. |
| Apr 13-14 | Built the lead-magnet skill (guide + auto-DM distribution). Banned 3-item parallel sentence stacks in the voice guide after spotting the pattern in AI output. |
| Apr 17 | Added the Andromeda / entity-ID framework to positioning. |
| Apr 20 | X article skill v1.2 and v1.3, driven entirely by corrections from a real article edit. Lowercase default, full template bank, clickability principles. |
| Apr 20 | Started the agency marketing dashboard plan: Google Forms + Sheets + Next.js. |
| Apr 22 | Added auto-commit and session-note hooks so work saves itself. |
| Apr 27 | Static ads skill. ICP v2.1. |
| Apr 28 | Started the wins log: a running record of real client results, each entry tagged with which post format it can feed. |

**⭐ Content angles from April**
- "I banned 12 sentence patterns from my AI writing and my content stopped sounding like AI." The voice guide bans are all real, each one added after catching it in output.
- "The skill that turned every client win into a post: my wins log." Show the actual file structure.
- "Insight beats value in cold email." The rewrite is documented with the before and after logic.

---

### May 2026 — the content taxonomy and the second account

| Date | What happened |
|---|---|
| May 11 | Repo restructure v1.2: split into ops / research / accounts. Added a DM-setting skill, a LinkedIn document-carousel skill, 17 discovery-call transcripts and 6 case-study transcripts. |
| May 19 | Weekly SOPs, voice guide pattern #9, weekly research v2. |
| May 26 | Rebuilt the long-form skill from scratch, organized **by media format** rather than by writing pattern. 9 subtypes: case study, doc screenshot, infographic HTML, video, operator stance, result+replicable, tactical tutorial, two before/after variants. |
| May 26 | Rebuilt the lead-magnet skill into 5 parameterized subtypes so it works across any account, not just one. Retired v1. |
| May 26 | Saved and dissected a competitor's auto-DM lead magnets, validated the email-gate landing page workflow. |
| May 27 | Built a short-form-from-long-content skill off real 2026 performance data, plus 6 templates. |
| May 27 | Collected 33 long-form inspiration screenshots across 8 competitor accounts, coded into 3 new format variants. |
| May 27 | Wrote the 3-step article SOP. |
| May 27 | Full strategy plan for a second anonymous X account, taken through 3 revisions to a greenlight. |
| May 27 | Built a recap system that writes per-day files and creates a Google Calendar event through MCP. |

**⭐ Content angles from May**
- "I reorganized my content system by media format instead of by writing pattern, and everything got faster." This is a genuinely good insight and nobody teaches it.
- "How I turn one long video into 6 short posts, using only formats that already won." The templates came from analytics, not from taste.
- "I screenshotted 33 competitor posts and found 3 formats I was missing." Show the folder.
- "Making a skill portable: how I stopped writing a new prompt for every account."

---

### June 2026 — measurement gets built

| Date | What happened |
|---|---|
| Jun 2 | Formalized the Monday acquisition analysis as a repeatable SOP. This is the weekly loop that turns raw exports into a decision doc. |
| Jun 3 | Case-study production SOP locked. Captured the guidance that personal posts still have to reinforce the brand's process. |
| Jun 5 | Built the first **agent** (not just a skill) for YouTube lead magnets. |
| Jun 7-9 | Built the Growthub Control Panel: Next.js dashboard, edit-in-Sheets data model, week selector, call sources page, password gate, stay-signed-in login. |
| Jun 8 | Redefined the call model: booked vs conducted, with a real qualified definition pulled from the sales team's own doc. |
| Jun 15-24 | Ran the weekly analysis for W24, W25, W26. Backfilled W21 to W24 into the dashboard so the trend was real. |
| Jun 16 | Read the paid-X data: geo and age targeting off-ICP, 0 clicks on \$250 spent. Killed the assumption. |
| Jun 24 | Built the @maurojpelle audience file from a voice-of-customer analysis of 26 Reddit threads, with canonical permalinks per quote. Then wrote the positioning off it. |
| Jun 25-29 | Made the Notion delivery page the standard lead-magnet layer. Built a content-calendar classification system with a Python generator. |
| Jun 29 | Built the ad-teardown skill (competitor ad analysis straight from transcripts). |
| Jun 30 | Started the Q1+Q2 content-to-calls dataset: the sales call log, both Calendly exports, X analytics for two profiles. |

**⭐ Content angles from June**
- "I built my ICP from 26 Reddit threads and real quotes, not from a persona template." The method is repeatable and the audience file is the proof. **This is the single best piece of source material in the whole doc.**
- "The Monday loop: how I turn 5 exports into one decision doc every week." Walk the SOP.
- "We spent \$250 on X ads and got 0 clicks. Here's what the targeting was doing." Honest failure post.
- "Booked vs conducted: the metric change that made our reporting real."
- "Skills to agents: what changed when I stopped writing prompts and started writing workers."

---

### July 2026 — analysis, extraction, and the honest findings

| Date | What happened |
|---|---|
| Jul 1 | Wrote the @maurojpelle operating baseline: 17 questions answered honestly, followed by a brutal self-assessment. Named his own pattern out loud: "I hide in building systems because it feels productive." |
| Jul 3 | Pulled and saved Lorenzo's full YouTube transcript library, 31 videos, as searchable source material. |
| Jul 6-10 | Built the bulk short-form generator (transcripts to a scheduling-tool CSV) and calibrated it through **4 rounds of corrections in 3 days**: variable length from real data, blank-line formatting, voice bans, tweets that stand alone. |
| Jul 6 | Built the daily ops focus + accountability system, live through 3 cloud routines and a shared canvas. |
| Jul 7 | Wrote 30 standalone tweets answering the exact pain points buyers typed into the booking form. |
| Jul 8 | Built a shared worklog hook: every terminal session writes to one daily worklog automatically. |
| Jul 8 | Built the weekly content loop skill, adapted from a competitor's control panel, and wired the Monday analysis to write hypotheses into Notion. |
| Jul 8 | **Finished the H1 2026 content-to-calls report.** Every finding in section 1 comes from this. |
| Jul 13-22 | Article skill v2: mega-playbook length, house structure, hand-drawn doodle image style, mandatory inline image prompts. Four rounds of taste corrections. |
| Jul 14 | YouTube process v2 locked from a real call: title decided early, delegation to the VA by Loom, HTML to Miro, target 2-3 hours per video. |
| Jul 14 | Hard rule added: YouTube ideas must be episodes of a repeatable series, never one-off videos. |
| Jul 15 | Built the client research pipeline: a 6-skill chain covering review mining, angle mining, buyer personas, competitor analysis, root-cause audience work, and ad writing. |
| Jul 15 | Logged wins with real attribution, including two bookings traced to one specific post format. |
| Jul 16 | Made lead-magnet Notion pages real nested child pages instead of one long page. Small fix, big delivery difference. |
| Jul 20-23 | Studied three competitor long-form articles that did 80k-85k views and coded the patterns into the article skill. |
| Jul 21-23 | Built a full case study from raw client data: 30-day creative export, dashboard screenshots, spend curve, individual ad records with beat maps, production specs. Annotated which results were actually attributable and which were not. |
| Jul 23 | Named and banned another AI writing pattern (the isocolon) and went back to purge it from existing records. |
| Jul 24 | Pulled acquisition call notes automatically from the meeting recorder for the first time. |
| Jul 24 | Collected 288 verbatim buyer pain answers, grouped by spend tier. |
| Jul 28 | Built the UTM tracking system and a link generator, then rejected it in practice because the links are too ugly for a bio. |
| Jul 29-31 | Built the Miro skill set: visual language, writing-for-boards rules, API gotchas. All rules extracted from corrections on real boards. |
| Jul 31 | Answered 20 questions on his own role, blockers and 90-day priorities. Then asked for 10 sharper diagnostic questions on where he is the bottleneck, because the general version was too vague to act on. |

**⭐ Content angles from July**
- **"Lead magnets are a reach weapon, not a pipeline weapon."** He publicly killed his own best-performing format after the data said it brought volume and worse leads. This is the strongest single post in the doc.
- **"We scaled content volume and lead quality fell 20 points."** 45% high-tier to 25% high-tier while bookings rose. Everyone chasing reach needs this.
- **"No single post is a booking machine."** 16 posts above 25k impressions moved bookings by 1.1. Direct contradiction of how the whole space talks.
- "I asked 95 qualified buyers what they actually wanted. One answer beat everything else combined."
- "One post, 15,000 views, 4 calls the same day. Here's why I can say that without a tracking link."
- "I built a UTM system and then refused to use it." Honest, contrarian, and shows judgment over tooling.
- "Four rounds of corrections in three days to make AI write one tweet properly." The calibration loop is the real skill and nobody shows it.
- "My AI content system is 51 files in git. Here's why version control matters more than prompts."
- "I wrote down my own biggest weakness in my own strategy doc." The operating baseline is unusually honest and that honesty is the brand.

---

### mauro-os specifically (his own brand repo, started Jul 13)

| Date | What happened |
|---|---|
| Jul 13 | Repo created by extracting brand context, skills and Claude setup out of the agency repo. |
| Jul 14 | Scrubbed every trace of agency material so all skills target Mauro's own brand. Made all hooks portable. |
| Jul 15 | Wrote the phased setup plan for you (`docs/JUAN-PLAN.md`) and a calibration backlog. |
| Jul 16 | Built the visual doc system for rendering HTML docs to images, plus a YouTube board format. Overhauled the board format after a real critique. |
| Jul 16 | Competitor YouTube research: a top-10 dig on one large agency-growth channel including thumbnails and title patterns. |
| Jul 21-22 | Organized the repo, scrubbed the agency name, moved article skills off a color that wasn't working. |
| Jul 23 | Your YouTube competitor mining research merged (9 channels). |
| Jul 24 | Set up `content/qa/` for your questions plus Mauro's transcribed voice-note answers. First topic filled: reach, virality, trendjacking, lead magnets. |

**Open items you own from this:** two unanswered questions in `content/qa/lead-magnet-qa.md` (posting time/day, and the niche in the first-line answer), and moving any questions you've collected elsewhere into `content/qa/`.

---

## 3. The systems inventory

Use this when you need to explain *what exists*. Each of these is a legitimate standalone piece of content because most agency owners have none of them.

**Content production**
- X article creator, at v2 after roughly 8 rounds of corrections
- Long-form skill with 9 subtypes organized by media format
- Bulk short-form generator, transcripts straight to a scheduling CSV
- Lead magnet system, 5 subtypes, Notion delivery pages, auto-DM distribution
- LinkedIn document carousels
- Visual doc system, HTML rendered to images
- Miro board system with its own visual language and writing rules
- 8 YouTube skills covering ideas, titles, hooks, boards, slides, brand breakdowns

**Research and inputs**
- 111 saved transcripts (competitor videos, client calls, internal trainings, discovery calls)
- 24 post studies, each decoding one high-performing competitor post into a reusable format
- 11 competitor accounts tracked with screenshot archives
- Client research pipeline, 6 chained skills
- Weekly research skill for competitor channel scanning
- Ad teardown and brand breakdown skills

**Measurement and ops**
- Monday acquisition analysis SOP, run weekly since early June
- H1 2026 content-to-calls report, 375 bookings mapped against six months of posts
- Next.js control panel with password gate and week-over-week views
- Weekly learning files with a stated hypothesis per week
- Content calendar classification system
- Daily ops system: 3 cloud routines and a shared canvas
- Automatic worklog hook across every terminal session
- Wins log tying client results to post formats

**Distribution and sales**
- Auto-DM lead magnet flow
- DM-setting playbook for a setter
- Cold-email-to-call skill
- Warm-reply calling motion on inbound replies

---

## 4. What is honestly broken or unfinished

Publish these carefully, and only as "here's what I'm still solving". They are useful because the audience is living the same problems.

1. **Input shortage is the real bottleneck.** Production is fast now. Raw material is the constraint. Ideation is the blocking step, not writing.
2. **The AI offer is undefined.** What gets sold on the AI side has never been decided, which blocks the second account's content and the booking-form routing.
3. **Attribution is timing-based, not tracked.** No per-post links. Day-level inference is the accepted proof.
4. **The second X account was greenlit in May and has shipped nothing.**
5. **YouTube is the channel Mauro dreads** because each video needs a high-quality board. The Miro skill exists to fix this and is new.
6. **@maurojpelle has no offer and almost no output.** 200 followers, 1 video, roughly one post saved since May.

---

## 5. Content bank: 20 posts you can write this week

Mapped to the three pillars in `brand/positioning.md`.

**Pillar 1: Cobbler's children (build your own inbound engine)**
1. Content produced 62% of our qualified pipeline. Cold email produced 18%. Here's the split.
2. We scaled posting volume and lead quality dropped 20 points. The data.
3. Baseline bookings, and why no single post moved them.
4. The Monday loop: 5 exports in, one decision doc out.
5. Booked vs conducted, and why the distinction changed our reporting.
6. I built a dashboard for our own acquisition before we built one for a client.
7. 95 qualified buyers, one dominant pain, in their own words.

**Pillar 2: Anti-cringe authority (post as the expert without the guru ick)**
8. Lead magnets are a reach weapon. Here's what they don't do.
9. The 12 sentence patterns I banned to stop sounding like AI.
10. Four rounds of corrections in three days to get one tweet right.
11. I built my ICP from 26 Reddit threads and real quotes.
12. My voice doc, from scratch, and how the bans got there.
13. Proof posts get 2,300 impressions and book the qualified calls. Lead magnets get 27,500 and don't.
14. I wrote my own weakness into my own strategy doc.

**Pillar 3: Low-time system that proves it converts**
15. 51 files in git is my content system. Version control beats prompt collections.
16. Organize content skills by media format, not by writing pattern.
17. Transcript to 6 posts, using only formats that already won.
18. I built a UTM system and then refused to use it.
19. Skills to agents: what changed.
20. One post, 15k views, 4 calls same day, no tracking link. The case for day-level reading.

---

## 6. Series ideas for YouTube and long-form

Per the standing rule, every YouTube idea has to be an episode of a repeatable series.

**Series A: The Agency Content Engine.** One episode per component, each one showing the real file. Voice doc, skill library, weekly analysis, lead magnet flow, Miro boards. Episode 1 is already scripted (the voice doc episode, in the Jul 24 handoff).

**Series B: Weekly Numbers.** Publish a redacted version of the Monday analysis every week. Reach, calls, qualified, what shipped, what the hypothesis is. Nobody in the agency-AI space publishes a measured loop. This is the biggest differentiation available.

**Series C: Steal My Skill.** One skill file per episode, handed over in full, with the correction history that made it work.

**Series D: I Was Wrong.** One episode per finding that killed one of Mauro's own assumptions. Lead magnets, X ads, UTM links, VA commenting, post-level attribution. There are already five episodes' worth in this doc.

---

## 7. Hard rules

1. Nothing publishes without Mauro's review.
2. Never invent a number. Bracket it and flag it.
3. Never name a client in public content.
4. Never use the agency's aggregate proof as Mauro's personal proof.
5. Articles and lead magnets are delivered in chat and are not saved to the repo.
6. Do not edit files in `skills/` without Mauro approving the exact change.
7. No em dashes. No "it's not X, it's Y". No "most brands" openers. No trailing summaries.
8. Every deliverable lands in Slack with one line saying what it is and which skill produced it.
