---
title: 广告平台入驻指南
metadata:
  keywords:
    - Ad Network
    - Advertisers
    - Ad Networks
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
  created_at: '2019-03-28T08:41:59Z'
  edited_at: '2026-10-14T10:03:17Z'
  id: 360001300998
  locale: zh-cn
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/zh-cn/articles/360001300998
---
> **概要：** 本文介绍了广告平台应如何设置并测试归因链接及回传对接，从而完成与AppsFlyer的对接，旨在帮助您了解相关的操作步骤、时间顺序以及流程中涉及的人员。

<Image align="center" alt="AdNetworks_-_Onboarding__2_.png" src="https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png" />

<div id="what-is-appsflyer" />

## AppsFlyer的角色

作为移动归因行业的领军企业，AppsFlyer热忱欢迎您加入我们的对接渠道阵营。本指南旨在帮助已完成AppsFlyer渠道注册的广告平台进行对接设置。如果您想要注册为渠道，需要<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#在appsflyer中添加新的对接渠道">AppsFlyer客户（即广告主）向您发出相关邀请。</Anchor>

<div id="ad-network-onboarding" />

## 广告平台入驻

请参考本文的**入驻步骤**部分，其中列出了对接流程的步骤以及各环节的预估耗时。

对接的意义：

* 让AppsFlyer记录您的广告互动（点击和展示），并根据<Anchor target="_blank" href="/marketers/zh/docs/appsflyer-attribution-model">AppsFlyer归因模型</Anchor>对这些互动进行归因。
* 将回传数据以您指定的格式发送到您的端点。
* 您可以使用点击签名、Protect360、Data Locker等一系列AppsFlyer功能。

<div id="if-you-need-help" />

<Accordion title="参考资料">

* 如遇问题，可以在<Anchor target="_blank" href="/partners/zh/docs/integrated-partners-faq">常见问题答疑</Anchor>中找到答案
* 或者参考<Anchor target="_blank" href="/partners/zh/docs/integration-requests-for-partners">对接变更请求</Anchor>

</Accordion>

考虑：

* 本文中的耗时预估是根据我们与广告平台的对接经验得出的。每个对接都会稍有不同，因此实际用时会有出入。
* AppsFlyer支持多个<Anchor target="_blank" href="/partners/zh/docs/platforms-for-ad-networks">效果广告平台</Anchor>。如果您使用了列表中的平台，请务必在对接前参考相关平台的专用指南。

<div id="onboarding-steps" />

## 入驻步骤

**请按以下流程与AppsFlyer对接**：

