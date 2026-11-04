---
title: Guía de tipos de engagement enriquecidos para ad networks
metadata:
  keywords:
    - Advertisers
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2024-10-15T10:54:29Z'
  edited_at: '2026-08-12T12:28:23Z'
  id: 29221265052433
  locale: es
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/es/articles/29221265052433
---
> **En resumen:** Aprende a crear enlaces de atribución de Tipos de Engagement Enriquecidos (EET) para reflejar el espectro completo del engagement de los usuarios y lograr una optimización de campaña precisa y efectiva.

Los tipos de engagement enriquecidos (EET) reflejan todo el espectro de engagement e intencionalidad de los usuarios cuando ven un anuncio o interactúan con él, desde la exposición momentánea hasta la respuesta directa. Este artículo detalla cómo los partners deben reportar los tipos de engagement en los enlaces de atribución de AppsFlyer según cómo los usuarios interactúan con sus anuncios.

<div id="disclaimer" />

> ❗️ **Advertencia**
>
> Este artículo se centra en los aspectos de EET relevantes para los partners. Para aprender qué es EET y obtener información completa al respecto, consulta el artículo sobre <Anchor target="_blank" href="/marketers/es/docs/about-enriched-engagement-types#which-ad-networks-report-enriched-engagement-types">Tipos de Engagement Enriquecidos</Anchor>.

<div id="which-networks-can-report-eet-to-appsflyer" />

## ¿Qué redes pueden reportar EETs a AppsFlyer?

El soporte a engagement enriquecidos estará disponible para las redes que cumplan los criterios Premier, Advance o Engage del programa de partners de AppsFlyer. Estos niveles se refieren a redes que tienen un historial significativo de entrega de tráfico de alta calidad a escala a nuestros clientes comunes, envían datos de engagement de forma transparente y confiable, y están integradas con una amplia gama de servicios de AppsFlyer.

<div id="note" />

> 📘 **Nota:**
>
> Para comenzar a reportar engaged views y engaged clicks, las ad networks deben contactar al soporte de AppsFlyer.

