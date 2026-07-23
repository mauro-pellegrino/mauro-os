# YouTube competitor mining — research

Date run: 2026-07-23. Channels sorted by Popular (all-time) + latest (recent baseline). Outlier rule: 3x or more the median of the channel's ~15 most recent videos. Full outlier list with view counts, dates, links and thumbnail URLs is in `01-outliers.csv`. Grid screenshots per channel were saved to your machine at `...\AppData\Local\Temp\claude-chrome-screenshots-VEGrmZ\`.

Two honesty notes up front. First, several titles reference tools/models I can't vouch for (Fable 5, GPT 5.6 Sol, Opus 4.7, GLM 5.2, etc.) because they postdate my knowledge and/or are just what's live on YouTube right now. I logged everything verbatim, I didn't verify any claim. Second, Justin Welsh returned no accessible long-form video grid (his YouTube is minimal), so he's not in the data. That leaves 9 channels.

---

## Recent baselines (for the 3x outlier math)

| Channel | Recent median | 3x threshold | Note |
|---|---|---|---|
| Nick Saraev | ~43K | ~129K | recent output well below his all-time course hits |
| Liam Ottley | ~25K | ~75K | recent posting is sparse and low vs his 1yr-old megahits |
| Nate Herk | ~68K | ~204K | steady, big all-time course hits |
| David Ondrej | ~45K | ~135K | |
| Dan Koe | ~112K | ~336K | off-lane topically (mindset / one-person business) |
| Greg Isenberg | ~74K | ~222K | |
| Marcos Ruiz | ~750 | ~2.2K | small channel, most on-lane to you (X to clients) |
| Alex Hormozi | ~218K | ~654K | off-lane topically (general wealth/business) |
| Jordan Platten | ~10K | ~30K | old hits are SMMA/ads; recent pivot to AI agency is the relevant part |

Read: on the big channels, the recent median is far below the all-time hits, so almost every all-time top video clears 3x. The useful signal isn't "which cleared 3x" (most did), it's the repeating shapes below.

---

## TASK 2 — Title formulas that repeat across the outliers

Ranked by how often they show up on top performers.

1. **Long time-box / marathon course** — "FULL COURSE", "X HOURS", "Master ... in 2 Hours".
   - "CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell" (Nick, 2.1M)
   - "Build & Sell n8n AI Agents (8+ Hour Course, No Code)" (Nate, 1.7M)
   - "AI Agents Full Course 2026 (2 Hours)" (Nick, 528K)

2. **Build & Sell [thing]** — the outcome is a sellable asset, not just knowledge.
   - "How to Build & Sell AI Agents: Ultimate Beginner's Guide" (Liam, 3.6M)
   - "Build & Sell with Claude Code (10+ Hour Course)" (Nate, 853K)

3. **"Build Anything/Everything with [tool], here's how"** — one template reused on every new tool/model.
   - "Build Everything with AI Agents: Here's How" (Ondrej, 1.7M)
   - "Build Anything With ChatGPT, Here's How" (Ondrej, 1.1M)
   - "Build anything with DeepSeek R1, here's how" (Ondrej, 590K)

4. **Fake-precise number + time box** — a specific $ or count, plus exact minutes.
   - "$2.4M of Prompt Engineering Hacks in 53 Mins" (Nick, 348K)
   - "ChatGPT Operator Built a $500/Day Business in 30 Minutes" (Greg, 938K)
   - "I can't believe we coded an app with AI in 67 mins" (Greg, 727K)

5. **"X just 10x'd / just destroyed Y" newsjack** — attach to a fresh launch or name.
   - "Andrej Karpathy Just 10x'd Everyone's Claude Code" (Nate, 650K)
   - "Google just destroyed all vibe-coding apps (Firebase Studio)" (Ondrej, 416K)

6. **"Clearly Explained"** — claim clarity on a confusing hot term.
   - "Model Context Protocol (MCP), clearly explained" (Greg, 1.3M)
   - "How AI agents & Claude skills work (Clearly Explained)" (Greg, 647K)

