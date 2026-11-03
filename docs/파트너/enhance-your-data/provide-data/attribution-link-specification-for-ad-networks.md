---
title: 광고 네트워크를 위한 어트리뷰션 링크 사양
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2021-12-06T10:31:00Z'
  edited_at: '2026-10-14T10:30:42Z'
  id: 4412938154513
  locale: ko
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ko/articles/4412938154513
---
> **요약:** 앱스플라이어와 연동하는 광고 네트워크는 본 문서에 따라 어트리뷰션 링크를 지정해야 합니다.

## 광고 네트워크를 위한 어트리뷰션 링크

어트리뷰션 링크는 사용자가 광고를 클릭했음을 앱스플라이어에 알리는 데 사용됩니다. 가장 간단한 형태로, 광고 뒤에 어트리뷰션 링크를 배치하여 사용자가 광고를 클릭할 때 어트리뷰션 링크를 클릭하게 됩니다.

### 어트리뷰션 모델

첫 번째 클릭이나 노출에서부터 인스톨 또는 이벤트 어트리뷰션, 그리고 그 이후까지의 여정을 설명합니다.

[altappsflyer-attribution-model-for-partners.pngalt](https://support.appsflyer.com/hc/article_attachments/51858280490129)

1. 유저가 배너나 오퍼 링크를 클릭합니다.
2. 배너나 링크가 유저를 앱스플라이어 어트리뷰션 링크로 리디렉션합니다. 앱스플라이어 어트리뷰션 링크는 클릭 시 수집된 정보로 채워집니다.
3. 앱스플라이어는 어트리뷰션 링크에서 정보를 수집해 데이터베이스에 저장합니다.
4. 인스톨이 발생하고 앱이 처음으로 실행됩니다. 앱 내의 앱스플라이어 SDK가 앱이 설치된 디바이스에 대한 정보를 앱스플라이어 서버에 전송합니다.
5. 앱스플라이어는 **어트리뷰션 메서드**를 사용하여 이 데이터를 클릭 데이터베이스와 매칭합니다.
   * **리퍼러 매칭**  
     이 어트리뷰션 메서드는 안드로이드 디바이스에만 적용됩니다. 유저가 링크를 클릭해 구글 플레이로 리디렉션될 때, 구글 플레이는 고유한 리퍼러 ID를 부여합니다. 인스톨이 발생하면, 앱스플라이어는 디바이스에서 이 ID를 수집합니다. 그런 다음, 이를 구글 플레이 기록과 매칭합니다.
   * **디바이스 ID 매칭**  
     앱스플라이어는 클릭 시 수집된 디바이스 ID(iOS의 IDFA 또는 안드로이드 디바이스의 GAID)를 인스톨을 수행한 디바이스의 ID와 일치시킵니다.
   * <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-attribution-model#probabilistic-modeling">**확률적 모델링**</Anchor>

   <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-attribution-model">어트리뷰션 메서드</Anchor>에 대해 자세히 알아보기.

   앱스플라이어는 클릭 데이터베이스 내에서 리퍼러, 디바이스 ID 및 확률적 모델링 데이터 포인트(순서대로)를 검색합니다. 일치하는 항목을 찾으면, 인스톨을 클릭에 어트리뷰션합니다. 일치하는 항목이 없으면, 인스톨을 오가닉 다운로드로 어트리뷰션합니다.
6. 인스톨이 어트리뷰션되면, 전환 상세 내역을 애드 네트워크에 포스트백으로 발송합니다.

이 과정에서, 어트리뷰션 링크를 통해 정보를 수집하고 포스트백으로 정보를 다시 발송합니다.

> 📘 **참고**
>
> TUNE, CAKE 또는 Affise와 같은 써드 파티 성과 마케팅 도구를 사용하는 경우 <Anchor target="_blank" href="/partners/ko/docs/platforms-for-ad-networks">플랫폼별 지침</Anchor>을 참조하십시오.

### 어트리뷰션 링크 템플릿

어트리뷰션 링크(배너/오퍼에 적용되는 링크)는 다음과 같습니다:

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={clickid}&advertising_id={gaid}&af_siteid={affiliate_id}&af_cost_model=CPI&af_cost_value={cost_value}&af_cost_currency={currency}&c={Campaign}&af_ad_type={AdType}&af_adset={Adset}&af_ad={Ad}&is_incentivized={true\false}&expires={timestamp}&signature={signature}
```

`https://app.appsflyer.com/`은 앱스플라이어 엔드포인트이고, `com.yourapp`는 앱 ID이며, `pid=mediaName_int`은 귀사의 네트워크에 할당된 고유한 미디어 소스 이름입니다.

링크의 이 부분은 고정적이며, 귀사에서 별도로 수행할 필요는 없습니다.

링크 구조 설명:

* '=' 이후 `{} 내부의 값은 클릭이 발생할 때 삽입되어 앱스플라이어로 전송됩니다. 템플릿을 준비할 때 괄호 {}` 내부의 값을 귀사의 파라미터 이름으로 바꿉니다.
* 귀사의 시스템이 매크로 이름을 실제 정확한 값으로 대체하기만 하면, 매크로 이름 자체는 큰 의미가 없습니다. '=' 기호 이전의 파라미터는 앱스플라이어가 사용하는 플레이스홀더로서, 어떤 값이 전송되는지 파악할 수 있게 합니다.
* 귀사의 매크로 이름을 포함한 어트리뷰션 링크 템플릿을 이메일로 발송해 주세요.

다음 표에 나열된 파라미터를 권장 최소값으로 간주합니다. 더 많은 파라미터를 지원합니다. 클릭에서 수집한 만큼의 정보를 최대한 공유해 주세요. <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#어트리뷰션-링크-파라미터">어트리뷰션 링크 파라미터 목록</Anchor>을 참조하십시오.

#### 권장 최소 어트리뷰션 링크 파라미터

| 파라미터 | 설명 |
| --- | --- |
| `&clickid={clickid}` | 클릭 ID는 귀사의 애드 네트워크에서 발생하는 각 클릭의 고유한 식별자입니다. |
| `&advertising_id={gaid}` 또는  <br />`&idfa={IDFA}` | 클릭이 발생한 디바이스의 디바이스 ID (안드로이드는 GAID, Apple은 IDFA). |
| `&c={campaign}` | 광고주가 정의한 캠페인 이름입니다. |
| `&af_siteid={publisher_id}` | 클릭을 일으킨 퍼블리셔 또는 어필리에이트의 퍼블리셔 ID나 어필리에이트 ID입니다. |
| `&af_ad_type={search_text}` | 광고 유형. 다음과 같은 이름 규칙을 사용할 수 있습니다.  <br />search\_text  <br />배너  <br />interstitial  <br />비디오  <br />rewarded\_video  <br />playable  <br />sponsored\_content  <br />오디오 |
| `&af_adset={adsetid}` | 광고 세트 이름 – 광고주 또는 퍼블리셔가 제공합니다. 광고 세트는 캠페인과 광고 사이의 중간 데이터 계층 구조 수준입니다. <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#데이터의-세분화-수준">더 보기</Anchor> |
| `&af_ad={ad_id}` | 광고 이름( <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters#데이터의-세분화-수준">참조</Anchor>) - 광고주 또는 퍼블리셔가 제공합니다. |
| `&is_incentivized={true}` | 보상형 또는 비보상형 캠페인 (true/false). |
| `&af_cost_value={cost_value}` | 전환 비용 값은 소수점 아래 4자리까지 지원합니다.  <br />반드시 숫자만 사용하십시오 (필요한 경우, 소수점 포함) 예: "56", "2.85" 등. |
| `&af_cost_currency={currency}` | 비용 통화 – 통화 코드 (예: USD, EUR). 기본 값은 USD입니다.  <br /><Anchor target="_blank" href="https://en.wikipedia.org/wiki/ISO_4217">통화 코드 목록</Anchor>. |
| `&expires={timestamp}` | 애드 네트워크가 클릭을 청구하지 않는 Unix 타임스탬프입니다. 클릭 프로드를 방지하기 위해 클릭 서명에 사용됩니다. <Anchor target="_blank" href="/partners/ko/docs/click-signing-for-ad-networks">더 보기</Anchor> |
| `&signature={signature}` | HMAC-SHA256 서명은 클릭을 검증하고 프로드를 방지하는 데 사용됩니다. <Anchor target="_blank" href="/partners/ko/docs/click-signing-for-ad-networks">더 보기</Anchor> |

<div data-zendesk-anchors="attribution-links-for-ad-networks=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC 01H8GPNM9XTR602BWRBQ5JV8DT=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC attribution-model=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%AA%A8%EB%8D%B8 01H8GPNM9XSKS66F02GZQKK8E8=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%AA%A8%EB%8D%B8 01H8GPNM9XBCVVXZ5HFKQZQ79D=%EC%B0%B8%EA%B3%A0 attribution-link-template=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF 01H8GPNM9XS4JE8B1F6TJGKSBR=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%85%9C%ED%94%8C%EB%A6%BF recommended-minimum-attribution-link-parameters=%EA%B6%8C%EC%9E%A5-%EC%B5%9C%EC%86%8C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 01H8GPNM9XD0GASJ93PNDGMDE8=%EA%B6%8C%EC%9E%A5-%EC%B5%9C%EC%86%8C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0" />
