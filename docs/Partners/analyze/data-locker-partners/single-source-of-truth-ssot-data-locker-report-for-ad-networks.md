---
title: Single Source of Truth (SSOT) Data Locker report for ad networks
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2024-07-31T19:51:34Z'
  edited_at: '2025-04-17T08:51:20Z'
  id: 27168206416017
  locale: en-us
  section: Data Locker
  section_id: 6551591547409
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/27168206416017-Single-Source-of-Truth-SSOT-Data-Locker-report-for-ad-networks
---
**At a glance:** The Single Source of Truth (SSOT) report in Data Locker offers a unified and accurate overview of app campaign performances by merging data from various attribution methods, such as ID matching and SKAN.  It provides a way to load data into your BI systems to get the highest accuracy of data.

> 📘 **Note**
>
> * Before we start sharing the data with you, the advertisers must grant [permissions](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) in the dashboard
> * The SSOT Data Locker report contains LTV-based data, not activity-based data. This means the data reflects users’ lifetime value across all touchpoints, rather than their in-app or event activity

## What is Data Locker

Data Locker is a secure solution that delivers data directly to main cloud platforms, such as AWS, GCS, and Snowflake. This allows you to easily integrate and consume data into your internal BI systems for comprehensive analysis and reporting. <Anchor target="_blank" href="/partners/docs/data-locker-for-partners">Learn more</Anchor>.

## What is Single Source of Truth (SSOT)

The Single Source of Truth (SSOT) solution aims to solve data fragmentation issues by offering a unified and accurate overview of app campaign performances by merging data from various attribution methods, such as ID matching and SKAN. <Anchor target="_blank" href="/marketers/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Learn more</Anchor>.

## Benefits of SSOT reports in Data Locker

The Single Source of Truth report provides the same visibility that marketers use to analyze and measure performance.

* **Get an accurate, complete attribution view:** SSOT handles the logic of merging data from different attribution methods, effectively preventing double-counting installs that were attributed by multiple attribution methods. This ensures the data is accurate and reflective of true user behavior and attribution.
* **Load data into your BI systems:** SSOT provides an efficient and accurate way to load the aggregated data into your internal BI systems. This includes attributions, in-app events, and revenue data, covering all dimensions and metrics.

<div id="setting-up-data-locker" />

<Accordion title="Setting up Data Locker">

Use this procedure to set up Data Locker. Changes to settings take effect within 3 hours.

**Prerequisite:**

Complete one or more of the following storage procedures:

* <Anchor target="_blank" href="/marketers/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor> bucket
* <Anchor target="_blank" href="/marketers/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor> bucket
* [Beta] <Anchor target="_blank" href="/marketers/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor> bucket
* <Anchor target="_blank" href="/marketers/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor> data warehouse

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/9f23f475e562992154e0d64ac0775a3b4c8029500e17a00aaf2cb5a4fc4bd9ac-31262593759377.png) To set up Data Locker:**

1. Log in to your <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">AppsFlyer partner dashboard.</Anchor>
2. Go to:
   * **Advertisers:Report**>**Data Locker**.
   * **Marketing partners**: Click the **account menu** > **Data Locker**.
3. Follow the <Anchor target="_blank" href="/marketers/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">Data Locker setup instructions</Anchor> steps 3-16.

</Accordion>

<div id="permissions" />

<Accordion title="Permissions">

Ad networks appointed (activated) by agencies: The agency can't grant permission. The agency must ask the advertiser to grant the permissions for them.

**To allow the ad network to get Single Source of Truth or SSOT data:**

1. In AppsFlyer, from the side menu, select **Collaborate** > **Integrated partners**.
2. Search for the partner and select it.
3. Click **Set up integration**. You’re directed to the integration setup page.
4. Verify that **Activate partner**is on. If not, data isn't shared.
5. Go to the **Permissions** tab.
6. Turn on the following ad network permissions:
   * **Access aggregate conversions data**.
   * **Access aggregate in-app events data**.
   * **Access aggregate revenue data**.
