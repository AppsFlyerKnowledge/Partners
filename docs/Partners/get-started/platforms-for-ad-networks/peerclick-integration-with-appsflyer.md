---
title: Integración de PeerClick con AppsFlyer
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
  created_at: '2024-01-07T08:27:18Z'
  edited_at: '2026-08-12T12:30:37Z'
  id: 21479841979793
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/21479841979793
---
> **De un vistazo:** Las redes de publicidad que utilizan PeerClick pueden beneficiarse de la solución de modelado probabilístico de AppsFlyer para recibir datos de atribución sobre instalaciones y eventos in-app.

<div id="starting-the-integration" />

## Comenzar la integración

Para comenzar la integración, debes enviar a AppsFlyer tanto el enlace de atribución como el postback para fines de generación de reportes.

A continuación tienes el enlace de atribución base con una explicación detallada de cada parámetro:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| URL base de AppsFlyer | Descripción |
| --- | --- |
| https://app.appsflyer.com | Punto de conexión de AppsFlyer |
| id\_aplicación | ID único de la aplicación: el valor dinámico cambiado por cada aplicación promocionada |
| pid= | El nombre de la fuente de medios incluye **\_int** para identificar la red **integrada** en los servidores de AppsFlyer |
| c= | Nombre de la campaña |

**Parámetros recomendados de los enlaces de atribución:**

| Parámetro de AppsFlyer | Macros de volumen | Descripción |
| --- | --- | --- |
| &clickid= | `{clickid}` | ID de transacción único de la sesión del usuario: **obligatorio** |
| &af\_siteid= | `{trafficsource.id}` | ID de la fuente de tráfico: **opcional** |

<div id="note" />

> 📘 **Nota**
>
> * Para obtener la lista completa de parámetros de AppsFlyer, <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">haz clic aquí</Anchor>.
> * Para obtener la lista completa de PeerClick, <Anchor target="_blank" href="https://help-center.peerclick.com/en/">haz clic aquí</Anchor>.

<div id="complete-attribution-link-template" />

### Plantilla de enlace de atribución completa

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### Postbacks de instalaciones y eventos in-app

**Postback de instalación global:**

```http
https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}
```

**Postback de evento in-app global:**

`https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}&payout={monetary}&txid={event-name}`

* **userid:** ID de usuario proporcionado por PeerClick.
* **txid:** nombre real del evento in-app, establecido como **etiqueta de evento** en el panel de control de AppsFlyer para cada aplicación por parte del anunciante.

<div id="appsflyers-in-app-event-dashboard" />

### Panel de control de eventos in-app de AppsFlyer

<Image align="center" alt="Voluum_msc_new_1.png" src="https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png" />
Se puede agregar información de atribución adicional al postback mediante solicitud, como el código de país, ID de publicidad, IDFA, etc.

<div data-zendesk-anchors="starting-the-integration=comenzar-la-integraci%C3%B3n h_01HKHFT3RFWF5H349GP7MHDAYX=comenzar-la-integraci%C3%B3n h_01HM8M27S5WFJVKBG0JAFW548H=nota complete-attribution-link-template=plantilla-de-enlace-de-atribuci%C3%B3n-completa h_01HKHFT3RFDW6GZM3E72SYPJSD=plantilla-de-enlace-de-atribuci%C3%B3n-completa install-and-inapp-event-postbacks=postbacks-de-instalaciones-y-eventos-in-app h_01HKHFT3RF1PTSJ4SF9RTQ93N8=postbacks-de-instalaciones-y-eventos-in-app appsflyers-inapp-event-dashboard=panel-de-control-de-eventos-in-app-de-appsflyer h_01HKHFT3RFDVPCSKJGZPRFB55V=panel-de-control-de-eventos-in-app-de-appsflyer" />
