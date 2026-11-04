---
title: 广告平台可用的回传宏
metadata:
  keywords:
    - postbacks
    - Advertisers
    - Ad Networks
    - macros
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
  created_at: '2016-01-11T14:41:40Z'
  edited_at: '2026-10-14T10:07:00Z'
  id: 207273946
  locale: zh-cn
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/zh-cn/articles/207273946
---
> **概要：** 作为广告平台，您可以在与AppsFlyer的对接中定义回传的内容和接收端点，回传用户相关的互动，例如激活、应用内事件、再营销等。

相关对接渠道回传指南：

* <Anchor target="_blank" href="/partners/zh/docs/advanced-privacy-guide-postback-macros-for-ad-networks">高级隐私保护</Anchor>
* <Anchor target="_blank" href="/partners/zh/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/zh/docs/rejected-attribution-postbacks-to-integrated-partners">被拒绝的归因回传</Anchor>

<div id="postbacks-for-ad-networks" />

## 广告平台的回传

* **回传配置：** 要更改您的回传设置，可通过<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>提交请求，或联系您的AppsFlyer合作伙伴拓展经理。
* **回传类型**：可对激活、应用内事件以及被拦截的激活和应用内事件（由Protect360识别或违反定向验证规则的事件）进行回传。

<div id="postback-data-sources" />

### 回传数据来源

| 来源 | 说明 |
| --- | --- |
| <Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters">归因链接参数</Anchor> | 合作渠道在点击和展示URL中提供的参数。<br /><br />例如: 归因链接中的点击ID参数 -"&click\_id=CLICK\_ID" |
| AppsFlyer中的合作渠道ID | 合作渠道向广告主提供的唯一ID。<br /><br />示例：app ID、account ID、user ID、network ID |
| SDK提取的信息 | AppsFlyer SDK从设备中提取的信息。<br /><br />示例：可通过 "&IDFA=(idfa)" 在回传中获取iOS设备ID |
| AppsFlyer平台提取信息 | 由AppsFlyer平台提取的信息。 |
| Protect360及验证规则 | 被判定为作弊、违反定向投放规则的激活及其关联的应用内事件信息。 |

<div id="postback-macros" />

## 回传宏

在回传中出现时，宏会被替换为与用户相关的数据。例如，要获取安装应用用户的IP地址，可以在回传结构中加入`country_code=(ip)`。支持的宏如下表所示：

表格说明：

* **数据来源：** 数据的产生来源。
  * 链接：归因链接
  * SDK：嵌入应用中的AppsFlyer SDK或S2S API
  * AF：经AppsFlyer处理的数据
* **全部发送**:若为是，则您可以接收归因到其他广告平台或自然流量的激活和事件数据（即非归因于您的流量）。
* **[基础] 适用于所有回传的宏**：涵盖激活、应用内事件和被拒绝事件。
* **[可选]** 仅适用于应用内事件和被拒绝事件，详见表格中的标注（如rejected、in-app）。

<div id="macrosinstalls-in-app-events-and-rejected-events" />

### 激活、应用内事件和被拒绝事件中的宏

