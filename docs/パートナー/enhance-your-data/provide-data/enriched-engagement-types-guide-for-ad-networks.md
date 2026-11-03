---
title: 拡張エンゲージメントタイプガイド：アドネットワーク向け
metadata:
  keywords:
    - Advertisers
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2024-10-15T10:54:29Z'
  edited_at: '2026-10-14T09:38:52Z'
  id: 29221265052433
  locale: ja
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ja/articles/29221265052433
---
> **概要：** このページでは、ユーザーのエンゲージメントの全体像を反映し、正確かつ効果的なキャンペーン最適化を実現するための、拡張エンゲージメントタイプ（EET）の計測リンクの作成方法について説明しています。

拡張エンゲージメントタイプ（EET）は、広告を閲覧または操作した際のユーザーのエンゲージメントや意図の度合いを、瞬間的な露出からダイレクトレスポンスまで幅広く反映します。本記事では、ユーザーが広告とどのように接触したかに応じて、パートナーが AppsFlyer の計測リンクでエンゲージメントタイプをどのようにレポートすべきかを解説します。

> ❗️ **免責事項**
>
> 本記事は、パートナー向けのEETの仕様を説明しています。EET の概要や詳細については、<Anchor target="_blank" href="/marketers/ja/docs/about-enriched-engagement-types#which-ad-networks-report-enriched-engagement-types">拡張エンゲージメントタイプ</Anchor> の記事をご参照ください。

## EETに対応している広告媒体

拡張エンゲージメントタイプを利用する広告媒体は、AppsFlyer パートナープログラムにおける Premier、Advance、Engageの基準を満たしている必要があります。これらのレベルは、広告主に対して大規模かつ一貫して高品質なトラフィックを提供してきた実績があり、透明性と信頼性の高い形でエンゲージメントデータを送信し、AppsFlyer の幅広いサービスと統合されているネットワークを指します。

> 📘 **注意**
>
> エンゲージビューとエンゲージクリックのレポートの開始を検討したい場合には、担当PDMまでお問い合わせください。

また、EETをレポートする資格のあるネットワーク一覧もご参照ください。

> ❗️ **要注意**
>
> 許可されていない広告媒体からの、`af_engagement_type` パラメータを含むクリックとインプレッションのレポートは拒否され、計測には使用されなくなるのでご注意ください。

<div id="engaged-click-or-engaged-view-attribution-flow" />

<Accordion title="エンゲージクリック・エンゲージビューの計測フロー">

以下は、広告の表示から、エンゲージクリックまたはエンゲージビューを通じたインストールイベントの、最終的なアトリビューションまでの一連の流れです。

1. アドネットワークが広告を表示します。
2. アドネットワークが、指定された `af_ad_tran_id` を含むインプレッションを AppsFlyer に送信します。
3. ユーザーが広告とエンゲージします。
4. アドネットワークが、`af_engagement_type`、 `af_ad_tran_id`、 `af_ad_format`、 `af_ad_type`（および任意で `viewability`のパラメータ）を含むクリックまたはインプレッションを送信します。
5. AppsFlyer が、エンゲージクリックまたはエンゲージビューとインストールイベントを紐付けます。
6. AppsFlyer が、アドネットワークにインストールイベントの成果を紐づけます。

</Accordion>

<div id="parameters-for-reporting-engagement-types-in-attribution-links" />

<Accordion title="計測リンクでエンゲージメントタイプをレポートするためのパラメータ">

ネットワークは、以下のパラメータを計測リンクに含めることで、エンゲージメントタイプをレポートできます。

* `af_engagement_type`：エンゲージメントのタイプ（例：`engaged_click`、 `click_to_app`、`engaged_view`）。詳細は<Anchor target="_blank" href="/marketers/ja/docs/about-enriched-engagement-types#拡張エンゲージメントタイプとは">各エンゲージメントタイプの一覧と説明</Anchor>を参照してください。
* `af_ad_type`：広告の種類。（例：`rewarded_video`、`interstitial`、`banner`）詳細は<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#af_ad_type">各広告タイプの一覧と説明</Anchor>を参照してください。
* `af_ad_format`：広告フォーマット。（例：`text`、`image`、`video`、`playable`）詳細は<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#af_ad_format">各広告フォーマットの一覧と説明</Anchor>を参照してください。
* `viewability`：（任意）広告エンゲージメントに関する追加情報。（例：`af_video_total_length`、`af_ad_time_viewed`、`af_audio_played_length`）詳細は<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#ビューアビリティのパラメータ">ビューアビリティに関する項目一覧と説明</Anchor>を参照してください。
* `af_ad_tran_id`：直前のインプレッションと紐付けることで、AppsFlyerがエンゲージクリックやエンゲージビューを検証するためのトランザクション ID。
* `is_skoverlay=true` もしくは `is_autostore=true`：[SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) または Android Auto Inline Installs によって発生したエンゲージビューを識別するするパラメータです。

