#!/usr/bin/env python3
"""Bake the hero geometry into a single small JSON asset.

Inputs
  * flybody (Vaxenburg et al. 2024, bioRxiv 2024.03.11.584515; Apache-2.0) —
    MuJoCo whole-body model of Drosophila melanogaster, ~85 mesh parts placed
    by a kinematic tree. Used for the body silhouette only.
  * VFB template meshes, fetched from virtualflybrain.org/data:
      JRC2018Unisex adult brain   VFB_00101567
      JRC2018UnisexVNC adult VNC  VFB_00200000

Output
  themes/vfb-nova/assets/data/hero-geometry.json
    { body: [...], brain: [...], vnc: [...] } — voxel-downsampled point sets in
    one normalised frame, quantised to int16 (1/10000 of the frame).

The CNS is placed inside the body by segment centroid and scaled from microns
to the model's centimetres. That is anatomically sensible, not a registration:
the two sources have no common coordinate frame.
"""
import json, math, pathlib
import xml.etree.ElementTree as ET

FLYBODY = pathlib.Path('/tmp/flybody/flybody/fruitfly/assets')
MESHES = pathlib.Path('/tmp/meshes')
OUT = pathlib.Path('/tmp/vfb2/themes/vfb-nova/assets/data/hero-geometry.json')

UM_TO_CM = 1e-4

# ---------------------------------------------------------------- quaternions
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return (w1*w2 - x1*x2 - y1*y2 - z1*z2,
            w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2,
            w1*z2 + x1*y2 - y1*x2 + z1*w2)

def qrot(q, v):
    w, x, y, z = q; vx, vy, vz = v
    tx = 2*(y*vz - z*vy); ty = 2*(z*vx - x*vz); tz = 2*(x*vy - y*vx)
    return (vx + w*tx + (y*tz - z*ty),
            vy + w*ty + (z*tx - x*tz),
            vz + w*tz + (x*ty - y*tx))

def parse_q(s):
    if not s: return (1.0, 0.0, 0.0, 0.0)
    v = [float(x) for x in s.split()]
    n = math.sqrt(sum(c*c for c in v)) or 1.0
    return tuple(c/n for c in v)

def parse_v(s, d=(0.0, 0.0, 0.0)):
    return tuple(float(x) for x in s.split()) if s else d

# --------------------------------------------------------------------- meshes
def load_obj(path):
    pts = []
    with open(path) as fh:
        for line in fh:
            if line.startswith('v '):
                p = line.split()
                pts.append((float(p[1]), float(p[2]), float(p[3])))
    return pts

