---
title: "Image Sample"
date: 2024-01-30T21:38:44+01:00
authors: ["Lukas Rist"]
tags: []
draft: true
---

Get a logo.png and convert it to webp: `cwebp logo.png -o logo.webp`

In order to embed the image in the post, the image has to be either in the folder of the post, a subfolder or the `static` folder.

Embed the image like this:
`![alt text](logo.webp "hover text")`

Technically we are not creating an image but embedding an arbitrary file. The `!` distinguishes between a link and an embedded file.

![alt text](logo.webp "hover text")
