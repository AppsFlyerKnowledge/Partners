---
title: Integración de Cake con AppsFlyer
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
  edited_at: '2026-08-12T12:30:15Z'
  id: 207273986
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/207273986
---
> **De un vistazo:** Las ad network que usan CAKE pueden recibir datos de atribución de AppsFlyer sobre instalaciones y eventos in-app.

<div id="base-attribution-link" />

## Enlace de atribución de base

A continuación tienes el enlace de atribución base con una explicación detallada de cada parámetro:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| URL base de AppsFlyer | Nota |
| --- | --- |
| https://app.appsflyer.com | Punto de conexión de AppsFlyer |
| id\_aplicación | ID único de la aplicación: valor dinámico que cambia por cada aplicación promocionada |
| PID | El nombre de la fuente de medios incluye **\_int** para identificar la red **integrada** en los servidores de AppsFlyer |
| C | Nombre de la campaña |

<div id="recommended-attribution-link-parameters" />

### Parámetros recomendados de los enlaces de atribución

| Parámetro de AppsFlyer | Macros de CAKE | Nota |
| --- | --- | --- |
| clickid | #oreqid# | ID de solicitud de cada sesión de usuario: **obligatorio** |
| af\_siteid | #affid# | ID del afiliado que promociona la oferta: **opcional** |

Para obtener la lista completa de parámetros de AppsFlyer, haz clic <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">aquí</Anchor>

Para obtener la lista completa de macros de CAKE, haz clic <Anchor target="_blank" href="https://support.getcake.com/support/solutions/articles/5000566463-tokens">aquí</Anchor>.

<div id="complete-attribution-link-template" />

### Plantilla de enlace de atribución completa

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#oreqid#
```

<div id="install-and-in-app-event-postbacks" />

## Postbacks de instalaciones y eventos in-app

<div id="global-install-postback" />

### Postback de instalación global

```http
https://{company-domain}.com/p.ashx?f=pb&r=(Click-ID)
```

<div id="global-in-app-event-postback" />

### Postback global de evento in-app

```http
Clic-ID
```

`{Company-Domain}`, el nombre de ID de red (dominio) proporcionado por CAKE.  
e= Se configura como **Event Tag** en el dashboard de AppsFlyer para cada App por el anunciante. Este es el nombre real del evento in-app de la aplicación.  
Para ver la estructura completa del postback de CAKE, haz clic aquí

<div id="appsflyer-in-app-events-dashboard" />

### Dashboard de eventos in-app de AppsFlyer

![IAEP.png](https://files.readme.io/3ce734c3930649fdb0b119cd6e12e135e6bcba19225862e9e93b93991451fc8b-360002326529.png)

Se puede añadir información de atribución adicional al postback previa solicitud, como el código de país, el ID de publicidad, el IDFA, etc.

<div id="finalizing-your-registration" />

## Finaliza tu registro

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros utilizando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para Partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de anuncios Partners <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div data-zendesk-anchors="base-attribution-link=enlace-de-atribuci%C3%B3n-de-base 01EZPMKP0AFM26H2ZG9FY1D2S4=enlace-de-atribuci%C3%B3n-de-base recommended-attribution-link-parameters=par%C3%A1metros-recomendados-de-los-enlaces-de-atribuci%C3%B3n 01EZPMKP0A7DBV5KAGZ08C3R49=par%C3%A1metros-recomendados-de-los-enlaces-de-atribuci%C3%B3n complete-attribution-link-template=plantilla-de-enlace-de-atribuci%C3%B3n-completa 01EZPMKP0AH1MB0XYE3PXQPP0V=plantilla-de-enlace-de-atribuci%C3%B3n-completa install-and-inapp-event-postbacks=postbacks-de-instalaciones-y-eventos-in-app 01EZPMKP0A2D0PB41GD04HX9JX=postbacks-de-instalaciones-y-eventos-in-app global-install-postback=postback-de-instalaci%C3%B3n-global 01EZPMKP0AVAJRP8YM48T4GV47=postback-de-instalaci%C3%B3n-global global-inapp-event-postback=postback-global-de-evento-in-app 01EZPMKP0AM7JD7HWW7BCJDQF3=postback-global-de-evento-in-app appsflyer-inapp-events-dashboard=dashboard-de-eventos-in-app-de-appsflyer 01EZPMKP0AJTYT0G9E8G833KT0=dashboard-de-eventos-in-app-de-appsflyer finalizing-your-registration=finaliza-tu-registro h_01HY03H1PMWZX3T12RZFV15CFE=finaliza-tu-registro" />
