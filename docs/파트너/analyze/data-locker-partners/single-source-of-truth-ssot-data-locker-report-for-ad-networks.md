---
title: 애드 네트워크에 대한 SSOT(Single Source of Truth) 데이터 락커 리포트
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2024-07-31T19:51:34Z'
  edited_at: '2026-10-14T10:34:41Z'
  id: 27168206416017
  locale: ko
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ko/articles/27168206416017
---
> **한눈에 보기:** 데이터 락커의 SSOT(Single Source of Truth) 리포트는 ID 매칭, SKAN 등의 다양한 어트리뷰션 방법에서 얻은 데이터를 병합하여 앱 캠페인 성과에 대한 통합적이고 정확한 개요를 제공합니다.  또한 최고의 데이터 정확도를 얻기 위해 BI 시스템에 데이터를 로드하는 방법을 제공합니다.

> 📘 **참고**
>
> * 광고주가 대시보드에서 [권한을 부여](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions)해야 사용자와의 데이터 공유를 시작할 수 있습니다.

## 데이터 락커란?

데이터 락커는 AWS, GCS, Snowflake 등 주요 클라우드 플랫폼에 직접 데이터를 제공하는 보안 솔루션입니다. 데이터 락커를 통해 포괄적인 분석 및 리포팅을 위해 내부 BI 시스템에 데이터를 쉽게 통합하고 사용할 수 있습니다. <Anchor target="_blank" href="/partners/ko/docs/data-locker-for-partners">더 알아보기</Anchor>.

## SSOT(Single Source of Truth)란?

SSOT(Single Source of Truth) 솔루션은 ID 매칭, SKAN 등의 다양한 어트리뷰션 방법에서 얻은 데이터를 병합하여 앱 캠페인 성과에 대한 통합적이고 정확한 개요를 제공하여 데이터 단편화 문제를 해결하는 것을 목표로 합니다. <Anchor target="_blank" href="/marketers/ko/docs/single-source-of-truth-ssot-guide-for-ios-attribution">더 알아보기</Anchor>.

## 데이터 락커에서 SSOT 리포트의 이점

Single Source of Truth 리포트는 마케터가 성과 분석 및 측정에 사용하는 것과 동일한 가시성을 제공합니다.

* **정확하고 완전한 어트리뷰션 뷰 확보:** SSOT는 다양한 어트리뷰션 방법의 데이터를 병합하는 논리를 처리하여 여러 어트리뷰션 방법으로 어트리뷰션된 설치를 중복으로 계산하는 것을 사실상 방지합니다. 이를 통해 데이터가 정확하고 실제 유저 행동과 어트리뷰션을 반영하도록 보장합니다.
* **BI 시스템에 데이터 로드:** SSOT는 집계된 데이터를 내부 BI 시스템에 효율적이고 정확하게 로드하는 방법을 제공합니다. 여기에는 모든 차원 및 지표와 함께 어트리뷰션, 인앱 이벤트, 수익 데이터가 포함됩니다.

<div id="setting-up-data-locker" />

<Accordion title="데이터 락커 설정">

상기 절차를 사용하여 데이터 락커를 설정합니다. 설정 변경 사항은 3시간 이내에 적용됩니다.

**전제 조건:**

다음 스토리지 절차 중 하나 이상을 완료하십시오.

* <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>버킷
* <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>버킷
* [베타] <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor> 버킷
* <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor> 데이터 웨어하우스

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) 데이터 락커 설정 방법:**

1. <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">앱스플라이어 파트너 대시보드</Anchor>에 로그인합니다.
2. 다음으로 이동하세요.
   * **광고주:리포트**>**데이터 락커**.
   * **마케팅 파트너**: **계정 메뉴** > **데이터 락커**를 클릭합니다.
3. <Anchor target="_blank" href="/marketers/ko/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">데이터 락커 설정 지침</Anchor> 3&#126;16단계를 따릅니다.

</Accordion>

<div id="permissions" />

<Accordion title="권한">

에이전시가 지정한(활성화한) 애드 네트워크: 에이전시에서 권한을 부여할 수 없습니다. 에이전시는 광고주에게 권한을 부여해 달라고 요청해야 합니다.

**애드 네트워크가 Single Source of Truth 또는 SSOT 데이터를 가져올 수 있도록 허용하는 방법:**

1. 앱스플라이어의 사이드 메뉴에서 **협업** > **연동된 파트너***를 선택합니다.*
2. 파트너를 검색하여 선택하세요.
3. **연동 설정**을 클릭합니다. 연동 설정 페이지로 이동합니다.
4. **파트너 활성화**가 켜짐 상태인지 확인하세요. 아닌 경우 데이터를 공유할 수 없습니다.
5. **권한** 탭으로 이동합니다.
6. 다음 애드 네트워크 권한을 사용 설정합니다.
   * **집약형 전환 데이터 액세스**.
   * **집약형 인앱 이벤트 데이터 액세스**.
   * **집약형 수익 데이터 액세스**.
7. **권한 저장**을 클릭합니다.
8. 권한을 부여받았음을 애드 네트워크에 알립니다.
9. 앱이 여러 개인 경우 파트너와 연동된 각 앱에 대해 이 절차를 반복합니다.

</Accordion>

<div id="ssot-report-facts" />

