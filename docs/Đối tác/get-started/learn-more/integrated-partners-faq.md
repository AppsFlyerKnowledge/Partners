---
title: Integrated partners—FAQ
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2021-09-02T09:33:34Z'
  edited_at: '2026-01-14T08:33:02Z'
  id: 4406549295249
  locale: en-us
  section: Learn more
  section_id: 6551121200017
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/4406549295249-Integrated-partners-FAQ
---
> **At a glance**: FAQ and integration troubleshooting for integrated partners.

## Account and dashboard

<div id="i-want-to-become-an-integrated-partner" />

<Accordion title="I want to become an integrated partner">

An advertiser should invite you to be onboarded with us.

Share <Anchor target="_blank" href="/marketers/vi/docs/set-up-an-integrated-partner#mời-các-đối-tác-mới-vào-appsflyer">this invitation procedure</Anchor> with the advertiser. After the advertiser invites you, you will receive an email with a form to fill out.  
Once the form is filled out, we will let you know the next steps.

Important: Use an email that has never been used before to create an account in AppsFlyer. Make sure the advertiser uses the same email in the invitation.

</Accordion>

<div id="how-can-i-update-my-integration" />

<Accordion title="How can I update my integration?">

Take a look at the required update <Anchor target="_blank" href="/partners/vi/docs/integration-requests-for-partners">here</Anchor> and follow the instructions provided.

If your update isn't listed, contact AppsFlyer using the <Anchor target="_blank" href="https://files.readme.io/abd47a9d733ee12aaeef473b3e243f2063034bae8919dc671e4a85e97edb0ab8-42824303168657.gif">partner assistant widget</Anchor>, include your integration PID, and describe your request.

</Accordion>

<div id="how-do-i-change-the-login-email-of-the-account" />

<Accordion title="How do I change the login email of the account?">

Follow <Anchor target="_blank" href="/partners/vi/docs/integration-requests-for-partners#create-update-partner-dashboard-login-email">these instructions</Anchor>.

</Accordion>

<div id="i-cant-add-an-app-to-the-dashboard" />

<Accordion title="I can't find or add an app to the dashboard">

If you can't add an app to the **App search** screen, verify that:

* The advertiser has added the app to their dashboard
* The advertiser has activated the app integration with your network and given you <Anchor target="_blank" href="/marketers/vi/docs/set-up-an-integrated-partner#quyền-truy-cập-mạng-quảng-cáo">relevant permissions</Anchor>.

</Accordion>

<div id="the-integration-with-the-app-isnt-active-in-the-dashboard-when-it-definitely-should-be-active" />

<Accordion title="The integration with the app isn't active in the dashboard when it definitely should be active">

| Reason | Solution |
| --- | --- |
| The integration was activated by an agency and not by the advertiser. Ad network setup is visible to ad networks only when the advertiser (app owner) configures it. | No further action is required. Once the agency activates the integration, attribution and postbacks work normally. |

</Accordion>

<div id="im-not-receiving-password-recovery-emails" />

<Accordion title="I'm not receiving password recovery emails">

1. Check your spam folder.
2. Clear the browser cache or open AppsFlyer in a different browser.
3. Try to reset your password again (wait at least 20 minutes after the previous request).
4. If you still don't receive password recovery emails, use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> to check the status of your email.

</Accordion>

<div id="how-do-i-enable-the-appsflyer-audience-integration" />

<Accordion title="How do I enable the AppsFlyer Audience integration?">

1. Get approval from the advertiser to implement the Audience integration.
2. Email the advertiser's CSM (ask the advertiser for the correct email) **and** contact AppsFlyer Partner Solutions using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
3. Once the request is approved, we will proceed with the integration.

</Accordion>

<div id="how-do-i-enable-advanced-privacy" />

<Accordion title="How do I enable Advanced Privacy postbacks?">

Follow <Anchor target="_blank" href="/partners/vi/docs/self-serve-integration-management-for-ad-networks#advanced-privacy-and-skan-postbacks">these instructions</Anchor>.

</Accordion>

<div id="Why-can-t-advertisers-find-my-account" />

<Accordion title="Why can't advertisers find my account?">

