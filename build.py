import os, json, re
SITE="https://www.generateyouraudience.com"
PHONE="1300889840"
OUT=os.path.dirname(os.path.abspath(__file__))

NAV=[("index.html","Home"),("dental-marketing.html","Dental Marketing"),("dental-websites.html","Dental Websites"),
     ("smileox.html","SmileOX"),("marketing.html","All Industries"),("ai-marketing.html","AI Marketing"),("work.html","Work"),("about.html","About")]

FONTS="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Inter+Tight:wght@400;500;600&display=swap"

def head(title,desc,slug,schema=None):
    s=json.dumps(schema) if schema else ""
    url=SITE+"/"+("" if slug=="index.html" else slug)
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0a0a0a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Generate Your Audience">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="GYA. We're not going to tell you why you should hire us.">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="icon" href="assets/favicon-16.png" type="image/png" sizes="16x16">
<link rel="apple-touch-icon" href="assets/favicon-180.png">
<link rel="manifest" href="assets/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="css/style.css">
{'<script type="application/ld+json">'+s+'</script>' if s else ''}
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
<header class="header">
  <div class="wrap nav">
    <a class="logo" href="index.html" aria-label="Generate Your Audience home"><img src="assets/gya-logo.png" alt="GYA, Generate Your Audience" width="240" height="60" fetchpriority="high"></a>
    <nav class="menu" aria-label="Primary">
      {''.join(f'<a href="{h}">{l}</a>' for h,l in NAV[1:])}
    </nav>
    <div class="nav-cta">
      <a class="btn" href="tel:{PHONE}"><span class="dot"></span>Contact us</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  {''.join(f'<a class="item" href="{h}">{l}<small>0{i+1}</small></a>' for i,(h,l) in enumerate(NAV))}
  <div class="mm-foot">
    <a class="btn" href="tel:{PHONE}"><span class="dot"></span>Contact us</a>
    <a class="btn ghost" href="#" data-open-contact>Send us a note</a>
  </div>
</div>
<main id="main">
"""

def pills(name="need"):
    opts=["Fill my books","A new website","SmileOX on my leads","Google Ads","Local SEO","Social media","Branding or design","Video","Not sure yet"]
    return '<div class="pills" role="group" aria-label="What do you need">'+''.join(
        f'<input type="checkbox" id="{name}-{i}" name="{name}" value="{o}"><label for="{name}-{i}">{o}</label>' for i,o in enumerate(opts))+'</div>'

def form(idp="c"):
    return f"""<form class="form" data-contact method="post" action="#">
  <div class="two">
    <label>Your name<input type="text" name="name" autocomplete="name" required></label>
    <label>Business name<input type="text" name="company" autocomplete="organization"></label>
  </div>
  <div class="two">
    <label>Email<input type="email" name="email" autocomplete="email" required></label>
    <label>Mobile<input type="tel" name="phone" autocomplete="tel" required></label>
  </div>
  <div class="group">What do you need? {pills(idp)}</div>
  <label>What's not working right now?<textarea name="message" placeholder="Where you are, what you want more of, what's going wrong"></textarea></label>
  <button class="btn" type="submit"><span class="dot"></span>Send it through</button>
</form>"""

MODAL=f"""
<div class="modal" id="contact-modal" role="dialog" aria-modal="true" aria-labelledby="cm-title">
  <div class="backdrop" data-close></div>
  <div class="panel">
    <button class="close" aria-label="Close" data-close>×</button>
    <h2 id="cm-title">Tell us what's going on.</h2>
    <p class="muted">Or skip the form and call us on <a class="link" href="tel:{PHONE}">1300 889 840</a>.</p>
    {form("m")}
  </div>
