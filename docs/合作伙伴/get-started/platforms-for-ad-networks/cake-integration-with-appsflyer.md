---
title: AppsFlyer中的Xbox对接
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
  created_at: '2016-01-11T14:44:55Z'
  edited_at: '2026-10-14T10:10:22Z'
  id: 207273986
  locale: zh-cn
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/zh-cn/articles/207273986
---
> **概要：**

## 基础归因链接

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

|  | 说明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id |  |
| pid |  |
| c | 即广告系列的名称 |


| <span id="recommended-attribution-link-parameters"></span>AppsFlyer参数 |  | 说明 |
| --- | --- | --- |
| clickid | #oreqid# |  |
| af\_siteid | #affid# |  |


```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#oreqid#
```



```http
https://{company-domain}.com/p.ashx?f=pb&r=(Click-ID)
```

### 3. 全球应用内事件回传。

```http
Click-ID
```

<div data-zendesk-anchors="base-attribution-link=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01EZPMKP0AFM26H2ZG9FY1D2S4=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01EZPMKP0A7DBV5KAGZ08C3R49=recommended-attribution-link-parameters complete-attribution-link-template=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01EZPMKP0AH1MB0XYE3PXQPP0V=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 install-and-inapp-event-postbacks=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 global-install-postback=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01EZPMKP0A2D0PB41GD04HX9JX=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01EZPMKP0AVAJRP8YM48T4GV47=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 global-inapp-event-postback=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 01EZPMKP0AM7JD7HWW7BCJDQF3=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 appsflyer-inapp-events-dashboard=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 finalizing-your-registration=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 01EZPMKP0AJTYT0G9E8G833KT0=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 h_01HY03H1PMWZX3T12RZFV15CFE=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0" />
