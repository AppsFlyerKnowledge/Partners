---
title: 광고 네트워크를 위한 SKAN 연동 가이드
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
  edited_at: '2026-10-14T10:35:56Z'
  id: 360011502657
  locale: ko
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ko/articles/360011502657
---
> **간단히 보기**: 요약: 광고 네트워크는 앱스플라이어 SKAdNetworks(SKAN)와 연동하여 캠페인을 최적화하고 생성하는 트래픽에 어트리뷰트 할 수 있습니다.

<div id="appsflyer-offering-for-ad-networks" />

## 광고 네트워크를 위한 앱스플라이어 오퍼링

**광고주 용 앱스플라이어 SKAN 솔루션 자세히 알아보기**:

<Anchor target="_blank" href="/marketers/ko/docs/skadnetwork-skan-solution-guide">SKAN 솔루션 가이드|</Anchor> <Anchor target="_blank" href="/marketers/ko/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAN 대시보드</Anchor>

* **캠페인 전환에 어트리뷰트됩니다.**
  * 앱스플라이어와의 연동을 통해 광고 네트워크는 광고주를 대신하여 실행된 캠페인을 통해 발생한 모든 인스톨, 인앱이벤트 및 수익에 어트리뷰트됩니다.
  * 연동이 없으면 인스톨, 인앱이벤트, 수익은 광고 네트워크가 아닌 오가닉으로 어트리뷰트됩니다.
* **캠페인 최적화:**
  * 포스트백의 전환 값이 인코딩됩니다.
  * 광고 네트워크는 앱스플라이어를 사용하여 각 포스트백의 전환 가치를 변환할 수 있으므로 광고 네트워크가 앱당 디코딩된 값을 기반으로 캠페인을 최적화할 수 있습니다.
* **각 광고주와 직접 연동할 필요가 없습니다.** SKAN 포스트백은 광고 네트워크로만 전송되며 광고주는 다음 중 하나를 사용하여 데이터를 사용할 수 있습니다.
  * 각 광고 네트워크와의 개별 연동. 광고 네트워크나 광고주에 대해 확장할 수 없는 솔루션입니다.
  * 앱스플라이어와의 단일 연동. 광고주와 광고 네트워크 모두에 맞게 확장 가능합니다.
* **앱스플라이어의 중요성 증가:**
  * SKAN 연동을 포함한 광고 네트워크는 앱스플라이어 대시보드에서 인증되고 식별됩니다.
  * 이로부터 광고주는 이 어트리뷰션 모델을 통해 결정론적으로 측정할 수 있는 광고 네트워크로 작업하고 있음을 확신할 수 있습니다.

<div id="skan-data-flow" />

## SKAN 데이터 흐름

<Image align="center" alt="5754_Postback_flow_for_SKAD__1_.png" src="https://files.readme.io/dff0fb00721802f59d199ae6a69f9ea7484bc0ef038c669904aa1a7c2b97dfc8-12574373654161.png" />

전체 SKAN 포스트백 흐름은 다음과 같습니다.

1. **iOS**는 어트리뷰트된 광고 네트워크에 SKAN 포스트백을 보냅니다.
2. **광고 네트워크**는 다음 기능 중 하나를 수행합니다.
   * 보강 및 전달 보강 및 전달: 광고 네트워크 캠페인 ID/소스 식별자, 캠페인 이름 및 iOS 디바이스 IP 주소로 SKAN 포스트백을 보강합니다.
   * 리디렉트
3. **앱스플라이어** 는 포스트백을 검증하고 디코드합니다. 그런 다음 디코드되고 보강된 포스트백을 광고 네트워크로 보냅니다 (또한 광고주와 공유함).

<div id="main-integration-parts" />

## 기본 연동 부분

앱스플라이어와 광고 네트워크 간의 SKAN 연동은 본 문서에 설명된 대로 다음과 같은 주요 부분으로 구성됩니다.

* 광고 네트워크가 SKAN 데이터를 앱스플라이어로 전송
* 광고 네트워크가 포스트백을 통해 앱스플라이어로부터 보강되고 디코드된 데이터 수신

<div id="send-data-to-appsflyer" />

## 앱스플라이어로 데이터 전송

광고 네트워크는 디바이스에서 SKAN 포스트백을 수신한 후 다음 방법 중 하나를 사용하여 이를 앱스플라이어로 전달합니다.

* 보강 및 전달(POST)
* 리디렉트(HTTP 307 리디렉트 메서드)

앱스플라이어는 SKAN 포스트백을 수신하면 다음을 수행합니다.

* 디코딩한 포스트백을 광고 네트워크로 보냅니다.
* 광고주가 대시보드와 리포트를 통해 어트리뷰션 데이터를 사용할 수 있도록 합니다.

<div id="enrich-and-forward" />

<Accordion title="보강 및 전달">

광고 네트워크는 이 메서드를 사용하여 디바이스에서 수신한 각 포스트백을 앱스플라이어로 전달합니다.

**광고 네트워크:**

* iOS 기기에서 포스트백을 수신합니다.
* [필수 사항] 다음 항목으로 포스트백을 보강합니다.  
  * 광고 네트워크 캠페인 ID 및 캠페인 이름.
  * iOS 디바이스에서 보낸 포스트백의 타임 스탬프.
* [선택 사항] 다음 항목으로 포스트백을 보강합니다.
  * 디바이스에서 받은 IP 주소로, 주로 지역 확인을 위해 필요합니다.
  * 광고 세트 ID 및 이름
  * 광고 ID 및 이름
  * 애드 네트워크 이름
  * 국가 코드
  * 소스 앱 ID
  * 광고소재
  * 채널
* 포스트백을 앱스플라이어에 전송
* **참고! 참고! 앱스플라이어에 포스트백을 보내기 전에 발신 포스트백의 콘텐츠를 사용하여 Apple** 어트리뷰션 서명/strong>을 검증하여 실수로 데이터가 손상되지 않도록 합니다.

<div id="skan-enriched-postback-protocol" />

#### SKAN 강화 포스트백 프로토콜

