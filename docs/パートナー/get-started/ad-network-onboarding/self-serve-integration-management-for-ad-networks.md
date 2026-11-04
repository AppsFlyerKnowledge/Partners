---
title: セルフサービスの連携設定画面：アドネットワーク向け
metadata:
  keywords:
    - postbacks
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
  created_at: '2021-03-15T10:03:41Z'
  edited_at: '2026-10-14T09:38:33Z'
  id: 360018512658
  locale: ja
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ja/articles/360018512658
---
> **概要**：概要：このページでは、AppsFlyerの管理画面上から連携設定のセットアップや編集を行う方法について記載しています。

<Embed title="セルフサービスの連携設定画面：アドネットワーク向け" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/9kvwrhnzjo" providerUrl="https://fast.wistia.com" />

**前提条件：**

* 計測リンクやポストバックの設定を確認、編集するには、まずはAppsFlyerの管理画面にログインできるパートナーアカウントのIDが必要になります。<Anchor target="_blank" href="/partners/ja/docs/getting-started-onboarding-guide-for-ad-networks">連携済みパートナーへの登録とパートナーアカウントを作成</Anchor>するには、AppsFlyerの<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#appsflyerに新しいパートナーを招待する">広告主から紹介</Anchor>してもらう必要があります。
* 計測リンクとデフォルトポストバックの管理機能は、2022年2月1日以降に登録されたパートナーに対してのみ提供されています。
* 以下の仕様に従って、ご自身のアドネットワークのサーバーがAppsFlyerからのポストバックを受け取れる状態にあることを確認してください：
  * エンドポイントとの通信を確実にするために、自社のファイアウォールとセキュリティシステムにて、AppsFlyerサーバーの<Anchor target="_blank" href="/marketers/ja/docs/appsflyer-server-ip-address-ranges-allowlisting">IPアドレス</Anchor>を許可リストに追加してください。
  * TLS バージョン
  * ポート2024-02-26

<div id="accessing-integration-management" />

## 連携管理へのアクセス

1. AppsFlyerのパートナーアカウント(Admin)でログインしてください。
2. 上段右のメールアドレスをクリックし、ドロップダウンメニューから**ポストバック管理**を選択してください。

<div id="attribution-link" />

## 計測リンク

もっともシンプルな例は、計測リンクを広告の裏側に設定しておいて、ユーザーが広告をクリックした際に計測リンクもクリックされたことになるというものです。

計測リンクの設定完了はアドネットワークとしての連携設定において、必ず必要ですのでご注意ください。

**計測リンクを設定するには：**

1. **計測リンク**のタブで、あなたの計測リンクに含めるパラメータを追加してください：
   * パラメータ名
   * **あなたのマクロ：** パラメータへ値を渡すアドネットワーク側のマクロを追加してください。
   * **追加：** リンクにそのパラメータを追加する場合には、チェックを入れてください。

   <div id="important" />

   > 🚧 **重要！**
   >
   > * キャンペーンパフォーマンスに関するデータをより豊富にするために、キャンペーンや広告関連のパラメータを可能な限り追加してください。
   > * **Site ID**は連携において必須のパラメータです。
   > * 広告主は、この計測リンクを特定アプリにおける連携の基盤として利用しており、広告主自身で追加のパラメータを追加することも可能です。
   > * AppID、ルックバック期間、アドネットワークのIDは自動的に計測リンクに追加されるので、このテンプレート上では追加する必要はありません。

2. **[任意]** AppsFlyerで提供していないパラメータも、カスタムパラメータとして追加可能です。(マクロのご用意はないので、固定値のみ送信可能です。)
3. 最後に、プレビューを確認して、正しく設定されていることを確認してください。
4. **保存**をクリックしてください。

より詳細は、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">計測リンクの構造とパラメータの詳細</Anchor>を参照してください。

<div id="default-postback" />

## デフォルトポストバック

ポストバックは、AppsFlyerによって生成されたマクロを含むURLで、それぞれの値が変換後にリアルタイムのアドネットワークのサーバーに送信されます（ご自身のアドネットワーク上、もしくは他社のアドネットワーク上で発生したものなど、連携設定に依り異なります。）

**デフォルトポストバックを設定するには：**

