import os, json
SITE="https://www.generateyouraudience.com"
OUT=os.path.dirname(os.path.abspath(__file__))

NAV=[("index.html","Home"),("dental-marketing.html","Dental Marketing"),("dental-websites.html","Dental Websites"),
     ("smileox.html","Smileox"),("ai-marketing.html","AI Marketing"),("work.html","Work"),("about.html","About")]

def head(title,desc,slug,schema=None):
    s=json.dumps(schema) if schema else ""
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if slug=='index.html' else slug}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0a0a0a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Generate Your Audience">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{'' if slug=='index.html' else slug}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Inter+Tight:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Inter+Tight:wght@400;500;600&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Inter+Tight:wght@400;500;600&display=swap"></noscript>
<link rel="stylesheet" href="css/style.css">
{'<script type="application/ld+json">'+s+'</script>' if s else ''}
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
<header class="header">
  <div class="wrap nav">
    <a class="logo" href="index.html" aria-label="Generate Your Audience home"><img src="assets/gya-logo.png" alt="GYA — Generate Your Audience" width="240" height="60" fetchpriority="high"></a>
    <nav class="menu" aria-label="Primary">
      {''.join(f'<a href="{h}">{l}</a>' for h,l in NAV[1:])}
    </nav>
    <div class="nav-cta">
      <a class="btn" href="contact.html"><span class="dot"></span>Fill my books</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  {''.join(f'<a class="item" href="{h}">{l}<small>0{i+1}</small></a>' for i,(h,l) in enumerate(NAV))}
  <div class="mm-foot">
    <a class="btn" href="contact.html"><span class="dot"></span>Fill my books</a>
    <span class="muted" style="font-size:.9rem">Sydney · Working with clinics Australia-wide</span>
  </div>
</div>
<main id="main">
"""

FOOT=f"""
</main>
<footer class="footer dark">
  <div class="wrap">
    <div class="top">
      <div>
        <div class="wordmark">g<b>y</b>a</div>
        <p class="muted" style="margin-top:16px;max-width:34ch">Generate Your Audience. Lead generation, websites and AI marketing for the dental industry. Built in Sydney, working Australia-wide.</p>
      </div>
      <div><h4>Services</h4><ul>
        <li><a href="dental-marketing.html">Dental marketing</a></li>
        <li><a href="dental-websites.html">Dental websites</a></li>
        <li><a href="smileox.html">Smileox lead platform</a></li>
        <li><a href="ai-marketing.html">AI marketing</a></li></ul></div>
      <div><h4>Studio</h4><ul>
        <li><a href="work.html">Recent work</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Talk to us</h4><ul>
        <li><a href="mailto:hello@generateyouraudience.com">hello@generateyouraudience.com</a></li>
        <li><a href="contact.html">Book a 20-minute call</a></li></ul></div>
    </div>
    <div class="bottom">
      <span>© 2026 Generate Your Audience Pty Ltd</span>
      <span>Dental marketing · Sydney · Melbourne · Brisbane · Perth · Adelaide</span>
    </div>
  </div>
</footer>
<script src="js/main.js" defer></script>
</body>
</html>
"""

def cta(title="Let's fill your books.",sub="A 20-minute call. We'll look at your numbers, your suburb and your competitors — and tell you what we'd do first."):
    return f"""
<section class="section tight">
  <div class="wrap">
    <div class="cta-band dark reveal">
      <div><h2>{title}</h2><p class="lead" style="margin-top:16px">{sub}</p></div>
      <div class="actions"><a class="btn light" href="contact.html">Book a call</a><a class="btn ghost-light" href="work.html">See the work</a></div>
    </div>
  </div>
</section>"""

SITES=[
 ("https://lava-street-dental.vercel.app","lava-street-dental.vercel.app","Lava Street Dental","Brand · Website · Video banner"),
 ("https://horizon.gya.net.au","horizon.gya.net.au","Horizon Dental","Website · Booking flow · Video banner"),
 ("https://www.artarmondentists.com","artarmondentists.com","Artarmon Dentists","Website · Local SEO · Video banner"),
 ("https://www.greystreetdentist.com.au","greystreetdentist.com.au","Grey Street Dentist","Website · Google Ads landing · Video banner"),
]
def work_grid(limit=None):
    items=SITES[:limit] if limit else SITES
    out='<div class="work-grid">'
    for url,host,name,tags in items:
        out+=f"""
<article class="site reveal">
  <div class="frame">
    <div class="frame-bar"><i></i><i></i><i></i><span class="url">{host}</span><span class="live">Live</span></div>
    <div class="screen" data-src="{url}" data-title="{name} website preview">
      <div class="skeleton"></div>
      <div class="overlay"><a class="btn light" href="{url}" target="_blank" rel="noopener">Open live site ↗</a></div>
    </div>
  </div>
  <div class="site-meta"><h3><a href="{url}" target="_blank" rel="noopener">{name}</a></h3><span class="tags">{tags}</span></div>
