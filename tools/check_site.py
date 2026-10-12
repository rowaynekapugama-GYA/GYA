#!/usr/bin/env python3
"""Checks a built site: internal links and anchors, JSON-LD, headings, meta, dashes, placeholders.
   python3 tools/check_site.py dist"""
import os, re, sys, json
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
D = sys.argv[1] if len(sys.argv) > 1 else "dist"
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.ids=set(); s.h1=0; s.ld=[]; s._ld=False; s.meta={}; s.title=""; s._t=False; s.imgs_noalt=0
    def handle_starttag(s,t,a):
        a=dict(a)
        if "id" in a: s.ids.add(a["id"])
        for k in ("href","src"):
            if k in a and a[k]: s.links.append(a[k])
        if t=="h1": s.h1+=1
        if t=="img" and "alt" not in a: s.imgs_noalt+=1
        if t=="script" and a.get("type")=="application/ld+json": s._ld=True; s.ld.append("")
        if t=="meta" and a.get("name") in ("description","robots"): s.meta[a["name"]]=a.get("content","")
        if t=="link" and a.get("rel")=="canonical": s.meta["canonical"]=a.get("href")
        if t=="title": s._t=True
    def handle_endtag(s,t):
        if t=="script": s._ld=False
        if t=="title": s._t=False
    def handle_data(s,d):
        if s._ld: s.ld[-1]+=d
        if s._t: s.title+=d
pages={}
for root,_,files in os.walk(D):
    for f in files:
        if f.endswith(".html"):
            path=os.path.join(root,f); rel=os.path.relpath(path,D)
            p=P(); txt=open(path,encoding="utf-8").read(); p.feed(txt); p.txt=txt; pages[rel]=p
errors=[]
for rel,p in pages.items():
    if p.h1!=1: errors.append(f"{rel}: {p.h1} h1 tags")
    if p.imgs_noalt: errors.append(f"{rel}: {p.imgs_noalt} images without alt")
    if "—" in p.txt or "–" in p.txt: errors.append(f"{rel}: em/en dash")
    if "CLIENT TO PROVIDE" in p.txt and "preview" not in D: errors.append(f"{rel}: placeholder in production")
    for blob in p.ld:
        try: json.loads(blob)
        except Exception as e: errors.append(f"{rel}: bad JSON-LD {e}")
    for l in p.links:
        u=urlparse(l)
        if u.scheme in ("http","https","mailto","tel","data") or l.startswith("//"): continue
        if l == "/data/fdd80dd6-export": continue   # Live Agent Watch canary, meant to 404
        target=unquote(u.path); frag=u.fragment
        if not target:
            if frag and frag not in p.ids and frag not in ("main","talk"): errors.append(f"{rel}: missing anchor #{frag}")
            continue
        tp=os.path.normpath(os.path.join(os.path.dirname(rel),target))
        if not os.path.exists(os.path.join(D,tp)): errors.append(f"{rel}: broken link {l}"); continue
        if frag and tp in pages and frag not in pages[tp].ids: errors.append(f"{rel}: missing anchor {l}")
titles={}; descs={}
for rel,p in pages.items():
    titles.setdefault(p.title,[]).append(rel); descs.setdefault(p.meta.get("description"),[]).append(rel)
    if not p.meta.get("description"): errors.append(f"{rel}: no description")
    if not p.meta.get("canonical"): errors.append(f"{rel}: no canonical")
for k,v in list(titles.items())+list(descs.items()):
    if len(v)>1: errors.append(f"duplicate title/description: {v}")
print(f"{len(pages)} pages checked in {D}")
print("\n".join(errors) if errors else "No problems found.")
sys.exit(1 if errors else 0)
