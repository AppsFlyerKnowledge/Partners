---
title: 통합 파트너를 위한 Protect360
metadata:
  keywords:
    - Protect360
    - Ad Networks
    - Partners
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2017-09-19T08:27:29Z'
  edited_at: '2026-10-14T10:34:47Z'
  id: 115004745523
  locale: ko
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/ko/articles/115004745523
---
> **한눈에 보기:** 통합 파트너(애드 네트워크 및 대행사)는 ProtectLITE 및 Protect360 엔진에 의해 식별되고 차단된 트래픽과 관련된 프로드를 볼 수 있으며, 고객이 수동으로 정의한 유효성 검증 규칙도 확인 가능합니다.

<div id="overview" />

## 개요

앱스플라이어는 다음을 통해 프로드를 식별하고 차단합니다:

* <Anchor target="_blank" href="/marketers/ko/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">ProtectLITE</Anchor><Anchor target="_blank" href="/marketers/ko/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">: 모든 고객을 위한 기본 프로드 보호.</Anchor>
* <Anchor target="_blank" href="/marketers/ko/docs/protect360-anti-fraud-guide">Protect360</Anchor><Anchor target="_blank" href="/marketers/ko/docs/protect360-anti-fraud-guide">: 프리미엄 구독 플랜을 가진 광고주를 위한 고급 프로드 보호.</Anchor>

광고주는 다음을 허용해야 합니다:

* 애드 네트워크에 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#permissions-tab">권한</Anchor> 을 부여하여 Protect360 대시보드 및 로데이터 보고서(ProtectLITE 포함)에 **액세스하고**, 인앱 이벤트 프로드에 대한 **인앱 이벤트 데이터에 액세스**할 수 있도록 해야 합니다.
* 대행사<Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#permissions-tab">에게</Anchor>  Protect360 대시보드 및 로데이터에 액세스할 수 있는 **권한을 부여해야 합니다.**

적절한 권한이 주어지면, 통합 파트너는 다음을 수행할 수 있습니다:

* 발생한 트래픽과 관련된 데이터를 확인할 수 있습니다.
* 관련된 <Anchor target="_blank" href="/marketers/ko/docs/protect360-anti-fraud-guide#raw-data">로데이터 리포트</Anchor>를 다운로드할 수 있습니다.

애드 네트워크에서는 <Anchor target="_blank" href="/partners/ko/docs/protect360-reports-for-ad-networks">로데이터 리포트</Anchor>를 통해 클릭 및 노출 제한과 실패한 클릭 서명에 대한 정보를 확인할 수 있으며, 이는 광고주의 권한이 필요하지 않습니다.

<div id="note" />

> 📘 **참고**
>
> 대행사를 통해 애드 네트워크와 협력하는 광고주의 경우, 애드 네트워크와 대행사가 모두 데이터에 액세스하려면 광고주가 앱스플라이어에 대행사와 애드 네트워크를 모두 연동하고, 둘 다에 데이터 액세스 권한을 부여해야 합니다.
>
> 대행사만 연동하고 권한이 부여된 경우, 애드 네트워크는 데이터에 액세스할 수 없습니다.

<div id="dashboard-view" />

### 대시보드 보기

**전제 조건**: 광고주는 ProtectLITE 및 Protect360에 대한 액세스를 허가해야 합니다.

통합 파트너는 대시보드와 차트를 볼 수 있습니다. 다음 스크린샷을 참조하세요.

<Anchor target="_blank" href="/marketers/ko/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting#대시보드">ProtectLITE</Anchor> 와 <Anchor target="_blank" href="/marketers/ko/docs/protect360-anti-fraud-guide#dashboard">Protect360</Anchor> 대시보드에서 어떤 데이터를 사용할 수 있는지 더 보기.

제한 사항:

* 애드 네트워크는 이상 대시보드에 액세스할 수 없습니다. 대행사는 액세스할 수 있지만 앱스플라이어가 사용자로부터 신뢰받는 트래픽 소스에서만 데이터를 볼 수 있어야 하며, 다른 매체 소스를 비교하기 위한 기준선을 만들어야 합니다.

[altp360\_dashboard\_1.jpgalt](https://support.appsflyer.com/hc/article_attachments/30445650800913)

<div id="raw-data-reports" />

### 로데이터 리포트

**전제 조건: 광고주는 ProtectLITE 및 Protect360에 대한 액세스를 허가해야 합니다.**

Protect360 로데이터 리포트는 ProtectLITE, Protect360, 유효성 검증 규칙을 통해 확인되고 차단된 프로드를 보여줍니다.

리포트는 다음 방법으로 제공됩니다:

* 데이터 내보내기: 앱스플라이어의 사이드 메뉴에서 **리포트** > **로데이터 내보내기를 선택합니다.**
* API: 다음 [애드 네트워크 리포팅 API](/docs/protect360-for-integrated-partners#protect360-애드-네트워크-리포팅-api) 섹션을 참조하세요.

<Anchor target="_blank" href="/marketers/ko/docs/protect360-raw-data-reports">Protect360 로데이터 리포트</Anchor>에 대해 더 보기.

<div id="protect360-ad-network-reporting-api" />

## Protect360 애드 네트워크 리포팅 API

* 이 섹션에 나열된 로데이터 리포트는 API를 통해 애드 네트워크에서 사용할 수 있습니다.
* 유사한 리포트는 대시보드의 데이터 내보내기 페이지에서 확인할 수 있습니다.
* 광고주가 Protect360 구독이 없는 경우, 인스톨 리포트만 사용할 수 있습니다.

**전제 조건**

* API를 통해 광고주 데이터에 액세스하려면, 광고주는 애드 네트워크에 API로 Protect360 대시보드 및 데이터에 액세스할 수 있는 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#permissions-tab">권한</Anchor>을 부여해야 합니다. 대시보드에 액세스할 수 있는 애드 네트워크는 API를 사용할 수 있습니다. 광고주는 아무런 조치를 취할 필요가 없습니다.
* Protect360 권한이 있는 앱 목록을 보려면 <Anchor target="_blank" href="/partners/ko/docs/app-list-api-for-ad-networks">앱 목록 API 가져오기</Anchor>를 사용하세요.
* 관리자는 대시보드에서 사용할 수 있는 앱스플라이어 <Anchor target="_blank" href="/marketers/ko/docs/managing-appsflyer-tokens">V2.0 인증 토큰</Anchor>을 가져와야 합니다.

<div id="protect360-api-reports" />

#### Protect360 API 리포트

| 리포트 | 데이터 최신성 | 설명 |
| --- | --- | --- |
| 인앱 이벤트 사후 프로드 | 매일 10:00 UTC | <ul><li>사기로 식별된 인스톨에 의해 수행된 인앱 이벤트입니다.</li><li>인스톨 여부와 관계없이 사기로 판단되는 다른 인앱 이벤트입니다.</li></ul>리포트는 다음의 파라미터 표에 설명된 대로 인앱 이벤트 유형별로 선택적으로 필터링할 수 있습니다.<br /><br />리포트 주제: `fraud-post-inapps` |
| 어트리뷰션 이후 인스톨 | 매일 10:00 UTC | <ul><li>어트리뷰션 이후 사기로 식별된 인스톨.</li><li>리포트는 다음 섹션 설명대로 감지 날짜별로 선택적으로 필터링할 수 있습니다.</li></ul>리포트 주제:  detection |
| 인스톨 | 실시간 | 차단 사유로 차단된 인스톨<br /><br />리포트 주제:  blocked\_installs\_report |
| 인앱 이벤트 | 실시간 | 차단된 사용자가 수행한 인앱 이벤트<br /><br />리포트 주제: `blocked_in-app_events_report` |
| 클릭 | 실시간 | 차단된 사용자가 수행한 클릭<br /><br />리포트 주제: `blocked_clicks_report` |

<div id="procedure-for-ad-networks-to-get-protect360-reports-by-download" />

#### **광고 네트워크가 다운로드로 Protect360 보고서를 받는 절차**

**API를 사용하여 리포트를 받으려면:**

1. 이전 목록에서 필요한 리포트를 식별하세요.
2. 다음 섹션에 있는 관련 curl 예제를 사용하여 스크립트를 준비하세요.
3. 다음 자리 표시자를 교체하세요:
   1. 앱 ID
   2. 시작 날짜
   3. 종료 날짜
   4. Bearer 토큰 (앱스플라이어 <Anchor target="_blank" href="/marketers/ko/docs/managing-appsflyer-tokens">V2.0 인증 토큰</Anchor>)
4. 일부 호출에는 이 문서 에 설명된 대로 [선택적 파라미터](/docs/protect360-for-integrated-partners#api-parameters)가 있습니다.

<div id="curl-examples" />

### curl 예시

<div id="installs-blocked_installs_report" />

<Accordion title="인스톨(blocked_installs_report)">

app\_id, from, to, token 자리 표시자를 바꾸세요.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_installs_report/app/{app_id}?from={2020-07-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-installs-detection" />

<Accordion title="인스톨 후 어트리뷰션 (감지)">

app\_id, from, to, token 자리 표시자를 바꾸세요.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/detection/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additonal-fields=fraud_reason,fraud_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="inapp-event-blocked_in_app_events_report" />

<Accordion title="인앱 이벤트(blocked_in_app_events_report)">

app\_id, from, to, token 자리 표시자를 바꾸세요.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_in_app_events_report/app/?from=YYYY-MM-DD&to=YYYY-MM-DD&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-inapp-events-fraud-fraud_post_inapps" />

<Accordion title="인앱 이벤트 프로드(fraud_post_inapps)">

app\_id, from, to, token 자리 표시자를 바꾸세요.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/fraud-post-inapps/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,fraud_reason,fraud_sub_reason,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="clicks-blockedclicks_report" />

<Accordion title="클릭(blocked-clicks_report)">

app\_id, from, to, token 자리 표시자를 바꾸세요.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_clicks_report/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="protect360-ad-network-api-reference-guide" />

### Protect360 애드 네트워크 API 참조 가이드

<div id="api-basics" />

<Accordion title="API 기본사항">

Protect360 애드 네트워크 API 기본사항:

| 경로 | `https://hq1.appsflyer.com/api/adnets-data/v1/export/report_topic/app/app_id` |
| --- | --- |
| 메서드 | GET |
| 경로 파라미터 (필수) | <ul><li>`app_id`:<ul><li>앱스플라이어 대시보드에서 확인할 수 있는 앱 식별자입니다. 대시보드에 나타난 대로 정확하게 입력하세요.</li><li>iOS 앱에는 **id.** 를 접두사로 붙여야 합니다.</li></ul></li><li>:</li></ul> |
| 허용되는 콘텐츠 유형 | `application/json` |
| 인증 | <ul><li>요청 헤더에 Bearer 토큰 포함.</li><li>![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) 관리자에게 <Anchor target="_blank" href="/marketers/ko/docs/managing-appsflyer-tokens">토큰</Anchor> 페이지에서 V2.0 토큰을 요청하세요. 토큰의 길이는 약 700자입니다.</li></ul> |
| 콜 제한 | <Anchor target="_blank" href="/marketers/ko/docs/report-generation-quotas-rate-limitations">콜 제한</Anchor> |
| 날짜 범위 제한 | <ul><li>지원되는 가장 이른 날짜: 현재 데이터로부터 90일 전</li><li>이전 90일 중 31일</li></ul> |
| 행 제한 | 200K 행 |
| 리포트 특성 | <ul><li>시간대: UTC</li><li>통화: USD</li></ul> |

</Accordion>

<div id="api-parameters" />

<Accordion title="API 파라미터">

Protect360 API 파라미터:

| 파라미터 | 설명 | 형식 | 필수 |
| --- | --- | --- | --- |
| app\_id | 앱스플라이어에 표시되는 앱 ID | 문자열 | 예 |
| 시작 | 날짜 범위 시작:<ul><li>인스톨의 경우에는 인스톨 날짜입니다.</li><li>인앱 이벤트의 경우에는 이벤트 날짜입니다.</li></ul> | YYYY-MM-DD | 예 |
| 끝 | 날짜 범위 끝:<ul><li>인스톨의 경우에는 인스톨 날짜입니다.</li><li>인앱 이벤트의 경우에는 이벤트 날짜입니다.</li></ul> | YYYY-MM-DD | 예 |
| event\_name | [사후 어트리뷰션 인앱 이벤트 프로드에 대한 선택사항]<br /><br />인앱 이벤트로 이벤트를 필터하세요. 특정 이벤트에 리포트를 제한합니다. 하나 이상의 이벤트를 포함할 수 있습니다.<br /><br />사용 예: `&event_name=af_purchase,af_login` | 문자열 | 아니오 |
| 시작 감지 | [사후 어트리뷰션 인스톨에 대한 선택 사항]<br /><br />프로드 감지 시작 날짜 범위입니다. (기본값은 시작입니다.) | YYYY-MM-DD | 아니오 |
| 감지 종료 | [사후 어트리뷰션 인스톨에 대한 선택사항]<br /><br />프로드 감지 날짜 범위의 끝입니다. (기본값은 끝입니다.) | YYYY-MM-DD | 아니요 |

</Accordion>

<div id="protect360-api-http-return-codes" />

<Accordion title="Protect360 API HTTP 반환 코드">

오류 코드 및 솔루션:

| 상태 | 코드 | 증상/메시지 | 해결 방안 |
| --- | --- | --- | --- |
| 정상 | 200 | 빈 CSV 파일 | `addtional_fields`URI에서 여러 번 사용됨 |
| 정상 | 200 | 빈 CSV 파일 | 시작 및 종료 날짜가 yyyy-mm-dd 형식인지 확인하세요. |
| 정상 | 200 | 앱스플라이어 HTML 로그인 페이지가 반환됨 | Bearer 토큰 헤더에 토큰이 없습니다. |
| 잘못된 요청 | 400 | 잘못된 요청 | <ul><li>날짜 범위 제약.<ul><li>최소 허용 날짜는 현재로부터 90일 전입니다.</li><li>인스톨의 경우 기간은 60일을 초과할 수 없으며, 인앱 보고서는 90일을 초과할 수 없습니다.</li></ul></li></ul> |
| 인증되지 않음 | 401 | 인증되지 않음 | 토큰을 찾았지만 유효하지 않습니다. 귀사의 계정에 최신 V2.0 토큰이 있는지 확인하세요. 관리자에게 대시보드에서 현재 토큰을 가져오도록 요청하세요. |
| 찾을 수 없음 | 404 |  | <ul><li>지정된 종단점이 올바르지 않습니다.</li><li>앱 ID가 정확한지 확인하세요.</li><li>귀사 앱에 대한 액세스 권한이 없습니다.</li></ul> |

</Accordion>

<div id="impression-capping" />

## 노출 및 클릭 제한

애드 네트워크에 노출 또는 클릭 프로드가 매우 높으면 Protect360이 24시간 주기로 해당 애드 네트워크의 노출 또는 클릭을 차단합니다. 즉, 임계값에 도달한 후 발생하는 모든 노출/클릭은 앱스플라이어에 기록되지 않으며 어트리뷰션 대상이 아닙니다. 차단된 노출/클릭은 Protect360 대시보드와 보고서에 표시됩니다.

앱스플라이어 프로드 보호 알고리즘은 노출/클릭 수량, CVR, 감지된 프로드 비율, 정상적인 액티비티 변동, 업계 및 지리적 벤치마크, 자체 개발한 파라미터 등을 고려하여 프로드를 감지합니다. 이 알고리즘은 변화하는 트렌드를 반영하여 매시간 동적으로 업데이트됩니다.

**노출 또는 클릭 플러딩(Click Flooding) 임계값을 반복적으로 초과하면 앱스플라이어 플랫폼에서 파트너 연동이 영구적으로 제거될 수 있습니다.**

노출 및 클릭 제한 임계값:

* 모든 애드 네트워크에 공통으로 적용됩니다. 즉, 매우 높은 노출 또는 클릭 프로드 율로 인해 제한이 걸리지 않는 애드 네트워크는 없습니다.
* 앱/애드 네트워크 수준입니다. 즉, 프로드 분석은 앱의 모든 애드 네트워크 캠페인을 고려하며, 차단은 앱의 모든 애드 네트워크 캠페인의 리포팅 및 어트리뷰션에 영향을 미칩니다(해당 계정에 Protect360이 있는지 여부와 관계없음).
* 24시간 주기로 재설정되며 차단은 주기가 끝날 때까지 적용됩니다. 주기가 시작되고 끝나는 구체적인 시간은 앱스플라이어에서 비공개로 유지됩니다.
* 변경하거나 중단할 수 없습니다. Protect360은 프로드 탐지에서 매우 정밀하게 조정되며, 알고리즘을 수동으로 조정하거나 끌 수 없습니다.
* 이상한 액티비티를 보이는 캠페인과 게시자를 중단함으로써 피할 수 있습니다.

<div id="faq" />

<Accordion title="자주 묻는 질문">

노출 및 클릭 제한 FAQ:

| **질문: 네트워크 임계값이란 무엇인가요?**<br /><br />**답변**: 클릭 제한 메커니즘의 세부사항은 우회를 방지하기 위해 보호됩니다. 즉, 임계값에 도달하는 것은 인간의 행위로는 불가능한 엄청난 양의 노출/클릭이 발생해야 가능합니다. 하루 동안의 노출, 클릭 및 인스톨 볼륨을 확인하면 여러 게시자에서 비롯된 클릭 플러딩(Click Flooding) 문제가 있는지 명확하게 파악할 수 있습니다. |
| --- |
| **질문: 네트워크 차단을 어떻게 해제할 수 있나요?**<br /><br />**답변**: 네트워크는 이상한 액티비티가 있는 캠페인과 게시자를 중단하여 임계값을 피할 수 있습니다. 차단되면 네트워크는 클릭이 다시 기록될 수 있을 때까지 24시간의 주기가 끝나기를 기다려야 합니다. |
| **질문: 차단이 Protect360이 없는 앱스플라이어 고객에게도 영향을 미칩니까?**<br /><br />**답변**: 네, 고객이 Protect360을 보유했는지 여부와 상관없이 상한이 적용됩니다. 캡핑 메커니즘은 모든 고객을 클릭과 노출 남용으로부터 보호합니다. |
| **Q**: 이는 프로드가 아닙니다. 네트워크는 저렴한 소스와 협력하고 있으며, 때때로 그 품질이 낮습니다.<br /><br />**답변**: 의심스럽지 않은 출처에서 보통 수준의 성과가 좋지 않은 경우에는 클릭 제한이 적용되지 않습니다. 알고리즘은 인간일 수 없는 성과를 식별합니다. |
| **Q**: 이로 인해 캠페인을 확장할 수 없게 되며, 이러한 노출과 클릭이 차단되는 것을 원하지 않습니다.<br /><br />**답변**:  앱스플라이어의 프로드 보호 알고리즘은 극단적이고 명백한 플러딩 사례로부터 고객을 보호합니다. 이는 비인간적으로 발생한 노출과 클릭을 다루므로 확장 능력에 영향을 주지 않으며, 대부분의 차단은 책임만 발생시킵니다.  귀사에 우려 사항이 있다면 앱스플라이어에 문의하여 문제를 해결하세요. |
| **Q**: 이는 프로드가 아닙니다. 어쩌면 앱스플라이어가 노출과 클릭 볼륨을 처리하는 데 문제가 있을 수 있는 건가요?<br /><br />**답변**: 우리는 볼륨을 처리하는 데 아무런 문제가 없습니다. 우리는 세계 최대 규모의 광고주들을 지원하고 있으며, 매일 엄청난 수의 정당한 클릭을 포함해 수십억 개의 실시간 데이터를 처리합니다. 풍부하고 정확한 데이터로 대규모 성장을 지원하려는 노력의 일환으로, 우리는 고객의 이익을 위해 행동하고 클릭 플러딩의 명확한 사례를 차단합니다. |
| **질문: 인스톨 외에 클릭 수를 제한하는 접근 방식을 변경한 이유는 무엇입니까?**<br /><br />**A: 당사는 고객을 보호하기 위한 지속적인 노력의 일환으로 프로드 예방 메커니즘을 지속적으로 개선하고 있습니다. 지금까지는 노출과 클릭을 허용하고 인스톨만 차단해왔습니다. 그러나 극단적인 경우, 클릭률이 어마어마하게 높으면 그러한 경우에 우리 시스템에 수용하는 것은 의미가 없습니다.** |
| **질문: 트래픽과 노출/클릭 볼륨이 크게 증가할 것으로 예상되는 경우(예: New 캠페인으로 인해) 어떻게 대응할 수 있을까요? 차단을 방지하기 위해 무엇을 할 수 있을까요?**<br /><br />답변:** 이 알고리즘은 다양한 추세를 고려하여 매시간 동적으로 업데이트됩니다. 이 알고리즘은 급격한 수요 증가를 처리할 만큼 정교하며, 급격한 수요 증가를 포함한 일반적인 액티비티 변동에 의해 쉽게 흔들리지 않습니다. 따라서 파트너는 노출/클릭 데이터와 보고서를 활용하여 의심스러운 소스를 식별하고 해당 캠페인을 멈출 수 있습니다.** |
| **질문: 문제가 있는 트래픽을 확인하고 캠페인 성과를 개선하려면 어떻게 해야 하나요?**<br /><br />답변:** 파트너는 노출\/클릭 데이터를 통해 의심스러운 출처를 식별하고 해당 캠페인을 중단할 수 있습니다. 파트너는 Protect360\/ProtectLITE 대시보드의 전용 열에서 차단된 노출 및 클릭 데이터를 볼 수 있으며, 광고주로부터 프로드 데이터를 볼 수 있는 권한을 받은 경우에만 가능합니다.** |
| **질문: 캡핑과 관련된 알림 이메일이 네트워크에 전송되나요?**<br /><br />답: **클릭 캡핑의 경우, 앱스플라이어는 클릭 캡핑 임계값에 도달할 때마다 애드 네트워크에 이메일 알림을 보냅니다.** |

</Accordion>

<div id="click-signing" />

### 클릭 서명

애드 네트워크는 클릭에 HMAC-SHA256 <Anchor target="_blank" href="/partners/ko/docs/click-signing-for-ad-networks">서명을 추가할 수 있습니다</Anchor>.

서명은 앱스플라이어가 클릭을 검증하고 사기꾼에 의해 클릭 정보가 조작되지 않았음을 확인할 수 있게 합니다.

* 검증된 클릭은 기록되어 애드 네트워크에 귀속됩니다.
* 무효화된 클릭은 거부되며: 
  * Protect360 보고서에 데이터 집약형으로 포함되어 애드 네트워크에서만 사용할 수 있습니다 (광고주 제외).
  * 애드 네트워크의 전환율이나 클릭 캡핑 임계값에 영향을 주지 않습니다.

<div data-zendesk-anchors="overview=%EA%B0%9C%EC%9A%94 h_01HGSXTKYQB4Q1QQX4ZQS60AAJ=%EA%B0%9C%EC%9A%94 h_01HGSXTKYQN42EEMPSZMWVAMWD=%EC%B0%B8%EA%B3%A0 dashboard-view=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EB%B3%B4%EA%B8%B0 h_01HGSXTKYQPQP72R2VJB68ZDRZ=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EB%B3%B4%EA%B8%B0 rawdata-reports=%EB%A1%9C%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%A6%AC%ED%8F%AC%ED%8A%B8 h_01HGSXTKYQWRZECN905RGSEQ42=%EB%A1%9C%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%A6%AC%ED%8F%AC%ED%8A%B8 protect360-ad-network-reporting-api=protect360-%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%A6%AC%ED%8F%AC%ED%8C%85-api h_01HGSXTKYQ9388SCQTT2MX59Q9=protect360-%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%A6%AC%ED%8F%AC%ED%8C%85-api protect360-api-reports=protect360-api-%EB%A6%AC%ED%8F%AC%ED%8A%B8 h_01HGSXTKYQXZN2DMNZ09HE7355=protect360-api-%EB%A6%AC%ED%8F%AC%ED%8A%B8 procedure-for-ad-networks-to-get-protect360-reports-by-download=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C%EB%A1%9C-protect360-%EB%B3%B4%EA%B3%A0%EC%84%9C%EB%A5%BC-%EB%B0%9B%EB%8A%94-%EC%A0%88%EC%B0%A8 h_01HGSXTKYQ913MF0G38B23NYBG=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C%EB%A1%9C-protect360-%EB%B3%B4%EA%B3%A0%EC%84%9C%EB%A5%BC-%EB%B0%9B%EB%8A%94-%EC%A0%88%EC%B0%A8 curl-examples=curl-%EC%98%88%EC%8B%9C h_01HGSXTKYQX3VN5NRMNQWW4AE4=curl-%EC%98%88%EC%8B%9C h_01HGSXTKYQQBJTM4ZMMQZ0VZNH=installs-blocked_installs_report h_01HGSXTKYQ5KTCD7K63DSVS6E2=postattribution-installs-detection h_01HGSXTKYQ6MA96W8E6R2SXBS5=inapp-event-blocked_in_app_events_report h_01HGSXTKYQMMC0WNWP56Q9J0ZS=postattribution-inapp-events-fraud-fraud_post_inapps h_01HGSXTKYQEG0JXJHS7QBAEBCA=clicks-blockedclicks_report protect360-ad-network-api-reference-guide=protect360-%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-api-%EC%B0%B8%EC%A1%B0-%EA%B0%80%EC%9D%B4%EB%93%9C h_01HGSXTKYQJRE1Y9C5RSCANWT2=protect360-%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-api-%EC%B0%B8%EC%A1%B0-%EA%B0%80%EC%9D%B4%EB%93%9C h_01HGSXTKYQE24FAPYHHMFP0B3X=api-basics h_01HGSXTKYRFSZRPHNPDHNREDH2=api-parameters h_01HGSXTKYRGSQ230NVN06SP6DG=protect360-api-http-return-codes impression-and-click-capping=%EB%85%B8%EC%B6%9C-%EB%B0%8F-%ED%81%B4%EB%A6%AD-%EC%A0%9C%ED%95%9C h_01HGSXTKYRN6TP3KDYX5YZJV7N=%EB%85%B8%EC%B6%9C-%EB%B0%8F-%ED%81%B4%EB%A6%AD-%EC%A0%9C%ED%95%9C h_01HGSXTKYR8BK5A2J6TJECMKZA=faq click-signing=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85 h_01HGSXTKYR915V6E4NWGWR61PG=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85" />
