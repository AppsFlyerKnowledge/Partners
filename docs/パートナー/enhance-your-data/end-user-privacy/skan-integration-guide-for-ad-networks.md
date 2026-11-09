---
title: SKAN連携ガイド：アドネットワーク向け
metadata:
  keywords:
    - Ad Networks
    - Partners
    - SKAD
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2020-08-03T08:56:14Z'
  edited_at: '2026-10-14T09:20:58Z'
  id: 360011502657
  locale: ja
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ja/articles/360011502657
---
> **概要**：概要：このページでは、SKAdNetwork (SKAN) におけるアドネットワークとAppsFlyerの連携方法、キャンペーンの最適化の方法や各アドネットワークが生み出したトラフィックに成果を紐付ける方法などを記載しています。

<div id="appsflyer-offering-for-ad-networks" />

## AppsFlyerが提供するもの

参考：**広告主向けのSKAdNetworkソリューション**：

<Anchor target="_blank" href="/marketers/ja/docs/skadnetwork-skan-solution-guide">SKANソリューションガイド</Anchor>|<Anchor target="_blank" href="/marketers/ja/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKANダッシュボード</Anchor>

* **キャンペーンの成果紐付け：**
  * AppsFlyerとのSKAd連携により、SKAdNetworkによって計測されたインストール、アプリ内イベント、収益といった情報を、弊社SKAdNetworkの管理画面上でご自身のアドネットワークの成果として紐付けることが可能になります。
  * SKAd連携が行われていない場合、インストール、アプリ内イベント、収益といった情報はアドネットワークへは紐付けられず、すべてオーガニックとして計測されます。
* **キャンペーンの最適化の手助け：**
  * ポストバックに含まれているコンバージョン値はエンコードされています。
  * AppsFlyerと連携することで各ポストバックに含まれているコンバージョン値を解読することができるので、アプリ毎に解読されたコンバージョン値の情報に基づいて、アドネットワーク側でキャンペーンの最適化に活用できるようになります。
* **各広告主との直接連携が不要：** SKANのポストバックはアドネットワークにのみ送信され、広告主は以下のいずれかの方法でデータを取得できます：
  * 各アドネットワークとの個別連携。（アドネットワークと広告主、双方にとって拡張性のないソリューション）
  * AppsFlyerとの単一連携。（アドネットワークと広告主、双方にとって容易で拡張性のあるソリューション）
* **AppsFlyer上でもSKAdNetworkの連携状況をアピール：**
  * SKAdNetworkの連携が完了したアドネットワークは、AppsFlyerの管理画面上でもその認証が付与されます。
  * この認証表示により、SKAdNetworkによる計測をサポートしたアドネットワークを使用していることを、各広告主は確認できるようになります。

<div id="skan-data-flow" />

## SKAdNetworkのデータフロー

<Image align="center" alt="5754_Postback_flow_for_SKAD__1_.png" src="https://files.readme.io/dff0fb00721802f59d199ae6a69f9ea7484bc0ef038c669904aa1a7c2b97dfc8-12574373654161.png" />

SKANのポストバックの全体像は以下のような流れになっています：

1. **iOS**から成果を獲得したアドネットワークに対して、SKANのポストバックが送信されます。
2. **アドネットワーク**は以下のいずれかの作業を行います：
   * A：データ追加と転送データの追加と転送：受け取ったSKANのポストバックに、アドネットワークのcampaign ID / ソース識別子、キャンペーン名、iOS端末のIPアドレスを追加して、AppsFlyerへ転送。
   * リダイレクト
3. **AppsFlyer**は受け取ったSKAdNetworkのポストバックを検証・解読し、再度、その解読し情報を追加したポストバックをアドネットワークへ送信します。(広告主側へも管理画面上で情報が提供されます。)

<div id="main-integration-parts" />

## 連携について

この記事でも記載しているように、AppsFlyerとアドネットワークのSKAdNetworkの連携は、以下の2つのパートから構成されています。

* アドネットワークが、SKAdNetworkのデータをAppsFlyerへ送信する。
* アドネットワークが、解読され情報が追加されたSKAdNetworkのデータをAppsFlyerからポストバックで受け取る。

<div id="send-data-to-appsflyer" />

## AppsFlyerへのデータ送信

iOS端末からSKANのポストバックを受け取った後、 アドネットワークは以下のどちらかの方法を使ってAppsFlyerへその情報を転送する必要があります。

* A：データの追加と転送 (POST)
* B：リダイレクト (HTTP 307でのリダイレクト)

そのSKANのポストバックを受信すると、AppsFlyerは以下の処理を実行します。

* データの返信：解読したポストバックの情報をアドネットワークに送信します。
* 管理画面反映：広告主が利用する管理画面とレポートに、SKAdNetworkのデータを表示します。

<div id="enrich-and-forward" />

<Accordion title="A：データ追加と転送">

この方法を使用する場合、アドネットワークがiOS端末から受け取ったSKAdの各ポストバックをAppsFlyerへ転送することになります。

**アドネットワークは：**

* iOS端末からSKAdのポストバックを受信します
* ［必須］ポストバックへ以下内容を追加してください：  
  * アドネットワークのキャンペーンIDとキャンペーン名
  * iOS端末から送信されたポストバックのタイムスタンプ
* ［任意］ポストバックへの以下内容の追加は任意です：
  * iOS端末から受信したIPアドレス (主に地理的情報の目的で必要)
  * Adset Name と Adset ID
  * Ad Name と Ad ID
  * アドネットワーク名
  * Country code
  * ソースアプリID
  * クリエイティブ
  * Channel
* ポストバックをAppsFlyerへ送信
* **注！注意！ポストバックをAppsFlyerに送信する前に、送信するポストバックの内容を使ってAppleの**Attribution Signature/strong>を検証し、データを誤って改変してしまっていないか確認してください。

