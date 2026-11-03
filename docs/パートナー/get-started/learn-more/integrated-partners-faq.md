---
title: 連携済みパートナー　— よくある質問
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
  created_at: '2021-09-02T09:33:34Z'
  edited_at: '2026-10-14T09:32:44Z'
  id: 4406549295249
  locale: ja
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/ja/articles/4406549295249
---
> **概要**：概要：このページでは、連携済みパートナからよくいただく質問や連携のトラブルシューティングについて記載しています。

## アカウントと管理画面について

<div id="i-want-to-become-an-integrated-partner" />

<Accordion title="連携済みパートナーになりたい場合">

AppsFlyerと新しく連携を行うには、広告主から招待してもらう必要があります。

まずは<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#appsflyerに新しいパートナーを招待する">こちらの招待手順</Anchor>を広告主に共有してください。広告主からの招待が完了すると、記入フォームが添えられたメールが届きます。  
入力が完了しましたら次のステップについて順次ご連絡させていただきます。

重要：重要：過去にAppsFlyerで各種アカウントの作成に使用したことのないメールアドレスを必ず使用してください。また、広告主は自身の広告主アカウントと同じメールアドレスを使って招待する必要があるので、そちらもご注意ください。

</Accordion>

<div id="how-can-i-update-my-integration" />

<Accordion title="連携設定を更新したい場合には？">

<Anchor target="_blank" href="/partners/ja/docs/integration-requests-for-partners">こちら</Anchor>で必要な更新内容をご覧いただき、それぞれの案内に従ってください。

</Accordion>

<div id="how-do-i-change-the-login-email-of-the-account" />

<Accordion title="アカウントのログインメールアドレスを変更するにはどうしたらいいですか？">

<Anchor target="_blank" href="/partners/ja/docs/integration-requests-for-partners#create-update-partner-dashboard-login-email">こちらの手順</Anchor>に従ってください。

</Accordion>

<div id="i-cant-add-an-app-to-the-dashboard" />

<Accordion title="管理画面に広告主のアプリを追加することができません">

**アプリ検索**の画面にアプリが追加されない場合、以下のポイントを確認してください。

* 広告主がそのアプリを広告主アカウント上に追加済みであること
* 広告主がそのアプリにおいて、ご自身のアドネットワークとの連携を有効にしていること

</Accordion>

<div id="i-dont-see-the-app-on-my-dashboard" />

<Accordion title="管理画面に広告主のアプリが表示されません">

| 理由 | 解決策 |
| --- | --- |
| 広告主が、あなたのアドネットワークに対して適切な権限を付与していないからです。 | 広告主に連絡し、<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#アドネットワークの権限">こちらの手順</Anchor>に従ってあなたのアドネットワークに対する権限を有効にするよう依頼してください。 |

</Accordion>

<div id="the-integration-with-the-app-isnt-active-in-the-dashboard-when-it-definitely-should-be-active" />

<Accordion title="アプリとの連携が有効になっているなはずなのに、管理画面上で有効と表示されていません">

| 理由 | 解決策 |
| --- | --- |
| 広告主ではなく、代理店によって連携が有効にされているからです。アドネットワークの連携設定は、広告主アカウント上で設定されたもののみが、アドネットワークアカウント上で表示されます。 | これ以上の操作は必要ありません。設定内容は確認できませんが、代理店が連携設定を有効にしているのであれば計測やポストバックは正常に機能します。 |

</Accordion>

<div id="im-not-receiving-password-recovery-emails" />

<Accordion title="パスワード再設定のメールが届きません。">

1. まずは迷惑メールフォルダを確認してください。
2. 使用しているブラウザのキャッシュをクリアする化、別のブラウザソフトを使ってAppsFlyerへアクセスしてください。
3. お手数ですが、再度パスワードのリセットを行ってください。（前回の作業から30分以上待ってください。）

</Accordion>

<div id="how-do-i-enable-the-appsflyer-audience-integration" />

<Accordion title="AppsFlyerとのAudiences連携を有効にしたい場合にはどうしたらいいですか？">

