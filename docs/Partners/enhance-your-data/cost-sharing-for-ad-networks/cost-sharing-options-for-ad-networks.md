---
title: Opciones de costos compartidos para redes publicitarias
metadata:
  keywords:
    - clicks
    - Partner
    - cost
    - Ad Networks
    - Partners
    - ad spend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2020-09-07T13:50:24Z'
  edited_at: '2026-08-12T12:27:58Z'
  id: 360012893658
  locale: es
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/es/articles/360012893658
---
> **En resumen:** Compara los métodos de costos compartidos disponibles para los partners de la red publicitaria de AppsFlyer.

<div id="sharing-cost-with-appsflyer-and-advertisers" />

## Costo compartido con AppsFlyer y anunciantes

Los anunciantes utilizan AppsFlyer como fuente de confianza para el ROI, la facturación y para tomar decisiones de asignación del presupuesto de marketing. Para que las redes sean visibles, es imprescindible compartir datos de costos con AppsFlyer. Las redes sin datos de costo aparecen en la parte inferior de la lista del dashboard de AppsFlyer.

Las redes publicitarias comparten costos con AppsFlyer utilizando cualquiera de los siguientes: 

* **InCost API**: Envía datos a AppsFlyer
* **Cost API**: AppsFlyer extrae datos
* **Importación de costos**: Los archivos de datos de costos se cargan/envían a AppsFlyer
* **Costo por clic:** Las redes reportan el costo cada vez que se hace clic en un enlace de atribución

<div id="cost-badge-for-ad-networks" />

### Indicador de costo para redes publicitarias

<Image align="center" alt="CostBadge.jpg" src="https://files.readme.io/6b660b68b932802f7982a3beb3a155ecc350de1b4cb3baede6e84ef0d704388c-360011247338.jpg" />

* Se muestra un indicador de costo en la <Anchor target="_blank" href="/marketers/es/docs/partner-integrations#partner-details-and-performance">página de detalles del partner</Anchor> que destaca a los partners que utilizan InCost o Cost API.
* Esto certifica que es un partner con capacidad de costos.
* Los análisis internos y las extensas encuestas a los usuarios muestran que los anunciantes siempre están buscando nuevos partners. Aquellos con un indicador de costo tienen más probabilidades de destacarse, ya que los anunciantes quieren comprender su desempeño de marketing basándose en el análisis del ROI.

<div id="reporting-cost-options-available-to-ad-networks" />

### Opciones de reporte de costos disponibles para las redes publicitarias

| Opción | Calificar para un indicador de costo | Características de la opción |
| --- | --- | --- |
| <Anchor target="_blank" href="/partners/es/docs/incost-api-for-ad-networks">API InCost</Anchor> | ✓ | La red publicitaria tiene plena propiedad sobre cuándo configurar los reportes InCost.<br /><br />InCost tiene las siguientes características:<ul><li>Soporta todos los modelos de costos</li><li>Preciso y confiable</li><li>Completamente automatizado</li><li>Controles de partners de la red publicitaria:<ul><li>Esquema de upload de datos</li><li>Tasa de cuándo se hace el upload (actualización de los datos)</li></ul></li><li>El anunciante concede permiso en el dashboard de AppsFlyer al partner para cargar datos de costos</li></ul>**Limitación**:<br /><br />Las cuentas de agencia de AppsFlyer no son compatibles. |
| Cost API | ✓ | <ul><li>Soporta todos los modelos de costos</li><li>Preciso</li><li>El partner conserva cierto control sobre sus datos de costos en AppsFlyer</li><li>Admite costos para cuentas de agencia en AppsFlyer</li><li>Los anunciantes proporcionan sus credenciales de partner en el dashboard de AppsFlyer</li><li>Frecuencia de actualización de datos: 6 veces al día, cada cuatro horas.</li></ul>**Limitación**:<br /><br />La integración está sujeta a las prioridades de AppsFlyer. |
| <Anchor target="_blank" href="/partners/es/docs/cost-import-for-ad-networks">Importación de costos</Anchor><br /><br />(Subir archivo) | No | <ul><li>El partner de la red publicitaria:<ul><li>Carga datos manualmente si no tiene recursos de ingeniería para automatizar</li><li>Controla cuándo cargar datos</li><li>Mantiene cierto control sobre sus datos de costos en AppsFlyer</li><li>La integración es por aplicación. El anunciante proporciona permiso en el dashboard de AppsFlyer al partner para cargar datos de costos.</li><li>La coincidencia con los datos de atribución se basa en el nombre de la campaña (no en el ID de la campaña).</li></ul></li></ul>**Limitación**:<ul><li>Las cuentas de agencia de AppsFlyer no son compatibles</li><li>Riesgo de fallo si la carga se automatiza por correo electrónico</li></ul> |
| <Anchor target="_blank" href="/partners/es/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Costo por clic</Anchor><br /><br />(en el enlace de atribución) | No | <ul><li>Solución rápida para campañas de CPI</li><li>Casi en tiempo real</li><li>El costo por clic puede ser menos preciso si el anunciante utiliza SKAdNetwork</li></ul>**Limitación**:<ul><li>Limitado al modelo de costos CPI</li><li>Si se envían datos incorrectos en el enlace, no se pueden cambiar retroactivamente</li><li>Retargeting no compatible</li><li>El costo reportado por clic se muestra en el dashboard de SKAdNework cuando esté disponible</li></ul> |

<div data-zendesk-anchors="sharing-cost-with-appsflyer-and-advertisers=costo-compartido-con-appsflyer-y-anunciantes h_01HN0A1ER3MNZM508ZCG9KP26P=costo-compartido-con-appsflyer-y-anunciantes cost-badge-for-ad-networks=indicador-de-costo-para-redes-publicitarias h_01HN0A1ER4K1V4479W5SXCEC30=indicador-de-costo-para-redes-publicitarias reporting-cost-options-available-to-ad-networks=opciones-de-reporte-de-costos-disponibles-para-las-redes-publicitarias h_01HN0A1ER4Y128ZHJERXS6A8ET=opciones-de-reporte-de-costos-disponibles-para-las-redes-publicitarias" />
