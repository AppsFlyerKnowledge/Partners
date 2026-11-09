---
title: 광고 네트워크에 대한 클릭 서명
metadata:
  keywords:
    - Ad Network
    - Advertisers
    - Protect360
    - Ad Networks
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Ad Networks
    - Data Management
  created_at: '2021-02-22T09:33:52Z'
  edited_at: '2026-10-14T10:31:25Z'
  id: 360017831497
  locale: ko
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ko/articles/360017831497
---
> **한눈에 보기:** 요약: 사기 책임을 방지하기 위해 클릭에 서명 유효성 검증을 추가하면 광고 네트워크에서 부정한 클릭이 발생하지 않습니다.

<div id="about-click-signing" />

## 클릭 서명 정보

간단한 기술을 이용하여, 사기범들은 광고 네트워크를 대신하여 클릭을 전송할 수 있고, 수천 또는 심지어 수백만의 가짜 클릭을 생성하여 앱스플라이어에 전송할 수 있습니다. 광고 네트워크 자체가 이 문제를 인식하지 못하는 경우도 있습니다.

광고 네트워크가 실제로 앱스플라이어에 의해 어트리뷰트된 클릭이 가짜 클릭을 작성하는 사기범이 아니라 실제 광고 네트워크에서 클릭된 것인지 확인하기 위해, 광고 네트워크는 <Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256 서명</Anchor>을 사용하여 클릭을 서명해야 합니다.

서명은 앱스플라이어가 클릭을 검증하고 사기꾼에 의해 클릭 정보가 조작되지 않았음을 확인할 수 있게 합니다.

* 검증된 클릭은 기록되어 애드 네트워크에 귀속됩니다.
* 무효화된 클릭은 거부되며:
  * 광고 네트워크(광고주가 아님)용 Protect360 리포트에서 보실 수 있습니다. <Anchor target="_blank" href="/partners/ko/docs/protect360-reports-for-ad-networks#failed-click-signatures">더 알아보기</Anchor>
  * 전환율이나 광고 네트워크의 클릭 차단 임계값에 영향을 주지 않습니다.

<div id="click-signature-integration" />

## 클릭 서명 연동

<div id="flow" />

### 플로우

다음 차트는 초기 개발 및 기본 테스트, 생산 테스트, 마지막으로 생산까지의 흐름을 개략적으로 설명합니다.

<Image align="center" alt="Click_signing_integration_flow.png" src="https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png" />

<div id="procedure" />

### 절차

전제 조건: 필수 구성 요소: 클릭 서명 API를 인증하기 위한 관리자의 API V2.0 토큰.

클릭 서명 방법:

1. 비밀 키 생성 API로 비밀 키를 생성합니다.  
   모범 사례: 모범 사례: 유효 기간을 36시간으로 하고 24시간마다 새 비밀 키를 생성하여 사용합니다.
3. 상기 코드는 다음 정보를 클릭 URL에 추가합니다.
   * **Unix 타임스탬프(UTC로)를** 포함하는 만기 파라미터이며, 이후 광고 네트워크에서 클릭을 요청하지 않습니다.
   * HMAC-SHA256 서명.  
     예시:

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```

<div id="building-a-signature-example" />

<div id="signature-example" />

<div id="signature-algorithm" />

<div id="json-spaces" />

<div id="attribute-value-escaping" />

<div id="json-data-structure" />

<div id="empty-attributes" />

<div id="order-and-appearance-of-attributes" />

<div id="attribute-and-json-rules" />

<div id="note" />

> 📘 **참고**
>
> 클릭 서명이 생성되기 전에 링크에 특수 문자 또는 공백의 URL 인코딩이 발생하는지 확인하십시오.  서명을 먼저 생성하면 검증에 실패하게 됩니다.



| <span id="creating-a-click-signature"></span><span id="list-of-attributes"></span>순서 | 파라미터 | 필수 | 참고 |
| --- | --- | --- | --- |
| 1 | link\_domain | 예 | <ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | 예 |  |
| 3 | pid | 예 |  |
| 4 | af\_prt | 아니요 |  |
| 5 | af\_siteid | 예 |  |
| 6 | 클릭아이디 | 예 |  |
| 7 |  | 예 |  |
| 8 | af\_engagement\_type | 아니요 |  |
| 9 | af\_클릭\_룩백 | 아니요 |  |
| 10 | af\_viewthrough\_lookback | 아니요 |  |
| 11 | af\_reengagement\_window | 아니요 |  |
| 12 | 리타겟팅 여부 | 아니요 |  |
| 13 | af\_ip | 아니요 |  |
| 14 | advertising\_id | 아니요 |  |
| 15 | oaid | 아니요 |  |
| 16 | fire\_advertising\_id | 아니요 |  |
| 17 | idfa | 아니요 |  |
| 18 | idfv | 아니요 |  |





* * 예시:   
    `[["key-1","value-1"],["key-2","value-2"]...["key-n","value-n"]]`




```json
//generate a signature from the click url and encode it with base64 without padding String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(jsonString.getBytes()));
```


```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&clickid=sdkfjasksjskdfj9845weh&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615
```

```json
[
	["link_domain","yourbrand.onelink.me"],
	["link_path","qswl"],
	["pid","mediasource_int"],
	["af_siteid","my_site"],
	["clickid","12345"],
	["expires","1689695615"]
]
```

```json
[["link_domain","yourbrand.onelink.me"],["link_path","qswl"],["pid","mediasource_int"],["template-id","qswl"],["af_siteid","my_site"],["clickid","12345"],["expires","1689695615"]]
```

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615  
&signature_v2=WIfCmfLAPSsVrBTqCqfihMeLCnbE4dIAlhHF84WsiWA
```


