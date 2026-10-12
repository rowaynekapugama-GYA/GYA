# Blog index and articles, generated from content/blog/*.md
POSTS = load_posts()
PER_PAGE = 9

def by(p):
    a = PEOPLE.get(p.get("author", ""))
    return a

def post_url(p): return f"blog/{p['slug']}.html"

def post_card(R, p, eager=False, h="h3"):
    a = by(p)
    draft = '<span class="draft-chip">Draft</span>' if (PREVIEW and p.get("draft")) else ""
    return f"""<article class="post-card reveal">
  <a class="pc-img" href="{R}{post_url(p)}" tabindex="-1" aria-hidden="true">{img(R, p['image'], p.get('image_alt', ''), '(max-width:640px) 92vw, (max-width:1050px) 46vw, 380px', eager=eager)}</a>
  <p class="pc-meta"><span class="pc-cat">{esc(p['category'])}</span>{draft}<span>{p['minutes']} min read</span></p>
  <{h} class="pc-title"><a href="{R}{post_url(p)}">{esc(p['title'])}</a></{h}>
  <p class="pc-excerpt">{esc(p['excerpt'])}</p>
  <p class="pc-by">{esc(a.get('full_name') or a['name']) if a else ''} · <time datetime="{p['published_d'].isoformat()}">{fmt_date(p['published_d'])}</time></p>
</article>"""

def index_slug(n): return "blog.html" if n == 1 else f"blog-page-{n}.html"

