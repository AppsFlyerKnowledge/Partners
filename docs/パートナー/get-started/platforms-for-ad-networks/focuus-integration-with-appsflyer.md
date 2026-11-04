---
title: Roku連携設定ガイド
metadata:
  keywords:
    - Focuus
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
  created_at: '2016-10-02T05:18:19Z'
  edited_at: '2026-10-14T09:19:53Z'
  id: 213374546
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/213374546
---
> **概要：** PeerClick を使用するアドネットワークは、AppsFlyer の確率論的モデリングソリューションを活用して、インストールやアプリ内イベントに関するアトリビューションデータを受け取ることができます。


<span id="creating-your-attribution-link"></span>以下のAppsFlyerの基本的な計測リンクと、各マクロの詳細な雪面を参照してください。

| AppsFlyer ベース URL | 説明 |
| --- | --- |
| https://app.appsflyer.com |  |
| app\_id |  |
| pid | メディアソース名には、AppsFlyer サーバーの連携ネットワークを識別するための\_intが含まれています |
| c | キャンペーン名 |

<div id="recommended-attribution-link-parameters" />

### 推奨アトリビューションリンクパラメーター：

| AppsFlyer のパラメーター |  | 説明 |
| --- | --- | --- |
| **clickid** | **`{tid}`** |  |
| af\_siteid | `{publisher_id}` |  |

<div id="complete-attribution-link-template" />

### 完全なアトリビューションリンクテンプレート

`https://app.appsflyer.com/com.appsflyer?pid={traffic_source}&clickid={tid}&af_siteid={publisher_id}`

<div id="install-and-in-app-event-postbacks" />

## インストールとアプリ内イベントのポストバック

4. `https://pixel.focuusing.com/event.php?type=imp&tid={clickid}`

|  | 説明 | 例 |
| --- | --- | --- |
| event\_value |  |  |

* `https://traffic.focuusing.com/install?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/conversion?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/ftd?tid={TRANSACTION_ID}`

<div data-zendesk-anchors="01JFT11W3GWZ3QFYPHEZTS7EX7=creating-your-attribution-link recommended-attribution-link-parameters=%E6%8E%A8%E5%A5%A8%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC 01JFT11W3QWT08KMGEPGK7MV5R=%E6%8E%A8%E5%A5%A8%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%83%BC complete-attribution-link-template=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 01JFT11W3Y7HRB7FYS1K173G2W=%E5%AE%8C%E5%85%A8%E3%81%AA%E3%82%A2%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88 install-and-inapp-event-postbacks=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF 01JFT11W3YMN4RBW0WFTQ9EADK=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF" />
