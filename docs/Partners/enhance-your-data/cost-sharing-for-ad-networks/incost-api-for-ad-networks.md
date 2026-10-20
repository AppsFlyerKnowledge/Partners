---
title: InCost API for ad networks
excerpt: >-
  InCost API, part of AppsFlyer ROI360, lets ad networks programmatically send
  advertising cost data to AppsFlyer. Doing so provides advertisers with
  aggregate cost data and lets them understand the true impact of your network.
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Marketers
    - ROI360
    - Ad Networks
  created_at: '2020-04-26T19:13:47Z'
  edited_at: '2026-09-15T08:39:11Z'
  id: 360007714957
  locale: en-us
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360007714957-InCost-API-for-ad-networks
---
## About InCost API

InCost API is the optimal solution for ad networks to send cost data to AppsFlyer. Ad network partners send detailed advertising cost data to AppsFlyer using the API. AppsFlyer ingests and processes the data, and makes it available to advertisers and partners via dashboards and reports.

#### Benefits

* Help your customers understand the true impact of your network with frictionless cost reporting. Without cost data, your customers are missing a crucial piece of the measurement puzzle and can't accurately measure ROAS. As such, they may mistakenly invest in other media sources, negatively impacting your bottom line.
* Prove your ROI with a solution that guarantees accurate, complete, and real-time cost measurement.
* InCost API is quick and simple to deploy, and the impact is almost immediate. You also get complete control over how and when you send the data, including the ability to send cost data for up to 90 days back.
* InCost API supports all campaign pricing models; not just CPI (which is the only model available when sending cost by click).
* Stand out in the AppsFlyer Partner Marketplace with a “Cost” badge that indicates this is a feature you support.

## Implementing InCost API

**Prerequisites**: For InCost API eligibility, your ad network requires:

* That 90% of campaigns contain the Campaign ID in attribution.
* The ability to send data at least 6 times per day for increased data freshness. The specific times are up to the ad network.
* [If the ad network updates data retroactively] The ability to send data for the last 7 days every time, for increased data completion.

**To implement InCost API and start sending cost data to AppsFlyer**:

* Follow the steps in the following table.

