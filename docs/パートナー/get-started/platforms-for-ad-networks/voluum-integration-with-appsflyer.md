---
title: AppsFlyerとTealiumの連携
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
  created_at: '2016-01-11T14:46:09Z'
  edited_at: '2026-10-14T09:26:10Z'
  id: 207274016
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/207274016
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

AppsFlyer の全パラメーターリストについては、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">こちらをクリック</Anchor>してください

<div id="complete-attribution-link-template" />

### 完全なアトリビューションリンクテンプレート

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### インストールとアプリ内イベントのポストバック

グローバルインストールポストバック：

```http
https://{Company-Domain}.voluumtrk.com/postback?cid={clickid}
```

グローバルアプリ内イベントポストバック：

```http
https://{Company-Domain}.trackvoluum.com/postback?cid={clickid}&payout={monetary}&txid={event-name}
```

<div id="appsflyers-in-app-event-dashboard" />

### AppsFlyer のアプリ内イベント管理画面

<Image align="center" alt="Voluum_msc_new_1.png" src="https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png" />
リクエストに応じて、国コード、広告ID、IDFA などのアトリビューション情報をポストバックに追加できます。

<div id="finalizing-your-registration" />

## 登録の完了

* AppsFlyerとパートナー連携を行う場合、まずは <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">こちら</Anchor>からパートナー申請を行ってください。

<div data-zendesk-anchors="starting-the-integration=%E9%80%A3%E6%90%BA%E3%82%92%E9%96%8B%E5%A7%8B%E3%81%99%E3%82%8B 01JFT0VZZ5KVMKYRD222JT55NH=%E9%80%A3%E6%90%BA%E3%82%92%E9%96%8B%E5%A7%8B%E3%81%99%E3%82%8B complete-attribution-link-template=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 01JFT0VZZ7B1RRY82B65GWF4P7=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 install-and-inapp-event-postbacks=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT0VZZ86KYXSVE1QBD2V0HF=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF appsflyers-inapp-event-dashboard=appsflyer-%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 01JFT0VZZ9A4JWG38KPH0CNQ72=appsflyer-%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 finalizing-your-registration=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86 01JFT0VZZATFYY75QPCPKZF3S6=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86" />
