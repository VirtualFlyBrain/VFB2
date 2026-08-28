---
title: "Safari failing to load VFB data? Check iCloud Private Relay"
linkTitle: "Safari / Private Relay Issue"
date: 2026-08-28
description: >
    Recent Safari releases (macOS 26 / iOS 26) can fail to establish the secure WebSocket connection VFB uses to load data, particularly when iCloud Private Relay is enabled. Here is how to work around it.
---

We are aware that on some recent Safari releases (Safari 26 on macOS 26 and iOS 26) Virtual Fly Brain can fail to load, sitting on the splash/help screen with empty viewer panels. This happens when the browser cannot establish the secure WebSocket connection VFB uses to pull data from our servers.

Our servers are working normally: the same connection succeeds from Chrome, Firefox and Edge, and from earlier Safari releases. The failures match WebSocket regressions in Safari 26 that Apple has been fixing progressively (see WebKit bugs [298616](https://bugs.webkit.org/show_bug.cgi?id=298616) and [302561](https://bugs.webkit.org/show_bug.cgi?id=302561)), and they occur mainly when **iCloud Private Relay** is enabled — an iCloud+ feature that routes Safari traffic through Apple relay servers.

If VFB fails to load in Safari, try the steps below.

## First, the quick checks

* Update to the latest version of macOS/iOS and Safari — Apple has fixed several of these WebSocket problems in point releases.
* Close any other VFB tabs and reload: one known Private Relay bug allows only a single WebSocket connection per site, so a second VFB tab can hang indefinitely.
* If you are not an iCloud+ subscriber, Private Relay is not the cause — please try another browser (Chrome, Firefox or Edge) and [let us know](https://github.com/VirtualFlyBrain/VFB2/issues/new) so we can investigate.

## Turn off iCloud Private Relay on a Mac

1. Open **System Settings** from the Apple menu.
2. Click your name (Apple Account) at the top of the sidebar, then click **iCloud**.
3. Click **Private Relay**.
4. Turn Private Relay off. You can choose **Turn Off Until Tomorrow** (it re-enables automatically after 24 hours) or **Turn Off Private Relay** to disable it until you switch it back on.
5. Reload [VFB](https://v2.virtualflybrain.org).

Apple's own instructions are here: [Use iCloud Private Relay on Mac](https://support.apple.com/en-gb/guide/mac-help/mchlecadabe0/mac).

## Turn off iCloud Private Relay on iPhone or iPad

1. Open the **Settings** app.
2. Tap your name at the top, then tap **iCloud**.
3. Tap **Private Relay**.
4. Turn Private Relay off, choosing **Turn Off Until Tomorrow** or **Turn Off Private Relay** when prompted.
5. Reload [VFB](https://v2.virtualflybrain.org).

Apple's own instructions are here: [Protect your web browsing with iCloud Private Relay on iPhone](https://support.apple.com/en-sg/guide/iphone/iph499d287c2/ios).

## Alternative: disable it for your current network only

If you would rather keep Private Relay on for general browsing, you can exclude just the network you are on:

* **Mac:** **System Settings → Network → Wi-Fi** (or Ethernet), click **Details…** next to your network, then turn off **Limit IP address tracking**.
* **iPhone/iPad:** **Settings → Wi-Fi**, tap the ⓘ next to your network, then turn off **Limit IP Address Tracking**.

This disables Private Relay on that network only, on that device only.

## Still stuck?

If VFB still fails to load after these steps, please use another browser for now and [report the problem](https://github.com/VirtualFlyBrain/VFB2/issues/new) telling us your Safari and macOS/iOS versions — failed connections are also reported to us automatically, which helps us track how widespread the issue is.
