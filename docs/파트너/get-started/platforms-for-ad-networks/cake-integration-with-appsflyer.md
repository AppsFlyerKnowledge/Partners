---
title: Roku와 앱스플라이어 연동
metadata:
  keywords:
    - Advertisers
    - Ad Networks
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
  created_at: '2016-01-11T14:44:55Z'
  edited_at: '2026-10-14T10:35:52Z'
  id: 207273986
  locale: ko
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ko/articles/207273986
---
> **한눈에 보기:**

<div id="base-attribution-link" />

## 기본 어트리뷰션 링크

아래에서 각 파라미터에 대한 자세한 설명이 포함된 기본 어트리뷰션 링크를 확인할 수 있습니다.

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| 앱스플라이어 기본 URL | 설명 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id | 애플리케이션 고유 ID - 프로모션하는 앱마다 변경되는 동적 값 |
| pid |  |
| c | 캠페인 이름 |

<div id="recommended-attribution-link-parameters" />

### 권장 어트리뷰션 링크 파라미터:

| 앱스플라이어 파라미터 |  | 설명 |
| --- | --- | --- |
| 클릭아이디 | #oreqid# |  |
| af\_siteid | #affid# |  |

전체 앱스플라이어 파라미터 목록을 보려면 <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">여기를 클릭하세요</Anchor>

<div id="complete-attribution-link-template" />

### 전체 어트리뷰션 링크 템플릿

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#oreqid#
```

<div id="install-and-in-app-event-postbacks" />

## 인스톨 및 인앱 이벤트 포스트백

<div id="global-install-postback" />

### 글로벌 인스톨 포스트백:

```http
https://{company-domain}.com/p.ashx?f=pb&r=(Click-ID)
```

<div id="finalizing-your-registration" />

<div id="global-in-app-event-postback" />

### 글로벌 인앱 이벤트 포스트백:

```http
Click-ID
```

광고주가 각 앱의 앱스플라이어 대시보드에서 **이벤트 태그**로 설정한 앱의 실제 인앱 이벤트 이름


<Image align="center" alt="IAEP.png" src="https://files.readme.io/3ce734c3930649fdb0b119cd6e12e135e6bcba19225862e9e93b93991451fc8b-360002326529.png" />

<span id="appsflyer-in-app-events-dashboard"></span><span id="appsflyer-inapp-events-dashboard"></span>요청에 따라 국가 코드, 광고 ID, IDFA 등과 같은 추가 어트리뷰션 정보를 포스트백에 추가할 수 있습니다.

<div data-zendesk-anchors="base-attribution-link=%EA%B8%B0%EB%B3%B8-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC 01EZPMKP0AFM26H2ZG9FY1D2S4=%EA%B8%B0%EB%B3%B8-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC recommended-attribution-link-parameters=%EA%B6%8C%EC%9E%A5-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 01EZPMKP0A7DBV5KAGZ08C3R49=%EA%B6%8C%EC%9E%A5-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 complete-attribution-link-template=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF 01EZPMKP0AH1MB0XYE3PXQPP0V=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF install-and-inapp-event-postbacks=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01EZPMKP0A2D0PB41GD04HX9JX=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 global-install-postback=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01EZPMKP0AVAJRP8YM48T4GV47=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 global-inapp-event-postback=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01EZPMKP0AM7JD7HWW7BCJDQF3=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01EZPMKP0AJTYT0G9E8G833KT0=appsflyer-inapp-events-dashboard finalizing-your-registration=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HY03H1PMWZX3T12RZFV15CFE=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1" />
