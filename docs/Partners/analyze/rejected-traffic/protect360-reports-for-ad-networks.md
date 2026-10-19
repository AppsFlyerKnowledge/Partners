---
title: Protect360 reports for ad networks
excerpt: >-
  Ad networks responsible for user acquisition and retargeting can receive data
  regarding blocked clicks and impressions.
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  created_at: '2022-02-08T14:53:48Z'
  edited_at: '2023-03-12T12:50:25Z'
  id: 4420246395793
  locale: en-us
  section: Rejected traffic
  section_id: 6551666000273
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/4420246395793-Protect360-reports-for-ad-networks
---
## Protect360 reports for ad networks

**Disclaimer**: This article provides information on Protect360 reports available only to ad networks. For data that is also available to advertisers, see [Protect360 for integrated partners](/docs/protect360-for-integrated-partners).

Ad networks can receive reports via [Data Locker for Partners](/docs/data-locker-for-partners) with valuable information regarding clicks and impressions that are blocked either because of:

* Blocked clicks and impressions that occur when ad networks cross their fraud limit. The report includes total blocks, as well as blocks due to click and impression capping. [Learn more about capping](/docs/protect360-for-integrated-partners#impression-capping)
* Failed click signatures that occur when a click with the network's PID parameter networks and a click signature to validate clicks can't be validated. [Learn more about click signing](/docs/click-signing-for-ad-networks)

Ad networks can then ingest this network-level data with cross-customer visibility of their blocked clicks and impressions and use it to protect against fraud.

### Report considerations

* Data arrives in CSV format to the UA/retargeting partner's bucket.
* Contains dimensions and metrics relevant to the ad network (that is cleaned of all dimensions irrelevant to the ad network).
* Available via [Data Locker for Partners](/docs/data-locker-for-partners).
* Data freshness: [Daily, meaning data for Day 0 arrives on Day 1](/appsflyer-marketers/docs/about-data-freshness-and-timezone-support#ad-revenue). Data is written daily at 07:00 [UTC time](/appsflyer-marketers/docs/about-data-freshness-and-timezone-support#daily-processing) to the h=23 of your Data Locker bucket.
* Apps included: A single report contains the data of all apps.

## Report types

<div id="blocked-clicks-and-impressions" />

<Accordion title="Blocked clicks and impressions">

This report contains aggregate level data about clicks and impressions that are blocked due to capping or any other reason. 

#### Report structure: Fields/Dimensions

| **Field** | **Remarks** |
| --- | --- |
| app\_id | App ID in the AppsFlyer platform. |
| site\_id | ID that identifies the publisher that displays the ad. |
| date | Blocked date |
| agency | <ul><li>Agency that brought the traffic via this ad network.</li><li>Returns as null if there is no agency involved.</li></ul> |

#### Report structure: Metrics

| **Field** | **Remarks** |
| --- | --- |
| number\_of\_blocked\_clicks | Total number of the network’s blocked clicks |
| number\_of\_blocked\_impressions | Total number of the network’s blocked impressions |
| number\_of\_capped\_clicks | The number of the network’s capped clicks (out of the total blocked clicks) |
| number\_of\_capped\_impressions | The number of the network’s capped impressions (out of the total blocked impressions) |

</Accordion>

<div id="failed-click-signatures" />

<Accordion title="Failed click signatures">

This report contains user-level about failed click signatures. Meaning, when ad networks use the [AppsFlyer click signing method](/docs/click-signing-for-ad-networks), the report contains clicks of URLs with the network’s PID that don't have validated click signatures, either because the signature is invalid or expired, or the click is not signed at all. Click signing failures could occur when there are technical errors in the implementation of click signatures by the ad network, or when clicks are sent on behalf of the network (with its PID) by another party.

#### Report structure: Fields/Dimensions

| **Field** | **Remarks** |
| --- | --- |
| event\_time |  |
| original\_url |  |
| failed\_signing\_reason | For example:<ul><li>Invalid signature</li><li>Missing signature</li><li>Expired signature</li><li>Expired secret key</li></ul> |
| is\_blocking\_enabled | Refers to the configuration mode of the [click signature API](/docs/click-signing-for-ad-networks):<ul><li>TRUE for enabled.</li><li>FALSE for report-only.</li><li>Not included in the report for disabled.</li></ul> |

</Accordion>

<div data-zendesk-anchors="report-structure-fieldsdimensions::44afb679=report-structure-fieldsdimensions-1" />
