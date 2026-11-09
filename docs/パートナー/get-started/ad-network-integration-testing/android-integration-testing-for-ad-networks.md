---
title: Android連携テスト：アドネットワーク向け
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
  created_at: '2021-12-06T10:35:58Z'
  edited_at: '2026-10-14T09:33:34Z'
  id: 4412945443857
  locale: ja
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ja/articles/4412945443857
---
> **概要：** 概要：AppsFlyerとのAndroidのポストバック連携を、専用のアプリを使ってテストすることが可能です。

<div id="android-integration-testing" />

## Androidの連携テスト

テストは以下の要素で構成されています。

* iOS版のAppsFlyerのパートナー連携アプリを使用して、まずはテストインストールを発火させ、続いてアプリ内で購入イベントを実施してください。これらのテストによって、あなたのアドネットワークのエンドポイントへポストバックが送信されます。また、ログインと会員登録完了のイベントをテストすることも可能です。
* ポストバックを受信したら、それらをシステムへ取り込むことができるかを確認してください。

**テストの範囲**

以下の表で、利用可能な設定の組み合わせに応じた、テストシナリオを示しています。

各シナリオ毎に、インストールとアプリ内イベントのテストが可能です。アプリ内イベントに関しては、<Anchor target="_blank" href="/partners/ja/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">アプリ内イベントをマッピング</Anchor>して、広告主イベントをパートナー側のイベントにマッピングすることが可能です。

<div id="testing" />

## テスト

前提条件の準備を全て完了してから、以降のセクションに記載されているテスト手順に従ってください。各テストセクションには、テスト結果を記録するのを助ける表が記載されています。

<div id="prerequisites" />

<Accordion title="前提条件">

テストを開始する前に、前提条件の準備を全て完了してください。

| 前提条件 |
| --- |
| <Anchor target="_blank" href="/partners/ja/docs/turn-on-test-app-integration-for-ad-networks">Androidのテストアプリのパートナーアカウントへの追加（AppsFlyer側の作業）</Anchor> |
| テストアプリがあなたのパートナーアカウント内に表示されていることを確認。 |
| <Anchor target="_blank" href="/partners/ja/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">アプリ内イベントのマッピング</Anchor> |
| <Anchor target="_blank" href="/partners/ja/docs/ios-integration-testing-for-ad-networks#attribution-link">計測リンクの準備</Anchor> |
| Android端末を使ったインストール計測のテスト |
| Android端末を使ったアプリ内イベントのテスト |
| Android端末を使ったリターゲティング計測のテスト |

</Accordion>

<div id="test-install-attribution" />

<Accordion title="インストール計測のテスト">

**ポストバックを発火させるには：**

1. 準備したテスト端末に計測リンクを送信してください。
2. リンクをクリックして、アプリをインストールして起動してください。  
   その後、以下のような**インストールデータ**のページが表示されます。
3. 以下のパラメータを使用して、アトリビューション内容を検証してください。検証がうまく行かない場合には、<Anchor target="_blank" href="/partners/ja/docs/ios-integration-testing-for-ad-networks#troubleshooting">トラブルシューティング</Anchor>を確認してください。

   1. タイムゾーンはUTCで記録されます。
4. **In-App Event Tests**をタップしてください。
5. **Purchase Event**をタップしてください。  
   そうすると、購入イベントの確認が表示されます。
6. 最後に以下を確認してください。
   1. インストールと購入イベントのポストバックを受け取ったこと。
   2. イベント名が正しくマッピングされていること。(イベント名をマッピングした場合)
   3. 受け取ったポストバックを正しく取り込めたこと。

</Accordion>

<div id="supplementary-information-and-procedures" />

## 補足情報および手順詳細について

<div id="about-the-partner-integrations-test-app" />

<Accordion title="パートナー連携テストアプリについて">

アプリを初めて開くと、［**インストールデータ**］のページにAppsFlyer上に記録されたコンバージョンデータが表示されます。また、アプリ内イベントのテストもアプリの画面内で発火可能です。

以下のような機能が利用可能です：

* **In-App Event Tests**をタップしてください。  
  各アプリ内イベントをアドネットワーク側のイベント名にマッピングすることで、そのイベント名を使用したポストバックを生成することも可能です。

</Accordion>

<div id="attribution-link" />

<Accordion title="計測リンク">

以下のいずれかの方法を使って、AppsFlyerの管理画面上で計測リンクを作成してください。

