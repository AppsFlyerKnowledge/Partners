---
title: ポストバックマクロ：アナリティクスパートナー向け
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2021-01-04T04:44:40Z'
  edited_at: '2026-10-14T09:29:55Z'
  id: 360016751637
  locale: ja
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ja/articles/360016751637
---
> **概要：** 概要： 関連する計測データをアナリティクスパートナーに対してポストバックで送信する際に利用可能なマクロについて記載しています。

## アナリティクスパートナーへのポストバック

アドネットワークは、AppsFlyerとの連携の一環として、AppsFlyerから送信されるポストバックの内容とエンドポイントの情報を定義する必要があります。 ポストバックは、インストール、アプリ内イベント、リエンゲージメントなど、アプリユーザーのエンゲージメント全般に関連します。

## ポストバックのマクロ

マクロをポストバックに含めることで、ポストバック時に関連する実際のユーザーデータに自動的に置き換えられます。たとえば、インストール時のユーザーのIPアドレスを取得するには、ポストバックURLに"&country\_code=(ip)"を追加します。サポートされているマクロについては以下の表を参照してください。

* ソース：データソース： データの取得元がどこかを示しています。
  * SDKSDK＝アプリに実装されているAppsFlyerSDK、もしくはServer-to-ServerのAPI
  * AppsFlyer計測：AF＝AppsFlyer側で処理した情報
* [基本] すべてのポストバック向け
* **[オプション] アプリ内イベント向け：** アプリ内イベントのデータ専用のマクロです。

#### インストールおよびアプリ内イベントのマクロ

