# Lead Magnet Skill: Master File

**Version:** 2.0
**Created:** 2026-05-25
**Replaces:** `skills/lead-gen/lead-magnet.md` (v1.0, to be retired once all subtypes ship)
**Status:** Shared shell across all lead magnet subtypes. Always load this file together with the relevant subtype file.

---

## How This Skill Is Structured

Lead magnets at Growthub split into 5 content-type subtypes (confirmed by Mauro 2026-05-25):

- `prompt-swipe-file.md`: Claude / GPT prompts + curated hook / script / asset libraries
- `framework.md`: a framework for a content or ad format
- `case-study.md`: anonymized client transformation
- `youtube-video.md`: existing YouTube video used as the magnet
- `industry-specific.md`: packaged for one vertical (supplement / pet / skincare / etc.)

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

- **Active account config** (e.g., `accounts/lorenzo-x/account-config.md` when running for Lorenzo's account). Substitute every `{{token}}` in this skill's output with the values from the active account-config. If no account is specified, ask which one.
- `brands/growthub/voice.md`: voice rules, hard bans, signature moves, 60-second pre-publish checklist (359 lines, all of it matters)
- `brands/growthub/audience.md`: ICP v2.2 (qualified buyer profile + verbatim pain phrases)

The production pipeline this skill plugs into:

- `ops/lead-magnet-autodm-sop.md`: 13-step production pipeline, Mauro and Joao roles, Hypefury + LeadShark distribution

---

## Deliverables Per Lead Magnet

Each magnet ships with:

1. The magnet asset (format depends on subtype: Notion 5-pager, Gamma deck, Canva slides, YouTube video link, .md prompt file, etc.)
2. Cover image (yellow Growthub-branded header + dark body, see Cover Image spec below)
3. X post copy (autodm version)
4. LinkedIn post copy (autodm version, different structure from X)
5. DM message that gets sent when someone comments the keyword
6. LeadShark / Hypefury scheduling notes
7. Landing page (LP) — the email-capture page the DM links to. One per magnet. See Landing Page Spec below. (Standard since 2026-06-29.)

**Not shipped by default:**

- Follow-up DM: not used (LeadShark "Follow-up DM" setting is OFF)

**Email:** the welcome email now delivers the magnet after LP signup (see Landing Page Spec). Standalone article emails remain a separate workstream.

---

## X Post Template

Based on top X performers Apr-May 2026 (verified in `brands/growthub/best-performing-posts.md` and image set provided 2026-05-25).

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

### Hook formulas (proven, trend-driven selection)

| Formula | Example post | Views | When to use |
|---|---|---|---|
| "[Tool] is CRAZY good" | "GPT Images 2.0 is CRAZY good." | 73.2K | A specific tool is having a moment (novel, trending, hot release) |
| "[Tool] is INSANE for [task]" | "Claude is INSANE for ad scriptwriting." | 51.8K, 45.5K, 40.6K (3 separate posts) | Tool plus use-case combo, replicable across multiple use cases of the same tool |
| "[Problem statement], and that's killing your performance" | "Your ads look like ads, and that's killing your performance." | 41K | Pain-led variant when no specific tool is the hook |

These formulas don't rank against each other in the abstract. The GPT Images 2.0 post hit 73K because GPT Images 2.0 was the novel tool at that moment, not because the formula is universally stronger. The INSANE formula has been replicated 3 times and works as a workhorse. Trend signal drives the choice. Hook formula reuse without a real trend behind it underperforms.

This is why the trendjacking system (X API integration, greenlit 2026-05-26) feeds directly into this skill. Topic and hook formula selection should be informed by what's currently trending in the niche. See `project_trendjack_system` memory for status.

### Rules

- Bullets use dash (`-`), never checkmark
- Keyword in quotes, ALL CAPS, no punctuation around the quotes
- Always close with `(Must be following)` as a single line
- Always include "Like + Comment" as a double-action CTA. Single "Comment" tested worse.
- "I'll send it over ASAP" is the canonical close. "I'll send it over" is the shorter variant when space is tight.

### Word count target

120-160 words. Shorter often wins. The AI / GPT Images 2.0 post (top performer at 73K views) is 78 words.

---

## LinkedIn Post Template

LinkedIn has different structural requirements than X (verified in image set 2026-05-25). Do not reuse the X post on LinkedIn without restructuring.

### Structure (7 parts)

```
[Hook line: 1 sentence, often outcome-led or contrarian]

[Setup: 2-3 sentences. Explanation plus authority anchor plus what you built.]

[Optional aside: "(These are the strategies my team & I are currently using)"]

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

### Hook formulas (proven)

| Formula | Example post | Impressions |
|---|---|---|
| "I [achieved big outcome with specifics]" | "I took my pet brand client from $29k to $750k/month." | 21,350 |
| "I've [scaled X clients/brands] and generated $[Y] for them" | "I've scaled over 10 pet brands and generated $20M for them." | 16,321 |
| "[Topic] is the 80/20 of [thing]" | "Hooks are the 80/20 of ANY ad." | 15,175 |
| "You need to [contrarian action]" | "You need to create ads that don't look like ads." | 11,872 |
| "[Thing] requires a NEW playbook" | "Scaling on Meta on 2026 requires a NEW playbook." | 11,760 |

The outcome-led formula ("I scaled X to Y") consistently drives the highest impressions on LinkedIn.

### Rules

- Bullets use ✓ checkmark, not dash
- CTA is 2-step: Connect with `{{linkedin_full_name}}` + Comment KEYWORD
- The `{{linkedin_full_name}}` token resolves to the account's full name with any accents intact (it links to the profile). For Lorenzo's account that's "Lorenzo Pravatà".
- Close with "I'll send it over ASAP."
- Optional P.S. line: "P.S. Repost if you believe it will help anyone in your network!" Use occasionally, not every post.
- No "(Must be following)" on LinkedIn

### Word count target

180-220 words. Slightly longer than X because LinkedIn rewards depth.

### Authority anchors (rotate by post topic, gut call)

- "$107M+ in managed Meta ad spend"
- "$100M+ on Meta ads"
- "$20M generated for [N] [vertical] brands" (use for industry-specific posts)
- "7/8-figure clients" (use when a dollar number doesn't fit the sentence)

No anchor is enforced as canonical. Selection is by gut depending on the post topic. Always include one of these in the first 2 paragraphs.

---

## DM Template (Universal)

When someone comments the keyword, this auto-DM fires:

```
Hey (name), here's the (noun):

LINK

P.S. Would you like a free audit for your brand? Reply "yes" and we can chat about how it works.
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
- LINK points to the magnet's Kit landing page (email gate), not the raw asset. The LP captures the email and the welcome email delivers the asset. See Landing Page Spec. (Pre-2026-06-29 magnets linked the asset directly.)
- The P.S. audit-offer is canonical. Other P.S. variations have been tested but this is the default. If a subtype warrants a different P.S., it overrides in the subtype file.
- No follow-up DM is configured (LeadShark setting OFF). Do not write follow-up DM copy.

---

## LeadShark Configuration

Per current production setup (confirmed 2026-05-25):

| Setting | Value |
|---|---|
| Trigger keyword | [magnet-specific, ALL CAPS] |
| DM template | (see DM Template section above with subtype noun substituted) |
| Auto-connect | OFF |
| Partially Engage | ON |
| Follow-up DM | OFF |

The v1 skill (`skills/lead-gen/lead-magnet.md`) listed Auto-connect as ON. That was incorrect. OFF is the live setting.

---

## Cover Image Spec

Every magnet has a cover image that gets attached to the X or LinkedIn post.

Consistent structure across all winning posts:

- Yellow band header (Growthub brand yellow) at top
- Dark body below (near-black background, white text)
- Title in large white sans-serif at top of dark section
- 1-2 line subtitle in smaller white text
- "Created by Growthub.Agency" or "Created by @growthub.agency" line
- 4-6 bulleted items showing what's inside, each prefixed with a small emoji or icon
- Optional asset thumbnail or file icon at the bottom (used in prompt-pack covers)

The cover image is the magnet's identity in the feed. Skipping it = the post performs noticeably worse.

---

## Landing Page Spec

Every lead magnet ships with a landing page. The auto-DM link points to the LP, the user enters their email, and the welcome email delivers the magnet. This turns every magnet into an email-list builder. Implemented 2026-06-29 (promoted from Future Direction #1). External validation: @mikefutia runs this live at scale.

### Platform decision (2026-06-29)

- **Kit (kit.com), not Webflow.** Velocity is the priority. A new magnet must not be blocked on building a page in a tool we fight with, and Kit LP templates clone in minutes. Webflow was tried before and is painful to iterate.
- **Custom subdomain** mapped in Kit (e.g. `get.growthub.agency`) so the LP sits on our domain without touching Webflow.
- **One LP per magnet** (skill-specific page). The headline matches the magnet name. Shared/generic pages convert worse (mikefutia structure).
- **Meta pixel + GA4** installed on every LP, so we retarget non-converters and tie signups into conversion tracking.

### Structure (the LP has one job: capture the email)

- Eyebrow: `FREE RESOURCE`
- Headline = the magnet name (identical to the asset title)
- Subhead: 1-2 lines of value with a scale anchor ($107M+ / past $1M/month)
- 3-5 value bullets, each a bolded label + one line
- Single email field + button. Button text is an action ("Send me the system"), never "Submit"
- One proof line or anonymized testimonial (or lean on $107M+)
- Fine print: "Free. You'll also join the Growthub newsletter. Unsubscribe anytime." (sets the list expectation honestly)
- The magnet cover image alongside the copy

### Zero exits before conversion

The LP carries one action. No nav bar, no logo linking off-page, no portfolio button, no Calendly button. Every exit competes with the email capture and bleeds conversion.

Portfolio and Calendly CTAs belong on the **thank-you page** and in the **welcome email**, after the email is captured. Post-conversion, stack every CTA you want.

### Delivery

On signup, the welcome email delivers the magnet (Notion link / file) and opens the audit / call offer.

---

## Asset Build Constraints

Magnet assets are built via the Claude Chrome extension. The workflow: Mauro pastes the skill + content into Claude in the browser, the extension renders the output into Notion (or sometimes Miro). The extension output is **text + prompts only**. It does not render inline images, charts, or interactive elements.

This means:
- Visual elements (screenshots, diagrams, charts) are added manually by Mauro after the extension build
- When a visual is needed inside a magnet, mark the spot with `[VISUAL: description of what to insert]` so Mauro knows where to drop the image manually
- For frameworks specifically, the before/after panel can be inserted as text inside the Notion page if a visual isn't ready, then swapped for a designed panel later

---

## Voice Rules (Critical Reminders)

Full rules in `brands/growthub/voice.md`. Non-negotiables for lead magnet copy:

1. **No em dashes.** Never. Not in posts, not in DMs, not in magnet content. Replace with periods, commas, or rewrite the sentence.
2. **No "It's not X, it's Y" structures** or any variant of that contrast pattern.
3. **No "Most brands / Most people" openers.**
4. **No problem-to-purpose reversals** like "that's the filter doing its job" or "that's a feature not a bug."
5. **Numbers over adjectives.** Always cite a specific dollar, count, or time figure.
6. **Speak from experience.** "After $107M+ in spend" beats "we have lots of experience."

Run every lead magnet post and DM through the 60-second pre-publish checklist at the bottom of voice.md.

---

## After Producing All Outputs

Ask Mauro:

> "Do you want to adjust the keyword or the P.S. offer for this magnet, or stick with the defaults?"

The default audit-offer P.S. has held up across most magnets. Occasionally a topic warrants a different P.S. (a workflow-drop magnet might use P.S. "Want the n8n template for free? Reply 'flow'.").

---

## Future Direction (2026-05-26)

Three ideas under consideration. None implemented yet. Do not author copy or rules for these until the workflow is locked.

**1. Email signup gate before magnet delivery. → IMPLEMENTED 2026-06-29.** Now the standard for every magnet. See the Landing Page Spec section above. Kit-hosted LP, custom subdomain, one page per magnet, welcome email delivers the asset. `@mikefutia`'s skill-specific-LP structure validated the approach; Growthub uses an anonymized testimonial per `feedback_client_naming`.

**2. HTML / styling prompt per page in the magnet asset.**
The Claude Chrome extension output is text + prompts only (see Asset Build Constraints above). Idea: add a small HTML / styling block per page so the page renders richer than plain text. Could be a layout spec, color block, sectioning. Status: idea-stage, raised by Mauro 2026-05-26. When the workflow is locked, this becomes a build rule and propagates to every subtype's asset structure.

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
