---
title: 代理商入门指南
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
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
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2026-10-14T10:09:17Z'
  id: 360002381617
  locale: zh-cn
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/zh-cn/articles/360002381617
---
> **概要：概要：本文介绍了代理账户的设置方式，以及设置完毕后如何开展客户投放监测工作。**

<Embed title="代理商入门指南" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/54qzpj1lm7" providerUrl="https://fast.wistia.com" />

## AppsFlyer归因模型

AppsFlyer的归因原理是非常重要的核心知识点，建议您先了解相关内容后再着手下一步工作。本节解释了从首次点击/展示到激活/事件归因，再到数据呈现/回传的整条链路。

[![ua-agency-flow.png](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)

1. 广告主或代理代表广告主通过AppsFlyer归因链接配置某个广告平台上的广告投放。
2. 用户点击了其中一则广告，比如横幅或优惠链接。
3. 广告背后的AppsFlyer归因链接会在点击发生时收集信息。AppsFlyer从归因链接中提取信息，并将其存储到我们的数据库中。
4. 用户跳转到应用商店。
5. 用户安装相关应用后，在首次打开该应用时会触发AppsFlyer SDK调用我们的服务器，提供该用户设备的相关信息。
6. AppsFlyer通过各种<Anchor target="_blank" href="/marketers/zh/docs/appsflyer-attribution-model">归因方式</Anchor>将这些数据与我们的点击数据库进行匹配。
7. 如果AppsFlyer找到了匹配数据，会将这次激活归因到相关的点击。如果没有匹配数据，则会将这次激活判定为自然激活。
8. 归因完毕后，AppsFlyer会在广告主和代理的面板和报告中（<Anchor target="_blank" href="/partners/zh/docs/about-agency-accounts#自归因平台平台">Meta ads和X Ads除外</Anchor>）呈现归因结果。
9. 然后，AppsFlyer会向广告平台发送回传，其中包含详细的转化数据。广告平台可以利用这些信息进一步优化广告投放。

## 代理在移动归因产业链中的角色

广告主（即应用所有者）在其应用中接入AppsFlyer SDK，以衡量其营销成效。

部分广告主会选择雇用营销代理为其代投广告。这时，代理就需要开设一个AppsFlyer账户，并让广告主为其开放<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">相关应用的权限</Anchor>。

也就是说，代理本质上并不持有这些应用的技术，而只是在其合作的营销渠道上推广这些应用，因此不涉及SDK对接等技术流程。AppsFlyer为代理提供一系列产品功能，各种功能可用性具体取决于广告主为代理设置的权限。

当AF将某个激活归因到某个代理投放的广告时，会在代理的面板上呈现该激活。广告主也会在其面板上看到这个激活，并知道它被归因到该代理。

注意：若贵司持有某个应用，或同时负责某个应用的开发和营销工作，则需开设广告主账户，而非代理账户。

## 定价

代理账户的使用范围取决于广告主在每个应用下为代理设置的权限。因此代理账户是**免费**的，归因费用完全由广告主承担。广告主和代理可以使用AppsFlyer的归因数据作为结算依据。

## 启用流程

请按以下步骤开设代理账户：

1. 1. 填写<Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">注册表格</Anchor>。
   * 请使用您的公司邮箱进行注册。
   * 请确保您使用的邮箱没有关联到其他现行的AppsFlyer账户。
2. 如果注册过程中需要您提供其他信息，AppsFlyer的代理团队会与您取得联系。
3. 您的账户激活后会收到通知，确认您可以开始使用AppsFlyer的服务。

## 添加团队成员

账户设立完毕并成功激活后，账户管理员（即开户人）可以在该账户中添加团队成员，为他们开放该代理账户下部分或所有应用的权限。有关添加团队成员的详细信息，请参考此文档。

## 在您的账户下添加应用

账户创建之初，账户下没有任何关联的应用，界面如下：

![agency-start.png](https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png)

代理侧的任何团队或个人都需要广告主授权才能执行以下操作：

* 访问相关应用的面板
* 更改配置
* 投放广告

广告主可以直接在AF后台<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#代理权限">为相关代理开放访问权限</Anchor> 。账户设置完毕并获得相关应用的权限后，您就可以使用AppsFlyer的功能来投放广告了。

### 广告主授权的作用

代理获得广告主授权后：

* 相关应用会出现在您的账户中。
* 您可以为该应用设置渠道对接（除部分渠道会要求广告主来完成相关配置）。
* 您可以创建归因链接，用于广告投放。
* 您可以与渠道设置成本对接（前提是该渠道支持成本对接）。
* 您可以查看相关应用的数据。
* 您可以为广告平台及其团队成员开放权限，允许其查看相关应用的基本信息。  
  也就是说，如果广告主和代理同时使用同一个广告平台，那么双方都可以调整该广告平台的团队成员查看应用面板的权限，且各自都能看到对方所做的更改。如果代理在未做任何更改的情况下看到该广告平台的团队成员有所增减，可能是因为广告主更改了团队成员。

此外，您还可让广告主为您开放其他功能的权限，如群组报告、Protect360面板及汇总的自然量数据等。

### 应用列表

广告主授权后，授权应用就会出现在代理的“应用”页面中。

代理账户的“应用”页面最多可显示1000个应用。如果您账户下的授权应用超过1000个，则部分应用不会显示在列表中，但您仍可以通过搜索找到这些应用。

![agency-apps.png](https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png)

#### 搜索应用程序

2. 在搜索栏中输入关键词，如：
   * App Name（应用名称）
   * App ID（应用ID）
   * 广告主邮箱

### 代理数据透明化设置

鉴于业界对行业生态中数据透明度的日益重视，AppsFlyer现支持广告主与代理之间的数据透明化，帮助双方充分利用AppsFlyer的报告和分析工具。

请注意：

## 代理面板

您仅需点击应用列表中的相关应用，就能进入其<Anchor target="_blank" href="/marketers/zh/docs/getting-started-with-appsflyer-dashboards">面板</Anchor>。投放广告时，您可以在面板中查看归因给您的汇总数据。

![agency-dashboard.png](https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png)

代理账户的面板默认具备以下功能：

* LTV（生命周期价值）维度的数据总览面板
* 应用内事件控制面板
* 重定向控制面板

## 广告投放

### 自归因平台（SRN）

自归因平台（Self- reporting Networks或Self-attributing Networks，简称SRN或SAN）不需要通过AppsFlyer的归因链接来上报点击数和其他数据，而是与AppsFlyer直接对接。这些自归因平台包括<Anchor target="_blank" href="/marketers/zh/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta ads</Anchor>、<Anchor target="_blank" href="/marketers/zh/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor>、<Anchor target="_blank" href="/marketers/zh/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads</Anchor>、<Anchor target="_blank" href="/marketers/zh/docs/snapchat-advanced-srn-integration-setup">Snapchat</Anchor>、DoubleClick、<Anchor target="_blank" href="/marketers/zh/docs/apple-ads-integration-setup">Apple Ads Search</Anchor>、<Anchor target="_blank" href="/marketers/zh/docs/yahoo-integration-setup">Yahoo</Anchor>、和<Anchor target="_blank" href="/marketers/zh/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">Yahoo! JAPAN</Anchor>。JAPAN

代理在大多数自归因平台中投放广告时都需要进行特殊设置。例如，由于Meta ads和X Ads规定只能由广告主来配置对接，因此代理投放的广告系列名称必须以代理的名称开头，否则代理带来的激活将无法正常归因到该代理。

有关具体SRN的操作指南和代理设置，请参见上文链接中的文档。

### 非SRN

大多数广告平台需要在广告中设置归因链接。在非SRN平台上投放广告的详细指南请见<Anchor target="_blank" href="/partners/zh/docs/about-agency-accounts#非srn">此文档</Anchor>。


<span id="sandbox-attribution-agency-campaigns"></span>虽然Apple并没有把代理纳入SKAN的归因流程，且AppsFlyer也不能直接将转化归因到代理，但在SKAN环境中投放广告的代理仍能获得AppsFlyer提供的归因数据。

#### 广告系列的命名

* 代理的af\_prt（<Anchor target="_blank" href="/partners/zh/docs/about-agency-accounts#af_prt参数">定义及获取方式</Anchor>），
* 下划线，
* 由代理命名的实际广告系列名称。

举例来说，假设您的af\_prt是AgencyX，那么您可以将广告系列名称设置为：

`AgencyX_SummerSale`

### SKAdNetwork中的代理投放

Apple推出的SKAdNetwork框架（简称SKAN）是iOS的一部分，该框架可让广告主在没有IDFA或广告ID的情况下衡量投放效果。虽然Apple并没有把代理纳入SKAN的归因流程，且AppsFlyer也不能直接将转化归因到代理，但在SKAN环境中投放广告的代理仍能获得AppsFlyer提供的归因数据。

#### 广告系列的命名

代理配置的SKAN广告系列名称中必须包含代理的渠道标识符，才能在AppsFlyer的SKAN面板中正常显示。请务必按以下结构配置广告系列名称：

* 代理的af\_prt（<Anchor target="_blank" href="/partners/zh/docs/about-agency-accounts#af_prt参数">定义及获取方式</Anchor>），
* 下划线，
* 由代理命名的实际广告系列名称。

举例来说，假设您的af\_prt是AgencyX，那么您可以将广告系列名称设置为：

`AgencyX_SummerSale`

> 📘 **注意**
>
> * SKAN中的代理投放信息始终是透明的，不会对广告主隐瞒代理使用的广告平台。而且从iOS 15开始，广告主（即应用所有者）可以<Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">选择直接接收SKAN回传副本</Anchor>。
> * 上述操作不是您面板中的渠道激活设置，您在代理面板中激活渠道后还需要广告主完成上述操作。

#### SKAN转化值操作台的访问权限

代理可以在<Anchor target="_blank" href="/marketers/zh/docs/skan-conversion-studio#view-cv-mapping">转化值操作台</Anchor>中<Anchor target="_blank" href="/marketers/zh/docs/skan-conversion-studio#skan转化值操作台基础操作指南">查看并下载</Anchor>广告主的SKAN CV映射配置，但不能进行配置或更改操作。

#### SKAN面板

<Embed title="代理商入门指南" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**相关文档：**

* <Anchor target="_blank" href="/marketers/zh/docs/about-att-and-skan">SKAdNetwork快速入门指南</Anchor>
* <Anchor target="_blank" href="/marketers/zh/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAN面板</Anchor>
* <Anchor target="_blank" href="/marketers/zh/docs/skadnetwork-skan-solution-guide">SKAdNetwork 解决方案</Anchor>

### 代理的单一可信数据源（SSOT）权限

SSOT机制可结合不同模式的归因数据，并对激活及其相关的成本和收入指标进行去重，从而将所有归因模式产生的数据进行统一的标准化处理，这样就能确保eCPI、ROI和ROAS等指标的正确计算。

代理可以访问总览面板中的SSOT数据，但不能使用API拉取SSOT数据。

广告主必须在转化值操作台中打开SSOT开关，才能让代理在其总览面板中看到SSO标记。

**相关文档：**

* <Anchor target="_blank" href="/marketers/zh/docs/single-source-of-truth-ssot-guide-for-ios-attribution">iOS归因的单一可信数据源（SSOT）指南</Anchor>

## 代理可用的其他功能

* 衡量用户的留存率
* 使用应用内事件数据来优化投放
* 投放<Anchor target="_blank" href="/marketers/zh/docs/retargeting-attribution-guide">再营销</Anchor>广告
* 导出<Anchor target="_blank" href="/marketers/zh/docs/manage-data-access-permissions">数据</Anchor>
* <Anchor target="_blank" href="/marketers/zh/docs/registering-test-devices">测试机加白</Anchor>
* 以及未来开发的其他功能。

有关代理账户的更多功能请见<Anchor target="_blank" href="/partners/zh/docs/about-agency-accounts#agency-setting-up-campaigns">此文档</Anchor>。

文档中出现了陌生的概念？请参考我们的<Anchor target="_blank" href="/marketers/zh/docs/appsflyer-knowledge-base-glossary">词汇表</Anchor>，帮助您理解文档内容。

遇到了紧急的技术问题？请在我们的帮助中心中搜索相关内容，说不定就能找到答案！如果没找到您需要的信息，请通过面板右下角的按钮联系我们的技术支持团队。

<div data-zendesk-anchors="appsflyer-attribution-model=appsflyer%E5%BD%92%E5%9B%A0%E6%A8%A1%E5%9E%8B h_01HFXXKCMW7EREMC7KEYTF3ERH=appsflyer%E5%BD%92%E5%9B%A0%E6%A8%A1%E5%9E%8B agency-role-in-mobile-attribution-chain=%E4%BB%A3%E7%90%86%E5%9C%A8%E7%A7%BB%E5%8A%A8%E5%BD%92%E5%9B%A0%E4%BA%A7%E4%B8%9A%E9%93%BE%E4%B8%AD%E7%9A%84%E8%A7%92%E8%89%B2 h_01HFXXKCMW987FV2PB4EPXH92Z=%E4%BB%A3%E7%90%86%E5%9C%A8%E7%A7%BB%E5%8A%A8%E5%BD%92%E5%9B%A0%E4%BA%A7%E4%B8%9A%E9%93%BE%E4%B8%AD%E7%9A%84%E8%A7%92%E8%89%B2 pricing=%E5%AE%9A%E4%BB%B7 h_01HFXXKCMWPN6AN98A5RD5YXW7=%E5%AE%9A%E4%BB%B7 getting-started=%E5%90%AF%E7%94%A8%E6%B5%81%E7%A8%8B h_01HFXXKCMWRXVBYTW9RYEX7X8F=%E5%90%AF%E7%94%A8%E6%B5%81%E7%A8%8B adding-team-members=%E6%B7%BB%E5%8A%A0%E5%9B%A2%E9%98%9F%E6%88%90%E5%91%98 h_01HFXXKCMWB6ZG3PSHDSETC4XC=%E6%B7%BB%E5%8A%A0%E5%9B%A2%E9%98%9F%E6%88%90%E5%91%98 adding-apps-to-your-account=%E5%9C%A8%E6%82%A8%E7%9A%84%E8%B4%A6%E6%88%B7%E4%B8%8B%E6%B7%BB%E5%8A%A0%E5%BA%94%E7%94%A8 h_01HFXXKCMWBZVTHAEKED1Q27M3=%E5%9C%A8%E6%82%A8%E7%9A%84%E8%B4%A6%E6%88%B7%E4%B8%8B%E6%B7%BB%E5%8A%A0%E5%BA%94%E7%94%A8 what-does-it-mean-to-get-permission-from-a-marketer=%E5%B9%BF%E5%91%8A%E4%B8%BB%E6%8E%88%E6%9D%83%E7%9A%84%E4%BD%9C%E7%94%A8 h_01HFXXKCMWYNNZWTKP9KEQ4VCD=%E5%B9%BF%E5%91%8A%E4%B8%BB%E6%8E%88%E6%9D%83%E7%9A%84%E4%BD%9C%E7%94%A8 app-list=%E5%BA%94%E7%94%A8%E5%88%97%E8%A1%A8 h_01HFXXKCMWKW78TMC76F40PY2C=%E5%BA%94%E7%94%A8%E5%88%97%E8%A1%A8 searching-for-apps=%E6%90%9C%E7%B4%A2%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F h_01HFXXKCMW8S93N577393QZTYX=%E6%90%9C%E7%B4%A2%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F transparency=%E4%BB%A3%E7%90%86%E6%95%B0%E6%8D%AE%E9%80%8F%E6%98%8E%E5%8C%96%E8%AE%BE%E7%BD%AE h_01HFXXKCMW5YC2APNGHNV6B35C=%E4%BB%A3%E7%90%86%E6%95%B0%E6%8D%AE%E9%80%8F%E6%98%8E%E5%8C%96%E8%AE%BE%E7%BD%AE agency-dashboard=%E4%BB%A3%E7%90%86%E9%9D%A2%E6%9D%BF h_01HFXXKCMWPZVADY15DKATJ7Z4=%E4%BB%A3%E7%90%86%E9%9D%A2%E6%9D%BF running-campaigns=%E5%B9%BF%E5%91%8A%E6%8A%95%E6%94%BE h_01HFXXKCMWFB9RXY7AVBX5CGB9=%E5%B9%BF%E5%91%8A%E6%8A%95%E6%94%BE selfreporting-networks-srns=%E8%87%AA%E5%BD%92%E5%9B%A0%E5%B9%B3%E5%8F%B0srn h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=%E8%87%AA%E5%BD%92%E5%9B%A0%E5%B9%B3%E5%8F%B0srn nonsrns=%E9%9D%9Esrn h_01HFXXKCMWPAMZ373D5AVD5EJF=%E9%9D%9Esrn h_01J6PCDYM2W1X6EMMEE7SFB3VE=sandbox-attribution-agency-campaigns campaign-naming=%E5%B9%BF%E5%91%8A%E7%B3%BB%E5%88%97%E7%9A%84%E5%91%BD%E5%90%8D h_01HFXXKCMWMW1AHXMS19CYD4VC=%E5%B9%BF%E5%91%8A%E7%B3%BB%E5%88%97%E7%9A%84%E5%91%BD%E5%90%8D h_01HFXXKCMWEQ41A7TZ2K6DE424=%E6%B3%A8%E6%84%8F skadnetwork-agency-campaigns=skadnetwork%E4%B8%AD%E7%9A%84%E4%BB%A3%E7%90%86%E6%8A%95%E6%94%BE h_01HFXXKCMWZ19E0QR1VE977BTS=skadnetwork%E4%B8%AD%E7%9A%84%E4%BB%A3%E7%90%86%E6%8A%95%E6%94%BE 01J6PCG6JGY2R8T5DDCR8APM66=%E5%B9%BF%E5%91%8A%E7%B3%BB%E5%88%97%E7%9A%84%E5%91%BD%E5%90%8D-1 01J6PCG6JHK9TGX93SD4DRP393=%E6%B3%A8%E6%84%8F access-to-skan-conversion-studio=skan%E8%BD%AC%E5%8C%96%E5%80%BC%E6%93%8D%E4%BD%9C%E5%8F%B0%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 h_01HFXXKCMWX53HMRG2ZTD9FYQE=skan%E8%BD%AC%E5%8C%96%E5%80%BC%E6%93%8D%E4%BD%9C%E5%8F%B0%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90 skadnetwork-dashboard=skan%E9%9D%A2%E6%9D%BF h_01HFXXKCMW1HHMSS3XAXJKME29=skan%E9%9D%A2%E6%9D%BF single-source-of-truth-ssot-for-agencies=%E4%BB%A3%E7%90%86%E7%9A%84%E5%8D%95%E4%B8%80%E5%8F%AF%E4%BF%A1%E6%95%B0%E6%8D%AE%E6%BA%90ssot%E6%9D%83%E9%99%90 h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=%E4%BB%A3%E7%90%86%E7%9A%84%E5%8D%95%E4%B8%80%E5%8F%AF%E4%BF%A1%E6%95%B0%E6%8D%AE%E6%BA%90ssot%E6%9D%83%E9%99%90 what-else-you-can-do=%E4%BB%A3%E7%90%86%E5%8F%AF%E7%94%A8%E7%9A%84%E5%85%B6%E4%BB%96%E5%8A%9F%E8%83%BD h_01HFXXKCMXQ2JT63GBMC74PWBA=%E4%BB%A3%E7%90%86%E5%8F%AF%E7%94%A8%E7%9A%84%E5%85%B6%E4%BB%96%E5%8A%9F%E8%83%BD" />
