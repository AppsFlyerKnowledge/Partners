---
title: CTVからモバイルアプリへのビュースルーアトリビューション（アドネットワーク向け）
metadata:
  keywords:
    - Attribution
    - Ad Networks
    - Partners
    - CTV
    - CTV Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roi-tamir
    - CTV Attribution
    - Ad Networks
  created_at: '2022-08-21T06:49:24Z'
  edited_at: '2026-10-15T17:36:53Z'
  id: 8528418936977
  locale: ja
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ja/articles/8528418936977
---
> **At a glance:** コネクテッドTV（CTV）端末で視聴された広告に、モバイルアプリのインストールを紐付けます。

<div id="ctv-to-mobile-app-attribution-for-ad-networks" />

## CTVからモバイルアプリへのアトリビューション（アドネットワーク向け）

AppsFlyerのクロスプラットフォーム向けインプレッションURLを使用すると、CTVに表示された広告にモバイルアプリのインストールを紐付けられます。同一世帯内の複数のインストールを、同じCTV広告のインプレッションに紐付けることができます。

<Image align="center" alt="CTVからモバイルアプリへのアトリビューションの流れを示す図" src="https://files.readme.io/401bcb083e1cc618794cb302668f7271cf825a5a6045ff10055e0164baf423a1-19774176963473.jpg" />

CTVからモバイルアプリへのビュースルーアトリビューションでは、<Anchor target="_blank" href="/marketers/ja/docs/set-up-cross-platform-links-for-multi-device-campaigns#setup">OneLinkのインプレッションURL</Anchor>を使用します。このURLは、広告主が作成したクロスプラットフォーム向けOneLinkテンプレート（テンプレートID付き）に基づいています。これにより、広告主は異なるプラットフォームの複数のアプリ（AndroidアプリとiOSアプリなど）を1つのURLにまとめられます。

ユーザーがCTVで広告を視聴した際に、インプレッションURLをリアルタイムでAppsFlyerに送信します。

URLの例：

```
https://impressions.onelink.me/{template_id}?pid=__media_source__&af_xplatform=true&af_xplatform_vt_lookback=24h&af_siteid=__CSITE__&c=__CAMPAIGN_NAME__&af_channel=__PLACEMENT__&af_c_id=__CAMPAIGN_ID__&af_adset=__AID_NAME__&af_adset_id=__AID__&af_ad=__CID_NAME__&af_ad_id=__CID__&af_source_platform=__source_platform__&af_source_device_category=__device_category__&af_ad_type=__CTYPE__&af_ip=__IP__&af_ua=__UA__&redirect=false
```

AppsFlyerは、コンバージョンが発生するたびにアドネットワークにポストバックを送信します。

> 📘 **Note**
>
> この機能を利用できるのは、指定されたパートナーのみです。ご希望の場合は、担当PDMまでお問い合わせください。

<Accordion title="CTVからモバイルへのアトリビューションの設定">

**広告主とCTVからモバイルアプリへのビュースルーアトリビューションを設定するには**：

