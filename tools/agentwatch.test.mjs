// Tests for the Live Agent Watch watcher (middleware.js). No packages: Node's built-in runner.
//   node --test tools/agentwatch.test.mjs      (or: npm test)
// Run `python3 build.py` first so dist/ exists.
import { test, before, after, beforeEach } from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import middleware, { redact, stripQuery, isSkippedAsset, buildEvent, send, _reset, config } from '../middleware.js';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DIST = path.join(ROOT, 'dist');

// ---- Test vectors, copied from https://api.liveagentwatch.com/spec/vectors/redact.json and skip.json
const REDACT = [
  ['/products/42', '/products/42'],
  ['/search?q=jane@example.com', '/search'],
  ['/page#section', '/page'],
  ['/u/jane@example.com/settings', '/u/[email]/settings'],
  ['/u/jane%40example.com', '/u/[email]'],
  ['/reset/eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0In0.c2lnbmF0dXJl', '/reset/[token]'],
  ['/invite/8f2aK9xQ7mP3vL1sR6tW0yZ4bN5c', '/invite/[token]'],
  ['/card/4111111111111111', '/card/[number]'],
  ['/orders/0192f3a4-7c1e-7b2a-9d40-5f1e2c3b4a59', '/orders/0192f3a4-7c1e-7b2a-9d40-5f1e2c3b4a59'],
  ['/blog/my-post-about-2024-trends-and-more', '/blog/my-post-about-2024-trends-and-more'],
  ['/orders/123456', '/orders/123456'],
  ['/.env', '/.env'],
  ['/admin/..;/secret', '/admin/..;/secret'],
  ['/', '/'],
];
const SKIP = [
  ['/static/app.css', 200, true],
  ['/img/logo.PNG', 304, true],
  ['/fonts/inter.woff2', 200, true],
  ['/static/app.js', 404, false],
  ['/config.bak.js', 403, false],
  ['/products', 200, false],
  ['/api/data.json', 200, false],
];

// ---- helpers
const ALLOWED = new Set(['kind', 'time', 'method', 'path', 'status', 'duration_ms', 'ip', 'user_agent', 'country']);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
function listen(handler) {
  return new Promise((resolve) => {
    const s = http.createServer(handler);
    s.listen(0, '127.0.0.1', () => resolve(s));
  });
}
const urlOf = (s) => `http://127.0.0.1:${s.address().port}`;
function closeAll(s) { s.closeAllConnections?.(); return new Promise((r) => s.close(() => r())); }

// A stand-in for Vercel: run the middleware first, then serve dist/ unchanged.
let pending = [];
function site(withWatcher) {
  return listen(async (req, res) => {
    if (withWatcher) {
      const headers = new Headers();
      for (const [k, v] of Object.entries(req.headers)) headers.set(k, Array.isArray(v) ? v.join(', ') : v);
      const request = new Request(`http://${req.headers.host}${req.url}`, { method: req.method, headers });
      const out = middleware(request, { waitUntil: (p) => pending.push(p) });
      if (out !== undefined) { res.writeHead(500); res.end('middleware returned a response'); return; }
    }
    const p = decodeURIComponent(req.url.split('?')[0]);
    const file = path.join(DIST, p.endsWith('/') ? p + 'index.html' : p);
    try {
      const body = await fs.readFile(file);
      res.writeHead(200, { 'content-type': file.endsWith('.html') ? 'text/html; charset=utf-8' : 'application/octet-stream' });
      res.end(body);
    } catch {
      res.writeHead(404, { 'content-type': 'text/plain' }); res.end('Not found');
    }
  });
}
async function fetchPage(base, p, headers = {}) {
  const r = await fetch(base + p, { headers });
  return { status: r.status, body: await r.text() };
}
function req(p, headers = {}) {
  return new Request('https://www.generateyouraudience.com' + p, { headers: { 'x-real-ip': '203.0.113.7', 'user-agent': 'TestAgent/1.0', ...headers } });
}

const envBackup = { ...process.env };
beforeEach(() => {
  _reset(); pending = [];
  process.env.AGENTWATCH_SITE_KEY = 'aw_sk_test_notreal';
  delete process.env.AGENTWATCH_ENDPOINT;
});
after(() => { process.env = envBackup; });
before(async () => { await fs.access(path.join(DIST, 'index.html')); });

// ---- 1. vectors
test('redaction vectors (redact.json)', () => {
  for (const [input, output] of REDACT) assert.equal(redact(stripQuery(input)), output, input);
});
test('skip vectors (skip.json)', () => {
  for (const [p, status, skip] of SKIP) assert.equal(isSkippedAsset(p, status), skip, `${p} ${status}`);
});
test('matcher keeps our own static files away from the watcher', () => {
  const re = new RegExp('^' + config.matcher[0].replace(/\\\\/g, '\\') + '$');
  for (const p of ['/', '/index.html', '/blog/ai-search-for-local-businesses.html', '/data/fdd80dd6-export', '/wp-login.php', '/robots.txt'])
    assert.ok(re.test(p), `should watch ${p}`);
  for (const p of ['/assets/gya-logo.png', '/css/style.css', '/js/main.js', '/favicon.ico'])
    assert.ok(!re.test(p), `should skip ${p}`);
});

