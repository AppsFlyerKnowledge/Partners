---
title: Test marketer campaign integration with the ad network
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
  created_at: '2021-12-08T04:41:04Z'
  edited_at: '2024-01-16T09:44:09Z'
  id: 4413093220113
  locale: en-us
  section: Ad network integration testing
  section_id: 6551070667537
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/4413093220113-Test-marketer-campaign-integration-with-the-ad-network
---
> **At a glance**: Test ad network integration using marketer apps.

<div id="prerequisites" />

## Prerequisites

Before you can start testing the marketer's integration with your ad network, there are a few requirements:

* Allowlist devices: you need to ask the marketer to <Anchor target="_blank" href="/marketers/docs/registering-test-devices">allowlist</Anchor> any devices that you use for testing
* The app should include the AppsFlyer SDK
* If the app is not live on Google Play or the iOS App Store, you need to ask the marketer to provide you with the app
* Whether or not the app is live, it must be <Anchor target="_blank" href="/marketers/docs/adding-an-app-to-appsflyer">in the marketer's AppsFlyer account</Anchor>

<div id="getting-started" />

## Getting started

Open your AppsFlyer Dashboard. In the **App search** screen, enter the marketer's app ID:

<div id="example" />

> 📄 **Example**
>
> Android - **com.example.app**
>
> iOS- **id1234123412**

Once the green tick appears in the input field, click on the blue arrow. Clicking the arrow opens the app's dashboard.

<Image align="center" alt="partner-app-search.png" src="https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png" />

<div id="testing-live-apps" />

## Testing live apps

In the AppsFlyer dashboard for your app, from the side menu, select, **Active integrations**. Choose your ad network and click on **Attribution link**.

<div id="important" />

> 🚧 **Important!**
>
> If the options under **Attribution link** are grayed out, ask the marketer to <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">enable ad network permissions</Anchor>. The required permissions are **Allow to configure integration** and **Allow to configure in-app events postbacks**.
>
> Alternatively, you can ask the marketer to provide you with the attribution link.

<div id="installing-the-app-through-the-attribution-link" />

<Accordion title="Installing the app through the attribution link">

Now you can generate an attribution Link to test install attribution.

Add parameters to the attribution link according to your requirements and the data that you want to record.

<Image align="center" alt="partner-configure-attribution-link.png" src="https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png" />

<div id="tip" />

> 👍 **Tip**
>
> To learn more about the parameters that you can add to the attribution link, see <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">AppsFlyer attribution link structure and parameters</Anchor>.

</Accordion>

<div id="testing-install-attribution" />

<Accordion title="Testing install attribution">

Send the attribution link to the test device. Open the link in the browser, install the app, and launch.

Launching the app is crucial for the attribution flow. If the app is not launched, no attribution is recorded.

