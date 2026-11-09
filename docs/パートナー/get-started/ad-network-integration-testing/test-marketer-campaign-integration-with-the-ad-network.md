---
title: マーケターのキャンペーンを使ったアドネットワークとの連携テスト
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
  created_at: '2021-12-08T04:41:04Z'
  edited_at: '2026-10-14T09:38:38Z'
  id: 4413093220113
  locale: ja
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ja/articles/4413093220113
---
> **概要**：

<div id="prerequisites" />

## 前提条件

マーケターによるあなたのアドネットワークとの連携をテストする前に、いくつかの前提条件を確認してください。

* テスト端末のホワイトリスト登録 - テストに使用する<Anchor target="_blank" href="/marketers/ja/docs/registering-test-devices">端末のホワイトリスト登録</Anchor>をマーケターに依頼してください。
* アプリにはAppsFlyer SDKが含まれている必要があります
* アプリが Google Play または iOS App Store で公開されていない場合は、マーケターにアプリの提供を依頼する必要があります
* アプリが公開されているかどうかにかかわらず、<Anchor target="_blank" href="/marketers/ja/docs/adding-an-app-to-appsflyer">マーケターのAppsFlyerアカウントにある</Anchor>必要があります

<div id="getting-started" />

## はじめよう

AppsFlyerダッシュボードを開いてください。**アプリ検索**画面で、マーケターのアプリ IDを入力します。

<div id="example" />

> 📄 **例**
>
> Android - **com.example.app**
>
> iOS- **id1234123412**

入力フィールドに緑色のチェックマークが表示されたら、青い矢印をクリックしてください。矢印をクリックすることで、アプリの管理画面が開きます。

<Image align="center" alt="partner-app-search.png" src="https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png" />

<div id="testing-live-apps" />

## リリース済みアプリのテスト

アプリのAppsFlyer管理画面にて、サイドメニューから**アクティブな連携**を選択します。あなたのアドネットワークを選択して**計測リンク**をクリックしてください。

<div id="important" />

> 🚧 **重要！**
>
> 下のオプションがグレー表示されている場合は、マーケターに<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">広告ネットワークの権限を有効にする</Anchor>よう依頼してください。必要な権限は、**パートナー連携の設定を許可する** と **アプリ内イベントのポストバック設定を許可する**です。
>
> または、マーケターに計測リンクの提供を依頼することもできます。

<div id="installing-the-app-through-the-attribution-link" />

<Accordion title="計測リンク経由でのアプリインストール">

インストール計測をテストするための計測リンクをまずは作成しましょう。

あなたのアドネットークの要件と計測したいデータに沿う形で、計測リンクにパラメータを追加してください。

<Image align="center" alt="partner-configure-attribution-link.png" src="https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png" />

<div id="tip" />

> 👍 **ヒント**
>
> 計測リンクに追加可能なパラメータの詳細については、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">AppsFlyerの計測リンクの構造とパラメータ</Anchor>のページを参照してください。

</Accordion>

<div id="testing-install-attribution" />

<Accordion title="インストールアトリビューションのテスト">

テスト端末に計測リンクを送信し、

