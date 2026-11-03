---
title: UA平台的广告收入数据
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-michael-talapov
    - ROI360
    - Ad Networks
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2026-10-14T10:05:15Z'
  id: 4402898251409
  locale: zh-cn
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/zh-cn/articles/4402898251409
---
> **概要： UA平台可以获取广告收入数据，以此为基础优化广告主的UA投放。**

广告平台可以通过Data Locker获取包含用户广告收入信息的报告，这些用户来自各种渠道，可能是该平台本身，也可能是其他的媒体平台。

广告平台完成数据入库后，可将其用于定向投放和算法优化，同时全面了解通过UA广告产生的收入，以此为基础提升ROAS。

## 设置Data Locker中的广告收入报告

您必须先完成以下操作，才能在Data Locker中获取广告收入报告。

* 广告平台需要<Anchor target="_blank" href="/partners/zh/docs/data-locker-for-partners#set-up-data-locker">启用AppsFlyer的渠道Data Locker</Anchor>。
* 广告平台需要[配置报告内容](#configure-the-report-output-settings)并[启用广告收入报告](#enable-the-ad-revenue-report)。
* 广告主需要向广告平台开放报告访问权限。详见<Anchor target="_blank" href="/marketers/zh/docs/share-ad-revenue-data-with-partners#ua-signals-for-ad-networks">广告主说明文档</Anchor>

<div id="configure-the-report-output-settings" />

<Accordion title="报告输出配置">

配置报告输出的方式如下：

1. 从AppsFlyer后台进入**报告**->**Data Locker**。
2. 在**报告输出配置**部分打开**发送报告**开关。
3. 设置报告的输出文件属性。
   * 报告格式（Parqet/CSV）。
   * 报告的压缩方式（Snappy/GZIPO/Uncompressed）。
   * 报告中可包含的数据行数上线。
4. 查看报告的输出文件路径，该路径取决于您的数据连接设置。如需进一步了解数据连接的设置，请参见<Anchor target="_blank" href="/partners/zh/docs/data-locker-for-partners#set-up-data-locker">Data Locker设置说明</Anchor>。

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="启用广告收入报告">

1. 在**Data Locker内容**部分，选择报告类型**广告收入【每日】。**
2. 点击**保存链接**。
3. 请确保广告主已为广告平台开通报告查看权限。
4. 详细说明请见<Anchor target="_blank" href="/marketers/zh/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">向广告平台开放广告收入数据的方法</Anchor>。

</Accordion>

## 报告规格

<div id="report-considerations" />

<Accordion title="报告的结构和格式">

* 格式：Data Locker以CSV格式向UA平台的S3存储桶发送数据。
* 数据级别：报告中包含设备级别的维度和指标。
* 扩充数据：报告中包含来自聚合平台的广告收入数据，并添加适用于相关UA平台的归因数据（剔除与UA平台无关的所有维度）。
* 数据时效性：<Anchor target="_blank" href="/marketers/zh/docs/about-data-freshness-and-timezone-support#ad-revenue">每日，即第0天的数据在第1天显示</Anchor>。数据会在每天<Anchor target="_blank" href="/marketers/zh/docs/about-data-freshness-and-timezone-support#ad-revenue">UTC时间21</Anchor>:00写入Data Locker存储桶的h=23文件夹中。
* 覆盖的应用：单个报告可包含所有授权应用的数据。
* 报告包含所有转化类型的数据：激活、再归因和再互动的数量。
* 货币：美元。以美元（USD）为货币单位。事件收入在事件发生当天以USD计算。
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv">查看报告样例。</Anchor>

</Accordion>

<div id="report-structure" />

<Accordion title="报告字段">

| **字段** | **说明** |
| --- | --- |
| 版本 | 以秒为单位的Unix时间戳，示例：1661315124 |
| app\_id | AppsFlyer后台显示的App ID |
| install\_time | <ul><li>激活时间戳：YYYY-MM-DD HH:MM:SS<br />示例：2020-08-16 11:22:33</li><li>如果用户使用iOS 14+设备或拒绝授权，或者如果启用了高级隐私保护（Advanced Privacy），激活时间取整到最近的小时数。</li></ul> |
| campaign、campaign\_id、adset\_name、adset\_id、ad\_name、ad\_name、ad\_id、site\_id | 仅当新增激活归因到数据接收渠道时才会填充这些参数值。 |
| idfa、idfv、advertising\_id | <ul><li>若存在多个广告收入变现事件，则同一个设备ID（如IDFA、IDFV或advertiser\_id）会在报告中分多行多次出现。</li><li>如果用户使用iOS 14+设备或拒绝授权，或者如果广告主启用了高级隐私保护，则报告中不会显示这些字段。</li></ul> |
| 平台 | 设备系统：iOS、Android或Windows Mobile |
| 国家/地区 | <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166（alpha-2）</Anchor>中的国家代码，如：US、CN。 |
| original\_url | <ul><li>如果用户使用iOS 14+设备或拒绝授权，或者如果广告主启用了高级隐私保护，则报告中不会显示这些字段。</li><li>仅当新增激活归因到数据接收渠道时才会填充这些参数值。</li></ul> |
| ad\_unit |  |
| placement |  |
| mediation\_network |  |
| engagement\_type |  |

指标：

| **字段** | **说明** |
| --- | --- |
| impressions | 用户看到该条广告的次数 |
| revenue\_usd | 由该设备ID产生的每日收入（以USD为单位）。**请注意**：收入金额较小时以科学计数法表示，如：8.00E-05 |

</Accordion>

<div data-zendesk-anchors="set-the-ad-revenue-report-in-data-locker=%E8%AE%BE%E7%BD%AEdata-locker%E4%B8%AD%E7%9A%84%E5%B9%BF%E5%91%8A%E6%94%B6%E5%85%A5%E6%8A%A5%E5%91%8A h_01H8Y7ABGVR7BNHEYVFKPFM4JN=%E8%AE%BE%E7%BD%AEdata-locker%E4%B8%AD%E7%9A%84%E5%B9%BF%E5%91%8A%E6%94%B6%E5%85%A5%E6%8A%A5%E5%91%8A h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report report-specification=%E6%8A%A5%E5%91%8A%E8%A7%84%E6%A0%BC h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=%E6%8A%A5%E5%91%8A%E8%A7%84%E6%A0%BC h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
