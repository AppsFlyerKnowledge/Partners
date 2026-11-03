---
title: Integración de Trackier con AppsFlyer
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
  edited_at: '2026-08-12T12:30:40Z'
  id: 360006111917
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/360006111917
---
> **De un vistazo:** Las ad network que usan Trackier pueden recibir Datos de atribución de AppsFlyer sobre instalaciones y eventos in-app.

Para iniciar la integración, proporciona a AppsFlyer tanto la URL del enlace de atribución como la URL del postback. Las URL son necesarias para fines de reportar. En este artículo se explica cómo crear estas URL.

## URL del enlace de atribución

En esta sección se proporcionan el enlace de atribución base y las descripciones de los parámetros relacionados.

### URL del enlace de atribución base

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={click_id}&af_siteid={publishedr_id}\n&af_c_id={camp_id}
```

| URL base de AppsFlyer | Definición | Nota |
| --- | --- | --- |
| https://app.appsflyer.com | URL base | Punto de conexión de AppsFlyer |
| id\_aplicación | ID de aplicación | Valor dinámico que varía para cada App |
| pid= | Nombre de fuente de medios | **\_int** identifica una red **integrada** |
| c= | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. | Nombre asignado por el anunciante |

### Parámetros de enlaces de atribución

> 📘 **Nota**
>
> Los enlaces de atribución de la siguiente tabla son **obligatorios**.
>
> Consulta las listas completas de parámetros para:
>
> * <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">AppsFlyer</Anchor>
> * <Anchor target="_blank" href="https://trackier.com/support/kb/tracking-macros/">Trackier</Anchor>

| Parámetro de AppsFlyer | Macro de Trackier | Nota |
| --- | --- | --- |
| &clickid= | `{click_id}` | Solicita el ID de cada sesión de usuario |
| &af\_siteid= | `{publisher_id}` | ID del afiliado que promociona una oferta |
| &af\_c\_id= | `{camp_id}` | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |

## URL de postback para eventos de instalación y eventos in-app

Esta sección ofrece ejemplos de URL de postback y parámetros para eventos de instalación y eventos in-app.

### URL de postback para **iOS**

#### Postback de instalación global

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}
```

#### Postback de evento in-app global

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}&goal_value={event-name}
```

### URL de postback para **Android**

#### Postback de instalación global

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}
```

#### Postback de evento in-app global

```http
https://yourdomain.com/acquisition?click_id={click_id}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}&goal_value={event-name}
```

### Parámetros de postback

| URL base de AppsFlyer | Nota |
| --- | --- |
| yourdomain.com | <ul><li>Nombre del ID de red (dominio)</li><li>Lo proporciona Trackier</li></ul> |
| event-name | <ul><li>Nombre del evento in-app</li><li>Lo define el anunciante</li></ul> |
| security\_token | Lo proporciona Trackier |
| Código de país, ID de publicidad, IDFA, etc. | [Opcional] Información de atribución que se puede añadir a un postback |

## Finalización del registro

¿Ya te has integrado con AppsFlyer? Envíanos las URL a través del <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.

¿Todavía no te has integrado con AppsFlyer? Completa la <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">solicitud de registro de partners publicitarios</Anchor>.

<div data-zendesk-anchors="attribution-link-url=url-del-enlace-de-atribuci%C3%B3n 01JFT1SETSSMD0Z0EEQZCYPDB6=url-del-enlace-de-atribuci%C3%B3n base-attribution-link-url=url-del-enlace-de-atribuci%C3%B3n-base 01JFT1SETTCEC1CAGT89SGNZNX=url-del-enlace-de-atribuci%C3%B3n-base attribution-link-parameters=par%C3%A1metros-de-enlaces-de-atribuci%C3%B3n 01JFT1SEVJTM09KHEKS51KQB7F=par%C3%A1metros-de-enlaces-de-atribuci%C3%B3n 01JFT1SEVJR7TW06CAZWGMBZEB=nota postback-urls-for-install-and-inapp-events=url-de-postback-para-eventos-de-instalaci%C3%B3n-y-eventos-in-app 01JFT1SEWCM9DFRANRJRDSG5DC=url-de-postback-para-eventos-de-instalaci%C3%B3n-y-eventos-in-app ios-postback-urls=url-de-postback-para-ios 01JFT1SEWCSS585NF8P0T251PZ=url-de-postback-para-ios global-install-postback=postback-de-instalaci%C3%B3n-global 01JFT1SEWD3A0JP6MRM1QXKX53=postback-de-instalaci%C3%B3n-global global-inapp-event-postback=postback-de-evento-in-app-global 01JFT1SEWDT1CWHHTVWVACDT0B=postback-de-evento-in-app-global android-postback-urls=url-de-postback-para-android 01JFT1SEWD0HA5WKC83V8HYAA2=url-de-postback-para-android global-install-postback::1726dfc2=postback-de-instalaci%C3%B3n-global-1 01JFT1SEWDY7882HGY032SPGP7=postback-de-instalaci%C3%B3n-global-1 global-inapp-event-postback::ab23c9cb=postback-de-evento-in-app-global-1 01JFT1SEWDYKTWDE536A4ZY34G=postback-de-evento-in-app-global-1 postback-parameters=par%C3%A1metros-de-postback 01JFT1SEWEZQF38K9V9M6TNP3N=par%C3%A1metros-de-postback finalizing-your-registration=finalizaci%C3%B3n-del-registro 01JFT1SEWTPX9BH7N1FPN4NJJW=finalizaci%C3%B3n-del-registro" />
