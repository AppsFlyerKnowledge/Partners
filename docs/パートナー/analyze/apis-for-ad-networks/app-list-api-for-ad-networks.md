---
title: アプリリストAPI：アドネットワーク向け
metadata:
  keywords:
    - API
    - Ad Networks
    - Partners
    - Developers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-08-06T20:11:15Z'
  edited_at: '2026-10-14T09:27:06Z'
  id: 360011700857
  locale: ja
  section: APIs for ad networks
  section_id: 6551618728209
  url: https://support.appsflyer.com/hc/ja/articles/360011700857
---
> **概要：** 概要： アドネットワークは、自分の連携済みパートナーアカウントに紐付けられている広告主アプリのメタデータを取得できます。

## アプリリストの取得API

以下のセクションにて、APIを使用するために必要な情報を記載しています。

<div id="get-app-list-basics" />

<Accordion title="アプリリスト基本情報の取得">

<table><thead><tr><th>カテゴリ</th><th>アイテム</th><th><p><span>説明</span></p></th></tr></thead><tbody><tr><td rowspan="3">リクエスト</td><td>HTTP メソッド</td><td><code>GET</code></td></tr><tr><td>経路</td><td><p><span>https://hq1.appsflyer.com/api/mng/apps</span></p></td></tr><tr><td>認証ヘッダー  </td><td><ul><li>認証ヘッダーには、Bearerトークンを含める必要があります。  </li><li>管理者ユーザーは、次のようにダッシュボードでトークンを取得します。<a href="/marketers/ja/docs/managing-appsflyer-tokens" target="_blank">管理者はメールドロップダウンリスト &gt; API トークンの順で移動し、V2.0 トークンを取得します</a> </li></ul></td></tr><tr><td rowspan="3"><p> レスポンス</p>  </td><td><p>結果</p></td><td><p>JSON 形式で返されます</p></td></tr><tr><td>リクエスト制限</td><td><ul><li>20リクエスト / 分</li><li>100リクエスト / 日</li></ul></td></tr><tr><td>レコード数の制限</td><td><p>1リクエストにつき、1,000レコードまで取得可能です。1000以上のレコードが返される場合には、この記事内で紹介されているページネーションのリクエストを使用してください。</p></td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="API リクエスト">

API リクエストは、メソッド、経路、必須の機能パラメーター、オプションのページネーションパラメーターで構成されています。また、API トークンは認証ヘッダーに含まれます。

**メソッド**

```http
GET https://hq1.appsflyer.com/api/mng/apps?capabilities={capabilities} 
```

#### 必須パラメーター

<Table>
  <thead>
    <tr>
      <th>
        クエリパラメーター
      </th>
      <th>
        説明
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        機能
      </td>
      <td>
        アクセス許可と連携権限を持っているアプリの一覧と数を取得するには、以下に記載されている機能パラメーターを設定してください。

        | 任意 | タイプ | 説明 |
        | --- | --- | --- |
        | `protect_360` | レポート権限 | <Anchor target="_blank" href="/partners/ja/docs/protect360-for-integrated-partners">アドネットワーク向けのProtect360のローデータレポート</Anchor> の取得権限 |
        | `cost` | 統合 | <Anchor target="_blank" href="/partners/ja/docs/incost-api-for-ad-networks">InCost API経由</Anchor>でのコストデータ取得が有効になっている状態 |

        **例：**
      </td>
    </tr>
  </tbody>
</Table>

#### **ページネーションの仕組みについて**

随時機能するページネーションの仕組みが実装されています。

**ページネーションの仕様：**

* リクエスト(ページ)毎に最大1,000レコードまで返します。
* レスポンスJSON には、以下のページネーション関連のキーが含まれています：
  * **meta.total\_items**:全ページ合算でのレコード数です。これはあなたが 機能 権限を付与されているアプリの数を示しています。
  * ページネーションリンク(下記 JSON を参照)には、以下のキーが含まれます：  
    * **links.prev**:それよりも前のリクエストがあった場合 - 前のページを生成するために使用されたリクエストが入ります。
    * **links.self**:現在のリクエスト：現在の JSON （ページ）を生成するために使用されたリクエスト
    * **links.next**:次のページを取得するためのリクエストです。次へのキーがない場合は、これが最終ページです。

**次のいずれかのページネーションの制御方法を使用してください。**

* [ベストプラクティス] JSON 内のリンクを使用する：links.next キーが存在する場合は、それを使用して次のページを取得するリクエストを作成します。links.nextのkeyがないJSONを受け取るまでは、この作業を続けてください。
* limitとoffsetのパラメータをtotal\_itemsのkeyを組み合わせたプログラムを実装してください。

**ページネーションリンク JSON の例**

* 次の例は、最初のリクエストの結果を含んでおり、データセクション（非表示）に2つのレコードを含む2番目のリクエストで構成されています。
* 返されるレコードの総数は6です。
* **links.next**のkeyには次のページ（レコード5と6）を返すリクエストが含まれています。

