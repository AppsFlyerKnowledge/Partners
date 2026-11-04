---
title: Data Locker中广告平台可用的SSOT报告
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2024-07-31T19:51:34Z'
  edited_at: '2026-10-14T10:09:08Z'
  id: 27168206416017
  locale: zh-cn
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/zh-cn/articles/27168206416017
---
> **概要：** Data Locker中的SSOT报告结合ID匹配和SKAN等多种归因模式的数据，以一体化的视图全面准确地呈现应用广告的投放效果。  您可以将这些报告导入您的BI系统，从而获得最为精准的数据。

<div id="note" />

> 📘 **注意**
>
> * 广告主必须先在面板中为您开放必要[权限](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions)，然后我们才会与您共享相关数据。
> * SSOT Data Locker报告提供的是LTV维度数据而非活跃维度数据。也就是说，报告中的数据反映的是用户在各个触点上的生命周期价值，而不是应用内或事件活跃数据。

<div id="what-is-data-locker" />

## Data Locker简介

Data Locker能够以安全可靠的方式直接向AWS、GCS和Snowflake等主流云平台传输数据。您可以通过该解决方案便捷地完成数据对接和入库，便于对数据进行综合分析与上报。详情请见<Anchor target="_blank" href="/partners/zh/docs/data-locker-for-partners">此文档</Anchor>。

<div id="what-is-single-source-of-truth-ssot" />

## 单一可信数据源（SSOT）简介

SSOT报告结合ID匹配和SKAN等多种归因模式的数据，以一体化的视图全面准确地呈现应用广告的投放效果，旨在解决数据碎片化所带来的问题。详情请见<Anchor target="_blank" href="/marketers/zh/docs/single-source-of-truth-ssot-guide-for-ios-attribution">此文档</Anchor>。

<div id="benefits-of-ssot-reports-in-data-locker" />

## 通过Data Locker获取SSOT报告的优势

SSOT报告所呈现的数据能完全满足营销人员对投放效果分析与衡量的需求。

* **准确掌握完整的转化情况：** SSOT可联合处理多种不同归因模式所产生的数据，有效避免多模式并行时的激活数据重复统计，从而确保相关数据能准确地反映真实的用户行为和转化。
* **将数据导入您的BI系统：** SSOT能够帮助您将汇总数据高效、精准地导入您的内部BI系统。这些汇总数据包括归因、应用内事件以及收入数据，且涵盖所有的维度和指标。

<div id="setting-up-data-locker" />

<Accordion title="Data Locker的设置方式">

请按本节所述流程设置Data Locker。若您对Data Locker的设置做出了更改，新的设置会在3小时内生效。

**前期准备：**

完成以下一个或多个云存储配置流程：

* <Anchor target="_blank" href="/marketers/zh/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>存储桶
* <Anchor target="_blank" href="/marketers/zh/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>存储桶
* 【Beta】<Anchor target="_blank" href="/marketers/zh/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor>存储桶
* <Anchor target="_blank" href="/marketers/zh/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor>数据仓库

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Data Locker的设置方式如下：**

1. 登录到您的<Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">AppsFlyer合作伙伴面板。</Anchor>
2. 进入以下页面：
   * **广告主**：**报告**>**Data Locker**。
   * **营销合作伙伴**：点击 **帐户菜单** > **Data Locker**。
3. 按照<Anchor target="_blank" href="/marketers/zh/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">Data Locker设置说明</Anchor>中的第3-16步进行操作。

</Accordion>

<div id="permissions" />

<Accordion title="授权">

由代理指定（启用）的广告平台：代理无法授权，必须让广告主代其授权。

**如需向广告平台开放SSOT数据，广告主需完成以下操作：**

1. 在AppsFlyer后台左侧的菜单栏中，选择**协作** > **对接渠道**。
2. 搜索并选择相关渠道。
3. 点击**设置对接**。界面会跳转到对接设置页。
4. 确认**启用该渠道**开关已开启。如果该开关未打开，AppsFlyer就不会共享数据。
5. 进入授权选项卡。
6. 为广告平台开放以下权限：
   * **访问汇总转化数据**。
   * **访问汇总应用内事件数据**。
   * **访问汇总收入数据**。
7. 点击**保存权限**。
8. 通知广告平台您已为其开放相应权限。
9. 如果您有多个应用与该渠道对接，需为各个应用分别完成上述流程。

