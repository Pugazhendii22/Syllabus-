// Only cache the public app shell and prepared notes, never API responses or private user data.
const CACHE = 'ammu-study-shell-v51';
const DOCUMENTS = ['/notes/spoken-english/Spoken_English_Notes.pdf', '/notes/spoken-english/downloads/Spoken-English-All-Units.docx', ...[1,2,3,4,5].flatMap(n=>[`/notes/spoken-english/downloads/Spoken-English-Unit-${n}.pdf`,`/notes/spoken-english/downloads/Spoken-English-Unit-${n}.docx`])];
const documentPaths = new Set(DOCUMENTS);
const SHELL = ['/', '/style.css?v=31', '/app.js?v=28', '/pwa.js?v=6', '/courses.json', '/prepared-notes.json', '/manifest.webmanifest', '/icons/icon-192.png', '/icons/icon-512.png', '/icons/apple-touch-icon.png', '/icons/favicon.png', ...DOCUMENTS];
const paths = new Set(SHELL.map(p => new URL(p, self.location.origin).pathname));
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(SHELL)));
});
// Activate an installed update only after the reader chooses to reload.
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') self.skipWaiting();
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith('ammu-study-shell-') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', event => {
  const request = event.request, url = new URL(request.url);
  if (request.method !== 'GET' || url.origin !== self.location.origin || url.pathname.startsWith('/api/')) return;
  // Keep documents in their own cache entries, even when a browser opens a PDF as a navigation.
  if (documentPaths.has(url.pathname)) {
    // Leave byte-range requests to the network rather than storing partial files.
    if (request.headers?.has('range')) return;
    event.respondWith((async () => {
      const cache = await caches.open(CACHE);
      try {
        const response = await fetch(request);
        if (response.status === 200) await cache.put(url.pathname, response.clone());
        return response;
      } catch (_) {
        return (await cache.match(url.pathname)) || new Response('This document is not available offline yet.', {status: 503});
      }
    })());
    return;
  }
  const navigation = request.mode === 'navigate';
  if (!navigation && !paths.has(url.pathname)) return;
  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    try {
      const response = await fetch(request);
      if (response.ok) await cache.put(navigation ? '/' : request, response.clone());
      return response;
    } catch (_) {
      const stored = await cache.match(navigation ? '/' : request);
      return stored || new Response('This page is not available offline yet. Please connect to the internet.', {status: 503, headers: {'Content-Type': 'text/plain; charset=utf-8'}});
    }
  })());
});
