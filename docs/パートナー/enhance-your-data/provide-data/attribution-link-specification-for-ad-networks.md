---
title: 計測リンクの仕様：アドネットワーク向け
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2021-12-06T10:31:00Z'
  edited_at: '2026-10-14T09:27:26Z'
  id: 4412938154513
  locale: ja
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ja/articles/4412938154513
---
> **概要：** 概要： AppsFlyerと連携しているアドネットワークは、このページの内容に従って計測リンクの設定を行ってください。

## 計測リンク：アドネットワーク向け

計測リンクは、ユーザーが広告をクリックすることで広告へエンゲージしたことをAppsFlyerへ通知するために使用するものです。もっともシンプルな例は、計測リンクを広告の裏側に設定しておいて、ユーザーが広告をクリックした際に計測リンクもクリックされたことになるというものです。

### 計測方法

このセクションでは、最初のクリックまたはインプレッションからインストール / イベントの紐付けに至るまでの過程で何が起こるかを説明しています。

[![appsflyer-attribution-model-for-partners.png](https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png)](https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png)

1. ユーザーがバナーやリンクをクリック。
2. そのバナーやリンクは、ユーザーをAppsFlyerの計測リンクへリダイレクトし、AppsFlyerの計測リンクには、このクリック中に収集された情報が入力される。
3. AppsFlyerはそれらの情報を計測リンクから取得し、データベースへ格納。
4. ユーザーはアプリをインストールしてアプリを初回起動。アプリがインストールされた端末のデータと一緒に、アプリ内のAppsFlyer SDKがサーバーと通信。
5. AppsFlyerの **計測メソッド**を使用して、このデータをクリックデータベースと照合。
   * ユーザーがリンクをクリックしてGoogle Play にリダイレクトされると、Google Playはユニークなリファラー IDを発行します。アプリのインストールが発生すると、AppsFlyerは端末からこのリファラーIDを収集します。そして、このIDをGooglePlay側の記録と照合します。
   * **デバイスIDのマッチング**  
     IDマッチング URLクリック時に収集された広告ID（iOS：IDFA / Android：GAID）と、インストール時にSDKが取得した端末の広告IDを照合します。
   * 確率論的モデリング

   すべての計測メソッドの詳細については、<Anchor target="_blank" href="/marketers/ja/docs/appsflyer-attribution-model">こちら</Anchor>を参照してください。

   クリックデータベースにて、リファラー、広告ID、確率論的モデリングのデータポイントの順にデータを探します。データがマッチすれば、そのクリックにインストールを紐付け、マッチしなければオーガニックインストールに紐付け。
6. インストールが計測されると、コンバージョンの詳細が含まれたポストバックがアドネットワークに送信されます。

この流れに沿って、計測リンクを利用してアドネットワークから情報を得て、ポストバックで情報を送り返しています。

> 📘 **注意**
>
> TUNE、CAKE、Affiseなどのサードパーティのパフォーマンスマーケティングツールを使用している場合は、<Anchor target="_blank" href="/partners/ja/docs/platforms-for-ad-networks">プラットフォーム向けのガイド</Anchor>を代わりに参照してください。

### 計測リンクのテンプレート

