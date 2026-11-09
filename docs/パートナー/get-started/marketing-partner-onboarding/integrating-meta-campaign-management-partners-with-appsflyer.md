---
title: Integrating Meta campaign management partners with AppsFlyer
metadata:
  keywords:
    - Callbacks
    - Integration
    - Facebook
    - Partner
    - In-App
    - partner account
    - User Level
    - Data policy
    - FMP
    - Partners
    - Developers
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
  created_at: '2015-03-29T12:38:26Z'
  edited_at: '2026-10-13T01:52:12Z'
  id: 207034146
  locale: ja
  section: Marketing partner onboarding
  section_id: 6551118224657
  url: https://support.appsflyer.com/hc/ja/articles/207034146
---
> **At a glance:** Learn what data types Meta campaign management partners can receive from AppsFlyer.

## Install postbacks

Upon conversion, AppsFlyer can return the following parameters:

| Parameter Name | Parameter Name Convention |
| --- | --- |
| Campaign Name | `{campaign_name}` |
| Campaign ID | `{campaign_id}` |
| Ad Set Name | `{adset_name}` |
| Ad Set ID | `{adset_id}` |
| Ad Group Name | `{adgroup_name}` |
| Ad Group ID | `{adgroup_id}` |
| Event time – Rounded up | `{timestamp}` |
| Unique AppsFlyer User ID | `{sha1-appsflyer-device-id}` |
| Device ID Hashed MD5 | `{md5IDFA\md4GAID}` |
| If the attribution was from a view | `{is-impression}` |
| Channel (Instagram, Meta Audience Network, Facebook, Messenger) | `{af_channel}` |
| Geo | `{user_country}` |

> 📄 **Example**
>
> http://mcmp_postbackURL.........&mcmp_ADset_name =`{adset_name}`

## In-app event postbacks

Upon In-app events, AppsFlyer can return the following parameters (in addition to the above):

| Parameter Name | Parameter Name Convention |
| --- | --- |
| Event Name* | `{event_name}` |
| Event Value | `{event_value}` |

> 📄 **Example**
>
> `http://FMP_postbackURL.........&eventname={event_name}`

* The Meta campaign management partner can choose to receive the in-app event name as the advertiser configured it in AppsFlyer's SDK or to have the advertiser fill in a free text field per event.

## User-level data policy

* AppsFlyer cannot pass IDFA or Android/Advertising ID.

* AppsFlyer passes rounded-up installs/events timestamps to the closest hour.

For example: If an install happened at 4.32 pm and 42 seconds, we can pass 5 pm as the timestamp

* AppsFlyer can use a Random ID of its own creation to attach to events that ID shouldn’t be derived from the IDFA/Android ID and should be unique to Meta ads. The same random ID can be passed downstream for In-app event postbacks.

> 📘 **Note**
>
> Based on Meta terms sending postbacks is available only for companies obtaining the following badges: Ad Technology

> 📄 **Example**
>
> <Image align="center" alt="" src="https://files.readme.io/6832879dafaadb91a795988abdc5e51203c9c1775054e35829cfe60cb2175a66-360001440909.png" />
>
> For the full list of Meta campaign management partners, click <Anchor target="_blank" href="https://www.facebook.com/business/partner-directory/search?programBadges=ADTECH_FB.ADTECH_IG&solution_type=campaign_management">here</Anchor>.

<div data-zendesk-anchors="inapp-event-postbacks=in-app-event-postbacks userlevel-data-policy=user-level-data-policy" />
