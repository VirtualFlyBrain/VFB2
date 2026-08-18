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
  const solrURL = pal.dataset.solr;
  const browserURL = pal.dataset.browser;
  let docs = null;
  let sel = 0;
  let seq = 0;            /* guards against out-of-order SOLR responses */
  let termCtl = null;     /* aborts the in-flight SOLR request when typing */
  let termTimer = null;

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

  /* --- anatomy terms, live from SOLR ---------------------------------------
     The ~763k generated term pages are not in the Hugo index, so the site
     search alone answers "medulla" with nothing. These come from the same
     ontology core and the same query the 3D browser's own search uses
     (geppetto-vfb searchConfiguration.js): identical qf/pf/bq/fq weighting, so
     ranking matches what users get in the browser. rows is 8 rather than 500
     because this is a palette, not a results page.

     Fails silently. SOLR being down must never break search over site pages. */
  const SOLR_FQ = [
    '(short_form:VFB* OR short_form:FB* OR facets_annotation:DataSet OR facets_annotation:pub) AND NOT short_form:VFBc_*',
    'NOT facets_annotation:Deprecated',
  ];
  const SOLR_BQ = 'short_form:VFBexp*^10.0 short_form:VFB*^50.0 facets_annotation:Class^200.0 ' +
    'short_form:FBbt*^150.0 short_form:FBbt_00003982^2 facets_annotation:Deprecated^0.001 ' +
    'facets_annotation:DataSet^500.0 facets_annotation:pub^100.0';

  /* SOLR labels can carry a stray backslash before a quote from over-escaped
     source data ("y5B\'2a" for "y5B'2a"). Never legitimate; safe to strip. */
  const cleanLabel = (l) => (typeof l === 'string' ? l.replace(/\\(['"])/g, '$1') : l);

  async function fetchTerms(q, mine) {
    if (!solrURL || q.length < 2) return null;
    if (termCtl) termCtl.abort();
    termCtl = new AbortController();
    const p = new URLSearchParams({
      q: q, 'q.op': 'OR', defType: 'edismax', mm: '45%',
      qf: 'label^110 synonym^100 label_autosuggest synonym_autosuggest shortform_autosuggest',
      pf: 'label^250 synonym^120', ps: '0',
      fl: 'short_form,label,unique_facets',
      bq: SOLR_BQ, rows: '8', start: '0', wt: 'json',
    });
    SOLR_FQ.forEach((f) => p.append('fq', f));
    try {
      const r = await fetch(solrURL + '?' + p.toString(), { signal: termCtl.signal });
      if (!r.ok) return null;
      const j = await r.json();
      if (mine !== seq) return null;      /* a newer query has since been typed */
      return (j.response && j.response.docs) || [];
    } catch (e) { return null; }
  }

  function termsHTML(terms, q) {
    if (!terms || !terms.length) return '';
    return '<li class="palette__group" aria-hidden="true">Anatomy terms &middot; opens in the 3D browser</li>' +
      terms.map((t) => {
        const label = cleanLabel(t.label) || t.short_form;
        const facets = (t.unique_facets || []).slice(0, 3).join(' · ');
        return '<li class="res">' +
          '<a href="' + browserURL + '?id=' + encodeURIComponent(t.short_form) + '" target="_blank" rel="noopener">' +
            '<i class="r-icon fas fa-diagram-project"></i>' +
            '<span class="r-title">' + mark(label, q) +
              '<span class="r-desc">' + esc(t.short_form) + (facets ? ' — ' + esc(facets) : '') + '</span>' +
            '</span>' +
            '<span class="r-sec">term</span>' +
          '</a></li>';
      }).join('');
  }

  function render(q) {
    const items = (docs || [])
      .map((d) => ({ d, s: score(d, q) }))
      .filter((x) => x.s < 99)
      .sort((a, b) => a.s - b.s || a.d.title.length - b.d.title.length)
      .slice(0, 24);

    sel = 0;
    const pageHTML = (x) => {
      const d = x.d;
      const icon = ICONS[d.section] || ICONS[''];
      return '<li class="res">' +
        '<a href="' + d.url + '">' +
          '<i class="r-icon fas ' + icon + '"></i>' +
          '<span class="r-title">' + mark(d.title, q) +
            (d.desc ? '<span class="r-desc">' + esc(d.desc) + '</span>' : '') +
          '</span>' +
          '<span class="r-sec">' + esc(d.section || 'page') + '</span>' +
        '</a></li>';
    };

    /* A page whose *title* matches outranks any anatomy term: someone typing
       "solr api" wants the doc. A page that merely mentions the word in its
       body does not — "medulla" must not bury the medulla under two API
       tutorials that happen to use it as their example query. So title-tier
       hits sit above the terms group and the rest below it. */
    const strongHTML = items.filter((x) => x.s <= 2).map(pageHTML).join('');
    const weakHTML = items.filter((x) => x.s > 2).map(pageHTML).join('');
    const pagesHTML = strongHTML + weakHTML;

    const mine = ++seq;
    list.innerHTML = pagesHTML || '<li class="palette__empty">Searching anatomy terms…</li>';
    markFirst();

    fetchTerms(q, mine).then((terms) => {
      if (mine !== seq) return;
      const th = termsHTML(terms, q);
      if (!pagesHTML && !th) {
        list.innerHTML = '<li class="palette__empty">No match for “' + esc(q) + '”.</li>';
        return;
      }
      list.innerHTML = th ? strongHTML + th + weakHTML : pagesHTML;
      markFirst();
    });
  }

  function markFirst() {
    const first = list.querySelector('li.res');
    if (first) first.classList.add('is-sel');
    sel = 0;
  }

  function recent() {
    list.innerHTML = (docs || []).filter((d) => d.pinned).slice(0, 8).map((d, i) =>
      '<li class="res ' + (i === 0 ? 'is-sel' : '') + '"><a href="' + d.url + '">' +
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
    const items = $$('#palette-results li.res');
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
      if (a) {
        e.preventDefault();
        /* term results carry target=_blank; Enter should honour that too */
        if (a.target === '_blank') window.open(a.href, '_blank', 'noopener');
        else window.location.href = a.getAttribute('href');
      }
    }
  });
})();
