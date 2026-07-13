# Skill: Case Study Production

**Version:** 1.0 (draft — fields marked ⚠️ need team confirmation)
**Created:** 2026-06-02
**Origin:** Committed on the 2026-06-01 acquisition call — replace one-off manual requests with a repeatable gather → structure → publish workflow.
**Output:** A structured case study record in `brands/growthub/social-proof/case-studies/`, ready to feed content (lead magnets, long-form posts, website, pinned-post refreshes).

---

## What This Skill Does

Turns a client win into a reusable case study asset. The call's pain point was that case studies were produced by manual, one-off requests — slow and inconsistent. This SOP fixes the **intake**: Mauro coordinates with the creative lead, who pulls the screenshots + data from the media buyer, against a fixed checklist, so every case study lands with the same fields filled.

This is the **production** process (gathering the raw proof). It is upstream of:
- `skills/lead-gen/lead-magnet/case-study.md` — case study as a lead magnet
- `skills/content/long-form/case-study-long-form.md` — case study as a long-form post
- `brands/growthub/social-proof/` — the quote/testimonial library

Produce the asset once here; repurpose it many times downstream.

---

## The Intake Checklist (what to gather per case study)

Hand this list to the creative lead → media buyer. Nothing gets written up until the required fields are in.

**Client context**
- Brand name (and the redaction-safe alias to use publicly — see Privacy below)
- Vertical (ecom subcategory / SaaS)
- Monthly ad spend tier at the time
- Starting situation / the problem they came in with

**The standing case-study spec — every case study reports these three:**

1. **Formats we ran for them** — the creative formats Growthub produced (podcast ad / street interview / founder story / documentary / reaction, plus concept + hook-angle count).
2. **Revenue or spend scaled** — the hard number. How much we scaled their revenue or ad spend, before → after, with the date range. **Screenshot-backed** (ad account / Meta ads manager). No number without a screenshot.
3. **Creative-strategy change** — how we changed their current creative strategy (what they were doing before vs the approach we moved them to).

That's the locked set. (1) and (3) are the narrative, (2) is the proof.

**Privacy gate (from the 6/1 decision)**
- Per the `feedback_client_naming` rule + the 6/1 "result redaction protocol": redact specific client names and sensitive numbers in any **public** version; keep the fully-named version internal.
- Capture both: the internal named record AND the public-safe alias/redaction in the same file, clearly labelled.

---

## Roles

| Role | Responsibility |
|---|---|
| Mauro | Owns the SOP, requests the case study, does the final write-up |
| Creative lead | **Resolved per client** — there's no single creative lead; it depends on the client + industry. Look up who owns that account, then request screenshots + data from them / their media buyer. |
| Media buyer | The media buyer on that specific client account — source of the ad-account screenshots + performance numbers |
| Lorenzo | Approves the public-safe version before it ships |

> **First case study to run:** skincare. Candidate = **Forge Skin** (pending — Mauro confirming in the group whether it qualifies as a case study). Resolve the creative lead for that account before starting intake.

---

## Steps

1. **Trigger.** A client hits a reportable win (scaled spend, ROAS/CPA milestone, a winning concept). Mauro opens a new case study.
2. **Request.** Send the intake checklist to the creative lead. The creative lead pulls screenshots + numbers from the media buyer. Don't write until required fields + at least one screenshot-backed metric are in.
3. **Verify the numbers.** Every metric must trace to a screenshot. Per `feedback_no_fabricated_performance_numbers`: no number goes in the file that isn't backed by a screenshot or data file. Use bracketed placeholders for anything pending.
4. **Write the record.** Use the file template below. Fill the internal (named) version and the public-safe (redacted) version in the same file.
5. **Privacy approval.** Lorenzo signs off on the public-safe version before any public use.
6. **Save + commit.** Write to `brands/growthub/social-proof/case-studies/[client-alias].md`. Commit + push.
7. **Flag for repurposing.** Note which downstream assets it should feed (lead magnet / long-form / website / pinned post) so it doesn't sit unused.

---

## File Template

```markdown
# Case Study — [Client alias]

**Status:** [gathering / drafted / approved]
**Internal client name:** [real name — INTERNAL ONLY]
**Public alias:** [e.g. "a 7-figure skincare brand"]
**Vertical:** [ecom subcategory / SaaS]
**Spend tier at start:** [£/$ per month]
**Engagement window:** [start – end]

## The problem
[Starting situation in the client's own framing]

## 1. Formats we ran
[Creative formats produced — podcast ad / street interview / founder story / etc. + concept and hook-angle count]

## 2. Revenue / spend scaled (screenshot-backed)
| What | Before | After | Window | Screenshot |
|---|---|---|---|---|
| [Revenue or ad spend] | [x] | [y] | [dates] | [link/path] |

## 3. Creative-strategy change
[What their creative strategy was before → what we moved them to]

## Public-safe version
[The redacted version Lorenzo approves — alias only, sensitive numbers softened or banded]

## Repurposing
- [ ] Lead magnet  - [ ] Long-form post  - [ ] Website  - [ ] Pinned post
```

---

## Routing Instructions

When triggered:
1. Open a new case study record; send the intake checklist to the creative lead.
2. Gather → verify every number traces to a screenshot.
3. Write both the named (internal) and redacted (public) versions.
4. Get Lorenzo's approval on the public version.
5. Save to `brands/growthub/social-proof/case-studies/[alias].md`, commit + push.
6. Flag downstream repurposing targets.

---

## Trigger Phrases

- "Create a case study for [client]"
- "Start a case study"
- "Write up the [client] results"

---

## Anti-Patterns

- **No number without a screenshot.** Claims aren't proof. (`feedback_no_fabricated_performance_numbers`)
- **Never publish a named version without sign-off.** Default to the redacted alias publicly. (`feedback_client_naming`)
- **Don't write before the checklist is filled.** A half-gathered case study is the manual one-off problem this SOP exists to kill.
- **Don't let it sit.** Every case study gets at least one repurposing target flagged, or it was wasted effort.

---

## Open items to lock down (⚠️ before v1.1)

- ~~Confirm the creative lead + media buyer names.~~ RESOLVED: creative lead is **per client/industry**, not a fixed role — look up the account owner each time.
- Confirm whether **Forge Skin** qualifies as the first (skincare) case study — Mauro checking in the group.
- ~~Confirm the standing metric set.~~ RESOLVED: (1) formats we ran, (2) revenue/spend scaled (screenshot-backed), (3) creative-strategy change.
- Confirm the destination folder name (`brands/growthub/social-proof/case-studies/` assumed — create if it doesn't exist).
