# Lead Magnet Skill: Insight Model

**Version:** 1.0 (14 Aug 2026)
**Status:** The second of two magnet models. The first is `skills/lead-gen/lead-magnet/` (the value model). Both are live. Pick one per magnet, never blend them.
**Derived from:** the JK Molina library at `research/jk-molina/`, synthesised in `research/jk-molina/synthesis.md`. Adapted to Mauro's ICP. All of JK's numbers stay labelled as his.

---

## Which model to use

| | Value model (`lead-magnet/`) | Insight model (this file) |
|---|---|---|
| **Gives** | The answer, in full | Proof that you have the answer |
| **Bar** | $100 of work they didn't do | The least that makes the gap real |
| **Reader leaves** | Able to do it themselves | Wanting you to do it |
| **Best for** | Warm audience, people who already paid, existing clients | Cold audience, people who have given you $0 |
| **Risk** | They implement without you | They feel teased and disengage |

**The gate, one question:** has this person given you more than $0?

- **No** → insight only.
- **Yes** → insight plus value.

JK's evidence for the split: two value-based videos produced 0 clients, one insight video produced 5. His data, his account.

**Mauro's ICP caveat, read before adopting this wholesale.** Lorenzo rejected the insight approach for a similar buyer in Oct 2024: established operators want to save time more than money, so withholding the how can read as friction rather than intrigue. The insight model earns its keep on cold reach. On a warm agency owner who already trusts you, the value model usually converts faster. When unsure, use the value model.

---

## Required reading

Before drafting: `brand/voice.md`, `brand/audience.md`, `brand/positioning.md`.

---

## The ladder this magnet sits inside

**Followers → Leads → Customers → Core Clients → Top Clients**

The insight magnet's job is the second arrow: turning a follower into a lead who is worth talking to. Its second job is setting up the third arrow, the small paid offer that creates a **customer**.

The step almost everyone skips is Leads → **Customers** → Clients. Going straight from a free asset to a high-ticket install is a jump most won't make. A customer who paid $100 is a materially better prospect than a lead who paid nothing.

**Blocked today.** The customer tier needs a way to take payment and a way to deliver. Mauro has neither. Until that exists, this model stops at "qualified lead in the DMs" and the next step is a conversation, not a checkout.

---

## What goes in an insight magnet

**Structure:** 3 to 5 pages. Shorter than the value model on purpose.

| Page | Contains |
|---|---|
| 1 | The problem, named precisely, with why it's happening |
| 2 | The mechanism. Why the common approach fails and where to look instead |
| 3 | Proof it worked. Real screenshots, real numbers, from the engine you run |
| 4 | What this means for their agency specifically |
| 5 | The next step. A conversation, or the small offer when one exists |

**What it deliberately withholds:** the step-by-step, the paste-ready prompts, the fill-in templates, the complete rule set. Those belong to the value model.

**What it must never withhold:** the truth. Insight means showing the real mechanism, and stopping before the implementation. Vagueness dressed as mystery fails immediately with this ICP.

**The test before shipping:** a reader should finish it able to explain *why* their inbound isn't working, and unable to build the fix this week without help. If they can build it, it's a value magnet and should be labelled as one.

---

## The three insight post types

Every post and every magnet page is one of three, run through the same frame:

**What → Why → Where → Bridge**

| What | Why | Where |
|---|---|---|
| **Problem** | Why is this problem happening to you? | Where to look to get rid of it |
| **Outcome** | Why did this outcome happen? | Where to look to create a similar one |
| **Idea** | Why does this idea benefit you? | Where to look to get its benefits |

The bridge changes by channel. On X and LinkedIn: a reply, a DM, a follow. In email: a booking, a buy, a reply.

**Sourcing them.** Collect, don't invent. The best material is the work already done. Mauro's sources: the weekly acquisition analysis, the skills he builds, the Miro boards, what broke and got fixed. Log raw one-liners as they happen and pick the one that shines brightest when it's time to write.

---

## Packaging: Tool plus Promise

**The Tool** is the proprietary name. Capitalize it, name it like a tool in a toolbox, reuse it until other people say it back to you. That last part is the test for whether an idea is actually a Big Idea.

**The Promise** is what they get, and it has to pass the **Meaning Test**: show it to two people and it means the same thing to both.

| Fails the test | Passes |
|---|---|
| Transform your agency's marketing | Book 3 calls from content next month |
| Build a real personal brand | Turn one client call into a week of posts |
| Master AI for your agency | Cut content production to 1 hour a week |

**Magic Pill:** the wrapper matters as much as the thing. JK's example: "Waitlist" sold 9 copies, "The 90 Days Of Offers Swipe File" sold 117. Same category of asset.

Always propose 3 title options. Never ship one without alternatives.

---

## The post and the DM

The post structure from `lead-magnet/_master.md` still applies (hook, setup with a credibility specifier, bullets, keyword CTA, "must be following"). Two differences:

**The bullets name the gap, not the deliverables.** The value model's bullets promise things received. The insight model's bullets promise things understood.

- Value bullet: "10 paste-ready prompts with variable slots"
- Insight bullet: "Why your posts get impressions and no replies"

**The DM opens a conversation.** The value model's DM hands over the asset and adds a P.S. The insight DM hands over the asset and asks a question, because the reply is the point.

```
Hey (name), here's the breakdown:

LINK

Page 2 is the one to start on. What's your current setup for turning
client work into content?
```

The question is the whole mechanism. A DM that only delivers a file ends the conversation the moment it lands.

---

## Scarcity, urgency, cycling

JK runs offers on 1-2 week cycles with a hard close, plus daily front-end offers and weekly back-end offers. That cadence assumes full-time attention.

**Scaled to 5-7 hours a week:**

- One magnet live at a time, cycled every 2 to 3 weeks
- Every cycle has a real closing date, even a soft one ("I'm taking this down Friday")
- Never evergreen. An asset that's always available stops being worth claiming
- Recycle a winner after 8 to 12 weeks with a changed hook rather than building a new one

The fatigue data in `lead-magnet/_master.md` (7,839 → 901 across five DMs in six days) is the same finding from the other direction. Rotate the shape, don't cut the volume.

---

## What this inherits, unchanged

Do not duplicate these. Load `skills/lead-gen/lead-magnet/_master.md` for:

- Voice rules and the pre-publish checklist
- LeadShark configuration (Auto-connect OFF, Partially Engage ON, Follow-up DM OFF)
- The Notion delivery build, including the rule that every section is a real nested child page
- Cover image spec (screenshot the asset's own home page)
- The X and LinkedIn post skeletons
- Token resolution for `{{calendly_url}}` and `{{linkedin_full_name}}`

---

## Blockers before this model can run end to end

1. `{{calendly_url}}` does not exist. The next step has to be a DM reply until it does.
2. No payment processor, so the customer tier is unavailable.
3. No email platform or landing page, so the lead is captured in the DMs rather than on a list.
4. `brand/social-proof/` and `brand/wins-log.md` do not exist, so page 3 (proof) has to be sourced live from Mauro each time.

None of these block a first insight magnet. All of them cap it at "conversation started."

---

## Anti-patterns

- Withholding the mechanism instead of the implementation. That's teasing, and this ICP leaves.
- Running the insight model on someone who already paid you. They earned the value version.
- Naming a Tool nobody repeats back. If it isn't in someone else's sentence after a month, rename it.
- A promise that fails the Meaning Test.
- Using JK's numbers as proof. They are his, from his account, and none of them are cleared.
- Blending the models in one asset. A magnet that half-explains and half-teaches reads as an unfinished value magnet.
- Building this before checking whether the value model would convert that specific reader faster.
