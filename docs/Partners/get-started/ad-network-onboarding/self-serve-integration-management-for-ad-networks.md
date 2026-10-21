---
title: Self-serve integration management for ad networks
metadata:
  keywords:
    - postbacks
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
  created_at: '2021-03-15T10:03:41Z'
  edited_at: '2026-08-13T00:01:05Z'
  id: 360018512658
  locale: en-us
  section: Ad network onboarding
  section_id: 6551058566033
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360018512658-Self-serve-integration-management-for-ad-networks
---
**At a glance**: Set up and manage your integration from the AppsFlyer dashboard.

<Embed title="Self-serve integration management for ad networks" typeOfEmbed="wistia" url="https://fast.wistia.com/embed/iframe/9kvwrhnzjo" providerUrl="https://fast.wistia.com" />

## **Prerequisites:**

* You have to have login credentials (username and password) for AppsFlyer before you can manage attribution links and postbacks. To <Anchor target="_blank" href="/partners/docs/getting-started-onboarding-guide-for-ad-networks">create a partner</Anchor> account, ask an AppsFlyer customer (advertiser) to <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#invite-new-partners-to-appsflyer">invite you</Anchor>.
* Management of attribution links and default postbacks is available only to partners who joined after February 1, 2022.
* Verify that your servers are ready to receive postbacks by complying with the following:
  * Allowlist AppsFlyer server <Anchor target="_blank" href="/marketers/docs/appsflyer-server-ip-address-ranges-allowlisting">IP addresses</Anchor> in your firewalls and security systems to ensure communication with your endpoints
  * TLS versions: TLS 1.1, TLS 1.2+ with the <Anchor target="_blank" href="/marketers/docs/appsflyer-https-ssl-encryption-policy-support#outgoing-messages-appsflyer-as-client">ciphers listed.</Anchor>
  * Ports: 80, 443
