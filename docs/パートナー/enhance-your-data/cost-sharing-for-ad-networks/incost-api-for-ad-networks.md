---
title: InCost API：アドネットワーク向け
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Marketers
    - ROI360
    - Ad Networks
  created_at: '2020-04-26T19:13:47Z'
  edited_at: '2026-10-14T09:35:28Z'
  id: 360007714957
  locale: ja
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ja/articles/360007714957
---
> **概要：** AppsFlyer の ROI360 の機能の一部である InCost API を使用することで、アドネットワークは広告のコストデータを AppsFlyer へ送信できるようになります。そうすることで、広告主に集計コストデータが提供され、あなたのアドネットワークの本当のパフォーマンスを理解してもらえるようになります。

<div id="about-incost-api" />

## InCost API について

InCost API は、アドネットワークが AppsFlyer へコストデータを送信するためのソリューションです。アドネットワークは、API を使用して広告の詳細なコストデータを AppsFlyer へ送信します。AppsFlyer がそのデータを取り込んで処理するので、管理画面やレポート上で広告主やパートナーが利用できるようになります。

<div id="benefits" />

#### メリット

* 円滑なコストレポートにより、広告主があなたのアドネットワークの本当のパフォーマンスを理解するのを助けます。コストデータがなければ、広告主は計測データの重要な部分を見逃してしまい、ROAS を正確に計測することができません。そのため、誤って他のメディアソースに投資し、収益に悪影響を及ぼす可能性があります。
* 正確でリアルタイムなコスト計測を担保するこのソリューションで ROI を証明してください。
* InCost API は迅速かつ簡単に実装でき、利用開始までの期間も短いです。また、最大で過去90日間のコストデータを送り返す機能など、データをいつどのように送信するかを完全に制御できます。
* InCost APIでは、CPI（クリックURL経由でコスト情報を共有する場合は唯一対応）だけでなく、すべてのコスト形式をサポートしています。
* AppsFlyerのPartner Marketplace上でも、InCost APIの連携が完了すれば「コスト」のバッジが付与されます。

<div id="note" />

<div id="implementing-incost-api" />

## InCost API の実装

**前提条件**：InCost API の実装を行うには、以下の条件を満たす必要があります。

* 計測しているキャンペーンの90%において、データにaf\_c\_id（キャンペーンID）が含まれていること。
* データの鮮度向上のために、1日に6回以上コストデータを送信できること。（具体的な送信時間はアドネットワーク次第です。）
* （コストデータを過去に遡って更新したい場合）データの完成度向上のため、過去7日間のコストデータを毎回送信できること

**InCost API を実装して、コストデータの送信を始めるには**：

* 以下の手順に従ってください。

