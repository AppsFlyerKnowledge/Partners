---
title: Pruebas de integración de Android para ad networks
metadata:
  keywords:
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
  created_at: '2021-12-06T10:35:58Z'
  edited_at: '2026-08-12T12:28:54Z'
  id: 4412945443857
  locale: es
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/es/articles/4412945443857
---
> **De un vistazo:** Prueba tu integración de Android con AppsFlyer usando la aplicación AppsFlyer Partner Integrations para activar postbacks.

<div id="android-integration-testing" />

## Pruebas de integración de Android

Las pruebas constan de los siguientes elementos:

* Usa la versión para Android de la aplicación AppsFlyer Partner Integrations para generar eventos in-app de instalación de prueba y de compra. Estas pruebas, a su vez, activan postbacks enviados a tus endpoints. También tienes la opción de probar eventos in-app de login y registro.
* Al recibir los postbacks, verifica que puedas ingerirlos.

**Alcance de las pruebas**

La siguiente tabla enumera escenarios de prueba según las combinaciones de ajustes disponibles.

Para cada escenario, puedes probar instalaciones y eventos in-app. Para los eventos in-app, puedes usar el <Anchor target="_blank" href="/partners/es/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">mapeo de eventos in-app</Anchor> para asignar los eventos del anunciante a tus eventos.

<div id="testing" />

## Pruebas

Completa los requisitos previos y, a continuación, realiza los procedimientos de prueba de las secciones siguientes. Cada sección de prueba contiene una tabla que puedes usar para registrar los resultados de tus pruebas.

<div id="prerequisites" />

<Accordion title="Prerrequisitos">

Completa los requisitos previos antes de empezar a ejecutar el procedimiento de prueba.

| Prerrequisitos |
| --- |
| <Anchor target="_blank" href="/partners/es/docs/turn-on-test-app-integration-for-ad-networks">Integra la aplicación de prueba para Android en tu cuenta.</Anchor> |
| Verifica que la aplicación de prueba esté integrada en tu cuenta |
| <Anchor target="_blank" href="/partners/es/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Asigna los eventos in-app a los nombres de tus eventos</Anchor>. Nombres de eventos que se deben asignar: `purchase`, `login`, `registration` |
| <Anchor target="_blank" href="/partners/es/docs/ios-integration-testing-for-ad-networks#attribution-link">Prepara el enlace de atribución</Anchor> |
| Prueba la atribución de instalaciones usando un dispositivo con Android |
| Prueba la atribución de eventos in-app usando un dispositivo Android |
| Prueba la atribución de retargeting usando un dispositivo Android |

</Accordion>

<div id="test-install-attribution" />

<Accordion title="Probar la atribución de instalaciones">

**Para activar postbacks:**

1. Envía el enlace de atribución que has preparado previamente a un dispositivo de prueba.
2. Haz clic en el enlace, realiza la instalación y luego abre la app.  
   Se muestra la página **Install Data**.
3. Valida la atribución con los siguientes parámetros. Si la validación falla, consulta <Anchor target="_blank" href="/partners/es/docs/ios-integration-testing-for-ad-networks#troubleshooting">Solución de problemas</Anchor>.

   1. `install_time`: cerca de la hora actual. La hora está en UTC.
   2. `af_status: Non-organic` Si no es así, la instalación no se ha atribuido.
   3. `media_source`: tu ad network
4. Toca **In-App Event Tests.**
5. Toca **Purchase Event.**  
   Se muestra la confirmación de Purchase Event.
6. Verifica que:
   1. Has recibido los postbacks de instalación y compra.
   2. El nombre del evento está asignado correctamente (si has asignado eventos in-app).
   3. Puedes procesar el postback.

</Accordion>

<div id="supplementary-information-and-procedures" />

## Información y procedimientos complementarios

<div id="about-the-partner-integrations-test-app" />

<Accordion title="Acerca de la app Partner Integrations de prueba">

La app Partner Integrations está disponible en Google Play. La app envía eventos de instalación y eventos in-app a la plataforma AppsFlyer.

Cuando se abre la app por primera vez, la página **Install Data** muestra los datos de conversión registrados en la plataforma AppsFlyer. Los eventos in-app de prueba se activan en la interfaz de usuario.

Las siguientes funciones están disponibles:

* **In-App Event Tests**  
  Envía `purchase`, `login` y `registration`, y eventos in-app. Al asignar los nombres de los eventos in-app de la app a tus nombres de evento, los postbacks se completan con tus nombres de evento.

</Accordion>

<div id="attribution-link" />

