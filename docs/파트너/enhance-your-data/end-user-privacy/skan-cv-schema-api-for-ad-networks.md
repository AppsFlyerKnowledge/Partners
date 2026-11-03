---
title: 광고 네트워크를 위한 SKAN CV 스키마 API
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2026-10-14T10:37:24Z'
  id: 11705009866001
  locale: ko
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ko/articles/11705009866001
---
> **간단히 보기**: 요약: 광고주가 매핑한 SKAN CV 스키마를 확인합니다.

## 광고 네트워크를 위한 SKAN CV 스키마 API

SKAdNetwork(SKAN) 어트리뷰션을 통해 광고주는 특정 기간(기간) 동안의 설치 후 사용자 활동을 기반으로 전환 가치(CV)를 설정하여 사용자 품질을 평가합니다. <Anchor target="_blank" href="/marketers/ko/docs/skadnetwork-skan-solution-guide">SKAN에 대해 자세히 알아보기</Anchor>

iOS는 광고를 게재하는 광고 네트워크로 전송된 포스트백을 통해 CV를 리포트합니다. iOS 15부터 광고주는 포스트백을 앱스플라이어로 직접 전송하도록 iOS에 지시할 수도 있습니다.

이 API는 CV-어트리뷰션-이벤트-값 맵을 광고 네트워크에 제공합니다. 광고 네트워크는 이를 사용하여 수신한 포스트백을 디코딩합니다.

API는 중첩된 JSON으로 반환합니다. 각 앱의 스키마는 별개입니다. CV당 매핑은 conversion\_value\_mapping 배열 내에 포함됩니다.

API를 사용하려면 개발자에게 <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">광고 네트워크용 SKAN CV 스키마 API 지침</Anchor>을 따르도록 요청하십시오. 키 목록과 설명을 보려면 시뮬레이터에서 200을 클릭합니다.

**참고**:

* CV 값 범위는 다음과 같습니다.
  * SKAN 4 기간 1 세밀 값: 0-63. 24,033.07
  * SKAN 4 기간 1, 2 및 3 대략 값: 낮음, 중간 또는 높음.
  * SKAN 3 이하 0-63
* 광고주는 언제든지 CV 매핑을 변경할 수 있습니다.
* 광고 네트워크는 이 API를 매일 쿼리하여 최신 스키마를 가지고 있는지 확인해야 합니다.

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-skan-cv-%EC%8A%A4%ED%82%A4%EB%A7%88-api" />
