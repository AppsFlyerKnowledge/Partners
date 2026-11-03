---
title: iOS integration testing for ad networks
metadata:
  keywords:
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
  created_at: '2020-12-16T11:39:36Z'
  edited_at: '2026-10-13T01:48:57Z'
  id: 360016588278
  locale: zh-cn
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/zh-cn/articles/360016588278
---
> **At a glance:** Test your AppsFlyer iOS integration using the AppsFlyer Partner Integrations app to trigger regular and Advanced Privacy postbacks.

## iOS integration testing

Testing consists of the following elements:

* Use the iOS version of the AppsFlyer Partner Integrations app to generate test install and purchase in-app events. These tests, in turn, trigger postbacks sent to your endpoints. You also have the option to test login and registration in-app events.
* On receipt of the postbacks, verify that you are able to ingest them.

### Testing scope

Advertisers control the data shared with ad networks via the Advanced Privacy setting. This setting, in conjunction with the app user <Anchor target="_blank" href="/marketers/zh/docs/att-implications-ios-14-and-deprecation-of-lat">ATT</Anchor> setting, impacts the postback type and the data shared with ad networks, as described in the <Anchor target="_blank" href="/partners/zh/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Advanced Privacy postback guide</Anchor>. The following table lists test scenarios according to the setting combinations available.

For each scenario, you can test installs and in-app events. In regards to in-app events, you can use <Anchor target="_blank" href="/partners/zh/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">in-app event mapping</Anchor> to map advertiser events to your events.

#### Test scenario combinations

| Scenario | Advanced Privacy setting | ATT setting in the app | Postback type sent |
| --- | --- | --- | --- |
| A | Off | Allow | Regular |
| B | On | Ask app not to track | Advanced Privacy |

## Testing

Complete the prerequisites and then perform the test procedures in the sections that follow. The test sections each contain a table you can use to record your test results.

<div id="prerequisites" />

<Accordion title="Prerequisites">

Complete the prerequisites before beginning to execute the test procedure.

