---
title: 广告平台的InCost API
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Marketers
    - ROI360
    - Ad Networks
  created_at: '2020-04-26T19:13:47Z'
  edited_at: '2026-10-14T10:11:59Z'
  id: 360007714957
  locale: zh-cn
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/zh-cn/articles/360007714957
---
> **概要：** InCost API是AppsFlyer ROI360的一部分，能让广告平台通过程序化的方式向AppsFlyer发送广告成本数据，从而为广告主提供汇总成本信息，让其了解贵平台真正的投放价值。

<div id="about-incost-api" />

## InCost API简介

InCost API是广告平台向AppsFlyer发送成本数据的最佳解决方案。与广告主合作的广告平台可通过此API向AppsFlyer发送详细的广告投放成本数据。AppsFlyer取得该数据后会对其进行处理，并通过面板和报告向广告主和平台呈现相关信息。

<div id="benefits" />

#### 优势

* 通过流畅的成本数据上报让您的广告主了解贵平台真正的投放价值。如果缺少成本数据，您的广告主就失去了衡量投放效果的关键信息，无法准确地掌握ROAS，导致广告主将预算盲目投入其他渠道，最终影响到贵平台的效益。
* 使用该API可保障成本数据衡量的准确性、完整性和实时性，更有效地展示贵平台的ROI。
* InCost API部署简单快捷，效果立竿见影，并能让您完全把控数据发送的方式和节点，且支持前90天内的成本数据发送。
* InCost API支持所有的广告定价模式，不仅仅局限于CPI（若通过点击发送成本，则仅支持CPI）。
* 完成InCost API对接后贵平台在AppsFlyer Partner Marketplace中会获得一个“成本”徽章，表示支持成本数据。

<div id="note" />

<div id="implementing-incost-api" />

## InCost API的部署方式

**前期准备**：如需使用InCost API，贵平台需符合以下条件：

* 90%的广告系列在归因链接中包含广告系列ID（Campaign ID）。
* 每天可发送数据至少6次，以提高数据时效性。具体的发送时间由贵平台决定。
* 【如果广告平台对数据进行回滚更新】每次可发送最近7天的数据，以提高数据的完整性。

**请按以下方式部署InCost API并向AppsFlyer发送成本数据：**

* 请按下表所列的步骤操作。

| 步骤 | 操作 |
| --- | --- |
| 1 | 申请使用InCost：<ol><li>进入AppsFlyer后台，在页面顶部的菜单中选择**帮助** > **联系我们**。<br />界面会打开渠道支持微件。</li><li>选择**启用成本衡量**，并提交相关信息。<br />提交完毕后，系统会创建工单，并且会有AppsFlyer渠道解决方案工程师与您联系。</li></ol> |
| 2 | 确保至少90%的流量在其归因链接中包含广告层级信息，这些信息包括广告系列ID（必须配置）以及广告组ID和广告ID（可选）。 |
| 3 | 从AppsFlyer面板中获取AppsFlyer API token。 |
| 4 | 将API token发送给您的开发人员，在API认证头（authorization header）中使用，并让其按照<Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-overview">相关说明</Anchor>部署以下3个API方法：<ol><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get">Get app list</Anchor>。</li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-uploader-post">InCost upload</Anchor>： 告知开发人员用于填充JSON文件的字段：<ul><li>必须发送的字段一定要填充，也就是说这些字段不能发送空值。</li><li>媒体渠道仅限关联到贵平台账户（即在平台账户下注册）的渠道。请让您的渠道拓展负责人向您提供相关渠道列表。</li><li>请注意相关应用的<Anchor target="_blank" href="/marketers/zh/docs/about-data-freshness-and-timezone-support#app-specific-time-zone">时区</Anchor>设置（通过Get app permission list API上报），确保成本数据的日期与应用时区相符。</li><li>请勿上传不包含在成本数据中的广告层级字段，如广告组ID、素材资产名称、广告ID、广告名称等。</li></ul></li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-jobstatus-get">Get job status</Anchor>。</li></ol> |
| 5 | 测试对接<ol><li>在工单线程（来自第1步）中，通知AppsFlyer API实现已完成，并获取以下应用的权限，这些应用可以在不使用真实数据的情况下测试API：<ul><li>com.cost.app</li><li>id888123456</li></ul></li><li>在AppsFlyer中，从侧边菜单中选择 **协作** > **合作伙伴市场**，然后选择合作伙伴。</li><li>点击**设置对接**，</li><li>选择1个测试应用。</li><li>打开相关渠道对接页面中的**成本**选项卡。</li><li>打开**获取成本数据**的开关。</li><li>点击**保存成本**。</li><li>点击**测试连接**。<br />完成上述操作后，API即处于启用状态。</li></ol> |
| 6 | 在工单线程（来自第1步）中，确认与AppsFlyer的集成已正常运行。 |
| 7 | 请确保您的广告主在AppsFlyer对接渠道页面的成本选项卡中打开了<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#cost-tab">获取成本数据</Anchor>的开关。打开该开关后广告主即可获取成本数据。 |

<div id="fields-for-incost-upload-json" />

### JSON格式的InCost Upload字段

