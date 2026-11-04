---
title: 'Introducción: onboarding de agencias'
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
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
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2026-08-18T00:39:05Z'
  id: 360002381617
  locale: es
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/es/articles/360002381617
---
> **De un vistazo:** Comienza a medir las campañas de tus clientes configurando una cuenta de agencia.

<Embed title="Introducción: onboarding de agencias" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/54qzpj1lm7" providerUrl="https://fast.wistia.com" />


<div id="appsflyer-attribution-model" />

## Modelo de atribución de AppsFlyer

Antes de continuar, es esencial comprender cómo funciona la atribución de AppsFlyer. En esta sección se explica lo que sucede en todo el proceso, desde el primer clic o impresión hasta la atribución de una instalación o un evento, y posterior a ello.

[![ua-flujo-agencia.png](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)

1. Un marketer o una agencia en nombre del marketer configura una campaña con una determinada red de publicidad, utilizando los enlaces de atribución de AppsFlyer.
2. Un usuario hace clic en uno de sus anuncios, por ejemplo, un banner o un enlace de oferta.
3. El enlace de atribución de AppsFlyer detrás del anuncio se llena con la información recopilada durante el clic. Recopilamos la información del enlace de atribución y la almacenamos en nuestra base de datos.
4. Se redirige al usuario a una tienda de aplicaciones.
5. El usuario instala la aplicación y la abre por primera vez. El SDK de AppsFlyer dentro de la aplicación llama a nuestros servidores con la información sobre el dispositivo en el que está instalada la aplicación.
6. Emparejamos estos datos con nuestra base de datos de clics usando nuestros <Anchor target="_blank" href="/marketers/es/docs/appsflyer-attribution-model">métodos de atribución</Anchor>.
7. Si encontramos una coincidencia, atribuimos la instalación al clic. Si no, atribuimos la instalación a una descarga orgánica.
8. Una vez que se atribuye la instalación, la mostramos en los paneles de control y reportes del marketer y la agencia (<Anchor target="_blank" href="/partners/es/docs/about-agency-accounts#redes-publicitarias-de-autoinforme">excepto Anuncios de Meta y X Ads</Anchor>).
9. Luego, enviamos un postback con los detalles de conversión a la red de publicidad, que puede usar esta información para una mayor optimización.

<div id="agency-role-in-mobile-attribution-chain" />

## Rol de la agencia en la cadena de atribución móvil

Un marketer que es propietario de la aplicación integra el SDK de AppsFlyer dentro de ella para cuantificar sus esfuerzos de marketing.

Algunos propietarios de aplicaciones optan por contratar agencias de marketing para ejecutar campañas publicitarias en su nombre. Para hacerlo, la agencia debe tener una cuenta de AppsFlyer y los marketers deben darle a la agencia <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">acceso a sus aplicaciones</Anchor>.

Por lo tanto, la agencia no posee técnicamente las aplicaciones, solo las promociona en los canales de marketing con los que trabaja, sin la participación técnica, como una integración de SDK. Según el conjunto de permisos otorgados por un marketer, una agencia puede tener control sobre una variedad de funciones.

Cuando se atribuye una instalación a un anuncio colocado por una agencia, se muestra en el panel de control de la agencia. El propietario de la aplicación también lo verá y sabrá que se atribuye a la agencia.

Nota: Si tu organización es propietaria de la aplicación o gestiona su desarrollo y marketing, debes abrir una cuenta de marketer.

<div id="pricing" />

## Precios

El alcance de la funcionalidad de una cuenta de agencia depende de los permisos proporcionados por el propietario de la aplicación para cada aplicación. Por lo tanto, las cuentas de agencia se ofrecen **de forma gratuita** y solo los propietarios de aplicaciones pagan por la atribución. Las agencias y los propietarios de aplicaciones pueden usar los datos de atribución de AppsFlyer con fines de compensación.

<div id="getting-started" />

## Primeros pasos

Para configurar una nueva cuenta de agencia:

1. Completa el <Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">formulario de registro</Anchor>.
   * Utiliza el dominio de correo electrónico de tu empresa para el registro.
   * Usa una dirección de correo electrónico que no esté asociada con una cuenta de AppsFlyer existente.
2. Un miembro del equipo de la agencia de AppsFlyer puede contactarte con más información necesaria para completar el registro.
3. Una vez que se active tu cuenta, recibirás una notificación y podrás comenzar a usar AppsFlyer.

<div id="adding-team-members" />

## Agregar miembros al equipo

Cuando tu cuenta esté en funcionamiento, el administrador de la cuenta (la persona que abrió la cuenta) puede agregar más miembros del equipo, quienes pueden tener acceso a algunas o todas las aplicaciones administradas por la agencia. Para saber cómo agregar nuevos miembros al equipo, haz clic aquí.

<div id="adding-apps-to-your-account" />

## Agregar aplicaciones a tu cuenta

Cuando creas tu cuenta por primera vez, esta no tiene aplicaciones asociadas:

![inicio-agencia.png](https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png)

Cualquier individuo o equipo de la agencia requiere permiso del propietario de la aplicación para:

* Obtener acceso al panel de control de la aplicación
* Hacer cambios en la configuración
* Ejecutar campañas

Los marketers <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">proporcionan acceso a cualquier agencia</Anchor> directamente a través de la plataforma. Una vez que tu cuenta esté configurada y hayas obtenido acceso a las aplicaciones, puedes comenzar a ejecutar campañas utilizando las funciones de AppsFlyer.

<div id="what-does-it-mean-to-get-permission-from-a-marketer" />

### Qué significa obtener el permiso de un marketer

Cuando obtienes permiso de un marketer:

* La aplicación aparece en tu cuenta.
* Puedes configurar integraciones con redes de publicidad para la aplicación (con la excepción de algunas redes que requieren configuración por parte del propietario de la aplicación).
* Puedes crear enlaces de atribución para usarlos en tus campañas.
* Puedes configurar integraciones de costos con los partners (que lo permitan).
* Puedes ver los datos de la aplicación.
* Puedes conceder permiso a las redes de publicidad y a los miembros de sus equipos para ver información básica sobre la aplicación.  
    

  <div id="note" />

  > 📘 **Nota**
  >
  > La agencia obtiene el control del interruptor principal de permisos de ad network y de los permisos individuales anidados en él. Tanto la agencia como el anunciante pueden cambiar estos ajustes, y el cambio más reciente de cualquiera de las dos partes determina el estado actual.


Los permisos adicionales incluyen acceso al reporte de cohortes, al panel de control de Protect360 y a datos orgánicos agregados. Consulta una <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-la-agencia">descripción de los distintos permisos de la red publicitaria</Anchor>.

<div id="app-list" />

### Lista de aplicaciones

Una vez que hayas obtenido el permiso del marketer, la aplicación aparecerá en la página de la aplicación.

La página de aplicaciones de tu cuenta enumera hasta 1000 aplicaciones. Si la lista de aplicaciones para las que tienes permisos supera las 1000, algunas aplicaciones no se muestran en la lista. Aún puedes encontrarlas usando la búsqueda.

![aplicaciones-agencia.png](https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png)

<div id="searching-for-apps" />

#### Búsqueda de aplicaciones

1. En tu cuenta, en el menú superior, selecciona **Mis apps**.
2. En el campo de búsqueda, ingresa el término de búsqueda, por ejemplo:
   * Nombre de aplicación
   * ID de aplicación
   * Correo electrónico del propietario de la aplicación

<div id="agency-dashboard" />

## Panel de control de agencia

Haz clic en cualquier aplicación de la lista de aplicaciones para acceder a su <Anchor target="_blank" href="/marketers/es/docs/getting-started-with-appsflyer-dashboards">panel de control</Anchor>. Cuando comienzas a ejecutar campañas, los datos agregados que se te atribuyen se muestran aquí.

![agency-dashboard.png](https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png)

El panel de control de la cuenta de agencia incluye acceso predeterminado a:

* Panel de Control con Información General sobre el Valor de Vida Útil
* Panel de Control de Eventos In-App
* Panel de Control de Retargeting

<div id="running-campaigns" />

## Campañas en ejecución

<div id="self-reporting-networks-srns" />

### Redes de autorreporte (SRN)

Las SRN, también conocidas como redes de autoatribución (SAN), son redes que no requieren el enlace de atribución de AppsFlyer para reportar clics y otros datos, y usan la integración directa con AppsFlyer en su lugar. Algunas de estas redes son <Anchor target="_blank" href="/marketers/es/docs/meta-ads-faq#attributing-agencies-with-facebook">Anuncios de Meta</Anchor>, <Anchor target="_blank" href="/marketers/es/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor>, <Anchor target="_blank" href="/marketers/es/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads</Anchor>, <Anchor target="_blank" href="/marketers/es/docs/snapchat-advanced-srn-integration-setup">Snapchat</Anchor>, DoubleClick, <Anchor target="_blank" href="/marketers/es/docs/apple-ads-integration-setup">Apple Ads Search</Anchor>, <Anchor target="_blank" href="/marketers/es/docs/yahoo-integration-setup">Yahoo</Anchor> y <Anchor target="_blank" href="/marketers/es/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">Yahoo! JAPAN</Anchor>. JAPÓN.

La mayoría de estas redes requieren una configuración especial para las agencias. Por ejemplo, dado que la integración de Anuncios de Meta y X Ads solo puede configurarla el propietario de una aplicación, los nombres de las campañas de la agencia DEBEN comenzar con el nombre de la agencia para asegurarse de que las instalaciones se atribuyan correctamente a la agencia.

Haz clic en los enlaces anteriores para leer las guías de la red y las instrucciones específicas para la configuración de la agencia.

<div id="non-srns" />

### No SRN

La mayoría de las redes de publicidad necesitan enlaces de atribución que se colocan detrás de un anuncio. Lee más sobre cómo ejecutar campañas con ellos <Anchor target="_blank" href="/partners/es/docs/about-agency-accounts#no-srn">aquí</Anchor>.

<div id="sandbox-attribution-agency-campaigns" />

### Campañas de agencia en la atribución de Sandbox

La infraestructura SKAdNetwork, parte de iOS de Apple, permite a los marketers medir el éxito de la campaña sin el identificador de anunciante (IDFA) o el ID de publicidad. Aunque Apple no incluye las agencias como parte del proceso de atribución de SKAdNetwork, y AppsFlyer no puede atribuir las agencias directamente, AppsFlyer todavía tiene la capacidad de proporcionar datos de atribución para las campañas de agencias que se ejecutan en SKAdNetworks.

<div id="campaign-naming" />

#### Introducción: onboarding de agencias

En AppsFlyer, en el menú lateral, selecciona **Configuración** > **Configuración de la App**.

* tu af\_prt (<Anchor target="_blank" href="/partners/es/docs/about-agency-accounts#parámetro-af_prt">Cuál es tu af\_prt y dónde encontrarlo</Anchor>),
* guion bajo,
* el nombre de tu campaña que sigue la convención de denominación de tu agencia.

Si ejecutas campañas en medios que no sean redes de publicidad (redes sociales, correos electrónicos, blogs, SMS), puedes usar <Anchor target="_blank" href="/marketers/es/docs/create-a-onelink-template">enlaces personalizados</Anchor> para ellas.

`Comenzar`

<div id="note-1" />

> 📘 **Nota:**
>
> * Las campañas de agencia en la atribución de Sandbox también son transparentes, y la identidad de la ad network que ejecuta la campaña no queda enmascarada para el profesional de marketing.

<div id="skadnetwork-agency-campaigns" />

### Campañas de agencias de SKAdNetwork

La infraestructura SKAdNetwork, parte de iOS de Apple, permite a los marketers medir el éxito de la campaña sin el identificador de anunciante (IDFA) o el ID de publicidad. Aunque Apple no incluye las agencias como parte del proceso de atribución de SKAdNetwork, y AppsFlyer no puede atribuir las agencias directamente, AppsFlyer todavía tiene la capacidad de proporcionar datos de atribución para las campañas de agencias que se ejecutan en SKAdNetworks.

<div id="campaign-naming-1" />

#### Nombres de las campañas

Para ver tus campañas en el panel de control de AppsFlyer SKAdNetwork, los nombres de las campañas que configures con SKAdNetwork deben incluir tu identificador de partner y estar estructurados de la siguiente manera:

* tu af\_prt (<Anchor target="_blank" href="/partners/es/docs/about-agency-accounts#parámetro-af_prt">Cuál es tu af\_prt y dónde encontrarlo</Anchor>),
* guion bajo,
* el nombre de tu campaña que sigue la convención de denominación de tu agencia.

Si ejecutas campañas en medios que no sean redes de publicidad (redes sociales, correos electrónicos, blogs, SMS), puedes usar <Anchor target="_blank" href="/marketers/es/docs/create-a-onelink-template">enlaces personalizados</Anchor> para ellas.

`Comenzar`

<div id="note-2" />

> 📘 **Nota:**
>
> * Las campañas de agencias en SKAdNetwork siempre son transparentes y la identidad de la red de publicidad que ejecuta la campaña no está enmascarada del marketer. Ten en cuenta que a partir de iOS 15, el marketer (propietario de la aplicación) puede <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">optar por recibir directamente una copia del postback.</Anchor>
> * <mark>Debes pedirle al marketer que habilite la configuración de **activación de partners**</mark> de la red de publicidad en la pestaña de integración. Si no lo haces, la red de publicidad no recibirá los postbacks relacionados con las campañas de SKAN. Nota: Esto es una adición a la configuración de activación de partners a la que puedes acceder en la interfaz de usuario.

<div id="access-to-skan-conversion-studio" />

#### Acceso a SKAN Conversion Studio

Las agencias pueden <Anchor target="_blank" href="/marketers/es/docs/skan-conversion-studio#view-cv-mapping">ver y descargar</Anchor> la configuración de asignación de CV de SKAN de un marketer en <Anchor target="_blank" href="/marketers/es/docs/skan-conversion-studio#aspectos-básicos-del-skan-conversion-studio">Conversion Studio</Anchor>, pero no pueden configurar o editar los ajustes.

<div id="skadnetwork-dashboard" />

#### Panel de control de SKAdNetwork

<Embed title="Introducción: onboarding de agencias" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**Lectura adicional:**

* <Anchor target="_blank" href="/marketers/es/docs/about-att-and-skan">Guía de inicio rápido de SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/es/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">Panel de control de SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/es/docs/skadnetwork-skan-solution-guide">Solución SKAdNetwork</Anchor>

<div id="single-source-of-truth-ssot-for-agencies" />

### Fuente única de verdad (SSOT) para agencias

La SSOT unifica todos los métodos de atribución combinando datos de atribución de diferentes modelos y eliminando las instalaciones duplicadas y las métricas asociadas a costos e ingresos. De esta manera, el eCPI, ROI y ROAS, por ejemplo, se calculan correctamente.

Las agencias pueden acceder a los datos de SSOT en el panel de control general, pero no a través de la API.

Para incluir el indicador SSOT en tu panel de control, el marketer debe activar SSOT en el Conversion Studio.

**Lectura adicional:**

* <Anchor target="_blank" href="/marketers/es/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Guía de la Única fuente de verdad (SSOT) para la atribución de iOS</Anchor>

<div id="what-else-you-can-do" />

## Qué más puedes hacer

* Medir la retención de usuarios
* Usar eventos in-app para optimizar tus campañas
* Ejecutar campañas de <Anchor target="_blank" href="/marketers/es/docs/retargeting-attribution-guide">retargeting</Anchor>
* Exportar tus <Anchor target="_blank" href="/marketers/es/docs/manage-data-access-permissions">datos</Anchor>
* <Anchor target="_blank" href="/marketers/es/docs/registering-test-devices">Registrar tu dispositivo de prueba</Anchor>
* y más.

Puedes encontrar más información sobre el uso avanzado de la cuenta de agencia <Anchor target="_blank" href="/partners/es/docs/about-agency-accounts#agency-setting-up-campaigns">aquí</Anchor>.

¿Te topaste con un término desconocido? Encuéntralo en nuestro <Anchor target="_blank" href="/marketers/es/docs/appsflyer-knowledge-base-glossary">Glosario</Anchor>.

¿Tienes una pregunta técnica urgente? Busca en nuestro Centro de ayuda: probablemente tengamos una respuesta. Si no es así, ponte en contacto con nuestro equipo de soporte en la esquina inferior derecha de tu panel de control.

<div data-zendesk-anchors="appsflyer-attribution-model=modelo-de-atribuci%C3%B3n-de-appsflyer h_01HFXXKCMW7EREMC7KEYTF3ERH=modelo-de-atribuci%C3%B3n-de-appsflyer h_01KZTW5D6QWFP2Z3J31M9B6QKR=modelo-de-atribuci%C3%B3n-de-appsflyer agency-role-in-mobile-attribution-chain=rol-de-la-agencia-en-la-cadena-de-atribuci%C3%B3n-m%C3%B3vil h_01HFXXKCMW987FV2PB4EPXH92Z=rol-de-la-agencia-en-la-cadena-de-atribuci%C3%B3n-m%C3%B3vil pricing=precios h_01HFXXKCMWPN6AN98A5RD5YXW7=precios getting-started=primeros-pasos h_01HFXXKCMWRXVBYTW9RYEX7X8F=primeros-pasos adding-team-members=agregar-miembros-al-equipo h_01HFXXKCMWB6ZG3PSHDSETC4XC=agregar-miembros-al-equipo adding-apps-to-your-account=agregar-aplicaciones-a-tu-cuenta h_01HFXXKCMWBZVTHAEKED1Q27M3=agregar-aplicaciones-a-tu-cuenta what-does-it-mean-to-get-permission-from-a-marketer=qu%C3%A9-significa-obtener-el-permiso-de-un-marketer h_01HFXXKCMWYNNZWTKP9KEQ4VCD=qu%C3%A9-significa-obtener-el-permiso-de-un-marketer h_01JV9KR17EEHA6F2F8J13AEZEV=nota app-list=lista-de-aplicaciones h_01HFXXKCMWKW78TMC76F40PY2C=lista-de-aplicaciones searching-for-apps=b%C3%BAsqueda-de-aplicaciones h_01HFXXKCMW8S93N577393QZTYX=b%C3%BAsqueda-de-aplicaciones agency-dashboard=panel-de-control-de-agencia h_01HFXXKCMWPZVADY15DKATJ7Z4=panel-de-control-de-agencia running-campaigns=campa%C3%B1as-en-ejecuci%C3%B3n h_01HFXXKCMWFB9RXY7AVBX5CGB9=campa%C3%B1as-en-ejecuci%C3%B3n selfreporting-networks-srns=redes-de-autorreporte-srn h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=redes-de-autorreporte-srn nonsrns=no-srn h_01HFXXKCMWPAMZ373D5AVD5EJF=no-srn sandbox-attribution-agency-campaigns=campa%C3%B1as-de-agencia-en-la-atribuci%C3%B3n-de-sandbox h_01J6PCDYM2W1X6EMMEE7SFB3VE=campa%C3%B1as-de-agencia-en-la-atribuci%C3%B3n-de-sandbox campaign-naming=introducci%C3%B3n-onboarding-de-agencias h_01HFXXKCMWMW1AHXMS19CYD4VC=introducci%C3%B3n-onboarding-de-agencias h_01HFXXKCMWEQ41A7TZ2K6DE424=nota-1 skadnetwork-agency-campaigns=campa%C3%B1as-de-agencias-de-skadnetwork h_01HFXXKCMWZ19E0QR1VE977BTS=campa%C3%B1as-de-agencias-de-skadnetwork 01J6PCG6JGY2R8T5DDCR8APM66=nombres-de-las-campa%C3%B1as 01J6PCG6JHK9TGX93SD4DRP393=nota-2 access-to-skan-conversion-studio=acceso-a-skan-conversion-studio h_01HFXXKCMWX53HMRG2ZTD9FYQE=acceso-a-skan-conversion-studio skadnetwork-dashboard=panel-de-control-de-skadnetwork h_01HFXXKCMW1HHMSS3XAXJKME29=panel-de-control-de-skadnetwork single-source-of-truth-ssot-for-agencies=fuente-%C3%BAnica-de-verdad-ssot-para-agencias h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=fuente-%C3%BAnica-de-verdad-ssot-para-agencias what-else-you-can-do=qu%C3%A9-m%C3%A1s-puedes-hacer h_01HFXXKCMXQ2JT63GBMC74PWBA=qu%C3%A9-m%C3%A1s-puedes-hacer" />
