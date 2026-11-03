---
title: 連携済みパートナー向け管理画面
metadata:
  keywords:
    - partner login
    - partner dashboard
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
  created_at: '2016-08-08T08:11:38Z'
  edited_at: '2026-10-14T09:25:32Z'
  id: 212955423
  locale: ja
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/ja/articles/212955423
---
> **概要：** 概要： 連携済みパートナーは、管理画面と各種レポートを使用することで、自社媒体に紐づくキャンペーンのトラフィックを確認可能です。

## AppsFlyer管理画面の利用

**AppsFlyerの管理画面にログインするには：**

1. <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">こちらからログイン</Anchor>するか、https://hq1.appsflyer.com/auth/login へ移動してください。  
   すると、アプリの一覧が表示されます。
2. アプリを選択するか、任意のアプリを検索してください。  
   ご注意ください目的のアプリが表示されない場合には、広告主に<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">アドネットワークへの権限付与</Anchor>を行うよう依頼してください。広告主は、AppsFlyerの管理画面上で［連携済みパートナー］から対象のアドネットワークの設定画面を開き、［権限］タブでこの作業を行う必要があります。

## オーバービュー管理画面

オーバービューでは、キャンペーンのパフォーマンス指標とグラフを確認できます。この画面には、UA (新規獲得) とリターゲティング、という異なるビュータイプが用意されています。

## レポートへのアクセス

レポートデータを取得するには：

* 管理画面左メニューで以下のいずれかを選択してください：
  * <Anchor target="_blank" href="/marketers/ja/docs/raw-data-export-page">ローデータ出力</Anchor>
  * <Anchor target="_blank" href="/marketers/ja/docs/aggregated-data-export-page">集計データエクスポート</Anchor>  
    クリックすると、以下のようなレポート画面が開かれます。

> 📘 **注意**
>
> * **Event Value** （アプリ内イベントに含まれる詳細な値）に関するデータは、レポート内では一切表示されません。event\_valueに関するデータを確認したい場合には、以下のいずれかの対応が必要になります。
>
> * * アプリ内イベントのローデータレポートの提供を広告主へ依頼する

### ポストバックレポートの活用

インストールとアプリ内イベントの<Anchor target="_blank" href="/marketers/ja/docs/raw-data-reporting-overview#postbacks">ポストバックレポート</Anchor> を使用することで、"正しく受け取れていない"各種イベントを見つけることができます。ポストバックレポート上に記載されているのに、アドネットワーク側で記録されていないイベントが存在している状況などがこれに当てはまります。

関連するポストバックのローデータレポートをダウンロードし、**Postback URL** と**Postback HTTP Response Code** のカラムを確認してください：

* レスポンスコードの値が200の場合、AppsFlyerから送信されたポストバックデータは、アドネットワーク側でも正しく受け取られています。
* レスポンスコードが空欄の場合には、AppsFlyerからポストバックは送信したものの、アドネットワーク側からレスポンスが受け取れていません。この場合、**Postback Error Message**のカラムに問題の詳細が記載されます。