その後、 [ダッシュボードでインストールを表示できます](/docs/test-marketer-campaign-integration-with-the-ad-network#管理画面でのインストールの確認)。

</Accordion>

<div id="testing-apps-in-development" />

## 開発中アプリのテスト

マーケターのキャンペーンと広告ネットワークの統合は、アプリが公開されていない場合でもテストできます。ただし、媒体側のテスト端末でインストールテストが行えるよう、事前に広告主に対してテストアプリ(apkもしくはipaファイル)を提供するよう依頼する必要があります。

<div id="generate-an-attribution-link" />

<Accordion title="計測リンクの作成">

次に計測リンクを作成してください。手順は、[上記の手順と同様のものを使用可能です。](/docs/test-marketer-campaign-integration-with-the-ad-network#installing-the-app-through-the-attribution-link)計測リンクをテスト端末へ送信して、テスト端末のブラウザを使ってリンクを開いてください。

次の画面が表示されます。

<Image align="center" alt="app-not-available.png" src="https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png" />

この画面表示が理想の挙動の結果です。アプリはまだリリースされていないため、計測リンクはどのアプリストアにも遷移しません。

</Accordion>

<div id="installing-the-app" />

<Accordion title="アプリのインストール">

マーケターから提供されたアプリデータをテスト端末上でインストールして、アプリを起動してください。次にアプリを一度削除して、(複数件インストールを発生させるために)同じプロセスを繰り返してください。そうすることで、[管理画面上でインストールが確認できる](/docs/test-marketer-campaign-integration-with-the-ad-network#管理画面でのインストールの確認)ようになります。

</Accordion>

<div id="testing-in-app-events" />

## アプリ内イベントのテスト

<div id="note-1" />

<div id="note" />

> 📘 **注意**
>
> アプリ内イベントのポストバックのテストは、リリース済み、開発中、どちらのアプリでもテスト可能です。

アプリ内イベントのポストバックをテストする前にマーケターに連絡して、計測するアプリ内イベントの種類と、どのようにそのアプリ内イベントを発火するのかを確認してください。

<div id="mapping-events" />

<Accordion title="アプリ内イベントのマッピング">

マーケターがアドネットワークの連携設定で <Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">**アプリ内イベントのポストバック設定**</Anchor> 権限を有効にしている場合、AppsFlyerのイベントをサーバーにログインしたイベントにマッピングできます。

アプリのAppsFlyer管理画面で、サイドメニューから **アクティブな連携**を選択し、アドネットワークを選択します。**連携**タブで**アプリ内イベントポストバック**の箇所までスクロールしてください。アプリ内イベントを選択して、必要な場合には対となるイベントにマッピングしてください：

<Image align="center" alt="partner-in-app-events-postbacks-mapping.png" src="https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png" />

</Accordion>

<div id="triggering-inapp-events" />

<Accordion title="アプリ内イベントの発火">

マーケターがどのアプリ内イベントを計測し、イベントマッピングを設定したら、インストール済みのアプリからいくつかのイベントをトリガーします。

アプリ内イベントのポストバックレポートでは、Postback URLやマッピングされたパラメータのデータを確認することができます。ポストバックレポート内のデータとサーバー内のデータと比較し、ポストバックされたデータが正しくサーバー側で記録されていることを確認してください。

アプリ内イベントのポストバックレポートを取得すると、レポートを確認することで以下のことが確認できます。

1. **Media Source**の列で、あなたのアドネットワークにイベントが紐付けられていること
2. **Event Name**の列で、イベント名が正しいこと
3. ポストバックが有効な場合には、**Postback URL**の列でイベント名とイベントの値が含まれていること
4. **Postback URL**の列で、アプリ内イベントが正しくマッピングされていること

</Accordion>

<div id="viewing-installs-in-the-dashboard" />

## 管理画面でのインストールの確認

アプリをダウンロードして初回起動すると、管理画面にその結果が表示されます。

<div id="important-1" />

> 🚧 **重要！**
>
> 一つの端末で複数回のインストールを発生させるためには、[予め端末をホワイトリスト登録する必要があります](/docs/test-marketer-campaign-integration-with-the-ad-network#前提条件)。

AppsFlyer管理画面にアクセスし、サイドメニューから**分析**>**概要**を選択します。

クリックとインストールに関するデータは、**オーバービュー**の画面の上部に表示されます。

<div id="verifying-postback-data" />

## ポストバックデータの検証

あなたのアドネットワークにインストールが紐付けられる毎に、インストールポストバックが発生します。アプリ内イベントのポストバックが有効になっている場合には、インストールがあなたのアドネットワークに紐付いているアプリから発生したイベントのポストバックも発生します。

<Anchor target="_blank" href="/marketers/ja/docs/raw-data-export-page">ローデータのエクスポートページ</Anchor>を開き、2つのポストバックレポートを生成します。

1. **インストール**
2. **In-app events**

どちらのレポートにも、 **Postback URL**というカラム名の列があります。この列には、インストールまたはアプリ内イベントの実際のポストバックURLが記載されます。

このデータを見て、以下のことを確認してください。

* URLのエンドポイントが正しいものであること
* Postback URLに追加されたパラメータが、AppsFlyerの計測URLに追加されているパラメータと対応していること
* `sdk_event=af_purchase&mapped-event=purchase`  
  `sdk_event=af_login&mapped-event=login`
* **Postback Error Message**の列が空欄であること

<div data-zendesk-anchors="prerequisites=%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6 h_01HKA1DE8VKXM92D7S5BANFZJ4=%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6 getting-started=%E3%81%AF%E3%81%98%E3%82%81%E3%82%88%E3%81%86 h_01HKA1DE8V9A9AJWYQR9VJQ0H8=%E3%81%AF%E3%81%98%E3%82%81%E3%82%88%E3%81%86 h_01HKA1DE8VA7HAM8BT3KZ8HYGP=%E4%BE%8B testing-live-apps=%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E6%B8%88%E3%81%BF%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 h_01HKA1DE8V0J2Y8DQ60J9S5DAK=%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E6%B8%88%E3%81%BF%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 h_01HKA1DE8VDQGKYSYFDF5K2HSX=%E9%87%8D%E8%A6%81 h_01HKA1DE8VEEH8YE1QT28QVFZQ=installing-the-app-through-the-attribution-link h_01HKA1DE8VV0K8J2AG7W0FDDWY=%E3%83%92%E3%83%B3%E3%83%88 h_01HKA1DE8VEH7S0JAJTJ91KE7X=testing-install-attribution testing-apps-in-development=%E9%96%8B%E7%99%BA%E4%B8%AD%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 h_01HKA1DE8VK9RQGQ8BCG157H1Y=%E9%96%8B%E7%99%BA%E4%B8%AD%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 h_01HKA1DE8VSPE0FFM65AFQRJ8S=generate-an-attribution-link h_01HKA1DE8V68Z5CM4EF7YBPHPS=installing-the-app testing-inapp-events=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 h_01HKA1DE8VVJXK11BM77D3YWA5=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88 h_01HKA1DE8W2VT648E022BHJP0K=%E6%B3%A8%E6%84%8F h_01HKA1DE8WQVGPSTG2SQCM2BQW=mapping-events h_01HKA1DE8WRZPCX3GGV01ZK10K=triggering-inapp-events h_01HKA1DE8W8XXM4BK7843TAEJQ=%E6%B3%A8%E6%84%8F viewing-installs-in-the-dashboard=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%A7%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%AE%E7%A2%BA%E8%AA%8D h_01HKA1DE8WY7VCST4XDN1HWGC7=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%A7%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%AE%E7%A2%BA%E8%AA%8D h_01HKA1DE8WYRTTNC2Q0VGKMM82=%E9%87%8D%E8%A6%81-1 verifying-postback-data=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E6%A4%9C%E8%A8%BC h_01HKA1DE8WEQY58XAPS9MBNGKE=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E6%A4%9C%E8%A8%BC" />
