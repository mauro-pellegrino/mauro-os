# Offer 2: The Lead Magnet System — $500 one-time

**Filed 18 Aug 2026.** Mauro's words when sending the cashie chats: *"will be mostly focused for sending them the lead magnet system for a one payment of 500$."*

**Type:** One-time self-serve asset. The cheap first yes.
**Status:** the product does not exist yet as a thing anyone can receive. Build plan below.

---

## Why two offers, not one

| | Offer 1 | Offer 2 |
|---|---|---|
| Name | Agency Booked Calls | The Lead Magnet System |
| Type | Client offer | Customer offer |
| Price | $200/week x 4 | $500 one-time |
| They get | Weekly call, Slack, done-with-you | The system, self-serve |
| Spots | 1 | Unlimited |
| Job | Revenue and a case study | Create a customer |

The $500 asset is the cheaper yes. Someone buys it, uses it, and the next conversation starts from "you already paid me once" instead of cold. Someone who has paid you is a better prospect than someone who has only read you.

It also fits the ICP. They already make good YouTube videos, X and LinkedIn are solid or dormant, they want to set the system up themselves. Self-serve is what they asked for.

---

## Where the hell is the thing

Right now, nowhere. That is the honest answer and it's the reason it isn't worth $500 yet.

What exists:
- `skills/lead-gen/lead-magnet/` — 7 files, 1,652 lines, internal, written for Claude to read
- `brand/lead-magnets/shareable/lead-magnet-system.md` — 254 lines, one file, cleaned for handing out

Neither is a product. A buyer would receive a markdown file and no way to run it.

## What it becomes

**A duplicable Notion workspace.** One link. They hit Duplicate and it's theirs.

Notion because he already builds magnets there, the delivery-page prompt already targets it, duplication is native, and it costs nothing.

Six sections, each a real nested page:

| Page | Contains | Exists? |
|---|---|---|
| 1. Start Here | What you need before you begin, what comes out, how long it takes | No |
| 2. The Rules | The title formula, the $100 bar, structure, images, cover, fatigue, measurement | Yes, in `shareable/` |
| 3. The Prompts | Every prompt written out, paste-ready. The ones currently ending in `...` | No |
| 4. The Worked Example | One magnet built start to finish, every page shown | No |
| 5. The Scoring Sheet | Fill-in: title against the formula, page count, does each page have a fill-in, does each image add or restate, verdict | No |
| 6. The Delivery Kit | Post template, DM template, LeadShark config, cover spec | Yes, in `_master.md` |

Two of six exist. That is the gap between a reference doc and a $500 product.

**The scoring sheet matters more than it looks.** The system's own rule says a magnet must be a thing you fill in, not a thing you read. Right now the system breaks its own rule. Page 5 fixes that.

---

## Payment

**Manual invoice, decided 21 Aug.** Not Stripe links, not Whop, not Gumroad, not Skool.

At one buyer arriving through a DM, an invoice is the whole payment system. Revisit a payment link at the third buyer, when sending invoices by hand starts costing more than the setup would.

At one-to-ten buyers arriving through a DM conversation, a storefront adds nothing. He sends a link, they pay, he shares the Notion duplicate link. Manual delivery is fine at this volume and takes thirty seconds.

| Option | Cost | Verdict |
|---|---|---|
| Stripe payment link | 2.9% + $0.30 | **Use this.** No monthly fee, no storefront to maintain |
| Whop | 3% + 2.7% + $0.30, up to 30% via their marketplace | Later, if he wants discovery and a real storefront |
| Gumroad | ~10% | Worse economics for the same job |
| Skool | $99/mo | Wrong tool. Community-first, and he has no community |

Revisit Whop once there is a second paid asset and repeat buyers.

---

## Build order

Nothing here needs new invention. It needs assembly.

| # | What | Owner | Blocked by |
|---|---|---|---|
| 1 | Run the system end to end on one real input | Juan | A test target |
| 2 | That run becomes page 4, the worked example | Juan | Step 1 |
| 3 | Write out every prompt that currently ends in `...` | Juan writes them as he needs them, Mauro reviews | Step 1 |
| 4 | Log every place the docs were unclear | Juan | Step 1 |
| 5 | Page 1, Start Here, written from Juan's gap log | Mauro | Step 4 |
| 6 | Page 5, the scoring sheet | Mauro | Nothing |
| 7 | Assemble all six into Notion, set the duplicate link | Mauro | Steps 1-6 |
| 8 | Brand colour picked, applied to every page | Mauro | Nothing |
| 9 | Stripe payment link created | Mauro | Nothing |

Steps 6, 8 and 9 are unblocked today and take under an hour combined.

The brief for steps 1-4 is at `docs/juan-lead-magnet-test-brief.md`.

---

## Is it worth $500 once built

Yes, and the reason is the evidence, not the rules.

The rules are good but a competent operator could reconstruct most of them. What can't be reconstructed: 40 magnet posts with view counts and comment rates, seven titles shown as rejected and then shipped, and the fatigue curve (7,839 down to 901 across five DMs in six days). That is what someone pays for. Nobody publishes their losers.

**Constraint:** that evidence is from an account Mauro runs, not from his own. It ships unnamed, phrased as it already is in `_master.md`. His own numbers replace it as they accrue.

---

## Open

- Does the $500 buyer get any access to Mauro, or is it purely self-serve? Purely self-serve is cleaner and protects the $200/week tier.
- Is there an upgrade path priced in, for example $500 credited against the first month of Offer 1.