# New E-E-A-T pages: team, success stories, awards, expertise, privacy, terms.
# Everything is driven by content/*.json. Empty fields render nothing in production
# and a [[CLIENT TO PROVIDE]] slot in the preview build.

CALL = f'<a class="btn" href="tel:{PHONE}"><span class="dot"></span>Call {PHONE_TXT}</a>'
UPDATED = "12 October 2026"

def hero(R, crumbs, eyebrow, h1, lead, extra=""):
    return f"""<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">{eyebrow}</p>
  <h1 style="margin-top:22px">{h1}</h1>
  <p class="lead">{lead}</p>{extra}
</div></section>"""

# ================================================================ TEAM
def founder_profile(R, p, flip=False):
    paras = "".join(f"<p>{x}</p>" for x in p.get("profile", []))
    chips = "".join(f"<li>{esc(x)}</li>" for x in p.get("expertise", []))
    facts = []
    if p["slug"] == "rowayne":
        facts += [("Before GYA", "Store manager at Myer, running multiple stores across NSW, a bit over $60m between them"), ("At GYA", "Founder, since 2015")]
    if p["slug"] == "brett":
        facts += [("Before GYA", "General Manager at Myer, NSW and ACT, a store portfolio worth over $1b"), ("At GYA", "Co-founder, since 2015")]
    for key, label in [("years_experience", "Years in marketing"), ("qualifications", "Qualifications"), ("specialities", "Specialities")]:
        v = p.get(key)
        if v: facts.append((label, esc(v)))
        elif PREVIEW: facts.append((label, ph(f"{p['name']}: {label.lower()}")))
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    li = f'<a class="link" href="{esc(p["linkedin"])}" target="_blank" rel="noopener me">LinkedIn profile</a>' if p.get("linkedin") else ph(f"{p['name']}: LinkedIn URL")
    return f"""<article class="founder{' flip' if flip else ''}" id="{p['slug']}">
  <div class="founder-photo reveal">{img(R, p['photo'], f"{p.get('full_name') or p['name']}, {p['role']} at GYA", "(max-width:860px) 92vw, 460px")}</div>
  <div class="founder-copy reveal">
    <p class="eyebrow">{esc(p['role'])}</p>
    <h2 style="margin:14px 0 18px">{esc(p.get('full_name') or p['name'])}</h2>
    <div class="story">{paras}</div>
    <dl class="facts">{dl}</dl>
    <ul class="chips" aria-label="Areas of expertise">{chips}</ul>
    <p style="margin-top:22px">{li}</p>
  </div>
</article>"""

def team_body(R):
    crumbs = [("Home", "index.html"), ("About", "about.html"), ("Team", "team.html")]
    founders = [p for p in TEAM if p.get("founder")]
    others = [p for p in TEAM if not p.get("founder")]
    profiles = "".join(founder_profile(R, p, i % 2 == 1) for i, p in enumerate(founders))
    cards = "".join(f"""<article class="member reveal"><div class="pic">{img(R, p['photo'], p.get('full_name') or p['name'], '(max-width:640px) 46vw, 280px')}</div><h3>{esc(p.get('full_name') or p['name'])}</h3><p class="role">{esc(p['role'])}</p></article>""" for p in others)
    if not cards and PREVIEW:
        cards = "".join(f'<article class="member"><div class="pic member-slot"></div><h3>{ph("team member name")}</h3><p class="role">{ph("role")}</p></article>' for _ in range(6))
    grid = f'<div class="members stagger">{cards}</div>' if cards else ""
    return hero(R, crumbs, "Team", "The people you'll actually deal with.",
                "Two founders who came out of Myer, and more than 40 people doing the work in house. Nobody gets handed to someone they've never met.") + f"""
<section class="section tight"><div class="wrap">
  <figure class="photo-band reveal" data-parallax-wrap>{img(R, SET['images']['office_team'], "Brett and Rowayne with a GYA team member reviewing work in the office", "(max-width:1280px) 100vw, 1200px", "parallax-img", eager=True)}<figcaption>Brett and Rowayne with the team.</figcaption></figure>
</div></section>
<section class="section tight"><div class="wrap">{profiles}</div></section>
<section class="section dark"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">The team</p><h2 style="margin-top:18px">Over 40 of us, and they become part of your family too.</h2></div>
    <div class="reveal story">
      <p>Behind Rowayne and Brett there's a team of more than 40: ads specialists, SEO, designers, developers, video, copywriters, and the account managers who'll be on your fortnightly call. You're not handed off to a junior after you sign. The people who build your plan are the people who run it, and most of our clients end up knowing them by name.</p>
      <p>Everything is done in house. No white labelling, no reselling somebody else's platform, no work quietly sent elsewhere and marked up.</p>
    </div>
  </div>
  {grid}
</div></section>
{cta("Say hello.", "We pick up the phone.", "Twenty minutes, no deck. We'll look at what you're spending, where it's going, and what your site and your Google listing are doing, then tell you which of them is costing you the most right now.", photo=True, R=R)}
"""

