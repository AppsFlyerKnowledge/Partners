---
title: Guía de privacidad avanzada y macros de postback para redes de publicidad
metadata:
  keywords:
    - Ad Networks
    - Partners
    - ios14
    - SKAD
    - Advanced Privacy
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-07-27T07:09:37Z'
  edited_at: '2026-08-12T12:28:07Z'
  id: 360011316197
  locale: es
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/es/articles/360011316197
---
> **De un vistazo:** intercambio de datos con partners cuando la privacidad avanzada está habilitada. Instrucciones para las redes de publicidad sobre cómo configurar postbacks de privacidad avanzada. ¡Atención! Nota: Este artículo no está relacionado con los postbacks de SKAdNetwork ni está destinado a ser utilizado por anunciantes.

<div id="advanced-privacy-for-ad-networks-news" />

> 📄 **Noticias sobre privacidad avanzada para redes de publicidad**
>
> El mecanismo de postback de privacidad avanzada que se describe en este artículo funciona cuando se cumplen todas las condiciones siguientes:
>
> * El dispositivo del usuario ejecuta iOS 14.5+.
> * La privacidad avanzada está activada.

<Image align="center" alt="AdvancedPrivacy.png" src="https://files.readme.io/2a80740637c1003e03bc169df274bf0fa6240ee850c7fd6e967c4abea234e0d1-360018213598.png" />

En este artículo se explica lo siguiente:

* El impacto del uso compartido de datos de privacidad avanzada en los partners
* Los requisitos de la [URL de clic](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements) para poder optar a la atribución
* La configuración de tus [postbacks](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification) de privacidad avanzada en el panel de control de AppsFlyer
* La diferencia entre [privacidad avanzada y SKAdNetwork](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#ap-vs-skadnetwork)

<div id="ad-network-advanced-privacy-data-sharing-principles" />

## Principios del uso compartido de datos de privacidad avanzada en redes de publicidad

A partir de iOS 14.5+, el <Anchor target="_blank" href="/marketers/es/docs/apply-aggregated-advanced-privacy-framework">Marco de privacidad avanzada agregada</Anchor> (AAP) de AppsFlyer brinda a los anunciantes la capacidad de controlar la disponibilidad de los datos de atribución a nivel de usuario proporcionados a través de la plataforma de AppsFlyer.

En el contexto de las redes de publicidad, el marco de AAP se implementa con privacidad avanzada (AP). Para facilitar la comprensión, los términos privacidad avanzada y AP se utilizan indistintamente en este artículo.

La privacidad avanzada (AP) no afecta la disponibilidad de datos agregados para partners o redes de publicidad.

**Qué datos se ven afectados por la AP**

Cuando AP está activado, los datos que los clientes pueden poner a disposición mediante postbacks u otros métodos de reporte solo se agregan. No se incluyen datos a nivel de usuario, incluidos los reportes relacionados con fraude de Protect360.

En el contexto de los postbacks, se usan distintos tipos de postback en función de si hay un ID de anunciante disponible y de otros factores.

Puedes ver la configuración de AP actual, por aplicación, en el panel de control de AppsFlyer. Ve a **Configuración** > **Integraciones activas** > selecciona tu red de publicidad > **pestaña Integración.** La configuración predeterminada está activada.

<Image align="center" alt="APforPartners2.png" src="https://files.readme.io/e4fb5617a47635f24dc83881c2be3d18b770200a576cb67bd3312e6fc2c123e1-360018154777.png" />

<div id="types-of-templates-for-sending-postbacks" />

#### Tipos de plantillas para enviar postbacks

* **Plantilla normal:** tu plantilla de integración existente con AppsFlyer. Contiene macros de identificación de usuario y de datos de atribución. Esta plantilla se utiliza para enviar postbacks que contienen datos de atribución a nivel de usuario.
* **Plantilla de Privacidad Avanzada**: una plantilla sin macros de identificador de usuario. Esta plantilla se utiliza para enviar postbacks que contienen datos de atribución agregados.   
  **Nota:** Si se requiere un postback AP y no has completado la integración de AP, no se envía ningún postback. Puedes configurar la integración de AP utilizando nuestra herramienta de [administración de postbacks.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback)

<div id="note" />

> 📘 **Nota**
>
> * Si un usuario otorga el consentimiento de ATT en las aplicaciones tanto del anunciante como del publisher ("doble consentimiento"), se envían postbacks periódicos a las redes de publicidad atribuidas y no atribuidas.
> * **Excepción:** Para las instalaciones atribuidas a Apple Search Ads (ASA), ASA envía postbacks de instalación a la red de publicidad incluso cuando la privacidad avanzada está activada para el anunciante en las siguientes condiciones:
>   * el usuario no dio su consentimiento
>   * el postback de instalación de la red de publicidad está configurado en **Todas las fuentes de medios, incluyendo las orgánicas**
>   * la red de publicidad no es compatible con la privacidad avanzada

<div id="type-of-postback-used" />

### Tipo de postback utilizado

La siguiente tabla describe los tipos de postback según la disponibilidad del ID de anunciante y el estado de Advanced Privacy.

<div id="postback-type-for-ios-145" />

#### Tipo de postback para iOS 14.5+

<table><thead><tr><th rowspan="2">Estado de AP</th><th colspan="2">Autorizado</th><th rowspan="2">Tipo de plantilla de postback al partner atribuido\* que admite AP </th><th rowspan="2">Tipo de plantilla de postback al partner atribuido\* que no admite AP </th><th rowspan="2">Partner de postback no atribuido\*</th></tr><tr><th>Aplicación de publisher</th><th>Aplicación de anunciante</th></tr></thead><tbody><tr><td>en</td><td>disponible</td><td>No autorizado</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla AP</a> (datos agregados)</td><td>Sin postback</td><td>Ninguna</td></tr><tr><td>en</td><td>No autorizado</td><td>disponible</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla AP</a> (datos agregados)</td><td>Sin postback</td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Autorizado</a></p><p>Los <a href="/marketers/es/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">campos de atribución</a> no están disponibles.\*</p></td></tr><tr><td>en</td><td>disponible</td><td>disponible</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla normal</a>. Esto incluye ID disponibles como: IDFA, IDFV, CUID, ID de clic y campos de atribución. </td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla normal</a>. Esto incluye ID disponibles como: IDFA, IDFV, CUID, ID de clic y campos de atribución. </td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla normal</a> que incluye los ID disponibles. Los <span><a href="/marketers/es/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">campos de atribución</a> no están disponibles.\*</span> </td></tr><tr><td>en</td><td>No autorizado</td><td>No autorizado</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipo-de-postback-utilizado"><span>Plantilla AP</span></a> (datos agregados)</td><td>Sin postback</td><td>Ninguna</td></tr><tr><td>Desactivado</td><td>No considerado</td><td>No considerado</td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla normal</a></td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla normal</a></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-plantillas-para-enviar-postbacks">Plantilla normal</a>.</p><p>Los <a href="/marketers/es/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">campos de atribución</a> no están disponibles.\*</p></td></tr></tbody></table>

**(\*) Principios para el intercambio de datos con partners**

Para cualquier evento dado, varios partners de la red de publicidad pueden tener derecho a un postback. Los postbacks enviados son los siguientes:

* Partner atribuido: red de publicidad acreditada con el evento
* Partner no atribuido: partner integrado no acreditado con el evento, cuando **Postback de eventos in-app** > **Opción de envío** está establecido en **todas las fuentes de medios, incluidas las orgánicas.** Si la aplicación del anunciante tiene el consentimiento de ATT, el postback contiene los ID de usuario sin datos atribuidos. (Esta opción no es compatible con todas las redes de publicidad).

  <Image align="center" alt="InAppEventAll.png" src="https://files.readme.io/e24037f75b2b82797031eb13d5e063b8c2006812491e69674ff066ac830919f7-35847850644881.png" />

<div id="web-campaigns" />

### Campañas web

La AP se comporta de manera diferente cuando la red de publicidad sirve un anuncio en la web.

Para indicar si un clic proviene de la web o de una aplicación, debes enviar el parámetro `af_media_type=web` o `af_media_type=app` en la URL del clic.

Si no envías `af_media_type`, el valor predeterminado es `app`.

<div id="postback-type-used-for-ios-145-when-ap-is-on" />

#### Tipo de postback utilizado para iOS 14.5+ cuando la AP está activada

<table><thead><tr><th colspan="2">Estado de ATT</th><th rowspan="2">Tipo de postback para un partner atribuido\*</th><th rowspan="2">Tipo de postback para un partner no atribuido\*</th></tr><tr><th>Aplicación de publisher</th><th>Aplicación de anunciante</th></tr></thead><tbody><tr><td>N/D</td><td>No autorizado</td><td>Privacidad avanzada</td><td>Ninguna</td></tr><tr><td>N/D</td><td>Autorizado</td><td>Normal. Solo ID de nivel de usuario.</td><td>Normal. Nivel de usuario con los siguientes ID:</td></tr></tbody></table>

<div id="integration" />

## Integración

Actualiza las URL de tus clics y completa la integración de privacidad avanzada.

<div id="click-url-requirements" />

<Accordion title="Requisitos de la URL de clic">

En muchos casos, según el consentimiento de ATT de usuario, el identificador de anunciante (IDFA) no estará disponible en la aplicación del publisher, la aplicación del anunciante o en ambas. En estos casos, AppsFlyer permite la atribución utilizando la <Anchor target="_blank" href="/marketers/es/docs/appsflyer-attribution-model#aggregated-advanced-privacy-aap">privacidad avanzada agregada</Anchor> y el <Anchor target="_blank" href="/marketers/es/docs/appsflyer-attribution-model#probabilistic-modeling">modelado probabilístico.</Anchor>

**[Práctica recomendada]** Para maximizar tus atribuciones, envía todos los parámetros enumerados.

1. Agrega los siguientes parámetros las URL de clic:

<table><thead><tr><th>Identificador</th><th>Parámetro de clic</th><th>Ejemplo</th></tr></thead><tbody><tr><td>Campaña</td><td>C</td><td>US_20_30</td></tr><tr><td>ID de campaña</td><td>af_c_id</td><td>12345</td></tr><tr><td>Conjunto de anuncios</td><td>af_conjunto de anuncios</td><td>ADSET_1</td></tr><tr><td>ID de conjunto de anuncios</td><td>af_adset_id</td><td>56789</td></tr><tr><td>Anuncio </td><td>af_anuncio</td><td>creative_name</td></tr><tr><td>ID de anuncio</td><td>id_del_anuncio_af</td><td>34567</td></tr><tr><td>ID de sitio</td><td>af_siteid</td><td>abcdefgh12345678</td></tr><tr><td>ID de sub sitio</td><td>af_sub_siteid</td><td>abcdefgh12345678</td></tr><tr><td>Canal</td><td>af_canal</td><td>channel_name</td></tr><tr><td>Tipo de anuncio</td><td>af_ad_type</td><td>Video</td></tr><tr><td>Modelo de dispositivo iOS\*</td><td>af_model</td><td><p>El modelo del dispositivo. Valores permitidos:</p><ul><li>iphone (todo en minúsculas)</li><li>ipad (todo en minúsculas)</li></ul></td></tr><tr><td>Sistema operativo\*</td><td>af_os</td><td>Versión del sistema operativo</td></tr><tr><td colspan="3">\* Es posible que también se proporcione información a través del agente de usuario. En este caso, el valor enviado con el identificador específico tiene prioridad.</td></tr></tbody></table>

   Incorporar detalles de la campaña a la URL de clic

   El ejemplo siguiente muestra cómo agregar los detalles de tu campaña a la URL de clic:

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adsetname}&af_adset_id={adset ID}&af_ad={adname}&af_ad_id={ad ID}&af_ad_type={Adtype}&af_siteid={PublisherId}` |
| --- |

2. Agrega los siguientes parámetros obligatorios a las URL de clic*:

   <div id="caution" />

   > ❗️ **Precaución**
   >
   > Si tu URL de clic no pasa los parámetros obligatorios, no se te acreditará la mayoría de las instalaciones que manejes.


   * IP
   * Agente de usuario

   * No se requiere ninguna acción al enviar un clic usando un referente de HTTP simple que redirige a AppsFlyer. 

   Utiliza el método de extracción descrito para incorporar los parámetros a la URL de clic cuando se utilice cualquiera de los siguientes métodos:

   * Redirigir a través de la aplicación
   * Clics de servidor a servidor (también conocido como S2S)

   <div id="parameters-for-advanced-privacy-attribution" />

   #### Parámetros para la atribución de privacidad avanzada

   <Table>
     <thead>
       <tr>
         <th>
           Parámetro
         </th>
         <th>
           Obligatorio
         </th>
         <th>
           Método de extracción
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           **Idioma y configuración regional del dispositivo**

           af\_lang
         </td>
         <td>
           No
         </td>
         <td>
           NSString *language = [[NSLocale preferredLanguages] objectAtIndex:0];

           [Recomendado] Proporciona el idioma y la configuración regional; por ejemplo, en-US.
         </td>
       </tr>
       <tr>
         <td>
           **Agente de usuario**

           af\_ua
         </td>
         <td>
           Sí
         </td>
         <td>
           Extrae el agente de usuario con el formato:

           ```
           Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+13_3_1  
           +like+Mac+OS+X%29 AppleWebKit%2F605.1.15+%28KHTML%2C  
           +like+Gecko%29+Mobile%2F15E148
           ```

           * **No** extraigas el *agente de usuario* de CFNetwork, extrae el otro.
           * El agente de usuario debe estar codificado en URL.
         </td>
       </tr>
       <tr>
         <td>
           **Dirección IP del dispositivo**

           af\_ip
         </td>
         <td>
           Sí
         </td>
         <td>
           La mejor opción: si está disponible, proporciona la IP del dispositivo en el parámetro af\_ip.

           Siguiente opción: si está disponible, AppsFlyer usará la IP en X-Fordered-For.
         </td>
       </tr>
     </tbody>
   </Table>

   Incorporar parámetros a la URL de clic

   Para pasar estos parámetros obligatorios en el enlace de atribución de clics, usa esta referencia:

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad-type}&af_siteid={PublisherId}&af_ua={USER-AGENT}&af_lang={LANGUAGE}&af_ip={IP}` |
| --- |

   Ejemplo

