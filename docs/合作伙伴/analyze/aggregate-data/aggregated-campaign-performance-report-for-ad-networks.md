---
title: 为广告平台提供汇总广告活动业绩报告
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketing Analytics
    - Ad Networks
  created_at: '2021-05-30T12:34:03Z'
  edited_at: '2026-10-14T10:04:35Z'
  id: 360020834237
  locale: zh-cn
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/zh-cn/articles/360020834237
---
> **概要**：概览：广告平台将汇总业绩报告加载到他们的BI系统中，以计算广告活动绩效指标，如7天留存率KPI。

<div id="aggregated-campaign-performance-report" />

## 汇总广告活动业绩报告

此报告提供广告活动绩效数据，包括执行给定事件的独特用户数量。您（广告平台），使用您BI系统中的数据，在广告主KPI的背景下，计算广告活动的绩效指标。该报告每天可通过<Anchor target="_blank" href="/partners/zh/docs/data-locker-for-partners">Data Locker for Partners</Anchor>获取

**为什么需要报告？**

在iOS 14.5之前，AppsFlyer发送给您的回传包含足够数据来计算独特的用户事件指标。

从iOS 14.5开始，以及广告主采用汇总高级隐私（AAP），非同意用户的回传不包括用户标识符。由于缺乏标识符，无法计算出独特的用户指标，例如7天的留存率。缺乏独特的用户指标损害您优化广告活动的能力，以及与广告主制定共同留存目标的能力。

报告包含哪些内容？

使用所报告的特征提供具有最佳粒度的指标，并具有以下绩效指标：

* 收入
* 给定事件的执行次数
* 执行事件的唯一用户数量
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vS89RlkFIss7uARroJcOcX1rU6gUmZ2ySYwfTprg9GaA2BYnvDPVqWmOicea1wrBnNuGgEuLPwzL_ac/pub?gid=0&single=true&output=csv">报告示例</Anchor>

如何获取报告？

