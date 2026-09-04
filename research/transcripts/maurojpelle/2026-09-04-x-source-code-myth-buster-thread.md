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
Posting more does not stack on x.
There's a diversity function that decays your own posts against each other inside one feed response:

* it sorts by score, not time
* your best post keeps its value
* your weaker posts absorb the decay
* you're never zeroed, just worth less each time

Five posts don't buy five slots in one person's feed.
You are basically competing with yourself at some times

**6.**
The "links get suppressed 80% on x" thing:

* there is no link filter in the published code
* nothing in the scorer touches external links at all

So just link away

**7.**
Ragebait isn't free reach on x.
Four actions are scored negative and subtracted:

* not interested
* block author
* mute author
* report

Bait that provokes mutes and blocks lowers your score mechanically.

**8.** (cut in the final edit)

**9.**
Nothing resurfaces on x.

* old posts get removed
* if the age can't even be read, the post is dropped

There's no evergreen resurfacing in for you.
You are better off just reposting your winners with different angles or QT tweeting

**10.**
What i'm actually changing after reading the x alg:

* optimize for profile-click into follow, both are scored, that's the growth path
* make content people forward, share via dm and copy link are scored actions
* stop treating volume as reach

---

## What changed in Mauro's final edit (2026-09-04)

The posts above are Mauro's finalized versions. His edits are the lesson, not the first draft:

- **He trims the second explanatory sentence off the closer.** #7 dropped "the engagement it wins can cost more than it makes." #10 dropped "and i'll never quote a weight number again". The mechanical statement lands and stops; he does not add the follow-on that spells out the takeaway.
- **He'll swap a careful hedge for a flat punch.** #6 replaced the whole "that doesn't prove links are boosted, it proves the suppression claim has nothing behind it" honesty beat with "So just link away." When a shorter, more direct closer exists, he takes it.
- **He'll add a plain-spoken aside instead.** #5 added "You are basically competing with yourself at some times." #9 swapped the "praying an old banger revives" line for "You are better off just reposting your winners with different angles or QT tweeting" — a direct what-to-do-instead, in his own loose phrasing.
- **He cut a whole post (#8).** Tighter thread beats completeness.
- **Sentence-case first letters, lowercase product names and bullets.** Not strict all-lowercase.