7. Click **Save Permissions**.
8. Notify the ad network that you have granted the permissions.
9. If you have multiple apps, repeat the procedure for each app integrated with the partner.

</Accordion>

<div id="ssot-report-facts" />

<Accordion title="SSOT report facts">

| Name | Description |
| --- | --- |
| Reports available | The following reports are available:<ul><li>User acquisition: attributes conversions to user acquisition channels. This includes post-install activity occurring during re-engagement windows.</li><li>Retargeting: attributes conversions to retargeting channels for events occurring:<ul><li>As a result of re-attributions</li><li>During a re-engagement window</li></ul></li><li>Unified: attributes conversions to the last touch channel, according to the AppsFlyer <Anchor target="_blank" href="/marketers/docs/resolve-retargeting-double-attribution">double attribution</Anchor> rules. This means that post-install activity occurring during re-engagements displays under the retargeting media source and not under the UA media source.</li></ul> |
| Reporting period | The report provides cohort metrics up to 7 days post-install. |
| Directory structure | The directory structure is organized by install date. Each install date folder includes multiple versions created daily. Each version reflects the updated cumulative data for this install date. This means you should only process the latest available report version. <Anchor target="_blank" href="/marketers/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#directory-structure">Learn more</Anchor> |
| Report structure | The schema of the report (the dimensions and metrics included) is fixed and can't be modified. |
| Timezone | UTC |
| Data freshness | <ul><li>Daily.</li><li>Metrics are calculated using data available at midnight UTC, which is the end of the day.</li><li>SLA: New reports are available in Data Locker by 16:00 UTC. A new version is created for the last 15 install dates each day. <Anchor target="_blank" href="/marketers/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#report-folder-hierarchy">See more</Anchor></li></ul> |

</Accordion>

## Report structure

The report is comprised of dimensions and metrics.

The metrics covers data of attributions, revenue, and the unique users performing an event.

<div id="field-formats" />

<Accordion title="Field formats">

<Table>
  <thead>
    <tr>
      <th>
        Format name
      </th>
      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        String [n]
      </td>
      <td>
        The maximum length of the string. We don't usually enforce field length limitations on receipt of the data, but data may be truncated thereafter.
      </td>
    </tr>
    <tr>
      <td>
        Time string
      </td>
      <td>
        Strings have the format,

        ```
        yyyy-mm-dd hh:mm:ss.
        ```

        For example,

        ```
        2019-09-17 00:09:25
        ```
      </td>
    </tr>
    <tr>
      <td>
        Enum [n]
      </td>
      <td>
        Enum fields can only contain specific values. For example, selected\_currency has 3 characters and can contain only currency codes as specified.
      </td>
    </tr>
    <tr>
      <td>
        Timestamp
      </td>
      <td>
        10-digit UNIX timestamp. Example:  
        August 4, 2020, 07:25 UTC translates to

        ```
         "timestamp": "1596525944"
        ```
      </td>
    </tr>
    <tr>
      <td>
        Boolean
      </td>
      <td>
        The value of the field can be either *TRUE* or *FALSE*
      </td>
    </tr>
    <tr>
      <td>
        Integer
      </td>
      <td>
        Integer
      </td>
    </tr>
    <tr>
      <td>
        Float
      </td>
      <td>
        Real floating number that can have a decimal point and values after the decimal point.
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="dimensions" />