* 通过Data Locker for Partners提供。<Anchor target="_blank" href="/marketers/zh/docs/about-data-freshness-and-timezone-support#daily-processing">每日UTC时间</Anchor>更新报告。
* 广告主必须先在面板中为您开放必要[权限](/docs/aggregated-campaign-performance-report-for-ad-networks#permission-to-get-aggregated-performance-data)，然后我们才会与您共享相关数据。

<div id="about-the-report" />

## 关于报告

<div id="report-structure" />

<Accordion title="报告结构">

<div id="dimensions" />

#### 维度

<Table>
  <thead>
    <tr>
      <th>
        字段名称
      </th>
      <th>
        说明
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        app\_id
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        * 可能的值：安装、再次互动、重新归因
        * 等效的回传宏：is\_retargeting
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        可能出现的值包括click（点击）、impression（展示）、pre-installed（预装）、unknown（未知）、tv、null
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        归因事件后经过的天数。  
        最多可以显示180天内的趋势。

        小贴士：您可以使用该数据来计算留存和KPI天数。
      </td>
    </tr>
    <tr>
      <td>
        event\_date
      </td>
      <td>
        事件发生日期。

        格式：yyyy-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        conversion\_date
      </td>
      <td>
        格式：yyyy-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        event\_name
      </td>
      <td>
        用于标识事件。有些事件名称具有特定含义，而有些则与广告主在应用中设置的应用内事件有关。

        | event\_name | 用户行为 |
        | --- | --- |
        | af\_conversion | 用户转化。使用conversion\_type来识别转化类型，即激活、再互动、再归因或再互动。 |
        | 互动次数 | 用户打开应用 |
        | af\_uninstall | 用户卸载应用 |
        | 广告主定义的应用内事件 | 在应用程序中执行应用内事件。应用内事件名称未映射到合作伙伴事件名称。 |
      </td>
    </tr>
    <tr>
      <td>
        campaign
      </td>
      <td>
        广告层次结构中的一个层级
      </td>
    </tr>
    <tr>
      <td>
        campaign\_id
      </td>
      <td>
        广告层次结构中的一个层级。
      </td>
    </tr>
    <tr>
      <td>
        adset
      </td>
      <td>
        广告层次结构中的一个层级。
      </td>
    </tr>
    <tr>
      <td>
        adset\_id
      </td>
      <td>
        广告层次结构中的一个层级。
      </td>
    </tr>
    <tr>
      <td>
        ad
      </td>
      <td>
        广告层次结构中的一个层级。
      </td>
    </tr>
    <tr>
      <td>
        ad\_id
      </td>
      <td>
        广告层次结构中的一个层级。
      </td>
    </tr>
    <tr>
      <td>
        channel
      </td>
      <td>
        广告层次结构中的一个层级
      </td>
    </tr>
    <tr>
      <td>
        site\_id
      </td>
      <td>
        广告层次结构中的一个层级
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        用于识别和删除再营销的数据
      </td>
    </tr>
    <tr>
      <td>
        country\_code
      </td>
      <td>
        从用户IP地址派生
      </td>
    </tr>
    <tr>
      <td>
        agency
      </td>
      <td>
        如果空白，则没有关联的代理
      </td>
    </tr>
    <tr>
      <td>
        Keywords（关键词）
      </td>
      <td>
        [可从2022年4月27日开始使用] 用户在线搜索中使用的单词。由广告平台上报。
      </td>
    </tr>
    <tr>
      <td>
        Keyword ID （关键词ID）
      </td>
      <td>
        由广告平台上报的关键词ID【该字段自2022年4月27起可用】。
      </td>
    </tr>
  </tbody>
</Table>

<div id="metrics" />

#### 指标

| 特点 | 字段 | 完成事件的唯一用户 |
| --- | --- | --- |
| 独立用户数 | unique\_users | 完成事件的独立用户数 |
| 收入 | revenue\_usd | 累计收入以美元计算。如100.56美元会显示为100.56。 |
| event\_count | event\_count | 事件发生次数 |

</Accordion>

<div id="bi-developer-considerations" />

<Accordion title="BI开发者注意事项">

**报告中的数据范围**

报告包含用户归因、安装、重新归因和再次互动，及其相关的应用内事件。

在您的数据消费过程中，您必须使用逻辑在广告活动类型之间拆分数据。含义，用户归因（安装）和再营销（再次互动）。为此，请使用conversion\_type和is\_primary\_attribution字段。另请参见<Anchor target="_blank" href="/marketers/zh/docs/resolve-retargeting-double-attribution">再营销事件的双重归因</Anchor>。

**字段级注意事项**

* 您可以通过归因后的天数来计算留存指标。
* 您可以使用广告系列名称和广告系列ID这两个维度来计算独立用户数：在不用考虑广告系列名称颗粒度的情况下，将广告系列ID的独立用户数相加可以得出准确的指标。
* 您可以使用广告层次结构字段来汇总数据。
* 应用内事件使用广告主的事件名称，而不是映射到您的事件名称。要求广告主向您提供映射，或在控制面板中查看。<Anchor target="_blank" href="/marketers/zh/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">合作伙伴应用内事件映射</Anchor>。
* 以美元计算的收入使用事件当天的汇率计算。
* 广告收入事件包含在可用的地方，但更新滞后达5天。

**常规注意事项**

* 数据时效性：每天，从08:00 UTC开始。数据会写入Data Locker的h=23文件夹中。
* 可用数据是由AppsFlyer归因的用户路径数据。意思是，iOS回传报告的SKAdNetwork并不包含在此数据集中。
* 数据包含在包含多个应用程序的文件中。使用app\_id字段来标识应用程序。
* 如果您没有获取给定应用程序的数据，请确认广告主是否已授予您必要的权限。

</Accordion>

<div id="retention-report-considerations" />

<Accordion title="保留率报告注意事项">

要创建留存指标，例如留存第 7 天，请通过在以下字段上设置过滤器来实现：

* days\_post\_install=7
* event\_name=af\_session
* 根据需要的conversion\_type
* 为防止包含<Anchor target="_blank" href="/marketers/zh/docs/resolve-retargeting-double-attribution">重复的再营销事件</Anchor>，请选择 is\_primary\_attribution=true或使用conversion\_type来限制数据集的安装。
* 分组依据：广告活动和其他需要的特征。
* 总和：unique\_users\_count

通过添加或删除特征，您可以获得不同粒度的指标。

</Accordion>

<div id="permissions" />

## 授权

您（广告平台）必须要求广告主授予您此处列出的权限。广告主必须为每个应用程序执行一次该一步骤。

<div id="permission-to-get-aggregated-performance-data" />

<Accordion title="获取汇总业绩数据的权限">

由代理指定（启用）的广告平台：代理无法授权，必须让广告主代其授权。

**为了让广告平台获取汇总业绩数据：**

1. 在AppsFlyer后台左侧的菜单栏中，选择**协作** > 对接渠道。
2. 搜索并选择相关渠道。
3. 点击**设置对接**。界面会跳转到对接设置页。
4. 确认启用该渠道开关已开启。如果该开关未打开，AppsFlyer就不会共享数据。
5. 进入**授权**选项卡。
6. 为广告平台开放以下权限：
   * **访问汇总转化数据**。
   * **访问汇总应用内事件数据**。
   * **访问汇总收入数据**。
7. 点击**保存权限**。
8. 通知广告平台您已为其开放相应权限。
9. 如果您有多个应用与该渠道对接，需为各个应用分别完成上述流程。

</Accordion>

<div data-zendesk-anchors="aggregated-campaign-performance-report=%E6%B1%87%E6%80%BB%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%E4%B8%9A%E7%BB%A9%E6%8A%A5%E5%91%8A h_01HM8SQ5RE1FGQDY6V1A8MMEQX=%E6%B1%87%E6%80%BB%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%E4%B8%9A%E7%BB%A9%E6%8A%A5%E5%91%8A about-the-report=%E5%85%B3%E4%BA%8E%E6%8A%A5%E5%91%8A h_01HM8SQ5REM6MW5GBRSXTF0N73=%E5%85%B3%E4%BA%8E%E6%8A%A5%E5%91%8A h_01HM8SQ5RETK7HCPZGGX8KX9VG=report-structure dimensions=%E7%BB%B4%E5%BA%A6 h_01HM8SQ5RE11PW6HGTWGC2AGR5=%E7%BB%B4%E5%BA%A6 metrics=%E6%8C%87%E6%A0%87 h_01HM8SQ5RGQEH6G6W75FVWJKSP=%E6%8C%87%E6%A0%87 h_01HM8SQ5RGCGTWTSRHB8B4FSY2=bi-developer-considerations h_01HM8SQ5RG4JEE75F6CBTFCBB5=retention-report-considerations permissions=%E6%8E%88%E6%9D%83 h_01HM8SQ5RGNXENZ89GD74KJWH2=%E6%8E%88%E6%9D%83 h_01HM8SQ5RGQADHTEP5ED3W87VZ=permission-to-get-aggregated-performance-data" />
