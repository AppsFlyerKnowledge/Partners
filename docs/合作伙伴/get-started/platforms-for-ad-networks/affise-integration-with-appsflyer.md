---
title: AppsFlyer中的Steam对接配置说明
metadata:
  keywords:
    - Integration
    - affise
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
  created_at: '2016-04-19T12:08:58Z'
  edited_at: '2026-10-14T10:07:36Z'
  id: 208537116
  locale: zh-cn
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/zh-cn/articles/208537116
---
> **概要：**

## 基础归因链接

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}&af_c_id={offerid}
```

| AppsFlyer参数 |  | 说明 |
| --- | --- | --- |
| clickid | `{clickid}` |  |
| af\_siteid | `{pid}` |  |
| af\_c\_id | `{offer_id}` |  |


```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}
```



```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}
```


```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}
```

### 3. 全球应用内事件回传。

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}&goal={event-name}
```


```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}&goal={event-name}
```

<div data-zendesk-anchors="base-attribution-link=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT0RZG0F67JFBC7W5KK54BM=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 complete-attribution-link-template=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT0RZG2QTT3Z9S6SVNV5VE7=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 install-and-inapp-event-postbacks=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 global-install-postback-ios=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT0RZG3C7MBBYFKA6W813PF=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT0RZG3HM9P81XYGKHZXHFK=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 global-install-postback-android=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 global-inapp-event-postback-android=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT0RZG4JCDP8D4CWQW02AY7=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 01JFT0RZG4PA9WTP212AX52QWZ=%E5%9F%BA%E7%A1%80%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 global-inapp-event-postback-ios=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 01JFT0RZG40N0VNNVMDBFYNT9E=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 finalizing-your-registration=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 01JFT0RZG52JW6C5GR0KA4CZF6=3-%E5%85%A8%E7%90%83%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0" />
