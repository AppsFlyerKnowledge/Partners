---
title: Data Locker reports for API partners
excerpt: >-
  Reports listed in this article are available to you (API partners) in your
  Data Locker. Before we can share the data with you, the advertiser (app owner)
  must grant you data access as detailed in this article.
metadata:
  keywords:
    - Advertisers
    - Partners
    - marketing partners
    - Marketers
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Marketers
    - Data Locker
  created_at: '2023-01-08T11:32:00Z'
  edited_at: '2026-03-10T08:28:05Z'
  id: 12000718524561
  locale: en-us
  section: Data Locker
  section_id: 6551591547409
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/12000718524561-Data-Locker-reports-for-API-partners
---
## Data Locker reports for API partners

To get reports you, the API partner must:

* Ensure that the advertiser has provided you with permission to [access Aggregated analytics reporting](/docs/access-to-aggregated-analytics-tools-for-api-partners#grant-permission-to-a-partner).
* [Set up Data Locker](/docs/data-locker-for-partners#set-up-data-locker). **Note**: Skip steps 3-4.

The following reports are available to API partners: (daily)

* [Cohort unified](/marketers/docs/cohort-analytics-via-data-locker) (daily)
* [Cohort user acquisition](/marketers/docs/cohort-analytics-via-data-locker) (daily)
* [Cohort retargeting](/marketers/docs/cohort-analytics-via-data-locker) (daily)
* [Advanced aggregated (versioned) reports](/marketers/docs/advanced-aggregated-reports-in-data-locker) are also available, with better data freshness.

Reports are streamed to the h=23 folder.

<div id="specifications-and-limitations" />

<Accordion title="Traits and limitations">

| Spec | Remarks |
| --- | --- |
| Agency transparency | Not supported |
| App-specific timezone | Available in advanced aggregated (versioned) reports |
| App-specific currency | Yes |
| Organic data | Available |
| Non-organic data | Available |
| Cost data | Not available |
| Data freshness | <ul><li>For daily cohort reports:<ul><li>Reports are typically available by 10:00 UTC in the h=23 folder of the preceding day. For example, the report for data generated on Monday is in the Monday h=23 folder.</li><li>Exception: Ad revenue events have data freshness of Day 0+3. Meaning, ad revenue events in the Monday report occurred on Saturday.</li></ul></li><li>The first versioned reports are typically available by 06:00 UTC.</li></ul> |

Trait

</Accordion>

> 📘 **See also**
>
> * [Aggregated analytics tools for API partners](/docs/access-to-aggregated-analytics-tools-for-api-partners)

<div data-zendesk-anchors="data-locker-reports-for-marketing-partners=data-locker-reports-for-api-partners h_01HBZZ5BFJC82MW9JQ9MEX991S=data-locker-reports-for-api-partners h_01HBZZ5BFJYFH54X70RJ63CJCV=specifications-and-limitations h_01HE7RFGCZ65YJRX1VCND691CX=see-also" />
