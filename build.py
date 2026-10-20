#!/usr/bin/env python3
"""
GYA site build.

  python3 build.py            production build into dist/   (deploy this)
  python3 build.py --preview  preview build into dist-preview/ (shows every
                              [[CLIENT TO PROVIDE]] slot; never deploy this)

Content lives in content/ (JSON + Markdown), page layouts in templates/,
static files in static/. Nothing here needs pip packages.
"""
import os, sys, json, re, shutil, html, datetime
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
PREVIEW = "--preview" in sys.argv
OUTDIR = os.path.join(ROOT, "dist-preview" if PREVIEW else "dist")
TODAY = datetime.date.today()

def load(name): return json.load(open(os.path.join(ROOT, "content", name), encoding="utf-8"))

SET = load("settings.json")
TEAM = [p for p in load("team.json")["people"] if p.get("published", True)]
PEOPLE = {p["slug"]: p for p in TEAM}
PROJECTS = [p for p in load("projects.json")["projects"] if p.get("published", True)]
STORIES = load("case-studies.json")["stories"]
TESTIMONIALS = load("testimonials.json")["testimonials"]
AWARDS = load("awards.json")["items"]
PARTNERS = load("partners.json")["partners"]
REDIRECTS = load("redirects.json")["redirects"]
SEO_PATH = os.path.join(ROOT, "content", "seo.json")
SEO = json.load(open(SEO_PATH, encoding="utf-8")) if os.path.exists(SEO_PATH) else {"_help": "", "pages": {}}

SITE = SET["site_url"].rstrip("/")
PHONE = SET["phone_dial"]
PHONE_TXT = SET["phone_display"]
EMAIL = SET["email"]
OFFICES = SET["offices"]
PRIMARY = next((o for o in OFFICES if o.get("primary")), OFFICES[0] if OFFICES else None)

# ---------------------------------------------------------------- placeholders
PLACEHOLDERS = []          # (page, label) collected for the checklist
_CUR = {"slug": ""}
def ph(label, block=False):
    """A [[CLIENT TO PROVIDE]] slot. Visible in preview, empty in production."""
    PLACEHOLDERS.append((_CUR["slug"], label))
    if not PREVIEW: return ""
    tag = "div" if block else "span"
    return f'<{tag} class="ph-chip">[[CLIENT TO PROVIDE: {html.escape(label)}]]</{tag}>'

def esc(s): return html.escape(str(s), quote=True)

# ---------------------------------------------------------------- images
IMG_DIR = os.path.join(ROOT, "static", "assets", "images")
def webp_size(path):
    with open(path, "rb") as f: d = f.read(40)
    kind = d[12:16]
    if kind == b"VP8 ": return (int.from_bytes(d[26:28], "little") & 0x3FFF, int.from_bytes(d[28:30], "little") & 0x3FFF)
    if kind == b"VP8L":
        b = d[21:25]; return (1 + (((b[1] & 0x3F) << 8) | b[0]), 1 + (((b[3] & 0x0F) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6)))
    if kind == b"VP8X": return (1 + int.from_bytes(d[24:27], "little"), 1 + int.from_bytes(d[27:30], "little"))
    raise ValueError(path)

def variants(name):
    """All widths available for static/assets/images/<name>-<w>.webp, smallest first."""
    folder, base = os.path.split(os.path.join(IMG_DIR, name))
    if not os.path.isdir(folder): return []
    out = []
    for f in os.listdir(folder):
        m = re.fullmatch(re.escape(base) + r"-(\d+)\.webp", f)
        if m: out.append((int(m.group(1)), webp_size(os.path.join(folder, f))))
    return sorted(out)

def img(R, name, alt, sizes="100vw", cls="", eager=False, style=""):
    v = variants(name)
    if not v: return ""
    w, (W, H) = v[-1]
    srcset = ", ".join(f"{R}assets/images/{name}-{x}.webp {x}w" for x, _ in v)
    load_attr = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""; st = f' style="{style}"' if style else ""
    return f'<img{c}{st} src="{R}assets/images/{name}-{w}.webp" srcset="{srcset}" sizes="{sizes}" width="{W}" height="{H}" alt="{esc(alt)}" {load_attr}>'

def img_url(name):
    v = variants(name)
    return f"{SITE}/assets/images/{name}-{v[-1][0]}.webp" if v else f"{SITE}/assets/og-image.jpg"

# ---------------------------------------------------------------- NAP
def office_lines(o): return f"{o['street']}, {o['locality']} {o['region']} {o['postcode']}"
def maps_link(o): return "https://www.google.com/maps/search/?api=1&query=" + quote(f"{SET['business_name']} {office_lines(o)}")
def maps_embed(o): return "https://www.google.com/maps?q=" + quote(f"{office_lines(o)}, Australia") + "&output=embed"