<div id="code-examples" />

### 코드 예

<div id="signingsupportedparamsjson" />

<Accordion title="signing-supported-params.json">

```json
[
  {"index":1, "name":"pid", "mandatory":true},
  {"index":2, "name":"af_prt", "mandatory":false},
  {"index":3, "name":"af_siteid", "mandatory":true},
  {"index":4, "name":"clickid", "mandatory":true},
  {"index":5, "name":"expires", "mandatory":true},
  {"index":6, "name":"af_engagement_type", "mandatory":false},
  {"index":7, "name":"af_click_lookback", "mandatory":false},
  {"index":8, "name":"af_viewthrough_lookback", "mandatory":false},
  {"index":9, "name":"af_reengagement_window", "mandatory":false},
  {"index":10, "name":"is_retargeting", "mandatory":false},
  {"index":11, "name":"af_ip", "mandatory":false},
  {"index":12, "name":"advertising_id", "mandatory":false},
  {"index":13, "name":"oaid", "mandatory":false},
  {"index":14, "name":"fire_advertising_id", "mandatory":false},
  {"index":15, "name":"idfa", "mandatory":false},
  {"index":16, "name":"idfv", "mandatory":false}
]
```

</Accordion>

<div id="signatureexamplego" />

<Accordion title="signature-example.go">

```json
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/url"
	"os"
	"strings"
	"time"
)

type Param struct {
	Name      string
	Mandatory bool
}

func LoadSupportedParams() ([]Param, error) {
	path := "./signing-supported-params.json"
	jsonFile, _ := os.Open(path)
	defer jsonFile.Close()
	byteValue, err := io.ReadAll(jsonFile)
	if err != nil {
		return nil, errors.New("failed loading " + path)
	}
	var params []Param
	_ = json.Unmarshal(byteValue, &params)
	return params, nil
}

func computeHmac256(message, secret string) (res string, errResult error) {
	defer func() {
		if r := recover(); r != nil {
			errResult = r.(error)
			fmt.Println("failed to invoke ComputeHmac256. err: %+v", errResult)
			res = ""
			return
		}
	}()

	key := []byte(secret)
	h := hmac.New(sha256.New, key)
	h.Write([]byte(message))
	return base64.URLEncoding.WithPadding(base64.NoPadding).EncodeToString(h.Sum(nil)), nil
}

// this function accepts a click url, a ttl for the click in seconds, and the list of supported params
// the function:
// 1. adds the expiration to the click based on the provided ttl
// 2. builds a json for the signature
// 3. create an HMAC256 signature
// 4. adds the signature to the click url
func signURLV2(originalURL string, secret string, clickTtlSeconds int64, supportedParams []Param) (signedURL string, err error) {

	//add an expiration to the click
	expires := time.Now().UTC().Unix() + clickTtlSeconds
	urlWithExpired := fmt.Sprintf("%s%s%d", originalURL, "&expires=", expires)

	//parse the url
	parsedURL, err := url.Parse(urlWithExpired)
	if err != nil {
		return "", errors.New("failed parsing URL")
	}

	//build a json from the url
	jsonStr, err := buildJSONFromURLV2(parsedURL, supportedParams)
	if err != nil {
		return "", err
	}

	//create a signature
	signatureV2, err := computeHmac256(jsonStr, secret)
	if err != nil {
		fmt.Println("Failed to computeHMAC256 for url %s. err: %+v", jsonStr, err)
		return "", errors.New("fail to computeHMAC256 for url")
	}

	//add the signature to the url
	signedURL = fmt.Sprintf("%s%s%s", urlWithExpired, "&signature_v2=", signatureV2)

	return signedURL, nil

}

// this function builds a json from a given click url.
// It returns a string representation of the json ready to be signed.
func buildJSONFromURLV2(parsedURL *url.URL, supportedParams []Param) (string, error) {
	//initiate an empty json in the structure [[key-1,val-1],[key-2,val-2]...[key-n,val-n]]
	var jsonData [][2]string

	//add the url host domain to the json
	domain := parsedURL.Host
	param := [2]string{"link_domain", domain}
	jsonData = append(jsonData, param)

	//add the path (app-id or template-id) to the json
	path := parsedURL.Path
	if len(path) > 1 {
		param := [2]string{"link_path", path[1:]}
		jsonData = append(jsonData, param)
	}

	//loop over the ordered list of supported parameters and add them to the json
	for i := 0; i <len(supportedParams); i++ {name := supportedParams[i].Name val := parsedURL.Query().Get(name) if len(val) > 0 {
			param := [2]string{name, val}
			jsonData = append(jsonData, param)
		} else if supportedParams[i].Mandatory {
			return "", errors.New("missing mandatory param: " + name)
		}
	}

	//generate string representation of the json object
	jsonObj, _ := json.Marshal(jsonData)
	return strings.ToLower(string(jsonObj)), nil
}

func main() {

	supportedParams, err := LoadSupportedParams()
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}

	var secretKey = "tqJU4Qd/eFTEWfqW7KCG9asDO0bmZoFzv8GY3VPSPAM="
	var clickTtlSeconds int64 = 60
	var originalUrl = "https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012&clickid=1234&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign"

	fmt.Println("Original URL: ", originalUrl)

	signedUrl, err := signURLV2(originalUrl, secretKey, clickTtlSeconds, supportedParams)
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	} else {
		fmt.Println("Signed URL: ", signedUrl)
	}
}
```