<div id="skan-enriched-postback-protocol" />

#### SKAdNetworkのデータ追加ポストバックのプロトコル

| エンドポイント | `https://skadpostbacks.appsflyer.com/api/postbacks` |
| --- | --- |
| HTTP メソッド | POST |
| 受け入れ可能なcontent types | `application/json` |
| 返されるコード | 200 OK200 OK：受信したポストバックは有効なフォーマットです。<br /><br />2024-02-26Bad request400：不正なリクエスト：不正な形式のJSON、空のJSONデータ、必須な値の欠損など |

<div id="skan-enriched-postback-json-parameters" />

#### SKAdNetworkのデータ追加ポストバックのJSONパラメータ一覧

| パラメータ | 形式 | 説明 | ソース |
| --- | --- | --- | --- |
| version | 文字列 | SKAdNetworkのversion<br /><br />例： `"version":"2.0"` | SKAN postback |
| ad-network-id | 文字列 | アドネットワークID<br /><br />例： `"ad-network-id":" abc123defg.SKAdnetwork"` | SKAN postback |
| ad-network-name | 文字列 | <ul><li>アドネットワーク名</li><li>例： `ad_network_name=your_network`</li></ul> | アドネットワーク |
| ad-network-country-code | 文字列 | <ul><li>アドネットワークによって判別されたユーザーの位置情報</li><li><Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO</Anchor>  3166 (alpha-2) の国コードを使用してください。</li><li>例：CN, ZA</li><li>アドネットワークではキャンペーンのターゲットとなっている配信地域に応じて、地域情報を導き出すことが多いです。</li><li>AppsFlyerではレポートや管理画面上の地域情報に関する項目を埋めるために、この国コードを利用しています。</li></ul> | アドネットワーク |
| campaign-id | 整数 | <ul><li>SKAN 3以下のみ</li><li>SKAdNetwork campaign ID</li><li>例： `"campaign-id":23`</li></ul> | SKAN postback |
| transaction-id | 文字列 | SKAdNetworkポストバックのtransaction ID | SKAN postback |
| app-id | 整数 | <ul><li>AppsFlyer上に表示されている対象となるアプリIDで、常に冒頭に"id"がつきます。</li><li>例:`app_id=id123456789`</li></ul> | SKAN postback |
| アトリビューション署名 | 文字列 | アトリビューション署名 | SKAN postback |
| redownload | ブール値 | redownload = trueの場合、そのユーザーはストアからそのアプリを再ダウンロードしたことを意味します。 | SKAN postback |
| source-app-id | 整数 | <ul><li>Source App ID (パブリッシャー)</li><li>[Apple のドキュメンテーション](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)を参照</li></ul> | SKAN postback |
| conversion-value | 整数 | AppsFlyer SDKが、広告主が事前に設定した内容に応じて設定したコンバージョン値です。<br /><br />**注意**！<ul><li>Appleのプライバシー保護のしきい値の仕様のため、iOSでポストバック時にパラメータが入力されず、コンバージョン値の値がnullになる場合があります。</li><li>Null と 0 は意味が異なります。<ul><li>Null：Appleがコンバージョン値をマスクした状態。</li><li>2024-02-26０：ユーザーはアプリをインストールしたが、コンバージョン値に関連するイベントを何も行わなかった状態。</li></ul></li></ul> | SKAN postback |
| ad-network-campaign-id | 文字列 | アドネットワーク、広告主、AppsFlyerの3社間で共通言語を持つために、アドネットワークのCampaign IDを提供する必要があります。 | アドネットワーク |
| ad-network-campaign-name | 文字列 | アドネットワークのcampaign IDに関連付けられた、アドネットワークのキャンペーン名です。(AppsFlyerの管理画面上やレポートにも表示されます。) | アドネットワーク |
| ad-network-adset-id | 文字列 | アドネットワークのアドセット単位のID | アドネットワーク |
| ad-network-adset-name | 文字列 | アドネットワークのアドセット名 | アドネットワーク |
| ad-network-ad-name | 文字列 | アドネットワークの広告名 | アドネットワーク |
| ad-network-ad-id | 文字列 | アドネットワークの広告単位のID | アドネットワーク |
| ip | 文字列 | <ul><li>ポストバックを送信するユーザー端末の IP アドレスです。</li><li>IPv4とIPv6のIPアドレスをサポートしています。</li><li>例： `"ip":"198.51.100.1"`</li></ul> | アドネットワーク |
| timestamp | 文字列 | <ul><li>アドネットワークがポストバックを受信した時刻。</li><li>例： 2020年8月4日 07:25 UTC は以下のように変換されます：`"timestamp": "1596525944"`</li></ul> | アドネットワーク |
| fidelity-type | 整数 | <ul><li>アトリビューションに影響する、広告表示方法の違いを区別します。次のように 0と1の値を使用して示されます：<ul><li>0：ビュースルー</li><li>1：クリックスルー（StoreKitでレンダリングされた広告）</li></ul></li><li>SKAdNetworkのV2.2以降では必須のフィールドになります。</li></ul> | SKAN postback (V2.2以上) |
| did\_win | ブール値 | <ul><li>インストールに[貢献したのか、または成果が紐づくキャンペーンなのかを](https://developer.apple.com/documentation/storekit/SKAdnetwork/SKAdnetwork_release_notes/SKAdnetwork_version_3_0_release_notes)区別するのに使用されます。</li><li>trueの場合：キャンペーンはインストールに貢献したとみなされます（ラストタッチアトリビューション獲得）。</li><li>false の場合、キャンペーンはインストールに貢献したことを示しています。</li></ul> | SKAN postback (V3.0以上) |
| ad-network-source-app-id | 文字列 |  | アドネットワーク |
| postback-sequence-index | 整数 | <ul><li>SKAN 4以降のみ</li><li>値はシーケンス番号 (SKAN期間) を示し、0、`0`10、`1`21のいずれかになります。</li></ul> | SKAN 4.0 ポストバック (iOS 16.2) |
| coarse-conversion-value | 文字列 | <ul><li>SKAN 4以降のみ</li><li>値は 、`low` 、`medium` のいずれか。</li><li>最初のポストバックでは、tier 1でのみ利用できます。2回目、3回目のポストバックでは、tier 1-3で利用できます。[Apple のドキュメンテーション](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)を参照</li></ul> | SKAN 4.0 ポストバック (iOS 16.2) |
| source-identifier | 文字列 | <ul><li>SKAN 4以降のみ</li><li>値は最大4桁です。</li><li>最初のポストバックでは、tier 2-3では最大4桁、tier 0-1 では2桁を使用できます。2番目と3番目のポストバックでは、tiers 1-3 では2桁を使用できます。tier 0 ではポストバックはありません。[Apple のドキュメンテーション](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)を参照</li></ul> | SKAN 4.0 ポストバック (iOS 16.2) |
| source-domain | 文字列 | <ul><li>SKAN 4以降のみ</li><li>値は、アトリビューション可能なウェブ広告のソースを示します。`example.com` example.com例</li><li>[Apple のドキュメンテーション](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)を参照</li></ul> | SKAN 4.0 ポストバック (iOS 16.2) |
| クリエイティブ | 文字列 | <ul><li>SKAN 4以降にのみ</li><li>キャンペーンの粒度を高めるために source\_identifier で追加の数字を使用する場合に使用できます</li></ul> | アドネットワーク |
| channel | 文字列 | <ul><li>SKAN 4以降にのみ</li><li>キャンペーンの粒度を高めるために source\_identifier で追加の数字を使用する場合に使用できます</li></ul> | アドネットワーク |

<div id="curl-exampleenriched-skan-3-postback" />

#### **Curlの例—データを追加したSKAN 3のポストバック**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version":"3.0",
      "app-id": 888707086,
      "ip": "192.0.2.0",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "source-app-id": 888707074,
      "ad-network-id": "abcabcabc.skadnetwork",
      "transaction-id": "68eb3d91-15f5-44ee-9267-25c7655c20b6",
      "redownload": false,
      "attribution-signature": "MDYCGQCsQ4y8d4BlYU9b8Qb9BPWPi+ixk/OiRysCGQDZZ8fpJnuqs9my8iSQVbJO/oU1AXUROYU=",
      "timestamp": "1596525944",
      "ad-network-campaign-id": "222222",
      "conversion-value": 63,
      "campaign-id": 99
  }'
