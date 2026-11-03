---
title: 파트너를 위한 통합 변경 요청
metadata:
  keywords:
    - postbacks
    - integrated partner
    - view-through attribution
    - Advertisers
    - Ad Networks
    - Partners
    - SKAD
    - Advanced Privacy
    - Marketers
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2021-01-28T12:40:43Z'
  edited_at: '2026-10-14T10:37:05Z'
  id: 360017189177
  locale: ko
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ko/articles/360017189177
---
> **간단히 보기**: 초기 통합 설정 변경 요청에 필요한 모든 정보입니다.

> 🚧 **중요!**
>
> AppsFlyer 포스트백 및 귀속 URL 구조는 전 세계적으로 적용됩니다. 이는 이러한 구조의 변경이 모든 앱의 기존 및 미래 캠페인에 영향을 미친다는 것을 의미합니다.

<Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/51858349878289">파트너 설정 변경을 위한 티켓을 열려면 파트너 어시스턴트 위젯을 사용하세요.</Anchor>

1. 모든 AppsFlyer 페이지의 오른쪽 상단에서 도움말 아이콘을 클릭하세요.
2. 위젯에서 다음 옵션 순서를 선택하세요:  
   **우리 팀에 연락하기** > **(2) 통합을 이해하거나 업데이트하고 싶습니다.** > **(1)** **내 통합 업데이트**.
3. **고급 개인 정보 보호 또는 SKAD 모드** 또는 **기본 모드** 중 하나를 선택하세요.
4. 아래 표에 명시된 필수 요구 사항을 제공하세요.

