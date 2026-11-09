---
title: 시작하기—에이전시 온보딩
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
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
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2026-10-14T10:34:52Z'
  id: 360002381617
  locale: ko
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/ko/articles/360002381617
---
> **요약: 요약: 에이전시 계정을 설정하여 고객의 캠페인 측정을 시작합니다.**

<Embed title="시작하기—에이전시 온보딩" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/54qzpj1lm7" providerUrl="https://fast.wistia.com" />

<div id="appsflyer-attribution-model" />

## 앱스플라이어 어트리뷰션 모델

진행하기 전에 앱스플라이어의 어트리뷰션 작업 방식을 이해하는 것이 필수입니다. 이 섹션에서는 첫 번째 클릭 또는 광고 노출로부터 인스톨 또는 이벤트의 어트리뷰션, 그리고 그 이후까지 이르는 길을 따라 발생하는 상황에 대해 설명합니다.

<Image align="center" alt="ua-agency-flow.png" src="https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png" />

1. 마케터 또는 마케터를 대신하는 에이전시는 앱스플라이어 어트리뷰선 링크를 사용하여 특정 광고 네트워크를 통한 캠페인을 설정합니다.
2. 사용자가 자신의 광고, 예를 들어, 배너 또는 오퍼 링크 중 하나를 클릭합니다.
3. 그러면 광고에 연결된 앱스플라이어 어트리뷰션 링크는 클릭 시 수집된 정보로 채워집니다. 앱스플라이어는 어트리뷰션 링크에서 정보를 수집해 데이터베이스에 저장합니다.
4. 유저는 앱 스토어로 리디렉션됩니다.
5. 사용자가 앱을 설치하고 처음으로 앱을 실행합니다. 앱 내의 앱스플라이어 SDK가 앱이 설치된 디바이스에 대한 정보를 앱스플라이어 서버에 전송합니다.
6. 앱스플라이어는 <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-attribution-model">어트리뷰션 방법</Anchor>을 사용하여 이 데이터를 앱스플라이어 클릭 데이터베이스와 매칭합니다.
7. 일치하는 항목을 찾으면, 인스톨을 클릭에 어트리뷰션합니다. 일치하는 항목이 없으면, 인스톨을 오가닉 다운로드로 어트리뷰션합니다.
8. 인스톨이 어트리뷰트되면 마케터 및 에이전시의 대시보드와 리포트(<Anchor target="_blank" href="/partners/ko/docs/about-agency-accounts#자체-보고-광고-네트워크">Facebook 및 X Ads 제외</Anchor>)에 이를 표시합니다.
9. 그런 다음 전환 세부 정보가 포함된 포스트백을 광고 네트워크로 전송하면 이 정보를 추가적인 최적화에 사용할 수 있습니다.

<div id="agency-role-in-mobile-attribution-chain" />

## 모바일 어트리뷰션 체인에서 에이전시의 역할

앱을 소유한 마케터는 앱스플라이어 SDK를 체인에 통합하여 마케팅 노력을 정량화합니다.

일부 앱 소유자는 마케팅 에이전시를 고용하여 광고 캠페인을 대신 운영하기로 선택합니다. 그렇게 하려면 에이전시는 앱스플라이어 계정을 가지고 있어야 하며, 마케터는 에이전시에 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">앱에 대한 액세스 권한</Anchor>을 부여해야 합니다.

따라서 에이전시는 기술적으로 앱을 소유하는 것이 아니라 SDK 통합과 같은 기술적인 관여 없이 작동하는 마케팅 채널에서 앱을 홍보만 합니다. 마케터가 부여한 권한 설정에 따라 에이전시는 다양한 기능을 제어할 수 있습니다.

에이전시가 게시한 광고에 인스톨이 어트리뷰트되는 경우 에이전시의 대시보드에 표시됩니다. 앱 소유자도 이를 볼 수 있으며, 해당 앱이 에이전시가 어트리뷰트한 것임을 알 수 있습니다.

일러두기: 만약 조직이 앱을 소유하고 있거나, 앱의 마케팅뿐만 아니라 개발도 취급한다면, 마케터 계정을 개설해야 합니다.