| GET `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset` name\}&af\_adset\_id=`{adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />&af\_ua=Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2012\_1\_4%20  <br />like%20Mac%20OS%20X%29%20AppleWebKit%<br /><br />`2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%2F16D57&af_lang=en-US&af_ip=11.11.1.11` |
| --- |

   * Los parámetros de consulta deben estar codificados por URL.

   **Pasar datos en encabezados de URL de clics**

   Para pasar los campos en el encabezado de la URL de clic, usa la siguiente referencia:

| GET `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset` name\}&af\_adset\_id=`{adset ID}&af_ad={ad name}&af_ad_id={ad ID}`<br />`&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />`accept-language: en-US,en;q=0.`<br /><br />`User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)`<br /><br />`AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148`<br /><br />`X-Forwarded-For: 11.11.1.11, 222.222.2.222` |
| --- |

</Accordion>

<div id="advanced-privacy-postback-specification" />

<Accordion title="Especificación de postbacks de privacidad avanzada">

Para recibir los postbacks de privacidad avanzada, debes configurar una integración de privacidad avanzada además de la integración de postbacks regular. Puedes configurar el [postback de privacidad avanzada](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback) tú mismo en el panel de control de AppsFlyer.

**Diferencias entre la plantilla normal y la plantilla de privacidad avanzada**

