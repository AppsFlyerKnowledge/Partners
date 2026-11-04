---
title: 将用户重定向到应用商店
metadata:
  keywords:
    - clicks
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2018-04-30T08:08:25Z'
  edited_at: '2026-10-14T09:59:21Z'
  id: 360000807629
  locale: zh-cn
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/zh-cn/articles/360000807629
---
> **概要：** 了解在广告投放后将用户重定向到应用商店的选项，以及如何将参与数据发送到AppsFlyer。

<div id="overview" />

## 速览

AppsFlyer通过多种方式接收参与数据（点击和展示）以进行归因：

* 用户**点击**广告并[被重定向到AppsFlyer](#通过appsflyer重定向的用户)，然后再到应用商店。
* 用户**点击或查看**广告并[直接发送到应用商店](#广告网络直接发送的用户)，同时**归因链接从服务器发送到AppsFlyer**。

在这两种情况下，使用常规的<Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters">归因链接结构和参数</Anchor>。

<div id="note" />

> 📘 **注意**
>
> 对于SRN，数据通过专用API接收

<div id="users-redirected-via-appsflyer" />

## 通过AppsFlyer重定向的用户

当广告被点击时，用户被引导到AppsFlyer，然后通过以下流程重定向到应用商店：

1. 用户被重定向到AppsFlyer
2. AppsFlyer记录点击
3. AppsFlyer将用户重定向到应用商店
4. 用户安装应用
5. AppsFlyer归因安装

<div id="users-sent-directly-by-the-ad-network" />

## 广告网络直接发送的用户

当广告被点击时，用户通过广告网络被引导到应用商店，最小化重定向次数：

1. 用户被发送到应用商店
2. 广告网络从设备向AppsFlyer报告参与数据
3. 用户安装应用
4. AppsFlyer归因安装

<div id="sending-engagement-data-to-appsflyer" />

### 将参与数据发送到AppsFlyer

直接将用户发送到应用商店通过减少重定向次数改善了他们的体验。它还确保了安装的准确归属，并能够提供高质量的流量。

广告网络只能直接从用户的设备向 AppsFlyer 报告点击和展示。

<div id="timing-of-sending-redirects" />

#### 发送重定向的时机

为了防止广告网络的归属和收入损失，点击和展示必须实时发送给 AppsFlyer：

* 一旦广告投放，必须报告展示 URL。
* 一旦用户点击广告，必须报告点击 URL。

<div data-zendesk-anchors="overview=%E9%80%9F%E8%A7%88 h_01HDY3CARC0A9504XGMJHYHGY4=%E9%80%9F%E8%A7%88 h_01HDY3CARCZK06C5XHEQFQYA8W=%E6%B3%A8%E6%84%8F redirect-users-via-appsflyer=%E9%80%9A%E8%BF%87appsflyer%E9%87%8D%E5%AE%9A%E5%90%91%E7%9A%84%E7%94%A8%E6%88%B7 01HDYFGYW3FDR64C54KKPXRHDF=%E9%80%9A%E8%BF%87appsflyer%E9%87%8D%E5%AE%9A%E5%90%91%E7%9A%84%E7%94%A8%E6%88%B7 send-users-directly-by-the-ad-network=%E5%B9%BF%E5%91%8A%E7%BD%91%E7%BB%9C%E7%9B%B4%E6%8E%A5%E5%8F%91%E9%80%81%E7%9A%84%E7%94%A8%E6%88%B7 01HDYFH8ZCSP2SN4ZYQQVG7EED=%E5%B9%BF%E5%91%8A%E7%BD%91%E7%BB%9C%E7%9B%B4%E6%8E%A5%E5%8F%91%E9%80%81%E7%9A%84%E7%94%A8%E6%88%B7 send-engagement-data-to-appsflyer=%E5%B0%86%E5%8F%82%E4%B8%8E%E6%95%B0%E6%8D%AE%E5%8F%91%E9%80%81%E5%88%B0appsflyer h_01HDYGSEFHVF8ZD43XCVNGYT9N=%E5%B0%86%E5%8F%82%E4%B8%8E%E6%95%B0%E6%8D%AE%E5%8F%91%E9%80%81%E5%88%B0appsflyer timing-of-sending-redirects=%E5%8F%91%E9%80%81%E9%87%8D%E5%AE%9A%E5%90%91%E7%9A%84%E6%97%B6%E6%9C%BA h_01HDXXDDXDEP43YHE3GF81BSKV=%E5%8F%91%E9%80%81%E9%87%8D%E5%AE%9A%E5%90%91%E7%9A%84%E6%97%B6%E6%9C%BA" />
