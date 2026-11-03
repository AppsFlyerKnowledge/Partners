---
title: 高プライバシーポストバック &amp; ポストバックマクロ：アドネットワーク向け
metadata:
  keywords:
    - Ad Networks
    - Partners
    - ios14
    - SKAD
    - Advanced Privacy
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-07-27T07:09:37Z'
  edited_at: '2026-10-14T09:39:26Z'
  id: 360011316197
  locale: ja
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ja/articles/360011316197
---
> **概要：概要：高プライバシーポストバックが有効になっている場合の、パートナーへのデータ共有について記載しています。ご注意くださいこの記事はSKAdNetworkのポストバックには一切関係なく、広告主向けのものでもありません。**

> 📄 **高プライバシーポストの更新情報**
>
> 本ページ内に記載されている高プライバシーポストバックの機能は、以下条件に全て当てはまった場合に有効になります：
>
> * ユーザーの端末がiOS 14.5以上を搭載していること
> * 高プライバシーポストバックがONになっていること

![AdvancedPrivacy.png](https://files.readme.io/2a80740637c1003e03bc169df274bf0fa6240ee850c7fd6e967c4abea234e0d1-360018213598.png)

この記事では以下の内容について記載しています：

* 高プライバシーポストバックが与えるパートナーへの影響
* アトリビューションの対象となるために必要な、[Click URL](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements)の要件
* AppsFlyerの管理画面上での、[高プライバシーポストバックのテンプレート](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification)の設定方法
* [高プライバシーポストバックとSKAdNetwork](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#ap-vs-skadnetwork)の違い

## 高プライバシーポストバックでのデータ共有の原則

iOS14.5以降、AppsFlyerの<Anchor target="_blank" href="/marketers/ja/docs/apply-aggregated-advanced-privacy-framework">高プライバシー一括設定(AAP)</Anchor>のフレームワークはユーザーレベルのアトリビューションデータの可用性を管理する機能を広告主へ提供します。

アドネットワークにとっては、このAAPのフレームワークは高プライバシーポストバック(AP)の使用をもって適用されます。わかりやすく、このページでは高プライバシーポストバックをAPと略して記載してきます。

また、APはアドネットワークや代理店も利用可能である集計データの可用性には何も影響しませんのでご安心ください。

**APの設定によって影響を受けるデータについて**

APがONになっている場合、iOS14.5以上のOSでATTに同意しなかった端末のユーザーレベルのデータは、ポストバックやProtect360の不正関連のレポートを含む各種レポート機能において利用できなくなります。

つまりポストバックにおいて、ユーザーのATT同意状況とその他の要因によって、異なるタイプのポストバックが都度使用されることになります。

 デフォルト設定はAPがONになっています。

![APforPartners2.png](https://files.readme.io/e4fb5617a47635f24dc83881c2be3d18b770200a576cb67bd3312e6fc2c123e1-360018154777.png)


* <span id="types-of-templates-for-sending-postbacks"></span>レギュラーテンプレートレギュラーポストバック：AppsFlyerとの既存のポストバック連携のテンプレートで、ユーザー識別子やclickID、アトリビューションデータに関するマクロが含まれています。
* **注記：** AP連携の作業はパートナーアカウント上のポストバック管理の画面を使って、ご自身で設定が可能です。

> 📘 **注意**
>
> * エンドユーザーが広告主アプリと広告配信アプリの両方でATTに同意した場合、レギュラーポストバックのテンプレートを使って成果の紐付いた媒体と成果の紐付いていない媒体へもポストバックが送信されます。

### 使用されるポストバックの種類について

以下の表は、iOS14.5以降のユーザーデータに適用されるものです。

ご注意ください

#### iOS14.5以降使用されるポストバックの種類

<table><thead><tr><th rowspan="2"><p>AP設定</p></th><th colspan="2">ATTのステータス</th><th rowspan="2">APをサポートしている媒体への紐付いた成果\*のポストバック  </th><th rowspan="2">APをサポートしていない媒体への紐付いた成果\*のポストバック  </th><th rowspan="2">紐付いていない成果のポストバック\*</th></tr><tr><th><p>広告掲載アプリ</p></th><th><p>広告主アプリ</p></th></tr></thead><tbody><tr><td><p><span>オン</span></p></td><td><p><span>承認</span></p></td><td><p><span>許可されていません</span></p></td><td></td><td><p><span>ポストバックなし</span></p></td><td><p><span>なし</span></p></td></tr><tr><td><p><span>オン</span></p></td><td><p><span>許可されていません</span></p></td><td><p><span>承認</span></p></td><td> </td><td><p><span>ポストバックなし</span></p></td><td><p>レギュラーテンプレート<a href="./advanced-privacy-guide-postback-macros-for-ad-networks#types-of-templates-for-sending-postbacks"></a></p><p>(<span>媒体関連の情報</span>は利用不可)\*</p></td></tr><tr><td><p><span>オン</span></p></td><td><p><span>承認</span></p></td><td><p><span>承認</span></p></td><td><p>レギュラーテンプレート<span></span></p></td><td>レギュラーテンプレート<span></span> </td><td> (媒体関連の情報は利用不可)\* </td></tr><tr><td><p><span>オン</span></p></td><td><p><span>許可されていません</span></p></td><td><p><span>許可されていません</span></p></td><td></td><td><p><span>ポストバックなし</span></p></td><td><p><span>なし</span></p></td></tr><tr><td><p><span>オフ</span></p></td><td><p><span>考慮外</span></p></td><td><p><span>考慮外</span></p></td><td>レギュラーテンプレート<a href="./advanced-privacy-guide-postback-macros-for-ad-networks#types-of-templates-for-sending-postbacks"></a> </td><td><p>レギュラーテンプレート<span></span></p></td><td><p>レギュラーテンプレート<span></span></p><p>(<span>媒体関連の情報</span>は利用不可)\*</p></td></tr></tbody></table>

**(\*)パートナーとのデータ共有の原則**

特定のイベントについて、AppsFlyerでは複数のアドネットワークがポストバックを受け取ることが可能です。送信されるポストバックは以下の通りです：

* 成果の紐付け先ではないパートナー：成果やイベントが紐付いていない連携済みパートナーも、**アプリ内イベントのポストバック設定**において、**送信オプション**の設定を、**オーガニックを含むすべてのメディアソース**にした場合に、ポストバックを受け取ります。広告主アプリにおいてATTダイアログにユーザーが同意した場合、ポストバックに他社媒体情報は含まれませんが、各種ユーザーIDは含まれます。(この送信オプションの機能は全てのアドネットワークでサポートしているわけではありません。)  

  ![InAppEventAll.png](https://files.readme.io/e24037f75b2b82797031eb13d5e063b8c2006812491e69674ff066ac830919f7-35847850644881.png)

### Web面での広告配信

アドネットワークがWeb面上で広告を表示している場合、APの挙動が異なります。

#### APがON かつ iOS14.5以降において使用されるポストバックタイプ

<table><thead><tr><th colspan="2">ATTのステータス</th><th rowspan="2">紐付いた成果のポストバックタイプ\*</th><th rowspan="2">紐付いていない成果のポストバックタイプ\*</th></tr><tr><th><p>広告掲載アプリ</p></th><th><p>広告主アプリ</p></th></tr></thead><tbody><tr><td><p><span>N/A</span></p></td><td><p><span>許可されていません</span></p></td><td><p><span>高プライバシーポストバック</span></p></td><td><p><span>なし</span></p></td></tr><tr><td><p><span>N/A</span></p></td><td><p><span>承認</span></p></td><td><p>レギュラー<span>ポストバックIDFA, IDFV, CUID, Click ID</span></p></td><td><p>レギュラーポストバック(媒体情報は含まれず、IDFAなどのユーザー情報のみ)</p></td></tr></tbody></table>

## 統合

クリックURLをアップデートして、高プライバシーポストバックの連携を完了してください。

<div id="click-url-requirements" />

<Accordion title="クリックURLのパラメータについて">

多くのケースにおいて、ユーザーのATTへの同意状況に応じて、IDFAは配信面アプリ、広告主アプリ、またはその両方で使用できなくなるでしょう。そのようなシナリオにおいて、AppsFlyerでは確率論的モデリングと<Anchor target="_blank" href="/marketers/ja/docs/appsflyer-attribution-model#aggregated-advanced-privacy-aap">高プライバシー一括設定</Anchor>の機能を活用してアトリビューションを実施することがあります。

［推奨］計測情報を最大限充実させるために、表に記載されているパラメータを全て送信してください。

1. 計測URLに以下の各種パラメータを追加してください：

<table><thead><tr><th>識別子</th><th>クリックパラメータ</th><th><p>例</p></th></tr></thead><tbody><tr><td><p><span>Campaign</span></p></td><td><p><span>c</span></p></td><td><p><span>US_20_30</span></p></td></tr><tr><td><p><span>Campaign ID</span></p></td><td><p><span>af_c_id</span></p></td><td><p><span>12345</span></p></td></tr><tr><td><p><span>Adset</span></p></td><td><p><span>af_adset</span></p></td><td><p><span>ADSET_1</span></p></td></tr><tr><td><p><span>Adset ID</span></p></td><td><p><span>af_adset_id</span></p></td><td><p><span>56789</span></p></td></tr><tr><td><p><span>広告</span></p></td><td><p><span>af_ad</span></p></td><td><p><span>creative_name</span></p></td></tr><tr><td><p><span>Ad ID</span></p></td><td><p><span>af_ad_id</span></p></td><td><p><span>34567</span></p></td></tr><tr><td><p><span>Site ID</span></p></td><td><p><span>af_siteid</span></p></td><td><p><span>abcdefgh12345678</span></p></td></tr><tr><td><p><span>Subsite ID</span></p></td><td><p><span>af_sub_siteid</span></p></td><td><p><span>abcdefgh12345678</span></p></td></tr><tr><td><p><span>Channel</span></p></td><td><p><span>af_channel</span></p></td><td><p><span>channel_name</span></p></td></tr><tr><td><p><span>広告タイプ</span></p></td><td><p><span>af_ad_type</span></p></td><td><p><span>video</span></p></td></tr><tr><td><p>iOSの端末モデル\*</p></td><td><p><span>af_model</span></p></td><td><p>デバイスモデル。利用可能な値は以下のみです。</p><ul><li>iphone (すべて小文字)</li><li>ipad (すべて小文字)</li></ul></td></tr><tr><td><p><span>OS\*</span></p></td><td><p><span>af_os</span></p></td><td><p><span>端末のOSバージョンを入力してください。</span></p></td></tr><tr><td colspan="3"><p>※ 一部の情報は、ユーザーエージェントを介して提供される場合があります。その場合には、特定のパラメータを使って送信された値の方が計測時に優先されます。</p></td></tr></tbody></table>

   クリックURLへのキャンペーン詳細の情報追加

   次の例を参考に、キャンペーン詳細に関するパラメータをクリックURLに追加してください：

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adsetname}&af_adset_id={adset ID}&af_ad={adname}&af_ad_id={ad ID}&af_ad_type={Adtype}&af_siteid={PublisherId}` |
| --- |

2. 各クリックURLに、以下の必須パラメータを追加してください*：  

   > ❗️ **注意**
   >
   > クリックURLが各必須パラメータを渡さない場合、配信しているキャンペーンに紐づくべきインストールの大部分があなたの媒体成果として反映されなくなる可能性があるので注意してください。


   * IP
   * User-agent

   *AppsFlyerへリダイレクトするシンプルなHTTPリファラを使用してクリックを送信している場合には、これらのパラメータを追加する必要はありません。 

   以下の方法のいずれかを使用している場合には、記載されている取得方法などを参考にしてクリックURLへパラメータとその値を追加してください： 

   * アプリ内でのリダイレクト(アプリ面)
   * サーバーtoサーバーでのクリック計測 (S2S)

   #### 高プライバシー計測用のパラメータ

   <Table>
     <thead>
       <tr>
         <th>
           パラメータ
         </th>
         <th>
           必須
         </th>
         <th>
           取得方法
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           **端末の言語設定と地域情報**

           af\_lang
         </td>
         <td>
           いいえ
         </td>
         <td>
           NSString *language = [[NSLocale preferredLanguages] objectAtIndex:0];

           ［推奨］言語と地域情報を左記の形式で提供してください。例：en-US
         </td>
       </tr>
       <tr>
         <td>
           **ユーザーエージェント**

           af\_ua
         </td>
         <td>
           はい
         </td>
         <td>
           以下の形式でユーザーエージェントを取得してください。

           ```
           Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+13_3_1  
           +like+Mac+OS+X%29 AppleWebKit%2F605.1.15+%28KHTML%2C  
           +like+Gecko%29+Mobile%2F15E148
           ```

           * CFNetworkのユーザーエージェントは**取得せず**、*それ以外のユーザーエージェントを取得してください。*
           * ユーザーエージェントはURLエンコードされている必要があります。
         </td>
       </tr>
       <tr>
         <td>
           **デバイスのIPアドレス**

           af\_ip
         </td>
         <td>
           はい
         </td>
         <td>
           可能であれば、af\_ip パラメータにデバイスのIPを入力してください。

           次のオプション:可能な場合、AppsFlyerはX-Forwarded-ForのIPを利用します。
         </td>
       </tr>
     </tbody>
   </Table>

   クリックURLへのパラメータ追加

   クリック計測URLにおいて上記の必須パラメータをパスするには、以下の例を参考にしてください： 

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad-type}&af_siteid={PublisherId}&af_ua={USER-AGENT}&af_lang={LANGUAGE}&af_ip={IP}` |
| --- |

   **サンプル**

| `name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={adID}  <br />&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />`&af_ua=Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2012_1_4%20`<br /><br />`2F605.1.15%20%``28KHTML%2C%20like%20Gecko%29%20Mobile%2F16D57&af_lang=en-US&af_ip=11.11.1.11` |
| --- |

   * クエリパラメータはURLエンコードする必要があります。

   **クリックURLヘッダー上で、データをパスしてください。**

   クリックURLヘッダー上で各フィールドを渡すには、以下の例を使用してください。

| GET<br /><br />`accept-language: en-US,en;q=0.`<br /><br />`User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)`<br /><br />`AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148`<br /><br />`X-Forwarded-For: 11.11.1.11, 222.222.2.222` |
| --- |

</Accordion>

<div id="advanced-privacy-postback-specification" />

<Accordion title="高プライバシーポストバックの仕様について">

**レギュラーポストバックと高プライバシーポストバックのテンプレートの違い**

* ポストバックは1時間毎にまとめて送信されます。
  * このバッチにはインストール、アプリ内イベントなどすべてのイベントタイプが含まれます。
  * このバッチには、成果の紐付いたアトリビューションデータと、ブロックされたリジェクトポストバックの両方が含まれます。
  * なお、0.001%のポストバックデータが後から別のバッチで送信される可能性があり、最大で24時間の遅延が発生する可能性があります。
* ポストバックの送信時間は実際のイベント発生時間とは異なります。
* タイムスタンプのマクロについて：
  * インストールとアプリ内イベントのデータの場合、タイムスタンプは発生した時間単位での情報に丸められます。例："22:55:30"というデータは"22:00:00"としてレポートされます。
  * UTCのタイムゾーンが適用されます。例： "timestamp" : 15848352001232024-02-26

**連携のために必要なアドネットワーク側のアクション**

1. [AppsFlyerのパートナーアカウント上での、高プライバシーポストバックの設定](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback)
2. <Anchor target="_blank" href="/partners/ja/docs/ios-integration-testing-for-ad-networks">高プライバシーポストバックの連携テスト</Anchor>

#### 高プライバシーポストバックのエンドポイント [必要に応じて]

| ポストバックの種類 |
| --- |
| インストール |
| アプリ内 |

#### 高プライバシーポストバックで利用可能なポストバックマクロ

<table><thead><tr><th><p>ポストバックマクロ名</p></th><th>備考</th><th>全ポストバック向けの基本パラメータ</th><th>アプリ内イベント専用のパラメータ </th><th>リジェクトされた計測データ専用のパラメータ</th></tr></thead><tbody><tr><td>af_ad</td><td>クリエイティブ名</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_ad_id</td><td>34567</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_ad_type</td><td>例：banner, footer, video</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_adset</td><td>ADSET_1</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_adset_id</td><td>56789</td><td>はい</td><td> </td><td> </td></tr><tr><td>app_id</td><td>-</td><td>はい</td><td> </td><td> </td></tr><tr><td>app_name</td><td>-</td><td>はい</td><td> </td><td> </td></tr><tr><td>attributed_touch_hour</td><td><p>時間(Hour)単位に切り捨て </p><p>Format：注(1)を参照してください</p></td><td>はい</td><td> </td><td> </td></tr><tr><td>attributed_touch_type</td><td>例：click, impression</td><td>はい</td><td> </td><td> </td></tr><tr><td>blocked_reason</td><td>検証ルール/Protect360に関連します</td><td> </td><td> </td><td>はい</td></tr><tr><td>blocked_reason_value</td><td>検証ルール/Protect360に関連します</td><td> </td><td> </td><td>はい</td></tr><tr><td>blocked_sub_reason</td><td>検証ルール/Protect360に関連します</td><td> </td><td> </td><td>はい</td></tr><tr><td>bundle_id</td><td>広告主側で設定</td><td>はい</td><td> </td><td> </td></tr><tr><td>c</td><td>キャンペーン名など例：US_20_30</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_c_id</td><td>キャンペーンIDなど例：12345</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_channel</td><td>チャネル名</td><td>はい</td><td> </td><td> </td></tr><tr><td>country_code</td><td>コンバージョン記録時のISO国コード</td><td>はい</td><td> </td><td> </td></tr><tr><td>event_hour</td><td><p>時間(Hour)単位に切り捨て </p><p>Format：注(1)を参照してください</p></td><td>はい</td><td> </td><td> </td></tr><tr><td>event_name</td><td>アプリによって異なるイベント名が入ります</td><td> </td><td>はい</td><td> </td></tr><tr><td>event_revenue</td><td>event_currencyに基づく収益金額</td><td> </td><td>はい</td><td> </td></tr><tr><td>event_revenue_<br/>currency</td><td>収益の通貨単位</td><td> </td><td>はい</td><td> </td></tr><tr><td>event_revenue_usd</td><td>USDに換算された収益金額</td><td> </td><td>はい</td><td> </td></tr><tr><td>install_hour</td><td><p>時間(Hour)単位に切り捨て </p><p>Format：注(1)を参照してください</p></td><td>はい</td><td> </td><td> </td></tr><tr><td>is_first</td><td>そのアプリ内イベントが、そのユーザーにとって初めて発火されたイベントだった場合にはTrueが入ります</td><td> </td><td>はい</td><td> </td></tr><tr><td>is_primary</td><td><p>重複除外に利用可能</p><p>ブール値2024-02-26</p></td><td> </td><td>はい</td><td> </td></tr><tr><td>is_retargeting</td><td><p>重複除外に利用可能 </p><p>形式：注(2)を参照してください。</p></td><td>はい</td><td> </td><td> </td></tr><tr><td>is_reengagement</td><td><p>形式：注(2)を参照してください。</p></td><td> </td><td>はい</td><td> </td></tr><tr><td>is_reattribution</td><td><p>重複除外に利用可能 </p><p>形式：注(2)を参照してください。</p></td><td>はい</td><td> </td><td> </td></tr><tr><td>match_type</td><td>例：id_matching, probabilistic</td><td>はい</td><td> </td><td> </td></tr><tr><td>event_id</td><td>アドネットワークのプラットフォーム上で発生したイベントと称号するための名称またはIDです</td><td> </td><td>はい</td><td> </td></tr><tr><td>platform</td><td>例：ios, android</td><td>はい</td><td> </td><td> </td></tr><tr><td>postback_id</td><td>ポストバック毎にユニークなID</td><td>はい</td><td> </td><td> </td></tr><tr><td>retargeting_<br/>conversion_type</td><td>例：re-engagement, re-attribution</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_siteid</td><td>abcdefgh12345678</td><td>はい</td><td> </td><td> </td></tr><tr><td>af_sub_siteid</td><td>abcdefgh12345678</td><td>はい</td><td> </td><td> </td></tr></tbody><tfoot><tr><td colspan="5"><p>注：</p><p>(1) 利用可能なタイムスタンプ形式：</p><ul><li>YYYY-MM-DD HH:MM:SS</li><li>10桁のUNIXタイムスタンプが用いられます。 </li></ul><p>(2) Booleanの形式が利用可能</p><ul><li>[デフォルト] 数値：0, 1 2024-02-26 </li><li>String： <em>false</em>, <em>true</em> </li></ul></td></tr></tfoot></table>

</Accordion>

<div id="setting-up-your-advanced-privacy-postback" />

<Accordion title="高プライバシーポストバックの設定方法について">

AppsFlyerの管理画面上にある、ポストバック管理の機能を使って、高プライバシーポストバックを設定してください。

**前提条件**：

* 高プライバシーポストバックの設定を管理するには、AppsFlyerと有効な連携設定 / パートナーアカウントが必要です。

**ポストバックを設定するには：**

1. 管理画面右上のアカウントメニュー（メールアドレスのドロップダウン）> ユーザー管理を開きます。
2. 高度なプライバシー:：
3. トグルをONにして、設定画面をアクティブにしてください。  

   ![postback-management-enter-endpoint_en-us.png](https://files.readme.io/4ea0ffc61d1ecdb11d3c745876c29a942fde4133b8ebb54a1426a73c1dc63b16-360018215218.png)
4. AppsFlyerからのポストバックを受け取る**エンドポイントのアドレス**をインストールとアプリ内イベントで、それぞれ関連するURLを入力してください。
5. ポストバック内に含めたいパラメータを入力してください。
   * パラメータ名
   * **受け取り側のパラメータ名**：御社側で値を受け取る際の各パラメータ名
   * **パラメータの値**(いくつかのパラメータで利用可能)：値のフォーマットを選択してください。例えばBoolean値の場合、"true"/"false"と1/0、どちらで受け取るのかを選択します。
   * **Install**: インストールのポストバックに含めたいパラメータにチェックを入れてください。
   * **In-app event**: アプリ内イベントのポストバックに含めたいパラメータにチェックを入れてください。

   ![postback-management-parameters_en-us.png](https://files.readme.io/818ef31df9c4e349ca26b5421a0ba0582ed5f7f9fae39f1d0e4ec3b7562f4192-360018213698.png)

   [高プライバシーポストバック用のマクロ一覧](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification)
6. <strong>［任意］</strong>AppsFlyerでは提供していないカスタムパラメータも追加可能です。

   ![postback-management-custom-parameters_en-us.png](https://files.readme.io/6bca46e1d39c6822b0e041eb1dcbb1b2d40e42fa062c34877c8cbf0c2d2847d6-16589581250321.png)
7. 最後に、作成されたポストバックテンプレートのプレビューを確認して、全て正しく設定されていることを確認してください。

   ![postback-management-template_en-us.png](https://files.readme.io/b5e41cad37859365c7818c4561620f8a78250c207d8326dae53ed9b522fe3716-360018213718.png)
8. **保存**をクリックしてください。この設定を保存すると、その変更内容がすぐに適用・有効になります。

</Accordion>

## 追加情報

<div id="ap-for-analytics-partners" />

<Accordion title="アナリティクスパートナー向けのAP">

アナリティクスパートナーに対して、ポストバックは以下のように送信されます：

* AP OFF：制約なく、ユーザーレベルのポストバックが送信されます。
* AP ON：ユーザーの流入元とATTのステータスに応じて、以下表のようにポストバックが送信されます。

#### ATTステータスとユーザーの流入元毎のポストバックタイプ：アナリティクスパートナー向け

<table><thead><tr><th rowspan="2"><p>流入元</p></th><th colspan="2">ATTのステータス</th><th rowspan="2">アナリティクスパートナー向けのポストバックタイプ</th></tr><tr><th><p>広告掲載アプリ</p></th><th><p> 広告主アプリ</p></th></tr></thead><tbody><tr><td rowspan="3"><p><span>非オーガニック</span></p><br/><p><span> </span></p><br/><p><span> </span></p></td><td><p><span>承認</span></p></td><td><p><span>承認</span></p></td><td>レギュラーポストバック</td></tr><tr><td><p><span>許可されていません</span></p></td><td><p><span>承認</span></p></td><td><p>なし</p></td></tr><tr><td><p><span>上記以外</span></p></td><td><p>許可されていません</p></td><td>なし</td></tr><tr><td><p><span>オーガニック / Web</span></p></td><td>N/A</td><td><p>承認</p></td><td>レギュラーポストバック</td></tr><tr><td><p><span>オーガニック / Web</span></p></td><td><p><span>N/A</span></p></td><td><p>許可されていません</p></td><td>なし</td></tr></tbody></table>

</Accordion>

<div id="ap-vs-skadnetwork" />

<Accordion title="SKAdNetwork">

<Anchor target="_blank" href="/partners/ja/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>はAppleがiOS端末向けに提供しているアトリビューション技術です。一方、高プライバシーポストバックは<Anchor target="_blank" href="/marketers/ja/docs/apply-aggregated-advanced-privacy-framework">高プライバシー一括設定(AAP)</Anchor>のフレームワークの一部であり、AppsFlyerによるアトリビューションに関連するものです。このフレームワークにより、広告主はAppsFlyerプラットフォームを介してユーザーレベルのアトリビューションデータの可用性を制御できます。

</Accordion>

<div data-zendesk-anchors="h_01HJR7MWPM9XA4BXHDRD2K6D56=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%81%AE%E6%9B%B4%E6%96%B0%E6%83%85%E5%A0%B1 ad-network-advanced-privacy-datasharing-principles=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%A7%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E5%85%B1%E6%9C%89%E3%81%AE%E5%8E%9F%E5%89%87 h_01HJR7MWPNYNMKZ3R8C3BB5EVG=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%A7%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E5%85%B1%E6%9C%89%E3%81%AE%E5%8E%9F%E5%89%87 h_01HJR7MWPN92BDJRK734P6YXSK=types-of-templates-for-sending-postbacks h_01HJR7MWPN71TP0KWVVBHPC0H2=%E6%B3%A8%E6%84%8F type-of-postback-used=%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%82%8B%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E7%A8%AE%E9%A1%9E%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 h_01HJR7MWPNJEDNDT1ZY7P78HMG=%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%82%8B%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E7%A8%AE%E9%A1%9E%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6 postback-type-for-ios-145=ios145%E4%BB%A5%E9%99%8D%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%82%8B%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E7%A8%AE%E9%A1%9E h_01HJR7MWPNESP8BDC4D6Y7SBFZ=ios145%E4%BB%A5%E9%99%8D%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%82%8B%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E7%A8%AE%E9%A1%9E web-campaigns=web%E9%9D%A2%E3%81%A7%E3%81%AE%E5%BA%83%E5%91%8A%E9%85%8D%E4%BF%A1 h_01HJR7MWPNXHHCSQ6BGCNRBHZK=web%E9%9D%A2%E3%81%A7%E3%81%AE%E5%BA%83%E5%91%8A%E9%85%8D%E4%BF%A1 postback-type-used-for-ios-145-when-ap-is-on=ap%E3%81%8Con-%E3%81%8B%E3%81%A4-ios145%E4%BB%A5%E9%99%8D%E3%81%AB%E3%81%8A%E3%81%84%E3%81%A6%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%82%8B%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%82%BF%E3%82%A4%E3%83%97 h_01HJR7MWPNQCCNGHQY5RQHQ6D1=ap%E3%81%8Con-%E3%81%8B%E3%81%A4-ios145%E4%BB%A5%E9%99%8D%E3%81%AB%E3%81%8A%E3%81%84%E3%81%A6%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%82%8B%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%82%BF%E3%82%A4%E3%83%97 integration=%E7%B5%B1%E5%90%88 h_01HJR7MWPP7YGRXJQR29F3ERHH=%E7%B5%B1%E5%90%88 h_01HJR7MWPPAXK18KER56E30G8R=click-url-requirements h_01HJR7MWPPRN8XYVSS7HX7NQB9=%E6%B3%A8%E6%84%8F-1 parameters-for-advanced-privacy-attribution=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E8%A8%88%E6%B8%AC%E7%94%A8%E3%81%AE%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF h_01HJR7MWPPK2HET3XYW4WBFAZ1=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E8%A8%88%E6%B8%AC%E7%94%A8%E3%81%AE%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF h_01HJR7MWPQ60F4CESKRRMTQ7HX=advanced-privacy-postback-specification h_01HJR7MWPQ8K06A1YM4KV4RTN8=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E8%A8%88%E6%B8%AC%E7%94%A8%E3%81%AE%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF advanced-privacy-postback-endpoint-%5Bcomplete-as-required%5D=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%82%A8%E3%83%B3%E3%83%89%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E5%BF%85%E8%A6%81%E3%81%AB%E5%BF%9C%E3%81%98%E3%81%A6 h_01HJR7MWPQX9SXJZMBS6QR07WD=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E3%82%A8%E3%83%B3%E3%83%89%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-%E5%BF%85%E8%A6%81%E3%81%AB%E5%BF%9C%E3%81%98%E3%81%A6 advanced-privacy-attribution-macros-available=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%A7%E5%88%A9%E7%94%A8%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%9E%E3%82%AF%E3%83%AD h_01HJR7MWPQKH52XMD6H9TJ0SM3=%E9%AB%98%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%81%A7%E5%88%A9%E7%94%A8%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%9E%E3%82%AF%E3%83%AD h_01HJR7MWPRC44K908A4EAPN9GV=setting-up-your-advanced-privacy-postback additional-information=%E8%BF%BD%E5%8A%A0%E6%83%85%E5%A0%B1 h_01HJR7MWPRVFR6YN56Y0DGBAXH=%E8%BF%BD%E5%8A%A0%E6%83%85%E5%A0%B1 h_01HJR7MWPR6ACNYVZHK7YPHQGP=ap-for-analytics-partners analytics-partner-postback-type-according-to-att-status-and-user-source=att%E3%82%B9%E3%83%86%E3%83%BC%E3%82%BF%E3%82%B9%E3%81%A8%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%81%AE%E6%B5%81%E5%85%A5%E5%85%83%E6%AF%8E%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%82%BF%E3%82%A4%E3%83%97%E3%82%A2%E3%83%8A%E3%83%AA%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91 h_01HJR7MWPRZDJNSZNB981WB5Z1=att%E3%82%B9%E3%83%86%E3%83%BC%E3%82%BF%E3%82%B9%E3%81%A8%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%81%AE%E6%B5%81%E5%85%A5%E5%85%83%E6%AF%8E%E3%81%AE%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%82%BF%E3%82%A4%E3%83%97%E3%82%A2%E3%83%8A%E3%83%AA%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E5%90%91%E3%81%91 h_01HJR7MWPR3YR7E9S49P9ZZ3CT=ap-vs-skadnetwork" />