* La hora del postback no se correlaciona con las horas reales de los eventos.
* Macros de marca de tiempo:
  * Para las instalaciones y los eventos in-app, las marcas de tiempo se redondean a la hora en que ocurrieron. Por ejemplo, 22:55:30 se reporta como 22:00:00.
  * Se reportan usando la zona horaria UTC. Ejemplo de marca de tiempo: (2020-07-20 20:00:00)
* Los siguientes parámetros no están disponibles en los postbacks de privacidad avanzada: ID de clic, ID de usuario de cliente, ID de AppsFlyer, identificador de anunciante (IDFA), identificador de proveedor (IDFV), modelo del dispositivo, versión de sistema operativo, operador.

**Acción requerida por la red de publicidad para integrar:**

1. [Configura tu postback de privacidad avanzada en el panel de control de AppsFlyer.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback)
2. <Anchor target="_blank" href="/partners/es/docs/ios-integration-testing-for-ad-networks">Prueba la integración de privacidad avanzada.</Anchor>

<div id="important" />

> 🚧 **¡Importante!**
>
> * Para poder distinguir entre postbacks para eventos legítimos y postbacks rechazados, debes configurar las macros de postbacks rechazados.
> * Para habilitar el postback de instalaciones/eventos rechazados, ponte en contacto con nosotros utilizando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.

