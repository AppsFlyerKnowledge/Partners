---
title: ROI360—cost reporting options for agencies
metadata:
  keywords:
    - clicks
    - cost
    - Agencies
    - Partners
    - ad spend
    - Xpend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Agencies
    - ROI360
  created_at: '2020-10-04T15:07:34Z'
  edited_at: '2026-10-13T01:46:28Z'
  id: 360014054998
  locale: ko
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ko/articles/360014054998
---
> **At a glance:** Report cost data via cost API (requires a subscription to ROI360 premium solution), and cost by click.

## Cost reporting for agencies

Advertisers use AppsFlyer as their source of truth for ROI, billing, and to make marketing budget allocation decisions. To do so, they need to have all the cost information on a single platform. ROI360, an AppsFlyer premium solution, enables advertisers and agencies to collect cost data via API, making it available for viewing using AppsFlyer dashboards and reporting tools. 

Cost data can be aggregated via either of the following methods: 

* **Cost API**: AppsFlyer pulls data from partners
* **Cost by click:** Networks report cost each time an attribution link is clicked

The following table lists cost aggregation capabilities available with, and without, ROI360.

| Option | Requires ROI360 subscription | Description |
| --- | --- | --- |
| <Anchor target="_blank" href="/marketers/ko/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">Cost API</Anchor> | Yes | <ul><li>Agencies use their ad network API credentials to connect to enable cost API in the AppsFlyer dashboard.</li><li>Cost data is reflected according to <Anchor target="_blank" href="/marketers/ko/docs/view-agency-data">agency transparency</Anchor>. (For SRNs, this includes clicks and impressions.)</li><li>Supports all cost models</li><li>Accurate</li><li>Data refresh rate: 6 times a day, every four hours.</li></ul> |
| <Anchor target="_blank" href="/partners/ko/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Cost by click</Anchor><br /><br />(on the attribution link) | No | <ul><li>Agencies send their CPI, value, and cost currency on the attribution link. AppsFlyer aggregates the cost.</li><li>Data freshness: Near real-time</li></ul>**Limitations:**<ul><li>Limited to CPI cost model</li><li>If the wrong data is sent on the link, it can't be changed retroactively.</li><li>Cost reported by click is not available in the SKAdNework dashboard.</li><li>Cost by click is less accurate if the advertiser uses SKAdNetwork.</li></ul> |