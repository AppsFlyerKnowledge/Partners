---
title: Trackier integration with AppsFlyer
metadata:
  keywords:
    - AdNetwork Integration
    - ad networks
    - Advertisers
    - ad network
    - Partners
    - trackier
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
  created_at: '2020-02-24T13:25:45Z'
  edited_at: '2026-10-13T01:53:37Z'
  id: 360006111917
  locale: zh-cn
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/zh-cn/articles/360006111917
---
> **At a glance:** Ad networks that use Trackier can receive attribution data from AppsFlyer about installs and in-app events.

To begin integration, provide AppsFlyer with both the attribution link URL and the postback URL. The URLs are needed for reporting purposes. This article explains how to build these URLs.

## Attribution link URL

This section provides the base attribution link and related parameter descriptions.

### Base attribution link URL

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={click_id}&af_siteid={publishedr_id}
&af_c_id={camp_id}
```

| AppsFlyer base URL | Definition | Description |
| --- | --- | --- |
| https://app.appsflyer.com | Base URL | AppsFlyer endpoint |
| app\_id | Application ID | Dynamic value that differs for each app |
| pid= | Media source name | **\_int** identifies an **integrated** network |
| c= | Campaign name | Name given by the advertiser |

### Attribution link parameters

> 📘 **Note**
>
> The attribution links in the following table are **mandatory**.
>
> See complete parameter lists for:
>
> * <Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters">AppsFlyer</Anchor>
> * <Anchor target="_blank" href="https://trackier.com/support/kb/tracking-macros/">Trackier</Anchor>

| AppsFlyer parameter | Trackier macro | Description |
| --- | --- | --- |
| &clickid= | `{click_id}` | Request the ID for each user session |
| &af\_siteid= | `{publisher_id}` | ID of the affiliate promoting an offer |
| &af\_c\_id= | `{camp_id}` | Offer ID |

## Postback URLs for install and in-app events

This section provides examples of postback URLs and parameters for install and in-app events.

### **iOS** postback URLs

#### Global install postback

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}
```

#### Global in-app event postback

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}&goal_value={event-name}
```

### **Android** postback URLs

#### Global install postback

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}
```

#### Global in-app event postback

```http
https://yourdomain.com/acquisition?click_id={click_id}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}&goal_value={event-name}
```

### Postback parameters

| AppsFlyer Base URL | Description |
| --- | --- |
| yourdomain.com | <ul><li>Network ID (domain) name</li><li>Provided by Trackier</li></ul> |
| event-name | <ul><li>In-app event name</li><li>Defined by the advertiser</li></ul> |
| security\_token | Provided by Trackier |
| Country code, advertising ID, IDFA, etc. | [Optional] Attribution information that can be added to a postback |

## Finalizing your registration

Already integrated with AppsFlyer? Send us the URLs using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.

Not yet integrated with AppsFlyer? Complete the <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">Ad partners registration application</Anchor>.

<div data-zendesk-anchors="01JFT1SETSSMD0Z0EEQZCYPDB6=attribution-link-url 01JFT1SETTCEC1CAGT89SGNZNX=base-attribution-link-url 01JFT1SEVJTM09KHEKS51KQB7F=attribution-link-parameters 01JFT1SEVJR7TW06CAZWGMBZEB=note postback-urls-for-install-and-inapp-events=postback-urls-for-install-and-in-app-events 01JFT1SEWCM9DFRANRJRDSG5DC=postback-urls-for-install-and-in-app-events 01JFT1SEWCSS585NF8P0T251PZ=ios-postback-urls 01JFT1SEWD3A0JP6MRM1QXKX53=global-install-postback global-inapp-event-postback=global-in-app-event-postback 01JFT1SEWDT1CWHHTVWVACDT0B=global-in-app-event-postback 01JFT1SEWD0HA5WKC83V8HYAA2=android-postback-urls global-install-postback::1726dfc2=global-install-postback-1 01JFT1SEWDY7882HGY032SPGP7=global-install-postback-1 global-inapp-event-postback::ab23c9cb=global-in-app-event-postback-1 01JFT1SEWDYKTWDE536A4ZY34G=global-in-app-event-postback-1 01JFT1SEWEZQF38K9V9M6TNP3N=postback-parameters 01JFT1SEWTPX9BH7N1FPN4NJJW=finalizing-your-registration" />