<div id="pricing" />

## 과금 체계

에이전시 계정 기능의 범위는 각 앱에 대해 앱 소유자가 제공하는 권한에 따라 달라집니다. 따라서 에이전시 계정은 **무료로** 제공되며 앱 소유자에게만 어트리뷰션 요금이 부과됩니다. 앱 소유자 및 에이전시는 보상 목적으로 앱스플라이어 어트리뷰션 데이터를 사용할 수 있습니다.

<div id="getting-started" />

## 시작하기

새 에이전시 계정 설정 방법:

1. <Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">등록 양식</Anchor>을 작성합니다.
   * 회사 이메일 도메인을 사용하여 등록합니다.
   * 기존 앱스플라이어 계정과 연결되지 않은 이메일 주소를 사용합니다.
2. 앱스플라이어 에이전시 팀의 팀원이 등록을 완료하는 데 필요한 추가 정보를 문의할 수 있습니다.
3. 계정이 활성화되면 알림을 받게 되며 그러면 앱스플라이어를 사용하기 시작할 수 있습니다.

<div id="adding-team-members" />

## 팀원 추가

계정이 개설되어 실행되면 계정 관리자(계정을 개설한 자)는 에이전시에서 관리하는 앱의 일부 또는 전체에 액세스할 수 있는 팀원을 추가할 수 있습니다. 새 팀원을 추가하는 자세한 방법은 여기를 클릭하세요.

<div id="adding-apps-to-your-account" />

## 앱을 계정에 추가하기

계정을 처음 생성했을 때는 이 계정과 연관된 앱이 없습니다.

<Image align="center" alt="agency-start.png" src="https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png" />

에이전시의 개인 또는 팀은 앱 소유자에게 다음 권한을 요구합니다.

* 앱 대시보드에 대한 액세스 권한
* 설정 변경 권한
* 캠페인 실행 권한

마케터는 플랫폼에서 직접 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#에이전시-권한">에이전시에 액세스 권한을 부여합니다</Anchor>. 계정을 설정하고 앱에 액세스할 수 있게 되면 앱스플라이어 기능을 사용하여 캠페인 실행을 시작할 수 있습니다.

<div id="note" />

<div id="what-does-it-mean-to-get-permission-from-a-marketer" />

### 이것은 마케터로부터 권한을 부여받는다는 것을 의미합니다.

마케터로부터 권한을 부여받는 방법:

* 앱이 계정에 표시됩니다.
* 앱에 대해 광고 네트워크와의 연동을 설정할 수 있습니다(앱 소유자가 설정해야 할 일부 네트워크는 예외).
* 캠페인에 사용할 어트리뷰션 링크를 만들 수 있습니다.
* (이를 허용하는) 파트너와의 비용 연동을 설정할 수 있습니다.
* 앱 데이터를 볼 수 있습니다.
* 광고 네트워크 및 해당 팀원에게 앱에 대한 기본 정보를 볼 수 있는 권한을 부여할 수 있습니다.  
  즉, 에이전시와 마케터가 광고 네트워크로 작업할 때, 두 사람 모두 광고 네트워크 팀 구성원의 권한을 편집하여 앱 대시보드를 보고 서로가 변경한 내용을 볼 수 있습니다. 따라서 예를 들어 추가하지 않은 새 광고 네트워크 팀 구성원이나 제거하지 않은 팀 구성원이 없는 경우 마케터가 추가하거나 제거할 수 있습니다.

추가 권한으로는 코호트 리포트, Protect360 대시보드 및 오가닉 데이터 집계 등이 있습니다.

<div id="app-list" />

### 앱 목록

마케터로부터 권한을 받으면 앱이 앱 페이지에 나타납니다.

계정의 앱 페이지는 최대 1000 개의 앱을 나열합니다. 권한이 있는 앱 목록이 1,000을 초과하면 일부 앱이 목록에 표시되지 않습니다. 검색을 사용하면 여전히 찾을 수는 있습니다.

<Image align="center" alt="agency-apps.png" src="https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png" />

