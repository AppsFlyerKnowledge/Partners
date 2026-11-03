---
title: Data Lockerを使用したSSOTレポートの取得｜アドネットワーク向け
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2024-07-31T19:51:34Z'
  edited_at: '2026-10-14T09:32:23Z'
  id: 27168206416017
  locale: ja
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ja/articles/27168206416017
---
> **概要：** Data Locker経由で取得できるSSOTレポートでは、IDマッチングやSKANなどのさまざまな計測方法のデータを統合することで、アプリキャンペーンのパフォーマンスを統一的かつ正確に把握できます。  BIシステムにデータをロードする方法を提供し、精度の高いデータの取得が可能です。

> 📘 **注意**
>
> * アドネットワークへのデータ共有を可能にするには、予め広告主側で管理画面上から[権限を付与する](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions)必要があります。
> * SSOT Data Locker レポートには、アクティビティベースのデータではなく、LTVベースのデータが含まれています。つまり、アプリ内アクティビティやイベントアクティビティではなく、すべてのタッチポイントにおけるユーザーの生涯価値がデータに反映されます。

## Data Lockerとは

Data Lockerは、AWS、GCS、Snowflakeなどの主要なクラウドプラットフォームにデータを直接配信できる、AppsFlyerの提供するソリューションです。これにより、担当者はデータを社内のBIシステムに簡単に統合し、包括的な分析とレポートを作成できるようになります。詳細は<Anchor target="_blank" href="/partners/ja/docs/data-locker-for-partners">こちらのページ</Anchor>を参照してください。

## SSOT（Single Source of Truth）とは

SSOT（Single Source of Truth）は、IDマッチングやSKANなどのさまざまな計測手法のデータを重複なく統合することで、アプリキャンペーンのパフォーマンスを統一的かつ正確に把握できるようにする機能です。詳細は<Anchor target="_blank" href="/marketers/ja/docs/single-source-of-truth-ssot-guide-for-ios-attribution">こちらのページ</Anchor>を参照してください。

## Data LockerでのSSOTレポート取得の利点

SSOTレポートは、広告主が見ているパフォーマンスの計測や分析データと同じ目線でデータを分析することを可能にします。

* **正確で包括的なアトリビューションデータ提供：** SSOTは、さまざまな計測手法のデータを統合するロジックを持っており、複数の計測方法によって本来重複している可能性のあるインストールを、成果重複のない状態で可視化することを可能にします。そして、正確なデータでユーザーのインストール成果とその後のアプリ内での行動を捉えることができるようになります。
* **BIシステムへのデータの取り込み：** 集計データを社内のBIシステムに取り込みたい場合にも、効率的で正確な方法を提供しています。このデータには、すべてのディメンションと指標をカバーした、インストール、アプリ内イベント、収益データが含まれます。

<div id="setting-up-data-locker" />

<Accordion title="Data Lockerの設定">

以下の手順に従って、Data Lockerを設定してください。なお、設定変更を行った後、機能が有効になるまで最大3時間かかる場合があります。

**前提条件：**

以下のいずれかのストレージの作業手順を完了してください。

* <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>バケット
* <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>バケット
* [Beta] <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor> バケット
* <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor> データウェアハウス

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Data Lockerを設定するには：**

1. 所有している <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">AppsFlyerのパートナーアカウント</Anchor>で管理画面へログインしてください。
2. 管理画面内で以下に移動してください：
   * **広告媒体の場合**：**左メニューのReport**>**Data Locker**
   * マーケティングパートナーの場合： **アカウントメニュー**をクリックして、 **Data Locker**へ進んでください。
3. DataLockerのセットアップ手順のうち、ステップ3〜16に従って設定してください。

</Accordion>

<div id="permissions" />

<Accordion title="権限">

代理店アカウント経由で計測の連携設定がされている場合：代理店アカウントからはパートナーアカウントへ権限を付与することができないので、本件に関する権限付与の作業は、広告主へ依頼する必要があります。

**アドネットワークがSSOTデータを取得できるようにするには（広告主アカウント上）：**

1. AppsFlyerの管理画面に入り、左メニューの連携 > **連携済みパートナー**へ進んでください。
2. 対象のアドネットワークを検索して選択してください。
3. **連携設定** をクリックして、連携設定のページに移動してください。
4. ［連携］のタブで **パートナーを有効にする**のトグルが**ON**になっていることを確認してください。OFFの場合、SSOTデータは共有されないのでご注意ください。
5. **権限** のタブへ移動してください。
6. 広告媒体権限をONにし、追加で以下の各権限についてもONにしてください：
   * **集計コンバージョンデータへのアクセス**
   * **アプリ内イベントの集計データへのアクセス権限を付与する**
   * **収益データへのアクセス権限を付与する**
7. 最後に、右下の **権限を保存**のボタンをクリックしてください。
8. 上記対応後に、権限を付与したことをアドネットワークに伝えてください。
9. 複数アプリが対象の場合には、連携しているアプリ毎に同じ作業を繰り返してください。

