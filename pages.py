CALL=f'<a class="btn" href="tel:{PHONE}"><span class="dot"></span>Call 1300 889 840</a>'

def svc_list(items):
    out='<ul class="list">'
    for title,line,more in items:
        extra="".join(f"<p>{m}</p>" for m in more)
        out+=f'<li class="reveal"><strong>{title}</strong><div><p>{line}</p>{extra}</div></li>'
    return out+"</ul>"

# ================= HOME =================
HOME_FAQ,HOME_FAQ_S=faq([
 ("Do you only work with dentists?","No. Dental is what we're known for, and we also look after around thirty other industries, from cafes and retailers to trades, gyms and professional services."),
 ("Will you take on my competitor?","Not if they're a dental practice within 7km of you."),
 ("Do you work outside Sydney?","Yes. We're Sydney based and we work Australia wide."),
 ("How soon will I see something?","Local search can move in weeks. Competitive organic terms take months. Google Ads can produce enquiries in days, which is usually why we start there."),
 ("What happens after the first week?","We call you every fortnight, look at the numbers together, and change what needs changing."),
])
pages["index.html"]=dict(
 title="Dental Marketing Agency Australia | Lead Generation, Websites, Google Ads | GYA",
 desc="GYA is the marketing agency behind 100+ dental clinics and around 30 other industries. Google Ads, local SEO, websites and our own SmileOX lead platform. Founded 2015, Sydney based, Australia-wide.",
 schema={"@context":"https://schema.org","@graph":[ORG,{"@type":"WebSite","url":SITE,"name":"Generate Your Audience"},HOME_FAQ_S]},
 body=f"""
<section class="hero hero-img">
  <div class="wrap">
    <p class="eyebrow">Marketing · Websites · Lead generation · Since 2015</p>
    <h1 style="margin-top:24px">We're not going to <span class="strike">tell you why you should hire us.</span></h1>
    <div class="hero-foot">
      <div>
        <p class="lead">Everyone does that. Instead, here's our story, everything we do, exactly what happens in your first week, and some of the sites we've built. If you get to the bottom and still want to talk, give us a call.</p>
        <div class="hero-actions">{CALL}<a class="btn ghost" href="#story">Read the story</a></div>
      </div>
      <div class="hero-meta">
        <div><strong>100+</strong><span>dental clinics we manage</span></div>
        <div><strong>30+</strong><span>other industries we look after</span></div>
        <div><strong>2015</strong><span>the year we started</span></div>
        <div><strong>7km</strong><span>minimum gap between our dental clients</span></div>
        <div><strong>$0</strong><span>of your money spent marketing us</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="story">
  <div class="wrap">
    <div class="split">
      <div class="story-side reveal">
        <p class="eyebrow">The story</p>
        <h2 style="margin:18px 0 32px">Two retail guys who started an agency at night.</h2>
        <div class="stat"><strong>$1b+</strong><span>Brett's store portfolio at Myer, NSW and ACT</span></div>
        <div class="stat"><strong>$60m+</strong><span>Rowayne's stores across NSW</span></div>
        <div class="stat"><strong>7 yrs</strong><span>since our first dental client</span></div>
      </div>
      <div class="story reveal">
        <p>We started GYA in 2015. Back then Brett and I both worked at Myer during the day and built the agency at night. Brett was General Manager looking after NSW and ACT, a store portfolio worth over a billion dollars. I was a store manager running multiple stores across NSW, a bit over 60 million between them.</p>
        <p>We took what we learnt inside one of Australia's biggest retailers, the targets, the accountability, the "why is this number down and what are we doing about it by Thursday" conversations, and used it to run a digital marketing company. That conversation is the one most agencies have quietly designed themselves out of. We kept it.</p>
        <p>We never set out to work in a niche. Before the first dentist there were cafes, retailers, tradies, gyms and professional services. Then about seven years ago we took on a dental practice, The Caringbah Dentists, run by Dr Ram. It went really well. Well enough that the practice expanded, people noticed, and the referrals kept coming.</p>
        <p>Today we manage over 100 dental clinics and around 30 other industries. Dental is what we're known for. It's not all we do.</p>

        <h3>What we don't do</h3>
        <ul>
          <li>We don't take on two dental clinics within 7km of each other, so we're never bidding against ourselves with your money.</li>
          <li>We don't give you excuses.</li>
          <li>We don't beat around the bush.</li>
          <li>We don't set unrealistic expectations, and we won't promise you page one by Friday.</li>
          <li>We don't take you on as a client if we think you're a bad fit.</li>
          <li>And we don't spend your money marketing ourselves. What you pay us goes towards your marketing, not ours.</li>
        </ul>

        <h3>What we do do</h3>
        <ul>
          <li>Work hard. Work our team hard, and keep them accountable.</li>
          <li>Find the problem, then fix it.</li>
          <li>Fill your books the ways we know how to: Google Ads, lead generation through a platform we built ourselves called SmileOX, and local SEO (the map listing), because nobody scrolls down to the organic results anymore.</li>
          <li>Get AI noticing your site, so when someone asks ChatGPT or Google's AI for a business like yours, your chances beat the one down the road.</li>
          <li>Talk to you every fortnight, so you always know where things are at.</li>
        </ul>
        <p class="big">We genuinely get anxiety when your books are empty. So we go and fix it.</p>
      </div>
    </div>
  </div>
</section>

<section class="section dark" id="services">
  <div class="wrap">
    <div class="split" style="align-items:end;margin-bottom:clamp(32px,5vw,56px)">
      <div class="reveal"><p class="eyebrow">Everything we do</p><h2 style="margin-top:18px">Nine things. All of them in house.</h2></div>
      <div class="reveal"><a class="link" href="marketing.html">See how we do all of it</a></div>
    </div>
    <div class="grid g3">
      <div class="card reveal"><h3>Google Ads</h3><p>Search, Shopping, Performance Max and YouTube, built per service and per suburb, tracked to the enquiry rather than the click.</p></div>
      <div class="card reveal"><h3>SEO and local SEO</h3><p>The map listing first, because that's where the clicks are, then the technical work and the content underneath it.</p></div>
      <div class="card reveal"><h3>Websites</h3><p>Fast, mobile first, built to rank and to convert. You own everything.</p></div>
      <div class="card reveal"><h3>Social media</h3><p>Meta, Instagram, TikTok and LinkedIn. Paid and organic, with creative shot at your business rather than pulled from a stock library.</p></div>
      <div class="card reveal"><h3>Lead generation</h3><p>SmileOX answers, qualifies and scores every enquiry, so your team only speaks to people ready to buy.</p></div>
      <div class="card reveal"><h3>Branding and design</h3><p>Identity, print, signage and ad creative, so the site and the sign out the front look like the same business.</p></div>
      <div class="card reveal"><h3>Video</h3><p>Brand films, website banners and social content, shot and edited by us.</p></div>
      <div class="card reveal"><h3>Email and SMS</h3><p>Automations, recall and reactivation.</p></div>
      <div class="card reveal"><h3>Content and copywriting</h3><p>Website copy, service pages, blogs and ad copy that sounds like a person wrote it.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="sticky reveal"><p class="eyebrow">Before you call</p><h2 style="margin-top:18px">Any of this sound familiar?</h2></div>
      <div class="reveal">
        <ul class="checks">
          <li>You're spending on Google Ads and you can't say which enquiries came from it.</li>
          <li>Your site looks fine on your laptop and takes six seconds to load on a phone.</li>
          <li>You rank well for your own business name and nowhere for the thing you actually want to sell.</li>
          <li>Enquiries come in on a Friday afternoon and get answered on Monday.</li>
          <li>Your agency sends a report every month and you've never read past the first page.</li>
          <li>Your competitor down the road is on the same agency's client list as you.</li>
        </ul>
        <p class="lead" style="margin-top:28px">If you recognised more than two of those, the call is worth twenty minutes.</p>
        <div class="hero-actions">{CALL}</div>
      </div>
    </div>
  </div>
</section>

<section class="section dark" id="monday">
  <div class="wrap">
    <div class="split">
      <div class="sticky reveal">
        <p class="eyebrow">Your first week</p>
        <h2 style="margin-top:18px">What actually happens on Monday.</h2>
        <p class="lead" style="margin-top:18px">Not a proposal. This is the sequence. We might take a breather in between, but you get the idea.</p>
      </div>
      <div class="reveal">
        <div class="plan">
          <div class="plan-row"><div class="when">Day 1<small>Breakdown</small></div><h3>Full breakdown of where you're at.</h3><p>Calls, enquiries, your Google profile, your suburb, who's outbidding you. No fluff, just the numbers.</p></div>
          <div class="plan-row"><div class="when">Day 2<small>Strategy</small></div><h3>We build your strategy.</h3><p>Which services, which suburbs, what budget, what we expect and by when.</p></div>
          <div class="plan-row"><div class="when">Day 3<small>Foundation</small></div><h3>Local SEO and AI search work in play.</h3><p>Map listing sorted, site structured so Google and the AI assistants actually understand what you do.</p></div>
          <div class="plan-row"><div class="when">Day 4<small>Demand</small></div><h3>Google Ads up and running.</h3><p>Built per service, per suburb, landing on pages that convert.</p></div>
          <div class="plan-row"><div class="when">Day 5<small>Creative</small></div><h3>Assets created for Meta ads.</h3><p>Video and stills that look like your business, not stock.</p></div>
          <div class="plan-row"><div class="when">Day 6<small>Social</small></div><h3>Meta ads running.</h3><p>Your highest value services in front of the right people in your area.</p></div>
          <div class="plan-row"><div class="when">Day 7<small>Leads</small></div><h3>SmileOX integrated. Leads coming in, triaged, contacted.</h3><p>Every enquiry answered in under a minute, nurtured, scored, and handed to your team ready to book.</p></div>
        </div>
        <p class="lead" style="margin-top:32px"><strong>Then the part that matters more than the first week.</strong> We call you every fortnight, look at the numbers together, and change what needs changing.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="sticky reveal">
        <p class="eyebrow">The formula</p>
        <h2 style="margin-top:18px">Marketing isn't rocket science.</h2>
        <p class="lead" style="margin-top:18px">Everyone says they do it differently. Even Elon Musk, with actual rocket science, fails time and time again. So we keep it simple and do it properly.</p>
      </div>
      <div class="reveal">
        <ol class="formula">
          <li><div><strong>Build a solid foundation</strong><p>Long term SEO with local SEO at the core, and future-proof your brand for AI search. This is the part that keeps working when you pause the ads.</p></div></li>
          <li><div><strong>Build a solid Google Ads strategy, then talk about it</strong><p>We catch up with you every fortnight to see if it's working. We still send reports, but we don't hide behind them. You'll always know what we're doing.</p></div></li>
          <li><div><strong>Build a lead generation machine</strong><p>SmileOX nurtures and triages every lead, then your team takes over with people who are ready to buy.</p></div></li>
        </ol>
        <div class="story"><p class="big" style="margin-top:40px">There are two ways someone finds you online. They search, or they see you. Fix those two and you're halfway there. The rest is a funnel that makes sure nothing slips through the cracks.</p></div>
        <p class="lead">If you read all of this, it's probably worth talking to us about it. Call <a class="link" href="tel:{PHONE}">1300 889 840</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section dark" id="work">
  <div class="wrap">
    <div class="split" style="align-items:end;margin-bottom:clamp(32px,5vw,64px)">
      <div class="reveal"><p class="eyebrow">Recent work</p><h2 style="margin-top:18px">Have a look at what we've built.</h2></div>
      <p class="lead reveal">Real client websites, built by us. Each one shaped around what that business actually needed to get out of it.</p>
    </div>
    {showcase()}
    <div style="margin-top:48px"><a class="link" href="work.html">See all recent work</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split" style="margin-bottom:clamp(32px,5vw,56px)">
      <div class="reveal"><p class="eyebrow">SmileOX</p><h2 style="margin-top:18px">Getting the lead is half the job. SmileOX does the other half.</h2><p class="lead" style="margin-top:18px">Our own platform. Not a reseller badge on somebody else's software.</p></div>
      <div class="reveal story">
        <p>The expensive part was never generating the enquiry. It's the next five minutes. An enquiry answered inside a minute behaves completely differently to one answered the next morning, and most businesses answer the next morning, because the phone rang while everyone was busy.</p>
        <p>SmileOX answers instantly, from any source. It asks the questions your team would ask, scores the enquiry hot, warm or cool, nurtures the ones that aren't ready, texts back the calls you missed, and hands over to a human the moment a human is needed.</p>
        <p><strong>Your team only speaks to people who are ready to book.</strong></p>
        <a class="link" href="smileox.html">See how SmileOX works</a>
      </div>
    </div>
    <div class="reveal">{BOARD}</div>
    <p class="muted" style="font-size:.8rem;margin-top:14px">Example data. We don't show real patients.</p>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <p class="eyebrow reveal" style="margin-bottom:24px">Where to next</p>
    <div class="grid g4">
      <a class="card reveal" href="dental-marketing.html"><span class="eyebrow">Dental</span><h3>Dental marketing</h3><p>Google Ads, local SEO, Meta and SmileOX, all pointed at booked patients.</p></a>
      <a class="card reveal" href="dental-websites.html"><span class="eyebrow">Dental</span><h3>Dental websites</h3><p>Fast, good looking, built to rank and to book.</p></a>
      <a class="card reveal" href="marketing.html"><span class="eyebrow">Every other industry</span><h3>Marketing for all industries</h3><p>The same retail discipline, for around thirty other industries.</p></a>
      <a class="card reveal" href="ai-marketing.html"><span class="eyebrow">What's next</span><h3>AI marketing</h3><p>What changes when people ask an AI instead of Google.</p></a>
    </div>
  </div>
</section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Questions we get asked</p><h2 style="margin-top:18px">Straight answers.</h2></div>
    <div class="reveal">{HOME_FAQ}</div>
  </div>
</div></section>
{cta()}
""")

