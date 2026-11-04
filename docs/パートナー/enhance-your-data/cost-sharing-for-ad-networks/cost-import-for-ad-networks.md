---
title: 広告ネットワークのコストインポート
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2026-10-14T09:25:34Z'
  id: 360002868097
  locale: ja
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ja/articles/360002868097
---
> **概要：** アドネットワークが広告主のキャンペーン費用をCSVファイル形式で直接AppsFlyerへ報告する方法について記載しています。

<div id="cost-import-for-ad-networks" />

## 広告ネットワークのコストインポート

![AdspendIngestion.jpg](https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg)

<div id="overview" />

#### 概要

* 以下のような広告費の詳細を含むCSVファイルを準備してください：
  * 広告費の発生した日付
  * AppID（アプリが同じ広告主に紐付いている場合には、1つのファイル内に複数のアプリデータも入力可能です）
  * メディアソース（ファイル毎に1つまで）
  * キャンペーン名
  * 広告費の合計
  * ［任意］国
  * ［任意］通貨単位（デフォルト設定：USD）
* メールでAppsFlyerへファイルを送付するか、AppsFlyerのパートナーアカウントで管理画面にログインして、ファイルをアップロードしてください。    
  **注記：**
  * ファイルを初めて送信する前に、広告主は広告ネットワークにコストのインポート権限を付与する必要があります。これはアプリごとに 1 回実行する必要があり、非常に簡単なプロセスです。
  * 一度ファイルをアップロードすると、元に戻すことはできません。
* インポート後は、ファイルにエラーが見つからなかったことを確認してください。

<div id="submitting-ad-spend-files-for-ad-networks" />

### 広告費インポート：アドネットワーク向け

* 管理画面からのアップロード、またはメール方式のどちらかを使って、広告費をインポートしてください。
* ［推奨］CSVフォーマットに関する問題を解決するのがより簡単なため、基本的には管理画面からのアップロード方式をご利用ください。
* アドネットワークは代理店のコストデータをインポートできません。広告主のみがインポートできます。

<div id="submission-by-file-upload" />

#### ファイルアップロードによるファイル提出

**コストインポート ファイルをアップロードして送信するには:**

1. ［作業するアプリ毎に都度必要です］<Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-permissions-for-ad-networks">広告主に対して、広告費インポートの権限を付与するよう依頼してください。</Anchor>
2. <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#prepare-csv-file-with-cost-data">このフォーマットとスキームを使って、CSVファイルを準備してください。</Anchor>
3. ここをクリックして、<Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">AppsFlyerのパートナーアカウントへログインしてください。</Anchor>
4. <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#upload-file">ファイルをアップロード・インポートしてください。</Anchor>
5. AppsFlyerの管理画面上で、インポート状況を確認してください：

   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">ステータス</Anchor>
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#matched-rows">一致した行数</Anchor>
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">コストインポートアクション</Anchor>
6. その他の作業：
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">以前に取り込んだ広告費の上書き</Anchor>
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">インポートのキャンセル</Anchor>

<div id="submission-by-email" />

#### メールでの提出

**コストインポート ファイルを電子メールで送信するには:**

1. ［作業するアプリ毎に都度必要です］<Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-permissions-for-ad-networks">広告主に対して、広告費インポートの権限を付与するよう依頼してください。</Anchor>
2. <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#prepare-csv-file-with-cost-data">このフォーマットとスキームを使って、CSVファイルを準備してください。</Anchor>
3. コストインポートのトークンを持っていない場合 (ファイルをメールで送信する際に必要です)：
   * こちらをクリックして、<Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">AppsFlyerのパートナーアカウントへログインしてください。</Anchor>
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#token-for-email-import">広告費用のトークンを取得してください。</Anchor> （注意：同じトークンがすべての広告主に対して使用されます。 ）
4. <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#email-file">メール</Anchor> でファイルを送信してください。
5. AppsFlyerからステータスレポートがメールで送信されます。(インポートが成功したかどうか、または問題が見つかったかどうかが記録されます。)　**注：** ステータスメールを受信しなかった場合は、<Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">コストインポートダッシュボードを</Anchor>参照してください。
6. AppsFlyerの管理画面上で、インポート状況を確認してください：

   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">ステータス</Anchor>
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#matched-rows">一致した行数</Anchor>
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">コストインポートアクション</Anchor>
7. その他の作業：
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">以前に取り込んだ広告費の上書き</Anchor>
   * <Anchor target="_blank" href="/marketers/ja/docs/import-cost-data#cost-import-dashboard">インポートのキャンセル</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=%E5%BA%83%E5%91%8A%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%AE%E3%82%B3%E3%82%B9%E3%83%88%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88 h_01HX94WSX07YEG40X66TMRFJGA=%E5%BA%83%E5%91%8A%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%AE%E3%82%B3%E3%82%B9%E3%83%88%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88 overview=%E6%A6%82%E8%A6%81 h_01HX94WSX0HR2KTGRT7MQ481Y6=%E6%A6%82%E8%A6%81 submitting-ad-spend-files-for-ad-networks=%E5%BA%83%E5%91%8A%E8%B2%BB%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91 h_01HX94WSX0G429FTHKYCG07BB9=%E5%BA%83%E5%91%8A%E8%B2%BB%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91 submission-by-file-upload=%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%AB%E3%82%88%E3%82%8B%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E6%8F%90%E5%87%BA h_01HX94WSX0ENTJEDMXWRHDCP0D=%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%AB%E3%82%88%E3%82%8B%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E6%8F%90%E5%87%BA submission-by-email=%E3%83%A1%E3%83%BC%E3%83%AB%E3%81%A7%E3%81%AE%E6%8F%90%E5%87%BA h_01HX94WSX0HVTMFQQ0NMW0VSKP=%E3%83%A1%E3%83%BC%E3%83%AB%E3%81%A7%E3%81%AE%E6%8F%90%E5%87%BA" />