<Accordion title="Enlace de atribución">

Prepara un enlace de atribución en el Dashboard de AppsFlyer con uno de los siguientes métodos:

* Genera el enlace en el panel de control de AppsFlyer.
* Edita el enlace de ejemplo que aparece a continuación.

**Para generar un enlace en el panel de control:**

1. En AppsFlyer, en el menú superior, selecciona **Mis aplicaciones**.
2. Selecciona **adNetworkTest**.
3. En AppsFlyer, en el menú lateral, selecciona **Colaborar** > **Integraciones activas** > selecciona tu ad network > la pestaña **Enlace de atribución**.
4. En la pestaña Enlace de atribución, configura los parámetros que se indican. Puedes añadir parámetros adicionales si es necesario. Enlace al enlace de atribución 

| Parámetro | Valor de ejemplo | Nota |
| --- | --- | --- |
| <span id="campaign"></span>Apps asociadas que pertenecen a una plantilla OneLink relacionada para atribución multiplataforma | c-test-2020-12-20 | Establece un valor que puedas identificar en tus postbacks |
| <span id="pid"></span>PID no integrados. | pitestap |  |

5. Copia el enlace resultante para usarlo más adelante.

**Enlace de atribución de ejemplo:**

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Aplicación de prueba integrada en tu cuenta">

**Para verificar que la aplicación de prueba está disponible en tu cuenta:**

1. En AppsFlyer, en el menú superior, ve a **Mis aplicaciones**.
2. Verifica que la app **Partner Integrations adNewtorkTest** aparezca en Apps disponibles. Si no es así, ponte en contacto con tu Partners Development Manager.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Solución de problemas">

| Síntoma | Causa/acción correctiva |
| --- | --- |
| La hora de instalación no es la hora actual | La aplicación no se eliminó antes de la instalación.<br /><br />Elimina la aplicación y repite el procedimiento. |
| La fuente de medios no es tu fuente de medios | Verifica que has establecido el valor correcto de **pid** en el enlace de atribución. Verifica que estás usando el enlace de atribución correcto |
| af\_status es orgánico | Comprueba el formato del enlace de atribución, especialmente el valor de **pid**. |

</Accordion>

<div id="test-retargeting-attribution" />

<Accordion title="Prueba de atribución de retargeting">

También puedes probar la atribución de retargeting. El proceso es casi el mismo, salvo por un parámetro que añades al enlace de atribución.

Genera un nuevo enlace de atribución y añádele el parámetro `is_retargeting=true`.

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_click_lookback=7d
          &clickid={clickid}&is_retargeting=true