1. <Anchor target="_blank" href="/partners/ja/docs/getting-started-onboarding-guide-for-ad-networks">AppsFlyerの連携済みパートナー</Anchor>であること、ポストバックが適切に設定されていること、およびAppsFlyerとの[CTVからモバイルアプリへの連携テスト](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#test-partner-integration)が完了していることを確認してください。
2. URLに[必須パラメータ](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#parameters)と、その他の必要なパラメータが含まれていることを確認してください。
3. ユーザーのIPアドレスとユーザーエージェントをAppsFlyerに送信してください。これらは、CTVからモバイルアプリへのビュースルーアトリビューションに必要です。次のいずれかの方法で送信できます。
   1. インプレッションURLの`af_ip`パラメータと`af_ua`パラメータで送信します。
   2. とをリクエストヘッダーのパラメータとして送信します。

</Accordion>

<Accordion title="パートナー連携のテスト">

**CTVからモバイルアプリへのビュースルーアトリビューションをテストするには**：

1. 次のテストアプリを使用してください：com.appsflyer.android.deviceid および id1192323960
2. AppsFlyerのパートナーソリューションチームに連絡し、テスト用URLを入手してください。<Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">パートナー管理画面</Anchor>にログインし、上部メニューの**ヘルプ** > **お問い合わせ**をクリックすると、チームに連絡できます。
   * URLの例：`https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false`
3. `pid`パラメータのパートナーIDが正しいことを確認してください。
4. `af_ip`パラメータにIPアドレスを入力してください。
5. `af_ua`パラメータにユーザーエージェントを入力してください。
6. PCのブラウザにURLを入力してください。
7. モバイル端末でアプリストアにアクセスし、アプリをダウンロードしてインストールした後、起動してください。
8. AppsFlyerに新規インストールが表示され、対応するポストバックが送信されます。インストールが表示されない場合やポストバックを受信できない場合は、パートナーソリューションチームにお問い合わせください。

</Accordion>

<Accordion title="パラメータ">

以下のパラメータは、広告主へのアトリビューションデータと計測結果の提供に使用されます。

| パラメータ | 必須 | 説明 |
| --- | --- | --- |
| template\_id | ✓ | <Anchor target="_blank" href="/marketers/ja/docs/create-a-onelink-template">OneLinkテンプレート</Anchor>のIDです。テンプレートには、広告主のアプリに関する基本的な予測設定が含まれており、他のリンクを作成する際の基盤となります。注意：`template_id`の値は絶対にエンコードしないでください。 |
| pid | ✓ | 広告を配信するメディアソース（アドネットワーク）にAppsFlyerが割り当てるパートナー識別子です。 |
| af\_xplatform | ✓ | <ul><li>広告主が設定し、リンクがクロスプラットフォームアトリビューションに対応するかどうかを指定します。</li><li>値：true/false</li></ul> |
| af\_xplatform\_vt\_lookback | - | インプレッションの発生後、アプリのインストールをそのインプレッションに紐付けられる時間数を指定する期間です。任意に設定できます。設定可能なパラメータ値：1h～72h（1～72時間）。デフォルトは24hです。 |
| af\_ip | ✓ | <ul><li>広告を表示するCTV端末のIPアドレスです。</li><li>IPアドレスをURLで送信しない場合は、必ずリクエストヘッダーで送信してください。AppsFlyerがCTVからモバイルアプリへのアトリビューションを行うために必要です。</li></ul> |
| af\_ua | ✓ | <ul><li>広告を表示するCTV端末のユーザーエージェントです。</li><li>ユーザーエージェントをURLで送信しない場合は、必ずリクエストヘッダーで送信してください。AppsFlyerがCTVからモバイルアプリへのアトリビューションを行うために必要です。</li></ul> |
| af\_source\_platform | - | <ul><li>インプレッションが発生した端末のOSを表す値を、以下のリストから指定します。</li><li>値：<ul><li>android</li><li>ios</li><li>tizen</li><li>webos</li><li>smartcast</li><li>roku</li><li>windowsphone</li><li>vidaa</li><li>PlayStation</li><li>website</li></ul></li></ul> |
| af\_source\_device\_category | - | <ul><li>インプレッションが発生した端末の種類を表す値を、以下のリストから指定します。<ul><li>tv</li><li>mobile\_phone</li><li>desktop</li><li>tablet</li><li>set\_top\_box</li><li>games\_console</li><li>unknown\_device\_category</li><li>media\_player</li></ul></li></ul> |

URLに追加できるその他のパラメータについては、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">アトリビューションリンクの構造とパラメータの記事</Anchor>を参照してください。

</Accordion>

<Accordion title="特性と制限事項">

| 特性 | 説明 |
| --- | --- |
| アトリビューション期間 | ルックバック期間を指定する`af_xplatform_vt_lookback`パラメータの値に応じて、1～72時間です。 |
| リターゲティング | <ul><li>リアトリビューション：異なるプラットフォームからモバイルへのアトリビューションに対応しています。その他のプラットフォームには対応していません。</li><li>リエンゲージメント：非対応</li></ul> |
| アトリビューション方法 | 確率論的モデリング（IPアドレス）を使用したビュースルーアトリビューション |
| 世帯単位のアトリビューション | 対応しています。同一世帯内の複数のインストールを、同じCTV広告のインプレッションに紐付けられます。 |
| パートナー連携のテスト | モバイルアプリ間の不正が高い割合で発生していると判定されたアドネットワーク、または同様の判定を受けた他のメディアソースと提携しているアドネットワークは利用できません。 |

</Accordion>

<div data-zendesk-anchors="ctvtomobile-app-attribution-for-ad-networks=ctv%E3%81%8B%E3%82%89%E3%83%A2%E3%83%90%E3%82%A4%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91 h_01HE2X91GTDTPKKFBRRYYFMHDW=ctv%E3%81%8B%E3%82%89%E3%83%A2%E3%83%90%E3%82%A4%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91" />
