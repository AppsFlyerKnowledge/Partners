---
title: アドネットワークへのポストバック：トラブルシューティング
metadata:
  keywords:
    - Postback
    - Ad Networks
    - Partners
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2022-07-07T15:16:00Z'
  edited_at: '2026-10-14T09:31:53Z'
  id: 7466104144145
  locale: ja
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ja/articles/7466104144145
---
> **概要：** ポストバックの受信に問題がある場合は、以下の解決策をご確認ください。

| **問題** | **解決策** |
| --- | --- |
| <span id="i-dont-see-my-advertisers-app-under-my-apps"></span>**マイアプリ**に広告主のアプリが表示されない。 | <ul><li>広告主のアプリが（トップメニューの）**マイアプリ**に表示されない場合は、広告主に連絡して、<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#アドネットワークの権限">関連する権限を付与するよう依頼してください</Anchor>。</li><li>（広告主側で連携設定を有効にしていても、権限付与が行われない限りパートナーアカウント上にはアプリは表示されません。）</li></ul>**注意：** 本番環境のアプリで計測テストを行う場合は、<Anchor target="_blank" href="/marketers/ja/docs/registering-test-devices">こちら</Anchor>の手順に従ってテスト端末を広告主に登録してもらってください。 |
| <span id="im-not-receiving-install-postbacks"></span>インストールポストバックが届かない。 | <ul><li>まず、アプリのインストールが発生していなければ、インストールポストバックも送付されません。  対象アプリでインストール計測があるかどうかを確認するには、**設定** >[**マイアプリ** > [アプリを選択] > <Anchor target="_blank" href="/partners/ja/docs/integrated-partners-dashboard">**オーバービュー**</Anchor> の順に移動してください。</li></ul> |
| <span id="im-not-receiving-inapp-event-postbacks"></span>アプリ内イベントのポストバックが届きません | <ul><li>統合タブの**アプリ内イベントポストバック**セクションで、イベントが<Anchor target="_blank" href="/marketers/ja/docs/in-app-event-postback-configuration">正しくマッピング</Anchor>されていることを確認します。</li></ul>**注意：** イベント名は大文字と小文字が区別されるため、サーバー間/SDK 経由で配信されるのと同じ名前を使用してマッピングする必要があります。 |
| <span id="im-not-receiving-both-install-and-inapp-event-postbacks"></span>インストールとアプリ内イベントのポストバックの両方が届きません | <ul><li>まず、アプリのインストールが発生していなければ、インストールポストバックも送付されません。アプリでインストール成果が計測されているかどうかを確認するには、**設定** >[**マイアプリ** > [アプリを選択] > <Anchor target="_blank" href="/partners/ja/docs/integrated-partners-dashboard">**オーバービュー**</Anchor> の順に移動してください。</li><li>インストール / アプリ内イベントのポストバックのローデータレポートを取得し、以下の項目を確認してください：<ul><li>**Postback URL**：実際に送信されたポストバックのURLです。ポストバック受信に必要な値などが正しく送付されているかを確認してください。</li><li>**Postback HTTP Response Code**：AppsFlyer がパートナーのサーバーから受信するレスポンスコードです。HTTP レスポンスコードを確認し、2XX でない場合は自社サーバーの設定を確認してください。</li><li>**Original URL**：関係するインストール・イベントを計測するにあたって、AppsFlyer が受け取ったクリック・インプレッションのURLです。計測リンクに問題がないか確認してください。リンクに記載されていないパラメータのデータは、ポストバックでも返すことができません。</li></ul></li><li>**高プライバシーモード**の設定を確認してください：有効な場合、<Anchor target="_blank" href="/partners/ja/docs/advanced-privacy-guide-postback-macros-for-ad-networks">iOS 14.5以降のATT非同意ユーザーのユーザーレベルのデータ</Anchor>はポストバックで利用できなくなります。<ul><li>高プライバシーポストバックの連携設定が行われていないのに、広告主が高プライバシーモードを有効なままにしている場合、同意していない iOS ユーザーに関連するポストバックは送信されません。</li></ul></li><li><Anchor target="_blank" href="/marketers/ja/docs/in-app-event-postback-configuration#アプリ内イベントポストバック期間">ポストバック期間</Anchor>の設定を確認してください。設定した期間が過ぎると、ポストバックは送信されません。</li><li><Anchor target="_blank" href="/marketers/ja/docs/in-app-event-postback-configuration#条件付きアプリ内イベントポストバック">条件付きポストバック</Anchor>が定義されているか確認してください。</li><li><Anchor target="_blank" href="/partners/ja/docs/rejected-attribution-postbacks-to-integrated-partners">トラフィックがブロック</Anchor>されていないか確認：**ブロックされたインストールポストバックレポート**をダウンロードして確認してください。</li></ul> |

<div id="see-also" />

> 📄 **参照：**
>
> * <Anchor target="_blank" href="/marketers/ja/docs/postback-troubleshooting-for-advertisers">広告主向け：ポストバックに関するトラブルシューティング</Anchor>
> * <Anchor target="_blank" href="/marketers/ja/docs/in-app-event-postback-configuration">アプリ内イベントのポストバック設定</Anchor>

<div data-zendesk-anchors="h_01HDP4JFM42RZNBGM9TTD5SRP0=%E5%8F%82%E7%85%A7" />