# ================= DENTAL MARKETING =================
DM_FAQ,DM_FAQ_S=faq([
 ("How much should a dental clinic spend on marketing?","Most clinics we manage put between 3% and 8% of revenue into marketing, mostly Google Ads and SEO. We set the budget by treatment goal and how competitive your suburb is, then track every dollar to a booked appointment."),
 ("How long until dental SEO works?","You usually see map-pack movement in 6 to 10 weeks. Competitive treatment terms like \"dental implants\" take 4 to 9 months. Google Ads covers the gap from week one."),
 ("Do you work with dentists outside Sydney?","Yes. We're based in Sydney and manage clinics in every state."),
 ("Will you work with my competitor down the road?","No. We won't take on two dental clinics within 7km of each other. If there's a conflict we'll tell you on the first call."),
 ("Is this AHPRA compliant?","Yes. No testimonials in ads, no misleading claims, no before and afters without the right context. We've run dental campaigns for seven years and know the guidelines well."),
 ("Can I use my Google reviews in my advertising?","Not as testimonials about clinical care. Patients can leave them, you can respond to them, and they help your map ranking, but they can't go in your ads or get reposted as promotional content. We'll set up collection and responses without crossing that line."),
 ("Can you work with our existing website?","Yes. If it's fast enough and structured properly, we'll use it. If it isn't, we'll tell you what's holding it back before you spend anything sending traffic to it."),
 ("Do I need Google Ads if my SEO is good?","Usually yes, at least at the start. SEO takes months and only covers the searches you rank for. Ads cover the gap and show us which treatments actually convert."),
])
pages["dental-marketing.html"]=dict(
 title="Dental Marketing Agency | Google Ads, Local SEO & Lead Generation for Dentists | GYA",
 desc="Dental marketing measured in booked patients. Google Ads for dentists, local SEO, AI search, Meta ads and SmileOX lead follow-up, written to AHPRA guidelines. 100+ clinics across Australia.",
 schema={"@context":"https://schema.org","@graph":[{"@type":"Service","name":"Dental Marketing","provider":ORG,"serviceType":"Dental marketing, dental SEO, Google Ads for dentists, dental lead generation","areaServed":"AU"},DM_FAQ_S]},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Dental marketing</p>
  <h1 style="margin-top:22px">Marketing for dentists that's measured in <span class="u">booked patients</span>, not impressions.</h1>
  <p class="lead">Google Ads, local SEO, Meta and SmileOX, all wired together so no enquiry goes cold. We do this for more than 100 clinics and we've been doing it for seven years.</p>
  <p class="muted" style="margin-top:14px">Built per treatment, per suburb, and written to the AHPRA guidelines before it goes live.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#services">What's included</a></div>
</div></section>

<section class="section tight" id="services"><div class="wrap">
  <div class="grid g4" style="margin-bottom:clamp(40px,6vw,80px)">
    <div class="stat reveal"><strong>100+</strong><span>dental clinics under management</span></div>
    <div class="stat reveal"><strong>&lt;60s</strong><span>first response to a new lead via SmileOX</span></div>
    <div class="stat reveal"><strong>Fortnightly</strong><span>calls with you, not just reports</span></div>
    <div class="stat reveal"><strong>7km</strong><span>minimum gap between our dental clients</span></div>
  </div>
  <p class="eyebrow reveal" style="margin-bottom:18px">What's included</p>
  {svc_list([
   ("Google Ads for dentists","Campaigns built per treatment (implants, Invisalign, emergency, cosmetic, general) and per suburb, landing on pages that convert. Call and form tracking plus SmileOX mean we optimise to booked appointments, not clicks.",
    ["An implant patient and a checkup patient are worth completely different amounts, so they don't belong in the same campaign sharing a budget. And the traffic lands on a page about that treatment, not your homepage, which is the most expensive habit in dental advertising.",
     "Negative keyword lists do the quiet work. Dental accounts leak money on job seekers, students, DIY searches and treatments you don't offer. We build those on day one and keep maintaining them."]),
   ("Local SEO (your map listing)","Nobody scrolls past the map anymore. Google Business Profile, reviews strategy, suburb and treatment pages, schema. This is the channel that gets cheaper every year.",
    ["Your profile gets categorised properly, filled out completely, and kept alive with photos and posts. Your name, address and phone number get made identical everywhere they appear online, because inconsistency is the most common reason a good practice sits fourth in its own suburb."]),
   ("AI search visibility","Structured data and content written the way people actually ask questions, so when someone asks an AI for a dentist near them, you come up.",
    ["Patients don't type \"dentist Caringbah\" into an AI assistant. They ask whether they need a crown or a filling, what an implant costs, and whether anyone can see them today. Answering those questions plainly is what gets you cited back."]),
   ("Meta and social ads","Video-led campaigns for cosmetic, ortho and high-value treatments, retargeting, and audiences built from your real patient base.",
    ["Search catches patients who have already decided. Social creates the decision, which is why cosmetic and ortho belong there and emergency doesn't. We shoot the creative at your clinic, so the ad looks like your practice rather than a stranger's."]),
   ("Lead nurture and triage (SmileOX)","Instant SMS and email replies, 14-day nurture sequences, missed-call text-back, and scoring by treatment value so your team rings the right people first.",
    ["The enquiry that arrives at 4:50 on a Friday is often the one that decides the month. Missed-call text-back is the feature practices are most surprised by, because every clinic misses calls and most never find out what they were worth."]),
   ("Email and reactivation","Recalls, dormant patient reactivation and treatment plan follow-up. Often the cheapest appointments you'll ever book.",
    ["Unaccepted treatment plans, patients who haven't been in for two years, and recalls that went out once and were never chased are all sitting in your practice software right now."]),
   ("AHPRA-compliant copy as standard","Every ad, landing page and post is written to the advertising rules that apply to registered practitioners, before it goes live rather than after somebody complains.",
    ["No testimonials about clinical care, no claims creating unreasonable expectations, no offers without clear terms, and no use of restricted specialist titles unless you hold that registration. Seven years of dental campaigns means you shouldn't have to proofread our work for compliance."]),
   ("Reporting you'll actually read, and a call to go with it","One dashboard: leads, bookings, cost per booking, by channel. Then a fortnightly call to decide what to push next.",
    ["Cost per booked appointment is the number that matters. Impressions and reach are the numbers agencies show you when the first one isn't good."]),
  ])}
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Beyond the clinic</p><h2 style="margin-top:18px">We also market to dentists.</h2><p class="lead" style="margin-top:18px">Selling into dental is a different game. The buyer is a principal or a practice manager, the decision takes months, and there are only so many of them in the country. We run lead generation for equipment manufacturers, suppliers, labs and course providers too.</p></div>
    <div class="grid g2 reveal">
      <div class="card"><h3>Equipment and suppliers</h3><p>Product launches, dealer and clinic lead generation, LinkedIn and Google, and nurture built for long dental buying cycles.</p><p>A practice that downloads a spec sheet in March might buy in September, so the follow-up has to survive that without becoming spam.</p></div>
      <div class="card"><h3>Labs and course providers</h3><p>Clinic acquisition for labs, course fill and waitlist automation for educators.</p><p>SmileOX triages those enquiries too, so an enrolment enquiry gets the same under-a-minute reply a patient would.</p></div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Straight answers</p><h2 style="margin-top:18px">Questions dentists ask us.</h2></div>
    <div class="reveal">{DM_FAQ}</div>
  </div>
</div></section>
{cta()}
""")

# ================= DENTAL WEBSITES =================
DW_FAQ,DW_FAQ_S=faq([
 ("How long does it take?","Weeks rather than months. You get a date up front and we tell you early if anything threatens it."),
 ("Will I lose my rankings?","Not if the migration is done properly. Every old URL is redirected before launch."),
 ("Can you use our booking system?","Yes. We plug in what you already use rather than making you change software to suit a website."),
 ("We already have a site. Does it have to go?","Not necessarily. If it's fast and structured properly we'll tell you to keep it and spend the money on marketing instead."),
])
pages["dental-websites.html"]=dict(
 title="Dental Website Design Australia | Fast, Modern Dentist Websites | GYA",
 desc="Dental websites that load fast, look expensive and book patients. Video banners, online booking, treatment and suburb pages, AHPRA-aware copy and Core Web Vitals Google rewards.",
 schema={"@context":"https://schema.org","@graph":[{"@type":"Service","name":"Dental Website Design","provider":ORG,"serviceType":"Dental website design and development","areaServed":"AU"},DW_FAQ_S]},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Dental web design and development</p>
  <h1 style="margin-top:22px">Dental websites that load fast, look expensive and <span class="u">book patients</span>.</h1>
  <p class="lead">Video banners, online booking, treatment pages built for search, and Core Web Vitals that Google actually rewards.</p>
  <p class="muted" style="margin-top:14px">Below are a few of the practices we've built for, and what went into each one.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#builds">See recent builds</a></div>
</div></section>

<section class="section dark" id="builds"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:clamp(32px,5vw,64px)">
    <div class="reveal"><p class="eyebrow">Recent builds</p><h2 style="margin-top:18px">Built to load fast and book patients.</h2></div>
    <p class="lead reveal">Six practices, six different personalities, built on the same bones. Here's what went into each.</p>
  </div>
  {showcase("mid")}
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Why this matters</p><h2 style="margin-top:18px">Your website is the most expensive thing in your practice that nobody measures.</h2></div>
    <div class="story reveal">
      <p>You know what a chair costs and what your lab bill was last month. Almost no owner can tell you what their website costs them, because it never arrives as an invoice. It arrives as patients who never called.</p>
      <p>A three second load and they've tapped the next practice on the list. A booking button three taps deep and the patient who'd already decided is gone. Implants listed in eleven words on a services page, so when someone searches for implants in your suburb, Google has nothing of yours to show. And a site that looks like 2016, being read by someone about to spend fifteen thousand dollars on their mouth.</p>
      <p class="big">None of it shows up on a report. All of it shows up in your diary.</p>
    </div>
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">In every build</p><h2 style="margin-top:18px">The boring stuff, done properly.</h2><p class="lead" style="margin-top:18px">The prettiest dental site in Australia is worthless if it scores 40 on mobile and nobody can work out how to book.</p></div>
    <ul class="list reveal">
      <li><strong>Speed first</strong><p>Your site should be up and usable in under two and a half seconds, with nothing shifting around underneath a thumb that's already going to tap. Photos and video get shrunk down so they don't hold the page up. This is what decides whether the patient standing in a car park with two bars waits for you or taps the next result.</p></li>
      <li><strong>Mobile first</strong><p>We design the phone version first and scale it up. Every decision has to earn its place in a space the size of a hand, and click-to-call gets tested on a real device.</p></li>
      <li><strong>Video banners</strong><p>Clinic walk-throughs and team footage, shot at your practice. Dental fear is about the room, and a video answers it in eight seconds. We shrink the file right down and load it a moment after the rest of the page, so it looks cinematic without making anyone wait.</p></li>
      <li><strong>Booking and SmileOX</strong><p>Booking on every page, not buried on a contact page. Then every enquiry lands in SmileOX and gets answered in under a minute, day or night, instead of sitting in an inbox until Monday.</p></li>
      <li><strong>Built to rank</strong><p>A treatment in a list ranks for nothing. A page about it can rank for years and cost nothing per click. So implants, Invisalign and emergency each get one, plus the suburbs you actually draw from, with schema built in during the build.</p></li>
      <li><strong>Accessible and compliant</strong><p>Proper contrast and keyboard navigation, and every word written to the AHPRA advertising rules. Seven years of dental copy means you're not proofreading your own site for compliance.</p></li>
      <li><strong>Copy written for you</strong><p>Treatment pages, suburb pages and FAQs, in your voice. This is what stalls most website projects for six weeks. We write them, you approve them, it ships.</p></li>
    </ul>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">A fair question</p><h2 style="margin-top:18px">Can't we just use a template?</h2></div>
    <div class="story reveal">
      <p>For some businesses, yes. For a practice competing on local search, rarely. A template gives you a services page instead of treatment pages, code you don't need slowing the whole thing down, no schema and no suburb strategy, so you rank for your practice name and nothing else. None of that is visible on day one. All of it is visible when you start paying for ads to make up for a site that can't earn its own traffic.</p>
      <p>It also can't give you someone who knows dental, and knows which words get you a letter from AHPRA.</p>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <p class="eyebrow reveal" style="margin-bottom:24px">How it runs</p>
  <div class="grid g3">
    <div class="card reveal"><span class="num">01</span><h3>Discovery</h3><p>Your treatments, your suburb, your competitors, your brand. One workshop, then we write before we design, because design built around real words survives and design built around placeholder text doesn't.</p></div>
    <div class="card reveal"><span class="num">02</span><h3>Design and build</h3><p>Mobile-first design, custom build, video if you need it. You get a link to the site as we build it, so you can watch it come together and say what you want changed while it's easy to change, instead of seeing it for the first time at the end.</p></div>
    <div class="card reveal"><span class="num">03</span><h3>Launch and grow</h3><p>Every old URL mapped before launch, which is the thing that goes wrong when migrations go wrong. Analytics and SmileOX wired in from day one, then we watch it for a fortnight.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Questions we get asked</p><h2 style="margin-top:18px">Straight answers.</h2></div>
    <div class="reveal">{DW_FAQ}</div>
  </div>
</div></section>
{cta("Your next website, live in weeks.","Tell us the clinic and the suburb. You'll get a plan, an honest timeline, and a straight answer about whether you need a new site at all.")}
""")

