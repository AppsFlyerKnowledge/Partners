---
title: 广告平台的高级隐私保护指南和回传宏
metadata:
  keywords:
    - Ad Networks
    - Partners
    - ios14
    - SKAD
    - Advanced Privacy
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-07-27T07:09:37Z'
  edited_at: '2026-10-14T10:15:31Z'
  id: 360011316197
  locale: zh-cn
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/zh-cn/articles/360011316197
---
> **概要：概要：本文解释了高级隐私保护（Advanced Privacy，简称AP）启用时与渠道共享数据的注意事项，并为广告平台提供了高级隐私保护回传的设置指南。请注意：本文与SKAdNetwork回传无关，且其中的信息不适用于广告主。**

<div id="advanced-privacy-for-ad-networks-news" />

> 📄 **广告平台的高级隐私保护适用条件**
>
> 本文所述的高级隐私保护回传机制在同时符合以下条件时生效：
>
> * 用户设备的操作系统为iOS 14.5+
> * 高级隐私保护（Advanced Privacy）处于启用状态

![AdvancedPrivacy.png](https://files.readme.io/2a80740637c1003e03bc169df274bf0fa6240ee850c7fd6e967c4abea234e0d1-360018213598.png)

本文内容涵盖以下主题：

* 高级隐私保护模式下的数据共享对渠道的影响
* 用于归因的[点击链接](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements)需要符合的要求
* 在AppsFlyer控制面板中设置您的高级隐私保护[回传](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification)
* [高级隐私保护模式和SKAdNetwork](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#ap-vs-skadnetwork)之间的区别。

<div id="ad-network-advanced-privacy-data-sharing-principles" />

## 广告平台在高级隐私保护（AP）模式下的数据共享原则

从iOS14.5+开始，广告主可以通过AppsFlyer<Anchor target="_blank" href="/marketers/zh/docs/apply-aggregated-advanced-privacy-framework">汇总层级的高级隐私保护框架</Anchor>（即Aggregated Advanced Privacy Framework，简称AAP）把控AppsFlyer提供的用户级别归因数据的可用性。

在广告平台的场景中，AAP框架是通过高级隐私保护（AP）来实现的。为了便于说明，本文中将高级隐私保护（Advanced Privacy）简称为AP，两者意义完全相同。

AP并不影响汇总数据对渠道或广告平台的可用性。

**受到AP影响的数据**

AP处于启用状态时，如果iOS 14.5+用户在ATT弹窗中拒绝授权广告追踪，则广告平台无法通过回传或其他数据上报方式（包括各种Protect360假量报告）来获取其用户级别数据。

也就是说，AppsFlyer会根据用户的ATT授权状态等各种因素的具体情况，相应地使用不同类型的回传。

 该设置默认开启。

![APforPartners2.png](https://files.readme.io/e4fb5617a47635f24dc83881c2be3d18b770200a576cb67bd3312e6fc2c123e1-360018154777.png)

<div id="types-of-templates-for-sending-postbacks" />

#### 用于发送回传的各类模版

* **常规模板**常规模板：您与AppsFlyer之间的现行对接模板，其中带有用户标识符以及归因数据宏。该模板用于发送包含用户级别归因数据的回传。
* 该模板用于发送包含汇总归因数据的回传。   
  **请注意：** 请注意：如果有AP回传要求，但您尚未完成AP对接，则AppsFlyer不会发送回传。您可以使用我们的自助回传管理工具设置AP对接。

<div id="note" />

> 📘 **注意**
>
> * 如果用户在广告主应用和流量侧应用中都授权了ATT（即“双授权”），则AppsFlyer会同时向获得归因以及未获得归因的广告平台发送常规回传。
> * **请注意：** 例外情况：对于归因到Apple Search Ads（ASA）的激活，ASA会在符合以下条件时向相关广告平台发送激活回传，无论广告主是否启用高级隐私保护模式：
>   * 用户拒绝授权
>   * 相关广告平台的激活回传设置为**所有媒体渠道，包括自然流量**
>   * 该广告平台不支持高级隐私保护模式

<div id="type-of-postback-used" />

### 使用的回传类型

下表适用于iOS 14.5+用户的数据。

请注意： 如果用户的操作系统为iOS14.4或更早的版本，则下表所列信息不适用。AppsFlyer会使用常规模板向获得归因以及未获得归因的广告平台发送回传。

<div id="postback-type-for-ios-145" />

#### 适用于iOS 14.5+的回传类型

<table><thead><tr><th rowspan="2"><p>AP状态</p></th><th colspan="2">ATT状态</th><th rowspan="2">向获得归因的AP适配渠道\*发送的回传模板类型 </th><th rowspan="2">向获得归因的非AP适配渠道\*发送的回传模板类型 </th><th rowspan="2">向未获得归因的渠道发送的回传\*</th></tr><tr><th><p>流量侧应用（Publisher App）</p></th><th><p>广告主 App</p></th></tr></thead><tbody><tr><td><p><span>启用</span></p></td><td><p><span>已授权</span></p></td><td><p><span>Not authorized（拒绝授权）</span></p></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">AP模板</a>（汇总数据）</p></td><td><p><span>无回传</span></p></td><td><p><span>无</span></p></td></tr><tr><td><p><span>启用</span></p></td><td><p><span>Not authorized（拒绝授权）</span></p></td><td><p><span>已授权</span></p></td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">AP模板</a>（汇总数据）</td><td><p><span>无回传</span></p></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">常规模板</a></p><p><span>归因字段</span>不存在。\*</p></td></tr><tr><td><p><span>启用</span></p></td><td><p><span>已授权</span></p></td><td><p><span>已授权</span></p></td><td><p><span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">常规模板</a></p></td><td> <span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">常规模板</a> </td><td> 归因字段不存在。\* </td></tr><tr><td><p><span>启用</span></p></td><td><p><span>Not authorized（拒绝授权）</span></p></td><td><p><span>Not authorized（拒绝授权）</span></p></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#使用的回传类型"><span>AP模板</span></a>（汇总数据）</p></td><td><p><span>无回传</span></p></td><td><p><span>无</span></p></td></tr><tr><td><p><span>停用</span></p></td><td><p><span>未选择授权状态</span></p></td><td><p><span>未选择授权状态</span></p></td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">常规模板</a></td><td><p><span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">常规模板</a></p></td><td><p><span></span><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#用于发送回传的各类模版">常规模板</a></p><p><span>归因字段</span>不存在。\*</p></td></tr></tbody></table>

**(\*) 与渠道共享数据的原则**

任何一个事件都有可能会对应多个有权获得其回传的合作渠道。具体的回传发送对象如下：

* 未归因的合作伙伴：对接合作伙伴不归因于事件，当**应用内事件回传>** **发送选项**设置为<strong>包括自然渠道的所有媒体渠道。</strong>如果用户在广告主应用中授权了ATT，则回传中会包含不带归因数据的用户ID。(此选项不受所有广告平台的支持。)  

  ![InAppEventAll.png](https://files.readme.io/e24037f75b2b82797031eb13d5e063b8c2006812491e69674ff066ac830919f7-35847850644881.png)

<div id="web-campaigns" />

### 网页广告

当广告平台在网页上投放广告时，AP模式的生效方式不同于应用内广告场景。

<div id="postback-type-used-for-ios-145-when-ap-is-on" />

#### AP开启时适用于iOS 14.5+的回传类型

<table><thead><tr><th colspan="2">ATT状态</th><th rowspan="2">向获得归因的渠道发送的回传类型</th><th rowspan="2">向未获得归因的渠道发送的回传类型\*</th></tr><tr><th><p>流量侧应用（Publisher App）</p></th><th><p>广告主 App</p></th></tr></thead><tbody><tr><td><p><span>不适用</span></p></td><td><p><span>Not authorized（拒绝授权）</span></p></td><td><p><span>高级隐私保护</span></p></td><td><p><span>无</span></p></td></tr><tr><td><p><span>不适用</span></p></td><td><p><span>已授权</span></p></td><td><p>常规IDFA, IDFV, CUID, Click ID</p></td><td><p>常规。仅限用户级别ID。</p></td></tr></tbody></table>

<div id="integration" />

## 对接

更新您的点击链接并完成高级隐私保护对接。

<div id="click-url-requirements" />

<Accordion title="点击链接的配置要求">

大部分情况下，流量侧应用和/或广告主应用中的IDFA可能不可用，具体取决于用户的ATT授权状态。这时，AppsFlyer可能会使用汇总层级的高级隐私保护机制和<Anchor target="_blank" href="/marketers/zh/docs/appsflyer-attribution-model#aggregated-advanced-privacy-aap">概率建模</Anchor>来完成归因。

【最佳方式】建议发送下表所列的所有参数，以确保您带来的流量能得到充分的归因。

1. 请在点击链接的末尾添加以下参数：

<table><thead><tr><th>标识符</th><th>点击参数</th><th><p>示例</p></th></tr></thead><tbody><tr><td><p><span>Campaign</span></p></td><td><p><span>c</span></p></td><td><p><span>US_20_30</span></p></td></tr><tr><td><p><span>即广告系列的ID</span></p></td><td><p><span>af_c_id</span></p></td><td><p><span>12345</span></p></td></tr><tr><td><p><span>Adset</span></p></td><td><p><span>af_adset</span></p></td><td><p><span>ADSET_1</span></p></td></tr><tr><td><p><span>即广告组的ID</span></p></td><td><p><span>af_adset_id</span></p></td><td><p><span>56789</span></p></td></tr><tr><td><p><span>Ad </span></p></td><td><p><span>af_ad</span></p></td><td><p><span>creative_name</span></p></td></tr><tr><td><p><span>即相关广告的ID</span></p></td><td><p><span>af_ad_id</span></p></td><td><p><span>34567</span></p></td></tr><tr><td><p><span>Site ID</span></p></td><td><p><span>af_siteid</span></p></td><td><p><span>abcdefgh12345678</span></p></td></tr><tr><td><p><span>Subsite ID</span></p></td><td><p><span>af_sub_siteid</span></p></td><td><p><span>abcdefgh12345678</span></p></td></tr><tr><td><p><span>流量入口（Channel）</span></p></td><td><p><span>af_channel</span></p></td><td><p><span>channel_name</span></p></td></tr><tr><td><p><span>Ad type</span></p></td><td><p><span>af_ad_type</span></p></td><td><p><span>video</span></p></td></tr><tr><td><p>iOS device model\*</p></td><td><p><span>af_model</span></p></td><td><p>用于表示设备型号。允许的值：</p><ul><li>iphone（全部小写）</li><li>ipad（全部小写）</li></ul></td></tr><tr><td><p><span>Operating system\*</span></p></td><td><p><span>af_os</span></p></td><td><p><span>操作系统版本</span></p></td></tr><tr><td colspan="3"><p>\* 您也可以通过用户代理（user agent）提供部分信息，这时我们会优先使用通过具体标识符发送的值。</p></td></tr></tbody></table>

   在点击链接末尾添加广告系列信息

   请参照以下示例在点击链接中添加广告系列信息：

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adsetname}&af_adset_id={adset ID}&af_ad={adname}&af_ad_id={ad ID}&af_ad_type={Adtype}&af_siteid={PublisherId}` |
| --- |

2. 请在点击链接中添加下列必须配置的参数*：  

   <div id="caution" />

   > ❗️ **注意事项**
   >
   > 如果您未在点击请求中添加必须配置的参数，则您带来的大部分激活都不会归因到贵平台。


   * IP
   * User-agent

   * 若使用跳转到AppsFlyer的HTTP referrer发送点击，则无需任何操作。

   若您使用以下任一方式发送点击，请使用本文所述的数据提取方法在点击链接末尾添加相关参数：

   * 点击请求通过应用内流量跳转
   * 服务器到服务器的点击（又称S2S）

   <div id="parameters-for-advanced-privacy-attribution" />

   #### 适用于高级隐私保护归因的参数

   <Table>
     <thead>
       <tr>
         <th>
           参数
         </th>
         <th>
           必须配置
         </th>
         <th>
           数据提取方法
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           **设备语言和区域设置**

           af\_lang
         </td>
         <td>
           否
         </td>
         <td>
           NSString *language = [[NSLocale preferredLanguages] objectAtIndex:0];

           【推荐方式】建议您同时提供语言和区域设置，例如en-US。
         </td>
       </tr>
       <tr>
         <td>
           **User-agent**

           af\_ua
         </td>
         <td>
           是
         </td>
         <td>
           请使用以下格式提取user-agent：

           ```
           Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+13_3_1  
           +like+Mac+OS+X%29 AppleWebKit%2F605.1.15+%28KHTML%2C  
           +like+Gecko%29+Mobile%2F15E148
           ```

           * 请务必提取**非**CFNetwork的*user-agent*。
           * user-agent值须经URL编码处理。
         </td>
       </tr>
       <tr>
         <td>
           **设备IP地址**

           af\_ip
         </td>
         <td>
           是
         </td>
         <td>
           在af\_ip参数中提供设备IP（若可用）。

           次优方案：AppsFlyer会使用X-Forwarded-For中的IP（若可用）。
         </td>
       </tr>
     </tbody>
   </Table>

   在点击链接末尾添加参数

   如需通过点击归因链接传递这些必要参数，请参考以下示例：

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad-type}&af_siteid={PublisherId}&af_ua={USER-AGENT}&af_lang={LANGUAGE}&af_ip={IP}` |
| --- |

   **示例**

| `ID}`<br />`&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />`&af_ua=Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2012_1_4%20`<br />`like%20Mac%20OS%20X%29%20AppleWebKit%`<br /><br />`2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%2F16D57&af_lang=en-US&af_ip=11.11.1.11` |
| --- |

   * 查询参数须经URL编码处理。

   **通过点击链接请求header传递数据**

   如需通过点击链接请求header传递数据，请参考以下示例：

| GET<br /><br />`accept-language: en-US,en;q=0.`<br /><br />`User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)`<br /><br />`AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148`<br /><br />`X-Forwarded-For: 11.11.1.11, 222.222.2.222` |
| --- |

</Accordion>

<div id="advanced-privacy-postback-specification" />

<Accordion title="高级隐私保护回传规范">

**常规模板和高级隐私保护模板的区别**

* 每小时发送一批回传。
  * 涵盖所有事件类型。
  * 涵盖归因和拦截回传。
  * 0.001%的回传可能会在之后的批次中发送，最多可能会有24小时的延迟。
* 回传时间与事件实际发生时间无关。
* 时间戳宏：
  * 对于激活和应用内事件，时间戳近似到转化发生时间的小时数。例如，如果事件发生时间为22:55:30，则其上报的时间戳为22:00:00。
  * 按UTC时区上报时间戳。时间戳示例：(2020-07-20 20:00:00) (2020-07-20 20:00:00)

**广告平台进行对接时必须完成的操作：**

1. [在AppsFlyer面板中设置您的高级隐私保护回传。](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback)
2. <Anchor target="_blank" href="/partners/zh/docs/ios-integration-testing-for-ad-networks">测试高级隐私保护对接。</Anchor>

<div id="important" />

> 🚧 **重要提示！**
>
> * 如需区分正常事件和被拦截的回传，必须配置被拦截的回传宏。
> * 如需启用被拦截的激活/事件回传，请使用<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系我们。

<div id="advanced-privacy-postback-endpoint-complete-as-required" />

#### 高级隐私保护回传端点【根据实际需求配置】

| 回传类型 |
| --- |
| 激活 |
| 应用内事件 |

<div id="advanced-privacy-attribution-macros-available" />

#### 高级隐私保护归因可用参数

<table><thead><tr><th><p>回传宏（名称）</p></th><th>说明</th><th>所有回传的基础参数</th><th>应用内事件可选参数 </th><th>被拦截归因的可选参数</th></tr></thead><tbody><tr><td>af_ad</td><td>广告素材名称</td><td>是</td><td> </td><td> </td></tr><tr><td>af_ad_id</td><td>34567</td><td>是</td><td> </td><td> </td></tr><tr><td>af_ad_type</td><td>例如：banner、footer、video</td><td>是</td><td> </td><td> </td></tr><tr><td>af_adset</td><td>ADSET_1</td><td>是</td><td> </td><td> </td></tr><tr><td>af_adset_id</td><td>56789</td><td>是</td><td> </td><td> </td></tr><tr><td>app_id</td><td>-</td><td>是</td><td> </td><td> </td></tr><tr><td>app_name</td><td>-</td><td>是</td><td> </td><td> </td></tr><tr><td>attributed_touch_hour</td><td><p>小时数就近取整。 </p><p>具体格式请参考脚注（1）</p></td><td>是</td><td> </td><td> </td></tr><tr><td>attributed_touch_type</td><td>如click（点击）、impression（展示）</td><td>是</td><td> </td><td> </td></tr><tr><td>blocked_reason</td><td>适用于验证规则（Validation Rules）/Protect360</td><td> </td><td> </td><td>是</td></tr><tr><td>blocked_reason_value</td><td>适用于验证规则（Validation Rules）/Protect360</td><td> </td><td> </td><td>是</td></tr><tr><td>blocked_sub_reason</td><td>适用于验证规则（Validation Rules）/Protect360</td><td> </td><td> </td><td>是</td></tr><tr><td>bundle_id</td><td>由广告主设置</td><td>是</td><td> </td><td> </td></tr><tr><td>c</td><td>广告系列名称，如US_20_30</td><td>是</td><td> </td><td> </td></tr><tr><td>af_c_id</td><td>广告系列ID，如12345</td><td>是</td><td> </td><td> </td></tr><tr><td>af_channel</td><td>流量入口名称</td><td>是</td><td> </td><td> </td></tr><tr><td>country_code</td><td>转化发生时记录到的ISO国家代码</td><td>是</td><td> </td><td> </td></tr><tr><td>event_hour</td><td><p>小时数就近取整。 </p><p>具体格式请参考脚注（1）</p></td><td>是</td><td> </td><td> </td></tr><tr><td>event_name</td><td>由相关应用上报</td><td> </td><td>是</td><td> </td></tr><tr><td>event_revenue</td><td>以事件货币为单位的收入金额</td><td> </td><td>是</td><td> </td></tr><tr><td>event_revenue_<br/>currency</td><td></td><td> </td><td>是</td><td> </td></tr><tr><td>event_revenue_usd</td><td>换算成USD的收入金额</td><td> </td><td>是</td><td> </td></tr><tr><td>install_hour</td><td><p>小时数就近取整。 </p><p>具体格式请参见脚注（1）</p></td><td>是</td><td> </td><td> </td></tr><tr><td>is_first</td><td>相关应用内事件首次被用户触发时，该参数的值为True</td><td> </td><td>是</td><td> </td></tr><tr><td>is_primary</td><td><p>用于去重</p><p>布尔21</p></td><td> </td><td>是</td><td> </td></tr><tr><td>is_retargeting</td><td><p>用于去重 </p><p>格式：参见脚注（2）</p></td><td>是</td><td> </td><td> </td></tr><tr><td>is_reengagement</td><td><p>格式：参见脚注（2）</p></td><td> </td><td>是</td><td> </td></tr><tr><td>is_reattribution</td><td><p>用于去重 </p><p>格式：参见脚注（2）</p></td><td>是</td><td> </td><td> </td></tr><tr><td>match_type</td><td>如: id_matching、probabilistic</td><td>是</td><td> </td><td> </td></tr><tr><td>event_id</td><td>该事件在广告平台中的对应名称/ID</td><td> </td><td>是</td><td> </td></tr><tr><td>platform</td><td>如：ios、Android</td><td>是</td><td> </td><td> </td></tr><tr><td>postback_id</td><td>具有唯一性的回传ID</td><td>是</td><td> </td><td> </td></tr><tr><td>retargeting_<br/>conversion_type</td><td>如：re-engagement（再互动）、re-attribution（再归因）</td><td>是</td><td> </td><td> </td></tr><tr><td>af_siteid</td><td>abcdefgh12345678</td><td>是</td><td> </td><td> </td></tr><tr><td>af_sub_siteid</td><td>abcdefgh12345678</td><td>是</td><td> </td><td> </td></tr></tbody><tfoot><tr><td colspan="5"><p>请注意：</p><p>（1）支持以下时间戳格式：</p><ul><li> </li><li>10位UNIX时间戳。 </li></ul><p>（2）支持以下布尔格式：</p><ul><li>21 </li><li>字符串：<em>false</em>、<em>true</em> </li></ul></td></tr></tfoot></table>

</Accordion>

<div id="setting-up-your-advanced-privacy-postback" />

<Accordion title="设置您的高级隐私保护回传">

您可以使用AppsFlyer面板中的回传管理选项设置您的AP回传。

**前期准备**：

* 如需管理您的高级隐私保护回传，您与AppsFlyer之间必须存在活跃对接。请通过<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系我们，以<Anchor target="_blank" href="/partners/zh/docs/getting-started-onboarding-guide-for-ad-networks">创建对接</Anchor>。

**请按以下方式设置回传：**

1. 从页面顶部导航栏打开账户菜单（点击右上角的邮箱地址，打开下拉菜单）> **回传管理**。
2. 高级隐私保护：
3. 激活配置工具。  

   ![postback-management-enter-endpoint_en-us.png](https://files.readme.io/4ea0ffc61d1ecdb11d3c745876c29a942fde4133b8ebb54a1426a73c1dc63b16-360018215218.png)
4. 输入**端点地址**。请输入激活和/或应用内事件的对应URL。
5. 输入回传中需要包含的参数：
   * 参数名称
   * **渠道映射参数**：即渠道侧接收到的对应参数
   * **参数值**（适用于某些参数）：选择参数值的格式。如在布尔型参数下可选的参数值格式为"true"/"false"或1/0。
   * **激活**：勾选需要在激活回传中传递的参数。
   * **应用内事件**：勾选需要在应用内事件回传中传递的参数。

   ![postback-management-parameters_en-us.png](https://files.readme.io/818ef31df9c4e349ca26b5421a0ba0582ed5f7f9fae39f1d0e4ec3b7562f4192-360018213698.png)

   [高级隐私保护回传宏](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification)完整列表。
6. <strong>【可选】</strong>在AppsFlyer预定义参数之外添加自定义参数：

   ![postback-management-custom-parameters_en-us.png](https://files.readme.io/6bca46e1d39c6822b0e041eb1dcbb1b2d40e42fa062c34877c8cbf0c2d2847d6-16589581250321.png)
7. 查看最终的回传模板预览，检查各项配置是否正确无误。

   ![postback-management-template_en-us.png](https://files.readme.io/b5e41cad37859365c7818c4561620f8a78250c207d8326dae53ed9b522fe3716-360018213718.png)
8. 点击**保存**。请注意：保存回传配置后，新配置会立刻生效。

如果出现任何问题，请通过<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系我们。

</Accordion>

<div id="additional-information" />

## 其他相关信息

<div id="ap-for-analytics-partners" />

<Accordion title="数据分析平台的AP说明">

发送到分析平台的回传分以下两种情况：

* AP关闭时：回传用户级别数据，无限制。
* AP开启时：回传类型取决于用户来源和ATT授权状态，具体请见下表：

<div id="analytics-partner-postback-type-according-to-att-status-and-user-source" />

#### 分ATT授权状态和用户来源的数据分析平台回传类型

<table><thead><tr><th rowspan="2"><p>用户来源</p></th><th colspan="2">ATT状态</th><th rowspan="2">向数据分析平台发送的回传类型</th></tr><tr><th><p>流量侧应用（Publisher App）</p></th><th><p> 广告主 App</p></th></tr></thead><tbody><tr><td rowspan="3"><p><span>非自然</span></p><br/><p><span> </span></p><br/><p><span> </span></p></td><td><p><span>已授权</span></p></td><td><p><span>已授权</span></p></td><td>常规</td></tr><tr><td><p><span>Not authorized（拒绝授权）</span></p></td><td><p><span>已授权</span></p></td><td><p>无</p></td></tr><tr><td><p><span>任何值</span></p></td><td><p>Not authorized（拒绝授权）</p></td><td>无</td></tr><tr><td><p><span>自然量或网页</span></p></td><td>不适用</td><td><p>已授权</p></td><td>常规</td></tr><tr><td><p><span>自然量或网页</span></p></td><td><p><span>不适用</span></p></td><td><p>Not authorized（拒绝授权）</p></td><td>无</td></tr></tbody></table>

</Accordion>

<div id="ap-vs-skadnetwork" />

<Accordion title="SKAdNetwork">

<Anchor target="_blank" href="/partners/zh/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>是Apple针对iOS设备提供的一种归因技术。高级隐私保护是<Anchor target="_blank" href="/marketers/zh/docs/apply-aggregated-advanced-privacy-framework">AppsFlyer汇总层级高级隐私保护</Anchor>（AAP）框架的一部分，是针对AppsFlyer归因的解决方案。广告主可通过AAP框架在AppsFlyer后台调整用户级别归因数据的可用性。

</Accordion>

<div data-zendesk-anchors="h_01HJR7MWPM9XA4BXHDRD2K6D56=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E7%9A%84%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E9%80%82%E7%94%A8%E6%9D%A1%E4%BB%B6 ad-network-advanced-privacy-datasharing-principles=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%9C%A8%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4ap%E6%A8%A1%E5%BC%8F%E4%B8%8B%E7%9A%84%E6%95%B0%E6%8D%AE%E5%85%B1%E4%BA%AB%E5%8E%9F%E5%88%99 h_01HJR7MWPNYNMKZ3R8C3BB5EVG=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%9C%A8%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4ap%E6%A8%A1%E5%BC%8F%E4%B8%8B%E7%9A%84%E6%95%B0%E6%8D%AE%E5%85%B1%E4%BA%AB%E5%8E%9F%E5%88%99 types-of-templates-for-sending-postbacks=%E7%94%A8%E4%BA%8E%E5%8F%91%E9%80%81%E5%9B%9E%E4%BC%A0%E7%9A%84%E5%90%84%E7%B1%BB%E6%A8%A1%E7%89%88 h_01HJR7MWPN92BDJRK734P6YXSK=%E7%94%A8%E4%BA%8E%E5%8F%91%E9%80%81%E5%9B%9E%E4%BC%A0%E7%9A%84%E5%90%84%E7%B1%BB%E6%A8%A1%E7%89%88 h_01HJR7MWPN71TP0KWVVBHPC0H2=%E6%B3%A8%E6%84%8F type-of-postback-used=%E4%BD%BF%E7%94%A8%E7%9A%84%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B h_01HJR7MWPNJEDNDT1ZY7P78HMG=%E4%BD%BF%E7%94%A8%E7%9A%84%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B postback-type-for-ios-145=%E9%80%82%E7%94%A8%E4%BA%8Eios-145%E7%9A%84%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B h_01HJR7MWPNESP8BDC4D6Y7SBFZ=%E9%80%82%E7%94%A8%E4%BA%8Eios-145%E7%9A%84%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B web-campaigns=%E7%BD%91%E9%A1%B5%E5%B9%BF%E5%91%8A h_01HJR7MWPNXHHCSQ6BGCNRBHZK=%E7%BD%91%E9%A1%B5%E5%B9%BF%E5%91%8A postback-type-used-for-ios-145-when-ap-is-on=ap%E5%BC%80%E5%90%AF%E6%97%B6%E9%80%82%E7%94%A8%E4%BA%8Eios-145%E7%9A%84%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B h_01HJR7MWPNQCCNGHQY5RQHQ6D1=ap%E5%BC%80%E5%90%AF%E6%97%B6%E9%80%82%E7%94%A8%E4%BA%8Eios-145%E7%9A%84%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B integration=%E5%AF%B9%E6%8E%A5 h_01HJR7MWPP7YGRXJQR29F3ERHH=%E5%AF%B9%E6%8E%A5 h_01HJR7MWPPAXK18KER56E30G8R=click-url-requirements h_01HJR7MWPPRN8XYVSS7HX7NQB9=%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9 parameters-for-advanced-privacy-attribution=%E9%80%82%E7%94%A8%E4%BA%8E%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%BD%92%E5%9B%A0%E7%9A%84%E5%8F%82%E6%95%B0 h_01HJR7MWPPK2HET3XYW4WBFAZ1=%E9%80%82%E7%94%A8%E4%BA%8E%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%BD%92%E5%9B%A0%E7%9A%84%E5%8F%82%E6%95%B0 h_01HJR7MWPQ60F4CESKRRMTQ7HX=advanced-privacy-postback-specification h_01HJR7MWPQ8K06A1YM4KV4RTN8=%E9%87%8D%E8%A6%81%E6%8F%90%E7%A4%BA advanced-privacy-postback-endpoint-%5Bcomplete-as-required%5D=%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%9B%9E%E4%BC%A0%E7%AB%AF%E7%82%B9%E6%A0%B9%E6%8D%AE%E5%AE%9E%E9%99%85%E9%9C%80%E6%B1%82%E9%85%8D%E7%BD%AE h_01HJR7MWPQX9SXJZMBS6QR07WD=%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%9B%9E%E4%BC%A0%E7%AB%AF%E7%82%B9%E6%A0%B9%E6%8D%AE%E5%AE%9E%E9%99%85%E9%9C%80%E6%B1%82%E9%85%8D%E7%BD%AE advanced-privacy-attribution-macros-available=%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%BD%92%E5%9B%A0%E5%8F%AF%E7%94%A8%E5%8F%82%E6%95%B0 h_01HJR7MWPQKH52XMD6H9TJ0SM3=%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%BD%92%E5%9B%A0%E5%8F%AF%E7%94%A8%E5%8F%82%E6%95%B0 h_01HJR7MWPRC44K908A4EAPN9GV=setting-up-your-advanced-privacy-postback additional-information=%E5%85%B6%E4%BB%96%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF h_01HJR7MWPRVFR6YN56Y0DGBAXH=%E5%85%B6%E4%BB%96%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF h_01HJR7MWPR6ACNYVZHK7YPHQGP=ap-for-analytics-partners analytics-partner-postback-type-according-to-att-status-and-user-source=%E5%88%86att%E6%8E%88%E6%9D%83%E7%8A%B6%E6%80%81%E5%92%8C%E7%94%A8%E6%88%B7%E6%9D%A5%E6%BA%90%E7%9A%84%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B9%B3%E5%8F%B0%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B h_01HJR7MWPRZDJNSZNB981WB5Z1=%E5%88%86att%E6%8E%88%E6%9D%83%E7%8A%B6%E6%80%81%E5%92%8C%E7%94%A8%E6%88%B7%E6%9D%A5%E6%BA%90%E7%9A%84%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B9%B3%E5%8F%B0%E5%9B%9E%E4%BC%A0%E7%B1%BB%E5%9E%8B h_01HJR7MWPR3YR7E9S49P9ZZ3CT=ap-vs-skadnetwork" />