</Accordion>

<div id="ssot-report-facts" />

<Accordion title="SSOT报告详情说明">

| 特点 | 说明 |
| --- | --- |
| 可用报告 | 可用的报告类型有以下两种：<ul><li>用户获取：将转化归因到拉新渠道，包括再互动窗口期内的激活后用户行为。</li><li>再营销：将转化归因到再营销渠道，适用于以下事件：<ul><li>再归因后发生的事件</li><li>再互动窗口期内发生的事件</li></ul></li><li>统一：根据AppsFlyer的<Anchor target="_blank" href="/marketers/zh/docs/resolve-retargeting-double-attribution">双重归因</Anchor>原则，将转化归因到末次触达渠道。也就是说在统一视图中，激活后的用户行为数据会显示在再营销渠道下，而不会显示在UA渠道下。</li></ul> |
| 报告周期 | 该报告最多可呈现激活后7天内的群组指标。 |
| 文件目录结构 | 文件目录结构按激活日期设定。每个激活日期的文件夹中包含当日生成的多个数据版本，各版本呈现当日最新的累计数据。也就是说，您应仅处理最近期的那一版数据。<Anchor target="_blank" href="/marketers/zh/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#文件目录结构">了解详情</Anchor> |
| 报告结构 | 报告结构（即其中的维度和指标）是固定的，无法更改。 |
| 时区 | UTC |
| 数据时效性 | <ul><li>每天更新一次，</li><li>根据UTC时间凌晨（即一天结束）时的数据计算指标。</li><li>SLA：新报告会在UTC时间16:00前写入Data Locker中。每天生成一个新版本，每个版本覆盖最近15个激活日期。<Anchor target="_blank" href="/marketers/zh/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#report-folder-hierarchy">详情请见此处说明。</Anchor></li></ul> |

</Accordion>

<div id="report-structure" />

## 报告结构

报告由不同的维度和指标组成。

这些指标涵盖了归因、收入以及完成具体事件的独立用户。

<div id="field-formats" />

<Accordion title="字段格式">

<Table>
  <thead>
    <tr>
      <th>
        格式名称
      </th>
      <th>
        说明
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        字符串 [n]
      </td>
      <td>
        字符串的长度上限。AF接收数据时并不会对字段长度做出硬性限制，但超过上限的字段可能会被截断。
      </td>
    </tr>
    <tr>
      <td>
        时间字符串
      </td>
      <td>
        字符串的格式为：

        ```
        yyyy-mm-dd hh:mm:ss.
        ```

        示例：

        ```
        2019-09-17 00:09:25
        ```
      </td>
    </tr>
    <tr>
      <td>
        枚举 [n]
      </td>
      <td>
        枚举字段仅可包含特定的值。比如selected\_currency字段的值只能由指定的3字符货币代码组成。
      </td>
    </tr>
    <tr>
      <td>
        时间戳
      </td>
      <td>
        10位UNIX时间戳。比如：  
        UTC时间2020年8月4日07:25的时间戳为：

        ```
         "timestamp": "1596525944"
        ```
      </td>
    </tr>
    <tr>
      <td>
        布尔
      </td>
      <td>
        该字段中可能出现的值为*TRUE*或*FALSE*
      </td>
    </tr>
    <tr>
      <td>
        整数
      </td>
      <td>
        整数
      </td>
    </tr>
    <tr>
      <td>
        浮点数
      </td>
      <td>
        浮点数（实型）中可以带小数点，且小数点后可以有值。
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="dimensions" />

<Accordion title="维度">