</article>"""
    return out+"</div>"

ORG={"@context":"https://schema.org","@type":"ProfessionalService","name":"Generate Your Audience","alternateName":"GYA",
 "url":SITE,"logo":SITE+"/assets/gya-logo.png","image":SITE+"/assets/og-image.jpg",
 "description":"Dental marketing agency and lead generation platform. Websites, Google Ads, SEO, AI marketing and the Smileox lead nurture platform for dental clinics, labs, equipment suppliers and course providers.",
 "areaServed":"AU","address":{"@type":"PostalAddress","addressLocality":"Sydney","addressRegion":"NSW","addressCountry":"AU"},
 "knowsAbout":["Dental marketing","Dental SEO","Dental website design","Dental lead generation","Google Ads for dentists","AI marketing"],
 "sameAs":[]}

pages={}

# ---------------- HOME ----------------
pages["index.html"]=dict(
 title="Dental Marketing Agency Australia | Lead Generation for Dentists — GYA",
 desc="GYA is the dental marketing agency behind 100+ clinics, labs, equipment suppliers and course providers. Websites, Google Ads, SEO, AI marketing and the Smileox lead platform. We fill your books.",
 schema={"@context":"https://schema.org","@graph":[ORG,{"@type":"WebSite","url":SITE,"name":"Generate Your Audience"}]},
 body=f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Dental marketing · Lead generation · Sydney, Australia-wide</p>
    <h1 style="margin-top:24px">We're not going to <span class="strike">tell you why you should hire us.</span></h1>
    <div class="hero-foot">
      <div>
        <p class="lead">Every agency does that. Instead, here's what we'd do in your first 30 days, the sites we shipped this quarter playing live, and the platform that turns enquiries into booked patients.</p>
        <div class="hero-actions"><a class="btn" href="#monday"><span class="dot"></span>Show me the first 30 days</a><a class="btn ghost" href="work.html">Watch the sites</a></div>
      </div>
      <div class="hero-meta">
        <div><strong>100+</strong><span>dental clinics managed</span></div>
        <div><strong>1</strong><span>industry. Only dental.</span></div>
        <div><strong>Smileox</strong><span>our lead nurture &amp; triage platform</span></div>
        <div><strong>Books</strong><span>filled, not just "brand awareness"</span></div>
      </div>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true"><div class="ticker-track">
  <span>Dental clinics</span><span>Dental labs</span><span>Equipment manufacturers</span><span>Equipment suppliers</span><span>Dental course providers</span><span>Vatic</span><span>MDS by Henry Schein</span>
  <span>Dental clinics</span><span>Dental labs</span><span>Equipment manufacturers</span><span>Equipment suppliers</span><span>Dental course providers</span><span>Vatic</span><span>MDS by Henry Schein</span>
</div></div>

<section class="section" id="monday">
  <div class="wrap">
    <div class="split">
      <div class="sticky reveal">
        <p class="eyebrow">Your first 30 days</p>
        <h2 style="margin-top:18px">What actually happens on Monday.</h2>
        <p class="lead" style="margin-top:18px">Not a proposal. A plan. This is the sequence we run for every clinic that joins — it's why the books fill.</p>
        <a class="link" href="contact.html" style="margin-top:24px">Start the clock</a>
      </div>
      <div class="plan reveal">
        <div class="plan-row"><div class="when">Day 1<small>Audit</small></div><h3>We read your numbers, not your brief.</h3><p>Call volume, booking conversion, Google Business Profile, suburb demand, who's outbidding you on Ads. You'll get a one-page truth sheet.</p></div>
        <div class="plan-row"><div class="when">Day 3<small>Plumbing</small></div><h3>Smileox goes live on your enquiries.</h3><p>Every form, call and DM flows into one place. Leads get answered in minutes, nurtured automatically and triaged by treatment value before your front desk touches them.</p></div>
        <div class="plan-row"><div class="when">Day 7<small>Demand</small></div><h3>Google Ads built around the treatments you want more of.</h3><p>Implants, Invisalign, emergency, cosmetic — campaigns per treatment, per suburb, landing on pages that convert. Spend is tracked to the booked appointment, not the click.</p></div>
        <div class="plan-row"><div class="when">Day 14<small>Foundation</small></div><h3>Local SEO that compounds.</h3><p>Profile optimisation, treatment pages, suburb pages, schema, Core Web Vitals in the green. The work that makes next year cheaper than this year.</p></div>
        <div class="plan-row"><div class="when">Day 30<small>Proof</small></div><h3>You see booked patients, by source, by treatment.</h3><p>One dashboard. What came in, what it cost, what it was worth. Then we do it again — better.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="split" style="align-items:end;margin-bottom:clamp(32px,5vw,64px)">
      <div class="reveal"><p class="eyebrow">Recent work · playing live</p><h2 style="margin-top:18px">Don't read about the sites. Watch them.</h2></div>
      <p class="lead reveal">These are real, live clinic websites — video banners and all — streaming in from the web right now. Hover to look around, open one in a tab.</p>
    </div>
    {work_grid(4)}
    <div style="margin-top:40px"><a class="link" href="work.html">All recent work</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid g3">
      <a class="card reveal" href="dental-marketing.html"><span class="eyebrow">Service</span><h3>Dental marketing</h3><p>Google Ads, local SEO, Meta, email and the Smileox follow-up engine. One team, one goal: booked patients.</p><span class="link" style="margin-top:20px">Explore</span></a>
      <a class="card reveal" href="dental-websites.html"><span class="eyebrow">Service</span><h3>Dental websites</h3><p>Fast, beautiful, conversion-built sites with video banners, online booking and Core Web Vitals that Google rewards.</p><span class="link" style="margin-top:20px">Explore</span></a>
      <a class="card reveal" href="ai-marketing.html"><span class="eyebrow">Service</span><h3>AI marketing</h3><p>How AI search, AI agents and automated follow-up change the way patients find a dentist — and what we're building for it.</p><span class="link" style="margin-top:20px">Explore</span></a>
    </div>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="split">
      <div class="reveal"><p class="eyebrow">Who we work with</p><h2 style="margin-top:18px">Clinics, and the companies that supply them.</h2></div>
      <div class="reveal">
        <p class="lead">We manage marketing for over 100 dental clinics, plus the equipment manufacturers, labs, suppliers and course providers that sell to dentists. We know the industry from both sides of the chair.</p>
        <div class="brands" style="margin-top:28px"><span>Vatic</span><span>MDS by Henry Schein</span><span>100+ clinics</span><span>Dental labs</span><span>Course providers</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Smileox</p>
        <h2 style="margin-top:18px">Getting the lead is half the job. Smileox does the other half.</h2>
        <p class="lead" style="margin-top:18px">Our own platform. It answers, nurtures and triages every enquiry so your front desk only talks to people ready to book.</p>
        <a class="btn light" href="smileox.html" style="margin-top:26px">See how Smileox works</a>
      </div>
      <div class="triage reveal" aria-label="Example of Smileox lead triage">
        <div class="row"><span class="t">09:02</span><span>New enquiry · implants · Parramatta · via Google Ads</span><span class="hot">HOT</span></div>
        <div class="row"><span class="t">09:02</span><span>Auto-reply sent · consult options offered · SMS + email</span><span class="cool">AUTO</span></div>
        <div class="row"><span class="t">09:06</span><span>Patient replied "Thursday works" · booking link sent</span><span class="hot">BOOKED</span></div>
        <div class="row"><span class="t">09:41</span><span>New enquiry · whitening · via website form</span><span class="warm">WARM</span></div>
        <div class="row"><span class="t">09:41</span><span>Nurture sequence started · day 0 of 14</span><span class="cool">AUTO</span></div>
        <div class="row"><span class="t">11:15</span><span>Missed call · unknown · voicemail transcribed · "check-up?"</span><span class="warm">WARM</span></div>
        <div class="row"><span class="t">11:16</span><span>Text-back sent within 60 seconds</span><span class="cool">AUTO</span></div>
      </div>
    </div>
  </div>
</section>
{cta()}
""")

