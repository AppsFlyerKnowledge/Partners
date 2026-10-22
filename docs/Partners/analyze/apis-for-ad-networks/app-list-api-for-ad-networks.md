---
title: App list API for ad networks
metadata:
  keywords:
    - API
    - Ad Networks
    - Partners
    - Developers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-08-06T20:11:15Z'
  edited_at: '2026-05-05T07:03:21Z'
  id: 360011700857
  locale: en-us
  section: APIs for ad networks
  section_id: 6551618728209
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360011700857-App-list-API-for-ad-networks
---
> **At a glance:** Ad networks can retrieve metadata of apps associated with their integrated partner account.

## Get app list API

The following sections include information necessary for using the API.

<div id="get-app-list-basics" />

<Accordion title="Get app list basics">

<table><thead><tr><th>Category</th><th>Item</th><th><span>Description</span></th></tr></thead><tbody><tr><td rowspan="3">Request</td><td>HTTP method</td><td><code>GET</code></td></tr><tr><td>Path</td><td><span>https://hq1.appsflyer.com/api/mng/apps</span></td></tr><tr><td>Authorization header </td><td><ul><li>The mandatory authorization header contains a Bearer token. </li><li>The admin gets the token in the dashboard as follows: <a href="/marketers/docs/managing-appsflyer-tokens" target="_blank">The Admin goes to email drop-down list &gt; API tokens to get the V2.0 token</a></li></ul></td></tr><tr><td rowspan="3"> Response</td><td>Results</td><td>Return in JSON</td></tr><tr><td>Request limit</td><td><ul><li>20 requests/minute</li><li>100 requests/day</li></ul></td></tr><tr><td>Record limit</td><td>1,000 records/request. If more than 1,000 records are to be returned, use follow-on pagination requests, described in this article.</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="API request">

The API request consists of the method, path, mandatory capabilities parameter, and optional pagination parameters. The token is contained in the authorization header.

**Method**

```http
GET https://hq1.appsflyer.com/api/mng/apps?capabilities={capabilities} 
```

#### Get app list mandatory parameters

<table><thead><tr><th>Query parameter</th><th>Description</th></tr></thead><tbody><tr><td>capabilities</td><td><p>To get the list and number of apps to which you have permission/integration capabilities: set the capabilities parameter to one of the options listed. </p><figure><table><thead><tr><th>Option</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>protect_360</code></td><td>Report permission</td><td>Get <a href="./protect360-for-integrated-partners" target="_blank">Protect360 raw data reports for ad networks</a></td></tr><tr><td><code>cost</code> </td><td>Integration</td><td>App is enabled to get cost data <a href="./incost-api-for-ad-networks" target="_blank">via InCost API</a></td></tr></tbody></table></figure><p><strong>Example</strong>: List of apps for which you have Protect360 report API permission:<code>capabilities=protect_360</code></p></td></tr></tbody></table>

#### **Pagination mechanism**

A pagination mechanism, always operational, is implemented.

**Pagination principles:**

* Returns up to 1,000 records per request (page).
* Response JSONs contain the following pagination related keys:
  * **meta.total\_items**: The number of records to be returned by all pages combined. This represents the number of apps for which you have been granted the capabilities being queried.
  * Pagination links (depicted in the JSON that follows) have the following keys:
    * **links.prev**: If there was a previous request: the request used to generate the previous page.
    * **links.self**: The current request: the request used to generate the current JSON (page)
    * **links.next**: The request required to get the next page. If there is no next key, this is the last page.

**Use one of the following pagination control methods:**

* [Best practice] Use the links in the JSON: If the links.next key exists, use it to create a request to get the next page. Continue to do so until you receive a JSON without a links.next key.
* Programmatically implement limit and offset parameters in conjunction with the total\_items key.

**Pagination links JSON example**

* The example that follows contains the result of the first request, consisting of the second request containing two records in the data section (not displayed).
* The total number of records to return is 6.
* The **links.next** key contains the request that returns the next page—records 5 and 6.

```json
{                                                                                         
    "data": {[...]},   
    "meta": {
        "total_items": 6
    },
    "links": {
        "prev": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=2",
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=2&limit=2",
        "next": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=4&limit=2"
    }
}
```

