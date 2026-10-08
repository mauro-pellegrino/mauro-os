# Whop product v1: one system, one close date

Built 2026-10-08. Reads with `content/plan/ownership-inventory.md`, `content/plan/jk-molina-review.md`
and the sales page draft `content/plan/whop-product-v1.html`. Nothing here is decided. Every open
choice is a `[NEEDS]`.

---

## The pick: outlier to template intake

**One system: the outlier to template intake.** It scores other accounts' posts against their own
median, saves each outlier as a template, and runs the templates on a weekly loop.

Why this one, in JK's terms:

- **His first move names it.** "Get a written yes from the agency on the outlier-to-template system. Fix it ... and put it on Whop with a close date" (`jk-molina-review.md`, last section, our reading).
- **It is the only system with a stranger test.** The LI1 card (review queue, 2026-10-08) loaded the intake sheet in headless Chrome with no repo. It works after two number fixes.
- **The free part and the paid part are already split.** The LI1 card says a stranger gets steps 1 to 3 (score, capture, prompt). Steps 4 to 10 have "nothing behind them" for him. JK: "Give them 1. Then sell the workshop with the other 10." (`1000-new-whales.pdf` p10). The free sheet is the 1. The paid kit is the rest.
- **Approved posts already teach it.** X7 "the outlier rule" (Tue 20 Oct) and X8 "templates live in a doc" (Wed 21 Oct) are APPROVED (`review-queue/decisions/2026-10-08-v2.txt`, lines 53-54).
- **His own top keywords fit.** On @maurojpelle, posts about skills, prompts, articles, code and agents go up. Posts about "ai", "voice" and "write" go down to 0.3x (`tools/x-keywords.py`, 8 Oct).

**The blocker: ownership is mixed.** The scorer landed in growthub-os on 2026-10-02, two days before
mauro-os. The method comes from Mauro's own Loom of 2026-08-28. Full evidence:
`ownership-inventory.md`, row 5. `[NEEDS: a written yes from the agency to sell a rebuilt, generic version]`

**Fallback if the agency says no: the Gate kit.** The growthub-os copy says "Modelled on the mauro-os
Gate" (`growthub-os/.claude/agents/gate.md` line 11). The kit is the Gate agent, the hook, the
rejections log and the claims file, plus the voice extraction method. Two parts stay out:
`anti-slop-protocol.md` (Ronin's public protocol) and `brand/voice.md` (a fork of the agency's). The
demand signal is weaker: his "voice" and "write" posts sit at 0.3x.

**v2 candidate: the ASCII visuals kit.** It has the cleanest ownership of all (growthub-os calls
mauro-os `render.py` by path). It has no stranger test yet.

**Out: the $500 lead magnet system of 22 Aug** (`ACTIONS.md`). Its skills have growthub-os twins, its
proof comes from the agency account, and its delivery is comment-to-DM, which stopped after the X
automation bans.

---

## Name options

No "ghosted" in any of them.