</Accordion>

<div id="click-signature-apis" />

## 클릭 서명 API

앱스플라이어는 광고 네트워크가 클릭 서명 프로세스를 관리하고 테스트하는 데 사용할 수 있는 API를 제공합니다. 아래 표의 API 목록과 API 사용에 필요한 정보가 포함된 섹션을 참조하십시오.

<div id="click-signature-apis-1" />

#### 클릭 서명 API

| API 메서드 | 비고 |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">비밀 키를 생성합니다.</Anchor> | 서명에 사용할 비밀 키를 생성합니다. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">비밀 키를 취소합니다.</Anchor> | 손상된 비밀 키를 취소합니다. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">실험군</Anchor> | 단일 클릭을 서명 테스트를 위해 전송합니다. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">설정 모드</Anchor> | 클릭 서명 모드의 설정 모드:<ul><li>이를 통해 프로덕션 및 실제 트래픽에 영향을 주지 않고 클릭 서명을 테스트합니다.</li><li>**활성화됨** 사용 가능: 앱스플라이어는 서명이 유효하지 않거나 누락되면 클릭을 차단합니다./strong></li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-circuit-breaker-put">회로 차단기 설정</Anchor> | 광고 네트워크에 너무 많은 차단 클릭이 들어오는 것을 보호하는 회로 차단기의 모드를 설정합니다.<ul><li>사용 가능(기본값): Protect360 시스템에서 너무 많은 클릭이 유효하지 않은 것으로 표시되는 경우 광고 네트워크에서 클릭이 잘못 차단되지 않도록 보호하려면 다음을 수행합니다.<ul><li>모드 API 변경 사항을 리포트 전용으로 설정합니다.</li><li>그리고 클릭 서명 API가 올바르게 설정되어 있는지 확인하기 위한 이메일 알림이 광고 네트워크로 전송됩니다.</li></ul></li><li>비활성화 완료 사용 안 함: Protect360은 차단 비율이 비정상적으로 높은 경우에도 유효하지 않은 것으로 표시된 모든 클릭을 계속 차단합니다.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">설정 가져오기</Anchor> | 활성 비밀 키의 모드와 ID를 가져옵니다. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">보고서</Anchor> | 시스템이 리포트 전용 모드 또는 **사용가능** 모드일 때 성공 클릭 및 실패 클릭에 대한 통계 가져오기. 이를 통해 프로덕션 및 실제 트래픽에 영향을 주지 않고 클릭 서명을 테스트합니다. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">앱 제외</Anchor> | 클릭 서명에서 제외할 앱 ID를 구성합니다. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">제외된 앱 삭제</Anchor> | 앱 ID가 제외된 후 서명 클릭에 포함되도록 구성합니다. |