If your ad network account doesn't show on the Partner Marketplace, it could be due to incomplete integration or because the integration is still under its validation period. For additional details, review the following articles:

* <Anchor target="_blank" href="/partners/vi/docs/self-serve-integration-management-for-ad-networks?query=self%20serve">Self-serve integration management for ad networks</Anchor> (for an incomplete integration)
* <Anchor target="_blank" href="/partners/vi/docs/getting-started-onboarding-guide-for-ad-networks#integration-validation-period">Integration validation period</Anchor>

For agency accounts seeking further assistance, contact AppsFlyer via the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.

</Accordion>

<div id="why-don-t-i-see-event-data-on-the-dashboard" />

<Accordion title="Why don’t I see event data on the dashboard?">

To view event data on the dashboard, the advertiser must grant you permission to access aggregated in-app event data. If this permission hasn’t been enabled, event data won’t be displayed.

<Image alt="截屏2025-12-01 15.03.05.png" src="https://files.readme.io/3a0c4a4f28c27479b0927ab33c97a46f1ad58963424c2368fd002af38f22ae81-42824303171601.png" width="578px" />

</Accordion>

## Partner permissions

<div id="what-are-the-partner-permissions" />

<Accordion title="What are the partner permissions?">

An advertiser can grant permission to a partner to configure the integration with that partner.

Partners can test the campaign configuration when they have permission to edit and change the partner integration that the advertiser set up.

The permissions are (depending on the advertiser account):

* Integration parameter configurations
* In-app event postback configuration
* Retention reports
* Protect360 dashboard

For more information, visit the <Anchor target="_blank" href="/marketers/vi/docs/set-up-an-integrated-partner#permissions-tab">Providing permissions to ad networks</Anchor> guide.

</Accordion>

<div id="i-cant-configure-the-integration-with-the-advertiser" />

<Accordion title="I can't configure the integration with the advertiser">

| Reason | Solution |
| --- | --- |
| The advertiser did not grant you permission to configure the integration. | Request from the advertiser to make sure that the following permissions are granted to you:<ul><li>Ad network permissions (the main toggle)</li><li>Configure integration</li><li>Configuring in-app event postbacks</li></ul> |

</Accordion>

<div id="what-about-agency-permissions" />

<Accordion title="What about agency permissions?">

<Anchor target="_blank" href="/partners/vi/docs/getting-started-agency-onboarding#what-does-it-mean-to-get-permission-from-a-marketer">Read here</Anchor> about agency permissions given by a marketer.

</Accordion>

<div id="why-can-t-i-redirect-users-to-a-designated-landing-page" />

<Accordion title="Why can’t I redirect users to a designated landing page?">

The user journey prior to installing an advertised app can impact how users perceive the advertiser’s brand. For this reason, redirection to landing pages is restricted to domains that appear on the advertiser’s <Anchor target="_blank" href="/marketers/vi/docs/set-up-your-domain-redirect-allowlist">domain redirect allowlist</Anchor>.

The allowlist is managed by the advertiser. To use a specific landing page, share the page URL with your advertiser and ask them to add its domain to their allowlist.

</Accordion>

## Data - postbacks and reports

<div id="how-long-does-it-take-for-results-to-appear-in-the-dashboard" />

<Accordion title="How long does it take for results to appear in the dashboard?">

Installs appear in the dashboard within two minutes from the moment of an install.

Install and in-app data appears in reports within 15 minutes.

</Accordion>

<div id="there-are-missing-dashboard-parameters-in-the-postback" />

<Accordion title="There are missing dashboard parameters in the postback">

| Reason | Solution |
| --- | --- |
| The advertiser didn't define any value for the dashboard parameters. | <ul><li>If you have access to the application setup,<ol><li>In the AppsFlyer Dashboard, go to **Active integrations**, and click on your logo.</li><li>Under the **Integration** tab, find the relevant parameter and check its value.</li><li>If it's not defined, contact the Advertiser and ask to fill in the value.</li></ol></li><li>If you don't have the application setup, ask the Advertiser to <Anchor target="_blank" href="/marketers/vi/docs/set-up-an-integrated-partner#quyền-truy-cập-mạng-quảng-cáo">enable Ad Network Permissions</Anchor></li></ul> |

</Accordion>