7. **Result + relatability qualifier** — a real number softened by "as a beginner" / "for a stranger".
   - "How I Sold These 4 AI Agents for $23,000 (as a beginner)" (Nate, 457K)
   - "Building a $1,000,000 Business for a Stranger in 42 Minutes" (Hormozi, 428K)

8. **Contrarian "instead"** — reject the obvious move, offer the real one.
   - "What I'd Learn Instead of Automation in 2026" (Nick, 492K)
   - "'Learn AI' Is Bad Advice. Learn This Instead" (Greg, 110K)

9. **Anti-hype "that actually work / with PROOF"**
   - "Building AI Agents that actually work (Full Course)" (Greg, 566K)
   - "3 Boring AI Systems That Sell For $4000+ Right Now (With PROOF)" (Platten, 67K)

10. **Free template / steal this / scripts exposed** — hand over the asset in the title.
    - "I Built the Ultimate Team of AI Agents in n8n (Free Template)" (Nate, 1.1M)
    - "How I Made $2M ONLY Using Twitter/X DM's (Scripts Exposed)" (Marcos, 5.4K)

11. **0 to N in a time box**
    - "How To Grow From 0 to 10,000 Followers (IN 90 DAYS)" (Marcos, 18K)
    - "$0 to $10k/mo in 70 Days With AI Lead Gen (Real Proof)" (Platten, 10K)

12. **Numbered "N [things]"**
    - "5 AI Startup Ideas So Good You'll Quit Your Job in 24hrs" (Greg, 402K)
    - "The 8 AI Skills That Will Separate Winners From Losers" (Liam, 1.6M)

---

## TASK 1 (part 2) — Video ideas for your channel

All drafts, all in your lane (AI content engine for agency owners), none final. Each = working title, the competitor outlier it's modeled on, and the angle. Titles with a number in them are placeholders until you sign off on a real public figure (per positioning.md). 18 here so you can cut.

