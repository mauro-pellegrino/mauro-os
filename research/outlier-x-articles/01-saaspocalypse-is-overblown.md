# 01. Everyone claims that SaaS is dead. They're all wrong. (the SaaSpocalypse)

> **STATUS: RESEARCH INPUT. NOT ADOPTED.** Raw capture for the outlier-article corpus. Per the process spec in
> `research/transcripts/maurojpelle/2026-08-28-how-to-save-outlier-x-articles-loom.md`: save only, no skill
> changes until the corpus is built out. Nothing here enters `skills/` without Mauro's row-by-row sign-off.

**Source account:** `@denk_tweets` (handle read off the screenshot; the body self-identifies as the CEO of beehiiv, ex-Morning Brew product and engineering lead, ex-YouTube Product Lead)
**Format:** X Article, quote-posted with a full-bleed illustrated cover
**Captured:** 2026-09-02, pasted into chat by Mauro.
**Why Mauro saved it:** the cover image and the title, explicitly. Subject matter is SaaS/tech, outside his lane. Packaging only.

## Capture completeness

| Component | Status |
|---|---|
| Title | Captured (visible headline, see note below) |
| Thumbnail | **Described, not stored.** Image file not supplied. Drop the PNG in this folder as `01-cover.png` to complete the row. |
| Text | Captured, **likely partial.** The paste ends on "aren't going to build their own CRMs either." No CTA, keyword, or sign-off in what was captured. |
| Link | **Missing.** Needs the post URL. |
| Views | **Missing.** Views are the only number used to pick an outlier, so this needs filling in. |

---

## Post-level packaging

### Card image

Black-and-white, high-contrast painterly illustration (reads as AI-generated). A Victorian/Edwardian funeral scene: six or seven mourners in period dress crowded around an open casket, faces grieving or alarmed. Sitting upright *inside* the coffin is a young man in a suit and open-collar shirt, calmly working on a MacBook (Apple logo visible on the lid). Roses and lilies banked at the base. **"SAAS" carved in large serif capitals across the front panel of the coffin.** Landscape crop, no headline overlay, no logo, no face of the author.

Card mechanics worth noting:

1. **The image states the article's whole thesis before a word is read.** The thing everyone is mourning is not dead, it is sitting up working. One frame, one gag, no argument to follow.
2. **The only word in the image is the category name.** No headline overlay, no subtitle, no author credit. The joke does not need a caption.
3. **Period-drama setting against a modern object.** The MacBook is the only anachronism in the frame and it is the punchline. The costume drama does the tonal work of "this is a funeral being held far too early."
4. **It is an argument, not decoration.** A reader who scrolls past and never opens still receives the take.

### Title

**Visible headline:** `Everyone claims that SaaS is dead. They're all wrong.`

Note: this is the headline as it appeared with the post. The X Article's own title field was not captured separately, so treat this as the headline/opener pair rather than a confirmed title string.

**Opening line of body:** "You may have heard of the SaaSpocalypse."

**Title mechanics:**

1. **Two sentences: the consensus, then a flat contradiction.** Nine words. No number, no "how to", no parenthetical qualifier, nothing promised to the reader.
2. **The second sentence is the entire hook.** "They're all wrong" is a stance with no hedge and no explanation, so the only way to resolve it is to open the article.
3. **A coined enemy word carries the piece:** "SaaSpocalypse". Named in line one of the body and used as the article's handle throughout. Coining the label for a position is what lets him attack it as a single object.
4. **The named entity is a category, not a company or a tool** (`SaaS`). Works off stance alone, no proof number in the title.
5. **It only works because the consensus genuinely exists.** The body establishes that immediately: "in the past year, the SaaSpocalypse has gone from fringe to consensus." Contradicting a belief nobody holds has no charge.
6. Sentence case, plain punctuation, no colon.

### Structural notes (observation only, no adoption call)

