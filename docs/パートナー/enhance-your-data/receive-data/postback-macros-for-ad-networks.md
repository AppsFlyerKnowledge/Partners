---
title: ポストバックマクロ：アドネットワーク向け
metadata:
  keywords:
    - postbacks
    - Advertisers
    - Ad Networks
    - macros
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
  created_at: '2016-01-11T14:41:40Z'
  edited_at: '2026-10-14T09:30:14Z'
  id: 207273946
  locale: ja
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ja/articles/207273946
---
> **概要：** ポストバックは、インストール、アプリ内イベント、リエンゲージメントなど、アプリユーザーのエンゲージメント全般に関連します。

関連する連携済みパートナー向けのポストバックガイド：

* <Anchor target="_blank" href="/partners/ja/docs/advanced-privacy-guide-postback-macros-for-ad-networks">高プライバシーポストバック</Anchor>
* <Anchor target="_blank" href="/partners/ja/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/ja/docs/rejected-attribution-postbacks-to-integrated-partners">ブロックされたデータのポストバック</Anchor>

<div id="postbacks-for-ad-networks" />

## アドネットワークへのポストバック

* ポストバックの種類： ポストバックは、インストールとアプリ内イベント、ブロックされたインストールとアプリ内イベント(Protect360による不正検知、もしくは検証ルールの違反によるもの)において利用可能です。

<div id="postback-data-sources" />

#### ポストバックデータのソース

| ソース | 説明 |
| --- | --- |
| <Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">計測リンクパラメーター</Anchor> | クリックURLとインプレッションURL上でパートナーによって提供されたパラメータ<br /><br />例：計測リンク上のclick IDのパラメータ - "&click\_id=CLICK\_ID" |
| 各種Partner ID | パートナーから広告主へ提供された一意のID<br /><br />例：app ID, account ID, user ID, network ID |
| SDKによる取得情報 | AppsFlyerのSDKによって端末から取得された情報<br /><br />例：iOSの広告IDは、ポストバック時に"&IDFA=(idfa)"を使うことで取得できます。 |
| AppsFlyerのプラットフォームが取得 | AppsFlyerのプラットフォームによって取得された情報 |
| Protect360と検証ルール | 不正と判定されたインストールと検証ルールを違反したインストール、またそれらに紐付くアプリ内イベントに関する情報 |

<div id="postback-macros" />

## ポストバックのマクロ

マクロをポストバックに含めることで、ポストバック時に関連する実際のユーザーデータに自動的に置き換えられます。たとえば、インストール時のユーザーのIPアドレスを取得するには、ポストバックURLに"`country_code=(ip)`&ip\_address=(ip) country\_code=**(ip)**"を追加します。サポートされているマクロについては以下の表を参照してください。

* **ソース：** データソース： データの取得元がどこかを示しています。
  * リンク：計測リンク
  * SDKSDK＝アプリに実装されているAppsFlyerSDK、もしくはServer-to-ServerのAPI
  * AppsFlyer計測：AF＝AppsFlyer側で処理した情報
* Send all
* [基本] すべてのポストバック向け
* **[オプション] アプリ内イベントとブロックされたイベント向け：** 列に記入されているイベント向けのマクロです。(ブロック / アプリ内イベント)

<div id="macrosinstalls-in-app-events-and-rejected-events" />

#### マクロ名一覧 - インストール / アプリ内イベント / ブロックされたイベント向け