| ステップ # | 対応事項 |
| --- | --- |
| 1 | InCost API連携の申請：<ol><li>パートナーアカウントで管理画面に入り、上部メニューの［**ヘルプ**］>［**チームへのお問い合わせ / サポートチケットの提出**］を選択してください。<br />パートナーアシスタントのウィジェットが開きます。</li><li>[**コスト計測を有効にする(Enabling cost measurement)**] を選択して、各種情報を送信してください。<br />フォーム送信後にチケットが作成され、AppsFlyerのパートナーソリューションエンジニアから連絡があります。</li></ol> |
| 2 | あなたのアドネットワークの90%以上のトラフィックにおいて、計測データにキャンペーン階層の情報（af\_c\_id（キャンペーン ID）は必須、af\_adset\_id（アドセットID）、af\_ad\_id（アドID）は任意です）の情報が含まれていることを確認してください。 |
| 3 | AppsFlyerの管理画面から <Anchor target="_blank" href="/marketers/ja/docs/managing-appsflyer-tokens">APIトークン</Anchor>を取得してください。 |
| 4 | API 認証ヘッダーで使用する APIトークンを開発担当者に共有し、以下の3つの APIを<Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-overview">各指示に従って</Anchor>実装するよう依頼してください。<ol><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get">Get app list（アプリリストの取得）</Anchor></li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-uploader-post">InCost upload（コスト情報のアップロード）</Anchor>： JSON にどの項目を入力するかを開発担当者に伝えてください：<ul><li>必須項目はすべて入力する必要があるので注意してください。(空の項目は送信できません。 )</li><li>メディアソースの項目は、そのアドネットワークアカウントに紐づけられているメディアソースのみに制限されます。自社のメディアソースIDが不明な場合は、担当PDMに確認してください。</li><li>コストデータの日付とアプリの日付を揃えるために、Get app permission APIで取得できるアプリ毎の<Anchor target="_blank" href="/marketers/ja/docs/about-data-freshness-and-timezone-support#アプリごとのタイムゾーン設定">タイムゾーン</Anchor>を考慮してください。</li><li>あなたのキャンペーントラフィックにおいてコスト計測の階層に含まれていない項目がある場合は、APIリクエストにも含めないでください。例：af\_adset\_id（広告セットID）/ af\_adset（広告セット名）/ af\_ad\_id（広告ID） / af\_ad（広告名）</li></ul></li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-jobstatus-get">ジョブステータスの取得</Anchor></li></ol> |
| 5 | 連携テスト：<ol><li>ステップ1から続くチケットスレッド内で、APIの実装が完了したことをAppsFlyerへ連絡し、実データではなくAPIテストに使用できる以下アプリの権限を付与してもらってください。<ul><li>com.cost.app</li><li>id888123456</li></ul></li><li>パートナーアカウントで管理画面に入り、左メニューの**連携** > **Partner Marketplace**を選択し、自社媒体を選択してください。</li><li>**連携設定**をクリックしてください。</li><li>テストアプリを1つ選択してください。</li><li>連携画面の**コスト**タブを開いてください。</li><li>**コストデータを取得**のトグルをオンにしてください。</li><li>**コストを保存**をクリックしてください。</li><li>**接続テスト**をクリックします。<br />これでAPIが有効になります。</li></ol> |
| 6 | チケットスレッドにて、連携が正しく機能しているかどうかをAppsFlyerへ確認してください。 |
| 7 | 連携完了後、広告主にAppsFlyer の連携ページのコストタブで、<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#cost-tab">コストデータの取得</Anchor>を有効にしてもらってください。以降、コストデータの受信が開始されます。 |

<div id="fields-for-incost-upload-json" />

### InCost アップロード JSON の項目

