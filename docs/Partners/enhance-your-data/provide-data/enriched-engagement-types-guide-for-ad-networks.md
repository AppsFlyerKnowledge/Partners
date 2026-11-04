---
title: Enriched Engagement Types guide for ad networks
metadata:
  keywords:
    - Advertisers
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2024-10-15T10:54:29Z'
  edited_at: '2026-06-03T08:39:59Z'
  id: 29221265052433
  locale: en-us
  section: Provide data
  section_id: 6551209900817
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/29221265052433-Enriched-Engagement-Types-guide-for-ad-networks
---
> **At a glance:** Learn how to create Enriched Engagement Types (EET) attribution links to reflect users’ full spectrum of engagement and achieve accurate and effective campaign optimization.

Enriched Engagement Types (EET) reflect users' full spectrum of engagement and intentionality when viewing or interacting with an ad, from momentary exposure to direct response. This article details how partners should report engagement types in AppsFlyer attribution links based on how users interact with their ads.

<div id="disclaimer" />

> ❗️ **Disclaimer**
>
> This article focuses on the aspects of EET relevant to partners. To learn what EET is and to get comprehensive information on it, see the <Anchor target="_blank" href="/marketers/docs/about-enriched-engagement-types#which-ad-networks-report-enriched-engagement-types">Enriched Engagement Types</Anchor> article.

<div id="which-networks-can-report-eet-to-appsflyer" />

## Which networks can report EET to AppsFlyer?

Enriched Engagement support will be available for networks that meet the Premier, Advance, or Engage criteria of AppsFlyer’s Partner Program. These levels refer to networks that have a significant track record of delivering consistently high-quality traffic at scale to our mutual customers, send engagement data in a transparent and trusted manner, and are integrated with a comprehensive range of AppsFlyer services.

<div id="note" />

> 📘 **Note**
>
> To begin reporting engaged views and clicks, ad networks should contact AppsFlyer support.

