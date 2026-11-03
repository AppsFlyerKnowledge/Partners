---
title: 시작하기—광고 네트워크를 위한 온보딩 가이드
metadata:
  keywords:
    - Ad Network
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
  created_at: '2019-03-28T08:41:59Z'
  edited_at: '2026-10-14T10:29:50Z'
  id: 360001300998
  locale: ko
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ko/articles/360001300998
---
> **한눈에 보기:** 귀사의 어트리뷰션 링크 및 포스트백 연동을 설정하고 테스트하여 앱스플라이어와 완벽하게 연동하세요. 프로세스의 단계, 일정 및 종속성을 이해하세요.

![AdNetworks_-_Onboarding__2_.png](https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png)

## 앱스플라이어란 무엇인가요?

모바일 어트리뷰션의 선두주자인 앱스플라이어는 귀사를 애드 네트워크 연동 파트너로 환영합니다. 이 문서는 앱스플라이어 파트너 등록을 완료한 애드 네트워크를 위한 것입니다. 파트너로 등록하려면 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#앱스플라이어에-새로운-파트너-초대">앱스플라이어 고객(광고주)에게 초대를 요청해야 합니다.</Anchor>

## 광고 네트워크 온보딩

연동에 필요한 단계와 이를 완료하는 데 걸리는 예상 시간은 이 문서의 **온보딩 단계** 섹션에 나와 있습니다.

연동이란:

* 앱스플라이어가 귀사의 클릭과 노출을 기록합니다. 인게이지먼트는 <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-attribution-model">앱스플라이어 어트리뷰션 모델</Anchor>에 따라 어트리뷰션됩니다.
* 요구하는 형식의 포스트백이 귀사의 엔드포인트로 전송됩니다.
* 클릭 서명, Protect360, 데이터 락커 등의 앱스플라이어 기능에 액세스할 수 있습니다.

<div id="if-you-need-help" />

<Accordion title="도움이 필요하면">

* 파트너 <Anchor target="_blank" href="/partners/ko/docs/integrated-partners-faq">FAQ</Anchor>를 확인하세요
* <Anchor target="_blank" href="/partners/ko/docs/integration-requests-for-partners">연동 변경 요청</Anchor> 문서를 참조하세요.

</Accordion>

유의사항:

* 이 문서의 예상 시간은 애드 네트워크와 협력한 경험을 바탕으로 합니다. 각 연동은 약간씩 다르므로 실제 시간은 달라질 수 있습니다.
* 앱스플라이어는 다양한 <Anchor target="_blank" href="/partners/ko/docs/platforms-for-ad-networks">성과 플랫폼</Anchor>을 지원합니다. 목록에 있는 플랫폼 중 하나를 사용한다면, 연동하기 전에 플랫폼별 지침을 검토하세요.

## 온보딩 단계

**앱스플라이어와 연동하려면**:

1. [1부—연동 및 테스트 완료.](/docs/getting-started-onboarding-guide-for-ad-networks#1부-연동-및-테스트)
2. [2부—광고주 앱과의 테스트 완료.](/docs/getting-started-onboarding-guide-for-ad-networks#2부-광고주-앱을-사용하여-테스트하세요)
3. [3부—앱스플라이어 대시보드 및 리포팅 도구 사용.](/docs/getting-started-onboarding-guide-for-ad-networks#3부-앱스플라이어-대시보드-및-리포팅-옵션)

### 1부: 연동 및 테스트

<table><thead><tr><th>작업</th><th>소요 시간</th></tr></thead><tbody><tr><td>필수 연동 단계를 완료하도록 초대하는 등록 승인 이메일을 기다리세요.</td><td>--</td></tr><tr><td colspan="2"> <strong>필수 연동 단계</strong> </td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#어트리뷰션-링크" target="_blank">귀사의 어트리뷰션 링크를 지정하세요.</a>: 어트리뷰션 링크는 매크로가 포함된 URL입니다. 매크로는 귀사가 실제 값으로 채워 사용자가 링크를 클릭할 때마다 앱스플라이어로 전송됩니다. <br/>주의! 앱스플라이어가 지원하는 성과 네트워크 플랫폼을 사용하는 경우, 플랫폼별 지침을 유념하세요. <a href="./platforms-for-ad-networks" target="_blank">성과 네트워크 가이드</a>를 참조하세요. </td><td>60</td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#기본-포스트백" target="_blank">포스트백 매크로 지정</a>: 포스트백은 앱스플라이어에서 생성된 매크로를 포함한 URL로, 전환 후 실시간으로 귀사의 서버에 전송됩니다.</td><td>60</td></tr><tr><td>제공된 자격 증명을 사용하여 <a href="https://hq1.appsflyer.com/auth/login" target="_blank">앱스플라이어 대시보드</a>에 로그인하세요. </td><td> </td></tr><tr><td>귀사의 회사 로고를 업로드하세요. 로고는 200 X 50 크기의 투명 PNG 형식이어야 합니다. <ol><li>앱스플라이어의 메뉴 표시줄에서 귀사의 이메일을 선택하고 <strong>파트너 설정</strong>을 클릭하세요. </li><li> <strong>프로필</strong> 탭에서 귀사의 로고를 업로드하세요. </li><li> <strong>저장</strong>을 클릭합니다.</li></ol></td><td>5</td></tr><tr><td>앱스플라이어 시험 앱을 이용하여 연동을 테스트하세요.<ul><li><a href="./android-integration-testing-for-ad-networks" target="_blank">안드로이드</a></li><li><a href="./ios-integration-testing-for-ad-networks" target="_blank">iOS</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>선택적 연동 단계</strong></td></tr><tr><td>[iOS] 귀사의 광고주가 앱스플라이어의 데이터 집약형 개인 정보 보호를 요구하는 경우 <a href="./self-serve-integration-management-for-ad-networks#프라이버시-강화-모드와-skan-포스트백" target="_blank">고급 개인 정보 보호</a> 연동을 완료하세요.</td><td>60</td></tr><tr><td>[iOS] SKAdNetwork 캠페인을 실행하는 경우 <a href="./self-serve-integration-management-for-ad-networks#프라이버시-강화-모드와-skan-포스트백" target="_blank">SKAdNetwork 연동</a>을 완료하세요. </td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>공인 대행사</strong></h4>성공적인 캠페인을 위해 승인한 대행사의 목록을 생성하고 관리하세요. 보안 센터의 <a href="./set-up-your-list-of-authorized-agencies" target="_blank"><strong>공인 대행사</strong></a>  섹션에 기관 ID (af_prt)를 입력하여 이 작업을 완료하세요. 대행사 ID를 얻으려면 해당 대행사가 귀사에 연락하여 제공해야 합니다.</td><td>2</td></tr><tr><td colspan="2"><p><strong>선택 기능 및 고려 사항</strong><br/> </p><p>광고주 요구 사항에 따라 연동 및 옵션을 고려하여 구현하세요.</p></td></tr><tr><td>귀사의 파트너 식별자가 사용되어 사기성 클릭이 전송되지 않도록 <a href="./click-signing-for-ad-networks" target="_blank">클릭 서명</a>을 구현하세요. </td><td>60+</td></tr><tr><td>Protect360 또는 유효성 검증 규칙을 적용하는 광고주의 경우 <a href="./postback-macros-for-ad-networks#macros-installs-inapp-events-and-rejected-events" target="_blank">거부된 어트리뷰션 포스트백</a>을 추가하세요.</td><td>15</td></tr><tr><td>API를 통해 앱스플라이어로 비용을 전송하세요. <a href="./incost-api-for-ad-networks" target="_blank">InCost API</a>를 참조하세요.</td><td>60+</td></tr><tr><td> <a href="/marketers/ko/docs/retargeting-attribution-guide" target="_blank">리타게팅 연동</a>.</td><td>15</td></tr><tr><td> <a href="/marketers/ko/docs/measure-view-through-engagements" target="_blank">뷰-쓰루 어트리뷰션 연동</a>.</td><td>15</td></tr></tbody></table>

### 2부: 광고주 앱을 사용하여 테스트하세요.

이번 단계에서는 광고주 앱을 활용하여 연동을 시험해 보겠습니다. 따라서 광고주에게 연락하여 이 부분의 몇 가지 단계를 완료해 달라고 요청해야 합니다. 이 부분에서 '광고주'라는 언급은 광고주의 대행사를 의미할 수도 있습니다.

| 수행자 | 작업 | 소요 시간 |
| --- | --- | --- |
| 광고주 | <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#integration-tab">파트너 활성화</Anchor>를 켜세요.<br /><br />이 기능이 켜지면 앱스플라이어가 귀하의 참여를 어트리뷰션 후보로 간주합니다. | 2 |
| 광고주 | <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#애드-네트워크-권한">애드 네트워크 권한</Anchor>을 부여하고 귀사의 팀원을 추가하세요.<br /><br />이 기능이 켜지면, 앱스플라이어 대시보드에서 앱 성과 데이터를 확인할 수 있습니다. 목록에 등록된 팀원만 데이터에 액세스할 수 있습니다. | 2 |
| 애드 네트워크 | <Anchor target="_blank" href="/marketers/ko/docs/user-management#creating-users">팀원을 귀사의 계정에 추가하세요</Anchor>. | 2 |
| 광고주(관리자) | <Anchor target="_blank" href="/marketers/ko/docs/registering-test-devices">시험 디바이스를 등록하세요</Anchor>. 광고주에게 귀하를 대신하여 이 작업을 해달라고 요청하세요. | 3 |
| 애드 네트워크 | <Anchor target="_blank" href="/partners/ko/docs/test-marketer-campaign-integration-with-the-ad-network">광고주 앱을 사용하여 연동을 시험하세요.</Anchor> | 60 |

### 3부: 앱스플라이어 대시보드 및 리포팅 옵션

| 옵션 |
| --- |
| <Anchor target="_blank" href="/partners/ko/docs/integrated-partners-dashboard">파트너 대시보드를 사용하세요</Anchor>. |
| 애드 네트워크를 위한 <Anchor target="_blank" href="/partners/ko/docs/data-locker-for-partners">데이터 락커</Anchor>를 사용하여 클라우드 스토리지를 통해 데이터 집약형 성과 데이터를 얻으세요. |
| Protect360 <Anchor target="_blank" href="/marketers/ko/docs/raw-data-export-page">로데이터를 받으세요.</Anchor> |

## 연동 유효성 검증 기간

앱스플라이어 생태계의 무결성을 보장하고 내부 시스템을 잘못된 트래픽으로부터 보호하기 위해 모든 새로운 애드 네트워크 연동은 유효성 검증 기간을 거칩니다. 이 기간 동안 앱스플라이어는 트래픽을 철저히 검증하고 품질을 평가한 후 <Anchor target="_blank" href="/marketers/ko/docs/partner-integrations">마켓플레이스</Anchor>에서 다른 광고주들이 연동을 사용할 수 있도록 합니다.

### 유효성 검증 기간 - FAQ

| **질문** | **답변** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>연동을 완료했는데도 광고주가 마켓플레이스에서 저를 찾을 수 없는 이유는 무엇인가요? | 유효성 검증 기간 동안, 귀하의 연동은 귀하를 추천한 광고주에게만 표시됩니다. 트래픽 품질을 검증한 후, 모든 광고주가 연동을 사용할 수 있다는 내용의 이메일을 받게 됩니다. |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>연동이 승인되도록 하려면 어떻게 해야 하나요? | 추천한 광고주에게 고품질 트래픽을 많이 제공하세요. |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>유효성 검증 완료 이메일은 언제 받을 수 있나요? | 충분한 트래픽을 검증할 수 있게 되면 유효성 검증 기간이 종료되었다는 이메일을 받게 됩니다. |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>유효성 검증의 현재 상태를 알 수 있나요? | 유효성 검증 기간이 마무리되고 이메일 알림을 받은 후에야 알 수 있습니다. |
| <span id="what-are-the-validation-criteria-based-on"></span>유효성 검증 기준은 무엇을 기준으로 하나요? | 유효성 검증 기준은 <Anchor target="_blank" href="/marketers/ko/docs/protect360-anti-fraud-guide">Protect360</Anchor>의 동적 머신러닝 알고리즘을 기반으로 합니다. 트래픽 품질, 규모 및 데이터 유효성과 같은 요소들이 업계의 모범 사례와 함께 고려됩니다. |
| <span id="another-adviertiser-wants-to-work-with-me"></span>유효성 검증 기간 동안 다른 광고주가 함께 일하고 싶다면 어떻게 해야 하나요? | 유효성 검증 기간 동안 귀사의 연동은 추천한 광고주에게만 표시됩니다. 유효성 검증 기간이 성공적으로 종료된 후에는 다른 광고주도 귀사와 협력할 수 있습니다. |
| <span id="my-integration-fails"></span>귀사의 연동이 유효성 검증에 실패하면 어떻게 되나요? | 트래픽 품질 개선을 모니터링하기 위해 유효성 검증 기간이 연장될 수도 있고, 귀사의 연동이 앱스플라이어 플랫폼에서 영구적으로 제거될 수도 있습니다. 어느 경우든 알림을 받게 됩니다. |
| <span id="replace-advertiser"></span>추천 광고주를 함께 일하는 다른 광고주로 교체할 수 있나요? | 교체는 30일 유효성 검증 기간 내에 가능합니다. |

<div data-zendesk-anchors="what-is-appsflyer=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94 h_01J09255QNBFRV8DYZPGG990A0=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94 ad-network-onboarding=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%98%A8%EB%B3%B4%EB%94%A9 h_01J09255QN61VPW292PC2CH9KN=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%98%A8%EB%B3%B4%EB%94%A9 h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help onboarding-steps=%EC%98%A8%EB%B3%B4%EB%94%A9-%EB%8B%A8%EA%B3%84 h_01J09255QNZ9QXXFB54YRYCM8P=%EC%98%A8%EB%B3%B4%EB%94%A9-%EB%8B%A8%EA%B3%84 part-1-integration-and-testing=1%EB%B6%80-%EC%97%B0%EB%8F%99-%EB%B0%8F-%ED%85%8C%EC%8A%A4%ED%8A%B8 h_01J09255QN35ZBKE2R2HDDZWSZ=1%EB%B6%80-%EC%97%B0%EB%8F%99-%EB%B0%8F-%ED%85%8C%EC%8A%A4%ED%8A%B8 h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies part-2-test-using-advertiser-apps=2%EB%B6%80-%EA%B4%91%EA%B3%A0%EC%A3%BC-%EC%95%B1%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%95%98%EC%84%B8%EC%9A%94 h_01J09255QP11XJD3C83VZZXXQZ=2%EB%B6%80-%EA%B4%91%EA%B3%A0%EC%A3%BC-%EC%95%B1%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%95%98%EC%84%B8%EC%9A%94 part-3-appsflyer-dashboard-and-reporting-options=3%EB%B6%80-%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EB%B0%8F-%EB%A6%AC%ED%8F%AC%ED%8C%85-%EC%98%B5%EC%85%98 h_01J09255QPSSD8CF0HR059RWXZ=3%EB%B6%80-%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EB%B0%8F-%EB%A6%AC%ED%8F%AC%ED%8C%85-%EC%98%B5%EC%85%98 integration-validation-period=%EC%97%B0%EB%8F%99-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D-%EA%B8%B0%EA%B0%84 h_01J09255QP82ZYZDJMA74SRYGZ=%EC%97%B0%EB%8F%99-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D-%EA%B8%B0%EA%B0%84 validation-period%E2%80%94faq=%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D-%EA%B8%B0%EA%B0%84---faq h_01J09255QP77BME57P9B7S222V=%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D-%EA%B8%B0%EA%B0%84---faq" />
