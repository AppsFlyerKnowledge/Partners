---
title: Getting started—agency onboarding
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
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
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2026-08-12T11:37:20Z'
  id: 360002381617
  locale: en-us
  section: Agency onboarding
  section_id: 6551110223889
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360002381617-Getting-started-agency-onboarding
---
**At a glance:** Start measuring the campaigns of your clients by setting up an Agency account.

<Embed title="Getting started—agency onboarding" typeOfEmbed="wistia" url="https://fast.wistia.com/embed/iframe/54qzpj1lm7" providerUrl="https://fast.wistia.com" />


## AppsFlyer attribution model

Before you proceed, it’s essential to understand how AppsFlyer’s attribution works. This section explains what happens along the way from the first click or impression to the attribution of an install or an event — and beyond.

[![ua-agency-flow.png](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)

1. A marketer or an agency on behalf of the marketer configures a campaign with a certain ad network, using AppsFlyer attribution links.
2. A user clicks on one of their ads – for example, a banner or an offer link.
3. AppsFlyer attribution link behind the ad is then populated with information collected during the click. We gather the information from the attribution link and store it in our database.
4. The user is redirected to an app store.
5. The user installs the app and opens it for the first time. The AppsFlyer SDK inside the app calls our servers with the information about the device that the app is installed on.
6. We match this data to our click database using our <Anchor target="_blank" href="/marketers/docs/appsflyer-attribution-model">Attribution methods</Anchor>.
7. If we find a match, we attribute the install to the click. If not, we attribute the install to an organic download.
8. Once the install is attributed, we show it on marketer and agency dashboards and reports (<Anchor target="_blank" href="/partners/docs/about-agency-accounts#self-reporting-ad-networks">except Meta ads and X Ads</Anchor>).
9. Then, we send a postback with the conversion details to the ad network, who can use this information for further optimization.

## Agency role in mobile attribution chain

A marketer, who owns the app, integrates AppsFlyer SDK inside it in order to quantify their marketing effort.

Some app owners choose to hire marketing agencies to run advertising campaigns on their behalf. To do so, the agency should have an AppsFlyer account, and marketers should give the agency <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">access to their apps</Anchor>.

Agency, therefore, doesn’t technically own the apps but only promotes them on the marketing channels it works with, without the technical involvement, such an SDK integration. Depending on the set of permissions given by a marketer, an agency can have control over a range of functions.

When an install is attributed to an ad placed by an agency, it is displayed on agency's dashboard. The app owner will see it too, and will know that it's attributed to the agency.

Note: if your organization owns the app, or handles its development as well as marketing, you should open a marketer account.

## Pricing

The scope of an agency account functionality depends on the permissions provided by the app owner for each app. Therefore, agency accounts are offered **for free**, and only app owners are charged for attribution. App owners and agencies can use AppsFlyer attribution data for compensation purposes.

## Getting started

To set up a new agency account:

1. Complete the <Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">registration form</Anchor>.
   * Use your company email domain for registration.
   * Use an email address that is not associated with an existing AppsFlyer account.
2. A member of the AppsFlyer agency team may contact you with further information required to complete the registration.
3. Once your account is activated, you get notified and can start using AppsFlyer.

## Adding team members

When your account is up and running, the account admin (the person who opened the account) can add more team members, who can get access to some or all of the apps managed by the agency. For the details of how to add new team members, click here.

## Adding apps to your account

When you first create your account, it has no apps associated with it:

![agency-start.png](https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png)

Any agency individual or team requires permission from the app owner to:

* gain access to the app dashboard
* make configuration changes
* run campaigns

Marketers <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">provide access to any agency</Anchor> directly through the platform. Once your account is set up and you've received access to the apps, you can start running campaigns using AppsFlyer features.

### What does it mean to get permission from a marketer

When you get permission from a marketer:

* The app appears in your account.
* You can set up integrations with ad networks for the app (with the exception
  of some networks that require configuration by the app owner).
* You can create attribution links to use in your campaigns.
* You can set up cost integrations with partners (that allow it).
* You can see the app data.
* You can grant permission for ad networks and their team members to view
  basic information about the app.  

  > 📘 **Note**
  >
  > The agency gains control over the main toggle for ad network permissions and the individual permissions nested under it. Both the agency and the advertiser can change these settings, and the most recent change by either party determines the current state.


Additional permissions include access to the Cohort report, the Protect360 dashboard, and aggregate organic data. See a <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#agency-permissions">description of the different ad network permissions</Anchor>.

### App list

Once you got permission from the marketer, the app appears on the app's page.

The apps page in your account lists up to 1000 apps. If the list of apps you have permissions for exceeds 1000, some apps are not shown on the list. You can still find them using the search.

![agency-apps.png](https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png)

#### Searching for apps

1. In your account, from the top menu, select **My Apps.**
2. In the search field, enter the search term, for example:
   * App Name
   * App ID
   * App Owner Email

## Agency dashboard

Click any app in the list of apps to access its <Anchor target="_blank" href="/marketers/docs/getting-started-with-appsflyer-dashboards">dashboard</Anchor>. When you start running campaigns, the aggregate data attributed to you is displayed here.

![agency-dashboard.png](https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png)

The Agency account dashboard includes default access to:

* Lifetime value overview dashboard
* In-app events dashboard
* Retargeting dashboard

## Running campaigns

### Self-reporting networks (SRNs)

SRNs, also knows as Self-attributing networks (SANs), are networks that don’t require AppsFlyer’s attribution link in order to report clicks and other data, and use direct integration with AppsFlyer instead. Among these networks are <Anchor target="_blank" href="/marketers/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta ads</Anchor>, <Anchor target="_blank" href="/marketers/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor>, <Anchor target="_blank" href="/marketers/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads</Anchor>, <Anchor target="_blank" href="/marketers/docs/snapchat-advanced-srn-integration-setup">Snapchat</Anchor>, DoubleClick, <Anchor target="_blank" href="/marketers/docs/apple-ads-integration-setup">Apple Ads Search</Anchor>, <Anchor target="_blank" href="/marketers/docs/yahoo-integration-setup">Yahoo</Anchor>, and <Anchor target="_blank" href="/marketers/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">Yahoo! JAPAN</Anchor>.

A majority of these networks require special setup for agencies. For example, since Meta ads and X Ads integration can only be configured by an app owner, the agency campaign names MUST begin with the agency's name to make sure that the installs are eventually correctly attributed to the agency.

Click the links above to read network guides and specific instructions for agency settings.

### Non-SRNs

Most ad networks need attribution links that are placed behind an ad. Read more about running campaigns with them <Anchor target="_blank" href="/partners/docs/about-agency-accounts#non-srns">here</Anchor>.

### Sandbox attribution agency campaigns

Sandbox attribution infrastructure, part of Android by Google, lets marketers measure campaign success without advertising ID. Although Google doesn't include agencies as part of the Sandbox attribution process, and AppsFlyer can't attribute agencies directly, AppsFlyer still has the ability to provide attribution data for agency campaigns running on Sandbox.

#### Campaign naming

To view your campaigns in the AppsFlyer Sandbox dashboard, the names of campaigns that you configure, should include your partner identifier and be structured as follows:

* your af\_prt (<Anchor target="_blank" href="/partners/docs/about-agency-accounts#af_prt-parameter">What's your af\_prt and where to find it</Anchor>),
* underscore,
* your actual campaign name that follows your agency’s naming convention.

For example, if your af\_prt is AgencyX, your campaign name may look like this:

`AgencyX_SummerSale`

> 📘 **Note**
>
> * Agency campaigns in Sandbox attribution are also transparent and the identity of the ad network running the campaign is not masked from the marketer.

### SKAdNetwork agency campaigns

SKAdNetwork infrastructure, part of iOS by Apple, lets marketers measure campaign success without IDFA or advertising ID. Although Apple doesn't include agencies as part of the SKAdNetwork attribution process, and AppsFlyer can't attribute agencies directly, AppsFlyer still has the ability to provide attribution data for agency campaigns running on SKAdNetworks.

#### Campaign naming

To view your campaigns in the AppsFlyer SKAdNetwork dashboard, the names of campaigns that you configure with the SKAdNetwork, should include your partner identifier and be structured as follows:

* your af\_prt (<Anchor target="_blank" href="/partners/docs/about-agency-accounts#af_prt-parameter">What's your af\_prt and where to find it</Anchor>),
* underscore,
* your actual campaign name that follows your agency’s naming convention.

For example, if your af\_prt is AgencyX, your campaign name may look like this:

`AgencyX_SummerSale`

> 📘 **Note**
>
> * Agency campaigns in SKAdNetwork are also transparent and the identity of the ad network running the campaign is not masked from the marketer. Consider that starting iOS 15, the marketer (app owner) can <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">opt-in to directly receive a copy of the postback.</Anchor>
> * Make sure the marketer activates the ad network **Partner activation** setting in the Integration tab. Failure to do so will prevent AppsFlyer from sharing decoded postback data with networks, impacting their ability to use it for reporting and optimization. This is in addition to the Partner activation setting that you can access in the user interface.

#### Access to SKAN Conversion Studio

Agencies can <Anchor target="_blank" href="/marketers/docs/skan-conversion-studio#view-cv-mapping">view and download</Anchor> a marketer's SKAN CV mapping configuration in <Anchor target="_blank" href="/marketers/docs/skan-conversion-studio#skan-conversion-studio-basics">Conversion Studio</Anchor>, but they can't configure or edit the settings.

#### SKAdNetwork Dashboard

<Embed title="Getting started—agency onboarding" typeOfEmbed="wistia" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**Further reading:**

* <Anchor target="_blank" href="/marketers/docs/about-att-and-skan">SKAdNetwork Quickstart guide</Anchor>
* <Anchor target="_blank" href="/marketers/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAdNetwork Dashboard</Anchor>
* <Anchor target="_blank" href="/marketers/docs/skadnetwork-skan-solution-guide">SKAdNetwork Solution</Anchor>

### Single Source of Truth (SSOT) for agencies

SSOT unifies all attribution methods by combining attribution data from different models and removing duplicate installs and the associated cost and revenue-related metrics. This way, eCPI, ROI, and ROAS, for example, are calculated correctly.

Agencies can access SSOT data in the Overview dashboard, but not via API.

To include the SSOT flag in your overview dashboard, the marketer must turn on SSOT in the Conversion Studio.

**Further reading:**

* <Anchor target="_blank" href="/marketers/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Single Source of Truth (SSOT) guide for iOS attribution</Anchor>

## What else you can do

* Measure user retention
* Use in-app events to optimize your campaigns
* Run <Anchor target="_blank" href="/marketers/docs/retargeting-attribution-guide">retargeting</Anchor> campaigns
* Export your <Anchor target="_blank" href="/marketers/docs/manage-data-access-permissions">data</Anchor>
* <Anchor target="_blank" href="/marketers/docs/registering-test-devices">Register your test device</Anchor>
* and more.

You can find more information about advanced Agency account use <Anchor target="_blank" href="/partners/docs/about-agency-accounts#agency-setting-up-campaigns">here</Anchor>.

Stumbled upon an unfamiliar term? Find it in our <Anchor target="_blank" href="/marketers/docs/appsflyer-knowledge-base-glossary">Glossary</Anchor>.

Got an urgent technical question? Search our Help Center: we probably have an answer. If we don't, contact our support team via the bottom right corner of your dashboard.

<div data-zendesk-anchors="h_01HFXXKCMW7EREMC7KEYTF3ERH=appsflyer-attribution-model h_01KZTW5D6QWFP2Z3J31M9B6QKR=appsflyer-attribution-model h_01HFXXKCMW987FV2PB4EPXH92Z=agency-role-in-mobile-attribution-chain h_01HFXXKCMWPN6AN98A5RD5YXW7=pricing h_01HFXXKCMWRXVBYTW9RYEX7X8F=getting-started h_01HFXXKCMWB6ZG3PSHDSETC4XC=adding-team-members h_01HFXXKCMWBZVTHAEKED1Q27M3=adding-apps-to-your-account h_01HFXXKCMWYNNZWTKP9KEQ4VCD=what-does-it-mean-to-get-permission-from-a-marketer h_01JV9KR17EEHA6F2F8J13AEZEV=note h_01HFXXKCMWKW78TMC76F40PY2C=app-list h_01HFXXKCMW8S93N577393QZTYX=searching-for-apps h_01HFXXKCMWPZVADY15DKATJ7Z4=agency-dashboard h_01HFXXKCMWFB9RXY7AVBX5CGB9=running-campaigns selfreporting-networks-srns=self-reporting-networks-srns h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=self-reporting-networks-srns nonsrns=non-srns h_01HFXXKCMWPAMZ373D5AVD5EJF=non-srns h_01J6PCDYM2W1X6EMMEE7SFB3VE=sandbox-attribution-agency-campaigns h_01HFXXKCMWMW1AHXMS19CYD4VC=campaign-naming h_01HFXXKCMWEQ41A7TZ2K6DE424=note-1 h_01HFXXKCMWZ19E0QR1VE977BTS=skadnetwork-agency-campaigns 01J6PCG6JGY2R8T5DDCR8APM66=campaign-naming-1 01J6PCG6JHK9TGX93SD4DRP393=note-2 h_01HFXXKCMWX53HMRG2ZTD9FYQE=access-to-skan-conversion-studio h_01HFXXKCMW1HHMSS3XAXJKME29=skadnetwork-dashboard h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=single-source-of-truth-ssot-for-agencies h_01HFXXKCMXQ2JT63GBMC74PWBA=what-else-you-can-do" />
