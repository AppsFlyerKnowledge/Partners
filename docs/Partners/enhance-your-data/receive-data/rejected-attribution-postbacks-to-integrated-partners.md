---
title: Publicación de atribución rechazada a socios integrados
metadata:
  keywords:
    - fraud
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
  created_at: '2017-09-19T07:03:47Z'
  edited_at: '2026-08-12T12:28:39Z'
  id: 115004744123
  locale: es
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/es/articles/115004744123
---
> **A simple vista:** Los socios integrados reciben notificaciones de instalaciones y eventos dentro de la aplicación rechazados debido a fraude o incumplimiento de las reglas de validación.

<div id="rejected-attribution-postbacks-relating-to-fraud-and-validation-rules" />

## Publicaciones de atribución rechazadas relacionadas con el fraude y las reglas de validación

**Terminología**:

* **Eventos de fraude:** instalaciones y eventos dentro de la aplicación bloqueados por Protect360
* **Eventos no conformes**: instalaciones y eventos dentro de la aplicación que no cumplen con las reglas de validación
* **Eventos rechazados**: Eventos de fraude y eventos de reglas de validación no cumplidos
* **Instalación corregida por atribución:** Una instalación secuestrada identificada y bloqueada, cuya atribución se corrige posteriormente y se asigna a la fuente de medios genuina.

**Devoluciones de mensajes**

* Los socios integrados reciben notificaciones de eventos rechazados en tiempo real.
* No hay notificaciones de eventos de fraude para eventos dentro de la aplicación de instalaciones con atribución corregida.
* Las notificaciones de eventos rechazados se envían al endpoint especificado por el socio tanto para instalaciones como para eventos rechazados, con parámetros adicionales como:  
  * Razón del bloqueo
  * Sub-razón del rechazo
  * Es-rechazado
  * Valor de la razón del rechazo (cuando esté disponible). Por ejemplo: `reject_reason=site_blacklist&reject_reason_value="1123456"&is_rejected=1`

La siguiente tabla enumera la razón del rechazo, el valor de la razón del rechazo y una explicación de la razón del rechazo:

| Razón del rechazo | Valor de la razón del rechazo | El usuario puede configurar | Explicación |
| --- | --- | --- | --- |
| anomalías en ctit | El tiempo medido de clic a instalación en segundos | . | Las anomalías de CTIT son clics atribuidos que han sido bloqueados debido a CTIT irrazonable (tiempo de clic a instalación). |
| store\_install\_validation | N/D | . | Instalaciones que fallaron la validación en el App Store |
| lista negra de sitios | ID del sitio | . | Instalaciones procedentes de IDs de sitios que AppsFlyer bloqueó debido a una alta densidad de actividad fraudulenta. Determinado por nuestros algoritmos internos. |
| Bots | N/D | . | Intentos de instalación bloqueados realizados por Bots |
| inundación de clics | ID del sitio o vacío | . | Instalaciones provenientes de clusters bloqueados por AppsFlyer debido a un gran número de instalaciones con un alto CTIT y una baja tasa de conversión. |
| anomalías en el comportamiento | N/D | . | Anomalías de comportamiento siendo fraude de instalación bloqueadas debido a un comportamiento posterior a la instalación inconsistente y anormal. |
| secuestro de instalación | N/D | . | La instalación de secuestro se atribuye a clics bloqueados en función de un tiempo de clic y de instalación irrazonable, basado en la API del lado del servidor de Google Play. |
| validación\_bots | Nombres de reglas u vacío | ✓ | Regla definida por el cliente. |
| validación\_secuestro | Nombres de reglas | ✓ | Regla definida por el cliente. |
| capa\_ai | N/D | . | Se utilizan modelos de AI para analizar grandes cantidades de puntos de datos, mejorando las capacidades de detección para identificar actividades fraudulentas en dispositivos e instalaciones. |

<div id="reject-reasons-for-in-app-events" />

#### Razones para rechazar eventos en la app

| Razón del rechazo | Valor de la razón del rechazo | Explicación |
| --- | --- | --- |
| Hereda de la instalación | Hereda de la instalación | Instalación inicial identificada como falsa basada en<Anchor target="_blank" href="/marketers/es/docs/protect360-raw-data-reports#motivos-de-bloqueo">instalación</Anchor> o<Anchor target="_blank" href="/marketers/es/docs/protect360-raw-data-reports#motivos-de-bloqueo"> motivo de lista denegada</Anchor> |
| inapps\_bots | parámetros\_de\_dispositivo\_falso | el algoritmo de AppsFlyer detecta fraude |
| validación\_inapps | nombre\_de\_evento\_inválido | Basado en la regla de validación solicitada o definida manualmente |
| validación\_inapps | valor\_de\_evento\_inválido | Basado en la regla de validación solicitada o definida manualmente |
| validación\_inapps | Nombre/s\_de\_la\_regla | Basado en reglas definidas manualmente |

<div id="important" />

> 🚧 **Importante:**
>
> * Para poder distinguir entre las devoluciones de eventos legítimos y las devoluciones rechazadas, debes configurar los <Anchor target="_blank" href="/partners/es/docs/postback-macros-for-ad-networks#macros-instalaciones-eventos-in-app-y-eventos-rechazados">macros de devoluciones rechazadas</Anchor>.
> * Para habilitar las devoluciones rechazadas por Privacidad Avanzada, primero debes añadir los siguientes parámetros a la <Anchor target="_blank" href="/partners/es/docs/self-serve-integration-management-for-ad-networks#postback-predeterminado">Devolución predeterminada</Anchor>:
>   * `is-rejected`
>   * `blocked-reason`
>   * `blocked-sub-reason`
>   * `blocked-reason-value`
> * Cuando se agregan los parámetros anteriores tanto a la devolución predeterminada como a la devolución de privacidad avanzada, se habilitan las devoluciones rechazadas de instalación/eventos en la app.

<div data-zendesk-anchors="rejected-attribution-postbacks-relating-to-fraud-and-validation-rules=publicaciones-de-atribuci%C3%B3n-rechazadas-relacionadas-con-el-fraude-y-las-reglas-de-validaci%C3%B3n h_01J5597AMDVWR2KTANSF7Y7T4P=publicaciones-de-atribuci%C3%B3n-rechazadas-relacionadas-con-el-fraude-y-las-reglas-de-validaci%C3%B3n reject-reasons-for-inapp-events=razones-para-rechazar-eventos-en-la-app h_01J5597AMDHT5GJQN7QJZKV41F=razones-para-rechazar-eventos-en-la-app h_01J5597AMD29TAZSKZS9WTFSM5=importante" />
