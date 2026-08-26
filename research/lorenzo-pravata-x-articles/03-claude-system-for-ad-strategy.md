# 03. the Claude system we built to generate ad strategy for ecom brands (full breakdown)

> **STATUS: RESEARCH INPUT. NOT ADOPTED.** Raw source capture. Nothing here enters `skills/` without Mauro's row-by-row sign-off.

**Source account:** @lorenzo_pravata (an account we run, per attribution resolved 2026-08-25). Never name it in public-facing content.
**Format:** X Article, quote-posted with a designed title card
**Captured:** 2026-08-26. Part of the "top 10 articles that booked the most calls" set.

## ⚠️ This article was posted twice. It is the only repeat in the set.

Identical title, identical body, identical card image. Posted 4 Apr 2026, then again 27 Jul 2026, 16 weeks apart.

| | **Run 1 — 4 Apr** | **Run 2 — 27 Jul** | Change |
|---|---|---|---|
| Impressions | **15,000** | 2,500 | **-83%** |
| Likes | 69 | 25 | -64% |
| Replies | 7 | 2 | -71% |
| Reposts | **13** | 1 | **-92%** |
| Like rate | 0.46% | **1.00%** | +117% |
| Repost rate | 0.087% | 0.040% | -54% |

**This is the most useful data point in the entire set,** because it is the only controlled comparison available: same asset, same account, same card, two dates. Everything that differs is timing and audience state.

What it says:

1. **Re-running an article is a real practice on this account,** not an accident. The set of "top 10 articles that booked calls" contains the same article twice, which means both runs booked calls.
2. **The second run reached 17% of the first run's audience but engaged them harder.** Like rate more than doubled. A much smaller, much warmer pool saw it.
3. **Reposts collapsed almost completely (13 → 1).** Reposting is the discovery mechanic. On run 2 the article had already been shared by the people who would share it, so it had no route out to new audiences and settled onto the existing followers.
4. **Reach and engagement rate move in opposite directions on the same asset.** This kills any remaining case for using like rate to rank posts. Run 2 looks better on the dashboard metric and is worse on every outcome that matters.

**Correction to the earlier read on this article.** When only the July run was visible, this looked like a low-reach, high-engagement article, and I read that as a smaller but more engaged audience finding it. That read was measuring a repost, not the article. The article's actual first-run performance is 15K impressions and 13 reposts, which puts it **second only to article 08 (25K)** and well above article 06 (12K). It is one of the strongest articles in the set, not the weakest.

---

## Post-level packaging

- **Card image:** a designed title card, no screenshot and no product. Cream background, large orange Claude asterisk on the left, serif headline right: **"The Claude System We Built to *Generate* Ad Strategy"** with a peach highlight bar behind "Generate". Reads like a book cover or a course module, not a social graphic.
- **Title:** `the Claude system we built to generate ad strategy for ecom brands (full breakdown)`
- **Preview line:** "We are currently plugging Claude into every layer of our creative strategy process. We're still improving it and learning everyday, but it now runs our entire research-to-brief pipeline...."

Title mechanics: lowercase, `(full breakdown)` again, same as 01. But note the title names a **tool** (Claude) rather than a competitor or a format. Borrowed search interest from a named product.

**On its first run (4 Apr) this is the second-highest-reach article in the set: 15K impressions, 69 likes, 13 reposts.** Only article 08 (25K) beat it. The 27 Jul repost did 2.5K. See the two-run table above.

---

## Article body

We are currently plugging Claude into every layer of our creative strategy process.

We're still improving it and learning everyday, but it now runs our entire research-to-brief pipeline.

Here's the exact system, how it works, and why we'll never go back.

### The setup

Everything runs inside Claude Projects.

One project per ecom brand.

Private chats inside each project keep research completely separate nothing bleeds across accounts.

We may move over to cowork, code or whatever, but for now this goes.

Two things go into a project before any work starts:

1. Master prompts in markdown files so these guide the research methodology and live in the project permanently
2. Brand context: product info, customer data, brand voice, competitive landscape

We run Opus 4.6 extended for everything.

The extended context window handles the volume of research without losing detail.

### The 6-step pipeline

Every ecom brand SHOULD run through these 6.

If you don't, you're just far away from winning ads in 2026.

**Step 1: Root cause analysis**

Most agencies describe what a product does and send that to GPT.

We use Claude to identify why someone actually buys it.

Not "premium ingredients" or "clean formula." The real problem the product solves in someone's daily life. The purchase trigger that makes someone stop scrolling and click.

Claude breaks down the actual drivers behind the purchase decision.

We push it until it sounds like something a real customer would say to a friend.

This works great if the research is done in reddit or other forum sites. (more on this later)

**Step 2: Competitor analysis**

