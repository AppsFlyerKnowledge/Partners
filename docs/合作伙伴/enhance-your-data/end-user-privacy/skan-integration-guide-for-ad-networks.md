---
title: 广告平台的SKAN对接指南
metadata:
  keywords:
    - Ad Networks
    - Partners
    - SKAD
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2020-08-03T08:56:14Z'
  edited_at: '2026-10-14T10:10:29Z'
  id: 360011502657
  locale: zh-cn
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/zh-cn/articles/360011502657
---
> **概要**：概要：广告平台与AppsFlyer完成SKAdNetwork（SKAN）对接后，便可获得SKAN归因结果并进行相应的投放优化。

## AppsFlyer可为广告平台提供以下优势：

**如需了解AppsFlyer为广告主提供的SKAN解决方案，请参见以下文档**：

<Anchor target="_blank" href="/marketers/zh/docs/skadnetwork-skan-solution-guide">SKAN解决方案指南 |</Anchor> <Anchor target="_blank" href="/marketers/zh/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAN面板</Anchor>

* **广告转化归因：**
  * 广告平台与AppsFlyer对接后，可确保广告主在该平台上的投放所带来的所有应用激活、应用内事件以及收入都得到准确归因
  * 如果没有对接，则这些激活、应用内事件和收入都会被归为自然量，而不会归因到平台
* **投放优化：**
  * 回传中的转化值是编译后的值。
  * AppsFlyer支持广告平台对每条回传里的转化值进行解析，并根据解析后的值对相关应用的营销投放进行优化。
* **无需针对每个广告主分别完成对接——** SKAN回传只发送给广告平台，广告主侧如果想获取对应数据，可采用以下任一方式：
  * 分别与每个合作的广告平台进行对接。但不管是广告主还是广告平台，都无法使用这种方式实现大量级的对接。
  * 与AppsFlyer对接。只需一个对接就能全面铺开，对广告主和广告平台来说都是极为高效的对接方式。
* **让您的渠道在AppsFlyer平台中脱颖而出：**
  * AppsFlyer会对支持SKAN对接的广告平台进行认证并予以特别标识。
  * 便于使用SKAN的广告主准确定位到支持SKAN归因的广告平台。

## SKAN数据流

![5754_Postback_flow_for_SKAD__1_.png](https://files.readme.io/dff0fb00721802f59d199ae6a69f9ea7484bc0ef038c669904aa1a7c2b97dfc8-12574373654161.png)

完整的SKAN回传链路包含以下几个环节：

1. **iOS**设备先将SKAN回传发送到获得归因的广告平台。
2. **广告平台**可选择下列两种方式的的任意一种：
   * 补充数据维度并转发补充数据维度并转发：广告平台会在其中添加广告系列ID/来源标识符（Source Identifier）、广告系列名称、iOS设备所在IP地址等信息，以细化回传数据。
   * redirect
3. **AppsFlyer**会对回传进行验证和解析，然后将解析并扩充后的回传数据发回给广告平台（同时同步给广告主）。

## 主要对接流程

AppsFlyer与广告平台的SKAN对接主要分为以下几个步骤（下文会有详细说明）：

* 广告平台将SKAN数据发送给AppsFlyer
* AppsFlyer对SKAN数据进行解析和扩充，然后发回给广告平台

## 向AppsFlyer发送数据

广告平台接收到来自设备的SKAN回传后，会通过以下任一方式将其发送给AppsFlyer：

* 补充数据维度并转发（POST)
* 重定向（HTTP307重定向方式）

AppsFlyer接收到SKAN回传后会进行如下处理：

* 将解析后的回传发送到广告平台。
* 通过数据面板和报告将归因数据提供给广告主和广告平台。

<div id="enrich-and-forward" />

<Accordion title="补充数据维度并转发">

广告平台可使用此方法将其从设备侧接收到的各次回传分别转发到AppsFlyer。

**广告平台**

* 接收来自iOS设备的回传。
* 【必须完成】在回传数据中补充以下维度：  
  * 相关广告系列在广告平台中的ID和名称。
  * iOS设备发送回传的时间戳。
* 【可选】在回传数据中补充以下维度：
  * 从设备收到的IP地址，主要用于地理位置解析。
  * 广告组ID和名称
  * 广告ID和名称
  * Ad network name
  * Country code
  * Source app ID
  * Creative
  * 流量入口（Channel）
* 完成上述数据扩充后，再将回传发送到AppsFlyer
* **请注意：注意：向AppsFlyer转发回传之前，广告平台必须先通过回传内容验证Apple的**归因签名/strong>（Attribution Signature），避免对数据造成意外损坏。

#### 扩充后的SKAN数据回传规范

| 端点 | `https://skadpostbacks.appsflyer.com/api/postbacks` |
| --- | --- |
| HTTP方法 | POST |
| 可用格式 | `application/json` |
| 响应码 | 200 OK200 OK：接收到的回传格式正确。<br /><br />21Bad request（请求无效）400：请求无效——JSON文件格式错误、文件为空、缺失必要字段。 |

#### 扩充后的JSON格式SKAN回传参数

