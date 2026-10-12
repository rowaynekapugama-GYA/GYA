// Live Agent Watch watcher for a static site on Vercel (Routing Middleware).
// Observes only: never changes, delays or blocks a response.
// Does nothing unless AGENTWATCH_SITE_KEY is set in the Vercel project settings.
// Contract: https://api.liveagentwatch.com/spec/contract.md (rules W1 to W10 noted inline)

export const config = {
  runtime: 'nodejs',
  // W10: our own CSS, JS, images and fonts never reach the watcher.
  // Everything else is observed, including requests for pages that don't exist.
  matcher: ['/((?!assets/|css/|js/|favicon\\.ico).*)'],
};

const CLIENT = { name: 'gya-vercel-static', version: '2026-10' };
const MAX_IN_FLIGHT = 50;   // W4
const TIMEOUT_MS = 2000;    // W4
let inFlight = 0;
let pausedUntil = 0;
let dropped = 0;

const endpoint = () =>
  (process.env.AGENTWATCH_ENDPOINT || 'https://api.liveagentwatch.com').replace(/\/+$/, '');

// W6: path only, never anything after ? or #
export function stripQuery(p) {
  return String(p || '/').split(/[?#]/)[0] || '/';
}

// W6: redaction, same rules as the Live Agent Watch reference watcher
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
export function redact(path) {
  return path
    .split('/')
    .map((segment) => {
      let s = segment;
      try { s = decodeURIComponent(segment); } catch {}
      const at = s.indexOf('@');
      if (at > 0 && s.indexOf('.', at) > at) return '[email]';
      if (UUID.test(s)) return segment;
      if (s.length >= 20 && /^[\w-]{4,}\.[\w-]{4,}\.[\w-]{4,}$/.test(s)) return '[token]';
      if (/^\d{12,}$/.test(s)) return '[number]';
      if (s.length >= 24 && /^[\w-]+$/.test(s) && /\d/.test(s) && /[A-Za-z]/.test(s) &&
          !/^[a-z0-9]+(?:-[a-z0-9]+){2,}$/.test(s)) return '[token]';
      return segment;
    })
    .join('/')
    .slice(0, 512);
}

// W10
const ASSET = /\.(css|js|mjs|map|png|jpe?g|gif|webp|avif|svg|ico|woff2?|ttf|mp4|webm)$/i;
export function isSkippedAsset(path, status) {
  return ASSET.test(path) && ((status >= 200 && status < 300) || status === 304);
}

// W5: exactly these fields, nothing else.
// Middleware runs before the page is served, so it can't see the status or timing:
// status is 0 (the protocol's value for "not visible") and duration_ms is 0,
// the same as Live Agent Watch's own edge snippet.
export function buildEvent(request, now = new Date()) {
  const h = request.headers;
  const ev = {
    kind: 'request',
    time: now.toISOString(),
    method: request.method,
    path: redact(stripQuery(new URL(request.url).pathname)),
    status: 0,
    duration_ms: 0,
    ip: h.get('x-real-ip') || '',          // W7: set by Vercel, can't be spoofed by the visitor
  };
  const ua = h.get('user-agent');
  if (ua) ev.user_agent = ua.slice(0, 512);
  const country = h.get('x-vercel-ip-country'); // set by Vercel only
  if (country && /^[A-Z]{2}$/.test(country)) ev.country = country;
  return ev;
}

export async function send(ev) {
  const key = process.env.AGENTWATCH_SITE_KEY;   // W8
  if (!key || Date.now() < pausedUntil) return;
  if (inFlight >= MAX_IN_FLIGHT) { dropped++; return; }   // W4: drop, never queue
  inFlight++;
  const body = { v: 1, client: CLIENT, events: [ev] };
  if (dropped) { body.dropped = dropped; dropped = 0; }
  try {
    const res = await fetch(`${endpoint()}/v1/events`, {
      method: 'POST',
      headers: { authorization: `Bearer ${key}`, 'content-type': 'application/json' },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(TIMEOUT_MS),
    });
    // W9
    if (res.status === 401 || res.status === 403) pausedUntil = Date.now() + 600000;
    else if (res.status === 429) pausedUntil = Date.now() + 1000 * (Number(res.headers.get('retry-after')) || 60);
    else if (res.status === 410) pausedUntil = Infinity;
    try { await res.body?.cancel(); } catch {}
  } catch {
    // W1: network errors and timeouts are ignored
  } finally {
    inFlight--;
  }
}

// For tests only: clears the back-off and drop counters between cases.
export function _reset() { inFlight = 0; pausedUntil = 0; dropped = 0; }

export default function middleware(request, context) {
  try {                                              // W1
    if (!process.env.AGENTWATCH_SITE_KEY) return;   // W8
    const ev = buildEvent(request);
    if (!ev.ip || isSkippedAsset(ev.path, ev.status)) return;
    const pending = send(ev).catch(() => {});
    // W2: send in the background after the response has gone
    if (context && typeof context.waitUntil === 'function') context.waitUntil(pending);
  } catch {}
  // W3: returning nothing means Vercel serves the page exactly as it would without this file
}
