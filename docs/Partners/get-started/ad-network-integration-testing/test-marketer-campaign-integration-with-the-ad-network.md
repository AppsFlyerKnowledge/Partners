---
title: Probar la integración de la campaña de marketing con la ad network
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
  created_at: '2021-12-08T04:41:04Z'
  edited_at: '2026-08-12T12:28:59Z'
  id: 4413093220113
  locale: es
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/es/articles/4413093220113
---
> **Resumen**: prueba la integración con la ad network usando aplicaciones de marketing.

<div id="prerequisites" />

## Prerrequisitos

Antes de que puedas empezar a probar la integración de marketing con tu ad network, hay algunos requisitos:

* Dispositivos en la allowlist: debes pedir al marketer que incluya en la <Anchor target="_blank" href="/marketers/es/docs/registering-test-devices">allowlist</Anchor> cualquier dispositivo que uses para la prueba
* La aplicación debe incluir el SDK de AppsFlyer
* Si la aplicación no está publicada en Google Play o en la tienda de aplicaciones de iOS, debes pedir al marketer que te proporcione la aplicación
* Tanto si la aplicación está publicada como si no, debe estar <Anchor target="_blank" href="/marketers/es/docs/adding-an-app-to-appsflyer">en la cuenta de AppsFlyer del marketer</Anchor>

<div id="getting-started" />

## Primeros pasos

Abre tu Dashboard de AppsFlyer. En la pantalla **App search**, introduce el ID de la aplicación del marketer:

<div id="example" />

> 📄 **Ejemplo**
>
> Android - **com.example.app**
>
> iOS- **id1234123412**

Cuando aparezca la marca de verificación verde en el campo de entrada, haz clic en la flecha azul. Al hacer clic en la flecha, se abre el Dashboard de la aplicación.

[![partner-app-search.png](https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png)](https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png)

<div id="testing-live-apps" />

## Prueba de aplicaciones en producción

En el Dashboard de AppsFlyer de tu aplicación, selecciona **Active integrations** en el menú lateral. Elige tu ad network y haz clic en **Attribution link**.

<div id="important" />

> 🚧 **Dos puntos (:)**
>
> Si las opciones de **Attribution link** aparecen atenuadas, pide al marketer que <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions-tab">habilite los permisos de la ad network</Anchor>. Los permisos necesarios son **Allow to configure integration** y **Allow to configure in-app events postbacks**.
>
> También puedes pedir al marketer que te proporcione el enlace de atribución.

<div id="installing-the-app-through-the-attribution-link" />

<Accordion title="Instalar la aplicación mediante el enlace de atribución">

Ahora puedes generar un enlace de atribución para probar la atribución de la instalación.

Añade parámetros al enlace de atribución según tus necesidades y los datos que quieras registrar.

[![partner-configure-attribution-link.png](https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png)](https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png)

<div id="tip" />

> 👍 **Consejo**
>
> Para obtener más información sobre los parámetros que puedes añadir al enlace de atribución, consulta <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">la estructura y los parámetros del enlace de atribución de AppsFlyer</Anchor>.

</Accordion>

<div id="testing-install-attribution" />

<Accordion title="Probando la atribución de instalaciones">

Envía el enlace de atribución al dispositivo de prueba. Abre el enlace en el navegador, instala la aplicación y ejecútala.

Iniciar la aplicación es fundamental para el flujo de atribución. Si no se inicia la aplicación, no se registra ninguna atribución.

