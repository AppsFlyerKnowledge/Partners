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
  created_at: '2016-01-11T14:46:45Z'
  edited_at: '2026-10-14T10:38:01Z'
  id: 207583573
  locale: ko
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ko/articles/207583573
---
> **한눈에 보기:** PeerClick을 사용하는 애드 네트워크는 앱스플라이어 확률적 모델링 솔루션을 통해 인스톨 및 인앱 이벤트에 대한 어트리뷰션 데이터를 받을 수 있습니다.


<span id="basic-attribution-link"></span>아래에서 각 파라미터에 대한 자세한 설명이 포함된 기본 어트리뷰션 링크를 확인할 수 있습니다.

```http
https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}
```

| 앱스플라이어 기본 URL | 설명 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id | 애플리케이션 고유 ID - 프로모션하는 앱마다 변경되는 동적 값 |
| pid |  |
| c | 캠페인 이름 |

**권장 어트리뷰션 링크 파라미터:**

| 앱스플라이어 파라미터 |  | 설명 |
| --- | --- | --- |
| 클릭아이디 | `{TID}` |  |
| af\_siteid | `{SC}` |  |

전체 앱스플라이어 파라미터 목록을 보려면 <Anchor target="_blank" href="/partners/ko/docs/postback-macros-for-ad-networks">여기를 클릭하세요</Anchor>

전체 어트리뷰션 링크 템플릿

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={TID}&af_siteid={ADV_SID}
```

### 인스톨 및 인앱 이벤트 포스트백

글로벌 인스톨 포스트백:

```
https://tracking.zadsmobile.com/pb?tid={TID}
```

<div data-zendesk-anchors="01JFT0DX287AWQND2BYFSV50HW=basic-attribution-link install-and-inapp-event-postbacks=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0DX2B6FFE3K7VTXG1YVJ1=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 finalizing-your-registration=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0DX2BD8A19BY9197X11QW=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1" />
