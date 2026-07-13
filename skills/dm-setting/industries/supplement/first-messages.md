# Supplement DM: Two-Message Punch

The opening DM sequence Nathan runs for supplement-brand prospects on LinkedIn. Targets founder or CMO of a supplement brand actively running Meta ads.

**Goal:** turn a connection acceptance into a deck delivery, then into a booked call. Two messages handle the YES path. Follow-up handlers (no-response, deferred-yes, polite-no) live in `objections.md`.

## Message 1: Permission ask (PRIMARY, per Mauro 2026-05-07)

Send this immediately after connection acceptance. Short, observation-led, ends with an easy yes question. No authority anchor in the opener. Keep it conversational and low-pressure. The deck does the authority work.

```
Hey [First name], quick one.

Saw you were running ads for [BrandName]. I put together a short doc on what's working for the supplement brands we manage this year to scale on Meta. Formats, creative strategy, mechanic stuff in general.

Want me to send it over?
```

### CTA close options (pick whichever feels natural)

The closing question is the highest-leverage line in Message 1. Three equally-good options, ranked by tone:

| CTA | Tone | When to use |
|---|---|---|
| `Want me to send it over?` | Direct, casual | Default. Works for almost everyone. |
| `Cool if I send it?` | Softer, very casual | When the prospect's profile is informal / younger / scrappy founder vibe. |
| `Worth me sending?` | Confident, slightly more poised | When the prospect is a CMO / VP / more senior tier. |

Avoid the original gerund form ("would that be something you'd like me sending over"). Slightly clunky cadence.

### Optional pickups

If you want to layer authority into Message 1 (use sparingly, the soft version above tests cleaner without it), here are the strongest insertable lines:

- After the second sentence: `(We manage $17M+ in supplement spend on Meta.)`
- After the second sentence: `(We manage multiple supplement brands past $1M/month.)`
- After the closing question: `Genuinely useful even if we never end up working together.`

Treat these as inserts not requirements. The default version above is the lead.

### Variants for tone

**Founder-coded variant** (when the prospect is a founder of a younger / scrappier brand):

```
Hey [First name], quick one.

Saw [BrandName] running ads on Meta. Put together a short doc on what's working for the supplement brands we manage this year. Formats, creative strategy, the mechanic side.

Want me to send it over?
```

**CMO-coded variant** (when the prospect is a marketing director / CMO, slightly more poised):

```
Hi [First name],

Saw [BrandName] is running ads on Meta. I put together a short doc on what's working for the supplement brands we manage at Growthub this year. Format spread, subscription mechanics, the stuff that's distinguishing scaled brands from plateaued ones.

Worth me sending it?
```

### What NOT to do in Message 1

- Don't pitch services or mention pricing.
- Don't ask for a call directly. The deck is the wedge, not the call.
- Don't lead with "I help [audience] do [thing]". Too templated, gets ignored.
- Don't stack multiple questions. One easy yes question only.
- Don't use em dashes, "not X but Y" structures, or generic agency-speak.

## Message 2: Deck delivery (after YES)

Send within a few hours of their yes. Attach the personalized PDF (built via the personalization skill at `skills/content/linkedin-docs/personalization-guide.md`).

```
Sent. Personalized for [BrandName] specifically: [attached PDF].

Took ~30 min to adapt the system around your brand. Feel free to forward to your CMO or whoever runs your Meta ad creative.

Let me know what lands. Happy to walk through any section that's unclear.
```

### What this does

- Frames the deck as personalized work product (not a generic giveaway).
- Suggests the prospect forward it internally, opening the multi-stakeholder path that ~30% of qualified buyers travel.
- Soft no-CTA close. The deck does the work. The call comes later if they self-initiate.

### What NOT to do in Message 2

- Don't ask for the call inside Message 2. Wait for them to engage with the deck first.
- Don't summarize the deck contents in the message ("inside you'll find..."). The deck speaks for itself.
- Don't over-promise ("this will 10x your account"). Soft confidence beats hype.

## After Message 2 (the next layer, not in this file)

The path forward depends on the prospect's response to the deck. Common scenarios:

- They reply with a question about a section → conversational continuation, eventually offer the call
- They reply asking for an audit / call directly → book it
- They ghost → nudge sequence in `objections.md`

## Italian-market variant

Per Apr 30 Mauro / Nathan call, Italian supplement brands need a "super-direct" pre-drafted message. Italian variant TBD. Mauro committed to drafting it. Until that ships, default to the standard variant in English.

## Common pitfalls

- Sending Message 1 to a freshly-accepted connection without their context loaded → high ignore rate. Spend 30 seconds on their profile first.
- Sending Message 2 with a non-personalized deck → loses the entire wedge. Always run the personalization skill first.
- Sending Message 2 as plain text "here's a doc" without the personalized PDF attached → reads like spam.
- Following up with a third message before they've had time to read the deck → desperation tell. Wait 48-72 hours minimum.

## Tracking (per Apr 30 call)

Log every send in the LinkedIn connections Google Sheet:
- Prospect name
- Brand
- Status (Message 1 sent / Yes received / Deck sent / Reply / Booked)
- First-message variant used (standard / founder-coded / CMO-coded)
- Date stamps per stage

This feeds the funnel-stage drop-off dashboard so we know which message variant pulls best.
