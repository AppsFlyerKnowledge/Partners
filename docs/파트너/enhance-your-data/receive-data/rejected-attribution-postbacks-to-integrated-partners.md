---
title: 연동된 파트너에 거부된 어트리뷰션 포스트백
metadata:
  keywords:
    - fraud
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
  created_at: '2017-09-19T07:03:47Z'
  edited_at: '2026-10-14T10:35:04Z'
  id: 115004744123
  locale: ko
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ko/articles/115004744123
---
> **한눈에 보기:** 연동된 파트너는 프로드 또는 유효성 검증 규칙 미준수로 인해 거부된 인스톨 및 인앱 이벤트의 포스트백을 받습니다.

<div id="rejected-attribution-postbacks-relating-to-fraud-and-validation-rules" />

## 프로드와 유효성 검증 규칙과 관련된 거부된 어트리뷰션 포스트백

**용어:**

* **프로드 이벤트:** Protect360에 의해 차단된 인스톨 및 인앱 이벤트
* **비준수 이벤트:** 유효성 검증 규칙을 준수하지 않는 인스톨 및 인앱 이벤트
* **거부된 이벤트:** 프로드 이벤트와 비준수 유효성 검증 규칙 이벤트
* **어트리뷰션이 수정된 인스톨:** 하이재킹된 인스톨이 식별되고 차단된 후, 어트리뷰션이 수정되어 실제 미디어 소스에 어트리뷰션됨.

**포스트백**

* 연동된 파트너는 거부된 이벤트 포스트백을 실시간으로 받습니다.
* 어트리뷰션이 수정된 인스톨의 인앱 이벤트에 대한 프로드 이벤트 포스트백은 없습니다.
* 거부된 이벤트 포스트백은 인스톨과 거부된 이벤트 포스트백 모두에 대해 파트너가 지정한 엔드포인트로 전송되며, 추가 파라미터는 다음과 같습니다:  
  * 차단 사유
  * 거부 세부 사유
  * 거부됨
  * 거부 사유 값(사용 가능한 경우). 예를 들어: `reject_reason=site_blacklist&reject_reason_value="1123456"&is_rejected=1`

다음 표에는 거부 사유, 거부 사유 값 및 거부 사유에 대한 설명이 나와 있습니다:

| 거부 사유 | 거부 사유 값 | 사용자가 구성할 수 있음 | 설명 |
| --- | --- | --- | --- |
| ctit\_anomalies | 측정된 클릭-인스톨 시간(초) | **x** | CTIT 이상 현상은 비정상적으로 긴 클릭-인스톨 시간으로 인해 차단된 클릭입니다. |
| 스토어 인스톨 유효성 검증 | 해당 없음 | **x** | 애플 앱 스토어에서 유효성 검증에 실패한 인스톨 |
| 사이트 블랙리스트 | 사이트 ID | **x** | 프로드 행위가 빈번하여 앱스플라이어가 차단한 사이트 ID에서 발생하는 인스톨입니다. 내부 알고리즘에 따라 결정됩니다. |
| 봇 | 해당 없음 | **x** | 봇에 의해 시도된 차단된 인스톨 시도 |
| 클릭 플러드 | 사이트 ID 또는 비어 있음 | **x** | CTIT가 높고 전환율이 낮은 인스톨이 많이 발생하여 앱스플라이어가 차단한 클러스터에서 발생하는 인스톨 |
| 이상 행동 | 해당 없음 | **x** | 비정상적이고 일관되지 않은 앱 설치 후 행동으로 인해 인스톨 프로드가 차단된 경우 |
| 인스톨 하이재킹 | 해당 없음 | **x** | 인스톨 하이재킹이 구글 플레이 서버 측 API를 기반으로, 불합리한 클릭 및 인스톨 타임을 기준으로 클릭이 차단되었습니다. |
| 유효성 검증 봇 | 규칙 이름 또는 비어 있음 | ✓ | 고객이 정의한 규칙. |
| 유효성 검증 하이재킹 | 규칙 이름 | ✓ | 고객이 정의한 규칙. |
| ai 층 | 해당 없음 | **x** | AI 모델은 방대한 양의 데이터 포인트를 분석하는 데 활용되어 사기성 디바이스 및 인스톨 활동을 식별하기 위한 탐지 기능이 강화됩니다. |

<div id="reject-reasons-for-in-app-events" />

#### 인앱 이벤트 거부 이유

| 거부 사유 | 거부 사유 값 | 설명 |
| --- | --- | --- |
| 인스톨에서 상속됨 | 인스톨에서 상속됨 | <Anchor target="_blank" href="/marketers/ko/docs/protect360-raw-data-reports#차단된-이유">인스톨</Anchor> 또는<Anchor target="_blank" href="/marketers/ko/docs/protect360-raw-data-reports#차단된-이유"> 거부</Anchor> 수준 이유를 기반으로 초기 인스톨이 가짜로 식별되었습니다. |
| 인앱봇 | 가짜 디바이스 파라미터 | 앱스플라이어 알고리즘이 프로드를 감지합니다. |
| 유효성 검증 인앱 | 잘못된\_이벤트\_이름 | 요청 또는 수동으로 정의된 유효성 검증 규칙 |
| 유효성 검증 인앱 | 잘못된 이벤트 값 | 요청 또는 수동으로 정의된 유효성 검증 규칙 |
| 유효성 검증 인앱 | 규칙 이름 | 수동으로 정의된 규칙 기반 |

<div id="important" />

> 🚧 **중요!**
>
> * 합법적인 이벤트에 대한 포스트백과 거부된 포스트백을 구분하려면 <Anchor target="_blank" href="/partners/ko/docs/postback-macros-for-ad-networks#macros-installs-inapp-events-and-rejected-events">거부된 포스트백 매크로</Anchor>를 구성해야 합니다.
> * 거부된 포스트백을 활성화하려면 먼저 다음 파라미터를 <Anchor target="_blank" href="/partners/ko/docs/self-serve-integration-management-for-ad-networks#기본-포스트백">기본 포스트백</Anchor>에 추가해야 합니다.
>   * `is-rejected`
>   * `blocked-reason`
>   * `blocked-sub-reason`
>   * `blocked-reason-value`
> * 위의 파라미터를 기본 포스트백과 고급 개인 정보 보호 포스트백에 모두 추가하면 거부된 인스톨/인앱 이벤트 포스트백이 활성화됩니다.

<div data-zendesk-anchors="rejected-attribution-postbacks-relating-to-fraud-and-validation-rules=%ED%94%84%EB%A1%9C%EB%93%9C%EC%99%80-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D-%EA%B7%9C%EC%B9%99%EA%B3%BC-%EA%B4%80%EB%A0%A8%EB%90%9C-%EA%B1%B0%EB%B6%80%EB%90%9C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01J5597AMDVWR2KTANSF7Y7T4P=%ED%94%84%EB%A1%9C%EB%93%9C%EC%99%80-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D-%EA%B7%9C%EC%B9%99%EA%B3%BC-%EA%B4%80%EB%A0%A8%EB%90%9C-%EA%B1%B0%EB%B6%80%EB%90%9C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 reject-reasons-for-inapp-events=%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B1%B0%EB%B6%80-%EC%9D%B4%EC%9C%A0 h_01J5597AMDHT5GJQN7QJZKV41F=%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B1%B0%EB%B6%80-%EC%9D%B4%EC%9C%A0 h_01J5597AMD29TAZSKZS9WTFSM5=%EC%A4%91%EC%9A%94" />
