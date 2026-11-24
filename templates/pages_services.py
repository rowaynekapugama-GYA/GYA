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

# ================= IMPLANT CLINIC MARKETING =================
IMPLANT_FAQ, IMPLANT_FAQ_S = faq([
 ("How is marketing an implant clinic different from general dental marketing?", "An implant patient is worth far more than a check-up patient and takes far longer to decide. So implants get their own pages, their own Google Ads campaign and budget, and follow-up that keeps going for weeks instead of one reply and done."),
 ("How long does it take to rank for \"dental implants\"?", "It's one of the most competitive terms in dentistry. It usually takes 4 to 9 months. Google Ads can bring in implant enquiries within days, so most clinics run ads while the SEO builds."),
 ("Should implant ads share a budget with our other ads?", "No. If implants and check-ups share a campaign, the cheaper, more common searches quietly use up the money meant for implants. Implants get a campaign and a budget of their own."),
 ("Can we call ourselves implant specialists?", "Only if the practitioner holds a specialist registration that allows it. Specialist titles are restricted under AHPRA's rules. If you're a dentist who places implants, we'll say exactly that, and lead with your training and experience instead."),
 ("Can we advertise a price or a payment plan for implants?", "Only with clear terms. AHPRA's rules don't allow offers without them, so anything about price or payments says exactly what's included and who it applies to before it goes anywhere near an ad."),
 ("Will you work with another implant clinic near us?", "Not if they're a dental practice within 7km of you."),
])

