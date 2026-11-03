---
title: About probabilistic modeling
metadata:
  keywords:
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2025-10-21T14:32:11Z'
  edited_at: '2026-04-19T13:00:27Z'
  id: 40188089592209
  locale: en-us
  section: Provide data
  section_id: 6551209900817
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/40188089592209-About-probabilistic-modeling
---
> **At a glance:** Learn how to set up your ad engagement data so AppsFlyer can apply probabilistic modelling when deterministic signals aren’t available.

## About probabilistic modeling

AppsFlyer uses probabilistic modeling as a privacy-preserving statistical method to report on how app developers’ marketing campaigns are performing. It produces aggregate campaign-level performance reports for app developers.

**Implementation characteristics**

* Uses statistics and is not based on unique IDs.
* It is a fallback method used when a referer or advertising IDs are unavailable. Deterministic attribution methods, i.e., clicks with referrer or ID matching, are given priority if they occur within the lookback window.

### When is probabilistic modeling used?

Except where otherwise configured by the customer, probabilistic modeling will apply in cases where deterministic data is unavailable, including:

* Web-to-app conversions
* Cross-device experiences (for example, a desktop ad followed by a mobile install)
* CTV, PC, or console environments where deterministic attribution isn’t possible

<div data-zendesk-anchors="about-probabilistic-modeling-attribution=about-probabilistic-modeling h_01K83JWQ84H0P1WABG939X55KD=about-probabilistic-modeling h_01K83JWQ8412VK2ZN39CQ5TJEZ=when-is-probabilistic-modeling-used" />