| 参数 | 格式 | 说明 | 流量来源 |
| --- | --- | --- | --- |
| version | 字符串 | SKAdNetwork版本<br /><br />示例：`"version":"2.0"` | SKAN回传 |
| ad-network-id | 字符串 | Ad network ID<br /><br />示例：`"ad-network-id":" abc123defg.SKAdnetwork"` | SKAN回传 |
| ad-network-name | 字符串 | <ul><li>广告平台名称</li><li>示例：`ad_network_name=your_network`</li></ul> | 广告平台 |
| ad-network-country-code | 字符串 | <ul><li>广告平台得出的用户位置信息（国家/地区）</li><li>使用<Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO</Anchor> 3166（alpha-2）代码填充该字段</li><li>比如</li><li>广告平台一般会通过广告系列的投放地区得出国家/地区信息</li><li>AppsFlyer会使用国家/地区代码来填充报告和面板中与地理位置有关的字段</li></ul> | 广告平台 |
| campaign-id | 整数 | <ul><li>仅限SKAN 3及以下版本</li><li>SKAdNetwork 广告系列 ID</li><li>示例：`"campaign-id":23`</li></ul> | SKAN回传 |
| transaction-id | 字符串 | SKAdNetwork回传交易ID（transaction ID） | SKAN回传 |
| app-id | 整数 | <ul><li>AppsFlyer中目标应用的App ID，总是以“id”开头。</li><li>示例：`app_id=id123456789`</li></ul> | SKAN回传 |
| Attribution signature | 字符串 | Attribution signature | SKAN回传 |
| redownload | 布尔 | redownload = true时，表示该用户再次从App Store下载相关应用 | SKAN回传 |
| source-app-id | 整数 | <ul><li>流量侧应用的App ID（发布广告的应用）</li><li>详见[Apple相关文档](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)。</li></ul> | SKAN回传 |
| conversion-value | 整数 | AppsFlyer SDK 根据广告主的配置设置的转化值<br /><br />**注意**：<ul><li>受iOS隐私保护阈值限制而无法在回传中填充该字段时，对应的值会显示为null。</li><li>null值和0值的意义不同：<ul><li>null值表示iOS拒绝披露相关的转化值。</li><li>210值表示该用户激活了应用，但未记录到其完成任何转化操作。</li></ul></li></ul> | SKAN回传 |
| ad-network-campaign-id | 字符串 | 为了确保广告主、广告平台和AppsFlyer之间的数据解读方式一致，请务必提供广告系列ID | 广告平台 |
| ad-network-campaign-name | 字符串 | 广告平台中的广告系列名称，与该广告平台为相应广告系列赋予的ID相关联。该名称会呈现在面板和报告中。 | 广告平台 |
| ad-network-adset-id | 字符串 | 广告组ID | 广告平台 |
| ad-network-adset-name | 字符串 | 广告组名称 | 广告平台 |
| ad-network-ad-name | 字符串 | 广告名称 | 广告平台 |
| ad-network-ad-id | 字符串 | 广告ID | 广告平台 |
| ip | 字符串 | <ul><li>回传发送设备的IP地址</li><li>支持 iPv4 及 IPv6 地址</li><li>示例：`"ip":"198.51.100.1"`</li></ul> | 广告平台 |
| timestamp | 字符串 | <ul><li>广告平台接收到SKAN回传的时间，</li><li>举例来说， UTC时间2020年8月4日07:25的时间戳为：</li></ul> | 广告平台 |
| fidelity-type | 整数 | <ul><li>用于区分广告呈现方式，这会影响到归因结果。通过0和1来表达，具体如下：<ul><li>浏览型广告（View-though Ads）：0</li><li>渲染型广告（StoreKit-rendered Ads）：1</li></ul></li><li>从SKAN V2.2开始，该字段为必要字段</li></ul> | SKAN postback (V2.2+) |
| did-win | 布尔 | <ul><li>用于区分[激活助攻和获得激活归因](https://developer.apple.com/documentation/storekit/SKAdnetwork/SKAdnetwork_release_notes/SKAdnetwork_version_3_0_release_notes)的广告系列</li><li>如果该字段值为true，则表示该广告系列获得了此次激活的归因</li><li>如果该字段值为false，则表示该广告系列在此次激活中形成助攻</li></ul> | SKAN postback (V3.0+) |
| ad-network-source-app-id | 字符串 | 该字段以*publisher ID*填充，即发布相关广告的应用所关联的ID。一般指您为该流量侧应用指定的ID，而非Apple生成的ID。 | 广告平台 |
| postback-sequence-index | 整数 | <ul><li>仅限SKAN 4+</li><li>该参数的值代表SKAN窗口序号，可能出现的值为0、`0`10或`1`21。</li></ul> | SKAN 4.0回传（iOS 16.2） |
| coarse-conversion-value | 字符串 | <ul><li>仅限SKAN 4+</li><li>在第1梯队的首次回传以及第1-3梯队的第二和第三次回传中可用。详见[Apple相关文档](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)。</li></ul> | SKAN 4.0回传（iOS 16.2） |
| source-identifier | 字符串 | <ul><li>仅限SKAN 4+</li><li>该字段的值最多可有四位数</li><li>在首次回传中，第2-3梯队最多可获得4位数字，第0-1梯队最多可获得2位数字。在第二和第三次回传中，第1-3梯队可获得2位数字。而第0梯队没有第二和第三次回传。详见[Apple相关文档](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)。</li></ul> | SKAN 4.0回传（iOS 16.2） |
| source-domain | 字符串 | <ul><li>仅限SKAN 4+</li><li>该字段的值代表可归因的网页广告来源比如</li><li>详见[Apple相关文档](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)。</li></ul> | SKAN 4.0回传（iOS 16.2） |
| creative | 字符串 | <ul><li>仅适用于SKAN 4+</li><li>在source\_identifier中使用额外数位以细化广告系列颗粒度时可用</li></ul> | 广告平台 |
| channel | 字符串 | <ul><li>仅适用于SKAN 4+</li><li>在source\_identifier中使用额外数位以细化广告系列颗粒度时可用</li></ul> | 广告平台 |

#### **Curl示例—扩充后的SKAN 3回传数据**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version":"3.0",
      "app-id": 888707086,
      "ip": "192.0.2.0",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "source-app-id": 888707074,
      "ad-network-id": "abcabcabc.skadnetwork",
      "transaction-id": "68eb3d91-15f5-44ee-9267-25c7655c20b6",
      "redownload": false,
      "attribution-signature": "MDYCGQCsQ4y8d4BlYU9b8Qb9BPWPi+ixk/OiRysCGQDZZ8fpJnuqs9my8iSQVbJO/oU1AXUROYU=",
      "timestamp": "1596525944",
      "ad-network-campaign-id": "222222",
      "conversion-value": 63,
      "campaign-id": 99
  }'