<table><thead><tr><th>字段</th><th>是否必须发送</th><th>说明</th></tr></thead><tbody><tr><td>date</td><td><span>是</span></td><td><ul><li><span>产生消耗的日期</span></li><li> <span>格式：</span><code><span>YYYY-MM-DD</span></code> </li><li> <span>比如 </span> </li></ul></td></tr><tr><td>app_id</td><td>是</td><td><ul><li>AppsFlyer后台显示的应用ID</li><li><span>格式：字符串，最多可包含250个字符</span></li><li> <span>比如 安卓 + iOS </span> </li></ul></td></tr><tr><td><span>media_source</span></td><td><span>是</span></td><td><ul><li><span>在AppsFlyer中关联到您广告平台账户的平台名称（ID）</span></li><li><span>格式：50个字符的字符串</span></li><li> <span>比如 </span> </li></ul></td></tr><tr><td><span>af_prt</span></td><td><span>否\*</span></td><td><ul><li><span>如需衡量代理流量和成本，必须填充该字段。</span></li><li><span>归因链接中的代理名称，也是AppsFlyer中关联到该代理账户的名称。</span></li><li><span>格式：50个字符的字符串</span></li><li> <span>比如 </span> </li></ul></td></tr><tr><td><span>campaign_id</span></td><td><span>是</span></td><td><ul><li> <span>必须与归因链接中传递的</span><code><span>af_c_id</span></code><span><span>参数值完全一致 </span></span> </li><li><span>字符串不能为空</span></li><li><span>格式：24个字符的字符串</span></li><li> <span>比如 </span> </li></ul></td></tr><tr><td><span>campaign_name</span></td><td><span>是</span></td><td><ul><li><span>格式：100个字符的字符串</span></li><li> <span>示例：</span><code><span>my_campaign123</span></code> </li></ul></td></tr><tr><td><span>adset_id</span></td><td>否\*</td><td><ul><li> 如果发送<span><code><span>adset_name</span></code></span>，则必须填充该字段 </li><li> <span>必须与归因链接中传递的</span><code><span>af_adset_id</span></code><span><span>参数值完全一致 </span></span> </li><li> <span>如果您贵平台上报的成本中不支持<code><span>adset_id</span></code>，切勿发送该字段</span> </li><li><span>格式：24个字符的字符串</span></li><li> <span>比如 </span> </li></ul></td></tr><tr><td><span>adset_name</span></td><td><span>否</span></td><td><ul><li> <span>若发送此字段，还必须一并发送<code><span>adset_id</span></code></span> </li><li><span>格式：100个字符的字符串</span></li><li> <span>比如 </span> </li></ul></td></tr><tr><td><span>ad_id</span></td><td>否\*</td><td><ul><li>如果发送<code><span>ad_name</span></code><span>，则必须填充该字段</span> </li><li> <span>必须与归因链接中传递的<code><span>af_ad_id</span></code>参数值完全一致</span> </li><li> <span>如果您贵平台上报的成本中不支持<code><span>adset_id</span></code>，切勿发送该字段</span> </li><li><span>格式：24个字符的字符串</span></li><li>示例：<code>123AB</code> </li></ul></td></tr><tr><td><span>site_id</span></td><td>否</td><td><ul><li>用于标记广告发行商（展示广告的媒体）的唯一ID。</li><li>格式：24个字符的字符串。</li></ul></td></tr><tr><td><span>ad_name</span></td><td><span>否</span></td><td><ul><li> <span>若发送此字段，还必须一并发送<code><span>ad_id</span></code></span> </li><li><span>格式：100个字符的字符串</span></li><li>示例：<code>Ad-name</code> </li></ul></td></tr><tr><td><span>geo</span></td><td><span>否</span></td><td><ul><li><span>贵平台记录到的收入所关联的国家</span></li><li><span>应尽可能填充展示广告的国家</span></li><li><span>格式： 符合ISO 3166标准的2字符国家/地区代码</span></li><li> <span>比如 </span> </li></ul></td></tr><tr><td>currency</td><td><span>是</span></td><td><ul><li><span>广告消耗的币种</span></li><li><span>格式： 符合ISO 4217标准的3字符货币代码</span></li><li> <span>比如 </span> </li></ul></td></tr><tr><td>spend</td><td>是</td><td><ul><li>以指定币种为单位的消耗金额 </li><li>最多可精确到小数点后五位</li><li>可填充零值（0）</li><li>不可填充负值</li><li> <code>,</code>切勿发送分隔符“”,</li><li>切勿使用引号发送值。 </li><li>格式：十进制数</li><li>示例值：<code>1</code>、<code>1.2</code>、<code>1234.20</code> </li></ul></td></tr><tr><td>channel</td><td>否</td><td><ul><li> <code><span>af_channel</span></code>必须与归因链接中传递的<span>参数值完全一致</span> </li><li>格式：20个字符的字符串 </li><li>示例：<code>my_channel</code> </li></ul></td></tr><tr><td>keywords</td><td>否</td><td><ul><li>格式：100个字符的字符串</li><li>示例：<code>abc app</code> </li></ul></td></tr><tr><td colspan="3">\* 部分情况下必须发送此字段，详情请见说明栏。</td></tr></tbody></table>

<div data-zendesk-anchors="incost-api=incost-api%E7%AE%80%E4%BB%8B h_01HE0WCBD9GD66KB1QGQ9MEXBJ=incost-api%E7%AE%80%E4%BB%8B benefits=%E4%BC%98%E5%8A%BF h_01HKVW85AYFG91PGYE5BDQVJNR=%E4%BC%98%E5%8A%BF implementing-incost-api=incost-api%E7%9A%84%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F h_01HKVWSWTWETTES5ZTNZ05X9VA=incost-api%E7%9A%84%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F fields-for-incost-upload-json=json%E6%A0%BC%E5%BC%8F%E7%9A%84incost-upload%E5%AD%97%E6%AE%B5 h_01HM8VCV81GQ6XQ4NA1EDCZ4K7=json%E6%A0%BC%E5%BC%8F%E7%9A%84incost-upload%E5%AD%97%E6%AE%B5" />
