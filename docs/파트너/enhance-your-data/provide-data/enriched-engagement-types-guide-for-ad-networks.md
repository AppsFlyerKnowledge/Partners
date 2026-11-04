---
title: 광고 네트워크를 위한 Enriched Engagement Types 가이드
metadata:
  keywords:
    - Advertisers
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2024-10-15T10:54:29Z'
  edited_at: '2026-10-14T10:40:05Z'
  id: 29221265052433
  locale: ko
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ko/articles/29221265052433
---
> **한눈에 보기:** 사용자의 다양한 엔게이지먼트 범위를 그대로 반영하고, 정확하고 효과적인 캠페인 최적화를 달성할 수 있도록 Enriched Engagement Types(EET) 어트리뷰션 링크를 생성하는 방법을 알아보세요.

Enriched Engagement Types(EET)는 사용자가 광고를 조회하거나 이와 상호작용할 때 발생하는 순간적인 노출부터 즉각적인 반응에 이르기까지, 사용자의 모든 엔게이지먼트 범위와 전환 의도를 반영합니다. 본 문서는 사용자가 광고와 상호작용하는 방식에 따라, 파트너사가 앱스플라이어 어트리뷰션 링크에서 인게이지먼트 타입을 리포팅하는 방법을 상세히 설명합니다.

<div id="disclaimer" />

> ❗️ **주의 사항**
>
> 이 기사는 파트너와 관련된 EET의 측면에 초점을 맞추고 있습니다. EET가 무엇인지 알아보고 이에 대한 종합적인 정보를 확인하려면 <Anchor target="_blank" href="/marketers/ko/docs/about-enriched-engagement-types#which-ad-networks-report-enriched-engagement-types">Enriched Engagement Types</Anchor> 문서를 참조하세요.

<div id="which-networks-can-report-eet-to-appsflyer" />

## 어떤 네트워크가 AppsFlyer에 EET를 보고할 수 있나요?

Enriched Engagement 기능은 앱스플라이어 파트너 프로그램의 Premier, Advance, 또는 Engage 기준을 충족하는 네트워크에 한해 지원됩니다. 이 등급들은 양사의 공통 고객에게 지속적으로 높은 품질의 트래픽을 대규모로 제공하고, 인게이지먼트 데이터를 투명하고 신뢰할 수 있는 방식으로 전송하며, 앱스플라이어의 광범위한 서비스와 연동되어 활발하게 활동 중인 네트워크를 의미합니다.

<div id="note" />

> 📘 **참고**
>
> 인게이지드 뷰와 클릭을 리포팅하기 위해, 광고 네트워크는 앱스플라이어 서포트 팀에 문의해야 합니다.