# ================= SMILEOX =================
SX_FAQ,SX_FAQ_S=faq([
 ("Is it a bot that annoys people?","No. It replies like a person would, answers the obvious questions, and hands straight over to your team the moment a human is needed. Nobody gets trapped in a loop."),
 ("Does it replace my front desk?","No, it protects them. They stop chasing people who were only ever price shopping and spend their time on patients ready to book."),
 ("What if we already answer quickly?","Then you'll get less out of it, and we'll tell you that. Most practices think they answer quickly until they see the first week of response times on the board."),
 ("Can we use it on campaigns another agency runs?","Yes. It sits in front of whatever's producing your enquiries."),
])
pages["smileox.html"]=dict(
 title="SmileOX | Lead Nurture and Triage Platform by GYA",
 desc="SmileOX is the lead platform we built. It replies to every enquiry in under a minute, nurtures leads automatically, texts back missed calls and ranks every lead by value so your team books more.",
 schema={"@context":"https://schema.org","@graph":[{"@type":"SoftwareApplication","name":"SmileOX","applicationCategory":"BusinessApplication","operatingSystem":"Web","creator":ORG,"description":"Lead nurture and triage platform for dental clinics and enquiry-driven businesses."},SX_FAQ_S]},
 body=f"""
<section class="page-hero dark" style="padding-bottom:0"><div class="wrap">
  <p class="eyebrow">SmileOX · built by GYA</p>
  <h1 style="margin-top:22px">The lead comes in at 9:02. By 9:06 it's <span class="accent">booked</span>.</h1>
  <p class="lead">We built SmileOX because our ads were generating leads faster than front desks could answer them. It replies instantly, nurtures automatically and scores every lead by treatment value. Weekends and after hours included.</p>
  <p class="muted" style="margin-top:14px">Our own platform, not a badge on somebody else's software.</p>
  <div class="hero-actions" style="margin-bottom:clamp(48px,7vw,96px)">{CALL}</div>
  <div class="flow reveal">
    <div><span class="k"><b>01</b> Capture</span><h3>Every channel, one inbox</h3><p>Website forms, Google Ads calls, missed calls, Meta lead forms, Instagram DMs, email. Nothing sits in a spam folder at 6pm on a Friday, and nothing sits unread in somebody's personal Instagram messages over the weekend.</p></div>
    <div><span class="k"><b>02</b> Respond</span><h3>Reply in under a minute</h3><p>A text or email back on whichever channel they used, with consult times and a booking link already in it. If they rang and nobody picked up, they get a text within seconds asking how we can help, so instead of ringing the next practice on the list, they reply to you.</p></div>
    <div><span class="k"><b>03</b> Nurture</span><h3>14-day sequences by treatment</h3><p>Most people who enquire aren't ready to book today, and most practices never speak to them again. Implant enquiries get implant answers, Invisalign gets Invisalign, and the cost and payment questions get handled before anyone has to work up the nerve to ask.</p></div>
    <div><span class="k"><b>04</b> Triage</span><h3>Hot, warm, cool, by value</h3><p>Your team opens a ranked list instead of a voicemail backlog. Who's ready, what they want, what it's worth. They ring the implant consult at 9am and the check-up after lunch, which is the right way round and almost never what happens.</p></div>
  </div>
  <div style="height:clamp(48px,7vw,96px)"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:clamp(32px,5vw,56px)">
    <div class="reveal"><p class="eyebrow">What your team sees</p><h2 style="margin-top:18px">One board. Everything ranked.</h2></div>
    <div class="reveal"><p class="lead">Response times sit at the top, so nothing hides. Leads are sorted by how ready they are, so your front desk works top to bottom and stops guessing.</p><p class="muted" style="margin-top:12px">It also answers the question you've never been able to answer: of everyone who enquired last month, how many actually got booked, and which channel did they come from.</p></div>
  </div>
  <div class="reveal">{BOARD}</div>
  <p class="muted" style="font-size:.8rem;margin-top:14px">Example data. We don't show real patients.</p>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Why we built it</p><h2 style="margin-top:18px">Marketing stops at the enquiry. SmileOX doesn't.</h2></div>
    <div class="reveal story">
      <p>We manage ads for over 100 clinics. The pattern was always the same. Good campaigns, real leads, then silence. An unanswered form, a voicemail nobody returned, a "we'll call you back" that never happened. The patient booked somewhere else.</p>
      <p>It was never the front desk's fault. Someone is standing at the counter with a card, the phone is ringing, and a form has just landed in an inbox nobody has opened since Tuesday. Three things need doing and there's one person.</p>
      <p>So we built the thing that closes the gap. SmileOX sits between your marketing and your front desk, and it never takes a lunch break.</p>
      <p class="big">Think about what one enquiry is worth to you. Now think about how many came in last Friday afternoon, and when they were actually answered.</p>
      <p>That gap is the most expensive thing in most practices, and it's the cheapest one to fix.</p>
      <div class="grid g3" style="margin-top:32px">
        <div class="stat"><strong>&lt;60s</strong><span>first response</span></div>
        <div class="stat"><strong>24/7</strong><span>weekends and after hours</span></div>
        <div class="stat"><strong>Ranked</strong><span>every lead scored by value</span></div>
      </div>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <p class="eyebrow reveal" style="margin-bottom:18px">Who it's for</p>
  <ul class="list">
    <li class="reveal"><strong>For clinics</strong><p>Enquiries answered, nurtured and booked. Dormant patients reactivated. Your front desk works a ranked list instead of a voicemail backlog, and stops being the reason good leads go cold.</p></li>
    <li class="reveal"><strong>For labs, suppliers and educators</strong><p>Clinic and dealer enquiries sorted by account size, course enquiries nurtured to enrolment. Same engine, pointed at B2B, where the buying cycle is months and the follow-up has to survive it.</p></li>
    <li class="reveal"><strong>For your reporting</strong><p>Because SmileOX sees the lead and the booking, we can finally tell you cost per booked patient by channel and treatment. Not cost per click, which is the number agencies show you when the real one isn't good.</p></li>
    <li class="reveal"><strong>Included with GYA marketing</strong><p>SmileOX comes with every marketing engagement. It also runs on its own, on top of campaigns somebody else is managing, if your enquiries are already arriving and going nowhere.</p></li>
  </ul>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Questions we get asked</p><h2 style="margin-top:18px">Straight answers.</h2></div>
    <div class="reveal">{SX_FAQ}</div>
  </div>
</div></section>
{cta("Put SmileOX on your enquiries.","We'll connect your forms and phone lines, show you the first week of ranked leads, and you'll wonder how you ran without it.","Your team's morning gets a lot simpler. One list, in order of value, with the qualifying already done.")}
""")

