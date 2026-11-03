---
title: Macros de postbacks para ad networks
metadata:
  keywords:
    - postbacks
    - Advertisers
    - Ad Networks
    - macros
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
  created_at: '2016-01-11T14:41:40Z'
  edited_at: '2026-08-12T12:28:29Z'
  id: 207273946
  locale: es
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/es/articles/207273946
---
> **En resumen:** Como una ad network, puedes definir el contenido y los puntos de conexión de los postbacks que se te envían como parte de tu integración con AppsFlyer. Los postbacks se relacionan con el engagement del usuario de la aplicación, como instalaciones, eventos in-app, re-engagements, etc.

Guías relacionadas de postback de partners integrados:

* <Anchor target="_blank" href="/partners/es/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Privacidad avanzada</Anchor>
* <Anchor target="_blank" href="/partners/es/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/es/docs/rejected-attribution-postbacks-to-integrated-partners">Postbacks de atribución rechazados</Anchor>

## Postbacks para ad networks

* **Configuración de postback:** Para solicitar cambios en tu configuración de postbacks, usa el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor> o contacta con tu gerente de desarrollo de partners de AppsFlyer.
* **Tipos de postback**: Los postbacks están disponibles para los eventos in-app e instalaciones y los eventos in-app e instalaciones bloqueadas debido al fraude identificado por Protect360 o a la violación de las reglas de validación de segmentación.

### Fuentes de datos de postbacks

| Fuente | Descripción |
| --- | --- |
| <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">Parámetros del enlace de atribución</Anchor> | Los parámetros proporcionados por el partner en las URL de impresiones o clics<br /><br />Ejemplo: parámetro de ID de clic en el enlace de atribución "&click\_id=CLICK\_ID". |
| ID de partner en AppsFlyer | IDs únicos proporcionados al anunciante por parte del partner<br /><br />Ejemplos: ID de aplicación, ID de cuenta, ID de usuario, ID de red. |
| Información derivada del SDK | Información extraída del dispositivo por el SDK de AppsFlyer.<br /><br />Ejemplo: los IDs de dispositivos iOS pueden extraerse utilizando "&IDFA=(idfa)" en el postback. |
| Derivado de la plataforma de AppsFlyer | Información derivada de la plataforma de AppsFlyer. |
| Protect360 y reglas de validación | Información sobre instalaciones identificadas como fraude e instalaciones que violan las reglas de segmentación de la campaña y sus eventos in-app asociados. |

## Macros de postbacks

Cuando se incluyen en un postback, las macros se sustituyen por datos relevantes para el usuario. Por ejemplo, para obtener la dirección IP del usuario que instala la aplicación, incluye `country_code=(ip)` en la estructura del postback. Las macros admitidas se enumeran en la siguiente tabla:

Las columnas de la tabla a continuación tienen el siguiente significado:

* **Fuente:** De dónde proceden los datos.
  * Enlace: Enlaces de atribución
  * SDK: El SDK de AppsFlyer incorporado en la aplicación o la API de servidor a servidor
  * AF: Tras el procesamiento por parte de AppsFlyer.
* **Enviar todo**:  En caso afirmativo, puedes recibir los datos sobre instalaciones y eventos atribuidos a otras redes u orgánicos (es decir, los no atribuidos a ti). (es decir, los no atribuidos a ti).
* [Base] Macros para todos los postbacks Macros relevantes para la instalación, eventos in-app y postbacks de eventos rechazados
* **[Opcional]** para eventos in-app y eventos rechazados como se indica en la columna (rechazado, in-app).

### Macros: instalaciones, eventos in-app y eventos rechazados

