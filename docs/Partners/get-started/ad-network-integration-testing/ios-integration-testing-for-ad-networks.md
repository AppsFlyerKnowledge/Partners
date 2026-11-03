---
title: iOS integration testing for ad networks
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
  created_at: '2020-12-16T11:39:36Z'
  edited_at: '2026-08-12T12:28:57Z'
  id: 360016588278
  locale: es
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/es/articles/360016588278
---
> **De un vistazo:** Prueba la integración de AppsFlyer para iOS con la aplicación AppsFlyer Partner Integrations para activar postbacks normales y de Advanced Privacy.

## iOS integration testing

Las pruebas constan de los siguientes elementos:

* Usa la versión para iOS de la aplicación AppsFlyer Partner Integrations para generar eventos in-app de instalación y compra de prueba. Estas pruebas, a su vez, activan postbacks que se envían a tus endpoints. También tienes la opción de probar eventos in-app de login y registro.
* Cuando recibas los postbacks, verifica que puedas ingerirlos.

### Alcance de las pruebas

Los anunciantes controlan los datos que se comparten con ad network mediante la configuración de Advanced Privacy. Esta configuración, junto con la configuración de <Anchor target="_blank" href="/marketers/es/docs/att-implications-ios-14-and-deprecation-of-lat">ATT</Anchor> del usuario de la aplicación, afecta al tipo de postback y a los datos compartidos con ad network, tal como se describe en la <Anchor target="_blank" href="/partners/es/docs/advanced-privacy-guide-postback-macros-for-ad-networks">guía de postback de Advanced Privacy</Anchor>. La siguiente tabla enumera los escenarios de prueba según las combinaciones de configuración disponibles.

Para cada escenario, puedes probar instalaciones y eventos in-app. En cuanto a los eventos in-app, puedes usar el <Anchor target="_blank" href="/partners/es/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">mapeo de eventos in-app</Anchor> para asignar los eventos del anunciante a tus eventos.

#### Combinaciones de escenarios de prueba

| Situación | Configuración de privacidad avanzada | Configuración de ATT en la aplicación | Tipo de postback enviado |
| --- | --- | --- | --- |
| A | Desactivado | Permitir | Regular |
| B | en | Pedir a la aplicación que no rastree | Privacidad Avanzada |

## Pruebas

Completa los requisitos previos y luego realiza los procedimientos de prueba de las secciones siguientes. Cada una de las secciones de prueba contiene una tabla que puedes usar para registrar los resultados de las pruebas.

<div id="prerequisites" />

<Accordion title="Prerrequisitos">

Completa los requisitos previos antes de empezar a ejecutar el procedimiento de prueba.

