---
title: "GreedyBear: Modularizing the Dashboard"
authors: ["Rachit Pandey"]
date: "2026-08-14T17:00:00+05:30"
tags: ["GSoC", "GreedyBear", "React"]
---

I spent this summer as a [GSoC](https://summerofcode.withgoogle.com/) contributor on **[GreedyBear](https://github.com/GreedyBear-Project/GreedyBear)** under the mentorship of **[Tim Leonhard](https://github.com/regulartim)**, refactoring its hardcoded dashboard into a configuration-driven widget system with a drag-and-drop admin editor and backend persistence.

**Mentor:** Tim Leonhard  
**Organization:** The Honeynet Project  
**Project:** [GreedyBear: Dashboard Modularization](https://summerofcode.withgoogle.com/)

## GSoC Proposal

The goal of my project was to modularize the GreedyBear dashboard.

Before this project, every widget - its type, data source, position, and column span was hardcoded directly in `Dashboard.jsx`. Adding a new chart meant editing the layout file by hand, and there was no way for an admin to customize the dashboard without touching source code and redeploying.

My proposal was to replace this with three layers: a **widget registry** as a central catalog, a **renderer** that reads a configuration array rather than hardcoded lists, and an **admin UI** backed by a Django REST endpoint so a superuser can rearrange the dashboard entirely through the browser.

## GSoC Tasks and Deliverables

### 1. Widget Registry and Renderer

The foundation of the whole system is `widgetRegistry.js`, a `Map<string, WidgetDefinition>` that is the single source of truth for every widget the dashboard knows about. Each entry stores the React component, display name, default height, API endpoints, and default props.

`DashboardRenderer.jsx` reads a `widgetConfigs` array and renders the dashboard entirely from it, with no hardcoded widget references. Adding a new widget is one entry in the registry and one entry in the config and the renderer, dashboard, and editor all pick it up automatically.


### 2. Refactoring Existing Widgets

With the registry in place, I refactored all eight widgets.`defaultDashboardConfig.js` reproduces the original layout exactly, with zero visual regression.

[PR #1381](https://github.com/GreedyBear-Project/GreedyBear/pull/1381)

### 3. Shared Data-Fetching Hook

The `AttackOriginMap` and `AttackOriginCountriesChart` widgets both called the same API endpoint on mount which meant two identical concurrent GETs every page load. The data-fetching pattern was also copy-pasted across every chart component.

I extracted a `useWidgetData(url, params)` hook backed by a module-level cache (5-minute TTL) and an in-flight deduplication Map. When two components request the same URL simultaneously, only one network request fires and the second subscribes to the existing Promise.

This also let me delete `useAttackerCountriesStore.jsx`, 97 lines of redundant Zustand state that existed solely to share data between the two map widgets.

[PR #1410](https://github.com/GreedyBear-Project/GreedyBear/pull/1410)

### 4. Admin Configuration UI

Before starting work on the project, I had evaluated `@dnd-kit/core` and `react-grid-layout`.
I chose `react-grid-layout` because it can do a grid system with built-in drag-and-drop and resize without much extra code which was perfect to maintain and use.

[PR #1444](https://github.com/GreedyBear-Project/GreedyBear/pull/1444)

### 5. Backend Persistence

I've only little experience with Python and Django, so I struggled slightly with this one.

`DashboardConfig` is a singleton model with a `JSONField` storing the full layout. A DRF endpoint at `/api/dashboard-config/` serves GET (any authenticated user) and PUT (superusers only). When no record exists, GET falls back to the hardcoded defaults.

[PR #1491](https://github.com/GreedyBear-Project/GreedyBear/pull/1491)



## Final Thoughts

GSoC 2026 was a fantastic experience. I learned a lot about React, Django, but most importantly how beautiful open-source collaboration can be.

I am especially grateful to **Tim Leonhard**, who was always available and actually reviewed each line of code :)

I'd love to continue contributing to GreedyBear.