<div id="legacy-versions" />

<div id="v1-legacy" />

<Accordion title="V1(레거시)">

<div id="generate-secret-key-method" />

### 비밀 키 메서드 생성

<div id="generate-secret-key-basics" />

<Accordion title="비밀 키 베이직 생성">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>POST</code></td></tr><tr><td>경로</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>"}</code></span></td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>비밀 키는 JSON 형식으로 반환됩니다.</td></tr><tr><td> </td><td>요청 제한</td><td>활성 비밀 키는 한 번에 최대 2개입니다.</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="API 요청">

**방법**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

<div id="parameters" />

#### 파라미터

| 파라미터 | 설명 |
| --- | --- |
| ttlHours | <ul><li>비밀 키를 사용할 수 있는 시간, 1-1440시간.</li><li>기본값은 36시간입니다.</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="JSON 응답">

| **키** | **설명** |
| --- | --- |
| secret-key-id | 비밀 키용 ID |
| Secret key | 클릭 서명을 위한 비밀 키 |
|  | 밀리초 단위의 에포크(Epoch) 시간 |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="비밀 키 컬 예시와 응답을 생성합니다.">

**컬 요청**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON 응답**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="HTTP 응답 코드">

<div id="response-codes" />

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="revoke-secret-key-method" />

### 비밀 키 메서드 취소

<div id="revoke-secrete-key-basics" />

<Accordion title="비밀 키 베이직 취소합니다">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>DELETE</code></td></tr><tr><td>경로</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>"}</code></span></td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>비어있음</td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<Accordion title="API 요청">

**방법**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

<div id="parameters-1" />

#### 파라미터

| 파라미터 | 설명 |
| --- | --- |
| secret-id | 취소할 비밀 키의 ID |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="비밀 키 컬 예시와 응답을 생성합니다.">

**컬 요청**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="HTTP 응답 코드">

<div id="response-codes-1" />

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="test-method" />

### 테스트 방법

<div id="test-basics" />

<Accordion title="테스트 기본">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>POST</code></td></tr><tr><td>경로</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/test</span></td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>JSON 형식으로 반환</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="API 요청">

**방법**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

<div id="parameters-2" />

#### 파라미터

| 파라미터 | 설명 |
| --- | --- |
| URL | 테스트할 클릭 URL(서명 포함) |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="JSON 응답">

| **키** | **설명** |
| --- | --- |
|  | 통과 또는 실패함 |
| 메시지 | 테스트 실패 이유. 예를 들어:<ul><li>서명 누락</li><li>유효하지 않은 서명</li><li>만료됨</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="컬 예시 및 응답 테스트">

**컬 요청**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**JSON 응답**

```json
{
	"test-status":"Passed / Failed",
	"message": "Invalid signature"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="HTTP 응답 코드">

<div id="response-codes-2" />

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="configure-mode-method" />

### 모드 메서드 설정

<div id="configure-mode-basics" />

<Accordion title="모드 베이직 설정합니다">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>POST</code></td></tr><tr><td>경로</td><td> <span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>mode/&lt;mode&gt;</strong></span></span> </td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>JSON 형식으로 반환</td></tr></tbody></table>

</Accordion>

<Accordion title="API 요청">

**방법**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

<div id="parameters-3" />

#### 파라미터

| 파라미터 | 설명 |
| --- | --- |
| 모드 | 옵션:<ul><li>활성화 완료<br />**참고!** 몇 시간 동안 리포트 전용 모드로 실행한 후에만 모드를 "사용 가능"으로 설정하고 모든 클릭이 서명 유효성 검사를 통과했는지 리포트를 확인하십시오.</li><li>비활성화 완료</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="모드 컬 예시 설정합니다">

**컬 요청**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<Accordion title="HTTP 응답 코드">

<div id="response-codes-3" />

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 400 | 잘못된 요청 | 유효하지 않은 모드 |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="configure-circuit-breaker-method" />

### 회로 차단기 메서드 설정

<div id="configure-circuit-breaker-basics" />

<Accordion title="회로 차단기 베이직 설정">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>POST</code></td></tr><tr><td>경로</td><td><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td><span>HTTP 상태</span></td></tr></tbody></table>

</Accordion>

<div id="api-request::ef73eae0" />

<Accordion title="API 요청">

**방법**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```

<div id="request-body-json" />

#### 요청 본문 JSON

| 파라미터 | 설명 |
| --- | --- |
| 상태 | <ul><li>활성화 완료</li><li>비활성화 완료</li></ul> |

