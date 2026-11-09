---
title: Acerca de las cuentas de agencia
metadata:
  keywords:
    - In-App Events
    - Agency Account
    - ROI
    - Agency
    - FMP
    - Advertisers
    - Agencies
    - Listed Agency
    - all installs
    - all launches
    - Partners
    - agency sign up
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2013-12-08T10:02:42Z'
  edited_at: '2026-08-12T12:29:35Z'
  id: 207034106
  locale: es
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/es/articles/207034106
---
> **De un vistazo:** Aprovecha al máximo tu cuenta de AppsFlyer Agency con una configuración avanzada.

<div id="about-agency-accounts" />

## Acerca de las cuentas de agencia

Los equipos de agencias utilizan las cuentas de agencia para medir las campañas de marketing de aplicaciones que realiza la agencia en nombre de los clientes comercializadores (propietarios de aplicaciones).

* Se encuentran disponibles métricas clave previas y posteriores a la instalación para asegurar que las agencias ofrezcan un rendimiento óptimo a lo largo de su cartera de clientes.
* Los paneles de cuentas de agencia ofrecen capacidades y contenido similar a los de los paneles de marketing. Esto incluye los siguientes paneles:
  * Visión general del valor del ciclo de vida
  * Eventos dentro de la aplicación
  * Redireccionamiento
* Los KPI disponibles incluyen impresiones, clics, instalaciones, fidelidad del usuario, costo y ROI. Acerca del <Anchor target="_blank" href="/marketers/es/docs/getting-started-with-appsflyer-dashboards">panel de control.</Anchor>

<div id="agency-access-to-marketer-data" />

### Acceso de la agencia a los datos de los comercializadores

Las agencias siempre tienen acceso a los datos de tráfico atribuidos a la agencia. Los vendedores pueden <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">dar a las agencias acceso a</Anchor> datos adicionales, como datos agregados orgánicos. Consulta <Anchor target="_blank" href="/marketers/es/docs/manage-data-access-permissions">el acceso a los datos por diferentes tipos de usuarios.</Anchor>

<div id="agency-access-to-ad-network-integrations" />

### Acceso de la agencia a las integraciones de redes publicitarias

