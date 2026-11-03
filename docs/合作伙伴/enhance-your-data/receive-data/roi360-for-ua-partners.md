---
title: UA渠道的ROI360使用说明
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2023-08-12T17:09:08Z'
  edited_at: '2026-10-14T10:10:31Z'
  id: 17735150011921
  locale: zh-cn
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/zh-cn/articles/17735150011921
---
> **概要：** AppsFlyer可通过报告和回传向UA渠道提供完整精确的广告、应用内购买和自动续费数据。渠道可以将这些信息入库，将其用于UA投放的优化。

## 简介

  完成这一流程后，

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="哪些类型的收入会上报给渠道？">

应用侧会产生以下两类收入：

* **广告收入：广告变现收入：在相关应用内展示广告（包括横幅、插屏等样式）时就会产生广告收入。不管广告主使用何种投放计费方式，我们都可以计算这部分收入。**

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="AppsFlyer如何向UA渠道提供收入信息？">

AppsFlyer会通过以下方式向渠道提供应用内广告、应用内购买和订阅的收入数据：

* 每天更新一次，呈现前一天的数据。您可以通过Data Locker获取该报告。
* **广告收入回传**，广告收入回传：客户端设备上每展示一次广告，AppsFlyer就会向相关渠道发送回传，其中包含该广告收入事件的详细信息。
* 商店收入回传：每产生一次购买或订阅事件，AppsFlyer就会向相关渠道发送回传，其中包含该收入事件的详细信息。

</Accordion>

## 渠道的ROI360设置说明

渠道如需接收UA Signals报告以及广告收入和商店收入回传，请参照本节说明完成相关配置。

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="ROI360 UA Signals报告的订阅方式">

渠道如需开通该报告在Data Locker中的拉取权限，请按以下方式操作：

* 相关渠道需要在Data Locker中完成以下操作：
  1. 在渠道账户中<Anchor target="_blank" href="/partners/zh/docs/data-locker-for-partners#set-up-data-locker">设置Data Locker</Anchor>，包括绑定云存储工具并设定报告的格式和内容。
  2. <Anchor target="_blank" href="/partners/zh/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">启用ROI360 UA Signals报告</Anchor>。
* 广告主需要<Anchor target="_blank" href="/marketers/zh/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">为渠道开放该报告的权限</Anchor>。

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="从AppsFlyer接收ROI360回传的方式">

如需接收AppsFlyer的回传，渠道必须先与AppsFlyer渠道对接团队沟通，他们会在AppsFlyer平台中配置ROI应用内收入回传值。

如需联系AppsFlyer的渠道支持团队，请在您的面板中打开**帮助**菜单，然后选择**联系我们的团队**。

alt

</Accordion>

## UA平台的ROI UA Signals报告

该报告功能可每天向UA渠道的S3存储桶发送完整且准确的收入记录（CSV/parquet格式），每条记录代表设备层级的汇总广告收入事件。

与广告收入回传不同，UA Signal报告不提供实时数据，但可确保数据的准确性和完整性。这是因为广告展示的收入金额可能会随时间变化，尤其是通过常规CPM竞价而非实时竞价（RTB）产生的展示级别广告收入。

<div id="what-are-the-report-data-sources" />

<Accordion title="报告数据的来源">

报告数据的来源取决于广告主的对接类型，一般分为以下三种：

1. <Anchor target="_blank" href="/marketers/zh/docs/integrate-the-roi360-ad-revenue-sdk-api">AdRevenue SDK connector</Anchor>对接：广告主可以将渠道上传的展示级别收入数据共享到客户端设备，然后再以近乎实时的方式上报给AppsFlyer。
2. 基于S2S API的设备级别对接：广告主可以在AppsFlyer面板的对接渠道部分配置渠道证书，允许ROI360广告收入功能代其收集设备级别的广告收入数据。
3. 同时结合上述两种方式（即兼顾数据时效性和准确性的F2A）。**请注意：** 请注意：广告主是否能向AppsFlyer传输数据取决于广告主侧的授权状态及其ROI360高阶套餐的订阅情况。

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="该报告如何处理数据？">