<Table>
  <thead>
    <tr>
      <th>
        字段名称
      </th>
      <th>
        说明
      </th>
      <th>
        格式
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        af\_ad\_id
      </td>
      <td>
        广告标识符，广告层次结构中的一个层级。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        af\_ad
      </td>
      <td>
        广告名称。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        af\_adset\_id
      </td>
      <td>
        广告组标识符。广告层次结构中的一个层级。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        af\_adset
      </td>
      <td>
        广告组名称。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        app\_id
      </td>
      <td>
        以“ID”开头的App ID（广告主应用）。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        attribution\_method
      </td>
      <td>
        用于事件归因的机制。包括AppsFlyer归因机制、SKAN归因、以及自然量。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        可能出现的值有：click（点击）、impression（展示）和null值。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        campaign
      </td>
      <td>
        广告平台上报给AppsFlyer的广告系列名称
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        af\_c\_id
      </td>
      <td>
        广告系列标识符。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        转化后的天数（不是实际转化的时间戳）  
        小贴士：您可以使用该数据来计算留存和KPI天数。
      </td>
      <td>
        整型
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
        | af\_conversion | 用户转化。使用conversion\_type来识别转化类型，即激活、重新下载（re-download）、再归因或再互动。 |
        | 广告主定义的应用内事件 | 用户完成指定应用内事件。 |
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        geo
      </td>
      <td>
        ISO国家/地区代码。AppsFlyer传统归因模式根据用户的IP地址判断此信息，而在SKAN模式中，该数据由广告平台上报或通过建模推算得出。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        install\_date
      </td>
      <td>
        SKAN：由AppsFlyer根据回传接收时间估算得出

        AF：

        * UA（用户获取）：安装相关应用后首次打开该应用的时间。
        * 再营销：再互动/再归因后首次打开应用的时间。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        UA（用户获取）：True

        再营销：在再互动窗口期内，AF会将用户同时归因到最初的拉新渠道（即再互动之前的渠道）以及带来再互动的渠道。如果事件发生在再互动窗口期内，初始媒体渠道字段会显示为FALSE（即不是主要渠道），而再互动渠道字段则为TRUE。
      </td>
      <td>
        布尔值
      </td>
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td>
        获得某个事件归因的广告平台。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        selected\_currency
      </td>
      <td>
        3个字母组成的货币代码（如USD、EUR等），由广告主在AF后台的应用设置页面中配置。需使用ISO-4217标准中的货币代码。这里的货币与SSOT面板中收入指标的货币单位一致。
      </td>
      <td>
        字符串
      </td>
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        可能出现的值为：  
        Install（激活）：用户首次下载并打开相关应用。  
        Re-attribution（再归因）：用户完成卸载重装，并归因到新的广告系列。  
        Re-download（重新下载，适用于SKAN）：用户卸载相关应用后再次安装该应用。  
        Re-engagementRe-engagement用户与再营销广告交互后再次打开相关应用。
      </td>
      <td>
        字符串
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="metrics" />

<Accordion title="指标">

| 各指标在Data Locker中的名称 | 说明 | 格式 |
| --- | --- | --- |
| revenue\_selected\_currency | 以选定货币为单位的累计收入金额。最多精确到小数点后2位。  <br />比如：若事件名称为event\_name=purchase，窗口期为days\_post\_attribution=2，则该字段的值为激活后2天（而非仅第2天）内来自购买事件的总体收入。 | 双精度浮点数 |
| revenue\_usd | 以美元（USD）为单位的累计收入。  <br />比如：若事件名称为event\_name=purchase，窗口期为days\_post\_attribution=2，则该字段的值为激活后2天（而非仅第2天）内来自购买事件的总体收入。 | 双精度浮点数 |
| skan\_duplicates | 对于由SKAN归因及AF传统归因模式归因到的激活进行去重处理，避免SSOT数据中出现重复。 | 长整型 |
| uninstalls\_count | 激活应用后卸载（删除）应用的用户数量（仅适用于用户获取） | 长整型 |
| unique\_users | 完成某个事件的独立用户数。该字段表达累计值。  <br />比如：若事件名称为event\_name=purchase，窗口期为days\_post\_attribution=2，则该字段的值为激活后2天（而非仅第2天）内完成购买的独立用户数量。 | 整型 |

</Accordion>

<div id="modeled-data" />

<Accordion title="模型推算数据">

AppsFlyer的数据模型可推算出基础SKAN数据无法提供的信息。

* null值：Apple为了保障用户隐私，会在SKAN中将实际值替换为“Null”值，再进行上报。为了填补数据缺口，SSOT会通过数据模型对这些null值进行推算。详情请见<Anchor target="_blank" href="/marketers/zh/docs/skan-modeled-data#null-conversion-values">此文档</Anchor>。
* 激活后的监测窗口期更长：SKAN对用户激活后两天以外的行为无法提供粒度较细的数据，这方面的局限性会导致数据不准确。为了确保数据质量，我们会对激活后更长一段时间内产生的事件独立用户及收入进行建模推算。详情请见<Anchor target="_blank" href="/marketers/zh/docs/skan-modeled-data#revenue-ltv">此文档</Anchor>。

