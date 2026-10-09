---
description: Monday loop for Ghosted Calls + life. Dump the week, then propose lane changes
---

1. Run `python3 private/system/week.py` (add `--this` only if Mauro asks for the week so far).
2. Run `python3 tools/x-keyword-tracker.py Mauro`. If it prints a WARNING, ask Mauro for a fresh X content export.
3. Read the file `week.py` prints, `private/system/ROADMAP.md` and `BACKLOG.md`.
4. Reply to Mauro in STE, about 10 lines:
   - Line 1: mauro-os minutes last week against the 450 target, and how many weekdays had a full 90-minute block.
   - What shipped in mauro-os (from the commits), in one line.
   - The one item in the Build lane that moves the offer closest to a sent message.
   - The lane changes you propose (move, freeze, park), each as one line.
   - Keywords: the winners to repeat next week, and the add/drop proposals from the tracker, in one line.
   - Remind him to write the 5-question diary in the notebook.
5. Write the proposed lane changes into the week file under "Lane changes proposed by Claude".
6. Change `ROADMAP.md` and `BACKLOG.md` only after Mauro approves. Never change them silently.