1. [第一部分——对接与测试。](/docs/getting-started-onboarding-guide-for-ad-networks#第一部分对接与测试)
2. [第二部分——通过广告主应用测试。](/docs/getting-started-onboarding-guide-for-ad-networks#第二部分通过广告主应用测试)
3. [第三部分——使用AppsFlyer面板及报告工具。](/docs/getting-started-onboarding-guide-for-ad-networks#第三部分appsflyer面板及报告选项)

<div id="part-1-integration-and-testing" />

### 第一部分：对接与测试

<table><thead><tr><th>操作</th><th>用时（分钟）</th></tr></thead><tbody><tr><td>您的注册申请获批后会收到邮件通知，其中包含对接邀请，让您完成必要的步骤。</td><td>--</td></tr><tr><td colspan="2"> <strong>必须完成的对接步骤</strong>  </td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#归因链接" target="_blank">配置您的归因链接</a>： 归因链接是带有宏的URL，广告平台以实际产生的值填充这些宏，然后每当有用户点击链接时将其发送到AppsFlyer。 <br/>请注意：如果您使用了AppsFlyer支持的效果广告平台，必须按相关平台的专用指南进行操作。详情请见<a href="./platforms-for-ad-networks" target="_blank">效果广告平台指南。</a> </td><td>60</td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#默认回传" target="_blank">配置回传宏</a>：回传URL中所包含的宏由AppsFlyer填充，并会在每次发生转化后实时发送到您的服务器。</td><td>60</td></tr><tr><td>使用证书登录到<a href="https://hq1.appsflyer.com/auth/login" target="_blank">AppsFlyer面板</a>。 </td><td> </td></tr><tr><td>上传您的公司Logo。Logo的格式必须为200 X 50透明PNG。 <ol><li>在AppsFlyer后台的菜单栏中点选您的邮箱地址 &gt; <strong>合作伙伴配置</strong>。 </li><li>在<strong>简介</strong>选项卡中上传您的公司Logo。 </li><li>点击<strong>保存</strong>。</li></ol></td><td>5</td></tr><tr><td>使用AppsFlyer的测试应用来测试对接：<ul><li><a href="./android-integration-testing-for-ad-networks" target="_blank">安卓</a></li><li><a href="./ios-integration-testing-for-ad-networks" target="_blank">iOS</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>可选对接设置</strong></td></tr><tr><td>【iOS】如果您的广告主需要使用AppsFlyer的AAP功能（Aggregated Advanced Privacy，即汇总层级的高级隐私保护），请完成<a href="./self-serve-integration-management-for-ad-networks#高级隐私保护和skan回传" target="_blank">高级隐私</a>对接。</td><td>60</td></tr><tr><td>【iOS】如果您投放SKAdNetwork广告，请完成<a href="./self-serve-integration-management-for-ad-networks#高级隐私保护和skan回传" target="_blank">SKAdNetwork对接</a>。 </td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>授权代理</strong></h4>您可以创建一个授权代理列表，并根据需要对其进行调整，获得您认可的代理才能通过您的平台对接来投放广告。如需添加授权代理，请进入AppsFlyer后台的安全中心，并将相关代理的代理ID（af_prt）添加到<a href="./set-up-your-list-of-authorized-agencies" target="_blank"><strong>授权代理</strong></a>部分。代理ID信息须由相关代理提供。</td><td>2</td></tr><tr><td colspan="2"><p><strong>其他功能及注意事项</strong><br/> </p><p>请根据广告主的要求配置对接。</p></td></tr><tr><td>如需防止作弊平台使用您的渠道标识符发送点击假量，请启用<a href="./click-signing-for-ad-networks" target="_blank">点击签名</a>。 </td><td>60+</td></tr><tr><td>如果广告主启用了Protect360或验证规则，请添加<a href="./postback-macros-for-ad-networks#激活应用内事件和被拒绝事件中的宏" target="_blank">被拦截的归因回传</a>。</td><td>15</td></tr><tr><td>通过API向AppsFlyer发送成本数据。详见<a href="./incost-api-for-ad-networks" target="_blank">InCost API</a>。</td><td>60+</td></tr><tr><td> <a href="/marketers/zh/docs/retargeting-attribution-guide" target="_blank">再营销对接</a>。</td><td>15</td></tr><tr><td> <a href="/marketers/zh/docs/measure-view-through-engagements" target="_blank">浏览型归因对接</a>。</td><td>15</td></tr></tbody></table>

<div id="part-2-test-using-advertiser-apps" />

### 第二部分：通过广告主应用测试

本节讲解了如何使用广告主的应用测试您的对接。由于这部分涉及到广告主，因此有些步骤需要广告主来完成。代理也可以以广告主的身份代替广告主完成相关操作。

| 涉及人员 | 操作 | 用时（分钟） |
| --- | --- | --- |
| 广告主 | 打开<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#integration-tab">激活渠道</Anchor>开关。<br /><br />此开关开启时AppsFlyer会将您带来的广告互动纳入归因范围。 | 2 |
| 广告主 | 向<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#广告平台权限">广告平台开放权限</Anchor>并添加您的团队成员。<br /><br />权限开放后，您可以在AppsFlyer面板中查看效果数据。相关数据仅对列表中的团队成员可用。 | 2 |
| 广告平台 | <Anchor target="_blank" href="/marketers/zh/docs/user-management#creating-users">在您的账户中添加团队成员</Anchor>。 | 2 |
| 广告主（管理员） | <Anchor target="_blank" href="/marketers/zh/docs/registering-test-devices">测试机加白</Anchor>。需要广告主代您完成此步骤。 | 3 |
| 广告平台 | <Anchor target="_blank" href="/partners/zh/docs/test-marketer-campaign-integration-with-the-ad-network">使用广告主的应用测试对接。</Anchor> | 60 |

<div id="part-3-appsflyer-dashboard-and-reporting-options" />

### 第三部分：AppsFlyer面板及报告选项

| 可选方案 |
| --- |
| <Anchor target="_blank" href="/partners/zh/docs/integrated-partners-dashboard">使用合作伙伴面板</Anchor>。 |
| 使用面向广告平台的<Anchor target="_blank" href="/partners/zh/docs/data-locker-for-partners">Data Locker</Anchor>通过云存储服务获取汇总的效果数据。 |
| 获取Protect360<Anchor target="_blank" href="/marketers/zh/docs/raw-data-export-page">原始数据</Anchor>。 |

<div id="integration-validation-period" />

## 对接认证期

为了确保AppsFlyer生态系统中各方的真实性和有效性，同时保护我们的内部系统不受无效流量影响，所有新增的广告平台对接都需要完成对接认证。在对接认证期间，AppsFlyer会对相关渠道进行全面的流量验证和质量评估。新渠道必须先通过认证才能出现在<Anchor target="_blank" href="/marketers/zh/docs/partner-integrations">Marketplace</Anchor>平台中，对所有广告主可见。

<div id="validation-periodfaq" />

### 对接认证期的常见问题解答

| **问题** | **答案** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>我已经完成了对接，但广告主仍然无法在Marketplace中找到我，为什么？ | 在对接认证期间，您的对接仅对引荐您的广告主可见。流量质量认证完毕后，您会收到通知邮件，说明您的对接已对所有广告主可见。 |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>如何确保我的对接能通过认证？ | 为引荐您的广告主带来大量优质流量。 |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>何时可收到认证完成的通知邮件？ | 得到认证的流量到达一定量后，您会收到邮件，通知您认证期已结束。 |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>可否了解当前的认证评估状态？ | 需等到认证期结束后您才会收到邮件通知。 |
| <span id="what-are-the-validation-criteria-based-on"></span>认证标准有哪些？ | 认证标准以<Anchor target="_blank" href="/marketers/zh/docs/protect360-anti-fraud-guide">Protect360</Anchor>的动态机器学习算法为基础，综合考量广告平台的流量质量和数量、整体的数据有效性以及行业最佳水平。 |
| <span id="another-adviertiser-wants-to-work-with-me"></span>如果在认证期间有其他广告主想要与我合作，要如何处理？ | 在认证期间您的对接仅对引荐您的广告主可见。认证顺利完成后，其他广告主就可以跟您开展合作了。 |
| <span id="my-integration-fails"></span>如果我的对接没有通过认证要怎么办？ | 我们会延长认证期，观测您的流量质量是否有所改善。如果没有改善，您的对接会被永久性地从AppsFlyer平台中移除。无论是否通过认证，您都会收到通知邮件。 |
| <span id="replace-advertiser"></span>是否可更换引荐方广告主？ | 可以，但必须在30天的认证期内更换。 |

<div data-zendesk-anchors="what-is-appsflyer=appsflyer%E7%9A%84%E8%A7%92%E8%89%B2 h_01J09255QNBFRV8DYZPGG990A0=appsflyer%E7%9A%84%E8%A7%92%E8%89%B2 ad-network-onboarding=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%85%A5%E9%A9%BB h_01J09255QN61VPW292PC2CH9KN=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E5%85%A5%E9%A9%BB h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help onboarding-steps=%E5%85%A5%E9%A9%BB%E6%AD%A5%E9%AA%A4 h_01J09255QNZ9QXXFB54YRYCM8P=%E5%85%A5%E9%A9%BB%E6%AD%A5%E9%AA%A4 part-1-integration-and-testing=%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86%E5%AF%B9%E6%8E%A5%E4%B8%8E%E6%B5%8B%E8%AF%95 h_01J09255QN35ZBKE2R2HDDZWSZ=%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86%E5%AF%B9%E6%8E%A5%E4%B8%8E%E6%B5%8B%E8%AF%95 h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies part-2-test-using-advertiser-apps=%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%E9%80%9A%E8%BF%87%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%BA%94%E7%94%A8%E6%B5%8B%E8%AF%95 h_01J09255QP11XJD3C83VZZXXQZ=%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%E9%80%9A%E8%BF%87%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%BA%94%E7%94%A8%E6%B5%8B%E8%AF%95 part-3-appsflyer-dashboard-and-reporting-options=%E7%AC%AC%E4%B8%89%E9%83%A8%E5%88%86appsflyer%E9%9D%A2%E6%9D%BF%E5%8F%8A%E6%8A%A5%E5%91%8A%E9%80%89%E9%A1%B9 h_01J09255QPSSD8CF0HR059RWXZ=%E7%AC%AC%E4%B8%89%E9%83%A8%E5%88%86appsflyer%E9%9D%A2%E6%9D%BF%E5%8F%8A%E6%8A%A5%E5%91%8A%E9%80%89%E9%A1%B9 integration-validation-period=%E5%AF%B9%E6%8E%A5%E8%AE%A4%E8%AF%81%E6%9C%9F h_01J09255QP82ZYZDJMA74SRYGZ=%E5%AF%B9%E6%8E%A5%E8%AE%A4%E8%AF%81%E6%9C%9F validation-period%E2%80%94faq=%E5%AF%B9%E6%8E%A5%E8%AE%A4%E8%AF%81%E6%9C%9F%E7%9A%84%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E8%A7%A3%E7%AD%94 h_01J09255QP77BME57P9B7S222V=%E5%AF%B9%E6%8E%A5%E8%AE%A4%E8%AF%81%E6%9C%9F%E7%9A%84%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E8%A7%A3%E7%AD%94" />