計測リンク（バナーの背後に設置されているリンク）は、次のように形になります。

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={clickid}&advertising_id={gaid}&af_siteid={affiliate_id}&af_cost_model=CPI&af_cost_value={cost_value}&af_cost_currency={currency}&c={Campaign}&af_ad_type={AdType}&af_adset={Adset}&af_ad={Ad}&is_incentivized={true\false}&expires={timestamp}&signature={signature}
```

リンクのこの部分はスタティックであり、アドネットワーク側では何も変更する必要はありません。

リンクの構造に関する解説：

* '='の後ろにある`{}内の値は、クリックが発生しAppsFlyerにデータが送信されるときにアドネットワーク側で値を入力する必要があるマクロです。テンプレートを作成する際には、{}`内の値を御社のマクロに置き換えてください。
* 御社側でのマクロの命名は、御社のシステムがそれらのマクロを実際の正しい値に置き換えることができるのでれば特に意味を持ちません。'='の記号の前のパラメータは、AppsFlyer側で使用するプレースホルダであるため、どのパラメータの値をあなたがAppsFlyerへ送信しているかが判別できます。
* AppsFlyerとの連携をご希望の場合には、計測リンクのテンプレートを御社側のマクロも記載した上でメールでご連絡ください。

クリック時に取得できた情報は、できる限り多くAppsFlyerへ共有してください。詳細は、 <Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#計測リンクのパラメータ">計測リンクパラメータの一覧</Anchor>をご覧ください。

#### 最低限推奨の計測リンクパラメータ

| パラメータ | 説明 |
| --- | --- |
| `&clickid={clickid}` | ClickID は、アドネットワーク上で発生した各クリックに対して割り振られるユニークなクリック識別子です。 |
| もしくは  <br />`&idfa={IDFA}` | クリックが行われた端末の広告ID（Android：GAID / iOS：IDFA）です。 |
| `&c={campaign}` | 広告主によって定義されたキャンペーン名です。 |
| `&af_siteid={publisher_id}` | クリックを生んだパブリッシャー(配信面)またはアフィリエイター毎に振られたパブリッシャー/アフィリエイトIDです。 |
| `&af_ad_type={search_text}` | 広告タイプです。  <br />search\_text  <br />banner  <br />interstitial  <br />video  <br />rewarded\_video  <br />playable  <br />sponsored\_content  <br />audio |
| `&af_adset={adsetid}` | 広告セットID。広告主かパブリッシャーにより設定。広告セットはキャンペーンと広告の間の階層の中間レベルです。<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#データの詳細度の階層">もっと見る</Anchor> |
| `&af_ad={ad_id}` | 広告名（<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters#データの詳細度の階層">詳細を参照</Anchor>）。広告主かパブリッシャーにより設定。 |
| `&is_incentivized={true}` | インセンティブキャンペーンなのか、またはそうではない(ノンインセンティブキャンペーン)なのかをtrue / false の値で返してください。 |
| `&af_cost_value={cost_value}` | コンバージョンのコストの値です。小数点以下4桁まで対応しています。  <br />"56"、"2.85"など、数値のみ設定可ですので注意してください。（必要に応じて小数点は使用可です） |
| `&af_cost_currency={currency}` | デフォルト値は7日です。  <br /><Anchor target="_blank" href="https://en.wikipedia.org/wiki/ISO_4217">通貨コードのリスト</Anchor> |
| `&expires={timestamp}` | アドネットワークがクリックを主張しなくなるUnixのタイムスタンプです。クリック洪水を防止するための、クリック署名の機能で使用します。<Anchor target="_blank" href="/partners/ja/docs/click-signing-for-ad-networks">詳細はこちら</Anchor> |
| `&signature={signature}` | クリックの検証と不正を防止するための、HMAC-SHA256形式の署名です。<Anchor target="_blank" href="/partners/ja/docs/click-signing-for-ad-networks">詳細はこちら</Anchor> |

<div data-zendesk-anchors="attribution-links-for-ad-networks=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91 01H8GPNM9XTR602BWRBQ5JV8DT=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E5%90%91%E3%81%91 attribution-model=%E8%A8%88%E6%B8%AC%E6%96%B9%E6%B3%95 01H8GPNM9XSKS66F02GZQKK8E8=%E8%A8%88%E6%B8%AC%E6%96%B9%E6%B3%95 01H8GPNM9XBCVVXZ5HFKQZQ79D=%E6%B3%A8%E6%84%8F attribution-link-template=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%81%AE%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 01H8GPNM9XS4JE8B1F6TJGKSBR=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%81%AE%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 recommended-minimum-attribution-link-parameters=%E6%9C%80%E4%BD%8E%E9%99%90%E6%8E%A8%E5%A5%A8%E3%81%AE%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF 01H8GPNM9XD0GASJ93PNDGMDE8=%E6%9C%80%E4%BD%8E%E9%99%90%E6%8E%A8%E5%A5%A8%E3%81%AE%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF" />
