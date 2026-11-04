---
title: 代理账户详解
metadata:
  keywords:
    - In-App Events
    - Agency Account
    - ROI
    - Agency
    - FMP
    - Advertisers
    - Agencies
    - Listed Agency
    - all installs
    - all launches
    - Partners
    - agency sign up
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2013-12-08T10:02:42Z'
  edited_at: '2026-10-14T10:07:28Z'
  id: 207034106
  locale: zh-cn
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/zh-cn/articles/207034106
---
> **概要：** 本文解释了如何利用高级配置，充分发挥AppsFlyer代理账户的作用。

<div id="about-agency-accounts" />

## 代理账户详解

代理账户是专为代理团队设计的，用于衡量代理代广告主（应用所有者）投放的应用营销广告效果。

* 代理账户可以使用关键预装和预装指标，为广告主带来最佳的投放效果。
* 代理账户与广告主账户的面板功能及内容相似，两者都具备以下面板：
  * LTV数据总览面板
  * 应用内事件
  * 再营销
* 可用指标包括展示量、点击量、激活量、用户忠实度、广告成本、ROI等。详见<Anchor target="_blank" href="/marketers/zh/docs/getting-started-with-appsflyer-dashboards">AppsFlyer面板指南</Anchor>。

<div id="agency-access-to-marketer-data" />

### 代理对广告主数据的访问权限

对于归因到代理的流量，代理总是可以访问其相关数据。广告主也可以<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">向代理开放</Anchor>其他数据的权限，例如自然量汇总数据。详见<Anchor target="_blank" href="/marketers/zh/docs/manage-data-access-permissions">不同类型用户的数据访问权限</Anchor>。

<div id="agency-access-to-ad-network-integrations" />

### 代理对广告平台对接的访问权限

