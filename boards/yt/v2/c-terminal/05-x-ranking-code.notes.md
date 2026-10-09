# I read X's ranking code: presenter notes (format C, terminal)

Source: `research/video-knowledge/05-x-ranking-code.md`. Numbers: `brand/claims.md` only. Board: `05-*.html` in this folder.
Frames: 22. Planned length: about 21 minutes. Press N on the board to see these notes on screen.

## Today we go over

01  The folklore: where the numbers you were quoted come from
02  The weights: every default in param.rs, read line by line
03  What to write for, and what costs you

Each section: one worked example, one before and after.

## Rules for this video
- Every weight is a default. Say so whenever a value is on screen.
- No deltas (tap 0.4 to 0.3 and the rest), no decay percentages, no pre-30-Sep cold start limits: claims.md marks them unverified.
- The 2023 numbers always carry 2023 in the same line.
- The param.rs pane is a defaults view from claims.md. Swap in a live capture of the file on the day.

## 01 · 0:00-0:10 · hook
**Caption:** I read X's ranking code. Every weight.
**On-screen NEEDS:** live capture of param.rs on the day

ON SCREEN: the defaults from param.rs, copy link highlighted.

SAY: These are the ranking weights X uses for the For You feed. Every default, read from the file on 1 October. Share via copy link is the highest positive in the file, at 20. A like is 0.5.

## 02 · 0:10-0:20 · hook
**Caption:** Every number you were quoted: 2023

ON SCREEN: grep pulls the three folklore numbers out of my own thread.

SAY: And these are the numbers everyone quotes. Reply equals 13.5 likes. Repost is 20x. One reply beats 150 likes. All three are from 2023, from a system X replaced.

## 03 · 0:20-0:30 · hook
**Caption:** Folklore. The weights. What to write for.

ON SCREEN: the agenda in this video's notes file.

SAY: Today we go over three things. Where the folklore comes from. The real weights, line by line. And what that means for what you write, including the four actions that cost you.

## 04 · 0:30-1:40 · 01 folklore
**Caption:** Two repos. Three years apart.

ON SCREEN: the timeline of releases.

SAY: 2023, Twitter open-sourced the-algorithm, and that release shipped explicit weights. That's where 13.5 and 20x come from. January 2026, xAI published a new system, x-algorithm. The formula and the scored actions, and no values. Then on 13 and 14 August, a params file landed with every default. I read it line by line on 1 October.

## 05 · 1:40-2:50 · 01 folklore
**Caption:** A weighted sum of predicted actions

ON SCREEN: the scorer. The weights are named constants pulled from the params module.

SAY: The score is a weighted sum. For each action, the model predicts the chance this viewer does it, and multiplies it by a weight. Then it adds them up. The weights come from one place, the params module.

## 06 · 2:50-3:50 · 01 folklore
**Caption:** Likes are one scored action of many

ON SCREEN: the scored actions, positive then negative.

SAY: Here's what gets scored. Like is in there. So are profile click, follow author, share via DM, share via copy link, dwell time, quoted click. And four negatives at the bottom. A post that earns a profile visit and a follow works more of the scorer than one that earns a like.

## 07 · 3:50-5:00 · 01 folklore
**Caption:** January: no file. August: param.rs.

ON SCREEN: worked example. The same ls, before and after August.

SAY: Before. On 4 August I searched the whole tree for the params module the scorer imports. It wasn't there, 404 on every path. After. On 13 and 14 August, home-mixer/params/param.rs was added. Same command, now it returns the file.

## 08 · 5:00-6:20 · 01 folklore
**Caption:** My own thread is now out of date

ON SCREEN: post 2 of my own thread from 4 September.

SAY: And I have to correct myself. On 4 September I posted that the code gives you zero of the weight values. That was true of the January release. It's out of date now, and if you check, you'll find that. So I'm saying it first.

## 09 · 6:20-7:30 · 02 weights
**Caption:** Every default, read 1 October 2026
**On-screen NEEDS:** live capture of param.rs on the day

ON SCREEN: the full defaults list.

SAY: Here's the whole block. Positive actions at the top, the boost, then the four negatives. Every one of these is a default. X can override any of them per experiment or per user without a release. Keep that in your head for the rest of the video.

## 10 · 7:30-8:40 · 02 weights
**Caption:** Copy link tops the file at 20

ON SCREEN: the ten positive weights as bars.

SAY: Top to bottom. Share via copy link, 20. Reply and quote, 5. Retweet, 1. Like, 0.5. Time after the tap, 0.4. The tap, 0.3. Open link, 0.2. Video open, 0.07. And video quality view sits at zero.