国家/地区（Geo）数据：由于SKAN的数据颗粒度限制，国家/地区数据通常不可用。在这种情况下，我们会通过模型推算这些数据，帮助您进行有效的数据分析。详情请见<Anchor target="_blank" href="/marketers/zh/docs/skan-modeled-data#geo">此文档</Anchor>。

</Accordion>

<div id="partial-data" />

<Accordion title="不完整数据">

如果您需要对最近几个激活日期内产生的数据进行分析，这时较长期的激活后指标（如激活后7天）可能尚未达到完备状态。这种情况下，相关指标仍然可用，但其数据不完整。

请充分考虑下列事项：

* 每当有可用数据出现时，该报告就会立即呈现这些数据。
* 激活后两天内的指标会在5天后达到完备状态。
* 激活后七天内的指标会在7天后达到完备状态。在激活后的15天内，我们的模型会不断对这些数据进行精细化处理。

出现不完整数据的原因有以下几种：

* 数据成熟度：如果激活日期与当前日期之间的时间段短于您要分析的时间段，则相关数据仍在累计中，尚不完整。
* SKAN延时：SKAN在发送数据时会有随机的延时。比如激活后2天内的用户行为数据最多可能会在激活后的96小时（即4天）后方才送达。
* 模型推算数据的处理节奏：我们会对激活后2天以上的SKAN数据进行建模推算，并在激活日期的7天之后生成首个推算值。在激活后第2到7天这段时间内，AppsFlyer传统归因模式的数据已达到可用状态，但SKAN的模型推算数据尚不可用。

示例（假设激活日期为1月1日）：

* 1月2日：AppsFlyer尚未收到SKAN数据。激活后2天内的数据与激活后7天的数据相同，且两者都不完整，由AppsFlyer传统归因模式的数据组成。
* 1月3日：AppsFlyer接收到部分SKAN数据。激活后2天的数据不完整，但这时其中包含部分SKAN数据。激活后7天的数据尚不包含模型推算的SKAN数据（首个模型推算值将在激活日期起的7天后可用）。因此在激活后的2到7天内，激活后7天的指标值可能低于激活后2天的指标值。
* 1月6日：AppsFlyer己接收到激活后2天的完整SKAN数据，包括延时最长的回传。此时，激活后2天的指标已充分涵盖完整数据，但激活后7天的指标值尚不完整。
* 1月8日：激活后7天的SKAN模型推算数据已生成完成。我们的模型会持续细化该数据，一直到1月16日为止。

</Accordion>

<div id="directory-structure" />

## 文件目录结构

<div id="report-folder-hierarchy" />

<Accordion title="报告文件夹的层次结构">

* 主文件夹按报告类型整理归类。可能出现的文件夹名称为：“ssot\_unified”、“ssot\_retargeting”和“ssot\_user\_acquisition”。
* 这些文件夹下的子文件夹则按照激活日期整理归类。

**报告版本**

* 每个激活日期的文件夹中都包含多个版本的数据，每天一次写入Data Locker。
* 每个版本都反映该激活日期的最新累计数据。
* 报告中包含该激活日期的所有可用数据。比如在4月18日，各个激活日期文件夹中的最新版数据包含截至4月18日的所有可用数据。
* 提示：建议您总是处理最近期的那一版数据，以确保数据准确性。

每个激活日期文件夹下最多可容纳15个版本的报告。激活日期的15天后，所有指标都已充分覆盖完整数据，并已打磨完毕。详情请见<Anchor target="_blank" href="/marketers/zh/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">此文档</Anchor>。

</Accordion>

<div id="directory-and-filename-structure" />

<Accordion title="目录与文件名结构">

SSOT报告的路径格式如下：

`<bucket-name>`/t=`<ssot_unified OR ssot_retargeting OR ssot_user_acquisition>`/install\_date=`<yyyy-mm-dd>`/version=`<unix timestamp>`/`<parquet file number>`

广告主存储桶中的文件夹层次结构示例：

```
bucket
|
└── t=ssot_unified
    |
    ├── install_date=2024-05-05
    |   |
    |   └── version=1714890235
    |   |    |
    |   |    ├── part-00000-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    |
    |   |    ├── part-00001-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    │
    |   |    └── part-00002-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |
    |   |
    |   └── version=1714890286
    |        |
    |        ├── part-00000-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        |
    |        ├── part-00001-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        │
    |        └── part-00002-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |   |
    .   . 
    .   .
```

