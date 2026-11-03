---
title: 广告平台的成本导入说明
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2026-10-14T10:02:45Z'
  id: 360002868097
  locale: zh-cn
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/zh-cn/articles/360002868097
---
> **概要：** 了解广告网络如何通过 CSV 文件直接向 AppsFlyer 报告广告主的活动成本。

## 广告平台的成本导入说明

![AdspendIngestion.jpg](https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg)

#### 概览

* 准备一个包含广告支出详细信息的 CSV 文件，如下所示：
  * 支出日期
  * 应用 ID（如果应用属于同一所有者，文件中允许多个应用）
  * 媒体来源（每个文件允许一个）
  * Campaign name
  * 支出金额
  * [可选] 地理位置
  * [可选] 货币（默认 USD）
* 通过电子邮件/文件上传使用 AppsFlyer 中的广告网络账户将文件提交给 AppsFlyer。   
  **注意：**
  * 在您第一次提交文件之前，广告主必须授予您，广告网络，成本导入权限。每个应用只需执行一次，这是一个非常简短的过程。
  * 一旦文件上传，就无法恢复。
* 监控并检查文件中是否没有发现错误。

### 为广告网络提交广告支出文件

* 使用上传或电子邮件方法来导入广告支出文件。
* [最佳实践] 最初使用上传方法，因为它更容易解决 CSV 格式问题。
* 广告网络无法导入代理成本数据；只有广告主可以。

#### 通过文件上传提交

**通过上传提交成本导入文件：**

1. [对于您合作的每个应用，您需要执行一次] <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-permissions-for-ad-networks">请广告主授予您成本导入权限</Anchor>.
2. <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#prepare-csv-file-with-cost-data">使用此格式和架构准备CSV文件</Anchor>。
3. 点击这里<Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">登录到您的AppsFlyer广告网络账户</Anchor>。
4. <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#upload-file">上传并摄取文件</Anchor>。
5. 在AppsFlyer仪表板中，监控摄取情况：

   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">状态</Anchor>
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#matched-rows">匹配行</Anchor>
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">成本导入操作</Anchor>
6. 其他操作
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">覆盖先前的摄取</Anchor>
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">恢复（取消）</Anchor>

#### 通过电子邮件提交

**通过电子邮件提交成本导入文件：**

1. [对于您合作的每个应用程序，您需要执行此操作一次]<Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-permissions-for-ad-networks">请广告主授予您成本导入权限</Anchor>。
2. <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#prepare-csv-file-with-cost-data">使用此格式和架构准备CSV文件</Anchor>。
3. 如果您没有成本导入令牌（在您通过电子邮件发送文件时需要）：
   * 点击这里<Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">登录到您的AppsFlyer广告网络账户</Anchor>。
   * 获取Ad Spend token 注意：所有广告主共用同一个token。
4. 通过<Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#email-file">电子邮件提交文件</Anchor>
5. AppsFlyer会通过邮件发送状态报告，说明数据接入是否成功或是否发现任何问题。**注意**：如果未收到状态邮件，请查看<Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">成本导入仪表板</Anchor>.
6. 在AppsFlyer仪表板中监控摄取情况：

   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">状态</Anchor>
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#matched-rows">匹配行</Anchor>
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">成本导入操作</Anchor>
7. 其他操作
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">覆盖先前的摄取</Anchor>
   * <Anchor target="_blank" href="/marketers/zh/docs/import-cost-data#cost-import-dashboard">恢复（取消）</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E7%9A%84%E6%88%90%E6%9C%AC%E5%AF%BC%E5%85%A5%E8%AF%B4%E6%98%8E h_01HX94WSX07YEG40X66TMRFJGA=%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E7%9A%84%E6%88%90%E6%9C%AC%E5%AF%BC%E5%85%A5%E8%AF%B4%E6%98%8E overview=%E6%A6%82%E8%A7%88 h_01HX94WSX0HR2KTGRT7MQ481Y6=%E6%A6%82%E8%A7%88 submitting-ad-spend-files-for-ad-networks=%E4%B8%BA%E5%B9%BF%E5%91%8A%E7%BD%91%E7%BB%9C%E6%8F%90%E4%BA%A4%E5%B9%BF%E5%91%8A%E6%94%AF%E5%87%BA%E6%96%87%E4%BB%B6 h_01HX94WSX0G429FTHKYCG07BB9=%E4%B8%BA%E5%B9%BF%E5%91%8A%E7%BD%91%E7%BB%9C%E6%8F%90%E4%BA%A4%E5%B9%BF%E5%91%8A%E6%94%AF%E5%87%BA%E6%96%87%E4%BB%B6 submission-by-file-upload=%E9%80%9A%E8%BF%87%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%8F%90%E4%BA%A4 h_01HX94WSX0ENTJEDMXWRHDCP0D=%E9%80%9A%E8%BF%87%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%8F%90%E4%BA%A4 submission-by-email=%E9%80%9A%E8%BF%87%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6%E6%8F%90%E4%BA%A4 h_01HX94WSX0HVTMFQQ0NMW0VSKP=%E9%80%9A%E8%BF%87%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6%E6%8F%90%E4%BA%A4" />