* AppsFlyerの管理画面上で計測リンクを作成する。
* 以下のサンプルリンクを編集する。

**管理画面上で計測リンクを作成するには：**

1. AppsFlyerにて、トップメニューから **マイアプリ**を選択します。
2. **adNetworkTest**のアプリを選択してください。
4. 計測リンクタブ内で、以下に記載されているパラメータを設定してください。必要であれば、任意のパラメータをさらに追加することも可能です。 

| パラメータ | 値の例 | 備考 |
| --- | --- | --- |
| <span id="campaign"></span>Campaign | c-test-2020-12-20 | ポストバック内でテストのデータであることを識別可能な値を設定してください。 |
| <span id="pid"></span>pid | pitestap |  |

5. 後で使用するので、作成した計測リンクをコピーしてください。

**計測リンクのサンプル：**

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="パートナーアカウントへのテストアプリの紐付け">

**あなたのパートナーアカウントで、テストアプリが利用可能かどうかの確認方法：**

1. AppsFlyerのトップメニューから **マイアプリ**へ進んでください。
2. もし見当たらない場合には、担当PDMまでご連絡ください。

</Accordion>

<div id="troubleshooting" />

<Accordion title="トラブルシューティング">

| 症状 | 原因と対策 |
| --- | --- |
| インストール時刻が現在の時刻ではない。 | ←アプリがテストインストール前に削除されていなかった可能性が高いです。<br /><br />一度アプリを削除して、テスト手順を繰り返してください。 |
| 計測されたメディアソースがあなたのメディアソース名ではなかった。 | 計測リンクに正しい**pid**の値が設定されているかどうか確認してください。また、正しい計測リンクを使用しているかどうかも確認してください。 |
| af\_statusがOrganicで計測される。 | 計測リンクの形式、特に**pid**の値を確認してみてください。 |

</Accordion>

<div id="test-retargeting-attribution" />

<Accordion title="リターゲティング計測のテスト">

リターゲティング計測のテストも可能です。計測リンクにパラメータを一つ追加する以外のプロセスはほぼ同じです。

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_click_lookback=7d
          &clickid={clickid}&is_retargeting=true
