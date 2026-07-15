# Session: Juan onboarding call (Juan x Mauro)

**Date:** 2026-07-15
**Duration:** ~51 min (call)
**Who was involved:** Mauro Pellegrino + Juan Cruz Lago
**Source:** Gemini transcript of the 2026-07-15 11:59 CEST call. Most of the call was personal (World Cup, gaming, catching up); the work-relevant content is extracted below.

---

## What this call was

Mauro onboarding Juan into the mauro-os system. Juan is coming on to help run Mauro's personal brand (@maurojpelle) content engine. The call walked Juan through the setup and set the near-term focus.

Juan's availability: at least July and August for sure, likely continuing even if a separate job (a BIM / AutoCAD office role he interviews for Monday) comes through. He'll give Mauro a hand around that.

This call is the source of everything done in the first Claude Code session: the session-end push rule, "do you have access to Mauro OS", and the short-form skill correction all came from Mauro's instructions here.

---

## Setup decisions (done on the call)

1. **Move from Claude web chat to Claude Code** (desktop app). Reason: faster, self-improving, and it carries memory of both Mauro's and Juan's work. Slower to set up the first time, cheaper/faster after.
2. **Cloned the `mauro-os` repo** to Juan's machine. Juan added as a **collaborator** on GitHub (`mauro-pellegrino/mauro-os`) so Mauro can see his files and they share the same skills.
3. **Model: Opus**, not Sonnet 5 (switch bottom-right).
4. **Permission mode: auto / "send everything"** (bottom-left) so Juan can fire instructions without approving each step.
5. **No need for separate Claude projects** now that it's Claude Code, everything runs from one chat against the repo.
6. **HTML infographics are built in the Claude web app, not Claude Code** (harder in Code). Images/HTML work lives in a project or the home dir; everything else runs from Claude Code.

---

## Short-form status

- Mauro **already corrected the tweets** in the shared doc (his rewrites of the AI batches).
- Juan pasted the corrected batches and asked Claude to "correct or build Mauro's short-form skill."
- Mauro kept the ones he liked and dropped the rest ("left five, the others I didn't like").
- The session-end **push rule** was created as **shared** (in `.claude/settings.json`) because both want the auto-push behavior.
- On scope, Mauro's call: **repo-wide** for the cobbler's-children pillar cut, and **skill + voice.md note** for his personal edge (see the strategy note below).

---

## Strategy / voice note (Mauro's principle)

Mauro prefers to **invest heavily in `voice.md` and get it really right**, because then any skill can just be told "look at the voice" and it starts from his real voice. The `voice.md` is how Mauro talks *everywhere* (tweets, YouTube, infographics), not just short-form, so genuine voice signals belong there, not buried in one skill.

He also flagged the cobbler's-children framing as wrong for his ICP ("makes no sense for service based businesses that are qualified").

---

## Next steps

### Focus for the coming days: YouTube + HTML (Mauro's stated #1 priority)

This is the pipeline Mauro wants built next, and he said it on the call specifically so it lands in the transcript:

1. **Build a list of ~10 YouTube competitors** (e.g., Marcos Ruiz, among others Mauro sent). Ask Claude in-chat to generate it.
2. From that list + their best videos, **generate 10 video ideas**.
3. From the 10 ideas, **generate questions for Mauro to answer by audio**.
4. Juan builds an **HTML per video** for Mauro to read off-screen while recording. These HTMLs are **longer** than the content ones (Mauro talks for ~15 min per video). Leave some whitespace, keep it easy to read, not too heavy.
5. Use the existing **YouTube skills** (titles, etc.) throughout.
6. Once a 15-min video exists, its transcript feeds the tweet engine, so short-form quality jumps too.

### Tweets / short-form
- There's a **backlog ready to schedule** (enough for several days).
- **Tomorrow's task:** decide the **scheduling software** for tweets (repo skills assume TweetHunter) and start pushing them out.

### Engagement / comments
- Decide **who to comment on**. Mauro has a Twitter list; can build a separate tab/list of specific accounts to watch, plus comment in For You.
- Ongoing, both comment.

### Housekeeping
- **Save this call transcript** to the repo (this recap).
- Juan to prep tomorrow's questions / HTMLs; discuss over Slack / voice notes.

---

## Context worth remembering

- Mauro **hasn't posted since June** (personal reasons). This is a long-game rebuild.
- The brand is ultimately Juan-assisted growth for Mauro's own account, on top of the agency he runs. Framed as building Mauro's independence/authority over time.
- Language: Juan can prompt Claude in Spanish; that's fine.

---

## What Claude already shipped this session (git-tracked)

- Added the **`SessionEnd` auto commit+push hook** to `.claude/settings.json` (shared).
- Baked Mauro's short-form edit pass into `skills/content/short-form/` (personal-edge voice rule, real before→after anchors, gold examples).
- Added the **"Personal edge"** section to `brand/voice.md` (mild profanity, personal specificity, action closers, factual precision, non-native-speaker angle).
- **Cut the cobbler's-children pillar** repo-wide (positioning, CLAUDE.md, audience, and the skills that referenced it as an active pillar).
