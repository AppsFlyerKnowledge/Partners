---
title: Protect360：連携済みパートナー向け
metadata:
  keywords:
    - Protect360
    - Ad Networks
    - Partners
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2017-09-19T08:27:29Z'
  edited_at: '2026-10-14T09:32:29Z'
  id: 115004745523
  locale: ja
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/ja/articles/115004745523
---
> **概要：** 概要： 連携済みパートナー(アドネットワークと代理店)は、ProtectLITEとProtect360、広告主によって定義された検証ルールによって検知・ブロックされたトラフィックの情報を確認可能です。

<div id="overview" />

## 概要

AppsFlyerでは以下の機能で不正を検知・ブロックします。

* ProtectLITE
* Protect360Protect360：追加の有償契約をした広告主向けのより高度な不正対策機能

パートナーが不正検知機能を利用するには、広告主側で以下作業が必要です：

* アドネットワーク｜<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">Protect360の管理画面とローデータへのアクセス（ProtectLITEを含む）と、**集計されたアプリ内イベントデータへのアクセス**（アプリ内イベント不正向け）の**権限付与**</Anchor>
* 代理店｜<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">Protect360の管理画面とローデータへのアクセスの**権限付与**</Anchor>

また適宜権限を付与してもらうことで、連携済みパートナーは以下が可能になります：

* 関係するアドネットワークが生み出したトラフィックに関するデータの閲覧
* 関連する<Anchor target="_blank" href="/marketers/ja/docs/protect360-anti-fraud-guide#raw-data">ローデータレポート</Anchor>のダウンロード

また、クリックとインプレッションの上限設定、失敗したクリック署名については、アドネットワークが利用できるローデータレポートがあり、これについては広告主の許可は必要ありません。

<div id="note" />

> 📘 **注意**
>
> 代理店を通してアドネットワークを利用している広告主の場合、代理店とアドネットワークの両方がデータにアクセスするためには、広告主がAppsFlyerの管理画面上で代理店とアドネットワークの両方の連携設定を行い、権限付与とP360へのアクセスを付与する必要があります。
>
> 代理店のみが統合され、許可が与えられている場合は、アドネットワークはデータにアクセスできません。

<div id="dashboard-view" />

### 管理画面表示

前提条件前提条件：ProtectLite / Protect360へのアクセスに関する、広告主からの権限付与が必要です。

連携済みパートナーは、管理画面とグラフを確認できるようになります。(詳細は以下のスクリーンショットを確認してください。)

ProtectLITE<Anchor target="_blank" href="/marketers/ja/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting#ダッシュボード">と</Anchor> Protect360の<Anchor target="_blank" href="/marketers/ja/docs/protect360-anti-fraud-guide#dashboard">画面</Anchor>で利用可能なデータの詳細についてはこちらを参照してください。

制限：

* 代理店アカウントはアクセス権を持っていますが、他のメディアソースと比較するための基準値を作成できるように、AppsFlyerによって保証されているメディアソースからのトラフィックにおいて不成立が低い場合にのみ、データが表示されます。

