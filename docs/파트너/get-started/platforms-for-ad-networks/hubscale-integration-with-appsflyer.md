---
title: Iterable과 앱스플라이어의 연동
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
  edited_at: '2026-10-14T10:37:39Z'
  id: 115005874869
  locale: ko
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ko/articles/115005874869
---
> **한눈에 보기:**

## 어트리뷰션 링크 사용

| 앱스플라이어 기본 URL | 설명 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id | 애플리케이션 고유 ID - 프로모션하는 앱마다 변경되는 동적 값 |
| pid |  |
| c | 캠페인 이름 |

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
        이벤트
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
        이벤트
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
        이벤트
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



| <span id="finalizing-your-registration"></span>앱스플라이어 파라미터를 추가하세요. |  | 설명 |
| --- | --- | --- |
| pid | pub\_id | <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#partner-id-pid-parameter">자세한 내용</Anchor>. |
| c | campaign\_name |  |
| 클릭아이디 | 거래\_ID | 광고 네트워크 고유 클릭 식별자 |
| af\_siteid | pub\_id | 광고 네트워크 퍼블리셔 ID |
| af\_sub\_siteid | sub\_pub\_id | 광고 하위 네트워크와 퍼블리셔 ID |
| af\_c\_id | campaign\_id |  |
| af\_adset |  | 광고세트  <br />  <br /> <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#데이터의-세분화-수준">더 보기</Anchor> |
| af\_ad | adv\_name |  |
| af\_ad\_id | adv\_id | 광고 ID |
| af\_cost\_model | adv\_payout\_model | model |
| af\_cost\_currency | adv\_payout\_currency | USD) |
| af\_cost\_value | adv\_payout\_amount | 비용 값 |

<div data-zendesk-anchors="creating-the-attribution-link=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%EC%82%AC%EC%9A%A9 01JFT1EB6KZE1D6C9HMXQ5A841=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%EC%82%AC%EC%9A%A9 global-postbacks-for-installs-and-inapp-events=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%EC%82%AC%EC%9A%A9 01JFT1EB6PH56T619J1197TAK2=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%EC%82%AC%EC%9A%A9 mapping-of-appsflyer-parameters-and-hubscale-macros=finalizing-your-registration 01JFT1EB70G5V9EBMD4XMAR3GF=finalizing-your-registration 01JFT1EB71F36JD4QNB8KHKZRX=finalizing-your-registration" />
