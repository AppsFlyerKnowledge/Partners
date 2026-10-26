---
title: Aggregated campaign performance report for ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketing Analytics
    - Ad Networks
  created_at: '2021-05-30T12:34:03Z'
  edited_at: '2026-02-04T10:24:58Z'
  id: 360020834237
  locale: en-us
  section: Aggregate data
  section_id: 6551715006353
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360020834237-Aggregated-campaign-performance-report-for-ad-networks
---
> **At a glance**: Ad networks load the aggregated performance report (AKA Cohort report) into their BI systems to calculate campaign performance metrics like the 7-day retention KPI.

## Aggregated campaign performance report

This report provides campaign performance data, including the number of unique users performing a given event. You (the ad network), use the data in your BI systems to calculate campaign performance metrics in the context of advertiser KPIs. The report is available daily via <Anchor target="_blank" href="/partners/docs/data-locker-for-partners">Data Locker for Partners</Anchor>

**Why do you need the report?**

Before iOS 14.5, the postbacks AppsFlyer sent you, contained sufficient data to calculate unique user event metrics.

Starting iOS 14.5, and advertiser adoption of Aggregated Advanced Privacy (AAP), postbacks of non-consenting users don't include user identifiers. The lack of identifiers prevents calculating unique user metrics, for example, 7-day retention. The lack of unique user metrics hurts your ability to optimize campaigns and the ability to set common retention goals with advertisers.

**What does the report contain?**

Metrics are provided with the best granularity possible using the dimensions reported and have the following performance metrics:

* Revenue
* Number of times a given event is performed
* Number of unique users performing an event
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vS89RlkFIss7uARroJcOcX1rU6gUmZ2ySYwfTprg9GaA2BYnvDPVqWmOicea1wrBnNuGgEuLPwzL_ac/pub?gid=0&single=true&output=csv">Example report</Anchor>

**How do you get the report?**

