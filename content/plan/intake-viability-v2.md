# Intake sheet viability, test 2: two strangers and a price

Built 2026-10-08 for decision #28 ("test again as another 2 strangers, treat as different
personas, then tell me how much someone would pay for that"). Tool under test:
`content/lead-magnets/outlier-to-template-intake/index.html`. Test 1 is the LI1 viability card
(`review-queue/data-archive/2026-10-08-v3/gc-v3.json`) and commit 15dc841.

Script: `content/plan/intake-viability-v2/run.py` (Playwright, headless Chromium, a fresh browser
context per persona, so no saved data and no "Load my worked example"). Screenshots and the page
state after every step: `intake-viability-v2/before/` (the page at 15dc841) and
`intake-viability-v2/after/` (the page after the fix commit 03f73d8). Contact sheet:
`intake-viability-v2/contact.png`.

---

## Verdict

**The sheet works as a free magnet for both strangers after today's fixes. Nobody pays for it as
it stands.** Before the fixes, both strangers got a wrong or empty result from the first paste.
After the fixes, both reach a correct outlier and a ready prompt, but only after they lower the
floor by hand, and the page never tells them they can. The paid version is the part that is not
on the page: a template store, a rewrite step and an SOP a VA can run.

- Persona A (agency owner, LinkedIn, VA): $0 for the sheet. $49 to $99 for a VA kit. $150 to $300
  for the full system with a starter template library. Estimate, reasoning below.
- Persona B (B2B consultant, X, ChatGPT): $0 for the sheet. $27 to $49 for a one-time kit. Not a
  $100+ buyer unless the kit writes his posts.

---

## The personas

Both are test personas built from `brand/audience.md` and the wider ICP. They are not real people.

**A. Agency owner, LinkedIn.** Runs a paid social agency at about $150K a month, 12 staff,
referral pipeline (audience.md segment 1, "burned-out-on-outreach operator"). Posts on LinkedIn
twice a week. A VA copies and schedules the posts. He uses ChatGPT in the browser, no Claude Code,
no terminal. Goal: find which posts of a peer agency owner pull comments, so his VA can copy the
shape. Second goal: score his own posts from the LinkedIn export the VA already downloads.
What he pastes:
1. 12 rows of a peer's posts, typed by the VA into a Google Sheet the way LinkedIn shows them:
   relative dates ("2w", "1mo"), first words, the post URL, and the count as LinkedIn prints it
   ("27 comments", "1,204 comments", one dash cell where the VA could not see the count).
2. His own LinkedIn export, TOP POSTS sheet, header row included. The layout is copied from a real
   export (`growthub-os/research/x-analytics-exports/linkedin-lorenzo-2026-09-22-to-2026-10-05.xlsx`):
   `Post URL, Post Publish Date, Engagements, (blank), Post URL, Post Publish Date, Impressions`,
   two tables side by side in one row.
   All LinkedIn values in this test are `[fixture]` numbers. They test the parser and describe no
   real account.

**B. B2B consultant, X.** Solo consultant, about 8K followers on X, sells a $5K to $10K advisory
project (audience.md segment 3, "wants-authority believer"). Writes with ChatGPT, never opened a
terminal. Goal: score a peer he follows and turn its best posts into his own shapes. The peer in
the test is @maurojpelle, with real numbers from `research/x-analytics/maurojpelle-2026-07-08-to-2026-10-05.csv`
(the first 15 original posts in the file).
What he pastes:
1. 15 rows from a Google Sheet, views the way X shows them: "463", "1.1K", one "2,316 Views"
   copied from the post page, one blank cell where an article card shows no views.
2. The same 15 posts as raw rows of an X analytics CSV, header included
   (`Post id,Date,Post text,Post Link,Impressions,...,Permalink Clicks`).
3. The same sheet at 390px phone width.

---

## Run log

Truth for persona B: the 15 posts have 47, 463, 2,316, 137, 245, 137, 217, 44, 610, 155, 113,
124, 287, 1,125 and 158 impressions. The real outlier is the 2,316 post (about 15x the median).

### Before the fix (page at 15dc841)

| Step | What the page did | Shot |
|---|---|---|
| A1 peer paste | Read every "27 comments" as no number. Posts scored: 0. Verdict: "Fill in at least 5 posts". No message about why. | `before/A-02-feed-paste.png` |
| A2 own export | The header became row 1. The URL went into Date, the date into First words, Engagements into Link. Scored on impressions under a "linkedin · comments" label with a 300 floor. | `before/A-05-own-export.png` |
| B1 feed paste | "2,316 Views" read as no number, so the best post dropped out silently. The blank cell moved the post link into the Number column. "463" showed "3.0x" with the label "normal". | `before/B-01-feed-paste.png` |
| B2 CSV paste | Scored the last column (Permalink Clicks): 15 posts, median 0, verdict "No outliers. Every post sits inside this account's normal range". Every number on the page was wrong. | `before/B-02-export-paste.png` |

