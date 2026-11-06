// Shared helpers for the Vercel serverless functions. Files starting with "_" are not exposed as routes.
// Behaviour mirrors server.py so the front end (app.js) needs no changes.

const MAX_BODY_CHARS = 60000;
const hits = new Map(); // best-effort, per warm instance only
const WINDOW_MS = 10 * 60 * 1000;
const MAX_HITS = 20;

function config() {
  return {
    key: process.env.AI_API_KEY || '',
    model: process.env.AI_MODEL || '',
    base: (process.env.AI_BASE_URL || 'https://api.openai.com/v1').replace(/\/+$/, ''),
  };
}

function send(res, status, obj) {
  res.status(status);
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  res.send(JSON.stringify(obj));
}

function sameOrigin(req) {
  const origin = req.headers.origin;
  if (!origin) return true; // same-origin fetches from some browsers omit Origin on GET only; POST normally sends it
  try {
    const host = req.headers['x-forwarded-host'] || req.headers.host;
    return new URL(origin).host === host;
  } catch (_) {
    return false;
  }
}

function limited(req) {
  const ip = String(req.headers['x-forwarded-for'] || req.socket?.remoteAddress || 'unknown').split(',')[0].trim();
  const now = Date.now();
  const recent = (hits.get(ip) || []).filter(t => now - t < WINDOW_MS);
  recent.push(now);
  hits.set(ip, recent);
  if (hits.size > 500) for (const [k, v] of hits) if (!v.some(t => now - t < WINDOW_MS)) hits.delete(k);
  return recent.length > MAX_HITS;
}

module.exports = { MAX_BODY_CHARS, config, send, sameOrigin, limited };