* Provided via Data Locker for Partners. The report updates <Anchor target="_blank" href="/marketers/docs/about-data-freshness-and-timezone-support#daily-processing">Daily UTC time</Anchor>.
* Before we start sharing the data with you, the advertisers must [grant permissions](/docs/aggregated-campaign-performance-report-for-ad-networks#permission-to-get-aggregated-performance-data) in the dashboard.

## About the report

<div id="report-structure" />

<Accordion title="Report structure">

#### Dimensions

<Table>
  <thead>
    <tr>
      <th>
        Field name
      </th>
      <th>
        Remarks
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        app\_id
      </td>
      <td />
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td />
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        <ul><li>Possible values: install, re-engagement, re-attribution</li><li>Equivalent postback macro: is\_retargeting</li></ul>
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        Possible values: click, impressions, pre-install, unknown, tv, null
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        The number of days elapsed since the attribution event.  <br />The maximum number of days is 180.<br /><br />Tip! Use this to calculate retention and KPI days.
      </td>
    </tr>
    <tr>
      <td>
        event\_date
      </td>
      <td>
        The date the event occurred.<br /><br />Format: yyyy-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        conversion\_date
      </td>
      <td>
        Format: yyyy-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        event\_name
      </td>
      <td>
        Identifies the event. Some event names have a specific meaning while others relate to in-app events set by the advertiser in the app.

        | event\_name | What did the user do |
        | --- | --- |
        | af\_conversion | User converted. Use conversion\_type to identify if it is an install, re-engagement, or re-attribution. |
        | af\_sessions | Opened the app |
        | af\_uninstall | Uninstalled the app |
        | Advertiser defined in-app event | Performed an in-app event in the app. In-app event names aren't mapped to partner event names. |
      </td>
    </tr>
    <tr>
      <td>
        campaign
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        campaign\_id
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        adset
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        adset\_id
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        ad
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        ad\_id
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        channel
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        site\_id
      </td>
      <td>
        Campaign hierarchy
      </td>
    </tr>
    <tr>
      <td>
        {"is_primary_"} attribution
      </td>
      <td>
        Use to identify and deduplicate retargeting data
      </td>
    </tr>
    <tr>
      <td>
        country\_code
      </td>
      <td>
        Derived from the user IP address
      </td>
    </tr>
    <tr>
      <td>
        agency
      </td>
      <td>
        If blank, there is no agency associated
      </td>
    </tr>
    <tr>
      <td>
        Keywords
      </td>
      <td>
        [Available starting April 27, 2022] Word(s) used in the user's online search. As reported by the ad network
      </td>
    </tr>
    <tr>
      <td>
        Keyword ID
      </td>
      <td>
        [Available starting April 27, 2022] Keyword ID returned by the ad network.
      </td>
    </tr>
  </tbody>
</Table>

#### Metrics

| Name | Field | Unique users performing the event |
| --- | --- | --- |
| Unique users | unique\_users | Number of unique users performing the event |
| Revenue | revenue\_usd | Cumulative revenue in USD. For example, $100.00 is reflected as 100. |
| event\_count | event\_count | Number of event occurrences |

</Accordion>

<div id="bi-developer-considerations" />

<Accordion title="BI developer considerations">

**Scope of data in the report**

The report contains user attributions, installs, re-attributions, and re-engagements, and their related in-app events.

In your data consumption process, you must use logic to split the data between campaign types. Meaning, user attribution (installs) and retargeting (re-engagements). To do so, use the conversion\_type and is\_primary\_attribution field. See <Anchor target="_blank" href="/marketers/docs/resolve-retargeting-double-attribution">Double attribution of retargeting events.</Anchor>

**Field-level considerations**

* Use post-attribution days to enable easy calculation of retention metrics.
* Calculating unique users using campaign name and campaign ID dimensions: If you can disregard campaign name granularity, you can sum unique count on campaign ID and the metrics are correct.
* You can aggregate the data using the campaign hierarchy fields.
* In-app events use the advertiser event name and aren't mapped to your event names. Ask the advertiser to provide you with the mappings or view them in the dashboard. <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">Partner in-app event mapping</Anchor>.
* Revenue is in USD is calculated using the exchange rate on the event day.
* Ad revenue events are included where available but update with a lag of up to 5 days.

**General considerations**

* Data freshness: Daily, starting 08:00 UTC. Data is written to the Data Locker h=23 folder.
* Data available is user journey attribution data attributed by AppsFlyer. Meaning, SKAdNetwork reported by iOS postbacks isn't included in this data set.
* Data is contained in files that contain multiple apps. Use the app\_id field to identify the app.
* If you don't get data for a given app, verify that the advertiser has granted you the necessary permissions.

</Accordion>

<div id="retention-report-considerations" />

<Accordion title="Retention report considerations">

To create retention metrics, for example, retention day-7, do so by setting filters on the following fields:

* days\_post\_install=7
* event\_name=af\_session
* conversion\_type as required
* To prevent the inclusion of <Anchor target="_blank" href="/marketers/docs/resolve-retargeting-double-attribution">duplicate retargeting events</Anchor>, select is\_primary\_attribution=true or use conversion\_type to limit the data set to installs.
* Group by: campaign and other dimensions as needed.
* Sum: unique\_users\_count

By adding or removing dimensions you can get metrics with different granularity.

</Accordion>

## Permissions

You (the ad network), must ask the advertiser to grant you the permissions listed here. The advertiser must perform this procedure once per app.

<div id="permission-to-get-aggregated-performance-data" />

<Accordion title="Permission to get aggregated performance data">

Ad networks appointed (activated) by agencies: The agency can't grant permission. The agency must ask the advertiser to grant the permissions for them.

**To allow the ad network to get aggregated performance data:**

1. In AppsFlyer, from the side menu, select **Collaborate** > **Integrated partners**.
2. Search for the partner and select it.
3. Click **Set up integration**. You’re directed to the integration setup page.
4. Verify that **Activate partner** is on. If not, data isn't shared.
5. Go to the **Permissions** tab.
6. Turn on the following ad network permissions:
   * **Access aggregate conversions data**.
   * **Access aggregate in-app events data**.
   * **Access aggregate revenue data**.
7. Click **Save Permissions**.
8. Notify the ad network that you have granted the permissions.
9. If you have multiple apps, repeat the procedure for each app integrated with the partner.

</Accordion>

<div data-zendesk-anchors="h_01HM8SQ5RE1FGQDY6V1A8MMEQX=aggregated-campaign-performance-report h_01HM8SQ5REM6MW5GBRSXTF0N73=about-the-report h_01HM8SQ5RETK7HCPZGGX8KX9VG=report-structure h_01HM8SQ5RE11PW6HGTWGC2AGR5=dimensions h_01HM8SQ5RGQEH6G6W75FVWJKSP=metrics h_01HM8SQ5RGCGTWTSRHB8B4FSY2=bi-developer-considerations h_01HM8SQ5RG4JEE75F6CBTFCBB5=retention-report-considerations h_01HM8SQ5RGNXENZ89GD74KJWH2=permissions h_01HM8SQ5RGQADHTEP5ED3W87VZ=permission-to-get-aggregated-performance-data" />