| 回传宏（名称） | 来源 | 全部发送 | 说明 | [基础] 适用于所有回传的宏 | [可选] 仅适用于应用内事件和被拒绝事件 |
| --- | --- | --- | --- | --- | --- |
| <span id="advertising_id"></span>advertising\_id | SDK | 是 | 用户可重置的设备ID，又称GAID。即: (sha1-advertiserId) | 是 |  |
| <span id="af_ad"></span>af\_ad | 链接 | 否 | 广告名称（<Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#数据粒度级别">了解详情</Anchor>）- 由广告主/媒体提供 | 是 | 是 |
| <span id="af_ad_id"></span>af\_ad\_id | 链接 | 否 | 由广告主/媒体提供 | 是 | 是 |
| <span id="af_ad_type"></span>af\_ad\_type | 链接 | 否 | 请使用以下命名方式配置参数值：<ul><li>**text**（文本）：仅包含文本的广告，比如搜索结果</li><li>**banner**（横幅）；显示在设备屏幕顶部或底部的基础样式</li><li>**interstitial**（插屏）：在当前体验暂停时出现的全屏广告</li><li>**video**（视频）：无奖励的标准视频</li><li>**rewarded\_video**（奖励视频）：向观看视频的用户提供应用内奖励的广告</li><li>**playable**（可玩广告）：包含预览式互动体验的广告</li><li>**sponsored\_content**（赞助内容）：软文等赞助内容中所包含的链接</li><li>**audio**（音频）：音频广告</li></ul> | 是 | 是 |
| <span id="af_adset"></span>af\_adset | 链接 | 否 | <ul><li>由广告商/媒体提供</li><li>广告组是在广告系列之下、广告之上的一个广告层级。<Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#数据粒度级别">详情请见此处。</Anchor></li></ul> | 是 | 是 |
| <span id="af_adset_id"></span>af\_adset\_id | 链接 | 否 | 由广告主/媒体提供 | 是 | 是 |
| <span id="af_c_id"></span>af\_c\_id | 链接 | 否 | 由广告主/媒体提供 | 是 | 是 |
| <span id="af_siteid"></span>af\_siteid | 链接 | 否 | <ul><li>用于标记媒体的唯一ID。<Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#site-id-parameter">详情请见此处说明。</Anchor></li></ul> | 是 | 是 |
| <span id="af_subsite_id"></span>af\_subsite\_id | 链接 | 否 | <ul><li>次级广告平台/媒体ID。</li><li>如果除了主要媒体（子渠道）以外还有次级媒体，或者您想要了解广告样式（如横幅、插屏、视频）等的其他信息，请使用af\_sub\_siteid参数。示例：af\_sub\_siteid =ABCD\_4567</li></ul> | 是 | 是 |
| <span id="af_validated"></span>af\_validated | AF | 是 | 表示购买是否成功验证。可能的取值：true 或 false。 | 是 |  |
| <span id="af_validation_type"></span>af\_validation\_type | AF | 是 | 表示执行的验证类型。可能的取值：roi360\_purchase，roi360\_subscription或Basic。 | 是 |  |
| <span id="app_id"></span>app\_id | SDK | 是 | 应用上报的app ID | 是 |  |
| <span id="app_name"></span>app\_name | SDK | 是 | 广告主设置的应用名称 | 是 |  |
| <span id="app_version"></span>app\_version | SDK | 是 | 开发者在应用代码中设置的应用版本名称 | 是 |  |
| <span id="appsflyer_id"></span>appsflyer\_id | SDK | 是 | AppsFlyer在转化时记录的唯一标识符 | 是 |  |
| <span id="att01"></span>att-0-1 | SDK | 是 | 可用值包括：<ul><li>1:ATT状态已授权或af\_authorized。</li><li>0:任何其他ATT状态。</li></ul> | 是 |  |
| <span id="attstatus"></span>att-status | SDK | 是 | iOS上报的<Anchor target="_blank" href="/marketers/zh/docs/att-implications-ios-14-and-deprecation-of-lat#att-values">ATT状态</Anchor>，如authorized、not\_determined。<br /><br />在某些情况下，该字段可能为空，返回 ""。 | 是 |  |
| <span id="attributed_touch_type"></span>attributed\_touch\_type | SDK | 否 | 可能的取值：点击、展示、电视广告、预装 | 是 |  |
| <span id="blocked_reason"></span>blocked\_reason | AF | 否 | 作弊/验证规则原因 | 否 | rejected |
| <span id="blocked_reason_value"></span>blocked\_reason\_value | AF | 否 | 作弊/验证规则原因值（如站点ID） | 否 | rejected |
| <span id="blocked_sub_reason"></span>blocked\_sub\_reason | AF | 否 | 作弊/验证规则子原因 | 否 | rejected |
| <span id="bundle_id"></span>bundle\_id | SDK | 是 | iOS：用于标记iOS平台中一个或一组应用的标识符（请参阅Apple关于Bundle ID的开发者文档）Android：应用名称 | 是 |  |
| <span id="c"></span>c | 链接 | 否 | 由广告商/媒体提供超过100个字符的广告系列活动名称将在后台显示为 'c\_name\_exceeded\_max\_length'。 | 是 | 是 |
| <span id="country_code"></span>country\_code | AF | 是 | ISO 3166（alpha-2）中的国家代码，如：US、CN。 | 是 |  |
| <span id="event_name"></span>event\_name | SDK | 是 | 分配给事件的名称 | 否 | 应用内事件 |
| <span id="event_revenue_currency"></span>event\_revenue | SDK | 是 | 由SDK上报的事件值，使用event\_revenue\_currency或您所选择的币种。 | 否 | 应用内事件 |
| {"event_revenue"}  <br />{"_currency"} | SDK | 是 | 事件中报告的事件收入货币代码或您选择的币种 | 否 | 应用内事件 |
| <span id="event_revenue_usd"></span>event\_revenue\_USD | AF | 是 | 事件价值 (美元) | 否 | 应用内事件 |
| <span id="event_time"></span>event\_time | SDK | 是 | Event time | 否 | 应用内事件 |
| <span id="event_value"></span>event\_value | SDK | 是 | 应用内事件包含的属性及其取值，可以在回传中以JSON格式完整发送。通过 (encode) 宏进行URL编码。 | 否 | 应用内事件 |
| <span id="idfa"></span>idfa | SDK | 是 | iOS设备上的可重置用户广告ID。也可用作：(sha1-idfa) | 是 |  |
| <span id="idfv"></span>idfv | SDK | 是 | iOS设备上每个用户在每个厂商下的唯一标识符 | 是 |  |
| <span id="imei"></span>imei | SDK | 是 | 用于识别手机的唯一号码 | 是 |  |
| <span id="install_time"></span>install\_time | SDK | 是 | 激活时间戳 | 是 |  |
| <span id="install_unix_ts"></span>install\_unix\_ts | SDK | 是 | 以unix格式表示的激活时间戳 | 是 |  |
| <span id="is_attributed"></span>is\_attributed | AF | 是 | 表示激活或事件是否归因于此渠道的标记 | 是 |  |
| <span id="is_contrib"></span>is\_contrib | AF | 是 | 表示该广告平台是否位列激活的前三大贡献渠道。<ul><li>若广告平台未赢得归因但在前三贡献渠道中，则`is_contrib=1`。</li><li>若广告平台赢得归因，则`is_contrib=0`。</li><li>若广告平台不在前三贡献渠道，则`is_contrib=0`。</li></ul> | 是 |  |
| <span id="is_lat"></span>is\_lat | SDK | 是 | Limit ad tracking（限制广告跟踪，简称LAT）：iOS：Apple在iOS 14以后的版本中不再使用LAT，而是通过ATT判断用户的隐私状态，在这种情况下请忽略is\_lat。对于iOS 14以下的版本，如果该字段值为true，即表示IDFA不可用且显示为0。安卓：如果该字段值为true，即表示用户选择了关闭个性化广告，但这不会限制对GAID的收集。 | 是 |  |
| <span id="is_organic"></span>is\_organic | AF | 是 | 当针对所有媒体渠道（包括自然量）发送激活回传时，广告平台可获知该激活是否为自然激活。 | 仅激活 |  |
| <span id="is_primary_attribution"></span>is\_primary\_attribution | AF | 是 | 若为false，请查看is\_retargeting。 | 否 | 应用内事件 |
| <span id="is_retargeting"></span>is\_retargeting | 链接 | 否 | 与is\_primary\_attribution配合使用。另请参见<Anchor target="_blank" href="/marketers/zh/docs/resolve-retargeting-double-attribution">再营销事件的双重归因</Anchor>。<br /><br />若为true (1)，则事件作为再营销活动的一部分上报，媒体渠道为再营销渠道。<br /><br />若为false (0)，且is\_primary\_attribution也为false，则事件属于再营销活动，但媒体渠道为用户归因渠道。 | 否 |  |
| <span id="language"></span>language | SDK | 是 | 由设备上报的设备操作系统语言（语言环境）。 | 是 |  |
| <span id="oaid"></span>oaid | SDK | 是 | 部分安卓设备上的用户可重置ID，通常作为GAID的替代方案。 | 是 |  |
| <span id="partner_event_id"></span>partner\_event\_id | AF | 是 | 在合作渠道平台中的对应事件名称/ID。 | 否 | 应用内事件 |
| <span id="platform"></span>platform | SDK | 是 | 设备系统：iOS、Android或Windows Mobile | 是 |  |
| <span id="retargeting-conversion-type"></span>retargeting\_conversion\_type | AF | 否 | 标记该事件是否为重新归因或再互动。 | 仅再营销 |  |

