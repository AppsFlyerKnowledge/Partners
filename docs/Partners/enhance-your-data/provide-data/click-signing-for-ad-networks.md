---
title: Click signing for ad networks
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
  edited_at: '2024-11-17T09:37:22Z'
  id: 360017831497
  locale: en-us
  section: Provide data
  section_id: 6551209900817
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360017831497-Click-signing-for-ad-networks
---
> **At a glance:** Add signature validation to clicks to avoid fraud liabilities and so fraudulent clicks aren't attributed to your ad network.

## About click signing

With minimal tech, fraudsters can send clicks on behalf of an ad network and create thousands, or even millions, of fake clicks that get sent to AppsFlyer. Sometimes, the ad networks themselves aren't aware of the issue.

In order for an ad network to ensure that clicks attributed to it by AppsFlyer actually originated from the ad network, and not from a fraudster creating fake clicks, ad networks should sign their clicks with <Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256</Anchor> signatures.

Click signing also prevents the ad network’s traffic from being blocked due to click flooding. Meaning, that if an ad network reaches the click-blocking threshold due to an extreme level of click flooding, AppsFlyer stops recording and attributing their clicks for the rest of the day.

The signatures enable AppsFlyer to validate the clicks and make sure that the click information hasn't been manipulated by fraudsters.

* Validated clicks are recorded, and attributed to the ad network
* Invalidated clicks are rejected and:
  * Are made available in Protect360 reports for ad networks (not advertisers). <Anchor target="_blank" href="/partners/docs/protect360-reports-for-ad-networks#failed-click-signatures">Learn more</Anchor>
  * Do not impact the conversion rate or click-blocking threshold of the ad network

## Click signature integration

### Flow

The following chart outlines the flow from initial development and basic tests to production tests, and finally, to production.

![Click_signing_integration_flow.png](https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png)

### Procedure

**Prerequisite:** <Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">API V2.0 token</Anchor> from the admin to authorize the click signing API.

**To sign your clicks**:

1. Generate a secret key with the Generate secret key API.  
   Best practice: Generate and use a new secret key every 24 hours, with an expiration of 36 hours.
2. Develop code in your servers that calls the Generate secret key API, takes the secret key and generates an HMAC-SHA256 signature. See code sample.  
   You can use the other APIs as described in the table that follows.
3. The code adds the following to your click URLs:
   * An **expires** parameter that contains a Unix timestamp (in UTC) after which the ad network doesn't claim the click.
   * The HMAC-SHA256 signature.  
     Example:

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```

> 📘 **Note**
>
> Make sure any URL encoding of special characters or spaces in your link occurs before the click signature is generated. Generating the signature first results in verification failure.

## Creating a click signature

To create a click signature you must:

1. Build a JSON using the list of attributes and JSON rules below
2. Create the signature from this JSON using HMAC56

### List of attributes

The following list of attributes is supported for click and engagement signing.

| Order | Parameter | Mandatory | Notes |
| --- | --- | --- | --- |
| 1 | link\_domain | Yes | The domain from the click URL For example:<ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | Yes | The path of the click URL not including a leading backslash.  <br />**app-id** for single platform links or **template-id** for OneLink |
| 3 | pid | Yes |  |
| 4 | af\_prt | No |  |
| 5 | af\_siteid | Yes |  |
| 6 | clickid | Yes | A one-time unique identifier of the click |
| 7 | expires | Yes | click expiration |
| 8 | af\_engagement\_type | No |  |
| 9 | af\_click\_lookback | No |  |
| 10 | af\_viewthrough\_lookback | No |  |
| 11 | af\_reengagement\_window | No |  |
| 12 | is\_retargeting | No |  |
| 13 | af\_ip | No |  |
| 14 | advertising\_id | No |  |
| 15 | oaid | No |  |
| 16 | fire\_advertising\_id | No |  |
| 17 | idfa | No |  |
| 18 | idfv | No |  |

### Attribute and JSON rules

#### Order and appearance of attributes

* Supported parameters in the engagement URL with a value must be in the JSON
* Attributes must be listed in the JSON in the order listed in the table above

#### Empty attributes

* Attributes listed in the JSON cannot be empty values or contain only spaces

#### JSON Data structure

* The JSON data structure must be an array of attributes
  * Each attribute will be in the format ["key", "value"]  
    Example:   
    `[["key-1","value-1"],["key-2","value-2"]...["key-n","value-n"]]`

#### Attribute value escaping

* The values in the JSON must be written in **lowercase strings** as defined in the <Anchor target="_blank" href="https://www.w3docs.com/snippets/java/how-should-i-escape-strings-in-json.html">JSON standard</Anchor>.

#### JSON spaces

* The JSON must be compacted. It should not contain any blanks, tabs, or newline characters between the values.

#### Signature algorithm

* Use HmacSHA256 with the secret key to create the signature for the JSON
* Encode the signature with Base64 **without** padding
* Add the signature to the click URL with a parameter signature\_v2

```json
//generate a signature from the click url and encode it with base64 without padding String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(jsonString.getBytes()));
```

### Signature example

<div id="building-a-signature-example" />

<Accordion title="Building a signature example">

Example OneLink (multi-platform) click URL:

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&clickid=sdkfjasksjskdfj9845weh&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615
```