add(slug="team.html", title="Our Team | Rowayne Kapugama and Brett Dyson, GYA Founders",
    desc="Meet Rowayne Kapugama and Brett Dyson, the ex-Myer founders of Generate Your Audience, and the 40+ in-house team behind GYA's dental and local marketing.",
    crumbs=[("Home", "index.html"), ("About", "about.html"), ("Team", "team.html")], nav="about.html",
    schema=[{"@type": "AboutPage", "@id": SITE + "/team.html", "url": SITE + "/team.html", "name": "Team",
             "about": {"@id": ORG_ID}, "mentions": [{"@id": f"{SITE}/team.html#{p['slug']}"} for p in TEAM]}],
    body=team_body)

# ================================================================ SUCCESS STORIES
PROJ = {p["slug"]: p for p in PROJECTS}
def story_block(R, s, i):
    proj = PROJ.get(s.get("project")) or {"slug": s["slug"], "name": s["client"], "place": s["place"], "url": s.get("url", ""), "host": re.sub(r"^https?://(www\.)?", "", s.get("url", "")).rstrip("/")}
    media = f'<div class="work-mock">{browser(R, proj)}</div>' if proj.get("url") else ""
    parts = ""
    if s.get("story"):
        parts += '<h3 class="cs-h">The story</h3>' + "".join(f"<p>{x}</p>" for x in s["story"])
    if s.get("challenge"): parts += f'<h3 class="cs-h">What they needed</h3><p>{s["challenge"]}</p>'
    if s.get("what_we_did"): parts += f'<h3 class="cs-h">What we did</h3><p>{s["what_we_did"]}</p>'
    res = s.get("results") or []
    if res:
        stats = "".join(f'<div class="stat"><strong data-count>{esc(r["value"])}</strong><span>{esc(r["label"])}{(" · " + esc(r["period"])) if r.get("period") else ""}</span></div>' for r in res)
        parts += f'<h3 class="cs-h">What changed</h3><div class="cs-results">{stats}</div>'
    elif PREVIEW:
        parts += '<h3 class="cs-h">What changed</h3><div class="cs-results">' + "".join(f'<div class="stat"><strong>{ph("result")}</strong><span>{ph("metric, period and source")}</span></div>' for _ in range(3)) + "</div>"
    t = s.get("testimonial")
    if t:
        photo = f'<img src="{R}{esc(t["photo"])}" alt="{esc(t["name"])}" width="56" height="56" loading="lazy">' if t.get("photo") else ""
        parts += f'<figure class="cs-quote"><blockquote>{esc(t["quote"])}</blockquote><figcaption>{photo}<span><strong>{esc(t["name"])}</strong><small>{esc(t["role"])}, {esc(t["practice"])}, {esc(t["suburb"])}</small></span></figcaption></figure>'
    elif PREVIEW:
        parts += f'<figure class="cs-quote"><blockquote>{ph("named testimonial, with written consent")}</blockquote><figcaption><span><strong>{ph("name")}</strong><small>{ph("role, practice, suburb")}</small></span></figcaption></figure>'
    links = ""
    if s.get("url"): links += f'<a class="link" href="{esc(s["url"])}" target="_blank" rel="noopener">Visit site</a>'
    if s.get("project"): links += f'<a class="link" href="{R}work.html#{s["project"]}">See the build</a>'
    contact = f' · {esc(s["contact"])}' if s.get("contact") else ""
    return f"""<article class="cs{' flip' if i % 2 else ''}" id="{s['slug']}">
  <div class="cs-media reveal">{media}</div>
  <div class="cs-copy reveal">
    <p class="eyebrow">{esc(s['place'])}{contact}</p>
    <h2 style="margin:14px 0 6px">{esc(s['client'])}</h2>
    <p class="work-tags">{esc(s['tags'])}</p>
    {parts}
    <p class="work-links">{links}</p>
  </div>
</article>"""