* ![AppsFlyerAdmin_us-en.png](https://files.readme.io/047d2ffa8bd5258c09f60c6f560162b285c4e9742d98b1158952a26d988ce763-18271759619089.png) Only Admin users can access and manage this section.

## Accessing Integration management

1. Log into your AppsFlyer partner account.
2. Click the top-right drop-down menu > **Postback Management**.

## Attribution link

The attribution link is the most important part of your integration. Attribution links are used to notify AppsFlyer about user engagement with an ad. Attribution links are placed behind ads, so that when a user clicks on an ad they are clicking on an attribution link.

Completion of attribution link configuration is mandatory

**To configure attribution link:**

1. In the **Attribution link** tab, add the parameters to be included in your attribution link:

   * **Parameter name**: AppsFlyer parameter screen name.
   * **Your macro**: add the macro that populates the parameters with values.
   * **Include**: check the box to include the parameter in the link

   > 🚧 **Important!**
   >
   > * Add campaign and ad-related parameters to provide more robust data about campaign performance.
   > * **Site ID** is a mandatory parameter
   > * Advertisers use this link as a basis for the integration of a specific app and can add additional parameters to it.
   > * App ID, Lookback window duration, and your Partner ID are added to the link automatically and you don't need to add them to this template.

2. **[Optional]** Add custom parameters that are not provided by AppsFlyer.
3. Use the link preview to verify that everything is correct.
4. Click **Save**.

<Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">More about attribution links and available parameters</Anchor>.

In the case of any issues, reach out using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.

## Default postback

Postbacks are URLs containing macros populated by AppsFlyer and sent to your servers in real-time after each conversion (either on your network, or other networks too — depending on your configuration).

**To configure the default postback:**

1. Enter the **endpoint addresses.** These are the endpoints to which postbacks are sent. Enter the relevant URLs for installs, in-app events, or both. To be able to activate the integration, at least the install postback URL is required.
2. Add parameters to the postback:

   * **Parameter name**: AppsFlyer parameter screen name.
   * **Your receiving parameter**: the respective receiving parameter on your side.
   * **Parameter value** (available for some parameters): choose the value format. For example, for boolean values, choose whether to receive them as "true"/"false", or 1/0.
   * **Install**: check the box to include the parameter in the install postback.
   * **In-app event**: check the box to include the parameter in the in-app event postback.

   <Anchor target="_blank" href="/partners/docs/postback-macros-for-ad-networks">Full list of postback macros</Anchor>

   > 🚧 **Important!**
   >
   > * To be able to distinguish between postbacks for legitimate events and rejected postbacks,  configure the <Anchor target="_blank" href="/partners/docs/postback-macros-for-ad-networks#macrosinstalls-in-app-events-and-rejected-events">rejected postback macros</Anchor>.
   > * To enable rejected install/in-app event postbacks, append the following parameters to your default postback template:
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`  
   >     **Note:** If the Advanced Privacy postback is enabled, append the parameters above to the Advanced Privacy template as well.

3. [Optional] **Custom parameters:** Configure your own parameters to include in the postback.
4. Use the postback template preview to verify that everything is correct.
5. Click **Save**.

<Anchor target="_blank" href="/marketers/docs/in-app-event-postback-configuration">More postback info and examples.</Anchor>

In the case of any issues, use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.

## Advanced Privacy and SKAN postbacks

Advanced Privacy and SKAN postbacks can be configured only after the attribution link and default postback are created.

**To manage the postbacks:**

1. Select a postback type:
   * <Anchor target="_blank" href="/partners/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Advanced privacy</Anchor> postback.
   * <Anchor target="_blank" href="/partners/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> postback.
2. Activate the builder.
3. **[For SKAdNetwork postback configuration only]** Enter your SKAdNetwork ID. This field is mandatory and the configuration can't be saved without a valid ID.
4. Enter the **endpoint addresses.** These are the endpoints to which postbacks are sent. Enter the relevant URLs for installs, in-app events, or both.
5. Add postback parameters:

   * **Parameter name**: AppsFlyer parameter screen name.
   * **Your receiving parameter**: The respective receiving parameter on your side.
   * **Parameter value** (available for some parameters): Choose the value format. For example, for boolean values, choose whether to receive them as "true"/"false", or 1/0.
   * **Install**: Check the box to include the parameter in the install postback.
   * **In-app event**: Check the box to include the parameter in the in-app event postback.

   List of <Anchor target="_blank" href="/partners/docs/skan-integration-guide-for-ad-networks#receive-data-from-appsflyer">SKAdNetwork postback macros</Anchor>

   List of <Anchor target="_blank" href="/partners/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification">Advanced Privacy postback macros</Anchor>

   > 🚧 **Important!**
   >
   > * To enable rejected install/in-app event postbacks, append the following parameters to your default postback template:
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`
   > * To enable rejected postbacks for Advance Privacy you must first append the parameters above to the [Default postback](/docs/self-serve-integration-management-for-ad-networks#default-postback)
   > * When the parameters above are added to both the Default postback and the Advanced Privacy postback (if enabled), rejected install/in-app event postbacks are enabled.

6. [Optional] **Custom parameters:** Configure your own parameters to include in the postback.
7. Use the postback template preview to verify that everything is correct.
8. Click **Save**.  
   Note, that when you save the postback, the changes take place immediately.

In the case of any issues, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.

<div data-zendesk-anchors="h_01KZTVV00EB224GJD5F7VBP071=prerequisites h_01H9FCSTYR157CCJWTYSNE9JQ0=accessing-integration-management h_01H9FCSTYR6HRSF9F8KCR4B3X7=attribution-link h_01H9FCSTYR4Q1985DTHNE1M1CC=important h_01H9FCSTYR2WX0M0ZW3B22EKBM=default-postback h_01H9FCSTYSEP367WAAKCFHZT58=important-1 h_01H9FCSTYSRKBMYR2BYNQJJKVM=advanced-privacy-and-skan-postbacks h_01H9FCSTYSEJD59AWCFNXDZMYW=important-2" />
