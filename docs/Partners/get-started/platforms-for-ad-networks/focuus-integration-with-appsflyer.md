---
title: FOCUUS integration with AppsFlyer
metadata:
  keywords:
    - Focuus
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
  created_at: '2016-10-02T05:18:19Z'
  edited_at: '2026-05-05T07:16:25Z'
  id: 213374546
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/213374546-FOCUUS-integration-with-AppsFlyer
---
> **At a glance:** Ad networks that use FOCUUS can utilize the AppsFlyer Probabilistic modeling solution to receive attribution data about installs and in-app events.

<div id="creating-your-attribution-link" />

## Creating your attribution link

The attribution link consists of the below AppsFlyer base attribution link and additional macros added by the ad network.

See below AppsFlyers base attribution link with a detailed explanation per macro:

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer endpoint |
| app\_id | Application unique ID |
| pid | Media source name include \_int to identify integrated network at AppsFlyer servers |
| c | Campaign name |

<div id="recommended-attribution-link-parameters" />

### Recommended attribution link parameters

| AppsFlyer Parameter | FOCUUS Macros | Description |
| --- | --- | --- |
| **clickid** | **`{tid}`** | **Request ID of each user session** - **Required** |
| af\_siteid | `{publisher_id}` | ID of the Affiliate promoting the offer - Optional |

For a complete list of AppsFlyer parameters, <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#attribution-link-parameters">click here</Anchor>.

FOCUUS allows an unlimited number of macros, and you can name them as you wish, <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#attribution-link-parameters">click</Anchor> <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827379-traffic-source-template-tokens-macros">here</Anchor>.

<div id="complete-attribution-link-template" />

### Complete attribution link template

`https://app.appsflyer.com/com.appsflyer?pid={traffic_source}&clickid={tid}&af_siteid={publisher_id}`

This attribution link is set on your FOCUUS campaign <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827784-adding-a-new-link">destination</Anchor>.

<div id="install-and-in-app-event-postbacks" />

## Install and in-app event postbacks

To create your install and in-app event postbacks at **FOCUUS**

1. Create a <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827775-events">new event</Anchor> (Install and any other in-app events).
2. <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Generate pixel</Anchor> (postback) for implementation.
3. Copy the postback URL that appears in the box labeled <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Server2Server Pixel</Anchor>.
4. Replace the TRANSACTION\_ID with AppsFleyr macro - “**clickid**”  
   `https://pixel.focuusing.com/event.php?type=imp&tid={clickid}`

**Optional Postback Parameters**

| FOCUUS Macros | Description | Example |
| --- | --- | --- |
| event\_value | Payout value for each type of event | `https://pixel.focuusing.com/event.php?type=cpi&tid={Your_TRANSACTION_ID}&eid=49816&event_value={25}` |

**Event name (Install, Registration, etc.) appears by default on the generated pixel. for example:**

* `https://traffic.focuusing.com/install?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/conversion?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/ftd?tid={TRANSACTION_ID}`

<div data-zendesk-anchors="01JFT11W3GWZ3QFYPHEZTS7EX7=creating-your-attribution-link 01JFT11W3QWT08KMGEPGK7MV5R=recommended-attribution-link-parameters 01JFT11W3Y7HRB7FYS1K173G2W=complete-attribution-link-template install-and-inapp-event-postbacks=install-and-in-app-event-postbacks 01JFT11W3YMN4RBW0WFTQ9EADK=install-and-in-app-event-postbacks" />
