---
title: Postback macros for ad networks
metadata:
  keywords:
    - postbacks
    - Advertisers
    - Ad Networks
    - macros
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
  created_at: '2016-01-11T14:41:40Z'
  edited_at: '2025-12-22T10:42:52Z'
  id: 207273946
  locale: en-us
  section: Receive data
  section_id: 6551235995281
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/207273946-Postback-macros-for-ad-networks
---
**At a glance:** As an ad network, you can define the content and endpoints of postbacks sent to you as part of your integration with AppsFlyer. Postbacks relate to app user engagement like installs, in-app events, re-engagements, and so on.

Related integrated partner postback guides:

* <Anchor target="_blank" href="/partners/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Advanced Privacy</Anchor>
* <Anchor target="_blank" href="/partners/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/docs/rejected-attribution-postbacks-to-integrated-partners">Rejected attribution postbacks</Anchor>

## Postbacks for ad networks

* **Postback configuration:** To request changes to your postback settings, use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>, or contact your AppsFlyer partner development manager.
* **Postback types**: Postbacks are available for install and in-app events and blocked install and in-app events (due to fraud identified by Protect360 or in violation of targeting validation rules).

### Postback data sources

| Source | Description |
| --- | --- |
| <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">Attribution link parameters</Anchor> | Parameters provided by the partner on click and impression URLs<br /><br />Example: click ID parameter on the attribution link - "&click\_id=CLICK\_ID" |
| Partner IDs in AppsFlyer | Unique IDs provided to the advertiser by the partner<br /><br />Examples: app ID, account ID, user ID, network ID |
| SDK derived information | Information extracted from the device by the AppsFlyer SDK<br /><br />Example: iOS device IDs can be extracted by using "&IDFA=(idfa)" on the postback |
| Derived by the AppsFlyer platform | Information derived by the AppsFlyer platform. |
| Protect360 and validation rules | Information about installs identified as fraud and installs violating campaign targeting rules, and their associated in-app events |

## Postback macros

When included in a postback, macros are replaced with user-relevant data. For example, to get the IP address of the user installing the app, include `country_code=(ip)` in the postback structure. Supported macros are listed in the following table:

The columns in the table below have the following meaning:

* **Source:** Where the data originates from.
  * Link: Attribution links
  * SDK: AppsFlyer SDK embedded in the app or server-to-server API
  * AF: After processing by AppsFlyer
* **Send all**: If yes, you can receive the data of installs and events attributed to other networks or organic. (Means not attributed to you).
* **[Base] Macros for all postbacks**: Macros relevant to install, in-app event, and rejected event postbacks
* **[Optional]** for in-app events and rejected events as indicated in the column (rejected, in-app)

### Macros—installs, in-app events, and rejected events

