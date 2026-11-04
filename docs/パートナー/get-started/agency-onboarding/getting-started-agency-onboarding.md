---
title: 代理店アカウント：入門
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
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
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2026-10-14T09:32:31Z'
  id: 360002381617
  locale: ja
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/ja/articles/360002381617
---
> **概要：概要：代理店アカウントの設定を行うことで、広告主の代わりにキャンペーンの計測設定を行なうことが可能です。**

<Embed title="代理店アカウント：入門" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/54qzpj1lm7" providerUrl="https://fast.wistia.com" />

<div id="appsflyer-attribution-model" />

## AppsFlyerの計測モデル

まずはじめに、AppsFlyerでの計測がどのように働いているのかを理解する必要があります。このセクションでは、最初のクリックまたはインプレッションからインストール / イベントの紐付けに至るまでの過程で何が起こるかを説明します。

[![ua-agency-flow.png](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)

1. マーケティング担当者、またはマーケティング担当者の代わりに代理店が、AppsFlyerの計測リンクを使用して特定のアドネットワークでキャンペーンを設定。
2. ユーザーがそれらの広告 (例: バナーやリンク)をクリック。
3. 広告の裏側に設置されているAppsFlyerの計測リンクが、クリック時に必要な情報とともに発火。AppsFlyerはそれらの情報を計測リンクから取得し、データベースへ格納。
4. ユーザーはアプリストアへリダイレクト。
5. ユーザーはアプリをインストールして、初めてアプリを起動。アプリがインストールされた端末のデータと一緒に、アプリ内のAppsFlyer SDKがサーバーと通信。
6. AppsFlyerの <Anchor target="_blank" href="/marketers/ja/docs/appsflyer-attribution-model">計測メソッド</Anchor>を使用して、このデータをクリックデータベースを照合。
7. データがマッチすれば、そのクリックにインストールを紐付け、マッチしなければオーガニックインストールに紐付け。
8. 一度インストールが計測されると、広告主と代理店両方の管理画面とレポート(<Anchor target="_blank" href="/partners/ja/docs/about-agency-accounts#セルフレポーティング広告ネットワーク">Meta広告 と Twitterは例外あり</Anchor>)に表示。
9. 最後に、今後の配信最適化のためなどに情報を利用できるアドネットワークに対して、コンバージョンデータをポストバック。

<div id="agency-role-in-mobile-attribution-chain" />

## モバイル計測における代理店の役割

アプリを所有しているマーケティング担当者は、マーケティングの成果を測るためにAppsFlyerのSDKをアプリに実装します。

一部のアプリ所有者は、広告代理店を雇って広告キャンペーンを実施することを選択しています。そのためには、代理店は予めAppsFlyerの代理店アカウントを持っている必要があり、マーケティング担当者はその代理店に対して <Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#代理店の許可">自社アプリへの代理店権限</Anchor>を付与すべきです。

したがって、代理店は技術的にはアプリを所有せず、SDK実装などの技術的な部分に関与することなく、連携しているマーケティングチャネルでのみアプリを宣伝します。マーケティング担当者によって与えられた権限の種類に応じて、代理店はさまざまな機能を利用できます。

インストールが代理店によって出稿された広告に起因する場合、代理店の管理画面に表示されます。広告主側の管理画面にもそれが表示され、代理店に起因していることがわかります。

注：広告代理店自体がアプリを所有している場合、またはアプリの開発も担当している場合には、マーケティング担当者アカウントを開設することをお勧めします。

<div id="pricing" />

## 料金

代理店アカウントの機能 の範囲は、各アプリの所有者(広告主)によって提供される権限に依存します。したがって、代理店アカウントは**無料**で提供され、アプリ所有者(広告主)のみに対して計測における費用が発生します。アプリの所有者と代理店は、AppsFlyerのデータを相互補完的に利用することが可能です。

<div id="getting-started" />

## はじめよう

新しい代理店アカウントを設定するには：

1. <Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">登録フォーム</Anchor>に記入してください。
   * 会社のメールドメインを使用して登録してください。
   * 既存のAppsFlyerアカウントに関連付けられていない、新しいメールアドレスを使用してください。
2. AppsFlyerの代理店チームの担当者から、登録を完了するために必要な詳細情報を連絡する場合があります。
3. アカウントがアクティブになると通知が届き、AppsFlyerを使用できるようになります。

<div id="adding-team-members" />

## チームメンバーの追加

アカウントが立ち上がったら、アカウントアドミン（アカウントを開いた人）がチームメンバーを追加でき、広告主から権限付与されているアプリの一部、もしくはすべてのアプリへのアクセスを付与することができます。新しいチームメンバーの追加方法の詳細については、こちらを参照してください。

<div id="adding-apps-to-your-account" />

## 代理店アカウント上にアプリを表示させる

アカウントを最初に作成したときには、紐付けられているアプリはありません。

![agency-start.png](https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png)

どの代理店アカウントも、まずはアプリ所有者からの権限付与が必要です。

* アプリの管理画面へのアクセス権限をもらう
* 設定を変更する
* キャンペーンを出稿する

マーケティング担当者は、直接管理画面上から<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#代理店の許可">各代理店アカウントに対して権限を付与</Anchor>できます。代理店アカウントを設定し、アプリへのアクセス権を取得したら、AppsFlyer機能を使用してキャンペーンの設定・配信を開始できます。

<div id="note" />

<div id="what-does-it-mean-to-get-permission-from-a-marketer" />

### マーケティング担当者からの権限を得るとはどういうことですか

マーケティング担当者から権限を得た場合：

* アプリが代理店アカウント内に表示されます。
* そのアプリと広告ネットワークとの計測連携を設定できます（アプリ所有者による設定が必要な、Facebook、Twitterなどの一部媒体を除く）。
* キャンペーンで使用する計測リンクを作成できます。
* パートナーとのコスト連携を設定できます。（連携可能な場合）
* アプリのデータを見ることができます。
* アドネットワークとそのチームメンバーに対して、アプリの基本情報を閲覧する権限を付与できます。  
  つまり、代理店と広告主がアドネットワークを使用している場合、アドネットワークのチームメンバーの権限を編集して、アプリのダッシュボードを表示したり、お互いに加えられた変更を確認したりできます。新しいアドネットワークのチームメンバーが追加されていたり、削除していないチームメンバーが表示されない場合には、広告主側で追加または削除した可能性があります。

その他の権限には、コホート/リテンションレポート、Protect360の管理画面、および集約パフォーマンスレポートへのオーガニックデータへの表示が含まれます。

<div id="app-list" />

### アプリ一覧

マーケティング担当者から権限を得ると、アプリがアプリページに表示されます。

アプリページには、最大1000個までのアプリが表示されます。アプリのリストが1000を超えた場合、一部のアプリはリストに表示されなくなりますが、検索機能を使用してそれらを見つけることが可能です。

![agency-apps.png](https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png)

<div id="searching-for-apps" />

#### アプリの検索

1. アカウントで、トップメニューから **マイアプリ**を選択します。
2. 検索欄に、以下項目のどれかを入力してください。
   * アプリ名
   * App ID
   * アプリ所有者のAdminアカウントのメールアドレス

### 運用媒体の開示

業界がより透明性の高いエコシステムへ移行する中、AppsFlyerは広告主と代理店の間での運用媒体の開示機能を提供しており、AppsFlyerのレポートと分析機能を最大限に活用することを可能にしています。

注記：

<div id="agency-dashboard" />

## 代理店管理画面

アプリ一覧にあるアプリをクリックして、 <Anchor target="_blank" href="/marketers/ja/docs/getting-started-with-appsflyer-dashboards">管理画面</Anchor>にアクセスしてください。広告出稿を開始すると、あなた代理店アカウントに紐付いた集計データがここに表示されます。

![agency-dashboard.png](https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png)

代理店アカウントの管理画面には、デフォルトで以下権限が含まれています。

* ライフタイム価値概要管理画面
* アプリ内イベント管理画面
* リターゲティング管理画面

<div id="running-campaigns" />

## 広告出稿

<div id="self-reporting-networks-srns" />

### セルフレポーティングネットワーク（SRN）

SRNは、セルフアトリビューションネットワーク（SAN）とも呼ばれ、クリックやその他のデータをレポートするためにAppsFlyerの計測リンクを必要とせず、代わりにAppsFlyerとのAPI連携を使用するネットワークです。これらのネットワークは、<Anchor target="_blank" href="/marketers/ja/docs/meta-ads-faq#attributing-agencies-with-facebook">Facebook</Anchor>、<Anchor target="_blank" href="/marketers/ja/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">Twitter</Anchor>、<Anchor target="_blank" href="/marketers/ja/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads</Anchor>、<Anchor target="_blank" href="/marketers/ja/docs/snapchat-advanced-srn-integration-setup">Snapchat</Anchor>、DoubleClick、<Anchor target="_blank" href="/marketers/ja/docs/apple-ads-integration-setup">Apple Ads Search</Anchor>、<Anchor target="_blank" href="/marketers/ja/docs/yahoo-integration-setup">Yahoo</Anchor>、<Anchor target="_blank" href="/marketers/ja/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">Yahoo! JAPAN（検索広告）</Anchor> です。日本

これらのネットワークの大部分は、代理店側でも追加の対応が必要です。例えば、FacebookやTwitterとの連携はアプリ所有者(広告主)のみが設定することができ、出稿する際はキャンペーン名の冒頭に指定された代理店識別子を付与する必要があります。そうすることで、それらのインストールを代理店アカウントに紐付けることが可能になります。

上記のリンクをクリックして、各ネットワークのガイドと代理店設定の具体的な手順を確認してください。

<div id="non-srns" />

### 非SRN

ほとんどの広告ネットワークは、出稿の際広告の裏に設置される計測リンクが必要です。詳細については、<Anchor target="_blank" href="/partners/ja/docs/about-agency-accounts#非srn">こちら</Anchor>を参照してください。


<span id="sandbox-attribution-agency-campaigns"></span>AppleのSKAdNetworkの計測プロセスに代理店は含まれておらず、AppsFlyerは代理店を直接成果を紐づけることはできませんが、AppsFlyerではSKAdNetworkで配信されている代理店のキャンペーンを代理店アカウントへ紐付け計測データを提供することができます。

<div id="campaign-naming" />

#### キャンペーンの命名規則

* あなたの代理店アカウントの af\_prt (<Anchor target="_blank" href="/partners/ja/docs/about-agency-accounts#af_prtパラメータ">af\_prt の詳細と見つけ方</Anchor>)
* \_ (アンダーバー)
* キャンペーン名

たとえば af\_prt の値がAgencyXの場合、キャンペーン名は以下のようになります：

`AgencyX_SummerSale`

<div id="skadnetwork-agency-campaigns" />

### SKAdNetworkの代理店データ

AppleのiOSの一部であるSKAdNetworkは、マーケティング担当者がIDFAなどの広告IDを使わずにキャンペーンの良し悪しを計測可能なものです。AppleのSKAdNetworkの計測プロセスに代理店は含まれておらず、AppsFlyerは代理店を直接成果を紐づけることはできませんが、AppsFlyerではSKAdNetworkで配信されている代理店のキャンペーンを代理店アカウントへ紐付け計測データを提供することができます。

<div id="campaign-naming-1" />

#### キャンペーンの命名規則

AppsFlyerのSKAdNetworkの管理画面においてデータを確認できるようにするには、SKAdNetworkで配信するキャンペーン名に代理店識別子を追加し、以下のように構成する必要があります：

* あなたの代理店アカウントの af\_prt (<Anchor target="_blank" href="/partners/ja/docs/about-agency-accounts#af_prtパラメータ">af\_prt の詳細と見つけ方</Anchor>)
* \_ (アンダーバー)
* キャンペーン名

たとえば af\_prt の値がAgencyXの場合、キャンペーン名は以下のようになります：

`AgencyX_SummerSale`

<div id="note-2" />

<div id="note-1" />

> 📘 **注**
>
> * SKAdNetworkで計測された代理店のキャンペーンは常にマーケティング担当者に対して開示された状態であり、キャンペーンを配信しているアドネットワーク名はマーケティング担当者に対してマスクされません。iOS 15 以降では、マーケティング担当者(アプリの所有者)が<Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">オプトインしてポストバックのコピーを直接受け取る</Anchor>ことができることを考慮ください。
> * これは、ユーザー インターフェイスでアクセスできるパートナーのアクティブ化設定に追加されます。

<div id="access-to-skan-conversion-studio" />

#### SKAN Conversion Studioへのアクセス

広告代理店は<Anchor target="_blank" href="/marketers/ja/docs/skan-conversion-studio#view-cv-mapping">Conversion Studio</Anchor>でマーケティング担当者のSKAN CVマッピングの設定を<Anchor target="_blank" href="/marketers/ja/docs/skan-conversion-studio#skan-conversion-studioの基本">閲覧およびダウンロード</Anchor>できますが、設定を作成または編集することはできません。

<div id="skadnetwork-dashboard" />

#### SKAdNetworkの管理画面

<Embed title="代理店アカウント：入門" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**参考記事：**

* <Anchor target="_blank" href="/marketers/ja/docs/about-att-and-skan">SKAdNetworkクイックスタートガイド</Anchor>
* <Anchor target="_blank" href="/marketers/ja/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAdNetworkの管理画面</Anchor>
* <Anchor target="_blank" href="/marketers/ja/docs/skadnetwork-skan-solution-guide">SKAdNetwork ソリューション</Anchor>

<div id="single-source-of-truth-ssot-for-agencies" />

### 代理店向け Single Source of Truth (SSOT)

SSOTは、異なるモデルのアトリビューションデータを組み合わせて、重複するインストールと、関連する費用と収益に関連する指標を削除することで、すべてのアトリビューション方法を統一します。これにより、例えば eCPI、ROI、ROASなどが正しく計算されます。

代理店はオーバービュー管理画面のSSOTデータにアクセスできますが、API経由ではできません。

オーバービュー管理画面にSSOTフラグを含めるためには、マーケティング担当者がConversion Studio にてSSOTをオンにする必要があります。

**参考記事：**

* <Anchor target="_blank" href="/marketers/ja/docs/single-source-of-truth-ssot-guide-for-ios-attribution">SSOT (Single Source of Truth) - iOS計測ガイド</Anchor>

<div id="what-else-you-can-do" />

## 他にできること

* ユーザーの継続率を計測する
* アプリ内イベントを使用してキャンペーンを最適化する
* <Anchor target="_blank" href="/marketers/ja/docs/retargeting-attribution-guide">リターゲティング</Anchor>キャンペーンを実行する
* <Anchor target="_blank" href="/marketers/ja/docs/manage-data-access-permissions">データ</Anchor>をエクスポートする
* <Anchor target="_blank" href="/marketers/ja/docs/registering-test-devices">テスト端末の登録</Anchor>
* その他多数。

より発展的な代理店アカウントの利用に関する詳細は、<Anchor target="_blank" href="/partners/ja/docs/about-agency-accounts#agency-setting-up-campaigns">こちら</Anchor>をご覧ください。

なじみのない用語がありますか？その場合には<Anchor target="_blank" href="/marketers/ja/docs/appsflyer-knowledge-base-glossary">用語集</Anchor>を確認してみてください。

緊急の技術的な / エンジニア寄りの質問がありますか？そんなときにはまずヘルプセンター内で検索してみてください。それでも見つかれなかった場合には、管理画面右上からサポートチームに連絡してください。

<div data-zendesk-anchors="appsflyer-attribution-model=appsflyer%E3%81%AE%E8%A8%88%E6%B8%AC%E3%83%A2%E3%83%87%E3%83%AB h_01HFXXKCMW7EREMC7KEYTF3ERH=appsflyer%E3%81%AE%E8%A8%88%E6%B8%AC%E3%83%A2%E3%83%87%E3%83%AB agency-role-in-mobile-attribution-chain=%E3%83%A2%E3%83%90%E3%82%A4%E3%83%AB%E8%A8%88%E6%B8%AC%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E5%BD%B9%E5%89%B2 h_01HFXXKCMW987FV2PB4EPXH92Z=%E3%83%A2%E3%83%90%E3%82%A4%E3%83%AB%E8%A8%88%E6%B8%AC%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%AE%E5%BD%B9%E5%89%B2 pricing=%E6%96%99%E9%87%91 h_01HFXXKCMWPN6AN98A5RD5YXW7=%E6%96%99%E9%87%91 getting-started=%E3%81%AF%E3%81%98%E3%82%81%E3%82%88%E3%81%86 h_01HFXXKCMWRXVBYTW9RYEX7X8F=%E3%81%AF%E3%81%98%E3%82%81%E3%82%88%E3%81%86 adding-team-members=%E3%83%81%E3%83%BC%E3%83%A0%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%AE%E8%BF%BD%E5%8A%A0 h_01HFXXKCMWB6ZG3PSHDSETC4XC=%E3%83%81%E3%83%BC%E3%83%A0%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%AE%E8%BF%BD%E5%8A%A0 adding-apps-to-your-account=%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E4%B8%8A%E3%81%AB%E3%82%A2%E3%83%97%E3%83%AA%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%95%E3%81%9B%E3%82%8B h_01HFXXKCMWBZVTHAEKED1Q27M3=%E4%BB%A3%E7%90%86%E5%BA%97%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E4%B8%8A%E3%81%AB%E3%82%A2%E3%83%97%E3%83%AA%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%95%E3%81%9B%E3%82%8B what-does-it-mean-to-get-permission-from-a-marketer=%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E6%8B%85%E5%BD%93%E8%80%85%E3%81%8B%E3%82%89%E3%81%AE%E6%A8%A9%E9%99%90%E3%82%92%E5%BE%97%E3%82%8B%E3%81%A8%E3%81%AF%E3%81%A9%E3%81%86%E3%81%84%E3%81%86%E3%81%93%E3%81%A8%E3%81%A7%E3%81%99%E3%81%8B h_01HFXXKCMWYNNZWTKP9KEQ4VCD=%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E6%8B%85%E5%BD%93%E8%80%85%E3%81%8B%E3%82%89%E3%81%AE%E6%A8%A9%E9%99%90%E3%82%92%E5%BE%97%E3%82%8B%E3%81%A8%E3%81%AF%E3%81%A9%E3%81%86%E3%81%84%E3%81%86%E3%81%93%E3%81%A8%E3%81%A7%E3%81%99%E3%81%8B app-list=%E3%82%A2%E3%83%97%E3%83%AA%E4%B8%80%E8%A6%A7 h_01HFXXKCMWKW78TMC76F40PY2C=%E3%82%A2%E3%83%97%E3%83%AA%E4%B8%80%E8%A6%A7 searching-for-apps=%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E6%A4%9C%E7%B4%A2 h_01HFXXKCMW8S93N577393QZTYX=%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E6%A4%9C%E7%B4%A2 transparency=%E9%81%8B%E7%94%A8%E5%AA%92%E4%BD%93%E3%81%AE%E9%96%8B%E7%A4%BA h_01HFXXKCMW5YC2APNGHNV6B35C=%E9%81%8B%E7%94%A8%E5%AA%92%E4%BD%93%E3%81%AE%E9%96%8B%E7%A4%BA agency-dashboard=%E4%BB%A3%E7%90%86%E5%BA%97%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 h_01HFXXKCMWPZVADY15DKATJ7Z4=%E4%BB%A3%E7%90%86%E5%BA%97%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 running-campaigns=%E5%BA%83%E5%91%8A%E5%87%BA%E7%A8%BF h_01HFXXKCMWFB9RXY7AVBX5CGB9=%E5%BA%83%E5%91%8A%E5%87%BA%E7%A8%BF selfreporting-networks-srns=%E3%82%BB%E3%83%AB%E3%83%95%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AFsrn h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=%E3%82%BB%E3%83%AB%E3%83%95%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AFsrn nonsrns=%E9%9D%9Esrn h_01HFXXKCMWPAMZ373D5AVD5EJF=%E9%9D%9Esrn h_01J6PCDYM2W1X6EMMEE7SFB3VE=sandbox-attribution-agency-campaigns campaign-naming=%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E3%81%AE%E5%91%BD%E5%90%8D%E8%A6%8F%E5%89%87 h_01HFXXKCMWMW1AHXMS19CYD4VC=%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E3%81%AE%E5%91%BD%E5%90%8D%E8%A6%8F%E5%89%87 h_01HFXXKCMWEQ41A7TZ2K6DE424=%E6%B3%A8 skadnetwork-agency-campaigns=skadnetwork%E3%81%AE%E4%BB%A3%E7%90%86%E5%BA%97%E3%83%87%E3%83%BC%E3%82%BF h_01HFXXKCMWZ19E0QR1VE977BTS=skadnetwork%E3%81%AE%E4%BB%A3%E7%90%86%E5%BA%97%E3%83%87%E3%83%BC%E3%82%BF 01J6PCG6JGY2R8T5DDCR8APM66=%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E3%81%AE%E5%91%BD%E5%90%8D%E8%A6%8F%E5%89%87-1 01J6PCG6JHK9TGX93SD4DRP393=%E6%B3%A8 access-to-skan-conversion-studio=skan-conversion-studio%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HFXXKCMWX53HMRG2ZTD9FYQE=skan-conversion-studio%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 skadnetwork-dashboard=skadnetwork%E3%81%AE%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 h_01HFXXKCMW1HHMSS3XAXJKME29=skadnetwork%E3%81%AE%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 single-source-of-truth-ssot-for-agencies=%E4%BB%A3%E7%90%86%E5%BA%97%E5%90%91%E3%81%91-single-source-of-truth-ssot h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=%E4%BB%A3%E7%90%86%E5%BA%97%E5%90%91%E3%81%91-single-source-of-truth-ssot what-else-you-can-do=%E4%BB%96%E3%81%AB%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8 h_01HFXXKCMXQ2JT63GBMC74PWBA=%E4%BB%96%E3%81%AB%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8" />