```

<div id="curl-exampleenriched-skan-4-postback-with-fine-conversion-values" />

#### **Curlの例—細かいコンバージョン値でデータを追加したSKAN 4のポストバック**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "5239",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e30",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "conversion-value": 63
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIGRmSMrqedNu6uaHyhVcifs118R5z/AB6cvRaKrRRHWRAiEAv96ne3dKQ5kJpbsfk4eYiePmrZUU6sQmo+7zfP/1Bxo="
  }'
```

<div id="curl-exampleenriched-skan-4-postback-with-coarse-conversion-values" />

#### **Curlの例—粗いコンバージョン値でデータを追加したSKAN 4のポストバック**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "39",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e31",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "coarse-conversion-value": "high"
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIQD4rX6eh38qEhuUKHdap345UbmlzA7KEZ1bhWZuYM8MJwIgMnyiiZe6heabDkGwOaKBYrUXQhKtF3P/ERHqkR/XpuA="
  }'
```

</Accordion>

<div id="redirect" />

<Accordion title="B：リダイレクト">

<Image align="center" alt="Redirect_us-en__2_.png" src="https://files.readme.io/17d4a668cde784a2f823e702e04fc75a2bbbdb483e44d9d10edfad03d865bbb7-360012352758.png" />

この方法を使用する場合、アドネットワークはHTTPのリダイレクトコマンド(307)でiOS端末からのポストバックに応答し、AppsFlyerに対して直接ポストバックを送信するようにiOS端末に要求することになります： 

このリダイレクトの方法には以下の利点があります：

<div id="implementation" />

#### **実装について**

1. HTTP 307 のレスポンスで応答するようにサーバーを設定し、ポストバックを *[https://skadredirect.appsflyer.com/api/redirects](https://skadredirect.appsflyer.com/api/redirects)* へリダイレクトさせてください。
2. 以下の表に記載されているクエリパラメータを使って、キャンペーンの詳細な情報を追加してください。なお、キャンペーン詳細の送信は必須です。キャンペーン詳細を送信してもらうことで、SKAdNetworkの情報をより充実させ、広告主はキャンペーンをより効果的に最適化することが可能になります。

**リダイレクトURLの例**

```http
https://skadredirect.appsflyer.com/api/redirects?
  &ad-network-campaign-id=243232&ad-network-campaign-name=yarg_campaign_name
  &ad-network-adset-name=dsdsa&creative=examplecreative&channel=channelexample
