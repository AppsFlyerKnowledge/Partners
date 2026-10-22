---
title: SKAN CV schema API for ad networks
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2023-03-05T13:50:47Z'
  id: 11705009866001
  locale: en-us
  section: End-user privacy
  section_id: 6551186412689
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/11705009866001-SKAN-CV-schema-API-for-ad-networks
---
> **At a glance**: See the SKAN CV schema as mapped by the advertiser.

## SKAN CV schema API for ad networks

With SKAdNetwork (SKAN) attribution, advertisers grade user quality by setting conversion values (CV) based on post-install user activity during specific time periods (windows). <Anchor target="_blank" href="/marketers/docs/skadnetwork-skan-solution-guide">Learn more about SKAN</Anchor>

iOS reports the CV via postbacks sent to the ad network placing the ad. Starting iOS 15 advertisers can also instruct iOS to send the postbacks directly to AppsFlyer.

This API provides ad networks the CV-to-attribution-events-and-values map. Ad networks use it to decode the postbacks that they receive.

The API returns as a nested JSON. The schema for each app is separate. The mappings per CV are contained within the conversion\_value\_mapping array.

To use the API, ask your developer to follow their <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">SKAN CV schema API for ad networks instructions</Anchor>. For a list of keys and their description, click 200 in the simulator.

**Note**:

* The CV value range is:
  * SKAN 4 window 1 fine value: 0-63.
  * SKAN 4 windows 1, 2, and 3 coarse value: low, medium, or high.
  * SKAN 3 and below: 0-63
* Advertisers can change the CV mapping at any time.
* You, the ad network, must query this API daily, to ensure that you have the most updated schema.