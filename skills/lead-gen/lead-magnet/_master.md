# Lead Magnet Skill: Master File

**Version:** 2.1 (retargeted to Mauro's brand, 2026-07-14)
**Status:** Shared shell across all lead magnet subtypes. Always load this file together with the relevant subtype file.

---

## How This Skill Is Structured

Lead magnets split into 5 content-type subtypes:

- `prompt-swipe-file.md`: Claude / GPT prompts + curated hook / script / asset libraries
- `framework.md`: a framework for a content or acquisition system
- `case-study.md`: anonymized transformation breakdown
- `youtube-video.md`: existing YouTube video used as the magnet
- `industry-specific.md`: packaged for one agency niche (paid media / SEO / creative / social / etc.)

This `_master.md` file holds the shared 60% every subtype inherits:

- X / LinkedIn post template (with hook formulas + structure)
- DM template + noun mapping
- LeadShark configuration
- Cover image spec
- Voice rules summary

Each subtype file holds the unique 40%: input form, magnet structure, prompts, output checks.

When building a lead magnet, load `_master.md` + the relevant subtype file. Both together = the full skill.

---

## Required Reading

Read in full before drafting any output:

- `brand/voice.md`: voice rules, hard bans, signature moves, pre-publish checklist
- `brand/audience.md`: ICP (established agency owners) + verbatim pain phrases
- `brand/positioning.md`: the flag, the belief to break, proof rules

**Token resolution:** where this skill uses `{{tokens}}`:
- `{{linkedin_full_name}}` = Mauro's exact LinkedIn display name (it must match the profile so LinkedIn links it)
- `{{calendly_url}}` = [BOOKING LINK — pending]. Flag as a blocker instead of inventing a link.

**Production pipeline:** a written SOP for this brand's magnet pipeline doesn't exist yet. The Deliverables list below is the pipeline for now. Shipped magnets are archived in `brand/lead-magnets/`.

---

## Deliverables Per Lead Magnet

Each magnet ships with:

1. The magnet asset (format depends on subtype: Notion 5-pager, Gamma deck, Canva slides, YouTube video link, .md prompt file, etc.)
2. Cover image (branded header + dark body, see Cover Image spec below)
3. X post copy (autodm version)
4. LinkedIn post copy (autodm version, different structure from X)
5. DM message that gets sent when someone comments the keyword
6. LeadShark / Hypefury scheduling notes
7. Landing page (LP) — the email-capture page the DM links to. One per magnet. See Landing Page Spec below.

**Not shipped by default:**

- Follow-up DM: not used (LeadShark "Follow-up DM" setting is OFF)

**Email:** the welcome email delivers the magnet after LP signup (see Landing Page Spec). Standalone article emails remain a separate workstream.

---

## X Post Template

The hook formulas below were proven on the agency X account Mauro ran before this brand. The structures carry; revalidate performance on this account as its own data accrues and log top performers in `brand/` as they happen.

### Structure (6 parts)

```
[Hook line: 1 sentence]

[Setup: 1-2 sentences. What you built plus a credibility specifier.]

[Optional bridge line: used sparingly when the magnet is unusually high-value, e.g. "And now, for the next 48 hours I'm giving it away:"]

Inside the mini-guide:

- [Specific bullet 1]
- [Specific bullet 2]
- [Specific bullet 3]
- [Optional bullet 4-5]

Want a copy? Like + Comment "[KEYWORD]" and I'll send it over ASAP

(Must be following)
```

### Hook formulas (proven structures, trend-driven selection)

| Formula | Example (this brand's lane) | When to use |
|---|---|---|
| "[Tool] is CRAZY good" | "GPT Images 2.0 is CRAZY good." | A specific tool is having a moment (novel, trending, hot release) |
| "[Tool] is INSANE for [task]" | "Claude is INSANE for turning client calls into content." | Tool plus use-case combo, replicable across multiple use cases of the same tool. Proven opener for Claude-based auto-DM posts. |
| "[Problem statement], and that's killing your [outcome]" | "Your pipeline runs on referrals, and that's killing your growth." | Pain-led variant when no specific tool is the hook |

These formulas don't rank against each other in the abstract. Tool-led hooks work when the tool is genuinely having a moment, and fade when it isn't. Trend signal drives the choice. Hook formula reuse without a real trend behind it underperforms. Topic and hook formula selection should be informed by what's currently trending in the niche (AI systems for agency owners).

### Rules

- Bullets use dash (`-`), never checkmark
- Keyword in quotes, ALL CAPS, no punctuation around the quotes
- Always close with `(Must be following)` as a single line
- Always include "Like + Comment" as a double-action CTA. Single "Comment" tested worse.
- "I'll send it over ASAP" is the canonical close. "I'll send it over" is the shorter variant when space is tight.

### Word count target

120-160 words. Shorter often wins.

---

## LinkedIn Post Template

LinkedIn has different structural requirements than X. Do not reuse the X post on LinkedIn without restructuring.

### Structure (7 parts)

```
[Hook line: 1 sentence, often outcome-led or contrarian]

[Setup: 2-3 sentences. Explanation plus authority anchor plus what you built.]

[Optional aside: "(This is the exact system I run daily)"]

I break down: (or "Inside the guide:")

✓ [Specific bullet 1]
✓ [Specific bullet 2]
✓ [Specific bullet 3]
✓ [Optional bullet 4]

Here's how to get it:

1. Connect with me {{linkedin_full_name}}
2. Comment "[KEYWORD]" below

I'll send it over ASAP.

[Optional P.S. line: repost ask or related note]
```

### Hook formulas (proven structures)

| Formula | Example (this brand's lane) |
|---|---|
| "I [achieved outcome with specifics]" | "I turned one week of client calls into [N] pieces of content and [N] booked calls." (fill numbers from real data only) |
| "[Topic] is the 80/20 of [thing]" | "Lead magnets are the 80/20 of agency inbound." |
| "You need to [contrarian action]" | "You need to build content that doesn't look like content." |
| "[Thing] requires a NEW playbook" | "Agency inbound in 2026 requires a NEW playbook." |

Outcome-led hooks ("I did X and got Y") consistently drive the highest impressions on LinkedIn. Only use them with verified numbers.

### Rules

- Bullets use ✓ checkmark, not dash
- CTA is 2-step: Connect with `{{linkedin_full_name}}` + Comment KEYWORD
- The `{{linkedin_full_name}}` token resolves to Mauro's full LinkedIn display name exactly as it appears on the profile (it links to the profile).
- Close with "I'll send it over ASAP."
- Optional P.S. line: "P.S. Repost if you believe it will help anyone in your network!" Use occasionally, not every post.
- No "(Must be following)" on LinkedIn

### Word count target

180-220 words. Slightly longer than X because LinkedIn rewards depth.

### Authority anchors (rotate by post topic, gut call)

Candidates, all Mauro's own proof (per `brand/positioning.md`, any specific public number needs Mauro's sign-off before it ships):

- "I run the AI content engine for the agency I run ($300k/mo)" [SIGN-OFF REQUIRED]
- "I closed a $28k deal off X" [SIGN-OFF REQUIRED]
- "The engine I run daily for a real B2B agency" (operational, no number, safest default)
- "[RESULT — fill from the weekly acquisition analysis when available]"

No anchor is enforced as canonical. Selection is by gut depending on the post topic. Always include one in the first 2 paragraphs. Never borrow the agency's client anchors as personal proof.

---

## DM Template (Universal)

When someone comments the keyword, this auto-DM fires:

```
Hey (name), here's the (noun):

LINK

P.S. Want a free teardown of your agency's content and inbound setup? Reply "yes" and we can chat about how it works.
```

### Noun mapping per subtype

| Subtype | Noun |
|---|---|
| Prompt / swipe file | file |
| Framework | breakdown |
| Case study | breakdown |
| YouTube video | breakdown (NEVER "video". The post copy and the image never reveal it's a video.) |
| Industry-specific | guide |

### Rules

- `(name)` token is auto-populated by LeadShark from the LinkedIn or X profile
- LINK points to the magnet's Kit landing page (email gate), not the raw asset. The LP captures the email and the welcome email delivers the asset. See Landing Page Spec.
- The P.S. teardown-offer is the default until Mauro locks his call offer. Confirm the P.S. wording with him before a magnet ships. If a subtype warrants a different P.S., it overrides in the subtype file.
- No follow-up DM is configured (LeadShark setting OFF). Do not write follow-up DM copy.

---

## LeadShark Configuration

| Setting | Value |
|---|---|
| Trigger keyword | [magnet-specific, ALL CAPS] |
| DM template | (see DM Template section above with subtype noun substituted) |
| Auto-connect | OFF |
| Partially Engage | ON |
| Follow-up DM | OFF |

Auto-connect OFF is the verified live setting. Do not flip it to ON.

---

## Cover Image Spec

Every magnet has a cover image that gets attached to the X or LinkedIn post.

Consistent structure:

- Colored band header at top ([BRAND COLOR — visual identity for @maurojpelle pending; pick one color and reuse it on every magnet])
- Dark body below (near-black background, white text)
- Title in large white sans-serif at top of dark section
- 1-2 line subtitle in smaller white text
- "Created by @maurojpelle" credit line
- 4-6 bulleted items showing what's inside, each prefixed with a small emoji or icon
- Optional asset thumbnail or file icon at the bottom (used in prompt-pack covers)

The cover image is the magnet's identity in the feed. Skipping it = the post performs noticeably worse.

---

## Landing Page Spec

Every lead magnet ships with a landing page. The auto-DM link points to the LP, the user enters their email, and the welcome email delivers the magnet. This turns every magnet into an email-list builder. External validation: @mikefutia runs this live at scale.

### Platform decision

- **Kit (kit.com).** Velocity is the priority. A new magnet must not be blocked on building a page in a tool you fight with, and Kit LP templates clone in minutes.
- **Custom subdomain** mapped in Kit (e.g. `get.ghostedcalls.com`) so the LP sits on the brand's domain.
- **One LP per magnet** (skill-specific page). The headline matches the magnet name. Shared/generic pages convert worse (mikefutia structure).
- **Meta pixel + GA4** installed on every LP where retargeting and conversion tracking are in play.

### Structure (the LP has one job: capture the email)

- Eyebrow: `FREE RESOURCE`
- Headline = the magnet name (identical to the asset title)
- Subhead: 1-2 lines of value with an authority anchor (see Authority anchors above, sign-off required)
- 3-5 value bullets, each a bolded label + one line
- Single email field + button. Button text is an action ("Send me the system"), never "Submit"
- One proof line: [TESTIMONIAL — fill from social-proof/ (create as results come in)] or lean on the operational proof line
- Fine print: "Free. You'll also join my newsletter. Unsubscribe anytime." (sets the list expectation honestly)
- The magnet cover image alongside the copy

### Zero exits before conversion

The LP carries one action. No nav bar, no logo linking off-page, no portfolio button, no booking button. Every exit competes with the email capture and bleeds conversion.

Booking CTAs belong on the **thank-you page** and in the **welcome email**, after the email is captured. Post-conversion, stack every CTA you want.

### Delivery

On signup, the welcome email delivers the magnet (Notion link / file) and opens the call offer.

---

## Asset Build Constraints

Magnet assets are built via the Claude Chrome extension. The workflow: Mauro pastes the skill + content into Claude in the browser, the extension renders the output into Notion (or sometimes Miro). The extension output is **text + prompts only**. It does not render inline images, charts, or interactive elements.

This means:
- Visual elements (screenshots, diagrams, charts) are added manually by Mauro after the extension build
- When a visual is needed inside a magnet, mark the spot with `[VISUAL: description of what to insert]` so Mauro knows where to drop the image manually
- For frameworks specifically, the before/after panel can be inserted as text inside the Notion page if a visual isn't ready, then swapped for a designed panel later

---

## Voice Rules (Critical Reminders)

Full rules in `brand/voice.md`. Non-negotiables for lead magnet copy:

1. **No em dashes.** Never. Not in posts, not in DMs, not in magnet content. Replace with periods, commas, or rewrite the sentence.
2. **No "It's not X, it's Y" structures** or any variant of that contrast pattern.
3. **No "Most brands / Most people" openers.**
4. **No problem-to-purpose reversals** like "that's the filter doing its job" or "that's a feature not a bug."
5. **Numbers over adjectives.** Always cite a specific dollar, count, or time figure, and only real ones. Bracket-placeholder anything unverified.
6. **Speak from experience.** "The engine I run daily" beats "I have lots of experience."

Run every lead magnet post and DM through the pre-publish checklist in voice.md.

---

## After Producing All Outputs

Ask Mauro:

> "Do you want to adjust the keyword or the P.S. offer for this magnet, or stick with the defaults?"

Occasionally a topic warrants a different P.S. (a workflow-drop magnet might use P.S. "Want the n8n template for free? Reply 'flow'.").

---

## Future Direction

**1. Email signup gate before magnet delivery. → IMPLEMENTED 2026-06-29.** Now the standard for every magnet. See the Landing Page Spec section above. Kit-hosted LP, custom subdomain, one page per magnet, welcome email delivers the asset. `@mikefutia`'s skill-specific-LP structure validated the approach. Use anonymized testimonials per `feedback_client_naming`.

**2. HTML / styling prompt per page in the magnet asset.**
The Claude Chrome extension output is text + prompts only (see Asset Build Constraints above). Idea: add a small HTML / styling block per page so the page renders richer than plain text. Could be a layout spec, color block, sectioning. Status: idea-stage. When the workflow is locked, this becomes a build rule and propagates to every subtype's asset structure.

**3. Anything else surfaced during ongoing SOP rewrites.**
Add new directions here as they surface, with date stamps.

---

## File Output Convention

When this skill produces outputs in a session, organize them as:

```
[Magnet name]
├── X post copy
├── LinkedIn post copy
├── DM message (with noun substituted per subtype)
├── LeadShark config block
└── Cover image brief (text-described, for Canva / Notion screenshot)
```

The magnet asset itself is produced by the subtype file, not by `_master.md`.