说明：

* t：报告主题（类型）。
* install\_date：用户激活相关应用的日期。也就是说报告按用户激活应用的日期呈现激活后的用户行为数据，而不是按用户行为发生的日期来呈现数据。
* version：使用Unix时间戳来表示相关版本的创建时间。

</Accordion>

<div id="bi-developer-considerations" />

## BI开发者注意事项

**报告中的数据范围：**

这些报告中包含新增激活、再营销产生的再互动（即SKAN中的re-downloads）和再互动，以及相关的应用内事件。

<div id="loading-reports" />

<Accordion title="报告入库">

您可以同时将统一、UA和再营销报告导入您的BI系统，也可以分开单独导入。如果您选择同时导入这三种报告，需要自行筛选不同视图的数据：

* 统一报告：使用is\_primary\_attribution=true或null来筛选数据。
* 用户获取报告：使用conversion\_type=Install来筛选数据。
* 再营销报告：使用conversion\_type=re-engagement或re-attribution来筛选数据。
* 统一视图：如果您在数据入库的过程中使用统一视图，可以按投放类型来拆分数据：

* 使用conversion\_type=install、re-engagement或re-attribution（在SKAN中为re-downloads）来筛选数据。
* 详情请见《再营销事件的双重归因》。

</Accordion>

<div id="days-postattribution" />

<Accordion title="归因后的天数">

<div id="important" />

> 🚧 **重要提示！**
>
> 报告中包含days\_post\_attribution（归因后的天数）维度，该维度将收入及独立用户数据关联到激活后的特定天数。

* 对于转化（激活、再互动等），该维度的值为0。
* 对于收入和应用内事件，相关数据会被分为两个预定义群组，目前仅限激活后“2”天和“7”天。

<strong>为了确保您能对应用内事件和收入进行准确分析，建议使用days\_post\_attribution维度来筛选数据。</strong>详见下文说明。

一种常见的错误查询方式是运用过于简单的逻辑将一系列维度的收入值进行加总。由于这种方式会重复统计部分收入（days\_post\_install=2的收入和days\_post\_install=7的收入之间有重叠），因此得出的数据不准确。这个例子同样也适用于特定应用内事件的独立用户数分析。

</Accordion>

<div id="considerations" />

<Accordion title="注意事项">

**请务必注意以下几点：**

* 最新版本：总是查询各激活日期下最近期的版本，以确保您在数据分析中使用的是最新最准确的数据。
* 收入计算：以美元为单位的收入指标是根据事件当天的汇率计算的。
* 归因分析：带有event\_name=af\_conversion的记录即表示对转化的归因（包括激活、再归因/SKAN中的re-downloads以及再互动）。归因到的转化数量呈现在独立用户指标下，这些字段的收入指标为空，days\_post\_attribution的值为0。
* 面板对比：对比面板中的激活数时，请使用重新下载（redownloads）和激活（install）这两种转化类型的总和，因为面板会将这两种类型的转化都计为激活（install）。
* 应用内事件分析：event\_name不等于“af\_conversion”的记录即表示应用内事件。完成该事件的独立用户数呈现在独立用户指标下，而这些事件带来的收入则呈现在收入指标下。
* 转化类型：您可以使用这个维度来区分拉新和再营销转化。请注意，SKAN数据还有另一层细分（区分激活与redownloads）。与SSOT面板中的数据进行对比时，需注意在面板中这类转化都计为激活。
* 广告收入事件：这类数据可用时会在相应的记录内呈现。
* 分应用取数：所有应用的数据都集中在一个文件中。您可以使用App ID字段来区分各应用的数据，或将Data Locker设置为按应用区分数据。

</Accordion>

<div id="example-use-cases" />

<Accordion title="使用场景示例">

本节列举了一些通过Data Locker拉取数据并用于BI的常见使用场景，且每个示例都配以相关的SQL语句及Excel表格数据，作为更直观的说明。

<div id="calculating-total-attributions-per-campaign" />

<Accordion title="针对每个广告系列计算归因到的转化总量">

这类数据的查询方式如下：

