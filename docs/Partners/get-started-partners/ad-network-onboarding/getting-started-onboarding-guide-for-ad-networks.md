---
title: Getting started—onboarding guide for ad networks
excerpt: >-
  Complete integration with AppsFlyer by setting up and testing your attribution
  link and postback integrations. Understand the steps, timelines, and
  dependencies of the process.
metadata:
  keywords:
    - Ad Network
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  created_at: '2019-03-28T08:41:59Z'
  edited_at: '2025-11-13T10:20:40Z'
  id: 360001300998
  locale: en-us
  section: Ad network onboarding
  section_id: 6551058566033
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360001300998-Getting-started-onboarding-guide-for-ad-networks
---
![AdNetworks_-_Onboarding__2_.png](https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png)

## What is AppsFlyer?

AppsFlyer, a leader in mobile attribution, welcomes you as our ad network integrated partner. This article is for ad networks that have completed AppsFlyer partner registration. If you want to register as a partner, you must ask an [AppsFlyer customer (advertiser) to invite you to do so.](/appsflyer-marketers/docs/set-up-an-integrated-partner#invite-new-partners-to-appsflyer)

## Ad network onboarding

The steps required to integrate and the estimated time to complete them are listed in the **Onboarding steps** section of this article.

Integration means that:

* AppsFlyer records your engagements (clicks and impressions). The engagements are attributed according to the [AppsFlyer attribution model](/appsflyer-marketers/docs/appsflyer-attribution-model).
* Postbacks of the format required by you are sent to your endpoints.
* You can access AppsFlyer features like click signing, Protect360, Data Locker, and so on.

<div id="if-you-need-help" />

<Accordion title="If you need help">

* Look at the partner [FAQ](/docs/integrated-partners-faq)
* Consult the [Integration change requests](/docs/integration-requests-for-partners) article

</Accordion>

Consider:

* Time estimates in this article are based on our experience working with ad networks. Each integration is slightly different, so the actual times can vary.
* AppsFlyer supports many [performance platforms](/docs/platforms-for-ad-networks). If you use one of the platforms on the list, you must review platform-specific instructions before integrating.

## Onboarding steps

**To integrate with AppsFlyer**:

1. [Complete part 1—integration and testing.](/docs/getting-started-onboarding-guide-for-ad-networks#part-1-integration-and-testing)
2. [Complete part 2—testing with advertiser apps.](/docs/getting-started-onboarding-guide-for-ad-networks#part-2-test-using-advertiser-apps)
3. [Complete part 3—use AppsFlyer dashboard and reporting tools.](/docs/getting-started-onboarding-guide-for-ad-networks#part-3-appsflyer-dashboard-and-reporting-options)

### Part 1: Integration and testing

<table><thead><tr><th>Action</th><th>Minutes required</th></tr></thead><tbody><tr><td>Wait for your registration approval email inviting you to complete the mandatory integration steps.</td><td>--</td></tr><tr><td colspan="2"><strong>Mandatory integration steps</strong> </td></tr><tr><td><a href="./self-serve-integration-management-for-ad-networks#attribution-link">Specify your attribution link</a>: Attribution links are URLs with macros. These macros are populated by you with actual values and sent to AppsFlyer each time a user clicks on a link. <br/>Note! If you use a performance network platform supported by AppsFlyer, you must consider the platform-specific instructions provided. See <a href="./platforms-for-ad-networks">Performance network guides.</a></td><td>60</td></tr><tr><td><a href="./self-serve-integration-management-for-ad-networks#default-postback">Specify postback macros</a>: Postbacks are URLs containing macros populated by AppsFlyer and sent to your servers in real-time after each conversion.</td><td>60</td></tr><tr><td>Log in to the <a href="https://hq1.appsflyer.com/auth/login">AppsFlyer dashboard</a> using the credentials provided. </td><td> </td></tr><tr><td><p>Upload your company logo. Your logo must have the format 200 X 50 transparent PNG. </p><ol><li>In AppsFlyer, in the menu bar, select your email address &gt; <strong>Partner Setup</strong>. </li><li>On the <strong>Profile</strong> tab, upload your company logo. </li><li>Click <strong>Save</strong>.</li></ol></td><td>5</td></tr><tr><td><p>Test the integration using AppsFlyer test apps:</p><ul><li><a href="./android-integration-testing-for-ad-networks">Android</a></li><li><a href="./ios-integration-testing-for-ad-networks">iOS</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>Optional integration steps</strong></td></tr><tr><td>[iOS] If your advertisers require AppsFlyer Aggregated Advanced Privacy, complete <a href="./self-serve-integration-management-for-ad-networks#advanced-privacy-and-skan-postbacks">Advanced Privacy</a> integration.</td><td>60</td></tr><tr><td>[iOS] If you run SKAdNetwork campaigns, complete<a href="./self-serve-integration-management-for-ad-networks#advanced-privacy-and-skan-postbacks"> SKAdNetwork integration.</a></td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>Authorized agencies</strong></h4><p>Create and manage a list of agencies you approve to run campaigns through your network integration. This is done by entering their agency ID (af_prt) in the <a href="./set-up-your-list-of-authorized-agencies"><strong>Authorized agencies</strong></a> section of the Security center. To obtain the agency ID, the agency must contact you and provide it.</p></td><td>2</td></tr><tr><td colspan="2"><p><strong>Optional features and considerations</strong><br/> </p><p>Consider implementing integrations and options based on advertiser requirements.</p></td></tr><tr><td>To make sure that fraudulent clicks aren't sent using your partner identifier, implement <a href="./click-signing-for-ad-networks">click signing.</a></td><td>60+</td></tr><tr><td>For advertisers that implement Protect360 or validation rules, add <a href="./postback-macros-for-ad-networks#macrosinstalls-in-app-events-and-rejected-events">rejected attribution postbacks</a>.</td><td>15</td></tr><tr><td>Send cost to AppsFlyer by API. See <a href="./incost-api-for-ad-networks">InCost API</a>.</td><td>60+</td></tr><tr><td><a href="./retargeting-attribution-guide">Retargeting integration</a>.</td><td>15</td></tr><tr><td><a href="./measure-view-through-engagements">View-through attribution integration</a>.</td><td>15</td></tr></tbody></table>

### Part 2: Test using advertiser apps

In this part, you'll be testing your integration using an app that belongs to an advertiser. As such, you must contact the advertiser and ask them to complete some of the steps in this part. In this part, regard references to advertisers can also mean agencies if they are acting on behalf of an advertiser.

| Performed by | Action | Minutes required |
| --- | --- | --- |
| Advertiser | Turn on [activate partner.](/appsflyer-marketers/docs/set-up-an-integrated-partner#integration-tab)<br /><br />When on, AppsFlyer considers engagements brought by you as candidates for attribution. | 2 |
| Advertisers | Grant [ad network permissions*](/appsflyer-marketers/docs/set-up-an-integrated-partner#ad-network-permissions)and add your team members.<br /><br />When on, app performance data is available in your AppsFlyer dashboard. Only listed team members can access the data. | 2 |
| Ad network | [Add team members to your account](/appsflyer-marketers/docs/user-management#creating-users). | 2 |
| Advertiser (admin) | [Register your test devices](/appsflyer-marketers/docs/registering-test-devices). Ask the advertiser to do this on your behalf. | 3 |
| Ad networks | [Test the integration using advertiser apps.](/docs/test-marketer-campaign-integration-with-the-ad-network) | 60 |

### Part 3: AppsFlyer dashboard and reporting options

| Option |
| --- |
| [Use the partner dashboard](/docs/integrated-partners-dashboard). |
| Get aggregated performance data via cloud storage with [Data Locker](/docs/data-locker-for-partners) for ad networks. |
| Get Protect360 [raw data.](/appsflyer-marketers/docs/raw-data-export-page) |

## Integration validation period

To ensure the integrity of the AppsFlyer ecosystem and protect internal systems from invalid traffic, all new ad network integrations undergo a validation period. During this period, AppsFlyer thoroughly verifies the traffic and evaluates its quality before making the integration available to other advertisers in the [Marketplace](/appsflyer-marketers/docs/partner-integrations). Ad network integrations that don’t meet high-quality traffic criteria will face removal.

### Validation period—FAQ

| **Question** | **Answer** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>Why can’t advertisers find me in the Marketplace even though I've completed the integration? | During the validation period, your integration is visible only to the advertiser who referred you. After we've validated your traffic quality, you'll receive an email letting you know that your integration is available to all advertisers. |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>What can I do to make sure my integration will be approved? | Deliver a significant volume of high-quality traffic for the advertiser who referred you. |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>When should I expect to receive the validation completion email? | After we've been able to validate enough traffic, you'll receive an email notifying you that the validation period has ended. |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>Can I know the current status of my validation evaluation? | You'll know only when the validation period has ended, after receiving an email notification. |
| <span id="what-are-the-validation-criteria-based-on"></span>What are the validation criteria based on? | Validation criteria are based on [Protect360](/appsflyer-marketers/docs/protect360-anti-fraud-guide) dynamic machine learning algorithms. Factors such as traffic quality, volume, and data validity overall are considered, combined with industry best practices. |
| <span id="another-adviertiser-wants-to-work-with-me"></span>What if another advertiser wants to start working with me during my validation period? | During the validation period, your integration is visible only to the referring advertiser. Other advertisers will be able to work with you after your validation period has ended successfully. |
| <span id="my-integration-fails"></span>What happens if my integration fails the validation? | The validation period may be extended to monitor for improvements in traffic quality, or your integration may be permanently removed from the AppsFlyer platform. You'll get notified in either case. |

<div data-zendesk-anchors="h_01J09255QNBFRV8DYZPGG990A0=what-is-appsflyer h_01J09255QN61VPW292PC2CH9KN=ad-network-onboarding h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help h_01J09255QNZ9QXXFB54YRYCM8P=onboarding-steps h_01J09255QN35ZBKE2R2HDDZWSZ=part-1-integration-and-testing h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies h_01J09255QP11XJD3C83VZZXXQZ=part-2-test-using-advertiser-apps h_01J09255QPSSD8CF0HR059RWXZ=part-3-appsflyer-dashboard-and-reporting-options h_01J09255QP82ZYZDJMA74SRYGZ=integration-validation-period validation-period%E2%80%94faq=validation-periodfaq h_01J09255QP77BME57P9B7S222V=validation-periodfaq" />
