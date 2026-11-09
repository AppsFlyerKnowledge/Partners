---
title: AppsFlyer中的Steam对接配置说明
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-01-11T14:46:09Z'
  edited_at: '2026-10-14T10:03:16Z'
  id: 207274016
  locale: zh-cn
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/zh-cn/articles/207274016
---
> **概要：**

<div id="finalizing-your-registration" />

<div id="appsflyers-in-app-event-dashboard" />

<div id="install-and-in-app-event-postbacks" />

<div id="complete-attribution-link-template" />

<div id="starting-the-integration" />

## 测试对接

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

|  | 说明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id |  |
| pid= |  |
| c= | 即广告系列的名称 |

| AppsFlyer参数 |  | 说明 |
| --- | --- | --- |
| &clickid= | `{clickid}` |  |
| &af\_siteid= | `{trafficsource.id}` |  |


```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```


```http
https://{Company-Domain}.voluumtrk.com/postback?cid={clickid}
```

3. 全球应用内事件回传。

```http
https://{Company-Domain}.trackvoluum.com/postback?cid={clickid}&payout={monetary}&txid={event-name}
```


<Image align="center" alt="Voluum_msc_new_1.png" src="https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png" />

<div data-zendesk-anchors="starting-the-integration=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 01JFT0VZZ5KVMKYRD222JT55NH=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 complete-attribution-link-template=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 01JFT0VZZ7B1RRY82B65GWF4P7=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 install-and-inapp-event-postbacks=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 01JFT0VZZ86KYXSVE1QBD2V0HF=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 appsflyers-inapp-event-dashboard=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 finalizing-your-registration=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 01JFT0VZZ9A4JWG38KPH0CNQ72=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 01JFT0VZZATFYY75QPCPKZF3S6=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5" />
