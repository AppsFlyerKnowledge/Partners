---
title: Integración de Offerslook con AppsFlyer para ad networks
metadata:
  keywords:
    - Offerslook
    - Advertisers
    - Ad Networks
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
    - Ad Networks
  created_at: '2016-05-31T08:47:36Z'
  edited_at: '2026-08-12T12:30:32Z'
  id: 209074606
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/209074606
---
> **De un vistazo:** Descubre cómo las ad networks que usan Offerslook pueden integrarse con AppsFlyer y recibir datos de atribución de instalaciones.

Para iniciar la integración, envía a AppsFlyer:

1. Tu enlace de atribución

   ```http
   https://networkname.offerstrack.net/index.php?offer_id={offer_id}&aff_id={aff_id}
   ```
2. Tu postback (para instalaciones)  

   ```http
   https://networkname.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}
   ```

<div id="creating-your-attribution-link" />

## Cómo crear tu enlace de atribución

El enlace de atribución consta del enlace de atribución base de AppsFlyer que aparece a continuación y de macros adicionales añadidas por la ad network.

A continuación puedes ver el enlace de atribución base de AppsFlyer con una explicación detallada de cada macro:

| URL base de AppsFlyer | Nota | Offerslook |
| --- | --- | --- |
| http://app.appsflyer.com | Endpoint de AppsFlyer |  |
| id\_aplicación | ID único de la aplicación: valor dinámico que cambia según la aplicación promocionada |  |
| pid= | Nombre de la fuente de medios concatenado con \_int para identificar redes integradas |  |
| c= | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. | `{offer_id}` |

A continuación puedes ver un ejemplo de un enlace de atribución una vez que hayas añadido macros adicionales de Offerslook:

```http
  https://app.appsflyer.com/com.
  
  appsflyer?pid=mediaName_int&
  
  clickid={click_id}&af_siteid={
  
  aff_id}&advertising_id={ga_id}
  
  &idfa={idfa}
```

Para obtener una lista completa de los parámetros de AppsFlyer, haz clic <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">aquí</Anchor>.

Macros disponibles en los enlaces de atribución de AppsFlyer

Las siguientes macros están disponibles para usarlas en el enlace generado:

| **Nombre de la macro** | **Nota** | **Offerslook** |
| --- | --- | --- |
| PID | Nombre de la fuente de medios: lo proporciona AppsFlyer y no debe cambiarse |  |
| C | Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>. |  |
| clickid | El identificador de clics exclusivo de la red de publicidad | `{click_id}` |
| af\_siteid | ID de publisher de Ad network | `{aff_id}` |

<div id="new-macros" />

#### Nuevas macros

El nuevo conjunto de macros añade una serie de parámetros adicionales de forma clara, estandarizada y estructurada. Recomendamos encarecidamente usar estas macros antes de volver a las macros af\_sub1-5.

| **Nombre de la macro** | **Nota** | **Offerslook** |
| --- | --- | --- |
| af\_c\_id | ID de campaña: proporcionado por el anunciante | `{adv_sub1}<br /><br />{adv_sub2}<br /><br />{adv_sub3}` |
| af\_conjunto de anuncios | Nombre del conjunto de anuncios: proporcionado por el anunciante. El conjunto de anuncios es un nivel intermedio en la jerarquía entre **Campaña** y **Anuncio**. |  |
| af\_adset\_id | ID del adset |  |
| af\_anuncio | Nota |  |
| id\_del\_anuncio\_af | Retargeting: Primer inicio después del re-engagement o la reatribución. |  |
| af\_ad\_type | Tipo de anuncio: usa cualquier valor que «describa» el formato del anuncio (por ejemplo: vídeo o banner, tamaño mediano o grande) |  |
| af\_canal | El canal a través del que se distribuyen los anuncios (por ejemplo: YouTube frente a Google Search) |  |
| af\_palabras\_clave | Lista de palabras clave para campañas orientadas a texto |  |
| af\_modelo\_de\_coste | Modelo de costo: actualmente se admite CPI y es el modelo predeterminado. Los valores CPC y CPA también son válidos. | `{pricing_type}` |
| af\_cost\_currency | Código de moneda (ejemplo: USD) | `{currency}` |
| af\_valor\_de\_coste | Valor del coste | `{revenue}` |

**Macros específicas de Android**

| **Nombre de la macro** | **Nota** | **Offerslook** |
| --- | --- | --- |
| android\_id | Dispositivo Android\_id: requiere soporte de ad network | `{android_id}` |
| sha1\_android\_id | Dispositivo Android\_id encriptado con SHA1: requiere soporte de ad network |  |
| advertising\_id | ID de publicidad de Google: requiere soporte de ad network | `{ga_id}` |
| sha1\_advertising\_id | ID de publicidad de Google encriptado con SHA1: requiere soporte de ad network |  |
| af\_r | Solo para fuera de la tienda: URL de redirección de destino |  |
| sha1\_el | Se usa para la atribución de escritorio a móvil: correo electrónico con hashing SHA1; requiere soporte de ad network |  |

**Macros específicas de iOS**

| **Nombre de la macro** | **Nota** | **Offerslook** |
| --- | --- | --- |
| idfa | ID de anunciante de Apple: debe proporcionarse en mayúsculas; requiere soporte de ad network | `{idfa}` |
| sha1\_idfa | ID de anunciante de Apple con hash SHA1: requiere soporte de ad network |  |
| mac | Dirección mac del dispositivo - Requiere soporte de ad network | `{mac}` |
| sha1\_mac | Dirección MAC del dispositivo con hash SHA1: requiere soporte de ad network |  |

<div id="creating-your-install-postbacks" />

## Crear tus postbacks de instalación

A continuación, encontrarás una explicación paso a paso de cómo crear tus postbacks de instalación con la plataforma Offerslook:

1. Crea o selecciona una oferta que use el protocolo Postback con ID de transacción
2. En la sección de detalles de la página de la oferta, haz clic en el enlace con la etiqueta «tracking»
3. Copia la URL del postback que aparece en el campo con la etiqueta postback URL
4. Elimina el parámetro offer\_id y su valor de la URL del postback para convertir un postback específico en un postback global

Postback de instalación global:

`http://{networkname}.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}`

`networkname` es el nombre de dominio que proporciona Offerslook.

**Finalizar tu registro**

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros usando el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de ad Partners <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div data-zendesk-anchors="creating-your-attribution-link=c%C3%B3mo-crear-tu-enlace-de-atribuci%C3%B3n 01JFT1JFND230EFDBRTWNKXKSH=c%C3%B3mo-crear-tu-enlace-de-atribuci%C3%B3n new-macros=nuevas-macros 01JFT1JFP8T3HF5GQBR19YHQW5=nuevas-macros creating-your-install-postbacks=crear-tus-postbacks-de-instalaci%C3%B3n 01JFT1JFP9BMZM99TKDR58FNZP=crear-tus-postbacks-de-instalaci%C3%B3n" />