<div id="searching-for-apps" />

#### 앱 검색하기

1. 계정의 상단 메뉴에서 **나의 앱**을 선택합니다.
2. 검색 필드에 검색어를 입력합니다. 예를 들면 다음과 같습니다.
   * 앱 이름
   * 앱 ID
   * 앱 소유주 이메일

### 투명성

업계가 보다 투명한 생태계로 이동함에 따라 앱스플라이어는 광고주와 에이전시 간의 투명성을 지원하여 앱스플라이어 리포트와 분석 제품을 최대한 활용할 수 있도록 지원합니다.

참고:

<div id="agency-dashboard" />

## 에이전시 대시보드

앱 목록에서 원하는 앱을 클릭하여 앱의 <Anchor target="_blank" href="/marketers/ko/docs/getting-started-with-appsflyer-dashboards">대시보드</Anchor>에 액세스합니다. 캠페인 실행을 시작하면 어트리뷰트된 집계 데이터가 여기에 표시됩니다.

<Image align="center" alt="agency-dashboard.png" src="https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png" />

에이전시 계정 대시보드에는 다음 항목에 대한 기본 액세스 권한이 포함되어 있습니다.

* 라이프타임 가치 개요 대시보드
* 인앱 이벤트 대시보드
* 리타겟팅 대시보드

<div id="running-campaigns" />

## 캠페인 실행

<div id="self-reporting-networks-srns" />

### 셀프 리포팅 네트워크(SRN)

셀프 어트리뷰팅 네트워크(SAN)라고도 하는 SRN은 클릭 및 기타 데이터를 보고하기 위해 앱스플라이어의 어트리뷰션 링크가 필요하지 않고 대신 앱스플라이어와의 직접 통합을 사용하는 네트워크입니다. 이러한 네트워크 중에는 <Anchor target="_blank" href="/marketers/ko/docs/meta-ads-faq#attributing-agencies-with-facebook">메타 광고</Anchor>, <Anchor target="_blank" href="/marketers/ko/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor>, <Anchor target="_blank" href="/marketers/ko/docs/google-ads-adwords-integration-setup-for-agencies">구글 광고</Anchor>, <Anchor target="_blank" href="/marketers/ko/docs/snapchat-advanced-srn-integration-setup">스냅챗</Anchor>, 더블클릭, <Anchor target="_blank" href="/marketers/ko/docs/apple-ads-integration-setup">애플 광고 검색</Anchor>, 야후 및 <Anchor target="_blank" href="/marketers/ko/docs/yahoo-integration-setup">야후</Anchor> <Anchor target="_blank" href="/marketers/ko/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">재팬</Anchor>이 있습니다. 일본

이러한 네트워크는 대부분 에이전시를 위한 특별한 설정이 필요합니다. 예를 들어, Facebook과 X Ads의 연동은 앱 소유자만 설정할 수 있으므로, 에이전시 캠페인 이름은 해당 에이전시의 이름으로 시작해야 인스톨이 최종적으로 해당 에이전트에 올바르게 어트리뷰트되는지 확인할 수 있습니다.

위의 링크를 클릭하여 네트워크 가이드와 에이전트 설정에 대한 특정 지침을 읽어보십시오.

<div id="non-srns" />

### 비 SRN

대부분의 광고 네트워크에는 광고 뒤에 배치되는 어트리뷰션 링크가 필요합니다. <Anchor target="_blank" href="/partners/ko/docs/about-agency-accounts#비-srn">여기</Anchor>에서 그것을 통해 캠페인을 실행하는 방법에 대해 자세히 알아보십시오.


<span id="sandbox-attribution-agency-campaigns"></span>Apple은 SKAdNetwork 어트리뷰션 프로세스의 일부로 에이전시를 포함하지 않고 앱스플라이어는 에이전시를 직접 어트리뷰션할 수 없지만 앱스플라이어는 여전히 SKAdNetworks에서 실행되는 에이전시 캠페인에 대한 어트리뷰션 데이터를 제공할 수 있습니다.

<div id="campaign-naming" />

#### 캠페인 이름 지정