def stories_body(R):
    crumbs = [("Home", "index.html"), ("Success stories", "success-stories.html")]
    jump = "".join(f'<a href="#{s["slug"]}">{esc(s["client"])}</a>' for s in STORIES)
    return hero(R, crumbs, "Success stories", "What they needed, what we did, what changed.",
                "We only publish numbers and quotes the client has signed off on. Everything else on this page is just what happened.",
                f'<nav class="jump" aria-label="Stories on this page">{jump}</nav>') + f"""
<section class="section dark"><div class="wrap">{''.join(story_block(R, s, i) for i, s in enumerate(STORIES))}</div></section>
{cta("Want to be the next one on this page?", "Tell us about your business. You'll get a plan, a timeline and a straight answer about whether we're the right fit.", R=R)}
"""

add(slug="success-stories.html", title="Success Stories | Dental and Local Marketing Results | GYA",
    desc="How GYA helped The Caringbah Dentists, My Dentist, Tooth n Care, Horizon Dental, Artarmon Dentists and more. What they needed and what we did.",
    crumbs=[("Home", "index.html"), ("Success stories", "success-stories.html")], nav="work.html",
    schema=[{"@type": "CollectionPage", "@id": SITE + "/success-stories.html", "name": "Success stories", "about": {"@id": ORG_ID}}],
    body=stories_body)

# ================================================================ AWARDS
def awards_body(R):
    crumbs = [("Home", "index.html"), ("Awards and certifications", "awards.html")]
    groups = ""
    for kind, title in [("award", "Awards"), ("certification", "Certifications"), ("partnership", "Partnerships")]:
        items = [a for a in AWARDS if a.get("type") == kind]
        cards = ""
        for a in items:
            badge = f'<img src="{R}{esc(a["badge"])}" alt="{esc(a["name"])} badge" height="64" loading="lazy">' if a.get("badge") else ""
            proof = f'<a class="link" href="{esc(a["url"])}" target="_blank" rel="noopener">Verify</a>' if a.get("url") else ""
            cards += f'<article class="award reveal">{badge}<h3>{esc(a["name"])}</h3><p class="muted">{esc(a.get("issuer", ""))}{(" · " + esc(a["year"])) if a.get("year") else ""}</p>{proof}</article>'
        if not cards and PREVIEW:
            names = {"award": ["Industry award"], "certification": ["Google Partner", "Meta Business Partner", "Microsoft Advertising Partner"], "partnership": ["Technology or industry partner"]}[kind]
            cards = "".join(f'<article class="award award-slot"><div class="badge-slot" aria-hidden="true"></div><h3>{n}</h3><p>{ph(n + ": only display once confirmed, with proof link")}</p></article>' for n in names)
        if cards: groups += f'<div class="award-group"><h2 class="reveal">{title}</h2><div class="awards stagger">{cards}</div></div>'
    if not groups:
        groups = '<p class="lead">Nothing listed yet. We only add things here once we hold them and can link to the proof.</p>'
    return hero(R, crumbs, "Awards and certifications", "Awards, certifications and partnerships.",
                "We only list things we actually hold, and each one links to somewhere you can check it.") + f"""
<section class="section tight"><div class="wrap">{groups}</div></section>
{cta(R=R)}
"""