```

Instala la aplicación con el enlace de retargeting. El flujo es el mismo que se describe en [la prueba de atribución de instalación](/docs/android-integration-testing-for-ad-networks#test-install-attribution).

<div id="viewing-retargeted-installs-in-the-dashboard" />

### Ver instalaciones de retargeting en el dashboard

Accede a tu dashboard de AppsFlyer y haz clic en **retargeting** en el menú lateral izquierdo. Es posible que debas esperar hasta 30 minutos para que la instalación con retargeting aparezca en el dashboard.

<Image align="center" alt="com_appsflyer_adNetworkTest-retargeting.png" src="https://files.readme.io/e46789b004be2f4fc15f095ba11a0f3f5d03abb1240e54e4b534285e3e4efd8d-21266228899601.png" />

</Accordion>

<div id="test-viewthrough-attribution" />

<Accordion title="Prueba de atribución view-through">

1. En AppsFlyer, ve a **My Apps**.
2. Selecciona **adNetworkTest**.
3. En AppsFlyer, en el menú lateral, selecciona **Collaborate** > **Active Integrations** > selecciona tu ad network > pestaña **Integration**.
4. Asegúrate de que **Enable view-through attribution** esté activado.
5. Copia el enlace de atribución de impresiones.

   ```http
   https://impression.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_viewthrough_lookback=24h&advertising_id=YOUR_GAID&af_siteid=YOUR_SITEID
   ```

   Sustituye los parámetros de la siguiente manera:

   * YOUR\_PID: tu ID de partner proporcionado por AppsFlyer (termina en *\_int*)
   * YOUR\_CAMPAIGN: cualquier nombre de campaña
   * YOUR\_GAID: tu Google Advertising ID
   * YOUR\_SITEID: cualquier ID de sitio

   Nota: los parámetros del enlace son los parámetros básicos que se usan aquí con fines de prueba. Puedes incluir otros parámetros en el enlace de atribución view-through según tus necesidades.
6. Envía el enlace de atribución view-through al dispositivo de prueba.
7. Abre el enlace en el navegador e instala la aplicación desde la tienda.
8. Inicia la aplicación.  
   Aparecerá la siguiente pantalla:

   <Image align="center" alt="vta-testing-postback.png" src="https://files.readme.io/88b6720928d7540eeb2fe8f42f39ecdccc04655aa49f95d08dba5741d5e39982-4831106525457.png" />

   Si no ves este mensaje, asegúrate de que el enlace de atribución view-through tenga el formato correcto. Desinstala la aplicación y vuelve a instalarla usando el enlace de atribución view-through con el nuevo dispositivo de prueba.

Consejo

Para obtener resultados más completos, repite el proceso de instalación usando el enlace de atribución view-through con el nuevo dispositivo de prueba. Desinstala la aplicación, cambia los parámetros del enlace (el nombre de la campaña, af\_siteid y advertising\_id) y vuelve a instalarla haciendo clic en la URL.

<div id="view-installs-in-the-dashboard" />

### Ver instalaciones en el Dashboard

Una vez que instales e inicies la aplicación, podrás ver los resultados en tu dashboard de AppsFlyer.

Espera hasta 30 minutos para que la instalación aparezca en el dashboard de la aplicación.

</Accordion>

<div id="raw-data-export" />

<Accordion title="Exportación de raw data">

Los datos relacionados con las aplicaciones cuya instalación se atribuye a tu ad network se pueden exportar en formato CSV.

Los datos incluyen lo siguiente:

* Instalaciones asistidas
* Eventos dentro de la aplicación
* Instalaciones de retargeting
* Eventos in-app de aplicaciones instaladas desde campañas de retargeting

**Para exportar raw data**:

1. En AppsFlyer, ve a **Report** > **Raw data export**.
2. Selecciona el intervalo de fechas.
3. Selecciona un reporte.  
   El reporte se descarga en unos minutos.

</Accordion>

<div id="verify-postback-data" />

<Accordion title="Verificar datos de postback">

Cada instalación genera un postback que se envía a tus servidores. Para verificar la URL del postback, su estructura y los parámetros que se le añaden, exporta el reporte **Installation postbacks**.

El reporte **Installation postbacks** contiene una columna titulada **Postback URL**. Esta columna muestra las URL de postback generadas para todas y cada una de las instalaciones.

Revisa los datos de esa columna para verificar lo siguiente:

* El extremo de la URL es el correcto
* Los parámetros añadidos a la URL se corresponden con los añadidos al enlace de atribución de AppsFlyer
* La columna **Mensaje de error de postback** está vacía

</Accordion>

<div data-zendesk-anchors="android-integration-testing=pruebas-de-integraci%C3%B3n-de-android h_01HJR6V0MYJXD4QSRT95SVXTWH=pruebas-de-integraci%C3%B3n-de-android testing=pruebas h_01HJR6V0MYBPC3CSAJTTQSWGAR=pruebas h_01HJR6V0MYG42PPWXT7H2AGTAE=prerequisites h_01HJR6V0MYDRZGQQ74TJWDJ2WS=test-install-attribution supplementary-information-and-procedures=informaci%C3%B3n-y-procedimientos-complementarios h_01HJR6V0MYZ5NG21FEKB4HY6HT=informaci%C3%B3n-y-procedimientos-complementarios h_01HJR6V0MYTZCS097RQP9HG7GY=about-the-partner-integrations-test-app h_01HJR6V0MYVCNVHNCPZ29KRA4K=attribution-link h_01HJR6V0MY6JZXP2NX9YJ9ZY2T=test-app-integrated-in-your-account h_01HJR6V0MYWK7WAAFHRYPCVM7N=troubleshooting h_01HJR6V0MY2SSP17ZEWRM3NXKE=test-retargeting-attribution viewing-retargeted-installs-in-the-dashboard=ver-instalaciones-de-retargeting-en-el-dashboard h_01HJR6V0MYPC0AZF05YF32Z571=ver-instalaciones-de-retargeting-en-el-dashboard h_01HJR6V0MY027J9PKXZZ4TCXRX=test-viewthrough-attribution view-installs-in-the-dashboard=ver-instalaciones-en-el-dashboard h_01HJR6V0MZ4VA3V8CA3PN5Z31K=ver-instalaciones-en-el-dashboard h_01HJR6V0MZCZ3E8NCR6DG6P6P1=raw-data-export h_01HJR6V0MZAHSXCTEZKTVWM96V=verify-postback-data" />
