---
title: Integración de Everflow con AppsFlyer
metadata:
  keywords:
    - everflow
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2017-11-21T07:36:24Z'
  edited_at: '2026-08-12T12:30:21Z'
  id: 115005709185
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/115005709185
---
> **En resumen:** Everflow es un partner integrado de AppsFlyer. AppsFlyer envía Datos de atribución a Everflow para instalaciones y eventos in-app.

<div id="initiating-the-integration-with-appsflyer" />

## Iniciar la integración con AppsFlyer

**Para iniciar la integración con AppsFlyer:**

1. Completa el <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">**Formulario de información de registro de Partners**</Anchor>.
2. Una vez que hayas enviado el formulario de registro anterior, recibirás un correo electrónico de un Partner Development Manager en un plazo de 24 horas.
3. Responde a este correo electrónico con el nombre del cliente de AppsFlyer que estás incorporando. Envíanos la siguiente información mediante el widget del asistente de partners:
   * El nombre de tu empresa
   * Logotipo transparente
   * La plantilla recomendada de enlace de atribución de Everflow (usa la plantilla que aparece a continuación)
   * El valor de *pid* debe configurarse con el nombre que hayas elegido y aparecerá en los reportes de AppsFlyer.
   * Cualquier valor adicional que quieras usar.
   * Tu ID de red de Everflow (nid) y el dominio de postback para las configuraciones de postbacks de instalación y de eventos in-app

<div id="attribution-url-template" />

### Plantilla de URL de atribución

```http
https://app.appsflyer.com/{app_id}?pid=mediaName_int&clickid={transaction_id}&af_siteid={affiliate_id}
&af_sub_siteid={affiliate_source_id}&idfa={idfa}&sha1_idfa={idfa_sha1}&advertising_id={google_aid}
&af_cost_value={amount}&af_cost_currency={offer_currency}&af_cost_model=CPI
```

Si actualmente tienes una integración con AppsFlyer, ponte en contacto con nosotros mediante el widget del asistente de partners

 e incluye el nuevo postback de Everflow y la plantilla de enlace de atribución.

<div id="creating-your-attribution-link" />

## Crear tu enlace de atribución

El enlace de atribución consta del enlace de atribución base de AppsFlyer y de macros adicionales añadidas por la red publicitaria, tal como se detalla aquí. 

A continuación tienes el enlace de atribución base de AppsFlyer con una explicación detallada de cada macro:

| URL base de AppsFlyer | Nota |
| --- | --- |
| `https://app.appsflyer.com/{app_id}?` | Punto de conexión de AppsFlyer<br /><br />app\_id= ID única de la aplicación: representa el ID de la aplicación que se está promocionando |
| pid= | Nombre de la fuente de medios concatenado con \_int para identificar redes integradas. Ejemplo: medioName\_int |
| c= | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |

A continuación se muestra un enlace de atribución completo una vez que hayas añadido las macros adicionales de Everflow:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={transaction_id}&af_siteid={affiliate_id}
&af_sub_siteid={affiliate_source_id}&idfa={idfa}&sha1_idfa={idfa_sha1}&advertising_id={google_aid}
&af_cost_value={amount}&af_cost_currency={offer_currency}&af_cost_model=CPI
```

<div id="note" />

> 📘 **Nota:**
>
> * Para modelos de costo de campaña distintos de CPI, actualiza el parámetro **&af\_cost\_model=** al modelo correspondiente. Ejemplo:  CPA, CPC
> * Si ya eres un partner de AppsFlyer y actualmente estás migrando a Everflow desde una plataforma diferente, asegúrate de añadir `&af_additional_postback=1` a tus enlaces de atribución.

Para ver la lista completa de parámetros de AppsFlyer, haz clic <Anchor target="_blank" href="/partners/es/docs/postback-macros-for-ad-networks">aquí</Anchor>.

Para ver la lista completa de macros de Everflow, haz clic <Anchor target="_blank" href="https://help.everflow.io/support/solutions/articles/22000176119-parameters-and-macros">aquí</Anchor>.

<div id="integrating-your-install-and-in-app-event-postbacks" />

## Integración de tus postbacks de instalación y de eventos in-app

<div id="note-1" />

> 📘 **Nota:**
>
> * Consulta a continuación cómo formatear los postbacks de instalación y de eventos in-app para la plataforma Everflow.
> * Debes enviar a AppsFlyer tu dominio personalizado de Everflow en lugar de  [everflow\_domain\_placeholder] en los postbacks siguientes.
> * NID es el ID de red proporcionado por Everflow.

<div id="global-install-postback" />

## Postback de instalación global

```http
https://[everflow_domain_placeholder]/?nid=[everflow_network_placeholder]&transaction_id=$$click(clickid)
```

<div id="global-in-app-event-postback" />

## Postback de evento in-app global

```http
https://[everflow_domain_placeholder]/?event_id=[everflow_eventid_placeholder]&nid=[everflow_network_placeholder]&transaction_id=$$click(clickid)
```

**Event\_ID**

El ID único del evento in-app que Everflow genera para cada evento de la oferta.

**Event\_ID = el anunciante lo establece como etiqueta de evento en el Dashboard de AppsFlyer para cada aplicación**

Este es el nombre real del evento in-app de la aplicación.

Para obtener más información sobre Dynamic Event Mapping para eventos in-app, haz clic <Anchor target="_blank" href="/partners/es/docs/dynamic-event-mapping-for-in-app-events">aquí</Anchor>

<div id="event-setup-in-everflow" />

## Configuración de eventos en Everflow

**Para configurar un evento en Everflow, sigue los pasos que se indican a continuación**:

1. Para configurar los eventos en el nivel de oferta, usa la guía <Anchor target="_blank" href="https://help.everflow.io/support/solutions/articles/22000176131-add-post-conversion-events-">aquí</Anchor>.
2. Después de configurar los eventos, recuerda qué ID de evento corresponde a cada uno. En el ejemplo siguiente, el ID de evento 275 es para Compra y el ID de evento 276 es para Registro
3. Añade estos eventos al enlace de atribución de AppsFlyer.  
   Debes tener un ID de evento por cada valor de "&goalid\_x".  
   Sustituye la «x» por un número goalid distinto. Para este ejemplo, hemos usado &goalid\_1=275 y &goalid\_2=276
4. Añádelos al enlace de atribución de AppsFlyer en la página **General** después de editar la oferta. [![](https://files.readme.io/2c8e34fb91800fefac0da3c9285579833cdb17366234529001683ae008fba851-360002535645.png)](https://files.readme.io/2c8e34fb91800fefac0da3c9285579833cdb17366234529001683ae008fba851-360002535645.png)
5. Añade &goalid\_1=275&goalid\_2=276 al enlace de atribución de AppsFlyer y haz clic en Guardar.  
   Cuando termines, debería tener este aspecto (puede que tus ID de evento sean distintos): [![](https://files.readme.io/9c62bc03423febe5e990bb230c5a5c3023dba723b7c8877ead5d3328a24ee3bb-360002539489.png)](https://files.readme.io/9c62bc03423febe5e990bb230c5a5c3023dba723b7c8877ead5d3328a24ee3bb-360002539489.png)
6. Pide al anunciante que asigne esos eventos en AppsFlyer. Para obtener más información sobre el mapeo dinámico de eventos para eventos in-app.
7. Obtén el postback del evento de Everflow y envíalo a AppsFlyer; asegúrate de asignar las macros goalid correctas a los eventos correspondientes en el lado del anunciante.

<div data-zendesk-anchors="initiating-the-integration-with-appsflyer=iniciar-la-integraci%C3%B3n-con-appsflyer h_01KPJWT3XQ0WZRT7PD6GVRR6SH=iniciar-la-integraci%C3%B3n-con-appsflyer attribution-url-template=plantilla-de-url-de-atribuci%C3%B3n h_01KPJWT3XQZKMBEP7S20TNT82Q=plantilla-de-url-de-atribuci%C3%B3n creating-your-attribution-link=crear-tu-enlace-de-atribuci%C3%B3n h_01KPJWT3XQ4M7Z0G1EDD2BNGXP=crear-tu-enlace-de-atribuci%C3%B3n h_01KPJWT3XQEX5TFPKBW14CZPQ3=nota integrating-your-install-and-inapp-event-postbacks=integraci%C3%B3n-de-tus-postbacks-de-instalaci%C3%B3n-y-de-eventos-in-app h_01KPJWT3XQ86V1D429YC6FSP2Z=integraci%C3%B3n-de-tus-postbacks-de-instalaci%C3%B3n-y-de-eventos-in-app h_01KPJWT3XQ8E01ZJAZPXSFH55P=nota-1 global-install-postback=postback-de-instalaci%C3%B3n-global h_01KPJWT3XQW3TKNPR7Z6K2NCQZ=postback-de-instalaci%C3%B3n-global global-inapp-event-postback=postback-de-evento-in-app-global h_01KPJWT3XQCM2BWTJVDXSVSBQP=postback-de-evento-in-app-global event-setup-in-everflow=configuraci%C3%B3n-de-eventos-en-everflow h_01KPJWT3XQ9K4WPVCSGGGC4Z6S=configuraci%C3%B3n-de-eventos-en-everflow" />