1. **The Full AI Content Engine Course for Agency Owners (build it in a weekend)** — model: Nick "CLAUDE CODE FULL COURSE" / Nate "Build & Sell Course" — one long cornerstone video that installs your whole engine end to end.
2. **Build & Sell an AI Content System to Your Clients (full walkthrough)** — model: Liam "Build & Sell AI Agents" — package the engine you run as a client offer, not just self-use.
3. **Watch Me Build an Agency's Inbound Content Engine in [X] Hours** — model: Nick "Watch me start & sell an AI service in 10 hours" — real-time build on camera, fixed time box.
4. **I Let AI Run My Agency's Content for 30 Days (here's what it booked)** — model: Platten "I Let Claude AI Get Me Clients for 30 Days (240 Meetings)" — 30-day experiment tied to booked calls (needs a real, signed-off number).
5. **Replace Your Whole Content Team With One AI System** — model: Nate "Marketing Team with 1 AI Agent" — the cobbler's-children angle, one operator + system beats a team.
6. **What I'd Do Instead of 'Just Post More' in 2026 (for agency owners)** — model: Nick "What I'd Learn Instead of Automation" — contrarian: system over volume.
7. **5 AI Content Systems Every Agency Should Steal** — model: Greg "5 AI Startup Ideas" / Platten "3 Boring AI Systems" — numbered, stealable, proof attached.
8. **The AI Content Engine, Clearly Explained (why it beats posting more)** — model: Greg "MCP clearly explained" — explainer of the mechanism for people who think content doesn't convert.
9. **How I Turn One Client Case Study Into 30 Posts With AI** — model: Marcos "Use AI to Create 100+ Viral X Posts in 1 Hour" — one source, many posts, watch-me build.
10. **The Anatomy of a Top 1% AI-Native Agency's Content System** — model: Platten "Anatomy Of A Top 1% AI-Native Agency" — teardown of what the best actually run.
11. **I Studied 1,000 Agency Posts. Here's What Actually Books Calls** — model: Marcos "I Studied 1,000 X Hooks" — data-backed teardown, proof over theory.
12. **Copy My Exact AI Content Workflow (I'll give you the docs)** — model: Ondrej "just copy him" + Marcos "Steal My Strategy" — hand over the real workflow and voice docs.
13. **The Voice Doc That Kills 'Obvious AI' Content (build it in 20 minutes)** — model: Nate "How I Make Opus Think Like Fable (5 easy steps)" — anti-cringe pillar, the mechanic that removes AI tells.
14. **Cold Outreach Is Dying for Agencies. Build This Instead.** — model: Ondrej "X just destroyed Y" + your ICP's outbound burnout — content engine vs the outbound treadmill.
15. **How I'd Build an Agency's Inbound Engine From $0 (if I started today)** — model: Platten "Starting A New SMMA From $0 Using AI" / Koe "if I started over" — from-zero blueprint.
16. **0 to Booked Calls: A Low-Time Content System for Busy Agency Owners** — model: Marcos "0 to 10,000 in 90 days" — 0-to-outcome, low-time pillar, leading indicators so they don't quit at week 3.
17. **3 Boring AI Content Systems That Book Clients (with proof)** — model: Platten "3 Boring AI Systems That Sell (With PROOF)" — unsexy but proven, proof-first.
18. **How Agency Owners Actually Use AI for Content in 2026 (not the hype)** — model: Greg "that actually work" + Hormozi "How to Use AI in Your Business" — anti-hype positioning piece.

Note on lane discipline: Dan Koe and Alex Hormozi are the two off-lane channels (mindset / general wealth). I pulled their title MECHANICS (99%-of-people, time-boxed value, "for a stranger" series) but none of their topics. Don't make a "get rich" or "reinvent yourself" video, that's not your positioning.

---

## TASK 3 — Thumbnail patterns

Grouped from the grids I could view during the run (Nick, Liam most clearly) plus the outlier set. The full set of grid screenshots is on your machine (temp folder above) if you want to verify the grouping visually.

1. **Big ALL-CAPS text (2-4 words) + creator facecam + tool logos** — the dominant style across every AI/agency channel (Nick, Liam, Nate, Ondrej, Greg, Platten). Examples seen: "ZERO TO HERO", "No-code AI AGENTS full guide", "MUST HAVE AI SKILLS". The text is the promise, the logos signal which tools, the face adds trust.
2. **Hand-drawn / whiteboard diagram + facecam** — used on the marathon course hits ("FULL CLAUDE CODE COURSE" with a numbered board next to Nick's face). Signals depth and structure. Strong on the long-form course outliers.
3. **Concept illustration, no face** — rarer, used on trend/opinion pieces ("Death of the Smartphone"). Higher variance.
4. **Big number / $ figure as the focal point** — on the result videos ($ per day, $M, meetings booked). The number does the work.

Takeaway for you: default to style 1 (big caps promise + your face + the tool logos you actually use) for tactical videos, and style 2 (board/diagram + face) for the long "engine" course. Both read as operator, not guru, which fits your anti-cringe pillar.

---

## TASK 4 — Format check (AI/agency channels: Saraev, Ottley, Herk, Ondrej)

This is inferred from titles, durations and thumbnails, not from watching each video end to end, so treat it as a strong hypothesis, not confirmed.

- **Winners are long-form screen-share builds / courses**, not pure talking head. The biggest hits are multi-hour "FULL COURSE" videos, which are almost always talking-head intro then screen-share execution (building the thing live). Nick, Nate, Liam all fit this.
- **"Watch me build / live walkthrough"** is a recurring winning format (Nick's "start & sell in 10 hours", Platten's live SMMA walkthrough, Nate's "I Built..."). Screen-share heavy.
- **Ondrej leans more talking-head + screen-share hybrid**, with some documentary/personality pieces (the Sam Altman video) that are edited talking-head/voiceover.
- Pure talking-head dominates on the OFF-lane channels (Koe, Hormozi), which is a different game (authority/mindset), not what wins on the AI/agency channels.

Implication for your channel: your "engine course" and "watch me build" ideas (1, 2, 3, 9, 12) should be screen-share-first with a talking-head intro. That's the format the winners use in your category.

If you want, I can open the single top video on each of the 4 AI/agency channels and confirm the exact format (talking head vs screen-share vs board) instead of inferring, that's a few minutes more.
