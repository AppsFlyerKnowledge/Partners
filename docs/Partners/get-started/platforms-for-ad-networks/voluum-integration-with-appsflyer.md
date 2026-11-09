---
title: Integración de Voluum con AppsFlyer
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
  created_at: '2016-01-11T14:46:09Z'
  edited_at: '2026-08-12T12:30:48Z'
  id: 207274016
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/207274016
---
> **De un vistazo:** Las ad networks que usan Voluum pueden utilizar la solución de Modelado probabilístico de AppsFlyer para recibir Datos de atribución sobre instalaciones y eventos in-app.

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
| c= | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |

**Parámetros recomendados de los enlaces de atribución:**

| Parámetro de AppsFlyer | Macros de volumen | Nota |
| --- | --- | --- |
| &clickid= | `{clickid}` | ID de transacción único de la sesión del usuario: **obligatorio** |
| &af\_siteid= | `{trafficsource.id}` | ID de la fuente de tráfico: **opcional** |

** Para obtener la lista completa de parámetros de AppsFlyer, <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">haz clic aquí</Anchor>

** Para obtener la lista completa de macros de Voluum, <Anchor target="_blank" href="http://feedback.voluum.com/knowledgebase/articles/318681-click-urls">haz clic aquí</Anchor>

<div id="complete-attribution-link-template" />

### Plantilla de enlace de atribución completa

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### Postbacks de instalaciones y eventos in-app

Postback de instalación global:

```http
https://{Company-Domain}.voluumtrk.com/postback?cid={clickid}
```

Postback de evento in-app global:

```http
https://{Company-Domain}.trackvoluum.com/postback?cid={clickid}&payout={monetary}&txid={event-name}
```

** `{Company-Domain}` es el nombre del ID de red (dominio) proporcionado por Voluum.  
** txid= Se configura como **Event Tag** en el dashboard de AppsFlyer para cada App por parte del anunciante. Este es el nombre real del evento in-app de la aplicación.

<div id="appsflyers-in-app-event-dashboard" />

### Panel de control de eventos in-app de AppsFlyer

<Image align="center" alt="Voluum_msc_new_1.png" src="https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png" />
** Se puede agregar información de atribución adicional al postback mediante solicitud, como el código de país, ID de publicidad, IDFA, etc.

<div id="finalizing-your-registration" />

## Finalizando tu registro

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de anuncios Partners <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div data-zendesk-anchors="starting-the-integration=comenzar-la-integraci%C3%B3n 01JFT0VZZ5KVMKYRD222JT55NH=comenzar-la-integraci%C3%B3n complete-attribution-link-template=plantilla-de-enlace-de-atribuci%C3%B3n-completa 01JFT0VZZ7B1RRY82B65GWF4P7=plantilla-de-enlace-de-atribuci%C3%B3n-completa install-and-inapp-event-postbacks=postbacks-de-instalaciones-y-eventos-in-app 01JFT0VZZ86KYXSVE1QBD2V0HF=postbacks-de-instalaciones-y-eventos-in-app appsflyers-inapp-event-dashboard=panel-de-control-de-eventos-in-app-de-appsflyer 01JFT0VZZ9A4JWG38KPH0CNQ72=panel-de-control-de-eventos-in-app-de-appsflyer finalizing-your-registration=finalizando-tu-registro 01JFT0VZZATFYY75QPCPKZF3S6=finalizando-tu-registro" />