* af\_prt(<Anchor target="_blank" href="/partners/ko/docs/about-agency-accounts#af_prt-매개변수">af\_prt가 무엇이고 찾을 수 있는 장소</Anchor>),
* 밑줄,
* 에이전시의 이름 지정 규칙을 따르는 실제 캠페인 이름.

예를 들어, af\_prt가 AgencyX인 경우 캠페인 이름은 다음과 같을 수 있습니다.

`AgencyX_SummerSale`

<div id="skadnetwork-agency-campaigns" />

### SKAdNetwork 에이전시 캠페인

Apple iOS의 일부인 SKAdNetwork 인프라를 사용하여 마케터는 IDFA나 광고 ID 없이 캠페인 성공을 측정할 수 있습니다. Apple은 SKAdNetwork 어트리뷰션 프로세스의 일부로 에이전시를 포함하지 않고 앱스플라이어는 에이전시를 직접 어트리뷰션할 수 없지만 앱스플라이어는 여전히 SKAdNetworks에서 실행되는 에이전시 캠페인에 대한 어트리뷰션 데이터를 제공할 수 있습니다.

<div id="campaign-naming-1" />

#### 캠페인 이름 지정

앱스플라이어 SKAdNetwork 대시보드에서 캠페인을 보려면 SKAdNetwork를 사용하여 설정하는 캠페인 이름에 파트너 식별자를 포함해야 하며 다음과 같이 구성해야 합니다.

* af\_prt(<Anchor target="_blank" href="/partners/ko/docs/about-agency-accounts#af_prt-매개변수">af\_prt가 무엇이고 찾을 수 있는 장소</Anchor>),
* 밑줄,
* 에이전시의 이름 지정 규칙을 따르는 실제 캠페인 이름.

예를 들어, af\_prt가 AgencyX인 경우 캠페인 이름은 다음과 같을 수 있습니다.

`AgencyX_SummerSale`

<div id="note-2" />

<div id="note-1" />

> 📘 **참고**
>
> * SKAdNetwork의 에이전시 캠페인은 항상 투명하며 캠페인을 실행하는 광고 네트워크의 ID는 마케터로부터 숨겨지지 않습니다. iOS 15부터는 마케터(앱 소유자)가 <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">포스트백 복사본을 직접 수신하도록 선택</Anchor>할 수 있습니다.
> * 이 요청은 사용자 인터페이스에서 액세스할 수 있는 파트너 활성화 설정에 추가됩니다.

<div id="access-to-skan-conversion-studio" />

#### SKAN Conversion Studio 액세스

에이전시는 <Anchor target="_blank" href="/marketers/ko/docs/skan-conversion-studio#view-cv-mapping">Conversion Studio</Anchor>에서 마케터의 SKAN CV 매핑 구성을 <Anchor target="_blank" href="/marketers/ko/docs/skan-conversion-studio#skan-conversion-studio-basics">보고 다운로드</Anchor> 할 수 있지만 설정을 구성하거나 수정할 수는 없습니다 .

<div id="skadnetwork-dashboard" />

#### SKAdNetwork 대시보드

<Embed title="시작하기—에이전시 온보딩" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**더 읽어보기:**

* <Anchor target="_blank" href="/marketers/ko/docs/about-att-and-skan">SKAdNetwork 빠른 시작 가이드</Anchor>
* <Anchor target="_blank" href="/marketers/ko/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAdNetwork 대시보드</Anchor>
* <Anchor target="_blank" href="/marketers/ko/docs/skadnetwork-skan-solution-guide">SKAdNetwork 솔루션</Anchor>

<div id="single-source-of-truth-ssot-for-agencies" />

### 에이전시를 위한 SSOT(단일진성공급원)

SSOT는 서로 다른 모델의 어트리뷰션 데이터를 결합하고 중복 인스톨과 관련 비용 및 수익 관련 지표를 제거하여 모든 어트리뷰션 방법을 통합합니다. 이렇게 하면 예를 들어 eCPI, ROI 및 ROAS가 올바르게 계산됩니다.

