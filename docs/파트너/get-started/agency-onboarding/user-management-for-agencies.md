---
title: 에이전시를 위한 사용자 관리
metadata:
  keywords:
    - Agencies
    - Partners
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Platform essentials
    - Agencies
  created_at: '2021-12-19T11:18:09Z'
  edited_at: '2026-10-14T10:29:06Z'
  id: 4414231896337
  locale: ko
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/ko/articles/4414231896337
---
> **요약:** 에이전시 계정의 앱스플라이어 사용자를 생성 및 관리하고, 이들에게 기능 및 앱에 액세스할 수 있는 권한을 할당합니다.

## 사용자 역할 및 액세스 권한

앱스플라이어 계정은 여러 사용자가 사용할 수 있으며, 각 사용자는 개별적으로 관리되는 권한을 가질 수 있습니다. 각 사용자의 권한은 2가지 기본 차원에 따라 정의됩니다.

* **역할** (기능에 액세스하고 기능을 수행할 수 있는 능력)
* 현재 및 미래의 앱에 대한 **앱 액세스**

이러한 각 차원 내의 사용 권한은 독립적으로 할당됩니다. 즉, 사용자에게 광범위한 기능적 역량을 갖춘 **역할**을 할당하면서도 해당 역량을 엄격하게 정의된 **앱** 세트 내에서만 행사하도록 허용할 수 있습니다.

