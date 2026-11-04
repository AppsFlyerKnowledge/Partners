---
title: 广告平台的点击签名指南
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
  edited_at: '2026-10-14T10:00:12Z'
  id: 360017831497
  locale: zh-cn
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/zh-cn/articles/360017831497
---
> **概要：** 广告平台可以在点击中添加签名验证，这样作弊点击就不会被归因到该渠道，避免承担作弊风险。

<div id="about-click-signing" />

## 点击签名简介

作弊分子能够凭借极低的技术成本，以广告平台的名义生成上千甚至上百万的虚假点击，并将其发送到AppsFlyer。有些情况下，广告平台本身也不知情。

为了确保AppsFlyer归因到某个平台的点击确实来自该平台，而非作弊平台生成的虚假点击，建议广告平台在其点击中使用<Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256签名</Anchor>。

点击签名还能帮助广告平台避免点击撞库导致的流量截断（capping）。这个机制会在广告平台出现极端水平的点击撞库并到达capping阈值时，停止AppsFlyer当天对其点击的记录和归因。

AppsFlyer可以通过这类签名来验证广告平台的点击，并确保点击信息不被作弊分子篡改。

* 经过验证的点击会被记录到AppsFlyer，并归因到相关的广告平台。
* 未通过验证的点击会被拦截，并且：
  * 相关数据会通过Protect360报告提供给广告平台（而非广告主）。<Anchor target="_blank" href="/partners/zh/docs/protect360-reports-for-ad-networks#failed-click-signatures">详情请见此处说明。</Anchor>
  * 不会影响该广告平台的转化率或点击截断（capping）的阈值。

<div id="click-signature-integration" />

## 点击签名的接入方式

<div id="flow" />

### 链路

下图简要说明了点击签名从初始开发和基础测试到生产环境测试，最后正式上线的整条链路。

![](https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png) altClick\_signing\_integration\_flow.png

<div id="procedure" />

### 流程

前期准备：**需要让您的账户管理员提供API V2.0 token，用于点击签名API的授权。**

**点击签名的部署方式如下：**

1. 使用Generate secret key API生成一个密钥（secret key）。  
   推荐方法：每24小时生成一个新的secret key并投入使用，每个key的有效期为36小时。
2. 在您的服务器中编写相关代码，用于调用Generate secret key API，从而获取secret key并生成HMAC-SHA256签名。详情请参见代码示例。  
   此外，您还可以使用下文表格中列出的其他API。
3. 该代码会在您的点击链接中添加以下内容：
   * **expires**参数，用于表达secret key的过期时间，其中包含一个Unix时间戳（UTC时区），过期后相关平台就不再认领该点击。
   * 举例来说，

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```

<div id="note" />

> 📘 **注意**
>
> 如果您的链接中存在特殊字符或空格，请务必在点击签名生成之前完成所有的URL编码， 否则会导致验证失败。

<div id="creating-a-click-signature" />

## 点击签名的创建方式

如需创建点击签名，必须完成以下操作：

1. 使用下文的参数列表和JSON格式创建一个JSON字符串。
2. 使用HMAC56为这个JSON创建签名

<div id="list-of-attributes" />

### 参数列表

点击签名以及广告交互签名支持下列参数。

| 顺序 | 参数 | 是否必须配置 | 说明 |
| --- | --- | --- | --- |
| 1 | link\_domain | 是 | 点击链接中的域名，例如<ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | 是 | 点击链接的路径，不带前导反斜杠  <br />在单一平台链接中即为**app-id**；在OneLink链接中即为**template-id** |
| 3 | pid | 是 |  |
| 4 | af\_prt | 否 |  |
| 5 | af\_siteid | 是 |  |
| 6 | clickid | 是 | 相关点击的一次性唯一标识符 |
| 7 | expires | 是 | 相关点击的过期时间 |
| 8 | af\_engagement\_type | 否 |  |
| 9 | af\_click\_lookback | 否 |  |
| 10 | af\_viewthrough\_lookback | 否 |  |
| 11 | af\_reengagement\_window | 否 |  |
| 12 | is\_retargeting | 否 |  |
| 13 | af\_ip | 否 |  |
| 14 | advertising\_id | 否 |  |
| 15 | oaid | 否 |  |
| 16 | fire\_advertising\_id | 否 |  |
| 17 | idfa | 否 |  |
| 18 | idfv | 否 |  |

<div id="attribute-and-json-rules" />

### 参数及JSON格式说明

<div id="order-and-appearance-of-attributes" />

#### 参数的顺序和形式

* 广告交互链接中适用参数及其值必须以JSON格式配置。
* JSON格式中的参数必须以上表所列的顺序排列。

<div id="empty-attributes" />

#### 空值参数

* JSON中所列参数的值不能为空，也不能仅包含空格。

<div id="json-data-structure" />

#### JSON的数据结构

* JSON数据必须由一个参数数组构成。
  * 各参数都以键值对的格式呈现，即["key", "value"]。  
    举例来说，   
    `[["key-1","value-1"],["key-2","value-2"]...["key-n","value-n"]]`

<div id="attribute-value-escaping" />

#### 参数值转义（escape）

* JSON中的值必须按照<Anchor target="_blank" href="https://www.w3docs.com/snippets/java/how-should-i-escape-strings-in-json.html">JSON格式标准</Anchor>以**小写字符串**编写。

<div id="json-spaces" />

#### JSON中的空格

* 必须对JSON进行轻量化处理，即参数值之间不能出现任何空格、tab字符或换行字符。


* <span id="signature-algorithm"></span>使用HmacSHA256和secret key为该JSON创建签名
* 使用Base64对该签名进行编码，**不带**尾部填充（padding）
* 以signature\_v2参数的形式将该签名添加到点击链接中

```json
//generate a signature from the click url and encode it with base64 without padding String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(jsonString.getBytes()));
```


<div id="signature-example" />

<div id="building-a-signature-example" />

<Accordion title="签名创建环节的示例">

多平台的OneLink点击链接示例：

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&clickid=sdkfjasksjskdfj9845weh&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615
```

