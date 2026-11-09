---
title: CTV到移动应用程序的视图归因用于广告网络
metadata:
  keywords:
    - Attribution
    - Ad Networks
    - Partners
    - CTV
    - CTV Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roi-tamir
    - CTV Attribution
    - Ad Networks
  created_at: '2022-08-21T06:49:24Z'
  edited_at: '2026-10-14T10:08:32Z'
  id: 8528418936977
  locale: zh-cn
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/zh-cn/articles/8528418936977
---
> **概要：概要：本文解释了如何将应用激活归因到用户在CTV设备上浏览的广告。**

<div id="ctv-to-mobile-app-attribution-for-ad-networks" />

## CTV到移动应用程序的归因用于广告网络

您可以利用AppsFlyer的跨平台展示链接将应用激活归因到CTV上展示的广告。同一住宅内的多次激活可以归因到同一个CTV广告展示。

<Image align="center" alt="50310_CTV_flow_chart__2_.jpg" src="https://files.readme.io/401bcb083e1cc618794cb302668f7271cf825a5a6045ff10055e0164baf423a1-19774176963473.jpg" />

CTV到移动应用程序的视图归因使用一个<Anchor target="_blank" href="/marketers/zh/docs/set-up-cross-platform-links-for-multi-device-campaigns#setup">OneLink展示URL</Anchor>，基于广告主创建的跨平台OneLink模板（带有模板ID）。这使广告主能够使用单个URL对来自不同平台的多个应用程序（例如，Android和iOS应用程序）进行分组。

当用户在CTV上查看广告时，您实时向AppsFlyer发送展示URL。

URI示例

```http
https://impressions.onelink.me/{template_id}?pid=__media_source__&af_xplatform=true&af_xplatform_vt_lookback=24h&af_siteid=__CSITE__&c=__CAMPAIGN_NAME__&af_channel=__PLACEMENT__&af_c_id=__CAMPAIGN_ID__&af_adset=__AID_NAME__&af_adset_id=__AID__&af_ad=__CID_NAME__&af_ad_id=__CID__&af_source_platform=__source_platform__&af_source_device_category=__device_category__&af_ad_type=__CTYPE__&af_ip=__IP__&af_ua=__UA__&redirect=false
```

每次转化后会向您发送回调。

<div id="note" />

> 📘 **注意**
>
> 此功能仅对指定合作伙伴可用。如果您感兴趣，请联系您的合作伙伴发展经理（PDM）。

<div id="setup" />

<Accordion title="设置方式">

**要与广告主设置CTV到移动应用程序的视图归因**：