<div id="advanced-privacy-postback-endpoint-complete-as-required" />

#### Punto de conexión de postback de privacidad avanzada [completar según sea necesario]

| Tipo de postback |
| --- |
| Instalación |
| Dentro de la aplicación |

<div id="advanced-privacy-attribution-macros-available" />

#### Macros de atribución de privacidad avanzada disponibles

<table><thead><tr><th>Macro de postback (nombre)</th><th>Observaciones</th><th>Parámetros base para todas los postbacks</th><th>Parámetros opcionales para eventos in-app </th><th>Parámetros opcionales para atribución rechazada</th></tr></thead><tbody><tr><td>af_anuncio</td><td>Nombre de la creatividad</td><td>Sí</td><td> </td><td> </td></tr><tr><td>id_del_anuncio_af</td><td>34567</td><td>Sí</td><td> </td><td> </td></tr><tr><td>af_ad_type</td><td>Como: banner, pie de página, video</td><td>Sí</td><td> </td><td> </td></tr><tr><td>af_conjunto de anuncios</td><td>ADSET_1</td><td>Sí</td><td> </td><td> </td></tr><tr><td>af_adset_id</td><td>56789</td><td>Sí</td><td> </td><td> </td></tr><tr><td>id_aplicación</td><td>-</td><td>Sí</td><td> </td><td> </td></tr><tr><td>nombre_aplicación</td><td>-</td><td>Sí</td><td> </td><td> </td></tr><tr><td>attributed_touch_hour</td><td><p>Redondeado hacia abajo hasta la hora más cercana. </p><p>Formato: ver nota (1)</p></td><td>Sí</td><td> </td><td> </td></tr><tr><td>tipo_táctil_atribuido</td><td>Como: clic, impresión</td><td>Sí</td><td> </td><td> </td></tr><tr><td>razón_bloqueo</td><td>Se relaciona con las reglas de validación/Protect360</td><td> </td><td> </td><td>Sí</td></tr><tr><td>valor_del_motivo_bloqueado</td><td>Se relaciona con las reglas de validación/Protect360</td><td> </td><td> </td><td>Sí</td></tr><tr><td>submotivo_bloqueado</td><td>Se relaciona con las reglas de validación/Protect360</td><td> </td><td> </td><td>Sí</td></tr><tr><td>id_paquete</td><td>Según lo establecido por el anunciante</td><td>Sí</td><td> </td><td> </td></tr><tr><td>C</td><td>Nombre de campaña, como US_20_30</td><td>Sí</td><td> </td><td> </td></tr><tr><td>af_c_id</td><td>ID de campaña, como 12345</td><td>Sí</td><td> </td><td> </td></tr><tr><td>af_canal</td><td>Nombre del canal</td><td>Sí</td><td> </td><td> </td></tr><tr><td>código_de_país</td><td>Código de país ISO registrado en la conversión</td><td>Sí</td><td> </td><td> </td></tr><tr><td>event_hour</td><td><p>Redondeado hacia abajo hasta la hora más cercana. </p><p>Formato: ver nota (1)</p></td><td>Sí</td><td> </td><td> </td></tr><tr><td>nombre_del_evento</td><td>Según lo reportado por la aplicación</td><td> </td><td>Sí</td><td> </td></tr><tr><td>ingresos_evento</td><td>Importe de ingresos en la divisa del evento</td><td> </td><td>Sí</td><td> </td></tr><tr><td>event_revenue_<br/>currency</td><td>Código de divisa de los ingresos</td><td> </td><td>Sí</td><td> </td></tr><tr><td>ingresos_evento_usd</td><td>Ingresos convertidos a USD</td><td> </td><td>Sí</td><td> </td></tr><tr><td>Autorizado</td><td><p>Redondeado hacia abajo hasta la hora más cercana. </p><p>Formato: ver nota (1)</p></td><td>Sí</td><td> </td><td> </td></tr><tr><td>is_first</td><td>Verdadero si esta es la primera vez que un usuario final específico activó este evento in-app</td><td> </td><td>Sí</td><td> </td></tr><tr><td>es_primario</td><td><p>Usar para eliminar datos duplicados</p><p>Booleano: 0, 1</p></td><td> </td><td>Sí</td><td> </td></tr><tr><td>es_retargeting</td><td><p>Usar para eliminar datos duplicados </p><p>Formato: ver nota (2)</p></td><td>Sí</td><td> </td><td> </td></tr><tr><td>is_reengagement</td><td>Formato: ver nota (2)</td><td> </td><td>Sí</td><td> </td></tr><tr><td>is_reattribution</td><td><p>Usar para eliminar datos duplicados </p><p>Formato: ver nota (2)</p></td><td>Sí</td><td> </td><td> </td></tr><tr><td>match_type</td><td>Como: id_matching, probabilistic</td><td>Sí</td><td> </td><td> </td></tr><tr><td>Ingresos asociados al SKU en la moneda indicada en el campo <code>event_revenue_currency</code>.</td><td>Nombre/ID del evento correspondiente en la plataforma de la red de publicidad</td><td> </td><td>Sí</td><td> </td></tr><tr><td>Identificador de origen</td><td>Como: ios, Android</td><td>Sí</td><td> </td><td> </td></tr><tr><td>postback_id</td><td>ID de postback único</td><td>Sí</td><td> </td><td> </td></tr><tr><td>retargeting_<br/>conversion_type</td><td>Como: re-engagement, reatribución</td><td>Sí</td><td> </td><td> </td></tr><tr><td>af_siteid</td><td>abcdefgh12345678</td><td>Sí</td><td> </td><td> </td></tr><tr><td>af_sub_siteid</td><td>abcdefgh12345678</td><td>Sí</td><td> </td><td> </td></tr><tr><td colspan="5"><p>Notas:</p><p>(1) Formatos de marca de tiempo disponibles:</p><ul><li>[Predeterminado] Cadena: AAAA-MM-DD HH: MM:SS</li><li>Tiempo Epoch: marca de tiempo Unix de 10 dígitos </li></ul><p>(2) Formato booleano disponible</p><ul><li>[Predeterminado] Numérico: 0, 1 </li><li>Cadena: <em>false</em>, <em>true</em> </li></ul></td></tr></tbody></table>

