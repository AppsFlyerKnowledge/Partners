---
title: 广告平台自助对接管理指南
metadata:
  keywords:
    - postbacks
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2021-03-15T10:03:41Z'
  edited_at: '2026-10-14T10:14:41Z'
  id: 360018512658
  locale: zh-cn
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/zh-cn/articles/360018512658
---
> **概要**：概要：本文主要说明了广告平台应如何通过AppsFlyer面板设置并管理其对接配置。

<Embed title="广告平台自助对接管理指南" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/9kvwrhnzjo" providerUrl="https://fast.wistia.com" />

**前期准备：**

* 您必须先获取AppsFlyer的登陆证书（即用户名和密码），才能管理归因链接和回传配置。如需<Anchor target="_blank" href="/partners/zh/docs/getting-started-onboarding-guide-for-ad-networks">创建渠道账户</Anchor>，请让相关广告主向您<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#在appsflyer中添加新的对接渠道">发送邀请</Anchor>。
* AF仅向2022年2月1日之后入驻的渠道开放归因链接和回传默认配置管理功能。
* 请确认您的服务器符合以下条件，可以接收回传：
  * AppsFlyer服务器的<Anchor target="_blank" href="/marketers/zh/docs/appsflyer-server-ip-address-ranges-allowlisting">IP地址</Anchor>已在您的防火墙和安全系统中加白，确保AF服务器与端点之间的数据传输保持畅通。
  * TLS版本 TLS 1.2+，详情请见<Anchor target="_blank" href="/marketers/zh/docs/appsflyer-https-ssl-encryption-policy-support#outgoing-messages-appsflyer-as-client">密码列表</Anchor>。
  * 端口 21

## 管理对接

1. 登入您的AppsFlyer渠道账户。
2. 点击右上角的下拉菜单 >**回传管理**。

## 归因链接

归因链接是渠道对接中最重要的组成部分，因为AppsFlyer是通过归因链接记录用户与广告的互动情况的。归因链接是广告背后的链接，用户点击广告时，实际上点击的是一条归因链接。

因此归因链接是渠道对接中必须配置的内容。

**请按以下步骤配置归因链接：**

1. 进入**归因链接**标签页，在归因链接中添加相关参数：
   * 参数名称
   * **宏**：添加宏以填充参数值。
   * **链接参数**：勾选需要在链接中添加的参数。

   > 🚧 **重要提示！**
   >
   > * 添加与广告系列及广告相关的参数可以为广告主提供更为丰富全面的投放效果数据。
   > * **子渠道ID**是必须配置的参数。
   > * 广告主需以该链接为基础，针对具体应用完成渠道对接，并可在该链接其中添加其他参数。
   > * 系统会在归因链接中自动添加应用ID、回溯窗口期时长以及您的渠道ID，因此您无需在链接模板中添加这些参数。

2. <strong>【可选】</strong>在AppsFlyer预定义参数之外添加自定义参数。
3. 查看链接预览，检查各项配置是否正确无误。
4. 点击**保存**。

如需进一步了解相关信息，请参考<Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters">归因链接和可用参数说明</Anchor>。

如出现任何问题，请通过<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系我们。

## 默认回传

回传是包含宏的URL，AppsFlyer会填充这些宏，并在每次转化发生后将其实时发送到您的服务器。回传中可仅包含您的平台带来的转化，也可同时包含其他平台的转化，具体取决于您的回传配置。

**请按以下方式配置默认回传：**

