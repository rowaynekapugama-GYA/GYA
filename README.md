# GYA website (generateyouraudience.com)

Static site, no frameworks, no pip packages. Python builds the HTML from content files.

## Folders

| Folder | What's in it | Who edits it |
|---|---|---|
| `content/` | All editable content: settings (address, phone, ABN), SEO per page, team, projects, success stories, testimonials, awards, partners, redirects, blog posts | SEO team, later through the CMS |
| `templates/` | Page layouts. The copy in `templates/pages.py` is approved, don't rewrite it | Developer |
| `static/` | CSS, JS, images, favicons. Copied into `dist/` as is | Developer |
| `tools/` | Screenshot capture script and the site checker | Developer |
| `dist/` | The built site. This is what Vercel serves | Generated, don't edit |

## Build

```
python3 build.py             # production build into dist/ (deploy this)
python3 build.py --preview   # preview into dist-preview/, shows every [[CLIENT TO PROVIDE]] slot
python3 tools/check_site.py dist   # links, anchors, JSON-LD, headings, meta, dashes
```

The build refuses to finish if any page has an em or en dash, a meta description over 160 characters, or a duplicate title.

Production builds hide anything that's still a placeholder: empty results, testimonials, awards, partner logos and team fields simply don't render. The Awards page stays noindex and unlinked until it has at least one entry. Blog posts with `draft: true` are published but noindex and left out of the sitemap.

## Common edits

- **Address, phone, ABN, socials:** `content/settings.json`. Changes the header, footer, contact page, about page and the schema on every page.
- **Page titles and descriptions:** `content/seo.json`. Blank values use the page default. Also supports `og_image`, `canonical` and `noindex`.
- **New blog post:** copy a file in `content/blog/`, change the front matter, write in Markdown. Set `draft: false` to index it. A future `published` date holds it back until that day's build.
- **Testimonials, results, awards:** the JSON file of the same name. Only add things you can back up (see the `_help` line at the top of each file).
- **Redirects:** `content/redirects.json`. Written into `vercel.json` on every build.
- **Team photos:** put `<name>-400.webp` and `<name>-600.webp` in `static/assets/images/` and set `photo` in `content/team.json`.

## Project screenshots

Until real captures exist, the site falls back to a free screenshot service and then to a styled placeholder. To capture proper ones (needs a machine that can reach the client sites):

```
cd tools
npm install
npx playwright install chromium
node capture-screenshots.mjs          # all projects, or pass slugs: node capture-screenshots.mjs footscray artarmon
cd .. && python3 build.py
```

It saves `static/assets/work/<slug>-desktop.webp`, `-mobile.webp` and `-full.webp`, each under 200KB, with cookie banners, chat widgets and popups hidden. Sites that fail to load are skipped and listed.

## Deploy

`vercel.json` (generated) tells Vercel to serve `dist/`. Deploy from the repo root. No build command is needed while `dist/` is committed. When the CMS goes in, add `"buildCommand": "python3 build.py"` so Vercel rebuilds on every content change.

## Live Agent Watch

`middleware.js` (project root) reports page requests to Live Agent Watch so you can see when AI agents visit. It only observes: it never changes, delays or blocks a page, and it does nothing at all unless `AGENTWATCH_SITE_KEY` is set in Vercel (Project, Settings, Environment Variables). The key never goes in the code.

- Sends only time, method, path (query removed, emails and tokens redacted), status, duration, IP (`x-real-ip`), user agent and country (`x-vercel-ip-country`). Status and duration are always 0, because middleware runs before the page is served.
- Skips `/assets/`, `/css/`, `/js/` and the favicon.
- Every page has a hidden canary link to `/data/fdd80dd6-export` (added in `build.py`). That page deliberately doesn't exist, so crawl tools will report it as a 404. That's expected.
- Tests: `python3 build.py && npm test` (Node 20+, no packages).
- The middleware only deploys if Vercel gets the whole project folder, not just `dist/`.
