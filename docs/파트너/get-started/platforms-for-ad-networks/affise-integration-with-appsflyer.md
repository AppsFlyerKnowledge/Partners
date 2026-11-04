---
title: Steam과 앱스플라이어 연동
metadata:
  keywords:
    - Integration
    - affise
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
  created_at: '2016-04-19T12:08:58Z'
  edited_at: '2026-10-14T10:33:21Z'
  id: 208537116
  locale: ko
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ko/articles/208537116
---
> **한눈에 보기:** PeerClick을 사용하는 애드 네트워크는 앱스플라이어 확률적 모델링 솔루션을 통해 인스톨 및 인앱 이벤트에 대한 어트리뷰션 데이터를 받을 수 있습니다.

연동을 시작하려면 앱스플라이어에 어트리뷰션 링크와 리포팅을 위한 포스트백을 모두 보내야 합니다.

<div id="base-attribution-link" />

## 기본 어트리뷰션 링크

아래에서 각 파라미터에 대한 자세한 설명이 포함된 기본 어트리뷰션 링크를 확인할 수 있습니다.

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}&af_c_id={offerid}
```

| 앱스플라이어 파라미터 |  | 설명 |
| --- | --- | --- |
| 클릭아이디 | `{clickid}` |  |
| af\_siteid | `{pid}` |  |
| af\_c\_id | `{offer_id}` |  |

전체 앱스플라이어 파라미터 목록을 보려면 <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">여기를 클릭하세요</Anchor>

<div id="complete-attribution-link-template" />

## 전체 어트리뷰션 링크 템플릿

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}
```

<div id="install-and-in-app-event-postbacks" />

## 인스톨 및 인앱 이벤트 포스트백

<div id="global-in-app-event-postback-android" />

<div id="global-install-postback-android" />

<div id="global-install-postback-ios" />

### 글로벌 인스톨 포스트백:

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}
```


```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}
```

<div id="finalizing-your-registration" />

<div id="global-in-app-event-postback-ios" />

### 글로벌 인앱 이벤트 포스트백:

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}&goal={event-name}
```


```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}&goal={event-name}
```

광고주가 각 앱의 앱스플라이어 대시보드에서 **이벤트 태그**로 설정한 앱의 실제 인앱 이벤트 이름

요청에 따라 국가 코드, 광고 ID, IDFA 등과 같은 추가 어트리뷰션 정보를 포스트백에 추가할 수 있습니다.

<div data-zendesk-anchors="base-attribution-link=%EA%B8%B0%EB%B3%B8-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC 01JFT0RZG0F67JFBC7W5KK54BM=%EA%B8%B0%EB%B3%B8-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC complete-attribution-link-template=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF 01JFT0RZG2QTT3Z9S6SVNV5VE7=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF install-and-inapp-event-postbacks=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0RZG3C7MBBYFKA6W813PF=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 global-install-postback-ios=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0RZG3HM9P81XYGKHZXHFK=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 global-install-postback-android=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 global-inapp-event-postback-android=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0RZG4JCDP8D4CWQW02AY7=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0RZG4PA9WTP212AX52QWZ=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%8A%A4%ED%86%A8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 global-inapp-event-postback-ios=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0RZG40N0VNNVMDBFYNT9E=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 finalizing-your-registration=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT0RZG52JW6C5GR0KA4CZF6=%EA%B8%80%EB%A1%9C%EB%B2%8C-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1" />
