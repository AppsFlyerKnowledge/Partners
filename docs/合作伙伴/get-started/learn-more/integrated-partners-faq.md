---
title: 对接渠道：
metadata:
  keywords:
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
  created_at: '2021-09-02T09:33:34Z'
  edited_at: '2026-10-14T10:09:25Z'
  id: 4406549295249
  locale: zh-cn
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/zh-cn/articles/4406549295249
---
> **概要**：


<span id="account-and-dashboard"></span>重要提示！


1. 按<Anchor target="_blank" href="/partners/zh/docs/integration-requests-for-partners#create-update-partner-dashboard-login-email">此文档</Anchor>中的说明完成相关操作。


| Reason | 解决方法 |
| --- | --- |
|  |  |


| Reason | 解决方法 |
| --- | --- |
| 由广告主（应用所有者）配置广告平台对接时，相关平台才能看到这些设置。 |  |


1. 按<Anchor target="_blank" href="/partners/zh/docs/self-serve-integration-management-for-ad-networks#高级隐私保护和skan回传">此文档</Anchor>中的说明完成相关操作。


* <Anchor target="_blank" href="/partners/zh/docs/getting-started-onboarding-guide-for-ad-networks#对接认证期">对接认证期</Anchor>



* <span id="partner-permissions"></span>留存报告
* Protect360面板


| Reason | 解决方法 |
| --- | --- |
|  | <ul><li>配置对接</li></ul> |


| Reason | 解决方法 |
| --- | --- |
|  | **请注意：** |



<table><thead><tr><th><span id="data-postbacks-and-reports"></span>Reason</th><th>解决方法</th></tr></thead><tbody><tr><td></td><td> </td></tr><tr><td></td><td><ul><li><ol><li>从AppsFlyer的侧边栏中选择<strong>协作</strong> &gt; <strong>活跃对接</strong>，然后选择相关渠道。</li><li> </li><li> </li></ol></li><li> </li></ul></td></tr><tr><td></td></tr></tbody></table>


| Reason | 解决方法 |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |


| Reason | 解决方法 |
| --- | --- |
|  |  |
|  |  |
|  |  |


| Reason | 解决方法 |
| --- | --- |
|  |  |


| Reason | 解决方法 |
| --- | --- |
|  |  |


| Reason | 解决方法 |
| --- | --- |
|  |  |
|  |  |
|  |  |


| Reason | 解决方法 |
| --- | --- |
|  |  |
|  |  |


| Reason | 解决方法 |
| --- | --- |
|  |  |
|  | 如果用户没有应用... |


| Reason | 解决方法 |
| --- | --- |
|  |  |
|  |  |


只有广告主帐户操作的设置才可以对广告平台可见，代理帐户不可以。

> 📄 **示例**
>
> Yuval是com.fused应用的推广人，这个应用是Sonnet广告平台客户的应用。Yuval把af\_purchase事件设置为回传给Sonnet的事件，当归因给Sonnet的用户产生购买事件时，这些事件就会回传到Sonnet。 **Sava是 com.fused应用的授权代理，也 Sonnet平台配置为合作平台，并把 af\_completeregistration 事件设置为回传事件。
>
> 当Sonnet登录到com.fused的面板时，他们看到只有af\_purchase事件有映射给他们，但不是af\_completeregistration 事件。但是，当归因给Sava的用户执行注册事件后，这些注册事件就会以 af\_completeregistration 事件发送给 Sonnet。**


如果回传中缺少点击数据，请确保AppsFlyer链接中含有所有你想要回传的数据。请参阅我们的 <Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters">归因链接指南</Anchor> 来了解更多信息。


需要把AppsFlyer归因链接作为您服务器上的跳转 URL。然后需要用您服务器自己的链接来做一个完整的测试。

确保把贵平台归因链接的参数映射到 AppsFlyer 的归因链接。


<Accordion title="">

</Accordion>


|  | 解决方法 |
| --- | --- |
|  |  |
| click\_capping |  |
|  |  |
|  |  |
|  | 不适用 |


## Protect360

<div data-zendesk-anchors="h_01HKW6K6RFAEX8SKMAWSCKC3AD=account-and-dashboard h_01HW8J4Q9J83ANG3VX2T2V0JMH=partner-permissions h_01HKW6K6RFHBVQMMWZYCE0VWB6=data-postbacks-and-reports h_01HKW6K6RGCRPTK1B78JH94WR4=%E7%A4%BA%E4%BE%8B h_01HKW6K6RHWS457Q0DAKK0R1Q6=protect360" />