See [the list of networks eligible to report EET](#01JCAT81K2EJNH91YS6NJGMXMB-data-title)

<div id="warning" />

> ❗️ **Warning**
>
> Clicks and impressions from non-allowed networks that include the `af_engagement_type` parameter will be rejected and won’t be used for attribution.

<div id="engaged-click-or-engaged-view-attribution-flow" />

<Accordion title="Engaged click or engaged view attribution flow">

The following steps outline the flow from the initial ad display to the final attribution of an install event, through either an engaged click or an engaged view:

1. The ad network displays an ad.
2. The ad network sends an impression to AppsFlyer with a specified `af_ad_tran_id`
3. The user is engaging with the ad.
4. The ad network sends a click or impression with the `af_engagement_type`, `af_ad_tran_id`, `af_ad_format`, `af_ad_type`, and optionally with the `viewability` parameters.
5. AppsFlyer matches an install event with the engaged click or the engaged view.
6. AppsFlyer attributes the install event to the ad network.

</Accordion>

<div id="parameters-for-reporting-engagement-types-in-attribution-links" />

<Accordion title="Parameters for reporting engagement types in attribution links">

Networks can report engagement types by including the following parameters in the attribution links

* `af_engagement_type`: The type of engagement for example, `engaged_click`, `click_to_app` or `engaged_view`. See a <Anchor target="_blank" href="/marketers/docs/about-enriched-engagement-types#what-are-enriched-engagement-types">comprehensive list of the different engagement types and their descriptions</Anchor>.
* `af_ad_type`: The ad type. For example, `rewarded_video`, `interstitial` or `banner`. See <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#af_ad_type">a comprehensive list of the different ad types and their descriptions</Anchor>.
* `af_ad_format`: The ad format, for example, `text`, `image`, `video`, `playable`. See <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#af_ad_format">a comprehensive list of the different ad formats and their descriptions.</Anchor>
* `viewability`: (optional) Additional info about the engagement, for example, `af_video_total_length`, `af_ad_time_viewed`, `af_audio_played_length`. See <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#viewability-parameters">a comprehensive list of the different viewability options and their descriptions.</Anchor>
* `af_ad_tran_id`: A transaction ID allowing AppsFlyer to verify an engaged click or engaged view by matching it to a preceding impression.
* `is_skoverlay=true` or `is_autostore=true` : Identify engaged views triggered by [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) or Android Auto Inline Installs

**An Example for an engaged click**

```http HTTPS
https://app.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_click&af_ad_type=interstitial&af_ad_format=playable&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0
```

**An Example for an engaged view**

```http
https://impression.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_view&af_ad_type=interstitial&af_ad_format=video&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0&af_video_total_length=20&af_video_played_length=15
```

</Accordion>

<div id="user-engagements-to-report-as-engaged-clicks" />

<Accordion title="User engagements to report as engaged clicks">

An *engaged click* is a click that keeps the user in the same context, interacting with the ad, without redirecting them to the app store or launching the app.

Below are examples of user engagements that ad networks should report with the `af_engagement_type=engaged_click` parameter value:

* **Playable Ad:** Clicking to engage with a playable ad, such as tapping to play a mini-game or interactive content within the ad.
* **Social Engagement:** Clicking to like, comment on, or share the ad on social media platforms, thereby promoting further interaction and potential virility.
* **Redirection:** Clicking to visit a landing page or other external content site/page.
* **Dynamic product ad/catalog or carousel:** Clicking to swipe between products.
* **Add to Wishlist:** Clicking to add the promoted product to a wishlist or favorites list within the app or an external website.
* **Save for Later:** Clicking to save the ad and its contents for future reference, thereby indicating an interest in revisiting the ad or exploring it further.
* **Bookmark or Add to Collections:** Clicking to bookmark the ad or add it to curated collections within the app, thereby indicating an intention to revisit or categorize the ad.
* **Unmute Ad:** Clicking to enable audio.

**When not to report engaged clicks to AppsFlyer?**

Below are examples of user engagements that ad networks should **not** report with the `engaged_click` parameter value.

* **Ad Dismissal:** Clicking the "x" button or a similar indicator to close or dismiss the ad, thereby showing disinterest in further engagement.
* **Skip Ad**: Clicking a designated button to skip an ad and proceed directly to the intended content, thereby indicating that the ad was not engaging or relevant to the user.
* **Report Ad**: Clicking to report the ad for reasons like being offensive, misleading, or inappropriate, thereby expressing dissatisfaction with the ad content.
* **Opt-out or Unsubscribe**: Clicking to opt-out or unsubscribe from receiving similar ads in the future, thereby expressing the intention to discontinue engagement with the ad or its category.
* **Exit Ad:** Clicking on a link or button that exits the current ad experience, leading the user outside the advertised context or landing page.
* **Mute Ad:** muting the sound on a video.

</Accordion>

<div id="user-engagements-to-report-as-engaged-views" />

<Accordion title="User engagements to report as engaged views">

Networks should report user engagements with `af_engagement_type=engaged_view` in the following cases:

* **Skippable ad unit:** The users watches at least 5 seconds after the skip option appears on a video ad. If the network cannot measure the number of seconds viewed, then:
  * Send `engaged_view` on 2/4 view (50% viewed pixel) when the video is longer than 20 seconds.
  * Send `engaged_view` on complete (100% video complete) when the video is shorter than 20 seconds
  * The `af_ad_format` parameter value must be `video` or `playable`
* **Rewarded video:** The user watches a rewarded video in its entirety. The `af_ad_type` parameter value must be `rewarded_video`.
* **Auto StoreKit rendered ads:** Clicks on StoreKit-rendered ads ([`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay) or an [`SKStore`](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)) are not recorded by the publishers, but by Apple forSKAdNetwork (SKAN) attribution. The same is true for the Android Auto Inline Installs (autostore).

  Since there is no way for the ad networks to know whether those ads were engaged they report an impression or click whenever the ads appear even if no engagement occurred.

  Networks can report the `click_to_app` engagement type whenever the ad appears but then run the risk of a very high click-through rate. The same is true for Android with the Auto Inline installs.

  To mitigate this risk we recommend to report the `engaged_view` engagement type instead. In this use case, the attribution link must include `is_skoverlay=true` for iOS or `is_autostore=true` for Android.

**When not to report engaged views to AppsFlyer?**

Below is a use case of user engagement that ad networks should **not** report with the `engaged_view` parameter value but rather with the `view` parameter.

* The user watches a non-skippable ad which is not a rewarded video and was not overlaid by an `SKOverlay` or `autostore` ad.

</Accordion>

<div id="01JCAT81K2EJNH91YS6NJGMXMB-data-title" />

<Accordion title="Networks eligible to report EET">

The allowed network list includes partners whose enriched engagement-type events can be processed by AppsFlyer, with the exclusion of engaged clicks and views. Networks from this list that would like AppsFlyer to process their engaged clicks and views should contact AppsFlyer support. To learn which networks already have their engaged clicks and views processed by AppsFlyer, see the <Anchor target="_blank" href="/marketers/docs/about-enriched-engagement-types#which-networks-can-report-engaged-views-and-engaged-clicks">EET advertisers article</Anchor>.

<div id="warning-1" />

> ❗️ **Warning**
>
> Clicks and impressions from non-allowed networks that include the `af_engagement_type` parameter will be rejected and won’t be used for attribution.

| Partner Name |
| --- |
| AdColony |
| Adaction |
| Adaction3 |
| Adikteev |
| adjoe GmbH |
| Amazon |
| Amazon DSP |
| AppLovin |
| Appier |
| Appnext |
| Apple Search Ads |
| Aura from Unity |
| AWIN |
| Bidease |
| ByteDance Ads China |
| Cauly |
| Criteo |
| Digital Turbine |
| Digital Turbine On Device |
| Fluent |
| Glance |
| Google Ads (Adwords) |
| Google Marketing Platform (DV360/CM360) |
| Hotstar |
| Huawei |
| InMobi DSP |
| ironSource |
| Jampp |
| Josh |
| Kakao |
| Kuaishou |
| Liftoff |
| Line |
| Meta ads |
| Mintegral |
| Mistplay |
| Motorola Pre-Install |
| Naver |
| OPPO |
| OPPO Global |
| OPPO Store Traffic(Global) |
| OPPOPAI Pre-Install |
| PayTM |
| Rakuten |
| Reddit |
| Remerge |
| RevX |
| Samsung |
| Smadex |
| Snapchat |
| Stackadapt |
| Tapjoy |
| Tencent AMS |
| TikTok For Business - Advanced SRN |
| TikTok for Business - Legacy |
| The Trade Desk |
| Transsion |
| Treasure Data |
| Truecaller |
| Unity Ads |
| Vivo Preload |
| vivo Global |
| Vungle |
| X Ads (formerly Twitter Ads) |
| Xiaomi Global |
| XiaomiPAI Pre-Install |
| Yahoo Japan |
| Yandex |
| YouAppi |

</Accordion>

<div data-zendesk-anchors="01JA7WZH43ECDKRC0R0J89ED1E=disclaimer h_01JJPVYGWZSFSATZ4TH5VBSVXW=which-networks-can-report-eet-to-appsflyer 01JAN5JRM56C6S6EP27WFJ2Y4W=note h_01J00XFV133YYAB7YPQNXM5R37=warning 01JA7WZH46RJBG996NG9EZV7T9=engaged-click-or-engaged-view-attribution-flow 01JA7WZH4BZVGS9Z1NNHQC72N6=parameters-for-reporting-engagement-types-in-attribution-links 01JA7WZH4JDJFCVT25WJ4GNE20=user-engagements-to-report-as-engaged-clicks 01JA7WZH4Q32TEWM5EKME142R7=user-engagements-to-report-as-engaged-views 01JCAT81K2EJNH91YS6NJGMXMB%20data-title%3D=01JCAT81K2EJNH91YS6NJGMXMB-data-title allowed-network-list=01JCAT81K2EJNH91YS6NJGMXMB-data-title h_01JJPVYGWZ4T6TPFRWTR2AB027=warning-1" />