# ---------------- DENTAL MARKETING ----------------
pages["dental-marketing.html"]=dict(
 title="Dental Marketing Agency | Google Ads, SEO & Lead Generation for Dentists — GYA",
 desc="Dental marketing that fills books: Google Ads for dentists, dental SEO, local SEO, Meta ads and automated lead follow-up through Smileox. Trusted by 100+ dental clinics across Australia.",
 schema={"@context":"https://schema.org","@graph":[{"@type":"Service","name":"Dental Marketing","provider":ORG,"serviceType":"Dental marketing, dental SEO, Google Ads for dentists, dental lead generation","areaServed":"AU"},
  {"@type":"FAQPage","mainEntity":[
   {"@type":"Question","name":"How much should a dental clinic spend on marketing?","acceptedAnswer":{"@type":"Answer","text":"Most clinics we manage invest between 3% and 8% of revenue, weighted toward Google Ads and SEO. We set budgets by treatment goal and suburb competition, then track every dollar to a booked appointment."}},
   {"@type":"Question","name":"How long until dental SEO works?","acceptedAnswer":{"@type":"Answer","text":"Local map-pack movement is typically visible within 6–10 weeks. Competitive treatment terms like dental implants take 4–9 months. Google Ads fills the gap from week one."}},
   {"@type":"Question","name":"Do you work with dentists outside Sydney?","acceptedAnswer":{"@type":"Answer","text":"Yes. We're based in Sydney and manage clinics in every Australian state, as well as labs, equipment suppliers and course providers who sell nationally."}}]}]},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Dental marketing</p>
  <h1 style="margin-top:22px">Marketing for dentists that's measured in <span class="u">booked patients</span>, not impressions.</h1>
  <p class="lead">Google Ads, dental SEO, Meta and email — all wired into Smileox so no enquiry goes cold. We do this for 100+ clinics and nothing else.</p>
  <div class="hero-actions"><a class="btn" href="contact.html"><span class="dot"></span>Fill my books</a><a class="btn ghost" href="#services">What's included</a></div>
</div></section>

<section class="section tight" id="services"><div class="wrap">
  <div class="grid g4" style="margin-bottom:clamp(40px,6vw,80px)">
    <div class="stat reveal"><strong>100+</strong><span>dental clinics under management</span></div>
    <div class="stat reveal"><strong>&lt;60s</strong><span>median first response to a new lead via Smileox</span></div>
    <div class="stat reveal"><strong>By treatment</strong><span>every campaign reports cost per booked patient, per treatment</span></div>
    <div class="stat reveal"><strong>Dental only</strong><span>clinics, labs, suppliers, manufacturers, educators</span></div>
  </div>
  <ul class="list">
    <li class="reveal"><strong>Google Ads for dentists</strong><p>Campaigns built per treatment (implants, Invisalign, emergency, cosmetic, general) and per suburb, landing on pages that convert. Call tracking, form tracking and Smileox integration mean we optimise to booked appointments, not clicks.</p></li>
    <li class="reveal"><strong>Dental SEO &amp; local SEO</strong><p>Google Business Profile, map-pack ranking, treatment and suburb pages, technical health and schema. The compounding channel — we build it so your cost per patient drops every year.</p></li>
    <li class="reveal"><strong>Meta &amp; social ads</strong><p>Video-led campaigns for cosmetic, orthodontic and high-value treatments, retargeting site visitors, and lookalike audiences built from your real patient base.</p></li>
    <li class="reveal"><strong>Lead nurture &amp; triage (Smileox)</strong><p>Instant SMS and email replies, 14-day nurture sequences, missed-call text-back, and triage by treatment value so your team talks to the right people first. <a class="link" href="smileox.html">About Smileox</a></p></li>
    <li class="reveal"><strong>Email &amp; reactivation</strong><p>Recall campaigns, dormant-patient reactivation and treatment-plan follow-up. Often the cheapest appointments a clinic will ever book.</p></li>
    <li class="reveal"><strong>Reporting you'll actually read</strong><p>One dashboard: leads, bookings, cost per booking and estimated treatment value, by channel. A 15-minute monthly call to decide what to push next.</p></li>
  </ul>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Beyond the clinic</p><h2 style="margin-top:18px">B2B dental marketing.</h2><p class="lead" style="margin-top:18px">Selling to dentists is a different game. We run demand generation for equipment manufacturers, suppliers, labs and course providers — including Vatic and MDS by Henry Schein.</p></div>
    <div class="grid g2 reveal">
      <div class="card"><h3>Equipment &amp; suppliers</h3><p>Product launch campaigns, dealer and clinic lead generation, LinkedIn and Google, and nurture sequences tuned to long dental buying cycles.</p></div>
      <div class="card"><h3>Labs &amp; course providers</h3><p>Clinic acquisition for labs; course fill campaigns and waitlist automation for educators. Smileox triages enquiries the same way it does for patients.</p></div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Questions dentists ask us</p><h2 style="margin-top:18px">Straight answers.</h2></div>
    <div class="reveal">
      <details><summary>How much should a dental clinic spend on marketing?</summary><p>Most clinics we manage invest between 3% and 8% of revenue, weighted toward Google Ads and SEO. We set budgets by treatment goal and suburb competition, then track every dollar to a booked appointment.</p></details>
      <details><summary>How long until dental SEO works?</summary><p>Local map-pack movement is typically visible within 6–10 weeks. Competitive treatment terms like "dental implants" take 4–9 months. Google Ads fills the gap from week one.</p></details>
      <details><summary>Do you work with dentists outside Sydney?</summary><p>Yes. We're based in Sydney and manage clinics in every Australian state, plus labs, suppliers and course providers who sell nationally.</p></details>
      <details><summary>Will you work with my competitor down the road?</summary><p>We protect core suburbs for core treatments. If there's a conflict, we'll tell you on the first call.</p></details>
      <details><summary>Is this AHPRA-compliant?</summary><p>Yes. No testimonials in ads, no misleading claims, no before/after without the right context. We've run dental campaigns for years and know the guidelines cold.</p></details>
    </div>
  </div>
</div></section>
{cta()}
""")

# ---------------- DENTAL WEBSITES ----------------
pages["dental-websites.html"]=dict(
 title="Dental Website Design Australia | Fast, Modern Dentist Websites — GYA",
 desc="Modern dental website design with video banners, online booking and Core Web Vitals in the green. Built to rank for dental SEO terms and convert visitors into booked patients.",
 schema={"@context":"https://schema.org","@type":"Service","name":"Dental Website Design","provider":ORG,"serviceType":"Dental website design and development","areaServed":"AU"},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Dental web design &amp; development</p>
  <h1 style="margin-top:22px">Dental websites that load fast, look expensive and <span class="u">book patients</span>.</h1>
  <p class="lead">Video banners, online booking, treatment pages built for SEO, and Core Web Vitals Google actually rewards. Every site below is live — watch them.</p>
  <div class="hero-actions"><a class="btn" href="contact.html"><span class="dot"></span>Start a website</a><a class="btn ghost" href="#live">See live sites</a></div>
</div></section>

<section class="section dark" id="live"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:clamp(32px,5vw,64px)">
    <div class="reveal"><p class="eyebrow">Live previews</p><h2 style="margin-top:18px">Shipped this quarter.</h2></div>
    <p class="lead reveal">Real clinic sites streaming from the web, video banners playing. Hover to browse, open in a tab to go deeper.</p>
  </div>
  {work_grid()}
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">What's in every build</p><h2 style="margin-top:18px">The boring stuff, done properly.</h2><p class="lead" style="margin-top:18px">The prettiest dental site in Australia is worthless if it scores 40 on mobile and has no booking path.</p></div>
    <ul class="list reveal">
      <li><strong>Performance first</strong><p>Largest Contentful Paint under 2.5s, no layout shift, optimised video and images. We tune for Core Web Vitals because Google ranks on them.</p></li>
      <li><strong>Mobile-first design</strong><p>70%+ of dental traffic is on a phone. We design the mobile experience first and scale it up — not the other way round.</p></li>
      <li><strong>Video banners</strong><p>Clinic walk-throughs and team footage, compressed and lazy-loaded so they look cinematic without costing you speed.</p></li>
      <li><strong>Booking &amp; Smileox</strong><p>Online booking integration plus every form routed into Smileox for instant reply, nurture and triage.</p></li>
      <li><strong>SEO architecture</strong><p>Treatment pages, suburb pages, FAQ schema, LocalBusiness schema, clean URLs, internal linking. Built to rank from day one.</p></li>
      <li><strong>Accessibility &amp; compliance</strong><p>WCAG-minded contrast and keyboard navigation, AHPRA-aware content, privacy and cookie handling for Australian clinics.</p></li>
    </ul>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g3">
    <div class="card reveal"><span class="num">01</span><h3>Discovery</h3><p>Your treatments, your suburb, your competitors, your brand. One workshop, then we write before we design.</p></div>
    <div class="card reveal"><span class="num">02</span><h3>Design &amp; build</h3><p>Mobile-first design, custom build, video production if needed. You see it live on a staging link the whole way.</p></div>
    <div class="card reveal"><span class="num">03</span><h3>Launch &amp; grow</h3><p>Migration with zero SEO loss, analytics and Smileox wired in, then ongoing care and content as part of your marketing.</p></div>
  </div>
</div></section>
{cta("Your next website, live in weeks.","Tell us the clinic and the suburb. We'll send back a plan and a realistic timeline.")}
""")

