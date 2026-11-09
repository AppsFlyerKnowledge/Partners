---
title: Cost-sharing options for ad networks
metadata:
  keywords:
    - clicks
    - Partner
    - cost
    - Ad Networks
    - Partners
    - ad spend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2020-09-07T13:50:24Z'
  edited_at: '2024-05-22T12:07:38Z'
  id: 360012893658
  locale: en-us
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360012893658-Cost-sharing-options-for-ad-networks
---
> **At a glance:** Compare cost-sharing methods available to AppsFlyer ad network partners.

<div id="sharing-cost-with-appsflyer-and-advertisers" />

## Sharing cost with AppsFlyer and advertisers

Advertisers use AppsFlyer as their source of truth for ROI, billing, and to make marketing budget allocation decisions. For networks to be visible, sharing cost data with AppsFlyer is a must. Networks with no cost data appear at the bottom of the AppsFlyer dashboard list.

Ad networks share cost with AppsFlyer using any of the following: 

* **InCost API**: Push data to AppsFlyer
* **Cost API**: AppsFlyer pulls data
* **Cost Import**: Cost data files are uploaded/sent to AppsFlyer
* **Cost by click:** Networks report cost each time an attribution link is clicked

<div id="cost-badge-for-ad-networks" />

### Cost badge for ad networks

<Image align="center" alt="CostBadge.jpg" src="https://files.readme.io/6b660b68b932802f7982a3beb3a155ecc350de1b4cb3baede6e84ef0d704388c-360011247338.jpg" />

* A cost badge displays in the <Anchor target="_blank" href="/marketers/docs/partner-integrations#partner-details-and-performance">partner details page</Anchor> highlighting partners using the InCost or Cost API.
* The badge certifies that the partner as a cost-capable partner.
* Internal analytics and extensive user surveys show that advertisers are always on the lookout for new partners. Those with a cost badge are more likely to stand out, as advertisers want to understand their marketing performance based on ROI analysis.

<div id="reporting-cost-options-available-to-ad-networks" />

### Reporting cost options available to ad networks

| Option | Qualify for a cost badge | Option characteristics |
| --- | --- | --- |
| <Anchor target="_blank" href="/partners/docs/incost-api-for-ad-networks">InCost API</Anchor> | ✓ | The ad network has full ownership of when to set up InCost reporting.<br /><br />InCost has the following features:<ul><li>Supports all cost models</li><li>Accurate and reliable</li><li>Fully automated</li><li>Ad network partner controls:<ul><li>Data upload scheme</li><li>When to upload (data freshness rate)</li></ul></li><li>The advertiser grants permission in the AppsFlyer dashboard to the partner to upload cost data</li></ul>**Limitation**:<br /><br />AppsFlyer agency accounts aren't supported. |
| Cost API | ✓ | <ul><li>Supports all cost models</li><li>Accurate</li><li>Partner retains some control over their cost data in AppsFlyer</li><li>Supports cost for agency accounts in AppsFlyer</li><li>Advertisers provide their partner credentials in the AppsFlyer dashboard</li><li>Data refresh rate: 6 times a day, every four hours</li></ul>**Limitation**:<br /><br />Integration is subject to AppsFlyer priorities. |
| <Anchor target="_blank" href="/partners/docs/cost-import-for-ad-networks">Cost Import</Anchor><br /><br />(file upload) | No | <ul><li>The ad network partner:<ul><li>Uploads data manually if it does not have engineering resources to automate</li><li>Controls when to upload data</li><li>Retains some control over their cost data in AppsFlyer</li><li>Integration is per app. The advertiser grants permission in the AppsFlyer dashboard to the partner to upload cost data.</li><li>Matching to attribution data is based on campaign name (not campaign ID)</li></ul></li></ul>**Limitation**:<ul><li>AppsFlyer agency accounts aren't supported</li><li>Risk of failure if the upload is automated via email</li></ul> |
| <Anchor target="_blank" href="/partners/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Cost by click</Anchor><br /><br />(on the attribution link) | No | <ul><li>Quick solution for CPI campaigns</li><li>Near real-time</li><li>Cost by click can be less accurate if the advertiser uses SKAdNetwork</li></ul>**Limitation**:<ul><li>Limited to CPI cost model</li><li>If the wrong data is sent on the link, it can't be changed retroactively</li><li>Retargeting not supported</li><li>Cost reported by click is displayed in the SKAdNework dashboard when available</li></ul> |

<div data-zendesk-anchors="h_01HN0A1ER3MNZM508ZCG9KP26P=sharing-cost-with-appsflyer-and-advertisers h_01HN0A1ER4K1V4479W5SXCEC30=cost-badge-for-ad-networks h_01HN0A1ER4Y128ZHJERXS6A8ET=reporting-cost-options-available-to-ad-networks" />
