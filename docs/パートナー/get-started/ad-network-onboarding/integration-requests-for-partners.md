---
title: パートナーのための統合変更リクエスト
metadata:
  keywords:
    - postbacks
    - integrated partner
    - view-through attribution
    - Advertisers
    - Ad Networks
    - Partners
    - SKAD
    - Advanced Privacy
    - Marketers
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2021-01-28T12:40:43Z'
  edited_at: '2026-10-14T09:35:09Z'
  id: 360017189177
  locale: ja
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ja/articles/360017189177
---
> **概要**：初期統合設定の変更をリクエストするために知っておくべきことすべて。

<div id="implement-audience-feature" />

<div id="implement-incost-api" />

<div id="important" />

> 🚧 **重要！**
>
> AppsFlyerのポストバックとアトリビューションURL構造はグローバルです。これは、これらの構造の変更がすべてのアプリにわたる既存および将来のキャンペーンに影響を与えることを意味します。

<Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/51444772373393">パートナーアシスタントウィジェット</Anchor>を使用して、パートナー設定を変更するためのチケットを開いてください：

1. AppsFlyerの任意のページの右上から、ヘルプアイコンをクリックします。
2. ウィジェットで次のオプションのシーケンスを選択します：  
   **チームに連絡する** > **(2) 統合を理解または更新したい** > **(1)** **統合を更新**。
3. **高度なプライバシーまたはSKADモード**または**デフォルトモード**のいずれかを選択します。
4. 以下の表に指定された必要な要件を提供してください。

