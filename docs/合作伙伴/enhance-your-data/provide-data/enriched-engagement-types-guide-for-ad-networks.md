---
title: 扩展广告交互类型-广告平台指南
metadata:
  keywords:
    - Advertisers
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2024-10-15T10:54:29Z'
  edited_at: '2026-10-14T10:15:06Z'
  id: 29221265052433
  locale: zh-cn
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/zh-cn/articles/29221265052433
---
> **概要：** 了解如何创建扩展广告交互类型（EET）归因链接，以全面反映用户的广告交互行为，从而实现更准确、更高效的投放优化。

扩展广告交互类型（Enriched Engagement Types）能帮助广告主全面掌握用户在浏览广告或与广告交互时所产生的各种互动层次和意向强度，覆盖了从短暂曝光到即时反馈等各种级别的互动。本文详细说明了合作渠道应如何根据用户与广告的交互方式，在AppsFlyer归因链接中上报相应的交互类型。

> ❗️ **声明**
>
> 本文重点介绍与合作渠道相关的EET内容。如需了解完整信息，请参阅<Anchor target="_blank" href="/marketers/zh/docs/about-enriched-engagement-types#which-ad-networks-report-enriched-engagement-types">扩展广告交互类型</Anchor>文档。

## 哪些广告平台可以向AppsFlyer上报EET？

您的合作渠道必须在AppsFlyer的渠道认证项目中达到Premier、Advance或Engage标准，才能使用扩充互动类型。达到这些标准的渠道具有以下特质：1）向我们的共同客户持续提供大量优质流量，长期表现稳健扎实；2）以透明可信的方式发送互动数据；3）与AppsFlyer的各项服务进行了全面对接。

> 📘 **注意**
>
> 广告平台如需上报深度点击或深度浏览，请联系AppsFlyer支持团队。

