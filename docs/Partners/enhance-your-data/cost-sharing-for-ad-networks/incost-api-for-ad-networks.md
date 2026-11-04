---
title: API InCost para redes de publicidad
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Marketers
    - ROI360
    - Ad Networks
  created_at: '2020-04-26T19:13:47Z'
  edited_at: '2026-09-17T00:35:29Z'
  id: 360007714957
  locale: es
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/es/articles/360007714957
---
> **Resumen:** La API InCost, que forma parte de AppsFlyer ROI360, permite a las ad network enviar datos de costo publicitario de forma programática a AppsFlyer. Al hacerlo, los anunciantes obtienen datos de costos agregados y comprenden el verdadero impacto de tu red.

<div id="about-incost-api" />

## Acerca de la API InCost

La API InCost es la solución óptima para que las redes de publicidad envíen datos de costos a AppsFlyer. Los partners de la red de publicidad envían datos detallados de los costos publicitarios a AppsFlyer mediante la API. AppsFlyer ingiere y procesa los datos, y los pone a disposición de los anunciantes y partners a través de paneles de control y reportes.

<div id="benefits" />

#### Ventajas

* Ayuda a tus clientes a comprender el verdadero impacto de tu red con reportes de costos sin fricciones. Sin datos de costos, a tus clientes les falta una pieza crucial del rompecabezas de la medición y no pueden medir con precisión el ROAS. En consecuencia, pueden invertir erróneamente en otras fuentes de medios, lo que afectaría negativamente tus resultados.
* Demuestra tu ROI con una solución que garantiza una medición de costos precisa, completa y en tiempo real.
* La API InCost es rápida y sencilla de implementar, y el impacto es casi inmediato. También obtienes un control completo sobre cómo y cuándo envías los datos, incluida la capacidad de enviar datos de costos de hasta 90 días atrás.
* La API InCost es compatible con todos los modelos de precios de campaña, no solo el CPI (que es el único modelo disponible cuando se envía el costo por clic).
* Destácate en el Partner Marketplace de AppsFlyer con una insignia de "Costo" que indica que esta es una función que admites.

<div id="implementing-incost-api" />

## Implementación de la API InCost

**Requisitos previos**: Para cumplir los requisitos de la API InCost, tu red de publicidad requiere lo siguiente:

* Que el 90 % de las campañas incluyan el ID de campaña en la atribución.
* La capacidad de enviar datos al menos 6 veces al día para aumentar la actualización de los datos. Los horarios específicos dependen de la red de publicidad.
* [Si la red de publicidad actualiza los datos con carácter retroactivo] La capacidad de enviar datos de los últimos 7 días cada vez, para una mayor exhaustividad de los datos.

**Para implementar la API InCost y comenzar a enviar datos de costos a AppsFlyer**:

* Sigue los pasos de la tabla siguiente.

| N.º de paso | Acción |
| --- | --- |
| 1 | Solicitar InCost:<ol><li>En AppsFlyer, en el menú superior, selecciona **Ayuda** > **Contactar con nuestro equipo**.<br />Se abre el widget del asistente para partners.</li><li>Selecciona **Habilitación de la medición de costos** y envía tu información.<br />Una vez enviada, se abre un ticket y un ingeniero de soluciones para partners de AppsFlyer se pondrá en contacto contigo.</li></ol> |
| 2 | Asegúrate de que las jerarquías de campaña (ID de campaña y, opcionalmente, ID de conjunto de anuncios e ID de anuncio) se incluyan en los enlaces de atribución para más del 90 % de tu tráfico. |
| 3 | Obtén el  <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">token de API</Anchor> de AppsFlyer desde el panel de control de AppsFlyer. |
| 4 | Entrega el token de API a tu desarrollador para que lo use en el encabezado de autorización de API y pídele que siga <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-overview">sus instrucciones</Anchor> para implementar los 3 métodos de API:<ol><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get">Obtener la lista de aplicaciones</Anchor>.</li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-uploader-post">Carga de InCost</Anchor>: dile al desarrollador qué campos del JSON debe rellenar:<ul><li>Los campos obligatorios deben rellenarse. Es decir, no deben enviarse vacíos.</li><li>La fuente de medios está restringida a las fuentes de medios asociadas a (registradas en) tu cuenta de red de publicidad. Obtén la lista de tu gerente de desarrollo de partners.</li><li>Ten en cuenta la <Anchor target="_blank" href="/marketers/es/docs/about-data-freshness-and-timezone-support#zona-horaria-específica-de-la-aplicación">zona horaria</Anchor> de la aplicación (reportada a través de la API Obtener lista de permisos de la aplicación) para alinear las fechas de los datos de costos con las de la aplicación.</li><li>Si hay campos que no forman parte de la jerarquía de reporte de costos de la campaña, no los incluyas. Por ejemplo, ID de conjunto de anuncios, nombre del recurso, ID de anuncio, nombre del anuncio.</li></ul></li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-jobstatus-get">Obtener el estado del trabajo</Anchor>.</li></ol> |
| 5 | Pruebe la integración:<ol><li>En el hilo del ticket (del paso 1), notifica a AppsFlyer que se ha completado la implementación de la API y obtén permisos para las siguientes aplicaciones, que se pueden usar para probar la API sin usar datos reales:<ul><li>com.cost.app</li><li>id888123456</li></ul></li><li>En AppsFlyer, en el menú lateral, selecciona **Collaborate** > **Partner Marketplace** y selecciona el partner.</li><li>Haz clic en **Configurar integración**.</li><li>Selecciona 1 de las aplicaciones de prueba.</li><li>Abre la pestaña **Costo** del partner integrado.</li><li>Activa la opción **Obtener datos de costos**.</li><li>Haz clic en **Guardar costo**.</li><li>Haz clic en **Probar conexión**.<br />La API está activa.</li></ol> |
| 6 | En el hilo del ticket (del paso 1), notifica a AppsFlyer que se completó la implementación de la API y espera a que confirmen que tu integración está operativa. |
| 7 | Asegúrate de que tus anunciantes habiliten la <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#cost-tab">obtención de datos de costos</Anchor> en la pestaña de costos de su página de partner integrado de AppsFlyer. Luego comenzarán a recibir datos de costos. |

