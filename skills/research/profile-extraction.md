# Profile extraction: raw capture of an account's last 35 days

Step 1 of the four-step profile study. Produces the raw material only. No analysis happens here.

**The four steps** (set by Mauro on the Juan loom, 2026-09-15):

1. **Copy and extract** every piece of content plus its numbers. This file.
2. **Understand success and outliers.** Why it works and which 20% carries it.
3. **Break down, deeply.** Not "his article looks like this". Why does this account pop at all.
4. **Templatize the vehicles** for our own accounts and for clients.

Steps 2 to 4 are a separate skill and do not exist yet.

**Why the study is itself content.** A breakdown of a big account borrows its authority. Two
forms work: the name ("I broke down @handle's system") and the number ("I broke down 40
articles"). The study serves us, our clients and the community at the same time.

---

## The prompt

Run with the profile open in one tab and an empty Google Doc in another.

```
You are doing raw extraction. No analysis, no summarising, no opinions.

Source: the profile open in this tab.
Target: the empty Google Doc open in the other tab.
Scope: every post, thread, article and quote tweet published in the last 35 days.

Before you start: scroll the profile to the bottom of the date range and let everything
load. Content loads lazily, so an item you did not scroll past does not exist to you. Do
the same inside any thread or article you open. If you cannot reach 35 days back, say how
far you got and stop rather than filling the gap.

For each item, write one block into the doc:

---
DATE        YYYY-MM-DD
TYPE        post | thread | article | quote tweet | repost with comment
URL         the permalink
IMPRESSIONS
LIKES
REPLIES
REPOSTS
BOOKMARKS
MEDIA       none | image | video | carousel | link card
MEDIA NOTE  see the media rule below
TEXT
<the full text, verbatim, line breaks preserved>
---

Rules, all hard:

1. Verbatim. Copy the text exactly as written. Do not fix typos, do not tidy grammar, do
   not shorten. Line breaks are part of the content.
2. Threads are one block. Number the parts 1/, 2/, 3/ inside TEXT. Never split a thread.
3. Articles get the full body. Open it, scroll to the end, copy all of it including the
   headers. Title on its own first line.
4. A missing number is MISSING. Never estimate, never round, never infer one number from
   another.
5. No commentary. Do not write what a post is about or why it worked.

The media rule:

Try to copy the image into the doc first. If it copies, paste it under MEDIA NOTE.

If it does not copy, write a plain factual description: what is on screen, any text in the
image transcribed exactly, and the format. Describe what is there, not what it means.

For video: duration, first frame, and any on-screen text in the first three seconds.

Outliers:

After every item is in, add a section at the top called POSSIBLE OUTLIERS. Work out the
median impressions across everything extracted. List, as links only, every item at or above
3x that median, plus the bottom three. Write the median and the item count next to the
heading. Nothing about why anything is on the list.

Finish with:

EXTRACTED   <count> items
RANGE       <earliest date> to <latest date>
MEDIAN      <impressions>
NOT REACHED <anything you could not load or open, with the reason>
```

---

## Known limits of this pass

- **X truncates timeline previews at "Show more".** Clicking each one is possible but slow. The
  capture is an opening excerpt unless the item was opened.
- **Articles do not reliably appear in the Articles tab.** The in-range article on the first run
  was found on the Posts timeline and was absent from the tab.
- **Self-quote chains are not threads.** An account that chains self-quotes produces no native
  threads, and the extraction will correctly report zero.
- **Character limits bite on paste.** A full month of a prolific account will not paste into one
  chat window. Extract to the doc, then read the doc in pieces.
- **Image copy usually fails.** The description fallback is what actually delivers.

## Output convention

`research/profile-studies/<handle>-<YYYY-MM-DD>-raw.md` for the capture, and
`-analysis.md` beside it for steps 2 to 4. The raw file is never edited after it lands.
