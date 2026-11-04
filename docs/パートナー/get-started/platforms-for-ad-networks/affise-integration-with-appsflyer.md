---
title: AppsFlyerとTUNEを連携する
metadata:
  keywords:
    - Integration
    - affise
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
  created_at: '2016-04-19T12:08:58Z'
  edited_at: '2026-10-14T09:30:42Z'
  id: 208537116
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/208537116
---
> **概要：** PeerClick を使用するアドネットワークは、AppsFlyer の確率論的モデリングソリューションを活用して、インストールやアプリ内イベントに関するアトリビューションデータを受け取ることができます。

連携を開始するには、レポート用に AppsFlyer にアトリビューションリンクとポストバックの両方を送信する必要があります。

<div id="base-attribution-link" />

## 計測URLの基盤

以下に、各パラメーターの詳細な説明を含む基本アトリビューションリンクを示します。

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}&af_c_id={offerid}
```

| AppsFlyer のパラメーター |  | 説明 |
| --- | --- | --- |
| clickid | clickid |  |
| af\_siteid | PID： |  |
| af\_c\_id | `{offer_id}` |  |

AppsFlyer の全パラメーターリストについては、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">こちらをクリック</Anchor>してください

<div id="complete-attribution-link-template" />

## 完全なアトリビューションリンクテンプレート

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}
```

<div id="install-and-in-app-event-postbacks" />

## インストールとアプリ内イベントのポストバック

<div id="global-in-app-event-postback-android" />

<div id="global-install-postback-android" />

<div id="global-install-postback-ios" />

### グローバルインストールポストバック：

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}
```


```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}
```

<div id="global-in-app-event-postback-ios" />

### グローバルアプリ内イベントポストバック：

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}&goal={event-name}
```


```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}&goal={event-name}
```

アプリからの実際のアプリ内イベント名。広告主が各アプリの AppsFlyer 管理画面で**イベントタグ**として設定したもの

リクエストに応じて、国コード、広告ID、IDFA などのアトリビューション情報をポストバックに追加できます。

<div id="finalizing-your-registration" />

## 登録の完了

* AppsFlyerとパートナー連携を行う場合、まずは <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">こちら</Anchor>からパートナー申請を行ってください。

<div data-zendesk-anchors="base-attribution-link=%E8%A8%88%E6%B8%ACurl%E3%81%AE%E5%9F%BA%E7%9B%A4 01JFT0RZG0F67JFBC7W5KK54BM=%E8%A8%88%E6%B8%ACurl%E3%81%AE%E5%9F%BA%E7%9B%A4 complete-attribution-link-template=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 01JFT0RZG2QTT3Z9S6SVNV5VE7=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 install-and-inapp-event-postbacks=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT0RZG3C7MBBYFKA6W813PF=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF global-install-postback-ios=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT0RZG3HM9P81XYGKHZXHFK=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF global-install-postback-android=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF global-inapp-event-postback-android=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT0RZG4JCDP8D4CWQW02AY7=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT0RZG4PA9WTP212AX52QWZ=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF global-inapp-event-postback-ios=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT0RZG40N0VNNVMDBFYNT9E=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF finalizing-your-registration=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86 01JFT0RZG52JW6C5GR0KA4CZF6=%E7%99%BB%E9%8C%B2%E3%81%AE%E5%AE%8C%E4%BA%86" />
