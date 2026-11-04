---
title: クリック署名：アドネットワーク向け
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
  edited_at: '2026-10-14T09:28:26Z'
  id: 360017831497
  locale: ja
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ja/articles/360017831497
---
> **概要：** 概要：クリックに署名の検証を追加することで、広告不正による被害を回避することが可能です。これにより、不正なクリックがアドネットワークに紐付けられなくなります。

<div id="about-click-signing" />

## クリック署名について

不正業者は、ごくわずかな技術でアドネットワークに代わって、数千はたまた数百万もの偽クリックを作成し、AppsFlyerへ送信することが可能です。アドネットワーク自身がこのような問題が発生していることを認識できていない場合もあります。

AppsFlyerによって媒体へ紐付けられたクリックが、不正業者によって作られた偽クリックではなく実際にアドネットワークから発生したものであることを確実にするために、<Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256の署名</Anchor>を使ってクリックに署名を付与することをおすすめします。

この署名によりAppsFlyerはクリックを検証でき、クリック情報が不正業者によって操作されていないことを確認します。

* 検証されたクリックは記録され、アドネットワークへ紐付けられます。
* 無効になったクリックは除外され、以下のように処理されます：
  * <Anchor target="_blank" href="/partners/ja/docs/protect360-reports-for-ad-networks#failed-click-signatures">詳細はこちら</Anchor>
  * アドネットワークのコンバージョン率やクリック洪水のしきい値には影響を与えません。

<div id="click-signature-integration" />

## クリック署名の連携

<div id="flow" />

### フロー

以下のチャートでは、初期の開発と基本テストから実稼働テスト、そして最終的な実稼働までの流れの概要を示しています。

![Click_signing_integration_flow.png](https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png)

<div id="note" />

<div id="procedure" />

<div id="building-a-signature-example" />

<div id="signature-example" />

### 手順

前提条件：

クリックに署名するには：

1. シークレットキーの生成APIを使用して、シークレットキーを生成してください。  
   ベストプラクティス：推奨：24時間毎に新しいシークレットキーを生成して使用してください。シークレットキーの有効期限は36時間です。
