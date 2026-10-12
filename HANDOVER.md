# GYA site: handover, 7 October 2026

Approved copy is unchanged. New copy only appears where a new page or section needed it (Team, Success stories, Expertise, Awards, legal pages, three blog drafts), written in the same voice, Australian English, no em dashes. All URLs from the previous build are unchanged.

## Read this first: three decisions I made

1. **Light theme kept.** The brief says to keep the dark #0a0a0a theme, but Rowayne switched the site to light in September and that's the current identity. Everything here is built on the light version. Dark would be a theme change, not a modernisation, so I'd confirm with him before going back.
2. **No AI images of Rowayne and Brett yet.** Reasons: generating their likeness needs both of them to agree to it, the image tools need the reference photos uploaded by hand, and staged AI scenes of real people sit awkwardly next to an E-E-A-T push and the "don't fabricate anything that affects trust" rule. There's already a real photo of Rowayne, Brett and a team member in the office, and real photos beat AI ones for trust, so that's what I used. Every image slot is set from `content/settings.json`, so AI or real images drop straight in. Prompt pack at the bottom if they still want them.
3. **Placeholders never reach the live site.** Production hides anything unfilled. `python3 build.py --preview` shows every `[[CLIENT TO PROVIDE]]` slot so the layout can be reviewed.

## Changelog

### Part 1: E-E-A-T fixes

- **Privacy policy** `/privacy-policy.html`. Privacy Act 1988 and APPs: what's collected (form fields, calls, client data, analytics and ad pixels, SmileOX lead data), why, storage and security, disclosure, overseas disclosure, cookies, access and correction, complaints and the OAIC, Notifiable Data Breaches. Last updated date at the top. **Template, needs a lawyer's review.**
- **Terms of use** `/terms.html`. Use of the site, general information not advice, no guaranteed results, IP, third-party links, Australian Consumer Law, liability limits, NSW governing law. Last updated date. **Template, needs a lawyer's review.**
- Privacy and Terms linked in the footer of every page. Privacy linked right above the submit button on both forms (Contact page and the "Send a note" pop-up).
- **Blog**: `/blog.html` index (card grid, topics, pagination-ready, page 2 onwards becomes `/blog-page-2.html`) and articles in `/blog/`. Every article shows author (linked to their Team profile), published date, last updated date, reading time and a "Reviewed by" line. BlogPosting and BreadcrumbList schema. "Blog" added to the header, mobile menu and footer.
- **Three starter articles, DRAFT FOR SEO TEAM REVIEW**, drawn only from what's already on the site, no new stats:
  - `/blog/why-the-map-listing-matters-for-dentists.html`
  - `/blog/what-happens-in-your-first-week.html`
  - `/blog/ai-search-for-local-businesses.html`

  They're published but noindex and out of the sitemap until `draft: false` is set.
- **Address and ABN**: both offices (Crows Nest and Parramatta) plus ABN, pre-filled from what Rowayne has given us before. In the footer of every page, on Contact (with a Google Map per office and directions links) and on About. Edited once in `content/settings.json`. **Rowayne to confirm.**
- **Schema** on every page: Organization + ProfessionalService with address, second office as a department, phone, email, ABN, founding date 2015, founders, 40+ staff, area served Australia, plus WebSite and the founders as Person. NAP is identical everywhere because it all comes from one file.
- **Team** `/team.html`: full profiles for Rowayne and Brett using facts already on the site (Myer roles, $60m+ and $1b+, 2015, building it at night, Caringbah), real headshots, expertise, Person schema. LinkedIn, qualifications, years and specialities appear as soon as they're filled in. Team grid ready for more people.
- **Success stories** `/success-stories.html`: The Caringbah Dentists plus the six Work clients, each with what they needed, what we did (existing approved copy), a results block and a named testimonial block. Results and testimonials stay hidden until real ones are added.
- **Awards and certifications** `/awards.html`: awards, certifications and partnerships sections with badge and proof-link slots. Noindex and unlinked until at least one real entry exists, then it links itself into the footer automatically.
- **Expertise** `/expertise.html`: hub for the nine services, the dental specialty, AI search and SmileOX, linking to every service page, with a "Strategy reviewed by" credit on each and a "who checks what" section.
- **Trust strip** (100+ / 30+ / 2015, plus badges once they exist) on About. Badges strip on the homepage appears once there's a badge.
- **Testimonial slider** on the homepage and About, built and hidden until there's a real testimonial.
- **"Reviewed by" author box** on all five service pages, linking to the Team profile, with a last reviewed date.

### Part 2: Project screenshots

- **Couldn't capture from here.** The build environment's network blocks the client domains, and this chat isn't linked to a computer. Instead:
  - `tools/capture-screenshots.mjs` does exactly what the brief asks: 1440x900 desktop and 390x844 mobile at 2x, waits for fonts, lazy content and hero videos, hides cookie banners, chat widgets and popups, saves hero and full-page captures as WebP under 200KB to `static/assets/work/<slug>-desktop|mobile|full.webp`, and skips and lists any site that fails. Tested end to end here against local pages.
  - Until it's run, the site uses a free screenshot service as a fallback, and a styled placeholder with the clinic's initials if that fails.
