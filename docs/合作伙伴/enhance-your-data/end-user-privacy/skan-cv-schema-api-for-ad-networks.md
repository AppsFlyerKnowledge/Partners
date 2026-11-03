---
title: 广告平台的SKAN转化值映射构架API
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2026-10-14T10:12:17Z'
  id: 11705009866001
  locale: zh-cn
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/zh-cn/articles/11705009866001
---
> **概要**：概要：本文介绍了广告平台应如何查看广告主设置的SKAN转化值映射构架。

## 广告平台的SKAN转化值映射构架API

在SKAdNetwork（SKAN）归因场景中，广告主需要根据用户激活后指定时间段（即窗口期）内的行为设置转化值（CV），从而对用户质量分级。<Anchor target="_blank" href="/marketers/zh/docs/skadnetwork-skan-solution-guide">详情请见SKAN解决方案指南。</Anchor>

在SKAN归因中，iOS会向发布相关广告的渠道发送回传，从而完成数据上报。从iOS 15开始，广告主还可以让iOS直接将回传发送到AppsFlyer。

该API可向广告平台提供CV-归因事件-值的映射构架，帮主广告平台对其接收到的回传进行解析。

该API会以嵌套型的JSON格式返回数据。每个应用都具有其单独的映射构架。分CV的映射配置包含在conversion\_value\_mapping数组中。

如需使用该API，请让您的开发人员按照<Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">广告平台的SKAN转化值映射构架指南</Anchor>进行操作。如需查看键列表及对应说明，请在模拟器中点击200。

**请注意**：

* 转化值的范围如下：
  * SKAN 4中窗口1的精细值：0-63。21
  * SKAN 4中窗口1、2、3的粗略值：low（低）、medium（中）、high（高）。
  * 使用SKAN 3及以下0-63
* 广告主可以随时更改其CV映射。
* 广告平台必须每天使用该API查询映射构架，以确保及时更新。

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E7%9A%84skan%E8%BD%AC%E5%8C%96%E5%80%BC%E6%98%A0%E5%B0%84%E6%9E%84%E6%9E%B6api" />