</div>"""

FOOT=f"""
</main>
<footer class="footer light">
  <div class="wrap">
    <div class="top">
      <div>
        <img class="flogo" src="assets/gya-logo.png" alt="GYA, Generate Your Audience" width="240" height="60" loading="lazy">
        <p class="muted" style="margin-top:16px;max-width:34ch">Generate Your Audience. Founded 2015. Lead generation, websites and marketing for dental and about 30 other industries. Sydney based, working Australia-wide.</p>
      </div>
      <div><h4>Services</h4><ul>
        <li><a href="dental-marketing.html">Dental marketing</a></li>
        <li><a href="dental-websites.html">Dental websites</a></li>
        <li><a href="smileox.html">SmileOX</a></li>
        <li><a href="marketing.html">Marketing for all industries</a></li>
        <li><a href="ai-marketing.html">AI marketing</a></li></ul></div>
      <div><h4>Us</h4><ul>
        <li><a href="work.html">Recent work</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Talk to us</h4><ul>
        <li><a href="tel:{PHONE}">1300 889 840</a></li>
        <li><a href="mailto:hello@generateyouraudience.com">hello@generateyouraudience.com</a></li>
        <li><a href="#" data-open-contact>Send a note</a></li></ul></div>
    </div>
    <div class="bottom">
      <span>© 2026 Generate Your Audience Pty Ltd</span>
      <span>Sydney · Melbourne · Brisbane · Perth · Adelaide</span>
    </div>
  </div>
</footer>
{MODAL}
<script src="js/main.js" defer></script>
</body>
</html>
"""

def cta(title="Empty books give us anxiety. Genuinely.",sub="So if yours are looking a bit light, call us. Twenty minutes, no pitch, just a look at what's going on and what we'd do about it.",extra=""):
    ex=f'<p class="muted" style="margin-top:14px">{extra}</p>' if extra else ""
    return f"""
<section class="section tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <div><h2>{title}</h2><p class="lead" style="margin-top:16px">{sub}</p>{ex}</div>
      <div class="actions"><a class="btn" href="tel:{PHONE}"><span class="dot"></span>Call 1300 889 840</a><a class="btn ghost" href="#" data-open-contact>Send a note instead</a></div>
    </div>
  </div>
</section>"""

def faq(items):
    html="".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)
    schema={"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}
    return html,schema

from urllib.parse import quote
SITES=[
 dict(slug="footscray",url="https://www.footscraydentalstudio.com.au",host="footscraydentalstudio.com.au",name="Footscray Dental Studio",place="Footscray VIC",tags="Brand · Website · Google Ads",
  short="New owners, new name, same chairs. The site had to tell Footscray what changed without losing the patients who'd been coming for years.",
  long=["An established practice on Barkly St, taken over by new owners and renamed. That's a tricky one. Half the job is winning new patients, and the other half is making sure the old ones don't assume the place shut down.",
        "So the old name is mentioned plainly, the new patient offer sits on the homepage with a price on it, and every treatment they do has its own page, from check-ups through to All-on-X. The Google Ads went live pointing at those same pages, so the brand, the site and the ads all turned up together."]),
 dict(slug="my-dentist",url="https://dentist-alderley-newmarket.com.au",host="dentist-alderley-newmarket.com.au",name="My Dentist",place="Alderley QLD",tags="Website · Positioning · Suburb pages",
  short="A holistic practice with a strong point of view. The site says it in five seconds and still works for a family that just wants a check-up.",
  long=["This practice knows exactly what it is: whole-body, low-tox dentistry. That's a great position and an easy one to overdo, because the same site also has to work for a parent booking two kids in for a clean.",
        "The hero leads with the idea, the exam packages sit right under it with prices on them, and each suburb they draw patients from gets its own page. Someone who's never heard of holistic dentistry gets it straight away, and someone who went looking for it knows they've found the right place."]),
 dict(slug="tooth-n-care",url="https://toothncare.vercel.app",host="toothncare.vercel.app",name="Tooth n Care",place="East Maitland NSW",tags="Website · Online booking · Treatment pages",
  short="A family practice in the Hunter, open Saturdays. Built for the parent booking from the car park at 5pm.",
  long=["A family practice on Lawes Street in East Maitland. Lots of kids, lots of first visits, and lots of people who haven't seen a dentist in a while and aren't thrilled about it.",
        "So Book Online is on every screen, the new patient price is on the homepage instead of hidden behind a phone call, and there's a page called Feeling Nervous? Start Here, which does exactly what it says. Every treatment has its own page, and the whole thing holds up on a phone with two bars."]),
 dict(slug="horizon",url="https://horizon.gya.net.au",host="horizon.gya.net.au",name="Horizon Dental",place="Sydney CBD",tags="Website · Booking flow · Video banner",
  short="Every page has a short path to the booking, not a trip back to a contact form.",
  mid="Built around one action, with a short route to the booking from wherever a patient lands.",
  long=["Built around one action. Wherever a patient lands, the path to a booking is short and obvious, and treatment pages carry their own booking prompts rather than sending someone back to a contact page to start again.",
        "Most sites make you decide twice. Once to want the thing, and again to work out how to get it. The second decision is where they lose people, so we took it out."]),
 dict(slug="newgen",url="https://newgen-site-sep24.vercel.app",host="newgen-site-sep24.vercel.app",name="New'Gen Dental Surgery",place="Seymour VIC",tags="Website · Local SEO",
  short="A regional practice where the map listing is most of the game. Built so Google knows exactly what they do and which towns they look after.",
  long=["Seymour is regional Victoria, and in a town that size the map listing does most of the heavy lifting. People aren't comparing twelve practices. They're checking who's close, who's open and whether anyone picks up.",
        "The site was built to back the listing up: details that match everywhere the practice appears, a page for each treatment, and the phone number where a thumb can find it. Nothing fancy for the sake of it, just a site that makes the practice easy to choose."]),
 dict(slug="artarmon",url="https://www.artarmondentists.com",host="artarmondentists.com",name="Artarmon Dentists",place="Artarmon NSW",tags="Website · Local SEO · Video banner",
  short="Built with the map listing as a design constraint rather than an afterthought.",
  mid="The map listing and the site were designed as one thing, which is how you win inside a few kilometres.",
  long=["For a practice competing inside a few kilometres, the map listing and the website have to work as one thing. So the local SEO wasn't bolted on after launch.",
        "The site was built with it in mind: the right code so search engines and AI assistants can tell exactly what the practice does and where, details that match everywhere the business is listed, and content written for the real catchment rather than a template with a suburb name swapped in."]),
]
def shot_src(s):
    local=f"assets/work/{s['slug']}.jpg"
    if os.path.exists(os.path.join(OUT,local)): return local,False
    return "https://s0.wp.com/mshots/v1/"+quote(s["url"],safe="")+"?w=900&h=1400&vpw=1280&vph=2000",True

def shot(s):
    src,remote=shot_src(s)
    initials="".join(w[0] for w in s["name"].replace("'","").split()[:2]).upper()
    return f"""<a class="shot" href="{s['url']}" target="_blank" rel="noopener" aria-label="Open the {s['name']} website">
  <div class="shot-bar"><i></i><i></i><i></i><span>{s['host']}</span></div>
  <div class="shot-img">
    <div class="ph" aria-hidden="true"><b>{initials}</b><span>{s['name']}</span><small>{s['place']}</small></div>
    <img src="{src}" alt="{s['name']} website homepage" width="900" height="1400" loading="lazy" decoding="async"{' data-mshot' if remote else ''} onerror="this.parentNode.classList.add('noimg')">
  </div>