# ================= ALL INDUSTRIES =================
def mcard(t,a,b): return f'<div class="card reveal"><h3>{t}</h3><p>{a}</p><p>{b}</p></div>'
pages["marketing.html"]=dict(
 title="Digital Marketing Agency Sydney | Google Ads, SEO, Social, Websites | GYA",
 desc="Digital marketing for around 30 industries: Google Ads, SEO and local SEO, social media, websites, lead generation, branding, video, email and copywriting. Founded 2015, Sydney based, Australia-wide.",
 schema={"@context":"https://schema.org","@type":"Service","name":"Digital Marketing","provider":ORG,"serviceType":"Digital marketing, SEO, Google Ads, social media marketing, web design, branding, video production","areaServed":"AU"},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Marketing for all industries</p>
  <h1 style="margin-top:22px">Dental is what we're known for. It's not all we do.</h1>
  <p class="lead">Before the first dentist there were cafes, retailers, tradies, gyms and professional services. We still look after about 30 industries with the same retail discipline: targets, a fortnightly call, and no excuses.</p>
  <p class="muted" style="margin-top:14px;max-width:62ch">Whatever you sell, it comes down to two things. Can people find you when they go looking, and do they see you when they're not looking yet. Everything we do sits under one of those.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="#services">Everything we do</a></div>
</div></section>

<section class="section tight" id="services"><div class="wrap">
  <div class="grid g3">
    {mcard("Google Ads","Search, Shopping, Performance Max and YouTube. Built around what you sell and where, tracked to the enquiry or the sale.","Most accounts we take over are paying for searches that were never going to buy anything. We start at the enquiry you want and work backwards to the search that produces it, then send that click to a page about the thing they searched for instead of your homepage.")}
    {mcard("SEO and local SEO","Map listing, technical health, content that answers real questions, and the AI search work most agencies haven't started yet.","Three listings and a map take most of the local clicks. The business sitting above you often isn't better than you, it just keeps its listing properly maintained. That's the cheapest position you'll ever win back.")}
    {mcard("Social media marketing","Meta, Instagram, TikTok and LinkedIn. Paid and organic, with content made for your brand, not pulled from a stock library.","Search catches people who've already decided. Social is where the deciding happens, which is why it matters most for anything expensive or considered.")}
    {mcard("Website design and development","Fast, mobile-first sites built to rank and to convert. Ecommerce, booking, lead capture, whatever your business needs.","A site has one job: load fast and get you the enquiry. Everything else is decoration. That means a page for every service you sell, because a service in a list can't rank and a page about it can.")}
    {mcard("Lead generation","SmileOX isn't only for dentists. Any business that lives on enquiries gets instant reply, nurture and triage.","The expensive part was never getting the enquiry. It's the next five minutes. Answered in under a minute, day or night, then ranked by value, so your team spends its time on the people ready to buy.")}
    {mcard("Branding and graphic design","Logos, identity, print and digital assets. The stuff that makes the ads and the site feel like the same company.","Consistency isn't vanity. It's why someone recognises you the fourth time they see you, which is usually the time they finally do something about it.")}
    {mcard("Video production","Brand films, ads, walk-throughs and social cut-downs, shot and edited by us.","Made for your brand rather than pulled off a stock site. One shoot, planned properly, gets cut into a month of content across every platform you run.")}
    {mcard("Email and SMS marketing","Automations, campaigns and reactivation. Usually the cheapest sales a business makes.","Your database is the least competitive audience you'll ever advertise to. No auction, no competitor bidding against you, and they already know who you are.")}
    {mcard("Content and copywriting","Website copy, blogs, landing pages and ad copy that sounds like a person wrote it.","Every page gets a job and a next step before a word is written. If we can't say what a page is for, we don't write it.")}
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Who it's for</p><h2 style="margin-top:18px">If you live on enquiries, we can help.</h2></div>
    <div class="reveal story">
      <p>Hospitality, retail, trades and home services, health and allied health, professional services, education, ecommerce and more. Same two problems every time, just weighted differently. A tradie lives or dies on being found. A restaurant lives or dies on being noticed. Most businesses need work on both, and the first thing we'll do is tell you which one is costing you more: being hard to find, or not being seen in the first place.</p>
      <p>The rest is the bit most agencies skip. What happens to the enquiry once it arrives, and whether anyone is honest with you about the numbers afterwards.</p>
      <p>That's the part we brought out of retail. Every account has a name against it and a target to hit, and every fortnight we sit down with you and go through what the number did and what we're changing before the next one. If a month was bad, you'll hear it from us first.</p>
      <div class="brands" style="margin-top:28px"><span>Hospitality</span><span>Retail</span><span>Trades</span><span>Allied health</span><span>Professional services</span><span>Education</span><span>Ecommerce</span></div>
    </div>
  </div>
</div></section>
{cta("We'll tell you what's not working.","Give us twenty minutes and a look at your site, your ads and your Google listing. You'll get a straight read on where the money's going, what to fix first, and whether we're the right people to do it.","No pitch. You get the read whether or not you hire us.")}
""")

# ================= AI MARKETING =================
pages["ai-marketing.html"]=dict(
 title="AI Marketing | Getting Recommended by ChatGPT and Google AI | GYA",
 desc="People are asking AI assistants instead of Google. Here's how AI search changes marketing, and what GYA is already doing so your business is the one that gets named in the answer.",
 schema={"@context":"https://schema.org","@type":"Article","headline":"People are starting to ask an AI instead of Google. Is it recommending you?","author":{"@type":"Organization","name":"Generate Your Audience"},"publisher":ORG},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">AI marketing</p>
  <h1 style="margin-top:22px">People are starting to ask an AI instead of Google. <span class="u">Is it recommending you?</span></h1>
  <p class="lead">Search is changing faster than most agencies will admit. Here's how we see it, what it means for you, and what we're already doing about it.</p>
  <p class="muted" style="margin-top:14px;max-width:62ch">Open ChatGPT and ask it for the best business in your suburb doing what you do. Someone gets named. If it isn't you, that's a decision being made about your business, in a room you're not in.</p>
  <div class="hero-actions">{CALL}</div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Why this matters</p><h2 style="margin-top:18px">Getting left out of the answer is invisible. That's what makes it expensive.</h2></div>
    <div class="story reveal">
      <p>When you slip off page one you can see it happen. Traffic drops, rankings move, somebody notices and says something. When an AI quietly stops naming you, nothing happens at all. No alert, no line on a report, and no customer ringing to tell you they went with the business the assistant suggested instead.</p>
      <p class="big">You just get fewer enquiries, and no explanation for them.</p>
      <p>The businesses being named aren't necessarily better than you. They're easier for a machine to be confident about. Their details match everywhere they appear, their pages answer the questions people actually ask, and their site says plainly what they do and where they do it. Almost none of that is expensive. It's just done, or it isn't.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">What's changing</p><h2 style="margin-top:18px">Three shifts, already happening.</h2></div>
    <div class="reveal">
      <ul class="list">
        <li><strong>AI answers are replacing result pages</strong><div><p>Google's AI Overviews, ChatGPT and Perplexity answer "who does dental implants near me", "best physio in Cronulla" or "electrician open today" with a short list and a recommendation. Being on page one isn't enough anymore. You need to be in the answer. That takes structured data, consistent business info everywhere, real reviews, and content that answers questions the way people actually ask them.</p><p>There used to be ten results on a page and you could win work from any of them. Now there's often one answer with two or three businesses named in it. You're either one of those names or you may as well not be on the page.</p></div></li>
        <li><strong>Follow-up is getting automated, and personal</strong><div><p>The businesses winning right now aren't spending more on ads. They're answering faster and saying something relevant. AI-driven nurture, the kind SmileOX runs, makes a two-person business feel like it has a ten-person front desk.</p><p>Being quick to answer used to be a nice touch. Now it's often the whole difference between the enquiry being yours and it being someone else's.</p></div></li>
        <li><strong>Making ads got easy. Knowing which ones to run didn't</strong><div><p>Anyone can produce fifty versions of an ad in an afternoon now. That was never the hard part.</p><p>The hard part is picking which suburb to run them in, which offer to lead with and which service to push this month, then switching off the ones that aren't working before they eat your budget. The tools got cheap. The judgement didn't, and the judgement is what you're actually paying an agency for.</p><p>Ours comes from seven years in dental and about 30 other industries.</p></div></li>
      </ul>
    </div>
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split" style="margin-bottom:clamp(32px,5vw,56px)">
    <div class="reveal"><p class="eyebrow">What we do about it</p><h2 style="margin-top:18px">AI-ready marketing.</h2></div>
    <p class="lead reveal">Practical, not theoretical. Everything below is running for our clients today.</p>
  </div>
  <div class="grid g3">
    <div class="card reveal"><h3>Getting you into the answer</h3><p>Consistent business data everywhere you're listed, code on your site that spells out what you do and where you do it, and content written the way customers actually ask the question. Then we watch how the assistants describe you, and fix it when they get it wrong.</p></div>
    <div class="card reveal"><h3>AI lead response</h3><p>SmileOX replies, qualifies and nurtures on the customer's channel in seconds. Hot leads get flagged for a human call, so nobody sits in an automated loop when they were ready to book.</p></div>
    <div class="card reveal"><h3>Budget that moves</h3><p>Spend shifts toward the service and suburb combinations producing enquiries this month, not last quarter's plan. Most accounts are still running a budget somebody set in January.</p></div>
    <div class="card reveal"><h3>Ads tested, not guessed</h3><p>We run several versions of an ad against each other rather than betting on one. Whichever is producing enquiries keeps the budget, and the rest get switched off within days, before they've wasted anything worth arguing about.</p></div>
    <div class="card reveal"><h3>Winning back the customers you already have</h3><p>We go through your database, work out who's likely due for something and what that something is, then contact them with a message that suits. No auction, nobody bidding against you, and they already know who you are. It's the cheapest sale you'll ever make and the one most businesses never go after.</p></div>
    <div class="card reveal"><h3>Reports in plain English</h3><p>A monthly summary that reads like a note from a person, not a spreadsheet export. Plus the fortnightly call, where we tell you what's not working before you have to ask.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Our view</p><h2 style="margin-top:18px">Who wins the next five years.</h2></div>
    <div class="reveal story"><p>Three things decide it. Whether your data is clean enough for a machine to recommend you. Whether your follow-up is fast enough to beat the competitor down the road. And whether your agency treats AI as a tool rather than a headline.</p><p>We plan to be that agency, and to keep telling you exactly what's working and what isn't.</p></div>
  </div>
</div></section>
{cta("Right now, an AI is recommending someone in your area.","It might be you. It might be the place up the road that isn't half the business you are, but whose website is easier for a machine to read.","Twenty minutes and we'll show you which, and what it takes to be the name that comes up.")}
""")

