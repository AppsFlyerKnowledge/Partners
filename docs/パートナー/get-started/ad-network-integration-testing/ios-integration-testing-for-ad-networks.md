---
title: iOS連携テスト：アドネットワーク向け
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
  created_at: '2020-12-16T11:39:36Z'
  edited_at: '2026-10-14T09:21:41Z'
  id: 360016588278
  locale: ja
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ja/articles/360016588278
---
> **概要：** 概要：AppsFlyerとのiOSの連携を、専用のアプリを使うことでレギュラーモード、高プライバシーポストバックでそれぞれポストバックをテストすることが可能です。

## iOSの連携テスト

テストは以下の要素で構成されています。

* iOS版のAppsFlyerのパートナー連携アプリを使用して、まずはテストインストールを発火させ、続いてアプリ内で購入イベントを実施してください。これらのテストによって、あなたのアドネットワークのエンドポイントへポストバックが送信されます。また、ログインと会員登録完了のイベントをテストすることも可能です。
* ポストバックを受信したら、それらをシステムへ取り込むことができるかを確認してください。

### テストの範囲

アドネットワークと共有するデータは、広告主が高プライバシーポストバックの設定で管理します。この設定はアプリユーザーの <Anchor target="_blank" href="/marketers/ja/docs/att-implications-ios-14-and-deprecation-of-lat">ATT</Anchor> の設定状況と連動しており、ポストバックの種類とアドネットワークへ共有されるデータ内容に影響します (詳細は、 <Anchor target="_blank" href="/partners/ja/docs/advanced-privacy-guide-postback-macros-for-ad-networks">高プライバシーポストバックガイド</Anchor> を参照してください。)以下の表で、利用可能な設定の組み合わせに応じた、テストシナリオを示しています。

各シナリオ毎に、インストールとアプリ内イベントのテストが可能です。アプリ内イベントに関しては、<Anchor target="_blank" href="/partners/ja/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">アプリ内イベントをマッピング</Anchor>して、広告主イベントをパートナー側のイベントにマッピングすることが可能です。

#### テストシナリオの組み合わせ

| シナリオ | 高プライバシーポストバック | アプリ側のATT設定 | 送信されるポストバックの種類 |
| --- | --- | --- | --- |
| A | オフ | 許可 | レギュラーポストバック |
| B | オン | 拒否 (追跡しないように設定) | 高プライバシーポストバック |

## テスト

前提条件の準備を全て完了してから、以降のセクションに記載されているテスト手順に従ってください。各テストセクションには、テスト結果を記録するのを助ける表が記載されています。

<div id="prerequisites" />

<Accordion title="前提条件">

テストを開始する前に、前提条件の準備を全て完了してください。

