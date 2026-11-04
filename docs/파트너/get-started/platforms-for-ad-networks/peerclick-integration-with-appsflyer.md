---
title: 앱스플라이어와 PeerClick 연동
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
  created_at: '2024-01-07T08:27:18Z'
  edited_at: '2026-10-14T10:40:39Z'
  id: 21479841979793
  locale: ko
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ko/articles/21479841979793
---
> **한눈에 보기:** PeerClick을 사용하는 애드 네트워크는 앱스플라이어 확률적 모델링 솔루션을 통해 인스톨 및 인앱 이벤트에 대한 어트리뷰션 데이터를 받을 수 있습니다.

<div id="starting-the-integration" />

## 연동 시작하기

연동을 시작하려면 앱스플라이어에 어트리뷰션 링크와 리포팅을 위한 포스트백을 모두 보내야 합니다.

아래에서 각 파라미터에 대한 자세한 설명이 포함된 기본 어트리뷰션 링크를 확인할 수 있습니다.

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| 앱스플라이어 기본 URL | 설명 |
| --- | --- |
| https://app.appsflyer.com | 앱스플라이어 엔드포인트 |
| app\_id | 애플리케이션 고유 ID - 프로모션하는 앱마다 변경되는 동적 값 |
| pid= |  |
| c= | 캠페인 이름 |

**권장 어트리뷰션 링크 파라미터:**

| 앱스플라이어 파라미터 | Voluum 매크로 | 설명 |
| --- | --- | --- |
| &clickid= | `{clickid}` | 유저 세션의 고유 트랜잭션 ID - **필수** |
| &af\_siteid= | `{trafficsource.id}` | 트래픽 소스 ID - **선택** |

<div id="note" />

> 📘 **참고**
>
> * 전체 앱스플라이어 파라미터 목록을 보려면 <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">여기를 클릭하세요</Anchor>
> * 전체 PeerClick 목록을 보려면 <Anchor target="_blank" href="https://help-center.peerclick.com/en/">여기를 클릭하세요</Anchor>

<div id="complete-attribution-link-template" />

### 전체 어트리뷰션 링크 템플릿

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### 인스톨 및 인앱 이벤트 포스트백

**글로벌 인스톨 포스트백:**

```http
https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}
```

**글로벌 인앱 이벤트 포스트백:**

`https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}&payout={monetary}&txid={event-name}`

* **userid:** PeerClick에서 제공한 유저 ID
* **txid:** 광고주가 각 앱의 앱스플라이어 대시보드에서 **이벤트 태그**로 설정한 앱의 실제 인앱 이벤트 이름

<div id="appsflyers-in-app-event-dashboard" />

### 앱스플라이어의 인앱 이벤트 대시보드

![Voluum_msc_new_1.png](https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png)  
요청에 따라 국가 코드, 광고 ID, IDFA 등과 같은 추가 어트리뷰션 정보를 포스트백에 추가할 수 있습니다.

<div data-zendesk-anchors="starting-the-integration=%EC%97%B0%EB%8F%99-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0 h_01HKHFT3RFWF5H349GP7MHDAYX=%EC%97%B0%EB%8F%99-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0 h_01HM8M27S5WFJVKBG0JAFW548H=%EC%B0%B8%EA%B3%A0 complete-attribution-link-template=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF h_01HKHFT3RFDW6GZM3E72SYPJSD=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF install-and-inapp-event-postbacks=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HKHFT3RF1PTSJ4SF9RTQ93N8=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 appsflyers-inapp-event-dashboard=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EC%9D%98-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C h_01HKHFT3RFDVPCSKJGZPRFB55V=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EC%9D%98-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C" />
