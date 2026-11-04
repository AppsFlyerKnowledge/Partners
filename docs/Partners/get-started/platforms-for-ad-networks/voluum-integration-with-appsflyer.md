---
title: Voluum integration with AppsFlyer
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
  created_at: '2016-01-11T14:46:09Z'
  edited_at: '2026-05-04T09:31:48Z'
  id: 207274016
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/207274016-Voluum-integration-with-AppsFlyer
---
> **At a glance:** Ad networks that use Voluum can utilize the AppsFlyer Probabilistic modeling solution to receive attribution data about installs and in-app events.

<div id="starting-the-integration" />

## Starting the integration

To start the integration you must send AppsFlyer both the attribution link and the postback for reporting purposes.

Below you can find the base attribution link with a detailed explanation per each parameter:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer End-Point |
| app\_id | Application Unique ID - Dynamic value changed per app promoted |
| pid= | Media source name include **\_int** to identify **integrated** network at AppsFlyer servers |
| c= | Campaign name |

**Recommended Attribution Link Parameters:**

| AppsFlyer Parameter | Voluum Macros | Description |
| --- | --- | --- |
| &clickid= | `{clickid}` | Unique transaction ID of the user session - **Required** |
| &af\_siteid= | `{trafficsource.id}` | ID of the traffic source - **Optional** |

** For complete AppsFlyer parameter list, <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">click here</Anchor>

** For complete Voluum macro list, <Anchor target="_blank" href="http://feedback.voluum.com/knowledgebase/articles/318681-click-urls">click here</Anchor>

<div id="complete-attribution-link-template" />

### Complete attribution link template

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### Install and in-app event postbacks

Global Install Postback:

```http
https://{Company-Domain}.voluumtrk.com/postback?cid={clickid}
```

Global In-App Event Postback:

```http
https://{Company-Domain}.trackvoluum.com/postback?cid={clickid}&payout={monetary}&txid={event-name}
```

** `{Company-Domain}` the network ID (domain) name provided by Volumm.  
** txid= Set as **Event Tag** in the AppsFlyer dashboard for each App by the advertiser. This is the actual in-app event name from the application.

<div id="appsflyers-in-app-event-dashboard" />

### AppsFlyer's in-app event dashboard

![Voluum_msc_new_1.png](https://files.readme.io/bb58ccaabf1eb8d615288d259102b3dc7883c5c79448131c67374ad8fbdaf6c0-360002325069.png)  
** Additional attribution information can be added to the postback by request such as Country Code, Advertising ID, IDFA, etc.

<div id="finalizing-your-registration" />

## Finalizing your registration

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div data-zendesk-anchors="01JFT0VZZ5KVMKYRD222JT55NH=starting-the-integration 01JFT0VZZ7B1RRY82B65GWF4P7=complete-attribution-link-template install-and-inapp-event-postbacks=install-and-in-app-event-postbacks 01JFT0VZZ86KYXSVE1QBD2V0HF=install-and-in-app-event-postbacks appsflyers-inapp-event-dashboard=appsflyers-in-app-event-dashboard 01JFT0VZZ9A4JWG38KPH0CNQ72=appsflyers-in-app-event-dashboard 01JFT0VZZATFYY75QPCPKZF3S6=finalizing-your-registration" />
