---
title: UA 파트너를 위한 ROI360
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2023-08-12T17:09:08Z'
  edited_at: '2026-10-14T10:36:00Z'
  id: 17735150011921
  locale: ko
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ko/articles/17735150011921
---
> **한눈에 보기:** 앱스플라이어는 리포트 및 포스트백을 통해 UA 파트너에게 완전하고 정확한 광고, 인앱 구매, 자동 갱신 구독 데이터를 제공합니다. 파트너는 정보를 수집하여 UA 캠페인을 최적화할 수 있습니다.

<div id="introduction" />

## 소개

  앱스플라이어는 UA 파트너에게 정보를 전송할 수 있습니다.

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="파트너에게 리포트되는 수익 유형은 무엇인가요?">

앱은 두 가지 수익 유형을 창출합니다.

* **광고 수익: 광고 수익: 광고 수익은 배너, 전면 광고 및 기타 형식과 같은 앱 내에 광고가 표시될 때마다 생성됩니다. 광고주에게 청구되는 캠페인 방법에 관계없이 계산할 수 있습니다.**

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="앱스플라이어는 UA 파트너에게 수익 신호를 어떻게 제공하나요?">

앱스플라이어는 다음과 같은 수단을 통해 파트너에게 인앱 광고, 인앱 구매 및 구독 수익에 대한 정보를 제공합니다.

* 이 리포트는 데이터 락커에서 매일 사용할 수 있으며 전날의 데이터를 포함합니다.
* 광고 수익 포스트백 **광고 수익 포스트백: 클라이언트 디바이스에서 광고 노출이 발생할 때마다 앱스플라이어에서 파트너에게 광고 수익 이벤트의 세부 정보가 포함된 포스트백이 전송됩니다.**
* 스토어 매출 포스트백: 구매 또는 구독 이벤트가 발생할 때마다 앱스플라이어에서 수익 이벤트의 세부 정보가 포함된 포스트백이 파트너에게 전송됩니다.

</Accordion>

<div id="set-up-roi360-for-partners" />

## 파트너를 위한 ROI360 설정

UA 신호 리포트와 광고 수익 및 매장 수익 포스트백을 수신하기 위해 파트너가 취해야 할 조치는 무엇인가요?

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="ROI360 UA 신호 리포트를 구독하는 방법">

파트너가 데이터 락커를 통해 리포트를 받을 수 있도록 하려면 다음을 수행합니다.

* 파트너는 데이터 락커에서 다음 단계를 수행해야 합니다.
  1. 클라우드 서비스 공급자에 대한 연결, 리포트의 형식 및 내용을 포함하여 파트너 계정에서 <Anchor target="_blank" href="/partners/ko/docs/data-locker-for-partners#set-up-data-locker">데이터 락커를 설정합니다</Anchor>.
  2. <Anchor target="_blank" href="/partners/ko/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">ROI360 UA 신호 리포트를 활성화합니다</Anchor>.
* 광고주는 <Anchor target="_blank" href="/marketers/ko/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">파트너에게 리포트에 대한 권한을 부여해야 합니다</Anchor>.

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="앱스플라이어에서 ROI360 포스트백을 수신하는 방법">

앱스플라이어로부터 포스트백을 받으려면 파트너는 앱스플라이어의 파트너 연동 팀과 대화를 시작해야 합니다. 그 후, 팀은 앱스플라이어 플랫폼 내에서 ROI 인앱 수익 포스트백 값을 구성합니다.

앱스플라이어 파트너 지원팀에 문의하려면 대시보드에서 **도움말** 메뉴를 열고 **팀에 문의**를 선택하십시오.

alt

</Accordion>

<div id="roi360-ua-signals-report-for-ua-networks" />

## UA 네트워크를 위한 ROI360 UA 신호 리포트

이 리포트는 매일 UA 파트너의 S3 버킷에 완전하고 정확한 x+1 CSV/parquet 수익 레코드를 제공합니다. 각 레코드는 디바이스 수준에서 광고 수익 이벤트를 집계한 것입니다.

