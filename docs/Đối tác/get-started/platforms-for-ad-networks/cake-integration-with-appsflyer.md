---
title: Cake integration with AppsFlyer
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
  created_at: '2016-01-11T14:44:55Z'
  edited_at: '2024-12-23T15:15:33Z'
  id: 207273986
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/207273986-Cake-integration-with-AppsFlyer
---
> **At a glance:** Ad networks that use CAKE can receive attribution data from AppsFlyer about installs and in-app events.

## Base attribution link

Below you can find the base attribution link with a detailed explanation per each parameter:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer endpoint |
| app\_id | Application unique ID - Dynamic value changed per app promoted |
| pid | Media source name include **\_int** to identify<br />**integrated** network at AppsFlyer servers |
| c | Campaign name |

### Recommended attribution link parameters

| AppsFlyer Parameter | CAKE Macros | Description |
| --- | --- | --- |
| clickid | #oreqid# | Request ID of each user session - **Required** |
| af\_siteid | #affid# | ID of the Affiliate promoting the offer - **Optional** |

For a complete AppsFlyer parameter list, click <Anchor target="_blank" href="/marketers/vi/docs/about-link-structure-and-parameters">here</Anchor>

For a complete CAKE macro list, click <Anchor target="_blank" href="https://support.getcake.com/support/solutions/articles/5000566463-tokens">here</Anchor>.

### Complete attribution link template

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#oreqid#
```

## Install and in-app event postbacks

### Global install postback

```http
https://{company-domain}.com/p.ashx?f=pb&r=(Click-ID)
```

### Global in-app event postback

```http
Click-ID
```

`{Company-Domain}` the network ID (domain) name provided by CAKE.  
e= Set as **Event Tag** in the AppsFlyer dashboard for each App by the advertiser - This is the actual in-app event name from the application.  
For complete CAKE postback structure Click Here

### AppsFlyer in-app events dashboard

<Image align="center" alt="IAEP.png" src="https://files.readme.io/3ce734c3930649fdb0b119cd6e12e135e6bcba19225862e9e93b93991451fc8b-360002326529.png" />

Additional attribution information can be added to the postback by request such as Country Code, Advertising ID, IDFA, and so on.

## Finalizing your registration

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div data-zendesk-anchors="01EZPMKP0AFM26H2ZG9FY1D2S4=base-attribution-link 01EZPMKP0A7DBV5KAGZ08C3R49=recommended-attribution-link-parameters 01EZPMKP0AH1MB0XYE3PXQPP0V=complete-attribution-link-template install-and-inapp-event-postbacks=install-and-in-app-event-postbacks 01EZPMKP0A2D0PB41GD04HX9JX=install-and-in-app-event-postbacks 01EZPMKP0AVAJRP8YM48T4GV47=global-install-postback global-inapp-event-postback=global-in-app-event-postback 01EZPMKP0AM7JD7HWW7BCJDQF3=global-in-app-event-postback appsflyer-inapp-events-dashboard=appsflyer-in-app-events-dashboard 01EZPMKP0AJTYT0G9E8G833KT0=appsflyer-in-app-events-dashboard h_01HY03H1PMWZX3T12RZFV15CFE=finalizing-your-registration" />
