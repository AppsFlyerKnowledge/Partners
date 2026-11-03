---
title: Integración de Partners de gestión de campañas de Meta con AppsFlyer
metadata:
  keywords:
    - Callbacks
    - Integration
    - Facebook
    - Partner
    - In-App
    - partner account
    - User Level
    - Data policy
    - FMP
    - Partners
    - Developers
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
  created_at: '2015-03-29T12:38:26Z'
  edited_at: '2026-08-12T12:30:06Z'
  id: 207034146
  locale: es
  section: Marketing partner onboarding
  section_id: 6551118224657
  url: https://support.appsflyer.com/hc/es/articles/207034146
---
> **De un vistazo:** Descubre qué tipos de datos pueden recibir los partners de gestión de campañas de Meta de AppsFlyer.

## Postbacks de instalaciones

Tras la conversión, AppsFlyer puede devolver los siguientes parámetros:

| Nombre de parámetro | Convención de nombre de parámetro |
| --- | --- |
| Nombre de la campaña | `{campaign_name}` |
| Cadena | `{campaign_id}` |
| Nombre de conjunto de anuncios | `{adset_name}` |
| ID de conjunto de anuncios | `{adset_id}` |
| Nombre del grupo de anuncios | `{adgroup_name}` |
| ID del grupo de anuncios | `{adgroup_id}` |
| Hora del evento: redondeada al alza | `{timestamp}` |
| ID de usuario único de AppsFlyer | `{sha1-appsflyer-device-id}` |
| ID de dispositivo con hash MD5 | `{md5IDFA\md4GAID}` |
| Si la atribución procede de una visualización | `{is-impression}` |
| Canal (Instagram, Meta Audience Network, Facebook, Messenger) | `{af_channel}` |
| Geografía | `{user_country}` |

> 📄 **Ejemplo**
>
> http://mcmp_postbackURL.........&mcmp_ADset_name =`{adset_name}`

## Habilitar la atribución por impresiones

Tras los eventos in-app, AppsFlyer puede devolver los siguientes parámetros (además de los indicados anteriormente):

| Nombre de parámetro | Convención de nombre de parámetro |
| --- | --- |
| Nombre del evento* | `{event_name}` |
| Valor del evento | `{event_value}` |

> 📄 **Ejemplo**
>
> `http://FMP_postbackURL.........&eventname={event_name}`

* El partner de gestión de campañas de Meta puede elegir recibir el nombre del evento in-app tal como lo configuró el anunciante en el SDK de AppsFlyer o hacer que el anunciante rellene un campo de texto libre por evento.

## Política de datos a nivel de usuario

* AppsFlyer no puede transferir el IDFA ni el ID de publicidad de Android.

* AppsFlyer transfiere las marcas de tiempo de instalaciones/eventos redondeadas a la hora más cercana.

Por ejemplo: Si una instalación se produjo a las 4.32 pm y 42 segundos, podemos indicar las 5 pm como marca de tiempo

* AppsFlyer puede usar un ID aleatorio de creación propia para adjuntarlo a eventos. Ese ID no debería derivarse del IDFA/ID de Android y debería ser único para los anuncios de Meta. El mismo ID aleatorio se puede transferir a sistemas posteriores para los postbacks de eventos in-app.

> 📘 **Nota:**
>
> Según los términos de Meta, el envío de postbacks solo está disponible para las empresas que obtengan la siguiente acreditación: Ad Technology

> 📄 **Ejemplo**
>
> ![](https://files.readme.io/6832879dafaadb91a795988abdc5e51203c9c1775054e35829cfe60cb2175a66-360001440909.png)
>
> Para consultar la lista completa de Partners de gestión de campañas de Meta, haz clic <Anchor target="_blank" href="https://www.facebook.com/business/partner-directory/search?programBadges=ADTECH_FB.ADTECH_IG&solution_type=campaign_management">aquí</Anchor>.

<div data-zendesk-anchors="install-postbacks=postbacks-de-instalaciones inapp-event-postbacks=habilitar-la-atribuci%C3%B3n-por-impresiones userlevel-data-policy=pol%C3%ADtica-de-datos-a-nivel-de-usuario" />
