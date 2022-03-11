---
title: "Fix for problems with current Safari release"
linkTitle: "Safari Issue Fix"
weight: 100
description: >-
     Virtual Fly Brain 3D browser won't load on Safari Version 15.3 (17612.4.9.1.8) with expreimental feature enabled. Please follow these instructions to disable until Apple fix the issue.
---

We are aware that VFB's secure websocket connection is failing to connect on the latest version of Safari on MacOS meaning that no data can be pulled from our servers.

The issue is down to an 'expreimental feature' (NSURLSession WebSocket) being set to ON by default which seams to break most sites using secure websockets. 

To turn reolve this issue turn this off:


## In Safari on the desktop:

     Under 'Develop' expand 'Experimental Features' untick 'NSURLSession WebSocket'
     
     
If you don’t see the Develop menu in the menu bar, choose Safari > Preferences, click Advanced, then select “Show Develop menu in menu bar”.



## On IOS devices:

     Open the Settings app

     Scroll down and tap on “Safari”
     
     Scroll down to the bottom and tap on “Advanced”
     
     Tap on “Experimental Features” at the bottom
     
     Scroll down until you see “NSURLSession WebSocket"
     
     Disable “NSURLSession WebSocket”