</Accordion>

<div id="configure-circuit-breaker-curl-example-and-response" />

<Accordion title="회로 차단기 컬 예시 및 응답 설정">

**컬 요청**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
```

</Accordion>

<div id="http-response-codes::d35e3a62" />

<Accordion title="HTTP 응답 코드">

<div id="response-codes-4" />

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 400 | 잘못된 요청 | 유효하지 않은 상태 |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="response-codes-5" />

<div id="get-configuration-method" />

### 설정 메서드 가져오기

<div id="get-configuration-basics" />

<Accordion title="설정 베이직 가져오기">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>GET</code></td></tr><tr><td>경로</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config</span></td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>JSON 형식으로 반환</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<Accordion title="API 요청">

**방법**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="JSON 응답">

| **키** | **설명** |
| --- | --- |
| 모드 | 다음 중 한 개:<ul><li>활성화 완료</li><li>비활성화 완료</li></ul> |
| circuit-breaker-config | 다음 중 하나의 상태를 포함하는 JSON 개체:<ul><li>활성화 완료</li><li>비활성화 완료</li></ul> |
| active-key-ids | 활성 키를 담고 있는 JSON 배열:<ul><li>**secret-key-id**:</li><li>만료: 밀리초 단위의 비밀 키의 에포크 시간</li></ul> |
| excluded-app-ids | app-ids를 배제한 JSON 배열 |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="설정 컬 예시 및 응답 가져오기">

**컬 요청**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON 응답**

```json
{
	"mode": "report-only",
	"active-key-ids": [
		{
			"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
			"expiration": 1610533263
		}
	],
	"excluded-app-ids": [
		"app-id-1", 	"app-id-2"
	]

}
```

</Accordion>

<div id="http-response-codes::90a409c" />

<Accordion title="HTTP 응답 코드">

<div id="response-codes-7" />

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="report-method" />

### 리포트 메서드

<div id="report-basics" />

<Accordion title="리포트 베이직">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>GET</code></td></tr><tr><td>경로</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/report</span></td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>CSV 형식으로 반환</td></tr></tbody></table>

</Accordion>

<div id="api-request::b28cedb0" />

<Accordion title="API 요청">

**방법**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

<div id="response-codes-6" />

<div id="parameters-4" />

#### 파라미터

<table><thead><tr><th>파라미터</th><th>설명</th></tr></thead><tbody><tr><td>시작날짜</td><td>리포트 시작 날짜 및 시간. 형식: yyyy-mm-ddThh</td></tr><tr><td>종료일.</td><td>리포트 마감 날짜 및 시간. 형식: yyyy-mm-ddThh</td></tr><tr><td colspan="2">API를 사용하려면 시작 날짜와 마감 날짜가 <span>모두</span> 필요하거나 둘 <strong>다</strong> 필요하지 않습니다. 시작/마감 날짜가 제공되지 않으면 리포트는 지난 24시간 동안의 결과를 표시합니다.</td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="CSV 응답">

| **열** | **설명** |
| --- | --- |
| 시간 | 클릭의 날짜 및 시간. 형식: yyyy-mm-ddThh |
| total\_clicks | 리포트 기간 동안 총 클릭 수 |
| valid\_clicks | 리포트 기간 동안 유효한 클릭 수 |
| missing\_signature | 리포트 기간 동안 서명이 누락된 클릭 수 |
| expired\_clicks | 리포트 기간 동안 만료된 클릭 수 |
| invalid\_signature | 리포트 기간 동안 유효하게 서명한 클릭 수 |
| no\_active\_secrets | 시스템에 활성 비밀 키가 없기 때문에 거부된 클릭 수(일반적으로 시스템이 리포트 전용 모드인 경우) |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="컬 예시 및 응답 테스트">

**컬 요청**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/report?start-date=2021-01-07T07&end-date=2021-01-17T12' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**CSV 응답**

| **시간** | **total\_clicks** | **valid\_clicks** | **missing\_signature** | **expired\_clicks** | **invalid\_signature** | **no\_active\_signatures** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<div id="http-response-codes::8454f45d" />

<Accordion title="HTTP 응답 코드">

<div id="response-codes-8" />

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="exclude-app-method" />

### 앱 메서드 제외

<div id="exclude-app-method-basics" />

<Accordion title="앱 메서드 베이직 제외">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>POST</code></td></tr><tr><td>경로</td><td> </td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>비어있음</td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::1054abca" />

<Accordion title="API 요청">

**방법**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-5" />

#### 파라미터

| 파라미터 | 설명 |
| --- | --- |
| app-id | 클릭 서명 유효성 검증에서 제외된 애플리케이션 ID |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="앱 컬 예시 제외">

**컬 요청**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7991b66" />

<Accordion title="HTTP 응답 코드">

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="remove-excluded-app-method" />

### 제외된 앱 메서드 삭제

<div id="remove-excluded-app-method-basics" />

<Accordion title="제외된 앱 메서드 베이직 삭제">

<table><thead><tr><th>카테고리</th><th>항목</th><th><span>설명</span></th></tr></thead><tbody><tr><td rowspan="3">요청</td><td>HTTP 메서드</td><td><code>DELETE</code></td></tr><tr><td>경로</td><td> </td></tr><tr><td>권한 관리 헤더  </td><td><ul><li>필수 권한 관리 헤더에는 Bearer 토큰이 포함되어 있습니다.  </li><li>   </li></ul></td></tr><tr><td>응답</td><td>결과</td><td>비어있음</td></tr></tbody></table>

</Accordion>

<div id="api-request::9504d16f" />

<Accordion title="API 요청">

**방법**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-6" />

#### 파라미터

| 파라미터 | 설명 |
| --- | --- |
| app-id | 클릭 서명 유효성 검증에서 제외된 앱 목록에서 제거할 애플리케이션 ID |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="제외된 앱 컬 예시 삭제">

**컬 요청**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b5e059da" />

<Accordion title="HTTP 응답 코드">

#### 응답 코드

| 코드 | 메시지 | 비고 |
| --- | --- | --- |
| 200 | 정상 |  |
| 401 | 승인되지 않음 | 유효하지 않거나 누락된 권한 관리 헤더 |

</Accordion>

<div id="code-sample" />

<Accordion title="코드 샘플">

```java
package sign;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