</a>"""

def showcase(key="short"):
    out='<div class="showcase">'
    for s in SITES:
        blurb=s.get(key) or s["short"]
        out+=f"""
<article class="work reveal">
  {shot(s)}
  <div class="work-meta"><h3>{s['name']}</h3><span>{s['place']}</span></div>
  <p class="work-tags">{s['tags']}</p>
  <p class="work-blurb">{blurb}</p>
  <a class="link" href="{s['url']}" target="_blank" rel="noopener">Visit site</a>
</article>"""
    return out+"</div>"

def work_rows():
    out=""
    for i,s in enumerate(SITES):
        paras="".join(f"<p>{p}</p>" for p in s["long"])
        out+=f"""
<article class="work-row{' flip' if i%2 else ''} reveal">
  <div>{shot(s)}</div>
  <div class="work-copy">
    <p class="eyebrow">{s['place']}</p>
    <h2 style="margin:14px 0 6px">{s['name']}</h2>
    <p class="work-tags">{s['tags']}</p>
    {paras}
    <a class="link" href="{s['url']}" target="_blank" rel="noopener">Visit site</a>
  </div>
</article>"""
    return out

def card(name,ini,tags,rows,bar=True):
    t=''.join(f'<span class="tag {c}">{x}</span>' for c,x in tags)
    r=''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k,v in rows)
    return f'<div class="lead-card"><div class="nm"><span>{name}</span><span class="av">{ini}</span></div>{t}<dl>{r}</dl>{"<div class=bar></div>" if bar else ""}</div>'
BOARD=f"""
<div class="board" aria-label="SmileOX lead board, example data">
  <div class="board-top"><b>Leads · Google Ads + Meta</b><div><span class="pill">Sample Dental, Caringbah</span> <span class="pill">All forms</span> <span class="pill">Journeys (1)</span></div></div>
  <div class="kpis">
    <div class="kpi"><small>Avg first response</small><strong class="good">48s</strong></div>
    <div class="kpi"><small>Within 5 min</small><strong class="good">91%</strong></div>
    <div class="kpi"><small>Booked this month</small><strong>37</strong></div>
    <div class="kpi"><small>Needs a human</small><strong class="warn">4</strong></div>
  </div>
  <div class="cols">
    <div class="col" style="--c:#f0565c"><h5>Hot<small>6 leads · call now</small></h5>
      {card("J. Mitchell","JM",[("hot","Implants"),("ai","AI scored"),("ok","52s")],[("Source","Google Ads"),("Suburb","Miranda"),("Wants","Consult this week")])}
      {card("P. Nguyen","PN",[("hot","Invisalign"),("ok","1m 04s")],[("Source","Meta"),("Suburb","Cronulla"),("Wants","Finance options")])}
    </div>
    <div class="col" style="--c:#f5a25a"><h5>Warm<small>14 leads · in nurture</small></h5>
      {card("S. Okafor","SO",[("warm","Whitening"),("ai","Day 3 of 14")],[("Source","Website"),("Suburb","Gymea"),("Last","Opened email")])}
      {card("L. Romano","LR",[("warm","Check-up"),("ai","Missed call")],[("Source","Phone"),("Text-back","Sent 41s"),("Last","No reply yet")])}
    </div>
    <div class="col" style="--c:#18a35d"><h5>Booked<small>37 this month</small></h5>
      {card("A. Haddad","AH",[("ok","Booked Thu 2:30"),("hot","Crown")],[("Source","Google Ads"),("Value","$1,800"),("Handled by","Front desk")],False)}
      {card("T. Walker","TW",[("ok","Booked Mon 9:00"),("warm","Clean")],[("Source","Local SEO"),("Value","$240"),("Handled by","SmileOX")],False)}
    </div>
    <div class="col" style="--c:#8a8a8a"><h5>Cool<small>9 leads · low intent</small></h5>
      {card("M. Chen","MC",[("cool","Price only"),("ai","AI scored")],[("Source","Meta"),("Suburb","Out of area"),("Next","Monthly email")],False)}
      {card("R. Singh","RS",[("cool","No response"),("ai","Day 14")],[("Source","Website"),("Tries","SMS x3, email x2"),("Next","Archive")],False)}
    </div>
  </div>
