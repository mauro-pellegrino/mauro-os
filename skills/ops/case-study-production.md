# Skill: Case Study Production

**Version:** 2.0
**Created:** 2026-06-02, retargeted to this brand 2026-07
**Purpose:** Replace one-off manual write-ups with a repeatable gather → structure → publish workflow for client results.
**Output:** A structured case study record in `brand/social-proof/case-studies/` (create the folder as results come in), ready to feed content (lead magnets, long-form posts, website, pinned-post refreshes).

---

## What This Skill Does

Turns a client win into a reusable case study asset. Case studies produced as one-off requests are slow and inconsistent. This SOP fixes the **intake**: Mauro (or Juan, the VA, on Mauro's request) gathers the screenshots and data against a fixed checklist, so every case study lands with the same fields filled.

This is the **production** process (gathering the raw proof). It is upstream of:
- `skills/lead-gen/lead-magnet/case-study.md`: case study as a lead magnet
- `skills/content/long-form/case-study-long-form.md`: case study as a long-form post
- `brand/social-proof/`: the quote/testimonial library (create as results come in)

Produce the asset once here; repurpose it many times downstream.

---

## The Intake Checklist (what to gather per case study)

Nothing gets written up until the required fields are in.

**Client context**
- Agency name (and the redaction-safe alias to use publicly, see Privacy below)
- Agency type (marketing / creative / ad / social / SEO) and rough monthly revenue tier
- Starting situation / the problem they came in with (pipeline dried up, no time for content, cringe fear, etc.)

**The standing case-study spec. Every case study reports these three:**

1. **The system installed**: what was actually built for them (content engine, lead-magnet flow, auto-DM setup, measurement loop, which skills/agents power it).
2. **The result**: the hard number. Inbound calls booked, qualified calls, revenue signed, posting consistency before → after, with the date range. **Screenshot-backed** (Calendly, analytics, DMs, signed-deal proof). No number without a screenshot.
3. **The operating change**: how they produced content and got clients before vs after the system (hours spent, who does what, what runs without them).

That's the locked set. (1) and (3) are the narrative, (2) is the proof.

**Privacy gate**
- Per the `feedback_client_naming` rule: redact client names and sensitive numbers in any **public** version; keep the fully-named version internal.
- Capture both: the internal named record AND the public-safe alias/redaction in the same file, clearly labelled.

---

## Roles

| Role | Responsibility |
|---|---|
| Mauro | Owns the SOP, opens the case study, verifies numbers, does the write-up, approves the public-safe version |
| Juan (VA) | Chases and collects screenshots + raw data against the checklist when asked |

---

## Steps

1. **Trigger.** A client hits a reportable win (booked-call milestone, a signed deal traced to content, a system running without them). Mauro opens a new case study.
2. **Gather.** Work the intake checklist (delegate collection to Juan if useful). Don't write until required fields plus at least one screenshot-backed metric are in.
3. **Verify the numbers.** Every metric must trace to a screenshot. Per `feedback_no_fabricated_performance_numbers`: no number goes in the file that isn't backed by a screenshot or data file. Use bracketed placeholders for anything pending.
4. **Write the record.** Use the file template below. Fill the internal (named) version and the public-safe (redacted) version in the same file.
5. **Privacy check.** Mauro signs off on the public-safe version before any public use.
6. **Save + commit.** Write to `brand/social-proof/case-studies/[client-alias].md` (create the folder on first use). Commit + push.
7. **Flag for repurposing.** Note which downstream assets it should feed (lead magnet / long-form / website / pinned post) so it doesn't sit unused.

---

## File Template

```markdown
# Case Study: [Client alias]

**Status:** [gathering / drafted / approved]
**Internal client name:** [real name, INTERNAL ONLY]
**Public alias:** [e.g. "a 7-figure SEO agency"]
**Agency type:** [marketing / creative / ad / social / SEO]
**Revenue tier at start:** [$/mo band]
**Engagement window:** [start – end]

## The problem
[Starting situation in the client's own framing]

## 1. The system installed
[What was built: content engine, lead-magnet flow, auto-DM setup, measurement loop, which skills/agents power it]

## 2. The result (screenshot-backed)
| What | Before | After | Window | Screenshot |
|---|---|---|---|---|
| [Calls booked / revenue / consistency] | [x] | [y] | [dates] | [link/path] |

## 3. The operating change
[How they produced content and got clients before vs after]

## Public-safe version
[The redacted version: alias only, sensitive numbers softened or banded]

## Repurposing
- [ ] Lead magnet  - [ ] Long-form post  - [ ] Website  - [ ] Pinned post
```

---

## Routing Instructions

When triggered:
1. Open a new case study record; work (or delegate) the intake checklist.
2. Gather → verify every number traces to a screenshot.
3. Write both the named (internal) and redacted (public) versions.
4. Mauro approves the public version.
5. Save to `brand/social-proof/case-studies/[alias].md`, commit + push.
6. Flag downstream repurposing targets.

---

## Trigger Phrases

- "Create a case study for [client]"
- "Start a case study"
- "Write up the [client] results"

---

## Anti-Patterns

- **No number without a screenshot.** Claims aren't proof. (`feedback_no_fabricated_performance_numbers`)
- **Never publish a named version.** Default to the redacted alias publicly. (`feedback_client_naming`)
- **Don't write before the checklist is filled.** A half-gathered case study is the manual one-off problem this SOP exists to kill.
- **Don't let it sit.** Every case study gets at least one repurposing target flagged, or it was wasted effort.

---

## Open items

- No client case study exists yet for this brand. First candidate: [CLIENT RESULT, fill from social-proof/ when available].
