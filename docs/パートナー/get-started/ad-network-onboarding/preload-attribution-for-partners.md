---
title: パートナー向けプリロードアトリビューション
metadata:
  keywords:
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-alina-koifman
    - Marketers
    - Mobile Attribution
  created_at: '2023-05-15T09:45:55Z'
  edited_at: '2026-10-21T19:20:12Z'
  id: 15321350340241
  locale: ja
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ja/articles/15321350340241
---
> **概要：** OEMでの工場出荷時プリロードや、ユーザーが初めて端末を起動した際のプリロードによるアプリインストールを、該当するキャンペーンへアトリビューションします。

<div id="overview" />

## 概要

AppsFlyerのプリロードアトリビューションソリューションに対応することで、プリロードパートナーは、アプリインストールをプリロードキャンペーンへアトリビューションできます。プリロードキャンペーンとは、プリロードパートナーが工場出荷時、または端末のアクティベーション時（ユーザーが初めて端末の電源を入れたとき）にアプリを端末へインストールするキャンペーンです。

プリロードパートナーには、以下が含まれます。

* 端末メーカー（OEM）
* アプリディスカバリープラットフォーム
* モバイルキャリア

プリロードキャンペーンをアトリビューションする方法は3つあります。

* ［推奨］AppsFlyerリファラ
* Google Play自動インストール（PAI）
* ［旧方式］System Propertyを使用した工場出荷時のプリロード

各コンバージョン後に、ポストバックが送信されます。

<Anchor target="_blank" href="/marketers/ja/docs/appsflyer-attribution-model#preload-campaigns">プリロードキャンペーンのアトリビューション方法について詳しくはこちら</Anchor>

<div id="set-up-preload-attribution" />

## プリロードアトリビューションの設定

プリロードアトリビューションを設定するには：

1. AppsFlyerの<Anchor target="_blank" href="/partners/ja/docs/getting-started-onboarding-guide-for-ad-networks">連携済みパートナー</Anchor>であることを確認します。
2. 広告主のニーズに応じて、連携するプリロードアトリビューションソリューションを選択します。**注意**：連携ごとに、AppsFlyerパートナーアカウントで個別のPIDが必要です。サポートウィジェットからパートナーソリューションチームへお問い合わせください。
   * ［推奨］<Anchor target="_blank" href="/marketers/ja/docs/set-up-appsflyer-preload-referrer-attribution">AppsFlyerリファラ</Anchor>：連携手順については、担当のPDMにお問い合わせください。
   * <Anchor target="_blank" href="/marketers/ja/docs/measure-preload-campaigns-with-google-play-install">Google Play自動インストール（PAI）</Anchor>：以下のUTMパラメータを使用し、PAIキャンペーン向けのGoogle Play Referrer APIでメディアソース情報を設定します。`utm_source=play-auto-installs&utm_medium=preload&utm_campaign=brandnamepai_int`。例：`utm_source=play-auto-installs&utm_medium=preload&utm_campaign=xiaomipai_int`。
3. サポートウィジェットからAppsFlyerパートナーソリューションチームへ連絡し、連携設定を完了します。必要に応じて、ポストバックも設定できます。  
   **注意**：<Anchor target="_blank" href="/marketers/ja/docs/measure-preload-campaigns-with-google-play-install#プリロードパートナーのポストバック">Google PAI</Anchor>および<Anchor target="_blank" href="/partners/ja/docs/postback-macros-for-ad-networks">AppsFlyerリファラ／Androidマニフェストファイル</Anchor>のプリロード方式でサポートされるポストバックマクロを確認してください。

<div data-zendesk-anchors="organic-search-attribution=%E6%A6%82%E8%A6%81 h_01HQFFB20SKDVW1X3ECMZCZQW0=%E6%A6%82%E8%A6%81 set-up-preload-attribution=%E3%83%97%E3%83%AA%E3%83%AD%E3%83%BC%E3%83%89%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E8%A8%AD%E5%AE%9A h_01HQFFB20S6KJH3PBF5N2190TJ=%E3%83%97%E3%83%AA%E3%83%AD%E3%83%BC%E3%83%89%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E8%A8%AD%E5%AE%9A" />
