---
title: 애드 네트워크를 위한 포스트백 매크로
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
  edited_at: '2026-10-14T10:32:48Z'
  id: 207273946
  locale: ko
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ko/articles/207273946
---
> **한눈에 보기:**

* <Anchor target="_blank" href="/partners/ko/docs/advanced-privacy-guide-postback-macros-for-ad-networks">프라이버시 강화 모드</Anchor>
* <Anchor target="_blank" href="/partners/ko/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>



| <span id="postback-data-sources"></span><span id="postbacks-for-ad-networks"></span>소스 | 설명 |
| --- | --- |
| <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">어트리뷰션 링크 파라미터</Anchor> | 예: 어트리뷰션 링크의 클릭 ID 파라미터 - "&click\_id=CLICK\_ID" |
|  |  |
|  |  |
|  |  |
| 프로텍트360 및 유효성 검증 규칙 |  |


<span id="postback-macros"></span>지원되는 매크로는 다음 표에 나열되어 있습니다.

* **출처:**
  * 링크 + 어트리뷰션 링크
  * SDK: 앱 또는 서버 간 API에 내장된 앱스플라이어 SDK.
  * AF: 앱스플라이어에서 처리한 후.
* 모두 전송


| <span id="retargeting-conversion-type"></span><span id="is-reinstall"></span><span id="is_contrib"></span><span id="af_validation_type"></span><span id="af_validated"></span><span id="macrosinstalls-in-app-events-and-rejected-events"></span><span id="macros-installs-inapp-events-and-rejected-events"></span>포스트백 매크로(이름) | 소스 | 모두 전송 | 설명 |  |  |
| --- | --- | --- | --- | --- | --- |
| <span id="advertising_id"></span>advertising\_id | SDK | 예 | 사용자가 재설정할 수 있는 디바이스 ID, 일명 GAID. (sha1-advertiserId)도 사용 가능 | 예 |  |
| <span id="app_name"></span>app\_name | SDK | 예 | 광고주가 설정한 앱 이름 | 예 |  |
| <span id="appsflyer_id"></span>appsflyer\_id | SDK | 예 | 전환 시에 기록된 앱스플라이어 고유 식별자 | 예 |  |
| <span id="attributed_touch_type"></span>attributed\_touch\_type | SDK | 아니요 | UA: 가능한 값: Click, impression, TV, pre-installed | 예 |  |
| <span id="blocked_reason"></span>blocked\_reason | AF | 아니요 |  | 아니요 | 거부됨 |
| <span id="blocked_reason_value"></span>차단 이유 값 | AF | 아니요 |  | 아니요 | 거부됨 |
| <span id="blocked_sub_reason"></span>차단된 하위 이유 | AF | 아니요 |  | 아니요 | 거부됨 |
| <span id="bundle_id"></span>bundle\_id | SDK | 예 | iOS: iOS에서 단일 앱 또는 앱 그룹을 일치시키기 위한 식별(Apple 개발자 번들 ID 참조) | 예 |  |
| <span id="country_code"></span>country\_code | AF | 예 | ISO 3166(alpha-2)을 사용한 국가 코드. 예: 미국, 중국 | 예 |  |
| <span id="event_name"></span>event\_name | SDK | 예 | 이벤트에 할당된 이름. | 아니요 | 인앱 |
| <span id="event_revenue_usd"></span>event\_revenue\_USD | AF | 예 | 이벤트 값, USD | 아니요 | 인앱 |
| <span id="event_revenue"></span>event\_revenue | SDK | 예 |  | 아니요 | 인앱 |
| <span id="event_revenue_currency"></span>{"event_revenue"}  <br />{"_currency"} | SDK | 예 |  | 아니요 | 인앱 |
| <span id="event_time"></span>event\_time | SDK | 예 | 이벤트 시간 | 아니요 | 인앱 |
| <span id="event_value"></span>event\_value | SDK | 예 |  | 아니요 | 인앱 |
| <span id="idfa"></span>idfa | SDK | 예 |  | 예 |  |
| <span id="idfv"></span>idfv | SDK | 예 |  | 예 |  |
| <span id="install_time"></span>설치 시간 | SDK | 예 | 타임스탬프 설치 | 예 |  |
| <span id="install_unix_ts"></span>install\_unix\_ts | SDK | 예 |  | 예 |  |
| <span id="is_attributed"></span>is\_attributed | AF | 예 | 인스톨이나 이벤트가 이 미디어 소스에 어트리뷰션 됐음을 표시하는 플래그 | 예 |  |
| <span id="is_lat"></span>is\_lat | SDK | 예 | 광고 제한 추적 (LAT): iOS 14부터 Apple은 LAT를 더 이상 지원하지 않습니다. 앱 추적 투명성을 사용하여 유저의 개인 정보 보호 상태를 판단합니다. 이 사례에서 is\_lat을 무시하십시오. iOS 14 이전에서는 true이면 IDFA를 사용할 수 없으며 0으로 설정됩니다. 안드로이드: true인 경우, 유저는 관심 기반 광고를 거부합니다. 이렇게 되면 GAID를 수집할 수 있습니다. | 예 |  |
| <span id="is_primary_attribution"></span>is\_primary\_attribution | AF | 예 |  | 아니요 | 인앱 |
| <span id="is_retargeting"></span>리타겟팅 여부 | 링크 | 아니요 |  | 아니요 |  |
| <span id="language"></span>언어 | SDK | 예 | 장치에서 보고하고 장치 OS에서 설정하는 언어(로캘)입니다. | 예 |  |
| <span id="oaid"></span>oaid | SDK | 예 | 일부 안드로이드 디바이스에서 유저가 재설정할 수 있는 ID로, 주로 GAID의 대안으로 사용됩니다. | 예 |  |
| <span id="partner_event_id"></span>partner\_event\_id | AF | 예 | 파트너 플랫폼의 해당 이벤트 이름 및 ID | 아니요 | 인앱 |
| <span id="platform"></span>플랫폼 | SDK | 예 | 기기 플랫폼: iOS, 안드로이드, 또는 Windows Mobile | 예 |  |
| <span id="::10f35742"></span>retargeting\_  <br />conversion\_type | AF | 아니요 |  |  |  |
| <span id="app_version"></span>app\_version | SDK | 예 |  | 예 |  |
| <span id="app_id"></span>app\_id | SDK | 예 |  | 예 |  |
| <span id="att01"></span>att-0-1 | SDK | 예 | 가능한 값:<ul><li>1:</li><li>0:</li></ul> | 예 |  |
| <span id="attstatus"></span>ATT 상태 | SDK | 예 |  | 예 |  |
| <span id="af_ad"></span>af\_ad | 링크 | 아니요 | 광고주\/퍼블리셔가 제공한 광고 이름(<Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#데이터의-세분화-수준">더 보기</Anchor>) | 예 | 예 |
| <span id="af_ad_id"></span>af\_ad\_id | 링크 | 아니요 | 광고주\/퍼블리셔가 제공합니다. | 예 | 예 |
| <span id="af_adset"></span>af\_adset | 링크 | 아니요 | <ul><li>광고주\/퍼블리셔가 제공합니다.</li><li>광고세트는 캠페인과 광고 사이의 중간 데이터 계층 구조 수준입니다. <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#데이터의-세분화-수준">더 보기</Anchor></li></ul> | 예 | 예 |
| <span id="af_adset_id"></span>af\_adset\_id | 링크 | 아니요 | 광고주\/퍼블리셔가 제공합니다. | 예 | 예 |
| <span id="c"></span>c | 링크 | 아니요 | 광고주\/퍼블리셔가 제공합니다. | 예 | 예 |
| <span id="af_c_id"></span>af\_c\_id | 링크 | 아니요 | 광고주\/퍼블리셔가 제공합니다. | 예 | 예 |
| <span id="af_siteid"></span>af\_siteid | 링크 | 아니요 | <ul><li>광고를 게재하는 퍼블리셔를 식별하는 고유 ID입니다. <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#site-id-parameter">더 알아보기</Anchor></li></ul> | 예 | 예 |
| <span id="af_subsite_id"></span>af\_subsite\_id | 링크 | 아니요 | <ul><li>광고 서브 네트워크\/퍼블리셔 ID입니다.</li><li>주요 퍼블리셔(사이트 ID) 외에 하위 퍼블리셔가 있거나 앱 내 광고 유형\/배치(배너, 전면 광고, 비디오 등)와 같은 추가 정보를 포함하려면 af\_sub\_siteid를 사용하세요. 예: af\_sub\_siteid =ABCD\_4567</li></ul> | 예 | 예 |
| <span id="af_ad_type"></span>af\_ad\_type | 링크 | 아니요 | 다음 명명 규칙을 사용하세요:<ul><li>**text:** 문자만 포함하는 광고 단위, 예: 검색 결과</li><li>**배너:** 디바이스 화면 상단 또는 하단에 표시되는 기본 형식</li><li>**interstitial:** 현재 사용 중인 앱의 쉬는 시간에 표시되는 전면 광고</li><li>**video:** 표준 비디오, 비보상형</li><li>**rewarded\_video:** 동영상을 시청하면 인앱 보상을 제공하는 광고 단위</li><li>**playable:** 앱 체험을 미리보기로 제공하는 광고 단위</li><li>**sponsored\_content:** 광고 기사와 같이, 스폰서된 컨텐츠를 포함하는 링크</li><li>**audio:** 오디오 광고</li></ul> | 예 | 예 |
| <span id="imei"></span>imei | SDK | 예 |  | 예 |  |
| <span id="is_organic"></span>오가닉 여부 | AF | 예 |  |  |  |


<div id="example" />

<div id="in-app-event-only-macros" />

> 📄 **예시**
>
> 이벤트 포스트백 템플릿 "&event=(event)&json=(encode)"는 특정 af\_purchase 이벤트에 대해 다음 포스트백으로 해석됩니다.
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> 이 포스트백의 디코딩된 JSON 값은 다음과 같습니다.
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

<div id="encoded-values" />

#### **인코딩된 값**

포스트백은 영문자나 숫자가 아닌 특수 문자를 포함해야할 경우가 있습니다.

<div id="sample-postbacks" />

### 샘플 포스트백

<div id="general-install-postback-examples" />

### 일반적인 설치 포스트백 예시

<Tabs>
<Tab title="안드로이드">

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

<div id="general-in-app-event-postback-examples" />

### 일반적인 인앱 이벤트 포스트백 예시

<Tabs>
<Tab title="안드로이드">

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

<div id="in-app-event-postback-example" />

### 리치 인앱 이벤트 포스트백 예시

이벤트 파라미터:

* 이벤트 수익 120.00
* Event Currency USD

포스트백

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postback-data-sources=postbacks-for-ad-networks 01JHFZWJT74GNA6J5MYMQBGDWX=postbacks-for-ad-networks 01JHFZWJT978TTXB7FQ6AVG1ZS=postbacks-for-ad-networks 01JHFZWJTTP66NHZRG0RQAY3W8=postback-macros macros%E2%80%94installs-inapp-events-and-rejected-events=macros-installs-inapp-events-and-rejected-events 01JHFZWJTXD2K4RJ8RDWXKSYDD=macros-installs-inapp-events-and-rejected-events inapp-event-only-macros=%EC%98%88%EC%8B%9C 01JHFZWK3FQ5HCX9NDEKT6SPT1=%EC%98%88%EC%8B%9C 01JHFZWK3F2E31WE5N1G0T0ZHA=%EC%98%88%EC%8B%9C encoded-values=%EC%9D%B8%EC%BD%94%EB%94%A9%EB%90%9C-%EA%B0%92 01JHFZWK3GM9XRS2GC4SNXFVD7=%EC%9D%B8%EC%BD%94%EB%94%A9%EB%90%9C-%EA%B0%92 sample-postbacks=%EC%83%98%ED%94%8C-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JHFZWK3GJSA8RF4AMKVM4XD4=%EC%83%98%ED%94%8C-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 general-install-postback-examples=%EC%9D%BC%EB%B0%98%EC%A0%81%EC%9D%B8-%EC%84%A4%EC%B9%98-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%98%88%EC%8B%9C 01JHFZWK3HD1NFJJW1Y8HGVPX2=%EC%9D%BC%EB%B0%98%EC%A0%81%EC%9D%B8-%EC%84%A4%EC%B9%98-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%98%88%EC%8B%9C general-inapp-event-postback-examples=%EC%9D%BC%EB%B0%98%EC%A0%81%EC%9D%B8-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%98%88%EC%8B%9C 01JHFZWK3JW0D1GZ739FV0EZWG=%EC%9D%BC%EB%B0%98%EC%A0%81%EC%9D%B8-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%98%88%EC%8B%9C inapp-event-postback-example=%EB%A6%AC%EC%B9%98-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%98%88%EC%8B%9C 01JHFZWK3JT8GM7BEM3RXCMXV5=%EB%A6%AC%EC%B9%98-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%98%88%EC%8B%9C" />
