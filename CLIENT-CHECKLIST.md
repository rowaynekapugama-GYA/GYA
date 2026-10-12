# GYA website: what we need from Rowayne

Everything below is either hidden on the live site until it's provided, or pre-filled and needs a quick yes. Nothing on the site has been invented.

## 1. Please confirm (already filled in)

- [ ] **Offices.** Crows Nest: 119 Willoughby Road, Crows Nest NSW 2065. Parramatta: 215-217 Church Street, Parramatta NSW 2150. Is Crows Nest the main one for Google?
- [ ] **ABN** 68 620 590 481, shown in the footer and on Contact and About.
- [ ] **Surnames.** The Team page, blog bylines and schema use Rowayne Kapugama and Brett Dyson. OK to publish both?
- [ ] **Brett's title.** The site says "Co-founder · Client success". If he should be listed as COO anywhere, say so.
- [ ] **Naming clients.** Success stories name The Caringbah Dentists (and Dr Ram), Footscray Dental Studio, My Dentist, Tooth n Care, Horizon Dental, New'Gen Dental Surgery and Artarmon Dentists. Each practice should be happy to be named.
- [ ] **Caringbah link.** The story links to thecaringbahdentists.com.au. Correct?
- [ ] **Partner logo strip.** It's built but hidden. Rowayne removed the old scrolling logos earlier, so only add logos if he wants that back.

## 2. Founder profiles (Team page)

- [ ] LinkedIn URL for Rowayne
- [ ] LinkedIn URL for Brett
- [ ] Qualifications, if any, for each
- [ ] Years in marketing for each
- [ ] Specialities, in their own words (optional)
- [ ] Company LinkedIn, Facebook, Instagram, YouTube URLs (used in schema and footer)

## 3. Team

- [ ] Team members to feature: name, role, a real photo, and their OK to be on the site. Even 4 to 6 people makes the "40+ team" claim far more believable.
- [ ] Specialist lead for each service (Google Ads, SEO, websites, social, video and so on), so the Expertise page and service pages can credit the actual expert, not just the founders.

## 4. Proof (the E-E-A-T gaps that matter most)

- [ ] **Results for each success story.** For each of the 7 stories: the number, the period it covers, and where it came from (Google Ads, SmileOX, practice software). Only numbers the client agrees to publish.
- [ ] **Testimonials.** Named, with written consent: quote, name, role, practice, suburb, photo. These should be clinic owners or managers talking about our marketing, never patients talking about clinical care (AHPRA).
- [ ] **Awards, certifications and partnerships** actually held, with a link we can point to as proof and the badge file. For example Google Partner, Meta Business Partner, Microsoft Advertising Partner, any industry awards. The Awards page and badges stay hidden until there's at least one.

## 5. Legal and tracking

- [ ] **Lawyer review** of the Privacy policy and Terms of use. They're written for an Australian business under the Privacy Act 1988 and the APPs, but they're a template.
- [ ] Which tracking is actually installed or planned: GA4, Google Ads tag, Meta Pixel, call tracking. Are calls recorded?
- [ ] Where SmileOX data is hosted (country), and which other providers store data overseas (the privacy policy currently says "including the United States").
- [ ] Where contact form submissions should go: a SmileOX webhook, or an email inbox. The form doesn't send anywhere yet.

## 5b. Live Agent Watch

- [ ] Add `AGENTWATCH_SITE_KEY` in Vercel (Project, Settings, Environment Variables, Production). The key is on the Live Agent Watch install page. Then redeploy.
- [ ] Check the install page shows "First visit received".
- [ ] Find out which country Live Agent Watch stores data in, for the privacy policy's overseas section.

## 6. Before the DNS switch

- [ ] **Old site URL list.** Export from Google Search Console (Pages report) or the old sitemap.xml, so every old URL gets a 301 redirect. Missing these is the main way a rebuild loses rankings.
- [ ] Live domains for **Tooth n Care** and **New'Gen**. They currently link to vercel.app staging addresses.

## 7. Images

- [ ] **Project screenshots.** Someone with normal internet access runs `node tools/capture-screenshots.mjs` (instructions in README). Or send desktop and mobile homepage screenshots for the six sites.
- [ ] **Office photos.** The site uses the real photo of Rowayne, Brett and a team member in three places. A proper office shoot (team at screens, a strategy session, a client call) would replace the need for AI images. See the note on AI images in HANDOVER.md before generating any.
- [ ] A photo for the "Your first week" section (optional, slot is ready).

## 8. Content sign-off

- [ ] Three draft blog posts (SEO team review): "Why the map listing matters more than page one for dental practices", "What actually happens in your first week with GYA", "AI search for local businesses: how to be the name that comes up". They're live but noindex until `draft: false`.
- [ ] New copy on the Team, Success stories, Expertise, Awards and legal pages (the rest of the site's copy is unchanged).
