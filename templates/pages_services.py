# Service pages added by the autopilot plan (October 2026).
# One page per service so each one can own its own searches. The approved copy
# in pages.py is untouched; these pages link back to it as their hub.
# Facts used here must exist in autopilot/facts.md.
ORG = {"@id": ORG_ID}
CALL = f'<a class="btn" href="tel:{PHONE}"><span class="dot"></span>Call 1300 889 840</a>'

def steps(items):
    out = '<ul class="list">'
    for title, line, more in items:
        extra = "".join(f"<p>{m}</p>" for m in more)
        out += f'<li class="reveal"><strong>{title}</strong><div><p>{line}</p>{extra}</div></li>'
    return out + "</ul>"

# ================= DENTAL SEO =================
SEO_FAQ, SEO_FAQ_S = faq([
 ("How long until dental SEO works?", "Map movement usually shows in 6 to 10 weeks. Competitive treatment terms like \"dental implants\" take 4 to 9 months. Google Ads covers the gap from week one."),
 ("Do I need SEO if I'm already running Google Ads?", "Usually yes. Ads stop the day you stop paying. The map listing and treatment pages keep working, and they get cheaper over time."),
 ("Will you work with my competitor?", "Not if they're a dental practice within 7km of you."),
 ("Can I use my Google reviews on my website?", "Not as testimonials about clinical care. Patients can leave them and you can reply to them, and they help your map ranking, but they can't be reused as promotional content."),
 ("Do you work outside Sydney?", "Yes. We're based in Sydney and work with clinics Australia-wide."),
])

