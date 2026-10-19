---
title: Protect360—FAQ for partners
excerpt: Find answers to questions frequently asked by partners about Protect360.
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  created_at: '2023-06-12T12:43:34Z'
  edited_at: '2026-01-25T06:59:41Z'
  id: 16091549732497
  locale: en-us
  section: Learn more
  section_id: 6551121200017
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/16091549732497-Protect360-FAQ-for-partners
---
## Impression level anomalies

<div id="why-are-impressionsclicks-being-capped" />

<Accordion title="Why are impressions being capped?">

The AppsFlyer Protect360 system takes into account various parameters when making decisions on capping ad engagements, including but not limited to the volume of impressions, CVR, detected anomaly rate, normal fluctuations in activity, as well as industry and geographic benchmarks. The algorithm is dynamic and updated on an hourly basis, to take into consideration changing trends.

Once the capping mechanism is triggered, Protect360 blocks the ad network’s impressions for the related app within the current 24-hour cycle. This means that any impressions that occur after the threshold is reached are not recorded by AppsFlyer, nor are they eligible for attribution.

A network can avoid surpassing the threshold by stopping campaigns and publishers with unusually high volumes of ad engagements that do not show any impact on performance results.

We recommend taking a look at these articles:  
[Impression capping](/docs/protect360-for-integrated-partners#impression-capping)  
[Capping FAQ](/docs/protect360-for-integrated-partners#faq)

</Accordion>

<div id="the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate" />

<Accordion title="Why are installs blocked due to click flooding, yet the conversion rate is high?">

Our click-flood algorithms run at various intervals over the course of the day, and whenever the threshold is crossed, based on internal parameters and logic, the publisher’s ad engagements will be ineligible for attribution.

**Please note:** Some of our click flood algorithms work across apps, implying that anomalies originating from identical fraudulent sources would be recognized for other advertised apps as well.

We recommend reading: [What is click flooding?](https://www.appsflyer.com/glossary/click-flooding/)

</Accordion>

## Install/in-app event level anomalies

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="Why was my test install rejected from attribution?">

AppsFlyer’s anti-fraud detection applies different methodologies across various protection layers, such as single installs and install clusters. Clusters are being reviewed in various aggregations: by publisher, media source, app, and so on. The fraudulent activity is examined using various statistical algorithms and machine learning algorithms that consider each cluster as a whole. Thus, if a cluster is found fraudulent with high statistical significance, all installs in that cluster are considered fraudulent. It's a well-known fraudster tactic to mix some legitimate installs into high volumes of fraudulent activity in the hope that the fraud will be “diluted” enough to avoid triggering blocking mechanisms.

By default, all incoming installs are considered as LIVE traffic - hence to ensure your test install isn't categorized under the Protect360 algorithms, you would need to follow the steps mentioned in [this article](/marketers/docs/registering-test-devices) to register your device as a test device before performing a test.

</Accordion>

<div id="What-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="What detection methods are used to detect install rejections?">

Please review the "fraud sub reason" associated with the rejection for better clarity. This data is also available in Protect360 reports and on the Protect360 dashboard, subject to access granted by the respective advertiser.

We recommend reading about [Protect360 blocked reasons](/marketers/docs/protect360-raw-data-reports#blocked-reasons).

</Accordion>

## Protect360 data visibility and comprehension

<div id="how-do-i-gain-visibility-into-the-protect360-results" />

<Accordion title="How do I gain visibility into the Protect360 results?">

You can view the results of our detection efforts using the Protect360 dashboard and raw data reports, subject to access granted by the respective advertiser.

We recommend taking a look at these articles:  
[Protect360 Dashboard](/marketers/docs/protect360-dashboard)  
[Protect360 Raw Data](/marketers/docs/protect360-raw-data-reports#getting-raw-data-reports)

</Accordion>

<div id="how-can-i-get-notified-in-realtime-about-blocked-traffic" />

<Accordion title="How can I get notified in real time about blocked traffic?">

AppsFlyer provides rejected attribution postbacks to ad networks for every install Protect360 rejects from attribution.

You can enable “rejected postback” by appending “rejected postback” parameters to your postback template by using [Integration Management](/docs/self-serve-integration-management-for-ad-networks).

</Accordion>

<div id="why-do-i-see-spikes-in-postattribution-detections" />

<Accordion title="Why do I see spikes in post-attribution detections?">

Real-time detection before attribution and post-attribution detection both belong to AppsFlyer’s Protect360 anomaly detection mechanism that applies in different time dimensions.

Compared to real-time detection, post-attribution detection relies more on data pointers collected after the install, during which, if anomalies are observed, Protect360 will record anomalous activities and display them under the post-attribution category.

Considering the above, certain detection methods (timestamp\_anomalies, behavioral\_anomalies, etc.) are more likely to be detected in the post-attribution stage rather than in real time, since the data is inconclusive on the level of an individual install but gains significance when examined for its distribution in statistical analysis.

Learn more about [post-attribution detection](/marketers/docs/protect360-anti-fraud-guide#postattribution-detection).

</Accordion>

<div data-zendesk-anchors="click-impression-level-anomalies=impression-level-anomalies 01H8GKS08Y22PX2SBTW5ME02C4=impression-level-anomalies 01H8GKS08YXVK4CPNW9TX9XBYN=why-are-impressionsclicks-being-capped 01H8GKS08ZGNTMNZ5JH846T9Q9=the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate install-inapp-event-level-anomalies=installin-app-event-level-anomalies 01H8GKS08ZRA7YT9FWJNBBSV4Q=installin-app-event-level-anomalies 01H8GKS08Z2M0RTMR4GM1BJE7G=why-was-my-test-install-rejected-from-attribution What-detection-methods-are-used-to-detect-install-rejections%3F=What-detection-methods-are-used-to-detect-install-rejections 01H8H30KARRPAPT9XRREDYKHVT=What-detection-methods-are-used-to-detect-install-rejections protect360-data-visibility-and-understanding=protect360-data-visibility-and-comprehension 01H8GKS08ZX2W1G0K165H96N4Z=protect360-data-visibility-and-comprehension 01H8GKS08ZGEEK0HQVCRD546MW=how-do-i-gain-visibility-into-the-protect360-results 01H8GKS08ZC6SB4PT53JG5QKHG=how-can-i-get-notified-in-realtime-about-blocked-traffic 01H8GKS08Z673WG6C6JGW31F42=why-do-i-see-spikes-in-postattribution-detections" />
