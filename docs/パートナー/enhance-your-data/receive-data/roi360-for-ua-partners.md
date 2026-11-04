---
title: UA パートナー向けの ROI360
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2023-08-12T17:09:08Z'
  edited_at: '2026-10-14T09:33:52Z'
  id: 17735150011921
  locale: ja
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ja/articles/17735150011921
---
> **概要：** 概要： AppsFlyerは、レポートとポストバックを通じて、完全で正確な広告、アプリ内購入、自動更新サブスクリプションデータをUAパートナーに提供します。パートナーは、UAキャンペーンを最適化するために情報を取り込むことができます。

<div id="introduction" />

## はじめに

AppsFlyerは、パートナーとアプリストア（Apple App StoreとGoogle Play Store）の両方から収益情報を受け取ります。受信後、データは検証、正規化、アトリビューション、追加のプロパティやディメンションによるエンリッチメントなどの一連のステップを受けます。  AppsFlyerはUA（ユーザー獲得）パートナーに情報を送信することができます。このプロセスに続いて、AppsFlyerはエンリッチメントおよびアトリビューションされたデータをUAパートナーに送信します。UAパートナーは、この情報を活用してユーザー獲得キャンペーンを最適化し、広告主へのサービスを強化できます。

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="パートナーに報告される収益タイプは何ですか?">

アプリは２つの収益タイプを作成します：

* **広告収益：広告収益： 広告収益は、バナー、インタースティシャル広告、その他のフォーマットを含む広告がアプリ内に表示されるたびに生成されます。これは、広告主が課金するキャンペーン方法に関係なく計算できます。**
* **アプリ内購入と自動更新サブスクリプション：** ストア収益は、アプリ内購入またはサブスクリプション関連のトランザクションが実行されるたびに生成されます。

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="AppsFlyerはUAパートナーに対して、どのように収益シグナルを提供していますか？">

AppsFlyerは、以下の方法でアプリ内広告、アプリ内購入、サブスクリプション収益に関する情報をパートナーに提供しています。

* **広告収益 UA シグナルレポート**：レポートには、デバイスレベルで集計された広告収益イベントが表示されます。レポートはデータロッカーで毎日利用可能で、前日のデータを含んでいます。
* 広告収益のポストバック広告収益のポストバック：クライアントのデバイスで広告インプレッションが発生するたびに、広告収益イベントの詳細を含むポストバックがAppsFlyerからパートナーへ送信されます。
* **ストア収益のポストバック**:ストア収益のポストバック：購入またはサブスクリプションイベントが発生するたびに、収益イベントの詳細を含むポストバックがAppsFlyerからパートナーに送信されます。

</Accordion>

<div id="set-up-roi360-for-partners" />

## パートナー向けにROI360を設定します

UAシグナルレポートと広告収益とストア収益のポストバックを受信するために、パートナーはどのようなアクションを取る必要がありますか？

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="ROI360 UA シグナルレポートを購読する方法">

データロッカー経由でパートナーがレポートを取得できるようにするには：

* パートナーは、データロッカーで次のステップを実行する必要があります：
  1. クラウドサービスプロバイダーへの接続、レポートのフォーマットや内容など、パートナーアカウントの<Anchor target="_blank" href="/partners/ja/docs/data-locker-for-partners#set-up-data-locker">データロッカーを設定</Anchor>します。
  2. <Anchor target="_blank" href="/partners/ja/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">ROI360のUAシグナルレポートを有効にします</Anchor>。
* 広告主は、<Anchor target="_blank" href="/marketers/ja/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">レポートに対する権限をパートナーに付与する</Anchor>必要があります。

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="AppsFlyerからROI360ポストバックを受け取る方法">

AppsFlyerからポストバックを受信するには、パートナーはAppsFlyerのパートナー連携チームとの会話を開始する必要があります。その後、チームはAppsFlyerのプラットフォーム内で、ROIアプリ内収益のポストバック値を設定します。

AppsFlyerのパートナーサポートにお問い合わせするには、管理画面の**ヘルプ**メニューを開いて「**チームにお問い合わせ**」を選択してください。

alt

</Accordion>

<div id="roi360-ua-signals-report-for-ua-networks" />

## UAネットワーク向けのROI360 UAシグナルレポート

このレポートは、完全で正確な X＋１日目の CSV/parquet 収益レコードをUAパートナーの S3 バケットに毎日提供します。各レコードは、デバイスレベルでの広告収益イベントの集計です。

UAシグナルレポートは、広告収益のポストバックのようにリアルタイムデータを提供しません。ただし、より正確で完全です。これは、インプレッションの値が時間経過とともに変化する可能性があるためです。これは、インプレッションレベルの収益データが、リアルタイム入札ではなく標準的なCPM入札で販売された広告インプレッションに関するものである場合に、特に当てはまります。

<div id="what-are-the-report-data-sources" />

<Accordion title="レポートのデータソースとは何か？">

広告主の連携タイプに応じて、レポートデータは次のいずれかから取得されます：