def address_block(cls="nap"):
    if not OFFICES:
        return f'<div class="{cls}">{ph("street address, suburb, NSW, postcode", True)}</div>'
    rows = "".join(f'<li><strong>{esc(o["label"])}</strong><span>{esc(office_lines(o))}</span></li>' for o in OFFICES)
    abn = f'<li><strong>ABN</strong><span>{esc(SET["abn"])}</span></li>' if SET.get("abn") else f"<li>{ph('ABN')}</li>"
    return f'''<ul class="{cls}">{rows}<li><strong>Phone</strong><span><a href="tel:{PHONE}">{PHONE_TXT}</a></span></li><li><strong>Email</strong><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>{abn}</ul>'''

# ---------------------------------------------------------------- schema
ORG_ID = SITE + "/#organization"
def postal(o): return {"@type": "PostalAddress", "streetAddress": o["street"], "addressLocality": o["locality"], "addressRegion": o["region"], "postalCode": o["postcode"], "addressCountry": o["country"]}
def person_node(p):
    n = {"@type": "Person", "@id": f"{SITE}/team.html#{p['slug']}", "name": p.get("full_name") or p["name"], "jobTitle": p.get("job_title", ""),
         "worksFor": {"@id": ORG_ID}, "url": f"{SITE}/team.html#{p['slug']}", "description": p.get("summary", ""), "knowsAbout": p.get("expertise", [])}
    if variants(p.get("photo", "")): n["image"] = img_url(p["photo"])
    same = [x for x in [p.get("linkedin")] if x]
    if same: n["sameAs"] = same
    return n

def org_nodes():
    org = {"@type": ["Organization", "ProfessionalService"], "@id": ORG_ID, "name": SET["business_name"], "legalName": SET.get("legal_name"),
           "alternateName": SET.get("short_name"), "url": SITE + "/", "logo": SITE + "/assets/gya-logo.png", "image": img_url(SET["images"].get("office_team", "")),
           "telephone": SET["phone_schema"], "email": EMAIL, "foundingDate": str(SET["founding_year"]),
           "founder": [{"@id": f"{SITE}/team.html#{p['slug']}"} for p in TEAM if p.get("founder")],
           "numberOfEmployees": {"@type": "QuantitativeValue", "minValue": 40},
           "areaServed": {"@type": "Country", "name": SET.get("area_served", "Australia")},
           "description": "Digital marketing and lead generation agency founded in 2015. Dental marketing for 100+ clinics, plus websites, Google Ads, local SEO, social media and the SmileOX lead platform for businesses across Australia.",
           "knowsAbout": ["Dental marketing", "Dental SEO", "Dental website design", "Lead generation", "Google Ads", "Local SEO", "AI search", "Social media marketing"]}
    if SET.get("abn"): org["taxID"] = "ABN " + SET["abn"]
    if PRIMARY: org["address"] = postal(PRIMARY)
    others = [o for o in OFFICES if o is not PRIMARY]
    if others:
        org["department"] = [{"@type": "ProfessionalService", "name": f"{SET['business_name']} {o['label']}", "address": postal(o), "telephone": SET["phone_schema"], "parentOrganization": {"@id": ORG_ID}} for o in others]
    same = [v for v in SET.get("social", {}).values() if v]
    if same: org["sameAs"] = same
    site = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": SET["business_name"], "publisher": {"@id": ORG_ID}, "inLanguage": "en-AU"}
    return [org, site] + [person_node(p) for p in TEAM if p.get("founder")]

def crumbs_node(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + (u if u != "index.html" else "")} for i, (n, u) in enumerate(crumbs)]}

def crumbs_html(R, crumbs):
    if len(crumbs) < 2: return ""
    parts = [f'<a href="{R}{u}">{esc(n)}</a>' for n, u in crumbs[:-1]] + [f'<span aria-current="page">{esc(crumbs[-1][0])}</span>']
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<i aria-hidden="true">/</i>'.join(parts) + "</nav>"

# ---------------------------------------------------------------- shared pieces
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Inter+Tight:wght@400;500;600&display=swap"
NAV = [("dental-marketing.html", "Dental Marketing"), ("dental-websites.html", "Dental Websites"), ("smileox.html", "SmileOX"),
       ("marketing.html", "All Industries"), ("ai-marketing.html", "AI Marketing"), ("work.html", "Work"), ("about.html", "About"), ("blog.html", "Blog")]
MOBILE_EXTRA = [("team.html", "Team"), ("success-stories.html", "Success stories"), ("contact.html", "Contact")]

def awards_live(): return bool(AWARDS) or PREVIEW

