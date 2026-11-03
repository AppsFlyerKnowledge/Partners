---
title: Fuseclick integration with AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-01-11T14:46:45Z'
  edited_at: '2026-10-13T01:53:00Z'
  id: 207583573
  locale: zh-cn
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/zh-cn/articles/207583573
---
> **At a glance:** Ad networks that use FuseClick can utilize the AppsFlyer Probabilistic modeling solution to receive attribution data about installs and in-app events.

## Basic attribution link

Below you can find the base attribution link with a detailed explanation per each parameter:

```http
https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}
```

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer endpoint |
| app\_id | Application unique ID - Dynamic value changed per-app promoted |
| pid | Media source name include **\_int** to identify<br />**integrated** network at AppsFlyer servers |
| c | Campaign name |

**Recommended Attribution Link Parameters:**

| AppsFlyer Parameter | FuseClick Macros | Description |
| --- | --- | --- |
| clickid | `{TID}` | Request ID of each user session - **Required** |
| af\_siteid | `{SC}` | ID of the affiliate promoting the offer - **Optional** |

For the complete AppsFlyer parameter list <Anchor target="_blank" href="/partners/zh/docs/postback-macros-for-ad-networks">click here</Anchor>

For complete FuseClick macro list <Anchor target="_blank" href="https://support.fuseclick.com/documentation/open/iwf/2016/0805/199.html">click here</Anchor>

Complete Attribution Link Template:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={TID}&af_siteid={ADV_SID}
```

### Install and in-app event postbacks

Global Install Postback:

```
https://tracking.zadsmobile.com/pb?tid={TID}
```

Additional attribution information can be added to the postback by request such as: Country Code, Advertising ID, IDFA, and more.

## Finalizing your registration

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div data-zendesk-anchors="01JFT0DX287AWQND2BYFSV50HW=basic-attribution-link install-and-inapp-event-postbacks=install-and-in-app-event-postbacks 01JFT0DX2B6FFE3K7VTXG1YVJ1=install-and-in-app-event-postbacks 01JFT0DX2BD8A19BY9197X11QW=finalizing-your-registration" />