add(slug="awards.html", title="Awards, Certifications and Partnerships | GYA",
    desc="The awards, platform certifications and partnerships Generate Your Audience holds, each with a link so you can check it yourself.",
    crumbs=[("Home", "index.html"), ("Awards and certifications", "awards.html")], nav="about.html",
    noindex=not AWARDS, body=awards_body)

# ================================================================ EXPERTISE
SERVICES = [
    ("ads", "Google Ads", "Search, Shopping, Performance Max and YouTube, built per service and per suburb, tracked to the enquiry rather than the click.", "dental-marketing.html", "rowayne"),
    ("seo", "SEO and local SEO", "The map listing first, because that's where the clicks are, then the technical work and the content underneath it.", "dental-marketing.html", "rowayne"),
    ("web", "Websites", "Fast, mobile first, built to rank and to convert. You own everything.", "dental-websites.html", "rowayne"),
    ("social", "Social media", "Meta, Instagram, TikTok and LinkedIn. Paid and organic, with creative shot at your business rather than pulled from a stock library.", "marketing.html", "rowayne"),
    ("leads", "Lead generation", "SmileOX answers, qualifies and scores every enquiry, so your team only speaks to people ready to buy.", "smileox.html", "rowayne"),
    ("brand", "Branding and design", "Identity, print, signage and ad creative, so the site and the sign out the front look like the same business.", "marketing.html", "rowayne"),
    ("video", "Video", "Brand films, website banners and social content, shot and edited by us.", "marketing.html", "rowayne"),
    ("email", "Email and SMS", "Automations, recall and reactivation.", "marketing.html", "rowayne"),
    ("copy", "Content and copywriting", "Website copy, service pages, blogs and ad copy that sounds like a person wrote it.", "marketing.html", "rowayne"),
]
def reviewer(R, slug):
    p = PEOPLE.get(slug)
    return f'<p class="reviewed">Strategy reviewed by <a href="{R}team.html#{slug}">{esc(p.get("full_name") or p["name"])}</a></p>' if p else ""

def expertise_body(R):
    crumbs = [("Home", "index.html"), ("Expertise", "expertise.html")]
    cards = "".join(f'<article class="card x-card reveal">{icon(i)}<h3><a href="{R}{u}">{t}</a></h3><p>{d}</p>{reviewer(R, who)}</article>' for i, t, d, u, who in SERVICES)
    specialists = ph("specialist lead for each service (name and team profile)", True) if PREVIEW else ""
    return hero(R, crumbs, "Expertise", "What we know, and who's accountable for it.",
                "Nine services, all in house. Seven years in dental. And the AI search and lead follow-up work most agencies haven't started yet. Here's where each one lives, and who checks it.") + f"""
<section class="section tight"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">The specialty</p><h2 style="margin-top:18px">Dental, for more than 100 clinics.</h2></div>
    <div class="reveal story">
      <p>Google Ads, local SEO, Meta and SmileOX, all wired together so no enquiry goes cold. We do this for more than 100 clinics and we've been doing it for seven years.</p>
      <p>Built per treatment, per suburb, and written to the AHPRA guidelines before it goes live.</p>
      <p class="work-links"><a class="link" href="{R}dental-marketing.html">Dental marketing</a><a class="link" href="{R}dental-websites.html">Dental websites</a></p>
    </div>
  </div>
</div></section>
<section class="section dark"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:clamp(32px,5vw,56px)">
    <div class="reveal"><p class="eyebrow">Everything we do</p><h2 style="margin-top:18px">Nine things. All of them in house.</h2></div>
    <div class="reveal"><a class="link" href="{R}marketing.html">See how we do all of it</a></div>
  </div>
  <div class="grid g3 stagger">{cards}</div>
  {specialists}
</div></section>
<section class="section"><div class="wrap">
  <div class="grid g2">
    <div class="card reveal">{icon('ai')}<h3><a href="{R}ai-marketing.html">AI search</a></h3><p>Search is changing faster than most agencies will admit. Here's how we see it, what it means for you, and what we're already doing about it.</p>{reviewer(R, 'rowayne')}</div>
    <div class="card reveal">{icon('leads')}<h3><a href="{R}smileox.html">SmileOX</a></h3><p>We built SmileOX because our ads were generating leads faster than front desks could answer them. It replies instantly, nurtures automatically and scores every lead by treatment value. Weekends and after hours included.</p>{reviewer(R, 'rowayne')}</div>
  </div>
</div></section>
<section class="section tight"><div class="wrap">
  <div class="split">
    <div class="reveal"><p class="eyebrow">Who checks what</p><h2 style="margin-top:18px">Every area has a name against it.</h2></div>
    <ul class="list reveal">
      <li><strong><a href="{R}team.html#rowayne">Rowayne</a></strong><p>Sets the strategy on every account: which services, which suburbs, what the budget goes on and what it should be returning by when.</p></li>
      <li><strong><a href="{R}team.html#brett">Brett</a></strong><p>Runs client success, which mostly means making sure the fortnightly calls actually happen and that nobody is being quietly managed by a monthly report.</p></li>
    </ul>
  </div>
</div></section>
{cta(R=R)}
"""