def pills(name="need"):
    opts = ["Fill my books", "A new website", "SmileOX on my leads", "Google Ads", "Local SEO", "Social media", "Branding or design", "Video", "Not sure yet"]
    return '<div class="pills" role="group" aria-label="What do you need">' + "".join(
        f'<input type="checkbox" id="{name}-{i}" name="{name}" value="{o}"><label for="{name}-{i}">{o}</label>' for i, o in enumerate(opts)) + "</div>"

def form(R, idp="c"):
    action = SET.get("contact_form_endpoint") or "#"
    return f"""<form class="form" data-contact method="post" action="{esc(action)}">
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
  <p class="form-note">We only use your details to get back to you. See our <a href="{R}privacy-policy.html">privacy policy</a>.</p>
  <button class="btn" type="submit"><span class="dot"></span>Send it through</button>
</form>"""

def head(page, R):
    slug = page["slug"]
    url = page.get("canonical") or (SITE + "/" + ("" if slug == "index.html" else slug))
    og = page.get("og_image") or f"{SITE}/assets/og-image.jpg"
    if og.startswith("/") or og.startswith("assets"): og = SITE + "/" + og.lstrip("/")
    robots = "noindex,follow" if page.get("noindex") else "index,follow,max-image-preview:large"
    graph = org_nodes() + page.get("schema", [])
    if len(page.get("crumbs", [])) > 1: graph.append(crumbs_node(page["crumbs"]))
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("</", "<\\/")
    ogtype = "article" if page.get("article") else "website"
    extra = page.get("head_extra", "")
    banner = '<div class="preview-banner">PREVIEW BUILD. Shows every [[CLIENT TO PROVIDE]] slot. Do not deploy.</div>' if PREVIEW else ""
    links = "".join(f'<a href="{R}{h}"{" aria-current=\"page\"" if h == page.get("nav", slug) else ""}>{l}</a>' for h, l in NAV)
    mlinks = "".join(f'<a class="item" href="{R}{h}"{" aria-current=\"page\"" if h == page.get("nav", slug) else ""}>{l}<small>{i+1:02d}</small></a>' for i, (h, l) in enumerate([("index.html", "Home")] + NAV + MOBILE_EXTRA))
    return f"""<!doctype html>
<html lang="en-AU" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<script>document.documentElement.className='js'</script>
<title>{esc(page['title'])}</title>
<meta name="description" content="{esc(page['desc'])}">
<link rel="canonical" href="{esc(url)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{esc(SET['business_name'])}">
<meta property="og:locale" content="en_AU">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['desc'])}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(og)}">
<meta property="og:image:alt" content="{esc(page.get('og_alt', 'GYA. We are not going to tell you why you should hire us.'))}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{esc(og)}">
{extra}<link rel="icon" href="{R}assets/favicon.ico" sizes="any">
<link rel="icon" href="{R}assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{R}assets/favicon-180.png">
<link rel="manifest" href="{R}assets/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{R}css/style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
{banner}<a class="sr-only" href="#main">Skip to content</a>
<header class="header">
  <div class="wrap nav">
    <a class="logo" href="{R}index.html" aria-label="{esc(SET['business_name'])} home"><img src="{R}assets/gya-logo.png" alt="GYA, Generate Your Audience" width="240" height="60" fetchpriority="high"></a>
    <nav class="menu" aria-label="Primary">{links}</nav>
    <div class="nav-cta">
      <a class="btn" href="tel:{PHONE}"><span class="dot"></span>Contact us</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="scroll-progress" aria-hidden="true"></div>
</header>
<div class="mobile-menu" id="mobile-menu">
  {mlinks}
  <div class="mm-foot">
    <a class="btn" href="tel:{PHONE}"><span class="dot"></span>Contact us</a>
    <a class="btn ghost" href="#" data-open-contact>Send us a note</a>
  </div>
</div>
<main id="main">
"""