```json
{                                                                                         
    "data": {[...]},   
    "meta": {
        "total_items": 6
    },
    "links": {
        "prev": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=2",
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=2&limit=2",
        "next": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=4&limit=2"
    }
}
```

#### ページネーション機能のパラメータ（任意）

<table><tbody><tr><th><p>クエリパラメーター</p></th><th>説明</th></tr><tr><td>limit</td><td><p>コール毎に返されるレコード数</p><ul><li>最大値：2024-02-26</li><li> <code>limit</code>を送信しない場合、自動的に1,000に設定されます。</li><li>例： <code>limit=2</code> </li><li>必須：いいえ</li></ul></td></tr><tr><td>offset</td><td><p>コールで返される最初のレコードです。レコード番号は0から始まります。 </p><ul><li> <code>offset</code>を送信しない場合、自動的に0に設定されます。</li><li>例：<code>offset=2</code> </li><li>必須：いいえ</li></ul></td></tr><tr><td colspan="2"> </td></tr></tbody></table>

</Accordion>

<div id="json-response" />

<Accordion title="JSON レスポンス">

| **キー** | **説明** |
| --- | --- |
| id | アプリ ID (例:`id123456789`id123456789, `com.myapp.com`com.myapp.com |
| type | 常に戻る `app` |
| 名称 | App name |
| platform | iOS or Android が返されます。 |
| currency | 広告主側で設定した、アプリ固有の通貨単位が返されます。 |
| time\_zone | 広告主側で設定した、アプリ固有のタイムゾーン設定が返されます。 |
| total\_items | アドネットワークがリクエストした機能オプションを持っているアプリの数が返されます。 |
| links | ページネーション機能（パラメーターのセクションを参照してください）<ul><li>prev: 前のページを生成するために使用されたコールが返されます。</li><li>self: そのページを生成するために使用されたコールが返されます。</li><li>next: 次のページを生成するために使用するコールが返されます。</li></ul> |

</Accordion>

<div id="get-app-list-curl-example-and-response" />

<Accordion title="アプリリスト取得のCurlの例とそのレスポンス">

**Curl リクエスト**

この例は、任意のページネーションパラメーターを含む完全なコール内容が記載されています。

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&limit=1000&offset=0' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**JSON レスポンス**

```json
{
    "data": [
        {
            "id": "com.appsflyer.xpend_qa1",
            "type": "app",
            "attributes": {
                "name": "com.appsflyer.xpend_qa1",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC"
            }
        },
        {
            "id": "com.abc.app",
            "type": "app",
            "attributes": {
                "name": "com.abc.app",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC",
                "enable_retargetting": true
            }
        },
        {
            "id": "com.xyz.app",
            "type": "app",
            "attributes": {
                "name": "com.xyz.app",
                "platform": "android",
                "currency": "JPY",
                "time_zone": "UTC"
            }
        }
    ],
    "meta": {
        "total_items": 3
    },
    "links": {
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=1000"
           }
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="HTTP のレスポンスコード">

| コード | メッセージ | 備考 / トラブルシューティング |
| --- | --- | --- |
| 200 | OK | 有効なデータが返されました |
| 200 | OK | **症状**：データ返却なし<br /><br />**アクション**：bearer ヘッダー内に認証トークンがあることを確認してください。 |
| 400 | Bad request | <ul><li>JSON内に含まれているメッセージを確認してください。</li><li>JSONが空の場合：正しくない機能が指定されている状況です。</li></ul> |
| 401 | Unauthorized | **メッセージ**：認証トークンの形式が正しくありません<br /><br />正しいトークンであることを確認してください。トークン文字数は700字以上です。 |
| 404 | Not found | <ul><li>ネットワークやファイアウォールに関する問題を処理してください。</li><li>AppsFlyer の<Anchor target="_blank" href="/marketers/ja/docs/appsflyer-server-ip-address-ranges-allowlisting">IP アドレスが許可リストに登録されていること</Anchor>を確認してください</li><li>必ず直近に発行された最新のトークンを使用してください。</li><li>データが見つかりませんでした：データが見つかりません：リクエストした権限や連携のタイプは有効ですが、アクセス許可のあるアプリが見つかりませんでした。</li></ul> |
| 429 | Too many requests | レート制限を超えました |

</Accordion>

<div data-zendesk-anchors="get-app-list-api=%E3%82%A2%E3%83%97%E3%83%AA%E3%83%AA%E3%82%B9%E3%83%88%E3%81%AE%E5%8F%96%E5%BE%97api get-app-list-mandatory-parameters=%E5%BF%85%E9%A0%88%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC pagination-mechanism=%E3%83%9A%E3%83%BC%E3%82%B8%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E4%BB%95%E7%B5%84%E3%81%BF%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 pagination-mechanism-parameters-optional=%E3%83%9A%E3%83%BC%E3%82%B8%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E6%A9%9F%E8%83%BD%E3%81%AE%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E4%BB%BB%E6%84%8F" />