</Accordion>

<div id="setting-up-your-advanced-privacy-postback" />

<Accordion title="Configuración de tu postback de privacidad avanzada">

Configura tu postback de AP con la opción de administración de postbacks en el panel de control de AppsFlyer.

**Requisitos previos**:

* Debes tener una integración activa con AppsFlyer para administrar tu postback de privacidad avanzada. Ponte en contacto con nosotros usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor> para <Anchor target="_blank" href="/partners/es/docs/getting-started-onboarding-guide-for-ad-networks">crear una integración</Anchor>.
* ![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) La administración de postbacks la realiza el administrador de la cuenta; los miembros del equipo no tienen acceso.

**Para configurar el postback:**

1. Haz clic en el menú desplegable de la parte superior derecha> **Administración de postbacks**.
2. Selecciona el tipo de postback: **Privacidad avanzada.**
3. Activa el creador.

   <Image align="center" alt="postback-management-enter-endpoint_en-us.png" src="https://files.readme.io/4ea0ffc61d1ecdb11d3c745876c29a942fde4133b8ebb54a1426a73c1dc63b16-360018215218.png" />
4. Introduce la **dirección de punto de conexión**: la URL del punto de conexión a la que AppsFlyer envía los postbacks. Introduce las URL relevantes para instalaciones y/o eventos in-app.
5. Introduce los parámetros que se incluirán en los postbacks:

   * **Nombre del parámetro**: nombre de la pantalla del parámetro de AppsFlyer
   * **Tu parámetro de recepción**: el parámetro de recepción respectivo de tu lado
   * **Valor de parámetro** (disponible para algunos parámetros): elige el formato del valor. Por ejemplo, para los valores booleanos, elige si deseas recibirlos como "true"/"false" o 1/0.
   * **Instalación**: marca la casilla para incluir el parámetro en el postback de instalación.
   * **Evento in-app**: marca la casilla para incluir el parámetro en el postback de evento in-app.

   <Image align="center" alt="postback-management-parameters_en-us.png" src="https://files.readme.io/818ef31df9c4e349ca26b5421a0ba0582ed5f7f9fae39f1d0e4ec3b7562f4192-360018213698.png" />

   Lista completa de [macros de postback de privacidad avanzada.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification)