</Accordion>

<div id="ssot-report-facts" />

<Accordion title="SSOTレポートの仕様">

| 仕様 | 詳細 |
| --- | --- |
| 利用できるレポート | 以下のレポートが利用可能です：<ul><li>ユーザー獲得：インストールや各イベントをユーザー獲得媒体へ紐付けたデータです。これには、リエンゲージメント期間中に発生したアプリ内イベントも含まれます。</li><li>リターゲティング：リターゲティング媒体へ各イベントを紐づけたデータです：<ul><li>リアトリビューション後に発生したアプリ内イベント</li><li>リエンゲージメント計測後、リエンゲージメント期間中に発生したアプリ内イベント</li></ul></li><li>統合：<Anchor target="_blank" href="/marketers/ja/docs/resolve-retargeting-double-attribution">AppsFlyerの重複計測ルール</Anchor>に従いながら、メインの成果の紐づけ先にのみイベントを紐づけたデータです。つまり、リエンゲージメント期間中に発生したアプリ内イベントは、元々アプリをインストールさせたユーザー獲得媒体ではなく、リターゲティング媒体へ紐づけられます。</li></ul> |
| レポート期間 | レポートには、インストール後最大7日間のコホートデータが表示されます。 |
| ディレクトリの構造 | ディレクトリのインストール日ごとに作成・整理されます。各インストール日のフォルダには、毎日作成される複数バージョンのデータが格納されます。各バージョンのデータには、そのインストール日における更新された累積データが反映されます。そのため、利用可能な一番新しいレポートバージョンのみを処理するようにしてください。<Anchor target="_blank" href="/marketers/ja/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#ディレクトリの構造">（詳細はこちら）</Anchor> |
| レポート構成 | レポートのスキーマ（ディメンションと指標を含む）は固定されており、変更できません。 |
| データに用いられるタイムゾーン | UTC |
| データ更新頻度 | <ul><li>毎日更新されます。</li><li>各指標は、日本時間午前9時（UTC時間 0:00）までのデータを用いて算出されます。言い換えれば、UTC時間ベースでその日の終わりまでのデータです。</li><li>SLA：新しいレポートは、翌日の日本時間午前01:00 (UTC 16:00)までに取得できるようになります。毎日、過去15日分のインストール日に新しいバージョンのレポートが作成されます。<Anchor target="_blank" href="/marketers/ja/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#report-folder-hierarchy">（詳細）</Anchor></li></ul> |

</Accordion>

## レポート構成

SSOTレポートは、ディメンションとメトリック(各指標)で構成されています。

指標には、アトリビューション、収益、イベントを実行したユニークユーザーのデータが含まれます。

<div id="field-formats" />

<Accordion title="各項目のフォーマット">

<Table>
  <thead>
    <tr>
      <th>
        フォーマット名
      </th>
      <th>
        説明
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        文字列 (String [n])
      </td>
      <td>
        文字列の最大長。通常、データの受信時に項目長の制限を強制しませんが、その後データが切り捨てられる可能性があります。
      </td>
    </tr>
    <tr>
      <td>
        時間文字列(Time String)
      </td>
      <td>
        以下のような形式で記録されます：

        ```
        yyyy-mm-dd hh:mm:ss.
        ```

        例：

        ```
        2019-09-17 00:09:25
        ```
      </td>
    </tr>
    <tr>
      <td>
        列挙型 (Enum [n])
      </td>
      <td>
        列挙型の項目には、特定の値のみが含まれます。たとえば、selected\_currencyは3文字であり、指定された通貨コードのみを含めることができます。
      </td>
    </tr>
    <tr>
      <td>
        タイムスタンプ(Timestamp)
      </td>
      <td>
        10桁のUNIXタイムスタンプが用いられます。例：  
        2020年8月4日 07:25 UTC は以下のように変換されます：

        ```
         "timestamp": "1596525944"
        ```
      </td>
    </tr>
    <tr>
      <td>
        ブーリアン型(Boolean)
      </td>
      <td>
        項目の値は、*TRUE* と*FALSE* のいずれかです。
      </td>
    </tr>
    <tr>
      <td>
        整数型(Integer)
      </td>
      <td>
        整数型(Integer)
      </td>
    </tr>
    <tr>
      <td>
        Float型(Float)
      </td>
      <td>
        浮動小数点数を表し、小数点を含む実数値が入ります。
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="dimensions" />

<Accordion title="ディメンション">

