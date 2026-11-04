---
title: 代理店向けのData Lockerレポート
metadata:
  keywords:
    - Agencies
    - Partners
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Data Locker
    - Agencies
  created_at: '2022-03-02T09:16:03Z'
  edited_at: '2026-10-14T09:31:04Z'
  id: 4543231254417
  locale: ja
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ja/articles/4543231254417
---
> **概要**：概要：本記事に記載されているレポートは、代理店向けのData Lockerにて利用可能なものです。なお、AppsFlyerからパートナーへデータを共有するには、本記事内に記載のように広告主（アプリの所有者）からパートナーへのデータアクセスの権限付与が必要です。

<div id="data-locker-reports-for-agencies" />

## 代理店向けのData Lockerレポート

以下に記載のデータ共有の原則が適用されます：

* 非オーガニックデータアトリビュートする必要があります。つまり、af\_prtのパラメータを使って成果を紐づけられているトラフィックです。
* オーガニックデータ広告主から明示的な権限付与が必要です。
* Data Locker広告主はサブスクリプションは必要ありません。
* [近日提供予定］他社へ紐付いた非オーガニックデータも今後提供予定です。

<div id="permissions-required-per-report-granted-by-the-advertiser" />

### レポート毎の広告主が必要な権限付与

レポート毎に必要な権限については以下の表を参照していただき、代理店側はまず広告主へ以下の作業を実施するよう依頼してください。

**広告主が代理店に権限を付与する方法**

1. この作業は、広告主アカウントのアドミンもしくは必要な権限を持っているチームメンバーであれば対応可能です。
2. AppsFlyer管理画面 左メニュー **連携**  > **連携済みパートナー**に移動します。
3. 連携パートナー（代理店）を選択してください。
4. **権限**タブへ進んでください。
5. 次の表をガイドとして、データアクセス権限を付与してください。データ共有ポリシーに従って権限を付与する必要があります。

<div id="reports-available-to-agencies" />

#### 代理店が利用できるレポート

<table><thead><tr><th><span>レポートの種類 (topic)</span></th><th>広告主からの付与が必要な権限</th><th><span>データの更新頻度\*</span></th></tr></thead><tbody><tr><td><a href="/marketers/ja/docs/cohort-analytics-via-data-locker" target="_blank">コホート全体</a></td><td><ul><li>［必須］リテンションとコホートレポートへのアクセス</li><li>集計オーガニックデータへのアクセス</li><li>［近日提供開始］他社へ紐付いたデータ</li></ul></td><td>毎日 </td></tr><tr><td><a href="/marketers/ja/docs/cohort-analytics-via-data-locker" target="_blank">コホートユーザー獲得</a></td><td><ul><li>［必須］リテンションとコホートレポートへのアクセス</li><li>集計オーガニックデータへのアクセス</li><li>[近日提供予定] 他社へ紐付いたデータ</li></ul></td><td>毎日</td></tr><tr><td><a href="/marketers/ja/docs/cohort-analytics-via-data-locker" target="_blank">コホートリターゲティング</a></td><td><ul><li>［必須］リテンションとコホートレポートへのアクセス</li><li>集計オーガニックデータへのアクセス</li><li>[近日提供予定] 他社へ紐付いたデータ</li></ul></td><td>毎日 </td></tr><tr><td colspan="3"><p>略語の意味</p><p><strong><span>デイリー</span></strong><span>：</span></p><ul><li><span>レポートは、h=23のフォルダに書き込まれます。</span></li><li><span>通常、これらのレポートは前日のh=23フォルダ内に格納され、日本時間の18:00-21:00 (09:00-12:00 UTC) までに利用できるようになります。</span></li><li><span>例えば、月曜日に発生したデータのレポートは月曜日のh=23のレポートに格納されます。</span></li><li> <span>そして、各データが取得可能になるのは火曜日 or 水曜日(日本時間)のそれぞれ以下時間です：</span><ul><li>キャンペーンの集約パフォーマンスレポート 10:00 UTC以降。</li><li>広告収益シグナル<span>の場合：21:00 UTC以降。</span> </li><li>ブロックされたクリックとインプレッション、失敗したクリック署名のデータ：<span>火曜日の16:00以降(日本時間) | 07:00 UTC07:00 UTC以降。</span> </li></ul></li></ul></td></tr></tbody></table>

<div data-zendesk-anchors="data-locker-reports-for-agencies=%E4%BB%A3%E7%90%86%E5%BA%97%E5%90%91%E3%81%91%E3%81%AEdata-locker%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HE7RC367DWWDQHAVFSKV6VEK=%E4%BB%A3%E7%90%86%E5%BA%97%E5%90%91%E3%81%91%E3%81%AEdata-locker%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 permissions-required-per-report-granted-by-the-advertiser=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E6%AF%8E%E3%81%AE%E5%BA%83%E5%91%8A%E4%B8%BB%E3%81%8C%E5%BF%85%E8%A6%81%E3%81%AA%E6%A8%A9%E9%99%90%E4%BB%98%E4%B8%8E h_01HE7RC367NTSVESAYE69Q7NJY=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E6%AF%8E%E3%81%AE%E5%BA%83%E5%91%8A%E4%B8%BB%E3%81%8C%E5%BF%85%E8%A6%81%E3%81%AA%E6%A8%A9%E9%99%90%E4%BB%98%E4%B8%8E reports-available-to-agencies=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%8C%E5%88%A9%E7%94%A8%E3%81%A7%E3%81%8D%E3%82%8B%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88 h_01HE7RC368VVM3SMDN7S8YV6DY=%E4%BB%A3%E7%90%86%E5%BA%97%E3%81%8C%E5%88%A9%E7%94%A8%E3%81%A7%E3%81%8D%E3%82%8B%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88" />