| 앤드 포인트 | `https://skadpostbacks.appsflyer.com/api/postbacks` |
| --- | --- |
| HTTP 메서드 | POST |
| 허용되는 콘텐츠 유형 | `application/json` |
| 리턴 코드 | 200 OK 200 OK: 수신한 포스트백의 형식이 잘못되었습니다.<br /><br />400: 잘못된 요청 400: 잘못된 요청: 잘못된 형식의 JSON, 비어 있는 값, JSON, 필수 필드 누락. |

<div id="skan-enriched-postback-json-parameters" />

#### SKAN 보강 포스트백 JSON 파라미터

| 파라미터 | 형식 | 설명 | 소스 |
| --- | --- | --- | --- |
| 버전 | 문자열 | SKAdNetwork 버전<br /><br />예: `"version":"2.0"` | SKAN 포스트백 |
| ad-network-id | 문자열 | 애드 네트워크 ID<br /><br />예: `"ad-network-id":" abc123defg.SKAdnetwork"` | SKAN 포스트백 |
| ad-network-name | 문자열 | <ul><li>광고 네트워크의 이름</li><li>예: `ad_network_name=your_network`</li></ul> | 애드 네트워크 |
| ad-network-country-code | 문자열 | <ul><li>광고 네트워크에서 산생한 사용자 위치(지역)입니다.</li><li><Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO</Anchor> 3166(알파-2) 코드를 사용하여 채웁니다.</li><li>예: CN, ZA</li><li>광고 네트워크는 종종 특정 캠페인의 타겟 지역에 따라 지역을 산생합니다.</li><li>앱스플라이어는 리포트 및 대시보드의 지역 관련 필드를 국가 코드로 채웁니다.</li></ul> | 애드 네트워크 |
| campaign-id | 정수 | <ul><li>SKAN 3 이하에만 해당</li><li>SKAdNetwork 캠페인 ID</li><li>예: `"campaign-id":23`</li></ul> | SKAN 포스트백 |
| transaction-id | 문자열 | SKAdNetwork 포스트백 트랜젝션 ID | SKAN 포스트백 |
| app-id | 정수 | <ul><li>앱스플라이어에 나타나는 타겟 앱 ID입니다. 항상 접두사 id가 있습니다.</li><li>예:`app_id=id123456789`</li></ul> | SKAN 포스트백 |
| 어트리뷰션 서명 | 문자열 | 어트리뷰션 서명 | SKAN 포스트백 |
| 재다운로드 | Boolean | redownload = true이면 사용자가 앱 스토어에서 앱을 다시 다운로드했음을 의미합니다. | SKAN 포스트백 |
| source-app-id | 정수 | <ul><li>소스 앱 ID(퍼블리셔)</li><li>[애플 문서](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)참조</li></ul> | SKAN 포스트백 |
| conversion-value | 정수 | 앱스플라이어 SDK는 광고주 설정에 따라 전환 가치를 설정합니다.<br /><br />**참고**!<ul><li>iOS 프라이버시 보호 임계값으로 인해 iOS는 포스트백의 파라미터를 채우지 못할 수 있으며 이 때 값은 null이 됩니다.</li><li>Null과 0은 서로 다른 의미를 가집니다.<ul><li>Null: iOS에서 전환 가치를 보류</li><li>0: 0: 사용자가 앱을 인스톨했지만 측정된 작업을 수행하지 않았습니다.</li></ul></li></ul> | SKAN 포스트백 |
| ad-network-campaign-id | 문자열 | 광고 네트워크와 광고주, 앱스플라이어 간에 공통 언어를 활성화하려면 캠페인 ID를 제공해야 합니다. | 애드 네트워크 |
| ad-network-campaign-name | 문자열 | 광고 네트워크 캠페인 ID와 연결된 광고 네트워크 캠페인 이름입니다. 이 이름은 대시보드와 리포트에 표시됩니다. | 애드 네트워크 |
| ad-network-adset-id | 문자열 | 광고 네트워크 광고 세트 ID | 애드 네트워크 |
| 애드 네트워크 광고 세트 이름 | 문자열 | 광고 네트워크 광고 세트 이름 | 애드 네트워크 |
| ad-network-ad-name | 문자열 | Ad network ad name | 애드 네트워크 |
| ad-network-ad-id | 문자열 | 광고 네트워크 광고 ID | 애드 네트워크 |
| ip | 문자열 | <ul><li>포스트백을 보내는 장치의 IP 주소입니다.</li><li>iPv4 및 IPv6 주소가 지원됩니다.</li><li>예: `"ip":"198.51.100.1"`</li></ul> | 애드 네트워크 |
| 타임스탬프 | 문자열 | <ul><li>광고 네트워크가 SKAN 포스트백을 수신한 시간입니다.</li><li>예시: 2020년 8월 4일 07:25 UTC는 다음과 같이 변환됩니다.</li></ul> | 애드 네트워크 |
| fidelity-type | 정수 | <ul><li>어트리뷰션에 영향을 미치는 광고 표현 방법을 구분합니다. 다음과 같이 0과 1의 값으로 표시됩니다.<ul><li>시청 기반 광고 (0)</li><li>StoreKit 광고 (1)</li></ul></li><li>SKAN V2.2부터 필수 필드</li></ul> | SKAN 포스트백(V2.2+) |
| did\_win | Boolean | <ul><li>설치에 기여[하거나 기여](https://developer.apple.com/documentation/storekit/SKAdnetwork/SKAdnetwork_release_notes/SKAdnetwork_version_3_0_release_notes) 한 캠페인을 구별하는 데 사용됩니다 .</li><li>진실이라면, 캠페인은 인스톨을 가져온 것으로 간주됩니다.</li><li>false이면 캠페인은 인스톨을 기여하는 것으로 인식됩니다.</li></ul> | SKAN 포스트백(V3.0+) |
| ad-network-source-app-id | 문자열 | 광고를 게시하는 앱과 연결하는 *게시자 ID* 로 채웁니다. 일반적으로 Apple에서 생성한 ID가 아니라 게시자에게 할당한 ID입니다. | 애드 네트워크 |
| postback-sequence-index | 정수 | <ul><li>스칸 4+ 전용</li><li>값은 시퀀스 번호(SKAN 창) 중0,`0`10`1`21 중 하나를 나타냅니다.</li></ul> | SKAN 4.0 포스트백(iOS 16.2) |
| coarse-conversion-value | 문자열 | <ul><li>스칸 4+ 전용</li><li>첫 번째 포스트백의 경우 계층 1에만 사용할 수 있습니다. 두 번째 및 세 번째 포스트백의 경우 계층 1-3에 사용할 수 있습니다. [애플 문서](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)참조</li></ul> | SKAN 4.0 포스트백(iOS 16.2) |
| source-identifier | 문자열 | <ul><li>스칸 4+ 전용</li><li>값은 최대 4자리까지 가능합니다.</li><li>첫 번째 포스트백의 경우 계층 2-3에 대해 최대 4자리, 계층 0-1에 대해 2자리를 사용할 수 있습니다. 두 번째 및 세 번째 포스트백의 경우 계층 1-3에 대해 2자리 숫자를 사용할 수 있습니다. 계층 0의 경우 포스트백이 없습니다. [애플 문서](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)참조</li></ul> | SKAN 4.0 포스트백(iOS 16.2) |
| source-domain | 문자열 | <ul><li>스칸 4+ 전용</li><li>값은 어트리뷰션이 가능한 웹 광고의 소스를 나타냅니다. `example.com` example.com예시</li><li>[애플 문서](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)참조</li></ul> | SKAN 4.0 포스트백(iOS 16.2) |
| 광고 소재 | 문자열 | <ul><li>SKAN 4+에만 해당됩니다.</li><li>추가 캠페인 세분성을 위해 source\_identifier 에서 추가 숫자를 사용할 때 사용할 수 있습니다.</li></ul> | 애드 네트워크 |
| channe | 문자열 | <ul><li>SKAN 4+에만 해당됩니다.</li><li>추가 캠페인 세분성을 위해 source\_identifier 에서 추가 숫자를 사용할 때 사용할 수 있습니다.</li></ul> | 애드 네트워크 |

<div id="curl-exampleenriched-skan-3-postback" />

#### **Curl 예제 - 강화된 SKAN 3 포스트백**

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

<div id="curl-exampleenriched-skan-4-postback-with-fine-conversion-values" />

#### **curl 예제 - 미세 변환 값으로 강화된 SKAN 4 포스트백**

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

<div id="curl-exampleenriched-skan-4-postback-with-coarse-conversion-values" />

#### curl 예제 - 코스 변환 값으로 강화된 SKAN 4 포스트백

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

<Accordion title="리다이렉트">

<Image align="center" alt="Redirect_us-en__2_.png" src="https://files.readme.io/17d4a668cde784a2f823e702e04fc75a2bbbdb483e44d9d10edfad03d865bbb7-360012352758.png" />

이 방법을 사용하여 광고 네트워크는 HTTP 리디렉션 명령(307)으로 디바이스에 응답하여 디바이스에 앱스플라이어에 직접 포스트백을 전송하도록 요청합니다. 

리디렉션 방법에는 다음과 같은 장점이 있습니다:

<div id="implementation" />

#### **구현하기**

1. 포스트백을 *[https://skadredirect.appsflyer.com/api/redirects](https://skadredirect.appsflyer.com/api/redirects)*로 리디렉션하는 HTTP 307 응답으로 응답하도록 서버를 구성합니다.
2. 다음 표에 나열된 쿼리 매개 변수를 사용하여 캠페인 세부 정보가 포함된 쿼리 매개 변수를 추가합니다. 캠페인 세부 정보 전송을 필수로 간주하십시오. 캠페인 세부 정보를 통해 비용 및 기타 캠페인 데이터로 SKAN 데이터를 보강하고 광고주가 캠페인을 효과적으로 최적화할 수 있습니다.

**리디렉션 URL 예**

```http
https://skadredirect.appsflyer.com/api/redirects?
  &ad-network-campaign-id=243232&ad-network-campaign-name=yarg_campaign_name
  &ad-network-adset-name=dsdsa&creative=examplecreative&channel=channelexample
```

<div id="query-params-for-campaign-details-not-mandatory" />

#### 캠페인 세부 정보에 대한 쿼리 매개 변수(필수 아님)

| Query param | 설명 |
| --- | --- |
| ad-network-name | <ul><li>광고 네트워크의 이름</li><li>`ad_network_name=your_network` ad\_network\_name=your\_network예시</li></ul> |
| ad-network-campaign-id | 캠페인 ID |
| ad-network-campaign-name | 캠페인 이름 |
| ad-network-adset-id | 광고세트 ID |
| 애드 네트워크 광고 세트 이름 | 광고 세트 이름 |
| ad-network-ad-id | 광고 ID |
| ad-network-ad-name | 광고 이름 |
| ad-network-country-code | <ul><li>광고 네트워크에서 산생한 사용자 위치(지역)입니다.</li><li><Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO</Anchor> 3166(알파-2) 코드를 사용하여 채웁니다.</li><li>예: CN, ZA</li><li>광고 네트워크는 종종 특정 캠페인의 타겟 지역에 따라 지역을 산생합니다.</li><li>앱스플라이어는 리포트 및 대시보드의 지역 관련 필드를 국가 코드로 채웁니다.</li></ul> |
| ad-network-source-app-id | 광고를 게시하는 앱과 연결하는 게시자 ID 로 채웁니다. 일반적으로 Apple에서 생성한 ID가 아니라 게시자에게 할당한 ID입니다. |
| ip | <ul><li>포스트백을 보내는 장치의 IP 주소입니다.</li><li>iPv4 및 IPv6 주소가 지원됩니다.</li><li>`"ip":"198.51.100.1"` "ip":"198.51.100.1"예시</li></ul> |
| 타임스탬프 | <ul><li>광고 네트워크가 SKAN 포스트백을 수신한 시간입니다.</li><li>예시: 2020년 8월 4일 07:25 UTC는 다음과 같이 변환됩니다.</li></ul> |
| 광고 소재 | <ul><li>SKAN 4+에만 해당됩니다.</li><li>추가 캠페인 세분성을 위해 source\_identifier 에서 추가 숫자를 사용할 때 사용할 수 있습니다.</li></ul> |
| channe | <ul><li>SKAN 4+에만 해당됩니다.</li><li>추가 캠페인 세분성을 위해 source\_identifier 에서 추가 숫자를 사용할 때 사용할 수 있습니다.</li></ul> |

</Accordion>

<div id="receive-data-from-appsflyer" />

## 앱스플라이어에서 데이터 수신

첫 번째 포스트백을 받기 전에 다음 사항을 고려하십시오.

* 광고 네트워크는 포스트백 엔드포인트와 템플릿을 정의해야 합니다(  <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">파트너 어시스턴트 위젯</Anchor>을 사용하여 앱스플라이어 파트너 개발 매니저에게 연락하여 이를 제대로 구현 해야 함).
* 앱스플라이어는 사용자에게 전송된 기존 포스트백과 동일한 메커니즘을 사용하여 SKAN 포스트백을 전송합니다.

<div id="principles" />

<Accordion title="원칙">

* 광고 네트워크에서 앱스플라이어로 전송된 각 포스트백에 대해 앱스플라이어는 다음을 전송합니다:
  * 한 번의 설치 포스트백. 다시 다운로드는 다시 다운로드 파라미터에 의해 신호를 받습니다.
  * 인앱 이벤트 포스트백이 0개에서 여러 개입니다. 정확한 숫자는 전환 값의 변환에 따라 다릅니다. 시뮬레이션된 포스트백을 참조하십시오.

</Accordion>

<div id="postback-macros-available-to-ad-network-partners" />

<Accordion title="광고 네트워크 파트너가 사용할 수 있는 포스트백 매크로">

<table><thead><tr><th><p>포스트백 매크로(이름)</p></th><th><p>설명</p></th><th>형식 및 예</th><th>인앱 이벤트에만 해당</th></tr></thead><tbody><tr><td><p>site_id</p></td><td><p>광고를 게시하는 앱(원본 앱 ID)</p></td><td><p>문자열: 876534</p></td><td></td></tr><tr><td><p>설치 시간</p></td><td><p>앱스플라이어가 <em>업데이트 전환</em> 창을 기준으로 추정합니다. 10자리 UNIX epoch 타임스탬프 또는 사람이 읽을 수 있는 타임스탬프로 제공</p></td><td><ul><li>문자열: 1596119460 </li><li>2020년 7월 30일 14:31 UTC로 변환됩니다.</li></ul></td><td> </td></tr><tr><td><p>skadnetwork_ad_network_time</p></td><td><p>iOS 기기에서 광고 네트워크에 포스트백을 수신한 시간입니다. 광고 네트워크에서 보고합니다. 10자리 UNIX epoch 타임스탬프 또는 사람이 읽을 수 있는 타임스탬프로 제공</p></td><td><ul><li>문자열: 1596119460 </li><li>2020년 7월 30일 14:31 UTC로 변환</li></ul></td><td> </td></tr><tr><td><p><br/>skadnetwork_received_time</p></td><td><p>Time AppsFlyer는 광고 네트워크로부터 포스트백을 수신했습니다. 10자리 UNIX epoch 타임스탬프 또는 사람이 읽을 수 있는 타임스탬프로 제공</p></td><td><ul><li>문자열: 1596119460 </li><li>2020년 7월 30일 14:31 UTC로 변환</li></ul></td><td></td></tr><tr><td><p>event_name</p></td><td><p>이벤트 이름 </p><ul><li>af_skadnetwork_revenue</li><li>af_로그인</li><li>af_skadnetwork_revenue</li><li>또는 광고주가 설정한 대로  </li></ul></td><td><p>String: af_skadnetwork_revenue, abc123</p></td><td><p>예</p></td></tr><tr><td><p>수익</p></td><td><p>지정된 통화 코드를 사용한 수익 금액</p></td><td><p>숫자 5, 20, 0.4</p></td><td><p>예</p></td></tr><tr><td><p>통화</p></td><td><p>통화 코드는 광고주가 설정한 앱별 통화입니다.</p></td><td><p>문자열: EUR, USD, ZAR</p></td><td><p>예</p></td></tr><tr><td><p>attribution_source</p></td><td><p>어트리뷰션 데이터의 출처:</p><p>SKAdNetwork SKAdNetwork</p></td><td><p>문자열: SKAdNetwork</p></td><td></td></tr><tr><td><p>app_id</p></td><td><p>앱 ID(광고주 앱)</p></td><td><p>문자열: ID123456790</p></td><td></td></tr><tr><td><p>country</p></td><td><p>광고 네트워크에 의해 결정된 설치 지역(국가)</p></td><td><p>문자열: US, UK, ZA </p></td><td></td></tr><tr><td><p>campaign</p></td><td><p>광고 네트워크에서 포스트백으로 전송된<em>d-network-campaign-name</em> 을 사용하여 채워진 캠페인 이름</p></td><td><p>문자열: UA_US_23+</p></td><td></td></tr><tr><td><p>campaign_id</p></td><td><p>광고 네트워크에서 포스트백으로 전송된 광고 네트워크 캠페인 ID를 사용하여 채워진 <em>광고 네트워크 캠페인 ID</em>. <strong>참고</strong>: 참고: SKAN 4의 경우 이 값은 항상 null입니다.</p></td><td><p>문자열: 3456745</p></td><td></td></tr><tr><td><p>재다운로드</p></td><td><p>가능한 값: 참, 거짓</p><p>다시 다운로드 = true이면 사용자가 앱 스토어에서 앱을 다시 다운로드했음을 의미합니다.</p></td><td><p>불 값: 참/거짓</p></td><td></td></tr><tr><td><p>skadnetwork_ambiguous_event</p></td><td><p>광고주가 대시보드에서 SKAN 설정을 변경한 후 처음 72시간 동안 수신된 이벤트입니다. SKAN 앱스플라이어에서 사용하는 다양한 타이머로 인해 이벤트를 정확하게 매핑할 수 없습니다.</p><ul><li> </li></ul></td><td><p>불 값: 참/거짓</p></td><td></td></tr><tr><td><p>skadnetwork_campaign_id</p></td><td>오리지널 SKAN 포스트백에서 제공한 SKAN 캠페인 ID</td><td><p>56, 23</p></td><td></td></tr><tr><td><p>af_skadnetwork_nonce</p></td><td>파트너가 중복된 포스트백을 식별할 수 있도록 하는 고유한 임의 식별자</td><td></td><td></td></tr><tr><td><p>event_id</p></td><td>광고 네트워크 플랫폼에서 해당<span> </span><span>이벤트</span><span> </span>의 이름/ID</td><td></td><td><p>예</p></td></tr><tr><td><p>거래_ID</p></td><td><p><span>SKAN 포스트백 트랜잭션 ID</span></p><p><span><strong>참고</strong>: 참고: 광고주는 transaction_id 공유할 수 있도록 명시적으로 허용해야 합니다. 광고주에게 통합 탭에서 그렇게 하도록 요청합니다.</span></p></td><td></td><td></td></tr><tr><td>애드 네트워크 광고 세트 ID</td><td>광고 네트워크에 의해 iOS 포스트백에 추가됨</td><td>문자열</td><td> </td></tr><tr><td>애드 네트워크 광고 세트 이름</td><td>광고 네트워크에 의해 iOS 포스트백에 추가됨</td><td>문자열</td><td> </td></tr><tr><td>애드 네트워크 광고 이름</td><td>광고 네트워크에 의해 iOS 포스트백에 추가됨</td><td>문자열</td><td> </td></tr><tr><td>애드 네트워크 광고 ID</td><td>광고 네트워크에 의해 iOS 포스트백에 추가됨</td><td>문자열</td><td> </td></tr><tr><td>SKAN_min_event_counter</td><td>참고 (1) 참조</td><td><p>정수</p></td><td>예</td></tr><tr><td>SKAN_max_event_counter</td><td>참고 (1) 참조</td><td><p>정수</p></td><td>예</td></tr><tr><td>SKAN_min_time_post-install</td><td>참고 (2) 참조</td><td><p>정수</p></td><td>예</td></tr><tr><td>SKAN_max_time_post-install</td><td>참고 (2) 참조</td><td><p>정수</p></td><td>예</td></tr><tr><td>SKAN_min_event_revenue</td><td>일러두기 (3)을 참조하십시오.</td><td>실수</td><td>예</td></tr><tr><td>SKAN_max_event_revenue</td><td>일러두기 (3)을 참조하십시오.</td><td><p>실수 </p></td><td>예</td></tr><tr><td>fidelity-type</td><td><p>어트리뷰션에 영향을 미치는 <span>광고 표현 방법을 구분합니다</span>. 다음과 같이 0과 1의 값으로 표시됩니다.</p><ul><li><span>시청 기반 광고 (0)</span></li><li>StoreKit 광고 (1)</li></ul></td><td>정수</td><td> </td></tr><tr><td>skad_af_attribution_flag</td><td><p>사용자가 <span>단일 진성원 메커니즘</span>을 사용하는 앱스플라이어에 의해 어트리뷰트되었음을 표시하는 데 사용됩니다. </p></td><td>Boolean</td><td> </td></tr><tr><td><span>skad_포스트백_서열_인덱스</span></td><td><ul><li>값은 SKAN 기간, 즉 0, 1 또는 2를 나타냅니다.</li><li>SKAN 3의 경우 값은 0</li></ul></td><td><span>정수</span></td><td> </td></tr><tr><td><span>skad_coarse_conversion_value</span></td><td><ul><li> </li><li>SKAN 3의 경우 값은 0</li></ul></td><td><span>문자열</span></td><td> </td></tr><tr><td><span>skad_source_identifier</span></td><td><ul><li>값은 최대 4자리까지 가능합니다.</li><li>SKAN 3의 경우 값은 0</li></ul></td><td><span>문자열</span></td><td> </td></tr><tr><td><span>skad_source_domain</span></td><td><ul><li>값은 어트리뷰션이 가능한 웹 광고의 소스를 나타냅니다.</li><li>SKAN 3의 경우 값은 0</li></ul></td><td><span>문자열</span></td><td> </td></tr><tr><td><span>애드 네트워크 크리에이티브</span></td><td><ul><li>값은 애드 네트워크에서 수신한 데이터 보강에 기반합니다.</li><li>SKAN 3의 경우 값은 0</li></ul></td><td><span>문자열</span></td><td> </td></tr><tr><td><span>애드 네트워크 채널</span></td><td><ul><li><span>SKAN 4+에만 해당됩니다.</span></li><li>추가 캠페인 세분성을 위해 <span>source_identifier</span> 에서 추가 숫자를 사용할 때 사용할 수 있습니다.</li></ul></td><td><span>문자열</span></td><td> </td></tr><tr><td colspan="4"><p>참고:</p><ol><li> 이벤트 발생 <br/><code>[round up (SKAN_min_event_counter+SKAN_max_event_counter) / 2]</code><br/>참고! 값은 가장 가까운 정수로 반올림되게 됩니다.</li></ol><ul><li>예시: <ul><li>A. A. min=0이고 max=1이면 이벤트 수는 1입니다.</li><li>B. A. min=0이고 max=1이면 이벤트 수는 1입니다.</li></ul></li><li> 인스톨 시간 결정: 터스텀 전환을 구현하는 광고주의 경우 앱스플라이어는 인스톨 시간을 포스트백 도착 시간 - 48시간- 평균(min_time_post_install + max_time_post_install)으로 계산합니다. 광고 네트워크는 이러한 매크로를 사용할 필요가 없습니다.   </li><li> 수익 결정: 앱스플라이어는 이 값을 사용하여 최소 및 최대의 평균을 계산하여 이벤트의 수익을 결정합니다. 광고 네트워크는 이러한 매크로를 사용할 필요가 없습니다.  </li></ul></td></tr></tbody></table>

</Accordion>

<div id="skan-postback-examples" />

<Accordion title="SKAN 포스트백 예시">

**앱스플라이어에서 보낸 인스톨 SKAN 포스트백의 예시**

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

**앱스플라이어에서 보낸 인앱 SKAN 포스트백의 예시**

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

<div id="integration-testing" />

## 연동 테스트

앱스플라이어와의 연동을 검증하려면 다음 방법 중 하나 또는 둘 다를 사용하십시오. 

* 실제 SKAN 포스트백: 네트워크에서 수신한 실제 SKAN 트래픽에 기반
* 시뮬레이션된 포스트백: 앱스플라이어 테스트 앱 기반

**iOS 디바이스에서 실제 SKAN 포스트백을 수신하기 위해 광고 네트워크는 다음 처리를 완료합니다.**

* 애플에 등록하기
* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/generating_the_signature_to_validate_storekit-rendered_ads">SKAdNetwork 서명으로 광고에 서명합니다</Anchor>.
* 퍼블리셔 앱 퍼블리셔 앱: info.plist 파일에 네트워크 ID를 추가하고 /a>광고 노출 시 <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/generating_the_signature_to_validate_an_installation">loadProduct 함수를 호출</Anchor> 합니다.
* V6.0.3 이전 버전은 지원되지 않습니다.

**시뮬레이션된 포스트백을 받으려면:**

* <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">파트너 지원 위젯</Anchor>을 사용하여 연락하여 시뮬레이션 앱과의 연동을 요청합니다.
* [다음 섹션의](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks)목록에서 앱의 ID를 지정합니다.

<div id="real-environment" />

<Accordion title="실제 환경">

광고 네트워크는 이 방법을 사용하여 라이브 앱에서 앱스플라이어에 실제 SKAN 포스트백을 전송합니다.

<div id="testing-integration" />

#### 테스트 통합

| 책임 | 작업 |
| --- | --- |
| 애드 네트워크 | Apple에서 제공하는 SKAN 네트워크 ID에 관해 파트너 개발 관리자를 통해(또는 파트너 지원 위젯을 사용하여) 앱스플라이어에 알립니다. |
| 광고 네트워크 및 앱스플라이어 | 포스트백 통합 인증에 사용할 상호 고객(최신 AppsFlyer SDK를 통합)에 동의합니다. |
| 애드 네트워크 | 본 기사에서 설명한 방법 중 하나를 사용하여 앱 SKAN 포스트백을 앱스플라이어로 보냅니다. |
| 앱스플라이어 | 광고주에 의해 설정된 변환 값 매핑에 따라 디코딩된 포스트백을 광고 네트워크로 보냅니다. |

<div id="test-criteria" />

#### 테스트 기준

| 책임 | 작업 |
| --- | --- |
| 애드 네트워크 | 합의된 상호 고객에 대해 지정된 기간 동안 전송된 SKAN 포스트백의 수량에 대해 앱스플라이어에 알립니다. |
| 앱스플라이어 | 수신된 포스트백 수와 광고 네트워크에서 보낸 포스트백 수를 확인합니다. |
| 앱스플라이어 | 광고 네트워크와 특정 앱에 대해 네트워크로 전송된 포스트백 수를 유형별로 분류하여 공유합니다:<ul><li>포스트백 설치/다시 다운로드</li><li>인앱 포스트백.</li></ul>참고: 참고: 확률적 포스트백에 동일한 엔드포인트를 사용하는 경우 *attribution\_source=skad network*/span>를 사용하여 SKAN 네트워크 포스트백을 다른 포스트백과 구별하여 필터링해야 합니다. |

</Accordion>

<div id="simulated-postbacks" />

<Accordion title="시뮬레이션된 포스트백">

* 이 방법을 사용하여 광고 네트워크는 아래 표에 설명된 대로 앱스플라이어에 미리 준비된 포스트백을 앱스플라이어 테스트 앱으로 전송합니다. 앱스플라이어는 디코딩된 포스트백으로 광고 네트워크에 응답합니다.
* 각 테스트 앱에는 표에 설명된 대로 서로 다른 전환 값 매핑이 있습니다.

| 앱 ID | 변환 모드 | 지침 |
| --- | --- | --- |
| <span id="id888707085"></span>id888707085 | 수익, $1 단위<br /><br />예상 결과: | <ol><li>통합 탭에서 i**n-app 이벤트 포스트백을 활성화합니다**.</li><li>이벤트 이름 af\_SKAN\_revenue을 선택하고 이벤트 식별자에 매핑합니다.</li><li>구성을 저장합니다.</li><li>포스트백에서 전송 전환 가치 = 7.</li><li>앱스플라이어는 다음과 같이 응답합니다:<ul><li>인스톨 포스트백</li><li>$7 가치의 af\_SKAN\_revenue 포스트백</li></ul></li></ol> |
| <span id="id888707086"></span>id888707086 | 인앱 이벤트를 포함한 전환:<ul><li>af\_레벨\_완성</li><li>af\_로그인</li><li>af\_SKAN\_revenue</li><li>af\_등록</li><li>af\_구독</li><li>af\_고객\_이벤트</li></ul> | <ol><li>통합 탭에서 i**n-app 이벤트 포스트백을 활성화합니다**.</li><li>나열된 각 인앱 이벤트를 선택하고 이벤트 식별자에 매핑합니다.</li><li>구성을 저장합니다.</li><li>포스트백에서 전송 전환 가치 = 7.</li><li>앱스플라이어는 다음과 같이 응답합니다:<ul><li>인스톨 포스트백</li><li>af\_레벨\_완성 포스트백</li><li>af\_로그인 포스트백</li><li>af\_SKAN\_revenue 포스트백</li><li>af\_등록 포스트백</li><li>af\_구독 포스트백</li><li>af\_고객\_이밴트 포스트백</li></ul></li></ol> |
| <span id="id888707087"></span>id888707087 | af\_SKAN\_revenue 이벤트를 사용하여 측정한 인게이지먼트 | <ol><li>통합 탭에서 i**n-app 이벤트 포스트백을 활성화합니다**.</li><li>이벤트 이름 af\_SKAN\_revenue*을 매핑하고 이벤트 식별자에 보냅니다.*</li><li>설정 저장</li><li>포스트백에서 전송 전환 가치 = 7.</li><li>앱스플라이어는 다음과 같이 응답합니다:<ul><li>인스톨 포스트백</li><li>af\_SKAN\_revenue 이벤트의 3개 포스트백</li></ul></li></ol> |

<div id="integration-steps" />

#### 통합 단계

| 책임 | 작업 |
| --- | --- |
| 애드 네트워크 |  |
| 애드 네트워크 | <ol><li><Anchor target="_blank" href="/partners/ko/docs/turn-on-test-app-integration-for-ad-networks">테스트 앱을 활성화합니다</Anchor>.</li><li>각 앱에 대해 이전 표의 지침 열을 완료합니다.</li><li>앞의 표에 나열된 테스트 앱을 사용하여 시뮬레이션된 포스트백을 보냅니다. 시뮬레이션된 포스트백을 보낼 때의 고려 사항:<ul><li>app\_id 및 변환 값을 앞의 표에 나열된 대로 설정합니다.</li><li>광고 네트워크는 Apple 호환 서명을 생성할 수 없으므로 시뮬레이션된 포스트백에 서명 필드를 포함할 필요가 없습니다. 앱스플라이어는 시뮬레이션된 포스트백에 대해 이를 확인하지 않습니다.</li><li>광고 네트워크는 포스트 또는 리디렉션 접근 방식을 사용하여 포스트백을 보냅니다.</li></ul></li></ol> |
| 앱스플라이어 | 통합 중에 광고 네트워크에서 지정한 엔드포인트에 대한 디코딩된 포스트백으로 응답합니다. |

<div id="test-criteria-1" />

#### 테스트 기준

| 책임 | 작업 |
| --- | --- |
| 앱스플라이어 | 포스트백을 처리하고 광고 네트워크에 포스트백을 보냅니다. |
| 애드 네트워크 | <ul><li>광고 네트워크는 번역된 포스트백을 수신하고 디코딩합니다.</li><li>앱스플라이어에서 보낸 인앱 포스트백은 예상 흐름과 일치합니다. 예를 들어 앱 ID888707087의 전환 값이 3인 경우 광고 네트워크는*af\_SKAN\_revenue* 이벤트의 포스트백을 3회 수신합니다.</li></ul> |

</Accordion>

<div id="clarifications" />

## 규명

필수 필드, 강화, 인증 등과 관련된 설명.

<div id="faq" />

<Accordion title="자주 묻는 질문">

| 포스트백에 대한 질문과 대답 |
| --- |
| **보강 필드는 필수인가요?**<br /><br />현재로서는 다음 보강 매개 변수 중 하나 이상이 누락된 경우에도 포스트백을 처리합니다. 다음과 같은 이유로 정보가 필요합니다.<ul><li>애드 네트워크 캠페인 ID</li><li>애드 네트워크 캠페인 이름</li><li>IP 주소</li><li>타임스탬프 타임스탬프: 설치를 올바른 날짜로 표시하는 데 도움이 됩니다.</li></ul> |
| 캠페인 ID 또는 캠페인 이름 중 하나만 보낼 수 있습니까?<br /><br />이전 답변을 참조하십시오. ID와 이름을 모두 동일한 값으로 채우는 것이 좋습니다. |
| 예, 가능합니다. 당사는 포스트백을 처리하고 저작자 표시 서명이 유효한 경우 추가 정보를 무시합니다. |
| SKAN 포스트백 템플릿은 기존 포스트백 템플릿과 다릅니까?<br /><br />네. 흐름과 구조가 다릅니다. |
| 동일한 인스톨과 관련된 SKAN 포스트백 및 확률적/결정론적 모델링 포스트백을 받게 되면 이는 동일한 인스톨에 대한 중복 리포트를 의미합니까?<br /><br />예. 각각의 경우에 대해 방법에 관계없이 귀하에게 귀속된 설치를 기록하고 포스트백을 보내드립니다.<br /><br />attribution\_source를 사용하여 SKAN 포스트백을 구분합니다. |
| **앱스플라이어의 포스트백을 처리해야 하나요?**<br /><br />아니요. 모범 사례는 포스트백을 통해 보고된 사용자 품질에 따라 캠페인을 최적화하는 것입니다. |
| **앱스플라이어 어트리뷰션 링크를 호출해야 합니까, 아니면 SKAN 페이로드 및 보강된 데이터와 함께 포스트백을 전송하는 것으로 충분합니까?**<br /><br />SKAN 페이로드와 보강된 데이터를 보내는 것으로 충분합니다. |
| **앱스플라이어 대시보드에서 SKAN 연동 파트너로 인증을 받기 위해 필요한 것은 무엇입니까?**<ul><li>이 문서에 나열된 방법 중 하나를 사용하여 완전한 통합</li><li>앱스플라이어를 어트리뷰션 파트너로 사용하는 앱의 포스트백 보내기</li></ul> |
| **100개의 SKAN 캠페인 ID 제한은 어떤 영향을 미칩니까**?<br /><br />1-100까지 제한은 Apple에서 캠페인에 서명하고 번호를 매기는 방법과 관련됩니다. 즉, 언제든지 100개의 동시 고유 캠페인을 가질 수 있습니다. 실제 캠페인 이름과 ID로 포스트백을 보강할 수 있습니다. 즉, SKAN 캠페인 ID를 포스트백이 수신되는 시점에 사용 중인 실제 캠페인 ID에 매핑합니다. 이렇게 하는 것은 물론 특정 앱에 대해 동시에 100개 이상의 캠페인을 수행하지 않는 한 앱플라이어에서 측정하는 캠페인의 수를 제한하지 않는다는 것을 의미합니다. |

</Accordion>

<div data-zendesk-anchors="appsflyer-offering-for-ad-networks=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4-%EC%98%A4%ED%8D%BC%EB%A7%81 h_01HDG8991Y6EWWN9KYBR9FEAJZ=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4-%EC%98%A4%ED%8D%BC%EB%A7%81 skan-data-flow=skan-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%9D%90%EB%A6%84 h_01HDG8991Y5DW0BVD674RS88F2=skan-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%9D%90%EB%A6%84 main-integration-parts=%EA%B8%B0%EB%B3%B8-%EC%97%B0%EB%8F%99-%EB%B6%80%EB%B6%84 h_01HDG8991YDTY85NK7TQ26B2Z1=%EA%B8%B0%EB%B3%B8-%EC%97%B0%EB%8F%99-%EB%B6%80%EB%B6%84 send-data-to-appsflyer=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%86%A1 h_01HDG8991YTFP2HE0Y8P8X0C20=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%86%A1 h_01HDG8991YRW3TWSDARFM58FA8=enrich-and-forward skan-enriched-postback-protocol=skan-%EA%B0%95%ED%99%94-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C h_01HDG8991YAKZMSA4MAY0YTFPB=skan-%EA%B0%95%ED%99%94-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C skan-enriched-postback-json-parameters=skan-%EB%B3%B4%EA%B0%95-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-json-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 h_01HDG8991YS91CWESZH0M7CA00=skan-%EB%B3%B4%EA%B0%95-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-json-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 curl-example%E2%80%94enriched-skan-3-postback=curl-%EC%98%88%EC%A0%9C---%EA%B0%95%ED%99%94%EB%90%9C-skan-3-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HDG8991YFHBQDRG4K0XA3JQ8=curl-%EC%98%88%EC%A0%9C---%EA%B0%95%ED%99%94%EB%90%9C-skan-3-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 curl-example%E2%80%94enriched-skan-4-postback-with-fine-conversion-values=curl-%EC%98%88%EC%A0%9C---%EB%AF%B8%EC%84%B8-%EB%B3%80%ED%99%98-%EA%B0%92%EC%9C%BC%EB%A1%9C-%EA%B0%95%ED%99%94%EB%90%9C-skan-4-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HDG8991YNVCK92TVNJHGKNG5=curl-%EC%98%88%EC%A0%9C---%EB%AF%B8%EC%84%B8-%EB%B3%80%ED%99%98-%EA%B0%92%EC%9C%BC%EB%A1%9C-%EA%B0%95%ED%99%94%EB%90%9C-skan-4-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 curl-example%E2%80%94enriched-skan-4-postback-with-coarse-conversion-values=curl-%EC%98%88%EC%A0%9C---%EC%BD%94%EC%8A%A4-%EB%B3%80%ED%99%98-%EA%B0%92%EC%9C%BC%EB%A1%9C-%EA%B0%95%ED%99%94%EB%90%9C-skan-4-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HDG8991YXTS27V0NJ4ZXQ53T=curl-%EC%98%88%EC%A0%9C---%EC%BD%94%EC%8A%A4-%EB%B3%80%ED%99%98-%EA%B0%92%EC%9C%BC%EB%A1%9C-%EA%B0%95%ED%99%94%EB%90%9C-skan-4-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HDG8991YGHWJ9R1ZKTCFJZCA=redirect implementation=%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0 h_01HDG8991YBR7VWRH9079GT695=%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0 query-params-for-campaign-details-not-mandatory=%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%84%B8%EB%B6%80-%EC%A0%95%EB%B3%B4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%BF%BC%EB%A6%AC-%EB%A7%A4%EA%B0%9C-%EB%B3%80%EC%88%98%ED%95%84%EC%88%98-%EC%95%84%EB%8B%98 h_01HDG8991YQB77MMF906PCAWC2=%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%84%B8%EB%B6%80-%EC%A0%95%EB%B3%B4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%BF%BC%EB%A6%AC-%EB%A7%A4%EA%B0%9C-%EB%B3%80%EC%88%98%ED%95%84%EC%88%98-%EC%95%84%EB%8B%98 receive-data-from-appsflyer=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EC%97%90%EC%84%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%8B%A0 h_01HDG8991ZNF2PKKJN3FPN6QXA=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EC%97%90%EC%84%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%8B%A0 h_01HDG8991ZKR35WHWVX0DHC612=principles h_01HDG8991ZG9GMMY57XYZF1Q3S=postback-macros-available-to-ad-network-partners h_01HDG8991ZD6ARRK6Z83NQBGRR=skan-postback-examples integration-testing=%EC%97%B0%EB%8F%99-%ED%85%8C%EC%8A%A4%ED%8A%B8 h_01HDG8991ZS10MJJ3ZN31YDPTK=%EC%97%B0%EB%8F%99-%ED%85%8C%EC%8A%A4%ED%8A%B8 h_01HDG8991ZPR41S5T9HZ9N1ZWF=real-environment testing-integration=%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%86%B5%ED%95%A9 h_01HDG8991ZJ1KTHX6FE9R0QJNP=%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%86%B5%ED%95%A9 test-criteria=%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%A4%80 h_01HDG8991ZP59K8RQQ7G1GGMPG=%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%A4%80 h_01HDG8991Z7DX65Y3E6RPHB2M3=simulated-postbacks integration-steps=%ED%86%B5%ED%95%A9-%EB%8B%A8%EA%B3%84 h_01HDG8991ZZPYH7H329EY8TNV9=%ED%86%B5%ED%95%A9-%EB%8B%A8%EA%B3%84 test-criteria::26c15d59=%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%A4%80-1 h_01HDG8991ZR4F21KVYF0MQ9GZA=%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%A4%80-1 clarifications=%EA%B7%9C%EB%AA%85 h_01HDG8991Z8C0K0SMBT9VSX12Y=%EA%B7%9C%EB%AA%85 h_01HDG8991ZDAGFV8GGC1RH73KQ=faq" />
