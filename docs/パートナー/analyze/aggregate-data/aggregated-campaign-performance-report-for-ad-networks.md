---
title: アドネットワーク向けキャンペーンの集計パフォーマンスレポート
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketing Analytics
    - Ad Networks
  created_at: '2021-05-30T12:34:03Z'
  edited_at: '2026-10-14T09:27:37Z'
  id: 360020834237
  locale: ja
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/ja/articles/360020834237
---
> **概要**：概要：アドネットワークは、7日目のリテンションKPIなどのキャンペーンパフォーマンス指標を計算するために、集計パフォーマンスレポート（≒ コホートレポート）を自社のBIシステムに取り込むことができます。

<div id="aggregated-campaign-performance-report" />

## キャンペーンの集計パフォーマンスレポート

このレポートでは、特定のイベントを実行したユニークユーザー数を含む、キャンペーンのパフォーマンスデータを提供します。アドネットワークは、このデータを自社のBIシステムで使用して、広告主のKPIを把握するためのキャンペーンパフォーマンス指標を計算することができます。このレポートは<Anchor target="_blank" href="/partners/ja/docs/data-locker-for-partners">パートナー向けData Locker</Anchor>経由で毎日更新されます。

**なぜこのレポートが必要ですか？**

iOS 14.5のリリース前は、AppsFlyerが送信したレポートには、ユニークユーザーイベント指標を計算するために十分なデータが含まれていました。

iOS 14.5以降、広告主による高プライバシー一括設定（AAP）の採用により、非同意ユーザーのポストバックデータにはユーザー識別子が含まれていません。識別子がないと、7日目リテンション率などのユニークユーザー指標を計算することができません。ユニークユーザー指標が欠けていると、キャンペーンを最適化する手段や広告主と共通のリテンション目標を設定することができません。

レポートにはどんなデータが含まれていますか？

指標は、レポートされたディメンションを使用し可能な限りの粒度で提供され、次のパフォーマンス指標が含まれています。

* 収益
* イベントが実行された回数
* イベントを実行したユニークユーザー数
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vS89RlkFIss7uARroJcOcX1rU6gUmZ2ySYwfTprg9GaA2BYnvDPVqWmOicea1wrBnNuGgEuLPwzL_ac/pub?gid=0&single=true&output=csv">サンプルレポート</Anchor>

レポートはどのように取得できますか？

