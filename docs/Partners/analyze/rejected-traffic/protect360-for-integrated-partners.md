---
title: Protect360 para socios integrados
metadata:
  keywords:
    - Protect360
    - Ad Networks
    - Partners
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2017-09-19T08:27:29Z'
  edited_at: '2026-08-12T12:27:36Z'
  id: 115004745523
  locale: es
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/es/articles/115004745523
---
> **Resumen:** Los socios integrados, como redes publicitarias y agencias, pueden visualizar el fraude relacionado con el tráfico que ha sido identificado y bloqueado por los motores ProtectLITE y Protect360, así como también por las reglas de validación definidas manualmente por el cliente.

<div id="overview" />

## Visión general

AppsFlyer detecta y bloquea el fraude a través de: 

* <Anchor target="_blank" href="/marketers/es/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">ProtectLITE</Anchor><Anchor target="_blank" href="/marketers/es/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">: Protección básica contra fraudes para todos los clientes.</Anchor>
* <Anchor target="_blank" href="/marketers/es/docs/protect360-anti-fraud-guide">Protect360</Anchor><Anchor target="_blank" href="/marketers/es/docs/protect360-anti-fraud-guide">: Protección avanzada contra fraudes para anunciantes con un plan de suscripción premium.</Anchor>

Los anunciantes deben otorgar:

* Permisos de ad networks <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions-tab">permisos</Anchor> para **acceder al dashboard de Protect360 y a los reportes de raw data** (incluido ProtectLITE) y **acceder a datos agregados de eventos in-app** (para fraude en eventos in-app).
* Permisos <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions-tab">a las agencias</Anchor> para **acceder al panel de control y a los datos sin procesar de Protect360.**

Con los permisos adecuados, los socios integrados pueden:

* Visualizar datos relacionados con el tráfico que generan.
* Descargar <Anchor target="_blank" href="/marketers/es/docs/protect360-anti-fraud-guide#raw-data">informes de datos en bruto</Anchor> relacionados.

Además, hay <Anchor target="_blank" href="/partners/es/docs/protect360-reports-for-ad-networks">informes de datos sin procesar</Anchor> accesibles para redes publicitarias sobre límites de clics e impresiones, así como firmas de clics fallidos, que no requieren permisos de los anunciantes.

<div id="note" />

> 📘 **Nota:**
>
> Para anunciantes que trabajan con redes publicitarias a través de una agencia, es necesario que tanto la red publicitaria como la agencia tengan acceso a los datos. Por lo tanto, el anunciante debe integrar a ambos en AppsFlyer y concederles permiso para acceder a los datos.
>
> Si solo la agencia está integrada y tiene permisos, la red publicitaria no podrá acceder a los datos.

<div id="dashboard-view" />

### Vista del panel de control

**Requisitos previos**: Permiso del anunciante para acceder a ProtectLITE y Protect360. 

Los socios integrados pueden ver el panel y los gráficos; consulte la captura de pantalla que se muestra a continuación.

Obtenga más información acerca de los datos disponibles en los paneles de control <Anchor target="_blank" href="/marketers/es/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting#panel-de-control">ProtectLITE</Anchor> y <Anchor target="_blank" href="/marketers/es/docs/protect360-anti-fraud-guide#dashboard">Protect360</Anchor> .   

Limitaciones:

* Las redes publicitarias no tienen acceso al panel de anomalías.

[![p360_dashboard_1.jpg](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)](https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg)

* Las ad networks y las agencias no pueden acceder al estudio de protección contra el fraude ni al nivel de raw data de los datos etiquetados. Sin embargo, pueden verlo de forma agregada en el dashboard de Protect360, en la atribución etiquetada y en los eventos in-app etiquetados. Además de identificar el fraude por tipo de etiqueta (nueva versión, etc.). Para saber más sobre FPS, consulta <Anchor target="_blank" href="/marketers/es/docs/beta-fraud-protection-studio">este artículo</Anchor>.

  <Image alt="" src="https://files.readme.io/7e8bee04ecaf53148f65ae0aa9b2e3559a550bdbc5a5ebf9047a7e82dc093966-44928678660881.png" width="624px" />

  <Image alt="" src="https://files.readme.io/fa35e6046d6c06579e602ccc1cb919e5312ec22055b3e29d3ead6b2a7ab5ea82-44928694758161.png" width="624px" />

