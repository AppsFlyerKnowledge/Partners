---
title: Android integration testing for ad networks
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
  created_at: '2021-12-06T10:35:58Z'
  edited_at: '2026-10-13T01:48:49Z'
  id: 4412945443857
  locale: zh-cn
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/zh-cn/articles/4412945443857
---
> **At a glance:** Test your AppsFlyer Android integration using the AppsFlyer Partner Integrations app to trigger postbacks.

## Android integration testing

Testing consists of the following elements:

* Use the Android version of the AppsFlyer Partner Integrations app to generate test install and purchase in-app events. These tests, in turn, trigger postbacks sent to your endpoints. You also have the option to test login and registration in-app events.
* On receipt of the postbacks, verify that you are able to ingest them.

**Testing scope**

The following table lists test scenarios according to the setting combinations available.

For each scenario, you can test installs and in-app events. For in-app events, you can use <Anchor target="_blank" href="/partners/zh/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">in-app event mapping</Anchor> to map advertiser events to your events.

## Testing

Complete the prerequisites and then perform the test procedures in the sections that follow. The test sections each contain a table you can use to record your test results.

<div id="prerequisites" />

<Accordion title="Prerequisites">

Complete the prerequisites before beginning to execute the test procedure.

| Prerequisites |
| --- |
| <Anchor target="_blank" href="/partners/zh/docs/turn-on-test-app-integration-for-ad-networks">Integrate the Android test app into your account.</Anchor> |
| Verify that the test app is integrated into your account |
| <Anchor target="_blank" href="/partners/zh/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Map in-app events to your event names</Anchor>. Event names to be mapped: `purchase`, `login`, `registration` |
| <Anchor target="_blank" href="/partners/zh/docs/ios-integration-testing-for-ad-networks#attribution-link">Prepare attribution link</Anchor> |
| Test install attribution using a device running Android |
| Test in-app event attribution using an Android device |
| Test retargeting attribution using an Android device |

</Accordion>

<div id="test-install-attribution" />

<Accordion title="Test install attribution">

**To trigger postbacks:**

1. Send the attribution link previously prepared to a test device.
2. Click on the link, install and then open the app.  
   The **Install Data** page displays.
3. Validate the attribution using the following parameters. If the validation fails, see <Anchor target="_blank" href="/partners/zh/docs/ios-integration-testing-for-ad-networks#troubleshooting">Troubleshooting</Anchor>.

   1. `install_time`: near the current time. Time is in UTC.
   2. `af_status: Non-organic` If this is not the case, the install was not attributed.
   3. `media_source`: your ad network
4. Tap **In-App Event Tests.**
5. Tap **Purchase Event.**  
   The Purchase Event confirmation displays.
6. Verify that:
   1. You received install and purchase postbacks.
   2. The event name is mapped correctly (if you mapped in-app events).
   3. You are able to ingest the postback.

</Accordion>

## Supplementary information and procedures

<div id="about-the-partner-integrations-test-app" />

<Accordion title="About the Partner Integrations test app">

The Partner Integrations app is available in Google Play. The app sends install and in-app events to the AppsFlyer platform.

When the app is opened for the first time, the **Install Data** page displays the conversion data recorded in the AppsFlyer platform. Test in-app events are triggered in the user interface.

The following functions are available:

* **In-App Event Tests**  
  Send `purchase`,`login`, and `registration` and in-app events. By mapping the app in-app event names to your event names, postbacks are populated using your event names.

</Accordion>

<div id="attribution-link" />

<Accordion title="Attribution link">

Prepare an attribution link in the AppsFlyer dashboard, using one of the following methods:

* Generate the link in the AppsFlyer dashboard.
* Edit the example link that follows.

**To generate a link in the dashboard:**

1. In AppsFlyer, from the top menu, select to **My Apps**.
2. Select **adNetworkTest**.
3. In AppsFlyer, from the side menu, select **Collaborate** > **Active Integrations** > select your ad network > **Attribution link** tab.
4. In the Attribution link tab, set the parameters listed. You can add additional parameters if required. Link to attribution linkd 

| Parameter | Example value | Remark |
| --- | --- | --- |
| <span id="campaign"></span>Campaign | c-test-2020-12-20 | Set a value that is identifiable in your postbacks |
| <span id="pid"></span>PID | pitestap |  |

5. Copy the resulting link for later use.

**Example attribution link:**

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Test app integrated in your account">

**To verify that the test app is available in your account:**

1. In AppsFlyer, from the top menu, go to **My Apps**.
2. Verify that the app **Partner Integrations adNewtorkTest** displays under Available Apps. If this is not the case, contact your Partner Development Manager.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Troubleshooting">

| Symptom | Cause/corrective action |
| --- | --- |
| The install time is not the current time | The app was not deleted before the install.<br /><br />Delete the app and repeat the procedure. |
| The media source is not your media source | Verify that you have set the correct **pid** value on the attribution link. Verify that you are using the correct attribution link |
| af\_status is Organic | Check the format of the attribution link, especially the value of **pid**. |

</Accordion>

<div id="test-retargeting-attribution" />

<Accordion title="Test retargeting attribution">

