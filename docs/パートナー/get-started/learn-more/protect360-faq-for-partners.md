---
title: Protect360 - パートナー向け FAQ
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2023-06-12T12:43:34Z'
  edited_at: '2026-10-14T09:25:24Z'
  id: 16091549732497
  locale: ja
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/ja/articles/16091549732497
---
> **概要：** Protect360 に関するパートナー様からのよくある質問への回答をご覧ください。

<div id="impression-level-anomalies" />

## クリック数/インプレッション数の異常

<div id="why-are-impressionsclicks-being-capped" />

<Accordion title="インプレッション/クリック数に上限があるのはなぜですか?">

AppsFlyer Protect360 システムは、広告エンゲージメントの上限を決定する際に、インプレッション数/クリック数、CVR、検出された異常率、アクティビティの通常の変動、業界や地域のベンチマークなど、さまざまなパラメーターを考慮します。アルゴリズムは動的であり、変化する傾向を考慮して時間単位で更新されます。

上限設定メカニズムがトリガーされると、Protect360 は現在の24時間サイクル内で、関連するアプリのアドネットワークのインプレッションまたはクリックをブロックします。つまり、閾値に達したあとに発生したインプレッションとクリックはAppsFlyerで記録されず、アトリビューションの対象にもなりません。

ネットワークは、パフォーマンス結果に影響を及ぼさない広告エンゲージメントが異常に多いキャンペーンやサイトパブリッシャーを停止することで、しきい値を超えることを回避できます。

次の記事をご覧になることをお勧めします：  
<Anchor target="_blank" href="/partners/ja/docs/protect360-for-integrated-partners#インプレッションとクリックの上限ブロックcapping">インプレッションとクリックの上限設定</Anchor>  
<Anchor target="_blank" href="/partners/ja/docs/protect360-for-integrated-partners#faq">上限設定に関する FAQ</Anchor>

</Accordion>

<div id="i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client" />

<Accordion title="このクライアントで作業していないのに、アプリでクリック上限の問題が発生するのはなぜですか?">

このシナリオは、PID がサードパーティによって操作され、独自の測定作業を回避したことを示している可能性があります。予防策として、AppsFlyer は「クリック署名」ソリューションを提供し、PID を含むすべてのクリックが実際にあなたからのものであることを確認します。

「<Anchor target="_blank" href="/partners/ja/docs/click-signing-for-ad-networks">アドネットワークのクリック署名</Anchor>」の記事を社内チームに提出して、実装の可能性を探ります。その間、管理画面のチャットボットにケースを開くように指示していただければ、当社のチームが次のステップをご案内します。

</Accordion>

<div id="the-number-of-capped-clicks-is-very-small-why-does-such-a-small-amount-trigger-click-capping" />

<Accordion title="クリック数の上限は非常に少ないのに、なぜクリック数の上限が設定されるのでしょうか?">

Protect360 管理画面に表示される「クリック数の上限」は、上限設定のトリガーにはなりません。代わりに、キャッピングサイクル内でアトリビューションのために無視された後続のクリックの数を表します。

これと並行して、上限設定メカニズムによって調べられたクリック数と相関パフォーマンスは、メカニズムがトリガーされる前に何が起こったかを表します。

以下を読むことをお勧めします <Anchor target="_blank" href="/partners/ja/docs/protect360-for-integrated-partners#インプレッションとクリックの上限ブロックcapping">インプレッション数とクリック数の上限設定</Anchor>.

</Accordion>

<div id="the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate" />

<Accordion title="クリック洪水が原因でインストールがブロックされているのに、コンバージョン率が高いのはなぜですか?">

クリック洪水アルゴリズムは、その日のうちにさまざまな間隔で実行され、しきい値を超えると、内部パラメーターとロジックに基づいて、パブリッシャーの広告エンゲージメントはアトリビューションの対象外になります。

**注記：** クリック洪水アルゴリズムの一部はアプリ間で機能し、同一の不正なソースから発生した異常は、宣伝されている他のアプリでも認識されることを意味します。

以下を読むことをお勧めします：<Anchor target="_blank" href="https://www.appsflyer.com/glossary/click-flooding/">クリック洪水とは?</Anchor>

</Accordion>

<div id="installin-app-event-level-anomalies" />

## インストール/アプリ内イベントレベルの異常

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="テストインストールがアトリビューションから拒否されたのはなぜですか?">

AppsFlyer の不正検知対策は、シングルインストールやインストールクラスターなど、さまざまな保護レイヤーに異なる方法論を適用します。クラスターは、パブリッシャー、メディア ソース、アプリなど、さまざまな集計でレビューされています。 不正行為は、各クラスターを全体として考慮したさまざまな統計アルゴリズムと機械学習アルゴリズムを使用して調査されます。したがって、クラスターが統計的有意性が高い不正であることが判明した場合、そのクラスター内のすべてのインストールが不正と見なされます。これは、正規のインストールを大量の不正活動に混ぜて、不正が十分に「希釈」され、ブロックメカニズムが作動するのを避けるという、よく知られた詐欺師の手口です。

デフォルトでは、すべての受信インストールはLIVEトラフィックと見なされるため、テストインストールが Protect360 アルゴリズムに分類されないようにするには、 <Anchor target="_blank" href="/marketers/ja/docs/registering-test-devices">この記事</Anchor>に記載されている手順に従い、 テストを実行する前に、デバイスをテストデバイスとして登録する必要があります。

