---
title: 에이전시 계정 소개
metadata:
  keywords:
    - In-App Events
    - Agency Account
    - ROI
    - Agency
    - FMP
    - Advertisers
    - Agencies
    - Listed Agency
    - all installs
    - all launches
    - Partners
    - agency sign up
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2013-12-08T10:02:42Z'
  edited_at: '2026-10-14T10:26:48Z'
  id: 207034106
  locale: ko
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/ko/articles/207034106
---
> **한눈에 보기:** 고급 설정을 통해 귀사의 앱스플라이어 에이전시 계정을 최대한 활용하세요.

<div id="about-agency-accounts" />

## 에이전시 계정 소개

에이전시 계정은 에이전시 팀이 마케터 고객(앱 소유자)을 대신하여 에이전시에서 앱 마케팅 캠페인을 실행하고 측정하는 데 사용됩니다.

* 주요 사전 인스톨 및 앱 설치 후 지표를 사용하여 에이전시가 고객 포트폴리오 전체에 걸쳐 최적의 성과를 제공하는지 확인할 수 있습니다.
* 에이전시 계정 대시보드는 마케터 대시보드와 유사한 기능과 콘텐츠를 제공합니다. 여기에는 다음 대시보드가 포함됩니다.
  * 유저 생애 가치 개요
  * 인앱 이벤트
  * 리타겟팅
* 사용 가능한 KPI에는 노출 수, 클릭 수, 인스톨, 사용자 충성도, 비용, ROI (투자수익률) 등이 있습니다. <Anchor target="_blank" href="/marketers/ko/docs/getting-started-with-appsflyer-dashboards">대시보드 소개</Anchor>

<div id="agency-access-to-marketer-data" />

### 마케터 데이터에 대한 에이전시 액세스

에이전시는 항상 에이전시에 어트리뷰트된 트래픽 데이터에 액세스할 수 있습니다. 마케터는 에이전시에 추가 데이터(예: 오가닉 통합 데이터)에 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">액세스 권한을 부여할 수 있습니다</Anchor>. <Anchor target="_blank" href="/marketers/ko/docs/manage-data-access-permissions">사용자 유형에 따른 데이터 액세스</Anchor>를 참조하세요.

<div id="agency-access-to-ad-network-integrations" />

### 애드 네트워크 연동에 대한 에이전시 액세스

