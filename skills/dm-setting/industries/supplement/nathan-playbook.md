# Nathan's Supplement DM Playbook

The full system for converting supplement-brand LinkedIn connections into booked calls. Two-message punch + personalized deck delivery. Use this as your run-doc.

**Target prospect:** founder or CMO of a supplement brand currently running ads on Meta.
**Goal:** turn connection acceptance into deck delivery, then into a booked call.
**Time budget per prospect:** 7-12 minutes (Message 1 takes 1 min, personalization + Message 2 takes 6-10 min).

---

## Step 1: Send Message 1 (permission ask)

Send this immediately after they accept your connection request. Keep it short, observational, and end with an easy yes question.

**PRIMARY (use this by default):**

```
Hey [First name], quick one.

Saw you were running ads for [BrandName]. I put together a short doc on what's working for the supplement brands we manage this year to scale on Meta. Formats, creative strategy, mechanic stuff in general.

Want me to send it over?
```

### CTA close options (pick one)

| CTA | Tone | When to use |
|---|---|---|
| `Want me to send it over?` | Direct, casual | Default. Works for almost everyone. |
| `Cool if I send it?` | Softer, very casual | Informal or scrappy founder vibe. |
| `Worth me sending?` | Confident, slightly poised | CMO, VP, or senior tier. |

### Tone variants

**Founder-coded** (younger / scrappier brand):

```
Hey [First name], quick one.

Saw [BrandName] running ads on Meta. Put together a short doc on what's working for the supplement brands we manage this year. Formats, creative strategy, the mechanic side.

Want me to send it over?
```

**CMO-coded** (slightly more poised):

```
Hi [First name],

Saw [BrandName] is running ads on Meta. I put together a short doc on what's working for the supplement brands we manage at Growthub this year. Format spread, subscription mechanics, the stuff that's distinguishing scaled brands from plateaued ones.

Worth me sending it?
```

### Optional authority inserts (use sparingly)

If the prospect's profile suggests they need credibility before saying yes (very large brand, very senior title), insert one of these as a parenthetical after the second sentence:

- `(We manage $17M+ in supplement spend on Meta.)`
- `(We manage multiple supplement brands past $1M/month.)`

Or add this as a closing sentence after the CTA:

- `Genuinely useful even if we never end up working together.`

The default version usually tests cleaner without these. Add only when the prospect's tier demands it.

### What NOT to do in Message 1

- Don't pitch services or mention pricing.
- Don't ask for a call directly. The deck is the wedge, the call comes later.
- Don't lead with "I help [audience] do [thing]". Too templated, gets ignored.
- Don't stack multiple questions. One easy yes only.
- Don't use em dashes or generic agency language.

---

## Step 2: Wait for YES, then personalize the deck

When they reply "yes" or "go for it" or any positive signal, run the personalization workflow before sending Message 2.

### Master deck file

Open: `skills/content/linkedin-docs/industry-decks/supplement-scaling.html`

This is the canonical supplement deck. You'll create a personalized copy of it per prospect.

### The find-and-replace checklist

Open the master HTML in a text editor (VS Code, Sublime, or even TextEdit). Run these substitutions in order:

| # | Find | Replace with | Required? |
|---|---|---|---|
| 1 | `How to Scale a Supplement Brand` | `How [BrandName] Could Scale` | Required |
| 2 | `your supplement brand` (in bookmark hook) | `[BrandName]` | Required |
| 3 | `your account` (in CTA paragraph, section 5) | `[BrandName]'s account` | Recommended |
| 4 | `DM me "audit"` (CTA close) | `Reply to this thread for an audit on [BrandName]` | Required for DM use |

### What NOT to change

- The $107M+ authority anchor in the subhead
- Section headings, structure, or order
- Public example brand names in body text (Primal Queen, Arrae, Arctic Goddess). These are positioning case studies, not Growthub clients.
- Footer signature ("— Lorenzo" + "Growthub Brand Breakdowns")
- Closer italic line

### Save the personalized HTML

Save as: `accounts/lorenzo-x/personalized-decks/supplement/[brand-slug]-supplement-deck.html`

Brand-slug = lowercase, hyphenated brand name. Example: `proteinco-supplement-deck.html` for ProteinCo.

### Convert to PDF

LinkedIn renders HTML poorly inline, so convert to PDF before sending:

1. Open the saved HTML in your browser (Chrome works best).
2. Verify both pages render correctly with brand name swapped.
3. Print to PDF (Cmd+P → "Save as PDF").
4. Save with same slug + `.pdf` extension. Example: `proteinco-supplement-deck.pdf`.

### Quality check before sending

- Brand name appears in the title, the bookmark hook, and the CTA (at least 3 places)
- No leftover generic phrasing where a swap was missed
- PDF renders both pages cleanly with no overflow
- Filename matches the brand-slug convention

---

## Step 3: Send Message 2 (deck delivery)

Send within a few hours of their yes. Attach the personalized PDF.

```
Sent. Personalized for [BrandName] specifically: [attached PDF].

Took ~30 min to adapt the system around your brand. Feel free to forward to your CMO or whoever runs your Meta ad creative.

Let me know what lands. Happy to walk through any section that's unclear.
```

### What NOT to do in Message 2

- Don't ask for the call inside Message 2. Wait for them to engage with the deck first.
- Don't summarize the deck contents in the message. The deck speaks for itself.
- Don't over-promise or hype. Soft confidence beats salesy energy.

---

## Step 4: Log the send

Update the LinkedIn connections Google Sheet (Mauro shares the link). Required columns:

| Column | What to enter |
|---|---|
| Prospect name | Full name |
| Brand | Their company / brand name |
| Status | Message 1 sent / Yes received / Deck sent / Reply / Booked |
| First-message variant | standard / founder-coded / CMO-coded |
| CTA used | "Want me to send it over?" / "Cool if I send it?" / "Worth me sending?" |
| Date Message 1 sent | YYYY-MM-DD |
| Date deck sent | YYYY-MM-DD |
| Reply received? | Yes / No / Date |
| Booked? | Yes / No |

This feeds the funnel-stage drop-off dashboard. Reply rate by variant tells us which message version pulls best.

---

## Step 5: After Message 2

Three scenarios. Handle accordingly:

**Scenario A: They reply with a question about the deck.**
Engage conversationally. Answer their question. Don't pitch the call yet. After 2-3 exchanges, soft offer: "Happy to dig into [their specific gap] on a quick call if useful."

**Scenario B: They reply asking for an audit / call directly.**
Book it. Send Lorenzo's calendar link.

**Scenario C: They ghost (no reply within 5-7 days).**
Send one follow-up nudge. Example:

```
Hey [First name], just bumping this. Did the doc land OK? Curious if any section stood out for [BrandName].
```

If still no reply after another 5-7 days, mark dormant in the tracker. Don't keep pushing.

---

## Common pitfalls

1. **Sending Message 1 without checking the prospect's profile first.** Spend 30 seconds on their profile before DM. Confirm they're actually a supplement brand and currently running Meta ads. Bulk-feeling DMs get ignored.

2. **Sending Message 2 with the generic deck (not personalized).** Loses the entire wedge. The personalization is the whole reason this works. Always run the find-and-replace.

3. **Following up too fast.** Wait 48-72 hours minimum after Message 2 before any nudge. Earlier than that reads as desperation.

4. **Forgetting to attach the PDF.** Test before pressing send. Reading the message back to yourself catches this.

5. **Over-explaining the deck in Message 2.** The doc is the asset. The message is the wrapper. Don't pitch the doc, just deliver it.

6. **Responding in long paragraphs.** Match Lorenzo's voice on chat. Short, direct, no fluff. Multiple short messages beat one long one.

---

## Files you need access to

| File | Path | Purpose |
|---|---|---|
| Master supplement deck | `skills/content/linkedin-docs/industry-decks/supplement-scaling.html` | Source HTML you personalize per prospect |
| This playbook | `skills/dm-setting/industries/supplement/nathan-playbook.md` | The doc you're reading now |
| LinkedIn tracking sheet | (link from Mauro) | Where you log every send |
| Personalized deck output folder | `accounts/lorenzo-x/personalized-decks/supplement/` | Where your saved personalized HTMLs and PDFs live |

---

## Italian-market variant

For Italian supplement brands, Mauro is drafting a "super-direct" pre-drafted message. Until that ships, default to the standard English version.

---

## Next industries

Once supplement is validated (5-10 actual replies), the same workflow clones to skincare, pet, and app. Each industry will have its own deck and a parallel playbook. For now, supplement is the active queue.

Questions or stuck on something? Slack Mauro.