<div id="in-app-event-only-macros" />

### 仅适用于应用内事件的宏

以下示例展示了广告平台可用的应用内事件回传。

<div id="example" />

> 📄 **示例**
>
> 事件回传模板 "&event=(event)&json=(encode)" 在具体的af\_purchase事件中被转换为如下回传：
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> 此回传的解码JSON值是
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

<div id="encoded-values" />

#### **编码值说明**

回传可能包含非字母数字的特殊字符。为了确保这些值能被正确传输，AppsFlyer会对所有非字母数字的值进行URL编码。

要对回传进行解码或编码，可使用<Anchor target="_blank" href="https://www.urldecoder.org/">编码网络服务。</Anchor>

<div id="sample-postbacks" />

## 回传示例

<div id="general-install-postback-examples" />

### 常规激活回传示例

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)
&advertising_id=(advertiser_id)&android_id=(android_id)
&install_time=(install_unix_ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?&site_id=(publisher_id)&
device_ip=(ip)&;idfa=(idfa)&install_time=(install_unix_ts)
```

</Tab>
</Tabs>

<div id="general-in-app-event-postback-examples" />

### 常规应用内事件回传示例

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)&
device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android_id)&
install_time=(install_unix_ts)&event_name=(event_name)&currency=(currency)&
json=(event_value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?clickid=(clickid)&site_id=(publisher_id)&
device_ip=(ip)&idfa=(idfa)&install_time=(install_unix_ts)
&event_name=(event_name)&currency=(currency)&json=(event_value)
```

</Tab>
</Tabs>

<div id="in-app-event-postback-example" />

### 应用内事件回传示例

事件参数:

* 事件名称：af\_revenue
* 事件收入：120.00
* Event Currency（事件货币）：USD
* 事件值：`{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

回传：

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-ad-networks=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E7%9A%84%E5%9B%9E%E4%BC%A0 01JHFZWJT74GNA6J5MYMQBGDWX=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E7%9A%84%E5%9B%9E%E4%BC%A0 postback-data-sources=%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE%E6%9D%A5%E6%BA%90 01JHFZWJT978TTXB7FQ6AVG1ZS=%E5%9B%9E%E4%BC%A0%E6%95%B0%E6%8D%AE%E6%9D%A5%E6%BA%90 postback-macros=%E5%9B%9E%E4%BC%A0%E5%AE%8F 01JHFZWJTTP66NHZRG0RQAY3W8=%E5%9B%9E%E4%BC%A0%E5%AE%8F macros%E2%80%94installs-inapp-events-and-rejected-events=%E6%BF%80%E6%B4%BB%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%92%8C%E8%A2%AB%E6%8B%92%E7%BB%9D%E4%BA%8B%E4%BB%B6%E4%B8%AD%E7%9A%84%E5%AE%8F 01JHFZWJTXD2K4RJ8RDWXKSYDD=%E6%BF%80%E6%B4%BB%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%92%8C%E8%A2%AB%E6%8B%92%E7%BB%9D%E4%BA%8B%E4%BB%B6%E4%B8%AD%E7%9A%84%E5%AE%8F inapp-event-only-macros=%E4%BB%85%E9%80%82%E7%94%A8%E4%BA%8E%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E7%9A%84%E5%AE%8F 01JHFZWK3FQ5HCX9NDEKT6SPT1=%E4%BB%85%E9%80%82%E7%94%A8%E4%BA%8E%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E7%9A%84%E5%AE%8F 01JHFZWK3F2E31WE5N1G0T0ZHA=%E7%A4%BA%E4%BE%8B encoded-values=%E7%BC%96%E7%A0%81%E5%80%BC%E8%AF%B4%E6%98%8E 01JHFZWK3GM9XRS2GC4SNXFVD7=%E7%BC%96%E7%A0%81%E5%80%BC%E8%AF%B4%E6%98%8E sample-postbacks=%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B 01JHFZWK3GJSA8RF4AMKVM4XD4=%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B general-install-postback-examples=%E5%B8%B8%E8%A7%84%E6%BF%80%E6%B4%BB%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B 01JHFZWK3HD1NFJJW1Y8HGVPX2=%E5%B8%B8%E8%A7%84%E6%BF%80%E6%B4%BB%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B general-inapp-event-postback-examples=%E5%B8%B8%E8%A7%84%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B 01JHFZWK3JW0D1GZ739FV0EZWG=%E5%B8%B8%E8%A7%84%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B inapp-event-postback-example=%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B 01JHFZWK3JT8GM7BEM3RXCMXV5=%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0%E7%A4%BA%E4%BE%8B" />