Mira la [lista de redes elegibles para reportar EET](#01JCAT81K2EJNH91YS6NJGMXMB-data-title)

> ❗️ **Advertencia**
>
> Los clics y las impresiones procedentes de redes no permitidas que incluyan el parámetro `af_engagement_type` se rechazarán y no se utilizarán para la atribución.

<div id="engaged-click-or-engaged-view-attribution-flow" />

<Accordion title="Flujo de atribución de engaged clicks o engaged views">

Los siguientes pasos describen el flujo desde la visualización inicial del anuncio hasta la atribución final de un evento de instalación, ya sea a través de un engaged click o un engaged view:

1. La ad networks muestra un anuncio.
2. La ad networks envía una impresión a AppsFlyer con un `af_ad_tran_id` especificado
3. El usuario está interactuando con el anuncio.
4. La ad networks envía un clic o impresión con los parámetros `af_engagement_type`, `af_ad_tran_id`, `af_ad_format`, `af_ad_type`, y opcionalmente con los parámetros `viewability`.
5. AppsFlyer empareja un evento de instalación con el engaged click o engaged view.
6. AppsFlyer atribuye el evento de instalación a la ad networks.

</Accordion>

<div id="parameters-for-reporting-engagement-types-in-attribution-links" />

<Accordion title="Parámetros para reportar sobre los tipos de engagement en los enlaces de atribución">

Las redes pueden informar los tipos de engagement incluyendo los siguientes parámetros en los enlaces de atribución.

* `af_engagement_type`: El tipo de engagement, por ejemplo, `engaged_click`, `click_to_app` o `engaged_view`. Aquí tienes una <Anchor target="_blank" href="/marketers/es/docs/about-enriched-engagement-types#cuáles-son-los-tipos-de-engagement-enriquecido">lista completa de los diferentes tipos de engagement y sus descripciones</Anchor>.
* `af_ad_type`: Tipo de anuncio. Por ejemplo, `rewarded_video`, `interstitial` o `banner`. Aquí tienes <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#af_ad_type">una lista completa de los diferentes tipos de anuncios y sus descripciones</Anchor>.
* `af_ad_format`: El formato del anuncio, por ejemplo, `text`, `image`, `video`, `playable`. Aquí tienes <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#af_ad_format">una lista completa de los diferentes formatos de anuncios y sus descripciones.</Anchor>
* `viewability`: (opcional) Información adicional sobre el engagement, por ejemplo, `af_video_total_length`, `af_ad_time_viewed`, `af_audio_played_length`. Aquí tienes <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#parámetros-de-visibilidad">una lista completa de las diferentes opciones de visibilidad y sus descripciones</Anchor>.
* `af_ad_tran_id`: Un ID de transacción que permite a AppsFlyer verificar un engaged click o engaged view al coincidirlo con una impresión anterior.
* `is_skoverlay=true` o `is_autostore=true` : Identificar engaged views desencadenadas por [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) o instalaciones inline de Android Auto

**Ejemplo de un engaged click**

```http HTTPS
https://app.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_click&af_ad_type=interstitial&af_ad_format=playable&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0
```

**Ejemplo de una engaged view**

```http
https://impression.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_view&af_ad_type=interstitial&af_ad_format=video&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0&af_video_total_length=20&af_video_played_length=15
```

</Accordion>

<div id="user-engagements-to-report-as-engaged-clicks" />

<Accordion title="Interacciones de usuarios para reportar engaged clicks">

Un *engaged click* es un clic que mantiene al usuario en el mismo contexto, interactuando con el anuncio, sin enviarlo a la tienda de aplicaciones ni abrir la aplicación.

A continuación se presentan ejemplos de engagements de usuarios que las ad networks deben informar con el valor del parámetro `af_engagement_type=engaged_click`:

* **Anuncios reproducibles:** Al hacer clic para interactuar con un anuncio jugable, como tocar para jugar un mini-juego o contenido interactivo dentro del anuncio.
* **Engagement social:** Al hacer clic para dar me gusta, comentar o compartir el anuncio en las plataformas de redes sociales, lo que promueve una mayor interacción y una posible viralidad.
* **Redirección:** Al hacer clic para visitar una landing page u otro sitio/página de contenido externo.
* **Anuncio dinámico de producto/catálogo o carrusel**: Al hacer clic para deslizar entre productos.
* **Añadir a la lista de deseos:** Al hacer clic para añadir el producto promocionado a una lista de deseos o a una lista de favoritos dentro de la aplicación o de un sitio web externo.
* **Guardar para más tarde:** Al hacer clic para guardar el anuncio y su contenido para referencia futura, indicando así un interés en volver a visitar el anuncio o explorarlo más a fondo.
* **Marcador o Añadir a colecciones:** Al hacer clic para marcar el anuncio como favorito o agregarlo a una colección seleccionada de la aplicación, se indica la intención de volver a visitar o categorizar el anuncio.
* **Desactivar el silencio del anuncio:** Al hacer clic para habilitar el audio.

**¿Cuándo no reportar engaged clicks a AppsFlyer?**

A continuación se presentan ejemplos de interacciones de usuarios que las ad networks **no** deben informar con el valor del parámetro `engaged_click`.

* **Cerrar anuncios:** Al hacer clic en la “x” o en un indicador similar, se cierra o se descarta el anuncio, lo que demuestra que no hay interés en aumentar el engagement.
* **Saltar anuncio**: Al hacer clic en un botón designado para saltar un anuncio y pasar directamente al contenido deseado, lo que indica que el anuncio no es atractivo ni relevante para el usuario.
* **Reportar anuncio**: Al hacer clic para denunciar el anuncio por motivos como ser ofensivo, engañoso o inapropiado, y expresar tu insatisfacción con el contenido del anuncio.
* **Opción de exclusión o cancelar suscripción**: Al hacer clic para excluirse o cancelar la suscripción a la recepción de anuncios similares en el futuro, expresando el deseo de dejar de interactuar con el anuncio o su categoría.
* **Salir del anuncio:** Hacer clic en un enlace o botón que sale de la experiencia publicitaria actual, llevando al usuario fuera del contexto o landing page anunciada.
* **Silenciar anuncio:** silenciar el sonido de un video.

</Accordion>

<div id="user-engagements-to-report-as-engaged-views" />

<Accordion title="Interacciones de usuarios para reportar engaged views">

Las redes deben informar sobre los engagement de los usuarios con `af_engagement_type=engaged_view` en los siguientes casos:

* **Anuncio saltable:** Los usuarios ven al menos 5 segundos después de que aparece la opción de omitir en un anuncio de video. Si la red no puede medir el número de segundos vistos, entonces:
  * Envía `engaged_view` en vista 2/4 (50% de píxeles vistos) cuando el video dura más de 20 segundos.
  * Envia `engaged_view` al completar (100% video completo) cuando el video sea más corto de 20 segundos
  * El valor del parámetro `af_ad_format` debe ser `video` o `playable`
* **Video recompensado:** El usuario ve un video recompensado en su totalidad. El valor del parámetro `af_ad_type` debe ser `rewarded_video`.
* **Anuncios renderizados por StoreKit:** Los clics en anuncios renderizados por StoreKit ([`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay) o [`SKStore`](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)) no son registrados por los publishers, sino por Apple para la atribución de SKAdNetwork (SKAN). Lo mismo es cierto para las instalaciones inline de Android Auto (autostore).

  Dado que no hay forma de que las ad networks sepan si esos anuncios interactuaron, informan una impresión o clic cada vez que los anuncios aparecen, incluso si no ocurrió ninguna interacción.

  Las redes pueden informar el tipo de engagement `click_to_app` cada vez que aparece el anuncio, pero luego corren el riesgo de tener una tasa de clics muy alta. Lo mismo ocurre con Android con las instalaciones automáticas inline.

  Para mitigar este riesgo, recomendamos informar el tipo de engagement `engaged_view` en su lugar. En este caso de uso, el enlace de atribución debe incluir `is_skoverlay=true` para iOS o `is_autostore=true` para Android.

**¿Cuándo no reportar engaged views a AppsFlyer?**

A continuación se presenta un caso de uso de engagement de usuario que las ad networks **no** deben informar con el valor del parámetro `engaged_view`, sino más bien con el parámetro `view`.

* El usuario ve un anuncio no saltable que no es un video recompensado y no fue superpuesto por un anuncio de `SKOverlay` o `autostore`.

</Accordion>

<div id="01JCAT81K2EJNH91YS6NJGMXMB-data-title" />

<Accordion title="Redes elegibles para reportar EETs">

La lista de redes permitidas incluye partners cuyos eventos de tipo de engagement enriquecido pueden ser procesados por AppsFlyer, con la exclusión de engaged clicks y engaged views. Las redes de esta lista que deseen que AppsFlyer procese sus engaged clicks y engaged views deben contactar al soporte de AppsFlyer. Para saber qué redes ya tienen sus engaged clicks y engaged views procesados por AppsFlyer, consulta el <Anchor target="_blank" href="/marketers/es/docs/about-enriched-engagement-types#qué-redes-pueden-reportar-sobre-view-engaged-y-engaged-clicks">artículo de anunciantes de EET</Anchor>.

<div id="warning-1" />

<div id="warning" />

> ❗️ **Advertencia**
>
> Los clics y las impresiones procedentes de redes no permitidas que incluyan el parámetro `af_engagement_type` se rechazarán y no se utilizarán para la atribución.

| Nombre del partner |
| --- |
| AdColony |
| Adaction |
| Adaction3 |
| Adikteev |
| adjoe GmbH |
| Amazon |
| Amazon DSP |
| AppLovin |
| Appier |
| Appnext |
| Anuncios en la búsqueda de Apple |
| Aura de Unity |
| AWIN |
| Bidease |
| ByteDance Ads China |
| Cauly |
| Criteo |
| Digital Turbine |
| Digital Turbine On Device |
| Fluent |
| Glance |
| Google Ads (Adwords) |
| Google Marketing Platform (DV360/CM360) |
| Hotstar |
| Huawei |
| InMobi DSP |
| ironSource |
| Jampp |
| Josh |
| Kakao |
| Kuaishou |
| Liftoff |
| Linea |
| Meta Ads |
| Mintegral |
| Mistplay |
| Motorola preinstalado |
| Naver |
| Oppo |
| OPPO Global |
| OPPO Store Traffic(Global) |
| OPPOPAI preinstalado |
| Paytm |
| Rakuten |
| Reddit |
| Remerge |
| RevX |
| Samsung |
| Smadex |
| Snapchat |
| StackAdapt |
| Tapjoy |
| Tencent AMS |
| TikTok for Business: SRN avanzada |
| TikTok for Business: Legacy |
| The Trade Desk |
| Transsion |
| Treasure Data |
| Truecaller |
| Unity Ads |
| Vivo Preload |
| vivo Global |
| Vungle |
| X Ads (anteriormente Twitter Ads) |
| Xiaomi Global |
| XiaomiPAI preinstalado |
| Yahoo Japón |
| Yandex |
| YouAppi |

</Accordion>

<div data-zendesk-anchors="01JA7WZH43ECDKRC0R0J89ED1E=advertencia which-networks-can-report-eet-to-appsflyer=qu%C3%A9-redes-pueden-reportar-eets-a-appsflyer h_01JJPVYGWZSFSATZ4TH5VBSVXW=qu%C3%A9-redes-pueden-reportar-eets-a-appsflyer 01JAN5JRM56C6S6EP27WFJ2Y4W=nota h_01J00XFV133YYAB7YPQNXM5R37=advertencia-2 01JA7WZH46RJBG996NG9EZV7T9=engaged-click-or-engaged-view-attribution-flow 01JA7WZH4BZVGS9Z1NNHQC72N6=parameters-for-reporting-engagement-types-in-attribution-links 01JA7WZH4JDJFCVT25WJ4GNE20=user-engagements-to-report-as-engaged-clicks 01JA7WZH4Q32TEWM5EKME142R7=user-engagements-to-report-as-engaged-views 01JCAT81K2EJNH91YS6NJGMXMB%20data-title%3D=01JCAT81K2EJNH91YS6NJGMXMB-data-title allowed-network-list=01JCAT81K2EJNH91YS6NJGMXMB-data-title h_01JJPVYGWZ4T6TPFRWTR2AB027=advertencia-2" />
