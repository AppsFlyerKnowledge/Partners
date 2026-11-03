---
title: 代理店アカウントについて
metadata:
  keywords:
    - In-App Events
    - Agency Account
    - ROI
    - Agency
    - FMP
    - Advertisers
    - Agencies
    - Listed Agency
    - all installs
    - all launches
    - Partners
    - agency sign up
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2013-12-08T10:02:42Z'
  edited_at: '2026-10-14T09:21:10Z'
  id: 207034106
  locale: ja
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/ja/articles/207034106
---
> **概要:** 高度な設定を活用し、AppsFlyer代理店アカウントを最大限に活用しましょう。

## 代理店アカウントについて

代理店アカウントは、代理店チームがクライアント(アプリ所有者)に代わって行うアプリマーケティングキャンペーンを測定します。

* 代理店がクライアントポートフォリオ全体で最適なパフォーマンスを提供できるように、インストール前とインストール後の主要な指標が利用できます。
* 代理店アカウントの管理画面は、マーケターの管理画面と同様の機能とコンテンツを提供します。次の管理画面が含まれます。
  * ライフタイムバリュー概要
  * アプリ内イベント
  * リターゲティング
* 利用可能なKPIは、インプレッション、クリック、インストール、ユーザーロイヤルティ、コスト、ROIなどがあります。管理画面について

### 代理店のマーケターデータへのアクセス

代理店は、関連するトラフィックのデータにいつでもアクセスできます。マーケターは、オーガニック集計データなどの追加データへのアクセス権を代理店に付与できます。さまざまなタイプのユーザーによるデータへのアクセスについては、<Anchor target="_blank" href="/marketers/ja/docs/manage-data-access-permissions">こちらをご覧ください。</Anchor>

### アドネットワーク統合への代理店のアクセス