You can also test retargeting attribution. The process is almost the same except for one parameter that you add to the attribution link.

Generate a new attribution link and add the parameter `is_retargeting=true` to it.

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_click_lookback=7d
          &clickid={clickid}&is_retargeting=true
```

Install the app using the retargeting link. The flow is the same as described in [testing install attribution](/docs/android-integration-testing-for-ad-networks#test-install-attribution).

### Viewing retargeted installs in the dashboard

Access your AppsFlyer dashboard and click on **Re-targeting** in the left-side menu. Allow up to 30 minutes for the retargeted install to appear in the dashboard.

<Image align="center" alt="com_appsflyer_adNetworkTest-retargeting.png" src="https://files.readme.io/e46789b004be2f4fc15f095ba11a0f3f5d03abb1240e54e4b534285e3e4efd8d-21266228899601.png" />

</Accordion>

<div id="test-viewthrough-attribution" />

<Accordion title="Test view-through attribution">

1. In AppsFlyer, go to **My Apps**.
2. Select **adNetworkTest**.
3. In AppsFlyer, from the side menu, select **Collaborate** > **Active Integrations** > select your ad network > **Integration** tab.
4. Make sure that **Enable view-through attribution** is ON.
5. Copy the Impression attribution link.

   ```http
   https://impression.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_viewthrough_lookback=24h&advertising_id=YOUR_GAID&af_siteid=YOUR_SITEID
   ```

   Replace the parameters as follows:

   * YOUR\_PID - your partner ID supplied by AppsFlyer (ending with *\_int*)
   * YOUR\_CAMPAIGN - any campaign name
   * YOUR\_GAID - your Google Advertising ID
   * YOUR\_SITEID - any site ID

   Note: the parameters in the link are the basic parameters used here for the purpose of testing. You can have other parameters in the view-through attribution link according to your requirements.
6. Send the view-through attribution link to the test device.
7. Open the link in the browser and install the app from the store.
8. Launch the app.  
   The following screen displays:

   <Image align="center" alt="vta-testing-postback.png" src="https://files.readme.io/88b6720928d7540eeb2fe8f42f39ecdccc04655aa49f95d08dba5741d5e39982-4831106525457.png" />

   If you don't see this message, make sure that the view-through attribution link is formatted correctly. Uninstall the app and reinstall using the view-through attribution link with the new test device.

Tip

For more elaborate results, repeat the installation process using the view-through attribution link with the new test device. Uninstall the app, change the parameters in the link (the campaign name, af\_siteid, and advertising\_id), and install again by clicking the URL.

### View installs in the dashboard

Once you install and launch the app, you can see the results in your AppsFlyer dashboard.

Allow up to 30 minutes for the install to appear in the app dashboard.

</Accordion>

<div id="raw-data-export" />

<Accordion title="Raw data export">

Data related to apps whose install is attributed to your ad network can be exported in CSV format.

The data includes the following:

* Installs
* In-app events
* Retargeting installs
* In-app events of apps installed from retargeting campaigns

**To export raw data**:

1. In AppsFlyer go to, **Report** > **Raw data export**.
2. Select the date range.
3. Select a report.  
   The report downloads within a few minutes.

</Accordion>

<div id="verify-postback-data" />

<Accordion title="Verify postback data">

Every install generates a postback that is sent to your servers. To verify the postback URL, its structure, and the parameters that are appended to it, export the **Installation postbacks** report.

The **Installation postbacks** report contains a column titled **Postback URL**. This column lists the postback URLs as generated for each and every install.

Review the data in that column to verify the following:

* The URL endpoint is the correct one
* The parameters appended to the URL correspond to those appended to the AppsFlyer attribution link
* The **Postback Error Message** column is empty

</Accordion>

<div data-zendesk-anchors="h_01HJR6V0MYJXD4QSRT95SVXTWH=android-integration-testing h_01HJR6V0MYBPC3CSAJTTQSWGAR=testing h_01HJR6V0MYG42PPWXT7H2AGTAE=prerequisites h_01HJR6V0MYDRZGQQ74TJWDJ2WS=test-install-attribution h_01HJR6V0MYZ5NG21FEKB4HY6HT=supplementary-information-and-procedures h_01HJR6V0MYTZCS097RQP9HG7GY=about-the-partner-integrations-test-app h_01HJR6V0MYVCNVHNCPZ29KRA4K=attribution-link h_01HJR6V0MY6JZXP2NX9YJ9ZY2T=test-app-integrated-in-your-account h_01HJR6V0MYWK7WAAFHRYPCVM7N=troubleshooting h_01HJR6V0MY2SSP17ZEWRM3NXKE=test-retargeting-attribution h_01HJR6V0MYPC0AZF05YF32Z571=viewing-retargeted-installs-in-the-dashboard h_01HJR6V0MY027J9PKXZZ4TCXRX=test-viewthrough-attribution h_01HJR6V0MZ4VA3V8CA3PN5Z31K=view-installs-in-the-dashboard h_01HJR6V0MZCZ3E8NCR6DG6P6P1=raw-data-export h_01HJR6V0MZAHSXCTEZKTVWM96V=verify-postback-data" />