<Table>
  <thead>
    <tr>
      <th>
        フィールド名
      </th>
      <th>
        説明
      </th>
      <th>
        形式
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        af\_ad\_id
      </td>
      <td>
        広告単位のID（キャンペーン階層の情報です）
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_ad
      </td>
      <td>
        広告単位の名称
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_adset\_id
      </td>
      <td>
        広告セット単位のID（キャンペーン階層の情報です）
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_adset
      </td>
      <td>
        広告セット単位の名称
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        app\_id
      </td>
      <td>
        接頭辞のidを含んだ、広告主のアプリID
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        attribution\_method
      </td>
      <td>
        イベントの計測に使用されたメカニズム（例: AppsFlyer method、SKAdNetwork（SKAN）、Organicなど）
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        含まれる値：click / impression / null
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        campaign
      </td>
      <td>
        アドネットワークからAppsFlyerへレポートされたキャンペーン名
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_c\_id
      </td>
      <td>
        キャンペーンID
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        コンバージョン日からの経過日数（特定のコンバージョンのタイムスタンプではありません）。  
        ［ヒント］この値を使用して、リテンションや〇日後時点でのKPIなどを計算しましょう。
      </td>
      <td>
        int
      </td>
    </tr>
    <tr>
      <td>
        event\_name
      </td>
      <td>
        イベントを特定します。特定の意味を持つイベント名もあれば、アプリ内で広告主が設定したアプリ内イベントに関連するイベント名もあります。

        | event\_name | 計測内容 |
        | --- | --- |
        | af\_conversion | ユーザーによるコンバージョンイベントです。conversion\_typeの項目で、それがインストール(install)、再ダウンロード(re-download)、リアトリビューション(re-attribution)、リエンゲージメント(re-engagement)のどれであるかを確認してください） |
        | 広告主が定義したアプリ内イベント | ユーザーが行ったアプリ内イベントです。 |
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        geo
      </td>
      <td>
        ISOの国コード（AppsFlyerの従来の計測方法ではユーザーのIPアドレスから取得しますが、SKANではアドネットワーク側で補足されたデータか、モデル化されたデータになります。）
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        install\_date
      </td>
      <td>
        SKAN：SKANポストバックの到着時刻を基に、AppsFlyerが推定

        AppsFlyer計測：

        * UAデータ（非オーガニックインストール）：インストール後の初回起動時刻
        * リターゲティングデータ：リエンゲージメント/リアトリビューション後の初回起動時刻
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        UAデータ（非オーガニックインストール）：TRUE

        リターゲティング:リエンゲージメント期間中は、元のメディアソース（リエンゲージメント前）と、リエンゲージメントメディアソースの両方にアトリビューションします。イベントがリエンゲージメント期間内にある場合。元のメディアソースはFALSE（プライマリアトリビューションではない）になります。リエンゲージメント媒体では値がTRUEとなります。
      </td>
      <td>
        bool
      </td>
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td>
        イベントが紐づけられたアドネットワーク名
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        selected\_currency
      </td>
      <td>
        アプリ設定でユーザーが設定した3文字の通貨コード（USD、EUR｜形式：ISO-4217）（SSOTモードの画面で収益を表示する際に使用され通貨単位と同じです。）
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        想定値：  
        Install：ユーザーが初めてアプリをダウンロードして初回起動した場合  
        Re-attribution：ユーザーがリターゲティング広告に接触後にアプリを再インストールした場合  
        Re-donwload (SKAN)：ユーザーがアンインストール後にアプリを再インストールした場合  
        Re-engagement：Re-engagement：ユーザーが、リターゲティング広告に接触後にアプリを再起動した場合
      </td>
      <td>
        string
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="metrics" />

<Accordion title="指標">

| 名称 | 詳細 | 形式 |
| --- | --- | --- |
| revenue\_selected\_currency | 選択した通貨単位での累積収益額（小数点以下2桁まで）  <br />例：event\_name=purchaseでdays\_post\_attribution=2の場合、この値には2日目だけでなく、インストール後2日目までにおける購入イベントの総収益金額が反映されます。 | double |
| revenue\_usd | USD単位での累積収益額  <br />例：event\_name=purchaseでdays\_post\_attribution=2の場合、この値には2日目だけでなく、インストール後2日目までにおける購入イベントの総収益金額が反映されます。 | double |
| skan\_duplicates | SKANとAppsFlyerの計測手法によって同時に媒体へ成果が紐づけられ、SSOTデータにおいて重複除外されたインストールデータ | long |
| uninstalls\_count | アプリインストール後にアンインストールしたユーザー数（UAキャンペーンのみ対象） | long |
| unique\_users | イベントを実行したユニークユーザ数（値は累積値です）  <br />例：event\_name=purchaseでdays\_post\_attribution=2の場合、この値には2日目だけでなく、インストール後2日目までにおける購入イベントを実行したユニークユーザー数が反映されます。 | int |

</Accordion>

<div id="modeled-data" />

<Accordion title="推定値">

AppsFlyerは、通常のSKAdNetworkレポートでは提供できないデータをモデル化して提供しています。

