# Setter Playbook: Agency-Owner DMs

The full system for converting agency-owner LinkedIn connections into booked calls. Two-message punch + personalized deck delivery. This is the run-doc for whoever runs DM setting on Mauro's account (a setter or VA, or Mauro himself). (v2, 2026-07-14)

**Target prospect:** founder/owner of an established agency (marketing, creative, ad, social, SEO) whose pipeline runs on referrals and outbound. ICP details in `brand/audience.md`.
**Goal:** turn connection acceptance into deck delivery, then into a booked call.
**Time budget per prospect:** 7-12 minutes (Message 1 takes 1 min, personalization + Message 2 takes 6-10 min).

**Blocker before running at volume:** the master agency-owner deck does not exist yet. Build it at `skills/content/linkedin-docs/industry-decks/agency-inbound.html` first (use `linkedin-doc-template.html` in that folder as the structural template). Everything below assumes that deck exists.

---

## Step 1: Send Message 1 (permission ask)

Send this immediately after they accept your connection request. Keep it short, observational, and end with an easy yes question.

**PRIMARY (use this by default):**

```
Hey [First name], quick one.

Saw you run [AgencyName]. I put together a short doc on how agency owners are using AI to turn their client work into inbound clients this year. Content systems, lead magnets, the acquisition side.

Want me to send it over?
```

### CTA close options (pick one)

| CTA | Tone | When to use |
|---|---|---|
| `Want me to send it over?` | Direct, casual | Default. Works for almost everyone. |
| `Cool if I send it?` | Softer, very casual | Informal or scrappy solo-operator vibe. |
| `Worth me sending?` | Confident, slightly poised | Larger, more established shop. |

### Tone variants

**Solo-operator** (smaller / scrappier shop):

```
Hey [First name], quick one.

Saw you run [AgencyName]. Put together a short doc on how agency owners are using AI to turn client work into inbound this year. Content systems, lead magnets, the acquisition side.

Want me to send it over?
```

**Established-owner** (larger team, slightly more poised):

```
Hi [First name],

Saw [AgencyName]'s work. I put together a short doc on how agency owners are getting inbound clients with AI content systems this year. The engine setup, lead magnets, the stuff that's separating agencies with inbound from agencies stuck on referrals.

Worth me sending it?
```

### Optional authority inserts (use sparingly)

If the prospect's profile suggests they need credibility before saying yes (large shop, very established), insert one of these as a parenthetical after the second sentence. Only Mauro's own signed-off proof:

- `(It's the exact system I run daily for a B2B agency.)`
- `[PROOF LINE — signed-off number from the weekly analysis, when available]`

Or add this as a closing sentence after the CTA:

- `Genuinely useful even if we never end up working together.`

The default version usually tests cleaner without these. Add only when the prospect's tier demands it.

### What NOT to do in Message 1

- Don't pitch services or mention pricing.
- Don't ask for a call directly. The deck is the wedge, the call comes later.
- Don't lead with "I help [audience] do [thing]". Too templated, gets ignored.
- Don't stack multiple questions. One easy yes only.
- Don't use em dashes or generic guru language.

---

## Step 2: Wait for YES, then personalize the deck

When they reply "yes" or "go for it" or any positive signal, run the personalization workflow before sending Message 2.

### Master deck file

Open: `skills/content/linkedin-docs/industry-decks/agency-inbound.html` (build pending, see blocker note at top)

This is the canonical agency-owner deck. You'll create a personalized copy of it per prospect. Full personalization workflow: `skills/content/linkedin-docs/personalization-guide.md`.

### The find-and-replace checklist

Open the master HTML in a text editor (VS Code, Sublime, or even TextEdit). Run these substitutions in order (exact strings to be locked once the deck ships):

| # | Find | Replace with | Required? |
|---|---|---|---|
| 1 | The generic deck title (e.g. `How to Build an Agency Inbound Engine`) | `How [AgencyName] Could Build Its Inbound Engine` | Required |
| 2 | `your agency` (in the bookmark hook) | `[AgencyName]` | Required |
| 3 | `your account` (in the CTA paragraph) | `[AgencyName]'s setup` | Recommended |
| 4 | The public-post CTA close (e.g. `DM me "teardown"`) | `Reply to this thread for a free teardown on [AgencyName]` | Required for DM use |

### What NOT to change