1. 确保您是一个 AppsFlyer 的已对接广告平台 您已正确设置回调，并且您已 [测试您的CTV到移动应用程序的集成](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#test-partner-integration) 借助 AppsFlyer
2. 确保URL包含 是否必须配置 以及您想要的任何其他参数。
3. 向AppsFlyer发送用户IP地址和用户代理。这些 是CTV到移动应用程序视图归因所必需的。 它们可以以以下任一方式发送：
   1. 作为`af_ip`和`af_ua` 展示URL上的参数。
   2. 作为  和  请求头中的参数。

</Accordion>

<div id="test-partner-integration" />

<Accordion title="技术合作伙伴对接：">

CTV到移动应用的浏览型归因

1. 使用以下测试应用程序： com.appsflyer.android.deviceid and id1192323960
2. 联系 AppsFlyer 合作伙伴解决方案团队以获取测试 URL。为此，请登录到您的 [合作伙伴仪表板](https://hq1.appsflyer.com/auth/login)，然后从顶部菜单中点击 **帮助** > **联系我们的团队**。
   * 示例URL `https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false`
3. 确认您的合作伙伴 ID 在 `pid` 参数中是正确的。 是正确的。
4. 输入您的 IP 地址作为 `af_ip` 参数。
5. 输入您的用户代理作为 `af_ua` 参数。
6. 在桌面浏览器中输入 URL。
7. 在您的移动设备上，前往应用商店，下载、安装并启动该应用。
8. 新的安装应在 AppsFlyer 中显示，您应收到相应的回调。如果您没有看到安装或未收到回调，请联系合作伙伴解决方案团队。

</Accordion>

<div id="parameters" />

<Accordion title="参数说明">

以下参数用于 为广告客户提供归因数据和测量。

| 参数 | 是否必须配置 | 说明 |
| --- | --- | --- |
| 模板ID | ✓ | 的 ID OneLink 模版 模板包含基本的预测设置，用于 广告客户应用程序，并且是创建的基础 其他链接。 |
| pid | ✓ | 由 AppsFlyer 分配给投放广告的媒体来源（广告网络）的合作伙伴标识符。 |
| af\_xplatform | ✓ | <ul><li>由广告客户设置以指示链接是否支持跨平台归因。</li><li>值：true/false</li></ul> |
| af\_xplatform\_vt\_lookback | - | 可配置的窗口 表示在印象后可以归因于印象的应用安装的小时数。 可用的参数值为：1小时 - 72小时（小时）。默认为24小时。 |
| af\_ip | ✓ | <ul><li>显示广告的CTV设备的IP地址。</li><li>如果URL中未发送IP地址，必须在请求的头部中发送，以便AppsFlyer能够执行CTV到移动应用的归因。</li></ul> |
| af\_ua | ✓ | <ul><li>显示广告的CTV设备的用户代理。</li><li>如果URL中未发送用户代理，必须在请求的头部中发送，以便AppsFlyer能够执行CTV到移动应用的归因。</li></ul> |
| af\_source\_platform | - | <ul><li>一组值，用于表示发生印象的操作系统。</li><li>可能出现的值为：<ul><li>安卓</li><li>iOS</li><li>tizen</li><li>webos</li><li>smartcast</li><li>Roku</li><li>windowsphone</li><li>vidaa</li><li>PlayStation</li><li>smartcast</li><li>网站*</li></ul></li></ul> |
| af\_source\_device\_category | - | <ul><li>一组值，用于表示发生印象的设备类型。<ul><li>电视</li><li>mobile\_phone（手机）</li><li>desktop（PC端）</li><li>平板</li><li>set\_top\_box（机顶盒）</li><li>games\_console（游戏主机）</li><li>unknown\_device\_category</li><li>media\_player（媒体播放器）</li></ul></li></ul> |

可以添加到URL的其他参数可以在 下文的 归因链接的结构和参数

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="特点与局限性">

| 特点 | 说明 |
| --- | --- |
| 归因窗口 | 在1-72小时之间，具体取决于回溯窗口参数`af_xplatform_vt_lookback`。 |
| 再营销 | <ul><li>再归因：支持跨平台到移动端，不支持到其它平台。</li><li>再互动：不支持</li></ul> |
| 归因方法 | 使用概率模型完成浏览型归因 IP address（IP地址） |
| 基于住宅的归因 | 支持。意味着同一 家庭中的多个安装可以归因于同一CTV广告印象。 |
| 技术合作伙伴对接： | 不适用于已被标记的广告网络 因高移动应用到移动应用欺诈率 或与不同的标记媒体来源有关联。 |

</Accordion>

<div data-zendesk-anchors="ctvtomobile-app-attribution-for-ad-networks=ctv%E5%88%B0%E7%A7%BB%E5%8A%A8%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%BD%92%E5%9B%A0%E7%94%A8%E4%BA%8E%E5%B9%BF%E5%91%8A%E7%BD%91%E7%BB%9C h_01HE2X91GTDTPKKFBRRYYFMHDW=ctv%E5%88%B0%E7%A7%BB%E5%8A%A8%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%BD%92%E5%9B%A0%E7%94%A8%E4%BA%8E%E5%B9%BF%E5%91%8A%E7%BD%91%E7%BB%9C h_01K4806R6RER2837V0M0W9BX04=%E6%B3%A8%E6%84%8F h_01HE2X91GT6406JZNK2RCQKPVM=setup h_01HE2X91GT1B9SG9J4C3SNAPWD=test-partner-integration h_01HE2X91GTA96HJJNG3HRV18DF=parameters h_01HE2X91GVK9P44J1MA0M44KE1=traits-and-limitations" />