#### Pagination mechanism parameters (optional)

<table><thead><tr><th>Query parameter</th><th>Description</th></tr></thead><tbody><tr><td>limit</td><td><p>Number of records that return per call</p><ul><li>Maximum: 1,000</li><li>If you don't send<code>limit</code>, it is automatically set to 1,000.</li><li>Example: <code>limit=2</code></li><li>Mandatory: No</li></ul></td></tr><tr><td>offset</td><td><p>The first record to return in the call. Record numbers start with 0. </p><ul><li>If you don't send <code>offset</code>, it is automatically set to 0.</li><li>Example: <code>offset=2</code></li><li>Mandatory: No</li></ul></td></tr><tr><td colspan="2"> </td></tr></tbody></table>

</Accordion>

<div id="json-response" />

<Accordion title="JSON response">

| **Key** | **Description** |
| --- | --- |
| id | App ID, for example: `id123456789`, `com.myapp.com` |
| type | Always return `app` |
| name | App name |
| platform | iOS or Android |
| currency | App-specific currency code as set by the advertiser |
| time\_zone | App-specific timezone as set by the advertiser |
| total\_items | Number of apps to which the ad network has the requested capabilities option |
| links | Pagination mechanism (explained in the parameters section)<ul><li>prev: the call used to generate the previous page</li><li>self: the call used to generate the current page</li><li>next: the call used to generate the next page</li></ul> |

</Accordion>

<div id="get-app-list-curl-example-and-response" />

<Accordion title="Get app list curl example and response">

**Curl request**

This example includes a complete call, including optional pagination parameters.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&limit=1000&offset=0' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**JSON response**

```json
{
    "data": [
        {
            "id": "com.appsflyer.xpend_qa1",
            "type": "app",
            "attributes": {
                "name": "com.appsflyer.xpend_qa1",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC"
            }
        },
        {
            "id": "com.abc.app",
            "type": "app",
            "attributes": {
                "name": "com.abc.app",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC",
                "enable_retargetting": true
            }
        },
        {
            "id": "com.xyz.app",
            "type": "app",
            "attributes": {
                "name": "com.xyz.app",
                "platform": "android",
                "currency": "JPY",
                "time_zone": "UTC"
            }
        }
    ],
    "meta": {
        "total_items": 3
    },
    "links": {
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=1000"
           }
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="HTTP response codes">

| Code | Message | Remarks/troubleshooting |
| --- | --- | --- |
| 200 | OK | Valid data returned |
| 200 | OK | **Symptom**: No data returns<br /><br />**Action**: Make sure the authentication token is in the bearer header. |
| 400 | Bad request | <ul><li>See the message contained in the JSON</li><li>Empty JSON: illegal capability specified</li></ul> |
| 401 | Unauthorized | **Message**: Authorization token is malformed<br /><br />Make sure you have the correct token; token must have 700+ characters. |
| 404 | Not found | <ul><li>Handle any network or firewall-related problems.</li><li>Make sure that AppsFlyer <Anchor target="_blank" href="/marketers/docs/appsflyer-server-ip-address-ranges-allowlisting">IP addresses are allowlisted</Anchor></li><li>Make sure you use the most recently-issued token.</li><li>No data found: The permission/integration (capabilities) type requested is legal, but no apps with permission were found.</li></ul> |
| 429 | Too many requests | Exceeded rate limitation |

</Accordion>

<div data-zendesk-anchors="h_01KQS54YXJ2XBV5BAT3TGJ9SBT=get-app-list-api h_01KQS54YXJHYS9KC2Y7BEP87MZ=get-app-list-basics h_01KQS54YXJJ9SE7DSRTA2X2A9M=api-request h_01KQS54YXJPDZGJB7K6KH1D2W1=get-app-list-mandatory-parameters h_01KQS54YXJ9X0XBJQ01K6WK2RB=pagination-mechanism h_01KQS54YXJX943PMF5JWV67THW=pagination-mechanism-parameters-optional h_01KQS54YXJS43JYQQHCWCAED6Q=json-response h_01KQS54YXJJK7Y23TSSF1BB58R=get-app-list-curl-example-and-response h_01KQS54YXJ2638DBZWDSN4J9G4=http-response-codes" />
