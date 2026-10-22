---
title: Integrated partners dashboard
metadata:
  keywords:
    - partner login
    - partner dashboard
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-08-08T08:11:38Z'
  edited_at: '2023-10-11T12:54:23Z'
  id: 212955423
  locale: en-us
  section: Aggregate data
  section_id: 6551715006353
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/212955423-Integrated-partners-dashboard
---
> **At a glance:** Integrated partners use the dashboard and reports to view and analyze campaign traffic attributed to you.

## Using the AppsFlyer dashboard

**To log in to AppsFlyer**:

1. <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">Log in</Anchor> or navigate to https://hq1.appsflyer.com/auth/login  
   The list of apps displays.
2. Select an app or search for it.  
   Note! If you don't see the required app, ask the advertiser to grant you <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">Ad network permissions</Anchor>. The advertiser does this in the AppsFlyer dashboard in the permissions tab.

## Overview dashboard

Campaign performance metrics and charts are available in the Overview dashboard. This dashboard contains different view types for UA and retargeting campaigns.

## Report access

To view report data:

* In the side menu, select one of the following:
  * <Anchor target="_blank" href="/marketers/docs/raw-data-export-page">Raw Data Export</Anchor>
  * <Anchor target="_blank" href="/marketers/docs/aggregated-data-export-page">Aggregated Data Export</Anchor>  
    The Reports window opens.

> 📘 **Note**
>
> * Data shown in raw data reports is limited to raw data in postbacks attributed to the partner only.
> * For Protect360 subscribers, when the **<Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#access-protect360-dashboard-raw-data">Protect360 dashboard & raw data</Anchor>** permission is granted by the advertiser, partners also have access to Protect360 raw data reports.
> * **Event value** data is not displayed in this report. To get event values, you can do one of the following:
>
> * * Request from the advertiser to provide you in-app event raw data reports
>   * Add `(event-value)` <Anchor target="_blank" href="/partners/docs/postback-macros-for-ad-networks">macro to the postback URL</Anchor>

### Using Postback reports

You can use the Installation and In-app event <Anchor target="_blank" href="/marketers/docs/raw-data-reporting-overview#postbacks">postback reports</Anchor> to find 'missing' actions., i.e. when the advertiser's raw data shows user actions that were not recorded in the ad network.

Download the relevant Postbacks report and look for the **Postback URL** and **Postback HTTP Response Code** fields:

* If the response code is 200, AppsFlyer sent the postback and received acknowledgment from the ad network.
* If the response code is missing, AppsFlyer sent the postback but received no response. The **Postback Error Message** field describes the problem.

[![](https://files.readme.io/e846104ebdd43b6bdd5c635e645ba5806aa152e6fa84d92f957b754b22fd819a-360005578257.png)](https://files.readme.io/e846104ebdd43b6bdd5c635e645ba5806aa152e6fa84d92f957b754b22fd819a-360005578257.png)

## Viewing configuration settings and data

Click **Active Integrations** on the left side of the window to view the current configuration settings. Even if you have not been granted permissions, you may be able to view the configuration settings (read-only mode).

Ad network can view the configuration on its dashboard only when it is set up by the advertiser. 

Agencies can configure ad network setup upon getting relevant permission from the advertiser. Note that **when** **the configuration is made by an agency, the ad network sees it as inactive**.

## Permissions

Using the **Permissions** tab, advertisers can <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">grant different types of permissions to the ad networks</Anchor>.

### Enabling Permissions

The first step is for your client to enable permissions. Your client must switch **Ad Network Permissions** on. When they do so, the following takes place:

1. The app displays in your ad network account.
2. The admin of your ad network account gets access to view the dashboard of your client's app. At the first stage, only the admin has access. If you want your team member to also view the app's dashboard, your client needs to give them permissions.
3. Permissions to view the app's dashboard are given only to your ad network.

### Granting permissions to ad network team members

If you want your team member to also view the app's dashboard, your client needs to give them permissions.

1. Give your client the emails of the team members that you want the client to give permissions to.
2. The client should then <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">add them to the integration with your ad network</Anchor>.

### Granting additional permissions

Your client can grant additional permission for the ad network and its team members to view the following:

* Integration parameter configuration
* In-app event postback configuration
* Retention report
* Loyal users
* In-app events
* Revenue
* Protect360 dashboard & raw data - available only to Protect360 customers

To allow this, contact your client to select you from the list of Active Integrations and grant you access to the relevant section within the Permissions tab.

When the advertiser gives permission for the ad network to configure their attribution link and map in-app events, they can enter the relevant tabs and make changes accordingly.

> 📘 **Note**
>
> * Any changes made to the configuration overwrite the current configuration irrespective of whether it is set by the advertiser or the ad network.
> * Agencies can add ad network team members to the configuration, but only app owners can provide permissions to ad networks.

Once your client has granted you permission to the integration parameter configurations, you are able to access it from the left side of the main dashboard and select **Active Integrations.**

If your client has granted you permission to the Retention Report, you are able to access it from the left side of the main dashboard and select **Retention.**

<div data-zendesk-anchors="h_01HCF5VPHN5RRQFXVJJFPFQBSW=using-the-appsflyer-dashboard h_01HCF5VPHNXBQZNF9MNEVCQ243=overview-dashboard h_01HCF5VPHN08CV555KDHB7QP1Z=report-access h_01HCF5VPHN3REJ2FPD8386Z92S=note h_01HCF5VPHN8RV3GBX1NNFX10P0=using-postback-reports h_01HCF5VPHNSW9X7SNQPC17Q45A=viewing-configuration-settings-and-data h_01HCF5VPHN6AJ7SE6MGW57BPW8=permissions h_01HCF5VPHNRCQ5P3MZF9S5RWZW=enabling-permissions h_01HCF5VPHP2EXY705GW2VM5YMA=granting-permissions-to-ad-network-team-members h_01HCF5VPHPHS8QQBMVTGV7B4VJ=granting-additional-permissions h_01HCF5VPHPCD52R9222AFQH176=note-1" />
