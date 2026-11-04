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
  created_at: '2016-01-11T14:46:45Z'
  edited_at: '2026-10-14T09:36:24Z'
  id: 207583573
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/207583573
---
> **概要：** PeerClick を使用するアドネットワークは、AppsFlyer の確率論的モデリングソリューションを活用して、インストールやアプリ内イベントに関するアトリビューションデータを受け取ることができます。


<span id="basic-attribution-link"></span>以下に、各パラメーターの詳細な説明を含む基本アトリビューションリンクを示します。

```http
https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}
```

| AppsFlyer ベース URL | 説明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id | アプリケーション固有 ID - プロモートされたアプリごとに動的値が変更されます |
| pid |  |
| c | キャンペーン名 |

**推奨アトリビューションリンクパラメーター：**

| AppsFlyer のパラメーター |  | 説明 |
| --- | --- | --- |
| clickid | `{TID}` |  |
| af\_siteid | `{SC}` |  |

AppsFlyer の全パラメーターリストについては、<Anchor target="_blank" href="/partners/ja/docs/postback-macros-for-ad-networks">こちらをクリック</Anchor>してください

完全なアトリビューションリンクテンプレート

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={TID}&af_siteid={ADV_SID}
```

<div id="install-and-in-app-event-postbacks" />

### インストールとアプリ内イベントのポストバック

グローバルインストールポストバック：

```
https://tracking.zadsmobile.com/pb?tid={TID}
```

<div id="finalizing-your-registration" />

## 登録の完了

* AppsFlyerとパートナー連携を行う場合、まずは <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">こちら</Anchor>からパートナー申請を行ってください。

<div data-zendesk-anchors="01JFT0DX287AWQND2BYFSV50HW=basic-attribution-link install-and-inapp-event-postbacks=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT0DX2B6FFE3K7VTXG1YVJ1=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF finalizing-your-registration=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86 01JFT0DX2BD8A19BY9197X11QW=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86" />
