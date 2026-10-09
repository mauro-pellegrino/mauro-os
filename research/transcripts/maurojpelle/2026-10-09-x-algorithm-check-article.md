# X article: checking the 30 Sep algorithm post against param.rs

**Source:** Mauro, handed over 2026-10-09, his own article text in full.
**Subject:** the viral 30 September post about x algorithm changes, checked line by line against
`home-mixer/params/param.rs` in `github.com/xai-org/x-algorithm`.
**Relationship to claims.md:** this is the article behind the "X ranking weights, read from param.rs on
2026-10-01" block. It carries four things that block were missing a source for: the absence of a 10 second
dwell threshold, the insult-label rule, the 30 September fresh-post-pool switch-on, and "it never drops to
zero" on the diversity decay. [NEEDS: confirm whether this is published. If it is, those four become public
rows citing this file. If it is still a draft, they stay unconfirmed.]

---

On 30 Sep a post went round about what changed in the x algorithm.
The tap weight going down, the time after the tap counting more, a fresh post pool that was still switched off.
The for you code is open source, so I asked Claude to check it against home-mixer/params/param.rs, the file where every weight lives.
It was mostly right. One claim isn't in the code at all, and one went out of date the same day.

How a post is scored, in one line

The score is a sum of weights, each multiplied by the model's predicted chance that someone does that action.
The weights multiply probabilities, not counts.
The file says so in a comment, and it names the misreading itself.
A report sits at -234 because a report is far rarer than a like, so the weight has to be big for the model to notice it at all. "One report cancels 468 likes" is wrong, and the code says as much.

What the post got right

Every one of these is in the file today:

* the tap on a post, ClickWeight, 0.3
* the time spent after the tap, ContClickDwellTimeWeight, 0.4
* not interested, -47.52
* posts labelled as insults hidden from people who don't follow you

The tap and the time after it are the two that matter for writing, because the time after the tap is worth more than the tap itself.
A hook that wins the click and then loses the reader scores lower than one that holds them, so the body has to be worth reading to the end.
One thing to be careful with.
There are four dwell parameters in that file and they're easy to mix up. DwellWeight is 0.05 and that's dwell with no tap.
ContDwellTimeWeight is 0.004. The 0.4 is specifically the time after a click. Quote the wrong one and the advice flips.

The claim that isn't in the code

The post said the time after a tap counts from 10 seconds.
There's no 10 second threshold anywhere in that file.
The model predicts the time as a value. I'd treat the 10 seconds as the author's reading, not as something x published.

The claim that went out of date in a day

The post said the fresh post pool was still switched off. The release on 30 Sep switched it on.
What it covers now:

* Accounts under 50,000 followers.
* Posts under 200 impressions.
* In their first 2 hours.
* Landing in feed slots 15 and 16.

So the first two hours of a post matter more than they did on Monday, and if your account is under 50k, answer every reply in that window.

The weights worth writing for

These didn't change this week and they're the ones I'd actually write for:

* Share via copy link, 20, the highest positive in the whole file.
* Reply and quote, 5 each.
* A reply from someone you follow back carries a boost of 15.
* Opening a link, 0.2, so the scorer doesn't punish links.
* A like, 0.5.
* Video quality view, 0.

The copy link weight is the one nobody talks about.
It's private and deliberate, somebody liked your post enough to send it to one person, and it's the single thing the ranker works hardest to predict.
On the follow-back boost, the file names it and doesn't say whether it adds to the 5 or multiplies it. I'm not going to pick one for you.

Posting more still doesn't stack

This one didn't change either and I'd still put it at the top of the list.
There's a diversity function that decays your own posts against each other inside one feed response.
Your best post keeps its full value, the weaker ones absorb the decay, and it never drops to zero.
It sorts by score and not by time, so the posts that absorb it are the ones you cared least about.
Five posts don't buy five slots in one person's feed, you're basically competing with yourself at some times.

Ragebait still costs you

Four actions are scored negative and subtracted from the post.
Not interested at -47.52, block author at -31.2, mute author at -58.8, and report at -234.
Bait that gets someone to tap not interested lowers your score mechanically, and that's the weight that moved this week.

What I'm changing

* Write the body for the time after the tap, the tap alone is worth less than holding them.
* Post when the audience is online and answer every reply in the first two hours.
* Make things people forward, copy link is the top of the file by a distance.
* Keep linking articles, there's no link penalty in there.
* Stop treating volume as reach.

On my own account

In September my bare link posts to articles got a median of 532 impressions against 156 for everything else on the account.
That's one small account over one month, so it proves nothing on its own.
The code has no link penalty and my numbers look like it, which is as far as I'd take it.

What this can't tell you

Every value in that file is a default.
X can override any of them per experiment or per user without a release.
A default is where the feed starts, never proof of what your feed is running today.
Re-check the file before you quote a number, they changed some of them this week.

Talk soon, Mauro.

---

## Note on the September number

"Median 532 impressions on bare link posts against 156 for everything else, September" is a different cut
from the row already in `claims.md`, which covers 2 to 15 September and reads "15 words or under n=4 median
529 impressions; 30-60 words n=17 median 143, all four posts in the short bucket are bare t.co links". The
two are close but not the same window or the same split. [NEEDS: the export behind the full-September cut
before 532 / 156 ships as a claims row.]