3. 以下のようにコードをクリックURLに追加してください：
   * **expires**のパラメータにはアドネットワークがクリックを主張しなくなるUnixのタイムスタンプを含めてください。
   * HMAC-SHA256の署名情報を含めてください。  
     例：

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```



| <span id="creating-a-click-signature"></span><span id="signature-algorithm"></span><span id="json-spaces"></span><span id="attribute-value-escaping"></span><span id="json-data-structure"></span><span id="empty-attributes"></span><span id="order-and-appearance-of-attributes"></span><span id="attribute-and-json-rules"></span><span id="list-of-attributes"></span>順序 | パラメータ | 必須 | 備考 |
| --- | --- | --- | --- |
| 1 | link\_domain | はい | <ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | はい |  |
| 3 | pid | はい |  |
| 4 | af\_prt | いいえ |  |
| 5 | af\_siteid | はい |  |
| 6 | clickid | はい |  |
| 7 | &expires= | はい |  |
| 8 | af\_engagement\_type | いいえ |  |
| 9 | af\_click\_lookback | いいえ |  |
| 10 | af\_viewthrough\_lookback= | いいえ |  |
| 11 | af\_reengagement\_window | いいえ |  |
| 12 | is\_retargeting | いいえ |  |
| 13 | af\_ip | いいえ |  |
| 14 | advertising\_id | いいえ |  |
| 15 | oaid | いいえ |  |
| 16 | fire\_advertising\_id | いいえ |  |
| 17 | idfa | いいえ |  |
| 18 | idfv | いいえ |  |





* * 例：   
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

### コードの例

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

## クリック署名の各種API

AppsFlyerでは、アドネットワークがクリック署名のプロセルを管理できる各種APIを用意しています。以下表のAPI一覧と、APIの利用に必要な各種情報をまとめた各セクションを参照してください。

<div id="click-signature-apis-1" />

#### クリック署名の各種API

| APIメソッド | 備考 |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">Generate secret key</Anchor> | 署名に使用するシークレットキーを生成します。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">Revoke secret key</Anchor> | シークレットキーを無効化します。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">Test</Anchor> | 署名をテストするために単発のクリックを送信します。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">Configure mode</Anchor> | クリック署名の各モードを設定します：<ul><li>無効 (デフォルト設定)</li><li>有効enabled: AppsFlyerが無効な署名を持つクリック、または署名が欠損しているクリックを実際にブロックします。/strong></li></ul> |
|  | <ul><li>不可</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">Get configuration</Anchor> | 有効なシークレットキーのIDと選択されているモードを取得します。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">レポート</Anchor> | システムがreport-onlyモードまたは**enabledモード**の場合、正常なクリックと失敗したクリックに関する統計情報を取得します。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">Exclude app</Anchor> | クリック署名のルールから除外するアプリIDを設定します。 |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">Remove excluded app</Anchor> | 一度除外した後に、再度クリック署名のルールに含めるアプリIDを設定します。 |


<div id="legacy-versions" />

<div id="v1-legacy" />

<Accordion title="V1（レガシー）">

<div id="generate-secret-key-method" />

### Generate secret keyのメソッド

<div id="generate-secret-key-basics" />

<Accordion title="Generate secret keyの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>POST</code></td></tr><tr><td>経路</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>"}</code></span></td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>JSON内でシークレットキーが返されます。</td></tr><tr><td> </td><td>リクエスト制限</td><td>一度に最大2つまでシークレットキーをアクティブにできます</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="API リクエスト">

**メソッド**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

<div id="parameters" />

#### パラメーター

| パラメータ | 説明 |
| --- | --- |
| ttlHours | <ul><li>デフォルト設定は36時間です。</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="JSON レスポンス">

| **キー** | **説明** |
| --- | --- |
| secret-key-id | シークレットキーのIDです。 |
| secret key | クリック署名のシークレットキーです。 |
| expiration | ミリ秒単位のエポックタイムです。 |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="Generate secret keyのcurlサンプルとレスポンス">

**Curl リクエスト**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON レスポンス**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="HTTP のレスポンスコード">

<div id="response-codes" />

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="revoke-secret-key-method" />

### Revoke secret keyのメソッド

<div id="revoke-secrete-key-basics" />

<Accordion title="Revoke secret keyの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>DELETE</code></td></tr><tr><td>経路</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>"}</code></span></td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>Empty</td></tr></tbody></table>

</Accordion>

<Accordion title="API リクエスト">

**メソッド**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

<div id="parameters-1" />

#### パラメーター

| パラメータ | 説明 |
| --- | --- |
| secret-id | 無効にするシークレットキーのIDです。 |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="Generate secret keyのcurlサンプルとレスポンス">

**Curl リクエスト**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="HTTP のレスポンスコード">

<div id="response-codes-1" />

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="test-method" />

### Testのメソッド

<div id="test-basics" />

<Accordion title="Testの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>POST</code></td></tr><tr><td>経路</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/test</span></td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>JSONで返されます。</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="API リクエスト">

**メソッド**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

<div id="parameters-2" />

#### パラメーター

| パラメータ | 説明 |
| --- | --- |
| URL | 署名を含む、テストで使用するクリックURLです。 |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="JSON レスポンス">

| **キー** | **説明** |
| --- | --- |
| test-status | Passed(成功) もしくは Failed(失敗) |
| メッセージ | テストの失敗理由。例：<ul><li>Missing signature (署名がありません。)</li><li>Invalid signature (署名が無効です。)</li><li>Expired  (署名が期限切れです。)</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="Testのcurlサンプルとレスポンス">

**Curl リクエスト**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**JSON レスポンス**

```json
{
	"test-status":"Passed / Failed",
	"message": "Invalid signature"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="HTTP のレスポンスコード">

<div id="response-codes-2" />

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="configure-mode-method" />

### Configure modeのメソッド

<div id="configure-mode-basics" />

<Accordion title="Configure modeの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>POST</code></td></tr><tr><td>経路</td><td> <span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>mode/&lt;mode&gt;</strong></span></span> </td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>JSONで返されます。</td></tr></tbody></table>

</Accordion>

<Accordion title="API リクエスト">

**メソッド**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

<div id="parameters-3" />

#### パラメーター

| パラメータ | 説明 |
| --- | --- |
| mode | 含まれる値：<ul><li>enabled<br />**ご注意ください**</li><li>disabled</li><li>report-only</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="Configure modeのcurlサンプル">

**Curl リクエスト**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<Accordion title="HTTP のレスポンスコード">

<div id="response-codes-3" />

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | Invalid mode (無効なモード) |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>


<table><thead><tr><th><span id="configure-circuit-breaker-basics"></span><span id="configure-circuit-breaker-method"></span>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>POST</code></td></tr><tr><td>経路</td><td><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td></td></tr></tbody></table>


<div id="api-request::ef73eae0" />

<Accordion title="API リクエスト">

**メソッド**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```


| <span id="configure-circuit-breaker-curl-example-and-response"></span><span id="request-body-json"></span>パラメータ | 説明 |
| --- | --- |
| ステータス | <ul><li>enabled</li><li>disabled</li></ul> |

</Accordion>

**Curl リクエスト**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
```


<div id="http-response-codes::d35e3a62" />

<Accordion title="HTTP のレスポンスコード">

<div id="response-codes-4" />

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="response-codes-5" />

<div id="get-configuration-method" />

### Get configurationのメソッド

<div id="get-configuration-basics" />

<Accordion title="Get configurationの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>GET</code></td></tr><tr><td>経路</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config</span></td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>JSONで返されます。</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<Accordion title="API リクエスト">

**メソッド**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="JSON レスポンス">

| **キー** | **説明** |
| --- | --- |
| mode | 以下のいずれか：<ul><li>enabled</li><li>disabled</li><li>report-only</li></ul> |
| circuit-breaker-config | <ul><li>enabled</li><li>disabled</li></ul> |
| active-key-ids | アクティブなキーを保持したJSON配列です:<ul><li>**secret-key-id**:</li><li>expirationexpiration: シークレットキーのミリ秒単位のエポック時間で表現された有効期限です。</li></ul> |
| excluded-app-ids | 除外したアプリIDを含むJSON配列です。 |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="Get configurationのcurlサンプルとレスポンス">

**Curl リクエスト**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON レスポンス**

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

<Accordion title="HTTP のレスポンスコード">

<div id="response-codes-7" />

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="report-method" />

### Reportのメソッド

<div id="report-basics" />

<Accordion title="Reportの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>GET</code></td></tr><tr><td>経路</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/report</span></td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>CSVで返されます。</td></tr></tbody></table>

</Accordion>

<div id="api-request::b28cedb0" />

<Accordion title="API リクエスト">

**メソッド**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

<div id="response-codes-6" />

<div id="parameters-4" />

#### パラメーター

<table><thead><tr><th>パラメータ</th><th>説明</th></tr></thead><tbody><tr><td>start-date</td><td>レポートの開始日時です。形式： yyyy-mm-ddThh</td></tr><tr><td>end-date</td><td>レポートの終了日時です。形式：yyyy-mm-ddThh</td></tr><tr><td colspan="2">API には、<span> start-dateとend-dateの両方を含めるか</span>、もしくは<strong>どちらも入力しなくても機能します。</strong>start/end-dateが指定されていない場合、過去24時間の結果が表示されます。</td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="CSVレスポンス">

| **列** | **説明** |
| --- | --- |
| time | クリックの日時です。形式：yyyy-mm-ddThh |
| total\_clicks | レポート期間におけるクリック数の合計です。 |
| valid\_clicks | レポート期間における有効なクリック数です。 |
| missing\_signature | レポート期間における署名が欠損しているクリック数です。 |
| expired\_clicks | レポート期間における署名の期限切れのクリック数です。 |
| invalid\_signature | レポート期間における無効な署名のクリック数です。 |
| no\_active\_secrets | システム上に有効なシークレットキーがないために拒否されたクリック数です。(report-onlyモードの場合) |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="Testのcurlサンプルとレスポンス">

**Curl リクエスト**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/report?start-date=2021-01-07T07&end-date=2021-01-17T12' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**CSVレスポンス**

| **time** | **total\_clicks** | **valid\_clicks** | **missing\_signature** | **expired\_clicks** | **invalid\_signature** | **no\_active\_signatures** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<Accordion title="HTTP のレスポンスコード">

<div id="response-codes-8" />

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="exclude-app-method" />

### Exclude appのメソッド

<div id="exclude-app-method-basics" />

<Accordion title="Exclude appの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>POST</code></td></tr><tr><td>経路</td><td> https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<span><span>excluded-app/&lt;app-id&gt;</span></span> </td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>Empty</td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::1054abca" />

<Accordion title="API リクエスト">

**メソッド**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-5" />

#### パラメーター

| パラメータ | 説明 |
| --- | --- |
| app-id | クリック署名の検証対象から除外するアプリIDです。 |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="Exclude appのcurlサンプル">

**Curl リクエスト**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::90a409c" />

<Accordion title="HTTP のレスポンスコード">

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="remove-excluded-app-method" />

### Remove excluded appのメソッド

<div id="remove-excluded-app-method-basics" />

<Accordion title="Remove excluded appの基本仕様">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><span>説明</span></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>DELETE</code></td></tr><tr><td>経路</td><td> https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<span><span>excluded-app/&lt;app-id&gt;</span></span> </td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。  <a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a>  </li></ul></td></tr><tr><td>レスポンス</td><td>結果</td><td>Empty</td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<div id="api-request::9504d16f" />

<Accordion title="API リクエスト">

**メソッド**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-6" />

#### パラメーター

| パラメータ | 説明 |
| --- | --- |
| app-id | クリック署名の検証対象から一度除外し、改めてそのリストから削除するアプリIDです。 |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="Remove excluded appのcurlサンプル">

**Curl リクエスト**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::8454f45d" />

<div id="http-response-codes::7991b66" />

<div id="http-response-codes::b5e059da" />

<Accordion title="HTTP のレスポンスコード">

#### 応答コード

| コード | メッセージ | 備考 |
| --- | --- | --- |
| 200 | OK |  |
| 401 | 許可されていません | 認証ヘッダーが無効、または見つかりません。 |

</Accordion>

<div id="code-sample" />

<Accordion title="Codeサンプル">

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

## 追加情報

<div id="troubleshooting" />

<Accordion title="トラブルシューティング">

</Accordion>

<div id="faq" />

<Accordion title="よくある質問">

| **Q:**<br /><br />**A**: |
| --- |
| **Q:**<br /><br />**A**: APIトークン<br /><br />Secret Key |
| **Q:**<br /><br />**A**: |

</Accordion>

<div id="traits" />

<Accordion title="特性">

| 特性 | 説明 |
| --- | --- |
| クリック署名 | 署名はアドネットワークのサーバー上で生成する必要があります。 |
| Secret Key | <ul><li>広告ネットワークでは、最大2つまでシークレットキーを同時にアクティブにすることが可能です。</li><li>個々のシークレットキーには有効期限があります。</li><li>期限切れのシークレットキーで署名されたクリックは除外されます。</li></ul> |
| Report API | クリックの有効性の更新は、時間単位で集計されます。 |

</Accordion>

<div data-zendesk-anchors="about-click-signing=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HNWC70BPGDJAG3X8M5Z2RHQ4=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 click-signature-integration=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AE%E9%80%A3%E6%90%BA h_01HNWC70BPFYMZ56GTPV3W6DXA=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AE%E9%80%A3%E6%90%BA flow=%E3%83%95%E3%83%AD%E3%83%BC h_01HNWC70BPMXTKF9NZBYGCB874=%E3%83%95%E3%83%AD%E3%83%BC procedure=%E6%89%8B%E9%A0%86 h_01HNWC70BPHCAGD1ECA56CC1Q6=%E6%89%8B%E9%A0%86 h_01HNWC70BPAR4QNTNSFE1JZM2J=%E6%89%8B%E9%A0%86 h_01HP4A42YYFFF6M4VEH84KRTTK=list-of-attributes h_01HNWD3XYWFRY262HZZVAVWACR=list-of-attributes code-example=%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E4%BE%8B h_01HNYT8Z33M69JAS72MQ03YX0M=%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E4%BE%8B h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego click-signature-apis=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AE%E5%90%84%E7%A8%AEapi h_01HNWC70BPNEVT00S040TQ9KVD=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AE%E5%90%84%E7%A8%AEapi click-signature-apis::58bf03c7=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AE%E5%90%84%E7%A8%AEapi-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D%E3%81%AE%E5%90%84%E7%A8%AEapi-1 h_01HNZ3YMFRWFDY751EBA58V6Q0=legacy-versions h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy generate-secret-key-method=generate-secret-key%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BPBPSX1WKJJC2W6H69=generate-secret-key%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request parameters=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC h_01HNWC70BPS83JD78JWQYK1NX9=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes response-codes=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89 h_01HNWC70BPMQ8Q94JD5CBT5RHZ=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89 revoke-secret-key-method=revoke-secret-key%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BP8V05Q04J6EVGAS9T=revoke-secret-key%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-1 h_01HNWC70BPQ5S06E210RTE7E6R=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-1 h_01HNWC70BPN18MB98KWND886QN=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-1 test-method=test%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BPKEVRDMT8N4HMC98W=test%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-2 h_01HNWC70BPKQFVEGWR9QT566YX=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-2 h_01HNWC70BPC43F5H85F56DDSQR=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-2 configure-mode-method=configure-mode%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BP6NPF7NSF0MGA4BJ3=configure-mode%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-3 h_01HNWC70BQZ657X25N8JGM57A1=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-3 h_01HNWC70BQVSFS7G330NF4XHEP=configure-circuit-breaker-method h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 h_01HNWC70BQ6R955776Y6H4EZRG=request-body-json h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-4 get-configuration-method=get-configuration%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BQZY6TYSQBWZ17S0W5=get-configuration%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-5 h_01HNWC70BQDGVBZ94F0N49FF40=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-5 report-method=report%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BQTBMNKHV4RH4ZQ0AE=report%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-6 h_01HNWC70BQTPPWA4SNG25E8FFB=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-6 exclude-app-method=exclude-app%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BQ9SK2XCBGGHXVMRDV=exclude-app%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-5 h_01HNWC70BREG4XQJV3X9518FC5=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-5 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-7 h_01HNWC70BRN8BHWF6WGY2RH45X=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-7 remove-excluded-app-method=remove-excluded-app%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BR18P0H96VN64RS05G=remove-excluded-app%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89 h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-6 h_01HNWC70BR4ADH7T3AFG58FZH6=%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=%E5%BF%9C%E7%AD%94%E3%82%B3%E3%83%BC%E3%83%89-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample additional-information=%E8%BF%BD%E5%8A%A0%E6%83%85%E5%A0%B1 h_01HNWC70BRN0NGTQVWED6VG81Y=%E8%BF%BD%E5%8A%A0%E6%83%85%E5%A0%B1 h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
