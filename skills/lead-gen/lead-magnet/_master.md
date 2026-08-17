# Lead Magnet Skill: Master File

**Version:** 2.3 (2026-08-17)
**Status:** The live magnet system. Shared shell across all subtypes. Always load this file together with the relevant subtype file.

> **Note on the JK Molina research.** A candidate second model (the "insight model", give the least that proves you have the answer) is written up at `research/jk-molina/candidate-insight-model.md`. It is **not adopted** and nothing from it runs here. That file carries an adopt / adapt / reject table awaiting Mauro's call. Do not import from it without his sign-off.

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

## Title Engineering (applies to every subtype)

**Ported from the agency repo 2026-08-06.** The rules are universal. The evidence behind them is the agency's, and is labelled as such, so replace it with @maurojpelle data as that accrues.

### The formula

`[topic a beginner recognises] + [artifact noun] + [number or year]`

Three jobs. The topic earns the scroll, the **artifact noun** creates the perceived value, the number or year makes it feel current and finite.

### The artifact noun is non-negotiable

The title has to name the thing that lands in their DMs.

Approved artifact nouns: guide, playbook, checklist, sheet, kit, system, workflow, prompt file, stack, template, swipe file, breakdown, tutorial, formats, prompts.

### The evidence (the agency's account, 40 rows, pulled 2026-07-31)

| Post | Views | Comment rate |
|---|---|---|
| AUTODM AI | 59,471 | 0.9% |
| Winning Hooks Guide | 38,724 | 1.3% |
| Andromeda 101 | 27,918 | **3.9%** |
| Andromeda Redo | 20,934 | **4.0%** |
| AI Statics Workflow | 21,057 | 3.5% |

Two separate effects, and they are not the same effect:

- **Breadth drives reach.** "AI" is the widest word available and pulled the highest views on the account.
- **A concrete, currently-urgent named thing drives redemption.** The Andromeda posts hit roughly 4x the comment rate. Comments are the redemption action, so this is the number that matters for leads.

Broad enough that a beginner recognises it, concrete enough that it feels urgent.

**For @maurojpelle the equivalent of "Andromeda" is whatever is currently live and unresolved for agency owners.** Right now that is the skills-to-agents transition. Swap the anchor as the live problem changes.

### Hard bans on titles

- **No invented concept nouns.** Nobody wants a "camouflage static" or an "autopsy".
- **No diagnoses or questions.** "Why Your Ads Stopped Scaling" promises nothing received.
- **No sophistication signalling.** Broad title for reach, real depth for the qualified reader.

### Worked corrections (the agency's account, kept as pattern reference)

| Rejected | Shipped |
|---|---|
| The Camouflage Static Swipe File | Ads That Don't Look Like Ads (Full Playbook) |
| The 3-Bottleneck Ad Account Audit | The Meta Ads Audit Checklist (2026) |
| The Losing-Ad Autopsy Sheet | The Losing Ads Review Sheet |
| Rebuild a Competitor's Winner (Legally) | The Competitor Ad Teardown Kit |
| The $3k to $100k a Day Ladder | The Scaling Checklist: $3k to $100k a Day |

The pattern in every fix: stop being clever, name the object.

---

## THE $100 BAR

**Every lead magnet has to be worth at least $100 to the person who asks for it.** Not $100 of reading. $100 of work they did not have to do.

1. The magnet is **a thing you fill in, not a thing you read.** If a page has no blank field, no row to score, and no verdict at the end, it is an article wearing a magnet's title.
2. The last two pages are usually where the $100 lives. The explainer pages are setup.

The four things that clear the bar, in order of value:

| | What it is |
|---|---|
| **Paste-ready prompts** | With variable slots, chained, in order. Including at least one that tells them no |
| **A real swipe file** | Named examples pulled apart, plus a blank sheet so they map their own |
| **A scoring artifact** | They put their own numbers in and get a verdict out: kill, iterate, scale |
| **A filled-in worked example** | The template completed for a real case, so they can see what done looks like |