<Accordion title="SSOT 리포트 관련 팩트">

| 이름 | 설명 |
| --- | --- |
| 사용 가능한 리포트 | 다음 리포트를 사용할 수 있습니다.<ul><li>유저 유입: 유저 유입 채널에 전환을 어트리뷰션합니다. 여기에는 리인게이지먼트 기간 동안 발생하는 설치 후 활동이 포함됩니다.</li><li>리타겟팅: 발생하는 이벤트에 대한 리타겟팅 채널에 전환을 어트리뷰션합니다.<ul><li>리어트리뷰션의 결과</li><li>리인게이지먼트 기간 동안</li></ul></li><li>통합: 앱스플라이어 <Anchor target="_blank" href="/marketers/ko/docs/resolve-retargeting-double-attribution">더블 어트리뷰션</Anchor> 규칙에 따라 마지막 터치 채널에 전환을 어트리뷰션합니다. 즉, 리인게이지먼트 중에 발생하는 설치 후 활동은 UA 미디어소스가 아닌 리타겟팅 미디어소스 아래에 표시됩니다.</li></ul> |
| 리포팅 기간 | 이 리포트에서는 설치 후 최대 7일까지 코호트 지표를 제공합니다. |
| 디렉터리 구조 | 디렉터리 구조는 설치 날짜를 기준으로 구성됩니다. 각 설치 날짜 폴더에는 매일 생성되는 여러 버전이 포함됩니다. 각 버전은 이 설치 날짜에 대해 업데이트된 누적 데이터를 반영합니다. 즉, 사용 가능한 최신 리포트 버전만 처리해야 합니다. <Anchor target="_blank" href="/marketers/ko/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#디렉터리-구조">더 알아보기</Anchor> |
| 리포트 구조 | 리포트의 스키마 (측정기준 및 측정항목 포함)는 고정되어 있으며 수정할 수 없습니다. |
| 시간대 | UTC |
| 데이터 최신성 | <ul><li>일별.</li><li>지표는 해당 날짜가 끝나는 시점인 자정(UTC)에 사용 가능한 데이터를 사용하여 계산합니다.</li><li>SLA: 새 리포트는 16:00 UTC까지 데이터 락커에서 확인할 수 있습니다. 매일 마지막 15개 설치 날짜에 대해 새 버전이 생성됩니다. <Anchor target="_blank" href="/marketers/ko/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#report-folder-hierarchy">더 보기</Anchor></li></ul> |

</Accordion>

## 리포트 구조

리포트는 기준 및 지표로 구성됩니다.

지표는 어트리뷰션, 수익, 이벤트를 수행하는 고유 유저에 대한 데이터를 포괄합니다.

<div id="field-formats" />

<Accordion title="필드 형식">

<Table>
  <thead>
    <tr>
      <th>
        필드 이름
      </th>
      <th>
        설명
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        문자열 [n]
      </td>
      <td>
        문자열의 최대 길이. 일반적으로 데이터 수신 시에는 필드 길이 제한 사항을 적용하지 않지만 수신 이후에 데이터가 잘릴 수 있습니다.
      </td>
    </tr>
    <tr>
      <td>
        시간 문자열
      </td>
      <td>
        문자열의 형식은 다음과 같습니다.

        ```
        yyyy-mm-dd hh:mm:ss.
        ```

        예를 들어,

        ```
        2019-09-17 00:09:25
        ```
      </td>
    </tr>
    <tr>
      <td>
        Enum [n]
      </td>
      <td>
        Enum 필드는 특정 값만 포함할 수 있습니다. 예를 들어, selected\_currency는 3자이며 지정된 통화 코드만 포함할 수 있습니다.
      </td>
    </tr>
    <tr>
      <td>
        Timestamp
      </td>
      <td>
        10자리 UNIX 타임 스탬프. 예:  
        2020년 8월 4일 07:25 UTC는 다음과 같이 변환됩니다.

        ```
         "timestamp": "1596525944"
        ```
      </td>
    </tr>
    <tr>
      <td>
        Boolean
      </td>
      <td>
        필드의 값은 *TRUE* 또는 *FALSE*일 수 있습니다.
      </td>
    </tr>
    <tr>
      <td>
        정수
      </td>
      <td>
        정수
      </td>
    </tr>
    <tr>
      <td>
        Float
      </td>
      <td>
        소수점과 소수점 뒤의 값을 가질 수 있는 실제 부동소수입니다.
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="dimensions" />

<Accordion title="디멘션">

