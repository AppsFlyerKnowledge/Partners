---
title: Reglas de validación para redes de publicidad y agencias
metadata:
  keywords:
    - Agency
    - Networks
    - Validation Rules
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2017-09-18T13:53:49Z'
  edited_at: '2026-08-12T12:27:41Z'
  id: 115004751486
  locale: es
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/es/articles/115004751486
---
> **De un vistazo:** Los anunciantes utilizan las reglas de validación para definir manualmente las condiciones para bloquear las instalaciones, la atribución y los eventos in-app de las instalaciones/IAE no compatibles. Los partners integrados (redes de publicidad y agencias) pueden ver las reglas y obtener reportes de instalaciones bloqueadas, atribución e IAE.

## Acerca de las reglas de validación

Reglas de validación:

* Las define el anunciante en el creador de reglas mediante condiciones y lógica personalizadas que filtran y seleccionan qué instalaciones de aplicaciones o eventos in-app conservar o bloquear.
* Se basan en una variedad de parámetros para múltiples casos de uso, incluyendo:
  * Instalaciones no dirigidas para la campaña del anunciante (geolocalización incorrecta, versión del sistema operativo, etc.).
  * Instalaciones que no cumplen con el pedido de inserción firmado entre el anunciante y tú.
  * Instalaciones secuestradas por publishers fraudulentos, malware, etc.
  * Instalaciones falsas o eventos in-app enviados desde bots, emuladores o granjas de dispositivos.
* Las reglas definidas para eventos in-app solo tienen efecto en los IAE asociados con instalaciones que no se bloquearon previamente.
* Las reglas que incluyen una red de publicidad son visibles para el personal de esa red de publicidad (pero no pueden ver otras redes de publicidad incluidas en la regla).
* Se ejecutan en tiempo real y toman medidas inmediatas. Se envía un postback de rechazo a los partners que han rechazado la configuración de postbacks. <Anchor target="_blank" href="/partners/es/docs/rejected-attribution-postbacks-to-integrated-partners">Aprender más</Anchor>.
* Tienen opciones adicionales disponibles para los clientes de <Anchor target="_blank" href="/marketers/es/docs/protect360-anti-fraud-guide">Protect360</Anchor>, además del bloqueo y detección automáticas de fraudes de Protect360. Estas condiciones son conocidas por ayudar en la detección de diversos tipos de fraude de instalaciones, instalaciones falsas y eventos in-app falsos.

## Disponibilidad para redes de publicidad y agencias

Las reglas que rigen el acceso adicional a las reglas de validación para las agencias son las siguientes:

* Los partners integrados pueden ver la lista de reglas de validación que se aplican a ellos.
  * Ven que otros partners están incluidos en la norma, aunque los nombres de los otros partners no se revelan.
  * Si una regla de validación se aplica a varias aplicaciones pero un partner solo está integrado para una o algunas de las aplicaciones, solo puede ver la regla y la aplicación para la que está integrado.
* Para hacer clic en una regla específica y ver sus detalles, se requiere permiso del anunciante para **Ver reglas de validación**.
  * Por defecto, el permiso está desactivado.
  * Si está desactivado, un partner puede hacer clic en **Solicitar acceso**. El anunciante recibe una notificación de la solicitud.
* Una red de publicidad no puede crear o editar reglas.

### Agencias

Las normas que rigen el acceso de las reglas de validación a las redes de publicidad y agencias son las siguientes:

* Las agencias pueden crear, editar y eliminar reglas, si tienen permiso del anunciante para **Agregar reglas de validación**.
  * Las agencias solo pueden editar o eliminar las reglas que crean, no las creadas por el anunciante.
* Para agregar reglas con las condiciones de Protect360:
  * El anunciante debe tener una suscripción a Protect360.
  * Se necesita permiso del anunciante para **Acceder al panel de control de Protect360 y al raw data**.
* Si una agencia crea una regla para varias aplicaciones con las que está integrada, y luego el anunciante elimina la integración de una o más aplicaciones, la regla se divide en reglas separadas para cada aplicación, y las reglas de las aplicaciones que no están integradas quedan inactivas.

**Para acceder a las reglas de validación**:

1. En AppsFlyer, ve a **Configuración** > **Reglas de validación**.
2. Para ver la regla de validación, selecciona una **cuenta de propietario de la aplicación**.
   * Se muestra la lista de reglas definidas por la cuenta del propietario de la aplicación para el tráfico que podría provenir de ti.
   * Para obtener una explicación de cómo funcionan los conjuntos de reglas, consulta <Anchor target="_blank" href="/marketers/es/docs/implement-validation-rules-to-prevent-fraud">Reglas de validación para propietarios de aplicaciones</Anchor>.

## Reportes

### Fraude Protect360: Datos exportados

Los anunciantes pueden otorgar a los partners (redes de publicidad y agencias) <Anchor target="_blank" href="/marketers/es/docs/raw-data-reporting-overview#protect360-fraud-and-validation-rules">permisos</Anchor> para descargar los siguientes reportes de **Reportes** > **Datos exportados**:

* Instalaciones: instalaciones bloqueadas o con atribución bloqueada.
* Eventos in-app bloqueados: eventos in-app rechazados (requiere que el anunciante tenga una suscripción a Protect360).
* Postbacks de instalaciones bloqueadas: un único reporte de postbacks de rechazos que se te envía en tiempo real.

Los campos **Motivo del bloqueo** y **Valor del motivo del bloqueo** se rellenan en los reportes. El **valor de motivo del bloqueo** incluye el nombre de la regla que provocó el rechazo.

## Postbacks de instalaciones rechazadas por reglas de validación

Los partners integrados que se integran con AppsFlyer pueden <Anchor target="_blank" href="/partners/es/docs/rejected-attribution-postbacks-to-integrated-partners">recibir postbacks de instalaciones bloqueadas</Anchor> en tiempo real cada vez que se rechaza una instalación debido al cumplimiento de las reglas.

Ponte en contacto con tu representante de desarrollo de partners para obtener más información.

<div data-zendesk-anchors="about-validation-rules=acerca-de-las-reglas-de-validaci%C3%B3n h_01HKA04414ZAS0EZX6AGHVTZHY=acerca-de-las-reglas-de-validaci%C3%B3n availability-to-ad-networks-and-agencies=disponibilidad-para-redes-de-publicidad-y-agencias h_01HKA04415K37N997EDS8X26PK=disponibilidad-para-redes-de-publicidad-y-agencias agencies=agencias h_01HKA044155S4Y7DAGP05S5FJA=agencias reports=reportes h_01HKA04415P5K6J4VXS64GA2SP=reportes protect360-fraud-export-data=fraude-protect360-datos-exportados h_01HKA0441501DKTQHT3X0G0RC7=fraude-protect360-datos-exportados validation-rules-rejected-installation-postbacks=postbacks-de-instalaciones-rechazadas-por-reglas-de-validaci%C3%B3n h_01HKA04415BR5XJABRHSWYTTS7=postbacks-de-instalaciones-rechazadas-por-reglas-de-validaci%C3%B3n" />
