---
title: Gestión de la integración de autoservicio para redes de publicidad
metadata:
  keywords:
    - postbacks
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
  created_at: '2021-03-15T10:03:41Z'
  edited_at: '2026-08-22T00:38:06Z'
  id: 360018512658
  locale: es
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/es/articles/360018512658
---
> **En resumen:** Configura y administra tu integración desde el panel de control de AppsFlyer.

<Embed title="Gestión de la integración de autoservicio para redes de publicidad" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/9kvwrhnzjo" providerUrl="https://fast.wistia.com" />

## **Pré-requisitos:**

* Debes disponer de credenciales de inicio de sesión (nombre de usuario y contraseña) para AppsFlyer antes de poder administrar enlaces de atribución y postbacks. Para <Anchor target="_blank" href="/partners/es/docs/getting-started-onboarding-guide-for-ad-networks">crear una cuenta de partner</Anchor>, pídele a un cliente de AppsFlyer (anunciante) que <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#invita-a-nuevos-partners-a-appsflyer">te invite</Anchor>.
* La gestión de enlaces de atribución y postbacks predeterminadas está disponible solo para los partners que se unieron después del 1 de febrero de 2022.
* Verifica que tus servidores estén listos para recibir postbacks cumpliendo con lo siguiente:
  * Agrega a la lista de permitidos las <Anchor target="_blank" href="/marketers/es/docs/appsflyer-server-ip-address-ranges-allowlisting">direcciones IP</Anchor> de los servidores de AppsFlyer en tus firewalls y sistemas de seguridad para garantizar la comunicación con tus puntos de conexión.
  * Versiones de TLS: TLS 1.1, TLS 1.2+ con los <Anchor target="_blank" href="/marketers/es/docs/appsflyer-https-ssl-encryption-policy-support#mensajes-salientes-appsflyer-como-cliente">cifrados enumerados.</Anchor>
  * Puertos: 80, 443
