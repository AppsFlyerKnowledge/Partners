---
title: 关于概率建模
metadata:
  keywords:
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2025-10-21T14:32:11Z'
  edited_at: '2026-10-14T10:00:51Z'
  id: 40188089592209
  locale: zh-cn
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/zh-cn/articles/40188089592209
---
> **概要：** 本文介绍将为您介绍如何设置广告交互数据，以便在无法使用确定性信号时启用概率性模型。

<div id="about-probabilistic-modeling" />

## 关于概率建模

概率建模是一种保护隐私的统计方法。AppsFlyer通过概率建模，报告应用开发者营销广告系列的表现。通过该方法，AppsFlyer为应用开发者生成广告系列层级的汇总数据报告。

**功能特点**

* 使用统计学原理，而不是通过唯一ID进行匹配。
* 在无法获取引荐来源信息或广告ID时，AppsFlyer会使用概率建模作为备用方法。由于确定性归因法可以把点击行为匹配到追踪码或ID，因此具有更高的优先级。也就是说，在归因窗口期内，如果条件允许，我们会先使用确定性归因法。

<div id="when-is-probabilistic-modeling-used" />

### 适用场景

除非客户另行配置，否则当无法获取确定性数据时，AppsFlyer会启用概率建模，包括以下情况：

* Web-to-App转化
* 跨设备路径（例如用户在桌面端看到广告后，在移动端完成激活）
* CTV、PC或主机端环境等无法使用确定性归因的场景

<div data-zendesk-anchors="about-probabilistic-modeling-attribution=%E5%85%B3%E4%BA%8E%E6%A6%82%E7%8E%87%E5%BB%BA%E6%A8%A1 h_01K83JWQ84H0P1WABG939X55KD=%E5%85%B3%E4%BA%8E%E6%A6%82%E7%8E%87%E5%BB%BA%E6%A8%A1 when-is-probabilistic-modeling-used=%E9%80%82%E7%94%A8%E5%9C%BA%E6%99%AF h_01K83JWQ8412VK2ZN39CQ5TJEZ=%E9%80%82%E7%94%A8%E5%9C%BA%E6%99%AF" />
