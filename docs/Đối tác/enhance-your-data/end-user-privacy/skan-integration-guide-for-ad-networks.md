---
title: SKAN integration guide for ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - SKAD
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2020-08-03T08:56:14Z'
  edited_at: '2023-06-26T11:42:18Z'
  id: 360011502657
  locale: vi
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/vi/articles/360011502657
---
> **At a glance**: Ad networks integrate with AppsFlyer SKAdNetworks (SKAN), enabling them to optimize campaigns and to be attributed to the traffic they generate.

## AppsFlyer offering for ad networks

**Learn more about the AppsFlyer SKAN solution for advertisers:**

<Anchor target="_blank" href="/marketers/vi/docs/skadnetwork-skan-solution-guide">SKAN solution guide |</Anchor> <Anchor target="_blank" href="/marketers/vi/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAN dashboard</Anchor>

* **Be attributed for campaign conversions:**
  * Integration with AppsFlyer ensures that the ad network is attributed for all installs, in-app events, and revenue resulting from campaigns run on advertisers' behalf.
  * Without integration in place, installs, in-app events, and revenue are attributed as organic and not to the ad network.
* **Campaign optimization:**
  * The conversion value in the postback is encoded.
  * AppsFlyer enables ad networks to translate the conversion value of each postback, ensuring ad networks can optimize their campaigns based on the decoded value per app.
* **No need for direct integration with each advertiser—** SKAN postbacks are sent only to the ad network and advertisers can consume the data using any of the following:
  * Individual integration with each ad network. A solution that is not scalable, neither for ad networks nor for advertisers.
  * A single integration with AppsFlyer. Scalable for both the advertiser and the ad network.
* **Increase your prominence in AppsFlyer:**
  * Ad networks having SKAN integration are certified and identified as such in the AppsFlyer dashboard.
  * This assures advertisers that they are working with ad networks that can be measured deterministically via this attribution model.

## SKAN data flow

<Image align="center" alt="5754_Postback_flow_for_SKAD__1_.png" src="https://files.readme.io/dff0fb00721802f59d199ae6a69f9ea7484bc0ef038c669904aa1a7c2b97dfc8-12574373654161.png" />

The full SKAN postback flow is as follows:

1. **iOS** sends the SKAN postback to the attributed ad network.
2. **The ad network** does one of the following:
   * **Enrich and forward:** Enrich the SKAN postback with the ad network campaign ID/source identifier, campaign name, and the iOS device IP address.
   * **Redirect:** The network requests the iOS device to redirect the postback directly to AppsFlyer. In this case, campaign data enrichment will be performed via a separate API between AppsFlyer and the ad network.
3. **AppsFlyer** validates and decodes the postback. Then, it sends the decoded and enriched postback to the ad network (in parallel to sharing it with the advertiser).

## Main integration parts

SKAN integration between AppsFlyer and ad networks consists of the following main parts as described in this article:

* Ad networks send SKAN data to AppsFlyer
* Ad networks receive enriched and decoded data from AppsFlyer via postbacks

## Send data to AppsFlyer

After the ad network receives the SKAN postback from the device, the ad network forwards it to AppsFlyer using one of the following methods:

* Enrich and forward (POST)
* Redirect (HTTP 307 redirect method)

Upon receipt of a SKAN postback, AppsFlyer performs the following:

* Postback validation: Ensure that it is unique.
* Conversion value decode: Generate attribution install/in-app event records.
* Send decoded postbacks to the ad network.
* Make attribution data available to advertisers via dashboards and reports.

<div id="enrich-and-forward" />

<Accordion title="Enrich and forward">

Using this method, ad networks forward each postback received from the device to AppsFlyer.

**The ad network:**

* Receives the postback from the iOS device.
* [Mandatory] Enriches the postback with:
  * Ad network campaign ID and campaign name.
  * IP address received from the device, required mainly for geo resolution purposes.
  * The timestamp of the postback sent from the iOS device.
* [Optional] Enriches the postback with:
  * Adset ID and name
  * Ad ID and name
  * Ad network name
  * Country code
  * Source app ID
  * Creative
  * Channel
* Sends the postback to AppsFlyer
* **Note!** Before sending the postback to AppsFlyer, validate the Apple <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/verifying_an_install-validation_postback">attribution signature</Anchor> using the content of the outgoing postback to ensure that you didn't inadvertently corrupt the data.