add(slug="expertise.html", title="Expertise | Dental Marketing, Google Ads, SEO and AI Search | GYA",
    desc="The nine services GYA runs in house, seven years of dental marketing, AI search and SmileOX, and the person accountable for each one.",
    crumbs=[("Home", "index.html"), ("Expertise", "expertise.html")], nav="about.html",
    schema=[{"@type": "ItemList", "name": "GYA services", "itemListElement": [{"@type": "ListItem", "position": n + 1, "name": t, "url": f"{SITE}/{u}"} for n, (_, t, _d, u, _w) in enumerate(SERVICES)]}],
    body=expertise_body)

# ================================================================ LEGAL
def legal_page(R, crumbs, eyebrow, h1, intro, sections):
    toc = "".join(f'<li><a href="#{sid}">{t}</a></li>' for sid, t, _ in sections)
    secs = "".join(f'<section id="{sid}"><h2>{t}</h2>{b}</section>' for sid, t, b in sections)
    note = '<div class="ph-chip" style="display:block;margin-top:18px">Template. Needs review by your lawyer before launch.</div>' if PREVIEW else ""
    return f"""<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">{eyebrow}</p>
  <h1 style="margin-top:22px">{h1}</h1>
  <p class="muted" style="margin-top:14px">Last updated {UPDATED}</p>
  <p class="lead" style="margin-top:14px">{intro}</p>{note}
</div></section>
<section class="section tight"><div class="wrap legal">
  <nav class="legal-toc" aria-label="On this page"><p class="eyebrow">On this page</p><ol>{toc}</ol></nav>
  <div class="prose">{secs}</div>
</div></section>"""

def contact_lines():
    o = PRIMARY
    addr = esc(office_lines(o)) if o else ph("street address, suburb, NSW, postcode")
    return f"<p>{esc(SET['legal_name'])}{(' (ABN ' + esc(SET['abn']) + ')') if SET.get('abn') else ''}<br>Attention: Privacy Officer<br>{addr}<br>Phone: <a href=\"tel:{PHONE}\">{PHONE_TXT}</a><br>Email: <a href=\"mailto:{EMAIL}\">{EMAIL}</a></p>"