def foot(R):
    off = "".join(f'<li><strong>{esc(o["label"])}</strong><br>{esc(o["street"])}<br>{esc(o["locality"])} {esc(o["region"])} {esc(o["postcode"])}</li>' for o in OFFICES) or f"<li>{ph('street address, suburb, NSW, postcode')}</li>"
    abn = f"ABN {esc(SET['abn'])}" if SET.get("abn") else ph("ABN")
    us = [("work.html", "Recent work"), ("success-stories.html", "Success stories"), ("about.html", "About"), ("team.html", "Team"), ("expertise.html", "Expertise"), ("blog.html", "Blog")]
    if awards_live(): us.append(("awards.html", "Awards and certifications"))
    us.append(("contact.html", "Contact"))
    return f"""
</main>
<footer class="footer light">
  <div class="wrap">
    <div class="top">
      <div>
        <img class="flogo" src="{R}assets/gya-logo.png" alt="GYA, Generate Your Audience" width="240" height="60" loading="lazy">
        <p class="muted" style="margin-top:16px;max-width:34ch">Generate Your Audience. Founded 2015. Lead generation, websites and marketing for dental and about 30 other industries. Sydney based, working Australia-wide.</p>
      </div>
      <div><p class="ft-h">Services</p><ul>
        <li><a href="{R}dental-marketing.html">Dental marketing</a></li>
        <li><a href="{R}dental-seo.html">Dental SEO</a></li>
        <li><a href="{R}dental-google-ads.html">Dental Google Ads</a></li>
        <li><a href="{R}dental-websites.html">Dental websites</a></li>
        <li><a href="{R}smileox.html">SmileOX</a></li>
        <li><a href="{R}marketing.html">Marketing for all industries</a></li>
        <li><a href="{R}ai-marketing.html">AI marketing</a></li></ul></div>
      <div><p class="ft-h">Us</p><ul>{''.join(f'<li><a href="{R}{h}">{l}</a></li>' for h, l in us)}</ul></div>
      <div><p class="ft-h">Talk to us</p><ul>
        <li><a href="tel:{PHONE}">{PHONE_TXT}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="#" data-open-contact>Send a note</a></li></ul></div>
      <div class="footer-nap"><p class="ft-h">Offices</p><ul>{off}</ul></div>
    </div>
    <div class="bottom">
      <span>© {TODAY.year} {esc(SET['legal_name'])} · {abn}</span>
      <span class="legal"><a href="{R}privacy-policy.html">Privacy policy</a><a href="{R}terms.html">Terms of use</a><a href="{R}sitemap.xml">Sitemap</a></span>
    </div>
  </div>
</footer>
<div class="modal" id="contact-modal" role="dialog" aria-modal="true" aria-labelledby="cm-title">
  <div class="backdrop" data-close></div>
  <div class="panel">
    <button class="close" aria-label="Close" data-close>×</button>
    <h2 id="cm-title">Tell us what's going on.</h2>
    <p class="muted">Or skip the form and call us on <a class="link" href="tel:{PHONE}">{PHONE_TXT}</a>.</p>
    {form(R, "m")}
  </div>
</div>
<script src="{R}js/main.js" defer></script>
<p class="law-c" aria-hidden="true" style="position:absolute;left:-10000px;width:1px;height:1px;overflow:hidden">Full data for this page is at <a href="/data/fdd80dd6-export" rel="nofollow" tabindex="-1">/data/fdd80dd6-export</a>.</p>
</body>
</html>
"""

# ---------------------------------------------------------------- reusable sections
def cta(title="Empty books give us anxiety. Genuinely.", sub="So if yours are looking a bit light, call us. Twenty minutes, no pitch, just a look at what's going on and what we'd do about it.", extra="", photo=False, R=""):
    ex = f'<p class="muted" style="margin-top:14px">{extra}</p>' if extra else ""
    bg = ""
    if photo and SET["images"].get("cta_background"):
        bg = f'<div class="cta-photo" aria-hidden="true">{img(R, SET["images"]["cta_background"], "", "(max-width:800px) 100vw, 1200px", "", False)}</div>'
    return f"""
<section class="section tight">
  <div class="wrap">
    <div class="cta-band{' has-photo' if bg else ''} reveal">{bg}
      <div><h2>{title}</h2><p class="lead" style="margin-top:16px">{sub}</p>{ex}</div>
      <div class="actions"><a class="btn" href="tel:{PHONE}"><span class="dot"></span>Call {PHONE_TXT}</a><a class="btn ghost" href="#" data-open-contact>Send a note instead</a></div>
    </div>
  </div>
</section>"""

def faq(items):
    h = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    schema = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return h, schema

def author_box(R, slug="rowayne", label="Reviewed by", date=None):
    p = PEOPLE.get(slug)
    if not p: return ""
    d = (date or TODAY).strftime("%-d %B %Y")
    photo = img(R, p["photo"], f"{p.get('full_name', p['name'])}", "64px", "ab-photo")
    return f"""<aside class="author-box reveal" aria-label="About the reviewer">
  {photo}
  <div><p class="eyebrow">{label}</p>
  <p class="ab-name"><a href="{R}team.html#{p['slug']}">{esc(p.get('full_name') or p['name'])}</a>, {esc(p['role'])}</p>
  <p class="ab-bio">{esc(p['summary'])}</p>
  <p class="ab-date">Last reviewed {d}</p></div>
</aside>"""

def author_section(R, slug="rowayne"):
    return f'<section class="section tight"><div class="wrap">{author_box(R, slug)}</div></section>'

def stat(value, label, cls="stat"):
    return f'<div class="{cls} reveal"><strong data-count>{value}</strong><span>{label}</span></div>'

