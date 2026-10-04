---
name: template-intake
description: "Input 1 · Template intake. Turns any outlier post from a tracked profile (X or LinkedIn, any post type) into a saved template with its shape, its rules and the original with numbers. Triggers on \"template intake\", \"save this as a template\", \"score these posts\", \"is this an outlier\", or a batch of pasted posts with links and numbers."
---

# Input 1 · Template intake (any outlier post → a template)

Every post format the content engine runs starts as someone else's outlier. This skill is the intake: it finds the posts that beat their own account's normal, saves each one as a template, and routes it to the process that will run it.

Source: Mauro's process-map voice notes (`research/transcripts/maurojpelle/2026-10-01-process-maps-voice-notes.md`) and the outlier-article Loom (`research/transcripts/maurojpelle/2026-08-28-how-to-save-outlier-x-articles-loom.md`). In his words: "it was basically checking for outliers from a profile ... that's just a way to get templates created, both for lead magnets and for just normal posts as well."

## Where things live

| What | Path |
|---|---|
| Profiles to check | `research/tracked-profiles.csv` (platform, handle, name, why_tracked, source) |
| Raw intake rows (one file per session) | `content-log/intake/YYYY-MM-DD.csv` |
| The scorer | `tools/outlier-score.py` |
| The templates store | `research/post-templates.md`. Create it on the first save if it does not exist. |
| X articles (one post type with its own corpus) | `research/outlier-x-articles/`, method in `skills/research/article-corpus.md` |

**Templates live in a doc, never inside a skill.** A skill says how to run a process. The templates store holds the shapes the process can run. Keep them apart, so that a template can be added or retired without a skill edit.

## The outlier rule

Outlier = the post's number ÷ that account's median over its last 10-20 posts.

| Ratio | Verdict |
|---|---|
| 3x or more | OUTLIER |
| 10x or more | STRONG |

- **The number:** X = impressions. LinkedIn = comments. Use the number shown on the post.
- **Floor:** X 50,000 impressions, LinkedIn 300 comments. A post under the floor is not worth a template, whatever its ratio.
- **Minimum:** 5 or more posts from the account in the file, or there is no median to compare against.
- **Compare to that account, never to ours.** A 20K post is an outlier on a 4K account and a normal day on a 30K account.

## The steps

Who: **H** = the human (Mauro, or the operator in a client install). **C** = Claude.

| # | Step | Who | Output |
|---|---|---|---|
| 1 | Open a tracked profile | H | X or LinkedIn profile open |
| 2 | Spot the outliers | H + C | posts far above that account's normal |
| 3 | Capture + verify | H | text, screenshot, link, exact numbers sent to Claude |
| 4 | Read the post type | C | which shape it is |
| 5 | Score + check the floor | C | outlier score + floor result |
| 6 | Dedupe against the templates store | C | a new shape, or a new example of an old one |
| 7 | Save the template | C | shape + rules + original with numbers |
| 8 | Route to a process | C | template → the process that runs it |
| 9 | Pick the week's run | H | 3-5 templates queued |
| 10 | Reuse or retire (Monday) | C reports, H decides | template scoreboard |

### 1. Open a tracked profile

Start from `research/tracked-profiles.csv`, not from a random scroll. To find new accounts, run 5-10 keyword searches on X and browse Home for large accounts. A big follower count is a reason to look, never a reason to save. Every new account gets a row in the CSV, with a `source` that says where it came from.

Any post type counts: text post, long form, X article, lead magnet, quote tweet, video.

### 2. Spot the outliers

Write the newest 10-20 posts of the account into `content-log/intake/YYYY-MM-DD.csv`:

```
handle,platform,date,metric,link,first_words
```

`platform` is lowercase `x` or `linkedin`. Then run:

```
python3 tools/outlier-score.py content-log/intake/YYYY-MM-DD.csv
```

It prints the OUTLIER and STRONG rows first and writes `<file>-scored.csv` next to the input. Capture only those rows.