에이전시는 개요 대시보드에서 SSOT 데이터에 액세스할 수 있지만 API를 통해서는 액세스할 수 없습니다.

개요 대시보드에 SSOT 플래그를 포함하려면 마케터가 Conversion Studio에서 SSOT를 설정해야 합니다.

**더 읽어보기:**

* <Anchor target="_blank" href="/marketers/ko/docs/single-source-of-truth-ssot-guide-for-ios-attribution">iOS 어트리뷰션을 위한 Single Source of Truth (SSOT) 가이드</Anchor>

<div id="what-else-you-can-do" />

## 할 수 있는 다른 작업

* 사용자 리텐션 측정
* 인앱 이벤트를 사용하여 캠페인 최적화
* <Anchor target="_blank" href="/marketers/ko/docs/retargeting-attribution-guide">리타게팅</Anchor> 캠페인 실행
* <Anchor target="_blank" href="/marketers/ko/docs/manage-data-access-permissions">데이터</Anchor> 내보내기
* <Anchor target="_blank" href="/marketers/ko/docs/registering-test-devices">테스트 기기 등록</Anchor>
* 그리고 더 많은 내용.

고급 에이전시 계정 사용에 대한 자세한 내용은 <Anchor target="_blank" href="/partners/ko/docs/about-agency-accounts#agency-setting-up-campaigns">여기</Anchor>에서 확인할 수 있습니다.

생소한 용어를 우연히 발견했습니까? 당사 <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-knowledge-base-glossary">용어 사전</Anchor>에서 찾아보십시오.

긴급한 기술적 질문이 있습니까? 도움말 센터를 찾아보세요. 답을 찾을 수 있습니다. 답이 없는 경우 대시보드의 오른쪽 하단 모서리를 통해 지원 팀에 문의하십시오.

