---
title: 광고 네트워크를 위한 CTV-모바일 앱 뷰-쓰루(view-through) 어트리뷰션
metadata:
  keywords:
    - Attribution
    - Ad Networks
    - Partners
    - CTV
    - CTV Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roi-tamir
    - CTV Attribution
    - Ad Networks
  created_at: '2022-08-21T06:49:24Z'
  edited_at: '2026-10-14T10:34:15Z'
  id: 8528418936977
  locale: ko
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ko/articles/8528418936977
---
> **한눈에 보기:** CTV 디바이스에서 시청한 광고에 대한 모바일 앱 인스톨을 측정합니다.

## 광고 네트워크를 위한 CTV-모바일 앱 어트리뷰션

앱스플라이어 크로스 플랫폼 노출 URL을 사용하면 모바일 앱 인스톨을 CTV에 표시된 광고에 귀속시킬 수 있습니다. 한 가구 내에서 여러 번의 인스톨이 동일한 CTV 광고 노출에 의해 측정될 수 있습니다.

![50310_CTV_흐름_차트__2_.jpg](https://files.readme.io/401bcb083e1cc618794cb302668f7271cf825a5a6045ff10055e0164baf423a1-19774176963473.jpg)

CTV-모바일 앱 뷰-쓰루 어트리뷰션은 광고주가 만든 크로스 플랫폼 원링크 템플릿(템플릿 ID 포함)을 기반으로 한 <Anchor target="_blank" href="/marketers/ko/docs/set-up-cross-platform-links-for-multi-device-campaigns#setup">원링크 노출 URL</Anchor>을 사용합니다. 이를 통해 광고주는 단일 URL을 사용하여 다양한 플랫폼(예: 안드로이드 및 iOS 앱)의 여러 앱을 그룹화할 수 있습니다.

사용자가 CTV에서 광고를 볼 때 앱스플라이어에 실시간으로 노출 URL을 보냅니다.

예시 URL:

```http
https://impressions.onelink.me/{template_id}?pid=__media_source__&af_xplatform=true&af_xplatform_vt_lookback=24h&af_siteid=__CSITE__&c=__CAMPAIGN_NAME__&af_channel=__PLACEMENT__&af_c_id=__CAMPAIGN_ID__&af_adset=__AID_NAME__&af_adset_id=__AID__&af_ad=__CID_NAME__&af_ad_id=__CID__&af_source_platform=__source_platform__&af_source_device_category=__device_category__&af_ad_type=__CTYPE__&af_ip=__IP__&af_ua=__UA__&redirect=false
```

전환 발생 후 포스트백이 발송됩니다.

> 📘 **참고**
>
> 이 기능은 지정된 파트너만 사용할 수 있습니다. 궁금하신 경우, 파트너 개발 매니저(PDM)에 문의하세요.

<div id="setup" />

<Accordion title="설정">

**광고주와 함께 CTV-모바일 앱 뷰-쓰루(view-through) 어트리뷰션을 설정하려면**:

1. 귀하가 <Anchor target="_blank" href="/partners/ko/docs/getting-started-onboarding-guide-for-ad-networks">앱스플라이어의 연동 파트너</Anchor>이고, 포스트백이 올바르게 설정되었으며, 앱스플라이어와 [CTV-모바일 앱 연동 테스트](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#test-partner-integration)를 마쳤는지 확인하십시오.
2. URL에 [필수 파라미터](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#parameters)와 그 밖에 원하는 기타 파라미터를 포함하는지 확인하십시오.
3. 앱스플라이어로 사용자 IP 주소와 사용자 에이전트를 전송하세요. 이러한 정보는 CTV-모바일 앱 뷰-쓰루(view-through) 어트리뷰션에 필요합니다. 다음 중 하나의 방법으로 전송할 수 있습니다:
   1. 노출 URL의 `af_ip` 및 `af_ua` 파라미터
   2. As  and  요청 헤더의 파라미터

</Accordion>

<div id="test-partner-integration" />

<Accordion title="파트너 연동 시험">

**CTV-모바일 앱 뷰-쓰루(view-through) 어트리뷰션을 시험하려면**:

1. 다음 테스트 앱을 사용하십시오. com.appsflyer.android.deviceid and id1192323960
2. 시험 URL을 받으려면 앱스플라이어 파트너 솔루션 팀에 문의하세요. 이 작업을 위해 [파트너 대시보드](https://hq1.appsflyer.com/auth/login)에 로그인한 후 상단 메뉴에서 **도움말** > **문의**를 클릭하세요.
   * 샘플 URL: `https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false` `https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false`
3. 파트너 ID가 맞는지 `pid` 파라미터에서 확인하세요.
4. 파라미터`af_ip`에 IP 주소를 입력하세요.
5. 파라미터`af_ua`에 유저 에이전트를 입력하세요.
6. URL을 데스크톱 브라우저에 입력하세요.
7. 모바일 디바이스에서 애플 앱 스토어로 이동하여 앱을 다운로드, 인스톨하고 실행하세요.
8. 새로운 인스톨이 앱스플라이어에 표시되고 해당 포스트백을 받게 됩니다. 인스톨이 보이지 않거나 포스트백을 받지 못하는 경우 파트너 솔루션 팀에 문의하세요.

</Accordion>

<div id="parameters" />

<Accordion title="파라미터">

다음 파라미터는 광고주에게 어트리뷰션 데이터와 측정을 제공하는 데 사용됩니다.

| 파라미터 | 필수 | 설명 |
| --- | --- | --- |
| 템플릿 ID | ✓ | <Anchor target="_blank" href="/marketers/ko/docs/create-a-onelink-template">원링크 템플릿</Anchor> ID 이 템플릿은 광고주 앱을 위한 기본 예측 설정을 포함하며, 다른 링크 생성의 기반이 됩니다. |
| pid | ✓ | 광고를 게재하는 미디어 소스(애드 네트워크)에 앱스플라이어가 할당한 파트너 식별자입니다. |
| af\_xplatform | ✓ | <ul><li>광고주가 설정하여 링크가 플랫폼 간 어트리뷰션을 지원하는지 여부를 나타냅니다.</li><li>값: 참/거짓</li></ul> |
| af\_xplatform\_vt\_lookback | - | 노출 후 앱 인스톨이 해당 노출에 기인한 것으로 간주될 수 있는 시간을 설정하는 창입니다. 사용 가능한 파라미터 값: 1시간 - 72시간. 기본값은 24시간입니다. |
| af\_ip | ✓ | <ul><li>광고를 표시하는 CTV 디바이스의 IP 주소입니다.</li><li>URL에 IP 주소가 전송되지 않으면 요청 헤더에 이를 포함해서 앱스플라이어가 CTV-모바일 앱 어트리뷰션을 할 수 있도록 해야 합니다.</li></ul> |
| af\_ua | ✓ | <ul><li>광고를 표시하는 CTV 디바이스의 사용자 에이전트입니다.</li><li>사용자 에이전트가 URL에 전송되지 않은 경우, 요청 헤더에 반드시 전송되어야 합니다.그래야만 앱스플라이어가 CTV-모바일 앱 어트리뷰션을 수행할 수 있습니다.</li></ul> |
| af\_source\_platform | - | <ul><li>노출이 발생한 운영 체제를 나타내는 값 목록</li><li>값:<ul><li>안드로이드</li><li>ios</li><li>티젠</li><li>웹OS</li><li>스마트캐스트</li><li>로쿠</li><li>윈도우폰</li><li>비다</li><li>플레이스테이션</li><li>스마트캐스트</li><li>웹사이트</li></ul></li></ul> |
| af\_source\_device\_category | - | <ul><li>노출이 발생하는 디바이스 유형을 나타내는 값의 목록입니다.<ul><li>TV</li><li>모바일\_폰</li><li>데스크톱</li><li>태블릿</li><li>set\_top\_box</li><li>게임 콘솔</li><li>알 수 없는 디바이스 카테고리</li><li>미디어 플레이어</li></ul></li></ul> |

URL에 추가할 수 있는 다른 파라미터는 여기 <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">어트리뷰션 링크 구조 및 파라미터 문서에서</Anchor> 확인할 수 있습니다.

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="특징 및 제한 사항">

| 특징 | 비고 |
| --- | --- |
| 어트리뷰션 기간 | 룩백 윈도우 파라미터 에 따라 1&#126;72시간 사이입니다. |
| 리타겟팅 | <ul><li>리어트리뷰션: 크로스 플랫폼-모바일에서 지원됩니다. 다른 플랫폼에서는 해당되지 않습니다.</li><li>리인게이지먼트: 지원되지 않음</li></ul> |
| 어트리뷰션 방법 | 확률적 모델링을 사용한 뷰-쓰루 어트리뷰션 (IP 주소) |
| 가구 단위 어트리뷰션 | 지원됨. 동일 가구 내 다중 인스톨이 동일한 CTV 광고 노출에 기인할 수 있음을 의미합니다. |
| 파트너 연동 시험 | 모바일 앱-to-모바일 앱 프로드 발생률이 높아 플래그 되었거나 다른 이유로 플래그된 미디어 소스와 관련된 애드 네트워크에서는 사용할 수 없습니다. |

</Accordion>

<div data-zendesk-anchors="ctvtomobile-app-attribution-for-ad-networks=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-ctv-%EB%AA%A8%EB%B0%94%EC%9D%BC-%EC%95%B1-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98 h_01HE2X91GTDTPKKFBRRYYFMHDW=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-ctv-%EB%AA%A8%EB%B0%94%EC%9D%BC-%EC%95%B1-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98 h_01K4806R6RER2837V0M0W9BX04=%EC%B0%B8%EA%B3%A0 h_01HE2X91GT6406JZNK2RCQKPVM=setup h_01HE2X91GT1B9SG9J4C3SNAPWD=test-partner-integration h_01HE2X91GTA96HJJNG3HRV18DF=parameters h_01HE2X91GVK9P44J1MA0M44KE1=traits-and-limitations" />