代理如需使用某个广告平台的对接，并对自己在该平台中代投的广告进行衡量，必须事先获得平台侧的认可。也就是说该平台的授权代理列表中必须包含该代理的ID（即af\_prt）。请联系您的合作渠道，沟通授权事宜。如需查找相关代理ID，请参考[这部分说明](/docs/about-agency-accounts#af_prt参数)。

<div id="note" />

> 📘 **注意**
>
> * 即使归因链接中的af\_prt参数为空，也同样需要符合上述要求。
> * 与<Anchor target="_blank" href="/marketers/zh/docs/self-reporting-networks-srns">SRN</Anchor>合作的代理不在此要求的适用范围之内。

<div id="agency-transparency" />

### 代理数据透明化

您的流量数据默认对广告主可见。<Anchor target="_blank" href="/partners/zh/docs/getting-started-agency-onboarding#代理数据透明化设置">详情请见此处说明。</Anchor>

<div id="comparing-different-types-of-accounts" />

## 对比不同类型的账户

<div id="agency-versus-marketer-accounts" />

<Accordion title="代理账户与广告主账户对比">

* **广告主帐户**是专为应用及数据持有者所设计的，广告主可以在其账户下添加应用并设置数据访问权限。
* **代理帐户**是专为代理团队设计的，其中的各种工具旨在帮助代理对各个客户的营销投放进行有效的衡量和分析。

这样的账户构架是为了推动跨国代理团队之间的信息交流，并打通团队层级的ROI衡量、计算、上报和优化。

<div id="differences-between-marketer-and-agency-accounts" />

#### 广告主帐户与代理帐户的差异：

|  | 营销人员 | **Agency（代理）** |
| --- | --- | --- |
| 代码层级设置 | 是 | 不涉及；代理仅负责仅推广应用 |
| 帐户层级设置 | 团队成员、团队成员权限、设置、指定付款方式 | 代理团队成员及其权限 |
| 应用层级设置 | 再归因窗口、OneLink配置、时区、货币 | 其他所有设置均取决于广告主侧的设置 |
| 合作伙伴配置 | <ul><li>代理权限</li><li>所有非SRN（即使用归因链接的广告平台）的配置</li><li>SRN配置</li><li>链接管理</li></ul> | <ul><li>所有非SRN的配置</li><li>下列SRN要求必须由广告主完成的配置很少：</li></ul><ul><li>Google Doubleclick<ul><li>Snapchat</li><li>腾讯</li></ul></li></ul>其他SRN必须由广告主配置后代理方可使用。<ul><li>链接管理（使用广告主定义的模板）</li></ul> |
| 其他功能 | 是（限套餐包含的产品） | 取决于广告主购买的套餐和授予代理的<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">权限</Anchor> （请参见下表） |

<div id="features-available-to-agencies" />

### 代理可用的功能

| 默认可用 | 不可用 | 需要广告主授权 |
| --- | --- | --- |
| <ul><li>LTV（生命周期价值）维度的数据总览面板</li><li>应用内事件控制面板</li><li>重定向控制面板</li><li>活跃渠道</li><li><Anchor target="_blank" href="/partners/zh/docs/getting-started-agency-onboarding#代理的单一可信数据源ssot权限">SSOT面板</Anchor>\*\*</li></ul>\*\* 需要广告主侧启用该选项后方可使用。 | <ul><li>活跃数据面板</li><li>自定义面板</li><li>基于用户的归因（PBA）</li><li>受众共享（Audiences）</li><li>数据透视表</li><li>Push API</li><li>Data Locker</li></ul>*仅群组报告需广告主授权后可用。 | <ul><li>留存报告</li><li>群组面板报告</li><li><Anchor target="_blank" href="/partners/zh/docs/data-locker-reports-for-agencies">Data Locker的群组报告</Anchor></li><li>Protect360</li><li>原始数据导出</li><li>自然量汇总数据</li><li>Pull API</li></ul> |

</Accordion>

<div id="agency-vs-ad-network-account" />

<Accordion title="代理帐户与广告平台帐户">

<div id="differences-between-ad-network-and-agency-accounts" />

#### 广告平台帐户与代理帐户的差异：

<table><thead><tr><th>广告平台</th><th>Agency（代理）</th></tr></thead><tbody><tr><td>归因链接中用于标识渠道的参数：<code>pid</code> </td><td>归因链接中用于标识渠道的参数：<code>af_prt</code> </td></tr><tr><td>将应用广告投放在自家平台上</td><td>通过多个媒体渠道推广应用</td></tr><tr><td>仅可查看自家平台上的广告带来的流量</td><td>仅可查看代理使用的媒体渠道所带来的流量</td></tr><tr><td>可以通过回传接收实时的激活和应用内事件信息</td><td>无法通过回传接收实时的激活和应用内事件信息</td></tr><tr><td>可以配置自带流量的所有应用内事件回传\*</td><td>可以配置某些带量渠道的应用内事件回传\*</td></tr><tr><td colspan="2">\*需要广告主授权</td></tr></tbody></table>

</Accordion>

<div id="agency-accountscampaigns-and-reporting" />

## 代理账户——广告投放及数据上报

<div id="agency-setting-up-campaigns" />

<Accordion title="代理：广告投放设置">

代理可以监测的流量类型主要分以下几种：

* * [自归因平台（SRN）](/docs/about-agency-accounts#自归因平台平台)
  * [非SRN（使用归因链接的广告平台）](/docs/about-agency-accounts#非srn)

<div id="self-reporting-ad-networks" />

### 自归因平台平台

自归因平台（如Meta ads、Google Ads或X Ads）不使用外部归因链接，而是提供各自专用的方法和API，让AppsFlyer获取新增激活、应用内事件等信息。

<div id="srn-configurations" />

#### SRN配置

| SRN | 需要广告主完成SRN的初始设置 | 说明 |
| --- | --- | --- |
| Apple Search Ads | 是 | 更多关于Apple Search Ads广告活动配置的详情，请点击<Anchor target="_blank" href="/marketers/zh/docs/apple-ads-integration-setup#如何配置代理商和营销合作伙伴">这里</Anchor>。 |
| Google Ads | 是 | 详情请见<Anchor target="_blank" href="/marketers/zh/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads广告的代理配置指南</Anchor>。 |
| Google Marketing Platform（GMP） | 否 | GMP有两个不同的API。请详细了解<Anchor target="_blank" href="/marketers/zh/docs/google-marketing-platform-display-video-360-dv360-integration#comparing-the-legacy-and-new-integrations">这两个API之间的差异</Anchor>，并选择更适合您的那个API。 |
| Meta ads  <br />和  <br />X Ads | 是 | **请注意：** 这部分内容仅针对Meta ads。如需了解Facebook Social（帖子）的归因，请参考[自有媒体说明](/docs/about-agency-accounts#owned-media%E2%80%94onelink-and-custom-links)。<br /><br />**所有Meta ads和X Ads的广告系列都必须以代理帐户的名称开头，后接" \_ " 。** 这里的名称指在AppsFlyer后台设定的账户名称。<br />未按上述要求命名的广告系列只对广告主可见，代理不可见。<br /><br />**请注意：**<ul><li>代理名称要注意区分大小写。</li><li>详情请见<Anchor target="_blank" href="/marketers/zh/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta ads</Anchor>和<Anchor target="_blank" href="/marketers/zh/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor>的代理设置指南。</li><li>如果您对此有任何疑问，请发送邮件至[agency@appsflyer.com](mailto:agency@appsflyer.com)。</li></ul>**示例**<br />代理agencyx在Meta ads上投放了一个名为agencyx\_brilliantcampaign的广告系列，agencyx就可以在面板上看到这个广告系列的相关数据。<br /><br />代理agencyz在X Ads上投放了一个名为AgencyZ\_whathaveidonewrong的广告系列，但未看到任何效果数据。这是因为该广告系列中的代理名称与后台设定的代理名称不一致（广告系列中的A和Z是大写，而后台设定的代理名称为小写）。 |
| Snapchat | 否 | 详情请见<Anchor target="_blank" href="/marketers/zh/docs/snapchat-advanced-srn-integration-setup">Snapchat广告的代理配置指南</Anchor>。 |
| TikTok for Business | 是 | 如需进一步了解代理的TikTok for Business投放配置方式，请参考<Anchor target="_blank" href="/marketers/zh/docs/tiktok-for-business-advanced-srn-integration-setup#代理的tiktok-for-business对接设置">此文档</Anchor>。 |
| Yahoo（Oath:Ad Platforms / Yahoo Gemini) | 是 | 详情请见<Anchor target="_blank" href="/marketers/zh/docs/yahoo-integration-setup#agency-configuration">Yahoo广告的代理配置指南</Anchor>。 |

<div id="non-srns" />

### 非SRN

与SRN不同，绝大多数广告平台使用归因链接进行归因。AppsFlyer后台的合作伙伴配置页中为各平台提供<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#attribution-link-tab">现成的归因链接</Anchor>，可以直接复制取用。

代理帐户的操作方式与广告主帐户基本一致，任何常规广告平台的设置页面都会提供现成的归因链接，唯一的区别在于代理账户的归因链接中会自动添加`af_prt`参数。

<div id="ad-network-configuration-visibility" />

#### 广告平台配置对代理的可见性

由广告主（应用所有者）配置广告平台对接时，相关平台才能看到这些设置。如果由代理激活并配置广告平台对接，则这部分设置对广告平台会显示为未启用。

<div id="af_prt-parameter" />

#### af\_prt参数

`af_prt`参数的值即表示代理的名称。代理名称在`af_prt`参数里总是会转换成小写格式。

如果归因链接中的`af_prt`参数填充了代理名称，那么新增激活就能被归因到您使用的代理账号。否则，这些激活会直接归因到相关的广告平台。

[![agency-af-prt.png](https://files.readme.io/61559e2e1628e9411665b7e8d3d3d440a55effb3bccda79c7fe1ee02fd43fb8c-32355631649937.png)](https://files.readme.io/61559e2e1628e9411665b7e8d3d3d440a55effb3bccda79c7fe1ee02fd43fb8c-32355631649937.png)

**请勿使用广告主侧的链接**：请务必使用您自己帐户中的链接，以防导致错误归因。

<div id="special-case-all-installs-and-all-launches-networks" />

#### 特殊情况：全安装和全启动广告平台

一些非自归因平台会要求（或允许）广告主向其**回传归因到其他渠道的设备信息**。

全量激活回传渠道

这类平台接收所有新增激活的回传，不限流量来源

全量应用开启回传平台

这类平台接收所有应用打开的回传，不限流量来源

全量激活回传渠道包括Vungle、Wechat、Startapp、Unity Ads等。

下表列出了所有的全量应用开启回传平台：

| 平台名称 | 平台PID（在AF归因链接中配置） |
| --- | --- |
| Supersonicads（前ironSource旗下平台） | supersonicads\_int |
| Adelphic Remarketing | adelphicremarketing\_int |
| Grow Mobile | growmobile\_int |
| ONE by AOL | advertising.com\_int |
| Lemmonet Mobile | lemmonetmobile\_int |
| Clickky | clickky\_int |
| Remerge | remerge\_int |
| MyThings | mythings\_int |
| TikTok for Business | bytedanceglobal\_int |

<div id="how-to-setup-agency-attribution-with-all-installslaunches-networks" />

#### 如何在全量激活/应用开启回传渠道上配置代理链接？

与这类平台合作时，需要向其发送所有激活的信息，即是这些激活不是由相关代理带来的。因此，这些平台会要求广告主在配置**代理**前先对他们进行配置。

<div id="example" />

> 📄 **示例**
>
> 让我们以Tapjoy为例介绍一下代理的归因设置：
>
> 1. 广告主侧的营销人员从其帐户面板进入Tapjoy的配置页面。
> 2. 该营销人员在**app\_id**字段中输入Tapjoy的App ID（由Tapjoy提供给该**营销人员**）。
> 3. 在**对接**选项卡中的默认回传部分，该营销人员选择了**所有媒体渠道，包括自然流量**。
> 4. 代理从其帐户的面板进入Tapjoy的配置页面
> 5. 代理在**app\_id**字段中输入Tapjoy的App ID（由Tapjoy提供给**代理**）

<div id="deep-linking" />

### 深度链接

深度链接是指用户点击个性化广告时吊起相关应用和/或让用户进入应用中的特定页面，从而为用户带来极佳的体验并提升用户与应用的互动。

如需使用深度链接，开发人员必须在应用代码中写入深度链接功能，否则深度链接无法正常生效。因此请在投放广告前先与广告主确认相关应用是否能支持深度链接。

<div id="retargeting" />

### 再营销

* * <Anchor target="_blank" href="/marketers/zh/docs/retargeting-attribution-guide">再营销归因</Anchor>使您可以在广告系列中锁定现有或历史用户。再营销广告通常需要深度链接功能才能达到预期的效果。

<div id="in-app-events" />

### 应用内事件

应用所有者可以在其应用中对各种事件打点（如购买、观看教程、通关等），这样他们就能通过AppsFlyer对这些事件进行记录和分析。代理可以在其帐户的事件面板中查看归因给自己的应用内事件数据。

<div id="in-app-event-postbacks" />

#### 应用内事件回传

广告主可以授权让代理为广告平台配置<Anchor target="_blank" href="/marketers/zh/docs/in-app-event-postback-configuration">应用内事件回传</Anchor>（包括<Anchor target="_blank" href="/marketers/zh/docs/measure-sessions">af\_app\_opened事件</Anchor>）。

代理也可以授权给广告平台，让其自行配置应用内事件回传。 但这需要广告主在代理授权选项卡中<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">开放权限</Anchor>。

</Accordion>

<div id="reporting-for-agencies" />

<Accordion title="代理可用的报告工具">

* 代理可直接在AppsFlyer面板上查看并下载流量数据。
* 代理可以在AppsFlyer后台的<Anchor target="_blank" href="/marketers/zh/docs/raw-data-reporting-overview">导出数据</Anchor>页中拉取报告，并使用<Anchor target="_blank" href="/partners/zh/docs/data-locker-reports-for-agencies">Data Locker</Anchor>拉取群组分析报告。
* 代理可用的报告类型有以下两种：
  * 汇总
  * 原始数据
* 大多数情况下，广告主和代理在面板、报告等工具中的数据权限都有所不同。
* 由于代理通常仅负责广告主的部分流量，因此代理仅具有部分数据的权限。
* 有关各类账户之间的差异请参见<Anchor target="_blank" href="/marketers/zh/docs/manage-data-access-permissions">此文档</Anchor>。下文重点说明了代理账户的权限。

<div id="note-1" />

> 📘 **注意**
>
> 在Meta ads和X Ads的服务条款中，**代理**属于第三方，因此**无法获取来自Meta ads和X Ads的原始数据报告**。

<div id="access-to-aggregate-data" />

### 汇总数据的访问权限

* 代理账户默认具有效果报告（即汇总数据报告）的权限。 相关文档：<Anchor target="_blank" href="/marketers/zh/docs/aggregated-and-analytics-reporting-overview">汇总效果报告</Anchor>
* 代理可以获取汇总自然量报告，但需要广告主<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">授权</Anchor>。
* 代理可以查看留存报告、群组报告和Protect360面板，但需要广告主向代理<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">**开放留存和群组报告的权限**</Anchor>和/或<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">**Protect360面板的权限**</Anchor>，这两种权限在**活跃对接**页面的**授权**选项卡中分别设有配置选项。

<div id="access-to-raw-data" />

### 原始数据权限

<Anchor target="_blank" href="/marketers/zh/docs/raw-data-reporting-overview">原始数据报告</Anchor>（用户级别数据报告）中包含归因信息，并分为各种专项报告。

<div id="time-zone-and-currency" />

### 时区和货币

代理可以查看在应用配置中设定的时区和货币，但只有广告主可以修改这些设置。

<div id="cost-reporting" />

### 成本上报

如果代理配置的对接渠道**提供成本数据**，那么代理就可以<Anchor target="_blank" href="/marketers/zh/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">获取成本数据</Anchor>。

**请按以下步骤获取成本数据：**

1. 从AppsFlyer的侧边栏中选择**协作** > **活跃对接**。
2. 按成本筛选渠道：在**活跃对接**页面的顶部选择**支持的功能** > **成本**。
3. 选择您要查看的渠道，界面会跳转到**渠道对接**选项卡。点击进入**成本**选项卡。
4. 打开**获取成本数据**的开关。
5. 输入该渠道的API key。
6. 点击**保存**。

<div id="accessing-and-viewing-cost-data" />

#### 成本数据的查看及拉取

代理可以从以下数据来源中获取费用信息：

* **数据总览**面板：代理可以在数据总览面板的**汇总效果报告**中查看成本数据。
* **报告**：代理可以导出**原始数据**下的**激活**报告或**效果数据**下的**渠道**报告，并在其中查看成本数据。

<div id="hybrid-account-data-access" />

### 混合账户的数据访问权限

混合账户是一种具有双重身份的代理账户，分别以代理（应用合作渠道）和广告主（应用所有者）的身份管理不同的应用。

混合账户对以下功能的使用受限：

* <Anchor target="_blank" href="/marketers/zh/docs/custom-dashboards">自定义面板</Anchor>：代理账户和混合账户不可用。
* 群组报告：广告主授权后可用。
* Protect360：广告主授权后可用。

这些功能虽然也会出现在混合账户的面板上，但点开后会显示404报错。

如果您需要使用以上功能，建议新开一个广告主帐户，并将您的自有应用和代投应用分开管理。这样，您就可以在广告主帐户中开通并使用这些功能。

</Accordion>

<div data-zendesk-anchors="about-agency-accounts=%E4%BB%A3%E7%90%86%E8%B4%A6%E6%88%B7%E8%AF%A6%E8%A7%A3 h_01HDNYNZYR2FTMQ71EV2AY3A3A=%E4%BB%A3%E7%90%86%E8%B4%A6%E6%88%B7%E8%AF%A6%E8%A7%A3 agency-access-to-marketer-data=%E4%BB%A3%E7%90%86%E5%AF%B9%E5%B9%BF%E5%91%8A%E4%B8%BB%E6%95%B0%E6%8D%AE%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 h_01HDNYNZYRZKK97GZ6R0MB9RQN=%E4%BB%A3%E7%90%86%E5%AF%B9%E5%B9%BF%E5%91%8A%E4%B8%BB%E6%95%B0%E6%8D%AE%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 agency-access-to-ad-network-integrations=%E4%BB%A3%E7%90%86%E5%AF%B9%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%AF%B9%E6%8E%A5%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 h_01J00RYT8J0MBPHTGK5T4WEE43=%E4%BB%A3%E7%90%86%E5%AF%B9%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%AF%B9%E6%8E%A5%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 h_01HJR00RGQX0CQEHDS9BHBGJD4=%E6%B3%A8%E6%84%8F agency-transparency=%E4%BB%A3%E7%90%86%E6%95%B0%E6%8D%AE%E9%80%8F%E6%98%8E%E5%8C%96 h_01HDNYNZYRYHJ98YQWVVENZ07P=%E4%BB%A3%E7%90%86%E6%95%B0%E6%8D%AE%E9%80%8F%E6%98%8E%E5%8C%96 comparing-different-types-of-accounts=%E5%AF%B9%E6%AF%94%E4%B8%8D%E5%90%8C%E7%B1%BB%E5%9E%8B%E7%9A%84%E8%B4%A6%E6%88%B7 h_01HDNYNZYR65409AGM9F2PZRC8=%E5%AF%B9%E6%AF%94%E4%B8%8D%E5%90%8C%E7%B1%BB%E5%9E%8B%E7%9A%84%E8%B4%A6%E6%88%B7 h_01HDNYNZYS7A2H60EEAJ114VSM=agency-versus-marketer-accounts differences-between-marketer-and-agency-accounts=%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%90%E6%88%B7%E4%B8%8E%E4%BB%A3%E7%90%86%E5%B8%90%E6%88%B7%E7%9A%84%E5%B7%AE%E5%BC%82 h_01HDNYNZYSS7WSQ07S7KRADN7Z=%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%90%E6%88%B7%E4%B8%8E%E4%BB%A3%E7%90%86%E5%B8%90%E6%88%B7%E7%9A%84%E5%B7%AE%E5%BC%82 features-available-to-agencies=%E4%BB%A3%E7%90%86%E5%8F%AF%E7%94%A8%E7%9A%84%E5%8A%9F%E8%83%BD h_01HDNYNZYSX4WPQKS0H6JN6FCP=%E4%BB%A3%E7%90%86%E5%8F%AF%E7%94%A8%E7%9A%84%E5%8A%9F%E8%83%BD h_01HDNYNZYS8KRSPM5CPVJEJ74Y=agency-vs-ad-network-account differences-between-ad-network-and-agency-accounts=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%B8%90%E6%88%B7%E4%B8%8E%E4%BB%A3%E7%90%86%E5%B8%90%E6%88%B7%E7%9A%84%E5%B7%AE%E5%BC%82 h_01HDNYNZYS4VPZMY34WA3SG5JT=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%B8%90%E6%88%B7%E4%B8%8E%E4%BB%A3%E7%90%86%E5%B8%90%E6%88%B7%E7%9A%84%E5%B7%AE%E5%BC%82 agency-accounts%E2%80%94campaigns-and-reporting=%E4%BB%A3%E7%90%86%E8%B4%A6%E6%88%B7%E5%B9%BF%E5%91%8A%E6%8A%95%E6%94%BE%E5%8F%8A%E6%95%B0%E6%8D%AE%E4%B8%8A%E6%8A%A5 h_01HDNYNZYS32SNR5F0WKJ4G9Q1=%E4%BB%A3%E7%90%86%E8%B4%A6%E6%88%B7%E5%B9%BF%E5%91%8A%E6%8A%95%E6%94%BE%E5%8F%8A%E6%95%B0%E6%8D%AE%E4%B8%8A%E6%8A%A5 h_01HDNYNZYSNF2RQ3E7PM4HK433=agency-setting-up-campaigns selfreporting-ad-networks=%E8%87%AA%E5%BD%92%E5%9B%A0%E5%B9%B3%E5%8F%B0%E5%B9%B3%E5%8F%B0 h_01HDNYNZYS8X1VA4T46DQYQZFE=%E8%87%AA%E5%BD%92%E5%9B%A0%E5%B9%B3%E5%8F%B0%E5%B9%B3%E5%8F%B0 srn-configurations=srn%E9%85%8D%E7%BD%AE h_01HDNYNZYS8AM2MFPRXFA4JXNS=srn%E9%85%8D%E7%BD%AE h_01HDNYNZYSFXZXR99T6ME2R43F=%E7%A4%BA%E4%BE%8B nonsrns=%E9%9D%9Esrn h_01HDNYNZYSN28VZQKCBRGXAVY0=%E9%9D%9Esrn ad-network-configuration-visibility=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E9%85%8D%E7%BD%AE%E5%AF%B9%E4%BB%A3%E7%90%86%E7%9A%84%E5%8F%AF%E8%A7%81%E6%80%A7 h_01HDNYNZYSG5MQDDKV55HF4X9C=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E9%85%8D%E7%BD%AE%E5%AF%B9%E4%BB%A3%E7%90%86%E7%9A%84%E5%8F%AF%E8%A7%81%E6%80%A7 af_prt-parameter=af_prt%E5%8F%82%E6%95%B0 h_01HDNYNZYSC7XNJCJ1F27KTM9Z=af_prt%E5%8F%82%E6%95%B0 special-case-allinstalls-and-alllaunches-networks=%E7%89%B9%E6%AE%8A%E6%83%85%E5%86%B5%E5%85%A8%E5%AE%89%E8%A3%85%E5%92%8C%E5%85%A8%E5%90%AF%E5%8A%A8%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0 h_01HDNYNZYSB4MKXD47E1VHDN62=%E7%89%B9%E6%AE%8A%E6%83%85%E5%86%B5%E5%85%A8%E5%AE%89%E8%A3%85%E5%92%8C%E5%85%A8%E5%90%AF%E5%8A%A8%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0 how-to-setup-agency-attribution-with-all-installslaunches-networks=%E5%A6%82%E4%BD%95%E5%9C%A8%E5%85%A8%E9%87%8F%E6%BF%80%E6%B4%BB%E5%BA%94%E7%94%A8%E5%BC%80%E5%90%AF%E5%9B%9E%E4%BC%A0%E6%B8%A0%E9%81%93%E4%B8%8A%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86%E9%93%BE%E6%8E%A5 h_01HDNYNZYSHNV2B27JQV4EEVFM=%E5%A6%82%E4%BD%95%E5%9C%A8%E5%85%A8%E9%87%8F%E6%BF%80%E6%B4%BB%E5%BA%94%E7%94%A8%E5%BC%80%E5%90%AF%E5%9B%9E%E4%BC%A0%E6%B8%A0%E9%81%93%E4%B8%8A%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86%E9%93%BE%E6%8E%A5 h_01HDNYNZYS5WYADGW24AVK9RCZ=%E7%A4%BA%E4%BE%8B deep-linking=%E6%B7%B1%E5%BA%A6%E9%93%BE%E6%8E%A5 h_01HDNYNZYS5W0SMCF1YC6C3G4C=%E6%B7%B1%E5%BA%A6%E9%93%BE%E6%8E%A5 retargeting=%E5%86%8D%E8%90%A5%E9%94%80 h_01HDNYNZYS3Z7RE51M7G7386VZ=%E5%86%8D%E8%90%A5%E9%94%80 inapp-events=%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6 h_01HDNYNZYTDFN4MB6QBEQ8P5XW=%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6 inapp-event-postbacks=%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 h_01HMDP38S3NPE5R4QZJ5CW404W=%E5%BA%94%E7%94%A8%E5%86%85%E4%BA%8B%E4%BB%B6%E5%9B%9E%E4%BC%A0 h_01HDNYNZYTA767NGSTNECTBCV2=reporting-for-agencies h_01HDNYNZYTYBWGMY2PP8MPQE2F=%E6%B3%A8%E6%84%8F-1 access-to-performance-reports=%E6%B1%87%E6%80%BB%E6%95%B0%E6%8D%AE%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 h_01HDNYNZYTDH4S38XG3JCZQYJJ=%E6%B1%87%E6%80%BB%E6%95%B0%E6%8D%AE%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 access-to-raw-data=%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E6%9D%83%E9%99%90 h_01HDNYNZYT4ZKBNGDR3QR1VTEZ=%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E6%9D%83%E9%99%90 time-zone-and-currency=%E6%97%B6%E5%8C%BA%E5%92%8C%E8%B4%A7%E5%B8%81 h_01HDNYNZYT97ET1TQHKSRDMWDC=%E6%97%B6%E5%8C%BA%E5%92%8C%E8%B4%A7%E5%B8%81 cost-reporting=%E6%88%90%E6%9C%AC%E4%B8%8A%E6%8A%A5 h_01HDNYNZYTYT9NHMHQQ77PK8CQ=%E6%88%90%E6%9C%AC%E4%B8%8A%E6%8A%A5 accessing-and-viewing-cost-data=%E6%88%90%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%9A%84%E6%9F%A5%E7%9C%8B%E5%8F%8A%E6%8B%89%E5%8F%96 h_01HDNYNZYTWB5WVYY8C347G1ME=%E6%88%90%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%9A%84%E6%9F%A5%E7%9C%8B%E5%8F%8A%E6%8B%89%E5%8F%96 hybrid-account-data-access=%E6%B7%B7%E5%90%88%E8%B4%A6%E6%88%B7%E7%9A%84%E6%95%B0%E6%8D%AE%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 h_01HDNYNZYTKZTCBSBKZEJ7M0JN=%E6%B7%B7%E5%90%88%E8%B4%A6%E6%88%B7%E7%9A%84%E6%95%B0%E6%8D%AE%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90" />
