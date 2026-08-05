/* =============================================================================
   connectome.js — procedural hero visual.

   Draws a rotating point cloud shaped like a Drosophila central nervous system
   (two optic lobes, central brain, SEZ and a ventral nerve cord), wires nearby
   points into a sparse graph, and runs signal pulses along random edges. No
   external assets, no WebGL, ~6 kB. Honours prefers-reduced-motion by drawing
   a single static frame.
   ============================================================================= */

(function () {
  const canvas = document.getElementById('connectome');
  if (!canvas) return;

  const ctx = canvas.getContext('2d', { alpha: true });
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* deterministic PRNG so the layout is identical on every load */
  let seed = 20240611;
  const rnd = () => {
    seed = (seed * 1664525 + 1013904223) % 4294967296;
    return seed / 4294967296;
  };
  const gauss = () => (rnd() + rnd() + rnd() - 1.5) / 1.5;

  /* --- build the cloud ---------------------------------------------------- */
  const nodes = [];
  function blob(n, cx, cy, cz, rx, ry, rz, kind) {
    for (let i = 0; i < n; i++) {
      let x, y, z, d;
      do {
        x = gauss(); y = gauss(); z = gauss();
        d = x * x + y * y + z * z;
      } while (d > 1);
      // push mass towards the shell — neuropils are hollower than a solid ball
      const s = 0.62 + 0.38 * Math.cbrt(rnd());
      nodes.push({
        x: cx + x * rx * s,
        y: cy + y * ry * s,
        z: cz + z * rz * s,
        k: kind,
        r: 0.7 + rnd() * 1.5,
      });
    }
  }

  blob(150, -0.92, -0.06, 0, 0.30, 0.40, 0.28, 0); // left optic lobe
  blob(150,  0.92, -0.06, 0, 0.30, 0.40, 0.28, 0); // right optic lobe
  blob(210,  0.00, -0.10, 0, 0.46, 0.34, 0.34, 1); // central brain
  blob(70,   0.00,  0.30, 0, 0.26, 0.18, 0.24, 1); // SEZ
  // ventral nerve cord: a tapering column below the brain
  for (let i = 0; i < 130; i++) {
    const t = i / 130;
    const w = 0.20 * (1 - 0.55 * t);
    nodes.push({
      x: gauss() * w,
      y: 0.50 + t * 0.78 + gauss() * 0.03,
      z: gauss() * w * 0.8,
      k: 2,
      r: 0.6 + rnd() * 1.2,
    });
  }

  /* --- wire the graph ----------------------------------------------------- */
  const edges = [];
  const LINK = 0.20;
  for (let i = 0; i < nodes.length; i++) {
    let made = 0;
    for (let j = i + 1; j < nodes.length && made < 3; j++) {
      const a = nodes[i], b = nodes[j];
      const dx = a.x - b.x, dy = a.y - b.y, dz = a.z - b.z;
      const d2 = dx * dx + dy * dy + dz * dz;
      if (d2 < LINK * LINK) { edges.push([i, j, Math.sqrt(d2)]); made++; }
    }
  }
  // a handful of long-range commissures, the thing that makes it read as a brain
  for (let i = 0; i < 26; i++) {
    const a = Math.floor(rnd() * nodes.length);
    const b = Math.floor(rnd() * nodes.length);
    if (a !== b) edges.push([a, b, 1, true]);
  }

  const pulses = Array.from({ length: 16 }, () => ({
    e: Math.floor(rnd() * edges.length),
    t: rnd(),
    v: 0.004 + rnd() * 0.010,
  }));

  /* --- render ------------------------------------------------------------- */
  const PAL_DARK = [
    [164, 107, 255], // violet — optic lobes
    [76, 141, 255],  // brand  — central brain
    [53, 231, 224],  // cyan   — VNC
  ];
  const PAL_LIGHT = [
    [124, 66, 214],
    [29, 95, 214],
    [14, 150, 145],
  ];
  let PAL = PAL_DARK;
  const syncPalette = () => {
    PAL = document.documentElement.getAttribute('data-theme') === 'light' ? PAL_LIGHT : PAL_DARK;
  };
  syncPalette();
  new MutationObserver(syncPalette).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  let w = 0, h = 0, dpr = 1, cx = 0, cy = 0, scale = 1;
  let mx = 0, my = 0, tmx = 0, tmy = 0;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = rect.width; h = rect.height;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    // sit the brain to the right of the headline on wide screens
    cx = w > 980 ? w * 0.70 : w * 0.5;
    cy = h * (w > 980 ? 0.42 : 0.40);
    scale = Math.min(w, h) * (w > 980 ? 0.46 : 0.36);
  }

  const proj = [];
  function frame(time) {
    const t = reduce ? 0 : time * 0.00013;
    mx += (tmx - mx) * 0.05;
    my += (tmy - my) * 0.05;

    const ay = t + mx * 0.5;
    const ax = -0.22 + Math.sin(t * 1.7) * 0.06 + my * 0.28;
    const cosY = Math.cos(ay), sinY = Math.sin(ay);
    const cosX = Math.cos(ax), sinX = Math.sin(ax);

    ctx.clearRect(0, 0, w, h);

    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      const x1 = n.x * cosY - n.z * sinY;
      const z1 = n.x * sinY + n.z * cosY;
      const y2 = n.y * cosX - z1 * sinX;
      const z2 = n.y * sinX + z1 * cosX;
      const persp = 2.6 / (2.6 + z2);
      proj[i] = {
        x: cx + x1 * scale * persp,
        y: cy + y2 * scale * persp,
        d: z2,
        p: persp,
      };
    }

    /* edges */
    ctx.lineWidth = 1;
    for (let i = 0; i < edges.length; i++) {
      const [a, b, len, long] = edges[i];
      const pa = proj[a], pb = proj[b];
      const depth = (pa.d + pb.d) * 0.5;
      const alpha = (long ? 0.10 : 0.20) * (0.35 + 0.65 * (1 - (depth + 1) / 2));
      if (alpha <= 0.01) continue;
      const c = PAL[nodes[a].k];
      ctx.strokeStyle = `rgba(${c[0]},${c[1]},${c[2]},${alpha.toFixed(3)})`;
      ctx.beginPath();
      ctx.moveTo(pa.x, pa.y);
      ctx.lineTo(pb.x, pb.y);
      ctx.stroke();
    }

    /* nodes, painted back to front */
    const order = proj.map((p, i) => i).sort((i, j) => proj[j].d - proj[i].d);
    for (const i of order) {
      const p = proj[i], n = nodes[i];
      const c = PAL[n.k];
      const fade = 0.30 + 0.70 * (1 - (p.d + 1) / 2);
      ctx.fillStyle = `rgba(${c[0]},${c[1]},${c[2]},${(fade * 0.85).toFixed(3)})`;
      ctx.beginPath();
      ctx.arc(p.x, p.y, n.r * p.p * (w > 980 ? 1 : 0.8), 0, 6.283);
      ctx.fill();
    }

    /* travelling signals */
    if (!reduce) {
      for (const s of pulses) {
        const e = edges[s.e];
        const pa = proj[e[0]], pb = proj[e[1]];
        const x = pa.x + (pb.x - pa.x) * s.t;
        const y = pa.y + (pb.y - pa.y) * s.t;
        const g = ctx.createRadialGradient(x, y, 0, x, y, 9);
        g.addColorStop(0, 'rgba(255,255,255,.85)');
        g.addColorStop(0.4, 'rgba(120,200,255,.45)');
        g.addColorStop(1, 'rgba(120,200,255,0)');
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.arc(x, y, 9, 0, 6.283);
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
  if (reduce) frame(0); else requestAnimationFrame(frame);
})();