<Accordion title="Dimensions">

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Field name</th><th>Description</th><th>Format</th></tr></thead><tbody><tr><td>af_ad_id</td><td>Ad identifier. Campaign hierarchy.</td><td>string</td></tr><tr><td>af_ad</td><td>Ad name.</td><td>string</td></tr><tr><td>af_adset_id</td><td>Ad-set identifier. Campaign hierarchy.</td><td>string</td></tr><tr><td>af_adset</td><td>Ad-set name.</td><td>string</td></tr><tr><td>app_id</td><td>App ID (advertiser app) with prefix ID.</td><td>string</td></tr><tr><td>attribution_method</td><td>The mechanism used for attributing the event. Examples of such mechanisms include AppsFlyer methods, SKAdNetwork (SKAN), and organic.</td><td>string</td></tr><tr><td>attributed_touch_type</td><td>Possible values: click impression, null.</td><td>string</td></tr><tr><td>campaign</td><td>Campaign name reported by the ad network to AppsFlyer.</td><td>string</td></tr><tr><td>af_c_id</td><td>Campaign identifier.</td><td>string</td></tr><tr><td>days_post_attribution</td><td>The number of days elapsed since the conversion date (not the specific conversion timestamp).<br/>Tip! Use this to calculate retention and KPI days.</td><td>int</td></tr><tr><td>event_name</td><td>Identifies the event. Some event names have a specific meaning while others relate to in-app events set by the advertiser in the app.<figure><table><thead><tr><th>event_name</th><th>What did the user do</th></tr></thead><tbody><tr><td>af_conversion</td><td>User converted. Use conversion_type to identify if it is an install, re-download, re-attribution. or re-engagement.</td></tr><tr><td>Advertiser defined in-app event</td><td>Performed an in-app event in the app</td></tr></tbody></table></figure></td><td>string</td></tr><tr><td>geo</td><td>The ISO country code. Derived from the user IP address in AppsFlyer classic attribution methods, while in SKAN the data is either enriched from ad-networks or modeled.</td><td>string</td></tr><tr><td>install_date</td><td><p>SKAN: Estimated by AppsFlyer based on the postback arrival time.</p><p>AF:</p><ul><li>UA: First launch after install</li><li>Retargeting: First launch after re-engagement/re-attribution</li></ul></td><td>string</td></tr><tr><td>is_primary_attribution</td><td><p>UA: True</p><p>Retargeting: During a re-engagement window, we attribute to both the original media source (before the re-engagement) and to the re-engagement media source. While the event is within the re-engagement window. The original media source will be FALSE (not primary attribution). The re-engagement media source will be TRUE.</p></td><td>bool</td></tr><tr><td>media_source</td><td>Ad network attributed to an event.</td><td>string</td></tr><tr><td>selected_currency</td><td>3-letter currency code (USD, EUR) set by you in the app settings. Format ISO-4217. This is the same currency used to display revenue in SSOT user interface.</td><td>string</td></tr><tr><td>conversion_type</td><td>Possible values:<br/>Install: User downloads and opens an app for the first time.<br/>Re-attribution: User reinstalls and is attributed to a new campaign.<br/>Re-download (SKAN): User installs the app again after uninstalling.<br/>Re-engagement: Re-engagement: User reopens the app after interacting with a retargeting ad.</td><td>string</td></tr></tbody></table>

</Accordion>

<div id="metrics" />

<Accordion title="Metrics">

| chosen dl name | Description | Format |
| --- | --- | --- |
| revenue\_selected\_currency | The cumulative revenue amount in the selected currency. Maximum of two places after the decimal point.  <br />Example: For event\_name=purchase with days\_post\_attribution=2, the value reflects the total revenue from purchase events within two days post-install (not only on the second day). | double |
| revenue\_usd | The cumulative revenue amount in USD.  <br />Example: For event\_name=purchase with days\_post\_attribution=2, the value reflects the total revenue from purchase events within two days post-install (not only on the second day). | double |
| skan\_duplicates | Installs simultaneously attributed by SKAN and other AF methods are then removed to prevent double counting in SSOT data. | long |
| uninstalls\_count | Number of app users installing the app who subsequently uninstall (delete) the app (relevant for User Acquisition only) | long |
| unique\_users | The number of distinct users performing an event. Values are cumulative.  <br />Example: For event\_name=purchase with days\_post\_attribution=2, the value reflects unique users who made purchases within two days post-install (not only on the second day). | int |

