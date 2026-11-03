---
title: Integración de Fuseclick con AppsFlyer
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
  created_at: '2016-01-11T14:46:45Z'
  edited_at: '2026-08-12T12:30:26Z'
  id: 207583573
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/207583573
---
> **De un vistazo:** Las ad networks que usan FuseClick pueden aprovechar la solución de modelado probabilístico de AppsFlyer para recibir datos de atribución sobre instalaciones y eventos in-app.

## Enlace de atribución básico

A continuación tienes el enlace de atribución base con una explicación detallada de cada parámetro:

```http
https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}
```

| URL base de AppsFlyer | Nota |
| --- | --- |
| https://app.appsflyer.com | Punto de conexión de AppsFlyer |
| id\_aplicación | ID único de la aplicación: valor dinámico que cambia según la aplicación promocionada |
| PID | El nombre de la fuente de medios incluye **\_int** para identificar la red **integrada** en los servidores de AppsFlyer |
| C | Nombre de la campaña |

**Parámetros recomendados de los enlaces de atribución:**

| Parámetro de AppsFlyer | Macros de FuseClick | Nota |
| --- | --- | --- |
| clickid | `{TID}` | ID de solicitud de cada sesión de usuario - **obligatorio** |
| af\_siteid | `{SC}` | ID del afiliado que promociona la oferta: **opcional** |

Para obtener la lista completa de parámetros de AppsFlyer, <Anchor target="_blank" href="/partners/es/docs/postback-macros-for-ad-networks">haz clic aquí</Anchor>

Para obtener la lista completa de macros de FuseClick, <Anchor target="_blank" href="https://support.fuseclick.com/documentation/open/iwf/2016/0805/199.html">haz clic aquí</Anchor>

Plantilla completa del enlace de atribución:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={TID}&af_siteid={ADV_SID}
```

### Postbacks de instalaciones y eventos in-app

Postback de instalación global:

```
https://tracking.zadsmobile.com/pb?tid={TID}
```

Se puede añadir información de atribución adicional al postback mediante solicitud, como el código de país, el ID de publicidad, el IDFA y más.

## Finaliza tu registro

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para Partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de Partners de anuncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div data-zendesk-anchors="basic-attribution-link=enlace-de-atribuci%C3%B3n-b%C3%A1sico 01JFT0DX287AWQND2BYFSV50HW=enlace-de-atribuci%C3%B3n-b%C3%A1sico install-and-inapp-event-postbacks=postbacks-de-instalaciones-y-eventos-in-app 01JFT0DX2B6FFE3K7VTXG1YVJ1=postbacks-de-instalaciones-y-eventos-in-app finalizing-your-registration=finaliza-tu-registro 01JFT0DX2BD8A19BY9197X11QW=finaliza-tu-registro" />
