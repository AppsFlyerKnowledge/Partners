---
title: Guía de integración de SKAN para redes de publicidad
metadata:
  keywords:
    - Ad Networks
    - Partners
    - SKAD
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2020-08-03T08:56:14Z'
  edited_at: '2026-08-12T12:28:12Z'
  id: 360011502657
  locale: es
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/es/articles/360011502657
---
> **De un vistazo**: Las redes de publicidad se integran con AppsFlyer SKAdNetworks (SKAN), lo que les permite optimizar campañas y atribuirse el tráfico que generan.

## Oferta de AppsFlyer para redes de publicidad

**Aprender más sobre la solución SKAN de AppsFlyer para anunciantes:**

<Anchor target="_blank" href="/marketers/es/docs/skadnetwork-skan-solution-guide">Guía de soluciones SKAN |</Anchor> <Anchor target="_blank" href="/marketers/es/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">Panel de control de SKAN</Anchor>

* **Atribución de conversiones de la campaña:**
  * La integración con AppsFlyer garantiza la atribución a la red de publicidad de todas las instalaciones, los eventos in-app y los ingresos resultantes de las campañas ejecutadas en nombre de los anunciantes.
  * Sin la integración, las instalaciones, los eventos in-app y los ingresos se atribuyen como orgánicos y no a la red de publicidad.
* **Optimización de campañas:**
  * El valor de conversión en el postback está codificado.
  * AppsFlyer permite que las redes de publicidad traduzcan el valor de conversión de cada postback, lo que garantiza que las mismas puedan optimizar sus campañas en función del valor decodificado por aplicación.
* **Sin necesidad de integración directa con cada anunciante:** los postbacks de SKAN se envían solo a la red de publicidad y los anunciantes pueden consumir los datos utilizando cualquiera de estas opciones:
  * Integración individual con cada red de publicidad. Una solución que no es escalable, ni para las redes de publicidad ni para los anunciantes.
  * Una sola integración con AppsFlyer. Escalable tanto para el anunciante como para la red de publicidad.
* **Aumenta tu protagonismo en AppsFlyer:**
  * Las redes de publicidad con integración de SKAN están certificadas e identificadas como tales en el panel de control de AppsFlyer.
  * Esto asegura a los anunciantes que están trabajando con redes de publicidad que pueden medirse de forma determinista a través de este modelo de atribución.

## Flujo de datos de SKAN

