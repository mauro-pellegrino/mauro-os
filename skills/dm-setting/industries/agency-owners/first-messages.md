# Agency-Owner DM: Two-Message Punch

The opening DM sequence for agency-owner prospects on LinkedIn. Targets the founder/owner of an established agency (marketing, creative, ad, social, SEO) whose pipeline visibly runs on referrals and outbound, per `brand/audience.md`. (v2, 2026-07-14)

**Goal:** turn a connection acceptance into a deck delivery, then into a booked call. Two messages handle the YES path. Follow-up handlers (no-response, deferred-yes, polite-no) will live in `objections.md` (not yet written; handle manually until it ships).

**Blocker before running at volume:** a master agency-owner deck does not exist yet. Build it at `skills/content/linkedin-docs/industry-decks/agency-inbound.html` (use `linkedin-doc-template.html` in that folder as the structural template). Do not send Message 1 until the deck is ready to deliver.

## Message 1: Permission ask (PRIMARY)

Send this immediately after connection acceptance. Short, observation-led, ends with an easy yes question. No authority anchor in the opener. Keep it conversational and low-pressure. The deck does the authority work.

```
Hey [First name], quick one.

Saw you run [AgencyName]. I put together a short doc on how agency owners are using AI to turn their client work into inbound clients this year. Content systems, lead magnets, the acquisition side.

Want me to send it over?
```

### CTA close options (pick whichever feels natural)

The closing question is the highest-leverage line in Message 1. Three equally-good options, ranked by tone:

| CTA | Tone | When to use |
|---|---|---|
| `Want me to send it over?` | Direct, casual | Default. Works for almost everyone. |
| `Cool if I send it?` | Softer, very casual | When the prospect's profile is informal / scrappy solo-operator vibe. |
| `Worth me sending?` | Confident, slightly more poised | When the prospect runs a larger, more established shop. |

Avoid gerund constructions ("would that be something you'd like me sending over"). Clunky cadence.

### Optional pickups

If you want to layer authority into Message 1 (use sparingly, the soft version above tests cleaner without it), the insertable lines must be Mauro's own signed-off proof:

- After the second sentence: `(It's the exact system I run daily for a B2B agency.)`
- After the second sentence: `[PROOF LINE — signed-off number, e.g. a booked-calls figure from the weekly analysis]`
- After the closing question: `Genuinely useful even if we never end up working together.`

Treat these as inserts not requirements. The default version above is the lead. Never borrow client anchors from the agency Mauro runs (per `brand/positioning.md`).

### Variants for tone

**Solo-operator variant** (when the prospect runs a smaller / scrappier shop):

```
Hey [First name], quick one.

Saw you run [AgencyName]. Put together a short doc on how agency owners are using AI to turn client work into inbound this year. Content systems, lead magnets, the acquisition side.

Want me to send it over?
```

**Established-owner variant** (larger team, more senior, slightly more poised):

```
Hi [First name],

Saw [AgencyName]'s work. I put together a short doc on how agency owners are getting inbound clients with AI content systems this year. The engine setup, lead magnets, the stuff that's separating agencies with inbound from agencies stuck on referrals.

Worth me sending it?
```

### What NOT to do in Message 1

- Don't pitch services or mention pricing.
- Don't ask for a call directly. The deck is the wedge, not the call.
- Don't lead with "I help [audience] do [thing]". Too templated, gets ignored.
- Don't stack multiple questions. One easy yes question only.
- Don't use em dashes, "not X but Y" structures, or generic guru-speak. This audience is allergic to guru energy (see `brand/audience.md`).

## Message 2: Deck delivery (after YES)

Send within a few hours of their yes. Attach the personalized PDF (built via the personalization skill at `skills/content/linkedin-docs/personalization-guide.md`).

```
Sent. Personalized for [AgencyName] specifically: [attached PDF].

Took ~30 min to adapt the system around your agency. Feel free to forward to whoever runs your marketing.

Let me know what lands. Happy to walk through any section that's unclear.
```

### What this does

- Frames the deck as personalized work product (not a generic giveaway).
- Suggests the prospect forward it internally, opening the multi-stakeholder path.
- Soft no-CTA close. The deck does the work. The call comes later if they self-initiate.

### What NOT to do in Message 2

- Don't ask for the call inside Message 2. Wait for them to engage with the deck first.
- Don't summarize the deck contents in the message ("inside you'll find..."). The deck speaks for itself.
- Don't over-promise ("this will 10x your pipeline"). Soft confidence beats hype.

## After Message 2 (the next layer, not in this file)

The path forward depends on the prospect's response to the deck. Common scenarios:

- They reply with a question about a section → conversational continuation, eventually offer the call
- They reply asking for a call or teardown directly → book it
- They ghost → one nudge after 5-7 days (see `setter-playbook.md` Step 5), then mark dormant

## Common pitfalls

- Sending Message 1 to a freshly-accepted connection without their context loaded → high ignore rate. Spend 30 seconds on their profile first. Confirm they actually run an agency and fit the ICP (established, service-based, not a beginner).
- Sending Message 2 with a non-personalized deck → loses the entire wedge. Always run the personalization skill first.
- Sending Message 2 as plain text "here's a doc" without the personalized PDF attached → reads like spam.
- Following up with a third message before they've had time to read the deck → desperation tell. Wait 48-72 hours minimum.

## Tracking

Log every send in the LinkedIn connections Google Sheet (Mauro shares the link):
- Prospect name
- Agency
- Status (Message 1 sent / Yes received / Deck sent / Reply / Booked)
- First-message variant used (standard / solo-operator / established-owner)
- Date stamps per stage

This feeds the funnel-stage drop-off view so we know which message variant pulls best.
