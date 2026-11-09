---
title: PeerClick integration with AppsFlyer
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
  created_at: '2024-01-07T08:27:18Z'
  edited_at: '2024-12-23T14:57:46Z'
  id: 21479841979793
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/21479841979793-PeerClick-integration-with-AppsFlyer
---
> **At a glance:** Ad networks that use PeerClick can benefit from the AppsFlyer Probabilistic modeling solution to receive attribution data about installs and in-app events.

## Starting the integration

To start the integration you must send AppsFlyer both the attribution link and the postback for reporting purposes.

Below you can find the base attribution link with a detailed explanation per each parameter:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer End-Point |
| app\_id | Application Unique ID - Dynamic value changed per app promoted |
| pid= | Media source name include **\_int** to identify<br />**integrated** network at AppsFlyer servers |
| c= | Campaign name |

**Recommended Attribution Link Parameters:**

| AppsFlyer Parameter | Voluum Macros | Description |
| --- | --- | --- |
| &clickid= | `{clickid}` | Unique transaction ID of the user session - **Required** |
| &af\_siteid= | `{trafficsource.id}` | ID of the traffic source - **Optional** |

> 📘 **Note**
>
> * For the complete AppsFlyer parameter list, <Anchor target="_blank" href="/marketers/id/docs/about-link-structure-and-parameters">click here</Anchor>
> * For the complete PeerClick list, <Anchor target="_blank" href="https://help-center.peerclick.com/en/">click here</Anchor>

### Complete attribution link template

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

### Install and in-app event postbacks

**Global Install Postback:**

```http
https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}
```

**Global In-App Event Postback:**

`https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}&payout={monetary}&txid={event-name}`

* **userid:** The user ID provided by PeerClick
* **txid:** The actual in-app event name from the application, set as **Event Tag** in the AppsFlyer dashboard for each App by the advertiser

### AppsFlyer's in-app event dashboard

<Image align="center" alt="Voluum_msc_new_1.png" src="https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png" />
Additional attribution information can be added to the postback by request such as Country Code, Advertising ID, IDFA, etc.

<div data-zendesk-anchors="h_01HKHFT3RFWF5H349GP7MHDAYX=starting-the-integration h_01HM8M27S5WFJVKBG0JAFW548H=note h_01HKHFT3RFDW6GZM3E72SYPJSD=complete-attribution-link-template install-and-inapp-event-postbacks=install-and-in-app-event-postbacks h_01HKHFT3RF1PTSJ4SF9RTQ93N8=install-and-in-app-event-postbacks appsflyers-inapp-event-dashboard=appsflyers-in-app-event-dashboard h_01HKHFT3RFDVPCSKJGZPRFB55V=appsflyers-in-app-event-dashboard" />
