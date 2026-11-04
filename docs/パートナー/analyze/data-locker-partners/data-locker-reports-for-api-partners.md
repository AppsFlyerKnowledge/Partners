---
title: APIパートナー向けデータロッカーレポート
metadata:
  keywords:
    - Advertisers
    - Partners
    - marketing partners
    - Marketers
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Marketers
    - Data Locker
  created_at: '2023-01-08T11:32:00Z'
  edited_at: '2026-10-14T09:36:39Z'
  id: 12000718524561
  locale: ja
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ja/articles/12000718524561
---
> **概要**：本記事に記載されているレポートは、代理店向けのData Lockerにて利用可能なものです。なお、AppsFlyerからパートナーへデータを共有するには、本記事内に記載のように広告主（アプリの所有者）からパートナーへのデータアクセスの権限付与が必要です。

<div id="data-locker-reports-for-api-partners" />

## APIパートナー向けデータロッカーレポート

レポートを取得するには、APIパートナーは、次の条件を満たす必要があります。

* 広告主から <Anchor target="_blank" href="/partners/ja/docs/access-to-aggregated-analytics-tools-for-api-partners#grant-permission-to-a-partner">集計アナリティクスレポートへのアクセス</Anchor>権限が付与されていることを確認してください。
* <Anchor target="_blank" href="/partners/ja/docs/data-locker-for-partners#set-up-data-locker">Data Locker</Anchor>の設定してください。　**注：** 手順3〜4をスキップします。

APIパートナーは以下のレポートを利用できます。

* <Anchor target="_blank" href="/marketers/ja/docs/cohort-analytics-via-data-locker">コホート統合</Anchor>表示(毎日)
* <Anchor target="_blank" href="/marketers/ja/docs/cohort-analytics-via-data-locker">コホートユーザー獲得</Anchor> (毎日)
* <Anchor target="_blank" href="/marketers/ja/docs/cohort-analytics-via-data-locker">コホートリターゲティング</Anchor> (毎日)
* <Anchor target="_blank" href="/marketers/ja/docs/advanced-aggregated-reports-in-data-locker">高度な集計（</Anchor>バージョン管理）レポートも利用でき、データの鮮度が向上します。

レポートは、h=23のフォルダに書き込まれます。

<div id="specifications-and-limitations" />

<Accordion title="特性と制限">

| 仕様 | 備考 |
| --- | --- |
| 代理店の運用媒体の開示設定 | サポートされておらず、計測対象外です |
| アプリ固有のタイムゾーン | 高度な集約（バージョン管理）レポートで利用可能 |
| App-specific currency | はい |
| オーガニックデータ | 利用可能 |
| 非オーガニックデータ | 利用可能 |
| コストデータ | 利用不可 |
| データ更新頻度 | <ul><li>日次コホートレポートの場合：<ul><li>このレポートは、通常翌日の h=23フォルダ内にて10:00-12:00 UTC までに利用できるようになります。例えば、月曜日に発生したデータのレポートは月曜日のh=23のレポートに格納されます。</li><li>例外：例外：広告収益イベントのデータ更新頻度は0+3日です。つまり、月曜日のレポート内の広告収益イベントは、土曜日に発生したものです。</li></ul></li><li>[ベータ版] バージョン管理されたレポートは、通常、日本時間 15:00 (06:00 UTC) までに利用できます。</li></ul> |

特性

</Accordion>

<div id="see-also" />

> 📄 **参照：**
>
> * <Anchor target="_blank" href="/partners/ja/docs/access-to-aggregated-analytics-tools-for-api-partners">集計アナリティクスツール：APIパートナー向け</Anchor>

<div data-zendesk-anchors="data-locker-reports-for-marketing-partners=api%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91%E3%83%87%E3%83%BC%E3%82%BF%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HBZZ5BFJC82MW9JQ9MEX991S=api%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91%E3%83%87%E3%83%BC%E3%82%BF%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HBZZ5BFJYFH54X70RJ63CJCV=specifications-and-limitations h_01HE7RFGCZ65YJRX1VCND691CX=%E5%8F%82%E7%85%A7" />
