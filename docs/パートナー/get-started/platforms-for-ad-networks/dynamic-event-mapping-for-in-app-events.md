---
title: アプリ内イベントの動的なイベントマッピング
metadata:
  keywords:
    - In-App
    - Mapping
    - Dynamic Event Mapping
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
  created_at: '2016-05-26T08:48:23Z'
  edited_at: '2026-10-14T09:33:30Z'
  id: 208996726
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/208996726
---
> **概要：** 概要： TUNEやCAKEといったパートナーがGoal IDに基づいて１つのアプリ内イベントを異なるポストバックで受け取ることができるように、計測リンクを設定しましょう。

<div id="introduction" />

## はじめに

Goal IDに基づいて、１つのアプリ内イベントについて異なるイベントポストバックを送信することが可能です。

この機能は、HasOffersやCAKE、または１つのアプリ内イベントに対して異なるアプリ内イベントのポストバックを受け取りたいパートナーでサポートされています。

管理画面上の［連携済みパートナー］ページにおいて、広告主は実装したアプリ内イベントを各パートナーの適切な動的なイベントタグにマッピングすることになります。イベントタグには、アプリ内イベントとブロックされたアプリ内イベントの両方が含まれます。

動的なイベントタグは、クリックURLに設置された値に基づいてポストバック時にアドネットワークへ送信されます。

<div id="attribution-link" />

## 計測リンク

<div id="attribution-link-example" />

> 📄 **計測リンクの例**
>
> ：
>
> ```http
> https://app.appsflyer.com/com.xyz.abc?pid=mediasource_int&clickid={transaction_id}
> &goalid_1={XXX}&goalid_2={YYY}
> ```

広告主は、アドネットワークの案内に従ってアプリ内イベントの項目（下記参照）ですべてのgoal\_idをマッピングする必要があります。

以下の例では、level20\_finishedのイベントは$$click(goalid\_1)としてマッピングされ、level25\_finishedのイベントは$$click(goalid\_2)としてマッピングされています。

以下の設定のとき、アプリユーザーがレベル20に到達すると、AppsFlyerは計測URLクリック時にgoalid\_1のパラメータに渡されたXXXの値を載せてイベントのポストバックを送信します。

もし同じユーザー、もしくは別のユーザーがレベル25に到達した場合には、AppsFlyerは計測URLクリック時にgoalid\_2のパラメータに渡されたYYYの値を載せてイベントのポストバックを送信します。

![Goadid.png](https://files.readme.io/35390305a93cc7a49f193fa1667b491827736252a9133bc01d01c07dfdc38586-360001400478.png)

<div data-zendesk-anchors="introduction=%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB attribution-link=%E8%A8%88%E6%B8%AC%E3%83%AA%E3%83%B3%E3%82%AF" />