</Accordion>

<div id="What-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="インストール拒否の検出にはどのような検出方法が使用されますか?">

より明確にするために、拒否に関連する「詐欺のサブ理由」を確認してください。このデータは、Protect360 レポートや Protect360 管理画面でも確認でき、それぞれの広告主からアクセス権が付与されます。

<Anchor target="_blank" href="/marketers/ja/docs/protect360-raw-data-reports#ブロック理由">Protect360 のブロックされた理由</Anchor>を読まれることをお勧めします。

</Accordion>

<div id="protect360-data-visibility-and-comprehension" />

## Protect360 データの可視性と理解

<div id="how-do-i-gain-visibility-into-the-protect360-results" />

<Accordion title="Protect360 の結果を可視化するにはどうすればいいですか?">

Protect360 管理画面とローデータレポートを使用して、検出作業の結果を確認できますが、各広告主から許可されたアクセス権を条件としています。

次の記事をご覧になることをお勧めします：  
<Anchor target="_blank" href="/marketers/ja/docs/protect360-dashboard">Protect360 管理画面</Anchor>  
<Anchor target="_blank" href="/marketers/ja/docs/protect360-raw-data-reports#ローデータレポートの取得">Protect360 ローデータ</Anchor>

</Accordion>

<div id="how-can-i-get-notified-in-realtime-about-blocked-traffic" />

<Accordion title="ブロックされたトラフィックについてリアルタイムで通知を受け取るにはどうすればよいですか?">

AppsFlyer は、Protect360 がアトリビューションを拒否したすべてのインストールに対して、アドネットワークへのアトリビューションポストバックを拒否します。

<Anchor target="_blank" href="/partners/ja/docs/self-serve-integration-management-for-ad-networks">統合管理</Anchor>を使用して、ポストバックテンプレートに「拒否されたポストバック」パラメーターを追加することにより、「拒否されたポストバック」を有効にすることができます。

</Accordion>

<div id="why-do-i-see-spikes-in-postattribution-detections" />

<Accordion title="ポストアトリビューション検出が急増するのはなぜですか?">

アトリビューション前のリアルタイム検知とアトリビューション後の検知は、どちらも AppsFlyer の Protect360 の不正検出メカニズムに属しており、異なる時間軸で適用されます。

リアルタイム検知と比較して、ポストアトリビューション検知は、インストール後に収集されたデータポインタに依存しており、異常が観察された場合、Protect360 は異常なアクティビティを記録し、ポストアトリビューションカテゴリに表示します。

上記を考慮すると、特定の検出方法 (timestamp\_anomalies、behavioral\_anomalies など) は、個々のインストール レベルではデータが決定的ではありませんが、統計分析でその分布を調べると重要性が増すため、リアルタイムではなくポストアトリビューションの段階で検出される可能性が高くなります。

もっと詳しく知る：<Anchor target="_blank" href="/marketers/ja/docs/protect360-anti-fraud-guide#postattribution-detection">ポストアトリビューション検出</Anchor>

</Accordion>

<div data-zendesk-anchors="click-impression-level-anomalies=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E6%95%B0%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AC%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E6%95%B0%E3%81%AE%E7%95%B0%E5%B8%B8 01H8GKS08Y22PX2SBTW5ME02C4=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E6%95%B0%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AC%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E6%95%B0%E3%81%AE%E7%95%B0%E5%B8%B8 01H8GKS08YXVK4CPNW9TX9XBYN=why-are-impressionsclicks-being-capped i%E2%80%99m-facing-a-click-capping-issue-with-an-app-but-i%E2%80%99m-not-working-with-this-client=i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client 01H8GKS08Y3G46SFASMJRFETXR=i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client 01H8GKS08ZGM2QXBNNQCFRC007=the-number-of-capped-clicks-is-very-small-why-does-such-a-small-amount-trigger-click-capping 01H8GKS08ZGNTMNZ5JH846T9Q9=the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate install-inapp-event-level-anomalies=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%AC%E3%83%99%E3%83%AB%E3%81%AE%E7%95%B0%E5%B8%B8 01H8GKS08ZRA7YT9FWJNBBSV4Q=%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%97%E3%83%AA%E5%86%85%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%83%AC%E3%83%99%E3%83%AB%E3%81%AE%E7%95%B0%E5%B8%B8 01H8GKS08Z2M0RTMR4GM1BJE7G=why-was-my-test-install-rejected-from-attribution What-detection-methods-are-used-to-detect-install-rejections%3F=What-detection-methods-are-used-to-detect-install-rejections 01H8H30KARRPAPT9XRREDYKHVT=What-detection-methods-are-used-to-detect-install-rejections protect360-data-visibility-and-understanding=protect360-%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E5%8F%AF%E8%A6%96%E6%80%A7%E3%81%A8%E7%90%86%E8%A7%A3 01H8GKS08ZX2W1G0K165H96N4Z=protect360-%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E5%8F%AF%E8%A6%96%E6%80%A7%E3%81%A8%E7%90%86%E8%A7%A3 01H8GKS08ZGEEK0HQVCRD546MW=how-do-i-gain-visibility-into-the-protect360-results 01H8GKS08ZC6SB4PT53JG5QKHG=how-can-i-get-notified-in-realtime-about-blocked-traffic 01H8GKS08Z673WG6C6JGW31F42=why-do-i-see-spikes-in-postattribution-detections" />
