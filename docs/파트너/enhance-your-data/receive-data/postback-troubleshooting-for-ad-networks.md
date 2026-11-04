---
title: 애드 네트워크에 대한 포스트백 트러블슈팅문제 해결
metadata:
  keywords:
    - Postback
    - Ad Networks
    - Partners
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2022-07-07T15:16:00Z'
  edited_at: '2026-10-14T10:34:17Z'
  id: 7466104144145
  locale: ko
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ko/articles/7466104144145
---
> **한눈에 보기:** 요약: 포스트백을 수신하는 데 문제가 있는 경우 다음 솔루션을 검토하십시오.

| **문제** | **해결 방안** |
| --- | --- |
| <span id="i-dont-see-my-advertisers-app-under-my-apps"></span>내 앱 아래에 내 **광고주**의 앱이 표시되지 않습니다. | <ul><li>광고주의 앱이 **내 앱** (상단 메뉴) 아래에 표시되지 않으면 광고주에게 연락하여 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#애드-네트워크-권한">관련 권한을 제공</Anchor>하도록 요청하십시오.</li><li><Anchor target="_blank" href="/marketers/ko/docs/partner-activation-deactivation#파트너-연동-활성화">**파트너 활성화**토글이 설정</Anchor>되어 있는지 확인하십시오.</li></ul>**참고:** 참고: 프로덕션 애플리케이션으로 테스트를 실행하는 경우 <Anchor target="_blank" href="/marketers/ko/docs/registering-test-devices">여기</Anchor>의 지침에 따라 장치를 등록했는 지 확인하십시오. |
| <span id="im-not-receiving-install-postbacks"></span>인스톨 포스트백을 받지 못하고 있습니다. | <ul><li>앱 설치가 없는 경우 설치 포스트백이 표시되지 않습니다.  앱에 설치 어트리뷰션이 있는지 확인: 설정 > 내 앱 > [**앱** 선택] > **<Anchor target="_blank" href="/partners/ko/docs/integrated-partners-dashboard">개요</Anchor>** 로 이동합니다.</li><li>어트리뷰션 링크에 *af\_installpostback=false* 파라미터가 포함되어 있는지 확인하십시오. 인스톨 포스트백은 어트리뷰션 링크에 이 파라미터가 있으면 트리거되지 않습니다.</li></ul> |
| <span id="im-not-receiving-inapp-event-postbacks"></span>인앱이벤트 포스트백을 받지 못하고 있습니다. | <ul><li><Anchor target="_blank" href="/marketers/ko/docs/in-app-event-postback-configuration">인앱이벤트 포스트백</Anchor> 섹션 아래의 연동 탭에서 이벤트가 **올바르게 매핑**되었는지 확인하십시오.</li></ul>**참고:** 참고: 이벤트 이름은 대소문자를 구분하며 서버 간/SDK를 통해 전달된 것과 동일한 이름을 사용하여 매핑해야 합니다. |
| <span id="im-not-receiving-both-install-and-inapp-event-postbacks"></span>인스톨 및 인앱이벤트 포스트백을 모두 받지 못하고 있습니다. | <ul><li>앱 설치가 없는 경우 설치 포스트백이 표시되지 않습니다. 앱에 인스톨 어트리뷰션이 있는지 확인하십시오. 설정 > 내 앱 > [ **앱** 선택] > **<Anchor target="_blank" href="/partners/ko/docs/integrated-partners-dashboard">개요</Anchor>** 로 이동합니다.</li><li>인스톨/인앱이벤트 포스트백 리포트를 확인하고 다음 필드를 검토하십시오:<ul><li>포스트백 URL 템플릿에 중요한 값이 누락되지 않았는지 확인하십시오.</li><li>포스트백 HTTP 응답 코드 HTTP 응답 코드를 확인하십시오. 2XX가 아니면 내부 서버 설정을 확인하십시오.</li><li>원래 URL 원본 URL: 해당 인스톨/이벤트에 대해 앱스플라이어가 받는 클릭/노출 URL입니다. 어트리뷰션 링크의 완전성을 확인하십시오. 링크에 제공되지 않은 데이터는 포스트백을 통해 반환할 수 없습니다.</li></ul></li><li>**Advanced Privacy** 설정 확인: 활성화된 경우 <Anchor target="_blank" href="/partners/ko/docs/advanced-privacy-guide-postback-macros-for-ad-networks">iOS 14.5 이상을 실행하는 동의하지 않은 사용자에 대한 사용자 수준 데이터</Anchor>는 포스트백에서 사용할 수 없습니다.<ul><li>연동에 Advanced Privacy 포스트백이 정의되어 있지 않지만 광고주가 Advanced Privacy를 사용하기로 결정한 경우 동의하지 않은 iOS 사용자에게는 포스트백이 제공되지 않습니다.</li></ul></li><li><Anchor target="_blank" href="/marketers/ko/docs/in-app-event-postback-configuration#인앱-이벤트-포스트백-기간">포스트백 기간</Anchor> 정의를 확인하십시오. 정의된 시간이 지나면 포스트백이 전송되지 않습니다.</li><li><Anchor target="_blank" href="/marketers/ko/docs/in-app-event-postback-configuration#조건부-인앱-이벤트-포스트백">조건부 포스트백</Anchor>이 정의되어 있는지 확인하십시오.</li><li><Anchor target="_blank" href="/partners/ko/docs/rejected-attribution-postbacks-to-integrated-partners">트래픽이 차단</Anchor>되었는지 확인하십시오: **차단된 인스톨 포스트백** 리포트를 다운로드하고 검토합니다.</li></ul> |

<div id="see-also" />

> 📄 **참고 항목**
>
> * <Anchor target="_blank" href="/marketers/ko/docs/postback-troubleshooting-for-advertisers">광고주를 위한 포스트백 문제 해결</Anchor>
> * <Anchor target="_blank" href="/marketers/ko/docs/in-app-event-postback-configuration">인앱 이벤트 포스트백 구성</Anchor>

<div data-zendesk-anchors="h_01HDP4JFM42RZNBGM9TTD5SRP0=%EC%B0%B8%EA%B3%A0-%ED%95%AD%EB%AA%A9" />