</Accordion>

<div id="modeled-data" />

<Accordion title="Modeled data">

AppsFlyer models data that basic SKAdNetwork reporting cannot provide.

* Null Conversion Values (CV): In SKAN, Apple may replace actual data with a "Null" value to maintain user privacy. To ensure no data is omitted, these null values are modeled in SSOT. <Anchor target="_blank" href="/marketers/docs/skan-modeled-data#null-conversion-values">Learn more</Anchor>.
* Longer Post-Install Metrics: SKAN's data granularity for post-install periods beyond the first two days is limited, which may lead to inaccuracies. To maintain high data quality, we model revenue and unique in-app event users for days\_post\_attribution greater than 2. <Anchor target="_blank" href="/marketers/docs/skan-modeled-data#revenue-ltv">Learn more</Anchor>.

Geo Data: SKAN limits data granularity, often making geo data unavailable. In such cases, we model the data to enable efficient performance analysis. <Anchor target="_blank" href="/marketers/docs/skan-modeled-data#geo">Learn more</Anchor>.

</Accordion>

<div id="partial-data" />

<Accordion title="Partial data">

When analyzing recent install days, metrics for extended post-install periods (e.g., 7 days) might not be fully matured. In such cases, the metrics will still be available but will reflect partial data.

Some rules of thumb:

* The report shows any available data as soon as it is available.
* After 5 days, metrics for two days post-install are completed*.
* After 7 days, metrics for seven days post-install are completed. Up to 15 days post-install, the model might refine this value.

Reasons for Partial Data:

* Data maturity: When the time since the install date is shorter than the days being analyzed, the data is still accumulating and not yet complete.
* SKAN delays: SKAN data is received with a random delay. For example, post-install activity for the first two days can be received up to 96 hours (4 days) after installation.
* Modeled data timing: SKAN data for periods greater than 2 days post-install is modeled. Our models generate the first estimated value after 7 days. During this period (days 2 to 7), data from AppsFlyer's classic attribution methods is available, while SKAN modeled data isn’t.

Examples (assuming an install date of January 1st):

* On January 2nd: SKAN data has yet to be received. Data for 2 days post-install will equal data under 7 days post-install, and both are partial, consisting of data from AppsFlyer's classic attribution methods.
* On January 3rd: SKAN data is partially received. Data for 2 days post-install will still be partial, now partially containing SKAN data. Data for 7 days post-install will not include any modeled SKAN data yet (the first modeled value is available after 7 days from installation). Therefore, between 2 to 7 days post-install, we might see a lower value for 7 days post-install relative to 2 days post-install.
* On January 6th: SKAN data for the first two days post-install was fully received, including postbacks with the maximum possible delay. Metrics for two days post-installs are completed. At this point, metrics for 7 days post-installs aren’t completed yet.
* On January 8th: SKAN modeled data for 7 days post-installs is completed. Our model will keep refining the value up to January 16th.

</Accordion>

## Directory structure

<div id="report-folder-hierarchy" />

<Accordion title="Report folder hierarchy">

* The primary folders are organized by the report type. Possible values: ‘ssot\_unified’, ‘ssot\_retargeting’, and ‘ssot\_user\_acquisition’.
* Within these folders, sub-folders are organized by the install date.

**Versioning**

* Each install date folder contains multiple versions, created daily.
* Each version reflects the updated cumulative data for that install date.
* Reports will include all available data for the install date. For example, on April 18, the latest version for each install date contains all data up to that point for April 18.
* Tip: Always process the latest available report version to ensure accuracy.

Each install date is limited to up to 15 versions. After 15 days, all metrics are fully fixed and completed. <Anchor target="_blank" href="/marketers/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Learn more</Anchor>.

</Accordion>

<div id="directory-and-filename-structure" />

