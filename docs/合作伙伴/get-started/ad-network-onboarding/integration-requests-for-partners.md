---
title: 合作伙伴的集成变更请求
metadata:
  keywords:
    - postbacks
    - integrated partner
    - view-through attribution
    - Advertisers
    - Ad Networks
    - Partners
    - SKAD
    - Advanced Privacy
    - Marketers
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2021-01-28T12:40:43Z'
  edited_at: '2026-10-14T10:11:50Z'
  id: 360017189177
  locale: zh-cn
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/zh-cn/articles/360017189177
---
> **概要**：请求更改初始集成设置所需了解的所有信息。

<div id="implement-audience-feature" />

<div id="implement-incost-api" />

<div id="important" />

> 🚧 **重要提示！**
>
> AppsFlyer 的回调和归因 URL 结构是全球性的。这意味着这些结构中的任何更改都会影响所有应用程序的所有现有和未来活动。

使用 <Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/51165640234513">合作伙伴助手小部件</Anchor> 提交更改合作伙伴设置的工单：

1. 在任何 AppsFlyer 页面右上角，点击帮助图标。
2. 在小部件中选择以下选项序列：  
   **联系团队** > **(2) 我想了解或更新我的集成** > **(1)** **更新我的集成**。
3. 选择 **高级隐私或 SKAD 模式** 或 **默认模式**。
4. 提供下表中指定的必要要求。

