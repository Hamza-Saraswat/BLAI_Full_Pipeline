# SOURCE CACHE
# fetched via: web_extract
# accessed: 2026-11-25
# note: page text as fetched this session; em dashes (U+2014) replaced with -- per repo convention.

# url: https://news.ycombinator.com/item?id=48346990
# title: Why not just use open webui? | Hacker News
# tier: tier 4 (community)
# note: comment thread attached to the story "Odysseus - self-hosted AI workspace" (item 48346693).
# Timestamps on the page read "5 months ago" relative to 2026-11-25 (roughly June 2026; one comment
# references "launching tomorrow, June 1st"). This is standing sentiment about Open WebUI, NOT
# reaction to 0.13.5, which shipped 2026-11-25. Em dashes (U+2014) replaced with --.

---

[patosullivan, 5 months ago, on: Odysseus - self-hosted AI workspace]
Why not just use open webui?

[andai, 5 months ago]
I tried installing openwebui once. I gave up after the first 12 gigabytes of pip packages. Made my own LLM chat UI in 500 lines of HTML/JS. That's really all I needed.
This project does look fun though.

[redrove, 5 months ago, replying to andai]
Wow, if you you could've just done docker compose up. I guess we'll never know.

[enos_feedler, 5 months ago, replying to andai]
did you share your UI anywhere? would like to just pull a proven one versus vibe code my own.

[jerieljan, 5 months ago, replying to andai]
Surprisingly, there's a lot of items I'm seeing at first glance here at Odysseus that open-webui either doesn't have or takes extra effort to add in and I've used the latter for a really long time already.
Stuff like an agent mode, deep research and document work are things you'd be able to have with open-webui as well but Odysseus seems to have them thought out.

[bluejay2387, 5 months ago]
I am a 'fan' of Open Web UI, but the document editing mode is a compelling feature that Open Web UI does not have. I'll probably wait a while before trying Odysseus... let the inevitable security problems work themselves out.

[thayne, 5 months ago]
Open webui isn't fully open source, because it doesn't allow you to change or remove Open Webui branding.
I don't know if that was a motivation for creating this, but it is a reason some people might choose not to use it.

[dakolli, 5 months ago]
The truth is, there's something about the vibe coder hive mind where they all create the same thing. Everyone is working on the same thing. There's hundreds of projects like this where the creator thinks they've created the most unique powerful thing.
I think it demonstrates how overuse of LLMs for brainstorming/planning and building destroys creativity. That zeitgeist changes from month to month, but when a vibe coded "AI Native" project gets released you'll always see dozens of people in the replies talking about the identical project they've also built or are working on.
I also notice this in my own work, the people who have most eaten the LLM brainworm will come to me asking for us to build the same projects. They all eventually converge to wanting some sort of power user app (like this) that can just do everything because AI is magic to them and there's no reason why it can't do everything.
I hate Peter Thiel but he has that famous quote form years ago where he says not to build the obvious thing because the obvious thing isn't special, so maybe this has always been a phenomenon.

[skeledrew, 5 months ago]
I think the thing is users run into the same problems (barely desirable tool UX), and arrive at very similar solutions (but with their own small twists and preferences). And now that the barrier to make things is essentially gone, they jump in and make things that git their own desires week because nothing out there was an exact fit.
Like I found a really cool project a few weeks ago that I started using and even made a few QoL changes to. Then I thought of the many other changes I wanted, and that the project was written in a language I'm not familiar with (Rust), and I started a port in what I know well (Python) so that I'll be able to actually review the code if needed and generally make better architectural decisions.

[doright, 5 months ago]
It's like the Lisp Curse but for everything now.

[anigbrowl, 5 months ago]
Blockchain solves this

[BoredPositron, 5 months ago]
It's personal computing time...

[loctran0323, 5 months ago]
Yea good point, the branding clause is a real gotcha, technically "open source" but with that restriction baked in, which makes it source-available rather than properly free under the OSI definition. A lot of people don't realize until they try to fork or rebrand it for a team/customer deployment and hit the wall.
Conifer (launching tomorrow, June 1st) goes the other way on this, properly open source with no branding strings attached, so you can actually fork or rebrand if you need to. Local AI runtime + IDE, native on Mac/Linux/Windows: conifer.build

[dikei, 5 months ago]
Plus, if you look at OpenWebUI horror of a commit history, they don't often take external contributions.