* ![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Solo los usuarios administradores pueden acceder y administrar esta sección.

## Acceso a la gestión de integraciones

1. Inicia sesión en tu cuenta de partner de AppsFlyer.
2. Haz clic en el menú desplegable de la parte superior derecha > **Administración de postbacks**.

## Enlace de atribución

El enlace de atribución es la parte más importante de tu integración. Los enlaces de atribución se utilizan para notificar a AppsFlyer sobre el engagement del usuario con un anuncio. Los enlaces de atribución se colocan detrás de los anuncios, de modo que cuando un usuario hace clic en un anuncio, hace clic en un enlace de atribución.

Es obligatorio completar la configuración del enlace de atribución.

**Para configurar el enlace de atribución:**

1. En la pestaña **Enlace de atribución**, agrega los parámetros que se incluirán en tu enlace de atribución:

   * **Nombre de parámetro**: nombre de pantalla del parámetro AppsFlyer.
   * **Tu macro**: agrega la macro que completa los parámetros con valores.
   * **Incluir**: marca la casilla para incluir el parámetro en el enlace.

   > 🚧 **¡Importante!**
   >
   > * Agrega parámetros relacionados con la campaña y los anuncios para proporcionar datos más sólidos sobre el rendimiento de la campaña.
   > * El **ID del sitio** es un parámetro obligatorio.
   > * Los anunciantes utilizan este enlace como base para la integración de una aplicación específica y pueden agregarle parámetros adicionales.
   > * El ID de aplicación, la duración de la ventana retrospectiva y tu ID de partner se agregan al enlace automáticamente y no es necesario agregarlos a esta plantilla.

2. **[Opcional]** Agrega parámetros personalizados que no proporcione AppsFlyer.
3. Usa la vista previa del enlace para verificar que todo esté correcto.
4. Haz clic en **Guardar**.

<Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">Más información sobre enlaces de atribución y parámetros disponibles</Anchor>.

Si tienes algún problema, ponte en contacto con nosotros a través del <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.

## Postback predeterminado

Los postbacks son URL que contienen macros completadas por AppsFlyer y enviadas a tus servidores en tiempo real después de cada conversión (ya sea en tu red o también en otras redes, dependiendo de tu configuración).

**Para configurar el postback predeterminado:**

1. Introduce las **direcciones de los puntos de conexión.** Estos son los puntos de conexión a los que se envían los postbacks. Introduce las URL relevantes para instalaciones, eventos in-app o ambos. Para poder activar la integración, se requiere al menos la URL de postback de instalación.
2. Agrega parámetros al postback:

   * **Nombre de parámetro**: nombre de pantalla del parámetro AppsFlyer.
   * **Tu parámetro de recepción**: el parámetro de recepción respectivo de tu lado.
   * **Valor de parámetro** (disponible para algunos parámetros): elige el formato del valor. Por ejemplo, para los valores booleanos, elige si deseas recibirlos como "true"/"false" o 1/0.
   * **Instalación**: marca la casilla para incluir el parámetro en el postback de instalación.
   * **Evento in-app**: marca la casilla para incluir el parámetro en el postback de evento in-app.

   <Anchor target="_blank" href="/partners/es/docs/postback-macros-for-ad-networks">Lista completa de macros de postback</Anchor>

   > 🚧 **¡Importante!**
   >
   > * Para poder distinguir entre postbacks de eventos legítimos y postbacks rechazados, configura las <Anchor target="_blank" href="/partners/es/docs/postback-macros-for-ad-networks#macros-instalaciones-eventos-in-app-y-eventos-rechazados">macros de los postbacks rechazados</Anchor>.
   > * Para habilitar los postbacks de eventos de instalación/in-app rechazados, agrega los siguientes parámetros a tu plantilla de postback predeterminada:
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`  
   >     **Nota:** Si el postback de Privacidad avanzada está habilitado, agrega también los parámetros anteriores a la plantilla de Privacidad avanzada.

3. [Opcional] **Parámetros personalizados:** configura tus propios parámetros para incluir en el postback.
4. Usa la vista previa de la plantilla de postback para verificar que todo esté correcto.
5. Haz clic en **Guardar**.

<Anchor target="_blank" href="/marketers/es/docs/in-app-event-postback-configuration">Más información sobre los postbacks y ejemplos.</Anchor>

Si tienes algún problema, usa el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente de partners</Anchor>.

## Postbacks de Privacidad avanzada y SKAN

Los postbacks de Privacidad avanzada y SKAN se pueden configurar solo después de crear el enlace de atribución y el postback predeterminado.

**Para gestionar los postbacks:**

1. Selecciona un tipo de postback:
   * Postback de <Anchor target="_blank" href="/partners/es/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Privacidad avanzada</Anchor>.
   * Postback de <Anchor target="_blank" href="/partners/es/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>.
2. Activa el creador.
3. **[Solo para la configuración de postbacks de SKAdNetwork]** Introduce tu ID de SKAdNetwork. Este campo es obligatorio y la configuración no se puede guardar sin un ID válido.
4. Introduce las **direcciones de los puntos de conexión.** Estos son los puntos de conexión a los que se envían los postbacks. Introduce las URL relevantes para instalaciones, eventos in-app o ambos.
5. Agrega los parámetros del postback:

   * **Nombre de parámetro**: nombre de pantalla del parámetro AppsFlyer.
   * **Tu parámetro de recepción**: el parámetro de recepción respectivo de tu lado.
   * **Valor del parámetro** (disponible para algunos parámetros): elija el formato del valor. Por ejemplo, para los valores booleanos, elige si deseas recibirlos como "true"/"false" o 1/0.
   * **Instalación**: marca la casilla para incluir el parámetro en el postback de instalación.
   * **Evento in-app**: marca la casilla para incluir el parámetro en el postback del evento in-app.

   Lista de <Anchor target="_blank" href="/partners/es/docs/skan-integration-guide-for-ad-networks#recibir-datos-de-appsflyer">macros de postbacks de SKAdNetwork</Anchor>

   Lista de <Anchor target="_blank" href="/partners/es/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification">macros de postbacks de Privacidad avanzada.</Anchor>

   > 🚧 **¡Importante!**
   >
   > * Para habilitar los postbacks de eventos de instalación/in-app rechazados, agrega los siguientes parámetros a tu plantilla de postback predeterminada:
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`
   > * Para habilitar los postbacks rechazados para Privacidad avanzada, primero debes agregar los parámetros anteriores al [postback predeterminado](/docs/self-serve-integration-management-for-ad-networks#postback-predeterminado).
   > * Cuando los parámetros anteriores se agregan tanto al postback predeterminado como al postback de Privacidad avanzada (si está habilitado), se habilitan los postbacks de eventos de instalación o in-app rechazados.

6. [Opcional] **Parámetros personalizados:** configura tus propios parámetros para incluir en el postback.
7. Usa la vista previa de la plantilla de postback para verificar que todo esté correcto.
8. Haz clic en **Guardar**.  
   Ten en cuenta que cuando guardas el postback, los cambios entran en vigor inmediatamente.

Si tienes algún problema, contáctanos utilizando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente de partners</Anchor>.

<div data-zendesk-anchors="prerequisites=pr%C3%A9-requisitos h_01KZTVV00EB224GJD5F7VBP071=pr%C3%A9-requisitos accessing-integration-management=acceso-a-la-gesti%C3%B3n-de-integraciones h_01H9FCSTYR157CCJWTYSNE9JQ0=acceso-a-la-gesti%C3%B3n-de-integraciones attribution-link=enlace-de-atribuci%C3%B3n h_01H9FCSTYR6HRSF9F8KCR4B3X7=enlace-de-atribuci%C3%B3n h_01H9FCSTYR4Q1985DTHNE1M1CC=importante default-postback=postback-predeterminado h_01H9FCSTYR2WX0M0ZW3B22EKBM=postback-predeterminado h_01H9FCSTYSEP367WAAKCFHZT58=importante-1 advanced-privacy-and-skan-postbacks=postbacks-de-privacidad-avanzada-y-skan h_01H9FCSTYSRKBMYR2BYNQJJKVM=postbacks-de-privacidad-avanzada-y-skan h_01H9FCSTYSEJD59AWCFNXDZMYW=importante-2" />
