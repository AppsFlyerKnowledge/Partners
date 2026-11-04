---
title: Integración de Affise con AppsFlyer
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
  edited_at: '2026-08-12T12:30:10Z'
  id: 208537116
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/208537116
---
> **De un vistazo:** Las ad networks que utilizan Affise pueden usar la solución de modelado probabilístico de AppsFlyer para recibir datos de atribución sobre instalaciones y eventos in-app.

Para comenzar la integración, debes enviar a AppsFlyer tanto el enlace de atribución como el postback para fines de generación de reportes.

<div id="base-attribution-link" />

## Enlace de atribución de base

A continuación tienes el enlace de atribución base con una explicación detallada de cada parámetro:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}&af_c_id={offerid}
```

**Parámetros obligatorios del enlace de atribución**

| Parámetro de AppsFlyer | Macros de Affise | Descripción |
| --- | --- | --- |
| clickid | `{clickid}` | ID de solicitud de cada sesión de usuario |
| af\_siteid | `{pid}` | ID del afiliado que promociona la oferta |
| af\_c\_id | `{offer_id}` | ID de la oferta |

Para obtener la lista completa de parámetros de AppsFlyer, <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">haz clic aquí</Anchor>.

<div id="complete-attribution-link-template" />

## Plantilla de enlace de atribución completa

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}
```

<div id="install-and-in-app-event-postbacks" />

## Postbacks de instalaciones y eventos in-app

A continuación, se muestran ejemplos de postbacks de instalación y de eventos in-app:

<div id="global-install-postback-ios" />

### Postback de instalación global iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}
```

<div id="global-install-postback-android" />

### Postback de instalación global Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}
```

<div id="global-in-app-event-postback-ios" />

### Postback de evento in-app global iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}&goal={event-name}
```

<div id="global-in-app-event-postback-android" />

### Postback de evento in-app global Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}&goal={event-name}
```

Domain.com es el nombre del ID de red (dominio) proporcionado por Affise.

e= Se establece como **Event Name** en el dashboard de AppsFlyer para cada app por parte del anunciante. Este es el nombre real del evento in-app de la aplicación.

Se puede agregar información de atribución adicional al postback mediante solicitud, como el código de país, ID de publicidad, IDFA, etc.

<div id="finalizing-your-registration" />

## Finaliza tu registro

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de ad Partners <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div data-zendesk-anchors="base-attribution-link=enlace-de-atribuci%C3%B3n-de-base 01JFT0RZG0F67JFBC7W5KK54BM=enlace-de-atribuci%C3%B3n-de-base complete-attribution-link-template=plantilla-de-enlace-de-atribuci%C3%B3n-completa 01JFT0RZG2QTT3Z9S6SVNV5VE7=plantilla-de-enlace-de-atribuci%C3%B3n-completa install-and-inapp-event-postbacks=postbacks-de-instalaciones-y-eventos-in-app 01JFT0RZG3C7MBBYFKA6W813PF=postbacks-de-instalaciones-y-eventos-in-app global-install-postback-ios=postback-de-instalaci%C3%B3n-global-ios 01JFT0RZG3HM9P81XYGKHZXHFK=postback-de-instalaci%C3%B3n-global-ios global-install-postback-android=postback-de-instalaci%C3%B3n-global-android 01JFT0RZG4JCDP8D4CWQW02AY7=postback-de-instalaci%C3%B3n-global-android global-inapp-event-postback-ios=postback-de-evento-in-app-global-ios 01JFT0RZG40N0VNNVMDBFYNT9E=postback-de-evento-in-app-global-ios global-inapp-event-postback-android=postback-de-evento-in-app-global-android 01JFT0RZG4PA9WTP212AX52QWZ=postback-de-evento-in-app-global-android finalizing-your-registration=finaliza-tu-registro 01JFT0RZG52JW6C5GR0KA4CZF6=finaliza-tu-registro" />
