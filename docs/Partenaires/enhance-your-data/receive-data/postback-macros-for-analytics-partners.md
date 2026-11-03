---
title: Postback macros for analytics partners
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
  created_at: '2021-01-04T04:44:40Z'
  edited_at: '2026-08-14T16:22:42Z'
  id: 360016751637
  locale: en-us
  section: Receive data
  section_id: 6551235995281
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360016751637-Postback-macros-for-analytics-partners
---
> **At a glance:** Use macros as part of the postbacks sent to analytics partners to get relevant attribution data.

## Postbacks for analytics partners

Analytics partners can define the content and endpoints of postbacks sent to them, as part of their integration with AppsFlyer. Postbacks relate to app user engagement like installs, in-app events, re-engagements, and so on.

* **Postback configuration:** To request changes to your postback settings, use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> to open a ticket, or contact your AppsFlyer partner development manager.
* **Postback types**: Postbacks are available for install and in-app events.

## Postback macros

When included in a postback, macros are replaced with user-relevant data. For example, to get the IP address of the user installing the app, include country\_code=(ip) in the postback structure. Supported macros are listed in the following table:

* Source: Where the data originates from:
  * SDK: AppsFlyer SDK embedded in the app or server-to-server API
  * AF: After processing by AppsFlyer
* **[Base]** **Macros for all postbacks**: Macros relevant to install and in-app event.
* **[Optional]** for in-app events as indicated in the column.

#### Macros—installs and in-app events

