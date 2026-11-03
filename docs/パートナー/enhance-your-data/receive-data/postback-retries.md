---
title: ポストバックの再送信
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
  created_at: '2018-08-06T04:59:54Z'
  edited_at: '2026-10-14T09:25:53Z'
  id: 360001376085
  locale: ja
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ja/articles/360001376085
---
> **概要：** 概要： AppsFlyerでのポストバックの再送信の仕組みと、パートナー側でのポストバックの受け取りの仕組みをどのように構成するべきかを説明しています。

## はじめに

各パートナーへのポストバックは、AppsFlyerとパートナーとの連携において非常に重要な機能です。どんなシステムでもレスポンスに関する一時的な問題が発生する可能性があるため、AppsFlyerでは失敗したポストバックを再送信する機能を用意しています。

## 重要な情報

<div id="when-does-appsflyer-retry-a-failed-postback" />

<Accordion title="失敗したポストバックをAppsFlyerが再送信するのはいつ？">

受け取り側のサーバーレスポンスが5XXのエラーであった時に、ポストバックが再送信されます。

</Accordion>

<div id="how-often-does-appsflyer-retry-a-failed-postback" />

<Accordion title="失敗したポストバックをAppsFlyerが再送信する頻度は？">

失敗したポストバックは、15分間隔で最大4回まで再送信されるため、合計で1つのポストバックは最大5回まで送信される可能性があります。

</Accordion>

<div id="can-retried-postbacks-be-identified-in-postback-reports" />

<Accordion title="再送信されたポストバックであることは、ポストバックレポート内で識別可能？">

ローデータポストバックレポート最初に送信されたポストバックの場合には、この列の値は空欄で入力され、その後の再送信されたポストバックの場合には、この列にTRUEの値が入力されます。

</Accordion>

<div id="how-can-a-partner-identify-the-total-eventual-failed-postbacks-in-the-postback-report" />

<Accordion title="最終的に失敗したポストバックの総数を、ポストバックレポート内で確認することは可能？">

"Postback Retry"の列に合計4つの"TRUE"の値があり、Postback HTTP Response Codeにエラーコードを含んでいるポストバックデータは、パートナーへの送信が完全に失敗したものになります。

</Accordion>

<div id="is-there-anything-special-a-partner-should-consider-about-retried-postbacks" />

<Accordion title="再送信されたポストバックに関して、パートナーが考慮しなければいけない特別な注意点は？">

ポストバックがパートナー側のシステムに送信され正常に処理される、サーバーレスポンスの送信にエラーまたは遅延があった場合には、結果的にポストバックが失敗したとみなされ、15分後にポストバックを再送信します。これにより、パートナー側でデータの重複が発生する可能性があるため、パートナー側でも重複除外のメカニズムを実装していただく必要があります。

</Accordion>

<div id="are-postback-retries-automatically-enabled-for-all-partners" />

<Accordion title="ポストバックの再送信の機能は、自動的に有効になっている？">

いいえ、ポストバックの再送信の機能を有効にしたい場合には、担当PDMに連絡してこの機能を有効にしてもらってください。

</Accordion>

<div data-zendesk-anchors="introduction=%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB important-information=%E9%87%8D%E8%A6%81%E3%81%AA%E6%83%85%E5%A0%B1" />