def dental_seo_body(R):
    crumbs = [("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("Dental SEO", "dental-seo.html")]
    return f"""
<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">Dental SEO</p>
  <h1 style="margin-top:22px">Dental SEO that starts with the map, because that's where your <span class="u">patients click</span>.</h1>
  <p class="lead">Someone searches "dentist near me" and gets three practices on a map. Most of them never scroll past it. We get your practice into that map, then build the site and content underneath it so it stays there.</p>
  <p class="muted" style="margin-top:14px">We do this for more than 100 dental clinics across Australia.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#how">How we do it</a></div>
</div></section>

<section class="section tight" id="how"><div class="wrap">
  <div class="grid g3" style="margin-bottom:clamp(40px,6vw,80px)">
    <div class="stat reveal"><strong>100+</strong><span>dental clinics we manage</span></div>
    <div class="stat reveal"><strong>6 to 10 weeks</strong><span>for map movement, usually</span></div>
    <div class="stat reveal"><strong>7km</strong><span>minimum gap between our dental clients</span></div>
  </div>
  <p class="eyebrow reveal" style="margin-bottom:18px">The order we do it in</p>
  {steps([
   ("1. Your map listing first", "Your Google Business Profile is the most valuable thing you own online, and most practices treat it as a form they filled in once.",
    ["We set the right primary category, list every treatment as a service, add real photos of your team and rooms, and make your hours accurate. Google leans towards practices that are open when someone searches, so hours matter more than they used to.",
     "Then we make your name, address and phone number match everywhere they appear online. Mismatched details are the most common reason a good practice sits fourth in its own suburb."]),
   ("2. Reviews, steadily", "Reviews are one of the biggest things Google weighs on the map, and a steady flow beats a burst.",
    ["We set up a simple way for patients to leave one and help you reply, without crossing AHPRA's line: patients can review you, but reviews can't be reused as testimonials in your ads."]),
   ("3. A page for every treatment", "\"Dental implants\" and \"check-up and clean\" are different searches from different people.",
    ["Each treatment gets its own page that answers what patients actually ask: what it involves, roughly how long it takes, and how to book. A single services page rarely ranks first for anything."]),
   ("4. The technical work underneath", "Fast on a phone, clean structure, and the right schema so Google and AI assistants know exactly what you do and where.",
    ["It's the unglamorous part, and it's what holds everything else up."]),
   ("5. AI search", "Patients now ask ChatGPT and Google's AI whether they need a crown or a filling, or who can see them today.",
    [f"We write your pages so the answer is clear in the first lines, which is what those assistants quote. <a class=\"link\" href=\"{R}ai-marketing.html\">More on AI search</a>."]),
  ])}
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">How long it takes</p><h2 style="margin-top:18px">Straight answer: weeks for the map, months for the big terms.</h2></div>
    <div class="reveal">
      <p class="lead">Map movement usually shows in 6 to 10 weeks. Competitive treatment terms like "dental implants" take 4 to 9 months.</p>
      <p style="margin-top:18px">That gap is why most of our clients run Google Ads at the start. Ads bring enquiries in days while SEO builds, and they tell us which treatments actually convert before we spend months ranking for them. <a class="link" href="{R}dental-marketing.html">See everything we do for dentists</a>.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">What happens to the enquiries</p><h2 style="margin-top:18px">Ranking is half the job.</h2></div>
    <div class="reveal">
      <p class="lead">An enquiry answered in a minute behaves completely differently to one answered the next morning.</p>
      <p style="margin-top:18px">Every enquiry from search goes through SmileOX, our own lead platform. It replies instantly, asks the questions your team would ask, scores the lead, and texts back the calls you miss. Your team only speaks to people ready to book. <a class="link" href="{R}smileox.html">See how SmileOX works</a>.</p>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g2">
    <div class="card reveal"><h3>What you get</h3><ul>
      <li>Your map listing set up properly and kept alive</li>
      <li>A page for each treatment you want more of</li>
      <li>Reporting on enquiries and bookings, not impressions</li>
      <li>A call every fortnight to look at the numbers together</li>
    </ul></div>
    <div class="card reveal"><h3>What we won't do</h3><ul>
      <li>Take on another dental clinic within 7km of you</li>
      <li>Promise you page one by Friday</li>
      <li>Write content that breaks AHPRA's advertising rules</li>
    </ul></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Straight answers</p><h2 style="margin-top:18px">Questions dentists ask about SEO.</h2></div>
    <div class="reveal">{SEO_FAQ}</div>
  </div>
</div></section>
{author_section(R)}
{cta("Empty books give us anxiety. Genuinely.", "If your map listing isn't bringing in the patients it should, call us. Twenty minutes, no pitch, just a look at what's going on and what we'd do about it.", R=R)}
"""

add(slug="dental-seo.html",
    title="Dental SEO Australia | SEO for Dentists, Map Listing First | GYA",
    desc="Dental SEO built around the map listing, where the clicks are. Local SEO, treatment pages and AI search for 100+ clinics across Australia.",
    crumbs=[("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("Dental SEO", "dental-seo.html")],
    nav="dental-marketing.html",
    schema=[{"@type": "Service", "name": "Dental SEO", "provider": ORG, "serviceType": "Dental SEO, local SEO for dentists, Google Business Profile optimisation", "areaServed": "AU"}, SEO_FAQ_S],
    body=dental_seo_body)

# ================= DENTAL GOOGLE ADS =================
ADS_FAQ, ADS_FAQ_S = faq([
 ("How quickly do Google Ads bring in enquiries?", "Usually within days of going live. In our first week with a new clinic, ads are running by day four."),
 ("How much should I spend on Google Ads?", "Most clinics we manage put between 3% and 8% of revenue into marketing, mostly Google Ads and SEO. We set the ads budget by treatment goal and how competitive your suburb is, then track it to booked appointments."),
 ("Should implant and check-up ads share a budget?", "No. An implant patient and a check-up patient are worth very different amounts, so each treatment gets its own campaign and its own budget."),
 ("Do I still need Google Ads if my SEO is good?", "Usually yes, at least at the start. SEO takes months and only covers the searches you rank for. Ads cover the gap and show us which treatments actually convert."),
 ("Can my ads include special offers?", "Only with clear terms. AHPRA's advertising rules don't allow offers without them, and we write every ad and landing page to those rules before it goes live."),
 ("Will you run ads for my competitor?", "Not if they're a dental practice within 7km of you."),
])

def dental_google_ads_body(R):
    crumbs = [("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("Dental Google Ads", "dental-google-ads.html")]
    return f"""
<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">Google Ads for dentists</p>
  <h1 style="margin-top:22px">Google Ads for dentists, built per treatment and per suburb, and judged on <span class="u">booked patients</span>.</h1>
  <p class="lead">Google Ads is the quickest way to get new patients ringing, usually within days. But only if implants, Invisalign, emergency and check-ups each get their own campaign, every click lands on a page about the thing they searched for, and you can see which ads actually filled a chair. That's how we run them.</p>
  <p class="muted" style="margin-top:14px">We manage marketing for more than 100 dental clinics across Australia.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#how">How we set it up</a></div>
</div></section>

<section class="section tight" id="how"><div class="wrap">
  <div class="grid g3" style="margin-bottom:clamp(40px,6vw,80px)">
    <div class="stat reveal"><strong>100+</strong><span>dental clinics we manage</span></div>
    <div class="stat reveal"><strong>Day 4</strong><span>your ads go live in week one</span></div>
    <div class="stat reveal"><strong>7km</strong><span>minimum gap between our dental clients</span></div>
  </div>
  <p class="eyebrow reveal" style="margin-bottom:18px">How we build a dental account</p>
  {steps([
   ("1. One campaign per treatment", "An implant patient and a check-up patient are worth completely different amounts, so they don't belong in the same campaign sharing a budget.",
    ["Implants, Invisalign, emergency, cosmetic and general each get their own campaign. That way the budget goes where you want the patients, and a cheap check-up search can't quietly eat the money meant for implants."]),
   ("2. Built around your suburbs", "Patients book close to home. Ads shown to people who'll never make the drive are money gone.",
    ["We target the suburbs you actually draw patients from, and shift spend toward the treatment and suburb combinations bringing in enquiries this month, not the plan someone set in January."]),
   ("3. Negative keywords from day one", "This is the quiet work that saves the most money.",
    ["Dental accounts leak budget on job seekers, students, DIY searches and treatments you don't offer. We build those negative keyword lists before the first ad runs, then keep adding to them every week the account is live."]),
   ("4. Every click lands on the right page", "Sending ad traffic to your homepage is the most expensive habit in dental advertising.",
    [f"Someone who searched for Invisalign lands on a page about Invisalign, with a clear way to book. If those pages don't exist yet, we build them. <a class=\"link\" href=\"{R}dental-websites.html\">More on dental websites</a>."]),
   ("5. Tracked to the booking, not the click", "Clicks are easy to buy. Patients are what you're paying for.",
    ["We track calls and forms from every campaign, and SmileOX picks up each enquiry the moment it comes in. So we optimise toward booked appointments, and you can see which treatments and suburbs are worth more budget."]),
   ("6. Written to AHPRA's rules", "Every ad and landing page is checked against the AHPRA advertising guidelines before it goes live.",
    ["No testimonials about clinical care, nothing that sets up unreasonable expectations, and no offers without clear terms. Getting a practice in trouble isn't a growth strategy."]),
  ])}
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Ads or SEO?</p><h2 style="margin-top:18px">Straight answer: usually both, ads first.</h2></div>
    <div class="reveal">
      <p class="lead">Google Ads can produce enquiries in days. Map movement from SEO usually takes 6 to 10 weeks, and competitive terms like "dental implants" take 4 to 9 months.</p>
      <p style="margin-top:18px">So ads cover the gap while SEO builds, and they tell us which treatments actually convert before we spend months ranking for them. Ads stop the day you stop paying. The map listing keeps working. <a class="link" href="{R}dental-seo.html">How we do dental SEO</a>.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">What happens to the enquiries</p><h2 style="margin-top:18px">A click you paid for deserves a fast reply.</h2></div>
    <div class="reveal">
      <p class="lead">You pay for the click whether or not anyone answers. An enquiry answered in a minute behaves completely differently to one answered the next morning.</p>
      <p style="margin-top:18px">Every enquiry from your ads goes through SmileOX, our own lead platform. It replies to new enquiries in under 60 seconds, asks the questions your team would ask, scores the lead, and texts back the calls you miss. Your team only speaks to people ready to book. <a class="link" href="{R}smileox.html">See how SmileOX works</a>.</p>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g2">
    <div class="card reveal"><h3>What you get</h3><ul>
      <li>A campaign for each treatment you want more of</li>
      <li>Negative keyword lists built on day one and kept up</li>
      <li>Call and form tracking, so you know which ads booked patients</li>
      <li>A call every fortnight to look at the numbers together</li>
    </ul></div>
    <div class="card reveal"><h3>What we won't do</h3><ul>
      <li>Run ads for another dental clinic within 7km of you</li>
      <li>Report on clicks and impressions and call it a result</li>
      <li>Spend your budget marketing ourselves</li>
      <li>Write ads that break AHPRA's advertising rules</li>
    </ul></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Straight answers</p><h2 style="margin-top:18px">Questions dentists ask about Google Ads.</h2></div>
    <div class="reveal">{ADS_FAQ}</div>
  </div>
</div></section>
{author_section(R)}
{cta("Empty books give us anxiety. Genuinely.", "If you're paying for Google Ads and can't say which patients came from it, call us. Twenty minutes, no pitch, just a look at your account and what we'd change.", R=R)}
"""

add(slug="dental-google-ads.html",
    title="Google Ads for Dentists | Dental PPC Agency Australia | GYA",
    desc="Google Ads for dentists, built per treatment and per suburb, with negative keywords from day one and tracking to booked patients. 100+ clinics Australia-wide.",
    crumbs=[("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("Dental Google Ads", "dental-google-ads.html")],
    nav="dental-marketing.html",
    schema=[{"@type": "Service", "name": "Dental Google Ads", "provider": ORG, "serviceType": "Google Ads for dentists, dental PPC, dental Google Ads management", "areaServed": "AU"}, ADS_FAQ_S],
    body=dental_google_ads_body)

# ================= MISSED CALL TEXT BACK (SmileOX) =================
MCT_FAQ, MCT_FAQ_S = faq([
 ("What is missed call text back?", "When someone rings your practice and nobody picks up, they get a text within seconds asking how we can help. They reply to you, instead of ringing the next practice on their list."),
 ("Won't an automatic text annoy people?", "Not when it reads like a person wrote it. SmileOX answers the obvious questions and hands straight over to your team the moment a human is needed. Nobody gets stuck in a loop."),
 ("Does it work after hours and on weekends?", "Yes. It runs 24/7, so the call that comes in at 7pm on a Saturday gets the same reply as one at 10am on a Tuesday."),
 ("Does it replace my front desk?", "No, it backs them up. Calls get missed because your team is busy with the patients in front of them. The text buys them time, and the lead is waiting in a ranked list when they're free."),
 ("Can I use it if another agency runs my ads?", "Yes. SmileOX sits in front of whatever is producing your enquiries, whoever runs it."),
 ("Is it included with GYA marketing?", "Yes. SmileOX comes with every GYA marketing engagement. It also runs on its own if you only want the follow-up side."),
])

def missed_call_body(R):
    crumbs = [("Home", "index.html"), ("SmileOX", "smileox.html"), ("Missed call text back", "smileox-missed-call-text-back.html")]
    return f"""
<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">SmileOX · Missed call text back</p>
  <h1 style="margin-top:22px">Missed a call? They get a text within seconds, so they reply to you instead of <span class="u">the next practice</span>.</h1>
  <p class="lead">That's missed call text back. Someone rings, nobody can get to the phone, and SmileOX sends them a text asking how we can help. Replying to a text is easier than leaving a voicemail, and once they've replied, they're talking to you. Not ringing down the list.</p>
  <p class="muted" style="margin-top:14px">Part of SmileOX, the lead platform we built and run for our clinics. Not someone else's software with our logo on it.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#how">How it works</a></div>
</div></section>

<section class="section tight" id="how"><div class="wrap">
  <div class="grid g3" style="margin-bottom:clamp(40px,6vw,80px)">
    <div class="stat reveal"><strong>&lt;60s</strong><span>first response to a new lead</span></div>
    <div class="stat reveal"><strong>24/7</strong><span>weekends and after hours included</span></div>
    <div class="stat reveal"><strong>14 days</strong><span>of follow-up for people not ready yet</span></div>
  </div>
  <p class="eyebrow reveal" style="margin-bottom:18px">What happens after a missed call</p>
  {steps([
   ("1. The call rings out", "It happens in every practice. Someone's at the counter paying, the dentist needs a hand, it's lunch, or it's 6:15 and the lights are off.",
    ["None of that is your team doing anything wrong. There's one phone and a lot going on."]),
   ("2. A text goes out within seconds", "Before they've had a chance to look up another practice, they've got a message from yours.",
    ["It's short and friendly, it asks how we can help, and it's sent from your practice. It doesn't push an offer or make promises. It just starts the conversation."]),
   ("3. SmileOX picks up the reply", "When people text back, it's usually with what they need: a check-up, a sore tooth, a question about Invisalign.",
    ["SmileOX answers the simple stuff, like hours and how to book, and asks the questions your team would ask. If someone needs a person, it hands straight over."]),
   ("4. Your team gets a ranked list", "Every lead is scored hot, warm or cool, so your front desk knows who to call back first.",
    ["They open one list in order of value instead of a pile of voicemails, and they ring the people ready to book while those people still want to."]),
   ("5. Not ready yet? They're not forgotten", "Plenty of people ring to ask a question and aren't booking today.",
    ["They go into a 14-day follow-up sequence for the treatment they asked about, so an implant question gets implant answers. Most practices never speak to these people again."]),
   ("6. You see what the missed calls were worth", "This is the bit practices usually find most surprising.",
    ["Because SmileOX sees both the enquiry and the booking, you can finally see how many missed calls turned into booked patients, and which ads or listings they came from."]),
  ])}
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Why it matters</p><h2 style="margin-top:18px">Every clinic misses calls. Most never find out what they were worth.</h2></div>
    <div class="reveal">
      <p class="lead">A voicemail is easy to ignore. A missed call with no follow-up looks, from the patient's side, exactly like a practice that doesn't want them.</p>
      <p style="margin-top:18px">People looking for a dentist usually have a few names in mind. If you don't answer, the next one might. The text closes that gap without your team having to stop what they're doing. And if you're paying for Google Ads, a missed call is a click you've already paid for. <a class="link" href="{R}dental-google-ads.html">How we run Google Ads for dentists</a>.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Where the calls come from</p><h2 style="margin-top:18px">It works on every line, not just one campaign.</h2></div>
    <div class="reveal">
      <p class="lead">Calls from your Google Ads, your map listing and your website all land in the same place. So do forms, Meta lead forms, Instagram DMs and email.</p>
      <p style="margin-top:18px">That matters because your map listing has a call button on it, so plenty of calls never touch your ads at all. Getting found is the first half. <a class="link" href="{R}dental-seo.html">How we do dental SEO</a>. Answering is the second half, and that's what SmileOX is for. <a class="link" href="{R}smileox.html">See everything SmileOX does</a>.</p>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g2">
    <div class="card reveal"><h3>What you get</h3><ul>
      <li>A text back within seconds on every missed call, day or night</li>
      <li>Replies handled, with a hand-over to your team when it needs a person</li>
      <li>Every lead scored hot, warm or cool</li>
      <li>14-day follow-up for people who aren't ready to book yet</li>
      <li>Reporting on booked patients, not just calls</li>
    </ul></div>
    <div class="card reveal"><h3>What it won't do</h3><ul>
      <li>Trap people in a bot conversation when they want a human</li>
      <li>Replace your front desk</li>
      <li>Send offers or promises your practice hasn't signed off</li>
    </ul></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Straight answers</p><h2 style="margin-top:18px">Questions dentists ask about missed call text back.</h2></div>
    <div class="reveal">{MCT_FAQ}</div>
  </div>
</div></section>
{author_section(R)}
{cta("Empty books give us anxiety. Genuinely.", "If you've got no idea how many calls you missed last week, call us. Twenty minutes, no pitch, just a look at where your enquiries are going and what we'd do about it.", R=R)}
"""

add(slug="smileox-missed-call-text-back.html",
    title="Missed Call Text Back for Dentists | SmileOX by GYA",
    desc="Missed call text back for dental practices. Every unanswered call gets a text within seconds, day or night, so patients reply to you, not the next practice.",
    crumbs=[("Home", "index.html"), ("SmileOX", "smileox.html"), ("Missed call text back", "smileox-missed-call-text-back.html")],
    nav="smileox.html",
    schema=[{"@type": "Service", "name": "Missed call text back for dental practices", "provider": ORG, "serviceType": "Missed call text back, dental lead follow up", "areaServed": "AU", "isRelatedTo": {"@type": "SoftwareApplication", "name": "SmileOX"}}, MCT_FAQ_S],
    body=missed_call_body)
