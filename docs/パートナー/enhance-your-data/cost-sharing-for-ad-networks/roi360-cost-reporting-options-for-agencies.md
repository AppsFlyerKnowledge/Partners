---
title: Xpend - 代理店向けのコストレポート機能
metadata:
  keywords:
    - clicks
    - cost
    - Agencies
    - Partners
    - ad spend
    - Xpend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Agencies
    - ROI360
  created_at: '2020-10-04T15:07:34Z'
  edited_at: '2026-10-14T09:39:04Z'
  id: 360014054998
  locale: ja
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ja/articles/360014054998
---
> **概要：** cost API (プレミアム機能であるROI360の契約が必要)やクリックでのコスト計測の機能を使うことで、コストデータの記録が可能になります。

<div id="cost-reporting-for-agencies" />

## コストの記録：代理店向け

広告主は、AppsFlyerをROI / 請求 / マーケティング予算配分に関する意思決定のための情報源として使用しています。そうするためには、全てのコストに関する情報を1つのプラットフォーム上に集約する必要があります。AppsFlyerのプレミアム機能であるXpendを使うことで、広告主や代理店はAPI経由でコストデータを収集しAppsFlyerの管理画面やレポートツール上に表示することが可能になります。 

コストデータは以下のいずれかの方法を使うことで集計できます。 

* **Cost API**：AppsFlyer pulls data from partners
* **Cost by click**計測リンクがクリックされるたびにコストが記録される方法です

次の表では、Xpendの契約有無によって利用可能なコスト計測の機能を記載しています。

| 任意 | ROI360のご契約が必要です | 説明 |
| --- | --- | --- |
| <Anchor target="_blank" href="/marketers/ja/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">Cost API</Anchor> | はい | <ul><li>代理店はアドネットワークのAPI認証情報を使って連携し、AppsFlyer管理画面上でのコストAPIの機能を有効にできます。</li><li>コストデータは運用媒体の開示設定に応じて反映されます。(SRN媒体の場合、クリック数とインプレッション数も含まれます。)</li><li>全てのコストモデルをサポート</li><li>高い正確性</li><li>データ更新頻度:１日６回、４時間ごと/span></li></ul> |
| <Anchor target="_blank" href="/partners/ja/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Cost by click</Anchor><br /><br />(計測URLへのパラメータ追加) | いいえ | <ul><li>代理店アカウント上で発行した計測URLにCPI、通貨単位などのパラメータを追加することで、AppsFlyer上にコストが集計されます。AppsFlyerがコストを集計します。</li><li>データ更新頻度データの更新頻度はほぼリアルタイム</li></ul>制限事項<ul><li>CPI課金でしか利用できません。</li><li>誤ったデータがリンク上で送信された場合、後から変更することはできません。</li><li>クリックURLによって記録されたコストは、SKAdNetworkのオーバービューでは利用できません。</li><li>クリックURLによるコスト共有は、広告主がSKAdNetworkを利用していた場合、正確性に欠ける可能性があります。</li></ul> |

<div data-zendesk-anchors="cost-reporting-for-agencies=%E3%82%B3%E3%82%B9%E3%83%88%E3%81%AE%E8%A8%98%E9%8C%B2%E4%BB%A3%E7%90%86%E5%BA%97%E5%90%91%E3%81%91" />
