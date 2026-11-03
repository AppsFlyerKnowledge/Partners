---
title: AppsFlyer中的Steam对接配置说明
metadata:
  keywords:
    - Focuus
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-10-02T05:18:19Z'
  edited_at: '2026-10-14T09:59:06Z'
  id: 213374546
  locale: zh-cn
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/zh-cn/articles/213374546
---
> **概要：**


<span id="creating-your-attribution-link"></span>请参阅下列AppsFlyer基本归因链接，附有每个宏的详细说明：

|  | 说明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id |  |
| pid |  |
| c | 即广告系列的名称 |


| AppsFlyer参数 |  | 说明 |
| --- | --- | --- |
| **clickid** | **`{tid}`** |  |
| af\_siteid | `{publisher_id}` |  |


`https://app.appsflyer.com/com.appsflyer?pid={traffic_source}&clickid={tid}&af_siteid={publisher_id}`


4. `https://pixel.focuusing.com/event.php?type=imp&tid={clickid}`

|  | 说明 | 示例 |
| --- | --- | --- |
| event\_value |  |  |

* `https://traffic.focuusing.com/install?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/conversion?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/ftd?tid={TRANSACTION_ID}`

<div data-zendesk-anchors="01JFT11W3GWZ3QFYPHEZTS7EX7=creating-your-attribution-link" />