#### SKAN enriched postback protocol

| Endpoint | `https://skadpostbacks.appsflyer.com/api/postbacks` |
| --- | --- |
| HTTP method | POST |
| Accepted content types | `application/json` |
| Return codes | 200 OK: Postback received has a valid format.<br /><br />400: Bad request: Malformed JSON, empty, JSON, missing mandatory fields. |

#### SKAN enriched postback JSON parameters

| Parameter | Format | Description | Source |
| --- | --- | --- | --- |
| version | String | SKAdNetwork version<br /><br />Example: `"version":"2.0"` | SKAN postback |
| ad-network-id | String | Ad network ID<br /><br />Example: `"ad-network-id":" abc123defg.SKAdnetwork"` | SKAN postback |
| ad-network-name | String | <ul><li>Name of the ad network</li><li>Example: `ad_network_name=your_network`</li></ul> | Ad network |
| ad-network-country-code | String | <ul><li>The user location (geo) as derived by the ad network.</li><li>Populate using <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> codes.</li><li>Example: CN, ZA</li><li>Ad networks often derive geo according to a given campaign's target region.</li><li>AppsFlyer uses the country code to populate geo-related fields in reports and dashboards.</li></ul> | Ad network |
| campaign-id | Integer | <ul><li>Only for SKAN 3 and below</li><li>SKAdNetwork campaign ID</li><li>Example: `"campaign-id":23`</li></ul> | SKAN postback |
| transaction-id | String | SKAdNetwork postback transaction ID | SKAN postback |
| app-id | Integer | <ul><li>Target app ID as it appears in AppsFlyer. Always has the prefix id.</li><li>Example:`app_id=id123456789`</li></ul> | SKAN postback |
| attribution-signature | String | Attribution signature | SKAN postback |
| redownload | Boolean | When redownload = true, it means the user downloaded the app from the app store again. | SKAN postback |
| source-app-id | Integer | <ul><li>Source App ID (publisher)</li><li>For SKAN 4, available only in the first postback, for tier 3. See [Apple documentation](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | SKAN postback |
| conversion-value | Integer | AppsFlyer SDK sets the conversion value according to advertiser settings.<br /><br />**Notes**!<ul><li>iOS due to iOS privacy-preserving thresholds may not populate the parameter in the postback and the value will be null.</li><li>Null and 0 have different meanings:<ul><li>Null: iOS withheld the conversion value</li><li>0: The user installed the app but didn't perform any measured actions.</li></ul></li></ul> | SKAN postback |
| ad-network-campaign-id | String | To enable a common language between ad networks, advertisers, and AppsFlyer, you must provide your campaign-id. | Ad network |
| ad-network-campaign-name | String | Ad network campaign name associated with the ad network campaign ID. This name displays in dashboards and reports. | Ad network |
| ad-network-adset-id | String | Ad network adset ID | Ad network |
| ad-network-adset-name | String | Ad network adset name | Ad network |
| ad-network-ad-name | String | Ad network ad name | Ad network |
| ad-network-ad-id | String | Ad network ad ID | Ad network |
| ip | String | <ul><li>The IP address of the device sending the postback.</li><li>iPv4 and IPv6 addresses supported.</li><li>Example: `"ip":"198.51.100.1"`</li></ul> | Ad network |
| timestamp | String | <ul><li>Time the ad network received the SKAN postback. A 10-digit epoch UNIX timestamp. [Optional] 13-digit epoch timestamp permitted.</li><li>Example: August 4, 2020, 07:25 UTC translates to `"timestamp": "1596525944"`</li></ul> | Ad network |
| fidelity-type | Integer | <ul><li>Differentiate between <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/receiving_ad_attributions">ad presentation</Anchor> options that affect attribution. Indicated using the values 0 and1 as follows:<ul><li>View-though ads (0)</li><li>Storekit-rendered ads (1)</li></ul></li><li>Mandatory field starting SKAN V2.2</li></ul> | SKAN postback (V2.2+) |
| did-win | Boolean | <ul><li>Used to distinguish between campaigns [contributing or attributed](https://developer.apple.com/documentation/storekit/SKAdnetwork/SKAdnetwork_release_notes/SKAdnetwork_version_3_0_release_notes) with the install.</li><li>If true, the campaign is attributed for bringing the install.</li><li>If false, the campaign is recognized as contributing to the install</li></ul> | SKAN postback (V3.0+) |
| ad-network-source-app-id | String | Populate with the *publisher ID* that you associate with the app publishing the ad. This is usually the ID you allocated to the publisher, and not the ID generated by Apple. | Ad network |
| postback-sequence-index | Integer | <ul><li>Only for SKAN 4+</li><li>Value represents the sequence number (SKAN window), either`0`,`1`, or`2`.</li></ul> | SKAN 4.0 postback (iOS 16.2) |
| coarse-conversion-value | String | <ul><li>Only for SKAN 4+</li><li>Value can be`low`,`medium`, or`high`.</li><li>For the first postback, only available for tier 1. For the second and third postbacks, available for tiers 1-3. See [Apple documentation](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | SKAN 4.0 postback (iOS 16.2) |
| source-identifier | String | <ul><li>Only for SKAN 4+</li><li>Replaces `campaign-id`</li><li>Value can be up to 4 digits.</li><li>For the first postback, up to 4 digits are available for tiers 2-3 and 2 digits are available for tiers 0-1. For the second and third postbacks, 2 digits are available for tiers 1-3. For tier 0, there isn't a postback. See [Apple documentation](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | SKAN 4.0 postback (iOS 16.2) |
| source-domain | String | <ul><li>Only for SKAN 4+</li><li>Value represents the source of attributable web ads. Example: `example.com`</li><li>Available in web ads only, in the first postback, for tier 3. See [Apple documentation](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | SKAN 4.0 postback (iOS 16.2) |
| creative | String | <ul><li>Only relevant for SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> | Ad network |
| channel | String | <ul><li>Only relevant for SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> | Ad network |

#### **Curl example—enriched SKAN 3 postback**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version":"3.0",
      "app-id": 888707086,
      "ip": "192.0.2.0",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "source-app-id": 888707074,
      "ad-network-id": "abcabcabc.skadnetwork",
      "transaction-id": "68eb3d91-15f5-44ee-9267-25c7655c20b6",
      "redownload": false,
      "attribution-signature": "MDYCGQCsQ4y8d4BlYU9b8Qb9BPWPi+ixk/OiRysCGQDZZ8fpJnuqs9my8iSQVbJO/oU1AXUROYU=",
      "timestamp": "1596525944",
      "ad-network-campaign-id": "222222",
      "conversion-value": 63,
      "campaign-id": 99
  }'
```

#### **Curl example—enriched SKAN 4 postback with fine conversion values**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "5239",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e30",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "conversion-value": 63
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIGRmSMrqedNu6uaHyhVcifs118R5z/AB6cvRaKrRRHWRAiEAv96ne3dKQ5kJpbsfk4eYiePmrZUU6sQmo+7zfP/1Bxo="
  }'
```

#### **Curl example—enriched SKAN 4 postback with coarse conversion values**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "39",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e31",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "coarse-conversion-value": "high"
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIQD4rX6eh38qEhuUKHdap345UbmlzA7KEZ1bhWZuYM8MJwIgMnyiiZe6heabDkGwOaKBYrUXQhKtF3P/ERHqkR/XpuA="
  }'
```

</Accordion>

<div id="redirect" />

<Accordion title="Redirect">

<Image align="center" alt="Redirect_us-en__2_.png" src="https://files.readme.io/17d4a668cde784a2f823e702e04fc75a2bbbdb483e44d9d10edfad03d865bbb7-360012352758.png" />

Using this method, the ad network responds to the device with an HTTP redirect command (307), requesting the device to send the postback directly to AppsFlyer. 

The redirect method has the following advantages:

* **Increased advertiser trust:** The MMP acts on behalf of an advertiser. By providing AppsFlyer access to the postback firsthand, advertisers are confident that postbacks are not manipulated in transit.
* **No processing required by the ad network:** Ad networks respond with the redirect command (to the device), thus eliminating the need to process postbacks. In comparison, the enrich and forward method requires that ad networks consume the postback, enrich it with additional parameters, and finally forward it to AppsFlyer.

#### **Implementation**

1. Configure your server to respond with an HTTP 307 response redirecting the postback to *[https://skadnetworkredirect.appsflyer.com/api/redirects](https://SKANredirect.appsflyer.com/api/redirects)*
2. Append query params that contain campaign details using the query params listed in the table that follows. Regard the sending of your campaign details as mandatory. Campaign details enable us to enrich SKAN data with cost and other campaign data and enable advertisers to effectively optimize campaigns.

**Example redirect URL**

```http
https://skadnetworkredirect.appsflyer.com/api/redirects?
  &ad-network-campaign-id=243232&ad-network-campaign-name=yarg_campaign_name
  &ad-network-adset-name=dsdsa&creative=examplecreative&channel=channelexample
```

#### Query params for campaign details (not mandatory)

| Query param | Description |
| --- | --- |
| ad-network-name | <ul><li>Name of the ad network</li><li>Example:`ad_network_name=your_network`</li></ul> |
| ad-network-campaign-id | Campaign ID |
| ad-network-campaign-name | Campaign name |
| ad-network-adset-id | Ad set ID |
| ad-network-adset-name | Ad set name |
| ad-network-ad-id | Ad ID |
| ad-network-ad-name | Ad name |
| ad-network-country-code | <ul><li>The user location (geo) derived by the ad network.</li><li>Populate using <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> codes.</li><li>Example: CN, ZA</li><li>Ad networks often derive geo according to a given campaign's target region.</li><li>AppsFlyer uses the country code to populate geo-related fields in reports and dashboards.</li></ul> |
| ad-network-source-app-id | Populate with the *publisher ID* that you associate with the app publishing the ad. This is usually the ID you allocated to the publisher, and not the ID generated by Apple. |
| ip | <ul><li>The IP address of the device sending the postback.</li><li>iPv4 and IPv6 addresses supported.</li><li>Example:`"ip":"198.51.100.1"`</li></ul> |
| timestamp | <ul><li>Time the ad network received the SKAN postback. A 10-digit epoch UNIX timestamp. [Optional] 13-digit epoch timestamp permitted.</li><li>Example: August 4, 2020, 07:25 UTC translates to`"timestamp": "1596525944"`</li></ul> |
| creative | <ul><li>Only relevant for SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> |
| channel | <ul><li>Only relevant for SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> |

</Accordion>

## Receive data from AppsFlyer

Prior to receiving your first postback, take into consideration the following:

* Ad networks must define the postback end-point and template (reach out to your AppsFlyer Partner Development Manager using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>, to ensure this is in place).
* AppsFlyer sends SKAN postbacks using the same mechanism as with the existing postbacks sent to you.

<div id="principles" />

<Accordion title="Principles">

* For each postback sent from the ad network to AppsFlyer, AppsFlyer sends:
  * One install postback. Redownloads are signaled by the redownload parameter.
  * Zero to several in-app event postbacks. The exact number depends on the translation of the conversion value. See [simulated postbacks.](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks)
* When you consume postbacks, the same install or event can be attributed by more than one AppsFlyer attribution solution. Use the *attribution\_source* parameter to differentiate between postback types.

</Accordion>

<div id="postback-macros-available-to-ad-network-partners" />

<Accordion title="Postback macros available to ad network partners">

<table><thead><tr><th><p>Postback macro (name)</p></th><th><p>Description</p></th><th>Format and example</th><th>Relevant to in-app events only</th></tr></thead><tbody><tr><td><p>site_id</p></td><td><p>The app publishing the ad (source app ID)</p></td><td><p>String: 876534</p></td><td></td></tr><tr><td><p>install_time</p></td><td><p>Estimated by AppsFlyer based on the <em>updateConversion</em> window. Provided as a 10-digit UNIX epoch timestamp or as a human-readable timestamp</p></td><td><ul><li>String: 1596119460 </li><li>Translates to July 30, 2020, 14:31 UTC.</li></ul></td><td> </td></tr><tr><td><p>skadnetwork_ad_network_time</p></td><td><p>Time the postback was received by the ad network from the iOS device. Reported by the ad network. Provided as a 10-digit UNIX epoch timestamp or as a human-readable timestamp</p></td><td><ul><li>String: 1596119460 </li><li>Translates to July 30, 2020, 14:31 UTC</li></ul></td><td> </td></tr><tr><td><p><br/>skadnetwork_received_time</p></td><td><p>Time AppsFlyer received the postback from the ad network. Provided as a 10-digit UNIX epoch timestamp or as a human-readable timestamp</p></td><td><ul><li>String: 1596119460 </li><li>Translates to July 30, 2020, 14:31 UTC</li></ul></td><td></td></tr><tr><td><p>event_name</p></td><td><p>Event name </p><ul><li>af_skadnetwork_revenue</li><li>af_login</li><li>af_skadnetwork_revenue</li><li>or as set by the advertiser </li></ul></td><td><p>String: af_skadnetwork_revenue, abc123</p></td><td><p>Yes</p></td></tr><tr><td><p>revenue</p></td><td><p>Revenue amount using the specified currency code</p></td><td><p>Number: 5, 20, 0.4</p></td><td><p>Yes</p></td></tr><tr><td><p>currency</p></td><td><p>Currency code being the app-specific currency set by the advertiser</p></td><td><p>String: EUR, USD, ZAR</p></td><td><p>Yes</p></td></tr><tr><td><p>attribution_source</p></td><td><p>The source of the attribution data:</p><p>SKAdNetwork: SKAdNetwork</p></td><td><p>String: SKAdNetwork</p></td><td></td></tr><tr><td><p>app_id</p></td><td><p>App ID (advertiser app)</p></td><td><p>String: ID123456790</p></td><td></td></tr><tr><td><p>country</p></td><td><p>Install geo (country) determined by the ad network</p></td><td><p>String: US, UK, ZA </p></td><td></td></tr><tr><td><p>campaign</p></td><td><p>Campaign name populated using a<em>d-network-campaign-name</em> sent in the postback from the ad network</p></td><td><p>String: UA_US_23+</p></td><td></td></tr><tr><td><p>campaign_id</p></td><td><p>Ad network Campaign ID populated using <em>ad network-campaign-id</em> sent in the postback from the ad network. <strong>Note</strong>: For SKAN 4, this value is always null.</p></td><td><p>String: 3456745</p></td><td></td></tr><tr><td><p>redownload</p></td><td><p>Possible values: true, false</p><p>When redownload = true, it means the user downloaded the app from the app store again</p></td><td><p>Boolean: true, false</p></td><td></td></tr><tr><td><p>skadnetwork_ambiguous_event</p></td><td>Events received during the first 72-hours after an advertiser changes the SKAN settings in the dashboard. Due to the various timers employed by SKAN AppsFlyer can't map the event accurately.</td><td><p>Boolean: true, false</p></td><td></td></tr><tr><td><p>skadnetwork_campaign_id</p></td><td>SKAN campaign ID as provided by the original SKAN postback</td><td><p>56, 23</p></td><td></td></tr><tr><td><p>af_skadnetwork_nonce</p></td><td>A unique random identifier enabling partners to identify duplicate postbacks</td><td></td><td></td></tr><tr><td><p>event_id</p></td><td><span>Name/ID of the corresponding<span> </span><span>event</span><span> </span>in the ad network platform</span></td><td></td><td><p>Yes</p></td></tr><tr><td><p>transaction_id</p></td><td><p><span>SKAN postback transaction ID</span></p><p><span><strong>Note</strong>: The advertiser must explicitly allow us to share the transaction_id with you. Ask the advertiser to do so in the <a href="/marketers/vi/docs/set-up-an-integrated-partner#integration-tab" target="_blank"><strong>Integration</strong></a> tab.</span></p></td><td></td><td></td></tr><tr><td>ad_network_adset_id</td><td>Added to the iOS postback by the ad network</td><td>String</td><td> </td></tr><tr><td>ad_network_adset_name</td><td>Added to the iOS postback by the ad network</td><td>String</td><td> </td></tr><tr><td>ad_network_ad_name</td><td>Added to the iOS postback by the ad network</td><td>String</td><td> </td></tr><tr><td>ad_network_ad_id</td><td>Added to the iOS postback by the ad network</td><td>String</td><td> </td></tr><tr><td>SKAN_min_event_counter</td><td>See note (1)</td><td><p>Integer</p></td><td>Yes</td></tr><tr><td>SKAN_max_event_counter</td><td>See note (1)</td><td><p>Integer</p></td><td>Yes</td></tr><tr><td>SKAN_min_time_post-install</td><td>See note (2)</td><td><p>Integer</p></td><td>Yes</td></tr><tr><td>SKAN_max_time_post-install</td><td>See note (2)</td><td><p>Integer</p></td><td>Yes</td></tr><tr><td>SKAN_min_event_revenue</td><td>See note (3)</td><td>Real number</td><td>Yes</td></tr><tr><td>SKAN_max_event_revenue</td><td>See note (3)</td><td><p>Real number </p></td><td>Yes</td></tr><tr><td>fidelity-type</td><td><p><span>Differentiate between <a href="https://developer.apple.com/documentation/storekit/SKAdnetwork/receiving_ad_attributions" target="_blank">ad presentation</a> options that affect attribution. Indicated using the values 0 and1 as follows: </span></p><ul><li><span>View-though ads (0)</span></li><li><span>Storekit-rendered ads (1) </span></li></ul></td><td>Integer</td><td> </td></tr><tr><td>skad_af_attribution_flag</td><td><p><span>Used to indicate if the user was attributed by AppsFlyer using the <a href="/marketers/vi/docs/single-source-of-truth-ssot-guide-for-ios-attribution#trường-cờ-phân-bổ" target="_blank">Single Source of Truth mechanism</a>. </span></p></td><td>Boolean</td><td> </td></tr><tr><td><span>skad_postback_sequence_index</span></td><td><ul><li><span>Value represents the SKAN window, either<code>0</code>,<code>1</code>, or<code>2</code>. </span></li><li><span>For SKAN 3 the value is<code>0</code></span></li></ul></td><td><span>Integer</span></td><td> </td></tr><tr><td><span>skad_coarse_conversion_value</span></td><td><ul><li><span>Value can be<code>low</code>,<code>medium</code>, or<code>high</code>. </span></li><li><span>For SKAN 3 the value is<code>null</code>.</span></li></ul></td><td><span>String</span></td><td> </td></tr><tr><td><span>skad_source_identifier</span></td><td><ul><li><span>Value can be up to 4 digits. </span></li><li><span>For SKAN 3 the value is<code>null</code>. </span></li></ul></td><td><span>String</span></td><td> </td></tr><tr><td><span>skad_source_domain</span></td><td><ul><li><span>Value represents the source of attributable web ads. </span></li><li><span>For SKAN 3 the value is<code>null</code>.</span></li></ul></td><td><span>String</span></td><td> </td></tr><tr><td><span>ad_network_creative</span></td><td><ul><li><span>Value is based on data enrichment received from the ad network. </span></li><li><span>For SKAN 3 the value is <code>null</code>.</span></li></ul></td><td><span>String</span></td><td> </td></tr><tr><td><span>ad_network_channel</span></td><td><ul><li><span>Only relevant for SKAN 4+</span></li><li>Available when you use additional digits in the <span>source_identifier</span> for additional campaign granularity.</li></ul></td><td><span>String</span></td><td> </td></tr><tr><td colspan="4"><p>Notes:</p><ol><li> <strong>Event occurrences</strong>: The number of event occurrences is calculated using the following formula:<br/><code>[round up (SKAN_min_event_counter+SKAN_max_event_counter) / 2]</code><br/>Note! The value must be rounded up to the nearest integer.</li></ol><ul><li>Example: <ul><li>A. If min=0 and max=1 the number of events is 1.</li><li>B. If min=0 and max =10 the number of events is 5.</li></ul></li><li> <strong>Determine install time</strong>: For advertisers implementing custom conversion, AppsFlyer calculates install time as the postback arrival time - 48h - average (min_time_post_install + max_time_post_install). Ad networks don't need to make use of these macros.  </li><li> <strong>Determine revenue</strong>: AppsFlyer uses these values to determine the revenue of an event by calculating the average of min and max. Ad networks don't need to make use of these macros. </li></ul></td></tr></tbody></table>

</Accordion>

<div id="skan-postback-examples" />

<Accordion title="SKAN postback examples">

**Example of an install SKAN postback sent by AppsFlyer**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)
  &attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

**Example of an in-app SKAN postback sent by AppsFlyer**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)&revenue=(value)
  &currency=(code)&event_name=(event-name)&attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

</Accordion>

## Integration testing

To validate the integration with AppsFlyer, use either or both of the following methods. 

* Real SKAN postbacks: based on actual SKAN traffic received by the network
* Simulated postbacks: based on AppsFlyer test apps

**To receive real SKAN postbacks from iOS devices, the ad network completes the following:**

* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/registering_an_ad_network">Register with Apple</Anchor>
* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/generating_the_signature_to_validate_storekit-rendered_ads">Sign ads with a SKAdNetwork signature</Anchor>.
* Publisher app: <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/configuring_a_source_app">Add the network ID to the info.plist file</Anchor> and <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/generating_the_signature_to_validate_an_installation">call the loadProduct</Anchor> function upon ad impression.
* Advertised app: Use the most recent AppsFlyer <Anchor target="_blank" href="/marketers/vi/docs/sdk-integration-overview">iOS SDK.</Anchor> Versions prior to V6.0.3 aren't supported.

**To receive simulated postbacks:**

* Contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> and request integration with simulation apps.
* Specify IDs of the apps from the list in the [following section](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks).

<div id="real-environment" />

<Accordion title="Real environment">

Using this method, the ad network sends AppsFlyer actual SKAN postbacks from live apps.

#### Testing integration

| Responsibility | Action |
| --- | --- |
| Ad network | Notify AppsFlyer via your partner development manager (or use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>) as to your SKAN network ID, provided by Apple. |
| Ad network and AppsFlyer | Agree on a mutual customer (having integrated the most recent AppsFlyer SDK) to use for postback integration verification. |
| Ad network | Send app SKAN postbacks to AppsFlyer, using one of the methods described in this article. |
| AppsFlyer | Send decoded postbacks to the ad network in accordance with the conversion value mapping set by the advertiser. |

#### Test criteria

| Responsibility | Action |
| --- | --- |
| Ad network | Notify AppsFlyer as to the quantity of SKAN postbacks sent during a specified period for the agreed mutual customer. |
| AppsFlyer | Verify the count of postbacks received versus the count sent by the ad network. |
| AppsFlyer | Share with the ad network the count of postbacks sent to the network for a given app broken down by type:<ul><li>Install/redownload postbacks</li><li>In-app postbacks.</li></ul>Note: If you use the same endpoint for probabilistic postbacks, ensure that you filter using *attribution\_source=skadnetwork* to distinguish SKAN Network postbacks from other postbacks. |

</Accordion>

<div id="simulated-postbacks" />

<Accordion title="Simulated postbacks">

* Using this method, the ad network sends AppsFlyer preprepared postbacks to AppsFlyer test apps, as detailed in the table below. AppsFlyer replies with decoded postbacks to the ad network.
* Each test app has a different conversion value mapping, as detailed in the table.

| App ID | Conversion mode | Instructions |
| --- | --- | --- |
| <span id="id888707085"></span>id888707085 | Revenue, in $1 units<br /><br />Expected results: | <ol><li>In the **Integration** tab, enable i**n-app events postbacks**.</li><li>Select event name *af\_SKAN\_revenue* and map to your event identifier.</li><li>Save configuration.</li><li>In a postback, send conversion value = 7.</li><li>AppsFlyer responds with:<ul><li>Install postback</li><li>af\_SKAN\_revenue postback with value of $7</li></ul></li></ol> |
| <span id="id888707086"></span>id888707086 | Conversion, including the in-app events:<ul><li>af\_level\_complete</li><li>af\_login</li><li>af\_SKAN\_revenue</li><li>af\_register</li><li>af\_subscription</li><li>af\_custom\_event</li></ul> | <ol><li>In the **Integration** tab, enable i**n-app events postbacks**.</li><li>Select each of the in-app events listed and map it to your event identifier.</li><li>Save configuration.</li><li>In a postback, send conversion value = 63.</li><li>AppsFlyer responds with:<ul><li>Install postback</li><li>af\_level\_complete postback</li><li>af\_login postback</li><li>af\_SKAN\_revenue postback</li><li>af\_register postback</li><li>af\_subscription postback</li><li>af\_custom\_event postback</li></ul></li></ol> |
| <span id="id888707087"></span>id888707087 | Engagement, measured using af\_SKAN\_revenue event | <ol><li>In the **Integration** tab, enable i**n-app events postbacks**.</li><li>Map the event name *af\_SKAN\_revenue* and to your event identifier.</li><li>**Save** configuration.</li><li>In a postback, send conversion value = 3.</li><li>AppsFlyer responds with:<ul><li>Install postback</li><li>3 postbacks of af\_SKAN\_revenue event</li></ul></li></ol> |

#### Integration steps

| Responsibility | Action |
| --- | --- |
| Ad network | Configure your SKAN network ID (provided by Apple) and SKAN postback template on the <Anchor target="_blank" href="/partners/vi/docs/self-serve-integration-management-for-ad-networks">postback management platform</Anchor>. For queries and assistance, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>. |
| Ad network | <ol><li><Anchor target="_blank" href="/partners/vi/docs/turn-on-test-app-integration-for-ad-networks">Activate the test apps</Anchor>.</li><li>For each app complete the instructions column in the previous table.</li><li>Send simulated postbacks, using the test apps listed in the preceding table. Considerations when sending simulated postbacks:<ul><li>Set the app\_id and conversion value as listed in the preceding table.</li><li>Since Ad networks can't generate Apple compatible signatures, the simulated postbacks don't have to include the signature fields. AppsFlyer will not verify them for simulated postbacks.</li><li>Ad networks send the postback using either the POST or REDIRECT approach.</li></ul></li></ol> |
| AppsFlyer | Responds with the decoded postbacks to the endpoint designated by the ad network during integration |

#### Test criteria

| Responsibility | Action |
| --- | --- |
| AppsFlyer | Process the postback and sends postbacks to the ad network. |
| Ad network | <ul><li>Ad network receives and decodes the translated postbacks.</li><li>In-app postbacks sent by AppsFlyer match the expected flows. For example, conversion value 3 for app ID888707087, the ad network receives 3 postbacks of *af\_SKAN\_revenue* event.</li></ul> |

</Accordion>

## Clarifications

Clarifications relating to mandatory fields, enrichment, certification, and more.

<div id="faq" />

<Accordion title="FAQ">

| Questions and answers about postbacks |
| --- |
| **Are the enrichment fields mandatory?**<br /><br />For the present, we will process the postback even if it is missing one or more of the following enrichment parameters. Consider that the information is required for the following reasons:<ul><li>**Ad network campaign ID**: If we have cost integration with you then this is reported using your campaign ID.</li><li>**Ad network campaign name**: Many advertisers relate to the campaign name and not the campaign number.</li><li>**IP address**: Required for geo resolution.</li><li>**Timestamp**: Assists us to attribute the install to the correct date.</li></ul> |
| **Can we send either our campaign ID, or our campaign name, but not both?**<br /><br />See the previous answer. Consider populating both ID and name with the same value. |
| **We are using *Enrich and Forward.* Can we add key-value pairs that are not in the AppsFlyer specification?**<br /><br />Yes, you can. We will process the postback and disregard the extra information provided that the attribution signature is valid |
| **Are the SKAN postback templates distinct from the existing postback templates?**<br /><br />Yes. The flow and structure differ. |
| **Will we receive a SKAN postback and a probabilistic/deterministic modeling postback related to the same install, meaning duplicate reporting of the same install?**<br /><br />Yes. For each case, we record an install attributed to you, irrespective of method, we will send you a postback.<br /><br />Use *attribution\_source* to differentiate SKAN postbacks. |
| **Are we required to process the postback from AppsFlyer?**<br /><br />No. Consider, that best practice is to optimize campaigns according to user-quality reported via the postback. |
| **Are we expected to call AppsFlyer attribution links or is it sufficient to send the postback with the SKAN payload and enriched data?**<br /><br />It is sufficient to send us the SKAN payload and enriched data. |
| **What is required for us to be certified in the AppsFlyer dashboard as a SKAN integrated partner?**<ul><li>Complete integration using one of the methods listed in this article</li><li>Send us postbacks of apps using AppsFlyer as their attribution partner</li></ul> |
| **How does the limit of 100 SKAN campaign IDs impact me**?<br /><br />The 1-100 limit relates to the way you sign and number your campaigns in Apple. It means that at any time, you can have 100 simultaneous unique campaigns. We allow you to enrich the postback with your actual campaign name and ID. Meaning you map the SKAN campaign ID to your actual campaign IDs in use at the time the postback is received. Doing so means that the 100 ID limit does not restrict the number of campaigns that you measure in AppsFlyer provided of course that you don't have more than 100 simultaneous campaigns for a given app. |

</Accordion>

<div data-zendesk-anchors="curl-example%E2%80%94enriched-skan-3-postback=curl-exampleenriched-skan-3-postback curl-example%E2%80%94enriched-skan-4-postback-with-fine-conversion-values=curl-exampleenriched-skan-4-postback-with-fine-conversion-values curl-example%E2%80%94enriched-skan-4-postback-with-coarse-conversion-values=curl-exampleenriched-skan-4-postback-with-coarse-conversion-values test-criteria::26c15d59=test-criteria-1" />
