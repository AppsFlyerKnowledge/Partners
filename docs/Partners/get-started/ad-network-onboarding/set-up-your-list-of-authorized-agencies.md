---
title: Configura tu lista de agencias autorizadas
metadata:
  keywords:
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
  created_at: '2024-06-09T19:29:56Z'
  edited_at: '2026-08-12T12:29:27Z'
  id: 25774607860113
  locale: es
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/es/articles/25774607860113
---
> **En resumen:** Administra qué agencias autorizas a ejecutar campañas a través de la integración de tu red.

<div id="overview" />

## Visión general

Para evitar el uso no autorizado de tu red, todas las agencias que ejecuten campañas a través de la integración de tu red deben contar con una aprobación previa. Esto se hace agregando su ID de agencia (`af_prt`) a tu lista de agencias autorizadas. Las agencias que no aparecen en la lista no pueden configurar la integración, ya que la ventana de configuración de Partners aparece atenuada. Esto impide que gestionen campañas. La aprobación se realiza a nivel de cuenta, lo que significa que una vez que se aprueba una agencia, tiene acceso a todas las aplicaciones que ejecutan campañas en tu red.

A partir del 31 de julio de 2024, solo el tráfico de las agencias autorizadas por las redes de publicidad se registrará y medirá en AppsFlyer. El tráfico no autorizado dará lugar a una respuesta 403 (Prohibido) de AppsFlyer.

<div id="note" />

> 📘 **Nota**
>
> * Esto no se aplica a las agencias que trabajan con <Anchor target="_blank" href="/marketers/es/docs/self-reporting-networks-srns">SRN</Anchor>.
> * Solo los administradores tienen acceso a esta página.
> * La lista de agencias autorizadas puede incluir hasta 200 agencias.

[![authorized-agencies-5.jpg](https://files.readme.io/10012bde55cffa967f2e581420a9c32b7ce8b9cb120e203ba230bf7f271b0d9a-25977984018833.jpg)](https://files.readme.io/10012bde55cffa967f2e581420a9c32b7ce8b9cb120e203ba230bf7f271b0d9a-25977984018833.jpg)

<div id="manage-authorized-agencies" />

## Gestión de las agencias autorizadas

Desde la página **Agencias autorizadas**, puedes agregar agencias, ver la lista existente de agencias que aprobaste para ejecutar campañas en tu red y eliminar las agencias que no apruebas. La página incluye dos secciones:

* Panel izquierdo: Agregar nuevas agencias
* Panel derecho:
  * Ver la lista de agencias autorizadas
  * Eliminar agencias

**Para acceder a la página de agencias autorizadas:**

1. En la barra superior, abre el menú de la cuenta (menú desplegable de direcciones de correo electrónico) > **Centro de seguridad**.
2. En la sección **Agencias autorizadas**, haz clic en **Administrar agencias autorizadas**.

<div id="add-an-agency-to-the-list" />

### Agregar una agencia a la lista

1. En el panel izquierdo de la página **Agencias autorizadas**, introduce el ID de la agencia.
2. Haz clic en **Agregar a la lista**. La agencia ahora aparece en el panel derecho.
3. [Opcional] Repite los pasos 1 y 2 para agregar más agencias.
4. Haz clic en **Guardar lista**.

<div id="note-1" />

> 📘 **Nota**
>
> Asegúrate de introducir un ID de agencia válido. Por ejemplo, (af\_prt=) `my_agency_123`

<div id="delete-an-agency-from-the-list" />

### Eliminar una agencia de la lista

1. En el panel derecho de la página **Agencias autorizadas**, coloca el cursor sobre la agencia que deseas eliminar y haz clic en el ícono de la papelera.
2. Confirma la eliminación. La eliminación correcta de la agencia se confirma con una indicación.
3. [Opcional] Repite los pasos 1 y 2 para eliminar más agencias.

<div data-zendesk-anchors="overview=visi%C3%B3n-general h_01HJR00RGQ2PK3T8BB2ZG3PFQN=visi%C3%B3n-general h_01HJR00RGQX0CQEHDS9BHBGJD4=nota accessing-the-allowlists=gesti%C3%B3n-de-las-agencias-autorizadas h_01HZZ5FP1560HJYDVDNSJ8WAAP=gesti%C3%B3n-de-las-agencias-autorizadas add-an-agency-to-the-list=agregar-una-agencia-a-la-lista h_01HZZ691KMKTYVAETT4RM3AD97=agregar-una-agencia-a-la-lista h_01HZZ7QGY0VTS0FY0HJJAZ2AXV=nota-1 h_01HJR00RGQ4ZEGE0RDK01S5SQQ=eliminar-una-agencia-de-la-lista" />