* レポートはパートナー向けData Locker経由で提供されます。レポートは<Anchor target="_blank" href="/marketers/ja/docs/about-data-freshness-and-timezone-support#daily">UTC時刻で毎日</Anchor>更新されます。
* アドネットワークへのデータ共有を可能にするには、予め広告主側で管理画面上から[権限を付与する](/docs/aggregated-campaign-performance-report-for-ad-networks#permission-to-get-aggregated-performance-data)必要があります。

<div id="about-the-report" />

## レポートについて

<div id="report-structure" />

<Accordion title="レポート構成">

<div id="dimensions" />

#### ディメンション

<Table>
  <thead>
    <tr>
      <th>
        フィールド名
      </th>
      <th>
        備考
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        app\_id
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        * 入力される値：install、re-engagement、re-attribution
        * 同等のポストバックマクロ：is\_retargeting
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        含まれる値：click, impressions, pre-install, unknown, tv, null
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        インストールやリエンゲージメントなどのコンバージョンイベントから経過した日数です。   
        最大日数は180です。

        ヒントこの値を使用して、リテンションや〇日後時点でのKPIなどを計算しましょう。
      </td>
    </tr>
    <tr>
      <td>
        event\_date
      </td>
      <td>
        イベントが発生した日。

        形式： yyyy-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        conversion\_date
      </td>
      <td>
        形式： yyyy-mm-dd
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
        | af\_conversion | コンバージョンしたユーザー。conversion\_type を使用して、インストール、リエンゲージメント、リアトリビューションなどのCVタイプを区別してください。 |
        | af\_sessions | アプリ起動 |
        | af\_uninstall | アプリのアンインストール |
        | 広告主が定義したアプリ内イベント | アプリ内イベントを実行しました。アプリ内イベント名はパートナー側のイベント名にマッピングされていません。 |
      </td>
    </tr>
    <tr>
      <td>
        campaign
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        campaign\_id
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        adset
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        adset\_id
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        ad
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        ad\_id
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        channel
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        site\_id
      </td>
      <td>
        キャンペーン階層の情報です。
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        リターゲティングデータを特定し重複排除するために使用されます
      </td>
    </tr>
    <tr>
      <td>
        country\_code
      </td>
      <td>
        ユーザーのIPアドレスから生成されます
      </td>
    </tr>
    <tr>
      <td>
        agency
      </td>
      <td>
        空白の場合、関連する代理店はいません。
      </td>
    </tr>
    <tr>
      <td>
        Keywords
      </td>
      <td>
        [2022年4月27日より利用可能] アドネットワークからレポートされた、エンドユーザーがオンライン検索時に使用した単語アドネットワークからレポートされたもの
      </td>
    </tr>
    <tr>
      <td>
        キーワードID
      </td>
      <td>
        [2022年4月27日より利用可能] アドネットワークからレポートされた、キーワードID
      </td>
    </tr>
  </tbody>
</Table>

<div id="metrics" />

#### 指標

| 名前 | フィールド | イベントを実行したユニークユーザー |
| --- | --- | --- |
| ユニークユーザー数 | unique\_users | イベントを実行したユニークユーザー数 |
| 収益 | revenue\_usd | 累計収益（米ドル）。例：$100.56 は100.56 と反映されます。 |
| event\_count | event\_count | イベントの発生数 |

</Accordion>

<div id="bi-developer-considerations" />

<Accordion title="データ分析担当者向けの考慮事項">

**レポート内のデータ範囲**

レポートには、ユーザーアトリビューション、インストール、リアトリビューション、リエンゲージメント、そしてそれらに紐づくアプリ内イベントが含まれています。

データ取り込みプロセスにて、キャンペーンタイプ別にデータを分別するロジックを使用する必要があります。つまり、ユーザーアトリビューション（インストール）とリターゲティング（リエンゲージメント）で分ける必要があります。これを行うには、[conversion\_type] と [is\_primary\_attribution] の項目を使用する必要があります。<Anchor target="_blank" href="/marketers/ja/docs/resolve-retargeting-double-attribution">リターゲティングイベントの二重アトリビューション</Anchor>についてご覧ください。

**フィールドレベルの考慮事項**

* 継続率の指標を簡単に計算するには、days\_post\_attributionのカラムを活用しましょう。
* キャンペーン名とキャンペーン ID ディメンションを使用したユニークユーザー数の計算：キャンペーン名の細分性を無視できる場合は、キャンペーン ID のユニークカウントを合計すれば指標は正確です。
* キャンペーン階層の項目を使用することでデータを集計可能です。
* アプリ内イベントは広告主が設定したイベント名を使用し、アドネットワークのイベント名にはマッピングされていません。広告主にマッピング情報を問い合わせるか、管理画面上で閲覧してください。<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">パートナーのアプリ内イベントマッピング設定について</Anchor>。
* 収益はUSD単位で、イベント当日の為替レートを使用して計算されます。
* 広告収益イベントは、利用可能な場合に含まれますが、更新されるまでに最大5日間の遅れが生じることがあります。

**一般的な考慮事項**

* データ更新頻度：データはData Lockerの h=23 フォルダに書き込まれます。
* 利用可能なデータは、AppsFlyerによって計測されたユーザージャーニーに関する計測データです。つまり、iOSポストバックにより報告されたSKAdNetworkはこのデータセットには含まれません。
* データには複数プリを含むファイルが格納されます。app\_id 項目を使用してアプリを特定してください。
* 特定のアプリのデータを取得できない場合は、広告主から必要な権限が付与されていることを確認してください。

</Accordion>

<div id="retention-report-considerations" />

<Accordion title="リテンションレポートに関する考慮事項">

リテンション指標を作成するには、次の項目にフィルタを設定して、リテンション7日目のように作成します。

* days\_post\_install=7
* event\_name=af\_session
* 必要に応じて conversion\_type
* <Anchor target="_blank" href="/marketers/ja/docs/resolve-retargeting-double-attribution">重複リターゲティングイベント</Anchor>が含まれるのを防ぐために、is\_primary\_attribution=true を選択するか、conversion\_type を使用してデータセットをインストールに限定してください。
* グループ化：キャンペーンと必要に応じてその他のディメンション。
* 合計：unique\_users\_count

ディメンションを追加または削除することで、異なる粒度の指標を取得できます。

</Accordion>

<div id="permissions" />

## 権限

アドネットワークは、以下に記載してある権限を広告主に付与してもらう必要があります。広告主はアプリごとにこの手順を実行する必要があります。

<div id="permission-to-get-aggregated-performance-data" />

<Accordion title="集計パフォーマンスデータを取得するための権限">

代理店アカウント経由で計測の連携設定がされている場合：代理店アカウントからはパートナーアカウントへ権限を付与することができないので、本件に関する権限付与の作業は、広告主へ依頼する必要があります。

**アドネットワークが集計パフォーマンスデータを取得するのを許可する方法：**

1. AppsFlyerの管理画面に入り、左メニューの**連携** > **連携済みパートナー**へ進んでください。
2. パートナーを検索し選択してください。
3. **連携設定** をクリックして、連携の設定ページに移動します。
4. ［連携］のタブで パートナーを有効にする のトグルが**ON**になっていることを確認してください。OFFの場合、SSOTデータは共有されないのでご注意ください。
5. **権限**タブへ進んでください。
6. 広告媒体権限をONにし、追加で以下の各権限についてもONにしてください：
   * **集計コンバージョンデータへのアクセス**
   * **アプリ内イベントの集計データへのアクセス権限を付与する**
   * **収益データへのアクセス権限を付与する**
7. 最後に、右下の 権限を保存のボタンをクリックしてください。
8. 上記対応後に、権限を付与したことをアドネットワークに伝えてください。
9. 複数アプリが対象の場合には、連携しているアプリ毎に同じ作業を繰り返してください。

</Accordion>

<div data-zendesk-anchors="aggregated-campaign-performance-report=%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E3%81%AE%E9%9B%86%E8%A8%88%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HM8SQ5RE1FGQDY6V1A8MMEQX=%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%9A%E3%83%BC%E3%83%B3%E3%81%AE%E9%9B%86%E8%A8%88%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 about-the-report=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HM8SQ5REM6MW5GBRSXTF0N73=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HM8SQ5RETK7HCPZGGX8KX9VG=report-structure dimensions=%E3%83%87%E3%82%A3%E3%83%A1%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3 h_01HM8SQ5RE11PW6HGTWGC2AGR5=%E3%83%87%E3%82%A3%E3%83%A1%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3 metrics=%E6%8C%87%E6%A8%99 h_01HM8SQ5RGQEH6G6W75FVWJKSP=%E6%8C%87%E6%A8%99 h_01HM8SQ5RGCGTWTSRHB8B4FSY2=bi-developer-considerations h_01HM8SQ5RG4JEE75F6CBTFCBB5=retention-report-considerations permissions=%E6%A8%A9%E9%99%90 h_01HM8SQ5RGNXENZ89GD74KJWH2=%E6%A8%A9%E9%99%90 h_01HM8SQ5RGQADHTEP5ED3W87VZ=permission-to-get-aggregated-performance-data" />