用于签名的json对象示例（未删除空格）：

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

用于签名的json对象示例（删除空格后）：

```json
[["link_domain","yourbrand.onelink.me"],["link_path","qswl"],["pid","mediasource_int"],["template-id","qswl"],["af_siteid","my_site"],["clickid","12345"],["expires","1689695615"]]
```

最后可得到以下带有签名的点击链接：

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615  
&signature_v2=WIfCmfLAPSsVrBTqCqfihMeLCnbE4dIAlhHF84WsiWA
```

</Accordion>

<div id="code-examples" />

### 代码示例

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

## 用于点击签名的API

AppsFlyer提供多种API，帮助广告平台管理并测试其点击签名流程。如需详细了解这些API的使用方式，请参考下文的API列表以及后续章节的说明。

<div id="click-signature-apis-1" />

#### 用于点击签名的API

| API方法 | 说明 |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">Generate secret key</Anchor> | 生成秘钥（secret key），后续在签名中使用。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">Revoke secret key</Anchor> | 撤销泄露的秘钥。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">Test</Anchor> | 发送单次点击，用于测试签名。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">Configure mode</Anchor> | 配置点击签名的模式：<ul><li>**disabled**（默认禁用）：AppsFlyer不验证点击签名。</li><li>**report-only**（仅报告，用于测试模式）：AppsFlyer会验证点击签名，但不会拦截签名无效的点击。广告平台可以使用**Report** **API**获取验证成功/失败的点击数据，以便在不影响生产环境和真实流量的情况下测试点击签名。</li><li>**enabled**（启用）：AppsFlyer会拦截签名无效或缺失的点击。</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-circuit-breaker-put">Configure circuit breaker</Anchor> | 配置熔断机制可以保护广告平台，避免产生过多被拦截的点击：<ul><li>**enabled**（默认启用）：如果Protect360系统发现过多点击被标记为无效，则为了保护相关平台，避免发生点击拦截误伤：<ul><li>AF会将Configure mode API更改为report-only（仅报告）。</li><li>并向广告平台发送邮件，提醒其检查点击签名API的设置是否正确。</li></ul></li><li>**disabled**（禁用）：即使拦截比率超过正常水平，Protect360仍会拦截所有被标记为无效的点击。</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">Get configuration</Anchor> | 获取现行secret key的模式和ID信息。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">报告</Anchor> | 用于在系统处于**report-only**（仅报告）或**enabled**（启用）模式时获取验证成本/失败的点击数据，以便在不影响生产环境和真实流量的情况下测试点击签名。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">Exclude app</Anchor> | 配置应用ID，在点击签名验证机制中排除相关应用。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">Remove excluded app</Anchor> | 配置应用ID，将被排除的应用其重新添加到点击签名验证机制中。 |

<div id="legacy-versions" />

## 历史版本

下列信息仅供参考，请勿使用这些历史版本。

<div id="v1-legacy" />

<Accordion title="V1（历史版本）">

<div id="generate-secret-key-method" />

### Generate secret key方法

<div id="generate-secret-key-basics" />

<Accordion title="Generate secret key方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>POST</code></td></tr><tr><td>路径</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>"}</code></span></td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td>以JSON格式返回Secret key</td></tr><tr><td> </td><td>请求限制</td><td>一次最多请求2个现行secret key。</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="API请求">

**方法**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

<div id="parameters" />

#### 参数

| 参数 | 说明 |
| --- | --- |
| ttlHours | <ul><li>相关secret key的有效期，以小时为单位，可用范围为1-1440小时。</li><li>默认为36小时。</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="JSON响应">

| **键** | **说明** |
| --- | --- |
| secret-key-id | 相关secret key的ID |
| secret key | 相关点击签名的secret key |
| expiration | 以毫秒为单位的Epoch时间 |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="Generate secret key的curl示例及响应">

**Curl请求**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON响应**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="HTTP响应代码">

<div id="response-codes" />

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="revoke-secret-key-method" />

### Revoke secret key方法

<div id="revoke-secrete-key-basics" />

<Accordion title="Revoke secret key方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>DELETE</code></td></tr><tr><td>路径</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>"}</code></span></td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td></td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<Accordion title="API请求">

**方法**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

<div id="parameters-1" />

#### 参数

| 参数 | 说明 |
| --- | --- |
| secret-id | 用于撤销相关secret key的ID |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="Generate secret key的curl示例及响应">

**Curl请求**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="HTTP响应代码">

<div id="response-codes-1" />

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="test-method" />

### Test方法

<div id="test-basics" />

<Accordion title="Test方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>POST</code></td></tr><tr><td>路径</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/test</span></td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td>以JSON格式返回数据</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="API请求">

**方法**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

<div id="parameters-2" />

#### 参数

| 参数 | 说明 |
| --- | --- |
| URL: | 要测试的点击链接（含签名） |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="JSON响应">

| **键** | **说明** |
| --- | --- |
| test-status | Passed（通过）或Failed（未通过） |
| 消息 | 测试失败的原因。比如：/span><ul><li>Missing signature（签名缺失）</li><li>Invalid signature（签名无效）</li><li>Expired （已过期）</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="Test方法的curl示例及响应">

**Curl请求**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**JSON响应**

```json
{
	"test-status":"Passed / Failed",
	"message": "Invalid signature"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="HTTP响应代码">

<div id="response-codes-2" />

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="configure-mode-method" />

### Configure mode方法

<div id="configure-mode-basics" />

<Accordion title="Configure mode方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>POST</code></td></tr><tr><td>路径</td><td> <span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>mode/&lt;mode&gt;</strong></span></span> </td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td>以JSON格式返回数据</td></tr></tbody></table>

</Accordion>

<Accordion title="API请求">

**方法**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

<div id="parameters-3" />

#### 参数

| 参数 | 说明 |
| --- | --- |
| mode | 可用值包括：<ul><li>enabled（启用）<br />**请注意：** 请务必先在“report-only”（仅报告）模式下运行数小时，并检查您的报告，确保相关配置正确无误且所有点击均已通过签名验证，然后再切换到“enabled”。</li><li>disabled（禁用）</li><li>report-only（仅报告）</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="Configure mode方法的curl示例">

**Curl请求**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<Accordion title="HTTP响应代码">

<div id="response-codes-3" />

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request（请求无效） | 模式无效 |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="configure-circuit-breaker-method" />

### Configure circuit breaker方法

<div id="configure-circuit-breaker-basics" />

<Accordion title="Configure circuit breaker方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>POST</code></td></tr><tr><td>路径</td><td><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td><span>HTTP状态</span></td></tr></tbody></table>

</Accordion>

<div id="api-request::ef73eae0" />

<Accordion title="API请求">

**方法**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```

<div id="request-body-json" />

#### 请求体中的JSON格式参数

| 参数 | 说明 |
| --- | --- |
| status | <ul><li>enabled（启用）</li><li>disabled（禁用）</li></ul> |

</Accordion>

<div id="configure-circuit-breaker-curl-example-and-response" />

<Accordion title="Configure circuit breaker方法的curl示例和响应">

**Curl请求**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
```

</Accordion>

<div id="http-response-codes::d35e3a62" />

<Accordion title="HTTP响应代码">

<div id="response-codes-4" />

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request（请求无效） | 状态无效 |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="get-configuration-method" />

### Get configuration方法

<div id="get-configuration-basics" />

<Accordion title="Get configuration方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>GET</code></td></tr><tr><td>路径</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config</span></td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td>以JSON格式返回数据</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<Accordion title="API请求">

**方法**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="JSON响应">

| **键** | **说明** |
| --- | --- |
| mode | 可能出现的值：<ul><li>enabled（启用）</li><li>disabled（禁用）</li><li>report-only（仅报告）</li></ul> |
| circuit-breaker-config | 一个包含**status**（状态）参数的JSON对象，可能出现的值为：<ul><li>enabled（启用）</li><li>disabled（禁用）</li></ul> |
| active-key-ids | JSON格式的数组，其中包含现行密钥的以下信息：<ul><li>**secret-key-id**：随机生成的密钥ID</li><li>**expiration**：密钥效期的Epoch时间，以毫秒为单位</li></ul> |
|  | JSON格式的数组，其中包含被排除应用的app-ids |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="Get configuration方法的curl示例及响应">

**Curl请求**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON响应**

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

<Accordion title="HTTP响应代码">

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="report-method" />

### Report方法

<div id="report-basics" />

<Accordion title="Report方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>GET</code></td></tr><tr><td>路径</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/report</span></td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td>以CSV格式返回数据</td></tr></tbody></table>

</Accordion>

<div id="api-request::b28cedb0" />

<Accordion title="API请求">

**方法**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

<div id="parameters-4" />

#### 参数

<table><thead><tr><th>参数</th><th>说明</th></tr></thead><tbody><tr><td>开始日期：</td><td>报告的起始日期和时间。格式：yyyy-mm-ddThh</td></tr><tr><td>结束日期：</td><td><span>报告的截止日期和时间。格式：yyyy-mm-ddThh</span></td></tr><tr><td colspan="2"><span>API配置要求：<strong>同时</strong>配置start-date和end-date，或者两者<strong>都不</strong>配置。若不配置起始/截止日期，则报告会显示过去24小时的数据。</span></td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="CSV响应">

| **栏位** | **说明** |
| --- | --- |
| time | 指点击的日期和时间。格式为：yyyy-mm-ddThh |
| total\_clicks | 报告周期内的点击总数 |
| valid\_clicks | 报告周期内的有效点击数量 |
| missing\_signature | 报告周期内出现签名缺失的点击数量 |
| expired\_clicks | 报告周期内过期的点击数量 |
| invalid\_signature | 报告周期内签名无效的点击数量 |
| no\_active\_secrets | 由于系统中没有现行的secret key，因而被拦截的点击数量（通常是因为系统处于report-only模式） |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="Test方法的curl示例及响应">

**Curl请求**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/report?start-date=2021-01-07T07&end-date=2021-01-17T12' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**CSV响应**

| **time** | **total\_clicks** | **valid\_clicks** | **missing\_signature** | **expired\_clicks** | **invalid\_signature** | **no\_active\_signatures** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<Accordion title="HTTP响应代码">

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="exclude-app-method" />

### Exclude app方法

<div id="exclude-app-method-basics" />

<Accordion title="Exclude app方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>POST</code></td></tr><tr><td>路径</td><td> <span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<span><strong>excluded-app/&lt;app-id&gt;</strong></span></span> </td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td></td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::1054abca" />

<Accordion title="API请求">

**方法**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-5" />

#### 参数

| 参数 | 说明 |
| --- | --- |
| app-id | 需要从点击签名验证机制中排除的应用ID |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="Exclude app方法的curl示例">

**Curl请求**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::90a409c" />

<Accordion title="HTTP响应代码">

<div id="response-codes-7" />

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="remove-excluded-app-method" />

### Remove excluded app方法

<div id="remove-excluded-app-method-basics" />

<Accordion title="Remove excluded app方法的基础信息">

<table><thead><tr><th>类别</th><th>注意事项</th><th><span>说明</span></th></tr></thead><tbody><tr><td rowspan="3">请求</td><td>HTTP方法</td><td><code>DELETE</code></td></tr><tr><td>路径</td><td> <span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<span><strong>excluded-app/&lt;app-id&gt;</strong></span></span> </td></tr><tr><td>授权请求头（Authorization header） </td><td><ul><li>必须配置Authorization header，其中包含一个Bearer token。 </li><li>相关账户的管理员可以按以下方式在面板中获取该token：  <a href="/marketers/zh/docs/managing-appsflyer-tokens" target="_blank">点击面板右上角的邮箱地址，打开下拉菜单 &gt; API token，找到V2.0 token</a> </li></ul></td></tr><tr><td>响应</td><td>结果</td><td></td></tr></tbody></table>

</Accordion>

<div id="api-request::9504d16f" />

<Accordion title="API请求">

**方法**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-6" />

#### 参数

| 参数 | 说明 |
| --- | --- |
| app-id | 需要从点击签名验证机制的排除列表中移除的应用ID（将这些应用重新加入点击签名验证机制） |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="Remove excluded app方法的curl示例">

**Curl请求**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::8454f45d" />

<div id="http-response-codes::7991b66" />

<div id="http-response-codes::b5e059da" />

<Accordion title="HTTP响应代码">

<div id="response-codes-8" />

#### 响应代码

| 代码 | 响应消息 | 说明 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized（拒绝授权） | 授权请求头（authorization header）无效或缺失 |

</Accordion>

<div id="code-sample" />

<Accordion title="代码示例">

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

## 其他相关信息

<div id="troubleshooting" />

<Accordion title="问题排查">

如果一小时内超过90%的点击都未通过签名验证，AppsFlyer会停止点击签名验证，并切换到report-only（仅报告）模式。

这是为了保护贵司免受技术问题影响，并帮助您排查异常现象的根因：

* 如果您发现签名正常生效，且点击拦截正确无误，请使用[configure circuit breaker方法](/docs/click-signing-for-ad-networks#configure-circuit-breaker方法)关闭熔断机制。
* 如果您发现点击拦截有误伤，请完成以下操作：
  1. [使用get](/docs/click-signing-for-ad-networks#get-configuration方法) configuration方法，检查点击签名的配置，确保您使用的secret key是一个有效密钥。
  2. 使用[点击签名报告](/docs/click-signing-for-ad-networks#report方法)进一步掌握被拦截点击的信息，考察无效点击的来源（如代理/应用ID）及成因。
* 如果您发现问题来自某个未进行标准化对接的应用，请使用[exclude app API](/docs/click-signing-for-ad-networks#exclude-app方法)该应用从点击签名验证机制中排除。
* 如果您发现配置有问题：
  1. 继续使用report-only（仅报告）模式。
  2. 修复您的点击签名流程。
  3. 查看点击签名报告中的数据，看到点击可正常得到验证后，再重新启用点击签名验证。

</Accordion>

<div id="faq" />

<Accordion title="常见问题解答">

| **问：如何在不影响生产环境的前提下测试点击签名？**<br /><br />**解答**：测试点击签名的方式有以下两种：<ol><li>[使用](/docs/click-signing-for-ad-networks#test方法)test API。这一方法适用于开发阶段，可测试单次点击的签名。</li><li>使用report-only（仅报告）模式。Report-only模式下，AppsFlyer会验证生产环境中的点击签名，并为您呈现拦截结果，但是不会对无效点击进行实际拦截。这样，您就可以在不影响真实流量的情况下测试点击签名。</li></ol> |
| --- |
| **问：API token和secret key有什么区别？**<br /><br />**答**： **API token**用于授权并执行点击签名API，每个广告平台只有一个API token。<Anchor target="_blank" href="/marketers/zh/docs/managing-appsflyer-tokens">AppsFlyer API V2.0 token</Anchor>必须由账户管理员获取。<br /><br />**Secret key**用于生成签名，可通过[Generate secret key方法](/docs/click-signing-for-ad-networks#generate-secret-key方法)创建。广告平台需要负责生成新的secret key，详见[特点说明](/docs/click-signing-for-ad-networks#traits)部分。 |
| **问：能否仅对特定的广告系列使用点击签名验证？**<br /><br />**答**：点击签名会对一个广告平台所产生的所有点击生效。您可以将特定的应用排除在验证机制之外，但无法按广告系列进行排除。 |

</Accordion>

<div id="traits" />

<Accordion title="特点">

| 特点 | 说明 |
| --- | --- |
| 点击签名 | 签名必须在广告平台侧的服务器中完成。 |
| Secret Key | <ul><li>一个广告平台最多同时可以有两个现行的secret key。</li><li>每个secret key都有一个有效期。</li><li>使用过期的secret key签名的点击会被拦截。</li></ul> |
| Report API | 点击有效性数据以每小时一次的频率进行更新并汇总。 |

</Accordion>

<div data-zendesk-anchors="about-click-signing=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%AE%80%E4%BB%8B h_01HNWC70BPGDJAG3X8M5Z2RHQ4=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%AE%80%E4%BB%8B click-signature-integration=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84%E6%8E%A5%E5%85%A5%E6%96%B9%E5%BC%8F h_01HNWC70BPFYMZ56GTPV3W6DXA=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84%E6%8E%A5%E5%85%A5%E6%96%B9%E5%BC%8F flow=%E9%93%BE%E8%B7%AF h_01HNWC70BPMXTKF9NZBYGCB874=%E9%93%BE%E8%B7%AF procedure=%E6%B5%81%E7%A8%8B h_01HNWC70BPHCAGD1ECA56CC1Q6=%E6%B5%81%E7%A8%8B h_01HNWC70BPAR4QNTNSFE1JZM2J=%E6%B3%A8%E6%84%8F list-of-attributes=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84%E5%88%9B%E5%BB%BA%E6%96%B9%E5%BC%8F h_01HP4A42YYFFF6M4VEH84KRTTK=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84%E5%88%9B%E5%BB%BA%E6%96%B9%E5%BC%8F h_01HNWD3XYWFRY262HZZVAVWACR=%E5%8F%82%E6%95%B0%E5%88%97%E8%A1%A8 attribute-rules=%E5%8F%82%E6%95%B0%E5%8F%8Ajson%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E h_01HNWE3A19RM7757B707TWZ6G0=%E5%8F%82%E6%95%B0%E5%8F%8Ajson%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E order-and-appearance-of-attributes=%E5%8F%82%E6%95%B0%E7%9A%84%E9%A1%BA%E5%BA%8F%E5%92%8C%E5%BD%A2%E5%BC%8F h_01HNWE3A1920YQGZX2VG4X3M4B=%E5%8F%82%E6%95%B0%E7%9A%84%E9%A1%BA%E5%BA%8F%E5%92%8C%E5%BD%A2%E5%BC%8F empty-attributes=%E7%A9%BA%E5%80%BC%E5%8F%82%E6%95%B0 h_01HNYRZ1DPDDQ5H8RFYKAQWVKP=%E7%A9%BA%E5%80%BC%E5%8F%82%E6%95%B0 json-data-structure=json%E7%9A%84%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84 h_01HNYS6R7F0MNPBN08TXKQS5DV=json%E7%9A%84%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84 attribute-value-escaping=%E5%8F%82%E6%95%B0%E5%80%BC%E8%BD%AC%E4%B9%89escape h_01HNYSEBGD1DBSV2MHS7DZ75HS=%E5%8F%82%E6%95%B0%E5%80%BC%E8%BD%AC%E4%B9%89escape json-spaces=json%E4%B8%AD%E7%9A%84%E7%A9%BA%E6%A0%BC h_01HNYSY42HS1RXFG7T7QS9B0TK=json%E4%B8%AD%E7%9A%84%E7%A9%BA%E6%A0%BC h_01HNYSJDFWAM9RREYH4M8DZQJA=signature-algorithm h_01HP3YAN03BWVA30JP1JAFZYAG=signature-example h_01HP3Y2Z65BN0SZ56XSHD52MSY=building-a-signature-example code-example=%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B h_01HNYT8Z33M69JAS72MQ03YX0M=%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego click-signature-apis=%E7%94%A8%E4%BA%8E%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84api h_01HNWC70BPNEVT00S040TQ9KVD=%E7%94%A8%E4%BA%8E%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84api click-signature-apis::58bf03c7=%E7%94%A8%E4%BA%8E%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84api-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=%E7%94%A8%E4%BA%8E%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D%E7%9A%84api-1 legacy-versions=%E5%8E%86%E5%8F%B2%E7%89%88%E6%9C%AC h_01HNZ3YMFRWFDY751EBA58V6Q0=%E5%8E%86%E5%8F%B2%E7%89%88%E6%9C%AC h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy generate-secret-key-method=generate-secret-key%E6%96%B9%E6%B3%95 h_01HNWC70BPBPSX1WKJJC2W6H69=generate-secret-key%E6%96%B9%E6%B3%95 h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request parameters=%E5%8F%82%E6%95%B0 h_01HNWC70BPS83JD78JWQYK1NX9=%E5%8F%82%E6%95%B0 h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes response-codes=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81 h_01HNWC70BPMQ8Q94JD5CBT5RHZ=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81 revoke-secret-key-method=revoke-secret-key%E6%96%B9%E6%B3%95 h_01HNWC70BP8V05Q04J6EVGAS9T=revoke-secret-key%E6%96%B9%E6%B3%95 h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=%E5%8F%82%E6%95%B0-1 h_01HNWC70BPQ5S06E210RTE7E6R=%E5%8F%82%E6%95%B0-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-1 h_01HNWC70BPN18MB98KWND886QN=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-1 test-method=test%E6%96%B9%E6%B3%95 h_01HNWC70BPKEVRDMT8N4HMC98W=test%E6%96%B9%E6%B3%95 h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=%E5%8F%82%E6%95%B0-2 h_01HNWC70BPKQFVEGWR9QT566YX=%E5%8F%82%E6%95%B0-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-2 h_01HNWC70BPC43F5H85F56DDSQR=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-2 configure-mode-method=configure-mode%E6%96%B9%E6%B3%95 h_01HNWC70BP6NPF7NSF0MGA4BJ3=configure-mode%E6%96%B9%E6%B3%95 h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=%E5%8F%82%E6%95%B0-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=%E5%8F%82%E6%95%B0-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-3 h_01HNWC70BQZ657X25N8JGM57A1=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-3 configure-circuit-breaker-method=configure-circuit-breaker%E6%96%B9%E6%B3%95 h_01HNWC70BQVSFS7G330NF4XHEP=configure-circuit-breaker%E6%96%B9%E6%B3%95 h_01HNWC70BQ097J2VXW0XKSH3M9=configure-circuit-breaker-basics h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 request-body-json=%E8%AF%B7%E6%B1%82%E4%BD%93%E4%B8%AD%E7%9A%84json%E6%A0%BC%E5%BC%8F%E5%8F%82%E6%95%B0 h_01HNWC70BQ6R955776Y6H4EZRG=%E8%AF%B7%E6%B1%82%E4%BD%93%E4%B8%AD%E7%9A%84json%E6%A0%BC%E5%BC%8F%E5%8F%82%E6%95%B0 h_01HNWC70BQRZEZ4PTV59FGYS4Z=configure-circuit-breaker-curl-example-and-response h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-4 get-configuration-method=get-configuration%E6%96%B9%E6%B3%95 h_01HNWC70BQZY6TYSQBWZ17S0W5=get-configuration%E6%96%B9%E6%B3%95 h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-7 h_01HNWC70BQDGVBZ94F0N49FF40=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-7 report-method=report%E6%96%B9%E6%B3%95 h_01HNWC70BQTBMNKHV4RH4ZQ0AE=report%E6%96%B9%E6%B3%95 h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=%E5%8F%82%E6%95%B0-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=%E5%8F%82%E6%95%B0-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-8 h_01HNWC70BQTPPWA4SNG25E8FFB=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-8 exclude-app-method=exclude-app%E6%96%B9%E6%B3%95 h_01HNWC70BQ9SK2XCBGGHXVMRDV=exclude-app%E6%96%B9%E6%B3%95 h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=%E5%8F%82%E6%95%B0-5 h_01HNWC70BREG4XQJV3X9518FC5=%E5%8F%82%E6%95%B0-5 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-8 h_01HNWC70BRN8BHWF6WGY2RH45X=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-8 remove-excluded-app-method=remove-excluded-app%E6%96%B9%E6%B3%95 h_01HNWC70BR18P0H96VN64RS05G=remove-excluded-app%E6%96%B9%E6%B3%95 h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=%E5%8F%82%E6%95%B0-6 h_01HNWC70BR4ADH7T3AFG58FZH6=%E5%8F%82%E6%95%B0-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=%E5%93%8D%E5%BA%94%E4%BB%A3%E7%A0%81-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample additional-information=%E5%85%B6%E4%BB%96%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF h_01HNWC70BRN0NGTQVWED6VG81Y=%E5%85%B6%E4%BB%96%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