| リクエスト | 詳細 | 要件 |
| --- | --- | --- |
| <span id="enable-viewthrough-attribution"></span>ビュースルーアトリビューションの有効化 | ビューを通じたアトリビューション測定を許可します。  <br />マクロ`attributed_touch_type`は、エンゲージメントタイプを示すためにインプレッションまたはクリックを含みます。 <br /><br /><Anchor target="_blank" href="/marketers/ja/docs/measure-view-through-engagements">ビューを通じたアトリビューションの詳細。</Anchor> | この機能は指定されたパートナーのみが利用可能です。興味がある場合は、パートナー開発マネージャー（PDM）に連絡してください。 |
| <span id="enable-rejected-postback"></span>拒否されたポストバックを有効にする | 詐欺や検証ルールの不遵守による拒否されたインストールおよびアプリ内イベントのポストバックを送信することを許可します。 | <ol><li>AppsFlyerダッシュボードで拒否されたポストバックを構成するには、<Anchor target="_blank" href="/partners/ja/docs/self-serve-integration-management-for-ad-networks">広告ネットワークのセルフサービス統合管理</Anchor>に従ってください。</li><li>拒否されたパラメータをデフォルトのポストバックテンプレート（インストール/アプリ内イベント）に追加することを確認してください。<ul><li>`{is-rejected}</li><li>blocked_reason</li><li>ブロックされたサブ理由</li><li>{blocked-reason-value}</li></ul></li><li>拒否されたパラメータが両方のデフォルトポストバックに追加されると、拒否されたインストール/アプリ内イベントポストバックが有効になります。</li></ol>問題が発生した場合、またはPostback Management Platformにアクセスできない場合:<ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>チケットタイトルとして「拒否されたポストバックを有効にする」と記入してください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>[推奨] マクロの受信パラメータの名前（技術チームによって定義された）is-rejected},{blocked-reason},{blocked-sub-reason},{blocked-reason-value}`</li><li>パラメータを追加すべきポストバックのタイプ（インストール、アプリ内イベント、または両方）</li></ul></li></ol> |
| <span id="enable-retargeting"></span>Enable Retargeting（リターゲティングを有効化） | リターゲティング活動の測定を許可します。<br />AppsFlyerは、キャンペーンがリターゲティングキャンペーンであるかどうか、及びコンバージョンタイプ（再帰属または再エンゲージメント）を特定するために、ポストバックに以下のマクロを提供します:<ul><li>`is-retarget`</li><li>`retargeting_conversion_type`</li></ul><Anchor target="_blank" href="/marketers/ja/docs/retargeting-attribution-guide">リターゲティングについての詳細。</Anchor> | <ol><li>ポストバックをAppsFlyerダッシュボード（インストール/アプリ内イベント）で構成するには、<Anchor target="_blank" href="/partners/ja/docs/self-serve-integration-management-for-ad-networks">セルフサービス統合管理を参照してください</Anchor>。</li><li>以下のパラメータが追加され、設定が保存されると、AppsFlyerバックエンドの「リターゲティングを有効にする」トグルが自動的に有効になります。<ul><li>`{is-retarget}</li><li>{retargeting-conversion-type}`</li></ul></li></ol>問題が発生した場合、またはPostback Management Platformにアクセスできない場合:<ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>チケットタイトルとして「リターゲティングを有効にする」 と記入してください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>[推奨] マクロの受信パラメータの名前（技術チームによって定義された）`is-retarget` と `retargeting_conversion_type`.</li><li>パラメータを追加すべきポストバックのタイプ（インストール、アプリ内イベント、または両方）</li><li>リターゲージメントイベントのために再エンゲージメントポストバックが必要かどうかを示してください（リターゲティングキャンペーン広告をクリックした後の既存アプリの最初のアプリオープンを意味します）</li></ul></li></ol> |
| <span id="enable-uninstall"></span>アンインストールを有効にする | アンインストールを測定するために`af_uninstall`のアプリ内イベントのポストバックを取得します。<br /><br />アンインストールについての詳細。 | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>チケットタイトルとして「af\_uninstallアプリ内イベントポストバックを有効にする」と記入してください。</li><li>PIDまたはログインユーザー名を共有してください</li></ol> |
| <span id="enable-sending-session-data"></span>セッションデータの送信を有効にします | `af_app_opened`のアプリ内イベントのデータ共有を許可します。<br /><br /><Anchor target="_blank" href="/marketers/ja/docs/measure-sessions">セッションデータの詳細について。</Anchor> | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>"af\_app\_openedポストバックを有効にする"をチケットタイトルとして書いてください。</li><li>PIDまたはログインユーザー名を共有してください。</li></ol> |
| <span id="enable-postbacks-retry"></span>ポストバックの再送信を有効化する | 送信失敗の場合にポストバックを複数回送信できるようにします。  <br />ポストバックIDを識別するために`postback-id`マクロを使用します。<br /><br /><Anchor target="_blank" href="/partners/ja/docs/postback-retries">ポストバックの再試行について。</Anchor> | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>"ポストバック再試行を有効にする"をチケットタイトルとして書いてください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>`postback-id`マクロの受信パラメータ名</li></ul></li></ol> |
| <span id="update-postback"></span>ポストバックを更新します | 現在のポストバック構造を変更します（例：パラメータの削除/追加、エンドポイントURLの変更）。<br /><br /><Anchor target="_blank" href="/partners/ja/docs/postback-macros-for-ad-networks">ポストバックとマクロについて。</Anchor> | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>"ポストバックを更新する"をチケットタイトルとして書いてください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>利用可能なマクロに基づく新しいポストバック構造</li></ul></li></ol> |
| <span id="enable-advanced-privacy-postback"></span>高度なプライバシーポストバックを有効にします | 広告主のデータ共有ポリシーに準拠するために高度なプライバシー統合を設定します。<br /><br /><Anchor target="_blank" href="/partners/ja/docs/advanced-privacy-guide-postback-macros-for-ad-networks">高度なプライバシーポストバックについて。</Anchor> | <ol><li>AppsFlyerダッシュボードの<Anchor target="_blank" href="/partners/ja/docs/self-serve-integration-management-for-ad-networks">高度なプライバシーポストバック構成の手順</Anchor>に従ってください。</li><li><Anchor target="_blank" href="/partners/ja/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements">あなたの帰属リンクにすべての必須パラメータが含まれていることを確認してください</Anchor>。</li></ol>問題が発生した場合、または帰属リンクテンプレートにパラメータを追加する必要がある場合：<ol><li>ウィジェットから**高度なプライバシーまたはSKADモード**を選択します。</li><li>チケットタイトルとして「高度なプライバシーのポストバックを有効にする」と記入してください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>利用可能なマクロに基づく高度なプライバシーポストバック構造</li><li>リンクの更新：新しいパラメータとそれに対応するマクロ</li></ul></li></ol> |
| <span id="enable-skadnetwork-postback"></span>SKAdNetworkポストバックを有効にする | SKAdNetworkの統合を設定し、ポストバックを介してAppsFlyerからデコードされたデータを受信できるようにします。<br /><br /><Anchor target="_blank" href="/partners/ja/docs/skan-integration-guide-for-ad-networks">SKAdNetworkポストバックについての詳細。</Anchor> | AppsFlyerダッシュボードで<Anchor target="_blank" href="/partners/ja/docs/self-serve-integration-management-for-ad-networks">SKAdNetworkポストバック構成の手順</Anchor>に従ってください。<br /><br />問題が発生した場合：<ol><li>ウィジェットから**高度なプライバシーまたはSKADモード**を選択します。</li><li>チケットタイトルとして「高度なプライバシーのポストバックを有効にする」と記入してください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>KBからの利用可能なマクロに基づくSKAdNetworkポストバック構造</li><li>AppleのSKAdNetwork ID</li></ul></li></ol> |
| <span id="update-the-logo"></span>ロゴを更新する | ロゴを追加するか、現在のものを置き換えます。 | <ol><li>適切なロゴファイルを持っていることを確認してください：(200x50pxの透明なPNG)</li><li>AppsFlyer管理画面へ進みます。</li><li>右上隅のメールアドレスをクリック > **パートナー設定**を選択します。</li><li>**プロフィール**タブに移動 > **会社のロゴ**。</li><li>**アップロード**アイコンをクリックします。</li><li>ロゴファイルを選択して確認します。</li><li>ページの下部で**保存**をクリックします。ロゴはすぐに更新されます。</li></ol> |
| <span id="update-the-click-attribution-url"></span>クリックの帰属URLを更新します。 | 広告主があなたとキャンペーンを実行するために使用するクリックの帰属URLを更新します。  <br /><Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">帰属リンクについての詳細。</Anchor> | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>チケットタイトルとして「クリックの帰属URLを更新」を記入してください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>新しいパラメータとそれに対応するマクロ。</li></ul></li><li>クリックの帰属URLが更新された後、広告主に更新された帰属リンクURLを尋ねてください。</li></ol> |
| <span id="create-update-partner-dashboard-login-email"></span>パートナーダッシュボードのログインメールを更新します。 | AppsFlyerアカウントへのログイン、ダッシュボードデータの確認、AppsFlyerダッシュボードからのレポートのエクスポートに必要です。 | ユーザーがまだあなたのアカウントに存在しない場合、<Anchor target="_blank" href="/partners/ja/docs/user-management-for-ad-networks#ユーザーの作成">追加する方法はここにあります</Anchor>。<ol><li>新しいユーザーが<Anchor target="_blank" href="/partners/ja/docs/user-management-for-ad-networks#becoming-an-active-user">アクティブ</Anchor>であることを確認してください。</li><li>ウィジェットから**デフォルトモード**を選択します。</li><li>チケットタイトルとして「パートナーダッシュボードのログインを更新」を記入してください。</li><li>以下の情報を共有してください:<ul><li>現在のアカウントメール</li><li>新しいアカウントメール</li><li>アカウント内でのあなたの役割（管理者/チームメンバー/チームメンバーでない）</li></ul></li><li>ダッシュボードのログインが更新された後、通知されます。その後、更新されたメールを使用してパスワードをリセットできます。</li></ol> |
| <span id="disable-integration"></span>連携を無効にする | 統合が無効になっている場合、インストールとアプリ内イベントは無効な統合に帰属しません。<br /><br />**注：** 無効にする前に、広告主が統合との作業を停止したことを確認してください。 | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>「統合を無効にする」とチケットタイトルに書いてください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>無効にする統合はどれですか：インストール、またはアプリ内イベント</li></ul></li></ol> |
| <span id="add-new-dashboard-parameter"></span>新しいダッシュボードパラメータを追加 | 広告主がAppsFlyer広告主ダッシュボードで特定のパラメータを提供できるようにし、ポストバックを介して受け取れるようにします。 | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>「新しいダッシュボードパラメータを追加」とチケットタイトルに書いてください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>新しいダッシュボードパラメータ名</li><li>受信パラメータ—インストールまたはアプリ内イベントポストバックを介して受け取りたい場合</li><li>[推奨] AppsFlyerダッシュボードのパラメータフィールドの横に表示されるツールチップに表示されるパラメータの説明</li></ul></li></ol> |
| <span id="provide-the-postback-template-to-the-partner"></span>パートナーにポストバックテンプレートを提供する | 現在の統合を確認する | <ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>「ポストバックテンプレートを提供する」とチケットタイトルに書いてください。</li><li>以下の情報を共有してください:<ul><li>あなたのPIDまたはログインユーザー名</li><li>確認したいポストバックを指定してください：インストールポストバック、アプリ内イベントポストバック、または拒否されたポストバック</li></ul></li></ol> |
| <span id="implement-click-signing"></span>クリック署名を実装する | 概要：クリックに署名の検証を追加することで、広告不正による被害を回避することが可能です。これにより、不正なクリックがアドネットワークに紐付けられなくなります。 | これらの指示&lt;2>に従って、あなたの側でクリック署名を実装してください。<br />質問がある場合：<ol><li>ウィジェットから**デフォルトモード**を選択します。</li><li>「クリック署名」とチケットタイトルに書いてください。</li><li>PIDまたはログインユーザー名を共有してください。</li></ol> |

<div data-zendesk-anchors="h_01HEPXV5HY3Q502Y8WJAV7HTME=%E9%87%8D%E8%A6%81" />