<div id="raw-data-reports" />

### Informes de datos sin procesar

**Requisitos previos: Permiso del anunciante para acceder a ProtectLITE y Protect360.**

Los informes de datos brutos de Protect360 muestran el fraude identificado y bloqueado a través de ProtectLITE, Protect360 y las reglas de validación.

Los informes están disponibles a través de:

* Exportar datos: En AppsFlyer, desde el menú lateral, seleccione **Informes** > **Exportación de Datos Brutos**
* Permisos a las redes publicitarias <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions-tab">para</Anchor> **acceder al panel de Protect360 y a los informes de datos sin procesar** (incluyendo ProtectLITE) y **acceder a datos agregados de eventos in-app** (para fraudes en eventos in-app).

Obtenga más información sobre los <Anchor target="_blank" href="/marketers/es/docs/protect360-raw-data-reports">informes de datos brutos de Protect360</Anchor>.

<div id="protect360-ad-network-reporting-api" />

## API de informes de redes publicitarias de Protect360

* Los informes de datos brutos que se describen en esta sección están disponibles para las redes publicitarias a través de API.
* Informes equivalentes están accesibles desde el panel de control en la página de Exportar Datos.
* Si el anunciante no posee una suscripción a Protect360, solo estará disponible el informe de Instalaciones.

**Requisitos previos**

* Para acceder a los datos del anunciante mediante API, el anunciante concede a la red publicitaria <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions-tab">permisos</Anchor> para acceder a su panel de control y a los datos de Protect360 mediante API. Las redes publicitarias con acceso al panel de control están autorizadas a usar la API. No se requiere ninguna acción por parte del anunciante.
* Para obtener una lista de aplicaciones para las que tiene permisos de Protect360, utilice la <Anchor target="_blank" href="/partners/es/docs/app-list-api-for-ad-networks">API de lista de aplicaciones.</Anchor>
* El administrador debe obtener un token de autenticación de AppsFlyer <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">V2.0</Anchor> disponible en el panel.

<div id="protect360-api-reports" />

#### Informes de la API de Protect360

| Informe | Actualización de datos | Descripción |
| --- | --- | --- |
| Fraude en eventos dentro de la aplicación posteriores a la atribución | Diariamente a las 10:00 UTC | <ul><li>Eventos dentro de la aplicación llevados a cabo por instalaciones identificadas como fraudulentas.</li><li>Cualquier otro evento dentro de la aplicación que se considere fraudulento independientemente de la instalación.</li></ul>El informe puede filtrarse opcionalmente por tipo de evento en la aplicación, como se describe en la tabla de parámetros que se presenta a continuación.<br /><br />Tema del informe: `fraud-post-inapps` |
| Instalaciones posteriores a la atribución | Diariamente a las 10:00 UTC | <ul><li>Instalaciones identificadas como fraudulentas después de la atribución.</li><li>El informe puede filtrarse opcionalmente por la fecha de detección, como se describe en la sección siguiente.</li></ul>Tema del informe:  detección |
| Instalaciones | En tiempo real | Instalaciones bloqueadas con motivo del bloqueo<br /><br />Tema del informe:  blocked\_installs\_report |
| Evento en la aplicación | En tiempo real | Eventos dentro de la aplicación realizados por usuarios bloqueados<br /><br />Tema del informe: `blocked_in-app_events_report` |
| Clics | En tiempo real | Clics realizados por usuarios bloqueados<br /><br />Tema del informe: `blocked_clicks_report` |

<div id="procedure-for-ad-networks-to-get-protect360-reports-by-download" />

#### **Procedimiento para que las redes publicitarias obtengan informes de Protect360 a través de descarga**