Para habilitar el acceso a las integraciones de redes publicitarias y que se midan tus campañas, tu agencia debe ser previamente aprobada por la red publicitaria. Esto se logra al incluir tu ID de agencia (af\_prt) en la lista de agencias autorizadas de la red publicitaria. Contacta al socio para asegurarte de que tu agencia esté incluida. [Consulta aquí](/docs/about-agency-accounts#parámetro-af_prt) cómo encontrar el ID de tu agencia.

<div id="note" />

> 📘 **Nota:**
>
> * Se aplica también a parámetros af\_prt vacíos en enlaces de atribución
> * No se aplica a agencias que trabajan con <Anchor target="_blank" href="/marketers/es/docs/self-reporting-networks-srns">SRNs</Anchor>

<div id="agency-transparency" />

### Transparencia de la agencia

El tráfico de la agencia está configurado por defecto para ser transparente. <Anchor target="_blank" href="/partners/es/docs/getting-started-agency-onboarding#transparency">Más información</Anchor>

<div id="comparing-different-types-of-accounts" />

## Comparación de diferentes tipos de cuentas

<div id="agency-versus-marketer-accounts" />

<Accordion title="Cuentas de agencias versus cuentas de comercializadores">

* **Las cuentas de mercadotecnia** están orientadas a servir a la aplicación y al propietario de los datos. Los vendedores añaden aplicaciones a sus cuentas y establecen los permisos de acceso a los datos.
* **Las cuentas de agencia** están diseñadas específicamente para equipos de agencias. Incluyen herramientas para una eficiente medición y análisis de campañas de marketing en toda su cartera de clientes.

Las estructuras de cuentas permiten compartir conocimientos entre equipos de agencias globales y facilitan la medición del ROI a nivel de grupo, cálculos, reportes y optimización.

<div id="differences-between-marketer-and-agency-accounts" />

#### Diferencias entre cuentas de comercializadores y de agencias

|  | Comercializador | **Agencia** |
| --- | --- | --- |
| Implementación a nivel de código | Sí | No; solo promoción de la aplicación |
| Configuraciones a nivel de cuenta | Miembros del equipo, permisos de los miembros del equipo, configuraciones, preferencias de pago | Miembros del equipo de la agencia y sus permisos |
| Configuraciones a nivel de aplicación | Ventana de reatribución, configuración de OneLink, zona horaria, moneda | Todos los demás ajustes siguen los establecidos por el comercializador |
| Configuración a nivel de socio integrado | <ul><li>Permisos de la agencia</li><li>Todas las configuraciones basadas en redes publicitarias, excepto SRN</li><li>Configuraciones de SRN</li><li>Gestión de enlaces</li></ul> | <ul><li>Todas las configuraciones excepto SRN</li><li>Algunas configuraciones de SRN que requieren mínima intervención del comercializador:</li></ul><ul><li>Google Doubleclick<ul><li>Snapchat</li><li>Tencent</li></ul></li></ul>Otros SRN deben ser configurados por el comercializador para que la agencia pueda utilizarlos<ul><li>Gestión de enlaces (utilizando plantillas definidas por los marketers)</li></ul> |
| Funcionalidades adicionales | Sí (algunos, si están en el plan de suscripción) | Según la suscripción del comercializador y los <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">permisos</Anchor> otorgados a la agencia (ver tabla abajo) |

<div id="features-available-to-agencies" />

### Funciones disponibles para las agencias

| Disponible por defecto | No disponible | Requiere permiso del comercializador |
| --- | --- | --- |
| <ul><li>Panel de vista general del valor de vida útil</li><li>Panel de eventos in-app</li><li>Panel de retargeting</li><li>Integraciones activas</li><li><Anchor target="_blank" href="/partners/es/docs/getting-started-agency-onboarding#fuente-única-de-verdad-ssot-para-agencias">Panel SSOT</Anchor>\*\*</li></ul>\*\* Disponible solo después de que el comercializador haya habilitado esta opción | <ul><li>Panel de actividades</li><li>Panel personalizado</li><li>Analítica basada en personas</li><li>Audiencias</li><li>Informe de pivote</li><li>API push</li><li>Casillero de datos</li></ul>*Solo los informes de cohorte están disponibles con permiso del comercializador | <ul><li>Informe de retención</li><li>Informe del panel de cohorte</li><li><Anchor target="_blank" href="/partners/es/docs/data-locker-reports-for-agencies">Informe de cohorte del Casillero de Datos</Anchor></li><li>Las alertas de Protect360 se actualizan a la hora UTC diaria.</li><li>Exportación de datos en bruto</li><li>Datos orgánicos agregados</li><li>API de extracción</li></ul> |

</Accordion>

<div id="agency-vs-ad-network-account" />

<Accordion title="Cuenta de agencia vs. cuenta de red publicitaria">

<div id="differences-between-ad-network-and-agency-accounts" />

#### Diferencias entre cuentas de red publicitaria y de agencia

<table><thead><tr><th>Red publicitaria</th><th>Agencia</th></tr></thead><tbody><tr><td>Parámetro de enlace de atribución para identificación: <code>pid</code> </td><td>Parámetro de enlace de atribución para identificación: <code>af_prt</code> </td></tr><tr><td>Coloca anuncios de aplicaciones en su propia plataforma</td><td>Promociona la aplicación a través de múltiples fuentes de medios</td></tr><tr><td>Solo observa el tráfico de los anuncios en su plataforma</td><td>Solo observa el tráfico de las fuentes de medios en las que se anuncia</td></tr><tr><td>Puede recibir información en tiempo real sobre instalaciones y eventos dentro de la aplicación a través de postbacks</td><td>No puede recibir información en tiempo real sobre instalaciones y eventos dentro de la aplicación a través de postbacks</td></tr><tr><td>Puede configurar devoluciones de eventos dentro de la aplicación para cualquier tráfico que provenga de sí mismo\*</td><td>Puede configurar devoluciones de eventos en la aplicación para algunos de los socios de los que obtiene tráfico\*</td></tr><tr><td colspan="2">\* Requiere permiso del especialista en marketing</td></tr></tbody></table>

</Accordion>

<div id="agency-accountscampaigns-and-reporting" />

## Cuentas de agencias: campañas y reportes

<div id="agency-setting-up-campaigns" />

<Accordion title="Agencia: configuración de campañas">

Las agencias pueden medir los siguientes tipos principales de tráfico:

* [Redes publicitarias de autoinforme (SRN)](/docs/about-agency-accounts#redes-publicitarias-de-autoinforme)
* [No SRN (redes publicitarias que utilizan enlaces de atribución)](/docs/about-agency-accounts#no-srn)

<div id="important" />

> 🚧 **¡Importante!**
>
> Al trabajar con agencias, desactivar un partner integrado no desactiva automáticamente ciertas capacidades de atribución para las agencias vinculadas a ese partner:
>
> Para desactivar completamente estas funcionalidades para las agencias, el anunciante debe desactivar manualmente las siguientes configuraciones antes de desactivar al partner:
>
> 1. Atribución view-through en la instalación
> 2. Igual prioridad de atribución multiplataforma
>
> Solo después de desactivar estas opciones, el anunciante deberá proceder a desactivar al partner.
>
> **Nota:** Si el anunciante desactiva al partner sin antes desactivar estas configuraciones, las agencias podrán seguir utilizando estas capacidades de atribución.

<div id="self-reporting-ad-networks" />

### Redes publicitarias de autoinforme

Las redes de autorreporte, como Meta Ads, Google Ads o X Ads, no emplean enlaces de atribución externos. En su lugar, cada red dispone de sus métodos y API propios que AppsFlyer utiliza para comunicar nuevas instalaciones, eventos dentro de la app, entre otros.

<div id="srn-configurations" />

#### Configuraciones de SRN

| nombres de SRN reservados | El especialista en marketing debe realizar la configuración inicial del SRN | Detalles |
| --- | --- | --- |
| Anuncios en la búsqueda de Apple | Sí | Para obtener más información sobre la configuración de agencia para campañas de Apple Search Ads, haga clic <Anchor target="_blank" href="/marketers/es/docs/apple-ads-integration-setup#configuración-de-agencias-y-partners-de-marketing">aquí</Anchor>. |
| Anuncios de Google | Sí | Para obtener más información sobre la configuración de agencia para campañas de Google Ads, haga clic <Anchor target="_blank" href="/marketers/es/docs/google-ads-adwords-integration-setup-for-agencies">aquí</Anchor>. |
| Plataforma de Marketing de Google (GMP) | No | GMP cuenta con dos API diferentes. Conozca más sobre las <Anchor target="_blank" href="/marketers/es/docs/google-marketing-platform-display-video-360-dv360-integration#comparing-the-legacy-and-new-integrations">diferencias entre ambas</Anchor> y elija la que sea relevante para usted. |
| Anuncios Meta  <br />y  <br />Anuncios X | Sí | **Nota:** Esta sección se refiere a los anuncios de Meta. Para la atribución de Facebook Social (publicaciones), consulte [Medios propios](/docs/about-agency-accounts#owned-media%E2%80%94onelink-and-custom-links).<br /><br />**Todos los anuncios de Meta y las campañas de X Ads deben comenzar con el nombre de la cuenta de la agencia seguido de "\_".** El nombre se define en la plataforma AppsFlyer.<br />Las campañas que no estén correctamente nombradas son visibles para el especialista en marketing, pero no para la cuenta de la agencia.<br /><br />**Nota:**<ul><li>El nombre de la agencia DISTINGUE ENTRE MAYÚSCULAS Y MINÚSCULAS.</li><li>Vea más detalles sobre la configuración de <Anchor target="_blank" href="/marketers/es/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta ads</Anchor> y <Anchor target="_blank" href="/marketers/es/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X ads</Anchor> para agencias.</li><li>Contacte a [agency@appsflyer.com](mailto:agency@appsflyer.com) si tiene alguna pregunta sobre esto.</li></ul>**Ejemplo**<br />Agencyx lleva a cabo una campaña de anuncios Meta llamada agencyx\_brilliantcampaign, que es visible para dicha agencia.<br /><br />Agencyz ejecuta una campaña de X Ads llamada AgencyZ\_whathaveidonewrong, pero no ve los resultados. Esto sucede porque la parte del nombre de la agencia en la campaña difiere del nombre de la agencia definido (con A y Z en mayúsculas). |
| Snapchat | No | Para más detalles sobre cómo configurar agencias para campañas en Snapchat, haga clic <Anchor target="_blank" href="/marketers/es/docs/snapchat-advanced-srn-integration-setup">aquí</Anchor>. |
| TikTok para empresas | Sí | Para más detalles sobre cómo configurar agencias para campañas en TikTok for Business, haga clic <Anchor target="_blank" href="/marketers/es/docs/tiktok-for-business-advanced-srn-integration-setup#setting-up-tiktok-for-business-for-agencies">aquí</Anchor>. |
| Yahoo (Oath: Plataformas de anuncios / Yahoo Gemini) | Sí | Para más detalles sobre la configuración de la agencia para campañas en Yahoo, <Anchor target="_blank" href="/marketers/es/docs/yahoo-integration-setup#configuración-de-agencia">haga clic aquí</Anchor>. |

<div id="non-srns" />

### No SRN

A diferencia de las SRN, la mayoría de las redes de anuncios utilizan enlaces de atribución para sus propósitos. <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#attribution-link-tab">Estos enlaces de atribución ya están disponibles</Anchor> en la configuración de cada red en AppsFlyer y se pueden copiar directamente desde allí.

Para las agencias, el proceso es casi idéntico al que siguen los comercializadores. Al acceder a la ventana de configuración de cualquier red de anuncios regular, el enlace de atribución ya está presente. La única diferencia es la adición automática del parámetro `af_prt` al enlace de atribución.

<div id="ad-network-configuration-visibility" />

#### Visibilidad de la configuración de la red de anuncios

La configuración de la red de anuncios solo es visible para las redes mismas cuando el comercializador (propietario de la app) la configura. Cuando una agencia activa y configura la integración de la red de anuncios, esta ve la sección como inactiva.

<div id="af_prt-parameter" />

#### Parámetro af\_prt

El valor del parámetro `af_prt` es el nombre de la agencia. Cuando el nombre de la agencia se incluye en el parámetro `af_prt`, se convierte a minúsculas.

Cuando `af_prt` incluye el nombre de su agencia en el enlace de atribución, las nuevas instalaciones pueden atribuirse a su cuenta de agencia. De lo contrario, las nuevas instalaciones se atribuyen directamente a la red de anuncios.

<Image align="center" alt="agencia-af-prt.png" src="https://files.readme.io/61559e2e1628e9411665b7e8d3d3d440a55effb3bccda79c7fe1ee02fd43fb8c-32355631649937.png" />

**No utilice enlaces provinientes del comercializador**: asegúrese de usar los enlaces de su propia cuenta para evitar atribuciones incorrectas.

<div id="special-case-all-installs-and-all-launches-networks" />

#### Caso especial: Redes que registran todas las instalaciones y todos los lanzamientos

Algunos no SRN requieren (o permiten) que los comercializadores les envíen postbacks **para dispositivos no atribuidos a ellos**.

Red de todas las instalaciones

La red acepta un postback por cada nueva instalación de app, independientemente de su origen

Red de todos los lanzamientos

La red acepta un postback por cada nuevo lanzamiento de app, de cualquier fuente

Algunos ejemplos de redes que registran todas las instalaciones son Vungle, WeChat, StartApp, Unity Ads, y más.

La siguiente tabla muestra la lista completa de todas las redes de lanzamientos:

| Nombre de la red | PID de red (en enlaces de atribución de AF) |
| --- | --- |
| Supersonicads (una red heredada de ironSource) | supersonicads\_int |
| Adelphic Remarketing | adelphicremarketing\_int |
| Grow Mobile | growmobile\_int |
| ONE by AOL | advertising.com\_int |
| Lemmonet Mobile | lemmonetmobile\_int |
| Clickky | clickky\_int |
| Remerge | remerge\_int |
| MyThings | mythings\_int |
| TikTok para empresas | bytedanceglobal\_int |

<div id="how-to-setup-agency-attribution-with-all-installslaunches-networks" />

#### ¿Cómo configurar la atribución de agencia con todas las redes de instalaciones/lanzamientos?

Trabajar con estas redes implica enviar información de instalaciones no gestionadas por la agencia. Por lo tanto, estas redes requieren que el marketer las configure antes que la **agencia**.

<div id="example" />

> 📄 **Ejemplo**
>
> Veamos como ejemplo la configuración de atribución de agencia con Tapjoy:
>
> 1. El marketer accede a la ventana de configuración de Tapjoy en su panel de control.
> 2. El marketer introduce el ID de la aplicación de Tapjoy, dado por Tapjoy al **marketer**, en el campo de texto **app\_id**.
> 3. En la pestaña **Integración** > Postbacks predeterminados, el marketer selecciona **Todas las fuentes de medios, incluidas las orgánicas**.
> 4. La agencia accede a la ventana de configuración de Tapjoy en su panel.
> 5. La agencia introduce el ID de la aplicación de Tapjoy, dado a la **agencia** por Tapjoy, en el campo de texto **app\_id**.

<div id="deep-linking" />

### Enlaces profundos

El enlace profundo permite lanzar una aplicación móvil al abrir contenido personalizado y/o dirigir a los usuarios a actividades específicas dentro de la app. Esto puede ofrecer una experiencia superior a sus usuarios y aumentar su participación.

Para que el enlace profundo funcione, la app móvil debe estar desarrollada con capacidades e infraestructura adecuadas. Contacte con el propietario de la app para confirmar si es adecuada para enlaces profundos antes de configurar las campañas.

<div id="retargeting" />

### Redireccionamiento

* * La <Anchor target="_blank" href="/marketers/es/docs/retargeting-attribution-guide">atribución de retargeting</Anchor> permite dirigirse a usuarios existentes o pasados en sus campañas. Las campañas de retargeting a menudo necesitan capacidades de enlace profundo para funcionar correctamente.

<div id="in-app-events" />

### Eventos dentro de la aplicación

Los propietarios de apps pueden tener diversos eventos en sus aplicaciones (por ejemplo, compras, ver un tutorial, superar un nivel, etc.) que pueden registrar y analizar en AppsFlyer. Las agencias pueden visualizar los datos de los eventos que se les atribuyen en la página Eventos de su cuenta.

<div id="in-app-event-postbacks" />

#### Postbacks de eventos in-app

Las agencias pueden recibir permiso para configurar <Anchor target="_blank" href="/marketers/es/docs/in-app-event-postback-configuration">postbacks de eventos in-app</Anchor> (incluyendo el <Anchor target="_blank" href="/marketers/es/docs/measure-sessions">evento af\_app\_opened</Anchor>) para redes publicitarias, tras recibir la autorización del Marketer.

Las agencias pueden otorgar permiso a las redes publicitarias para configurar postbacks dentro de la aplicación. El <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">permiso se concede</Anchor> por los especialistas en marketing en la pestaña de permisos de la agencia.

</Accordion>

<div id="reporting-for-agencies" />

<Accordion title="Informes para agencias">

* Las estadísticas de tráfico se visualizan y descargan directamente desde el panel de AppsFlyer.
* Se accede a los informes a través de la página <Anchor target="_blank" href="/marketers/es/docs/raw-data-reporting-overview">Exportar datos</Anchor> en el panel de AppsFlyer. También puedes acceder a los informes de cohorte a través de <Anchor target="_blank" href="/partners/es/docs/data-locker-reports-for-agencies">Data Locker</Anchor>.
* Están disponibles los siguientes tipos de informes:
  * Agregados
  * Datos sin procesar
* Los especialistas en marketing y las agencias generalmente no pueden acceder a los mismos datos en el panel, informes, etc.
* Las agencias suelen ser responsables solo de una parte del tráfico del comercializador, por lo que su acceso a los datos es limitado en comparación con el de los comercializadores.
* <Anchor target="_blank" href="/marketers/es/docs/manage-data-access-permissions">Este artículo</Anchor> detalla estas diferencias. Las siguientes secciones las destacan.

<div id="note-1" />

> 📘 **Nota**
>
> Debido a los términos de servicio de Meta Ads y X Ads, las **agencias**, que se consideran terceros, **no tienen acceso a los informes de datos sin procesar sobre tráfico originado en Meta Ads o X Ads**.

<div id="access-to-aggregate-data" />

### Acceso a datos agregados

* Los informes de rendimiento, también conocidos como informes de datos agregados, están disponibles de forma predeterminada para las cuentas de agencia. Lectura relacionada: <Anchor target="_blank" href="/marketers/es/docs/aggregated-and-analytics-reporting-overview">Informes de rendimiento agregado</Anchor>
* El acceso a los informes de datos orgánicos agregados requiere el <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">permiso</Anchor> del comercializador.
* Las agencias pueden acceder a los informes de retención y cohorte, y al panel de Protect360. Esto requiere que el comercializador active <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">**Permitir acceso a sus informes de retención y cohorte**</Anchor> o <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">**Permitir acceso a su panel de Protect360**</Anchor>, respectivamente, en la pestaña **Permisos** de **Integraciones activas**.

<div id="access-to-raw-data" />

### Acceso a datos sin procesar

<Anchor target="_blank" href="/marketers/es/docs/raw-data-reporting-overview">Los informes de datos sin procesar</Anchor> (informes a nivel de usuario) contienen información de atribución y están divididos en temas.

<div id="time-zone-and-currency" />

### Zona horaria y moneda

Las agencias ven las aplicaciones en la zona horaria y moneda definidas por la aplicación, pero estos ajustes solo pueden ser modificados por los especialistas en marketing.

<div id="cost-reporting" />

### Informe de costos

Las agencias pueden habilitar **Obtener datos de costos** al configurar un socio integrado que <Anchor target="_blank" href="/marketers/es/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">admita datos de costos</Anchor>.

**Para habilitar la obtención de datos de costos:**

1. En AppsFlyer, desde el menú lateral, selecciona **Colaborar** > **Integraciones activas**.
2. Filtra los socios por Costo: Desde la parte superior de la página **Integraciones activas**, selecciona **Funciones compatibles** >**Costo**.
3. Selecciona el socio. Serás dirigido a la pestaña **Integración**. Seleccione la pestaña **Costo**.
4. Activa la opción **Obtener datos de costos**.
5. Introduce la clave API para este socio.
6. Haz clic en **Guardar**.

<div id="accessing-and-viewing-cost-data" />

#### Acceso y visualización de datos de costos

Los datos de costos están disponibles para la agencia en las siguientes fuentes de datos:

* Página de **Descripción general**: los datos de costos se muestran en el **Informe de rendimiento agregado** de esta página.
* **Informes**: los datos de costos están disponibles en informes exportados como **Instalaciones** en **Informes de datos sin procesar** y **Socios (fuentes de medios)** en **Informes de rendimiento**.

<div id="hybrid-account-data-access" />

### Acceso a datos en cuentas híbridas

Las cuentas híbridas son cuentas de agencia que gestionan algunas aplicaciones como una agencia (socio de aplicación) y otras como comercializador (propietario de la aplicación).

Las siguientes funciones a nivel de cuenta tienen disponibilidad limitada:

* <Anchor target="_blank" href="/marketers/es/docs/custom-dashboards">Panel personalizado</Anchor>: no está disponible para agencias y cuentas híbridas.
* Informe de cohortes: disponible con autorización del comercializador.
* Protect360: accesible con permiso del comercializador.

Si posees una cuenta híbrida, pueden aparecer en tu panel de control, pero recibirás un error 404 al intentar abrirlas.

Si deseas utilizar estas funciones, se recomienda crear una nueva cuenta de Marketer y separar tus aplicaciones de Marketer y Agencia. Las funciones mencionadas estarán disponibles en tu cuenta de Marketer si las tienes habilitadas.

</Accordion>

<div data-zendesk-anchors="about-agency-accounts=acerca-de-las-cuentas-de-agencia h_01HDNYNZYR2FTMQ71EV2AY3A3A=acerca-de-las-cuentas-de-agencia agency-access-to-marketer-data=acceso-de-la-agencia-a-los-datos-de-los-comercializadores h_01HDNYNZYRZKK97GZ6R0MB9RQN=acceso-de-la-agencia-a-los-datos-de-los-comercializadores agency-access-to-ad-network-integrations=acceso-de-la-agencia-a-las-integraciones-de-redes-publicitarias h_01J00RYT8J0MBPHTGK5T4WEE43=acceso-de-la-agencia-a-las-integraciones-de-redes-publicitarias h_01HJR00RGQX0CQEHDS9BHBGJD4=nota agency-transparency=transparencia-de-la-agencia h_01HDNYNZYRYHJ98YQWVVENZ07P=transparencia-de-la-agencia comparing-different-types-of-accounts=comparaci%C3%B3n-de-diferentes-tipos-de-cuentas h_01HDNYNZYR65409AGM9F2PZRC8=comparaci%C3%B3n-de-diferentes-tipos-de-cuentas h_01HDNYNZYS7A2H60EEAJ114VSM=agency-versus-marketer-accounts differences-between-marketer-and-agency-accounts=diferencias-entre-cuentas-de-comercializadores-y-de-agencias h_01HDNYNZYSS7WSQ07S7KRADN7Z=diferencias-entre-cuentas-de-comercializadores-y-de-agencias features-available-to-agencies=funciones-disponibles-para-las-agencias h_01HDNYNZYSX4WPQKS0H6JN6FCP=funciones-disponibles-para-las-agencias h_01HDNYNZYS8KRSPM5CPVJEJ74Y=agency-vs-ad-network-account differences-between-ad-network-and-agency-accounts=diferencias-entre-cuentas-de-red-publicitaria-y-de-agencia h_01HDNYNZYS4VPZMY34WA3SG5JT=diferencias-entre-cuentas-de-red-publicitaria-y-de-agencia agency-accounts%E2%80%94campaigns-and-reporting=cuentas-de-agencias-campa%C3%B1as-y-reportes h_01HDNYNZYS32SNR5F0WKJ4G9Q1=cuentas-de-agencias-campa%C3%B1as-y-reportes h_01HDNYNZYSNF2RQ3E7PM4HK433=agency-setting-up-campaigns h_01KC9MDDRPTB05PV6NCGZVFRMJ=importante selfreporting-ad-networks=redes-publicitarias-de-autoinforme h_01HDNYNZYS8X1VA4T46DQYQZFE=redes-publicitarias-de-autoinforme srn-configurations=configuraciones-de-srn h_01HDNYNZYS8AM2MFPRXFA4JXNS=configuraciones-de-srn h_01HDNYNZYSFXZXR99T6ME2R43F=ejemplo nonsrns=no-srn h_01HDNYNZYSN28VZQKCBRGXAVY0=no-srn ad-network-configuration-visibility=visibilidad-de-la-configuraci%C3%B3n-de-la-red-de-anuncios h_01HDNYNZYSG5MQDDKV55HF4X9C=visibilidad-de-la-configuraci%C3%B3n-de-la-red-de-anuncios af_prt-parameter=par%C3%A1metro-af_prt h_01HDNYNZYSC7XNJCJ1F27KTM9Z=par%C3%A1metro-af_prt special-case-allinstalls-and-alllaunches-networks=caso-especial-redes-que-registran-todas-las-instalaciones-y-todos-los-lanzamientos h_01HDNYNZYSB4MKXD47E1VHDN62=caso-especial-redes-que-registran-todas-las-instalaciones-y-todos-los-lanzamientos how-to-setup-agency-attribution-with-all-installslaunches-networks=c%C3%B3mo-configurar-la-atribuci%C3%B3n-de-agencia-con-todas-las-redes-de-instalacioneslanzamientos h_01HDNYNZYSHNV2B27JQV4EEVFM=c%C3%B3mo-configurar-la-atribuci%C3%B3n-de-agencia-con-todas-las-redes-de-instalacioneslanzamientos h_01HDNYNZYS5WYADGW24AVK9RCZ=ejemplo deep-linking=enlaces-profundos h_01HDNYNZYS5W0SMCF1YC6C3G4C=enlaces-profundos retargeting=redireccionamiento h_01HDNYNZYS3Z7RE51M7G7386VZ=redireccionamiento inapp-events=eventos-dentro-de-la-aplicaci%C3%B3n h_01HDNYNZYTDFN4MB6QBEQ8P5XW=eventos-dentro-de-la-aplicaci%C3%B3n inapp-event-postbacks=postbacks-de-eventos-in-app h_01HMDP38S3NPE5R4QZJ5CW404W=postbacks-de-eventos-in-app h_01HDNYNZYTA767NGSTNECTBCV2=reporting-for-agencies h_01HDNYNZYTYBWGMY2PP8MPQE2F=nota-1 access-to-performance-reports=acceso-a-datos-agregados h_01HDNYNZYTDH4S38XG3JCZQYJJ=acceso-a-datos-agregados access-to-raw-data=acceso-a-datos-sin-procesar h_01HDNYNZYT4ZKBNGDR3QR1VTEZ=acceso-a-datos-sin-procesar time-zone-and-currency=zona-horaria-y-moneda h_01HDNYNZYT97ET1TQHKSRDMWDC=zona-horaria-y-moneda cost-reporting=informe-de-costos h_01HDNYNZYTYT9NHMHQQ77PK8CQ=informe-de-costos accessing-and-viewing-cost-data=acceso-y-visualizaci%C3%B3n-de-datos-de-costos h_01HDNYNZYTWB5WVYY8C347G1ME=acceso-y-visualizaci%C3%B3n-de-datos-de-costos hybrid-account-data-access=acceso-a-datos-en-cuentas-h%C3%ADbridas h_01HDNYNZYTKZTCBSBKZEJ7M0JN=acceso-a-datos-en-cuentas-h%C3%ADbridas" />
