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

# ================= AI SEARCH FOR DENTISTS =================
AI_FAQ, AI_FAQ_S = faq([
 ("How do I get my dental practice to show up in ChatGPT?", "Make it easy for the assistant to be sure about you. Your name, address, phone and treatments need to match everywhere you're listed, each treatment needs its own page that answers patient questions plainly in the first lines, the code on your site should spell out what you do and where, and you need a steady flow of real reviews."),
 ("Can you guarantee ChatGPT or Google's AI will recommend my practice?", "No, and nobody honestly can. Nobody controls what an AI assistant says. What we can do is fix the things that make a practice easy to recommend, then check how the assistants describe you and keep fixing what they get wrong."),
 ("Is AI search different from dental SEO?", "Less than people think. Most of the work is the same: an accurate map listing, a page for every treatment, clean technical structure and real reviews. The difference is in how the pages are written, with the answer up top where an assistant can quote it."),
 ("How long does it take?", "The foundations go in during your first week with us, on day three. How quickly each assistant picks up the changes varies, so we won't put a date on it. We check how they describe you as we go."),
 ("Can AI answers about my practice break AHPRA rules?", "The content we write for your site follows AHPRA's advertising guidelines, so what the assistants pick up from it does too. No testimonials about clinical care and nothing that sets up unreasonable expectations."),
 ("Will you do this for my competitor?", "Not if they're a dental practice within 7km of you."),
])

def ai_search_dentists_body(R):
    crumbs = [("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("AI search for dentists", "ai-search-for-dentists.html")]
    return f"""
<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">AI search for dentists</p>
  <h1 style="margin-top:22px">When a patient asks ChatGPT for a dentist, the practice it names is the one it's <span class="u">most sure about</span>.</h1>
  <p class="lead">Getting your practice named by ChatGPT, Perplexity or Google's AI comes down to four things. Your details match everywhere. Each treatment has its own page. Those pages answer what patients ask in the first lines. And you've got a steady flow of real reviews. None of it is expensive. It's just done, or it isn't.</p>
  <p class="muted" style="margin-top:14px">We do this for more than 100 dental clinics across Australia.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#how">What we fix</a></div>
</div></section>

<section class="section tight" id="how"><div class="wrap">
  <div class="grid g3" style="margin-bottom:clamp(40px,6vw,80px)">
    <div class="stat reveal"><strong>100+</strong><span>dental clinics we manage</span></div>
    <div class="stat reveal"><strong>Day 3</strong><span>AI search foundations go in, week one</span></div>
    <div class="stat reveal"><strong>7km</strong><span>minimum gap between our dental clients</span></div>
  </div>
  <p class="eyebrow reveal" style="margin-bottom:18px">What we fix, in this order</p>
  {steps([
   ("1. Your details, matching everywhere", "If your website says one phone number and a directory says another, an assistant is less sure which is right. Less sure means less likely to name you.",
    ["We line up your practice name, address, phone, hours and treatments across your site, your Google listing and every directory you're on. It's the same job that lifts you on the map, so it pays twice."]),
   ("2. A page for every treatment", "An assistant can't recommend you for implants if your site only mentions them in a list.",
    ["Implants, Invisalign, emergency, check-ups and whatever else you want more of each get a page that says plainly what it is, who it's for and how to book. Actual treatments and actual suburbs, in plain words."]),
   ("3. The answer in the first lines", "Patients don't type \"dentist Caringbah\" into ChatGPT. They ask whether they need a crown or a filling, or whether anyone can see them today.",
    ["So we write your pages the way those questions get asked, with the answer up top. That's the part an assistant quotes. Everything is written to AHPRA's advertising guidelines, so nothing sets up expectations it shouldn't."]),
   ("4. The code underneath", "Structured data, or schema, is code on your site that spells out for machines what you do, where you are and when you're open.",
    ["Most patients will never see it. Google and the AI tools read it on every visit."]),
   ("5. Real reviews, answered", "A steady flow of genuine reviews tells Google and the AI tools that your practice is active and trusted.",
    ["We set up a simple way for patients to leave one and help you reply to them. They stay reviews, not testimonials, which keeps you inside AHPRA's rules."]),
   ("6. Checking what the assistants say", "This is the step most agencies skip.",
    ["We ask the assistants the questions your patients ask, note whether you're named and how you're described, and fix the source when they get something wrong. Then we do it again, because the answers change."]),
  ])}
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Is this separate from SEO?</p><h2 style="margin-top:18px">Straight answer: mostly the same work, written a bit differently.</h2></div>
    <div class="reveal">
      <p class="lead">An accurate map listing, a page per treatment, clean structure and real reviews help you on Google and in AI answers at the same time.</p>
      <p style="margin-top:18px">What changes is the writing. Pages need the answer up top, in the words a patient would use, so an assistant can lift it straight out. That's why AI search is part of how we do dental SEO, not an extra line on the invoice. <a class="link" href="{R}dental-seo.html">How we do dental SEO</a>.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">What happens when you're named</p><h2 style="margin-top:18px">Two or three names, and the patient rings more than one.</h2></div>
    <div class="reveal">
      <p class="lead">An assistant usually hands someone a short list. Whoever answers first tends to get the booking.</p>
      <p style="margin-top:18px">Every enquiry goes through SmileOX, our own lead platform. It replies to new enquiries in under 60 seconds, asks the questions your team would ask, and texts back the calls you miss. Getting named only matters if somebody answers. <a class="link" href="{R}smileox.html">See how SmileOX works</a>.</p>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g2">
    <div class="card reveal"><h3>What you get</h3><ul>
      <li>Your practice details matching everywhere they appear</li>
      <li>A page for each treatment, written so an assistant can quote it</li>
      <li>Schema on your site that spells out what you do and where</li>
      <li>Regular checks on how the AI assistants describe you</li>
      <li>A call every fortnight to look at the numbers together</li>
    </ul></div>
    <div class="card reveal"><h3>What we won't do</h3><ul>
      <li>Promise you'll be named. Nobody controls what an assistant says</li>
      <li>Take on another dental clinic within 7km of you</li>
      <li>Write content that breaks AHPRA's advertising rules</li>
    </ul></div>
  </div>
  <p class="muted reveal" style="margin-top:28px">Want to check where you stand first? <a class="link" href="{R}blog/ai-search-for-local-businesses.html">Here's a simple test you can run today</a>. Or read <a class="link" href="{R}ai-marketing.html">how we think about AI marketing</a> more broadly.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Straight answers</p><h2 style="margin-top:18px">Questions dentists ask about AI search.</h2></div>
    <div class="reveal">{AI_FAQ}</div>
  </div>
</div></section>
{author_section(R)}
{cta("Right now, an AI is recommending a dentist in your suburb.", "It might be you. Call us and in twenty minutes we'll show you what the assistants say about your practice, and what we'd fix first. No pitch.", R=R)}
"""

add(slug="ai-search-for-dentists.html",
    title="AI Search for Dentists | Get Named by ChatGPT and Google AI | GYA",
    desc="How to get your dental practice named when patients ask ChatGPT, Perplexity or Google's AI. Matching details, treatment pages, schema and real reviews.",
    crumbs=[("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("AI search for dentists", "ai-search-for-dentists.html")],
    nav="dental-marketing.html",
    schema=[{"@type": "Service", "name": "AI search for dentists", "provider": ORG, "serviceType": "AI search optimisation for dental practices, AI SEO for dentists", "areaServed": "AU"}, AI_FAQ_S],
    body=ai_search_dentists_body)