## 11 · 8:40-9:50 · 02 weights
**Caption:** A like: 0.5. A copy link: 20.

ON SCREEN: worked example, three weights side by side.

SAY: Worked example. A like is 0.5. A copy-link share is 20. And a reply from someone you follow back gets a boost of 15. The file doesn't say whether that boost adds to the 5 or multiplies it, so I won't pick one.

## 12 · 9:50-11:00 · 02 weights
**Caption:** Weights multiply predicted probabilities

ON SCREEN: the line in my claims file that records the file's own warning.

SAY: Before you start doing maths. These weights multiply predicted probabilities. The file says so in a comment, and it names the misreading: one report cancels 468 likes. That's wrong. A report sits at minus 234 because a report is rare.

## 13 · 11:00-12:10 · 02 weights
**Caption:** Time after the tap beats the tap

ON SCREEN: the four dwell params.

SAY: Four separate dwell params, and people collapse them. Time after a tap, 0.4. The tap itself, 0.3. Dwell with no tap, 0.05. The continuous dwell time, 0.004. So the time someone spends after they open your post is worth more than the open.

## 14 · 12:10-13:10 · 02 weights
**Caption:** Before: one dwell. After: four params.

ON SCREEN: my September list on the left, the four params on the right.

SAY: Before. In September I listed dwell time as one thing to aim for. After reading param.rs, it's four params with very different values. Quote 0.05 as time after the tap and the advice flips. Write the body for the 0.4.

## 15 · 13:10-14:20 · 03 write for
**Caption:** Four actions get subtracted

ON SCREEN: the four negatives, drawn on absolute value.

SAY: What costs you. Report, minus 234. Mute author, minus 58.8. Not interested, minus 47.52. Block author, minus 31.2. Same rule as before: these scale probabilities. Ragebait that provokes mutes and blocks lowers the score mechanically.

## 16 · 14:20-15:20 · 03 write for
**Caption:** Five posts don't buy five slots

ON SCREEN: the shape of the author diversity decay. Shape only, no values.

SAY: Posting more doesn't stack. A diversity function decays your own posts against each other inside one feed response. It sorts by score, so your best post keeps its value and the weaker ones absorb the decay. You're never zeroed, you're just competing with yourself.

## 17 · 15:20-16:20 · 03 write for
**Caption:** Under 50,000 followers: a test window

ON SCREEN: the four cold start values.

SAY: Cold start. Accounts under 50,000 followers. Posts under 200 impressions and under two hours old get tested in feed slots 15 to 16. Same caveat: defaults, and X can change them without a release.

## 18 · 16:20-17:30 · 03 write for
**Caption:** No 9am lever. No hashtag lever.

ON SCREEN: the README sentence.

SAY: The most useful line in the repo is a sentence. They eliminated every hand-engineered feature, and the model reads the viewer's own engagement history. So no post-at-9am lever, no hashtag lever, no reply-to-yourself lever. And there's no link filter in the published code. Nothing resurfaces, old posts get removed.

## 19 · 17:30-18:40 · 03 write for
**Caption:** Replies earned 10x the profile visits

ON SCREEN: worked example on my own account, one week.

SAY: My own account, 9 to 15 September. 173 replies did 22.5 profile visits per 1,000 impressions. Four bare article links did 2.2. A profile click is a scored action, and replies are where I earn them. One week, one account, so it's a read, not a trend.

## 20 · 18:40-19:40 · 03 write for
**Caption:** Before: the hacks. After: the actions.

ON SCREEN: the before and after for what you write.

SAY: Before. Post at 9am, add hashtags, avoid links, post more. None of those exist in the code. After. Write for the actions that are scored: the profile click into a follow, the share by DM or copy link, and the time after the tap.

## 21 · 19:40-20:30 · 03 write for
**Caption:** Check any claim against the file
**On-screen NEEDS:** live capture of this run on the day

ON SCREEN: the check, run live.

SAY: Here's how you check any algorithm claim yourself. Open the repo, ask Claude to find the param and quote the line, read the value, and check the date. If a post quotes a number and the file has a different one, the file wins.

## 22 · 20:30-21:15 · cta
**Caption:** Link in the description: Agency Booked Calls

ON SCREEN: the CTA.

SAY: The formula is public and so are the defaults. Write for the time after the tap and for the share. If you run an established agency and you want a content system built on this for your own inbound, the link is in the description. It's called Agency Booked Calls.