// ---- 2. fail open: endpoint unreachable
test('with the endpoint unreachable, pages are byte-for-byte the same', async () => {
  process.env.AGENTWATCH_ENDPOINT = 'http://127.0.0.1:9';
  const plain = await site(false), watched = await site(true);
  try {
    for (const p of ['/index.html', '/blog.html', '/does-not-exist.html', '/data/fdd80dd6-export?x=1']) {
      const a = await fetchPage(urlOf(plain), p);
      const b = await fetchPage(urlOf(watched), p, { 'x-real-ip': '203.0.113.7', 'user-agent': 'GPTBot/1.0' });
      assert.equal(b.status, a.status, p);
      assert.equal(b.body, a.body, p);
    }
    assert.ok(pending.length >= 4, 'watcher should have tried to send');
    await Promise.all(pending);   // and never rejects
  } finally { await closeAll(plain); await closeAll(watched); }
});

// ---- 3. fail open: endpoint hangs
test('a hanging endpoint does not slow pages, and the send gives up within ~2s', async () => {
  const hang = await listen(() => {});   // accepts, never answers
  process.env.AGENTWATCH_ENDPOINT = urlOf(hang);
  const watched = await site(true);
  try {
    const t0 = Date.now();
    const r = await fetchPage(urlOf(watched), '/index.html', { 'x-real-ip': '203.0.113.7' });
    const pageMs = Date.now() - t0;
    assert.equal(r.status, 200);
    assert.ok(pageMs < 500, `page took ${pageMs}ms`);
    const s0 = Date.now(); await Promise.all(pending); const sendMs = Date.now() - s0;
    assert.ok(sendMs < 2600, `send took ${sendMs}ms`);
  } finally { await closeAll(watched); await closeAll(hang); }
});

// ---- 4. no key, nothing sent
test('without AGENTWATCH_SITE_KEY nothing is sent', async () => {
  delete process.env.AGENTWATCH_SITE_KEY;
  let hits = 0;
  const ep = await listen((q, r) => { hits++; r.end(); });
  process.env.AGENTWATCH_ENDPOINT = urlOf(ep);
  try {
    const ctx = { waitUntil: (p) => pending.push(p) };
    assert.equal(middleware(req('/'), ctx), undefined);
    await Promise.all(pending); await sleep(50);
    assert.equal(hits, 0); assert.equal(pending.length, 0);
  } finally { await closeAll(ep); }
});

// ---- 5. what gets sent
test('sends only the allowed fields, redacted, with the right IP and auth', async () => {
  const got = [];
  const ep = await listen((q, r) => {
    let b = ''; q.on('data', (c) => (b += c));
    q.on('end', () => { got.push({ url: q.url, auth: q.headers.authorization, type: q.headers['content-type'], body: JSON.parse(b) }); r.writeHead(202); r.end('{"accepted":1}'); });
  });
  process.env.AGENTWATCH_ENDPOINT = urlOf(ep);
  try {
    const ctx = { waitUntil: (p) => pending.push(p) };
    middleware(req('/u/jane@example.com/settings?token=abc#x', {
      'x-forwarded-for': '6.6.6.6, 203.0.113.7', 'x-vercel-ip-country': 'AU',
      cookie: 'session=secret', authorization: 'Bearer visitor-secret', referer: 'https://example.com/',
    }), ctx);
    await Promise.all(pending);
    assert.equal(got.length, 1);
    const { url, auth, type, body } = got[0];
    assert.equal(url, '/v1/events');
    assert.equal(auth, 'Bearer aw_sk_test_notreal');
    assert.equal(type, 'application/json');
    assert.equal(body.v, 1);
    assert.deepEqual(Object.keys(body).sort(), ['client', 'events', 'v']);
    const ev = body.events[0];
    for (const k of Object.keys(ev)) assert.ok(ALLOWED.has(k), `unexpected field ${k}`);
    assert.equal(ev.kind, 'request');
    assert.equal(ev.path, '/u/[email]/settings');
    assert.equal(ev.ip, '203.0.113.7');       // from x-real-ip, not x-forwarded-for
    assert.equal(ev.country, 'AU');
    assert.equal(ev.user_agent, 'TestAgent/1.0');
    assert.equal(ev.status, 0); assert.equal(ev.duration_ms, 0);
    assert.match(ev.time, /^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(\.\d+)?Z$/);
    const raw = JSON.stringify(body);
    for (const leak of ['session=secret', 'visitor-secret', 'token=abc', 'example.com/', '6.6.6.6', 'jane']) assert.ok(!raw.includes(leak), `leaked ${leak}`);
  } finally { await closeAll(ep); }
});

test('no IP header means nothing is sent', () => {
  const ctx = { waitUntil: (p) => pending.push(p) };
  middleware(new Request('https://www.generateyouraudience.com/'), ctx);
  assert.equal(pending.length, 0);
});

test('user agent is capped at 512 characters, bad country values dropped', () => {
  const ev = buildEvent(req('/', { 'user-agent': 'x'.repeat(900), 'x-vercel-ip-country': 'Australia' }));
  assert.equal(ev.user_agent.length, 512);
  assert.equal('country' in ev, false);
});

// ---- 6. back-off
for (const [status, label] of [[401, '401'], [403, '403'], [429, '429 with Retry-After'], [410, '410']]) {
  test(`backs off after ${label}`, async () => {
    let hits = 0;
    const ep = await listen((q, r) => { hits++; q.resume(); r.writeHead(status, status === 429 ? { 'retry-after': '120' } : {}); r.end(); });
    process.env.AGENTWATCH_ENDPOINT = urlOf(ep);
    try {
      await send(buildEvent(req('/')));
      await send(buildEvent(req('/about.html')));
      assert.equal(hits, 1);
    } finally { await closeAll(ep); }
  });
}

test('a thrown error inside the watcher never reaches the site', () => {
  const broken = { headers: { get() { throw new Error('boom'); } }, url: 'not a url', method: 'GET' };
  assert.doesNotThrow(() => middleware(broken, { waitUntil() { throw new Error('boom'); } }));
  assert.equal(middleware(broken, null), undefined);
});