pages_n = max(1, -(-len(POSTS) // PER_PAGE))
for n in range(1, pages_n + 1):
    chunk = POSTS[(n - 1) * PER_PAGE: n * PER_PAGE]
    cats = sorted({p["category"] for p in POSTS})
    def body(R, chunk=chunk, n=n, cats=cats):
        crumbs = [("Home", "index.html"), ("Blog", "blog.html")]
        chips = "".join(f'<li>{esc(c)}</li>' for c in cats)
        prev_ = f'<a class="btn ghost" rel="prev" href="{R}{index_slug(n-1)}">Newer posts</a>' if n > 1 else ""
        next_ = f'<a class="btn ghost" rel="next" href="{R}{index_slug(n+1)}">Older posts</a>' if n < pages_n else ""
        pager = f'<nav class="pager" aria-label="Blog pages">{prev_}<span>Page {n} of {pages_n}</span>{next_}</nav>' if pages_n > 1 else ""
        cards = "".join(post_card(R, p, eager=(i == 0 and n == 1), h="h2") for i, p in enumerate(chunk)) or '<p class="lead">First posts are on the way.</p>'
        return f"""<section class="page-hero"><div class="wrap">
  {crumbs_html(R, crumbs)}
  <p class="eyebrow">Blog</p>
  <h1 style="margin-top:22px">Notes from the agency.</h1>
  <p class="lead">Plain answers on Google Ads, local SEO, websites, AI search and lead follow-up. Written by the people who do the work.</p>
  <ul class="chips" aria-label="Topics" style="margin-top:24px">{chips}</ul>
</div></section>
<section class="section tight"><div class="wrap">
  <div class="post-grid stagger">{cards}</div>
  {pager}
</div></section>
{cta(R=R)}"""
    head_extra = ""
    if n > 1: head_extra += f'<link rel="prev" href="{SITE}/{index_slug(n-1)}">\n'
    if n < pages_n: head_extra += f'<link rel="next" href="{SITE}/{index_slug(n+1)}">\n'
    add(slug=index_slug(n), title="Blog | Dental Marketing, Local SEO and AI Search Notes | GYA" + (f" | Page {n}" if n > 1 else ""),
        desc="Plain answers on Google Ads, local SEO, dental websites, AI search and lead follow-up, written by the GYA team who do the work every day.",
        crumbs=[("Home", "index.html"), ("Blog", "blog.html")], nav="blog.html", head_extra=head_extra,
        schema=[{"@type": "Blog", "@id": SITE + "/blog.html", "name": "GYA Blog", "publisher": {"@id": ORG_ID},
                 "blogPost": [{"@id": f"{SITE}/{post_url(p)}#article"} for p in chunk]}],
        body=body)

for p in POSTS:
    a = by(p)
    rv = PEOPLE.get(p.get("reviewed_by", ""))
    url = f"{SITE}/{post_url(p)}"
    related = [q for q in POSTS if q is not p][:2]
    def body(R, p=p, a=a, rv=rv, related=related):
        crumbs = [("Home", "index.html"), ("Blog", "blog.html"), (p["title"], post_url(p))]
        draft = '<div class="ph-chip" style="display:block;margin-bottom:18px">DRAFT FOR SEO TEAM REVIEW. Set draft: false in the front matter to publish and index it.</div>' if (PREVIEW and p.get("draft")) else ""
        aphoto = img(R, a["photo"], a.get("full_name") or a["name"], "48px", "byline-photo") if a else ""
        upd = f' · Updated <time datetime="{p["updated_d"].isoformat()}">{fmt_date(p["updated_d"])}</time>' if p["updated_d"] != p["published_d"] else f' · Last updated <time datetime="{p["updated_d"].isoformat()}">{fmt_date(p["updated_d"])}</time>'
        rel = "".join(post_card(R, q) for q in related)
        relsec = f'<section class="section tight"><div class="wrap"><h2 class="reveal" style="margin-bottom:28px">Keep reading</h2><div class="post-grid two stagger">{rel}</div></div></section>' if rel else ""
        reviewed = f'<p class="reviewed">Reviewed by <a href="{R}team.html#{rv["slug"]}">{esc(rv.get("full_name") or rv["name"])}</a>, {esc(rv["role"])}</p>' if rv else ""
        return f"""<article class="post">
<header class="page-hero post-hero"><div class="wrap narrow">
  {crumbs_html(R, crumbs)}
  {draft}<p class="eyebrow">{esc(p['category'])}</p>
  <h1 style="margin-top:22px">{esc(p['title'])}</h1>
  <p class="lead">{esc(p['excerpt'])}</p>
  <div class="byline">{aphoto}<p>By <a href="{R}team.html#{a['slug']}" rel="author">{esc(a.get('full_name') or a['name'])}</a>, {esc(a['role'])}<br>
  <span class="muted">Published <time datetime="{p['published_d'].isoformat()}">{fmt_date(p['published_d'])}</time>{upd} · {p['minutes']} min read</span></p></div>
  {reviewed}
</div></header>
<figure class="post-cover wrap">{img(R, p['image'], p.get('image_alt', ''), '(max-width:1100px) 100vw, 1100px', eager=True)}</figure>
<div class="wrap narrow prose post-body">{p['html']}</div>
<div class="wrap narrow">{author_box(R, a['slug'], 'Written by', p['updated_d'])}</div>
</article>
{relsec}
{cta(R=R)}"""
    og = f"{SITE}/assets/images/{p['image']}-og.jpg" if os.path.exists(os.path.join(IMG_DIR, p["image"] + "-og.jpg")) else img_url(p["image"])
    schema = [{"@type": "BlogPosting", "@id": url + "#article", "headline": p["title"], "description": p["description"],
               "image": [img_url(p["image"]), og], "datePublished": p["published_d"].isoformat(), "dateModified": p["updated_d"].isoformat(),
               "author": {"@type": "Person", "@id": f"{SITE}/team.html#{a['slug']}", "name": a.get("full_name") or a["name"], "url": f"{SITE}/team.html#{a['slug']}"},
               "publisher": {"@id": ORG_ID}, "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "articleSection": p["category"],
               "wordCount": p["words"], "inLanguage": "en-AU", "isPartOf": {"@id": SITE + "/blog.html"}}]
    if rv: schema[0]["reviewedBy"] = {"@id": f"{SITE}/team.html#{rv['slug']}"}
    extra = (f'<meta property="article:published_time" content="{p["published_d"].isoformat()}">\n'
             f'<meta property="article:modified_time" content="{p["updated_d"].isoformat()}">\n'
             f'<meta property="article:author" content="{SITE}/team.html#{a["slug"]}">\n'
             f'<meta property="article:section" content="{esc(p["category"])}">\n')
    add(slug=post_url(p), title=f"{p['title']} | GYA", desc=p["description"], article=True, nav="blog.html",
        crumbs=[("Home", "index.html"), ("Blog", "blog.html"), (p["title"], post_url(p))],
        noindex=bool(p.get("draft")) or bool(p.get("noindex")), canonical=p.get("canonical") or "",
        og_image=p.get("og_image") or og, og_alt=p.get("image_alt", ""), head_extra=extra, schema=schema,
        lastmod=p["updated_d"], body=body)