# ================= WORK =================
pages["work.html"]=dict(
 title="Recent Work | Dental Websites, Branding and Video | GYA",
 desc="Recent websites built by GYA: Footscray Dental Studio, My Dentist Alderley, Tooth n Care East Maitland, Horizon Dental, New'Gen Dental Surgery and Artarmon Dentists, and why each was built the way it was.",
 schema={"@context":"https://schema.org","@type":"CollectionPage","name":"Recent work","isPartOf":{"@type":"WebSite","url":SITE}},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Recent work</p>
  <h1 style="margin-top:22px">Some of what we've built.</h1>
  <p class="lead">A look at recent websites, branding and video. Each one below says what it was built to do, and why it was built that way.</p>
  <p class="muted" style="margin-top:14px;max-width:62ch">A portfolio shows you what something looks like. It doesn't show you why it was built that way, which is the part that decides whether it works.</p>
</div></section>

<section class="section dark"><div class="wrap">
  {work_rows()}
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">What they share</p><h2 style="margin-top:18px">Different businesses. Same spine.</h2></div>
    <div class="story reveal">
      <p>These are six different personalities and six different budgets, but the bones underneath are the same.</p>
      <p>A page for every service, because a service in a list can't rank and a page about it can. An enquiry route on every screen. Video and images shrunk down and loaded a moment after the rest of the page, so it looks good without making anyone wait. And a build light enough to hold up on a phone with two bars of reception, which is how a lot of people will meet the business for the first time.</p>
      <p>None of it is the sort of thing you notice at a glance. All of it is the reason these sites keep working long after launch.</p>
    </div>
  </div>
</div></section>
{cta("Want a site like these?","Tell us about your business. You'll get a plan, a timeline and a couple of directions.")}
""")

# ================= ABOUT =================
pages["about.html"]=dict(
 title="About GYA | Rowayne and Brett, Founders of Generate Your Audience",
 desc="Meet Rowayne and Brett, the founders of Generate Your Audience, and the 40+ team behind them. Two ex-Myer managers who started an agency at night in 2015 and now manage 100+ dental clinics plus 30 other industries.",
 schema={"@context":"https://schema.org","@type":"AboutPage","mainEntity":ORG},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">About</p>
  <h1 style="margin-top:22px">Two founders, 40+ team members, and a very full calendar.</h1>
  <p class="lead">We started GYA in 2015 while still running stores for Myer. Brett had NSW and ACT, over a billion dollars of retail. Rowayne had multiple stores across NSW. We brought that discipline to marketing and never really switched it off.</p>
  <p class="muted" style="margin-top:14px;max-width:62ch">Retail teaches you one thing better than any marketing course. You can't argue with a day's takings. The number is the number, and somebody has to say out loud what they're doing about it before the week is out. That's the meeting most agencies have quietly designed themselves out of.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="team">
    <div class="person reveal">
      <div class="pic"><img src="assets/rowayne.jpg" alt="Rowayne, founder of Generate Your Audience" width="600" height="750" loading="lazy"></div>
      <h3>Rowayne</h3><p class="role">Founder · Strategy</p>
      <p>Ran multiple Myer stores across NSW, a bit over 60 million between them. Sets the strategy on every account: which services, which suburbs, what the budget goes on and what it should be returning by when.</p>
    </div>
    <div class="person brett reveal">
      <div class="pic"><img src="assets/brett.jpg" alt="Brett, co-founder of Generate Your Audience" width="600" height="750" loading="lazy"></div>
      <h3>Brett</h3><p class="role">Co-founder · Client success</p>
      <p>General Manager at Myer looking after NSW and ACT, a store portfolio worth over a billion dollars. Runs client success here, which mostly means making sure the fortnightly calls actually happen and that nobody is being quietly managed by a monthly report.</p>
    </div>
  </div>
  <div class="split" style="margin-top:clamp(48px,7vw,96px)">
    <div class="reveal"><p class="eyebrow">The team</p><h2 style="margin-top:18px">Over 40 of us, and they become part of your family too.</h2></div>
    <div class="reveal story">
      <p>Behind Rowayne and Brett there's a team of more than 40: ads specialists, SEO, designers, developers, video, copywriters, and the account managers who'll be on your fortnightly call. You're not handed off to a junior after you sign. The people who build your plan are the people who run it, and most of our clients end up knowing them by name.</p>
      <p>That matters more than it sounds. The usual agency pattern is that you're sold by the person you like and then handed to somebody you've never met, who inherits an account they didn't build and a plan they don't agree with. Everything after that is slower and worse, and you never quite know why.</p>
      <p>Everything is done in house. No white labelling, no reselling somebody else's platform, no work quietly sent elsewhere and marked up.</p>
      <div class="grid g3" style="margin-top:32px">
        <div class="stat"><strong>40+</strong><span>team members across GYA</span></div>
        <div class="stat"><strong>2</strong><span>founders who still pick up the phone</span></div>
        <div class="stat"><strong>1</strong><span>account manager who knows your business</span></div>
      </div>
    </div>
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Where it started</p><h2 style="margin-top:18px">The Caringbah Dentists.</h2></div>
    <div class="reveal story"><p>About seven years ago Dr Ram took a punt on two retail guys running an agency at night. His practice grew, people noticed, and the referrals haven't really stopped since.</p><p class="big">Over 100 clinics later, nothing about the method has changed. Look at the numbers. Find the problem. Fix it. Call the client.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">How we work</p><h2 style="margin-top:18px">Things we believe that other agencies find inconvenient.</h2></div>
    <ul class="list reveal">
      <li><strong>Booked patients are the only metric</strong><p>Impressions, reach and brand lift are lovely. Your books being full is the job. Every other number is something to look at on the way to that one, not instead of it.</p></li>
      <li><strong>Speed beats spend</strong><p>The business that answers first usually wins. That's why we built SmileOX before we built a sales deck. Most agencies would rather sell you more budget than fix the five minutes after an enquiry arrives, because more budget is easier to invoice.</p></li>
      <li><strong>7km</strong><p>We won't take on two dental clinics within 7km of each other. Ever. Which means we're never building your campaign and your competitor's with the same hands, and never bidding against ourselves with your money. Ask any other agency how many of your competitors they also work for.</p></li>
      <li><strong>Say what isn't working</strong><p>You'll hear it from us first, with the fix. Every fortnight. A bad month is a conversation, not something you find on page four of a report nobody expected you to read.</p></li>
      <li><strong>Your money goes on your marketing</strong><p>We don't spend your money marketing ourselves. What you pay us goes on your campaigns, not on ours.</p></li>
    </ul>
  </div>
</div></section>
{cta("Say hello.","We pick up the phone.","Twenty minutes, no deck. We'll look at what you're spending, where it's going, and what your site and your Google listing are doing, then tell you which of them is costing you the most right now.")}
""")