</div>"""

ORG={"@context":"https://schema.org","@type":"ProfessionalService","name":"Generate Your Audience","alternateName":"GYA",
 "url":SITE,"logo":SITE+"/assets/gya-logo.png","image":SITE+"/assets/team.jpg","foundingDate":"2015","telephone":PHONE,
 "founder":[{"@type":"Person","name":"Rowayne","jobTitle":"Founder, Strategy"},{"@type":"Person","name":"Brett","jobTitle":"Co-founder, Client Success"}],"numberOfEmployees":{"@type":"QuantitativeValue","minValue":40},
 "description":"Digital marketing and lead generation agency founded in 2015. Dental marketing for 100+ clinics, plus websites, Google Ads, local SEO, social media and the SmileOX lead platform for businesses across Australia.",
 "areaServed":"AU","address":{"@type":"PostalAddress","addressLocality":"Sydney","addressRegion":"NSW","addressCountry":"AU"},
 "knowsAbout":["Dental marketing","Dental SEO","Dental website design","Lead generation","Google Ads","Local SEO","AI marketing","Social media marketing"]}

pages={}
exec(open(os.path.join(OUT,"pages.py")).read())

for slug,p in pages.items():
    html=head(p["title"],p["desc"],slug,p.get("schema"))+p["body"]+FOOT
    assert "\u2014" not in html and "\u2013" not in html, f"dash found in {slug}"
    open(os.path.join(OUT,slug),"w").write(html)

urls="".join(f"<url><loc>{SITE}/{'' if s=='index.html' else s}</loc><changefreq>monthly</changefreq><priority>{'1.0' if s=='index.html' else '0.8'}</priority></url>" for s in pages)
open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("built",list(pages))
