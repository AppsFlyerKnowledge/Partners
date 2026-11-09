---
title: Panel de control de partners integrados
metadata:
  keywords:
    - partner login
    - partner dashboard
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-08-08T08:11:38Z'
  edited_at: '2026-08-12T12:27:13Z'
  id: 212955423
  locale: es
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/es/articles/212955423
---
> **De un vistazo:** Los partners integrados utilizan el panel de control y los reportes para ver y analizar el tráfico de campaña que se te atribuye.

<div id="using-the-appsflyer-dashboard" />

## Uso del panel de control de AppsFlyer

**Para iniciar sesión en AppsFlyer**:

1. <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">Inicia sesión</Anchor> o ve a https://hq1.appsflyer.com/auth/login  
   Se muestra la lista de aplicaciones.
2. Selecciona una aplicación o búscala.  
   ¡Atención! Nota: Si no ves la aplicación requerida, pídele al anunciante que te conceda <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions">permisos de red de publicidad</Anchor>. El anunciante hace esto en el panel de control de AppsFlyer en la pestaña de permisos.

<div id="overview-dashboard" />

## Panel de vista general

Las métricas y los gráficos de rendimiento de la campaña están disponibles en el Panel de control general. Este panel de control contiene diferentes tipos de vistas para las campañas UA y de retargeting.

<div id="report-access" />

## Acceso a reportes

Para ver los datos del reporte:

* En el menú lateral, selecciona uno de los siguientes:
  * <Anchor target="_blank" href="/marketers/es/docs/raw-data-export-page">Exportación de raw data</Anchor>
  * <Anchor target="_blank" href="/marketers/es/docs/aggregated-data-export-page">Exportación de datos agregados</Anchor>  
    Se abre la ventana Reportes.

<div id="note" />

> 📘 **Nota**
>
> * Los datos que se muestran en los reportes de raw data se limitan a los raw data en los postbacks atribuidos solo al partner.
> * Para los suscriptores de Protect360, cuando el anunciante concede el permiso de **<Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#access-protect360-dashboard-raw-data">dashboard & raw data de Protect360</Anchor>**, los partners también tienen acceso a los reportes de raw data de Protect360.
> * Los datos del **valor de evento** no se muestran en este reporte. Para obtener valores de eventos, puedes realizar una de las siguientes acciones:
>
> * * Solicita al anunciante que te proporcione reportes de raw data de eventos in-app
>   * Add `(event-value)` <Anchor target="_blank" href="/partners/es/docs/postback-macros-for-ad-networks">macro to the postback URL</Anchor>

<div id="using-postback-reports" />

### Uso de reportes de postback

Puedes utilizar los <Anchor target="_blank" href="/marketers/es/docs/raw-data-reporting-overview#postbacks%C2%A0">reportes de postbacks</Anchor> de instalación y de eventos in-app para encontrar acciones "faltantes", es decir, cuando el raw data del anunciante muestra acciones del usuario que no se registraron en la red de publicidad.

Descarga el reporte de Postbacks correspondiente y busca los campos **URL de postback** y **Código de respuesta HTTP de postback**:

* Si el código de respuesta es 200, AppsFlyer envió el postback y recibió un acuse de recibo de la red de publicidad.
* Si falta el código de respuesta, AppsFlyer envió el postback pero no recibió respuesta. El campo **Mensaje de error de postback** describe el problema.

<Image align="center" alt="" src="https://files.readme.io/e846104ebdd43b6bdd5c635e645ba5806aa152e6fa84d92f957b754b22fd819a-360005578257.png" />

<div id="viewing-configuration-settings-and-data" />

## Ver la configuración y los datos

Click **Integrated Partners** on the left side of the window to view the current configuration settings. Incluso si no te han otorgado permisos, es posible que puedas ver los ajustes de configuración (modo de solo lectura).

La ad network puede ver la configuración en su dashboard solo cuando la configura el anunciante. 

Las agencias pueden configurar la configuración de la ad network al recibir el permiso correspondiente del anunciante. Ten en cuenta que **cuando** **la configuración la realiza una agencia, la ad network la ve como inactiva**.

<div id="permissions" />

## Permisos

