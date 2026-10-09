---
description: Process the review-queue and morning-page files Mauro downloaded, then act on them
---

1. Run `python3 ~/inbox/run.py`. It files the downloads, logs the approval rates, ticks the BACKLOG day block and carries unticked tasks to the next morning page.
2. Read its summary. For each KILL / CHANGE line, apply it (Notion via the connector, files in the repo). For each note, answer or act.
3. Reply to Mauro in STE, about 10 lines: first-pass rate against the last round, what you changed, what still needs him.
