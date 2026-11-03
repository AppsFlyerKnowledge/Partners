---
title: 애드 네트워크용 InCost API
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Marketers
    - ROI360
    - Ad Networks
  created_at: '2020-04-26T19:13:47Z'
  edited_at: '2026-10-14T10:37:11Z'
  id: 360007714957
  locale: ko
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ko/articles/360007714957
---
> **한눈에 보기:** 앱스플라이어 ROI360의 일부인 InCost API를 사용하면 애드 네트워크가 프로그래밍 방식으로 광고 비용 데이터를 앱스플라이어로 전송할 수 있습니다. 그러면 광고주에게 종합적인 비용 데이터가 제공되어 광고주가 네트워크의 실제 영향력을 파악할 수 있습니다.

## InCost API 소개

InCost API는 애드 네트워크가 앱스플라이어에 비용 데이터를 전송할 수 있는 최적의 솔루션입니다. 애드 네트워크 파트너는 이 API를 사용하여 앱스플라이어에 자세한 광고 비용 데이터를 전송합니다. 앱스플라이어는 데이터를 수집하고 처리하여 대시보드와 리포트를 통해 광고주와 파트너에게 제공합니다.

#### 장점

* 원활한 비용 리포팅을 통해 고객이 네트워크의 실제 영향을 이해하는 데 도움이 됩니다. 비용 데이터가 없으면 고객은 측정 문제에서 중요한 사항을 놓치게 되고 ROAS를 정확하게 측정할 수 없습니다. 따라서 다른 미디어소스에 잘못 투자하여 수익에 부정적인 영향을 미칠 수 있습니다.
* 정확하고 완벽한 실시간 비용 측정을 보장하는 솔루션으로 ROI를 입증하세요.
* InCost API는 빠르고 간단하게 배포할 수 있으며, 그 영향은 거의 즉각적입니다. 또한 최대 90일 전의 비용 데이터를 전송할 수 있는 기능을 포함하여 데이터를 전송하는 방법과 시기를 완벽하게 제어할 수 있습니다.
* InCost API는 (클릭당 비용 전송 시 사용할 수 있는 유일한 모델인) CPI뿐만 아니라 모든 캠페인 과금 정책 모델을 지원합니다.
* 앱스플라이어 파트너 마켓플레이스에서 귀사가 지원하는 기능임을 나타내는 "비용" 배지로 이목을 끌어 보세요.

## InCost API 구현

**선행 조건:** InCost API 자격을 갖추려면 애드 네트워크에 다음이 필요합니다.

* 캠페인의 90%가 어트리뷰션에 캠페인 ID를 포함해야 합니다.
* 데이터의 최신성을 높이기 위해 하루에 6회 이상 데이터를 전송할 수 있어야 합니다. 구체적인 횟수는 애드 네트워크에 따라 다릅니다.
* [애드 네트워크가 데이터를 소급하여 업데이트하는 경우] 데이터 완성도를 높이기 위해 매번 지난 7일 동안의 데이터를 전송할 수 있어야 합니다.

**InCost API를 구현하고 앱스플라이어에 비용 데이터를 전송하기 시작합니다**.

* 다음 표의 단계를 따르세요.