# ---------------- SMILEOX ----------------
pages["smileox.html"]=dict(
 title="Smileox | Dental Lead Nurture & Triage Platform by GYA",
 desc="Smileox is the lead platform built by GYA for dental clinics. It replies to every enquiry in seconds, nurtures leads automatically and triages them by treatment value — so your front desk books more patients.",
 schema={"@context":"https://schema.org","@type":"SoftwareApplication","name":"Smileox","applicationCategory":"BusinessApplication","operatingSystem":"Web","creator":ORG,"description":"Dental lead nurture and triage platform."},
 body=f"""
<section class="page-hero dark" style="padding-bottom:0"><div class="wrap">
  <p class="eyebrow">Smileox · built by GYA</p>
  <h1 style="margin-top:22px">The lead comes in at 9:02. By 9:06 it's <span class="accent">booked</span>.</h1>
  <p class="lead">Smileox is the platform we built because ads were generating leads faster than front desks could answer them. It replies instantly, nurtures automatically and triages by treatment value — 24/7.</p>
  <div class="hero-actions" style="margin-bottom:clamp(48px,7vw,96px)"><a class="btn light" href="contact.html"><span class="dot"></span>Get Smileox on my enquiries</a></div>
  <div class="flow reveal">
    <div><span class="k"><b>01</b> Capture</span><h3>Every channel, one inbox</h3><p>Website forms, Google Ads calls, missed calls, Meta lead forms, Instagram DMs, email. Nothing lands in a spam folder at 6pm on Friday.</p></div>
    <div><span class="k"><b>02</b> Respond</span><h3>Reply in under a minute</h3><p>Personalised SMS and email on the patient's channel. Missed-call text-back. Consult options and booking links, automatically.</p></div>
    <div><span class="k"><b>03</b> Nurture</span><h3>14-day sequences by treatment</h3><p>Implant leads get implant content. Invisalign leads get Invisalign content. Finance questions answered before they're asked.</p></div>
    <div><span class="k"><b>04</b> Triage</span><h3>Hot, warm, cool — by value</h3><p>Your team sees a ranked list: who's ready, what they want, what it's worth. They call the implant consult before the check-up.</p></div>
  </div>
  <div style="height:clamp(48px,7vw,96px)"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">Why we built it</p><h2 style="margin-top:18px">Marketing stops at the enquiry. Smileox doesn't.</h2></div>
    <div class="reveal">
      <p class="lead">We manage ads for over 100 clinics. The pattern was always the same: good campaigns, real leads, and then silence — an unanswered form, a voicemail nobody returned, a "we'll call you back" that never happened. The patient booked somewhere else.</p>
      <p class="lead" style="margin-top:20px">So we built the thing that closes the gap. Smileox sits between your marketing and your front desk, and it never takes a lunch break.</p>
      <div class="grid g3" style="margin-top:40px">
        <div class="stat"><strong>&lt;60s</strong><span>median first response</span></div>
        <div class="stat"><strong>24/7</strong><span>including weekends and after hours</span></div>
        <div class="stat"><strong>Ranked</strong><span>every lead scored by treatment value</span></div>
      </div>
    </div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <ul class="list">
    <li class="reveal"><strong>For clinics</strong><p>Patient enquiries answered, nurtured and booked. Reactivation of dormant patients. Front desk works a prioritised list instead of a voicemail backlog.</p></li>
    <li class="reveal"><strong>For labs, suppliers &amp; educators</strong><p>Clinic and dealer enquiries triaged by account size, course enquiries nurtured to enrolment. The same engine, pointed at B2B.</p></li>
    <li class="reveal"><strong>For your reporting</strong><p>Because Smileox sees the lead and the booking, we can finally report cost per booked patient by channel and treatment — not cost per click.</p></li>
    <li class="reveal"><strong>Included with GYA marketing</strong><p>Smileox comes with every marketing engagement. It can also run standalone on your existing campaigns.</p></li>
  </ul>
</div></section>
{cta("Put Smileox on your enquiries.","We'll connect your forms and phone lines, show you the first week of triaged leads, and you'll wonder how you ran without it.")}
""")

