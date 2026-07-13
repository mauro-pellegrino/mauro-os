# Ad Teardown Skill

**Version:** 1.0
**Created:** 2026-06-29
**Purpose:** Paste one or more competitor (or client) ad transcripts, optionally with their ad-library metrics, and extract the winning structure: who it targets, what problem it addresses, what awareness level it speaks to, and what creative elements are actually driving performance. Output feeds scripting and the `creative-strategy-map`.

**Relationship to other skills:** `creative-strategy-map/main.md` plans creative forward from a product. This skill works backward from ads that are already winning. `brand-breakdown.md` is the brand/account-level version for YouTube videos; this one is ad-level and transcript-first.

---

## Required reading

Before any audience-facing output, read `brands/growthub/voice.md` (hard bans + 60-second checklist) and `brands/growthub/audience.md` (ICP). Ground persona and pain calls in the ICP, never invent.

---

## The four questions this skill answers

Every teardown exists to answer these, in order:

1. **Who is this ad targeting?** (the buyer, by why they buy, not demographics)
2. **What problem does it address?**
3. **What awareness level is it speaking to?** (unaware / problem aware / solution aware / product aware / most aware)
4. **What creative elements are actually driving performance?**

Once these are answered, the team can build winning creative instead of guessing.

---

## Inputs

- **Ad transcript(s).** One is enough for a single teardown. **3-4 winning ads** are needed for pattern recognition (the highest-value output).
- **Ad-library metrics (optional, sharpens everything):** frequency, cost per result, spend rank in the account, age/gender breakdown, how long the ad has run. With these, the read goes from qualitative to evidenced.
- **Brand + product context:** what it sells, the category.

If metrics are missing, run the qualitative teardown and clearly flag every conclusion that real metrics would confirm or change. If only one ad is provided, do the per-ad teardown and note that pattern recognition needs more. Ask for missing inputs one at a time. Never invent metrics.

---

## The process

### Step 1 — Start with the first second
You don't need the full ad. The first second tells you almost everything: who it's for, what problem it tackles, and whether there's a real hook or just a strong visual.
- Read the opening frame / first line.
- Note any captions or on-screen headers (there almost always are).
- Name what the ad is doing to draw attention.

### Step 2 — Separate the hook from the angle
- **Hook** = what stops the scroll (the first line/frame).
- **Angle** = the specific lens used to frame the problem.
- Always ask "what is the angle," not "what is it about." The angle is the replicable, testable, buildable thing. State it as one line.

### Step 3 — Read frequency and cost per result together
Numbers don't explain themselves. High frequency + a lower cost per result than the account's top spender usually means a **mid-funnel converter**: it closes people already warmed up by something else. Pattern to look for: one ad captures cold audiences, a second converts them. Two numbers can hand you the funnel structure. (Skip if metrics weren't provided, and say so.)

### Step 4 — Read the age and gender breakdown
Most people stop here after a minute. Don't. Ask *why* a segment over-indexes.
- Same gender, different life stage = different pain (a 37-year-old single mom is not a 27-year-old in her first serious relationship).
- If a segment you didn't expect over-indexes (e.g. male audiences on a product aimed at women), stop and find out why: the creator's existing audience, a format that crosses over, etc. That is a creative insight to use.

### Step 5 — Build pattern recognition (after 3-4 ads)
This is the payoff. Across the winning ads, answer:
1. What angle consistently shows up?
2. What type of hook keeps appearing?
3. What awareness level is the account leaning on?
4. Is there a funnel gap (only bottom-funnel, ignoring cold traffic)?

Write down **every keyword, hook format, and framing device** that appears in the winners. This becomes a checklist to run new creative against before building, so new ads are informed by what works instead of starting from scratch.

### Step 6 — The fastest way to make a new winner
1. Take the best-performing ad.
2. Identify the core angle.
3. Rewrite it in a **different format with a different creative treatment** (different actor, setting, format).

It should not feel like the same ad to the viewer, but it carries the same ingredients that drove performance. Use Growthub's stealth formats (podcast ads, skit conversations, street interviews, Pixar/native) to grab quick wins that are **visually different** from everything else in the account. Visual difference is the #1 proven lever to scale on Meta in 2026 (entity-ID / Andromeda groups near-identical creatives and caps their reach).

---

## Output structure

**Per ad:**
```
AD [n] — [one-line label]
First second: [opening frame + caption/header + attention mechanism]
Hook: [the scroll-stopper, verbatim if possible]
Angle: [the specific lens, one line]
Targeting (who): [buyer by why-they-buy]
Problem: [the problem it addresses]
Awareness level: [stage + one line of evidence]
Creative elements driving it: [format, proof, authority, structure]
Metrics read: [freq + CPR → cold/mid-funnel; segment skew + why] (or "metrics not provided")
```

**Across the set (pattern recognition):**
```
Recurring angle:
Recurring hook type:
Awareness level the account leans on:
Funnel gap:
Winning-elements checklist: [every keyword / hook format / framing device]
```

**New-winner recommendations:**
```
For each of the top 2-3 angles:
  Angle: [...]
  Keep (the ingredients that drove performance): [...]
  Change (format + treatment, must be visually different): [stealth format choice]
```

End by asking whether to push the winning angles into the `creative-strategy-map` for the brand, or straight into scripting.

---

## Anti-patterns

- Answering "what is it about" instead of naming the **angle**.
- Reading metrics without context (a number with no comparison is noise).
- Stopping at the age/gender chart without asking *why* a segment responds.
- Copying the winning ad instead of extracting its angle and rebuilding it differently.
- A "new" ad that looks like the old one. If it isn't visually different, it gets grouped by Meta and caps your reach.
- Inventing metrics, segments, or results that weren't in the inputs. Flag the gap instead.

---

## Note
This same framework can power a lead magnet or YouTube breakdown (the "how we tear down competitor ads" angle). When used for that, route through the relevant `lead-gen/lead-magnet` subtype and apply `feedback_no_fabricated_performance_numbers` and `feedback_client_naming`.
