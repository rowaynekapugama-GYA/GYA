// Captures hero screenshots of every project in content/projects.json.
//
//   cd tools && npm install && npx playwright install chromium
//   node capture-screenshots.mjs                 # all projects
//   node capture-screenshots.mjs footscray artarmon   # just these slugs
//
// Writes static/assets/work/<slug>-desktop.webp, -mobile.webp and -full.webp,
// then run `python3 build.py` and the site uses them instead of the fallback.
import { chromium } from 'playwright';
import sharp from 'sharp';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT = process.env.OUT_DIR || path.join(ROOT, 'static/assets/work');
const projects = JSON.parse(await fs.readFile(path.join(ROOT, 'content/projects.json'), 'utf8')).projects;
const only = process.argv.slice(2);
const list = projects.filter(p => !only.length || only.includes(p.slug));

// Hide cookie banners, chat widgets and popups before capture.
const HIDE = `
  [id*="cookie" i],[class*="cookie" i],[id*="consent" i],[class*="consent" i],
  [class*="cmplz" i],#CybotCookiebotDialog,.cky-consent-container,#onetrust-consent-sdk,
  iframe[src*="chat" i],[id*="chat-widget" i],[class*="chat-widget" i],#hubspot-messages-iframe-container,
  .intercom-lightweight-app,#intercom-container,[class*="tawk" i],#fb-root,.fb_dialog,
  [class*="popup" i][style*="fixed"],[class*="modal" i][aria-modal="true"],.elementor-popup-modal,
  [class*="userway" i],[id*="userway" i],[class*="accessibe" i],[class*="notes-widget" i]
  { display:none !important; visibility:hidden !important; }
  html,body{overflow:visible !important}
  *,*::before,*::after{animation-duration:0s !important;animation-delay:0s !important;transition:none !important;scroll-behavior:auto !important}
`;

async function settle(page) {
  await page.waitForLoadState('networkidle', { timeout: 20000 }).catch(() => {});
  await page.evaluate(() => document.fonts && document.fonts.ready);
  // trigger lazy content, then come back up
  await page.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); }
    window.scrollTo(0, 0);
  });
  await page.addStyleTag({ content: HIDE });
  // Lazy images: load them all now and wait for them to arrive.
  await page.evaluate(() => document.querySelectorAll('img').forEach(i => { i.loading = 'eager'; if (i.dataset.src && !i.src) i.src = i.dataset.src; }));
  await page.waitForFunction(() => [...document.images].every(i => i.complete), { timeout: 10000 }).catch(() => {});
  // let hero videos show a frame, and reveal-on-scroll content settle
  await page.evaluate(() => document.querySelectorAll('video').forEach(v => { try { v.muted = true; v.play(); } catch (e) {} }));
  await page.waitForTimeout(2500);
  await tidy(page);
}

// Video hosts (Vimeo, YouTube) block cloud servers such as GitHub's runners and
// show an error box instead of the video. Hide embedded players so the section
// shows its own background, and collapse empty video wrappers. Then hide small
// floating widgets pinned to the bottom of the screen (accessibility buttons,
// chat bubbles, sticky call bars) so they don't sit on top of the design.
async function tidy(page) {
  const report = await page.evaluate(() => {
    const out = { videos: [], floats: [] };
    const host = /vimeo|youtube|youtu\.be|wistia|vidyard/i;
    document.querySelectorAll('iframe').forEach(f => {
      if (host.test(f.src || f.dataset.src || '')) { out.videos.push(f.src.slice(0, 80)); f.style.setProperty('display', 'none', 'important'); }
    });
    document.querySelectorAll('.elementor-background-video-container, [class*="video-background" i], [class*="bg-video" i]').forEach(c => {
      const v = c.querySelector('video');
      if (!v || v.readyState < 2) c.style.setProperty('visibility', 'hidden', 'important');
    });
    const vh = window.innerHeight, vw = window.innerWidth;
    for (const el of document.body.querySelectorAll('*')) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' || cs.display === 'none') continue;
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const smallWidget = r.width * r.height < 40000;
      const bottomBar = r.height < 140 && r.top > vh * 0.6;
      if ((smallWidget || bottomBar) && r.top > vh * 0.5 && !(r.top < 5 && r.width > vw * 0.9)) {
        out.floats.push((el.id || el.className || el.tagName).toString().slice(0, 40));
        el.style.setProperty('display', 'none', 'important');
      }
    }
    return out;
  });
  if (report.videos.length || report.floats.length) console.log(`     hid videos: ${report.videos.join(', ') || 'none'} | floats: ${report.floats.join(', ') || 'none'}`);
}