- **Presentation**:
  - Homepage: a slow-panning carousel of browser-framed screenshots that pauses on hover or focus. Hover shows name, location, tags and the existing blurb. Click goes to the success story, with a separate "Visit site" link. Swipe carousel on mobile, static under reduced motion.
  - `/work.html`: each project in a large browser frame with an overlapping phone frame. The full-page capture scrolls inside the browser frame as you scroll past. Each project links to its success story.
  - Alt text on every capture, for example "Footscray Dental Studio website homepage designed by GYA".
- Other GYA-built sites I know of that could be added (one line in `content/projects.json` each): The Caringbah Dentists, Grey Street Dentist, Dental Specialists, Kariong Dental Care and Cronulla Dentists (both still on staging).

### Part 3: Modernise sections, imagery, motion

- "Nine things" is now a bento grid with icons and hover states, each card linking to its service page.
- "Your first week" is a scroll-driven timeline: a progress line fills as you scroll, each day lights up as you reach it, and a large Day 01 to 07 counter tracks it on desktop.
- Animated counters on all the stats. The final number is in the HTML; the animation only runs when it scrolls into view.
- Staggered fade-and-rise reveals on cards and lists.
- Subtle parallax on the hero background and the photo bands.
- Header shrinks and gains a shadow on scroll, with a thin progress bar. Active page shown in the nav.
- Real office photo added to the homepage story, About, the Team page header and the CTA backgrounds on About and Team.
- Logo and partner marquee built, hidden until there are logos.
- **Motion budget**: no libraries, transforms and opacity only, one scroll handler throttled to animation frames, carousels only animate while on screen. Everything turns off under `prefers-reduced-motion`, and all content is in the HTML on load (reveals only fade content that's already there, and stay visible if JavaScript doesn't run).

### Part 4: CMS

Recommendation below. Nothing migrated. The build has been restructured so a CMS can sit straight on top: every editable thing now lives in `content/` as JSON or Markdown (address/NAP, per-page SEO, team, projects, success stories, testimonials, awards, partners, redirects, blog), with one shared header and footer.

### Part 5: SEO housekeeping

- `sitemap.xml` rebuilt automatically with every indexable page and `lastmod` dates. Noindex pages are left out.
- `robots.txt` allows everything and points to the sitemap. The preview build blocks all crawlers.
- Unique titles, descriptions under 160 characters, canonical and OG tags on every page. The build fails if a title is duplicated or a description is too long. I tightened eight existing descriptions that ran past 160 characters (meta only, page copy unchanged).
- Per-page title, description, OG image, canonical and noindex overrides in `content/seo.json`.
- Visible breadcrumbs plus BreadcrumbList schema on every inner page.
- Redirects: `content/redirects.json` becomes `vercel.json` on every build. Starter set covers common old paths (/about-us, /contact-us, /privacy-policy and so on). **The old site's real URL list still needs mapping** before the DNS switch.
- `tools/check_site.py` checks every page for broken links and anchors, invalid JSON-LD, missing H1, images without alt, missing meta, duplicates, dashes and placeholders. Currently: no problems on all 19 pages.

## Lighthouse