**エンゲージクリックのURLサンプル**

```http HTTPS
https://app.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_click&af_ad_type=interstitial&af_ad_format=playable&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0
```

**エンゲージビューのURLサンプル**

```http
https://impression.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_view&af_ad_type=interstitial&af_ad_format=video&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0&af_video_total_length=20&af_video_played_length=15
```

</Accordion>

<div id="user-engagements-to-report-as-engaged-clicks" />

<Accordion title="エンゲージクリックとしてレポートすべき広告接触">

*エンゲージクリック*とは、アプリストアへリダイレクトされたりアプリが起動されたりすることなく、同一コンテキスト内で広告とのインタラクションが継続されるクリックを指します。

以下は、アドネットワークが `af_engagement_type=engaged_click` としてレポートしてもよい広告接触の例です：

* **プレイアブル広告：** ミニゲームをプレイするための画面タップや、インタラクティブコンテンツを再生するための画面タップ。
* **ソーシャルでのエンゲージメント：** SNS 上で広告にいいね、コメント、シェアを行うための画面タップ。
* **リダイレクト：** ランディングページや外部コンテンツなど、ストアページ以外へ遷移した際の画面タップ。
* **ダイナミックな商品広告 / カタログまたはカルーセル**商品をスワイプして閲覧する画面操作。
* **ウィッシュリスト追加：** アプリ内または外部サイトで広告表示された商品をお気に入りに追加した際の画面タップ。
* **後で見る：広告やその内容を後で見るために保存した場合の画面タップ。**
* **ブックマークやコレクションへの追加：** 広告をブックマークまたはコレクションに追加した際の画面タップ。広告に再度アクセスしたりする意図がユーザーにあることを示します。
* **広告のミュート解除：** オーディオを有効にするための画面タップ。

**エンゲージクリックとしてレポートすべきではない広告接触**

以下は、`engaged_click`として**レポートすべきでない**広告接触の例です。

* **広告の非表示：** 「×」ボタンなどで広告を閉じるための画面タップ。ユーザーがそれ以上その広告に関心がないことを示します。
* **広告のスキップ：** 広告をスキップして次のコンテンツへ進むための画面タップ。その広告がユーザーにとって魅力も関連性も持っていないことを示します。
* **広告の報告：** 不適切・誤解を招くなどの理由で広告を報告した際の画面タップ。
* **オプトアウト／配信停止：** 今後同様の広告を受け取らない選択した際の画面タップ。
* **広告からの退出：** 別の画面へ遷移するために、広告体験を終了した際の画面タップ。
* **広告をミュート：** 動画広告の音をミュートするための画面タップ。

</Accordion>

<div id="user-engagements-to-report-as-engaged-views" />

<Accordion title="エンゲージビューとしてレポートすべき広告接触">

以下は、アドネットワークが `af_engagement_type=engaged_view` としてレポートしてもよい広告接触の例です：

* **スキップ可能な動画広告：** スキップ可能になった後、5 秒以上動画広告が視聴された場合。視聴秒数を測定できない場合は以下を適用します：
  * 動画が 20 秒超の場合：50%以上視聴の時点で `engaged_view` を送信
  * 動画が 20 秒未満の場合：完全視聴の時点で `engaged_view` を送信
  * `af_ad_format` のパラメータの値は、`video` または `playable` を送信する必要があります。