**Para obtener un informe mediante la API:**

1. Identifique el informe necesario de la lista anterior.
2. Utilice el ejemplo relevante de curl (en la siguiente sección) para preparar su script.
3. Asegúrese de reemplazar los siguientes marcadores de posición:
   1. ID de la aplicación
   2. Desde la fecha
   3. Hasta la fecha
   4. Token de portador (token de autenticación de AppsFlyer <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">V2.0</Anchor>)
4. Algunas llamadas tienen [parámetros opcionales](/docs/protect360-for-integrated-partners#api-parameters), como se describe en este artículo.

<div id="curl-examples" />

### Ejemplos de curl

<div id="installs-blocked_installs_report" />

<Accordion title="Instalaciones (blocked_installs_report)">

Sustituya los marcadores de posición app\_id, desde, hasta y token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_installs_report/app/{app_id}?from={2020-07-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="postattribution-installs-detection" />

<Accordion title="Instalaciones tras la atribución (detección)">

Sustituya los marcadores de posición para el ID de la aplicación, desde, hasta y token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/detection/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additonal-fields=fraud_reason,fraud_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="inapp-event-blocked_in_app_events_report" />

<Accordion title="Evento dentro de la aplicación (blocked_in_app_events_report)">

Sustituya los marcadores de posición para el ID de la aplicación, desde, hasta y token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_in_app_events_report/app/?from=YYYY-MM-DD&to=YYYY-MM-DD&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="postattribution-inapp-events-fraud-fraud_post_inapps" />

<Accordion title="Fraude en eventos dentro de la aplicación tras la atribución (fraud_post_inapps)">

Sustituya los marcadores de posición para el ID de la aplicación, desde, hasta y token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/fraud-post-inapps/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,fraud_reason,fraud_sub_reason,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="clicks-blockedclicks_report" />

<Accordion title="Clics (blocked-clicks_report)">

Sustituya los marcadores de posición para el ID de la aplicación, desde, hasta y token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_clicks_report/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="protect360-ad-network-api-reference-guide" />

### Guía de referencia de la API de la red publicitaria Protect360

<div id="api-basics" />

<Accordion title="Conceptos básicos de la API">

Conceptos básicos de la API de la red publicitaria Protect360:

| Ruta | `https://hq1.appsflyer.com/api/adnets-data/v1/export/report_topic/app/app_id` |
| --- | --- |
| Método | GET |
| Parámetros de ruta (obligatorios) | <ul><li>`app_id`:<ul><li>El identificador de la aplicación, tal como aparece en el panel de AppsFlyer. Insértelo tal cual se muestra en el tablero.</li><li>Asegúrese de usar el prefijo **id.** para las aplicaciones iOS.</li></ul></li><li>P: ¿Las redes reciben correos electrónicos de notificación sobre la limitación de clics?</li></ul> |
| Tipos de contenido aceptados | `application/json` |
| Autorización | <ul><li>Token portador en el encabezado de la solicitud.</li><li>![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png)Solicite al administrador el token V2.0 de la página de <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">tokens</Anchor>. Este token tiene aproximadamente 700 caracteres.</li></ul> |
| Limitación de velocidad | <Anchor target="_blank" href="/marketers/es/docs/report-generation-quotas-rate-limitations">Limitaciones de velocidad</Anchor> |
| Limitación del rango de fechas | <ul><li>La fecha más antigua admitida: 90 días antes de los datos actuales</li><li>31 días de los 90 días anteriores</li></ul> |
| Limitaciones de filas | 200K filas |
| Características del informe | <ul><li>Cadena</li><li>Moneda: USD</li></ul> |

</Accordion>

<div id="api-parameters" />

<Accordion title="Parámetros de la API">

Parámetros de la API de Protect360:

| Parámetro | Descripción | Formato | Obligatorio |
| --- | --- | --- | --- |
| id\_aplicación | ID de la aplicación tal como aparece en AppsFlyer | Cadena | Sí |
| desde | Inicio del rango de fechas:<ul><li>Para las instalaciones, es la fecha de instalación.</li><li>Para eventos dentro de la aplicación, es la fecha del evento.</li></ul> | AAAA-MM-DD | Sí |
| hasta | Fin del rango de fechas:<ul><li>Para las instalaciones, es la fecha de instalación.</li><li>Para eventos dentro de la aplicación, es la fecha del evento.</li></ul> | AAAA-MM-DD | Sí |
| nombre\_del\_evento | [Opcional para fraudes en eventos dentro de la aplicación tras la atribución]<br /><br />Filtrar eventos por evento en la aplicación. Limite el informe a eventos específicos. Se pueden incluir uno o más eventos.<br /><br />Ejemplo de uso: `&event_name=af_purchase,af_login` | Cadena | No |
| detectar desde | [Opcional para instalaciones posteriores a la atribución]<br /><br />Inicio del rango de fechas para la detección de fraude. (Por defecto es 'desde'). | AAAA-MM-DD | No |
| detectar-hasta | [Opcional para instalaciones posteriores a la atribución]<br /><br />Fin del rango de fechas para la detección de fraude. (Por defecto es 'hasta'.) | AAAA-MM-DD | No |

</Accordion>

<div id="protect360-api-http-return-codes" />

<Accordion title="Códigos de retorno HTTP de Protect360 API">

Códigos de error y soluciones:

| Estado | Código | Síntoma/mensaje | Solución |
| --- | --- | --- | --- |
| Correcto | 200 | Archivo CSV vacío | `addtional_fields`Se ha utilizado más de una vez en la URI |
| Correcto | 200 | Archivo CSV vacío | Asegúrese de que las fechas de inicio y fin estén en el formato aaaa-mm-dd |
| Correcto | 200 | La página de inicio de sesión en HTML de AppsFlyer devuelve | Falta el token en el encabezado de Bearer token |
| Solicitud incorrecta | 400 | Solicitud incorrecta | <ul><li>Limitación del rango de fechas.<ul><li>La fecha más antigua permitida es 90 días antes del día actual.</li><li>El período no puede exceder los 60 días para instalaciones y los 90 días para informes dentro de la aplicación.</li></ul></li></ul> |
| No autorizado | 401 | No autorizado | Se encontró un token, pero no es válido. Verifique que dispone del token actual V2.0 para su cuenta. Solicite al administrador que recupere el token actual desde el panel de control. |
| No encontrado | 404 |  | <ul><li>El endpoint especificado es incorrecto</li><li>Asegúrese de que el ID de la aplicación sea correcto</li><li>No está autorizado para acceder a la aplicación.</li></ul> |

</Accordion>

<div id="impression-capping" />

## Umbral de impresiones

Si una red de anuncios presenta tasas extremadamente altas de fraude en impresiones o clics, Protect360 bloquea estas acciones de la red durante un ciclo de 24 horas. Esto significa que cualquier impresión o clic que ocurra después de alcanzar el umbral no se registra en AppsFlyer ni es elegible para atribución. Las impresiones/clics bloqueados aparecen en el panel de control y en los informes de Protect360.

El algoritmo de protección contra el fraude de AppsFlyer considera diversos parámetros al detectar este fraude, como el volumen de impresiones/clics, CVR, tasa de fraude detectada, fluctuaciones normales en la actividad, puntos de referencia industriales y geográficos, y parámetros propios. El algoritmo es dinámico y se actualiza cada hora para considerar las tendencias cambiantes.

**Activar repetidamente los umbrales de inundación de impresiones o clics puede conllevar la eliminación definitiva de la integración del socio en la plataforma de AppsFlyer.**

Umbrales de umbral de impresiones:

* Se aplican equitativamente a todas las redes publicitarias. Es decir, ninguna red publicitaria se salva de una limitación si exhibe tasas extremadamente altas de fraude en impresiones o clics.
* Operan a nivel de aplicación/red publicitaria. Es decir, el análisis del fraude considera todas las campañas de una red publicitaria en una aplicación, y el bloqueo afecta los reportes y la atribución de todas ellas (independientemente de si la cuenta tiene Protect360 o no).
* Se restablecen tras un ciclo de 24 horas y los bloqueos permanecen hasta que finaliza dicho ciclo. AppsFlyer no revela detalles sobre cuándo comienzan o terminan los ciclos.
* No se pueden modificar ni detener. Protect360 está meticulosamente calibrado y es exacto en la detección de fraude, y el algoritmo no se puede ajustar ni desactivar manualmente.
* Se pueden evitar deteniendo campañas y editores con actividad anómala.

<div id="faq" />

<Accordion title="Preguntas frecuentes">

Preguntas frecuentes sobre umbrales de impresiones y clics:

| **P: ¿Cuál es el umbral de la red?**<br /><br />**R**: Los detalles del mecanismo de limitación de clics están protegidos para evitar intentos de elusión.  Dicho esto, el umbral solo se alcanza si hay un volumen extremo de impresiones o clics, completamente alejado de un comportamiento humano normal. Revisar los volúmenes diarios de impresiones, clics e instalaciones le proporcionará una idea clara de si existe un problema de inundación provocado por uno o más editores. |
| --- |
| **P: ¿Cómo puede una red desbloquearse?**<br /><br />**R**: Una red puede evitar alcanzar el umbral si detiene las campañas y los editores que muestran actividad anómala. Una vez que se bloquea, la red debe esperar hasta que termine el ciclo de 24 horas para que los registros de clics puedan reanudarse. |
| **P: ¿El bloqueo afecta a los clientes de AppsFlyer que no tienen Protect360?**<br /><br />**R**: Sí, la limitación afectará independientemente de si el cliente posee Protect360. El mecanismo de limitación protege a todos los clientes del abuso de clics e impresiones. |
| **Q**: Esto no es fraude. La red trabaja con fuentes económicas y a veces su calidad es baja.<br /><br />**R**: El bajo rendimiento a una escala normal de fuentes no sospechosas no desencadena la limitación de clics. El algoritmo detecta un rendimiento que no podría ser humano. |
| **Q**: Esto nos impide escalar campañas y no queremos que se bloqueen estas impresiones o clics.<br /><br />**R**: El algoritmo de protección contra fraudes de AppsFlyer protege a los clientes de casos extremos y claros de inundación. No afecta la capacidad de crecimiento, ya que se dirige a impresiones o clics no humanos, donde la mayoría de los bloqueos solo causan problemas. Si tiene preocupaciones, por favor comuníquese con AppsFlyer para tratar sus problemas. |
| **Q**: Esto no es fraude. ¿Podría ser que AppsFlyer tenga dificultades para manejar el volumen de impresiones o clics?<br /><br />**R**: No tenemos problemas para gestionar el volumen. Damos soporte a algunos de los anunciantes de mayor escala del mundo y procesamos miles de millones de puntos de datos en tiempo real diariamente, incluyendo una gran cantidad de clics legítimos. Como parte de nuestro compromiso de apoyar un crecimiento a gran escala con datos ricos y precisos, actuamos en el mejor interés de nuestros clientes y bloqueamos casos claros de inundación de clics. |
| P: ¿Qué podemos hacer si prevemos un aumento considerable en el tráfico y el volumen de impresiones/clics, por ejemplo, debido a nuevas campañas? ¿Cómo podemos prevenir el bloqueo? ¿Qué se puede hacer para evitar que te bloqueen?<br /><br />R:**El algoritmo es dinámico y se actualiza de forma horaria para considerar las diferentes tendencias. Es suficientemente sofisticado para gestionar picos y no se activa con fluctuaciones normales de actividad, incluso con incrementos súbitos y significativos en el volumen. Dicho esto, los colaboradores pueden utilizar sus datos e informes de impresiones/clicks para identificar fuentes sospechosas y detener esas campañas.** |
| P: ¿Cómo podemos detectar tráfico problemático y mejorar el rendimiento de las campañas?<br /><br />R:**Los socios pueden utilizar sus datos e informes de impresiones y clics para identificar fuentes sospechosas y detener esas campañas. Adicionalmente, pueden ver datos de clics e impresiones bloqueados en el panel de control de Protect360/ProtectLITE en las columnas dedicadas, siempre que el anunciante les haya concedido el permiso necesario para ver los datos de fraude en el panel.** |

</Accordion>

<div id="click-signing" />

### Firma de clics

Las redes publicitarias pueden agregar firmas HMAC-SHA256 <Anchor target="_blank" href="/partners/es/docs/click-signing-for-ad-networks">a sus clics</Anchor>.

Estas firmas permiten a AppsFlyer validar los clics, asegurándose de que la información no haya sido manipulada por estafadores.

* Los clics validados se registran y se atribuyen a la red publicitaria.
* Los clics inválidos se rechazan y:
  * Se incluyen en los informes de Protect360 que están disponibles para la red publicitaria (excluyendo a los anunciantes).
  * No afectan la tasa de conversión ni el umbral de limitación de clics de la red publicitaria

<div data-zendesk-anchors="overview=visi%C3%B3n-general h_01HGSXTKYQB4Q1QQX4ZQS60AAJ=visi%C3%B3n-general h_01HGSXTKYQN42EEMPSZMWVAMWD=nota dashboard-view=vista-del-panel-de-control h_01HGSXTKYQPQP72R2VJB68ZDRZ=vista-del-panel-de-control rawdata-reports=informes-de-datos-sin-procesar h_01HGSXTKYQWRZECN905RGSEQ42=informes-de-datos-sin-procesar protect360-ad-network-reporting-api=api-de-informes-de-redes-publicitarias-de-protect360 h_01HGSXTKYQ9388SCQTT2MX59Q9=api-de-informes-de-redes-publicitarias-de-protect360 protect360-api-reports=informes-de-la-api-de-protect360 h_01HGSXTKYQXZN2DMNZ09HE7355=informes-de-la-api-de-protect360 procedure-for-ad-networks-to-get-protect360-reports-by-download=procedimiento-para-que-las-redes-publicitarias-obtengan-informes-de-protect360-a-trav%C3%A9s-de-descarga h_01HGSXTKYQ913MF0G38B23NYBG=procedimiento-para-que-las-redes-publicitarias-obtengan-informes-de-protect360-a-trav%C3%A9s-de-descarga curl-examples=ejemplos-de-curl h_01HGSXTKYQX3VN5NRMNQWW4AE4=ejemplos-de-curl h_01HGSXTKYQQBJTM4ZMMQZ0VZNH=installs-blocked_installs_report h_01HGSXTKYQ5KTCD7K63DSVS6E2=postattribution-installs-detection h_01HGSXTKYQ6MA96W8E6R2SXBS5=inapp-event-blocked_in_app_events_report h_01HGSXTKYQMMC0WNWP56Q9J0ZS=postattribution-inapp-events-fraud-fraud_post_inapps h_01HGSXTKYQEG0JXJHS7QBAEBCA=clicks-blockedclicks_report protect360-ad-network-api-reference-guide=gu%C3%ADa-de-referencia-de-la-api-de-la-red-publicitaria-protect360 h_01HGSXTKYQJRE1Y9C5RSCANWT2=gu%C3%ADa-de-referencia-de-la-api-de-la-red-publicitaria-protect360 h_01HGSXTKYQE24FAPYHHMFP0B3X=api-basics h_01HGSXTKYRFSZRPHNPDHNREDH2=api-parameters h_01HGSXTKYRGSQ230NVN06SP6DG=protect360-api-http-return-codes impression-and-click-capping=umbral-de-impresiones h_01HGSXTKYRN6TP3KDYX5YZJV7N=umbral-de-impresiones h_01HGSXTKYR8BK5A2J6TJECMKZA=faq click-signing=firma-de-clics h_01HGSXTKYR915V6E4NWGWR61PG=firma-de-clics" />