# ---------------- AI MARKETING ----------------
pages["ai-marketing.html"]=dict(
 title="AI Marketing for Dentists | How AI Changes Dental Patient Acquisition — GYA",
 desc="How AI search, AI agents and automated follow-up are changing dental marketing — and what GYA is building so your clinic gets found and books patients in an AI-first world.",
 schema={"@context":"https://schema.org","@type":"Article","headline":"AI marketing and the future of dental patient acquisition","author":{"@type":"Organization","name":"Generate Your Audience"},"publisher":ORG},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">AI marketing</p>
  <h1 style="margin-top:22px">Patients are starting to ask an AI for a dentist. <span class="u">Is it recommending you?</span></h1>
  <p class="lead">Search is changing faster than most agencies admit. Here's how we see it, what it means for your clinic, and what we're already doing about it.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="split">
    <div class="sticky reveal"><p class="eyebrow">What's changing</p><h2 style="margin-top:18px">Three shifts, already underway.</h2></div>
    <div class="reveal">
      <ul class="list">
        <li><strong>AI answers replace result pages</strong><p>Google's AI Overviews, ChatGPT and Perplexity answer "best dentist for implants near me" with a short list and a recommendation. Being on page one isn't enough — you need to be in the answer. That means structured data, consistent entity information, real reviews, and content that answers questions the way a person would ask them.</p></li>
        <li><strong>Follow-up becomes automated and personal</strong><p>The clinics winning right now aren't spending more on ads. They're answering faster and more relevantly. AI-driven nurture — the kind Smileox runs — makes a solo practice feel like it has a ten-person patient coordination team.</p></li>
        <li><strong>Creative and content get cheaper, so judgement gets dearer</strong><p>Anyone can generate fifty ad variations. Knowing which suburb, which treatment and which offer to run them on is the work. We use AI to move faster and our dental experience to decide what's worth moving on.</p></li>
      </ul>
    </div>
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split" style="margin-bottom:clamp(32px,5vw,56px)">
    <div class="reveal"><p class="eyebrow">What we do about it</p><h2 style="margin-top:18px">AI-ready dental marketing.</h2></div>
    <p class="lead reveal">Practical, not speculative. Every item below is running for GYA clinics today.</p>
  </div>
  <div class="grid g3">
    <div class="card reveal"><h3>Answer-engine optimisation</h3><p>Entity-consistent clinic data, FAQ and medical schema, conversational treatment content, and monitoring of how AI assistants describe your clinic.</p></div>
    <div class="card reveal"><h3>AI-driven lead response</h3><p>Smileox replies, qualifies and nurtures on the patient's channel, in their language, in seconds. Hot leads are flagged for a human call.</p></div>
    <div class="card reveal"><h3>Predictive budget allocation</h3><p>Spend moves toward the treatment-suburb combinations producing booked patients this month, not last quarter's plan.</p></div>
    <div class="card reveal"><h3>Creative at volume, tested fast</h3><p>Dozens of ad variations generated, tested and pruned weekly. The winners get budget; the rest are gone in days.</p></div>
    <div class="card reveal"><h3>Reactivation intelligence</h3><p>Your patient database, segmented by likely next treatment, contacted with the right message at the right time.</p></div>
    <div class="card reveal"><h3>Reporting in plain English</h3><p>A monthly summary that reads like a note from your practice manager, not a spreadsheet export.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Our view</p><h2 style="margin-top:18px">The clinics that win the next five years.</h2></div>
    <div class="reveal"><p class="lead">They'll be the ones whose data is clean enough for machines to recommend, whose follow-up is fast enough to beat the clinic down the road, and whose marketing partner treats AI as a tool rather than a headline. We intend to be that partner — and to keep saying exactly what's working and what isn't.</p></div>
  </div>
</div></section>
{cta("See how AI describes your clinic today.","We'll run the check on your clinic's AI visibility and lead response time, and show you both on a call.")}
""")

# ---------------- WORK ----------------
pages["work.html"]=dict(
 title="Recent Dental Website Work | Live Previews — GYA",
 desc="Live previews of recent dental websites built by GYA: Lava Street Dental, Horizon Dental, Artarmon Dentists and Grey Street Dentist. Video banners, online booking and fast load times.",
 schema={"@context":"https://schema.org","@type":"CollectionPage","name":"Recent work","isPartOf":{"@type":"WebSite","url":SITE}},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Recent work</p>
  <h1 style="margin-top:22px">Live, not screenshots.</h1>
  <p class="lead">Every site here is streaming in from the web right now, video banners playing. Hover to browse. Open one in a new tab and run it through PageSpeed yourself.</p>
</div></section>
<section class="section dark"><div class="wrap">{work_grid()}</div></section>
<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Also in the studio</p><h2 style="margin-top:18px">Brands we build for.</h2></div>
    <div class="reveal"><p class="lead">Alongside clinic work, we run marketing and digital for dental industry brands including Vatic and MDS by Henry Schein, plus labs, equipment suppliers and course providers across Australia.</p>
    <div class="brands" style="margin-top:24px"><span>Vatic</span><span>MDS by Henry Schein</span><span>100+ clinics</span></div></div>
  </div>
</div></section>
{cta("Want a site like these?","Tell us about your clinic. We'll send back a plan, a timeline and a couple of directions.")}
""")

