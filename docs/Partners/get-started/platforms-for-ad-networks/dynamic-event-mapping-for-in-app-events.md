---
title: Asignación dinámica de eventos para eventos in-app
metadata:
  keywords:
    - In-App
    - Mapping
    - Dynamic Event Mapping
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
  created_at: '2016-05-26T08:48:23Z'
  edited_at: '2026-08-12T12:30:18Z'
  id: 208996726
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/208996726
---
> **De un vistazo:** Configura tu enlace de atribución para que tus Partners (como TUNE o CAKE) puedan recibir distintos postbacks para un único evento in-app, en función de los ID de objetivo.

<div id="introduction" />

## Introducción

Se pueden enviar distintos postbacks para un evento in-app en función del ID de objetivo.

Esta función es compatible con redes que usan HasOffers, CAKE u otras redes que quieren recibir distintos postbacks de evento in-app para un único evento in-app del SDK.

En la página Active Integrations del Dashboard, los anunciantes asignan cada uno de sus eventos del SDK a la etiqueta de evento dinámica preferida para cada Partner. La etiqueta del evento incluye tanto eventos in-app como postbacks de eventos in-app rechazados.

Esto permite a las Ad network abrir varias campañas con una etiqueta de evento dinámica independiente (por ejemplo, HasOffers llama a esto goal\_id) para cada campaña. A continuación, las etiquetas de evento dinámicas se pasan a la Ad network en el postback en función del valor que se colocó en la URL de clic.

<div id="attribution-link" />

## Enlace de atribución

<div id="attribution-link-example" />

> 📄 **Ejemplo de enlace de atribución**
>
> **Decodificado**:
>
> ```http
> https://app.appsflyer.com/com.xyz.abc?pid=mediasource_int&clickid={transaction_id}
> &goalid_1={XXX}&goalid_2={YYY}
> ```

El anunciante debe asignar todos los goal\_id en la sección de eventos in-app (consulta más abajo) según las instrucciones de la red.

En el ejemplo siguiente, level20\_finished se asigna como $$click(goalid\_1) y level25\_finished se asigna como $$click(goalid\_2).

Cuando el usuario de la aplicación completa el nivel 20, AppsFlyer recupera el valor correspondiente (en este caso, XXX, tal como aparece en el enlace de atribución anterior) y lo envía en el postback.

Si ese mismo usuario u otro completa después el nivel 25, AppsFlyer vuelve a consultar el enlace de atribución, rellena dinámicamente el goal\_id con el valor correspondiente (en este caso, YYY) y lo envía en el postback.

<Image align="center" alt="Goadid.png" src="https://files.readme.io/35390305a93cc7a49f193fa1667b491827736252a9133bc01d01c07dfdc38586-360001400478.png" />

<div data-zendesk-anchors="introduction=introducci%C3%B3n attribution-link=enlace-de-atribuci%C3%B3n" />
