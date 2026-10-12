/* GYA site. No libraries. Everything here is enhancement: all content is in the HTML. */
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var raf = window.requestAnimationFrame || function (f) { return setTimeout(f, 16); };

  /* ---------- header: shrink, blur, progress bar ---------- */
  var header = document.querySelector('.header');
  var bar = document.querySelector('.scroll-progress');
  var ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    raf(function () {
      var y = window.scrollY, max = doc.scrollHeight - innerHeight;
      if (header) header.classList.toggle('scrolled', y > 8);
      if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0) + ')';
      timeline(); parallax(); scrollShots();
      ticking = false;
    });
  }
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector('.burger'), mm = document.querySelector('.mobile-menu');
  function closeMenu() { mm.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; }
  if (burger && mm) {
    burger.addEventListener('click', function () {
      var open = mm.classList.toggle('open');
      burger.setAttribute('aria-expanded', open); document.body.style.overflow = open ? 'hidden' : '';
    });
    mm.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeMenu); });
  }

  /* ---------- reveal + stagger ---------- */
  document.querySelectorAll('.stagger').forEach(function (g) {
    var kids = g.querySelectorAll(':scope > .reveal');
    kids.forEach(function (k, i) { k.style.transitionDelay = Math.min(i, 8) * 70 + 'ms'; });
  });
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else { reveals.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- counters (final value is already in the HTML) ---------- */
  function countUp(el) {
    var txt = el.textContent.trim();
    var m = txt.match(/^([^\d]*)(\d[\d,]*\.?\d*)(.*)$/);
    if (!m) return;
    var pre = m[1], num = parseFloat(m[2].replace(/,/g, '')), suf = m[3];
    if (!num) return;
    var from = num >= 1900 && num <= 2100 ? num - 20 : 0;
    var dur = 1200, t0 = null, dec = (m[2].split('.')[1] || '').length;
    el.setAttribute('aria-label', txt);
    function step(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      var v = from + (num - from) * e;
      el.textContent = pre + (dec ? v.toFixed(dec) : Math.round(v).toLocaleString('en-AU').replace(/,/g, num >= 1900 && num <= 2100 ? '' : ',')) + suf;
      if (k < 1) raf(step); else el.textContent = txt;
    }
    raf(step);
  }
  var counters = document.querySelectorAll('[data-count], .hero-meta strong, .stat strong');
  if ('IntersectionObserver' in window && !reduce) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { countUp(e.target); co.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counters.forEach(function (c) { co.observe(c); });
  }

  /* ---------- "Your first week" timeline ---------- */
  var tl = document.querySelector('[data-timeline]');
  var tlFill = tl && tl.querySelector('.tl-fill');
  var tlItems = tl ? tl.querySelectorAll('.tl-item') : [];
  var tlNow = document.querySelector('[data-tl-now]');
  function timeline() {
    if (!tl) return;
    var r = tl.getBoundingClientRect(), mid = innerHeight * 0.55;
    var p = Math.max(0, Math.min(1, (mid - r.top) / r.height));
    if (tlFill) tlFill.style.transform = 'scaleY(' + p + ')';
    var active = 0;
    tlItems.forEach(function (it, i) {
      var on = it.getBoundingClientRect().top < mid;
      it.classList.toggle('on', on); if (on) active = i + 1;
    });
    if (tlNow) tlNow.textContent = ('0' + Math.max(1, active)).slice(-2);
  }

  /* ---------- parallax (transform only) ---------- */
  var plx = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.parallax-img, .hero-bg'));
  function parallax() {
    plx.forEach(function (el) {
      var host = el.parentNode, r = host.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) return;
      var p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
      el.style.transform = 'translate3d(0,' + (p * -40).toFixed(1) + 'px,0) scale(1.08)';
    });
  }

  /* ---------- screenshot scrolls inside the browser frame ---------- */
  var shots = Array.prototype.slice.call(document.querySelectorAll('[data-scroll-shot]'));
  function scrollShots() {
    if (reduce) return;
    shots.forEach(function (s) {
      var im = s.querySelector('img'); if (!im || !im.naturalHeight) return;
      var r = s.getBoundingClientRect();
      if (r.bottom < -200 || r.top > innerHeight + 200) return;
      var p = Math.max(0, Math.min(1, (innerHeight - r.top) / (innerHeight + r.height)));
      var travel = Math.max(0, im.getBoundingClientRect().height - r.height);
      im.style.transform = 'translate3d(0,' + (-p * travel).toFixed(1) + 'px,0)';
    });
  }

  /* ---------- carousels: only animate while on screen ---------- */
  document.querySelectorAll('[data-marquee], .logo-marquee').forEach(function (m) {
    if (reduce || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (es) { es.forEach(function (e) { m.classList.toggle('run', e.isIntersecting); }); }).observe(m);
  });

  /* ---------- testimonial slider ---------- */
  document.querySelectorAll('[data-slider]').forEach(function (sl) {
    var wrap = sl.closest('section');
    function go(dir) { sl.scrollBy({ left: dir * sl.clientWidth * 0.9, behavior: reduce ? 'auto' : 'smooth' }); }
    var p = wrap.querySelector('[data-t-prev]'), n = wrap.querySelector('[data-t-next]');
    if (p) p.addEventListener('click', function () { go(-1); });
    if (n) n.addEventListener('click', function () { go(1); });
  });

  /* ---------- fallback screenshots (until local captures are added) ---------- */
  document.querySelectorAll('img[data-mshot]').forEach(function (img) {
    var tries = 0;
    function check() {
      if (img.naturalWidth && img.naturalWidth < 400) {
        if (tries++ < 4) { var u = img.src.split('&_r=')[0]; setTimeout(function () { img.src = u + '&_r=' + Date.now(); }, 3000); }
        else img.parentNode.classList.add('noimg');
      } else if (img.naturalWidth) { img.parentNode.classList.add('loaded'); onScroll(); }
    }
    img.addEventListener('load', check); if (img.complete) check();
  });
  document.querySelectorAll('.mb-screen img:not([data-mshot]), .mp-screen img:not([data-mshot])').forEach(function (img) {
    function ok() { img.parentNode.classList.add('loaded'); onScroll(); }
    if (img.complete && img.naturalWidth) ok(); else img.addEventListener('load', ok);
  });

  /* ---------- contact modal ---------- */
  var modal = document.getElementById('contact-modal'), lastFocus = null;
  if (modal) {
    var open = function () { lastFocus = document.activeElement; modal.classList.add('open'); document.body.style.overflow = 'hidden'; var f = modal.querySelector('input'); if (f) f.focus(); };
    var close = function () { modal.classList.remove('open'); document.body.style.overflow = ''; if (lastFocus) lastFocus.focus(); };
    document.querySelectorAll('[data-open-contact]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); if (mm && mm.classList.contains('open')) closeMenu(); open(); }); });
    modal.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', close); });
    addEventListener('keydown', function (e) { if (e.key === 'Escape' && modal.classList.contains('open')) close(); });
    if (location.hash === '#talk') open();
  }

  /* ---------- contact forms ---------- */
  document.querySelectorAll('form[data-contact]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type=submit]'), action = form.getAttribute('action');
      btn.disabled = true;
      if (!action || action === '#') { btn.textContent = 'Sent. We will call you.'; return; }
      fetch(action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) { btn.textContent = r.ok ? 'Sent. We will call you.' : 'That did not send. Call 1300 889 840.'; })
        .catch(function () { btn.textContent = 'That did not send. Call 1300 889 840.'; });
    });
  });

  onScroll();
})();
