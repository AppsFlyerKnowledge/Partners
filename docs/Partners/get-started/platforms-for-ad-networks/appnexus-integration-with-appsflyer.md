---
title: Integración de AppNexus con AppsFlyer
metadata:
  keywords:
    - Integration
    - AppNexus
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
  created_at: '2016-01-11T14:45:34Z'
  edited_at: '2026-08-12T12:30:12Z'
  id: 207583523
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/207583523
---
> **De un vistazo:** Las ad networks que usan Affise pueden utilizar la solución de modelado probabilístico de AppsFlyer para recibir datos de atribución sobre instalaciones y eventos in-app.

<div id="starting-the-integration" />

## Comenzar la integración

Para comenzar la integración, debes enviar a AppsFlyer tanto el enlace de atribución como el postback para fines de generación de reportes.

A continuación tienes el enlace de atribución base con una explicación detallada de cada parámetro:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| URL base de AppsFlyer | Nota |
| --- | --- |
| https://app.appsflyer.com | Punto de conexión de AppsFlyer |
| id\_aplicación | ID único de la aplicación: el valor dinámico cambiado por cada aplicación promocionada |
| PID | El nombre de la fuente de medios incluye **\_int** para identificar la red **integrada** en los servidores de AppsFlyer |
| C | Nombre de la campaña |

**Macros de ID de publicidad de AppNexus**

| Sistema operativo | Macro |
| --- | --- |
| Android | &advertising\_id=$`{DEVICE_AAID}` |
| apps de iOS, | idfa=$`{DEVICE_APPLE_IDA}` |

**Parámetros recomendados de los enlaces de atribución**

| Parámetro de AppsFlyer | Macros de AppNexus | Nota |
| --- | --- | --- |
| clickid | $`{SSP_DATA}` | ID de solicitud de cada sesión de usuario - **obligatorio** |
| af\_siteid | $`{PUBLISHER_ID}` | ID del afiliado que promociona la oferta: **opcional** |

Para obtener la lista completa de parámetros de AppsFlyer, <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">haz clic aquí</Anchor>.

Para obtener la lista completa de macros de AppNexus, <Anchor target="_blank" href="https://wiki.appnexus.com/display/sdk/Welcome">haz clic aquí</Anchor>.

<div id="complete-attribution-link-template" />

### Plantilla de enlace de atribución completa:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=${SSP_DATA}&af_siteid=${PUBLISHER_ID}
```

<div id="install-and-in-app-event-postbacks" />

### Postbacks de instalaciones y eventos in-app

Postback de instalación global:

```http
https://sspx-router.adnxs.net/sspx?id={ID}&sspdata={clickid}
```

`{ID}` el ID de la red proporcionado por AppNexus, insertado en el Dashboard de AppsFlyer por app.

<div id="appsflyer-install-dashboard" />

### Dashboard de instalaciones de AppsFlyer

[<Image align="center" alt="appnexus-pixelid.png" src="https://files.readme.io/0f14632fc7421fbbb26f90c13cc37afad58e4e217f4bcebd931cddb7576c5113-360018728918.png" />](https://support.appsflyer.com/hc/article_attachments/49754744756625)

Se puede agregar información de atribución adicional al postback mediante solicitud, como el código de país, ID de publicidad, IDFA, etc.

<div id="finalizing-your-registration" />

## Finalizar tu registro

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de ad partners <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div data-zendesk-anchors="starting-the-integration=comenzar-la-integraci%C3%B3n 01JFT0Z4H4N0SFK6CAKQGW41Q4=comenzar-la-integraci%C3%B3n complete-attribution-link-template=plantilla-de-enlace-de-atribuci%C3%B3n-completa 01JFT0Z4H7MA1B9FMNWKESF170=plantilla-de-enlace-de-atribuci%C3%B3n-completa install-and-inapp-event-postbacks=postbacks-de-instalaciones-y-eventos-in-app 01JFT0Z4H7TZPQCFGZCASNWHD7=postbacks-de-instalaciones-y-eventos-in-app appsflyer-install-dashboard=dashboard-de-instalaciones-de-appsflyer 01JFT0Z4H89BP3YWFRSJ69RK6D=dashboard-de-instalaciones-de-appsflyer finalizing-your-registration=finalizar-tu-registro 01JFT0Z4H9TF582WHB69MT9VP2=finalizar-tu-registro" />