def privacy_body(R):
    overseas = ph("countries where your providers store data, for example the United States") if PREVIEW else "including the United States"
    S = [
     ("who", "Who we are", f"<p>This policy explains how {esc(SET['legal_name'])} (GYA, we, us) collects, uses, holds and discloses personal information. We're bound by the <em>Privacy Act 1988</em> (Cth) and the Australian Privacy Principles (APPs).</p>{contact_lines()}"),
     ("collect", "What we collect", """<p>We only collect what we need. Depending on how you deal with us, that can include:</p>
<ul><li><strong>Contact form and enquiries:</strong> your name, business name, email address, mobile number, what you need help with, and anything you tell us in your message.</li>
<li><strong>Phone calls:</strong> your phone number and the time and length of the call. Where we use call tracking on our own campaigns, we may also record calls for quality and training, and we'll tell you at the start of the call if it's being recorded.</li>
<li><strong>Clients:</strong> contact details for the people we work with, billing details, and access details for the ad accounts, websites and listings you ask us to manage.</li>
<li><strong>Website use:</strong> information about how you use our website, such as pages visited, device and browser type, approximate location and the site that referred you. This is collected through analytics and advertising tools such as Google Analytics 4, Google Ads and the Meta Pixel, where they're enabled.</li>
<li><strong>Automated visits:</strong> we use Live Agent Watch to see when automated tools and AI agents visit the site. For each page request it receives the time, the page address with anything identifying removed, your IP address, browser type and country. It doesn't use cookies.</li>
<li><strong>SmileOX lead data:</strong> when we run SmileOX for a client, it handles the enquiries that client's own customers send, such as names, contact details and what they're enquiring about. We handle that information on our client's behalf and under their instructions, and our client's own privacy policy also applies.</li></ul>
<p>We don't ask for sensitive information, such as health information, through our website. If you include it in a message, we'll only use it to respond to you.</p>"""),
     ("how", "How we collect it", "<p>Mostly directly from you: when you fill in a form, call, email, or work with us. We also collect some information automatically through cookies and similar tools when you use our website, and sometimes from third parties, such as the ad platforms we manage on your behalf.</p><p>You can contact us without giving your name, but it's hard for us to help if we can't get back to you.</p>"),
     ("use", "How we use it", """<ul><li>To respond to your enquiry and give you the information you asked for.</li>
<li>To provide our services, manage your account and send invoices.</li>
<li>To run, measure and improve our website and our own advertising.</li>
<li>To send you updates about our services, if you've agreed to that. Every email has an unsubscribe link, and we follow the <em>Spam Act 2003</em> (Cth).</li>
<li>To meet our legal obligations.</li></ul>"""),
     ("disclose", "Who we share it with", """<p>We don't sell personal information. We share it only where we need to, with:</p>
<ul><li>service providers who help us run the business, such as website hosting, email, cloud storage, analytics, a website monitoring service, advertising platforms and the infrastructure SmileOX runs on</li>
<li>contractors working on your account, under confidentiality obligations</li>
<li>professional advisers such as accountants and lawyers</li>
<li>government bodies or others where the law requires it.</li></ul>"""),
     ("overseas", "Overseas disclosure", f"<p>Some of our service providers store or process information outside Australia, {overseas}. Where we use them, we take reasonable steps to make sure they handle personal information in a way that's consistent with the APPs.</p>"),
     ("cookies", "Cookies and analytics", "<p>Our website uses cookies and similar technology to remember your preferences, understand how the site is used, and measure our advertising. You can block or delete cookies in your browser settings. Some parts of the site may not work as well if you do.</p><p>You can opt out of Google Analytics with Google's browser add-on, and manage ad personalisation in your Google and Meta account settings.</p>"),
     ("security", "Storage and security", "<p>We store personal information electronically with reputable providers and take reasonable steps to protect it from misuse, loss, and unauthorised access, change or disclosure. Access is limited to the people who need it. When we no longer need information for any purpose, we take reasonable steps to destroy or de-identify it.</p><p>If a data breach is likely to cause serious harm, we'll notify you and the Office of the Australian Information Commissioner under the Notifiable Data Breaches scheme.</p>"),
     ("access", "Accessing and correcting your information", "<p>You can ask for a copy of the personal information we hold about you, or ask us to correct it, by contacting us using the details above. We'll respond within 30 days. If we can't give you access, we'll tell you why in writing.</p>"),
     ("complaints", "Complaints", "<p>If you think we've mishandled your personal information, contact our Privacy Officer using the details above. We'll acknowledge your complaint and aim to resolve it within 30 days.</p><p>If you're not happy with our response, you can complain to the Office of the Australian Information Commissioner (OAIC) at <a href=\"https://www.oaic.gov.au\" target=\"_blank\" rel=\"noopener\">oaic.gov.au</a> or on 1300 363 992.</p>"),
     ("changes", "Changes to this policy", "<p>We may update this policy from time to time. The latest version will always be on this page, with the date it was last updated at the top.</p>"),
    ]
    return legal_page(R, [("Home", "index.html"), ("Privacy policy", "privacy-policy.html")], "Legal", "Privacy policy",
                      "Plain version first: we collect what we need to get back to you and do the work, we don't sell it, and you can ask to see or correct it at any time.", S)

