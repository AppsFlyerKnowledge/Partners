---
title: 파트너용 데이터 락커
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Data Locker
    - Agencies
    - Ad Networks
  created_at: '2021-05-28T15:37:04Z'
  edited_at: '2026-10-14T10:34:49Z'
  id: 360020818517
  locale: ko
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ko/articles/360020818517
---
> **한눈에 보기:** 요약: 파트너(광고 네트워크 및 에이전시)용 데이터 락커는 앱 데이터를 AWS, GCS 또는 BigQuery에 있는 파트너의 스토리지로 전달합니다.

<Image align="center" alt="6133DataLockerForPartners.png" src="https://files.readme.io/f6cad12250fe07cf2b0a12b64eeaa597c83527b4b4e09aea11cc2a52ab53339b-4637680455313.png" />

<div id="data-locker-for-partners" />

## 파트너용 데이터 락커

파트너용 데이터 락커는 앱 데이터를 클라우드 스토리지로 전달합니다. 광고주는 앱스플라이어에 선택한 데이터를 특정 파트너와 공유할 수 있는 권한을 설정합니다.

<div id="data-locker-features" />

<Accordion title="데이터 락커 기능">

| 기능 | 설명 |
| --- | --- |
| 스토리지 옵션(클라우드) | 사용자가 다음에서 소유한 스토리지(버킷):<ul><li>AWS</li><li>GCS</li><li>Yandex</li><li>빅쿼리</li></ul><Anchor target="_blank" href="/marketers/ko/docs/data-locker-for-marketers#storage-options">스토리지 옵션 정보</Anchor> |
| 여러 앱 지원 | 사용자와 연동한 앱의 데이터를 지원합니다. 광고주는 사용자가 데이터를 가져오도록 리포트별로 권한을 부여해야 합니다. |
| 데이터 형식 옵션 | <ul><li>버킷 클라우드 스토리지의 경우:<ul><li>CSV</li><li>PARQUET</li><li>어도비</li></ul></li><li>데이터 웨어하우스</li></ul> |
| 데이터 최신성 | 최신성은 리포트 유형별로 다릅니다.<ul><li>시간별</li><li>일별. 일별: 일부 리포트는 일별로 작성되며 다음 날 준비됩니다.</li></ul> |

</Accordion>

<div id="reports-available-for-partners" />

<Accordion title="파트너가 사용할 수 있는 리포트">

사용 가능한 리포트와 리포트를 가져오는 데 필요한 권한은 파트너 별로 다릅니다. 그러나 데이터 락커 메커니즘, 스토리지 옵션 및 필요한 설정은 파트너 유형에 관계없이 동일합니다. 다음과 같이 파트너 유형별 문서를 참조하십시오.

* <Anchor target="_blank" href="/partners/ko/docs/data-locker-reports-available-for-ad-networks">애드 네트워크</Anchor>
* <Anchor target="_blank" href="/partners/ko/docs/data-locker-reports-for-agencies">대행사</Anchor>
* <Anchor target="_blank" href="/partners/ko/docs/data-locker-reports-for-api-partners">마케팅 파트너</Anchor>

</Accordion>

<div id="data-storage-architecture" />

## 데이터 스토리지 아키텍처

<div id="overview" />

<Accordion title="개요">

데이터는 선택한 스토리지 옵션에 따라 기록됩니다. 사용자는 언제든지 한 옵션에서 다른 옵션으로 변경할 수 있습니다. 변경 사항은 몇 시간 내에 반영됩니다.

클라우드 버킷 스토리지의 데이터는 보고서 유형, 날짜 및 시간에 따라 계층적 폴더 구조로 구성됩니다. 다음 그림은 이 구조의 예를 표시합니다:

<Image align="center" alt="DLFolderOVerview.png" src="https://files.readme.io/78f360ec1df72253e5b2cd725f3eecf4e17548a7f06b544a94a75a2c319d77a0-18107910420369.png" />

지정된 리포트의 데이터는 해당 리포트와 연결된 시간(h) 폴더에 포함됩니다.

