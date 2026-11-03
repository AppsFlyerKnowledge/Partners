---
title: Cost Import for ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2025-09-10T14:33:39Z'
  id: 360002868097
  locale: en-us
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360002868097-Cost-Import-for-ad-networks
---
> **At a glance:** Learn how ad networks can report the advertiser's campaign costs directly to AppsFlyer via CSV files.

## Cost Import for ad networks

![AdspendIngestion.jpg](https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg)

#### Overview

* Prepare a CSV file containing the ad spend details as follows:
  * Date of spend
  * App ID (multiple apps allowed per file if the apps belong to the same owner)
  * Media source (one per file allowed)
  * Campaign name
  * Spend amount
  * [Optional] Geo
  * [Optional] Currency (default USD)
* Submit the file to AppsFlyer by email/file upload using the ad network account in AppsFlyer.   
  **Note:**
  * Before you submit files for the first time, the advertiser must grant you, the ad network, Cost Import permission. This needs to be done once for each app and is a very brief process.
  * Once a file is uploaded, it can't be reverted.
* Monitor and check that no errors were found in the file.

### Submitting ad spend files for ad networks

* Use either the upload or email method to ingest ad spend files.
* [Best practice] Initially, use the upload method as it is easier to resolve CSV formatting issues.
* Ad Networks cannot import agency cost data; only advertisers can.

#### Submission by file upload

**To submit Cost Import files by upload:**

1. [For each app that you work with you need to do this once] <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-permissions-for-ad-networks">Ask the advertiser to grant you Cost Import permission</Anchor>.
2. <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#prepare-csv-file-with-cost-data">Prepare the CSV file using this format and schema</Anchor>.
3. Click here to <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">log in to your AppsFlyer ad network account.</Anchor>
4. <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#upload-file">Upload and ingest the file</Anchor>.
5. In the AppsFlyer dashboard, monitor the ingestion:

   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Status</Anchor>
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#matched-rows">Matched rows</Anchor>
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Cost Import actions</Anchor>
6. Additional procedures:
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Overwrite previous ingestion</Anchor>
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Revert (cancel)</Anchor>

#### Submission by email

**To submit Cost Imports files by email:**

1. [For each app that you work with you need to do this once] <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-permissions-for-ad-networks">Ask the advertiser to grant you Cost Import permission</Anchor>.
2. <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#prepare-csv-file-with-cost-data">Prepare the CSV file using this format and schema</Anchor>.
3. If you don't have an Cost Import token (you'll need it when you email the file):
   * Click here to <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">log in to your AppsFlyer ad network account</Anchor>.
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#token-for-email-import">Get an Ad Spend token.</Anchor> Note: The same token is used for all advertisers.
4. Submit file by <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#email-file">Email</Anchor>
5. AppsFlyer emails a status report; it notes if the ingest was successful or if issues were found. **Note**: If the status mail was not received see <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">the Cost import dashboard</Anchor>.
6. In the AppsFlyer dashboard monitor the ingestion:

   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Status</Anchor>
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#matched-rows">Matched rows</Anchor>
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Cost Import actions</Anchor>
7. Additional procedures:
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Overwrite previous ingestion</Anchor>
   * <Anchor target="_blank" href="/marketers/vi/docs/import-cost-data#cost-import-dashboard">Revert (cancel)</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=cost-import-for-ad-networks h_01HX94WSX07YEG40X66TMRFJGA=cost-import-for-ad-networks h_01HX94WSX0HR2KTGRT7MQ481Y6=overview h_01HX94WSX0G429FTHKYCG07BB9=submitting-ad-spend-files-for-ad-networks h_01HX94WSX0ENTJEDMXWRHDCP0D=submission-by-file-upload h_01HX94WSX0HVTMFQQ0NMW0VSKP=submission-by-email" />
