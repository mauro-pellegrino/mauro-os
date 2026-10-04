# Content log

## post-tags.csv

`post-tags.csv` records which template (and which process) each post was built from. It exists so
the weekly review can score each template: which shapes won, which lost, which to run again and
which to retire (`skills/research/template-intake.md`, step 10). Without a row, the review has to
guess the template from the post's wording, and that guess is unreliable.

**Who adds a row:** Claude, in the stage step of every process, at the moment the post is handed
over for scheduling. One row per post per account. A card or a draft that is not staged gets no row.

| Column | What goes in it |
|---|---|
| date | the planned post date, YYYY-MM-DD |
| account | the account and platform, for example `Mauro X`, `Mauro LinkedIn` |
| match | 4-8 words from the post's first line, lowercase, or the post link once it is live |
| template | the template ID and name from `research/post-templates.md`, or empty if none |
| process | `x-article`, `long-form`, `lead-magnet-autodm`, `quote-tweet`, `short-form` |

The first data row is an example. Delete it when the first real row goes in.

A row whose `match` text is in no exported post never matches. Check the unmatched rows in the
Monday review.

**Status:** the review does not read this file yet. `skills/ops/content-analytics-review.py` scores
posts from the X export only. Until it reads `post-tags.csv` first, join the two by hand in the
Monday review (`skills/ops/content-loop.md`).

## intake/

Raw rows from template intake, one CSV per session (`intake/YYYY-MM-DD.csv`), scored with
`tools/outlier-score.py`.

## timing.csv

One row per ASCII article run, from brand pick to staged. Measured times only. Format in
`skills/content/ascii-article.md`.