Con la pestaña **Permisos**, los anunciantes pueden <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions">otorgar diferentes tipos de permisos a las redes de publicidad</Anchor>.

<div id="enabling-permissions" />

### Habilitar permisos

El primer paso es que tu cliente habilite los permisos. Tu cliente debe activar los **Permisos de Ad network**. Cuando lo haga, ocurre lo siguiente:

1. La aplicación se muestra en tu cuenta de la red de publicidad.
2. El admin de tu cuenta de ad network obtiene acceso para ver el dashboard de la app de tu cliente. En la primera fase, solo el administrador tiene acceso. Si quieres que un miembro de tu equipo también vea el dashboard de la app, tu cliente tiene que concederle permisos.
3. Los permisos para ver el dashboard de la app se conceden solo a tu ad network.

<div id="granting-permissions-to-ad-network-team-members" />

### Concesión de permisos a miembros del equipo de la ad network

Si quieres que un miembro de tu equipo también vea el dashboard de la app, tu cliente tiene que concederle permisos.

1. Da a tu cliente los correos electrónicos de los miembros del equipo a los que quieres que conceda permisos.
2. A continuación, el cliente debería <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions">agregarlos a la integración con tu red de publicidad</Anchor>.

<div id="granting-additional-permissions" />

### Conceder permisos adicionales

Tu cliente puede conceder permisos adicionales para que la ad network y los miembros de su equipo vean lo siguiente:

* Configuración de parámetros de integración
* Configuración de eventos in-app
* Informe de retención
* Usuarios leales
* Eventos dentro de la aplicación
* Ingresos totales
* Protect360 dashboard - available only to Protect360 customers

To allow this, contact your client to select you from the Integrated Partners list and grant you access to the relevant section within the Permissions tab.

Cuando el anunciante concede permiso a la ad network para configurar su enlace de atribución y mapear eventos in-app, pueden entrar en las pestañas correspondientes y hacer los cambios necesarios.

<div id="note-1" />

> 📘 **Nota**
>
> * Any changes made to the configuration overwrites the current configuration irrespective of whether it is set by the advertiser or the ad network.
> * Las agencias pueden añadir miembros del equipo de la ad network a la configuración, pero solo los propietarios de la aplicación pueden conceder permisos a las ad networks.

Once your client has granted you permission to the integration parameter configurations, you are able to access it from the left side of the main dashboard and select **Integrated Partners.**

Si tu cliente te ha concedido permiso para los reportes de retención, puedes acceder a ellos desde el lado izquierdo del dashboard principal y seleccionar **Retention.**

<div data-zendesk-anchors="using-the-appsflyer-dashboard=uso-del-panel-de-control-de-appsflyer h_01HCF5VPHN5RRQFXVJJFPFQBSW=uso-del-panel-de-control-de-appsflyer overview-dashboard=panel-de-vista-general h_01HCF5VPHNXBQZNF9MNEVCQ243=panel-de-vista-general report-access=acceso-a-reportes h_01HCF5VPHN08CV555KDHB7QP1Z=acceso-a-reportes h_01HCF5VPHN3REJ2FPD8386Z92S=nota using-postback-reports=uso-de-reportes-de-postback h_01HCF5VPHN8RV3GBX1NNFX10P0=uso-de-reportes-de-postback viewing-configuration-settings-and-data=ver-la-configuraci%C3%B3n-y-los-datos h_01HCF5VPHNSW9X7SNQPC17Q45A=ver-la-configuraci%C3%B3n-y-los-datos permissions=permisos h_01HCF5VPHN6AJ7SE6MGW57BPW8=permisos enabling-permissions=habilitar-permisos h_01HCF5VPHNRCQ5P3MZF9S5RWZW=habilitar-permisos granting-permissions-to-ad-network-team-members=concesi%C3%B3n-de-permisos-a-miembros-del-equipo-de-la-ad-network h_01HCF5VPHP2EXY705GW2VM5YMA=concesi%C3%B3n-de-permisos-a-miembros-del-equipo-de-la-ad-network granting-additional-permissions=conceder-permisos-adicionales h_01HCF5VPHPHS8QQBMVTGV7B4VJ=conceder-permisos-adicionales h_01HCF5VPHPCD52R9222AFQH176=nota-1" />