| Step # | Action |
| --- | --- |
| 1 | Apply for InCost:<ol><li>In AppsFlyer, from the top menu, select **Help** > **Contact our team**.<br />The Partner assistant widget opens.</li><li>Select **Enabling cost measurement** and submit your information.<br />Once submitted, a ticket opens and an AppsFlyer partner solution engineer will contact you.</li></ol> |
| 2 | Make sure campaign hierarchies (campaign ID, and optionally, adset ID and ad ID) are included on your attribution links for more than 90% of your traffic. |
| 3 | Get the AppsFlyer [API token](/marketers/docs/managing-appsflyer-tokens) from the AppsFlyer dashboard. |
| 4 | Give the API token to your developer to use in the API authorization header and ask them to follow [their instructions](https://dev.appsflyer.com/hc/reference/incost-overview) to implement the 3 API methods:<ol><li>[Get app list](https://dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get).</li><li>[InCost upload](https://dev.appsflyer.com/hc/reference/incost-uploader-post): Tell the developer what [fields to populate the JSON](#fields-for-incost-upload-json) with:<ul><li>Mandatory fields must be populated. Meaning, don't send empty fields.</li><li>Media source is restricted to media sources associated with (registered under) your ad network account. Get the list from your partner development manager.</li><li>Take into consideration the app [timezone](/marketers/docs/about-data-freshness-and-timezone-support#app-specific-time-zone) (as reported via the Get app permission list API) to align cost data dates with that of the app.</li><li>If there are fields that are not part of your campaign cost reporting hierarchy, don’t include them. For example, adset ID, asset name, ad ID, ad name.</li></ul></li><li>[Get job status](https://dev.appsflyer.com/hc/reference/incost-jobstatus-get).</li></ol> |
| 5 | Test the integration:<ol><li>In the ticket thread (from step 1), notify AppsFlyer that the API implementation is complete and get permissions for the following apps which can be used to test the API without using real data:<ul><li>com.cost.app</li><li>id888123456</li></ul></li><li>In AppsFlyer, from the side menu, select **Collaborate** > **Partner Marketplace**, and select the partner.</li><li>Click **Set up integration**.</li><li>Select 1 of the test apps.</li><li>Open the integrated partner **Cost** tab.</li><li>Turn on the **Get Cost Data** toggle.</li><li>Click **Save Cost**.</li><li>Click **Test Connection.**<br />The API is active.</li></ol> |
| 6 | In the ticket thread (from step 1), confirm with AppsFlyer that your integration is operational. |
| 7 | Make sure your advertisers enable [get cost data](/marketers/docs/set-up-an-integrated-partner#cost-tab) in the cost tab of their AppsFlyer integrated partner page. Then they'll begin to receive cost data. |

> 📘 **Note**
>
> Best practice: only resend data for a given date if its cost has changed. You can send the last 7 days on every call, but you don't need to resend unchanged records.

### Fields for InCost Upload JSON

<table><thead><tr><th>Field</th><th>Mandatory</th><th>Remarks</th></tr></thead><tbody><tr><td>date</td><td><span>Yes</span></td><td><ul><li><span>Spend date</span></li><li><span>Format: </span><code><span>YYYY-MM-DD</span></code></li><li><span>Example:</span><code><span>2019-12-30</span></code></li></ul></td></tr><tr><td>app_id</td><td>Yes</td><td><ul><li>The app ID as it appears in the AppsFlyer platform</li><li><span>Format: String up to 250 characters</span></li><li><span>Example: Android:</span><code><span>com.app.name</span></code><span>, </span>iOS: <code>id123456789</code></li></ul></td></tr><tr><td><span>media_source</span></td><td><span>Yes</span></td><td><ul><li><span>Network name (ID) displaying the ad associated with your ad network partner account in AppsFlyer</span></li><li><span>Format: String 50 characters</span></li><li><span>Example: </span><code><span>network_int</span></code></li></ul></td></tr><tr><td><span>af_prt</span></td><td><span>No\*</span></td><td><ul><li>Required for agency attribution and cost data. </li><li>Agency name as it displays on the attribution link and is associated with the agency account in AppsFlyer. </li><li>Format: String 50 characters </li><li>Example: <code>agencya</code> </li><li>If cost data is resent for the same dates and <code>af_prt</code> is included in a subsequent API call when it was absent in the original, resulting in duplicated cost data.</li></ul></td></tr><tr><td><span>campaign_id</span></td><td><span>Yes</span></td><td><ul><li><span>Must be identical to the </span><code><span>af_c_id</span></code><span> param sent on the attribution link</span></li><li><span>Empty string not permitted</span></li><li><span>Format: String 24 characters</span></li><li><span>Example: </span><code><span>123abc</span></code><span></span></li></ul></td></tr><tr><td><span>campaign_name</span></td><td><span>Yes</span></td><td><ul><li><span>Format: String 100 characters</span></li><li><span>Example: </span><code><span>my_campaign123</span></code></li></ul></td></tr><tr><td><span>adset_id</span></td><td>No\*</td><td><ul><li><span>Required if you send </span><code><span>adset_name</span></code></li><li><span>Must be identical to the </span><code><span>af_adset_id</span></code><span> param sent on the attribution link</span></li><li><span>If your cost reporting does not support </span><code><span>adset_id</span></code><span>, never send it</span></li><li><span>Format: String 24 characters</span></li><li><span>Example: </span><code><span>123A</span></code></li></ul></td></tr><tr><td><span>adset_name</span></td><td><span>No</span></td><td><ul><li><span>If you send this field, you must also send </span><code><span>adset_id</span></code></li><li><span>Format: String 100 characters</span></li><li><span>Example:</span><code><span>my_adset_name</span></code></li></ul></td></tr><tr><td><span>ad_id</span></td><td>No\*</td><td><ul><li>Required if you send <code><span>ad_name</span></code>.</li><li><span>This field must be identical to the </span><code><span>af_ad_id</span></code><span> param sent on the attribution link</span></li><li><span>If your cost reporting does not support </span><code><span>adset_id</span></code><span>, never send it</span></li><li><span>Format: String 24 characters</span></li><li>Example:<code>123AB</code></li></ul></td></tr><tr><td><span>site_id</span></td><td>No</td><td><ul><li>Unique ID that identifies the publisher that displays the ad.</li><li>Format: String 24 characters.</li></ul></td></tr><tr><td><span>ad_name</span></td><td><span>No</span></td><td><ul><li><span>If you send this field, you must also send </span><code><span>ad_id</span></code></li><li><span>Format: String 100 characters</span></li><li>Example:<code>Ad-name</code></li></ul></td></tr><tr><td><span>geo</span></td><td><span>No</span></td><td><ul><li><span>The country you recorded as associated with the cost</span></li><li><span>Where possible, this should represent the country where the ad was displayed</span></li><li><span>Format: ISO 3166 2-character country code</span></li><li><span>Example:</span><code><span>US, CN, ZA</span></code></li></ul></td></tr><tr><td>currency</td><td><span>Yes</span></td><td><ul><li><span>Spend currency type</span></li><li><span>Format: ISO 4217 3-character currency code</span></li><li><span>Example:</span> <code><span>USD, EUR, ZAR</span></code></li></ul></td></tr><tr><td>spend</td><td>Yes</td><td><ul><li>Spend amount using the specified currency </li><li>Five digits allowed after the decimal point</li><li>The value 0 (zero) is permitted</li><li>Negative values are NOT permitted</li><li>Don't send <code>,</code> delimiters</li><li>Don't send values in quotation marks. </li><li>Format: Decimal number</li><li>Example values: <code>1</code> <code>1.2</code> <code>1234.20</code></li></ul></td></tr><tr><td>channel</td><td>No</td><td><ul><li>Must be identical to the <code><span>af_channel</span></code><em> </em>param sent on the attribution link</li><li>Format: String 20 chars</li><li>Example:<code>my_channel</code></li></ul></td></tr><tr><td>keywords</td><td>No</td><td><ul><li>Format: String 100 chars</li><li>Example:<code>abc app</code></li></ul></td></tr><tr><td>reported_clicks</td><td>No</td><td><ul><li>Number of clicks reported by the network for this record.</li><li>Format: Non-negative integer.</li><li>Example: <code>150</code></li><li>Optional. If empty or omitted, reported as 0.</li><li>Decimal or negative values are rejected (error 422: <code>Reported clicks can be positive integer</code>).</li></ul></td></tr><tr><td>reported_impressions</td><td>No</td><td><ul><li>Number of impressions reported by the network for this record.</li><li>Format: Non-negative integer.</li><li>Example: <code>1000</code></li><li>Optional. If empty or omitted, reported as 0.</li><li>Decimal or negative values are rejected (error 422: <code>Reported impression can be positive integer</code>).</li></ul></td></tr><tr><td colspan="3">\* See the remarks column, as in some cases you must send this field.</td></tr></tbody></table>

<div data-zendesk-anchors="incost-api=about-incost-api h_01HE0WCBD9GD66KB1QGQ9MEXBJ=about-incost-api h_01HKVW85AYFG91PGYE5BDQVJNR=benefits h_01HKVWSWTWETTES5ZTNZ05X9VA=implementing-incost-api h_01M2J3GBMFJW7XT08MK5JR3D3Y=note h_01HM8VCV81GQ6XQ4NA1EDCZ4K7=fields-for-incost-upload-json" />