UA 신호 리포트는 광고 수익 포스트백처럼 실시간 데이터를 제공하지 않습니다. 그러나 더 정확하고 완전합니다. 노출의 가치는 시간이 지남에 따라 변할 수 있기 때문입니다. 노출 수준 수익 데이터가 실시간 입찰이 아닌 표준 CPM 입찰을 통해 판매된 광고 노출에 대한 경우 특히 그렇습니다.

<div id="what-are-the-report-data-sources" />

<Accordion title="리포트 데이터 소스란 무엇입니까?">

광고주 통합 유형에 따라 리포트 데이터는 다음 중 하나에서 발생할 수 있습니다.

1. <Anchor target="_blank" href="/marketers/ko/docs/integrate-the-roi360-ad-revenue-sdk-api">AdRevenue SDK 커넥터</Anchor> 통합: 고객은 파트너가 로드한 노출 수준 수익 데이터를 클라이언트 디바이스에 공유한 다음 거의 실시간으로 앱스플라이어에 보고할 수 있습니다.
2. S2S API 기반 디바이스 레벨 통합: 고객은 연동 파트너의 앱스플라이어 UI 내에서 파트너 자격 증명을 구성하고 ROI360 광고 수익이 자신을 대신하여 디바이스 레벨 광고 수익 데이터를 수집하도록 허용할 수 있습니다.
3. 이 둘의 조합(정확성 최신성). **참고:** 참고: 광고주에서 앱스플라이어로의 데이터 전송은 광고주 권한과 광고주가 ROI360 고급 어드밴스드 고객인지 여부에 따라 달라집니다.

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="리포트 데이터에 대해 어떤 데이터 처리가 수행됩니까?">

앱스플라이어 ROI360 광고 수익은 다음을 수행합니다.

1. 데이터 정규화
2. 설치 미디어소스 및 데이터 보강에 대한 어트리뷰션특성
3. 광고 수익 이벤트 생성
4. 이벤트는 디바이스 단위로 집계됩니다

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="리포트 데이터는 어떻게 전달됩니까?">

디바이스 단위 데이터는 데이터 락커의 리포트에 매일 기록됩니다

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="리포트 데이터 최신도란 무엇입니까?">

데이터는 매일 21:00 <Anchor target="_blank" href="/marketers/ko/docs/about-data-freshness-and-timezone-support#daily">(UTC 시간)</Anchor>에 데이터 락커 버킷의 h=23 폴더에 기록됩니다.

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="리포트 필드에는 어떤 것이 있나요?">

| **필드** | **비고** |
| --- | --- |
| 버전 | 두 번째 Unix 타임스탬프입니다. 예시: 1661315124 |
| app\_id | 앱스플라이어 플랫폼의 앱 ID |
| 설치 시간 | 인스톨 타임스탬프: iOS 14 이상 기기 및 비동의 유저의 경우, 또는 광고주가 고급 개인정보 보호를 설정한 경우, 인스톨 시간은 가장 가까운 시간으로 반올림됩니다. |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | UA가 데이터를 수신하는 파트너에 기인하는 경우에만 채워집니다. |
| idfa, idfv, advertising\_id | • 광고 수익 창출 이벤트가 두 개 이상인 경우 IDFA, IDFV 또는 advertiser\_id와 같은 동일한 기기 ID가 여러 행에 표시될 수 있습니다. • iOS 14+ 디바이스 및 동의하지 않은 사용자의 경우 또는 광고주가 고급 개인 정보 보호를 켠 경우 표시되지 않습니다. |
| 플랫폼 | 기기 플랫폼: iOS, 안드로이드, 또는 Windows Mobile |
| country | ISO 3166(alpha-2)을 사용한 국가 코드. 예: 미국, 중국 |
| original\_url | • iOS 14+ 디바이스 및 동의하지 않은 사용자의 경우 또는 광고주가 고급 개인 정보 보호를 켠 경우 표시되지 않습니다.• UA가 데이터를 수신하는 파트너에 기인하는 경우에만 채워집니다. |
| mediation\_network | 2023년 3분기 출시 예정: 노출과 관련된 미디에이션 네트워크 |
| ad\_unit | 2023년 3분기 출시 예정: 노출과 관련된 수익 창출 ad\_unit |
| placement | 2023년 3분기 출시 예정: 노출과 관련된 수익 창출 배치 |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="리포트 데이터 샘플 다운로드">