- **Credential is placed mid-article, not at the top.** "As for my credentials: I'm a self-taught developer. I led product and engineering at Morning Brew, was a Product Lead at YouTube, and currently run product at beehiiv." It lands immediately before the self-experiment, where it is load-bearing, rather than in the first three lines.
- **The proof is a self-experiment with a result that goes against him.** He built the thing himself and reports the cost honestly: 6 weekends, 80+ hours build, 20+ hours QA, $300/month in stitched-together infrastructure against under $100/month for the off-the-shelf option, and he is still on call for it.
- **The strongest credibility move is arguing against his own bias.** "You would expect me (the CEO of a tech company, with 50+ engineers and a huge bias towards building vs buying) to have totally replaced all of our SaaS spend." Then he lists the eleven tools he still pays for, and says he pays more than a year ago.
- **Named enemy is a person type, not a company:** "every thinkboi on X", "a small vocal minority of indie hackers who run solo teams", "they probably think that Opus is some sort of peptide."
- **Self-limiting admission is one line and early:** "I'm not betting against Anthropic (or AI), but..."
- **Borrowed compression line, attributed:** "As my COO, Dan, says: we've been able to bake bread forever. Most people still buy it."
- **Closes on a concrete absurd case, not a summary:** the person selling cowboy boots in Jackson Hole cancelling $39/month Shopify to spend 100+ hours building their own store.
- Real third parties named freely throughout: HubSpot, Shopify, Adobe, Zoom, Canva, Salesforce, beehiiv, Slack, Sentry, Linear, Loom, Zendesk, Amplitude, Ramp, Notion, Customer.io, Twilio, Resend, Vercel, Supabase, Wompi, Mindbody, WellnessLiving, Walla, Anthropic, Morning Brew, YouTube.
- One-idea-per-line-break paragraphing, almost nothing over two sentences.
- Two inline image slots inside the body, both used as a joke or as proof: "The person warning you about the SaaSpocalypse." and "Here's the MADRE landing page to vouch for that design eye."

---

## Article body (verbatim as captured)

Everyone claims that SaaS is dead. They're all wrong.

You may have heard of the SaaSpocalypse.

The thesis: with the rise of AI agents and coding tools, people and businesses are all going to build their own bespoke software, leaving these incumbent software businesses behind with an ever-diminishing customer base. That, and the rise of agentic workflows that will destroy the per-seat model that has grown so popular these past few decades.

Every thinkboi on X shares this vision, claiming that software as we know it is dead. And in the past year, the SaaSpocalypse has gone from fringe to consensus.

The markets have taken note. Shares in public SaaS companies have gotten crushed, despite many of those businesses performing arguably better than ever.

Let's look at HubSpot, for example. Over eight quarters HubSpot compounded revenue at ~20%, expanded margins nearly every quarter, went GAAP-profitable, and grew free cash flow more than 50% (hitting its 2027 margin target a year ahead of schedule).

But the stock is down ~55% from its 52-week high (bottomed out at 68%).

The market hates uncertainty. Sure, performance has been good (arguably excellent), but the acceleration of AI is so "unprecedented" that it's impossible to bet on the status quo (i.e. HubSpot remaining relevant in an AI-first world).

Betting on the SaaSpocalypse means betting on the thesis that all of these companies will soon be moot in a world where AI deploys custom software for everyone. That every SMB on earth is just one Claude Code session away from firing their entire stack, and that nobody will ever have to maintain any of it.

I'm not betting against Anthropic (or AI), but I am here to tell you that the SaaSpocalypse is totally overblown and complete bullshit.

Most of those claiming that SaaS is dead have never actually built anything at all. They aren't in the arena using the latest tools. They've never built or run a business at scale. They probably think that Opus is some sort of peptide.

> [inline image] The person warning you about the SaaSpocalypse.

Let me tell you why they're all wrong. Actually, let me take it from the very top.

Here are a few examples of SaaS companies: Shopify, Adobe, Zoom, Canva, Salesforce, beehiiv, etc. Software as a service (SaaS) is exactly what it sounds like, you pay someone to provide a service you don't have to build yourself.

When you host your storefront on Shopify, you don't need to build your own payment infrastructure, or host your own website, or think about sales tax across all 50 states, VAT in the EU, PCI compliance, chargeback disputes, or fraud.

In fact, they have a team of nearly 8,000 people who specialize in e-commerce, payments, checkout, fraud, logistics, and everything else to ensure your storefront is best positioned for success. They even routinely push updates to make the Shopify software better while you sleep.

You get best-in-class infrastructure for your online storefront, and no one on your team even thinks about it at all. From that perspective, the $39 per month you're paying Shopify feels like a steal. That's the beauty of SaaS.

We can use beehiiv as an example too. Technically, anyone has been able to build their own email infrastructure for decades. The same way anyone could build their own storefront for e-commerce. AI just makes it easier, and puts it within reach of people who aren't technical.

With the help of AI, sure, you could spend thousands of dollars and several months building your own email platform and have your own (much worse) version of beehiiv, custom-built just for you.

But when your team needs to integrate the newsletter with your podcast, or send dynamic content to your readers, or have access to enriched audience data, you'll need to go back to the well and have someone on your team build these features themselves.

