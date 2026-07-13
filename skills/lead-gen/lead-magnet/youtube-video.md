# Lead Magnet Subtype: YouTube Video

**Version:** 2.0
**Created:** 2026-05-26
**Migrated from:** `skills/content/yt-to-autodm.md` (v1.2, dated 2026-04-15)
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
| Written deep-dive on one client transformation | `case-study.md` |
| Vertical-packaged kit (multiple assets themed to one industry), even if it includes a video link | `industry-specific.md` |

If the link in the autodm goes to a YouTube URL, this is the right file.

---

## Input Form

Before drafting, get these from Mauro:

1. **YouTube video URL** (Claude fetches transcript and description automatically, then checks `research/transcripts/lorenzopravata/` for an existing saved copy before fetching again per CLAUDE.md Research Protocol)
2. **OR video idea / topic summary** if the video doesn't exist yet
3. **Client context if applicable** (which case study, which vertical, which framework the video covers)
4. **Trigger keyword** (3-7 chars, ALL CAPS, topic-related)
5. **Adjacent resource for the BTW upsell** (optional, see DM section below)
6. **The 3-5 core insights from the video** (Claude extracts these from the transcript)
7. **The single strongest claim or consequence** from the video — this becomes the post hook
8. **Trend signal** (is the topic hot right now? Used to weight the hook formula choice.)

---

## Research Phase (if video URL is provided)

Before drafting:

1. Check `research/transcripts/lorenzopravata/[video-id].md` first per CLAUDE.md Section 9. Don't re-fetch what's already saved.
2. If not saved, fetch the YouTube page, extract title + description + chapter headings, save to `research/transcripts/lorenzopravata/[video-id].md` in the canonical format
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

Mauro can draft the post + autodm BEFORE recording, then the video is recorded against the brief that was already published. This is the workflow Lorenzo has used for the case study videos. In this mode:
- The "3-5 core insights" become the brief Lorenzo records against
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
- Process-based videos (e.g., "before our system" vs "after our system" with anonymized creative grids)
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

`_master.md` has the universal hook formulas. For YouTube video magnets specifically, the patterns that have worked:

### LinkedIn (primary channel for video magnets per past performance)

- **"I took [client framing] from [number] to [bigger number]"** (pet brand $29K → $750K, 21K impressions)
- **"[Topic] is the 80/20 of [thing]"** (works when the video is about a tactical lever)
- **"You need to [contrarian action]"** (works when the video challenges a default)

### X (less common for YouTube videos, but works)

- **"[Tool] is INSANE for [task]"** when the video is a tool walkthrough
- **"[Problem statement], and that's killing your performance"** for pain-led video topics

### Post body opening

For YouTube subtype, the post body usually includes a "So I've put together..." or "I broke down..." bridge that hides the format:
- "So I've just put together a 14 min vid breaking it down so you can do the same." (the pet brand $29K → $750K post — note "14 min vid" can be revealed in the body even though "video" isn't used in the hook. This is the one place where the format leaks.)
- "I broke this down in a new resource based on what's working for our clients right now."

The "14 min vid" reveal is an exception, not a rule. It works because the post is on LinkedIn where the audience is more tolerant of "vid" framing. On X, the format reveal should be even more hidden.

### Bullet structure (the "I break down:" list)

```
✓ How we're planning to [specific next outcome]
✓ Insights that are applicable to [broader audience cut]
✓ The exact way we [specific tactical move]
```

The bullet list always promises: next steps + broader applicability + specific tactics. The promise is more concrete than the video itself can deliver in 14 minutes, which is fine — the cover image and the bullet list set expectations, the video over-delivers on at least one of them.

---

## DM Override

The DM uses the `_master.md` canonical with one optional addition: a BTW upsell line for an adjacent resource.

### Default (master canonical)

```
Hey (name), here's the breakdown:

LINK

P.S. Would you like a free audit for your brand? Reply "yes" and we can chat about how it works.
```

### Optional variant (with BTW upsell)

Only use when there's a real adjacent resource to offer:

```
Hey (name), here's the breakdown:

LINK

BTW, want me to send over [adjacent resource, e.g. "our 5-format static ads prompt file"] as well? Let me know.

P.S. Would you like a free audit for your brand? Reply "yes" and we can chat about how it works.
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

The v1.2 yt-to-autodm.md skill listed Auto-connect ON and Follow-up DM enabled. Both are wrong per current production. OFF on both.

---

## Output Checklist

Before handing off to Joao for scheduling, confirm:

- [ ] YouTube video URL is verified and the video is live (or scheduled to go live before the autodm fires)
- [ ] If video doesn't exist yet, the recording is on the calendar and Lorenzo has the brief
- [ ] Transcript is saved to `research/transcripts/lorenzopravata/[video-id].md` per CLAUDE.md research protocol
- [ ] Post copy never says "video", "watch", or anything that reveals the format (except optional "14 min vid" body line on LinkedIn)
- [ ] Cover image brief output exists (Option A / B / C / D selected)
- [ ] Cover image will not include play button, YouTube branding, or video thumbnail elements
- [ ] DM copy is the `_master.md` default (or BTW variant if adjacent resource exists)
- [ ] DM noun is "breakdown" (not "video")
- [ ] Keyword is ALL CAPS, 3-7 chars, topic-related
- [ ] LeadShark config: Auto-connect OFF, Partially Engage ON, Follow-up DM OFF
- [ ] Voice.md 60-second pre-publish checklist passed

---

## Anti-Patterns (Specific to This Subtype)

- Calling it a "video" in the post copy (the entire subtype premise is that the reader doesn't know it's a video until they click)
- Cover image with a play button or YouTube branding (kills the disguise)
- Skipping the cover image brief (this subtype lives or dies on the cover)
- BTW upsell for a resource that doesn't exist or isn't ready to send
- Re-using a video from 6+ months ago without re-checking that the claims still hold up
- Launching the autodm before the video is actually live (the link goes to a 404 — instant trust kill)
- Drafting from the video title alone, without reading the transcript (the strongest hook is almost never the title)

---

## Migration Notes

This file replaces `skills/content/yt-to-autodm.md` (v1.2). Key changes:

- Email section removed (per Mauro 2026-05-26: emails are reserved for articles, not lead magnets)
- Follow-up DM section removed (LeadShark Follow-up DM setting is OFF in current production)
- LeadShark config corrected (Auto-connect OFF, Follow-up DM OFF — both were wrong in v1.2)
- DM aligned to `_master.md` canonical with BTW upsell as optional variant
- Research phase explicitly references CLAUDE.md Section 9 (fetch once, save always)
- Old file at `skills/content/yt-to-autodm.md` to be deleted in the v1 retirement commit (task #7)
- CLAUDE.md routing table to be updated in the same commit