Example json object for signature (before removing blank spaces):

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

Example json object for signature (after removing blank spaces)

```json
[["link_domain","yourbrand.onelink.me"],["link_path","qswl"],["pid","mediasource_int"],["template-id","qswl"],["af_siteid","my_site"],["clickid","12345"],["expires","1689695615"]]
```

Final click URL with the signature:

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615  
&signature_v2=WIfCmfLAPSsVrBTqCqfihMeLCnbE4dIAlhHF84WsiWA
```

</Accordion>

### Code examples

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

## Click signature APIs

AppsFlyer provides APIs that allow ad networks to manage and test the click signing process. See the list of APIs in the table below, and the sections that follow with information necessary for using the API. 

#### Click signature APIs

| API method | Remarks |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">Generate secret key</Anchor> | Generate secret keys to be used in the signature. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">Revoke secret key</Anchor> | Cancel compromised secret keys. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">Test</Anchor> | Send single clicks for testing the signature. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">Configure mode</Anchor> | Configure mode of click signing mode:<ul><li>**disabled** (default): No click signature validation is done.</li><li>**report-only** (testing mode): AppsFlyer validates click signatures, but doesn't block clicks with invalid signatures. The ad network can use the **Report API** to get statistics on successful/failing clicks. Use this to test click signing without impacting production and real traffic.</li><li>**enabled:** AppsFlyer blocks clicks with invalid or missing signatures.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-circuit-breaker-put">Configure circuit breaker</Anchor> | Configure the mode of the circuit breaker that protects the ad network from having too many blocked clicks:<ul><li>**enabled** (default): If the Protect360 system detects that too many clicks are marked as invalid, then in order to protect the ad network from having potentially incorrectly blocked clicks:<ul><li>Configure mode API changes to report-only.</li><li>And email alert is sent to the ad network to verify the click signing API is correctly set up.</li></ul></li><li>**disabled**: Protect360 continues to block all clicks marked as invalid, even when the block percentage is unusually high.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">Get configuration</Anchor> | Get the mode and IDs of active secret keys. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">Report</Anchor> | Get the last 3 days statistics on successful and failing clicks when the system is in **report-only** or **enabled** mode. Use this to test click signing without impacting production and real traffic. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">Exclude app</Anchor> | Configure app IDs to be excluded from click signing. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">Remove excluded app</Anchor> | Configure app IDs to be included in click signing after being excluded. |

## Legacy versions

These versions should not be used and are listed for reference only

<div id="v1-legacy" />

<Accordion title="V1 - Legacy">

### Generate secret key method

<div id="generate-secret-key-basics" />

<Accordion title="Generate secret key basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>POST</code></td></tr><tr><td>Path</td><td><span><code>https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=&lt;ttlHours&gt;</code></span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Secret key returns in a JSON</td></tr><tr><td> </td><td>Request limit</td><td>Maximum of 2 active secret keys at a time</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="API request">

**Method**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

#### Parameters

| Parameter | Description |
| --- | --- |
| ttlHours | <ul><li>Time to live for the secret key, in hours, from 1-1440 hours.</li><li>Default is 36 hours.</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="JSON response">

| **Key** | **Description** |
| --- | --- |
| secret-key-id | An ID for the secret key |
| secret key | The secret key for the click signature |
| expiration | Epoch time in milliseconds |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="Generate secret key curl example and response">

**Curl request**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON response**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Revoke secret key method

<div id="revoke-secrete-key-basics" />

<Accordion title="Revoke secrete key basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>DELETE</code></td></tr><tr><td>Path</td><td><span><code>https://hq1.appsflyer.com/api/p360-click-signing/secret/&lt;secret-id&gt;</code></span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Empty</td></tr></tbody></table>

</Accordion>

<Accordion title="API request">

**Method**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

#### Parameters

| Parameter | Description |
| --- | --- |
| secret-id | The ID of the secret key to be revoked |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="Generate secret key curl example and response">

**Curl request**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Test method

<div id="test-basics" />

<Accordion title="Test basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>POST</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/test</span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Returns in a JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="API request">

**Method**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

#### Parameters

| Parameter | Description |
| --- | --- |
| url | The click URL (including signature) to test |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="JSON response">

| **Key** | **Description** |
| --- | --- |
| test-status | Either Passed or Failed |
| message | Reason for the test failure. For example:<ul><li>Missing signature</li><li>Invalid signature</li><li>Expired</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="Test curl example and response">

**Curl request**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**JSON response**

```json
{
	"test-status":"Passed / Failed",
	"message": "Invalid signature"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Configure mode method

<div id="configure-mode-basics" />

<Accordion title="Configure mode basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>POST</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>mode/&lt;mode&gt;</strong></span></span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Returns in a JSON</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="API request">

**Method**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

#### Parameters

| Parameter | Description |
| --- | --- |
| mode | Options:<ul><li>enabled<br />**Note!** Only set the mode to "enabled" after you run in report-only mode for few hours and check your reports to ensure the configuration is correct and that all clicks passed signature validation.</li><li>disabled</li><li>report-only</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="Configure mode curl example">

**Curl request**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | Invalid mode |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Configure circuit breaker method

<div id="configure-circuit-breaker-basics" />

<Accordion title="Configure circuit breaker basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>POST</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td><span>HTTP status</span></td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::ef73eae0" />

<Accordion title="API request">

**Method**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```

#### Request body JSON

| Parameter | Description |
| --- | --- |
| status | <ul><li>enabled</li><li>disabled</li></ul> |

</Accordion>

<div id="configure-circuit-breaker-curl-example-and-response" />

<Accordion title="Configure circuit breaker curl example and response">

**Curl request**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<div id="http-response-codes::d35e3a62" />

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | Invalid status |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Get configuration method

<div id="get-configuration-basics" />

<Accordion title="Get configuration basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>GET</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config</span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Returns in a JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="API request">

**Method**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="JSON response">

| **Key** | **Description** |
| --- | --- |
| mode | One of:<ul><li>enabled</li><li>disabled</li><li>report-only</li></ul> |
| circuit-breaker-config | A JSON object containing **status**, one of:<ul><li>enabled</li><li>disabled</li></ul> |
| active-key-ids | A JSON array holding active keys:<ul><li>**secret-key-id**: Randomly-generated ID of the secret key</li><li>**expiration**: Epoch time in milliseconds of the secret key</li></ul> |
| excluded-app-ids | A JSON array with excluded app-ids |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="Get configuration curl example and response">

**Curl request**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**JSON response**

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

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Report method

<div id="report-basics" />

<Accordion title="Report basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>GET</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/report</span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Returns in a CSV</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<div id="api-request::b28cedb0" />

<Accordion title="API request">

**Method**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

#### Parameters

<table><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>start-date</td><td>Start date and time for the report. Format: yyyy-mm-ddThh</td></tr><tr><td>end-date</td><td><span>End date and time for the report. Format: yyyy-mm-ddThh</span></td></tr><tr><td colspan="2"><span>The API requires either <strong>both</strong> start-date and end-date or <strong>neither</strong> of them. If start/end date are not provided, the report shows results for the past 24 hours.</span></td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="CSV response">

| **Column** | **Description** |
| --- | --- |
| time | Date and time of the clicks. Format yyyy-mm-ddThh |
| total\_clicks | Total number of clicks during the reporting period |
| valid\_clicks | Number of valid clicks during the reporting period |
| missing\_signature | Number of clicks missing signatures during the reporting period |
| expired\_clicks | Number of expired clicks during the reporting period |
| invalid\_signature | Number of clicks with invalid signatured during the reporting period |
| no\_active\_secrets | Number of clicks rejected because there are no active secret keys in the system (usually when the system is in report-only mode) |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="Test curl example and response">

**Curl request**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/report?start-date=2021-01-07T07&end-date=2021-01-17T12' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**CSV response**

| **time** | **total\_clicks** | **valid\_clicks** | **missing\_signature** | **expired\_clicks** | **invalid\_signature** | **no\_active\_signatures** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Exclude app method

<div id="exclude-app-method-basics" />

<Accordion title="Exclude app method basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>POST</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>excluded-app/&lt;app-id&gt;</strong></span></span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Empty</td></tr></tbody></table>

</Accordion>

<div id="api-request::1054abca" />

<Accordion title="API request">

**Method**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

#### Parameters

| Parameter | Description |
| --- | --- |
| app-id | Application ID to be excluded from click signing validation |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="Exclude app curl example">

**Curl request**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::90a409c" />

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

### Remove excluded app method

<div id="remove-excluded-app-method-basics" />

<Accordion title="Remove excluded app method basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>DELETE</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>excluded-app/&lt;app-id&gt;</strong></span></span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows:  <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a>  </li></ul></td></tr><tr><td>Response</td><td>Results</td><td>Empty</td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<div id="api-request::9504d16f" />

<Accordion title="API request">

**Method**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

#### Parameters

| Parameter | Description |
| --- | --- |
| app-id | Application ID to be removed from the list of apps excluded from click signing validation |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="Remove excluded app curl example">

**Curl request**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::8454f45d" />

<div id="http-response-codes::7991b66" />

<div id="http-response-codes::b5e059da" />

<Accordion title="HTTP response codes">

#### Response codes

| Code | Message | Remarks |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Not authorized | Invalid or missing authorization header |

</Accordion>

<div id="code-sample" />

<Accordion title="Code sample">

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

## Additional information

<div id="troubleshooting" />

<Accordion title="Troubleshooting">

AppsFlyer stops click signature validation and reverts to the report-only mode when more than 90% of clicks in an hour fail signature validation.

This is to protect your business from a potential technical issue and allows you to find the cause of the anomaly:

* If you find that the signature is working as expected and the clicks are being correctly blocked, disable the circuit-breaker using the [configure circuit breaker method.](/docs/click-signing-for-ad-networks#configure-circuit-breaker-method)
* If you find that clicks are being incorrectly blocked:
  1. Make sure that you have a valid secret key by checking the click signing configuration using the [get configuration method.](/docs/click-signing-for-ad-networks#get-configuration-method)
  2. Use the [click signing report](/docs/click-signing-for-ad-networks#report-method) to get more information about the blocked clicks and investigate the sources (agency/app- iDs) and reasons for invalid clicks.
* If you find a problem with a specific app because of a non-standard integration, exclude this app from click signing validation using the [exclude app API.](/docs/click-signing-for-ad-networks#exclude-app-method)
* If you find a problem with your configuration:
  1. Continue running in report-only mode.
  2. Fix the click signing process on your side.
  3. Check the results in the [click signing report](/docs/click-signing-for-ad-networks#report-method) and re-enable click-signing validation when you see that clicks are being validated as expected.

</Accordion>

<div id="faq" />

<Accordion title="FAQ">

| **Q: How can we test click signing without impacting production?**<br /><br />**A**: There are two ways to test click signing:<ol><li>Use the [test API](/docs/click-signing-for-ad-networks#test-method). This method is useful during the development phase, to test the signatures of single clicks.</li><li>Use report-only mode. Report-only mode verifies the signatures on the production clicks and shows you what would be blocked, but doesn't block invalid clicks. Therefore, you can test that click signing works without impacting real traffic.</li></ol> |
| --- |
| **Q: What is the difference between an API token and a secret-key?**<br /><br />**A**: **API token**: Is used to authorize and run the click signing API. There is only one per ad network. The <Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">AppsFlyer API V2.0 token</Anchor> must be obtained from the admin<br /><br />**Secret key**: Is used to generate the signature. Use the [generate secret key method](/docs/click-signing-for-ad-networks#generate-secret-key-method) to create secret keys. The ad network is responsible for generating new secret keys. See the [traits section](/docs/click-signing-for-ad-networks#traits) for more information. |
| **Q: Can we apply click signing to only certain campaigns?**<br /><br />**A**: No. Click signing is applied to all clicks from an ad network. You can exclude certain apps from click signing, but you can’t exclude only certain campaigns. |

</Accordion>

<div id="traits" />

<Accordion title="Traits">

| Trait | Description |
| --- | --- |
| Click signature | The signature must occur on the ad network servers. |
| Secret key | <ul><li>Ad networks can have a maximum of two secret keys active simultaneously.</li><li>Each secret key has an expiration.</li><li>Clicks signed with expired secret keys are rejected.</li></ul> |
| Report API | Updated statistics of click validity are aggregated on an hourly basis. |

</Accordion>

<div data-zendesk-anchors="h_01HNWC70BPGDJAG3X8M5Z2RHQ4=about-click-signing h_01HNWC70BPFYMZ56GTPV3W6DXA=click-signature-integration h_01HNWC70BPMXTKF9NZBYGCB874=flow h_01HNWC70BPHCAGD1ECA56CC1Q6=procedure h_01HNWC70BPAR4QNTNSFE1JZM2J=note list-of-attributes=creating-a-click-signature h_01HP4A42YYFFF6M4VEH84KRTTK=creating-a-click-signature h_01HNWD3XYWFRY262HZZVAVWACR=list-of-attributes attribute-rules=attribute-and-json-rules h_01HNWE3A19RM7757B707TWZ6G0=attribute-and-json-rules h_01HNWE3A1920YQGZX2VG4X3M4B=order-and-appearance-of-attributes h_01HNYRZ1DPDDQ5H8RFYKAQWVKP=empty-attributes h_01HNYS6R7F0MNPBN08TXKQS5DV=json-data-structure h_01HNYSEBGD1DBSV2MHS7DZ75HS=attribute-value-escaping h_01HNYSY42HS1RXFG7T7QS9B0TK=json-spaces h_01HNYSJDFWAM9RREYH4M8DZQJA=signature-algorithm h_01HP3YAN03BWVA30JP1JAFZYAG=signature-example h_01HP3Y2Z65BN0SZ56XSHD52MSY=building-a-signature-example code-example=code-examples h_01HNYT8Z33M69JAS72MQ03YX0M=code-examples h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego h_01HNWC70BPNEVT00S040TQ9KVD=click-signature-apis click-signature-apis::58bf03c7=click-signature-apis-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=click-signature-apis-1 h_01HNZ3YMFRWFDY751EBA58V6Q0=legacy-versions h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy h_01HNWC70BPBPSX1WKJJC2W6H69=generate-secret-key-method h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request h_01HNWC70BPS83JD78JWQYK1NX9=parameters h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes h_01HNWC70BPMQ8Q94JD5CBT5RHZ=response-codes h_01HNWC70BP8V05Q04J6EVGAS9T=revoke-secret-key-method h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=parameters-1 h_01HNWC70BPQ5S06E210RTE7E6R=parameters-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=response-codes-1 h_01HNWC70BPN18MB98KWND886QN=response-codes-1 h_01HNWC70BPKEVRDMT8N4HMC98W=test-method h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=parameters-2 h_01HNWC70BPKQFVEGWR9QT566YX=parameters-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=response-codes-2 h_01HNWC70BPC43F5H85F56DDSQR=response-codes-2 h_01HNWC70BP6NPF7NSF0MGA4BJ3=configure-mode-method h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=parameters-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=parameters-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=response-codes-3 h_01HNWC70BQZ657X25N8JGM57A1=response-codes-3 h_01HNWC70BQVSFS7G330NF4XHEP=configure-circuit-breaker-method h_01HNWC70BQ097J2VXW0XKSH3M9=configure-circuit-breaker-basics h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 h_01HNWC70BQ6R955776Y6H4EZRG=request-body-json h_01HNWC70BQRZEZ4PTV59FGYS4Z=configure-circuit-breaker-curl-example-and-response h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=response-codes-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=response-codes-4 h_01HNWC70BQZY6TYSQBWZ17S0W5=get-configuration-method h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=response-codes-7 h_01HNWC70BQDGVBZ94F0N49FF40=response-codes-7 h_01HNWC70BQTBMNKHV4RH4ZQ0AE=report-method h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=parameters-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=parameters-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=response-codes-8 h_01HNWC70BQTPPWA4SNG25E8FFB=response-codes-8 h_01HNWC70BQ9SK2XCBGGHXVMRDV=exclude-app-method h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=parameters-5 h_01HNWC70BREG4XQJV3X9518FC5=parameters-5 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=response-codes-8 h_01HNWC70BRN8BHWF6WGY2RH45X=response-codes-8 h_01HNWC70BR18P0H96VN64RS05G=remove-excluded-app-method h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=parameters-6 h_01HNWC70BR4ADH7T3AFG58FZH6=parameters-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=response-codes-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=response-codes-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample h_01HNWC70BRN0NGTQVWED6VG81Y=additional-information h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