* Null コンバージョン値（CV）：SKANでは、Appleがユーザーのプライバシーを保護するために実際のデータを「Null」値に置き換えることがあります。データが省略されないように、これらのNULL値は SSOTでモデル化されます。（<Anchor target="_blank" href="/marketers/ja/docs/skan-modeled-data#null-conversion-values">詳細</Anchor>）
* より長いインストール以降の計測指標：インストール後2日間を超えた後のSKANのデータ粒度は制限が多く、不正確になる可能性があります。高いデータ品質を維持するために、days\_post\_attributionが2を超えた場合、収益と、アプリ内イベントのユニークユーザー数をAppsFlyerが推定します。（<Anchor target="_blank" href="/marketers/ja/docs/skan-modeled-data#revenue-ltv">詳細</Anchor>）

国データ：SKANはデータ粒度を制限しており、多くのケースにおいて国データを利用できません。このような場合は、データをモデル化して効率的なパフォーマンス分析を可能にします。（<Anchor target="_blank" href="/marketers/ja/docs/skan-modeled-data#geo">詳細</Anchor>）

</Accordion>

<div id="partial-data" />

<Accordion title="部分的なデータ">

直近のインストール日のデータを分析する場合、インストール後の長期間（例：7日間）のイベント指標が完全に成熟していない（出揃っていない）可能性があります。このような場合、指標は使用できますが、部分的なデータがレポートに反映されます。

その他の仕様：

* レポートは、入手可能なデータが利用可能になるとすぐに表示されます。
* 5日後に、インストール後2日間までの指標が完成します*。
* 7日後に、インストール後7日間までの指標が完成します。なお、インストール後15日以内までは、推定値が調整される場合があります。

部分的なデータの理由：

* データの成熟度：インストール日からの経過時間が分析対象とするイベント日数よりも短い場合、データはまだ蓄積途中であり完全ではありません。
* SKANの遅延仕様：SKANデータはランダムに遅延してレポートされます。たとえば、インストール後最初の2日間のイベント情報は、インストール後最大 96 時間後 (4日後) までにレポートされます。
* SKAN推定値のデータ反映のタイミング：インストール後2日以降の期間のSKANデータが推定されます。AppsFlyerのモデル化機能は、7日後に最初の推定値を生成します。この期間（2日目から7日目）、AppsFlyerの従来の計測手法のデータは利用できますが、SKAN推定値のデータは利用できません。

例：インストール日が1月1日の場合

* 1月2日：SKANデータはまだ受信されていません。インストール後2日間とインストール後7日未満のデータはどちらも部分的であり、AppsFlyerの従来の計測手法のデータで構成されます。
* 1月3日：SKANデータが部分的にレポートされ始めます。インストール後2日間のデータは部分的なままですが、一部SKAN計測のデータが含まれるようになります。インストール後7日間のデータには、推定されたSKANデータはまだ含まれません（最初のモデル化されたデータは、インストールから7日後に利用可能になります）。そのため、インストール後2～7日目までの間は、インストール後2日間と比較して、インストール後7日間の推定値が小さくなる可能性があります。
* 1月6日：インストール後の最初の2日間のSKANデータは、遅延のあったポストバックも含めて完全に受信されます。この時点で、インストール後 2日間の指標が完成しますが、インストール後7日間の指標はまだこの時点では完成していません。
* 1月8日：インストール後7日間のSKAN推定値データが完成します。AppsFlyerのSKAN推定値は、1月16日まで数値の調整が続きます。

</Accordion>

## ディレクトリの構造

<div id="report-folder-hierarchy" />

<Accordion title="レポートのフォルダ階層">

* プライマリフォルダはレポートタイプ別に整理され、含まれる想定値は、'ssot\_unified'、'ssot\_reargeting'、'sot\_user\_quisition' のいずれかです。
* これらのフォルダ内のサブフォルダは、インストール日順に整理されます。

**バージョン管理**

* 各インストール日のフォルダには複数のバージョンが格納され、各バージョンは毎日作成されます。
* 各バージョンには、そのインストール日の更新された累積データが反映されます。
* レポートには、インストール日で入手可能なすべてのデータが含まれます。たとえば、4月18日の各インストール日の最新バージョンには、その時点の4月18日までのすべてのデータが含まれます。
* ヒント：正確性を確保するために、常に最新バージョンのレポートデータを処理してください。

各インストール日は、最大15個までのバージョンに制限されます。つまり15日後、すべての指標が完全にフィックスして完成します。（<Anchor target="_blank" href="/marketers/ja/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">詳細</Anchor>）

</Accordion>

<div id="directory-and-filename-structure" />

<Accordion title="ディレクトリとファイル名の構造">

レポートへのパスは次の形式で構成されます：

`<bucket-name>`/t=`<ssot_unified OR ssot_retargeting OR ssot_user_acquisition>`/install\_date=`<yyyy-mm-dd>`/version=`<unix timestamp>`/`<parquet file number>`

例：広告主バケットにおけるフォルダ階層の場合：

