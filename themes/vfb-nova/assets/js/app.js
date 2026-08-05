/* =============================================================================
   app.js — theme, navigation, scroll behaviour and the ⌘K palette.
   No framework, no dependencies.
   ============================================================================= */

(function () {
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  /* --- theme -------------------------------------------------------------- */
  const root = document.documentElement;
  const setTheme = (t) => {
    root.setAttribute('data-theme', t);
    try { localStorage.setItem('vfb-theme', t); } catch (e) { /* private mode */ }
    $$('.js-theme i').forEach((i) => {
      i.className = t === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    });
  };
  $$('.js-theme').forEach((b) => b.addEventListener('click', () => {
    setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  }));
  setTheme(root.getAttribute('data-theme') || 'dark');

  /* --- sticky nav + reading progress -------------------------------------- */
  const nav = $('.nav');
  const bar = $('.progress');
  const onScroll = () => {
    const y = window.scrollY;
    if (nav) nav.classList.toggle('is-stuck', y > 8);
    if (bar) {
      const max = document.body.scrollHeight - window.innerHeight;
      bar.style.width = max > 0 ? (y / max) * 100 + '%' : '0';
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* --- mobile menu -------------------------------------------------------- */
  const burger = $('.nav__burger');
  const links = $('.nav__links');
  if (burger && links) {
    burger.addEventListener('click', () => {
      const open = links.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', String(open));
    });
  }

  /* --- docs sidebar: collapsed on narrow screens --------------------------- */
  const side = $('.doc__side');
  if (side) {
    const narrow = window.matchMedia('(max-width: 900px)');
    const sync = () => { if (narrow.matches) side.removeAttribute('open'); else side.setAttribute('open', ''); };
    sync();
    narrow.addEventListener('change', sync);
  }

  /* --- reveal on scroll --------------------------------------------------- */
  const io = 'IntersectionObserver' in window
    ? new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 })
    : null;
  const revealables = $$('.reveal');
  revealables.forEach((el, i) => {
    el.style.transitionDelay = Math.min(i % 6, 5) * 60 + 'ms';
    if (io) io.observe(el); else el.classList.add('is-in');
  });
  /* Safety net: never leave content invisible if the observer never fires
     (printing, in-page find, a browser that throttles the callback). */
  setTimeout(() => revealables.forEach((el) => el.classList.add('is-in')), 4000);
  window.addEventListener('beforeprint', () => revealables.forEach((el) => el.classList.add('is-in')));

  /* blocks/link-down: scroll to whatever follows the hero */
  $$('.link-down').forEach((a) => a.addEventListener('click', (e) => {
    e.preventDefault();
    const hero = $('.hero');
    const next = hero && (hero.nextElementSibling || hero.parentElement.nextElementSibling);
    (next || document.body).scrollIntoView({ behavior: 'smooth', block: 'start' });
  }));

  /* --- pointer sheen on cards --------------------------------------------- */
  $$('.card').forEach((c) => {
    c.addEventListener('pointermove', (e) => {
      const r = c.getBoundingClientRect();
      c.style.setProperty('--mx', ((e.clientX - r.left) / r.width) * 100 + '%');
      c.style.setProperty('--my', ((e.clientY - r.top) / r.height) * 100 + '%');
    });
  });

  /* --- copy buttons on code blocks ---------------------------------------- */
  $$('.highlight, .prose pre').forEach((block) => {
    const pre = block.matches('pre') ? block : block.querySelector('pre');
    if (!pre) return;
    const host = block.matches('.highlight') ? block : pre.parentElement;
    if (!host || host.querySelector('.copy-btn')) return;
    if (getComputedStyle(host).position === 'static') host.style.position = 'relative';
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = 'copy';
    btn.addEventListener('click', () => {
      navigator.clipboard.writeText(pre.innerText).then(() => {
        btn.textContent = 'copied';
        setTimeout(() => (btn.textContent = 'copy'), 1600);
      });
    });
    host.appendChild(btn);
  });

  /* --- on-this-page scroll spy -------------------------------------------- */
  const tocLinks = $$('.doc__toc a');
  if (tocLinks.length) {
    const targets = tocLinks
      .map((a) => {
        const id = decodeURIComponent(a.getAttribute('href') || '').replace(/^.*#/, '');
        return id ? document.getElementById(id) : null;
      })
      .filter(Boolean);
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        tocLinks.forEach((a) => a.classList.remove('is-active'));
        const hit = tocLinks.find((a) => decodeURIComponent(a.getAttribute('href')).endsWith('#' + e.target.id));
        if (hit) hit.classList.add('is-active');
      });
    }, { rootMargin: '-80px 0px -70% 0px' });
    targets.forEach((t) => spy.observe(t));
  }

  /* --- command palette ----------------------------------------------------- */
  const pal = $('.palette');
  if (!pal) return;
  const input = $('#palette-input');
  const list = $('#palette-results');
  const indexURL = pal.dataset.index;
  let docs = null;
  let sel = 0;

  const ICONS = {
    docs: 'fa-book', blog: 'fa-newspaper', about: 'fa-circle-info',
    hosted: 'fa-server', term: 'fa-diagram-project', '': 'fa-file-lines',
  };

  async function load() {
    if (docs) return docs;
    try {
      const r = await fetch(indexURL, { credentials: 'same-origin' });
      docs = await r.json();
    } catch (e) { docs = []; }
    return docs;
  }

  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  function mark(text, q) {
    if (!q) return esc(text);
    const i = text.toLowerCase().indexOf(q);
    if (i < 0) return esc(text);
    return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length));
  }

  function score(d, q) {
    const t = d.title.toLowerCase();
    if (t === q) return 0;
    if (t.startsWith(q)) return 1;
    if (t.includes(q)) return 2;
    if ((d.section || '').toLowerCase().includes(q)) return 4;
    if ((d.desc || '').toLowerCase().includes(q)) return 5;
    if ((d.body || '').toLowerCase().includes(q)) return 7;
    return 99;
  }

  function render(q) {
    const items = (docs || [])
      .map((d) => ({ d, s: score(d, q) }))
      .filter((x) => x.s < 99)
      .sort((a, b) => a.s - b.s || a.d.title.length - b.d.title.length)
      .slice(0, 24);

    if (!items.length) {
      list.innerHTML = '<li class="palette__empty">No match for “' + esc(q) + '”. ' +
        'Anatomy terms live in the <a href="/term/">term index</a>.</li>';
      return;
    }
    sel = 0;
    list.innerHTML = items.map((x, i) => {
      const d = x.d;
      const icon = ICONS[d.section] || ICONS[''];
      return '<li class="' + (i === 0 ? 'is-sel' : '') + '">' +
        '<a href="' + d.url + '">' +
          '<i class="r-icon fas ' + icon + '"></i>' +
          '<span class="r-title">' + mark(d.title, q) +
            (d.desc ? '<span class="r-desc">' + esc(d.desc) + '</span>' : '') +
          '</span>' +
          '<span class="r-sec">' + esc(d.section || 'page') + '</span>' +
        '</a></li>';
    }).join('');
  }

  function recent() {
    list.innerHTML = (docs || []).filter((d) => d.pinned).slice(0, 8).map((d, i) =>
      '<li class="' + (i === 0 ? 'is-sel' : '') + '"><a href="' + d.url + '">' +
      '<i class="r-icon fas ' + (ICONS[d.section] || ICONS['']) + '"></i>' +
      '<span class="r-title">' + esc(d.title) + '</span>' +
      '<span class="r-sec">' + esc(d.section || 'page') + '</span></a></li>').join('');
    sel = 0;
  }

  async function open() {
    pal.hidden = false;
    document.body.style.overflow = 'hidden';
    await load();
    recent();
    input.value = '';
    input.focus();
  }
  function close() {
    pal.hidden = true;
    document.body.style.overflow = '';
  }

  $$('.js-search').forEach((b) => b.addEventListener('click', open));
  pal.addEventListener('click', (e) => { if (e.target === pal) close(); });
  $('.js-close-palette')?.addEventListener('click', close);

  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    if (!q) return recent();
    render(q);
  });

  function move(step) {
    const items = $$('#palette-results li');
    if (!items.length) return;
    items[sel]?.classList.remove('is-sel');
    sel = (sel + step + items.length) % items.length;
    items[sel].classList.add('is-sel');
    items[sel].scrollIntoView({ block: 'nearest' });
  }

  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); pal.hidden ? open() : close(); return; }
    if (e.key === '/' && !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName) && pal.hidden) { e.preventDefault(); open(); return; }
    if (pal.hidden) return;
    if (e.key === 'Escape') { close(); }
    else if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter') {
      const a = $('#palette-results li.is-sel a');
      if (a) { e.preventDefault(); window.location.href = a.getAttribute('href'); }
    }
  });
})();
