---
title: Redirigir a los usuarios a la tienda de aplicaciones
metadata:
  keywords:
    - clicks
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2018-04-30T08:08:25Z'
  edited_at: '2026-08-12T12:28:26Z'
  id: 360000807629
  locale: es
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/es/articles/360000807629
---
> **En resumen:** Obtén información sobre las opciones para redirigir a los usuarios a la tienda de aplicaciones después de publicar un anuncio y cómo enviar los datos de engagement a AppsFlyer.

<div id="overview" />

## Descripción general

AppsFlyer recibe los datos de engagement (clics e impresiones) para su atribución de varias maneras:

* El usuario **hace clic** en el anuncio y se le [redirige a AppsFlyer](#usuarios-redirigidos-a-través-de-appsflyer) y, después, a la tienda de aplicaciones.
* El usuario hace **clic o visualiza** el anuncio y es [redirigido directamente a la tienda de aplicaciones](#usuarios-enviados-directamente-por-la-red-publicitaria), mientras que el **enlace de atribución se envía a AppsFlyer desde el servidor**.

En ambos casos, se utilizan la <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">estructura y los parámetros habituales de los enlaces de atribución</Anchor>.

<div id="note" />

> 📘 **Nota:**
>
> En el caso de las SRN, los datos se reciben a través de API especializadas.

<div id="users-redirected-via-appsflyer" />

## Usuarios redirigidos a través de AppsFlyer

Cuando se hace clic en un anuncio, se dirige al usuario a AppsFlyer, que luego lo redirige a la tienda de aplicaciones mediante el siguiente flujo:

1. El usuario es redirigido a AppsFlyer.
2. AppsFlyer registra el clic.
3. AppsFlyer redirige al usuario a la tienda de aplicaciones.
4. El usuario instala la aplicación.
5. AppsFlyer atribuye la instalación.

<div id="users-sent-directly-by-the-ad-network" />

## Usuarios enviados directamente por la red publicitaria

Cuando se hace clic en un anuncio, la red publicitaria dirige al usuario a la tienda de aplicaciones, lo que minimiza la cantidad de redireccionamientos:

1. El usuario es enviado a la tienda de aplicaciones.
2. La red publicitaria reporta los datos de engagement a AppsFlyer desde el dispositivo.
3. El usuario instala la aplicación.
4. AppsFlyer atribuye la instalación.

<div id="sending-engagement-data-to-appsflyer" />

### Envío de los datos de engagement a AppsFlyer

Enviar al usuario directamente a la tienda de aplicaciones mejora su experiencia al reducir la cantidad de redirecciones. También garantiza una atribución precisa de las instalaciones y permite un tráfico de alta calidad.

Las redes publicitarias solo pueden reportar los clics y las impresiones a AppsFlyer **directamente desde el dispositivo del usuario**.

<div id="timing-of-sending-redirects" />

#### Tiempo de envío de redireccionamientos

Para evitar la pérdida de atribuciones e ingresos para la red publicitaria, los clics y las impresiones deben enviarse a AppsFlyer en tiempo real:

* Las **URL de impresiones** deben reportarse una vez que se publica un anuncio.
* Las **URL de clics** deben reportarse cuando un usuario hace clic en el anuncio.

<div data-zendesk-anchors="overview=descripci%C3%B3n-general h_01HDY3CARC0A9504XGMJHYHGY4=descripci%C3%B3n-general h_01HDY3CARCZK06C5XHEQFQYA8W=nota redirect-users-via-appsflyer=usuarios-redirigidos-a-trav%C3%A9s-de-appsflyer 01HDYFGYW3FDR64C54KKPXRHDF=usuarios-redirigidos-a-trav%C3%A9s-de-appsflyer send-users-directly-by-the-ad-network=usuarios-enviados-directamente-por-la-red-publicitaria 01HDYFH8ZCSP2SN4ZYQQVG7EED=usuarios-enviados-directamente-por-la-red-publicitaria send-engagement-data-to-appsflyer=env%C3%ADo-de-los-datos-de-engagement-a-appsflyer h_01HDYGSEFHVF8ZD43XCVNGYT9N=env%C3%ADo-de-los-datos-de-engagement-a-appsflyer timing-of-sending-redirects=tiempo-de-env%C3%ADo-de-redireccionamientos h_01HDXXDDXDEP43YHE3GF81BSKV=tiempo-de-env%C3%ADo-de-redireccionamientos" />
