---
title: API de lista de aplicaciones para ad network
metadata:
  keywords:
    - API
    - Ad Networks
    - Partners
    - Developers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-08-06T20:11:15Z'
  edited_at: '2026-08-12T12:27:16Z'
  id: 360011700857
  locale: es
  section: APIs for ad networks
  section_id: 6551618728209
  url: https://support.appsflyer.com/hc/es/articles/360011700857
---
> **De un vistazo:** Las ad network pueden recuperar metadatos de las aplicaciones asociadas a su cuenta de partner integrada.

## Obtener API de lista de apps

Las siguientes secciones incluyen la información necesaria para usar la API.

<div id="get-app-list-basics" />

<Accordion title="Conceptos básicos para obtener la lista de aplicaciones">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Nota</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>GET</code></td></tr><tr><td>Ruta</td><td><span>https://hq1.appsflyer.com/api/mng/apps</span></td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera: <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a> </li></ul></td></tr><tr><td rowspan="3"> Respuesta</td><td>Resultados</td><td>Devuelve en JSON</td></tr><tr><td>Límite de solicitud</td><td><ul><li>20 solicitudes/minuto</li><li>100 solicitudes/día</li></ul></td></tr><tr><td>Límite de registros</td><td>1.000 registros/solicitud. Si se van a devolver más de 1.000 registros, utiliza solicitudes de paginación posteriores, descritas en este artículo.</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="Solicitud API">

La solicitud de la API consta del método, la ruta, el parámetro obligatorio capabilities y los parámetros opcionales de paginación. El token se incluye en el encabezado de autorización.

**Emitido**

```http
GET https://hq1.appsflyer.com/api/mng/apps?capabilities={capabilities} 
```

#### Parámetros obligatorios para obtener la lista de aplicaciones

<Table>
  <thead>
    <tr>
      <th>
        Parámetro de consulta
      </th>
      <th>
        Descripción
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Capacidades
      </td>
      <td>
        Para obtener la lista y el número de aplicaciones para las que tienes capacidades de permiso/integración, establece el parámetro capabilities en una de las opciones indicadas.

        | Opción | Tipo de valor esperado | Nota |
        | --- | --- | --- |
        | `protect_360` | Permiso de reporte | Obtén <Anchor target="_blank" href="/partners/es/docs/protect360-for-integrated-partners">Reportes de raw data de Protect360 para ad networks</Anchor> |
        | `cost` | Integración | La aplicación está habilitada para obtener datos de costo <Anchor target="_blank" href="/partners/es/docs/incost-api-for-ad-networks">a través de la API de InCost</Anchor> |

        **Ejemplo**: Lista de aplicaciones para las que tienes permiso de API de reporte de Protect360:`capabilities=protect_360`
      </td>
    </tr>
  </tbody>
</Table>

#### **Mecanismo de paginación**

Se ha implementado un mecanismo de paginación, siempre operativo.

**Principios de paginación:**

* Devuelve hasta 1.000 registros por solicitud (página).
* Los JSON de respuesta contienen las siguientes claves relacionadas con la paginación:
  * **meta.total\_items**: El número de registros que devolverán todas las páginas en conjunto. Representa el número de aplicaciones para las que se te han concedido las capacidades consultadas.
  * Los enlaces de paginación (mostrados en el JSON siguiente) tienen las siguientes claves:
    * **links.prev**: Si hubo una solicitud anterior: la solicitud usada para generar la página anterior.
    * **links.self**: La solicitud actual: la solicitud usada para generar el JSON actual (página)
    * **links.next**: La solicitud necesaria para obtener la página siguiente. Si no hay una clave next, esta es la última página.

**Usa uno de los siguientes métodos de control de paginación:**

* [Mejores prácticas] Usa los enlaces en el JSON: Si existe la clave links.next, úsala para crear una solicitud y obtener la página siguiente. Sigue haciéndolo hasta que recibas un JSON sin una clave links.next.
* Implementa mediante programación los parámetros limit y offset junto con la clave total\_items.

**Ejemplo de JSON de enlaces de paginación**

* El ejemplo siguiente contiene el resultado de la primera solicitud y consiste en la segunda solicitud, que contiene dos registros en la sección de datos (no mostrada).
* El número total de registros que se devolverán es 6.
* La clave **links.next** contiene la solicitud que devuelve la página siguiente: los registros 5 y 6.

```json
{                                                                                         
    "data": {[...]},   
    "meta": {
        "total_items": 6
    },
    "links": {
        "prev": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=2",
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=2&limit=2",
        "next": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=4&limit=2"
    }
}
```

#### Parámetros del mecanismo de paginación (opcional)

<table><thead><tr><th>Parámetro de consulta</th><th>Descripción</th></tr></thead><tbody><tr><td>limit</td><td><p>Número de registros que se devuelven por llamada</p><ul><li>Máximo: 1.000</li><li>Si no envías <code>limit</code>, se establece automáticamente en 1.000.</li><li>Ejemplo: <code>limit=2</code> </li><li>Obligatorio: No</li></ul></td></tr><tr><td>offset</td><td><p>El primer registro que se devolverá en la llamada. La numeración de los registros empieza en 0. </p><ul><li>Si no envías <code>offset</code>, se establece automáticamente en 0.</li><li>Ejemplo: <code>offset=2</code> </li><li>Obligatorio: No</li></ul></td></tr><tr><td colspan="2"> </td></tr></tbody></table>

