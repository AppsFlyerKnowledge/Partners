---
title: ユーザーをアプリストアにリダイレクトする方法
metadata:
  keywords:
    - clicks
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2018-04-30T08:08:25Z'
  edited_at: '2026-10-14T09:38:04Z'
  id: 360000807629
  locale: ja
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ja/articles/360000807629
---
> **概要：** 広告配信後にユーザーをアプリストアへリダイレクトする方法と、エンゲージメントデータをAppsFlyerに送信する方法について説明します。

<div id="overview" />

## 概要

AppsFlyerは、アトリビューションのためにエンゲージメントデータ（クリックおよびインプレッション）を複数の方法で受け取ります。

* ユーザーが広告を**クリック**し、[AppsFlyerを経由して](#appsflyer経由でリダイレクトされるユーザー)アプリストアへリダイレクトされる
* ユーザーが広告を**クリックまたは閲覧**し、[直接アプリストアへ遷移](#アドネットワークから直接送られるユーザー)する一方で、**アトリビューションリンクがサーバーからAppsFlyerへ送信される**

いずれの場合も、<Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">通常のアトリビューションリンク構造とパラメータが使用されます</Anchor>。

<div id="note" />

> 📘 **注意**
>
> SRN の場合、データは専用の API を介して受信されます

<div id="users-redirected-via-appsflyer" />

## AppsFlyer経由でリダイレクトされるユーザー

広告がクリックされると、ユーザーはまずAppsFlyerに遷移し、その後アプリストアへリダイレクトされます。フローは以下の通りです：

1. ユーザーがAppsFlyerへリダイレクト
2. AppsFlyerがクリックを記録
3. AppsFlyerがユーザーをアプリストアへリダイレクト
4. ユーザーがアプリをインストール
5. AppsFlyerがそのインストール成果を媒体へ紐付け

<div id="users-sent-directly-by-the-ad-network" />

## アドネットワークから直接送られるユーザー

広告がクリックされると、ユーザーはアドネットワークによってアプリストアに誘導されるため、リダイレクトの数を最小限に抑えることができます。

1. ユーザーはアプリストアに送られます
2. アドネットワークは、デバイスからAppsFlyerにエンゲージメントデータを報告します
3. ユーザーがアプリをインストール
4. AppsFlyerがそのインストール成果を媒体へ紐付け

<div id="sending-engagement-data-to-appsflyer" />

### AppsFlyerへのエンゲージメントデータの送信

ユーザーをアプリストアに直接送信すると、リダイレクトの数が減り、エクスペリエンスが向上します。また、インストールの正確なアトリビューションが可能になり、高品質なトラフィックが可能になります。

アドネットワークは、**クリックとインプレッションをユーザーのデバイスから直接AppsFlyerに報告することしかできません**。

<div id="timing-of-sending-redirects" />

#### リダイレクトを送信するタイミング

広告ネットワークのアトリビューションと収益の損失を防ぐには、クリックとインプレッションをリアルタイムでAppsFlyerに送信する必要があります。

* 広告が配信されたら、**インプレッション URL** を報告する必要があります
* **ユーザーが広告をクリックしたら、クリック URL** を報告する必要があります

<div data-zendesk-anchors="overview=%E6%A6%82%E8%A6%81 h_01HDY3CARC0A9504XGMJHYHGY4=%E6%A6%82%E8%A6%81 h_01HDY3CARCZK06C5XHEQFQYA8W=%E6%B3%A8%E6%84%8F redirect-users-via-appsflyer=appsflyer%E7%B5%8C%E7%94%B1%E3%81%A7%E3%83%AA%E3%83%80%E3%82%A4%E3%83%AC%E3%82%AF%E3%83%88%E3%81%95%E3%82%8C%E3%82%8B%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC 01HDYFGYW3FDR64C54KKPXRHDF=appsflyer%E7%B5%8C%E7%94%B1%E3%81%A7%E3%83%AA%E3%83%80%E3%82%A4%E3%83%AC%E3%82%AF%E3%83%88%E3%81%95%E3%82%8C%E3%82%8B%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC send-users-directly-by-the-ad-network=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%8B%E3%82%89%E7%9B%B4%E6%8E%A5%E9%80%81%E3%82%89%E3%82%8C%E3%82%8B%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC 01HDYFH8ZCSP2SN4ZYQQVG7EED=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%8B%E3%82%89%E7%9B%B4%E6%8E%A5%E9%80%81%E3%82%89%E3%82%8C%E3%82%8B%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC send-engagement-data-to-appsflyer=appsflyer%E3%81%B8%E3%81%AE%E3%82%A8%E3%83%B3%E3%82%B2%E3%83%BC%E3%82%B8%E3%83%A1%E3%83%B3%E3%83%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E9%80%81%E4%BF%A1 h_01HDYGSEFHVF8ZD43XCVNGYT9N=appsflyer%E3%81%B8%E3%81%AE%E3%82%A8%E3%83%B3%E3%82%B2%E3%83%BC%E3%82%B8%E3%83%A1%E3%83%B3%E3%83%88%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E9%80%81%E4%BF%A1 timing-of-sending-redirects=%E3%83%AA%E3%83%80%E3%82%A4%E3%83%AC%E3%82%AF%E3%83%88%E3%82%92%E9%80%81%E4%BF%A1%E3%81%99%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%9F%E3%83%B3%E3%82%B0 h_01HDXXDDXDEP43YHE3GF81BSKV=%E3%83%AA%E3%83%80%E3%82%A4%E3%83%AC%E3%82%AF%E3%83%88%E3%82%92%E9%80%81%E4%BF%A1%E3%81%99%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%9F%E3%83%B3%E3%82%B0" />
