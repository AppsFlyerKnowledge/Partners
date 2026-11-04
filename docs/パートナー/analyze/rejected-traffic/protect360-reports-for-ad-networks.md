---
title: Protect360レポート：アドネットワーク向け
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2022-02-08T14:53:48Z'
  edited_at: '2026-10-14T09:25:16Z'
  id: 4420246395793
  locale: ja
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/ja/articles/4420246395793
---
> **概要：** 概要：新規ユーザー獲得やリターゲティングを担当するアドネットワークは、ブロックされたクリックやインプレッションのデータを受け取ることが可能です。

<div id="protect360-reports-for-ad-networks" />

## Protect360レポート：アドネットワーク向け

免責事項免責事項：このページでは、アドネットワークのみが利用できるProtect360のレポートに関する情報を記載しています。広告主が利用可能なデータについては、Protect360：連携済みパートナー向けを参照してください。

アドネットワークは、パートナー向けのData Lockerにて、以下のいずれかの理由でブロックされたクリックやインプレッションに関する情報を含むレポートを受け取ることができます。

* アドネットワークが不正の上限を超えた場合に発生する、ブロックされたクリックやインプレッションのデータ。このレポートには、すべてのブロックデータと、クリックとインプレッションの上限設定によってブロックされたデータが含まれます。（上限設定について）
* アドネットワークのPIDパラメータとクリックを検証するためのクリック署名が有効でない場合に発生する、クリック署名が失敗した場合のデータ。（クリック署名について）

アドネットワークは、ブロックされたクリックやインプレッションのデータを広告主を横断して自社のアドネットワーク単位で取得することで、不正行為から自身を保護するために活用することができます。

<div id="report-considerations" />

### レポートに関する注意点

* データは、CSV形式で新規獲得 / リターゲティングアドネットワークのバケットに格納されます。
* アドネットワークに関連するカラムと指標が含まれています（広告ネットワークに無関係なカラムはすべて削除されています）。
* データは、 パートナー向けのData Lockerから取得可能です。
* データ更新頻度

<div id="report-types" />

## レポートタイプ

<div id="blocked-clicks-and-impressions" />

<Accordion title="ブロックされたクリックとインプレッション">

このレポートには、上限設定やその他の理由でブロックされたクリックとインプレッションに関する集計レベルのデータが含まれます。 

<div id="report-structure-fieldsdimensions" />

#### レポート構成フィールド ／ ディメンション

| **フィールド** | **備考** |
| --- | --- |
| app\_id | AppsFlyerの管理画面上のアプリID |
| site\_id | 広告を表示したパブリッシャー (配信面) を識別する、広告媒体が発行しているID |
| date | ブロックされた日付 |
| agency | <ul><li>そのアドネットワーク経由で、トラフィックをもたらした代理店</li><li>代理店が関与していない場合には、nullを返す</li></ul> |

<div id="report-structure-metrics" />

#### レポート構成：指標

| **フィールド** | **備考** |
| --- | --- |
| number\_of\_blocked\_clicks | アドネットワークがブロックされたクリックの総数 |
| number\_of\_blocked\_impressions | アドネットワークがブロックされたインプレッションの総数 |
| number\_of\_capped\_clicks | アドネットワークが上限設定でブロックされたクリック数（ブロックされた全クリックのうち） |
| number\_of\_capped\_impressions | アドネットワークが上限設定でブロックされたインプレッション数（ブロックされた全インプレッションのうち） |

</Accordion>

<div id="failed-click-signatures" />

<Accordion title="失敗したクリック署名データ">

このレポートには失敗したクリック署名に関するユーザーレベルのデータが含まれ、アドネットワークがAppsFlyerのクリック署名の機能を使用する場合、有効なクリック署名を持っていないもののアドネットワークのPIDが振ってあるURKのクリック、もしくは署名が無効か期限切れといったデータが含まれます。クリック署名の失敗は、アドネットワークによるクリック署名の実装に技術的なエラーがある場合、またはクリックが第三者によってアドネットワークの代わりに（そのPIDで）送信された場合に発生する可能性があります。

<div id="report-structure-fieldsdimensions-1" />

#### レポート構成フィールド ／ ディメンション

| **フィールド** | **備考** |
| --- | --- |
| event\_time |  |
| original\_url |  |
| failed\_signing\_reason | 例：<ul><li>Invalid signature (署名が無効です。)</li><li>Missing signature (署名がありません。)</li><li>Expired signature (期限切れの署名)</li><li>Expired secret key (期限切れのシークレットキー)</li></ul> |
| is\_blocking\_enabled | <Anchor target="_blank" href="/partners/ja/docs/click-signing-for-ad-networks">クリック署名のAPI</Anchor>の設定モードを記載：<ul><li>TRUEの場合は、APIが有効になっている状態。</li><li>FALSEの場合は、レポートのみの状態。</li><li>無効になっている場合には、レポートには含まれません。</li></ul> |

</Accordion>

<div data-zendesk-anchors="protect360-reports-for-ad-networks=protect360%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91 report-considerations=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%B3%A8%E6%84%8F%E7%82%B9 report-types=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%82%BF%E3%82%A4%E3%83%97 report-structure-fieldsdimensions=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E6%A7%8B%E6%88%90%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89--%E3%83%87%E3%82%A3%E3%83%A1%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3 report-structure-metrics=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E6%A7%8B%E6%88%90%E6%8C%87%E6%A8%99 report-structure-fieldsdimensions::44afb679=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E6%A7%8B%E6%88%90%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89--%E3%83%87%E3%82%A3%E3%83%A1%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3-1" />