| Postback macro (name) | Source | Description | [Base] Macros for all postbacks | [Optional] In-app events |
| --- | --- | --- | --- | --- |
| advertising\_id | SDK | User-resettable device ID, AKA GAID. Also available as: (sha1-advertiserId) | Yes |  |
| event\_name | SDK | Name allocated to an event |  | Yes |
| event\_revenue\_USD | AF | Event value in USD |  | Yes |
| event\_revenue | SDK | Event value reported by SDK using event\_revenue\_currency or currency selected by you. |  | Yes |
| event\_revenue\_currency | SDK | The event revenue currency code reported in the event or the currency selected by you. |  | Yes |
| event\_time | SDK | Event time |  | Yes |
| event\_value | SDK | in-app event includes attributes with values, which can be sent entirely on the postback in JSON format. URL encoded using the (encode) macro. |  | Yes |
| partner\_event\_id | AF | Name/ID of the corresponding event in the partner's platform |  | Yes |
| app\_name | SDK | App name set by the advertiser | Yes |  |
| appsflyer\_id | SDK | AppsFlyer unique identifier recorded on conversion | Yes |  |
| attributed\_touch\_type | AF | A flag marking if the attribution occurred due to a view-through (1 = impression, 0 = click) | Yes |  |
| country\_code | AF | Country Code using ISO 3166 (alpha-2) Example: US, CN. | Yes |  |
| idfa | SDK | User resettable advertising ID found on iOS devices Also available as: (sha1-idfa) | Yes |  |
| idfv | SDK | Unique identifier per user per vendor on IOS devices | Yes |  |
| install\_time | SDK | Install timestamp | Yes |  |
| install\_unix\_ts | SDK | Install timestamp in unix format | Yes |  |
| is\_lat | SDK | Limit ad tracking (LAT): iOS: Starting iOS 14 LAT is deprecated by Apple. Determine user privacy status using ATT. In this case disregard is\_lat. Before iOS 14, if true, IDFA is not available and is set to 0. Android: When true, the user has opted-out of interest-based ads. This does not prevent the collection of GAID. | Yes |  |
| language | SDK | Language (locale) reported by the device and set by the device OS. | Yes |  |
| app\_id | SDK | Unique app identifier in Appsflyer | Yes |  |
| app-version-name | SDK | App version set by the app developer in the app code | Yes |  |
| attributed\_touch time | AF | Time of the touch AppsFlyer attributed to | Yes |  |
| device\_type | SDK | The commercial model name of the device. Example: SM-GM284 or iPhone7 | Yes |  |
| ip | AF | IP of the user device reporting the event | Yes |  |
| match\_type | AF | Attribution method type. For example, srn, id\_matching, probabilistic | Yes |  |
| os\_version | SDK | Device operating system version | Yes |  |
| user\_agent | SDK | The URL user agent | Yes |  |
| wifi | SDK | If true, the connection was a wifi connection at the conversion time | Yes |  |
| oaid | SDK | User-resettable ID on some Android devices usually as an alternative to GAID | Yes |  |
| platform | SDK | Device platform: iOS, Android, or Windows Mobile | Yes |  |
| retargeting\_conversion\_type | SDK | A flag marking if this is a re-attribution or re-engagement | Yes |  |
| pid | AF | Ad network that the install or in-app event is attributed to | Yes |  |
| af\_ad | Link | Ad Name (<Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters#niveaux-de-granularité-des-données">see more</Anchor>) provided by the advertiser/publisher | Yes | Yes |
| af\_ad\_id | Link | Provided by the advertiser/publisher | Yes | Yes |
| af\_adset | Link | <ul><li>Provided by the advertiser/publisher.</li><li>Adset is an intermediate level in the hierarchy between Campaign and Ad. <Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters#niveaux-de-granularité-des-données">See more</Anchor></li></ul> | Yes | Yes |
| af\_adset\_id | Link | Provided by the advertiser/publisher | Yes | Yes |
| c | Link | Provided by the advertiser/publisher. Campaign names that exceed 100 characters in length are displayed on the dashboard as "c\_name\_exceeded\_max\_length" | Yes | Yes |
| af\_c\_id | Link | Provided by the advertiser/publisher | Yes | Yes |
| af\_siteid | Link | <ul><li>Unique ID that identifies the publisher that displays the ad. <Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters#site-id-parameter">Learn more</Anchor></li></ul> | Yes | Yes |
| af\_subsite\_id | Link | <ul><li>Ad sub-network/Publisher ID.</li><li>If in addition to the main publisher (site ID), there is a sub-publisher, or you want to include additional info, such as ad type/placement within the app, like banner, interstitial, video, etc. use af\_sub\_siteid. For example: af\_sub\_siteid =ABCD\_4567</li></ul> | Yes | Yes |
| af\_ad\_type | Link | Use the following naming convention:<ul><li>**text:** an ad unit containing only text, for example a search result</li><li>**banner:** a basic format that appears at the top or bottom of the device screen</li><li>**interstitial:** a full-page ad that appears during breaks in the current experience</li><li>**video:** a standard video, that is non-rewarded</li><li>**rewarded\_video:** an ad unit offering in-app rewards in exchange for watching a video</li><li>**playable:** an ad unit containing an interactive preview of the app experience</li><li>**sponsored\_content:** a link included in a piece of sponsored content, like an advertorial article</li><li>**audio:** an audio ad</li></ul> | Yes | Yes |

## In-app event only macros

The examples that follow relate to in-app event postbacks available to partners.

> 📘 **Note**
>
> **Example**
>
> Event postback template `&event=(event)&json=(encode)` was translated to the following postback for a specific af\_purchase event:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> The decoded JSON value of this postback is `{"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

### Encoded values

Postbacks may contain irregular characters, which are not alpha-numerical. To transfer these values correctly via postbacks, AppsFlyer URL-encodes non-alpha-numerical values.  
To decode or encode a postback use [an encoding web service](https://www.urldecoder.org/).

## Sample postbacks

### General install postback examples

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?pid=(media_source)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?pid=(media source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)
```

</Tab>
</Tabs>

### General in-app event postback examples

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>
</Tabs>

## In-app event postback example

**Event Parameters:**

* Event Name: af\_revenue
* Event Revenue: 120.00
* Event Currency: USD
* Event Value: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

**Postback:**

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&android_id=9aaeecc4455xxxxx&install_time=1451923560&event_name=af_purchase&currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="01JH2HWTN05T8S3P4W6CKVA7K4=postbacks-for-analytics-partners 01JH2HWTN52E8CVVGTQWK3QXW6=postback-macros macros%E2%80%94installs-and-inapp-events=macrosinstalls-and-in-app-events 01JH2HWTN7XY6B55TED4NT2KRR=macrosinstalls-and-in-app-events inapp-event-only-macros=in-app-event-only-macros 01JH2HWTVN8880HZSF6V6XZ7EF=in-app-event-only-macros 01JH2HWTVNARNYV0M9AKHQ0NDA=encoded-values 01JH2HWTVNQT0NPJ7SG9424MTQ=sample-postbacks 01JH2HWTVN4DDQ6F70WP3XE19D=general-install-postback-examples general-inapp-event-postback-examples=general-in-app-event-postback-examples 01JH2HWTVN2MH2SB6W34DH2MF7=general-in-app-event-postback-examples inapp-event-postback-example=in-app-event-postback-example 01JH2HWTVP50J5WV11DZR3RSTM=in-app-event-postback-example" />
