---
title: ROI360—opciones de reportes de costos para agencias
metadata:
  keywords:
    - clicks
    - cost
    - Agencies
    - Partners
    - ad spend
    - Xpend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Agencies
    - ROI360
  created_at: '2020-10-04T15:07:34Z'
  edited_at: '2026-08-12T12:28:03Z'
  id: 360014054998
  locale: es
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/es/articles/360014054998
---
> **De un vistazo:** reporta datos de costos mediante la API de costos (requiere una suscripción a la solución premium ROI360) y el costo por clic.

<div id="cost-reporting-for-agencies" />

## Reporte de costos para agencias

Los anunciantes utilizan AppsFlyer como fuente de confianza para el ROI, la facturación y para tomar decisiones de asignación del presupuesto de marketing. Para ello, necesitan tener toda la información de costos en una sola plataforma. ROI360, una solución premium de AppsFlyer, permite a anunciantes y agencias recopilar datos de costos mediante la API, y ponerlos a disposición para su consulta mediante los dashboards y las herramientas de reportes de AppsFlyer. 

Los datos de costos se pueden agregar mediante cualquiera de los siguientes métodos: 

* **API de costos**: AppsFlyer extrae datos de los Partners
* **Costo por clic:** Las redes reportan el costo cada vez que se hace clic en un enlace de atribución

La siguiente tabla enumera las funciones de agregación de costos disponibles con y sin ROI360.

| Opción | Requiere suscripción a ROI360 | Descripción |
| --- | --- | --- |
| <Anchor target="_blank" href="/marketers/es/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">Cost API</Anchor> | Sí | <ul><li>Las Agencias usan sus credenciales de la API de ad network para conectarse y habilitar la API de costos en el Dashboard de AppsFlyer.</li><li>Los datos de costos se reflejan de acuerdo con la <Anchor target="_blank" href="/marketers/es/docs/view-agency-data">transparencia de la agencia</Anchor>. (Para los SRN, esto incluye clics e impresiones.)</li><li>Soporta todos los modelos de costos</li><li>Preciso</li><li>Frecuencia de actualización de datos: 6 veces al día, cada cuatro horas.</li></ul> |
| <Anchor target="_blank" href="/partners/es/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Costo por clic</Anchor><br /><br />(en el enlace de atribución) | No | <ul><li>Las Agencias envían su CPI, valor y moneda de costo en el enlace de atribución. AppsFlyer agrega el Costo.</li><li>Actualización de los datos: casi en tiempo real</li></ul>**Limitaciones:**<ul><li>Limitado al modelo de costos CPI</li><li>Si se envían datos incorrectos en el enlace, no se pueden cambiar retroactivamente.</li><li>El costo reportado por clic no está disponible en el Dashboard de SKAdNework.</li><li>El costo por clic es menos preciso si el anunciante utiliza SKAdNetwork.</li></ul> |

<div data-zendesk-anchors="cost-reporting-for-agencies=reporte-de-costos-para-agencias" />