- The authority anchor line in the subhead (Mauro's own signed-off proof; do not edit or inflate it)
- Section headings, structure, or order
- Public example references in body text (positioning examples, not clients)
- Footer signature ("— Mauro")
- Closer italic line

### Save the personalized HTML

Save as: `skills/content/linkedin-docs/personalized-decks/agency-owners/[agency-slug]-inbound-deck.html` (create the folder on first send)

Agency-slug = lowercase, hyphenated agency name. Example: `northpeak-media-inbound-deck.html` for NorthPeak Media.

### Convert to PDF

LinkedIn renders HTML poorly inline, so convert to PDF before sending:

1. Open the saved HTML in your browser (Chrome works best).
2. Verify both pages render correctly with the agency name swapped.
3. Print to PDF (Cmd+P → "Save as PDF").
4. Save with same slug + `.pdf` extension. Example: `northpeak-media-inbound-deck.pdf`.

### Quality check before sending

- Agency name appears in the title, the bookmark hook, and the CTA (at least 3 places)
- No leftover generic phrasing where a swap was missed
- PDF renders both pages cleanly with no overflow
- Filename matches the agency-slug convention

---

## Step 3: Send Message 2 (deck delivery)

Send within a few hours of their yes. Attach the personalized PDF.

```
Sent. Personalized for [AgencyName] specifically: [attached PDF].

Took ~30 min to adapt the system around your agency. Feel free to forward to whoever runs your marketing.

Let me know what lands. Happy to walk through any section that's unclear.
```

### What NOT to do in Message 2

- Don't ask for the call inside Message 2. Wait for them to engage with the deck first.
- Don't summarize the deck contents in the message. The deck speaks for itself.
- Don't over-promise or hype. Soft confidence beats salesy energy.

---

## Step 4: Log the send

Update the LinkedIn connections Google Sheet (link from Mauro). Required columns:

| Column | What to enter |
|---|---|
| Prospect name | Full name |
| Agency | Their agency name |
| Status | Message 1 sent / Yes received / Deck sent / Reply / Booked |
| First-message variant | standard / solo-operator / established-owner |
| CTA used | "Want me to send it over?" / "Cool if I send it?" / "Worth me sending?" |
| Date Message 1 sent | YYYY-MM-DD |
| Date deck sent | YYYY-MM-DD |
| Reply received? | Yes / No / Date |
| Booked? | Yes / No |

This feeds the funnel-stage drop-off view. Reply rate by variant tells us which message version pulls best.

---

## Step 5: After Message 2

Three scenarios. Handle accordingly:

**Scenario A: They reply with a question about the deck.**
Engage conversationally. Answer their question. Don't pitch the call yet. After 2-3 exchanges, soft offer: "Happy to dig into [their specific gap] on a quick call if useful."

**Scenario B: They reply asking for a call or teardown directly.**
Book it. Send Mauro's calendar link. [BOOKING LINK — pending, flag to Mauro if not yet set up]

**Scenario C: They ghost (no reply within 5-7 days).**
Send one follow-up nudge. Example:

```
Hey [First name], just bumping this. Did the doc land OK? Curious if any section stood out for [AgencyName].
```

If still no reply after another 5-7 days, mark dormant in the tracker. Don't keep pushing.

---

## Common pitfalls

1. **Sending Message 1 without checking the prospect's profile first.** Spend 30 seconds on their profile before DM. Confirm they actually run an established agency (not a beginner, not a freelancer hunting cheap prompts). Bulk-feeling DMs get ignored.

2. **Sending Message 2 with the generic deck (not personalized).** Loses the entire wedge. The personalization is the whole reason this works. Always run the find-and-replace.

3. **Following up too fast.** Wait 48-72 hours minimum after Message 2 before any nudge. Earlier than that reads as desperation.

4. **Forgetting to attach the PDF.** Test before pressing send. Reading the message back to yourself catches this.

5. **Over-explaining the deck in Message 2.** The doc is the asset. The message is the wrapper. Don't pitch the doc, just deliver it.

6. **Responding in long paragraphs.** Match Mauro's voice on chat. Short, direct, no fluff. Multiple short messages beat one long one. Voice rules in `brand/voice.md`.

---

## Files you need access to

| File | Path | Purpose |
|---|---|---|
| Master agency-owner deck | `skills/content/linkedin-docs/industry-decks/agency-inbound.html` (build pending) | Source HTML you personalize per prospect |
| Personalization workflow | `skills/content/linkedin-docs/personalization-guide.md` | The find-and-replace skill |
| This playbook | `skills/dm-setting/industries/agency-owners/setter-playbook.md` | The doc you're reading now |
| LinkedIn tracking sheet | (link from Mauro) | Where you log every send |
| Personalized deck output folder | `skills/content/linkedin-docs/personalized-decks/agency-owners/` (create on first send) | Where saved personalized HTMLs and PDFs live |

---

## Next segments

Once agency-owner outreach is validated (5-10 actual replies), the same workflow can clone to narrower segments (paid-media agencies, SEO agencies, creative studios), each with its own deck and a parallel playbook. Keep anchors consistent with the lead-magnet side (`skills/lead-gen/lead-magnet/industry-specific.md`). For now, the broad agency-owner queue is the active one.

Questions or stuck on something? Message Mauro.
