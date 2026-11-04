---
title: Macros de postback para Partners de analítica
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
  created_at: '2021-01-04T04:44:40Z'
  edited_at: '2026-08-22T00:37:15Z'
  id: 360016751637
  locale: es
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/es/articles/360016751637
---
> **At a glance:** Usa macros como parte de los postbacks enviados a partners de analítica para obtener datos de atribución relevantes.

<div id="postbacks-for-analytics-partners" />

## Postbacks para Partners de analítica

Los Partners de analítica pueden definir el contenido y los endpoints de los postbacks que se les envían como parte de su integración con AppsFlyer. Los postbacks se relacionan con el engagement del usuario de la aplicación, como instalaciones, eventos in-app, re-engagements, etc.

* **Configuración de postback:** Para solicitar cambios en la configuración de postback, usa el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para Partners</Anchor> para abrir un ticket o contacta con tu gerente de desarrollo de Partners de AppsFlyer.
* **Tipos de postback**: Hay postbacks disponibles para instalación y eventos in-app.

<div id="postback-macros" />

## Macros de postbacks

Cuando se incluyen en un postback, las macros se sustituyen por datos relevantes para el usuario. Por ejemplo, para obtener la dirección IP del usuario que instala la aplicación, incluye country\_code=(ip) en la estructura del postback. Las macros admitidas se enumeran en la siguiente tabla:

* Fuente: De dónde proceden los datos:
  * SDK: El SDK de AppsFlyer incorporado en la aplicación o la API de servidor a servidor
  * AF: Tras el procesamiento por parte de AppsFlyer.
* **[Base]** **Macros para todos los postbacks**: Macros relevantes para la instalación y el evento in-app.
* **[Opcional]** para eventos in-app, como se indica en la columna.

<div id="macrosinstalls-and-in-app-events" />

#### Macros: instalaciones y eventos in-app

