---
title: "Try the new V3 interface and tell us what you think"
linkTitle: "V3 interface preview"
date: 2026-11-28
image: https://www.virtualflybrain.org/images/v3-preview/v3-default-view.jpg
description: >
    A preview of the next Virtual Fly Brain interface is ready to test. Open it with one link, switch between the old and new layouts from the View menu, and send us your feedback from the Help menu.
---

A preview of the next Virtual Fly Brain (VFB) interface, V3, is now on the live site. We would like you to try it on your own work and tell us what helps and what gets in the way.

**[Open VFB in the V3 view](https://v3.virtualflybrain.org/org.geppetto.frontend/geppetto?view=v3)**

Nothing changes unless you choose it. VFB still opens in the layout you know, now called *V2 default*. The link above opens the same site, with the same data, in the new layout.

## What is different in V3

![The V3 default view: the Neuroglass viewer with tabs for the 3D Viewer and Slice Viewer, Term Info on the right and Layers below](/images/v3-preview/v3-default-view.jpg)

*The V3 default view, with four optic lobe neurons loaded.*

The V3 view puts the Neuroglass viewer first. It shows the template and your loaded neurons as slices in three planes next to a 3D view, in one window, with each loaded item as its own layer. The 3D Viewer and Slice Viewer are tabs behind it, Term Info stays on the right and the Layers list sits underneath.

![The V2 default view: Slice Viewer and 3D Viewer on the left, Template ROI Browser and Layers in the middle, Term Info on the right](/images/v3-preview/v2-default-view.jpg)

*The same neurons in the V2 default view.*

## The View menu

![The View menu, listing V2 default, V3 default, Term Info only, Viewers, Circuit, Save current as My view, and Always start in this view](/images/v3-preview/view-menu.jpg)

The new **View** menu in the top bar switches between layouts at any time:

- **V2 default**: the original three-column layout.
- **V3 default**: the new layout with the Neuroglass viewer.
- **Term Info only**, **Viewers** and **Circuit**: layouts for reading about a term, for looking at images, and for the Circuit Browser.
- **Save current as My view**: keeps your own arrangement of windows, in this browser, and adds it to the menu.
- **Always start in this view**: makes the current view the one VFB opens in. You can go back with *Start in the V2 default view again*.

A view only rearranges the windows. It never changes what you have loaded. Windows a view leaves out are parked in the bar at the bottom of the page, one click away.

You can also put a view in a link. Add `&view=v3` to any VFB address to open it in the V3 view, or `&view=v2` for the original layout.

## Tell us what you think

![The Help menu, with Report an issue near the bottom](/images/v3-preview/help-report-an-issue.jpg)

Choose **Help > Report an issue** from the top bar. The window that opens gives you two ways to reach us: email [support@virtualflybrain.org](mailto:support@virtualflybrain.org), or raise an issue on [GitHub](https://github.com/VirtualFlyBrain/VFB2/issues) with the *Create GitHub Issue* button.

![The Report an issue window, with the email address, the Create GitHub Issue button, and the page address and system details](/images/v3-preview/report-an-issue-dialog.jpg)

The window lists the page address and your browser details. Please include them, so we can see exactly what you were looking at. Questions and requests are as welcome as bug reports. We would most like to hear:

- what you were trying to do, and whether the V3 view made it easier or harder;
- anything you could do in the V2 view that you could not find in V3;
- anything that was slow, broken or confusing.

## Also in this release

The [Circuit Browser](https://www.virtualflybrain.org/docs/website-features/circuitbrowser/) now finds paths between neuron types as well as individual neurons, shows which connectome each result comes from, and draws each path in its own lane.
