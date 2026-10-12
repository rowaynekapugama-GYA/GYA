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
  // let hero videos show a frame, and reveal-on-scroll content settle
  await page.evaluate(() => document.querySelectorAll('video').forEach(v => { try { v.muted = true; v.play(); } catch (e) {} }));
  await page.waitForTimeout(2500);
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
  await settle(page);
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