```
bucket
|
└── t=ssot_unified
    |
    ├── install_date=2024-05-05
    |   |
    |   └── version=1714890235
    |   |    |
    |   |    ├── part-00000-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    |
    |   |    ├── part-00001-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    │
    |   |    └── part-00002-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |
    |   |
    |   └── version=1714890286
    |        |
    |        ├── part-00000-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        |
    |        ├── part-00001-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        │
    |        └── part-00002-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |   |
    .   . 
    .   .
```

説明：

* t：　 レポートトピック（タイプ）
* install\_date：　アプリのインストール日を指します。つまり、インストール後のアクティビティは、ユーザーアクションが発生した日ではなく、ユーザーがアプリをダウンロードしたインストール日に基づいて表示されます。
* version：　バージョンが作成された日時を示すUnix形式のタイムスタンプです。

</Accordion>

## データ分析担当者向けの注意点

**レポート内のデータ範囲について：**

レポートには、ユーザー獲得施策での新規インストール、リターゲティング施策のリアトリビューション（SKANにおける再ダウンロード）、リエンゲージメントに関するデータと、それらに紐づくアプリ内イベントが含まれます。

<div id="loading-reports" />

<Accordion title="レポートの読み込み">

統合レポート、ユーザー獲得レポート、リターゲティングレポートを別々に、またはまとめてBIで取得することが可能です。これらをまとめて読み込んで、独自にデータをフィルターする場合は以下の対応が必要です：

* 統合レポート：　is\_primary\_attribution=true または NULL のデータを使用してください。
* ユーザー獲得レポート：　conversion\_type=Install のデータを使用してください。
* リターゲティングレポート：　conversion\_type=re\_engagement と re-attribution のデータを使用してください。
* 統合ビュー：　データ読み込みのプロセスにおいて統合ビューのデータを使用すると、キャンペーンタイプ間でデータを分割できます：

* その場合は、conversion\_type=install、re-engagement、re-attribution（SKAN計測における再ダウンロード）を使用してください。
* 詳細については、「リターゲティングイベントの二重計測ロジック」のページを参照してください。

</Accordion>

<div id="days-postattribution" />

<Accordion title="Days post_attributionについて">

> 🚧 **重要！**
>
> レポートには days\_post\_attribution というディメンション（項目）が含まれています。このディメンションは、収益とユニークユーザーのデータをインストール後の特定の日数に紐付けるものです。

* アトリビューション（インストール、リエンゲージメントなど）データの場合、この値は0です。
* 収益とアプリ内イベントについては、データは事前定義されているコホート毎に分類され、現状はインストール後「2日」と「7日」のみに制限されています。

<strong>アプリ内イベントと収益を正確に分析するには、days\_post\_attributionのディメンションにフィルターを適用する必要があります。</strong>詳細は、以下のクエリ例を参考にしてください。

よくある間違いの例として、特定のディメンションの収益列を合計するという単純なロジックを適用してしまうケースが挙げられます。この方法では、一部の収益データが 2 回 (1 回は days\_post\_install=2、もう 1 回は days\_post\_install=7) カウントされるため、誤った数値になります。この例は、特定のアプリ内イベントにおけるユニークユーザー数を分析する場合にも関係します。

</Accordion>

<div id="considerations" />

<Accordion title="注意事項">

**考慮事項：**

* 最終バージョン：　常にインストール日ごとに利用可能な最新バージョンのデータを参照して、分析には最新かつ正確なデータを使用してください。
* 収益の計算：　revenue\_usd (USD換算の収益金額) は、イベント発生日のUSDの為替レートを使用して計算されているので注意してください。
* アトリビューションデータの分析：　event\_name=af\_conversion のデータは、アトリビューション（インストール、リアトリビューション（SKANにおける再ダウンロード）、リエンゲージメント）のデータを意味します。アトリビューション数はユニークユーザー数の指標の下に表示され、これらのデータの収益指標は空になります。前述の通り、days\_post\_attribution の値は0になります。
* 管理画面上の数値との比較：　インストールを管理画面上のデータと比較する場合、新規インストールと再ダウンロード、両方のコンバージョンタイプを合計してください。SKANオーバービュー上では、インストールのフィルタで新規インストールと再ダウンロードの両方が選択されています。
* アプリ内イベントの分析：　event\_nameが「af\_conversion」ではないデータが、アプリ内イベントに関するデータです。イベントを実行したユニークユーザー数はユニークユーザー数の指標に表示され、これらのイベントから発生した収益は収益指標に表示されます。
* コンバージョンタイプ：　conversion\_typeののディメンションを使用して、ユーザー獲得とリターゲティングのコンバージョンを区別してください。なお、SKANデータの場合にはinstallと再ダウンロードで更に分解されます。データをSSOTモードをONにした管理画面と比較する場合は、どちらのタイプもインストールと見なして処理されます。
* 広告収益イベント：　これらは可能な場合は含まれています。
* データの分割：　すべてのアプリデータが1つのファイル内にまとめて提供されます。App ID の項目を使用してアプリ毎にデータを分割するか、Data Locker上でアプリ毎に分割するよう設定してください。

