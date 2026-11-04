---
title: 광고 네트워크에 대한 셀프서비스 연동 관리
metadata:
  keywords:
    - postbacks
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
  created_at: '2021-03-15T10:03:41Z'
  edited_at: '2026-10-14T10:39:48Z'
  id: 360018512658
  locale: ko
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ko/articles/360018512658
---
> **간단히 보기**: 요약: 앱스플라이어 대시보드에서 연동을 설정하고 관리합니다.

<Embed title="광고 네트워크에 대한 셀프서비스 연동 관리" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/9kvwrhnzjo" providerUrl="https://fast.wistia.com" />

**선행 조건:**

* 앱스플라이어에 대한 로그인 자격 증명(사용자 이름 및 암호)이 있어야 어트리뷰션 링크 및 포스트백을 관리할 수 있습니다. <Anchor target="_blank" href="/partners/ko/docs/getting-started-onboarding-guide-for-ad-networks">파트너 계정을 생성</Anchor>하려면 앱스플라이어 고객(광고주)에게 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#앱스플라이어에-새로운-파트너-초대">자신을 초대</Anchor>하도록 요청하십시오.
* 어트리뷰션 링크 및 기본 포스트백 관리는 2022년 2월 1일 이후 가입한 파트너에 한해 가능합니다.
* 다음을 준수하여 서버가 포스트백을 수신할 준비가 되었는지 확인하십시오.
  * 방화벽 및 보안 시스템에 앱스플라이어 서버 <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-server-ip-address-ranges-allowlisting">IP 주소</Anchor>를 등록하여 사용자의 엔드포인트와의 통신을 보장합니다.
  * TLS 버전 <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-https-ssl-encryption-policy-support#outgoing-messages-appsflyer-as-client">기재된 암호 포함</Anchor> TLS 1.2 이상.
  * 포트 80, 443

<div id="accessing-integration-management" />

## 연동 관리에 액세스하기

1. 앱스플라이어 파트너 계정에 로그인합니다.
2. 오른쪽 맨 위 드롭다운 메뉴 > **포스트백 관리**를 클릭합니다.

<div id="attribution-link" />

## 어트리뷰션 링크

어트리뷰션 링크는 연동에서 가장 중요한 부분입니다. 어트리뷰션 링크는 앱스플라이어에 광고 인게이지먼트에 대해 알리는 데 사용됩니다. 어트리뷰션 링크는 광고 뒤에 배치되므로 사용자가 광고를 클릭할 때 어트리뷰션 링크를 클릭하게 됩니다.

어트리뷰션 링크 설정 완료는 필수입니다.

**어트리뷰션 링크 설정 방법:**

1. **어트리뷰션 링크** 탭에서 어트리뷰션 링크에 포함할 다음 파라미터를 추가합니다.
   * 파라미터 이름
   * **사용자 매크로**: 파라미터를 값으로 채우는 매크로를 추가합니다.
   * **포함**: 링크에 파라미터를 포함하려면 확인란을 선택합니다.

   <div id="important" />

   > 🚧 **중요!**
   >
   > * 캠페인 및 광고 관련 파라미터를 추가하여 캠페인 성과에 대한 보다 강력한 데이터를 제공할 수 있습니다.
   > * **사이트 ID**는 필수 파라미터입니다.
   > * 광고주는 이 링크를 특정 앱의 연동 기준으로 사용하며 추가 파마미터를 추가할 수 있습니다.
   > * 앱 ID, 기여 기간 및 파트너 ID가 링크에 자동으로 추가되므로 이 템플릿에 추가할 필요가 없습니다.

2. **[선택사항]** 앱스플라이어에서 제공하지 않는 사용자정의 파라미터를 추가합니다.
3. 링크 미리보기를 사용하여 모든 내용이 올바른지 확인합니다.
4. **저장**을 클릭하세요.

<Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">어트리뷰션 링크 및 사용가능한 파라미터에 대해 자세히 알아보십시오</Anchor>.

문제가 있는 경우 <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">파트너 도우미 위젯</Anchor>을 사용하여 문의하세요.

<div id="default-postback" />

## 기본 포스트백

포스트백은 앱스플라이어에서 매크로를 포함하고 전환 후 실시간으로 서버로 전송되는 URL입니다(구성에 따라 네트워크 또는 다른 네트워크에서도).

**기본 포스트백 설정 방법:**