```

このリターゲティング用のURLを使用して、アプリをインストールしてください。フローは、[インストール計測のテスト](/docs/android-integration-testing-for-ad-networks#test-install-attribution)で説明したものと同様です。

<div id="viewing-retargeted-installs-in-the-dashboard" />

### 管理画面でのリターゲティングコンバージョンの確認

AppsFlyerの管理画面を開いて、左メニューにある**リターゲティング**をクリックしてください。リターゲティングされたインストールが管理画面に表示されるまで、最大30分程度お待ちください。

<Image align="center" alt="com_appsflyer_adNetworkTest-retargeting.png" src="https://files.readme.io/e46789b004be2f4fc15f095ba11a0f3f5d03abb1240e54e4b534285e3e4efd8d-21266228899601.png" />

</Accordion>

<div id="test-viewthrough-attribution" />

<Accordion title="ビュースルー計測のテスト">

1. AppsFlyerの管理画面で、**My Apps**のタブに移動してください。
2. **adNetworkTest**のアプリを選択してください。
4. **ビュースルーアトリビューション**がONになっていることを確認してください。
5. インプレッションの計測リンクをコピーしてください。

   ```http
   https://impression.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_viewthrough_lookback=24h&advertising_id=YOUR_GAID&af_siteid=YOUR_SITEID
   ```

   パラメータに渡す値を以下のように置き換えてください。

   * {"pid(YOUR_PID)"} - AppsFlyerから指定された、あなたのpidを入力してください。(末尾は*{"_int"}*です）
   * c (YOUR\_CAMPAIGN) - 任意のキャンペーン名を入力してください。
   * advertising\_id（YOUR\_GAID）- テスト端末のGAIDを入力してください。
   * af\_siteid（YOUR\_SITEID）- 任意のサイトIDを入力してください。

   注意：リンク内のパラメータは、テストの目的で使用されている基本的なパラメータです。必要に応じて、計測リンクには他のパラメータも追加することが可能です。
6. テスト端末にビュースルーの計測リンクを送信してください。
7. ブラウザ上でリンクを開いて、アプリをストアからインストールしてください。
8. アプリを起動します。  
   以下の画面が表示されます。

   <Image align="center" alt="vta-testing-postback.png" src="https://files.readme.io/88b6720928d7540eeb2fe8f42f39ecdccc04655aa49f95d08dba5741d5e39982-4831106525457.png" />

ヒント

<div id="view-installs-in-the-dashboard" />

### 管理画面上でのインストールの確認

アプリをダウンロードして初回起動すると、AppsFlyerの管理画面にその結果が表示されます。

インストールがアプリの管理画面に表示されるまで最大30分ほどかかることがあります。

</Accordion>

<div id="raw-data-export" />

<Accordion title="ローデータ出力">

あなたのアドネットワークにインストールが紐付いているアプリに関するデータがCSVフォーマットで取得可能です。

以下のデータが含まれます：

* インストール
* In-app events
* リターゲティングコンバージョン
* リターゲティングキャンペーンに紐づくアプリ内イベント

**ローデータをエクスポートするには**：

2. 日付範囲を選択してください。
3. レポートを選択します。  
   レポートは数分以内にダウンロードされます。

</Accordion>

<div id="verify-postback-data" />

<Accordion title="ポストバックデータの検証">

インストールが発生する毎に、サーバーへ送信するポストバックが生成されます。ポストバックURL、その内容とパラメータを確認するには、**インストールポストバック**のレポートを取得してください。

**インストールポストバック**のレポートには、**Postback Url**という名称のカラム(列)があります。この列に、インストール毎に生成されたポストバックURLが一覧表示されます。

このデータを見て、以下のことを確認してください。

* URLのエンドポイントが正しいものであること
* Postback URLに追加されたパラメータが、AppsFlyerの計測URLに追加されているパラメータと対応していること
* **Postback Error Message**の列が空欄であること

</Accordion>

<div data-zendesk-anchors="android-integration-testing=android%E3%81%AE%E9%80%A3%E6%90%BA%E3%83%86%E3%82%B9%E3%83%88 h_01HJR6V0MYJXD4QSRT95SVXTWH=android%E3%81%AE%E9%80%A3%E6%90%BA%E3%83%86%E3%82%B9%E3%83%88 testing=%E3%83%86%E3%82%B9%E3%83%88 h_01HJR6V0MYBPC3CSAJTTQSWGAR=%E3%83%86%E3%82%B9%E3%83%88 h_01HJR6V0MYG42PPWXT7H2AGTAE=prerequisites h_01HJR6V0MYDRZGQQ74TJWDJ2WS=test-install-attribution supplementary-information-and-procedures=%E8%A3%9C%E8%B6%B3%E6%83%85%E5%A0%B1%E3%81%8A%E3%82%88%E3%81%B3%E6%89%8B%E9%A0%86%E8%A9%B3%E7%B4%B0%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HJR6V0MYZ5NG21FEKB4HY6HT=%E8%A3%9C%E8%B6%B3%E6%83%85%E5%A0%B1%E3%81%8A%E3%82%88%E3%81%B3%E6%89%8B%E9%A0%86%E8%A9%B3%E7%B4%B0%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HJR6V0MYTZCS097RQP9HG7GY=about-the-partner-integrations-test-app h_01HJR6V0MYVCNVHNCPZ29KRA4K=attribution-link h_01HJR6V0MY6JZXP2NX9YJ9ZY2T=test-app-integrated-in-your-account h_01HJR6V0MYWK7WAAFHRYPCVM7N=troubleshooting h_01HJR6V0MY2SSP17ZEWRM3NXKE=test-retargeting-attribution viewing-retargeted-installs-in-the-dashboard=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%A7%E3%81%AE%E3%83%AA%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AE%E7%A2%BA%E8%AA%8D h_01HJR6V0MYPC0AZF05YF32Z571=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%A7%E3%81%AE%E3%83%AA%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AE%E7%A2%BA%E8%AA%8D h_01HJR6V0MY027J9PKXZZ4TCXRX=test-viewthrough-attribution view-installs-in-the-dashboard=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E4%B8%8A%E3%81%A7%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%AE%E7%A2%BA%E8%AA%8D h_01HJR6V0MZ4VA3V8CA3PN5Z31K=%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E4%B8%8A%E3%81%A7%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%AE%E7%A2%BA%E8%AA%8D h_01HJR6V0MZCZ3E8NCR6DG6P6P1=raw-data-export h_01HJR6V0MZAHSXCTEZKTVWM96V=verify-postback-data" />