**The test before shipping any magnet:** if someone read the whole thing and did nothing differently tomorrow, it failed, regardless of how good the writing was.

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

Every magnet has a cover image that gets attached to the X or LinkedIn post. It is the magnet's identity in the feed, and skipping it makes the post perform noticeably worse.

### Default: screenshot the magnet's own home page (Mauro, 2026-08-06)

**"Usually the cover image for the Notion, Gamma, or just most lead magnets is the screenshot of the home page tbh."**

The default is not a designed card. It is a clean screenshot of the asset's own first screen:

- **Notion magnet** -> the parent delivery page, showing title, intro callout and the list of nested subpages
- **Gamma deck** -> slide one
- **PDF or HTML doc** -> page one
- **Prompt pack** -> the first page with a prompt visible

**Why.** It shows the reader the actual thing they are about to receive, and the visible subpage list does the "what's inside" job for free. A designed card promises, a screenshot proves. It is also faster, since the asset already exists by the time the cover is needed.

**What makes a screenshot cover work:**

- Crop tight, no browser chrome, no sidebar, no cursor
- Title legible at feed thumbnail size. If it isn't, zoom the page before capturing
- Enough of the subpage list visible that the reader can count the pages
- No internal UI: no comment bubbles, no Share button, no member avatars
- Retina capture, then downscale. A 1x screenshot looks soft in feed

### Fallback: the designed card

Use when there is no asset to screenshot yet, or its first screen is text-heavy and dull.

- Colored band header at top ([BRAND COLOR - visual identity for @maurojpelle pending; pick one and reuse it on every magnet])
- Dark body below, near-black background, white text
- Title in large white sans-serif
- 1-2 line subtitle
- "Created by @maurojpelle" credit line
- 4-6 bulleted items showing what's inside

Build the designed card as HTML and screenshot it. Do not generate it with an image model, the title and bullets have to be exactly right.

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

### Notion structure rule

Every section of a magnet ("Page 1", "Page 2", ...) is a **real, separately created Notion child page** nested inside the parent delivery page. Never headings, toggles, or dividers stacked on one page.

Build order: one create-pages call for the parent, then one call per section with the parent as its parent, then reference the children in the parent content. End state: parent = cover + intro + N clickable subpages + CTA + credit line. **If a build ends with all content on the parent page, it is wrong. Rebuild it as subpages.**

### In-asset prompt blocks

Every page of a Notion magnet ships with two generation-ready prompt blocks, so the visuals never depend on inventing prompts later.

1. **Page image prompt** — a quote block where the image should render: `> **PAGE IMAGE PROMPT (16:9, <style>):** ...`
2. **HTML style prompt** — a per-page prompt that renders that page as a styled HTML block: `> **HTML STYLE PROMPT (Claude):** ...`

Three allowed image styles, rotate across them:

| Style | When |
|---|---|
| **Real example screenshot** | Any page teaching a format or structure. **Strongest option, use it most** |
| **Worked example** | Any page whose deliverable is a template. Show it filled in |
| **Doodle scene** | Concept and mechanism pages only |

**The rule: the image ADDS to the page, it never restates it.** Cover the page text. Does the image still teach something? If not, it is decoration and it is wrong.

**Banned outright:** an infographic or "key takeaways" graphic whose content is a restatement of the text on the same page.

### Render vs generate

**Render as HTML and screenshot** when the image has more than ~30 words that must be exactly right, any table, checklist, aligned diagram boxes, or numbers you will want to change later.

**Generate with an image model** only for illustrative work: a doodle, a scene, a metaphor, one or two short labels.

**Never generate a fake example of a real thing.** A fabricated ad, a fabricated dashboard, a fabricated screenshot with invented engagement numbers. If the page teaches by example, the example has to be real.


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