* 시간 폴더 수는 리포트가 시간별 또는 일별로 스트리밍되는지 여부에 따라 다릅니다.
* 데이터는 Snappy 또는 GZIP 압축 파일 또는 Parquet 또는 CSV 형식의 압축되지 않은 파일로 제공됩니다.
* 데이터 파일은 열(필드)로 구성됩니다.
* 열 구조는 리포트 유형별로 정의됩니다.

</Accordion>

<div id="folder-structure" />

<Accordion title="폴더 구조">

| 폴더 | 설명 |
| --- | --- |
| data-locker-hourly | ![DLHourly.png](https://files.readme.io/c257b82d22622d97808a6c23603ac4eee9f2ab091bcb68a33637ac4fb749fdff-18107874510353.png)<ul><li>버킷의 최상위 폴더는 스토리지 제공업체에 따라 다릅니다.</li><li>*data-locker-hourly* 폴더에는 리포트 주제가 포함되어 있습니다.</li></ul>**버킷 소유자 및 클라우드 제공자에 기반한 폴더 구조 예시**:<ul><li>**AWS 버킷**: *&lt;af-datalocker-your bucket prefix>/&lt;generated-home-folder>&lt;subscription-id>*</li><li>**GCS 버킷:** &lt;your bucket name>/&lt;generated-home-folder>/&lt;subscription-id></li></ul> |
| t(주제) | 리포트 유형은 리포트의 주제와 관련됩니다. |
| dt(날짜) | 이는 관련 데이터 날짜입니다. 대부분의 경우 이 날짜는 이벤트가 발생한 날짜를 의미합니다. |
| h(시간) | h 폴더는 앱스플라이어가 데이터를 수신한 시간과 관련됩니다. 예를 들어 UTC 14:00-15:00 사이에 수신된 인스톨 이벤트는 h=14 파일로 스트리밍됩니다. 참고! 데이터가 앱스플라이어에 도착한 시점부터 h 폴더가 데이터 락커로 스트리밍될 때까지 약 6시간의 지연이 있습니다. 예를 들어 h=14 폴더는 6시간 후 23:00 UTC에 스트리밍됩니다.<br /><br />**폴더 특성**:<ul><li>0-23으로 번호가 지정된 24개 h 폴더가 있습니다. 예를 들어, h= 0, h= 1 등입니다.</li><li>또한 late 폴더에는 자정 이후에 도착하는 전날의 이벤트(즉, 다음 날 00:00-02:00 UTC 사이에 도착하는 이벤트)가 포함됩니다. 예를 들어 사용자가 월요일 08:00에 앱을 설치하고 이벤트가 화요일 01:00에 도착하면 이벤트는 월요일 late 폴더에 기록됩니다.</li><li>02:00 이후에 도착한 데이터는 실제 도착일시 폴더에 기록됩니다.</li><li>사용자는 late 폴더의 데이터를 사용해야 합니다. 다른 폴더에는 포함되어 있지 않습니다.</li></ul> |
| 통합 데이터 | 모든 앱의 데이터는 통합된 데이터 파일로 제공됩니다. 데이터를 로드할 때 행 수준 app\_id 필드를 사용하여 앱을 구별합니다.<br /><br />**데이터 파일의 예시는 h= 2 폴더에 있습니다.**<br /><br />![UnifiedByApp.png](https://files.readme.io/dbc39c2ce99c1ff607fd553b9c9034e55728c102f31fd18a501cc00910267b28-18107874522513.png)<ul><li>데이터 로드 프로세스에서 다음을 확인하십시오.<ul><li>\_SUCCESS 플래그가 설정된 후에만 데이터 사용을 시작합니다.</li><li>*확장자가 .gz*인 모든 파일을 로드합니다.</li></ul></li></ul> |
| 완료 플래그 | 마지막 파일(완료) 플래그는 지정된 h 폴더에 대한 모든 데이터가 기록될 때 설정됩니다.<ul><li>\_SUCCESS 플래그가 존재하는지 확인하기 전에 폴더의 데이터를 읽지 마십시오.</li><li>폴더에 데이터가 기록되지 않은 경우에도 \_SUCCESS 플래그가 설정됩니다. 다시 말하면 폴더가 비어 있을 때입니다.</li></ul> |
| 압축하기 | 파일은 gz를 사용하여 압축됩니다. 압축을 푼 후:<ul><li>파일에는 확장자가 없습니다.</li><li>각 파일에는 열(필드) 이름이 포함된 헤더 행이 있습니다.</li></ul> |
| 열 순서 | 리포트에서 필드 순서는 항상 동일합니다. 새 필드는 기존 필드의 오른쪽에 추가됩니다.<br /><br />열(필드) 정의는 리포트별로 정의됩니다. 설명은 관련 리포트 기사를 확인하십시오. |
| 필드 채우기 고려사항 | 이것은 지정된 리포트의 맥락에서 볼 때 리포트할 데이터가 없음을 의미합니다. 일반적으로 *null* 은 이 필드가 지정된 리포트 및 앱 유형의 컨텍스트로 채워지지 않음을 의미합니다. 공백 "" 은 필드가 해당 컨텍스트에서 관련이 있지만 채우는 데이터가 없음을 의미합니다.<br /><br />**시간대와 통화**:<br /><br />데이터 락커에서 제공하는 데이터는 앱별 시간대 및 통화 설정이 무시됩니다. 다음과 같습니다.<ul><li>시간대</li><li>**통화**: 통화: event\_revenue\_usd 필드는 미국 달러화(USD) 기준 입니다.</li></ul> |

</Accordion>

<div id="data-files" />

<Accordion title="데이터 파일">

데이터 파일은 분리 유형에 따라 다릅니다.

<table><thead><tr><th>콘텐츠</th><th colspan="2">세부 정보</th></tr></thead><tbody><tr><td>완료 플래그</td><td colspan="2"><p>마지막 파일(완료) 플래그는 지정된 h 폴더에 대한 모든 데이터가 기록될 때 설정됩니다.  </p><ul><li><p>_SUCCESS 플래그가 존재하는지 확인하기 전에 폴더의 데이터를 읽지 마십시오.</p></li><li><p>_SUCCESS 플래그는 지정된 폴더에 기록할 데이터가 없고 폴더가 비어 있는 경우에도 설정됩니다.  </p></li><li>참고! 앱별 구분 옵션에서는 플래그가 개별 앱 폴더가 아닌 h 폴더에 설정됩니다. 이전 절의 그림을 참조하십시오.  </li></ul></td></tr><tr><td>파일 형식</td><td colspan="2"><ul><li>데이터는 Snappy 또는 GZIP 압축 파일 또는 Parquet 또는 CSV 형식의 압축되지 않은 파일로 제공됩니다.</li><li>압축 해제 이후 데이터 파일은 사용자의 설정에 따라 Parquet 또는 CSV 형식을 가집니다.</li></ul></td></tr><tr><td>열 순서(CSV 파일)  </td><td colspan="2"><p>CSV 파일의 경우 리포트의 필드 순서는 항상 동일합니다. 새 필드를 추가하면 기존 필드 오른쪽에 추가됩니다.  </p><p>이와 관련하여:  </p><ul><li>사용자 여정 리포트의 열 구조는 동일합니다. 따라서 서로 다른 리포트 유형에 대해 유사한 데이터 로드 절차를 수행할 수 있습니다. 리포트에 포함될 필드를 선택합니다. 필드 의미는 <a href="/marketers/ko/docs/raw-data-field-dictionary" target="_blank">로데이터 사전</a>에 자세히 설명되어 있습니다.  </li><li>리포트 가용성 섹션에 FF 표기가 있는 리포트는 공통 열 구조를 따르지 않습니다.  </li></ul></td></tr><tr><td>필드 채우기 고려사항</td><td colspan="2"><p>  이것은 지정된 리포트의 맥락에서 볼 때 리포트할 데이터가 없음을 의미합니다. 일반적으로 <em>null</em> 은 이 필드가 지정된 리포트 및 앱 유형의 컨텍스트로 채워지지 않음을 의미합니다. 공백 "" 은 필드가 해당 컨텍스트에서 관련이 있지만 채우는 데이터가 없음을 의미합니다.  </p><p>제한된 미디어소스의 경우 제한된 필드의 내용이 null로 설정됩니다.  </p><p>전체적으로 null과 blank를 동일한 것으로 간주하며 모두 사용할 수 있는 데이터가 없습니다.  </p><p><strong>시간대와 통화</strong></p><p>앱별 시간대와 통화 설정은 데이터 락커에 기록된 데이터에 영향을 주지 않습니다. 다음 사항이 적용됩니다.  </p><ul><li> 시간대 </li><li> <strong>통화</strong>: 통화: event_revenue_usd 필드는 미국 달러화(USD) 기준 입니다. </li></ul></td></tr></tbody></table>

</Accordion>

<div id="storage-options" />

<Accordion title="스토리지 옵션">

* 데이터는 다음과 같이 사용자가 선택한 스토리지 소유자에게 기록됩니다.
* 스토리지 선택은 언제든 변경할 수 있습니다.
* 스토리지를 변경하는 경우 다음 사항이 발생합니다.
  * 새로 선택한 스토리지에 한 시간 이내에 쓰기를 시작할 수 있습니다.
  * 7일의 전환 기간 동안 기존 스토리지에 계속 기록합니다. 전환 기간 만료 시간이 사용자 인터페이스에 표시됩니다. 전환 기간을 사용하여 데이터 로딩 프로세스를 업데이트합니다.
  * 버킷 변경: 스토리지를 변경하는 경우 데이터는 7일간의 전환 기간에 전송되며 사용자는 데이터 사용 프로세스를 조정할 수 있습니다.

|  | 파트너 소유 스토리지(GCS, AWS, BigQuery) |
| --- | --- |
| 버킷 이름 | <ul><li>GCS:</li><li>AWS  접두사 af-가 있어야 합니다.</li></ul>예: `af-datalocker-your-bucket-name` |
| 스토리지 소유자 | 파트너 |
| 스토리지 플랫폼 | AWS, GCS, Yandex, BigQuery |
| 사용자가 데이터에 액세스하기 위한 자격 증명 | 앱스플라이어에는 알려지지 않습니다. 스토리지 제공자가 보장한 자격 증명을 사용하십시오. |
| 데이터 보존 | 사용자가 제어 |
| 보안 | 사용자가 스토리지를 제어합니다.<ul><li>AWS  AWS: 앱스플라이어를 사용하려면 버킷에 대한 GetObject, ListBucket, DeleteObject, PutObject 사용 권한이 필요합니다. 버킷은 앱스플라이어 사용 전용이어야 합니다. 다른 목적으로 사용하지 마십시오.</li><li><Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor></li></ul> |

<div id="notice-to-security-officers" />

#### **보안 담당자에 대한 통지**

고려 사항:

* 버킷 또는 대상은 앱스플라이어 전용입니다. 다른 업체는 버킷에 기록할 수 없어야 합니다.
* 데이터를 작성한 후 25시간 후에 버킷의 데이터를 삭제할 수 있습니다.
* 대상에 기록된 데이터는 이미 서버에 있는 데이터의 사본입니다. 데이터는 회사 리텐션 정책에 따라 서버에 계속 남아 있습니다.

</Accordion>

<div id="multipleconnection-principles-more-than-one-destination" />

<Accordion title="다중 연결 원칙(하나 이상의 대상)">

데이터 락커에서 데이터의 일부 또는 전체를 둘 이상의 대상(연결 설정에서 정의)으로 보낼 수 있습니다. 예를 들어 앱 A 데이터를 AWS로 보내고 앱 B 데이터를 GCS로 보낼 수 있습니다.

각 연결은 대상을 포함한 완전한 데이터 락커 설정 세트로 구성됩니다. 연결 설정은 서로 독립적입니다.

연결을 관리할 때 다음을 고려하십시오.

* 데이터 락커 설정에서 연결은 탭에 표시됩니다. 각 연결에는 연결을 관리할 수 있는 자체 설정 탭이 있습니다. 기본 탭은 "데이터 락커"입니다.
* 새 연결을 생성하는 방법은 다음과 같습니다.
  1. **Add Connection(연결 추가)** 를 클릭합니다.
  2. 연결 이름을 제공하고 스토리지 유형을 선택합니다.
  3. **저장**을 클릭하세요.  
     저장되면 기본 "데이터 락커" 탭 옆에 연결이 표시됩니다. 각 탭의 아이콘은 스토리지 유형을 나타냅니다.
* 연결 내용을 확인하거나 연결을 복제하거나 연결을 삭제하려면 ⋮(옵션)을 클릭하십시오.

</Accordion>

<div id="procedures" />

## 절차

<div id="set-up-data-locker" />

<Accordion title="데이터 락커 설정">

상기 절차를 사용하여 데이터 락커를 설정합니다. 설정 변경 사항은 3시간 이내에 적용됩니다.

**전제 조건:**

다음 스토리지 절차 중 하나 이상을 완료하십시오.

* <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor> 버킷
* <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor> bucket
* [베타] <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor> 버킷
* <Anchor target="_blank" href="/marketers/ko/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor> 데이터 웨어하우스

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) 데이터 락커 설정 방법:**

1. <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">앱스플라이어 파트너 대시보드</Anchor>에 로그인합니다.
2. 다음으로 이동하세요.
   * **광고주**: **리포트** > **데이터 락커**.
   * **마케팅 파트너**: **계정 메뉴** > 데이터 락커를 클릭합니다.
3. <Anchor target="_blank" href="/marketers/ko/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">데이터 락커 설정 지침</Anchor> 단계 3-16을 따릅니다.

</Accordion>

<div id="additional-information" />

## 추가 정보

<div id="traits-and-limitations" />

<Accordion title="특성과 제한 사항">

| **특징** | 비고 |
| --- | --- |
| 앱별 시간대 | 해당 사항 없음. |
| 앱별 통화 | 지원되지 않음 |
| 사이즈 제한 | 적용 불가 |
| 데이터 최신성 | 데이터는 본 기사에서 자세히 설명하는 특정 리포트 데이터 최신성에 따라 업데이트됩니다. |
| 과거 데이터 | 지원되지 않음 |
| 팀 멤버의 접근 권한 | 팀 구성원은 데이터 락커를 설정할 수 없습니다. |

</Accordion>

<div id="troubleshooting" />

<Accordion title="문제 해결">

<Anchor target="_blank" href="/marketers/ko/docs/data-locker-for-marketers#troubleshooting">이 문제 해결 가이드를 사용하십시오</Anchor> .

</Accordion>

<div data-zendesk-anchors="data-locker-for-partners=%ED%8C%8C%ED%8A%B8%EB%84%88%EC%9A%A9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4 h_01H8Y0DGS4Y2N99YNYEEJA6RSF=%ED%8C%8C%ED%8A%B8%EB%84%88%EC%9A%A9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4 h_01H8Y0DGS4EM06PYNS1DRMZM6Y=data-locker-features h_01H8Y0DGS4A0MYGVZ9XQ49EBT2=reports-available-for-partners data-storage-architecture=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98 h_01H8Y0DGS4WTAJV7QE2DX3VGBP=%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98 h_01H8Y0DGS4BQHBKNHZ4CD9ZMT4=overview h_01H8Y0DGS43JAREX23YX1F125K=folder-structure h_01H8Y0DGS524WNXY63351XGJKA=data-files h_01H8Y0DGS5MV6J1MMJJS8G4HC4=storage-options notice-to-security-officers=%EB%B3%B4%EC%95%88-%EB%8B%B4%EB%8B%B9%EC%9E%90%EC%97%90-%EB%8C%80%ED%95%9C-%ED%86%B5%EC%A7%80 h_01H8Y0DGS5R4QX01WBK2S33QP5=%EB%B3%B4%EC%95%88-%EB%8B%B4%EB%8B%B9%EC%9E%90%EC%97%90-%EB%8C%80%ED%95%9C-%ED%86%B5%EC%A7%80 h_01H8Y0DGS56GN6TVTSEV713DWQ=multipleconnection-principles-more-than-one-destination procedures=%EC%A0%88%EC%B0%A8 h_01H8Y0DGS5588GQPZT7MQ686T3=%EC%A0%88%EC%B0%A8 h_01H8Y0DGS57YK2PZ9ENZ80EWRJ=set-up-data-locker additional-information=%EC%B6%94%EA%B0%80-%EC%A0%95%EB%B3%B4 h_01H8Y0DGS5SYZRWFAXDSKE3YHX=%EC%B6%94%EA%B0%80-%EC%A0%95%EB%B3%B4 h_01H8Y0DGS540HK8MSCFYT9Q1RM=traits-and-limitations h_01H8Y0DGS55PJ7HV1PQ72XDDAB=troubleshooting" />
