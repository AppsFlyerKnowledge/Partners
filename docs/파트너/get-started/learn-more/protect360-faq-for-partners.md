---
title: Protect360—파트너를 위한 FAQ
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2023-06-12T12:43:34Z'
  edited_at: '2026-10-14T10:29:18Z'
  id: 16091549732497
  locale: ko
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/ko/articles/16091549732497
---
> **한눈에 보기:** 파트너가 Protect360에 대해 자주 묻는 질문에 대한 답변을 찾아보세요.

<div id="impression-level-anomalies" />

## 클릭/노출 수준 이상

<div id="why-are-impressionsclicks-being-capped" />

<Accordion title="노출 수/클릭 수가 제한되는 이유는 무엇인가요?">

앱스플라이어 Protect360 시스템은 노출 수/클릭 수 볼륨, CVR, 감지된 이상 비율, 활동의 정상적인 변동, 업계 및 지역별 벤치마크를 포함하되 이에 국한되지 않는 다양한 파라미터를 고려하여 광고 인게이지먼트 제한을 결정합니다. 알고리즘은 동적이며 변화하는 추세를 고려하여 매시간 업데이트됩니다.

제한 메커니즘이 작동하면 Protect360가 현재 24시간 주기 내에서 관련 앱에 대한 애드 네트워크의 노출 수 또는 클릭 수를 차단합니다. 다시 말하면 임계값에 도달한 후 발생한 노출/클릭은 앱스플라이어에서 기록되지 않으며, 어트리뷰션 자격도 없다는 것을 의미합니다.

네트워크는 성과 결과에 아무런 영향이 보이지 않는 비정상적으로 높은 광고 인게이지먼트 볼륨이 있는 캠페인과 퍼블리셔를 중단함으로써 임계값을 초과하지 못하게 할 수 있습니다.

다음 문서를 살펴보시기 바랍니다.  
<Anchor target="_blank" href="/partners/ko/docs/protect360-for-integrated-partners#노출-및-클릭-제한">노출 및 클릭 제한</Anchor>  
<Anchor target="_blank" href="/partners/ko/docs/protect360-for-integrated-partners#faq">제한 관련 FAQ</Anchor>

</Accordion>

<div id="i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client" />

<Accordion title="이 클라이언트를 사용하지 않음에도 불구하고 앱에서 클릭 수 제한 문제가 발생하는 이유는 무엇인가요?">

이 시나리오는 귀하의 PID가 귀하의 자체적인 측정 노력을 회피하기 위해 제3자가 조작했음을 나타낼 가능성이 큽니다. 예방적 방법으로, 앱스플라이어는 귀하의 PID가 포함된 모든 클릭이 실제로 귀하에게서 비롯되는 것인지 확인하는 "클릭 서명" 솔루션을 제공합니다.

"<Anchor target="_blank" href="/partners/ko/docs/click-signing-for-ad-networks">애드 네트워크를 위한 클릭 서명</Anchor>" 문서를 내부 팀과 공유하여 구현 가능성을 모색하세요. 그동안 대시보드의 챗봇에 사례를 시작하라고 말씀해 주시면 저희 팀에서 다음 단계를 안내해 드리겠습니다.

</Accordion>

<div id="the-number-of-capped-clicks-is-very-small-why-does-such-a-small-amount-trigger-click-capping" />

<Accordion title="제한된 클릭 수가 매우 적은데, 왜 그렇게 적은 양으로 인해 클릭 제한이 실행되나요?">

Protect360 대시보드에 표시되는 "제한된 클릭 수"는 제한이 실행되는 원인이 아닙니다. 대신, 이는 제한 주기 내에서 어트리뷰션을 위해 무시된 후속 클릭 수를 나타냅니다.

동시에, 제한 메커니즘을 통해 조사된 클릭 수와 그와 상관관계가 있는 성과는 메커니즘이 작동하기 전에 발생한 일을 나타냅니다.

<Anchor target="_blank" href="/partners/ko/docs/protect360-for-integrated-partners#노출-및-클릭-제한">노출 및 클릭 제한</Anchor>에 대해 읽어보시기 바랍니다.

