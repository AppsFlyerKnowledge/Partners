---
title: UA 애드 네트워크용 광고 수익 신호
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-michael-talapov
    - ROI360
    - Ad Networks
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2026-10-14T10:31:22Z'
  id: 4402898251409
  locale: ko
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ko/articles/4402898251409
---
> **요약:** 유저 유입을 담당하는 애드 네트워크는 광고 수익 관련 데이터를 수신하여 고객의 UA 캠페인을 최적화하는 데 사용할 수 있습니다.

애드 네트워크는 데이터 락커를 통해 유저에 관한 중요한 광고 수익 정보가 담긴 리포트를 받을 수 있습니다. 이러한 유저는 애드 네트워크를 통해 제공되는 캠페인에서 유입된 유저일 수도 있고, 다른 미디어소스에서 유입된 유저일 수도 있습니다.

다음으로 애드 네트워크는 이 데이터를 캠페인 타겟팅 및 최적화 알고리즘에 수집하고, UA에서 생성된 수익에 대한 전체 보기를 기반으로 ROAS 캠페인을 개선하는 데 사용할 수 있습니다.

<div id="set-the-ad-revenue-report-in-data-locker" />

## 데이터 락커에서 광고 수익 리포트 설정

데이터 락커에서 광고 수익 리포트에 액세스하려면 다음 활동을 완료해야 합니다.

* 애드 네트워크는 <Anchor target="_blank" href="/partners/ko/docs/data-locker-for-partners#set-up-data-locker">파트너용 데이터 락커에 온보딩</Anchor>해야 합니다.
* 애드 네트워크는 [리포트 출력 설정을 구성](#configure-the-report-output-settings)하고 [광고 수익 리포트를 활성화](#enable-the-ad-revenue-report)해야 합니다.
* 광고주는 애드 네트워크에서 리포트를 볼 수 있도록 허용해야 합니다. <Anchor target="_blank" href="/marketers/ko/docs/share-ad-revenue-data-with-partners#ua-signals-for-ad-networks">광고주 지침 참조</Anchor>

<div id="configure-the-report-output-settings" />

<Accordion title="리포트 출력 설정 구성">

리포트 출력 설정을 구성하려면 아래 단계를 따르세요.

1. **앱스플라이어에서** **리포트** > 데이터 락커로 이동합니다.
2. **리포트 출력 설정** 영역에서 **리포트 보내기**를 켭니다.
3. 리포트 파일 출력 속성을 설정합니다.
   * 리포트 형식(Parqet/CSV).
   * 리포트 압축 방식(Snappy/GZIPO/비압축).
   * 파일의 최대 행 수.
4. 리포트 파일 출력의 예상 경로를 검토합니다. 경로는 연결 설정에 따라 설정됩니다. 연결 설정 방법을 알아보려면 <Anchor target="_blank" href="/partners/ko/docs/data-locker-for-partners#set-up-data-locker">데이터 락커 설정</Anchor>을 참조하세요.

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="광고 수익 리포트 활성화">

1. **데이터 락커 콘텐츠** 섹션에서 **광고 수익[일일]** 리포트 유형**을 선택합니다.**
2. **연결 저장**을 클릭합니다.
3. 광고주가 애드 네트워크에서 리포트를 볼 수 있도록 허용했는지 확인합니다.
4. 지침은 <Anchor target="_blank" href="/marketers/ko/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">애드 네트워크가 광고 수익 데이터를 가져올 수 있도록 허용</Anchor>을 참조하세요.

</Accordion>

<div id="report-specification" />

## 리포트 사양

<div id="report-considerations" />

<Accordion title="리포트 구조 및 형식">

* 형식: 데이터는 CSV 형식으로 UA 파트너의 S3 버킷에 도착합니다.
* 수준 기기 단위 차원 및 메트릭을 포함합니다.
* 데이터 강화 중재 파트너의 광고 수익 데이터를 포함하며, UA 애드 네트워크와 관련된 어트리뷰션 데이터(UA 애드 네트워크와 관련이 없는 모든 차원이 정리된 데이터)를 추가합니다.
* 데이터 최신성: <Anchor target="_blank" href="/marketers/ko/docs/about-data-freshness-and-timezone-support#ad-revenue">매일, 즉 0일 차 데이터는 1일 차에 도착합니다</Anchor>. 데이터는 매일 21:00(<Anchor target="_blank" href="/marketers/ko/docs/about-data-freshness-and-timezone-support#daily">UTC 시간</Anchor>)에 데이터 락커 버킷의 h=23에 기록됩니다.
* 앱 포함 내역: 단일 리포트에 광고주가 권한을 부여한 모든 앱의 데이터가 포함됩니다.
* 통화: USD 기준. 이벤트 수익은 이벤트가 발생한 날의 USD로 계산됩니다.
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv">샘플 리포트 보기</Anchor>

</Accordion>

<div id="report-structure" />

<Accordion title="리포트 필드">

| **필드** | **비고** |
| --- | --- |
| 버전 | 두 번째 Unix 타임스탬프입니다. 예시: 1661315124 |
| app\_id | 앱스플라이어 플랫폼의 앱 ID |
| 설치 시간 | <ul><li>인스톨 타임스탬프: YYYY-MM-DD HH:MM:SS<br />예시: 24,033.07</li><li>iOS 14 이상 기기 및 비동의 유저의 경우, 또는 광고주가 고급 개인정보 보호를 설정한 경우, 인스톨 시간은 가장 가까운 시간으로 반올림됩니다.</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | UA가 데이터를 수신하는 파트너에 기인하는 경우에만 채워집니다. |
| idfa, idfv, advertising\_id | <ul><li>광고 수익 창출 이벤트가 두 개 이상인 경우 IDFA, IDFV 또는 advertiser\_id와 같은 동일한 기기 ID가 여러 행에 표시될 수 있습니다.</li><li>iOS 14 이상 기기 및 동의하지 않은 유저의 경우 또는 광고주가 고급 개인 정보 보호를 켠 경우 표시되지 않습니다.</li></ul> |
| 플랫폼 | 기기 플랫폼: iOS, 안드로이드, 또는 Windows Mobile |
| country | ISO 3166(alpha-2)을 사용한 국가 코드. 예: 미국, 중국 |
| original\_url | <ul><li>iOS 14 이상 기기 및 동의하지 않은 유저의 경우 또는 광고주가 고급 개인 정보 보호를 켠 경우 표시되지 않습니다.</li><li>UA가 데이터를 수신하는 파트너에 기인하는 경우에만 채워집니다.</li></ul> |
| ad\_unit |  |
| placement |  |
| mediation\_network |  |
| engagement\_type |  |

지표:

| **필드** | **비고** |
| --- | --- |
| 노출 | 유저가 광고를 본 횟수 |
| revenue\_usd | 디바이스 ID에 대해 발생한 일일 수익(USD)입니다. **참고**: 수익 금액이 작을 경우 과학적 표기로 표시됩니다. 예를 들어: 8.00E-05 |

</Accordion>

<div data-zendesk-anchors="set-the-ad-revenue-report-in-data-locker=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4%EC%97%90%EC%84%9C-%EA%B4%91%EA%B3%A0-%EC%88%98%EC%9D%B5-%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%84%A4%EC%A0%95 h_01H8Y7ABGVR7BNHEYVFKPFM4JN=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4%EC%97%90%EC%84%9C-%EA%B4%91%EA%B3%A0-%EC%88%98%EC%9D%B5-%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%84%A4%EC%A0%95 h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report report-specification=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%82%AC%EC%96%91 h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%82%AC%EC%96%91 h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