<table><thead><tr><th>項目</th><th>必須</th><th>備考</th></tr></thead><tbody><tr><td>date</td><td><span>はい</span></td><td><ul><li><span>コストの発生日</span></li><li> <span>形式：</span><code><span>YYYY-MM-DD</span></code> </li><li> <span>例：</span><code><span>2019-12-30</span></code> </li></ul></td></tr><tr><td>app_id</td><td>必須</td><td><ul><li>AppsFlyer プラットフォームに表示されてるアプリ ID</li><li><span>形式：文字列250文字まで</span></li><li> <span>例： Android：</span><code><span>com.app.name</span></code><span>, </span>iOS：<code>id123456789</code> </li></ul></td></tr><tr><td><span>media_source</span></td><td><span>必須</span></td><td><ul><li><span>AppsFlyer のアドネットワークパートナーアカウントが紐づいている、アドネットワークID（PID）</span></li><li><span>形式：文字列50文字まで</span></li><li> <span>例：</span><code><span>network_int</span></code> </li></ul></td></tr><tr><td><span>af_prt</span></td><td><span>任意\*</span></td><td><ul><li><span><b>代理店アカウントが関係する成果とコストデータの場合は必須です。</b></span></li><li><span>代理店識別子は計測URL内のaf_prtのパラメータへ渡されており、代理店アカウント毎に一意な値を所有しています。</span></li><li><span>形式：文字列50文字まで</span></li><li> <span>例：</span><code><span>agencya</span></code> </li></ul></td></tr><tr><td><span>campaign_id</span></td><td><span>必須</span></td><td><ul><li> <span>計測リンクで送信される</span><code><span>af_c_id</span></code><span>パラメータと同じ値である必要があります</span> </li><li><span>空 (empty) の文字列は禁止です。</span></li><li><span>形式：文字列24文字まで</span></li><li> <span>例：</span><code><span>123abc</span></code><span></span> </li></ul></td></tr><tr><td><span>campaign_name</span></td><td><span>必須</span></td><td><ul><li><span>形式：文字列100 文字まで</span></li><li> <span>例：</span><code><span>my_campaign123</span></code> </li></ul></td></tr><tr><td><span>adset_id</span></td><td>任意\*</td><td><ul><li> <span><code><span>adset_name</span></code></span>を送信する場合は必須です。 </li><li> <span>計測リンクで送信される</span><code><span>af_adset_id</span></code><span>パラメータと同じ値である必要があります</span> </li><li> <span>あなたのコストレポート側で<code><span>adset_id</span></code>をサポートしていない場合には</span>、<span>送信しないでください。</span> </li><li><span>形式：文字列24文字まで</span></li><li> <span>例：</span><code><span>123A</span></code> </li></ul></td></tr><tr><td><span>adset_name</span></td><td><span>任意</span></td><td><ul><li> <span>この項目を送信する場合は、<code><span>adset_id</span></code>も送信する必要があります。</span> </li><li><span>形式：文字列100 文字まで</span></li><li> <span>例：</span><code><span>my_adset_name</span></code> </li></ul></td></tr><tr><td><span>ad_id</span></td><td>任意\*</td><td><ul><li> <code><span>ad_name</span></code>を送信する場合は、この項目も必須です。</li><li> <span>計測リンクで送信している</span><code><span>af_ad_id</span></code><span>  パラメータと同じ値である必要があります。</span> </li><li> <span>あなたのコストレポート側で<code><span>adset_id</span></code>をサポートしていない場合には</span>、<span>送信しないでください。</span> </li><li><span>形式：文字列24文字まで</span></li><li>例：<code>123AB</code> </li></ul></td></tr><tr><td><span>site_id</span></td><td>任意</td><td><ul><li>広告を表示している配信面毎のIDです。</li><li>形式：文字列24文字まで</li></ul></td></tr><tr><td><span>ad_name</span></td><td><span>任意</span></td><td><ul><li> <span>この項目を送信する場合は、<code><span>ad_id</span></code>も送信する必要があります。</span> </li><li><span>形式：文字列100 文字まで</span></li><li>例：<code>Ad-name</code> </li></ul></td></tr><tr><td><span>geo</span></td><td><span>任意</span></td><td><ul><li><span>コストに関連付けて記録された国情報</span></li><li><span>可能であれば、広告が表示された国情報の送付が推奨です。</span></li><li><span>形式： ISO 3166の2文字の国コード</span></li><li> <span>例：</span><code><span>US, CN, ZA</span></code> </li></ul></td></tr><tr><td>currency</td><td><span>必須</span></td><td><ul><li><span>コストの通貨単位</span></li><li><span>形式： ISO 4217の3文字の通貨コード</span></li><li> <span>例：</span> <code><span>USD, EUR, ZAR</span></code> </li></ul></td></tr><tr><td>spend</td><td>必須</td><td><ul><li>指定した通貨単位におけるコスト金額 </li><li>小数点以下5桁まで入力可能です。</li><li>0 (ゼロ)の値も入力可能です。</li><li>マイナスの値は入力できません。</li><li> <code>,</code>(区切り文字)は送信しないでください。</li><li>引用符をつけて値を送信しないでください。 </li><li>形式：10進数</li><li>値の例：<code>1</code> / <code>1.2</code> / <code>1234.20</code> </li></ul></td></tr><tr><td>channel</td><td>任意</td><td><ul><li>計測リンクで送信される<code><span>af_channel</span></code> パラメータと同じ値である必要があります。</li><li>形式：文字列20文字まで</li><li>例：<code>my_channel</code> </li></ul></td></tr><tr><td>keywords</td><td>任意</td><td><ul><li>形式：文字列100 文字まで</li><li>例：<code>abc app</code> </li></ul></td></tr><tr><td colspan="3">\* この項目を送信する必要がある場合もあるので、必ず備考欄を参照してください。</td></tr></tbody></table>

<div data-zendesk-anchors="incost-api=incost-api-%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HE0WCBD9GD66KB1QGQ9MEXBJ=incost-api-%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 benefits=%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88 h_01HKVW85AYFG91PGYE5BDQVJNR=%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88 implementing-incost-api=incost-api-%E3%81%AE%E5%AE%9F%E8%A3%85 h_01HKVWSWTWETTES5ZTNZ05X9VA=incost-api-%E3%81%AE%E5%AE%9F%E8%A3%85 fields-for-incost-upload-json=incost-%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89-json-%E3%81%AE%E9%A0%85%E7%9B%AE h_01HM8VCV81GQ6XQ4NA1EDCZ4K7=incost-%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89-json-%E3%81%AE%E9%A0%85%E7%9B%AE" />