| ポストバックマクロ名 | ソース | Send all | 説明 | [基本] すべてのポストバック向け | [オプション]アプリ内イベントとブロックされたデータ向け |
| --- | --- | --- | --- | --- | --- |
| <span id="advertising_id"></span>advertising\_id | SDK | はい | ユーザーがリセット可能なデバイスID（別名GAID）。(sha1-advertiserId)も使用可能 | はい |  |
| <span id="app_name"></span>app\_name | SDK | はい | 広告主が設定したアプリ名 | はい |  |
| <span id="appsflyer_id"></span>appsflyer\_id | SDK | はい | コンバージョン記録時に発番される、AppsFlyerのユニークID | はい |  |
| <span id="attributed_touch_type"></span>attributed\_touch\_type | SDK | いいえ | 想定値：click, impression, TV, pre-install | はい |  |
| <span id="blocked_reason"></span>blocked\_reason | AF | いいえ | 不正/検証ルールのブロック理由 | いいえ | ブロック |
| <span id="blocked_reason_value"></span>blocked\_reason\_value | AF | いいえ | 不正/検証ルールのブロックに関する値(site IDなど) | いいえ | ブロック |
| <span id="blocked_sub_reason"></span>blocked\_sub\_reason | AF | いいえ | 不正/検証ルールのブロック理由の追加情報 | いいえ | ブロック |
| <span id="bundle_id"></span>bundle\_id | SDK | はい | iOS:単一のアプリまたはiOS内のアプリ群を識別するID（Apple開発者バンドルIDを参照） | はい |  |
| <span id="country_code"></span>country\_code | AF | はい | ISO 3166 (alpha-2)を使用した国コード：US, CN など米国、中国。 | はい |  |
| <span id="event_name"></span>event\_name | SDK | はい | 各イベントに割り当てられたイベント名 | いいえ | アプリ内 |
| <span id="event_revenue_usd"></span>event\_revenue\_USD | AF | はい | イベントの値（USD（米ドル）） | いいえ | アプリ内 |
| <span id="event_revenue"></span>event\_revenue | SDK | はい | event\_revenue\_currency もしくは 予め選択した通貨単位を使ってSDKによってレポートされるイベント値 | いいえ | アプリ内 |
| <span id="event_revenue_currency"></span>{"event_revenue"}  <br />{"_currency"} | SDK | はい | イベントでレポートされたイベント収益の通貨コード、もしくは予め選択された通貨単位 | いいえ | アプリ内 |
| <span id="event_time"></span>event\_time | SDK | はい | Event time | いいえ | アプリ内 |
| <span id="event_value"></span>event\_value | SDK | はい | アプリ内イベントに含まれるvalueの情報は、JSON形式ですべて送信可能です。URLは(encode)のマクロを使用してエンコードされます。 | いいえ | アプリ内 |
| <span id="idfa"></span>idfa | SDK | はい | ユーザーがリセット可能なiOSの広告ID＝IDFAで、(sha1-idfa)も使用可能 | はい |  |
| <span id="idfv"></span>idfv | SDK | はい | iOS端末において、アプリベンダー毎にユーザー毎に発番される一意の識別子 | はい |  |
| <span id="install_time"></span>install\_time | SDK | はい | インストールのタイムスタンプ | はい |  |
| <span id="install_unix_ts"></span>install\_unix\_ts | SDK | はい | UNIXフォーマットでのインストールのタイムスタンプ | はい |  |
| <span id="is_attributed"></span>is\_attributed | AF | はい | インストールまたはイベントがこのメディアソースに成果として紐付けられているかどうかを示すフラグ | はい |  |
| <span id="is_lat"></span>is\_lat | SDK | はい | 追跡型広告の制限（LAT）:iOS 14以降、LATはAppleによって非推奨となります。ATTを使用してユーザーのプライバシーステータスを決定します。この場合、is\_latを無視します。iOS 14より前では、trueの場合、IDFAは利用できず、0に設定されます。Android:trueの場合、ユーザーは興味に基づく広告をオプトアウトしています。これはGAIDの収集を妨げるものではありません。 | はい |  |
| <span id="is_primary_attribution"></span>is\_primary\_attribution | AF | はい | falseの場合には、"is\_retargeting"の項目も参照してください | いいえ | アプリ内 |
| <span id="is_retargeting"></span>is\_retargeting | リンク | いいえ | "is\_primary\_attribution"の項目と組み合わせて使用します。詳細については、<Anchor target="_blank" href="/marketers/ja/docs/resolve-retargeting-double-attribution">リターゲティングイベントの二重計測</Anchor>を参照してください。<br /><br />True(1)の場合、そのイベントはリターゲティングキャンペーンに紐付く形でレポートされ、media\_sourceの値もリターゲティング媒体になります。<br /><br />False(0)でis\_primary\_attributionもfalseの場合、そのイベントはリターゲティングキャンペーンに紐づきますが、media\_sourceの値には元々そのユーザーを獲得した新規獲得媒体が入ります。 | いいえ |  |
| <span id="language"></span>言語 | SDK | はい | 端末OSによって設定され、端末から取得した言語設定(+地域情報) | はい |  |
| <span id="oaid"></span>oaid | SDK | はい | 一部のAndroidデバイスでユーザーがリセット可能なIDで、通常GAIDの代替として使用されます。 | はい |  |
| <span id="partner_event_id"></span>partner\_event\_id | AF | はい | パートナーのプラットフォームで発生したイベントと照合するための名前またはID | いいえ | アプリ内 |
| <span id="platform"></span>platform | SDK | はい | デバイスプラットフォーム：iOS、Android、またはWindows Mobile | はい |  |
| <span id="::10f35742"></span>retargeting\_  <br />conversion\_type | AF | いいえ | リアトリビューション、またはリエンゲージメントであるかどうかを示すフラグ | リターゲティング限定 |  |
| <span id="app_version"></span>app\_version | SDK | はい | アプリのバージョン（開発者によってアプリのコードに設定） | はい |  |
| <span id="app_id"></span>app\_id | SDK | はい | アプリによって記録されたapp ID | はい |  |
| <span id="att01"></span>att-0-1 | SDK | はい | / 想定値：<ul><li>2024-02-261: ATTステータス＝authorized または af\_authorized</li><li>2024-02-260: 上記以外</li></ul> | はい |  |
| <span id="attstatus"></span>ATTのステータス | SDK | はい | iOSによって記録された<Anchor target="_blank" href="/marketers/ja/docs/att-implications-ios-14-and-deprecation-of-lat#attの値">ATTステータス</Anchor>。(authorized、not\_determinedなど )<br /><br />場合によっては値がなく、""が返されることがあります。 | はい |  |
| <span id="af_ad"></span>af\_ad | リンク | いいえ | 広告主/パブリッシャーが提供した広告名（<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#データの詳細度の階層">詳細</Anchor>） | はい | はい |
| <span id="af_ad_id"></span>af\_ad\_id | リンク | いいえ | 広告主/パブリッシャー提供 | はい | はい |
| <span id="af_adset"></span>af\_adset | リンク | いいえ | <ul><li>広告主/パブリッシャーによって提供されます。</li><li>広告セットはキャンペーンと広告の間の階層の中間レベルです。<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#データの詳細度の階層">もっと見る</Anchor></li></ul> | はい | はい |
| <span id="af_adset_id"></span>af\_adset\_id | リンク | いいえ | 広告主/パブリッシャー提供 | はい | はい |
| <span id="c"></span>c | リンク | いいえ | 広告主/パブリッシャーによって提供されます。 | はい | はい |
| <span id="af_c_id"></span>af\_c\_id | リンク | いいえ | 広告主/パブリッシャー提供 | はい | はい |
| <span id="af_siteid"></span>af\_siteid | リンク | いいえ | <ul><li>広告を表示するパブリッシャーを識別する一意のID。<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#site-id-parameter">詳細はこちら</Anchor></li></ul> | はい | はい |
| <span id="af_subsite_id"></span>af\_subsite\_id | リンク | いいえ | <ul><li>アドネットワークのサブネットワーク／パブリッシャーID。</li><li>メインパブリッシャー（サイトID）に加えてサブパブリッシャーがある場合、またはバナー、インタースティシャル、ビデオなど、アプリ内の広告タイプ／配置情報を含める場合は、af\_sub\_siteidを使用します。例: af\_sub\_siteid =ABCD\_4567</li></ul> | はい | はい |
| <span id="af_ad_type"></span>af\_ad\_type | リンク | いいえ | 以下の命名規則を利用してください：<ul><li>**テキスト：** テキストのみを含む広告ユニット(例：検索結果など）</li><li>**バナー：** 画面の上部または下部に表示される基本フォーマット</li><li>**インタースティシャル：** 画面閲覧中に差し込まれる、インターステシャル広告</li><li>**ビデオ：** リワード広告ではない通常の動画広告</li><li>**rewarded\_video:** 動画視聴と引き換えにアプリ内報酬を提供するリワード動画広告</li><li>**プレイアブル：** 実際のアプリ操作が一部可能な、インタラクティブな広告</li><li>**sponsored\_content:** 広告記事のようなスポンサードコンテンツに含まれるリンク</li><li>**オーディオ：** 音声広告</li></ul> | はい | はい |
| <span id="imei"></span>imei | SDK | はい | 携帯電話の識別に使用される端末固有の番号 | はい |  |
| <span id="is_organic"></span>is\_organic | AF | はい |  | インストールのみ |  |

<div id="in-app-event-only-macros" />

### アプリ内イベント専用マクロ

以下の例では、パートナーが利用可能なアプリ内イベントのポストバックについて紹介しています。

<div id="example" />

> 📄 **例**
>
> イベントポストバックのテンプレート"&event=(event)&json=(encode)"が、次の固有の af\_purchaseイベントのポストバックに変換されています。
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> このポストバックのデコードされたJSONの値は次のようになります。
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

<div id="encoded-values" />

#### **エンコードされる値**

ポストバックに、 英数字以外の特殊文字が含まれる場合があります。ポストバック時にこれらの値を正しく送信するために、AppsFlyerではポストバック内の英数字以外の値をURLエンコードします。

ポストバックをデコード、もしくはエンコードする場合には、<Anchor target="_blank" href="https://www.urldecoder.org/">各種エンコードのWebサービス</Anchor>を利用してください。

<div id="sample-postbacks" />

### ポストバックの例

<div id="general-install-postback-examples" />

### 一般的なインストールポストバックの例

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)
&advertising_id=(advertiser_id)&android_id=(android_id)
&install_time=(install_unix_ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?&site_id=(publisher_id)&
device_ip=(ip)&;idfa=(idfa)&install_time=(install_unix_ts)
```

</Tab>
</Tabs>

<div id="general-in-app-event-postback-examples" />

### 一般的なアプリ内イベントのポストバックの例

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)&
device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android_id)&
install_time=(install_unix_ts)&event_name=(event_name)&currency=(currency)&
json=(event_value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?clickid=(clickid)&site_id=(publisher_id)&
device_ip=(ip)&idfa=(idfa)&install_time=(install_unix_ts)
&event_name=(event_name)&currency=(currency)&json=(event_value)
```

</Tab>
</Tabs>

<div id="in-app-event-postback-example" />

### アプリ内イベントのポストバック例

イベントパラメータ：

* イベント名：af\_revenue
* イベント収益2024-02-26
* 。USD

ポストバック：

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-ad-networks=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%B8%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JHFZWJT74GNA6J5MYMQBGDWX=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%B8%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF postback-data-sources=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%82%BD%E3%83%BC%E3%82%B9 01JHFZWJT978TTXB7FQ6AVG1ZS=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%82%BD%E3%83%BC%E3%82%B9 postback-macros=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD 01JHFZWJTTP66NHZRG0RQAY3W8=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD macros%E2%80%94installs-inapp-events-and-rejected-events=%E3%83%9E%E3%82%AF%E3%83%AD%E5%90%8D%E4%B8%80%E8%A6%A7---%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB--%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88--%E3%83%96%E3%83%AD%E3%83%83%E3%82%AF%E3%81%95%E3%82%8C%E3%81%9F%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%90%91%E3%81%91 01JHFZWJTXD2K4RJ8RDWXKSYDD=%E3%83%9E%E3%82%AF%E3%83%AD%E5%90%8D%E4%B8%80%E8%A6%A7---%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB--%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88--%E3%83%96%E3%83%AD%E3%83%83%E3%82%AF%E3%81%95%E3%82%8C%E3%81%9F%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%90%91%E3%81%91 inapp-event-only-macros=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%B0%82%E7%94%A8%E3%83%9E%E3%82%AF%E3%83%AD 01JHFZWK3FQ5HCX9NDEKT6SPT1=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%B0%82%E7%94%A8%E3%83%9E%E3%82%AF%E3%83%AD 01JHFZWK3F2E31WE5N1G0T0ZHA=%E4%BE%8B encoded-values=%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89%E3%81%95%E3%82%8C%E3%82%8B%E5%80%A4 01JHFZWK3GM9XRS2GC4SNXFVD7=%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89%E3%81%95%E3%82%8C%E3%82%8B%E5%80%A4 sample-postbacks=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B 01JHFZWK3GJSA8RF4AMKVM4XD4=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B general-install-postback-examples=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B 01JHFZWK3HD1NFJJW1Y8HGVPX2=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B general-inapp-event-postback-examples=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B 01JHFZWK3JW0D1GZ739FV0EZWG=%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E4%BE%8B inapp-event-postback-example=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E4%BE%8B 01JHFZWK3JT8GM7BEM3RXCMXV5=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E4%BE%8B" />
