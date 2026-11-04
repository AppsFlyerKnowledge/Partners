---
title: AppsFlyerとの単一連携。
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
  edited_at: '2026-10-14T09:36:00Z'
  id: 115005874869
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/115005874869
---
> **概要：**

<div id="global-postbacks-for-installs-and-in-app-events" />

<div id="creating-the-attribution-link" />

## 計測リンクを使用する

以下のAppsFlyerの基本的な計測リンクと、各マクロの詳細な雪面を参照してください。

| AppsFlyer ベース URL | 説明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id | アプリケーション固有 ID - プロモートされたアプリごとに動的値が変更されます |
| pid | ネットワーク |
| c | キャンペーン名 |

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


```http
https://companyname.156th.com/conv?transaction_id={publisher_ref_id}&ios_ifa={ios_ifa}
&google_id={google_aid}&app_version={app_version}&language={language}&ext_country_code={country_code}
&ext_city={city}&user_agent={user_agent}&user_ip={device_ip}&adv_revenue={revenue_usd}
```

<Table>
  <thead>
    <tr>
      <th>
        event\_number
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
        イベント
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
        イベント
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
        イベント
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

![In-App_Events.png](https://files.readme.io/5fa9ea3c2428e0dce7ce6a8062ebdf9aca5b2f873cc4e3d76d815d83b3a72b64-360002301369.png)

```http
https://app.appsflyer.com/com.appsflyer?pid=partnername_int&clickid={transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id={google_id}&idfa={ios_ifa}
```

<div id="finalizing-your-registration" />

## 登録の完了

* AppsFlyerとパートナー連携を行う場合、まずは <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">こちら</Anchor>からパートナー申請を行ってください。


|  |  | <span id="mapping-of-appsflyer-parameters-and-hubscale-macros"></span>説明 |
| --- | --- | --- |
| pid | pub\_id | <Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#partner-id-pid-parameter">詳細はこちら</Anchor> |
| c | campaign\_name |  |
| clickid | トランザクションID | アドネットワークの固有となるクリックID |
| af\_siteid | pub\_id | アドネットワークパブリッシャーID |
| af\_sub\_siteid | sub\_pub\_id | アドネットワークのサブネットワーク/パブリッシャーID |
| af\_c\_id | campaign\_id |  |
| af\_adset |  | Adset  <br />  <br /><Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#データの詳細度の階層">もっと見る</Anchor> |
| af\_ad | adv\_name |  |
| af\_ad\_id | adv\_id | Ad ID |
| af\_cost\_model | adv\_payout\_model | model |
| af\_cost\_currency | adv\_payout\_currency | USD) |
| af\_cost\_value | adv\_payout\_amount | コスト値 |

<div data-zendesk-anchors="creating-the-attribution-link=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B 01JFT1EB6KZE1D6C9HMXQ5A841=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B global-postbacks-for-installs-and-inapp-events=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B 01JFT1EB6PH56T619J1197TAK2=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B finalizing-your-registration=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86 01JFT1EB70G5V9EBMD4XMAR3GF=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86 01JFT1EB71F36JD4QNB8KHKZRX=mapping-of-appsflyer-parameters-and-hubscale-macros" />