# ---------------- ABOUT ----------------
pages["about.html"]=dict(
 title="About GYA | The Dental Marketing Team Behind 100+ Clinics",
 desc="Meet Rowayne and Brett, the team behind Generate Your Audience — a Sydney dental marketing agency managing 100+ clinics plus labs, suppliers, manufacturers and course providers.",
 schema={"@context":"https://schema.org","@type":"AboutPage","mainEntity":ORG},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">About</p>
  <h1 style="margin-top:22px">Two people. One industry. A very full calendar.</h1>
  <p class="lead">We only do dental. Clinics, labs, equipment manufacturers, suppliers and course providers — over 100 of them. It's why we can tell you on the first call what's going to work in your suburb.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="team">
    <div class="person reveal">
      <img src="assets/rowayne.jpg" alt="Rowayne, founder of Generate Your Audience" width="600" height="750" loading="lazy">
      <h3>Rowayne</h3><p class="role">Founder · Strategy &amp; growth</p>
      <p>Built GYA from a handful of local businesses into the agency behind 100+ dental clinics. Lives in the numbers — cost per booked patient, by treatment, by suburb — and is the reason Smileox exists.</p>
    </div>
    <div class="person reveal">
      <img src="assets/brett.jpg" alt="Brett, Generate Your Audience" width="600" height="750" loading="lazy">
      <h3>Brett</h3><p class="role">Partnerships · Client success</p>
      <p>The person clinics actually talk to. Runs onboarding, reporting and the monthly "what do we push next" calls. Has probably already met your practice manager at a conference.</p>
    </div>
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">How we work</p><h2 style="margin-top:18px">Things we believe that other agencies find inconvenient.</h2></div>
    <ul class="list reveal">
      <li><strong>Booked patients are the only metric</strong><p>Impressions, reach and "brand lift" are lovely. Your books being full is the job.</p></li>
      <li><strong>Speed beats spend</strong><p>The clinic that answers first usually wins. That's why we built Smileox before we built a sales deck.</p></li>
      <li><strong>Only dental</strong><p>No restaurants, no gyms, no real estate. One industry means pattern recognition you can't buy.</p></li>
      <li><strong>Say what isn't working</strong><p>You'll hear it from us first, with the fix. Every month.</p></li>
    </ul>
  </div>
</div></section>
{cta("Say hello.","A 20-minute call. No deck, no pitch — just a look at your numbers and what we'd do first.")}
""")

# ---------------- CONTACT ----------------
pages["contact.html"]=dict(
 title="Contact GYA | Book a Dental Marketing Call",
 desc="Book a 20-minute call with Generate Your Audience. We'll look at your clinic's numbers, suburb and competitors and tell you what we'd do first to fill your books.",
 schema={"@context":"https://schema.org","@type":"ContactPage","mainEntity":ORG},
 body=f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1 style="margin-top:22px">Let's fill your books.</h1>
  <p class="lead">Tell us who you are and what you want more of. We'll come back within one business day with a time and a first read on your numbers.</p>
</div></section>
<section class="section tight"><div class="wrap">
  <div class="split">
    <div class="sticky reveal">
      <h3>What happens next</h3>
      <ul class="list" style="margin-top:16px">
        <li><strong>1 day</strong><p>We reply with a time.</p></li>
        <li><strong>20 min</strong><p>A call about your clinic, your suburb, your competitors.</p></li>
        <li><strong>A plan</strong><p>Your first 30 days, in writing.</p></li>
      </ul>
      <p class="muted" style="margin-top:24px;font-size:.95rem">Prefer email? <a class="link" href="mailto:hello@generateyouraudience.com">hello@generateyouraudience.com</a></p>
    </div>
    <form class="form reveal" data-contact method="post" action="#">
      <div class="two">
        <label>Name<input type="text" name="name" autocomplete="name" required></label>
        <label>Practice / company<input type="text" name="company" autocomplete="organization" required></label>
      </div>
      <div class="two">
        <label>Email<input type="email" name="email" autocomplete="email" required></label>
        <label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
      </div>
      <label>I am a…<select name="type"><option>Dental clinic</option><option>Dental lab</option><option>Equipment manufacturer or supplier</option><option>Dental course provider</option><option>Something else</option></select></label>
      <label>What do you want more of?<textarea name="message" placeholder="Implant consults in the inner west, a new website, Smileox on our enquiries…"></textarea></label>
      <button class="btn" type="submit"><span class="dot"></span>Send</button>
    </form>
  </div>
</div></section>
""")

for slug,p in pages.items():
    html=head(p["title"],p["desc"],slug,p.get("schema"))+p["body"]+FOOT
    with open(os.path.join(OUT,slug),"w") as f:f.write(html)

# sitemap + robots
urls="".join(f"<url><loc>{SITE}/{'' if s=='index.html' else s}</loc><changefreq>monthly</changefreq><priority>{'1.0' if s=='index.html' else '0.8'}</priority></url>" for s in pages)
open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(OUT,"assets","favicon.svg"),"w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#f0565c"/><stop offset="1" stop-color="#f58a5a"/></linearGradient></defs><rect width="64" height="64" rx="14" fill="#0a0a0a"/><text x="32" y="44" text-anchor="middle" font-family="system-ui,sans-serif" font-weight="700" font-size="34" fill="url(#g)">g</text></svg>')
print("built",list(pages))
