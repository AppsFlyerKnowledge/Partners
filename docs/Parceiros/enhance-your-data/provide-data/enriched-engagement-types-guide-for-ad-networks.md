---
title: Guia de engajamentos enriquecidos para ad networks
metadata:
  keywords:
    - Advertisers
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2024-10-15T10:54:29Z'
  edited_at: '2026-08-18T00:39:07Z'
  id: 29221265052433
  locale: pt
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/pt/articles/29221265052433
---
> **Resumo:** Aprenda a criar links de atribuição para engajamentos enriquecidos (EETs) que refletem todo o espectro de engajamento dos usuários e obtenha uma otimização de campanha precisa e eficaz.

Esse novo padrão de qualidade reflete todo o espectro do engajamento e intencionalidade dos usuários quando eles visualizam ou interagem com um anúncio, desde uma exposição momentânea até uma resposta direta. Nesse artigo, explicamos como os parceiros devem relatar os tipos de engajamento nos links de atribuição da AppsFlyer com base em como os usuários interagem com seus anúncios.

> ❗️ **Isenção de responsabilidade**
>
> Esse artigo tem como foco os aspectos de EET relevantes para os parceiros. Para saber o que são EETs e obter informações mais completas, consulte o artigo <Anchor target="_blank" href="/marketers/pt/docs/about-enriched-engagement-types#which-ad-networks-report-enriched-engagement-types">Tipos de engajamento enriquecidos</Anchor>.

## Quais ad networks podem relatar EETs à AppsFlyer?

O suporte para engajamentos enriquecidos estará disponível para ad networks que atendam aos critérios Premier, Advance ou Engage do Programa de Parceiros da AppsFlyer. Esses níveis se referem a ad networks que têm um histórico significativo de fornecimento de tráfego de alta qualidade em grande escala para nossos clientes mútuos, enviam dados de engajamento de forma transparente e confiável e estão integrados com uma ampla variedade de serviços da AppsFlyer.

> 📘 **Nota**
>
> Para começar a relatar engaged views e engaged clicks, as ad networks devem entrar em contato com o suporte da AppsFlyer.