| 前提条件 |
| --- |
| <Anchor target="_blank" href="/partners/ja/docs/getting-started-onboarding-guide-for-ad-networks#パート1統合とテスト">AppsFlyerとのスタンダードな連携の完了</Anchor>（必要に応じて、 <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">パートナーアシスタントウィジェット</Anchor>を使用してAppsFlyerへお問い合わせください。） |
| <Anchor target="_blank" href="/partners/ja/docs/self-serve-integration-management-for-ad-networks#高プライバシーとskanのポストバック">AppsFlyerとの高プライバシーポストバックの連携の完了</Anchor>（必要に応じて、 <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">パートナーアシスタントウィジェット</Anchor>を使用してAppsFlyerへお問い合わせください。） |
| <Anchor target="_blank" href="/partners/ja/docs/turn-on-test-app-integration-for-ad-networks">iOSのテストアプリのパートナーアカウントへの追加</Anchor> |
| [テストアプリがあなたのパートナーアカウント内に表示されていることを確認。](/docs/ios-integration-testing-for-ad-networks#test-app-integrated-in-your-account) |
| <Anchor target="_blank" href="/partners/ja/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">アプリ内イベントのマッピング</Anchor> |
| [計測リンクの準備](/docs/ios-integration-testing-for-ad-networks#attribution-link) |
| iOS14.5以降の端末でのテスト実行 |

</Accordion>

<div id="test-advanced-privacy-off" />

<Accordion title="テスト—高プライバシーポストバック：OFF">

**ポストバックを発火させるには：**

1. AppsFlyerの管理画面上で、[高プライバシーポストバックを有効にする](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy)をOFFに設定してください。
2. 端末上では：
   1. テストアプリがまだインストールされていないことを確認してください。(必要に応じて、一旦テストアプリを削除してください。)
   2. iPhoneのプライバシー設定の項目内で、**アプリのトラッキング要求を許可** の設定がONになっていることを確認してください。  

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. テスト端末に計測リンクを送信し、
4. 端末のブラウザ内で、計測リンクを開いてください。  
   そうすると、AppStoreへリダイレクトされます。
5. アプリをダウンロードして開いてください。  
   そうすると、ATTの同意ダイアログが表示されます。

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. **許可**をタップしてください。  
   その後、以下のような**インストールデータ**のページが表示されます。

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. **ATT Status**のボタンをタップしてください。  
   [ **Authorized (承認済)** ] のステータスが表示されます。
8. 以下のパラメータを使用して、アトリビューション内容を検証してください。検証がうまく行かない場合には、[トラブルシューティング](/docs/ios-integration-testing-for-ad-networks#troubleshooting)を確認してください。

   1. タイムゾーンはUTCで記録されます。
9. **In-App Event Tests**をタップしてください。

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. **Purchase Event**をタップしてください。  
    そうすると、購入イベントの確認が表示されます。
11. 最後に以下を確認してください。
    1. インストールと購入イベントのポストバックを受け取ったこと。
    2. イベント名が正しくマッピングされていること。(イベント名をマッピングした場合)
    3. 受け取ったポストバックを正しく取り込めたこと。

#### 高プライバシーポストバックOFF—テスト結果

| ポストバック | イベントを発火させた時間 | 想定のポストバックの種類 | 実際に受け取ったポストバック(成功/失敗) | ポストバック内容の検証(成功/失敗) |
| --- | --- | --- | --- | --- |
| インストール |  | レギュラーポストバック |  |  |
| アプリ内イベント：購入 |  | レギュラーポストバック |  |  |

</Accordion>

<div id="test-advanced-privacy-on" />

<Accordion title="テスト—高プライバシーポストバックON">

**ポストバックを発火させるには：**

1. AppsFlyerの管理画面上で、[高プライバシーポストバックを有効にする](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy)をONに設定してください。
2. 端末上では：
   1. テストアプリがまだインストールされていないことを確認してください。(必要に応じて、一旦テストアプリを削除してください。)
   2. iPhoneのプライバシー設定の項目内で、**アプリのトラッキング要求を許可** の設定がONになっていることを確認してください。

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. テスト端末に計測リンクを送信し、
4. 端末のブラウザ内で、計測リンクを開いてください。  
   そうすると、AppStoreへリダイレクトされます。
5. アプリをダウンロードして開いてください。  
   そうすると、ATTの同意ダイアログが表示されます。

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. **Appにトラッキングしないように要求**をタップしてください。  
   その後、以下のようなインストールデータ/strong>のページが表示されます。

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. **ATT Status**のボタンをタップしてください。  
   ［**拒否**］のステータスが表示されます。
8. 以下のパラメータを使用して、アトリビューション内容を検証してください。検証がうまく行かない場合には、[トラブルシューティング](/docs/ios-integration-testing-for-ad-networks#troubleshooting)を確認してください。

   1. タイムゾーンはUTCで記録されます。
9. **In-App Event Tests**をタップしてください。

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. **Purchase Event**をタップしてください。
11. 最後に以下を確認してください。
    1. インストールと購入イベントのポストバックを受け取ったこと。
    2. イベント名が正しくマッピングされていること。(イベント名をマッピングした場合)
    3. 受け取ったポストバックを正しく取り込めたこと。

#### 高プライバシーポストバックON—テスト結果

| ポストバック | イベントを発火させた時間 | 想定のポストバックの種類 | 実際に受け取ったポストバック(成功/失敗) | ポストバック内容の検証(成功/失敗) |
| --- | --- | --- | --- | --- |
| インストール |  | 高プライバシーポストバック |  |  |
| アプリ内イベント：購入 |  | 高プライバシーポストバック |  |  |

</Accordion>

## 補足情報および手順詳細について

<div id="about-the-partner-integrations-test-app" />

<Accordion title="パートナー連携テストアプリについて">

アプリを初めて開くと、**iOSのATTダイアログ**が表示され、**インストールデータ**のページにAppsFlyerのプラットフォーム上に記録されたコンバージョンデータが表示されます。また、アプリ内イベントのテストもアプリの画面内で発火可能です。

[<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)

以下のような機能が利用可能です：

* **In-App Event Tests**をタップしてください。  
  各アプリ内イベントをアドネットワーク側のイベント名にマッピングすることで、そのイベント名を使用したポストバックを生成することも可能です。
* ATTのステータス  
  ATTステータス **/strong>iOSによって記録された、現状のATTステータス(［**Authorized<strong>］(承認) / ［Denied］(拒否))の値を返します。ATTステータスは、ATTの同意ダイアログで計測したユーザー同意状況と、端末上での [Appからのトラッキング要求を許可] の設定内容に依って異なります。</strong>

</Accordion>

<div id="attribution-link" />

<Accordion title="計測リンク">

以下のいずれかの方法を使って、AppsFlyerの管理画面上で計測リンクを作成してください。

* AppsFlyerの管理画面上で計測リンクを作成する。
* 以下のサンプルリンクを編集する。

**管理画面上で計測リンクを作成するには：**

1. AppsFlyerの管理画面で、**My Apps**のタブに移動してください。
2. **id1543229303**を選択してください。
4. 計測リンクタブ内で、以下に記載されているパラメータを設定してください。必要であれば、任意のパラメータをさらに追加することも可能です。 

| パラメータ | 値の例 | 備考 |
| --- | --- | --- |
| Campaign | c-test-2020-12-20 | ポストバック内でテストのデータであることを識別可能な値を設定してください。 |

5. 後で使用するので、作成した計測リンクをコピーしてください。

**計測リンクのサンプル：**

```http
https://app.appsflyer.com/id1543229303?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="set-advanced-privacy" />

<Accordion title="高プライバシーポストバックの設定">

<Image alt="AdvancedPrivacyOff.png" src="https://files.readme.io/ef845ea74cbaa0d3214e61c6e2229fd4b9026d0e221b19fecb9e3486e9b795eb-360014980157.png" width="357px" />

**高プライバシーポストバックの設定を変更するには：**

1. AppsFlyerの管理画面で、**My Apps**のタブに移動してください。
2. id1543229303のアプリを選択してください。
4. **高プライバシーポストバックを有効にする**の項目をテストシナリオごとに適切な設定に変更し、設定を保存してください。
5. **連携を保存** をクリックします。

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="パートナーアカウントへのテストアプリの紐付け">

**あなたのパートナーアカウントで、テストアプリが利用可能かどうかの確認方法：**

1. AppsFlyerの管理画面で、**My Apps**のタブに移動してください。
2. もし見当たらない場合には、担当PDMまでご連絡ください。

</Accordion>

<div id="troubleshooting" />

<Accordion title="トラブルシューティング">

| 症状 | 原因と対策 |
| --- | --- |
| インストール時刻が現在の時刻ではない。 | アプリがテストインストール前に削除されていなかった可能性が高いです。<br /><br />一度アプリを削除して、テスト手順を繰り返してください。 |
| 計測されたメディアソースがあなたのメディアソース名ではなかった。 | 計測リンクに正しい**pid**の値が設定されているかどうか確認してください。また、正しい計測リンクを使用しているかどうかも確認してください。 |
| af\_statusがOrganicで計測される。 | 端末のOSバージョンが、前提条件に記載されているものに従っているかを確認してください。<br /><br />計測リンクの形式、特に**pid**の値を確認してみてください。 |

</Accordion>

<div data-zendesk-anchors="ios-integration-testing=ios%E3%81%AE%E9%80%A3%E6%90%BA%E3%83%86%E3%82%B9%E3%83%88 h_01HJR5YDW9ENA1B1AC1DQVX8SF=ios%E3%81%AE%E9%80%A3%E6%90%BA%E3%83%86%E3%82%B9%E3%83%88 testing-scope=%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E7%AF%84%E5%9B%B2 h_01HJR5YDW92MXP9DDBX9C1928V=%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E7%AF%84%E5%9B%B2 test-scenario-combinations=%E3%83%86%E3%82%B9%E3%83%88%E3%82%B7%E3%83%8A%E3%83%AA%E3%82%AA%E3%81%AE%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B h_01HJR5YDW9Q7B10MXB1V4AKH2D=%E3%83%86%E3%82%B9%E3%83%88%E3%82%B7%E3%83%8A%E3%83%AA%E3%82%AA%E3%81%AE%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B testing=%E3%83%86%E3%82%B9%E3%83%88 h_01HJR5YDW9AGY148E1ZD97JFRB=%E3%83%86%E3%82%B9%E3%83%88 h_01HJR5YDW9SGN9KH63CPZ54RM5=prerequisites test%E2%80%94advanced-privacy-off=test-advanced-privacy-off h_01HJR5YDWA20EQT5RE1EJ7QK2X=test-advanced-privacy-off advanced-privacy-off%E2%80%94test-results=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AFoff%E3%83%86%E3%82%B9%E3%83%88%E7%B5%90%E6%9E%9C h_01HJR5YDWAEAR22NPXF8ZD5QX6=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AFoff%E3%83%86%E3%82%B9%E3%83%88%E7%B5%90%E6%9E%9C test%E2%80%94advanced-privacy-on=test-advanced-privacy-on h_01HJR5YDWAY6B55BFQ1B0WJEHR=test-advanced-privacy-on advanced-privacy-on%E2%80%94test-results=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AFon%E3%83%86%E3%82%B9%E3%83%88%E7%B5%90%E6%9E%9C h_01HJR5YDWAK3DZ1Q0W3TSR7ZKZ=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AFon%E3%83%86%E3%82%B9%E3%83%88%E7%B5%90%E6%9E%9C supplementary-information-and-procedures=%E8%A3%9C%E8%B6%B3%E6%83%85%E5%A0%B1%E3%81%8A%E3%82%88%E3%81%B3%E6%89%8B%E9%A0%86%E8%A9%B3%E7%B4%B0%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HJR5YDWA74Q46F6XKY5J375C=%E8%A3%9C%E8%B6%B3%E6%83%85%E5%A0%B1%E3%81%8A%E3%82%88%E3%81%B3%E6%89%8B%E9%A0%86%E8%A9%B3%E7%B4%B0%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HJR5YDWASJWC1NGNABWR1VW5=about-the-partner-integrations-test-app h_01HJR5YDWA0WXWN5B5VNPK40FY=attribution-link h_01HJR5YDWA73BQB478D6N0R8GP=set-advanced-privacy h_01HJR5YDWAGZ5XMQJG1KX3J6CP=test-app-integrated-in-your-account h_01HJR5YDWAXRD7DVHTZPJCFM56=troubleshooting" />