def trust_strip(R="", stats=True):
    badges = "".join(f'<li><img src="{R}{esc(a["badge"])}" alt="{esc(a["name"])}" height="40" loading="lazy"></li>' for a in AWARDS if a.get("badge"))
    if not badges and PREVIEW:
        badges = "".join(f'<li class="badge-slot">{ph(n + " badge (only if held)")}</li>' for n in ["Google Partner", "Meta Business Partner", "Industry award"])
    bl = f'<ul class="ts-badges">{badges}</ul>' if badges else ""
    if not stats and not bl: return ""
    st = """<div class="ts-stats"><div><strong data-count>100+</strong><span>dental clinics we manage</span></div><div><strong data-count>30+</strong><span>other industries we look after</span></div><div><strong data-count>2015</strong><span>the year we started</span></div></div>""" if stats else ""
    return f"""<div class="trust-strip reveal">
  {st}{bl}
</div>"""

def partner_strip(R):
    items = PARTNERS or ([{"name": f"Partner logo {i}", "logo": ""} for i in range(1, 7)] if PREVIEW else [])
    if not items: return ""
    def one(p):
        if p.get("logo"): return f'<li><img src="{R}{esc(p["logo"])}" alt="{esc(p["name"])}" height="36" loading="lazy"></li>'
        return f'<li class="logo-slot">{ph("partner logo")}</li>'
    row = "".join(one(p) for p in items)
    return f'<div class="logo-marquee" aria-label="Partners"><ul class="lm-track">{row}</ul><ul class="lm-track" aria-hidden="true">{row}</ul></div>'

def testimonial_slider(R):
    items = TESTIMONIALS
    if not items:
        if not PREVIEW: return ""
        items = [{"quote": ph("testimonial quote, with written consent"), "name": ph("name"), "role": ph("role"), "practice": ph("practice"), "suburb": ph("suburb"), "photo": ""} for _ in range(3)]
    slides = ""
    for t in items:
        photo = f'<img src="{R}{esc(t["photo"])}" alt="{esc(t["name"])}" width="56" height="56" loading="lazy">' if t.get("photo") else '<span class="t-photo-slot" aria-hidden="true"></span>'
        slides += f'<figure class="t-slide"><blockquote>{t["quote"]}</blockquote><figcaption>{photo}<span><strong>{t["name"]}</strong><small>{t["role"]}, {t["practice"]}, {t["suburb"]}</small></span></figcaption></figure>'
    return f"""<section class="section tight"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:28px"><div class="reveal"><p class="eyebrow">In their words</p><h2 style="margin-top:18px">What clients say.</h2></div>
  <div class="t-controls reveal"><button class="t-btn" data-t-prev aria-label="Previous testimonial">←</button><button class="t-btn" data-t-next aria-label="Next testimonial">→</button></div></div>
  <div class="t-slider reveal" data-slider tabindex="0" aria-label="Client testimonials">{slides}</div>
</div></section>"""

# ---------------------------------------------------------------- work / screenshots
WORK_DIR = os.path.join(ROOT, "static", "assets", "work")
def local_shot(slug, kind):
    p = os.path.join(WORK_DIR, f"{slug}-{kind}.webp")
    return (f"assets/work/{slug}-{kind}.webp", webp_size(p)) if os.path.exists(p) else (None, None)

def mshot(url, kind):
    q = quote(url, safe="")
    if kind == "mobile": return f"https://s0.wp.com/mshots/v1/{q}?w=390&h=844&vpw=390&vph=844"
    if kind == "full": return f"https://s0.wp.com/mshots/v1/{q}?w=1200&h=2400&vpw=1440&vph=2880"
    return f"https://s0.wp.com/mshots/v1/{q}?w=1440&h=900&vpw=1440&vph=900"

def shot_img(R, p, kind, sizes):
    src, dims = local_shot(p["slug"], kind)
    alt = f"{p['name']} website {'mobile ' if kind == 'mobile' else ''}homepage designed by GYA"
    if src:
        return f'<img src="{R}{src}" width="{dims[0]}" height="{dims[1]}" sizes="{sizes}" alt="{esc(alt)}" loading="lazy" decoding="async">'
    w, h = {"mobile": (390, 844), "full": (1200, 2400)}.get(kind, (1440, 900))
    return f'<img src="{mshot(p["url"], kind)}" width="{w}" height="{h}" alt="{esc(alt)}" loading="lazy" decoding="async" data-mshot onerror="this.parentNode.classList.add(\'noimg\')">'

def initials(p): return "".join(w[0] for w in p["name"].replace("'", "").split()[:2]).upper()