Both strangers would have closed the tab at their first paste. Console errors: 0.

### Fixes (commit 03f73d8, `index.html` only)

1. A number with a word after it ("27 comments", "2,316 Views") reads as the number.
2. A header row from an X or LinkedIn export is read by column name: the impressions or comments
   column, with the date and link next to it. If the export has no comments column (LinkedIn),
   the sheet reads impressions and says so under the verdict.
3. Blank cells stay blank, so a missing number no longer shifts the link.
4. The link is the last URL in the row, so a post whose text is a t.co link keeps the right link.
5. A note under the verdict lists the rows left out of the median and why.
6. The ratio shows rounded down (2.95 shows 2.9x, not 3.0x "normal").
7. The paste hint says to copy the header row with export rows.

### After the fix

| Step | Result | Shot |
|---|---|---|
| A1 peer paste, floor 300 | 11 scored, median 22, line 66. 1 capture: "Comment PLAYBOOK and I'll send it", 1,204 comments, STRONG 54.7x. The 140-comment post (6.3x) is "under floor". Note: "Row 8: the number is not readable". | `after/A-02-feed-paste.png` |
| A2 own export | 7 posts, median 2,950, 1 outlier (12,400, 4.2x). Note: "This export has no comments column, so the sheet reads impressions. Set the floor in the same unit." First words stay empty: the export has no post text. | `after/A-05-own-export.png` |
| A3 floor 50 | 2 captures: the 140-comment post (6.3x) and the comment-bait post. Prompt lists both. | `after/A-06-floor-50.png`, `A-08-prompt-floor-50.png` |
| A4 steps 4 and 5 | A form and a route table that point to "your comment-for-access process", "your long-form post process". | `after/A-09-steps-4-5.png` |
| B1 feed paste, floor 50,000 | 14 scored, median 157. "No template here. 3 posts beat this account's median by 3x or more, but under the floor of 50,000 impressions." | `after/B-01-feed-paste.png` |
| B2 CSV paste | 15 scored, median 158, the 2,316 post at 14.7x. Same floor verdict. | `after/B-02-export-paste.png` |
| B3 floor 1,000 | 2 captures: the 2,316 post (STRONG 14.7x) and the 1.1K post (OUTLIER 7.0x). 610 (3.8x) is under the floor. | `after/B-03-floor-1000.png`, `B-04-capture.png` |
| B4 prompt | Ready to paste. Nothing in it needs Claude: it runs in ChatGPT with the screenshots attached. | `after/B-05-prompt.png` |
| B5 phone 390px | Date, First words and Link columns are 2 characters wide. Ratio column is cut off. | `after/B-06-phone.png` |

Console errors after the fix: 0.

### Moment of value

- **A:** the floor-50 run. The peer's "$40k retainer" post at 6.3x his own median, with a checklist
  and a prompt, is the thing his VA could act on this week.
- **B:** the floor-1,000 run. The peer's best post is at 14.7x with its link, and the prompt is
  one click.

In both runs the value arrives only after the stranger lowers the floor. The page does not say the
floor field can change.

---

## Product gaps (not fixed, each one is a call for Mauro)

1. **The floor wall.** At the default floors, A keeps only the comment-bait post and B keeps
   nothing. Test 1 flagged the same thing. Options: a floor that scales with the account (for
   example a share of follower count), a line next to the field that says it can change, or no
   floor for the free version.
2. **LinkedIn comments reward comment-gating.** "Comment PLAYBOOK" ranks first at 54.7x. The sheet
   turns a comment-for-DM post into the top template, which goes against the no-autodm rule in the
   8 Oct rules. A flag for gated posts, or reactions as the LinkedIn metric, would fix the ranking.
3. **LinkedIn export has no comments and no post text.** A's own data scores on impressions and
   the capture shows no first words. The 300-comment floor means nothing next to 12,400 impressions.
4. **Phone width.** Unreadable at 390px. Open since test 1.
5. **X CSV rows without the header** still score the last column. The hint now asks for the
   header. A full fix needs the sheet to know the X export column count.
6. **The prompt stops at the shape.** Step 3 says "Do not rewrite the post for me yet". Both
   personas want a draft of their own post. This is the step they would pay for.
7. **Steps 4 and 5 have nothing behind them.** "Check your store" and "your long-form process"
   assume a system the stranger does not have. The route table still lists a comment-for-access
   process.
8. **One browser only.** A's VA fills the sheet and A reads it on another machine. The data does not
   travel.
9. **Prompt wording names Claude.** It works in ChatGPT. B reads "Paste it into Claude" and may
   think he needs a Claude account.