1. <Anchor target="_blank" href="/marketers/ja/docs/integrate-the-roi360-ad-revenue-sdk-api">広告収益 SDK コネクター</Anchor>の連携：顧客は、パートナーがロードしたインプレッションレベルの収益データをクライアントデバイスと共有可能で、ほぼリアルタイムでAppsFlyerにレポートされます。
2. S2S APIベースのデバイスレベルの連携：顧客は、AppsFlyerのUI内の連携パートナーのもとでパートナーの認証情報を設定することができ、それによりROI360の広告収益が代わりにデバイスレベルの広告収益データを収集できるようになります。
3. ２つの組み合わせ（鮮度と精度）。**注記：** 注記：広告主からAppsFlyerへのデータの転送は、広告主の権限と、広告主がROI360のアドバンスパッケージ顧客であるかどうかに左右されます。

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="レポートデータに対してどのようなデータ処理が行われますか？">

AppsFlyer ROI360 Ad Revenueは以下を実行します。

1. データの正規化
2. インストールメディアソースとデータエンリッチメントへのアトリビューション
3. 広告収益イベントの生成
4. イベントはデバイスレベルで集計されます。

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="レポートデータはどのように配信されますか？">

デバイスレベルのデータはデータロッカー内のレポートに毎日書き込まれます。

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="レポートデータの鮮度はどのくらいですか？">

データは、毎日21:00 <Anchor target="_blank" href="/marketers/ja/docs/about-data-freshness-and-timezone-support#daily">UTC時刻</Anchor>にデータロッカーバケットの h=23 フォルダーに書き込まれます。

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="レポートのフィールドとは何か？">

