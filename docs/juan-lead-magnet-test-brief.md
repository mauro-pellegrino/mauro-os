# Juan: test the lead magnet system

**18 Aug 2026.** One job, and it produces four things we need.

We are packaging the lead magnet system as a $500 product. Before it can be sold, someone who is not Mauro has to build a magnet with it and prove the instructions are good enough to follow alone.

**That someone is you, and you working alone is the point.** Our buyer sets the system up himself. If you can build a magnet from the docs with Mauro out of the room, it's precise enough to sell. If you can't, we found the gap before a paying client did.

---

## What you have

Everything is already in the repo you have access to.

- **The rules:** `skills/lead-gen/lead-magnet/_master.md` plus one subtype file
- **Start with:** `skills/lead-gen/lead-magnet/prompt-swipe-file.md`. It's named in the system as the default first subtype to ship
- **The build prompt:** `skills/lead-gen/lead-magnet/notion-delivery-build.md`
- **The cleaned version:** `brand/lead-magnets/shareable/lead-magnet-system.md`

You'll need a Notion workspace to build into. Your own is fine.

---

## The rule while you work

**Do not ask Mauro how to do it.** When you get stuck, write down where you got stuck and make your best guess, then keep going.

Every place you had to guess is a hole in the product. The log of those holes is worth as much as the magnet you build.

---

## What to produce

**1. One finished magnet.** Any topic from the repo's source material. A Notion page with real nested subpages, a cover image, post copy and DM copy. Follow the system exactly, including the parts you disagree with.

**2. A gap log.** One line per moment you were unsure. Format:

```
[file, section] — what I couldn't tell — what I guessed
```

Example: `_master.md, In-asset prompt blocks — the page image prompt just says "..." so I don't know what to actually write — I wrote my own, pasted below`

**3. Every prompt you had to invent.** The system defines two prompt blocks (page image prompt, HTML style prompt) and every example ends in `...`. Whatever you write to fill those, keep it. That becomes page 3 of the product.

**4. A time log.** Roughly how long each stage took. The offer claims about 15 minutes plus a VA. We need to know if that's true.

---

## Known problems, so you don't waste time on them

These are already logged. Note them if you hit them, don't try to solve them.

- `{{calendly_url}}` is still an unfilled placeholder. Use anything, flag it.
- Brand colour is now set: `#4A392C`. Full palette in `brand/colors.md`.
- `notion-delivery-build.md` is hardcoded to exactly 5 subpages while the spec says 5-7. Pick one and say which.
- `case-study.md` and `industry-specific.md` are unusable. Don't try them.
- There is no landing page or email capture. The DM links straight to the Notion page for now.
- No production SOP exists. `_master.md` line 44 says so itself. Your run is effectively the first draft of one.

---

## Where it goes

- The magnet: your Notion, share the link
- The gap log, the prompts and the time log: a new file at `content/qa/lead-magnet-build-log.md`, committed on a fresh branch

**Branch and PR, please.** One branch for this batch, open the PR when it's done. The last batch sat unmerged for three weeks because it went on an old branch.

---

## Why this matters

Four of the six pages of the $500 product don't exist. Your run produces three of them: the worked example, the prompts, and the raw material for the Start Here page.

Full plan in `research/jk-molina/cashie-studio/offer/lead-magnet-system-500.md`.