<Table>
  <thead>
    <tr>
      <th>
        필드 이름
      </th>
      <th>
        설명
      </th>
      <th>
        형식
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        af\_ad\_id
      </td>
      <td>
        광고 식별자. 캠페인 구조.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_ad
      </td>
      <td>
        광고 이름
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_adset\_id
      </td>
      <td>
        광고 세트 식별자. 캠페인 구조.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_adset
      </td>
      <td>
        광고 세트 이름.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        app\_id
      </td>
      <td>
        접두사 ID를 가진 앱 ID(광고주 앱).
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        attribution\_method
      </td>
      <td>
        이벤트를 어트리뷰션하는 데 사용되는 메커니즘. 이러한 메커니즘의 예로는 앱스플라이어 메서드, SKAdNetwork(SKAN) 및 오가닉이 있습니다.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        가능한 값: 클릭 노출, null.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        campaign
      </td>
      <td>
        애드 네트워크가 앱스플라이어에 리포트한 캠페인 이름.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_c\_id
      </td>
      <td>
        캠페인 식별자.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        전환 날짜 이후 경과된 일수(특정 전환 타임스탬프 아님).  
        팁! 이를 사용하여 보존 기간 및 KPI 일수를 계산합니다.
      </td>
      <td>
        int
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
        | af\_conversion | 유저가 전환했습니다. conversion\_type을 사용하여 설치, 재다운로드, 리어트리뷰션 또는 리인게이지먼트인지 파악하세요. |
        | 광고주가 인앱이벤트 정의 | 앱에서 인앱이벤트를 실행했습니다. |
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        지역
      </td>
      <td>
        ISO 국가 코드. 앱스플라이어의 기존 어트리뷰션 방법에서는 유저 IP 주소에서 파생되는 반면, SKAN에서는 데이터가 애드 네트워크에서 보강되거나 모델링됩니다.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        install\_date
      </td>
      <td>
        SKAN 앱스플라이어가 포스트백 도착 시간을 기준으로 추정합니다.

        AF:

        * UA: 설치 이후 첫 실행
        * 리타겟팅: 리인게이지먼트/리어트리뷰션 후 첫 실행
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        UA: True

        리타겟팅: 리인게이지먼트 기간 동안 원래 미디어 소스(리인게이지먼트 이전)와 리인게이지먼트 미디어 소스 둘 다에 어트리뷰션을 부여합니다. 인게이지먼트 창 내에 있는 이벤트. 원래 미디어 소스는 FALSE가 됩니다 (1차 어트리뷰션 아님). 리인게이지먼트 미디어 소스는 TRUE입니다.
      </td>
      <td>
        bool
      </td>
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td>
        이벤트에 어트리뷰션된 애드 네트워크.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        selected\_currency
      </td>
      <td>
        앱 설정에서 유저가 설정한 3자리 통화 코드(USD, EUR). ISO-4217 형식입니다. SSOT 유저 인터페이스에서 수익을 표시하는 데 사용되는 것과 동일한 통화입니다.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        가능한 값:  
        설치: 유저가 처음으로 앱을 다운로드하고 엽니다.  
        리어트리뷰션: 유저가 재설치하고 새 캠페인에 어트리뷰션됩니다.  
        재다운로드(SKAN): 유저가 앱을 삭제한 후 다시 설치합니다.  
        리인게이지먼트: 리인게이지먼트: 유저가 리타겟팅 광고와 상호 작용한 후 앱을 다시 엽니다.
      </td>
      <td>
        string
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="metrics" />

<Accordion title="측정 지표">

| 선택한 dl 이름 | 설명 | 형식 |
| --- | --- | --- |
| revenue\_selected\_currency | 선택한 통화의 누적 수익 금액. 소수점 이하 최대 2자리입니다.  <br />예: days\_post\_attribution=2인 event\_name=purchase의 경우, 이 값은 설치 후 2일 이내(둘째 날뿐만 아니라) 구매 이벤트에서 발생한 총수익을 반영합니다. | double |
| revenue\_usd | 누적 수익 금액(USD).  <br />예: days\_post\_attribution=2인 event\_name=purchase의 경우, 이 값은 설치 후 2일 이내(둘째 날뿐만 아니라) 구매 이벤트에서 발생한 총수익을 반영합니다. | double |
| skan\_duplicates | SKAN과 다른 AF 메서드에 의해 동시에 어트리뷰션된 설치는 SSOT 데이터의 중복 계산 방지를 위해 제거됩니다. | long |
| uninstalls\_count | 나중에 앱을 제거(삭제)하는 유저의 앱 유저 설치 수(유저 인입에만 해당) | long |
| unique\_users | 이벤트를 수행하는 고유 유저의 수. 값은 누적됩니다.  <br />예: days\_post\_attribution=2인 event\_name=purchase의 경우, 이 값은 설치 후 2일째 이내(둘째 날뿐만 아니라)에 구매한 고유 유저 수를 반영합니다. | int |

</Accordion>

<div id="modeled-data" />

<Accordion title="모델링된 데이터">

앱스플라이어는 기본 SKAdNetwork 리포팅이 제공할 수 없는 데이터를 모델링합니다.

* Null 변환 값(CV): SKAN에서 Apple은 유저 개인 정보를 보호하기 위해 실제 데이터를 "Null" 값으로 바꿀 수 있습니다. 데이터가 누락되지 않도록 이러한 null 값은 SSOT에서 모델링됩니다. <Anchor target="_blank" href="/marketers/ko/docs/skan-modeled-data#null-conversion-values">더 알아보기</Anchor>.
* 더 긴 설치 후 지표: 첫 2일 이후의 설치 후 기간 동안 SKAN의 데이터 세분화는 제한적이며, 이로 인해 부정확성이 발생할 수 있습니다. 높은 데이터 품질을 유지하기 위해 2보다 큰 days\_post\_attribution에 대해 수익과 고유 인앱 이벤트 유저를 모델링합니다. <Anchor target="_blank" href="/marketers/ko/docs/skan-modeled-data#revenue-ltv">더 알아보기</Anchor>.