When you want to monetize your newsletter, whether with ads or subscriptions, you'll need to build your own sales pipeline, reporting, user authentication, payment rails, renewal logic, customer alerts, and more.

When your emails start to land in spam, your team is now solely responsible for figuring out email deliverability all on their own.

And remember, replacing SaaS and building the software yourself isn't free. You still need to pay for the infrastructure, servers, maintenance, monitoring, and the other software and plugins required to make it all work. Not to mention the added human capital required to build and manage everything (indefinitely).

So after all of the time, money, and labor required to build a worse version of beehiiv, you're now stuck having to maintain and update it all on your own forever. Or, hear me out, you could pay a small premium to have 130 specialists own all of that for you. That premium comes with regular software updates, access to the latest tools, uptime guarantees, and a team of experts in email deliverability and creator tools who can help you whenever you need it.

That's the crux of the SaaSpocalypse debate. And there's a small vocal minority of indie hackers who run solo teams claiming that everyone is going to build their own software just because it's now technically possible.

If that were true, you would expect me (the CEO of a tech company, with 50+ engineers and a huge bias towards building vs buying) to have totally replaced all of our SaaS spend. But we still happily pay for Slack, Sentry, Linear, HubSpot, Loom, Zendesk, Amplitude, Ramp, Notion, Customer.io, etc. In fact, we pay considerably more for these today than we did just a year ago.

As my COO, Dan, says: we've been able to bake bread forever. Most people still buy it.

Meanwhile, I'm not just yapping from the peanut gallery talking hypotheticals either. I'm in the arena. I've done the work myself.

Last week, I announced that a few friends and I launched a social wellness club in Medellin. It's called MADRE, and it's home to the largest sauna in all of Latin America. (By the way, if you live there you should book a session. And if you don't live in Medellin, you should follow us on Instagram).

We could have used Mindbody, WellnessLiving, Walla, or any of the other platforms to manage bookings and memberships. It would have cost less than $100 a month and been ready to use in a few hours. SaaS baby.

But out of curiosity, watching this whole vibe coding movement from the sidelines on X, I wanted to take advantage of the opportunity to get my hands dirty and build it myself.

As for my credentials: I'm a self-taught developer. I led product and engineering at Morning Brew, was a Product Lead at YouTube, and currently run product at beehiiv. I've built a lot of software, and I think I have a decent eye for design.

> [inline image] Here's the MADRE landing page to vouch for that design eye.

Keep all of that in mind as I explain what happened next.

I spent about 6 full weekends, I'd estimate maybe 80+ hours, building this website and platform from scratch. I probably spent another 20+ hours doing QA to ensure everything works perfectly.

I had to build custom integrations with Twilio, Resend, Customer.io, Vercel, Slack, Sentry, Supabase, and Wompi (a local payment provider in Colombia). Yes, pay for and configure each of those individual accounts as well. I built an admin portal so our managers can run the business. I had to purchase datafonos (payment terminals) to build and test the physical payment infrastructure.

I also had to create user guides and tutorials to hand off to the team so they could learn and operate the software on their own.

And that's just the upfront investment. When the staff provided feedback, I had to build new features to support their requests. I also have Sentry errors piping into Slack to alert the team whenever there's an issue with the platform.

As for who has to update and fix the software when it's broken? That's on me. But I have a full-time job running beehiiv and don't have the bandwidth to do that outside a couple of hours here and there on the weekends (uh oh).

Add up Twilio, Vercel, Customer.io, Sentry, Resend, and Supabase and we're paying multiples more than what a SaaS company would charge to handle all of it for us. And that SaaS company would be improving the product, watching it for problems, and answering the phone when something breaks.

For the low, low price of $300 per month, and hours of my life I'll never get back, we have a fully custom-built solution that we can edit and tweak however we'd like.

Remember my credentials? I've led product and engineering at multiple startups and it still took me a hundred hours. Hell, I'm still technically on-call to support it.

Do you think the average person selling cowboy boots in Jackson Hole is going to cancel their $39 per month Shopify subscription to spend 100+ hours building their own store, and then hire someone to manage it forever?

Of course not. And the millions of small businesses paying for Salesforce aren't going to build their own CRMs either.

*[capture ends here. Remainder of the article, CTA and sign-off not captured.]*

---

## Lane note

Every number in this file is first-party to that account and about SaaS economics. They are **theirs**, never Mauro's, and never borrowed into his content. The subject does not port. What is being saved here is the cover-image convention and the title device.
