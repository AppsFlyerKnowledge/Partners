---
title: 与AppsFlyer对接。
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
  edited_at: '2026-10-14T09:59:26Z'
  id: 115005874869
  locale: zh-cn
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/zh-cn/articles/115005874869
---
> **概要：**

<div id="global-postbacks-for-installs-and-in-app-events" />

<div id="creating-the-attribution-link" />

## 使用归因链接

请参阅下列AppsFlyer基本归因链接，附有每个宏的详细说明：

|  | 说明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id |  |
| pid |  |
| c | 即广告系列的名称 |

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


适用于激活的验证结果：

```http
https://companyname.156th.com/conv?transaction_id={publisher_ref_id}&ios_ifa={ios_ifa}
&google_id={google_aid}&app_version={app_version}&language={language}&ext_country_code={country_code}
&ext_city={city}&user_agent={user_agent}&user_ip={device_ip}&adv_revenue={revenue_usd}
```

<Table>
  <thead>
    <tr>
      <th>

      </th>
      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

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
        活动
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
        活动
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>

      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        活动
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

<Image align="center" alt="In-App_Events.png" src="https://files.readme.io/5fa9ea3c2428e0dce7ce6a8062ebdf9aca5b2f873cc4e3d76d815d83b3a72b64-360002301369.png" />

```http
https://app.appsflyer.com/com.appsflyer?pid=partnername_int&clickid={transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id={google_id}&idfa={ios_ifa}
```



|  |  | <span id="mapping-of-appsflyer-parameters-and-hubscale-macros"></span><span id="finalizing-your-registration"></span>说明 |
| --- | --- | --- |
| pid | pub\_id | <Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#partner-id-pid-parameter">更多详情</Anchor>。 |
| c | campaign\_name |  |
| clickid | transaction\_id | 广告平台特有的点击识别参数 |
| af\_siteid | pub\_id | 广告平台的发行商ID |
| af\_sub\_siteid | sub\_pub\_id | 次级广告平台／发行商ID |
| af\_c\_id | campaign\_id |  |
| af\_adset |  | Adset  <br />  <br /><Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#数据粒度级别">详情请见此处。</Anchor> |
| af\_ad | adv\_name |  |
| af\_ad\_id | adv\_id | 即相关广告的ID |
| af\_cost\_model | adv\_payout\_model | 型号 |
| af\_cost\_currency | adv\_payout\_currency | USD |
| af\_cost\_value | adv\_payout\_amount | Cost value |

<div data-zendesk-anchors="creating-the-attribution-link=%E4%BD%BF%E7%94%A8%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT1EB6KZE1D6C9HMXQ5A841=%E4%BD%BF%E7%94%A8%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 global-postbacks-for-installs-and-inapp-events=%E4%BD%BF%E7%94%A8%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT1EB6PH56T619J1197TAK2=%E4%BD%BF%E7%94%A8%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 mapping-of-appsflyer-parameters-and-hubscale-macros=finalizing-your-registration 01JFT1EB70G5V9EBMD4XMAR3GF=finalizing-your-registration 01JFT1EB71F36JD4QNB8KHKZRX=finalizing-your-registration" />
