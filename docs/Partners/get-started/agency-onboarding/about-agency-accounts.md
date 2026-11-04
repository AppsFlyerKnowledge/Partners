---
title: About agency accounts
metadata:
  keywords:
    - In-App Events
    - Agency Account
    - ROI
    - Agency
    - FMP
    - Advertisers
    - Agencies
    - Listed Agency
    - all installs
    - all launches
    - Partners
    - agency sign up
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2013-12-08T10:02:42Z'
  edited_at: '2026-05-26T11:24:00Z'
  id: 207034106
  locale: en-us
  section: Agency onboarding
  section_id: 6551110223889
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/207034106-About-agency-accounts
---
> **At a glance:** Make the most of your AppsFlyer Agency account with advanced configuration.

<div id="about-agency-accounts" />

## About agency accounts

Agency accounts are used by agency teams to measure app marketing campaigns run by the agency on behalf of marketer clients (app owners).

* Key pre-install and post-install metrics are available to ensure that agencies are delivering optimal performance across their client portfolio.
* Agency account dashboards provide similar capabilities and content to that of marketer dashboards. This includes the following dashboards:
  * Lifetime value overview
  * In-app events
  * Retargeting
* KPIs available include impressions, clicks, installs, user loyalty, cost, and ROI. About the <Anchor target="_blank" href="/marketers/docs/getting-started-with-appsflyer-dashboards">dashboard.</Anchor>

<div id="agency-access-to-marketer-data" />

### Agency access to marketer data

Agencies always have access to data of traffic attributed to the agency. Marketers can <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">grant agencies access to</Anchor> additional data, for example, organic aggregate data. See <Anchor target="_blank" href="/marketers/docs/manage-data-access-permissions">access to data by different types of users.</Anchor>

<div id="agency-access-to-ad-network-integrations" />

### Agency access to ad network integrations

To enable access to ad network integrations and have your campaigns measured, your agency must be pre-approved by the ad network. This is done by having your agency ID (af\_prt) included in the ad network's list of authorized agencies. Contact the partner to ensure your agency is included. [See here](/docs/about-agency-accounts#af_prt-parameter) how to find your agency ID.

<div id="note" />

> 📘 **Note**
>
> * Applies also to empty af\_prt parameters on attribution links
> * Doesn't apply to agencies working with <Anchor target="_blank" href="/marketers/docs/self-reporting-networks-srns">SRNs</Anchor>

<div id="agency-transparency" />

### Agency transparency

Agency traffic is set by default to be transparent. <Anchor target="_blank" href="/partners/docs/getting-started-agency-onboarding#transparency">Learn more</Anchor>

<div id="comparing-different-types-of-accounts" />

## Comparing different types of accounts

<div id="agency-versus-marketer-accounts" />

<Accordion title="Agency versus marketer accounts">

* **Marketer accounts** are geared towards serving the app and data-owner. Marketers add apps to their accounts and determine the data-access permissions.
* **Agency accounts** are purpose-built for agency teams. They include tools for efficient measurement and analysis of marketing campaigns across their client portfolio.

Account structures permit knowledge-sharing between global agency teams and enable group-level ROI measurement, calculations, reporting, and optimization.

<div id="differences-between-marketer-and-agency-accounts" />

#### Differences between Marketer and Agency accounts

|  | Marketer | **Agency** |
| --- | --- | --- |
| Code-level implementation | Yes | No; only promotion of the app |
| Account-level settings | Team members, team member permissions, settings, payment preferences | Agency team members and their permissions. |
| App-level settings | Reattribution window, OneLink configuration, time zone, currency | Settings are according to those set by the marketer |
| Integrated-partner-level configuration | <ul><li>Agency permissions</li><li>All non-SRN (attribution-link-based ad networks) configurations</li><li>SRN configurations</li><li>Link management</li></ul> | <ul><li>All non-SRN configurations</li><li>Some SRN configurations that require minimum intervention from the marketer's side:</li></ul><ul><li>Google Doubleclick<ul><li>Snapchat</li><li>Tencent</li></ul></li></ul>Other SRNs must be configured by the marketer in order for the agency to use them.<ul><li>Link management (using templates defined by Marketers)</li></ul> |
| Additional features | Yes (some, if part of the subscription plan) | As per marketer subscription and <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">permissions</Anchor> given to the agency (see the table below) |

<div id="features-available-to-agencies" />

### Features available to agencies