지역 데이터: SKAN은 데이터 세분화를 제한하여 지역 데이터를 사용할 수 없게 만드는 경우가 많습니다. 이러한 경우 효율적인 성능 분석이 가능하도록 데이터를 모델링합니다. <Anchor target="_blank" href="/marketers/ko/docs/skan-modeled-data#geo">더 알아보기</Anchor>.

</Accordion>

<div id="partial-data" />

<Accordion title="부분 데이터">

최근 설치 일수를 분석할 때 연장된 설치 후 기간(예: 7일)의 지표가 완전히 성숙되지 않았을 수 있습니다. 이러한 경우 지표를 계속 사용할 수는 있지만 부분적인 데이터만 반영하게 됩니다.

몇 가지 경험칙:

* 리포트에는 사용 가능한 모든 데이터가 사용 가능하게 되는 즉시 표시됩니다.
* 5일이 지나면 설치 후 2일간의 지표가 완성됩니다*.
* 7일이 지나면 설치 후 7일간의 지표가 완성됩니다*. 설치 후 최대 15일까지 모델은 이 값을 구체화할 수 있습니다.

부분 데이터의 이유:

* 데이터 성숙도: 설치 날짜 이후의 시간이 분석 중인 일수보다 짧으면 데이터가 계속 누적되는 중이며 아직 완료되지 않은 것입니다.
* SKAN 지연: SKAN 데이터는 무작위로 지연 수신됩니다. 예를 들어, 처음 2일 동안의 설치 후 활동은 설치 후 최대 96시간(4일)까지 수신 가능합니다.
* 모델링된 데이터 타이밍: 설치 후 2일 이상의 기간에 대한 SKAN 데이터가 모델링됩니다. 우리가 사용하는 모델은 7일 후에 첫 번째 추정 값을 생성합니다. 이 기간(2일 차부터 7일 차까지) 중에는 앱스플라이어의 기존 어트리뷰션 방법의 데이터를 사용할 수 있지만 SKAN 모델링 데이터는 사용할 수 없습니다.

예(설치 날짜가 1월 1일이라고 가정):

* 1월 2일: SKAN 데이터는 아직 수신되지 않았습니다. 설치 후 2일 동안의 데이터는 설치 후 7일의 데이터와 동일하며, 둘 다 부분적이며 앱스플라이어의 기존 어트리뷰션 방법의 데이터로 구성됩니다.
* 1월 3일: SKAN 데이터가 부분적으로 수신됩니다. 설치 후 2일 동안의 데이터는 여전히 부분적 데이터이며, 이제 부분적으로 SKAN 데이터를 포함합니다. 설치 후 7일 동안의 데이터에는 아직 모델링된 SKAN 데이터가 포함되지 않습니다(첫 번째 모델링된 값은 설치 후 7일이 지나면 사용 가능함). 따라서 설치 후 2일에서 7일 사이에는 설치 후 2일에 비해 설치 후 7일의 값이 더 낮을 수 있습니다.
* 1월 6일: 설치 후 첫 2일 동안의 SKAN 데이터가 완전히 수신되었으며, 여기에는 가능한 최대 지연이 있는 포스트백이 포함되었습니다. 설치 후 2일 동안의 지표가 완성되었습니다. 이 시점에서 설치 후 7일간의 지표는 아직 완성되지 않았습니다.
* 1월 8일: 설치 후 7일간의 SKAN 모델링 데이터가 완성되었습니다. 이 모델은 1월 16일까지 값을 계속 구체화합니다.

</Accordion>

## 디렉터리 구조

<div id="report-folder-hierarchy" />

<Accordion title="리포트 폴더 계층 구조">

* 기본 폴더는 리포트 유형별로 구성됩니다. 가능한 값: ‘ssot\_unified’, ‘ssot\_retargeting’, ‘ssot\_user\_acquisition’.
* 이러한 폴더 내의 하위 폴더는 설치 날짜별로 구성됩니다.

**버전 관리**

* 각 설치 날짜 폴더에는 매일 생성되는 여러 버전이 포함됩니다.
* 각 버전은 해당 설치 날짜에 대해 업데이트된 누적 데이터를 반영합니다.
* 리포트에는 설치 날짜에 사용 가능한 모든 데이터가 포함됩니다. 예를 들어 4월 18일에 각 설치 날짜의 최신 버전에는 4월 18일 해당 시점까지의 모든 데이터가 포함됩니다.
* 팁: 정확성을 보장하기 위해 항상 사용 가능한 최신 리포트 버전을 처리합니다.

각 설치 날짜는 최대 15개 버전으로 제한됩니다. 15일이 지나면 모든 지표가 완전히 확정되고 완성됩니다. <Anchor target="_blank" href="/marketers/ko/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">더 알아보기</Anchor>.

</Accordion>

<div id="directory-and-filename-structure" />

<Accordion title="디렉터리 및 파일 이름 구조">

리포트 경로는 다음 형식으로 구성됩니다.

`<bucket-name>`/t=`<ssot_unified OR ssot_retargeting OR ssot_user_acquisition>`/install\_date=`<yyyy-mm-dd>`/version=`<unix timestamp>`/`<parquet file number>`

광고주 버킷의 폴더 계층 구조 예:

```
bucket
|
└── t=ssot_unified
    |
    ├── install_date=2024-05-05
    |   |
    |   └── version=1714890235
    |   |    |
    |   |    ├── part-00000-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    |
    |   |    ├── part-00001-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    │
    |   |    └── part-00002-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |
    |   |
    |   └── version=1714890286
    |        |
    |        ├── part-00000-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        |
    |        ├── part-00001-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        │
    |        └── part-00002-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |   |
    .   . 
    .   .
```

범례:

* t: 리포트 주제(유형)
* install\_date: 앱의 설치 날짜입니다. 즉, 설치 후 활동은 유저 작업이 발생한 날이 아니라 유저가 앱을 다운로드한 설치 날짜를 기준으로 표시됩니다.
* version: 버전이 생성된 시점을 나타내는 Unix 타임스탬프입니다.

</Accordion>

## BI 개발사 고려사항

**리포트의 데이터 범위:**

이 리포트에는 유저 유입 설치, 리타겟팅 리어트리뷰션(SKAN에서 재다운로드), 리인게이지먼트에 대한 데이터와 관련 인앱 이벤트에 대한 데이터가 포함됩니다.

<div id="loading-reports" />

<Accordion title="리포트 로드">

통합 리포트, 유저 유입 리포트, 리타겟팅 리포트를 개별적으로 또는 함께 BI 시스템에 로드할 수 있습니다. 함께 로드하고 직접 뷰를 필터링하려는 경우:

* 통합 리포트: is\_primary\_attribution=true 또는 null 필드를 사용합니다.
* 유저 유입 리포트: conversion\_type=Install을 사용합니다.
* 리타겟팅 리포트: conversion\_type=re-engagement 또는 re-attribution을 사용합니다.
* 통합 뷰: 데이터 로드 프로세스에서 통합 뷰를 사용하는 경우 캠페인 유형 간에 데이터를 분할할 수 있습니다.

* conversion\_type=install, re-engagement 또는 re-attribution(SKAN에서 재다운로드)을 사용합니다.
* 자세한 내용은 "리타겟팅 이벤트의 이중 어트리뷰션"을 참조하세요.

</Accordion>

<div id="days-postattribution" />

<Accordion title="어트리뷰션 후 일수">

> 🚧 **중요!**
>
> 이 리포트에는 수익 및 고유 유저 데이터를 설치 후 특정 일수와 연결하는 차원 days\_post\_attribution이 포함됩니다.

* 어트리뷰션(설치, 리인게이지먼트 등)의 경우 값은 0입니다.
* 수익 및 인앱 이벤트의 경우 데이터는 사전 정의된 코호트로 분류되며, 현재 설치 후 "2일" 및 "7일"로 제한됩니다.

**인앱 이벤트와 수익을 정확하게 분석하려면 days\_post\_attribution 차원에 필터를 적용해야 합니다.** 아래 예제 쿼리를 참조하세요.

흔히 범하는 실수의 예는 특정 차원 세트에 대한 수익 열을 합산하는 단순화된 논리를 적용하는 것입니다. 이 접근 방식을 사용하면 일부 수익 데이터가 두 번(days\_post\_install=2에 한 번, days\_post\_install=7에 다시 한 번) 계산되므로 잘못된 숫자가 생성됩니다. 이 예는 특정 인앱 이벤트에 대한 고유 유저를 분석할 때도 관련이 있습니다.

</Accordion>

<div id="considerations" />

<Accordion title="고려 사항">

**팁 고려 사항:**

* 마지막 버전: 항상 각 설치 날짜에 사용 가능한 최신 버전을 쿼리하여 분석을 위해 가장 최신의 정확한 데이터로 작업하고 있는지 확인합니다.
* 수익 계산: 매출은 USD로 표시되며 이벤트 당일의 환율로 계산됩니다.
* 어트리뷰션 분석: event\_name=af\_conversion인 레코드는 어트리뷰션(설치, 리어트리뷰션(SKAN에서 재다운로드), 리인게이지먼트)을 반영합니다. 어트리뷰션 수는 고유 유저 지표 아래에 표시되며, 이러한 필드에 대한 수익 지표는 비어 있게 됩니다. days\_post\_attribution 아래의 값은 0이 됩니다.
* 대시보드 비교: 설치를 대시보드와 비교할 때, 대시보드는 설치 열에서 재다운로드 및 설치 전환 유형을 모두 고려하므로 두 유형을 모두 합산합니다.
* 인앱 이벤트 분석: event\_name이 'af\_conversion'과 같지 않은 레코드는 인앱 이벤트를 반영합니다. 이벤트를 수행하는 고유 유저 수는 고유 유저 지표 아래에 표시되고, 이러한 이벤트에서 생성된 수익은 수익 지표 아래에 표시됩니다.
* 전환 유형: 이 차원을 사용하여 유저 유입 전환과 리타겟팅 전환을 구분합니다. SKAN 데이터에 대한 추가 중단(설치 대 재다운로드)을 사용할 수 있습니다. SSOT 대시보드와 데이터를 비교할 때 두 유형 모두 설치로 간주됩니다.
* 광고 수익 이벤트: 사용 가능한 경우 이러한 이벤트가 포함됩니다.
* 데이터 분리: 모든 앱 데이터는 단일 파일로 제공됩니다. 앱 ID 필드를 사용하여 앱별로 데이터를 분리하거나 데이터 락커를 앱별로 분리하도록 설정합니다.

