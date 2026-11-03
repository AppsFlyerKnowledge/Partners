---
title: Data Locker：連携済みパートナー向け
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Data Locker
    - Agencies
    - Ad Networks
  created_at: '2021-05-28T15:37:04Z'
  edited_at: '2026-10-14T09:32:28Z'
  id: 360020818517
  locale: ja
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ja/articles/360020818517
---
> **概要：** 概要：パートナー（アドネットワーク / 代理店）向けのData Lockerは、アプリのデータを AWS、GCSまたはBig Queryのパートナーのストレージへ配信します。

![6133DataLockerForPartners.png](https://files.readme.io/f6cad12250fe07cf2b0a12b64eeaa597c83527b4b4e09aea11cc2a52ab53339b-4637680455313.png)

## Data Locker：連携済みパートナー向け

パートナー向けのデータロッカーは、アプリデータをクラウドストレージに提供します。広告主は、AppsFlyerが特定のパートナーと選択したデータを共有できるようにする権限を設定します。

<div id="data-locker-features" />

<Accordion title="Data Lockerの主な機能">

| 機能 | 説明 |
| --- | --- |
| ストレージオプション（クラウド） | 自社で保持している以下のストレージ(バケット)：<ul><li>AWS</li><li>GCS</li><li>Yandex</li><li>BigQuery</li></ul><Anchor target="_blank" href="/marketers/ja/docs/data-locker-for-marketers#storage-options">ストレージの選択肢について</Anchor> |
| 複数アプリ対応 | 計測連携しているアプリのデータを取得可能です。ただし、データを取得するには広告主がレポート毎に権限を付与する必要があります。 |
| データ形式のオプション | <ul><li>バケットクラウドストレージの場合：<ul><li>CSV</li><li>Parquet</li><li>Adobe</li></ul></li><li>データウェアハウス</li></ul> |
| データ更新頻度 | レポートタイプ毎に更新頻度が異なります：<ul><li>**毎時：** 継続的に生成されるデータ</li><li>**毎日： １日毎(daily)：  一部のレポートは日時で作成され、翌日以降に利用可能になります。**</li></ul> |

</Accordion>

<div id="reports-available-for-partners" />

<Accordion title="連携済みパートナーが利用可能なレポート">

利用可能なレポートとレポートを取得するために必要な権限は、パートナーの種類によって異なります。ただし、データロッカーのメカニズム、ストレージオプション、および必要な設定は、パートナーの種類に関係なく同じです。パートナータイプ毎に、以下の記事を参照してください：

* <Anchor target="_blank" href="/partners/ja/docs/data-locker-reports-available-for-ad-networks">アドネットワーク</Anchor>
* <Anchor target="_blank" href="/partners/ja/docs/data-locker-reports-for-agencies">代理店</Anchor>
* <Anchor target="_blank" href="/partners/ja/docs/data-locker-reports-for-api-partners">マーケティングパートナー</Anchor>

</Accordion>

## データストレージのアーキテクチャ

<div id="overview" />

<Accordion title="概要">

各種データは、選択したストレージオプションに書き込まれます。ストレージオプションは、いつでも別のオプションに変更できます。変更は数時間以内に完了します。

クラウドバケットストレージ内のデータは、レポートタイプ、日付、時刻に従って階層フォルダ構造に編成されます。次の図は、この構造の例を示しています：

![DLFolderOVerview.png](https://files.readme.io/78f360ec1df72253e5b2cd725f3eecf4e17548a7f06b544a94a75a2c319d77a0-18107910420369.png)

レポートデータは、そのレポートが関連している時間 (h) のフォルダに格納されます。

* 時間 (h) フォルダの数は、レポートデータの更新頻度 (DailyまたはHourly) によって異なります。
* データは、Snappy または GZIP圧縮ファイル、もしくはParquet 形式またはCSV形式の非圧縮ファイルで提供されます。
* データファイルは列（項目）で構成されています。
* カラムの構成はレポート種別毎に定義されています。

</Accordion>

<div id="folder-structure" />

<Accordion title="フォルダの構成">

| フォルダ | 説明 |
| --- | --- |
| data-locker-hourly | ![DLHourly.png](https://files.readme.io/c257b82d22622d97808a6c23603ac4eee9f2ab091bcb68a33637ac4fb749fdff-18107874510353.png)<ul><li>バケット内の最上層のフォルダはストレージサービスによって異なります。</li><li>*data-locker-hourly* フォルダにはレポートトピックが含まれています。</li></ul>**バケット所有者とクラウドプロバイダー毎のフォルダ構成の例**：<ul><li>**広告主保有のAWSバケット**: *&lt;af-datalocker-your bucket prefix>/&lt;generated-home-folder>&lt;subscription-id>*</li><li>**広告主保有のGCSバケット:** &lt;your bucket name>/&lt;generated-home-folder>/&lt;subscription-id></li></ul> |
| t (topic) | レポートタイプはレポートの主題に関連します。 |
| dt (日付) | これはデータの日付に関連します。ほとんどの場合、これはイベントが発生した日時を意味します。 |
| h (hour) | h フォルダはAppsFlyerがデータを受信した時刻に紐付けられています。例えば、インストールイベントを 14:00-15:00 UTC に受信した場合、h=14 ファイルにストリーミングされます。ご注意くださいAppsFlyerにデータが到着してから、h フォルダがData Lockerに書き込まれるまで、約6時間のタイムラグがあります。例えば、h=14 フォルダは6時間後の 23:00 UTCにストリーミングされます。<br /><br />**フォルダの特性**：<ul><li>0〜23の番号が付いた24個の h フォルダがあります。例えば、h=0, h=1などです。</li><li>また、Lateというフォルダも存在し、こちらには午前0時以降に到着した前日のイベントが含まれます（つまり、翌日 00:00–02:00 UTCの間に到着したものです）。例えば、ユーザーが月曜日の08:00にアプリをインストールし、イベントが火曜日の01:00に到着した場合です。このイベントは月曜日のLateフォルダに記録されます。</li><li>02:00以降に到着したデータは、実際の到着日時のフォルダに記録されます。</li><li>lateフォルダのデータも必ず確認し、利用してください。これらのデータは他の h フォルダには含まれていません。</li><li>一時フォルダ：場合によっては、hフォルダ内に一時的なフォルダを生成する場合があります。一時フォルダとサブフォルダは無視してください。例： /t=impressions/dt=2021-04-11/h=18/\_temporary</li></ul> |
| 統合データ | 全アプリに関するデータは、統合したデータファイルで提供されます。データを取り込む際には、行単位でapp\_idの項目を使用してアプリを区別してください。<br /><br /><strong>データファイルの例は、h=2 フォルダをご覧ください</strong><br /><br />![UnifiedByApp.png](https://files.readme.io/dbc39c2ce99c1ff607fd553b9c9034e55728c102f31fd18a501cc00910267b28-18107874522513.png)<ul><li>データの取り込みプロセスでは、以下のことに注意してください：<ul><li>\_SUCCESS フラグが設定された後にのみ、データを取り込んでください。</li><li>フォルダの全てのファイルに<em>.gzの拡張子</em>が付いた状態でデータを取り込んでください。</li></ul></li></ul> |
| 完了フラグ | 最終ファイル（完了）フラグは、対象の h フォルダの全てのデータが書き込まれたあとに設定されます。<ul><li>\_SUCCESS フラグが存在していることを確認してから、h フォルダ内のデータを読み込んでください。</li><li>フォルダーにデータが書き込まれない場合でも、\_SUCCESSフラグは設定されます。つまり、フォルダーは空です。</li></ul> |
| データ圧縮 | ファイルはgzを使って圧縮されます。ファイルの解凍後：<ul><li>このファイルには拡張子はありません。</li><li>各ファイルには列（項目）名を含むヘッダー行があります。</li></ul> |
| 列シーケンス | レポート項目の順序は常に同じです。新しい項目が追加される場合には、常に既存項目の右端に追加されます。<br /><br />カラム(フィールド)の定義は、レポート毎に異なります。各内容については、関連するレポートのヘルプページを参照してください。 |
| 項目入力に関する考慮事項 | **空白または空のフィールド：** 一部の項目は *null* または空白になります。これは、特定のレポートのコンテキストでは、レポートするデータがないことを意味します。通常、*null* は、特定のレポートおよびアプリタイプのコンテキストでこの項目に値が入力されないことを意味します。空白（""）は、この項目がこのコンテキストに関連しているものの、入力するデータが見つからなかったことを意味します。<br /><br />**タイムゾーンと通貨設定**：<br /><br />アプリ毎に管理画面上で設定されているタイムゾーンと通過設定は、Data Lockerに書き込まれるデータでは無視されます。代わりに、以下仕様が適用されます：<ul><li>**time\_zone**日付と時間のデータはUTCです。</li><li>**通貨：** event\_revenue\_usd フィールドは USD です。</li></ul>**カンマで区切られた値**：これらのカンマは二重引用符 `"` の間に含まれます。例： |

</Accordion>

<div id="data-files" />

<Accordion title="データファイル">

データファイルはセグメンテーションタイプにより異なります。

<table><thead><tr><th>コンテンツ</th><th colspan="2">詳細</th></tr></thead><tbody><tr><td>完了フラグ</td><td colspan="2"><p>最終ファイル（完了）フラグは、対象の h フォルダの全てのデータが書き込まれたあとに設定されます。 </p><ul><li><p>_SUCCESS フラグが存在していることを確認してから、h フォルダ内のデータを読み込んでください。</p></li><li><p>_SUCCESS フラグは、特定のフォルダに書き込むデータがなく、フォルダが空である場合にも設定されます。 </p></li><li>注！アプリごとの分離オプションでは、フラグは各アプリフォルダごとではなく、h フォルダ内で設定されます。前のセクションの図を参照してください。 </li></ul></td></tr><tr><td>ファイルの種類</td><td colspan="2"><ul><li>データは、Snappy または GZIP圧縮ファイル、もしくはParquet 形式またはCSV形式の非圧縮ファイルで提供されます。</li><li>解凍後のデータファイルは、設定に応じてParquetまたはCSV形式で出力されます。</li></ul></td></tr><tr><td>列の並び（CSVファイル） </td><td colspan="2"><p>CSVファイルの場合、レポート項目の順序は常に同じです。新しい項目が追加される場合は、既存項目の右側に追加されます。 </p><p>この点に関して： </p><ul><li>ユーザー経路レポートの列の構成は同じです。つまり、異なるレポートタイプに対して同様のデータ読み込み手順を実行できます。レポートに含める項目を選択してください。 各項目の詳細・定義：<a href="/marketers/ja/docs/raw-data-field-dictionary" target="_blank">ローデータ項目の手引き</a> </li><li>レポート可用性セクションで、FFと表示されているレポートは、共通の列構造ではありません。 </li></ul></td></tr><tr><td>項目入力に関する考慮事項</td><td colspan="2"><p><strong>空白または空のフィールド：</strong> 一部の項目は <em>null</em> または空白になります。これは、特定のレポートのコンテキストでは、レポートするデータがないことを意味します。通常、<em>null</em> は、特定のレポートおよびアプリタイプのコンテキストでこの項目に値が入力されないことを意味します。空白（""）は、この項目がこのコンテキストに関連しているものの、入力するデータが見つからなかったことを意味します。 </p><p>制限付きメディアソースの場合、制限された項目の内容は null になります。  </p><p>一般的に、nullとブランクは同じものであり、利用可能なデータはありません。  </p><p><strong>タイムゾーンと通貨</strong></p><p>アプリ固有のタイムゾーンと通貨設定は、Data Locker に書き込まれるデータには影響しません。次のことが当てはまります。 </p><ul><li> <strong>time_zone</strong>日付と時間のデータはUTCです。</li><li> <strong>通貨：</strong>event_revenue_usd フィールドは USD です。</li></ul><p><strong>カンマで区切られた値</strong>：これらのカンマは二重引用符 `"` の間に含まれます。例：<code>`"iPhone6,1"`</code></p></td></tr></tbody></table>

</Accordion>

<div id="storage-options" />

<Accordion title="ストレージオプション">

* データは、選択したストレージ所有者に次のように書き込まれます。AWS、GCS、およびBigQuery。
* ストレージの選択はいつでも変更できます。
* ストレージを変更すると、次のことが起こります：
  * 新しく選択したストレージへの書き込みは1時間以内に開始します。
  * 7日間の移行期間中、既存のストレージへの書き込みを続行します。移行期間の有効期限がユーザーインターフェイスに表示されます。移行期間を使用して、データ読み込みプロセスを更新してください。
  * **バケットの変更**:バケットの変更：ストレージを変更した場合、7日間の移行期間中はデータは両方のバケットに送信され、データ取り込みプロセスを調整できます。

|  | パートナー所有のストレージ(GCS、AWS、BigQuery) |
| --- | --- |
| バケット名 | <ul><li>GCS：制限なし</li><li>AWS：広告主が設定します（プレフィックス af- が必要です）。</li></ul>例： `af-datalocker-your-bucket-name` |
| ストレージの所有者 | Partner |
| ストレージプラットフォーム | AWS、GCS、Yandex、BigQuery |
| データへアクセスするための認証情報 | AppsFlyerには開示されません。ストレージプロバイダーから提供される認証情報を使用してください。 |
| データ保持期間 | 御社による管理 |
| セキュリティ | 御社がストレージを管理します：<ul><li>**AWS：** AppsFlyerでは、バケットへのGetObject、ListBucket、DeleteObject、PutObject 権限が必要です。バケットはAppsFlyer専用にする必要があります。他の用途には使用しないでください。</li><li><Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor></li></ul> |

#### **セキュリティ担当者へのお知らせ：**

次の点を考慮してください：

* バケットまたはストレージ先は、AppsFlyer専用です。他の部門からそのバケットへのデータ書き込みは行わないでください。
* データを書き込まれた後25時間後に、バケット内のデータを削除できます。
* ストレージに書き込まれるデータは、当社のサーバーに既に存在しているデータのコピーです。データは、当社の保持ポリシーに従って引き続き当社のサーバーに格納されます。
* 技術的な理由により、データを削除したり書き換えたりすることがあります。この理由から、削除およびリスト権限が必要です。リストまたは削除は、あなたにとってセキュリティリスクではありません。リストの場合、我々はバケットに書き込む唯一の存在です。削除の場合、データを再生成できます。

</Accordion>

<div id="multipleconnection-principles-more-than-one-destination" />

<Accordion title="複数連携の仕様について（2つ以上の接続先設定）">

Data Lockerでは、一部または全てのデータを複数のディスティネーション（連携設定で定義）に送信することができます。例えば、アプリAのデータをAWSへ、アプリBのデータをGCSへ送信できます。

各連携に対して、ディスティネーションを含むData Lockerの設定を全て実行する必要があります。連携設定は互いに独立しています。

連携管理について、以下の点を考慮してください。

* Data Locker設定では、連携はタブに表示されます。各連携には独自の設定タブがあり、そこから連携を管理できます。デフォルトタブは「Data Locker」です。
* 新しい連携を作成する方法：
  1. **接続の追加**をクリックします。
  2. 連携の名前を入力し、ストレージの種類を選択してください。
  3. **保存**をクリックしてください。  
     保存したら、連携はデフォルトの「Data Locker」タブの隣に表示されます。各タブのアイコンはストレージの種類を示しています。
* 連携の詳細の確認、連携の複製、連携の削除を行うには、⋮ (オプション) をクリックしてください。

</Accordion>

## 手順

<div id="set-up-data-locker" />

<Accordion title="Data Lockerの設定">

この手順に従って、Data Lockerを設定します。なお、設定変更を行った後、機能が有効になるまで最大3時間かかる場合があります。

**前提条件：**

以下のいずれかのストレージの作業手順を完了してください。

* <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>バケット
* <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>バケット
* [Beta] <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor>バケット
* <Anchor target="_blank" href="/marketers/ja/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor>データウェアハウス

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Data Lockerの設定：**

1. AppsFlyerのパートナーアカウントで<Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">ログインしてください。</Anchor>
2. 管理画面内で以下に移動してください：
   * AdvertisersAppsFlyerでは、サイドバーから**エクスポート** >**データロッカー**.
   * マーケティングパートナーの場合： **アカウントメニューをクリックして、** Data Lockerへ進んでください。
3. <Anchor target="_blank" href="/marketers/ja/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">DataLockerのセットアップ手順</Anchor>のステップ3〜16に従ってください。

</Accordion>

## 追加情報

<div id="traits-and-limitations" />

<Accordion title="特徴と制限">

| **特性** | 備考 |
| --- | --- |
| アプリ固有のタイムゾーン | 不適用 |
| App-specific currency | サポートされておらず、計測対象外です |
| サイズ制限 | 不適用 |
| データ更新頻度 | データは、この記事内に記載されている個々のレポートデータの更新頻度に従って更新されます。 |
| 過去データ | サポートされておらず、計測対象外です |
| チームメンバーアクセス | チームメンバーは、管理画面上でData Lockerの設定を行うことができません。 |

</Accordion>

<div id="troubleshooting" />

<Accordion title="トラブルシューティング">

こちらの<Anchor target="_blank" href="/marketers/ja/docs/data-locker-for-marketers#troubleshooting">トラブルシューティングガイド</Anchor>をご確認ください。

</Accordion>

<div data-zendesk-anchors="data-locker-for-partners=data-locker%E9%80%A3%E6%90%BA%E6%B8%88%E3%81%BF%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91 h_01H8Y0DGS4Y2N99YNYEEJA6RSF=data-locker%E9%80%A3%E6%90%BA%E6%B8%88%E3%81%BF%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91 h_01H8Y0DGS4EM06PYNS1DRMZM6Y=data-locker-features h_01H8Y0DGS4A0MYGVZ9XQ49EBT2=reports-available-for-partners data-storage-architecture=%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%B8%E3%81%AE%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3 h_01H8Y0DGS4WTAJV7QE2DX3VGBP=%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%B8%E3%81%AE%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3 h_01H8Y0DGS4BQHBKNHZ4CD9ZMT4=overview h_01H8Y0DGS43JAREX23YX1F125K=folder-structure h_01H8Y0DGS524WNXY63351XGJKA=data-files h_01H8Y0DGS5MV6J1MMJJS8G4HC4=storage-options notice-to-security-officers=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E6%8B%85%E5%BD%93%E8%80%85%E3%81%B8%E3%81%AE%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B h_01H8Y0DGS5R4QX01WBK2S33QP5=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E6%8B%85%E5%BD%93%E8%80%85%E3%81%B8%E3%81%AE%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B h_01H8Y0DGS56GN6TVTSEV713DWQ=multipleconnection-principles-more-than-one-destination procedures=%E6%89%8B%E9%A0%86 h_01H8Y0DGS5588GQPZT7MQ686T3=%E6%89%8B%E9%A0%86 h_01H8Y0DGS57YK2PZ9ENZ80EWRJ=set-up-data-locker additional-information=%E8%BF%BD%E5%8A%A0%E6%83%85%E5%A0%B1 h_01H8Y0DGS5SYZRWFAXDSKE3YHX=%E8%BF%BD%E5%8A%A0%E6%83%85%E5%A0%B1 h_01H8Y0DGS540HK8MSCFYT9Q1RM=traits-and-limitations h_01H8Y0DGS55PJ7HV1PQ72XDDAB=troubleshooting" />
