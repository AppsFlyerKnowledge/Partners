---
title: 광고 네트워크에 대한 Advanced Privacy 안내서 및 포스트백 매크로
metadata:
  keywords:
    - Ad Networks
    - Partners
    - ios14
    - SKAD
    - Advanced Privacy
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-07-27T07:09:37Z'
  edited_at: '2026-10-14T10:40:34Z'
  id: 360011316197
  locale: ko
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ko/articles/360011316197
---
> **요약: 요약: Advanced Privacy가 활성화된 경우 파트너와 데이터 공유를 수행할 수 있습니다. Advanced Privacy 포스트백 설정에 대한 광고 네트워크의 지침. 참고! 이 문서는 SKAdNetwork 포스트백과 관련이 없으며 광고주들이 사용하기 위한 것도 아닙니다.**

<div id="advanced-privacy-for-ad-networks-news" />

> 📄 **광고 네트워크 뉴스에 대한 Advanced Privacy**
>
> 이 문서에서 설명하는 Advanced Privacy 포스트백 메커니즘은 다음 사항이 모두 충족되는 경우에 작동합니다.
>
> * 사용자 기기는 iOS 14.5 이상입니다.
> * Advanced Privacy가 설정되어 있습니다.

![AdvancedPrivacy.png](https://files.readme.io/2a80740637c1003e03bc169df274bf0fa6240ee850c7fd6e967c4abea234e0d1-360018213598.png)

본 문서에서는 다음을 논의합니다. 

* 파트너에 대한 Advanced Privacy 데이터 공유의 영향
* 어트리뷰션 자격을 가지려면 [URL 요구 사항을 클릭하십시오.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements)
* 앱스플라이어 대시보드에서 Advanced Privacy [포스트백](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification) 설정
* [Advanced Privacy 및 SKAdNetwork](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#ap-vs-skadnetwork)사이의 차이.

<div id="ad-network-advanced-privacy-data-sharing-principles" />

## 광고 네트워크 Advanced Privacy 데이터 공유 원칙

iOS 14.5 이상부터 앱스플라이어 <Anchor target="_blank" href="/marketers/ko/docs/apply-aggregated-advanced-privacy-framework">집약형 프라이버시 강화 프레임워크</Anchor> (AAP)는 앱스플라이어 플랫폼을 통해 제공되는 사용자 수준 어트리뷰션 데이터의 가용성을 제어하는 기능을 광고주에게 제공합니다.

광고 네트워크의 맥락에서 AAP 프레임워크는 AP(Advanced Privacy)를 사용하여 구현됩니다. 쉽게 이해할 수 있도록, 이 문서에서는 Advanced Privacy 및 AP라는 용어가 상호 교환적으로 사용됩니다.

AP는 파트너 또는 광고 네트워크에 사용할 수 있는 집약형 데이터의 가용성에 영향을 주지 않습니다.

**AP의 영향을 받는 데이터**

AP가 켜져 있을 때, iOS 14.5 이상을 실행하는 비동의 사용자에 대한 사용자 수준 데이터는 포스트백 또는 Protect360 사기 관련 리포트를 포함한 다른 리포팅 방법에서는 이용할 수 없습니다.

포스트백의 경우, 이는 사용자의 ATT 동의 상태 및 다른 인자에 따라 상이한 유형의 포스트백이 사용된다는 것을 의미합니다.

 기본 설정은 켜기입니다.

![APforPartners2.png](https://files.readme.io/e4fb5617a47635f24dc83881c2be3d18b770200a576cb67bd3312e6fc2c123e1-360018154777.png)

<div id="types-of-templates-for-sending-postbacks" />

#### 포스트백을 보내기 위한 템플릿의 종류

* **일반 템플릿** 일반 템플릿: 유저 식별자 및 어트리뷰트-데이터 매크로를 포함해 앱스플라이어와 함께 제공되는 기존 연동 템플릿. 를 포함합니다. 이 템플릿은 유저 수준 어트리뷰션 데이터가 포함된 포스트백을 보내는 데 사용됩니다.
* 이 템플릿은 집약된 어트리뷰션 데이터가 포함된 포스트백을 보내는 데 사용됩니다.    
  **참고:** 참고: AP 포스트백이 필요하고 AP 통합을 완료하지 않은 경우 포스트백이 전송되지 않습니다. 셀프 서비스 포스트백 관리 도구를 사용하여 AP 연동을 설정할 수 있습니다.

<div id="note" />

> 📘 **참고사항**
>
> * 사용자가 광고주와 퍼블리셔 모두의 앱에서 ATT 동의("이중 동의")를 제공하는 경우, 정기적인 포스트백은 어트리뷰션 광고 및 비어트리뷰션 광고 네트워크로 모두 전송됩니다.
> * 예외: ASA(Apple Search Ads)에 어트리뷰션된 인스톨의 경우, ASA는 다음과 같은 조건에서 광고주에 대해 사전 개인 정보 보호가 켜져 있어도 광고 네트워크에 인스톨 포스트백을 보냅니다.
>   * 사용자가 동의하지 않는 경우
>   * 광고 네트워크에 포스트백 인스톨이 **오가닉을 포함한 모든 미디어소스**로 설정된 경우
>   * 광고 네트워크에서 Advanced Privacy를 지원하지 않는 경우

<div id="type-of-postback-used" />

### 사용된 포스트백 유형

다음 표는 iOS 14.5 이상을 실행하는 사용자의 데이터에 적용할 수 있습니다.

참고! iOS 버전이 14.4 이하라면 아래 표는 해당되지 않습니다. 즉, 일반 템플릿을 사용한 포스트백은 어트리뷰션 광고 네트워크와 비어트리뷰션 광고 네트워크 모두 전송됩니다.

<div id="postback-type-for-ios-145" />

#### iOS 14.5 이상에 대한 포스트백 유형

<table><thead><tr><th rowspan="2"><p>AP 상태</p></th><th colspan="2">ATT 상태</th><th rowspan="2">AP를 지원하는 어트리뷰트 파트너\*에 대한 백엔드 템플릿 유형  </th><th rowspan="2">AP를 지원하지 않는 어트리뷰트 파트너\*에 대한 백엔드 템플릿 유형  </th><th rowspan="2">어트리뷰트 해제된 포스트백 파트너\*</th></tr><tr><th><p>퍼블리셔 앱</p></th><th><p>광고주 앱</p></th></tr></thead><tbody><tr><td><p><span>켜짐</span></p></td><td><p><span>승인됨</span></p></td><td><p><span>승인되지 않음</span></p></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">AP 템플릿</a>(집약된 데이터)</p></td><td><p><span>포스트백 없음</span></p></td><td><p><span>없음</span></p></td></tr><tr><td><p><span>켜짐</span></p></td><td><p><span>승인되지 않음</span></p></td><td><p><span>승인됨</span></p></td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">AP 템플릿</a>(집약된 데이터)</td><td><p><span>포스트백 없음</span></p></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">일반 템플릿</a></p><p><span>어트리뷰션 필드</span> 를 사용할 수 없습니다.\*</p></td></tr><tr><td><p><span>켜짐</span></p></td><td><p><span>승인됨</span></p></td><td><p><span>승인됨</span></p></td><td><p><span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">일반 템플릿</a> </p></td><td> <span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">일반 템플릿</a> </td><td> 어트리뷰션 필드 를 사용할 수 없습니다.\* </td></tr><tr><td><p><span>켜짐</span></p></td><td><p><span>승인되지 않음</span></p></td><td><p><span>승인되지 않음</span></p></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#사용된-포스트백-유형"><span>AP 템플릿</span></a>(집약된 데이터)</p></td><td><p><span>포스트백 없음</span></p></td><td><p><span>없음</span></p></td></tr><tr><td><p><span>꺼짐</span></p></td><td><p><span>고려 안 됨</span></p></td><td><p><span>고려 안 됨</span></p></td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">일반 템플릿</a></td><td><p><span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">일반 템플릿</a></p></td><td><p><span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#포스트백을-보내기-위한-템플릿의-종류">일반 템플릿</a></p><p><span>어트리뷰션 필드</span> 를 사용할 수 없습니다.\*</p></td></tr></tbody></table>

**(\*) 파트너와의 데이터 공유에 대한 원칙**

지정된 임의의 이벤트에 대해, 다수의 광고 네트워크 파트너들은 포스트백을 가질 자격이 있습니다. 발송된 포스트백은 다음과 같습니다.

* 어트리뷰트 해제 파트너: **인앱이벤트 포스트백 >** **보내기 옵션**이 **오가닉을 포함한 모든 미디어소스**로 설정된 경우 이벤트로 대변되지 않는 연동 파트너. 만약 광고주 앱이 ATT 동의를 갖는다면, 포스트백은 어트리뷰트 데이터가 없는 사용자 ID를 포함합니다. (이 옵션은 모든 광고 네트워크에서 지원되지 않습니다.)  

  ![InAppEventAll.png](https://files.readme.io/e24037f75b2b82797031eb13d5e063b8c2006812491e69674ff066ac830919f7-35847850644881.png)

<div id="web-campaigns" />

### 웹 캠페인

광고 네트워크가 웹상에서 광고를 제공하는 경우, AP는 다른 방식으로 작동합니다.

<div id="postback-type-used-for-ios-145-when-ap-is-on" />

#### AP가 켜져 있을 때 iOS 14.5 이상에 사용되는 포스트백 유형

<table><thead><tr><th colspan="2">ATT 상태</th><th rowspan="2">어트리뷰트 참여자에 대한 포스트백 유형\*</th><th rowspan="2">어트리뷰트 해제 참여자에 대한 포스트백 유형\*</th></tr><tr><th><p>퍼블리셔 앱</p></th><th><p>광고주 앱</p></th></tr></thead><tbody><tr><td><p><span>해당 없음</span></p></td><td><p><span>승인되지 않음</span></p></td><td><p><span>프라이버시 강화 모드</span></p></td><td><p><span>없음</span></p></td></tr><tr><td><p><span>해당 없음</span></p></td><td><p><span>승인됨</span></p></td><td><p>일반  IDFA, IDFV, CUID, Click ID.</p></td><td><p>일반. 사용자 수준 ID 전용.</p></td></tr></tbody></table>

<div id="integration" />

## 연동

클릭 URL을 업데이트하고 Advanced Privacy 연동을 완료하십시오.

<div id="click-url-requirements" />

<Accordion title="클릭 URL 요구 사항">

많은 경우에, IDFA는 사용자 ATT 동의에 의존하여, 퍼블리셔 앱, 광고주 앱 또는 둘 다 모두에서 이용할 수 없을 것입니다. 이런 경우 앱스플라이어는 집약형 Advanced Privacy 및 <Anchor target="_blank" href="/marketers/ko/docs/appsflyer-attribution-model#aggregated-advanced-privacy-aap">확률적 모델링</Anchor>을 사용하여 어트리뷰션을 수행할 수 있습니다.

[모범 사례] 어트리뷰트를 최대화하기 위해 기재한 모든 파라미터를 전송합니다.

1. 다음 파라미터를 클릭 URL에 추가합니다.

<table><thead><tr><th>식별자</th><th>클릭 파라미터</th><th><p>예시</p></th></tr></thead><tbody><tr><td><p><span>캠페인</span></p></td><td><p><span>c</span></p></td><td><p><span>US_20_30</span></p></td></tr><tr><td><p><span>캠페인 ID</span></p></td><td><p><span>af_c_id</span></p></td><td><p><span>12345</span></p></td></tr><tr><td><p><span>광고세트</span></p></td><td><p><span>af_adset</span></p></td><td><p><span>ADSET_1</span></p></td></tr><tr><td><p><span>광고세트 ID</span></p></td><td><p><span>af_adset_id</span></p></td><td><p><span>56789</span></p></td></tr><tr><td><p><span>광고 </span></p></td><td><p><span>af_ad</span></p></td><td><p><span>creative_name</span></p></td></tr><tr><td><p><span>광고 ID</span></p></td><td><p><span>af_ad_id</span></p></td><td><p><span>34567</span></p></td></tr><tr><td><p><span>사이트 ID</span></p></td><td><p><span>af_siteid</span></p></td><td><p><span>abcdefgh12345678</span></p></td></tr><tr><td><p><span>하위 사이트 ID</span></p></td><td><p><span>af_sub_siteid</span></p></td><td><p><span>abcdefgh12345678</span></p></td></tr><tr><td><p><span>채널</span></p></td><td><p><span>af_채널</span></p></td><td><p><span>channel_name</span></p></td></tr><tr><td><p><span>광고 유형</span></p></td><td><p><span>af_ad_type</span></p></td><td><p><span>비디오</span></p></td></tr><tr><td><p>iOS 기기 모델\*</p></td><td><p><span>af_model</span></p></td><td><p>디바이스 모델 허용된 값:</p><ul><li>아이폰(모든 소문자)</li><li>ipad(모든 소문자)</li></ul></td></tr><tr><td><p><span>운영 체제\*</span></p></td><td><p><span>af_os</span></p></td><td><p><span>운영 체제 버전</span></p></td></tr><tr><td colspan="3"><p>\* 일부 정보는 사용자 에이전트를 통해 제공될 수도 있습니다. 이 경우 특정 식별자를 사용하여 전송된 값이 우선합니다.</p></td></tr></tbody></table>

   클릭 URL에 캠페인 세부사항 추가

   다음 예제는 클릭 URL에 캠페인 상세 정보를 추가하는 방법을 보여줍니다.

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adsetname}&af_adset_id={adset ID}&af_ad={adname}&af_ad_id={ad ID}&af_ad_type={Adtype}&af_siteid={PublisherId}` |
| --- |

2. 다음 필수 파라미터를 클릭 URL에 추가합니다.*  

   <div id="caution" />

   > ❗️ **주의**
   >
   > 클릭 URL이 필수 파라미터를 전달하지 않는 경우, 유도하는 대부분의 인스톨로 인정되지 않습니다.


   * IP
   * 사용자-에이전트

   * 앱스플라이어로 경로를 리디렉트하는 단순 HTTP 리퍼러를 사용하여 클릭을 전송할 때 조치가 필요하지 않습니다. 

   다음 방법 중 하나를 사용할 때 클릭 URL에 파라미터를 추가하는 데 설명된 추출 방법을 사용하십시오. 

   * 인앱을 통한 리디렉트
   * 서버 간 클릭(일명, S2S)

   <div id="parameters-for-advanced-privacy-attribution" />

   #### Advanced Privacy 어트리뷰션용 파라미터

   <Table>
     <thead>
       <tr>
         <th>
           파라미터
         </th>
         <th>
           필수
         </th>
         <th>
           추출 방법
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           **기기 언어 및 로케일**

           af\_lang
         </td>
         <td>
           아니요
         </td>
         <td>
           NSString *language = [[NSLocale preferredLanguages] objectAtIndex:0];

           [권장] 언어 및 로케일을 제공하십시오. 예: en-US).
         </td>
       </tr>
       <tr>
         <td>
           **유저 에이전트**

           af\_ua
         </td>
         <td>
           예
         </td>
         <td>
           다음 형식으로 사용자-에이전트를 추출합니다.

           ```
           Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+13_3_1  
           +like+Mac+OS+X%29 AppleWebKit%2F605.1.15+%28KHTML%2C  
           +like+Gecko%29+Mobile%2F15E148
           ```

           * CFNetwork **사용자 에이전트를 추출하지 *마십시오.* 다른 사용자 에이전트를 추출하십시오.**
           * 사용자 에이전트는 URL로 인코딩되어야 합니다.
         </td>
       </tr>
       <tr>
         <td>
           **디바이스 IP 주소**

           af\_ip
         </td>
         <td>
           예
         </td>
         <td>
           가능한 경우 디바이스 IP를 af\_ip 파라미터에 입력하세요.

           다음 옵션: 가능하다면 앱스플라이어는 X-Forwarded-For의 IP를 사용합니다.
         </td>
       </tr>
     </tbody>
   </Table>

   클릭 URL에 파라미터 추가

   이러한 필수 파라미터를 클릭 어트리뷰션 링크에 전달하려면 다음 참조를 사용하십시오. 

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad-type}&af_siteid={PublisherId}&af_ua={USER-AGENT}&af_lang={LANGUAGE}&af_ip={IP}` |
| --- |

   **예**

| `name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={adID}  <br />&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />`&af_ua=Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2012_1_4%20  <br />like%20Mac%20OS%20X%29%20AppleWebKit%`<br /><br />`2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%2F16D57&af_lang=en-US&af_ip=11.11.1.11` |
| --- |

   * 쿼리 파라미터는 URL로 인코딩되어야 합니다.

   **데이터를 클릭 URL 헤더에 전달하기**

   클릭 URL 헤더의 필드를 전달하려면 다음 참조를 사용하십시오.

| GET<br /><br />`accept-language: en-US,en;q=0.`<br /><br />`User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)`<br /><br />`AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148`<br /><br />`X-Forwarded-For: 11.11.1.11, 222.222.2.222` |
| --- |

</Accordion>

<div id="advanced-privacy-postback-specification" />

<Accordion title="Advanced Privacy 포스트백 사양">

**일반 템플릿과 Advanced Privacy 템플릿 간의 차이**

* 포스트백은 시간당 배치 형태로 전송됩니다.
  * 배치에는 모든 이벤트 유형이 포함됩니다.
  * 배치에는 어트리뷰션 및 거부 포스트백이 모두 포함됩니다.
  * 포스트백의 0.001%는 다음 배치로 전송될 수 있으며 최대 24시간까지 지연될 수 있습니다.
* 포스트백 시간은 실제 이벤트 시간과 상관관계가 없습니다.
* 타임스탬프 매크로:
  * 인스톨 및 인앱이벤트의 경우 타임스탬프는 발생한 시간으로 반올림됩니다. 예를 들어, 22:55:30은 22:00:00으로 리포트됩니다.
  * UTC 시간대를 사용하여 리포트됩니다. 예제 타임스탬프: (2020-07-20 20:00:00) 24,033.07

**연동할 광고 네트워크에 필요한 조치:**

1. [앱스플라이어 대시보드에서 Advanced Privacy 포스트백을 설정합니다.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback)
2. <Anchor target="_blank" href="/partners/ko/docs/ios-integration-testing-for-ad-networks">Advanced Privacy 연동 테스트.</Anchor>

<div id="important" />

> 🚧 **중요!**
>
> * 합법적인 이벤트에 대한 포스트백과 거부된 포스트백을 구분하려면 거부된 포스트백 매크로를 구성해야 합니다.
> * 거부된 인스톨/이벤트 포스트백을 활성화하려면 <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">Partner Assistant 위젯</Anchor>을 사용하여 문의하십시오.

<div id="advanced-privacy-postback-endpoint-complete-as-required" />

#### Advanced Privacy 포스트백 엔드포인트 [필요에 따라 완료]

| 포스트백 유형 |
| --- |
| 인스톨 |
| 인앱 |

<div id="advanced-privacy-attribution-macros-available" />

#### 사용 가능한 Advanced Privacy 어트리뷰션 매크로

<table><thead><tr><th><p>포스트백 매크로(이름)</p></th><th>비고</th><th>모든 포스트백의 기본 파라미터</th><th>인앱이벤트에 대한 선택적 파라미터  </th><th>거부된 어트리뷰션에 대한 선택적 파라미터</th></tr></thead><tbody><tr><td>af_ad</td><td>광고소재 이름</td><td>예</td><td> </td><td> </td></tr><tr><td>af_ad_id</td><td>34567</td><td>예</td><td> </td><td> </td></tr><tr><td>af_ad_type</td><td>예를 들면: 배너, 바닥글, 비디오</td><td>예</td><td> </td><td> </td></tr><tr><td>af_adset</td><td>ADSET_1</td><td>예</td><td> </td><td> </td></tr><tr><td>af_adset_id</td><td>56789</td><td>예</td><td> </td><td> </td></tr><tr><td>app_id</td><td>-</td><td>예</td><td> </td><td> </td></tr><tr><td>app_name</td><td>-</td><td>예</td><td> </td><td> </td></tr><tr><td>attributed_touch_hour</td><td><p>가장 가까운 시간으로 반내림.  </p><p>형식 보기(1)</p></td><td>예</td><td> </td><td> </td></tr><tr><td>attributed_touch_type</td><td>예: 클릭, 노출</td><td>예</td><td> </td><td> </td></tr><tr><td>blocked_reason</td><td>유효성 검증 규칙/Protect360과 관련됨</td><td> </td><td> </td><td>예</td></tr><tr><td>blocked_reason_value</td><td>유효성 검증 규칙/Protect360과 관련됨</td><td> </td><td> </td><td>예</td></tr><tr><td>blocked_sub_reason</td><td>유효성 검증 규칙/Protect360과 관련됨</td><td> </td><td> </td><td>예</td></tr><tr><td>bundle_id</td><td>광고주에 의해 설정된 것과 같음</td><td>예</td><td> </td><td> </td></tr><tr><td>c</td><td>캠페인 이름, 예를 들면 US_20_30</td><td>예</td><td> </td><td> </td></tr><tr><td>af_c_id</td><td>캠페인 ID, 예를 들면 12345</td><td>예</td><td> </td><td> </td></tr><tr><td>af_channel</td><td>채널명</td><td>예</td><td> </td><td> </td></tr><tr><td>country_code</td><td>전환 시에 기록된 ISO 국가 코드</td><td>예</td><td> </td><td> </td></tr><tr><td>event_hour</td><td><p>가장 가까운 시간으로 반내림.  </p><p>형식 보기(1)</p></td><td>예</td><td> </td><td> </td></tr><tr><td>event_name</td><td>앱에 의해 리포트된 바와 같음</td><td> </td><td>예</td><td> </td></tr><tr><td>event_revenue</td><td>이벤트 통화 단위 수익 금액</td><td> </td><td>예</td><td> </td></tr><tr><td>event_revenue_<br/>currency</td><td>수익 통화 코드</td><td> </td><td>예</td><td> </td></tr><tr><td>event_revenue_usd</td><td>USD로 전환된 수익</td><td> </td><td>예</td><td> </td></tr><tr><td>install_hour</td><td><p>가장 가까운 시간으로 반내림.  </p><p>형식: 일러두기 (1) 참조</p></td><td>예</td><td> </td><td> </td></tr><tr><td>is_first</td><td>특정 말단 사용자가 이 앱에서 처음으로 이 이벤트를 트리거한 경우 참</td><td> </td><td>예</td><td> </td></tr><tr><td>is_primary</td><td><p>중복 제거에 사용</p><p>Boolean 0, 1</p></td><td> </td><td>예</td><td> </td></tr><tr><td>is_retargeting</td><td><p>중복 제거에 사용 </p><p>형식: 참고 (2) 참조</p></td><td>예</td><td> </td><td> </td></tr><tr><td>is_reengagement</td><td><p>형식: 참고 (2) 참조</p></td><td> </td><td>예</td><td> </td></tr><tr><td>is_reattribution</td><td><p>중복 제거에 사용 </p><p>형식: 참고 (2) 참조</p></td><td>예</td><td> </td><td> </td></tr><tr><td>match_type</td><td>예: id_matching, probabilistic</td><td>예</td><td> </td><td> </td></tr><tr><td>event_id</td><td>광고 네트워크 플랫폼에서 해당 이벤트의 이름/ID</td><td> </td><td>예</td><td> </td></tr><tr><td>platform</td><td>예: iOS, 안드로이드</td><td>예</td><td> </td><td> </td></tr><tr><td>postback_id</td><td>고유한 포스트백 ID</td><td>예</td><td> </td><td> </td></tr><tr><td>retargeting_<br/>conversion_type</td><td>예: 리인게이지먼트, 리어트리뷰션</td><td>예</td><td> </td><td> </td></tr><tr><td>af_siteid</td><td>abcdefgh12345678</td><td>예</td><td> </td><td> </td></tr><tr><td>af_sub_siteid</td><td>abcdefgh12345678</td><td>예</td><td> </td><td> </td></tr></tbody><tfoot><tr><td colspan="5"><p>참고:</p><p>(1) 사용 가능한 타임스탬프 형식:</p><ul><li> YYYY-MM-DD HH:MM:SS</li><li> 10자리 UNIX 타임 스탬프. </li></ul><p>(2) 사용 가능한 부울 형식</p><ul><li>[기본값] 숫자: 0, 1  0, 1 </li><li>문자열: <em>false</em>, <em>true</em> </li></ul></td></tr></tfoot></table>

</Accordion>

<div id="setting-up-your-advanced-privacy-postback" />

<Accordion title="Advanced Privacy 포스트백 설정">

앱스플라이어 대시보드에서 포스트백 관리 옵션을 사용하여 AP 포스트백 설정.

**선행 조건**:

* Advanced Privacy 포스트백을 관리하려면 앱스플라이어와의 활성 연동이 있어야 합니다. 연동을 생성<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">하려면</Anchor> <Anchor target="_blank" href="/partners/ko/docs/getting-started-onboarding-guide-for-ad-networks">Partner Assistant 위젯</Anchor> 을 사용하여 당사에 문의하십시오.

**포스트백 설정 하려면:**

1. 상단 바에서 계정 메뉴(이메일 주소 드롭다운) > 계정 관리를 선택하세요.
2. 프라이버시 강화 모드:
3. 빌더를 활성화합니다.  

   ![postback-management-enter-endpoint_en-us.png](https://files.readme.io/4ea0ffc61d1ecdb11d3c745876c29a942fde4133b8ebb54a1426a73c1dc63b16-360018215218.png)
4. **엔드포인트 주소**를 입력하십시오.  설치 및/또는 인앱이벤트에 대한 해당 URL을 입력합니다.
5. 다음과 같이 포스트백에 포함할 파라미터를 입력합니다.
   * 파라미터 이름
   * **수신 파라미터**: 사용자가 받는 각각의 수신 파라미터
   * **파라미터 값**(일부 파라미터에 사용 가능): 값 형식을 선택합니다. 예를 들어, 부울 값의 경우 "true"/"false" 또는 1/0으로 값을 수신할지 여부를 선택합니다.
   * **인스톨**: 인스톨 포스트백에 파라미터를 포함하도록 상자를 선택합니다.
   * **인앱이벤트**: 인앱이벤트 포스트백에 파라미터를 포함하도록 상자를 선택합니다.

   ![postback-management-parameters_en-us.png](https://files.readme.io/818ef31df9c4e349ca26b5421a0ba0582ed5f7f9fae39f1d0e4ec3b7562f4192-360018213698.png)

   [Advanced Privacy 포스트백 매크로](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification)의 전체 목록.
6. **[선택사항]** 앱스플라이어에서 제공하지 않는 사용자정의 파라미터를 추가합니다.

   ![postback-management-custom-parameters_en-us.png](https://files.readme.io/6bca46e1d39c6822b0e041eb1dcbb1b2d40e42fa062c34877c8cbf0c2d2847d6-16589581250321.png)
7. 최종 포스트백 템플릿 미리보기를 확인하여 모든 것이 올바른지 확인하십시오.

   ![postback-management-template_en-us.png](https://files.readme.io/b5e41cad37859365c7818c4561620f8a78250c207d8326dae53ed9b522fe3716-360018213718.png)
8. **저장**을 클릭하세요. 포스트백을 저장하면 변경사항이 즉시 적용된다는 점을 알아두십시오.

문제가 있는 경우 <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">Partner Assistant 위젯</Anchor>을 사용하여 당사에 문의하십시오.

</Accordion>

<div id="additional-information" />

## 추가 정보

<div id="ap-for-analytics-partners" />

<Accordion title="분석 파트너용 AP">

다음과 같이 포스트백이 분석 파트너에게 전송됩니다.

* AP 끄기: 제한 없는 사용자 수준 포스트백.
* AP 켜기: 이 테이블에 자세히 설명한 것처럼 사용자 소스 및 ATT 상태에 따름.

<div id="analytics-partner-postback-type-according-to-att-status-and-user-source" />

#### ATT 상태 및 사용자 소스에 따른 분석 파트너 포스트백 유형

<table><thead><tr><th rowspan="2"><p>사용자 소스</p></th><th colspan="2">ATT 상태</th><th rowspan="2">분석 파트너에 대한 포스트백 유형</th></tr><tr><th><p>퍼블리셔 앱</p></th><th><p> 광고주 앱</p></th></tr></thead><tbody><tr><td rowspan="3"><p><span>논오가닉 </span></p><br/><p><span> </span></p><br/><p><span> </span></p></td><td><p><span>승인됨</span></p></td><td><p><span>승인됨</span></p></td><td>일반</td></tr><tr><td><p><span>승인되지 않음</span></p></td><td><p><span>승인됨</span></p></td><td><p>없음</p></td></tr><tr><td><p><span>모든 값</span></p></td><td><p>승인되지 않음</p></td><td>없음</td></tr><tr><td><p><span>오가닉 또는 웹</span></p></td><td>해당 없음</td><td><p>승인됨</p></td><td>일반</td></tr><tr><td><p><span>오가닉 또는 웹</span></p></td><td><p><span>해당 없음</span></p></td><td><p>승인되지 않음</p></td><td>없음</td></tr></tbody></table>

</Accordion>

<div id="ap-vs-skadnetwork" />

<Accordion title="SKAdNetwork">

<Anchor target="_blank" href="/partners/ko/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>는 iOS 기기에 대해 Apple에서 제공하는 어트리뷰션 기술입니다. Advanced Privacy는 <Anchor target="_blank" href="/marketers/ko/docs/apply-aggregated-advanced-privacy-framework">앱스플라이어의 집계된 Advanced Privacy</Anchor> (AAP) 프레임워크의 일부이며 앱스플라이어가 수행한 어트리뷰션과 관련되어 있습니다. 프레임워크는 광고주에게 앱스플라이어 플랫폼을 통해 사용자 수준 어트리뷰션 데이터의 가용성을 제어할 수 있는 기능을 제공합니다.

</Accordion>

<div data-zendesk-anchors="h_01HJR7MWPM9XA4BXHDRD2K6D56=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%89%B4%EC%8A%A4%EC%97%90-%EB%8C%80%ED%95%9C-advanced-privacy ad-network-advanced-privacy-datasharing-principles=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-advanced-privacy-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B3%B5%EC%9C%A0-%EC%9B%90%EC%B9%99 h_01HJR7MWPNYNMKZ3R8C3BB5EVG=%EA%B4%91%EA%B3%A0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-advanced-privacy-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B3%B5%EC%9C%A0-%EC%9B%90%EC%B9%99 types-of-templates-for-sending-postbacks=%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1%EC%9D%84-%EB%B3%B4%EB%82%B4%EA%B8%B0-%EC%9C%84%ED%95%9C-%ED%85%9C%ED%94%8C%EB%A6%BF%EC%9D%98-%EC%A2%85%EB%A5%98 h_01HJR7MWPN92BDJRK734P6YXSK=%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1%EC%9D%84-%EB%B3%B4%EB%82%B4%EA%B8%B0-%EC%9C%84%ED%95%9C-%ED%85%9C%ED%94%8C%EB%A6%BF%EC%9D%98-%EC%A2%85%EB%A5%98 h_01HJR7MWPN71TP0KWVVBHPC0H2=%EC%B0%B8%EA%B3%A0%EC%82%AC%ED%95%AD type-of-postback-used=%EC%82%AC%EC%9A%A9%EB%90%9C-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 h_01HJR7MWPNJEDNDT1ZY7P78HMG=%EC%82%AC%EC%9A%A9%EB%90%9C-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 postback-type-for-ios-145=ios-145-%EC%9D%B4%EC%83%81%EC%97%90-%EB%8C%80%ED%95%9C-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 h_01HJR7MWPNESP8BDC4D6Y7SBFZ=ios-145-%EC%9D%B4%EC%83%81%EC%97%90-%EB%8C%80%ED%95%9C-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 web-campaigns=%EC%9B%B9-%EC%BA%A0%ED%8E%98%EC%9D%B8 h_01HJR7MWPNXHHCSQ6BGCNRBHZK=%EC%9B%B9-%EC%BA%A0%ED%8E%98%EC%9D%B8 postback-type-used-for-ios-145-when-ap-is-on=ap%EA%B0%80-%EC%BC%9C%EC%A0%B8-%EC%9E%88%EC%9D%84-%EB%95%8C-ios-145-%EC%9D%B4%EC%83%81%EC%97%90-%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 h_01HJR7MWPNQCCNGHQY5RQHQ6D1=ap%EA%B0%80-%EC%BC%9C%EC%A0%B8-%EC%9E%88%EC%9D%84-%EB%95%8C-ios-145-%EC%9D%B4%EC%83%81%EC%97%90-%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 integration=%EC%97%B0%EB%8F%99 h_01HJR7MWPP7YGRXJQR29F3ERHH=%EC%97%B0%EB%8F%99 h_01HJR7MWPPAXK18KER56E30G8R=click-url-requirements h_01HJR7MWPPRN8XYVSS7HX7NQB9=%EC%A3%BC%EC%9D%98 parameters-for-advanced-privacy-attribution=advanced-privacy-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98%EC%9A%A9-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 h_01HJR7MWPPK2HET3XYW4WBFAZ1=advanced-privacy-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98%EC%9A%A9-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 h_01HJR7MWPQ60F4CESKRRMTQ7HX=advanced-privacy-postback-specification h_01HJR7MWPQ8K06A1YM4KV4RTN8=%EC%A4%91%EC%9A%94 advanced-privacy-postback-endpoint-%5Bcomplete-as-required%5D=advanced-privacy-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8-%ED%95%84%EC%9A%94%EC%97%90-%EB%94%B0%EB%9D%BC-%EC%99%84%EB%A3%8C h_01HJR7MWPQX9SXJZMBS6QR07WD=advanced-privacy-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8-%ED%95%84%EC%9A%94%EC%97%90-%EB%94%B0%EB%9D%BC-%EC%99%84%EB%A3%8C advanced-privacy-attribution-macros-available=%EC%82%AC%EC%9A%A9-%EA%B0%80%EB%8A%A5%ED%95%9C-advanced-privacy-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%A4%ED%81%AC%EB%A1%9C h_01HJR7MWPQKH52XMD6H9TJ0SM3=%EC%82%AC%EC%9A%A9-%EA%B0%80%EB%8A%A5%ED%95%9C-advanced-privacy-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98-%EB%A7%A4%ED%81%AC%EB%A1%9C h_01HJR7MWPRC44K908A4EAPN9GV=setting-up-your-advanced-privacy-postback additional-information=%EC%B6%94%EA%B0%80-%EC%A0%95%EB%B3%B4 h_01HJR7MWPRVFR6YN56Y0DGBAXH=%EC%B6%94%EA%B0%80-%EC%A0%95%EB%B3%B4 h_01HJR7MWPR6ACNYVZHK7YPHQGP=ap-for-analytics-partners analytics-partner-postback-type-according-to-att-status-and-user-source=att-%EC%83%81%ED%83%9C-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%86%8C%EC%8A%A4%EC%97%90-%EB%94%B0%EB%A5%B8-%EB%B6%84%EC%84%9D-%ED%8C%8C%ED%8A%B8%EB%84%88-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 h_01HJR7MWPRZDJNSZNB981WB5Z1=att-%EC%83%81%ED%83%9C-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%86%8C%EC%8A%A4%EC%97%90-%EB%94%B0%EB%A5%B8-%EB%B6%84%EC%84%9D-%ED%8C%8C%ED%8A%B8%EB%84%88-%ED%8F%AC%EC%8A%A4%ED%8A%B8%EB%B0%B1-%EC%9C%A0%ED%98%95 h_01HJR7MWPR3YR7E9S49P9ZZ3CT=ap-vs-skadnetwork" />
