---
title: 合作渠道专用的Data Locker
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Data Locker
    - Agencies
    - Ad Networks
  created_at: '2021-05-28T15:37:04Z'
  edited_at: '2026-10-14T10:09:24Z'
  id: 360020818517
  locale: zh-cn
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/zh-cn/articles/360020818517
---
> **概要：** 合作渠道（包括广告平台和代理）专用的Data Locker可将应用数据传输至合作渠道在AWS、GCS或BigQuery中的存储空间。

![6133DataLockerForPartners.png](https://files.readme.io/f6cad12250fe07cf2b0a12b64eeaa597c83527b4b4e09aea11cc2a52ab53339b-4637680455313.png)

## 合作渠道专用的Data Locker

合作渠道专用的Data Locker可将应用数据传输至云端存储。广告主可设置权限，允许AppsFlyer向指定合作渠道共享所选数据。

<div id="data-locker-features" />

<Accordion title="Data Locker 功能简介">

| 功能 | 说明 |
| --- | --- |
| 存储方式 | 您在以下平台的自有数据存储桶：<ul><li>AWS</li><li>GCS</li><li>Yandex</li><li>BigQuery</li></ul><Anchor target="_blank" href="/marketers/zh/docs/data-locker-for-marketers#storage-options">关于存储选项</Anchor> |
| 支持多应用取数 | 支持获取已与您对接的多个应用的数据。如需获取数据，需由广告主对每份报告单独授权。 |
| 数据格式选项 | <ul><li>适用于云端数据存储桶：<ul><li>CSV</li><li>PARQUET</li><li>Adobe</li></ul></li><li>数据仓库</li></ul> |
| 数据时效性 | 不同报告类型的数据时效性不同：<ul><li>**每小时：** 数据持续生成</li><li>**每日：** 部分报告数据每日更新，次日可用</li></ul> |

</Accordion>

<div id="reports-available-for-partners" />

<Accordion title="合作渠道可获取的报告">

不同类型的合作渠道可访问的报告内容及所需权限不同。但所有合作渠道的Data Locker运行机制、存储选项以及所需配置均无差异。请根据合作渠道类型，参阅以下文章：

* <Anchor target="_blank" href="/partners/zh/docs/data-locker-reports-available-for-ad-networks">广告平台</Anchor>
* <Anchor target="_blank" href="/partners/zh/docs/data-locker-reports-for-agencies">代理</Anchor>
* <Anchor target="_blank" href="/partners/zh/docs/data-locker-reports-for-api-partners">平台官方合作渠道</Anchor>

</Accordion>

## 数据存储结构

<div id="overview" />

<Accordion title="概览">

Data Locker会将数据写入您指定的存储工具中。您可随时切换存储选项。更新将在数小时内生效。

Data Locker以分级的目录结构将数据写入存储桶中，分级维度为报告类型、日期和时间。下图为目录结构示例：下图为目录结构示例：

![DLFolderOVerview.png](https://files.readme.io/78f360ec1df72253e5b2cd725f3eecf4e17548a7f06b544a94a75a2c319d77a0-18107910420369.png)

具体报告的数据保存在该报告类型下的小时数（h）文件夹中。

* 文件夹的数量取决于该报告是按小时流式生成还是按天生成。
* 通过Snappy或GZIP压缩文件或未压缩的Parquet或CSV文件提供数据。
* 数据文件由列（字段）组成。
* 字段结构依据具体报告类型而定。

</Accordion>

<div id="folder-structure" />

<Accordion title="目录结构">

| 文件夹 | 说明 |
| --- | --- |
| data-locker-hourly | ![DLHourly.png](https://files.readme.io/c257b82d22622d97808a6c23603ac4eee9f2ab091bcb68a33637ac4fb749fdff-18107874510353.png)<ul><li>存储桶中的根目录命名方式取决于云服务商。</li><li>*data-locker-hourly*目录下是报告主题文件夹，</li></ul>**各种场景的文件夹结构示例**：<ul><li>**您的AWS存储桶**：*&lt;af-datalocker-your bucket prefix>/&lt;generated-home-folder>&lt;subscription-id>*</li><li>**您的GCS存储桶：** &lt;your bucket name>/&lt;generated-home-folder>/&lt;subscription-id></li></ul> |
| t（主题） | 报告类型与报告主题相关。 |
| dt（日期） | 代表相关的数据日期。大多数情况下为事件发生的日期。 |
| h（小时） | h文件夹表示AppsFlyer接收到该数据的时间。比如AF会将UTC时间14:00-15:00之间接收到的激活数据写入h=14文件夹中。请注意：数据从到达AppsFlyer到写入Data Locker的h文件夹之间存在约6小时的延迟。如，h=14的数据文件会在当日23:00（UTC）写入Data Locker。<br /><br />**小时数文件夹的特点**：<ul><li>共有24个h文件夹，分别以0-23编号，比如h=0、h=1等等。</li><li>另有一个late文件夹，用于存放前一日午夜后（即次日 00:00–02:00 UTC）到达的事件。例如，用户在周一08:00安装应用，但事件于周二01:00到达，此事件将记录在周一的late文件夹中。</li><li>在02:00之后到达的数据记录在实际到达日期和时间的文件夹中。</li><li>请务必处理late文件夹中的数据，该数据不会出现在其他文件夹中。</li><li>\_temporary 文件夹：:在某些情况下，我们会在h文件夹内生成临时文件夹。请忽略所有\_temporary文件夹及其子文件夹。例如：/t=impressions/dt=2021-04-11/h=18/**\_temporary**。</li></ul> |
| 统一数据 | 所有应用的数据合并在统一的数据文件中。取数时请使用行级的app\_id field字段来区分不同应用的数据。<br /><br /><strong>示例：h=2文件夹下为数据文件</strong><br /><br />![UnifiedByApp.png](https://files.readme.io/dbc39c2ce99c1ff607fd553b9c9034e55728c102f31fd18a501cc00910267b28-18107874522513.png)<ul><li>在加载数据时，请确保遵循以下要求：<ul><li>请在系统设置完\_SUCCESS标签后开始读取数据。</li><li>加载所有扩展名为<em>.gz</em>的文件。</li></ul></li></ul> |
| 完成标签 | 一个h文件夹中的所有数据都写入完毕后，系统会设置末尾文件（完成）标签。<ul><li>请务必先确认数据带有\_SUCCESS标签，然后再拉取数据。</li><li>即使某个文件夹内无数据（为空），也会生成 \_SUCCESS 标志。</li></ul> |
| 压缩说明 | 数据文件采用.gz格式压缩。解压后：<ul><li>文件不含扩展名。</li><li>每个文件首行均为列名（字段名）标题行。</li></ul> |
| 字段顺序 | 报告中的字段顺序始终相同。新字段会依次添加在现有字段的右侧。<br /><br />各报告字段（列）定义，请参阅对应报告的详细说明文档。 |
| 字段填充注意事项 | **空白或null字段**： 字段可能为空或为 null，出现这种情况即表示这个字段在该报告中没有数据可以上报。一般来说，*null*表示该字段在相应报告和应用类型中不适用。空值（显示为"'）表示该字段适用于相应的报告和应用类型，但未找到相关数据。<br /><br />**时区和货币**：<br /><br />Data Locker提供的数据不受应用层级的时区和货币设置影响。因此：<ul><li>**时区**：日期和小时数按UTC时间计算。</li><li>**货币**：event\_revenue\_usd字段以美元为单位。</li></ul>**带逗号的值**：逗号包含在双引号`"`中，例如，`` `"iPhone6,1"` ``。 |

</Accordion>

<div id="data-files" />

<Accordion title="数据文件">

不同的分类取数方式会产生不同的数据文件。

<table><thead><tr><th>内容</th><th colspan="2">说明</th></tr></thead><tbody><tr><td>完成标签</td><td colspan="2"><p>一个h文件夹中的所有数据都写入完毕后，系统会设置末尾文件（完成）标签。 </p><ul><li><p>请务必先确认数据带有_SUCCESS标签，然后再拉取数据。</p></li><li><p>即使某个文件夹中没有数据可写（即该文件夹为空时），系统也会设置_SUCCESS标签。 </p></li><li>请注意：在分应用取数时，需在h文件夹（而非应用文件夹）中确认该标签。详情请见上节图示。 </li></ul></td></tr><tr><td>文件类型</td><td colspan="2"><ul><li>通过Snappy或GZIP压缩文件或未压缩的Parquet或CSV文件提供数据。</li><li>解压后的数据文件是Parquet或CSV格式的，具体取决于您的设置。</li></ul></td></tr><tr><td>字段顺序（CSV文件） </td><td colspan="2"><p>如果是CSV文件，则报告中的字段顺序总是不变的，新添加的字段会出现在现有字段的右侧。 </p><p>在这种情况下： </p><ul><li>各种用户链路报告的字段结构完全一致。也就是说，不同类型的报告可以使用相同的数据入库流程。请参考 <a href="/marketers/zh/docs/raw-data-field-dictionary" target="_blank">原始数据字段词典</a>中的字段释义，在报告中选择您需要的字段。 </li><li>在报告可用性部分中，带有FF标记的报告字段结构与一般报告不同。 </li></ul></td></tr><tr><td>字段填充注意事项</td><td colspan="2"><p><strong>空白或空字段：</strong> 字段可能为空或为 null，出现这种情况即表示这个字段在该报告中没有数据可以上报。一般来说，<em>null</em>表示该字段在相应报告和应用类型中不适用。空值（显示为"'）表示该字段适用于相应的报告和应用类型，但未找到相关数据。 </p><p>如果媒体渠道受限，则受限字段的值为“null”。 </p><p>总体而言，null值和空值的含义基本相同，都可以理解为没有可用的值。 </p><p><strong>时区和货币</strong></p><p>Data Locker提供的数据不受应用层级的时区和货币设置影响。Data Locker数据的时区和货币单位如下： </p><ul><li> <strong>时区</strong>：日期和时间数据为UTC。</li><li> <strong>货币</strong>：event_revenue_usd字段以美元为单位。</li></ul><p><strong>带逗号的值</strong>：逗号包含在双引号`"`中，例如，<code>`"iPhone6,1"`</code>。</p></td></tr></tbody></table>

</Accordion>

<div id="storage-options" />

<Accordion title="存储工具选项">

* 可选的存储工具如下：AWS、GCS和BigQuery。
* 您可以随时切换存储工具。
* 更改存储工具后会发生以下变化：
  * AF会在一小时内将数据写入新的存储桶。
  * 更改存储工具后会有一个7天的过渡期，在此期间我们会继续将数据写入原先的存储工具。您可以在AF后台查看过渡期的结束时间，以便对后续的数据入库流程变更做出相应的安排。
  * **更改存储桶**:如您更换了存储位置，系统将在7天过渡期内同时向新旧存储空间发送数据，以便您有充足时间调整数据接收流程。

|  | 合作渠道存储工具（GCS、AWS、BigQuery） |
| --- | --- |
| 存储区名称 | <ul><li>GCS：没有限制</li><li>AWS：由您设置。必须带有前缀af-。</li></ul>示例：`af-datalocker-your-bucket-name` |
| 存储所有者 | Partner |
| 存储平台 | AWS、GCS、Yandex、BigQuery |
| 访问数据的凭证 | AppsFlyer不掌握该信息。请使用存储服务商提供的凭证。 |
| 数据保留 | 由您控制 |
| 数据安全 | 存储空间由您掌控。<ul><li>**AWS**:AppsFlyer需要存储桶的GetObject、ListBucket、DeleteObject、PutObject权限。该存储桶必须仅用于AppsFlyer数据存储。请勿将其用于其他用途。</li><li><Anchor target="_blank" href="/marketers/zh/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor></li></ul> |

#### **安全负责人须知**

注意事项：

* 该存储桶或宿端仅可用于AppsFlyer的数据写入，请确保无其他实体向其中写入数据。
* 您可在我们写入数据后25小时后删除数据。
* 宿端中的数据是AF服务器中数据的副本。我们会按AF的数据保存规定将这些数据保存在服务器中。
* 出于技术原因，我们有时可能需要删除并重写数据。因此，我们需要具备delete和list权限。这两项权限不会对您构成安全风险。在list权限下，我们是唯一写入存储桶的实体。在delete权限下，我们可以重新生成数据。

</Accordion>

<div id="multipleconnection-principles-more-than-one-destination" />

<Accordion title="多宿端作用原理">

您可以使用Data Locker将您的部分或所有数据发送到多个宿端（在连接部分设置）。比如，将A应用的数据发送到AWS，将B应用的数据发送到GCS。

每个连接由一套完整的Data Locker设置组成，其中包含一个宿端。每个连接的设置都是单独分开的。

管理宿端连接时需注意以下几点：

* 宿端连接在Data Locker设置部分中，分单独的标签页显示。也就是说，您可以在各连接的专属标签页中管理其配置。默认标签页为“Data Locker”。
* 请按以下步骤创建新连接：
  1. 点击**添加连接**。
  2. 为该连接命名，并选择存储工具类型。
  3. 点击**保存**。  
     保存成功后，该连接就会显示在默认的“Data Locker”标签页旁边。每个标签页的图标代表相应的存储工具类型。
* 如需查看连接详情、创建连接副本或删除连接，请点击⋮（选项图标）。

</Accordion>

## 配置流程

<div id="set-up-data-locker" />

<Accordion title="设置Data Locker">

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
   * **广告主**：从AppsFlyer后台左侧的菜单栏中选择**导出** > **Data Locker**。
   * **营销合作伙伴**：点击**账户菜单**>**Data Locker**。
3. 按照<Anchor target="_blank" href="/marketers/zh/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">Data Locker设置说明</Anchor>中的第3-16步进行操作。

</Accordion>

## 其他相关信息

<div id="traits-and-limitations" />

<Accordion title="特性与局限性">

| **特点** | 说明 |
| --- | --- |
| 应用层级的指定时区 | 不适用 |
| 应用配置中的指定货币 | 不支持 |
| 大小限制 | 不适用 |
| 数据时效性 | 数据的更新频率取决于具体报告的数据时效性，详情请见本文档。 |
| 历史数据 | 不支持 |
| 团队成员访问 | 团队成员无法配置Data Locker。 |

</Accordion>

<div id="troubleshooting" />

<Accordion title="问题排查">

请查看<Anchor target="_blank" href="/marketers/zh/docs/data-locker-for-marketers#troubleshooting">故障排查指南</Anchor>。

</Accordion>

<div data-zendesk-anchors="data-locker-for-partners=%E5%90%88%E4%BD%9C%E6%B8%A0%E9%81%93%E4%B8%93%E7%94%A8%E7%9A%84data-locker h_01H8Y0DGS4Y2N99YNYEEJA6RSF=%E5%90%88%E4%BD%9C%E6%B8%A0%E9%81%93%E4%B8%93%E7%94%A8%E7%9A%84data-locker h_01H8Y0DGS4EM06PYNS1DRMZM6Y=data-locker-features h_01H8Y0DGS4A0MYGVZ9XQ49EBT2=reports-available-for-partners data-storage-architecture=%E6%95%B0%E6%8D%AE%E5%AD%98%E5%82%A8%E7%BB%93%E6%9E%84 h_01H8Y0DGS4WTAJV7QE2DX3VGBP=%E6%95%B0%E6%8D%AE%E5%AD%98%E5%82%A8%E7%BB%93%E6%9E%84 h_01H8Y0DGS4BQHBKNHZ4CD9ZMT4=overview h_01H8Y0DGS43JAREX23YX1F125K=folder-structure h_01H8Y0DGS524WNXY63351XGJKA=data-files h_01H8Y0DGS5MV6J1MMJJS8G4HC4=storage-options notice-to-security-officers=%E5%AE%89%E5%85%A8%E8%B4%9F%E8%B4%A3%E4%BA%BA%E9%A1%BB%E7%9F%A5 h_01H8Y0DGS5R4QX01WBK2S33QP5=%E5%AE%89%E5%85%A8%E8%B4%9F%E8%B4%A3%E4%BA%BA%E9%A1%BB%E7%9F%A5 h_01H8Y0DGS56GN6TVTSEV713DWQ=multipleconnection-principles-more-than-one-destination procedures=%E9%85%8D%E7%BD%AE%E6%B5%81%E7%A8%8B h_01H8Y0DGS5588GQPZT7MQ686T3=%E9%85%8D%E7%BD%AE%E6%B5%81%E7%A8%8B h_01H8Y0DGS57YK2PZ9ENZ80EWRJ=set-up-data-locker additional-information=%E5%85%B6%E4%BB%96%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF h_01H8Y0DGS5SYZRWFAXDSKE3YHX=%E5%85%B6%E4%BB%96%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF h_01H8Y0DGS540HK8MSCFYT9Q1RM=traits-and-limitations h_01H8Y0DGS55PJ7HV1PQ72XDDAB=troubleshooting" />