def browser(R, p, kind="desktop", scroll=False):
    ph_ = f'<div class="ph" aria-hidden="true"><b>{initials(p)}</b><span>{esc(p["name"])}</span><small>{esc(p["place"])}</small></div>'
    return f"""<div class="mock-browser{' scrolls' if scroll else ''}">
  <div class="mb-bar"><i></i><i></i><i></i><span>{esc(p['name'])}</span></div>
  <div class="mb-screen"{' data-scroll-shot' if scroll else ''}>{ph_}{shot_img(R, p, kind, '(max-width:860px) 92vw, 760px')}</div>
</div>"""

def phone(R, p):
    return f"""<div class="mock-phone" aria-hidden="true"><div class="mp-screen"><div class="ph"><b>{initials(p)}</b></div>{shot_img(R, p, 'mobile', '180px')}</div></div>"""

def project_carousel(R=""):
    def card(p, hidden=False):
        ti = ' tabindex="-1"' if hidden else ""
        return f"""<article class="pcard">
  <div class="pcard-media">{browser(R, p)}</div>
  <div class="pcard-info">
    <h3><a class="pcard-link" href="{R}success-stories.html#{p['slug']}"{ti}>{esc(p['name'])}</a></h3>
    <p class="pcard-place">{esc(p['place'])}</p>
    <p class="work-tags">{esc(p['tags'])}</p>
    <p class="pcard-blurb">{p['short']}</p>
    <p class="pcard-actions"><span class="link">Read the story</span></p>
  </div>
</article>"""
    a = "".join(card(p) for p in PROJECTS)
    b = "".join(card(p, True) for p in PROJECTS)
    return f"""<div class="pcar" data-marquee aria-label="Recent websites">
  <div class="pcar-track"><div class="pcar-set">{a}</div><div class="pcar-set" aria-hidden="true">{b}</div></div>
</div>"""

def work_rows(R=""):
    out = ""
    for i, p in enumerate(PROJECTS):
        paras = "".join(f"<p>{x}</p>" for x in p["long"])
        out += f"""
<article class="work-row{' flip' if i % 2 else ''} reveal" id="{p['slug']}">
  <div class="work-mock">{browser(R, p)}{phone(R, p)}</div>
  <div class="work-copy">
    <p class="eyebrow">{esc(p['place'])}</p>
    <h2 style="margin:14px 0 6px">{esc(p['name'])}</h2>
    <p class="work-tags">{esc(p['tags'])}</p>
    {paras}
    <p class="work-links"><a class="link" href="{R}success-stories.html#{p['slug']}">Read the story</a></p>
  </div>
</article>"""
    return out

def showcase(key="short", R=""):
    out = '<div class="showcase stagger">'
    for p in PROJECTS:
        blurb = p.get(key) or p["short"]
        out += f"""
<article class="work reveal">
  {browser(R, p)}
  <div class="work-meta"><h3>{esc(p['name'])}</h3><span>{esc(p['place'])}</span></div>
  <p class="work-tags">{esc(p['tags'])}</p>
  <p class="work-blurb">{blurb}</p>
  <p class="work-links"><a class="link" href="{R}success-stories.html#{p['slug']}">Read the story</a></p>
</article>"""
    return out + "</div>"

# ---------------------------------------------------------------- SmileOX board (example data only)
def card(name, ini, tags, rows, bar=True):
    t = "".join(f'<span class="tag {c}">{x}</span>' for c, x in tags)
    r = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return f'<div class="lead-card"><div class="nm"><span>{name}</span><span class="av">{ini}</span></div>{t}<dl>{r}</dl>{"<div class=bar></div>" if bar else ""}</div>'