def implant_clinic_marketing_body(R):
    crumbs = [("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("Implant clinic marketing", "implant-clinic-marketing.html")]
    return f"""
<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">Implant clinic marketing</p>
  <h1 style="margin-top:22px">Implant marketing for patients who ask about cost first and book <span class="u">weeks later</span>.</h1>
  <p class="lead">An implant enquiry is a big one, for you and for them. They'll want to know what it costs, who's doing it, and whether it'll work for them, and most won't book on the day they ask. So we give implants their own pages, their own ad budget and their own follow-up, put the practitioner's training up front, and keep the conversation going until they're ready for a consult.</p>
  <p class="muted" style="margin-top:14px">We manage marketing for more than 100 dental clinics across Australia.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#how">How we do it</a></div>
</div></section>

<section class="section tight" id="how"><div class="wrap">
  <div class="grid g3" style="margin-bottom:clamp(40px,6vw,80px)">
    <div class="stat reveal"><strong>100+</strong><span>dental clinics we manage</span></div>
    <div class="stat reveal"><strong>4 to 9 months</strong><span>to rank for "dental implants", usually</span></div>
    <div class="stat reveal"><strong>14 days</strong><span>of follow-up for enquiries not ready yet</span></div>
  </div>
  <p class="eyebrow reveal" style="margin-bottom:18px">How we market implants</p>
  {steps([
   ("1. Implants get their own budget", "This is the one we see go wrong most. Implants sit in the same campaign as check-ups and cleans, and the cheaper searches eat the money.",
    [f"Implants get a Google Ads campaign of their own, with their own budget and their own suburbs, and negative keyword lists from day one so the money isn't spent on people looking for courses, jobs or overseas trips. <a class=\"link\" href=\"{R}dental-google-ads.html\">How we run dental Google Ads</a>."]),
   ("2. A page for each kind of implant search", "\"Single tooth implant\", \"full arch implants\" and \"implants or dentures\" are different people with different questions.",
    ["Each one gets a page that answers what they're actually worried about: what's involved, roughly how long it takes from first visit to finished, how payment works at your practice, and how to book a consult. Every ad click lands on the page about the thing they searched for."]),
   ("3. The practitioner up front", "Someone choosing who puts an implant in their jaw wants to know who that person is.",
    ["So the practitioner's training, experience and team sit at the top of the page and in the ads, with real photos taken at your practice. If someone holds a specialist registration, we lead with it. If not, we describe exactly what they do, and the specialist title stays out of it."]),
   ("4. SEO for the long game", "\"Dental implants\" is one of the hardest terms to rank for in dentistry, and it usually takes 4 to 9 months.",
    [f"We start the treatment pages, map listing and technical work in week one so the ads can ease off as the organic rankings come in. <a class=\"link\" href=\"{R}dental-seo.html\">How we do dental SEO</a>."]),
   ("5. Follow-up as long as the decision", "Most implant enquiries are a question, not a booking.",
    [f"SmileOX, our own lead platform, replies to every enquiry in under 60 seconds, asks the questions your team would ask, and scores it hot, warm or cool. The hot ones go straight to your team. The rest get 14 days of follow-up that answers cost and process questions, so nobody slips away just because they weren't ready on a Tuesday. <a class=\"link\" href=\"{R}smileox.html\">See how SmileOX works</a>."]),
   ("6. Checked against AHPRA's rules", "Results, prices and reviews are where implant advertising most often gets into trouble.",
    ["Every ad and page is checked against the AHPRA advertising guidelines before it goes live: no testimonials about clinical care, nothing that sets up unreasonable expectations about the result, and no price or payment offers without clear terms."]),
  ])}
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Why it's a different job</p><h2 style="margin-top:18px">One implant patient isn't one check-up patient.</h2></div>
    <div class="reveal">
      <p class="lead">A check-up is booked in a minute. An implant is a decision about money, time and their own mouth, and it can sit with someone for weeks before they ring.</p>
      <p style="margin-top:18px">That changes how you judge the marketing. An implant campaign can look slow on clicks and still be your best spend, because the number that matters is consults booked and treatment going ahead, not this week's enquiries. That's what we report on, and what we talk through on our call every fortnight. <a class="link" href="{R}dental-marketing.html">See everything we do for dentists</a>.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">After the consult</p><h2 style="margin-top:18px">The patient who said "let me think about it".</h2></div>
    <div class="reveal">
      <p class="lead">Plenty of implant patients come in, hear the plan, and go home to think. Some of them never hear from the practice again.</p>
      <p style="margin-top:18px">We set the follow-up up so those people get a friendly nudge and a chance to ask the questions they didn't ask in the chair, and your team knows who's warming up. It's often the cheapest booking a practice can get, because they've already found you, met you and been through the consult.</p>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g2">
    <div class="card reveal"><h3>What you get</h3><ul>
      <li>An implant campaign with its own budget and suburbs</li>
      <li>Pages for the implant searches your patients actually make</li>
      <li>Every enquiry answered fast and followed up if they're not ready</li>
      <li>Reporting on booked consults, and a call every fortnight</li>
    </ul></div>
    <div class="card reveal"><h3>What we won't do</h3><ul>
      <li>Take on another dental practice within 7km of you</li>
      <li>Use a specialist title for anyone who isn't registered for it</li>
      <li>Promise results, or run price offers without clear terms</li>
      <li>Report clicks and call it a result</li>
    </ul></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Straight answers</p><h2 style="margin-top:18px">Questions implant clinics ask about marketing.</h2></div>
    <div class="reveal">{IMPLANT_FAQ}</div>
  </div>
</div></section>
{author_section(R)}
{cta("Empty chairs give us anxiety. Genuinely.", "If you're getting implant enquiries but not enough of them turn into consults, call us. Twenty minutes, no pitch, just a look at where they're dropping off and what we'd do about it.", R=R)}
"""

add(slug="implant-clinic-marketing.html",
    title="Dental Implant Marketing | Implant Clinic Marketing Agency | GYA",
    desc="Marketing for implant clinics: implants get their own pages, ad budget and follow-up, the practitioner leads, and every enquiry is chased until it books.",
    crumbs=[("Home", "index.html"), ("Dental marketing", "dental-marketing.html"), ("Implant clinic marketing", "implant-clinic-marketing.html")],
    nav="dental-marketing.html",
    schema=[{"@type": "Service", "name": "Implant clinic marketing", "provider": ORG, "serviceType": "Dental implant marketing, implant clinic marketing", "areaServed": "AU"}, IMPLANT_FAQ_S],
    body=implant_clinic_marketing_body)
