---
title: Appnexus integration with AppsFlyer
metadata:
  keywords:
    - Integration
    - AppNexus
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
  created_at: '2016-01-11T14:45:34Z'
  edited_at: '2026-10-01T00:41:09Z'
  id: 207583523
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/207583523
---
> **At a glance:** Ad networks that use Affise can utilize the AppsFlyer Probabilistic modeling solution to receive attribution data about installs and in-app events.

## Starting the integration

To start the integration you must send AppsFlyer both the attribution link and the postback for reporting purposes.

Below you can find the base attribution link with a detailed explanation per each parameter:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer end-Point |
| app\_id | Application Unique ID - Dynamic value changed per app promoted |
| pid | Media source name include **\_int** to identify **integrated** network at AppsFlyer servers |
| c | Campaign name |

**AppNexus Advertising ID Macros**

| Operating System | Macro |
| --- | --- |
| Android | &advertising\_id=$`{DEVICE_AAID}` |
| iOS | idfa=$`{DEVICE_APPLE_IDA}` |

**Recommended Attribution Link Parameters**

| AppsFlyer Parameter | AppNexus Macros | Description |
| --- | --- | --- |
| clickid | $`{SSP_DATA}` | Request ID of each user session - **Required** |
| af\_siteid | $`{PUBLISHER_ID}` | ID of the affiliate promoting the offer - **Optional** |

For the complete AppsFlyer parameter list <Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">click here</Anchor>.

For the complete AppNexus macro list <Anchor target="_blank" href="https://wiki.appnexus.com/display/sdk/Welcome">click here</Anchor>.

### Complete attribution link template:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=${SSP_DATA}&af_siteid=${PUBLISHER_ID}
```

### Install and in-app event postbacks

Global Install Postback:

```http
https://sspx-router.adnxs.net/sspx?id={ID}&sspdata={clickid}
```

`{ID}` the Network ID provided by AppNexus, inserted in AppsFlyer dashboard per app.

### AppsFlyer install dashboard

[<Image align="center" alt="appnexus-pixelid.png" src="https://files.readme.io/0f14632fc7421fbbb26f90c13cc37afad58e4e217f4bcebd931cddb7576c5113-360018728918.png" />](https://support.appsflyer.com/hc/article_attachments/51444722110225)

Additional attribution information can be added to the postback by request such as Country Code, Advertising ID, IDFA, and so on.

## Finalizing your registration

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div data-zendesk-anchors="01JFT0Z4H4N0SFK6CAKQGW41Q4=starting-the-integration 01JFT0Z4H7MA1B9FMNWKESF170=complete-attribution-link-template install-and-inapp-event-postbacks=install-and-in-app-event-postbacks 01JFT0Z4H7TZPQCFGZCASNWHD7=install-and-in-app-event-postbacks 01JFT0Z4H89BP3YWFRSJ69RK6D=appsflyer-install-dashboard 01JFT0Z4H9TF582WHB69MT9VP2=finalizing-your-registration" />
