---
title: Affise integration with AppsFlyer
metadata:
  keywords:
    - Integration
    - affise
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
  created_at: '2016-04-19T12:08:58Z'
  edited_at: '2024-12-23T15:05:34Z'
  id: 208537116
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/208537116-Affise-integration-with-AppsFlyer
---
> **At a glance:** Ad networks that use Affise can utilize the AppsFlyer probabilistic modeling solution to receive attribution data about installs and in-app events.

To start the integration you must send AppsFlyer both the attribution link and the postback for reporting purposes.

<div id="base-attribution-link" />

## Base attribution link

Below you can find the base attribution link with a detailed explanation per each parameter:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}&af_c_id={offerid}
```

**Obligatory Attribution Link Parameters**

| AppsFlyer Parameter | Affise Macros | Description |
| --- | --- | --- |
| clickid | `{clickid}` | Request ID of each user session |
| af\_siteid | `{pid}` | ID of the affiliate promoting the offer |
| af\_c\_id | `{offer_id}` | ID of the offer |

For a complete AppsFlyer parameter list <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">click here</Anchor>.

<div id="complete-attribution-link-template" />

## Complete attribution link template

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}
```

<div id="install-and-in-app-event-postbacks" />

## Install and in-app event postbacks

The following are examples of Install and In-App Event Postbacks:

<div id="global-install-postback-ios" />

### Global install postback iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}
```

<div id="global-install-postback-android" />

### Global install postback Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}
```

<div id="global-in-app-event-postback-ios" />

### Global in-app event postback iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}&goal={event-name}
```

<div id="global-in-app-event-postback-android" />

### Global in-app event postback Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}&goal={event-name}
```

Domain.com is the network ID (domain) name provided by Affise.

e= Set as **Event Name** in the AppsFlyer dashboard for each App by the advertiser - This is the actual in-app event name from the application.

Additional attribution information can be added to the postback by request such as Country Code, Advertising ID, IDFA etc.

<div id="finalizing-your-registration" />

## Finalizing your registration

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div data-zendesk-anchors="01JFT0RZG0F67JFBC7W5KK54BM=base-attribution-link 01JFT0RZG2QTT3Z9S6SVNV5VE7=complete-attribution-link-template install-and-inapp-event-postbacks=install-and-in-app-event-postbacks 01JFT0RZG3C7MBBYFKA6W813PF=install-and-in-app-event-postbacks 01JFT0RZG3HM9P81XYGKHZXHFK=global-install-postback-ios 01JFT0RZG4JCDP8D4CWQW02AY7=global-install-postback-android global-inapp-event-postback-ios=global-in-app-event-postback-ios 01JFT0RZG40N0VNNVMDBFYNT9E=global-in-app-event-postback-ios global-inapp-event-postback-android=global-in-app-event-postback-android 01JFT0RZG4PA9WTP212AX52QWZ=global-in-app-event-postback-android 01JFT0RZG52JW6C5GR0KA4CZF6=finalizing-your-registration" />