| Prerrequisitos |
| --- |
| <Anchor target="_blank" href="/partners/es/docs/getting-started-onboarding-guide-for-ad-networks#parte-1-integración-y-pruebas">Completa la integración estándar con AppsFlyer.</Anchor> Si es necesario, ponte en contacto con AppsFlyer mediante el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente de partners</Anchor>. |
| <Anchor target="_blank" href="/partners/es/docs/self-serve-integration-management-for-ad-networks#postbacks-de-privacidad-avanzada-y-skan">Completa la integración de privacidad avanzada con AppsFlyer.</Anchor> Si es necesario, ponte en contacto con AppsFlyer mediante el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente de Partners</Anchor>. |
| <Anchor target="_blank" href="/partners/es/docs/turn-on-test-app-integration-for-ad-networks">Integra la aplicación de prueba de iOS en tu cuenta.</Anchor> |
| [Verifica que la aplicación de prueba esté integrada en tu cuenta](/docs/ios-integration-testing-for-ad-networks#test-app-integrated-in-your-account) |
| <Anchor target="_blank" href="/partners/es/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Asigna los eventos in-app a tus nombres de evento</Anchor>. Nombres de eventos que se deben asignar: `purchase`, `login`, `registration` |
| [Prepara el enlace de atribución](/docs/ios-integration-testing-for-ad-networks#attribution-link) |
| Haz la prueba con un dispositivo que ejecute iOS 14.5+ |

</Accordion>

<div id="test-advanced-privacy-off" />

<Accordion title="Prueba: privacidad avanzada desactivada">

**Para activar los postbacks:**

1. En el Dashboard de AppsFlyer, configura [Enable Advanced Privacy](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy) en desactivado.
2. En el dispositivo:
   1. Verifica que la aplicación de prueba no esté instalada. Elimínala si es necesario.
   2. En los ajustes de privacidad, verifica que **Allow Apps to Request to Track** esté activado.  

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Envía el enlace de atribución al dispositivo de prueba.
4. Abre el enlace de atribución en el navegador del dispositivo.  
   Se te redirige a la tienda de aplicaciones.
5. Descarga y abre la aplicación.  
   Se muestra el cuadro de diálogo de consentimiento de ATT.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Toca **Permitir**.  
   Se muestra la página **Datos de instalación**.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Toca **ATT Status**.  
   Se muestra el estado **Authorized**.
8. Valida la atribución con los siguientes parámetros. Si la validación falla, consulta [Solución de problemas](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: cerca de la hora actual. La hora está en UTC.
   2. `af_status: Non-organic` Si no es así, la instalación no se atribuyó.
   3. `media_source`: tu ad network
9. Toca **In-App Event Tests.**

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Toca **Purchase Event.**  
    Se muestra la confirmación de Purchase Event.
11. Verifica que:
    1. Has recibido los postbacks de instalación y compra.
    2. El nombre del evento está asignado correctamente (si has asignado eventos in-app).
    3. Puedes procesar el postback.

#### Privacidad avanzada desactivada: resultados de la prueba

| Postback | Hora a la que activaste el evento | Tipo de postback esperado | Postback real recibido (aprobado/no aprobado) | Validación del postback (aprobado/no aprobado) |
| --- | --- | --- | --- | --- |
| Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |  | Regular |  |  |
| Evento in-app: Purchase |  | Regular |  |  |

</Accordion>

<div id="test-advanced-privacy-on" />

<Accordion title="Prueba: Privacidad avanzada activada">

**Para activar postbacks:**

1. En el Dashboard de AppsFlyer, configura [Enable Advanced Privacy](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy) como activado.
2. En el dispositivo:
   1. Verifica que la app de prueba no esté instalada. Elimínala si es necesario.
   2. En los ajustes de privacidad, verifica que **Permitir que las apps soliciten realizar un seguimiento** esté activado.

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Envía el enlace de atribución al dispositivo de prueba.
4. Abre el enlace de atribución en el navegador del dispositivo.  
   Se te redirige a la tienda de aplicaciones.
5. Descarga y abre la aplicación.  
   Aparece el cuadro de diálogo de consentimiento de ATT.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Toca **Pedir a la app que no haga track.** Se muestra la página **datos de instalación**.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Toca **ATT Status**.  
   Se muestra el estado **Denied**.
8. Valida la atribución mediante los parámetros indicados. Si la validación falla, consulta [Solución de problemas](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: cerca de la hora actual. La hora está en UTC.
   2. `af_status: Non-organic` Si no es así, la instalación no se ha atribuido.
   3. `media_source`: tu Ad network
9. Toca **Pruebas de eventos in-app.**

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Toca **Evento de compra.**
11. Verifica que:
    1. Has recibido postbacks de instalación y compra.
    2. El nombre del evento está asignado correctamente (si has asignado eventos in-app).
    3. Puedes procesar el postback.

#### Privacidad Avanzada activada: resultados de la prueba

| Postback | Hora a la que activaste el evento | Tipo de postback esperado | Postback real recibido (correcto/incorrecto) | Validación del postback (correcto/incorrecto) |
| --- | --- | --- | --- | --- |
| Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |  | Privacidad Avanzada |  |  |
| Evento in-app: compra |  | Privacidad Avanzada |  |  |

</Accordion>

## Información y procedimientos complementarios

<div id="about-the-partner-integrations-test-app" />

<Accordion title="Acerca de la aplicación de prueba Partner Integrations">

La aplicación Partner Integrations está disponible en la tienda de aplicaciones. La aplicación envía instalaciones y eventos in-app a la plataforma AppsFlyer.

Cuando se abre la aplicación por primera vez, se muestra el cuadro de diálogo de iOS **request to track** y, a continuación, aparece la página **Install Data**, que muestra los datos de conversión registrados en la plataforma AppsFlyer. Los eventos in-app de prueba se activan en la interfaz de usuario.

[<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)

Las siguientes funciones están disponibles:

* **Pruebas de eventos in-app**Envía `purchase`, `login` y `registration`, además de eventos in-app. Al asignar los nombres de los eventos in-app de la aplicación a tus nombres de evento, los postbacks se completan con tus nombres de evento.
* **Estado de ATT**Devuelve el estado actual de ATT que iOS reporta como **Authorized** o **Denied**. El estado de ATT depende del consentimiento del usuario para el track en el cuadro de diálogo de consentimiento de ATT y del ajuste del dispositivo **Allow Apps to Request to Track**.

</Accordion>

<div id="attribution-link" />

<Accordion title="Enlace de atribución">

Prepara un enlace de atribución en el Dashboard de AppsFlyer mediante uno de los siguientes métodos:

* Genera el enlace en el Dashboard de AppsFlyer.
* Edita el enlace de ejemplo que aparece a continuación.

**Para generar un enlace en el Dashboard:**

1. En AppsFlyer, ve a **My Apps**.
2. Selecciona **id1543229303**.
3. En el menú lateral, selecciona **Collaborate** > **Active Integrations** > selecciona tu ad network > pestaña **Attribution link**.
4. En la pestaña Attribution link, configura los parámetros indicados. Puedes añadir parámetros adicionales si es necesario. 

| Parámetro | Valor de ejemplo | Nota |
| --- | --- | --- |
| Apps asociadas que pertenecen a una plantilla OneLink relacionada para atribución multiplataforma | c-test-2020-12-20 | Establece un valor que puedas identificar en tus postbacks |

5. Copia el enlace resultante para usarlo más adelante.

**Enlace de atribución de ejemplo:**

```http
https://app.appsflyer.com/id1543229303?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="set-advanced-privacy" />

<Accordion title="Configurar privacidad avanzada">

<Image alt="AdvancedPrivacyOff.png" src="https://files.readme.io/ef845ea74cbaa0d3214e61c6e2229fd4b9026d0e221b19fecb9e3486e9b795eb-360014980157.png" width="357px" />

**Para cambiar la configuración de Enable Advanced Privacy:**

1. En AppsFlyer, ve a **My Apps**.
2. Selecciona la aplicación id1543229303.
3. En el menú lateral, selecciona **Collaborate** > **Active Integrations** > selecciona tu ad network > **Integration** pestaña.
4. Configura **Enable Advanced Privacy** con la opción adecuada para cada escenario de prueba.
5. Haz clic en **Guardar integración**.

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Aplicación de prueba integrada en tu cuenta">

**Para verificar que la aplicación de prueba está disponible en tu cuenta:**

1. En AppsFlyer, ve a **My Apps**.
2. Verifica que la aplicación **Partner Integrations id1543229303** aparezca en Available Apps. Si no es el caso, ponte en contacto con tu Partner Development Manager.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Solución de problemas">

| Síntoma | Causa/acción correctiva |
| --- | --- |
| La hora de instalación no es la hora actual | La aplicación no se eliminó antes de la instalación.<br /><br />Elimina la aplicación y repite el procedimiento. |
| La fuente de medios no es tu fuente de medios | Verifica que has establecido el valor correcto de **pid** en el enlace de atribución. Verifica que estás usando el enlace de atribución correcto |
| af\_status es orgánico | Comprueba que la versión de iOS del dispositivo se ajusta a la indicada en los requisitos previos.<br /><br />Comprueba el formato del enlace de atribución, especialmente el valor de **pid**. |

</Accordion>

<div data-zendesk-anchors="h_01HJR5YDW9ENA1B1AC1DQVX8SF=ios-integration-testing testing-scope=alcance-de-las-pruebas h_01HJR5YDW92MXP9DDBX9C1928V=alcance-de-las-pruebas test-scenario-combinations=combinaciones-de-escenarios-de-prueba h_01HJR5YDW9Q7B10MXB1V4AKH2D=combinaciones-de-escenarios-de-prueba testing=pruebas h_01HJR5YDW9AGY148E1ZD97JFRB=pruebas h_01HJR5YDW9SGN9KH63CPZ54RM5=prerequisites test%E2%80%94advanced-privacy-off=test-advanced-privacy-off h_01HJR5YDWA20EQT5RE1EJ7QK2X=test-advanced-privacy-off advanced-privacy-off%E2%80%94test-results=privacidad-avanzada-desactivada-resultados-de-la-prueba h_01HJR5YDWAEAR22NPXF8ZD5QX6=privacidad-avanzada-desactivada-resultados-de-la-prueba test%E2%80%94advanced-privacy-on=test-advanced-privacy-on h_01HJR5YDWAY6B55BFQ1B0WJEHR=test-advanced-privacy-on advanced-privacy-on%E2%80%94test-results=privacidad-avanzada-activada-resultados-de-la-prueba h_01HJR5YDWAK3DZ1Q0W3TSR7ZKZ=privacidad-avanzada-activada-resultados-de-la-prueba supplementary-information-and-procedures=informaci%C3%B3n-y-procedimientos-complementarios h_01HJR5YDWA74Q46F6XKY5J375C=informaci%C3%B3n-y-procedimientos-complementarios h_01HJR5YDWASJWC1NGNABWR1VW5=about-the-partner-integrations-test-app h_01HJR5YDWA0WXWN5B5VNPK40FY=attribution-link h_01HJR5YDWA73BQB478D6N0R8GP=set-advanced-privacy h_01HJR5YDWAGZ5XMQJG1KX3J6CP=test-app-integrated-in-your-account h_01HJR5YDWAXRD7DVHTZPJCFM56=troubleshooting" />