AppsFlyer的ROI360广告收入报告功能会完成下列数据处理工作：

1. 数据规范化
2. 将收入归因到带来激活的渠道，并进行数据扩充
3. 生成广告收入事件
4. 将事件汇总到设备级别

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="报告数据的发送方式">

AppsFlyer会将设备级别的数据写入Data Locker的报告中，每天写入一次。

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="报告数据的时效性">

数据会在每天<Anchor target="_blank" href="/marketers/zh/docs/about-data-freshness-and-timezone-support#daily-processing">UTC时间21</Anchor>:00写入Data Locker存储桶的h=23文件夹中。

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="报告中的数据字段">

| **字段** | **说明** |
| --- | --- |
| 版本 | 以秒为单位的Unix时间戳，举例来说， 1661315124 |
| app\_id | AppsFlyer后台显示的App ID |
| install\_time | 如果用户使用iOS 14+设备或拒绝授权，或者如果启用了高级隐私保护（Advanced Privacy），激活时间取整到最近的小时数。 |
| campaign、campaign\_id、adset\_name、adset\_id、ad\_name、ad\_name、ad\_id、site\_id | 仅当新增激活归因到数据接收渠道时才会填充这些参数值。 |
| idfa、idfv、advertising\_id | • 若存在多个广告收入变现事件，则同一个设备ID（如IDFA、IDFV或advertiser\_id）会在报告中分多行多次出现。• 如果用户使用iOS 14+设备并拒绝在ATT弹窗中授权，或广告主启用了高级隐私保护（Advanced Privacy），报告中不会显示这些字段。 |
| platform | 设备系统：iOS、Android或Windows Mobile |
| country | [ISO 3166（alpha-2）](https://www.iso.org/iso-3166-country-codes.html)中的国家代码，如US、CNUS、CN。 |
| original\_url | • 如果用户使用iOS 14+设备并拒绝在ATT弹窗中授权，或广告主启用了高级隐私保护（Advanced Privacy），报告中不会显示这些字段。• 仅当新增激活归因到数据接收渠道时才会填充这些字段。 |
| mediation\_network | 将在2023年Q3上线：与展示相关联的聚合平台 |
| ad\_unit | 将在2023年Q3上线：与展示相关联的变现广告单元ad\_unit |
| placement | 将在2023年Q3上线：与展示相关联的变现广告位 |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="报告范例下载">

[您可以点击下载报告范例](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

## 应用内广告收入（IAA）回传

IAA回传是AppsFlyer用来向渠道发送收入信息的一种数据传输方式。IAA回传能够以近乎实时的方式与渠道共享IAA收入数据，而广告收入UA Signal报告的数据共享时间为第X+1天（即事件发生次日），因此在时效性方面，IAA回传要优于广告收入UA Signal报告。

但在准确性方面，实时数据略差于X+1天的数据，具体如下：

* 与UA Signal报告的X+1天数据相比，IAA实时回传数据的准确性平均会低±5%。
* 与UA Signal报告的X+1天数据相比，IAA实时回传数据的完整性平均会低±7%。

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="IAA回传数据的来源">

广告主能够通过这个connector上报展示事件，并在其中加入特定的参数，如ILRD（展示级别的收入数据）、货币单位、聚合平台和变现来源等。

广告主的客户端设备是否能向AppsFlyer传输数据取决于广告主侧的授权状态及其ROI360高阶套餐的订阅情况。

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="IAA回传数据的处理方式">

AppsFlyer的ROI360功能会对我们接收到的每条展示级别数据进行以下处理：

1. 数据标准化。
2. 将收入归因到带来激活的渠道，并进行数据扩充。
3. 生成**af\_ad\_revenue**事件。

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="回传数据的发送方式">

相关事件会作为一个附加的参数，通过渠道和AppsFlyer之间的现有回传配置发送到渠道。

</Accordion>

## 应用内购买（IAP）回传

ROI360的应用内事件回传会对每个交易进行验证、去重，然后再减去商店抽成和销售税，提供多层次的上报精度。

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="IAP回传数据的来源">

IAP回传的数据来源如下：

1. 由ROI360 Purchase SDK connector读取到的交易级别数据，每当用户设备上发生应用内购买或自动续费事件即会生成数据。
2. 所有传入AppsFlyer的**App Store和Google Play（RTDN）服务器通知**都会按照我们的购买和订阅收入逻辑进行处理：

   * 对于之前已经由SDK connector上报的交易，我们会对与其相关的通知进行验证和处理。
   * 与未知交易相关的通知不会上报到AppsFlyer系统。

   **请注意：** 请注意：广告主是否能向AppsFlyer传输数据取决于广告主侧的授权状态及其ROI360高阶套餐的订阅情况。

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="IAP回传数据的处理方式">

AppsFlyer的ROI360功能会对我们接收到的每条交易级别数据进行以下处理：

1. AppsFlyer会**与相关的商店验证购买或订阅**，以确保交易信息的真实性。
   * 验证成功后，AppsFlyer会记录该次购买或订阅。
   * 如果收据验证失败，则该事件会显示在被拦截的应用内事件原始数据报告中（需购买Protect360）。
2. AppsFlyer会对交易进行去重，包括iOS中的家人共享购买，以确保交易数据没有重复。
3. AppsFlyer会根据商店抽成和税费计算净收入数据（**真实收入**）。
4. AppsFlyer会针对已验证并处理的交易生成一个内部的购买或生命周期事件。

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="回传数据的发送方式">

IAP事件会通过渠道与AppsFlyer之间的现行回传对接发送到渠道。

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="IAP事件的界定">

购买了ROI360的客户可以共享下列含有收入信息的事件：

**事件名称**

| **事件名称** | **说明** |
| --- | --- |
| af\_purchase | 用户完成购买时记录该事件 |
| af\_purchase\_refund | 购买交易退款时记录该事件 |
| af\_ars\_trial\_converted | 用户在试用期后全价续订时记录该事件 |
| af\_ars\_subscription\_started | 折扣或全价的订阅周期开始时记录该事件 |
| af\_ars\_subscription\_resumed | 用户停止续订或退款后重新已全价订阅时记录该事件 |
| af\_ars\_subscription\_refunded | 向订阅用户退款发出时记录该事件 |
| af\_ars\_subscription\_renewed | 订阅自动续费时记录该事件 |
| af\_ars\_subscription\_xgraded | 用户订阅的产品发生升级、降级或变更时记录该事件 |

</Accordion>

<div data-zendesk-anchors="introduction=%E7%AE%80%E4%BB%8B 01H7T1DS6SNC7X8GX4DGXT4GC0=%E7%AE%80%E4%BB%8B 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=%E6%B8%A0%E9%81%93%E7%9A%84roi360%E8%AE%BE%E7%BD%AE%E8%AF%B4%E6%98%8E 01H7T1DS6TDA8CX1ZF3GGE4EHB=%E6%B8%A0%E9%81%93%E7%9A%84roi360%E8%AE%BE%E7%BD%AE%E8%AF%B4%E6%98%8E 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=ua%E5%B9%B3%E5%8F%B0%E7%9A%84roi-ua-signals%E6%8A%A5%E5%91%8A 01H7T1DS6T93844DMZY744ECQE=ua%E5%B9%B3%E5%8F%B0%E7%9A%84roi-ua-signals%E6%8A%A5%E5%91%8A 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=%E5%BA%94%E7%94%A8%E5%86%85%E5%B9%BF%E5%91%8A%E6%94%B6%E5%85%A5iaa%E5%9B%9E%E4%BC%A0 01H7T1DS6T0CN30EC97VARN80D=%E5%BA%94%E7%94%A8%E5%86%85%E5%B9%BF%E5%91%8A%E6%94%B6%E5%85%A5iaa%E5%9B%9E%E4%BC%A0 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=%E5%BA%94%E7%94%A8%E5%86%85%E8%B4%AD%E4%B9%B0iap%E5%9B%9E%E4%BC%A0 01H7T1DS6TH8AV2ZTY3M8ZXPYA=%E5%BA%94%E7%94%A8%E5%86%85%E8%B4%AD%E4%B9%B0iap%E5%9B%9E%E4%BC%A0 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