[리포트를 다운로드하려면 클릭하십시오.](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

<div id="in-app-ad-revenue-iaa-postbacks" />

## 인앱 광고 수익(IAA) 포스트백

IAA 포스트백은 앱스플라이어가 파트너에게 수익 정보를 전송하기 위해 사용하는 두 번째 수집 접근 방식입니다. 광고 수익 UA 신호 리포트에 비해 가장 큰 장점은 신선도인데, 포스트백이 거의 실시간으로 IAA 수익 데이터 공유를 제공하기 때문입니다. 이는 광고 수익 UA 신호 리포트를 통해 제공되는 X+1 최신도(이벤트 발생일 1일 후)와 대조됩니다.

그러나 실시간 새로 고침은 X+1에 비해 정확도가 떨어집니다.

* 실시간 IAA 포스트백 데이터는 UA 신호 리포트 X+1 데이터보다 평균 ±5% 덜 정확합니다.
* 실시간 IAA 포스트백 데이터는 UA 신호 리포트 X+1 데이터보다 평균적으로 ±7% 덜 완전합니다.

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="IAA 포스트백 데이터 소스는 무엇입니까?">

커넥터를 사용하면 앱 개발자가 ILRD, 통화, 미디에이션 플랫폼 및 수익 창출 소스와 같은 특정 매개변수를 포함하는 노출 이벤트를 보고할 수 있습니다.

광고주 클라이언트 디바이스에서 앱스플라이어로의 데이터 전송은 광고주 권한과 광고주가 ROI360 고급 고객인지 여부에 따라 달라집니다.

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="IAA 포스트백 데이터에 대해 어떤 처리가 수행됩니까?">

앱스플라이어 ROI360은 수신된 각 노출 수준 데이터에 대해 다음 단계를 수행합니다.

1. 데이터 정규화.
2. 설치 미디어소스 및 데이터 보강에 대한 어트리뷰션특성.
3. **af\_ad\_revenue** 이벤트 생성.

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="포스트백 데이터는 어떻게 전달됩니까?">

이벤트는 파트너와 앱스플라이어 간의 기존 포스트백 구성을 통해 추가 파라미터로 파트너에게 전송됩니다.

</Accordion>

<div id="in-app-purchase-iap-postbacks" />

## 앱에서 바로 구매(IAP) 포스트백

ROI360 인앱 구매 포스트백은 먼저 각 트랜잭션의 유효성을 검사하고 중복 제거한 다음 매장 수수료 및 판매세를 공제하여 여러 계층의 보고 정확도를 제공합니다.

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="IAP 포스트백 데이터 소스란 무엇인가요?">

IAP 포스트백에 대한 데이터의 출처는 다음과 같습니다.

1. 디바이스에서 앱에서 바로 구매 또는 자동 갱신 구독 이벤트가 발생할 때마다 ROI360 구매 SDK 커넥터에서 읽은 트랜잭션 수준 데이터입니다.
2. 수신되는 **모든 App Store 및 Google Play(RTDN) 서버 알림**은 앱스플라이어 구매 및 구독 수익 비즈니스 로직에 의해 처리됩니다.

   * SDK 커넥터를 통해 이전에 보고된 트랜잭션에 대한 알림은 유효성이 검사되고 처리됩니다.
   * 알 수 없는 거래에 대한 알림은 앱스플라이어에 보고되지 않습니다

   **참고:** 참고: 광고주에서 앱스플라이어로의 데이터 전송은 광고주 권한과 광고주가 ROI360 고급 어드밴스드 고객인지 여부에 따라 달라집니다.

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="IAP 포스트백 데이터에서 수행되는 데이터 처리는 무엇입니까?">

앱스플라이어 ROI360은 수신된 각 트랜잭션 수준 데이터에 대해 다음 단계를 수행합니다.

1. 앱스플라이어**는 관련 스토어의 구매 또는 구독을 검증**하여 사기가 아닌지 확인합니다.
   * 유효성 검사에 성공하면 앱스플라이어는 구매 또는 구독을 기록합니다.
   * 영수증 검증에 실패하면 차단된 인앱 이벤트 로데이터 리포트(Protect360 가입자가 사용할 수 있음)에 이벤트가 표시됩니다.
2. 앱스플라이어는 iOS에서 가족 공유와 관련된 거래를 포함하여 거래가 중복되지 않도록 합니다.
3. 앱스플라이어는 매장 수수료 및 세금(실제 수익)을 고려하여 순**수익** 데이터를 계산합니다.
4. 앱스플라이어는 검증 및 처리된 트랜잭션에 대한 내부 구매 또는 수명 주기 이벤트를 생성합니다.

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="포스트백은 어떻게 전달됩니까?">

IAP 이벤트는 파트너와 앱스플라이어 간의 기존 포스트백 연동을 통해 파트너에게 전송됩니다.

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="IAP 이벤트란 무엇인가요?">

ROI360 고객은 다음과 같은 수익 발생 이벤트 이름을 공유할 수 있습니다.

**이벤트 이름**

| **이벤트 이름** | **설명** |
| --- | --- |
| af\_구매 | 사용자가 구매할 때 기록됩니다. |
| af\_purchase\_refund | 구매가 환불될 때 기록됩니다. |
| af\_ars\_trial\_converted | 평가판 기간 후 전체 가격 갱신이 시작될 때 기록됩니다. |
| af\_ars\_subscription\_started | 할인된 구독 또는 정액이 책정된 구독이 시작될 때 기록됩니다. |
| af\_ars\_subscription\_resumed | 이탈 또는 환불된 구독 후 전체 가격의 구독이 다시 시작될 때 기록됩니다. |
| af\_ars\_subscription\_refunded | 구독자가 환불을 받을 때 기록됩니다. |
| af\_ars\_subscription\_renewed | 자동 갱신 구독이 발생할 때 기록됩니다. |
| af\_ars\_subscription\_xgraded | 구독자가 다른 제품으로 업그레이드, 다운그레이드 또는 교차 등급을 지정할 때 기록됩니다. |

</Accordion>

<div data-zendesk-anchors="introduction=%EC%86%8C%EA%B0%9C 01H7T1DS6SNC7X8GX4DGXT4GC0=%EC%86%8C%EA%B0%9C 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=%ED%8C%8C%ED%8A%B8%EB%84%88%EB%A5%BC-%EC%9C%84%ED%95%9C-roi360-%EC%84%A4%EC%A0%95 01H7T1DS6TDA8CX1ZF3GGE4EHB=%ED%8C%8C%ED%8A%B8%EB%84%88%EB%A5%BC-%EC%9C%84%ED%95%9C-roi360-%EC%84%A4%EC%A0%95 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=ua-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-roi360-ua-%EC%8B%A0%ED%98%B8-%EB%A6%AC%ED%8F%AC%ED%8A%B8 01H7T1DS6T93844DMZY744ECQE=ua-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-roi360-ua-%EC%8B%A0%ED%98%B8-%EB%A6%AC%ED%8F%AC%ED%8A%B8 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=%EC%9D%B8%EC%95%B1-%EA%B4%91%EA%B3%A0-%EC%88%98%EC%9D%B5iaa-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01H7T1DS6T0CN30EC97VARN80D=%EC%9D%B8%EC%95%B1-%EA%B4%91%EA%B3%A0-%EC%88%98%EC%9D%B5iaa-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=%EC%95%B1%EC%97%90%EC%84%9C-%EB%B0%94%EB%A1%9C-%EA%B5%AC%EB%A7%A4iap-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01H7T1DS6TH8AV2ZTY3M8ZXPYA=%EC%95%B1%EC%97%90%EC%84%9C-%EB%B0%94%EB%A1%9C-%EA%B5%AC%EB%A7%A4iap-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
