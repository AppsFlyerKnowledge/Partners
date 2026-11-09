---
title: Access to aggregated analytics tools for API partners
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Premium API
    - Marketers
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketers
    - Marketing Analytics
    - Ad Networks
  created_at: '2020-02-17T10:50:10Z'
  edited_at: '2026-08-13T13:36:27Z'
  id: 360005854857
  locale: en-us
  section: Aggregate data
  section_id: 6551715006353
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360005854857-Access-to-aggregated-analytics-tools-for-API-partners
---
> **At a glance:** API partners can use their API token to access advertisers' data when granted permission by the advertiser, allowing them to extract performance metrics from the platform.

## API token permissions

<Image align="center" alt="api-access-permissions.jpg" src="https://files.readme.io/7961394cb39cf1e6f85d77cd732183edea5fb1408c220ca05b23ae7bbb50138e-23701010316689.jpg" width="439px" />

Advertisers can grant the following app-level permissions:

| Permission type | Reporting tool | Limitations |
| --- | --- | --- |
| Aggregated analytics reporting | <Anchor target="_blank" href="/marketers/fr/docs/cohort-analytics-via-data-locker">Cohort analytics data via DataLocker</Anchor> | X Ads campaign data isn't available to API partners due to their restrictions. |
| SKAN reporting | <ul><li><Anchor target="_blank" href="/marketers/fr/docs/skan-aggregated-performance-report-api">SKAN performance reporting</Anchor></li><li><Anchor target="_blank" href="/marketers/fr/docs/skan-aggregated-postback-arrival-date-api">SKAN aggregate postback reporting</Anchor></li></ul> | -- |


### Considerations

* **Advertiser perspective**
  * Advertisers can grant the API partner permissions as listed in the preceding table.
* **Partner perspective**
  * Extract data by API. **Note**: Security is implemented via an authentication <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">token</Anchor> available in the AppsFlyer dashboard. The same token is valid for all apps and advertisers.
  * Get data via Data Locker
  * Advertisers can revoke permissions to access their app data. This won't impact your partner credentials.

<Accordion title="Granting access to the partner">

> 🚧 **Important**
>
> **warning**
>
> * The permissions type lets the partner access data, including traffic brought by other partners and organic data.
> * Don't share your token with partners.

**To grant API access to the partner:**

1. In AppsFlyer, from the side menu, select **Collaborate** > **Integrated partners**.
2. Search for the partner and select it.
3. Click **Set up integration**. You're directed to the integration setup page.
4. From the **API access** tab, turn on one or more permissions. Select from:
   * **Aggregate analytics reporting**
   * **SKAdNetwork reporting** (for iOS apps, not relevant for Data Locker)
5. Click **Save API access**.
6. Notify the partner that you have enabled the necessary API access.

</Accordion>

<div data-zendesk-anchors="api-access-permissions=api-token-permissions h_01HGG3N6KVF9MCQRW8594YG0HV=api-token-permissions h_01HT2J7ZFVDA812R35948XXEM1=considerations h_01KZXND2TWVKK51RH3JWNMFENK=considerations" />