You can then [view the install in your dashboard](/docs/test-marketer-campaign-integration-with-the-ad-network#viewing-installs-in-the-dashboard).

</Accordion>

<div id="testing-apps-in-development" />

## Testing apps in development

You can test a marketer's campaign integration with your ad network even if the app is not live. However, you need to ask the marketer to provide you with the app (an .apk or .ipa file) so you can install it on your test devices.

<div id="generate-an-attribution-link" />

<Accordion title="Generate an attribution link">

Generate an attribution link. You can use the [same instructions as listed above](/docs/test-marketer-campaign-integration-with-the-ad-network#installing-the-app-through-the-attribution-link). Send the attribution link to the test device and navigate to it using the device's browser.

The following screen appears:

<Image align="center" alt="app-not-available.png" src="https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png" />

This is the expected result. Since the app is not live, the attribution link doesn't lead to any app store. However, the attribution link is still valid for attribution purposes. the attribution link and its parameters are recorded by AppsFlyer servers and the data is used for attribution.

</Accordion>

<div id="installing-the-app" />

<Accordion title="Installing the app">

Install the app on the test device using the file that the marketer provides you and then launch the app. Delete the app and repeat the process (to generate several installs). You can then [view the installs in your dashboard](/docs/test-marketer-campaign-integration-with-the-ad-network#viewing-installs-in-the-dashboard).

</Accordion>

<div id="testing-in-app-events" />

## Testing in-app events

<div id="note" />

> 📘 **Note**
>
> You can test in-app events postbacks for both live apps and apps in development.

Before you can test in-app event postbacks, you should contact the marketer to learn about the type of in-app events that they record and how you can trigger them from the app.

<div id="mapping-events" />

<Accordion title="Mapping events">

If the marketer has enabled the permission <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">**Configure in-app event postbacks**</Anchor> in its integration settings for your ad network, you can map AppsFlyer events to the events that you log in your servers.

In your app's AppsFlyer dashboard, from the side menu, select **Active integrations** and choose your ad network. Under the **Integration** tab scroll down to **In-app event settings**. Choose the in-app event and map it to the corresponding event:

<Image align="center" alt="partner-in-app-events-postbacks-mapping.png" src="https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png" />

</Accordion>

<div id="triggering-inapp-events" />

<Accordion title="Triggering in-app events">

Once you know which in-app events the marketer records, and event mapping is in place, trigger a few events from the installed app.

<div id="note-1" />

> 📘 **Note**
>
> Ad networks don’t have access to the Events Dashboard and can see in-app events on Overview Dashboard only after the advertiser enables the **Access aggregate in-app events data** <Anchor target="_blank" href="/marketers/docs/set-up-an-integrated-partner#permissions-tab">ad network permission</Anchor>. However, you can export in-app event-related data from the [In-app events postback](/docs/test-marketer-campaign-integration-with-the-ad-network#verifying-postback-data) report.

In the in-app events postback report, you can find data such as the postback URL and mapped parameters. Use the data in the report and compare it with the data in your servers (from the postback) to make sure that data from postbacks is accurate and properly recorded by your servers.

After exporting the in-app events postbacks report, you can look into the report to verify the following:

1. The event is attributed to you as an ad network, under the field **Media source**
2. The event name is correct, under the **Event name** field
3. The postback, if enabled, contains the event name and value, under the **Postback URL** field
4. In-app events are mapped correctly under the **Postback URL** field

</Accordion>

<div id="viewing-installs-in-the-dashboard" />

## Viewing installs in the dashboard

Once you install and launch the app, you can see the results in your dashboard.

<div id="important-1" />

> 🚧 **Important!**
>
> In order to generate several installs, [the device must be allowlisted](/docs/test-marketer-campaign-integration-with-the-ad-network#prerequisites).

Access your AppsFlyer dashboard and from the side menu, select **Analyze** >  **Overview**.

Filter by your ad network. You can see the number of clicks and installs that are attributed to your ad network.

Data related to clicks and installs appears at the top of the **Overview** screen. The **Overview** screen also includes **Breakdown by campaign** and **Aggregated performance report**. Verify that campaigns that appear in these sections correspond with the campaign parameter in the attribution link.

<div id="verifying-postback-data" />

## Verifying postback data

Every install that is attributed to your ad network generates an install postback. If in-app events postbacks are enabled, events that come from an app whose install is attributed to your ad network, also generate postbacks.

Open the <Anchor target="_blank" href="/marketers/docs/raw-data-export-page">Raw data export page</Anchor> and generate 2 postback reports:

1. **Installs**
2. **In-app events**

Both reports contain a column titled **Postback URL**. This column lists postback URLs for installs or in-app events (depending on the type of report).

Review the data in that column to verify the following:

* The URL endpoint is the correct one
* The parameters appended to the URL correspond to those appended to the AppsFlyer attribution link
* For in-app events postbacks, the events are correctly mapped i.e.  
  `sdk_event=af_purchase&mapped-event=purchase`  
  `sdk_event=af_login&mapped-event=login`
* The **Postback Error Message** column is empty

<div data-zendesk-anchors="h_01HKA1DE8VKXM92D7S5BANFZJ4=prerequisites h_01HKA1DE8V9A9AJWYQR9VJQ0H8=getting-started h_01HKA1DE8VA7HAM8BT3KZ8HYGP=example h_01HKA1DE8V0J2Y8DQ60J9S5DAK=testing-live-apps h_01HKA1DE8VDQGKYSYFDF5K2HSX=important h_01HKA1DE8VEEH8YE1QT28QVFZQ=installing-the-app-through-the-attribution-link h_01HKA1DE8VV0K8J2AG7W0FDDWY=tip h_01HKA1DE8VEH7S0JAJTJ91KE7X=testing-install-attribution h_01HKA1DE8VK9RQGQ8BCG157H1Y=testing-apps-in-development h_01HKA1DE8VSPE0FFM65AFQRJ8S=generate-an-attribution-link h_01HKA1DE8V68Z5CM4EF7YBPHPS=installing-the-app testing-inapp-events=testing-in-app-events h_01HKA1DE8VVJXK11BM77D3YWA5=testing-in-app-events h_01HKA1DE8W2VT648E022BHJP0K=note h_01HKA1DE8WQVGPSTG2SQCM2BQW=mapping-events h_01HKA1DE8WRZPCX3GGV01ZK10K=triggering-inapp-events h_01HKA1DE8W8XXM4BK7843TAEJQ=note-1 h_01HKA1DE8WY7VCST4XDN1HWGC7=viewing-installs-in-the-dashboard h_01HKA1DE8WYRTTNC2Q0VGKMM82=important-1 h_01HKA1DE8WEQY58XAPS9MBNGKE=verifying-postback-data" />