| Available by default | Not available | Requires marketer permission |
| --- | --- | --- |
| <ul><li>Lifetime value overview dashboard</li><li>In-app events dashboard</li><li>Retargeting dashboard</li><li>Active integrations</li><li><Anchor target="_blank" href="/partners/docs/getting-started-agency-onboarding#single-source-of-truth-ssot-for-agencies">SSOT dashboard</Anchor>\*\*</li></ul>\*\* Available only after the marketer has enabled this option. | <ul><li>Activity dashboard</li><li>Custom dashboard</li><li>People-based analytics</li><li>Audiences</li><li>Pivot report</li><li>Push API</li><li>Data locker</li></ul>*Only cohort reports are available upon marketer permission | <ul><li>Retention report</li><li>Cohort dashboard report</li><li><Anchor target="_blank" href="/partners/docs/data-locker-reports-for-agencies">Cohort report from Data Locker</Anchor></li><li>Protect360</li><li>Raw-data export</li><li>Aggregate organic data</li><li>Pull API</li></ul> |

</Accordion>

<div id="agency-vs-ad-network-account" />

<Accordion title="Agency vs. ad network account">

<div id="differences-between-ad-network-and-agency-accounts" />

#### Differences between Ad network and Agency accounts

<table><thead><tr><th>Ad network</th><th>Agency</th></tr></thead><tbody><tr><td>Attribution link parameter for identification: <code>pid</code></td><td>Attribution link parameter for identification: <code>af_prt</code></td></tr><tr><td>Places app ads on its own platform</td><td>Promotes the app via multiple media sources</td></tr><tr><td>Sees only traffic from ads placed on its platform</td><td>Sees only traffic from media sources it advertises on</td></tr><tr><td>Can receive real-time information about installs and in-app events via postbacks</td><td>Cannot receive real-time information about installs and in-app events via postbacks</td></tr><tr><td>Can configure in-app event postbacks for any traffic from itself\*</td><td>Can configure in-app event postbacks to some of the partners it brings traffic from\*</td></tr><tr><td colspan="2">\* Requires marketer permission</td></tr></tbody></table>

</Accordion>

<div id="agency-accountscampaigns-and-reporting" />

## Agency accounts—campaigns and reporting

<div id="agency-setting-up-campaigns" />

<Accordion title="Agency: setting up campaigns">

Agencies can measure the following main traffic types:

* [Self-reporting ad networks (SRNs)](/docs/about-agency-accounts#self-reporting-ad-networks)
* [Non-SRNs (ad networks using attribution links)](/docs/about-agency-accounts#non-srns)

<div id="important" />

> 🚧 **Important!**
>
> When working with agencies, turning off an integrated partner does not automatically disable certain attribution capabilities for the agencies linked to that partner:
>
> To fully deactivate these capabilities for agencies, the advertiser must manually turn off the following settings before deactivating the partner:
>
> 1. Install view-through attribution
> 2. Cross-platform equal attribution priority
>
> Only after disabling these toggles should the advertiser proceed to deactivate the partner.
>
> **Note:** If the advertiser deactivates the partner without first turning off these settings, the agencies may continue to use these attribution capabilities.

<div id="self-reporting-ad-networks" />

### Self-reporting ad networks

Self-reporting networks, such as Meta ads, Google Ads, or X Ads don't use external attribution links. Instead, each network has its own methods and APIs that AppsFlyer uses to communicate new installs, in-app events, etc.

<div id="srn-configurations" />

#### SRN configurations

| SRN | Marketer to perform initial SRN setup | Details |
| --- | --- | --- |
| Apple Search Ads | Yes | For details of agency configuration for Apple Search Ads campaigns, click <Anchor target="_blank" href="/marketers/docs/apple-ads-integration-setup#configuring-agencies-and-marketing-partners">here</Anchor>. |
| Google Ads | Yes | For details of agency configuration for Google Ads campaigns, click <Anchor target="_blank" href="/marketers/docs/google-ads-adwords-integration-setup-for-agencies">here</Anchor>. |
| Google Marketing Platform (GMP) | No | GMP has two different APIs. Learn more about the <Anchor target="_blank" href="/marketers/docs/google-marketing-platform-display-video-360-dv360-integration#comparing-the-legacy-and-new-integrations">differences between the two</Anchor>, and choose the one relevant to you. |
| Meta ads  <br />and  <br />X Ads | Yes | **Note:** This section refers to Meta ads. For attribution of Facebook Social (posts), read about [Owned Media](/docs/about-agency-accounts#owned-media%E2%80%94onelink-and-custom-links).<br /><br />**All Meta ads and X Ads campaigns must start with the Agency account name followed by "\_".** The name is defined in the AppsFlyer platform.<br />Campaigns that aren't named correctly are visible to the marketer but remain invisible to the agency account.<br /><br />**Note:**<ul><li>The agency name is CASE SENSITIVE.</li><li>See more details about <Anchor target="_blank" href="/marketers/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta ads</Anchor> and <Anchor target="_blank" href="/marketers/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor> setup for agencies.</li><li>Contact [agency@appsflyer.com](mailto:agency@appsflyer.com) if you have any questions about this.</li></ul>**Example**<br />agencyx runs a Meta ads campaign called agencyx\_brilliantcampaign, which is visible to it.<br /><br />agencyz runs an X Ads campaign called AgencyZ\_whathaveidonewrong, but doesn't see any results. This happens because the agency name part of the campaign is different to the defined agency name (capital A and Z). |
| Snapchat | No | For details of agency configuration for Snapchat campaigns, click <Anchor target="_blank" href="/marketers/docs/snapchat-advanced-srn-integration-setup">here</Anchor>. |
| TikTok for Business | Yes | For details of agency configuration for TikTok for Business campaigns, click <Anchor target="_blank" href="/marketers/docs/tiktok-for-business-advanced-srn-integration-setup#setting-up-tiktok-for-business-for-agencies">here</Anchor>. |
| Yahoo (Oath: Ad Platforms / Yahoo Gemini) | Yes | For details of agency configuration for Yahoo campaigns, <Anchor target="_blank" href="/marketers/docs/yahoo-integration-setup#agency-configuration">click here</Anchor>. |

<div id="non-srns" />

### Non-SRNs

Unlike SRNs, the vast majority of ad networks use attribution links for attribution purposes. <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#attribution-link-tab">These attribution links are already provided</Anchor> in each network's settings on AppsFlyer and can be simply copied from there directly.

For agencies, the process is almost identical to that of the marketers. Upon going to the setup window of any regular ad networks the attribution link is already there. The only difference is the automatic addition of the `af_prt` parameter to the attribution link.

<div id="ad-network-configuration-visibility" />

#### Ad network configuration visibility

Ad network setup is visible to ad networks themselves only when the marketer (app owner) configures it. When an agency activates and configures ad network integration, the network sees this section as inactive.

<div id="af_prt-parameter" />

#### af\_prt parameter

The value of the `af_prt` parameter is the agency name. When the agency name is passed in the `af_prt` parameter, it's converted to lowercase letters.

When `af_prt` with your agency name is part of the attribution link, new installs can be attributed to your agency account. Otherwise, new installs are attributed directly to the ad network.

[![agency-af-prt.png](https://files.readme.io/61559e2e1628e9411665b7e8d3d3d440a55effb3bccda79c7fe1ee02fd43fb8c-32355631649937.png)](https://files.readme.io/61559e2e1628e9411665b7e8d3d3d440a55effb3bccda79c7fe1ee02fd43fb8c-32355631649937.png)

**Do not use links received from the marketer**: make sure to use the links from your own account to prevent wrong attribution.

<div id="special-case-all-installs-and-all-launches-networks" />

#### Special case: All-installs and all-launches networks

Some non-SRNs require (or allow) marketers to send them postbacks **for devices that aren't attributed to them**.

All-installs network The network accepts a postback for every new app install, from any source

All-launches network The network accepts a postback for every new app launch, from any source

Some examples for all-installs networks are Vungle, Wechat, Startapp, Unity Ads, and more.

The following table shows the full list of the all-launches networks:

| Network Name | Network PID (on AF attribution links) |
| --- | --- |
| Supersonicads (a legacy network of ironSource) | supersonicads\_int |
| Adelphic Remarketing | adelphicremarketing\_int |
| Grow Mobile | growmobile\_int |
| ONE by AOL | advertising.com\_int |
| Lemmonet Mobile | lemmonetmobile\_int |
| Clickky | clickky\_int |
| Remerge | remerge\_int |
| MyThings | mythings\_int |
| TikTok for Business | bytedanceglobal\_int |

<div id="how-to-setup-agency-attribution-with-all-installslaunches-networks" />

#### How to setup agency attribution with all installs/launches networks?

Working with these networks entails sending information from installs that are not brought by the agency. Therefore, these networks require the marketer to configure them BEFORE the **agency**.

<div id="example" />

> 📄 **Example**
>
> Let's use agency attribution setup with Tapjoy as an example:
>
> 1. Marketer goes to Tapjoy setup window on the marketer's dashboard.
> 2. Marketer enters the Tapjoy App ID, given to the **marketer** by Tapjoy, in the **app\_id** text field.
> 3. Under the **Integration** tab > Default postbacks, the marketer selects **All media sources, including organic**.
> 4. Agency goes to Tapjoy setup window on the agency's dashboard.
> 5. Agency enters the Tapjoy App ID, given to the **agency** by Tapjoy, in the **app\_id** text field.

<div id="deep-linking" />

### Deep linking

Deep linking is the launch of a mobile app when opening personalized content and/or sending the users to specific activities within the app. This can provide your users with superior user experience and enhance their engagement.

For deep linking to work, the mobile app MUST be developed with deep linking capabilities and infrastructure. Contact the app owner to find out whether the app is suitable for deep linking, before setting up the campaigns.

<div id="retargeting" />

### Retargeting

* * <Anchor target="_blank" href="/marketers/docs/retargeting-attribution-guide">Retargeting attribution</Anchor> allows you to target existing or past users in your campaigns. Retargeting campaigns often require deep linking capabilities to work correctly.

<div id="in-app-events" />

### In-app events

App owners can have various events in their apps (e.g. purchase, watching a tutorial, passing a level, etc), that they can record and analyze in AppsFlyer. Agencies can see data of events attributed to them on the Events page in their account.

<div id="in-app-event-postbacks" />

#### In-app event postbacks

Agencies can be given permission to configure <Anchor target="_blank" href="/marketers/docs/in-app-event-postback-configuration">in-app event postbacks</Anchor> (including the <Anchor target="_blank" href="/marketers/docs/measure-sessions">af\_app\_opened event</Anchor>) to ad networks, upon receipt of permission from the Marketer.

Agencies can give the ad networks permission to configure in-app postbacks to themselves. <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">Permission is granted</Anchor> by marketers in the agency permission tab.

</Accordion>

<div id="reporting-for-agencies" />

<Accordion title="Reporting for agencies">

* Traffic statistics are viewed and downloaded directly from the AppsFlyer dashboard.
* Reports are accessed via the <Anchor target="_blank" href="/marketers/docs/raw-data-reporting-overview">Export Data</Anchor> page in the AppsFlyer dashboard. You can also access Cohort reports via <Anchor target="_blank" href="/partners/docs/data-locker-reports-for-agencies">Data Locker</Anchor>.
* The following reports types are available:
  * Aggregate
  * Raw data
* Marketers and agencies mostly cannot access the same data in the dashboard, reports, and so on.
* Agencies are usually responsible for only a part of the marketer's traffic, so the agencies' access to the data is limited in comparison to that of marketers.
* <Anchor target="_blank" href="/marketers/docs/manage-data-access-permissions">This article</Anchor> breaks down these differences. The following sections highlight them

<div id="note-1" />

> 📘 **Note**
>
> Due to Meta ads and X Ads terms of service, **agencies**, who are considered 3rd parties, **do not have access to raw data reports traffic, originating from either Meta ads or X Ads**.

<div id="access-to-aggregate-data" />

### Access to aggregate data

* Performance reports also referred to as aggregate data reports, are available by default to agency accounts. Related reading: <Anchor target="_blank" href="/marketers/docs/aggregated-and-analytics-reporting-overview">Aggregate performance reports</Anchor>
* Access to aggregate organic data reports requires marketer <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">permission</Anchor>.
* Agencies can receive access to Retention and Cohort reports, and Protect360 dashboard. This requires that the marketer enable <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">**Allow access to your retention and cohort reports**</Anchor> or <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">**Allow access to your Protect360 dashboard**</Anchor>, respectively, in the **Permissions** tab of **Active integrations**.

<div id="access-to-raw-data" />

### Access to raw data

<Anchor target="_blank" href="/marketers/docs/raw-data-reporting-overview">Raw data reports</Anchor> (user-level data reports) contain attribution information and are divided into topics.

<div id="time-zone-and-currency" />

### Time zone and currency

Agencies see apps in the app-defined time zone and currency, but these settings can be changed only by marketers.

<div id="cost-reporting" />

### Cost reporting

Agencies can enable **Get cost data** when configuring an integrated partner that <Anchor target="_blank" href="/marketers/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">supports cost data</Anchor>.

**To enable Get cost data:**

1. In AppsFlyer, from the side menu, select **Collaborate** > **Active integrations**.
2. Filter the partners by the Cost: From the top of the **Active integrations** page, select **Supported features** > **Cost**.
3. Select the partner. You're directed to the **Integration** tab. Select Go to the **Cost** tab.
4. Turn on **Get cost data.**
5. Enter the API key for this partner.
6. Click **Save**.

<div id="accessing-and-viewing-cost-data" />

#### Accessing and viewing cost data

Cost data is available to the agency in the following data sources:

* **Overview** page: cost data is visible in the **Aggregated performance report** in the Overview page.
* **Reports**: cost data is available in exported reports such as **Installations** under **Raw data reports** and **Partners (Media sources)** under **Performance reports**

<div id="hybrid-account-data-access" />

### Hybrid account data access

Hybrid accounts are agency accounts that manage some of the apps as an Agency (app partner), and some as a Marketer (app owner).

The following account-level features have limited availability:

* <Anchor target="_blank" href="/marketers/docs/custom-dashboards">Custom dashboard</Anchor>: not available for agencies and hybrid accounts.
* Cohort report: available upon marketer's permission.
* Protect360: available upon marketer's permission.

If you have a hybrid account, they may appear on your dashboard, but you will get a 404 error when trying to open them.

If you would like to use these features, it's recommended to open a new Marketer account and separate your Marketer and Agency apps. The features mentioned above will be available in your Marketer account if you have them enabled.

</Accordion>

<div data-zendesk-anchors="h_01HDNYNZYR2FTMQ71EV2AY3A3A=about-agency-accounts h_01HDNYNZYRZKK97GZ6R0MB9RQN=agency-access-to-marketer-data h_01J00RYT8J0MBPHTGK5T4WEE43=agency-access-to-ad-network-integrations h_01HJR00RGQX0CQEHDS9BHBGJD4=note h_01HDNYNZYRYHJ98YQWVVENZ07P=agency-transparency h_01HDNYNZYR65409AGM9F2PZRC8=comparing-different-types-of-accounts h_01HDNYNZYS7A2H60EEAJ114VSM=agency-versus-marketer-accounts h_01HDNYNZYSS7WSQ07S7KRADN7Z=differences-between-marketer-and-agency-accounts h_01HDNYNZYSX4WPQKS0H6JN6FCP=features-available-to-agencies h_01HDNYNZYS8KRSPM5CPVJEJ74Y=agency-vs-ad-network-account h_01HDNYNZYS4VPZMY34WA3SG5JT=differences-between-ad-network-and-agency-accounts agency-accounts%E2%80%94campaigns-and-reporting=agency-accountscampaigns-and-reporting h_01HDNYNZYS32SNR5F0WKJ4G9Q1=agency-accountscampaigns-and-reporting h_01HDNYNZYSNF2RQ3E7PM4HK433=agency-setting-up-campaigns h_01KC9MDDRPTB05PV6NCGZVFRMJ=important selfreporting-ad-networks=self-reporting-ad-networks h_01HDNYNZYS8X1VA4T46DQYQZFE=self-reporting-ad-networks h_01HDNYNZYS8AM2MFPRXFA4JXNS=srn-configurations h_01HDNYNZYSFXZXR99T6ME2R43F=example nonsrns=non-srns h_01HDNYNZYSN28VZQKCBRGXAVY0=non-srns h_01HDNYNZYSG5MQDDKV55HF4X9C=ad-network-configuration-visibility h_01HDNYNZYSC7XNJCJ1F27KTM9Z=af_prt-parameter special-case-allinstalls-and-alllaunches-networks=special-case-all-installs-and-all-launches-networks h_01HDNYNZYSB4MKXD47E1VHDN62=special-case-all-installs-and-all-launches-networks h_01HDNYNZYSHNV2B27JQV4EEVFM=how-to-setup-agency-attribution-with-all-installslaunches-networks h_01HDNYNZYS5WYADGW24AVK9RCZ=example h_01HDNYNZYS5W0SMCF1YC6C3G4C=deep-linking h_01HDNYNZYS3Z7RE51M7G7386VZ=retargeting inapp-events=in-app-events h_01HDNYNZYTDFN4MB6QBEQ8P5XW=in-app-events inapp-event-postbacks=in-app-event-postbacks h_01HMDP38S3NPE5R4QZJ5CW404W=in-app-event-postbacks h_01HDNYNZYTA767NGSTNECTBCV2=reporting-for-agencies h_01HDNYNZYTYBWGMY2PP8MPQE2F=note-1 access-to-performance-reports=access-to-aggregate-data h_01HDNYNZYTDH4S38XG3JCZQYJJ=access-to-aggregate-data h_01HDNYNZYT4ZKBNGDR3QR1VTEZ=access-to-raw-data h_01HDNYNZYT97ET1TQHKSRDMWDC=time-zone-and-currency h_01HDNYNZYTYT9NHMHQQ77PK8CQ=cost-reporting h_01HDNYNZYTWB5WVYY8C347G1ME=accessing-and-viewing-cost-data h_01HDNYNZYTKZTCBSBKZEJ7M0JN=hybrid-account-data-access" />
