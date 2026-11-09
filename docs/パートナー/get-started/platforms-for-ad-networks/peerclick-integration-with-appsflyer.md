---
title: PeerClick と AppsFlyer の連携
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2024-01-07T08:27:18Z'
  edited_at: '2026-10-14T09:39:31Z'
  id: 21479841979793
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/21479841979793
---
> **概要：** PeerClick を使用するアドネットワークは、AppsFlyer の確率論的モデリングソリューションを活用して、インストールやアプリ内イベントに関するアトリビューションデータを受け取ることができます。

<div id="starting-the-integration" />

## 連携を開始する

連携を開始するには、レポート用に AppsFlyer にアトリビューションリンクとポストバックの両方を送信する必要があります。

以下に、各パラメーターの詳細な説明を含む基本アトリビューションリンクを示します。

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| AppsFlyer ベース URL | 説明 |
| --- | --- |
| https://app.appsflyer.com | AppsFlyer エンドポイント |
| app\_id | アプリケーション固有 ID - プロモートされたアプリごとに動的値が変更されます |
| pid= |  |
| c= | キャンペーン名 |

**推奨アトリビューションリンクパラメーター：**

| AppsFlyer のパラメーター | ボリュームマクロ | 説明 |
| --- | --- | --- |
| &clickid= | clickid | ユーザーセッションの一意のトランザクション ID -**必須** |
| &af\_siteid= | `{trafficsource.id}` | トラフィックソースの ID -**オプション** |

<div id="note" />

> 📘 **注**
>
> * AppsFlyer の全パラメーターリストについては、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">こちらをクリック</Anchor>してください
> * PeerClick の全リストについては、<Anchor target="_blank" href="https://help-center.peerclick.com/en/">こちらをクリック</Anchor>してください

<div id="complete-attribution-link-template" />

### 完全なアトリビューションリンクテンプレート

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### インストールとアプリ内イベントのポストバック

**グローバルインストールポストバック：**

```http
https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}
```

**グローバルアプリ内イベントポストバック：**

`https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}&payout={monetary}&txid={event-name}`

* PeerClick によって提供されたユーザー ID
* アプリからの実際のアプリ内イベント名。広告主が各アプリの AppsFlyer 管理画面で**イベントタグ**として設定したもの

<div id="appsflyers-in-app-event-dashboard" />

### AppsFlyer のアプリ内イベント管理画面

<Image align="center" alt="Voluum_msc_new_1.png" src="https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png" />
リクエストに応じて、国コード、広告ID、IDFA などのアトリビューション情報をポストバックに追加できます。

<div data-zendesk-anchors="starting-the-integration=%E9%80%A3%E6%90%BA%E3%82%92%E9%96%8B%E5%A7%8B%E3%81%99%E3%82%8B h_01HKHFT3RFWF5H349GP7MHDAYX=%E9%80%A3%E6%90%BA%E3%82%92%E9%96%8B%E5%A7%8B%E3%81%99%E3%82%8B h_01HM8M27S5WFJVKBG0JAFW548H=%E6%B3%A8 complete-attribution-link-template=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 h_01HKHFT3RFDW6GZM3E72SYPJSD=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 install-and-inapp-event-postbacks=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF h_01HKHFT3RF1PTSJ4SF9RTQ93N8=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF appsflyers-inapp-event-dashboard=appsflyer-%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 h_01HKHFT3RFDVPCSKJGZPRFB55V=appsflyer-%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2" />