Run locally with Lighthouse 12 against the built files. Google Fonts are blocked in this environment, which costs the Best Practices point (a console network error that won't happen live) and probably flatters performance slightly. Treat these as relative, and re-run on the live URL after deploy.

| Page | Before (mobile / desktop) | After (mobile / desktop) |
|---|---|---|
| Home | Perf 96 / 100, A11y 98, BP 96, SEO 100 | Perf 96 to 98 / 100, A11y 100, BP 96, SEO 100 |
| Work | Perf 99 / 100, A11y 98, BP 96, SEO 100 | Perf 97 / 100, A11y 100, BP 96, SEO 100 |
| Blog index | did not exist | Perf 99 / 100, A11y 100, BP 96, SEO 100 |
| Article (draft) | did not exist | Perf 97 / 100, A11y 100, BP 96, SEO 69 |

The article's SEO 69 is only the noindex tag on drafts. It goes to 100 once `draft: false` is set. CLS is 0 on every page. LCP is 1.9 to 2.2s on simulated mobile.

## E-E-A-T re-check list

| Audit item | Where it's fixed |
|---|---|
| Privacy policy missing | `/privacy-policy.html`, linked in every footer and above both form submit buttons |
| Terms missing | `/terms.html`, linked in every footer |
| No blog / no author or dates | `/blog.html`, `/blog/*.html`: author link, published, updated, reading time, reviewed by, BlogPosting schema |
| No physical address | Footer of every page, `/contact.html#offices` (with maps), `/about.html`, Organization schema on every page |
| No ABN | Footer of every page, `/contact.html`, `/about.html`, schema `taxID` |
| No author or expert profiles | `/team.html#rowayne`, `/team.html#brett`, Person schema, linked from bylines and reviewer boxes |
| No case studies or results | `/success-stories.html` (results and testimonials appear once provided) |
| No awards or certifications | `/awards.html` (goes live once there's an entry) |
| No expertise hub | `/expertise.html` |
| No reviewer on service pages | "Reviewed by" box on `/dental-marketing.html`, `/dental-websites.html`, `/smileox.html`, `/marketing.html`, `/ai-marketing.html` |
| Trust signals on homepage and About | Trust strip on `/about.html`; badges, partner strip and testimonial slider on `/` and `/about.html` (hidden until real entries) |
| Breadcrumbs | Every inner page, visible and in schema |

## CMS recommendation

**Current setup**: plain static HTML generated by one Python script, no framework, deployed on Vercel, DNS at SiteGround. No Git repo yet. Content is now in `content/` as JSON and Markdown.

### Option 1: Sveltia CMS (or Decap CMS) on top of the current build. Recommended for now.

A Git-based CMS: an `/admin` page with forms for every file in `content/`. Saving commits to GitHub, Vercel rebuilds in about a minute.

- **Covers**: blog posts with scheduling (future publish dates, plus a daily rebuild), per-page SEO, team, projects, stories, testimonials, awards, NAP in one place, image uploads with resizing and WebP conversion, redirects.
- **Ease for the SEO team**: plain forms, rich text for posts, image picker. No live page preview of the full layout.
- **Cost**: free and open source.
- **Logins**: each editor needs a GitHub account added to the repo.
- **Setup**: put the site in a GitHub repo, connect Vercel to it, add the build command, add `/admin` and its config. Roughly one to two days.
- **Downside**: forms rather than click-on-the-page editing, and editors need GitHub accounts.

### Option 2: TinaCMS

Also Git-based, but with visual editing (click the text on the page to change it) and a hosted login so editors don't need GitHub.

- **Cost**: free tier for small teams, paid per editor above that. Check current pricing.
- **Setup**: visual editing really wants a JavaScript framework, so this means moving the templates to Astro first. Roughly one to two weeks.
- **Downside**: more moving parts, a hosted dependency, and the migration effort.

### Option 3: Astro plus Sanity

Templates moved to Astro, content in Sanity's hosted editor.

- **Best editing experience**: roles and permissions, drafts and scheduled publishing, live preview, an image CDN that resizes and compresses automatically, structured content that's easy to reuse.
- **Cost**: free tier, then paid per user. Check current pricing.
- **Setup**: a rebuild of the templates and content model. Roughly two to three weeks.
- **Downside**: the biggest change, and a second platform to look after.

**My pick**: Option 1 now. It's free, it works with the build exactly as it is, and the SEO team could be editing within a couple of days. It also doesn't lock anything in: the same `content/` files can move to Option 2 or 3 later, or onto GYA's own client dashboard framework once that's ready, which would make GYA's own site the demo for it.

**Waiting on approval before touching any of this.**

## Prompt pack for office scenes (only with Rowayne and Brett's OK)

Use the real photos `rowayne-img.jpg` and `brett-img.jpg` as reference images. Same style for every scene: photographic, editorial, natural window light, slightly warm grade, modern Sydney office with plants and timber, shallow depth of field, people in black or white GYA t-shirts, no readable text or logos on screens, hands and faces natural.

1. Rowayne and two team members reviewing charts on a large monitor, Rowayne pointing, mid-conversation.
2. Brett leading a strategy session at a whiteboard covered in sticky notes, four team members seated, candid.
3. Casual morning stand-up, six people with coffees, Rowayne and Brett among them, laughing.
4. Brett on a video call with a client at a standing desk, headset, warm side light.

Generate several of each, pick the most natural, save to `static/assets/images/<name>-640.webp` and `-1280.webp`, then set the names in `content/settings.json` under `images`. Label them in alt text as what they show, and keep the real headshots on the Team page.

## Update 12 October 2026: Live Agent Watch

Added a watcher that tells you when AI agents visit the site. It observes only and fails open: if Live Agent Watch is down or slow, pages behave exactly as before.

- **New files:** `middleware.js` (Vercel Routing Middleware), `package.json` (just `"type": "module"`, no dependencies), `tools/agentwatch.test.mjs`.
- **Changed:** `build.py` (hidden canary note before `</body>` on every page), `tools/check_site.py` (ignores the canary link), `templates/pages_trust.py` (privacy policy now names Live Agent Watch under "Website use" and "a website monitoring service" under disclosure; last updated 12 October 2026), `README.md`.
- **Not changed:** `robots.txt`, `sitemap.xml`, `vercel.json`, page copy.
- **Tests:** 14 passing. They cover the redaction and skip vectors, pages unchanged byte for byte with the endpoint unreachable, a hanging endpoint not slowing pages, nothing sent without a key, only allowed fields sent with the IP taken from `x-real-ip` (not `x-forwarded-for`), and back-off on 401, 403, 429 and 410.
- **Heads-up for the SEO team:** the canary link 404s on purpose, so crawl tools and Search Console may report `/data/fdd80dd6-export` as a broken link or 404.