def voxel_downsample(pts, target):
    """Grid-average towards `target` points: keeps the shape, kills clumping."""
    if not pts or len(pts) <= target:
        return list(pts)
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; zs = [p[2] for p in pts]
    span = max(max(xs)-min(xs), max(ys)-min(ys), max(zs)-min(zs)) or 1.0
    n, grid = 8, {}
    for _ in range(45):
        cell = span / n
        grid = {}
        for p in pts:
            k = (int(p[0]//cell), int(p[1]//cell), int(p[2]//cell))
            g = grid.get(k)
            if g is None: grid[k] = [p[0], p[1], p[2], 1]
            else:
                g[0] += p[0]; g[1] += p[1]; g[2] += p[2]; g[3] += 1
        if len(grid) >= target:
            break
        n = int(n * 1.3) + 1
    return [(g[0]/g[3], g[1]/g[3], g[2]/g[3]) for g in grid.values()]

def bbox(pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; zs = [p[2] for p in pts]
    return (min(xs), min(ys), min(zs)), (max(xs), max(ys), max(zs))

def centre(pts):
    lo, hi = bbox(pts)
    return tuple((a+b)/2 for a, b in zip(lo, hi))

# ------------------------------------------------------- assemble the fly body
SEGMENTS = ('head', 'thorax', 'abdomen')

def assemble_body():
    root = ET.parse(FLYBODY / 'fruitfly.xml').getroot()

    # <default><mesh scale="0.1 0.1 0.1"/> applies to every mesh asset that does
    # not override it. Missing this makes the whole fly ten times too large.
    dscale = (1.0, 1.0, 1.0)
    d = root.find('default')
    if d is not None and d.find('mesh') is not None:
        dscale = parse_v(d.find('mesh').get('scale'), (1.0, 1.0, 1.0))

    assets = {}
    for m in root.find('asset').findall('mesh'):
        assets[m.get('name')] = (m.get('file'), parse_v(m.get('scale'), dscale))

    pts, seg_pts = [], {s: [] for s in SEGMENTS}

    def walk(body, ppos, pquat, seg):
        name = body.get('name') or ''
        # Only the body-wall segments themselves: the leg chains are children of
        # the thorax, and letting them inherit its label drags the centroid the
        # VNC is placed on down into the legs.
        if name in SEGMENTS or name.startswith('abdomen_'):
            seg = 'abdomen' if name.startswith('abdomen') else name
        elif name and seg and not name.startswith(seg):
            seg = None
        pos = parse_v(body.get('pos'))
        wq = qmul(pquat, parse_q(body.get('quat')))
        wp = tuple(a + b for a, b in zip(ppos, qrot(pquat, pos)))
        for g in body.findall('geom'):
            mname = g.get('mesh')
            if not mname or g.get('class') == 'collision':
                continue
            file, scale = assets.get(mname, (None, dscale))
            if not file:
                continue
            gwq = qmul(wq, parse_q(g.get('quat')))
            gwp = tuple(a + b for a, b in zip(wp, qrot(wq, parse_v(g.get('pos')))))
            # Cap generously per part, then downsample once globally: a hard
            # per-part cap over-represents the many small leg segments and
            # under-represents the head and thorax, which is exactly where the
            # silhouette needs to read.
            verts = voxel_downsample(load_obj(FLYBODY / file), 3000)
            for v in verts:
                rv = qrot(gwq, (v[0]*scale[0], v[1]*scale[1], v[2]*scale[2]))
                w = (gwp[0]+rv[0], gwp[1]+rv[1], gwp[2]+rv[2])
                pts.append(w)
                if seg:
                    seg_pts[seg].append(w)
        for child in body.findall('body'):
            walk(child, wp, wq, seg)

    for b in root.find('worldbody').findall('body'):
        walk(b, (0.0, 0.0, 0.0), (1.0, 0.0, 0.0, 0.0), None)
    return pts, seg_pts

# ----------------------------------------------------------------- CNS pieces
def place(pts, axis_map, signs, scale, target_centre):
    """Reorder VFB image axes onto the model's (x=anterior, y=lateral, z=dorsal)
    frame, scale microns to centimetres, then centre on a body segment."""
    c = centre(pts)
    out = []
    for p in pts:
        v = [(p[i] - c[i]) * scale for i in range(3)]
        out.append(tuple(signs[i] * v[axis_map[i]] + target_centre[i] for i in range(3)))
    return out

def main():
    print('assembling fly body …')
    body, seg = assemble_body()
    print('  raw points:', len(body))
    body = voxel_downsample(body, 9000)
    lo, hi = bbox(body)
    print('  points:', len(body))
    print('  bbox (cm):', [round(x, 4) for x in lo], [round(x, 4) for x in hi])
    for s in SEGMENTS:
        if seg[s]:
            print('  %-8s centroid %s' % (s, [round(x, 4) for x in centre(seg[s])]))

    head_c = centre(seg['head'])
    thorax_c = centre(seg['thorax'])

    brain_raw = voxel_downsample(load_obj(MESHES / 'VFB_00101567.obj'), 1100)
    vnc_raw = voxel_downsample(load_obj(MESHES / 'VFB_00200000.obj'), 620)
    print('  brain pts', len(brain_raw), 'bbox µm', [round(x) for x in bbox(brain_raw)[1]])
    print('  vnc   pts', len(vnc_raw), 'bbox µm', [round(x) for x in bbox(vnc_raw)[1]])

    # VFB image axes → model axes.
    #   brain: x = medio-lateral, y = antero-posterior, z = dorso-ventral
    #   model: x = antero-posterior (head at +x), y = lateral, z = dorsal
    brain = place(brain_raw, axis_map=(1, 0, 2), signs=(-1, 1, -1),
                  scale=UM_TO_CM, target_centre=head_c)
    # The VNC sits in the thorax, running antero-posteriorly and tilted ventrally.
    vnc = place(vnc_raw, axis_map=(1, 0, 2), signs=(-1, 1, -1),
                scale=UM_TO_CM,
                target_centre=(thorax_c[0] - 0.004, thorax_c[1], thorax_c[2] - 0.012))

    # ---- normalise everything into one frame centred on the body -------------
    allpts = body + brain + vnc
    lo, hi = bbox(allpts)
    c = tuple((a+b)/2 for a, b in zip(lo, hi))
    half = max(hi[i] - lo[i] for i in range(3)) / 2 or 1.0

    def norm(pts):
        """Flat [x,y,z,x,y,z,…] — a third smaller than nested arrays."""
        out = []
        for p in pts:
            for i in range(3):
                out.append(int(round(max(-1.0, min(1.0, (p[i]-c[i])/half)) * 10000)))
        return out

    data = {
        'units': 'int16, 10000 = one half-extent of the combined bounding box',
        'sources': {
            'body': 'flybody, Vaxenburg et al. 2024 (bioRxiv 2024.03.11.584515), Apache-2.0',
            'brain': 'VFB JRC2018Unisex adult brain template, VFB_00101567',
            'vnc': 'VFB JRC2018UnisexVNC adult VNC template, VFB_00200000',
        },
        'note': 'CNS placed by segment centroid, not registered to the body model.',
        'body': norm(body), 'brain': norm(brain), 'vnc': norm(vnc),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, separators=(',', ':')))
    print('wrote', OUT, '%.0f kB' % (OUT.stat().st_size / 1024))
    print('  counts: body=%d brain=%d vnc=%d' % (len(body), len(brain), len(vnc)))

if __name__ == '__main__':
    main()
