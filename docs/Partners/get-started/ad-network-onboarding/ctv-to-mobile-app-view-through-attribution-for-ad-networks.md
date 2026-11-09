---
title: CTV-to-mobile app view-through attribution for ad networks
metadata:
  keywords:
    - Attribution
    - Ad Networks
    - Partners
    - CTV
    - CTV Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roi-tamir
    - CTV Attribution
    - Ad Networks
  created_at: '2022-08-21T06:49:24Z'
  edited_at: '2026-08-26T10:59:04Z'
  id: 8528418936977
  locale: en-us
  section: Ad network onboarding
  section_id: 6551058566033
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/8528418936977-CTV-to-mobile-app-view-through-attribution-for-ad-networks
---
> **At a glance:** Attribute mobile app installs to ads viewed on Connected TV (CTV) devices.

<div id="ctv-to-mobile-app-attribution-for-ad-networks" />

## CTV-to-mobile app attribution for ad networks

With AppsFlyer cross-platform impression URLs, you can attribute mobile app installs to ads displayed on CTV. Multiple installs within the same household can be attributed to the same CTV ad impression.

<Image align="center" alt="Diagram of the CTV-to-mobile app attribution flow" src="https://files.readme.io/401bcb083e1cc618794cb302668f7271cf825a5a6045ff10055e0164baf423a1-19774176963473.jpg" />

CTV-to-mobile app view-through attribution uses a <Anchor target="_blank" href="/marketers/docs/set-up-cross-platform-links-for-multi-device-campaigns#setup">OneLink impression URL</Anchor> based on a cross-platform OneLink template (with a template ID) created by the advertisers. This lets advertisers group multiple apps from different platforms (for example, both Android and iOS apps) using a single URL.

When users view the ad on CTV, you send AppsFlyer the impression URL in real time. 

Example URL:

```
https://impressions.onelink.me/{template_id}?pid=__media_source__&af_xplatform=true&af_xplatform_vt_lookback=24h&af_siteid=__CSITE__&c=__CAMPAIGN_NAME__&af_channel=__PLACEMENT__&af_c_id=__CAMPAIGN_ID__&af_adset=__AID_NAME__&af_adset_id=__AID__&af_ad=__CID_NAME__&af_ad_id=__CID__&af_source_platform=__source_platform__&af_source_device_category=__device_category__&af_ad_type=__CTYPE__&af_ip=__IP__&af_ua=__UA__&redirect=false
```

AppsFlyer sends postbacks to you after each conversion.

<div id="note" />

> 📘 **Note**
>
> This feature is available only for designated partners. Contact your Partner Development Manager (PDM) if you’re interested.

<Accordion title="Set up CTV-to-mobile attribution">

**To set up CTV-to-mobile app view-through attribution with an advertiser**:

1. Make sure you're an <Anchor target="_blank" href="/partners/docs/getting-started-onboarding-guide-for-ad-networks">AppsFlyer integrated partner</Anchor>, that you have postbacks properly set up, and that you've [tested your CTV-to-mobile app integration](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#test-partner-integration) with AppsFlyer.
2. Make sure the URL has the [mandatory parameters](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#parameters), as well as any other parameters you want.
3. Send AppsFlyer the user IP address and user agent. These are required for CTV-to-mobile app view-through attribution. They can be sent either:
   1. As the `af_ip` and `af_ua` parameters on the impression URL.
   2. As `<X-Forwarded-For>` and `<User-Agent>` parameters in the headers of the request.

</Accordion>

<Accordion title="Test partner integration">

**To test CTV-to-mobile app view-through attribution**:

1. Use the following test apps: com.appsflyer.android.deviceid and id1192323960
2. Contact the AppsFlyer Partner Solutions Team to receive a test URL. To do so, log in to your <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">partner dashboard</Anchor>, and from the top menu, click **Help** > **Contact our team**.
   * Sample URL: `https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false`
3. Confirm that your partner ID in the `pid` parameter is correct.
4. Enter your IP address for the `af_ip` parameter.
5. Enter your user agent for the `af_ua` parameter.
6. Enter the URL into a desktop browser.
7. On your mobile device, go to the app store, and download, install, and launch the app.
8. A new install appears in AppsFlyer, along with a corresponding postback. If you don’t see the install or get the postback, contact the Partner Solutions Team.

</Accordion>

<Accordion title="Parameters">

The following parameters are used to provide attribution data and measurement to advertisers.

| Parameter | Mandatory | Description |
| --- | --- | --- |
| template\_id | ✓ | The ID of the <Anchor target="_blank" href="/marketers/docs/create-a-onelink-template">OneLink template</Anchor>. The template contains basic prediction settings for the advertiser apps and is the basis for creating other links. Note: Never encode the `template_id` value. |
| pid | ✓ | The partner identifier, allocated by AppsFlyer to the media source (ad network) placing the ad. |
| af\_xplatform | ✓ | <ul><li>Set by the advertiser to indicate whether the link supports cross-platform attribution.</li><li>Values: true/false</li></ul> |
| af\_xplatform\_vt\_lookback | - | Configurable window that indicates the number of hours following the impression during which the app install can be attributed to the impression. Available parameter values: 1h - 72h (hours). The default is 24h. |
| af\_ip | ✓ | <ul><li>The IP address of the CTV device that displays the ad.</li><li>If the IP address isn't sent in the URL, it must be sent in the headers of the request so AppsFlyer can perform CTV-to-mobile app attribution.</li></ul> |
| af\_ua | ✓ | <ul><li>The user agent of the CTV device that displays the ad.</li><li>If the user agent isn't sent in the URL, it must be sent in the headers of the request so AppsFlyer can perform CTV-to-mobile app attribution.</li></ul> |
| af\_source\_platform | - | <ul><li>A set list of values to represent the operating system where the impression occurs.</li><li>Values:<ul><li>android</li><li>ios</li><li>tizen</li><li>webos</li><li>smartcast</li><li>roku</li><li>windowsphone</li><li>vidaa</li><li>PlayStation</li><li>website</li></ul></li></ul> |
| af\_source\_device\_category | - | <ul><li>A set list of values to represent the device type where the impression occurs.<ul><li>tv</li><li>mobile\_phone</li><li>desktop</li><li>tablet</li><li>set\_top\_box</li><li>games\_console</li><li>unknown\_device\_category</li><li>media\_player</li></ul></li></ul> |

Other parameters that can be added to the URL can be found in the <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">attribution link structure and parameters article</Anchor>.

</Accordion>

<Accordion title="Traits and limitations">

| Trait | Description |
| --- | --- |
| Attribution window | Between 1-72 hours, depending on the lookback window parameter `af_xplatform_vt_lookback`. |
| Retargeting | <ul><li>Re-attribution: Supported for cross-platform-to-mobile. Not for other platforms.</li><li>Re-engagement: Not supported</li></ul> |
| Attribution method | View-through attribution using probabilistic modeling (IP address) |
| Household attribution | Supported. Meaning multiple installs within the same household can be attributed to the same CTV ad impression. |
| Test partner integration | Not available for ad networks that have been flagged for high rates of mobile app-to-mobile app fraud or are affiliated with different flagged media sources. |

</Accordion>

<div data-zendesk-anchors="ctvtomobile-app-attribution-for-ad-networks=ctv-to-mobile-app-attribution-for-ad-networks h_01HE2X91GTDTPKKFBRRYYFMHDW=ctv-to-mobile-app-attribution-for-ad-networks" />