| Macro de postback (nombre) | Fuente | Nota | [Base] Macros para todos los postbacks | [Opcional] Eventos in-app |
| --- | --- | --- | --- | --- |
| advertising\_id | SDK | ID del dispositivo que puede ser restablecido por el usuario, también conocido como GAID. También disponible como: (sha1-advertiserId) | Sí |  |
| nombre\_del\_evento | SDK | Nombre asignado a un evento |  | Sí |
| event\_revenue\_USD | AF | Valor del evento en USD |  | Sí |
| ingresos\_evento | SDK | Valor de evento reportado por SDK usando event\_revenue\_currency o la divisa que has seleccionado. |  | Sí |
| moneda\_ingresos\_evento | SDK | El código de divisa de los ingresos del evento reportado en el evento o la divisa que has seleccionado. |  | Sí |
| event\_time | SDK | gp\_referrer (Google Play Referrer string) |  | Sí |
| event\_value | SDK | El evento in-app incluye atributos con valores, que se pueden enviar por completo en el postback en formato JSON. URL codificada mediante la macro (encode). |  | Sí |
| partner\_event\_id | AF | Nombre/ID del evento correspondiente en la plataforma del partner |  | Sí |
| nombre\_aplicación | SDK | Nombre de la aplicación configurado por el anunciante | Sí |  |
| appsflyer\_id | SDK | Identificador único de AppsFlyer, registrado en la conversión | Sí |  |
| tipo\_táctil\_atribuido | AF | Indicador que marca si la atribución se produjo debido a una impresión (1 = impresión, 0 = clic) | Sí |  |
| código\_de\_país | AF | Código de país con ISO 3166 (alfa-2) Ejemplo: US, CN. | Sí |  |
| idfa | SDK | ID de publicidad que el usuario puede restablecer y que se encuentra en dispositivos iOS. También disponible como: (sha1-idfa) | Sí |  |
| idfv | SDK | Identificador único por usuario y por proveedor en los dispositivos iOS | Sí |  |
| hora\_de\_instalación | SDK | Marca de tiempo de instalación | Sí |  |
| install\_unix\_ts | SDK | Marca de tiempo de instalación en formato unix | Sí |  |
| es\_lat | SDK | Limit ad tracking (LAT): iOS: Desde iOS 14, Apple retiró LAT. Determina el estado de privacidad del usuario usando ATT. En este caso, ignora is\_lat. Antes de iOS 14, si es verdadero, el IDFA no está disponible y se establece en 0. Android: Cuando es verdadero, el usuario ha optado por no participar en anuncios basados en intereses. Esto no impide que se recopile el ID de publicidad de Google (GAID). | Sí |  |
| Indicador de atribución AF | SDK | Idioma (configuración regional) reportado por el dispositivo y establecido por el sistema operativo del dispositivo. | Sí |  |
| id\_aplicación | SDK | Identificador único de aplicación en Appsflyer. | Sí |  |
| app-version-name | SDK | Versión de la aplicación establecida por el desarrollador de la aplicación en el código de la aplicación | Sí |  |
| tiempo\_de\_toque\_atribuido | AF | Hora del toque al que AppsFlyer atribuyó | Sí |  |
| tipo\_de\_dispositivo | SDK | Nombre del modelo comercial del dispositivo. Ejemplo: SM-GM284 o iPhone7 | Sí |  |
| ip | AF | IP del dispositivo del usuario que reporta el evento | Sí |  |
| match\_type | AF | Tipo de método de atribución. Por ejemplo, srn, id\_matching, probabilistic | Sí |  |
| versión\_sistema\_operativo | SDK | Versión del sistema operativo del dispositivo | Sí |  |
| agente\_usuario | SDK | El agente de usuario de la URL | Sí |  |
| wifi | SDK | Si es true, la conexión era wifi en el momento de la conversión | Sí |  |
| oaid | SDK | ID que el usuario puede restablecer en algunos dispositivos Android, generalmente como alternativa a GAID | Sí |  |
| Identificador de origen | SDK | Plataforma del dispositivo: iOS, Android o Windows Mobile | Sí |  |
| tipo\_conversion\_retargeting | SDK | Un indicador que marca si se trata de una reatribución o un re-engagement | Sí |  |
| PID | AF | Ad network a la que se atribuye la instalación o el evento in-app | Sí |  |
| af\_anuncio | Atribución | Nombre del anuncio (<Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">ver más</Anchor>) proporcionado por el anunciante/publisher | Sí | Sí |
| id\_del\_anuncio\_af | Atribución | Proporcionado por el anunciante/publisher | Sí | Sí |
| af\_conjunto de anuncios | Atribución | <ul><li>Proporcionado por el anunciante/publisher.</li><li>El conjunto de anuncios representa un nivel intermedio en la jerarquía entre campaña y anuncio. <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">Ver más</Anchor></li></ul> | Sí | Sí |
| af\_adset\_id | Atribución | Proporcionado por el anunciante/publisher | Sí | Sí |
| C | Atribución | Proporcionado por el anunciante/publisher. Los nombres de campaña que superan los 100 caracteres de longitud se muestran en el dashboard como “c\_name\_exceeded\_max\_length” | Sí | Sí |
| af\_c\_id | Atribución | Proporcionado por el anunciante/publisher | Sí | Sí |
| af\_siteid | Atribución | <ul><li>ID único que identifica al publisher que muestra el anuncio. <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#site-id-parameter">Saber más</Anchor></li></ul> | Sí | Sí |
| af\_subsite\_id | Atribución | <ul><li>ID de subred publicitaria/ID del publisher.</li><li>Si, además del editor principal (ID del sitio), hay un subeditor o deseas incluir información adicional, como tipo de anuncio/ubicación dentro de la aplicación, como banner, intersticial, vídeo, etc., utiliza af\_sub\_siteid. Por ejemplo: af\_sub\_siteid =ABCD\_4567</li></ul> | Sí | Sí |
| af\_ad\_type | Atribución | Usa la siguiente convención de nomenclatura:<ul><li>**text:** una unidad de anuncio que contiene solo texto, por ejemplo, un resultado de búsqueda</li><li>**banner:** un formato básico que aparece en la parte superior o inferior de la pantalla del dispositivo</li><li>**interstitial:** un anuncio de página completa que aparece durante las pausas de la experiencia actual</li><li>**video:** un video estándar, es decir, no recompensado</li><li>**rewarded\_video:** una unidad de anuncio que ofrece recompensas in-app a cambio de ver un video</li><li>**playable:** una unidad de anuncio que contiene una vista previa interactiva de la experiencia de la aplicación</li><li>**sponsored\_content:** un enlace incluido en una pieza de contenido patrocinado, como un artículo publicitario</li><li>**audio:** un anuncio de audio</li></ul> | Sí | Sí |

<div id="in-app-event-only-macros" />

## Macros solo para eventos in-app

Los ejemplos a continuación se relacionan con los postbacks de eventos in-app disponibles para los partners.

> 📘 **Note**
>
> **Ejemplo**
>
> La plantilla de postback de evento `&event=(event)&json=(encode)` se tradujo al siguiente postback para un evento af\_purchase específico:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> El valor JSON decodificado de este postback es `{"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

<div id="encoded-values" />

### Valores codificados

Es posible que los postbacks incluyan caracteres irregulares no alfanuméricos. Para transferir estos valores correctamente a través de postbacks, AppsFlyer codifica en URL los valores no alfanuméricos.  
Para decodificar o codificar un postback, usa [un servicio web de codificación](https://www.urldecoder.org/).

<div id="sample-postbacks" />

## Postbacks de muestra

<div id="general-install-postback-examples" />

### Ejemplos de postbacks de instalación generales

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?pid=(media_source)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)
```

</Tab>

<Tab title="apps de iOS,">

```http
http://YourCompanyDomain.com?pid=(media source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)
```

</Tab>
</Tabs>

<div id="general-in-app-event-postback-examples" />

### Ejemplos de postbacks de eventos in-app generales

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>

<Tab title="apps de iOS,">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>
</Tabs>

<div id="in-app-event-postback-example" />

## Ejemplo de postbacks de eventos in-app

**Parámetros de evento:**

* Nombre del evento: af\_revenue
* Ingresos por evento: 120.00
* Moneda del evento: USD
* Valor del evento: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

**Postback:**

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&android_id=9aaeecc4455xxxxx&install_time=1451923560&event_name=af_purchase&currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-analytics-partners=postbacks-para-partners-de-anal%C3%ADtica 01JH2HWTN05T8S3P4W6CKVA7K4=postbacks-para-partners-de-anal%C3%ADtica postback-macros=macros-de-postbacks 01JH2HWTN52E8CVVGTQWK3QXW6=macros-de-postbacks macros%E2%80%94installs-and-inapp-events=macros-instalaciones-y-eventos-in-app 01JH2HWTN7XY6B55TED4NT2KRR=macros-instalaciones-y-eventos-in-app inapp-event-only-macros=macros-solo-para-eventos-in-app 01JH2HWTVN8880HZSF6V6XZ7EF=macros-solo-para-eventos-in-app encoded-values=valores-codificados 01JH2HWTVNARNYV0M9AKHQ0NDA=valores-codificados sample-postbacks=postbacks-de-muestra 01JH2HWTVNQT0NPJ7SG9424MTQ=postbacks-de-muestra general-install-postback-examples=ejemplos-de-postbacks-de-instalaci%C3%B3n-generales 01JH2HWTVN4DDQ6F70WP3XE19D=ejemplos-de-postbacks-de-instalaci%C3%B3n-generales general-inapp-event-postback-examples=ejemplos-de-postbacks-de-eventos-in-app-generales 01JH2HWTVN2MH2SB6W34DH2MF7=ejemplos-de-postbacks-de-eventos-in-app-generales inapp-event-postback-example=ejemplo-de-postbacks-de-eventos-in-app 01JH2HWTVP50J5WV11DZR3RSTM=ejemplo-de-postbacks-de-eventos-in-app" />