| **フィールド** | **備考** |
| --- | --- |
| バージョン | 秒単位のUnixタイムスタンプ。例： 1661315124 |
| app\_id | AppsFlyerプラットフォームのアプリID |
| install\_time | • インストールのタイムスタンプ：YYYY-MM-DD HH:MM:SS例：iOS 14+および同意していないユーザーの場合、または広告主が高プライバシーをオンにしている場合、インストール時間は時間単位で端数処理されます。 |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | UAがデータを受信するパートナーに帰属する場合にのみ設定されます。 |
| idfa, idfy, advertising\_id | 広告収益化イベントが複数ある場合、IDFA、IDFV、advertiser\_idなどの同じデバイス ID が複数の行に表示される可能性があります。iOS 14+および同意のないユーザーの場合、または広告主が高プライバシーをオンにしている場合、これは表示されません。 |
| platform | デバイスプラットフォーム：iOS、Android、またはWindows Mobile |
| country | [ISO 3166 (alpha-2)](https://www.iso.org/iso-3166-country-codes.html)を使用した国コード：US, CN などUS、CN |
| original\_url | iOS 14+および同意のないユーザーの場合、または広告主が高プライバシーをオンにしている場合、これは表示されません。UAがデータを受信するパートナーに帰属する場合にのみ設定されます。 |
| mediation\_network | 2023年第３四半期の予定：インプレッションに関連付けられたメディエーションネットワーク<Anchor target="_blank" href="/marketers/ja/docs/roi360-guide-ad-revenue-attribution#[closed-beta]-ua-signals-for-ad-networks">可能なネットワークのリストを参照してください。</Anchor> |
| ad\_unit | 2023年第3四半期予定：2023年第３四半期の予定：インプレッションに関連付けられたマネタイズ広告ユニット |
| 配置 | 2023年第3四半期予定：2023年第３四半期の予定：インプレッションに関連付けられたマネタイズプレースメント |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="レポートデータのサンプルをダウンロードします。">

[クリックしてレポートをダウンロードします。](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

<div id="in-app-ad-revenue-iaa-postbacks" />

## アプリ内広告収益（IAA）のポストバック

IAAポストバックは、AppsFlyerが収益情報をパートナーに送信するために使用する２番目の取り込みアプローチです。広告収益のUAシグナルレポートに対する主な利点は、ポストバックがほぼリアルタイムのIAA収益データ共有を提供するので、その鮮度です。これは、広告収益のUAシグナルレポートで提供される X＋１ の鮮度（イベント発生日の１日後）とは対照的です。

ただし、リアルタイムの鮮度は X＋１と比べて精度が低くなります：

* リアルタイムのIAAポストバックデータは、UAシグナルレポートの X＋１のデータよりも、平均して±５％精度が低くなります。
* リアルタイムのIAAポストバックデータは、UAシグナルレポートの X＋１のデータよりも、平均して±７％完全ではありません。

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="IAAポストバックのデータソースとは何か？">

IAAポストバックのデータは、パートナーがクライアントデバイスにロードするインプレッションレベルのデータから生成されます。このデータは、ROI360広告収益SDKを介してAppsFlyerと共有され、広告主によってデバイスにインストールされます。コネクターにより、アプリ開発者は ILRD、通貨、メディエーションプラットフォーム、マネタイズソースなどの特定のパラメーターを含むインプレッションイベントを報告することができます。

広告主のクライアントデバイスからAppsFlyerへのデータの転送は、広告主の権限と、広告主がROI360のアドバンスパッケージ顧客であるかどうかに左右されます。

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="IAAポストバックデータに対してどのような処理が行われますか？">

AppsFlyer ROI360は、受信したインプレッションレベルのデータごとに以下のステップを実行します：

1. データの正規化。
2. インストールメディアソースとデータエンリッチメントへのアトリビューション。
3. **af\_ad\_revenue** イベントの生成。

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="ポストバックデータはどのように配信されますか？">

イベントは、パートナーとAppsFlyer間の既存のポストバック設定を介して、追加のパラメーターとしてパートナーに送信されます。

</Accordion>

<div id="in-app-purchase-iap-postbacks" />

## アプリ内購入（IAP）のポストバック

ROI360のアプリ内購入のポストバックは、最初に各トランザクションを検証し、重複排除してから、店舗手数料と消費税を差し引くことにより、何重ものレポート精度を提供します。

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="IAPポストバックのデータソースとは何か？">

IAPポストバックのデータは以下から取得されます：

1. デバイスでアプリ内購入または自動更新サブスクリプションイベントが発生するたびに、ROI360 購入SDKコネクターによって読み取られるトランザクションレベルのデータ。
2. **App Store および Google Play (RTDN) サーバーからの全ての受信通知**も、AppsFlyerの購入およびサブスクリプション収益のビジネスロジックによって処理されます：

   * SDKコネクターを介して以前にレポートされたトランザクションに関する通知は、検証および処理されます。
   * 不明なトランザクションに関する通知は、AppsFlyerに報告されません。

   **注記：** 注記：広告主からAppsFlyerへのデータの転送は、広告主の権限と、広告主がROI360のアドバンスパッケージ顧客であるかどうかに左右されます。

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="IAPポストバックデータに対して、どのようなデータ処理が行われますか？">

AppsFlyer ROI360は、受信したトランザクションレベルのデータごとに以下のステップを実行します：

1. AppsFlyerは、不正ではないことを確認するために、**各ストアで購入またはサブスクリプションデータを検証します**。
   * 検証が成功すると、AppsFlyerは購入またはサブスクリプションをログに記録します。
   * レシート検証が失敗した場合、そのイベントは「ブロック済アプリ内イベント」ローデータレポート内に表示されます（Protect360を契約している場合に利用可能）。
2. AppsFlyerは、iOSのファミリー共有に関連するものも含め、トランザクションが重複しないようにします。
3. AppsFlyerは、店舗手数料と税金 （**真の収益**）を考慮して純収益データを計算します。
4. AppsFlyerは、検証および処理されたトランザクションの内部購入またはライフサイクルイベントを生成します。

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="ポストバックはどのように配信されますか？">

IAPイベントは、パートナーとAppsFlyer間の既存のポストバック連携を通じて、パートナーに送信されます。

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="IAPイベントとは何か？">

ROI360の顧客は以下の収益を伴うイベント名を共有できます。

**複数のイベント名**

| **Event name** | **説明** |
| --- | --- |
| af\_purchase | ユーザーが購入したときに記録されます。 |
| af\_purchase\_refund | 購入が払い戻し（返金）されたときに記録されます。 |
| af\_ars\_trial\_converted | トライアル期間後、正規価格の更新が開始されたときに記録されます。 |
| af\_ars\_subscription\_started | 割引または正規価格のサブスクリプションが開始されたときに記録されます。 |
| af\_ars\_subscription\_resumed | 解約または払い戻し（返金）されたサブスクリプションの後に、正規価格のサブスクリプションが再開されたときに記録されます。 |
| af\_ars\_subscription\_refunded | 加入者が払い戻し（返金）を受けたときに記録されます。 |
| af\_ars\_subscription\_renewed | 自動更新サブスクリプションが行われたときに記録されます。 |
| af\_ars\_subscription\_xgraded | 加入者が別のサービスにアップグレード、ダウングレード、またはクロスグレードしたときに記録されます。 |

</Accordion>

<div data-zendesk-anchors="introduction=%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB 01H7T1DS6SNC7X8GX4DGXT4GC0=%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91%E3%81%ABroi360%E3%82%92%E8%A8%AD%E5%AE%9A%E3%81%97%E3%81%BE%E3%81%99 01H7T1DS6TDA8CX1ZF3GGE4EHB=%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91%E3%81%ABroi360%E3%82%92%E8%A8%AD%E5%AE%9A%E3%81%97%E3%81%BE%E3%81%99 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=ua%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91%E3%81%AEroi360-ua%E3%82%B7%E3%82%B0%E3%83%8A%E3%83%AB%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 01H7T1DS6T93844DMZY744ECQE=ua%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91%E3%81%AEroi360-ua%E3%82%B7%E3%82%B0%E3%83%8A%E3%83%AB%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E5%BA%83%E5%91%8A%E5%8F%8E%E7%9B%8Aiaa%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01H7T1DS6T0CN30EC97VARN80D=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E5%BA%83%E5%91%8A%E5%8F%8E%E7%9B%8Aiaa%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E8%B3%BC%E5%85%A5iap%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01H7T1DS6TH8AV2ZTY3M8ZXPYA=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E8%B3%BC%E5%85%A5iap%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