### 3. Capture + verify (about 2 minutes per post)

For each outlier, send Claude four things in one batch:

1. The post text, copied (not retyped).
2. A screenshot of the post, with its image. For an X article, shoot it from the feed so the frame carries the title, the cover and the opening lines. For an HTML infographic cover, right-click and copy the image so the detail survives.
3. The post link.
4. The numbers, checked exact on the post: impressions or views, comments, reposts. For a LinkedIn lead magnet, add a screenshot of one comment and the reply it got.

Batch the captures. Do not send them one at a time.

### 4. Read the post type

Name the shape: lead magnet (comment-for-access), long form, X article, quote tweet, video, short text post. The type decides which corpus the original also goes into. An X article also gets saved to `research/outlier-x-articles/` by the rules in `skills/research/article-corpus.md`.

### 5. Score + check the floor

Confirm the ratio and the floor from `tools/outlier-score.py`. If the human sent a post that the script marks `normal` or `under floor`, say so in one line and do not save it as a template. It can still go into a swipe file.

### 6. Dedupe against the templates store

Search `research/post-templates.md` for the same shape. Two results:

- **Same shape exists:** add this post as a new example under the existing template, with its numbers. Do not make a second template.
- **New shape:** go to step 7.

### 7. Save the template

One entry per shape in `research/post-templates.md`:

```
## T-NN · <template name, 2-5 words>
- Type: lead magnet | long form | X article | quote tweet | video | short post
- Shape: <the structure line by line: hook line, body moves, close, image or media>
- Rules: <what makes it work, each rule tied to a line of the original>
- Process: <the process that runs it, from step 8>
- Status: active | retired (YYYY-MM-DD, reason)
- Examples:
  - @handle · YYYY-MM-DD · <metric> (<ratio>x their median) · <link>
    <the original text, verbatim, plus the screenshot path>
```

Rules describe the original. Never add a rule the original does not show (`brand/voice.md`, no invented detail). Any field the capture does not fill gets `[NEEDS: x]`.

### 8. Route to a process

| Template type | Process | Skill |
|---|---|---|
| Lead magnet, comment-for-access | `lead-magnet-autodm` | `skills/lead-gen/lead-magnet/_master.md` |
| Long form | `long-form` | `skills/content/long-form/_master.md` |
| X article | `x-article` | `skills/content/article-origination.md`, then `skills/content/x-articles-POINTER.md` |
| Quote tweet | `quote-tweet` | `skills/content/x-reply-assistant.md` |
| Short text post | `short-form` | `skills/content/short-form/short-form-from-long-content.md` |

A lead magnet template needs a real resource behind it. Match an existing resource first. If there is no match, building a new one is the slowest branch, so flag it before the run starts.

### 9. Pick the week's run (human)

Pick 3-5 templates for the week. The rest wait in the store. Each post built from a template gets a row in `content-log/post-tags.csv` at the stage step (see `content-log/README.md`).

### 10. Reuse or retire (Monday)

The weekly review (`skills/ops/content-loop.md`) reads `content-log/post-tags.csv` to score each template:

- **Won** last week → run it again with a new subject.
- **Lost twice** → set `Status: retired` with the date and the reason. Keep the entry.

## Save first, build later

Do not build a skill from templates until about **50** captures are in. A rule drawn from five posts is a rule drawn from what you happened to like that week. During collection, the only job is: save, save, save.

## Use in a client install

The steps do not change. The client gets their own `research/tracked-profiles.csv` (accounts in their niche), their own templates store, and their own process list in step 8. Their voice and claims files replace `brand/`.

## Done when

- Every captured post has a scored row in an intake CSV, with the link and the exact numbers.
- Every OUTLIER or STRONG post over the floor is in `research/post-templates.md`, as a new template or as a new example.
- Every template has a process from step 8.
- No new account was checked without a row in `research/tracked-profiles.csv`.