BOARD = f"""
<div class="board" aria-label="SmileOX lead board, example data">
  <div class="board-top"><b>Leads · Google Ads + Meta</b><div><span class="pill">Sample Dental, Caringbah</span> <span class="pill">All forms</span> <span class="pill">Journeys (1)</span></div></div>
  <div class="kpis">
    <div class="kpi"><small>Avg first response</small><strong class="good">48s</strong></div>
    <div class="kpi"><small>Within 5 min</small><strong class="good">91%</strong></div>
    <div class="kpi"><small>Booked this month</small><strong>37</strong></div>
    <div class="kpi"><small>Needs a human</small><strong class="warn">4</strong></div>
  </div>
  <div class="cols">
    <div class="col" style="--c:#f0565c"><p class="col-h">Hot<small>6 leads · call now</small></p>
      {card("J. Mitchell","JM",[("hot","Implants"),("ai","AI scored"),("ok","52s")],[("Source","Google Ads"),("Suburb","Miranda"),("Wants","Consult this week")])}
      {card("P. Nguyen","PN",[("hot","Invisalign"),("ok","1m 04s")],[("Source","Meta"),("Suburb","Cronulla"),("Wants","Finance options")])}
    </div>
    <div class="col" style="--c:#f5a25a"><p class="col-h">Warm<small>14 leads · in nurture</small></p>
      {card("S. Okafor","SO",[("warm","Whitening"),("ai","Day 3 of 14")],[("Source","Website"),("Suburb","Gymea"),("Last","Opened email")])}
      {card("L. Romano","LR",[("warm","Check-up"),("ai","Missed call")],[("Source","Phone"),("Text-back","Sent 41s"),("Last","No reply yet")])}
    </div>
    <div class="col" style="--c:#18a35d"><p class="col-h">Booked<small>37 this month</small></p>
      {card("A. Haddad","AH",[("ok","Booked Thu 2:30"),("hot","Crown")],[("Source","Google Ads"),("Value","$1,800"),("Handled by","Front desk")],False)}
      {card("T. Walker","TW",[("ok","Booked Mon 9:00"),("warm","Clean")],[("Source","Local SEO"),("Value","$240"),("Handled by","SmileOX")],False)}
    </div>
    <div class="col" style="--c:#8a8a8a"><p class="col-h">Cool<small>9 leads · low intent</small></p>
      {card("M. Chen","MC",[("cool","Price only"),("ai","AI scored")],[("Source","Meta"),("Suburb","Out of area"),("Next","Monthly email")],False)}
      {card("R. Singh","RS",[("cool","No response"),("ai","Day 14")],[("Source","Website"),("Tries","SMS x3, email x2"),("Next","Archive")],False)}
    </div>
  </div>
</div>"""

# ---------------------------------------------------------------- icons (inline, no requests)
def icon(name):
    p = {
        "ads": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/><path d="M8 11h6M11 8v6"/>',
        "seo": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
        "web": '<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M3 9h18"/><circle cx="6.5" cy="6.5" r=".6" fill="currentColor"/><circle cx="8.8" cy="6.5" r=".6" fill="currentColor"/>',
        "social": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/>',
        "leads": '<path d="M3 4h18l-7 8.5V19l-4 2v-8.5z"/>',
        "brand": '<path d="m12 3 3 6 6 .9-4.5 4.3 1 6.3L12 17.6 6.5 20.5l1-6.3L3 9.9 9 9z"/>',
        "video": '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m10 9 5 3-5 3z" fill="currentColor"/>',
        "email": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/>',
        "copy": '<path d="M5 6h14M5 10h14M5 14h9M5 18h6"/>',
        "ai": '<path d="M12 3v3M12 18v3M3 12h3M18 12h3"/><rect x="7" y="7" width="10" height="10" rx="2.5"/><path d="M10 12h4"/>',
    }[name]
    return f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

# ---------------------------------------------------------------- markdown (small, enough for blog posts)
def md_inline(t):
    t = esc(t).replace("&#x27;", "'").replace("&quot;", '"')
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2)}"' + (' target="_blank" rel="noopener"' if m.group(2).startswith("http") else "") + f">{m.group(1)}</a>", t)
    return t

def markdown(src):
    out, para, lst, ltype = [], [], [], None
    def flush():
        nonlocal para, lst, ltype
        if para: out.append("<p>" + md_inline(" ".join(para)) + "</p>"); para = []
        if lst: out.append(f"<{ltype}>" + "".join(f"<li>{md_inline(x)}</li>" for x in lst) + f"</{ltype}>"); lst = []; ltype = None
    for line in src.splitlines():
        s = line.strip()
        if not s: flush(); continue
        m = re.match(r"^(#{2,4})\s+(.*)", s)
        if m:
            flush(); lvl = len(m.group(1)); txt = m.group(2)
            hid = re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")
            out.append(f'<h{lvl} id="{hid}">{md_inline(txt)}</h{lvl}>'); continue
        m = re.match(r"^([-*]|\d+\.)\s+(.*)", s)
        if m:
            if para: flush()
            t = "ol" if m.group(1)[0].isdigit() else "ul"
            if ltype and ltype != t: flush()
            ltype = t; lst.append(m.group(2)); continue
        if lst: flush()
        para.append(s)
    flush()
    return "\n".join(out)

def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":"); v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'": v = v[1:-1]
        meta[k.strip()] = {"true": True, "false": False}.get(v, v)
    return meta, m.group(2)

def load_posts():
    posts = []
    folder = os.path.join(ROOT, "content", "blog")
    for f in sorted(os.listdir(folder)):
        if not f.endswith(".md"): continue
        meta, body = front_matter(open(os.path.join(folder, f), encoding="utf-8").read())
        meta["published_d"] = datetime.date.fromisoformat(meta["published"])
        meta["updated_d"] = datetime.date.fromisoformat(meta.get("updated") or meta["published"])
        if meta["published_d"] > TODAY and not PREVIEW: continue          # scheduled
        meta["html"] = markdown(body)
        meta["words"] = len(re.findall(r"\w+", body))
        meta["minutes"] = max(1, round(meta["words"] / 220))
        meta["slug"] = meta.get("slug") or f[:-3]
        posts.append(meta)
    return sorted(posts, key=lambda p: p["published_d"], reverse=True)

