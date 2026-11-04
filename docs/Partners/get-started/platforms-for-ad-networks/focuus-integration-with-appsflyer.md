---
title: Integración de FOCUUS con AppsFlyer
metadata:
  keywords:
    - Focuus
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
  created_at: '2016-10-02T05:18:19Z'
  edited_at: '2026-08-12T12:30:24Z'
  id: 213374546
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/213374546
---
> **De un vistazo:** Las ad network que utilizan FOCUUS pueden usar la solución de modelado probabilístico de AppsFlyer para recibir datos de atribución sobre instalaciones y eventos in-app.

<div id="creating-your-attribution-link" />

## Crear tu enlace de atribución

El enlace de atribución consta del enlace de atribución base de AppsFlyer que aparece a continuación y de macros adicionales añadidas por la ad network.

A continuación se muestra el enlace de atribución base de AppsFlyer con una explicación detallada por macro:

| URL base de AppsFlyer | Descripción |
| --- | --- |
| https://app.appsflyer.com | Punto de conexión de AppsFlyer |
| id\_aplicación | ID único de la aplicación |
| PID | El nombre de la fuente de medios incluye \_int para identificar la red integrada en los servidores de AppsFlyer |
| C | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |

<div id="recommended-attribution-link-parameters" />

### Parámetros recomendados de los enlaces de atribución

| Parámetro de AppsFlyer | Macros de FOCUUS | Nota |
| --- | --- | --- |
| **clickid** | **`{tid}`** | **ID de solicitud de cada sesión de usuario** - **Obligatorio** |
| af\_siteid | `{publisher_id}` | ID del afiliado que promociona la oferta - Opcional |

Para consultar la lista completa de parámetros de AppsFlyer, <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#parámetros-del-enlace-de-atribución">haz clic aquí</Anchor>.

FOCUUS permite un número ilimitado de macros y puedes ponerles el nombre que quieras; haz <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#parámetros-del-enlace-de-atribución">clic</Anchor> <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827379-traffic-source-template-tokens-macros">aquí</Anchor>.

<div id="complete-attribution-link-template" />

### Plantilla de enlace de atribución completa

`https://app.appsflyer.com/com.appsflyer?pid={traffic_source}&clickid={tid}&af_siteid={publisher_id}`

Este enlace de atribución se configura en el <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827784-adding-a-new-link">destino</Anchor> de tu campaña de FOCUUS.

<div id="install-and-in-app-event-postbacks" />

## Postbacks de instalaciones y eventos in-app

Para crear tus postbacks de instalación y de eventos in-app en **FOCUUS**

1. Crea un <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827775-events">evento nuevo</Anchor> (instalación y cualquier otro evento in-app).
2. <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Genera un píxel</Anchor> (postback) para implementarlo.
3. Copia la URL del postback que aparece en el cuadro etiquetado como <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Server2Server Pixel</Anchor>.
4. Sustituye el TRANSACTION\_ID por la macro de AppsFlyer «**clickid**»  
   `https://pixel.focuusing.com/event.php?type=imp&tid={clickid}`

**Parámetros opcionales del postback**

| Macros de FOCUUS | Nota | Ejemplo |
| --- | --- | --- |
| event\_value | Valor de payout para cada tipo de evento | `https://pixel.focuusing.com/event.php?type=cpi&tid={Your_TRANSACTION_ID}&eid=49816&event_value={25}` |

**El nombre del evento (instalación, registro, etc.) aparece por defecto en el píxel generado. por ejemplo,**

* `https://traffic.focuusing.com/install?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/conversion?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/ftd?tid={TRANSACTION_ID}`

<div data-zendesk-anchors="creating-your-attribution-link=crear-tu-enlace-de-atribuci%C3%B3n 01JFT11W3GWZ3QFYPHEZTS7EX7=crear-tu-enlace-de-atribuci%C3%B3n recommended-attribution-link-parameters=par%C3%A1metros-recomendados-de-los-enlaces-de-atribuci%C3%B3n 01JFT11W3QWT08KMGEPGK7MV5R=par%C3%A1metros-recomendados-de-los-enlaces-de-atribuci%C3%B3n complete-attribution-link-template=plantilla-de-enlace-de-atribuci%C3%B3n-completa 01JFT11W3Y7HRB7FYS1K173G2W=plantilla-de-enlace-de-atribuci%C3%B3n-completa install-and-inapp-event-postbacks=postbacks-de-instalaciones-y-eventos-in-app 01JFT11W3YMN4RBW0WFTQ9EADK=postbacks-de-instalaciones-y-eventos-in-app" />
