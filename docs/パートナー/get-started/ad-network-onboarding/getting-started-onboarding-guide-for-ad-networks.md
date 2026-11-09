---
title: 入門：アドネットワーク向けオンボーディングガイド
metadata:
  keywords:
    - Ad Network
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
  created_at: '2019-03-28T08:41:59Z'
  edited_at: '2026-10-14T09:26:15Z'
  id: 360001300998
  locale: ja
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ja/articles/360001300998
---
> **概要:** アトリビューションリンクとポストバック統合の設定とテストを行い、AppsFlyerとの統合を完了しましょう。プロセスの手順、タイムライン、依存関係を理解しましょう。

<Image align="center" alt="AdNetworks_-_Onboarding__2_.png" src="https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png" />

<div id="what-is-appsflyer" />

## AppsFlyerとは？

モバイルアトリビューションのリーダーであるAppsFlyerは、アドネットワーク統合パートナーとして皆様を歓迎します。この記事は、AppsFlyerのパートナー登録を完了したアドネットワーク向けです。パートナー登録を希望する場合は、<Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#appsflyerに新しいパートナーを招待する">AppsFlyerのカスタマー（広告主）</Anchor>に招待してもらう必要があります。

<div id="ad-network-onboarding" />

## アドネットワークのオンボーディング

統合に必要な手順とその完了までの推定時間は、このページの**オンボーディングステップ**セクションに記載されています。

統合とは以下のことを意味します：

* AppsFlyerは、あなたのエンゲージメント（クリックとインプレッション）を記録します。エンゲージメントは、<Anchor target="_blank" href="/marketers/ja/docs/appsflyer-attribution-model">AppsFlyerのアトリビューションモデル</Anchor>に従って紐づけされます。
* 指定された形式のポストバックがエンドポイントに送信されます。
* AppsFlyerのクリック署名、Protect360、Data Lockerなどの機能にアクセスできます。

<div id="if-you-need-help" />

<Accordion title="サポートが必要な場合">

* パートナー向けの<Anchor target="_blank" href="/partners/ja/docs/integrated-partners-faq">FAQ</Anchor>をご覧ください
* <Anchor target="_blank" href="/partners/ja/docs/integration-requests-for-partners">統合変更リクエスト</Anchor>の記事を参照してください

</Accordion>

注意点：

* この記事で記載されている所要時間は、アドネットワークとの作業体験に基づいています。各統合設定は多少異なるため、実際の所要時間も変わることがあります。
* AppsFlyerは多くの<Anchor target="_blank" href="/partners/ja/docs/platforms-for-ad-networks">パフォーマンスプラットフォーム</Anchor>をサポートしています。リストにあるプラットフォームを利用している場合は、統合前に該当プラットフォームの説明を確認する必要があります。

<div id="onboarding-steps" />

## オンボーディング手順

**AppsFlyerとの統合方法**:

1. [パート1 - 統合とテストを完了する](/docs/getting-started-onboarding-guide-for-ad-networks#パート1統合とテスト)
2. [パート2 - 広告主アプリでのテストの完了](/docs/getting-started-onboarding-guide-for-ad-networks#パート2広告主アプリを使用してテストします)
3. [パート3 - AppsFlyer管理画面とレポートツールの利用](/docs/getting-started-onboarding-guide-for-ad-networks#パート3appsflyer管理画面とレポーティングオプション)

<div id="part-1-integration-and-testing" />

### パート1：統合とテスト

<table><thead><tr><th>アクション</th><th>所要時間</th></tr></thead><tbody><tr><td>必須の統合手順を完了するための登録確認メールが届くまでお待ちください。</td><td>--</td></tr><tr><td colspan="2"> <strong>必須の統合手順</strong> </td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#計測リンク" target="_blank">アトリビューションリンクを指定してください</a>: アトリビューションリンクはマクロを含むURLです。これらのマクロには実際の値が入力され、ユーザーがリンクをクリックするたびにAppsFlyerに送信されます。 <br/>注意！AppsFlyerがサポートするパフォーマンスネットワークプラットフォームを利用する場合は、各プラットフォーム固有の指示を考慮する必要があります。<a href="./platforms-for-ad-networks" target="_blank">パフォーマンスネットワークガイド</a>をご覧ください。 </td><td>60</td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#デフォルトポストバック" target="_blank">ポストバックマクロを指定する</a>:ポストバックは、AppsFlyerによって入力されたマクロを含むURLで、各コンバージョン後にリアルタイムでサーバーに送信されます。</td><td>60</td></tr><tr><td>提供された資格情報を使って、<a href="https://hq1.appsflyer.com/auth/login" target="_blank">AppsFlyer管理画面</a>にログインします。 </td><td> </td></tr><tr><td>企業のロゴをアップロードします。ロゴは200 x 50の透明PNG形式である必要があります。 <ol><li>AppsFlyerのメニューバーで、自分のメールアドレス &gt; <strong>パートナー設定</strong>を選択します。 </li><li> <strong>プロフィール</strong>タブで、企業のロゴをアップロードします。 </li><li> <strong>保存</strong>をクリックします。</li></ol></td><td>5</td></tr><tr><td>AppsFlyerテストアプリを使って統合をテストします。<ul><li><a href="./android-integration-testing-for-ad-networks" target="_blank">Android</a></li><li><a href="./ios-integration-testing-for-ad-networks" target="_blank">iOS</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>オプションの統合手順</strong></td></tr><tr><td>[iOS] 広告主がAppsFlyer Aggregated Advanced Privacyを必要とする場合、<a href="./self-serve-integration-management-for-ad-networks#高プライバシーとskanのポストバック" target="_blank">Advanced Privacy</a>の統合を完了してください。</td><td>60</td></tr><tr><td>[iOS] SKAdNetworkキャンペーンを行う場合、<a href="./self-serve-integration-management-for-ad-networks#高プライバシーとskanのポストバック" target="_blank">SKAdNetwork統合</a>を完了してください。 </td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>認定代理店</strong></h4>ネットワーク統合を通じてキャンペーンを行うことを承認した代理店リストを作成、管理します。これは、セキュリティセンターの<a href="./set-up-your-list-of-authorized-agencies" target="_blank"><strong>承認済み代理店</strong></a> セクションに代理店ID (af_prt)を入力することで行います。代理店IDを取得するには、代理店が連絡し提供する必要があります。</td><td>2</td></tr><tr><td colspan="2"><p><strong>オプション機能と考慮事項</strong><br/> </p><p>広告主の要望に基づいて、統合やオプションの実装を検討してください。</p></td></tr><tr><td>不正なクリックがパートナーIDで送信されないようにするには、<a href="./click-signing-for-ad-networks" target="_blank">クリック署名</a>を実装します。 </td><td>60+</td></tr><tr><td>Protect360や検証ルールを実装している広告主には、<a href="./postback-macros-for-ad-networks#マクロ名一覧---インストール--アプリ内イベント--ブロックされたイベント向け" target="_blank">拒否されたアトリビューションポストバック</a>を追加します。</td><td>15</td></tr><tr><td>API経由でAppsFlyerにコストを送信します。<a href="./incost-api-for-ad-networks" target="_blank">InCost API</a>を参照してください。</td><td>60+</td></tr><tr><td> <a href="/marketers/ja/docs/retargeting-attribution-guide" target="_blank">リターゲティング統合</a>。</td><td>15</td></tr><tr><td> <a href="/marketers/ja/docs/measure-view-through-engagements" target="_blank">ビュースルーアトリビューション統合</a>。</td><td>15</td></tr></tbody></table>

<div id="part-2-test-using-advertiser-apps" />

### パート2:広告主アプリを使用してテストします

この部分では、広告主に属するアプリを使用して統合をテストします。そのため、広告主に連絡して、このパートの手順の一部を完了してもらうよう依頼する必要があります。この部分では、広告主に言及する際、代理店を指す場合もあり、これは代理店が広告主に代わって行動している場合に当てはまります。

| 作業担当者 | アクション | 所要時間 |
| --- | --- | --- |
| 広告主 | <Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#integration-tab">パートナーを有効化</Anchor>するをオンにします。<br /><br />オンになっていると、AppsFlyerはあなたによってもたらされたエンゲージメントをアトリビューションの候補として扱います。 | 2 |
| 広告主 | <Anchor target="_blank" href="/marketers/ja/docs/set-up-an-integrated-partner#アドネットワークの権限">アドネットワークの権限*を付与</Anchor>し、チームメンバーを追加します。<br /><br />オンになっていると、アプリのパフォーマンスデータをAppsFlyerの管理画面で利用できるようになります。リストされたチームメンバーのみがデータにアクセスできます。 | 2 |
| アドネットワーク | <Anchor target="_blank" href="/marketers/ja/docs/user-management#creating-users">あなたのアカウントにチームメンバーを追加します</Anchor>。 | 2 |
| 広告主（管理者） | <Anchor target="_blank" href="/marketers/ja/docs/registering-test-devices">テストデバイスを登録します</Anchor>。広告主に、あなたに代わってこれを実行するよう依頼してください。 | 3 |
| アドネットワーク | <Anchor target="_blank" href="/partners/ja/docs/test-marketer-campaign-integration-with-the-ad-network">広告主のアプリを使用して統合をテストします。</Anchor> | 60 |

<div id="part-3-appsflyer-dashboard-and-reporting-options" />

### パート3:AppsFlyer管理画面とレポーティングオプション

| オプション |
| --- |
| <Anchor target="_blank" href="/partners/ja/docs/integrated-partners-dashboard">パートナー管理画面</Anchor>を利用します。 |
| アドネットワーク向けに、<Anchor target="_blank" href="/partners/ja/docs/data-locker-for-partners">Data Locker</Anchor>を使用してクラウドストレージから集計パフォーマンスデータを取得します。 |
| Protect360<Anchor target="_blank" href="/marketers/ja/docs/raw-data-export-page">のローデータを取得します。</Anchor> |

<div id="integration-validation-period" />

## 統合検証期間

AppsFlyerエコシステムの整合性を確保し、内部システムを無効なトラフィックから保護するために、すべての新しいアドネットワーク統合には検証期間が設けられています。この期間中、AppsFlyerはトラフィックを徹底的に検証し、その品質を評価した上で、<Anchor target="_blank" href="/marketers/ja/docs/partner-integrations">マーケットプレイス</Anchor>で他の広告主に統合を利用可能にします。

<div id="validation-periodfaq" />

### 検証期間—FAQ

| **質問** | **回答** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>統合を完了しているにもかかわらず、広告主がマーケットプレイスで私を見つけられないのはなぜですか？ | 検証期間中、あなたの統合はあなたを紹介した広告主にのみ表示されます。トラフィックの品質が検証された後、統合がすべての広告主に利用可能になったことを通知するメールが届きます。 |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>統合が承認されるようにするにはどうすれば良いですか？ | あなたを紹介した広告主に向けて、大量の高品質トラフィックを提供します。 |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>検証完了メールはいつ頃届きますか？ | 十分なトラフィックが検証できた後、検証期間の終了を知らせるメールが届きます。 |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>検証評価の現在の状態を知ることはできますか？ | 検証期間が終了したかは、メール通知を受けて初めてわかります。 |
| <span id="what-are-the-validation-criteria-based-on"></span>検証基準は何に基づいていますか？ | 検証基準は、<Anchor target="_blank" href="/marketers/ja/docs/protect360-anti-fraud-guide">Protect360</Anchor> の動的機械学習アルゴリズムに基づいています。トラフィックの質、量、データの有効性などの要因が業界のベストプラクティスと組み合わされて考慮されます。 |
| <span id="another-adviertiser-wants-to-work-with-me"></span>検証期間中に別の広告主が協力を申し出た場合はどうすれば良いですか？ | 検証期間中は、あなたの連携は紹介元広告主にのみ表示されます。検証期間が無事に終了すると、他の広告主もあなたと仕事ができるようになります。 |
| <span id="my-integration-fails"></span>連携が検証に失敗した場合、どうなりますか？ | トラフィック品質の向上を監視するため検証期間を延長するか、連携がAppsFlyerプラットフォームから永久に削除される場合があります。どちらの場合も通知が届きます。 |
| <span id="replace-advertiser"></span>紹介広告主を、私が協力している他の広告主に変更することはできますか？ | それは、30日間の検証期間内であれば可能です。 |

<div data-zendesk-anchors="what-is-appsflyer=appsflyer%E3%81%A8%E3%81%AF h_01J09255QNBFRV8DYZPGG990A0=appsflyer%E3%81%A8%E3%81%AF ad-network-onboarding=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%AE%E3%82%AA%E3%83%B3%E3%83%9C%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0 h_01J09255QN61VPW292PC2CH9KN=%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%AE%E3%82%AA%E3%83%B3%E3%83%9C%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0 h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help onboarding-steps=%E3%82%AA%E3%83%B3%E3%83%9C%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E6%89%8B%E9%A0%86 h_01J09255QNZ9QXXFB54YRYCM8P=%E3%82%AA%E3%83%B3%E3%83%9C%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E6%89%8B%E9%A0%86 part-1-integration-and-testing=%E3%83%91%E3%83%BC%E3%83%881%E7%B5%B1%E5%90%88%E3%81%A8%E3%83%86%E3%82%B9%E3%83%88 h_01J09255QN35ZBKE2R2HDDZWSZ=%E3%83%91%E3%83%BC%E3%83%881%E7%B5%B1%E5%90%88%E3%81%A8%E3%83%86%E3%82%B9%E3%83%88 h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies part-2-test-using-advertiser-apps=%E3%83%91%E3%83%BC%E3%83%882%E5%BA%83%E5%91%8A%E4%B8%BB%E3%82%A2%E3%83%97%E3%83%AA%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E3%83%86%E3%82%B9%E3%83%88%E3%81%97%E3%81%BE%E3%81%99 h_01J09255QP11XJD3C83VZZXXQZ=%E3%83%91%E3%83%BC%E3%83%882%E5%BA%83%E5%91%8A%E4%B8%BB%E3%82%A2%E3%83%97%E3%83%AA%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E3%83%86%E3%82%B9%E3%83%88%E3%81%97%E3%81%BE%E3%81%99 part-3-appsflyer-dashboard-and-reporting-options=%E3%83%91%E3%83%BC%E3%83%883appsflyer%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%A8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3 h_01J09255QPSSD8CF0HR059RWXZ=%E3%83%91%E3%83%BC%E3%83%883appsflyer%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%A8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3 integration-validation-period=%E7%B5%B1%E5%90%88%E6%A4%9C%E8%A8%BC%E6%9C%9F%E9%96%93 h_01J09255QP82ZYZDJMA74SRYGZ=%E7%B5%B1%E5%90%88%E6%A4%9C%E8%A8%BC%E6%9C%9F%E9%96%93 validation-period%E2%80%94faq=%E6%A4%9C%E8%A8%BC%E6%9C%9F%E9%96%93faq h_01J09255QP77BME57P9B7S222V=%E6%A4%9C%E8%A8%BC%E6%9C%9F%E9%96%93faq" />