<div id="note" />

> 📘 **Nota:**
>
> Mejor práctica: vuelve a enviar datos de una fecha concreta solo si su costo ha cambiado. Puedes enviar los últimos 7 días en cada llamada, pero no necesitas reenviar los registros que no hayan cambiado.

<div id="fields-for-incost-upload-json" />

### Campos del JSON de carga de InCost

<table><thead><tr><th>Campo</th><th>Obligatorio</th><th>Observaciones</th></tr></thead><tbody><tr><td>fecha</td><td><span>Sí</span></td><td><ul><li><span>Fecha del gasto</span></li><li> Formato: <code>YYYY-MM-DD</code> </li><li> <span>Ejemplo:</span><code><span>2019-12-30</span></code> </li></ul></td></tr><tr><td>id_aplicación</td><td>Sí</td><td><ul><li>El ID de la aplicación tal y como aparece en la plataforma de AppsFlyer.</li><li><span>Formato: cadena de hasta 250 caracteres.</span></li><li> <span>Ejemplo: </span><span>Android:<code>com.app.name</code>, </span>iOS: <code>id123456789</code> </li></ul></td></tr><tr><td><span>fuente_de_medios</span></td><td><span>Sí</span></td><td><ul><li><span>Nombre de la red (ID) que muestra el anuncio asociado con tu cuenta de partner de la red de publicidad en AppsFlyer.</span></li><li><span>Formato: cadena de 50 caracteres.</span></li><li> Ejemplo: <code>network_int</code> </li></ul></td></tr><tr><td><span>af_prt</span></td><td><span>No\*</span></td><td><ul><li>Obligatorio para la atribución de agencia y los datos de costos. </li><li>Nombre de la agencia tal como se muestra en el enlace de atribución y está asociado con la cuenta de la agencia en AppsFlyer. </li><li>Formato: cadena de 50 caracteres. </li><li>Ejemplo: <code>agencya</code> </li><li>Si se reenvían datos de costo para las mismas fechas y se incluye <code>af_prt</code> en una llamada posterior a la API cuando no estaba presente en la original, lo que da como resultado datos de costo duplicados.</li></ul></td></tr><tr><td><span>id_campaña</span></td><td><span>Sí</span></td><td><ul><li> <span>Debe ser idéntico al parámetro </span><span><code>af_channel</code></span> enviado en el enlace de atribución. </li><li><span>No se permite una cadena vacía.</span></li><li><span>Formato: cadena de 24 caracteres.</span></li><li> <span>Ejemplo: <code>123abc</code></span><span></span> </li></ul></td></tr><tr><td><span>campaign_name</span></td><td><span>Sí</span></td><td><ul><li><span>Formato: cadena de 100 caracteres.</span></li><li> Ejemplo: <code>my_campaign123</code> </li></ul></td></tr><tr><td><span>id_anuncio</span></td><td>No\*</td><td><ul><li> Obligatorio si envías <span><code>ad_name</code></span>. </li><li> Debe ser idéntico al parámetro <code>af_adset_id</code> enviado en el enlace de atribución. </li><li> Si tus reportes de costos no admiten <code>adset_id</code>, no lo envíes. </li><li><span>Formato: cadena de 24 caracteres.</span></li><li> <span>Ejemplo: </span><code><span>123A</span></code> </li></ul></td></tr><tr><td><span>adset_name</span></td><td><span>No</span></td><td><ul><li> Si envías este campo, también debes enviar <code>adset_id</code>. </li><li><span>Formato: cadena de 100 caracteres.</span></li><li> Ejemplo:<code>my_adset_name</code> </li></ul></td></tr><tr><td><span>id_adset</span></td><td>No\*</td><td><ul><li>Obligatorio si envías <code>adset_name</code>.</li><li> Este campo debe ser idéntico al parámetro <code>af_ad_id</code> enviado en el enlace de atribución. </li><li> Si tus reportes de costos no admiten <code>adset_id</code>, no lo envíes. </li><li><span>Formato: cadena de 24 caracteres.</span></li><li>Ejemplo: <code>123AB</code> </li></ul></td></tr><tr><td><span>id_sitio</span></td><td>No</td><td><ul><li>ID único que identifica al publisher que muestra el anuncio.</li><li>Formato: cadena de 24 caracteres.</li></ul></td></tr><tr><td><span>ad_name</span></td><td><span>No</span></td><td><ul><li> Si envías este campo, también debes enviar <code>ad_id</code>. </li><li><span>Formato: cadena de 100 caracteres.</span></li><li>Ejemplo: <code>Ad-name</code> </li></ul></td></tr><tr><td><span>geolocalización</span></td><td><span>No</span></td><td><ul><li><span>El país que registraste como asociado con el costo.</span></li><li><span>Siempre que sea posible, debe representar el país en el que se mostró el anuncio.</span></li><li><span>Formato: <span>código de país ISO 3166 de 2 caracteres</span></span></li><li> Ejemplo:<code>US, CN, ZA</code> </li></ul></td></tr><tr><td>moneda</td><td><span>Sí</span></td><td><ul><li><span>Tipo de divisa del gasto.</span></li><li><span>Formato: <span>código de divisa ISO 4217 de 3 caracteres.</span></span></li><li> <span>Ejemplo:</span> <span><code>USD, EUR, ZAR</code></span> </li></ul></td></tr><tr><td>spend</td><td>Sí</td><td><ul><li>Monto de gasto con la divisa especificada. </li><li>Se permiten cinco dígitos después del punto decimal.</li><li>Se permite el valor 0 (cero).</li><li>NO se permiten valores negativos.</li><li>No envíes delimitadores <code>,</code>.</li><li>No envíes valores entre comillas. </li><li>Formato: número decimal</li><li>Valores de ejemplo: <code>1</code> <code>1.2</code> <code>1234.20</code> </li></ul></td></tr><tr><td>channel</td><td>No</td><td><ul><li>Debe ser idéntico al parámetro <code>af_c_id</code> enviado en el enlace de atribución.</li><li>Formato: cadena de 20 caracteres.</li><li>Ejemplo: <code>my_channel</code> </li></ul></td></tr><tr><td><span>palabras clave</span></td><td>No</td><td><ul><li>Formato: cadena de 100 caracteres.</li><li>Ejemplo: <code>abc app</code> </li></ul></td></tr><tr><td>reported_clicks</td><td>No</td><td><ul><li>Número de clics reportados por la red para este registro.</li><li>Monto de gasto con la divisa especificada.</li><li>Ejemplo: <code>123A</code> </li><li>Opcional: Si está vacío o se omite, se informa como 0.</li><li>Se rechazan los valores decimales o negativos (error 422: <code>Reported clicks can be positive integer</code>).</li></ul></td></tr><tr><td>reported_impressions</td><td>No</td><td><ul><li>Número de impresiones reportadas por la red para este registro.</li><li>Monto de gasto con la divisa especificada.</li><li>Ejemplo:<code>2019-12-30</code> </li><li>Opcional: Si está vacío o se omite, se informa como 0.</li><li>Se rechazan los valores decimales o negativos (error 422: <code>Reported impression can be positive integer</code>).</li></ul></td></tr><tr><td colspan="3">\* Consulta la columna de observaciones, ya que en algunos casos debes enviar este campo.</td></tr></tbody></table>

<div data-zendesk-anchors="incost-api=acerca-de-la-api-incost h_01HE0WCBD9GD66KB1QGQ9MEXBJ=acerca-de-la-api-incost benefits=ventajas h_01HKVW85AYFG91PGYE5BDQVJNR=ventajas implementing-incost-api=implementaci%C3%B3n-de-la-api-incost h_01HKVWSWTWETTES5ZTNZ05X9VA=implementaci%C3%B3n-de-la-api-incost h_01M2J3GBMFJW7XT08MK5JR3D3Y=nota fields-for-incost-upload-json=campos-del-json-de-carga-de-incost h_01HM8VCV81GQ6XQ4NA1EDCZ4K7=campos-del-json-de-carga-de-incost" />
