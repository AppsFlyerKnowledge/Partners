---
title: 对接渠道的Protect360指南
metadata:
  keywords:
    - Protect360
    - Ad Networks
    - Partners
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2017-09-19T08:27:29Z'
  edited_at: '2026-10-14T10:09:12Z'
  id: 115004745523
  locale: zh-cn
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/zh-cn/articles/115004745523
---
> **概要：** 对接渠道（包括广告平台和代理）可以查看与其流量相关的假量数据。这些数据包括由ProtectLITE及Protect360引擎识别并拦截的假量，以及根据广告主自定义的验证规则拦截的流量。

<div id="overview" />

## 速览

AppsFlyer通过以下方式识别并拦截假量：

* <Anchor target="_blank" href="/marketers/zh/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">ProtectLITE</Anchor>：向所有客户开放的基础防作弊产品。
* <Anchor target="_blank" href="/marketers/zh/docs/protect360-anti-fraud-guide">Protect360</Anchor>：向订购了高阶套餐的广告主提供的高级防作弊产品。

广告主必须开放以下权限：

* 向广告平台开放**Protect360面板和原始数据**（其中包含ProtectLITE）以及**应用内事件汇总数据**（用于应用内事件假量）的<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#permissions-tab">访问权限</Anchor>。
* 向代理开放**Protect360面板和原始数据的**<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#permissions-tab">访问权限</Anchor>。

获取必要权限后，对接渠道就可以进行以下操作：

* 查看与该平台产生的流量相关的数据。
* 下载相关的<Anchor target="_blank" href="/marketers/zh/docs/protect360-anti-fraud-guide#raw-data">原始数据报告</Anchor>。

此外，广告平台还可以获取点击和展示截断（capping）的原始数据以及验证失败的点击签名<Anchor target="_blank" href="/partners/zh/docs/protect360-reports-for-ad-networks">原始数据</Anchor>。广告平台在访问这类报告时不需要广告主开放权限。

<div id="note" />

> 📘 **注意**
>
> 如果广告主通过代理商在广告平台上进行投放，并且需要让广告平台和代理商都能取数，那么广告主必须在AF中同时对接代理商和广告平台，并为他们开通数据权限。
>
> 如果仅接入了代理商并为其开通了权限，这时广告平台没有数据权限。

<div id="dashboard-view" />

### 面板视图

**前期准备**：让广告主为您开放ProtectLITE和Protect360的访问权限。

对接渠道可以查看面板和图表，详见下图截屏。

如需进一步了解<Anchor target="_blank" href="/marketers/zh/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting#dashboard">ProtectLITE</Anchor>和<Anchor target="_blank" href="/marketers/zh/docs/protect360-anti-fraud-guide#dashboard">Protect360</Anchor>面板中的可用数据，请查看链接所对应的文档。

局限性：

* 广告平台无法访问异常数据面板。代理可以访问此面板，但仅当AppsFlyer认证的低作弊率渠道产生流量时才会看到数据，作为可供参考的基准水平，用于对比其他媒体渠道的表现。

