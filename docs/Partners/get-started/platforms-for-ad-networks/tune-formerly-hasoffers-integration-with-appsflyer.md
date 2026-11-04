---
title: Integración de TUNE (anteriormente, HasOffers) con AppsFlyer
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
  edited_at: '2026-08-12T12:30:43Z'
  id: 207034806
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/207034806
---
> **De un vistazo:** Descubre cómo las ad network que usan TUNE (anteriormente HasOffers) para gestionar campañas de marketing de afiliados pueden integrarse con AppsFlyer y recibir datos de atribución sobre instalaciones y eventos in-app.

**Para iniciar la integración, prepara y envía la siguiente información a AppsFlyer:**

1. Tu [enlace de atribución](/docs/tune-formerly-hasoffers-integration-with-appsflyer#crea-un-enlace-de-atribución)
2. Tus [postbacks](/docs/tune-formerly-hasoffers-integration-with-appsflyer#crea-postbacks-de-instalación-y-de-eventos-in-app) (para instalaciones y eventos in-app)

<div id="create-attribution-link" />

## Crea un enlace de atribución

El enlace de atribución consta del enlace de atribución base de AppsFlyer y de macros adicionales añadidas por la ad network.

Consulta el siguiente enlace de atribución base de AppsFlyer con una explicación detallada de cada macro:

| URL base de AppsFlyer | Nota |
| --- | --- |
| https://app.appsflyer.com | Punto de conexión de AppsFlyer |
| id\_aplicación | ID único de la aplicación: valor dinámico que cambia según la aplicación promocionada |
| pid= | Nombre de la fuente de medios concatenado con `_int` para identificar las redes integradas |
| c= | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |

<div id="example-attribution-link-after-adding-tune-macros" />

### Ejemplo de enlace de atribución después de añadir macros de TUNE

```
 
```

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_c_id={offer_id}&af_ad_id={offer_file_id}&idfa=
{ios_ifa}&advertiser_id={google_aid}&af_sub5={offer_id}
```

* En el enlace anterior, se ha añadido `af_sub5={offer_id}` con fines de reportar de TUNE.

Lee más sobre las [macros de TUNE](https://help.tune.com/hasoffers/parameters-macros-in-hasoffers/).

<div id="create-install-and-in-app-event-postbacks" />

## Crea postbacks de instalación y de eventos in-app

Instrucciones paso a paso para crear tus postbacks de instalación y de eventos in-app:

1. Crea o selecciona una oferta que use el protocolo Postback w/Transaction ID.
2. En la sección de detalles de la página de la oferta, haz clic en el enlace con la etiqueta **Tracking**.
3. Copia la URL del cuadro con la etiqueta **Postback URL**.
4. Elimina el parámetro `offer_id` y su valor de la URL del postback para convertirlo de un postback específico en un postback global.

Lee más sobre las [URL de postback globales de TUNE](http://help.tune.com/hasoffers/global-postback-urls/).

<div id="sample-postbacks" />

### Postbacks de muestra

<div id="global-install-postback" />

#### Postback de instalación global:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_lsr?offer_id={af_c_id}&transaction_id={clickid}
```

<div id="in-app-event-postback" />

#### Postback de eventos in-app:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_goal?a=lsr&goal_id={goal_id}&transaction_id={clickid}
```

En las URL de postback anteriores:

* NETWORK\_ID = nombre de dominio (ID de red) proporcionado por TUNE
  * Para garantizar una atribución correcta, NETWORK\_ID siempre debe ser el nombre de dominio de marca proporcionado por TUNE, no un dominio de tracking personalizado utilizado para una oferta concreta (si lo hay).
* goal\_id = etiqueta de evento en el Dashboard de AppsFlyer para cada una de tus aplicaciones. Este es el nombre real del evento in-app de la aplicación.

Saber más sobre <Anchor target="_blank" href="/partners/es/docs/dynamic-event-mapping-for-in-app-events">la asignación dinámica de eventos para eventos in-app</Anchor>.

<div id="finalizing-your-registration" />

## Finalizando tu registro

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros utilizando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de anuncios de Partners <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div data-zendesk-anchors="create-attribution-link=crea-un-enlace-de-atribuci%C3%B3n h_01ET22GJ5N67DKECBQ41QEPEAT=crea-un-enlace-de-atribuci%C3%B3n example-attribution-link-after-adding-tune-macros=ejemplo-de-enlace-de-atribuci%C3%B3n-despu%C3%A9s-de-a%C3%B1adir-macros-de-tune 01JFT1MXJJF3C17B3Y9Q8604BM=ejemplo-de-enlace-de-atribuci%C3%B3n-despu%C3%A9s-de-a%C3%B1adir-macros-de-tune create-install-and-inapp-event-postbacks=crea-postbacks-de-instalaci%C3%B3n-y-de-eventos-in-app h_01ET22H0A0MQ3HH30AJ1TMFNTQ=crea-postbacks-de-instalaci%C3%B3n-y-de-eventos-in-app sample-postbacks=postbacks-de-muestra 01JFT1MXJNSTV7YRVX3BPZ50CY=postbacks-de-muestra global-install-postback=postback-de-instalaci%C3%B3n-global 01JFT1MXJNJBY1P51JQ3ES7QYS=postback-de-instalaci%C3%B3n-global inapp-event-postback=postback-de-eventos-in-app 01JFT1MXJNMF0FWJ2RFER3E316=postback-de-eventos-in-app finalizing-your-registration=finalizando-tu-registro 01JFT1MXJQAXV53RKACW0VAS6E=finalizando-tu-registro" />
