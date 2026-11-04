---
title: 광고 네트워크에 대한 집약 캠페인 성과 리포트
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketing Analytics
    - Ad Networks
  created_at: '2021-05-30T12:34:03Z'
  edited_at: '2026-10-14T10:30:52Z'
  id: 360020834237
  locale: ko
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/ko/articles/360020834237
---
> **간단히 보기**: 요약: 광고 네트워크는 집계된 성과 리포트(일명 코호트 리포트)를 BI 시스템에 로드하여 7일 보존 KPI와 같은 캠페인 성과 지표를 계산합니다.

<div id="aggregated-campaign-performance-report" />

## 집약 캠페인 성과 리포트

이 리포트는 해당 이벤트를 수행하는 고유 사용자 수를 포함한 캠페인 성과 데이터를 제공합니다. 사용자(광고 네트워크)는 BI 시스템의 데이터를 사용하여 광고주 KPI의 맥락에서 캠페인 성과 지표를 계산합니다. 리포트는 <Anchor target="_blank" href="/partners/ko/docs/data-locker-for-partners">파트너용 데이터 락커</Anchor>를 통해 매일 갱신됩니다.

**리포트가 필요한 이유는 무엇인가요?**

iOS 14.5 이전에는 앱스플라이어가 보낸 포스트백에 고유한 사용자 이벤트 지표를 계산하기에 충분한 데이터가 포함되어 있었습니다.

iOS 14.5를 시작하고 광고주가 집약형 프라이버시 강화 프레임워크(AAP)를 채택하면서 비동의 사용자의 포스트백에는 사용자 식별자가 포함되지 않습니다. 식별자가 부족하면 고유한 사용자 지표, 예를 들어, 7일 리텐션을 계산할 수 없습니다. 고유한 사용자 자표가 부족하면 캠페인을 최적화할 수 있는 능력과 광고주와의 공통 리텐션 목표를 설정하는 할 수 있는 능력이 저하됩니다.

리포트에는 무엇이 포함됩니까?

지표는 리포트된 차원을 사용하여 최대한 세분화되어 제공되며 다음과 같은 성과 지표를 갖습니다.

* 수익
* 해당 이벤트를 수행한 횟수
* 이벤트를 수행하는 고유 사용자 수
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vS89RlkFIss7uARroJcOcX1rU6gUmZ2ySYwfTprg9GaA2BYnvDPVqWmOicea1wrBnNuGgEuLPwzL_ac/pub?gid=0&single=true&output=csv">리포트 예시</Anchor>

리포트를 어떻게 받습니까?

