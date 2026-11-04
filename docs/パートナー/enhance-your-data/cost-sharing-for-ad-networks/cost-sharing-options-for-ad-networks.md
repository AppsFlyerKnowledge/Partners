---
title: コスト連携の方法：アドネットワーク向け
metadata:
  keywords:
    - clicks
    - Partner
    - cost
    - Ad Networks
    - Partners
    - ad spend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2020-09-07T13:50:24Z'
  edited_at: '2026-10-14T09:31:45Z'
  id: 360012893658
  locale: ja
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ja/articles/360012893658
---
> **概要：** AppsFlyerのアドネットワークパートナーが利用できる、コストデータの共有方法について比較しています。

<div id="sharing-cost-with-appsflyer-and-advertisers" />

## AppsFlyer・広告主とのコストデータの共有

広告主は、AppsFlyerをROI / 請求 / マーケティング予算配分に関する意思決定のための情報源として使用しています。アドネットワークの情報を可視化する上で、AppsFlyerとのコストデータの共有は必要不可欠です。  なお、コストデータを持たないアドネットワークのデータは、AppsFlyerの管理画面上でも最下部に表示される仕様になっています。

アドネットワークは、以下のいずれかの方法を使用することでAppsFlyerとのコスト共有が可能です。

* **InCost API**：AppsFlyerにデータを流し込む方法です。
* **Cost API**：AppsFlyerがデータを引き出す方法です。
* **コストインポート**：コストデータのファイルをAppsFlyerにアップロード/送信する方法です。
* **Cost by click** 計測リンクがクリックされるたびにコストが記録される方法です

<div id="cost-badge-for-ad-networks" />

### コスト連携のバッジ

![CostBadge.jpg](https://files.readme.io/6b660b68b932802f7982a3beb3a155ecc350de1b4cb3baede6e84ef0d704388c-360011247338.jpg)

* <Anchor target="_blank" href="/marketers/ja/docs/partner-integrations#パートナーページ">パートナー詳細ページに</Anchor>、InCostまたはCost APIを使用しているパートナーを示すコストバッジが表示されます。
* このバッジは、そのパートナーがコスト計測に対応しているパートナーであることを証明します。
* 弊社分析とユーザー調査の結果、広告主は常に新しい広告媒体を探していることがわかっています。また、広告主はROIに注目しながらマーケティングパフォーマンスを分析したいと考えているため、コストバッジが付与されることで注目される可能性も高くなるでしょう。

<div id="reporting-cost-options-available-to-ad-networks" />

### アドネットワークが利用可能な、コスト連携の選択肢

| 連携方法 | コストバッジの付与資格 | 特徴 |
| --- | --- | --- |
| <Anchor target="_blank" href="/partners/ja/docs/incost-api-for-ad-networks">InCost API</Anchor> | ✓ | アドネットワークが、InCostのレポート設定をする時期/タイミングについて全ての管理権限を所有します。<br /><br />InCostには以下の特徴があります。<ul><li>全てのコストモデルをサポート</li><li>高い正確性 / 信頼性</li><li>完全自動化</li><li>アドネットワーク側がコントロールするもの：<ul><li>データアップロードのスキーム</li><li>データの更新頻度</li></ul></li><li>AppsFlyerの管理画面上で、広告主からアドネットワークに対してコストデータをアップロードできる権限を付与する必要あり。</li></ul>**制限事項**：<br /><br />AppsFlyerの代理店アカウントはサポートされていません。 |
| Cost API | ✓ | <ul><li>全てのコストモデルをサポート</li><li>高い正確性</li><li>AppsFlyer上でアドネットワークがコストデータをある程度管理</li><li>代理店アカウントのコストもサポート対象</li><li>広告主がAppsFlyerの管理画面上で、必要なIDなどの設定を実施。</li><li>データ更新頻度:１日６回、４時間ごと</li></ul>**制限事項**：<br /><br />連携作業は、AppsFlyer側の開発の優先順位に依存します。 |
| コストインポート<br /><br />(ファイルアップロード) | いいえ | <ul><li>アドネットワークでの作業について：<ul><li>自動化できる開発リソースがない場合、データを手動でアップロード</li><li>データをアップロードするタイミングは任意</li><li>AppsFlyer上でアドネットワークがコストデータをある程度管理</li><li>連携はアプリ毎に行う必要があり、AppsFlyerの管理画面上で、広告主からアドネットワークに対してコストデータをアップロードできる権限を付与する必要あり。</li><li>計測情報の紐付けは、キャンペーン名を基に実施されます。(キャンペーンIDはサポート外)</li></ul></li></ul>**制限事項**：<ul><li>AppsFlyerの代理店アカウントはサポートされていません。</li><li>メール経由でのアップロード自動化は、失敗のリスクがあるのでおすすめしません。</li></ul> |
| <Anchor target="_blank" href="/partners/ja/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Cost by click</Anchor><br /><br />(計測URLへのパラメータ追加) | いいえ | <ul><li>CPIキャンペーン向けのクイックソリューション</li><li>データの更新頻度はほぼリアルタイム</li><li>クリックURLによるコスト共有は、広告主がSKAdNetworkを利用していた場合、より正確性に欠ける可能性があります。</li></ul>**制限事項**：<ul><li>CPI課金でしか利用できません。</li><li>誤ったデータがリンク上で送信された場合、後から変更することはできません。</li><li>リターゲティングはサポートされていません。</li><li>クリックURLによって記録されたコストは、SKANオーバービューには反映されません。</li></ul> |

<div data-zendesk-anchors="sharing-cost-with-appsflyer-and-advertisers=appsflyer%E5%BA%83%E5%91%8A%E4%B8%BB%E3%81%A8%E3%81%AE%E3%82%B3%E3%82%B9%E3%83%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E5%85%B1%E6%9C%89 h_01HN0A1ER3MNZM508ZCG9KP26P=appsflyer%E5%BA%83%E5%91%8A%E4%B8%BB%E3%81%A8%E3%81%AE%E3%82%B3%E3%82%B9%E3%83%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E5%85%B1%E6%9C%89 cost-badge-for-ad-networks=%E3%82%B3%E3%82%B9%E3%83%88%E9%80%A3%E6%90%BA%E3%81%AE%E3%83%90%E3%83%83%E3%82%B8 h_01HN0A1ER4K1V4479W5SXCEC30=%E3%82%B3%E3%82%B9%E3%83%88%E9%80%A3%E6%90%BA%E3%81%AE%E3%83%90%E3%83%83%E3%82%B8 reporting-cost-options-available-to-ad-networks=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%8C%E5%88%A9%E7%94%A8%E5%8F%AF%E8%83%BD%E3%81%AA%E3%82%B3%E3%82%B9%E3%83%88%E9%80%A3%E6%90%BA%E3%81%AE%E9%81%B8%E6%8A%9E%E8%82%A2 h_01HN0A1ER4Y128ZHJERXS6A8ET=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%8C%E5%88%A9%E7%94%A8%E5%8F%AF%E8%83%BD%E3%81%AA%E3%82%B3%E3%82%B9%E3%83%88%E9%80%A3%E6%90%BA%E3%81%AE%E9%81%B8%E6%8A%9E%E8%82%A2" />