```

#### **Curl示例—扩充后带精细转化值的SKAN 4回传数据**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "5239",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e30",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "conversion-value": 63
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIGRmSMrqedNu6uaHyhVcifs118R5z/AB6cvRaKrRRHWRAiEAv96ne3dKQ5kJpbsfk4eYiePmrZUU6sQmo+7zfP/1Bxo="
  }'
```

#### **Curl示例—扩充后带粗略转化值的SKAN 4回传数据**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "39",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e31",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "coarse-conversion-value": "high"
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIQD4rX6eh38qEhuUKHdap345UbmlzA7KEZ1bhWZuYM8MJwIgMnyiiZe6heabDkGwOaKBYrUXQhKtF3P/ERHqkR/XpuA="
  }'
```

</Accordion>

<div id="redirect" />

<Accordion title="重定向">

Redirect\_us-en\_\_2\_.png

在此方法中，广告平台使用HTTP重定向指令（307）来响应iOS设备发出的SKAN信息，请求设备将SKAN回传直接发送到AppsFlyer。

重定向方法具有以下优势：

#### **启用方式**

1. 配置您的服务器以使用HTTP 307对SKAdNetwork回调进行响应，将回调信息重定向到 *[https://skadredirect.appsflyer.com/api/redirects](https://skadredirect.appsflyer.com/api/redirects)*
2. 您可以在SKAN回传中添加下表所列的广告系列信息查询参数。请务必在回传中发送广告系列信息，因为我们需要通过这些信息补充SKAN回传中的成本等投放数据，这样广告主才能有效地优化其投放。

**重定向的SKAdNetwork请求示例**

```http
https://skadredirect.appsflyer.com/api/redirects?
  &ad-network-campaign-id=243232&ad-network-campaign-name=yarg_campaign_name
  &ad-network-adset-name=dsdsa&creative=examplecreative&channel=channelexample
