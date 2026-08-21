import os, json, re
SITE="https://www.generateyouraudience.com"
PHONE="+61400000000"   # TODO: Brett's number
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
<meta property="og:image" content="{SITE}/assets/team.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
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
      <a class="btn" href="tel:{PHONE}"><span class="dot"></span>Speak to Brett</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  {''.join(f'<a class="item" href="{h}">{l}<small>0{i+1}</small></a>' for i,(h,l) in enumerate(NAV))}
  <div class="mm-foot">
    <a class="btn" href="tel:{PHONE}"><span class="dot"></span>Speak to Brett</a>
    <a class="btn ghost" href="#" data-open-contact>Send us a note</a>
  </div>
</div>
<main id="main">
"""

def pills(name="need"):
    opts=["Fill my books","A new website","SmileOX on my leads","Google Ads","Local SEO","Social media","Not sure yet"]
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
  <label>Anything else<textarea name="message" placeholder="Where you are, what you want more of, what's not working right now"></textarea></label>
  <button class="btn" type="submit"><span class="dot"></span>Send it to Brett</button>
</form>"""

MODAL=f"""
<div class="modal" id="contact-modal" role="dialog" aria-modal="true" aria-labelledby="cm-title">
  <div class="backdrop" data-close></div>
  <div class="panel">
    <button class="close" aria-label="Close" data-close>×</button>
    <h2 id="cm-title">Tell us what's going on.</h2>
    <p class="muted">Or skip the form and <a class="link" href="tel:{PHONE}">call Brett</a>. He picks up.</p>
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
      <div><h4>Talk to Brett</h4><ul>
        <li><a href="tel:{PHONE}">Call Brett</a></li>
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

def cta(title="Empty books give us anxiety. Genuinely.",sub="So if yours are looking a bit light, call Brett. Twenty minutes, no pitch, just a look at what's going on and what we'd do about it."):
    return f"""
<section class="section tight">
  <div class="wrap">
    <div class="cta-band dark reveal">
      <div><h2>{title}</h2><p class="lead" style="margin-top:16px">{sub}</p></div>
      <div class="actions"><a class="btn light" href="tel:{PHONE}"><span class="dot"></span>Speak to Brett</a><a class="btn ghost-light" href="#" data-open-contact>Send a note instead</a></div>
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
    out='<div class="work-grid">'
    for url,host,name,tags in (SITES[:limit] if limit else SITES):
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