アドネットワーク統合へのアクセスを可能にし、キャンペーンを測定するには、代理店がアドネットワークから事前承認を受ける必要があります。これは、代理店ID(af\_prt)をアドネットワークの認定代理店リストに含めることで行われます。代理店が含まれることを確認するためにパートナーに連絡してください。代理店IDの確認方法については、[こちら](/docs/about-agency-accounts#af_prtパラメータ)をご覧ください。

> 📘 **注記**
>
> * 帰属リンクの空のaf\_prtパラメーターにも適用されます
> * SRNを扱う代理店には適用されません。

### 代理店の透明性

代理店のトラフィックはデフォルトで透明に設定されています。<Anchor target="_blank" href="/partners/ja/docs/getting-started-agency-onboarding#運用媒体の開示">詳細はこちら</Anchor>

## 異なるアカウントのタイプの比較

<div id="agency-versus-marketer-accounts" />

<Accordion title="代理店アカウントとマーケターアカウントの比較">

* マーケターアカウントは、アプリおよびデータ所有者にサービスを提供するために設計されています。マーケターはアカウントにアプリを追加し、データアクセス権限を決定します。
* 代理店アカウントは代理店チーム向けに特別に設計されています。それには、クライアントポートフォリオ全体で行われるマーケティングキャンペーンを効率的に計測および分析するためのツールが含まれています。

アカウント構造により、グローバルな代理店チーム間での知識共有が可能になり、グループレベルでのROI計測、計算、レポート、最適化が可能になります。

#### マーケターアカウントと代理店アカウントの違い

|  | マーケター | **代理店** |
| --- | --- | --- |
| コードレベルの実装 | はい | いいえ、アプリのプロモーションのみ |
| アカウントレベルの設定 | チームメンバー、チームメンバーの権限、設定、支払い設定 | 代理店チームのメンバーとその権限。 |
| アプリレベルの設定 | リアトリビューション期間、OneLink構成、タイムゾーン、通貨 | 他のすべての設定はマーケターによって設定されたものに従う |
| 統合パートナーレベルの構成 | <ul><li>代理店の許可</li><li>すべての非SRN（アトリビューションリンクベースの広告ネットワーク）構成</li><li>SRN 構成</li><li>リンク管理</li></ul> | <ul><li>すべての非SRN構成</li><li>マーケター側の介入が最小限で済むSRN構成の例:</li></ul><ul><li>Googleダブルクリック<ul><li>Snapchat</li><li>Tencent</li></ul></li></ul>その他のSRNは、代理店が利用するためにマーケターにより設定される必要があります。<ul><li>リンク管理（マーケターが定義したテンプレートを使用）</li></ul> |
| 追加機能 | はい（サブスクリプションプランの一部である場合のみ） | マーケターのサブスクリプションと代理店に付与された<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#代理店の許可">権限</Anchor>に応じて（下のテーブルを参照） |

### 代理店が利用できる機能

| デフォルトで利用可能 | 利用不可 | マーケターの許可が必要 |
| --- | --- | --- |
| <ul><li>ライフタイム価値概要管理画面</li><li>アプリ内イベント管理画面</li><li>リターゲティング管理画面</li><li>アクティブ統合</li><li><Anchor target="_blank" href="/partners/ja/docs/getting-started-agency-onboarding#代理店向け-single-source-of-truth-ssot">SSOT管理画面</Anchor>\*\*</li></ul>\*\* マーケターがこのオプションを有効にした後にのみ利用可能です。 | <ul><li>アクティビティ管理画面</li><li>カスタム管理画面</li><li>人ベースの分析</li><li>オーディエンス</li><li>ピボットレポート</li><li>プッシュAPI</li><li>データロッカー</li></ul>*コホートレポートはマーケターからの許可が必要です | <ul><li>リテンションレポート</li><li>コホート管理画面レポート</li><li><Anchor target="_blank" href="/partners/ja/docs/data-locker-reports-for-agencies">データロッカーからのコホートレポート</Anchor></li><li>プロテクト360</li><li>生データのエクスポート</li><li>オーガニックデータの集計</li><li>プルAPI</li></ul> |

</Accordion>

<div id="agency-vs-ad-network-account" />

<Accordion title="代理店とアドネットワークのアカウント">

#### アドネットワークと代理店アカウントの違い

<table><thead><tr><th>アドネットワーク</th><th>代理店</th></tr></thead><tbody><tr><td>識別のためのアトリビューションリンクパラメータ: <code>pid</code> </td><td>識別のためのアトリビューションリンクパラメータ: <code>af_prt</code> </td></tr><tr><td>独自のプラットフォームにアプリ広告を掲載</td><td>複数のメディアソースを通じてアプリを宣伝する</td></tr><tr><td>自社のプラットフォームに掲載された広告からのトラフィックのみを表示</td><td>広告を掲載しているメディアソースからのトラフィックのみを表示</td></tr><tr><td>ポストバックを介してインストールやアプリ内イベントに関するリアルタイム情報を受け取ることができます</td><td>ポストバック経由でインストールやアプリ内イベントのリアルタイム情報を受け取れません</td></tr><tr><td>自社からのトラフィックに対して、アプリ内イベントポストバックの設定が可能です\*</td><td>トラフィックをもたらす一部のパートナーへのアプリ内イベントポストバックを設定可能です\*</td></tr><tr><td colspan="2">\* マーケターの許可が必要です</td></tr></tbody></table>

</Accordion>

## 代理店アカウント-キャンペーンとレポート

<div id="agency-setting-up-campaigns" />

<Accordion title="代理店：キャンペーンの設定">

代理店は以下の主要なトラフィックタイプを測定できます。

* * [セルフレポーティング広告ネットワーク（SRN）](/docs/about-agency-accounts#セルフレポーティング広告ネットワーク)
  * [非SRN（アトリビューションリンクを使用する広告ネットワーク）](/docs/about-agency-accounts#非srn)

### セルフレポーティング広告ネットワーク

Meta広告、Google広告、X広告などのセルフレポーティングネットワークは、外部アトリビューションリンクを使用しません。代わりに、各ネットワークには独自のメソッドとAPIがあり、AppsFlyerはそれらを活用して新規インストールやアプリ内イベントなどを伝達します。

#### SRN 構成

| SRN | マーケターが初期SRN設定を実行します | 詳細 |
| --- | --- | --- |
| Apple Search Ads | はい | Apple Search Adsキャンペーンの代理店設定の詳細については、<Anchor target="_blank" href="/marketers/ja/docs/apple-ads-integration-setup#代理店とマーケティングパートナーの設定">こちら</Anchor>をクリック。 |
| Google広告 | はい | Google広告キャンペーンの代理店設定の詳細については、<Anchor target="_blank" href="/marketers/ja/docs/google-ads-adwords-integration-setup-for-agencies">こちら</Anchor>をクリック。 |
| Googleマーケティングプラットフォーム (GMP) | いいえ | GMPには異なる2つのAPIがあります。<Anchor target="_blank" href="/marketers/ja/docs/google-marketing-platform-display-video-360-dv360-integration#comparing-the-legacy-and-new-integrations">二つの違い</Anchor>について詳細はこちら、自分に関連する方を選択してください。 |
| Meta広告  <br />と  <br />X広告 | はい | **注:** このセクションは、Meta広告についてです。Facebookソーシャル（投稿）のアトリビューションについては、[オウンドメディア](/docs/about-agency-accounts#owned-media%E2%80%94onelink-and-custom-links)をご覧ください。<br /><br /><strong>Meta広告とX広告のすべてのキャンペーンは、代理店アカウント名の後に「\_」を付ける必要があります。</strong>その名前はAppsFlyerプラットフォームで定義されます。<br />正しく命名されていないキャンペーンは、マーケターには表示されますが、代理店アカウントには表示されません。<br /><br />**注:**<ul><li>代理店名は大文字と小文字が区別されます。</li><li>代理店向けの<Anchor target="_blank" href="/marketers/ja/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta広告</Anchor>および<Anchor target="_blank" href="/marketers/ja/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X広告</Anchor>の設定の詳細については、こちらをご覧ください。</li><li>これに関してご質問がある場合は、[agency@appsflyer.com](mailto:agency@appsflyer.com)までお問い合わせください。</li></ul>**例**<br />agencyxは、agencyx\_brilliantcampaignというMeta広告キャンペーンを運営しており、これを見ることができます。<br /><br />agencyzは、AgencyZ\_whathaveidonewrongというX広告キャンペーンを運営していますが、結果が表示されません。これは、キャンペーンの代理店名の部分が、定義された代理店名（大文字のAとZ）と異なるために起こります。 |
| Snapchat | いいえ | Snapchatキャンペーンの代理店設定の詳細については、<Anchor target="_blank" href="/marketers/ja/docs/snapchat-advanced-srn-integration-setup">こちら</Anchor>をクリック。 |
| TikTok for Business | はい | TikTok for Businessキャンペーンの代理店設定の詳細については、<Anchor target="_blank" href="/marketers/ja/docs/tiktok-for-business-advanced-srn-integration-setup#代理店向けtiktok-for-businessとの連携">こちら</Anchor>をクリック。 |
| ヤフー（Oath：広告プラットフォーム／Yahoo Gemini) | はい | Yahooキャンペーンの代理店設定の詳細については、<Anchor target="_blank" href="/marketers/ja/docs/yahoo-integration-setup#agency-configuration">こちらをクリック</Anchor>してください。 |

### 非SRN

SRNとは異なり、大多数のアドネットワークはアトリビューションリンクをアトリビューション目的で使用します。<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#attribution-link-tab">これらのアトリビューションリンクは、AppsFlyerの各ネットワーク設定ですでに提供されており</Anchor>、そこから直接コピーできます。

代理店の場合、そのプロセスはマーケターとほぼ同じです。通常のアドネットワークのセットアップ期間にアクセスすると、アトリビューションリンクがすでに表示されています。唯一の違いは、`af_prt`パラメータがアトリビューションリンクに自動的に追加されることです。

#### アドネットワーク設定の可視性

アドネットワークの設定は、マーケター（アプリの所有者）が設定するときにのみ、アドネットワークに表示されます。代理店がアドネットワーク連携を有効化して設定すると、ネットワークはこのセクションを非アクティブと見なします。

#### af\_prtパラメータ

`af_prt`パラメータの値は代理店名です。代理店名が`af_prt`パラメータで渡されると、小文字に変換されます。

`af_prt`に代理店名が含まれると、新しいインストールを代理店アカウントにアトリビュートさせることができます。そうでない場合は、新規インストールがアドネットワークに直接アトリビュートされます。

[altagency-af-prt.pngalt](https://support.appsflyer.com/hc/article_attachments/30629262900241)

**マーケターから受け取ったリンクを使用しないでください**。誤ったアトリビューションを防ぐため、必ず自分のアカウントからのリンクを使用してください。

#### 特別なケース：全インストールネットワークと全起動ネットワーク

一部の非SRNでは、マーケターが**自分にアトリビュートされていないデバイスのポストバックを送信することを求めたり、許可したりします。**

全インストールネットワーク

ネットワークは、どのソースであっても、新しいアプリインストールごとにポストバックを受け入れます。

全起動ネットワーク

ネットワークは、どのソースでもアプリの新規起動ごとにポストバックを受け入れます。

全インストールネットワークの例としては、Vungle、Wechat、Startapp、Unity Adsなどがあります。

以下の表に、すべてのネットワーク起動の完全なリストが示されています。

| ネットワーク名 | ネットワーク PID（AppsFlyerのアトリビューションリンク上） |
| --- | --- |
| Supersonicads（ironSourceのレガシーネットワーク） | supersonicads\_int |
| Adelphic リマーケティング | adelphicremarketing\_int |
| Grow モバイル | growmobile\_int |
| ONE by AOL | advertising.com\_int |
| Lemmonet モバイル | lemmonetmobile\_int |
| Clickky | clickky\_int |
| Remerge | remerge\_int |
| MyThings | mythings\_int |
| TikTok for Business | bytedanceglobal\_int |

#### すべてのインストール／起動ネットワークでの代理店のアトリビューション設定方法

これらのネットワークを利用するには、代理店によらないインストールから情報を送信する必要があります。そのため、これらのネットワークは、マーケターが**代理店**より先に設定する必要があります。

> 📄 **例**
>
> Tapjoyの代理店アトリビューション設定例を使って説明します：
>
> 1. マーケターは、マーケター管理画面のTapjoyセットアップ期間に進みます。
> 2. マーケターは、**マーケター**にTapjoyから提供されたTapjoyアプリIDを**app\_id**テキストフィールドに入力します。
> 3. [**統合**]タブ > [デフォルトのポストバック]で、マーケターは[**オーガニックを含むすべてのメディアソース**]を選択します。
> 4. 代理店は、代理店管理画面のTapjoyセットアップ期間に進みます。
> 5. 代理店は、**代理店**にTapjoyから付与されたTapjoyアプリIDを**app\_id**テキストフィールドに入力します。

### ディープリンク

ディープリンクとは、パーソナライズされたコンテンツを開いたり、ユーザーをアプリ内の特定のアクティビティに送信したりしてモバイルアプリを起動することです。これにより、あなたのユーザーに優れた体験を提供し、エンゲージメントを高めることができます。

ディープリンクを機能させるためには、モバイルアプリがディープリンクの機能とインフラストラクチャを持って開発されていることが必要です。キャンペーンを設定する前に、アプリ所有者にアプリがディープリンクに適しているかどうか確認してください。

### リターゲティング

* * <Anchor target="_blank" href="/marketers/ja/docs/retargeting-attribution-guide">リターゲティングアトリビューション</Anchor>を利用すると、キャンペーンで既存または過去のユーザーをターゲットにすることができます。リターゲティングキャンペーンを正常に機能させるためには、ディープリンク機能が必要とされることが多いです。

### アプリ内イベント

アプリ所有者は、アプリ内でさまざまなイベント（例: 購入、チュートリアルの視聴、レベルクリアなど）を発生させ、それをAppsFlyerで記録して分析できます。代理店は、自分のアカウントの[イベント]ページで、自社に紐づくイベントデータを確認できます。

#### アプリ内イベントポストバック

代理店は、マーケターからの許可を得ることで、<Anchor target="_blank" href="/marketers/ja/docs/in-app-event-postback-configuration">アプリ内イベントポストバック</Anchor>（<Anchor target="_blank" href="/marketers/ja/docs/measure-sessions">af\_app\_openedイベント</Anchor>を含む）を広告ネットワークに設定する権限を持つことができます。

代理店は、広告ネットワークにアプリ内のポストバックを設定する権限を与えることができます。 <Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#代理店の許可">許可は代理店の許可タブでマーケターによって付与されます</Anchor>。

</Accordion>

<div id="reporting-for-agencies" />

<Accordion title="代理店向けレポーティング">

* トラフィック統計は、AppsFlyer管理画面から直接表示およびダウンロードできます。
* レポートは、AppsFlyer管理画面の[<Anchor target="_blank" href="/marketers/ja/docs/raw-data-reporting-overview">データのエクスポート</Anchor>]ページからアクセスできます。<Anchor target="_blank" href="/partners/ja/docs/data-locker-reports-for-agencies">Data Locker</Anchor>経由でコホートレポートにもアクセスできます。
* 利用可能なレポートタイプは次の通りです。
  * 集計
  * ローデータ
* マーケターと代理店は、ほとんどの場合、管理画面やレポートで同じデータにアクセスすることはできません。
* 代理店は通常、マーケターのトラフィックの一部のみを担当しているため、データへのアクセスはマーケターに比べて制限されています。
* <Anchor target="_blank" href="/marketers/ja/docs/manage-data-access-permissions">この記事</Anchor>では、これらの違いについて詳しく説明しています。以下のセクションでは、これらを強調しています。

> 📘 **注意**
>
> Meta広告とX広告の利用規約により、第三者とみなされる**代理店**は、**Meta広告またはX広告から発生するトラフィックのローデータレポートにアクセスできません**。

### 集計データへのアクセス

* パフォーマンスレポート（集計データレポートとも呼ばれます）は、代理店アカウントでデフォルトで利用できます。 関連記事:<Anchor target="_blank" href="/marketers/ja/docs/aggregated-and-analytics-reporting-overview">集計パフォーマンスレポート</Anchor>
* 集計オーガニックデータレポートにアクセスするには、マーケターの<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#代理店の許可">許可</Anchor>が必要です。
* 代理店はリテンションレポート、コホートレポート、Protect360管理画面にアクセスできます。これには、マーケターが<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#代理店の許可">**リテンションとコホートレポートへのアクセスを許可する**</Anchor> または<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#代理店の許可">**Protect360ダッシュボードへのアクセスを許可する**</Anchor>を有効にする必要があります。[**アクティブ統合**]の[**権限**]タブでそれぞれのアクセス許可を有効にする必要があります。

### ローデータへのアクセス

<Anchor target="_blank" href="/marketers/ja/docs/raw-data-reporting-overview">ローデータレポート</Anchor>（ユーザーレベルのデータレポート）にはアトリビューション情報が含まれており、トピックに分かれています。

### タイムゾーンと通貨

代理店はアプリで定義されたタイムゾーンと通貨でアプリを表示しますが、これらの設定を変更できるのはマーケターのみです。

### コストレポーティング

代理店は、<Anchor target="_blank" href="/marketers/ja/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">コストデータをサポートする</Anchor>統合パートナーを構成する際、**コストデータの取得**を有効にできます。

**コストデータの取得を有効にするには:**

1. AppsFlyerのサイドメニューから、**コラボレーション** > **アクティブ統合**を選択します。
2. コストでパートナーをフィルタリングします:**[アクティブ統合]** ページの上部から、[**サポートされている機能**] > [**コスト**]を選択します。
3. パートナーを選択してください。[**統合**]タブに移動します。[**コスト** タブに移動] を選んでください。
4. [**コストデータを取得**] をオンにしてください。
5. このパートナーのAPIキーを入力してください。
6. [**保存**] をクリックしてください。

#### コストデータのアクセスと表示

コストデータは次のデータソースにおいて代理店へ提供されます。

* **概要**ページ: コストデータは、概要ページ内の**集計パフォーマンスレポート**に表示されます。
* **レポート**: コストデータは、**ローデータレポート**の**インストール**や、**パフォーマンスレポート**内の<strong>パートナー（メディアソース）</strong>などのエクスポートレポートで利用可能です。

### ハイブリッドアカウントのデータアクセス

ハイブリッドアカウントは、一部のアプリを代理店（アプリパートナー）として、他の一部をマーケター（アプリオーナー）として管理する代理店アカウントです。

以下のアカウントレベルの機能は利用が制限されています。

* <Anchor target="_blank" href="/marketers/ja/docs/custom-dashboards">カスタム管理画面</Anchor>は、代理店およびハイブリッドアカウントでは使用できません。
* コホートレポート: マーケターの許可を得て利用可能です。
* Protect360: マーケターの許可を得て利用可能です。

ハイブリッドアカウントをお持ちの場合、管理画面に表示はされても、開こうとすると404エラーが発生します。

これらの機能を利用したい場合は、新しいMarketerアカウントを開設し、Marketerアプリと代理店アプリを分けることをお勧めします。上記の機能は、有効に設定がされている場合、Marketerアカウントで利用が可能です。

</Accordion>

<div data-zendesk-anchors="about-agency-accounts=%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HDNYNZYR2FTMQ71EV2AY3A3A=%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 agency-access-to-marketer-data=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E3%83%9E%E3%83%BC%E3%82%B1%E3%82%BF%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HDNYNZYRZKK97GZ6R0MB9RQN=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E3%83%9E%E3%83%BC%E3%82%B1%E3%82%BF%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 agency-access-to-ad-network-integrations=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E7%B5%B1%E5%90%88%E3%81%B8%E3%81%AE%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01J00RYT8J0MBPHTGK5T4WEE43=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E7%B5%B1%E5%90%88%E3%81%B8%E3%81%AE%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HJR00RGQX0CQEHDS9BHBGJD4=%E6%B3%A8%E8%A8%98 agency-transparency=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E9%80%8F%E6%98%8E%E6%80%A7 h_01HDNYNZYRYHJ98YQWVVENZ07P=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E9%80%8F%E6%98%8E%E6%80%A7 comparing-different-types-of-accounts=%E7%95%B0%E3%81%AA%E3%82%8B%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E3%82%BF%E3%82%A4%E3%83%97%E3%81%AE%E6%AF%94%E8%BC%83 h_01HDNYNZYR65409AGM9F2PZRC8=%E7%95%B0%E3%81%AA%E3%82%8B%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E3%82%BF%E3%82%A4%E3%83%97%E3%81%AE%E6%AF%94%E8%BC%83 h_01HDNYNZYS7A2H60EEAJ114VSM=agency-versus-marketer-accounts differences-between-marketer-and-agency-accounts=%E3%83%9E%E3%83%BC%E3%82%B1%E3%82%BF%E3%83%BC%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A8%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E9%81%95%E3%81%84 h_01HDNYNZYSS7WSQ07S7KRADN7Z=%E3%83%9E%E3%83%BC%E3%82%B1%E3%82%BF%E3%83%BC%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A8%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E9%81%95%E3%81%84 features-available-to-agencies=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%8C%E5%88%A9%E7%94%A8%E3%81%A7%E3%81%8D%E3%82%8B%E6%A9%9F%E8%83%BD h_01HDNYNZYSX4WPQKS0H6JN6FCP=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%8C%E5%88%A9%E7%94%A8%E3%81%A7%E3%81%8D%E3%82%8B%E6%A9%9F%E8%83%BD h_01HDNYNZYS8KRSPM5CPVJEJ74Y=agency-vs-ad-network-account differences-between-ad-network-and-agency-accounts=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%A8%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E9%81%95%E3%81%84 h_01HDNYNZYS4VPZMY34WA3SG5JT=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%A8%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E9%81%95%E3%81%84 agency-accounts%E2%80%94campaigns-and-reporting=%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88-%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E3%81%A8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HDNYNZYS32SNR5F0WKJ4G9Q1=%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88-%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E3%81%A8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HDNYNZYSNF2RQ3E7PM4HK433=agency-setting-up-campaigns selfreporting-ad-networks=%E3%82%BB%E3%83%AB%E3%83%95%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E5%BA%83%E5%91%8A%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF h_01HDNYNZYS8X1VA4T46DQYQZFE=%E3%82%BB%E3%83%AB%E3%83%95%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E5%BA%83%E5%91%8A%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF srn-configurations=srn-%E6%A7%8B%E6%88%90 h_01HDNYNZYS8AM2MFPRXFA4JXNS=srn-%E6%A7%8B%E6%88%90 h_01HDNYNZYSFXZXR99T6ME2R43F=%E4%BE%8B nonsrns=%E9%9D%9Esrn h_01HDNYNZYSN28VZQKCBRGXAVY0=%E9%9D%9Esrn ad-network-configuration-visibility=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E8%A8%AD%E5%AE%9A%E3%81%AE%E5%8F%AF%E8%A6%96%E6%80%A7 h_01HDNYNZYSG5MQDDKV55HF4X9C=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E8%A8%AD%E5%AE%9A%E3%81%AE%E5%8F%AF%E8%A6%96%E6%80%A7 af_prt-parameter=af_prt%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF h_01HDNYNZYSC7XNJCJ1F27KTM9Z=af_prt%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF special-case-allinstalls-and-alllaunches-networks=%E7%89%B9%E5%88%A5%E3%81%AA%E3%82%B1%E3%83%BC%E3%82%B9%E5%85%A8%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%A8%E5%85%A8%E8%B5%B7%E5%8B%95%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF h_01HDNYNZYSB4MKXD47E1VHDN62=%E7%89%B9%E5%88%A5%E3%81%AA%E3%82%B1%E3%83%BC%E3%82%B9%E5%85%A8%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%A8%E5%85%A8%E8%B5%B7%E5%8B%95%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF how-to-setup-agency-attribution-with-all-installslaunches-networks=%E3%81%99%E3%81%B9%E3%81%A6%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E8%B5%B7%E5%8B%95%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%A7%E3%81%AE%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E8%A8%AD%E5%AE%9A%E6%96%B9%E6%B3%95 h_01HDNYNZYSHNV2B27JQV4EEVFM=%E3%81%99%E3%81%B9%E3%81%A6%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E8%B5%B7%E5%8B%95%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%A7%E3%81%AE%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E8%A8%AD%E5%AE%9A%E6%96%B9%E6%B3%95 h_01HDNYNZYS5WYADGW24AVK9RCZ=%E4%BE%8B deep-linking=%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%AA%E3%83%B3%E3%82%AF h_01HDNYNZYS5W0SMCF1YC6C3G4C=%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%AA%E3%83%B3%E3%82%AF retargeting=%E3%83%AA%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 h_01HDNYNZYS3Z7RE51M7G7386VZ=%E3%83%AA%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 inapp-events=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88 h_01HDNYNZYTDFN4MB6QBEQ8P5XW=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88 inapp-event-postbacks=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01HMDP38S3NPE5R4QZJ5CW404W=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01HDNYNZYTA767NGSTNECTBCV2=reporting-for-agencies h_01HDNYNZYTYBWGMY2PP8MPQE2F=%E6%B3%A8%E6%84%8F access-to-performance-reports=%E9%9B%86%E8%A8%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HDNYNZYTDH4S38XG3JCZQYJJ=%E9%9B%86%E8%A8%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 access-to-raw-data=%E3%83%AD%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HDNYNZYT4ZKBNGDR3QR1VTEZ=%E3%83%AD%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 time-zone-and-currency=%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BE%E3%83%BC%E3%83%B3%E3%81%A8%E9%80%9A%E8%B2%A8 h_01HDNYNZYT97ET1TQHKSRDMWDC=%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BE%E3%83%BC%E3%83%B3%E3%81%A8%E9%80%9A%E8%B2%A8 cost-reporting=%E3%82%B3%E3%82%B9%E3%83%88%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 h_01HDNYNZYTYT9NHMHQQ77PK8CQ=%E3%82%B3%E3%82%B9%E3%83%88%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 accessing-and-viewing-cost-data=%E3%82%B3%E3%82%B9%E3%83%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%A8%E8%A1%A8%E7%A4%BA h_01HDNYNZYTWB5WVYY8C347G1ME=%E3%82%B3%E3%82%B9%E3%83%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%A8%E8%A1%A8%E7%A4%BA hybrid-account-data-access=%E3%83%8F%E3%82%A4%E3%83%96%E3%83%AA%E3%83%83%E3%83%89%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HDNYNZYTKZTCBSBKZEJ7M0JN=%E3%83%8F%E3%82%A4%E3%83%96%E3%83%AA%E3%83%83%E3%83%89%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9" />
