---
title: Atribución view-through de CTV-to-Mobile para ad networks
metadata:
  keywords:
    - Attribution
    - Ad Networks
    - Partners
    - CTV
    - CTV Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roi-tamir
    - CTV Attribution
    - Ad Networks
  created_at: '2022-08-21T06:49:24Z'
  edited_at: '2026-08-28T00:37:41Z'
  id: 8528418936977
  locale: es
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/es/articles/8528418936977
---
> **At a glance:** Atribuye instalaciones de apps móviles a anuncios vistos en dispositivos de TV conectada (CTV).

<div id="ctv-to-mobile-app-attribution-for-ad-networks" />

## Atribución de CTV-to-Mobile para ad networks

Con las URL de impresiones multiplataforma de AppsFlyer, puedes atribuir instalaciones de aplicaciones móviles a anuncios mostrados en CTV. Varias instalaciones dentro del mismo hogar pueden atribuirse a la misma impresión de anuncio en CTV.

![Diagrama del flujo de atribución de CTV a app móvil](https://files.readme.io/401bcb083e1cc618794cb302668f7271cf825a5a6045ff10055e0164baf423a1-19774176963473.jpg)

La atribución view-through de CTV a aplicación móvil usa una <Anchor target="_blank" href="/marketers/es/docs/set-up-cross-platform-links-for-multi-device-campaigns#setup">URL de impresión OneLink</Anchor> basada en una plantilla OneLink multiplataforma (con un ID de plantilla) creada por los anunciantes. Esto permite a los anunciantes agrupar varias apps de diferentes plataformas (por ejemplo, apps para Android e iOS) utilizando una única URL.

Cuando los usuarios ven el anuncio en CTV, envías a AppsFlyer la URL de impresión en tiempo real. 

URL de ejemplo:

```
https://impressions.onelink.me/{template_id}?pid=__media_source__&af_xplatform=true&af_xplatform_vt_lookback=24h&af_siteid=__CSITE__&c=__CAMPAIGN_NAME__&af_channel=__PLACEMENT__&af_c_id=__CAMPAIGN_ID__&af_adset=__AID_NAME__&af_adset_id=__AID__&af_ad=__CID_NAME__&af_ad_id=__CID__&af_source_platform=__source_platform__&af_source_device_category=__device_category__&af_ad_type=__CTYPE__&af_ip=__IP__&af_ua=__UA__&redirect=false
```

AppsFlyer te envía postbacks después de cada conversión.

> 📘 **Note**
>
> Esta función solo está disponible para partners designados. Ponte en contacto con tu Partner Development Manager (PDM) si te interesa.

<Accordion title="Configurar la atribución de CTV a móvil">

**Para configurar la atribución view-through de CTV-to-Mobile con un anunciante**:

1. Asegúrate de ser un <Anchor target="_blank" href="/partners/es/docs/getting-started-onboarding-guide-for-ad-networks">partner integrado de AppsFlyer</Anchor>, de tener los postbacks correctamente configurados y de haber [probado tu integración de CTV a aplicación móvil](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#test-partner-integration) con AppsFlyer.
2. Asegúrate de que la URL tenga los [parámetros obligatorios](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#parameters), además de cualquier otro parámetro que quieras.
3. Envía a AppsFlyer la dirección IP y el agente de usuario. Estos son necesarios para la atribución de visualización de CTV a aplicación móvil. Se pueden enviar de cualquiera de estas formas:
   1. Como los parámetros `af_ip` y `af_ua` en la URL de impresión.
   2. Como `<X-Forwarded-For>` y `<User-Agent>` parámetros en los encabezados de la solicitud.

</Accordion>

<Accordion title="Probar la integración del partner">

**Para probar la atribución view-through de CTV-to-Mobile**:

1. Usa las siguientes aplicaciones de prueba: com.appsflyer.android.deviceid y id1192323960
2. Ponte en contacto con el equipo de Partner Solutions de AppsFlyer para recibir una URL de prueba. Para hacerlo, inicia sesión en tu <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">dashboard de Partners</Anchor> y, en el menú superior, haz clic en **ayuda** > **Contact our team**.
   * URL de ejemplo: `https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false`
3. Confirma que tu ID de partner en el parámetro `pid` es correcto.
4. Introduce tu dirección IP en el parámetro `af_ip`.
5. Introduce tu agente de usuario en el parámetro `af_ua`.
6. Introduce la URL en un navegador de desktop.
7. En tu dispositivo móvil, ve a la tienda de aplicaciones y descarga, instala y abre la app.
8. Aparece una nueva instalación en AppsFlyer junto con el postback correspondiente. Si no ves la instalación o no recibes el postback, ponte en contacto con el equipo de Partner Solutions.

</Accordion>

<Accordion title="Parámetros">

Los siguientes parámetros se utilizan para proporcionar datos de atribución y medición a los anunciantes.

| Parámetro | Obligatorio | Descripción |
| --- | --- | --- |
| template\_id | ✓ | El ID de la <Anchor target="_blank" href="/marketers/es/docs/create-a-onelink-template">plantilla OneLink</Anchor>. La plantilla contiene configuraciones básicas de predicción para las aplicaciones del anunciante y es la base para crear otros enlaces. Nota: No codifiques nunca el valor de `template_id`. |
| pid | ✓ | El identificador del partner, asignado por AppsFlyer a la fuente de medios (ad network) que publica el anuncio. |
| af\_xplatform | ✓ | <ul><li>Lo establece el anunciante para indicar si el enlace admite la atribución multiplataforma.</li><li>Valores: true/false</li></ul> |
| af\_xplatform\_vt\_lookback | - | Ventana configurable que indica el número de horas tras la impresión durante las cuales la instalación de la app puede atribuirse a la impresión. Valores de parámetros disponibles: 1h - 72h (horas). El valor predeterminado es 24 h. |
| af\_ip | ✓ | <ul><li>La dirección IP del dispositivo CTV que muestra el anuncio.</li><li>Si la dirección IP no se envía en la URL, debe enviarse en los encabezados de la solicitud para que AppsFlyer pueda realizar la atribución de CTV a aplicación móvil.</li></ul> |
| af\_ua | ✓ | <ul><li>El agente de usuario del dispositivo CTV que muestra el anuncio.</li><li>Si el agente de usuario no se envía en la URL, debe enviarse en los encabezados de la solicitud para que AppsFlyer pueda realizar la atribución de CTV a aplicación móvil.</li></ul> |
| af\_source\_platform | - | <ul><li>Una lista fija de valores para representar el sistema operativo donde ocurre la impresión.</li><li>Valores:<ul><li>Android</li><li>ios</li><li>tizen</li><li>webos</li><li>smartcast</li><li>roku</li><li>Windows Phone</li><li>vidaa</li><li>PlayStation</li><li>sitio web</li></ul></li></ul> |
| af\_source\_device\_category | - | <ul><li>Lista predefinida de valores para representar el tipo de dispositivo donde se produce la impresión.<ul><li>tv</li><li>mobile\_phone</li><li>Escritorio</li><li>tablet</li><li>set\_top\_box</li><li>games\_console</li><li>unknown\_device\_category</li><li>media\_player</li></ul></li></ul> |

Otros parámetros que se pueden añadir a la URL se encuentran en el <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">artículo sobre la estructura y los parámetros del enlace de atribución</Anchor>.

</Accordion>

<Accordion title="Características y limitaciones">

| Caducado | Description |
| --- | --- |
| Ventana de atribución | Entre 1 y 72 horas, según el parámetro de ventana de lookback `af_xplatform_vt_lookback`. |
| Reorientación | <ul><li>Reatribución: Compatible con multiplataforma a dispositivos móviles. No es compatible con otras plataformas.</li><li>Re-engagement: No compatible</li></ul> |
| Método de atribución | Atribución por visualización mediante modelado probabilístico (dirección IP) |
| Atribución por hogar | Compatible. Es decir, se pueden atribuir múltiples instalaciones dentro del mismo hogar a la misma impresión de anuncio de CTV. |
| Probar la integración del partner | No disponible para redes publicitarias que han sido señaladas por altas tasas de fraude de app móvil a app móvil o están afiliadas a diferentes fuentes de medios señaladas. |

</Accordion>

<div data-zendesk-anchors="ctvtomobile-app-attribution-for-ad-networks=atribuci%C3%B3n-de-ctv-to-mobile-para-ad-networks h_01HE2X91GTDTPKKFBRRYYFMHDW=atribuci%C3%B3n-de-ctv-to-mobile-para-ad-networks" />