```

#### 建议添加的广告系列相关参数（非必须）

| 查询参数 | 说明 |
| --- | --- |
| ad-network-name | <ul><li>广告平台名称</li><li>比如</li></ul> |
| ad-network-campaign-id | 即广告系列的ID |
| ad-network-campaign-name | 即广告系列的名称 |
| ad-network-adset-id | Ad set ID（广告组ID） |
| ad-network-adset-name | Ad set name（广告组名称） |
| ad-network-ad-id | 即相关广告的ID |
| ad-network-ad-name | 即相关广告的名称 |
| ad-network-country-code | <ul><li>广告平台得出的用户位置信息（国家/地区）</li><li>使用<Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO</Anchor> 3166（alpha-2）代码填充该字段</li><li>比如</li><li>广告平台一般会通过广告系列的投放地区得出国家/地区信息</li><li>AppsFlyer会使用国家/地区代码来填充报告和面板中与地理位置有关的字段</li></ul> |
| ad-network-source-app-id | 该字段以publisher ID填充，即发布相关广告的应用所关联的ID。一般指您为该流量侧应用指定的ID，而非Apple生成的ID。 |
| ip | <ul><li>回传发送设备的IP地址</li><li>支持 iPv4 及 IPv6 地址</li><li>比如</li></ul> |
| timestamp | <ul><li>广告平台接收到SKAN回传的时间，</li><li>举例来说， UTC时间2020年8月4日07:25的时间戳为：</li></ul> |
| creative | <ul><li>仅适用于SKAN 4+</li><li>在source\_identifier中使用额外数位以细化广告系列颗粒度时可用</li></ul> |
| channel | <ul><li>仅适用于SKAN 4+</li><li>在source\_identifier中使用额外数位以细化广告系列颗粒度时可用</li></ul> |

</Accordion>

## 接收AppsFlyer发送的数据

开始接收回传之前，需先考虑以下事项：

* 广告平台必须设定回传端点和模板（请通过<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系您的PDM，以确保该设置妥善完成）。
* AppsFlyer发送SKAN回传时使用的机制与iOS向广告平台发送SKAN回传的机制相同。

<div id="principles" />

<Accordion title="原理">

* 对于广告平台侧发送到AppsFlyer的每条回传，AppsFlyer都会发送：
  * 一条激活回传。AF会使用“redownload”参数来标识重新下载行为。
  * 零次到数次的应用内事件回传。具体次数取决于转化值的解析结果，详见模拟回传。

</Accordion>

<div id="postback-macros-available-to-ad-network-partners" />

<Accordion title="广告平台可用的回传宏">

<table><thead><tr><th><p>回传宏（名称）</p></th><th><p>说明</p></th><th>格式和示例</th><th>仅适用于应用内事件</th></tr></thead><tbody><tr><td><p>site_id</p></td><td><p>发布广告的应用（即Source App ID，流量侧应用ID）</p></td><td><p>字符串：876534</p></td><td></td></tr><tr><td><p>install_time</p></td><td><p>由AppsFlyer根据<em>updateConversion</em>窗口估算。以10位UNIX时间戳或人类可读的时间戳表达。</p></td><td><ul><li>字符串：1596119460 </li><li>转换为UTC时间2020年7月30日14:31。</li></ul></td><td> </td></tr><tr><td><p>skadnetwork_ad_network_time</p></td><td><p>广告平台从iOS设备接收到回传的时间。由广告平台上报。以10位UNIX时间戳或人类可读的时间戳表达。</p></td><td><ul><li>字符串：1596119460 </li><li>转换为UTC时间2020年7月30日14:31。</li></ul></td><td> </td></tr><tr><td><p><br/>skadnetwork_received_time</p></td><td><p>AppsFlyer从广告平台接收到回传的时间。以10位UNIX时间戳或人类可读的时间戳表达。</p></td><td><ul><li>字符串：1596119460 </li><li>转换为UTC时间2020年7月30日14:31。</li></ul></td><td></td></tr><tr><td><p>event_name</p></td><td><p>事件名称 </p><ul><li>af_skadnetwork_revenue</li><li>af_login</li><li>af_skadnetwork_revenue</li><li>或由广告主设置 </li></ul></td><td><p>字符串：af_skadnetwork_revenue, abc123</p></td><td><p>是</p></td></tr><tr><td><p>revenue</p></td><td><p>以指定货币代码为单位的收入金额</p></td><td><p>数字21</p></td><td><p>是</p></td></tr><tr><td><p>currency</p></td><td><p>货币代码为广告主在AF后台针对相关应用设置的指定货币。</p></td><td><p>字符串：</p></td><td><p>是</p></td></tr><tr><td><p>attribution_source</p></td><td><p>归因数据的来源：</p><p>SKAdNetworkSKAdNetwork</p></td><td><p>字符串：SKAdNetwork</p></td><td></td></tr><tr><td><p>app_id</p></td><td><p>App ID（广告主应用）</p></td><td><p>字符串：ID123456790</p></td><td></td></tr><tr><td><p>country</p></td><td><p>由广告平台判定的激活所在国家</p></td><td><p>字符串： </p></td><td></td></tr><tr><td><p>campaign</p></td><td><p>广告系列名称使用从广告平台回传的<em>d-network-campaign-</em> name 填充</p></td><td><p>字符串：UA_US_23+</p></td><td></td></tr><tr><td><p>campaign_id</p></td><td><p>使用<em>广告平台</em>回传中发送的广告系列 ID 填充广告系列 ID。<strong>请注意</strong>：请注意：在SKAN 4中，该值总是为null。</p></td><td><p>字符串：3456745</p></td><td></td></tr><tr><td><p>redownload</p></td><td><p>可能出现的值为：true、false</p><p>redownload = true时，代表该用户再次从App Store下载相关应用</p></td><td><p>布尔值：true / false</p></td><td></td></tr><tr><td><p>skadnetwork_ambiguous_event</p></td><td><p>广告主在面板中更改SKAN设置后的最初72小时内接收到的事件。由于SKAN使用的计时器过多，因此AppsFlyer无法准确地映射该事件。</p><ul><li> </li></ul></td><td><p>布尔值：true / false</p></td><td></td></tr><tr><td><p>skadnetwork_campaign_id</p></td><td>原始SKAN回传中提供的SKAN广告系列ID</td><td><p>56, 23</p></td><td></td></tr><tr><td><p>af_skadnetwork_nonce</p></td><td>具有唯一性的随机标识符，便于渠道识别重复的回传</td><td></td><td></td></tr><tr><td><p>event_id</p></td><td>广告平台为对应<span></span><span>事件</span><span></span>赋予的名称/ID。</td><td></td><td><p>是</p></td></tr><tr><td><p>transaction_id</p></td><td><p><span>SKAN回传交易ID</span></p><p><span><strong>请注意</strong>：注意: 广告主必须手动开通AppsFlyer与广告平台之间的transaction_id共享。您可以让广告主在AppsFlyer后台的对接板块中完成相关操作。</span></p></td><td></td><td></td></tr><tr><td>ad_network_adset_id</td><td>由广告平台添加到iOS回传中</td><td>字符串</td><td> </td></tr><tr><td>ad_network_adset_name</td><td>由广告平台添加到iOS回传中</td><td>字符串</td><td> </td></tr><tr><td>ad_network_ad_name</td><td>由广告平台添加到iOS回传中</td><td>字符串</td><td> </td></tr><tr><td>ad_network_ad_id</td><td>由广告平台添加到iOS回传中</td><td>字符串</td><td> </td></tr><tr><td>SKAN_min_event_counter</td><td>参见脚注（1）</td><td><p>整数</p></td><td>是</td></tr><tr><td>SKAN_max_event_counter</td><td>参见脚注（1）</td><td><p>整数</p></td><td>是</td></tr><tr><td>SKAN_min_time_post-install</td><td>参见脚注（2）</td><td><p>整数</p></td><td>是</td></tr><tr><td>SKAN_max_time_post-install</td><td>参见脚注（2）</td><td><p>整数</p></td><td>是</td></tr><tr><td>SKAN_min_event_revenue</td><td>参见脚注（3）</td><td>实数</td><td>是</td></tr><tr><td>SKAN_max_event_revenue</td><td>参见脚注（3）</td><td><p>实数 </p></td><td>是</td></tr><tr><td>fidelity-type</td><td><p>用于区分<span>广告呈现</span>方式，这会影响到归因结果。通过0和1来表达，具体如下：</p><ul><li><span>浏览型广告（View-though Ads）：0</span></li><li>渲染型广告（StoreKit-rendered Ads）：1</li></ul></td><td>整数</td><td> </td></tr><tr><td>skad_af_attribution_flag</td><td><p>用于标识该用户是否由AppsFlyer通过<span>单一可信数据源机制</span>归因。</p></td><td>布尔</td><td> </td></tr><tr><td><span>skad_postback_sequence_index</span></td><td><ul><li>该字段代表SKAN窗口，可能出现的值为0、1或2。</li><li>在SKAN 3中，该字段的值为0。</li></ul></td><td><span>整数</span></td><td> </td></tr><tr><td><span>skad_coarse_conversion_value</span></td><td><ul><li> </li><li>在SKAN 3中，该字段的值为0。</li></ul></td><td><span>字符串</span></td><td> </td></tr><tr><td><span>skad_source_identifier</span></td><td><ul><li>该字段的值最多可有四位数</li><li>在SKAN 3中，该字段的值为0。</li></ul></td><td><span>字符串</span></td><td> </td></tr><tr><td><span>skad_source_domain</span></td><td><ul><li>该字段的值代表可归因的网页广告来源</li><li>在SKAN 3中，该字段的值为0。</li></ul></td><td><span>字符串</span></td><td> </td></tr><tr><td><span>ad_network_creative</span></td><td><ul><li>该字段的值基于广告平台提供的扩充数据得出</li><li>在SKAN 3中，该字段的值为0。</li></ul></td><td><span>字符串</span></td><td> </td></tr><tr><td><span>ad_network_channel</span></td><td><ul><li><span>仅适用于SKAN 4+</span></li><li>在<span>source_identifier</span>中使用额外数位以细化广告系列颗粒度时可用</li></ul></td><td><span>字符串</span></td><td> </td></tr><tr><td colspan="4"><p>请注意：</p><ol><li> 事件次数<br/><code>[round up (SKAN_min_event_counter+SKAN_max_event_counter) / 2]</code><br/>请注意：必须四舍五入取整。</li></ol><ul><li>举例来说， <ul><li>A. A. 如果min=0且max=1，则事件数量为1。</li><li>B. A. 如果min=0且max=1，则事件数量为1。</li></ul></li><li> 判断激活时间：对于使用自定义衡量模式（Custom）的广告主，AppsFlyer的激活时间计算方式为：回传接收时间 - 48h - (min_time_post_install + max_time_post_install)的平均值。广告平台不需要使用这些宏。  </li><li> 判断收入：AppsFlyer使用这些值来判断某个事件的收入，计算方式为(min + max)/2。广告平台不需要使用这些宏。 </li></ul></td></tr></tbody></table>

</Accordion>

<div id="skan-postback-examples" />

<Accordion title="SKAN回传示例">

**AppsFlyer发送的SKAN激活回传示例**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)
  &attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

**AppsFlyer发送的SKAN应用内事件回传示例**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)&revenue=(value)
  &currency=(code)&event_name=(event-name)&attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

</Accordion>

## 对接测试

您可以使用以下任一方式测试您的平台与AppsFlyer的SKAN对接：

* 真实的SKAN回传：基于广告平台收到的实际SKAN流量进行测试
* 模拟回传：基于AppsFlyer的测试应用

**如需从iOS设备侧接收到真实的SKAN回传，广告平台必须完成以下工作：**

* 在Apple的开发者网站中注册为广告平台
* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/generating_the_signature_to_validate_storekit-rendered_ads">使用SKAN签名对广告进行标记</Anchor>。
* 流量侧应用（Publisher App）流量侧应用（Publisher App）：将广告平台ID添加到info.plist文件中，并/a>在广告展示时<Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/generating_the_signature_to_validate_an_installation">调用loadProduct</Anchor>。
* V6.0.3之前的版本不支持SKAdNetwork归因。

**接收模拟回传：**

* 请使用<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系我们并申请模拟应用对接。
* 请明确告知您在测试中要使用的App ID（从[下一小节](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks)的列表中选择）。

<div id="real-environment" />

<Accordion title="真实环境测试">

在该方法中，广告平台需针对实际使用中的应用向AppsFlyer发送其真实的SKAN回传。

#### 测试对接

| 负责人员 | 操作 |
| --- | --- |
| 广告平台 | 与您的AppsFlyer PDM联系（或使用渠道支持微件），告知您的SKAN平台ID（由Apple提供）。 |
| 广告平台和AppsFlyer | 确认要参与回传对接测试的客户（需接入最新的AppsFlyer SDK）。 |
| 广告平台 | 使用本文所述的任一方法将相关应用的SKAN回传发送给AppsFlyer。 |
| AppsFlyer | 根据广告客户设置的转化价值映射关系，将解码后的应用内事件信息发送到广告平台。 |

#### 测试成功标准：

| 负责人员 | 操作 |
| --- | --- |
| 广告平台 | 测试结束后，广告平台需向AppsFlyer提供以下信息：广告平台在指定时间段内为测试客户发送的SKAN回传数量。 |
| AppsFlyer | 对比收到的回传数量与广告平台发送的数量。 |
| AppsFlyer | 按以下分类将发送到相关广告平台的回传数量信息分享给该平台：<ul><li>激活/重新下载（redownload）</li><li>应用内事件</li></ul>请注意：注意：如果您用于接收SKAN回传的端点与概率模型归因回传的端点相同，请务必使用*attribution\_source=skadnetwork*/span>，筛选出SKAN回传。 |

</Accordion>

<div id="simulated-postbacks" />

<Accordion title="模拟回传">

* 广告平台可使用此方法将AppsFlyer预先备制的回传数据发送到AppsFlyer测试应用，具体说明请见下表。然后AppsFlyer会把解析完毕的转化信息再回传给广告平台。
* 各测试应用的转化值映射构架都有所不同，具体请见下表。

| App ID（应用ID） | SKAN衡量模式 | 操作说明 |
| --- | --- | --- |
| <span id="id888707085"></span>id888707085 | 收入模式，且转化值每增加1，代表收入增加$1<br /><br />预期结果： | <ol><li>在对接选项卡中，打开**应用内事件回传**开关。</li><li>在事件名称中选择af\_SKAN\_revenue，并将其关联到您对应的事件标识符。</li><li>保存配置。</li><li>回传中发送的转化值 = 7。</li><li>AppsFlyer解码后回传：<ul><li>1次激活</li><li>值为$7的af\_SKAN\_revenue</li></ul></li></ol> |
| <span id="id888707086"></span>id888707086 | 转化模式，且记录以下事件：<ul><li>af\_level\_complete</li><li>af\_login</li><li>af\_SKAN\_revenue</li><li>af\_register</li><li>af\_subscription</li><li>af\_custom\_event</li></ul> | <ol><li>在对接选项卡中，打开**应用内事件回传**开关。</li><li>选择列表中的各个应用内事件，并将其关联到您对应的事件标识符。</li><li>保存配置。</li><li>回传中发送的转化值 = 63。</li><li>AppsFlyer解码后回传：<ul><li>1次激活</li><li>af\_level\_complete</li><li>af\_login</li><li>af\_register</li><li>af\_subscription</li><li>af\_custom\_event</li></ul></li></ol> |
| <span id="id888707087"></span>id888707087 | 使用af\_SKAN\_revenue事件记录到的互动 | <ol><li>在对接选项卡中，打开**应用内事件回传**开关。</li><li>将名为af\_SKAN\_revenue的事件*关联到您对应的事件标识符*。</li><li>保存配置。</li><li>回传中发送的转化值 = 3。</li><li>AppsFlyer解码后回传：<ul><li>1次激活</li><li>af\_SKAN\_revenue事件的3次回传</li></ul></li></ol> |

#### 对接流程

| 负责人员 | 操作 |
| --- | --- |
| 广告平台 |  |
| 广告平台 | <ol><li><Anchor target="_blank" href="/partners/zh/docs/turn-on-test-app-integration-for-ad-networks">激活测试应用</Anchor>。</li><li>为各应用完成上表所列操作。</li><li>使用上表所列的测试应用发送模拟回传。发送模拟回传时请注意以下事项：<ul><li>请按照上表内容设置模拟回传中的app\_id和转化值。</li><li>由于广告平台无法生成Apple支持的签名，因此模拟回传中不必带有签名字段。AppsFlyer不会验证模拟回传中的签名。</li><li>AppsFlyer支持广告平台使用POST或REDIRECT方法发送回传。</li></ul></li></ol> |
| AppsFlyer | 对模拟回传中的转化值进行解析，并再次回发给广告平台 |

#### 测试成功标准：

| 负责人员 | 操作 |
| --- | --- |
| AppsFlyer | 处理广告平台发来的模拟回传并将解析后信息发送到广告平台。 |
| 广告平台 | <ul><li>广告平台接收到解析后的回传。</li><li>确认AppsFlyer发送的回传与预期的事件回传内容完全一致。比如对于标识符为ID888707087的应用，假设其转化值为3，则广告平台会收到3次*af\_SKAN\_revenue*事件的回传。</li></ul> |

</Accordion>

## 说明

有关必要字段、数据维度补充、认证等的说明。

<div id="faq" />

<Accordion title="常见问题解答">

| 关于回传的常见问题答疑 |
| --- |
| **是否必须添加维度补充字段？**<br /><br />就目前而言，即使回传中缺失一个或多个必要的维度补充参数，我们也会对其进行处理。但基于以下原因，仍建议广告平台在回传中添加这些参数：<ul><li>ad\_network **\_campaign\_id**</li><li>ad\_network\_campaign **\_name**</li><li>**IP address**（IP地址）</li><li>时间戳时间戳：该信息能帮助我们正确地将激活匹配到激活发生的日期。</li></ul> |
| 是否只能发送广告系列ID**或**广告系列名称，不能两者同时发送？<br /><br />参见上一条答案。您可以使用同一个值来填充ID和名称字段。 |
| 可以。只要归因签名（Attribution Signature）有效，我们就会处理回传并忽略额外的信息。 |
| SKAN回传模板是否不同于现行回传模板？<br /><br />是两者的流程和结构不同。 |
| 对于同一个激活是否会同时收到SKAN回传和概率模型/确定性归因回传（即出现激活的重复上报）？<br /><br />可以，无论归因方法如何，对于每一个归因到某广告平台的激活，我们都会上报一条激活记录，并向该广告平台发送一条回传。<br /><br />您可以使用attribution\_source来筛选出SKAN回传。 |
| **广告平台是否需要处理来自AppsFlyer的回传？**<br /><br />不必处理回传，但建议使用回传中上报的用户质量信息对广告投放进行相应的优化。 |
| **除了发送带有SKAN信息以及补充数据的回传，是否还需要调用AppsFlyer归因链接？**<br /><br />不需要。广告平台只需向我们发送SKAN有效信息和补充数据即可。 |
| **如何在AppsFlyer面板中获得SKAN对接渠道的认证？**<ul><li>使用本文所述的任一方式完成对接</li><li>将AppsFlyer作为归因合作方，向我们发送相关应用的回传</li></ul> |
| **1-100的SKAN广告系列ID限制对我有何影响？**<br /><br />1-100的广告系列ID限制会影响您在Apple中对广告系列进行标识和编号的方式。在该限制下，您针对一个应用最多只能同时投放100个独立的广告系列。AppsFlyer支持您使用实际的广告系列名称和ID来对回传数据进行补充。也就是说，您可以将SKAN广告系列ID关联到回传送达时您实际使用的广告系列ID。只要您对于某个应用同时投放的广告系列不超过100个，则完成上述映射配置后，您对广告系列的标识及编号方式就不受1-100的ID限制影响。 |

</Accordion>

<div data-zendesk-anchors="appsflyer-offering-for-ad-networks=appsflyer%E5%8F%AF%E4%B8%BA%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E6%8F%90%E4%BE%9B%E4%BB%A5%E4%B8%8B%E4%BC%98%E5%8A%BF h_01HDG8991Y6EWWN9KYBR9FEAJZ=appsflyer%E5%8F%AF%E4%B8%BA%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E6%8F%90%E4%BE%9B%E4%BB%A5%E4%B8%8B%E4%BC%98%E5%8A%BF skan-data-flow=skan%E6%95%B0%E6%8D%AE%E6%B5%81 h_01HDG8991Y5DW0BVD674RS88F2=skan%E6%95%B0%E6%8D%AE%E6%B5%81 main-integration-parts=%E4%B8%BB%E8%A6%81%E5%AF%B9%E6%8E%A5%E6%B5%81%E7%A8%8B h_01HDG8991YDTY85NK7TQ26B2Z1=%E4%B8%BB%E8%A6%81%E5%AF%B9%E6%8E%A5%E6%B5%81%E7%A8%8B send-data-to-appsflyer=%E5%90%91appsflyer%E5%8F%91%E9%80%81%E6%95%B0%E6%8D%AE h_01HDG8991YTFP2HE0Y8P8X0C20=%E5%90%91appsflyer%E5%8F%91%E9%80%81%E6%95%B0%E6%8D%AE h_01HDG8991YRW3TWSDARFM58FA8=enrich-and-forward skan-enriched-postback-protocol=%E6%89%A9%E5%85%85%E5%90%8E%E7%9A%84skan%E6%95%B0%E6%8D%AE%E5%9B%9E%E4%BC%A0%E8%A7%84%E8%8C%83 h_01HDG8991YAKZMSA4MAY0YTFPB=%E6%89%A9%E5%85%85%E5%90%8E%E7%9A%84skan%E6%95%B0%E6%8D%AE%E5%9B%9E%E4%BC%A0%E8%A7%84%E8%8C%83 skan-enriched-postback-json-parameters=%E6%89%A9%E5%85%85%E5%90%8E%E7%9A%84json%E6%A0%BC%E5%BC%8Fskan%E5%9B%9E%E4%BC%A0%E5%8F%82%E6%95%B0 h_01HDG8991YS91CWESZH0M7CA00=%E6%89%A9%E5%85%85%E5%90%8E%E7%9A%84json%E6%A0%BC%E5%BC%8Fskan%E5%9B%9E%E4%BC%A0%E5%8F%82%E6%95%B0 curl-example%E2%80%94enriched-skan-3-postback=curl%E7%A4%BA%E4%BE%8B%E6%89%A9%E5%85%85%E5%90%8E%E7%9A%84skan-3%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE h_01HDG8991YFHBQDRG4K0XA3JQ8=curl%E7%A4%BA%E4%BE%8B%E6%89%A9%E5%85%85%E5%90%8E%E7%9A%84skan-3%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE curl-example%E2%80%94enriched-skan-4-postback-with-fine-conversion-values=curl%E7%A4%BA%E4%BE%8B%E6%89%A9%E5%85%85%E5%90%8E%E5%B8%A6%E7%B2%BE%E7%BB%86%E8%BD%AC%E5%8C%96%E5%80%BC%E7%9A%84skan-4%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE h_01HDG8991YNVCK92TVNJHGKNG5=curl%E7%A4%BA%E4%BE%8B%E6%89%A9%E5%85%85%E5%90%8E%E5%B8%A6%E7%B2%BE%E7%BB%86%E8%BD%AC%E5%8C%96%E5%80%BC%E7%9A%84skan-4%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE curl-example%E2%80%94enriched-skan-4-postback-with-coarse-conversion-values=curl%E7%A4%BA%E4%BE%8B%E6%89%A9%E5%85%85%E5%90%8E%E5%B8%A6%E7%B2%97%E7%95%A5%E8%BD%AC%E5%8C%96%E5%80%BC%E7%9A%84skan-4%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE h_01HDG8991YXTS27V0NJ4ZXQ53T=curl%E7%A4%BA%E4%BE%8B%E6%89%A9%E5%85%85%E5%90%8E%E5%B8%A6%E7%B2%97%E7%95%A5%E8%BD%AC%E5%8C%96%E5%80%BC%E7%9A%84skan-4%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE h_01HDG8991YGHWJ9R1ZKTCFJZCA=redirect implementation=%E5%90%AF%E7%94%A8%E6%96%B9%E5%BC%8F h_01HDG8991YBR7VWRH9079GT695=%E5%90%AF%E7%94%A8%E6%96%B9%E5%BC%8F query-params-for-campaign-details-not-mandatory=%E5%BB%BA%E8%AE%AE%E6%B7%BB%E5%8A%A0%E7%9A%84%E5%B9%BF%E5%91%8A%E7%B3%BB%E5%88%97%E7%9B%B8%E5%85%B3%E5%8F%82%E6%95%B0%E9%9D%9E%E5%BF%85%E9%A1%BB h_01HDG8991YQB77MMF906PCAWC2=%E5%BB%BA%E8%AE%AE%E6%B7%BB%E5%8A%A0%E7%9A%84%E5%B9%BF%E5%91%8A%E7%B3%BB%E5%88%97%E7%9B%B8%E5%85%B3%E5%8F%82%E6%95%B0%E9%9D%9E%E5%BF%85%E9%A1%BB receive-data-from-appsflyer=%E6%8E%A5%E6%94%B6appsflyer%E5%8F%91%E9%80%81%E7%9A%84%E6%95%B0%E6%8D%AE h_01HDG8991ZNF2PKKJN3FPN6QXA=%E6%8E%A5%E6%94%B6appsflyer%E5%8F%91%E9%80%81%E7%9A%84%E6%95%B0%E6%8D%AE h_01HDG8991ZKR35WHWVX0DHC612=principles h_01HDG8991ZG9GMMY57XYZF1Q3S=postback-macros-available-to-ad-network-partners h_01HDG8991ZD6ARRK6Z83NQBGRR=skan-postback-examples integration-testing=%E5%AF%B9%E6%8E%A5%E6%B5%8B%E8%AF%95 h_01HDG8991ZS10MJJ3ZN31YDPTK=%E5%AF%B9%E6%8E%A5%E6%B5%8B%E8%AF%95 h_01HDG8991ZPR41S5T9HZ9N1ZWF=real-environment testing-integration=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 h_01HDG8991ZJ1KTHX6FE9R0QJNP=%E6%B5%8B%E8%AF%95%E5%AF%B9%E6%8E%A5 test-criteria=%E6%B5%8B%E8%AF%95%E6%88%90%E5%8A%9F%E6%A0%87%E5%87%86 h_01HDG8991ZP59K8RQQ7G1GGMPG=%E6%B5%8B%E8%AF%95%E6%88%90%E5%8A%9F%E6%A0%87%E5%87%86 h_01HDG8991Z7DX65Y3E6RPHB2M3=simulated-postbacks integration-steps=%E5%AF%B9%E6%8E%A5%E6%B5%81%E7%A8%8B h_01HDG8991ZZPYH7H329EY8TNV9=%E5%AF%B9%E6%8E%A5%E6%B5%81%E7%A8%8B test-criteria::26c15d59=%E6%B5%8B%E8%AF%95%E6%88%90%E5%8A%9F%E6%A0%87%E5%87%86-1 h_01HDG8991ZR4F21KVYF0MQ9GZA=%E6%B5%8B%E8%AF%95%E6%88%90%E5%8A%9F%E6%A0%87%E5%87%86-1 clarifications=%E8%AF%B4%E6%98%8E h_01HDG8991Z8C0K0SMBT9VSX12Y=%E8%AF%B4%E6%98%8E h_01HDG8991ZDAGFV8GGC1RH73KQ=faq" />