Consulte [a lista de ad networks elegíveis para relatórios de EET](#01JCAT81K2EJNH91YS6NJGMXMB-data-title)

> ❗️ **Aviso**
>
> Os cliques e as impressões de ad networks que não fazem parte dessa lista e que incluam o parâmetro `af_engagement_type` serão rejeitados e não serão usados para atribuição.

<div id="engaged-click-or-engaged-view-attribution-flow" />

<Accordion title="Fluxo de atribuição de engaged click ou engaged view">

As etapas a seguir descrevem o fluxo desde a exibição inicial do anúncio até a atribuição final de um evento de instalação, por meio de um engaged click ou de um engaged view:

1. A ad network exibe um anúncio.
2. A ad network envia uma impressão à AppsFlyer com um `af_ad_tran_id` específico
3. O usuário está se engajando com o anúncio.
4. A ad network envia um clique ou impressão com os parâmetros `af_engagement_type`, `af_ad_tran_id`, `af_ad_format`, `af_ad_type` e, opcionalmente, com os parâmetros `viewability`.
5. A AppsFlyer faz a correspondência entre um evento de instalação com o engaged click ou engaged view.
6. A AppsFlyer atribui o evento de instalação à ad network.

</Accordion>

<div id="parameters-for-reporting-engagement-types-in-attribution-links" />

<Accordion title="Parâmetros para relatar tipos de engajamento em links de atribuição">

As ad networks podem relatar os tipos de engajamento, incluindo os seguintes parâmetros nos links de atribuição

* `af_engagement_type`: o tipo de engajamento, por exemplo, `engaged_click`, `click_to_app` ou `engaged_view`. Veja a <Anchor target="_blank" href="/marketers/pt/docs/about-enriched-engagement-types#engajamentos-enriquecidos">lista completa dos diferentes tipos de engajamento e suas descrições</Anchor>.
* `af_ad_type`: o tipo de anúncio. Por exemplo `rewarded_video`, `interstitial` ou`banner`. Veja a <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#af_ad_type">lista completa dos diferentes tipos de anúncios e suas descrições</Anchor>.
* `af_ad_format`: o formato do anúncio, por exemplo, `text`, `image`, `video`, `playable`. Veja <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#af_ad_format">a lista completa dos diferentes formatos de anúncios e suas descrições.</Anchor>
* `viewability`: (opcional) informações adicionais sobre o engajamento, por exemplo, `af_video_total_length`, `af_ad_time_viewed`, `af_audio_played_length`. Veja <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#parâmetros-de-visibilidade">a lista completa das diferentes opções de visibilidade e suas descrições.</Anchor>
* `af_ad_tran_id`: um ID de transação que permite que a AppsFlyer verifique um engaged click ou engaged view, combinando-o com uma impressão anterior.
* `is_skoverlay=true` ou `is_autostore=true`: Identifique engaged views acionados por [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) ou Android Auto Inline Installs.

**Exemplo de um engaged click**

```http HTTPS
https://app.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_click&af_ad_type=interstitial&af_ad_format=playable&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0
```

**Exemplo de engaged view**

```http
https://impression.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_view&af_ad_type=interstitial&af_ad_format=video&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0&af_video_total_length=20&af_video_played_length=15
```

</Accordion>

<div id="user-engagements-to-report-as-engaged-clicks" />

<Accordion title="Engajamentos do usuário relatados como engaged clicks">

Um *engaged click* é um clique que mantém o usuário em um mesmo contexto, interagindo com o anúncio sem ser redirecionado para a loja de aplicativos ou para a abertura do app.

Veja abaixo exemplos de engajamentos que as ad networks devem relatar com o valor do parâmetro `af_engagement_type=engaged_click`:

* **Anúncios interativos:** engajamento com um anúncio jogável, como clicar para jogar um mini-jogo ou interagir com um conteúdo dentro do anúncio.
* **Engajamento social:** clicar para curtir, comentar ou compartilhar o anúncio nas redes sociais, promovendo maior interação e potencial viralidade.
* **Redirecionamento:** clicar para visitar uma página inicial ou outro site/página de conteúdo externo.
* **Anúncio dinâmico de produtos/catálogo ou carrossel:** clicar para arrastar entre os produtos.
* **Adicionar à lista de desejos:** clicar para adicionar o produto divulgado a uma lista de desejos ou favoritos no app ou em um site externo.
* **Salvar para depois:** clicar para salvar o anúncio e seu conteúdo para referência futura, indicando assim um interesse em revisitar o anúncio ou explorá-lo ainda mais.
* **Marcar ou adicionar às coleções:** clicar para adicionar o anúncio aos favoritos ou adicioná-lo a coleções selecionadas no aplicativo indica a intenção de revisitar ou categorizar o anúncio.
* **Ativar o som do anúncio:** clicar para ativar o áudio.

**Quando você não deve relatar engaged clicks à AppsFlyer?**

Abaixo estão exemplos de engajamentos do usuário que as ad networks **não** devem relatar com o valor do parâmetro `engaged_click`.

* **Fechar anúncio:** clicar no botão “x” para fechar ou dispensar o anúncio, mostrando desinteresse em se engajar.
* **Pular anúncio**: clicar no botão designado para pular um anúncio e seguir diretamente para o conteúdo desejado, indicando que o anúncio não é atraente ou relevante para o usuário.
* **Denunciar anúncio:** clicar para denunciar o anúncio por motivos de conteúdo ofensivo, enganoso ou inapropriado, expressando insatisfação com o conteúdo.
* **Desativar ou cancelar inscrição**: clicar para cancelar o recebimento de anúncios semelhantes no futuro, expressando o desejo de interromper o engajamento com o anúncio.
* **Sair do anúncio:** clicar em um link ou botão que sai da experiência oferecida, levando o usuário para fora do contexto anunciado ou da landing page.
* **Mutar o anúncio:** silenciar o som em um vídeo.

</Accordion>

<div id="user-engagements-to-report-as-engaged-views" />

<Accordion title="Engajamentos do usuário relatados como engaged views">

As ad networks devem relatar os engajamentos do usuário com `af_engagement_type=engaged_view` nos seguintes casos:

* **Unidade de anúncio pulável:** os usuários assistem pelo menos 5 segundos após a opção de pular aparecer em um anúncio em vídeo. Se a ad network não conseguir mensurar o número de segundos visualizados, então:
  * Envie `engaged_view` na visualização de 2/4 (50% de pixel visualizado) quando o vídeo tiver mais de 20 segundos.
  * Envie `engaged_view` por completo (100% do vídeo completo) quando o vídeo tiver menos de 20 segundos
  * O valor do parâmetro `af_ad_format` deve ser `video` ou `playable`
* **Vídeo recompensado**: o usuário vê um vídeo com recompensa em sua totalidade. O valor do parâmetro `af_ad_type` deve ser `rewarded_video`.
* **Anúncios renderizados por StoreKit:** cliques em anúncios renderizados pelo StoreKit ([`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay) ou [`SKStore`](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)) não são registrados por publishers, e sim pela Apple através da atribuição da SKAdNetwork (SKAN). O mesmo vale para Android Auto Inline Installs (autostore).

  Como não há como as ad networks saberem se esses anúncios geraram um engajamento, elas relatam uma impressão ou um clique sempre que os anúncios aparecem, mesmo que nenhum engajamento tenha ocorrido.

  As ad networks podem relatar o tipo de engajamento de `click_to_app` sempre que o anúncio aparece, mas, em seguida, correm o risco de ter uma taxa de cliques muito alta. O mesmo vale para o Android com Auto Inline installs.

  Para reduzir esse risco, recomendamos relatar o tipo de engajamento de `engaged_view`. Nesse caso, o link de atribuição deve incluir `is_skoverlay=true` para iOS ou `is_autostore=true` para Android.

**Quando você não deve relatar engaged views à AppsFlyer?**

Veja abaixo um caso de engajamento do usuário que as ad networks **não** devem relatar com o valor do parâmetro `engaged_view`, mas sim com o parâmetro `view`.

* O usuário vê um anúncio que não pode ser pulado, que não é um vídeo com recompensa e que não foi sobreposto por um anúncio de `SKOverlay` ou `autostore`.

</Accordion>

<div id="01JCAT81K2EJNH91YS6NJGMXMB-data-title" />

<Accordion title="Ad networks elegíveis para relatar EET">

A lista de ad networks elegíveis inclui parceiros cujos eventos de engajamento enriquecido podem ser processados pela AppsFlyer, com a exclusão de engaged clicks e engaged views. As ad networks que fazem parte da lista e desejam que a AppsFlyer processe engaged clicks e engaged views devem entrar em contato com o suporte da AppsFlyer. Para saber quais ad networks já processam esses valores, veja o <Anchor target="_blank" href="/marketers/pt/docs/about-enriched-engagement-types#quais-networks-podem-relatar-engaged-views-e-engaged-clicks">artigo de EET para anunciantes</Anchor>.

> ❗️ **Aviso**
>
> Os cliques e as impressões de ad networks que não fazem parte dessa lista e que incluam o parâmetro `af_engagement_type` serão rejeitados e não serão usados para atribuição.

| Nome do parceiro |
| --- |
| AdColony |
| Adaction |
| Adaction3 |
| Adikteev |
| adjoe GmbH |
| Amazon |
| Amazon DSP |
| AppLovin |
| Appier |
| Appnext |
| Anúncios de Busca da Apple |
| Aura from Unity |
| AWIN |
| Bidease |
| ByteDance Ads China |
| Cauly |
| Criteo |
| Digital Turbine |
| Digital Turbine On Device |
| Fluent |
| Glance |
| Google Ads (Adwords) |
| Google Marketing Platform (DV360/CM360) |
| Hotstar |
| Huawei |
| InMobi DSP |
| ironSource |
| Jampp |
| Josh |
| Kakao |
| Kuaishou |
| Liftoff |
| Linha |
| Meta Ads |
| Mintegral |
| Mistplay |
| Motorola Pre-Install |
| Naver |
| Oppo |
| OPPO Global |
| OPPO Store Traffic (Global) |
| OPPOPAI Pre-Install |
| PayTM |
| Rakuten |
| Reddit |
| Remerge |
| RevX |
| Samsung |
| Smadex |
| Snapchat |
| Stackadapt |
| Tapjoy |
| Tencent AMS |
| TikTok for Business - SRN avançada |
| TikTok For Business - Legado |
| The Trade Desk |
| Transsion |
| Treasure Data |
| Truecaller |
| Unity Ads |
| Vivo Preload |
| vivo Global |
| Vungle |
| X Ads (antigo Twitter Ads) |
| Xiaomi Global |
| XiaomiPAI Pre-Install |
| Yahoo Japan |
| Yandex |
| YouAppi |

</Accordion>

<div data-zendesk-anchors="01JA7WZH43ECDKRC0R0J89ED1E=isen%C3%A7%C3%A3o-de-responsabilidade which-networks-can-report-eet-to-appsflyer=quais-ad-networks-podem-relatar-eets-%C3%A0-appsflyer h_01JJPVYGWZSFSATZ4TH5VBSVXW=quais-ad-networks-podem-relatar-eets-%C3%A0-appsflyer 01JAN5JRM56C6S6EP27WFJ2Y4W=nota h_01J00XFV133YYAB7YPQNXM5R37=aviso 01JA7WZH46RJBG996NG9EZV7T9=engaged-click-or-engaged-view-attribution-flow 01JA7WZH4BZVGS9Z1NNHQC72N6=parameters-for-reporting-engagement-types-in-attribution-links 01JA7WZH4JDJFCVT25WJ4GNE20=user-engagements-to-report-as-engaged-clicks 01JA7WZH4Q32TEWM5EKME142R7=user-engagements-to-report-as-engaged-views 01JCAT81K2EJNH91YS6NJGMXMB%20data-title%3D=01JCAT81K2EJNH91YS6NJGMXMB-data-title allowed-network-list=01JCAT81K2EJNH91YS6NJGMXMB-data-title h_01JJPVYGWZ4T6TPFRWTR2AB027=aviso-1" />