</Accordion>

<div id="the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate" />

<Accordion title="클릭 플러딩으로 인해 설치가 차단되는 반면 전환율은 높은 이유는 무엇입니까?">

당사의 클릭 플러드 알고리즘은 종일 다양한 간격으로 실행되며, 임계값을 초과할 때마다 내부 파라미터와 논리에 따라 퍼블리셔의 광고 인게이지먼트는 어트리뷰션될 수 없게 됩니다.

**다음 사항을 참고하십시오.** 일부 클릭 플러드 알고리즘은 여러 앱에서 작동하므로 동일한 사기성 소스에서 발생한 이상 징후는 다른 광고된 앱에서도 인식됩니다.

다음 내용을 읽어보시기 바랍니다. <Anchor target="_blank" href="https://www.appsflyer.com/glossary/click-flooding/">클릭 플러딩이란 무엇인가요?</Anchor>

</Accordion>

<div id="installin-app-event-level-anomalies" />

## 설치/인앱 이벤트 수준 이상

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="내 테스트 설치가 어트리뷰션에서 거부된 이유는 무엇인가요?">

앱스플라이어의 사기 방지 감지 기능은 단일 설치 및 설치 클러스터와 같은 다양한 보호 계층에 걸쳐 다양한 방법론을 적용합니다. 클러스터는 퍼블리셔, 미디어소스, 앱 등 다양한 집계 기준에 따라 검토됩니다. 사기성 활동은 각 클러스터를 전체적으로 고려하는 다양한 통계 알고리즘과 머신러닝 알고리즘을 사용하여 조사됩니다. 따라서 클러스터가 높은 통계적 유의성을 가지고 사기로 판명되면 해당 클러스터의 모든 설치는 사기로 간주됩니다. 사기꾼들이 차단 메커니즘이 작동하지 않을 정도로 사기가 "희석"되기를 바라며 합법적인 설치를 대량의 사기 활동에 섞는 행위는 잘 알려진 사기 수법입니다.

기본적으로 모든 수신 설치는 LIVE 트래픽으로 간주됩니다. 따라서 테스트 설치가 Protect360 알고리즘에 따라 분류되지 않도록 하려면 테스트를 수행하기 전에 <Anchor target="_blank" href="/marketers/ko/docs/registering-test-devices">이 문서</Anchor>에서 언급한 단계에 따라 기기를 테스트 기기로 등록해야 합니다.

</Accordion>

<div id="What-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="설치 거부를 감지하는 데 어떤 감지 방법을 사용하나요?">

더 명확한 설명을 위해 거부와 관련된 "사기 하위 사유"를 검토하세요. 이 데이터는 각 광고주가 액세스 권한을 부여한 경우에 한해 Protect360 리포트 및 Protect360 대시보드에서도 사용할 수 있습니다.

<Anchor target="_blank" href="/marketers/ko/docs/protect360-raw-data-reports#차단된-이유">Protect360 차단 사유</Anchor>에 대해 읽어보시기 바랍니다.

</Accordion>

<div id="protect360-data-visibility-and-comprehension" />

## Protect360 데이터 가시성 및 이해

<div id="how-do-i-gain-visibility-into-the-protect360-results" />

<Accordion title="Protect360 결과에 대한 가시성을 얻으려면 어떻게 해야 합니까?">

각 광고주가 허가한 액세스 권한에 따라 Protect360 대시보드와 로데이터 리포트를 사용하여 감지 활동의 결과를 볼 수 있습니다.

다음 문서를 살펴보시기 바랍니다.  
<Anchor target="_blank" href="/marketers/ko/docs/protect360-dashboard">Protect360 대시보드</Anchor>  
<Anchor target="_blank" href="/marketers/ko/docs/protect360-raw-data-reports#로데이터-리포트-받기">Protect360 로데이터</Anchor>

</Accordion>

<div id="how-can-i-get-notified-in-realtime-about-blocked-traffic" />

<Accordion title="교통 차단에 대한 실시간 알림을 받으려면 어떻게 해야 하나요?">

앱스플라이어는 Protect360이 어트리뷰션을 거부하는 모든 설치에 대해 거부된 어트리뷰션 포스트백을 애드 네트워크에 제공합니다.

