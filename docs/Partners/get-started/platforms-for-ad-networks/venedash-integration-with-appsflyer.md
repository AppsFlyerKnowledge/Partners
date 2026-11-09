---
title: integración de venedash con AppsFlyer
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
  created_at: '2020-04-24T21:20:47Z'
  edited_at: '2026-09-11T00:38:21Z'
  id: 360007705617
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/360007705617
---
> **De un vistazo:** Envía datos de atribución desde AppsFlyer a venedash. AppsFlyer puede enviar a venedash datos de instalación y de eventos in-app.

<div id="venedash-integration-setup" />

## configuración de la integración de venedash

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros utilizando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de anuncio Partners <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

**Para habilitar la integración con AppsFlyer:**

1. En **AppsFlyer**, ve a **Collaborate** > **Integraciones de Partners > Integraciones activas** y selecciona Venedash en la lista de partners.
2. En la pestaña **Integración**, habilita **Activate partner**.
3. Ve a la pestaña **Enlace de atribución** y genera un enlace de atribución con los siguientes parámetros obligatorios:

   

| Parámetro de AppsFlyer | parámetro de Venedash | Description |
| --- | --- | --- |
| &clickid= | `{#ydrid#}` | ID de solicitud de cada sesión de usuario |
| &af\_siteid= | `{#ydr_pid#}` | ID del afiliado que promociona la oferta |
| &advertising\_id | `{#android_adv#}` | ID de dispositivo de Android |
| &idfa= | `{#iosidfa#}` | ​ID del dispositivo iOS |

   Ten en cuenta que el parámetro pid lo completa el equipo de AppsFlyer.  
   Ejemplo:

   ```http
   https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#">https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#
   ```

   <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">Saber más</Anchor> sobre los parámetros del enlace de atribución.
4. En Venedash, crea una oferta y pega el enlace de atribución de AppsFlyer en el campo URL de destino.

   <Image align="center" alt="venedash-destination_url-es_es.png" src="https://files.readme.io/2a284eab8d25f57f1bfa2981e2d86bf16bce16b64b61858fdb819d5ac14eac20-360016242798.png" />

<div data-zendesk-anchors="venedash-integration-setup=configuraci%C3%B3n-de-la-integraci%C3%B3n-de-venedash h_01HKW87R2DGCXHZSVSV9D9203Z=configuraci%C3%B3n-de-la-integraci%C3%B3n-de-venedash" />