![5754_Postback_flow_for_SKAD__1_.png](https://files.readme.io/dff0fb00721802f59d199ae6a69f9ea7484bc0ef038c669904aa1a7c2b97dfc8-12574373654161.png)

El flujo de postback completo de SKAN es el siguiente:

1. **iOS** envía el postback de SKAN a la red de publicidad atribuida.
2. La **red de publicidad** realiza una de las siguientes acciones:
   * **Enriquecer y reenviar:** enriquece el postback de SKAN con el ID de campaña/identificador de fuente de la red de publicidad, el nombre de la campaña y la dirección IP del dispositivo iOS.
   * **Redirigir:** la red solicita al dispositivo iOS que redirija el postback y los datos de campaña que añade de vuelta a AppsFlyer.
3. **Redirigir:** la red solicita al dispositivo iOS que redirija el postback directamente a AppsFlyer. En este caso, el enriquecimiento de los datos de la campaña se realizará a través de una API separada entre AppsFlyer y la red de publicidad.

## Partes principales de la integración

La integración de SKAN entre AppsFlyer y las redes de publicidad consta de las siguientes partes principales, descritas en este artículo:

* Las redes de publicidad envían los datos de SKAN a AppsFlyer.
* Las redes de publicidad reciben los datos enriquecidos y decodificados de AppsFlyer a través de postbacks.

## Envío de datos a AppsFlyer

Después de que la red de publicidad reciba el postback de SKAN desde el dispositivo, la red de publicidad lo reenvía a AppsFlyer utilizando uno de los siguientes métodos:

* Enriquecer y reenviar (POST)
* Redirigir (método de redireccionamiento HTTP 307)

Al recibir un postback de SKAN, AppsFlyer realiza lo siguiente:

* Validar el postback: asegurar que sea único.
* Decodificar el valor de conversión: generar registros de atribución de instalaciones/eventos in-app.
* Enviar los postbacks decodificados a la red de publicidad.
* Poner los datos de atribución a disposición de los anunciantes a través de los paneles de control y reportes.

<div id="enrich-and-forward" />

<Accordion title="Enriquecer y reenviar">

Mediante este método, las redes de publicidad reenvían cada postback recibido del dispositivo a AppsFlyer.

**La red de publicidad:**

* Recibe el postback desde el dispositivo iOS.
* [Opcional] Enriquece el postback con:
  * Nombre e ID de la campaña de la red de publicidad.
  * Marca de tiempo del postback, enviada desde el dispositivo iOS.
* [Opcional] Enriquece el postback con:
  * Dirección IP recibida del dispositivo, requerida principalmente para fines de resolución de la geolocalización.
  * ID y nombre del anuncio
  * ID y nombre del conjunto de anuncios
  * Nombre de la red de publicidad
  * Código de país
  * ID de aplicación fuente
  * Creatividad
  * Canal
* Envía el postback a AppsFlyer
* **¡Atención!** Nota: **Antes de enviar el postback a AppsFlyer, valida la <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/verifying_an_install-validation_postback">firma de atribución</Anchor> de Apple usando el contenido del postback saliente, para asegurarte de que no corrompiste involuntariamente los datos.**

#### Protocolo de postback enriquecido de SKAN

| Punto final | `https://skadpostbacks.appsflyer.com/api/postbacks` |
| --- | --- |
| Método HTTP | POST |
| Tipos de contenido aceptado | `application/json` |
| Códigos de respuesta | 200 OK: el postback recibido tiene un formato válido.<br /><br />400: Solicitud incorrecta: JSON mal formado, JSON vacío, faltan campos obligatorios. |

#### Parámetros JSON de postbacks enriquecidos de SKAN

| Parámetro | Formato | Descripción | Fuente |
| --- | --- | --- | --- |
| version | Cadena | Versión de SKAdNetwork<br /><br />Ejemplo: `"version":"2.0"` | Postback de SKAN |
| ad-network-id | Cadena | ID de red de publicidad<br /><br />Ejemplo: `"ad-network-id":" abc123defg.SKAdnetwork"` | Postback de SKAN |
| ad-network-name | Cadena | <ul><li>Nombre de la red de publicidad</li><li>Ejemplo: `ad_network_name=your_network`</li></ul> | Red de publicidad |
| ad-network-country-code | Cadena | <ul><li>La ubicación del usuario (geolocalización) derivada por la red de publicidad.</li><li>Se rellena usando códigos <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alfa-2)</Anchor>.</li><li>Ejemplo: CN, ZA</li><li>Las redes de publicidad suelen derivar la geolocalización de acuerdo con la región objetivo de una campaña determinada.</li><li>AppsFlyer utiliza el código de país para rellenar los campos relativos a la geolocalización en los reportes y paneles de control.</li></ul> | Red de publicidad |
| campaign-id | Entero | <ul><li>Solo para SKAN 3 e inferiores</li><li>ID de campaña de SKAdNetwork</li><li>Ejemplo: `"campaign-id":23`</li></ul> | Postback de SKAN |
| transaction-id | Cadena | ID de transacción de postback de SKAdNetwork | Postback de SKAN |
| app-id | Entero | <ul><li>ID de la aplicación objetivo tal como aparece en AppsFlyer. Siempre tiene el prefijo id.</li><li>Ejemplo: `app_id=id123456789`</li></ul> | Postback de SKAN |
| firma de atribución | Cadena | Firma de atribución | Postback de SKAN |
| redownload | Booleano | Cuando redownload = true, significa que el usuario volvió a descargar la aplicación desde la tienda de aplicaciones. | Postback de SKAN |
| source-app-id | Entero | <ul><li>ID de la aplicación fuente (publisher)</li><li>Para SKAN 4, disponible solo en el primer postback, para el nivel 3. Ver [documentación de Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows).</li></ul> | Postback de SKAN |
| conversion-value | Entero | El SDK de AppsFlyer establece el valor de conversión de acuerdo con la configuración del anunciante.<br /><br />Notas:<ul><li>Debido a los umbrales de preservación de la privacidad de iOS, iOS puede no rellenar el parámetro en el postback y el valor será nulo.</li><li>Nulo y 0 tienen significados diferentes:<ul><li>Nulo: iOS retuvo el valor de conversión</li><li>0: el usuario instaló la aplicación pero no realizó ninguna acción medida.</li></ul></li></ul> | Postback de SKAN |
| ad-network-campaign-id | Cadena | Para habilitar un lenguaje común entre las redes de publicidad, los anunciantes y AppsFlyer deben proporcionar tu campaign-id. | Red de publicidad |
| ad-network-campaign-name | Cadena | Nombre de la campaña de la red de publicidad asociado con el ID de campaña de la red de publicidad. Este nombre se muestra en los paneles de control y reportes. | Red de publicidad |
| ad-network-adset-id | Cadena | ID del conjunto de anuncios de la red de publicidad | Red de publicidad |
| ad-network-adset-name | Cadena | Nombre del conjunto de anuncios de la red de publicidad | Red de publicidad |
| ad-network-ad-name | Cadena | Nombre del anuncio de la red de publicidad | Red de publicidad |
| ad-network-ad-id | Cadena | ID de anuncio de la red de publicidad | Red de publicidad |
| ip | Cadena | <ul><li>La dirección IP del dispositivo que envía el postback.</li><li>Se admiten direcciones IPv4 e IPv6.</li><li>Ejemplo: `"ip":"198.51.100.1"`</li></ul> | Red de publicidad |
| timestamp | Cadena | <ul><li>Hora en que la red de publicidad recibió el postback de SKAN. Una marca de tiempo UNIX epoch de 10 dígitos. [Opcional] Se permite una marca de tiempo epoch de 13 dígitos.</li><li>Ejemplo: 4 de agosto de 2020, 07:25 UTC se traduce como `"timestamp": "1596525944"`</li></ul> | Red de publicidad |
| fidelity-type | Entero | <ul><li>Permite diferenciar entre las opciones de <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/receiving_ad_attributions">presentación de anuncios</Anchor> que afectan a la atribución. Se indica con los valores 0 y 1 de la siguiente manera:<ul><li>Anuncios por impresiones (0)</li><li>Anuncios renderizados por Storekit (1)</li></ul></li><li>Campo obligatorio a partir de SKAN V2.2</li></ul> | Postback de SKAN (V2.2+) |
| did-win | Booleano | <ul><li>Se utiliza para distinguir entre las campañas [que contribuyen o se atribuyen](https://developer.apple.com/documentation/storekit/SKAdnetwork/SKAdnetwork_release_notes/SKAdnetwork_version_3_0_release_notes) con la instalación.</li><li>Si es true, se atribuye a la campaña por traer la instalación.</li><li>Si es false, se reconoce que la campaña contribuye a la instalación.</li></ul> | Postback de SKAN (V3.0+) |
| ad-network-source-app-id | Cadena | Rellénalo con el *ID de publisher* que asocies con la aplicación que publica el anuncio. Este suele ser el ID que asignaste al publisher, y no el ID generado por Apple. | Red de publicidad |
| postback-sequence-index | Entero | <ul><li>Solo para SKAN 4+.</li><li>El valor representa el número de secuencia (ventana de SKAN), ya sea `0`, `1` o `2`.</li></ul> | Postback de SKAN 4.0 (iOS 16.2) |
| coarse-conversion-value | Cadena | <ul><li>Solo para SKAN 4+.</li><li>El valor puede ser `low`, `medium` o `high`.</li><li>Para el primer postback, solo disponible para el nivel 1. Para el segundo y tercer postbacks, disponible para los niveles 1-3. Ver [documentación de Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows).</li></ul> | Postback de SKAN 4.0 (iOS 16.2) |
| source-identifier | Cadena | <ul><li>Solo para SKAN 4+.</li><li>Reemplaza a `campaign-id`.</li><li>El valor puede ser de hasta 4 dígitos.</li><li>Para el primer postback, hay disponibles hasta 4 dígitos para los niveles 2-3 y 2 dígitos están disponibles para los niveles 0-1. Para el segundo y tercer postbacks, 2 dígitos están disponibles para los niveles 1-3. Para el nivel 0, no hay ningún postback. Ver [documentación de Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows).</li></ul> | Postback de SKAN 4.0 (iOS 16.2) |
| source-domain | Cadena | <ul><li>Solo para SKAN 4+.</li><li>El valor representa la fuente de los anuncios web atribuibles. Ejemplo: `example.com`.</li><li>Disponible solo en anuncios web, en el primer postback, para el nivel 3. Ver [documentación de Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows).</li></ul> | Postback de SKAN 4.0 (iOS 16.2) |
| Creatividad | Cadena | <ul><li>Solo relevante para SKAN 4+.</li><li>Disponible cuando usas dígitos adicionales en el source\_identifier para obtener granularidad adicional de la campaña.</li></ul> | Red de publicidad |
| canal | Cadena | <ul><li>Solo relevante para SKAN 4+.</li><li>Disponible cuando usas dígitos adicionales en el source\_identifier para obtener granularidad adicional de la campaña.</li></ul> | Red de publicidad |

#### **Ejemplo de curl: postback de SKAN 3 enriquecido**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version":"3.0",
      "app-id": 888707086,
      "ip": "192.0.2.0",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "source-app-id": 888707074,
      "ad-network-id": "abcabcabc.skadnetwork",
      "transaction-id": "68eb3d91-15f5-44ee-9267-25c7655c20b6",
      "redownload": false,
      "attribution-signature": "MDYCGQCsQ4y8d4BlYU9b8Qb9BPWPi+ixk/OiRysCGQDZZ8fpJnuqs9my8iSQVbJO/oU1AXUROYU=",
      "timestamp": "1596525944",
      "ad-network-campaign-id": "222222",
      "conversion-value": 63,
      "campaign-id": 99
  }'