<Anchor target="_blank" href="/partners/ko/docs/self-serve-integration-management-for-ad-networks">Integration Management</Anchor>를 사용하여 포스트백 템플릿에 "거부된 포스트백" 파라미터를 추가하여 "거부된 포스트백"을 활성화할 수 있습니다.

</Accordion>

<div id="why-do-i-see-spikes-in-postattribution-detections" />

<Accordion title="어트리뷰션 이후 감지 횟수가 급증하는 이유는 무엇인가요?">

어트리뷰션 전 실시간 감지와 사후 어트리뷰션 감지는 모두 다양한 시간 차원에 적용되는 앱스플라이어의 Protect360 이상 감지 메커니즘에 속합니다.

실시간 감지에 비해, 사후 어트리뷰션 감지는 설치 후 수집된 데이터 포인터에 더 많이 의존합니다. 그 과정에서 이상 징후가 관찰되면 Protect360은 이상 활동을 기록하고 이를 사후 어트리뷰션 범주에 표시합니다.

위 사항을 고려해보면 특정 감지 방법(timestamp\_anomalies, behavioral\_anomalies 등)은 개별 설치 수준에서는 데이터가 확실하지 않지만 통계 분석에서 분포를 살펴보면 중요해지므로 실시간보다는 사후 어트리뷰션 단계에서 감지될 가능성이 더 큽니다.

<Anchor target="_blank" href="/marketers/ko/docs/protect360-anti-fraud-guide#postattribution-detection">사후 어트리뷰션 감지</Anchor>에 대해 자세히 알아보세요.

</Accordion>

<div data-zendesk-anchors="click-impression-level-anomalies=%ED%81%B4%EB%A6%AD%EB%85%B8%EC%B6%9C-%EC%88%98%EC%A4%80-%EC%9D%B4%EC%83%81 01H8GKS08Y22PX2SBTW5ME02C4=%ED%81%B4%EB%A6%AD%EB%85%B8%EC%B6%9C-%EC%88%98%EC%A4%80-%EC%9D%B4%EC%83%81 01H8GKS08YXVK4CPNW9TX9XBYN=why-are-impressionsclicks-being-capped i%E2%80%99m-facing-a-click-capping-issue-with-an-app-but-i%E2%80%99m-not-working-with-this-client=i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client 01H8GKS08Y3G46SFASMJRFETXR=i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client 01H8GKS08ZGM2QXBNNQCFRC007=the-number-of-capped-clicks-is-very-small-why-does-such-a-small-amount-trigger-click-capping 01H8GKS08ZGNTMNZ5JH846T9Q9=the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate install-inapp-event-level-anomalies=%EC%84%A4%EC%B9%98%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%88%98%EC%A4%80-%EC%9D%B4%EC%83%81 01H8GKS08ZRA7YT9FWJNBBSV4Q=%EC%84%A4%EC%B9%98%EC%9D%B8%EC%95%B1-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%88%98%EC%A4%80-%EC%9D%B4%EC%83%81 01H8GKS08Z2M0RTMR4GM1BJE7G=why-was-my-test-install-rejected-from-attribution What-detection-methods-are-used-to-detect-install-rejections%3F=What-detection-methods-are-used-to-detect-install-rejections 01H8H30KARRPAPT9XRREDYKHVT=What-detection-methods-are-used-to-detect-install-rejections protect360-data-visibility-and-understanding=protect360-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%8B%9C%EC%84%B1-%EB%B0%8F-%EC%9D%B4%ED%95%B4 01H8GKS08ZX2W1G0K165H96N4Z=protect360-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%8B%9C%EC%84%B1-%EB%B0%8F-%EC%9D%B4%ED%95%B4 01H8GKS08ZGEEK0HQVCRD546MW=how-do-i-gain-visibility-into-the-protect360-results 01H8GKS08ZC6SB4PT53JG5QKHG=how-can-i-get-notified-in-realtime-about-blocked-traffic 01H8GKS08Z673WG6C6JGW31F42=why-do-i-see-spikes-in-postattribution-detections" />
