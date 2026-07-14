# Skill: Creative Strategy Map
**Version:** 1.0
**Created:** 6 April 2026
**Input:** Brand name + product page URL + (optional) video ad transcripts
**Output:** Full creative strategy map — personas, awareness-level thoughts, angles, format recommendations

---

## Required Reading

Before producing any written output, read `brand/voice.md` and `brand/audience.md` in full. All copy must pass the pre-publish checklist in voice.md. The map itself is grounded in the analyzed brand's own research (reviews, transcripts, product page); voice.md governs how the write-up reads.

---

## What This Skill Does

Builds a full creative strategy map for a brand's hero product. Takes a product URL and optionally video ad transcripts, does all remaining research automatically (product mechanism, customer reviews, competitor context), and outputs a structured map ready to inform ad production.

---

## Inputs

### What Claude fetches automatically
- Product page (mechanism, claims, ingredients, clinical data)
- Customer reviews from third-party sites (Cult Beauty, Trustpilot, review blogs)
- Brand positioning from homepage
- Competitor context via search

### What Claude cannot fetch automatically
- Meta Ad Library video transcripts (videos can't be watched)
- Amazon reviews (access blocked)
- Reddit threads (search returns limited results)

### What the user provides
**Required:**
- Brand name
- Hero product page URL

**Optional but high-value:**
- 3-5 video ad transcripts (pasted as text) — longest-running or best-performing ads
- Amazon review dump (copy-paste from product page)
- Reddit thread links (Claude will fetch if URL is provided)

**If transcripts are provided:** Claude uses them to validate personas and angles against what's actually converting.
**If not provided:** Claude builds the map from automated research only and flags which assumptions need validation against real ad data.

---

## Research Phase (Claude runs this automatically)

### Step 1 — Fetch the product page
Extract:
- The mechanism (what biological/physical process does the product target?)
- The villain (what's causing the problem the product solves?)
- Key claims and clinical evidence
- Exact marketing copy used to describe the problem
- Who the product page is written for

### Step 2 — Fetch customer reviews
Try in this order until enough data is gathered (target 15-20 reviews minimum):
1. Cult Beauty product page (usually fetchable)
2. Trustpilot brand page
3. Third-party review sites (search "[brand name] review site:honestbrandreviews.com" or similar)
4. Any user-provided URLs

Extract from reviews:
- The exact phrase customers use to describe their problem before buying
- What they tried before and why it failed
- What changed after using the product
- What disappointed them
- Any unexpected benefits mentioned

### Step 3 — Fetch brand homepage
Extract core positioning, brand philosophy, and any claims about how they're different from other brands in the category.

### Step 4 — Competitor context (search only)
Search "[brand name] vs competitors" and "[category] best supplements/products reddit 2025" to understand:
- What alternatives buyers consider
- What the category conversation looks like
- What positioning gaps exist

### Step 5 — Process video transcripts (if provided)
For each transcript, extract:
- The awareness level being targeted (based on how the hook opens)
- The persona being addressed (based on the pain point entered from)
- The mechanism or villain introduced
- When the product is named
- The close structure

---

## Map Building Phase

After research, build the map in this exact order.

---

### 1. HERO PRODUCT SUMMARY

One paragraph. State the product, the mechanism, the villain (if one exists), and the core clinical claim. This is the factual foundation everything else builds on.

---

### 2. BUYER PERSONAS

Build 3-4 personas based on what the reviews and transcripts actually show. Each persona is defined by why they buy — not age, gender, or income.

Format each persona as:

**[Persona Name] — [One-line descriptor]**
- Core pain: [The specific discomfort or frustration driving them toward a solution]
- Emotional state: [How they feel about having tried things that didn't work]
- What they want: [Outcome — not product features]
- What makes them respond: [The type of claim, proof, or framing that lands for them]
- Best evidence from research: [Direct quote or review phrase that captures this persona]

---

### 3. AWARENESS-LEVEL THOUGHT MAP

For each persona, write one internal thought per awareness stage. These are the actual sentences running through their head — not hooks, not ad copy. First person.

| Stage | [Persona 1] | [Persona 2] | [Persona 3] |
|---|---|---|---|
| Unaware | | | |
| Problem Aware | | | |
| Solution Aware | | | |
| Product Aware | | | |
| Most Aware | | | |

---

### 4. ANGLES PER PERSONA

For the 2 highest-priority personas, list 3-5 angles per awareness level. An angle is a specific entry point into the persona's pain — not a hook, not a full idea. Just the emotional door you're opening.

Format:

**[Persona Name]**

Unaware angles:
- [Angle]
- [Angle]

Problem Aware angles:
- [Angle]
- [Angle]

Solution Aware angles:
- [Angle]

Product Aware angles:
- [Angle]

Star the 2-3 angles with the strongest signal from reviews or transcripts.

---

### 5. FORMAT RECOMMENDATIONS PER AWARENESS LEVEL

| Awareness Level | Recommended Formats | Why |
|---|---|---|
| Unaware | Long VSL, podcast-style, educational | Viewer needs to learn something before they'll believe anything. Length signals difference. |
| Problem Aware | Short VSL, podcast clip, POV | Hook lands the problem fast. Quiz funnel or soft CTA reduces friction. |
| Solution Aware | Doctor/expert format, clinical b-roll | Viewer knows solutions exist. Credentials and ingredient science close the gap. |
| Product Aware | Testimonial, before/after, UGC-style | Social proof and specific results. Price anchoring and guarantee close. |
| Most Aware | Static, offer-focused, retargeting | One message: here's why now. Discount, bundle, urgency. |

Adjust based on transcript evidence — if a specific format is clearly working in the transcripts, note it here.

---

### 6. PRIORITY TESTING ORDER

List the top 5 angle + persona + awareness level + format combinations to test first, ranked by confidence based on research signal.

Format:

1. **[Persona] | [Awareness Level] | [Angle] | [Format]**
   Reason: [What in the research backs this as the highest-confidence test]

2. [Same format]

...and so on.

---

### 7. GAPS AND VALIDATION NEEDED

List what the map is missing because Claude couldn't fetch it automatically:
- Which assumptions need validation against real ad transcripts
- What competitor ad data would change the angle prioritization
- Which personas are inferred vs. directly evidenced

---

## Rules

- Never invent review quotes. If a persona isn't directly evidenced in the research, flag it as inferred.
- Angles are entry points, not full concepts. Keep them raw — one line.
- The villain (if one exists) must come from the product's own mechanism claims, not invented.
- Flag every place where transcript input would sharpen the output.
- After completing the map, ask: "Do you want to add ad transcripts to validate the angle prioritization, or move to concept production?"

---

## Example Run — The Nue Co. Debloat+

**Input provided:** Brand name + product URL (https://thenueco.com/products/debloatplus)
**Transcripts provided:** None

### Hero Product Summary

Debloat+ targets bloating through 17 digestive enzymes that break down food groups (carbs, starches, fats) that the gut struggles to process. The mechanism is enzyme-based, not probiotic — it works immediately on contact with food rather than requiring weeks of gut microbiome changes. Key villain: the foods themselves aren't the problem, your gut's enzyme capacity is. Clinical backing: 90% felt less bloated, 89% saw reduction in gas, 100% felt reduction after one use (consumer panel, 28 respondents).

---

### Buyer Personas

**The Chronic Bloater — Has tried everything and still feels like she swallowed a balloon**
- Core pain: Regular bloating after meals that nothing has reliably fixed — probiotics take too long, cutting foods out is unsustainable
- Emotional state: Resigned. Has spent money on supplements that "kind of work" but never reliably. Price-skeptical but willing to try again.
- What they want: Fast relief. Something that works the same day.
- What makes them respond: Speed claim + specific mechanism. "17 digestive enzymes" sounds like something different from the probiotic she's already tried.
- Best evidence: "noticeably less bloated and my digestion is more balanced" / "feel less bloated after a few days"

**The Clean Ingredient Seeker — Reads every label and rejects most supplements**
- Core pain: Wants gut support but can't find a product without artificial sweeteners, fillers, or ingredients she doesn't recognize
- Emotional state: Frustrated with the industry. Feels like premium pricing rarely means premium ingredients.
- What they want: A supplement she can trust the ingredients list of
- What makes them respond: Ingredient transparency, banned ingredient list, organic sourcing claims
- Best evidence: Trustpilot reviews flagging products with "crazy amounts of stevia" — The Nue Co. is chosen specifically because it avoids this

**The Gut-Skin Connector — Takes digestive supplements but cares about the downstream effects**
- Core pain: Chronic low-grade skin issues (dullness, adult acne, uneven texture) she suspects are connected to gut health
- Emotional state: Cautiously optimistic. Has heard the gut-skin connection theory but hasn't found a product that proves it for her
- What they want: Both — better digestion and visible skin improvement
- What makes them respond: Unexpected benefit reviews ("my skin has a glow", "hair looks healthier") more than the primary claim
- Best evidence: Multiple Cult Beauty reviewers noting skin/hair changes as a surprise benefit

---

### Awareness-Level Thought Map

| Stage | Chronic Bloater | Clean Ingredient Seeker | Gut-Skin Connector |
|---|---|---|---|
| Unaware | "I just feel uncomfortable after most meals, it's probably stress or what I'm eating" | "I should probably take a probiotic but they all seem the same" | "My skin looks dull and I don't know why, I drink water and eat well" |
| Problem Aware | "I have chronic bloating and nothing reliably fixes it" | "Every supplement I check has fillers and sweeteners I don't want" | "I've read that gut health affects skin but I don't know where to start" |
| Solution Aware | "I've tried probiotics but they take weeks and I still get hit randomly" | "There must be a cleaner option out there, I just haven't found it" | "Maybe if I fix my gut the skin stuff will follow but what actually works" |
| Product Aware | "I've seen Debloat+ but I'm skeptical it's different from what I've tried" | "The Nue Co. has a banned ingredient list — that's more than most brands do" | "People in reviews are saying their skin improved too, that's interesting" |
| Most Aware | "I'm almost out and I do notice when I stop taking it" | "The price went up but it's still the cleanest formula I've found" | "I'll try the Pre + Probiotic stack to see if I get more of the skin benefit" |

---

### Angles Per Persona

**The Chronic Bloater**

Unaware angles:
- You're not eating too much — your gut is running out of enzymes to process what you eat ★
- The reason you feel worse after "healthy" foods like beans and broccoli

Problem Aware angles:
- Why probiotics didn't fix your bloating (they weren't designed to) ★
- The 17-enzyme formula that works on contact, not after 30 days

Solution Aware angles:
- What's different between enzyme-based and probiotic-based bloating relief ★

Product Aware angles:
- 90% felt less bloated. Here's the consumer panel data behind that claim

**The Clean Ingredient Seeker**

Unaware angles:
- The ingredient most supplement brands put in their "clean" formula that you'd never expect

Problem Aware angles:
- Why reading labels on supplements is harder than it should be ★
- The 200+ ingredient banned list a supplement brand built before formulating anything

Solution Aware angles:
- How ingredient sourcing actually changes what ends up in your bloodstream ★

Product Aware angles:
- Side by side: what's in a standard probiotic vs. what's in this one

---

### Format Recommendations Per Awareness Level

| Awareness Level | Recommended Formats | Why |
|---|---|---|
| Unaware | Long VSL, podcast-style educational, documentary snippet | Chronic Bloater has been burned before. Needs to learn the enzyme mechanism before she'll believe another product claim. |
| Problem Aware | Short VSL with mechanism hook, podcast clip | Lead with the specific problem (not generic "bloating"), then fast pivot to why the old category failed her. |
| Solution Aware | Expert/doctor format, ingredient walkthrough | Clean Ingredient Seeker needs credentials + transparency, not just claims. Clinical b-roll performs here. |
| Product Aware | Before/after testimonial, UGC-style | Specific results ("less bloated in 3 days") + guarantee removes final friction. |
| Most Aware | Static, offer-focused | Subscription discount, bundle with Pre + Probiotic, free shipping. One message. |

---

### Priority Testing Order

1. **Chronic Bloater | Problem Aware | "Why probiotics didn't fix your bloating" | Podcast-style short VSL**
   Reason: Directly evidenced in reviews (multiple mentions of trying probiotics first). High-volume audience. Mechanism contrast is clear and defensible.

2. **Chronic Bloater | Unaware | "You're not eating too much — your gut is running out of enzymes" | Long VSL**
   Reason: Reframes the villain (not food, not quantity — enzyme capacity). Removes self-blame. Pattern matches MiamiMD's Progerin mechanic that's proven in a parallel category.

3. **Gut-Skin Connector | Problem Aware | "The gut-skin connection your dermatologist probably hasn't mentioned" | Educational/expert format**
   Reason: Unexpected benefit mentioned in 3+ independent reviews unprompted. Larger addressable audience than pure bloating angle. Sephora retail placement signals this persona shops there too.

4. **Clean Ingredient Seeker | Problem Aware | "The 200-ingredient banned list built before formulating anything" | Founder/transparency format**
   Reason: Brand differentiator is real and specific. Works especially for audiences burned by "clean" brands that aren't. Lower volume but high conversion for right audience.

5. **Chronic Bloater | Solution Aware | "What's different between enzyme-based and probiotic-based relief" | Educational stats-based**
   Reason: Addresses the most common objection from someone who's already tried probiotics. Clinical data (90%, 89%, 100%) is strong social proof at this stage.

---

### Gaps and Validation Needed

- No video ad transcripts provided — angle prioritization is based on review research only. Transcripts would confirm which awareness levels The Nue Co. is already serving and where the gaps are.
- Amazon reviews blocked — likely a significant source of Chronic Bloater language. If user can paste these, persona 1 angles would sharpen considerably.
- Meta Ad Library not fetchable — can't confirm current creative strategy or identify what's already running.
- Reddit data not retrieved — gut health subreddits (r/SIBO, r/ibs, r/supplements) would add raw unfiltered buyer language for Unaware angles.