```

<div id="query-params-for-campaign-details-not-mandatory" />

#### キャンペーン詳細のクエリパラメータ(必須ではないです)

| クエリパラメータ | 説明 |
| --- | --- |
| ad-network-name | <ul><li>アドネットワーク名</li><li>`ad_network_name=your_network` ad\_network\_name=your\_network例</li></ul> |
| ad-network-campaign-id | Campaign ID |
| ad-network-campaign-name | キャンペーン名 |
| ad-network-adset-id | Adset ID |
| ad-network-adset-name | Ad set name |
| ad-network-ad-id | Ad ID |
| ad-network-ad-name | 広告名 |
| ad-network-country-code | <ul><li>アドネットワークによって判別されたユーザーの位置情報</li><li><Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO</Anchor>  3166 (alpha-2) の国コードを使用してください。</li><li>例：CN, ZA</li><li>アドネットワークではキャンペーンのターゲットとなっている配信地域に応じて、地域情報を導き出すことが多いです。</li><li>AppsFlyerではレポートや管理画面上の地域情報に関する項目を埋めるために、この国コードを利用しています。</li></ul> |
| ad-network-source-app-id |  |
| ip | <ul><li>ポストバックを送信するユーザー端末の IP アドレスです。</li><li>IPv4とIPv6のIPアドレスをサポートしています。</li><li>`"ip":"198.51.100.1"` "ip":"198.51.100.1"例</li></ul> |
| timestamp | <ul><li>アドネットワークがポストバックを受信した時刻。</li><li>例： 2020年8月4日 07:25 UTC は以下のように変換されます：</li></ul> |
| クリエイティブ | <ul><li>SKAN 4以降にのみ</li><li>キャンペーンの粒度を高めるために source\_identifier で追加の数字を使用する場合に使用できます</li></ul> |
| channel | <ul><li>SKAN 4以降にのみ</li><li>キャンペーンの粒度を高めるために source\_identifier で追加の数字を使用する場合に使用できます</li></ul> |

</Accordion>

<div id="receive-data-from-appsflyer" />

## AppsFlyerからのデータ受け取り

AppsFlyerから最初のデータを受け取る前に、以下の点を確認してください：

* アドネットワークは、予めAppsFlyerからデータを受け取るエンドポイントとそのテンプレートを定義する必要があります(詳細は担当PDM、もしく<Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">パートナーアシスタントウィジェット</Anchor>を使用してご連絡ください)。
* AppsFlyerは、既存のポストバックと同じメカニズムを使って、SKAdNetworkのポストバックをアドネットワークへ送信します。

<div id="principles" />

<Accordion title="原則">

* アドネットワークからAppsFlyerへ送信されたSKAdNetworkの各ポストバックについて、AppsFlyerは以下を送信します：
  * Installのポストバックを1つ送信
  * ゼロ件もしくは複数件のアプリ内イベントのポストバック。正確な件数は、コンバージョン値の変換によって変動します。詳細はこちらを参照してください。

</Accordion>

<div id="postback-macros-available-to-ad-network-partners" />

<Accordion title="アドネットワークパートナーが利用できるポストバックマクロ">

<table><thead><tr><th><p>ポストバックマクロ名</p></th><th><p>説明</p></th><th>フォーマットとサンプル</th><th>アプリ内イベント専用</th></tr></thead><tbody><tr><td><p>site_id</p></td><td><p>広告を掲載しているアプリ (Source app ID)</p></td><td><p>文字列：876534</p></td><td></td></tr><tr><td><p>install_time</p></td><td><p><em>updateConversion</em>の期間に基づいて、AppsFlyerが推定</p></td><td><ul><li>文字列：1596119460 </li><li>July 30, 2020, 14:31 UTC へ変換されます。</li></ul></td><td> </td></tr><tr><td><p>skadnetwork_ad_network_time</p></td><td><p>アドネットワークがiOS端末からポストバックを受信した時刻です。アドネットワークからレポートされたもの</p></td><td><ul><li>文字列：1596119460 </li><li>July 30, 2020, 14:31 UTC へ変換されます。</li></ul></td><td> </td></tr><tr><td><p><br/>skadnetwork_received_time</p></td><td><p>AppsFlyerがアドネットワークからポストバックを受け取った時間</p></td><td><ul><li>文字列：1596119460 </li><li>July 30, 2020, 14:31 UTC へ変換されます。</li></ul></td><td></td></tr><tr><td><p>event_name</p></td><td><p>Event name </p><ul><li>af_skadnetwork_revenue</li><li>ログイン</li><li>af_skadnetwork_revenue</li><li>または広告主が設定したもの </li></ul></td><td><p>String: af_skadnetwork_revenue, abc123</p></td><td><p>はい</p></td></tr><tr><td><p>revenue</p></td><td><p>指定された通貨コードを使用した収益金額です。</p></td><td><p>数値2024-02-26</p></td><td><p>はい</p></td></tr><tr><td><p>currency</p></td><td><p>広告主によって設定された、アプリ固有の通貨コード。</p></td><td><p>文字列：</p></td><td><p>はい</p></td></tr><tr><td><p>attribution_source</p></td><td><p>計測データのソース：</p><p>SKAdNetworkSKAdNetwork</p></td><td><p>文字列：SKAdNetwork</p></td><td></td></tr><tr><td><p>app_id</p></td><td><p>App ID (広告主アプリ)</p></td><td><p>文字列：ID123456790</p></td><td></td></tr><tr><td><p>country</p></td><td><p>アドネットワークによって決定されてたインストール時に位置(国)情報</p></td><td><p>文字列： </p></td><td></td></tr><tr><td><p>campaign</p></td><td><p>アドネットワークからのポストバック時に送信された、<em>ad-network-campaign-name</em>のパラメータで設定されたキャンペーン名です。</p></td><td><p>文字列：</p></td><td></td></tr><tr><td><p>campaign_id</p></td><td><p>アドネットワークからのポストバック時に送信される、<em>ad-network-campaign-id</em>のパラメータで設定された、アドネットワークのキャンペーンIDです。　<strong>注：</strong>注意：SKAN4の場合、この値は常にnullになります。</p></td><td><p>文字列：3456745</p></td><td></td></tr><tr><td><p>redownload</p></td><td><p>入る値: true もしくは false</p><p>redownload = trueの場合、そのユーザーはストアからそのアプリを再ダウンロードしたことを意味します。</p></td><td><p>Boolean: true, false</p></td><td></td></tr><tr><td><p>skadnetwork_ambiguous_event</p></td><td><p>広告主が管理画面上でSKANの設定を変更してから最初の72時間以内に受信したイベントです。SKANで採用されている様々なタイマーの仕様により、AppsFlyerではこのイベントを正確にマッピングすることはできません。</p><ul><li>SKAN 4以降では使用できません。</li></ul></td><td><p>Boolean: true, false</p></td><td></td></tr><tr><td><p>skadnetwork_campaign_id</p></td><td>元々のSKANのポストバックで提供された、SKANのキャンペーンIDです。</td><td><p>56, 23</p></td><td></td></tr><tr><td><p>af_skadnetwork_nonce</p></td><td>重複ポストバックを識別するためのユニークなランダム識別子</td><td></td><td></td></tr><tr><td><p>event_id</p></td><td>アドネットワークのプラットフォーム上で発生した<span> </span><span>イベント</span><span> </span>と照合するための名称またはIDです</td><td></td><td><p>はい</p></td></tr><tr><td><p>トランザクションID</p></td><td><p><span>SKAdNetworkポストバックのtransaction ID</span></p><p><span><strong>注記:</strong>注： 広告主は、AppsFlyerがパートナーに対してtransaction_idを共有することを明示的に許可する必要があります。広告主に 連携 タブ内で設定を行うように依頼してください。</span></p></td><td></td><td></td></tr><tr><td>ad_network_adset_id</td><td>アドネットワークによって、iOSのポストバックに追加</td><td>文字列</td><td> </td></tr><tr><td>ad_network_adset_name</td><td>アドネットワークによって、iOSのポストバックに追加</td><td>文字列</td><td> </td></tr><tr><td>ad_network_ad_name</td><td>アドネットワークによって、iOSのポストバックに追加</td><td>文字列</td><td> </td></tr><tr><td>ad_network_ad_id</td><td>アドネットワークによって、iOSのポストバックに追加</td><td>文字列</td><td> </td></tr><tr><td>SKAN_min_event_counter</td><td>注(1)を参照してください。</td><td><p>整数</p></td><td>はい</td></tr><tr><td>SKAN_max_event_counter</td><td>注(1)を参照してください。</td><td><p>整数</p></td><td>はい</td></tr><tr><td>SKAN_min_time_post-install</td><td>注(2)を参照してください。</td><td><p>整数</p></td><td>はい</td></tr><tr><td>SKAN_max_time_post-install</td><td>注(2)を参照してください。</td><td><p>整数</p></td><td>はい</td></tr><tr><td>SKAN_min_event_revenue</td><td>注 (3) を参照してください</td><td>実数</td><td>はい</td></tr><tr><td>SKAN_max_event_revenue</td><td>注 (3) を参照してください</td><td><p>実数 </p></td><td>はい</td></tr><tr><td>fidelity-type</td><td><p>アトリビューションに影響する、<span>広告表示方法の違い</span>を区別します。次のように 0と1の値を使用して示されます：</p><ul><li><span>0：ビュースルー</span></li><li>1：クリックスルー（StoreKitでレンダリングされた広告）</li></ul></td><td>整数</td><td> </td></tr><tr><td>skad_af_attribution_flag</td><td><p><span>SSOT (Single Source of Truth)のメカニズム（</span> ）を使用して、ユーザーがAppsFlyerによって成果を紐づけられたかどうかを示すために使用されます。 </p></td><td>ブール値</td><td> </td></tr><tr><td><span>skad_postback_sequence_index</span></td><td><ul><li>値はSKAN期間を（0、1、または2）を表します。</li><li>SKAN 3の場合：常に0</li></ul></td><td><span>整数</span></td><td> </td></tr><tr><td><span>skad_coarse_conversion_value</span></td><td><ul><li>値は<span> 、<code>low</code> 、<code>medium</code> のいずれか。</span> </li><li>SKAN 3の場合：常に0</li></ul></td><td><span>文字列</span></td><td> </td></tr><tr><td><span>skad_source_identifier</span></td><td><ul><li>値は最大4桁です。</li><li>SKAN 3の場合：常に0</li></ul></td><td><span>文字列</span></td><td> </td></tr><tr><td><span>skad_source_domain</span></td><td><ul><li>値は、アトリビューション可能なウェブ広告のソースを示します。</li><li>SKAN 3の場合：常に0</li></ul></td><td><span>文字列</span></td><td> </td></tr><tr><td><span>ad_network_creative</span></td><td><ul><li>値はアドネットワークから取得したデータの拡充に基づいています。</li><li>SKAN 3の場合：常に0</li></ul></td><td><span>文字列</span></td><td> </td></tr><tr><td><span>ad_network_channel</span></td><td><ul><li><span>SKAN 4以降にのみ</span></li><li>キャンペーンの粒度を高めるために <span>source_identifier</span> で追加の数字を使用する場合に使用できます</li></ul></td><td><span>文字列</span></td><td> </td></tr><tr><td colspan="4"><p>注：</p><ol><li> イベントの発生<br/><code>[round up (SKAN_min_event_counter+SKAN_max_event_counter) / 2]</code><br/>ご注意ください値は最も近い整数の値に切り上げられます。</li></ol><ul><li>例： <ul><li>A. 例1) min=0、max=1の場合、イベント発生数は1として記録されます。</li><li>B. 例1) min=0、max=1の場合、イベント発生数は1として記録されます。</li></ul></li><li> install_timeの決定に仕様： カスタムコンバージョン値を利用している広告主の場合、AppsFlyerではポストバック到着時間 - 48h - ("min_time_post_install" + "max_time_post_install")の平均値 をインストール時間(install_time)として計算しています。原則、アドネットワーク側ではこのマクロを利用する必要はありません。    </li><li> 収益金額の決定：AppsFlyerはこれらの値を使い、min と maxの合計した平均値を計算してイベントの収益を決定します。  </li></ul></td></tr></tbody></table>

</Accordion>

<div id="skan-postback-examples" />

<Accordion title="SKANのポストバックの例">

**AppsFlyerから送信される、SKANのインストールのポストバック例：**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)
  &attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

**AppsFlyerから送信される、SKANのアプリ内イベントのポストバック例：**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)&revenue=(value)
  &currency=(code)&event_name=(event-name)&attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

</Accordion>

<div id="integration-testing" />

## 連携テスト

AppsFlyerとの連携を検証するには、以下方法のいずれか、もしくは両方を使用してください。 

* 実際のSKANのポストバックでテスト：アドネットワークが受け取った実際のSKANのデータを利用
* ポストバックの模擬テスト：AppsFlyerのテストアプリを利用

**実際のSKAdNetworkのポストバックをiOS端末から受け取るには、アドネットワークは以下作業を完了する必要があります：**

* Appleに申請する
* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/generating_the_signature_to_validate_storekit-rendered_ads">SKAdNetwork Signatureで広告に署名する</Anchor>
* 広告掲載アプリパブリッシャー(配信面)アプリ：network IDをinfo.plist fileに追加/a><Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/generating_the_signature_to_validate_an_installation">して、</Anchor>広告のインプレッション時にloadProduct functionを呼び出す。
* 広告主アプリ

**ポストバックの模擬テストを受け取るには：**

* <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">パートナーアシスタントウィジェット</Anchor>を使用して、シミュレーションアプリとの連携をリクエストしてください。
* AppIDは、[以下のセクション](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks)に記載のあるリストの中から指定してください。

<div id="real-environment" />

<Accordion title="実環境でのテスト">

この方法を使用する場合、アドネットワークは広告主のアプリで実際のSKANのポストバックをAppsFlyerへ送信することになります。

<div id="testing-integration" />

#### 連携のテスト

| 担当者 | アクション |
| --- | --- |
| アドネットワーク | Appleから提供されたSKAN Network IDを、担当PDMへ（もしくはパートナーアシスタントウィジェットを使用して）共有してください。 |
| アドネットワークとAppsFlyer | ポストバック連携の検証に使用する広告主(最新のAppsFlyerSDKを実装済み)について、合意形成してください。 |
| アドネットワーク | このページに記載されているいずれかの方法を使って、SKANのポストバックをAppsFlyerに送信してください。 |
| AppsFlyer | 広告主が設定したコンバージョン値の計測設定に従って、解読したポストバックをアドネットワークへ送信します。 |

<div id="test-criteria" />

#### テストの判定基準

| 担当者 | アクション |
| --- | --- |
| アドネットワーク | 合意形成した広告主において、指定期間中に送信したSKAdNetworkのポストバックの数をAppsFlyerに共有してください。 |
| AppsFlyer | 受信したポストバックの数と、アドネットワークからの送信数を確認します。 |
| AppsFlyer | そのアプリについてアドネットワークに送信されたポストバックの数を、タイプ別に分けてアドネットワークへ共有します。<ul><li>インストール / 再インストールのポストバック</li><li>アプリ内イベントのポストバック</li></ul>注：注意：確率論的モデリングなどの計測でも同じエンドポイントを使用する場合には、 *attribution\_source=skadnetwork* /span>のパラメータを使ってデータをフィルタリングし 、SKANのポストバックを他のポストバックと区別するようにしてください。 |

</Accordion>

<div id="simulated-postbacks" />

<Accordion title="ポストバックの模擬テスト">

* この方法を使用する場合、次の表に記載されているように、アドネットワークは事前準備されたポストバックの内容をAppsFlyerのテストアプリに送信することになります。そして、AppsFlyerはコンバージョン値を解読したポストバックをアドネットワークへ返信します。
* 表に記載されているように、テストアプリ毎に異なるコンバージョン値のマッピングが用意されています。

| App ID | SKAdNetworkの計測設定 | 手順： |
| --- | --- | --- |
| <span id="id888707085"></span>id888707085 | ［収益］を選択し、単位は$1<br /><br />想定の結果： | <ol><li>[連携 ] タブにて、[**アプリ内イベントのポストバック**]を有効にしてください。</li><li>af\_SKAN\_revenueのイベントを選択して、御社側のイベント識別名を選択してください。(御社側の識別名を設定しない場合もございます)</li><li>設定を保存してください。</li><li>ポストバックにて、conversion value = 7 を送信してください。</li><li>AppsFlyerは以下の内容で応答します：<ul><li>Installのポストバックを1つ送信</li><li>af\_skad\_revenueのポストバックを1つ送信し、値は$7</li></ul></li></ol> |
| <span id="id888707086"></span>id888707086 | ［コンバージョン］を選択し、アプリ内イベントは以下を選択：<ul><li>af\_level\_complete</li><li>ログイン</li><li>af\_SKAN\_revenue</li><li>af\_register</li><li>af\_subscription</li><li>af\_custom\_event</li></ul> | <ol><li>[連携 ] タブにて、[**アプリ内イベントのポストバック**]を有効にしてください。</li><li>予めリストアップした各アプリ内イベントをマッピングし、御社側のイベント識別子も選択してください。(御社側の識別名を設定しない場合もございます)</li><li>設定を保存してください。</li><li>ポストバックにて、conversion value = 63 を送信してください。</li><li>AppsFlyerは以下の内容で応答します：<ul><li>Installのポストバックを1つ送信</li><li>af\_level\_completeのポストバックを1つ送信</li><li>af\_loginのポストバックを1つ送信</li><li>af\_SKAN\_revenueのポストバックを1つ送信</li><li>af\_registerのポストバックを1つ送信</li><li>af\_subscriptionのポストバックを1つ送信</li><li>af\_custom\_eventのポストバックを1つ送信</li></ul></li></ol> |
| <span id="id888707087"></span>id888707087 | ［エンゲージメント］を選択し、af\_SKAN\_revenueのイベントで計測 | <ol><li>[連携 ] タブにて、[**アプリ内イベントのポストバック**]を有効にしてください。</li><li>af\_SKAN\_revenueのイベント を選択して、*御社側のイベント識別子も設定してください。*(御社側の識別名を設定しない場合もございます)</li><li>設定を保存してください。</li><li>ポストバックにて、conversion value = 3 を送信してください。</li><li>AppsFlyerは以下の内容で応答します：<ul><li>Installのポストバックを1つ送信</li><li>af\_SKAN\_revenueのイベントのポストバックを3つ送信</li></ul></li></ol> |

<div id="integration-steps" />

#### 連携手順

| 担当者 | アクション |
| --- | --- |
| アドネットワーク |  |
| アドネットワーク | <ol><li><Anchor target="_blank" href="/partners/ja/docs/turn-on-test-app-integration-for-ad-networks">テストアプリをアクティブ化してください。</Anchor></li><li>各アプリにて、前の表の［作業(instructions)］の内容を完了してください。</li><li>前述の表に記載されているテストアプリを使用して、ポストバック送信の模擬テストを実施してください。ポストバックの模擬テストを送信するときの注意点：<ul><li>app\_idとconversion valueは、前述の表に記載されているものを設定してください。</li><li>アドネットワークではAppleのCompatible Signatureを生成できないため、ポストバックの模擬テストにはSignatureフィールドを含める必要はありません。(AppsFlyerでは、ポストバックの模擬テストでは検証を行いません。)</li><li>POSTもしくはREDIRECTのどちらかを使用して、ポストバックを送信してください。</li></ul></li></ol> |
| AppsFlyer | 連携時に定義したアドネットワークのエンドポイントに対し、解読されたポストバックを返します。 |

<div id="test-criteria-1" />

#### テストの判定基準

| 担当者 | アクション |
| --- | --- |
| AppsFlyer | ポストバックを処理し、ポストバックをアドネットワークへ送信する。 |
| アドネットワーク | <ul><li>解読されたポストバックを受け取り、デコードする。</li><li>AppsFlyerから送信されたアプリ内イベントのポストバックが、想定されたデータフローと合致する。例：ID888707087のアプリでコンバージョン値が3の場合、アドネットワークは*af\_SKAN\_revenue*のイベントのポストバックを3つ受信</li></ul> |

</Accordion>

<div id="clarifications" />

## 詳細

必須項目、データ追加、認証などに関する詳細を記載しています。

<div id="faq" />

<Accordion title="よくある質問">

| ポストバックに関するQA |
| --- |
| **データ追加で必要な各パラメータは必須ですか？**<br /><br />現時点では、以下の各追加パラメータが1つ以上不足していた場合でも、そのポストバックをAppsFlyerは処理します。ただし、以下のような理由からもこれらの情報が必要であることを考慮してください。<ul><li>ad\_network\_campaign\_id</li><li>ad-network-campaign-name</li><li>IPアドレス</li><li>timestampタイムスタンプ：インストールを正しい日付に紐付けるのに活用します。</li></ul> |
| 両方ではなく、キャンペーンIDまたはキャンペーン名のいずれかのみを送信することは可能ですか？<br /><br />前の回答を参照してください。キャンペーンIDとキャンペーン名の両方に同じ値を設定することも検討してください。 |
| はい、可能です。アトリビューション署名が有効なのであれば、追加された情報は無視しつつポストバックは処理します。 |
| SKAdNetworkのポストバックテンプレートは、既存のポストバックテンプレートとは異なるものですか？<br /><br />はい。データの流れと構造が異なります。 |
| 1つのインストールついて、SKAdNetworkのポストバックと既存のAppsFlyer SDKの計測でのポストバック、つまり重複したポストバックを受け取ることになりますか？<br /><br />はい。それぞれの場合において、AppsFlyerはあなたのアドネットワークに起因したインストールを記録し、その計測方法に関係なく、アドネットワークにそれぞれのポストバックを送信します。<br /><br />SKAdNetworkのポストバックを区別するには、attribution\_sourceのパラメータを活用してください。 |
| **私たちもAppsFlyerからのポストバックを処理する必要がありますか？**<br /><br />その必要はありません。ただし、ポストバックを通じて報告されたユーザーの質に応じて、キャンペーンの最適化を行えることが理想的です。 |
| **AppsFlyerの計測リンクを呼び出す必要がありますか？それともSKAdNetworkのペイロードとデータ追加したポストバックを送信するだけで十分ですか？**<br /><br />SKAdNetworkのペイロードとデータ追加したポストバックを送信するだけで大丈夫です。 |
| **SKAdNetworkの連携パートナーとしてAppsFlyerの管理画面上で認証をもらうには、何が必要ですか？**<ul><li>この記事に記載されている方法を使用して、AppsFlyerとの連携を完了させてください。</li><li>AppsFlyerを計測SDKとして使用しているアプリのSKAdNetworkのポストバックを送信してください。</li></ul> |
| **SKAdNetworkが持つ、キャンペーンIDの上限数が100という制限はどのような影響を与えますか？**<br /><br />これは100のID制限によってAppsFlyer側で計測するキャンペーンの数は制限されないことを意味します。もちろん、特定アプリに対して同時に配信しているキャンペーン数が100を超えないという条件の下の仕様になります。 |

</Accordion>

<div data-zendesk-anchors="appsflyer-offering-for-ad-networks=appsflyer%E3%81%8C%E6%8F%90%E4%BE%9B%E3%81%99%E3%82%8B%E3%82%82%E3%81%AE h_01HDG8991Y6EWWN9KYBR9FEAJZ=appsflyer%E3%81%8C%E6%8F%90%E4%BE%9B%E3%81%99%E3%82%8B%E3%82%82%E3%81%AE skan-data-flow=skadnetwork%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E3%83%95%E3%83%AD%E3%83%BC h_01HDG8991Y5DW0BVD674RS88F2=skadnetwork%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E3%83%95%E3%83%AD%E3%83%BC main-integration-parts=%E9%80%A3%E6%90%BA%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HDG8991YDTY85NK7TQ26B2Z1=%E9%80%A3%E6%90%BA%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 send-data-to-appsflyer=appsflyer%E3%81%B8%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E9%80%81%E4%BF%A1 h_01HDG8991YTFP2HE0Y8P8X0C20=appsflyer%E3%81%B8%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E9%80%81%E4%BF%A1 h_01HDG8991YRW3TWSDARFM58FA8=enrich-and-forward skan-enriched-postback-protocol=skadnetwork%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E8%BF%BD%E5%8A%A0%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB h_01HDG8991YAKZMSA4MAY0YTFPB=skadnetwork%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E8%BF%BD%E5%8A%A0%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB skan-enriched-postback-json-parameters=skadnetwork%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E8%BF%BD%E5%8A%A0%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AEjson%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E4%B8%80%E8%A6%A7 h_01HDG8991YS91CWESZH0M7CA00=skadnetwork%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E8%BF%BD%E5%8A%A0%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AEjson%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E4%B8%80%E8%A6%A7 curl-example%E2%80%94enriched-skan-3-postback=curl%E3%81%AE%E4%BE%8B%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%97%E3%81%9Fskan-3%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01HDG8991YFHBQDRG4K0XA3JQ8=curl%E3%81%AE%E4%BE%8B%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%97%E3%81%9Fskan-3%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF curl-example%E2%80%94enriched-skan-4-postback-with-fine-conversion-values=curl%E3%81%AE%E4%BE%8B%E7%B4%B0%E3%81%8B%E3%81%84%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E5%80%A4%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%97%E3%81%9Fskan-4%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01HDG8991YNVCK92TVNJHGKNG5=curl%E3%81%AE%E4%BE%8B%E7%B4%B0%E3%81%8B%E3%81%84%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E5%80%A4%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%97%E3%81%9Fskan-4%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF curl-example%E2%80%94enriched-skan-4-postback-with-coarse-conversion-values=curl%E3%81%AE%E4%BE%8B%E7%B2%97%E3%81%84%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E5%80%A4%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%97%E3%81%9Fskan-4%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01HDG8991YXTS27V0NJ4ZXQ53T=curl%E3%81%AE%E4%BE%8B%E7%B2%97%E3%81%84%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E5%80%A4%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%97%E3%81%9Fskan-4%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01HDG8991YGHWJ9R1ZKTCFJZCA=redirect implementation=%E5%AE%9F%E8%A3%85%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HDG8991YBR7VWRH9079GT695=%E5%AE%9F%E8%A3%85%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 query-params-for-campaign-details-not-mandatory=%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E8%A9%B3%E7%B4%B0%E3%81%AE%E3%82%AF%E3%82%A8%E3%83%AA%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E5%BF%85%E9%A0%88%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E3%81%A7%E3%81%99 h_01HDG8991YQB77MMF906PCAWC2=%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E8%A9%B3%E7%B4%B0%E3%81%AE%E3%82%AF%E3%82%A8%E3%83%AA%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E5%BF%85%E9%A0%88%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E3%81%A7%E3%81%99 receive-data-from-appsflyer=appsflyer%E3%81%8B%E3%82%89%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E5%8F%97%E3%81%91%E5%8F%96%E3%82%8A h_01HDG8991ZNF2PKKJN3FPN6QXA=appsflyer%E3%81%8B%E3%82%89%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E5%8F%97%E3%81%91%E5%8F%96%E3%82%8A h_01HDG8991ZKR35WHWVX0DHC612=principles h_01HDG8991ZG9GMMY57XYZF1Q3S=postback-macros-available-to-ad-network-partners h_01HDG8991ZD6ARRK6Z83NQBGRR=skan-postback-examples integration-testing=%E9%80%A3%E6%90%BA%E3%83%86%E3%82%B9%E3%83%88 h_01HDG8991ZS10MJJ3ZN31YDPTK=%E9%80%A3%E6%90%BA%E3%83%86%E3%82%B9%E3%83%88 h_01HDG8991ZPR41S5T9HZ9N1ZWF=real-environment testing-integration=%E9%80%A3%E6%90%BA%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 h_01HDG8991ZJ1KTHX6FE9R0QJNP=%E9%80%A3%E6%90%BA%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 test-criteria=%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E5%88%A4%E5%AE%9A%E5%9F%BA%E6%BA%96 h_01HDG8991ZP59K8RQQ7G1GGMPG=%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E5%88%A4%E5%AE%9A%E5%9F%BA%E6%BA%96 h_01HDG8991Z7DX65Y3E6RPHB2M3=simulated-postbacks integration-steps=%E9%80%A3%E6%90%BA%E6%89%8B%E9%A0%86 h_01HDG8991ZZPYH7H329EY8TNV9=%E9%80%A3%E6%90%BA%E6%89%8B%E9%A0%86 test-criteria::26c15d59=%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E5%88%A4%E5%AE%9A%E5%9F%BA%E6%BA%96-1 h_01HDG8991ZR4F21KVYF0MQ9GZA=%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E5%88%A4%E5%AE%9A%E5%9F%BA%E6%BA%96-1 clarifications=%E8%A9%B3%E7%B4%B0 h_01HDG8991Z8C0K0SMBT9VSX12Y=%E8%A9%B3%E7%B4%B0 h_01HDG8991ZDAGFV8GGC1RH73KQ=faq" />