<div data-zendesk-anchors="appsflyer-attribution-model=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%AA%A8%EB%8D%B8 h_01HFXXKCMW7EREMC7KEYTF3ERH=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%AA%A8%EB%8D%B8 agency-role-in-mobile-attribution-chain=%EB%AA%A8%EB%B0%94%EC%9D%BC-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EC%B2%B4%EC%9D%B8%EC%97%90%EC%84%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EC%9D%98-%EC%97%AD%ED%95%A0 h_01HFXXKCMW987FV2PB4EPXH92Z=%EB%AA%A8%EB%B0%94%EC%9D%BC-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EC%B2%B4%EC%9D%B8%EC%97%90%EC%84%9C-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EC%9D%98-%EC%97%AD%ED%95%A0 pricing=%EA%B3%BC%EA%B8%88-%EC%B2%B4%EA%B3%84 h_01HFXXKCMWPN6AN98A5RD5YXW7=%EA%B3%BC%EA%B8%88-%EC%B2%B4%EA%B3%84 getting-started=%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0 h_01HFXXKCMWRXVBYTW9RYEX7X8F=%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0 adding-team-members=%ED%8C%80%EC%9B%90-%EC%B6%94%EA%B0%80 h_01HFXXKCMWB6ZG3PSHDSETC4XC=%ED%8C%80%EC%9B%90-%EC%B6%94%EA%B0%80 adding-apps-to-your-account=%EC%95%B1%EC%9D%84-%EA%B3%84%EC%A0%95%EC%97%90-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0 h_01HFXXKCMWBZVTHAEKED1Q27M3=%EC%95%B1%EC%9D%84-%EA%B3%84%EC%A0%95%EC%97%90-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0 what-does-it-mean-to-get-permission-from-a-marketer=%EC%9D%B4%EA%B2%83%EC%9D%80-%EB%A7%88%EC%BC%80%ED%84%B0%EB%A1%9C%EB%B6%80%ED%84%B0-%EA%B6%8C%ED%95%9C%EC%9D%84-%EB%B6%80%EC%97%AC%EB%B0%9B%EB%8A%94%EB%8B%A4%EB%8A%94-%EA%B2%83%EC%9D%84-%EC%9D%98%EB%AF%B8%ED%95%A9%EB%8B%88%EB%8B%A4 h_01HFXXKCMWYNNZWTKP9KEQ4VCD=%EC%9D%B4%EA%B2%83%EC%9D%80-%EB%A7%88%EC%BC%80%ED%84%B0%EB%A1%9C%EB%B6%80%ED%84%B0-%EA%B6%8C%ED%95%9C%EC%9D%84-%EB%B6%80%EC%97%AC%EB%B0%9B%EB%8A%94%EB%8B%A4%EB%8A%94-%EA%B2%83%EC%9D%84-%EC%9D%98%EB%AF%B8%ED%95%A9%EB%8B%88%EB%8B%A4 app-list=%EC%95%B1-%EB%AA%A9%EB%A1%9D h_01HFXXKCMWKW78TMC76F40PY2C=%EC%95%B1-%EB%AA%A9%EB%A1%9D searching-for-apps=%EC%95%B1-%EA%B2%80%EC%83%89%ED%95%98%EA%B8%B0 h_01HFXXKCMW8S93N577393QZTYX=%EC%95%B1-%EA%B2%80%EC%83%89%ED%95%98%EA%B8%B0 transparency=%ED%88%AC%EB%AA%85%EC%84%B1 h_01HFXXKCMW5YC2APNGHNV6B35C=%ED%88%AC%EB%AA%85%EC%84%B1 agency-dashboard=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C h_01HFXXKCMWPZVADY15DKATJ7Z4=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C running-campaigns=%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%8B%A4%ED%96%89 h_01HFXXKCMWFB9RXY7AVBX5CGB9=%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%8B%A4%ED%96%89 selfreporting-networks-srns=%EC%85%80%ED%94%84-%EB%A6%AC%ED%8F%AC%ED%8C%85-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%ACsrn h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=%EC%85%80%ED%94%84-%EB%A6%AC%ED%8F%AC%ED%8C%85-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%ACsrn nonsrns=%EB%B9%84-srn h_01HFXXKCMWPAMZ373D5AVD5EJF=%EB%B9%84-srn h_01J6PCDYM2W1X6EMMEE7SFB3VE=sandbox-attribution-agency-campaigns campaign-naming=%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%9D%B4%EB%A6%84-%EC%A7%80%EC%A0%95 h_01HFXXKCMWMW1AHXMS19CYD4VC=%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%9D%B4%EB%A6%84-%EC%A7%80%EC%A0%95 h_01HFXXKCMWEQ41A7TZ2K6DE424=%EC%B0%B8%EA%B3%A0 skadnetwork-agency-campaigns=skadnetwork-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%BA%A0%ED%8E%98%EC%9D%B8 h_01HFXXKCMWZ19E0QR1VE977BTS=skadnetwork-%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C-%EC%BA%A0%ED%8E%98%EC%9D%B8 01J6PCG6JGY2R8T5DDCR8APM66=%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%9D%B4%EB%A6%84-%EC%A7%80%EC%A0%95-1 01J6PCG6JHK9TGX93SD4DRP393=%EC%B0%B8%EA%B3%A0 access-to-skan-conversion-studio=skan-conversion-studio-%EC%95%A1%EC%84%B8%EC%8A%A4 h_01HFXXKCMWX53HMRG2ZTD9FYQE=skan-conversion-studio-%EC%95%A1%EC%84%B8%EC%8A%A4 skadnetwork-dashboard=skadnetwork-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C h_01HFXXKCMW1HHMSS3XAXJKME29=skadnetwork-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C single-source-of-truth-ssot-for-agencies=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-ssot%EB%8B%A8%EC%9D%BC%EC%A7%84%EC%84%B1%EA%B3%B5%EA%B8%89%EC%9B%90 h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-ssot%EB%8B%A8%EC%9D%BC%EC%A7%84%EC%84%B1%EA%B3%B5%EA%B8%89%EC%9B%90 what-else-you-can-do=%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8A%94-%EB%8B%A4%EB%A5%B8-%EC%9E%91%EC%97%85 h_01HFXXKCMXQ2JT63GBMC74PWBA=%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8A%94-%EB%8B%A4%EB%A5%B8-%EC%9E%91%EC%97%85" />