| Prerequisites |
| --- |
| <Anchor target="_blank" href="/partners/zh/docs/getting-started-onboarding-guide-for-ad-networks#第一部分对接与测试">Complete standard integration with AppsFlyer.</Anchor> If necessary, contact AppsFlyer using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>. |
| <Anchor target="_blank" href="/partners/zh/docs/self-serve-integration-management-for-ad-networks#高级隐私保护和skan回传">Complete Advanced Privacy integration with AppsFlyer.</Anchor> If necessary, contact AppsFlyer using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>. |
| <Anchor target="_blank" href="/partners/zh/docs/turn-on-test-app-integration-for-ad-networks">Integrate the iOS test app into your account.</Anchor> |
| [Verify that the test app is integrated into your account](/docs/ios-integration-testing-for-ad-networks#test-app-integrated-in-your-account) |
| <Anchor target="_blank" href="/partners/zh/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Map in-app events to your event names</Anchor>. Event names to be mapped: `purchase`, `login`, `registration` |
| [Prepare attribution link](/docs/ios-integration-testing-for-ad-networks#attribution-link) |
| Test using a device running iOS 14.5+ |

</Accordion>

<div id="test-advanced-privacy-off" />

<Accordion title="Test—Advanced Privacy off">

**To trigger postbacks:**

1. On the AppsFlyer dashboard, set [Enable Advanced Privacy](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy) to off.
2. On the device:
   1. Verify that the test app is not installed. Delete it if necessary.
   2. In Privacy settings, verify that **Allow Apps to Request to Track** is on.  

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Send the attribution link to the test device.
4. Open the attribution link in the device browser.  
   You are redirected to the App Store.
5. Download and open the app.  
   The ATT consent dialogue displays.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Tap **Allow**.  
   The **Install Data** page displays.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Tap **ATT Status**.  
   The **Authorized** status displays.
8. Validate the attribution using the following parameters. If the validation fails, see [Troubleshooting](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: near the current time. Time is in UTC.
   2. `af_status: Non-organic` If this is not the case, the install was not attributed.
   3. `media_source`: your ad network
9. Tap **In-App Event Tests.**

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Tap **Purchase Event.**  
    The Purchase Event confirmation displays.
11. Verify that:
    1. You received install and purchase postbacks.
    2. The event name is mapped correctly (if you mapped in-app events).
    3. You are able to ingest the postback.

#### Advanced Privacy off—Test results

| Postback | Time you triggered the event | Expected postback type | Actual postback received (pass/fail) | Postback validation (pass/fail) |
| --- | --- | --- | --- | --- |
| Install |  | Regular |  |  |
| In-app event: Purchase |  | Regular |  |  |

</Accordion>

<div id="test-advanced-privacy-on" />

<Accordion title="Test—Advanced Privacy on">

**To trigger postbacks:**

1. On the AppsFlyer dashboard, set [Enable Advanced Privacy](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy) to on.
2. On the device:
   1. Verify that the test app is not installed. Delete it if necessary.
   2. In Privacy settings, verify that **Allow Apps to Request to Track** is on.

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Send the attribution link to the test device.
4. Open the attribution link in the device browser.  
   You are redirected to the App Store.
5. Download and open the app.  
   The ATT consent dialogue displays.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Tap **Ask App not to Track.** The **Install Data** page displays.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Tap **ATT Status**.  
   The **Denied** status displays.
8. Validate the attribution using the parameters listed. If validation fails, see [Troubleshooting](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: near the current time. Time is in UTC.
   2. `af_status: Non-organic` If this is not the case, the install was not attributed.
   3. `media_source`: your ad network
9. Tap **In-App Event Tests.**

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Tap **Purchase Event.**
11. Verify that:
    1. You received install and purchase postbacks.
    2. The event name is mapped correctly (if you mapped in-app events).
    3. You are able to ingest the postback.

#### Advanced Privacy on—Test results

| Postback | Time you triggered the event | Expected postback type | Actual postback received (pass/fail) | Postback validation (pass/fail) |
| --- | --- | --- | --- | --- |
| Install |  | Advanced Privacy |  |  |
| In-app event: Purchase |  | Advanced Privacy |  |  |

</Accordion>

## Supplementary information and procedures

<div id="about-the-partner-integrations-test-app" />

<Accordion title="About the Partner Integrations test app">

The Partner Integrations app is available in the App Store. The app sends install and in-app events to the AppsFlyer platform.

When the app is opened for the first time, the iOS **request to track** dialogue displays, followed by the **Install Data** page displaying the conversion data recorded in the AppsFlyer platform. Test in-app events are triggered in the user interface.

[<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)

The following functions are available:

* **In-App Event Tests**Send `purchase`,`login`, and `registration` and in-app events. By mapping the app in-app event names to your event names, postbacks are populated using your event names.
* **ATT Status**Returns the current ATT status reported by iOS as **Authorized** or **Denied**. The ATT status depends on user agreement to track in the ATT consent dialogue and the device **Allow Apps to Request to Track** setting.

</Accordion>

<div id="attribution-link" />

<Accordion title="Attribution link">

Prepare an attribution link in the AppsFlyer dashboard, using one of the following methods:

* Generate the link in the AppsFlyer dashboard.
* Edit the example link that follows.

**To generate a link in the dashboard:**

1. In AppsFlyer, go to **My Apps**.
2. Select **id1543229303**.
3. From the side menu, select **Collaborate** > **Active Integrations** > select your ad network > **Attribution link** tab.
4. In the Attribution link tab, set the parameters listed. You can add additional parameters if required. 

| Parameter | Example value | Remark |
| --- | --- | --- |
| Campaign | c-test-2020-12-20 | Set a value that is identifiable in your postbacks |

5. Copy the resulting link for later use.

**Example attribution link:**

```http
https://app.appsflyer.com/id1543229303?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="set-advanced-privacy" />

<Accordion title="Set Advanced Privacy">

<Image alt="AdvancedPrivacyOff.png" src="https://files.readme.io/ef845ea74cbaa0d3214e61c6e2229fd4b9026d0e221b19fecb9e3486e9b795eb-360014980157.png" width="357px" />

**To change the Enable Advanced Privacy setting:**

1. In AppsFlyer, go to **My Apps**.
2. Select app id1543229303.
3. From the side menu, select **Collaborate** > **Active Integrations** > select your ad network > **Integration** tab.
4. Set **Enable Advanced Privacy** to the appropriate setting for each test scenario.
5. Click **Save Integration**.

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Test app integrated in your account">

**To verify that the test app is available in your account:**

1. In AppsFlyer, go to **My Apps**.
2. Verify that the app **Partner Integrations id1543229303** displays under Available Apps. If this is not the case, contact your Partner Development Manager.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Troubleshooting">

| Symptom | Cause/corrective action |
| --- | --- |
| The install time is not the current time | The app wasn't deleted before the install.<br /><br />Delete the app and repeat the procedure. |
| The media source is not your media source | Verify that you have set the correct **pid** value on the attribution link. Verify that you are using the correct attribution link |
| af\_status is Organic | Check that the device iOS version is in accordance with that stated in the prerequisites.<br /><br />Check the format of the attribution link, especially the value of **pid**. |

</Accordion>

<div data-zendesk-anchors="h_01HJR5YDW9ENA1B1AC1DQVX8SF=ios-integration-testing h_01HJR5YDW92MXP9DDBX9C1928V=testing-scope h_01HJR5YDW9Q7B10MXB1V4AKH2D=test-scenario-combinations h_01HJR5YDW9AGY148E1ZD97JFRB=testing h_01HJR5YDW9SGN9KH63CPZ54RM5=prerequisites test%E2%80%94advanced-privacy-off=test-advanced-privacy-off h_01HJR5YDWA20EQT5RE1EJ7QK2X=test-advanced-privacy-off advanced-privacy-off%E2%80%94test-results=advanced-privacy-offtest-results h_01HJR5YDWAEAR22NPXF8ZD5QX6=advanced-privacy-offtest-results test%E2%80%94advanced-privacy-on=test-advanced-privacy-on h_01HJR5YDWAY6B55BFQ1B0WJEHR=test-advanced-privacy-on advanced-privacy-on%E2%80%94test-results=advanced-privacy-ontest-results h_01HJR5YDWAK3DZ1Q0W3TSR7ZKZ=advanced-privacy-ontest-results h_01HJR5YDWA74Q46F6XKY5J375C=supplementary-information-and-procedures h_01HJR5YDWASJWC1NGNABWR1VW5=about-the-partner-integrations-test-app h_01HJR5YDWA0WXWN5B5VNPK40FY=attribution-link h_01HJR5YDWA73BQB478D6N0R8GP=set-advanced-privacy h_01HJR5YDWAGZ5XMQJG1KX3J6CP=test-app-integrated-in-your-account h_01HJR5YDWAXRD7DVHTZPJCFM56=troubleshooting" />