.
.
.

String clickUrl = "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345";
String secretKey = "secret_key"; 
int ttlMinutes = 5;

//add expiration to the click URL
long expiration = System.currentTimeMillis() + (60000L * ttlMinutes);
clickUrl += "&expires="+expiration;

//create a SecretKey object from the given key string
SecretKeySpec signingKey = new SecretKeySpec(secretKey.getBytes(), "HmacSHA256");
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(signingKey);

//generate a signature from the click url and encode it with base64 without padding
String generatedSignature =     
Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(clickUrl.getBytes()));

//add the signature to the click URL
String signedClickUrl = clickUrl + "&signature=" + generatedSignature;
```

</Accordion>

</Accordion>

<div id="additional-information" />

## 추가 정보

<div id="troubleshooting" />

<Accordion title="문제 해결">

앱스플라이어는 한 시간 동안 90% 이상의 클릭이 서명 유효성 검증에 실패하면 서명 유효성 검증을 중지하고 리포트 전용 모드로 돌아갑니다.

목적은 잠재적인 기술적 문제로부터 비즈니스를 보호하기 위한 것이며 이를 통해 다음과 같은 이상의 원인을 찾을 수 있습니다.

* 서명이 예상대로 작동하고 클릭이 올바르게 차단되는 경우 회로 차단기 설정 방법을 사용하여 회로 차단기를 비활성화합니다.
* 상기 클릭이 올바르게 차단되지 않은 경우:
  1. [설정 가져오기 방법을 사용하여 클릭 서명 설정을 검사하여](/docs/click-signing-for-ad-networks#설정-메서드-가져오기) 유효한 비밀 키가 있는지 확인합니다.
  2. [클릭 서명 리포트](/docs/click-signing-for-ad-networks#리포트-메서드)를 사용하여 차단된 클릭에 대한 자세한 정보를 얻고 잘못된 클릭의 출처(에이전시/앱- ID)와 이유를 조사합니다.
* 비표준 연동으로 인해 특정 앱에서 문제가 발견되면 앱 제외 API를 사용하여 서명 유효성 검증을 클릭하지 않도록 [이 앱을 제외합니다.](/docs/click-signing-for-ad-networks#앱-메서드-제외)
* 설정에서 문제가 발견된 경우:
  1. 리포트 전용 모드에서 실행을 계속합니다.
  2. 사용자 쪽에서 클릭 서명 프로세스를 수정합니다.
  3. [클릭 서명 리포트에서](/docs/click-signing-for-ad-networks#리포트-메서드) 결과를 확인하고 클릭의 유효성을 예상대로 검증되는 경우 클릭 서명 유효성 검사를 다시 사용하도록 설정합니다.

</Accordion>

<div id="faq" />

<Accordion title="자주 묻는 질문">

| **질문: 질문: 프로덕션에 영향을 주지 않고 어떻게 클릭 서명을 테스트합니까?**<br /><br />**답변**: 답변: 클릭 서명을 테스트하는 방법에는 두 가지가 있습니다.<ol><li>테스트 API 사용. 이 방법은 개발 단계에서 단일 클릭 서명을 테스트하는 데 유용합니다.</li><li>리포트 전용 모드 사용. 리포트 전용 모드는 프로덕션 클릭에 대한 서명을 확인하고 차단할 항목을 표시하지만 잘못된 클릭을 차단하지는 않습니다. 따라서 실제 트래픽에 영향을 주지 않고 클릭 서명이 작동하는지 테스트할 수 있습니다.</li></ol> |
| --- |
| **질문: 질문: API 토큰과 비밀 키의 차이점은 무엇입니까?**<br /><br />**답변**: api\_token<br /><br />Secret key |
| **질문: 질문: 클릭 서명을 특정 캠페인에만 적용할 수 있나요?**<br /><br />**답변**: |

</Accordion>

<div id="traits" />

<Accordion title="특성">

| 특징 | 설명 |
| --- | --- |
| 클릭 서명 | 서명은 광고 네트워크 서버에 표시되어야 합니다. |
| Secret key | <ul><li>광고 네트워크에는 최대 두 개의 비밀 키가 동시에 활성화될 수 있습니다.</li><li>각 비밀 키에는 만료 기간이 있습니다.</li><li>만료된 비밀 키로 서명한 클릭은 거부됩니다.</li></ul> |
| 리포트 API | 클릭 유효성에 대한 업데이트된 통계는 매시간 집계됩니다. |

</Accordion>

<div data-zendesk-anchors="about-click-signing=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-%EC%A0%95%EB%B3%B4 h_01HNWC70BPGDJAG3X8M5Z2RHQ4=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-%EC%A0%95%EB%B3%B4 click-signature-integration=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-%EC%97%B0%EB%8F%99 h_01HNWC70BPFYMZ56GTPV3W6DXA=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-%EC%97%B0%EB%8F%99 flow=%ED%94%8C%EB%A1%9C%EC%9A%B0 h_01HNWC70BPMXTKF9NZBYGCB874=%ED%94%8C%EB%A1%9C%EC%9A%B0 procedure=%EC%A0%88%EC%B0%A8 h_01HNWC70BPHCAGD1ECA56CC1Q6=%EC%A0%88%EC%B0%A8 h_01HNWC70BPAR4QNTNSFE1JZM2J=%EC%B0%B8%EA%B3%A0 h_01HP4A42YYFFF6M4VEH84KRTTK=list-of-attributes h_01HNWD3XYWFRY262HZZVAVWACR=list-of-attributes attribute-rules=%EC%B0%B8%EA%B3%A0 order-and-appearance-of-attributes=%EC%B0%B8%EA%B3%A0 empty-attributes=%EC%B0%B8%EA%B3%A0 json-data-structure=%EC%B0%B8%EA%B3%A0 h_01HNWE3A19RM7757B707TWZ6G0=%EC%B0%B8%EA%B3%A0 h_01HNWE3A1920YQGZX2VG4X3M4B=%EC%B0%B8%EA%B3%A0 h_01HNYRZ1DPDDQ5H8RFYKAQWVKP=%EC%B0%B8%EA%B3%A0 h_01HNYS6R7F0MNPBN08TXKQS5DV=%EC%B0%B8%EA%B3%A0 attribute-value-escaping=%EC%B0%B8%EA%B3%A0 json-spaces=%EC%B0%B8%EA%B3%A0 signature-algorithm=%EC%B0%B8%EA%B3%A0 h_01HNYSEBGD1DBSV2MHS7DZ75HS=%EC%B0%B8%EA%B3%A0 h_01HNYSY42HS1RXFG7T7QS9B0TK=%EC%B0%B8%EA%B3%A0 h_01HNYSJDFWAM9RREYH4M8DZQJA=%EC%B0%B8%EA%B3%A0 signature-example=%EC%B0%B8%EA%B3%A0 h_01HP3YAN03BWVA30JP1JAFZYAG=%EC%B0%B8%EA%B3%A0 code-example=%EC%BD%94%EB%93%9C-%EC%98%88 h_01HNYT8Z33M69JAS72MQ03YX0M=%EC%BD%94%EB%93%9C-%EC%98%88 h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego click-signature-apis=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-api h_01HNWC70BPNEVT00S040TQ9KVD=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-api click-signature-apis::58bf03c7=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-api-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=%ED%81%B4%EB%A6%AD-%EC%84%9C%EB%AA%85-api-1 h_01HNZ3YMFRWFDY751EBA58V6Q0=legacy-versions h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy generate-secret-key-method=%EB%B9%84%EB%B0%80-%ED%82%A4-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%83%9D%EC%84%B1 h_01HNWC70BPBPSX1WKJJC2W6H69=%EB%B9%84%EB%B0%80-%ED%82%A4-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%83%9D%EC%84%B1 h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request parameters=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 h_01HNWC70BPS83JD78JWQYK1NX9=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes response-codes=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C h_01HNWC70BPMQ8Q94JD5CBT5RHZ=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C revoke-secret-key-method=%EB%B9%84%EB%B0%80-%ED%82%A4-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%B7%A8%EC%86%8C h_01HNWC70BP8V05Q04J6EVGAS9T=%EB%B9%84%EB%B0%80-%ED%82%A4-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%B7%A8%EC%86%8C h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-1 h_01HNWC70BPQ5S06E210RTE7E6R=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-1 h_01HNWC70BPN18MB98KWND886QN=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-1 test-method=%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%B0%A9%EB%B2%95 h_01HNWC70BPKEVRDMT8N4HMC98W=%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%B0%A9%EB%B2%95 h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-2 h_01HNWC70BPKQFVEGWR9QT566YX=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-2 h_01HNWC70BPC43F5H85F56DDSQR=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-2 configure-mode-method=%EB%AA%A8%EB%93%9C-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%84%A4%EC%A0%95 h_01HNWC70BP6NPF7NSF0MGA4BJ3=%EB%AA%A8%EB%93%9C-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%84%A4%EC%A0%95 h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-3 h_01HNWC70BQZ657X25N8JGM57A1=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-3 configure-circuit-breaker-method=%ED%9A%8C%EB%A1%9C-%EC%B0%A8%EB%8B%A8%EA%B8%B0-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%84%A4%EC%A0%95 h_01HNWC70BQVSFS7G330NF4XHEP=%ED%9A%8C%EB%A1%9C-%EC%B0%A8%EB%8B%A8%EA%B8%B0-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%84%A4%EC%A0%95 h_01HNWC70BQ097J2VXW0XKSH3M9=configure-circuit-breaker-basics h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 request-body-json=%EC%9A%94%EC%B2%AD-%EB%B3%B8%EB%AC%B8-json h_01HNWC70BQ6R955776Y6H4EZRG=%EC%9A%94%EC%B2%AD-%EB%B3%B8%EB%AC%B8-json h_01HNWC70BQRZEZ4PTV59FGYS4Z=configure-circuit-breaker-curl-example-and-response h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-4 get-configuration-method=%EC%84%A4%EC%A0%95-%EB%A9%94%EC%84%9C%EB%93%9C-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0 h_01HNWC70BQZY6TYSQBWZ17S0W5=%EC%84%A4%EC%A0%95-%EB%A9%94%EC%84%9C%EB%93%9C-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0 h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-5 h_01HNWC70BQDGVBZ94F0N49FF40=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-5 report-method=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EB%A9%94%EC%84%9C%EB%93%9C h_01HNWC70BQTBMNKHV4RH4ZQ0AE=%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EB%A9%94%EC%84%9C%EB%93%9C h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-6 h_01HNWC70BQTPPWA4SNG25E8FFB=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-6 exclude-app-method=%EC%95%B1-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%A0%9C%EC%99%B8 h_01HNWC70BQ9SK2XCBGGHXVMRDV=%EC%95%B1-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%A0%9C%EC%99%B8 h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-5 h_01HNWC70BREG4XQJV3X9518FC5=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-5 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-7 h_01HNWC70BRN8BHWF6WGY2RH45X=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-7 remove-excluded-app-method=%EC%A0%9C%EC%99%B8%EB%90%9C-%EC%95%B1-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%82%AD%EC%A0%9C h_01HNWC70BR18P0H96VN64RS05G=%EC%A0%9C%EC%99%B8%EB%90%9C-%EC%95%B1-%EB%A9%94%EC%84%9C%EB%93%9C-%EC%82%AD%EC%A0%9C h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-6 h_01HNWC70BR4ADH7T3AFG58FZH6=%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=%EC%9D%91%EB%8B%B5-%EC%BD%94%EB%93%9C-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample additional-information=%EC%B6%94%EA%B0%80-%EC%A0%95%EB%B3%B4 h_01HNWC70BRN0NGTQVWED6VG81Y=%EC%B6%94%EA%B0%80-%EC%A0%95%EB%B3%B4 h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