애드 네트워크 연동에 액세스하고 캠페인을 측정하려면 애드 네트워크에서 에이전시가 사전 승인을 받아야 합니다. 이는 귀사의 에이전시 ID (af\_prt)를 애드 네트워크의 승인된 에이전시 목록에 포함시켜야 합니다. 파트너에게 연락하여 귀사의 에이전시가 목록에 포함되어 있는지 확인하세요. [여기](/docs/about-agency-accounts#af_prt-매개변수)에서 에이전시 ID 찾는 방법을 확인하세요.

<div id="note" />

> 📘 **참고사항**
>
> * 어트리뷰션 링크의 빈 af\_prt 파라미터에도 적용됩니다.
> * 이는 <Anchor target="_blank" href="/marketers/ko/docs/self-reporting-networks-srns">SRN</Anchor>과 협력하는 에이전시에는 적용되지 않습니다.

<div id="agency-transparency" />

### 에이전시 투명성

에이전시 트래픽은 기본적으로 투명하게 설정됩니다. <Anchor target="_blank" href="/partners/ko/docs/getting-started-agency-onboarding#투명성">더 알아보기</Anchor>

<div id="comparing-different-types-of-accounts" />

## 다양한 계정 유형 비교

<div id="agency-versus-marketer-accounts" />

<Accordion title="에이전시 계정과 마케터 계정">

* **마케터 계정**은 앱 및 데이터 소유자에게 서비스를 제공하는 데 중점을 둡니다. 마케터는 계정에 앱을 추가하고 데이터 액세스 권한을 설정합니다.
* **에이전시 계정**은 에이전시 팀을 위해 특별히 제작되었습니다. 여기에는 고객 포트폴리오 전반에 걸친 마케팅 캠페인을 효율적으로 측정하고 분석할 수 있는 도구가 포함됩니다.

계정 구조를 통해 글로벌 에이전시 팀 간에 지식을 공유할 수 있으며 그룹 수준의 ROI(투자수익률) 측정, 계산, 리포팅 및 최적화가 가능합니다.

<div id="differences-between-marketer-and-agency-accounts" />

#### 마케터 계정과 에이전시 계정의 차이점

|  | 마케터 | **에이전시** |
| --- | --- | --- |
| 코드 수준 구현 | 예 | 아니요; 앱 홍보만 |
| 계정 수준 설정 | 팀 멤버, 팀 멤버 권한, 설정, 결제 환경 설정 | 에이전시 팀 멤버 및 해당 권한 |
| 앱 수준 설정 | 리어트리뷰션 윈도우, 원링크 설정, 시간대, 통화 | 다른 모든 설정은 마케터가 정한 설정에 따릅니다. |
| 연동 파트너 수준 설정 | <ul><li>에이전시 권한</li><li>모든 비(非) SRN (어트리뷰션 링크 기반 광고 네트워크) 설정</li><li>SRN 설정</li><li>링크 관리</li></ul> | <ul><li>모든 비(非) SRN 설정</li><li>마케터 측의 최소 개입으로도 설정 가능한 일부 SRN:</li></ul><ul><li>Google 더블클릭<ul><li>스냅챗</li><li>텐센트</li></ul></li></ul>다른 SRN은 에이전시가 사용하려면 마케터가 설정해야 합니다.<ul><li>링크 관리(마케터가 정의한 템플릿 사용)</li></ul> |
| 추가 기능 | 예(일부, 구독 플랜의 일부인 경우) | 마케터 구독 및 에이전시에 부여된 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">권한</Anchor>에 따라(아래 표 참조) |

<div id="features-available-to-agencies" />

### 에이전시에 제공되는 기능

| 기본적으로 사용 가능 | 사용 불가 | 마케터 권한 필수 |
| --- | --- | --- |
| <ul><li>라이프타임 가치 개요 대시보드</li><li>인앱 이벤트 대시보드</li><li>리타겟팅 대시보드</li><li>활성화된 연동</li><li><Anchor target="_blank" href="/partners/ko/docs/getting-started-agency-onboarding#에이전시를-위한-ssot단일진성공급원">SSOT 대시보드</Anchor>\*\*</li></ul>\*\* 마케터가 이 옵션을 활성화한 후에만 사용 가능 | <ul><li>액티비티 대시보드</li><li>커스텀 대시보드</li><li>사람 중심 분석</li><li>오디언스</li><li>피벗 리포트</li><li>Push API</li><li>데이터 락커</li></ul>*코호트 리포트만 마케터의 허락을 받아 사용할 수 있습니다. | <ul><li>리텐션 리포트</li><li>코호트 대시보드 리포트</li><li><Anchor target="_blank" href="/partners/ko/docs/data-locker-reports-for-agencies">데이터 락커의 코호트 리포트</Anchor></li><li>Protect360</li><li>로데이터 내보내기</li><li>집계된 오가닉 데이터</li><li>Pull API</li></ul> |

</Accordion>

<div id="agency-vs-ad-network-account" />

<Accordion title="에이전시 vs. 애드 네트워크 계정">

<div id="differences-between-ad-network-and-agency-accounts" />

#### 광고 네트워크 계정과 에이전시 계정의 차이점

<table><thead><tr><th>애드 네트워크</th><th>에이전시</th></tr></thead><tbody><tr><td>식별을 위한 어트리뷰션 링크 매개변수: <code>pid</code> </td><td>식별을 위한 어트리뷰션 링크 매개변수: <code>af_prt</code> </td></tr><tr><td>자체 플랫폼에만 앱 광고 배치</td><td>다양한 매체 소스를 통해 앱 홍보</td></tr><tr><td>자체 플랫폼에 게재된 광고로부터의 트래픽만 확인</td><td>광고하는 매체 소스로부터의 트래픽만 확인</td></tr><tr><td>포스트백을 통해 인스톨 및 인앱 이벤트에 대한 실시간 정보를 수신할 수 있음</td><td>포스트백으로 인스톨이나 인앱 이벤트에 대한 실시간 정보를 수신할 수 없음</td></tr><tr><td>자체에서 발생하는 모든 트래픽에 대해 인앱 이벤트 포스트백을 설정할 수 있습니다.\*</td><td>트래픽을 가져오는 일부 파트너에 대해 인앱 이벤트 포스트백을 설정할 수 있습니다.\*</td></tr><tr><td colspan="2">\* 마케터 권한이 필요합니다.</td></tr></tbody></table>

</Accordion>

<div id="important" />

<div id="agency-accountscampaigns-and-reporting" />

## 대행사 계정 - 캠페인 및 리포팅

<div id="agency-setting-up-campaigns" />

<Accordion title="대행사: 캠페인 설정">

대행사는 다음 주요 트래픽 유형을 측정할 수 있습니다.

* * [자체 보고 광고 네트워크 (SRN)](/docs/about-agency-accounts#자체-보고-광고-네트워크)
  * [비 SRN (어트리뷰션 링크를 사용하는 광고 네트워크)](/docs/about-agency-accounts#비-srn)

<div id="self-reporting-ad-networks" />

### 자체 보고 광고 네트워크

Meta Ads, Google Ads, X Ads와 같은 자체 보고 네트워크는 외부 어트리뷰션 링크를 사용하지 않습니다. 대신 각 네트워크는 앱스플라이어가 사용하여 새로운 인스톨, 인앱 이벤트 등을 전달할 수 있는 고유한 메서드와 API를 갖추고 있습니다.

<div id="srn-configurations" />

#### SRN 설정

| SRN | 마케터가 초기 SRN 설정을 진행합니다. | 세부 사항 |
| --- | --- | --- |
| Apple Search Ads | 예 | Apple Search Ads 캠페인에 대한 대행사 구성을 자세히 보려면 <Anchor target="_blank" href="/marketers/ko/docs/apple-ads-integration-setup#configuring-agencies-and-marketing-partners">여기</Anchor>를 클릭하세요. |
| Google Ads | 예 | Google Ads 캠페인에 대한 대행사 구성을 자세히 보려면 <Anchor target="_blank" href="/marketers/ko/docs/google-ads-adwords-integration-setup-for-agencies">여기</Anchor>를 클릭하세요. |
| 구글 마케팅 플랫폼 (GMP) | 아니오 | GMP에는 두 가지 다른 API가 있습니다. <Anchor target="_blank" href="/marketers/ko/docs/google-marketing-platform-display-video-360-dv360-integration#comparing-the-legacy-and-new-integrations">두 가지의 차이점</Anchor>에 대해 더 알아보고 자신에게 맞는 것을 선택하세요. |
| Meta Ads  <br />및  <br />X Ads | 예 | **참고:** 이 섹션은 Meta Ads에 관한 내용입니다. 페이스북 소셜(게시물)에 대한 어트리뷰션은 [온드 미디어](/docs/about-agency-accounts#owned-media%E2%80%94onelink-and-custom-links)에 대해 읽어보세요.<br /><br />**모든 Meta Ads 및 X Ads 캠페인은 에이전시 계정 이름으로 시작하고 그 뒤에 "\_"로 이어져야 합니다.** 이름은 앱스플라이어 플랫폼에서 정의됩니다.<br />잘못된 이름의 캠페인은 마케터에게 표시되지만 대행사 계정에서는 보이지 않습니다.<br /><br />**참고:**<ul><li>대행사 이름은 대소문자를 구분합니다.</li><li><Anchor target="_blank" href="/marketers/ko/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta Ads</Anchor> 및 <Anchor target="_blank" href="/marketers/ko/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor> 설정에 대한 자세한 내용을 대행사에서 확인하세요.</li><li>이에 관한 질문이 있으시면 [agency@appsflyer.com](mailto:agency@appsflyer.com)으로 문의해 주세요.</li></ul>**예시**<br />agencyx는 agencyx\_brilliantcampaign이라는 Meta Ads 캠페인을 실행하며, 이를 확인할 수 있습니다.<br /><br />agencyz는 AgencyZ\_whathaveidonewrong이라는 X Ads 캠페인을 실행하지만, 결과를 볼 수 없습니다. 이는 캠페인의 에이전시 이름 부분이 정의된 에이전시 이름(대문자 A와 Z)과 다르기 때문입니다. |
| 스냅챗 | 아니오 | 스냅챗 캠페인에 대한 에이전시 설정의 세부 사항을 보려면 <Anchor target="_blank" href="/marketers/ko/docs/snapchat-advanced-srn-integration-setup">여기</Anchor>를 클릭하세요. |
| TikTok for Business | 예 | TikTok for Business 캠페인에 대한 에이전시 설정의 자세한 내용을 보시려면 <Anchor target="_blank" href="/marketers/ko/docs/tiktok-for-business-advanced-srn-integration-setup#에이전시를-위한-tiktok-for-business-설정하기">여기</Anchor>를 클릭하세요. |
| 야후 (Oath: 광고 플랫폼 \/ Yahoo Gemini) | 예 | Yahoo 캠페인에 대한 에이전시 설정의 자세한 내용을 보려면 <Anchor target="_blank" href="/marketers/ko/docs/yahoo-integration-setup#agency-configuration">여기</Anchor>를 클릭하세요. |

<div id="non-srns" />

### 비 SRN

SRN과 달리, 대다수의 애드 네트워크는 어트리뷰션 목적으로 어트리뷰션 링크를 사용합니다. <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#attribution-link-tab">이러한 어트리뷰션 링크는 앱스플라이어의 각 네트워크 설정에 이미 제공되어 있으며</Anchor>, 간단히 복사할 수 있습니다.

에이전시의 경우, 그 절차는 마케터와 거의 동일합니다. 일반 애드 네트워크의 설정 기간으로 이동하면 어트리뷰션 링크가 이미 있습니다. 유일한 차이점은 어트리뷰션 링크에 `af_prt` 매개변수가 자동으로 추가된다는 점입니다.

<div id="ad-network-configuration-visibility" />

#### 애드 네트워크 설정 가시성

마케터(앱 소유자)가 설정했을 때만 애드 네트워크 설정이 애드 네트워크에 보여집니다. 에이전시가 애드 네트워크 연동을 활성화하고 구성하면 네트워크에서는 이 섹션이 비활성으로 표시됩니다.

<div id="af_prt-parameter" />

#### af\_prt 매개변수

`af_prt` 매개변수의 값은 에이전시 이름입니다. `af_prt` 매개변수로 에이전시 이름이 전달되면 소문자로 변환됩니다.

어트리뷰션 링크에 귀사의 에이전시 이름이 `af_prt`로 포함될 경우, 신규 인스톨은 귀사의 에이전시 계정으로 측정됩니다. 그렇지 않으면, 새로운 인스톨은 애드 네트워크에 직접 측정됩니다.

[altagency-af-prt.pngalt](https://support.appsflyer.com/hc/article_attachments/30679568792465)

**마케터로부터 받은 링크를 사용하지 마세요**: 잘못된 어트리뷰션을 방지하기 위해 귀사 계정에서 생성한 링크를 사용하세요.

<div id="special-case-all-installs-and-all-launches-networks" />

#### 특별한 경우: 모든 인스톨 및 모든 실행 네트워크

일부 비 SRN에서는 마케터가 **자신에게 측정되지 않은 기기에** 대한 포스트백을 발송하도록 요구하거나 허용합니다.

모든 인스톨 네트워크

네트워크는 모든 소스에서 새 앱 설치에 대한 모든 포스트백을 허용합니다.

모든 실행 네트워크

네트워크는 모든 소스에서 새 앱 실행에 대해 모든 포스트백을 허용합니다.

모든 인스톨 네트워크의 예로는 벙글, Wechat, Startapp, Unity Ads 등이 있습니다.

다음 표는 모든 실행 네트워크의 전체 목록입니다.

| 네트워크 이름 | 네트워크 PID (AF 어트리뷰션 링크) |
| --- | --- |
| Supersonicads (아이언소스의 기존 네트워크) | supersonicads\_int |
| Adelphic Remarketing | adelphicremarketing\_int |
| Grow Mobile | growmobile\_int |
| ONE by AOL | advertising.com\_int |
| Lemmonet Mobile | lemmonetmobile\_int |
| Clickky | clickky\_int |
| Remerge | remerge\_int |
| MyThings | mythings\_int |
| TikTok for Business | bytedanceglobal\_int |

<div id="how-to-setup-agency-attribution-with-all-installslaunches-networks" />

#### 모든 인스톨\/실행 네트워크에서 에이전시 어트리뷰션 설정하는 방법은?

이 네트워크들과 작업하려면 에이전시가 유입시키지 않은 인스톨 정보를 전송해야 합니다. 따라서 이러한 네트워크는 마케터가 **에이전시**보다 먼저 설정해야 합니다.

<div id="example" />

> 📄 **예시**
>
> 탭조이를 사용하여 에이전시 어트리뷰션 설정을 예로 들어 봅시다.
>
> 1. 마케터가 마케터 대시보드의 Tapjoy 설정 창으로 이동합니다.
> 2. 마케터는 Tapjoy가 **마케터**에게 제공한 Tapjoy 앱 ID를 **app\_id** 텍스트 필드에 입력합니다.
> 3. 마케터는 **연동** 탭 > 기본 포스트백에서 **오가닉을 포함한 모든 매체 소스**를 선택합니다.
> 4. 에이전시는 대시보드의 Tapjoy 설정 창으로 이동합니다.
> 5. 에이전시는 Tapjoy가 **에이전시**에 제공한 Tapjoy 앱 ID를 **app\_id** 텍스트 필드에 입력합니다.

<div id="deep-linking" />

### 딥링킹

딥링킹은 맞춤형 콘텐츠를 열거나 앱 내 특정 활동으로 사용자를 보내는 방식으로 모바일 앱을 시작하는 것을 의미합니다. 이를 통해 사용자에게 뛰어난 경험을 제공하고 인게이지먼트를 높일 수 있습니다.

딥링킹이 동작하려면 모바일 앱이 딥링킹 기능과 인프라로 개발되어야 합니다. 캠페인을 설정하기 전에 앱 소유자에게 연락하여 앱이 딥링킹에 적합한지 확인하세요.

<div id="retargeting" />

### 리타겟팅

* * <Anchor target="_blank" href="/marketers/ko/docs/retargeting-attribution-guide">리타겟팅 어트리뷰션</Anchor>을 통해 캠페인에서 기존 또는 이전 사용자를 타겟팅할 수 있습니다. 리타겟팅 캠페인은 올바르게 작동하기 위해 딥링킹 기능이 필요한 경우가 많습니다.

<div id="in-app-events" />

### 인앱 이벤트

앱 소유자는 앱스플라이어에서 기록하고 분석할 수 있는 다양한 이벤트(예: 구매, 튜토리얼 시청, 수준 통과 등)를 앱에서 발생시킬 수 있습니다. 에이전시는 계정의 이벤트 페이지에서 자신에게 어트리뷰션된 이벤트 데이터를 확인할 수 있습니다.

<div id="in-app-event-postbacks" />

#### 인앱 이벤트 포스트백

에이전시는 마케터로부터 권한을 받으면, 광고 네트워크에 <Anchor target="_blank" href="/marketers/ko/docs/in-app-event-postback-configuration">인앱 이벤트 포스트백</Anchor> (<Anchor target="_blank" href="/marketers/ko/docs/measure-sessions">af\_app\_opened 이벤트</Anchor> 포함)를 구성할 수 있습니다.

에이전시는 광고 네트워크에 인앱 포스트백을 직접 구성할 수 있는 권한을 줄 수 있습니다. <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">권한은</Anchor> 마케터가 에이전시 권한 탭에서 부여합니다.

</Accordion>

<div id="reporting-for-agencies" />

<Accordion title="에이전시에 대한 리포팅">

* 트래픽 통계는 앱스플라이어 대시보드에서 직접 보고 다운로드할 수 있습니다.
* 보고서는 앱스플라이어 대시보드의 <Anchor target="_blank" href="/marketers/ko/docs/raw-data-reporting-overview">데이터 내보내기</Anchor> 페이지를 통해 액세스할 수 있습니다. <Anchor target="_blank" href="/partners/ko/docs/data-locker-reports-for-agencies">데이터 락커</Anchor>를 통해서도 코호트 리포트에 액세스할 수 있습니다.
* 다음의 리포트 유형을 사용할 수 있습니다:
  * 집계
  * 로데이터
* 마케터와 에이전시는 대부분 대시보드, 리포트 등에서 동일한 데이터에 액세스할 수 없습니다.
* 에이전시는 일반적으로 마케터의 트래픽 일부에만 책임지므로 에이전시의 데이터 액세스는 마케터의 액세스에 비해 제한적입니다.
* <Anchor target="_blank" href="/marketers/ko/docs/manage-data-access-permissions">이 문서</Anchor>는 이러한 차이점을 설명합니다. 다음 섹션에서 주요 내용을 살펴봅니다.

<div id="note-1" />

> 📘 **참고**
>
> Meta Ads와 X Ads의 서비스 약관에 따라 제3자로 간주되는 **에이전시**는 **Meta Ads 또는 X Ads에서 발생하는 로데이터 리포트 트래픽에 액세스할 수 없습니다**.

<div id="access-to-aggregate-data" />

### 집계된 데이터에 대한 접근

* 성과 보고서는 집계 데이터 보고서라고도 하며, 에이전시 계정에서 기본적으로 제공됩니다. 관련 문서: <Anchor target="_blank" href="/marketers/ko/docs/aggregated-and-analytics-reporting-overview">집계 성과 리포트</Anchor>
* 집계된 오가닉 데이터 리포트에 접근하려면 마케터의 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">권한</Anchor>이 필요합니다.
* 에이전시는 리텐션 및 코호트 리포트와 Protect360 대시보드에 액세스할 수 있습니다. 이를 위해서는 마케터가 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">**리텐션 및 코호트 리포트 접근 허용**</Anchor> 또는 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">**Protect360 대시보드 접근 허용**</Anchor>을 각각 활성화해야 합니다. **권한** 탭에서 **활성화된 연동**을 통해 설정할 수 있습니다.

<div id="access-to-raw-data" />

### 로데이터 접근

<Anchor target="_blank" href="/marketers/ko/docs/raw-data-reporting-overview">로데이터 리포트</Anchor> (사용자 수준 데이터 리포트)는 어트리뷰션 정보를 포함하며 주제별로 구분됩니다.

<div id="time-zone-and-currency" />

### 시간대와 통화

에이전시는 앱에서 정의된 시간대와 통화로 앱을 볼 수 있지만, 이러한 설정은 마케터만이 변경할 수 있습니다.

<div id="cost-reporting" />

### 비용 리포팅

에이전시는 <Anchor target="_blank" href="/marketers/ko/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">비용 데이터를 지원하는</Anchor> 연동 파트너를 구성할 때 **비용 데이터 가져오기**를 활성화할 수 있습니다.

**비용 데이터 가져오기를 활성화하려면:**

1. 앱스플라이어의 사이드 메뉴에서 **협업** > **활성화된 연동**을 선택합니다.
2. 비용으로 파트너를 필터링합니다: **활성화된 연동** 페이지 상단에서 **지원되는 기능** > **비용**을 선택합니다.
3. 파트너를 선택하세요. **연동** 탭으로 이동합니다. **비용** 탭으로 이동합니다.
4. **비용 데이터 가져오기**를 켜세요.
5. 해당 파트너의 API 키를 입력하세요.
6. **저장**을 클릭하세요.

<div id="accessing-and-viewing-cost-data" />

#### 비용 데이터 액세스 및 보기

에이전시는 다음 데이터 소스를 통해 비용 데이터를 확인할 수 있습니다.

* **개요** 페이지: 비용 데이터는 개요 페이지의 **데이터 집약형 성과 리포트**에서 확인할 수 있습니다.
* **리포트**: 비용 데이터는 **설치**(**로데이터 리포트**) 및 **파트너 (매체 소스)**(**성과 리포트**) 같은 내보낸 리포트에서 확인할 수 있습니다.

<div id="hybrid-account-data-access" />

### 하이브리드 계정 데이터 액세스

하이브리드 계정은 일부 앱을 에이전시(앱 파트너)로, 일부를 마케터(앱 소유주)로 관리하는 에이전시 계정입니다.

다음 계정 수준 기능은 사용하기에 제약이 있습니다.

* <Anchor target="_blank" href="/marketers/ko/docs/custom-dashboards">커스텀 대시보드</Anchor>: 에이전시와 하이브리드 계정에서는 사용할 수 없습니다.
* 코호트 리포트: 마케터의 허가 하에 가능합니다.
* Protect360: 마케터의 허가 하에 사용 가능합니다.

하이브리드 계정을 사용하는 경우, 대시보드에 보일 수 있지만, 열려 하면 404 오류가 발생할 수 있습니다.

이 기능들을 사용하려면, 새로운 마케터 계정을 개설하고, 귀사의 마케터 앱과 에이전시 앱을 분리하는 것이 권장됩니다. 위에서 언급된 기능들은 귀사의 마케터 계정에서 활성화되어 있다면 사용 가능합니다.

</Accordion>

<div data-zendesk-anchors="about-agency-accounts=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EA%B3%84%EC%A0%95-%EC%86%8C%EA%B0%9C h_01HDNYNZYR2FTMQ71EV2AY3A3A=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EA%B3%84%EC%A0%95-%EC%86%8C%EA%B0%9C agency-access-to-marketer-data=%EB%A7%88%EC%BC%80%ED%84%B0-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%90-%EB%8C%80%ED%95%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%95%A1%EC%84%B8%EC%8A%A4 h_01HDNYNZYRZKK97GZ6R0MB9RQN=%EB%A7%88%EC%BC%80%ED%84%B0-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%90-%EB%8C%80%ED%95%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%95%A1%EC%84%B8%EC%8A%A4 agency-access-to-ad-network-integrations=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%97%B0%EB%8F%99%EC%97%90-%EB%8C%80%ED%95%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%95%A1%EC%84%B8%EC%8A%A4 h_01J00RYT8J0MBPHTGK5T4WEE43=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%97%B0%EB%8F%99%EC%97%90-%EB%8C%80%ED%95%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%95%A1%EC%84%B8%EC%8A%A4 h_01HJR00RGQX0CQEHDS9BHBGJD4=%EC%B0%B8%EA%B3%A0%EC%82%AC%ED%95%AD agency-transparency=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%ED%88%AC%EB%AA%85%EC%84%B1 h_01HDNYNZYRYHJ98YQWVVENZ07P=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%ED%88%AC%EB%AA%85%EC%84%B1 comparing-different-types-of-accounts=%EB%8B%A4%EC%96%91%ED%95%9C-%EA%B3%84%EC%A0%95-%EC%9C%A0%ED%98%95-%EB%B9%84%EA%B5%90 h_01HDNYNZYR65409AGM9F2PZRC8=%EB%8B%A4%EC%96%91%ED%95%9C-%EA%B3%84%EC%A0%95-%EC%9C%A0%ED%98%95-%EB%B9%84%EA%B5%90 h_01HDNYNZYS7A2H60EEAJ114VSM=agency-versus-marketer-accounts differences-between-marketer-and-agency-accounts=%EB%A7%88%EC%BC%80%ED%84%B0-%EA%B3%84%EC%A0%95%EA%B3%BC-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EA%B3%84%EC%A0%95%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90 h_01HDNYNZYSS7WSQ07S7KRADN7Z=%EB%A7%88%EC%BC%80%ED%84%B0-%EA%B3%84%EC%A0%95%EA%B3%BC-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EA%B3%84%EC%A0%95%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90 features-available-to-agencies=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EC%97%90-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EA%B8%B0%EB%8A%A5 h_01HDNYNZYSX4WPQKS0H6JN6FCP=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EC%97%90-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EA%B8%B0%EB%8A%A5 h_01HDNYNZYS8KRSPM5CPVJEJ74Y=agency-vs-ad-network-account differences-between-ad-network-and-agency-accounts=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EA%B3%84%EC%A0%95%EA%B3%BC-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EA%B3%84%EC%A0%95%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90 h_01HDNYNZYS4VPZMY34WA3SG5JT=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EA%B3%84%EC%A0%95%EA%B3%BC-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EA%B3%84%EC%A0%95%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90 agency-accounts%E2%80%94campaigns-and-reporting=%EB%8C%80%ED%96%89%EC%82%AC-%EA%B3%84%EC%A0%95---%EC%BA%A0%ED%8E%98%EC%9D%B8-%EB%B0%8F-%EB%A6%AC%ED%8F%AC%ED%8C%85 h_01HDNYNZYS32SNR5F0WKJ4G9Q1=%EB%8C%80%ED%96%89%EC%82%AC-%EA%B3%84%EC%A0%95---%EC%BA%A0%ED%8E%98%EC%9D%B8-%EB%B0%8F-%EB%A6%AC%ED%8F%AC%ED%8C%85 h_01HDNYNZYSNF2RQ3E7PM4HK433=agency-setting-up-campaigns selfreporting-ad-networks=%EC%9E%90%EC%B2%B4-%EB%B3%B4%EA%B3%A0-%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC h_01HDNYNZYS8X1VA4T46DQYQZFE=%EC%9E%90%EC%B2%B4-%EB%B3%B4%EA%B3%A0-%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC srn-configurations=srn-%EC%84%A4%EC%A0%95 h_01HDNYNZYS8AM2MFPRXFA4JXNS=srn-%EC%84%A4%EC%A0%95 h_01HDNYNZYSFXZXR99T6ME2R43F=%EC%98%88%EC%8B%9C nonsrns=%EB%B9%84-srn h_01HDNYNZYSN28VZQKCBRGXAVY0=%EB%B9%84-srn ad-network-configuration-visibility=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%84%A4%EC%A0%95-%EA%B0%80%EC%8B%9C%EC%84%B1 h_01HDNYNZYSG5MQDDKV55HF4X9C=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%84%A4%EC%A0%95-%EA%B0%80%EC%8B%9C%EC%84%B1 af_prt-parameter=af_prt-%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98 h_01HDNYNZYSC7XNJCJ1F27KTM9Z=af_prt-%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98 special-case-allinstalls-and-alllaunches-networks=%ED%8A%B9%EB%B3%84%ED%95%9C-%EA%B2%BD%EC%9A%B0-%EB%AA%A8%EB%93%A0-%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EB%AA%A8%EB%93%A0-%EC%8B%A4%ED%96%89-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC h_01HDNYNZYSB4MKXD47E1VHDN62=%ED%8A%B9%EB%B3%84%ED%95%9C-%EA%B2%BD%EC%9A%B0-%EB%AA%A8%EB%93%A0-%EC%9D%B8%EC%8A%A4%ED%86%A8-%EB%B0%8F-%EB%AA%A8%EB%93%A0-%EC%8B%A4%ED%96%89-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC how-to-setup-agency-attribution-with-all-installslaunches-networks=%EB%AA%A8%EB%93%A0-%EC%9D%B8%EC%8A%A4%ED%86%A8%EC%8B%A4%ED%96%89-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%97%90%EC%84%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EC%84%A4%EC%A0%95%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%80 h_01HDNYNZYSHNV2B27JQV4EEVFM=%EB%AA%A8%EB%93%A0-%EC%9D%B8%EC%8A%A4%ED%86%A8%EC%8B%A4%ED%96%89-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%97%90%EC%84%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EC%84%A4%EC%A0%95%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%80 h_01HDNYNZYS5WYADGW24AVK9RCZ=%EC%98%88%EC%8B%9C deep-linking=%EB%94%A5%EB%A7%81%ED%82%B9 h_01HDNYNZYS5W0SMCF1YC6C3G4C=%EB%94%A5%EB%A7%81%ED%82%B9 retargeting=%EB%A6%AC%ED%83%80%EA%B2%9F%ED%8C%85 h_01HDNYNZYS3Z7RE51M7G7386VZ=%EB%A6%AC%ED%83%80%EA%B2%9F%ED%8C%85 inapp-events=%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8 h_01HDNYNZYTDFN4MB6QBEQ8P5XW=%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8 inapp-event-postbacks=%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HMDP38S3NPE5R4QZJ5CW404W=%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01HDNYNZYTA767NGSTNECTBCV2=reporting-for-agencies h_01HDNYNZYTYBWGMY2PP8MPQE2F=%EC%B0%B8%EA%B3%A0 access-to-performance-reports=%EC%A7%91%EA%B3%84%EB%90%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%91%EA%B7%BC h_01HDNYNZYTDH4S38XG3JCZQYJJ=%EC%A7%91%EA%B3%84%EB%90%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%91%EA%B7%BC access-to-raw-data=%EB%A1%9C%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%91%EA%B7%BC h_01HDNYNZYT4ZKBNGDR3QR1VTEZ=%EB%A1%9C%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%91%EA%B7%BC time-zone-and-currency=%EC%8B%9C%EA%B0%84%EB%8C%80%EC%99%80-%ED%86%B5%ED%99%94 h_01HDNYNZYT97ET1TQHKSRDMWDC=%EC%8B%9C%EA%B0%84%EB%8C%80%EC%99%80-%ED%86%B5%ED%99%94 cost-reporting=%EB%B9%84%EC%9A%A9-%EB%A6%AC%ED%8F%AC%ED%8C%85 h_01HDNYNZYTYT9NHMHQQ77PK8CQ=%EB%B9%84%EC%9A%A9-%EB%A6%AC%ED%8F%AC%ED%8C%85 accessing-and-viewing-cost-data=%EB%B9%84%EC%9A%A9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%95%A1%EC%84%B8%EC%8A%A4-%EB%B0%8F-%EB%B3%B4%EA%B8%B0 h_01HDNYNZYTWB5WVYY8C347G1ME=%EB%B9%84%EC%9A%A9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%95%A1%EC%84%B8%EC%8A%A4-%EB%B0%8F-%EB%B3%B4%EA%B8%B0 hybrid-account-data-access=%ED%95%98%EC%9D%B4%EB%B8%8C%EB%A6%AC%EB%93%9C-%EA%B3%84%EC%A0%95-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%95%A1%EC%84%B8%EC%8A%A4 h_01HDNYNZYTKZTCBSBKZEJ7M0JN=%ED%95%98%EC%9D%B4%EB%B8%8C%EB%A6%AC%EB%93%9C-%EA%B3%84%EC%A0%95-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%95%A1%EC%84%B8%EC%8A%A4" />