6. **[Opcional]** Agrega parámetros personalizados que no proporcione AppsFlyer:

   <Image align="center" alt="postback-management-custom-parameters_en-us.png" src="https://files.readme.io/6bca46e1d39c6822b0e041eb1dcbb1b2d40e42fa062c34877c8cbf0c2d2847d6-16589581250321.png" />
7. Revisa la vista previa final de la plantilla de postback para asegurarte de que todo está correcto.

   <Image align="center" alt="postback-management-template_en-us.png" src="https://files.readme.io/b5e41cad37859365c7818c4561620f8a78250c207d8326dae53ed9b522fe3716-360018213718.png" />
8. Haz clic en **Guardar**. Ten en cuenta que cuando guardas el postback, los cambios entran en vigor inmediatamente.

Si tienes algún problema, ponte en contacto con nosotros a través del widget del asistente para partners.

</Accordion>

<div id="additional-information" />

## Información adicional

<div id="ap-for-analytics-partners" />

<Accordion title="AP para partners de analíticas">

Los postbacks se envían a los partners de analíticas de la siguiente manera:

* AP desactivada: postback a nivel de usuario sin restricciones.
* AP activado: el tipo de postback depende de la fuente del usuario y de la disponibilidad del ID de anunciante, como se detalla en la siguiente tabla.

<div id="analytics-partner-postback-type-according-to-att-status-and-user-source" />

#### Tipo de postback de partner de Analytics según el estado de ATT y la fuente de usuario

<table><thead><tr><th rowspan="2">Fuente de usuario</th><th colspan="2">Autorizado</th><th rowspan="2">Tipo de postback al partner de analíticas</th></tr><tr><th>Aplicación de publisher</th><th> Aplicación de anunciante</th></tr></thead><tbody><tr><td rowspan="3"><p>No orgánicas </p></td><td>disponible</td><td>disponible</td><td>Regular</td></tr><tr><td>No autorizado</td><td>disponible</td><td>Ninguna</td></tr><tr><td>Cualquier valor</td><td>No autorizado</td><td>Ninguna</td></tr><tr><td>Orgánico o web</td><td>N/D</td><td>disponible</td><td>Regular</td></tr><tr><td>Orgánico o web</td><td>N/D</td><td>No autorizado</td><td>Ninguna</td></tr></tbody></table>

</Accordion>

<div id="ap-vs-skadnetwork" />

<Accordion title="AP frente a SKAdNetwork">

<Anchor target="_blank" href="/partners/es/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> es una tecnología de atribución proporcionada por Apple para dispositivos iOS. La privacidad avanzada es parte del marco de <Anchor target="_blank" href="/marketers/es/docs/apply-aggregated-advanced-privacy-framework">Privacidad avanzada agregada de AppsFlyer</Anchor> (AAP) y se relaciona con la atribución realizada por AppsFlyer. La AAP ofrece a los anunciantes la capacidad de controlar la disponibilidad de los datos de atribución a nivel de usuario a través de la plataforma de AppsFlyer. Por lo general, las redes de publicidad admiten la integración de AP y SKAdNewtork.