<Accordion title="Directory and filename structure">

The path to the report consists of the following format:

`<bucket-name>`/t=`<ssot_unified OR ssot_retargeting OR ssot_user_acquisition>`/install\_date=`<yyyy-mm-dd>`/version=`<unix timestamp>`/`<parquet file number>`

Example folder hierarchy in advertiser bucket:

```
bucket
|
└── t=ssot_unified
    |
    ├── install_date=2024-05-05
    |   |
    |   └── version=1714890235
    |   |    |
    |   |    ├── part-00000-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    |
    |   |    ├── part-00001-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    │
    |   |    └── part-00002-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |
    |   |
    |   └── version=1714890286
    |        |
    |        ├── part-00000-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        |
    |        ├── part-00001-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        │
    |        └── part-00002-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |   |
    .   . 
    .   .
```

Legend:

* t: Report topic (type).
* install\_date: The installation date of the app. It means that post-install activity will appear based on the install date when the user downloaded the app, not the day the user action occurred.
* version: Unix timestamp indicating when the version was created.

</Accordion>

## BI developer considerations

**Scope of data in the report:**

The reports contain data on user acquisition installs, retargeting re-attributions (re-downloads in SKAN), and re-engagements, along with their related in-app events.

<div id="loading-reports" />

<Accordion title="Loading reports">

You can load unified, user acquisition, and retargeting reports separately or together into your BI system. If you load them together and want to filter views on your own:

* Unified reports: Use is\_primary\_attribution=true or null field.
* User acquisition reports: Use conversion\_type=Install.
* Retargeting reports: Use conversion\_type=re-engagement or re-attribution.
* Unified View: If you use the unified view in your data loading process, you can split the data between campaign types:

* Use conversion\_type=install, re-engagement, or re-attribution (re-downloads in SKAN).
* Refer to "Double attribution of retargeting events" for more details

</Accordion>

<div id="days-postattribution" />

<Accordion title="Days post-attribution">

> 🚧 **Important!**
>
> The report includes a dimension, days\_post\_attribution, which associates revenue and unique user data with the specific number of days post-install

* For attributions (installs, re-engagements, etc.), the value is 0.
* For revenue and in-app events, the data is categorized into predefined cohorts, currently limited to “2” days and “7” days post-install.

**To accurately analyze in-app events and revenue, you should apply a filter for the days\_post\_attribution dimension.** See the example query below.

An example of a common mistake is to apply a simplified logic that sums the revenue column for a specific set of dimensions. This approach results in incorrect numbers because some revenue data is counted twice (once for days\_post\_install=2 and again for days\_post\_install=7). This example is also relevant when analyzing unique users for specific in-app events.

</Accordion>

<div id="considerations" />

<Accordion title="Considerations">

**Tips considerations:**

* Last version: Always query the latest version available for each install date to ensure you are working with the most up-to-date and accurate data for your analysis.
* Revenue calculation: Revenue in USD is calculated using the exchange rate on the event day.
* Analyze attributions: Records where event\_name=af\_conversion reflect attributions (installs, re-attributions (re-downloads in SKAN), and re-engagements). The count of attributions appears under the unique users metric, and the revenue metrics for these fields will be empty. The value under days\_post\_attribution will be 0.
* Dashboard comparison: When comparing installs to the dashboard, sum both re-download and install conversion types, as the dashboard considers both under the install column.
* Analyze in-app events: Records where event\_name does not equal ‘af\_conversion’ reflect in-app events. The count of unique users performing the event appears under the unique users metric, while the revenue generated from these events appears under the revenue metrics.
* Conversion type: Differentiate user acquisition and retargeting conversions using this dimension. Note that an additional break for SKAN data is available (installs vs. re-downloads). When comparing data to the SSOT dashboard, both types are considered as installs.
* Ad Revenue Events: These are included where available.
* Data Segregation: All app data is provided in a single file. Use the App ID field to segregate data per app, or set Data Locker to segregate by app.