</Accordion>

<div id="example-use-cases" />

<Accordion title="活用事例：">

以下は、BI担当者が Data Lockerを介して抽出できるコホートデータの、一般的で実用的な応用例です。各例は、SQL ステートメントとサンプルの Excel ビジュアルで示されています。

<div id="calculating-total-attributions-per-campaign" />

<Accordion title="キャンペーンごとの合計アトリビューション数の計算">

このクエリでは：

* 各インストール日における、キャンペーンごとのユニークなアトリビューション数を合計しています。
* イベント名「af\_conversion」と、特定のキャンペーン ID (af\_c\_id) を含むコンバージョンでフィルターしています。

```sql
SELECT install_date, SUM(unique_users) AS total_attributions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign" />

<Accordion title="コンバージョン（インストール＆再ダウンロード）の計算と、キャンペーン毎の管理画面上のインストール数との比較">

このクエリでは：

* キャンペーンとインストール日毎に、新規インストールと再ダウンロードを区別してコンバージョン数をカウントしています。
* インストール数を、コンバージョンタイプ「install」と「re-download」を統合している管理画面上のインストール指標と比較しています。

```sql
SELECT install_date, conversion_type, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND conversion_type IN ('install', 're-download')    
-- The dashboard sums both under the install field
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type;
```

</Accordion>

<div id="calculating-retargeting-conversions-per-geo" />

<Accordion title="国別のリターゲティングコンバージョンの計算">

このクエリでは：

* リターゲティングキャンペーンのコンバージョンを国別にカウントしています。
* 「re-attribuition」と「re-engagement」のコンバージョンをカウント対象にしています。

```sql
SELECT install_date, conversion_type, geo, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type IN ('re-attribution', 're-engagement')    
-- Both types are relevant for re-targeting
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type, geo;
```

</Accordion>

<div id="calculating-installs-by-attribution-method-per-media-source" />

<Accordion title="メディアソース別 x 計測方法別でのインストール数の計算">

このクエリでは：

* 計測手法（SKAN、AppsFlyer、オーガニック）別にインストール数をカウントし、メディアソース別に分類しています。
* コンバージョンタイプが 「install」 、イベント名が「af\_conversion」のデータでフィルターしています。

```sql
SELECT install_date, attribution_method, media_source, SUM(unique_users)   
AS total_installs
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type = 'install'
    AND app_id = 'YOUR_APP'
GROUP BY install_date, attribution_method, media_source;
```

</Accordion>

<div id="calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset" />

<Accordion title="広告セット毎の、Facebookのインストール後7日間の累積収益の計算">

このクエリでは、Facebookで配信された広告のインストール後7日以内の累積収益を計測しています。

```sql
SELECT install_date,
       af_adset,
       SUM(revenue_usd) AS total_revenue_day_7
FROM ssot_unified
WHERE media_source = 'facebook'
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_adset;
```

</Accordion>

<div id="calculating-cumulative-revenue-for-selected-postinstall-periods" />

<Accordion title="インストール後の選択した期間における累積収益の計算">

このクエリでは：

* インストール後の選択した複数の日数における累積収益を計算して、2日目と7日目の合計の分割しています。
* 過去7日間のインストールを分析する場合は、インストール後7日間のデータがまた不完全である可能性がある点に注意してください。<Anchor target="_blank" href="/marketers/ja/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">（詳細はこちら）</Anchor>

```sql
SELECT install_date,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) AS total_revenue_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) AS total_revenue_day7
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source" />

<Accordion title="メディアソース別の、特定のアプリ内イベント（購入）からの収益の計算">

このクエリでは：

* 特定のアプリ内イベント（af\_purchaseなど）の収益額を計測し、そのデータをメディアソース別に集計しています。
* インストール後の特定の日数でフィルターして、データが重複してカウントされないようにしています。

```sql
SELECT install_date, media_source, SUM(revenue_usd) AS total_purchase_revenue
FROM ssot_unified
WHERE event_name = 'af_purchase'  -- Change to your specific event
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

<div id="calculating-inapp-event-conversion-rate-for-2-days-postinstalls" />

<Accordion title="インストール後2日間のアプリ内イベントのコンバージョン率の計算">

このクエリでは、全インストールおける特定のアプリ内イベント（af\_complete\_tutorialなど）のコンバージョン率を計算しています。

```sql
SELECT install_date,
  SUM(IF(days_post_attribution = 2 AND   
event_name = 'af_complete_tutorial', unique_users, 0)) 
  / SUM(IF(event_name = 'af_conversion', unique_users, 0))   
AS conversion_rate_day2_af_tutorial_conversion
FROM ssot_unified
WHERE conversion_type = 'install'    
-- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id" />

<Accordion title="キャンペーンIDごとのインストール後2日間と7日間のARPUの計算">

