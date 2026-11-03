---
title: 連携テストアプリの有効化：アドネットワーク向け
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
  created_at: '2021-05-22T15:56:20Z'
  edited_at: '2026-10-14T09:19:50Z'
  id: 360020713538
  locale: ja
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ja/articles/360020713538
---
> **概要：** 概要：アドネットワークが連携テストを行う場合には、必ずテストアプリの連携を有効化（アクティブ）する必要があります。

## アドネットワーク向けのテストアプリ（iOS/Android）

連携とポストバックの設定が完了したアドネットワークは、次にAppsFlyerのテストアプリを使って連携のテストを実施する必要があります。テスト前に、まずはそのテストアプリとの連携を有効にし、必要に応じて追加でアドネットワーク向けの権限を有効にする必要があります。なお、この作業は1アプリにつき1度のみ必要です。

| テストアプリのタイプ | アプリID |
| --- | --- |
| <Anchor target="_blank" href="/partners/ja/docs/getting-started-onboarding-guide-for-ad-networks#パート2広告主アプリを使用してテストします">Android</Anchor> | com.appsflyer.adNetworkTest |
| <Anchor target="_blank" href="/partners/ja/docs/ios-integration-testing-for-ad-networks">iOS</Anchor> | id1543229303 |
| <Anchor target="_blank" href="/partners/ja/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> | <ul><li>id888707085</li><li>id888707086</li><li>id888707087</li></ul> |

### 連携有効化の手順

以下の手順で、上記テストアプリとの連携を有効にしてください。繰り返しになりますが、この手順を行うのはアプリ毎に1回ずつです。

**連携を有効にし、テストアプリへの権限を付与するには：**

1. AppsFlyerのパートナーアカウントで管理画面に入り、上記表に記載されているテストアプリを１つ選んでクリックしてください。
2. AppsFlyer管理画面 左メニュー **連携** > **連携済みパートナー**を選択します。
3. ご自身のアドネットワークを検索して編集画面を開いてください。
4. **テストアプリとの連携を有効にするには：**  
   1. **連携**タブを開きます。
   2. **パートナーを有効にする** をオンにしてください。
   3. **連携を保存**をクリックします。
5. **権限を付与するには：**
   1. **権限**タブへ進んでください。
   2. <strong>［パートナー連携の設定を許可する］</strong>をONにしてください。
   3. **［アプリ内イベントのポストバックを許可する］** をONにしてください。
   4. 最後に、<strong>［保存 権限］</strong>をクリックしてください。

<div data-zendesk-anchors="test-apps-for-ad-networks-ios-and-android=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88%E3%82%A2%E3%83%97%E3%83%AAiosandroid h_01HKA15VM7FM69X0AZ1V2H5XPJ=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91%E3%81%AE%E3%83%86%E3%82%B9%E3%83%88%E3%82%A2%E3%83%97%E3%83%AAiosandroid activation-procedure=%E9%80%A3%E6%90%BA%E6%9C%89%E5%8A%B9%E5%8C%96%E3%81%AE%E6%89%8B%E9%A0%86 h_01HKA15VM7J47374WMRG5132GN=%E9%80%A3%E6%90%BA%E6%9C%89%E5%8A%B9%E5%8C%96%E3%81%AE%E6%89%8B%E9%A0%86" />
