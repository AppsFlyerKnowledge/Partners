---
title: 광고 네트워크에 대한 Protect360 리포트
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2022-02-08T14:53:48Z'
  edited_at: '2026-10-14T10:29:07Z'
  id: 4420246395793
  locale: ko
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/ko/articles/4420246395793
---
> **한눈에 보기:** UA 및 리타게팅을 담당하는 광고 네트워크는 차단된 클릭 및 노출에 대한 데이터를 수신할 수 있습니다.

<div id="protect360-reports-for-ad-networks" />

## 광고 네트워크에 대한 Protect360 리포트

주의 사항


* <span id="report-considerations"></span>데이터 최신성: <Anchor target="_blank" href="/marketers/ko/docs/about-data-freshness-and-timezone-support#ad-revenue">매일, 즉 0일 차 데이터는 1일 차에 도착합니다</Anchor>. 데이터는 매일 21:00(UTC 시간)에 데이터 락커 버킷의 h=23에 기록됩니다./span>
* 앱 포함 내역:

<div id="blocked-clicks-and-impressions" />

<div id="report-types" />

## 리포트 유형

<div id="report-structure-fieldsdimensions" />

#### 리포트 구조 필드 및 차원

| **필드** | **비고** |
| --- | --- |
| app\_id | 앱스플라이어 플랫폼에서의 앱 ID |
| site\_id | 광고를 게재하는 퍼블리셔를 식별하는 고유 ID입니다. |
| date |  |
| agency |  |

<div id="failed-click-signatures" />

<div id="report-structure-metrics" />

#### 리포트 구조: 측정 지표

| **필드** | **비고** |
| --- | --- |
| number\_of\_blocked\_clicks |  |
| number\_of\_blocked\_impressions |  |
| number\_of\_capped\_clicks |  |
| number\_of\_capped\_impressions |  |


<div id="report-structure-fieldsdimensions-1" />

#### 리포트 구조 필드 및 차원

| **필드** | **비고** |
| --- | --- |
| event\_time |  |
| original\_url |  |
| failed\_signing\_reason | 예를 들어:<ul><li>유효하지 않은 서명</li><li>서명 누락</li></ul> |
| is\_blocking\_enabled |  |

<div data-zendesk-anchors="protect360-reports-for-ad-networks=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%97%90-%EB%8C%80%ED%95%9C-protect360-%EB%A6%AC%ED%8F%AC%ED%8A%B8 report-types=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%9C%A0%ED%98%95 report-structure-fieldsdimensions=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EA%B5%AC%EC%A1%B0-%ED%95%84%EB%93%9C-%EB%B0%8F-%EC%B0%A8%EC%9B%90 report-structure-metrics=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EA%B5%AC%EC%A1%B0-%EC%B8%A1%EC%A0%95-%EC%A7%80%ED%91%9C report-structure-fieldsdimensions::44afb679=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EA%B5%AC%EC%A1%B0-%ED%95%84%EB%93%9C-%EB%B0%8F-%EC%B0%A8%EC%9B%90-1" />