1. **Outlier Intake**: the name of the system as it runs today. Plain, and it says what it does.
2. **The 3x Rule**: the rule at the centre (3x the account's own median = an outlier). It matches X7.
3. **Template Bank**: names the output, a store of templates that runs the weekly posting.
4. **Own Median**: names the one idea that makes it different. A post is scored against its own account, never against yours.

`[NEEDS: Mauro picks the name]`

---

## What the buyer gets

### Files

| File | What it does | Exists today? |
|---|---|---|
| `template-intake.md` (Claude Code skill) | The 10 steps: profile, outliers, capture, type, score, dedupe, save, route, week pick, Monday retire | Yes, mauro-os. Generic rewrite needed (ownership) |
| The scorer | Median, ratio, verdict, floor, for many accounts from one CSV | Yes (`tools/outlier-score.py`). It crashes on "12.4K" (LI1 card). Rewrite needed |
| The intake sheet | Browser page: paste posts, get the score, the capture checklist and the Claude prompt | Yes (`content/lead-magnets/outlier-to-template-intake/index.html`). This is the free part |
| `tracked-profiles.csv` | The list of accounts to check, with a source per row | Yes, 13 rows. Ships blank plus a how-to-fill note |
| `post-templates.md` (the templates store) | Shape, rules, the original's numbers, the process it routes to, status | **No.** `research/post-templates.md` does not exist in mauro-os yet. Build one with real templates from public outlier posts |
| `post-tags.csv` + README | One row per post built from a template, read on Monday to keep or retire it | Yes (`content-log/`) |
| Install README | What you need, how to start, one worked example | **No** |

### Setup

The buyer needs Claude Code for the skill. The intake sheet runs in any browser.
`[NEEDS: delivery: private repo, zip, or Whop files]`

### Looms to record

| # | Loom | Length |
|---|---|---|
| 1 | Install: put the files in a repo and run the first command | [NEEDS] |
| 2 | Pick the accounts: fill `tracked-profiles.csv` | [NEEDS] |
| 3 | Score one account live and read the verdict | [NEEDS] |
| 4 | Capture a batch: text, screenshot, link, numbers | [NEEDS] |
| 5 | Save a template and dedupe it against the store | [NEEDS] |
| 6 | Route a template to a process and pick the week's 3 to 5 | [NEEDS] |
| 7 | Monday: keep or retire each template from the post tags | [NEEDS] |

The 2026-08-28 Loom (`research/transcripts/maurojpelle/2026-08-28-how-to-save-outlier-x-articles-loom.md`)
is the base script for Looms 3 and 4.

### Access

JK puts files with no access in his weakest tier: "No access to you (maybe 1 team member).
Monetizes fish. Reduces churn. But rarely serves as an upsell." (`servant.pdf` p3). So v1 carries
one piece of access. Options: one live group install call per cohort, or one async thread where
Mauro answers for the open window. `[NEEDS: Mauro picks the access]`

---

## Who it is for, and not for

**For:**
- An agency owner who posts on X or LinkedIn and runs Claude Code, or has someone on the team who does.
- Someone who copies formats now by feel and wants a rule for which posts are worth copying.
- Someone who wants the system in their own repo and wants to own it.

**Not for:**
- Someone who wants posts written for them.
- Someone with no posting habit yet (the system feeds a weekly posting slot).
- Someone who wants a video course to watch.
- Someone who needs a Growthub-style done-for-you service. That is Agency Booked Calls.

---

## Price options

| Option | Price | Reasoning | Source |
|---|---|---|---|
| A | $49 one-time | Matches the Claude skill packs on sale now. It also puts the product next to bundles of 2,000 skills for $19 | Better with Claude, $19 rising to $39 ([betterwithclaude.com](https://www.betterwithclaude.com/skills)). SAP pack of 50 Claude Code prompts, $49 one-time (search result, 2026) |
| **B** | **$100 founding, one-time, then a higher price after [NEEDS] buyers** | JK's customer step. Small enough for a first payment. The founding price rises at a buyer count, the way Camilo's group did | "By asking them to give you a small amount first, say $100" (`the-customer-funnel.pdf` p2). "What thing worth $100 can I sell this week that I know will sell?" (p8). Camilo: $47 founding, $99 after 500 members ([aifunnelinsider.com](https://aifunnelinsider.com/ad-creators-lab-review-2026/)) |
| C | $297 one-time, with the live install call | The top of JK's workshop band. A Whop content course sells lifetime access at this price | "Workshops: $9 to $300." (`pricing.pdf` p9). Social Growth Premium: "$49.99/month or $297 lifetime" ([whop.com/blog/top-social-whops](https://whop.com/blog/top-social-whops/)) |

**Lean: B.** JK measures a customer offer on the clients it finds, not on its own revenue: "Unless
you have a big audience, the Customer Funnel probably won't make you more money than your clients."
(`the-customer-funnel.pdf` p3). At 19 follows in four months, the job of v1 is to make buyers who
then take Agency Booked Calls ($200 a week x 4, `research/jk-molina/cashie-studio/offer/agency-booked-calls.md`).
Option A puts it next to commodity packs. Option C asks a stranger for $297 before he has paid
anything.

**The 22 Aug anchor.** `ACTIONS.md` set $500 one-time for the lead magnet system. That was a
bigger product with 9 pages. It does not carry over to one system.

**Whop fees.** 2.7% + $0.30 per card sale, plus $0.10 for fraud checks and 3D Secure, no platform
fee as of 20 Aug 2026 ([ruzuku.com](https://www.ruzuku.com/learn/articles/whop-pricing)). Affiliates
take 30% by default when one sells it. At $100 the net is about $96.90 before payout fees.

**The goal.** The brief sets $10K/month across Growthub and Ghosted Calls. `brand/vision-2026.md`
sets $5k/mo for Ghosted Calls by 31 Dec 2026. At $100, $5k needs 50 buyers in a month. With 19
follows credited to posts from 26 May to 5 Oct, v1 cannot carry that alone. `[NEEDS: which goal is current]`

`[NEEDS: Mauro picks the price]`

---

## What must be built or cleaned before launch

| # | Item | Done when | Owner |
|---|---|---|---|
| 0 | Agency yes for row 5 of the inventory | Written answer, dated, in `ownership-inventory.md` | Mauro |
| 1 | Rewrite the scorer from scratch, generic | "12,400", "12.4K" and "1.2M" give the right median. 0 lines shared with the growthub-os file | Claude |
| 2 | Generic `template-intake.md` | A search for /Users/mauro, growthub, the agency's people and private/ returns 0 | Claude |
| 3 | The templates store with real entries | `post-templates.md` with [NEEDS: count] templates, each from a public outlier with its numbers | Mauro + Claude |
| 4 | Intake sheet fixes from LI1 | Ratio and Verdict readable at 390px. The page says the floor can be changed | Claude |
| 5 | Install README | One page: needs, start, one worked example | Claude |
| 6 | Stranger test of the full kit | One person outside the repo installs it from the README with no help. `[NEEDS: who]` | Mauro |
| 7 | 7 Looms | Recorded, linked in Whop | Mauro |
| 8 | Whop page | Product, price, close date, access option, the higher option (Agency Booked Calls) at checkout | Mauro |
| 9 | Delivery | `[NEEDS: private repo, zip or Whop files]` | Mauro |
| 10 | Public URL for the free sheet | The LI1 card names it as the ship blocker | Mauro |

JK on the higher option: "Include A Higher Access Option" (`the-customer-funnel.pdf` p9).

---

## The 14-day launch plan, driven by @maurojpelle posts

Rules for the window, from the data and JK:

- **No comment-to-DM and no autodm CTA.** The X automation bans ended that channel (Wiz call, 2026-08-28). The posts point to the Whop page in bio.
- **Replies and bullet stacks carry the traffic.** Replies earned 0.63 follows per 1K impressions, bullet stacks 0.42, bare-link article drops 0 on 11,993 impressions (`tools/maurojpelle-traffic.py`, 26 May to 5 Oct).
- **One offer mention a day**, in a post, a reply or a DM. "Make a Front End offer every day." (`the-offer-shell.pdf` p11)
- **A cap and a close date.** "Make sure to have a cap and a deadline. Typically I run 3-7 days." (`the-customer-funnel.pdf` p16). The cart is open 5 days.

Day 1 = `[NEEDS: open date]`. One option: put days 1 to 3 on 19 to 21 Oct, so the approved X6, X7,
X8 and LI3 fall into the warm-up. That works only if items 0 to 6 above are done by 18 Oct.

| Day | Phase | X | LinkedIn | Offer mention |
|---|---|---|---|---|
| 1 | Warm-up | X6 long form: the monday diary (approved) | | Waitlist line under the post |
| 2 | Warm-up | X7 short: the outlier rule (approved) | LI3 step-by-step: mapping one process (approved) | Reply to the top comment with the waitlist |
| 3 | Warm-up | X8 long form: templates live in a doc (approved) | | Waitlist line |
| 4 | Warm-up | Bullet stack: one template from the store and its numbers [NEEDS: draft] | | DM to everyone who replied on days 1 to 3 |
| 5 | Warm-up | Bullet stack: a template retired on Monday and why [NEEDS: draft] | Free intake sheet post (LI1 after fixes) | The sheet's last screen points to the kit |
| 6 | Warm-up | Replies only, under large agency-owner and AI-content accounts | | 1 reply mention |
| 7 | Warm-up | Reply day | | Waitlist count post `[NEEDS: real count]` |
| 8 | **Open** | Open post: what the kit is, the price, the close date | Same post, LinkedIn version | The post itself |
| 9 | Open | Bullet stack: the 10 steps in one list | | 1 reply mention |
| 10 | Open | Article drop with the Whop plug under it | LinkedIn post: who it is for and not for | The plug |
| 11 | Open | Bullet stack: one Loom still with what it shows | | DM to waitlist |
| 12 | Close | Last-day post: closes tonight | Same | The post itself |
| 13 | Closed | Reply day | | Buyer follow-up: "What's your focus?" |
| 14 | Closed | Monday read: offers made, buyers, buyer emails | | Offer Agency Booked Calls to buyers (cap and deadline) |

Day 14 follows JK's buyer path: "When Joining: Welcome. What's your focus so I can point you in the
right direction?" and the credit offer to the next tier (`the-customer-funnel.pdf` p16). Every post
in the window goes through the `gate` agent before Mauro sees it.

---

## Camilo Castañeda's community playbook

**Research only, not adopted** (`CLAUDE.md` section 7). Camilo's numbers are his.

What he runs: **Ad Creators Lab** on Skool, "The AI ad creative lab for ecom brands, media buyers &
editors", next to his agency **Epic Ads Lab** ([epicadslab.com](https://www.epicadslab.com/)).
"$99/month", "$83/mo for life with yearly", 1.1k members, "Weekly live ad reviews", "Static ad
templates", "Make your first AI ad in 24 hours"
([skool.com/adcreatorslab/about](https://www.skool.com/adcreatorslab/about), fetched 2026-10-08).
A review site gives the price path: $47 founding, $99 "once membership crossed 500", and a yearly tier
with "monthly 1-on-1 calls with Camilo and weekly ad-account audits"
([aifunnelinsider.com](https://aifunnelinsider.com/ad-creators-lab-review-2026/)). Another review
shows an earlier snapshot: "$47/month", "889" members, "4 events/month", "< 24h response time"
([skoolmakers.com](https://skoolmakers.com/communities/ad-creators-lab/)). The two reviews disagree
on the dates. The repo note of 20 Aug says "$77/mo" with no source
(`research/jk-molina/cashie-studio/offer/agency-booked-calls.md` line 152): treat it as stale.
Acquisition: ad teardowns on X (@Camicees, per aifunnelinsider) and the Skool Games winner badge.

| Mechanic | Verdict | Reason |
|---|---|---|
| Sell the system the agency runs for clients | **Adapt** | Same shape, but Mauro sells only what the agency says is his (inventory). Camilo owns his agency; Mauro does not |
| Founding price, raised at a member count | **Adopt** | Fits option B. A rise at a stated count gives a real reason to buy now |
| Weekly live roast | **Adapt** | Mauro wants low ongoing time. Make it an async roast thread during the open window, one batch of templates reviewed per buyer |
| $99/mo recurring | **Reject for v1** | Mauro asked for one payment. `ACTIONS.md` (22 Aug): recurring needs modules arriving, weekly corrections and a live element, and none exists |
| Yearly tier with 1-on-1 calls | **Adapt** | This is JK's higher access option. For Mauro the higher option is Agency Booked Calls |
| Vetted editors and creators directory | **Reject** | Ad creative is the agency's lane (`CLAUDE.md` section 1) |
| Teardowns on X as the top of the funnel | **Adopt** | Matches what earns Mauro follows: replies and bullet stacks on real systems |
| "First result in 24 hours" promise | **Adapt** | A plain promise for v1: one scored account and one saved template in the first session. `[NEEDS: Mauro confirms the promise]` |
| Skool as the platform | **Reject** | Mauro picked Whop (`ACTIONS.md`, 22 Aug) |

---

## Sources

- JK Molina PDFs in `research/jk-molina/`: `servant.pdf` p3, `the-customer-funnel.pdf` p2, p3, p8, p9, p16, `the-offer-shell.pdf` p11, `pricing.pdf` p9, `1000-new-whales.pdf` p10.
- [Ad Creators Lab, Skool about page](https://www.skool.com/adcreatorslab/about)
- [Ad Creators Lab review, aifunnelinsider](https://aifunnelinsider.com/ad-creators-lab-review-2026/)
- [Ad Creators Lab review, skoolmakers](https://skoolmakers.com/communities/ad-creators-lab/)
- [Camilo Castañeda, Skool profile](https://www.skool.com/@camilo-castaneda-6831)
- [Epic Ads Lab](https://www.epicadslab.com/)
- [Whop pricing and fees 2026, ruzuku](https://www.ruzuku.com/learn/articles/whop-pricing)
- [Top social offers on Whop, whop.com blog](https://whop.com/blog/top-social-whops/)
- [Better with Claude, skills bundle](https://www.betterwithclaude.com/skills)
