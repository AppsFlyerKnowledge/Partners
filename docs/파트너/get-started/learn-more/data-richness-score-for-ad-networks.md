---
title: Data richness score for ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - attribution link
    - data richness score
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-06-03T09:27:03Z'
  edited_at: '2026-10-13T01:51:43Z'
  id: 360009443338
  locale: ko
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/ko/articles/360009443338
---
> **At a glance:** Improve the quality of the data you provide to advertisers using the AppsFlyer data richness score.

The quality of the data that advertisers receive from ad networks on which they run their campaigns can play an important role in marketing decisions.

The data provided by different ad networks vary in terms of its coverage, accuracy, and granularity. Partial and inaccurate data reduces the advertisers' ability to analyze and optimize their campaign performance on AppsFlyer.

Data richness score, a metric provided by AppsFlyer, indicates the comprehensiveness of ad networks' data. This score is open to all advertisers, so they are able to understand each network's capabilities and data quality, and make educated business decisions.

To maximize the score, ad networks must overcome the data gaps they have.

## Data richness score

**To see your data richness score:**

1. Log into your account.
2. Open the dashboard for any app you manage.
3. Click **Active Integrations** in the left sidebar.  
   The score indicator is shown under your network name.

   ![integrated-partners-data-richness.png](https://files.readme.io/ee68f4ba63ef4e27292ed6b857e2cd05e4d83f8ba65a80655d1bf8b63df94f5f-360009360018.png)

Advertisers can see the data richness score (low, medium, or high) for each ad network that has an integration with AppsFlyer.

### Included data

To see the score in each data category included in the score, hover above the indicator. A pop-up opens, which presents the final score and the data groups: Campaign data, Ad data, and Publisher data.

In order to receive a high score, the following parameters should be provided by an ad network on all clicks and views:

* Campaign data:
  * Campaign ID
  * Campaign name
* Ad data:  
  * Adset ID
  * Adset name
  * Ad ID
  * Ad name
  * Ad type
* Publisher data
  * Site ID
  * Subsite ID
  * Channel

### Data threshold

* The score is calculated weekly and can rise or drop depending on the completeness of the parameters listed above.
* There is a minimum amount of conversions (installs, reattributions, reengagements) required for the score to be calculated. If the network has fewer conversions than the minimum within a given week, on the following week the score indicator will be disabled and no data categories will be shown.

## Next steps

To add more parameters, and improve your integration and visibility in the AppsFlyer platform,

1. Check which parameters your integration is missing.
   * <Anchor target="_blank" href="/partners/ko/docs/getting-started-onboarding-guide-for-ad-networks#1부-연동-및-테스트">Read about attribution link templates</Anchor>
   * <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#어트리뷰션-링크-파라미터">Check the full list of parameters available for use</Anchor>
2. Contact your PDM to update the link template or get more information.