| 请求 | 说明 | 要求 |
| --- | --- | --- |
| <span id="enable-viewthrough-attribution"></span>启用浏览型归因 | 允许查看转化归因测量。  <br />宏 `attributed_touch_type` 包含展示或点击以指示参与类型。 <br /><br /><Anchor target="_blank" href="/marketers/zh/docs/measure-view-through-engagements">有关查看转化归因的更多信息。</Anchor> | 此功能仅对指定的合作伙伴可用。如果您感兴趣，请联系您的合作伙伴发展经理 (PDM)。 |
| <span id="enable-rejected-postback"></span>启用拒绝的回调 | 允许发送因欺诈或不符合验证规则而被拒绝的安装和应用内事件的回调。 | <ol><li>按照 <Anchor target="_blank" href="/partners/zh/docs/self-serve-integration-management-for-ad-networks">广告网络的自助集成管理</Anchor> 在 AppsFlyer 仪表板中配置拒绝的回调。</li><li>确保将下面的拒绝参数附加到您的默认回调模板（安装/应用内事件）中。<ul><li>is-rejected</li><li>`{blocked-reason}</li><li>{blocked-sub-reason}</li><li>blocked_reason_value</li></ul></li><li>一旦将任何拒绝参数添加到默认回调中，拒绝的安装/应用内事件回调将被启用。</li></ol>如有任何问题，或如果您无法访问回调管理平台：<ol><li>从小部件中选择 **默认模式**。</li><li>将 "启用拒绝的回调" 写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>[推荐] 接收参数的名称（由您的技术团队定义）用于宏 is-rejected},{blocked-reason},{blocked-sub-reason},{blocked-reason-value}`</li><li>参数应添加到哪种类型的回调（安装、应用内事件或两者）</li></ul></li></ol> |
| <span id="enable-retargeting"></span>开启重定向广告 | 允许重新定位活动测量。<br />AppsFlyer 在回调中提供以下宏，以识别活动是否为重新定位活动以及转换类型（重新归属或重新参与）：<ul><li>`is-retarget`</li><li>`retargeting_conversion_type`</li></ul><Anchor target="_blank" href="/marketers/zh/docs/retargeting-attribution-guide">有关重新定位的更多信息。</Anchor> | <ol><li>按照 <Anchor target="_blank" href="/partners/zh/docs/self-serve-integration-management-for-ad-networks">自助服务广告网络集成管理</Anchor> 在 AppsFlyer 仪表板中配置回调（安装/应用内事件）</li><li>一旦添加了以下参数并保存配置，AppsFlyer 后台的 '启用重新定位' 切换将自动启用。<ul><li>`{is-retarget}</li><li>{retargeting-conversion-type}`</li></ul></li></ol>如有任何问题，或如果您无法访问回调管理平台：<ol><li>从小部件中选择 **默认模式**。</li><li>将 "启用重新定位" 写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>[推荐] 接收参数的名称（由您的技术团队定义）用于宏 `is-retarget` 和 `retargeting_conversion_type`.</li><li>参数应添加到哪种类型的回调（安装、应用内事件或两者）</li><li>指示是否需要为重新参与事件（即在点击重新定位活动广告后首次打开现有应用）提供重新参与回调。</li></ul></li></ol> |
| <span id="enable-uninstall"></span>启用卸载 | 获取 `af_uninstall` 应用内事件的回调以测量卸载。<br /><br />有关卸载的更多信息。 | <ol><li>从小部件中选择 **默认模式**。</li><li>将 "启用 af\_uninstall 应用内事件回调" 写为工单标题。</li><li>分享您的 PID 或登录用户名</li></ol> |
| <span id="enable-sending-session-data"></span>启用发送会话数据 | 允许为 `af_app_opened` 的应用内事件共享数据。<br /><br /><Anchor target="_blank" href="/marketers/zh/docs/measure-sessions">有关会话数据的更多信息。</Anchor> | <ol><li>从小部件中选择 **默认模式**。</li><li>将 "启用 af\_app\_opened 回调" 写为工单标题。</li><li>分享您的 PID 或登录用户名。</li></ol> |
| <span id="enable-postbacks-retry"></span>启用回调重试 | 在发送失败的情况下启用多次发送回调。  <br />使用 `postback-id` 宏来识别回调 ID。<br /><br /><Anchor target="_blank" href="/partners/zh/docs/postback-retries">有关回调重试的更多信息。</Anchor> | <ol><li>从小部件中选择 **默认模式**。</li><li>将 "启用回调重试" 写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>`postback-id` 宏的接收参数名称</li></ul></li></ol> |
| <span id="update-postback"></span>更新回调 | 更改当前回调结构（例如，删除/添加参数，改变端点 URL。）<br /><br /><Anchor target="_blank" href="/partners/zh/docs/postback-macros-for-ad-networks">有关回调和宏的更多信息。</Anchor> | <ol><li>从小部件中选择 **默认模式**。</li><li>将 "更新回调" 写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>基于可用宏的新回调结构</li></ul></li></ol> |
| <span id="enable-advanced-privacy-postback"></span>启用高级隐私回调 | 设置高级隐私集成以遵守广告商的数据共享政策。<br /><br /><Anchor target="_blank" href="/partners/zh/docs/advanced-privacy-guide-postback-macros-for-ad-networks">有关高级隐私回调的更多信息。</Anchor> | <ol><li>在 AppsFlyer 仪表板中遵循 <Anchor target="_blank" href="/partners/zh/docs/self-serve-integration-management-for-ad-networks">高级隐私回调配置的说明</Anchor>。</li><li>确保 <Anchor target="_blank" href="/partners/zh/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements">您的归因链接包含所有必需参数</Anchor>。</li></ol>如果出现任何问题，或者您必须向归因链接模板添加参数：<ol><li>从小部件中选择 **高级隐私或 SKAD 模式**。</li><li>将 "启用高级隐私回调" 写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>基于可用宏的高级隐私回调结构</li><li>链接更新：新参数及其对应的宏</li></ul></li></ol> |
| <span id="enable-skadnetwork-postback"></span>启用 SKAdNetwork 回调 | 设置 SKAdNetwork 集成，并能够通过回调从 AppsFlyer 接收解码数据。<br /><br /><Anchor target="_blank" href="/partners/zh/docs/skan-integration-guide-for-ad-networks">有关 SKAdNetwork 回调的更多信息。</Anchor> | 在 AppsFlyer 仪表板中遵循 <Anchor target="_blank" href="/partners/zh/docs/self-serve-integration-management-for-ad-networks">SKAdNetwork 回调配置的说明</Anchor>。<br /><br />如果出现任何问题：<ol><li>从小部件中选择 **高级隐私或 SKAD 模式**。</li><li>将 "启用高级隐私回调" 写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>基于 KB 中可用宏的 SKAdNetwork 回调结构</li><li>Apple SKAdnetwork id</li></ul></li></ol> |
| <span id="update-the-logo"></span>更新徽标 | 添加徽标或替换当前徽标。 | <ol><li>确保您拥有合适的徽标文件：(200x50px transparent PNG)</li><li>现在，转到AppsFlyer控制面板。</li><li>点击右上角的电子邮件地址 > 选择 **合作伙伴设置**。</li><li>转到 **个人资料** 选项卡 > **公司徽标**。</li><li>点击 **上传** 图标。</li><li>选择徽标文件并确认。</li><li>点击 **保存** 在页面底部。徽标会立即更新。</li></ol> |
| <span id="update-the-click-attribution-url"></span>更新点击归因 URL | 更新广告客户用于与您进行活动的点击归因 URL。  <br /><Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters">有关归因链接的更多信息。</Anchor> | <ol><li>从小部件中选择 **默认模式**。</li><li>将 "更新点击归因 URL" 写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>新参数及其对应的宏。</li></ul></li><li>在 点击归因 URL 更新后，询问广告客户更新的归因链接 URL。</li></ol> |
| <span id="create-update-partner-dashboard-login-email"></span>更新合作伙伴仪表板登录邮箱 | 登录 AppsFlyer 账户、检查仪表板数据和从 AppsFlyer 仪表板导出报告所需。 | 如果用户尚未在您的账户中存在，<Anchor target="_blank" href="/partners/zh/docs/user-management-for-ad-networks#creating-a-user">这是添加他们的方法</Anchor>。<ol><li>确保新用户是 <Anchor target="_blank" href="/partners/zh/docs/user-management-for-ad-networks#becoming-an-active-user">活跃</Anchor> 的。</li><li>从小部件中选择 **默认模式**。</li><li>将 "更新合作伙伴仪表板登录" 写为工单标题。</li><li>分享以下信息：<ul><li>当前账户邮箱</li><li>新账户邮箱</li><li>您在账户中的角色（管理员/团队成员/非团队成员）</li></ul></li><li>在仪表板登录已更新后，您将收到通知。然后您可以使用更新的邮箱重置密码。</li></ol> |
| <span id="disable-integration"></span>停用对接 | 如果集成被禁用，安装和应用内事件将不会归因于被禁用的集成。<br /><br />**注意**：在禁用之前，请确认广告客户已停止使用该集成。 | <ol><li>从小部件中选择 **默认模式**。</li><li>将“禁用集成”写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>要禁用哪个集成：安装，还是应用内事件</li></ul></li></ol> |
| <span id="add-new-dashboard-parameter"></span>添加新的仪表板参数 | 允许广告客户在 AppsFlyer 广告客户仪表板中提供特定参数，以便通过回调接收。 | <ol><li>从小部件中选择 **默认模式**。</li><li>将“添加新的仪表板参数”写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>新的仪表板参数名称</li><li>接收参数——如果您想通过安装或应用内事件回调接收它</li><li>[推荐] 将在 AppsFlyer 广告客户仪表板的参数字段旁边显示的参数描述的工具提示</li></ul></li></ol> |
| <span id="provide-the-postback-template-to-the-partner"></span>向合作伙伴提供回调模板 | 审查您当前的集成 | <ol><li>从小部件中选择 **默认模式**。</li><li>将“提供回调模板”写为工单标题。</li><li>分享以下信息：<ul><li>您的 PID 或登录用户名</li><li>指定您想检查的回调：安装回调、应用内事件回调或拒绝回调</li></ul></li></ol> |
| <span id="implement-click-signing"></span>实施点击签名 | 广告平台可以在点击中添加签名验证，这样作弊点击就不会被归因到该渠道，避免承担作弊风险。 | 按照<Anchor target="_blank" href="/partners/zh/docs/click-signing-for-ad-networks">这些说明</Anchor>在您这边实施点击签名。<br />如有疑问：<ol><li>从小部件中选择 **默认模式**。</li><li>将“点击签名”写为工单标题。</li><li>分享您的 PID 或登录用户名。</li></ol> |

<div data-zendesk-anchors="h_01HEPXV5HY3Q502Y8WJAV7HTME=%E9%87%8D%E8%A6%81%E6%8F%90%E7%A4%BA" />
