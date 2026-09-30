/* =============================================================================
   connectome.js — the hero visual.

   Draws a rotating Drosophila melanogaster with its central nervous system
   inside it: the body as a dim point silhouette, the brain and ventral nerve
   cord as a lit point cloud wired into a proximity graph with signal pulses
   travelling along it. The graph is the point of the thing — it is what the
   connectomic data on VFB looks like.

   Geometry comes from assets/hero/hero-geometry.json, baked by build_hero.py:
     body   flybody, Vaxenburg et al. 2024 (bioRxiv 2024.03.11.584515), Apache-2.0
     brain  VFB JRC2018Unisex adult brain template  (VFB_00101567)
     vnc    VFB JRC2018UnisexVNC adult VNC template (VFB_00200000)

   If the fetch fails the procedural fallback cloud is drawn instead, so the
   hero is never empty. No WebGL, no dependencies. prefers-reduced-motion draws
   a single static frame.
   ============================================================================= */

(function () {
  const canvas = document.getElementById('connectome');
  if (!canvas) return;

  const ctx = canvas.getContext('2d', { alpha: true });
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* deterministic PRNG so the scene is identical on every load */
  let seed = 20240611;
  const rnd = () => {
    seed = (seed * 1664525 + 1013904223) % 4294967296;
    return seed / 4294967296;
  };
  const gauss = () => (rnd() + rnd() + rnd() - 1.5) / 1.5;

  /* --- palette ------------------------------------------------------------ */
  const PAL_DARK = {
    body: [150, 170, 205],
    brain: [140, 120, 255],
    vnc: [53, 231, 224],
    link: [76, 141, 255],
  };
  const PAL_LIGHT = {
    body: [96, 116, 150],
    brain: [110, 70, 210],
    vnc: [14, 150, 145],
    link: [29, 95, 214],
  };
  let PAL = PAL_DARK;
  const syncPalette = () => {
    PAL = document.documentElement.getAttribute('data-theme') === 'light' ? PAL_LIGHT : PAL_DARK;
  };
  syncPalette();
  new MutationObserver(syncPalette).observe(document.documentElement,
    { attributes: true, attributeFilter: ['data-theme'] });

  /* --- scene -------------------------------------------------------------- */
  /* nodes: {x,y,z,r,k} where k indexes KINDS */
  const KINDS = ['body', 'brain', 'vnc'];
  let nodes = [];
  let edges = [];      /* [a, b, long] */
  let pulses = [];
  let ready = false;

  function buildEdges(from, to, radius, maxPerNode) {
    /* Spatial hash — a brute-force pass over ~5k CNS points would stall the
       first frame. */
    const cell = radius;
    const grid = new Map();
    const key = (i, j, k) => i + ',' + j + ',' + k;
    for (let i = from; i < to; i++) {
      const n = nodes[i];
      const k = key(Math.floor(n.x / cell), Math.floor(n.y / cell), Math.floor(n.z / cell));
      let b = grid.get(k);
      if (!b) grid.set(k, (b = []));
      b.push(i);
    }
    const r2 = radius * radius;
    for (let i = from; i < to; i++) {
      const a = nodes[i];
      const gx = Math.floor(a.x / cell), gy = Math.floor(a.y / cell), gz = Math.floor(a.z / cell);
      let made = 0;
      for (let dx = -1; dx <= 1 && made < maxPerNode; dx++)
        for (let dy = -1; dy <= 1 && made < maxPerNode; dy++)
          for (let dz = -1; dz <= 1 && made < maxPerNode; dz++) {
            const b = grid.get(key(gx + dx, gy + dy, gz + dz));
            if (!b) continue;
            for (let t = 0; t < b.length && made < maxPerNode; t++) {
              const j = b[t];
              if (j <= i) continue;
              const o = nodes[j];
              const ddx = a.x - o.x, ddy = a.y - o.y, ddz = a.z - o.z;
              if (ddx * ddx + ddy * ddy + ddz * ddz < r2) { edges.push([i, j, false]); made++; }
            }
          }
    }
  }

  function finalise(cnsFrom, cnsTo) {
    /* long-range links across the CNS — commissures and the neck connective,
       the thing that makes it read as a connectome rather than a dot cloud */
    for (let i = 0; i < 40; i++) {
      const a = cnsFrom + Math.floor(rnd() * (cnsTo - cnsFrom));
      const b = cnsFrom + Math.floor(rnd() * (cnsTo - cnsFrom));
      if (a !== b) edges.push([a, b, true]);
    }
    pulses = Array.from({ length: 22 }, () => ({
      e: Math.floor(rnd() * edges.length),
      t: rnd(),
      v: 0.004 + rnd() * 0.010,
    }));
    ready = true;
  }

  function loadGeometry(url) {
    fetch(url, { credentials: 'same-origin' })
      .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
      .then((d) => {
        nodes = [];
        const push = (flat, kind, jitter) => {
          if (!flat) return [0, 0];
          const from = nodes.length;
          for (let i = 0; i < flat.length; i += 3) {
            nodes.push({
              x: flat[i] / 10000, y: flat[i + 1] / 10000, z: flat[i + 2] / 10000,
              k: kind,
              r: jitter ? 0.40 + rnd() * 0.5 : 0.75 + rnd() * 0.8,
            });
          }
          return [from, nodes.length];
        };
        const bodyRange = push(d.body, 0, true);
        const brainRange = push(d.brain, 1, false);
        const vncRange = push(d.vnc, 2, false);

        /* The bake normalises on the largest extent, which is the wingspan, so
           the fly ends up small in frame. Re-normalise on body length instead
           and let the wing tips run off the edge — that is the better crop. */
        let lo = [1e9, 1e9, 1e9], hi = [-1e9, -1e9, -1e9];
        for (let i = bodyRange[0]; i < bodyRange[1]; i++) {
          const n = nodes[i];
          lo[0] = Math.min(lo[0], n.x); hi[0] = Math.max(hi[0], n.x);
          lo[1] = Math.min(lo[1], n.y); hi[1] = Math.max(hi[1], n.y);
          lo[2] = Math.min(lo[2], n.z); hi[2] = Math.max(hi[2], n.z);
        }
        const cxo = (lo[0] + hi[0]) / 2, cyo = (lo[1] + hi[1]) / 2, czo = (lo[2] + hi[2]) / 2;
        const k = 2 / ((hi[0] - lo[0]) || 1);
        for (const n of nodes) { n.x = (n.x - cxo) * k; n.y = (n.y - cyo) * k; n.z = (n.z - czo) * k; }

        /* The CNS is drawn larger than life about its own centre. At true
           relative scale the brain is ~1/6 of body length and resolves to a
           60px smudge next to a fly that fills the frame; nothing of the graph
           survives. The body stays at true scale as context. This is a figure
           convention, and it is stated in the theme README. */
        /* Legs and wings used to be classified here (wide in y, or hanging
           below in z) and drawn at roughly a third of the torso's alpha, on the
           theory that a side-on fly with prominent appendages reads as a
           spider. With the brain sitting upright in the head that no longer
           holds: the appendages give the silhouette its scale and its posture,
           and suppressing them left the fly looking clipped. The whole body is
           now drawn at one weight. */

        /* Each structure is enlarged about ITS OWN centroid, not about a
           shared one. Scaling the pair together threw the brain forward out of
           the head; scaling separately keeps each where the bake placed it —
           brain in the head, VNC in the thorax — which is the arrangement in
           Hartenstein's stage figures (central brain and optic lobe dorsal in
           the head, suboesophageal below it, thoracico-abdominal ganglion in
           the thorax, joined by a short cervical connective).

           The enlargement is a figure convention: at true relative scale the
           brain is ~1/6 of body length and resolves to a smudge. See README. */
        const CNS_SCALE = 1.0;   /* the brain fills the head at true scale — see README */
        const grow = (from, to, pull) => {
          let sx = 0, sy = 0, sz = 0, n = 0;
          for (let i = from; i < to; i++) { sx += nodes[i].x; sy += nodes[i].y; sz += nodes[i].z; n++; }
          if (!n) return;
          sx /= n; sy /= n; sz /= n;
          for (let i = from; i < to; i++) {
            const q = nodes[i];
            q.x = sx + pull + (q.x - sx) * CNS_SCALE;
            q.y = sy + (q.y - sy) * CNS_SCALE;
            q.z = sz + (q.z - sz) * CNS_SCALE;
          }
        };
        /* pull the two towards each other so the connective stays short */
        grow(brainRange[0], brainRange[1], 0);
        grow(vncRange[0], vncRange[1], 0);

        edges = [];
        /* Link radii are in the normalised frame and sit just above mean point
           spacing: too large and the graph collapses into a smear. */
        buildEdges(brainRange[0], brainRange[1], 0.020, 3);
        buildEdges(vncRange[0], vncRange[1], 0.026, 3);
        /* neck connective: nearest pairs between the two structures */
        for (let i = brainRange[0]; i < brainRange[1]; i += 37) {
          let best = -1, bd = 1e9;
          for (let j = vncRange[0]; j < vncRange[1]; j += 11) {
            const dx = nodes[i].x - nodes[j].x, dy = nodes[i].y - nodes[j].y, dz = nodes[i].z - nodes[j].z;
            const dd = dx * dx + dy * dy + dz * dz;
            if (dd < bd) { bd = dd; best = j; }
          }
          if (best >= 0 && bd < 0.020) edges.push([i, best, true]);
        }
        finalise(brainRange[0], vncRange[1]);
        resize();
        if (reduce) frame(0);
      })
      .catch(() => fallback());
  }

  /* --- procedural fallback ------------------------------------------------ */
  function fallback() {
    nodes = [];
    const blob = (n, cx, cy, cz, rx, ry, rz, kind) => {
      for (let i = 0; i < n; i++) {
        let x, y, z, dd;
        do { x = gauss(); y = gauss(); z = gauss(); dd = x * x + y * y + z * z; } while (dd > 1);
        const s = 0.62 + 0.38 * Math.cbrt(rnd());
        nodes.push({ x: cx + x * rx * s, y: cy + y * ry * s, z: cz + z * rz * s, k: kind, r: 0.7 + rnd() * 1.4 });
      }
    };
    blob(150, -0.55, -0.04, 0, 0.18, 0.24, 0.17, 1);
    blob(150, 0.55, -0.04, 0, 0.18, 0.24, 0.17, 1);
    blob(210, 0, -0.06, 0, 0.28, 0.20, 0.20, 1);
    for (let i = 0; i < 130; i++) {
      const t = i / 130, w = 0.12 * (1 - 0.55 * t);
      nodes.push({ x: gauss() * w, y: 0.30 + t * 0.47, z: gauss() * w * 0.8, k: 2, r: 0.6 + rnd() * 1.1 });
    }
    edges = [];
    buildEdges(0, nodes.length, 0.12, 3);
    finalise(0, nodes.length);
    resize();
    if (reduce) frame(0);
  }

  /* --- render ------------------------------------------------------------- */
  /* Negative yaw swings the head towards the camera; 0 is a flat lateral view
     and -pi/2 is head-on. Three-quarter anterior foreshortens the legs, which
     is the angle that stops it reading as a spider. */
  /* yaw pi is the lateral view from the fly's other side, which puts the head on
     the left; 0 is lateral head-right, negative swings the head to the camera. */
  const VIEW = window.__heroView || { yaw: Math.PI, pitch: -0.24, sway: 0.16 };

  let w = 0, h = 0, dpr = 1, cx = 0, cy = 0, scale = 1;
  let mx = 0, my = 0, tmx = 0, tmy = 0;
  const proj = [];

  function resize() {
    const rect = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = rect.width; h = rect.height;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cx = w * (VIEW.cx != null ? VIEW.cx : (w > 980 ? 0.80 : 0.5));
    cy = h * (VIEW.cy != null ? VIEW.cy : (w > 980 ? 0.40 : 0.47));
    scale = Math.min(w * 0.46, h * 0.95) * (VIEW.zoom != null ? VIEW.zoom : (w > 980 ? 0.74 : 0.62));
  }

  function frame(time) {
    if (!ready) { if (!reduce) requestAnimationFrame(frame); return; }
    const t = reduce ? 0.9 : time * 0.00011;
    mx += (tmx - mx) * 0.05;
    my += (tmy - my) * 0.05;

    /* yaw about the dorso-ventral axis, small pitch so it never looks flat */
    /* Hold near a lateral view and sway, rather than spinning: side-on is the
       only angle where head, thorax and abdomen — and so brain and VNC — are
       all legible at once. */
    const ay = VIEW.yaw + Math.sin(t * 0.62) * VIEW.sway + mx * 0.35;
    const ax = VIEW.pitch + Math.sin(t * 1.1) * 0.06 + my * 0.22;
    const cosY = Math.cos(ay), sinY = Math.sin(ay);
    const cosX = Math.cos(ax), sinX = Math.sin(ax);

    ctx.clearRect(0, 0, w, h);

    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      const x1 = n.x * cosY - n.y * sinY;
      const z1 = n.x * sinY + n.y * cosY;
      const y2 = -n.z * cosX - z1 * sinX;
      const z2 = -n.z * sinX + z1 * cosX;
      const persp = 2.6 / (2.6 + z2);
      proj[i] = { x: cx + x1 * scale * persp, y: cy + y2 * scale * persp, d: z2, p: persp };
    }

    /* body silhouette first, behind everything */
    const bodyCol = PAL.body;
    ctx.fillStyle = `rgb(${bodyCol[0]},${bodyCol[1]},${bodyCol[2]})`;
    for (let i = 0; i < nodes.length; i++) {
      if (nodes[i].k !== 0) continue;
      const p = proj[i];
      const fade = 0.35 + 0.65 * (1 - (p.d + 1) / 2);
      /* Raised from 0.05/0.22 base. At the original values the silhouette read
         as scattered dust rather than a fly, especially on the light theme where
         the body colour is a muted blue-grey on near-white. One weight for the
         whole body, appendages included — see the note above. Depth fade alone
         keeps the outline behind the CNS, which is the subject. */
      ctx.globalAlpha = 0.32 + 0.55 * fade;
      ctx.beginPath();
      ctx.arc(p.x, p.y, nodes[i].r * p.p * 1.45, 0, 6.283);
      ctx.fill();
    }
    ctx.globalAlpha = 1;

    /* CNS graph */
    ctx.lineWidth = 1;
    for (let i = 0; i < edges.length; i++) {
      const e = edges[i];
      const pa = proj[e[0]], pb = proj[e[1]];
      if (!pa || !pb) continue;
      const depth = (pa.d + pb.d) * 0.5;
      const alpha = (e[2] ? 0.13 : 0.26) * (0.35 + 0.65 * (1 - (depth + 1) / 2));
      if (alpha <= 0.012) continue;
      const c = e[2] ? PAL.link : PAL[KINDS[nodes[e[0]].k]];
      ctx.strokeStyle = `rgba(${c[0]},${c[1]},${c[2]},${alpha.toFixed(3)})`;
      ctx.beginPath();
      ctx.moveTo(pa.x, pa.y);
      ctx.lineTo(pb.x, pb.y);
      ctx.stroke();
    }

    /* CNS nodes, painted back to front */
    const order = [];
    for (let i = 0; i < nodes.length; i++) if (nodes[i].k !== 0) order.push(i);
    order.sort((i, j) => proj[j].d - proj[i].d);
    for (const i of order) {
      const p = proj[i], n = nodes[i], c = PAL[KINDS[n.k]];
      const fade = 0.28 + 0.72 * (1 - (p.d + 1) / 2);
      ctx.fillStyle = `rgba(${c[0]},${c[1]},${c[2]},${(fade * 0.55).toFixed(3)})`;
      ctx.beginPath();
      ctx.arc(p.x, p.y, n.r * p.p * (w > 980 ? 1 : 0.8), 0, 6.283);
      ctx.fill();
    }

    /* travelling signals */
    if (!reduce) {
      for (const s of pulses) {
        const e = edges[s.e];
        if (!e) continue;
        const pa = proj[e[0]], pb = proj[e[1]];
        if (!pa || !pb) continue;
        const x = pa.x + (pb.x - pa.x) * s.t;
        const y = pa.y + (pb.y - pa.y) * s.t;
        const g = ctx.createRadialGradient(x, y, 0, x, y, 7);
        g.addColorStop(0, 'rgba(255,255,255,.85)');
        g.addColorStop(0.4, 'rgba(120,200,255,.45)');
        g.addColorStop(1, 'rgba(120,200,255,0)');
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.arc(x, y, 7, 0, 6.283);
        ctx.fill();
        s.t += s.v;
        if (s.t > 1) { s.t = 0; s.e = Math.floor(rnd() * edges.length); }
      }
    }

    if (!reduce) requestAnimationFrame(frame);
  }

  window.addEventListener('resize', () => { resize(); if (reduce) frame(0); }, { passive: true });
  window.addEventListener('pointermove', (e) => {
    tmx = (e.clientX / window.innerWidth - 0.5) * 2;
    tmy = (e.clientY / window.innerHeight - 0.5) * 2;
  }, { passive: true });

  resize();
  if (!reduce) requestAnimationFrame(frame);
  loadGeometry(canvas.dataset.geometry || '/hero/hero-geometry.json');
})();