| Postback macro (name) | Source | Send all | Description | [Base] Macros for all postbacks | [Optional] In-app and rejected events |
| --- | --- | --- | --- | --- | --- |
| <span id="advertising_id"></span>advertising\_id | SDK | Yes | User-resettable device ID, AKA GAID. Also available as: (sha1-advertiserId) | Yes |  |
| <span id="af_ad"></span>af\_ad | LINK | No | Ad Name (<Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#levels-of-data-granularity">see more</Anchor>) provided by the advertiser/publisher | Yes | Yes |
| <span id="af_ad_id"></span>af\_ad\_id | LINK | No | Provided by the advertiser/publisher | Yes | Yes |
| <span id="af_ad_type"></span>af\_ad\_type | Link | No | Use the following naming convention:<ul><li>**text:** an ad unit containing only text, for example a search result</li><li>**banner:** a basic format that appears at the top or bottom of the device screen</li><li>**interstitial:** a full-page ad that appears during breaks in the current experience</li><li>**video:** a standard video, that is non-rewarded</li><li>**rewarded\_video:** an ad unit offering in-app rewards in exchange for watching a video</li><li>**playable:** an ad unit containing an interactive preview of the app experience</li><li>**sponsored\_content:** a link included in a piece of sponsored content, like an advertorial article</li><li>**audio:** an audio ad</li></ul> | Yes | Yes |
| <span id="af_adset"></span>af\_adset | Link | No | <ul><li>Provided by the advertiser/publisher.</li><li>Adset is an intermediate level in the hierarchy between Campaign and Ad. <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#levels-of-data-granularity">See more</Anchor></li></ul> | Yes | Yes |
| <span id="af_adset_id"></span>af\_adset\_id | Link | No | Provided by the advertiser/publisher | Yes | Yes |
| <span id="af_c_id"></span>af\_c\_id | Link | No | Provided by the advertiser/publisher | Yes | Yes |
| <span id="af_siteid"></span>af\_siteid | Link | No | <ul><li>Unique ID that identifies the publisher that displays the ad. <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#site-id-parameter">Learn more</Anchor></li></ul> | Yes | Yes |
| <span id="af_subsite_id"></span>af\_subsite\_id | Link | No | <ul><li>Ad sub-network/Publisher ID.</li><li>If in addition to the main publisher (site ID), there is a sub-publisher, or you want to include additional info, such as ad type/placement within the app, like banner, interstitial, video, etc. use af\_sub\_siteid. For example: af\_sub\_siteid =ABCD\_4567</li></ul> | Yes | Yes |
| <span id="af_validated"></span>af\_validated | AF | Yes | Indicates whether the purchase was successfully validated. Possible values: true or false. | Yes |  |
| <span id="af_validation_type"></span>af\_validation\_type | AF | Yes | Indicates the type of validation performed. Possible values: roi360\_purchase, roi360\_subscription, or receipt\_validation. | Yes |  |
| <span id="app_id"></span>app\_id | SDK | Yes | The app ID as reported by the app | Yes |  |
| <span id="app_name"></span>app\_name | SDK | Yes | App name set by the advertiser | Yes |  |
| <span id="app_version"></span>app\_version | SDK | Yes | App version name set by the developer in the app code | Yes |  |
| <span id="appsflyer_id"></span>appsflyer\_id | SDK | Yes | AppsFlyer unique identifier recorded upon conversion | Yes |  |
| <span id="att01"></span>att-0-1 | SDK | Yes | Possible values:<ul><li>1: The ATT status is authorized or af\_authorized.</li><li>0: Any other ATT status.</li></ul> | Yes |  |
| <span id="attstatus"></span>att-status | SDK | Yes | The <Anchor target="_blank" href="/marketers/docs/att-implications-ios-14-and-deprecation-of-lat#att-values">ATT status</Anchor> reported by iOS. Like authorized, not\_determined.<br /><br />In some cases there is no value and "" is returned. | Yes |  |
| <span id="attributed_touch_type"></span>attributed\_touch\_type | SDK | No | Possible values: click, impression, TV, pre-install | Yes |  |
| <span id="blocked_reason"></span>blocked\_reason | AF | No | Fraud/validation rules reason | No | Rejected |
| <span id="blocked_reason_value"></span>blocked\_reason\_value | AF | No | Fraud/validation rules reason value (like site ID) | No | Rejected |
| <span id="blocked_sub_reason"></span>blocked\_sub\_reason | AF | No | Fraud/validation rules sub-reason | No | Rejected |
| <span id="bundle_id"></span>bundle\_id | SDK | Yes | iOS: Identification to match either a single app or a group of apps in iOS (See Apple developer bundle ID) Android: The app name | Yes |  |
| <span id="c"></span>c | Link | No | Provided by the advertiser/publisher. Campaign names that exceed 100 characters in length are displayed on the dashboard as "c\_name\_exceeded\_max\_length" | Yes | Yes |
| <span id="country_code"></span>country\_code | AF | Yes | Country Code using ISO 3166 (alpha-2) Example: US, CN. | Yes |  |
| <span id="event_name"></span>event\_name | SDK | Yes | Name allocated to an event | No | In-app |
| <span id="event_revenue_currency"></span>event\_revenue | SDK | Yes | Event value reported by SDK using event\_revenue\_currency or currency selected by you. | No | In-app |
| {"event_revenue"}  <br />{"_currency"} | SDK | Yes | The event revenue currency code reported in the event or the currency selected by you | No | In-app |
| <span id="event_revenue_usd"></span>event\_revenue\_USD | AF | Yes | Event value in USD | No | In-app |
| <span id="event_time"></span>event\_time | SDK | Yes | Event time | No | In-app |
| <span id="event_value"></span>event\_value | SDK | Yes | in-app event includes attributes with values, which can be sent entirely on the postback in JSON format. URL encoded using the (encode) macro. | No | In-app |
| <span id="idfa"></span>idfa | SDK | Yes | User resettable advertising ID found on iOS devices Also available as: (sha1-idfa) | Yes |  |
| <span id="idfv"></span>idfv | SDK | Yes | Unique identifier per user per vendor on IOS devices | Yes |  |
| <span id="imei"></span>imei | SDK | Yes | A unique number used to identify mobile phones | Yes |  |
| <span id="install_time"></span>install\_time | SDK | Yes | Install timestamp | Yes |  |
| <span id="install_unix_ts"></span>install\_unix\_ts | SDK | Yes | Install timestamp in unix format | Yes |  |
| <span id="is_attributed"></span>is\_attributed | AF | Yes | A flag marking if the install or event is attributed to this media source | Yes |  |
| <span id="is_contrib"></span>is\_contrib | AF | Yes | Indicates whether the ad network was among the top 3 contributors to an install.<ul><li>If the ad network did not win the attribution but is in the top 3 contributors, `is_contrib=1`.</li><li>If the ad network won the attribution, `is_contrib=0`.</li><li>If the ad network is not in the top 3 contributors, `is_contrib=0`.</li></ul> | Yes |  |
| <span id="is_lat"></span>is\_lat | SDK | Yes | Limit ad tracking (LAT): iOS: Starting iOS 14 LAT is deprecated by Apple. Determine user privacy status using ATT. In this case disregard is\_lat. Before iOS 14, if true, IDFA is not available and is set to 0. Android: When true, the user has opted-out of interest-based ads. This does not prevent the collection of GAID. | Yes |  |
| <span id="is_organic"></span>is\_organic | AF | Yes | If an install postback is sent for all media sources including organic, then the ad network will receive an indication as to whether an install was organic or non-organic. | Installs only |  |
| <span id="is_primary_attribution"></span>is\_primary\_attribution | AF | Yes | If false, see is\_retargeting. | No | In-app |
| <span id="is-reinstall"></span>is\_reinstall | AF | Yes | If true, the event is reported as <Anchor target="_blank" href="/marketers/docs/measure-reinstalls">a reinstall</Anchor>. |  |  |
| <span id="is_retargeting"></span>is\_retargeting | Link | No | Use in conjunction with is\_primary\_attribution. Learn more about <Anchor target="_blank" href="/marketers/docs/resolve-retargeting-double-attribution">double attribution of retargeting events.</Anchor><br /><br />If true (1), the event is reported as part of a retargeting campaign and the media source is the retargeting media source.<br /><br />If false (0) and is\_primary\_attribution is false, the event is part of a retargeting campaign but the media source referenced is the user attribution media source | No |  |
| <span id="language"></span>language | SDK | Yes | Language (locale) reported by the device and set by the device OS. | Yes |  |
| <span id="oaid"></span>oaid | SDK | Yes | User-resettable ID on some Android devices usually as an alternative to GAID | Yes |  |
| <span id="partner_event_id"></span>partner\_event\_id | AF | Yes | Name/ID of the corresponding event in the partner's platform | No | In-app |
| <span id="platform"></span>platform | SDK | Yes | Device platform: iOS, Android, or Windows Mobile | Yes |  |
| <span id="retargeting-conversion-type"></span>retargeting\_conversion\_type | AF | No | A flag marking if this is a re-attribution or re-engagement | Retargeting only |  |

### In-app event only macros

The examples that follow relate to in-app event postbacks available to partners.

> 📄 **Example**
>
> Event postback template "&event=(event)&json=(encode)" was translated to the following postback for a specific af\_purchase event:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> The decoded JSON value of this postback is
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

#### **Encoded values**

Postbacks may contain irregular characters, which are not alpha-numerical. To transfer these values correctly via postbacks, AppsFlyer URL-encodes non-alpha-numerical values.

To decode or encode a postback use an <Anchor target="_blank" href="https://www.urldecoder.org/">encoding web service.</Anchor>

## Sample postbacks

### General install postback examples

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)
&advertising_id=(advertiser_id)&android_id=(android_id)
&install_time=(install_unix_ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?&site_id=(publisher_id)&
device_ip=(ip)&;idfa=(idfa)&install_time=(install_unix_ts)
```

</Tab>
</Tabs>

### General in-app event postback examples

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)&
device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android_id)&
install_time=(install_unix_ts)&event_name=(event_name)&currency=(currency)&
json=(event_value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?clickid=(clickid)&site_id=(publisher_id)&
device_ip=(ip)&idfa=(idfa)&install_time=(install_unix_ts)
&event_name=(event_name)&currency=(currency)&json=(event_value)
```

</Tab>
</Tabs>

### In-app event postback example

Event Parameters:

* Event Name: af\_revenue
* Event Revenue: 120.00
* Event Currency: USD
* Event Value: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

Postback:

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="01JHFZWJT74GNA6J5MYMQBGDWX=postbacks-for-ad-networks 01JHFZWJT978TTXB7FQ6AVG1ZS=postback-data-sources 01JHFZWJTTP66NHZRG0RQAY3W8=postback-macros macros%E2%80%94installs-inapp-events-and-rejected-events=macrosinstalls-in-app-events-and-rejected-events 01JHFZWJTXD2K4RJ8RDWXKSYDD=macrosinstalls-in-app-events-and-rejected-events inapp-event-only-macros=in-app-event-only-macros 01JHFZWK3FQ5HCX9NDEKT6SPT1=in-app-event-only-macros 01JHFZWK3F2E31WE5N1G0T0ZHA=example 01JHFZWK3GM9XRS2GC4SNXFVD7=encoded-values 01JHFZWK3GJSA8RF4AMKVM4XD4=sample-postbacks 01JHFZWK3HD1NFJJW1Y8HGVPX2=general-install-postback-examples general-inapp-event-postback-examples=general-in-app-event-postback-examples 01JHFZWK3JW0D1GZ739FV0EZWG=general-in-app-event-postback-examples inapp-event-postback-example=in-app-event-postback-example 01JHFZWK3JT8GM7BEM3RXCMXV5=in-app-event-postback-example" />
