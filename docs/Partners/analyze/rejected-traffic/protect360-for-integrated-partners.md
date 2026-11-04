---
title: Protect360 for integrated partners
metadata:
  keywords:
    - Protect360
    - Ad Networks
    - Partners
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2017-09-19T08:27:29Z'
  edited_at: '2026-05-25T07:54:54Z'
  id: 115004745523
  locale: en-us
  section: Rejected traffic
  section_id: 6551666000273
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/115004745523-Protect360-for-integrated-partners
---
> **At a glance:** Integrated partners (ad networks and agencies) can view fraud related to their traffic identified and blocked by the ProtectLITE and Protect360 engines, as well as the customer’s manually-defined validation rules.

<div id="overview" />

## Overview

AppsFlyer identifies and blocks fraud via: 

* <Anchor target="_blank" href="/marketers/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">ProtectLITE</Anchor>: Basic fraud protection for all customers.
* <Anchor target="_blank" href="/marketers/docs/protect360-anti-fraud-guide">Protect360</Anchor>: Advanced fraud protection for advertisers with a premium subscription plan.

Advertisers must give:

* Ad networks <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">permissions</Anchor> to **Access Protect360 dashboard and raw data** reports (that includes ProtectLITE), and **Access aggregate in-app events data** (for in-app event fraud).
* Agencies <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">permissions</Anchor> to **Access Protect360 dashboard and raw data.**

With the correct permissions, integrated partners can:

* View data related to the traffic they generated.
* Download related <Anchor target="_blank" href="/marketers/docs/protect360-anti-fraud-guide#raw-data">raw data reports</Anchor>.

There are also <Anchor target="_blank" href="/partners/docs/protect360-reports-for-ad-networks">raw data reports</Anchor> available to ad networks about impression capping, as well as failed click signatures, for which no advertiser permissions are required.

<div id="note" />

> 📘 **Note**
>
> For advertisers that work with ad networks through an agency, in order for both the ad network and agency to access data, the advertiser must integrate both the agency and ad network in AppsFlyer, and grant them both permission to access data.
>
> If only the agency is integrated and granted permissions, the ad network does not have access to the data.

<div id="dashboard-view" />

### Dashboard view

**Prerequisites**: Permission from the advertiser to access ProtectLITE and Protect360. 

Integrated partners can view the dashboard and charts; see the screenshot that follows.

Learn more about what data is available in the <Anchor target="_blank" href="/marketers/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting#dashboard">ProtectLITE</Anchor> and <Anchor target="_blank" href="/marketers/docs/protect360-anti-fraud-guide#dashboard">Protect360</Anchor> dashboards.   

Limitations:

* Ad networks cannot access the Anomalies dashboard.