</Accordion>

<div data-zendesk-anchors="h_01HJR7MWPM9XA4BXHDRD2K6D56=noticias-sobre-privacidad-avanzada-para-redes-de-publicidad ad-network-advanced-privacy-datasharing-principles=principios-del-uso-compartido-de-datos-de-privacidad-avanzada-en-redes-de-publicidad h_01HJR7MWPNYNMKZ3R8C3BB5EVG=principios-del-uso-compartido-de-datos-de-privacidad-avanzada-en-redes-de-publicidad types-of-templates-for-sending-postbacks=tipos-de-plantillas-para-enviar-postbacks h_01HJR7MWPN92BDJRK734P6YXSK=tipos-de-plantillas-para-enviar-postbacks h_01HJR7MWPN71TP0KWVVBHPC0H2=nota type-of-postback-used=tipo-de-postback-utilizado h_01HJR7MWPNJEDNDT1ZY7P78HMG=tipo-de-postback-utilizado postback-type-for-ios-145=tipo-de-postback-para-ios-145 h_01HJR7MWPNESP8BDC4D6Y7SBFZ=tipo-de-postback-para-ios-145 web-campaigns=campa%C3%B1as-web h_01HJR7MWPNXHHCSQ6BGCNRBHZK=campa%C3%B1as-web postback-type-used-for-ios-145-when-ap-is-on=tipo-de-postback-utilizado-para-ios-145-cuando-la-ap-est%C3%A1-activada h_01HJR7MWPNQCCNGHQY5RQHQ6D1=tipo-de-postback-utilizado-para-ios-145-cuando-la-ap-est%C3%A1-activada integration=integraci%C3%B3n h_01HJR7MWPP7YGRXJQR29F3ERHH=integraci%C3%B3n h_01HJR7MWPPAXK18KER56E30G8R=click-url-requirements h_01HJR7MWPPRN8XYVSS7HX7NQB9=precauci%C3%B3n parameters-for-advanced-privacy-attribution=par%C3%A1metros-para-la-atribuci%C3%B3n-de-privacidad-avanzada h_01HJR7MWPPK2HET3XYW4WBFAZ1=par%C3%A1metros-para-la-atribuci%C3%B3n-de-privacidad-avanzada h_01HJR7MWPQ60F4CESKRRMTQ7HX=advanced-privacy-postback-specification h_01HJR7MWPQ8K06A1YM4KV4RTN8=importante advanced-privacy-postback-endpoint-%5Bcomplete-as-required%5D=punto-de-conexi%C3%B3n-de-postback-de-privacidad-avanzada-completar-seg%C3%BAn-sea-necesario h_01HJR7MWPQX9SXJZMBS6QR07WD=punto-de-conexi%C3%B3n-de-postback-de-privacidad-avanzada-completar-seg%C3%BAn-sea-necesario advanced-privacy-attribution-macros-available=macros-de-atribuci%C3%B3n-de-privacidad-avanzada-disponibles h_01HJR7MWPQKH52XMD6H9TJ0SM3=macros-de-atribuci%C3%B3n-de-privacidad-avanzada-disponibles h_01HJR7MWPRC44K908A4EAPN9GV=setting-up-your-advanced-privacy-postback additional-information=informaci%C3%B3n-adicional h_01HJR7MWPRVFR6YN56Y0DGBAXH=informaci%C3%B3n-adicional h_01HJR7MWPR6ACNYVZHK7YPHQGP=ap-for-analytics-partners analytics-partner-postback-type-according-to-att-status-and-user-source=tipo-de-postback-de-partner-de-analytics-seg%C3%BAn-el-estado-de-att-y-la-fuente-de-usuario h_01HJR7MWPRZDJNSZNB981WB5Z1=tipo-de-postback-de-partner-de-analytics-seg%C3%BAn-el-estado-de-att-y-la-fuente-de-usuario h_01HJR7MWPR3YR7E9S49P9ZZ3CT=ap-vs-skadnetwork" />