* 파트너용 데이터 락커로 제공됩니다. 리포트는 <Anchor target="_blank" href="/marketers/ko/docs/about-data-freshness-and-timezone-support#daily">UTC 시간으로 매일</Anchor> 업데이트됩니다.
* 광고주가 대시보드에서 [권한을 부여](/docs/aggregated-campaign-performance-report-for-ad-networks#permission-to-get-aggregated-performance-data)해야 사용자와의 데이터 공유를 시작할 수 있습니다.

<div id="about-the-report" />

## 리포트 소개

<div id="report-structure" />

<Accordion title="리포트 구조">

<div id="dimensions" />

#### 디멘션

<Table>
  <thead>
    <tr>
      <th>
        필드 이름
      </th>
      <th>
        비고
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        app\_id
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        * 가능한 값: 인스톨, 리인게이지먼트, 리어트리뷰션
        * 등가 포스트백 매크로: is\_retargeting
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        가능한 값: 클릭, 노출, 사전 설치, 알 수 없음, TV, null
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        어트리뷰션 이벤트 이후 경과 일수.   
        최대는 day 180 입니다.

        팁! 이를 사용하여 보존 기간 및 KPI 일수를 계산합니다.
      </td>
    </tr>
    <tr>
      <td>
        event\_date
      </td>
      <td>
        이벤트 발생 날짜.

        형식: yyyy-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        conversion\_date
      </td>
      <td>
        형식: yyyy-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        event\_name
      </td>
      <td>
        이벤트를 식별합니다. 일부 이벤트 이름은 특정 의미를 갖지만, 다른 이벤트 이름은 앱에서 광고주가 설정한 인앱이벤트와 관련됩니다. 

        | event\_name | 사용자가 수행한 작업 |
        | --- | --- |
        | af\_conversion | 사용자가 전환했습니다. conversion\_type을 사용하여 인스톨인지, 리인게이지먼트인지 또는 리어트리뷰션인지를 식별합니다. |
        | af\_sessions | 앱 실행 |
        | af\_uninstall | 앱 삭제 |
        | 광고주가 인앱이벤트 정의 | 앱에서 인앱이벤트를 실행했습니다. 인앱이벤트 이름이 파트너 이벤트 이름과 매핑되지 않았습니다. |
      </td>
    </tr>
    <tr>
      <td>
        campaign
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        campaign\_id
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        광고 세트
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        adset\_id
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        광고
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        ad\_id
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        channe
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        site\_id
      </td>
      <td>
        캠페인 구조
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        리타게팅 데이터를 식별하고 중복을 제거하는 데 사용
      </td>
    </tr>
    <tr>
      <td>
        country\_code
      </td>
      <td>
        사용자 IP 주소에서 유래
      </td>
    </tr>
    <tr>
      <td>
        agency
      </td>
      <td>
        공백인 경우 연결된 에이전시가 없습니다.
      </td>
    </tr>
    <tr>
      <td>
        키워드
      </td>
      <td>
        애드 네트워크에서 보고된 내용입니다.
      </td>
    </tr>
    <tr>
      <td>
        키워드 ID
      </td>
      <td>
        [2022년 4월 27일부터 사용 가능] 광고 네트워크에서 리턴된 키워드 ID .
      </td>
    </tr>
  </tbody>
</Table>

<div id="metrics" />

#### 측정 지표

| 이름 | 필드 | 이벤트를 수행한 고유 유저 수 |
| --- | --- | --- |
| 고유 유저 | unique\_users | 이벤트를 수행한 고유 사용자 유저 수 |
| 수익 | revenue\_usd | 누적 수익(USD). 예를 들어, $100.56은 100.56으로 반영됩니다. |
| event\_count | event\_count | 이벤트가 발생한 횟수 |

</Accordion>

<div id="bi-developer-considerations" />

<Accordion title="BI 개발사 고려사항">

**리포트의 데이터 범위**

리포트에는 사용자 어트리뷰션, 인스톨, 리어트리뷰션 및 리인게이지먼트와 관련 인앱이벤트가 포함됩니다.

데이터 사용 과정에서 로직을 사용하여 캠페인 유형 간에 데이터를 분할해야 합니다. 다시 말하면 사용자 어트리뷰선(인스톨)과 리타게팅(리인게이지먼트)입니다. 이렇게 하려면 conversion\_type 및 is\_primary\_attribution 필드를 사용해야 합니다. <Anchor target="_blank" href="/marketers/ko/docs/resolve-retargeting-double-attribution">리타게팅 이벤트의 이중 어트리뷰션</Anchor>을 참고하십시오.

**필드 수준 고려 사항**

* 사후 어트리뷰션 날짜를 사용하여 리텐션 지표 계산을 쉽게 합니다.
* 캠페인 이름 및 캠페인 ID 차원을 사용하여 고유 사용자 계산: 캠페인 이름 세분성을 무시할 수 있는 경우, 캠페인 ID의 고유 개수를 합산할 수 있으며 지표가 정확합니다.
* 캠페인 계층 구조 필드를 사용하여 데이터를 집계할 수 있습니다.
* 인앱이벤트는 광고주 이벤트 이름을 사용하며 사용자의 이벤트 이름에 매핑되지 않습니다. 광고주에게 매핑을 제공하거나 대시보드에서 보도록 요청하십시오. <Anchor target="_blank" href="/marketers/ko/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">파트너 인앱이벤트 매핑</Anchor>.
* 수익의 단위는 USD이며 이벤트 일의 환율을 사용하여 계산됩니다.
* 광고 수익 이벤트는 가능한 경우 포함되지만 업데이트는 최대 5일 지연됩니다.

**일반 고려 사항**

* 데이터 최신성: 매일, 08:00 UTC에서 시작. 데이터는 데이터 락커 h=23 폴더에 기록됩니다.
* 사용 가능한 데이터는 앱스플라이어에서 어트리뷰트된 사용자 여정 어트리뷰트 데이터입니다. 즉, iOS 포스트백에서 리포트한 SKAdNetwork는 이 데이터 세트에 포함되지 않습니다.
* 데이터는 여러 앱을 포함하는 파일에 포함됩니다. app\_id를 사용하여 앱을 식별합니다.
* 특정 앱에 대한 데이터를 받지 못한 경우 광고주가 사용자에게 필요한 권한을 부여했는지 확인합니다.

</Accordion>

<div id="retention-report-considerations" />

<Accordion title="리텐션 리포트 고려사항">

예를 들어, 리텐션 7일과 같은 리텐션 지표를 생성하려면 다음 필드에 필터를 설정합니다.

* days\_post\_install=7
* event\_name=af\_session
* 필요에 따라 conversion\_type
* <Anchor target="_blank" href="/marketers/ko/docs/resolve-retargeting-double-attribution">중복 리타게팅 이벤트</Anchor>를 포함하지 않으려면 is\_primary\_production=true를 선택하거나 conversion\_type을 사용하여 데이터 집합을 인스톨로 제한합니다.
* 그룹화 기준: 필요에 따라 캠페인 및 기타 기준.
* 합계: unique\_users\_count

기준을 추가하거나 제거하면 달리 세분화된 지표를 얻을 수 있습니다.

</Accordion>

<div id="permissions" />

## 권한

사용자(광고 네트워크)는 광고주에게 여기에 나열된 권한을 부여해 달라고 요청해야 합니다. 광고주는 앱당 한 번씩 이 절차를 수행해야 합니다.

<div id="permission-to-get-aggregated-performance-data" />

<Accordion title="집약형 성과 데이터를 가져올 수 있는 권한">

에이전시가 지정한(활성화한) 애드 네트워크: 에이전시에서 권한을 부여할 수 없습니다. 에이전시는 광고주에게 권한을 부여해 달라고 요청해야 합니다.

**광고 네트워크가 집약형 성과 데이터를 가져올 수 있도록 하는 방법:**

1. 앱스플라이어의 사이드 메뉴에서 **협업** > 연동된 파트너를 선택합니다.
2. 파트너를 검색하여 선택하세요.
3. **연동 설정**을 클릭합니다. 연동 설정 페이지로 이동합니다.
4. 파트너 활성화가 켜짐 상태인지 확인하세요. 아닌 경우 데이터를 공유할 수 없습니다.
5. **권한** 탭으로 이동합니다.
6. 다음 애드 네트워크 권한을 사용 설정합니다.
   * **집약형 전환 데이터 액세스**.
   * **집약형 인앱 이벤트 데이터 액세스**.
   * **집약형 수익 데이터 액세스**.
7. 권한 저장을 클릭합니다.
8. 권한을 부여받았음을 애드 네트워크에 알립니다.
9. 앱이 여러 개인 경우 파트너와 연동된 각 앱에 대해 이 절차를 반복합니다.

</Accordion>

<div data-zendesk-anchors="aggregated-campaign-performance-report=%EC%A7%91%EC%95%BD-%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%84%B1%EA%B3%BC-%EB%A6%AC%ED%8F%AC%ED%8A%B8 h_01HM8SQ5RE1FGQDY6V1A8MMEQX=%EC%A7%91%EC%95%BD-%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%84%B1%EA%B3%BC-%EB%A6%AC%ED%8F%AC%ED%8A%B8 about-the-report=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%86%8C%EA%B0%9C h_01HM8SQ5REM6MW5GBRSXTF0N73=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%86%8C%EA%B0%9C h_01HM8SQ5RETK7HCPZGGX8KX9VG=report-structure dimensions=%EB%94%94%EB%A9%98%EC%85%98 h_01HM8SQ5RE11PW6HGTWGC2AGR5=%EB%94%94%EB%A9%98%EC%85%98 metrics=%EC%B8%A1%EC%A0%95-%EC%A7%80%ED%91%9C h_01HM8SQ5RGQEH6G6W75FVWJKSP=%EC%B8%A1%EC%A0%95-%EC%A7%80%ED%91%9C h_01HM8SQ5RGCGTWTSRHB8B4FSY2=bi-developer-considerations h_01HM8SQ5RG4JEE75F6CBTFCBB5=retention-report-considerations permissions=%EA%B6%8C%ED%95%9C h_01HM8SQ5RGNXENZ89GD74KJWH2=%EA%B6%8C%ED%95%9C h_01HM8SQ5RGQADHTEP5ED3W87VZ=permission-to-get-aggregated-performance-data" />