</Accordion>

<div id="example-use-cases" />

<Accordion title="Example use cases">

The following are examples of some popular, practical applications of the data that BI developers can extract via Data Locker. Each example is illustrated by an SQL statement and a sample Excel visual.

<div id="calculating-total-attributions-per-campaign" />

<Accordion title="Calculating total attributions per campaign">

In this query, we:

* Sum the total unique attributions per campaign for each install date.
* Filter for conversions with the event name 'af\_conversion' and a specific campaign ID (af\_c\_id).

```sql
SELECT install_date, SUM(unique_users) AS total_attributions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign" />

<Accordion title="Calculating conversions (installs & re-downloads) to compare to the installs in the dashboard per unique campaign">

In this query, we:

* Count conversions distinguishing between new installs and re-downloads per unique campaign and install date.
* Compare installs to the dashboard install metric, which merge conversion types 'install' and 're-download'.

```sql
SELECT install_date, conversion_type, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND conversion_type IN ('install', 're-download')    
-- The dashboard sums both under the install field
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type;
```

</Accordion>

<div id="calculating-retargeting-conversions-per-geo" />

<Accordion title="Calculating retargeting conversions per geo">

In this query, we:

* Count conversions from retargeting campaigns broken down by geographic location.
* By considering types 're-attribution' and 're-engagement' for these conversions.

```sql
SELECT install_date, conversion_type, geo, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type IN ('re-attribution', 're-engagement')    
-- Both types are relevant for re-targeting
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type, geo;
```

</Accordion>

<div id="calculating-installs-by-attribution-method-per-media-source" />

<Accordion title="Calculating installs by attribution method per media source">

In this query, we:

* Count installs by attribution methods (SKAN, AppsFlyer methods, and organic) and break it by media source.
* Filter based on 'af\_conversion' events with a conversion type of 'install'.

```sql
SELECT install_date, attribution_method, media_source, SUM(unique_users)   
AS total_installs
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type = 'install'
    AND app_id = 'YOUR_APP'
GROUP BY install_date, attribution_method, media_source;
```

</Accordion>

<div id="calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset" />

<Accordion title="Calculating cumulative revenue of 7 days post-install for Facebook per ad-set">

In this query, we measure the accumulated revenue within a 7-day period post-install for ads served on Facebook.

```sql
SELECT install_date,
       af_adset,
       SUM(revenue_usd) AS total_revenue_day_7
FROM ssot_unified
WHERE media_source = 'facebook'
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_adset;
```

</Accordion>

<div id="calculating-cumulative-revenue-for-selected-postinstall-periods" />

<Accordion title="Calculating cumulative revenue for selected post-install periods">

In this query, we:

* Calculate cumulative revenue for multiple selected days after installation, breaking out sums for day 2 and day 7.
* Please note that when analyzing installs from the past 7 days, the data for 7 days post-install may be incomplete. <Anchor target="_blank" href="/marketers/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Learn more</Anchor>

```sql
SELECT install_date,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) AS total_revenue_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) AS total_revenue_day7
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source" />

<Accordion title="Calculating revenue from a specific in-app event (purchase) per media source">

In this query, we:

* Measure revenue value from a specific in-app event (like 'af\_purchase') and sum that data by media source.
* Filter selected days post-install to make sure data isn’t double-counted.

```sql
SELECT install_date, media_source, SUM(revenue_usd) AS total_purchase_revenue
FROM ssot_unified
WHERE event_name = 'af_purchase'  -- Change to your specific event
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

<div id="calculating-inapp-event-conversion-rate-for-2-days-postinstalls" />

<Accordion title="Calculating in-app event conversion rate for 2 days post-installs">

In this query, we calculate the conversion rate of a specific in-app event (such as 'af\_complete\_tutorial') in relation to all installations.

```sql
SELECT install_date,
  SUM(IF(days_post_attribution = 2 AND   
event_name = 'af_complete_tutorial', unique_users, 0)) 
  / SUM(IF(event_name = 'af_conversion', unique_users, 0))   