| Macro de postback (nombre) | Fuente | Enviar todo | Descripción | [Base] Macros para todos los postbacks | [Opcional] Eventos rechazados in-app |
| --- | --- | --- | --- | --- | --- |
| <span id="advertising_id"></span>advertising\_id | SDK | Sí | ID del dispositivo que puede ser restablecido por el usuario, también conocido como GAID. También disponible como: (sha1-advertiserId) | Sí |  |
| <span id="af_ad"></span>af\_anuncio | ENLACE | No | Nombre del anuncio (<Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">ver más</Anchor>) proporcionado por el anunciante/publisher | Sí | Sí |
| <span id="af_ad_id"></span>id\_del\_anuncio\_af | ENLACE | No | Proporcionado por el anunciante/publisher | Sí | Sí |
| <span id="af_ad_type"></span>af\_ad\_type | Enlace | No | Usa la siguiente convención de nomenclatura:<ul><li>**text:** una unidad de anuncio que contiene solo texto, por ejemplo, un resultado de búsqueda.</li><li>**banner:** un formato básico que aparece en la parte superior o inferior de la pantalla del dispositivo.</li><li>**interstitial:** un anuncio de página completa que aparece durante los descansos en la experiencia actual.</li><li>**video:** un video estándar, es decir, no recompensado.</li><li>**rewarded\_video:** una unidad de anuncio que ofrece recompensas in-app a cambio de ver un video.</li><li>**playable:** una unidad de anuncio que contiene una vista previa interactiva de la experiencia de la aplicación.</li><li>**sponsored\_content:** un enlace incluido en una pieza de contenido patrocinado, como un artículo publicitario</li><li>**audio:** un anuncio de audio.</li></ul> | Sí | Sí |
| <span id="af_adset"></span>af\_conjunto de anuncios | Enlace | No | <ul><li>Proporcionado por el anunciante/publisher.</li><li>El conjunto de anuncios es un nivel intermedio en la jerarquía entre Campaña y Anuncio. <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">Ver más</Anchor></li></ul> | Sí | Sí |
| <span id="af_adset_id"></span>af\_adset\_id | Enlace | No | Proporcionado por el anunciante/publisher | Sí | Sí |
| <span id="af_c_id"></span>af\_c\_id | Enlace | No | Proporcionado por el anunciante/publisher | Sí | Sí |
| <span id="af_siteid"></span>af\_siteid | Enlace | No | <ul><li>ID único que identifica al publisher que muestra el anuncio. <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#site-id-parameter">Saber más</Anchor></li></ul> | Sí | Sí |
| <span id="af_subsite_id"></span>af\_subsite\_id | Enlace | No | <ul><li>ID de subred publicitaria/ID del publisher.</li><li>Si, además del editor principal (ID del sitio), hay un subeditor o deseas incluir información adicional, como tipo de anuncio/ubicación dentro de la aplicación, como banner, intersticial, vídeo, etc., utiliza af\_sub\_siteid. Por ejemplo: af\_sub\_siteid =ABCD\_4567</li></ul> | Sí | Sí |
| <span id="af_validated"></span>af\_validated | AF | Sí | Indica si la compra fue validada con éxito. Valores posibles: verdadero o falso. | Sí |  |
| <span id="af_validation_type"></span>af\_validation\_type | AF | Sí | Indica el tipo de validación realizada. Valores posibles: roi360\_purchase, roi360\_subscription o Básico. | Sí |  |
| <span id="app_id"></span>id\_aplicación | SDK | Sí | El ID de la aplicación tal como lo reporta la aplicación | Sí |  |
| <span id="app_name"></span>nombre\_aplicación | SDK | Sí | Nombre de la aplicación configurado por el anunciante | Sí |  |
| <span id="app_version"></span>version\_app | SDK | Sí | Nombre de versión de la aplicación configurado por el desarrollador en el código de la aplicación | Sí |  |
| <span id="appsflyer_id"></span>appsflyer\_id | SDK | Sí | Identificador único de AppsFlyer registrado tras la conversión | Sí |  |
| <span id="att01"></span>att-0-1 | SDK | Sí | Posibles valores:<ul><li>1: El estado de la ATT es authorized o af\_authorized.</li><li>0: Cualquier otro estado de la ATT.</li></ul> | Sí |  |
| <span id="attstatus"></span>att-status | SDK | Sí | El <Anchor target="_blank" href="/marketers/es/docs/att-implications-ios-14-and-deprecation-of-lat#valor-att">estado de la ATT</Anchor> reportado por iOS. Como authorized, not\_determined.<br /><br />En algunos casos no hay ningún valor y se devuelve "". | Sí |  |
| <span id="attributed_touch_type"></span>tipo\_táctil\_atribuido | SDK | No | Valores posibles: click, impression, TV, pre-install | Sí |  |
| <span id="blocked_reason"></span>razón\_bloqueo | AF | No | Motivo de las reglas de validación/fraude | No | Rechazado |
| <span id="blocked_reason_value"></span>valor\_del\_motivo\_bloqueado | AF | No | Valor del motivo de las reglas de validación/fraude (como ID de sitio) | No | Rechazado |
| <span id="blocked_sub_reason"></span>submotivo\_bloqueado | AF | No | Submotivo de las reglas de validación/fraude | No | Rechazado |
| <span id="bundle_id"></span>id\_paquete | SDK | Sí | iOS: Identificación para hacer coincidir una sola aplicación o un grupo de aplicaciones en iOS (consulta el ID del paquete del desarrollador de Apple) Android: Nombre de la aplicación | Sí |  |
| <span id="c"></span>C | Enlace | No | Proporcionado por el anunciante/publisher. Los nombres de campaña que superan los 100 caracteres de longitud se muestran en el dashboard como “c\_name\_exceeded\_max\_length” | Sí | Sí |
| <span id="country_code"></span>código\_de\_país | AF | Sí | Código de país con ISO 3166 (alfa-2) Ejemplo: US, CN. | Sí |  |
| <span id="event_name"></span>nombre\_del\_evento | SDK | Sí | Nombre asignado a un evento | No | Dentro de la aplicación |
| <span id="event_revenue_currency"></span>ingresos\_evento | SDK | Sí | Valor de evento reportado por SDK usando event\_revenue\_currency o la divisa que has seleccionado. | No | Dentro de la aplicación |
| {"event_revenue"}  <br />{"_moneda"} | SDK | Sí | El código de divisa del ingreso del evento reportado en el evento o la divisa que has seleccionado. | No | Dentro de la aplicación |
| <span id="event_revenue_usd"></span>event\_revenue\_USD | AF | Sí | Valor del evento en USD | No | Dentro de la aplicación |
| <span id="event_time"></span>event\_time | SDK | Sí | Hora del evento | No | Dentro de la aplicación |
| <span id="event_value"></span>event\_value | SDK | Sí | El evento in-app incluye atributos con valores, que se pueden enviar por completo en el postback en formato JSON. URL codificada mediante la macro (encode). | No | Dentro de la aplicación |
| <span id="idfa"></span>idfa | SDK | Sí | ID de publicidad que el usuario puede restablecer y que se encuentra en dispositivos iOS. También disponible como: (sha1-idfa) | Sí |  |
| <span id="idfv"></span>idfv | SDK | Sí | Identificador único por usuario y por proveedor en los dispositivos iOS | Sí |  |
| <span id="imei"></span>imei | SDK | Sí | Un número único utilizado para identificar teléfonos móviles | Sí |  |
| <span id="install_time"></span>hora\_de\_instalación | SDK | Sí | Marca de tiempo de instalación | Sí |  |
| <span id="install_unix_ts"></span>install\_unix\_ts | SDK | Sí | Marca de tiempo de instalación en formato unix | Sí |  |
| <span id="is_attributed"></span>is\_attributed | AF | Sí | Indicador que marca si la instalación o el evento se atribuye a esta fuente de medios | Sí |  |
| <span id="is_contrib"></span>is\_contrib | AF | Sí | Indica si la ad network estuvo entre los 3 principales contribuyentes a una instalación.<ul><li>Si la ad network no ganó la atribución pero está entre los 3 principales contribuyentes, `is_contrib=1`.</li><li>Si la ad network ganó la atribución, `is_contrib=0`.</li><li>Si la ad network no está entre los 3 principales contribuyentes, `is_contrib=0`.</li></ul> | Sí |  |
| <span id="is_lat"></span>es\_lat | SDK | Sí | Limit ad tracking (LAT): iOS: Desde iOS 14, Apple retiró LAT. Determina el estado de privacidad del usuario usando ATT. En este caso, ignora is\_lat. Antes de iOS 14, si es verdadero, el IDFA no está disponible y se establece en 0. Android: Cuando es verdadero, el usuario ha optado por no participar en anuncios basados en intereses. Esto no impide que se recopile el ID de publicidad de Google (GAID). | Sí |  |
| <span id="is_organic"></span>es\_orgánico | AF | Sí | Si se envía un postback de instalación para todas las fuentes de medios, incluyendo orgánico, entonces la ad network recibirá una indicación de si una instalación fue orgánica o no orgánica. | Solo instalaciones |  |
| <span id="is_primary_attribution"></span>es\_atribución\_primaria | AF | Sí | Cuando es falso, consulta is\_retargeting. | No | Dentro de la aplicación |
| <span id="is-reinstall"></span>es\_reinstalación | AF | Se instala el | Si es verdadero, el evento se reporta como <Anchor target="_blank" href="/marketers/es/docs/measure-reinstalls">una reinstalación</Anchor>. |  |  |
| <span id="is_retargeting"></span>es\_retargeting | Enlace | No | Se debe usar conjuntamente con is\_primary\_attribution. Obtén más información sobre la <Anchor target="_blank" href="/marketers/es/docs/resolve-retargeting-double-attribution">doble atribución de los eventos de retargeting</Anchor>.<br /><br />Si es verdadero (1), el evento se reporta como parte de una campaña de retargeting y la fuente de medios es la fuente de medios de retargeting.<br /><br />Si es falso (0) y is\_primary\_attribution es falso, el evento es parte de una campaña de retargeting, pero la fuente de medios a la que se hace referencia es la fuente de medios de atribución del usuario. | No |  |
| <span id="language"></span>Indicador de atribución AF | SDK | Sí | Idioma (configuración regional) reportado por el dispositivo y establecido por el sistema operativo del dispositivo. | Sí |  |
| <span id="oaid"></span>oaid | SDK | Sí | ID que el usuario puede restablecer en algunos dispositivos Android, generalmente como alternativa a GAID | Sí |  |
| <span id="partner_event_id"></span>partner\_event\_id | AF | Sí | Nombre/ID del evento correspondiente en la plataforma del partner | No | Dentro de la aplicación |
| <span id="platform"></span>Identificador de origen | SDK | Sí | Plataforma del dispositivo: iOS, Android o Windows Mobile | Sí |  |
| <span id="retargeting-conversion-type"></span>tipo\_conversion\_retargeting | AF | No | Un indicador que marca si se trata de una reatribución o un re-engagement | Solo retargeting |  |

### Macros solo para eventos in-app

Los ejemplos a continuación se relacionan con los postbacks de eventos in-app disponibles para los partners.

> 📄 **Ejemplo**
>
> La plantilla de postback de evento "&event=(event)&json=(encode)" se tradujo al siguiente postback para un evento af\_purchase específico:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> El valor JSON decodificado de este postback es
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

#### **Valores codificados**

Es posible que los postbacks incluyan caracteres irregulares no alfanuméricos. Para transferir estos valores correctamente a través de postbacks, la URL de AppsFlyer codifica valores no alfanuméricos.

Para decodificar o codificar un postback usa un <Anchor target="_blank" href="https://www.urldecoder.org/">servicio web de codificación.</Anchor>

## Postbacks de muestra

### Ejemplos de postbacks de instalación generales

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)
&advertising_id=(advertiser_id)&android_id=(android_id)
&install_time=(install_unix_ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?&site_id=(publisher_id)&
device_ip=(ip)&;idfa=(idfa)&install_time=(install_unix_ts)
```

</Tab>
</Tabs>

### Ejemplos de postbacks de eventos in-app generales

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)&
device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android_id)&
install_time=(install_unix_ts)&event_name=(event_name)&currency=(currency)&
json=(event_value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?clickid=(clickid)&site_id=(publisher_id)&
device_ip=(ip)&idfa=(idfa)&install_time=(install_unix_ts)
&event_name=(event_name)&currency=(currency)&json=(event_value)
```

</Tab>
</Tabs>

### Ejemplo de postbacks de eventos in-app

Parámetros de evento:

* Nombre del evento: af\_revenue
* Ingresos por evento: 120.00
* Moneda del evento: USD
* Valor del evento: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

Postback:

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-ad-networks=postbacks-para-ad-networks 01JHFZWJT74GNA6J5MYMQBGDWX=postbacks-para-ad-networks postback-data-sources=fuentes-de-datos-de-postbacks 01JHFZWJT978TTXB7FQ6AVG1ZS=fuentes-de-datos-de-postbacks postback-macros=macros-de-postbacks 01JHFZWJTTP66NHZRG0RQAY3W8=macros-de-postbacks macros%E2%80%94installs-inapp-events-and-rejected-events=macros-instalaciones-eventos-in-app-y-eventos-rechazados 01JHFZWJTXD2K4RJ8RDWXKSYDD=macros-instalaciones-eventos-in-app-y-eventos-rechazados inapp-event-only-macros=macros-solo-para-eventos-in-app 01JHFZWK3FQ5HCX9NDEKT6SPT1=macros-solo-para-eventos-in-app 01JHFZWK3F2E31WE5N1G0T0ZHA=ejemplo encoded-values=valores-codificados 01JHFZWK3GM9XRS2GC4SNXFVD7=valores-codificados sample-postbacks=postbacks-de-muestra 01JHFZWK3GJSA8RF4AMKVM4XD4=postbacks-de-muestra general-install-postback-examples=ejemplos-de-postbacks-de-instalaci%C3%B3n-generales 01JHFZWK3HD1NFJJW1Y8HGVPX2=ejemplos-de-postbacks-de-instalaci%C3%B3n-generales general-inapp-event-postback-examples=ejemplos-de-postbacks-de-eventos-in-app-generales 01JHFZWK3JW0D1GZ739FV0EZWG=ejemplos-de-postbacks-de-eventos-in-app-generales inapp-event-postback-example=ejemplo-de-postbacks-de-eventos-in-app 01JHFZWK3JT8GM7BEM3RXCMXV5=ejemplo-de-postbacks-de-eventos-in-app" />