def terms_body(R):
    S = [
     ("about", "About these terms", f"<p>These terms apply to your use of this website, run by {esc(SET['legal_name'])}{(' (ABN ' + esc(SET['abn']) + ')') if SET.get('abn') else ''}. By using the site you agree to them. If we work together, the agreement for that work applies to our services. These terms only cover the website.</p>"),
     ("use", "Using the site", "<p>Use the site for lawful purposes only. Don't try to interfere with how it works, get unauthorised access to it, or copy large parts of it by automated means.</p>"),
     ("info", "Information on the site", "<p>Everything on this site is general information. It isn't advice for your specific business, and you should get advice that fits your situation before acting on it.</p><p>Marketing results depend on a lot of things outside anyone's control, including your market, your competitors, your budget and what happens after an enquiry arrives. Stories and results on this site describe what happened for those clients. They aren't a promise of what will happen for you, and we don't guarantee any particular ranking, number of enquiries or return.</p>"),
     ("ip", "Intellectual property", "<p>The content on this site, including the text, design, graphics and the GYA and SmileOX names and logos, belongs to us or the people who licensed it to us. You can view and share pages for your own reference, but you can't copy, change or use the content commercially without our written permission.</p><p>Client websites shown on this site remain the property of their owners.</p>"),
     ("links", "Links to other sites", "<p>We link to other websites, including sites we've built for clients. We don't control those sites and aren't responsible for their content or how they handle your information.</p>"),
     ("acl", "Australian Consumer Law", "<p>Nothing in these terms excludes, restricts or changes any consumer guarantee, right or remedy you have under the Australian Consumer Law or any other law that can't be excluded.</p>"),
     ("liability", "Limiting our liability", "<p>To the extent the law allows, we're not liable for any loss or damage arising from your use of this website or reliance on its content, including indirect or consequential loss.</p><p>Where our liability can't be excluded but can be limited, it's limited to supplying the services again or paying the cost of having them supplied again.</p>"),
     ("privacy", "Privacy", f'<p>Our <a href="{R}privacy-policy.html">privacy policy</a> explains how we handle personal information collected through this site.</p>'),
     ("changes", "Changes", "<p>We may update these terms from time to time. The version on this page applies from the date shown at the top.</p>"),
     ("law", "Governing law", "<p>These terms are governed by the laws of New South Wales, Australia. You and we submit to the non-exclusive jurisdiction of the courts of New South Wales.</p>"),
     ("contact", "Contact", contact_lines().replace("Attention: Privacy Officer<br>", "")),
    ]
    return legal_page(R, [("Home", "index.html"), ("Terms of use", "terms.html")], "Legal", "Terms of use",
                      "The rules for using this website. Short version: use it fairly, it's general information rather than advice, and nobody can promise you marketing results.", S)

add(slug="privacy-policy.html", title="Privacy Policy | Generate Your Audience",
    desc="How Generate Your Audience collects, uses and protects personal information under the Privacy Act 1988 and the Australian Privacy Principles.",
    crumbs=[("Home", "index.html"), ("Privacy policy", "privacy-policy.html")], body=privacy_body)
add(slug="terms.html", title="Terms of Use | Generate Your Audience",
    desc="The terms for using the Generate Your Audience website, including intellectual property, links, liability and the Australian Consumer Law.",
    crumbs=[("Home", "index.html"), ("Terms of use", "terms.html")], body=terms_body)