</Accordion>

<div id="example-use-cases" />

<Accordion title="사용 사례 예시">

다음은 BI 개발자가 데이터 락커를 통해 추출할 수 있는 코호트 데이터의 인기 있고 실용적인 애플리케이션의 예입니다. 각 예제를 SQL 문과 샘플 Excel 시각적 개체로 설명합니다.

<div id="calculating-total-attributions-per-campaign" />

<Accordion title="캠페인당 총 어트리뷰션 수 계산">

이 쿼리에서는 다음을 수행합니다.

* 각 설치 날짜의 캠페인당 총 고유 어트리뷰션을 합산합니다.
* 이벤트 이름이 'af\_conversion'이고 특정 캠페인 ID(af\_c\_id)가 있는 전환을 필터링합니다.

```sql
SELECT install_date, SUM(unique_users) AS total_attributions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign" />

<Accordion title="전환(설치 및 재다운로드)을 계산하여 고유 캠페인마다 대시보드의 설치 수와 비교하기">

이 쿼리에서는 다음을 수행합니다.

* 전환 수를 계산하여 고유한 캠페인과 설치 날짜마다 신규 설치와 재다운로드를 구분합니다.
* 'install' 전환 유형과 're-download' 전환 유형을 병합하는 대시보드 설치 지표와 설치 수를 비교합니다.

```sql
SELECT install_date, conversion_type, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND conversion_type IN ('install', 're-download')    
-- The dashboard sums both under the install field
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type;
```

</Accordion>

<div id="calculating-retargeting-conversions-per-geo" />

<Accordion title="지역별 리타겟팅 전환 계산">

이 쿼리에서는 다음을 수행합니다.

* 리타겟팅 캠페인의 전환 수를 지리적 위치별로 분류하여 계산합니다.
* 이러한 전환에 대해 're-attribution' 및 're-engagement' 유형을 고려합니다.

```sql
SELECT install_date, conversion_type, geo, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type IN ('re-attribution', 're-engagement')    
-- Both types are relevant for re-targeting
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type, geo;
```

</Accordion>

<div id="calculating-installs-by-attribution-method-per-media-source" />

<Accordion title="미디어소스별 어트리뷰션 방법으로 설치 수 계산">

이 쿼리에서는 다음을 수행합니다.

* 어트리뷰션 방법(SKAN, 앱스플라이어 방법, 오가닉)으로 설치 수를 계산하고 미디어소스별로 분류합니다.
* 전환 유형이 'install'인 'af\_conversion' 이벤트를 기준으로 필터링합니다.

```sql
SELECT install_date, attribution_method, media_source, SUM(unique_users)   
AS total_installs
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type = 'install'
    AND app_id = 'YOUR_APP'
GROUP BY install_date, attribution_method, media_source;
```

</Accordion>

<div id="calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset" />

<Accordion title="광고 세트당 Facebook에 대해 설치 후 7일 동안의 누적 수익 계산">

이 쿼리에서는 Facebook에 게재된 광고의 설치 후 7일 이내에 누적된 수익을 측정합니다.

```sql
SELECT install_date,
       af_adset,
       SUM(revenue_usd) AS total_revenue_day_7
FROM ssot_unified
WHERE media_source = 'facebook'
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_adset;
```

</Accordion>

<div id="calculating-cumulative-revenue-for-selected-postinstall-periods" />

<Accordion title="선택한 설치 후 기간의 누적 수익 계산">

이 쿼리에서는 다음을 수행합니다.

* 설치 후 선택한 여러 날 동안의 누적 수익을 계산하여 2일 차와 7일 차의 합계를 분석합니다.
* 지난 7일 동안의 설치를 분석할 때 설치 후 7일 동안의 데이터가 완전하지 않을 수 있습니다. <Anchor target="_blank" href="/marketers/ko/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">더 알아보기</Anchor>

```sql
SELECT install_date,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) AS total_revenue_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) AS total_revenue_day7
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source" />

<Accordion title="미디어소스당 특정 인앱 이벤트(구매)의 수익 계산">

이 쿼리에서는 다음을 수행합니다.

* 특정 인앱 이벤트(예: 'af\_purchase')의 수익 가치를 측정하고 해당 데이터를 미디어소스별로 합산합니다.
* 설치 후 선택한 일수를 필터링하여 데이터가 이중 계산되지 않도록 합니다.

```sql
SELECT install_date, media_source, SUM(revenue_usd) AS total_purchase_revenue
FROM ssot_unified
WHERE event_name = 'af_purchase'  -- Change to your specific event
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

<div id="calculating-inapp-event-conversion-rate-for-2-days-postinstalls" />

<Accordion title="설치 후 2일 동안의 인앱 이벤트 전환율 계산">

이 쿼리에서는 모든 설치와 관련된 특정 인앱 이벤트(예: 'af\_complete\_tutorial')의 전환율을 계산합니다.

```sql
SELECT install_date,
  SUM(IF(days_post_attribution = 2 AND   
event_name = 'af_complete_tutorial', unique_users, 0)) 
  / SUM(IF(event_name = 'af_conversion', unique_users, 0))   
AS conversion_rate_day2_af_tutorial_conversion
FROM ssot_unified
WHERE conversion_type = 'install'    
-- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id" />

