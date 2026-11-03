---
title: ブロックされたデータのポストバック
metadata:
  keywords:
    - fraud
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
  created_at: '2017-09-19T07:03:47Z'
  edited_at: '2026-10-14T09:32:47Z'
  id: 115004744123
  locale: ja
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ja/articles/115004744123
---
> **概要：** 概要： 連携済みパートナーは、広告や検証ルールの違反によって、除外されたインストールとアプリ内イベントのポストバックを受け取ることが可能です。

## 広告不正と検証ルールによって除外された計測データのポストバック

**用語**：

* **不正イベント:** Protect360 によってブロックされたインストールイベントとアプリ内イベント
* **非準拠のイベント**：検証ルールの内容を満たしていないインストールとアプリ内イベント
* 紐付けを修正されたインストール： 検知・ブロックされたハイジャックインストールの紐付けは、ブロック後に修正され、正しい本来のメディアソースに成果が計測されます。

**Postbacks**

* 連携済みパートナーはブロックされたイベントのポストバックをリアルタイムに受け取ることが可能です。
* その中には、アトリビューションを修正されたインストールに紐付くアプリ内イベントのポストバックは含まれません。
* * Block reason (ブロックされた理由)
  * Reject sub-reason（ブロックされた詳細な理由）
  * Is-rejected
  * Reject reason value (詳細な値 / 利用可能な場合)例： `reject_reason=site_blacklist&reject_reason_value="1123456"&is_rejected=1`

以下の表で、Reject reason(ブロック理由)とReject reason valueにそれぞれどのような値が入ってくるかと、その詳細を記載しています。

| Reject reason | Reject reason value | 任意設定可能 | 概要 |
| --- | --- | --- | --- |
| ctit\_anomalies | 広告クリックから初回起動までの秒数 | **x** | CTIT anomalies(CTIT異常)とは、不可解なCTIT(広告クリックから初回起動までの時間)に基づいてブロックされたクリックが原因です。 |
| store\_install\_validation | N/A | **x** | AppStoreとの成果検証に失敗したインストールです。 |
| サイトブラックリスト | Site ID | **x** |  |
| ボット | N/A | **x** | Botに偽装行為をブロックしたインストールです。 |
| クリックフラッド | Site IDor空欄 | **x** | 長いCTITとコンバージョン率の低いインストールが多数発生していたため、AppsFlyerによってブロックされたクラスターからのインストール |
| 行動の異常 | N/A | **x** | インストール後のアプリ内での挙動に一貫性がなく、異常な挙動が検知された場合のインストールです。 |
| インストールハイジャック | N/A | **x** | 不可解なCTIT(広告接触から初回起動までの時間が極端に短いなど)の情報やGoogle Play Server-Side APIの情報を基にブロックされたインストールです。 |
| 検証ボット |  | ✓ | 広告主側で定義したルール |
| 検証ハイジャック |  | ✓ | 広告主側で定義したルール |
| ai\_layer | N/A | **x** | AIモデルを使用して、大量のデータポイントを分析し、不正なデバイスとインストール活動を検知する能力を強化します。 |

#### アプリ内イベント向けのブロック理由

| Reject reason | Reject reason value | 概要 |
| --- | --- | --- |
| インストールに基づく | インストールに基づく | 初回のインストールが<Anchor target="_blank" href="/marketers/ja/docs/protect360-raw-data-reports#ブロック理由">インストール</Anchor>または拒否リストレベルの理由で偽物として識別されました |
| アプリ内ボット | 偽のデバイスパラメータ | AppsFlyerのアルゴリズムが不正を検出しました |
| アプリ内検証 | invalid\_event\_name | 要求または手動で定義された検証ルールに基づく |
| アプリ内検証 | invalid\_event\_value | 要求または手動で定義された検証ルールに基づく |
| アプリ内検証 | ルール名 | 広告主側でマニュアルで定義したルール |

> 🚧 **重要！**
>
> * * `is-rejected`
>   * `blocked-reason`
>   * `blocked-sub-reason`
>   * `blocked-reason-value`

<div data-zendesk-anchors="rejected-attribution-postbacks-relating-to-fraud-and-validation-rules=%E5%BA%83%E5%91%8A%E4%B8%8D%E6%AD%A3%E3%81%A8%E6%A4%9C%E8%A8%BC%E3%83%AB%E3%83%BC%E3%83%AB%E3%81%AB%E3%82%88%E3%81%A3%E3%81%A6%E9%99%A4%E5%A4%96%E3%81%95%E3%82%8C%E3%81%9F%E8%A8%88%E6%B8%AC%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01J5597AMDVWR2KTANSF7Y7T4P=%E5%BA%83%E5%91%8A%E4%B8%8D%E6%AD%A3%E3%81%A8%E6%A4%9C%E8%A8%BC%E3%83%AB%E3%83%BC%E3%83%AB%E3%81%AB%E3%82%88%E3%81%A3%E3%81%A6%E9%99%A4%E5%A4%96%E3%81%95%E3%82%8C%E3%81%9F%E8%A8%88%E6%B8%AC%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF reject-reasons-for-inapp-events=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%90%91%E3%81%91%E3%81%AE%E3%83%96%E3%83%AD%E3%83%83%E3%82%AF%E7%90%86%E7%94%B1 h_01J5597AMDHT5GJQN7QJZKV41F=%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%90%91%E3%81%91%E3%81%AE%E3%83%96%E3%83%AD%E3%83%83%E3%82%AF%E7%90%86%E7%94%B1 h_01J5597AMD29TAZSKZS9WTFSM5=%E9%87%8D%E8%A6%81" />
