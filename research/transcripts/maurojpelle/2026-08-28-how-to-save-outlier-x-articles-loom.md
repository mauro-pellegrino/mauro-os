# How to Save Twitter Outlier Articles

**Source:** Loom (Mauro, screen recording + voiceover)
**URL:** https://www.loom.com/share/4aab7dc3e5934c9bbfe23e0f4fb568b5
**Fetched / transcribed:** 2026-08-28 (transcript pasted by Mauro; the Loom page exposes no transcript)
**Speaker:** Mauro (@maurojpelle)
**Use:** source material for X article + short-form content, and the spec for the outlier-article corpus that a future X-article skill gets built from.

---

## Transcript (verbatim, timestamps as given)

0:01 Hey bro, okay, so this is how you find the outliers on Twitter Specifically outliers for articles and then we save them into cloud code.
0:11 The first thing that I would like to do is just pick out for example an account that we know we like.
0:18 Obviously this guy is like super really good, of course, and he has a lot of articles and And what you can check is like, okay, which ones are actually, you know, his top articles, right?
0:34 So I don't think we can filter them by visualizations, like views. We know this one is really good, right? So at the same time, this one could be one that you can save.
0:47 What I like to do is to do this. The screenshot of the title needs to be here and not inside of the article itself.
0:56 Why? Because we want to see the title and then this description, which is the beginning of the text as well.
1:02 Obviously, we can zoom in a bit, or we can, you know, actually screenshot this if we want. We can actually copy the image as well.
1:13 But yeah, I think the best way to do it is to tell Cloud Code, for example, I'm going to start a new window and then I'm going to say, you know, if you were in Cloud, you can just start, and then you can say, I'm in Cloud Code.
1:29 Yes, I dress this folder, and then just say, I'm going to save, I'm going to save. Save, let me zoom in.
1:41 I'm going to save um outlying articles with three things. And then you can say um title, uh thumbnail and text of the article.
2:01 We need to store these in order to create future skills for X articles. Is that fine? And then what we will do now is just say that we will save about 50 of them.
2:19 I will send the four components that we mentioned and the link. So what I will do now is go back and then what I will do first is go back like I told you take a screenshot and then this is the first screenshot.
2:39 What I will do is I will select clipboard, screenshot here, and then Ctrl. Another thing that you can do as well is Um with the screenshot of the title and the and the thumbnail, you already have that done, right?
2:56 But you can also just come here, copy image, and then do this, even better. Because I think if you do this, it like gets the details inside and then this.
3:11 Oh, f***. S***. F***. With the title as well. We want to grab the title because we want the Cloud Code to ment to know um save this into the Growth Hub repo, but don't make changes.
3:37 To any skill yet until we have 50 articles. That's one, right? And we want to do this for a lot of them.
3:49 So, what I will try is as well, you know, we can see different, you know, different creators, of course. This one looks really good.
4:03 Because this one looks really good, you know why? Because this one is something that we can do as well. So we can also.
4:12 If we do this, the good thing about doing this from the home is that we can also grab the profile, you know, like this, paste, paste one.
4:25 This doesn't, we don't have to copy this image because it's just a screenshot, so you don't need to. I copied the image before because it's it was like more of a it was more of a you know HTML infographic, but this one is just more you know copy paste then I'll do another one, we don't need to.
4:49 Send every time you, you know, you don't need to send every time you grab one, right? We can come to home as well and see people that have a lot of followers.
5:01 Let me see this guy: 11.5. We'll see. His articles are s***. S*** articles. What the f*** is this, bro? This s*** is actually.
5:13 Ass, bro. Get the f*** out of here. That's terrible. You can see this. This people, these people are stupid. Sorry, like, um, you can make a tweet out of this if you want.
5:23 I'm not saying they're stupid, but it's so obvious that they take a YouTube video that they've done and they just copy and paste the script.
5:33 You know? Don't you see it? Like how this is literally a YouTube video? That's terrible. That's terrible. Lazy. Lazy. F****** horrible.
5:43 Um let me see this guy Horrible. I think uh Nicholas Cole is good at good at these ones. Let me see Yeah, he has some really good uh you know 35k um Yeah, these ones do look good.
6:05 Like, obviously, I'm looking at visualizations. This one's really good as well. I think I'm gonna grab a couple of them.
6:12 You could grab a couple of them from him. I'll grab this one. This one's really good. Yeah, so you know how the process works.
6:22 Like, we want to grab articles that are really. Really good and we can actually create a skill. We don't want Claude to start doing skills, so we would just want to save everything, just save.
6:35 Save, save, save, save. We don't want to do anything yet, like the skills, we don't care. We just want to save yet.
6:41 And then we'll s then we can see if like, okay, we want to make a template. I don't know. Um, this one's crazy.
6:48 This one's really good. I'm gonna save them, okay? So I'm gonna save articles for you in the in the fold in the bookmarks.
6:55 I'm gonna add the folder and I'm gonna create a folder called Articles Outlying Articles. I don't know if you say outlying like this, but it's fine.
7:07 Outlying articles, okay. Um I'm gonna save that. I'm gonna save um let's see, go up. This one is really good.
7:21 Save that. Add the folder, outline articles. Okay, I'll keep saving and you can get them from the saved, or you can just search them yourself.
7:29 But I hope you get the the idea.

---

## Process spec (extracted)

1. Start from an account you already rate, not from a random scroll. Open its articles.
2. There is no filter for article views on X, so read the view count off each article manually. Views are the only number used to pick.
3. Screenshot from the feed, not from inside the article. The frame must contain the title, the cover image and the opening lines of the body.
4. If the cover is an HTML infographic, right-click and copy image instead of screenshotting, so the detail inside survives.
5. Grabbing from the home feed also captures the account/profile in the frame.
6. Save four components per article: title, thumbnail, text, link.
7. Batch them. Do not send one at a time.
8. Explicit instruction to Claude Code: save into the repo, do not touch or build any skill until all ~50 are in.
9. Collection layer: an X bookmarks folder ("outlying articles"), sorted later.
10. Judgement calls in the video: follower count does not predict article quality (an 11.5k-follower account had none worth saving); the dominant failure mode is copy-pasting a YouTube script into an article; Nicolas Cole (transcript says "Nicholas") is named as good at the format, with one article around 35k views.

## Mauro's ask on this source (2026-08-28)

"With all this content you can create at least 2 articles and maybe between 20 and 25 tweets, always following the path and taking note about the latest pushes we have done with titles and ways to write everything."