<div id="servertoserver-event-data-from-the-advertiser-is-missing-or-incorrect" />

<Accordion title="Server-to-Server event data from the advertiser is missing or incorrect">

| Reason | Solution |
| --- | --- |
| The Advertiser didn't correctly configure sending S2S data to AppsFlyer. | Contact the advertiser and ask to verify the configuration. |

</Accordion>

<div id="im-not-receiving-reengagement-postbacks" />

<Accordion title="I'm not receiving re-engagement postbacks">

| Reason | Solution |
| --- | --- |
| Re-engagement postback is disabled in AppsFlyer backend | Use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> and ask to verify that re-engagement postback is enabled in AppsFlyer backend. |
| Your postback template doesn't have re-engagement identifier flag. | Use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> and ask to add the identifier if it's missing. |
| Retargeting parameter isn't included in a click attribution URL, and therefore re-attribution cannot get recorded in AppsFlyer. | Make sure the parameter `is_retargeting=true` is added to the click attribution URL. |

</Accordion>

<div id="im-not-receiving-reattribution-postbacks" />

<Accordion title="I'm not receiving re-attribution postbacks">

| Reason | Solution |
| --- | --- |
| Your postback template doesn't have the re-attribution identifier flag. | Use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> and ask to add the re-attribution identifier. |
| Retargeting parameter isn't included in a click attribution URL, and therefore reattribution cannot get recorded in AppsFlyer. | Make sure the parameter `is_retargeting=true` is added to the click attribution URL. |

</Accordion>

<div id="im-not-receiving-correct-event-identifiers-on-event-postbacks" />

<Accordion title="I'm not receiving correct event identifiers on event postbacks">

| Reason | Solution |
| --- | --- |
| Macro `(mapped-iae)` isn't integrated in the in-app event postback. | Use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> and request to integrate the macro. Include the following information:<ul><li>pid or ad network email</li><li>receiving parameter of partner event identifier</li></ul><Anchor target="_blank" href="/partners/vi/docs/postback-macros-for-ad-networks#postback-macros">More on postback macros</Anchor>. |
| Advertiser or agency didn't configure the partner event identifier correctly or at all. | If the click attribution URL contains `af_prt`<br /><br />ask the agency to check if the partner event identifier is correctly configured on their dashboard.<br /><br />If not,<br /><br />ask the advertiser to check if the partner event identifier is correctly configured on their dashboard. |

</Accordion>

<div id="i-cant-see-campaignlevel-data-for-nonattributed-traffic-on-postbacks" />

<Accordion title="I can't see campaign-level data for non-attributed traffic on postbacks">

Even if the Advertiser allows sending you postbacks for traffic attributed to all sources, AppsFlyer doesn't share with the partners the campaign-level data attributed to other partners.

</Accordion>

<div id="i-cant-export-reports" />

<Accordion title="I can't export reports">

| Reason | Solution |
| --- | --- |
| The larger the specified date range, the larger the generated file. Large files may require more time to download. | Specify a shorter time range for the report. |
| Too much browser cache can prevent the request from sending out. | Clear the browser cache and try again, or export the report from a different browser. |

</Accordion>

<div id="test-installs-dont-appear-in-the-dashboard" />

<Accordion title="Test installs don't appear in the dashboard">

To correctly perform integration tests using test apps, follow the relevant platform guide:

* <Anchor target="_blank" href="/partners/vi/docs/android-integration-testing-for-ad-networks">Android integration testing for ad networks</Anchor>
* <Anchor target="_blank" href="/partners/vi/docs/ios-integration-testing-for-ad-networks">iOS integration testing for ad networks</Anchor>

To perform an integration test with an advertised app, follow these <Anchor target="_blank" href="/partners/vi/docs/test-marketer-campaign-integration-with-the-ad-network">guidelines</Anchor> and make sure the advertiser has allowlisted the device used for testing.

</Accordion>

<div id="install-postbacks-arent-sent-to-my-servers" />

<Accordion title="Install postbacks aren't sent to my servers">

If you believe that postbacks aren't sent to your servers:

* Make sure that the postback endpoint is active
* For iOS users, ensure you’ve completed the <Anchor target="_blank" href="/partners/vi/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Advanced Privacy postback integration</Anchor>.

