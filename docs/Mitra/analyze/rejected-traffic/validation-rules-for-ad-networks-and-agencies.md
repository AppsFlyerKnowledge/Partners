---
title: Validation Rules for ad networks and agencies
metadata:
  keywords:
    - Agency
    - Networks
    - Validation Rules
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2017-09-18T13:53:49Z'
  edited_at: '2024-01-11T12:27:23Z'
  id: 115004751486
  locale: en-us
  section: Rejected traffic
  section_id: 6551666000273
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/115004751486-Validation-Rules-for-ad-networks-and-agencies
---
> **At a glance:** Advertisers use Validation Rules to manually define conditions to block installs, attribution, and in-app events of non-compliant installs/IAEs. Integrated partners (ad networks and agencies) can view the rules and get reports of blocked installs, attribution, and IAEs.

## About Validation Rules

Validation rules:

* Are defined by the advertiser in a rule builder using customized conditions and logic that filter and select which app installs or in-app events to keep or block.
* Are based on a variety of parameters for multiple use cases, including:
  * Untargeted installs for the advertiser's campaign (wrong geo, OS version, etc.).
  * Installs that do not meet the insertion order signed between the advertiser and you.
  * Hijacked installs by fraudulent publishers, malware, etc.
  * Fake installs or in-app events sent from bots, emulators, or device farms.
* Defined for in-app events only take effect on IAEs associated with installs that were not previously blocked.
* That include an ad network are visible to that ad network's personnel (but they cannot see other ad networks included in the rule).
* Run in real-time and take immediate action. A rejection postback is sent to partners who have rejected postbacks set up. <Anchor target="_blank" href="/partners/id/docs/rejected-attribution-postbacks-to-integrated-partners">Learn more</Anchor>.
* Have additional options available to <Anchor target="_blank" href="/marketers/id/docs/protect360-anti-fraud-guide">Protect360</Anchor> customers, on top of the automatic Protect360 fraud blocking and detection. These conditions are known to help in the detection of various install-hijacking, fake install, and fake in-app event fraud types.

## Availability to ad networks and agencies

The rules governing validation rule access to ad networks and agencies are as follows:

* Integrated partners can see the list of validation rules that apply to them.
  * They see that other partners are included in the rule, although the other partner names are undisclosed.
  * If a validation rule applies to multiple apps but a partner is only integrated for one or some of the apps, it can only see the rule and the app for which it's integrated.
* To click a specific rule and view its details requires permission from the advertiser to **View validation rules**.
  * By default, the permission is turned off.
  * If off, a partner can click **Request access**. The advertiser then receives a notification of the request.
* An ad network can't create or edit rules.

### Agencies

The rules governing additional validation rule access to agencies are as follows:

* Agencies can create, edit, and delete rules, if they have permission from the advertiser to **Add validation rules**.
  * Agencies can only edit or delete rules they create, not those created by the advertiser.
* To add rules with Protect360 conditions:
  * The advertiser needs to have a Protect360 subscription.
  * Permission is needed from the advertiser to **Access Protect360 dashboard & raw data**.
* If an agency makes a rule for multiple apps it is integrated with, and then integration for one or more apps is removed by the advertiser, the rule is split into separate rules for each app, and the rules for the apps that aren't integrated are inactive.

**To access Validation Rules**:

1. In AppsFlyer, from the side menu, select **Settings** > **Validation Rules**.
2. To view the validation rule, select an **app owner Account**.
   * The list of rules defined by the app owner account for traffic that could come from you is displayed.
   * For an explanation of how rulesets work see <Anchor target="_blank" href="/marketers/id/docs/implement-validation-rules-to-prevent-fraud">Validation Rules for app owners</Anchor>.

## Reports

### Protect360 fraud: export data

Advertisers can give partners (ad networks and agencies) <Anchor target="_blank" href="/marketers/id/docs/raw-data-reporting-overview#protect360-fraud-and-validation-rules">permission</Anchor> to download the following reports from **Reports** > **Export data**:

* Installs: Blocked installs or installs with blocked attribution.
* Blocked in-app events: Rejected in-app events (requires the advertiser to have a Protect360 subscription).
* Blocked install postbacks: A single report of the rejection postbacks sent to you in real-time.

The **Blocked Reason** and **Blocked Reason Value** fields are populated in the reports. The **Blocked Reason Value** includes the rule name that caused the rejection.

## Validation Rules rejected installation postbacks

Integrated partners who integrate with AppsFlyer can <Anchor target="_blank" href="/partners/id/docs/rejected-attribution-postbacks-to-integrated-partners">receive blocked install postbacks</Anchor> in real-time each time an install is rejected due to enforcement of the rules.

Contact your Partner Development representative for further details.

<div data-zendesk-anchors="h_01HKA04414ZAS0EZX6AGHVTZHY=about-validation-rules h_01HKA04415K37N997EDS8X26PK=availability-to-ad-networks-and-agencies h_01HKA044155S4Y7DAGP05S5FJA=agencies h_01HKA04415P5K6J4VXS64GA2SP=reports h_01HKA0441501DKTQHT3X0G0RC7=protect360-fraud-export-data h_01HKA04415BR5XJABRHSWYTTS7=validation-rules-rejected-installation-postbacks" />