* 针对各个激活日期，分广告系列对归因到的独立转化数量进行加总。
* 筛选事件名称为“af\_conversion”且带有特定广告系列ID（af\_c\_id）的转化

```sql
SELECT install_date, SUM(unique_users) AS total_attributions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign" />

<Accordion title="计算转化量（激活与re-downloads）以对比面板中各广告系列带来的激活">

这类数据的查询方式如下：

* 分广告系列和激活日期计算新增激活和重新下载（re-downloads）的总量。
* 将转化总量与面板中的激活指标（结合了“install”和“re-downloads”两类转化）进行对比。

```sql
SELECT install_date, conversion_type, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND conversion_type IN ('install', 're-download')    
-- The dashboard sums both under the install field
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type;
```

</Accordion>

<div id="calculating-retargeting-conversions-per-geo" />

<Accordion title="分国家/地区计算再营销转化量">

这类数据的查询方式如下：

* 分国家/地区计算由再营销广告带来的转化数量。
* 将转化类型设置为“re-attribution”和“re-engagement”，筛选出这些转化。

```sql
SELECT install_date, conversion_type, geo, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type IN ('re-attribution', 're-engagement')    
-- Both types are relevant for re-targeting
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type, geo;
```

</Accordion>

<div id="calculating-installs-by-attribution-method-per-media-source" />

<Accordion title="按归因方式计算各媒体渠道的激活">

这类数据的查询方式如下：

* 按归因方式（SKAN、AppsFlyer传统归因和自然量）统计激活量，并将该数据按媒体渠道细分。
* 筛选事件名称为“af\_conversion”且转化类型为“install”的记录。

```sql
SELECT install_date, attribution_method, media_source, SUM(unique_users)   
AS total_installs
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type = 'install'
    AND app_id = 'YOUR_APP'
GROUP BY install_date, attribution_method, media_source;
```

</Accordion>

<div id="calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset" />

<Accordion title="计算Facebook上各广告组的激活后7天累计收入">

这里我们针对Facebook上投放的广告，考察其激活后7天内的累计收入。

```sql
SELECT install_date,
       af_adset,
       SUM(revenue_usd) AS total_revenue_day_7
FROM ssot_unified
WHERE media_source = 'facebook'
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_adset;
```

</Accordion>

<div id="calculating-cumulative-revenue-for-selected-postinstall-periods" />

<Accordion title="计算激活后指定时间段内的累计收入">

这类数据的查询方式如下：

* 计算激活后多天的累计收入时，需要拆分激活后2天和7天的总收入。
* 请注意，分析过去7天的激活时，激活后7天的数据可能不完整。<Anchor target="_blank" href="/marketers/zh/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">了解详情</Anchor>

```sql
SELECT install_date,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) AS total_revenue_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) AS total_revenue_day7
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source" />

<Accordion title="分媒体渠道计算特定应用内事件（购买）带来的收入">

这类数据的查询方式如下：

* 衡量某个特定事件（如“af\_purchase”）所带来的收入值，并按媒体渠道细分。
* 按选定的激活后天数筛选数据，确保不出现重复统计。

```sql
SELECT install_date, media_source, SUM(revenue_usd) AS total_purchase_revenue
FROM ssot_unified
WHERE event_name = 'af_purchase'  -- Change to your specific event
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

<div id="calculating-inapp-event-conversion-rate-for-2-days-postinstalls" />

<Accordion title="计算激活后2天内的应用内事件转化率">

这里我们需要计算某个特定应用内事件（如“af\_complete\_tutorial”）在激活总量中的比率。

```sql
SELECT install_date,
  SUM(IF(days_post_attribution = 2 AND   
event_name = 'af_complete_tutorial', unique_users, 0)) 
  / SUM(IF(event_name = 'af_conversion', unique_users, 0))   
AS conversion_rate_day2_af_tutorial_conversion
FROM ssot_unified
WHERE conversion_type = 'install'    
-- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id" />

<Accordion title="分广告系列ID计算激活后7天和2天的ARPU">

这类数据的查询方式如下：

* 计算各广告系列在激活后2天和7天的每用户平均收入（ARPU）。
* 请注意，分析过去7天的激活时，激活后7天的数据可能不完整。<Anchor target="_blank" href="/marketers/zh/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">了解详情</Anchor>

```sql
SELECT install_date,
       af_c_id,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day7
FROM ssot_unified
WHERE conversion_type = 'install'  
       -- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_c_id;
```

