---
title: 広告収益のシグナルデータ：UAアドネットワーク向け
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-michael-talapov
    - ROI360
    - Ad Networks
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2026-10-14T09:28:18Z'
  id: 4402898251409
  locale: ja
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ja/articles/4402898251409
---
> **概要： 概要： ユーザー獲得を担当するアドネットワークへ広告収益データをポストバック送信し、そのデータを使用してキャンペーンを最適化することができます。**

アドネットワークは、ユーザーに関する貴重な広告収益情報のレポートをData Locker経由で受信できます。ユーザーは、これらを通じて提供されるキャンペーンから獲得されたユーザーか、別のメディアソースから取得されたユーザーである可能性があります。

アドネットワークは、このデータをキャンペーンターゲティングおよび最適化アルゴリズムに取り込み、それを使用して、生み出した収益の全体像に基づいてROASキャンペーンを改善できます。

<div id="set-the-ad-revenue-report-in-data-locker" />

## Data Lockerで広告収益レポートを設定

Data Lockerで広告収益レポートにアクセスするには、以下を完了する必要があります。

* アドネットワークは、 <Anchor target="_blank" href="/partners/ja/docs/data-locker-for-partners#set-up-data-locker">パートナー向けData Lockerにオンボード</Anchor>する必要があります。
* アドネットワークは、レポート [出力設定を行い](#configure-the-report-output-settings)、[広告収益レポートを有効にする](#enable-the-ad-revenue-report)必要があります。
* 広告主は、アドネットワークによるレポートの閲覧権限を付与する必要があります。<Anchor target="_blank" href="/marketers/ja/docs/share-ad-revenue-data-with-partners#ua-signals-for-ad-networks">広告主向けの手順を確認</Anchor>

<div id="configure-the-report-output-settings" />

<Accordion title="レポート出力設定の構成">

レポート出力設定を構成するには、次の手順に従ってください：

1. AppsFlyer管理画面 左メニュー **レポート** > **Data Locker**へ移動します。
2. **レポート出力設定**の項目で、**レポートの送信**をオンにします。
3. レポートファイルの出力プロパティを設定します。
   * レポートのフォーマット (Parqet/CSV)。
   * レポートの圧縮方法 (Snappy/GZIPO/非圧縮)。
   * ファイル内の最大行数。
4. レポートファイル出力の予想されるパスを確認します。パスは、接続設定に従って設定されます。接続の設定方法は、<Anchor target="_blank" href="/partners/ja/docs/data-locker-for-partners#set-up-data-locker">Data Lockerの設定</Anchor>を参照してください。

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="広告収益レポートを有効にします。">

1. **Data Lockerコンテンツ**の項目で、**広告収益 (日別)** のレポートタイプを選択します。
2. **接続を保存**をクリックします。
3. 広告主がアドネットワークにレポートの表示を許可していることを確認します。
4. 手順については、[<Anchor target="_blank" href="/marketers/ja/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">アドネットワークによる広告収益データの取得を許可する</Anchor>]をご覧ください。

</Accordion>

<div id="report-specification" />

## レポートの仕様

<div id="report-considerations" />

<Accordion title="レポートの構造と形式">

* 形式：形式: データはCSV形式でUAパートナーのS3バケットに到着します。
* レベルレベル: デバイスレベルのディメンションと指標が含まれます。
* データ拡充：データエンリッチメント: メディエーションパートナーからの広告収益データが含まれ、UAアドネットワークに関連するアトリビューションデータが追加されます(UAアドネットワークに関係のないすべてのディメンションは消去されます)。
* データ更新頻度：
* 含まれるアプリ： 1つのレポートには、広告主が許可を与えたすべてのアプリのデータが含まれます。
* 通貨:通貨： USD。イベント収益は、イベントが発生した日のUSDで計算されます。
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv">サンプルレポートをご覧ください。</Anchor>

</Accordion>

<div id="report-structure" />

<Accordion title="レポート項目">

| **フィールド** | **備考** |
| --- | --- |
| バージョン | 秒単位のUnixタイムスタンプ。例：1661315124 |
| app\_id | AppsFlyerプラットフォームのアプリID |
| install\_time | <ul><li>YYYY-MM-DD HH:MM:SS<br />例：2020-08-16 11:22:33</li><li>iOS 14+および同意していないユーザーの場合、または広告主が高プライバシーをオンにしている場合、インストール時間は時間単位で端数処理されます。</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | UAがデータを受信するパートナーに帰属する場合にのみ設定されます。 |
| idfa, idfy, advertising\_id | <ul><li>広告収益化イベントが複数ある場合、IDFA、IDFV、advertiser\_idなどの同じデバイス ID が複数の行に表示される可能性があります。</li><li>iOS 14+および同意のないユーザーの場合、または広告主が高プライバシーをオンにしている場合、これは表示されません。</li></ul> |
| platform | デバイスプラットフォーム：iOS、Android、またはWindows Mobile |
| country | <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor>を使用した国コード：US, CN などUS、CN |
| original\_url | <ul><li>iOS 14+および同意のないユーザーの場合、または広告主が高プライバシーをオンにしている場合、これは表示されません。</li><li>UAがデータを受信するパートナーに帰属する場合にのみ設定されます。</li></ul> |
| ad\_unit |  |
| 配置 |  |
| mediation\_network |  |
| engagement\_type |  |

指標：

| **フィールド** | **備考** |
| --- | --- |
| Impressions | ユーザーが広告を見た回数 |
| revenue\_usd | デバイスIDに対して生成された日次収益（USD）。　**注：** 例：8.00E-05 |

</Accordion>

<div data-zendesk-anchors="set-the-ad-revenue-report-in-data-locker=data-locker%E3%81%A7%E5%BA%83%E5%91%8A%E5%8F%8E%E7%9B%8A%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E8%A8%AD%E5%AE%9A h_01H8Y7ABGVR7BNHEYVFKPFM4JN=data-locker%E3%81%A7%E5%BA%83%E5%91%8A%E5%8F%8E%E7%9B%8A%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E8%A8%AD%E5%AE%9A h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report report-specification=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AE%E4%BB%95%E6%A7%98 h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AE%E4%BB%95%E6%A7%98 h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