1. AppsFlyerからのポストバックを受け取る**エンドポイントのアドレス**を入力してください。インストール、アプリ内イベントでそれぞれ、もしくは両方に対応するURLを入力してください。連携を有効にするには、少なくともインストールのポストバックURLを設定する必要があります。
2. ポストバックにパラメータを追加してください：
   * パラメータ名
   * **受け取り側のパラメータ名**：御社側で値を受け取る際のパラメータ名
   * **パラメータの値**(いくつかのパラメータで利用可能)：値のフォーマットを選択してください。例）boolean値の場合、"true"/"false" と 1/0、どちらで受け取るのかを選択してください。
   * **Install**: インストールのポストバックに含めたいパラメータにチェックを入れてください。
   * **In-app event**: アプリ内イベントのポストバックに含めたいパラメータにチェックを入れてください。

   <Anchor target="_blank" href="/partners/ja/docs/postback-macros-for-ad-networks">ポストバックマクロの全一覧</Anchor>

   <div id="important-1" />

   > 🚧 **重要！**
   >
   > * * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`  
   >     **注記：**

4. 最後に、ポストバックテンプレートのプレビューを確認して、全て正しく設定されていることを確認してください。
5. **保存**をクリックしてください。

<Anchor target="_blank" href="/marketers/ja/docs/in-app-event-postback-configuration">ポストバックの詳細とそのサンプルについても参照してください。</Anchor>

<div id="advanced-privacy-and-skan-postbacks" />

## 高プライバシーとSKANのポストバック

高プライバシーとSKANのポストバックは、計測リンクとデフォルトのポストバックの設定が完了した後にのみ、設定することが可能です。

**ポストバック管理の画面を操作するには：**

1. ポストバックのタイプを選択してください：
   * <Anchor target="_blank" href="/partners/ja/docs/advanced-privacy-guide-postback-macros-for-ad-networks">高プライバシーポストバック</Anchor>
   * <Anchor target="_blank" href="/partners/ja/docs/skan-integration-guide-for-ad-networks">SKAdNetworkのポストバック</Anchor>
2. トグルをONにして、設定画面をアクティブにしてください。
3. **[SKANのポストバック設定のみ]** SKAdNetwork IDを入力してください。これは必須項目であり、有効なIDでなければ連携設定を保存することはできません。
4. AppsFlyerからのポストバックを受け取る**エンドポイントのアドレス**を入力してください。インストール、アプリ内イベントでそれぞれ、もしくは両方に対応するURLを入力してください。
5. ポストバックパラメータを追加してください：
   * パラメータ名
   * 例）boolean値の場合、"true"/"false" と 1/0、どちらで受け取るのかを選択してください。
   * **インストール**：Install: インストールのポストバックに含めたいパラメータにチェックを入れてください。
   * **アプリ内イベント：** In-app event: アプリ内イベントのポストバックに含めたいパラメータにチェックを入れてください。

   <Anchor target="_blank" href="/partners/ja/docs/skan-integration-guide-for-ad-networks#appsflyerからのデータ受け取り">SKAdNetworkのポストバックマクロ一覧</Anchor>

   <Anchor target="_blank" href="/partners/ja/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification">高プライバシーポストバックのマクロ一覧</Anchor>

   <div id="important-2" />

   > 🚧 **重要！**
   >
   > * * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`

7. 最後に、ポストバックテンプレートのプレビューを確認して、全て正しく設定されていることを確認してください。
8. **保存**をクリックしてください。  
   設定を保存すると、その変更内容がすぐに適用・有効になるのでご注意ください。

<div data-zendesk-anchors="accessing-integration-management=%E9%80%A3%E6%90%BA%E7%AE%A1%E7%90%86%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01H9FCSTYR157CCJWTYSNE9JQ0=%E9%80%A3%E6%90%BA%E7%AE%A1%E7%90%86%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 attribution-link=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF h_01H9FCSTYR6HRSF9F8KCR4B3X7=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF h_01H9FCSTYR4Q1985DTHNE1M1CC=%E9%87%8D%E8%A6%81 default-postback=%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01H9FCSTYR2WX0M0ZW3B22EKBM=%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01H9FCSTYSEP367WAAKCFHZT58=%E9%87%8D%E8%A6%81-1 advanced-privacy-and-skan-postbacks=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%81%A8skan%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01H9FCSTYSRKBMYR2BYNQJJKVM=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%81%A8skan%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01H9FCSTYSEJD59AWCFNXDZMYW=%E9%87%8D%E8%A6%81-2" />