유일한 예외는 아래에 설명된 대로 모든 기능과 앱에 액세스할 수 있는 [관리자 역할](/docs/user-management-for-agencies#관리자특수한-역할)입니다.

### 사전 정의된 역할

#### 사전 정의된 역할 해시

에이전시 계정의 각 앱스플라이어 사용자에게는 사전 정의된 4가지 역할 중 하나가 할당됩니다.

* 관리자
* 팀 관리자
* 마케팅
* 기여자

이러한 각 역할은 사용자가 액세스할 수 있는 특정 앱스플라이어 기능과 사용자가 수행할 수 있는 기능을 정의합니다. 역할별 기능의 전체 목록은 **사용자 관리** 페이지의 [역할 탭](/docs/user-management-for-agencies#역할-탭)에서 확인할 수 있습니다.

일반적으로 모든 역할은 미리 정의되어 있으며 각 역할의 기능적인 능력은 고정되어 있으므로 "혼합 및 일치"는 허용되지 않습니다. 그러나 사용자의 역할을 변경하여 언제든지 사용자의 기능적 능력을 변경할 수 있습니다(아래에서 설명한 [계정 소유자](/docs/user-management-for-agencies#계정-소유자-해시) 제외).

> 📄 **예시**
>
> Bill Bates에게 **팀 관리자** 역할을 지정했습니다. 이 역할을 통해 Bill은 **앱 설정**을 관리할 수 있지만 **감사 로그**에는 액세스할 수 없습니다.
>
> **질문:** Bill을 팀 관리자 역할로 유지하되 감사 로그에 액세스할 권한을 부여할 수 있을까요? 앱 설정을 관리할 수 있는 기능을 박탈할 수 있습니까?
>
> **답변:** 아니요. Bill이 팀 관리자 역할을 유지하는 동안에는 감사 로그에 액세스할 권한을 부여할 수 없습니다. 또한 앱 설정을 관리하는 기능도 제거할 수 없습니다. 물론 Bill을 다른 역할에 배정할 수 있고, 그의 능력은 그 역할에 의해 정의된 것으로 바뀔 것입니다.

### 임시 역할—규칙의 예외

앱스플라이어 계정이 이전 사용자 관리 시스템에 존재했다면(관리자와 팀 구성원만 사용 가능했을 때), 모든 사용자가 변경되지 않은 기능을 가진 새 시스템으로 유입되었습니다. 따라서 이러한 사용자 대부분은 **임시 역할**로 나타납니다.

[임시 역할 관리](/docs/user-management-for-agencies#managing-temp-roles)에 대해 더 알아보세요.

### 관리자—특수한 역할

앱스플라이어 계정에는 관리자가 **하나 이상** 있을 수 있지만 모든 계정에는 관리자가 하나 이상 있습니다. 이 특수한 역할에는 다음과 같은 몇 가지 고유한 특성이 있습니다.

* 관리자 역할은 다음을 포함한 **모든** 계정 기능에 액세스할 수 있습니다.
  * 모든 특징 및 기능
  * 현재 및 미래의 모든 앱
  * 모든 미디어 소스 및 지역관리자 역할의 이 ‘모든 액세스’ 특성은 변경하거나 제한할 수 없습니다.

  #### 계정 소유자 해시
* 개정을 개설할 때 생성된 사용자 (**‘계정 소유자’**)에게는 기본적으로 관리자 역할이 할당됩니다.
  * 계정 소유자는 관리자 역할에서 삭제, 제거하거나 [**사용자 관리**](/docs/user-management-for-agencies#사용자-관리-페이지) 페이지에서 편집할 수 없습니다. 마찬가지로 계정 소유자의 이메일 주소는 변경할 수 없습니다.
    * 계정 소유자를 변경해야 하는 경우 [아래 나열된 단계](/docs/user-management-for-agencies#changing-the-account-owner)를 따르십시오.
  * 계정 소유자는 처음에는 (사용자 관리 기능을 가진 추가 사용자가 생성될 때까지) 추가 사용자를 생성해야 합니다.
* 관리자 역할이 있는 유저만 <Anchor target="_blank" href="/marketers/ko/docs/managing-appsflyer-tokens">API 및 S2S 토큰 관리</Anchor>할 수 있습니다.
* 계정 소유자 이외의 관리자는 사용자 관리 페이지를 통해 앱스플라이어 계정에서 삭제하거나 다른 역할로 변경 **가능**합니다.

## 사용자 관리 페이지

**사용자 관리 페이지에 액세스하는 방법:**

1. 상단 메뉴 표시줄에서 계정 메뉴(이메일 주소 드롭다운)를 클릭하여 엽니다.
2. **사용자 관리**를 선택합니다.

### 사용자 탭

**사용자** 탭에는 계정의 모든 기존 사용자 표가 표시됩니다. 여기서부터 사용자를 생성, 관리 및 삭제할 수 있습니다.

* **사용자** 열 제목을 클릭하여 표를 알파벳순으로 정렬합니다(오름차순/내림차순).
* 검색 상자를 사용하여 특정 사용자를 찾고 표시합니다.
* **역할** 열 제목에서 필터 아이콘 <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" />을 클릭하여 역할(임시 역할 포함)별로 사용자를 필터링합니다.
  * 필터를 지우려면 필터 드롭다운 목록에서 **없음**을 선택합니다.
* 확인란을 사용하여 동시에 여러 사용자를 선택하고 [여러 사용자를 편집](/docs/user-management-for-agencies#다중-유저-편집)합니다.

### 역할 탭

**역할** 탭에는 다음을 포함하여 계정에 정의된 모든 역할 목록이 표시됩니다.

* 7가지 [사전 정의된 역할](#사전-정의된-역할)
* 현재 사용자에게 할당된 모든 [임시 역할](/docs/user-management-for-agencies#임시-역할규칙의-예외)

왼쪽 패널에서 역할 이름을 클릭하여 다음을 확인합니다.

* 역할 기능의 모든 자세한 정보
* (현재 화면의 오른쪽 상단 모서리에 있는) 해당 역할이 할당된 사용자 수
  * 사용자 아이콘 <Image alt="user_icon.png" src="https://files.readme.io/afd47a11e82e0cfac3240fe39582bd141639465952f6eef76bcf1f6e7532d6a9-16162513473937.png" width="21px" /> 위에 마우스를 놓으면 처음 20개의 목록이 표시됩니다.

## 사용자 생성

**새 사용자를 생성하는 방법:**

1. **사용자** 탭에서 **신규 사용자** 버튼을 클릭합니다.
2. 사용자 이름을 입력합니다(필수).
   * 문자, 숫자, 공백, 마침표(.), 하이픈(-), 밑줄(\_), 작은따옴표(') 또는 큰따옴표(")를 포함할 수 있습니다.
   * 다른 특수 문자는 허용되지 않습니다.
3. 사용자의 이메일 주소를 입력합니다(필수).
   * 문자, 숫자, 아포스트로피('), 앰퍼샌드(&), 달러 기호($), 해시 기호(#), 하이픈(-), 밑줄(\_) 및 마침표(.)를 포함할 수 있습니다.
   * 연이은 두 개의 마침표(..) 및 기타 특수 문자는 허용되지 않습니다.
   * 유효한 이메일 도메인으로 끝나야 합니다.

   > 🚧 **중요!**
   >
   > 사용자의 이메일 주소는 앱스플라이어 플랫폼에서 사용자를 식별하는 요소로, 다음을 의미합니다.
   >
   > * 나중에 사용자를 삭제하고 다시 만들지 않으면 변경할 수 없습니다.
   > * 사용자가 이메일을 수신할 수 있는 올바른 이메일 주소여야 합니다.
   > * 앱스플라이어 계정의 다른 사용자와 연결할 수 없습니다.
   >   * 이메일 주소가 이미 사용 중인 경우(사용자의 계정 또는 다른 계정에서) *이 사용자를 만들 수 없습니다*라는 메시지가 표시됩니다.  이 문제를 해결하려면 [아래의 문제 해결 단계](/docs/user-management-for-agencies#troubleshooting-can-t-create-this-user)를 따르십시오.

4. 사용자의 부서를 선택합니다(선택 사항).
5. 사용자의 역할을 선택합니다(필수 사항).
6. 사용자가 액세스할 수 있는 앱을 선택합니다.
   * 기본 설정을 사용하면 계정의 현재 앱과 향후 앱에 모두 액세스할 수 있습니다. 이 설정을 변경하려면 확인란을 사용하여 앱을 선택하거나 선택 취소하십시오.
   * 유저는 현재 앱에 모두 액세스할 수 있는 경우에만 이후의 모든 앱에 대한 액세스 권한을 부여받을 수 있습니다.
7. **저장**을 클릭하여 사용자를 생성합니다.

   * 계정을 활성화하기 위한 이메일 초대가 사용자에게 전송됩니다.

   #### 계정 활성화 해시

   * 사용자가 사용자 테이블에 표시됩니다. 봉투 아이콘 ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png) 초대가 전송되었으며 계정이 활성화를 기다리고 있음을 나타냅니다. 사용자가 계정을 활성화하면 봉투가 사라집니다.
   * 사용자에게 전송된 활성화 링크는 48시간 동안 유효합니다. 사용자가 초대받지 못했거나 링크가 만료된 경우 [초대장을 다시 전송](/docs/user-management-for-agencies#resending-a-user-invitation)할 수 있습니다.

## 사용자 편집

사용자는 한 번에 하나씩 또는 그룹으로 편집할 수 있습니다.

### 개별 편집

**개별 사용자를 편집하는 방법:**

1. **사용자** 탭에서 사용자 행의 맨 오른쪽에 있는 **조치** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> 버튼을 클릭합니다.
2. 메뉴에서 **편집**을 선택합니다.
3. 필요에 따라 사용자 설정을 편집합니다.
4. 이메일 주소 이외의 모든 설정을 편집할 수 있습니다.
5. **저장**을 클릭합니다.

### 다중 유저 편집

다중 유저 편집은 여러 유저의 계정 권한을 한 번에 변경할 수 있는 효율적인 방법입니다. 이 기능을 **유저** 탭의 검색 및 필터링 기능과 함께 사용하면 특히 많은 유저를 관리하는 데 도움이 될 수 있습니다.

> 📘 **참고**
>
> 다중 사용자 편집을 사용하여 사용자를 삭제하거나 관리자 역할에 할당할 수 없습니다.

**다중 사용자를 편집하는 방법:**

1. **사용자** 탭에서 편집할 사용자의 확인란을 선택합니다.
   * 표시되는 모든 사용자를 선택하려면 열 제목의 확인란을 선택합니다.
   * 현재 선택한 사용자 수가 검색 상자의 오른쪽에 표시됩니다. [계정 소유자](/docs/user-management-for-agencies#계정-소유자-해시)를 선택할 수 없으며 선택한 사용자 수에 포함되지 않습니다.
2. 이 **역할** 그리고 **앱** 버튼은 테이블의 오른쪽 상단에 표시됩니다.
   * 선택한 유저 중 한 명 이상이 향후 앱에 액세스할 수 있는 경우 **앱** 버튼을 사용할 수 없습니다. (자세한 내용은 아래의 [임시 역할 제한](/docs/user-management-for-agencies#임시-역할-제한)을 참조하십시오.)
3. 변경하려는 권한에 대한 버튼을 클릭합니다.
4. 표시되는 대화 상자 또는 드롭다운 목록을 사용하여 필요한 내용을 변경합니다.
   * 변경 내용은 선택한 모든 유저에게 적용됩니다!
5. 편집된 사용자가 표에서 강조 표시되고 변경 사항이 저장되면 그대로 사용자가 나타납니다. 그러나 다음 단계에서 변경 사항을 검토하고 확인 또는 취소할 수 있습니다.
6. 변경 사항을 검토합니다. **저장**을 눌러 확인하거나 **취소**를 눌러 변경을 취소합니다.

> 📄 **예시**
>
> * 계정에 10명의 유저가 있습니다. 이 중 6명은 **마케팅**역할을 가집니다.
> * Alice, Bill, Charlie가 방금 승진했고, 이들의 **마케팅** 역할에서 **팀 관리자** 역할로 변경하려고 합니다.
> * Alice는 Astounding 앱으로 작업할 것입니다. Bill은 Astounding 앱으로 작업할 것입니다. Charlie는 Charming 앱으로 작업할 것입니다.
>
> **단계:**
>
> 1. 역할 필터 <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" />를 사용하여 **마케팅** 역할의 유저만 볼 수 있습니다.
> 2. Alice, Bill 및 Charlie를 **팀 매니저** 역할로 변경합니다.
>    * Alice, Bill, Charlie의 확인란을 선택합니다.
>    * **역할** 버튼을 클릭합니다.
>    * 드롭다운 목록에서 **팀 매니저**를 선택합니다.
>    * **저장**을 클릭하여 확인합니다.
>    * 변경 내용을 확인하면 **역할** 필터가 지워지고 표에 모든 유저가 표시됩니다.
> 3. Alice, Bill, Charlie에게 적절한 앱 액세스 권한을 부여합니다.
>    * 검색 상자를 사용하여 Alice를 찾은 다음 Alice의 유저를 개별적으로 편집하여 Astounding 앱에 액세스할 수 있습니다.
>    * Bill과 Charlie가 이 단계를 반복해 각각 Beautiful 및 Charming 앱에 대한 액세스 권한을 부여합니다.

## 사용자 삭제

**사용자를 삭제하는 방법:**

1. **사용자** 탭에서 사용자 행의 맨 오른쪽에 있는 **조치** 버튼 <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" />을 클릭합니다.
2. 메뉴에서 **삭제**를 선택합니다.

## 특수 상황 및 추가 절차

<div id="managing-temp-roles" />

<Accordion title="임시 역할 관리">

귀하의 계정이 이전에 선행 유저 관리 시스템을 사용한 경우 기존 유저에게 [**임시 역할**](/docs/user-management-for-agencies#임시-역할규칙의-예외)을 할당하여 새 시스템에 변경되지 않은 기능으로 가져올 수 있도록 했습니다.

* 동일한 기능을 가진 유저에게 동일한 임시 역할이 할당되었습니다.
* [역할 탭](/docs/user-management-for-agencies#역할-탭)의 기능을 사용하여 각 임시 역할의 기능과 현재 역할의 사용자 목록을 검토합니다.

#### 임시 역할 제한

임시 역할은 이전 사용자 관리 시스템에서 원활하게 전환할 수 있도록 특별히 설계되었습니다. 따라서 다음과 같은 제한된 상황에서만 사용할 수 있습니다.

* 임시 역할을 다른 사용자(새 사용자든 기존 사용자든)에게 할당할 수 없습니다.
* 임시 역할이 있는 사용자에게는 다른 임시 역할을 할당할 수 없습니다(단, 액세스 권한이 있는 앱은 변경할 수 있음).
  * 유저가 임시 역할인 동안에는 이후 앱에 대한 유저의 액세스 변경이 **불가**합니다.
* 임시 역할을 가진 유저를 사전 정의된 역할로 변경하면 이전에 할당된 임시 역할(또는 다른 임시 역할)로 되돌릴 수 없습니다.
* 임시 역할의 마지막 사용자가 삭제되면 해당 역할이 계정에 더 이상 표시되지 않습니다.

> 📄 **예시**
>
> 귀하의 계정은 이전에 당사의 이전 사용자 관리 시스템을 사용했습니다. 귀하의 계정이 새 시스템으로 이동될 당시 Diana와 Edward가 기존 사용자였습니다. Diana는 현재 임시 역할 1에 있고 Edward는 임시 역할 2에 있습니다.
>
> * 귀하는 새 직원 Fiona를 고용합니다. Fiona에게 7개의 [미리 정의된 역할](#사전-정의된-역할) 중 하나를 할당할 수 있습니다. 그러나 Fiona에게 임시 역할 1 또는 임시 역할 2는 할당할 수 없습니다.
> * Diana는 임시 역할 1에서 임시 역할 2로 이동할 수 없습니다. 하지만 사전 정의된 역할 중 어떤 역할이든 Diana에게 할당할 수 있습니다. 필요에 따라 앱 액세스 권한을 변경할 수도 있습니다.
> * Diana를 임시 역할 1에서 팀 관리자 역할로 이동하는 경우 나중에 임시 역할 1로 다시 이동할 수 없습니다.
> * Diana를 팀 관리자 역할로 이동했을 때 임시 역할 1의 마지막 사용자였다면, 임시 역할 1이 더 이상 계정에 표시되지 않습니다.

</Accordion>

<div id="changing-the-account-owner" />

<Accordion title="계정 소유자 변경하기">

모든 관리자는 계정 소유자와 동일한 권한을 가지므로 일반적으로 계정 소유자를 변경할 필요는 없습니다. 그러나 계정 소유자를 변경해야 하는 경우에는 다음 단계를 수행하십시오.

> 🚧 **중요!**
>
> 시작하기 전에 고려해야 할 몇 가지 문제:
>
> * 토큰 v1과 함께 Pull, Master 또는 GDPR API를 계속 사용하는 경우 계정 소유자를 변경하면 이러한 서비스가 자동으로 재설정됩니다. 데이터 손실을 방지하려면 **계정 소유자를 변경하기 전**에 <Anchor target="_blank" href="/marketers/ko/docs/bulletin-api-token-changes">토큰 v2로 이러한 API를 사용하도록 전환</Anchor>하세요.
> * 계정 소유자 변경은 다음 단계에 따라 수동으로 완료해야 합니다. **사용자 관리** 페이지에서는 수행할 수 없습니다.

#### #1–채팅 위젯을 통해 요청 보내기

계정 소유자 변경 과정을 시작하려면 <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">이 링크</Anchor>를 사용하여 채팅 위젯을 열거나 상단 메뉴 표시줄에서 도움말 버튼을 클릭하세요. 채팅에 다음 정보를 포함하세요.

* 바꾸려는 계정 소유자의 이름
* 새 계정 소유자의 이름, 직함, 이메일

#### #2–다음 단계

변경이 처리되면 귀하는 앱스플라이어로부터 이메일 알림을 받게 됩니다.

* 이전 계정 소유자가 앱스플라이어 계정을 계속 사용하도록 하려면 해당 계정에 대한 <Anchor target="_blank" href="/marketers/ko/docs/user-management#creating-users">새 사용자를 생성</Anchor>하고 새 역할을 할당하십시오.
* 토큰 v2를 사용하는 API는 계정 소유자 변경의 영향을 받지 않습니다. <Anchor target="_blank" href="/marketers/ko/docs/managing-appsflyer-tokens">토큰 관리에 대해 더 알아보기</Anchor>

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="'이 사용자를 생성할 수 없음' 문제 해결">

새 사용자의 이메일 주소를 입력할 때 *이 사용자를 생성할 수 없음*이라는 오류 메시지가 표시되면 일반적으로 이메일이 앱스플라이어 사용자(계정 또는 다른 사용자)와 이미 연결되어 있다는 의미입니다. 사용자의 상황과 관련된 단계를 수행하십시오.

사용자가 귀하의 계정에 있는 경우:

* 사용자가 계정을 활성화했는지 확인하십시오. 활성화하지 않았다면 필요한 경우 [초대장을 다시 보내십시오](/docs/user-management-for-agencies#resending-a-user-invitation).
* 사용자가 계정을 활성화한 경우 사용자와 연결된 이메일 주소를 사용하여 다시 로그인하도록 요청합니다. 필요한 경우 **암호 분실** 단계를 따르도록 안내합니다.

사용자의 이메일이 다른 계정에서 사용되거나 사용자의 이메일이 사용되는 계정을 결정할 수 없는 경우 다음 옵션 중 하나를 선택합니다.

* 다른 계정에서 해당 항목을 삭제하고 사용자의 계정에 추가합니다(다른 계정에서 필요한 권한이 사용자 또는 사용자에게 있어야 함).
* 또는 다른 이메일 주소를 사용하여 계정에 추가합니다. 이것은 그들이 실제로 이메일을 받을 수 있는 유효한 이메일 주소여야 합니다.
* 또는 고객 성공 관리자(CSM)에게 문의하거나 [hello@appsflyer.com](mailto:hello@appsflyer.com)의 고객 성공 팀으로 이메일을 보내십시오.

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="사용자 초대 재전송">

새 사용자가 [계정 활성화 초대](/docs/user-management-for-agencies#계정-활성화-해시)를 받지 못했거나 48시간 이내에 활성화되지 않은 경우 다음과 같이 이메일을 재발송할 수 있습니다.

1. **사용자** 탭에서 사용자 행의 맨 오른쪽에 있는 **조치** 버튼 <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" />을 클릭합니다.
   * 사용자에게 아직 계정을 활성화하지 않았음을 나타내는 봉투 아이콘 ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png)이 계속 표시됩니다.
2. 메뉴에서 **이메일 초대 재전송**을 선택합니다.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="사용자의 2단계 인증(2FA) 재설정">

2FA를 사용하는 계정의 경우 사용자의 2FA를 재설정해야 하는 경우가 있을 수 있습니다. <Anchor target="_blank" href="/marketers/ko/docs/implementing-and-using-2fa-login#reset">여기</Anchor>에서 이 작업을 수행하는 방법을 참조하세요.

</Accordion>

<div data-zendesk-anchors="background=%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%97%AD%ED%95%A0-%EB%B0%8F-%EC%95%A1%EC%84%B8%EC%8A%A4-%EA%B6%8C%ED%95%9C h_01HC72J0H988V27YCTWPFGF7EP=%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%97%AD%ED%95%A0-%EB%B0%8F-%EC%95%A1%EC%84%B8%EC%8A%A4-%EA%B6%8C%ED%95%9C predefined-roles=%EC%82%AC%EC%A0%84-%EC%A0%95%EC%9D%98%EB%90%9C-%EC%97%AD%ED%95%A0 h_01HC72J0H98447W34RD0ND2MC0=%EC%82%AC%EC%A0%84-%EC%A0%95%EC%9D%98%EB%90%9C-%EC%97%AD%ED%95%A0 predefined-roles-hash=%EC%82%AC%EC%A0%84-%EC%A0%95%EC%9D%98%EB%90%9C-%EC%97%AD%ED%95%A0-%ED%95%B4%EC%8B%9C h_01HC72J0H9RVA83J9F5QN4YS79=%EC%82%AC%EC%A0%84-%EC%A0%95%EC%9D%98%EB%90%9C-%EC%97%AD%ED%95%A0-%ED%95%B4%EC%8B%9C h_01HC72J0H9Y54Q2Y6AGP6H1DG0=%EC%98%88%EC%8B%9C temp-roles%E2%80%94an-exception-to-the-rule=%EC%9E%84%EC%8B%9C-%EC%97%AD%ED%95%A0%EA%B7%9C%EC%B9%99%EC%9D%98-%EC%98%88%EC%99%B8 h_01HC72J0H9NXMKJN64C73ZXZN1=%EC%9E%84%EC%8B%9C-%EC%97%AD%ED%95%A0%EA%B7%9C%EC%B9%99%EC%9D%98-%EC%98%88%EC%99%B8 admin%E2%80%94a-special-role=%EA%B4%80%EB%A6%AC%EC%9E%90%ED%8A%B9%EC%88%98%ED%95%9C-%EC%97%AD%ED%95%A0 h_01HC72J0HANGXV4GVJCQ5X2T84=%EA%B4%80%EB%A6%AC%EC%9E%90%ED%8A%B9%EC%88%98%ED%95%9C-%EC%97%AD%ED%95%A0 account-owner-hash=%EA%B3%84%EC%A0%95-%EC%86%8C%EC%9C%A0%EC%9E%90-%ED%95%B4%EC%8B%9C h_01HC72J0HA5RFZE1G0KNKR30KV=%EA%B3%84%EC%A0%95-%EC%86%8C%EC%9C%A0%EC%9E%90-%ED%95%B4%EC%8B%9C user-management-page=%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B4%80%EB%A6%AC-%ED%8E%98%EC%9D%B4%EC%A7%80 h_01HC72J0HANQ3Z6FCWXA0TF3TN=%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B4%80%EB%A6%AC-%ED%8E%98%EC%9D%B4%EC%A7%80 users-tab=%EC%82%AC%EC%9A%A9%EC%9E%90-%ED%83%AD h_01HC72J0HAFBMYM792GXMCEY3T=%EC%82%AC%EC%9A%A9%EC%9E%90-%ED%83%AD roles-tab=%EC%97%AD%ED%95%A0-%ED%83%AD h_01HC72J0HAXC2NAVQC4J2PMB0Z=%EC%97%AD%ED%95%A0-%ED%83%AD creating-a-user=%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%83%9D%EC%84%B1 h_01HC72J0HATN656W4B9DT82M60=%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%83%9D%EC%84%B1 h_01HC72J0HAP1GDH8JKGMT6XH67=%EC%A4%91%EC%9A%94 account-activation-hash=%EA%B3%84%EC%A0%95-%ED%99%9C%EC%84%B1%ED%99%94-%ED%95%B4%EC%8B%9C h_01HC72J0HA3QJ2CH8TGEMJBY3A=%EA%B3%84%EC%A0%95-%ED%99%9C%EC%84%B1%ED%99%94-%ED%95%B4%EC%8B%9C editing-users=%EC%82%AC%EC%9A%A9%EC%9E%90-%ED%8E%B8%EC%A7%91 h_01HC72J0HAG2XF42NSYRZDEKVN=%EC%82%AC%EC%9A%A9%EC%9E%90-%ED%8E%B8%EC%A7%91 individual-editing=%EA%B0%9C%EB%B3%84-%ED%8E%B8%EC%A7%91 h_01HC72J0HAF739MQPF482T0WVA=%EA%B0%9C%EB%B3%84-%ED%8E%B8%EC%A7%91 multiuser-editing=%EB%8B%A4%EC%A4%91-%EC%9C%A0%EC%A0%80-%ED%8E%B8%EC%A7%91 h_01HC72J0HA3BKXJCAVRQ5SJYYE=%EB%8B%A4%EC%A4%91-%EC%9C%A0%EC%A0%80-%ED%8E%B8%EC%A7%91 h_01HC72J0HAZM2NBXN5ZHZET4BS=%EC%B0%B8%EA%B3%A0 h_01HC72J0HAE70AMWSDP5BXGWK9=%EC%98%88%EC%8B%9C-1 deleting-users=%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%82%AD%EC%A0%9C h_01HC72J0HAQFD33VT0ARRWG0ZF=%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%82%AD%EC%A0%9C special-situations-and-additional-procedures=%ED%8A%B9%EC%88%98-%EC%83%81%ED%99%A9-%EB%B0%8F-%EC%B6%94%EA%B0%80-%EC%A0%88%EC%B0%A8 h_01HC72J0HAF5QFC5ZR7EHFMBM6=%ED%8A%B9%EC%88%98-%EC%83%81%ED%99%A9-%EB%B0%8F-%EC%B6%94%EA%B0%80-%EC%A0%88%EC%B0%A8 h_01HC72J0HAD8JXPPFET4N2P3EK=managing-temp-roles temp-role-limitations=%EC%9E%84%EC%8B%9C-%EC%97%AD%ED%95%A0-%EC%A0%9C%ED%95%9C h_01HC72J0HA8PP79VV1F03E5AXV=%EC%9E%84%EC%8B%9C-%EC%97%AD%ED%95%A0-%EC%A0%9C%ED%95%9C h_01HC72J0HAJES0N195DZ797C4V=%EC%98%88%EC%8B%9C-2 h_01HC72J0HAVXK83AK99NQVDT8T=changing-the-account-owner h_01HC72J0HANXBK4T1SD6V2KHE4=%EC%A4%91%EC%9A%94-1 1%E2%80%93send-an-email-request=1%EC%B1%84%ED%8C%85-%EC%9C%84%EC%A0%AF%EC%9D%84-%ED%86%B5%ED%95%B4-%EC%9A%94%EC%B2%AD-%EB%B3%B4%EB%82%B4%EA%B8%B0 h_01HC72J0HAJ3C8WJ767KG2307C=1%EC%B1%84%ED%8C%85-%EC%9C%84%EC%A0%AF%EC%9D%84-%ED%86%B5%ED%95%B4-%EC%9A%94%EC%B2%AD-%EB%B3%B4%EB%82%B4%EA%B8%B0 2%E2%80%93next-steps=2%EB%8B%A4%EC%9D%8C-%EB%8B%A8%EA%B3%84 h_01HC72J0HAM13NY9EKNKG8R1CA=2%EB%8B%A4%EC%9D%8C-%EB%8B%A8%EA%B3%84 troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HC72J0HAWRBVWGVT12W6M711=troubleshooting-can-t-create-this-user h_01HC72J0HANPD39FRCWSPMRY5D=resending-a-user-invitation h_01HC72J0HARYRSXHKX41A41MPG=resetting-twofactor-authentication-2fa" />
