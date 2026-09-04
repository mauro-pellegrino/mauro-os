# X Source Code Myth-Buster Thread

**Source:** Mauro (@maurojpelle), raw X posts typed straight into the box
**Captured:** 2026-09-04 (pasted by Mauro in chat)
**Speaker:** Mauro
**Use:** canonical voice reference for the source-check myth-buster tweet type. Push future tweet creation from this. See the matching rule in `brand/voice.md` (Raw tweet types, Type 4).

Angle: he read the open-source X "For You" ranking code (asked Claude to check it), and each post debunks one repeated algorithm myth against what the file actually contains. Authority comes from the source, not from him. Intellectual honesty is the spine: he refuses to overclaim even when a debunk would let him.

---

## The posts (verbatim)

**1.**
Stop blaming the x algorithm
The for you code is open source. I asked Claude to check it:

* "reply = 13.5 likes" is a 2023 number
* "repost = 20x" is a 2023 number
* "one reply beats 150 likes" is a 2023 number

that system got replaced.

**2.**
What the x code actually gives you:

* the exact formula, a weighted sum of predicted actions
* the full list of what's scored
* zero of the weight values

**3.**
A like isn't what you're looking for
Focus on generating all engagement:

* profile click
* follow author
* share via dm
* share via copy link
* dwell time
* quoted click

A post that gets a profile visit and a follow is working more of the scorer than one that gets a like.

**4.**
The single most useful line in the whole x repo isn't a number, it's a sentence.
They say they eliminated every hand-engineered feature and let the model read the viewer's own engagement history.

* no post-at-9am lever
* no hashtag lever
* no reply-to-yourself lever

the levers were deleted on purpose. hacks are dead by design.

**5.**
posting more does not stack on x.
there's a diversity function that decays your own posts against each other inside one feed response:

* it sorts by score, not time
* your best post keeps its value
* your weaker posts absorb the decay
* you're never zeroed, just worth less each time

five posts don't buy five slots in one person's feed.

**6.**
the "links get suppressed 80% on x" thing:

* there is no link filter in the published code
* nothing in the scorer touches external links at all

that doesn't prove links are boosted. it proves the suppression claim has nothing behind it. i believed links were fine from my own numbers, now there's no mechanism punishing them either.

**7.**
ragebait isn't free reach on x.
four actions are scored negative and subtracted:

* not interested
* block author
* mute author
* report

bait that provokes mutes and blocks lowers your score mechanically. the engagement it wins can cost more than it makes.

**8.**
two x myths that die the second you open the code:

* "first 30 minutes is the point of no return", there's no time-window mechanic, just a hard age cutoff
* "bookmarks are a top-3 signal", bookmark isn't one of the 19 scored actions at all

both get repeated weekly. neither is in the file.

**9.**
nothing resurfaces on x.

* age is a hard cutoff, not a slow decay
* old posts get removed
* if the age can't even be read, the post is dropped

there's no evergreen resurfacing in for you. repurposing means reposting a new angle, not praying an old banger revives.

**10.**
what i'm actually changing after reading the x source:

* optimize for profile-click into follow, both are scored, that's the growth path
* make content people forward, share via dm and copy link are scored actions
* stop treating volume as reach, the diversity decay throttles it

and i'll never quote a weight number again, because there aren't any to quote.
