---
title: TUNE (formerly, HasOffers) integration with AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Tune
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
  created_at: '2015-12-22T14:55:13Z'
  edited_at: '2024-12-23T15:20:29Z'
  id: 207034806
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/207034806-TUNE-formerly-HasOffers-integration-with-AppsFlyer
---
> **At a glance:** Learn how ad networks that use TUNE (formerly HasOffers) to manage affiliate marketing campaigns can integrate with AppsFlyer and receive attribution data about installs and in-app events.

**To initiate the integration, prepare, and send the following information to AppsFlyer:**

1. Your [attribution link](/docs/tune-formerly-hasoffers-integration-with-appsflyer#create-attribution-link)
2. Your [postbacks](/docs/tune-formerly-hasoffers-integration-with-appsflyer#create-install-and-in-app-event-postbacks) (for installs and in-app events)

## Create attribution link

The attribution link consists of the following AppsFlyer base attribution link and additional macros added by the ad network.

See the following AppsFlyers base attribution link with a detailed explanation per macro:

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer endpoint |
| app\_id | Unique app ID – dynamic value changed per app promoted |
| pid= | Media source name concatenated with `_int` to identify<br />integrated networks |
| c= | Campaign name |

### Example attribution link after adding TUNE macros

```
 
```

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_c_id={offer_id}&af_ad_id={offer_file_id}&idfa=
{ios_ifa}&advertiser_id={google_aid}&af_sub5={offer_id}
```

* In the previous link, `af_sub5={offer_id}` has been added for TUNE reporting purposes.

Read more about [TUNE macros](https://help.tune.com/hasoffers/parameters-macros-in-hasoffers/).

## Create install and in-app event postbacks

Step-by-step instructions for creating your install and in-app event postbacks:

1. Create or select an offer that uses the Postback w/Transaction ID protocol.
2. In the details section of the offer page, click the link labeled **Tracking**.
3. Copy the URL from the box labeled **Postback URL**.
4. Remove the `offer_id` parameter and value from the postback URL to convert it from a specific postback to a global postback.

Read more about [TUNE global postback URLs](http://help.tune.com/hasoffers/global-postback-urls/).

### Sample postbacks

#### Global install postback:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_lsr?offer_id={af_c_id}&transaction_id={clickid}
```

#### In-app event postback:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_goal?a=lsr&goal_id={goal_id}&transaction_id={clickid}
```

In the above postback URLs:

* NETWORK\_ID = domain name (network ID) provided by TUNE
  * To ensure proper attribution, the NETWORK\_ID should always be the branded domain name provided by TUNE, not a custom tracking domain used for a specific offer (if any).
* goal\_id = event tag in the AppsFlyer dashboard for each of your apps. This is the actual in-app event name from the app.

Learn more about <Anchor target="_blank" href="/partners/docs/dynamic-event-mapping-for-in-app-events">Dynamic Event Mapping for In-App Events</Anchor>.

## Finalizing your registration

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div data-zendesk-anchors="h_01ET22GJ5N67DKECBQ41QEPEAT=create-attribution-link 01JFT1MXJJF3C17B3Y9Q8604BM=example-attribution-link-after-adding-tune-macros create-install-and-inapp-event-postbacks=create-install-and-in-app-event-postbacks h_01ET22H0A0MQ3HH30AJ1TMFNTQ=create-install-and-in-app-event-postbacks 01JFT1MXJNSTV7YRVX3BPZ50CY=sample-postbacks 01JFT1MXJNJBY1P51JQ3ES7QYS=global-install-postback inapp-event-postback=in-app-event-postback 01JFT1MXJNMF0FWJ2RFER3E316=in-app-event-postback 01JFT1MXJQAXV53RKACW0VAS6E=finalizing-your-registration" />