[![](https://files.readme.io/e846104ebdd43b6bdd5c635e645ba5806aa152e6fa84d92f957b754b22fd819a-360005578257.png)](https://files.readme.io/e846104ebdd43b6bdd5c635e645ba5806aa152e6fa84d92f957b754b22fd819a-360005578257.png)

## 連携設定の確認

左メニューの **[連携済みパートナー]** をクリックして、現在の連携設定を確認することが可能です。たとえ編集権限が付与されていなくても、現状の連携設定を確認することは可能です。(読み取り専用です。)

ただし、パートナーアカウントから確認できる連携設定は、広告主アカウント上で設定されているもののみになります。

## 権限

広告主は、AppsFlyerの管理画面上で［連携済みパートナー］から対象のアドネットワークの設定画面を開き、<strong>［権限］</strong>タブを使うことで、<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">アドネットワークに対して様々な権限を付与</Anchor>することが可能です。

### 権限付与

最初のステップは、広告主によるパートナーへの権限付与作業です。

1. 広告主の対象となるアプリが、パートナーアカウント上に表示されます。
2. パートナーアカウントのAdmin権限を持つアカウントは、アプリのデータを表示する管理画面へアクセスできるようになり、この段階ではAdminアカウントのみにアクセス権があります。チームメンバーにもアプリの管理画面を確認できるようにしたい場合には、広告主から追加でチームメンバーに対して権限を付与する必要があります。
3. アプリの管理画面に表示されるデータは、そのアドネットワークに関するもののみです。

### 広告ネットワークチームメンバーに権限を付与する

チームメンバーにもアプリの管理画面を確認できるようにしたい場合には、広告主から追加でチームメンバーに対して権限を付与する必要があります。

1. 権限を付与したいチームメンバーのメールアドレスを広告主へ伝えてください。(注：このメールアドレスは、予めパートナーアカウント上でチームメンバーに追加されている必要があります。)
2. 広告主は、そのアドネットワークの連携設定画面の<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#permissions-tab">［権限］タブ内で、そのチームメンバーのメールアドレスを追加する必要があります。</Anchor>

### 追加権限の付与

広告主は、アドネットワークとそのチームメンバーに対して以下の情報に関する追加の権限を付与できます。

* 連携設定の変更権限
* アプリ内イベントのポストバック設定
* リテンションレポート
* ロイヤルユーザー
* In-app events
* 収益
* Protect360へのアクセス権限 - Protect360をご契約済みのお客様のみ

これらの権限を取得したい場合には、広告主に [連携済みパートナー]内で自社のアドネットワークを検索し、[権限]タブ内で該当する項目の権限を付与するよう依頼してください。

広告主がアドネットワークに連携設定の変更権限とアプリ内イベントのポストバック設定の権限を付与すると、パートナーアカウント上でも自社アドネットワークの関連するタブ内の設定を変更することができるようになります。

> 📘 **注意**
>
> * 設定に加えられた変更は、広告主と広告ネットワークのどちらが設定したかに関わらず、現在の設定を上書きします。
> * 代理店アカウント上でもアドネットワークのチームメンバーに対して権限付与することは可能ですが、広告主のみがこの追加の権限に関しては付与することができます。

広告主から連携設定の権限が付与されている場合は、管理画面左メニューの **[連携済みパートナー]** からアクセスが可能です。

広告主からリテンションレポートへのアクセス権限が付与されている場合は、管理画面左メニューの **[リテンション]** からアクセスが可能です。

<div data-zendesk-anchors="using-the-appsflyer-dashboard=appsflyer%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%AE%E5%88%A9%E7%94%A8 h_01HCF5VPHN5RRQFXVJJFPFQBSW=appsflyer%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%AE%E5%88%A9%E7%94%A8 overview-dashboard=%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%93%E3%83%A5%E3%83%BC%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 h_01HCF5VPHNXBQZNF9MNEVCQ243=%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%93%E3%83%A5%E3%83%BC%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2 report-access=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HCF5VPHN08CV555KDHB7QP1Z=%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%B8%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9 h_01HCF5VPHN3REJ2FPD8386Z92S=%E6%B3%A8%E6%84%8F using-postback-reports=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AE%E6%B4%BB%E7%94%A8 h_01HCF5VPHN8RV3GBX1NNFX10P0=%E3%83%9D%E3%82%B9%E3%83%88%E3%83%90%E3%83%83%E3%82%AF%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AE%E6%B4%BB%E7%94%A8 viewing-configuration-settings-and-data=%E9%80%A3%E6%90%BA%E8%A8%AD%E5%AE%9A%E3%81%AE%E7%A2%BA%E8%AA%8D h_01HCF5VPHNSW9X7SNQPC17Q45A=%E9%80%A3%E6%90%BA%E8%A8%AD%E5%AE%9A%E3%81%AE%E7%A2%BA%E8%AA%8D permissions=%E6%A8%A9%E9%99%90 h_01HCF5VPHN6AJ7SE6MGW57BPW8=%E6%A8%A9%E9%99%90 enabling-permissions=%E6%A8%A9%E9%99%90%E4%BB%98%E4%B8%8E h_01HCF5VPHNRCQ5P3MZF9S5RWZW=%E6%A8%A9%E9%99%90%E4%BB%98%E4%B8%8E granting-permissions-to-ad-network-team-members=%E5%BA%83%E5%91%8A%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%81%E3%83%BC%E3%83%A0%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%AB%E6%A8%A9%E9%99%90%E3%82%92%E4%BB%98%E4%B8%8E%E3%81%99%E3%82%8B h_01HCF5VPHP2EXY705GW2VM5YMA=%E5%BA%83%E5%91%8A%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%81%E3%83%BC%E3%83%A0%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%AB%E6%A8%A9%E9%99%90%E3%82%92%E4%BB%98%E4%B8%8E%E3%81%99%E3%82%8B granting-additional-permissions=%E8%BF%BD%E5%8A%A0%E6%A8%A9%E9%99%90%E3%81%AE%E4%BB%98%E4%B8%8E h_01HCF5VPHPHS8QQBMVTGV7B4VJ=%E8%BF%BD%E5%8A%A0%E6%A8%A9%E9%99%90%E3%81%AE%E4%BB%98%E4%B8%8E h_01HCF5VPHPCD52R9222AFQH176=%E6%B3%A8%E6%84%8F-1" />