[EET 리포팅이 가능한 네트워크 목록](#01JCAT81K2EJNH91YS6NJGMXMB-data-title)을 확인해 보세요.

<div id="warning" />

> ❗️ **경고**
>
> `af_engagement_type` 매개변수가 포함되어 있더라도 허용되지 않은 네트워크로부터 발생한 클릭과 노출은 거부되며, 어트리뷰션에 반영되지 않습니다.

<div id="engaged-click-or-engaged-view-attribution-flow" />

<Accordion title="인게이지드 클릭 또는 인게이지드 뷰 어트리뷰션 플로우">

다음 단계는 최초 광고 노출부터 인게이지드 클릭 또는 인게이지드 뷰를 거쳐 설치 이벤트의 최종 어트리뷰션에 이르기까지의 흐름을 보여줍니다.

1. 광고 네트워크가 광고를 표시합니다.
2. 광고 네트워크는 지정된 `af_ad_tran_id` 매개변수가 포함된 노출 데이터를 앱스플라이어로 전송합니다.
3. 사용자가 광고와 상호작용하고 있습니다.
4. 광고 네트워크는 `af_engagement_type`, `af_ad_tran_id`, `af_ad_format`, `af_ad_type`와 선택적으로 `viewability` 매개변수를 포함하여 클릭 또는 노출을 전송합니다.
5. 앱스플라이어는 설치 이벤트를 인게이지드 클릭 또는 인게이지드 뷰와 매칭합니다.
6. 앱스플라이어는 해당 설치 이벤트를 광고 네트워크의 성과로 어트리뷰션합니다.

</Accordion>

<div id="parameters-for-reporting-engagement-types-in-attribution-links" />

<Accordion title="어트리뷰션 링크에서 참여 타입을 리포팅하기 위한 매개변수">

네트워크는 어트리뷰션 링크에 다음 파라미터들을 포함시켜 참여 타입을 리포팅할 수 있습니다.

* `af_engagement_type`: 인게이지먼트 유형 예시: `engaged_click`, `click_to_app` 또는 `engaged_view`. 다양한 인게이지먼트 유형과 그 설명에 대한 포괄적인 목록을 확인하세요.
* `af_ad_type`: 광고 유형. 예를 들어 `rewarded_video`, `interstitial` 또는 `banner`. 다양한 광고 유형과 이에 대한 설명이 담긴 전체 목록을 확인해 보세요.
* `af_ad_format`: 광고 형식, 예를 들어 `text`, `image`, `video`, `playable`. <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#af_ad_format">다양한 광고 포맷과 이에 대한 설명이 담긴 전체 목록</Anchor>을 확인해 보세요.
* `viewability`: (선택 사항) 인게이지먼트에 대한 추가 정보, 예를 들어, `af_video_total_length`, `af_ad_time_viewed`, `af_audio_played_length`. 다양한 가시성 옵션과 이에 대한 설명이 담긴 전체 목록을 확인해 보세요.
* `af_ad_tran_id`: 앱스플라이어가 이전 노출과 매칭하여 인게이지드 클릭 또는 인게이지드 뷰를 검증할 수 있도록 지원하는 트랜잭션 ID입니다.
* `is_skoverlay=true` 또는 `is_autostore=true` : [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) 또는 Android Auto Inline Installs에 의해 트리거된 인게이지드 뷰를 식별합니다.

**인게이지드 클릭 예시**

```http HTTPS
https://app.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_click&af_ad_type=interstitial&af_ad_format=playable&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0
```

**인게이지드 뷰 예시**

```http
https://impression.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_view&af_ad_type=interstitial&af_ad_format=video&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0&af_video_total_length=20&af_video_played_length=15
```

</Accordion>

<div id="user-engagements-to-report-as-engaged-clicks" />

<Accordion title="사용자 인게이지먼트를 인게이지드 클릭으로 보고">

*인게이지드 클릭*은 사용자를 앱스토어로 리다이렉트하거나 앱을 실행하지 않고, 동일한 컨텍스트 내에 머물게 하면서 광고와 상호작용하도록 만드는 클릭을 의미합니다.

아래는 광고 네트워크가 `af_engagement_type=engaged_click` 매개변수 값으로 보고해야 하는 사용자 인게이지먼트의 예입니다.

* **재생 가능한 광고:** 미니 게임을 플레이하거나 광고 내 인터랙티브 콘텐츠를 실행하기 위해 탭하는 등, 플레이어블 광고와 상호작용하기 위해 발생하는 클릭을 의미합니다.
* **소셜 인게이지먼트:** 소셜 미디어 플랫폼에서 광고에 좋아요를 누르거나, 댓글을 달거나, 공유하여 추가적인 상호작용과 잠재적인 바이럴 효과를 촉진하는 클릭을 의미합니다.
* **리디렉션:** 랜딩 페이지나 다른 외부 콘텐츠 사이트/페이지를 방문하기 위해 발생하는 클릭을 의미합니다.
* **동적 제품 광고/카탈로그 또는 캐러셀:** 상품 사이를 스와이프해서 다른 상품을 확인하도록 하는 클릭입니다.
* **위시리스트 추가:** 앱 또는 외부 웹사이트에서 홍보 중인 상품을 위시리스트나 관심 목록에 추가하기 위해 발생하는 클릭을 의미합니다.
* **나중에 보기 위해 저장하기:** 추후에 다시 확인하기 위해 광고와 해당 콘텐츠를 저장하는 클릭으로, 광고에 다시 방문하거나 세부 사항을 더 탐색하려는 의도를 나타냅니다.
* **북마크 또는 컬렉션에 추가:** 광고를 북마크하거나 앱 내의 큐레이션된 컬렉션에 추가하기 위해 발생하는 클릭으로, 광고에 다시 방문하거나 카테고리별로 분류하려는 의도를 나타냅니다.
* **광고 음소거 해제:** 오디오를 활성화하려면 클릭하세요.

**앱스플라이어에 인게이지드 클릭을 보고하지 않아야 할 때는 언제인가요?**

다음은 광고 네트워크가 `engaged_click` 파라미터 값으로 리포팅해서는 **안** 되는 사용자 인게이지먼트 예시입니다.

* **광고 해제:** 광고를 닫거나 무시하기 위해 "x" 버튼 또는 이와 유사한 표시를 클릭하는 행위로, 추가적인 인게이지먼트에 관심이 없음을 나타냅니다.
* **광고 건너뛰기**: 광고를 건너뛰고 원래 보려던 콘텐츠로 바로 이동하기 위해 특정 버튼을 클릭하는 행위로, 해당 광고가 사용자에게 흥미롭지 않거나 관련이 없음을 나타냅니다.
* **광고 신고**: 불쾌함, 오도성, 부적절함 등의 이유로 광고를 신고하기 위해 클릭하는 행위로, 광고 콘텐츠에 대한 불만이나 거부감을 나타냅니다.
* **옵트아웃 또는 구독 취소**: 향후 유사한 광고를 수신하지 않기 위해 수신 거부 또는 구독 취소를 클릭하는 행위로, 해당 광고나 관련 카테고리와의 관계를 중단하려는 의도를 나타냅니다.
* **광고 종료:** 현재의 광고 환경을 벗어나 사용자에게 광고된 컨텍스트나 랜딩 페이지 외의 다른 외부 영역으로 이동하게 만드는 링크나 버튼을 클릭하는 행위입니다.
* **광고 음소거:** 비디오의 소리를 음소거 합니다.

</Accordion>

<div id="user-engagements-to-report-as-engaged-views" />

<Accordion title="인게이지드 뷰로 리포팅해야 하는 사용자 인게이지먼트">

네트워크는 다음과 같은 경우에 `af_engagement_type=engaged_view` 값을 포함하여 사용자 인게이지먼트를 리포팅해야 합니다.

* **건너뛸 수 있는 광고 단위:** 사용자가 동영상 광고에서 건너뛰기 옵션이 나타난 후에도 5초 이상 광고를 추가로 시청한 경우입니다. 네트워크가 시청 시간(초)을 측정할 수 없는 경우에는 다음과 같이 처리합니다.
  * 비디오 길이가 20초보다 긴 경우, 2/4 지점(50% 재생 시점)이 완료되었을 때 `engaged_view`을(를) 전송합니다.
  * 비디오 길이가 20초보다 짧은 경우, 전체 시청을 완료(100% 재생 완료)했을 때 `engaged_view`을(를) 전송합니다.
  * `af_ad_format` 매개변수 값은 `video` 또는 `playable`이어야 합니다.
* **보상형 비디오**: 사용자는 보상을 받는 동영상을 끝까지 시청합니다. `af_ad_type` 매개변수 값은 `rewarded_video` 이어야 합니다.
* **자동 StoreKit 렌더링 광고:** StoreKit 렌더링 광고(예: [`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay) 또는 [`SKStore`](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller))에서 발생하는 클릭은 퍼블리셔가 기록하지 않으며, SKAdNetwork(SKAN) 어트리뷰션을 위해 Apple에 의해 기록됩니다. Android Auto Inline Installs(오토스토어)의 경우도 마찬가지입니다.

  광고 네트워크 측에서는 해당 광고와의 실제 인게이지드 여부를 판별할 방법이 없기 때문에, 사용자의 실제 액션이 없었더라도 광고가 화면에 노출되는 시점에 노출 또는 클릭을 리포팅하게 됩니다.

  광고 네트워크는 광고가 노출될 때마다 `click_to_app` 인게이지먼트 유형을 리포팅할 수도 있지만, 이 경우 CTR이 비정상적으로 높아질 위험이 있습니다. Android의 Auto Inline Installs(오토인라인 인스톨)의 경우도 이와 마찬가지입니다.

  이러한 리스크를 완화하기 위해, 대신 해당 인게이지먼트 타입을 리포팅할 것을 권장합니다. 이 사용 사례에서는 어트리뷰션 링크에 iOS의 경우 `is_skoverlay=true`을(를), Android의 경우 `is_autostore=true`을(를) 반드시 포함해야 합니다.

**앱스플라이어에 인게이지드 뷰를 보고하지 않아야 할 때는?**

다음은 광고 네트워크가 `engaged_view` 매개변수 값으로 리포팅해서는 **안** 되며, 대신 다른 `view` 매개변수를 사용하여 리포팅해야 하는 사용자 인게이지먼트 유스케이스입니다.

* 사용자는 보상 비디오가 아니고 `SKOverlay` 또는 `autostore` 광고로 오버레이되지 않은 건너뛸 수 없는 광고를 시청합니다.

</Accordion>

<div id="01JCAT81K2EJNH91YS6NJGMXMB-data-title" />

<Accordion title="EET 보고가 가능한 네트워크">

허용된 네트워크 목록에는 앱스플라이어가 처리할 수 있는 인리치드 Enriched Engagement-type 이벤트를 지원하는 파트너들이 포함되며, 이때 인게이지드 클릭 및 인게이지드 뷰는 제외됩니다. 이 목록에 있는 네트워크 중 앱스플라이어가 자사의 인게이지드 클릭 및 인게이지드 뷰를 처리하기를 원하는 파트너는 앱스플라이어 지원 센터에 문의해야 합니다. 어떤 네트워크가 이미 앱스플라이어에서 인게이지드 클릭 및 뷰 데이터를 처리하고 있는지 확인하려면, <Anchor target="_blank" href="/marketers/ko/docs/about-enriched-engagement-types#allowed-networks">EET 광고주 안내 문서</Anchor>를 참조하세요.

<div id="warning-1" />

> ❗️ **경고**
>
> `af_engagement_type` 매개변수가 포함되어 있더라도 허용되지 않은 네트워크로부터 발생한 클릭과 노출은 거부되며, 어트리뷰션에 반영되지 않습니다.

| 파트너 이름 |
| --- |
| AdColony |
| Adaction |
| Adaction3 |
| Adikteev |
| adjoe GmbH |
| Amazon |
| Amazon DSP |
| AppLovin |
| Appier |
| AppNext |
| Apple Search Ads |
| Unity의 Aura |
| AWIN |
| Bidease |
| ByteDance Ads China |
| Cauly |
| Criteo |
| Digital Turbine |
| Digital Turbine On Device |
| Fluent |
| Glance |
| Google Ads(애드워즈) |
| Google Marketing Platform(DV360/CM360) |
| Hotstar |
| Huawei |
| InMobi DSP |
| ironSource |
| Jampp |
| Josh |
| Kakao |
| Kuaishou |
| Liftoff |
| Line |
| Meta Ads |
| Mintegral |
| Mistplay |
| Motorola Pre-Install |
| Naver |
| OPPO |
| OPPO Global |
| OPPO Store Traffic(글로벌) |
| OPPOPAI Pre-Install |
| PayTM |
| Rakuten |
| Reddit |
| Remerge |
| RevX |
| Samsung |
| Smadex |
| Snapchat |
| Stackadapt |
| Tapjoy |
| Tencent AMS |
| TikTok for Business - Advanced SRN |
| TikTok for Business - Legacy |
| The Trade Desk |
| Transsion |
| Treasure Data |
| Truecaller |
| Unity Ads |
| Vivo Preload |
| vivo Global |
| Vungle |
| X Ads(이전의 Twitter Ads) |
| Xiaomi Global |
| XiaomiPAI Pre-Install |
| Yahoo Japan |
| Yandex |
| YouAppi |

</Accordion>

<div data-zendesk-anchors="01JA7WZH43ECDKRC0R0J89ED1E=%EC%A3%BC%EC%9D%98-%EC%82%AC%ED%95%AD which-networks-can-report-eet-to-appsflyer=%EC%96%B4%EB%96%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-appsflyer%EC%97%90-eet%EB%A5%BC-%EB%B3%B4%EA%B3%A0%ED%95%A0-%EC%88%98-%EC%9E%88%EB%82%98%EC%9A%94 h_01JJPVYGWZSFSATZ4TH5VBSVXW=%EC%96%B4%EB%96%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-appsflyer%EC%97%90-eet%EB%A5%BC-%EB%B3%B4%EA%B3%A0%ED%95%A0-%EC%88%98-%EC%9E%88%EB%82%98%EC%9A%94 01JAN5JRM56C6S6EP27WFJ2Y4W=%EC%B0%B8%EA%B3%A0 h_01J00XFV133YYAB7YPQNXM5R37=%EA%B2%BD%EA%B3%A0 01JA7WZH46RJBG996NG9EZV7T9=engaged-click-or-engaged-view-attribution-flow 01JA7WZH4BZVGS9Z1NNHQC72N6=parameters-for-reporting-engagement-types-in-attribution-links 01JA7WZH4JDJFCVT25WJ4GNE20=user-engagements-to-report-as-engaged-clicks 01JA7WZH4Q32TEWM5EKME142R7=user-engagements-to-report-as-engaged-views 01JCAT81K2EJNH91YS6NJGMXMB%20data-title%3D=01JCAT81K2EJNH91YS6NJGMXMB-data-title allowed-network-list=01JCAT81K2EJNH91YS6NJGMXMB-data-title h_01JJPVYGWZ4T6TPFRWTR2AB027=%EA%B2%BD%EA%B3%A0-1" />
