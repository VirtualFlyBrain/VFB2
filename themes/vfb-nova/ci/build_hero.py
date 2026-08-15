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
  themes/vfb-nova/assets/hero/hero-geometry.json
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
OUT = pathlib.Path('/tmp/vfb2/themes/vfb-nova/assets/hero/hero-geometry.json')

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

def rotate_y(pts, deg):
    """Rotate about the medio-lateral axis, through the cloud's own mean point.

    y is the axis the hero camera looks down — connectome.js projects with
    yaw = pi, so screen-right is -x and screen-up is +z. A positive angle here
    is therefore anticlockwise as the visitor sees it: it carries screen-right
    round to screen-up. This sets a structure's pitch within the sagittal
    plane, which `axis_ranks` cannot express — that only assigns whole axes to
    whole axes, so it can put the brain's long axis medio-laterally but not
    tell you which way up the gnathal region ends.

    The pivot is the mean rather than the bounding-box centre, so the structure
    turns about its own mass and does not drift within the cavity.
    """
    t = math.radians(deg)
    c, s = math.cos(t), math.sin(t)
    cx = sum(p[0] for p in pts) / len(pts)
    cz = sum(p[2] for p in pts) / len(pts)
    out = []
    for x, y, z in pts:
        dx, dz = x - cx, z - cz
        out.append((cx + dx * c + dz * s, y, cz - dx * s + dz * c))
    return out

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
def extents(pts):
    lo, hi = bbox(pts)
    return [hi[i] - lo[i] for i in range(3)]

def fit_into(pts, cavity, scale=None, fill=None, axis_ranks=(1, 0, 2),
             flip=(), offset=(0.0, 0.0, 0.0)):
    """Orient, scale and centre a CNS mesh inside a body cavity.

    `axis_ranks` gives, for each MODEL axis (x = antero-posterior, y =
    medio-lateral, z = dorso-ventral), which of the structure's extents goes
    there by rank — 0 being its longest.

      brain  580 x 259 x 159 um   (1, 0, 2)
             longest is medio-lateral -> y; next antero-posterior -> x;
             shortest dorso-ventral -> z
      VNC    422 x 177 x 127 um   (0, 1, 2)
             longest runs head-to-abdomen -> x; next left/right -> y;
             flattest towards the back and wings -> z

    Nothing is inferred from the cavity. Two earlier bugs came from ranking the
    cavity's extents to decide the remaining axes: the head is 905 vs 913 um and
    the thorax 0.1060 vs 0.1077 cm in the relevant pairs, so both were settled on
    a hair's breadth, and both settled wrongly — the brain ended up on its side
    and the VNC flat-side-on.

    `flip` mirrors the given model axes after placement, for the sign ambiguities
    that no extent can resolve.
    """
    se, ce = extents(pts), extents(cavity)
    s_order = sorted(range(3), key=lambda i: -se[i])       # structure axes, longest first
    mapping = {m: s_order[r] for m, r in enumerate(axis_ranks)}

    if scale is None:
        scale = min((ce[c] * fill) / se[mapping[c]] for c in range(3) if se[mapping[c]] > 0)

    sc, cc = centre(pts), centre(cavity)
    out = []
    for q in pts:
        v = [q[i] - sc[i] for i in range(3)]
        out.append([v[mapping[c]] * scale + cc[c] + offset[c] for c in range(3)])

    for axis in flip:
        pivot = cc[axis] + offset[axis]
        for q in out:
            q[axis] = 2 * pivot - q[axis]

    return [tuple(q) for q in out], scale

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

    brain_raw = voxel_downsample(load_obj(MESHES / 'VFB_00101567.obj'), 1600)
    vnc_raw = voxel_downsample(load_obj(MESHES / 'VFB_00200000.obj'), 900)
    print('  brain extents um', [round(x) for x in extents(brain_raw)])
    print('  vnc   extents um', [round(x) for x in extents(vnc_raw)])
    print('  head  extents cm', [round(x, 4) for x in extents(seg['head'])])
    print('  thorax extents cm', [round(x, 4) for x in extents(seg['thorax'])])

    # The brain fills the head capsule; the VNC sits in the ventral thorax, so it
    # takes a smaller share and is pushed down and back a little.
    # Size comes from the true micron-to-centimetre conversion, NOT from filling
    # the cavity. JRC2018Unisex does not include the lamina — the optic lobe in
    # that template starts at the medulla — so scaling the mesh to fill the head
    # would push the medulla out to where the lamina and retina actually are.
    # The gap between the mesh and the eye is correct for what the mesh contains.
    # fit_into is used only to orient and centre.
    # Brain: widest axis is medio-lateral; gnathal region narrow and ventral.
    # Signs are set by inspection, not inferred: the medio-lateral taper test I
    # tried separates neither structure reliably (brain 0.0101 vs 0.0139, VNC
    # 0.00298 vs 0.00303). Confirmed against the reference figures — the central
    # complex V points ventrally, and the abdominal neuromere sits posteriorly.
    # The durable fix is to derive both from VFB's own painted domains on each
    # template rather than from shape statistics. See README.
    brain, bs = fit_into(brain_raw, seg['head'], scale=UM_TO_CM,
                         axis_ranks=(1, 0, 2), flip=(2,))
    # axis_ranks leaves the brain tipped, with the gnathal region pointing
    # antero-ventrally rather than straight down. 45 deg anticlockwise in the
    # sagittal plane (as seen from the fly's left, which is the hero's
    # viewpoint) brings it upright.
    brain = rotate_y(brain, 45)
    vnc, vs = fit_into(vnc_raw, seg['thorax'], scale=UM_TO_CM,
                       axis_ranks=(0, 1, 2), flip=(0,),
                       # forward in the thorax, close under the neck connective
                       offset=(0.014, 0.0, -0.012))
    print('  fitted brain scale %.4f (um->cm implies %.4f)' % (bs, UM_TO_CM))
    print('  fitted vnc   scale %.4f' % vs)

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
