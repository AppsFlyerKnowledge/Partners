---
title: Resolución de problemas con los postbacks para redes de publicidad
metadata:
  keywords:
    - Postback
    - Ad Networks
    - Partners
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2022-07-07T15:16:00Z'
  edited_at: '2026-08-12T12:28:37Z'
  id: 7466104144145
  locale: es
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/es/articles/7466104144145
---
> **En resumen:** Si tienes problemas a la hora de recibir postbacks, revisa las siguientes soluciones.

| **Problema** | **Solución** |
| --- | --- |
| <span id="i-dont-see-my-advertisers-app-under-my-apps"></span>No veo la aplicación de mi anunciante en **Mis aplicaciones** | <ul><li>Si la aplicación del anunciante no aparece en **Mis aplicaciones** (en el menú superior), comunícate con el anunciante y pídele que te <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-ad-network">proporcione los permisos pertinentes</Anchor>.</li><li>Verifica que el selector <Anchor target="_blank" href="/marketers/es/docs/partner-activation-deactivation#activar-la-integración-de-un-partner">**Activar partner** esté habilitado</Anchor>.</li></ul>**Nota:** Si estás ejecutando una prueba con una aplicación de producción, asegúrate de registrar tu dispositivo de acuerdo con las instrucciones <Anchor target="_blank" href="/marketers/es/docs/registering-test-devices">aquí</Anchor>. |
| <span id="im-not-receiving-install-postbacks"></span>No recibo postbacks de instalaciones | <ul><li>Si no hubo instalaciones de aplicaciones, no verás postbacks de instalaciones.  Comprueba si tu aplicación tiene atribuciones de instalación: ve a **Configuración** > **Mis aplicaciones** > [Elige la aplicación] > <Anchor target="_blank" href="/partners/es/docs/integrated-partners-dashboard">**Información general**</Anchor>.</li></ul> |
| <span id="im-not-receiving-inapp-event-postbacks"></span>No recibo postbacks de eventos in-app | <ul><li>Verifica que los eventos estén <Anchor target="_blank" href="/marketers/es/docs/in-app-event-postback-configuration">asignados correctamente</Anchor> en la pestaña de integración, en la sección **Postbacks de eventos in-app**.</li></ul>**Nota:** Los nombres de los eventos distinguen entre mayúsculas y minúsculas y deben asignarse utilizando el mismo nombre que se entrega a través de servidor a servidor/SDK. |
| <span id="im-not-receiving-both-install-and-inapp-event-postbacks"></span>No recibo notificaciones de postbacks de instalaciones ni de eventos in-app | <ul><li>Si no hubo instalaciones de aplicaciones, no verás postbacks de instalaciones. Comprueba si tu aplicación tiene atribuciones de instalación. Ve a **Configuración** > **Mis aplicaciones** > [Elige la aplicación] > <Anchor target="_blank" href="/partners/es/docs/integrated-partners-dashboard">**Información general**</Anchor>.</li><li>Verifica los postbacks de instalaciones/eventos in-app y revisa los siguientes campos:<ul><li>**URL del postback**: el postback real entregado. Comprueba que la plantilla no omita ningún valor crucial.</li><li>**Código de respuesta HTTP del postback**: el código de respuesta que AppsFlyer recibe del servidor del partner. Verifica el código de respuesta HTTP. Si no es 2XX, verifica la configuración de tu servidor interno.</li><li>**URL original**: la URL de clic/impresión que recibe AppsFlyer para la instalación/evento correspondiente. Verifica que el enlace de atribución esté completo. Los datos no proporcionados en el enlace no se pueden devolver mediante un postback.</li></ul></li><li>Verifica la configuración de **Privacidad avanzada**: cuando está habilitada, <Anchor target="_blank" href="/partners/es/docs/advanced-privacy-guide-postback-macros-for-ad-networks">los datos a nivel de usuario para usuarios que no dan su consentimiento y ejecutan iOS 14.5+</Anchor> NO están disponibles en los postbacks.<ul><li>Si el postback de Privacidad avanzada no está definido en tu integración, pero el anunciante decide utilizar la Privacidad avanzada, no se entregarán postbacks para los usuarios de iOS que no hayan dado su consentimiento.</li></ul></li><li>Consulta la definición de <Anchor target="_blank" href="/marketers/es/docs/in-app-event-postback-configuration#ventana-de-postback-de-eventos-in-app">Ventana de postback</Anchor>. Los postbacks no se envían después del período de tiempo definido.</li><li>Comprueba si el <Anchor target="_blank" href="/marketers/es/docs/in-app-event-postback-configuration#postbacks-condicionales-de-eventos-in-app">postback condicional</Anchor> está definido.</li><li>Comprueba si el <Anchor target="_blank" href="/partners/es/docs/rejected-attribution-postbacks-to-integrated-partners">tráfico está bloqueado</Anchor>: descarga y revisa el reporte de **postbacks de instalaciones bloqueados**.</li></ul> |

<div id="see-also" />

> 📄 **Consulta también**
>
> * <Anchor target="_blank" href="/marketers/es/docs/postback-troubleshooting-for-advertisers">Resolución de problemas de postbacks para anunciantes</Anchor>
> * <Anchor target="_blank" href="/marketers/es/docs/in-app-event-postback-configuration">Configuración de postbacks de eventos in-app</Anchor>

<div data-zendesk-anchors="h_01HDP4JFM42RZNBGM9TTD5SRP0=consulta-tambi%C3%A9n" />