| ポストバックマクロ名 | ソース | 説明 | [基本] すべてのポストバック向け | [オプション] アプリ内イベント向け |
| --- | --- | --- | --- | --- |
| advertising\_id | SDK | ユーザーがリセット可能なデバイスID（別名GAID）。(sha1-advertiserId)も使用可能 | はい |  |
| event\_name | SDK | 各イベントに割り当てられたイベント名 |  | はい |
| event\_revenue\_USD | AF | イベントの値（USD（米ドル）） |  | はい |
| event\_revenue | SDK | event\_revenue\_currency もしくは 予め選択した通貨単位を使ってSDKによってレポートされるイベント値 |  | はい |
| event\_revenue\_currency | SDK | イベントでレポートされたイベント収益の通貨コード、もしくは予め選択された通貨単位 |  | はい |
| event\_time | SDK | Event time |  | はい |
| event\_value | SDK | アプリ内イベントに含まれるvalueの情報は、JSON形式ですべて送信可能です。URLは(encode)のマクロを使用してエンコードされます。 |  | はい |
| partner\_event\_id | AF | パートナーのプラットフォームで発生したイベントと照合するための名前またはID |  | はい |
| app\_name | SDK | 広告主が設定したアプリ名 | はい |  |
| appsflyer\_id | SDK | コンバージョン時に記録されるAppsFlyerにおけるユニークID | はい |  |
| attributed\_touch\_type | AF | ビュースルーによってアトリビューションが発生したかどうかを示すフラグ（1 =impression、0 =click） | はい |  |
| country\_code | AF | ISO 3166 (alpha-2)を使用した国コード：US, CN など米国、中国。 | はい |  |
| idfa | SDK | ユーザーがリセット可能なiOSの広告ID＝IDFAで、(sha1-idfa)も使用可能 | はい |  |
| idfv | SDK | iOS端末において、アプリベンダー毎にユーザー毎に発番される一意の識別子 | はい |  |
| install\_time | SDK | インストールのタイムスタンプ | はい |  |
| install\_unix\_ts | SDK | UNIXフォーマットでのインストールのタイムスタンプ | はい |  |
| is\_lat | SDK | 追跡型広告の制限（LAT）:iOS 14以降、LATはAppleによって非推奨となります。ATTを使用してユーザーのプライバシーステータスを決定します。この場合、is\_latを無視します。iOS 14より前では、trueの場合、IDFAは利用できず、0に設定されます。Android:trueの場合、ユーザーは興味に基づく広告をオプトアウトしています。これはGAIDの収集を妨げるものではありません。 | はい |  |
| 言語 | SDK | 端末OSによって設定され、端末から取得した言語設定(+地域情報) | はい |  |
| app\_id | SDK | AppsFlyerで使用される一意のアプリ識別子 | はい |  |
| app-version-name | SDK | 開発者によってアプリのコードに設定された、アプリのバージョン | はい |  |
| attributed\_touch time | AF | ユーザーの広告接触時間 | はい |  |
| device\_type | SDK | デバイスの商用モデル名。例： | はい |  |
| ip | AF | イベント記録時のユーザー端末のIPアドレス | はい |  |
| マッチタイプ | AF | アトリビューション手法のタイプ。例：srn / id\_matching / probabilistic | はい |  |
| os\_version | SDK | デバイスのOSバージョン | はい |  |
| user\_agent | SDK | URLのユーザーエージェント | はい |  |
| Wi-Fi | SDK | trueの場合、各種イベントの計測時にWi-Fiに接続していたことを示します | はい |  |
| oaid | SDK | 一部のAndroidデバイスでユーザーがリセット可能なIDで、通常GAIDの代替として使用されます。 | はい |  |
| platform | SDK | デバイスプラットフォーム：iOS、Android、またはWindows Mobile | はい |  |
| retargeting\_conversion\_type | SDK | リアトリビューション、またはリエンゲージメントであるかどうかを示すフラグ | はい |  |
| pid | AF | インストールまたはアプリ内イベントが紐付けられたアドネットワークの識別ID | はい |  |
| af\_ad | リンク | 広告主/パブリッシャーが提供した広告名（<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#データの詳細度の階層">詳細</Anchor>） | はい | はい |
| af\_ad\_id | リンク | 広告主/パブリッシャー提供 | はい | はい |
| af\_adset | リンク | <ul><li>広告主/パブリッシャーによって提供されます。</li><li>広告セットはキャンペーンと広告の間の階層の中間レベルです。<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#データの詳細度の階層">もっと見る</Anchor></li></ul> | はい | はい |
| af\_adset\_id | リンク | 広告主/パブリッシャー提供 | はい | はい |
| c | リンク | 広告主/パブリッシャーによって提供されます。 | はい | はい |
| af\_c\_id | リンク | 広告主/パブリッシャー提供 | はい | はい |
| af\_siteid | リンク | <ul><li>広告を表示するパブリッシャーを識別する一意のID。<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#site-id-parameter">詳細はこちら</Anchor></li></ul> | はい | はい |
| af\_subsite\_id | リンク | <ul><li>アドネットワークのサブネットワーク／パブリッシャーID。</li><li>メインパブリッシャー（サイトID）に加えてサブパブリッシャーがある場合、またはバナー、インタースティシャル、ビデオなど、アプリ内の広告タイプ／配置情報を含める場合は、af\_sub\_siteidを使用します。例: af\_sub\_siteid =ABCD\_4567</li></ul> | はい | はい |
| af\_ad\_type | リンク | 以下の命名規則を利用してください：<ul><li>**テキスト：** テキストのみを含む広告ユニット(例：検索結果など）</li><li>**バナー：** 画面の上部または下部に表示される基本フォーマット</li><li>**インタースティシャル：** 画面閲覧中に差し込まれる、インターステシャル広告</li><li>**ビデオ：** リワード広告ではない通常の動画広告</li><li>**rewarded\_video:** 動画視聴と引き換えにアプリ内報酬を提供するリワード動画広告</li><li>**プレイアブル：** 実際のアプリ操作が一部可能な、インタラクティブな広告</li><li>**sponsored\_content:** 広告記事のようなスポンサードコンテンツに含まれるリンク</li><li>**オーディオ：** 音声広告</li></ul> | はい | はい |

## アプリ内イベント専用マクロ

以下の例では、パートナーが利用可能なアプリ内イベントのポストバックについて紹介しています。

> 📄 **例**
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> `{"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`このポストバックのデコードされたJSONの値は次のようになります。

### エンコードされる値

ポストバックに、 英数字以外の特殊文字が含まれる場合があります。ポストバック時にこれらの値を正しく送信するために、AppsFlyerではポストバック内の英数字以外の値をURLエンコードします。  
ポストバックをデコード、もしくはエンコードする場合には、[各種エンコードのWebサービス](https://www.urldecoder.org/)を利用してください。

## ポストバックの例

### 一般的なインストールポストバックの例

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?pid=(media_source)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?pid=(media source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)
```

</Tab>
</Tabs>

### 一般的なアプリ内イベントのポストバックの例

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>
</Tabs>

## アプリ内イベントのポストバック例

**イベントパラメータ：**

* イベント名：af\_revenue
* イベント収益2024-02-26
* 。USD

**ポストバック：**

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&android_id=9aaeecc4455xxxxx&install_time=1451923560&event_name=af_purchase&currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-analytics-partners=%E3%82%A2%E3%83%8A%E3%83%AA%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E3%81%B8%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JH2HWTN05T8S3P4W6CKVA7K4=%E3%82%A2%E3%83%8A%E3%83%AA%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E3%81%B8%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF postback-macros=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD 01JH2HWTN52E8CVVGTQWK3QXW6=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD macros%E2%80%94installs-and-inapp-events=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%8A%E3%82%88%E3%81%B3%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD 01JH2HWTN7XY6B55TED4NT2KRR=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%8A%E3%82%88%E3%81%B3%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD inapp-event-only-macros=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%B0%82%E7%94%A8%E3%83%9E%E3%82%AF%E3%83%AD 01JH2HWTVN8880HZSF6V6XZ7EF=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%B0%82%E7%94%A8%E3%83%9E%E3%82%AF%E3%83%AD encoded-values=%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89%E3%81%95%E3%82%8C%E3%82%8B%E5%80%A4 01JH2HWTVNARNYV0M9AKHQ0NDA=%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89%E3%81%95%E3%82%8C%E3%82%8B%E5%80%A4 sample-postbacks=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B 01JH2HWTVNQT0NPJ7SG9424MTQ=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B general-install-postback-examples=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B 01JH2HWTVN4DDQ6F70WP3XE19D=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B general-inapp-event-postback-examples=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B 01JH2HWTVN2MH2SB6W34DH2MF7=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B inapp-event-postback-example=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E4%BE%8B 01JH2HWTVP50J5WV11DZR3RSTM=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E4%BE%8B" />
