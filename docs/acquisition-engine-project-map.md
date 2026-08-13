# The acquisition engine project map

**Written:** 2026-08-13
**What this is:** the framework for deciding which acquisition projects and which agents an agency should run to hit a revenue target, and in what order. Generalized from a live build. Every number is a bracket placeholder, fill them from your own data.
**Note:** this is the portable version of a business-specific map. Client and partner specifics are deliberately absent.

---

## Start from the equation, not from the channel list

```
Revenue = qualified calls × close rate × ACV
```

Every project has to move one of those three. A project that moves none of them is not a project, it is a hobby.

Most agency owners map their acquisition work as a list of channels. That produces a to-do list with no priority, because every channel looks defensible in isolation. Mapping against the equation forces the question that actually matters: **which of the three multipliers is currently binding?**

**How to find the binding one.** Write down four numbers: calls booked per week, calls that show and qualify, deals closed, revenue per deal. Then look at which one is furthest from where it needs to be. If calls are booking and nothing is closing, adding top-of-funnel feeds a funnel that leaks at the bottom, and every hour spent on reach is wasted.

This is the single most common misallocation in agency acquisition. Reach is visible, satisfying and measurable daily. Close rate is uncomfortable and only measurable monthly. So people work on reach.

---

## The four project groups

### A. Qualified call volume

| Project | When it earns a slot |
|---|---|
| **Video engine (YouTube), N boards/week** | Highest ceiling of any organic channel, and one of only two assets an LLM will cite. Also the most resistant to platform algorithm swings, because search and recommendation behave differently to feeds. |
| **Format discipline on existing channels** | When your own analytics show that a minority of your post shapes carry most of the reach. The fix is a rule, not new capacity, which makes it the cheapest project on any map. |
| **Your own site as a channel** | Almost always unowned, and almost always already producing calls nobody attributes. Comparison pages get cited by AI answer engines, positioning pages never do. |
| **Reply-to-call conversion on existing outbound** | Before adding an outbound channel, check whether the one you have leaks at the booking step. Good replies that never book is a conversion problem, and it will reproduce itself in every new channel you open. |
| **LinkedIn InMails** | Paid direct access to a named inbox, no connection needed, no deliverability layer, no spam folder. Strongest for buyers who actually live on LinkedIn (multi-brand operators, CMOs at larger companies). Weak for founder-led single-brand buyers, who are usually elsewhere. |

**On InMails specifically.** They show up at the top of most B2B outbound tier lists, and the ranking is defensible on reply rate. Two things to hold onto anyway:

1. **Gate them on your reply-to-call fix.** InMails cost money per send. If warm replies currently die before booking, InMails will reproduce that leak at a higher unit cost than email.
2. **The opener is research, not pitch.** The version that works is a named, specific observation about the prospect's own live work, which is also the thing an agent can produce at scale and a generic competitor cannot. Attach something forwardable, because a large share of B2B deals contain someone who has to sell it internally.

Measure sends → replies → calls booked → qualified → closed. Kill or scale on the call number. Reply rate flatters every outbound channel ever invented.

**And on tier lists generally:** a generic ranking is a reason to run a test, never a reason to reweight a channel mix you have your own numbers for. If your own data says organic content drives most of your qualified pipeline, a list that puts content at C tier is describing a different business.

### B. Close rate

| Project | When it earns a slot |
|---|---|
| **Lost-call intelligence** | Always, and it is almost always unbuilt. If your calls are recorded, the objection that kills a deal is the brief for the content that prevents it and for the qualification copy that stops the wrong prospect booking. Most agencies have hundreds of hours of this sitting unread. |
| **Proof asset factory** | One forwardable client proof per month on a fixed calendar slot. Multi-stakeholder deals always contain a forwarder. Most agencies discover their proof "barely exists" only when a prospect asks for it. |
| **Qualification tightening** | When your intake marks prospects qualified and the sales verdict disagrees. Every wrong-tier booking costs a sales hour and drags the close rate the marketing side gets judged on. |

### C. ACV

Usually blocked on data rather than on ideas. The candidate is whichever segment has the highest lifetime value in your own buyer research. Whether it deserves a project depends on the spread between what that segment pays and what your median client pays. If you do not have that spread written down, that is the project.

### D. Measurement

**Attribution you can trust**, which means two cheap things: a "where did you find us" field at booking, and actually using whatever link-tagging system you already built. Self-reported attribution beats referrer data badly, because people read an answer or see a post and then navigate directly.

Without this, every allocation decision above is a guess wearing a spreadsheet.

---

## The agents

The test for building one: the work is **fan-out** (many similar items) or **recurring** (the same job weekly). Those are what a large token budget is genuinely good at. One-off judgement work is not.

| Agent | Feeds | What it does | Why an agent |
|---|---|---|---|
| **Call-loss analyst** | Close rate | Weekly. One subagent per lost call, clusters kill reasons, outputs an objection inventory plus content briefs and qualification fixes | Dozens of transcripts is pure fan-out. Single-threaded it is a week of work, parallel it is an afternoon |
| **Prospect research agent** | Outbound | Given a target account: pulls specific observations about their live work, drafts the personalized opener, picks the proof asset to attach | The one form of personalization a competitor cannot copy, and it does not scale by hand |
| **Pre-call brief** | Close rate | Before each call: prospect tier, objection pattern for their profile, which proof to send | The first feature worth putting in an acquisition-side internal tool. The thing your closer will actually open |
| **Outlier scout** | Volume | Weekly read of your analytics plus tracked competitor accounts, returns which formats to run and which to skip | Recurring, mechanical, judgement-light. Exactly what a scheduled agent is for |
| **Board / asset builder** | Video engine | Source material in, finished production board plus title and hook out | Real weekly volume on video is not reachable by hand alongside a full role |
| **Site / AEO writer** | Owned channel | Comparison pages, citation tracking, quarterly re-win of decayed phrases | AI citations decay in roughly three months, so this is maintenance, not a launch |
| **Reply triage** | Outbound | Triages replies across channels, drafts the same-day follow-up | Speed is the entire lever on a warm reply, and speed is what context switching destroys |
| **Attribution reconciler** | Measurement | Weekly join of booking data, call tracker and post data, flags unknowns instead of guessing | Removes the "we don't know" rows before they reach a decision |

---

## Sequencing, which matters more than the list

The failure mode is running every project at 20%. Count your currently active lanes honestly. If it is more than five, the two that matter are already getting leftovers.

**Days 0-30. Three projects, nothing else.** Pick the ones that need nobody else's calendar and that tell you where the rest should point. Usually: lost-call intelligence, attribution, and the format rule. All three are cheap and all three produce information.

**Days 30-60.** The projects that need other people. Proof assets, video at real volume, the reply-to-call fix.

**Days 60-90.** Owned-channel build, paid outbound tests gated on the conversion fix, and the first internal tool that someone other than you logs into.

That last point is the one worth holding: an agent that only you use makes you productive. A tool other people log into makes you infrastructure. The second one is what gets valued.

---

## Two rules that keep this map honest

1. **Nothing gets built without a user waiting for it that week.** The most common way this map fails is a project that is genuinely clever, serves four internal people, and never ships.
2. **A platform-wide drop is not your content getting worse.** Check whether the accounts you benchmark against dropped in the same window. If they did, it is a platform event, and rebuilding a working system in response to it is the expensive mistake.