[![p360_dashboard_1.jpg](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)

<div id="raw-data-reports" />

### ローデータレポート

**前提条件**前提条件：ProtectLite / Protect360へのアクセスに関する、広告主からの権限付与が必要です。

Protect360のローデータレポートでは、ProtectLITE / Protect360 / 検証ルールによって検知・ブロックされた不正データを提供しています。

利用可能なレポート：

* データをエクスポートAppsFlyerのサイドメニューから、 **レポート** > **ローデータ出力/span>** を選択します。
* API*API：アドネットワーク向けのレポートAPIのセクションを確認してください。

Protect360のローデータレポートの詳細については<Anchor target="_blank" href="/marketers/ja/docs/protect360-raw-data-reports">こちら</Anchor>を参照してください。

<div id="protect360-ad-network-reporting-api" />

## Protect360のアドネットワーク向けレポートAPI

* アドネットワークは、このセクションに記載されているローデータレポートをAPI経由で利用可能です。
* 同様のレポートは、管理画面内のデータエクスポートのページからも取得可能です。
* 広告主が Protect360を契約していない場合には、インストールのレポートのみが閲覧可能です。

**前提条件**

* 広告主のデータにAPIでアクセスするには、予め広告主がアドネットワークに対して、"Protect360管理画面とAPIでのローデータへのアクセスを許可する"という<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">権限を付与</Anchor>している必要があります。
* Protect360へのアクセス権限を持っているアプリの一覧については、<Anchor target="_blank" href="/partners/ja/docs/app-list-api-for-ad-networks">アプリリストの取得API</Anchor>を使用してください。
* パートナーアカウントのAdminアカウントは、AppsFlyerの管理画面からAppsFlyerの<Anchor target="_blank" href="/marketers/ja/docs/managing-appsflyer-tokens">V2.0 認証トークン</Anchor>を取得する必要があります。

<div id="protect360-api-reports" />

#### Protect360 APIレポート

| レポート | データ更新頻度 | 説明 |
| --- | --- | --- |
| ポストアトリビューションアプリ内イベント不正 | 毎日10:00 UTC | <ul><li>不正と特定されたインストールが実行したアプリ内イベント</li><li>インストールに関係なく、その他すべての不正と判断されたアプリ内イベント</li></ul>次のパラメータに関する表に示すとおり、このレポートはオプションとしてアプリ内イベントの種類で絞り込むことができます。<br /><br />`fraud-post-inapps`report\_topic: |
| アトリビューション後のインストール | 毎日10:00 UTC | <ul><li>アトリビューション後に不正と特定されたインストール</li><li>次のセクションで説明するとおり、このレポートはオプションとして検知日で絞り込むことができます。</li></ul>レポートトピック： detection |
| インストール | リアルタイム | ブロック済みインストールとブロックされた理由<br /><br />レポートトピック： blocked\_installs\_report |
| アプリ内イベント | リアルタイム | ブロックされたユーザーが実行したアプリ内イベント<br /><br />`blocked_in-app_events_report`report\_topic: |
| クリック | リアルタイム | ブロックされたユーザーが実行したクリック<br /><br />`blocked_clicks_report`report\_topic: |

<div id="procedure-for-ad-networks-to-get-protect360-reports-by-download" />

#### **Protect360のローデータレポートをダウンロードして取得する手順**

**APIを使用する場合：**

1. 前述の表から、取得したいレポートを決めてください。
2. 関連するCurlサンプル (以下参照) を使用して、スクリプトを準備してください。
3. 以下のプレースホルダをそれぞれ置き換えてください：
   1. App ID
   2. From date (開始日)
   3. To date (終了日)
   4. Bearer token  (AppsFlyer <Anchor target="_blank" href="/marketers/ja/docs/managing-appsflyer-tokens">V2.0 認証トークン</Anchor>)
4. 記事内に記載のあるように、一部のコールには[オプションのパラメータ](/docs/protect360-for-integrated-partners#api-parameters)もあります。

<div id="curl-examples" />

### Curl サンプル

<div id="installs-blocked_installs_report" />

<Accordion title="インストール (blocked_installs_report)">

app\_id / from / to / tokenのプレースホルダを書き換えてください。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_installs_report/app/{app_id}?from={2020-07-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-installs-detection" />

<Accordion title="ポストアトリビューションインストール (detection)">

app\_id / from / to / tokenのプレースホルダを書き換えてください。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/detection/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additonal-fields=fraud_reason,fraud_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="inapp-event-blocked_in_app_events_report" />

<Accordion title="アプリ内イベント (blocked_in_app_events_report)">

app\_id / from / to / tokenのプレースホルダを書き換えてください。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_in_app_events_report/app/?from=YYYY-MM-DD&to=YYYY-MM-DD&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="postattribution-inapp-events-fraud-fraud_post_inapps" />

<Accordion title="ポストアトリビューションのアプリ内イベント不正 (fraud_post_inapps)">

app\_id / from / to / tokenのプレースホルダを書き換えてください。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/fraud-post-inapps/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,fraud_reason,fraud_sub_reason,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="clicks-blockedclicks_report" />

<Accordion title="クリック (blocked-clicks_report)">

app\_id / from / to / tokenのプレースホルダを書き換えてください。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_clicks_report/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="protect360-ad-network-api-reference-guide" />

### Protect360 アドネットワーク API 仕様ガイド

<div id="api-basics" />

<Accordion title="APIの基本">

Protect360 アドネットワークAPIの基礎仕様：

| 経路 | `https://hq1.appsflyer.com/api/adnets-data/v1/export/report_topic/app/app_id` |
| --- | --- |
| メソッド | GET |
| Pathの必須パラメータ | <ul><li>`app_id`：<ul><li>AppsFlyerの管理画面上にも表示されているアプリの識別子です。管理画面上に表示されているものを正しく入力してください。</li><li>iOSは冒頭に**id**もつけてアプリIDを記載してください。</li></ul></li><li>**`report_topic`**</li></ul> |
| 受け入れ可能なcontent types | `application/json` |
| 承認 | <ul><li>リクエストヘッダー内のBearer tokenで行います。</li><li>このトークンの長さは約700文字です。</li></ul> |
| レート制限 | <Anchor target="_blank" href="/marketers/ja/docs/report-generation-quotas-rate-limitations">レート制限</Anchor> |
| 日付範囲の制限 | <ul><li>現在の日付から3-5日前</li><li>過去90日までのうち31日間までのデータ</li></ul> |
| 行数の上限 | 20万行 |
| レポート特性 | <ul><li>タイムゾーンUTC</li><li>通貨:USD</li></ul> |

</Accordion>

<div id="api-parameters" />

<Accordion title="API パラメータ">

Protect360のAPIパラメータ：

| パラメータ | 説明 | 形式 | 必須 |
| --- | --- | --- | --- |
| app\_id | AppsFlyerの管理画面上に表示されているアプリID | 文字列 | はい |
| 開始日 | 日付範囲の開始:<ul><li>インストールの場合、これはインストール日です。</li><li>アプリ内イベントの場合、これがイベントの日付です。</li></ul> | YYYY-MM-DD | はい |
| 終了日 | 日付範囲の終了:<ul><li>インストールの場合、これはインストール日です。</li><li>アプリ内イベントの場合、これがイベントの日付です。</li></ul> | YYYY-MM-DD | はい |
| イベント名 | [ポストアトリビューションアプリ内イベントの不正オプション]<br /><br />アプリ内イベントでイベントをフィルタリングします。レポートを特定のイベントに限定します。1つ以上のイベントを含めることができます。<br /><br />使用例: `&event_name=af_purchase,af_login` | 文字列 | いいえ |
| 検出開始日 | [ポストアトリビューションインストールの場合にはオプション]<br /><br />不正検出日付範囲の終了。（デフォルトは from）。 | YYYY-MM-DD | いいえ |
| 検出終了 | [ポストアトリビューションインストールの場合にはオプション]<br /><br />不正検出日付範囲の終了。(デフォルトは終了日です。) | YYYY-MM-DD | いいえ |

</Accordion>

<div id="protect360-api-http-return-codes" />

<Accordion title="Protect360 APIのHTTPリターンコード">

エラーコードと解決策：

| ステータス | コード | 症状／メッセージ | 解決策 |
| --- | --- | --- | --- |
| OK | 200 | Empty CSV file（CSVファイルが空です） |  |
| OK | 200 | Empty CSV file（CSVファイルが空です） | 開始日と終了日の両方の形式がyyyy-mm-ddであることを確認してください |
| OK | 200 | AppsFlyer HTMLログインページの戻り値 | Bearer tokenヘッダーにトークンがありません。 |
| Bad request | 400 | Bad request | <ul><li>日付範囲の制限<ul><li>過去データのサポート範囲：現在から90日前まで</li><li>インストールの場合は60日、アプリ内イベントのレポートの場合には90日を超える期間は取得できません。</li></ul></li></ul> |
| Unauthorized | 401 | Unauthorized | トークンは見つかりましたが、有効ではありません。パートナーアカウント内に現在のV2.0トークンが存在していることを確認し、Adminに管理画面から現在のトークンを改めて取得するよう依頼してください。 |
| Not found | 404 |  | <ul><li>指定されたエンドポイントが正しくありません。</li><li>App IDが正しいことを確認してください。</li><li>アプリへのアクセス権限がありません。</li></ul> |

</Accordion>

<div id="impression-capping" />

## インプレッションとクリックの上限ブロック(capping)

アドネットワークが非常に高いインプレッションとクリックの不正率を示す場合、Protect360はアドネットワークのインプレッションとクリックを24時間のサイクルでブロックします。つまり、閾値に達したあとに発生したインプレッションとクリックはAppsFlyerで記録されず、アトリビューションの対象にもなりません。これらのブロックされたインプレッションとクリックの情報は、Protect360の管理画面とレポートにのみ表示されます。

アルゴリズムは動的であり、変化する傾向を考慮して時間単位で更新されます。

インプレッションやクリックの増大により閾値に達することが繰り返し発生した場合、AppsFlyerのプラットフォームとの連携を永久的に削除する可能性もあります。

インプレッションとクリックの上限ブロックの閾値について： 

* すべてのアドネットワークに対して、平等に適用されます。つまり、インプレッション不正やクリック不正の割合が極端に高くても上限ブロックされないアドネットワークは存在しません。
* アプリ/アドネットワークレベルである。つまり、不正分析では、アプリ上のすべてのアドネットワークのキャンペーンが考慮され、ブロックは、アプリ上のすべてのアドネットワークのキャンペーンのレポートとアトリビューションに影響します（アカウントにProtect360があるかどうかに関係なく）。
* 24時間サイクルでブロックはリセットされ、サイクルが終了するまではブロックが適用されます。サイクルの開始と終了の詳細については、非公開です。
* 変更または停止できません。Protect360は、不正検出において細かい調節がなされており、そのアルゴリズムは手動で調整または無効にすることはできません。
* 異常なアクティビティを持つキャンペーンとパブリッシャー(配信面)を停止することで、回避できる可能性があります。

<div id="faq" />

<Accordion title="よくある質問">

インプレッションとクリックの上限ブロックに関するFAQ：

| **Q:Q：ネットワークに適用される閾値はどれくらいですか？**<br /><br />A. |
| --- |
| **Q:Q：ブロックを解除するにはどうしたらいいですか？**<br /><br />**A**: |
| **Q:Q: 上限ブロックは、Protect360を未使用のAppsFlyerの広告主にも適用されますか？**<br /><br />**A**:A: はい、キャッピングは、顧客がProtect360を持っているかどうかに関係なく影響します。キャッピングメカニズムは、クリック / インプレッションの不正使用からすべての顧客を保護します。 |
| **Q:**<br /><br />**A**: |
| **Q:Q：ブロックされることによってキャンペーンの拡大が困難になってしまうため、インプレッションやクリックの上限ブロックを行わないでください。**/strong><br /><br />**A**: 万が一それでも懸念がある場合には、AppsFlyerまでお問い合わせください。 |
| **Q:**<br /><br />**A**:A: ボリュームの処理に問題はありません。 |
| **Q:Q：インストールに加え、クリックもブロックするというアプローチに至ったのはなぜですか？**<br /><br />A. |
| **Q:Q：新しいキャンペーンなどにより、インプレッション数・クリック数が大幅に増加すると予想される場合はどうなりますか？ブロックされるのを防ぐためには何ができますか？**<br /><br />A.A：アルゴリズムは動的であり時間単位で更新されるため、さまざまな傾向を考慮します。このような増加を処理するのに十分洗練されており、突然の大幅なボリューム増加を含む通常の範囲の活動変動によってブロックが実行されることはありません。A: 連携済みパートナーは、インプレッション/クリックのデータとレポートを使用して、疑わしいソースを特定してキャンペーンを停止可能です。 |
| **Q:Q：問題のあるトラフィックをチェックし、キャンペーンのパフォーマンスを向上させるにはどうすればよいですか?**<br /><br />A.A: 連携済みパートナーは、インプレッション/クリックのデータとレポートを使用して、疑わしいソースを特定してキャンペーンを停止可能です。パートナーは、広告主からダッシュボードで不正行為データを表示するために必要な許可を得ている限り、Protect360/ProtectLITEダッシュボードの専用列でブロックされたインプレッションとクリックのデータを確認することもできます。 |
| **Q:Q: ネットワークには上限に関する通知メールが送信されますか?**<br /><br />A.A: クリック制限の場合、AppsFlyerはクリック上限のしきい値に達するたびに広告ネットワークにメール通知を送信します。/span> |

</Accordion>

<div id="click-signing" />

### クリック署名

この署名によりAppsFlyerはクリックを検証でき、 クリック情報が不正業者によって操作されていないことを確認します。

* 検証されたクリックは記録され、アドネットワークへ紐付けられます。
* 無効になったクリックは除外され、以下のように処理されます：
  * アドネットワーク向け(広告主向けではなく)に提供されるProtect360のレポート画面に集計されます。
  * アドネットワークのコンバージョン率やクリックの上限ブロックの閾値には影響を与えません。

<div data-zendesk-anchors="overview=%E6%A6%82%E8%A6%81 h_01HGSXTKYQB4Q1QQX4ZQS60AAJ=%E6%A6%82%E8%A6%81 h_01HGSXTKYQN42EEMPSZMWVAMWD=%E6%B3%A8%E6%84%8F dashboard-view=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E8%A1%A8%E7%A4%BA h_01HGSXTKYQPQP72R2VJB68ZDRZ=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E8%A1%A8%E7%A4%BA rawdata-reports=%E3%83%AD%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HGSXTKYQWRZECN905RGSEQ42=%E3%83%AD%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 protect360-ad-network-reporting-api=protect360%E3%81%AE%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88api h_01HGSXTKYQ9388SCQTT2MX59Q9=protect360%E3%81%AE%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88api protect360-api-reports=protect360-api%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HGSXTKYQXZN2DMNZ09HE7355=protect360-api%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 procedure-for-ad-networks-to-get-protect360-reports-by-download=protect360%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%81%97%E3%81%A6%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86 h_01HGSXTKYQ913MF0G38B23NYBG=protect360%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%81%97%E3%81%A6%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86 curl-examples=curl-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB h_01HGSXTKYQX3VN5NRMNQWW4AE4=curl-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB h_01HGSXTKYQQBJTM4ZMMQZ0VZNH=installs-blocked_installs_report h_01HGSXTKYQ5KTCD7K63DSVS6E2=postattribution-installs-detection h_01HGSXTKYQ6MA96W8E6R2SXBS5=inapp-event-blocked_in_app_events_report h_01HGSXTKYQMMC0WNWP56Q9J0ZS=postattribution-inapp-events-fraud-fraud_post_inapps h_01HGSXTKYQEG0JXJHS7QBAEBCA=clicks-blockedclicks_report protect360-ad-network-api-reference-guide=protect360-%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF-api-%E4%BB%95%E6%A7%98%E3%82%AC%E3%82%A4%E3%83%89 h_01HGSXTKYQJRE1Y9C5RSCANWT2=protect360-%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF-api-%E4%BB%95%E6%A7%98%E3%82%AC%E3%82%A4%E3%83%89 h_01HGSXTKYQE24FAPYHHMFP0B3X=api-basics h_01HGSXTKYRFSZRPHNPDHNREDH2=api-parameters h_01HGSXTKYRGSQ230NVN06SP6DG=protect360-api-http-return-codes impression-and-click-capping=%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AC%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%A8%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%AE%E4%B8%8A%E9%99%90%E3%83%96%E3%83%AD%E3%83%83%E3%82%AFcapping h_01HGSXTKYRN6TP3KDYX5YZJV7N=%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AC%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%A8%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%AE%E4%B8%8A%E9%99%90%E3%83%96%E3%83%AD%E3%83%83%E3%82%AFcapping h_01HGSXTKYR8BK5A2J6TJECMKZA=faq click-signing=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D h_01HGSXTKYR915V6E4NWGWR61PG=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E7%BD%B2%E5%90%8D" />