Después, puedes [ver la instalación en tu dashboard](/docs/test-marketer-campaign-integration-with-the-ad-network#ver-instalaciones-en-el-dashboard).

</Accordion>

<div id="testing-apps-in-development" />

## Prueba de aplicaciones en desarrollo

Puedes probar la integración de la campaña de un marketer con tu ad network aunque la aplicación aún no esté en vivo. Sin embargo, tienes que pedirle al marketer que te proporcione la aplicación (un archivo .apk o .ipa) para que puedas instalarla en tus dispositivos de prueba.

<div id="generate-an-attribution-link" />

<Accordion title="Generar un enlace de atribución">

Genera un enlace de atribución. Puedes usar las [mismas instrucciones indicadas arriba](/docs/test-marketer-campaign-integration-with-the-ad-network#installing-the-app-through-the-attribution-link). Envía el enlace de atribución al dispositivo de prueba y ábrelo con el navegador del dispositivo.

Aparecerá la siguiente pantalla:

[![app-not-available.png](https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png)](https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png)

Este es el resultado esperado. Dado que la aplicación no está activa, el enlace de atribución no conduce a ninguna tienda de aplicaciones. Sin embargo, el enlace de atribución sigue siendo válido para fines de atribución. el enlace de atribución y sus parámetros se registran en los servidores de AppsFlyer y los datos se usan para la atribución.

</Accordion>

<div id="installing-the-app" />

<Accordion title="Instalación de la aplicación">

Instala la aplicación en el dispositivo de prueba con el archivo que te proporcione el marketer y, luego, ejecútala. Elimina la aplicación y repite el proceso (para generar varias instalaciones). Después, puedes [ver las instalaciones en tu dashboard](/docs/test-marketer-campaign-integration-with-the-ad-network#ver-instalaciones-en-el-dashboard).

</Accordion>

<div id="testing-in-app-events" />

## Probando eventos in-app

<div id="note" />

> 📘 **Advertencia**
>
> Puedes probar los postbacks de eventos in-app tanto en aplicaciones publicadas como en aplicaciones en desarrollo.

Antes de poder probar los postbacks de eventos in-app, debes ponerte en contacto con el marketer para saber qué tipos de eventos in-app registra y cómo puedes activarlos desde la aplicación.

<div id="mapping-events" />

<Accordion title="Asignación de eventos">

Si el marketer ha habilitado el permiso <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">**Configurar postbacks de eventos in-app**</Anchor> en la configuración de integración de tu ad network, puedes asignar eventos de AppsFlyer a los eventos que registras en tus servidores.

En el dashboard de AppsFlyer de tu aplicación, selecciona **Active integrations** en el menú lateral y elige tu ad network. En la pestaña **Integración**, desplázate hacia abajo hasta **In-app event settings**. Elige el evento in-app y asígnalo al evento correspondiente:

[![partner-mapping-de-postbacks-de-eventos-in-app.png](https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png)](https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png)

</Accordion>

<div id="triggering-inapp-events" />

<Accordion title="Activar eventos in-app">

Cuando sepas qué eventos in-app registra el anunciante y el mapeo de eventos esté configurado, activa algunos eventos desde la aplicación instalada.

<div id="note-1" />

> 📘 **Advertencia**
>
> Las ad networks no tienen acceso al Dashboard de eventos y solo pueden ver los eventos in-app en el Dashboard general después de que el anunciante habilite el **Acceso a los datos agregados de eventos in-app** <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permissions-tab">permiso de ad network</Anchor>. Sin embargo, you can export in-app event-related data from the [In-app events postback](/docs/test-marketer-campaign-integration-with-the-ad-network#verificar-datos-de-postback) report.

En el reporte de postbacks de eventos in-app, puedes encontrar datos como la URL del postback y los parámetros mapeados. Usa los datos del reporte y compáralos con los datos de tus servidores (del postback) para asegurarte de que los datos de los postbacks sean correctos y tus servidores los registren adecuadamente.

Después de exportar el reporte de postbacks de eventos in-app, puedes revisarlo para verificar lo siguiente:

1. El evento se te atribuye como ad network en el campo **fuente de medios**
2. El nombre del evento es correcto en el campo **Nombre del evento**
3. El postback, si está habilitado, contiene el nombre y el valor del evento en el campo **URL del postback**
4. Los eventos in-app están mapeados correctamente en el campo **URL del postback**

</Accordion>

<div id="viewing-installs-in-the-dashboard" />

## Ver instalaciones en el dashboard

Cuando instales y abras la aplicación, podrás ver los resultados en tu dashboard.

<div id="important-1" />

> 🚧 **Dos puntos (:)**
>
> Para generar varias instalaciones, [el dispositivo debe estar en la lista de permitidos](/docs/test-marketer-campaign-integration-with-the-ad-network#prerrequisitos).

Accede a tu dashboard de AppsFlyer y, en el menú lateral, selecciona **Análisis** >  **General**.

Filtra por tu ad network. Puedes ver el número de clics e instalaciones que se atribuyen a tu ad network.

Los datos relacionados con clics e instalaciones aparecen en la parte superior de la pantalla **General**. La pantalla **General** también incluye **Desglose por campaña** y **Reporte de rendimiento agregado**. Verifica que las campañas que aparecen en estas secciones se correspondan con el parámetro de campaña del enlace de atribución.

<div id="verifying-postback-data" />

## Verificar datos de postback

Cada instalación que se atribuye a tu ad network genera un postback de instalación. Si los postbacks de eventos in-app están habilitados, los eventos procedentes de una aplicación cuya instalación se atribuye a tu ad network también generan postbacks.

Abre la <Anchor target="_blank" href="/marketers/es/docs/raw-data-export-page">página de exportación de raw data</Anchor> y genera 2 reportes de postback:

1. **Instalaciones asistidas**
2. **Eventos dentro de la aplicación**

Ambos reportes contienen una columna titulada **URL de Postback**. Esta columna enumera las URL de postback de instalaciones o eventos in-app (según el tipo de reporte).

Revisa los datos de esa columna para verificar lo siguiente:

* El endpoint de la URL es el correcto
* Los parámetros añadidos a la URL se corresponden con los añadidos al enlace de atribución de AppsFlyer
* En los postbacks de eventos in-app, los eventos están correctamente asignados; por ejemplo:  
  `sdk_event=af_purchase&mapped-event=purchase`  
  `sdk_event=af_login&mapped-event=login`
* La columna **Mensaje de error de postback** está vacía

<div data-zendesk-anchors="prerequisites=prerrequisitos h_01HKA1DE8VKXM92D7S5BANFZJ4=prerrequisitos getting-started=primeros-pasos h_01HKA1DE8V9A9AJWYQR9VJQ0H8=primeros-pasos h_01HKA1DE8VA7HAM8BT3KZ8HYGP=ejemplo testing-live-apps=prueba-de-aplicaciones-en-producci%C3%B3n h_01HKA1DE8V0J2Y8DQ60J9S5DAK=prueba-de-aplicaciones-en-producci%C3%B3n h_01HKA1DE8VDQGKYSYFDF5K2HSX=dos-puntos- h_01HKA1DE8VEEH8YE1QT28QVFZQ=installing-the-app-through-the-attribution-link h_01HKA1DE8VV0K8J2AG7W0FDDWY=consejo h_01HKA1DE8VEH7S0JAJTJ91KE7X=testing-install-attribution testing-apps-in-development=prueba-de-aplicaciones-en-desarrollo h_01HKA1DE8VK9RQGQ8BCG157H1Y=prueba-de-aplicaciones-en-desarrollo h_01HKA1DE8VSPE0FFM65AFQRJ8S=generate-an-attribution-link h_01HKA1DE8V68Z5CM4EF7YBPHPS=installing-the-app testing-inapp-events=probando-eventos-in-app h_01HKA1DE8VVJXK11BM77D3YWA5=probando-eventos-in-app h_01HKA1DE8W2VT648E022BHJP0K=advertencia h_01HKA1DE8WQVGPSTG2SQCM2BQW=mapping-events h_01HKA1DE8WRZPCX3GGV01ZK10K=triggering-inapp-events h_01HKA1DE8W8XXM4BK7843TAEJQ=advertencia-1 viewing-installs-in-the-dashboard=ver-instalaciones-en-el-dashboard h_01HKA1DE8WY7VCST4XDN1HWGC7=ver-instalaciones-en-el-dashboard h_01HKA1DE8WYRTTNC2Q0VGKMM82=dos-puntos--1 verifying-postback-data=verificar-datos-de-postback h_01HKA1DE8WEQY58XAPS9MBNGKE=verificar-datos-de-postback" />