查看可上报扩展广告交互类型的[广告平台名单](#01JCAT81K2EJNH91YS6NJGMXMB-data-title)

> ❗️ **警告**
>
> 不在允许范围内的平台若上报带有`af_engagement_type`参数的点击和展示，这些数据会被拦截且不会用于归因。

<div id="engaged-click-or-engaged-view-attribution-flow" />

<Accordion title="深度点击与深度浏览的归因流程">

以下步骤概述了从广告展示到到最终用户激活被归因的完整流程。归因可以基于用户的深度点击或深度浏览完成：

1. 广告平台展示广告。
2. 广告平台向AppsFlyer发送一次展示，其中包含具体的`af_ad_tran_id`。
3. 用户与广告产生交互。
4. 广告平台基于用户行为发送点击或展示，带有`af_engagement_type`，`af_ad_tran_id`，`af_ad_format`，`af_ad_type`，也可包含参数`viewability`。
5. AppsFlyer将激活事件与上报的深度点击或深度浏览进行匹配。
6. AppsFlyer将此次激活归因至对应的广告平台。

</Accordion>

<div id="parameters-for-reporting-engagement-types-in-attribution-links" />

<Accordion title="归因链接中上报交互类型所需的参数">

广告平台可通过在归因链接中添加以下参数以上报用户的交互类型：

* `af_engagement_type`:交互类型，例如`engaged_click`，`click_to_app`或`engaged_view`。详见<Anchor target="_blank" href="/marketers/zh/docs/about-enriched-engagement-types#什么是扩展广告交互类型">交互类型的完整说明</Anchor>。
* `af_ad_type`:广告类型。例如`rewarded_video`, `interstitial`或`banner`。详见`af_ad_type`广告类型的完整说明af\_ad\_type。
* `af_ad_format`:广告格式，例如，`text`，`image`，`video`，`playable`。广告交易ID，用于AppsFlyer将深度点击或深度浏览与之前的展示的进行匹配。
* `viewability`（可选）：关于用户交互的其他信息，例如，`af_video_total_length`，`af_ad_time_viewed`，`af_audio_played_length`。详见`viewability`可见性参数的完整说明viewability。
* `af_ad_tran_id`:广告交易ID，用于AppsFlyer将深度点击或深度浏览与之前的展示的进行匹配。
* `is_skoverlay=true`或`is_autostore=true`：用于识别[SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay)或Android Auto Inline Install触发的深度浏览。

**深度点击示例链接**

```http HTTPS
https://app.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_click&af_ad_type=interstitial&af_ad_format=playable&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0
```

**深度浏览示例链接**

```http
https://impression.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_view&af_ad_type=interstitial&af_ad_format=video&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0&af_video_total_length=20&af_video_played_length=15
```

</Accordion>

<div id="user-engagements-to-report-as-engaged-clicks" />

<Accordion title="上报为深度点击的用户交互行为">

*深度点击*是指用户点击广告后，仍留在原有场景内继续与广告内容进行交互，不跳转到应用商店或直接打开应用。

x广告平台应在以下场景中使用参数`af_engagement_type=engaged_click`进行上报：

* **试玩广告：** 与试玩广告交互，例如点击小游戏或广告中的交互内容。
* **社交交互：** 点赞、评论或分享在社交平台上分享广告，以促进进一步交互和传播。
* **跳转：** 点击跳转至落地页或外部内容/页面。
* **动态产品广告/目录或轮播：** 点击滑动浏览不同产品。
* **添加到心愿单：** 在应用内部或外部网站将推广的产品加入愿望清单或收藏。
* **保存：保存广告或其内容以备未来参考，表明用户有兴趣再次查看广告或进一步探索。**
* **添加书签或添加到收藏夹：** 点击将广告加为书签或添加到应用内的精选收藏夹，表明有意再次查看或分类广告。
* **取消静音广告：** 点击以启用音频。

**哪些交互行为不作为深度点击上报？**

以下使一些**不作为**`engaged_click`参数上报的例子：

* **广告关闭：** 点击“x”或类似按钮关闭或忽略广告，表明用户无意进行进一步交互。
* **跳过广告**：点击按钮跳过广告，表明广告未能吸引用户或相关度低。
* **举报广告**：点击举报广告，原因可能是广告内容令人反感、具有误导性或不恰当，表明用户对广告内容的不满。
* **不同意展示广告或取消订阅**：点击取消订阅或不再接收类似广告，表明用户不想继续与该广告或其类别交互。
* **退出广告：** 点击链接或按钮退出当前广告，将用户引导到广告内容或落地页之外的地方。
* **静音广告**：将视频静音。

</Accordion>

<div id="user-engagements-to-report-as-engaged-views" />

<Accordion title="上报为深度浏览的用户交互行为">

在以下场景中，广告平台应使用参数`af_engagement_type=engaged_view`进行上报：

* **可跳过广告：用户在“跳过”按钮出现后，观看广告至少5秒。若平台无法衡量观看时长，则可采用以下逻辑：
  * 当视频长度超过20秒时，在观看到2/4时（50%）发送`engaged_view`。
  * 当视频短于20秒时，在视频完成（100%）时发送`engaged_view`。
  * `af_ad_format`参数值必须是`video`或`playable`。**
* **激励视频：** 用户完整观看奖励视频。`af_ad_type`参数值必须是`rewarded_video`。
* **自动StoreKit广告：*** 渲染型广告（[`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay)和[`SKStore`](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)）的点击不会由发布方记录，而是由Apple用于SKAdNetwork（SKAN）归因。Android自动內联式激活广告（autostore）也遵循类似机制。

  由于广告平台无法判断用户是否实际与这类广告产生交互，因此会在广告展示时上报点击或展示，即便用户未进行交互。

  虽然广告平台可以选择在广告展示时上报`click_to_app`交互类型，但这样的做法会导致CTR（点击率）异常偏高。Android自动內联式激活广告（autostore）也遵循类似机制。

  为了规避此类风险，推荐广告平台使用`engaged_view`类型上报。在此类情景中，归因链接中必须包含`is_skoverlay=true`（iOS）或`is_autostore=true`（Android）。

**哪些交互行为不作为深度浏览上报？**

在以下情境中，应使用`view`参数**而非**`engaged_view`进行上报：

* 用户完整观看了一条不可跳过的视频广告，但该广告不是激励视频，且未通过`SKOverlay`或`autostore`机制展示。

</Accordion>

<div id="01JCAT81K2EJNH91YS6NJGMXMB-data-title" />

<Accordion title="支持EET的广告平台">

AppsFlyer可处理以下合作渠道上报的EET，但目前不包括深度点击与深度浏览。如名单中的广告平台希望AppsFlyer处理深度点击或深度浏览，请与AppsFlyer技术支持团队联系。如需查看AppsFlyer可处理哪些广告平台上报的深度点击与深度浏览，请参考<Anchor target="_blank" href="/marketers/zh/docs/about-enriched-engagement-types#哪些广告平台可以上报深度浏览和深度点击">扩展广告交互类型广告主指南</Anchor>。

> ❗️ **警告**
>
> 不在允许范围内的平台若上报带有`af_engagement_type`参数的点击和展示，这些数据会被拦截且不会用于归因。

| 渠道名称 |
| --- |
| AdColony |
| Adaction |
| Adaction3 |
| Adikteev |
| adjoe GmbH |
| Amazon |
| Amazon DSP |
| AppLovin |
| Appier |
| Appnext |
| Apple Search Ads |
| Aura from Unity |
| AWIN |
| Bidease |
| 巨量引擎 |
| Cauly |
| Criteo |
| Digital Turbine |
| Digital Turbine On Device |
| Fluent |
| Glance |
| Google Ads（AdWords） |
| Google Marketing Platform（DV360/CM360） |
| Hotstar |
| 华为 |
| InMobi DSP |
| ironSource |
| Jampp |
| Josh |
| Kakao |
| 快手 |
| Liftoff |
| Line |
| Meta ads |
| Mintegral |
| Mistplay |
| Motorola Pre-Install |
| Naver |
| OPPO |
| OPPO Global |
| OPPO Store Traffic(Global) |
| OPPOPAI Pre-Install |
| PayTM |
| Rakuten |
| Reddit |
| Remerge |
| RevX |
| Samsung |
| Smadex |
| Snapchat |
| Stackadapt |
| Tapjoy |
| 腾讯AMS |
| TikTok For Business - 高级SRN |
| TikTok for Business - 历史对接 |
| The Trade Desk |
| Transsion |
| Treasure Data |
| Truecaller |
| Unity Ads |
| Vivo Preload |
| vivo Global |
| Vungle |
| X Ads（前身为Twitter Ads） |
| Xiaomi Global |
| XiaomiPAI Pre-Install |
| Yahoo Japan |
| Yandex |
| YouAppi |

</Accordion>

<div data-zendesk-anchors="01JA7WZH43ECDKRC0R0J89ED1E=%E5%A3%B0%E6%98%8E which-networks-can-report-eet-to-appsflyer=%E5%93%AA%E4%BA%9B%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%8F%AF%E4%BB%A5%E5%90%91appsflyer%E4%B8%8A%E6%8A%A5eet h_01JJPVYGWZSFSATZ4TH5VBSVXW=%E5%93%AA%E4%BA%9B%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%8F%AF%E4%BB%A5%E5%90%91appsflyer%E4%B8%8A%E6%8A%A5eet 01JAN5JRM56C6S6EP27WFJ2Y4W=%E6%B3%A8%E6%84%8F h_01J00XFV133YYAB7YPQNXM5R37=%E8%AD%A6%E5%91%8A 01JA7WZH46RJBG996NG9EZV7T9=engaged-click-or-engaged-view-attribution-flow 01JA7WZH4BZVGS9Z1NNHQC72N6=parameters-for-reporting-engagement-types-in-attribution-links 01JA7WZH4JDJFCVT25WJ4GNE20=user-engagements-to-report-as-engaged-clicks 01JA7WZH4Q32TEWM5EKME142R7=user-engagements-to-report-as-engaged-views 01JCAT81K2EJNH91YS6NJGMXMB%20data-title%3D=01JCAT81K2EJNH91YS6NJGMXMB-data-title allowed-network-list=01JCAT81K2EJNH91YS6NJGMXMB-data-title h_01JJPVYGWZ4T6TPFRWTR2AB027=%E8%AD%A6%E5%91%8A-1" />