AS conversion_rate_day2_af_tutorial_conversion
FROM ssot_unified
WHERE conversion_type = 'install'    
-- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id" />

<Accordion title="Calculating ARPU for 7 days and 2 days post-install per campaign ID">

In this query, we:

* Calculate the Average Revenue Per User (ARPU) for day 2 and day 7 post-install across campaigns.
* Please note that when analyzing installs from the past 7 days, the data for 7 days post-install may be incomplete. <Anchor target="_blank" href="/marketers/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Learn more</Anchor>

```sql
SELECT install_date,
       af_c_id,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day7
FROM ssot_unified
WHERE conversion_type = 'install'  
       -- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_c_id;
```

</Accordion>

<div id="calculating-amount-of-duplicates-per-media-source-in-this-query" />

<Accordion title="Calculating Amount of Duplicates per Media Source In this query">

In this query, we count the total number of duplicated user attributions by media source and install date, to highlight media channels that may have higher duplication in user attribution.

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
    AND event_name = 'af_conversion'
GROUP BY install_date, media_source;
```

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Traits and limitations">

| Trait | Remark |
| --- | --- |
| Report availability per day | Only installation days where the SSOT toggle was turned on at the end of the day will have an SSOT report for that day |
| Two days post-install metrics | <ul><li>For SKAN 4 in Conversion Studio: Data is for 2 days post-install.</li><li>For SKAN 3 in Conversion Studio: Data is based on the defined SKAN activity window.<br />Example: If the activity window is 24 hours, events occurring within this window (even on Day X+1) are counted.</li></ul> |
| In-app events availability | Available only for events that occurred during the Window 1 period. |
| SKAN redownload breakdown | Available. In the SSOT dashboard, this breakdown is unavailable and both installs and redownloads are included in the installs metric. |
| SKAN Conversion Studio configuration changes | Changing the SKAN Conversion Studio configuration may cause inaccuracies in SSOT data for approximately 96 hours, as postbacks from installs encoded with the previous schema still arrive. |
| Timezone | App-specific timezone is not available. |
| Organic data | <ul><li>Available for 7 days post-install metrics.</li></ul> |
| Days post-conversion (install, re-attribution, re-engagement) data | Limited to 7 days post-conversion |
| Agency transparency | Supported |
| Campaign name changes | Not supported. Use campaign ID for grouping and filtering if campaign names were changed. |
| Ad networks | <ul><li>Can access SSOT DataLocker reports to see data attributed to their media source if:<ul><li>The advertiser has SSOT turned on in Conversion Studio.</li><li>The ad network is running SKAN campaigns.</li><li>The ad network has the required [permissions](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) from the advertiser to access aggregate data.</li></ul></li></ul> |
| Agency access | Not available. Agency users can view SSOT data in the SSOT dashboard. |
| D7 metrics | <ul><li>D7 metrics for organic traffic are available starting February 16, 2025.</li><li>May be missing or less than D2 metrics if:<ul><li>The date range includes dates for which 8 days haven't passed.</li><li>Modeled data isn't available (e.g., fewer than 14 days of revenue data). <Anchor target="_blank" href="/marketers/docs/skan-modeled-data#revenue-ltv">Learn more</Anchor>.</li><li>SKAN Conversion Studio configuration changed in the past 14 days.</li><li>There are fewer than 10 installs for a given date.</li></ul></li></ul> |
| Predefined event name | Since the event name ‘af\_conversion’ is used to indicate different types of conversions, apps that have an event specifically named ‘af\_conversion’ will see their original event renamed to ‘af\_conversion\_event’. |
| Local currency difference | As the SSOT dashboard and SSOT DataLocker report are not calculated simultaneously, minor discrepancies may occur when comparing revenue in local currency on the dashboard to the selected currency in the report. This is due to the slightly different currency rates used at the times the data were calculated. |
| SKAN D7 partial data | As SKAN D7 data is modeled and the initial version is ready 7 days post-install, when analyzing D7 metrics for days within the last 7 days, the D7 data will be partial. For records where the attribution method is SKAN, the D7 metrics will be lower than the D2 metrics. |
| Limited granularity for D7 revenue and in-app event metrics | Revenue and unique user event metrics for 7 days post-install are not available at the ad-set, ad, and conversion type levels of granularity. Since this level of detail is typically unavailable in SKAN, the model does not account for these dimensions. |
| Ad revenue data freshness | Ad revenue data has a delay of one day.<br /><br />For example, a report created on the morning of July 3 will include ad revenue data up to and including July 1. |

</Accordion>

<div data-zendesk-anchors="h_01J455DHWAB1J9611A4KA40PZM=note ssot-reports-in-data-locker=what-is-data-locker h_01J454K90GWKME8F4JCDQKM3CK=what-is-data-locker h_01J454K90GRCFR3PSAQRTX98B4=what-is-single-source-of-truth-ssot h_01J454PANH9J6ZZ069RS6FVWZM=benefits-of-ssot-reports-in-data-locker h_01J46C54ZB4YYTZ6CDHHC0EC8P=setting-up-data-locker h_01J455Q07J5XPYEBVP3BZ1FMVH=permissions h_01J29BTC9CESJF592P616WMK46=ssot-report-facts report-structure::673746b9=report-structure h_01J29CQ5K4JBEP4X8YQ0V32WYR=report-structure h_01J29CHBX2QNFTAQSA1W01PFH0=field-formats h_01J29BTC9CJ8GZDDCHK9NBZ4YX=dimensions h_01J29BTC9C86YMVEY17QQZNZCV=metrics h_01J29BTC9CH3DAA7ZRHG8C04MF=modeled-data h_01J29M72WAPH3KEW9N60JHTT3W=partial-data h_01J29MB7B7Q3PJ9YWFQESWN0KD=directory-structure h_01J29MCSH4V41CPB7ZG41751QW=report-folder-hierarchy h_01J29MCSH40ATHNAJMY8KR7ANZ=directory-and-filename-structure h_01J29MS6XV7XYTA9Q81454WEQN=bi-developer-considerations h_01J2F4HG8YHDGYFKHBBC5KSN2G=loading-reports h_01J2F4HG8YKNEVGEWTR91ADSDS=days-postattribution h_01J3YT1X908JVMDXKRQBCRD1JR=important h_01J2F4HG8YAAE0E04Y6Q9Z62NZ=considerations h_01J3A82HZF14CCS027FE991M0T=example-use-cases h_01J3A883DQFQE0WTTY4FMX3AQ4=calculating-total-attributions-per-campaign h_01J3A883DQ82K71XY408M2BW0B=calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign h_01J3A883DQ5QAVH6AX7CGCBSWG=calculating-retargeting-conversions-per-geo h_01J3A883DQE25X31SPPF166BRH=calculating-installs-by-attribution-method-per-media-source h_01J3A883DQ8QVR8WKPPX1QF414=calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset h_01J3A883DQ51T3Z6H239P5JDJ1=calculating-cumulative-revenue-for-selected-postinstall-periods h_01J3A883DQXRCQ4NWY0BCX886E=calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source h_01J3A883DQRR62BWQ6JBTZ7238=calculating-inapp-event-conversion-rate-for-2-days-postinstalls h_01J3A883DRPEVDQCWKCT9M3EC1=calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id h_01J3A883DRRZ9Y8F3KNAAPZT2S=calculating-amount-of-duplicates-per-media-source-in-this-query h_01J29MV69M667QDHMS5WGYKPCZ=traits-and-limitations" />
