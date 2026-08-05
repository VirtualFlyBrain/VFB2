# vfb-nova

A second presentation layer for the Virtual Fly Brain static site. It renders
the existing `content/en` tree — every markdown file, the generated term pages,
the home page shortcodes — with no content changes and no Docsy.

## Run it

```bash
hugo server --config hugo.nova.toml     # side by side with the current site
hugo --config hugo.nova.toml            # build to public/
```

`config.toml` is untouched, so the Docsy build keeps working exactly as before.
The two configs can be built from the same checkout. `Dockerfile.nova` and
`.github/workflows/nova-build.yml` build and check this config only.

## Toolchain

Verified on **Hugo 0.164.0, standard edition** — zero warnings, zero errors.
Output is byte-identical between the standard and extended editions.

| | |
|---|---|
| Hugo edition | **standard** — extended is not required |
| Dart Sass | not required |
| Node / npm | not required |
| Runtime CDN requests | none |

The theme ships plain CSS concatenated by `resources.Concat`, not Sass. LibSass
was deprecated in Hugo v0.153.0 and Dart Sass is a separate binary the build
host would have to install; avoiding both removes the migration and drops the
extended-edition requirement.

Minimum version is 0.128.0 (`[pagination] pagerSize`). The repo's existing
`Dockerfile` pins `klakegg/hugo`, which is unmaintained and too old — use
`Dockerfile.nova` or the workflow instead.

### Two config keys that are not optional on current Hugo

Both apply to the Docsy build too, and `config.toml` will need them before it
can move past Hugo 0.162:

```toml
[security]
  allowContent = ['^text/html$', '^text/markdown$']   # content/en/_index.html
```
Hugo ≥ 0.163 refuses `text/html` content files by default. Without this the
build fails at assembly with `access denied: "text/html" is not whitelisted`.

`cascade._target` was renamed to `cascade.target` in v0.156.0. Both are fixed on
this branch.

## Building at scale

The site's real size is the generated term corpus, not the ~130 authored pages.
Measured on this branch with a synthetic corpus shaped like `vfbterms.py`
output (Hugo 0.164.0 standard, 8-core container):

| pages | wall | peak RSS |
|------:|-----:|---------:|
| 186 (authored only) | 3.0 s | 1.16 GB |
| 5,180 | 7.9 s | 1.77 GB |
| 40,182 | 59.4 s | 3.59 GB |

Marginal cost is **~1.4 ms and ~60 kB of RSS per page**, and it is linear — no
quadratic behaviour. Extrapolated: 630k pages ≈ 15 min and ≈ 40 GB peak;
1M pages ≈ 25 min and ≈ 60 GB. Memory is the binding constraint, and it is a
property of Hugo holding the page set in memory rather than of this theme.
`HUGO_NUMWORKERMULTIPLIER=1` trades ~30% wall time for a lower peak.

Templates are written so that nothing scans the page set per page:

* **No site-wide `where`.** Every count and listing goes through `GetPage` on a
  known section. A single `where .Site.RegularPages …` is a full scan of the
  corpus; in a partial called from every page it is a scan per page.
* **`len` before `where`/`sort`/`union`.** `len` on a built slice is O(1), the
  filters are not. `pager.html`, `tree.html` and `_default/list.html` all check
  the size first and bail out above 400 children — which is what stops a term
  section from ever being enumerated.
* **`partialCached` for the asset pipeline**, so the CSS concat and the two
  `js.Build` calls resolve once rather than once per page.
* **Branches, not `default`.** Go templates evaluate every argument, so
  `.Description | default (.Summary | …)` extracts a summary even when the
  description exists. `head.html` branches instead.
* **`[services.rss] limit = 20`.** Otherwise each ontology section's `index.xml`
  serialises every page in that section into one file.
* **`disableKinds = ["taxonomy", "term"]`.** The generated pages carry tags like
  `Adult` and `Nervous_system`, so `/tags/adult/` would paginate into thousands
  of files nobody browses. Enabling taxonomies costs ~16% more wall time at 40k
  pages and the penalty grows with the corpus. Comment the line out to restore
  Docsy's behaviour — `_default/taxonomy.html` and `_default/term.html` are
  shipped and paginated, so it is safe either way.

## Layout map

| Content | Template | Result |
|---|---|---|
| `content/en/_index.html` | `layouts/index.html` | Hero + the page's own blocks, then a documentation map and hosted-services grid derived from the content tree |
| `docs/`, `about/`, `hosted/` | `_default/single.html`, `_default/list.html` | Three-column docs shell: sidebar tree, article, on-this-page |
| `blog/news`, `blog/releases` | `_default/list.html` | Dated post list |
| `content: [term]` front matter | `_default/single.html` (term branch) | Compact page; no sibling nav, no pager, no TOC |
| any | `_default/index.json` | ⌘K search index, built by walking the authored sections only |

## Shortcodes

Docsy's `blocks/cover`, `blocks/lead`, `blocks/section`, `blocks/feature` and
`blocks/link-down` are reimplemented with the same parameters, plus the repo's
own `button` and `email`. Two constraints drove how they are written:

1. They are called with the `{{%…%}}` form, so Hugo hands their output back to
   Goldmark. Goldmark ends an HTML block at the first blank line and does not
   process markdown inside one — so the emitted markup contains no blank lines
   and renders its own inner markdown with `markdownify`.
2. `blocks/feature` cards are `<div>`, never `<a>`. The inner markdown routinely
   contains links, and an anchor inside an anchor makes the parser close the
   outer one, splitting the card. The whole card is made clickable with a
   stretched pseudo-element on the title link instead.

## Generated term pages

`vfbterms.py` emits Bootstrap 4/5 utility classes (`card`, `row`, `col-md-*`,
`badge`, `btn`, `img-fluid`, `text-muted`). This theme ships no Bootstrap, so
`assets/css/compat.css` re-implements exactly the classes the generator uses,
scoped to `.prose`. **`vfbterms.py` needs no change.**

## The ontology OLS widget

The 22 ontology index pages carry an inline
`$("#result").load("https://www.ebi.ac.uk/ols/ontologies/<id> #ontology_info_box")`.
Docsy loaded jQuery site-wide; this theme does not, so `partials/script-shim.html`
provides the small slice of the jQuery surface those pages touch — emitted only
where front matter has `ontology:`.

The call itself has been dead for some time irrespective of theme:
`/ols/*` 301s to `/ols4/*`, OLS4 is client-rendered and has no
`#ontology_info_box`, and EBI sends no `Access-Control-Allow-Origin`, so the
request is blocked cross-origin first. The shim declines cross-origin fetches
and leaves `#result` empty, which the CSS hides. Deleting those five lines from
each `content/en/blog/ontologies/<id>/_index.md` would let the shim go too — a
content change, so it is not on this branch.

## Interaction

* `⌘K` / `Ctrl-K` / `/` — command palette over `/index.json`
* Scroll-spy on the on-this-page rail, reading-progress bar
* Copy buttons on code blocks
* Canvas hero: a procedural *Drosophila* CNS point cloud (optic lobes, central
  brain, SEZ, ventral nerve cord) with signal pulses along the graph. Seeded
  PRNG, so the layout is identical on every load. `prefers-reduced-motion`
  draws one static frame.

## Licence

MIT, matching the repo. Fonts: Inter, Space Grotesk, JetBrains Mono (SIL OFL).
Icons: Font Awesome 6 Free (CC BY 4.0 icons, SIL OFL fonts, MIT code).