</Accordion>

<div id="inapp-event-postbacks-arent-sent-to-my-servers" />

<Accordion title="In-app event postbacks aren't sent to my servers">

If you believe postbacks aren’t being sent to your servers, verify the following:

* The postback endpoint is active and reachable.
* For iOS users, ensure you’ve completed the <Anchor target="_blank" href="/partners/vi/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Advanced Privacy postback integration</Anchor>.

</Accordion>

<div id="i-cant-see-the-inapp-events-postback-setup-of-agencies" />

<Accordion title="I can't see the in-app events postback setup of agencies">

Ad networks get visibility to their setup done by advertisers, **but not when it's done by agencies**. Therefore, when an agency maps in-app events for postbacks to a network, although it's active for the agency, the ad network sees this section as inactive.

> 📄 **Example**
>
> Yuval is the marketer of the **com.fused** app, which is a client app of the **Sonnet** ad network. Yuval maps the **af\_purchase** event to be sent as a postback to Sonnet when an attributed user to Sonnet performs a purchase. **Sava**, an agency permitted to work with **com.fused**, also configures **Sonnet** and maps the **af\_completeregistration** event to be sent as postback.
>
> When **Sonnet** logs into the dashboard of **com.fused**, they see only the **af\_purchase** event mapped with them, but not the **af\_completeregistration** event. However, when users attributed to **Sava** perform registrations, the **af\_completeregistration** event is sent to **Sonnet.**

</Accordion>

<div id="click-data-is-missing" />

<Accordion title="Click data is missing">

If click data is missing from postbacks, make sure that the AppsFlyer link has all the data you want to return to you in the postbacks. See our <Anchor target="_blank" href="/marketers/vi/docs/about-link-structure-and-parameters">attribution link guide</Anchor> for more information.

If the advertiser configured the ad network to receive all postbacks, postbacks for events not attributed to the ad network don't contain click data.

</Accordion>

<div id="revenue-data-is-missing" />

<Accordion title="Revenue data is missing">

If revenue data is missing or appears as N/A in the advertiser postbacks, there could be two possible reasons:

* The advertiser has decided not to share revenue data.
* The advertiser has defined the in-app event incorrectly.

</Accordion>

<div id="dashboard-data-is-missing" />

<Accordion title="Dashboard data is missing">

If your network requires credentials or keys for integration and the advertiser doesn't provide them, postbacks from AppsFlyer are rejected by your servers. Data can't be posted to your server and is therefore missing.


In this case, you'll see data in the dashboard but not in your servers. The advertiser should add any credentials, keys, or tokens in the **General Settings** section of the **Integration** tab.

Verify that the advertiser provided the necessary credentials or keys when configuring the integration with your ad network.

</Accordion>

<div id="data-from-the-advertiser-is-missing-or-incorrect" />

<Accordion title="Data from the advertiser is missing or incorrect">

If you test integration with an advertiser and no data (installs, in-app events) is available, follow the suggestions below:

* If the issue happens with any advertiser, contact your PDM
* If the issue happens with only one advertiser or a few advertisers:
  * verify with the advertiser that they implemented the AppsFlyer SDK in their app
  * verify with the advertiser that the SDK implementation is correct

</Accordion>

<div id="my-agency-account-doesnt-show-skan-data" />

<Accordion title="My agency account doesn't show SKAN data">

**Confirm that your campaign name is correct.** To view your campaigns in the Agency SKAdNetwork dashboard, campaign names configured with the SKAdNetwork should include your agency identifier, and should be structured as follows:

your *af\_prt* + underscore (\_) + your actual campaign name that follows your agency’s naming convention.

For example, if your *af\_prt* is *greatagency*, your campaign name may look like this: *greatagency\_StreamKarxxxxxx.*

<Anchor target="_blank" href="/partners/vi/docs/getting-started-agency-onboarding#skadnetwork-agency-campaigns">More information on SKAN campaigns.</Anchor>

</Accordion>

## Anti-fraud (Protect360)

<div id="how-can-i-investigate-fraud-from-appsflyer-dashboard" />

<Accordion title="How can I investigate fraud from AppsFlyer dashboard?">

