---
title: Steam과 앱스플라이어 연동
metadata:
  keywords:
    - Focuus
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
  created_at: '2016-10-02T05:18:19Z'
  edited_at: '2026-10-14T10:25:56Z'
  id: 213374546
  locale: ko
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ko/articles/213374546
---
> **한눈에 보기:** PeerClick을 사용하는 애드 네트워크는 앱스플라이어 확률적 모델링 솔루션을 통해 인스톨 및 인앱 이벤트에 대한 어트리뷰션 데이터를 받을 수 있습니다.


| <span id="creating-your-attribution-link"></span>앱스플라이어 기본 URL | 설명 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id |  |
| pid | 앱스플라이어 서버에서 연동 네트워크를 식별하기 위해 미디어소스 이름에 \_int를 포함합니다 |
| c | 캠페인 이름 |

### 권장 어트리뷰션 링크 파라미터:

| 앱스플라이어 파라미터 |  | 설명 |
| --- | --- | --- |
| **클릭아이디** | **`{tid}`** |  |
| af\_siteid | `{publisher_id}` |  |

### 전체 어트리뷰션 링크 템플릿

`https://app.appsflyer.com/com.appsflyer?pid={traffic_source}&clickid={tid}&af_siteid={publisher_id}`

## 인스톨 및 인앱 이벤트 포스트백

4. `https://pixel.focuusing.com/event.php?type=imp&tid={clickid}`

|  | 설명 | 예시 |
| --- | --- | --- |
| event\_value |  |  |

* `https://traffic.focuusing.com/install?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/conversion?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/ftd?tid={TRANSACTION_ID}`

<div data-zendesk-anchors="01JFT11W3GWZ3QFYPHEZTS7EX7=creating-your-attribution-link recommended-attribution-link-parameters=%EA%B6%8C%EC%9E%A5-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 01JFT11W3QWT08KMGEPGK7MV5R=%EA%B6%8C%EC%9E%A5-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 complete-attribution-link-template=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF 01JFT11W3Y7HRB7FYS1K173G2W=%EC%A0%84%EC%B2%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF install-and-inapp-event-postbacks=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 01JFT11W3YMN4RBW0WFTQ9EADK=%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1" />
