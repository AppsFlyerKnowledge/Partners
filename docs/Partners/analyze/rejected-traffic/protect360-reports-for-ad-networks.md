---
title: Reportes de Protect360 para redes de publicidad
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2022-02-08T14:53:48Z'
  edited_at: '2026-08-12T12:27:38Z'
  id: 4420246395793
  locale: es
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/es/articles/4420246395793
---
> **A primera vista:** Las ad networks responsables de la adquisición de usuarios y del retargeting pueden recibir datos sobre clics e impresiones bloqueados.

<div id="protect360-reports-for-ad-networks" />

## Reportes de Protect360 para redes de publicidad

**Aviso**: Este artículo proporciona información sobre los reportes de Protect360 disponibles solo para ad networks. Para los datos que también están disponibles para los anunciantes, consulta <Anchor target="_blank" href="/partners/es/docs/protect360-for-integrated-partners">Protect360 para Partners integrados</Anchor>.

Las ad networks pueden recibir reportes a través de <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners">Data Locker for Partners</Anchor> con información valiosa sobre clics e impresiones que se bloquean por alguno de los siguientes motivos:

* Clics e impresiones bloqueados que se producen cuando las ad networks superan su límite de fraude. El reporte incluye el total de bloqueos, así como los bloqueos debidos al capping de clics e impresiones. <Anchor target="_blank" href="/partners/es/docs/protect360-for-integrated-partners#umbral-de-impresiones">Saber más sobre el capping</Anchor>
* Firmas de clic fallidas que se producen cuando no se puede validar un clic con el parámetro PID de la red y una firma de clic para validar los clics. <Anchor target="_blank" href="/partners/es/docs/click-signing-for-ad-networks">Saber más sobre la firma de clics</Anchor>

A continuación, las ad networks pueden ingerir estos datos a nivel de red con visibilidad entre clientes de sus clics e impresiones bloqueados y usarlos para protegerse contra el fraude.

<div id="report-considerations" />

### Consideraciones sobre el reporte

* Los datos llegan en formato CSV al bucket del partner de UA/retargeting.
* Contiene dimensiones y métricas relevantes para la ad network (es decir, depuradas de todas las dimensiones irrelevantes para la ad network).
* Disponible a través de <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners">Data Locker for Partners</Anchor>.
* Actualización de datos: <Anchor target="_blank" href="/marketers/es/docs/about-data-freshness-and-timezone-support#ad-revenue">A diario, lo que significa que los datos del Día 0 llegan el Día 1</Anchor>. Los datos se escriben diariamente a las 07:00 <Anchor target="_blank" href="/marketers/es/docs/about-data-freshness-and-timezone-support#daily">hora UTC</Anchor> en la h=23 de tu bucket de Data Locker.
* Aplicaciones incluidas: Un único reporte contiene los datos de todas las aplicaciones.

<div id="report-types" />

## Tipos de informes

<div id="blocked-clicks-and-impressions" />

<Accordion title="Clics e impresiones bloqueados">

Este reporte contiene datos de nivel agregado sobre clics e impresiones que se bloquean debido al capping o por cualquier otro motivo. 

<div id="report-structure-fieldsdimensions" />

#### Estructura del reporte: Campos/Dimensiones

| **Campo** | **Nota** |
| --- | --- |
| id\_aplicación | ID de aplicación en la plataforma AppsFlyer. |
| id\_sitio | ID que identifica al publisher que muestra el anuncio. |
| fecha | Fecha de bloqueo |
| agencia | <ul><li>Agencia que trajo el tráfico a través de esta ad network.</li><li>Devuelve null si no hay ninguna agencia implicada.</li></ul> |

<div id="report-structure-metrics" />

#### Estructura del reporte: Métricas

| **Campo** | **Nota** |
| --- | --- |
| numero\_de\_clics\_bloqueados | Cantidad total de clics bloqueados de la red |
| numero\_de\_impresiones\_bloqueadas | Cantidad total de impresiones bloqueadas de la red |
| numero\_de\_clics\_limitados | El número de clics limitados de la red (de los clics bloqueados totales) |
| numero\_de\_impresiones\_limitadas | El número de impresiones limitadas de la red (de las impresiones totales bloqueadas) |

</Accordion>

<div id="failed-click-signatures" />

<Accordion title="Firmas de clic fallidas">

Este reporte contiene datos a nivel de usuario sobre firmas de clic fallidas. Es decir, cuando las ad network usan el <Anchor target="_blank" href="/partners/es/docs/click-signing-for-ad-networks">método de firma de clics de AppsFlyer</Anchor>, el reporte contiene clics de URL con el PID de la red que no tienen firmas de clic validadas, ya sea porque la firma no es válida o ha caducado, o porque el clic no está firmado en absoluto. Los fallos en la firma de clics pueden producirse cuando hay errores técnicos en la implementación de las firmas de clic por parte de la ad network, o cuando otra party envía clics en nombre de la red (con su PID).

<div id="report-structure-fieldsdimensions-1" />

#### Estructura del reporte: Campos/Dimensiones

| **Campo** | **Nota** |
| --- | --- |
| event\_time |  |
| original\_url |  |
| motivo\_del\_error\_de\_firma | Por ejemplo,<ul><li>Firma inválida</li><li>Ausencia de firma</li><li>Firma caducada</li><li>Clave secreta caducada</li></ul> |
| el\_bloqueo\_esta\_habilitado | Hace referencia al modo de configuración de la <Anchor target="_blank" href="/partners/es/docs/click-signing-for-ad-networks">API de firma de clics</Anchor>:<ul><li>TRUE para habilitado.</li><li>FALSE para solo reporte.</li><li>No se incluye en el reporte si está deshabilitado.</li></ul> |

</Accordion>

<div data-zendesk-anchors="protect360-reports-for-ad-networks=reportes-de-protect360-para-redes-de-publicidad report-considerations=consideraciones-sobre-el-reporte report-types=tipos-de-informes report-structure-fieldsdimensions=estructura-del-reporte-camposdimensiones report-structure-metrics=estructura-del-reporte-m%C3%A9tricas report-structure-fieldsdimensions::44afb679=estructura-del-reporte-camposdimensiones-1" />
