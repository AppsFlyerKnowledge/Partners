---
title: Preload attribution for partners
metadata:
  keywords:
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-alina-koifman
    - Marketers
    - Mobile Attribution
  created_at: '2023-05-15T09:45:55Z'
  edited_at: '2026-10-13T01:50:11Z'
  id: 15321350340241
  locale: ko
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ko/articles/15321350340241
---
> **At a glance:** Attribute mobile app installs to campaigns that preload the app at the Original Equipment Manufacturer (OEM) or when the device is first turned on by the user.

## Overview

By supporting AppsFlyer preload attribution solutions, preload partners can have app installs attributed to preload campaigns. Preload campaigns are for when an app is installed on a device by a preload partner either at the factory or upon device activation (when the device is first turned on).

Preload partners are:

* Original Equipment Manufacturers (OEMs)
* App discovery platforms
* Mobile carriers

There are 3 ways to attribute preload campaigns:

* [Recommended] AppsFlyer referrer
* Google Play auto-install (PAI)
* [Legacy] Preload in factory via System Property

Postbacks are sent to you after each conversion.

<Anchor target="_blank" href="/marketers/ko/docs/appsflyer-attribution-model#preload-campaigns">Learn more about the preload campaign attribution methods</Anchor>

## Set up preload attribution

To set up preload attribution:

1. Make sure you're an <Anchor target="_blank" href="/partners/ko/docs/getting-started-onboarding-guide-for-ad-networks">AppsFlyer integrated partner</Anchor>.
2. Choose the preload attribution solutions to integrate (based on advertiser needs). **Note**: Each integration needs an independent PID with an AppsFlyer Partner Account. Reach out to your partner solutions team via the support widget.
   * [Recommended] <Anchor target="_blank" href="/marketers/ko/docs/set-up-appsflyer-preload-referrer-attribution">AppsFlyer referrer</Anchor>: Contact your PDM for integration instructions.
   * <Anchor target="_blank" href="/marketers/ko/docs/measure-preload-campaigns-with-google-play-install">Google Play auto-install (PAI)</Anchor>: Configure the media source information in the Google Play Referrer API for PAI campaigns using the following UTM parameters: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=brandnamepai_int`. For example: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=xiaomipai_int`.
3. Contact the AppsFlyer partner solutions team via the support widget to complete the integration and optionally set up postbacks.  
   **Note**: See which postback macros are supported for the preload method of <Anchor target="_blank" href="/marketers/ko/docs/measure-preload-campaigns-with-google-play-install#프리로드-파트너를-위한-포스트백">Google PAI</Anchor> and <Anchor target="_blank" href="/partners/ko/docs/postback-macros-for-ad-networks">AppsFlyer referrer/Android manifest file</Anchor>.

<div data-zendesk-anchors="organic-search-attribution=overview h_01HQFFB20SKDVW1X3ECMZCZQW0=overview h_01HQFFB20S6KJH3PBF5N2190TJ=set-up-preload-attribution" />