[![p360_dashboard_1.jpg](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)

* Ad networks and Agencies cannot access the fraud protection studio, or the raw data level of tagged data. They can, however, see it aggregated in the Protect360 dashboard under tagged attribution and tagged in-app events. As well as identify fraud by tag type (new release etc) . To learn more about FPS see <Anchor target="_blank" href="/marketers/docs/beta-fraud-protection-studio">this article</Anchor>.

  <Image alt="" src="https://files.readme.io/7e8bee04ecaf53148f65ae0aa9b2e3559a550bdbc5a5ebf9047a7e82dc093966-44928678660881.png" width="624px" />

  <Image alt="" src="https://files.readme.io/fa35e6046d6c06579e602ccc1cb919e5312ec22055b3e29d3ead6b2a7ab5ea82-44928694758161.png" width="624px" />

<div id="raw-data-reports" />

### Raw-data reports

**Prerequisites**: Permission from the advertiser to access ProtectLITE and Protect360. 

Protect360 raw-data reports show identified and blocked fraud via ProtectLITE, Protect360, and Validation Rules.

Reports are available via:

* Export data: In AppsFlyer, from the side menu, select **Report** > **Raw Data Export**
* API: See the [ad network reporting API](/docs/protect360-for-integrated-partners#protect360-ad-network-reporting-api) section that follows.

Learn more about <Anchor target="_blank" href="/marketers/docs/protect360-raw-data-reports">Protect360 raw data reports</Anchor>.

<div id="protect360-ad-network-reporting-api" />

## Protect360 ad network reporting API

* The raw-data reports listed in this section are available to ad networks via API.
* Equivalent reports are available from the dashboard on the Export Data page.
* If the advertiser does not have a Protect360 subscription, only the Installs report is available.

**Prerequisites**

* To access advertiser data by API, the advertiser grants the ad network <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">permissions</Anchor> to access their Protect360 dashboard and data by API. Ad networks having access to the dashboard are permitted to use the API. No action is required by the advertiser.
* For a list of apps for which you have Protect360 permissions use <Anchor target="_blank" href="/partners/docs/app-list-api-for-ad-networks">get app list API.</Anchor>
* The admin needs to get an AppsFlyer <Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">V2.0 authentication token</Anchor> available in the dashboard.

<div id="protect360-api-reports" />

#### Protect360 API reports

| Report | Data freshness | Description |
| --- | --- | --- |
| Post-attribution in-app events fraud | Daily 10:00 UTC | <ul><li>In-app events performed by installs identified as fraudulent.</li><li>Any other in-app event judged as fraudulent irrespective of the install.</li></ul>The report can be optionally filtered by in-app event type as described in the parameters table that follows.<br /><br />Report topic: `fraud-post-inapps` |
| Post-attribution installs | Daily 10:00 UTC | <ul><li>Installs identified as fraudulent post-attribution.</li><li>The report can be optionally filtered by the detection date as described in the section that follows.</li></ul>Report topic: detection |
| Installs | Real-time | Blocked installs with the block reason<br /><br />Report topic: blocked\_installs\_report |
| In-app event | Real-time | In-app events performed by blocked users<br /><br />Report topic: `blocked_in-app_events_report` |
| Clicks | Real-time | Clicks performed by blocked users<br /><br />Report topic: `blocked_clicks_report` |

<div id="procedure-for-ad-networks-to-get-protect360-reports-by-download" />

#### **Procedure for ad networks to get Protect360 reports by download**

**To get a report using the API:**

1. Identify the required report from the preceding list.
2. Use the relevant curl example (in the following section) to prepare your script.
3. Ensure that you replace the following placeholders:
   1. App ID
   2. From date
   3. To date
   4. Bearer token  (AppsFlyer <Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">V2.0 authentication token</Anchor>)
4. Some calls have [optional parameters](/docs/protect360-for-integrated-partners#api-parameters), as described in this article.

<div id="curl-examples" />

### Curl examples

<div id="installs-blocked_installs_report" />

<Accordion title="Installs (blocked_installs_report)">

Replace the app\_id, from, to, and token placeholders.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_installs_report/app/{app_id}?from={2020-07-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-installs-detection" />

<Accordion title="Post-attribution installs (detection)">

Replace the app id, from, to, and token placeholders.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/detection/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additonal-fields=fraud_reason,fraud_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="inapp-event-blocked_in_app_events_report" />

<Accordion title="In-app event (blocked_in_app_events_report)">

Replace the app id, from, to, and token placeholders.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_in_app_events_report/app/?from=YYYY-MM-DD&to=YYYY-MM-DD&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-inapp-events-fraud-fraud_post_inapps" />

<Accordion title="Post-attribution in-app events fraud (fraud_post_inapps)">

Replace the app id, from, to, and token placeholders.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/fraud-post-inapps/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,fraud_reason,fraud_sub_reason,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="clicks-blockedclicks_report" />

<Accordion title="Clicks (blocked-clicks_report)">

Replace the app id, from, to, and token placeholders.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_clicks_report/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="protect360-ad-network-api-reference-guide" />

### Protect360 ad network API reference guide

<div id="api-basics" />

<Accordion title="API basics">

Protect360 ad network API basics:

| Path | `https://hq1.appsflyer.com/api/adnets-data/v1/export/report_topic/app/app_id` |
| --- | --- |
| Method | GET |
| Path parameters (mandatory) | <ul><li>`app_id`:<ul><li>The app identifier, as found in the AppsFlyer dashboard. Insert it precisely as it displays in the dashboard.</li><li>Make sure to prefix iOS apps with **id.**</li></ul></li><li>`report_topic`:</li></ul> |
| Accepted content types | `application/json` |
| Authorization | <ul><li>Bearer token in the request header.</li><li>![AppsFlyerAdmin_us-en.png](https://files.readme.io/5708713f5adc7560748b16d2df4a439163e1310fc7d32f2e5ca786d176cbc8d3-44928678665617.png)Ask the admin to get the V2.0 token from the <Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">tokens</Anchor> page. This token is about 700 characters in length.</li></ul> |
| Rate limitation | <Anchor target="_blank" href="/marketers/docs/report-generation-quotas-rate-limitations">Rate limitations</Anchor> |
| Date range limitation | <ul><li>Earliest date supported: 90 days before the current data</li><li>31 days out of the previous 90 days</li></ul> |
| Row limitations | 200K rows |
| Report characteristics | <ul><li>Timezone: UTC</li><li>Currency: USD</li></ul> |

</Accordion>

<div id="api-parameters" />

<Accordion title="API parameters">

Protect360 API parameters:

| Parameter | Description | Format | Mandatory |
| --- | --- | --- | --- |
| app\_id | App ID as it displays in AppsFlyer | String | Yes |
| from | Start of the date range:<ul><li>For installs, this is the install date.</li><li>For in-app events, this is the date of the event.</li></ul> | YYYY-MM-DD | Yes |
| to | End of the date range:<ul><li>For installs, this is the install date.</li><li>For in-app events, this is the date of the event.</li></ul> | YYYY-MM-DD | Yes |
| event\_name | [Optional for Post-attribution in-app events fraud]<br /><br />Filter events by in-app event. Limit the report to specific events. One or more events can be included.<br /><br />Example usage: `&event_name=af_purchase,af_login` | String | No |
| detect-from | [Optional for Post-attribution installs]<br /><br />Start of the fraud detection date range. (Default is from.) | YYYY-MM-DD | No |
| detect-to | [Optional for Post-attribution installs]<br /><br />End of the fraud detection date range. (Default is to.) | YYYY-MM-DD | No |

</Accordion>

<div id="protect360-api-http-return-codes" />

<Accordion title="Protect360 API HTTP return codes">

Error codes and solutions:

| Status | Code | Symptom/message | Solution |
| --- | --- | --- | --- |
| OK | 200 | Empty CSV file | `addtional_fields`used more than once in the URI |
| OK | 200 | Empty CSV file | Ensure that both from and to dates have the format yyyy-mm-dd |
| OK | 200 | AppsFlyer HTML login page returns | There is no token in the Bearer token header |
| Bad request | 400 | Bad request | <ul><li>Date range limitation.<ul><li>The earliest date allowed is 90 days prior to the current day</li><li>Period can't exceed 60 days for installs and 90 days for in-app reports</li></ul></li></ul> |
| Unauthorized | 401 | Unauthorized | A token was found, but it is not valid. Check that you have the current V2.0 token for your account. Ask the admin to retrieve the current token from the dashboard. |
| Not found | 404 |  | <ul><li>The endpoint specified is incorrect</li><li>Ensure that the app ID is correct</li><li>You are not authorized to access the app</li></ul> |

</Accordion>

<div id="impression-capping" />

## Impression capping

If an ad network has extremely high rates of impression fraud, Protect360 blocks the ad network’s impressions for a 24-hour cycle. This means that any impressions that occur after the threshold is reached are not recorded by AppsFlyer, nor are they eligible for attribution. The blocked impressions do appear in the Protect360 dashboard and reports.

The AppsFlyer fraud protection algorithm takes into account various parameters when detecting this fraud, including volume of impressions, CVR, detected fraud rate, normal fluctuations in activity, industry and geographic benchmarks, and proprietary parameters. The algorithm is dynamic and updated on an hourly basis, to take into consideration changing trends.

**Repeatedly triggering impression flooding thresholds may result in the permanent removal of the partner integration from the AppsFlyer platform.**

Impression capping thresholds:

* Apply to all ad networks equally. Meaning, there is no ad network for which extremely high rates of impression fraud would not lead to capping.
* Are at the app/ad network level. Meaning, the analysis of fraud takes into account all the ad network’s campaigns on an app, And the block affects reporting and attribution for all the ad network’s campaigns on an app (whether or not the account has Protect360).
* Are reset after a 24-hour cycle and blocks apply until the end of the cycle. Details on when the cycle starts and ends are kept private by AppsFlyer.
* Cannot be changed or stopped. Protect360 is finely tuned and accurate in its fraud detection and the algorithm can’t be manually adjusted or turned off.
* Can be avoided by stopping campaigns and publishers with anomalous activity.

<div id="faq" />

<Accordion title="FAQ">

Impressions capping FAQ:

| **Q: What is the network threshold?**<br /><br />**A**: Details of the capping mechanism are protected to prevent attempts at circumvention. That said, the threshold is only reached if there is an extreme volume of impressions fired, beyond the possibility of human behavior. Looking at the day’s impression, install volumes will give you a clear idea of whether there is a flood issue stemming from one or more publishers. |
| --- |
| **Q: How can a network get unblocked?**<br /><br />**A**: A network can avoid the threshold by stopping campaigns and publishers with anomalous activity. Once blocked, the network needs to wait until the end of the 24-hour cycle to resume being recorded. |
| **Q: Does the block affect AppsFlyer customers without Protect360?**<br /><br />**A**: Yes, capping will affect regardless of whether or not a customer has Protect360. The capping mechanism protects all customers from impression abuse. |
| **Q: This is not fraud. The network is working with cheap sources and sometimes their quality is low.**<br /><br />**A**: Poor performance at a normal scale from non-suspicious sources does not trigger capping. The algorithm identifies performance that cannot possibly be human. |
| **Q: This stops us from scaling campaigns and we don't want these impressions to be blocked.**<br /><br />**A**: The AppsFlyer fraud protection algorithm protects customers from extreme and blatant instances of flooding. It doesn't impact scaling ability, as it addresses non-human generated impressions, where the vast majority of blocks only cause liabilities. If you have concerns, please contact AppsFlyer to address your issues. |
| **Q: This is not fraud. Maybe AppsFlyer has issues dealing with the volume of impressions?**<br /><br />**A**: We don't have any issues handling volume. We support some of the world’s largest-scale advertisers and process billions of real-time data points each day, including enormous numbers of legitimate impressions. As part of our commitment to support high-scale growth with rich and accurate data, we act in our customers’ best interests and block clear instances of impression flooding. |
| **Q: What can we do if we expect a significant increase in traffic and impression volume (for example, due to new campaigns)? What can be done to avoid being blocked?**<br /><br />**A: The algorithm is dynamic and updated on an hourly basis, to take into consideration different trends. It is sophisticated enough to handle spikes and is not triggered by normal activity fluctuations, including sudden and significant increases in volume. That said, partners can use their impression data and reports to identify suspicious sources and stop those campaigns.** |
| **Q: How can we check for problematic traffic and improve campaign performance?**<br /><br />**A: Partners can use their impression data and reports to identify suspicious sources and stop those campaigns. Partners can also see blocked impression data in the Protect360/ProtectLITE dashboard under the dedicated columns, as long as they have received the required permission from the advertiser to view fraud data in the dashboard.** |

</Accordion>

<div id="click-signing" />

### Click signing

Ad networks can add HMAC-SHA256 <Anchor target="_blank" href="/partners/docs/click-signing-for-ad-networks">signatures to their clicks</Anchor>.

The signatures enable AppsFlyer to validate the clicks and make sure that the click information hasn't been manipulated by fraudsters.

* Validated clicks are recorded, and attributed to the ad network
* Invalidated clicks are rejected and:
  * Are aggregated in Protect360 reports made available to the ad network (not advertisers).
  * Do not impact the conversion rate of the ad network

<div data-zendesk-anchors="h_01HGSXTKYQB4Q1QQX4ZQS60AAJ=overview h_01HGSXTKYQN42EEMPSZMWVAMWD=note h_01HGSXTKYQPQP72R2VJB68ZDRZ=dashboard-view rawdata-reports=raw-data-reports h_01HGSXTKYQWRZECN905RGSEQ42=raw-data-reports h_01HGSXTKYQ9388SCQTT2MX59Q9=protect360-ad-network-reporting-api h_01HGSXTKYQXZN2DMNZ09HE7355=protect360-api-reports h_01HGSXTKYQ913MF0G38B23NYBG=procedure-for-ad-networks-to-get-protect360-reports-by-download h_01HGSXTKYQX3VN5NRMNQWW4AE4=curl-examples h_01HGSXTKYQQBJTM4ZMMQZ0VZNH=installs-blocked_installs_report h_01HGSXTKYQ5KTCD7K63DSVS6E2=postattribution-installs-detection h_01HGSXTKYQ6MA96W8E6R2SXBS5=inapp-event-blocked_in_app_events_report h_01HGSXTKYQMMC0WNWP56Q9J0ZS=postattribution-inapp-events-fraud-fraud_post_inapps h_01HGSXTKYQEG0JXJHS7QBAEBCA=clicks-blockedclicks_report h_01HGSXTKYQJRE1Y9C5RSCANWT2=protect360-ad-network-api-reference-guide h_01HGSXTKYQE24FAPYHHMFP0B3X=api-basics h_01HGSXTKYRFSZRPHNPDHNREDH2=api-parameters h_01HGSXTKYRGSQ230NVN06SP6DG=protect360-api-http-return-codes impression-and-click-capping=impression-capping h_01HGSXTKYRN6TP3KDYX5YZJV7N=impression-capping h_01HGSXTKYR8BK5A2J6TJECMKZA=faq h_01HGSXTKYR915V6E4NWGWR61PG=click-signing" />