```

#### **Ejemplo de curl: postback de SKAN 4 enriquecido con valores de conversión precisos**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "5239",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e30",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "conversion-value": 63
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIGRmSMrqedNu6uaHyhVcifs118R5z/AB6cvRaKrRRHWRAiEAv96ne3dKQ5kJpbsfk4eYiePmrZUU6sQmo+7zfP/1Bxo="
  }'
```

#### Ejemplo de curl: postback de SKAN 4 enriquecido con valores de conversión aproximados****

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "39",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e31",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "coarse-conversion-value": "high"
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIQD4rX6eh38qEhuUKHdap345UbmlzA7KEZ1bhWZuYM8MJwIgMnyiiZe6heabDkGwOaKBYrUXQhKtF3P/ERHqkR/XpuA="
  }'
```

</Accordion>

<div id="redirect" />

<Accordion title="Redirigir">

![Redirect_us-en__2_.png](https://files.readme.io/17d4a668cde784a2f823e702e04fc75a2bbbdb483e44d9d10edfad03d865bbb7-360012352758.png)

Mediante este método, la red de publicidad responde al dispositivo con un comando de redireccionamiento HTTP (307), solicitando al dispositivo que envíe el postback directamente a AppsFlyer.

El método de redireccionamiento tiene las siguientes ventajas:

* **Mayor confianza del anunciante:** el MMP actúa en nombre de un anunciante. Al proporcionar acceso a AppsFlyer al postback de primera mano, los anunciantes confían en que los postbacks no se manipulan en tránsito.
* **No requiere procesamiento por parte de la red de publicidad:** las redes de publicidad responden con el comando de redireccionamiento (al dispositivo), eliminando así la necesidad de procesar postbacks. En comparación, el método de enriquecer y reenviar requiere que las redes de publicidad consuman el postback, lo enriquezcan con parámetros adicionales y finalmente lo reenvíen a AppsFlyer.

#### **Implementación**

1. Configura tu servidor para que responda con una respuesta HTTP 307 que redirija el postback a *[https://skadredirect.appsflyer.com/api/redirects](https://skadredirect.appsflyer.com/api/redirects)*
2. Anexa los parámetros de consulta que contengan los detalles de la campaña, utilizando los parámetros de consulta enumerados en la tabla que sigue. Considera como obligatorio el envío de los datos de tu campaña. Los detalles de la campaña nos permiten enriquecer los datos de SKAN con datos de costos y otros datos de campaña y permiten que los anunciantes optimicen las campañas de manera efectiva.

**Ejemplo de URL de redireccionamiento**

```http
https://skadredirect.appsflyer.com/api/redirects?
  https://skadredirect.appsflyer.com/api/redirects?
  &ad-network-campaign-id=243232&ad-network-campaign-name=yarg_campaign_name
  &ad-network-adset-name=dsdsa&creative=examplecreative&channel=channelexample