1. Audiences連携の実装を要求している広告主の了承を得てください。
3. 内容を確認後、リクエストが承認された場合には順次連携を進行させていただきます。

</Accordion>

<div id="how-do-i-enable-advanced-privacy" />

<Accordion title="高プライバシーポストバックの連携を行うにはどうしたらいいですか？">

<Anchor target="_blank" href="/partners/ja/docs/self-serve-integration-management-for-ad-networks#高プライバシーとskanのポストバック">こちらの手順</Anchor>に従ってください。

</Accordion>

* <Anchor target="_blank" href="/partners/ja/docs/getting-started-onboarding-guide-for-ad-networks#統合検証期間">統合検証期間</Anchor>


## パートナー権限

<div id="what-are-the-partner-permissions" />

<Accordion title="パートナー権限とは？">

広告主は、アドネットワーク(パートナー)との連携設定を行う権限をそのアドネットワーク自体に付与することができます。

パートナーは、広告主が設定したパートナー連携を編集および変更する権限を持っている場合、キャンペーン設定をテストできます。

付与可能な権限は以下です。(広告主側の契約内容によって異なります）：

* 連携設定の変更（広告主アカウント上）
* アプリ内イベントのポストバック設定
* リテンションレポート
* Protect360 管理画面

詳細は、<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">アドネットワークへの権限付与</Anchor>のページを参照してください。

</Accordion>

<div id="i-cant-configure-the-integration-with-the-advertiser" />

<Accordion title="広告主との連携を設定できません">

| 理由 | 解決策 |
| --- | --- |
| 広告主が、連携設定を行う権限をあなたのアドネットワークに対して付与していないからです。 | 以下の権限があなたのアドネットワークに対して付与されているかどうか、広告主へ確認を依頼してください：<ul><li>アドネットワークへの権限付与（メインのトグル）</li><li>連携を設定</li><li>アプリ内イベントポストバックの設定</li></ul> |

</Accordion>

<div id="the-advertiser-cant-grant-permissions-to-ad-network-team-members" />

<Accordion title="広告主がアドネットワークのチームメンバーへ権限を付与できません">

| 理由 | 解決策 |
| --- | --- |
|  | まずはあなたのパートナーアカウントのチームメンバーアカウントとして、そのメールアドレスを新しく追加してください。そして、追加後に広告主へ再度作業を依頼してください。<br /><br />**注記：** 注：新しいチームメンバーをパートナーアカウントに追加できるのは、アカウント管理者と関連する管理機能を持ったチームメンバーのみです。 |

</Accordion>

<div id="what-about-agency-permissions" />

<Accordion title="代理店の権限はどうですか？">

マーケティング担当が付与できる代理店の権限については<Anchor target="_blank" href="/partners/ja/docs/getting-started-agency-onboarding#マーケティング担当者からの権限を得るとはどういうことですか">こちらを参照</Anchor>ください。

</Accordion>

## データ：ポストバックとレポート

<div id="how-long-does-it-take-for-results-to-appear-in-the-dashboard" />

<Accordion title="管理画面に配信結果が反映されるまでには、どれくらい時間が掛かりますか？">

インストールの情報は、インストール発生から最長2分以内には管理画面上に表示されます。

インストールとアプリ内イベントの情報は。15分以内に各種レポートデータ内に記載されます。

</Accordion>

<div id="i-cant-see-the-event-value-or-revenue-in-the-event-postback-or-on-the-dashboard" />

<Accordion title="管理画面やイベントのポストバックにおいて、イベントの収益のデータやイベント値 (event_value) の情報が表示されません">

<table><thead><tr><th>理由</th><th>解決策</th></tr></thead><tbody><tr><td>1. イベントポストバックの設定に、収益に関するマクロが含まれていないからです。</td><td> </td></tr><tr><td>2. AppsFlyerから送信されるイベントポストバックデータに、収益データが含まないよう設定されているからです。</td><td><ul><li>アプリの連携設定画面への権限が付与されているのであれば、<ol><li>AppsFlyer管理画面 左メニュー <strong>連携</strong> &gt; <strong>連携済みパートナー</strong>へ移動し、アドネットワークを選択します。</li><li> <strong>連携</strong>タブ内にある<strong>アプリ内イベントポストバック</strong>のセクションで、マッピングされているイベントの一覧を確認してください。</li><li>関連するイベントの<strong>収益値を送信</strong>の箇所で、<strong>イベント値も収益も送信する</strong>の選択肢を選んで設定を保存してください。</li></ol></li><li>もしも連携設定の権限を持っていないのであれば、広告主に<a href="/marketers/ja/docs/set-up-an-integrated-partner#アドネットワークの権限" target="_blank">アドネットワークへの権限付与作業</a>を依頼してください。  </li></ul></td></tr><tr><td>3. 広告主が、あなたのアドネットワークと収益に関する情報を共有しないよう設定しているからです。</td></tr></tbody></table>

<Anchor target="_blank" href="/marketers/ja/docs/in-app-event-postback-configuration#ポストバックに含めるデータ">イベントデータの送信と想定シナリオの詳細については、こちらを参照してください。</Anchor>

</Accordion>

<div id="im-not-receiving-inapp-event-postbacks" />

<Accordion title="アプリ内イベントのポストバックが届きません">

| 理由 | 解決策 |
| --- | --- |
|  |  |
|  | 対象イベントが正しく発火しており、またアプリ内イベントのポストバック設定が正しく行われているかどうか、広告主（もしくは代理店）へ確認してください。 |
|  |  |
|  |  |

</Accordion>

<div id="click-data-is-missing-in-the-postback" />

<Accordion title="ポストバックにクリックデータがありません">

| 理由 | 解決策 |
| --- | --- |
|  | クリックパラメータとその値がクリックアトリビューションURLに含まれていることを確認してください。 |
|  |  |
|  |  |

</Accordion>

<div id="there-are-missing-dashboard-parameters-in-the-postback" />

<Accordion title="ポストバックにダッシュボードのパラメーターが含まれていません">

| 理由 | 解決策 |
| --- | --- |
|  | <ul><li>アプリの連携設定画面への権限が付与されているのであれば、</li><li>もしも連携設定の権限を持っていないのであれば、広告主に<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#アドネットワークの権限">アドネットワークへの権限付与作業</Anchor>を依頼してください。</li></ul> |

</Accordion>

<div id="servertoserver-event-data-from-the-advertiser-is-missing-or-incorrect" />

<Accordion title="広告主からのサーバー間 (S2S) イベントデータが見つからない / 正しくありません">

| 理由 | 解決策 |
| --- | --- |
|  |  |

</Accordion>

<div id="im-not-receiving-reengagement-postbacks" />

<Accordion title="リエンゲージメントポストバックが届きません">

| 理由 | 解決策 |
| --- | --- |
|  |  |
|  |  |
| リターゲティングパラメーターがクリック計測リンクに含まれていないため、リアトリビューションがAppsFlyerで記録されません。 |  |

</Accordion>

<div id="im-not-receiving-reattribution-postbacks" />

<Accordion title="リアトリビューションポストバックが届きません">

| 理由 | 解決策 |
| --- | --- |
|  |  |
| リターゲティングパラメーターがクリック計測リンクに含まれていないため、リアトリビューションがAppsFlyerで記録されません。 |  |

</Accordion>

<div id="im-not-receiving-correct-event-identifiers-on-event-postbacks" />

<Accordion title="イベントポストバックで正しいイベント識別子が届きません">

| 理由 | 解決策 |
| --- | --- |
|  |  |
|  | ユーザーがまだアプリを持っていない場合は... |

</Accordion>

<div id="i-cant-see-campaignlevel-data-for-nonattributed-traffic-on-postbacks" />

<Accordion title="ポストバックで成果に紐づいていないトラフィックのキャンペーンレベルのデータが確認できません">

</Accordion>

<div id="i-cant-export-reports" />

<Accordion title="レポートをエクスポートできません">

| 理由 | 解決策 |
| --- | --- |
|  |  |
|  | 使用しているブラウザのキャッシュをクリアして再度お試しいただくか、別のブラウザソフトを使用してレポートをエクスポートしてください。 |

</Accordion>

<div id="i-cant-download-a-report-i-get-a-message-that-the-report-quota-has-exceeded" />

<Accordion title="レポートをダウンロードできず、レポートの最大数を超えたというメッセージが表示されます">

</Accordion>

<div id="test-installs-dont-appear-in-the-dashboard" />

<Accordion title="テストインストールが管理画面に反映されない">

広告主と一緒にインストール計測のテストをしてもAppsFlyerの管理画面上にインストールが表示されない場合には：

1. テストに使用している端末を、広告主がホワイトリストに登録していることを確認してください。
2. S2Sでの確率論的モデリングを使用してキャンペーンを実施する場合には、連携が正しく行われているかどうかをAppsFlyerと確認する必要があります。詳細は担当PDMまでお問い合わせください。

</Accordion>

ポストバックがサーバーに送信されていないと思われる場合には：

* ポストバックのエンドポイントがアクティブな状態であることを確認してください。
* ポストバックのエンドポイントが正しいかどうかを確認してください。修正が必要な場合には、担当PDMまでお問い合わせください。


<div id="inapp-event-postbacks-arent-sent-to-my-servers" />

<Accordion title="アプリ内イベントのポストバックがサーバーに送信されない。">

アプリ内イベントのポストバック設定は、広告主アカウント（もしくは代理店アカウント）管理画面上であなたのアドネットワークの設定画面において行われている必要があります。

* まずは広告主または代理店へ、イベントのポストバック設定を有効にするよう依頼してください。
* 広告主がアプリ内イベントのポストバック設定権限を付与している場合には、 **連携**タブ内の**アプリ内イベントポストバック**が有効になっていることを確認してください。

</Accordion>

<div id="i-cant-see-the-inapp-events-postback-setup-of-agencies" />

<Accordion title="代理店で設定したアプリ内イベントポストバックが確認できません">

広告ネットワークは、広告主アカウント上で行われた連携設定を確認することができますが、**代理店アカウント上で行われた設定は確認できません**。そのため、代理店がアプリ内イベントをネットワークにマッピングしてポストバックを設定すると、そのイベントは代理店に対してはアクティブですが、広告ネットワークではこのセクションは非アクティブと見なされます。

> 📄 **例**
>
> Yuval氏は、**Sonnet**アドネットワークにとっての広告主である、**com.fused**というアプリのマーケターです。彼は、Sonnetに成果が紐付いたユーザーが購入イベントを行ったときに発火するaf\_purchaseイベントをSonnetにマッピングしています。
> **com.fused**の代理店権限を付与されている**Sava**という代理店も、同じく**Sonnet**の連携設定を行っており、**af\_completeregistration** のポストバックを行うよう設定を行っています。
>
> **Sonnet**がパートナーアカウントで**com.fused**の管理画面に入ると、**af\_purchase**のイベントのみがマッピングされているのが確認でき、**af\_completeregistration**はマッピングされていません。しかし、**Sava**に成果が紐付いたユーザーが**af\_completeregistration**のイベントを行うと、**Sonnet**に対してイベントがポストバックされます。

</Accordion>

<div id="click-data-is-missing" />

<Accordion title="クリックデータがない">

ポストバックデータの中にクリックに関するデータが見つからない場合は、AppsFlyerの計測リンクに、ポストバックで返送するべき全てのデータが含まれていることを確認してください。詳細は<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">計測リンクガイド</Anchor>を参照してください。

広告主側で全データのポストバックを受信するようにアドネットワークの連携設定を行った場合、そのアドネットワークに紐付けられていないインストール経由で発生したイベントのポストバックには、クリックデータは含まれません。

</Accordion>

<div id="revenue-data-is-missing" />

<Accordion title="収益データがない">

ポストバックの中で収益データが欠落しているか、「N/A」と表示される場合には次の2つの理由が考えられます。

* 広告主が収益データは共有しないよう設定している。
* 広告主が正しく収益の情報を実装できていない。

</Accordion>

<div id="i-see-installs-in-appsflyer-but-not-on-my-internal-servers" />

<Accordion title="AppsFlyer上ではインストールが発生しているが、媒体側のサーバー上にはない">

AppsFlyerの計測リンクを、リダイレクトURLとしてあなたのサーバーに設置する必要があります。次に、アドネットワーク側の独自の計測リンクを使用して、完全はテストを実施してください。

自身のアドネットワーク側の計測リンクのパラメータがAppsFlyer側の計測リンクにマッピングされていることを確認してください。

</Accordion>

<div id="dashboard-data-is-missing" />

<Accordion title="管理画面上にデータがない">

もしもあなたのアドネットワークが連携において各種IDやキーの入力を必要とするのに対し、広告主側（もしくは代理店側）で入力がされていなかった場合、AppsFlyerからのポストバックがアドネットワーク側のサーバーによって受信を拒否されることがあります。ポストバックデータをサーバーに送信できないため、結果的にデータがサーバー上にないのです。


この場合、管理画面にはデータが表示されますが、サーバーには表示されません。広告主（もしくは代理店）は、アドネットワークによっては**連携タブの**一般設定のセクションにある、ID、キー、トークンなどの情報を連携時に入力する必要があることがあります。

広告主がアドネットワークとの連携を設定する際に必要な認証情報またはキーを提供していることを確認してください。

</Accordion>

<div id="data-from-the-advertiser-is-missing-or-incorrect" />

<Accordion title="広告主からのデータが見つからない / 正しくない。">

広告主と一緒に連携をテストするも、インストール、アプリ内イベントのデータが利用できない場合には、以下のステップに従ってください。

* どの広告主においても問題が発生した場合には、担当のPDMまでお問い合わせください。
* 問題が１つの広告主のみ、もしくは一部の広告主に限られる場合には：
  * 広告主がアプリにAppsFlyerのSDKを実装していることを確認してください。
  * 広告主がアプリにAppsFlyerのSDKを正しく実装していることを確認してください。

</Accordion>

<div id="there-is-a-discrepancy-on-click-data-between-appsflyer-and-our-platform" />

<Accordion title="AppsFlyerと当社のプラットフォーム間でクリックデータに乖離があります">

| 問題 | 解決策 |
| --- | --- |
|  |  |
| クリックキャッピング |  |
|  |  |
|  |  |
|  | N/A |

</Accordion>

<div id="my-agency-account-doesnt-show-skan-data" />

<Accordion title="代理店アカウントに SKAN データが表示されません">

<strong>キャンペーン名が正しく設定されていることを確認してください。</strong>代理店のSKAdNetwork管理画面からキャンペーンを確認するには、以下の通り、SKAdNetworkで設定されたキャンペーン名に代理店の識別子を含める必要があります。

</Accordion>

## Protect360

不正なトラフィックを配信するサイト運営者とさらに調査し、そのようなサイト運営者との連携についてデータに基づいた決定を下すことができます。


<Anchor target="_blank" href="/partners/ja/docs/test-marketer-campaign-integration-with-the-ad-network">正しくテストするには、</Anchor>こちらの手順に従ってください。

<div data-zendesk-anchors="account-and-dashboard=%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A8%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HKW6K6RFAEX8SKMAWSCKC3AD=%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A8%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HKW6K6RF7M3YBCAE2QWDKP81=i-want-to-become-an-integrated-partner h_01HKW6K6RF4ZFY3YDW0KR1TQP2=how-can-i-update-my-integration h_01HKW6K6RF7JAC8MKMZGS8K01C=how-do-i-change-the-login-email-of-the-account h_01HKW6K6RFEDYV0T3019THZHF7=i-cant-add-an-app-to-the-dashboard h_01HKW6K6RF3RRTYQ8CJ453NM30=i-dont-see-the-app-on-my-dashboard h_01HKW6K6RF81BHWCAERR50QY1E=the-integration-with-the-app-isnt-active-in-the-dashboard-when-it-definitely-should-be-active h_01HKW6K6RFTBAJ1Y2HJTR3GKFD=im-not-receiving-password-recovery-emails h_01HKW6K6RFQ37XXGMVY7N3AP16=how-do-i-enable-the-appsflyer-audience-integration h_01HKW6K6RF50HWPS1E3KPYWQN0=how-do-i-enable-advanced-privacy partner-permissions=%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E6%A8%A9%E9%99%90 h_01HW8J4Q9J83ANG3VX2T2V0JMH=%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E6%A8%A9%E9%99%90 h_01HKW6K6RFRJXJ0JF5MPJ5SKZY=what-are-the-partner-permissions h_01HKW6K6RFX8V6AFKNBJBFZAK0=i-cant-configure-the-integration-with-the-advertiser h_01HKW6K6RFRQK1SFK8Z864RGTK=the-advertiser-cant-grant-permissions-to-ad-network-team-members h_01HKW6K6RFJ54162BJFWAW36DJ=what-about-agency-permissions data-postbacks-and-reports=%E3%83%87%E3%83%BC%E3%82%BF%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%A8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HKW6K6RFHBVQMMWZYCE0VWB6=%E3%83%87%E3%83%BC%E3%82%BF%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%A8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HKW6K6RF53FWYZJDYGJ3GWA8=how-long-does-it-take-for-results-to-appear-in-the-dashboard h_01HKW6K6RG99YJX6001R22KQVQ=i-cant-see-the-event-value-or-revenue-in-the-event-postback-or-on-the-dashboard h_01HKW6K6RGF9SCX7SBED6095R1=im-not-receiving-inapp-event-postbacks h_01HKW6K6RGZSQAZERA875QC5PC=click-data-is-missing-in-the-postback h_01HKW6K6RGV4FJ6B0HDV0N4P37=there-are-missing-dashboard-parameters-in-the-postback h_01HKW6K6RG9Y6J5RW4AYQABX95=servertoserver-event-data-from-the-advertiser-is-missing-or-incorrect h_01HKW6K6RGV8TEJ1N6MQFMXSXX=im-not-receiving-reengagement-postbacks h_01HKW6K6RGWXBDPEFQ2T2019Y5=im-not-receiving-reattribution-postbacks h_01HKW6K6RGKQY5YS1V1PVE97ZK=im-not-receiving-correct-event-identifiers-on-event-postbacks h_01HKW6K6RGJFD51XTBBSTMAW92=i-cant-see-campaignlevel-data-for-nonattributed-traffic-on-postbacks h_01HKW6K6RG401RK36GVWGX1JNP=i-cant-export-reports h_01HKW6K6RGYB3WF4EJZSQKKMK1=i-cant-download-a-report-i-get-a-message-that-the-report-quota-has-exceeded h_01HKW6K6RGGD3BQR36R971C952=test-installs-dont-appear-in-the-dashboard h_01HKW6K6RGR8GM3GBSNW5SE502=inapp-event-postbacks-arent-sent-to-my-servers h_01HKW6K6RGZ8J5RTYX5CZED36R=i-cant-see-the-inapp-events-postback-setup-of-agencies h_01HKW6K6RGCRPTK1B78JH94WR4=%E4%BE%8B h_01HKW6K6RGN804BA8SSTNP6SGG=click-data-is-missing h_01HKW6K6RG5HCS5XXTWJF42D89=revenue-data-is-missing h_01HKW6K6RGHGSC26XF43SE7HJY=i-see-installs-in-appsflyer-but-not-on-my-internal-servers h_01HKW6K6RGEYF4VZZTQW2BPMPN=dashboard-data-is-missing h_01HKW6K6RGWAEAP4YV4AWDVRKW=data-from-the-advertiser-is-missing-or-incorrect h_01HKW6K6RH2RWH5R9S8K0YRNVW=there-is-a-discrepancy-on-click-data-between-appsflyer-and-our-platform h_01HKW6K6RH18CM36N29K2QGXB7=my-agency-account-doesnt-show-skan-data h_01HKW6K6RHWS457Q0DAKK0R1Q6=protect360" />