<Accordion title="캠페인 ID당 설치 후 7일 및 2일 동안의 ARPU 계산">

이 쿼리에서는 다음을 수행합니다.

* 캠페인 전반에서 설치 후 2일 차와 7일 차의 유저당 평균 수익(ARPU)을 계산합니다.
* 지난 7일 동안의 설치를 분석할 때 설치 후 7일 동안의 데이터가 완전하지 않을 수 있습니다. <Anchor target="_blank" href="/marketers/ko/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">더 알아보기</Anchor>

```sql
SELECT install_date,
       af_c_id,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day7
FROM ssot_unified
WHERE conversion_type = 'install'  
       -- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_c_id;
```

</Accordion>

<div id="calculating-amount-of-duplicates-per-media-source-in-this-query" />

<Accordion title="이 쿼리에서 미디어소스당 중복 수량 계산">

이 쿼리에서는 미디어소스 및 설치 날짜별로 중복된 유저 어트리뷰션의 총 횟수를 계산하여 유저 어트리뷰션에서 중복이 더 많을 수 있는 미디어 채널을 강조 표시합니다.

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
    AND event_name = 'af_conversion'
GROUP BY install_date, media_source;
```

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="특징 및 제약 사항">

| 특성 | 비고 |
| --- | --- |
| 일별 리포트 가용성 | 하루가 끝날 때 SSOT 토글이 설정된 설치 날짜에만 해당 날짜에 대한 SSOT 리포트가 있습니다. |
| 설치 후 2일 지표 | <ul><li>Conversion Studio에서 SKAN 4의 경우: 데이터는 설치 후 2일 동안의 데이터입니다.</li><li>Conversion Studio에서 SKAN 3의 경우: 데이터는 정의된 SKAN 활동 기간을 기반으로 합니다.<br />예: 활동 기간이 24시간인 경우 이 기간 내에 발생하는 이벤트가 (X+1일 차에도) 계산됩니다.</li></ul> |
| 인앱 이벤트 가용성 | Window 1의 기간 동안 발생한 이벤트에 대해서만 사용할 수 있습니다. |
| SKAN 재다운로드 분석 | 사용 가능. SSOT 대시보드에서는 이 분석을 사용할 수 없으며 설치 및 재다운로드가 모두 설치 지표에 포함됩니다. |
| SKAN Conversion Studio 구성 변경 | SKAN Conversion Studio 구성을 변경하면 이전 스키마로 인코딩된 설치의 포스트백이 계속 도착하므로 약 96시간 동안 SSOT 데이터에 부정확성이 발생할 수 있습니다. |
| 시간대 | 앱별 시간대는 사용할 수 없습니다. |
| 오가닉 데이터 | <ul><li>설치 후 2일 지표에 사용할 수 있습니다.</li></ul> |
| 전환 후 일수(설치, 리어트리뷰션, 리인게이지먼트) 데이터 | 변환 후 7일로 제한됩니다. |
| 에이전시 투명성 | 지원됨. |
| 캠페인 이름 변경 | 지원 안 됨. 캠페인 이름이 변경된 경우 그룹화 및 필터링에 캠페인 ID를 사용합니다. |
| 애드 네트워크 | <ul><li>다음과 같은 경우 SSOT DataLocker 리포트에 액세스하여 미디어소스에 어트리뷰션되는 데이터를 볼 수 있습니다.<ul><li>광고주가 Conversion Studio에서 SSOT를 사용 설정했습니다.</li><li>애드 네트워크에서 SKAN 캠페인을 실행 중입니다.</li><li>애드 네트워크는 집계 데이터에 액세스하기 위해 광고주로부터 필요한 [권한](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions)이 있습니다.</li></ul></li></ul> |
| 에이전시 액세스 | 해당 없음. 에이전시 유저는 SSOT 대시보드에서 SSOT 데이터를 볼 수 있습니다. |
| D7 지표 | <ul><li>다음과 같은 경우 누락되거나 D2 지표보다 작을 수 있습니다.<ul><li>날짜 범위에는 8일이 지나지 않은 날짜가 포함됩니다.</li><li>모델링된 데이터를 사용할 수 없습니다(예: 14일 미만의 수익 데이터). <Anchor target="_blank" href="/marketers/ko/docs/skan-modeled-data#revenue-ltv">더 알아보기</Anchor>.</li><li>지난 14일 이내에 SKAN Conversion Studio 구성이 변경되었습니다.</li><li>지정된 날짜에 설치 수가 10개 미만입니다.</li></ul></li></ul> |
| 사전 정의된 이벤트 이름 | 이벤트 이름 'af\_conversion'은 다양한 유형의 전환을 나타내는 데 사용되므로 'af\_conversion'이라는 특정한 이름을 가진 이벤트가 있는 앱에는 원래 이벤트의 이름이 'af\_conversion\_event'로 바뀝니다. |
| 현지 통화 차이 | SSOT 대시보드와 SSOT DataLocker 리포트는 동시에 계산되지 않으므로 대시보드의 현지 통화로 표시된 수익을 리포트에서 선택한 통화와 비교할 때 약간의 불일치가 발생할 수 있습니다. 이는 데이터가 계산된 시점에 사용된 환율이 약간 다르기 때문입니다. |
| SKAN D7 부분 데이터 | SKAN D7 데이터가 모델링되고 설치 후 7일이 지나 초기 버전이 준비되므로 지난 7일 이내의 날에 대한 D7 지표를 분석할 때 D7 데이터는 부분 데이터입니다. 어트리뷰션 방법이 SKAN인 레코드의 경우 D7 지표는 D2 지표보다 낮습니다. |
| D7 수익 및 인앱 이벤트 지표에 대한 제한적 세분성 | 설치 후 7일 동안의 수익 및 고유 유저 이벤트 지표는 광고 세트, 광고, 전환 유형 세분화 수준에서 사용할 수 없습니다. 이 수준의 세부 정보는 일반적으로 SKAN에서 사용할 수 없으므로 모델은 이러한 차원을 고려하지 않습니다. |
| 광고 수익 데이터 최신성 | 광고 수익 데이터가 하루 지연됩니다.<br /><br />예를 들어 7월 3일 아침에 생성된 리포트에는 7월 1일까지의 광고 수익 데이터가 포함됩니다. |

</Accordion>

<div data-zendesk-anchors="h_01J455DHWAB1J9611A4KA40PZM=%EC%B0%B8%EA%B3%A0 ssot-reports-in-data-locker=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4%EB%9E%80 h_01J454K90GWKME8F4JCDQKM3CK=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4%EB%9E%80 what-is-single-source-of-truth-ssot=ssotsingle-source-of-truth%EB%9E%80 h_01J454K90GRCFR3PSAQRTX98B4=ssotsingle-source-of-truth%EB%9E%80 benefits-of-ssot-reports-in-data-locker=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4%EC%97%90%EC%84%9C-ssot-%EB%A6%AC%ED%8F%AC%ED%8A%B8%EC%9D%98-%EC%9D%B4%EC%A0%90 h_01J454PANH9J6ZZ069RS6FVWZM=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4%EC%97%90%EC%84%9C-ssot-%EB%A6%AC%ED%8F%AC%ED%8A%B8%EC%9D%98-%EC%9D%B4%EC%A0%90 h_01J46C54ZB4YYTZ6CDHHC0EC8P=setting-up-data-locker h_01J455Q07J5XPYEBVP3BZ1FMVH=permissions h_01J29BTC9CESJF592P616WMK46=ssot-report-facts report-structure::673746b9=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EA%B5%AC%EC%A1%B0 h_01J29CQ5K4JBEP4X8YQ0V32WYR=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EA%B5%AC%EC%A1%B0 h_01J29CHBX2QNFTAQSA1W01PFH0=field-formats h_01J29BTC9CJ8GZDDCHK9NBZ4YX=dimensions h_01J29BTC9C86YMVEY17QQZNZCV=metrics h_01J29BTC9CH3DAA7ZRHG8C04MF=modeled-data h_01J29M72WAPH3KEW9N60JHTT3W=partial-data directory-structure=%EB%94%94%EB%A0%89%ED%84%B0%EB%A6%AC-%EA%B5%AC%EC%A1%B0 h_01J29MB7B7Q3PJ9YWFQESWN0KD=%EB%94%94%EB%A0%89%ED%84%B0%EB%A6%AC-%EA%B5%AC%EC%A1%B0 h_01J29MCSH4V41CPB7ZG41751QW=report-folder-hierarchy h_01J29MCSH40ATHNAJMY8KR7ANZ=directory-and-filename-structure bi-developer-considerations=bi-%EA%B0%9C%EB%B0%9C%EC%82%AC-%EA%B3%A0%EB%A0%A4%EC%82%AC%ED%95%AD h_01J29MS6XV7XYTA9Q81454WEQN=bi-%EA%B0%9C%EB%B0%9C%EC%82%AC-%EA%B3%A0%EB%A0%A4%EC%82%AC%ED%95%AD h_01J2F4HG8YHDGYFKHBBC5KSN2G=loading-reports h_01J2F4HG8YKNEVGEWTR91ADSDS=days-postattribution h_01J3YT1X908JVMDXKRQBCRD1JR=%EC%A4%91%EC%9A%94 h_01J2F4HG8YAAE0E04Y6Q9Z62NZ=considerations h_01J3A82HZF14CCS027FE991M0T=example-use-cases h_01J3A883DQFQE0WTTY4FMX3AQ4=calculating-total-attributions-per-campaign h_01J3A883DQ82K71XY408M2BW0B=calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign h_01J3A883DQ5QAVH6AX7CGCBSWG=calculating-retargeting-conversions-per-geo h_01J3A883DQE25X31SPPF166BRH=calculating-installs-by-attribution-method-per-media-source h_01J3A883DQ8QVR8WKPPX1QF414=calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset h_01J3A883DQ51T3Z6H239P5JDJ1=calculating-cumulative-revenue-for-selected-postinstall-periods h_01J3A883DQXRCQ4NWY0BCX886E=calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source h_01J3A883DQRR62BWQ6JBTZ7238=calculating-inapp-event-conversion-rate-for-2-days-postinstalls h_01J3A883DRPEVDQCWKCT9M3EC1=calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id h_01J3A883DRRZ9Y8F3KNAAPZT2S=calculating-amount-of-duplicates-per-media-source-in-this-query h_01J29MV69M667QDHMS5WGYKPCZ=traits-and-limitations" />
