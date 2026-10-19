---
title: Ad revenue signals for UA ad networks
excerpt: >-
  Ad networks responsible for user acquisition can receive data regarding ad
  revenue and use it to optimize their customers' UA campaigns.
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2026-05-14T15:36:34Z'
  id: 4402898251409
  locale: en-us
  section: Data Locker
  section_id: 6551591547409
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/4402898251409-Ad-revenue-signals-for-UA-ad-networks
---
Ad networks can receive reports via Data Locker with valuable ad revenue information regarding users. These users may have been acquired from campaigns served through them, or they may be from a different media source.

Ad networks can then ingest this data to campaign-targeting and optimization algorithms, and use it to improve ROAS campaigns based on a complete view of UA-generated revenue.

## Set the Ad Revenue report in Data Locker

The following activities need to be completed to access the Ad Revenue report in Data Locker:

* Ad networks have to [onboard to Data Locker for Partners](/docs/data-locker-for-partners#set-up-data-locker).
* Ad networks have to [configure the report output settings](#configure-the-report-output-settings) and [enable the Ad revenue report](#enable-the-ad-revenue-report).
* Advertisers have to permit ad networks to view the report. [See advertiser instructions](/marketers/docs/share-ad-revenue-data-with-partners#ua-signals-for-ad-networks)

<div id="configure-the-report-output-settings" />

<Accordion title="Configure the report output settings">

To configure the report output setting, follow the steps below:

1. In AppsFlyer, go to **Report** > **Data Locker.**
2. In the **Report output settings** area turn on **Send reports**.
3. Set the report file output properties.
   * The report format (Parqet/CSV).
   * The report compression method (Snappy/GZIPO/Uncompressed).
   * The maximum number of rows in a file.
4. Review the expected path of the report file outputs. The path is set according to your connection settings. To learn how to set up the connection see [Set up Data Locker](/docs/data-locker-for-partners#set-up-data-locker).

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="Enable the Ad revenue report">

1. In the **Data Locker content** section select the **Ad revenue [daily]** report type.
2. Click **Save connection**.
3. Make sure that the advertiser permitted the Ad network to view the report.
4. For instruction, see [Permit ad networks to get ad revenue data.](/marketers/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data)

</Accordion>

## Report specification

<div id="report-considerations" />

<Accordion title="Report structure and format">

* Format: Data arrives in CSV format to the UA partner's S3 bucket.
* Level: Contains device-level dimensions and metrics.
* Data enrichment: Includes ad revenue data from mediation partners, and adds attribution data relevant to the UA ad network (that is cleaned of all dimensions irrelevant to the UA ad network).
* Data freshness: [Daily, meaning data for Day 0 arrives on Day 1](/marketers/docs/about-data-freshness-and-timezone-support#ad-revenue). Data is written daily at 17:00 [UTC time](/marketers/docs/about-data-freshness-and-timezone-support#daily-processing) to the h=23 of your Data Locker bucket.
* Apps included: A single report contains the data of all apps for which advertisers have granted permission.
* The reports include data about all conversion types: Installs, re-attributions, re-engagements, and reinstalls.
* Currency: In USD. Event revenue is calculated to USD on the day the event occurred.
* [See sample report](https://docs.google.com/spreadsheets/d/e/2PACX-1vSoV1U_pMUoTFhIpyYQmUI1zQWArY19c8gMmsfpRiAaGXVZEG4WqgSC26u5-fv32j8ZQN4uxtNgVkYs/pub?output=csv)

</Accordion>

<div id="report-structure" />

<Accordion title="Report fields">

| **Field** | **Remarks** |
| --- | --- |
| Version | Unix timestamp in second. Example: 1661315124 |
| app\_id | App ID in the AppsFlyer platform |
| install\_time | <ul><li>Timestamp of install: YYYY-MM-DD HH:MM:SS<br />Example: 2020-08-16 11:22:33</li><li>For iOS 14+ devices and non-consenting users, or if the advertiser has Advanced Privacy on, install time is rounded to the nearest hour.</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Only populated if UA is attributed to the partner receiving the data. |
| idfa, idfv, advertising\_id | <ul><li>The same device ID, like IDFA, IDFV, or advertiser\_id could display in multiple rows if there are more than one ad revenue monetization events.</li><li>For iOS 14+ devices and non-consenting users, or if the advertiser has Advanced Privacy on, this does not display.</li></ul> |
| platform | Device platform: iOS, Android, or Windows Mobile |
| country | Country code using [ISO 3166 (alpha-2)](https://www.iso.org/iso-3166-country-codes.html) Example: US, CN |
| original\_url | <ul><li>For iOS 14+ devices and non-consenting users, or if the advertiser has Advanced Privacy on, this does not display.</li><li>Only populated if UA is attributed to the partner receiving the data.</li></ul> |
| ad\_unit |  |
| placement |  |
| mediation\_network |  |
| engagement\_type |  |

Metrics:

| **Field** | **Remarks** |
| --- | --- |
| impressions | Number of times the user saw the ad |
| revenue\_usd | Daily revenue (in USD) generated for the device ID. **Note**: When the revenue amount is small, it's represented in scientific notation. For example: 8.00E-05 |

</Accordion>

<div data-zendesk-anchors="h_01H8Y7ABGVR7BNHEYVFKPFM4JN=set-the-ad-revenue-report-in-data-locker h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=report-specification h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