| 단계 번호 | 작업 |
| --- | --- |
| 1 | InCost를 신청합니다.<ol><li>앱스플라이어의 상단 메뉴에서 **도움말** > **팀에 문의**를 선택합니다.<br />파트너 도우미 위젯이 열립니다.</li><li>**비용 측정 활성화**를 선택하고 정보를 제출합니다.<br />티켓을 제출하면 티켓이 열리고 앱스플라이어 파트너 솔루션 엔지니어가 연락을 드릴 것입니다.</li></ol> |
| 2 | 트래픽의 90% 이상에 대한 어트리뷰션 링크에 캠페인 계층 구조(캠페인 ID와 선택 사항으로서 광고 세트 ID 및 광고 ID)가 포함되어 있는지 확인하세요. |
| 3 | 앱스플라이어 대시보드에서 앱스플라이어 API 토큰을 받습니다. |
| 4 | 개발자에게 API 권한 부여 헤더에 사용할 API 토큰을 제공하고 <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-overview">개발자의 지침</Anchor>에 따라 3가지 API 메서드를 구현하도록 요청합니다.<ol><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get">앱 목록을 가져옵니다</Anchor>.</li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-uploader-post">InCost 업로드</Anchor>: 개발자에게 어떤 필드로 JSON을 채울지 알려줍니다.<ul><li>필수 필드는 반드시 입력해야 합니다. 즉, 빈 필드를 보내지 마세요.</li><li>미디어소스는 애드 네트워크 계정과 연결된(해당 계정하에 등록된) 미디어소스로 제한됩니다. 파트너 개발 관리자로부터 목록을 받습니다.</li><li>앱 <Anchor target="_blank" href="/marketers/ko/docs/about-data-freshness-and-timezone-support#appspecific-time-zone">시간대</Anchor>(앱 권한 목록 가져오기 API를 통해 리포팅된 대로)를 고려하여 비용 데이터 날짜를 앱의 <Anchor target="_blank" href="/marketers/ko/docs/about-data-freshness-and-timezone-support#appspecific-time-zone">시간대</Anchor>에 맞춰 조정합니다.</li><li>캠페인 비용 리포팅 계층 구조에 포함되지 않은 필드가 있는 경우 해당 필드는 포함하지 마세요. 예: 광고 세트 ID, 애셋 이름, 광고 ID, 광고 이름.</li></ul></li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-jobstatus-get">작업 상태를 가져옵니다</Anchor>.</li></ol> |
| 5 | 연동을 테스트합니다.<ol><li>티켓 스레드(단계 1부터)에서 API 구현이 완료되었음을 앱스플라이어에 알리고 실제 데이터를 사용하지 않고 API를 테스트할 수 있는 다음 앱에 대한 권한을 얻으십시오.<ul><li>com.cost.app</li><li>id888123456</li></ul></li><li>AppsFlyer의 사이드 메뉴에서 **Collaborate** > **Partner Marketplace를** 선택하고 파트너를 선택합니다.</li><li>**연동 설정**을 클릭하세요.</li><li>테스트 앱 중 하나를 선택합니다.</li><li>통합된 파트너의 **비용** 탭을 엽니다.</li><li>**비용 데이터 가져오기** 토글을 활성화합니다.</li><li>**비용 저장**을 클릭합니다.</li><li>**연결 테스트**를 클릭합니다.<br />API가 활성 상태입니다.</li></ol> |
| 6 | 티켓 스레드(1단계부터)에서 AppsFlyer와 통합이 작동하고 있는지 확인하십시오. |
| 7 | 광고주가 앱스플라이어 연동 파트너 페이지의 비용 탭에서 <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#cost-tab">비용 데이터 가져오기</Anchor>를 활성화했는지 확인합니다. 그러면 비용 데이터를 받기 시작합니다. |

### InCost 업로드 JSON 필드

