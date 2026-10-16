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