You can check blocked data only if the advertiser gives you access to Protect360 and Raw Data reports.

1. Once the advertiser gives you the P360 access, you can download the blocked install/in-app events reports from the Export Data page of the dashboard. <Anchor target="_blank" href="/marketers/vi/docs/protect360-raw-data-reports#report-types">More about report types</Anchor>.
2. In Raw Data reports you can:
   * check the blocking reasons/sub-reasons
   * filter down by Site to see which SiteIDs deliver high numbers of fraud results

You can further investigate this with the publishers that deliver fraudulent traffic and make educated decisions about working with such publishers.

Learn more about <Anchor target="_blank" href="/marketers/vi/docs/protect360-anti-fraud-guide">fraud</Anchor>.

</Accordion>

<div id="why-do-clicks-and-impressions-get-capped" />

<Accordion title="Why are impressions/clicks being capped?">

AppsFlyer Protect360 evaluates multiple parameters when determining whether to apply ad engagement capping. These include, but are not limited to, the volume of impressions and clicks, conversion rate (CVR), detected anomaly rates, expected normal fluctuations in activity, and industry- and geography-specific benchmarks. The capping algorithm is dynamic and recalculated on an hourly basis to account for changing trends.

When the capping mechanism is triggered, Protect360 blocks the ad network’s impressions or clicks for the affected app for the remainder of the current 24-hour cycle. Any impressions or clicks generated after the threshold is reached are not recorded by AppsFlyer and are not eligible for attribution.

To avoid reaching the capping threshold, ad networks should pause campaigns or publishers that generate unusually high volumes of ad engagements without a corresponding impact on performance.

For more information, see:

* <Anchor target="_blank" href="/partners/vi/docs/protect360-for-integrated-partners#impression-capping">Impression and Click Capping</Anchor>
* <Anchor target="_blank" href="/partners/vi/docs/protect360-for-integrated-partners#faq">Capping FAQ</Anchor>

</Accordion>

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="Why was my test install rejected from attribution?">

AppsFlyer’s anti-fraud system evaluates installs using multiple protection layers, including analysis of individual installs and install clusters. Install clusters are reviewed across different aggregations—such as by publisher, media source, app, and are assessed using statistical models and machine-learning algorithms.

Each cluster is evaluated as a whole. If a cluster is identified as fraudulent with high statistical confidence, all installs within that cluster are classified as fraudulent, including installs that may otherwise appear legitimate. This approach is necessary because a common fraud tactic is to mix valid installs into large volumes of fraudulent activity in an attempt to dilute detection signals and bypass blocking mechanisms.

By default, all incoming installs are treated as live traffic. To prevent test installs from being evaluated by Protect360 anti-fraud algorithms, you must register your device as a test device before performing the test install.

For instructions, see <Anchor target="_blank" href="/marketers/vi/docs/registering-test-devices">Registering test devices</Anchor>.

</Accordion>

<div id="what-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="What detection methods are used to detect install rejections?">

Review the fraud sub-reason associated with the rejection to better understand why the event was blocked. This information is also available in Protect360 reports and on the Protect360 dashboard, subject to the advertiser’s access permissions.

For more details, see <Anchor target="_blank" href="/marketers/vi/docs/protect360-raw-data-reports#lý-do-bị-chặn">Protect360 blocked reasons</Anchor>.

</Accordion>

