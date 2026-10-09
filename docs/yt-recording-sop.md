# YT recording SOP (personal)

One page. How and when Mauro records a video off a v2 board in `boards/yt/v2/`.
Set 9 Oct 2026. Sources: `boards/yt/v2/BRIEF.md`, the boards' `*.notes.md`, `skills/youtube/`.

## When

- **Slot: Thursday 14:00 to 16:00 (Madrid), every week.** In the week of 12 to 16 Oct this is the
  longest open block on the calendar: lunch ends 14:00, nothing until the EOD recap at 17:15.
- **Back-up slot: Wednesday 14:00 to 16:00.** Open until the weekly YouTube review call at 16:30,
  so a recording made then can go straight into that review.
- Calendar checked: the work calendar only (read only, 9 Oct). The ghostedcalls calendar was not
  readable. `[NEEDS: check the slot against the ghostedcalls calendar]`.
- The 10:00 to 11:30 Build block stays for building. Record in the afternoon slot.
- One video per slot. A v2 board runs 20 to 25 minutes on screen (BRIEF rule 4).

## Before the slot (the day before, 10 minutes)

1. Pick the board in `boards/yt/v2/index.html`. Read its `<slug>.notes.md` once, top to bottom.
2. Confirm or cut every red `[NEEDS: x]` on the board. The list is in the format's `meta.json`.
   A `[NEEDS]` tag must not be on screen in a published video.
3. Pick the title from the 3 in `meta.json`. The title decides what the hook promises.

## Setup (10 minutes)

- **Screen recorder:** `[NEEDS: which app records screen + face + mic]`. No recorder is named in the repo.
- **Mic:** `[NEEDS: which mic]`. Do a 10-second test take and play it back.
- **Screen 1, the recording:** open the board in Chrome. Press **F** for fullscreen.
  Press **H** to hide the control bar. Check that nothing but the board is visible.
- **Screen 2, your notes:** open the same board in a second window. Press **N** to show the
  presenter notes. Move it with the bar (Prev / Next, or Frames to jump) to follow along.
- Close Slack, mail and notifications. Arrow keys and Space move the frames on screen 1.

## Per board (the take)

1. **Hook, first 30 seconds:** result first, then the promise, then "today we go over" the 3
   sections. Frames 1 to 3 hold it on every board. If the hook is weak, record it again
   before you continue. The rest of the video depends on it.
2. **One take per section.** A board has a hook, 3 sections and the CTA. Stop the recording
   only at a section edge (the "Section one / two / three" frame).
3. **On a mistake:** stop talking, wait 2 seconds, go back one frame (Left arrow) and say the
   line again. Do not stop the recording. The pause marks the cut for the edit.
4. **A full restart only if the hook fails.** Everything else is fixed with the pause-and-repeat rule.
5. **CTA frame:** "Link in the description", plus the offer name "Agency Booked Calls". No price, no URL.

## After the recording

- **File:** `[NEEDS: where raw files go]`. Proposed name: `<NN>-<slug>-<YYYY-MM-DD>.mov`,
  where NN and slug match the board file.
- **Editor:** `[NEEDS: who edits]`. The repo names Juan for articles, replies and the lead-magnet test,
  and no one for video edits.
- Write the date and the board name in `BACKLOG.md` row 17 (it asks for the first recorded video).

## Checklist before you publish

- [ ] Title: one of the 3 in `meta.json`, under 60 characters, no `$300k/mo`.
- [ ] Thumbnail: from the board's `<slug>.thumbs.html` (3 options, 1280x720, face slot).
      Doc 11 thumbnails exist only in `a-keynote/11-claude-code-content-system.thumbs.html`.
- [ ] Description CTA: "Agency Booked Calls" and the link. `[NEEDS: booking link]`.
- [ ] No client name, no agency name, no partner name on screen or in the description ("the agency I run").
- [ ] No number that is not in `brand/claims.md`. No red `[NEEDS]` tag visible in the cut.
- [ ] Mauro watches the final cut once before publish.