<table><thead><tr><th>필드</th><th>필수적</th><th>설명</th></tr></thead><tbody><tr><td>날짜</td><td><span>예</span></td><td><ul><li><span>지출 날짜</span></li><li> <span>형식: </span><span> </span> </li><li> <span><code><span>2019-12-30</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td>app_id</td><td>예</td><td><ul><li>앱스플라이어 플랫폼에 표시되는 앱 ID</li><li><span>형식: 최대 250자의 문자열</span></li><li> <span>예: 안드로이드 </span>iOS /span&gt; </li></ul></td></tr><tr><td><span>media_source</span></td><td><span>예</span></td><td><ul><li><span>앱스플라이어에서 애드 네트워크 파트너 계정과 연결된 광고를 표시하는 네트워크 이름(ID)</span></li><li><span>형식: 50자의 문자열</span></li><li> <span><code><span>network_int</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td><span>af_prt</span></td><td><span>번호\*</span></td><td><ul><li><span>에이전시 어트리뷰션 및 비용 데이터에 필요합니다.</span></li><li><span>어트리뷰션 링크에 표시되고 앱스플라이어의 에이전시 계정과 연결되는 에이전시 이름입니다.</span></li><li><span>형식: 50자의 문자열</span></li><li> <span><code><span>agencya</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td><span>campaign_id</span></td><td><span>예</span></td><td><ul><li> <span>어트리뷰션 링크를 통해 전송된</span> <code><span>af_c_id</span></code><span><span> 파라미터와 동일해야 합니다. </span></span> </li><li><span>빈 문자열은 허용되지 않습니다.</span></li><li><span>형식: 24자의 문자열</span></li><li> <span><code><span>123abc</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td><span>campaign_name</span></td><td><span>예</span></td><td><ul><li><span>형식: 100자의 문자열</span></li><li> <span>예시: </span><span> </span> </li></ul></td></tr><tr><td><span>adset_id</span></td><td>번호\*</td><td><ul><li> <span><code><span>adset_name</span></code></span>을 보내는 경우 필수 </li><li> <span>어트리뷰션 링크를 통해 전송된</span> <code><span>af_adset_id</span></code><span><span> 파라미터와 동일해야 합니다. </span></span> </li><li> <span>비용 리포팅이 <code><span>adset_id</span></code>를 지원하지 않는 경우 절대로 보내지 마세요.</span> </li><li><span>형식: 24자의 문자열</span></li><li> <span><code><span>123A</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td><span>adset_name</span></td><td><span>아니요</span></td><td><ul><li> <span>이 필드를 전송하는 경우 <code><span>adset_id</span></code></span>도 함께 보내야 합니다. </li><li><span>형식: 100자의 문자열</span></li><li> <span><code><span>my_adset_name</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td><span>ad_id</span></td><td>번호\*</td><td><ul><li> <code><span>ad_name</span></code><span>을 보내는 경우 필수</span> </li><li> <span>이 필드는 어트리뷰션 링크를 통해 전송된 <code><span>af_ad_id</span></code> 파라미터와 동일해야 합니다.</span> </li><li> <span>비용 리포팅이 <code><span>adset_id</span></code>를 지원하지 않는 경우 절대로 보내지 마세요.</span> </li><li><span>형식: 24자의 문자열</span></li><li>예:<code>123AB</code> </li></ul></td></tr><tr><td><span>site_id</span></td><td>아니오</td><td><ul><li>광고를 표시하는 퍼블리셔를 식별하는 고유 ID.</li><li>형식: 24자의 문자열.</li></ul></td></tr><tr><td><span>ad_name</span></td><td><span>아니요</span></td><td><ul><li> <span>이 필드를 전송하는 경우 <code><span>ad_id</span></code></span>도 함께 보내야 합니다. </li><li><span>형식: 100자의 문자열</span></li><li>예:<code>Ad-name</code> </li></ul></td></tr><tr><td><span>지역</span></td><td><span>아니오</span></td><td><ul><li><span>비용과 관련된 것으로 기록한 국가</span></li><li><span>가능한 경우 광고가 게재된 국가를 표시해야 합니다.</span></li><li><span>형식: ISO 3166 2자 국가 코드</span></li><li> <span><code><span>US, CN, ZA</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td>통화</td><td><span>예</span></td><td><ul><li><span>지출 통화 유형</span></li><li><span>형식: ISO 4217 3자 통화 코드</span></li><li> <span><code><span>USD, EUR, ZAR</span></code> <span></span>예시 </span> </li></ul></td></tr><tr><td>spend</td><td>예</td><td><ul><li>지정된 통화를 사용한 지출 금액 </li><li>소수점 뒤에 5자리 숫자 허용</li><li>값 0(영)은 허용</li><li>음수의 값이 허용되지 않습니다.</li><li> <code>,</code> 구분 기호를 보내지 마세요.,</li><li>값을 따옴표로 묶어 보내지 마세요. </li><li>형식: 십진수</li><li>예시 값: <code>1</code> <code>1.2</code> <code>1234.20</code> </li></ul></td></tr><tr><td>채널</td><td>아니요</td><td><ul><li> <code><span>af_channel</span></code>어트리뷰션 링크를 통해 전송된<span>  파라미터와 동일해야 합니다.</span> </li><li>형식: 20자의 문자열</li><li>예:<code>my_channel</code> </li></ul></td></tr><tr><td>키워드</td><td>아니오</td><td><ul><li>형식: 100자의 문자열</li><li>예:<code>abc app</code> </li></ul></td></tr><tr><td colspan="3">\* 경우에 따라 이 필드를 보내야 하는 경우도 있으므로 비고란을 참조하세요.</td></tr></tbody></table>

<div data-zendesk-anchors="incost-api=incost-api-%EC%86%8C%EA%B0%9C h_01HE0WCBD9GD66KB1QGQ9MEXBJ=incost-api-%EC%86%8C%EA%B0%9C benefits=%EC%9E%A5%EC%A0%90 h_01HKVW85AYFG91PGYE5BDQVJNR=%EC%9E%A5%EC%A0%90 implementing-incost-api=incost-api-%EA%B5%AC%ED%98%84 h_01HKVWSWTWETTES5ZTNZ05X9VA=incost-api-%EA%B5%AC%ED%98%84 fields-for-incost-upload-json=incost-%EC%97%85%EB%A1%9C%EB%93%9C-json-%ED%95%84%EB%93%9C h_01HM8VCV81GQ6XQ4NA1EDCZ4K7=incost-%EC%97%85%EB%A1%9C%EB%93%9C-json-%ED%95%84%EB%93%9C" />
