---
title: Hubscale integration with AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Hubscale
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
  created_at: '2017-12-19T12:25:07Z'
  edited_at: '2024-12-23T15:18:26Z'
  id: 115005874869
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/115005874869-Hubscale-integration-with-AppsFlyer
---
> **At a glance:** Learn how ad networks using Hubscale can integrate with AppsFlyer.

**To initiate the integration you need to send AppsFlyer**:

1. Your attribution link
2. Your postback (for installs and in-app events)

<div id="creating-the-attribution-link" />

## Creating the attribution link

the attribution link consists of the below AppsFlyer base attribution link and additional macros added by the ad network.

See below AppsFlyers base attribution link with a detailed explanation per macro:

| AppsFlyer Base URL | Description |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer endpoint |
| app\_id | Application unique ID – dynamic value changed per app promoted |
| pid | Media source name concatenated with \_int to identify integrated<br />networks |
| c | Campaign name |

See below what the complete attribution link should look like after you have added additional Hubscale macros:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id=
{offer_file_id}&advertising_id={google_aid}&idfa={ios_ifa}" target="
_blank" rel="nofollow noopener noreferrer" data-is-link="https://
app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={transaction_id}
&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id={offer_file_id}
&advertising_id={google_aid}&idfa={ios_ifa}">
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id=
{google_id}&idfa={ios_ifa}
```

<Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">AppsFlyer complete list of parameters</Anchor>

<div id="global-postbacks-for-installs-and-in-app-events" />

## Global postbacks for installs and in-app events:

Hubscale has global postbacks for installs and in-app events:

For installs:

```http
https://companyname.156th.com/conv?transaction_id={publisher_ref_id}&ios_ifa={ios_ifa}
&google_id={google_aid}&app_version={app_version}&language={language}&ext_country_code={country_code}
&ext_city={city}&user_agent={user_agent}&user_ip={device_ip}&adv_revenue={revenue_usd}
```

For post-install events, Hubscale can record up to nine post-install events for the same Transaction ID. Nine global postbacks should be created as templates as shown below:

<Table>
  <thead>
    <tr>
      <th>
        Event number
      </th>
      <th>
        URL template
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Event 2 (event 1 is the install)
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=2
        ```
      </td>
    </tr>
    <tr>
      <td>
        Event 3
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=3
        ```
      </td>
    </tr>
    <tr>
      <td>
        Event 4
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        ...
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        Event 10
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=10
        ```
      </td>
    </tr>
  </tbody>
</Table>

The Event tag is what is entered by the advertiser when mapping the events.

<Image align="center" alt="In-App_Events.png" src="https://files.readme.io/5fa9ea3c2428e0dce7ce6a8062ebdf9aca5b2f873cc4e3d76d815d83b3a72b64-360002301369.png" />

If the name of the partner using Hubscale is PARTNER, then the domain is normally: partner.156th.com.

Generic attribution link:

```http
https://app.appsflyer.com/com.appsflyer?pid=partnername_int&clickid={transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id={google_id}&idfa={ios_ifa}
```

<div id="finalizing-your-registration" />

## Finalizing your registration

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div id="mapping-of-appsflyer-parameters-and-hubscale-macros" />

## Mapping of AppsFlyer parameters and hubscale macros

| AppsFlyer Parameters | Hubscale Macros | Description |
| --- | --- | --- |
| pid | pub\_id | Media source name - for integrated partners  <br />and should not be changed. <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#partner-id-pid-parameter">More details</Anchor>. |
| c | campaign\_name | Campaign name - provided by the advertiser. |
| clickid | transaction\_id | The Ad network unique click identifier |
| af\_siteid | pub\_id | Ad Network publisher ID |
| af\_sub\_siteid | sub\_pub\_id | Ad Sub-Network/Publisher ID |
| af\_c\_id | campaign\_id | Campaign ID - provided by the advertiser |
| af\_adset |  | Adset Name - provided by the advertiser. Adset  <br />is an intermediate level in the hierarchy between  <br />Campaign and Ad. <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#levels-of-data-granularity">See more</Anchor> |
| af\_ad | adv\_name | Ad Name (<Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters#levels-of-data-granularity">see more</Anchor>) |
| af\_ad\_id | adv\_id | Ad ID |
| af\_cost\_model | adv\_payout\_model | Cost model - CPI is currently the only supported  <br />model |
| af\_cost\_currency | adv\_payout\_currency | Currency code (example: USD) |
| af\_cost\_value | adv\_payout\_amount | Cost value |

<div data-zendesk-anchors="01JFT1EB6KZE1D6C9HMXQ5A841=creating-the-attribution-link global-postbacks-for-installs-and-inapp-events=global-postbacks-for-installs-and-in-app-events 01JFT1EB6PH56T619J1197TAK2=global-postbacks-for-installs-and-in-app-events 01JFT1EB70G5V9EBMD4XMAR3GF=finalizing-your-registration 01JFT1EB71F36JD4QNB8KHKZRX=mapping-of-appsflyer-parameters-and-hubscale-macros" />