1. **엔드포인트 주소**를 입력하십시오. 포스트백이 전송되는 엔드포인트끝점입니다. 인스톨, 인앱이벤트 또는 둘 다에 대한 해당 URL을 입력합니다. 연동을 활성화하려면 적어도 인스톨 포스트백 URL이 필요합니다.
2. 파라미터를 포스트백에 추가:
   * 파라미터 이름
   * **수신 파라미터**: 사용자가 받는 각각의 수신 파라미터.
   * **파라미터 값**(일부 파라미터에 사용 가능): 값 형식을 선택합니다. 예를 들어, 부울 값의 경우 "true"/"false" 또는 1/0으로 값을 수신할지 여부를 선택합니다.
   * **인스톨**: 인스톨 포스트백에 파라미터를 포함하도록 상자를 선택합니다.
   * **인앱이벤트**: 인앱이벤트 포스트백에 파라미터를 포함하도록 상자를 선택합니다.

   <Anchor target="_blank" href="/partners/ko/docs/postback-macros-for-ad-networks">포스트백 매크로 전체 목록</Anchor>

   <div id="important-1" />

   > 🚧 **중요!**
   >
   > * 합법적인 이벤트에 대한 포스트백과 거부된 포스트백을 구분할 수 있으려면 <Anchor target="_blank" href="/partners/ko/docs/postback-macros-for-ad-networks#macros-installs-inapp-events-and-rejected-events">거부된 포스트백 매크로</Anchor>를 구성하세요.
   > * 거부된 설치/인앱이벤트 포스트백을 활성화하려면 기본 포스트백 템플릿에 다음 매개 변수를 추가하세요.
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`  
   >     **참고:** Advanced Privacy 포스트백이 활성화된 경우 위의 매개 변수를 Advanced Privacy 템플릿에 추가합니다.

4. 포스트백 템플릿 미리보기를 사용하여 모든 것이 올바른지 확인합니다.
5. **저장**을 클릭하세요.

<Anchor target="_blank" href="/marketers/ko/docs/in-app-event-postback-configuration">추가 포스트백 정보 및 예.</Anchor>

문제가 있는 경우 <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">파트너 도우미 위젯</Anchor>을 사용합니다.

<div id="advanced-privacy-and-skan-postbacks" />

## 프라이버시 강화 모드와 SKAN 포스트백

프라이버시 강화 모드 및 SKAN 포스트백은 어트리뷰션 링크와 기본 포스트백을 만든 후에만 설정할 수 있습니다.

**포스트백 관리 방법:**

1. 다음 중 포스트백 유형을 선택합니다.
   * <Anchor target="_blank" href="/partners/ko/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Advanced privacy</Anchor> 포스트백.
   * <Anchor target="_blank" href="/partners/ko/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> 포스트백.
2. 빌더를 활성화합니다.
3. **[SKAdNetwork 포스트백 구성 전용]** SKAdNetwork ID를 입력하십시오. 이 필드는 필수이며 올바른 ID가 없으면 설정을 저장할 수 없습니다.
4. **엔드포인트 주소**를 입력하십시오. 포스트백이 전송되는 엔드포인트끝점입니다. 인스톨, 인앱이벤트 또는 둘 다에 대한 해당 URL을 입력합니다.
5. 포스트백 파라미터 추가:
   * 파라미터 이름
   * 예를 들어, 부울 값의 경우 "true"/"false" 또는 1/0으로 값을 수신할지 여부를 선택합니다.
   * **인스톨**: 인스톨: 인스톨 포스트백에 파라미터를 포함하도록 상자를 선택합니다.
   * **인앱 이벤트**: 인앱이벤트: 인앱이벤트 포스트백에 파라미터를 포함하도록 상자를 선택합니다.

   <Anchor target="_blank" href="/partners/ko/docs/skan-integration-guide-for-ad-networks#앱스플라이어에서-데이터-수신">SKAdNetwork 포스트백 매크로</Anchor> 목록

   <Anchor target="_blank" href="/partners/ko/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification">Advanced Privacy 포스트백 매크로</Anchor> 목록

   <div id="important-2" />

   > 🚧 **중요!**
   >
   > * 거부된 설치/인앱이벤트 포스트백을 활성화하려면 기본 포스트백 템플릿에 다음 매개 변수를 추가하세요.
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`
   > * Advance Privacy에 대해 거부된 포스트백을 활성화하려면 먼저 위의 매개 변수를 [기본 포스트백](/docs/self-serve-integration-management-for-ad-networks#기본-포스트백)에 추가해야 합니다.
   > * 위의 파라미터가 기본 포스트백과 고급 개인 정보 보호 포스트백(활성화된 경우) 모두에 추가되면 거부된 인스톨/인앱이벤트 포스트백이 활성화됩니다.

7. 포스트백 템플릿 미리보기를 사용하여 모든 것이 올바른지 확인합니다.
8. **저장**을 클릭하세요.  
   포스트백을 저장하면 변경 사항이 즉시 적용된다는 점을 알아두십시오.

문제가 있는 경우 파트너 어시스턴트 위젯을 사용하여 문의하십시오.

<div data-zendesk-anchors="accessing-integration-management=%EC%97%B0%EB%8F%99-%EA%B4%80%EB%A6%AC%EC%97%90-%EC%95%A1%EC%84%B8%EC%8A%A4%ED%95%98%EA%B8%B0 h_01H9FCSTYR157CCJWTYSNE9JQ0=%EC%97%B0%EB%8F%99-%EA%B4%80%EB%A6%AC%EC%97%90-%EC%95%A1%EC%84%B8%EC%8A%A4%ED%95%98%EA%B8%B0 attribution-link=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC h_01H9FCSTYR6HRSF9F8KCR4B3X7=%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%81%ED%81%AC h_01H9FCSTYR4Q1985DTHNE1M1CC=%EC%A4%91%EC%9A%94 default-postback=%EA%B8%B0%EB%B3%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01H9FCSTYR2WX0M0ZW3B22EKBM=%EA%B8%B0%EB%B3%B8-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01H9FCSTYSEP367WAAKCFHZT58=%EC%A4%91%EC%9A%94-1 advanced-privacy-and-skan-postbacks=%ED%94%84%EB%9D%BC%EC%9D%B4%EB%B2%84%EC%8B%9C-%EA%B0%95%ED%99%94-%EB%AA%A8%EB%93%9C%EC%99%80-skan-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01H9FCSTYSRKBMYR2BYNQJJKVM=%ED%94%84%EB%9D%BC%EC%9D%B4%EB%B2%84%EC%8B%9C-%EA%B0%95%ED%99%94-%EB%AA%A8%EB%93%9C%EC%99%80-skan-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1 h_01H9FCSTYSEJD59AWCFNXDZMYW=%EC%A4%91%EC%9A%94-2" />