[![p360_dashboard_1.jpg](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)

<div id="raw-data-reports" />

### 原始数据报告

**前期准备**：让广告主为您开放ProtectLITE和Protect360的访问权限。

您可以使用Protect360原始数据报告查看通过ProtectLITE、Protect360和验证规则识别并拦截的假量。

该报告的获取方式如下：

* 导出数据：在AppsFlyer后台左侧的菜单栏中选择**导出** > **原始数据导出**。
* API：详见下文[广告平台数据上报API](/docs/protect360-for-integrated-partners#protect360的广告平台数据上报api)部分的说明。

如需进一步了解Protect360原始数据报告，请参考<Anchor target="_blank" href="/marketers/zh/docs/protect360-raw-data-reports">此文档</Anchor>。

<div id="protect360-ad-network-reporting-api" />

## Protect360的广告平台数据上报API

* 广告平台可以通过API拉取本节所列的原始数据报告。
* 面板的数据导出页中也提供相同的报告。
* 如果广告主未购买Protect360套餐，AppsFlyer只提供激活假量报告。

**前期准备**

* 广告平台如需通过API访问广告主侧数据，必须让广告主为其开放Protect360面板和数据的API访问<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#permissions-tab">权限</Anchor>。具有面板权限的广告平台可直接使用API，无需广告主进行任何操作。
* 如果您不知道自己可以访问哪些应用的Protect360数据，请使用<Anchor target="_blank" href="/partners/zh/docs/app-list-api-for-ad-networks">get app list API</Anchor>获取相关的应用列表。
* 账户管理员需要在面板中获取一个<Anchor target="_blank" href="/marketers/zh/docs/managing-appsflyer-tokens">2.0版本的AppsFlyer认证token</Anchor>。

<div id="protect360-api-reports" />

#### 可通过API拉取的Protect360报告

| 报告 | 数据时效性 | 说明 |
| --- | --- | --- |
| 归因后判定为假量的应用内事件 | 每天UTC时间10:00更新 | <ul><li>被识别为假量的激活所产生的应用内事件。</li><li>其他与激活假量无关但被识别为假量的应用内事件。</li></ul>您也可以使用下文参数列表中的应用内事件类型来筛选出该报告的数据。<br /><br />报告主题：`fraud-post-inapps` |
| 归因后判定为假量的激活 | 每天UTC时间10:00更新 | <ul><li>归因后被判定为假量的激活。</li><li>您也可以使用下一节所述的检测日期来筛选出该报告的数据。</li></ul>报告主题：detection |
| 激活假量 | 实时 | 已拦截的安装（包含拦截原因）<br /><br />报告主题：blocked\_installs\_report |
| 应用内事件 | 实时 | 已拦截的用户所完成的应用内事件<br /><br />报告主题：`blocked_in-app_events_report` |
| 点击 | 实时 | 已拦截的用户所完成的归因点击<br /><br />报告主题：`blocked_clicks_report` |

<div id="procedure-for-ad-networks-to-get-protect360-reports-by-download" />

#### **广告平台通过下载获取Protect360报告的方法**

**使用API获取报告的方式如下：**

1. 使用上文列表，找出您所需的报告。
2. 使用相关的curl示例（见下节说明），编写您的脚本。
3. 请务必在脚本中替换掉下列占位符：
   1. 应用ID
   2. 起始日期
   3. 截止日期
   4. Bearer token（<Anchor target="_blank" href="/marketers/zh/docs/managing-appsflyer-tokens">2.0版本的AppsFlyer认证token</Anchor>）
4. 部分调用请求支持[可选参数](/docs/protect360-for-integrated-partners#api-parameters)，详见本文相关小节的说明。

<div id="curl-examples" />

### Curl示例

<div id="installs-blocked_installs_report" />

<Accordion title="激活假量（blocked_installs_report）">

替换掉app\_id、from、to和token的占位符。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_installs_report/app/{app_id}?from={2020-07-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-installs-detection" />

<Accordion title="归因后被判定为假量的激活（检测）">

替换掉app\_id、from、to和token的占位符。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/detection/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additonal-fields=fraud_reason,fraud_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="inapp-event-blocked_in_app_events_report" />

<Accordion title="应用内事件假量（blocked_in_app_events_report）">

替换掉app\_id、from、to和token的占位符。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_in_app_events_report/app/?from=YYYY-MM-DD&to=YYYY-MM-DD&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-inapp-events-fraud-fraud_post_inapps" />

<Accordion title="归因后被判定为假量的应用内事件（fraud_post_inapps）">

替换掉app\_id、from、to和token的占位符。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/fraud-post-inapps/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,fraud_reason,fraud_sub_reason,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="clicks-blockedclicks_report" />

<Accordion title="已拦截的点击（blocked-clicks_report）">

替换掉app\_id、from、to和token的占位符。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_clicks_report/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="protect360-ad-network-api-reference-guide" />

### Protect360中的广告平台API参考信息

<div id="api-basics" />

<Accordion title="API基础信息">

Protect360中的广告平台API基础信息：

| 路径 | `https://hq1.appsflyer.com/api/adnets-data/v1/export/report_topic/app/app_id` |
| --- | --- |
| 方法 | GET |
| 路径参数（必须配置） | <ul><li>`app_id`：<ul><li>即AppsFlyer面板中的应用标识符。请完全按照面板上显示的方式填入。</li><li>对于iOS应用，请确保标识符中包含前缀**id**。</li></ul></li><li>**`report_topic`：**</li></ul> |
| 可用格式 | `application/json` |
| 授权 | <ul><li>Request Header（请求头）中的Bearer Token</li><li>![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png)让账户管理员从<Anchor target="_blank" href="/marketers/zh/docs/managing-appsflyer-tokens">token</Anchor>页面中获取V2.0 token。该token的长度约为700个字符。</li></ul> |
| 拉取频次限制 | <Anchor target="_blank" href="/marketers/zh/docs/report-generation-quotas-rate-limitations">详见拉取频次限制说明</Anchor> |
| 日期范围限制 | <ul><li>可查询范围内最早的日期：当前日期之前的90天</li><li>最长可查询前90天内31日的数据</li></ul> |
| 行数限制 | 20万行 |
| 报告特征： | <ul><li>时区UTC</li><li>货币：USD</li></ul> |

</Accordion>

<div id="api-parameters" />

<Accordion title="API参数">

Protect360 API参数：

| 参数 | 说明 | 格式 | 是否必须发送 |
| --- | --- | --- | --- |
| app\_id | AppsFlyer中显示的应用ID | 字符串 | 是 |
| from | 日期范围起始时间：<ul><li>在激活记录中指激活日期。</li><li>在应用内事件记录中指事件发生日期。</li></ul> | YYYY-MM-DD | 是 |
| to | 日期范围结束时间：<ul><li>在激活记录中指激活日期。</li><li>在应用内事件记录中指事件发生日期。</li></ul> | YYYY-MM-DD | 是 |
| event\_name | 【可选】适用于归因后识别的应用内事件假量<br /><br />按应用内事件筛选数据，让报告仅呈现特定的事件，其中可包含一个或多个事件。<br /><br />示例：`&event_name=af_purchase,af_login` | 字符串 | 否 |
| detect-from | 【查询归因后判定为假量的激活件时，起始检测日期为可选参数】<br /><br />假量检测日期范围的起始时间。日期范围的 | YYYY-MM-DD | 否 |
| detect-to | 【可选】适用于归因后识别的激活假量<br /><br />假量检测日期范围的结束时间（默认为<u>to</u>）。 | YYYY-MM-DD | 否 |

</Accordion>

<div id="protect360-api-http-return-codes" />

<Accordion title="Protect360 API返回的HTTP状态码">

可能出现的错误码及其对应的解决方案：

| 状态码 | 响应代码 | 问题表现/报错消息 | 解决方法 |
| --- | --- | --- | --- |
| OK | 200 | CSV文件为空 | 在URI中多次使用`addtional_fields` |
| OK | 200 | CSV文件为空 | 请确保“from”和“to”的日期都是yyyy-mm-dd格式 |
| OK | 200 | 返回AppsFlyer的HTML登录页面 | Bearer token请求头中缺失token |
| Bad request（请求无效） | 400 | Bad request（请求无效） | <ul><li>日期范围限制。<ul><li>可查询范围内的最早日期为当天之前的90天。</li><li>查询激活假量时日期范围不可超过60天；查询应用内事件假量时日期范围不可超过90天</li></ul></li></ul> |
| Unauthorized（未授权） | 401 | Unauthorized（未授权） | 发现了token，但token无效。检查您使用的token是否为您账户下现行的2.0版token。让您的账户管理员从面板中获取现行token。 |
| Not found（未找到） | 404 |  | <ul><li>指定的端点不正确。</li><li>请确保您使用的应用ID正确无误。</li><li>您未经授权，无法访问该应用</li></ul> |

</Accordion>

<div id="impression-capping" />

## 展示和点击截断（capping）

如果某个广告平台的展示或点击作弊率非常高，Protect360会在24小时的周期内拦截该平台的展示或点击。也就是说，广告平台一旦触达capping阈值后，AppsFlyer就不会再记录任何展示/点击，也不会对其进行归因。被拦截的展示/点击会出现在Protect360的面板或报告中。

AppsFlyer的防作弊算法在检测假量时会考察多种参数，包括展示/点击量、CVR，检测到的作弊率、用户行为的正常浮动、行业及国家/地区基准水平，以及AF专有参数。由于业界形势复杂多变，因此我们使用每小时更新一次的动态算法，以全面涵盖最新趋势。

**反复触发展示或点击截断（capping）的阈值可能会导致AppsFlyer平台永久性清除相关的渠道对接。**

展示或点击capping的阈值： 

* 对所有广告平台一致生效。也就是说，任何平台一旦出现极高的展示或点击作弊率，都会触发截断，无一例外。
* capping在应用/广告平台层级生效。也就是说，作弊分析算法会考察某个应用在某个广告平台上投放的所有广告系列，而且AF的拦截机制会影响该应用在该平台中投放的所有广告系列的数据上报和归因（无论该应用的AF账户是否购买了Protect360）。
* capping阈值会在24小时的周期过后重置。在capping周期结束前，拦截处理会持续生效。AppsFlyer不公布周期开始和结束的具体时间。
* Capping阈值无法更改，触发后无法停止拦截。我们对Protect360的作弊检测功能进行了精密的调试，确保能产出准确的检测结果。该产品的算法不能进行手动调整或停用。
* 避免capping的方式：停止投放数据异常的广告系列和子渠道。

<div id="faq" />

<Accordion title="常见问题解答">

与展示和点击截断（capping）相关的常见问题解答：

| **问：广告平台的capping阈值是多少？**<br /><br />**答**：为了防止规避行为，AppsFlyer不公开点击capping机制的详情。但触发该阈值所需的展示/点击量是极其庞大的，仅在数量超过人类行为极限时才会启动capping。您可以查看当天的展示、点击和激活数量，更清晰地了解子渠道是否有撞库问题。 |
| --- |
| **问：如何解除capping引起的流量拦截？**<br /><br />**答**：如需避免触发阈值，建议广告平台停止投放数据异常的广告系列和子渠道。capping一旦启动，相关平台需要等24小时的拦截周期结束，然后AppsFlyer才会重新开始记录其产生的点击。 |
| **问：未购买Protect360的广告主也会受到capping机制的影响吗？**<br /><br />**答**：是的，无论广告主是否购买了Protect360，capping机制都会保护其免受点击/展示作弊的侵害。 |
| **问：广告平台会与廉价渠道合作，这些渠道的质量可能不高，但不是作弊渠道。**<br /><br />**答**：非可疑渠道在正常流量水平下投放效果较差不会触发点击capping。capping算法判定为异常的数据仅限超出人类行为可能性的极端值。 |
| **问：这个机制使我们无法全面铺开投放，我们不希望AF拦截这些展示/点击。**<br /><br />**答**：AppsFlyer的防作弊算法旨在阻断极为明显的撞库风险，保护广告主的利益。该机制仅针对非人类产生的展示/点击进行拦截，此类数据的绝大部分有百害而无一利，因此capping不会影响到广告主的增投能力。 如果您有任何疑问，请联系AppsFlyer，我们会为您解答相关问题。 |
| **问：将这些流量判定为假量是否因为AppsFlyer无法处理较庞大的展示/点击量？**<br /><br />**答**：我们在数据处理的体量方面没有任何问题。我们每天为全球体量最大的广告主实时处理数十亿数据点，其中包括数量庞大的正常点击。我们致力于通过丰富且准确的数据帮助广告主实现高量级增长，以客户的利益为出发点，为他们阻断较为明显的点击撞库风险。 |
| **问：为什么要在激活假量拦截之外还增加点击capping？**<br /><br />**答：AppsFlyer持续为客户增长保驾护航，因此会不断改进我们的防作弊机制。此前，我们仅拦截激活，放行展示/点击。但如果出现超出人类行为极限的极高点击率，就没有必要再将这类点击纳入我们的系统。** |
| **问：如果我们已经预先知道展示/点击量会出现激增（比如新近投放广告之后），如何避免流量被屏蔽呢？**<br /><br />答<strong>：由于业界形势复杂多变，因此我们使用每小时更新一次的动态算法，以全面涵盖不同的数据趋势。该算法的精密度极高，可以识别出正常投放行为造成的流量激增（短期内大幅增长），这种情况下不会触发capping。</strong>当然，广告平台也可以使用其展示/点击数据和报告来判断可疑的流量来源，并相应地停投有关广告。 |
| **问：如何检查有问题的流量并优化投放效果？**<br /><br />答<strong>：广告平台可以使用其展示/点击数据和报告来判断可疑的流量来源，并相应地停投有关广告。广告主为其合作渠道开放相关权限，允许其在面板中查看假量数据后，渠道也可以在Protect360/ProtectLITE面板的专用栏位中看到被拦截的展示和点击数据。</strong> |
| **问：广告平台是否会收到capping的通知邮件？**<br /><br />答<strong>：对于点击capping，AppsFlyer会在广告平台达到capping阈值时向其发送邮件通知。</strong> |

</Accordion>

<div id="click-signing" />

### 点击签名

广告平台可以<Anchor target="_blank" href="/partners/zh/docs/click-signing-for-ad-networks">为其点击添加HMAC-SHA256签名</Anchor>。

AppsFlyer可以通过这类签名验证点击，并确保点击信息不被作弊分子篡改。

* 经过验证的点击会被记录到AppsFlyer，并归因到相关的广告平台。
* 未通过验证的点击会被拦截，并且：
  * 会被汇总到Protect360报告中，提供给广告平台（而非广告主）。
  * 不会影响该广告平台的转化率或点击capping阈值。

<div data-zendesk-anchors="overview=%E9%80%9F%E8%A7%88 h_01HGSXTKYQB4Q1QQX4ZQS60AAJ=%E9%80%9F%E8%A7%88 h_01HGSXTKYQN42EEMPSZMWVAMWD=%E6%B3%A8%E6%84%8F dashboard-view=%E9%9D%A2%E6%9D%BF%E8%A7%86%E5%9B%BE h_01HGSXTKYQPQP72R2VJB68ZDRZ=%E9%9D%A2%E6%9D%BF%E8%A7%86%E5%9B%BE rawdata-reports=%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E6%8A%A5%E5%91%8A h_01HGSXTKYQWRZECN905RGSEQ42=%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E6%8A%A5%E5%91%8A protect360-ad-network-reporting-api=protect360%E7%9A%84%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E6%95%B0%E6%8D%AE%E4%B8%8A%E6%8A%A5api h_01HGSXTKYQ9388SCQTT2MX59Q9=protect360%E7%9A%84%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E6%95%B0%E6%8D%AE%E4%B8%8A%E6%8A%A5api protect360-api-reports=%E5%8F%AF%E9%80%9A%E8%BF%87api%E6%8B%89%E5%8F%96%E7%9A%84protect360%E6%8A%A5%E5%91%8A h_01HGSXTKYQXZN2DMNZ09HE7355=%E5%8F%AF%E9%80%9A%E8%BF%87api%E6%8B%89%E5%8F%96%E7%9A%84protect360%E6%8A%A5%E5%91%8A procedure-for-ad-networks-to-get-protect360-reports-by-download=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E9%80%9A%E8%BF%87%E4%B8%8B%E8%BD%BD%E8%8E%B7%E5%8F%96protect360%E6%8A%A5%E5%91%8A%E7%9A%84%E6%96%B9%E6%B3%95 h_01HGSXTKYQ913MF0G38B23NYBG=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E9%80%9A%E8%BF%87%E4%B8%8B%E8%BD%BD%E8%8E%B7%E5%8F%96protect360%E6%8A%A5%E5%91%8A%E7%9A%84%E6%96%B9%E6%B3%95 curl-examples=curl%E7%A4%BA%E4%BE%8B h_01HGSXTKYQX3VN5NRMNQWW4AE4=curl%E7%A4%BA%E4%BE%8B h_01HGSXTKYQQBJTM4ZMMQZ0VZNH=installs-blocked_installs_report h_01HGSXTKYQ5KTCD7K63DSVS6E2=postattribution-installs-detection h_01HGSXTKYQ6MA96W8E6R2SXBS5=inapp-event-blocked_in_app_events_report h_01HGSXTKYQMMC0WNWP56Q9J0ZS=postattribution-inapp-events-fraud-fraud_post_inapps h_01HGSXTKYQEG0JXJHS7QBAEBCA=clicks-blockedclicks_report protect360-ad-network-api-reference-guide=protect360%E4%B8%AD%E7%9A%84%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0api%E5%8F%82%E8%80%83%E4%BF%A1%E6%81%AF h_01HGSXTKYQJRE1Y9C5RSCANWT2=protect360%E4%B8%AD%E7%9A%84%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0api%E5%8F%82%E8%80%83%E4%BF%A1%E6%81%AF h_01HGSXTKYQE24FAPYHHMFP0B3X=api-basics h_01HGSXTKYRFSZRPHNPDHNREDH2=api-parameters h_01HGSXTKYRGSQ230NVN06SP6DG=protect360-api-http-return-codes impression-and-click-capping=%E5%B1%95%E7%A4%BA%E5%92%8C%E7%82%B9%E5%87%BB%E6%88%AA%E6%96%ADcapping h_01HGSXTKYRN6TP3KDYX5YZJV7N=%E5%B1%95%E7%A4%BA%E5%92%8C%E7%82%B9%E5%87%BB%E6%88%AA%E6%96%ADcapping h_01HGSXTKYR8BK5A2J6TJECMKZA=faq click-signing=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D h_01HGSXTKYR915V6E4NWGWR61PG=%E7%82%B9%E5%87%BB%E7%AD%BE%E5%90%8D" />
