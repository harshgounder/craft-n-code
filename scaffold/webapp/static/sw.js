/* Signal PWA service worker (BUILD-SPEC B11).
 *
 * Cache-first for static assets so the UI loads offline-ish; network-first
 * for /api/* with a JSON error response when the network is gone. Requests
 * that carry auth material are never cached. Pure vanilla JS, no deps.
 */
const CACHE = 'signal-static-v1';
const STATIC = ['/', '/index.html', '/manifest.json', '/static/icon-192.png'];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll(STATIC))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  // never cache anything that carries auth material
  if (url.pathname.indexOf('token') !== -1 || url.search.indexOf('token') !== -1) return;

  if (url.pathname.startsWith('/api/')) {
    // network-first: the live data is the whole point, offline falls back
    // to a JSON error response instead of a stale snapshot
    event.respondWith(
      fetch(req).catch(() => new Response(
        JSON.stringify({ ok: false, error: 'offline', offline: true }),
        { status: 503, headers: { 'Content-Type': 'application/json' } }
      ))
    );
    return;
  }

  // cache-first for static assets, filling the cache on first miss
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        if (res.ok) {
          const clone = res.clone();
          caches.open(CACHE).then((cache) => cache.put(req, clone));
        }
        return res;
      }).catch(() => caches.match('/index.html'));
    })
  );
});
