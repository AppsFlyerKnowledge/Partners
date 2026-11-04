---
title: Integração do Trackier com a AppsFlyer
metadata:
  keywords:
    - AdNetwork Integration
    - ad networks
    - Advertisers
    - ad network
    - Partners
    - trackier
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
  created_at: '2020-02-24T13:25:45Z'
  edited_at: '2026-08-18T00:41:18Z'
  id: 360006111917
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/360006111917
---
> **Em resumo:** As ad networks que usam o Trackier podem receber dados de atribuição da AppsFlyer sobre instalações e eventos in-app.

Para iniciar a integração, forneça à AppsFlyer a URL do link de atribuição e a URL de postback. As URLs são necessárias para fins de reportar. Este artigo explica como criar essas URLs.

<div id="attribution-link-url" />

## URL do link de atribuição

Esta seção fornece o link de atribuição base e as descrições dos parâmetros relacionados.

<div id="base-attribution-link-url" />

### URL do link de atribuição base

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={click_id}&af_siteid={publishedr_id}\n&af_c_id={camp_id}
```

| URL base da AppsFlyer | Definição | A descrição |
| --- | --- | --- |
| https://app.appsflyer.com | URL base | Ponto final da AppsFlyer |
| ativado | ID do aplicativo | Valor dinâmico que difere para cada aplicativo |
| pid= | Nome da fonte de mídia | **\_int** identifica uma **integrada** network |
| c= | Campaign name | Nome dado pelo anunciante |

<div id="attribution-link-parameters" />

### Parâmetros de link de atribuição

<div id="note" />

> 📘 **Observação:**
>
> Os links de atribuição na tabela a seguir são **obrigatórios**.
>
> Veja as listas completas de parâmetros para:
>
> * <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">A AppsFlyer</Anchor>
> * <Anchor target="_blank" href="https://trackier.com/support/kb/tracking-macros/">Trackier</Anchor>

| Parâmetro da AppsFlyer | Macro do Trackier | A descrição |
| --- | --- | --- |
| &clickid= | `{click_id}` | Solicite o ID de cada sessão de usuário |
| &af\_siteid= | `{publisher_id}` | ID do afiliado que promove uma oferta |
| &af\_c\_id= | `{camp_id}` | ID da oferta |

<div id="postback-urls-for-install-and-in-app-events" />

## URLs de postback para instalação e eventos in-app

Esta seção fornece exemplos de URLs de postback e parâmetros para instalação e eventos in-app.

<div id="ios-postback-urls" />

### URLs de postback para **iOS**

<div id="global-install-postback" />

#### Postback de instalação global

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}
```

<div id="global-in-app-event-postback" />

#### Postback global de evento in-app

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}&goal_value={event-name}
```

<div id="android-postback-urls" />

### URLs de postback para **Android**

<div id="global-install-postback-1" />

#### Postback de instalação global

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}
```

<div id="global-in-app-event-postback-1" />

#### Postback global de evento in-app

```http
https://yourdomain.com/acquisition?click_id={click_id}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}&goal_value={event-name}
```

<div id="postback-parameters" />

### Parâmetros de postback

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| seudominio.com | <ul><li>Nome do ID da network (domínio)</li><li>Fornecido pela Trackier</li></ul> |
| event-name | <ul><li>"event\_name"</li><li>Definido pelo anunciante</li></ul> |
| security\_token | Fornecido pela Trackier |
| Código do país, ID de publicidade, IDFA etc. | [Opcional] Informações de atribuição que podem ser adicionadas a um postback |

<div id="finalizing-your-registration" />

## Finalizando seu registro

Já integrou a AppsFlyer? Envie-nos as URLs usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor>.

Ainda não integrou a AppsFlyer? Preencha a <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">solicitação de registro para Parceiros de Anúncio</Anchor>.

<div data-zendesk-anchors="attribution-link-url=url-do-link-de-atribui%C3%A7%C3%A3o 01JFT1SETSSMD0Z0EEQZCYPDB6=url-do-link-de-atribui%C3%A7%C3%A3o base-attribution-link-url=url-do-link-de-atribui%C3%A7%C3%A3o-base 01JFT1SETTCEC1CAGT89SGNZNX=url-do-link-de-atribui%C3%A7%C3%A3o-base attribution-link-parameters=par%C3%A2metros-de-link-de-atribui%C3%A7%C3%A3o 01JFT1SEVJTM09KHEKS51KQB7F=par%C3%A2metros-de-link-de-atribui%C3%A7%C3%A3o 01JFT1SEVJR7TW06CAZWGMBZEB=observa%C3%A7%C3%A3o postback-urls-for-install-and-inapp-events=urls-de-postback-para-instala%C3%A7%C3%A3o-e-eventos-in-app 01JFT1SEWCM9DFRANRJRDSG5DC=urls-de-postback-para-instala%C3%A7%C3%A3o-e-eventos-in-app ios-postback-urls=urls-de-postback-para-ios 01JFT1SEWCSS585NF8P0T251PZ=urls-de-postback-para-ios global-install-postback=postback-de-instala%C3%A7%C3%A3o-global 01JFT1SEWD3A0JP6MRM1QXKX53=postback-de-instala%C3%A7%C3%A3o-global global-inapp-event-postback=postback-global-de-evento-in-app 01JFT1SEWDT1CWHHTVWVACDT0B=postback-global-de-evento-in-app android-postback-urls=urls-de-postback-para-android 01JFT1SEWD0HA5WKC83V8HYAA2=urls-de-postback-para-android global-install-postback::1726dfc2=postback-de-instala%C3%A7%C3%A3o-global-1 01JFT1SEWDY7882HGY032SPGP7=postback-de-instala%C3%A7%C3%A3o-global-1 global-inapp-event-postback::ab23c9cb=postback-global-de-evento-in-app-1 01JFT1SEWDYKTWDE536A4ZY34G=postback-global-de-evento-in-app-1 postback-parameters=par%C3%A2metros-de-postback 01JFT1SEWEZQF38K9V9M6TNP3N=par%C3%A2metros-de-postback finalizing-your-registration=finalizando-seu-registro 01JFT1SEWTPX9BH7N1FPN4NJJW=finalizando-seu-registro" />