</Accordion>

<div id="json-response" />

<Accordion title="Respuesta JSON">

| **Clave** | **Nota** |
| --- | --- |
| ID | ID de la aplicación, por ejemplo: `id123456789`, `com.myapp.com` |
| tipo | Devuelve siempre `app` |
| nombre | Nombre de aplicación |
| plataforma | iOS o Android |
| moneda | Código de divisa específico de la aplicación, tal como lo establece el anunciante |
| time\_zone | Zona horaria específica de la aplicación, tal como la establece el anunciante |
| total\_items | Número de aplicaciones para las que la ad network tiene la opción de capacidades solicitada |
| enlaces | Mecanismo de paginación (explicado en la sección de parámetros)<ul><li>prev: la llamada utilizada para generar la página anterior</li><li>self: la llamada utilizada para generar la página actual</li><li>next: la llamada utilizada para generar la página siguiente</li></ul> |

</Accordion>

<div id="get-app-list-curl-example-and-response" />

<Accordion title="Ejemplo de curl y respuesta para obtener la lista de aplicaciones">

**Solicitud de curl**

Este ejemplo incluye una llamada completa, incluidos los parámetros opcionales de paginación.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&limit=1000&offset=0' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Respuesta JSON**

```json
{
    "data": [
        {
            "id": "com.appsflyer.xpend_qa1",
            "type": "app",
            "attributes": {
                "name": "com.appsflyer.xpend_qa1",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC"
            }
        },
        {
            "id": "com.abc.app",
            "type": "app",
            "attributes": {
                "name": "com.abc.app",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC",
                "enable_retargetting": true
            }
        },
        {
            "id": "com.xyz.app",
            "type": "app",
            "attributes": {
                "name": "com.xyz.app",
                "platform": "android",
                "currency": "JPY",
                "time_zone": "UTC"
            }
        }
    ],
    "meta": {
        "total_items": 3
    },
    "links": {
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=1000"
           }
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="Códigos de respuesta HTTP">

| Código | Mensaje | Observaciones/resolución de problemas |
| --- | --- | --- |
| 200 | Correcto | Datos válidos devueltos |
| 200 | Correcto | **Síntoma**: No se devuelven datos<br /><br />**Acción**: Asegúrate de que el token de autenticación esté en el encabezado Bearer. |
| 400 | Solicitud incorrecta | <ul><li>Consulta el mensaje incluido en el JSON</li><li>JSON vacío: se ha especificado una capacidad no válida</li></ul> |
| 401 | No autorizado | **Mensaje**: El token de autorización tiene un formato incorrecto<br /><br />Asegúrate de que tienes el token correcto; el token debe tener más de 700 caracteres. |
| 404 | No encontrado | <ul><li>Resuelve cualquier problema relacionado con la red o el cortafuegos.</li><li>Asegúrate de que las <Anchor target="_blank" href="/marketers/es/docs/appsflyer-server-ip-address-ranges-allowlisting">direcciones IP de AppsFlyer estén en la lista de permitidos</Anchor></li><li>Asegúrate de que usas el token emitido más recientemente.</li><li>No se han encontrado datos: el tipo de permiso/integración (capacidades) solicitado es legal, pero no se ha encontrado ninguna app con permiso.</li></ul> |
| 429 | Demasiadas solicitudes | Se ha superado el límite de solicitudes |

</Accordion>

<div data-zendesk-anchors="get-app-list-api=obtener-api-de-lista-de-apps h_01KQS54YXJ2XBV5BAT3TGJ9SBT=obtener-api-de-lista-de-apps h_01KQS54YXJHYS9KC2Y7BEP87MZ=get-app-list-basics h_01KQS54YXJJ9SE7DSRTA2X2A9M=api-request get-app-list-mandatory-parameters=par%C3%A1metros-obligatorios-para-obtener-la-lista-de-aplicaciones h_01KQS54YXJPDZGJB7K6KH1D2W1=par%C3%A1metros-obligatorios-para-obtener-la-lista-de-aplicaciones pagination-mechanism=mecanismo-de-paginaci%C3%B3n h_01KQS54YXJ9X0XBJQ01K6WK2RB=mecanismo-de-paginaci%C3%B3n pagination-mechanism-parameters-optional=par%C3%A1metros-del-mecanismo-de-paginaci%C3%B3n-opcional h_01KQS54YXJX943PMF5JWV67THW=par%C3%A1metros-del-mecanismo-de-paginaci%C3%B3n-opcional h_01KQS54YXJS43JYQQHCWCAED6Q=json-response h_01KQS54YXJJK7Y23TSSF1BB58R=get-app-list-curl-example-and-response h_01KQS54YXJ2638DBZWDSN4J9G4=http-response-codes" />