1. 输入**端点地址**。回传数据会发送到这些端点。请输入激活和/或应用内事件的相关URL。必须配置激活回传URL才能启用对接。
2. 在回传中添加参数：
   * 参数名称
   * **渠道映射参数**：即渠道侧接收到的对应参数。
   * **参数值**（适用于某些参数）：选择参数值的格式。如在布尔型参数下可选的参数值格式为"true"/"false"或1/0。
   * **激活**：勾选需要在激活回传中传递的参数。
   * **应用内事件**：勾选需要在应用内事件回传中传递的参数。

   <Anchor target="_blank" href="/partners/zh/docs/postback-macros-for-ad-networks">回传宏完整列表</Anchor>

   > 🚧 **重要提示！**
   >
   > * 如需区分正常事件和被拦截的回传，请配置<Anchor target="_blank" href="/partners/zh/docs/postback-macros-for-ad-networks#激活应用内事件和被拒绝事件中的宏">被拦截的回传宏</Anchor>。
   > * 如需启用被拦截的激活/应用内事件回传，请在默认回传模板的末尾添加以下参数：
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`  
   >     **请注意：** blocked-reason-value请注意：如果您启用了高级隐私保护（Advanced Privacy）回传，需要在Advanced Privacy模板的末尾也添加上述参数。

4. 查看回传模板预览，检查各项配置是否正确无误。
5. 点击**保存**。

<Anchor target="_blank" href="/marketers/zh/docs/in-app-event-postback-configuration">戳这里进一步了解回传信息和示例。</Anchor>

如出现任何问题，请通过<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系我们。

## 高级隐私保护和SKAN回传

您必须先创建归因链接和默认回传，才能配置高级隐私保护和SKAN回传。

**请按以下步骤管理回传配置：**

1. 选择回传类型：
   * <Anchor target="_blank" href="/partners/zh/docs/advanced-privacy-guide-postback-macros-for-ad-networks">高级隐私保护</Anchor>（AP）回传。
   * <Anchor target="_blank" href="/partners/zh/docs/skan-integration-guide-for-ad-networks">SKAN</Anchor>回传。
2. 激活配置工具。
3. <strong>【仅适用于SKAN回传配置】</strong>输入您的SKAdNetwork ID。这是一个必填字段，必须输入有效ID才能保存配置。
4. 输入**端点地址**。回传数据会发送到这些端点。请输入激活和/或应用内事件的相关URL。
5. 添加回传参数：
   * 参数名称
   * 如在布尔型参数下可选的参数值格式为"true"/"false"或1/0。
   * **转化**：激活：勾选需要在激活回传中传递的参数。
   * **应用内事件**：应用内事件：勾选需要在应用内事件回传中传递的参数。

   <Anchor target="_blank" href="/partners/zh/docs/skan-integration-guide-for-ad-networks#接收appsflyer发送的数据">SKAN回传宏</Anchor>列表

   <Anchor target="_blank" href="/partners/zh/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification">高级隐私保护回传宏</Anchor>列表

   > 🚧 **重要提示！**
   >
   > * 如需启用被拦截的激活/应用内事件回传，请在默认回传模板的末尾添加以下参数：
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`
   > * 如需启用高级隐私保护（Advance Privacy）的被拦截回传，必须先将上述参数添加到[默认回传](/docs/self-serve-integration-management-for-ad-networks#默认回传)
   > * 将上述参数同时添加到默认回传和Advanced Privacy回传（若启用）后，即完成了被拦截激活/应用内事件回传的启用。

7. 查看回传模板预览，检查各项配置是否正确无误。
8. 点击**保存**。  
   请注意：保存回传配置后，新配置会立刻生效。

如出现任何问题，请通过<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">渠道支持微件</Anchor>联系我们。

<div data-zendesk-anchors="accessing-integration-management=%E7%AE%A1%E7%90%86%E5%AF%B9%E6%8E%A5 h_01H9FCSTYR157CCJWTYSNE9JQ0=%E7%AE%A1%E7%90%86%E5%AF%B9%E6%8E%A5 attribution-link=%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 h_01H9FCSTYR6HRSF9F8KCR4B3X7=%E5%BD%92%E5%9B%A0%E9%93%BE%E6%8E%A5 h_01H9FCSTYR4Q1985DTHNE1M1CC=%E9%87%8D%E8%A6%81%E6%8F%90%E7%A4%BA default-postback=%E9%BB%98%E8%AE%A4%E5%9B%9E%E4%BC%A0 h_01H9FCSTYR2WX0M0ZW3B22EKBM=%E9%BB%98%E8%AE%A4%E5%9B%9E%E4%BC%A0 h_01H9FCSTYSEP367WAAKCFHZT58=%E9%87%8D%E8%A6%81%E6%8F%90%E7%A4%BA-1 advanced-privacy-and-skan-postbacks=%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%92%8Cskan%E5%9B%9E%E4%BC%A0 h_01H9FCSTYSRKBMYR2BYNQJJKVM=%E9%AB%98%E7%BA%A7%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%E5%92%8Cskan%E5%9B%9E%E4%BC%A0 h_01H9FCSTYSEJD59AWCFNXDZMYW=%E9%87%8D%E8%A6%81%E6%8F%90%E7%A4%BA-2" />
