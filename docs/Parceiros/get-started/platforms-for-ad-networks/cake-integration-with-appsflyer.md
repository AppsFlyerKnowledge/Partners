---
title: Integração do Cake com a AppsFlyer
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
  created_at: '2016-01-11T14:44:55Z'
  edited_at: '2026-08-18T00:40:55Z'
  id: 207273986
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/207273986
---
> **Em resumo:** As ad networks que usam a CAKE podem receber dados de atribuição da AppsFlyer sobre instalações e eventos in-app.

<div id="base-attribution-link" />

## Link de atribuição base

Abaixo você pode encontrar o link de atribuição de base com uma explicação detalhada por cada parâmetro:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| https://app.appsflyer.com | Ponto final da AppsFlyer |
| ativado | ID exclusivo do aplicativo - valor dinâmico alterado por aplicativo promovido |
| pid | O nome do canal de mídia inclui **\_int** para identificar a rede **integrada** nos servidores AppsFlyer |
| C | Nome da campanha |

<div id="recommended-attribution-link-parameters" />

### Parâmetros de link de atribuição recomendados

| Parâmetro da AppsFlyer | Macros da CAKE | Descrição |
| --- | --- | --- |
| clickid | #oreqid# | ID da solicitação de cada sessão do usuário - **Obrigatório** |
| af\_siteid | #affid# | ID do afiliado que promove a oferta - **Opcional** |

Para obter a lista completa de parâmetros da AppsFlyer, clique <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">aqui</Anchor>

Para obter a lista completa de macros da CAKE, clique <Anchor target="_blank" href="https://support.getcake.com/support/solutions/articles/5000566463-tokens">aqui</Anchor>.

<div id="complete-attribution-link-template" />

### Template de link de atribuição completo

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#oreqid#
```

<div id="install-and-in-app-event-postbacks" />

## Instalação e postbacks de eventos in-app

<div id="global-install-postback" />

### Postback de instalação global

```http
https://{company-domain}.com/p.ashx?f=pb&r=(Click-ID)
```

<div id="global-in-app-event-postback" />

### Postback global de evento in-app

```http
ID de clique
```

`{Company-Domain}` é o nome do ID da network (domínio) fornecido pela CAKE.  
e= Definido como **Event Tag** no dashboard da AppsFlyer para cada aplicativo pelo anunciante - este é o nome real do evento in-app do aplicativo.  
Para ver a estrutura completa do postback da CAKE, clique aqui

<div id="appsflyer-in-app-events-dashboard" />

### Dashboard de eventos in-app da AppsFlyer

![IAEP.png](https://files.readme.io/3ce734c3930649fdb0b119cd6e12e135e6bcba19225862e9e93b93991451fc8b-360002326529.png)

Informações adicionais de atribuição podem ser incluídas no postback por solicitação, como Código do país, ID de publicidade, IDFA e assim por diante.

<div id="finalizing-your-registration" />

## Finalização do seu registro

* Se você tiver uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget de assistente do parceiro</Anchor>.
* Se você não tiver uma integração com a AppsFlyer, preencha o formulário de registro de parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div data-zendesk-anchors="base-attribution-link=link-de-atribui%C3%A7%C3%A3o-base 01EZPMKP0AFM26H2ZG9FY1D2S4=link-de-atribui%C3%A7%C3%A3o-base recommended-attribution-link-parameters=par%C3%A2metros-de-link-de-atribui%C3%A7%C3%A3o-recomendados 01EZPMKP0A7DBV5KAGZ08C3R49=par%C3%A2metros-de-link-de-atribui%C3%A7%C3%A3o-recomendados complete-attribution-link-template=template-de-link-de-atribui%C3%A7%C3%A3o-completo 01EZPMKP0AH1MB0XYE3PXQPP0V=template-de-link-de-atribui%C3%A7%C3%A3o-completo install-and-inapp-event-postbacks=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app 01EZPMKP0A2D0PB41GD04HX9JX=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app global-install-postback=postback-de-instala%C3%A7%C3%A3o-global 01EZPMKP0AVAJRP8YM48T4GV47=postback-de-instala%C3%A7%C3%A3o-global global-inapp-event-postback=postback-global-de-evento-in-app 01EZPMKP0AM7JD7HWW7BCJDQF3=postback-global-de-evento-in-app appsflyer-inapp-events-dashboard=dashboard-de-eventos-in-app-da-appsflyer 01EZPMKP0AJTYT0G9E8G833KT0=dashboard-de-eventos-in-app-da-appsflyer finalizing-your-registration=finaliza%C3%A7%C3%A3o-do-seu-registro h_01HY03H1PMWZX3T12RZFV15CFE=finaliza%C3%A7%C3%A3o-do-seu-registro" />