```

#### Parámetros de consulta para los detalles de la campaña (no obligatorio)

| Parámetro de consulta | Descripción |
| --- | --- |
| ad-network-name | <ul><li>Nombre de la red de publicidad</li><li>Ejemplo:`ad_network_name=your_network`</li></ul> |
| ad-network-campaign-id | ID de campaña |
| ad-network-campaign-name | Nombre de la campaña |
| ad-network-adset-id | ID de conjunto de anuncios |
| ad-network-adset-name | Nombre de conjunto de anuncios |
| ad-network-ad-id | ID de anuncio |
| ad-network-ad-name | Nombre de anuncio |
| ad-network-country-code | <ul><li>La ubicación del usuario (geolocalización) derivada por la red de publicidad.</li><li>Se rellena usando códigos <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alfa-2)</Anchor>.</li><li>Ejemplo: CN, ZA</li><li>Las redes de publicidad suelen derivar la geolocalización de acuerdo con la región objetivo de una campaña determinada.</li><li>AppsFlyer utiliza el código de país para rellenar los campos relativos a la geolocalización en los reportes y paneles de control.</li></ul> |
| ad-network-source-app-id | Rellénalo con el *ID de publisher* que asocies con la aplicación que publica el anuncio. Este suele ser el ID que asignaste al publisher, y no el ID generado por Apple. |
| ip | <ul><li>La dirección IP del dispositivo que envía el postback.</li><li>Se admiten direcciones IPv4 e IPv6.</li><li>Ejemplo:`"ip":"198.51.100.1"`</li></ul> |
| timestamp | <ul><li>Hora en que la red de publicidad recibió el postback de SKAN. Una marca de tiempo UNIX epoch de 10 dígitos. [Opcional] Se permite una marca de tiempo epoch de 13 dígitos.</li><li>Ejemplo: 4 de agosto de 2020, 07:25 UTC se traduce como `"timestamp": "1596525944"`</li></ul> |
| Creatividad | <ul><li>Solo relevante para SKAN 4+.</li><li>Disponible cuando usas dígitos adicionales en el source\_identifier para obtener granularidad adicional de la campaña.</li></ul> |
| canal | <ul><li>Solo relevante para SKAN 4+.</li><li>Disponible cuando usas dígitos adicionales en el source\_identifier para obtener granularidad adicional de la campaña.</li></ul> |

</Accordion>

## Recibir datos de AppsFlyer

Antes de recibir tu primer postback, toma en consideración lo siguiente:

* Las redes de publicidad deben definir el punto de conexión del postback y la plantilla (comunícate con tu gerente de desarrollo de partners de AppsFlyer usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>, para asegurarse de que esto se esté cumpliendo).
* AppsFlyer envía los postbacks de SKAN utilizando el mismo mecanismo que con los postbacks existentes que se te envían.

<div id="principles" />

<Accordion title="Principios">

* Por cada postback enviado desde la red de publicidad a AppsFlyer, AppsFlyer envía:
  * Un postback de instalación. Las redescargas se señalan mediante el parámetro redownload.
  * De cero a varios postbacks de eventos in-app. El número exacto depende de la traducción del valor de conversión. Ver [postbacks simulados.](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks)
* Cuando consumes postbacks, la misma instalación o evento puede atribuirse mediante más de una solución de atribución de AppsFlyer. Utiliza el parámetro *atribution\_source* para diferenciar entre los tipos de postback.

</Accordion>

<div id="postback-macros-available-to-ad-network-partners" />

<Accordion title="Macros de postback disponibles para los partners de redes de publicidad">

<table><thead><tr><th>Macro de postback (nombre)</th><th>Descripción</th><th>Formato y ejemplo</th><th>Relevante solo para eventos in-app</th></tr></thead><tbody><tr><td>id_sitio</td><td>La aplicación que publica el anuncio (ID de aplicación fuente)</td><td>Cadena: 876534</td><td> </td></tr><tr><td>hora_de_instalación</td><td>Estimado por AppsFlyer en base a la ventana de <em>updateConversion</em>. Se proporciona como una marca de tiempo UNIX epoch de 10 dígitos o como una marca de tiempo legible por humanos.</td><td><ul><li>Cadena: 1596119460 </li><li>Se traduce como 30 de julio de 2020, 14:31 UTC.</li></ul></td><td> </td></tr><tr><td>skadnetwork_ad_network_time</td><td>Hora en que la red de publicidad recibió el postback desde el dispositivo iOS. Reportada por la red de publicidad. Se proporciona como una marca de tiempo UNIX epoch de 10 dígitos o como una marca de tiempo legible por humanos.</td><td><ul><li>Cadena: 1596119460 </li><li>Se traduce como 30 de julio de 2020, 14:31 UTC.</li></ul></td><td> </td></tr><tr><td> <br/>skadnetwork_received_time</td><td>Hora en que AppsFlyer recibió el postback de la red de publicidad. Se proporciona como una marca de tiempo UNIX epoch de 10 dígitos o como una marca de tiempo legible por humanos.</td><td><ul><li>Cadena: 1596119460 </li><li>Se traduce como 30 de julio de 2020, 14:31 UTC.</li></ul></td><td> </td></tr><tr><td>nombre_del_evento</td><td><p>Nombre del evento </p><ul><li>af_skadnetwork_revenue</li><li>af_login</li><li>af_skadnetwork_revenue</li><li>o según lo establecido por el anunciante </li></ul></td><td><p>Cadena: af_skadnetwork_revenue, abc123</p></td><td>Sí</td></tr><tr><td>ingresos</td><td>Monto de ingresos utilizando el código de divisa especificado.</td><td>Número: 5, 20, 0.4</td><td>Sí</td></tr><tr><td>moneda</td><td>El código de divisa es la divisa específica de la aplicación establecida por el anunciante.</td><td>Cadena: EUR, USD, ZAR</td><td>Sí</td></tr><tr><td>attribution_source</td><td><p>La fuente de los datos de atribución:</p><p>SKAdNetwork: SKAdNetwork</p></td><td>Cadena: SKAdNetwork</td><td> </td></tr><tr><td>id_aplicación</td><td>ID de aplicación (aplicación del anunciante)</td><td>Cadena: ID123456790</td><td> </td></tr><tr><td>País</td><td>Geolocalización (país) de instalación determinada por la red de publicidad.</td><td>Cadena: US, UK, ZA </td><td> </td></tr><tr><td>campaña</td><td>Nombre de la campaña rellenado mediante un <em>d-network-campaign-name</em> en el postback desde la red de publicidad.</td><td>Cadena: UA_US_23+</td><td> </td></tr><tr><td>id_campaña</td><td>ID de campaña de la red de publicidad rellenado mediante un <em>ad network-campaign-id</em> enviado en el postback desde la red de publicidad. <strong>Nota</strong>: Para SKAN 4, este valor siempre es nulo.</td><td>Cadena: 3456745</td><td> </td></tr><tr><td>redownload</td><td><p>Valores posibles: true, false</p><p>Cuando redownload = true, significa que el usuario volvió a descargar la aplicación desde la tienda de aplicaciones.</p></td><td>Booleano: true, false</td><td> </td></tr><tr><td><p>skadnetwork_ambiguous_event</p><p><strong>Ocurrencias del evento</strong>: el número de ocurrencias del evento se calcula usando la siguiente fórmula:<br/><code>[round up (SKAN_min_event_counter+SKAN_max_event_counter) / 2]</code><br/>Nota: El valor debe redondearse al entero más cercano.</p></td><td><p>Eventos recibidos durante las primeras 72 horas después de que un anunciante cambie la configuración de SKAN en el panel de control. Debido a los distintos temporizadores usados por SKAN, AppsFlyer no puede asignar el evento con precisión.</p><ul><li>No disponible en SKAN 4 y posteriores</li></ul></td><td>Booleano: true, false</td><td> </td></tr><tr><td>skadnetwork_campaign_id</td><td>ID de campaña de SKAN proporcionado por el postback original de SKAN.</td><td>56, 23</td><td> </td></tr><tr><td>af_skadnetwork_nonce</td><td>Un identificador aleatorio exclusivo que permite a los partners identificar los postbacks duplicados.</td><td> </td><td> </td></tr><tr><td>Ingresos asociados al SKU en la moneda indicada en el campo <code>event_revenue_currency</code>.</td><td>Nombre/ID del<span> </span><span>evento</span>correspondiente<span> </span>en la plataforma de la red de publicidad.</td><td> </td><td>Sí</td></tr><tr><td>transaction_id</td><td><p>ID de transacción del postback de SKAN.</p><p><strong>Nota</strong>: El anunciante debe permitirnos explícitamente compartir el transaction_id contigo. Pide al anunciante que lo haga en la pestaña <a href="/marketers/es/docs/set-up-an-integrated-partner#integration-tab" target="_blank"><strong>Integración</strong></a>.</p></td><td> </td><td> </td></tr><tr><td>ad_network_adset_id</td><td>Agregado al postback de iOS por la red de publicidad.</td><td>Cadena</td><td> </td></tr><tr><td>ad_network_adset_name</td><td>Agregado al postback de iOS por la red de publicidad.</td><td>Cadena</td><td> </td></tr><tr><td>ad_network_ad_name</td><td>Agregado al postback de iOS por la red de publicidad.</td><td>Cadena</td><td> </td></tr><tr><td>ad_network_ad_id</td><td>Agregado al postback de iOS por la red de publicidad.</td><td>Cadena</td><td> </td></tr><tr><td>SKAN_min_event_counter</td><td>Ver nota (1)</td><td>Entero</td><td>Sí</td></tr><tr><td>SKAN_max_event_counter</td><td>Ver nota (1)</td><td>Entero</td><td>Sí</td></tr><tr><td>SKAN_min_time_post-install</td><td>Ver nota (2)</td><td>Entero</td><td>Sí</td></tr><tr><td>SKAN_max_time_post-install</td><td>Ver nota (2)</td><td>Entero</td><td>Sí</td></tr><tr><td>SKAN_min_event_revenue</td><td>Ver nota (3)</td><td>Número real</td><td>Sí</td></tr><tr><td>SKAN_max_event_revenue</td><td>Ver nota (3)</td><td>Número real </td><td>Sí</td></tr><tr><td>fidelity-type</td><td><p>Permite diferenciar entre las opciones de <a href="https://developer.apple.com/documentation/storekit/SKAdnetwork/receiving_ad_attributions" target="_blank">presentación de anuncios</a> que afectan a la atribución. Se indica con los valores 0 y 1 de la siguiente manera: </p><ul><li>Anuncios por impresiones (0)</li><li>Anuncios renderizados por Storekit (1)</li></ul></td><td>Entero</td><td> </td></tr><tr><td>skad_af_attribution_flag</td><td>Se utiliza para indicar si el usuario fue atribuido por AppsFlyer usando el <a href="/marketers/es/docs/single-source-of-truth-ssot-guide-for-ios-attribution#campo-del-indicador-de-atribución" target="_blank">mecanismo de Única fuente de verdad</a>. </td><td>Booleano</td><td> </td></tr><tr><td>skad_postback_sequence_index</td><td><ul><li>Este valor representa la ventana de SKAN, ya sea<code>0</code>,<code>1</code> o <code>2</code>.</li><li>Para SKAN 3, el valor es <code>0</code>. </li></ul></td><td>Entero</td><td> </td></tr><tr><td>skad_coarse_conversion_value</td><td><ul><li>El valor puede ser <code>low</code>, <code>medium</code> o <code>high</code>.</li><li>Para SKAN 3, el valor es <code>null</code>.</li></ul></td><td>Cadena</td><td> </td></tr><tr><td>skad_source_identifier</td><td><ul><li>El valor puede ser de hasta 4 dígitos.</li><li>Para SKAN 3, el valor es <code>null</code>. </li></ul></td><td>Cadena</td><td> </td></tr><tr><td>skad_source_domain</td><td><ul><li>El valor representa la fuente de los anuncios web atribuibles.</li><li>Para SKAN 3, el valor es <code>null</code>.</li></ul></td><td>Cadena</td><td> </td></tr><tr><td>ad_network_creative</td><td><ul><li>El valor se basa en el enriquecimiento de los datos recibidos de la red de publicidad.</li><li>Para SKAN 3, el valor es <code>null</code>.</li></ul></td><td>Cadena</td><td> </td></tr><tr><td>ad_network_channel</td><td><ul><li>Solo relevante para SKAN 4+.</li><li>Disponible cuando usas dígitos adicionales en el <span>source_identifier</span> para obtener granularidad adicional de la campaña.</li></ul></td><td>Cadena</td><td> </td></tr><tr><td colspan="4"><p>Notas:</p><ol><li> <strong>Ocurrencias del evento</strong>: el número de ocurrencias del evento se calcula usando la siguiente fórmula:<br/><code>[round up (SKAN_min_event_counter+SKAN_max_event_counter) / 2]</code><br/>¡Atención! El valor debe redondearse al entero más cercano.</li></ol><ul><li>Ejemplo:<ul><li>A. Si min=0 y max=1, el número de eventos es 1.</li><li>B. Si min=0 y max=10, el número de eventos es 5.</li></ul></li><li> <strong>Determinar la hora de instalación</strong>: para los anunciantes que implementan la conversión personalizada, AppsFlyer calcula la hora de instalación como la hora de llegada del postback - 48 h - promedio (min_time_post_install + max_time_post_install). Las redes de publicidad no necesitan hacer uso de estas macros.  </li><li> <strong>Determinar ingresos</strong>: AppsFlyer utiliza estos valores para determinar los ingresos de un evento calculando el promedio de min y max. Las redes de publicidad no necesitan hacer uso de estas macros. </li></ul></td></tr></tbody></table>

</Accordion>

<div id="skan-postback-examples" />

<Accordion title="Ejemplos de postbacks de SKAN">

**Ejemplo de postback de instalación de SKAN enviado por AppsFlyer**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)
  &attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

**Ejemplo de postback de in-app de SKAN enviado por AppsFlyer**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)&revenue=(value)
  &currency=(code)&event_name=(event-name)&attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

</Accordion>

## Pruebas de integración

Para validar la integración con AppsFlyer, utiliza uno de los siguientes métodos o ambos.

* Postbacks reales de SKAN: basados en el tráfico de SKAN real recibido por la red
* Postbacks simulados: basados en aplicaciones de prueba AppsFlyer

**Para recibir los postbacks reales de SKAN desde dispositivos iOS, la red de publicidad realiza lo siguiente:**

* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/registering_an_ad_network">Registrarse con Apple.</Anchor>
* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/generating_the_signature_to_validate_storekit-rendered_ads">Firmar los anuncios con una firma de SKAdNetwork</Anchor>.
* Aplicación del publisher: <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/configuring_a_source_app">agregar el ID de red al archivo info.plist</Anchor> y<Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/generating_the_signature_to_validate_an_installation"> llamar a la función loadProduct</Anchor> tras la impresión del anuncio.
* Aplicación anunciada: usa el <Anchor target="_blank" href="/marketers/es/docs/sdk-integration-overview">SDK de AppsFlyer para iOS más reciente.</Anchor> Las versiones anteriores a V6.0.3 no son compatibles.

**Para recibir los postbacks simulados:**

* Contáctanos usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor> y solicita la integración con aplicaciones de simulación.
* Especifica los ID de las aplicaciones de la lista en la [siguiente sección](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks).

<div id="real-environment" />

<Accordion title="Entorno real">

Mediante este método, la red de publicidad envía a AppsFlyer los postbacks reales de SKAN desde aplicaciones activas.

#### Probar la integración

| Responsabilidad | Acción |
| --- | --- |
| Red de publicidad | Notificar a AppsFlyer a través de tu gerente de desarrollo de partners (o usa el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>) acerca de tu ID de red de SKAN, proporcionado por Apple. |
| Red de publicidad y AppsFlyer | Acordar un cliente mutuo (habiendo integrado el SDK de AppsFlyer más reciente) para usar para la verificación de la integración de postbacks. |
| Red de publicidad | Enviar postbacks de la aplicación de SKAN a AppsFlyer, utilizando uno de los métodos descritos en este artículo. |
| AppsFlyer | Enviar los postbacks decodificados a la red de publicidad de acuerdo con la asignación de valores de conversión establecida por el anunciante. |

#### Criterios de prueba

| Responsabilidad | Acción |
| --- | --- |
| Red de publicidad | Notificar a AppsFlyer sobre la cantidad de postbacks de SKAN enviados durante un período determinado para el cliente mutuo acordado. |
| AppsFlyer | Verificar el recuento de postbacks recibidos frente al recuento enviado por la red de publicidad. |
| AppsFlyer | Compartir con la red de publicidad el recuento de postbacks enviados a la red para una aplicación determinada, desglosado por tipo:<ul><li>Postbacks de instalación/redescarga</li><li>Postbacks in-app</li></ul>Nota: Si usas el mismo punto de conexión para postbacks probabilísticos, asegúrate de filtrar usando *attribution\_source=skadnetwork* para distinguir los postbacks de SKAN Network de otros postbacks. |

</Accordion>

<div id="simulated-postbacks" />

<Accordion title="Postbacks simulados">

* Mediante este método, la red de publicidad envía postbacks preparados previamente de AppsFlyer a las aplicaciones de prueba de AppsFlyer, como se detalla en la siguiente tabla. AppsFlyer responde con postbacks decodificados a la red de publicidad.
* Cada aplicación de prueba tiene una asignación de valores de conversión diferente, como se detalla en la tabla.

| ID de aplicación | Modo de conversión | Instrucciones |
| --- | --- | --- |
| <span id="id888707085"></span>id888707085 | Ingresos, en unidades de 1 USD<br /><br />Resultados esperados: | <ol><li>En la pestaña **Integración**, habilita los **postbacks de eventos in-app**.</li><li>Selecciona el nombre del evento *af\_SKAN\_revenue* y asígnalo a tu identificador de evento.</li><li>Guarda la configuración.</li><li>En un postback, envía el valor de conversión = 7.</li><li>AppsFlyer responde con:<ul><li>Postback de instalación</li><li>Postback af\_SKAN\_revenue con un valor de 7 USD</li></ul></li></ol> |
| <span id="id888707086"></span>id888707086 | Conversión, incluidos los eventos in-app:<ul><li>af\_level\_complete</li><li>af\_login</li><li>af\_SKAN\_revenue</li><li>af\_register</li><li>af\_subscription</li><li>af\_custom\_event</li></ul> | <ol><li>En la pestaña **Integración**, habilita los **postbacks de eventos in-app**.</li><li>Selecciona cada uno de los eventos in-app enumerados y asígnalos a tu identificador de evento.</li><li>Guarda la configuración.</li><li>En un postback, envía el valor de conversión = 63.</li><li>AppsFlyer responde con:<ul><li>Postback de instalación</li><li>af\_level\_complete postback</li><li>af\_login postback</li><li>Postback af\_SKAN\_revenue</li><li>af\_register postback</li><li>af\_subscription postback</li><li>af\_custom\_event postback</li></ul></li></ol> |
| <span id="id888707087"></span>id888707087 | Engagement, medido usando el evento af\_SKAN\_revenue | <ol><li>En la pestaña **Integración**, habilita los **postbacks de eventos in-app**.</li><li>Asigna el nombre del evento *af\_SKAN\_revenue* y a tu identificador de evento.</li><li>**Guarda** la configuración.</li><li>En un postback, envía el valor de conversión = 3.</li><li>AppsFlyer responde con:<ul><li>Postback de instalación</li><li>3 postbacks del evento af\_SKAN\_revenue</li></ul></li></ol> |

#### Pasos de integración

| Responsabilidad | Acción |
| --- | --- |
| Red de publicidad | Configura el ID de tu red de SKAN (proporcionado por Apple) y la plantilla de postback de SKAN en la <Anchor target="_blank" href="/partners/es/docs/self-serve-integration-management-for-ad-networks">plataforma de administración de postbacks</Anchor>. Para consultas y asistencia, contáctanos utilizando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>. |
| Red de publicidad | <ol><li><Anchor target="_blank" href="/partners/es/docs/turn-on-test-app-integration-for-ad-networks">Activa las aplicaciones de prueba</Anchor>.</li><li>Para cada aplicación, completa la columna de instrucciones en la tabla anterior.</li><li>Envía postbacks simulados usando las aplicaciones de prueba enumeradas en la tabla anterior. Consideraciones al enviar postbacks simulados:<ul><li>Establece el app\_id y el valor de conversión como se indica en la tabla anterior.</li><li>Dado que las redes de publicidad no pueden generar firmas compatibles con Apple, los postbacks simulados no tienen que incluir los campos de firma. AppsFlyer no los verificará para postbacks simulados.</li><li>Las redes de publicidad envían el postback usando el enfoque POST o REDIRECT.</li></ul></li></ol> |
| AppsFlyer | Responde con los postbacks decodificados al punto de conexión designado por la red de publicidad durante la integración. |

#### Criterios de prueba

| Responsabilidad | Acción |
| --- | --- |
| AppsFlyer | Procesa el postback y envía los postbacks a la red de publicidad. |
| Red de publicidad | <ul><li>La red de publicidad recibe y decodifica los postbacks traducidos.</li><li>Los postbacks in-app enviados por AppsFlyer coinciden con los flujos esperados. Por ejemplo, el valor de conversión 3 para la aplicación ID888707087, la red de publicidad recibe 3 postbacks del evento *af\_SKAN\_revenue* .</li></ul> |

</Accordion>

## Aclaraciones

Aclaraciones relativas a campos obligatorios, enriquecimiento, certificación y más.

<div id="faq" />

<Accordion title="Preguntas frecuentes">

| Preguntas y respuestas sobre postbacks |
| --- |
| **¿Los campos de enriquecimiento son obligatorios?**<br /><br />Por el momento, procesaremos el postback aunque falte uno o más de los siguientes parámetros de enriquecimiento. Ten en cuenta que la información se requiere por las siguientes razones:<ul><li>**ID de campaña de la red de publicidad**: si tenemos integración de costos contigo, esto se reporta usando tu ID de campaña.</li><li>**Nombre de la campaña de la red de publicidad**: muchos anunciantes hacen referencia al nombre de la campaña y no al número de campaña.</li><li>**Dirección IP**: requerida para la resolución de la geolocalización.</li><li>**Marca de tiempo**: nos ayuda a atribuir la instalación a la fecha correcta.</li></ul> |
| **¿Podemos enviar nuestro ID de campaña, o nuestro nombre de campaña, pero no ambos?**<br /><br />Ver la respuesta anterior. Considera rellenar tanto el ID como el nombre con el mismo valor. |
| **Estamos utilizando el método *Enriquecer y reenviar.* ¿Podemos agregar pares de clave y valor que no están en la especificación de AppsFlyer?**<br /><br />Sí. Procesaremos el postback e omitiremos la información adicional siempre que la firma de atribución sea válida. |
| **¿Las plantillas de postbacks de SKAN son distintas de las plantillas de postbacks existentes?**<br /><br />Sí. El flujo y la estructura difieren. |
| **¿Recibiremos un postback de SKAN y un postback de modelado probabilístico/determinista relacionados con la misma instalación, es decir, reportes duplicados de la misma instalación?**<br /><br />Sí. Para cada caso, registramos una instalación atribuida a ti, independientemente del método, te enviaremos un postback.<br /><br />Usa *attribution\_source* para diferenciar los postbacks de SKAN. |
| **¿Estamos obligados a procesar el postback de AppsFlyer?**  <br /> <br /><br />N.º Ten en cuenta que la práctica recomendada es optimizar las campañas de acuerdo a la calidad del usuario reportada a través del postback. |
| **¿Se espera que llamemos a los enlaces de atribución de AppsFlyer o es suficiente enviar el postback con la carga útil de SKAN y los datos enriquecidos?**<br /><br />Basta con enviarnos la carga útil de SKAN y los datos enriquecidos. |
| **¿Cuáles son los requisitos para obtener la certificación en el panel de control de AppsFlyer como partner integrado de SKAN?**<ul><li>Integración completa utilizando uno de los métodos enumerados en este artículo.</li><li>Envíanos postbacks de aplicaciones usando AppsFlyer como tu partner de atribución.</li></ul> |
| **¿Cómo me afecta el límite de 100 ID de campaña de SKAN**?<br /><br />El límite 1-100 hace referencia a la forma en que firmas y numeras tus campañas en Apple. Significa que, en cualquier momento, puedes tener 100 campañas únicas simultáneas. Te permitimos enriquecer el postback con tu nombre e ID de campaña reales. Lo que significa que asignas el ID de campaña de SKAN a tus ID de campaña reales en uso en el momento en que se recibe el postback. Hacerlo significa que el límite de 100 ID no restringe el número de campañas que mides en AppsFlyer siempre que, por supuesto, no tengas más de 100 campañas simultáneas para una aplicación determinada. |

</Accordion>

<div data-zendesk-anchors="appsflyer-offering-for-ad-networks=oferta-de-appsflyer-para-redes-de-publicidad h_01HDG8991Y6EWWN9KYBR9FEAJZ=oferta-de-appsflyer-para-redes-de-publicidad skan-data-flow=flujo-de-datos-de-skan h_01HDG8991Y5DW0BVD674RS88F2=flujo-de-datos-de-skan main-integration-parts=partes-principales-de-la-integraci%C3%B3n h_01HDG8991YDTY85NK7TQ26B2Z1=partes-principales-de-la-integraci%C3%B3n send-data-to-appsflyer=env%C3%ADo-de-datos-a-appsflyer h_01HDG8991YTFP2HE0Y8P8X0C20=env%C3%ADo-de-datos-a-appsflyer h_01HDG8991YRW3TWSDARFM58FA8=enrich-and-forward skan-enriched-postback-protocol=protocolo-de-postback-enriquecido-de-skan h_01HDG8991YAKZMSA4MAY0YTFPB=protocolo-de-postback-enriquecido-de-skan skan-enriched-postback-json-parameters=par%C3%A1metros-json-de-postbacks-enriquecidos-de-skan h_01HDG8991YS91CWESZH0M7CA00=par%C3%A1metros-json-de-postbacks-enriquecidos-de-skan curl-example%E2%80%94enriched-skan-3-postback=ejemplo-de-curl-postback-de-skan-3-enriquecido h_01HDG8991YFHBQDRG4K0XA3JQ8=ejemplo-de-curl-postback-de-skan-3-enriquecido curl-example%E2%80%94enriched-skan-4-postback-with-fine-conversion-values=ejemplo-de-curl-postback-de-skan-4-enriquecido-con-valores-de-conversi%C3%B3n-precisos h_01HDG8991YNVCK92TVNJHGKNG5=ejemplo-de-curl-postback-de-skan-4-enriquecido-con-valores-de-conversi%C3%B3n-precisos curl-example%E2%80%94enriched-skan-4-postback-with-coarse-conversion-values=ejemplo-de-curl-postback-de-skan-4-enriquecido-con-valores-de-conversi%C3%B3n-aproximados h_01HDG8991YXTS27V0NJ4ZXQ53T=ejemplo-de-curl-postback-de-skan-4-enriquecido-con-valores-de-conversi%C3%B3n-aproximados h_01HDG8991YGHWJ9R1ZKTCFJZCA=redirect implementation=implementaci%C3%B3n h_01HDG8991YBR7VWRH9079GT695=implementaci%C3%B3n query-params-for-campaign-details-not-mandatory=par%C3%A1metros-de-consulta-para-los-detalles-de-la-campa%C3%B1a-no-obligatorio h_01HDG8991YQB77MMF906PCAWC2=par%C3%A1metros-de-consulta-para-los-detalles-de-la-campa%C3%B1a-no-obligatorio receive-data-from-appsflyer=recibir-datos-de-appsflyer h_01HDG8991ZNF2PKKJN3FPN6QXA=recibir-datos-de-appsflyer h_01HDG8991ZKR35WHWVX0DHC612=principles h_01HDG8991ZG9GMMY57XYZF1Q3S=postback-macros-available-to-ad-network-partners h_01HDG8991ZD6ARRK6Z83NQBGRR=skan-postback-examples integration-testing=pruebas-de-integraci%C3%B3n h_01HDG8991ZS10MJJ3ZN31YDPTK=pruebas-de-integraci%C3%B3n h_01HDG8991ZPR41S5T9HZ9N1ZWF=real-environment testing-integration=probar-la-integraci%C3%B3n h_01HDG8991ZJ1KTHX6FE9R0QJNP=probar-la-integraci%C3%B3n test-criteria=criterios-de-prueba h_01HDG8991ZP59K8RQQ7G1GGMPG=criterios-de-prueba h_01HDG8991Z7DX65Y3E6RPHB2M3=simulated-postbacks integration-steps=pasos-de-integraci%C3%B3n h_01HDG8991ZZPYH7H329EY8TNV9=pasos-de-integraci%C3%B3n test-criteria::26c15d59=criterios-de-prueba-1 h_01HDG8991ZR4F21KVYF0MQ9GZA=criterios-de-prueba-1 clarifications=aclaraciones h_01HDG8991Z8C0K0SMBT9VSX12Y=aclaraciones h_01HDG8991ZDAGFV8GGC1RH73KQ=faq" />
