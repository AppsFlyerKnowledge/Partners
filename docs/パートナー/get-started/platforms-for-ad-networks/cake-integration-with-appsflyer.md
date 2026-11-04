---
title: AppsFlyerとTUNEを連携する
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
  created_at: '2016-01-11T14:44:55Z'
  edited_at: '2026-10-14T09:33:44Z'
  id: 207273986
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/207273986
---
> **概要：**

<div id="base-attribution-link" />

## 計測URLの基盤

以下に、各パラメーターの詳細な説明を含む基本アトリビューションリンクを示します。

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| AppsFlyer ベース URL | 説明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id | アプリケーション固有 ID - プロモートされたアプリごとに動的値が変更されます |
| pid |  |
| c | キャンペーン名 |

<div id="recommended-attribution-link-parameters" />

### 推奨アトリビューションリンクパラメーター：

| AppsFlyer のパラメーター |  | 説明 |
| --- | --- | --- |
| clickid |  |  |
| af\_siteid | #affid# |  |

AppsFlyer の全パラメーターリストについては、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">こちらをクリック</Anchor>してください

<div id="complete-attribution-link-template" />

### 完全なアトリビューションリンクテンプレート

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#oreqid#
```

<div id="install-and-in-app-event-postbacks" />

## インストールとアプリ内イベントのポストバック

<div id="global-install-postback" />

### グローバルインストールポストバック：

```http
https://{company-domain}.com/p.ashx?f=pb&r=(Click-ID)
```

<div id="global-in-app-event-postback" />

### グローバルアプリ内イベントポストバック：

```http
Click-ID
```

アプリからの実際のアプリ内イベント名。広告主が各アプリの AppsFlyer 管理画面で**イベントタグ**として設定したもの


![IAEP.png](https://files.readme.io/3ce734c3930649fdb0b119cd6e12e135e6bcba19225862e9e93b93991451fc8b-360002326529.png)

<span id="appsflyer-in-app-events-dashboard"></span><span id="appsflyer-inapp-events-dashboard"></span>リクエストに応じて、国コード、広告ID、IDFA などのアトリビューション情報をポストバックに追加できます。

<div id="finalizing-your-registration" />

## 登録の完了

* AppsFlyerとパートナー連携を行う場合、まずは <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">こちら</Anchor>からパートナー申請を行ってください。

<div data-zendesk-anchors="base-attribution-link=%E8%A8%88%E6%B8%ACurl%E3%81%AE%E5%9F%BA%E7%9B%A4 01EZPMKP0AFM26H2ZG9FY1D2S4=%E8%A8%88%E6%B8%ACurl%E3%81%AE%E5%9F%BA%E7%9B%A4 recommended-attribution-link-parameters=%E6%8E%A8%E5%A5%A8%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC 01EZPMKP0A7DBV5KAGZ08C3R49=%E6%8E%A8%E5%A5%A8%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC complete-attribution-link-template=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 01EZPMKP0AH1MB0XYE3PXQPP0V=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 install-and-inapp-event-postbacks=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01EZPMKP0A2D0PB41GD04HX9JX=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF global-install-postback=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01EZPMKP0AVAJRP8YM48T4GV47=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF global-inapp-event-postback=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01EZPMKP0AM7JD7HWW7BCJDQF3=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01EZPMKP0AJTYT0G9E8G833KT0=appsflyer-inapp-events-dashboard finalizing-your-registration=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86 h_01HY03H1PMWZX3T12RZFV15CFE=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86" />