</Accordion>

<div id="calculating-amount-of-duplicates-per-media-source-in-this-query" />

<Accordion title="计算分媒体渠道的重复数据量">

这里我们需要按媒体渠道和激活日期来计算重复归因的用户总量，来考察哪些渠道的用户归因重复率较高。

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
    AND event_name = 'af_conversion'
GROUP BY install_date, media_source;
```

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="特点与局限性">

| 特点 | 备注 |
| --- | --- |
| 各天的报告可用性 | 在激活日期结束时SSOT开关必须处于打开状态，否则该日期没有SSOT报告 |
| 激活后2天的指标 | <ul><li>若您在转化值操作台中设置了SKAN 4模式：该指标为激活后2天的数据</li><li>若您在转化值操作台中设置了SKAN 3模式：该指标取决于您指定的SKAN用户行为窗口期<br />比如：如果用户行为窗口期为24小时，则该指标仅计算这个窗口期内发生的事件（即使您查询的是激活后X+1天的数据）。</li></ul> |
| 应用内事件可用性 | 仅支持在第一个窗口期（Window 1）内发生的事件。 |
| SKAN中重新下载（redownloads）的细分数据 | 可用。但SSOT面板将激活和redownloads都计为激活，因此没有单独的redownloads数据。 |
| SKAN转化值操作台配置变更 | 更改SKAN转化值操作台的配置可能会导致SSOT数据持续约96小时出现不准确，这是因为这段时间内AppsFlyer仍会收到使用之前的映射构架编码的激活回传。 |
| 时区 | 不支持AF后台应用配置中的指定时区。 |
| 自然量数据 | <ul><li>支持激活后7天的指标。</li></ul> |
| 转化（激活、再归因、再互动）后天数 | 仅支持转化后7天 |
| 代理数据透明化 | 支持 |
| 广告系列名称变更 | 不支持。如果广告系列名称发生变更，请使用广告系列ID对数据进行分组和筛选。 |
| 广告平台 | <ul><li>符合以下条件的广告平台可以访问Data Locker中的SSOT报告，查看归因到自己平台的数据：<ul><li>广告主已在转化值操作台中启用SSOT。</li><li>广告平台正在投放SKAN广告系列。</li><li>广告主已向相关广告平台开放汇总数据的[必要权限](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions)。</li></ul></li></ul> |
| 代理访问权限 | 不支持。代理可以在SSOT面板中查看SSOT数据。 |
| D7（激活后7天）指标 | <ul><li>自然流量的D7指标自2025年2月16日起可用。</li><li>如果出现以下情况，D7指标可能出现缺失或低于D2指标：<ul><li>8天的日期范围中包含还未结束的日期。</li><li>模型推算数据不可用（如收入数据少于14天）。详情请见<Anchor target="_blank" href="/marketers/zh/docs/skan-modeled-data#revenue-ltv">此文档</Anchor>。</li><li>SKAN转化值操作台的配置在过去14天内发生变更。</li><li>某一天的激活数量低于10个。</li></ul></li></ul> |
| 预定义事件名称 | 由于事件名称“af\_conversion”用于表达转化类型，因此如果相关应用配置了名为“af\_conversion”事件，该事件会重命名为“af\_conversion\_event”。 |
| 指定货币的数据差异 | 由于SSOT面板和Data Locker中SSOT报告的数据不是同时计算的，因此您在对比面板和报告中以指定货币为单位的收入值时，可能会略有差异。这是因为在不同时间计算收入数据时使用的汇率可能会有浮动。 |
| SKAN的D7不完整数据 | 由于SKAN的D7数据是模型推算数据，且首版数据在激活后的7天生成，分析最近7天内的D7数据时需要注意，这里的D7数据是不完整的。对于归因方式为SKAN的记录，D7指标会低于D2指标。 |
| D7收入和应用内事件指标的颗粒度有限 | 激活后7天的收入和事件独立用户指标不支持广告组、广告和转化类型级别的颗粒度。由于SKAN一般不提供如此详细的信息，因此我们的数据模型不考虑这些维度。 |
| 变现数据时效性 | 广告收入数据会有一天的延迟。<br /><br />举例来说，7月3日上午生成的报告中包含截至7月1日（含）的广告收入数据。 |

</Accordion>

<div data-zendesk-anchors="h_01J455DHWAB1J9611A4KA40PZM=%E6%B3%A8%E6%84%8F ssot-reports-in-data-locker=data-locker%E7%AE%80%E4%BB%8B h_01J454K90GWKME8F4JCDQKM3CK=data-locker%E7%AE%80%E4%BB%8B what-is-single-source-of-truth-ssot=%E5%8D%95%E4%B8%80%E5%8F%AF%E4%BF%A1%E6%95%B0%E6%8D%AE%E6%BA%90ssot%E7%AE%80%E4%BB%8B h_01J454K90GRCFR3PSAQRTX98B4=%E5%8D%95%E4%B8%80%E5%8F%AF%E4%BF%A1%E6%95%B0%E6%8D%AE%E6%BA%90ssot%E7%AE%80%E4%BB%8B benefits-of-ssot-reports-in-data-locker=%E9%80%9A%E8%BF%87data-locker%E8%8E%B7%E5%8F%96ssot%E6%8A%A5%E5%91%8A%E7%9A%84%E4%BC%98%E5%8A%BF h_01J454PANH9J6ZZ069RS6FVWZM=%E9%80%9A%E8%BF%87data-locker%E8%8E%B7%E5%8F%96ssot%E6%8A%A5%E5%91%8A%E7%9A%84%E4%BC%98%E5%8A%BF h_01J46C54ZB4YYTZ6CDHHC0EC8P=setting-up-data-locker h_01J455Q07J5XPYEBVP3BZ1FMVH=permissions h_01J29BTC9CESJF592P616WMK46=ssot-report-facts report-structure::673746b9=%E6%8A%A5%E5%91%8A%E7%BB%93%E6%9E%84 h_01J29CQ5K4JBEP4X8YQ0V32WYR=%E6%8A%A5%E5%91%8A%E7%BB%93%E6%9E%84 h_01J29CHBX2QNFTAQSA1W01PFH0=field-formats h_01J29BTC9CJ8GZDDCHK9NBZ4YX=dimensions h_01J29BTC9C86YMVEY17QQZNZCV=metrics h_01J29BTC9CH3DAA7ZRHG8C04MF=modeled-data h_01J29M72WAPH3KEW9N60JHTT3W=partial-data directory-structure=%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84 h_01J29MB7B7Q3PJ9YWFQESWN0KD=%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84 h_01J29MCSH4V41CPB7ZG41751QW=report-folder-hierarchy h_01J29MCSH40ATHNAJMY8KR7ANZ=directory-and-filename-structure bi-developer-considerations=bi%E5%BC%80%E5%8F%91%E8%80%85%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9 h_01J29MS6XV7XYTA9Q81454WEQN=bi%E5%BC%80%E5%8F%91%E8%80%85%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9 h_01J2F4HG8YHDGYFKHBBC5KSN2G=loading-reports h_01J2F4HG8YKNEVGEWTR91ADSDS=days-postattribution h_01J3YT1X908JVMDXKRQBCRD1JR=%E9%87%8D%E8%A6%81%E6%8F%90%E7%A4%BA h_01J2F4HG8YAAE0E04Y6Q9Z62NZ=considerations h_01J3A82HZF14CCS027FE991M0T=example-use-cases h_01J3A883DQFQE0WTTY4FMX3AQ4=calculating-total-attributions-per-campaign h_01J3A883DQ82K71XY408M2BW0B=calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign h_01J3A883DQ5QAVH6AX7CGCBSWG=calculating-retargeting-conversions-per-geo h_01J3A883DQE25X31SPPF166BRH=calculating-installs-by-attribution-method-per-media-source h_01J3A883DQ8QVR8WKPPX1QF414=calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset h_01J3A883DQ51T3Z6H239P5JDJ1=calculating-cumulative-revenue-for-selected-postinstall-periods h_01J3A883DQXRCQ4NWY0BCX886E=calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source h_01J3A883DQRR62BWQ6JBTZ7238=calculating-inapp-event-conversion-rate-for-2-days-postinstalls h_01J3A883DRPEVDQCWKCT9M3EC1=calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id h_01J3A883DRRZ9Y8F3KNAAPZT2S=calculating-amount-of-duplicates-per-media-source-in-this-query h_01J29MV69M667QDHMS5WGYKPCZ=traits-and-limitations" />