---

## What comparable products sell for

All prices fetched or searched on 2026-10-08.

| Product | What it is | Price | Source |
|---|---|---|---|
| 1of10 | YouTube outlier finder. Same ratio as the sheet: views divided by the channel's typical views | Free tier; Basic $29/mo; Pro $69/mo | [1of10.com/blog/1of10-review](https://1of10.com/blog/1of10-review/) |
| Tweet Hunter | X scheduler with a 12M viral tweet library | $29 / $49 / $199 per month | [tweethunter.io/pricing](https://tweethunter.io/pricing) |
| Taplio | LinkedIn tool with a 5M+ viral post library | $39 / $69 / $199 per month | [taplio.com/pricing](https://taplio.com/pricing) |
| SuperX | X Chrome extension, analytics in the feed, 10M+ viral posts library on Advanced | $49 / $49 (launch, normally $99) / $199 per month | [superx.so/pricing](https://superx.so/pricing) |
| LinkedIn Swipe Files (Ross Simmonds) | 200+ viral LinkedIn posts, updated monthly | $10 (listed as "$10 a month") | [ross.gumroad.com/l/linkedin-swipe](https://ross.gumroad.com/l/linkedin-swipe) |
| LinkedIn Content Creation Swipe File (Gaurav Mehta) | Swipe file of viral LinkedIn posts | $12+ | [officialmehtag.gumroad.com/l/swipefile](https://officialmehtag.gumroad.com/l/swipefile/) |
| 700+ Twitter Swipe File (iNotion) | 700+ tweets to rewrite in your niche | $0 | [inotion.gumroad.com/l/twitter-swipe-file](https://inotion.gumroad.com/l/twitter-swipe-file) |
| linkedin-skills (GitHub, MIT, 4.3k stars) | 12 Claude Code skills, one extracts the hook formula of any LinkedIn post | Free | [github.com/sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) |
| Personal Branding Academy (Whop) | Course with brand audit templates and content frameworks | $12/mo | [whop.com/agi-hub/personal-branding-academy](https://whop.com/agi-hub/personal-branding-academy/) |
| Notion LinkedIn Content Management System | Official Notion template | Free | [notion.com/templates/linkedin-content-management-system](https://www.notion.com/templates/linkedin-content-management-system) |
| LinkedIn ghostwriting | Done for you posts | "$500/mo to several thousand"; Column charges $2,000/mo for about 15 pieces | [columncontent.com/linkedin-ghostwriter-pricing](https://columncontent.com/linkedin-ghostwriter-pricing/) |

What the table says: a list of viral posts sells for $0 to $12. The outlier ratio itself is free on
YouTube (1of10 free tier). Money starts at about $29 a month, where the tool does the collecting
for you. Above that sits done-for-you writing at $500 a month and up. The sheet today is a manual
version of the $0 to $29 band.

---

## Price per persona (estimate, from the table and the run log)

| Version | What it needs to have | A: agency owner, LinkedIn, VA | B: consultant, X, ChatGPT |
|---|---|---|---|
| The sheet as it is | Today's page after the fix | $0. Taplio at $39/mo already sells him a viral post library. | $0. Tweet Hunter at $29/mo gives him more posts with less work. |
| Free magnet | Floor line or scaled floor, gated-post flag, phone layout | Takes it, gives an email. | Takes it, gives an email. |
| $27 to $49 kit | Starter store as a Google Sheet or Notion page, prompt that writes a draft in his voice, ChatGPT Project instructions, a VA SOP (Loom + checklist) | $49 only with the VA SOP, because he never fills the sheet himself. | $27 to $49, his band: one payment, under one month of Tweet Hunter, and he keeps it. |
| $100+ system | A starter library of templates for his ICP, the weekly keep/retire loop with his own numbers, a reactions or impressions metric for LinkedIn, data that his VA and he both see, a review of his first batch | $150 to $300. He pays $500+ a month for writing help (ghostwriting band), so a system his VA runs is cheap next to that. The first-batch review is what makes it worth it. | Not a buyer at $100+ unless it writes the posts, which moves it toward the $29 to $49 a month tools he already knows. |

Reasoning in one line per persona:

- **A pays for time his VA saves and for a library he does not have to build.** He does not pay for
  a calculator. The $150 to $300 band needs gaps 1, 2, 3, 6, 7 and 8 closed.
- **B pays once, at the price of a template, for the rewrite step.** Gap 6 is the whole price
  for him. Gaps 1 and 9 decide whether he gets to the value at all.

Input for `content/plan/whop-product-v1.md`: the `[NEEDS: price]` there stays open. The data above
supports a $27 to $49 kit for the B buyer and a $150 to $300 system for the A buyer, with the
sheet itself free.