We feed Claude every direct response competitor actively spending on Meta.

Claude maps their positioning, hooks, and angles.

**Step 3: Review mining**

Real customer reviews go into Claude.

Claude pulls out the exact language customers use.

The specific benefits they call out on why they buy with the raw language people use when they're not being sold to.

This is where the best performing ad copy actually comes from.

**Step 4: Buyer personas**

Claude builds audience segments from the research (steps 1 to 3)

Then we validate every persona against competitor messaging. If a persona sounds identical to what competitors are already targeting, we kill it.

**Step 5: Angle mining**

This is where research starts to get closer to our briefs.

Claude generates messaging angles from the personas and all previous research context. Each angle is a unique way into the conversation the customer is already having in their head.

**Step 6: Brief generation**

Claude writes 45-70 second ad scripts pulled directly from the angle bank.

Every output from every step gets uploaded back into the project. This builds a compounding context library. The longer we work with a brand, the sharper every output gets because Claude has more context to pull from.

### What this actually means if you're running an ecom brand

This system lets us launch significantly more unique creatives per week than we could before.

If you add our stealth formats that don't look like ads to this...

It's the reason our clients are scaling.

If you're an ecom brand spending $100k+/month on Meta and you want to see how this system would work for your brand specifically, DM me "stealth." I'll build you a free roadmap with the exact angles, formats, and hooks we'd run.

Talk soon,
Lorenzo.

*(Note: the CTA paragraph arrives scrambled in the source paste, with the "$100k+" spend line rendering after the DM ask because X linkified `$100k+` as a cashtag. Reconstructed above in the intended order.)*

---

## Structural skeleton (the part that ports)

1. **Present tense, still-in-progress framing.** "We are currently plugging", "we're still improving it and learning everyday". No claim of a finished system. That's what makes it readable as build-in-public rather than a pitch.
2. **Setup before steps.** Tooling, structure, model, and what goes in before any work starts. The reader could actually replicate the container before the process.
3. **Numbered pipeline, one job per step**, each with a named failure mode it avoids ("most agencies describe what a product does and send that to GPT").
4. **The compounding-context payoff** at the end of step 6: outputs go back in, so the system sharpens over time. This is the single best idea in the article and it's buried in the last line of a step.
5. **No performance numbers at all.** Unlike 01 and 02, this one carries zero metrics. "Significantly more unique creatives per week" is deliberately unquantified. Reach was half, engagement rate was double.
6. **DM keyword CTA with a spend qualifier and a named deliverable** ("stealth" → a free roadmap with angles, formats, hooks).

## Where this one sits relative to Mauro's lane

This is the closest of the three to Mauro's actual lane. Strip the ecom subject and the shape is: *here is the AI system that runs a real pipeline inside a working agency, one project per client, master prompts as permanent files, outputs fed back in to compound.* That is Mauro's pillar 2 (low-time system that proves it converts) almost exactly, and it's the thing he genuinely runs. `mauro-os` itself is a more advanced version of what this article describes.

The transferable claim for Mauro is not "use Claude Projects." It's the compounding-context point: a system that gets sharper the longer it runs, because every output becomes input. Nobody in his ICP is running that.

## Cross-article pattern, 3 of 10 in

| | 01 shower head | 02 podcast ads | 03 Claude system |
|---|---|---|---|
| Title case | lowercase | lowercase | lowercase |
| Parenthetical | (full breakdown) | (step by step playbook) | (full breakdown) |
| Subject | someone else's account | our own format | our own internal system |
| Named entity in title | Jolie (leader) | podcast ads (format) | Claude (tool) |
| Card image | borrowed screenshot | custom teaching diagram | designed title card |
| Hard numbers in body | many | several | none |
| CTA | spend threshold, bio link | DM "AUDIT" or bio | DM "stealth", spend qualifier |
| Impressions | 5.0K | 5.5K | **15.0K** (Apr run) / 2.5K (Jul run) |
| Like rate | 0.48% | 0.67% | 0.46% (Apr) / 1.00% (Jul) |

**Three-article read:** every title is lowercase with a parenthetical promise, and every CTA carries a spend qualifier that filters for the buyer. Reach tracks with how well-known the entity in the title is. Engagement rate runs the opposite way. The three are: someone else's operation, our format, our system. That's a rotation, not a repetition, which is consistent with the six-week format-rotation finding in `research/lorenzo-pravata-x-formats/synthesis.md`.

## Notes pending Mauro's questions

- Model reference in the source says "Opus 4.6 extended". Preserved verbatim; if any of this becomes published content the model naming should be checked against current model IDs before it ships.
- The `growthub.agency` domain and the DM keywords appear across articles. Neither goes into anything public-facing for Mauro, per the never-name rule.
- Adopt / adapt / reject table gets written once all 10 are in.
