---
title: Integração da Affise com a AppsFlyer
metadata:
  keywords:
    - Integration
    - affise
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
  created_at: '2016-04-19T12:08:58Z'
  edited_at: '2026-08-18T00:40:51Z'
  id: 208537116
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/208537116
---
> **Visão geral:** As ad networks que usam a Affise podem utilizar a solução de Modelo probabilístico da AppsFlyer para receber dados de atribuição sobre instalações e eventos in-app.

Para iniciar a integração, você deve enviar à AppsFlyer o link de atribuição e o postback para fins de relatório.

<div id="base-attribution-link" />

## Link de atribuição base

Abaixo você pode encontrar o link de atribuição de base com uma explicação detalhada por cada parâmetro:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}&af_c_id={offerid}
```

**Parâmetros obrigatórios do link de atribuição**

| Parâmetro da AppsFlyer | Macros da Affise | Descrição |
| --- | --- | --- |
| clickid | `{clickid}` | ID da sessão de cada usuário |
| af\_siteid | `{pid}` | ID do afiliado que promove a oferta |
| af\_c\_id | `{offer_id}` | ID da oferta |

Para obter a lista completa de parâmetros da AppsFlyer, <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">clique aqui</Anchor>.

<div id="complete-attribution-link-template" />

## Template de link de atribuição completo

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}
```

<div id="install-and-in-app-event-postbacks" />

## Instalação e postbacks de eventos in-app

A seguir estão exemplos de postbacks de instalação e de evento in-app:

<div id="global-install-postback-ios" />

### Postback global de instalação iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}
```

<div id="global-install-postback-android" />

### Postback global de instalação Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}
```

<div id="global-in-app-event-postback-ios" />

### Postback global de evento in-app iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}&goal={event-name}
```

<div id="global-in-app-event-postback-android" />

### Postback global de evento in-app Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}&goal={event-name}
```

Domain.com é o nome do ID da network (domínio) fornecido pela Affise.

e = definido como **Event Name** no dashboard da AppsFlyer para cada Aplicativo pelo anunciante - este é o nome real do evento in-app no aplicativo.

Informações adicionais de atribuição podem ser incluídas no postback por solicitação, como Código do país, ID de publicidade, IDFA etc.

<div id="finalizing-your-registration" />

## Finalizar seu registro

* Se você tiver uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget do partner assistant</Anchor>.
* Se você não tiver uma integração com a AppsFlyer, preencha a solicitação de registro de parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div data-zendesk-anchors="base-attribution-link=link-de-atribui%C3%A7%C3%A3o-base 01JFT0RZG0F67JFBC7W5KK54BM=link-de-atribui%C3%A7%C3%A3o-base complete-attribution-link-template=template-de-link-de-atribui%C3%A7%C3%A3o-completo 01JFT0RZG2QTT3Z9S6SVNV5VE7=template-de-link-de-atribui%C3%A7%C3%A3o-completo install-and-inapp-event-postbacks=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app 01JFT0RZG3C7MBBYFKA6W813PF=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app global-install-postback-ios=postback-global-de-instala%C3%A7%C3%A3o-ios 01JFT0RZG3HM9P81XYGKHZXHFK=postback-global-de-instala%C3%A7%C3%A3o-ios global-install-postback-android=postback-global-de-instala%C3%A7%C3%A3o-android 01JFT0RZG4JCDP8D4CWQW02AY7=postback-global-de-instala%C3%A7%C3%A3o-android global-inapp-event-postback-ios=postback-global-de-evento-in-app-ios 01JFT0RZG40N0VNNVMDBFYNT9E=postback-global-de-evento-in-app-ios global-inapp-event-postback-android=postback-global-de-evento-in-app-android 01JFT0RZG4PA9WTP212AX52QWZ=postback-global-de-evento-in-app-android finalizing-your-registration=finalizar-seu-registro 01JFT0RZG52JW6C5GR0KA4CZF6=finalizar-seu-registro" />