このクエリでは：

* キャンペーン全体のインストール後2日間と7日間における、1ユーザーあたりの平均収益（ARPU）を計算しています。
* 過去7日間のインストールを分析する場合は、インストール後7日間のデータがまた不完全である可能性がある点に注意してください。<Anchor target="_blank" href="/marketers/ja/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">（詳細）</Anchor>

```sql
SELECT install_date,
       af_c_id,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day7
FROM ssot_unified
WHERE conversion_type = 'install'  
       -- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_c_id;
```

</Accordion>

<div id="calculating-amount-of-duplicates-per-media-source-in-this-query" />

<Accordion title="メディアソース別の重複数の算出">

このクエリでは、重複したユーザーアトリビューションの総数を、メディアソースとインストール日別にカウントし、ユーザーアトリビューションの重複が多いメディアチャネルを特定しています。

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
    AND event_name = 'af_conversion'
GROUP BY install_date, media_source;
```

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="仕様と制限">

| 特性 | 備考 |
| --- | --- |
| 1日あたりのレポートの可用性 | その日の終わりまでにSSOTトグルがオンになったインストール日のみ、SSOTレポートのデータが表示されます。 |
| インストール後2日間の指標 | <ul><li>Conversion Studio - SKAN 4の場合：データはインストール後2日間のものです。</li><li>Conversion Studio - SKAN 3の場合：データは、設定されたSKANのアクティビティ期間に基づきます。<br />例：アクティビティ期間が 24時間の場合、24時間以内に発生したイベント (X日+1日目であっても) がカウントされます。</li></ul> |
| アプリ内イベントの可用性 | 1つ目の計測期間中に発生したイベントのみが確認可能です。 |
| SKANにおける再ダウンロード(re-download)の内訳 | 分割可能です。SSOTの管理画面ではこの内訳は表示されず、インストールと再ダウンロードの両方がインストールのデータに含まれます。 |
| SKAN Conversion Studioの設定変更 | SKAN Conversion Studioの設定を変更すると、以前のスキーマでエンコードされたインストールからのポストバックがまだ届くため、変更後約96時間の間、SSOTデータが不正確になる可能性があります。 |
| データに適用されるタイムゾーン | アプリ毎に設定したタイムゾーンは適用されません。 |
| オーガニックデータ | <ul><li>インストール後7日間の指標を利用できます。</li></ul> |
| Days post-conversion（インストール、リアトリビューション、リエンゲージメント）のデータ | 7日までのdays post-conversionデータに限定されます。 |
| 代理店の運用媒体の開示設定 | 対応しています。（設定内容に応じてデータが表示されます） |
| キャンペーン名の変更 | 対応していません。キャンペーン名が変更された場合、キャンペーン IDを使用してグループ化とフィルタリングを行います。 |
| アドネットワーク | <ul><li>アドネットワークは、以下条件下において、SSOT DataLocker レポートにアクセスして、自社媒体に紐づいたデータを確認可能です。<ul><li>広告主が、SKAN Conversion Studio内でSSOTをオンにしている。</li><li>アドネットワークが、SKAN計測に対応している。</li><li>アドネットワークが、[集計データへのアクセス権限を広告主から付与されている。](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions)</li></ul></li></ul> |
| 代理店によるデータアクセス | 代理店アカウントでは利用できません。代理店アカウントは、管理画面上でSSOTモードをONにして SSOTデータを確認可能です。 |
| インストール後7日間（D7）の指標 | <ul><li>オーガニックトラフィックのD7指標は、2025年2月16日以降のデータのみで利用できます。</li><li>以下条件において、指標が欠損するか、D2よりも小さくなる可能性があります：<ul><li>指定した日付範囲に、インストール後8日が経過していない日付が含まれている</li><li>推定値がまだ利用可能ではない（例：14日未満の収益データ）（<Anchor target="_blank" href="/marketers/ja/docs/skan-modeled-data#revenue-ltv">詳細</Anchor>）</li><li>SKAN Conversion Studioの設定が、過去14日間に変更された</li><li>指定した日付におけるインストール数が10件未満</li></ul></li></ul> |
| 既定のイベント名 | 「af\_conversion」のイベント名はコンバージョンの種類を示すために使用されるため、仮に「af\_conversion」という名称のイベントが既に実装されているアプリでは、元のイベント名が「af\_conversion\_event」に変更されるので注意してください。 |
| 通貨設定の違い | SSOTモードの管理画面上の数値とSSOTのDataLockerレポートは同時に計算されないため、管理画面上で設定した通貨単位での収益金額と、レポート上でのそれと比較すると、収益金額に若干の相違が生じる場合があります。これは、データを計算した時点で使用した通貨レートが若干異なるためです。 |
| SKAN D7の部分的データ | SKANのD7データはモデル化されており、最初のバージョンのデータはインストールから7日後に利用可能になります。そのため、過去7日間のD7指標を分析した場合、D7のデータは部分的なデータになりまだ確定していない状況です。また、計測手法がSKANのデータの場合、D7の指標がD2指標よりも低くなる可能性があります。 |
| D7の収益とアプリ内イベントにおける、データ粒度の制限 | インストール後 7日間の収益とユニークユーザーイベントの指標は、広告セット、広告、コンバージョンタイプの各レベルでは確認できません。これは、SKANでは通常この粒度での詳細情報は確認できず、推定値においてもこれらのディメンションは考慮されないためです。 |
| 広告収益データの更新頻度 | 広告収益データは1日遅れで格納されます。<br /><br />例えば、7月3日の朝に作成されたレポートには、7月1日までの広告収益データが含まれます。 |

</Accordion>

<div data-zendesk-anchors="h_01J455DHWAB1J9611A4KA40PZM=%E6%B3%A8%E6%84%8F ssot-reports-in-data-locker=data-locker%E3%81%A8%E3%81%AF h_01J454K90GWKME8F4JCDQKM3CK=data-locker%E3%81%A8%E3%81%AF what-is-single-source-of-truth-ssot=ssotsingle-source-of-truth%E3%81%A8%E3%81%AF h_01J454K90GRCFR3PSAQRTX98B4=ssotsingle-source-of-truth%E3%81%A8%E3%81%AF benefits-of-ssot-reports-in-data-locker=data-locker%E3%81%A7%E3%81%AEssot%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E5%8F%96%E5%BE%97%E3%81%AE%E5%88%A9%E7%82%B9 h_01J454PANH9J6ZZ069RS6FVWZM=data-locker%E3%81%A7%E3%81%AEssot%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E5%8F%96%E5%BE%97%E3%81%AE%E5%88%A9%E7%82%B9 h_01J46C54ZB4YYTZ6CDHHC0EC8P=setting-up-data-locker h_01J455Q07J5XPYEBVP3BZ1FMVH=permissions h_01J29BTC9CESJF592P616WMK46=ssot-report-facts report-structure::673746b9=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E6%A7%8B%E6%88%90 h_01J29CQ5K4JBEP4X8YQ0V32WYR=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E6%A7%8B%E6%88%90 h_01J29CHBX2QNFTAQSA1W01PFH0=field-formats h_01J29BTC9CJ8GZDDCHK9NBZ4YX=dimensions h_01J29BTC9C86YMVEY17QQZNZCV=metrics h_01J29BTC9CH3DAA7ZRHG8C04MF=modeled-data h_01J29M72WAPH3KEW9N60JHTT3W=partial-data directory-structure=%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AE%E6%A7%8B%E9%80%A0 h_01J29MB7B7Q3PJ9YWFQESWN0KD=%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AE%E6%A7%8B%E9%80%A0 h_01J29MCSH4V41CPB7ZG41751QW=report-folder-hierarchy h_01J29MCSH40ATHNAJMY8KR7ANZ=directory-and-filename-structure bi-developer-considerations=%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%8B%85%E5%BD%93%E8%80%85%E5%90%91%E3%81%91%E3%81%AE%E6%B3%A8%E6%84%8F%E7%82%B9 h_01J29MS6XV7XYTA9Q81454WEQN=%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%8B%85%E5%BD%93%E8%80%85%E5%90%91%E3%81%91%E3%81%AE%E6%B3%A8%E6%84%8F%E7%82%B9 h_01J2F4HG8YHDGYFKHBBC5KSN2G=loading-reports h_01J2F4HG8YKNEVGEWTR91ADSDS=days-postattribution h_01J3YT1X908JVMDXKRQBCRD1JR=%E9%87%8D%E8%A6%81 h_01J2F4HG8YAAE0E04Y6Q9Z62NZ=considerations h_01J3A82HZF14CCS027FE991M0T=example-use-cases h_01J3A883DQFQE0WTTY4FMX3AQ4=calculating-total-attributions-per-campaign h_01J3A883DQ82K71XY408M2BW0B=calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign h_01J3A883DQ5QAVH6AX7CGCBSWG=calculating-retargeting-conversions-per-geo h_01J3A883DQE25X31SPPF166BRH=calculating-installs-by-attribution-method-per-media-source h_01J3A883DQ8QVR8WKPPX1QF414=calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset h_01J3A883DQ51T3Z6H239P5JDJ1=calculating-cumulative-revenue-for-selected-postinstall-periods h_01J3A883DQXRCQ4NWY0BCX886E=calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source h_01J3A883DQRR62BWQ6JBTZ7238=calculating-inapp-event-conversion-rate-for-2-days-postinstalls h_01J3A883DRPEVDQCWKCT9M3EC1=calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id h_01J3A883DRRZ9Y8F3KNAAPZT2S=calculating-amount-of-duplicates-per-media-source-in-this-query h_01J29MV69M667QDHMS5WGYKPCZ=traits-and-limitations" />