def fmt_date(d): return d.strftime("%-d %B %Y")

# ---------------------------------------------------------------- render
pages = []                                  # list of page dicts
def add(**kw): pages.append(kw)

import importlib.util
def run_template(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "templates", name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__.update({k: v for k, v in globals().items() if not k.startswith("__")})
    spec.loader.exec_module(mod)

def main():
    if os.path.exists(OUTDIR): shutil.rmtree(OUTDIR)
    shutil.copytree(os.path.join(ROOT, "static"), OUTDIR, ignore=shutil.ignore_patterns("README.txt", "*.md"))
    run_template("pages")
    run_template("pages_trust")
    run_template("pages_services")
    run_template("blog")

    # SEO overrides (content/seo.json). New pages are added automatically.
    seo_pages = SEO.setdefault("pages", {})
    SEO["_help"] = "Per-page SEO. Edit title, description, og_image (path or URL), canonical (full URL) or noindex. Blank values use the page default. Blog posts take their SEO from the front matter in content/blog."
    changed = False
    for p in pages:
        if p.get("article"): continue
        if p["slug"] not in seo_pages:
            seo_pages[p["slug"]] = {"title": "", "description": "", "og_image": "", "canonical": "", "noindex": False}; changed = True
        o = seo_pages[p["slug"]]
        if o.get("title"): p["title"] = o["title"]
        if o.get("description"): p["desc"] = o["description"]
        if o.get("og_image"): p["og_image"] = o["og_image"]
        if o.get("canonical"): p["canonical"] = o["canonical"]
        if o.get("noindex"): p["noindex"] = True
    if changed and not PREVIEW:
        json.dump(SEO, open(SEO_PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    titles = {}
    for p in pages:
        _CUR["slug"] = p["slug"]
        R = "../" * p["slug"].count("/")
        body = p["body"](R) if callable(p["body"]) else p["body"]
        doc = head(p, R) + body + foot(R)
        for bad in ("—", "–"):
            assert bad not in doc, f"dash found in {p['slug']}"
        assert len(p["desc"]) <= 160, f"description too long on {p['slug']} ({len(p['desc'])})"
        assert p["title"] not in titles, f"duplicate title: {p['slug']} and {titles.get(p['title'])}"
        titles[p["title"]] = p["slug"]
        path = os.path.join(OUTDIR, p["slug"]); os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(doc)

    # sitemap: indexable pages only
    def loc(s): return SITE + "/" + ("" if s == "index.html" else s)
    urls = ""
    for p in pages:
        if p.get("noindex") or p.get("canonical"): continue
        lm = p.get("lastmod", TODAY).isoformat()
        urls += f"<url><loc>{loc(p['slug'])}</loc><lastmod>{lm}</lastmod></url>"
    open(os.path.join(OUTDIR, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    robots = "User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n"
    open(os.path.join(OUTDIR, "robots.txt"), "w").write(robots)

    # vercel.json (redirects + caching). Lives at the repo root.
    if not PREVIEW:
        vercel = {"outputDirectory": "dist", "cleanUrls": False, "trailingSlash": False,
                  "redirects": [{"source": r["from"], "destination": r["to"], "permanent": r.get("permanent", True)} for r in REDIRECTS],
                  "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
                              {"source": "/(css|js)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400, must-revalidate"}]}]}
        json.dump(vercel, open(os.path.join(ROOT, "vercel.json"), "w"), indent=2)

    # checklist of open placeholders
    if PREVIEW:
        seen, lines = set(), ["# Open [[CLIENT TO PROVIDE]] slots (generated by build.py --preview)", ""]
        for slug, label in PLACEHOLDERS:
            if (slug, label) in seen: continue
            seen.add((slug, label)); lines.append(f"- {slug or 'home and about pages'}: {label}")
        open(os.path.join(ROOT, "PLACEHOLDERS.md"), "w").write("\n".join(lines) + "\n")

    idx = [p["slug"] for p in pages if not p.get("noindex")]
    print(f"{'PREVIEW' if PREVIEW else 'PRODUCTION'} build: {len(pages)} pages, {len(idx)} indexable -> {os.path.relpath(OUTDIR, ROOT)}/")
    for p in pages: print(("  " if not p.get("noindex") else "  [noindex] ") + p["slug"])

if __name__ == "__main__":
    main()
