---
title: SKANにおけるCV値設定の取得API：アドネットワーク向け
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2026-10-14T09:35:45Z'
  id: 11705009866001
  locale: ja
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ja/articles/11705009866001
---
> **概要**：概要：広告主によって定義された、アプリ毎のSKANCV値の設定を確認しましょう。

## SKANにおけるCV値設定の取得API：アドネットワーク向け

SKAN計測の場合、広告主はコンバージョン値(CV値)を設定することで、インストール後一定期間内に発生したユーザーの行動を計測しユーザーの質を評価しています。<Anchor target="_blank" href="/marketers/ja/docs/skadnetwork-skan-solution-guide">SKANの詳細はこちらを参照してください。</Anchor>

CV値ごとのマッピングは、conversion\_value\_mappingの配列内に含まれます。

このAPIを利用したい場合には、<Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">SKANにおけるCV値設定の取得API：アドネットワーク向け</Anchor>のガイドに従って作業を行うよう、ご自身の社内の開発担当者へ依頼をしてください。各キーとその説明のリストを参照したい場合には、上記別ページのシュミレーター上で［200］をクリックしてください。

**注：**

* CV値の範囲はそれぞれ以下の通りです：
  * SKAN 4｜1つ目のポストバック｜細かい粒度のCV値：　0 - 632024-02-26
  * SKAN 4｜1〜３つ目のポストバック｜粗い粒度のCV値：　low, medium, high
  * SKAN 3以前0-63
* 広告主はいつでもCV値のマッピングを変更することが可能です。
* そのため、アドネットワークはこのAPIを毎日クエリして、常に最新のCV値の構成であることを確認する必要があります。

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=skan%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8Bcv%E5%80%A4%E8%A8%AD%E5%AE%9A%E3%81%AE%E5%8F%96%E5%BE%97api%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91" />