async function shoot(p, kind, browser) {
  const mobile = kind === 'mobile';
  const ctx = await browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: 2, isMobile: mobile, hasTouch: mobile,
    userAgent: mobile ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' : undefined,
  });
  const page = await ctx.newPage();
  const res = await page.goto(p.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  if (!res || res.status() >= 400) throw new Error(`HTTP ${res && res.status()}`);
  // Cloudflare and similar sometimes show a "checking your connection" page to
  // a cloud server. Give it a moment to pass, otherwise skip the project so
  // the existing screenshot stays.
  for (let tries = 0; tries < 4; tries++) {
    const challenged = await page.evaluate(() => /just a moment|checking (the site|your) (connection|browser)|verify you are human|attention required/i.test(document.title + ' ' + document.body.innerText.slice(0, 600)));
    if (!challenged) break;
    if (tries === 3) throw new Error('site is showing a bot check page, kept the existing screenshot');
    await page.waitForTimeout(6000);
  }
  await settle(page);
  // Optional: start the desktop and mobile shots at a section further down the
  // page (projects.json "capture": {"start_text": "..."}), for sites whose top
  // of page doesn't show off the work. "mobile_start_text" picks a different
  // section for the phone, or "" to keep the top of the page there.
  const cap = p.capture || {};
  const start = kind === 'full' ? '' : (mobile && 'mobile_start_text' in cap ? cap.mobile_start_text : cap.start_text);
  if (start) {
    const found = await page.evaluate((text) => {
      const el = [...document.querySelectorAll('h1,h2,h3,h4,p,span,div')].find(e => e.children.length === 0 && e.textContent.trim().toLowerCase().includes(text.toLowerCase()));
      if (!el) return false;
      // On phones most themes stack the section's columns, so the heading's own
      // column can start well below the section's photo. Use the outermost
      // section so the shot starts where the section does.
      // Page-level wrappers (elementor-section-wrap and the like) match too,
      // so anything taller than about three screens is skipped.
      const limit = Math.max(1800, innerHeight * 3);
      let sec = el, cur = el;
      while ((cur = cur.parentElement) && cur !== document.body) {
        if (cur.matches('section,[class*="elementor-section" i],[class*="e-con" i],[class*="wp-block-group" i]') && cur.getBoundingClientRect().height <= limit) sec = cur;
      }
      const target = () => Math.max(0, sec.getBoundingClientRect().top + window.scrollY - 20);
      window.scrollTo(0, target());
      // Sticky and fixed headers would sit on top of the section. Remove them,
      // since the shot isn't of the top of the page any more, then line the
      // section up again because removing a sticky bar can shift the page.
      for (const h of document.body.querySelectorAll('header,nav,[class*="header" i],[id*="header" i],[class*="navbar" i],[class*="sticky" i]')) {
        const cs = getComputedStyle(h), r = h.getBoundingClientRect();
        if ((cs.position === 'fixed' || cs.position === 'sticky') && r.top < 160 && r.width > innerWidth * 0.6) h.style.setProperty('display', 'none', 'important');
      }
      window.scrollTo(0, target());
      return true;
    }, start);
    if (!found) console.log(`     start_text not found for ${p.slug}, using the top of the page`);
    await page.waitForTimeout(1200);
  }
  const buf = await page.screenshot({ fullPage: kind === 'full', type: 'png' });
  await ctx.close();
  return buf;
}

async function save(buf, file, width, maxHeight) {
  let img = sharp(buf);
  const meta = await img.metadata();
  if (maxHeight && meta.height > maxHeight * (meta.width / width)) img = img.extract({ left: 0, top: 0, width: meta.width, height: Math.round(maxHeight * (meta.width / width)) });
  let q = 72, out;
  do { out = await img.clone().resize({ width }).webp({ quality: q, effort: 6 }).toBuffer(); q -= 8; } while (out.length > 200 * 1024 && q > 30);
  await fs.writeFile(file, out);
  return Math.round(out.length / 1024);
}

await fs.mkdir(OUT, { recursive: true });
const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const failed = [];
for (const p of list) {
  try {
    const d = await shoot(p, 'desktop', browser);
    const m = await shoot(p, 'mobile', browser);
    const f = await shoot(p, 'full', browser);
    // A near-blank page (a bot check or a failed load) is never an improvement.
    for (const [buf, kind] of [[d, 'desktop'], [m, 'mobile']]) {
      const { entropy } = await sharp(buf).stats();
      if (entropy < 1.2) throw new Error(`${kind} shot looks blank, kept the existing screenshot`);
    }
    const a = await save(d, path.join(OUT, `${p.slug}-desktop.webp`), 1440);
    const b = await save(m, path.join(OUT, `${p.slug}-mobile.webp`), 390 * 2);
    const c = await save(f, path.join(OUT, `${p.slug}-full.webp`), 1200, 4200);
    console.log(`ok   ${p.slug.padEnd(14)} desktop ${a}KB  mobile ${b}KB  full ${c}KB`);
  } catch (e) {
    failed.push(p.slug); console.log(`FAIL ${p.slug.padEnd(14)} ${e.message}`);
  }
}
await browser.close();
if (failed.length) { console.log(`\nSkipped: ${failed.join(', ')}. Check those sites load, then rerun with their slugs.`); process.exitCode = 1; }
else console.log('\nDone. Now run: python3 build.py');
