---
title: Data Locker para partners
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Data Locker
    - Agencies
    - Ad Networks
  created_at: '2021-05-28T15:37:04Z'
  edited_at: '2026-08-12T12:27:22Z'
  id: 360020818517
  locale: es
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/es/articles/360020818517
---
> **En resumen:** Data Locker para partners (ad networks y agencias) entrega los datos de la aplicación al almacenamiento del partner en AWS, GCS o BigQuery.

![6133DataLockerForPartners.png](https://files.readme.io/f6cad12250fe07cf2b0a12b64eeaa597c83527b4b4e09aea11cc2a52ab53339b-4637680455313.png)

<div id="data-locker-for-partners" />

## Data Locker para partners

Data Locker para partners entrega los datos de la aplicación al almacenamiento en la nube. Los anunciantes establecen los permisos que permiten que AppsFlyer comparta los datos seleccionados con un partner determinado.

<div id="data-locker-features" />

<Accordion title="Características de Data Locker">

| Característica | Descripción |
| --- | --- |
| Opciones de almacenamiento (nube) | Almacenamiento (bucket) de tu propiedad en:<ul><li>AWS</li><li>GCS</li><li>Yandex</li><li>BigQuery</li></ul><Anchor target="_blank" href="/marketers/es/docs/data-locker-for-marketers#storage-options">Sobre las opciones de almacenamiento</Anchor> |
| Soporte de múltiples aplicaciones | Soporta los datos de las aplicaciones que tengas integradas. El anunciante debe dar permiso por cada reporte para que puedas obtener los datos. |
| Opciones de formato de datos | <ul><li>Para el almacenamiento en un bucket en la nube:<ul><li>CSV</li><li>PARQUET</li><li>Adobe</li></ul></li><li>Almacén de datos</li></ul> |
| Actualización de los datos | La actualización depende del tipo de reporte:<ul><li>**Por hora:** Datos generados continuamente</li><li>**A diario:** Algunos reportes se preparan diariamente y están listos al día siguiente</li></ul> |

</Accordion>

<div id="reports-available-for-partners" />

<Accordion title="Reportes disponibles para partners">

Los reportes disponibles y los permisos necesarios para obtener los reportes varían según el tipo de partner. Sin embargo, el mecanismo de Data Locker, las opciones de almacenamiento y los ajustes necesarios son los mismos independientemente del tipo de partner. Consulta los artículos por tipo de partner que se indican a continuación:

* <Anchor target="_blank" href="/partners/es/docs/data-locker-reports-available-for-ad-networks">Redes publicitarias</Anchor>
* <Anchor target="_blank" href="/partners/es/docs/data-locker-reports-for-agencies">Agencias</Anchor>
* <Anchor target="_blank" href="/partners/es/docs/data-locker-reports-for-api-partners">Partners de marketing</Anchor>

</Accordion>

<div id="data-storage-architecture" />

## Arquitectura de almacenamiento de datos

<div id="overview" />

<Accordion title="Descripción general">

Los datos se escriben en la opción de almacenamiento seleccionada. Puedes alternar entre las opciones en cualquier momento. El cambio entrará en vigor en el transcurso de unas horas.

Los datos del almacenamiento en el bucket en la nube están organizados en una estructura jerárquica de carpetas, según el tipo de reporte, la fecha y la hora. La siguiente figura contiene un ejemplo de esta estructura:

![DLFolderOVerview.png](https://files.readme.io/78f360ec1df72253e5b2cd725f3eecf4e17548a7f06b544a94a75a2c319d77a0-18107910420369.png)

Los datos de un reporte determinado están incluidos en las carpetas de horas (h) asociadas con ese reporte.

* La cantidad de carpetas de horas depende de si el reporte se transmite por hora o por día.
* Los datos se proporcionan en archivos comprimidos Snappy o GZIP, o en archivos sin comprimir, que tienen formato Parquet o CSV.
* Los archivos de datos constan de columnas (fields).
* La estructura de columnas se define por tipo de reporte.

</Accordion>

<div id="folder-structure" />

<Accordion title="Estructura de carpetas">

| Carpeta | Descripción |
| --- | --- |
| data-locker-hourly | ![DLHourly.png](https://files.readme.io/c257b82d22622d97808a6c23603ac4eee9f2ab091bcb68a33637ac4fb749fdff-18107874510353.png)<ul><li>La carpeta de nivel superior del bucket depende del proveedor del almacenamiento.</li><li>La carpeta *data-locker-hourly* contiene los temas de los reportes.</li></ul>**Ejemplos de estructura de carpetas en función del propietario del bucket y el proveedor de la nube**:<ul><li>**Tu bucket de AWS**: *&lt;af-datalocker-your bucket prefix>/&lt;generated-home-folder>&lt;subscription-id>*</li><li>**Tu bucket de GCS:** &lt;your bucket name>/&lt;generated-home-folder>/&lt;subscription-id></li></ul> |
| t (topic) | El tipo de reporte se relaciona con el asunto del reporte. |
| dt (date) | Esta es la fecha de los datos. En la mayoría de los casos, esto significa la fecha en que ocurrió el evento. |
| h (hour) | Las carpetas h se refieren al momento en que AppsFlyer recibió los datos. Por ejemplo, los eventos de instalación recibidos entre las 14:00 y 15:00 UTC se transmiten al archivo h=14. ¡Atención! ¡Nota! Hay una demora, de aproximadamente 6 horas, entre el momento en que los datos llegan a AppsFlyer hasta que la carpeta h se transmite a Data Locker. Por ejemplo, la carpeta h=14 se transmite seis horas más tarde a las 23:00 UTC.<br /><br />**Características de la carpeta**:<ul><li>Hay carpetas de 24 h numeradas del 0 al 23. Por ejemplo, h=0, h=1, etc.</li><li>Además, la carpeta “late” (tarde) contiene eventos del día anterior que llegaron después de la medianoche (es decir que llegaron entre las 00:00–02:00 UTC del día siguiente). Por ejemplo, un usuario instala una aplicación el lunes a las 08:00 y el evento llega el martes a la 01:00, el evento se registra en la carpeta “late” del lunes.</li><li>Los datos que llegan después de las 02:00 se registran en la carpeta de la fecha y hora de llegada real.</li><li>Debes utilizar los datos de la carpeta “late”. Estos datos no se encuentran en ninguna otra carpeta.</li><li>\_temporary folder: En algunos casos, generamos una carpeta temporal dentro de una carpeta h. Desestimar carpetas y subcarpetas temporales. Ejemplo: /t=impressions/dt=2021-04-11/h=18/**\_temporary**.</li></ul> |
| Datos unificados | Los datos de todas las aplicaciones se proporcionan en archivos de datos unificados. Al cargar los datos, utiliza el campo app\_id a nivel de fila para distinguir entre aplicaciones.<br /><br />**Ejemplos de archivos de datos que están en la carpeta h=2**<br /><br />![UnifiedByApp.png](https://files.readme.io/dbc39c2ce99c1ff607fd553b9c9034e55728c102f31fd18a501cc00910267b28-18107874522513.png)<ul><li>En tu proceso de carga de datos, asegúrate de que:<ul><li>Los datos se procesan solo después de que se configura el indicador \_SUCCESS.</li><li>Cargas todos los archivos que tienen una *extensión .gz.*</li></ul></li></ul> |
| Indicador de finalización | El indicador de último archivo (finalización) se establece cuando se han escrito todos los datos de una carpeta h determinada.<ul><li>No leas datos en una carpeta antes de verificar que tiene el indicador \_SUCCESS.</li><li>El indicador \_SUCCESS se establece incluso en los casos en los que no se escriben datos en la carpeta. Significa que la carpeta está vacía.</li></ul> |
| Compresión | Los archivos se comprimen con gz. Después de descomprimirlos:<ul><li>Los archivos no tienen extensión.</li><li>Cada archivo tiene una fila de encabezado que contiene los nombres de las columnas (campo).</li></ul> |
| Secuencia de columnas | La secuencia de campos en los reportes es siempre la misma. Los nuevos campos se agregan a la derecha de los campos existentes.<br /><br />Las definiciones de las columnas (campos) se definen por reporte. Consulta el artículo del reporte correspondiente para obtener la descripción. |
| Consideraciones del relleno de campos | **Campos en blanco o vacíos:** Algunos campos se completan con *null* o están vacíos. Esto significa que en el contexto de un reporte determinado no hay datos para reportar. Normalmente, *null* (nulo) significa que este campo no se completa en el contexto de un reporte y tipo de aplicación determinados. Blank "" (en blanco) significa que el campo es relevante en su contexto, pero no se encontraron datos para completarlo.<br /><br />**Zona horaria y divisa**:<br /><br />Los ajustes de zona horaria y divisa específicos de la aplicación no se tienen en cuenta para los datos proporcionados por Data Locker. Así pues:<ul><li>**Zona horaria**: La fecha y la hora están en UTC.</li><li>**Moneda**: El campo event\_revenue\_usd está en USD.</li></ul>**Valores con comas**: Estas comas están contenidas entre comillas dobles "", por ejemplo, `` `"iPhone6,1"` ``. |

</Accordion>

<div id="data-files" />

<Accordion title="Archivos de datos">

Los archivos de datos dependen del tipo de segregación.

<table><thead><tr><th>Contenido</th><th colspan="2">Detalles</th></tr></thead><tbody><tr><td>Indicador de finalización</td><td colspan="2"><p>El indicador de último archivo (finalización) se establece cuando se han escrito todos los datos de una carpeta h determinada. </p><ul><li><p>No leas datos en una carpeta antes de verificar que tiene el indicador _SUCCESS.</p></li><li><p>El indicador _SUCCESS se configura incluso en los casos en que no hay datos para escribir en una carpeta determinada y la carpeta está vacía. </p></li><li>¡Atención! ¡Nota! En la opción de segregación por aplicación, el indicador se configura en la carpeta h y no en las carpetas individuales de las aplicaciones. Consulta las figuras de la sección anterior. </li></ul></td></tr><tr><td>Tipos de archivo</td><td colspan="2"><ul><li>Los datos se proporcionan en archivos comprimidos Snappy o GZIP, o en archivos sin comprimir, que tienen formato Parquet o CSV.</li><li>Después de descomprimir, los archivos de datos están en formato Parquet o CSV de acuerdo con tu configuración.</li></ul></td></tr><tr><td>Secuencia de columnas (archivos CSV) </td><td colspan="2"><p>En el caso de los archivos CSV, la secuencia de campos en los reportes es siempre la misma. Cuando agregamos campos nuevos, estos se agregan a la derecha de los campos existentes. </p><p>En este sentido: </p><ul><li>La estructura de columnas de los reportes del viaje del usuario es idéntica. Esto significa que puedes tener procedimientos de carga de datos similares para diferentes tipos de reportes. Selecciona los campos contenidos en los reportes. El significado del campo se detalla en el <a href="/marketers/es/docs/raw-data-field-dictionary" target="_blank">diccionario de raw data</a>. </li><li>Los reportes que tienen una notación FF en la sección de disponibilidad del reporte no se adhieren a la estructura de columnas común. </li></ul></td></tr><tr><td>Consideraciones del relleno de campos</td><td colspan="2"><p><strong>Campos en blanco o vacíos:</strong> Algunos campos se completan con <em>null</em> o están vacíos. Esto significa que en el contexto de un reporte determinado no hay datos para reportar. Normalmente, <em>null</em> (nulo) significa que este campo no se completa en el contexto de un reporte y tipo de aplicación determinados. Blank "" (en blanco) significa que el campo es relevante en su contexto, pero no se encontraron datos para completarlo. </p><p>Si la fuente de medios está restringida, el contenido de los campos restringidos se establece en null. </p><p>En general, se considera null y blank como un único producto; no hay datos disponibles. </p><p><strong>Zona horaria y moneda</strong></p><p>La configuración de la zona horaria y divisa específicas de la aplicación no afecta los datos en Data Locker. Aplican las siguientes condiciones: </p><ul><li> <strong>Zona horaria</strong>: La fecha y la hora están en UTC.</li><li> <strong>Moneda</strong>: El campo event_revenue_usd está en USD.</li></ul><p><strong>Valores con comas</strong>: Estas comas están contenidas entre comillas dobles "", por ejemplo, <code>`"iPhone6,1"`</code>.</p></td></tr></tbody></table>

</Accordion>

<div id="storage-options" />

<Accordion title="Opciones de almacenamiento">

* Los datos se escriben en un propietario de almacenamiento de tu elección de la siguiente manera: AWS, GCS y BigQuery.
* Puedes cambiar la selección del almacenamiento en cualquier momento.
* Si cambias el almacenamiento, ocurre lo siguiente:
  * Comenzamos a escribir en el almacenamiento recién seleccionado en una hora.
  * Seguimos escribiendo en el almacenamiento existente durante un período de transición de 7 días. El tiempo de vencimiento del período de transición se muestra en la interfaz de usuario. Usa el período de transición para actualizar tus procesos de carga de datos.
  * **Cambiando buckets**: Si cambias el almacenamiento, los datos se envían a ambos durante un período de transición de 7 días, lo que te permite alinear tu proceso de consumo de datos.

|  | Almacenamiento propio del partner (GCS, AWS, BigQuery) |
| --- | --- |
| Nombre del bucket | <ul><li>GCS: Sin restricción</li><li>AWS: Configurado por ti. Debe tener el prefijo af-.</li></ul>Ejemplo: `af-datalocker-your-bucket-name` |
| Propietario de almacenamiento | Fuente de medios |
| Plataforma del almacenamiento | AWS, GCS, Yandex, BigQuery |
| Credenciales para que accedas a los datos | AppsFlyer no las conoce. Usa las credenciales proporcionadas por el proveedor de almacenamiento. |
| Retención de datos | Controlada por ti |
| Seguridad | Tú controlas el almacenamiento.<ul><li>**AWS**: AppsFlyer requiere permiso de GetObject, ListBucket, DeleteObject, PutObject para el bucket. El uso del bucket debe ser exclusivo de AppsFlyer. No lo uses para otros fines.</li><li><Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor></li></ul> |

<div id="notice-to-security-officers" />

#### **Aviso a los responsables de seguridad**

Consideración:

* El bucket o destino es para uso exclusivo de AppsFlyer. No debe haber ninguna otra entidad que escriba en el bucket.
* Puedes eliminar datos del bucket 25 horas después de que escribamos los datos.
* Los datos escritos en el destino son una copia de los datos que ya están en nuestros servidores. Los datos continúan estando en nuestros servidores de acuerdo con nuestra política de retención.
* Por razones técnicas, a veces eliminamos y reescribimos los datos. Por esta razón, requerimos permisos de eliminación y listado. Ni listar ni eliminar son un riesgo de seguridad para ti. En el caso de la lista, somos la única entidad que escribe en el bucket. En el caso de eliminar, podemos regenerar los datos.

</Accordion>

<div id="multipleconnection-principles-more-than-one-destination" />

<Accordion title="Principios de conexión múltiple (más de un destino)">

En Data Locker puedes enviar algunos o todos tus datos a más de un destino (definido en la configuración de la conexión). Por ejemplo, puedes enviar los datos de la aplicación A a AWS y los de la aplicación B a GCS.

Cada conexión consiste en un conjunto completo de configuraciones de Data Locker, incluido un destino. Las configuraciones de las conexiones son independientes entre sí.

Al administrar tus conexiones, ten en cuenta lo siguiente:

* En la configuración de Data Locker, las conexiones se muestran en pestañas. Cada conexión tiene su propia pestaña de configuración desde la que puedes administrar la conexión. La pestaña predeterminada es "Data Locker".
* Para agregar una conexión nueva:
  1. Haz clic en **Agregar conexión**.
  2. Proporciona un nombre para la conexión y elige el tipo de almacenamiento.
  3. Haz clic en **Guardar**.  
     Una vez guardada, la conexión se muestra junto a la pestaña predeterminada "Data Locker". El icono de cada pestaña representa el tipo de almacenamiento.
* Para ver los detalles de la conexión, duplicar una conexión o eliminar una conexión, haz clic en : (opciones).

</Accordion>

<div id="procedures" />

## Procedimientos

<div id="set-up-data-locker" />

<Accordion title="Configurar Data Locker">

Usa este procedimiento para configurar Data Locker. Los cambios en la configuración tienen efecto en 3 horas.

**Requisito previo:**

Completa uno o más de los siguientes procedimientos de almacenamiento:

* Bucket de <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>
* Bucket de <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>
* [Beta] Bucket de <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor>
* Almacén de datos de <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor>

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Para configurar Data Locker:**

1. Inicia sesión en tu <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">dashboard de partner de AppsFlyer.</Anchor>
2. Ve a:
   * **Anunciantes**: En AppsFlyer, desde la barra lateral, abre **Exportar** > **Data Locker**.
   * **Partners de marketing**: Haz clic en el **menú de la cuenta** > **Data Locker**.
3. Sigue los pasos 3-16 de las <Anchor target="_blank" href="/marketers/es/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">Instrucciones de configuración de Data Locker</Anchor>.

</Accordion>

<div id="additional-information" />

## Información adicional

<div id="traits-and-limitations" />

<Accordion title="Características y limitaciones">

| **Caducado** | Observaciones |
| --- | --- |
| Zona horaria específica de la aplicación | No corresponde |
| Moneda específica de la aplicación | No compatible |
| Limitaciones de tamaño | No aplicable |
| Actualización de los datos | Los datos se actualizan de acuerdo con la actualización específica de los datos del reporte que se detalla en este artículo. |
| Datos históricos | No compatible |
| Acceso de miembros del equipo | Los miembros del equipo no pueden configurar Data Locker. |

</Accordion>

<div id="troubleshooting" />

<Accordion title="Resolución de problemas">

<Anchor target="_blank" href="/marketers/es/docs/data-locker-for-marketers#troubleshooting">Usa esta guía de resolución de problemas</Anchor>.

</Accordion>

<div data-zendesk-anchors="data-locker-for-partners=data-locker-para-partners h_01H8Y0DGS4Y2N99YNYEEJA6RSF=data-locker-para-partners h_01H8Y0DGS4EM06PYNS1DRMZM6Y=data-locker-features h_01H8Y0DGS4A0MYGVZ9XQ49EBT2=reports-available-for-partners data-storage-architecture=arquitectura-de-almacenamiento-de-datos h_01H8Y0DGS4WTAJV7QE2DX3VGBP=arquitectura-de-almacenamiento-de-datos h_01H8Y0DGS4BQHBKNHZ4CD9ZMT4=overview h_01H8Y0DGS43JAREX23YX1F125K=folder-structure h_01H8Y0DGS524WNXY63351XGJKA=data-files h_01H8Y0DGS5MV6J1MMJJS8G4HC4=storage-options notice-to-security-officers=aviso-a-los-responsables-de-seguridad h_01H8Y0DGS5R4QX01WBK2S33QP5=aviso-a-los-responsables-de-seguridad h_01H8Y0DGS56GN6TVTSEV713DWQ=multipleconnection-principles-more-than-one-destination procedures=procedimientos h_01H8Y0DGS5588GQPZT7MQ686T3=procedimientos h_01H8Y0DGS57YK2PZ9ENZ80EWRJ=set-up-data-locker additional-information=informaci%C3%B3n-adicional h_01H8Y0DGS5SYZRWFAXDSKE3YHX=informaci%C3%B3n-adicional h_01H8Y0DGS540HK8MSCFYT9Q1RM=traits-and-limitations h_01H8Y0DGS55PJ7HV1PQ72XDDAB=troubleshooting" />