<div data-zendesk-anchors="h_01HKW6K6RFAEX8SKMAWSCKC3AD=account-and-dashboard h_01HKW6K6RF7M3YBCAE2QWDKP81=i-want-to-become-an-integrated-partner h_01HKW6K6RF4ZFY3YDW0KR1TQP2=how-can-i-update-my-integration h_01HKW6K6RF7JAC8MKMZGS8K01C=how-do-i-change-the-login-email-of-the-account h_01HKW6K6RFEDYV0T3019THZHF7=i-cant-add-an-app-to-the-dashboard h_01HKW6K6RF81BHWCAERR50QY1E=the-integration-with-the-app-isnt-active-in-the-dashboard-when-it-definitely-should-be-active h_01HKW6K6RFTBAJ1Y2HJTR3GKFD=im-not-receiving-password-recovery-emails h_01HKW6K6RFQ37XXGMVY7N3AP16=how-do-i-enable-the-appsflyer-audience-integration h_01HKW6K6RF50HWPS1E3KPYWQN0=how-do-i-enable-advanced-privacy Why-can%27t-advertisers-find-my-account%3F=Why-can-t-advertisers-find-my-account h_01HW8HSMSX2RJZQ6ABXE4WRW00=Why-can-t-advertisers-find-my-account why-don%E2%80%99t-i-see-event-data-on-the-dashboard=why-don-t-i-see-event-data-on-the-dashboard h_01KDHYCJ8W5A32MBP183F448TZ=why-don-t-i-see-event-data-on-the-dashboard h_01HW8J4Q9J83ANG3VX2T2V0JMH=partner-permissions h_01HKW6K6RFRJXJ0JF5MPJ5SKZY=what-are-the-partner-permissions h_01HKW6K6RFX8V6AFKNBJBFZAK0=i-cant-configure-the-integration-with-the-advertiser h_01HKW6K6RFJ54162BJFWAW36DJ=what-about-agency-permissions why-can%E2%80%99t-i-redirect-users-to-a-designated-landing-page=why-can-t-i-redirect-users-to-a-designated-landing-page h_01KDHYT69MCT665SQ39EY3T1ZF=why-can-t-i-redirect-users-to-a-designated-landing-page data-postbacks-and-reports=data---postbacks-and-reports h_01HKW6K6RFHBVQMMWZYCE0VWB6=data---postbacks-and-reports h_01HKW6K6RF53FWYZJDYGJ3GWA8=how-long-does-it-take-for-results-to-appear-in-the-dashboard h_01HKW6K6RGV4FJ6B0HDV0N4P37=there-are-missing-dashboard-parameters-in-the-postback h_01HKW6K6RG9Y6J5RW4AYQABX95=servertoserver-event-data-from-the-advertiser-is-missing-or-incorrect h_01HKW6K6RGV8TEJ1N6MQFMXSXX=im-not-receiving-reengagement-postbacks h_01HKW6K6RGWXBDPEFQ2T2019Y5=im-not-receiving-reattribution-postbacks h_01HKW6K6RGKQY5YS1V1PVE97ZK=im-not-receiving-correct-event-identifiers-on-event-postbacks h_01HKW6K6RGJFD51XTBBSTMAW92=i-cant-see-campaignlevel-data-for-nonattributed-traffic-on-postbacks h_01HKW6K6RG401RK36GVWGX1JNP=i-cant-export-reports h_01HKW6K6RGGD3BQR36R971C952=test-installs-dont-appear-in-the-dashboard h_01HKW6K6RGZ0F4J75RSR94S0ZP=install-postbacks-arent-sent-to-my-servers h_01HKW6K6RGR8GM3GBSNW5SE502=inapp-event-postbacks-arent-sent-to-my-servers h_01HKW6K6RGZ8J5RTYX5CZED36R=i-cant-see-the-inapp-events-postback-setup-of-agencies h_01HKW6K6RGCRPTK1B78JH94WR4=example h_01HKW6K6RGN804BA8SSTNP6SGG=click-data-is-missing h_01HKW6K6RG5HCS5XXTWJF42D89=revenue-data-is-missing h_01HKW6K6RGEYF4VZZTQW2BPMPN=dashboard-data-is-missing h_01HKW6K6RGWAEAP4YV4AWDVRKW=data-from-the-advertiser-is-missing-or-incorrect h_01HKW6K6RH18CM36N29K2QGXB7=my-agency-account-doesnt-show-skan-data protect360=anti-fraud-protect360 h_01HKW6K6RHWS457Q0DAKK0R1Q6=anti-fraud-protect360 h_01HKW6K6RHK2ZP0XHY5MWAGM42=how-can-i-investigate-fraud-from-appsflyer-dashboard h_01HKW6K6RHFV096ST796K53XQC=why-do-clicks-and-impressions-get-capped h_01KDJ4WS2ZGDM6RSCP1QHXBVJC=why-was-my-test-install-rejected-from-attribution h_01KDJ4WS2Z1CWENMY875E22QCE=what-detection-methods-are-used-to-detect-install-rejections" />
