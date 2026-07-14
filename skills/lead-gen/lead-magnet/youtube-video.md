# Lead Magnet Subtype: YouTube Video

**Version:** 2.1 (retargeted to Mauro's brand, 2026-07-14)
**Loaded with:** `_master.md` (always load both together)
**DM noun:** "breakdown" (never "video" — the post copy and image never reveal it's a video)

---

## What This Subtype Is

The magnet IS an existing YouTube video (or one about to record). The autodm sends the YouTube link. The post copy, the cover image, and the DM all reframe the video as a "breakdown" so the reader thinks they're getting a deep-dive document, then they click and the video earns them anyway.

Subtype identity: lowest production cost on the magnet side (the asset already exists or will exist), highest production cost on the disguise side (the cover image has to do real work to elevate the video to "course / framework / system" perception).

---

## When to Use This vs Other Subtypes

This subtype crosses with `case-study.md` and `industry-specific.md`. The decision rule:

| Source asset | Use this file |
|---|---|
| Existing YouTube video, regardless of content type | `youtube-video.md` |
| Written deep-dive on one transformation | `case-study.md` |
| Niche-packaged kit (multiple assets themed to one agency niche), even if it includes a video link | `industry-specific.md` |

If the link in the autodm goes to a YouTube URL, this is the right file.

---

## Input Form

Before drafting, get these from Mauro:

1. **YouTube video URL** (Claude fetches transcript and description automatically, then checks `research/transcripts/maurojpelle/` for an existing saved copy before fetching again per CLAUDE.md research protocol)
2. **OR video idea / topic summary** if the video doesn't exist yet
3. **Context if applicable** (which system, which case study, which framework the video covers)
4. **Trigger keyword** (3-7 chars, ALL CAPS, topic-related)
5. **Adjacent resource for the BTW upsell** (optional, see DM section below)
6. **The 3-5 core insights from the video** (Claude extracts these from the transcript)
7. **The single strongest claim or consequence** from the video — this becomes the post hook
8. **Trend signal** (is the topic hot right now? Used to weight the hook formula choice.)

---

## Research Phase (if video URL is provided)

Before drafting:

1. Check `research/transcripts/maurojpelle/[video-id].md` first per the CLAUDE.md research protocol. Don't re-fetch what's already saved.
2. If not saved, fetch the YouTube page, extract title + description + chapter headings, save to `research/transcripts/maurojpelle/[video-id].md` in the canonical format
3. Summarize 3-5 core insights from the transcript
4. Identify the strongest single claim — this becomes the post hook
5. Note the content format (breakdown / tutorial / framework / case study). This determines whether the post copy calls it a "breakdown", "framework", or "guide". **Never "video".**

---

## Asset Setup

The asset already exists (the YouTube video). Setup work is on the disguise layer:

### The "never-reveal-it's-a-video" rule

- Post copy never says "video", "watch", or "I just posted a YouTube video"
- Cover image never includes a play button, video thumbnail, or YouTube-branded element
- DM uses noun "breakdown" (per `_master.md` mapping)

The reader should feel they're being sent a written deep-dive. The video then over-delivers when they click.

### When the video doesn't exist yet

Mauro can draft the post + autodm BEFORE recording, then record the video against the brief that was already published. In this mode:
- The "3-5 core insights" become the brief the video is recorded against
- The cover image is designed first, the video matches it later
- Risk: if the recorded video doesn't match the published claims, the DM under-delivers. Verify before launching the autodm.

---

## Cover Image (Subtype-Specific — High Stakes)

The cover image does more work on LinkedIn than the copy. It has to raise perceived value before anyone reads a word. For YouTube subtype, the cover is the difference between "looks like a 14-minute video I won't watch" and "looks like a 30-page guide I want to read".

Inherits the base cover spec from `_master.md`.

### Subtype-specific options (pick one or combine)

**Option A: Table-of-contents preview**
- Screenshot of the video's chapters or sections, formatted as a table of contents
- Makes a 14-minute video look like a course with 8 modules
- Best when the video has clear chapter divisions

**Option B: Framework / diagram screenshot**
- A clean visual of a framework, system, or diagram from the video
- Best when the video presents a memorable framework that visualizes well

**Option C: Side-by-side before/after**
- Process-based videos (e.g., "before the system" vs "after the system" with anonymized content grids)
- Best when the video is transformation-focused

**Option D: Canva mock-up of thumbnail with overlaid text**
- Custom-designed cover that lists 3-5 specific things covered
- Used when the video itself doesn't visualize well, so the cover compensates

### Cover image brief format (output)

```
Image type: [A / B / C / D from above]
What to show: [Specific content to capture — e.g. "screenshot of chapters 1-5 with timestamps"]
Text overlay (if any): [Specific lines to add — usually the title + 3 bullets]
Goal: Make this look like a [course / guide / full breakdown], not a [N]-minute video
```

The cover image brief is mandatory output for this subtype. Skipping it = the post performs noticeably worse, every time.

---

## Post Hook Formulas (Subtype-Specific)

`_master.md` has the universal hook formulas. For YouTube video magnets specifically:

### LinkedIn (primary channel for video magnets)

- **"I [outcome with specifics]"** (outcome-led, verified numbers only)
- **"[Topic] is the 80/20 of [thing]"** (works when the video is about a tactical lever)
- **"You need to [contrarian action]"** (works when the video challenges a default)

### X (less common for YouTube videos, but works)

- **"[Tool] is INSANE for [task]"** when the video is a tool walkthrough
- **"[Problem statement], and that's killing your [outcome]"** for pain-led video topics

### Post body opening

For YouTube subtype, the post body usually includes a "So I've put together..." or "I broke down..." bridge that hides the format:
- "So I've just put together a 14 min breakdown so you can do the same."
- "I broke this down in a new resource based on what's working in the engine right now."

A "14 min vid" phrasing can appear in a LinkedIn body if the post needs it (LinkedIn audiences tolerate the "vid" framing), but never in the hook and never on X. Default to hiding the format entirely.

### Bullet structure (the "I break down:" list)

```
✓ How I'm planning to [specific next outcome]
✓ Insights that are applicable to [broader audience cut]
✓ The exact way I [specific tactical move]
```

The bullet list always promises: next steps + broader applicability + specific tactics. The promise is more concrete than the video itself can deliver in 14 minutes, which is fine — the cover image and the bullet list set expectations, the video over-delivers on at least one of them.

---

## DM Override

The DM uses the `_master.md` canonical with one optional addition: a BTW upsell line for an adjacent resource.

### Default (master canonical)

```
Hey (name), here's the breakdown:

LINK

P.S. Want a free teardown of your agency's content and inbound setup? Reply "yes" and we can chat about how it works.
```

### Optional variant (with BTW upsell)

Only use when there's a real adjacent resource to offer:

```
Hey (name), here's the breakdown:

LINK

BTW, want me to send over [adjacent resource, e.g. "my call-to-content prompt file"] as well? Let me know.

P.S. Want a free teardown of your agency's content and inbound setup? Reply "yes" and we can chat about how it works.
```

Rules for the BTW line:
- One line, low friction, easy yes/no
- The adjacent resource must actually exist. Don't offer something that's not ready to send.
- Skip the BTW entirely if there's no clear next resource. The default DM is fine.

---

## LeadShark Configuration

Per `_master.md` (no subtype override):

| Setting | Value |
|---|---|
| Trigger keyword | [magnet-specific, ALL CAPS] |
| DM template | (default or BTW variant from DM Override above) |
| Auto-connect | OFF |
| Partially Engage | ON |
| Follow-up DM | OFF |

---

## Output Checklist

Before scheduling, confirm:

- [ ] YouTube video URL is verified and the video is live (or scheduled to go live before the autodm fires)
- [ ] If video doesn't exist yet, the recording is on the calendar and the brief exists
- [ ] Transcript is saved to `research/transcripts/maurojpelle/[video-id].md` per the CLAUDE.md research protocol
- [ ] Post copy never says "video", "watch", or anything that reveals the format (except the optional "14 min vid" body line on LinkedIn)
- [ ] Cover image brief output exists (Option A / B / C / D selected)
- [ ] Cover image will not include play button, YouTube branding, or video thumbnail elements
- [ ] DM copy is the `_master.md` default (or BTW variant if adjacent resource exists)
- [ ] DM noun is "breakdown" (not "video")
- [ ] Keyword is ALL CAPS, 3-7 chars, topic-related
- [ ] LeadShark config: Auto-connect OFF, Partially Engage ON, Follow-up DM OFF
- [ ] Voice.md pre-publish checklist passed

---

## Anti-Patterns (Specific to This Subtype)

- Calling it a "video" in the post copy (the entire subtype premise is that the reader doesn't know it's a video until they click)
- Cover image with a play button or YouTube branding (kills the disguise)
- Skipping the cover image brief (this subtype lives or dies on the cover)
- BTW upsell for a resource that doesn't exist or isn't ready to send
- Re-using a video from 6+ months ago without re-checking that the claims still hold up
- Launching the autodm before the video is actually live (the link goes to a 404 — instant trust kill)
- Drafting from the video title alone, without reading the transcript (the strongest hook is almost never the title)