| 요청 | 세부 정보 | 요구 사항 |
| --- | --- | --- |
| <span id="enable-viewthrough-attribution"></span>뷰-쓰루 어트리뷰션 활성화 | 뷰 스루 귀속 측정 허용.  <br />매크로 `attributed_touch_type`는 참여 유형을 나타내기 위해 노출 또는 클릭을 포함합니다. <br /><br /><Anchor target="_blank" href="/marketers/ko/docs/measure-view-through-engagements">뷰 스루 귀속에 대한 자세한 내용.</Anchor> | 이 기능은 지정된 파트너에게만 제공됩니다. 관심이 있으시면 파트너 개발 관리자(PDM)에게 문의하세요. |
| <span id="enable-rejected-postback"></span>거부된 포스트백 활성화 | 연동된 파트너는 프로드 또는 유효성 검증 규칙 미준수로 인해 거부된 인스톨 및 인앱 이벤트의 포스트백을 받습니다. | <ol><li>AppsFlyer 대시보드에서 거부된 포스트백을 구성하려면 <Anchor target="_blank" href="/partners/ko/docs/self-serve-integration-management-for-ad-networks">광고 네트워크를 위한 셀프 서비스 통합 관리</Anchor>를 따르세요.</li><li>기본 포스트백 템플릿(설치/앱 내 이벤트)에 아래의 거부된 매개변수를 추가해야 합니다.<ul><li>`{is-rejected}</li><li>{blocked-reason}</li><li>{blocked-sub-reason}</li><li>{blocked-reason-value}</li></ul></li><li>거부된 매개변수가 기본 포스트백 모두에 추가되면 거부된 설치/앱 내 이벤트 포스트백이 활성화됩니다.</li></ol>문제가 발생하거나 포스트백 관리 플랫폼에 접근할 수 없는 경우:<ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"거부된 포스트백 활성화"를 티켓 제목으로 작성하십시오.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>[권장] 매크로에 대한 수신 매개변수의 이름(귀하의 기술 팀에서 정의함)은 is-rejected},{blocked-reason},{blocked-sub-reason},{blocked-reason-value}`입니다.</li><li>매개변수를 추가해야 하는 포스트백 유형(설치, 인앱 이벤트 또는 둘 다)</li></ul></li></ol> |
| <span id="enable-retargeting"></span>리타게팅 활성화 | 리타게팅 활동 측정을 허용합니다.<br />AppsFlyer는 캠페인이 리타게팅 캠페인인지 및 전환 유형(재귀속 또는 재참여)을 식별하기 위해 포스트백에 다음 매크로를 제공합니다:<ul><li>`is-retarget`</li><li>`retargeting_conversion_type`</li></ul><Anchor target="_blank" href="/marketers/ko/docs/retargeting-attribution-guide">리타게팅에 대한 자세한 내용.</Anchor> | <ol><li><Anchor target="_blank" href="/partners/ko/docs/self-serve-integration-management-for-ad-networks">광고 네트워크를 위한 셀프 서비스 통합 관리</Anchor>를 따라 AppsFlyer 대시보드에서 포스트백을 구성하십시오(설치/인앱 이벤트)</li><li>아래 매개변수가 추가되고 구성이 저장되면, AppsFlyer 백엔드의 '리타게팅 활성화' 토글이 자동으로 활성화됩니다.<ul><li>`{is-retarget}</li><li>{retargeting-conversion-type}`</li></ul></li></ol>문제가 발생하거나 포스트백 관리 플랫폼에 접근할 수 없는 경우:<ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"리타게팅 활성화" 를 티켓 제목으로 작성하십시오.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>[권장] 매크로에 대한 수신 매개변수의 이름(귀하의 기술 팀에서 정의함)은 `is-retarget` 및 `retargeting_conversion_type`.입니다.</li><li>매개변수를 추가해야 하는 포스트백 유형(설치, 인앱 이벤트 또는 둘 다)</li><li>리타게팅 캠페인 광고를 클릭한 후 기존 앱의 첫 번째 앱 열기에 대한 재참여 이벤트에 대해 재참여 포스트백이 필요한지 여부를 표시하십시오.</li></ul></li></ol> |
| <span id="enable-uninstall"></span>제거 활성화 | 제거를 측정하기 위해 `af_uninstall` 인앱 이벤트의 포스트백을 가져옵니다.<br /><br />제거에 대한 자세한 내용. | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"af\_uninstall 인앱 이벤트 포스트백 활성화"를 티켓 제목으로 작성하십시오.</li><li>귀하의 PID 또는 로그인 사용자 이름을 공유하십시오.</li></ol> |
| <span id="enable-sending-session-data"></span>세션 데이터 전송 활성화 | `af_app_opened` 인앱 이벤트에 대한 데이터 공유 허용.<br /><br /><Anchor target="_blank" href="/marketers/ko/docs/measure-sessions">세션 데이터에 대한 자세한 내용.</Anchor> | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"af\_app\_opened postback 활성화"를 티켓 제목으로 작성하세요.</li><li>PID 또는 로그인 사용자 이름을 공유하세요.</li></ol> |
| <span id="enable-postbacks-retry"></span>포스트백 재시도 활성화 | 전송 실패 시 포스트백을 여러 번 전송하도록 활성화합니다.  <br />포스트백 ID를 식별하기 위해 `postback-id` 매크로를 사용하세요.<br /><br /><Anchor target="_blank" href="/partners/ko/docs/postback-retries">포스트백 재시도에 대한 자세한 내용.</Anchor> | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"포스트백 재시도 활성화"를 티켓 제목으로 작성하세요.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>`postback-id` 매크로에 대한 수신 매개변수 이름</li></ul></li></ol> |
| <span id="update-postback"></span>포스트백 업데이트 | 현재 포스트백 구조 변경(예: 매개변수 삭제/추가, 엔드포인트 URL 변경)<br /><br /><Anchor target="_blank" href="/partners/ko/docs/postback-macros-for-ad-networks">포스트백 및 매크로에 대한 자세한 내용.</Anchor> | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"포스트백 업데이트"를 티켓 제목으로 작성하세요.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>사용 가능한 매크로를 기반으로 한 새로운 포스트백 구조</li></ul></li></ol> |
| <span id="enable-advanced-privacy-postback"></span>고급 개인정보 보호 포스트백 활성화 | 광고주의 데이터 공유 정책을 준수하기 위해 고급 개인정보 보호 통합을 설정하세요.<br /><br /><Anchor target="_blank" href="/partners/ko/docs/advanced-privacy-guide-postback-macros-for-ad-networks">고급 개인정보 보호 포스트백에 대한 자세한 내용.</Anchor> | <ol><li>AppsFlyer 대시보드에서 <Anchor target="_blank" href="/partners/ko/docs/self-serve-integration-management-for-ad-networks">고급 개인정보 보호 포스트백 구성에 대한 지침</Anchor>을 따르세요.</li><li><Anchor target="_blank" href="/partners/ko/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements">귀하의 출처 링크에 모든 필수 매개변수가 포함되어 있는지 확인하십시오.</Anchor></li></ol>문제가 발생하거나 출처 링크 템플릿에 매개변수를 추가해야 하는 경우:<ol><li>위젯에서 **고급 개인 정보 보호 또는 SKAD 모드**를 선택하십시오.</li><li>티켓 제목을 "고급 개인 정보 보호 포스트백 활성화"로 작성하십시오.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>사용 가능한 매크로를 기반으로 한 고급 개인 정보 보호 포스트백 구조</li><li>링크 업데이트: 새로운 매개변수 및 해당 매크로</li></ul></li></ol> |
| <span id="enable-skadnetwork-postback"></span>SKAdNetwork 포스트백 활성화 | SKAdNetwork 통합을 설정하고 AppsFlyer에서 포스트백을 통해 디코딩된 데이터를 수신할 수 있는 기능을 설정하십시오.<br /><br /><Anchor target="_blank" href="/partners/ko/docs/skan-integration-guide-for-ad-networks">SKAdNetwork 포스트백에 대한 자세한 내용.</Anchor> | AppsFlyer 대시보드에서 <Anchor target="_blank" href="/partners/ko/docs/self-serve-integration-management-for-ad-networks">SKAdNetwork 포스트백 구성에 대한 지침</Anchor>을 따르십시오.<br /><br />문제가 발생하는 경우:<ol><li>위젯에서 **고급 개인 정보 보호 또는 SKAD 모드**를 선택하십시오.</li><li>티켓 제목을 "고급 개인 정보 보호 포스트백 활성화"로 작성하십시오.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>KB에서 사용 가능한 매크로를 기반으로 한 SKAdNetwork 포스트백 구조</li><li>Apple SKAdNetwork ID</li></ul></li></ol> |
| <span id="update-the-logo"></span>로고 업데이트 | 로고를 추가하거나 현재 로고를 교체하십시오. | <ol><li>적절한 로고 파일이 있는지 확인하십시오: (200x50px 투명 PNG)</li><li>그런 다음, 앱스플라이어 대시보드로 이동합니다</li><li>오른쪽 상단 모서리의 이메일 주소를 클릭하십시오 > **파트너 설정**을 선택하십시오.</li><li>**프로필** 탭으로 이동하십시오 > **회사 로고**.</li><li>**업로드** 아이콘을 클릭하십시오.</li><li>로고 파일을 선택하고 확인하십시오.</li><li>페이지 하단에서 **저장**을 클릭하세요. 로고가 즉시 업데이트됩니다.</li></ol> |
| <span id="update-the-click-attribution-url"></span>클릭 귀속 URL을 업데이트하세요. | 광고주가 캠페인을 진행하는 데 사용하는 클릭 귀속 URL을 업데이트하세요.  <br /><Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">귀속 링크에 대한 자세히 알아보기.</Anchor> | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>티켓 제목으로 "클릭 귀속 URL 업데이트"를 작성하세요.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>새 매개변수 및 해당 매크로입니다.</li></ul></li><li>클릭 귀속 URL이 업데이트된 후, 광고주에게 업데이트된 귀속 링크 URL을 요청하세요.</li></ol> |
| <span id="create-update-partner-dashboard-login-email"></span>파트너 대시보드 로그인 이메일을 업데이트하세요. | AppsFlyer 계정에 로그인하고, 대시보드 데이터를 확인하며, AppsFlyer 대시보드에서 보고서를 내보내는 데 필요합니다. | 사용자가 아직 귀하의 계정에 존재하지 않는 경우, <Anchor target="_blank" href="/partners/ko/docs/user-management-for-ad-networks#사용자-생성">추가하는 방법은 다음과 같습니다.</Anchor><ol><li>새 사용자가 <Anchor target="_blank" href="/partners/ko/docs/user-management-for-ad-networks#활성-사용자-되기">활성</Anchor>인지 확인하세요.</li><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>티켓 제목으로 "파트너 대시보드 로그인 업데이트"를 작성하세요.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>현재 계정 이메일</li><li>새 계정 이메일</li><li>계정 내에서의 귀하의 역할 (관리자/팀원/팀원이 아님)</li></ul></li><li>대시보드 로그인이 업데이트된 후, 알림을 받게 됩니다. 그런 다음 업데이트된 이메일을 사용하여 비밀번호를 재설정할 수 있습니다.</li></ol> |
| <span id="disable-integration"></span>연동 중단 | 통합이 비활성화된 경우, 설치 및 인앱 이벤트는 비활성화된 통합에 귀속되지 않습니다.<br /><br />**참고**: 비활성화하기 전에 광고주가 통합 작업을 중단했는지 확인하세요. | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"통합 비활성화"를 티켓 제목으로 작성하세요.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>비활성화할 통합: 설치 또는 인앱 이벤트</li></ul></li></ol> |
| <span id="add-new-dashboard-parameter"></span>새 대시보드 매개변수 추가 | 광고주가 AppsFlyer 광고주 대시보드에서 특정 매개변수를 제공할 수 있도록 허용하여, 이를 포스트백을 통해 수신할 수 있습니다. | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"새 대시보드 매개변수 추가"를 티켓 제목으로 작성하세요.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>새 대시보드 매개변수 이름</li><li>수신 매개변수—설치 또는 인앱 이벤트 포스트백을 통해 수신하려는 경우</li><li>[추천] AppsFlyer 대시보드의 매개변수 필드 옆에 툴팁으로 표시될 매개변수 설명</li></ul></li></ol> |
| <span id="provide-the-postback-template-to-the-partner"></span>파트너에게 포스트백 템플릿을 제공하세요. | 현재 통합을 검토하세요. | <ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"포스트백 템플릿 제공"을 티켓 제목으로 작성하세요.</li><li>매크로 연동을 위해서 다음 정보가 필요합니다.<ul><li>귀하의 PID 또는 로그인 사용자 이름</li><li>확인하려는 포스트백을 지정하세요: 설치 포스트백, 인앱 이벤트 포스트백 또는 거부된 포스트백</li></ul></li></ol> |
| <span id="implement-click-signing"></span>클릭 서명을 실행합니다. | 요약: 사기 책임을 방지하기 위해 클릭에 서명 유효성 검증을 추가하면 광고 네트워크에서 부정한 클릭이 발생하지 않습니다. | 이 지침<Anchor target="_blank" href="/partners/ko/docs/click-signing-for-ad-networks">을 따르세요</Anchor> 클릭 서명을 구현하기 위해 귀하의 측에서.<br />질문이 있는 경우:<ol><li>위젯에서 **기본 모드**를 선택하십시오.</li><li>"클릭 서명"을 티켓 제목으로 작성하세요.</li><li>PID 또는 로그인 사용자 이름을 공유하세요.</li></ol> |

<div data-zendesk-anchors="h_01HEPXV5HY3Q502Y8WJAV7HTME=%EC%A4%91%EC%9A%94" />