# ================= CONTACT =================
pages["contact.html"]=dict(
 title="Contact GYA | Call 1300 889 840",
 desc="Call us on 1300 889 840 or send a note. Twenty minutes, no deck, no pitch, and you'll know what we'd change first. We call back within one business day.",
 schema={"@context":"https://schema.org","@type":"ContactPage","mainEntity":ORG},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1 style="margin-top:22px">Just call us. 1300 889 840.</h1>
  <p class="lead">We pick up. If it's late or you'd rather type, send a note below and we'll call you back within one business day.</p>
  <p class="muted" style="margin-top:14px">One call, twenty minutes, and you'll know what we'd change first.</p>
  <div class="hero-actions">{CALL}<a class="btn ghost" href="mailto:hello@generateyouraudience.com">Email instead</a></div>
</div></section>
<section class="section tight"><div class="wrap">
  <div class="split">
    <div class="sticky reveal">
      <h3>What happens next</h3>
      <ul class="list" style="margin-top:16px">
        <li><strong>1 day</strong><p>We call you back.</p></li>
        <li><strong>20 min</strong><p>A chat about your business, your area and your competitors. No deck, no pitch, and no obligation at the end of it.</p></li>
        <li><strong>A plan</strong><p>Your first week, in writing, so there's no argument in three months about what was said in the first twenty minutes.</p></li>
      </ul>
    </div>
    <div class="reveal">{form("p")}</div>
  </div>
</div></section>
""")