* **リワード広告：** ユーザーがリワード動画を最後まで視聴した場合。`af_ad_type`のパラメータの値は、`rewarded_video` を送信する必要があります。
* **StoreKitによる広告の自動表示：** StoreKitによる広告表示（[`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay)や[`SKStore`](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)）や AndroidのAuto Inline Installs に対するタップは、パブリッシャーではなく Apple によってSKAN計測のために記録されます。AndroidのAuto Inline Installs（autostore）についても同様です。

  これらのケースでは、アドネットワークはユーザーが実際に広告にエンゲージしたかどうかを判別できないため、エンゲージメントが発生していなくても、広告表示時にインプレッションまたはクリックをレポートすることがあります。

  広告が表示された時点で `click_to_app` をレポートすることも可能ですが、非常に高い CTR になってしまうリスクがあります。（Android の Auto Inline Installs も同様です。）

  このリスクを軽減するため、AppsFlyerでは `engaged_view` のレポートを推奨しています。その場合、計測リンクには iOS では `is_skoverlay=true`、Android では `is_autostore=true` を含める必要があります。

**エンゲージビューとしてレポートすべきではない広告接触**

以下は、`engaged_view`として**レポートするべきではなく**、`view`としてレポートすべき広告接触の例です。

* リワード動画ではなく、`SKOverlay` または `autostore` によるオーバーレイ表示もされていない、**スキップ不可の動画広告**を視聴した場合。

</Accordion>

<div id="01JCAT81K2EJNH91YS6NJGMXMB-data-title" />

<Accordion title="EETをレポートする資格のあるアドネットワーク">

このネットワーク一覧には、AppsFlyer が拡張エンゲージメントタイプのイベントを処理可能なパートナーが記載されています。（ただし、デフォルトではエンゲージビューとエンゲージクリックは除外されています）この一覧に含まれているアドネットワークで、エンゲージクリックおよびエンゲージビューの処理を希望する場合は、AppsFlyerの担当PDMまでお問い合わせください。既にエンゲージクリックとビューを処理されているネットワークについて知りたい場合は、<Anchor target="_blank" href="/marketers/ja/docs/about-enriched-engagement-types#エンゲージビューとエンゲージクリックを報告できるアドネットワーク">EETの広告主向けのヘルプページ</Anchor>を参照してください。

> ❗️ **注意**
>
> 許可されていない広告媒体からの、`af_engagement_type` パラメータを含むクリックとインプレッションのレポートは拒否され、計測には使用されなくなるのでご注意ください。

| パートナー名 |
| --- |
| AdColony |
| AdAction |
| Adaction3 |
| Adikteev |
| adjoe GmbH |
| Amazon |
| Amazon DSP |
| AppLovin |
| Appier |
| Appnext |
| Apple Search Ads |
| Aura from Unity |
| AWIN |
| Bidease |
| ByteDance Ads China |
| Cauly |
| Criteo |
| Digital Turbine |
| Digital Turbine On Device |
| Fluent |
| Glance |
| Google Ads (Adwords) |
| Google Marketing Platform (DV360/CM360) |
| Hotstar |
| Huawei |
| InMobi DSP |
| ironSource |
| Jampp |
| Josh |
| Kakao |
| Kuaishou |
| Liftoff |
| LINE |
| Meta Ads |
| Mintegral |
| Mistplay |
| Motorola プリインストール |
| Naver |
| Oppo |
| OPPO Global |
| OPPO Store Traffic（グローバル） |
| OPPOPAI プリインストール |
| PayTM |
| Rakuten |
| Reddit |
| Remerge |
| RevX |
| Samsung |
| Smadex |
| Snapchat |
| Stackadapt |
| Tapjoy |
| Tencent AMS |
| TikTok for Business - アドバンスSRN |
| TikTok For Business - 旧連携 |
| The Trade Desk |
| Transsion |
| Treasure Data |
| Truecaller |
| Unity Ads |
| Vivo プリロード |
| vivo Global |
| Vungle |
| X Ads（旧：Twitter Ads） |
| Xiaomi Global |
| XiaomiPAI プリインストール |
| Yahoo Japan |
| Yandex |
| YouAppi |

</Accordion>

<div data-zendesk-anchors="01JA7WZH43ECDKRC0R0J89ED1E=%E5%85%8D%E8%B2%AC%E4%BA%8B%E9%A0%85 which-networks-can-report-eet-to-appsflyer=eet%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E5%BA%83%E5%91%8A%E5%AA%92%E4%BD%93 h_01JJPVYGWZSFSATZ4TH5VBSVXW=eet%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E5%BA%83%E5%91%8A%E5%AA%92%E4%BD%93 01JAN5JRM56C6S6EP27WFJ2Y4W=%E6%B3%A8%E6%84%8F h_01J00XFV133YYAB7YPQNXM5R37=%E8%A6%81%E6%B3%A8%E6%84%8F 01JA7WZH46RJBG996NG9EZV7T9=engaged-click-or-engaged-view-attribution-flow 01JA7WZH4BZVGS9Z1NNHQC72N6=parameters-for-reporting-engagement-types-in-attribution-links 01JA7WZH4JDJFCVT25WJ4GNE20=user-engagements-to-report-as-engaged-clicks 01JA7WZH4Q32TEWM5EKME142R7=user-engagements-to-report-as-engaged-views 01JCAT81K2EJNH91YS6NJGMXMB%20data-title%3D=01JCAT81K2EJNH91YS6NJGMXMB-data-title allowed-network-list=01JCAT81K2EJNH91YS6NJGMXMB-data-title h_01JJPVYGWZ4T6TPFRWTR2AB027=%E6%B3%A8%E6%84%8F-1" />
