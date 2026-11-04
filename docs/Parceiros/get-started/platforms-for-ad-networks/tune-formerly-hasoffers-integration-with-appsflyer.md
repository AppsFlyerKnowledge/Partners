---
title: Integração do TUNE (antigo HasOffers) com AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Tune
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
  created_at: '2015-12-22T14:55:13Z'
  edited_at: '2026-08-18T00:41:21Z'
  id: 207034806
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/207034806
---
> **Resumo:** Saiba como ad networks que usam o TUNE (antigo HasOffers) para gerenciar campanhas de marketing de afiliados podem se integrar ao AppsFlyer e receber dados de atribuição sobre instalações e eventos in-app.

**Para iniciar a integração, prepare e envie as seguintes informações para AppsFlyer:**

1. Seu [link de atribuição](/docs/tune-formerly-hasoffers-integration-with-appsflyer#criar-link-de-atribuição)
2. Seus [postbacks](/docs/tune-formerly-hasoffers-integration-with-appsflyer#criar-postbacks-de-instalação-e-de-eventos-in-app) (para instalações e eventos in-app)

<div id="create-attribution-link" />

## Criar link de atribuição

O link de atribuição consiste no link de atribuição de base da AppsFlyer a seguir e em macros adicionais incluídas pela ad network.

Veja o link de atribuição de base da AppsFlyer a seguir com uma explicação detalhada de cada macro:

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| https://app.appsflyer.com | Ponto final da AppsFlyer |
| ativado | ID exclusivo do aplicativo – valor dinâmico alterado por aplicativo promovido |
| pid= | Nome do canal de mídia concatenado com `_int` para identificar networks integradas |
| c= | Campaign name |

<div id="example-attribution-link-after-adding-tune-macros" />

### Exemplo de link de atribuição após adicionar macros do TUNE

```
 
```

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_c_id={offer_id}&af_ad_id={offer_file_id}&idfa=
{ios_ifa}&advertiser_id={google_aid}&af_sub5={offer_id}
```

* No link anterior, `af_sub5={offer_id}` foi adicionado para fins de relatório do TUNE.

Saiba mais sobre as [macros do TUNE](https://help.tune.com/hasoffers/parameters-macros-in-hasoffers/).

<div id="create-install-and-in-app-event-postbacks" />

## Criar postbacks de instalação e de eventos in-app

Instruções passo a passo para criar seus postbacks de instalação e de eventos in-app:

1. Crie ou selecione uma oferta que use o protocolo postback c/ ID de transação.
2. Na seção de detalhes da página da oferta, clique no link identificado como **Tracking**.
3. Copie a URL da caixa identificada como **Postback URL**.
4. Remova o parâmetro `offer_id` e o valor dele da URL do postback para convertê-lo de um postback específico em um postback global.

Saiba mais sobre as [URLs de postback global do TUNE](http://help.tune.com/hasoffers/global-postback-urls/).

<div id="sample-postbacks" />

### Postbacks de amostra

<div id="global-install-postback" />

#### Postback de instalação global:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_lsr?offer_id={af_c_id}&transaction_id={clickid}
```

<div id="in-app-event-postback" />

#### Postback de evento in-app:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_goal?a=lsr&goal_id={goal_id}&transaction_id={clickid}
```

Nas URLs de postback acima:

* NETWORK\_ID = nome de domínio (ID da network) fornecido pela TUNE
  * Para garantir a atribuição correta, o NETWORK\_ID sempre deve ser o nome de domínio da marca fornecido pela TUNE, não um domínio de rastreamento personalizado usado para uma oferta específica (se houver).
* goal\_id = tag de evento no dashboard da AppsFlyer para cada um dos seus aplicativos. Este é o nome real do evento in-app do aplicativo.

Saiba mais sobre <Anchor target="_blank" href="/partners/pt/docs/dynamic-event-mapping-for-in-app-events">Mapeamento dinâmico de eventos para eventos in-app</Anchor>.

<div id="finalizing-your-registration" />

## Finalizando seu registro

* Se você tem uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor>.
* Se você não tem uma integração com a AppsFlyer, preencha o formulário de registro de parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div data-zendesk-anchors="create-attribution-link=criar-link-de-atribui%C3%A7%C3%A3o h_01ET22GJ5N67DKECBQ41QEPEAT=criar-link-de-atribui%C3%A7%C3%A3o example-attribution-link-after-adding-tune-macros=exemplo-de-link-de-atribui%C3%A7%C3%A3o-ap%C3%B3s-adicionar-macros-do-tune 01JFT1MXJJF3C17B3Y9Q8604BM=exemplo-de-link-de-atribui%C3%A7%C3%A3o-ap%C3%B3s-adicionar-macros-do-tune create-install-and-inapp-event-postbacks=criar-postbacks-de-instala%C3%A7%C3%A3o-e-de-eventos-in-app h_01ET22H0A0MQ3HH30AJ1TMFNTQ=criar-postbacks-de-instala%C3%A7%C3%A3o-e-de-eventos-in-app sample-postbacks=postbacks-de-amostra 01JFT1MXJNSTV7YRVX3BPZ50CY=postbacks-de-amostra global-install-postback=postback-de-instala%C3%A7%C3%A3o-global 01JFT1MXJNJBY1P51JQ3ES7QYS=postback-de-instala%C3%A7%C3%A3o-global inapp-event-postback=postback-de-evento-in-app 01JFT1MXJNMF0FWJ2RFER3E316=postback-de-evento-in-app finalizing-your-registration=finalizando-seu-registro 01JFT1MXJQAXV53RKACW0VAS6E=finalizando-seu-registro" />
